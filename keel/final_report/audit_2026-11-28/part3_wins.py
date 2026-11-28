"""Part 3: Table 1's arithmetic, the bonds' accrued interest, and how the $300,000 WInS book compresses Laura's
two-deposit plan. Fills from competition/wins/2026-10-23_snapshot.md (quantity x price paid). MODEL where marked."""
import json
from datetime import date

from audit_core import *

FILLS = {"IBTM": (4503, 21.65), "IBTO": (1024, 22.86), "IBTP": (927, 23.90), "IBTQ": (894, 23.46), "IBTR": (853, 23.24),
         "B2037": (20, 960.190), "B2038": (20, 930.763), "B2039": (18, 900.053), "B2040": (18, 877.240),
         "B2041": (20, 749.550), "VT": (167, 158.83)}
CASH, COMMISSIONS = 3513.79, 6 * 25 + 5 * 10
cost = {k: round(q * p, 2) for k, (q, p) in FILLS.items()}
tsy = round(sum(v for k, v in cost.items() if k != "VT"), 2)
resid = round(300000 - sum(cost.values()) - CASH, 2)
out = {"table1": {"costs": cost, "treasury_subtotal": tsy, "treasury_weight_pct": round(tsy / 3000, 2),
                  "vt_weight_pct": round(cost["VT"] / 3000, 2), "cash_weight_pct": round(CASH / 3000, 2),
                  "residual_after_cash": resid, "commissions": COMMISSIONS,
                  "residual_less_commissions": round(resid - COMMISSIONS, 2)}}

# standard Treasury accrued interest at settlement (actual/actual, semiannual)
acc = {}
for settle in (date(2026, 10, 7), date(2026, 10, 8)):
    tot = 0.0
    for (k, (q, _)), y in zip([(k, FILLS[k]) for k in ("B2037", "B2038", "B2039", "B2040", "B2041")], range(2038, 2043)):
        tot += BONDS[y].accrued(settle, q * 1000)
    acc[str(settle)] = round(tot, 2)
out["standard_accrued_interest"] = acc

# the WInS book against the plan. IBTM's 4,503 shares hold the 2033 rung and the floor stand-in: the team's split
# (3,361 shares as floor stand-in, attribution pack of 20 Oct, recorded in the register's assumptions) is used only to
# separate the two jobs.
cv = bootstrap_pchip()
fl = {y: instrument_flows(y, cv, J27, "fwd") for y in YEARS}
rung = {y: PAY / fv_at(fl[y], date(y, 1, 1), cv, "fwd") for y in YEARS}
book_rung = {2033: (4503 - 3361) * 21.65, 2034: cost["IBTO"], 2035: cost["IBTP"], 2036: cost["IBTQ"], 2037: cost["IBTR"],
             2038: cost["B2037"], 2039: cost["B2038"], 2040: cost["B2039"], 2041: cost["B2040"], 2042: cost["B2041"]}
out["book_share_of_each_full_rung"] = {y: round(book_rung[y] / rung[y], 3) for y in YEARS}
book_ladder, book_floor, book_vt = sum(book_rung.values()), 3361 * 21.65, cost["VT"]
# the plan on 1 Jan 2028 (forward values): the ten (bought 2027, carried at forwards), top-up and extra Treasuries,
# the floor, VT. Uses the draft's sizes for the 2028 money.
ten28 = sum(rung.values()) / cv.P(J27, J28)
plan28 = {"operating (ten + $39,162)": ten28 - (sum(rung.values()) - 300000) / cv.P(J27, J28) + 39162,
          "floor (IBTM)": 81244.0, "VT": 29594.0}
tot28 = sum(plan28.values())
out["plan_jan2028_weights_pct"] = {k: round(100 * v / tot28, 1) for k, v in plan28.items()}
out["plan_jan2028_total"] = round(tot28)
out["book_weights_pct"] = {"operating (ten rungs)": round(100 * book_ladder / 300000, 1),
                           "floor stand-in (IBTM)": round(100 * book_floor / 300000, 1),
                           "VT": round(100 * book_vt / 300000, 1), "cash and costs": round(100 * (CASH + resid) / 300000, 1)}
out["book_times_1.5"] = {"operating": round(book_ladder * 1.5), "floor": round(book_floor * 1.5), "VT": round(book_vt * 1.5)}
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / "results_part3.json", "w"), indent=1)
