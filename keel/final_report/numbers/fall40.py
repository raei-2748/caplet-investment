"""A 40% fall in world shares before 2031: what it does to the range, the contribution and her flexibility.
(Keel research worker, card Q6c, Sun 15 Nov 2026, Sydney.) MODEL, not a forecast, not a promise.

Run from the repo root:  python3 -I keel/final_report/numbers/fall40.py
   or from this folder:  python3 -I fall40.py
Writes keel/final_report/numbers/results_fall40_2026-11-15.json and prints the figures (about 15 seconds, numpy only).
Imports engine.py, plan.py and completion.py and changes none of them. It does NOT import joint_stress.py or
kept_half.py, which write their own results files when imported; the few lines it needs from joint_stress.py
(the Additive world and fund_ratio, for what the funds actually pay in a world where rates move) are copied below.

The claim tested (card Q6c, claim 2): "A 40% fall in VT between its purchase in January 2028 and the move before the
2031 meetings lowers only the top of the range and her flexibility; the ten payments and the bottom do not move."

Basis: the Tue 10 Nov register exactly (NUMBERS 0 and 4): curve of Fri 6 Nov 2026; design H_plain with the fee cushion
(completion.CALL); Keel's reading of "most" (plan.run, most=True); the range rule on the late-2032 fund's own holdings
(completion.rule: each end = money put in x what $1 of the holdings pays on 15 Dec 2032 if nothing earns interest from
the trade day, less 0.5%, rounded down to $5,000); the 2033 facility contribution is the lower of what the floor and the
shares moved before the 2031 meetings pay and the stated top; anything above the top joins her flexibility (CANON D12).
The move is modelled on 1 Jan 2031, as everywhere in the register.

"VT down 40%" means VT's value with dividends reinvested, before its 0.06% fee, is 0.6 times its value on the earlier
date (plan.run applies the fee on top: 0.9994^3 over 2028-2031). Scenarios (rates at today's forwards unless named):
  central  VT 7.5% a year throughout (must reproduce NUMBERS 8i's first row to the dollar)
  a        VT down 40% at the move from its Jan 2028 value, then 7.5% a year from the fallen level to Jan 2033
  a_flat   as a, but VT then flat to Jan 2033 (no recovery at all)
  b0       VT flat (0%) from Jan 2028 to the move, then 7.5% a year (the baseline for b)
  b        VT flat to the move, then down 40% by Jan 2033 (hits only her flexibility)
  c        VT down 40% at the move, then back to its 7.5% path by Jan 2033 (vt2 = 1.075^5 / 0.6)
  d        as a, with Treasury yields 2 points below today's forwards from the move on (a recession move); d3: 3 points
  e        VT 40% below where its 7.5% path would be at the move (a 40% fall from a peak reached on that path), then 7.5%
  zero     VT worthless at the move (the deletion test; must reproduce NUMBERS 4: $95,000, $103,178, excess $8,178)
Plus: the line of stated tops against VT's value at the move (and the falls at which each $5,000 step is lost); how
often VT is 40% or more below its January 2028 value at the move in the register's house model (200,000 futures,
seed 2033) and in US stock history since 1871 (rates at forwards), and what the plan states there; and US stock
drawdowns of 40% or more since 1871 from the repo's Shiller monthly mirror (US, not world; monthly averages).
"""
import json
import math
import sys
import time
from datetime import date
from pathlib import Path

import numpy as np

T0 = time.perf_counter()
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

NAME = C.design_arg()
DSG = C.design(NAME)
OWN, POOL, MARGIN = DSG["own"], DSG["pool"], DSG["margin"]
MF = C.margin_fn(NAME)
c = E.Curve(E.load_par())
BASE = E.Reinvest(c)
END = date(2032, 12, 15)
FEE = E.ASSUMPTIONS["fund_fee"]
VFEE = E.ASSUMPTIONS["vt_fee"]
S = P.setup(c)
fF, fM, tauF, tauM = S["fF"], S["fM"], S["tauF"], S["tauM"]
G75 = 1.075
FALL = 0.6                     # "down 40%": 0.6 times the earlier value
IBTM = E.instruments(c)[2033]


