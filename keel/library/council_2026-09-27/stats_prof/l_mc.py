import numpy as np
rng=np.random.default_rng(7); N=200000
for eq,mu in ((0.6,0.08),(0.6,0.06),(0.7,0.06),(0.6,0.045),(0.75,0.06)):
    S=np.full(N,7677.0); r=np.full(N,0.052)
    ws=[eq,eq,eq,eq,eq*0.8,eq*0.6]
    for t,w in enumerate(ws):
        if t==1: S+=150000
        z1=rng.standard_normal(N); dr=0.009*rng.standard_normal(N)
        req=np.exp(mu-0.5*0.16**2+0.16*z1)-1; rb=r-5*dr
        S*=1+w*req+(1-w)*rb; r=np.maximum(r+dr,0.005)
    print(f"L sleeve eq{eq} mu{mu}: median {np.median(S):,.0f} p5 {np.percentile(S,5):,.0f} p95 {np.percentile(S,95):,.0f}  P(reserve short)=0")
