import csv, json
from datetime import date
import indep_pricer as ip
rows = list(csv.DictReader(open('par2026.csv')))
out = []
for r in rows:
    m, d, y = map(int, r['Date'].split('/'))
    if not (y == 2026 and m in (8, 9)): continue
    d0 = date(y, m, d)
    pts = ip.load_curve('par2026.csv', r['Date'])
    c = ip.Curve(pts)
    pv = ip.ladder(c, d0, ip.NOV15)
    fwd = pv / c.df(ip.yf(d0, date(2027, 1, 1)))
    out.append((d0.isoformat(), round(fwd), float(r['10 Yr'])))
out.sort()
for o in out: print(o)
json.dump(out, open('sept_series.json', 'w'))
