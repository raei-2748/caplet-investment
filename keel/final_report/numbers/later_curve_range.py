"""The range rule on a later curve: 13 Nov 2026 against the register's 6 Nov 2026 (numbers owner, Wed 18 Nov 2026
evening, Sydney). MODEL and Keel arithmetic, not a forecast or a promise. NUMBERS 4, "On a later curve (Wed 18 Nov
evening)", and 5.

Bond desk 5 (research/panel/2026-11-18_bond_desk_5_3c_table3_3e.md, H3) re-ran the plan on the 13 Nov 2026 par curve
in scratch and found the range rule's ends at about $105,000 and $125,000 (first slice $31,859, floor money $86,597),
where section 5's dated line (card Q98's script, re-run Tue 17 Nov evening) gives a first slice of $32,074 and floor
money $86,440. This script:
  1. reads the 13 Nov curve from card Q98's own file (research/cards/data/Q98_eight_week_moves.py, the dict
     NOV13_FULL, read at source from treasury.gov's TextView on Tue 17 Nov) by parsing it, never by running it (importing
     the card's script re-runs it for four minutes and rewrites its CSV);
  2. reproduces the register on the 6 Nov curve through one curve-general route (completion.build on the curve, the
     first slice = (the ten plus the extra Treasuries - $300,000) carried a year at that curve's 2027 rate on 2027's 365
     days, plan.run with that backstop, the range rule's zero_per_dollar re-written with the curve as an argument) and
     asserts it against completion.rule(plan.run(...)) and NUMBERS 4 to the cent;
  3. runs the same route on the 13 Nov curve (main: the range rule's holdings as section 0 defines them, the engine's
     IBTM bond with its 4.2513% coupon fixed on 6 Nov, priced on the later curve, as break_test.py prices them on a moved
     curve); variants: holdings re-couponed at the 13 Nov par yield, IBTM's real 3.50% and 4.00% coupons, and the curve
     anchored on 13 Nov rather than the engine's 6 Nov value date;
  4. reproduces card Q98's route (the extra Treasuries read off a 0.05-point grid of PARALLEL shifts of the 6 Nov curve
     at the parallel shift that gives the same cost of the ten; a year's carry without the 365.25-day fix) and splits the
     gap between the two routes;
  5. measures the yield moves between the curves (par yields at each tenor; the forward rates the range turns on; the
     parallel shift with the same cost of the ten) and the parallel rises before 1 Jan 2027 that step each end, on 8u's
     method (break_test.bottom_raw_before: exact re-sizing, holdings priced on today's forwards plus the shift).
The register's curve does not change (NUMBERS 0: one curve, the day trading froze).

Run from the repo root:  python3 -I keel/final_report/numbers/later_curve_range.py
Writes keel/final_report/numbers/results_later_curve_2026-11-18.json (about a minute, numpy only). Imports engine,
plan and completion and changes none of them; reads the card's file as text; writes no other file.
"""
import ast
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

ROOT = HERE.parents[2]
CARD = ROOT / "keel/final_report/research/cards/data/Q98_eight_week_moves.py"
OUT = HERE / "results_later_curve_2026-11-18.json"
H, FEE, VFEE = C.HAIRCUT, C.FEE, E.ASSUMPTIONS["vt_fee"]
DEP, SHARE = 150_000.0, E.ASSUMPTIONS["floor_share"]
HALF1 = DEP / 2 + 1.0
f = lambda x: float(np.asarray(x).item())


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


def bisect(fn, lo, hi, iters=60):
    flo = fn(lo)
    assert flo * fn(hi) < 0, (lo, hi, flo, fn(hi))
    for _ in range(iters):
        mid = (lo + hi) / 2
        if (fn(mid) > 0) == (flo > 0):
            lo, flo = mid, fn(mid)
        else:
            hi = mid
    return (lo + hi) / 2


# ================================================================ 0. the curves
def card_constants():
    """NOV13_FULL and NOV_AT_SOURCE from the card's file, parsed (the file is Keel's own; never run here)."""
    got = {}
    for node in ast.parse(CARD.read_text()).body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id in ("NOV13_FULL", "NOV_AT_SOURCE")):
            got[node.targets[0].id] = eval(compile(ast.Expression(node.value), str(CARD), "eval"),
                                           {"__builtins__": {}, "date": date})
    return got


