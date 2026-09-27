import numpy as np
from datetime import date
t0=date(2026,9,28)
pay=[date(y,1,1) for y in range(2033,2043)]
T=np.array([(d-t0).days/365.25 for d in pay])
# Actuary zeros (as listed), from today
za=np.array([5.05,5.09,5.13,5.18,5.22,5.25,5.29,5.32,5.36,5.40])/100
pv0=(50000/(1+za)**T).sum(); print("Actuary PV today",round(pv0))
t27=(date(2027,1,1)-t0).days/365.25
for r in (0.0481,0.0487):
  print(" fwd to 1/1/27 at short",r,round(pv0*(1+r)**t27))
# naive: same zeros applied from 1/1/2027 (t=6..15)
print(" zeros applied t=6..15 from 2027:",round((50000/(1+za)**np.arange(6,16)).sum()))
# Macaulay/mod duration & DV01
mac=(T*50000/(1+za)**T).sum()/pv0; print(" Macaulay",round(mac,2),"mod~",round(mac/1.052,2))
up=(50000/(1+za+0.01)**T).sum(); dn=(50000/(1+za-0.01)**T).sum()
print(" +/-100bp",round(up),round(dn),"DV01",round((50000/(1+za-0.0001)**T).sum()-pv0))
# 2033 cost if locked now: forward value
print(" implied 2033 value",round(pv0*(1+za[0])**T[0]))
# annuity-due at flat rates
for r in (.05,.04,.03,.02): print(" 2033 annuity-due",r,round(sum(50000/(1+r)**k for k in range(10))))
# CIO: par used as zero, t=6..15 interp
par_t=[2,5,7,10,30]; par=[4.81,4.98,5.06,5.17,5.47]
z=np.interp(np.arange(6,16),par_t,par)/100
print("CIO par-as-zero PV27",round((50000/(1+z)**np.arange(6,16)).sum()), "-100bp",round((50000/(1+z-.01)**np.arange(6,16)).sum()))
# CIO whole-portfolio equity & floor
print("CIO equity share",0.7*150/450," floor 0.6*1.0481^2=",round(0.6*1.0481**2,3))
# Quant 2y growth
print("Quant x",round(1.0481**2,4))
# Quant $626k implied flat return: 300k@2027 6y + 150k@2028 5y
from scipy.optimize import brentq
f=lambda r:300e3*(1+r)**6+150e3*(1+r)**5-626e3
print("implied r for 626k",round(brentq(f,0,.2),4))
# Wait-strategy: who needs 2028? lock-only funded by 300k
print("Lock w/o 2028 margin",300000-294000,"(my) vs actuary", 300000-296692)
# my L31 check: reserve cost at 1/1/2031 with zeros t=2..11 approx interp
zz=np.interp(np.arange(2,12),[2,5,7,10,11],[4.87,5.03,5.10,5.24,5.31])/100
print("L31 approx",round((50000/(1+zz)**np.arange(2,12)).sum()))
