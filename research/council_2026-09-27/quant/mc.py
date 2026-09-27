"""Annual-step Monte Carlo, 1/1/2027 (t=0) .. 1/1/2033 (t=6). Payments 2033..2042 then fixed via Treasury ladder.
Rates: parallel shift X_t of today's bootstrapped zero curve, AR(1): X_t = phi X_{t-1} + sig_r * e_r.
Equity: annual log return ~ mu_l + sig_e * e_e (normal or scaled Student-t), corr(e_e, e_r)=rho.
Bond sleeve in growth portfolio: Treasury fund, duration Db, return = y_{t-1} - Db*dX + 0.5*C*dX^2.
STRIPS held to maturity: marked at df(T - t, X_t)."""
import numpy as np
from curve import zero, df
PAY=np.arange(6,16)   # payment times (yrs after 1/1/2027)
def simulate(n=100_000, seed=20260927, g=0.067, sig_e=0.16, sig_r=0.009, phi=0.9, rho=0.0,
             X0=0.0, tdf=None, glide=(.75,.75,.75,.75,.50,.25), Db=5.0, contrib2=150e3):
    rng=np.random.default_rng(seed)
    er=rng.standard_normal((n,6))
    ez=rng.standard_normal((n,6))
    if tdf: # scaled student-t, unit variance
        ez=rng.standard_t(tdf,(n,6))/np.sqrt(tdf/(tdf-2))
    ee=rho*er+np.sqrt(1-rho**2)*ez
    X=np.zeros((n,7)); X[:,0]=X0
    for t in range(1,7): X[:,t]=phi*X[:,t-1]+sig_r*er[:,t-1]
    mu_l=np.log(1+g)       # g = expected GEOMETRIC (median) annual return
    Req=np.exp(mu_l+sig_e*ee)-1
    y5=zero(Db)+X[:,:-1]; dX=np.diff(X,axis=1)
    Rb=y5 - Db*dX + 0.5*(Db**2+Db)*dX**2
    return dict(X=X,Req=Req,Rb=Rb,n=n,glide=glide,contrib2=contrib2)
def liab_pv(t,X,pays):   # value at time t of payments at times `pays` (>=t)
    return sum(50000*df(p-t,X) for p in pays)
def run(S, strat, lock_trigger=1.25):
    n=S['n'];X=S['X'];Req=S['Req'];Rb=S['Rb'];gl=S['glide']
    grow=np.full(n,300e3); locked=np.zeros((n,10),bool)
    rec={}
    def lock(mask,k,t):
        nonlocal grow
        cost=50000*df(PAY[k]-t,X[:,t])
        m=mask & ~locked[:,k] & (grow>=cost)
        grow=np.where(m,grow-cost,grow); locked[m,k]=True
    for t in range(0,6):
        if t==1: grow=grow+S['contrib2']
        if strat=='c':               # full early defeasance as soon as affordable
            for k in range(10): lock(np.ones(n,bool),k,t)
        if strat=='b':               # calendar ladder + trigger
            sched={0:[0,1,2,3],1:[4,5],2:[6],3:[7],4:[8],5:[9]}
            for k in sched[t]: lock(np.ones(n,bool),k,t)
            unl=[k for k in range(10) if True]
            pv_unl=sum(np.where(~locked[:,k],50000*df(PAY[k]-t,X[:,t]),0) for k in range(10))
            trig=grow>=lock_trigger*pv_unl
            for k in range(10): lock(trig,k,t)
        if t==4:   # 1/1/2031 snapshot
            lockedval=sum(np.where(locked[:,k],50000*df(PAY[k]-t,X[:,t]),0) for k in range(10))
            unl=sum(np.where(~locked[:,k],50000*df(PAY[k]-t,X[:,t]),0) for k in range(10))
            rec['A2031']=grow-unl       # surplus (mark-to-market) at 2031
            rec['V2031']=grow+lockedval
        w=gl[t]; grow=grow*(1+w*Req[:,t]+(1-w)*Rb[:,t])
    # 1/1/2033: buy remaining ladder at market
    need=sum(np.where(~locked[:,k],50000*df(PAY[k]-6,X[:,6]),0) for k in range(10))
    rec['R2033_mkt']=sum(50000*df(PAY[k]-6,X[:,6]) for k in range(10))
    rec['surplus']=grow-need
    rec['funded']=rec['surplus']>=0
    rec['locked_by_2027']=locked.sum(1)
    return rec
def pct(a,q=(5,25,50,75,95)): return np.percentile(a,q)
