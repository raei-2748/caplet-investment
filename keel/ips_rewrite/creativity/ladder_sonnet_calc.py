import numpy as np
from math import log, exp, sqrt
from statistics import NormalDist
_n=NormalDist()
class norm:
    cdf=staticmethod(_n.cdf); pdf=staticmethod(_n.pdf); ppf=staticmethod(_n.inv_cdf)

# par curve 25 Sep 2026
pts={1:4.50,2:4.81,3:4.94,5:4.98,7:5.06,10:5.17,20:5.54,30:5.49}
xs=sorted(pts); 
def par(t): return np.interp(t,xs,[pts[x] for x in xs])/100
# bootstrap annual spot discount factors
df={}
for n in range(1,31):
    c=par(n); s=sum(c*df[i] for i in range(1,n))
    df[n]=(1-s)/(1+c)
spot={n:df[n]**(-1/n)-1 for n in df}
pv=sum(50000*df[t] for t in range(6,16))
print("ladder PV 1 Jan 2027 (annual bootstrap):",round(pv))
dv01=sum(50000*df[t]*t/(1+spot[t])*1e-4 for t in range(6,16)); print("DV01 per bp ~",round(dv01))
# probability ladder cost > 300k
head=300000-298000
for sd in (20,30,40,50):
    h=head/290  # bp headroom
    z=h/sd
    p=norm.cdf(-z)   # P(yield falls by more than h bp)
    # expected excess cost given fall
    ex=290*sd*(norm.pdf(z)-z*(1-norm.cdf(z)))
    print(f"3-mo yield sd {sd}bp: headroom {h:.1f}bp, P(cost>300k)={p:.2f}, E[excess]=${ex:,.0f}")
# dedicated ladder, annual coupons, faces solved from cheques, coupons before 2033 idle
def ladder(c):
    F={}
    T=list(range(6,16))
    for j in reversed(range(10)):
        later=sum(F[i] for i in range(j+1,10))
        F[j]=(50000-c*later)/(1+c)
    # price each bond at spot curve
    price=0
    wait=0
    for j in range(10):
        Tj=T[j]
        cf={t:c*F[j] for t in range(1,Tj+1)}; cf[Tj]+=F[j]
        price+=sum(v*df[t] for t,v in cf.items())
        wait+=sum(v*df[t] for t,v in cf.items() if t<6)
    return sum(F.values()),price,wait
for c in (0.052,0.03,0.015,0.0001):
    tf,pr,w=ladder(c)
    print(f"coupon {c*100:.2f}%: total face {tf:,.0f}, cost no-reinvest ladder {pr:,.0f}, PV of coupons waiting before 2033 {w:,.0f} (share {w/pr:.1%})")
# facility
T=4.9; yb=0.0498
g_b=(1+yb)**T; print("bond growth 4.9y",round(g_b,4), "floor cost per 150k face", round(150/g_b,1))
sig=0.165*sqrt(T)
for label,med in (("7.5% = compound",1.075**T),("7.5% = arithmetic mean",1.075**T/exp(0.5*0.165**2*T))):
    mu=log(med)
    z=(log(g_b)-mu)/sig
    print(label,"median growth",round(med,3),"P(shares<bonds)",round(norm.cdf(z),3))
    for s in (0,0.10,0.21,0.40,0.80):
        S=150*s; B=150-S
        floor=B*g_b
        q=lambda p: S*exp(mu+sig*norm.ppf(p))
        if label.startswith("7.5% = arith"): mean=S*1.075**T
        else: mean=S*exp(mu+0.5*sig**2)
        print(f"  shares {s:>4.0%} of $150k (${S:.0f}k): bottom ${floor:.0f}k, p5 ${floor+q(.05):.0f}k, median ${floor+q(.5):.0f}k, p95 ${floor+q(.95):.0f}k, mean ${floor+mean:.0f}k")
