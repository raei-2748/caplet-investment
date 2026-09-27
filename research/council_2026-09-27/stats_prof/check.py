import numpy as np
from datetime import date
from scipy.stats import norm
val=date(2026,9,25); anchor=date(2027,1,1)
yf=lambda d:(d-val).days/365.25
A={1:4.49,2:4.81,5:4.98,7:5.11,10:5.17,20:5.51,30:5.49}
def build(par,shiftfn=lambda t:0.0):
    ts=sorted(par); grid=np.arange(0.5,30.01,0.5)
    p=np.interp(grid,ts,[par[t]/100 for t in ts])+np.array([shiftfn(t) for t in grid])
    df=[]
    for t,y in zip(grid,p):
        c=y/2; df.append((1-c*sum(df))/(1+c))
    g=np.r_[0,grid]; lz=np.log(np.r_[1,df])
    return lambda t: np.exp(np.interp(t,g,lz))
def pv(par,shiftfn=lambda t:0.0,years=range(2033,2043)):
    f=build(par,shiftfn); ta=yf(anchor)
    return sum(50000*f(yf(date(y,1,1)))/f(ta) for y in years)
base=pv(A); print("PV A",round(base))
dv=(pv(A,lambda t:-1e-4)-pv(A,lambda t:1e-4))/2; D=dv/base*1e4; print("DV01",round(dv,1),"dur",round(D,2))
# flat-rate checks
for r in (0.0517,0.0526,0.04):
    print("flat",r, round(sum(50000/(1+r)**(y-2027) for y in range(2033,2043))))
# 2037-42 portion
p2=pv(A,years=range(2037,2043)); print("PV 2037-42",round(p2))
# headroom and prob cost > 300k by Jan 1 (0.27y) under normal rate vol ASSUMPTION
for cost in (base,295000):
    head=(300000-cost)/dv
    for vol in (0.7,0.9,1.1):
        sd=vol*100*np.sqrt(yf(anchor))
        print(f"cost {cost:,.0f} headroom {head:.0f}bp vol {vol}%/yr sd3m {sd:.0f}bp P(cost>300k)={norm.cdf(-head/sd):.2f}")
# IEF/TLT hedge weights for duration D
for dI in (6.95,7.5):
    w=(D-dI)/(15.31-dI); print("IEF dur",dI,"TLT weight",round(w,3))
# twist test: front <=10y -50bp, 20y+ unchanged, linear 10-20
tw=lambda t: -0.005 if t<=10 else (-0.005*(20-t)/10 if t<20 else 0.0)
dL=pv(A,tw)-base
for dI,wT in ((6.95,0.35),(7.5,0.35),(6.95,0.353)):
    wI=1-wT
    # IEF ~ 8.5y avg maturity bucket gets -50bp; TLT ~ 20-30y gets 0 (approx; assumes TLT holdings >=20y)
    dH=base*(wI*dI*0.005+wT*15.31*0.0)
    print(f"twist: liab +{dL:,.0f}, hedge(IEF{dI},TLT{wT}) +{dH:,.0f}, gap {dH-dL:,.0f}")
# parallel -100 with convexity
dL100=pv(A,lambda t:-0.01)-base; print("parallel -100 liab",round(dL100))