# ---------------------------------------------------------------- copied from joint_stress.py (unchanged logic)
class Additive(E.Reinvest):
    """Reinvestment at today's forwards plus delta(d1) points (locked on arrival), floored at zero (joint_stress.py)."""

    def __init__(self, curve, delta):
        super().__init__(curve, "base")
        self.delta = delta

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        tau = (d2 - d1).days / 365.25
        f = self.c.fwd(max(d1, E.J27), d2) + (self.delta(d1) if d1 > E.J27 else 0.0)
        return math.exp(max(f, 0.0) * tau)


def fund_ratio(buy, world, m_buy, s_buy=0.0):
    """Payout on 15 Dec 2032 per $1 put into the late-2032 Treasury fund on `buy`, before the fund fee (joint_stress.py)."""
    fl = [(d, a / (1 - FEE) ** E.yf(d, E.J27), k) for d, a, k in IBTM.flows if d > buy]
    price = sum(a * math.exp(-max(c.fwd(buy, d) * m_buy + s_buy, 0.0) * E.yf(d, buy)) for d, a, _ in fl)
    pay = sum(a * world.grow(d, END) for d, a, _ in fl)
    return pay / price


# ---------------------------------------------------------------- one scenario
def payments(world):
    paid, avail, carry, left = C.ledger(world, OWN, POOL)
    return {"all_ten_paid": bool(all(v >= E.PAYMENT - 0.5 for v in paid.values())),
            "shortfall": float(sum(E.PAYMENT - v for v in paid.values())),
            "left_after_2042_nominal": float(left), "left_after_2042_jan2033_money": float(C.in_2033_money(left, world))}


def scenario(label, vt3, vt2, d2=0.0):
    """plan.run on the central path except VT (vt3: Jan 2028 -> move; vt2: move -> Jan 2033) and, if d2 != 0, yields
    moved by d2 points from the move on. Stated ends by completion.rule; funds pay as joint_stress.world_row prices them
    (realised along the world's rates) and as plan.run models them (the register's 'what the funds pay')."""
    res = P.run(c, margin=MARGIN, d2=d2, vt3=vt3, vt2=vt2, margin_fn=MF)
    rr = C.rule(res, sF=0.0, sM=d2)
    world = BASE if d2 == 0 else Additive(c, lambda d, s=d2: s if d >= E.J31 else 0.0)
    fr = fund_ratio(E.J28, world, 1.0, 0.0) / math.exp(fF * tauF)
    mr = fund_ratio(E.J31, world, 1.0, d2) / math.exp((fM + d2) * tauM)
    model_pay = float(res["floor"] + res["moved"])
    pay = float(res["floor"] * fr + res["moved"] * mr)
    top = float(rr["top"])
    contrib = min(pay, top)
    kept = float(res["kept33"])
    pm = payments(world)
    return {"label": label, "vt3_index": float(vt3), "vt2_index": float(vt2), "yield_move_at_move_points": d2 * 100,
            "vt_value_at_move_over_jan2028_cost_after_fee": float(res["vt31"] / res["vt28"]),
            "completion_jan2028": float(res["complete"]), "floor_money_jan2028": float(res["floor_money"]),
            "vt_bought_jan2028": float(res["vt28"]), "vt_on_move_day": float(res["vt31"]),
            "moved_money": float(res["moved_money"]), "floor_pays": float(res["floor"] * fr),
            "moved_shares_pay": float(res["moved"] * mr),
            "bottom_unrounded": float(rr["bottom_raw"]), "bottom_stated": float(rr["bottom"]),
            "top_unrounded": float(rr["top_raw"]), "top_stated": top,
            "funds_pay": pay, "funds_pay_plan_run_model": model_pay,
            "contribution": contrib, "above_top_to_her_flexibility": pay - contrib,
            "her_flexibility_jan2033": kept, "her_flexibility_plus_above_top": kept + pay - contrib,
            "contribution_plus_flexibility_plus_above_top": contrib + kept + pay - contrib,
            "contribution_inside_stated_range": bool(rr["bottom"] - 0.5 <= contrib <= top + 0.5),
            **{f"payments_{k}": v for k, v in pm.items()}}


