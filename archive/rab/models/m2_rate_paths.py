"""M2 rate paths: the chance Laura's ten-payment ladder costs more than $300,000 on 1 Jan 2027, and what rate moves to
1 Jan 2028 do to the stock fund. Reconciles insight_v1's "about 1 in 3".

WS4, RAB Kit, 2026-09-30 (Sydney). AI-generated research code (Claude Code) for Team Caplet; MODEL outputs.
Spec: rab/models/M2_SPEC.md (sections are mirrored here as [S3]..[S8]). Seed 20260930.

Reuse (rab/inventory.md, M2 row): the curve is M1's "D1 method" (rab/models/m1_ladder.py `Curve`, which itself equals
insight_v1 D1). This file vectorises it for many scenario curves and asserts, at run time, that it equals M1's `Curve`
to 1e-10 on every discount factor it checks and that it reproduces the numbers.yaml $292,418.11. The reconciliation rows
re-run insight_v1 D1 [6], strategy_mc_v2 (a) and AX1b [C] from their own input files.

Run from the worktree root:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m2_rate_paths.py [--curve-date YYYY-MM-DD] [--no-figs]
Writes rab/results/M2/*.csv, m2_results.json, m2_report.txt, m2_proposed_numbers.yaml and the PNG figures.
"""
import argparse
import csv
import glob
import importlib.util
import json
import math
import os
import sys
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import norm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import adfuller

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "rab", "results", "M2")
SEED = 20260930
NAMES = ["1 Mo", "2 Mo", "3 Mo", "6 Mo", "1 Yr", "2 Yr", "3 Yr", "5 Yr", "7 Yr", "10 Yr", "20 Yr", "30 Yr"]
TT = np.array([1 / 12, 2 / 12, .25, .5, 1, 2, 3, 5, 7, 10, 20, 30])
I1Y, I5Y, I10Y = NAMES.index("1 Yr"), NAMES.index("5 Yr"), NAMES.index("10 Yr")
GRID = 0.5 * np.arange(1, 61)
NODES = np.r_[0.0, GRID]
YEARS = list(range(2033, 2043))
PAY, DEP1, DEP2 = 50_000.0, 300_000.0, 150_000.0
A27, B28 = date(2027, 1, 1), date(2028, 1, 1)
FRED = {"DGS1MO": "1 Mo", "DGS3MO": "3 Mo", "DGS6MO": "6 Mo", "DGS1": "1 Yr", "DGS2": "2 Yr", "DGS3": "3 Yr",
        "DGS5": "5 Yr", "DGS7": "7 Yr", "DGS10": "10 Yr", "DGS20": "20 Yr", "DGS30": "30 Yr"}
# U.S. bond-market holidays with no Treasury curve (only those that can fall inside the horizons used here)
HOLIDAYS = ["2026-10-12", "2026-11-11", "2026-11-26", "2026-12-25", "2027-01-01"]
REPORT = []


def say(s=""):
    REPORT.append(str(s))
    print(s)


def nov15():
    return [date(y - 1, 11, 15) for y in YEARS]


def exact():
    return [date(y, 1, 1) for y in YEARS]


# ------------------------------------------------------------------------------------------------ [S3] vector curve
def interp_matrix(x_src, x_dst):
    """M with M @ v == np.interp(x_dst, x_src, v) for every v (linear, flat outside)."""
    x_src = np.asarray(x_src, float)
    M = np.zeros((len(x_dst), len(x_src)))
    for j in range(len(x_src)):
        e = np.zeros(len(x_src))
        e[j] = 1.0
        M[:, j] = np.interp(x_dst, x_src, e)
    return M


W_GRID = interp_matrix(TT, GRID)  # 60 x 12


def lndf_nodes(par12):
    """par12: (N, 12) par yields in percent at TT. Returns ln DF at NODES (N, 61): M1 A1 / D1 method."""
    par12 = np.atleast_2d(par12)
    pg = (par12 / 100.0) @ W_GRID.T
    n = pg.shape[0]
    df = np.empty_like(pg)
    cum = np.zeros(n)
    for j in range(pg.shape[1]):
        c = pg[:, j] / 2.0
        df[:, j] = (1.0 - c * cum) / (1.0 + c)
        cum += df[:, j]
    return np.c_[np.zeros(n), np.log(df)]


def lndf_at(nodes, taus):
    """ln DF at year fractions taus (same taus for every row)."""
    return nodes @ interp_matrix(NODES, taus).T


def taus(dates, v):
    return np.array([(d - v).days / 365.25 for d in dates])


def rungs_rw(par12, A, pays=None):
    """[S3.2] RW: the scenario curve is the curve on the purchase day A, valued at A. Returns (N, 10) rung costs."""
    return PAY * np.exp(lndf_at(lndf_nodes(par12), taus(pays or nov15(), A)))


def rungs_fwd(par12, D, A, pays=None):
    """[S3.2] FWD: shocked today (valued at D), carried to A at the curve's own rates. (N, 10) rung costs."""
    nodes = lndf_nodes(par12)
    ln = lndf_at(nodes, taus(pays or nov15(), D))
    la = lndf_at(nodes, taus([A], D))
    return PAY * np.exp(ln - la)


def cost_rw(par12, A):
    return rungs_rw(par12, A).sum(axis=1)


def cost_fwd(par12, D, A, pays=None):
    return rungs_fwd(par12, D, A, pays).sum(axis=1)


def breakeven(fun, lo=-6.0, hi=3.0):
    """Parallel shift b (percent) with fun(b) == DEP1; returned as a positive fall in bp."""
    return -100.0 * brentq(lambda b: fun(b) - DEP1, lo, hi, xtol=1e-9)


# ------------------------------------------------------------------------------------------------ [S4] panel
def read_treasury():
    files = sorted(glob.glob(os.path.join(ROOT, "rab/data/treasury_par_1990_1999/*.csv"))) + \
        sorted(f for f in glob.glob(os.path.join(ROOT, "rab/data/treasury_par_2000_2026/*.csv")) if "refetch" not in f)
    rows = {}
    for f in files:
        for r in csv.DictReader(open(f)):
            m, d, y = r["Date"].split("/")
            dt = date(int(y), int(m), int(d))
            vals = {k: float(r[k]) for k in NAMES if r.get(k) not in (None, "", "N/A")}
            rows[dt] = vals
    return rows


def read_fred(before):
    rows = {}
    for sid, name in FRED.items():
        for r in csv.DictReader(open(os.path.join(ROOT, "rab/data/fred", sid + ".csv"))):
            v = r[sid]
            dt = date.fromisoformat(r["observation_date"])
            if dt < before and v not in ("", "."):
                rows.setdefault(dt, {})[name] = float(v)
    return rows


def to_par12(vals):
    ks = [k for k in NAMES if k in vals]
    return np.interp(TT, [TT[NAMES.index(k)] for k in ks], [vals[k] for k in ks])


def build_panel(D):
    tsy = read_treasury()
    first_tsy = min(tsy)
    fred = read_fred(first_tsy)
    allrows = {**fred, **tsy}
    dates, pars, src = [], [], []
    for dt in sorted(allrows):
        v = allrows[dt]
        if dt > D or not all(k in v for k in ("1 Yr", "5 Yr", "10 Yr")):
            continue
        dates.append(dt)
        pars.append(to_par12(v))
        src.append("treasury" if dt >= first_tsy else "fred")
    # FRED vs Treasury on the overlap (10 Yr)
    f10 = {date.fromisoformat(r["observation_date"]): float(r["DGS10"])
           for r in csv.DictReader(open(os.path.join(ROOT, "rab/data/fred/DGS10.csv"))) if r["DGS10"] not in ("", ".")}
    common = [d for d in tsy if d in f10 and "10 Yr" in tsy[d]]
    diff = max(abs(f10[d] - tsy[d]["10 Yr"]) for d in common)
    return np.array(dates), np.array(pars), np.array(src), {"fred_vs_treasury_10y_max_abs_diff_pct": diff,
                                                            "overlap_days": len(common), "first_treasury": str(first_tsy)}


