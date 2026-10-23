import numpy as np
from scipy.stats import norm
from datetime import date
G,D=np.load("actuary/zc.npy")
df=lambda t: np.exp(np.interp(t,G,np.log(D)))
val=date(2026,9,28); yr=lambda d:(d-val).days/365.25
pay=[yr(date(y,1,1)) for y in range(2033,2043)]
t27,t31=yr(date(2027,1,1)),yr(date(2031,1,1))
pv=sum(50000*df(x) for x in pay)
print("MY forward PV 1/1/2027:",round(pv/df(t27)))
print("MY forward cost 1/1/2031 (Client L31 check):",round(pv/df(t31)))
# CIO: par yields as zeros, t=6..15, interp 2y4.81 5y4.98 7y5.06 10y5.17 30y5.47
T=[2,5,7,10,30];Y=[4.81,4.98,5.06,5.17,5.47]
pvc=lambda s: sum(50000/(1+np.interp(t,T,Y)/100+s)**t for t in range(6,16))
print("CIO zeros t6..15:",np.round(np.interp(range(6,16),T,Y),3))
print("CIO PV27 base:",round(pvc(0))," -100bp:",round(pvc(-0.01)))
for r in [.05,.04,.03]: print(" annuity-due 2033 at",r,round(sum(50000/(1+r)**k for k in range(10))))
print("CIO whole-port equity 2028:",0.7*150/450, " floor 0.6*1.0481^2=",0.6*1.0481**2)
# Client: F=0.5*86k*(1+z2)^2, equity 2y loss prob at 5.5%/16%
print("Client F at S=86k:",round(0.5*86000*1.0487**2))
mu=np.log(1.055);s=.16
print("P(2y equity loss) geometric-median interp:",round(norm.cdf(-2*mu/(s*2**.5)),3),
      " arithmetic-mean interp:",round(norm.cdf(-(2*(np.log(1.055)-s*s/2))/(s*2**.5)),3))
print("Client 5th/90th 2y factor (arith 5.5%):",np.round(np.exp(2*(mu-s*s/2)+np.array([-1.645,1.2816])*s*2**.5),3))
print("FX fwd 2y:",round(31.79*(1.02/1.0481)**2,2)," pct:",round((1.02/1.0481)**2-1,4))
print("Real 50k 2033/2042 @2%:",round(50000/1.02**7),round(50000/1.02**16))
# Quant: 2033 reserve cost via my forwards; $626k implied flat return
pay33=[p for p in pay]; print("fwd cost 1/1/2033:",round(pv/df(pay[0])))
# 300k 2027, 150k 2028 -> 626k 2033 solve r
from scipy.optimize import brentq
r=brentq(lambda r:300e3*(1+r)**6+150e3*(1+r)**5-626e3,0,.2); print("implied r for 626k:",round(r,4))
w=np.array([50000*df(x) for x in pay]); tt=np.array(pay)-t27
print("Macaulay dur from 1/1/2027:",round((w*tt).sum()/w.sum(),2))
