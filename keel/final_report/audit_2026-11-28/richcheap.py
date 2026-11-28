"""Part 1c: are the funds' notes priced fairly by a par-curve model? Vendor prices on 25 Nov 2026 (ishares.com
holdings files) against the audit's curve built from the 25 Nov 2026 treasury.gov par curve. MODEL."""
import csv, json
import audit_core as A
from datetime import date
PAR25 = {1/12: 4.27, 1.5/12: 4.27, 2/12: 4.30, 3/12: 4.34, 4/12: 4.37, 6/12: 4.44, 1: 4.56, 2: 4.61, 3: 4.64,
         5: 4.65, 7: 4.74, 10: 4.85, 20: 5.28, 30: 5.24}
A.VAL = date(2026, 11, 25)
cv = A.bootstrap_pchip(PAR25)
out = {}
for r in csv.DictReader(open(A.HERE / "data/ibonds_holdings.csv")):
    if r["cusip"] == "CASH" or r["asof"] != "2026-11-25": continue
    c = float(r["coupon"]); c = {4.13: 4.125, 2.88: 2.875, 1.88: 1.875, 3.88: 3.875, 4.38: 4.375, 4.63: 4.625}.get(c, c)
    b = A.Bond(r["cusip"], c, date.fromisoformat(r["maturity"]))
    settle = date(2026, 11, 26)
    clean_model = (b.dirty(cv, A.VAL) - b.accrued(settle)) * 100
    out.setdefault(r["fund"], []).append(round(float(r["price"]) - clean_model, 3))
summ = {f: {"mean_vendor_minus_model_per_100": round(sum(v)/len(v), 3), "min": min(v), "max": max(v)} for f, v in out.items()}
print(json.dumps(summ, indent=1)); json.dump(summ, open(A.HERE / "results_richcheap.json", "w"), indent=1)