SC = {
    "central": scenario("VT 7.5% a year throughout; today's forwards (NUMBERS 8i row 1)", G75 ** 3, G75 ** 2),
    "a": scenario("VT down 40% at the move from its Jan 2028 value, then 7.5% a year", FALL, G75 ** 2),
    "a_flat": scenario("VT down 40% at the move, then flat to Jan 2033", FALL, 1.0),
    "b0": scenario("VT flat to the move, then 7.5% a year (baseline for b)", 1.0, G75 ** 2),
    "b": scenario("VT flat to the move, then down 40% by Jan 2033", 1.0, FALL),
    "c": scenario("VT down 40% at the move, then back to its 7.5% path by Jan 2033", FALL, G75 ** 5 / FALL),
    "d": scenario("As a, with yields 2 points below today's forwards from the move on", FALL, G75 ** 2, -0.02),
    "d3": scenario("As a, with yields 3 points below today's forwards from the move on", FALL, G75 ** 2, -0.03),
    "e": scenario("VT 40% below its 7.5% path at the move (25.5% below cost), then 7.5% a year", FALL * G75 ** 3,
                  G75 ** 2),
    "zero": scenario("VT worthless at the move (deletion test)", 0.0, 1.0),
}
cen = SC["central"]
for k_, v in SC.items():
    if k_ != "central":
        v["change_vs_central"] = {x: v[x] - cen[x] for x in (
            "bottom_stated", "top_stated", "top_unrounded", "funds_pay", "contribution", "her_flexibility_jan2033",
            "her_flexibility_plus_above_top", "contribution_plus_flexibility_plus_above_top")}
SC["b"]["change_vs_b0"] = {x: SC["b"][x] - SC["b0"][x] for x in (
    "bottom_stated", "top_stated", "funds_pay", "contribution", "her_flexibility_jan2033",
    "her_flexibility_plus_above_top")}

# ---------------------------------------------------------------- checks against the register (NUMBERS 4, 8i, 8k)
# Sun 15 Nov evening: the unrounded ends are the register's after the fee is charged from each trade day (NUMBERS 0,
# section 4; were $98,728.56 and $118,443.46)
# Tue 17 Nov evening: re-sized (the payments' 0.5% margin, 365.25-day fix); the Sun 15 Nov register was bottom
# $98,379.86, top $118,072.32, funds pay $123,475.56, excess $8,475.56, half kept $21,347.30, completion $38,282.14,
# left after 2042 $74,122.57 ($45,455.58 in Jan 2033 money), VT $29,828.67, floor $81,889.19, VT at the move $36,989.
REG = {"bottom_stated": 95_000, "bottom_unrounded": 97_605.08, "top_stated": 115_000, "top_unrounded": 117_142.45,
       "funds_pay": 122_503.13, "contribution": 115_000, "above_top_to_her_flexibility": 7_503.13,
       "her_flexibility_jan2033": 21_179.18, "her_flexibility_plus_above_top": 28_682.31,
       "completion_jan2028": 39_161.97, "payments_left_after_2042_nominal": 75_934.02,
       "payments_left_after_2042_jan2033_money": 46_566.45, "vt_bought_jan2028": 29_593.75,
       "floor_money_jan2028": 81_244.28, "vt_on_move_day": 36_698.09}
checks = {k_: {"register": v, "this_run": cen[k_], "diff": cen[k_] - v} for k_, v in REG.items()}
zero_reg = {"top_stated": 95_000, "contribution": 95_000, "funds_pay": 102_365.47, "above_top_to_her_flexibility": 7_365.47}  # Sun 15 Nov: $103,178.04, $8,178.04
checks_zero = {k_: {"register": v, "this_run": SC["zero"][k_], "diff": SC["zero"][k_] - v} for k_, v in zero_reg.items()}
ok = all(abs(v["diff"]) < 1.0 for k_, v in checks.items() if k_ != "vt_on_move_day") and \
    abs(checks["vt_on_move_day"]["diff"]) < 1.0 and all(abs(v["diff"]) < 1.0 for v in checks_zero.values())
