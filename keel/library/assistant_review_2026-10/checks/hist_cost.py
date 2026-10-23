# Cost of the ten payments (6..15 years ahead, Nov-15 basis ~ 6.13..15.13 yrs) if Laura's Jan-2027 purchase had
# faced each historical day's par curve. Independent check of the IPS claim "2020-level yields ... about $460,000".
import csv, glob, statistics
import numpy as np
import indep_pricer as ip
res = {}
for path in sorted(glob.glob('../../../../archive/rab/data/treasury_par_2000_2026/20*.csv')):
    yr = path[-8:-4]
    vals = []
    with open(path) as f:
        for row in csv.DictReader(f):
            pts = sorted((ip.TENORS[k], float(v)/100) for k, v in row.items() if k in ip.TENORS and v not in ('', 'N/A'))
            ts = [t for t, _ in pts]
            if 30 not in ts and 20 not in ts: continue
            if not any(t >= 10 for t in ts): continue
            try:
                c = ip.Curve(pts)
            except Exception:
                continue
            # payments on 1 Jan 2033..2042 funded on 15 Nov of prior year; valuation 1 Jan 2027 => t = 5.87..14.87
            cost = sum(50_000 * c.df(y - 2027 - 1.5/12 + 0.0) for y in range(2033, 2043))
            vals.append(cost)
    if vals:
        res[yr] = (statistics.median(vals), min(vals), max(vals), len(vals), sum(v <= 300_000 for v in vals))
for yr, (med, lo, hi, n, le) in res.items():
    print(f"{yr}: median ${med:,.0f}  min ${lo:,.0f}  max ${hi:,.0f}  days {n:3d}  days <= $300k: {le}")
