# Historical Climate Model Evaluation

Trend analysis comparing observed temperature warming with radiative forcing estimates across 149 historical climate models (1896--2024). This is an update to [Hausfather et al. (2020)](https://doi.org/10.1029/2019GL085378), extending the analysis through 2024 with updated data and statistical methods.

## Overview

The analysis regresses observed global mean surface temperature (GMST) against anthropogenic radiative forcing to compute implied transient climate response (TCR) for each historical model's valid data window. It also compares model-projected warming rates against observations.

## Quick Start

```bash
# Install dependencies
pip install numpy pandas xarray statsmodels openpyxl tqdm matplotlib

# Run the trend analysis (produces 4 output CSVs, ~15 min)
python obs_forcing_analysis.py

# Generate all 6 figures
python plot_obs_forcing.py

# Run tests
pytest test_obs_forcing_analysis.py -v
```

## Input Data

| File | Description | Size |
|------|-------------|------|
| `common_history_1750-2024.nc` | 841-member anthropogenic forcing ensemble (1750--2024) | 1.8 MB |
| `gmst_ensemble.csv` | 10,000-member GMST ensemble (Thorne et al. 2026 approach), 1850--2024 | 13 MB |
| `Forcing and temperature time series.xlsx` | Model temperature (\_T) and forcing (\_F) predictions for 149 models | 184 KB |

## Scripts

### `obs_forcing_analysis.py`
Main analysis script. Produces four output CSVs:

1. **`obs_time_trends.csv`** -- Observed GMST trends vs. time for each model-defined timeframe. Uses 200 subsampled GMST ensemble members with ARMA(1,1) autocorrelation-corrected confidence intervals.

2. **`obs_forcing_trends.csv`** -- Observed GMST vs. anthropogenic forcing sensitivity. Uses 500 random (GMST member, forcing member) pairs per timeframe.

3. **`new_model_trends.csv`** -- Model trends: temperature vs. year and temperature vs. model's own forcing for each of 149 models.

4. **`model_obs_time_diffs.csv`** -- Trends in the difference between each model's temperature projection and observed GMST.

Options:
- `--seed N` -- Set random seed for reproducibility (default: 42)

### `plot_obs_forcing.py`
Generates 6 publication-quality figures in `figures/`:

| Figure | File | Description |
|--------|------|-------------|
| 1 | `implied_tcr_with_ci.png` | Implied TCR for each model vs. observed, with 95% CIs |
| 2 | `model_spaghetti.png` | All model projections aligned to observations |
| 3 | `model_quantile_envelope.png` | Model ensemble median and 5--95% range vs. observed |
| 4 | `warming_rate_comparison.png` | Warming rates (C/decade), color-coded by publication era |
| 5 | `model_accuracy_over_time.png` | Model/observed warming rate ratio vs. publication year |
| 6 | `forcing_comparison.png` | Model vs. observed anthropogenic forcing rates |

### `test_obs_forcing_analysis.py`
Unit tests for statistical functions, data loading, and output validation.

## Methods

### Statistical Approach
- **Regression**: OLS with ARMA(1,1) autocorrelation correction. Uses a conservative heuristic: keeps the OLS point estimate but widens the confidence interval to max(OLS CI, ARMA CI).
- **Uncertainty propagation**: Combines across-ensemble spread (SD) with within-regression standard error in quadrature: `1.96 * sqrt(coef_sd^2 + (ci_mean/1.96)^2)`.
- **TCR calculation**: Implied TCR = regression coefficient (C per W/m^2) x 3.7 W/m^2 (forcing at 2xCO2).

### Ensemble Sampling
- **GMST uncertainty**: 200 randomly subsampled members from the 10,000-member ensemble for obs-only trends and model--obs differences; 500 random pairs for obs-vs-forcing regressions.
- **Forcing uncertainty**: 841-member anthropogenic forcing ensemble from common_history dataset.
- **Reproducibility**: All random sampling uses a fixed seed (default: 42).

### Model Alignment (for time series figures)
Each model is aligned to a LOWESS-smoothed observational time series at the model's publication year, using the mean offset over a 5-year window.

## Models

The analysis includes 149 model variants spanning 1896--2007, from Arrhenius (1896) through IPCC AR4 (2007). Models with lower/median/upper variants are grouped by root name for visualization, with the median used as the central estimate.

## References

- Hausfather, Z., Drake, H. F., Abbott, T., & Schmidt, G. A. (2020). Evaluating the performance of past climate model projections. *Geophysical Research Letters*, 47(1), e2019GL085378.
