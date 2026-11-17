"""The share forecast from its building blocks (numbers owner's worker, Wed 18 Nov 2026 morning, Sydney). MODEL, not a
forecast or a promise. NUMBERS 8v; card Q124.

Card Q124 rebuilt world shares' expected return from today's yield, inflation, growth, buybacks and valuation (a sum
near 5% a year, range 3.1% to 6.4%) against the register's 7.5% (J.P. Morgan 2027, above the middle of published
forecasts, median about 6.5%). It read three things off NUMBERS 8p without a run: at 5% the stated top stays $115,000
and her flexibility is about $18,828 against $21,179; only its gloomiest sum (3.1%) sits under 8p's 3.4% a year; and
the step is lost mainly if valuations fall in the three years to the 2031 move (row 24: the P/E at which it goes).

This script runs the register's own engine (no new model) at expected world-share returns of 3.1%, 5.0%, 6.5% and 7.5%
a year, and one valuation case, and asserts every register figure it touches:
  central   plan.run on today's forwards with VT at (1 + r) cubed to the move and squared after (fall40.scenario's
            convention, 8p's house panel); completion.rule for the stated ends; what the funds pay as section 4 counts it.
  house     the register's 200,000 house paths (plan.draws, seed 2033) with VT's median moved to r and its 17.88% spread
            kept: the same random numbers, only the median moves (at 7.5% the draws equal plan.draws exactly).
  shares    "shares alone": rates at today's forwards, VT lognormal at r and 17.88%; the chance VT is under the level the
            $115,000 step needs at the move (8p's 35.4% at 7.5%), exact arithmetic.
  valuation the card's valuation input: J.P. Morgan's valuation block, -0.65% a year, takes ACWI's P/E from 20.82 to about
            19.5 over ten years (card Q124 row 18). The case keeps a 5.0% ten-year return but lands that whole fall in the
            three years from January 2028 to the move: the other blocks earn 1.05 / 0.9935 - 1 = 5.69% a year throughout,
            and VT's value at the move is also multiplied by 0.9935 ** 10 (P/E 20.82 to 19.505). The P/E in January 2028
            is taken as today's 20.82, as the card takes it. Also run on 7.5% the same way, and at P/E 19.5 exactly.
  row 24    the P/E at the move at which the step goes, for each of the card's four no-valuation sums (3.70, 4.70, 5.90,
            6.37% a year), on the engine's exact threshold with the blocks compounded yearly.

Nothing is re-sized: the register's design (H_plain with the fee cushion and the payments' 0.5% margin), the range rule on
the fund's holdings, Keel's reading of "most", the 6 Nov 2026 curve. VT does not enter the completion, the floor or the
ten payments' ledger; the script asserts that the completion, the floor money and the stated bottom are identical, path by
path, at every return.

Run from the repo root:  python3 -I keel/final_report/numbers/forecast_blocks.py
Writes keel/final_report/numbers/results_forecast_blocks_2026-11-18.json (about 10 seconds, numpy only). Imports
engine.py, plan.py and completion.py and changes none of them; reads no results file; writes no other file. It does not
import fall40.py, which re-runs and rewrites its own results file when imported.
"""
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

T0 = time.perf_counter()
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

c = C.c
NAME = C.CALL
MARGIN = C.design(NAME)["margin"]
MF = C.margin_fn(NAME)
SD = E.ASSUMPTIONS["eq_vol"]
STEP_TOP = 115_000.0
OUT = HERE / "results_forecast_blocks_2026-11-18.json"
f = lambda x: float(np.asarray(x).item())