def ladder_yield(par12, D):
    """[S3.3] Flat semiannual yield (percent) that prices the same-time-to-maturity Nov-15 ladder."""
    tau = taus(nov15(), D)
    V = (PAY * np.exp(lndf_at(lndf_nodes(par12), tau))).sum(axis=1)
    y = np.full(len(V), 0.05)
    for _ in range(60):
        g = 1 + y[:, None] / 2
        f = (PAY * g ** (-2 * tau)).sum(axis=1) - V
        fp = (PAY * (-tau) * g ** (-2 * tau - 1)).sum(axis=1)
        step = f / fp
        y -= step
        if np.max(np.abs(step)) < 1e-13:
            break
    assert np.max(np.abs(step)) < 1e-11
    return 100 * y


def ewma_vol(dy, lam=0.97, init=60):
    s2 = np.full(len(dy), np.nan)
    s2[init] = np.mean(dy[1:init + 1] ** 2)
    for t in range(init + 1, len(dy)):
        s2[t] = lam * s2[t - 1] + (1 - lam) * dy[t] ** 2
    return np.sqrt(s2)


def windows(dates, D, h_days, burn=250):
    starts = [i for i in range(burn, len(dates)) if dates[i] + timedelta(days=h_days) <= D]
    starts = np.array(starts)
    ends = np.searchsorted(dates, [dates[i] + timedelta(days=h_days) for i in starts], side="right") - 1
    return starts, ends


# ------------------------------------------------------------------------------------------------ statistics
PAR_EQ = {}


def par_equivalent(cost):
    """Parallel shift (bp) of R that gives the same RW cost on A (cost falls as yields rise)."""
    g, c = PAR_EQ["grid"], PAR_EQ["cost"]
    return np.interp(-cost, -c, g)


def summarise(rungs, name, n_h, extra=None):
    cost = rungs.sum(axis=1)
    gap = cost - DEP1
    pos = gap > 0
    q = lambda a, p: float(np.percentile(a, p))
    out = {"estimator": name, "n_scenarios": int(len(cost)), "P_gap": float(pos.mean()),
           "P_gap_gt_5k": float((gap > 5_000).mean()), "P_gap_gt_10k": float((gap > 10_000).mean()),
           "P_gap_gt_rung2033": float((gap > rungs[:, 0]).mean()),
           "mean_gap_given_gap": float(gap[pos].mean()) if pos.any() else 0.0,
           "gap_p90": max(0.0, q(gap, 90)), "gap_p95": max(0.0, q(gap, 95)), "gap_p99": max(0.0, q(gap, 99)),
           "cost_p5": q(cost, 5), "cost_p50": q(cost, 50), "cost_p95": q(cost, 95)}
    if PAR_EQ:
        b = par_equivalent(cost)
        out.update({"shift_eq_mean_bp": float(b.mean()), "shift_eq_sd_bp": float(b.std()),
                    "shift_eq_robust_sd_bp": float((np.percentile(b, 75) - np.percentile(b, 25)) / 1.349),
                    "shift_eq_p5_bp": q(b, 5), "shift_eq_p95_bp": q(b, 95)})
    if extra:
        out.update(extra)
    return out


def block_bootstrap(ind, block, reps=1000, seed_k=9):
    rng = np.random.default_rng([SEED, seed_k])
    n = len(ind)
    nb = int(math.ceil(n / block))
    starts = rng.integers(0, n - block + 1, size=(reps, nb))
    idx = (starts[:, :, None] + np.arange(block)[None, None, :]).reshape(reps, -1)[:, :n]
    ps = ind[idx].mean(axis=1)
    return float(np.percentile(ps, 5)), float(np.percentile(ps, 95))


def fmt_p(p):
    return f"{100 * p:5.1f}%"


