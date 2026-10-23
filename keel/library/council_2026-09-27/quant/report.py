from mc import *
import numpy as np, itertools
np.set_printoptions(suppress=True)
def summ(S,label):
    out={}
    for s in 'abc':
        r=run(S,s); sp=r['surplus']
        A=r['A2031']; ok=A>0
        ratio=sp[ok]/A[ok]; q05,q95=np.percentile(ratio,[5,95])
        # floor holding 95%: F = q05*A2031 ; check frequency
        hold=np.mean(sp[ok]>=q05*A[ok])
        out[s]=(r['funded'].mean(), pct(np.maximum(sp,0)), q05,q95, ok.mean(), np.median(A))
        print(f"{label:28s} {s}: P(all10)={r['funded'].mean():.4f}  Facility p5/25/50/75/95 = {np.round(pct(np.maximum(sp,0))/1e3,0)}k"
              f"  floor ratio q05={q05:.2f} q95={q95:.2f}  medA2031={np.median(A)/1e3:.0f}k P(A2031>0)={ok.mean():.3f}")
    return out
base=simulate()
print("seed 20260927, n=100000")
summ(base,"BASE g=6.7% vol16 rv.9")
r=run(base,'a'); print("2033 reserve cost pctiles (k):",np.round(pct(r['R2033_mkt'])/1e3,0))
for kw,lab in [(dict(g=0.042),"g=4.2% (Vgd low)"),(dict(g=0.052),"g=5.2% (Vgd mid)"),(dict(g=0.078),"g=7.8%"),
               (dict(sig_e=0.20),"eq vol 20%"),(dict(tdf=4),"fat tails t4"),(dict(sig_r=0.015),"rate vol 150bp"),
               (dict(rho=-0.3),"rho(eq,dy)=-0.3"),(dict(X0=-0.01),"start curve -100bp"),(dict(X0=0.01),"start curve +100bp"),
               (dict(contrib2=0),"2028 contrib = 0"),(dict(contrib2=75e3),"2028 contrib=75k")]:
    summ(simulate(**kw),lab)
# floor-lock variant: in 2031, lock floor = q05*A2031 of (c) into 2y zero -> certain