K = card_constants()
NOV13 = K["NOV13_FULL"]
row13 = K["NOV_AT_SOURCE"][date(2026, 11, 13)]           # 6 Mo, 1, 2, 3, 5, 7, 10, 20, 30 years
for t, v in zip((0.5, 1, 2, 3, 5, 7, 10, 20, 30), row13):
    assert NOV13[t] == v, (t, NOV13[t], v)
assert sorted(NOV13) == sorted(C.c.par), "same twelve tenors as the 6 Nov file"
c6 = C.c
c13 = E.Curve(NOV13)


class CurveAt(E.Curve):
    """The same bootstrap with its own value date (the engine's Curve measures every tenor from 6 Nov 2026)."""

    def __init__(self, par, val, shift=0.0):
        super().__init__(par, shift)
        self.val = val

    def P(self, d, base=E.J27):
        return self.df(E.yf(d, self.val)) / self.df(E.yf(base, self.val))


c13v = CurveAt(NOV13, date(2026, 11, 13))


# ================================================================ 1. one curve-general route
def zpd(buy, curve, hold):
    """completion.zero_per_dollar with the curve as an argument (no shift, no multiplier)."""
    fl = [(d, a) for d, a in hold if d > buy]
    nav = sum(a * math.exp(-max(curve.fwd(buy, d), 0.0) * E.yf(d, buy)) for d, a in fl)
    z = sum(a * (1 - FEE) ** E.yf(d, buy) * (C._PW if d == C.WAM else math.exp(-C.RULE_WAIT_FEE * E.yf(C.END, d)))
            for d, a in fl)
    return z / nav


def hold_on(curve):
    """The engine's IBTM holdings re-couponed at this curve's par yield to the fund's average maturity (variant)."""
    i = E.instruments(curve)[2033]
    return [(d, a / (1 - FEE) ** E.yf(d, E.J27)) for d, a, _ in i.flows]


def on_curve(curve, hold=None):
    hold = C.HOLD["engine"] if hold is None else hold
    b = C.build(curve)
    plain, back, tot = b["plain_cost"], b["H_plain"]["margin"], b["H_plain"]["cost"]
    carry = math.exp(curve.fwd(E.J27, E.J28) * E.T01)
    res = P.run(curve, margin=back)                       # margin_fn None: back x exp(f01 x T01) at no move
    first = (tot - 300_000.0) * carry
    near(f(res["R"]), DEP - first, 0.01, "plan.run's money left = deposit - first slice")
    fm, mm, vt = f(res["floor_money"]), f(res["moved_money"]), f(res["vt28"])
    zF, zM = zpd(E.J28, curve, hold), zpd(E.J31, curve, hold)
    Fz, Mz = fm * zF, mm * zM
    b_raw, t_raw = Fz * (1 - H), (Fz + Mz) * (1 - H)
    bottom, top = f(C.down(b_raw)), f(C.down(t_raw))
    pay = f(res["floor"]) + f(res["moved"])
    gift = min(pay, top)
    kept = f(res["kept33"])
    return {"ten_cost_jan2027": plain, "extra_treasuries_jan2027": back, "ten_and_extra_jan2027": tot,
            "carry_2027": carry, "topup_jan2028": max(plain - 300_000.0, 0.0) * carry,
            "left_over_from_first_deposit_jan2028": max(300_000.0 - plain, 0.0) * carry,
            "extra_treasuries_jan2028": back * carry, "first_slice_jan2028": first, "first_slice_share": first / DEP,
            "deposit_fall_standard_survives": 1 - first / DEP,
            "floor_money": fm, "vt_bought": vt, "moved_money": mm, "most_binds": bool(f(res["most_binds"])),
            "zF": zF, "zM": zM, "floor_zero": Fz, "moved_zero": Mz, "both_zero": Fz + Mz,
            "bottom_raw": b_raw, "top_raw": t_raw, "bottom": bottom, "top": top,
            "floor_pays": f(res["floor"]), "moved_pays": f(res["moved"]), "funds_pay": pay,
            "contribution": gift, "excess": pay - gift, "half_kept": kept, "flexibility": kept + pay - gift,
            "cover_top_zero": 1 - top / (Fz + Mz), "cover_top_forwards": 1 - top / pay,
            "cover_bottom_zero": 1 - bottom / Fz,
            "fwd_2027": curve.fwd(E.J27, E.J28), "fwd_floor_jan2028_to_end": curve.fwd(E.J28, C.END),
            "fwd_moved_jan2031_to_end": curve.fwd(E.J31, C.END)}


