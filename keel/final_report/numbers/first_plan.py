"""The first plan, re-run: how a share-led plan missed its payments (numbers owner, Mon 16 Nov 2026, Sydney). MODEL, not
a forecast or a promise. NUMBERS 8s.

Run from the repo root:  python3 -I keel/final_report/numbers/first_plan.py
   or from this folder:  python3 -I first_plan.py
Writes keel/final_report/numbers/results_first_plan_2026-11-16.json and prints the figures (about 10 seconds, numpy only).
Imports the 27 Sep model (keel/library/verified_2026-09-27/strategy_mc.py) by its path and engine.py, plan.py and
completion.py; changes none of them, writes no bytecode beside them, reads no results file and writes no other file.

The question. The Team Reflection (3f) tells how the team's first plan (team notes, Sun 27 Sep 2026,
keel/library/council_2026-09-27/team_notes_2026-09-27.md: a growth clock 2027-2031 at about 75% shares, a glide path
down to 20-25% shares by the eve of 2033, then a Treasury "Payment Ladder" bought from 2033) was tested on 27 Sep, before
any trade, by strategy_mc.py's Strategy G ("growth first, buy the reserve in 2033"), and missed at least one of the ten
$50,000 payments in 3.2% of simulated markets, 13.7% if the 2028 deposit was $75,000 and 40.8% if it never came.

Part A, the 27 Sep model exactly. The model is imported, its three figures asserted, and its draws rebuilt in the same
order (asserted equal to simulate("G")'s surplus, path by path) so that every miss can be taken apart:
  * which payment goes unpaid first, if the money on 1 Jan 2033 buys the ten in date order (2033 first);
  * the size of the shortfall in the failing paths;
  * what drives it: each year's return and the 2033 yield, as an exact split of the log gap from the model's central
    path (every return at its median, the 2033 yield at 5.26%); shares down over the four years at 75% (2027-2030); a
    single year with shares down 20% or more; the year of the worst share return;
  * two example paths.
  The model has no share returns after 2032: the growth-first design buys the ten in January 2033 (its glide ends at 40%
  shares in 2032), so every miss is decided on that one date. No share is sold to pay a payment date.

Part A2, the same design on US stock history (Keel's replay, not run on 27 Sep): shares = US stocks with dividends
(Shiller monthly, the register's history file, every 72-month window since 1871); the bond part at the 27 Sep model's
central 4.00% a year and the ten bought on 1 Jan 2033 at its central 5.26% flat (rates fixed, as the register's history
model keeps rates at forwards). Also on the register's basis: bonds rolled in 1-year Treasuries at the 6 Nov forwards,
the ten bought at the 6 Nov forwards, VT's 0.06% fee.

Part B, the same design on today's engine (Keel's re-run, MODEL): the register's house model (plan.draws, 200,000 paths,
seed 2033: VT median 7.5% a year, 17.88% spread; yields parallel, 0.9 points a year, apart from shares), the 6 Nov 2026
curve. The design is the 27 Sep one: $300,000 in January 2027, the 2028 deposit added in January 2028, shares 75% /
75% / 75% / 75% / 60% / 40% for 2027-2032, rebalanced each January; the rest in 1-year Treasuries rolled each January at
that day's rate (variant: a Treasury fund of 6.95 years' duration, IEF-like); on 1 Jan 2033 the ten bought at that day's
curve (each payment discounted from 1 Jan 2033 on the 6 Nov curve moved by the path's yield change, par yields floored
at zero). The paths are the register's own: VT's 2028-2030 and 2031-2032 growth and the yield moves to 2031 are
plan.draws' exactly, split into years by Brownian bridges; VT's 2027 growth and the yield moves of 2031-2032 are extra
draws (seed 2027). So, path by path, Caplet's plan (plan.run, completion.rule) can be read beside the first plan.
"""
import csv
import importlib.util
import inspect
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

sys.dont_write_bytecode = True       # write no __pycache__ beside the 27 Sep model or the engine
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

RUN = "Mon 16 Nov 2026 (Sydney)"
OUTFILE = HERE / f"results_first_plan_{C.RESULTS}.json"   # Tue 17 Nov evening re-run; the 2026-11-16 file is the record
SRC = E.ROOT / "keel/library/verified_2026-09-27/strategy_mc.py"
YEARS6 = list(range(2027, 2033))
PAY_YEARS = list(range(2033, 2043))
SEED_EXTRA = 2027
IEF_DUR = 6.95            # IEF effective duration, fact sheet as of 30 Jun 2026 (CLAUDE.md "Key facts", VERIFIED 27 Sep)


