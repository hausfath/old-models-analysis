#!/usr/bin/env python3
"""
Visualization for obs forcing trend analysis.
Produces 6 publication-quality figures from the CSV outputs
of obs_forcing_analysis.py plus raw input data.
"""

from __future__ import annotations

import re
import warnings
from pathlib import Path

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
from statsmodels.nonparametric.smoothers_lowess import lowess

from obs_forcing_analysis import trend_stats

# ────────────────────────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────────────────────────
BASE = Path(__file__).parent

# Input CSVs (from obs_forcing_analysis.py)
OBS_TIME_CSV = BASE / "obs_time_trends.csv"
OBS_FORCING_CSV = BASE / "obs_forcing_trends.csv"
MODEL_TRENDS_CSV = BASE / "new_model_trends.csv"
MODEL_DIFFS_CSV = BASE / "model_obs_time_diffs.csv"

# Raw data files
MODELS_FILE = BASE / "Forcing and temperature time series.xlsx"
GMST_FILE = BASE / "gmst_ensemble.csv"
FORCING_FILE = BASE / "common_history_1750-2024.nc"

YEAR_MIN, YEAR_MAX = 1938, 2024
LOESS_FRAC = 0.20
F_2xCO2 = 3.7  # W/m2 forcing at 2xCO2

# Variant tokens for grouping model lower/median/upper.
# "a"/"b"/"1"/"2" are *not* variants — they identify distinct scenarios
# (e.g. machta_1972_a vs machta_1972_b are separate models).
VARIANT_TOKENS = ("lower", "median", "upper", "average", "mean")
CENTRAL_PRIORITY = ("median", "average", "mean", "")
YEAR_RE = re.compile(r"_(\d{4})(?!\d)")

# Era color palette
ERA_COLORS = {
    "pre-1970": "#2166ac",
    "1970s": "#4393c3",
    "1980s": "#f4a582",
    "1990+": "#b2182b",
}
ERA_LABELS = list(ERA_COLORS.keys())
OBS_COLOR = "#333333"

plt.rcParams.update({
    "axes.labelsize": 11,
    "axes.titlesize": 13,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "figure.dpi": 150,
})


# ────────────────────────────────────────────────────────────
# Shared helpers
# ────────────────────────────────────────────────────────────
def era_color(pub_year: int) -> str:
    if pub_year < 1970:
        return ERA_COLORS["pre-1970"]
    if pub_year < 1980:
        return ERA_COLORS["1970s"]
    if pub_year < 1990:
        return ERA_COLORS["1980s"]
    return ERA_COLORS["1990+"]


def pub_year_from_name(name: str) -> int | None:
    m = YEAR_RE.search(name)
    return int(m.group(1)) if m else None


def parse_timeframe(s: str) -> tuple[int, int]:
    years = re.findall(r"\d{4}", str(s))
    return int(years[0]), int(years[1])


def match_obs_row(obs_df: pd.DataFrame, start: int, end: int, forcing_type: str | None = None):
    """Find the obs row matching a given timeframe."""
    mask = obs_df["timeframe"].str.contains(str(start)) & obs_df["timeframe"].str.contains(str(end))
    if forcing_type is not None and "forcing_type" in obs_df.columns:
        mask = mask & (obs_df["forcing_type"] == forcing_type)
    matches = obs_df[mask]
    return matches.iloc[0] if len(matches) > 0 else None


def parse_variants(df: pd.DataFrame, dtype_filter: str) -> pd.DataFrame:
    """
    Group model variants (lower/median/upper) into single rows.
    Returns DataFrame with: root, pub_year, start, end, coef_central,
    coef_low_variant, coef_high_variant, ci_lower, ci_upper.
    """
    sub = df[df["dtype"] == dtype_filter].copy()
    groups: dict[tuple, dict] = {}

    for _, row in sub.iterrows():
        name = row["model"]
        variant = ""
        root = name
        for tok in VARIANT_TOKENS:
            if name.endswith(f"_{tok}"):
                variant = tok
                root = name[: -(len(tok) + 1)]
                break

        start, end = parse_timeframe(row["timeframe"])
        key = (root, start, end)
        groups.setdefault(key, {})
        groups[key][variant] = row

    records = []
    for (root, start, end), vdict in groups.items():
        py = pub_year_from_name(root)
        if py is None:
            continue

        # Pick central variant
        central_row = None
        for tok in CENTRAL_PRIORITY:
            if tok in vdict:
                central_row = vdict[tok]
                break
        if central_row is None:
            continue

        coef_c = central_row["coef"]
        coef_low_v = vdict.get("lower", central_row)["coef"]
        coef_high_v = vdict.get("upper", central_row)["coef"]

        records.append({
            "root": root,
            "pub_year": py,
            "start": start,
            "end": end,
            "coef_central": coef_c,
            "coef_low_variant": coef_low_v,
            "coef_high_variant": coef_high_v,
            "ci_lower": central_row.get("ci_lower", np.nan),
            "ci_upper": central_row.get("ci_upper", np.nan),
        })

    return pd.DataFrame(records).sort_values("pub_year").reset_index(drop=True)


