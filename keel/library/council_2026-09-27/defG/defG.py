# Defender-of-G check. ALL inputs are ASSUMPTIONS unless noted.
# Equity: lognormal, vol 16%. 'mu' given either as arithmetic mean or as geometric (median) rate.
# Bonds/cash 4.8% (2y 4.81% snippet 2026-09-25). Ladder cost $292.3k (curve.md, snippet curve A).
# 2033 flat reserve rate ~ N(5.26%,1.25pp), corr +0.4 with 2031-32 equity log-return (judge's assumption).
import numpy as np
rng=np.random.default_rng(7); N=200_000; SIG=0.16; RB=0.048; LAD=292.3
def res_cost(r): k=np.arange(10); return (50/(1+r[:,None])**k).sum(1)
def eq(mu,geo,n):
    s2=np.log(1+SIG**2/(1+mu)**2) if not geo else SIG**2/(1+mu)**2*0+ (np.log(1+SIG**2/(1+mu)**2))
    m=np.log(1+mu) if geo else np.log(1+mu)-s2/2
    return rng.normal(m,np.sqrt(s2),(N,n))
def run(path, mu, geo, dep28=150, hedge=0.0, corr=0.4):
    z=eq(mu,geo,6)                     # log equity returns 2027..2032
    e32=z[:,4]+z[:,5]; zs=(e32-e32.mean())/e32.std()
    r33=np.clip(0.0526+0.0125*(corr*zs+np.sqrt(1-corr**2)*rng.standard_normal(N)),0.005,None)
    lock=hedge*LAD; W=np.full(N,300.0-lock)
    if W.min()<0: dep_use=-W; W=W*0
    for y in range(6):
        if y==1: W=W+dep28
        w=path[y]; W=W*(w*np.exp(z[:,y])+(1-w)*(1+RB))
    fac=W-(1-hedge)*res_cost(r33)
    return fac
def rep(lbl,f): print(f"{lbl:52s} p5 {np.percentile(f,5):7.0f}  p50 {np.median(f):6.0f}  P(short) {100*(f<0).mean():5.1f}%")
G=[.75,.75,.75,.75,.60,.40]; L=[.6]*6; G2=[1,1,1,1,.5,.5]
for mu,geo in [(0.067,False),(0.067,True),(0.05,False)]:
    t=f"eq {mu:.1%} {'geo' if geo else 'arith'}"
    print("==",t)
    rep("G original, reserve bought 2033",run(G,mu,geo))
    rep("G original, NO 2028 deposit",run(G,mu,geo,dep28=0))
    rep("L (lock Jan27, sleeve 60%)",run(L,mu,geo,hedge=1))
    rep("G-rev (lock Jan27, sleeve 100%->2031, 50% after)",run(G2,mu,geo,hedge=1))
    rep("G-rev, NO 2028 deposit",run(G2,mu,geo,dep28=0,hedge=1))
# minimum hedge ratio for P(short)<=1% with no 2028 deposit (G glide path on the unhedged money)
for h in [0.5,0.7,0.8,0.9,0.95,1.0]:
    f=run(G,0.067,True,dep28=0,hedge=h); print(f"hedge {h:.2f} no-2028 P(short) {100*(f<0).mean():5.1f}%")
# median-vs-bond: median annual equity growth when 6.7% is arithmetic
s2=np.log(1+SIG**2/1.067**2); print("median eq growth if 6.7% arith:",round(100*(np.exp(np.log(1.067)-s2/2)-1),2),"%")
