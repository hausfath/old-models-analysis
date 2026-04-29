#!/usr/bin/env python3
"""
Obs forcing trend analysis
==========================
Compares observed temperature warming with radiative forcing estimates
across ~120+ historical climate models (1896-2024).

Outputs four CSVs:
  1. obs_time_trends.csv        — observed temperature trends vs time
  2. obs_forcing_trends.csv     — observed temperature vs forcing relationship
  3. new_model_trends.csv       — model trends (vs time & vs forcing)
  4. model_obs_time_diffs.csv   — trends in model-observation differences

Data sources:
  - common_history_1750-2024.nc      (841-member anthropogenic forcing ensemble)
  - gmst_ensemble.csv               (10,000-member GMST ensemble, Thorne et al 2026)
  - Forcing and temperature time series.xlsx  (model _T/_F predictions)
"""

from __future__ import annotations

import argparse
import re
import warnings
from pathlib import Path
from typing import Literal, Sequence, TypedDict

import numpy as np
import pandas as pd
import xarray as xr
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tools.sm_exceptions import ConvergenceWarning
from tqdm import tqdm

# ────────────────────────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────────────────────────
BASE = Path(__file__).parent

FORCING_FILE = BASE / "common_history_1750-2024.nc"
GMST_FILE = BASE / "gmst_ensemble.csv"
MODELS_FILE = BASE / "Forcing and temperature time series.xlsx"

ALPHA = 0.05  # 95% CIs
N_GMST_SAMPLE = 200  # GMST members for obs-only & model-obs sections
N_PAIRS = 500  # random (GMST, forcing) pairs for obs-vs-forcing
FORCING_TYPES = ("anthropogenic",)  # common_history is anthropogenic-only
GMST_MAX_YEAR = 2024  # GMST ensemble ends here

# Suppress SARIMAX startup warnings
warnings.filterwarnings(
    "ignore", message="Non-invertible starting MA parameters", module="statsmodels"
)
warnings.filterwarnings(
    "ignore", message="Non-stationary starting", module="statsmodels"
)

# ────────────────────────────────────────────────────────────
# Statistical functions
# ────────────────────────────────────────────────────────────
class CoefResult(TypedDict):
    coef: float
    ci_lower: float
    ci_upper: float
    se: float


_ARIMA_ORDER = {"ols": None, "ar1": (1, 0, 0), "arma11": (1, 0, 1)}


def _extract_ci(res, param: int) -> tuple[float, float]:
    """Extract confidence interval bounds for parameter index `param`."""
    ci = res.conf_int(alpha=ALPHA)
    if hasattr(ci, "iloc"):
        return float(ci.iloc[param, 0]), float(ci.iloc[param, 1])
    return float(ci[param, 0]), float(ci[param, 1])


def trend_stats(
    y: Sequence[float] | np.ndarray,
    x: Sequence[float] | np.ndarray,
    runtype: Literal["ols", "ar1", "arma11"] = "arma11",
) -> CoefResult:
    """
    OLS trend slope with autocorrelation-corrected 95% CI.

    Uses a conservative heuristic: keeps the OLS point estimate but widens
    the CI to max(OLS_CI, ARMA_CI) when the ARMA model gives wider intervals.
    This accounts for autocorrelation inflating standard errors without
    discarding the OLS coefficient (which is unbiased for the trend).
    """
    y_arr, x_arr = np.asarray(y, dtype=float), np.asarray(x, dtype=float)

    # Drop any paired NaN values
    valid = np.isfinite(y_arr) & np.isfinite(x_arr)
    if valid.sum() < 5:
        return CoefResult(coef=np.nan, ci_lower=np.nan, ci_upper=np.nan, se=np.nan)
    y_arr, x_arr = y_arr[valid], x_arr[valid]

    ols = sm.OLS(y_arr, sm.add_constant(x_arr)).fit()
    coef = float(ols.params[1])
    low, up = _extract_ci(ols, 1)

    if runtype != "ols":
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=ConvergenceWarning)
                ar = ARIMA(y_arr, exog=x_arr, order=_ARIMA_ORDER[runtype]).fit()
            ar_low, ar_up = _extract_ci(ar, 1)
            if (ar_up - ar_low) > (up - low):
                # Shift ARMA CI to center on OLS coefficient
                shift = coef - float(ar.params[1])
                low, up = ar_low + shift, ar_up + shift
        except (np.linalg.LinAlgError, ValueError, RuntimeError):
            pass  # Keep OLS CI on failure

    se = (up - low) / (2 * 1.96)
    return CoefResult(coef=coef, ci_lower=low, ci_upper=up, se=se)