def load_and_align_models():
    """Load Excel models + GMST ensemble, align models to LOWESS-smoothed obs."""
    # Load GMST ensemble mean
    gmst = pd.read_csv(GMST_FILE, header=None)
    gmst_years = gmst.iloc[:, 0].values.astype(int)
    gmst_mean = gmst.iloc[:, 1:].mean(axis=1).values

    # LOWESS smooth
    valid = np.isfinite(gmst_mean)
    sm_vals = lowess(gmst_mean[valid], gmst_years[valid], frac=LOESS_FRAC, return_sorted=False)
    obs_lowess = np.full_like(gmst_mean, np.nan)
    obs_lowess[valid] = sm_vals

    # Load model data from Excel
    mdf = pd.read_excel(MODELS_FILE, engine="openpyxl")
    mdf.columns = [c.strip().lower() if isinstance(c, str) else c for c in mdf.columns]

    # Filter to YEAR_MIN-YEAR_MAX
    year_mask = (mdf["year"] >= YEAR_MIN) & (mdf["year"] <= YEAR_MAX)
    mdf = mdf[year_mask].copy()
    gmst_mask = (gmst_years >= YEAR_MIN) & (gmst_years <= YEAR_MAX)
    plot_years = gmst_years[gmst_mask]
    plot_obs = gmst_mean[gmst_mask]
    plot_lowess = obs_lowess[gmst_mask]

    # Select _T columns, prefer median > average > base
    temp_cols = [c for c in mdf.columns if isinstance(c, str) and c.endswith("_t")
                 and not c.endswith(("_lower_t", "_upper_t"))
                 and not c.endswith("_f")]

    # Strip optional "_median"/"_average" plus the required "_t" suffix.
    # The previous pattern required "_<group>_t" with group optional, which
    # silently failed for plain "_t" columns (callendar_1938_t, plass_*_t, etc.)
    # and dropped them from the figure.
    seen_bases = set()
    selected = []
    for col in sorted(temp_cols):
        base = re.sub(r"(?:_(median|average))?_t$", "", col, flags=re.I)
        if base in seen_bases:
            continue
        for pref in [f"{base}_median_t", f"{base}_average_t", f"{base}_t"]:
            if pref in mdf.columns:
                selected.append(pref)
                seen_bases.add(base)
                break

    # Align each model to LOWESS obs at publication year (or YEAR_MIN if pub
    # predates the obs window — e.g. Arrhenius 1896 aligns at 1938).
    aligned = {}
    for col in selected:
        py = pub_year_from_name(col)
        if py is None:
            continue
        align_year = max(py, YEAR_MIN)

        # 5-year window starting at align_year
        m5_mdf = (mdf["year"] >= align_year) & (mdf["year"] < align_year + 5)
        m5_gmst = (plot_years >= align_year) & (plot_years < align_year + 5)

        if m5_mdf.sum() == 0 or m5_gmst.sum() == 0:
            continue

        obs_mean_5 = np.nanmean(plot_lowess[m5_gmst])
        mod_mean_5 = mdf.loc[m5_mdf, col].mean()
        if np.isnan(obs_mean_5) or np.isnan(mod_mean_5):
            continue

        shift = obs_mean_5 - mod_mean_5
        series = mdf[col].values + shift
        series[mdf["year"].values < align_year] = np.nan
        aligned[col] = series

    return plot_years, plot_obs, aligned


