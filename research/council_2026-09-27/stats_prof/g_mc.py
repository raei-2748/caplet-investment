import numpy as np
rng=np.random.default_rng(7); N=200000
def reserve(r): return sum(50000/(1+r)**k for k in range(10))  # annuity-due at 2033
def run(mu_e=0.06,vol_e=0.16,r0=0.052,rvol=0.009,kappa=0.0,rho=0.0,dfree=None,c2028=150000,late_ladder=False):
    eqw=[0.75,0.75,0.75,0.75,0.60,0.40]  # 2027..2032 start-of-year weights (ASSUMED glide to ~22% by 2033)
    V=np.full(N,300000.0); r=np.full(N,r0)
    for t,w in enumerate(eqw):
        if t==1: V+=c2028
        z1=rng.standard_normal(N); z2=rho*z1+np.sqrt(1-rho**2)*rng.standard_normal(N)
        if dfree: z1=rng.standard_t(dfree,N)/np.sqrt(dfree/(dfree-2))
        dr=kappa*(r0-r)+rvol*z2
        req=np.exp(mu_e-0.5*vol_e**2+vol_e*z1)-1   # mu_e = log-mean + var/2 => arithmetic mean mu_e
        rb=r-5.0*dr   # intermediate bond, dur 5 (ASSUMED)
        V*=1+w*req+(1-w)*rb; r=np.maximum(r+dr,0.005)
    L=np.array([reserve(x) for x in r[:20000]]); L=np.interp(r,np.sort(r[:20000]),L[np.argsort(r[:20000])])
    short=V<L
    return short.mean(), np.median(V-L), np.percentile(V-L,5)
cases={
 "base mu6 vol16 rvol0.9 rw":{},
 "mean-rev k=0.15":dict(kappa=0.15),
 "rho +0.3 (eq down & rates down)":dict(rho=0.3),
 "fat tail t4":dict(dfree=4),
 "mu 4.5 (Vanguard-ish mid)":dict(mu_e=0.045),
 "vol 20":dict(vol_e=0.20),
 "no 2028 deposit":dict(c2028=0),
 "no 2028, mu4.5":dict(c2028=0,mu_e=0.045),
 "150k late -> 75k":dict(c2028=75000),
}
for k,v in cases.items():
    p,m,p5=run(**v); print(f"{k:34s} P(short)={p:.3f}  median surplus {m:,.0f}  p5 {p5:,.0f}")