for k_ in ("a", "b", "c", "e"):
    ok = ok and abs(SC[k_]["funds_pay"] - SC[k_]["funds_pay_plan_run_model"]) < 1.0

# ---------------------------------------------------------------- the line: stated top against VT at the move
grid = np.round(np.arange(0.0, 2.0001, 0.05), 4)
line = []
for g in grid:
    s = scenario("", float(g), G75 ** 2)
    line.append({"vt3_index": float(g), "top_unrounded": s["top_unrounded"], "top_stated": s["top_stated"],
                 "funds_pay": s["funds_pay"], "contribution": s["contribution"],
                 "her_flexibility_jan2033_if_7_5_after": s["her_flexibility_jan2033"],
                 "her_flexibility_plus_above_top": s["her_flexibility_plus_above_top"]})
# top_unrounded is linear in vt3: solve for the VT level at which each $5,000 step is reached
t0 = scenario("", 0.0, 1.0)["top_unrounded"]
t1 = scenario("", 1.0, 1.0)["top_unrounded"]
slope = t1 - t0
steps = {}
for stp in range(95_000, 150_001, 5_000):
    x = (stp - t0) / slope
    steps[f"{stp}"] = ({"vt3_needed": x, "vt_change_from_jan2028_needed": x - 1.0,
                        "yearly_growth_needed_2028_2031": (x ** (1 / 3) - 1) if x > 0 else None}
                       if x > 0 else {"note": "stated even if VT is worthless at the move (the bottom is $95,000)"})
breakeven = {"top_unrounded_at_vt_zero": t0, "top_added_per_1x_of_vt_at_move": slope,
             "top_added_per_1pct_of_vt_change": slope / 100, "steps": steps}

# ---------------------------------------------------------------- how often: house model and US history
def stated(res, sF, sM, mF=1.0, mM=1.0):
    rr = C.rule(res, sF, sM, mF, mM)
    n = np.size(res["kept33"])
    bc = lambda x: np.broadcast_to(np.asarray(x, float), (n,)).copy()
    return (bc(rr["bottom"]), bc(rr["top"]), bc(rr["payout"]), bc(rr["gift"]), bc(res["kept33"]),
            bc(rr["excess"]))


def cond(mask, B, T, pay, contrib, kept, exc):
    if not mask.any():
        return {"count": 0}
    return {"count": int(mask.sum()), "share": float(mask.mean()),
            "stated_bottom_p5_p50_p95": C.qs(B[mask]), "stated_top_p5_p50_p95": C.qs(T[mask]),
            "stated_top_min": float(T[mask].min()),
            "contribution_p5_p50_p95": C.qs(contrib[mask]),
            "funds_pay_p5_p50_p95": P.pct(pay[mask]),
            "her_flexibility_p5_p50_p95": P.pct(kept[mask]),
            "her_flexibility_plus_above_top_p5_p50_p95": P.pct(kept[mask] + exc[mask]),
            "contribution_inside_range": float(((contrib[mask] >= B[mask] - 0.5) & (contrib[mask] <= T[mask] + 0.5)).mean())}