def q(a, ps=(5, 50, 95)):
    a = np.asarray(a, float)
    return [float(np.percentile(a, p)) for p in ps] if a.size else None


def r0(x):
    return float(round(float(x)))


# ================================================================ Part A: the 27 Sep model, exactly
spec = importlib.util.spec_from_file_location("strategy_mc_27sep", SRC)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

sig = inspect.signature(M.simulate).parameters
GLIDE = sig["glide"].default
RATE_SD = sig["rate_sd"].default
SIM_SRC = inspect.getsource(M.simulate)
assert M.PATHS == 200_000 and M.SEED == 20260927 and M.RHO == -0.01
assert M.LADDER_COST_2027 == 292_264 and M.Y2 == 0.0481
assert GLIDE == (0.75, 0.75, 0.75, 0.75, 0.60, 0.40) and RATE_SD == 0.010
assert "rate33 = 0.0526 + rate_sd * rng.standard_normal(PATHS)" in SIM_SRC
assert np.allclose(M.EQ, M.lognorm_params(0.0670, 0.0794)) and np.allclose(M.BD, M.lognorm_params(0.0400, 0.0406))
R33 = 0.0526

inputs27 = {
    "file": "keel/library/verified_2026-09-27/strategy_mc.py (imported by path, unchanged)",
    "paths": M.PATHS, "seed": M.SEED,
    "curve": "official Treasury par curve of Fri 25 Sep 2026 (competition/official_market_data/), via the ladder cost "
             "$292,264 at 1 Jan 2027 and the 2y par yield 4.81%; the growth-first design uses neither",
    "shares": "J.P. Morgan 2026 LTCMA, U.S. large cap: 6.70% compound, 7.94% arithmetic, 16.47% volatility; lognormal "
              "with log mean/sd solved so compound and arithmetic match",
    "shares_log_mean_sd": [float(M.EQ[0]), float(M.EQ[1])],
    "bonds": "J.P. Morgan 2026 LTCMA, U.S. intermediate Treasuries: 4.00% compound, 4.06% arithmetic (3.48% vol)",
    "bonds_log_mean_sd": [float(M.BD[0]), float(M.BD[1])],
    "correlation": M.RHO,
    "glide_share_weight_2027_to_2032": list(GLIDE),
    "rebalanced": "each year; no fees, no taxes",
    "deposits": "$300,000 on 1 Jan 2027; the 2028 deposit added on 1 Jan 2028 before that year's return",
    "ten_in_2033": "annuity-due of ten $50,000 at a flat yield 5.26% + N(0, 1.0 point), floored at zero (ASSUMPTION in "
                   "the script: flat curve in 2033)",
    "miss": "the money on 1 Jan 2033 is below the cost of the ten that day (P(payments not fully funded))",
    "lock_early_L": "Strategy L's shortfall_prob is set to 0.0 in the code ('ladder covers all ten payments by "
                    "construction'); it is an assumption of the 27 Sep model, not a tested result",
}


def draws27(deposit=150_000.0, rate_sd=RATE_SD, eq_mu_shift=0.0):
    """strategy_mc.simulate('G')'s draws and arithmetic, in its order, returning every intermediate."""
    rng = np.random.default_rng(M.SEED)
    z1 = rng.standard_normal((M.PATHS, 6)); z2 = rng.standard_normal((M.PATHS, 6))
    ze = z1; zb = M.RHO * z1 + np.sqrt(1 - M.RHO ** 2) * z2
    req = np.exp(M.EQ[0] + eq_mu_shift + M.EQ[1] * ze - 0) - 1
    rbd = np.exp(M.BD[0] + M.BD[1] * zb) - 1
    rate33 = 0.0526 + rate_sd * rng.standard_normal(M.PATHS)
    reserve = M.annuity_due(np.maximum(rate33, 0.0))
    v = np.full(M.PATHS, 300_000.0)
    pot = []
    for y in range(6):
        if y == 1:
            v += deposit
        w = GLIDE[y]
        v *= 1 + w * req[:, y] + (1 - w) * rbd[:, y]
        pot.append(v.copy())
    return dict(req=req, rbd=rbd, rate33=rate33, reserve=reserve, v=v, surplus=v - reserve, pot=np.array(pot).T)


