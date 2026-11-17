"""What it takes to break each promise (numbers owner, Wed 18 Nov 2026 morning, Sydney). MODEL, not a forecast or a
promise. NUMBERS 8u.

Card Q109's shape for 3e (a reverse stress test: "define what constitutes business failure and then detail what
events could drive that outcome", PRA 2025 draft, 8.2): for each of Laura's promises, the failure in plain words, the
events that would drive it and the size each event would need. Most sizes are already register figures (NUMBERS 1-5,
8h, 8j, 8p, 8q, 8t); this script re-derives every one it can from the engine, asserts it against the register, and
computes the few that are not yet there:
  (1) the payments: the shortfall and the interest waiting money would need if fund costs beyond the 0.07% fee pass the
      0.5% margin the payments carry (0.75%, 1%, 2% of every iBond fund flow), the same ledger as cost_cover.py part B;
  (2) the stated bottom: its own cover against fund costs, the floor alone, centrally and in every house path, at zero
      interest and at the modelled payout; and the fall in yields (before 1 Jan 2027, or during 2027 alone) that would
      lower the bottom she can state by one $5,000 step (it lowers a figure not yet stated, so it breaks nothing).
Nothing is re-sized: the register's design (H_plain with the fee cushion and the payments' 0.5% margin), the range rule
on the fund's holdings, Keel's reading of "most", the house model (200,000 paths, seed 2033), the 6 Nov 2026 curve.

Run from the repo root:  python3 -I keel/final_report/numbers/break_test.py
Writes keel/final_report/numbers/results_break_2026-11-18.json (about 30 seconds, numpy only). Imports engine.py,
plan.py and completion.py and changes none of them; reads no results file; writes no other file. Two helpers are copied
from cost_cover.py (insts_less) and most_check.py (comp's re-pricing is not needed: a fall during 2027 is priced by
plan.run with completion.margin_fn, as section 5's "A fall during 2027" is), because importing either script re-runs it
and rewrites its results file.
"""
import copy
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
DEP = 150_000.0
HALF = DEP / 2
SHARE = E.ASSUMPTIONS["floor_share"]
H = C.HAIRCUT
FUND_YEARS = (2033, 2034, 2035, 2036, 2037)
OUT = HERE / "results_break_2026-11-18.json"
f = lambda x: float(np.asarray(x).item())


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


def bisect(fn, lo, hi, iters=80):
    """x in [lo, hi] where fn changes sign (fn(lo) and fn(hi) of opposite sign)."""
    flo = fn(lo)
    assert flo * fn(hi) < 0, (lo, hi, flo, fn(hi))
    for _ in range(iters):
        mid = (lo + hi) / 2
        if (fn(mid) > 0) == (flo > 0):
            lo, flo = mid, fn(mid)
        else:
            hi = mid
    return (lo + hi) / 2


out = {"run": "Wed 18 Nov 2026 morning (Sydney), numbers owner", "rule": C.RULE_VERSION, "design": NAME,
       "curve": E.CURVE_DAY, "register_results": C.RESULTS,
       "note": "MODEL. Register figures re-derived and asserted; new figures marked new in NUMBERS 8u."}

# ================================================================ 1. The ten payments
pay = {}
# 1a. The 2028 deposit: the first slice the standard needs, and the ladder's own tail (IPS l.13's top-up)
first = C.completion_exact(0.0)[0]
tail = C.completion_exact(0.0, "plain")[0]
near(first, 39_162, 1, "first slice")
near(tail, 2_388, 1, "top-up")
pay["deposit"] = {"first_slice_jan2028": first, "standard_survives_a_deposit_fall_of": 1 - first / DEP,
                  "topup_jan2028": tail, "ladder_at_forwards_survives_a_deposit_fall_of": 1 - tail / DEP}
# 1b. A fall in yields before 1 Jan 2027 that would take the whole deposit (the window closes when the ten are bought)
x_std = bisect(lambda x: C.completion_exact(-x)[0] - DEP, 0.02, 0.05)
x_lad = bisect(lambda x: C.completion_exact(-x, "plain")[0] - DEP, 0.02, 0.05)
near(100 * x_std, 3.57, 0.01, "standard takes the whole deposit")
near(100 * x_lad, 3.89, 0.01, "ladder takes the whole deposit")
pay["fall_before_jan2027_taking_the_whole_deposit_points"] = {"standard": 100 * x_std, "ladder_at_forwards": 100 * x_lad}
# 1c. A fall during 2027 alone (the ten bought): even at zero rates in January 2028 the first slice is (most_check (b))
z = P.run(c, d1=-0.10, margin_fn=MF)       # every rate floored (plan.run floors the floor's yield; the slice by margin_fn)
for fall, reg in ((0.005, 40_821), (0.01, 42_569), (0.02, 46_351)):
    near(f(P.run(c, d1=-fall, margin_fn=MF)["complete"]), reg, 1, f"2027 fall {fall}")