# ------------------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--curve-date", default=None)
    ap.add_argument("--no-figs", action="store_true")
    ap.add_argument("--out", default=None, help="output folder (default rab/results/M2)")
    args = ap.parse_args()
    global OUT
    if args.out:
        OUT = os.path.abspath(args.out)
    os.makedirs(OUT, exist_ok=True)

    tsy_rows = read_treasury()
    D = date.fromisoformat(args.curve_date) if args.curve_date else max(tsy_rows)
    A, B = A27, B28
    h, h2 = (A - D).days, (B - D).days
    n_h = int(np.busday_count((D + timedelta(days=1)).isoformat(), A.isoformat(), holidays=HOLIDAYS))
    now = datetime.now(timezone.utc)
    say("M2 rate paths (WS4, RAB Kit). AI-generated research (Claude Code) for Team Caplet. MODEL outputs.")
    say(f"Run {now.astimezone(ZoneInfo('America/New_York')):%Y-%m-%d %H:%M %Z} = "
        f"{now.astimezone(ZoneInfo('Australia/Sydney')):%Y-%m-%d %H:%M %Z}. Seed {SEED}.")
    say(f"Reference curve D = {D}; purchase A = {A} (h = {h} calendar days, n_h = {n_h} business days); "
        f"second deposit B = {B} (h2 = {h2} days).")
    R = to_par12(tsy_rows[D])[None, :]
    say("Reference par curve (percent): " + ", ".join(f"{k} {v:.2f}" for k, v in zip(NAMES, R[0])))

    # ---------------------------------------------------------------- [S3] checks against M1 and numbers.yaml
    spec = importlib.util.spec_from_file_location("m1", os.path.join(ROOT, "rab/models/m1_ladder.py"))
    m1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m1)
    row = dict(tsy_rows_raw_row(D))
    cv = m1.Curve(row)
    nodes = lndf_nodes(R)
    test_dates = nov15() + exact() + [A, B, D + timedelta(days=17), date(2040, 6, 30), date(2060, 1, 1)]
    mine = np.exp(lndf_at(nodes, taus(test_dates, D)))[0]
    theirs = np.array([cv.df(d) for d in test_dates])
    err = float(np.max(np.abs(mine - theirs)))
    assert err < 1e-10, err
    c_fwd = float(cost_fwd(R, D, A)[0])
    c_rw = float(cost_rw(R, A)[0])
    say(f"\n[S3] Vector curve equals M1 Curve (max |DF diff| {err:.1e}). Cost_FWD(R) = ${c_fwd:,.2f} "
        f"(numbers.yaml laura.ladder.cost_2027_strips $292,418.11 on 28 Sep); Cost_RW(R) = ${c_rw:,.2f} "
        f"(yields unchanged on {A}; +${c_rw - c_fwd:,.0f})")
    if D == date(2026, 9, 28):
        assert abs(c_fwd - 292_418.11) < 0.01, c_fwd
    be_fwd = breakeven(lambda b: cost_fwd(R + b, D, A)[0])
    be_rw = breakeven(lambda b: cost_rw(R + b, A)[0])
    say(f"     Break-even parallel fall: FWD {be_fwd:.2f}bp (numbers.yaml 26.2bp on 28 Sep); RW {be_rw:.2f}bp")
    gridb = np.arange(-400.0, 400.01, 0.25)
    PAR_EQ["grid"], PAR_EQ["cost"] = gridb, cost_rw(R + gridb[:, None] / 100, A)
    assert np.all(np.diff(PAR_EQ["cost"]) < 0)
    res = {"meta": {"curve_date": str(D), "purchase_date": str(A), "h_days": h, "n_h": n_h, "second_date": str(B),
                    "seed": SEED, "generated_utc": now.isoformat(timespec="seconds"),
                    "generated_et": now.astimezone(ZoneInfo("America/New_York")).isoformat(timespec="minutes"),
                    "generated_sydney": now.astimezone(ZoneInfo("Australia/Sydney")).isoformat(timespec="minutes"),
                    "basis": "Nov-15 STRIPS basis (numbers.yaml headline basis), laura_plan, MODEL",
                    "m1_df_max_abs_diff": err},
           "base": {"cost_fwd": c_fwd, "cost_rw": c_rw, "breakeven_fall_bp_fwd": be_fwd, "breakeven_fall_bp_rw": be_rw,
                    "headroom_fwd": DEP1 - c_fwd, "headroom_rw": DEP1 - c_rw}}

    # ---------------------------------------------------------------- [S4] panel, ladder yield, EWMA
    dates, par, src, chk = build_panel(D)
    assert dates[-1] == D and np.allclose(par[-1], R[0])
    y = ladder_yield(par, D)
    dy = np.r_[np.nan, np.diff(y) * 100]  # bp; dy[t] = change into t
    sig = ewma_vol(dy)
    iD = len(dates) - 1
    yb = ladder_yield(R + np.array([[-0.01], [0.01]]), D)
    ratio = float((yb[1] - yb[0]) / 0.02)
    say(f"\n[S4] Panel {dates[0]} .. {dates[-1]}: {len(dates):,} days ({(src == 'fred').sum():,} FRED before "
        f"{chk['first_treasury']}, {(src == 'treasury').sum():,} Treasury). FRED vs Treasury 10y max |diff| "
        f"{chk['fred_vs_treasury_10y_max_abs_diff_pct']:.2f}pp over {chk['overlap_days']:,} common days.")
    say(f"     Ladder yield today {y[iD]:.3f}% (d ladder yield / d parallel par shift = {ratio:.3f}). "
        f"EWMA vol today {sig[iD] * math.sqrt(252):.0f}bp/yr ({sig[iD]:.2f}bp/day); panel average "
        f"{np.sqrt(np.nanmean(dy[1:] ** 2) * 252):.0f}bp/yr; 2026 so far "
        f"{np.sqrt(np.mean(dy[[d.year == D.year for d in dates]][1:] ** 2) * 252):.0f}bp/yr.")
    res["panel"] = {"first": str(dates[0]), "last": str(dates[-1]), "days": int(len(dates)), **chk,
                    "ladder_yield_today_pct": float(y[iD]), "dy_per_parallel_shift": ratio,
                    "ewma_vol_today_bp_yr": float(sig[iD] * math.sqrt(252)),
                    "vol_all_bp_yr": float(np.sqrt(np.nanmean(dy[1:] ** 2) * 252))}

    st, en = windows(dates, D, h)
    delta = par[en] - par[st]
    k_s = sig[iD] / sig[st]
    y10s = par[st, I10Y]
    say(f"     {len(st):,} overlapping {h}-day windows ({dates[st[0]]} .. {dates[st[-1]]}); "
        f"{len(st) // n_h:,} non-overlapping. Scale factor k_s median {np.median(k_s):.2f} (p5 {np.percentile(k_s, 5):.2f},"
        f" p95 {np.percentile(k_s, 95):.2f}).")

    est, dists = [], {}

    # ---------------------------------------------------------------- [S5] E1 FHS
    d1 = k_s[:, None] * delta
    d1 = d1 - d1.mean(axis=0)
    r1 = rungs_rw(R + d1, A)
    ind1 = (r1.sum(1) > DEP1).astype(float)
    lo, hi = block_bootstrap(ind1, n_h)
    e1 = summarise(r1, "E1 history rescaled to today's volatility, 1962+", n_h,
                   {"id": "E1", "P_lo90": lo, "P_hi90": hi, "n_indep": len(st) // n_h, "in_headline": True,
                    "P_gap_fwd": float((cost_fwd(R + d1, D, A) > DEP1).mean())})
    est.append(e1)
    dists["E1"] = r1.sum(1)

    # ---------------------------------------------------------------- [S5] E2 similar-level
    mlev = (y10s >= 4.0) & (y10s <= 6.5)
    d2 = delta[mlev] - delta[mlev].mean(axis=0)
    r2 = rungs_rw(R + d2, A)
    ind2 = (r2.sum(1) > DEP1).astype(float)
    lo, hi = block_bootstrap(ind2, n_h)
    e2 = summarise(r2, "E2 history at similar yield levels (10y 4.0-6.5%), 1962+", n_h,
                   {"id": "E2", "P_lo90": lo, "P_hi90": hi, "n_indep": int(mlev.sum()) // n_h, "in_headline": True,
                    "P_gap_fwd": float((cost_fwd(R + d2, D, A) > DEP1).mean())})
    est.append(e2)
    dists["E2"] = r2.sum(1)

    # ---------------------------------------------------------------- [S5] E3 Vasicek / AR(1) on the ladder yield
    shift_grid = None  # parallel shifts priced exactly below
    vas_rows = []
    be_rw_pct = -be_rw / 100.0

    def fit_ar(yy, label):
        r = AutoReg(yy, lags=1, trend="c").fit()
        c_hat, phi = float(r.params[0]), float(r.params[1])
        n = int(r.nobs)
        s_e = math.sqrt(float(r.sigma2))
        cov = np.asarray(r.cov_params())
        phi_bc = min(1.0, phi + (1 + 3 * phi) / n)
        theta = c_hat / (1 - phi)
        c_bc = theta * (1 - phi_bc)
        adf_p = float(adfuller(yy, regression="c", autolag="AIC")[1])

        def plug(cc, pp):
            if pp >= 1:
                m, v = 0.0, n_h * s_e ** 2
            else:
                m = (cc - (1 - pp) * yy[-1]) * (1 - pp ** n_h) / (1 - pp)
                v = s_e ** 2 * (1 - pp ** (2 * n_h)) / (1 - pp ** 2)
            return float(norm.cdf((be_rw_pct - m) / math.sqrt(v))), m, math.sqrt(v)

        p_ols, m_ols, s_ols = plug(c_hat, phi)
        p_bc, m_bc, s_bc = plug(c_bc, phi_bc)
        kap = lambda p: (-math.log(p) * 252) if p < 1 else 0.0
        row = {"sample": label, "n": n, "c": c_hat, "phi": phi, "se_phi": float(np.sqrt(cov[1, 1])),
               "phi_bc": phi_bc, "theta_pct": theta, "kappa_ols_per_yr": kap(phi), "kappa_bc_per_yr": kap(phi_bc),
               "half_life_ols_yr": math.log(2) / kap(phi) if phi < 1 else float("inf"),
               "half_life_bc_yr": math.log(2) / kap(phi_bc) if phi_bc < 1 else float("inf"),
               "sigma_bp_yr": s_e * 100 * math.sqrt(252), "adf_pvalue": adf_p,
               "drift_to_A_bp_ols": 100 * m_ols, "drift_to_A_bp_bc": 100 * m_bc, "sd_to_A_bp": 100 * s_bc,
               "P_plugin_ols": p_ols, "P_plugin_bc": p_bc, "y_today_pct": float(yy[-1])}
        return row, (c_bc, phi_bc, cov, s_e)

    for label, first in (("1962+", dates[0]), ("1990+", date(1990, 1, 2)), ("2000+", date(2000, 1, 3))):
        m = dates >= first
        rowv, pars_bc = fit_ar(y[m], label)
        vas_rows.append(rowv)
        if label == "1962+":
            c_bc, phi_bc, cov, s_e = pars_bc
    rng = np.random.default_rng([SEED, 3])
    M = 100_000
    draws = rng.multivariate_normal([c_bc, phi_bc], cov, size=M)
    cc, pp = draws[:, 0], draws[:, 1]
    rw = pp >= 1
    pp = np.where(rw, 1.0, pp)
    cc = np.where(rw, 0.0, cc)
    with np.errstate(divide="ignore", invalid="ignore"):
        mm = np.where(rw, 0.0, (cc - (1 - pp) * y[iD]) * (1 - pp ** n_h) / (1 - pp))
        vv = np.where(rw, n_h * s_e ** 2, s_e ** 2 * (1 - pp ** (2 * n_h)) / (1 - pp ** 2))
    shifts3 = mm + np.sqrt(vv) * rng.standard_normal(M)
    r3 = rungs_rw(R + shifts3[:, None], A)
    e3 = summarise(r3, "E3 one-factor Vasicek AR(1) on the ladder yield, 1962+, bias-corrected, parameter uncertainty",
                   n_h, {"id": "E3", "in_headline": True, "share_draws_random_walk": float(rw.mean()),
                         "mean_drift_bp": float(100 * mm.mean())})
    est.append(e3)
    dists["E3"] = r3.sum(1)
    v0 = vas_rows[0]
    say(f"\n[E3] Vasicek on the ladder yield (statsmodels AutoReg, daily):")
    for v in vas_rows:
        say(f"     {v['sample']:5s}: n {v['n']:,}; phi {v['phi']:.6f} (se {v['se_phi']:.6f}) -> bias-corrected "
            f"{v['phi_bc']:.6f}; theta {v['theta_pct']:.2f}%; kappa {v['kappa_ols_per_yr']:.3f}/yr (bc "
            f"{v['kappa_bc_per_yr']:.3f}); half-life {v['half_life_ols_yr']:.1f}y (bc {v['half_life_bc_yr']:.1f}y); "
            f"sigma {v['sigma_bp_yr']:.0f}bp/yr; ADF p {v['adf_pvalue']:.3f}; drift to {A} {v['drift_to_A_bp_ols']:+.1f}bp "
            f"(bc {v['drift_to_A_bp_bc']:+.1f}bp); plug-in P {fmt_p(v['P_plugin_ols'])} (bc {fmt_p(v['P_plugin_bc'])})")
    say(f"     predictive (1962+, bc, parameter uncertainty): {fmt_p(e3['P_gap'])}; {rw.mean():.1%} of parameter draws "
        f"are random walks; mean drift {100 * mm.mean():+.1f}bp")

    # ---------------------------------------------------------------- [S5] E4 PCA + VAR(1), 1990+
    K = [NAMES.index(k) for k in ("3 Mo", "6 Mo", "1 Yr", "2 Yr", "3 Yr", "5 Yr", "7 Yr", "10 Yr", "20 Yr", "30 Yr")]
    m90 = dates >= date(1990, 1, 2)
    Y = par[m90][:, K]
    dY = np.diff(Y, axis=0)
    C = np.cov(dY.T, ddof=1)
    w, V = np.linalg.eigh(C)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    L = V[:, :3] * np.sign(V[:, :3].sum(axis=0))
    shares = w[:3] / w.sum()
    Ym = Y.mean(axis=0)
    F = (Y - Ym) @ L
    U = (Y - Ym) - F @ L.T
    var = VAR(F).fit(1, trend="c")
    mu = var.forecast(F[-1:], steps=n_h)[-1]
    S = var.forecast_cov(steps=n_h)[-1]
    CU = np.cov(np.diff(U, axis=0).T, ddof=1) * n_h
    MK = interp_matrix(TT[K], TT)  # 12 x 10
    rng = np.random.default_rng([SEED, 4])
    N4 = 100_000
    Fh = rng.multivariate_normal(mu, S, size=N4)
    dU = rng.multivariate_normal(np.zeros(len(K)), CU, size=N4, method="eigh")
    d4 = ((Fh - F[-1]) @ L.T + dU) @ MK.T
    r4 = rungs_rw(R + d4, A)
    comp = np.abs(np.linalg.eigvals(var.coefs[0]))
    e4 = summarise(r4, "E4 three-factor curve model (PCA + VAR(1)), 1990+", n_h,
                   {"id": "E4", "in_headline": True, "mean_change_10y_bp": float(100 * d4[:, I10Y].mean()),
                    "sd_change_10y_bp": float(100 * d4[:, I10Y].std())})
    est.append(e4)
    dists["E4"] = r4.sum(1)
    rng = np.random.default_rng([SEED, 44])
    CF = np.cov(np.diff(F, axis=0).T, ddof=1) * n_h
    Fh_rw = rng.multivariate_normal(np.zeros(3), CF, size=N4)
    dU_rw = rng.multivariate_normal(np.zeros(len(K)), CU, size=N4, method="eigh")
    d4rw = (Fh_rw @ L.T + dU_rw) @ MK.T
    r4rw = rungs_rw(R + d4rw, A)
    e4rw = summarise(r4rw, "E4-RW same factors, no mean reversion (sensitivity)", n_h,
                     {"id": "E4-RW", "in_headline": False, "P_gap_fwd": float((cost_fwd(R + d4rw, D, A) > DEP1).mean())})
    say(f"\n[E4] PCA of daily changes 1990+: level/slope/curve explain {shares[0]:.1%} / {shares[1]:.1%} / "
        f"{shares[2]:.1%}. VAR(1) eigenvalue moduli {', '.join(f'{c:.5f}' for c in comp)} (half-lives "
        + ", ".join(f"{math.log(0.5) / math.log(c) / 252:.1f}y" for c in comp) + ")")
    say(f"     forecast to {A}: mean 10y change {e4['mean_change_10y_bp']:+.1f}bp, sd {e4['sd_change_10y_bp']:.0f}bp; "
        f"P {fmt_p(e4['P_gap'])}; random-walk version {fmt_p(e4rw['P_gap'])}")
    pca = {"variance_shares": [float(x) for x in shares], "loadings_tenors": [float(TT[k]) for k in K],
           "loadings": L.tolist(), "var_eigen_moduli": [float(c) for c in comp],
           "var_half_lives_yr": [float(math.log(0.5) / math.log(c) / 252) for c in comp],
           "forecast_mean_factor_change": (mu - F[-1]).tolist(), "n_obs": int(len(Y))}

    # ---------------------------------------------------------------- [S5] E5 MOVE
    mv = pd.read_csv(os.path.join(ROOT, "rab/data/m2/MOVE_yahoo_daily.csv"), index_col=0, parse_dates=True)["Close"]
    mv = mv[mv.index <= pd.Timestamp(D)].dropna()
    mv_dates = np.array([d.date() for d in mv.index])
    move_D = float(mv.iloc[-1])
    assert mv_dates[-1] == D, "MOVE close missing on the curve date"
    ok = np.array([dates[i] >= mv_dates[0] for i in st])
    rv, mvs = [], []
    for i, e in zip(st[ok], en[ok]):
        rv.append(math.sqrt(252 * np.mean(dy[i + 1:e + 1] ** 2)))
        j = np.searchsorted(mv_dates, dates[i], side="right") - 1
        mvs.append(float(mv.iloc[j]))
    rv, mvs = np.array(rv), np.array(mvs)
    ratio_mv = rv / mvs
    rho = float(np.median(ratio_mv))
    rq = [float(np.percentile(ratio_mv, q)) for q in (25, 50, 75)]
    rng = np.random.default_rng([SEED, 5])
    z5 = rng.standard_normal(100_000)

    def e5_for(rr):
        sh = rr * move_D * math.sqrt(n_h / 252)
        return sh, rungs_rw(R + (z5 * sh / 100)[:, None], A)

    sh5, r5 = e5_for(rho)
    e5 = summarise(r5, "E5 options-market volatility (MOVE, calibrated to the ladder)", n_h,
                   {"id": "E5", "in_headline": True, "sigma_h_bp": sh5, "rho": rho, "move_D": move_D,
                    "P_gap_fwd": float((cost_fwd(R + (z5 * sh5 / 100)[:, None], D, A) > DEP1).mean())})
    est.append(e5)
    dists["E5"] = r5.sum(1)
    e5_var = []
    for lab, rr in (("E5 rho = 1 (MOVE as is)", 1.0), ("E5 rho at its 25th pct", rq[0]), ("E5 rho at its 75th pct", rq[2])):
        s_, r_ = e5_for(rr)
        e5_var.append(summarise(r_, lab, n_h, {"id": lab.split()[0] + "-" + ("raw" if rr == 1.0 else lab.split()[-2]),
                                             "in_headline": False, "sigma_h_bp": s_}))
    # sensitivities added after the first run (not in the pre-registered set; see M2_SPEC changelog)
    import statsmodels.api as sm
    ols = sm.OLS(rv, sm.add_constant(mvs)).fit()
    a_, b_ = float(ols.params[0]), float(ols.params[1])
    rv_reg = a_ + b_ * move_D
    move_63 = float(mv.iloc[-63:].mean())
    for lab, sigma_yr in ((f"E5 regression calibration (RV = {a_:.1f} + {b_:.3f} x MOVE)", rv_reg),
                          (f"E5 MOVE 63-day average ({move_63:.1f}) x rho", rho * move_63)):
        s_ = sigma_yr * math.sqrt(n_h / 252)
        r_ = rungs_rw(R + (z5 * s_ / 100)[:, None], A)
        e5_var.append(summarise(r_, lab, n_h, {"id": "E5-" + ("reg" if "regression" in lab else "avg63"),
                                             "in_headline": False, "sigma_h_bp": s_}))
    say(f"\n[E5] MOVE on {D}: {move_D:.2f}. Realised ladder-yield vol / MOVE over {len(rv):,} windows since "
        f"{mv_dates[0]}: median {rho:.3f} (IQR {rq[0]:.3f}-{rq[2]:.3f}). sigma to {A}: {sh5:.1f}bp -> P {fmt_p(e5['P_gap'])}"
        f" (MOVE as is: {fmt_p(e5_var[0]['P_gap'])})")
    move_cal = {"regression_a": a_, "regression_b": b_, "regression_rv_bp_yr": rv_reg, "move_63d_avg": move_63,
                "move_D": move_D, "rho_median": rho, "rho_q25": rq[0], "rho_q75": rq[2], "n_windows": int(len(rv)),
                "sigma_h_bp": sh5, "sigma_bp_yr": rho * move_D, "move_first": str(mv_dates[0])}

    # ---------------------------------------------------------------- sensitivities (not headline)
    sens = [e4rw] + e5_var
    for j, (lab, mask, scale, demean) in enumerate((
            ("History 1962+, raw (no scaling, no demeaning)", np.ones(len(st), bool), False, False),
            ("History 1962+, demeaned, not rescaled", np.ones(len(st), bool), False, True),
            ("History 1990+, raw", np.array([dates[i] >= date(1990, 1, 2) for i in st]), False, False),
            ("History 1990+, demeaned", np.array([dates[i] >= date(1990, 1, 2) for i in st]), False, True),
            ("History 2000+, demeaned", np.array([dates[i] >= date(2000, 1, 3) for i in st]), False, True),
            ("History 2022+, demeaned", np.array([dates[i] >= date(2022, 1, 3) for i in st]), False, True),
            ("History similar-level, raw (not demeaned)", mlev, False, False),
            ("History 1962+ rescaled, not demeaned", np.ones(len(st), bool), True, False)), start=1):
        dd = delta[mask] * (k_s[mask][:, None] if scale else 1.0)
        if demean:
            dd = dd - dd.mean(axis=0)
        rr_ = rungs_rw(R + dd, A)
        sens.append(summarise(rr_, lab, n_h, {"id": f"S{j}", "in_headline": False,
                                               "n_indep": int(mask.sum()) // n_h,
                                               "P_gap_fwd": float((cost_fwd(R + dd, D, A) > DEP1).mean())}))
    # purchase on Mon 4 Jan 2027 instead of 1 Jan (h = 98 days, n_h + 1)
    A2 = date(2027, 1, 4)
    st98, en98 = windows(dates, D, (A2 - D).days)
    d98 = (sig[iD] / sig[st98])[:, None] * (par[en98] - par[st98])
    d98 -= d98.mean(axis=0)
    sens.append(summarise(rungs_rw(R + d98, A2), "E1 with purchase on Mon 4 Jan 2027 (98 days)", n_h + 1,
                          {"id": "S-E1-4Jan", "in_headline": False}))

    # ---------------------------------------------------------------- headline [S5]
    head_ps = [e["P_gap"] for e in est]
    P_head = float(np.median(head_ps))
    N_head = int(round(1 / P_head))
    say("\n[S5] Five headline estimators (RW convention, Nov-15 basis, purchase 1 Jan 2027):")
    for e in est:
        ci = f" (90% block-bootstrap {fmt_p(e['P_lo90'])}-{fmt_p(e['P_hi90'])})" if "P_lo90" in e else ""
        say(f"     {e['id']}: {fmt_p(e['P_gap'])}{ci}"
            + (f" [FWD {fmt_p(e['P_gap_fwd']).strip()}]" if "P_gap_fwd" in e else "")
            + f"; spread of rates to {A} (parallel-equivalent) sd {e['shift_eq_sd_bp']:.0f}bp, robust sd "
            f"{e['shift_eq_robust_sd_bp']:.0f}bp, mean {e['shift_eq_mean_bp']:+.1f}bp; P(gap > $10k) {fmt_p(e['P_gap_gt_10k'])}; mean gap if any "
            f"${e['mean_gap_given_gap']:,.0f}; gap p95 ${e['gap_p95']:,.0f}; P(a whole payment waits) "
            f"{e['P_gap_gt_rung2033']:.2%} - {e['estimator']}")
    say(f"     HEADLINE (median of five): {fmt_p(P_head)} = about 1 in {N_head}; range {fmt_p(min(head_ps))} - "
        f"{fmt_p(max(head_ps))}")
    say("     Sensitivities (not headline):")
    for e in sens:
        say(f"       {fmt_p(e['P_gap'])}  " + (f"[FWD {fmt_p(e['P_gap_fwd'])}] " if "P_gap_fwd" in e else "")
            + f"(sd {e['shift_eq_sd_bp']:.0f}bp, mean {e['shift_eq_mean_bp']:+.1f}bp) " + e["estimator"])
    res["headline"] = {"P_gap": P_head, "about_1_in": N_head, "range": [min(head_ps), max(head_ps)],
                       "estimators": {e["id"]: e["P_gap"] for e in est},
                       "median_gap_p95": float(np.median([e["gap_p95"] for e in est])),
                       "median_mean_gap_given_gap": float(np.median([e["mean_gap_given_gap"] for e in est])),
                       "median_P_gap_gt_10k": float(np.median([e["P_gap_gt_10k"] for e in est])),
                       "max_P_whole_payment_waits": float(max(e["P_gap_gt_rung2033"] for e in est))}
    res["estimators"] = est
    res["sensitivities"] = sens
    res["vasicek"] = vas_rows
    res["pca_var"] = pca
    res["move"] = move_cal

    # ---------------------------------------------------------------- [S7] reconciliation
    rec = reconcile(D, A, R, c_fwd, c_rw, be_fwd, P_head, est)
    res["reconciliation"] = rec

    # ---------------------------------------------------------------- [S8] fifteen months
    res["fifteen_months"], dist28 = fifteen_months(dates, par, sig, iD, D, A, B, R, h, h2, c_fwd)
    res["h13_h14"] = h13_h14(R, D, A, B)

    # ---------------------------------------------------------------- write
    write_outputs(res, est, sens, vas_rows, dates, st, en, y, delta, k_s, y10s, mlev, d1, r1, r2, sig)
    if not args.no_figs:
        import m2_figures
        m2_figures.make_all(res, dists, dist28, dates, y, sig, vas_rows, OUT)
    open(os.path.join(OUT, "m2_report.txt"), "w").write("\n".join(REPORT) + "\n")


