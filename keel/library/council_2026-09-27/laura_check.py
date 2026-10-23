import numpy as np
rng=np.random.default_rng(7); N=200000
# ASSUMPTIONS: equity arithmetic mean mu (JPM 2026 LTCMA 6.7% per chair memo; alt 5.0% ~Vanguard mid), vol 16% (ASSUMPTION), lognormal iid
# bonds/cash earn 4.8% (2y ~4.81% snippet 2026-09-25) -- ASSUMPTION flat
def ann(r): return sum(50000/(1+r)**k for k in range(10))
def eq_ret(mu,sig,n):
    s2=np.log(1+sig**2/(1+mu)**2); m=np.log(1+mu)-s2/2
    return np.exp(rng.normal(m,np.sqrt(s2),(N,n)))-1
rb=0.048
res_fwd=396_500  # forward-implied 2033 reserve cost from chair memo
for mu in (0.067,0.05):
  E=eq_ret(mu,0.16,6)
  for c28 in (150000,75000,0):
    # Strategy G: equity weights at start of 2027..2032
    w=[0.75,0.75,0.75,0.75,0.60,0.40]
    V=np.full(N,300000.)
    for t in range(6):
        if t==1: V+=c28
        V=V*(1+w[t]*E[:,t]+(1-w[t])*rb)
    # L: ladder 295k locked -> worth res_fwd in 2033; growth sleeve 60% equity
    G=np.full(N,5000.)
    for t in range(6):
        if t==1: G+=c28
        G=G*(1+0.6*E[:,t]+0.4*rb)
    for r33,cost in (("fwd",res_fwd),("4%",ann(.04)),("3%",ann(.03))):
        fac=V-cost
        print(f"mu={mu} c28={c28} G reserve@{r33} cost={cost:,.0f}: P(short)={np.mean(fac<0):.3f} p5={np.percentile(fac,5):,.0f} med={np.median(fac):,.0f}")
    print(f"   L facility: p5={np.percentile(G,5):,.0f} med={np.median(G):,.0f} p95={np.percentile(G,95):,.0f}")
print("annuity-due 2033 @5/4/3%:",[round(ann(r)) for r in (.05,.04,.03)])
print("IEF weight for dur 9.9:",(15.31-9.9)/(15.31-6.95),(15.31-9.9)/(15.31-7.5))
print("real value 50k 2042 @2%:",50000/1.02**15, " whole-port equity L 2028:",0.6*150/450)
