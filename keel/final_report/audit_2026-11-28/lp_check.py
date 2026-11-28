"""Part 1b: why the extra Treasuries' size depends on whether the ten's own early receipts may be spent on earlier
payments (pooled) or are held for their own payment (the existing engine's rule). MODEL."""
import json, sys
import numpy as np
from scipy.optimize import linprog
from audit_core import *
cv = bootstrap_pchip() if (len(sys.argv) < 2 or sys.argv[1] == "B") else nss_fit()
pay_dates = [date(y, 1, 1) for y in YEARS]
flows27 = {y: instrument_flows(y, cv, J27, "fwd") for y in YEARS}
units = {y: PAY / fv_at(flows27[y], date(y, 1, 1), cv, "fwd") for y in YEARS}
cut = lambda y: CUT if y in FUND_FOR else 0.0
def win(d):
    for k, pd in enumerate(pay_dates):
        if (pay_dates[k-1] if k else date(1900,1,1)) < d <= pd: return k
    return None
def solve(buy, pooled):
    fl = {y: instrument_flows(y, cv, buy, "zero", cut(y)) for y in YEARS}
    fl0 = {y: instrument_flows(y, cv, J27, "zero", cut(y)) for y in YEARS}
    n = 10; a = np.zeros((n, n)); own = np.zeros(n)
    for j, y in enumerate(YEARS):
        for d, amt in fl[y]:
            k = win(d)
            if k is not None: a[k, j] += amt * (1 - WAIT_FEE) ** yf(d, pay_dates[k])
        for d, amt in fl0[y]:
            if pooled:
                k = win(d)
                if k is not None: own[k] += units[y] * amt * (1 - WAIT_FEE) ** yf(d, pay_dates[k])
            else:
                k = YEARS.index(y)
                if d <= pay_dates[k]: own[k] += units[y] * amt * (1 - WAIT_FEE) ** yf(d, pay_dates[k])
    c = np.r_[np.ones(n), np.zeros(n)]
    A = np.zeros((n, 2*n)); b = np.zeros(n)
    for k in range(n):
        A[k, :n] = a[k]; A[k, n+k] = -1
        if k: A[k, n+k-1] = 1 - WAIT_FEE
        b[k] = PAY - own[k]
    r = linprog(c, A_eq=A, b_eq=b, bounds=[(0, None)]*(2*n), method="highs")
    x = r.x[:n]
    return {"cost_at_purchase": round(x.sum()), "in_jan2028_money": round(x.sum() / (cv.P(J27, J28) if buy == J27 else 1)),
            "by_rung": {YEARS[j]: round(x[j]) for j in range(n) if x[j] > 1}, "spare_after_2042": round(r.x[-1])}
out = {"pooled_bought_2028": solve(J28, True), "own_rungs_kept_bought_2028": solve(J28, False),
       "own_rungs_kept_bought_2027": solve(J27, False), "pooled_bought_2027": solve(J27, True)}
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / "results_lp_check.json", "w"), indent=1)

# ---- independent check of the pooled solution by simulating one cash pot day by day (zero interest, 0.15% fee)
def simulate(xd, buy=J28):
    events = []
    for y in YEARS:
        for d, amt in instrument_flows(y, cv, J27, "zero", cut(y)):
            events.append((d, units[y] * amt))
        fl = instrument_flows(y, cv, buy, "zero", cut(y))
        px_unit = 1.0  # x is in dollars of market value? no: LP variables are $ of market value (flows per $1)
        for d, amt in fl:
            events.append((d, xd.get(y, 0.0) * amt))
    for y in YEARS:
        events.append((date(y, 1, 1), -PAY))
    events.sort(key=lambda e: (e[0], e[1] < 0))
    pot, last, low = 0.0, events[0][0], 1e18
    for d, a in events:
        pot *= (1 - WAIT_FEE) ** yf(last, d); last = d
        pot += a
        if a < 0: low = min(low, pot)
    return round(low), round(pot)
sol = solve(J28, True)
print("pooled solution, lowest pot after a payment and pot left after 2042:", simulate({int(k): v for k, v in sol["by_rung"].items()}))
