import numpy as np
rng=np.random.default_rng(7);N=200_000
def run(eq_mu,bd_mu,w,glide=True,eq_sd=0.16):
    cov=[[eq_sd**2,.2*eq_sd*.05],[.2*eq_sd*.05,.05**2]];L=np.linalg.cholesky(cov)
    e=rng.standard_normal((N,6,2))@L.T;EQ=np.exp(np.log1p(eq_mu)+e[...,0]);BD=np.exp(np.log1p(bd_mu)+e[...,1])
    v=np.full(N,2255.);out={}
    for i,y in enumerate(range(2027,2033)):
        if y==2028: v=v+150e3
        if y==2031: out['v31']=v.copy()
        we=w if (not glide or y<2031) else (w*.5 if y==2031 else w*.25)
        v=v*(we*EQ[:,i]+(1-we)*BD[:,i])
    out['v33']=v;return out
for eq,bd,lab in ((0.067,0.040,"JPM eq 6.7 / JPM intTsy 4.0"),(0.051,0.040,"Vang eq 5.1 / 4.0"),(0.067,0.0498,"JPM eq / 5y yield 4.98")):
  for w in (0.4,0.7,1.0):
    for g in (True,False):
      o=run(eq,bd,w,g);p=np.percentile(o['v33'],[5,10,50,90]).round(-3)
      print(f"{lab:28s} w={w:.0%} glide={g!s:5}: p5/p10/p50/p90={p} mean={o['v33'].mean():.0f}")
# 2031 conditional range: ratio v33/v31 with w=.7 glide
o=run(0.067,0.040,0.7,True);r=o['v33']/o['v31'];print("2031->2033 multiplier p5/p10/p50/p90",np.percentile(r,[5,10,50,90]).round(3))
print("floor factor if 60% of V31 in 2y Tsy at 4.81%:",round(0.6*1.0481**2,3))