d0, d1, d2, h3, h2 = P.draws()
H = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, h3, h2, MF)
HB, HT, Hpay, Hc, Hk, Hx = stated(H, d0 + d1, d0 + d1 + d2)
house = {
    "futures": int(h3.size),
    "check_unconditional": {"stated_bottom_p5_p50_p95": C.qs(HB), "stated_top_p5_p50_p95": C.qs(HT),
                            "her_flexibility_p1_p5_p50_p95": [float(np.percentile(Hk, p)) for p in (1, 5, 50, 95)]},
    "vt_40pct_or_more_below_cost_at_move": cond(h3 <= FALL, HB, HT, Hpay, Hc, Hk, Hx),
    "vt_30pct_or_more_below_cost_at_move": cond(h3 <= 0.7, HB, HT, Hpay, Hc, Hk, Hx),
    "vt_20pct_or_more_below_cost_at_move": cond(h3 <= 0.8, HB, HT, Hpay, Hc, Hk, Hx),
    "vt_below_cost_at_move": cond(h3 < 1.0, HB, HT, Hpay, Hc, Hk, Hx),
    "vt_falls_40pct_or_more_move_to_2033": cond(h2 <= FALL, HB, HT, Hpay, Hc, Hk, Hx),
    "vt_40pct_or_more_below_cost_on_1jan2033": cond(h3 * h2 <= FALL, HB, HT, Hpay, Hc, Hk, Hx),
    "all": cond(np.ones(h3.size, bool), HB, HT, Hpay, Hc, Hk, Hx),
    "note": "plan.draws, seed 2033: VT lognormal, 7.5% median a year, 17.88% s.d.; yields independent of shares",
}
# lognormal arithmetic for the same events (no simulation error)
mu, sd = math.log(1 + E.ASSUMPTIONS["eq_growth"]), E.ASSUMPTIONS["eq_vol"]
ncdf = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
house["lognormal_exact"] = {"p_vt3_le_0.6": ncdf((math.log(0.6) - 3 * mu) / (sd * math.sqrt(3))),
                            "p_vt2_le_0.6": ncdf((math.log(0.6) - 2 * mu) / (sd * math.sqrt(2))),
                            "p_vt5_le_0.6": ncdf((math.log(0.6) - 5 * mu) / (sd * math.sqrt(5))),
                            "p_vt3_le_1.0253": ncdf((math.log(steps["115000"]["vt3_needed"]) - 3 * mu) / (sd * math.sqrt(3)))}

w = P.shiller_windows()
starts = [k_ for k_, _, _ in w]
y3 = np.array([a for _, a, _ in w])
y2 = np.array([b for _, _, b in w])
Hh = P.run(c, MARGIN, None, 150_000.0, vt3=y3, vt2=y2, margin_fn=MF)
YB, YT, Ypay, Yc, Yk, Yx = stated(Hh, 0.0, 0.0)
m40 = y3 <= FALL
hist = {
    "windows": len(w), "first": starts[0], "last": starts[-1],
    "check_unconditional": {"stated_top_p5_p50_p95": C.qs(YT), "stated_top_min": float(YT.min()),
                            "her_flexibility_p5_p50_p95": P.pct(Yk)},
    "vt_40pct_or_more_below_cost_at_move": dict(cond(m40, YB, YT, Ypay, Yc, Yk, Yx),
                                                starts=[s for s, b in zip(starts, m40) if b]),
    "vt_30pct_or_more_below_cost_at_move": dict(cond(y3 <= 0.7, YB, YT, Ypay, Yc, Yk, Yx),
                                                starts=[s for s, b in zip(starts, y3 <= 0.7) if b]),
    "vt_20pct_or_more_below_cost_at_move": cond(y3 <= 0.8, YB, YT, Ypay, Yc, Yk, Yx),
    "vt_below_cost_at_move": cond(y3 < 1.0, YB, YT, Yc * 0 + Ypay, Yc, Yk, Yx),
    "vt_falls_40pct_or_more_move_to_2033": dict(cond(y2 <= FALL, YB, YT, Ypay, Yc, Yk, Yx),
                                                starts=[s for s, b in zip(starts, y2 <= FALL) if b]),
    "vt_40pct_or_more_below_cost_on_1jan2033": dict(cond(y3 * y2 <= FALL, YB, YT, Ypay, Yc, Yk, Yx),
                                                    starts=[s for s, b in zip(starts, y3 * y2 <= FALL) if b]),
    "lowest_vt3": {"value": float(y3.min()), "start": starts[int(np.argmin(y3))],
                   "stated_top": float(YT[int(np.argmin(y3))])},
    "note": "US stocks with dividends (Shiller monthly mirror), every 3-year window and the 2 years after, rates at "
            "today's forwards; US, not world; monthly averages smooth the lows",
}

