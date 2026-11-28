"""Part 1: the original ladder's cost, the stress test (Table 2), the extra Treasuries and the 2033 reserve.
MODEL. Run: python3 part1_ladder.py [B|C]   (B = PCHIP bootstrap, the audit's main curve; C = Nelson-Siegel-Svensson)"""
import json
import sys

import numpy as np
from scipy.optimize import linprog

from audit_core import *

meth = sys.argv[1] if len(sys.argv) > 1 else "B"
cv = bootstrap_pchip() if meth == "B" else nss_fit()
out = {"curve_method": meth}

# ---- 1. the original ladder: each rung sized so its flows, reinvested at forward rates, reach $50,000 on 1 Jan Y
flows27 = {y: instrument_flows(y, cv, J27, "fwd") for y in YEARS}          # per $1 of market value, bought 1 Jan 2027
cost = {}
for y in YEARS:
    fv = fv_at(flows27[y], date(y, 1, 1), cv, "fwd")
    cost[y] = PAY / fv
ladder27 = sum(cost.values())
pv_pay = sum(PAY * cv.P(J27, date(y, 1, 1)) for y in YEARS)
f27 = 1 / cv.P(J27, J28)
out["ladder"] = {"cost_by_rung_jan2027": {y: round(cost[y]) for y in YEARS},
                 "ladder_cost_jan2027": round(ladder27, 0),
                 "pv_payments_jan2027": round(pv_pay, 0),
                 "short_of_300k_jan2027": round(ladder27 - 300000, 0),
                 "short_of_300k_in_jan2028_money": round((ladder27 - 300000) * f27, 0)}

# ---- 2. the stress test: no interest on early receipts, 0.15% a year on waiting cash, fund payouts cut 0.5%
units = cost  # dollars of market value bought on 1 Jan 2027
fl0 = {y: instrument_flows(y, cv, J27, "zero", cut=CUT if y in FUND_FOR else 0.0) for y in YEARS}
net = {}
for y in YEARS:
    net[y] = units[y] * fv_at(fl0[y], date(y, 1, 1), cv, "zero", WAIT_FEE)
gap = {y: PAY - net[y] for y in YEARS}
out["stress"] = {"net_receipts": {y: round(net[y]) for y in YEARS}, "total": round(sum(net.values())),
                 "gap_by_year": {y: round(gap[y]) for y in YEARS}, "shortfall": round(sum(gap.values()))}
# the same without the fee and the cut, to show what each assumption costs
net_plain = {y: units[y] * fv_at(instrument_flows(y, cv, J27, "zero"), date(y, 1, 1), cv, "zero") for y in YEARS}
out["stress"]["shortfall_zero_interest_only"] = round(sum(PAY - v for v in net_plain.values()))

# ---- 3. the extra Treasuries: cheapest set bought 1 Jan 2028 from the same ten instruments whose receipts, held at
# zero interest less 0.15% a year (fund flows less 0.5%), cover every year's remaining gap. Receipts may be carried
# forward to later payments (at zero interest, less the fee) but never backward. Exact linear programme.
fl28 = {y: instrument_flows(y, cv, J28, "zero", cut=CUT if y in FUND_FOR else 0.0) for y in YEARS}
pay_dates = [date(y, 1, 1) for y in YEARS]
# A cumulative formulation: money arriving on date d, if first spent on payment k (date >= d), loses the fee from d
# to that date. Model the carry explicitly with variables: x_j (dollars of instrument j bought Jan 2028),
# s_k (surplus carried from payment k to k+1, losing the fee for one year). Balance at each payment k:
#   own_k + sum_j x_j * a_jk + s_{k-1} * (1 - fee) = 50,000 + s_k, with a_jk = receipts of $1 of j arriving in
#   (pay_{k-1}, pay_k], each charged the fee from its arrival to pay_k.
nJ, nK = len(YEARS), len(YEARS)
a = np.zeros((nK, nJ))
for j, y in enumerate(YEARS):
    for d, amt in fl28[y]:
        for k, pd in enumerate(pay_dates):
            lo = pay_dates[k - 1] if k else date(1900, 1, 1)
            if lo < d <= pd:
                a[k, j] += amt * (1 - WAIT_FEE) ** yf(d, pd)
# own receipts per payment window (the ten bought in 2027, pooled by arrival window, fee to that payment date)
own = np.zeros(nK)
for y in YEARS:
    for d, amt in fl0[y]:
        for k, pd in enumerate(pay_dates):
            lo = pay_dates[k - 1] if k else date(1900, 1, 1)
            if lo < d <= pd:
                own[k] += units[y] * amt * (1 - WAIT_FEE) ** yf(d, pd)
# variables: x (nJ), s (nK); minimise sum x
cvec = np.r_[np.ones(nJ), np.zeros(nK)]
Aeq = np.zeros((nK, nJ + nK)); beq = np.zeros(nK)
for k in range(nK):
    Aeq[k, :nJ] = a[k]
    Aeq[k, nJ + k] = -1.0
    if k:
        Aeq[k, nJ + k - 1] = (1 - WAIT_FEE)
    beq[k] = PAY - own[k]
res = linprog(cvec, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * (nJ + nK), method="highs")
x = res.x[:nJ]
extra28 = float(x.sum())
out["extra_treasuries"] = {"cost_jan2028": round(extra28), "by_instrument": {YEARS[j]: round(x[j]) for j in range(nJ) if x[j] > 1},
                           "pooled_own_receipts_total": round(own.sum())}

# the same LP with the second, pooled arrangement of the ten (receipts of the ten pooled across payments)
top_up28 = (ladder27 - 300000) * f27
out["second_deposit"] = {"top_up_jan2028": round(top_up28), "extra": round(extra28),
                         "operating_total_from_2028_deposit": round(top_up28 + extra28),
                         "operating_allocation_nominal_total": round(300000 + top_up28 + extra28),
                         "left_for_facility": round(150000 - top_up28 - extra28)}

# ---- 4. the reserve on 1 Jan 2033 on today's forward curve: market value of everything held for the ten
# (the ten as bought in 2027, plus the extra Treasuries), with every receipt before 2033 reinvested at forwards
def value_on(d_target, holdings_cost, buy):
    """Forward value on d_target of $holdings bought at `buy` = cost / P(buy, target) (self-financing at forwards)."""
    return holdings_cost / cv.P(buy, d_target)

res33 = value_on(J33, ladder27, J27) + value_on(J33, extra28, J28)
# the ladder's own cost includes the 0.07% fund fee drag; value at forwards on 1 Jan 2033 = PV of remaining flows
# reinvested at forwards. Fee drag after 2033 is small; use the cost-carry identity (exact for bonds, approx for funds)
pv33 = sum(PAY * cv.P(J33, date(y, 1, 1)) for y in YEARS)
out["reserve_2033"] = {"value_1jan2033": round(res33), "pv_payments_1jan2033": round(pv33),
                       "ratio": round(res33 / pv33, 4)}

# zero-interest totals of the whole reserve, for the "sufficient under stress" claim
zero_total = sum(net.values()) + float(sum(x[j] * sum(amt * (1 - WAIT_FEE) ** yf(d, pay_dates[-1]) for d, amt in fl28[YEARS[j]]) for j in range(nJ)))
out["reserve_2033"]["undiscounted_receipts_under_stress_approx"] = round(zero_total)
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / f"results_part1_{meth}.json", "w"), indent=1)