pay["fall_during_2027"] = {"first_slice_after_2pt": f(P.run(c, d1=-0.02, margin_fn=MF)["complete"]),
                           "register_first_slice_at_zero_rates_most_check_b": 60_393,
                           "plan_run_first_slice_at_d1_minus_10pt": f(z["complete"]),
                           "note": "most_check (b) prices the tail on its flows with rates floored at zero: $60,393 "
                                   "(register). plan.run prices the tail by duration, so its -10-point figure is not "
                                   "the floored one and is shown only as a check that no 2027 fall reaches $150,000."}
assert f(z["complete"]) < DEP
# 1d. A missed deposit (run_numbers.py's own construction): the ladder's tail unbought, no extra Treasuries
tailc = C.PLAIN_COST - 300_000
pl = dict(C.PLAIN)
pl[2033] = C.PLAIN[2033] - tailc / C.I[2033].price
miss_fwd = C.ledger(C.BASE, pl)[0]
miss_zero = C.short(C.ZERO, pl)
near(E.PAYMENT - miss_fwd[2033], 3_016, 1, "missed deposit 2033 at forwards")
near(miss_zero, 57_455, 1, "missed deposit at zero")
pay["missed_deposit"] = {"short_2033_at_forwards": E.PAYMENT - miss_fwd[2033], "short_ten_at_zero": miss_zero,
                         "short_ten_zero_and_bill_fee": C.short(C.FEEW, pl)}


# 1e. Fund costs beyond the 0.07% fee (copied from cost_cover.py: every iBond fund flow cut by x)
def insts_less(x_by_year):
    ins = {}
    for y in E.YEARS:
        i = copy.copy(C.I[y])
        x = x_by_year.get(y, 0.0)
        if x:
            i.flows = [(d, a * (1 - x), k) for d, a, k in C.I[y].flows]
        ins[y] = i
    return ins


OWN, POOL = C.PLAIN, C.BACKSTOP
costs = {}
for x in (0.005, 0.0075, 0.01, 0.02):
    ins = insts_less({y: x for y in FUND_YEARS})
    paid_fw = C.ledger(C.FEEW, OWN, POOL, ins)[0]
    sh = {y: E.PAYMENT - v for y, v in paid_fw.items() if E.PAYMENT - v > 0.005}
    lo, hi = -C.WAIT_FEE - 0.02, 0.05
    for _ in range(60):                       # the lowest net yearly rate on waiting money at which all ten are paid
        mid = (lo + hi) / 2
        if C.short(C.Flat(c, mid), OWN, POOL, ins) > 0.005:
            lo = mid
        else:
            hi = mid
    costs[f"{x:.4f}"] = {"short_standard_total": sum(sh.values()), "short_standard_by_year": {str(k): v for k, v in sh.items()},
                         "short_zero_no_bill_fee": C.short(C.ZERO, OWN, POOL, ins),
                         "left_after_2042_forwards": C.ledger(C.BASE, OWN, POOL, ins)[3],
                         "net_rate_needed_on_waiting_money": hi, "gross_rate_needed_before_bill_fee": hi + C.WAIT_FEE}
near(costs["0.0050"]["short_standard_total"], 0.0, 0.01, "0.5% covered under the standard")
near(costs["0.0050"]["left_after_2042_forwards"], 74_031, 1, "0.5% at forwards (NUMBERS 2)")
for key, world in (("standard", C.FEEW), ("zero_no_bill_fee", C.ZERO)):
    lo, hi = 0.0, 0.03
    for _ in range(60):
        mid = (lo + hi) / 2
        if C.short(world, OWN, POOL, insts_less({y: mid for y in FUND_YEARS})) > 0.005:
            hi = mid
        else:
            lo = mid
    costs[f"largest_cost_covered_{key}"] = lo
near(100 * costs["largest_cost_covered_standard"], 0.50, 0.005, "largest covered (standard)")
near(100 * costs["largest_cost_covered_zero_no_bill_fee"], 0.74, 0.005, "largest covered (no bill fee)")
pay["fund_costs_beyond_fee"] = costs
out["1_payments"] = pay

# ================================================================ 2. The stated bottom, and 3. the stated top (central)
cen = P.run(c, margin=MARGIN, margin_fn=MF)
rc = C.rule(cen)
Fz, Tz = f(rc["floor_zero"]), f(rc["zero_world"])
bot, top = f(rc["bottom"]), f(rc["top"])
Fpay, PAY = f(cen["floor"]), f(rc["payout"])
assert (bot, top) == (95_000.0, 115_000.0)
near(1 - top / Tz, 0.0232, 0.00005, "top cover zero")
near(1 - top / PAY, 0.06125, 0.00005, "top cover modelled")
near(1 - bot / Fz, 0.0316, 0.00005, "bottom cover floor alone zero")
near(Fpay, 102_365, 1, "floor payout")
bottom = {"central": {"floor_zero_value": Fz, "floor_modelled_payout": Fpay, "stated_bottom": bot,
                      "cover_floor_alone_zero_interest": 1 - bot / Fz,
                      "cover_floor_alone_modelled_payout": 1 - bot / Fpay}}