def tsy_rows_raw_row(D):
    """The raw CSV row of D as M1's loader produces it (for M1's Curve)."""
    f = os.path.join(ROOT, f"rab/data/treasury_par_2000_2026/{D.year}.csv")
    if D.year < 2000:
        f = os.path.join(ROOT, f"rab/data/treasury_par_1990_1999/{D.year}.csv")
    for r in csv.DictReader(open(f)):
        m, d, yy = r["Date"].split("/")
        if date(int(yy), int(m), int(d)) == D:
            r["_date"] = D
            return r
    raise KeyError(D)


# ------------------------------------------------------------------------------------------------ [S7]
def reconcile(D, A, R, c_fwd, c_rw, be_fwd, P_head, est):
    say("\n[S7] Reconciliation with insight_v1's 'about 1 in 3'")
    rows = []

    def d1_lognormal(path, last_date, pays, label, centre="fwd"):
        rr = []
        for r in csv.DictReader(open(path)):
            m, d, yy = r["Date"].split("/")
            dt = date(int(yy), int(m), int(d))
            if dt.year == last_date.year and dt <= last_date:
                rr.append((dt, to_par12({k: float(r[k]) for k in NAMES if r.get(k) not in (None, "", "N/A")})))
        rr.sort()
        vals = np.array([cost_fwd(p[None, :], dt, A, pays)[0] for dt, p in rr])
        vol = float(np.diff(np.log(vals)).std(ddof=1) * math.sqrt(252))
        t = (A - last_date).days / 365.25
        base = vals[-1] if centre == "fwd" else float(cost_rw(rr[-1][1][None, :], A)[0])
        p = float(1 - norm.cdf(math.log(DEP1 / base) / (vol * math.sqrt(t))))
        return {"row": label, "P": p, "base": float(base), "vol": vol, "t": t, "n_days": len(rr)}

    v1 = os.path.join(ROOT, "research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv")
    cur = os.path.join(ROOT, f"rab/data/treasury_par_2000_2026/{D.year}.csv")
    r1 = d1_lognormal(v1, date(2026, 9, 25), None, "R1 D1 [6] 25 Sep: lognormal, forward centre, 2026 vol")
    r2 = d1_lognormal(cur, D, None, f"R2 D1 [6] on {D}: same method")
    r2e = d1_lognormal(cur, D, exact(), f"R2e same, exact 1 Jan basis (not buyable)")
    r5 = d1_lognormal(cur, D, None, f"R5 R2 with the no-view centre (yields unchanged)", centre="rw")
    for r in (r1, r2, r2e):
        rows.append(r)
    # R3 strategy_mc_v2 (a): Normal(0, 0.37pp) parallel shift, FWD
    R25 = None
    for r in csv.DictReader(open(v1)):
        if r["Date"] == "09/25/2026":
            R25 = to_par12({k: float(r[k]) for k in NAMES if r.get(k) not in (None, "", "N/A")})[None, :]
    D25 = date(2026, 9, 25)
    be25 = breakeven(lambda b: cost_fwd(R25 + b, D25, A)[0])
    rows.append({"row": "R3 strategy_mc_v2 (a) 25 Sep: parallel shift sd 37bp, forward centre",
                 "P": float(norm.cdf(-be25 / 37.0)), "breakeven_bp": be25})
    rows.append({"row": f"R3' same on {D}", "P": float(norm.cdf(-be_fwd / 37.0)), "breakeven_bp": be_fwd})
    # R4 AX1b [C]
    def dgs10(path):
        ds, ys = [], []
        for r in csv.DictReader(open(path)):
            if r["DGS10"] not in ("", "."):
                ds.append(date.fromisoformat(r["observation_date"]))
                ys.append(float(r["DGS10"]))
        return np.array(ds), np.array(ys)

    ax = {}
    for tag, path in (("insight_v1 file", os.path.join(ROOT, "research/insight_v1/scripts/data/D3/fred_DGS10.csv")),
                      ("rab/data file", os.path.join(ROOT, "rab/data/fred/DGS10.csv"))):
        ds, ys = dgs10(path)
        hh = 68
        chg = ys[hh:] - ys[:-hh]
        start = ds[:-hh]
        for since in (1962, 1990, 2000):
            mk = start >= date(since, 1, 1)
            for x in (19, 26):
                ax[f"{tag} since {since} >= {x}bp"] = float((chg[mk] <= -x / 100).mean())
    rows.append({"row": "R4 AX1b [C]: 68-trading-day falls in FRED DGS10 >= X bp", "P": None, "detail": ax})
    rows.append(r5)
    rows.append({"row": "R6 M2 headline: median of E1-E5 (no-view centre)", "P": P_head})
    for r in rows:
        if r.get("P") is not None:
            extra = (f" (base ${r['base']:,.0f}, vol {r['vol'] * 100:.2f}%/yr, t {r['t']:.3f}y)" if "vol" in r
                     else (f" (break-even {r['breakeven_bp']:.2f}bp)" if "breakeven_bp" in r else ""))
            say(f"     {fmt_p(r['P'])}  {r['row']}{extra}")
        else:
            say(f"     {r['row']}:")
            for k, v in r["detail"].items():
                say(f"         {k}: {v:.1%}")
    wf = [("insight_v1 '1 in 3' basis (25 Sep curve, 19bp headroom)", r1["P"]),
          ("curve moved up by 28 Sep (26bp headroom)", r2["P"]),
          ("no view on rates: yields unchanged, not forwards", r5["P"]),
          ("volatility and curve shape from five methods (M2 headline)", P_head)]
    say("     Waterfall: " + " -> ".join(f"{lab} {fmt_p(p).strip()}" for lab, p in wf))
    return {"rows": rows, "waterfall": [{"step": lab, "P": p} for lab, p in wf]}