# 1a. the check: the route reproduces the register on 6 Nov to the cent
r6 = on_curve(c6)
MARGIN, MF = C.design(C.CALL)["margin"], C.margin_fn(C.CALL)
cen = P.run(c6, margin=MARGIN, margin_fn=MF)
rr = C.rule(cen)
near(r6["zF"], f(C.zero_per_dollar(E.J28)), 1e-12, "zF")
near(r6["zM"], f(C.zero_per_dollar(E.J31)), 1e-12, "zM")
for k, kk in (("bottom_raw", "bottom_raw"), ("top_raw", "top_raw"), ("bottom", "bottom"), ("top", "top"),
              ("funds_pay", "payout"), ("excess", "excess")):
    near(r6[k], f(rr[kk]), 0.01, f"6 Nov {k} against completion.rule")
near(r6["floor_money"], f(cen["floor_money"]), 0.01, "floor money")
near(r6["first_slice_jan2028"], C.completion_exact(0.0)[0], 0.01, "first slice")
for k, reg in (("first_slice_jan2028", 39_162), ("topup_jan2028", 2_388), ("extra_treasuries_jan2028", 36_774),
               ("floor_money", 81_244), ("vt_bought", 29_594), ("bottom_raw", 97_605), ("top_raw", 117_142),
               ("funds_pay", 122_503), ("excess", 7_503), ("half_kept", 21_179), ("flexibility", 28_682),
               ("ten_and_extra_jan2027", 337_499), ("ten_cost_jan2027", 302_287)):
    near(r6[k], reg, 1, f"register {k}")
assert (r6["bottom"], r6["top"]) == (95_000.0, 115_000.0)
near(r6["zF"], 1.207415, 5e-7, "1.207415")
near(r6["zM"], 1.070113, 5e-7, "1.070113")

# 1b. the 13 Nov curve: main and variants
r13 = on_curve(c13)
variants = {
    "holdings_recouponed_at_13nov_par": on_curve(c13, hold_on(c13)),
    "holdings_coupon_3.50": on_curve(c13, C.HOLD["coupon_3.50"]),
    "holdings_coupon_4.00": on_curve(c13, C.HOLD["coupon_4.00"]),
    "curve_anchored_on_13nov": on_curve(c13v),
}
variants["holdings_recouponed_at_13nov_par"]["coupon"] = 2 * hold_on(c13)[0][1]

# ================================================================ 2. card Q98's route, reproduced, and the gap
def ten_cost(curve):
    ins = E.instruments(curve)
    return E.cost(ins, E.size_own_rung(ins, E.Reinvest(curve)))


cost13 = ten_cost(c13)
near(cost13, r13["ten_cost_jan2027"], 1e-6, "ten cost")
# Q98's s_equiv: np.interp on a 0.0001 grid of parallel shifts of the 6 Nov curve; only the bracketing points matter
s_exact = bisect(lambda s: ten_cost(E.Curve(c6.par, shift=s)) - cost13, 0.0, 0.01)
g0 = math.floor(s_exact * 1e4) / 1e4
g1 = g0 + 1e-4
k0, k1 = ten_cost(E.Curve(c6.par, shift=g0)), ten_cost(E.Curve(c6.par, shift=g1))
s_q98 = g0 + (k0 - cost13) / (k0 - k1) * (g1 - g0)
near(s_q98, 0.00277293, 2e-8, "card Q98's s for 13 Nov (its CSV)")
# Q98's backstop: np.interp on a 0.0005 grid of C.shifted(s)["H_plain"]["margin"]
b0 = math.floor(round(s_q98 / 0.0005, 9)) * 0.0005
m0, m1 = C.shifted(b0)["H_plain"]["margin"], C.shifted(b0 + 0.0005)["H_plain"]["margin"]
back_q98 = m0 + (m1 - m0) * (s_q98 - b0) / 0.0005
carry_q98 = math.exp(c13.fwd(E.J27, E.J28))             # the card's carry: a 365.25-day 2027
q98 = {"parallel_equivalent_shift_points": 100 * s_q98, "extra_treasuries_jan2027": back_q98,
       "extra_treasuries_jan2028": back_q98 * carry_q98,
       "left_over_jan2028": (300_000.0 - cost13) * carry_q98}
q98["first_slice_jan2028"] = q98["extra_treasuries_jan2028"] - q98["left_over_jan2028"]
left = DEP - q98["first_slice_jan2028"]
q98["floor_money"] = max(SHARE * left, min(left, HALF1))
q98["vt_bought"] = left - q98["floor_money"]
for k, reg in (("extra_treasuries_jan2028", 38_277), ("left_over_jan2028", 6_203), ("first_slice_jan2028", 32_074),
               ("floor_money", 86_440), ("vt_bought", 31_486)):
    near(q98[k], reg, 1, f"section 5's later-curve line {k}")