CASES27 = {"base": {}, "deposit_75k": {"deposit_2028": 75_000}, "deposit_0": {"deposit_2028": 0},
           "shares_5pct": {"eq_mu_shift": np.log(1.05) - np.log(1.067)}, "rate_sd_1_5": {"rate_sd": 0.015}}
reproduce = {}
for key, kw in CASES27.items():
    g = M.simulate("G", **kw)
    ell = M.simulate("L", **kw)
    reproduce[key] = {"G_shortfall_prob": g["shortfall_prob"], "G_paths_short": int((g["surplus"] < 0).sum()),
                      "G_surplus_p5_p25_p50_p75_p95_rounded": M.pct(g["surplus"]),
                      "L_shortfall_prob_hardcoded": ell["shortfall_prob"]}
assert round(reproduce["base"]["G_shortfall_prob"] * 100, 1) == 3.2
assert round(reproduce["deposit_75k"]["G_shortfall_prob"] * 100, 1) == 13.7
assert round(reproduce["deposit_0"]["G_shortfall_prob"] * 100, 1) == 40.8
assert reproduce["base"]["G_surplus_p5_p25_p50_p75_p95_rounded"] == {5: 20000, 25: 131000, 50: 226000, 75: 338000,
                                                                        95: 540000}
assert round(reproduce["shares_5pct"]["G_shortfall_prob"] * 100, 1) == 5.5
assert round(reproduce["rate_sd_1_5"]["G_shortfall_prob"] * 100, 1) == 3.5
for key in reproduce:
    reproduce[key]["one_in"] = 1 / reproduce[key]["G_shortfall_prob"]
    reproduce[key]["G_surplus_p5_p25_p50_p75_p95_rounded"] = {str(k): v for k, v in
                                                              reproduce[key]["G_surplus_p5_p25_p50_p75_p95_rounded"].items()}

PRICE_T = np.arange(10)


def unit_prices(rate):
    """Price on 1 Jan 2033 of each of the ten $50,000 payments at the model's flat yield (annuity-due, as the model)."""
    return 50_000 / (1 + np.maximum(rate, 0.0)[..., None]) ** PRICE_T


def first_unpaid(pot, prices):
    """Buying the ten in date order (2033 first) with the money on 1 Jan 2033: the first year not fully bought (0 = none)
    and how many are fully bought."""
    cum = np.cumsum(prices, axis=-1)
    n_full = (cum <= pot[..., None] + 1e-9).sum(-1)
    return np.where(n_full < 10, 2033 + n_full, 0), n_full


def decompose27(deposit):
    d = draws27(deposit)
    g = M.simulate("G", deposit_2028=deposit)
    assert np.allclose(d["surplus"], g["surplus"], rtol=0, atol=1e-6)
    miss = d["surplus"] < 0
    nmiss = int(miss.sum())
    short = -d["surplus"][miss]
    prices = unit_prices(d["rate33"])
    fu, n_full = first_unpaid(d["v"], prices)
    out = {"deposit_2028": deposit, "paths": M.PATHS, "paths_short": nmiss, "share_short": nmiss / M.PATHS,
           "one_in": M.PATHS / nmiss if nmiss else None}
    out["shortfall_failing_paths"] = {
        "median": float(np.median(short)), "p95_1_in_20_largest": float(np.percentile(short, 95)),
        "largest": float(short.max()), "mean": float(short.mean()),
        "median_share_of_ten_cost": float(np.median(short / d["reserve"][miss])),
        "share_under_10k": float((short < 10_000).mean()), "share_under_one_payment_50k": float((short < 50_000).mean())}
    out["first_unpaid_year_date_order"] = {str(y): int((fu[miss] == y).sum()) for y in PAY_YEARS}
    out["payments_fully_bought_in_failing_paths_p5_p50"] = [float(np.percentile(n_full[miss], 5)),
                                                            float(np.median(n_full[miss]))]
    out["ten_cost_2033_central"] = float(M.annuity_due(np.array([R33]))[0])
    out["pot_2033_p5_p50_p95"] = q(d["v"])
    return d, miss, out


d27, miss27, dec = decompose27(150_000.0)
A = {"base": dec}
for dep in (75_000.0, 0.0):
    _, _, o = decompose27(dep)
    A[f"deposit_{int(dep // 1000)}k"] = o
