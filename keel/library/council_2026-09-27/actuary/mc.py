import numpy as np
rng=np.random.default_rng(7); N=200000
# ---- ASSUMPTIONS (not market data) ----
MU_EQ=0.065; SIG_EQ=0.16        # equity geometric exp return, vol
R0=0.051                         # starting reserve-curve level ~ matched to sourced zero curve (5.05-5.40%)
THETA=0.040; KAPPA=0.15; SIG_R=0.010   # Vasicek long-run mean, speed, vol for the level
CF=50000
def annuity(r): # cost at 1/1/2033 of 10 pmts, first immediate, flat yield r
    k=np.arange(10); return (CF/(1+r[:,None])**k).sum(1)
def liabPV(r,year): # PV at Jan 1 of 'year' of the 10 pmts
    k=np.arange(10)+(2033-year); return (CF/(1+r[:,None])**k).sum(1)
def run(strategy,rho=0.0):
    r=np.full(N,R0); A=np.zeros(N); H=np.zeros(N)  # H = face fraction of liability hedged (units of full ladder)
    hedge_frac=np.zeros(N)
    for year in range(2027,2033):
        if year==2027: A+=300000
        if year==2028: A+=150000
        L=liabPV(r,year)
        hedgeval=hedge_frac*L
        free=A-hedgeval
        # decide target hedge fraction
        if strategy=="lock":   tgt=np.minimum(1.0, np.maximum(hedge_frac,(A)/L))  # buy up to 100%
        elif strategy=="wait": tgt=np.zeros(N)
        elif strategy=="rule":
            floor={2027:0.5,2028:0.6,2029:0.7,2030:0.85,2031:1.0,2032:1.0}[year]
            FR=A/L
            trig=np.where(FR>=1.6,1.0,np.where(FR>=1.4,0.85,np.where(FR>=1.25,0.7,0.0)))
            tgt=np.minimum(np.maximum.reduce([hedge_frac,np.full(N,floor),trig]), A/L)
        hedge_frac=tgt; hedgeval=hedge_frac*L; free=A-hedgeval
        # equity share of free assets
        if strategy=="wait":
            eqw={2027:.75,2028:.75,2029:.75,2030:.75,2031:.5,2032:.25}[year]
        else: eqw=0.85
        # simulate one year
        z1=rng.standard_normal(N); z2=rho*z1+np.sqrt(1-rho**2)*rng.standard_normal(N)
        eq=np.exp(np.log(1+MU_EQ)-SIG_EQ**2/2+SIG_EQ*z1)
        r_new=r+KAPPA*(THETA-r)+SIG_R*z2
        cash=1+r   # short/intermediate bonds earn current level (ASSUMPTION)
        free=free*(eqw*eq+(1-eqw)*cash)
        L_new=liabPV(r_new,year+1)
        hedgeval=hedge_frac*L_new   # ladder tracks liability exactly
        A=free+hedgeval; r=r_new
    cost=annuity(r); S=A-cost
    return dict(p_short=(S<0).mean(),p5=np.percentile(S,5),p1=np.percentile(S,1),med=np.median(S),p95=np.percentile(S,95),
                cost_p5=np.percentile(cost,5),cost_p95=np.percentile(cost,95),cost_med=np.median(cost))
for rho in [0.0,0.3]:
    print(f"--- rho(equity shock, rate shock)={rho} (positive = rates fall when stocks fall? no: + means rates rise with stocks)")
    for s in ["lock","rule","wait"]:
        o=run(s,rho); print(s, {k:(round(v,4) if k=='p_short' else int(v)) for k,v in o.items()})