# The four returns (card Q124; NUMBERS 0 and 8p): the card's gloomiest sum (3.06%, said 3.1%), its middle and Syzygy's
# 5.0%, the fifteen-house median (card Q6b), J.P. Morgan's 7.5% (the register's)
RATES = {"3.1": 0.031, "5.0": 0.050, "6.5": 0.065, "7.5": 0.075}
PE0, VAL_BLOCK, YEARS_VAL = 20.82, -0.0065, 10           # card Q124 rows 18, 26: MSCI ACWI trailing P/E 30 Oct 2026
VAL10 = (1 + VAL_BLOCK) ** YEARS_VAL                       # 0.936863: P/E 20.82 to 19.505 over ten years
NO_VAL_SUMS = {"-2.0": 0.0370, "-1.0": 0.0470, "+0.2": 0.0590, "+0.67": 0.0637}   # card Q124 row 13, by buyback anchor
CARD_ROW24 = {"-2.0": 20.6, "-1.0": 20.0, "+0.2": 19.3, "+0.67": 19.0}


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


# ================================================================ central path
def central(vt3, vt2):
    res = P.run(c, margin=MARGIN, vt3=vt3, vt2=vt2, margin_fn=MF)
    rr = C.rule(res)
    pay, top = f(rr["payout"]), f(rr["top"])
    contrib = min(pay, top)
    kept = f(res["kept33"])
    return {"vt3_index_before_fee": float(vt3), "vt2_index_before_fee": float(vt2),
            "completion_jan2028": f(res["complete"]), "floor_money_jan2028": f(res["floor_money"]),
            "vt_bought_jan2028": f(res["vt28"]), "vt_on_move_day": f(res["vt31"]),
            "bottom_unrounded": f(rr["bottom_raw"]), "bottom_stated": f(rr["bottom"]),
            "top_unrounded": f(rr["top_raw"]), "top_stated": top,
            "top_clear_of_115000_step": f(rr["top_raw"]) - STEP_TOP,
            "funds_pay": pay, "contribution": contrib, "above_top": pay - contrib,
            "her_flexibility_shares_kept_jan2033": kept, "her_flexibility_plus_above_top": kept + pay - contrib,
            "contribution_plus_flexibility_plus_above_top": pay + kept}


cen = {k: central((1 + r) ** 3, (1 + r) ** 2) for k, r in RATES.items()}

# register checks (NUMBERS header and section 4; 8p's house panel, re-sized Tue 17 Nov evening)
j = cen["7.5"]
near(j["bottom_unrounded"], 97_605.08, 0.01, "bottom 7.5")
near(j["top_unrounded"], 117_142.45, 0.01, "top 7.5")
near(j["funds_pay"], 122_503.13, 0.01, "funds pay 7.5")
near(j["above_top"], 7_503.13, 0.01, "excess 7.5")
near(j["her_flexibility_shares_kept_jan2033"], 21_179.18, 0.01, "half kept 7.5")
near(j["her_flexibility_plus_above_top"], 28_682.31, 0.01, "flex plus 7.5")
near(j["completion_jan2028"], 39_161.97, 0.01, "completion")
near(j["floor_money_jan2028"], 81_244.28, 0.01, "floor money")
near(j["vt_bought_jan2028"], 29_593.75, 0.01, "VT bought")
near(j["vt_on_move_day"], 36_698.09, 0.01, "VT on the move day")
assert (j["bottom_stated"], j["top_stated"], j["contribution"]) == (95_000, 115_000, 115_000)
near(cen["5.0"]["top_unrounded"], 115_811, 1, "8p Syzygy top")
near(cen["5.0"]["her_flexibility_shares_kept_jan2033"], 18_828, 1, "8p Syzygy flexibility")
near(cen["6.5"]["top_unrounded"], 116_602, 1, "8p median top")
near(cen["6.5"]["her_flexibility_shares_kept_jan2033"], 20_212, 1, "8p median flexibility")
for k in RATES:   # VT never touches the completion, the floor or the bottom
    for x in ("completion_jan2028", "floor_money_jan2028", "bottom_unrounded", "bottom_stated"):
        assert cen[k][x] == j[x], (k, x)
assert cen["3.1"]["top_stated"] == 110_000 and all(cen[k]["top_stated"] == 115_000 for k in ("5.0", "6.5", "7.5"))

