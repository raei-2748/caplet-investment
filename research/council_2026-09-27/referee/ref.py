import numpy as np, sys
from datetime import date
from scipy.stats import norm
sys.path.insert(0,'/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/groundwork')
val=date(2026,9,25); anchor=date(2027,1,1); yf=lambda d:(d-val).days/365.25
def build(par):
    ts=sorted(par); grid=np.arange(0.5,30.01,0.5); p=np.interp(grid,ts,[par[t]/100 for t in ts]); df=[]
    for y in p: c=y/2; df.append((1-c*sum(df))/(1+c))
    grid=np.r_[0,grid]; lz=np.log(np.r_[1,df]); return lambda t: np.exp(np.interp(t,grid,lz))
A={1:4.49,2:4.81,5:4.98,7:5.11,10:5.17,20:5.51,30:5.49}
B={0.5:3.79,1:3.80,2:3.88,3:3.90,5:4.01,7:4.20,10:4.39,20:4.97,30:4.96}
def rungs(par,shift=0,short_only=None):
    c={k:v+(shift if (short_only is None or k<=short_only) else 0) for k,v in par.items()}
    f=build(c); ta=yf(anchor)
    return {y:50000*f(yf(date(y,1,1)))/f(ta) for y in range(2033,2043)}
pv=lambda par,s=0: sum(rungs(par,s).values())
print("== 1 Reserve cost at 1/1/2027 (forward, today's curve)")
for n,c in (("A",A),("B",B)):
    b=pv(c); d=(pv(c,-.01)-pv(c,.01))/2
    print(f"{n}: {b:,.0f}  DV01 {d:.0f}  dur {d/b*1e4:.2f}  -50bp {pv(c,-.5):,.0f} -100bp {pv(c,-1):,.0f}")
ann=lambda r,n=10,due=True: sum(50000/(1+r)**(t) for t in range(n))  # value AT first payment date
for r in (.04,.0517,.0526):
    print(f"flat {r:.2%} value at 1/1/2027 (6y before first pmt): {ann(r)/(1+r)**6:,.0f}")
print("headroom at A:",300000-pv(A),"bp:",(300000-pv(A))/289)
# pre-Jan risk
for sd in (36,57):
    print(f"P(fall>27bp) sd{sd}: {norm.sf(27/sd):.2f}; P(fall>17bp): {norm.sf(17/sd):.2f}")
print("== reserve value on 1/1/2033 (value of 10 remaining pmts incl. the one due that day)")
f=build(A); t33=yf(date(2033,1,1))
mv33=sum(50000*f(yf(date(y,1,1)))/f(t33) for y in range(2033,2043)); print("forward-implied:",round(mv33))
for r in (.03,.035,.04,.0526,.07): print(f" flat {r:.2%}: {ann(r):,.0f}")
print("== long-rungs-first allocation: fraction of 2033 / 2034 rung bought with $300k")
for lab,c,s in (("A",A,0),("A-50",A,-.5),("B",B,0),("A-100",A,-1),("A-47",A,-.47)):
    rg=rungs(c,s); budget=300000; cov={}
    for y in range(2042,2032,-1):
        x=min(1,budget/rg[y]); cov[y]=x; budget-=x*rg[y]
    gap=sum(rg.values())-300000
    print(f"{lab}: cost {sum(rg.values()):,.0f} gap {max(gap,0):,.0f} 2033 {cov[2033]:.0%} 2034 {cov[2034]:.0%} ; 2033 rung PV {rg[2033]:,.0f}")
# flat 4%
rg={y:50000/1.04**(y-2027) for y in range(2033,2043)}; b=300000;cov={}
for y in range(2042,2032,-1): x=min(1,b/rg[y]); cov[y]=x; b-=x*rg[y]
print("flat4%:",round(sum(rg.values())),{k:round(v,2) for k,v in cov.items() if v<1})
print("== IEF/TLT duration match")
DL=9.90; DT=15.31
for DI in (6.95,7.5):
    w=(DT-DL)/(DT-DI); print(f"IEF dur {DI}: IEF {w:.3f} TLT {1-w:.3f}")
# twist: rates <=10y -50bp, 20y+ unchanged. model IEF as 8y par bond, TLT as 25y par bond (ASSUMPTION)
def bond_pv(f,T,cpn,t0=0):
    ts=np.arange(0.5,T+1e-9,0.5); return sum(cpn/2*f(t) for t in ts)+f(T)
fA=build(A); fT=build({k:v+(-0.5 if k<=10 else 0) for k,v in A.items()})
L0=sum(rungs(A).values()); L1=sum(rungs(A,-.5,short_only=10).values())
res=[]
for DI,TI in ((6.95,8.1),(7.5,8.8)):
    # pick IEF maturity so its duration ≈ DI
    def dur(T,c):
        y=c; ts=np.arange(0.5,T+1e-9,.5); cf=np.full(len(ts),y/2); cf[-1]+=1; d=(1+y/2)**(-2*ts); return (ts*cf*d).sum()/(cf*d).sum()/(1+y/2)
    Ti=min(np.arange(6,10.01,0.1),key=lambda T:abs(dur(T,0.051)-DI)); Tt=min(np.arange(18,30.01,0.5),key=lambda T:abs(dur(T,0.055)-DT))
    w=(DT-DL)/(DT-DI)
    gi=bond_pv(fT,Ti,.051)/bond_pv(fA,Ti,.051)-1; gt=bond_pv(fT,Tt,.055)/bond_pv(fA,Tt,.055)-1
    hedge=L0*(w*gi+(1-w)*gt)
    print(f"twist -50bp<=10y: liability +{L1-L0:,.0f}, hedge +{hedge:,.0f}, gap {L1-L0-hedge:,.0f} (IEF proxy {Ti:.1f}y, TLT proxy {Tt}y)")
print("== 2031 floor examples F=a*S*1.0481^2")
g=1.0481**2
for S in (100000,189000):
    print(S,[round(a*S*g) for a in (.6,.8,1.0)])
F=0.8*189000*g; print("real/FX: construction 2y factor",round(1/1.0654**2,3),"F in 2031 construction $",round(F/1.0654**2),"; 1sd FX 2y",round(0.047*2**.5,3))
print("== coupon ladder (ASSUMPTION flat 5.26% annual, par bonds, annual coupons)")
c=.0526; Fk={}
for y in range(2042,2032,-1):
    later=sum(Fk.values()); Fk[y]=(50000-c*later)/(1+c)
cost_par=sum(Fk.values()); pre=c*cost_par
print(f"face needed {cost_par:,.0f}; coupons/yr 2027-32 {pre:,.0f}; PV of those 6 coupons {sum(pre/(1+c)**t for t in range(1,7)):,.0f}")
print(" -> if you buy par bonds matching only 2033+ flows, the cost is", round(cost_par/(1+c)**0), "at par? (bought 1/1/2027) vs zero-ladder", round(ann(c)/(1+c)**6))