NAMED = ["1929-09", "1937-03", "1973-01", "2000-03", "2000-08", "2007-10", "2008-01"]
hist["named_vt_purchase_months"] = {
    s: {"vt3_index": float(y3[i]), "vt2_index": float(y2[i]), "stated_top": float(YT[i]),
        "top_unrounded": float(C.rule(Hh)["top_raw"][i]), "contribution": float(Yc[i]),
        "her_flexibility_jan2033": float(Yk[i]), "her_flexibility_plus_above_top": float(Yk[i] + Yx[i])}
    for s in NAMED for i in [starts.index(s)]}

# ---------------------------------------------------------------- the house model's own tail, month by month
# The register's house model draws only VT's value at the move and in 2033. How often would a 40% fall from a peak
# happen INSIDE the three years on the same assumptions (lognormal, 7.5% median a year, 17.88% s.d., independent
# months)? Keel arithmetic, its own seed; it does not touch the register's draws.
rng = np.random.default_rng(4040)
mu_m, sd_m = mu / 12, sd / math.sqrt(12)
paths = np.exp(np.cumsum(rng.normal(mu_m, sd_m, (100_000, 60)), axis=1))
paths = np.c_[np.ones(100_000), paths]
def _mdd(seg):
    return (seg / np.maximum.accumulate(seg, axis=1) - 1).min(axis=1)
house["monthly_lognormal_same_assumptions"] = {
    "paths": 100_000, "seed": 4040,
    "share_40pct_fall_from_a_peak_inside_36_months": float((_mdd(paths[:, :37]) <= -0.4).mean()),
    "share_40pct_fall_from_a_peak_inside_60_months": float((_mdd(paths) <= -0.4).mean()),
    "share_ending_40pct_below_start_36_months": float((paths[:, 36] <= 0.6).mean()),
    "share_20pct_fall_from_a_peak_inside_36_months": float((_mdd(paths[:, :37]) <= -0.2).mean()),
}

# ---------------------------------------------------------------- developed-world shares, calendar years 1970-2025
# MSCI World (USD, gross total return) calendar-year returns. 2012-2025 read at msci.com (MSCI World Index (USD)
# factsheet, gross returns, 30 Oct 2026). 1970-2011 from the table in Wikipedia's "MSCI World" article (marked
# "citation needed"), read 15 Nov 2026: UNVERIFIED at the source; its 2012-2025 rows equal the factsheet's exactly.
# Annual points hide falls inside a year (2007-09's 54% monthly fall shows here only as 2008's -40.3%).
MSCI_WORLD_GROSS = {
    1970: -1.98, 1971: 19.56, 1972: 23.55, 1973: -14.51, 1974: -24.48, 1975: 34.50, 1976: 14.71, 1977: 5.00,
    1978: 18.22, 1979: 12.67, 1980: 27.72, 1981: -3.30, 1982: 11.27, 1983: 23.28, 1984: 5.77, 1985: 41.77,
    1986: 42.80, 1987: 16.76, 1988: 23.95, 1989: 17.19, 1990: -16.52, 1991: 18.97, 1992: -4.66, 1993: 23.13,
    1994: 5.58, 1995: 21.32, 1996: 14.00, 1997: 16.23, 1998: 24.80, 1999: 25.34, 2000: -12.92, 2001: -16.52,
    2002: -19.54, 2003: 33.76, 2004: 15.25, 2005: 10.02, 2006: 20.65, 2007: 9.57, 2008: -40.33, 2009: 30.79,
    2010: 12.34, 2011: -5.02, 2012: 16.54, 2013: 27.37, 2014: 5.50, 2015: -0.32, 2016: 8.15, 2017: 23.07,
    2018: -8.20, 2019: 28.40, 2020: 16.50, 2021: 22.35, 2022: -17.73, 2023: 24.42, 2024: 19.19, 2025: 21.60}
_yrs = sorted(MSCI_WORLD_GROSS)
_g = np.array([1 + MSCI_WORLD_GROSS[y] / 100 for y in _yrs])


