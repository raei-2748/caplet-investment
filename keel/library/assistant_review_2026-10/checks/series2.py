"""Both conventions: forward (forwards realised) and constant-curve (yields unchanged to 1 Jan 2027)."""
import sys, csv
from datetime import date
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
path = sys.argv[1]
rows = list(csv.DictReader(open(path)))
days = sorted((date(int(r["Date"][6:]), int(r["Date"][:2]), int(r["Date"][3:5])), r["Date"]) for r in rows)
days = [x for x in days if x[0] >= date(2026, 9, 22)]
J27 = date(2027, 1, 1)
def fwd(pts, d0, dates, s=0.0):
    c = P.Curve(pts, s); return P.ladder(c, d0, dates) / c.df(P.yf(d0, J27))
def unch(pts, d0, dates, s=0.0):
    c = P.Curve(pts, s); return P.ladder(c, J27, dates)   # today's curve applied on 1 Jan 2027
def be(fn, pts, d0, dates):
    lo, hi = -0.03, 0.01
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if fn(pts, d0, dates, mid) < 300_000 else (mid, hi)
    return -(lo + hi) / 2 * 1e4
print("date,basis,fwd_cost,fwd_room,fwd_be,unch_cost,unch_room,unch_be")
for dd, s in days:
    pts = P.load_curve(path, s)
    for name, dates in (("buyable", P.BUYABLE), ("nov15", P.NOV15)):
        f = fwd(pts, dd, dates); u = unch(pts, dd, dates)
        print(f"{dd},{name},{f:.0f},{300000-f:.0f},{be(fwd,pts,dd,dates):.1f},{u:.0f},{300000-u:.0f},{be(unch,pts,dd,dates):.1f}")