assert A["base"]["paths_short"] == reproduce["base"]["G_paths_short"]

# ---- what drives the miss (base case)
req, rbd, rate33, reserve, v = d27["req"], d27["rbd"], d27["rate33"], d27["reserve"], d27["v"]
geq_c, gbd_c = math.exp(M.EQ[0]) - 1, math.exp(M.BD[0]) - 1          # medians: 6.70% and 4.00%
W = np.array(GLIDE)
gy = W * req + (1 - W) * rbd                                          # each year's portfolio return
gy_c = W * geq_c + (1 - W) * gbd_c
dep = 150_000.0
cen_pot = (300_000 * (1 + gy_c[0]) + dep) * np.prod(1 + gy_c[1:])
cen_cost = float(M.annuity_due(np.array([R33]))[0])
contrib = np.empty((M.PATHS, 7))
contrib[:, 0] = np.log(300_000 * (1 + gy[:, 0]) + dep) - math.log(300_000 * (1 + gy_c[0]) + dep)
contrib[:, 1:6] = np.log1p(gy[:, 1:]) - np.log1p(gy_c[1:])
contrib[:, 6] = -(np.log(reserve) - math.log(cen_cost))
total = np.log(v / reserve) - math.log(cen_pot / cen_cost)
assert np.allclose(contrib.sum(1), total, atol=1e-10)
labels = [str(y) for y in YEARS6] + ["2033 yield"]
mc = contrib[miss27].mean(0)
drivers = {"central_path": {"pot_2033": cen_pot, "ten_cost_2033": cen_cost, "surplus": cen_pot - cen_cost,
                            "pot_over_cost": cen_pot / cen_cost,
                            "share_return_median": geq_c, "bond_return_median": gbd_c},
           "log_gap_failing_mean": float(total[miss27].mean()),
           "log_gap_share_by_part_failing_mean": {k: float(x / mc.sum()) for k, x in zip(labels, mc)},
           "log_gap_share_four_75pct_years_2027_2030": float(mc[:4].sum() / mc.sum()),
           "log_gap_share_glide_years_2031_2032": float(mc[4:6].sum() / mc.sum()),
           "log_gap_share_2033_yield": float(mc[6] / mc.sum())}
cum4 = np.prod(1 + req[:, :4], axis=1) - 1                            # shares, 2027-2030
cum6 = np.prod(1 + req, axis=1) - 1
down4 = cum4 < 0
drivers["shares_down_over_2027_2030"] = {
    "share_of_all_paths": float(down4.mean()), "share_of_failing_paths": float(down4[miss27].mean()),
    "miss_rate_if_down": float(miss27[down4].mean()), "miss_rate_if_up": float(miss27[~down4].mean())}
drivers["shares_cumulative_2027_2032_failing_p5_p50_p95"] = q(cum6[miss27])
drivers["shares_cumulative_2027_2030_failing_p5_p50_p95"] = q(cum4[miss27])
drivers["shares_cumulative_2027_2030_all_p5_p50_p95"] = q(cum4)
crash = req <= -0.20
c_early, c_late = crash[:, :4].any(1), crash[:, 4:].any(1)
drivers["a_year_with_shares_down_20pct_or_more"] = {
    "per_year_chance": float(crash.mean()),
    "all_paths_any_2027_2032": float(crash.any(1).mean()),
    "failing_any_in_2027_2030": float(c_early[miss27].mean()),
    "failing_only_in_2031_2032": float((~c_early & c_late)[miss27].mean()),
    "failing_none": float((~crash.any(1))[miss27].mean()),
    "miss_rate_if_one_in_2027_2030": float(miss27[c_early].mean()),
    "miss_rate_if_none_in_2027_2032": float(miss27[~crash.any(1)].mean())}
worst_y = np.argmin(req, axis=1)
drivers["year_of_worst_share_return"] = {
    "failing": {str(y): float((worst_y[miss27] == i).mean()) for i, y in enumerate(YEARS6)},
    "all_paths": {str(y): float((worst_y == i).mean()) for i, y in enumerate(YEARS6)}}
