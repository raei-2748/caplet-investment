from mc import *
S=simulate(); ra,rb,rc=run(S,'a'),run(S,'b'),run(S,'c')
for n,r in zip('abc',(ra,rb,rc)):
    sp=r['surplus']; print(n,"mean",round(sp.mean()),"sd",round(sp.std()),"P(sp<100k)",round((sp<1e5).mean(),3),"P(sp<50k)",round((sp<5e4).mean(),3), "locked@2027 mean",r['locked_by_2027'].mean())
print("P(a facility > c facility)",(ra['surplus']>rc['surplus']).mean())
# conditional 90% range for c given A2031 at its median and quartiles
A=rc['A2031']; sp=rc['surplus']; q05,q95=np.percentile(sp/A,[5,95])
for a in np.percentile(A,[10,50,90]): print("A2031",round(a),"-> 90% range",round(q05*a),round(q95*a))
print("A2031 pctiles c:",np.round(np.percentile(A,[5,25,50,75,95])))
# seed stability
for sd in [1,2,3]:
    r=run(simulate(seed=sd),'a'); print("seed",sd,"P(a)",r['funded'].mean(), "median c", np.median(run(simulate(seed=sd),'c')['surplus']).round())
# c with higher-risk surplus sleeve (full equity until 2031)
S2=simulate(glide=(1,1,1,1,.5,.25)); r=run(S2,'c'); print("c eq100 surplus pct",np.round(pct(r['surplus'])/1e3), "q05 ratio",np.percentile(r['surplus']/r['A2031'],5).round(2))
S3=simulate(glide=(1,1,1,1,1,1)); r=run(S3,'c'); print("c eq100 no glide pct",np.round(pct(r['surplus'])/1e3))
# team claim: 20% drawdown
print("team: 626k*0.8=",626*0.8,"; our a: V2033 median",round(np.median(ra['surplus']+ra['R2033_mkt'])))
