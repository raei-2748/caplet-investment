import numpy as np
from datetime import date
# Par CMT yields (bond-equivalent, semiannual), as of 2026-09-25 per search snippets
# 2y 4.81, 5y 4.99 (snippet, date ambiguous), 7y 5.06, 10y 5.17, 20y 5.45, 30y 5.48
T=np.array([2,5,7,10,20,30.]); Y=np.array([4.81,4.99,5.06,5.17,5.45,5.48])/100
grid=np.arange(0.5,30.01,0.5)
par=np.interp(grid,T,Y)          # linear interp of par yields (ASSUMPTION: flat below 2y)
# bootstrap semiannual zero discount factors
D=[]
for i,t in enumerate(grid):
    c=par[i]/2
    D.append((1-c*sum(D))/(1+c))
D=np.array(D)
zero=2*(D**(-1/(2*grid))-1)   # semiannual-compounded zero rate
def df(t):  # log-linear interp of DF
    return np.exp(np.interp(t,grid,np.log(D)))
def z(t): return 2*(df(t)**(-1/(2*t))-1)
val=date(2026,9,28)
pay=[date(y,1,1) for y in range(2033,2043)]
t=np.array([(p-val).days/365.25 for p in pay])
print("maturities (yrs):",np.round(t,2))
print("zero rates %:",np.round([100*z(x) for x in t],3))
cf=50000
pv=sum(cf*df(x) for x in t)
print(f"PV today of 10x50k: {pv:,.0f}")
# forward PV at 2027-01-01 and 2028-01-01
t27=(date(2027,1,1)-val).days/365.25; t28=(date(2028,1,1)-val).days/365.25
pv27=pv/df(t27); pv28=pv/df(t28)
print(f"Forward PV at 1/1/2027: {pv27:,.0f}; at 1/1/2028: {pv28:,.0f}")
# PV at 2033 using forward curve (implied cost of reserve in 2033)
t33=t[0]
L33=sum(cf*df(x) for x in t)/df(t33)
print(f"Implied forward cost of reserve at 1/1/2033 (incl first pmt): {L33:,.0f}")
for r in [0.02,0.03,0.04,0.05,0.06]:
    a=sum(cf/(1+r)**k for k in range(10)); print(f"  2033 reserve cost if flat {r:.0%}: {a:,.0f}")
# duration & shocks (parallel shift of zero curve, continuous approx via semiannual)
def pv_shift(s,ref=0.0):
    return sum(cf*(1+(z(x)+s)/2)**(-2*x) for x in t)
base=pv_shift(0)
for s in [-0.02,-0.01,0.01,0.02]:
    p=pv_shift(s); print(f"shift {s*1e4:+.0f}bp: PV {p:,.0f} ({p/base-1:+.2%})")
mod=(pv_shift(-1e-4)-pv_shift(1e-4))/(2e-4*base)
print(f"modified duration {mod:.2f}; DV01 ${base*mod*1e-4:,.0f}")
# PV-weighted Macaulay
w=np.array([cf*df(x) for x in t]); print("Macaulay dur", (w*t).sum()/w.sum())
# also discount at 1/1/2027 (forward) duration
print("dates each pay PV today:",[round(cf*df(x)) for x in t])
np.save("zc.npy",np.vstack([grid,D]))
