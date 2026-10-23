"""Ladder cost on every Treasury par curve since 2000 (rescued by WS1-inventory, 2026-09-30).

Why this file exists: the IPS Report says the ten payments "would have cost about $460,000" at 2020 yields, that
the plan was "tested on every Treasury curve since 2000", and the run brief says the 28 Sep 2026 cost is the
cheapest since 2002. The only code behind those claims was an uncommitted scratch script from an earlier session
(copied unchanged as `r4_hist_original.py`, which reads a /tmp path). This version reads the rescued curve files
in `rab/data/treasury_par_2000_2026/` and adds one check the original did not run: on which days would the 2027
gap be larger than the 2028 deposit, i.e. leave part of a payment unfunded (the IPS sentence).

Method: identical to `research/insight_v1/scripts/D1_purchase_rule.py` (imported unchanged): par = semiannual BEY,
linear interpolation on a 0.5y grid, bootstrap, log-linear discount factors, days/365.25, Nov-15 rungs 2032-2041.
Each historical day is priced with the SAME time-to-maturity as on 28 Sep 2026 ("same-ttm"), as spot and as the
forward to the equivalent of 1 Jan 2027. The deposit check values $150,000 one year after the forward date on that
day's curve (ASSUMPTION: the 2028 deposit arrives on time and in full).

Data: 27 yearly CSVs, home.treasury.gov Daily Treasury Par Yield Curve Rates, 2000-2026 (to 28 Sep 2026); each file
byte-identical to a fresh download on 2026-09-30 00:20 AEST (VERIFIED-PRIMARY). URL pattern in the data README.

Run from the repo root (rab-kit):  /Users/ray/Research/rab-ws/.venv/bin/python rab/rescued/ladder_history_2000_2026.py
MODEL prices, not STRIPS quotes. Reconcile with WS3/WS4 before any number is published.
"""
import glob
import importlib.util
import statistics as st
from datetime import date, timedelta

spec = importlib.util.spec_from_file_location("d1", "research/insight_v1/scripts/D1_purchase_rule.py")
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

rows = []
for f in sorted(glob.glob("rab/data/treasury_par_2000_2026/*.csv")):
    rows += d1.load(f)
rows = sorted({r["_date"]: r for r in rows}.values(), key=lambda r: r["_date"])

T0 = date(2026, 9, 28)
offs_spot = [date(y - 1, 11, 15) - T0 for y in d1.YEARS]
offs_fwd = [date(y - 1, 11, 15) - d1.ANCHOR for y in d1.YEARS]
res = []
for r in rows:
    try:
        f = d1.curve(r)
    except Exception:  # a day with missing tenors the interpolation cannot use
        continue
    d = r["_date"]
    a = d + (d1.ANCHOR - T0)                       # the day's equivalent of 1 Jan 2027
    spot = sum(50_000 * f(d + o) for o in offs_spot)
    fwd = sum(50_000 * f(a + o) for o in offs_fwd) / f(a)
    dep = 150_000 * f(a + timedelta(days=365)) / f(a)  # 2028 deposit in 2027 dollars on that curve
    res.append((d, spot, fwd, max(0.0, fwd - 300_000 - dep)))

print(f"days priced: {len(res)} ({res[0][0]} to {res[-1][0]})")
last = res[-1]
print(f"28 Sep 2026: spot ${last[1]:,.0f}; forward to 1 Jan 2027 ${last[2]:,.0f}")
for lab, i in (("spot", 1), ("forward", 2)):
    y20 = [x[i] for x in res if x[0].year == 2020]
    mx = max(res, key=lambda x: x[i])
    cheaper = [x[0] for x in res if x[i] <= last[i] and x[0] < T0]
    print(f"{lab:8s}: <= $300k on {100 * sum(x[i] <= 300_000 for x in res) / len(res):.1f}% of days; "
          f"2020 median ${st.median(y20):,.0f} (min ${min(y20):,.0f}, max ${max(y20):,.0f}); "
          f"max ${mx[i]:,.0f} on {mx[0]}; last day cheaper than 28 Sep 2026: {cheaper[-1] if cheaper else None}")
unf = [x for x in res if x[3] > 0]
print(f"days where the gap exceeds the 2028 deposit (part of a payment unfunded): {len(unf)} of {len(res)}")
if unf:
    yrs = sorted({x[0].year for x in unf})
    worst = max(unf, key=lambda x: x[3])
    print(f"  years: {yrs}; worst {worst[0]}: ${worst[3]:,.0f} unfunded (2027 dollars)")
