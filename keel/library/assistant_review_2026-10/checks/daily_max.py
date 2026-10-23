import sys, csv
from datetime import date
import numpy as np
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
J27 = date(2027,1,1); TEN = [P.yf(J27, d) for d in P.BUYABLE]
rows = list(csv.DictReader(open(sys.argv[1])))
ds = []
for r in rows:
    m, d, y = map(int, r["Date"].split("/"))
    pts = sorted((P.TENORS[k], float(v)/100) for k, v in r.items() if k in P.TENORS and v)
    c = P.Curve(pts); ds.append((date(y,m,d), sum(50000*c.df(t) for t in TEN)))
ds.sort()
ch = [((ds[i+1][1]/ds[i][1]-1)*ds[-1][1]/287, ds[i+1][0]) for i in range(len(ds)-1)]
ch.sort()
print("largest 1-day ladder-cost rises (bp-equivalent fall in yields):", [(f"{-x:.1f}bp", str(d)) for x, d in ch[-5:]][::-1])
# 5-day
ch5 = sorted(((ds[i+5][1]/ds[i][1]-1)*ds[-1][1]/287, ds[i+5][0]) for i in range(len(ds)-5))
print("largest 5-session rises:", [(f"{-x:.1f}bp", str(d)) for x, d in ch5[-3:]][::-1])