# ────────────────────────────────────────────────────────────
# Figure 1: Implied TCR (staggered, with model CIs)
# ────────────────────────────────────────────────────────────
def fig_implied_tcr():
    df_models = pd.read_csv(MODEL_TRENDS_CSV)
    df_obs = pd.read_csv(OBS_FORCING_CSV)

    res = parse_variants(df_models, "model_forcing")
    if res.empty:
        print("  No model_forcing data found, skipping TCR plot.")
        return

    # Compute TCR = coef * F_2xCO2
    res["tcr_central"] = res["coef_central"] * F_2xCO2
    res["tcr_low_v"] = res["coef_low_variant"] * F_2xCO2
    res["tcr_high_v"] = res["coef_high_variant"] * F_2xCO2

    # Match obs for each model's timeframe
    tcr_obs, ci_obs_low, ci_obs_high = [], [], []
    keep = []
    for _, row in res.iterrows():
        obs_row = match_obs_row(df_obs, row["start"], row["end"], "anthropogenic")
        if obs_row is None:
            keep.append(False)
            tcr_obs.append(np.nan)
            ci_obs_low.append(np.nan)
            ci_obs_high.append(np.nan)
        else:
            keep.append(True)
            t = obs_row["coef_mean"] * F_2xCO2
            tcr_obs.append(t)
            ci_obs_low.append(abs(t - obs_row["coef_low"] * F_2xCO2))
            ci_obs_high.append(abs(obs_row["coef_high"] * F_2xCO2 - t))

    res["tcr_obs"] = tcr_obs
    res["ci_obs_low"] = ci_obs_low
    res["ci_obs_high"] = ci_obs_high
    res = res[keep].reset_index(drop=True)

    # Plot
    fig_height = max(6, 0.26 * len(res))
    fig, ax = plt.subplots(figsize=(8, fig_height))

    ypos = np.arange(len(res))
    offset = 0.2

    # Model points with variant range
    model_err_low = np.abs(res["tcr_central"] - res["tcr_low_v"])
    model_err_high = np.abs(res["tcr_high_v"] - res["tcr_central"])
    ax.errorbar(res["tcr_central"], ypos - offset,
                xerr=[model_err_low, model_err_high],
                fmt="s", capsize=3, color="tab:blue", markersize=4,
                label="Model (central \u00b1 range)")

    # Obs points
    ax.errorbar(res["tcr_obs"], ypos + offset,
                xerr=[res["ci_obs_low"], res["ci_obs_high"]],
                fmt="o", capsize=3, color="tab:orange", markersize=4,
                label="Observed (95% CI)")

    ax.set_yticks(ypos)
    ax.set_yticklabels(res["root"], fontsize=7)
    ax.set_xlabel("Transient warming per CO\u2082 doubling (\u00b0C)")
    ax.axvline(0, ls="--", lw=0.7, color="gray")
    ax.set_title("Implied transient response with 95% CIs\n(each model\u2019s valid data window)")
    ax.legend(loc="upper right", fontsize=8)
    fig.subplots_adjust(left=0.28, right=0.97, top=0.96, bottom=0.04)
    plt.margins(y=0.01)

    out = BASE / "implied_tcr_with_ci.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Figure 2: Spaghetti Plot
# ────────────────────────────────────────────────────────────
def fig_spaghetti():
    plot_years, plot_obs, aligned = load_and_align_models()

    cmap = plt.colormaps.get_cmap("tab20").resampled(max(len(aligned), 20))
    fig, ax = plt.subplots(figsize=(9, 6))

    for idx, (col, series) in enumerate(aligned.items()):
        label = re.sub(r"_(median|average)?_t$", "", col, flags=re.I)
        ax.plot(plot_years, series, lw=0.8, color=cmap(idx % cmap.N), label=label, alpha=0.85)

    ax.plot(plot_years, plot_obs, color="black", lw=2.2, label="Observed")
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature anomaly (\u00b0C)")
    ax.set_title(f"Observed vs. Aligned Model-Projected Temperatures ({YEAR_MIN}\u2013{YEAR_MAX})")
    ax.set_xlim(YEAR_MIN, YEAR_MAX)
    ax.grid(True, ls="--", alpha=0.3)
    ax.legend(loc="upper left", ncol=2, frameon=False, prop={"size": 5.5},
              columnspacing=0.7, labelspacing=0.15, handletextpad=0.3)
    fig.tight_layout()

    out = BASE / "model_spaghetti.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Figure 3: Quantile Envelope
# ────────────────────────────────────────────────────────────
def fig_quantile_envelope():
    plot_years, plot_obs, aligned = load_and_align_models()

    aligned_df = pd.DataFrame(aligned, index=plot_years)
    median = aligned_df.median(axis=1)
    p05 = aligned_df.quantile(0.05, axis=1)
    p95 = aligned_df.quantile(0.95, axis=1)

    valid = median.notna() & p05.notna() & p95.notna()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(plot_years, plot_obs, color="black", lw=2.0, label="Observed")
    ax.fill_between(plot_years[valid], p05[valid], p95[valid],
                    color="tab:blue", alpha=0.22, label="Model 5\u201395% range")
    ax.plot(plot_years[valid], median[valid], color="tab:blue", lw=1.8, label="Model median")

    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature anomaly (\u00b0C)")
    ax.set_title(f"Observed vs. aligned model ensemble (median, 5\u201395%)")
    ax.set_xlim(YEAR_MIN, YEAR_MAX)
    ax.grid(True, ls="--", alpha=0.3)
    ax.legend(frameon=False)
    fig.tight_layout()

    out = BASE / "model_quantile_envelope.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Figure 4: Warming Rate Comparison (color-coded by era)