# ------------------------------------------------------------------------------------------------ [S8]
def fifteen_months(dates, par, sig, iD, D, A, B, R, h, h2, c_fwd):
    say(f"\n[S8] Fifteen months: rate moves to {A} and {B} (history), longest-first top-up, floor and stock fund")
    st, en1 = windows(dates, D, h2)
    en1 = np.searchsorted(dates, [dates[i] + timedelta(days=h) for i in st], side="right") - 1
    en2 = np.searchsorted(dates, [dates[i] + timedelta(days=h2) for i in st], side="right") - 1
    d1 = par[en1] - par[st]
    d2 = par[en2] - par[st]
    k = (sig[iD] / sig[st])[:, None]
    lev = (par[st, I10Y] >= 4.0) & (par[st, I10Y] <= 6.5)
    out, dist = [], {}

    def run(c1, c2, label):
        rc = rungs_rw(c1, A)
        rev = rc[:, ::-1]
        before = np.cumsum(rev, axis=1) - rev
        bought = np.clip((DEP1 - before) / rev, 0, 1)
        unb = (1 - bought)[:, ::-1]
        T = (unb * PAY * np.exp(lndf_at(lndf_nodes(c2), taus(nov15(), B)))).sum(axis=1)
        left = np.maximum(0.0, DEP1 - rc.sum(axis=1))
        y1 = c1[:, I1Y] / 100
        y5 = c2[:, I5Y] / 100
        G = DEP2 + left * (1 + y1) - T
        Fc = DEP2 / (1 + y5) ** 5
        S = np.maximum(0.0, G - Fc)
        face = np.where(G >= Fc, DEP2, G * (1 + y5) ** 5)
        q = lambda a, p: float(np.percentile(a, p))
        o = {"variant": label, "n_windows": int(len(S)), "fund_p5": q(S, 5), "fund_p50": q(S, 50),
             "fund_p95": q(S, 95), "P_fund_lt_20k": float((S < 20_000).mean()), "P_fund_zero": float((S <= 0).mean()),
             "P_topup": float((T > 0).mean()), "mean_topup_given_topup": float(T[T > 0].mean()) if (T > 0).any() else 0.0,
             "floor_cost_p5": q(Fc, 5), "floor_cost_p50": q(Fc, 50), "floor_cost_p95": q(Fc, 95),
             "P_floor_face_below_150k": float((face < DEP2 - 0.5).mean())}
        return o, S

    for label, c1, c2 in (("H-FHS (rescaled to today's volatility, demeaned)",
                           R + (k * d1 - (k * d1).mean(0)), R + (k * d2 - (k * d2).mean(0))),
                          ("H-LVL (10y 4.0-6.5% at start, demeaned)",
                           R + (d1[lev] - d1[lev].mean(0)), R + (d2[lev] - d2[lev].mean(0))),
                          ("H-RAW (all windows, as history happened)", R + d1, R + d2)):
        o, S = run(c1, c2, label)
        out.append(o)
        dist[label.split()[0]] = S
    base_rw, _ = run(R, R, "base: yields unchanged to both dates (RW)")
    # FWD base check: leftover = 300k - Cost_FWD(R), today's 1y and 5y
    left = DEP1 - c_fwd
    Fb = DEP2 / (1 + R[0, I5Y] / 100) ** 5
    S_fwd = left * (1 + R[0, I1Y] / 100) + DEP2 - Fb
    say(f"     check (FWD base, E6/M1 F method): stock fund ${S_fwd:,.0f} (numbers.yaml $40,736), floor ${Fb:,.0f} "
        f"(numbers.yaml $117,194); RW base (yields unchanged to both dates): fund ${base_rw['fund_p50']:,.0f}")
    if D == date(2026, 9, 28):
        assert abs(S_fwd - 40_736) < 1 and abs(Fb - 117_194) < 1, (S_fwd, Fb)
    for o in out:
        say(f"     {o['variant']}: {o['n_windows']:,} windows; stock fund p5/p50/p95 ${o['fund_p5']:,.0f} / "
            f"${o['fund_p50']:,.0f} / ${o['fund_p95']:,.0f}; P(fund < $20k) {o['P_fund_lt_20k']:.1%}; P(no fund) "
            f"{o['P_fund_zero']:.1%}; P(top-up) {o['P_topup']:.1%}; floor cost p5/p95 ${o['floor_cost_p5']:,.0f} / "
            f"${o['floor_cost_p95']:,.0f}; floor below $150k in {o['P_floor_face_below_150k']:.1%}")
    return {"variants": out, "base_rw": base_rw, "base_fwd_fund": S_fwd, "base_fwd_floor": Fb,
            "window_first": str(dates[st[0]]), "window_last": str(dates[st[-1]])}, dist


