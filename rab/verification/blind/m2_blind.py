#!/usr/bin/env python
"""m2_blind.py - blind rebuild of M2 (rate paths to Jan 2027 / Jan 2028) from rab/models/M2_SPEC.md alone.

WS4 blind builder (Claude Code), 2026-09-30 (Sydney). AI-generated research code for Team Caplet; no deliverable text.

Read to build this:  rab/models/M2_SPEC.md (the recipe), rab/data/ (raw inputs I1, I2, I3, I5), rab/numbers.yaml (I4,
cross-checks only).  Not read: any .py under rab/models or rab/results, and no insight_v1 script.  The reference
implementation's outputs were not looked at while this was written; see README.md for the one leak (a STATUS.md line).

Every section number below refers to M2_SPEC.md.  Seed 20260930.  Run:

    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind/m2_blind.py [--curve-date 2026-09-28]
        [--out rab/verification/blind] [--quick]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from scipy.optimize import brentq
from scipy.stats import norm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import adfuller

ROOT = Path(__file__).resolve().parents[3]  # blind -> verification -> rab -> worktree root
SEED = 20260930

# ----------------------------------------------------------------------------------------------------------------
# Constants (spec s2, s3.1)
# ----------------------------------------------------------------------------------------------------------------
TENOR_NAMES = ["1 Mo", "2 Mo", "3 Mo", "6 Mo", "1 Yr", "2 Yr", "3 Yr", "5 Yr", "7 Yr", "10 Yr", "20 Yr", "30 Yr"]
TEN = np.array([1 / 12, 2 / 12, 0.25, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0])
IDX = {n: i for i, n in enumerate(TENOR_NAMES)}
FRED_MAP = {"DGS1MO": "1 Mo", "DGS3MO": "3 Mo", "DGS6MO": "6 Mo", "DGS1": "1 Yr", "DGS2": "2 Yr", "DGS3": "3 Yr",
            "DGS5": "5 Yr", "DGS7": "7 Yr", "DGS10": "10 Yr", "DGS20": "20 Yr", "DGS30": "30 Yr"}
GRID = 0.5 * np.arange(1, 61)                  # t_j = 0.5 j, j = 1..60
KNOTS = np.concatenate([[0.0], GRID])          # (0, 0) prepended for ln DF interpolation
PAY_YEARS = list(range(2033, 2043))            # ten $50k payments, start of 2033 .. 2042
PAYMENT = 50_000.0
DEPOSIT_A = 300_000.0
DEPOSIT_B = 150_000.0
HOLIDAYS_2026 = {dt.date(2026, 10, 12), dt.date(2026, 11, 11), dt.date(2026, 11, 26), dt.date(2026, 12, 25)}
K_TENORS = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30], float)   # E4 fixed tenors
E4_TO_12 = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]                         # K index feeding each of the 12 tenors


def yf(d1, d0) -> float:
    """Year fraction (d1 - d0) days / 365.25 for python dates."""
    return (d1 - d0).days / 365.25


def mats_nov15():
    """P_Y = 15 Nov (Y - 1), Y = 2033..2042 (the Nov-15 STRIPS basis)."""
    return [dt.date(y - 1, 11, 15) for y in PAY_YEARS]


MATS = mats_nov15()


def business_days(D: dt.date, A: dt.date) -> int:
    """Weekdays strictly after D and strictly before A, excluding the 2026 bond-market holidays listed in the spec."""
    n = 0
    d = D + dt.timedelta(days=1)
    while d < A:
        if d.weekday() < 5 and d not in HOLIDAYS_2026:
            n += 1
        d += dt.timedelta(days=1)
    return n


# ----------------------------------------------------------------------------------------------------------------
# Curve engine (spec s3.1), vectorised over a matrix of par vectors at the 12 tenors
# ----------------------------------------------------------------------------------------------------------------
def interp_weights(x_known: np.ndarray, x_new: np.ndarray) -> np.ndarray:
    """Matrix M with M @ y = linear interpolation of the points (x_known, y) at x_new, flat outside."""
    M = np.zeros((len(x_new), len(x_known)))
    for i, t in enumerate(x_new):
        if t <= x_known[0]:
            M[i, 0] = 1.0
        elif t >= x_known[-1]:
            M[i, -1] = 1.0
        else:
            j = int(np.searchsorted(x_known, t))            # x_known[j-1] < t <= x_known[j]
            w = (t - x_known[j - 1]) / (x_known[j] - x_known[j - 1])
            M[i, j - 1] = 1.0 - w
            M[i, j] = w
    return M


W_GRID = interp_weights(TEN, GRID)      # 60 x 12: par at the semiannual grid from the 12 tenors
W_K = interp_weights(TEN, K_TENORS)     # 10 x 12: par at E4's K tenors from the 12 tenors


class Curves:
    """Bootstrapped discount factors for N par curves (percent, 12 tenors, no NaN)."""

    def __init__(self, C):
        C = np.atleast_2d(np.asarray(C, dtype=float))
        p = (C @ W_GRID.T) / 100.0                          # N x 60, decimal par at t_j
        N = p.shape[0]
        DF = np.empty_like(p)
        cum = np.zeros(N)
        for j in range(60):
            pj = 0.5 * p[:, j]
            DF[:, j] = (1.0 - pj * cum) / (1.0 + pj)        # DF_1 = 1/(1 + p_1/2) when cum = 0
            cum = cum + DF[:, j]
        self.lnDF = np.concatenate([np.zeros((N, 1)), np.log(DF)], axis=1)   # values at KNOTS

    def df(self, taus) -> np.ndarray:
        """DF(tau) = exp(L(tau)), L linear on (KNOTS, lnDF), flat beyond 30y.  Returns N x len(taus)."""
        taus = np.atleast_1d(np.asarray(taus, dtype=float))
        out = np.empty((self.lnDF.shape[0], len(taus)))
        for k, tau in enumerate(taus):
            if tau >= 30.0:
                out[:, k] = self.lnDF[:, -1]
            elif tau <= 0.0:
                out[:, k] = 0.0
            else:
                j = int(np.searchsorted(KNOTS, tau))
                w = (tau - KNOTS[j - 1]) / (KNOTS[j] - KNOTS[j - 1])
                out[:, k] = (1.0 - w) * self.lnDF[:, j - 1] + w * self.lnDF[:, j]
        return np.exp(out)


def rung_costs_rw(C, v: dt.date, mats=MATS) -> np.ndarray:
    """RW convention (s3.2): value at v of $50k at each maturity, curve C valued at v.  N x 10."""
    taus = np.array([yf(m, v) for m in mats])
    return PAYMENT * Curves(C).df(taus)


def cost_rw(C, v: dt.date) -> np.ndarray:
    return rung_costs_rw(C, v).sum(axis=1)


def rung_costs_fwd(C, D: dt.date, A: dt.date, mats=MATS) -> np.ndarray:
    """FWD convention (s3.2): today's PV of each rung carried to A at the curve's own short rate.  N x 10."""
    cv = Curves(C)
    taus = np.array([yf(m, D) for m in mats] + [yf(A, D)])
    d = cv.df(taus)
    return PAYMENT * d[:, :-1] / d[:, [-1]]


def cost_fwd(C, D: dt.date, A: dt.date) -> np.ndarray:
    return rung_costs_fwd(C, D, A).sum(axis=1)


def breakeven_fall_bp(R: np.ndarray, costfn) -> float:
    """Parallel shift b (bp, added to all 12 tenors) with costfn(R + b) = 300,000; returns -b (a positive fall)."""
    f = lambda b: float(costfn(R[None, :] + b / 100.0)[0]) - DEPOSIT_A
    b = brentq(f, -400.0, 400.0, xtol=1e-10, maxiter=500)
    return -b


# ----------------------------------------------------------------------------------------------------------------
# Data (spec s1, s4)
# ----------------------------------------------------------------------------------------------------------------
def load_treasury() -> pd.DataFrame:
    frames = []
    for folder in ("treasury_par_1990_1999", "treasury_par_2000_2026"):
        for f in sorted((ROOT / "rab" / "data" / folder).glob("*.csv")):
            df = pd.read_csv(f)
            df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
            keep = ["Date"] + [c for c in TENOR_NAMES if c in df.columns]      # drops "1.5 Month", "4 Mo"
            frames.append(df[keep])
    df = pd.concat(frames, ignore_index=True)
    dup = df["Date"].duplicated().sum()
    df = df.sort_values("Date").drop_duplicates("Date").set_index("Date")
    df = df.reindex(columns=TENOR_NAMES).apply(pd.to_numeric, errors="coerce")
    df.attrs["duplicates_dropped"] = int(dup)
    return df


def load_fred(before: pd.Timestamp) -> tuple[pd.DataFrame, pd.Series]:
    """Pre-1990 panel from FRED (mapped tenors, union of dates) and the full DGS10 series for the overlap check."""
    cols = {}
    for code, ten in FRED_MAP.items():
        df = pd.read_csv(ROOT / "rab" / "data" / "fred" / f"{code}.csv")
        df.columns = ["Date", ten]
        df["Date"] = pd.to_datetime(df["Date"])
        df[ten] = pd.to_numeric(df[ten], errors="coerce")
        cols[ten] = df.set_index("Date")[ten]
    panel = pd.concat(cols.values(), axis=1, sort=True).sort_index()
    panel = panel.reindex(columns=TENOR_NAMES)          # "2 Mo" has no FRED series -> NaN
    return panel[panel.index < before], cols["10 Yr"].dropna()


def build_panel(D: dt.date):
    """Daily curve panel 1962-D at the 12 tenors (spec s4), filled by par_d(t) (linear, flat outside)."""
    tre = load_treasury()
    first_tre = tre.index.min()                          # 2 Jan 1990
    fred, dgs10 = load_fred(first_tre)
    raw = pd.concat([fred, tre]).sort_index()
    raw = raw[raw.index <= pd.Timestamp(D)]
    keep = raw[["1 Yr", "5 Yr", "10 Yr"]].notna().all(axis=1)
    raw = raw[keep]
    vals = raw.to_numpy(dtype=float)
    filled = np.empty_like(vals)
    for i in range(vals.shape[0]):
        m = ~np.isnan(vals[i])
        filled[i] = np.interp(TEN, TEN[m], vals[i, m])   # np.interp is flat outside the known range
    dates = raw.index.to_numpy().astype("datetime64[D]")
    # overlap check: FRED DGS10 vs Treasury 10 Yr, common dates 1990+
    common = tre.index.intersection(dgs10.index)
    overlap_max = float((tre.loc[common, "10 Yr"] - dgs10.loc[common]).abs().max())
    info = {
        "treasury_rows": int(len(tre)), "treasury_first": str(tre.index.min().date()), "treasury_last": str(tre.index.max().date()),
        "treasury_duplicate_dates_dropped": tre.attrs["duplicates_dropped"],
        "fred_rows_pre1990": int(len(fred)), "panel_rows": int(len(dates)), "panel_first": str(dates[0]), "panel_last": str(dates[-1]),
        "rows_dropped_missing_1_5_10y": int((~keep).sum()),
        "fred_vs_treasury_10y_max_abs_diff_pct": overlap_max, "fred_vs_treasury_common_dates": int(len(common)),
    }
    return dates, filled, raw, info


def load_move() -> pd.Series:
    df = pd.read_csv(ROOT / "rab" / "data" / "m2" / "MOVE_yahoo_daily.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    s = pd.to_numeric(df["Close"], errors="coerce")
    s.index = df["Date"]
    return s.dropna().sort_index()


# ----------------------------------------------------------------------------------------------------------------
# Ladder yield, EWMA volatility, windows (spec s3.3, s4)
# ----------------------------------------------------------------------------------------------------------------
def ladder_yield(P12: np.ndarray, D: dt.date, mats=MATS) -> np.ndarray:
    """y(d) in percent: sum 50k (1 + y/200)^(-2 tau_Y) = V(d), tau_Y = (P_Y - D)/365.25, V from the date's own curve."""
    taus = np.array([yf(m, D) for m in mats])
    V = (PAYMENT * Curves(P12).df(taus)).sum(axis=1)
    lo = np.full(len(V), -5.0)
    hi = np.full(len(V), 60.0)
    for _ in range(120):                                  # bisection: 65 / 2^120 << 1e-10
        mid = 0.5 * (lo + hi)
        f = (PAYMENT * (1.0 + mid[:, None] / 200.0) ** (-2.0 * taus)).sum(axis=1) - V
        up = f > 0                                        # price too high -> yield too low
        lo = np.where(up, mid, lo)
        hi = np.where(up, hi, mid)
    return 0.5 * (lo + hi)


