"""What returns to Laura, checked a second way (Keel numbers owner, Tue 10 Nov 2026 evening, Sydney). MODEL.

Run from the repo root:  python3 -I keel/final_report/numbers/returns_check.py
Reads results_reserve_2026-11-10.json, results_range_rule_2026-11-10.json and results_joint_stress_2026-11-10.json
(run reserve, range_rule and joint_stress first); writes results_returns_2026-11-10.json. Takes a second.

Why: NUMBERS 8k reports what comes back to Laura at today's forward rates: the backstop's money left after the 2042
payment, the excess the cap sends back, and the half kept. joint_stress.py adds them up from its own ledger. A figure
that is part of a promise is tested by a calculation different from the one that sized it, so this script gets the
total twice more:

  Route 1, other files: the backstop's 1 Jan 2033 value from reserve.py (its holdings and waiting cash on that day, a
           different sum from joint_stress's ledger run to 2042 and brought back), the excess and the half kept from
           range_rule.py's central row (plan.run and the rule, rounded to the dollar there).
  Route 2, value conservation at today's forwards, with no ledger, no reserve and no plan.run: every Treasury dollar
           is bought at a forward price and earns forward rates, so in 1 Jan 2033 money
              what returns = the two deposits grown at forwards
                           + what VT earns above forwards (net of VT's 0.06% fee)
                           - the iBond funds' 0.07% fee (rungs, backstop, floor, moved half)
                           - the ten payments' forward value - the contribution (15 Dec 2032, carried 17 days).
           Inputs: the curve (engine.Curve), the instruments' cash flows (engine.instruments: for the fee only), the
           design's units and cost (results_reserve), the stated top (results_range_rule), VT at 7.5% (register).
           The completion and the split of the 2028 money are recomputed here from the IPS's order and Keel's reading
           of "most" (NUMBERS 0 and 4), not read from plan.run.
"""
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402

c = E.Curve(E.load_par())
I = E.instruments(c)
P = c.P
J27, J28, J31, J33 = E.J27, E.J28, E.J31, E.J33
END = date(2032, 12, 15)
FEE, VFEE = E.ASSUMPTIONS["fund_fee"], E.ASSUMPTIONS["vt_fee"]
G_VT = 1 + E.ASSUMPTIONS["eq_growth"]

R = json.load(open(HERE / "results_reserve_2026-11-10.json"))
RR = json.load(open(HERE / "results_range_rule_2026-11-10.json"))
JS = json.load(open(HERE / "results_joint_stress_2026-11-10.json"))
assert R["stamp"]["design"] == RR["stamp"]["design"] == JS["stamp"]["design"] == "H_plain"
cen = RR["central"]["holdings"]
fwd_js = JS["returns_to_laura"]["forwards"]
k33 = lambda d: P(d) / P(J33)          # $1 on date d in 1 Jan 2033 money at today's forwards (growth or discount)

# ---------------------------------------------------------------- route 1: other files
r1 = {"backstop_jan2033_from_reserve_composition": R["margin_value_1jan2033_at_forwards"],
      "backstop_jan2033_from_reserve_ledger_run_to_2042": R["base_left_after_2042_value_jan2033"],
      "backstop_jan2033_from_escrow_release_schedule": R["release_if_forwards_hold"]["value_jan2033"],
      "excess_from_range_rule_dec2032": cen["excess"], "half_kept_from_range_rule_jan2033": cen["kept"]}
r1["total_excess_at_face"] = r1["backstop_jan2033_from_reserve_composition"] + cen["excess"] + cen["kept"]

# ---------------------------------------------------------------- route 2: value conservation at forwards
units = {}
for row in R["composition_1jan2033_base"]:
    if "payment" in row:
        units[row["payment"]] = units.get(row["payment"], 0.0) + row["units_jan2027"]
