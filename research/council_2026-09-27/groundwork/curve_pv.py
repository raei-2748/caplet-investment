import numpy as np
from datetime import date
val=date(2026,9,25); anchor=date(2027,1,1)
yf=lambda d:(d-val).days/365.25
def build(par):  # par: {tenor: pct}, semiannual BEY; bootstrap on 0.5y grid, linear interp in par
    ts=sorted(par); grid=np.arange(0.5,30.01,0.5)
    p=np.interp(grid,ts,[par[t]/100 for t in ts])
    df=[]
    for i,(t,y) in enumerate(zip(grid,p)):
        c=y/2; df.append((1-c*sum(df))/(1+c))
    grid=np.r_[0,grid]; df=np.r_[1,df]
    lz=np.log(df)
    return lambda t: np.exp(np.interp(t,grid,lz))  # log-linear DF interp
def pv(par,shift=0):
    f=build({k:v+shift for k,v in par.items()})
    ta=yf(anchor)
    return sum(50000*f(yf(date(y,1,1)))/f(ta) for y in range(2033,2043))
curves={
 "A: Sep-25-2026 (search snippets; 1y,7y,20y from Sep-23 PrimeRates +0.06)":
   {1:4.49,2:4.81,5:4.98,7:5.11,10:5.17,20:5.51,30:5.49},
 "B: conflicting 'Treasury page' snippet (date unclear)":
   {0.5:3.79,1:3.80,2:3.88,3:3.90,5:4.01,7:4.20,10:4.39,20:4.97,30:4.96},
}
for n,c in curves.items():
    base=pv(c); print(n); print(f"  PV base {base:,.0f}")
    for s in (-1,-.5,.5,1): print(f"  shift {int(s*100):+d}bp: {pv(c,s):,.0f}  ({pv(c,s)-base:+,.0f})")
    dv01=(pv(c,-.01)-pv(c,.01))/2; print(f"  DV01 {dv01:,.2f}; eff dur {dv01/base*1e4:.2f}y")
    f=build(c); ta=yf(anchor)
    print("  implied zero (semi) 2033/2037/2042 from anchor:",[round(2*((f(ta)/f(yf(date(y,1,1))))**(1/(2*(yf(date(y,1,1))-ta)))-1)*100,3) for y in (2033,2037,2042)])
    print(f"  flat rate matching $295k:", end=" ")
    from scipy.optimize import brentq
    g=lambda r: sum(50000/(1+r)**(y-2027) for y in range(2033,2043))-295000
    print(f"{brentq(g,0.001,0.2)*100:.2f}% annual")