def aggregate_ensemble(results: list[CoefResult]) -> dict:
    """
    Aggregate trend results across ensemble members.

    Combines two independent uncertainty sources in quadrature:
      - coef_sd: spread of point estimates across ensemble members
      - ci_mean / 1.96: typical regression SE (within each member)

    Returns 95% uncertainty bounds: coef_mean +/- 1.96 * total_se
    """
    coefs = np.array([r["coef"] for r in results if np.isfinite(r["coef"])])
    ci_widths = np.array(
        [r["coef"] - r["ci_lower"] for r in results if np.isfinite(r["coef"])]
    )

    coef_mean = float(np.mean(coefs))
    coef_sd = float(np.std(coefs, ddof=1)) if len(coefs) > 1 else 0.0
    ci_mean = float(np.mean(ci_widths))

    # Combine ensemble spread and regression SE in quadrature
    total_se = np.sqrt(coef_sd**2 + (ci_mean / 1.96) ** 2)
    unc = 1.96 * total_se

    return {
        "coef_mean": coef_mean,
        "coef_sd": coef_sd,
        "ci_mean": ci_mean,
        "coef_low": coef_mean - unc,
        "coef_high": coef_mean + unc,
    }


# ────────────────────────────────────────────────────────────
# Data loading
# ────────────────────────────────────────────────────────────
def load_gmst_ensemble(
    path: Path, rng: np.random.Generator
) -> tuple[np.ndarray, np.ndarray]:
    """
    Load GMST ensemble (Thorne et al 2026).

    Returns:
        years: 1D array of integer years (1850-2024)
        members: 2D array (n_years, 10000) — all members
    """
    df = pd.read_csv(path, header=None)
    years = df.iloc[:, 0].values.astype(int)
    members = df.iloc[:, 1:].values  # (n_years, 10000)
    return years, members


def sample_gmst(
    members: np.ndarray, n_sample: int, rng: np.random.Generator
) -> np.ndarray:
    """Randomly sample n_sample columns from the full GMST ensemble."""
    n_total = members.shape[1]
    idx = rng.choice(n_total, size=n_sample, replace=False)
    return members[:, idx]


def load_forcing(path: Path) -> dict:
    """
    Load common_history_1750-2024.nc anthropogenic forcing ensemble.

    The file has timebounds (276 year edges 1750-2025) and a single variable
    with shape (276, 1, 841). We compute mid-year values (275 mid-points)
    by averaging adjacent time-edge values.

    Returns dict with:
        years: 1D int array of mid-years (1750-2024, length 275)
        anthropogenic: 2D array (275, 841) — anthropogenic ERF
    """
    ds = xr.open_dataset(path)
    var_name = list(ds.data_vars)[0]
    da = ds[var_name].squeeze()  # drop singleton scenario dim -> (276, 841)

    edges = ds["timebounds"].values  # 276 year edges
    mid_years = (0.5 * (edges[:-1] + edges[1:])).astype(int)  # 275 mid-points

    # Mid-point forcing values (average adjacent edges)
    rf = 0.5 * (da[:-1, :].values + da[1:, :].values)  # (275, 841)

    ds.close()
    return {"years": mid_years, "anthropogenic": rf}


def load_models(path: Path) -> tuple[pd.DataFrame, dict[str, tuple[int, int]], list]:
    """
    Load model predictions from Excel file.

    Returns:
        df: DataFrame with Year and model _T/_F columns
        model_years: {base_name: (start_year, end_year)} — end capped at GMST_MAX_YEAR
        timeframes: sorted list of unique (start, end) tuples
    """
    df = pd.read_excel(path, engine="openpyxl")
    df.columns = [c.strip().lower() if isinstance(c, str) else c for c in df.columns]

    # Parse model metadata from column names
    strip_suffix = lambda s: re.sub(r"_(?:f|t)$", "", s)
    model_years: dict[str, tuple[int, int]] = {}

    for col in df.columns:
        if not isinstance(col, str) or not col.endswith("_t"):
            continue
        base = strip_suffix(col)
        m = re.search(r"_(\d{4})(?!\d)", base)
        if not m:
            continue
        pub_year = int(m.group(1))
        valid_years = df.loc[df[col].notna(), "year"]
        if valid_years.empty:
            continue
        start = int(valid_years.min())
        end = min(int(valid_years.max()), GMST_MAX_YEAR)
        if end > start:
            model_years[base] = (start, end)

    timeframes = sorted(set(model_years.values()))
    return df, model_years, timeframes


