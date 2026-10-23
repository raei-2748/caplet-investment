import datetime as dt
etf={"IBTM":(4503,21.65),"IBTO":(1024,22.86),"IBTP":(927,23.90),"IBTQ":(894,23.46),"IBTR":(853,23.24)}
bonds={"T37":(20,4.75,(8,15),(2,15),96.019),"T38":(20,4.5,(5,15),(11,15),93.076),"T39":(18,4.375,(5,15),(11,15),90.005),
"T40":(18,4.25,(5,15),(11,15),87.724),"T41":(20,3.125,(5,15),(11,15),74.955)}
etf_cost=sum(q*p for q,p in etf.values())
clean=sum(u*1000*p/100 for u,c,a,b,p in bonds.values())
def accr(d):
    tot=0
    for u,c,(m1,d1),(m2,d2),p in bonds.values():
        last=dt.date(2026,m1,d1); nxt=dt.date(2026 if m2>m1 else 2027,m2,d2)
        tot+=u*1000*(c/2/100)*(d-last).days/(nxt-last).days
    return tot
comm=6*25+5*10
for vt in (164,167):
  for d in [None]+[dt.date(2026,10,x) for x in range(5,11)]:
    a=accr(d) if d else 0
    cash=300000-etf_cost-clean-a-comm-vt*158.83
    print(vt,d,round(a,2),round(cash,2))
print("etf",round(etf_cost,2),"clean",round(clean,2))
# what VT count gives 3513.79 with no accrued / with accrued
