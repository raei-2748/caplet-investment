import sys, csv
from datetime import date
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
J27 = date(2027,1,1)
rows = list(csv.DictReader(open(sys.argv[1])))
n = 0; over_f = []; over_u = []
for r in rows:
    m, d, y = map(int, r["Date"].split("/")); d0 = date(y,m,d)
    pts = sorted((P.TENORS[k], float(v)/100) for k, v in r.items() if k in P.TENORS and v)
    c = P.Curve(pts); n += 1
    f = P.ladder(c, d0, P.BUYABLE)/c.df(P.yf(d0, J27)); u = P.ladder(c, J27, P.BUYABLE)
    if f > 300000: over_f.append(d0)
    if u > 300000: over_u.append(d0)
print(f"2026 sessions {n}: buyable forward > $300k on {len(over_f)} (last {max(over_f)}); yields-unchanged > $300k on {len(over_u)} (last {max(over_u)})")