# ────────────────────────────────────────────────────────────
# Section 1: Obs-only time trends
# ────────────────────────────────────────────────────────────
def compute_obs_time_trends(
    gmst_years: np.ndarray,
    gmst_sample: np.ndarray,
    timeframes: list[tuple[int, int]],
) -> pd.DataFrame:
    """Regress each GMST ensemble member against year for each timeframe."""
    rows = []
    for start, end in tqdm(timeframes, desc="Obs time trends"):
        mask = (gmst_years >= start) & (gmst_years <= end)
        yrs = gmst_years[mask].astype(float)
        temps = gmst_sample[mask, :]  # (n_years_window, n_members)

        results = []
        for j in range(temps.shape[1]):
            results.append(trend_stats(temps[:, j], yrs, "arma11"))

        agg = aggregate_ensemble(results)
        agg["timeframe"] = f"{start}-{end}"
        rows.append(agg)

    return pd.DataFrame(rows)


# ────────────────────────────────────────────────────────────
# Section 2: Obs-vs-forcing trends
# ────────────────────────────────────────────────────────────
def compute_obs_forcing_trends(
    gmst_years: np.ndarray,
    gmst_all: np.ndarray,
    forcing: dict,
    timeframes: list[tuple[int, int]],
    n_pairs: int,
    rng: np.random.Generator,
) -> pd.DataFrame:
    """Regress GMST against forcing for random (GMST, forcing) pairs."""
    n_gmst_total = gmst_all.shape[1]
    # Get forcing member count from first available forcing type
    first_ftype = FORCING_TYPES[0]
    n_forcing_total = forcing[first_ftype].shape[1]

    # Pre-draw all random pairs
    gmst_idx = rng.choice(n_gmst_total, size=n_pairs, replace=True)
    forcing_idx = rng.choice(n_forcing_total, size=n_pairs, replace=True)

    rows = []
    combos = [(tf, ft) for tf in timeframes for ft in FORCING_TYPES]
    for (start, end), ftype in tqdm(combos, desc="Obs-forcing trends"):
        # GMST year mask
        g_mask = (gmst_years >= start) & (gmst_years <= end)
        yrs_gmst = gmst_years[g_mask]

        # Forcing year mask (aligned to same integer years)
        f_mask = (forcing["years"] >= start) & (forcing["years"] <= end)
        yrs_forc = forcing["years"][f_mask]

        # Find overlapping years
        common_years = np.intersect1d(yrs_gmst, yrs_forc)
        if len(common_years) < 5:
            continue

        g_idx = np.isin(gmst_years, common_years)
        f_idx = np.isin(forcing["years"], common_years)

        forcing_data = forcing[ftype][f_idx, :]  # (n_common, 1000)
        gmst_data = gmst_all[g_idx, :]  # (n_common, 10000)

        results = []
        for k in range(n_pairs):
            y = gmst_data[:, gmst_idx[k]]
            x = forcing_data[:, forcing_idx[k]]
            results.append(trend_stats(y, x, "arma11"))

        agg = aggregate_ensemble(results)
        agg["timeframe"] = f"{start}-{end}"
        agg["forcing_type"] = ftype
        rows.append(agg)

    return pd.DataFrame(rows)


# ────────────────────────────────────────────────────────────
# Section 3: Model trends (vs time & vs own forcing)
# ────────────────────────────────────────────────────────────
def compute_model_trends(
    models_df: pd.DataFrame,
    model_years: dict[str, tuple[int, int]],
) -> pd.DataFrame:
    """Compute temperature vs year and temperature vs forcing for each model."""
    rows = []
    for base, (start, end) in tqdm(model_years.items(), desc="Model trends"):
        mask = models_df["year"].between(start, end)
        yrs = models_df.loc[mask, "year"].values.astype(float)

        t_col = f"{base}_t"
        f_col = f"{base}_f"

        if t_col not in models_df.columns:
            continue

        temps = models_df.loc[mask, t_col].values

        # (a) Temperature vs year
        res_time = trend_stats(temps, yrs, "arma11")
        rows.append({
            "model": base,
            "timeframe": f"{start}-{end}",
            "dtype": "model_time",
            "coef": res_time["coef"],
            "ci_lower": res_time["ci_lower"],
            "ci_upper": res_time["ci_upper"],
            "se": res_time["se"],
        })

        # (b) Temperature vs model forcing
        if f_col in models_df.columns:
            forc = models_df.loc[mask, f_col].values
            if np.any(np.isfinite(forc)):
                res_forc = trend_stats(temps, forc, "arma11")
                rows.append({
                    "model": base,
                    "timeframe": f"{start}-{end}",
                    "dtype": "model_forcing",
                    "coef": res_forc["coef"],
                    "ci_lower": res_forc["ci_lower"],
                    "ci_upper": res_forc["ci_upper"],
                    "se": res_forc["se"],
                })

    return pd.DataFrame(rows)


