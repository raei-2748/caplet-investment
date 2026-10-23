import sys
from datetime import date
import indep_pricer as ip
path = 'par2026.csv'
for basis_name, dates in [('exact 1 Jan', ip.PAYS), ('Nov-15 STRIPS', ip.NOV15), ('WInS end dates', ip.BUYABLE)]:
    print('==', basis_name)
    for day in sys.argv[1:]:
        m, d, y = map(int, day.split('/')); d0 = date(y, m, d)
        pts = ip.load_curve(path, day); c = ip.Curve(pts)
        pv = ip.ladder(c, d0, dates); t27 = ip.yf(d0, date(2027,1,1)); fwd = pv / c.df(t27)
        lo, hi = -0.02, 0.0
        for _ in range(80):
            mid = (lo+hi)/2; cs = ip.Curve(pts, mid); v = ip.ladder(cs, d0, dates)/cs.df(t27)
            lo, hi = (lo, mid) if v < 300_000 else (mid, hi)
        print(f"  {day}: PV ${pv:,.0f} | fwd 1 Jan 2027 ${fwd:,.0f} | headroom ${300000-fwd:,.0f} | break-even fall {-(lo+hi)/2*1e4:.1f}bp")