cost27 = sum(u * I[y].price for y, u in units.items())
# the iBond funds' fee on the rungs and the backstop: price 1.0 against the forward value of the fee-reduced flows
# (the cash inside a fund in its last months earns forwards, so nothing else is lost at forwards)
fee27 = sum(u * (I[y].price - sum(a * P(d) for d, a, _ in I[y].flows)) for y, u in units.items() if y in E.FUNDS)
# the 2028 money, recomputed from the IPS's order: completion = (cost - $300,000) carried a year; "most" (NUMBERS 0)
complete28 = (cost27 - 300_000.0) / P(J28)
left28 = 150_000.0 - complete28
floor_money = max(0.733 * left28, min(left28, 150_000.0 / 2 + 1.0))
vt28 = left28 - floor_money
tauF, tauM = E.yf(END, J28), E.yf(END, J31)
floor_fee_end = floor_money * P(J28) / P(END) * (1 - (1 - FEE) ** tauF)
vt31 = vt28 * (G_VT * (1 - VFEE)) ** 3
moved_fee_end = vt31 / 2 * P(J31) / P(END) * (1 - (1 - FEE) ** tauM)
kept33 = vt31 / 2 * (G_VT * (1 - VFEE)) ** 2
vt_premium33 = vt31 / 2 * k33(J31) + kept33 - vt28 * k33(J28)      # VT's value above forward growth, in 2033 money
deposits33 = 300_000.0 * k33(J27) + 150_000.0 * k33(J28)
fees33 = fee27 * k33(J27) + (floor_fee_end + moved_fee_end) * k33(END)
pay33 = sum(E.PAYMENT * k33(date(y, 1, 1)) for y in E.YEARS)
contribution = cen["gift"]                                           # the stated top, the cap, centrally $115,000
contr33 = contribution * k33(END)
returns33 = deposits33 + vt_premium33 - fees33 - pay33 - contr33
r2 = {"deposits_grown_jan2033": deposits33, "vt_premium_jan2033": vt_premium33, "fees_jan2033": fees33,
      "fee_on_rungs_and_backstop_jan2027": fee27, "fee_floor_and_moved_dec2032": floor_fee_end + moved_fee_end,
      "payments_value_jan2033": pay33, "contribution_jan2033": contr33, "returns_jan2033": returns33,
      "returns_in_jan2027_money": returns33 * P(J33),
      "recomputed": {"cost_jan2027": cost27, "completion_jan2028": complete28, "left_jan2028": left28,
                     "floor_money": floor_money, "vt_bought": vt28, "half_kept_jan2033": kept33},
      "carry_15dec2032_to_1jan2033": k33(END)}
# the shares of all the money (1 Jan 2033 money at forwards; the same in any money year at forwards)
allm = pay33 + contr33 + returns33
r2["shares"] = {"all_money_jan2033": allm, "promised": (pay33 + contr33) / allm, "payments": pay33 / allm,
                "contribution": contr33 / allm, "returned": returns33 / allm,
                "promised_over_deposits_grown": (pay33 + contr33) / deposits33,
                "returned_over_deposits_grown": returns33 / deposits33,
                "vt_premium_less_fees_over_deposits_grown": (vt_premium33 - fees33) / deposits33}
# the same split, part by part, using route 1's parts (for the table): each part in 1 Jan 2033 money
parts33 = {"backstop": r1["backstop_jan2033_from_reserve_composition"], "excess": cen["excess"] * k33(END),
           "half_kept": cen["kept"]}
r2["parts_route1_jan2033"] = parts33

checks = {
    "route1_total_excess_at_face_minus_joint_stress": r1["total_excess_at_face"] - fwd_js["total_excess_at_face"],
    "route1_backstop_composition_minus_ledger": (r1["backstop_jan2033_from_reserve_composition"]
                                                  - r1["backstop_jan2033_from_reserve_ledger_run_to_2042"]),
    "route2_minus_joint_stress_total_jan2033": returns33 - fwd_js["total_jan2033"],
    "route2_minus_route1_total_jan2033": returns33 - sum(parts33.values()),
    "route2_floor_money_minus_range_rule": floor_money - cen["floor_money"],
    "route2_half_kept_minus_range_rule": kept33 - cen["kept"],
    "route2_cost_minus_reserve_file": cost27 - R["ladder_cost_jan2027"],
    "joint_stress_share_returned_minus_route2": fwd_js["share_returned"] - r2["shares"]["returned"],
}
out = {"stamp": {"curve": E.CURVE_DAY, "run": "Tue 10 Nov 2026 evening (Sydney)", "design": "H_plain", "status": "MODEL"},
       "route1_other_files": r1, "route2_value_conservation": r2, "joint_stress_forwards": fwd_js, "checks": checks}
(HERE / "results_returns_2026-11-10.json").write_text(json.dumps(out, indent=1))

f = lambda x: f"${x:,.2f}"
print("route 1 (reserve + range_rule):", {a: f(b) for a, b in r1.items()})
print("route 2 (value conservation):", {a: (f(b) if isinstance(b, float) else b) for a, b in r2.items()
                                        if not isinstance(b, dict)})
print("route 2 recomputed:", {a: f(b) for a, b in r2["recomputed"].items()})
print("shares:", {a: (f"{b:.4%}" if b < 2 else f(b)) for a, b in r2["shares"].items()})
print("joint_stress forwards total (face / 1 Jan 2033):", f(fwd_js["total_excess_at_face"]), f(fwd_js["total_jan2033"]))
print("checks:", {a: round(b, 4) for a, b in checks.items()})