def h13_h14(R, D, A, B):
    say(f"\n[S8] Re-check of WS4-owned references on the {D} curve (FWD convention, as D1/E6)")
    rows = []
    y5 = R[0, I5Y] / 100
    for b in (-50, -100, -150):
        c = R + b / 100
        rf = rungs_fwd(c, D, A)[0]
        gap = rf.sum() - DEP1
        nodes = lndf_nodes(c)
        la, lb = lndf_at(nodes, taus([A, B], D))[0]
        top = max(gap, 0) * math.exp(la - lb)
        for lab5, yy5 in (("5y unchanged", y5), ("5y also lower", y5 + b / 10000)):
            Fc = DEP2 / (1 + yy5) ** 5
            G = DEP2 - top
            fund = max(0.0, G - Fc)
            face = DEP2 if G >= Fc else G * (1 + yy5) ** 5
            rows.append({"shift_bp": b, "five_year": lab5, "gap_2027": gap, "topup_2028": top, "floor_cost": Fc,
                         "stock_fund": fund, "floor_face": face,
                         "unfunded_2033_if_no_deposit": gap / rf[0] * PAY if 0 < gap < rf[0] else None})
            say(f"     {b:+d}bp ({lab5:13s}): gap ${gap:,.0f}; top-up Jan 2028 ${top:,.0f}; floor cost ${Fc:,.0f}; "
                f"stock fund ${fund:,.0f}; floor face ${face:,.0f}"
                + (f"; H14 no deposit: ${gap / rf[0] * PAY:,.0f} of the 2033 payment unfunded" if 0 < gap < rf[0]
                   and lab5 == "5y unchanged" else ""))
    return rows