# the threshold: the top before rounding is linear in VT at the move (fall40's breakeven, re-derived)
t0 = f(C.rule(P.run(c, margin=MARGIN, vt3=0.0, vt2=1.0, margin_fn=MF))["top_raw"])
t1 = f(C.rule(P.run(c, margin=MARGIN, vt3=1.0, vt2=1.0, margin_fn=MF))["top_raw"])
X115 = (STEP_TOP - t0) / (t1 - t0)
R115 = X115 ** (1 / 3) - 1
near(X115 - 1, 0.106, 0.0005, "8p +10.6%")
near(R115, 0.034, 0.0005, "8p 3.4% a year")
threshold = {"top_unrounded_at_vt_zero": t0, "top_added_per_1x_vt_at_move": t1 - t0,
             "vt3_needed_for_115000": X115, "vt_change_needed": X115 - 1, "yearly_growth_needed_2028_2031": R115,
             "card_q124_row23_yield_plus_inflation_three_years": 1.0381 ** 3 - 1}
near(threshold["card_q124_row23_yield_plus_inflation_three_years"], 0.119, 0.0005, "card row 23's 11.9%")

# ================================================================ the valuation case
def val_case(r10, factor):
    """r10: the ten-year return, which contains J.P. Morgan's -0.65% a year valuation block; factor: the P/E change landed
    between January 2028 and the move instead of over ten years."""
    nv = (1 + r10) / (1 + VAL_BLOCK)                       # the other blocks, a year
    out = central(nv ** 3 * factor, nv ** 2)
    out.update({"ten_year_return": r10, "other_blocks_a_year": nv - 1, "pe_factor_by_the_move": factor,
                "pe_at_the_move": PE0 * factor, "vt_change_to_move_before_fee": nv ** 3 * factor - 1})
    return out, nv


val = {}
val["5.0_pe_19.505"], nv5 = val_case(0.05, VAL10)
val["5.0_pe_19.5_exact"], _ = val_case(0.05, 19.5 / PE0)
val["7.5_pe_19.505"], nv75 = val_case(0.075, VAL10)
v5 = val["5.0_pe_19.505"]
assert v5["top_stated"] == 110_000 and -10 < v5["top_clear_of_115000_step"] < 0, v5["top_clear_of_115000_step"]
assert val["5.0_pe_19.5_exact"]["top_stated"] == 110_000
assert val["7.5_pe_19.505"]["top_stated"] == 115_000
assert v5["bottom_stated"] == 95_000 and v5["bottom_unrounded"] == j["bottom_unrounded"]
near(PE0 * VAL10, 19.5, 0.01, "card row 18's P/E about 19.5")

# row 24: the P/E at the move at which the step goes, each no-valuation sum compounded yearly to the move
row24 = {}
for a, s in NO_VAL_SUMS.items():
    pe_star = PE0 * X115 / (1 + s) ** 3
    pe_card_way = PE0 * math.exp(math.log(X115) - 3 * s)    # the card's way: the sum read as a continuous rate
    at195 = central((1 + s) ** 3 * 19.5 / PE0, (1 + s) ** 2)
    row24[a] = {"no_valuation_sum": s, "pe_at_move_that_loses_the_step": pe_star, "fall_against_earnings": 1 - pe_star / PE0,
                "pe_if_sum_read_as_continuous_rate": pe_card_way, "card_row24": CARD_ROW24[a],
                "pe_19_5_by_the_move_top_stated": at195["top_stated"], "pe_19_5_by_the_move_top_unrounded": at195["top_unrounded"],
                "no_valuation_change_top_stated": central((1 + s) ** 3, (1 + s) ** 2)["top_stated"]}
    near(pe_card_way, CARD_ROW24[a], 0.05, f"card row 24 reproduced the card's way, {a}")
    assert row24[a]["no_valuation_change_top_stated"] == 115_000, a   # card: 3.7% to 6.4% state $115,000