# the range on section 5's figures (the rule's holdings priced on 13 Nov)
mm_q98 = q98["vt_bought"] * 1.075 ** 3 * (1 - VFEE) ** 3 / 2
q98["bottom_raw"] = q98["floor_money"] * r13["zF"] * (1 - H)
q98["top_raw"] = (q98["floor_money"] * r13["zF"] + mm_q98 * r13["zM"]) * (1 - H)
q98["bottom"], q98["top"] = f(C.down(q98["bottom_raw"])), f(C.down(q98["top_raw"]))
# the split of the gap in the first slice: (i) the extra Treasuries, exact on the 13 Nov curve against the parallel
# grid; (ii) the carry's day count
gap = {"first_slice_route_gap": q98["first_slice_jan2028"] - r13["first_slice_jan2028"],
       "extra_treasuries_jan2027_exact_minus_grid": r13["extra_treasuries_jan2027"] - back_q98,
       "from_the_extra_treasuries_jan2028": (back_q98 - r13["extra_treasuries_jan2027"]) * r13["carry_2027"],
       "from_the_carry_day_count": (r13["ten_and_extra_jan2027"] - 300_000.0) * (carry_q98 - r13["carry_2027"]),
       "extra_treasuries_exact_at_the_parallel_shift_jan2027": C.build(E.Curve(c6.par, shift=s_q98))["H_plain"]["margin"]}
gap["grid_interpolation_jan2027"] = back_q98 - gap["extra_treasuries_exact_at_the_parallel_shift_jan2027"]
gap["curve_shape_jan2027"] = gap["extra_treasuries_exact_at_the_parallel_shift_jan2027"] - r13["extra_treasuries_jan2027"]
near(gap["from_the_extra_treasuries_jan2028"] + gap["from_the_carry_day_count"], gap["first_slice_route_gap"], 0.01,
     "the two parts add up")

# ================================================================ 3. the yield moves, and the parallel rises that step each end
TEN = {"1 month": 1 / 12, "3 months": 0.25, "6 months": 0.5, "1 year": 1, "2 years": 2, "3 years": 3, "5 years": 5,
       "7 years": 7, "10 years": 10, "20 years": 20, "30 years": 30}
moves = {k: {"6 Nov": c6.par[t], "13 Nov": NOV13[t], "change_points": round(NOV13[t] - c6.par[t], 4)}
         for k, t in TEN.items()}
fwd = {k: {"6 Nov": 100 * r6[k], "13 Nov": 100 * r13[k], "change_points": 100 * (r13[k] - r6[k])}
       for k in ("fwd_2027", "fwd_floor_jan2028_to_end", "fwd_moved_jan2031_to_end")}


def bottom_raw_before(x):
    """8u's method (break_test.bottom_raw_before): parallel move -x of the 6 Nov curve before 1 Jan 2027 (x > 0 a fall),
    exact re-sizing, the rule's holdings priced on today's forwards moved by the same amount."""
    lft = DEP - C.completion_exact(-x)[0]
    fm = max(SHARE * lft, min(lft, HALF1))
    return fm * f(C.zero_per_dollar(E.J28, -x)) * (1 - H)


def top_raw_before(x):
    """The same for the top: the floor's part plus the moved half's (VT at 7.5% to the move), one rounding."""
    lft = DEP - C.completion_exact(-x)[0]
    fm = max(SHARE * lft, min(lft, HALF1))
    mm = (lft - fm) * 1.075 ** 3 * (1 - VFEE) ** 3 / 2
    return (fm * f(C.zero_per_dollar(E.J28, -x)) + mm * f(C.zero_per_dollar(E.J31, -x))) * (1 - H)


near(bottom_raw_before(0.0), r6["bottom_raw"], 0.01, "8u bottom at no move")
near(top_raw_before(0.0), r6["top_raw"], 0.01, "top at no move")
steps = {"bottom": {}, "top": {}}
for tgt in (100_000, 105_000, 110_000):
    steps["bottom"][f"rise_to_state_{tgt}"] = 100 * bisect(lambda x: bottom_raw_before(-x) - tgt, 0.0, 0.02)
for tgt in (120_000, 125_000, 130_000):
    steps["top"][f"rise_to_state_{tgt}"] = 100 * bisect(lambda x: top_raw_before(-x) - tgt, 0.0, 0.02)