# ------------------------------------------------------------------------------------------------ outputs
def write_outputs(res, est, sens, vas_rows, dates, st, en, y, delta, k_s, y10s, mlev, d1, r1, r2, sig):
    cols = ["id", "estimator", "in_headline", "P_gap", "P_lo90", "P_hi90", "P_gap_fwd", "P_gap_gt_5k", "P_gap_gt_10k",
            "P_gap_gt_rung2033", "mean_gap_given_gap", "gap_p90", "gap_p95", "gap_p99", "cost_p5", "cost_p50",
            "cost_p95", "n_scenarios", "n_indep"]
    with open(os.path.join(OUT, "m2_estimators.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for e in est + sens:
            w.writerow([round(e[c], 6) if isinstance(e.get(c), float) else e.get(c, "") for c in cols])
    with open(os.path.join(OUT, "m2_vasicek_fits.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(vas_rows[0]))
        w.writeheader()
        for v in vas_rows:
            w.writerow({k: (round(x, 8) if isinstance(x, float) else x) for k, x in v.items()})
    with open(os.path.join(OUT, "m2_reconciliation.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["row", "P", "detail"])
        for r in res["reconciliation"]["rows"]:
            det = {k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items() if k not in ("row", "P")}
            w.writerow([r["row"], "" if r["P"] is None else round(r["P"], 4), json.dumps(det)])
        for s in res["reconciliation"]["waterfall"]:
            w.writerow(["waterfall: " + s["step"], round(s["P"], 4), ""])
    with open(os.path.join(OUT, "m2_2028_horizon.csv"), "w", newline="") as f:
        rows = res["fifteen_months"]["variants"] + [res["fifteen_months"]["base_rw"]]
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(x, 4) if isinstance(x, float) else x) for k, x in r.items()})
    with open(os.path.join(OUT, "m2_h13_h14_recheck.csv"), "w", newline="") as f:
        rows = res["h13_h14"]
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(x, 2) if isinstance(x, float) else x) for k, x in r.items()})
    c1 = r1.sum(1)
    c2 = np.full(len(st), np.nan)
    c2[mlev] = r2.sum(1)
    with open(os.path.join(OUT, "m2_history_windows.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["start", "end", "y10_start_pct", "ladder_yield_start_pct", "d_ladder_yield_bp", "ewma_vol_start_bp_yr",
                    "k_scale", "cost_E1", "cost_E2"])
        for j, (i, e) in enumerate(zip(st, en)):
            w.writerow([dates[i], dates[e], f"{y10s[j]:.2f}", f"{y[i]:.4f}", f"{100 * (y[e] - y[i]):.2f}",
                        f"{sig[i] * math.sqrt(252):.1f}", f"{k_s[j]:.4f}", f"{c1[j]:.0f}",
                        "" if np.isnan(c2[j]) else f"{c2[j]:.0f}"])
    json.dump(res, open(os.path.join(OUT, "m2_results.json"), "w"), indent=1, default=str)
    proposed_numbers(res)


