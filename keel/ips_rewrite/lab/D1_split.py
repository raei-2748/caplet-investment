# AI-generated (Claude Code), 26 Oct 2026. MODEL. Run: python3 keel/ips_rewrite/lab/D1_split.py
# Independent re-derivation (Jun): 22 Oct 2026 par curve -> bootstrapped zeros (semiannual), forward 5y yield for IBTM
import numpy as np, datetime as dt, csv
rows=list(csv.DictReader(open("/home/user/caplet-investment/keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv")))
r=rows[0]; assert r["Date"]=="10/22/2026"
ten={"1 Mo":1/12,"3 Mo":.25,"6 Mo":.5,"1 Yr":1,"2 Yr":2,"3 Yr":3,"5 Yr":5,"7 Yr":7,"10 Yr":10,"20 Yr":20,"30 Yr":30}
ts=np.array(list(ten.values())); ps=np.array([float(r[k]) for k in ten])/100
def zdf(shift=0.0):
    grid=np.arange(.5,30.01,.5); p=np.interp(grid,ts,ps)+shift/100; d=[]
    for y in p:
        c=y/2; d.append((1-c*sum(d))/(1+c))
    g=np.r_[0,grid]; lz=np.log(np.r_[1,d]); return lambda t: np.exp(np.interp(t,g,lz))
V=dt.date(2026,10,22); y=lambda a,b:(b-a).days/365.25
T27,T28,MAT=dt.date(2027,1,1),dt.date(2028,1,2),dt.date(2032,12,15)
def ladder(shift):
    f=zdf(shift); a=y(V,T27); return sum(50000*f(y(V,dt.date(k,1,1)))/f(a) for k in range(2033,2043))
f0=zdf(); t1,t2=y(V,T28),y(V,MAT); tau=t2-t1
fwd=2*((f0(t1)/f0(t2))**(1/(2*tau))-1)
print(f"ladder cost 1Jan27 (22 Oct, bootstrapped, payment-date basis): {ladder(0):,.0f}; fwd IBTM yield Jan28->Dec32 {fwd*100:.2f}% tau {tau:.2f}y")
print("shift | Jan28 IBTM yield | R=150k: IBTM buy / VT(=interest) / VT share | if the shift held from 1 Jan 2027: ladder gap, R, IBTM, VT")
for s in (-2,-1,0,1,2):
    yy=fwd+s/100; disc=(1+yy/2)**(-2*tau)
    ib=150000*disc; vt=150000-ib
    gap=max(ladder(s)-300000,0); R=150000-gap; ib2=R*disc; vt2=R-ib2
    print(f"{s:+d}pp | {yy*100:.2f}% | {ib:,.0f} / {vt:,.0f} / {vt/150000:.1%} | gap {gap:,.0f}, R {R:,.0f}, IBTM {ib2:,.0f}, VT {vt2:,.0f}")