drivers["worst_share_year_failing_p5_p50_p95"] = q(req.min(1)[miss27])
drivers["worst_share_year_all_p50"] = float(np.median(req.min(1)))
at_central = draws27(150_000.0)["v"] < cen_cost                       # same share paths, the 2033 yield at 5.26%
drivers["2033_yield"] = {
    "failing_with_yield_below_5_26": float((rate33 < R33)[miss27].mean()),
    "miss_rate_at_central_yield_same_share_paths": float(at_central.mean()),
    "failing_that_also_miss_at_central_yield": float(at_central[miss27].mean()),
    "rate33_failing_p5_p50_p95": q(rate33[miss27]),
    "ten_cost_per_point_lower_at_central": float(M.annuity_due(np.array([R33 - 0.01]))[0] - cen_cost)}
A["drivers"] = drivers


def describe(i):
    return {"path": int(i), "share_returns_2027_2032": [float(x) for x in req[i]],
            "bond_returns_2027_2032": [float(x) for x in rbd[i]],
            "pot_by_year_end": [float(x) for x in d27["pot"][i]], "pot_2033": float(v[i]),
            "yield_2033": float(rate33[i]), "ten_cost_2033": float(reserve[i]), "shortfall": float(-d27["surplus"][i]),
            "shares_cumulative_2027_2030": float(cum4[i]), "shares_cumulative_2027_2032": float(cum6[i]),
            "first_unpaid_year_date_order": int(first_unpaid(v[i:i + 1], unit_prices(rate33[i:i + 1]))[0][0]),
            "first_unpaid_payment_part_paid": part_paid(i)}


def part_paid(i):
    """Of the first payment not fully bought (date order), the dollars the money left over buys, in that year's money."""
    pr = unit_prices(rate33[i:i + 1])[0]
    cum = np.cumsum(pr)
    n = int((cum <= v[i] + 1e-9).sum())
    if n == 10:
        return None
    left = v[i] - (cum[n - 1] if n else 0.0)
    return float(left / pr[n] * 50_000)


idx = np.flatnonzero(miss27)
sh = -d27["surplus"][idx]
med_i = int(idx[np.argsort(np.abs(sh - np.median(sh)), kind="stable")[0]])
mild = idx[req[idx].min(1) > -0.20]                                    # failing paths with no share year down 20%+
ex = {"median_failing_path": describe(med_i),
      "failing_paths_with_no_share_year_down_20pct": int(mild.size),
      "failing_paths_with_no_share_year_below_minus_10pct": int((req[idx].min(1) > -0.10).sum())}
if mild.size:
    shm = -d27["surplus"][mild]
    ex["no_crash_median"] = describe(int(mild[np.argsort(np.abs(shm - np.median(shm)), kind="stable")[0]]))
A["examples"] = ex

# ================================================================ Part A2: the same design on US stock history
p_, dv_, keys = [], [], []
for row in csv.DictReader(open(E.ROOT / "keel/models/data/shiller_monthly.csv")):
    if row["Date"] >= "2023-07":
        break
    p_.append(float(row["SP500"]))
    dv_.append(float(row["Dividend"]))
    keys.append(row["Date"][:7])
p_, dv_ = np.array(p_), np.array(dv_)
idxs = np.r_[1.0, np.cumprod((p_[1:] + dv_[:-1] / 12) / p_[:-1])]   # plan.shiller_windows' index
nwin = len(idxs) - 72
starts = keys[:nwin]
yr = np.array([[idxs[i + 12 * (k + 1)] / idxs[i + 12 * k] - 1 for k in range(6)] for i in range(nwin)])
# the same index as the register (plan.shiller_windows: 36- and 60-month factors)
sw = P.shiller_windows()
assert len(sw) == len(idxs) - 60 and abs(sw[0][1] - idxs[36] / idxs[0]) < 1e-12


def hist_run(bond_r, cost33, deposit=150_000.0, fee=0.0):
    vv = np.full(nwin, 300_000.0)
    for k in range(6):
        if k == 1:
            vv += deposit
        vv *= 1 + GLIDE[k] * ((1 + yr[:, k]) * (1 - fee) - 1) + (1 - GLIDE[k]) * bond_r[k]
    return vv - cost33


c = E.Curve(E.load_par())
J = [date(y, 1, 1) for y in range(2027, 2034)]
f1 = [c.fwd(J[k], J[k + 1]) for k in range(6)]                       # 1-year forwards on the 6 Nov curve
TEN33_6NOV = sum(E.PAYMENT * c.P(date(y, 1, 1), base=E.J33) for y in PAY_YEARS)
assert abs(TEN33_6NOV - E.ladder_cost(c) / c.P(E.J33)) < 1e-6


