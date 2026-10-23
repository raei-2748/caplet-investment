import sys, csv
from datetime import date
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
path = sys.argv[1]
rows = list(csv.DictReader(open(path)))
days = []
for r in rows:
    m, d, y = map(int, r["Date"].split("/"))
    dd = date(y, m, d)
    if dd >= date(2026, 9, 22):
        days.append((dd, r["Date"]))
days.sort()
J27 = date(2027, 1, 1)
def fwd(pts, d0, dates, shift=0.0):
    c = P.Curve(pts, shift)
    return P.ladder(c, d0, dates) / c.df(P.yf(d0, J27))
def be(pts, d0, dates):
    lo, hi = -0.03, 0.01
    for _ in range(80):
        mid = (lo + hi) / 2
        v = fwd(pts, d0, dates, mid)
        lo, hi = (lo, mid) if v < 300_000 else (mid, hi)
    return -(lo + hi) / 2 * 1e4
def dv01(pts, d0, dates):
    return (fwd(pts, d0, dates, -0.0001) - fwd(pts, d0, dates, 0.0001)) / 2
print("date,basis,fwd_cost,room,breakeven_bp,dv01_per_bp,par1y,par2y,par5y,par10y,par20y,par30y")
for dd, s in days:
    pts = P.load_curve(path, s)
    py = dict(pts)
    for name, dates in (("buyable", P.BUYABLE), ("nov15", P.NOV15), ("jan1", P.PAYS)):
        f = fwd(pts, dd, dates)
        print(f"{dd},{name},{f:.0f},{300000-f:.0f},{be(pts, dd, dates):.1f},{dv01(pts, dd, dates):.0f},"
              f"{py[1]*100:.2f},{py[2]*100:.2f},{py[5]*100:.2f},{py[10]*100:.2f},{py[20]*100:.2f},{py[30]*100:.2f}")