def _roll(n):
    r = np.array([np.prod(_g[i:i + n]) - 1 for i in range(len(_g) - n + 1)])
    first = [_yrs[i] for i in range(len(r))]
    return {"windows": int(r.size), "first_start": first[0], "last_start": first[-1],
            "total_return_min_p5_p10_p25_p50": [float(r.min())] + [float(np.percentile(r, p)) for p in (5, 10, 25, 50)],
            "worst_start": first[int(np.argmin(r))],
            "share_40pct_or_more_down": float((r <= -0.4).mean()),
            "starts_40pct_or_more_down": [first[i] for i in range(r.size) if r[i] <= -0.4],
            "share_20pct_or_more_down": float((r <= -0.2).mean()),
            "share_below_zero": float((r < 0).mean()),
            "starts_below_zero": [first[i] for i in range(r.size) if r[i] < 0],
            "compound_growth_whole_period": float(np.prod(_g) ** (1 / len(_g)) - 1)}


world = {"series": "MSCI World (USD, gross), calendar years 1970-2025; see source note in the script",
         "windows_3y": _roll(3), "windows_5y": _roll(5),
         "check_2012_2025_equal_factsheet": True}

# ---------------------------------------------------------------- US stock drawdowns of 40% or more since 1871
def shiller_tr():
    import csv
    p, dv, keys = [], [], []
    for r in csv.DictReader(open(E.ROOT / "keel/models/data/shiller_monthly.csv")):
        if r["Date"] >= "2023-07":
            break
        p.append(float(r["SP500"]))
        dv.append(float(r["Dividend"]))
        keys.append(r["Date"][:7])
    p, dv = np.array(p), np.array(dv)
    tr = (p[1:] + dv[:-1] / 12) / p[:-1]
    return keys, np.r_[1.0, np.cumprod(tr)]


keys, idx = shiller_tr()


def episodes(ix, depth):
    """Peak-to-trough falls of at least `depth` in the monthly index; recovery = first month back at the old peak."""
    out, i, n = [], 0, len(ix)
    peak_i = 0
    while i < n:
        if ix[i] >= ix[peak_i]:
            peak_i = i
        dd = ix[i] / ix[peak_i] - 1
        if dd <= -depth:
            # find trough before recovery
            j = i
            trough_i = i
            while j < n and ix[j] < ix[peak_i]:
                if ix[j] < ix[trough_i]:
                    trough_i = j
                j += 1
            rec = j if j < n else None
            out.append({"peak": keys[peak_i], "trough": keys[trough_i],
                        "fall": float(ix[trough_i] / ix[peak_i] - 1),
                        "months_peak_to_trough": trough_i - peak_i,
                        "recovered": keys[rec] if rec is not None else None,
                        "months_trough_to_recovery": (rec - trough_i) if rec is not None else None,
                        "months_peak_to_recovery": (rec - peak_i) if rec is not None else None})
            if rec is None:
                break
            i = rec
            peak_i = rec
            continue
        i += 1
    return out


def windows_stats(ix, months):
    r = ix[months:] / ix[:-months]
    # largest peak-to-trough fall inside each window
    mdd = []
    for s in range(len(ix) - months):
        seg = ix[s:s + months + 1]
        run = np.maximum.accumulate(seg)
        mdd.append(float((seg / run - 1).min()))
    mdd = np.array(mdd)
    return {"windows": int(r.size),
            "total_return_p1_p5_p10_p25_p50_p75_p95": [float(np.percentile(r - 1, p)) for p in (1, 5, 10, 25, 50, 75, 95)],
            "share_ending_40pct_or_more_down": float((r <= 0.6).mean()),
            "share_ending_20pct_or_more_down": float((r <= 0.8).mean()),
            "share_ending_below_start": float((r < 1.0).mean()),
            "share_with_a_40pct_fall_inside": float((mdd <= -0.4).mean()),
            "share_with_a_20pct_fall_inside": float((mdd <= -0.2).mean()),
            "starts_ending_40pct_or_more_down_first_last": (lambda ss: [ss[0], ss[-1], len(ss)] if ss else [])(
                [keys[s] for s in range(r.size) if r[s] <= 0.6])}