def episodes(mask):
    """Runs of consecutive failing start months, as (first, last, count)."""
    out, run = [], None
    for i, m in enumerate(mask):
        if m and run is None:
            run = [i, i]
        elif m:
            run[1] = i
        elif run is not None:
            out.append(run); run = None
    if run is not None:
        out.append(run)
    return [{"first_start": starts[a], "last_start": starts[b], "windows": b - a + 1} for a, b in out]


H27 = {}
for tag_, bond_r, cost33, fee in (("rates_27sep_central", [gbd_c] * 6, cen_cost, 0.0),
                                  ("rates_6nov_forwards", [math.exp(x) - 1 for x in f1], TEN33_6NOV,
                                   E.ASSUMPTIONS["vt_fee"])):
    o = {"windows": nwin, "first_start": starts[0], "last_start": starts[-1], "ten_cost_2033": cost33}
    for dep_, name in ((150_000.0, "deposit_150k"), (75_000.0, "deposit_75k"), (0.0, "deposit_0k")):
        s = hist_run(bond_r, cost33, dep_, fee)
        m = s < 0
        o[name] = {"windows_short": int(m.sum()), "share_short": float(m.mean()),
                   "shortfall_median_largest": [float(np.median(-s[m])), float((-s[m]).max())] if m.any() else None,
                   "episodes": episodes(m) if dep_ == 150_000.0 else None}
    s = hist_run(bond_r, cost33, 150_000.0, fee)
    o["named_starts"] = {k: {"surplus": float(s[starts.index(k)]),
                             "share_returns": [float(x) for x in yr[starts.index(k)]]}
                         for k in ("1929-01", "1929-09", "1937-01", "1969-01", "1973-01", "2000-01", "2000-08",
                                   "2007-10", "2008-01") if k in starts}
    H27[tag_] = o
A2 = H27

# ================================================================ Part B: the same design on today's engine
NAME = C.design_arg()
DSG = C.design(NAME)
MF = C.margin_fn(NAME)
MU, SD, YV = math.log(1 + E.ASSUMPTIONS["eq_growth"]), E.ASSUMPTIONS["eq_vol"], E.ASSUMPTIONS["yield_vol"]
VFEE = E.ASSUMPTIONS["vt_fee"]
d0, d1, d2, vt3, vt2 = P.draws()
N = P.N
rng = np.random.default_rng(SEED_EXTRA)
x27 = rng.normal(MU, SD, N)                                          # VT 2027 (log)
z3 = rng.standard_normal((N, 3)); z2_ = rng.standard_normal((N, 2))
x3 = np.log(vt3)[:, None] / 3 + SD * (z3 - z3.mean(1, keepdims=True))      # bridge: 2028, 2029, 2030
x2 = np.log(vt2)[:, None] / 2 + SD * (z2_ - z2_.mean(1, keepdims=True))    # bridge: 2031, 2032
zy = rng.standard_normal((N, 3))
s3 = d2[:, None] / 3 + YV * (zy - zy.mean(1, keepdims=True))               # yields: 2028, 2029, 2030 (sum = d2)
e3 = rng.normal(0, YV, (N, 2))                                             # yields: 2031, 2032
assert np.allclose(x3.sum(1), np.log(vt3)) and np.allclose(x2.sum(1), np.log(vt2)) and np.allclose(s3.sum(1), d2)
xs = np.column_stack([x27, x3, x2])                                        # VT log growth, 2027..2032
dy = np.column_stack([d1, s3, e3])                                         # yield change over each year 2027..2032
S = np.column_stack([d0, d0[:, None] + np.cumsum(dy, axis=1)])             # yield level shift on 1 Jan 2027..2033
geqB = np.exp(xs) * (1 - VFEE) - 1
roll = np.exp(np.maximum(np.array(f1)[None, :] + S[:, :6], 0.001)) - 1     # 1-year Treasuries, rolled each January


def fwd_zero(d, yrs=7):
    return -math.log(c.P(date(d.year + yrs, d.month, d.day), base=d)) / yrs


f7 = np.array([fwd_zero(J[k]) for k in range(6)])
ief = np.exp(np.maximum(f7[None, :] + S[:, :6], 0.001)) - 1 - IEF_DUR * dy  # variant: duration 6.95 (no convexity)

