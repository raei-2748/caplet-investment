from curve import *
from scipy.optimize import brentq
t0=0.26 # 2026-09-28 -> 2027-01-01
pay=np.arange(6,16)  # years after 2027-01-01
print("zeros at 6..15y:",np.round(100*zero(pay),2))
# forward price at 2027-01-01 of all ten payments (spot curve approximated as curve at 2027)
c27=sum(50000*df(p) for p in pay); print("Cost at 1/1/2027 to defease all 10 (today's curve):",round(c27))
# reserve cost in 2033 if curve unchanged (spot shape)
r33=sum(50000*df(k) for k in range(10)); print("Reserve cost 2033 unchanged curve:",round(r33))
a=lambda r: sum(50000/(1+r)**k for k in range(10))
for r in [.03,.04,.051]: print(r, round(a(r)), round(a(r)/(1+r)**6))
# team 626k implied return
g=brentq(lambda g:300e3*(1+g)**6+150e3*(1+g)**5-626e3,0,.2); print("implied return for 626k:",g)
print("PV 2033-2036 at 2027:",round(sum(50000*df(p) for p in pay[:4])))
