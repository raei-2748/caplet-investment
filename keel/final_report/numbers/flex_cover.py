"""The rise in building costs that her flexibility plus anything above the top covers, at four share returns (numbers
owner, Thu 19 Nov 2026 morning, Sydney). MODEL, not a forecast or a promise. NUMBERS 8u, "The about 25% at other share
returns"; bond desk 5, H2 (`research/panel/2026-11-18_bond_desk_5_3c_table3_3e.md`).

3e's note 3 figure, "about 25%" (8u row 4: her flexibility plus anything above the top, $28,682, covers a rise of 24.9% in
the US-dollar cost of a building budget set on the $115,000 top), rests mostly on the share forecast: $21,179 of the
$28,682 is the half of VT kept, grown at J.P. Morgan's 7.5% a year. Bond desk 5 gave the cover at 6.5% and 5.0% from
8v's pots by hand (23.6%, 21.7%). This script books them on the engine, with 3.1%, and asserts them:
  central   plan.run on today's forwards with VT at (1 + r) cubed to the move and squared after (8v's and 8p's
            convention); completion.rule for the stated ends; the contribution is the lower of what the late-2032 fund
            pays on its two purchases (January 2028 and the move) and the stated top; the pot is the half kept plus
            anything above the top; the cover is the pot over the contribution (= the stated top in every row), and,
            where the top steps down, also over $115,000.
  house     the register's 200,000 house paths (seed 2033) with VT's median moved to r and J.P. Morgan's 17.88% spread
            kept (8v's draws: at 7.5% they equal plan.draws number for number); the rise covered 19 times in 20 is the
            5th percentile of pot / contribution (8q's and taiwan_joint.py's definition; 15.8% at 7.5%, asserted).
The four returns are 8v's: 3.1% (card Q124's lowest sum, run at 3.1%), 5.0% (card Q124's middle; Syzygy, 8p), 6.5% (the
median of fifteen houses, card Q6b) and 7.5% (J.P. Morgan 2027, the register). 3.1% is also J.P. Morgan's 2026 cash
assumption (3.10%, the 2026 LTCMA in CLAUDE.md's verified facts); the 2027 edition's cash figure is not in the register,
so the row is labelled by card Q124, not as "J.P. Morgan's cash".

Nothing is re-sized: the register's design (H_plain with the fee cushion and the payments' 0.5% margin), the range rule
on the fund's holdings, Keel's reading of "most", the 6 Nov 2026 curve, the move on 1 Jan 2031.

Run from the repo root:  python3 -I keel/final_report/numbers/flex_cover.py
Writes keel/final_report/numbers/results_flex_cover_2026-11-19.json (about 10 seconds, numpy only). Imports engine.py,
plan.py and completion.py and changes none of them; reads no results file; writes no other file. It copies 8v's
central() and draws_at() from forecast_blocks.py rather than importing it, because importing it re-runs it and rewrites
its results file.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

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
OUT = HERE / "results_flex_cover_2026-11-19.json"
RATES = {"3.1": 0.031, "5.0": 0.050, "6.5": 0.065, "7.5": 0.075}     # 8v's four rows
f = lambda x: float(np.asarray(x).item())


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


def central(r):
    """8v's central row at a world-share return r (forecast_blocks.central, copied)."""
    res = P.run(c, margin=MARGIN, vt3=(1 + r) ** 3, vt2=(1 + r) ** 2, margin_fn=MF)
    rr = C.rule(res)
    pay, top = f(rr["payout"]), f(rr["top"])
    contrib = min(pay, top)
    kept = f(res["kept33"])
    pot = kept + pay - contrib
    return {"stated_bottom": f(rr["bottom"]), "stated_top": top, "top_unrounded": f(rr["top_raw"]),
            "late2032_fund_pays_both_purchases": pay, "contribution": contrib, "above_top": pay - contrib,
            "half_kept": kept, "her_flexibility_plus_anything_above_the_top": pot,
            "cover_on_the_stated_top": pot / contrib, "cover_on_115000": pot / STEP_TOP,
            "half_kept_alone_cover_on_the_stated_top": kept / contrib}


def draws_at(r):
    """plan.draws with VT's median growth at r: the same seed and order, so only the median moves (forecast_blocks)."""
    rng = np.random.default_rng(P.SEED)
    sv = E.ASSUMPTIONS["yield_vol"]
    d0 = rng.normal(0, sv * math.sqrt(E.yf(E.J27)), P.N)
    d1 = rng.normal(0, sv, P.N)
    d2 = rng.normal(0, sv * math.sqrt(3), P.N)
    mu = math.log(1 + r)
    vt3 = np.exp(rng.normal(mu * 3, SD * math.sqrt(3), P.N))
    vt2 = np.exp(rng.normal(mu * 2, SD * math.sqrt(2), P.N))
    return d0, d1, d2, vt3, vt2


for a_, b_ in zip(draws_at(0.075), P.draws()):
    assert np.array_equal(a_, b_)          # at 7.5% these are the register's draws, number for number


