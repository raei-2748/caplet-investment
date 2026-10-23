"""Independent synthetic Treasury par-curve bootstrap; Python standard library only.
Supplied inputs are accepted as given, not independently authenticated market quotes.
Time: ACT/365F for dated cash flows; quoted curve tenors use months/12 and years.
Short-end inputs are interpreted as nominal semiannually compounded zero yields.
No settlement lag, business-day adjustment, fees, tax or STRIPS basis.
"""
from bisect import bisect_left
from datetime import date
from math import exp, log
import csv
from pathlib import Path

TENORS = [1/12, 2/12, 3/12, .5, 1, 2, 3, 5, 7, 10, 20, 30]
PAR = [p/100 for p in [4.04, 4.20, 4.28, 4.41, 4.59, 4.92,
                        5.01, 5.06, 5.15, 5.24, 5.60, 5.56]]
TODAY, DELIVERY = date(2026, 9, 28), date(2027, 1, 1)
MATURITIES = [date(y, 11, 15) for y in range(2032, 2042)]
TIMES = [(m-TODAY).days/365 for m in MATURITIES]
S = (DELIVERY-TODAY).days/365
FACE = 50_000


def interp(t, xs, ys):
    assert xs[0] <= t <= xs[-1]
    k = bisect_left(xs, t)
    if xs[k] == t:
        return ys[k]
    w = (t-xs[k-1])/(xs[k]-xs[k-1])
    return ys[k-1]*(1-w) + ys[k]*w


def bootstrap(fall_bp=0):
    """Linear par yields at every half year; exact semiannual par bootstrap."""
    rates = [p-fall_bp/10_000 for p in PAR]
    grid, discounts = [], []
    for n in range(1, 61):
        t = n/2
        c = interp(t, TENORS, rates)/2
        d = (1-c*sum(discounts))/(1+c)
        assert 0 < d < 1
        # Every interpolated par bond must reprice to one.
        assert abs(c*sum(discounts)+(1+c)*d-1) < 1e-12
        grid.append(t)
        discounts.append(d)
    xs = [0] + TENORS[:3] + grid
    ds = [1] + [(1+r/2)**(-2*t)
                for t, r in zip(TENORS[:3], rates[:3])] + discounts
    logs = [log(d) for d in ds]
    return lambda t: exp(interp(t, xs, logs))


def costs(discount):
    today = [FACE*discount(t) for t in TIMES]
    forward = [v/discount(S) for v in today]
    return today, forward


def forward_cost(fall_bp):
    return sum(costs(bootstrap(fall_bp))[1])


def threshold(value):
    lo, hi = 0.0, 200.0
    assert value(lo) < 300_000 < value(hi)
    for _ in range(80):
        mid = (lo+hi)/2
        if value(mid) < 300_000:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def zero_shift_cost(fall_bp):
    """Alternative: shift today's bootstrapped semiannual ZERO yields."""
    base = bootstrap()
    def shifted(t):
        if t == 0:
            return 1.0
        z = 2*(base(t)**(-1/(2*t))-1)
        return (1+(z-fall_bp/10_000)/2)**(-2*t)
    return sum(costs(shifted)[1])


if __name__ == '__main__':
    d = bootstrap()
    pv, fwd = costs(d)
    rows = [(m.isoformat(), t, 100*2*(d(t)**(-1/(2*t))-1), a, b)
            for m, t, a, b in zip(MATURITIES, TIMES, pv, fwd)]
    print('Maturity       Years   Zero yield %      Today $     Forward $')
    for m, t, z, a, b in rows:
        print(f'{m} {t:10.6f} {z:12.6f} {a:12.2f} {b:13.2f}')
    print(f'TOTAL                              {sum(pv):12.2f} {sum(fwd):13.2f}')
    print(f'Delivery time = {S:.12f}; D(delivery) = {d(S):.12f}')
    root = threshold(forward_cost)
    print(f'Par-yield fall threshold = {root:.9f} bp; cost = {forward_cost(root):.6f}')
    print(f'Zero-yield fall threshold = {threshold(zero_shift_cost):.9f} bp')
    for bp in [0, 1, 25, 30, 35, 40, 50, 100]:
        print(f'Par fall {bp:3} bp: forward cost ${forward_cost(bp):,.2f}')
    print('Selected bootstrapped nodes: tenor, discount, semiannual zero %')
    for t in [.5, 1, 2, 3, 5, 7, 10, 15, 20, 30]:
        print(f'{t:5.1f} {d(t):.9f} {200*(d(t)**(-1/(2*t))-1):.6f}')
    out = Path(__file__).resolve().parent
    with (out/'rung_prices.csv').open('w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['maturity', 'years_ACT365F', 'zero_yield_pct', 'today_USD', 'forward_USD'])
        w.writerows(rows)