GRID = np.round(np.arange(-0.15, 0.1501, 0.0005), 6)


def ten33(s):
    par = {t: max(v_ + 100 * s, 0.0) for t, v_ in c.par.items()}
    cs = E.Curve(par)
    return sum(E.PAYMENT * cs.P(date(y, 1, 1), base=E.J33) for y in PAY_YEARS)


TG = np.array([ten33(s) for s in GRID])
assert abs(TG[np.argmin(np.abs(GRID))] - TEN33_6NOV) < 1e-6
cost33B = np.interp(S[:, 6], GRID, TG)
assert S[:, 6].min() > GRID[0] and S[:, 6].max() < GRID[-1]


def potB(bond, deposit):
    vv = np.full(N, 300_000.0)
    for k in range(6):
        if k == 1:
            vv += deposit
        vv *= 1 + GLIDE[k] * geqB[:, k] + (1 - GLIDE[k]) * bond[:, k]
    return vv


# Caplet's plan on the same paths (the register's house run)
HF = P.run(c, DSG["margin"], None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
RR = C.rule(HF, d0 + d1, d0 + d1 + d2)
assert C.qs(RR["top"]) == [95_000.0, 115_000.0, 140_000.0] and C.qs(RR["bottom"]) == [80_000.0, 95_000.0, 115_000.0]  # bottom's 1-in-20 low $85,000 until Tue 17 Nov evening
assert bool(np.all(HF["payments_full"]))

B = {"basis": "register house model, 6 Nov curve; growth-first glide as 27 Sep; bonds rolled in 1-year Treasuries "
              "(variant: duration 6.95); the ten bought 1 Jan 2033 at that day's curve, payment-date basis",
     "ten_cost_2033_central": TEN33_6NOV, "extra_seed": SEED_EXTRA,
     "bridge_check": {"vt_log_sd_2027": float(np.std(x27)), "vt_log_sd_2029": float(np.std(x3[:, 1])),
                      "vt_log_sd_2032": float(np.std(x2[:, 1])), "expected": SD,
                      "yield_sd_2029": float(np.std(s3[:, 1])), "expected_yield": YV,
                      "yield_shift_2033_sd": float(np.std(S[:, 6]))}}
cen_vB = 300_000 * (1 + GLIDE[0] * (1.075 * (1 - VFEE) - 1) + (1 - GLIDE[0]) * (math.exp(f1[0]) - 1)) + 150_000
for k in range(1, 6):
    cen_vB *= 1 + GLIDE[k] * (1.075 * (1 - VFEE) - 1) + (1 - GLIDE[k]) * (math.exp(f1[k]) - 1)
B["central_path"] = {"pot_2033": cen_vB, "ten_cost_2033": TEN33_6NOV, "surplus": cen_vB - TEN33_6NOV,
                     "pot_over_cost": cen_vB / TEN33_6NOV}
for bname, bond in (("bonds_1y_roll", roll), ("bonds_duration_6_95", ief)):
    o = {}
    for dep_, name in ((150_000.0, "deposit_150k"), (75_000.0, "deposit_75k"), (0.0, "deposit_0k")):
        vv = potB(bond, dep_)
        s = vv - cost33B
        m = s < 0
        o[name] = {"paths_short": int(m.sum()), "share_short": float(m.mean()),
                   "one_in": float(N / m.sum()) if m.any() else None,
                   "shortfall_median_p95_largest": [float(np.median(-s[m])), float(np.percentile(-s[m], 95)),
                                                    float((-s[m]).max())] if m.any() else None,
                   "pot_2033_p5_p50_p95": q(vv)}
        if dep_ == 150_000.0:
            o[name]["failing_with_shares_down_2027_2030"] = float((np.exp(xs[:, :4].sum(1)) < 1)[m].mean())
            o[name]["miss_rate_if_shares_down_2027_2030"] = float(m[np.exp(xs[:, :4].sum(1)) < 1].mean())
            o[name]["failing_with_yields_lower_by_2033"] = float((S[:, 6] < 0)[m].mean())
            o[name]["miss_rate_at_unmoved_2033_curve"] = float((vv < TEN33_6NOV).mean())
            o[name]["caplet_plan_same_failing_paths"] = {
                "all_ten_paid_escrow_standard": bool(np.all(HF["payments_full"][m])),
                "stated_bottom_p5_p50_p95": C.qs(RR["bottom"][m]), "stated_top_p5_p50_p95": C.qs(RR["top"][m]),
                "half_kept_p5_p50_p95": q(HF["kept33"][m])}
    B[bname] = o
# Caplet's plan with a smaller or no 2028 deposit, same paths (plan.run's payments_full: the deposit covers the
# completion to the escrow standard, $39,162 centrally since Tue 17 Nov evening ($38,282 before); NUMBERS 5)
B["caplet_plan_payments_full_by_deposit"] = {}
for dep_ in (150_000.0, 75_000.0, 0.0):
    hd = P.run(c, DSG["margin"], None, dep_, d0, d1, d2, vt3, vt2, MF)
    B["caplet_plan_payments_full_by_deposit"][f"{int(dep_ // 1000)}k"] = float(np.mean(hd["payments_full"]))
# With no 2028 deposit, the plain ladder alone at forward rates (plan.run's own Jan 2027 arithmetic: the ten cost
# c27 x exp(-duration x d0); any part over $300,000 is never bought, the 2033 rung's tail; NUMBERS 5: $3,016 short on
# the 2033 payment centrally)
_s = P.setup(c)
_c27 = _s["c27"] * np.exp(-_s["dur_l"] * d0)
B["caplet_plan_no_deposit_ladder_alone"] = {
    "share_paths_ladder_over_300k_in_jan_2027": float((_c27 > 300_000).mean()),
    "unbought_jan_2027_money_p50_p95_where_over": q((_c27 - 300_000)[_c27 > 300_000], (50, 95)),
    "central_unbought": float(_s["c27"] - 300_000)}

# the figures NUMBERS 8s quotes (a re-run that moves one of them fails here)
assert A["base"]["paths_short"] == 6453 and A["deposit_75k"]["paths_short"] == 27386
assert A["deposit_0k"]["paths_short"] == 81615
assert A["base"]["first_unpaid_year_date_order"] == {"2033": 0, "2034": 0, "2035": 0, "2036": 0, "2037": 1, "2038": 22,
                                                     "2039": 177, "2040": 726, "2041": 1881, "2042": 3646}
assert round(A["base"]["shortfall_failing_paths"]["median"]) == 27695
assert A2["rates_27sep_central"]["deposit_150k"]["windows_short"] == 25
assert B["bonds_1y_roll"]["deposit_150k"]["paths_short"] == 9953
assert B["bonds_duration_6_95"]["deposit_150k"]["paths_short"] == 8147
assert B["caplet_plan_payments_full_by_deposit"] == {"150k": 1.0, "75k": 0.99965, "0k": 1e-05}   # 75k: 0.999725 until Tue 17 Nov evening
assert round(B["caplet_plan_no_deposit_ladder_alone"]["central_unbought"]) == 2_287

# ================================================================ write
out = {"stamp": {"run": RUN, "status": "MODEL", "numbers_section": "8s", "design_today": NAME,
                 "note": "Part A is the 27 Sep 2026 model (strategy_mc.py), imported and unchanged; Parts A2 and B are "
                         "Keel's re-runs of the same growth-first design, not run on 27 Sep."},
       "inputs_27sep": inputs27, "reproduce_27sep": reproduce, "A_27sep_decomposition": A,
       "A2_history_replay": A2, "B_today_engine": B}
json.dump(out, open(OUTFILE, "w"), indent=1, default=float)

if __name__ == "__main__":
    b = A["base"]
    print(f"27 Sep model, growth first: {b['share_short']:.4%} short ({b['paths_short']} of {M.PATHS}; 1 in "
          f"{b['one_in']:.1f}); $75k {A['deposit_75k']['share_short']:.4%}; $0 {A['deposit_0k']['share_short']:.4%}")
    print("shortfall (failing):", {k: round(v_, 4) for k, v_ in b["shortfall_failing_paths"].items()})
    print("first unpaid (date order):", b["first_unpaid_year_date_order"])
    print("drivers:", json.dumps(drivers, indent=1, default=float))
    print("examples:", json.dumps(ex, indent=1, default=float))
    print("history:", json.dumps(A2, indent=1, default=float))
    print("today:", json.dumps(B, indent=1, default=float))
    print("wrote", OUTFILE)