# ────────────────────────────────────────────────────────────
def fig_warming_rate():
    df_models = pd.read_csv(MODEL_TRENDS_CSV)
    df_obs = pd.read_csv(OBS_TIME_CSV)

    res = parse_variants(df_models, "model_time")
    if res.empty:
        print("  No model_time data found, skipping warming rate plot.")
        return

    # Convert to C/decade
    for col in ["coef_central", "coef_low_variant", "coef_high_variant"]:
        res[col] = res[col] * 10

    # Match obs
    obs_c, ci_obs_low, ci_obs_high = [], [], []
    keep = []
    for _, row in res.iterrows():
        obs_row = match_obs_row(df_obs, row["start"], row["end"])
        if obs_row is None:
            keep.append(False)
            obs_c.append(np.nan)
            ci_obs_low.append(np.nan)
            ci_obs_high.append(np.nan)
        else:
            keep.append(True)
            c = obs_row["coef_mean"] * 10
            obs_c.append(c)
            ci_obs_low.append(abs(c - obs_row["coef_low"] * 10))
            ci_obs_high.append(abs(obs_row["coef_high"] * 10 - c))

    res["obs_c"] = obs_c
    res["ci_obs_low"] = ci_obs_low
    res["ci_obs_high"] = ci_obs_high
    res = res[keep].reset_index(drop=True)

    # Plot
    fig_height = max(6, 0.26 * len(res))
    fig, ax = plt.subplots(figsize=(8, fig_height))

    ypos = np.arange(len(res))
    offset = 0.2

    # Model points colored by era
    model_err_low = np.abs(res["coef_central"] - res["coef_low_variant"])
    model_err_high = np.abs(res["coef_high_variant"] - res["coef_central"])
    colors = [era_color(py) for py in res["pub_year"]]

    for i in range(len(res)):
        ax.errorbar(res.iloc[i]["coef_central"], ypos[i] - offset,
                    xerr=[[model_err_low.iloc[i]], [model_err_high.iloc[i]]],
                    fmt="s", capsize=3, color=colors[i], markersize=4)

    # Obs points
    ax.errorbar(res["obs_c"], ypos + offset,
                xerr=[res["ci_obs_low"], res["ci_obs_high"]],
                fmt="o", capsize=3, color=OBS_COLOR, markersize=4,
                label="Observed (95% CI)")

    # Era legend entries
    for era_label, era_col in ERA_COLORS.items():
        ax.plot([], [], "s", color=era_col, markersize=5, label=f"Model ({era_label})")

    ax.set_yticks(ypos)
    ax.set_yticklabels(res["root"], fontsize=7)
    ax.set_xlabel("Warming rate (\u00b0C per decade)")
    ax.axvline(0, ls="--", lw=0.7, color="gray")
    ax.set_title("Observed vs. model warming rates over each valid window")
    ax.legend(loc="upper right", fontsize=7)
    fig.subplots_adjust(left=0.28, right=0.97, top=0.96, bottom=0.04)
    plt.margins(y=0.01)

    out = BASE / "warming_rate_comparison.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Figure 5: Model Accuracy Over Time (NEW)