# ────────────────────────────────────────────────────────────
# Section 4: Model–obs difference trends
# ────────────────────────────────────────────────────────────
def compute_model_obs_diffs(
    models_df: pd.DataFrame,
    model_years: dict[str, tuple[int, int]],
    gmst_years: np.ndarray,
    gmst_sample: np.ndarray,
) -> pd.DataFrame:
    """
    Trend in (model - obs) difference over time.

    Note: coef_sd reflects only GMST observational uncertainty,
    not model structural uncertainty.
    """
    rows = []
    for base, (start, end) in tqdm(model_years.items(), desc="Model-obs diffs"):
        t_col = f"{base}_t"
        if t_col not in models_df.columns:
            continue

        mask = models_df["year"].between(start, end)
        model_yrs = models_df.loc[mask, "year"].values
        model_temps = models_df.loc[mask, t_col].values

        # Find common years with GMST
        common = np.intersect1d(model_yrs, gmst_years)
        if len(common) < 5:
            continue

        m_idx = np.isin(model_yrs, common)
        g_idx = np.isin(gmst_years, common)

        model_t = model_temps[m_idx]
        gmst_sub = gmst_sample[g_idx, :]
        yrs = common.astype(float)

        results = []
        for j in range(gmst_sub.shape[1]):
            diff = model_t - gmst_sub[:, j]
            results.append(trend_stats(diff, yrs, "arma11"))

        agg = aggregate_ensemble(results)
        agg["model"] = base
        agg["timeframe"] = f"{start}-{end}"
        rows.append(agg)

    return pd.DataFrame(rows)


# ────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────
def main(seed: int = 42):
    rng = np.random.default_rng(seed)

    # Load data
    print("Loading data...")
    gmst_years, gmst_all = load_gmst_ensemble(GMST_FILE, rng)
    gmst_sample = sample_gmst(gmst_all, N_GMST_SAMPLE, rng)
    forcing = load_forcing(FORCING_FILE)
    models_df, model_years, timeframes = load_models(MODELS_FILE)

    print(
        f"  GMST: {gmst_all.shape[1]} members, {len(gmst_years)} years "
        f"({gmst_years[0]}-{gmst_years[-1]})"
    )
    print(
        f"  Forcing: {forcing['anthropogenic'].shape[1]} members, "
        f"{len(forcing['years'])} years ({forcing['years'][0]}-{forcing['years'][-1]})"
    )
    print(f"  Models: {len(model_years)} models, {len(timeframes)} timeframes")

    # Section 1: Obs-only time trends
    print("\n[1/4] Obs-only time trends...")
    obs_time = compute_obs_time_trends(gmst_years, gmst_sample, timeframes)
    obs_time.to_csv(BASE / "obs_time_trends.csv", index=False)
    print(f"  Wrote obs_time_trends.csv ({len(obs_time)} rows)")

    # Section 2: Obs-vs-forcing trends
    print("\n[2/4] Obs-vs-forcing trends...")
    obs_forcing = compute_obs_forcing_trends(
        gmst_years, gmst_all, forcing, timeframes, N_PAIRS, rng
    )
    obs_forcing.to_csv(BASE / "obs_forcing_trends.csv", index=False)
    print(f"  Wrote obs_forcing_trends.csv ({len(obs_forcing)} rows)")

    # Section 3: Model trends
    print("\n[3/4] Model trends...")
    model_trends = compute_model_trends(models_df, model_years)
    model_trends.to_csv(BASE / "new_model_trends.csv", index=False)
    print(f"  Wrote new_model_trends.csv ({len(model_trends)} rows)")

    # Section 4: Model-obs differences
    print("\n[4/4] Model-obs difference trends...")
    model_diffs = compute_model_obs_diffs(
        models_df, model_years, gmst_years, gmst_sample
    )
    model_diffs.to_csv(BASE / "model_obs_time_diffs.csv", index=False)
    print(f"  Wrote model_obs_time_diffs.csv ({len(model_diffs)} rows)")

    print("\nDone — all four CSVs written.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obs forcing trend analysis")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    args = parser.parse_args()
    main(seed=args.seed)
