import numpy as np
# coupon reinvestment
cp=0.0526*295054
for dr in (0.02,):
    loss=sum(cp*((1.0526)**(6-t)-(1.0526-dr)**(6-t)) for t in range(1,7))
    print(f"coupons/yr {cp:,.0f}; FV loss by 2033 if reinvested 200bp lower: {loss:,.0f}")
# arithmetic vs geometric
s=.16
for m in (.067,.05):
    sl=np.sqrt(np.log(1+s**2/(1+m)**2)); med=np.exp(np.log(1+m)-sl**2/2)-1
    print(f"arith {m:.1%} -> median/geom growth {med:.2%}")
ann=lambda r: sum(50000/(1+r)**t for t in range(10))
rng=np.random.default_rng(7); N=200000
def run(m,geom=False,dep=150000,rho=0.4,Gw=(.75,.75,.75,.75,.60,.40),Lw=.70,ladder=292323):
    s=.16; sl=np.sqrt(np.log(1+s**2/(1+m)**2)); mu=np.log(1+m)-sl**2/2
    if geom: mu=np.log(1+m)
    Z=rng.standard_normal((N,6)); R=np.exp(mu+sl*Z)-1; b=.048
    G=np.full(N,300000.); Ls=np.full(N,300000.-ladder)
    for t in range(6):
        if t==1: G+=dep; Ls+=dep
        G*=1+Gw[t]*R[:,t]+(1-Gw[t])*b; Ls*=1+Lw*R[:,t]+(1-Lw)*b
    z=(Z[:,4]+Z[:,5])/np.sqrt(2); e=rng.standard_normal(N)
    r=.0526+.0125*(rho*z+np.sqrt(1-rho**2)*e); r=np.maximum(r,.005)
    cost=50000*(1-(1+r)**-10)/r*(1+r)
    fac=G-cost
    p=lambda x:np.percentile(x,[5,50,95]).round(-3)
    return (fac<0).mean(), p(fac), p(Ls)
print("case | P(G short) | G facility p5/p50/p95 | L facility (70% sleeve) p5/p50/p95")
for lab,kw in (("6.7% arith",dict(m=.067)),("6.7% geom",dict(m=.067,geom=True)),("5.0% arith",dict(m=.05)),
               ("6.7% rho=0",dict(m=.067,rho=0)),("6.7% dep 75k",dict(m=.067,dep=75000)),("6.7% dep 0",dict(m=.067,dep=0)),("5.0% dep 0",dict(m=.05,dep=0))):
    ps,g,l=run(**kw); print(f"{lab} | {ps:.3f} | {g} | {l}")
# judge stress: grow deterministic 6% to 2031
P=300000*1.06+150000; P*=1.06**3  # to 1/1/2031 ... approx
P31=(300000*1.06+150000)*1.06**3; P32=P31*(1+.6*.06+.4*.048); P33=P32*(1+.4*(-.30)+.6*.048)
print(f"stress: P2031 {P31:,.0f} P2033 {P33:,.0f} reserve@3.5% {ann(.035):,.0f} facility {P33-ann(.035):,.0f}")
