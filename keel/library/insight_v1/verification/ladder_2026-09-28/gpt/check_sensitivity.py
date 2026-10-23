"""Repricing checks and alternative assumptions. Run beside price_ladder.py."""
from math import exp, log
from price_ladder import *


def sparse_curve(fall_bp=0):
    """Calibrate only supplied pillars, with log-linear D between pillars."""
    rates = [r-fall_bp/10_000 for r in PAR]
    xs = [0] + TENORS[:4]
    logs = [0] + [-2*t*log(1+r/2) for t, r in zip(TENORS[:4], rates[:4])]
    for t, r in zip(TENORS[4:], rates[4:]):
        coupons = [n/2 for n in range(1, int(2*t)+1)]
        def residual(last_log):
            ds = [exp(interp(u, xs+[t], logs+[last_log])) for u in coupons]
            return r/2*sum(ds) + ds[-1]-1
        lo, hi = -10.0, logs[-1]
        assert residual(lo) < 0 < residual(hi)
        for _ in range(80):
            mid = (lo+hi)/2
            if residual(mid) < 0:
                lo = mid
            else:
                hi = mid
        xs.append(t)
        logs.append((lo+hi)/2)
    return lambda t: exp(interp(t, xs, logs))


base = bootstrap()
for name, d in [('linear par / log-linear D', base), ('sparse log-linear D', sparse_curve())]:
    errors = []
    for t, p in zip(TENORS[3:], PAR[3:]):
        cashflows = sum(d(n/2) for n in range(1, int(2*t)+1))
        errors.append(abs(p/2*cashflows+d(t)-1))
    assert max(errors) < 1e-12
    print(name, 'max supplied par repricing error:', max(errors))
    pv, fw = costs(d)
    assert abs(sum(fw)*d(S)-sum(pv)) < 1e-8
    print('  Today:', sum(pv), 'Forward:', sum(fw))
print('Alternative interpolation threshold (bp):',
      threshold(lambda bp: sum(costs(sparse_curve(bp))[1])))
for denom in [365, 365.25]:
    s = (DELIVERY-TODAY).days/denom
    value = sum(FACE*base((m-TODAY).days/denom) for m in MATURITIES)/base(s)
    print('Forward at day-count denominator', denom, value)
simple_xs = [0] + TENORS[:4]
simple_logs = [0] + [-log(1+r*t) for t, r in zip(TENORS[:4], PAR[:4])]
simple_ds = exp(interp(S, simple_xs, simple_logs))
print('Forward with simple-interest short end:', sum(costs(base)[0])/simple_ds)
wrong_pv = sum(FACE*(1+interp(t, TENORS, PAR)/2)**(-2*t) for t in TIMES)
print('If par yields incorrectly used as zero yields:', wrong_pv/base(S))
f0 = sum(costs(base)[1])
print('Symmetric par sensitivity dollars per bp:', (forward_cost(1)-forward_cost(-1))/2)
forward_zeros = [2*((base(t)/base(S))**(-1/(2*(t-S)))-1) for t in TIMES]
print('Threshold shifting delivery-date forward zero yields:', threshold(
    lambda bp: sum(FACE*(1+(z-bp/10_000)/2)**(-2*(t-S))
                   for z, t in zip(forward_zeros, TIMES))))
root = threshold(forward_cost)
assert forward_cost(root-0.0001) < 300_000 < forward_cost(root+0.0001)
assert forward_cost(26) < 300_000 < forward_cost(27)
print('All checks passed.')
