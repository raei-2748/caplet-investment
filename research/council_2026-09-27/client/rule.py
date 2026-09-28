import numpy as np
# Par CMT yields (semiannual BEY). Sources: web-search snippets (AdvisorPerspectives 2026-09-25: 2y 4.81, 10y 5.17;
# 30y 5.49 Forbes 2026-09-25; 5y 4.99, 7y 5.05, 20y 5.45 as of 2026-09-23 search snippet). Linear interp = ASSUMPTION.
T=np.array([2,5,7,10,20,30.]); Y=np.array([4.81,4.99,5.05,5.17,5.45,5.49])/100
grid=np.arange(0.5,30.01,0.5); par=np.interp(grid,T,Y); D=[]
for i,t in enumerate(grid):
    c=par[i]/2; D.append((1-c*sum(D))/(1+c))
D=np.array(D)
df=lambda t: np.exp(np.interp(t,np.r_[0,grid],np.r_[0,np.log(D)]))
z=lambda t: df(t)**(-1/t)-1   # annual-compounded zero
print("zeros (annual comp) 2..11y:",{k:round(100*z(k),2) for k in range(2,12)})
# ASSUMPTION: in 2031 the curve has the same shape/level as today -> reserve cost at 1/1/2031 for pmts at t=2..11
L31=sum(50000*df(k) for k in range(2,12)); print(f"L31 (cost 1/1/2031 of 10x50k, 2033-42) base: {L31:,.0f}")
for s in (-0.015,0.015):
    Ls=sum(50000/(1+z(k)+s)**k for k in range(2,12)); print(f"  L31 if zeros {s*1e4:+.0f}bp: {Ls:,.0f}")
y2=z(2); print(f"2y zero {y2:.4f}; PV of $1 floor paid 2033 = {1/(1+y2)**2:.4f}")
# Rule: S = V31 - L31 ; lock floor PV = a*S into 2y zero ; risky sleeve = (1-a)*S ; 2033 contribution = F + c*sleeve_2033
a,c=0.5,0.5
mu,sig=0.055,0.16  # ASSUMPTION: diversified equity sleeve 5.5% geometric-ish, 16% vol (see report)
rng=np.random.default_rng(7); n=200000
g=np.exp((np.log(1+mu)-sig**2/2)*2+sig*np.sqrt(2)*rng.standard_normal(n))  # 2-yr growth factor, lognormal
print(f"P(2yr equity loss)={np.mean(g<1):.2%}, 5th pct factor {np.percentile(g,5):.3f}, 90th {np.percentile(g,90):.3f}")
print("V31 | surplus S | floor F(2033) | upper U=F+c*sleeve p90 | median contrib | P(contrib>=F) | P(F<=contrib<=U) | flex retained median")
for V in [450e3,500e3,550e3,600e3,650e3,700e3]:
    S=V-L31
    if S<=0: print(f"{V:,.0f} | {S:,.0f} | 0 -> reserve shortfall, promise nothing"); continue
    F=a*S*(1+y2)**2; sleeve=(1-a)*S*g; contrib=F+c*sleeve
    U=F+c*np.percentile(sleeve,90)
    print(f"{V:,.0f} | {S:,.0f} | {F:,.0f} | {U:,.0f} | {np.median(contrib):,.0f} | {np.mean(contrib>=F-1):.1%} | {np.mean(contrib<=U):.1%} | {np.median((1-c)*sleeve):,.0f}")
# FX: USD/TWD 31.787 (2026-09-24 snippet). Covered-interest-parity 2y forward using ASSUMED TWD 2y rate = CBC policy 2.0%
spot=31.787; fwd=spot*(1.02/(1+y2))**2; print(f"indicative 2y fwd USD/TWD {fwd:.2f} ({fwd/spot-1:+.1%})")
for vol in (0.05,0.07):
    lo=spot*np.exp(-1.645*vol*np.sqrt(2)); print(f"  vol {vol:.0%}: 5th pct USD/TWD in 2y ~{lo:.2f} ({lo/spot-1:+.1%})")
# Taiwan inflation erosion of fixed $50k (TWD terms, ASSUMPTION 2%/yr, CBC 2027 fcst 1.8%)
for yr in (2033,2042): print(yr, f"real value in 2026 prices at 2%: {50000/1.02**(yr-2026):,.0f}")
# CPPI-style check of pre-2031 risk budget: PV at 1/1/2027 of liability (fwd) vs 300k
L27=sum(50000*df(k) for k in range(6,16))/1.0  # payments at t=6..15 from 1/1/2027, today's curve as ASSUMPTION
print(f"PV at 1/1/2027 of 10x50k (curve assumed unchanged): {L27:,.0f}")
