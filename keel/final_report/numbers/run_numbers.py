"""Every figure in keel/final_report/NUMBERS.md, from one curve and one engine (Keel, Mon 9 Nov 2026). MODEL.

Run from the repo root:  python3 -I keel/final_report/numbers/run_numbers.py
Writes keel/final_report/numbers/results_2026-11-06.json and prints the register's figures (about 20 seconds).
"""
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402
import plan as P     # noqa: E402

out = {}
c = E.Curve(E.load_par())
I = E.instruments(c)
base, zero = E.Reinvest(c), E.Reinvest(c, "zero")
shift = lambda s: E.Reinvest(c, "shift", s)
DGS1 = E.ROOT / "archive/rab/data/fred/DGS1.csv"

# ---------------------------------------------------------------- C3: the ladder's cost on the 6 Nov close
units = E.size_own_rung(I, base)
out["C3"] = {
    "curve_cost_payment_dates": E.ladder_cost(c),
    "ten_instruments_with_fund_fees": E.cost(I, units),
    "ladder_duration_years": P.setup(c)["dur_l"],
    "dv01_per_bp": (E.ladder_cost(E.Curve(c.par, -0.0001)) - E.ladder_cost(E.Curve(c.par, 0.0001))) / 2,
    "rungs": {y: {"instrument": I[y].name, "units": units[y], "cost": units[y] * I[y].price} for y in E.YEARS},
}
for fall in (0.0025, 0.005, 0.01, 0.02):
    cc = E.Curve(c.par, -fall)
    out["C3"][f"cost_if_yields_fall_{int(fall*1e4)}bp_before_jan2027"] = E.cost(E.instruments(cc), E.size_own_rung(E.instruments(cc), E.Reinvest(cc)))
# the fall before 1 Jan 2027 at which completing the ladder would take the whole 2028 deposit
lo, hi = 0.0, 0.06
f01 = c.fwd(E.J27, E.J28)
for _ in range(40):
    mid = (lo + hi) / 2
    cc = E.Curve(c.par, -mid)
    need = E.cost(E.instruments(cc), E.size_own_rung(E.instruments(cc), E.Reinvest(cc))) - 300_000
    lo, hi = (mid, hi) if need * math.exp(max(f01 - mid, 0.001)) < 150_000 else (lo, mid)
out["C3"]["fall_that_uses_whole_2028_deposit_pt"] = lo * 100

# the instruments actually held (fixed units) move less with yields than the payments: the gap is reinvestment risk
def _held(cc):
    return sum(units[y] * a * cc.P(d) for y in E.YEARS for d, a, k in E.rung_flows(I[y], base))
_v = _held(c)
out["C3"]["held_ladder_duration_years"] = (_held(E.Curve(c.par, -0.0001)) - _held(E.Curve(c.par, 0.0001))) / (2 * 0.0001 * _v)
out["C3"]["held_ladder_dv01_per_bp"] = (_held(E.Curve(c.par, -0.0001)) - _held(E.Curve(c.par, 0.0001))) / 2
out["C3"]["build_order"] = "longest rungs first; any part unbought in Jan 2027 is the 2033 rung, completed Jan 2028"

# ---------------------------------------------------------------- C1: reinvestment
designs = {}
for lab, w in [("forward", base), ("minus1", shift(0.01)), ("minus2", shift(0.02)), ("minus3", shift(0.03)),
               ("zero", zero)]:
    designs[f"A_{lab}"] = (E.size_own_rung(I, w), False)
designs["B_matched_forward"] = (E.size_matched(I, base), True)
designs["B_matched_zero"] = (E.size_matched(I, zero), True)
c1 = {}
hist = {k: [] for k in designs}
starts = []
for st, m in E.history_windows(DGS1, "DGS1"):
    w = E.Reinvest(c, "hist", mult=m)
    starts.append(st)
    for k, (u, pool) in designs.items():
        hist[k].append(sum(E.PAYMENT - v for _, v in E.deliver(I, u, w, pool)))
for k, (u, pool) in designs.items():
    h = np.array(hist[k])
    c1[k] = {
        "cost": E.cost(I, u),
        "units_bought_in_jan_2027": sum(1 for y in E.YEARS if u[y] > 1),
        "short_if_rates_fall_for_good": {f"{s}pt": sum(E.PAYMENT - v for _, v in E.deliver(I, u, shift(s / 100), pool))
                                         for s in (1, 2, 3)},
        "short_if_interest_earns_nothing": sum(E.PAYMENT - v for _, v in E.deliver(I, u, zero, pool)),
        "history_windows": len(h),
        "history_share_with_any_shortfall": float((h > 1).mean()),
        "history_median_shortfall": float(np.median(h)),
        "history_1_in_20_shortfall": float(np.percentile(h, 95)),
        "history_worst_shortfall": float(h.max()),
        "history_worst_start": starts[int(h.argmax())],
    }
