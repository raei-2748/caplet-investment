"""Historical frequency that the constant-tenor ladder PV rises by more than the current room over ~80 calendar days.
Ladder = $50k at tenors (BUYABLE date - 1 Jan 2027). Cost on 1 Jan 2027 under 'curve then' = PV at those tenors.
Today's cost (yields-unchanged convention) = same PV on the latest curve. So P(cost>300k) = P(ratio > 300k/PV_today)."""
import sys, csv, glob, math
from datetime import date, timedelta
import numpy as np
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
hist_dir, latest_csv = sys.argv[1], sys.argv[2]
J27 = date(2027, 1, 1)
TEN = [P.yf(J27, d) for d in P.BUYABLE]
curves = {}
for f in sorted(glob.glob(hist_dir + "/20*.csv")) + [latest_csv]:
    for r in csv.DictReader(open(f)):
        m, d, y = map(int, r["Date"].split("/"))
        pts = []
        for k, v in r.items():
            if k in P.TENORS and v not in (None, "", "N/A"):
                pts.append((P.TENORS[k], float(v) / 100))
        if len(pts) >= 6 and any(t >= 10 for t, _ in pts): curves[date(y, m, d)] = sorted(pts)
ds = sorted(curves)
pv = {}
for d in ds:
    c = P.Curve(curves[d])
    pv[d] = sum(50_000 * c.df(t) for t in TEN)
    # dv01 per bp
dlast = ds[-1]
c0 = P.Curve(curves[dlast]); cu = P.Curve(curves[dlast], 0.0001); cd = P.Curve(curves[dlast], -0.0001)
pv0 = pv[dlast]
dv01 = (sum(50_000 * cd.df(t) for t in TEN) - sum(50_000 * cu.df(t) for t in TEN)) / 2
need = 300_000 / pv0 - 1
H = (J27 - dlast).days
print(f"latest {dlast}: constant-tenor cost {pv0:,.0f}, dv01 {dv01:,.0f}/bp, horizon {H} days, rise needed {need*100:.2f}%")
import bisect
def changes(start, end):
    out = []
    for i, d in enumerate(ds):
        if d < start or d > end: continue
        tgt = d + timedelta(days=H)
        j = bisect.bisect_right(ds, tgt) - 1
        if ds[j] <= d or (tgt - ds[j]).days > 5 or ds[j] > end: continue
        out.append(pv[ds[j]] / pv[d] - 1)
    return np.array(out)
for lab, a, b in (("2000-2026", date(2000,1,1), dlast), ("2010-2026", date(2010,1,1), dlast),
                  ("2022-2026", date(2022,1,1), dlast), ("2023-2026", date(2023,1,1), dlast), ("2026 only", date(2026,1,1), dlast)):
    x = changes(a, b)
    if len(x) == 0: continue
    sd = x.std()
    print(f"{lab}: n={len(x)} overlapping windows, sd of {H}-day % change {sd*100:.2f}% "
          f"(= {sd*pv0/dv01:.0f}bp parallel-equivalent, {sd*pv0/dv01*math.sqrt(365.25/H):.0f}bp/yr), "
          f"freq(rise>{need*100:.2f}%) = {np.mean(x > need)*100:.1f}%")
# daily vol in 2026 of the ladder cost (as parallel-bp equivalent)
d26 = [d for d in ds if d.year == 2026]
r = np.array([pv[d26[i+1]]/pv[d26[i]] - 1 for i in range(len(d26)-1)])
print(f"2026 daily: n={len(r)}, sd {r.std()*100:.3f}% = {r.std()*pv0/dv01:.2f}bp/day -> {r.std()*pv0/dv01*math.sqrt(252):.0f}bp/yr")
t10 = np.array([dict(curves[d])[10] for d in d26]); dt10 = np.diff(t10) * 1e4
print(f"2026 10y par daily change sd {dt10.std():.2f}bp (n={len(dt10)}) -> {dt10.std()*math.sqrt(252):.0f}bp/yr")