def ewma_sigma(dy_bp: np.ndarray, lam=0.97, init=60) -> np.ndarray:
    """dy_bp[k] = change into date k (dy_bp[0] = nan).  Returns sigma per date (bp/day), nan before date `init`."""
    n = len(dy_bp)
    s2 = np.full(n, np.nan)
    s2[init] = np.mean(dy_bp[1:init + 1] ** 2)
    for k in range(init + 1, n):
        s2[k] = lam * s2[k - 1] + (1.0 - lam) * dy_bp[k] ** 2
    return np.sqrt(s2)


def make_windows(dates: np.ndarray, h: int, D: dt.date, min_changes=250):
    """Start index k (>= min_changes earlier changes, s + h <= D) and end index e = last panel date <= s + h."""
    target = dates + np.timedelta64(h, "D")
    ok = (np.arange(len(dates)) >= min_changes) & (target <= np.datetime64(D))
    k = np.where(ok)[0]
    e = np.searchsorted(dates, target[k], side="right") - 1
    return k, e


# ----------------------------------------------------------------------------------------------------------------
# Scenario statistics (spec s6)
# ----------------------------------------------------------------------------------------------------------------
def pct(x, q):
    return float(np.percentile(x, q))


def scen_stats(costs: np.ndarray, rung2033: np.ndarray, n_h: int | None = None, is_windows=False, par_equiv=None) -> dict:
    gap = costs - DEPOSIT_A
    pos = gap > 0
    out = {
        "n_scenarios": int(len(costs)),
        "P_gap_gt_0": float(pos.mean()),
        "P_gap_gt_5k": float((gap > 5_000).mean()),
        "P_gap_gt_10k": float((gap > 10_000).mean()),
        "P_gap_gt_rung2033": float((gap > rung2033).mean()),
        "mean_gap_given_pos_usd": float(gap[pos].mean()) if pos.any() else 0.0,
        "gap_p90_usd": max(0.0, pct(gap, 90)), "gap_p95_usd": max(0.0, pct(gap, 95)), "gap_p99_usd": max(0.0, pct(gap, 99)),
        "cost_p5_usd": pct(costs, 5), "cost_p50_usd": pct(costs, 50), "cost_p95_usd": pct(costs, 95),
    }
    if is_windows and n_h:
        out["n_nonoverlapping_windows"] = int(len(costs) // n_h)
    if par_equiv is not None:
        b = par_equiv(costs)
        out["parallel_equiv_bp"] = {"mean": float(b.mean()), "sd": float(b.std(ddof=1)),
                                    "robust_sd": float((np.percentile(b, 75) - np.percentile(b, 25)) / 1.349)}
    return out


def block_bootstrap_ci(ind: np.ndarray, block: int, reps: int, rng: np.random.Generator) -> list[float]:
    """Moving-block bootstrap of a mean over window-start order: ceil(n/block) blocks of length `block`, truncated to n."""
    n = len(ind)
    nb = math.ceil(n / block)
    Ps = np.empty(reps)
    offs = np.arange(block)
    for r in range(reps):
        st = rng.integers(0, n - block + 1, size=nb)
        idx = (st[:, None] + offs[None, :]).ravel()[:n]
        Ps[r] = ind[idx].mean()
    return [pct(Ps, 5), pct(Ps, 95)]


def mvn_draw(rng: np.random.Generator, mean: np.ndarray, cov: np.ndarray, size: int) -> np.ndarray:
    """Multivariate normal draws through an eigendecomposition (works for singular covariances)."""
    w, V = np.linalg.eigh(0.5 * (cov + cov.T))
    w = np.clip(w, 0.0, None)
    A = V * np.sqrt(w)[None, :]
    return mean[None, :] + rng.standard_normal((size, len(mean))) @ A.T


# ----------------------------------------------------------------------------------------------------------------
# Main model
# ----------------------------------------------------------------------------------------------------------------
def quote_1_in_n(P: float) -> str:
    return f"about 1 in {int(round(1.0 / P))}" if P > 0 else "about 0"


def run(curve_date: dt.date, out_dir: Path, quick: bool = False) -> dict:
    t0 = time.time()
    N_MC = 10_000 if quick else 100_000
    N_BOOT = 100 if quick else 1_000
    D = curve_date
    A = dt.date(2027, 1, 1)
    B = dt.date(2028, 1, 1)
    h = (A - D).days
    h2 = (B - D).days
    n_h = business_days(D, A)
    log = []

    def say(msg):
        log.append(msg)
        print(msg, flush=True)

    res: dict = {"meta": {
        "builder": "WS4 blind rebuild from M2_SPEC.md (rab/verification/blind/m2_blind.py)",
        "curve_date_D": str(D), "purchase_date_A": str(A), "second_deposit_B": str(B),
        "h_days": h, "n_h_business_days": n_h, "h2_days": h2, "seed": SEED, "N_MC": N_MC, "N_bootstrap": N_BOOT,
        "maturity_basis": "15 Nov of the year before each payment (STRIPS), ten x $50,000",
        "run_started_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    }}

    # ---- panel and reference curve --------------------------------------------------------------------------
    dates, P12, raw, info = build_panel(D)
    res["data"] = info
    iD = int(np.searchsorted(dates, np.datetime64(D)))
    assert dates[iD] == np.datetime64(D), f"reference date {D} not in the panel"
    R = P12[iD].copy()
    res["reference_curve_R_pct"] = dict(zip(TENOR_NAMES, [float(x) for x in R]))
    say(f"panel: {info['panel_rows']} dates {info['panel_first']}..{info['panel_last']}; "
        f"FRED vs Treasury 10Y max |diff| = {info['fred_vs_treasury_10y_max_abs_diff_pct']:.3f}pp over {info['fred_vs_treasury_common_dates']} dates")

    # cross-checks from numbers.yaml (I4)
    with open(ROOT / "rab" / "numbers.yaml") as f:
        nums = yaml.safe_load(f)["numbers"]
    ref = {
        "cost_2027_strips": float(nums["laura.ladder.cost_2027_strips"]["value"]),
        "breakeven_fall_bp_strips": float(nums["laura.ladder.breakeven_fall_bp_strips"]["value"]),
        "stock_fund_2028_strips": float(nums["laura.stock_fund_2028_usd.strips"]["value"]),
        "floor_cost_2028": float(nums["laura.floor_cost_2028"]["value"]),
        "H6_gap_odds_28sep": nums["ref.H6.gap_odds_28sep"]["value"],
        "H13": nums["ref.H13.rates_fall_first"]["value"],
        "H14": nums["ref.H14.joint_tail_no_deposit"]["value"],
    }
    yaml_curve = nums["market.par_curve"]["value"]
    gate_a_date = D == dt.date(2026, 9, 28)   # the numbers.yaml cross-checks hold only on the Gate A curve (Gate B fix)
    if gate_a_date:
        assert all(abs(float(yaml_curve[k]) - R[IDX[k]]) < 1e-9 for k in TENOR_NAMES), "numbers.yaml par curve != panel row"

    # ---- s3.2 deterministic checks -----------------------------------------------------------------------
    cost_fwd_R = float(cost_fwd(R[None, :], D, A)[0])
    cost_rw_R = float(cost_rw(R[None, :], A)[0])
    cost_today_R = float(rung_costs_rw(R[None, :], D).sum())          # PV on D, for information
    be_fwd = breakeven_fall_bp(R, lambda C: cost_fwd(C, D, A))
    be_rw = breakeven_fall_bp(R, lambda C: cost_rw(C, A))
    rungs_rw_R = rung_costs_rw(R[None, :], A)[0]
    res["deterministic"] = {
        "cost_fwd_R_usd": cost_fwd_R, "cost_fwd_R_check_vs_yaml_usd": cost_fwd_R - ref["cost_2027_strips"],
        "cost_rw_R_usd": cost_rw_R, "headroom_rw_usd": DEPOSIT_A - cost_rw_R, "headroom_fwd_usd": DEPOSIT_A - cost_fwd_R,
        "pv_today_R_usd": cost_today_R,
        "breakeven_fall_bp_fwd": be_fwd, "breakeven_fall_bp_fwd_check_vs_yaml": be_fwd - ref["breakeven_fall_bp_strips"],
        "breakeven_fall_bp_rw": be_rw,
        "rung_costs_rw_R_usd": dict(zip([str(y) for y in PAY_YEARS], [float(x) for x in rungs_rw_R])),
    }
    say(f"Cost_FWD(R) = {cost_fwd_R:,.2f} (yaml {ref['cost_2027_strips']:,.2f}); Cost_RW(R) = {cost_rw_R:,.2f}; "
        f"break-even fall FWD {be_fwd:.2f}bp (yaml {ref['breakeven_fall_bp_strips']}), RW {be_rw:.2f}bp")
    if gate_a_date:
        assert abs(cost_fwd_R - ref["cost_2027_strips"]) < 0.01, "Cost_FWD(R) does not reproduce numbers.yaml to the cent"

    # ---- s3.3 ladder yield, dy, EWMA -----------------------------------------------------------------------
    y = ladder_yield(P12, D)
    dy = np.full(len(y), np.nan)
    dy[1:] = np.diff(y) * 100.0                                         # bp, change into date k
    sig = ewma_sigma(dy)                                                # bp/day
    sigma_D = float(sig[iD])
    y_pm = ladder_yield(np.vstack([R + 0.01, R - 0.01]), D)
    dy_db = float((y_pm[0] - y_pm[1]) / 0.02)
    res["ladder_yield"] = {
        "y_D_pct": float(y[iD]), "dy_db_at_R": dy_db, "sigma_D_bp_per_day": sigma_D, "sigma_D_bp_per_year": sigma_D * math.sqrt(252),
        "y_min_pct": float(y.min()), "y_max_pct": float(y.max()),
        "realised_sd_2026_bp_per_day": float(np.nanstd(dy[dates >= np.datetime64("2026-01-01")], ddof=1)),
    }
    say(f"ladder yield y(D) = {y[iD]:.4f}%, dy/db = {dy_db:.4f}, EWMA sigma_D = {sigma_D:.2f} bp/day = {sigma_D*math.sqrt(252):.1f} bp/yr")

    # parallel-equivalent grid (changelog sensitivity)
    bgrid = np.arange(-400.0, 400.0 + 1e-9, 0.25)
    cgrid = cost_rw(R[None, :] + bgrid[:, None] / 100.0, A)
    par_equiv = lambda costs: np.interp(-costs, -cgrid, bgrid)

    def stats_curves(C, **kw):
        rc = rung_costs_rw(C, A)
        return scen_stats(rc.sum(axis=1), rc[:, 0], par_equiv=par_equiv, **kw), rc.sum(axis=1)

    # ---- s5 windows ------------------------------------------------------------------------------------------
    k, e = make_windows(dates, h, D)
    Delta = P12[e] - P12[k]                                             # windows x 12, percent
    ten10 = P12[k, IDX["10 Yr"]]
    res["windows"] = {"count": int(len(k)), "first_start": str(dates[k[0]]), "last_start": str(dates[k[-1]]),
                      "mean_changes_per_window": float(np.mean(e - k)), "n_nonoverlapping": int(len(k) // n_h)}
    say(f"windows (h={h}d): {len(k)} starts {dates[k[0]]}..{dates[k[-1]]}, mean {np.mean(e-k):.1f} panel changes each")

    rng_boot = np.random.default_rng([SEED, 9])
    est = {}

    # E1: filtered historical simulation
    ks = sigma_D / sig[k]
    D1 = ks[:, None] * Delta
    D1 = D1 - D1.mean(axis=0)
    C1 = R[None, :] + D1
    e1, costs1 = stats_curves(C1, n_h=n_h, is_windows=True)
    e1["P_gap_gt_0_ci90_blockboot"] = block_bootstrap_ci((costs1 > DEPOSIT_A).astype(float), n_h, N_BOOT, rng_boot)
    e1["P_gap_gt_0_FWD"] = float((cost_fwd(C1, D, A) > DEPOSIT_A).mean())
    e1["scale_factor_k"] = {"min": float(ks.min()), "median": float(np.median(ks)), "max": float(ks.max())}
    est["E1_history_rescaled"] = e1

    # E2: similar yield levels
    lvl = (ten10 >= 4.0) & (ten10 <= 6.5)
    D2 = Delta[lvl] - Delta[lvl].mean(axis=0)
    C2 = R[None, :] + D2
    e2, costs2 = stats_curves(C2, n_h=n_h, is_windows=True)
    e2["P_gap_gt_0_ci90_blockboot"] = block_bootstrap_ci((costs2 > DEPOSIT_A).astype(float), n_h, N_BOOT, rng_boot)
    e2["P_gap_gt_0_FWD"] = float((cost_fwd(C2, D, A) > DEPOSIT_A).mean())
    e2["level_band_pct"] = [4.0, 6.5]
    e2["ten_year_on_D_pct"] = float(R[IDX["10 Yr"]])
    est["E2_history_similar_level"] = e2
    say(f"E1 P = {e1['P_gap_gt_0']:.4f} (n={e1['n_scenarios']}); E2 P = {e2['P_gap_gt_0']:.4f} (n={e2['n_scenarios']})")

    # E3: AR(1) / Vasicek on the ladder yield
    be_rw_pct = -be_rw / 100.0                                         # RW break-even shift in percent (negative)

    def ar1_fit(series: np.ndarray, label: str) -> dict:
        r = AutoReg(series, lags=1, trend="c").fit()
        c_hat, phi_hat = [float(v) for v in r.params]
        n = int(r.nobs)
        s_e2 = float(r.sigma2)
        cov = np.asarray(r.cov_params(), dtype=float)
        phi_bc = min(1.0, phi_hat + (1.0 + 3.0 * phi_hat) / n)
        theta = c_hat / (1.0 - phi_hat)
        c_bc = theta * (1.0 - phi_bc)

        def nstep(c, phi):
            if phi >= 1.0:
                return 0.0, n_h * s_e2
            m = (c - (1.0 - phi) * y[iD]) * (1.0 - phi ** n_h) / (1.0 - phi)
            v = s_e2 * (1.0 - phi ** (2 * n_h)) / (1.0 - phi ** 2)
            return m, v

        def plug(c, phi):
            m, v = nstep(c, phi)
            return float(norm.cdf((be_rw_pct - m) / math.sqrt(v)))

        def vas(phi):
            kappa = -math.log(phi) * 252.0 if phi < 1 else 0.0
            return {"kappa_per_yr": kappa, "half_life_yr": (math.log(2) / kappa) if kappa > 0 else float("inf")}

        adf_p = float(adfuller(series, regression="c", autolag="AIC", result_object=False)[1])
        return {
            "sample": label, "n_obs": n, "c_hat": c_hat, "phi_hat": phi_hat, "theta_pct": theta,
            "s_e_pct_per_step": math.sqrt(s_e2), "sigma_bp_per_yr": math.sqrt(s_e2) * math.sqrt(252) * 100.0,
            "phi_bc": phi_bc, "c_bc": c_bc, "vasicek_hat": vas(phi_hat), "vasicek_bc": vas(phi_bc),
            "cov_params": cov.tolist(), "plugin_P_hat": plug(c_hat, phi_hat), "plugin_P_bc": plug(c_bc, phi_bc),
            "adf_pvalue": adf_p, "_cov": cov, "_s_e2": s_e2, "_nstep": nstep,
        }

    fit_all = ar1_fit(y, "1962+ (whole panel)")
    rng3 = np.random.default_rng([SEED, 3])
    params = rng3.multivariate_normal([fit_all["c_bc"], fit_all["phi_bc"]], fit_all["_cov"], size=N_MC)
    z = rng3.standard_normal(N_MC)
    c_d, phi_d = params[:, 0].copy(), params[:, 1].copy()
    rw = phi_d >= 1.0
    phi_d[rw] = 1.0
    c_d[rw] = 0.0
    s_e2 = fit_all["_s_e2"]
    with np.errstate(divide="ignore", invalid="ignore"):
        m = np.where(rw, 0.0, (c_d - (1.0 - phi_d) * y[iD]) * (1.0 - phi_d ** n_h) / (1.0 - phi_d))
        v = np.where(rw, n_h * s_e2, s_e2 * (1.0 - phi_d ** (2 * n_h)) / (1.0 - phi_d ** 2))
    change = m + np.sqrt(v) * z                                          # percent
    C3 = R[None, :] + change[:, None]
    e3, _ = stats_curves(C3)
    fits = [fit_all]
    for start, label in ((np.datetime64("1990-01-02"), "1990+"), (np.datetime64("2000-01-01"), "2000+")):
        fits.append(ar1_fit(y[dates >= start], label))
    clean = lambda f: {kk: vv for kk, vv in f.items() if not kk.startswith("_")}
    e3.update({"fits": [clean(f) for f in fits], "share_draws_random_walk": float(rw.mean()),
               "predictive_change_sd_bp": float(change.std(ddof=1) * 100), "predictive_change_mean_bp": float(change.mean() * 100)})
    est["E3_vasicek_ar1"] = e3
    say(f"E3 P = {e3['P_gap_gt_0']:.4f}; phi_hat={fit_all['phi_hat']:.6f} theta={fit_all['theta_pct']:.3f}% "
        f"kappa_bc={fit_all['vasicek_bc']['kappa_per_yr']:.4f}/yr half-life={fit_all['vasicek_bc']['half_life_yr']:.2f}y; "
        f"plug-in hat {fit_all['plugin_P_hat']:.4f}, bc {fit_all['plugin_P_bc']:.4f}; ADF p={fit_all['adf_pvalue']:.3f}")

    # E4: PCA + VAR(1) on 1990+
    m90 = dates >= np.datetime64("1990-01-02")
    Y = P12[m90] @ W_K.T                                                # 1990+ x K
    dY = np.diff(Y, axis=0)
    covY = np.cov(dY, rowvar=False, ddof=1)
    w, V = np.linalg.eigh(covY)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    L = V[:, :3]
    shares = w[:3] / w.sum()
    Ybar = Y.mean(axis=0)
    F = (Y - Ybar) @ L
    U = (Y - Ybar) - F @ L.T
    var = VAR(F).fit(1, trend="c")
    mu = var.forecast(F[-1:], n_h)[-1]
    S = var.forecast_cov(n_h)[-1]
    covdU = np.cov(np.diff(U, axis=0), rowvar=False, ddof=1)
    covdF = np.cov(np.diff(F, axis=0), rowvar=False, ddof=1)
    rng4 = np.random.default_rng([SEED, 4])
    Fh = mvn_draw(rng4, mu, S, N_MC)
    dU = mvn_draw(rng4, np.zeros(len(K_TENORS)), n_h * covdU, N_MC)
    DK = (Fh - F[-1]) @ L.T + dU
    C4 = R[None, :] + DK[:, E4_TO_12]
    e4, _ = stats_curves(C4)
    rng44 = np.random.default_rng([SEED, 44])
    Fh_rw = mvn_draw(rng44, np.zeros(3), n_h * covdF, N_MC)
    dU_rw = mvn_draw(rng44, np.zeros(len(K_TENORS)), n_h * covdU, N_MC)
    DK_rw = Fh_rw @ L.T + dU_rw
    C4rw = R[None, :] + DK_rw[:, E4_TO_12]
    e4rw, _ = stats_curves(C4rw)
    e4.update({"pca_variance_shares": [float(s) for s in shares], "pca_variance_share_top3_total": float(shares.sum()),
               "n_obs_1990plus": int(Y.shape[0]), "var_forecast_mean_minus_FD": [float(x) for x in (mu - F[-1])],
               "var_forecast_sd": [float(x) for x in np.sqrt(np.diag(S))],
               "var_phi_eigenvalues_abs": [float(abs(x)) for x in np.linalg.eigvals(var.coefs[0])],
               "implied_mean_shift_10y_bp": float(((mu - F[-1]) @ L.T)[K_TENORS.tolist().index(10.0)] * 100),
               "random_walk_variant": e4rw})
    est["E4_pca_var"] = e4
    say(f"E4 P = {e4['P_gap_gt_0']:.4f} (RW variant {e4rw['P_gap_gt_0']:.4f}); PCA shares {np.round(shares, 4).tolist()}")

    # E5: MOVE
    move = load_move()
    move_dates = move.index.to_numpy().astype("datetime64[D]")
    move_vals = move.to_numpy(dtype=float)
    pos = np.searchsorted(move_dates, dates[k], side="right") - 1        # last close <= s
    has = pos >= 0
    cs = np.nancumsum(np.where(np.isnan(dy), 0.0, dy ** 2))
    RV = np.sqrt(252.0 * (cs[e] - cs[k]) / (e - k))
    ratio = RV[has] / move_vals[pos[has]]
    rho = float(np.median(ratio))
    q25, q75 = float(np.percentile(ratio, 25)), float(np.percentile(ratio, 75))
    iMD = int(np.searchsorted(move_dates, np.datetime64(D), side="right") - 1)
    MOVE_D = float(move_vals[iMD])
    move_63 = float(move_vals[max(0, iMD - 62):iMD + 1].mean())
    X = np.column_stack([np.ones(has.sum()), move_vals[pos[has]]])
    beta = np.linalg.lstsq(X, RV[has], rcond=None)[0]
    rng5 = np.random.default_rng([SEED, 5])
    z5 = rng5.standard_normal(N_MC)

    def e5_variant(sigma_h_bp):
        C = R[None, :] + (sigma_h_bp * z5)[:, None] / 100.0
        st, costs = stats_curves(C)
        st["sigma_h_bp"] = float(sigma_h_bp)
        st["P_gap_gt_0_FWD"] = float((cost_fwd(C, D, A) > DEPOSIT_A).mean())
        st["P_gap_gt_0_analytic"] = float(norm.cdf(-be_rw / sigma_h_bp))
        return st

    scale = math.sqrt(n_h / 252.0)
    e5 = e5_variant(rho * MOVE_D * scale)
    e5.update({"MOVE_D": MOVE_D, "MOVE_D_date": str(move_dates[iMD]), "rho_median": rho, "rho_q25": q25, "rho_q75": q75,
               "n_windows_with_MOVE": int(has.sum()), "MOVE_63d_mean": move_63,
               "regression_RV_on_MOVE": {"intercept_bp": float(beta[0]), "slope": float(beta[1]), "RV_at_MOVE_D_bp": float(beta[0] + beta[1] * MOVE_D)},
               "variants": {
                   "rho_1": e5_variant(1.0 * MOVE_D * scale),
                   "rho_q25": e5_variant(q25 * MOVE_D * scale),
                   "rho_q75": e5_variant(q75 * MOVE_D * scale),
                   "regression": e5_variant((beta[0] + beta[1] * MOVE_D) * scale),
                   "move_63d_mean_x_rho": e5_variant(rho * move_63 * scale),
               }})
    est["E5_move_options"] = e5
    say(f"E5 P = {e5['P_gap_gt_0']:.4f}; MOVE_D={MOVE_D:.2f} rho={rho:.4f} [{q25:.4f},{q75:.4f}] sigma_h={e5['sigma_h_bp']:.2f}bp")

    res["estimators"] = est
    Ps = {kk: vv["P_gap_gt_0"] for kk, vv in est.items()}
    P_head = float(np.median(list(Ps.values())))
    res["headline"] = {
        "P_ladder_cost_gt_300k_on_1jan2027": P_head, "quote": quote_1_in_n(P_head),
        "range_min": float(min(Ps.values())), "range_max": float(max(Ps.values())), "per_estimator": Ps,
        "rule": "median of E1-E5, RW (yields unchanged) convention, Nov-15 STRIPS basis, valuation 1 Jan 2027, MODEL, laura_plan",
    }
    say(f"HEADLINE P = {P_head:.4f} ({quote_1_in_n(P_head)}), range {min(Ps.values()):.4f}-{max(Ps.values()):.4f}")

    # ---- s7 reconciliation -------------------------------------------------------------------------------
    rec = {}
    i5 = pd.read_csv(ROOT / "research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv")
    i5["Date"] = pd.to_datetime(i5["Date"], format="%m/%d/%Y")
    i5 = i5.sort_values("Date").set_index("Date").reindex(columns=TENOR_NAMES).apply(pd.to_numeric, errors="coerce")
    D25 = i5.index.max().date()
    assert D25 == dt.date(2026, 9, 25)
    i5v = np.vstack([np.interp(TEN, TEN[~np.isnan(r)], r[~np.isnan(r)]) for r in i5.to_numpy(float)])
    R25 = i5v[-1]

    def lognormal_p(curves, row_dates, Dx, centre):
        """Zero-drift lognormal around `centre`.  Spec reading: Cost_FWD(c) with the valuation date fixed at Dx for every
        2026 row.  Variant (explains insight_v1's printed figure): each row's curve carried from its own date, so the
        three-month roll sits inside the daily changes; it adds about 1.6% to the annualised sigma."""
        t = yf(A, Dx)
        c_fixed = cost_fwd(curves, Dx, A)
        c_moving = np.array([cost_fwd(curves[i][None, :], row_dates[i], A)[0] for i in range(len(row_dates))])
        out = {}
        for tag, c in (("fixed_valuation", c_fixed), ("moving_valuation", c_moving)):
            sigma = float(np.std(np.diff(np.log(c)), ddof=1) * math.sqrt(252))
            out[tag] = {"P": float(1.0 - norm.cdf(math.log(DEPOSIT_A / centre) / (sigma * math.sqrt(t)))), "sigma_ann": sigma}
        out["t_yr"] = t
        return out

    cf25 = float(cost_fwd(R25[None, :], D25, A)[0])
    r1 = lognormal_p(i5v, [d.date() for d in i5.index], D25, cf25)
    p1, s1, t1 = r1["fixed_valuation"]["P"], r1["fixed_valuation"]["sigma_ann"], r1["t_yr"]
    rec["R1_D1_lognormal_25sep"] = {"P": p1, "sigma_ann": s1, "t_yr": t1, "cost_fwd_25sep_usd": cf25, "n_rows": int(len(i5v)), "must_reproduce": 0.305,
                                    "variant_moving_valuation": r1["moving_valuation"],
                                    "note": "spec reading (valuation fixed at 25 Sep) gives P; the moving-valuation variant reproduces the printed 30.5%"}
    m26 = dates >= np.datetime64("2026-01-01")
    r2 = lognormal_p(P12[m26], [pd.Timestamp(d).date() for d in dates[m26]], D, cost_fwd_R)
    p2, s2, t2 = r2["fixed_valuation"]["P"], r2["fixed_valuation"]["sigma_ann"], r2["t_yr"]
    rec["R2_D1_lognormal_28sep"] = {"P": p2, "sigma_ann": s2, "t_yr": t2, "n_rows": int(m26.sum()), "must_reproduce": ref["H6_gap_odds_28sep"]["model_nov15"],
                                    "variant_moving_valuation": r2["moving_valuation"],
                                    "note": "spec reading gives P; the moving-valuation variant reproduces the printed 24.2%"}
    be25 = breakeven_fall_bp(R25, lambda C: cost_fwd(C, D25, A))
    rec["R3_strategy_mc_v2_parallel_37bp"] = {"P_25sep_analytic": float(norm.cdf(-be25 / 37.0)), "P_28sep_analytic": float(norm.cdf(-be_fwd / 37.0)),
                                              "breakeven_fall_bp_25sep_fwd": be25, "must_reproduce_25sep": 0.302, "note": "analytic; spec says the MC printed 30.2% (analytic 30.1%)"}
    # R4: AX1b windows on insight_v1's FRED DGS10
    f10 = pd.read_csv(ROOT / "research/insight_v1/scripts/data/D3/fred_DGS10.csv")
    f10.columns = ["Date", "v"]
    f10["Date"] = pd.to_datetime(f10["Date"])
    f10["v"] = pd.to_numeric(f10["v"], errors="coerce")
    f10 = f10.dropna().sort_values("Date")
    vals10 = f10["v"].to_numpy()
    d10 = f10["Date"].to_numpy().astype("datetime64[D]")
    ch68 = vals10[68:] - vals10[:-68]
    st68 = d10[:-68]
    r4 = {}
    for Xbp in (19, 26):
        for since in (1962, 1990, 2000):
            msk = st68 >= np.datetime64(f"{since}-01-01")
            r4[f"fell_ge_{Xbp}bp_since_{since}"] = {"share_le": float((ch68[msk] <= -Xbp / 100 + 1e-9).mean()),
                                                     "share_lt": float((ch68[msk] < -Xbp / 100 - 1e-9).mean()), "n": int(msk.sum())}
    r4["must_reproduce_26bp"] = {"1962": 0.276, "1990": 0.311, "2000": 0.285}
    r4["last_dgs10_date"] = str(d10[-1])
    rec["R4_AX1b_dgs10_68day_windows"] = r4
    p5 = float(1.0 - norm.cdf(math.log(DEPOSIT_A / cost_rw_R) / (s2 * math.sqrt(t2))))
    s2m = r2["moving_valuation"]["sigma_ann"]
    p5m = float(1.0 - norm.cdf(math.log(DEPOSIT_A / cost_rw_R) / (s2m * math.sqrt(t2))))
    rec["R5_lognormal_28sep_RW_centre"] = {"P": p5, "centre_usd": cost_rw_R, "variant_moving_valuation": {"P": p5m, "sigma_ann": s2m}}
    rec["R6_headline"] = {"P": P_head}
    rec["waterfall"] = [
        {"step": "R1 D1 lognormal, 25 Sep curve (insight_v1 '1 in 3')", "P_spec_reading": p1, "P_moving_valuation": r1["moving_valuation"]["P"]},
        {"step": "R2 curve moved to 28 Sep (headroom 19 -> 26bp)", "P_spec_reading": p2, "P_moving_valuation": r2["moving_valuation"]["P"]},
        {"step": "R5 no-view centre (yields unchanged) instead of forward rates", "P_spec_reading": p5, "P_moving_valuation": p5m},
        {"step": "R6 volatility and curve shape from five estimators (headline)", "P_spec_reading": P_head, "P_moving_valuation": P_head},
    ]
    res["reconciliation"] = rec
    say(f"R1 {p1:.4f} (0.305) | R2 {p2:.4f} (0.242) | R3 {rec['R3_strategy_mc_v2_parallel_37bp']['P_25sep_analytic']:.4f} (0.302) | "
        f"R4 26bp: {r4['fell_ge_26bp_since_1962']['share_le']:.4f}/{r4['fell_ge_26bp_since_1990']['share_le']:.4f}/{r4['fell_ge_26bp_since_2000']['share_le']:.4f} "
        f"(0.276/0.311/0.285) | R5 {p5:.4f} | R6 {P_head:.4f}")

    # ---- s8 fifteen-month section ----------------------------------------------------------------------------
    def branch_2028(C1, C2, step1_fwd=False):
        rc1 = rung_costs_fwd(C1, D, A) if step1_fwd else rung_costs_rw(C1, A)      # N x 10, 2033..2042
        cost1 = rc1.sum(axis=1)
        y1 = C1[:, IDX["1 Yr"]] / 100.0
        short = cost1 > DEPOSIT_A
        leftover = np.where(short, 0.0, DEPOSIT_A - cost1)
        # longest first: cumulative cost buying 2042, 2041, ...
        rev = rc1[:, ::-1]
        cum = np.cumsum(rev, axis=1)
        prev = cum - rev
        bought = np.clip((DEPOSIT_A - prev) / rev, 0.0, 1.0)                     # fraction of each rung bought (reverse order)
        bought = np.where(short[:, None], bought, 1.0)
        f_unbought = (1.0 - bought)[:, ::-1]                                       # back to 2033..2042 order
        rc2 = rung_costs_rw(C2, B)
        T = (f_unbought * rc2).sum(axis=1)
        G = DEPOSIT_B + leftover * (1.0 + y1) - T
        y5 = C2[:, IDX["5 Yr"]] / 100.0
        Fc = DEPOSIT_B / (1.0 + y5) ** 5
        S = np.maximum(0.0, G - Fc)
        face = np.where(G >= Fc, DEPOSIT_B, G * (1.0 + y5) ** 5)
        return {"cost1": cost1, "leftover": leftover, "T": T, "G": G, "F": Fc, "S": S, "face": face, "n_unbought_rungs": (f_unbought > 0).sum(axis=1)}

    def branch_stats(b):
        Tpos = b["T"] > 0
        return {"n": int(len(b["S"])), "S_p5": pct(b["S"], 5), "S_p50": pct(b["S"], 50), "S_p95": pct(b["S"], 95), "S_mean": float(b["S"].mean()),
                "P_S_lt_20k": float((b["S"] < 20_000).mean()), "P_S_eq_0": float((b["S"] <= 0).mean()), "P_T_gt_0": float(Tpos.mean()),
                "mean_T_given_pos": float(b["T"][Tpos].mean()) if Tpos.any() else 0.0, "T_p95": pct(b["T"], 95),
                "F_p5": pct(b["F"], 5), "F_p50": pct(b["F"], 50), "F_p95": pct(b["F"], 95),
                "face_p5": pct(b["face"], 5), "P_face_lt_150k": float((b["face"] < DEPOSIT_B - 1e-6).mean())}

    base_fwd = branch_2028(R[None, :], R[None, :], step1_fwd=True)
    base_rw = branch_2028(R[None, :], R[None, :])
    fm = {"check_base_fwd": {"S_usd": float(base_fwd["S"][0]), "F_usd": float(base_fwd["F"][0]), "leftover_usd": float(base_fwd["leftover"][0]),
                             "must_reproduce": {"S": ref["stock_fund_2028_strips"], "F": ref["floor_cost_2028"]},
                             "diff_S": float(base_fwd["S"][0]) - ref["stock_fund_2028_strips"], "diff_F": float(base_fwd["F"][0]) - ref["floor_cost_2028"]},
          "base_rw": {"S_usd": float(base_rw["S"][0]), "F_usd": float(base_rw["F"][0]), "leftover_usd": float(base_rw["leftover"][0])}}
    say(f"2028 base (FWD step 1): S = {base_fwd['S'][0]:,.0f} (yaml {ref['stock_fund_2028_strips']}), F = {base_fwd['F'][0]:,.0f} (yaml {ref['floor_cost_2028']}); RW base S = {base_rw['S'][0]:,.0f}")
    k2, e2_ = make_windows(dates, h2, D)
    e1_ = np.searchsorted(dates, dates[k2] + np.timedelta64(h, "D"), side="right") - 1
    Dl1 = P12[e1_] - P12[k2]
    Dl2 = P12[e2_] - P12[k2]
    ks2 = (sigma_D / sig[k2])[:, None]
    lvl2 = (P12[k2, IDX["10 Yr"]] >= 4.0) & (P12[k2, IDX["10 Yr"]] <= 6.5)
    variants = {
        "H-FHS": (ks2 * Dl1 - (ks2 * Dl1).mean(axis=0), ks2 * Dl2 - (ks2 * Dl2).mean(axis=0)),
        "H-LVL": (Dl1[lvl2] - Dl1[lvl2].mean(axis=0), Dl2[lvl2] - Dl2[lvl2].mean(axis=0)),
        "H-RAW": (Dl1, Dl2),
    }
    fm["windows"] = {"count": int(len(k2)), "first_start": str(dates[k2[0]]), "last_start": str(dates[k2[-1]]), "count_level_band": int(lvl2.sum())}
    for name, (d1, d2) in variants.items():
        b = branch_2028(R[None, :] + d1, R[None, :] + d2)
        fm[name] = branch_stats(b)
        fm[name]["P_cost1_gt_300k"] = float((b["cost1"] > DEPOSIT_A).mean())
        say(f"2028 {name}: S p5/p50/p95 = {fm[name]['S_p5']:,.0f}/{fm[name]['S_p50']:,.0f}/{fm[name]['S_p95']:,.0f}; "
            f"P(S<20k)={fm[name]['P_S_lt_20k']:.3f} P(S=0)={fm[name]['P_S_eq_0']:.3f} P(T>0)={fm[name]['P_T_gt_0']:.3f}")
    res["fifteen_month"] = fm

    # H13 / H14 re-check (FWD convention, 28 Sep curve)
    h13 = {}
    h14 = {}
    for b in (-50, -100, -150):
        Cb = (R + b / 100.0)[None, :]
        cv = Curves(Cb)
        dfA, dfB = [float(x) for x in cv.df([yf(A, D), yf(B, D)])[0]]
        gap = float(cost_fwd(Cb, D, A)[0]) - DEPOSIT_A
        topup = max(gap, 0.0) * dfA / dfB
        leftover = max(-gap, 0.0)
        G = DEPOSIT_B + leftover * dfA / dfB - topup
        row = {"gap_usd": gap, "topup_on_B_usd": topup, "G_usd": G}
        for tag, y5 in (("y5_unchanged", R[IDX["5 Yr"]]), ("y5_shifted", R[IDX["5 Yr"]] + b / 100.0)):
            Fc = DEPOSIT_B / (1 + y5 / 100.0) ** 5
            row[tag] = {"y5_pct": float(y5), "floor_cost_usd": Fc, "stock_fund_usd": max(0.0, G - Fc),
                        "floor_face_usd": DEPOSIT_B if G >= Fc else G * (1 + y5 / 100.0) ** 5}
        h13[f"{b}bp"] = row
        if b in (-50, -100):
            rung33 = float(rung_costs_fwd(Cb, D, A)[0, 0])
            h14[f"{b}bp"] = {"unfunded_2033_usd": gap / rung33 * PAYMENT, "rung_2033_fwd_usd": rung33,
                             "must_reproduce": ref["H14"][f"{b}bp_28sep"]}
    res["H13_recheck"] = {"results": h13, "insight_v1_25sep_values": ref["H13"]}
    res["H14_recheck"] = h14
    say("H13 fund (y5 unchanged / shifted): " + "; ".join(f"{b}: {h13[b]['y5_unchanged']['stock_fund_usd']:,.0f}/{h13[b]['y5_shifted']['stock_fund_usd']:,.0f}" for b in h13)
        + " | H14: " + ", ".join(f"{b}: {h14[b]['unfunded_2033_usd']:,.0f} (must {h14[b]['must_reproduce']})" for b in h14))

    # ---- sensitivities (spec changelog) -----------------------------------------------------------------------
    sens = {}
    starts = dates[k]

    def hist_P(mask, scale_k=False, demean=True):
        d = Delta[mask] * (ks[mask][:, None] if scale_k else 1.0)
        if demean:
            d = d - d.mean(axis=0)
        return {"P": float((cost_rw(R[None, :] + d, A) > DEPOSIT_A).mean()), "n": int(mask.sum())}

    allm = np.ones(len(k), bool)
    sens["history_subsamples"] = {
        "1962+_raw": hist_P(allm, False, False),
        "1962+_rescaled_not_demeaned": hist_P(allm, True, False),
        "1962+_raw_demeaned": hist_P(allm, False, True),
        "similar_level_raw": hist_P(lvl, False, False),
        "similar_level_rescaled_demeaned": hist_P(lvl, True, True),
    }
    for yr in (1990, 2000, 2022):
        mk = starts >= np.datetime64(f"{yr}-01-01")
        sens["history_subsamples"][f"{yr}+_raw"] = hist_P(mk, False, False)
        sens["history_subsamples"][f"{yr}+_raw_demeaned"] = hist_P(mk, False, True)
        sens["history_subsamples"][f"{yr}+_rescaled_demeaned"] = hist_P(mk, True, True)

    # purchase on Mon 4 Jan 2027
    A2 = dt.date(2027, 1, 4)
    h_2 = (A2 - D).days
    n_h2 = business_days(D, A2)
    k_, e_ = make_windows(dates, h_2, D)
    Dl = P12[e_] - P12[k_]
    ks_ = sigma_D / sig[k_]
    d1 = ks_[:, None] * Dl
    d1 = d1 - d1.mean(axis=0)
    lv_ = (P12[k_, IDX["10 Yr"]] >= 4.0) & (P12[k_, IDX["10 Yr"]] <= 6.5)
    d2 = Dl[lv_] - Dl[lv_].mean(axis=0)
    be_rw2 = breakeven_fall_bp(R, lambda C: cost_rw(C, A2))
    with np.errstate(divide="ignore", invalid="ignore"):
        m_ = np.where(rw, 0.0, (c_d - (1.0 - phi_d) * y[iD]) * (1.0 - phi_d ** n_h2) / (1.0 - phi_d))
        v_ = np.where(rw, n_h2 * s_e2, s_e2 * (1.0 - phi_d ** (2 * n_h2)) / (1.0 - phi_d ** 2))
    ch_ = m_ + np.sqrt(v_) * z
    mu2 = var.forecast(F[-1:], n_h2)[-1]
    S2 = var.forecast_cov(n_h2)[-1]
    rng4b = np.random.default_rng([SEED, 4])
    Fh2 = mvn_draw(rng4b, mu2, S2, N_MC)
    dU2 = mvn_draw(rng4b, np.zeros(len(K_TENORS)), n_h2 * covdU, N_MC)
    DK2 = (Fh2 - F[-1]) @ L.T + dU2
    P_4jan = {
        "E1": float((cost_rw(R[None, :] + d1, A2) > DEPOSIT_A).mean()),
        "E2": float((cost_rw(R[None, :] + d2, A2) > DEPOSIT_A).mean()),
        "E3": float((cost_rw(R[None, :] + ch_[:, None], A2) > DEPOSIT_A).mean()),
        "E4": float((cost_rw(R[None, :] + DK2[:, E4_TO_12], A2) > DEPOSIT_A).mean()),
        "E5": float((cost_rw(R[None, :] + (rho * MOVE_D * math.sqrt(n_h2 / 252.0) * z5)[:, None] / 100.0, A2) > DEPOSIT_A).mean()),
    }
    sens["purchase_4jan2027"] = {"A": str(A2), "h_days": h_2, "n_h": n_h2, "cost_rw_R_usd": float(cost_rw(R[None, :], A2)[0]),
                                 "breakeven_fall_bp_rw": be_rw2, "per_estimator": P_4jan, "P_median": float(np.median(list(P_4jan.values()))),
                                 "n_windows": int(len(k_))}
    res["sensitivities"] = sens
    say(f"4 Jan purchase: median P = {sens['purchase_4jan2027']['P_median']:.4f}; history raw 1962+ P = {sens['history_subsamples']['1962+_raw']['P']:.4f}")

    # ---- headline keys for the report ----------------------------------------------------------------------
    res["headline_keys"] = {
        "P_gap_headline": P_head,
        "P_gap_headline_quote": quote_1_in_n(P_head),
        "P_gap_range_min": res["headline"]["range_min"],
        "P_gap_range_max": res["headline"]["range_max"],
        "P_E1": Ps["E1_history_rescaled"], "P_E2": Ps["E2_history_similar_level"], "P_E3": Ps["E3_vasicek_ar1"],
        "P_E4": Ps["E4_pca_var"], "P_E5": Ps["E5_move_options"],
        "cost_fwd_R_usd": cost_fwd_R, "cost_rw_R_usd": cost_rw_R,
        "breakeven_fall_bp_fwd": be_fwd, "breakeven_fall_bp_rw": be_rw,
        "sigma_D_bp_per_year": sigma_D * math.sqrt(252),
        "R1_P": p1, "R2_P": p2, "R3_P_25sep": rec["R3_strategy_mc_v2_parallel_37bp"]["P_25sep_analytic"],
        "R4_26bp_1962": r4["fell_ge_26bp_since_1962"]["share_le"], "R4_26bp_1990": r4["fell_ge_26bp_since_1990"]["share_le"],
        "R4_26bp_2000": r4["fell_ge_26bp_since_2000"]["share_le"], "R5_P": p5,
        "vasicek_theta_pct": fit_all["theta_pct"], "vasicek_kappa_bc_per_yr": fit_all["vasicek_bc"]["kappa_per_yr"],
        "vasicek_half_life_bc_yr": fit_all["vasicek_bc"]["half_life_yr"],
        "pca_share_1": float(shares[0]), "pca_share_2": float(shares[1]), "pca_share_3": float(shares[2]),
        "move_rho_median": rho, "E5_sigma_h_bp": e5["sigma_h_bp"],
        "S2028_FHS_p5": fm["H-FHS"]["S_p5"], "S2028_FHS_p50": fm["H-FHS"]["S_p50"], "S2028_FHS_p95": fm["H-FHS"]["S_p95"],
        "S2028_FHS_P_lt_20k": fm["H-FHS"]["P_S_lt_20k"], "S2028_FHS_P_eq_0": fm["H-FHS"]["P_S_eq_0"], "S2028_FHS_P_T_gt_0": fm["H-FHS"]["P_T_gt_0"],
        "S2028_LVL_p50": fm["H-LVL"]["S_p50"], "S2028_RAW_p50": fm["H-RAW"]["S_p50"],
        "S2028_base_fwd_usd": fm["check_base_fwd"]["S_usd"], "F2028_base_usd": fm["check_base_fwd"]["F_usd"], "S2028_base_rw_usd": fm["base_rw"]["S_usd"],
        "H13_-50bp_fund_y5_unchanged": h13["-50bp"]["y5_unchanged"]["stock_fund_usd"], "H13_-50bp_fund_y5_shifted": h13["-50bp"]["y5_shifted"]["stock_fund_usd"],
        "H13_-100bp_fund_y5_unchanged": h13["-100bp"]["y5_unchanged"]["stock_fund_usd"], "H13_-100bp_fund_y5_shifted": h13["-100bp"]["y5_shifted"]["stock_fund_usd"],
        "H13_-150bp_floor_face_y5_unchanged": h13["-150bp"]["y5_unchanged"]["floor_face_usd"], "H13_-150bp_floor_face_y5_shifted": h13["-150bp"]["y5_shifted"]["floor_face_usd"],
        "H14_-50bp_unfunded_2033_usd": h14["-50bp"]["unfunded_2033_usd"], "H14_-100bp_unfunded_2033_usd": h14["-100bp"]["unfunded_2033_usd"],
        "P_median_4jan_purchase": sens["purchase_4jan2027"]["P_median"],
    }
    res["meta"]["runtime_s"] = round(time.time() - t0, 1)
    res["log"] = log
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "results.json", "w") as f:
        json.dump(res, f, indent=1, default=float)
    say(f"wrote {out_dir / 'results.json'} in {res['meta']['runtime_s']}s")
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--curve-date", default="2026-09-28")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent))
    ap.add_argument("--quick", action="store_true", help="10k draws, 100 bootstrap replicates (smoke test)")
    a = ap.parse_args(argv)
    run(dt.date.fromisoformat(a.curve_date), Path(a.out), quick=a.quick)


if __name__ == "__main__":
    main()