def house(r):
    d0, d1, d2, h3, h2 = draws_at(r)
    res = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, h3, h2, MF)
    rr = C.rule(res, d0 + d1, d0 + d1 + d2)
    pay, top = np.asarray(rr["payout"], float), np.asarray(rr["top"], float)
    contrib = np.minimum(pay, top)
    kept = np.asarray(res["kept33"], float)
    ok = contrib > 0
    cov = (kept + pay - contrib)[ok] / contrib[ok]
    cov_kept = kept[ok] / contrib[ok]
    return {"paths": int(ok.sum()),
            "rise_covered_19_in_20": float(np.percentile(cov, 5)), "rise_covered_median": float(np.median(cov)),
            "half_kept_alone_19_in_20": float(np.percentile(cov_kept, 5)),
            "half_kept_alone_median": float(np.median(cov_kept))}


cen = {k: central(r) for k, r in RATES.items()}
hs = {k: house(r) for k, r in RATES.items()}

# ---------------------------------------------------------------- register checks (8u, 8v, 8q)
j = cen["7.5"]
near(j["her_flexibility_plus_anything_above_the_top"], 28_682.31, 0.01, "8u/8v $28,682 at 7.5%")
near(j["half_kept"], 21_179.18, 0.01, "half kept 7.5%")
near(j["above_top"], 7_503.13, 0.01, "above the top 7.5%")
near(100 * j["cover_on_the_stated_top"], 24.94, 0.005, "8u/8q 24.9% at 7.5%")
near(cen["6.5"]["her_flexibility_plus_anything_above_the_top"], 27_159, 1, "8v $27,159 at 6.5%")
near(cen["5.0"]["her_flexibility_plus_anything_above_the_top"], 24_959, 1, "8v $24,959 at 5.0%")
near(cen["3.1"]["her_flexibility_plus_anything_above_the_top"], 27_316, 1, "8v $27,316 at 3.1%")
near(cen["6.5"]["half_kept"], 20_212, 1, "8v $20,212")
near(cen["5.0"]["half_kept"], 18_828, 1, "8v $18,828")
near(cen["3.1"]["half_kept"], 17_185, 1, "8v $17,185")
for k in RATES:
    assert cen[k]["stated_bottom"] == 95_000, k
    assert cen[k]["contribution"] == cen[k]["stated_top"], k        # the contribution is the stated top in every row
assert cen["3.1"]["stated_top"] == 110_000 and all(cen[k]["stated_top"] == STEP_TOP for k in ("5.0", "6.5", "7.5"))
# bond desk 5, H2: 23.6% at 6.5% and 21.7% at 5.0% (8v's pots over $115,000, by hand)
near(round(100 * cen["6.5"]["cover_on_the_stated_top"], 1), 23.6, 1e-9, "bond desk 23.6% at 6.5%")
near(round(100 * cen["5.0"]["cover_on_the_stated_top"], 1), 21.7, 1e-9, "bond desk 21.7% at 5.0%")
# new (Thu 19 Nov): 3.1%, on its own $110,000 top and on a $115,000 budget
near(round(100 * cen["3.1"]["cover_on_the_stated_top"], 1), 24.8, 1e-9, "3.1% on its $110,000 top")
near(round(100 * cen["3.1"]["cover_on_115000"], 1), 23.8, 1e-9, "3.1% on $115,000")
# 8q's house figures at 7.5%: 15.8% (9.3% half kept alone) covered 19 times in 20
near(round(100 * hs["7.5"]["rise_covered_19_in_20"], 1), 15.8, 1e-9, "8q house 15.8%")
near(round(100 * hs["7.5"]["half_kept_alone_19_in_20"], 1), 9.3, 1e-9, "8q house 9.3%")
# the order of the central covers: lower with the forecast, except where the top steps down and $5,000 stays with her
assert cen["5.0"]["cover_on_the_stated_top"] < cen["6.5"]["cover_on_the_stated_top"] < j["cover_on_the_stated_top"]
assert cen["3.1"]["cover_on_the_stated_top"] > cen["5.0"]["cover_on_the_stated_top"]

out = {"run": "Thu 19 Nov 2026 morning (Sydney), numbers owner", "section": "NUMBERS 8u (the about 25% at other share "
       "returns); bond desk 5, H2", "rule": C.RULE_VERSION, "design": NAME, "curve": E.CURVE_DAY,
       "register_results": C.RESULTS,
       "basis": "register as re-sized Tue 17 Nov evening; central path at today's forwards, VT at (1+r)^3 to the move and "
                "(1+r)^2 after; house model 200,000 paths, seed 2033, VT median moved to r, 17.88% spread kept; "
                "cover = (half kept + anything above the top) / contribution (= stated top)",
       "rates": RATES, "central": cen, "house": hs, "all_asserts_pass": True}
OUT.write_text(json.dumps(out, indent=1, default=float))

k_ = lambda x: f"${x:,.0f}"
for k in RATES:
    cc, hh = cen[k], hs[k]
    print(f"{k}% a year: range {k_(cc['stated_bottom'])}-{k_(cc['stated_top'])}; her flexibility plus anything above the "
          f"top {k_(cc['her_flexibility_plus_anything_above_the_top'])} (half kept {k_(cc['half_kept'])} + above the top "
          f"{k_(cc['above_top'])}); covers a rise of {cc['cover_on_the_stated_top']:.2%} on the stated top "
          f"({cc['cover_on_115000']:.2%} on $115,000; half kept alone {cc['half_kept_alone_cover_on_the_stated_top']:.2%}); "
          f"house 19 in 20 {hh['rise_covered_19_in_20']:.1%} (half kept alone {hh['half_kept_alone_19_in_20']:.1%}), "
          f"median {hh['rise_covered_median']:.1%}")
print("all asserts pass; wrote", OUT.name)
