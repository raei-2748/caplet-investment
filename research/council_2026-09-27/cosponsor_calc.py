import numpy as np
# Construction/FX erosion 2031->2033 (sources: taiwan.md; persistence = ASSUMPTION)
cci=0.0654; cpi=0.0204; fxvol=0.047
print("2y constr erosion factor", 1/(1+cci)**2, "cpi", 1/(1+cpi)**2)
print("2y FX 1sd", fxvol*np.sqrt(2))
# floor examples at Chair's rule: S=189k, a=0.8
F=0.8*189e3*1.0985; print("floor", F, "floor in 2031 constr-$", F/(1+cci)**2)
# spot vs 2y forward TWD
print("fwd discount", 30.09/31.76-1)
# operating erosion: real gap if residency costs grow at CPI 2.04% from 2033
g=sum(50e3*((1+cpi)**k-1) for k in range(10)); print("cum real gap 2033-42 @2.04%", g)
g2=sum(50e3*((1+cci)**k-1) for k in range(10)); print("cum gap if costs grow 6.54%", g2)
# Strategy G 2031->2033 facility as residual, MC (ALL ASSUMPTIONS: equity mu 6.7% arith, vol16%;
# bonds 4.81%; avg equity 50% over glide; rate shock on reserve sd 1.0pp over 2y, duration ~ 4.6 for annuity-due 10 @5%?)
rng=np.random.default_rng(1); N=200000
def L(r): return sum(50e3/(1+r)**k for k in range(10))
L0=L(0.0513)  # ~ forward-consistent 396k check
print("L2033 at 5.13%", L0)
for P31 in [500e3, 560e3]:
    eq=rng.normal(0.067,0.16,(N,2)); w=np.array([0.625,0.375])
    grow=np.prod(1+w*eq+(1-w)*0.0481,axis=1)
    P33=P31*grow
    dr=rng.normal(0,0.01,N)
    L33=np.array([L0])  # placeholder
    Lr=np.vectorize(L)(0.0513+dr[:20000])
    fac=P33[:20000]-Lr
    q=np.percentile(fac,[5,10,25,50,75,90])
    print("P31",P31,"facility pct 5/10/25/50/75/90",q.round(-3),"P(fac<0)",(fac<0).mean(),
          "P(fac< 0.5*median)",(fac<0.5*q[3]).mean())
    # 80% range width
    print(" 80% range", q[1].round(-3), q[5].round(-3))