# ────────────────────────────────────────────────────────────
def fig_accuracy_over_time():
    df_models = pd.read_csv(MODEL_TRENDS_CSV)
    df_obs = pd.read_csv(OBS_TIME_CSV)

    res = parse_variants(df_models, "model_time")
    if res.empty:
        print("  No model_time data, skipping accuracy plot.")
        return

    records = []
    for _, row in res.iterrows():
        obs_row = match_obs_row(df_obs, row["start"], row["end"])
        if obs_row is None or obs_row["coef_mean"] == 0:
            continue
        ratio_c = row["coef_central"] / obs_row["coef_mean"]
        ratio_low = row["coef_low_variant"] / obs_row["coef_mean"]
        ratio_high = row["coef_high_variant"] / obs_row["coef_mean"]
        records.append({
            "root": row["root"],
            "pub_year": row["pub_year"],
            "ratio": ratio_c,
            "ratio_low": ratio_low,
            "ratio_high": ratio_high,
        })

    rdf = pd.DataFrame(records)
    if rdf.empty:
        print("  No matching pairs for accuracy plot.")
        return

    fig, ax = plt.subplots(figsize=(9, 5))

    colors = [era_color(py) for py in rdf["pub_year"]]
    err_low = np.abs(rdf["ratio"] - rdf["ratio_low"])
    err_high = np.abs(rdf["ratio_high"] - rdf["ratio"])

    ax.errorbar(rdf["pub_year"], rdf["ratio"],
                yerr=[err_low, err_high],
                fmt="none", ecolor="lightgray", elinewidth=0.8, capsize=0, zorder=1)
    ax.scatter(rdf["pub_year"], rdf["ratio"], c=colors, s=30, zorder=2, edgecolors="white", linewidth=0.3)

    ax.axhline(1.0, color="black", ls="--", lw=1.0, label="Perfect agreement")
    ax.axhspan(0.8, 1.2, color="green", alpha=0.08, label="\u00b120% band")

    ax.set_xlabel("Publication year")
    ax.set_ylabel("Model / Observed warming rate ratio")
    ax.set_title("Model accuracy over time")
    ax.set_xlim(1935, rdf["pub_year"].max() + 2)
    ax.set_ylim(-0.5, max(4, rdf["ratio"].quantile(0.98) + 0.5))
    ax.grid(True, ls="--", alpha=0.2)

    for era_label, era_col in ERA_COLORS.items():
        ax.scatter([], [], color=era_col, s=30, label=era_label)
    ax.legend(fontsize=8, loc="upper left")

    fig.tight_layout()
    out = BASE / "model_accuracy_over_time.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Figure 5b: Implied TCR Accuracy Over Time
# ────────────────────────────────────────────────────────────
def fig_tcr_accuracy_over_time():
    """TCR-ratio analogue of fig_accuracy_over_time, using temp-vs-forcing slopes."""
    df_models = pd.read_csv(MODEL_TRENDS_CSV)
    df_obs = pd.read_csv(OBS_FORCING_CSV)

    res = parse_variants(df_models, "model_forcing")
    if res.empty:
        print("  No model_forcing data, skipping TCR accuracy plot.")
        return

    records = []
    for _, row in res.iterrows():
        obs_row = match_obs_row(df_obs, row["start"], row["end"], "anthropogenic")
        if obs_row is None or obs_row["coef_mean"] == 0:
            continue
        ratio_c = row["coef_central"] / obs_row["coef_mean"]
        ratio_low = row["coef_low_variant"] / obs_row["coef_mean"]
        ratio_high = row["coef_high_variant"] / obs_row["coef_mean"]
        records.append({
            "root": row["root"],
            "pub_year": row["pub_year"],
            "ratio": ratio_c,
            "ratio_low": ratio_low,
            "ratio_high": ratio_high,
        })

    rdf = pd.DataFrame(records)
    if rdf.empty:
        print("  No matching pairs for TCR accuracy plot.")
        return

    fig, ax = plt.subplots(figsize=(9, 5))

    colors = [era_color(py) for py in rdf["pub_year"]]
    err_low = np.abs(rdf["ratio"] - rdf["ratio_low"])
    err_high = np.abs(rdf["ratio_high"] - rdf["ratio"])

    ax.errorbar(rdf["pub_year"], rdf["ratio"],
                yerr=[err_low, err_high],
                fmt="none", ecolor="lightgray", elinewidth=0.8, capsize=0, zorder=1)
    ax.scatter(rdf["pub_year"], rdf["ratio"], c=colors, s=30, zorder=2,
               edgecolors="white", linewidth=0.3)

    ax.axhline(1.0, color="black", ls="--", lw=1.0, label="Perfect agreement")
    ax.axhspan(0.8, 1.2, color="green", alpha=0.08, label="±20% band")

    ax.set_xlabel("Publication year")
    ax.set_ylabel("Model / Observed implied TCR ratio")
    ax.set_title("Implied TCR accuracy over time")
    ax.set_xlim(1935, rdf["pub_year"].max() + 2)
    ax.set_ylim(-0.5, max(4, rdf["ratio"].quantile(0.98) + 0.5))
    ax.grid(True, ls="--", alpha=0.2)

    for era_label, era_col in ERA_COLORS.items():
        ax.scatter([], [], color=era_col, s=30, label=era_label)
    ax.legend(fontsize=8, loc="upper left")

    fig.tight_layout()
    out = BASE / "tcr_accuracy_over_time.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Compact 2-panel comparisons (scatter + bias-over-time)