topd = {"central": {"both_zero_value": Tz, "both_modelled_payout": PAY, "stated_top": top,
                    "cover_zero_interest": 1 - top / Tz, "cover_modelled_payout": 1 - top / PAY}}

# house model: the bottom's own cover in every path (floor alone), at zero interest and at the modelled payout
d0, d1, d2, vt3, vt2 = P.draws(P.N, P.SEED)
Hh = P.run(c, MARGIN, None, DEP, d0, d1, d2, vt3, vt2, MF)
rh = C.rule(Hh, d0 + d1, d0 + d1 + d2)
B, FZ, FP = rh["bottom"], rh["floor_zero"], np.asarray(Hh["floor"], float)
ok = B > 0
cbz, cbm = 1 - B[ok] / FZ[ok], 1 - B[ok] / FP[ok]
bottom["house"] = {"paths": int(ok.sum()),
                   "cover_zero_interest": {"min": float(cbz.min()), "p5": float(np.percentile(cbz, 5)),
                                           "median": float(np.median(cbz))},
                   "cover_modelled_payout": {"min": float(cbm.min()), "p5": float(np.percentile(cbm, 5)),
                                             "median": float(np.median(cbm))}}
assert cbz.min() >= H - 1e-9
for x in (0.0075, 0.01):
    bottom["house"][f"paths_below_bottom_zero_interest_at_cost_{x:.4f}"] = int((FZ[ok] * (1 - x) < B[ok] - 0.5).sum())


# 2b. One $5,000 step lower: the fall in yields that lowers the bottom she can state (nothing is stated yet)
def bottom_raw_before(x):
    """The unrounded bottom after a parallel fall x before 1 Jan 2027, exact re-sizing (section 5(e), most_check.at_fall)."""
    left = DEP - C.completion_exact(-x)[0]
    fm = max(SHARE * left, min(left, HALF + 1.0))
    return fm * float(C.zero_per_dollar(E.J28, -x)) * (1 - H)


def bottom_raw_during(x):
    """The unrounded bottom after a parallel fall x during 2027 alone (the ten bought), plan.run as section 5."""
    r = P.run(c, margin=MARGIN, d1=-x, margin_fn=MF)
    return f(C.rule(r, -x)["bottom_raw"])


near(bottom_raw_before(0.0), 97_605, 1, "bottom raw")
near(bottom_raw_during(0.0), 97_605, 1, "bottom raw (plan.run)")
near(float(C.down(bottom_raw_before(0.01))), 85_000, 0, "1-point fall gives $85,000 (Table 3 row 6)")
steps = {}
for label, fn in (("before_jan2027", bottom_raw_before), ("during_2027_alone", bottom_raw_during)):
    s = {}
    for target in (95_000, 90_000, 85_000):
        hi = 0.03
        if (fn(hi) - target) * (fn(0.0) - target) < 0:
            s[f"stated_below_{target}"] = 100 * bisect(lambda x: fn(x) - target, 0.0, hi)
    s["stated_after_0.25pt"] = float(C.down(fn(0.0025)))
    s["stated_after_0.5pt"] = float(C.down(fn(0.005)))
    s["stated_after_1pt"] = float(C.down(fn(0.01)))
    steps[label] = s
bottom["one_step_lower"] = steps
# rises: a rise in yields before January 2028 raises it (the first $5,000 step up)
up = bisect(lambda x: bottom_raw_before(-x) - 100_000, 0.0, 0.02)
bottom["one_step_higher_rise_before_jan2027_points"] = 100 * up
out["2_bottom"] = bottom

# 3b. The top: VT's growth from its January 2028 cost to the move at which the stated top steps (8p's thresholds)
vfee = E.ASSUMPTIONS["vt_fee"]


def top_raw_vt(g):
    """The unrounded top when VT is worth g x its January 2028 cost at the move (before its fee), rates at forwards."""
    r = P.run(c, margin=MARGIN, margin_fn=MF, vt3=g)
    return f(C.rule(r)["top_raw"])


# 8p's "VT at 1.106 of cost" is VT with dividends before its fee (fall40.py: "Down 40%" = 0.6 x value before the fee)
thr = {}
for target in (115_000, 110_000, 105_000, 100_000):
    g = bisect(lambda g: top_raw_vt(g) - target, 0.0001, 2.0)
    thr[str(target)] = g - 1