lowest_no_val = central(1.037 ** 3, 1.037 ** 2)
assert 0 < lowest_no_val["top_clear_of_115000_step"] < 200      # 3.70%: clears by $143
gloomiest = central(1.0306 ** 3, 1.0306 ** 2)                   # the card's exact 3.06%
assert gloomiest["top_stated"] == 110_000

# ================================================================ house paths
def draws_at(r, shift3=0.0):
    """plan.draws with VT's median growth at r (and log shift3 added to the move's draw): the same seed and order, so
    the same random numbers; only the median moves."""
    rng = np.random.default_rng(P.SEED)
    sv = E.ASSUMPTIONS["yield_vol"]
    t0_ = E.yf(E.J27)
    d0 = rng.normal(0, sv * math.sqrt(t0_), P.N)
    d1 = rng.normal(0, sv, P.N)
    d2 = rng.normal(0, sv * math.sqrt(3), P.N)
    mu = math.log(1 + r)
    vt3 = np.exp(rng.normal(mu * 3 + shift3, SD * math.sqrt(3), P.N))
    vt2 = np.exp(rng.normal(mu * 2, SD * math.sqrt(2), P.N))
    return d0, d1, d2, vt3, vt2


ref = P.draws()
for a_, b_ in zip(draws_at(0.075), ref):
    assert np.array_equal(a_, b_)          # at 7.5% these are the register's draws, number for number


def house(r, shift3=0.0):
    d0, d1, d2, h3, h2 = draws_at(r, shift3)
    res = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, h3, h2, MF)
    rr = C.rule(res, d0 + d1, d0 + d1 + d2)
    pay, top = np.asarray(rr["payout"]), np.asarray(rr["top"])
    contrib = np.minimum(pay, top)
    kept = np.asarray(res["kept33"])
    return res, rr, {"top_under_115000": float((top < STEP_TOP).mean()), "top_under_110000": float((top < 110_000).mean()),
                     "top_115000_or_more": float((top >= STEP_TOP).mean()),
                     "stated_top_p5_p50_p95": C.qs(top), "stated_bottom_p5_p50_p95": C.qs(rr["bottom"]),
                     "her_flexibility_shares_kept_p5_p50_p95": P.pct(kept),
                     "her_flexibility_plus_above_top_p5_p50_p95": P.pct(kept + pay - contrib)}


H, HR, hs = {}, {}, {}
for k, r in RATES.items():
    H[k], HR[k], hs[k] = house(r)
mu75 = math.log(1.075)
H["val_5.0"], HR["val_5.0"], hs["val_5.0"] = house(nv5 - 1, math.log(VAL10))
H["val_7.5"], HR["val_7.5"], hs["val_7.5"] = house(nv75 - 1, math.log(VAL10))

# register checks: section 4's "What Laura could announce", 57.2% at $115,000 or more; 1-in-20 / median / high
near(hs["7.5"]["top_115000_or_more"], 0.572, 0.0005, "section 4: 57.2%")
assert hs["7.5"]["stated_top_p5_p50_p95"] == [95_000, 115_000, 140_000]
assert hs["7.5"]["stated_bottom_p5_p50_p95"] == [80_000, 95_000, 115_000]
near(hs["7.5"]["her_flexibility_shares_kept_p5_p50_p95"][1], 20_486, 1, "8f median half kept")
for k in H:   # the bottom, the completion and the floor do not move with the share forecast, path by path
    assert np.array_equal(HR[k]["bottom"], HR["7.5"]["bottom"]), k
    assert np.array_equal(H[k]["complete"], H["7.5"]["complete"]), k
    assert np.array_equal(H[k]["floor_money"], H["7.5"]["floor_money"]), k
# path by path against J.P. Morgan's 7.5% (same futures): how often the lower forecast states a lower top
for k in H:
    hs[k]["top_lower_than_at_7_5_same_path"] = float((HR[k]["top"] < HR["7.5"]["top"]).mean())


# shares alone: rates at forwards, VT lognormal; the chance VT is under X115 at the move (8p's 35.4% at 7.5%)
def ncdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def shares_alone(r, shift3=0.0):
    return ncdf((math.log(X115) - 3 * math.log(1 + r) - shift3) / (SD * math.sqrt(3)))


