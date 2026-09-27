import numpy as np
from datetime import date
from scipy.optimize import brentq
val=date(2026,9,25); yf=lambda d:(d-val).days/365.25
def build(par,sh=lambda t:0):
    ts=sorted(par); grid=np.arange(0.5,30.01,0.5)
    p=np.interp(grid,ts,[par[t]/100 for t in ts])+np.array([sh(t) for t in grid])
    df=[]
    for c in p/2: df.append((1-c*sum(df))/(1+c))
    g=np.r_[0,grid]; lz=np.log(np.r_[1,df]); return lambda t: np.exp(np.interp(t,g,lz))
A={1:4.49,2:4.81,5:4.98,7:5.11,10:5.17,20:5.51,30:5.49}
B={0.5:3.79,1:3.80,2:3.88,3:3.90,5:4.01,7:4.20,10:4.39,20:4.97,30:4.96}
yrs=range(2033,2043); ta=yf(date(2027,1,1))
def rungs(par,sh=lambda t:0,anchor=date(2027,1,1)):
    f=build(par,sh); a=yf(anchor); return {y:50000*f(yf(date(y,1,1)))/f(a) for y in yrs}
# (a) sizes of "the reserve"
r=rungs(A); cost=sum(r.values())
mv33=sum(rungs(A,anchor=date(2033,1,1)).values())
print(f"cost 1/1/27 {cost:,.0f}; fwd MV 1/1/33 {mv33:,.0f}; face 500,000")
for lbl,rr in (("2033 MV if 2033 flat 7%",sum(50000/1.07**(y-2033) for y in yrs)),("flat 3%",sum(50000/1.03**(y-2033) for y in yrs))): print(lbl,f"{rr:,.0f}")
# (b) long-first lock rule
def lock(par,sh=lambda t:0,cash=300000):
    rr=rungs(par,sh); left=cash; bought=[]
    for y in sorted(yrs,reverse=True):
        if rr[y]<=left: left-=rr[y]; bought.append(y)
        else: part=left/rr[y]; left=0; bought.append(f"{y}:{part:.0%}"); break
    return sum(rr.values()),bought,sum(rr.values())-cash
for lbl,par,sh in (("A",A,lambda t:0),("A-50",A,lambda t:-.005),("A-100",A,lambda t:-.01),("B",B,lambda t:0)):
    c,b,gap=lock(par,sh); print(lbl,f"cost {c:,.0f} gap {max(gap,0):,.0f}",b[-2:])
# gap under A-100 filled Jan 2028: value of the gap-rungs 1 yr later if rates fall another 100bp in 2027
c,b,gap=lock(A,lambda t:-.01)
g28=sum(rungs(A,lambda t:-.01,anchor=date(2028,1,1))[y] for y in (2033,2034))
g28b=sum(rungs(A,lambda t:-.02,anchor=date(2028,1,1))[y] for y in (2033,2034))
print(f"2033-34 rungs cost Jan2028 at A-100 {g28:,.0f}, at A-200 {g28b:,.0f}")
# flat 4% whole ladder
print("flat4 cost",f"{sum(50000/1.04**(y-2027) for y in yrs):,.0f}")
# (c) key-rate hedge IEF/TLT/cash for twist
base=cost; tw=lambda t: -0.005 if t<=10 else (-0.005*(20-t)/10 if t<20 else 0.0)
dL_tw=sum(rungs(A,tw).values())-base
dv01=(sum(rungs(A,lambda t:-1e-4).values())-sum(rungs(A,lambda t:1e-4).values()))/2; DL=dv01/base*1e4
for dI in (6.95,7.5):
    wI=dL_tw/(base*dI*0.005); wT=(DL-wI*dI)/15.31; wC=1-wI-wT
    old=base*(0.65*dI*0.005)
    print(f"IEF dur {dI}: liab twist +{dL_tw:,.0f}; 3-fund IEF {wI:.2f} TLT {wT:.2f} cash {wC:.2f}; 65/35 gap {old-dL_tw:,.0f}")
# (d) coupon ladder reinvestment: dedicate annual-coupon bonds, coupon = zero-ish rate
f=build(A); cp={y:0.051+0.0035*(y-2033)/9 for y in yrs}  # ASSUMPTION coupons 5.10->5.45%
face={}; 
for y in sorted(yrs,reverse=True):
    later=sum(face[z]*cp[z] for z in face)  # coupons from later bonds paid in year y
    face[y]=(50000-later)/(1+cp[y])
pre=sum(face[y]*cp[y] for y in yrs)  # annual coupon flow 2028-2033 (6 coupons, last one at Jan 2033 counted in dedication? approx)
print(f"coupon ladder face {sum(face.values()):,.0f}; annual coupons pre-2033 {pre:,.0f}; 6 yrs={6*pre:,.0f}")
fv=lambda r: sum(pre*(1+r)**(2033-y) for y in range(2028,2033))
print(f"FV of 5 pre-2033 coupons at 4.8% {fv(.048):,.0f} vs 2.8% {fv(.028):,.0f}: shortfall {fv(.048)-fv(.028):,.0f}")
# (e) equity share after 2028 with 70% sleeve
sleeve=7677*1.048+150000; print(f"total equity share 2028: {0.7*sleeve/(sleeve+cost*1.051):.0%}")