near(100 * thr["115000"], 10.6, 0.05, "8p +10.6%")
near(100 * thr["110000"], -21.2, 0.05, "8p -21.2%")
topd["vt_change_from_jan2028_cost_at_the_move_for_stated_top_at_least"] = thr
out["3_top"] = topd

# ================================================================ 4. Her flexibility (register figures, re-derived)
kept, excess = f(cen["kept33"]), PAY - top
near(kept + excess, 28_682, 1, "her flexibility")
flex = {"central": kept + excess, "half_kept": kept, "above_the_top": excess,
        "rise_in_usd_building_cost_it_covers_on_the_top": (kept + excess) / top,
        "rise_it_covers_on_the_bottom": (kept + excess) / bot,
        "ten_pct_stronger_twd_on_the_top": 0.10 * top}
near(100 * flex["rise_in_usd_building_cost_it_covers_on_the_top"], 24.9, 0.05, "8q 24.9%")
vt0 = P.run(c, margin=MARGIN, margin_fn=MF, vt3=1e-9)
r0 = C.rule(vt0)
flex["vt_worthless_at_the_move"] = {"stated": [f(r0["bottom"]), f(r0["top"])], "her_flexibility": f(r0["excess"]) + f(vt0["kept33"])}
near(flex["vt_worthless_at_the_move"]["her_flexibility"], 7_365, 1, "deletion test")
out["4_flexibility"] = flex

OUT.write_text(json.dumps(out, indent=1, default=float))

k = C.fmt
print("1. Payments")
print(f"   first slice {k(first)} (standard survives a {1 - first / DEP:.1%} deposit fall); top-up {k(tail)} ({1 - tail / DEP:.1%})")
print(f"   fall before 1 Jan 2027 taking the whole deposit: standard {100 * x_std:.2f} pt, ladder {100 * x_lad:.2f} pt")
print(f"   missed deposit: 2033 short {k(E.PAYMENT - miss_fwd[2033])} at forwards; ten short {k(miss_zero)} at zero, "
      f"{k(pay['missed_deposit']['short_ten_zero_and_bill_fee'])} with the bill fee")
for key, v in costs.items():
    if key.startswith("0."):
        print(f"   cost {100 * float(key):.2f}%: short under the standard {k(v['short_standard_total'])} "
              f"{ {y: round(a) for y, a in v['short_standard_by_year'].items()} }; zero no bill fee {k(v['short_zero_no_bill_fee'])}; "
              f"needs waiting money at {100 * v['gross_rate_needed_before_bill_fee']:.3f}% a year before the bill fee "
              f"({100 * v['net_rate_needed_on_waiting_money']:.3f}% net); forwards left {k(v['left_after_2042_forwards'])}")
print(f"   largest cost covered: {100 * costs['largest_cost_covered_standard']:.3f}% (standard), "
      f"{100 * costs['largest_cost_covered_zero_no_bill_fee']:.3f}% (no bill fee)")
print("2. Bottom")
print(f"   central cover, floor alone: {100 * (1 - bot / Fz):.2f}% at zero interest, {100 * (1 - bot / Fpay):.2f}% at its modelled payout")
hb = bottom["house"]
print(f"   house cover (floor alone) zero: min {100 * hb['cover_zero_interest']['min']:.3f}% p5 {100 * hb['cover_zero_interest']['p5']:.3f}% "
      f"median {100 * hb['cover_zero_interest']['median']:.3f}%; modelled: min {100 * hb['cover_modelled_payout']['min']:.3f}% "
      f"p5 {100 * hb['cover_modelled_payout']['p5']:.3f}% median {100 * hb['cover_modelled_payout']['median']:.3f}%")
print(f"   paths below bottom at zero interest, costs 0.75% / 1%: {hb['paths_below_bottom_zero_interest_at_cost_0.0075']} / "
      f"{hb['paths_below_bottom_zero_interest_at_cost_0.0100']}")
for lab, s in steps.items():
    print(f"   one step lower ({lab}): {s}")
print(f"   one step higher: a rise of {100 * up:.2f} pt before 1 Jan 2027")
print("3. Top")
print(f"   cover {100 * (1 - top / Tz):.2f}% zero, {100 * (1 - top / PAY):.2f}% modelled; VT thresholds {({a: round(100 * b, 2) for a, b in thr.items()})}")
print("4. Flexibility")
print(f"   {k(kept + excess)}; covers a {100 * flex['rise_in_usd_building_cost_it_covers_on_the_top']:.1f}% rise on the top, "
      f"{100 * flex['rise_it_covers_on_the_bottom']:.1f}% on the bottom; 10% stronger NT$ {k(0.1 * top)}; VT worthless: "
      f"{flex['vt_worthless_at_the_move']}")
print("wrote", OUT.name)