sa = {k: shares_alone(r) for k, r in RATES.items()}
sa["val_5.0"] = shares_alone(nv5 - 1, math.log(VAL10))
sa["val_7.5"] = shares_alone(nv75 - 1, math.log(VAL10))
near(sa["7.5"], 0.354, 0.0005, "8p: 35.4%")
for k in sa:
    hs[k]["shares_alone_top_under_115000_rates_at_forwards"] = sa[k]

# ================================================================ write
out = {"run": "Wed 18 Nov 2026 morning (Sydney), numbers owner's worker", "card": "Q124", "section": "NUMBERS 8v",
       "rule": C.RULE_VERSION, "design": NAME, "curve": E.CURVE_DAY, "register_results": C.RESULTS,
       "basis": "register as re-sized Tue 17 Nov evening; central path at today's forwards; house model 200,000 paths, "
                "seed 2033, VT median moved, 17.88% spread kept",
       "rates": RATES, "central": cen, "threshold": threshold,
       "valuation_case": {"note": "J.P. Morgan's -0.65% a year valuation block over ten years (P/E 20.82 to 19.505) "
                                  "landed between January 2028 and the move; ten-year return unchanged",
                          **val},
       "card_row24": row24, "card_gloomiest_3.06": gloomiest, "card_lowest_no_valuation_3.70": lowest_no_val,
       "house": hs, "all_asserts_pass": True, "seconds": round(time.perf_counter() - T0, 1)}
json.dump(out, open(OUT, "w"), indent=1, default=float)

# ================================================================ print
k_ = lambda x: f"${x:,.0f}"
print("threshold: VT +{:.2%} at the move, {:.3%} a year".format(X115 - 1, R115))
rows = [(f"{k}%", cen[k], hs[k]) for k in RATES] + [("5.0% + P/E fall by the move", v5, hs["val_5.0"]),
                                                    ("7.5% + P/E fall by the move", val["7.5_pe_19.505"], hs["val_7.5"])]
for lab, cc, hh in rows:
    print(f"{lab:30s} range {k_(cc['bottom_stated'])}-{k_(cc['top_stated'])} (top {k_(cc['top_unrounded'])}, "
          f"{cc['top_clear_of_115000_step']:+,.0f}) pay {k_(cc['funds_pay'])} kept {k_(cc['her_flexibility_shares_kept_jan2033'])} "
          f"kept+ {k_(cc['her_flexibility_plus_above_top'])} | house top<115k {hh['top_under_115000']:.1%} "
          f"(<110k {hh['top_under_110000']:.1%}; lower than at 7.5% same path {hh['top_lower_than_at_7_5_same_path']:.1%}) "
          f"shares alone {hh['shares_alone_top_under_115000_rates_at_forwards']:.1%} top p5/50/95 {hh['stated_top_p5_p50_p95']} "
          f"kept p50 {k_(hh['her_flexibility_shares_kept_p5_p50_p95'][1])}")
print("P/E exactly 19.5:", k_(val["5.0_pe_19.5_exact"]["top_unrounded"]), val["5.0_pe_19.5_exact"]["top_stated"])
for a, v in row24.items():
    print(f"row 24 {a:6s} sum {v['no_valuation_sum']:.2%}: P/E {v['pe_at_move_that_loses_the_step']:.2f} "
          f"(fall {v['fall_against_earnings']:.1%}; continuous {v['pe_if_sum_read_as_continuous_rate']:.2f}; card {v['card_row24']}) "
          f"P/E 19.5 -> {k_(v['pe_19_5_by_the_move_top_stated'])} ({k_(v['pe_19_5_by_the_move_top_unrounded'])})")
print("3.06%:", k_(gloomiest["top_unrounded"]), "| 3.70%:", k_(lowest_no_val["top_unrounded"]))
print("all asserts pass; seconds", out["seconds"])
