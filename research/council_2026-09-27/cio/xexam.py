import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
# Actuary: zero rates for 1/1/2033..1/1/2042, valued 28 Sep 2026
z=np.array([5.05,5.09,5.13,5.18,5.22,5.25,5.29,5.32,5.36,5.40])/100
t0=(np.datetime64('2033-01-01')-np.datetime64('2026-09-28')).astype(int)/365.25
t=t0+np.arange(10)
pv=(50000/(1+z)**t).sum(); print("Actuary PV today",round(pv))
z27=4.87/100; t27=(np.datetime64('2027-01-01')-np.datetime64('2026-09-28')).astype(int)/365.25
print("fwd PV 1/1/2027",round(pv*(1+z27)**t27))
print("PV 2037-42",round((50000/(1+z[4:])**t[4:]).sum()), "2033-36",round((50000/(1+z[:4])**t[:4]).sum()))
pvf=lambda s:(50000/(1+z+s)**t).sum()
print("DV01",round((pvf(-1e-4)-pvf(1e-4))/2,1),"moddur",round((pvf(-1e-4)-pvf(1e-4))/(2e-4*pv),2))
print("+/-100bp",round(pvf(.01)),round(pvf(-.01)))
# tail -100bp exposure
tail=lambda s:(50000/(1+z[4:]+s)**t[4:]).sum()
print("tail extra cost -100/-200",round(tail(-.01)-tail(0)),round(tail(-.02)-tail(0)))
# forward cost at 1/1/2033 (using 6.26y zero ~5.05 approx)
print("implied 2033 cost",round(pv*(1+z[0])**t[0]))
# spot-curve annuity at 2033 using today's curve shape 0..9y (par approx): quant's 404k
for r in [.05,.04,.03]: print("annuity-due",r,round(sum(50000/(1+r)**k for k in range(10))))
# Client: F, median contribution, loss prob
z2=0.0487; S=450e3-364e3; F=.5*S*(1+z2)**2
mu=np.log(1.055)-.5*.16**2; m2,s2=2*mu,.16*np.sqrt(2)
print("Client F",round(F),"P(loss 2y)",round(norm.cdf(-m2/s2),3),"p5 fac",round(np.exp(m2-1.645*s2),3),"p90 fac",round(np.exp(m2+1.2816*s2),3))
med=F+.5*(.5*S*np.exp(m2)); U=F+.5*(.5*S*np.exp(m2+1.2816*s2)); print("median contrib",round(med),"U",round(U))
# client L31 forward-ish check: 294k locked at 2027 grown 4y at ~5.1%
print("294k*1.051^4",round(294e3*1.051**4))
# Quant: implied rate of team's 626k
f=lambda r:300*(1+r)**6+150*(1+r)**5-626
print("implied flat r for 626k",round(brentq(f,0,.2),4))
print("2y floor growth",round(1.0481**2,4))
# my ladder, -100bp at 2027 transmitted to 2033 facility
print("extra 2027 cost -100bp compounded to 2033 @5.1%",round((327931-297745)*1.051**6))