# ────────────────────────────────────────────────────────────
def _build_compact_records(df_models, df_obs, dtype, scale, forcing_type=None):
    """Pair each model's central value with obs over the same timeframe.

    `scale` multiplies coefs into display units (10 for °C/decade, F_2xCO2 for TCR).
    """
    res = parse_variants(df_models, dtype)
    if res.empty:
        return pd.DataFrame()

    records = []
    for _, row in res.iterrows():
        obs_row = match_obs_row(df_obs, row["start"], row["end"], forcing_type)
        if obs_row is None:
            continue
        m = row["coef_central"] * scale
        m_lo = row["coef_low_variant"] * scale
        m_hi = row["coef_high_variant"] * scale
        o = obs_row["coef_mean"] * scale
        o_lo = obs_row["coef_low"] * scale
        o_hi = obs_row["coef_high"] * scale
        records.append({
            "root": row["root"],
            "pub_year": row["pub_year"],
            "model": m,
            "model_err_low": abs(m - m_lo),
            "model_err_high": abs(m_hi - m),
            "obs": o,
            "obs_err_low": abs(o - o_lo),
            "obs_err_high": abs(o_hi - o),
            "bias": m - o,
            "bias_err": np.sqrt(((m_hi - m_lo) / 2) ** 2 + ((o_hi - o_lo) / 2) ** 2),
        })
    return pd.DataFrame(records)


def _draw_scatter_panel(ax, rdf, axis_label, *, lim=None):
    """Model-vs-obs scatter with 1:1 diagonal. Use robust limits and annotate
    any high outliers above the visible range."""
    colors = [era_color(py) for py in rdf["pub_year"]]
    ax.errorbar(
        rdf["obs"], rdf["model"],
        xerr=[rdf["obs_err_low"], rdf["obs_err_high"]],
        yerr=[rdf["model_err_low"], rdf["model_err_high"]],
        fmt="none", ecolor="lightgray", elinewidth=0.6, capsize=0, zorder=1,
    )
    ax.scatter(rdf["obs"], rdf["model"], c=colors, s=28, zorder=2,
               edgecolors="white", linewidth=0.3)

    if lim is None:
        # Robust square limits: drop high outliers so the dense cluster is readable.
        vals = np.concatenate([rdf["obs"].values, rdf["model"].values])
        vals = vals[np.isfinite(vals)]
        hi = np.quantile(vals, 0.97)
        lo = min(0, vals.min())
        pad = 0.05 * (hi - lo)
        lim = (lo - pad, hi + pad)

    ax.plot(lim, lim, ls="--", lw=0.9, color="black", label="1:1 (perfect)")
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel(f"Observed {axis_label}")
    ax.set_ylabel(f"Model {axis_label}")
    ax.grid(True, ls="--", alpha=0.25)

    # Mark high outliers at the top edge with up-arrow markers; list them in an
    # upper-right corner box, one per line.
    above = rdf[rdf["model"] > lim[1]].sort_values("model", ascending=False)
    if len(above) > 0:
        edge_y = lim[1] - 0.02 * (lim[1] - lim[0])
        edge_x = np.clip(above["obs"].values, lim[0], lim[1])
        edge_colors = [era_color(py) for py in above["pub_year"]]
        ax.scatter(edge_x, [edge_y] * len(above), marker="^",
                   c=edge_colors, s=44, edgecolors="black", linewidth=0.4, zorder=3)
        lines = ["Above range:"] + [
            f"  {r['root']} ({r['model']:.1f})" for _, r in above.iterrows()
        ]
        ax.text(0.98, 0.98, "\n".join(lines), transform=ax.transAxes,
                fontsize=6.5, color="dimgray", va="top", ha="right",
                bbox=dict(facecolor="white", edgecolor="lightgray",
                          boxstyle="round,pad=0.3", alpha=0.9))
    return lim