us = {"series": "US stocks with dividends, nominal USD, Shiller monthly mirror (monthly average prices), Jan 1871 to "
                "Jun 2023 (the window plan.py reads)",
      "episodes_40pct_or_more": episodes(idx, 0.40),
      "episodes_30pct_or_more": episodes(idx, 0.30),
      "windows_3y": windows_stats(idx, 36), "windows_5y": windows_stats(idx, 60)}
years_span = (len(idx) - 1) / 12
us["episodes_40pct_per_century"] = len(us["episodes_40pct_or_more"]) / years_span * 100
us["years_span"] = years_span

out = {"stamp": {"run": "Sun 15 Nov 2026 (Sydney); re-run Sun 15 Nov evening", "rule": C.RULE_VERSION, "curve": E.CURVE_DAY, "design": NAME, "card": "Q6c",
                 "margin_jan2027_value": MARGIN, "basis": "Tue 10 Nov register (NUMBERS 0, 4, 8i)",
                 "fall": "VT index with dividends, before its 0.06% fee, at 0.6x the earlier value"},
       "checks_central_vs_8i_row1": checks, "checks_zero_vs_numbers4": checks_zero, "all_checks_pass": bool(ok),
       "scenarios": SC, "line_stated_top_vs_vt_at_move": line, "breakeven": breakeven,
       "house": house, "history_us_rates_at_forwards": hist, "us_drawdowns_since_1871": us,
       "developed_world_msci_calendar_years": world,
       "seconds": round(time.perf_counter() - T0, 1)}
json.dump(out, open(HERE / f"results_fall40_{C.RESULTS}.json", "w"), indent=1, default=float)

# ---------------------------------------------------------------- print
k = lambda x: f"${x:,.0f}"
print("checks pass:", ok)
for kk, v in checks.items():
    print(f"  {kk:40s} register {v['register']:>12,.2f}  run {v['this_run']:>12,.2f}  diff {v['diff']:+.2f}")
for kk, v in checks_zero.items():
    print(f"  zero {kk:35s} register {v['register']:>12,.2f}  run {v['this_run']:>12,.2f}  diff {v['diff']:+.2f}")
for kk, s in SC.items():
    print(f"{kk:7s} bottom {k(s['bottom_stated'])} ({k(s['bottom_unrounded'])}) top {k(s['top_stated'])} "
          f"({k(s['top_unrounded'])}) pay {k(s['funds_pay'])} [model {k(s['funds_pay_plan_run_model'])}] "
          f"contrib {k(s['contribution'])} above {k(s['above_top_to_her_flexibility'])} "
          f"flex {k(s['her_flexibility_jan2033'])} flex+ {k(s['her_flexibility_plus_above_top'])} "
          f"total {k(s['contribution_plus_flexibility_plus_above_top'])} ten paid {s['payments_all_ten_paid']} "
          f"left {k(s['payments_left_after_2042_nominal'])}/{k(s['payments_left_after_2042_jan2033_money'])} "
          f"VT31 {k(s['vt_on_move_day'])}")
print("steps:", {a: round(b.get("vt_change_from_jan2028_needed", -1.0), 4) for a, b in steps.items()})
print("house:", json.dumps({a: b for a, b in house.items() if a != "note"}, default=float)[:3000])
print("hist:", json.dumps({a: b for a, b in hist.items() if a != "note"}, default=float)[:3000])
print("US 40% episodes:", json.dumps(us["episodes_40pct_or_more"], indent=0))
print("US 30% episodes:", len(us["episodes_30pct_or_more"]), [e["peak"] + ">" + e["trough"] for e in us["episodes_30pct_or_more"]])
print("US 3y:", us["windows_3y"])
print("US 5y:", us["windows_5y"])
print("named:", json.dumps(hist["named_vt_purchase_months"], indent=0))
print("monthly lognormal:", house["monthly_lognormal_same_assumptions"])
print("world 3y:", world["windows_3y"])
print("world 5y:", world["windows_5y"])
print("seconds", out["seconds"])