def proposed_numbers(res):
    """Candidate numbers.yaml entries for WS1 (the only writer). Same fields as the Gate A file."""
    m = res["meta"]
    hd = res["headline"]
    b = res["base"]
    lo, hi = hd["range"]
    r5 = lambda p: int(5 * round(100 * p / 5))
    common = {"scale": "laura_plan", "status": "MODEL", "curve_date": m["curve_date"], "valuation_date": m["purchase_date"],
              "maturity_convention": "15 Nov of the year before each payment (STRIPS maturity dates)",
              "instrument_basis": "zero-coupon ladder on the par-derived zero curve (D1 method); MODEL, no dealer mark-up",
              "as_of": m["curve_date"]}
    fm = res["fifteen_months"]["variants"]
    ent = {
        "laura.rates.gap_odds_2027": {
            "value": round(hd["P_gap"], 4), "unit": "probability",
            "quote_as": f"about 1 in {hd['about_1_in']} (MODEL; five methods give {r5(lo)}-{r5(hi)}%)",
            "method": "rab/models/M2_SPEC.md s5 (median of E1-E5, no-view centre)",
            "source": "rab/models/m2_rate_paths.py -> rab/results/M2/m2_results.json headline",
            "note": "Chance the ten payments cost more than $300,000 on 1 Jan 2027. Replaces ref.H5 ('about 1 in 3', "
                    "25 Sep) and ref.H6 (24.2%, forward centre and 2026 volatility). Never in a WInS note."},
        "laura.rates.gap_odds_2027_range": {
            "value": [round(lo, 4), round(hi, 4)], "unit": "probability (min, max of E1-E5)",
            "quote_as": f"between about {r5(lo)}% and {r5(hi)}% depending on the method",
            "method": "rab/models/M2_SPEC.md s5", "source": "m2_results.json headline.range"},
        "laura.rates.cost_2027_yields_unchanged": {
            "value": round(b["cost_rw"], 2), "unit": "USD",
            "quote_as": f"about ${1000 * round(b['cost_rw'] / 1000):,.0f} if yields stay where they are",
            "method": "rab/models/M2_SPEC.md s3.2 (RW)", "source": "m2_results.json base.cost_rw",
            "note": "Higher than laura.ladder.cost_2027_strips (forward rates come true): each bond is 3 months shorter "
                    "and rolls down an upward-sloping curve."},
        "laura.rates.breakeven_fall_bp_yields_unchanged": {
            "value": round(b["breakeven_fall_bp_rw"], 2), "unit": "basis points",
            "quote_as": f"about {round(b['breakeven_fall_bp_rw'])}bp",
            "method": "rab/models/M2_SPEC.md s3.2", "source": "m2_results.json base.breakeven_fall_bp_rw",
            "note": "Parallel fall of the par curve on the purchase day that makes the ladder cost $300,000."},
        "laura.rates.gap_if_any_2027": {
            "value": {"median_mean_gap_given_gap": round(hd["median_mean_gap_given_gap"]),
                      "median_gap_p95": round(hd["median_gap_p95"]),
                      "max_P_whole_payment_waits": round(hd["max_P_whole_payment_waits"], 5)},
            "unit": "USD (2027 dollars)",
            "quote_as": f"if there is a shortfall it is typically about ${1000 * round(hd['median_mean_gap_given_gap'] / 1000):,.0f}"
                        ", paid from the 2028 deposit",
            "method": "rab/models/M2_SPEC.md s6 (medians over E1-E5)", "source": "m2_results.json headline"},
        "laura.rates.stock_fund_2028_range": {
            "value": {v["variant"].split()[0]: [round(v["fund_p5"]), round(v["fund_p50"]), round(v["fund_p95"])] for v in fm},
            "unit": "USD on 1 Jan 2028 (p5, p50, p95)", "valuation_date": "2028-01-01",
            "quote_as": "typically about $" + f"{1000 * round(np.median([v['fund_p50'] for v in fm]) / 1000):,.0f}" +
                        "; under $20,000 in about 1 in " +
                        f"{round(1 / np.median([v['P_fund_lt_20k'] for v in fm]))} rate paths",
            "method": "rab/models/M2_SPEC.md s8", "source": "m2_results.json fifteen_months",
            "note": "History of 15-month curve moves; floor = $150,000 face repaid by late 2032 if affordable (E6 rule; "
                    "see inventory F4 for the IPS 'whole remainder' wording)."},
    }
    lines = ["# Proposed numbers.yaml entries from M2 (WS4). WS1 is the only writer: WS0/WS1 review, then add with a",
             "# changelog line and a new lock hash. Nothing here is in numbers.yaml yet.",
             f"# Generated {m['generated_et']} ({m['generated_sydney']}) by rab/models/m2_rate_paths.py", "proposed:"]
    import yaml
    body = {k: {**common, **v} for k, v in ent.items()}
    body["retire"] = {"ref.H5.one_in_three": "superseded by laura.rates.gap_odds_2027",
                      "ref.H6.gap_odds_28sep": "reproduced (R2); superseded by laura.rates.gap_odds_2027 as the quoted figure",
                      "ref.H13.rates_fall_first": "re-checked on 28 Sep in rab/results/M2/m2_h13_h14_recheck.csv",
                      "ref.H14.joint_tail_no_deposit": "reproduced on 28 Sep in rab/results/M2/m2_h13_h14_recheck.csv"}
    txt = yaml.safe_dump(body, sort_keys=False, width=120, allow_unicode=False)
    open(os.path.join(OUT, "m2_proposed_numbers.yaml"), "w").write(
        "\n".join(lines) + "\n" + "\n".join("  " + ln for ln in txt.splitlines()) + "\n")


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
