import numpy as np
rng=np.random.default_rng(2026)
N=200_000
# --- Sourced par yields (search snippet, close 2026-09-25): 2y 4.81,5y 4.98,7y 5.06,10y 5.17,30y 5.47
tenor=np.array([2,5,7,10,30.]); yld=np.array([4.81,4.98,5.06,5.17,5.47])/100
# ASSUMPTION: par curve used as zero(STRIPS) proxy, linear interp; curve unchanged to Jan-2027
pay_t=np.arange(6,16)  # payments 2033..2042 measured from Jan 2027
z=np.interp(pay_t,tenor,yld)
pv27=(50_000/(1+z)**pay_t).sum()
print("zero proxies",np.round(z*100,2)); print("PV at Jan-2027 of 10x50k ladder: %.0f"%pv27)
for r in (0.03,0.04,0.05):
    print("reserve cost at 2033 flat %.0f%%: %.0f"%(r*100,(50_000/(1+r)**np.arange(10)).sum()))
# ASSUMPTION stress on curve: -100bp
print("PV27 if curve -100bp: %.0f"%(50_000/(1+z-0.01)**pay_t).sum())

def sim(eq_mu, eq_sd=0.16, bd_mu=0.0498, bd_sd=0.05, rho=0.2):
    cov=[[eq_sd**2,rho*eq_sd*bd_sd],[rho*eq_sd*bd_sd,bd_sd**2]]
    # lognormal with geometric mean = mu
    L=np.linalg.cholesky(cov); e=rng.standard_normal((N,6,2))@L.T
    return np.exp(np.log1p(eq_mu)+e[...,0]), np.exp(np.log1p(bd_mu)+e[...,1])
def pct(x): return np.percentile(x,[5,10,50,90]).round(-3)

for label,eq_mu in (("JPM 6.7%",0.067),("Vanguard-blend 5.1%",0.051)):
    EQ,BD=sim(eq_mu)
    print(f"\n==== equity geo return {label} ====")
    for c2028,yr in ((150e3,2028),(150e3,2029),(75e3,2028),(0,2028)):
        # Design A: full ladder lock Jan-2027; growth sleeve with weight w
        for w in (0.6,0.8,1.0):
            v=np.full(N,300e3-pv27)
            for i,y in enumerate(range(2027,2033)):
                if y==yr: v=v+c2028
                # glide: from 2031 surplus sleeve de-risks to w_eff (2031: w*.66, 2032: w*.33) - protects 2031 range
                we = w if y<2031 else (w*0.5 if y==2031 else w*0.25)
                v=v*(we*EQ[:,i]+(1-we)*BD[:,i])
            print(f"A lock27 w={w:.0%} c={c2028/1e3:.0f}k@{yr}: facility-surplus p5/p10/p50/p90={pct(v)}  P(<0)={np.mean(v<0):.3f}")
        # Design B: team glide 75% eq through 2030 then 58/42/25..., reserve bought 2033 at random rates
        gl=[.75,.75,.75,.75,.50,.25]
        v=np.full(N,300e3)
        for i,y in enumerate(range(2027,2033)):
            if y==yr: v=v+c2028
            v=v*(gl[i]*EQ[:,i]+(1-gl[i])*BD[:,i])
        r33=np.clip(rng.normal(0.045,0.01,N),0.005,None)  # ASSUMPTION 2033 flat yield N(4.5%,1.0%)
        cost=(50_000/(1+r33[:,None])**np.arange(10)).sum(1)
        s=v-cost
        print(f"B team glide  c={c2028/1e3:.0f}k@{yr}: surplus p5/p10/p50/p90={pct(s)} P(shortfall)={np.mean(s<0):.3f} reserve p50={np.median(cost):.0f}")
