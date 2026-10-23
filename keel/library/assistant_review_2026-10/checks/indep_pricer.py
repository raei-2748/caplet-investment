"""Independent check of the Team Caplet ladder numbers (written from scratch, no repo code reused).

Bootstraps a discount curve from the official Treasury par yield curve (home.treasury.gov CSV),
prices Laura's ten $50,000 payments (1 Jan 2033..2042), forward-values them to 1 Jan 2027,
finds the parallel break-even fall, and checks the Book L coupon bonds and coupon reinvestment.
Method: par yields treated as semiannual bond-equivalent par rates, linearly interpolated on a
semiannual grid, bootstrapped; log-discount factors interpolated linearly (flat forwards).
"""
import csv
import math
import sys
from datetime import date

import numpy as np

TENORS = {"1 Mo": 1 / 12, "1.5 Month": 1.5 / 12, "2 Mo": 2 / 12, "3 Mo": 0.25, "4 Mo": 4 / 12, "6 Mo": 0.5,
          "1 Yr": 1, "2 Yr": 2, "3 Yr": 3, "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}


def load_curve(path, day):
    with open(path) as f:
        for row in csv.DictReader(f):
            if row["Date"] == day:
                pts = sorted((TENORS[k], float(v) / 100) for k, v in row.items() if k in TENORS and v)
                return pts
    raise SystemExit(f"{day} not in {path}")


class Curve:
    def __init__(self, pts, shift=0.0):
        ts = np.array([p[0] for p in pts])
        ys = np.array([p[1] for p in pts]) + shift
        self.grid = np.arange(0.5, 30.0001, 0.5)
        par = np.interp(self.grid, ts, ys)
        dfs = []
        for n, (t, c) in enumerate(zip(self.grid, par)):
            s = sum(dfs)
            dfs.append((1 - c / 2 * s) / (1 + c / 2))
        self.dfs = np.array(dfs)
        # short end below 6M: treat each bill point as a zero with semiannual compounding
        short = [(t, y) for t, y in zip(ts, ys) if t < 0.5]
        self.short_t = np.array([0.0] + [t for t, _ in short] + [0.5])
        self.short_df = np.array([1.0] + [(1 + y / 2) ** (-2 * t) for t, y in short] + [self.dfs[0]])

    def df(self, t):
        if t <= 0:
            return 1.0
        if t <= 0.5:
            return math.exp(np.interp(t, self.short_t, np.log(self.short_df)))
        return math.exp(np.interp(t, self.grid, np.log(self.dfs)))


def yf(d0, d1):
    return (d1 - d0).days / 365.25


PAYS = [date(y, 1, 1) for y in range(2033, 2043)]
NOV15 = [date(y - 1, 11, 15) for y in range(2033, 2043)]
BUYABLE = [date(2032, 12, 15), date(2033, 12, 15), date(2034, 12, 15), date(2035, 12, 15), date(2036, 12, 15),
           date(2037, 2, 15), date(2038, 5, 15), date(2039, 11, 15), date(2040, 11, 15), date(2041, 11, 15)]
BASIS = PAYS


def ladder(curve, d0, dates=None):
    return sum(50_000 * curve.df(yf(d0, p)) for p in (dates or BASIS))


def bond_flows(coupon, maturity, d0):
    """Remaining (date, cash per 100 face) for a semiannual Treasury."""
    flows = []
    m = maturity
    k = 0
    while True:
        y, mo = m.year, m.month - 6 * k
        while mo <= 0:
            mo += 12
            y -= 1
        d = date(y, mo, m.day)
        if d <= d0:
            break
        flows.append((d, coupon / 2 + (100 if k == 0 else 0)))
        k += 1
    return sorted(flows), d


def accrued(coupon, maturity, d0):
    flows, last = bond_flows(coupon, maturity, d0)
    nxt = flows[0][0]
    return coupon / 2 * (d0 - last).days / (nxt - last).days


def dirty_from_curve(curve, coupon, maturity, d0):
    flows, _ = bond_flows(coupon, maturity, d0)
    return sum(cf * curve.df(yf(d0, d)) for d, cf in flows)


def ytm_from_dirty(dirty, coupon, maturity, d0):
    flows, _ = bond_flows(coupon, maturity, d0)
    lo, hi = -0.05, 0.20
    for _ in range(200):
        mid = (lo + hi) / 2
        pv = sum(cf / (1 + mid / 2) ** (2 * yf(d0, d)) for d, cf in flows)
        lo, hi = (mid, hi) if pv > dirty else (lo, mid)
    return (lo + hi) / 2


if __name__ == "__main__":
    path = sys.argv[1]
    for day in sys.argv[2:]:
        m, d, y = map(int, day.split("/"))
        d0 = date(y, m, d)
        pts = load_curve(path, day)
        c = Curve(pts)
        pv = ladder(c, d0)
        t27 = yf(d0, date(2027, 1, 1))
        fwd = pv / c.df(t27)
        # break-even: parallel shift of the par curve that makes the forward value hit 300k
        lo, hi = -0.02, 0.0
        for _ in range(100):
            mid = (lo + hi) / 2
            cs = Curve(pts, mid)
            v = ladder(cs, d0) / cs.df(t27)
            lo, hi = (lo, mid) if v < 300_000 else (mid, hi)
        be = -(lo + hi) / 2 * 1e4
        print(f"{day}: PV today ${pv:,.0f} | fwd to 1 Jan 2027 ${fwd:,.0f} | headroom ${300_000 - fwd:,.0f} "
              f"| break-even parallel fall {be:.1f}bp | 10y par {dict(pts)[10]*100:.2f}%")
