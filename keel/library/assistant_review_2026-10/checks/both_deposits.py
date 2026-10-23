import sys
from datetime import date
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
path = sys.argv[1]; d0 = date(2026,10,13); J27, J28 = date(2027,1,1), date(2028,1,2)
pts = P.load_curve(path, "10/13/2026")
def gap(s):
    c = P.Curve(pts, s)
    cost27 = P.ladder(c, d0, P.BUYABLE) / c.df(P.yf(d0, J27))
    avail = 300000 + 150000 * c.df(P.yf(d0, J28)) / c.df(P.yf(d0, J27))
    return cost27 - avail
lo, hi = -0.06, 0.0
for _ in range(80):
    mid = (lo+hi)/2
    lo, hi = (lo, mid) if gap(mid) < 0 else (mid, hi)
print(f"parallel fall at which BOTH deposits no longer cover the ten payments (buyable, forward): {-(lo+hi)/2*1e4:.0f}bp")
for s in (-0.005, -0.01, -0.015):
    c = P.Curve(pts, s); cost27 = P.ladder(c, d0, P.BUYABLE)/c.df(P.yf(d0,J27))
    g = max(0, cost27-300000); g28 = g * c.df(P.yf(d0,J27))/c.df(P.yf(d0,J28)); rem = 150000-g28
    y5 = dict(pts)[5] + s; fc = rem/(1+y5)**5
    print(f"fall {-s*1e4:.0f}bp: ladder {cost27:,.0f}; top-up in 2028 {g28:,.0f}; floor face {rem:,.0f}; floor cost {fc:,.0f}; stock {rem-fc:,.0f}")