for tgt in (95_000, 90_000):
    steps["bottom"][f"fall_to_state_under_{tgt}"] = 100 * bisect(lambda x: bottom_raw_before(x) - tgt, 0.0, 0.02)
for tgt in (115_000, 110_000):
    steps["top"][f"fall_to_state_under_{tgt}"] = 100 * bisect(lambda x: top_raw_before(x) - tgt, 0.0, 0.02)
near(steps["bottom"]["rise_to_state_100000"], 0.09, 0.005, "8u: a rise of 0.09 points states $100,000")
near(steps["bottom"]["fall_to_state_under_95000"], 0.10, 0.005, "8u: a fall of about 0.10 points states $90,000")
# the parallel rise on the 6 Nov curve that gives the 13 Nov unrounded ends (how big the week was, for the range)
equiv = {"bottom": 100 * bisect(lambda x: bottom_raw_before(-x) - r13["bottom_raw"], 0.0, 0.02),
         "top": 100 * bisect(lambda x: top_raw_before(-x) - r13["top_raw"], 0.0, 0.02),
         "cost_of_the_ten": 100 * s_exact}

# ================================================================ 4. bond desk 5's scratch figures, against these
desk = {"ten_and_extra_jan2027": 330_402, "first_slice_jan2028": 31_859, "floor_money": 86_597,
        "bottom_raw": 105_407, "top_raw": 126_323}
for k, v in desk.items():
    near(r13[k], v, 1, f"bond desk 5's {k}")

out = {"run": "Wed 18 Nov 2026 evening (Sydney), numbers owner", "rule": C.RULE_VERSION, "design": C.CALL,
       "register_curve": E.CURVE_DAY, "register_results": C.RESULTS,
       "later_curve": "13 Nov 2026 close, treasury.gov TextView read at source Tue 17 Nov 2026 (Sydney), as embedded "
                      "in research/cards/data/Q98_eight_week_moves.py (NOV13_FULL; parsed, not run)",
       "note": "MODEL, Keel arithmetic. Disclosed beside the register, never re-booked: the register stays on 6 Nov.",
       "check_6nov_reproduces_register": r6, "on_13nov": r13, "variants_13nov": variants,
       "card_q98_route_13nov": q98, "route_gap_13nov": gap,
       "par_yield_moves": moves, "forward_rate_moves_percent": fwd,
       "parallel_steps_before_jan2027_points_8u_method": steps,
       "parallel_rise_equivalent_to_13nov_points": equiv,
       "bond_desk_5_scratch_reproduced": desk}
OUT.write_text(json.dumps(out, indent=1, default=float))

k = lambda x: f"${x:,.0f}"
print("6 Nov check:", k(r6["first_slice_jan2028"]), k(r6["floor_money"]), k(r6["bottom_raw"]), k(r6["top_raw"]),
      r6["bottom"], r6["top"])
print("13 Nov:", "ten", k(r13["ten_cost_jan2027"]), "ten+extra", k(r13["ten_and_extra_jan2027"]), "left over",
      k(r13["left_over_from_first_deposit_jan2028"]), "extra 2028", k(r13["extra_treasuries_jan2028"]), "first",
      k(r13["first_slice_jan2028"]), f"({r13['first_slice_share']:.1%})", "floor", k(r13["floor_money"]), "VT",
      k(r13["vt_bought"]))
print("   zF %.6f zM %.6f bottom raw %s top raw %s stated %s to %s; funds pay %s excess %s kept %s flex %s"
      % (r13["zF"], r13["zM"], k(r13["bottom_raw"]), k(r13["top_raw"]), k(r13["bottom"]), k(r13["top"]),
         k(r13["funds_pay"]), k(r13["excess"]), k(r13["half_kept"]), k(r13["flexibility"])))
for n, v in variants.items():
    print("   variant", n, k(v["bottom_raw"]), k(v["top_raw"]), k(v["bottom"]), k(v["top"]), "first",
          k(v["first_slice_jan2028"]))
print("Q98 route:", {a: (round(b) if abs(b) > 10 else round(b, 4)) for a, b in q98.items()})
print("gap:", {a: round(b, 2) for a, b in gap.items()})
print("par moves:", {a: b["change_points"] for a, b in moves.items()})
print("forward moves:", {a: round(b["change_points"], 3) for a, b in fwd.items()})
print("steps:", {a: {b: round(v, 3) for b, v in d.items()} for a, d in steps.items()})
print("13 Nov as a parallel rise:", {a: round(b, 3) for a, b in equiv.items()})
print("wrote", OUT)