c1["history_first_start"], c1["history_last_start"] = starts[0], starts[-1]
# the interest the ten earn before the first payment
pre = sum(units[y] * a * base.grow(d, E.J33) for y in E.YEARS for d, a, k in E.rung_flows(I[y], base)
          if d < E.J33 and k == "coupon")
c1["interest_received_before_2033_valued_jan_2033"] = pre
out["C1"] = c1

# ---------------------------------------------------------------- C2: an iBond fund pays its net asset value, not par
c2 = {}
for y in range(2033, 2038):
    inst = I[y]
    u = units[y]
    fee_free = sum(u * a / (1 - E.ASSUMPTIONS["fund_fee"]) ** E.yf(d, E.J27) * base.grow(d, date(y, 1, 1))
                   for d, a, _ in inst.flows)
    with_fee = sum(u * a * base.grow(d, date(y, 1, 1)) for d, a, _ in inst.flows)
    wam, end = inst.cash_wait
    principal = [a for d, a, k in inst.flows if k != "coupon"][0] * u
    wait_years = (end - wam).days / 365.25
    cash_lost_if_bills_zero = principal * (base.grow(wam, end) - 1)
    c2[inst.name] = {"fee_cost_on_50k": fee_free - with_fee, "months_in_cash_before_end": wait_years * 12,
                     "lost_if_cash_earns_nothing_in_final_months": cash_lost_if_bills_zero,
                     "as_share_of_payment": cash_lost_if_bills_zero / E.PAYMENT}
out["C2"] = c2

# ---------------------------------------------------------------- C5, C6, C8: the plan from 2028
CALL = "A_minus3"
plans = {}
for lab, k in [("no_margin", "A_forward"), ("margin_minus2", "A_minus2"), ("margin_minus3", "A_minus3"),
               ("margin_zero", "A_zero")]:
    m = c1[k]["cost"] - c1["A_forward"]["cost"]
    d = P.run(c, margin=m)
    h = P.house(c, margin=m)
    hs = P.history(c, margin=m)
    plans[lab] = {
        "margin_jan2027_value": m,
        "central": {k2: float(d[k2]) for k2 in ("complete", "R", "floor", "vt28", "vt31", "moved", "top", "kept33",
                                                 "total", "all_t")},
        "floor_share_of_2028_deposit": float(E.ASSUMPTIONS["floor_share"] * d["R"] / 150_000),
        "house": {k2: P.pct(h[k2]) for k2 in ("floor", "top", "moved", "kept33", "total", "all_t")},
        "house_share_total_below_all_treasury": float((h["total"] < h["all_t"]).mean()),
        "house_share_top_below_all_treasury": float((h["top"] < h["all_t"]).mean()),
        "house_payments_full": float(h["payments_full"].mean()),
        "history": {k2: P.pct(hs[k2]) for k2 in ("top", "moved", "kept33", "total")},
        "history_lowest_top": [float(hs["top"].min()), hs["starts"][int(hs["top"].argmin())]],
        "history_windows": len(hs["starts"]),
    }
m3 = plans["margin_minus3"]["margin_jan2027_value"]
plans["vt_growth_sensitivity_central"] = {f"{g:.3f}": {k2: float(P.run(c, margin=m3, vt3=(1 + g) ** 3, vt2=(1 + g) ** 2)[k2])
                                                       for k2 in ("top", "kept33", "total")} for g in (0.04, 0.06, 0.075, 0.09, 0.10)}
plans["deletion_test_vt_to_zero"] = float(P.run(c, margin=m3, vt3=0.0, vt2=0.0)["top"])
plans["margin_handed_back_if_rates_hold_jan2033_value"] = m3 / c.P(E.J33)
plans["missed_deposit_2033_payment_short"] = (c1["A_forward"]["cost"] - 300_000) / c.P(E.J33)
out["plan"] = plans

# C5: after the 2031 move both ends sit in a Treasury fund maturing late 2032; what can still move them
inst = I[2033]
wam, end = inst.cash_wait
out["C5"] = {
    "move_date_modelled": "1 Jan 2031",
    "after_move_worst_case_if_rates_go_to_zero": "both ends lose only the interest on the fund's final months in cash"
                                                  " and on its last distributions",
    "floor_cash_months": (end - wam).days / 365.25 * 12,
}