def _draw_bias_panel(ax, rdf, ylabel):
    """Bias (model − obs) vs publication year. Clips high outliers to keep the
    bulk of the data readable, marking them with edge arrows."""
    colors = [era_color(py) for py in rdf["pub_year"]]
    ax.errorbar(rdf["pub_year"], rdf["bias"], yerr=rdf["bias_err"],
                fmt="none", ecolor="lightgray", elinewidth=0.6, capsize=0, zorder=1)
    ax.scatter(rdf["pub_year"], rdf["bias"], c=colors, s=28, zorder=2,
               edgecolors="white", linewidth=0.3)
    ax.axhline(0, color="black", ls="--", lw=0.9)
    ax.set_xlabel("Publication year")
    ax.set_ylabel(ylabel)
    ax.set_xlim(1935, rdf["pub_year"].max() + 2)

    bias = rdf["bias"].values
    finite = bias[np.isfinite(bias)]
    hi = np.quantile(finite, 0.97)
    lo = np.quantile(finite, 0.03)
    span = hi - lo
    ylim = (lo - 0.15 * span, hi + 0.15 * span)
    ax.set_ylim(ylim)

    above = rdf[rdf["bias"] > ylim[1]].sort_values("bias", ascending=False)
    if len(above) > 0:
        edge_y = ylim[1] - 0.03 * (ylim[1] - ylim[0])
        edge_colors = [era_color(py) for py in above["pub_year"]]
        ax.scatter(above["pub_year"], [edge_y] * len(above), marker="^",
                   c=edge_colors, s=44, edgecolors="black", linewidth=0.4, zorder=3)
        lines = ["Above range:"] + [
            f"  {r['root']} ({r['bias']:+.1f})" for _, r in above.iterrows()
        ]
        ax.text(0.98, 0.98, "\n".join(lines), transform=ax.transAxes,
                fontsize=6.5, color="dimgray", va="top", ha="right",
                bbox=dict(facecolor="white", edgecolor="lightgray",
                          boxstyle="round,pad=0.3", alpha=0.9))

    ax.grid(True, ls="--", alpha=0.25)


def _add_era_legend(ax):
    for era_label, era_col in ERA_COLORS.items():
        ax.scatter([], [], color=era_col, s=28, label=era_label,
                   edgecolors="white", linewidth=0.3)
    ax.legend(fontsize=8, loc="best", frameon=True)


def fig_warming_rate_compact():
    """2-panel: model-vs-obs scatter (left), bias-vs-pub-year (right)."""
    df_models = pd.read_csv(MODEL_TRENDS_CSV)
    df_obs = pd.read_csv(OBS_TIME_CSV)
    rdf = _build_compact_records(df_models, df_obs, "model_time", scale=10)
    if rdf.empty:
        print("  No data for warming-rate compact plot, skipping.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    _draw_scatter_panel(axes[0], rdf, "warming rate (°C / decade)")
    _add_era_legend(axes[0])
    axes[0].set_title("Model vs. observed warming rate\n(matched timeframes)")

    _draw_bias_panel(axes[1], rdf, "Model − observed (°C / decade)")
    axes[1].set_title("Bias vs. publication year")

    fig.tight_layout()
    out = BASE / "warming_rate_compact.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out.name}")


