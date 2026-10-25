"""MODEL. Replica of the deterministic stress in keel/library/ips_numbers_2026-10/ips_numbers.py (lines 161-176),
split into parts, on the 15 Oct and 23 Oct curves. Usage: python3 -I caplet_replica.py CSV_OCT15 CSV_OCT23"""
import csv, sys, datetime as dt
import numpy as np
T27 = dt.date(2027, 1, 1); YMIN = .25; PAY = 50000.0
RUNGS = {2033: (dt.date(2032,12,15), None), 2034: (dt.date(2033,12,15), None), 2035: (dt.date(2034,12,15), None),
         2036: (dt.date(2035,12,15), None), 2037: (dt.date(2036,12,15), None), 2038: (dt.date(2037,2,15), 4.75),
         2039: (dt.date(2038,5,15), 4.50), 2040: (dt.date(2039,11,15), 4.375), 2041: (dt.date(2040,11,15), 4.25),
         2042: (dt.date(2041,11,15), 3.125)}
yrs = lambda a, b: (b - a).days / 365.25
def load(path, day):
    r = [x for x in csv.DictReader(open(path)) if x["Date"] == day][0]
    pts = {1/12: "1 Mo", .25: "3 Mo", .5: "6 Mo", 1: "1 Yr", 2: "2 Yr", 3: "3 Yr", 5: "5 Yr", 7: "7 Yr", 10: "10 Yr", 20: "20 Yr", 30: "30 Yr"}
    xs = np.array(list(pts)); ys = np.array([float(r[k]) for k in pts.values()])
    return lambda t: float(np.interp(t, xs, ys))
def stress(curve, today, dy, ib=True, tb=True, gap=True):
    TOFF = yrs(today, T27); tot = 0.0
    for py, (mat, cpn) in RUNGS.items():
        T = yrs(T27, mat); y0 = curve(T + TOFF)
        isib = cpn is None
        if (isib and not ib) or (not isib and not tb): tot += PAY; continue
        cc = (y0 if isib else cpn) / 100
        k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        yk = max(y0 + dy, YMIN) / 100
        d = 1 + cc / 2 * ((1 + yk / 2) ** (2 * (T - k))).sum()
        db = 1 + cc / 2 * ((1 + y0 / 200) ** (2 * (T - k))).sum()
        gy = yrs(mat, dt.date(py, 1, 1))
        g = (1 + max(curve(.25) + (dy if gap else 0), YMIN) / 100) ** gy; gb = (1 + curve(.25) / 100) ** gy
        tot += PAY / (db * gb) * d * g
    return 500000 - tot
for path, day, today in ((sys.argv[1], "10/15/2026", dt.date(2026,10,15)), (sys.argv[2], "10/23/2026", dt.date(2026,10,23))):
    c = load(path, day)
    for dy in (-1, -2, -3):
        print(f"{day} {dy:+d}pp: total ${stress(c,today,dy):,.0f} | iBonds only ${stress(c,today,dy,tb=False,gap=False):,.0f}"
              f" | T-bonds only ${stress(c,today,dy,ib=False,gap=False):,.0f} | gap-bill part ${stress(c,today,dy)-stress(c,today,dy,gap=False):,.0f}")
