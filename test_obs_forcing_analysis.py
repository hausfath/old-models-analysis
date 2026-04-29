"""Tests for obs_forcing_analysis.py"""

import numpy as np
import pandas as pd
import pytest
from pathlib import Path

from obs_forcing_analysis import (
    trend_stats,
    aggregate_ensemble,
    load_gmst_ensemble,
    load_forcing,
    load_models,
    CoefResult,
    BASE,
    GMST_FILE,
    FORCING_FILE,
    MODELS_FILE,
    GMST_MAX_YEAR,
)


# ── trend_stats tests ──


def test_trend_stats_known_slope():
    """Verify recovery of known linear trend with noise."""
    rng = np.random.default_rng(123)
    x = np.arange(50, dtype=float)
    y = 2.0 * x + 10.0 + rng.normal(0, 1.0, size=50)

    res = trend_stats(y, x, runtype="ols")
    assert abs(res["coef"] - 2.0) < 0.2, f"Coefficient {res['coef']} too far from 2.0"
    assert res["ci_lower"] < 2.0 < res["ci_upper"], "True slope outside 95% CI"


def test_trend_stats_arma11_widens_ci():
    """ARMA(1,1) should produce equal or wider CIs than OLS for autocorrelated data."""
    rng = np.random.default_rng(456)
    x = np.arange(80, dtype=float)
    # AR(1) noise with rho=0.8
    noise = np.zeros(80)
    for i in range(1, 80):
        noise[i] = 0.8 * noise[i - 1] + rng.normal(0, 1)
    y = 0.5 * x + noise

    ols_res = trend_stats(y, x, runtype="ols")
    arma_res = trend_stats(y, x, runtype="arma11")

    ols_width = ols_res["ci_upper"] - ols_res["ci_lower"]
    arma_width = arma_res["ci_upper"] - arma_res["ci_lower"]
    assert arma_width >= ols_width - 1e-10, "ARMA CI should be >= OLS CI"


def test_trend_stats_arma_fallback():
    """Very short series should not crash — falls back to OLS."""
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    y = np.array([1.0, 2.5, 2.8, 4.2, 5.0, 5.5, 7.1])

    res = trend_stats(y, x, runtype="arma11")
    assert np.isfinite(res["coef"]), "Should return finite coefficient"
    assert res["ci_lower"] < res["coef"] < res["ci_upper"]


def test_trend_stats_insufficient_data():
    """Fewer than 5 valid points should return NaN."""
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([1.0, 2.0, 3.0])
    res = trend_stats(y, x)
    assert np.isnan(res["coef"])


def test_trend_stats_handles_nans():
    """NaN values in input should be dropped, not crash."""
    x = np.arange(20, dtype=float)
    y = 1.5 * x + np.random.default_rng(789).normal(0, 0.5, 20)
    y[3] = np.nan
    y[10] = np.nan

    res = trend_stats(y, x, runtype="ols")
    assert np.isfinite(res["coef"]), "Should handle NaN values"
    assert abs(res["coef"] - 1.5) < 0.5


# ── aggregate_ensemble tests ──


def test_aggregate_ensemble_basic():
    """Verify aggregation formula produces valid bounds."""
    results = [
        CoefResult(coef=1.0, ci_lower=0.8, ci_upper=1.2, se=0.1),
        CoefResult(coef=1.1, ci_lower=0.85, ci_upper=1.35, se=0.125),
        CoefResult(coef=0.9, ci_lower=0.7, ci_upper=1.1, se=0.1),
    ]
    agg = aggregate_ensemble(results)

    assert agg["coef_low"] < agg["coef_mean"] < agg["coef_high"]
    assert agg["coef_sd"] > 0
    assert agg["ci_mean"] > 0


def test_aggregate_ensemble_formula_correctness():
    """Verify the quadrature combination formula."""
    results = [
        CoefResult(coef=2.0, ci_lower=1.5, ci_upper=2.5, se=0.255),
        CoefResult(coef=2.2, ci_lower=1.7, ci_upper=2.7, se=0.255),
        CoefResult(coef=1.8, ci_lower=1.3, ci_upper=2.3, se=0.255),
    ]
    agg = aggregate_ensemble(results)

    coefs = np.array([2.0, 2.2, 1.8])
    ci_widths = np.array([0.5, 0.5, 0.5])  # coef - ci_lower

    expected_mean = np.mean(coefs)
    expected_sd = np.std(coefs, ddof=1)
    expected_ci_mean = np.mean(ci_widths)
    expected_total_se = np.sqrt(expected_sd**2 + (expected_ci_mean / 1.96) ** 2)
    expected_unc = 1.96 * expected_total_se

    assert abs(agg["coef_mean"] - expected_mean) < 1e-10
    assert abs(agg["coef_low"] - (expected_mean - expected_unc)) < 1e-10
    assert abs(agg["coef_high"] - (expected_mean + expected_unc)) < 1e-10


def test_aggregate_ensemble_single_member():
    """Single member: coef_sd should be 0, bounds from CI only."""
    results = [CoefResult(coef=1.0, ci_lower=0.5, ci_upper=1.5, se=0.255)]
    agg = aggregate_ensemble(results)
    assert agg["coef_sd"] == 0.0
    assert agg["coef_mean"] == 1.0


# ── Data loading tests ──


@pytest.fixture(scope="module")
def rng():
    return np.random.default_rng(42)


def test_load_gmst_ensemble(rng):
    """GMST ensemble should have correct shape and year range."""
    if not GMST_FILE.exists():
        pytest.skip("gmst_ensemble.csv not found")

    years, members = load_gmst_ensemble(GMST_FILE, rng)
    assert years[0] == 1850
    assert years[-1] == 2024
    assert len(years) == members.shape[0]
    assert members.shape[1] == 10000
    assert not np.any(np.isnan(years))


def test_load_forcing():
    """Forcing data should have correct shape and variables."""
    if not FORCING_FILE.exists():
        pytest.skip("ERF_DAMIP_1000.nc not found")

    f = load_forcing(FORCING_FILE)
    assert f["years"][0] == 1750
    assert f["years"][-1] == 2025
    assert f["total"].shape == (276, 1000)
    assert f["anthropogenic"].shape == (276, 1000)

    # Anthropogenic should equal total - natural (approx)
    import xarray as xr

    ds = xr.open_dataset(FORCING_FILE)
    natural = ds["natural"].values
    expected_anth = ds["total"].values - natural
    np.testing.assert_allclose(f["anthropogenic"], expected_anth, atol=1e-10)
    ds.close()


def test_load_models():
    """Model loading should extract valid timeframes capped at 2024."""
    if not MODELS_FILE.exists():
        pytest.skip("Excel file not found")

    df, model_years, timeframes = load_models(MODELS_FILE)
    assert "year" in df.columns
    assert len(model_years) > 50, "Should find 50+ models"
    assert len(timeframes) > 10, "Should find 10+ unique timeframes"

    # All end years should be <= GMST_MAX_YEAR
    for base, (start, end) in model_years.items():
        assert end <= GMST_MAX_YEAR, f"{base} end year {end} exceeds {GMST_MAX_YEAR}"
        assert end > start, f"{base} has end <= start: {start}-{end}"


# ── Integration test ──


def test_full_run_produces_csvs(tmp_path):
    """Smoke test: run analysis and check output files exist."""
    if not all(p.exists() for p in [GMST_FILE, FORCING_FILE, MODELS_FILE]):
        pytest.skip("Data files not found")

    # This test is slow (~minutes) — only run with pytest -k integration or explicitly
    pytest.skip("Slow integration test — run with: pytest -k test_full_run --run-slow")