def fig_implied_tcr_compact():
    """2-panel TCR analogue of fig_warming_rate_compact."""
    df_models = pd.read_csv(MODEL_TRENDS_CSV)
    df_obs = pd.read_csv(OBS_FORCING_CSV)
    rdf = _build_compact_records(df_models, df_obs, "model_forcing",
                                 scale=F_2xCO2, forcing_type="anthropogenic")
    if rdf.empty:
        print("  No data for TCR compact plot, skipping.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    _draw_scatter_panel(axes[0], rdf, "implied TCR (°C / 2×CO₂)")
    _add_era_legend(axes[0])
    axes[0].set_title("Model vs. observed implied TCR\n(matched timeframes)")

    _draw_bias_panel(axes[1], rdf, "Model − observed (°C / 2×CO₂)")
    axes[1].set_title("Bias vs. publication year")

    fig.tight_layout()
    out = BASE / "implied_tcr_compact.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Figure 6: Forcing Comparison (NEW)
# ────────────────────────────────────────────────────────────
def fig_forcing_comparison():
    """Compare model forcing rate vs observed ERF forcing rate per timeframe."""
    df_models = pd.read_csv(MODEL_TRENDS_CSV)

    # We need model forcing rates (already in new_model_trends.csv as model_time dtype)
    # Actually we need forcing vs year — but model_trends only has temp vs year and temp vs forcing.
    # We need to compute forcing rates from the Excel _F columns and ERF data.
    # Load model data
    mdf = pd.read_excel(MODELS_FILE, engine="openpyxl")
    mdf.columns = [c.strip().lower() if isinstance(c, str) else c for c in mdf.columns]

    # Load anthropogenic forcing (common_history)
    ds = xr.open_dataset(FORCING_FILE)
    var_name = list(ds.data_vars)[0]
    da = ds[var_name].squeeze()
    edges = ds["timebounds"].values
    erf_years = (0.5 * (edges[:-1] + edges[1:])).astype(int)  # mid-years
    erf_total = 0.5 * (da[:-1, :].values + da[1:, :].values)  # (275, 841)
    ds.close()

    # Get model info from model_trends
    model_time = df_models[df_models["dtype"] == "model_time"].copy()
    parsed = parse_variants(model_time, "model_time")

    records = []
    for _, row in parsed.iterrows():
        root = row["root"]
        start, end = row["start"], min(row["end"], 2024)

        # Model forcing rate: regress _F vs year
        f_col = f"{root}_f"
        # Try median variant first
        for try_col in [f"{root}_median_f", f"{root}_average_f", f"{root}_f"]:
            if try_col in mdf.columns:
                f_col = try_col
                break
        else:
            if f_col not in mdf.columns:
                continue

        mask = mdf["year"].between(start, end)
        yrs = mdf.loc[mask, "year"].values.astype(float)
        fvals = mdf.loc[mask, f_col].values
        if np.sum(np.isfinite(fvals)) < 5:
            continue

        model_res = trend_stats(fvals, yrs, runtype="ols")
        model_rate = model_res["coef"] * 10  # W/m2 per decade

        # Obs forcing rate: mean across ERF ensemble
        erf_mask = (erf_years >= start) & (erf_years <= end)
        erf_yrs = erf_years[erf_mask].astype(float)
        erf_sub = erf_total[erf_mask, :]

        # Regress a subsample of forcing members against year
        n_sample = min(200, erf_sub.shape[1])
        obs_rates = []
        rng = np.random.default_rng(42)
        idx = rng.choice(erf_sub.shape[1], size=n_sample, replace=False)
        for j in idx:
            r = trend_stats(erf_sub[:, j], erf_yrs, runtype="ols")
            if np.isfinite(r["coef"]):
                obs_rates.append(r["coef"] * 10)

        if len(obs_rates) < 10:
            continue

        obs_mean = np.mean(obs_rates)
        obs_sd = np.std(obs_rates, ddof=1)

        records.append({
            "root": root,
            "pub_year": row["pub_year"],
            "start": start,
            "end": end,
            "model_rate": model_rate,
            "obs_rate": obs_mean,
            "obs_ci_low": 1.96 * obs_sd,
            "obs_ci_high": 1.96 * obs_sd,
        })

    rdf = pd.DataFrame(records).sort_values("pub_year").reset_index(drop=True)
    if rdf.empty:
        print("  No forcing comparison data, skipping.")
        return

    fig_height = max(6, 0.26 * len(rdf))
    fig, ax = plt.subplots(figsize=(8, fig_height))

    ypos = np.arange(len(rdf))
    offset = 0.2

    # Model forcing rate (no CI for simplicity — single model value)
    colors = [era_color(py) for py in rdf["pub_year"]]
    for i in range(len(rdf)):
        ax.plot(rdf.iloc[i]["model_rate"], ypos[i] - offset,
                "s", color=colors[i], markersize=4)

    # Obs forcing rate
    ax.errorbar(rdf["obs_rate"], ypos + offset,
                xerr=[rdf["obs_ci_low"], rdf["obs_ci_high"]],
                fmt="o", capsize=3, color=OBS_COLOR, markersize=4,
                label="Observed anthro. forcing (95% CI)")

    for era_label, era_col in ERA_COLORS.items():
        ax.plot([], [], "s", color=era_col, markersize=5, label=f"Model ({era_label})")

    ax.set_yticks(ypos)
    ax.set_yticklabels(rdf["root"], fontsize=7)
    ax.set_xlabel("Forcing rate (W/m\u00b2 per decade)")
    ax.axvline(0, ls="--", lw=0.7, color="gray")
    ax.set_title("Model vs. observed anthropogenic forcing rates")
    ax.legend(loc="upper right", fontsize=7)
    fig.subplots_adjust(left=0.28, right=0.97, top=0.96, bottom=0.04)
    plt.margins(y=0.01)

    out = BASE / "forcing_comparison.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out.name}")


# ────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────
def main():
    print("Generating figures...")

    print("\n[1/9] Implied TCR plot...")
    fig_implied_tcr()

    print("\n[2/9] Spaghetti plot...")
    fig_spaghetti()

    print("\n[3/9] Quantile envelope plot...")
    fig_quantile_envelope()

    print("\n[4/9] Warming rate comparison...")
    fig_warming_rate()

    print("\n[5/9] Model accuracy over time (warming rate)...")
    fig_accuracy_over_time()

    print("\n[6/9] Model accuracy over time (implied TCR)...")
    fig_tcr_accuracy_over_time()

    print("\n[7/9] Warming rate compact (scatter + bias)...")
    fig_warming_rate_compact()

    print("\n[8/9] Implied TCR compact (scatter + bias)...")
    fig_implied_tcr_compact()

    print("\n[9/9] Forcing comparison...")
    fig_forcing_comparison()

    print("\nDone — all figures saved.")


if __name__ == "__main__":
    main()
