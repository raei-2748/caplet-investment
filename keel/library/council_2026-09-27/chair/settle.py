import numpy as np
from scipy.optimize import brentq
# Par yields (snippets, ~2026-09-25; UNVERIFIED): annual-coupon convention ASSUMED
par_t=np.array([2,5,7,10,20,30.]); par_y=np.array([4.81,4.99,5.06,5.17,5.45,5.48])/100
T=np.arange(1,31); py=np.interp(T,par_t,par_y)  # flat below 2y (ASSUMPTION)
df=np.zeros(30)
for i,t in enumerate(T):
    c=py[i]; df[i]=(1-c*df[:i].sum())/(1+c)
z=df**(-1/T)-1
def DF(t):  # log-linear, DF(0)=1 anchored
    return np.exp(np.interp(t,np.r_[0,T],np.r_[0,np.log(df)]))
tau=(96)/365  # 2026-09-28 -> 2027-01-01
pays=np.arange(6,16)  # years after 1/1/2027
pv_today=sum(50000*DF(tau+t) for t in pays)
fwd27=pv_today/DF(tau)
unch27=sum(50000*DF(t) for t in pays)          # spot curve unchanged, as of 1/1/2027
parzero=sum(50000/(1+np.interp(t,par_t,par_y))**t for t in pays)
fwd31=pv_today/DF(tau+4); fwd33=pv_today/DF(tau+6)
unch31=sum(50000*DF(t) for t in pays-4)
ann=lambda r: sum(50000/(1+r)**k for k in range(10))
dv01=(sum(50000*DF(t)*np.exp(-0.0001*t) for t in pays)-unch27)
m100=sum(50000*DF(t)*(1.01)**t/(1+0)**0 for t in pays)  # rough -100bp
m100=sum(50000/(1+z[t-1]-0.01)**t for t in pays)
print("zeros 2033-42:",np.round(z[5:15]*100,2))
print(f"PV today {pv_today:,.0f}; fwd 1/1/27 {fwd27:,.0f}; unchanged-curve 1/1/27 {unch27:,.0f}; par-as-zero {parzero:,.0f}")
print(f"-100bp at 1/1/27 {m100:,.0f}; DV01~{dv01:,.0f}")
print(f"2031 fwd {fwd31:,.0f} unchanged {unch31:,.0f}; 2033 fwd {fwd33:,.0f}")
print("annuity-due 5/4/3%:",[round(ann(r)) for r in (.05,.04,.03)])
print("2y floor factor",1.0481**2)
r=brentq(lambda r:300*(1+r)**6+150*(1+r)**5-626,0,.2); print("626k implied",r)
print("headroom bp:", (300000-unch27)/abs(dv01))
# range rule example: reserve locked; S31 = sleeve value; floor share a locked in 2y T
for S in (100e3,189e3,250e3):
  for a in (0.6,0.8,1.0):
    print(S,a,"floor",round(a*S*1.0481**2))