# C6: a smaller or missed 2028 deposit, with or without a fall in yields before 1 Jan 2027
c6 = {}
for fall in (0.0, 0.005, 0.01, 0.02):
    row = {}
    for dep in (150_000, 112_500, 75_000, 37_500, 0):
        d = P.run(c, margin=plans["margin_minus3"]["margin_jan2027_value"], deposit=dep, d0=-fall)
        dz = P.run(c, margin=0.0, deposit=dep, d0=-fall)
        row[str(dep)] = {"ladder_complete": bool(dz["payments_full"]), "margin_complete": bool(d["payments_full"]),
                         "completion_needed_no_margin": float(dz["complete"]), "floor": float(d["floor"]),
                         "top": float(d["top"])}
    # smallest deposit that still completes the ladder (no margin) and the ladder plus margin
    need0 = float(P.run(c, margin=0.0, deposit=0, d0=-fall)["complete"])
    needm = float(P.run(c, margin=plans["margin_minus3"]["margin_jan2027_value"], deposit=0, d0=-fall)["complete"])
    row["smallest_deposit_ladder"] = need0
    row["smallest_deposit_ladder_and_margin"] = needm
    c6[f"fall_{int(fall*1e4)}bp"] = row
out["C6"] = c6
out["stamp"] = {"curve": "US Treasury par yield curve, 6 Nov 2026 close", "valuation": "forward to 1 Jan 2027",
                "assumptions": {k: v for k, v in E.ASSUMPTIONS.items()}, "call": CALL}

(HERE / "results_2026-11-06.json").write_text(json.dumps(out, indent=1, default=str))


def k(x):
    return f"${x/1000:,.1f}k"


print("C3 ladder:", f"curve ${out['C3']['curve_cost_payment_dates']:,.0f}", f"ten with fees ${out['C3']['ten_instruments_with_fund_fees']:,.0f}",
      f"dur {out['C3']['ladder_duration_years']:.2f}y DV01 ${out['C3']['dv01_per_bp']:,.0f}",
      {kk: round(v) for kk, v in out["C3"].items() if kk.startswith("cost_if")},
      f"whole-deposit fall {out['C3']['fall_that_uses_whole_2028_deposit_pt']:.2f}pt",
      f"held dur {out['C3']['held_ladder_duration_years']:.2f}y DV01 ${out['C3']['held_ladder_dv01_per_bp']:,.0f}")
for kk, v in c1.items():
    if isinstance(v, dict):
        print(f"C1 {kk:18s} cost ${v['cost']:,.0f} bought {v['units_bought_in_jan_2027']} | -1/-2/-3pt "
              f"{[round(x) for x in v['short_if_rates_fall_for_good'].values()]} zero {v['short_if_interest_earns_nothing']:,.0f} | hist "
              f"{v['history_share_with_any_shortfall']:.1%} med {v['history_median_shortfall']:,.0f} 1in20 {v['history_1_in_20_shortfall']:,.0f} "
              f"worst {v['history_worst_shortfall']:,.0f} ({v['history_worst_start']})")
print("C1 interest before 2033 (Jan 2033 value):", k(pre), "| windows", c1["history_first_start"], "to", c1["history_last_start"])
for kk, v in c2.items():
    print("C2", kk, f"fee ${v['fee_cost_on_50k']:,.0f}", f"cash {v['months_in_cash_before_end']:.1f} months",
          f"lost if cash earns 0: ${v['lost_if_cash_earns_nothing_in_final_months']:,.0f} ({v['as_share_of_payment']:.1%})")
for kk, v in plans.items():
    if not isinstance(v, dict) or "central" not in v:
        print("PLAN", kk, v if not isinstance(v, dict) else {g: {q: round(x) for q, x in d.items()} for g, d in v.items()})
        continue
    print(f"PLAN {kk:14s} margin {k(v['margin_jan2027_value'])} central floor {k(v['central']['floor'])} top {k(v['central']['top'])} "
          f"kept {k(v['central']['kept33'])} allT {k(v['central']['all_t'])} | house floor {[round(x/1000) for x in v['house']['floor']]} "
          f"top {[round(x/1000) for x in v['house']['top']]} moved {[round(x/1000) for x in v['house']['moved']]} "
          f"kept {[round(x/1000) for x in v['house']['kept33']]} total {[round(x/1000) for x in v['house']['total']]} "
          f"allT {[round(x/1000) for x in v['house']['all_t']]} P(total<allT) {v['house_share_total_below_all_treasury']:.0%} "
          f"P(top<allT) {v['house_share_top_below_all_treasury']:.0%} | hist top {[round(x/1000) for x in v['history']['top']]} "
          f"total {[round(x/1000) for x in v['history']['total']]} lowest top {k(v['history_lowest_top'][0])} {v['history_lowest_top'][1]}")
for kk, v in c6.items():
    print("C6", kk, "smallest deposit: ladder", k(v["smallest_deposit_ladder"]), "ladder+margin", k(v["smallest_deposit_ladder_and_margin"]),
          {d: (v[d]["ladder_complete"], round(v[d]["floor"] / 1000), round(v[d]["top"] / 1000)) for d in ("150000", "112500", "75000", "37500", "0")})
