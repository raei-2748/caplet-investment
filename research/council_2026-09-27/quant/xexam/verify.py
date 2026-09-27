import numpy as np
from datetime import date
from scipy.stats import norm
g,D=np.load('actuary/zc.npy')
gg=np.r_[0,g]; DD=np.r_[1,D]            # fix: anchor DF(0)=1
dfA=lambda t: np.exp(np.interp(t,g,np.log(D)))   # actuary's (clamped) version
dfF=lambda t: np.exp(np.interp(t,gg,np.log(DD)))
val=date(2026,9,28); t=np.array([(date(y,1,1)-val).days/365.25 for y in range(2033,2043)])
t27=(date(2027,1,1)-val).days/365.25; t28=(date(2028,1,1)-val).days/365.25
pv=sum(5e4*dfA(x) for x in t)
print("ACTUARY PV today %.0f"%pv)
print("fwd27 actuary %.0f  fixed %.0f"%(pv/dfA(t27),pv/dfF(t27)))
print("fwd28 actuary %.0f  fixed %.0f"%(pv/dfA(t28),pv/dfF(t28)))
print("implied 3-mo rate in actuary fwd27: %.2f%%"%(100*((1/dfA(t27))**(1/t27)-1)))
print("L33 %.0f"%(pv/dfA(t[0])))
for r in [.05,.04,.03,.02]: print("flat",r,"%.0f"%sum(5e4/(1+r)**k for k in range(10)))
# DV01
zz=lambda x:2*(dfA(x)**(-1/(2*x))-1)
p=lambda s:sum(5e4*(1+(zz(x)+s)/2)**(-2*x) for x in t)
print("modDur %.2f DV01 %.0f"%((p(-1e-4)-p(1e-4))/(2e-4*p(0)),(p(-1e-4)-p(1e-4))/2))
# CIO: par used as zero, annual comp, t=6..15, par linearly interpolated
T=np.array([2,5,7,10,30.]);Y=np.array([4.81,4.98,5.06,5.17,5.47])/100
tt=np.arange(6,16); z=np.interp(tt,T,Y)
print("CIO z",np.round(z*100,2)," PV27 %.0f  -100bp %.0f"%((5e4/(1+z)**tt).sum(),(5e4/(1+z-.01)**tt).sum()))
# CLIENT: F=a*S*(1+z2)^2, median contribution, P(loss)
z2=0.0481
for V in [450,550,650]:
    S=V-364; F=.5*S*(1+z2)**2
    m=2*(np.log(1.055)-.5*.16**2); s=.16*np.sqrt(2)  # 5.5% as arithmetic mean
    med=np.exp(m); q90=np.exp(m+1.2816*s)
    print(V,"S",S,"F %.1f med %.1f U %.1f flex %.1f"%(F,F+.5*.5*S*med,F+.5*.5*S*q90,.5*.5*S*med))
print("P(loss 2y) %.3f  q05 %.3f q90 %.3f"%(norm.cdf(-m/s),np.exp(m-1.645*s),np.exp(m+1.2816*s)))
# Client floor vs quant-rule floor, V31=550: a=0.5 floor vs 0.96*S (95%) vs full 2y lock
S=186; print("floor share of S: client %.2f, quant q05 0.96, full-lock %.2f"%(.5*1.0986,1.0986))
# Actuary Vasicek drift: expected 2033 short-level from 5.1 with theta 4, kappa .15 over 6y
print("Vasicek E[r_2033] %.2f%%"%(100*(0.04+(0.051-0.04)*np.exp(-.15*6))))
print("2033 cost at E-rate vs today-fwd:",round(sum(5e4/(1.0445)**k for k in range(10))), round(pv/dfA(t[0])))
