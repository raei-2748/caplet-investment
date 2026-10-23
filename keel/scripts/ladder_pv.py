"""FICTION (Team Keel). Cost on 1 Jan 2027 of ten $50,000 payments on 1 Jan 2033..2042.
MODEL: par yields as semiannual yields, bootstrapped on a 0.5y grid, log-linear discount factors
(same method as keel/library/verified_2026-09-27/official_curve_pv.py). Edit CURVE and VAL to re-run."""
from datetime import date
import numpy as np

VAL = date(2026, 10, 21)  # curve date
CURVE = {1/12: 4.09, 2/12: 4.16, .25: 4.25, .5: 4.35, 1: 4.52, 2: 4.81, 3: 4.89,
         5: 4.95, 7: 5.03, 10: 5.13, 20: 5.47, 30: 5.42}
ANCHOR = date(2027, 1, 1)


def yf(d):
    return (d - VAL).days / 365.25


def build(par):
    ts = sorted(par)
    grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts])
    df = []
    for y in p:
        c = y / 2
        df.append((1 - c * sum(df)) / (1 + c))
    g, lz = np.r_[0, grid], np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))


def cost(shift=0.0):
    f = build({k: v + shift for k, v in CURVE.items()})
    return sum(50000 * f(yf(date(y, 1, 1))) / f(yf(ANCHOR)) for y in range(2033, 2043))


if __name__ == "__main__":
    c = cost()
    dv01 = (cost(-.01) - cost(.01)) / 2
    print(f"cost ${c:,.0f}  headroom ${300000 - c:,.0f} = {(300000 - c) / dv01:.0f}bp  DV01 ${dv01:,.0f}/bp")
