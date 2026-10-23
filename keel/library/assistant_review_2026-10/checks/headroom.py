import csv, datetime as dt, numpy as np
rows = {r['Date']: r for r in csv.DictReader(open('tsy_202610.csv'))}
pts=[(1,"1 Yr"),(2,"2 Yr"),(3,"3 Yr"),(5,"5 Yr"),(7,"7 Yr"),(10,"10 Yr"),(20,"20 Yr"),(30,"30 Yr")]
def y(c,t): return np.interp(t,[p for p,_ in pts],[float(c[k]) for _,k in pts])
mats=[dt.date(2032,12,15),dt.date(2033,12,15),dt.date(2034,12,15),dt.date(2035,12,15),dt.date(2036,12,15),
      dt.date(2037,2,15),dt.date(2038,5,15),dt.date(2039,11,15),dt.date(2040,11,15),dt.date(2041,11,15)]
base=dt.date(2026,10,6)
cost=293447.0; dv01_total=cost-0  # placeholder
# weight each rung by PV of $50k discounted at its yield (approx zero) from 2027-01-01 to payment; duration ~ years from today
c6,c9,c13=rows['10/06/2026'],rows['10/09/2026'],rows['10/13/2026']
pv=[];dur=[];dy9=[];dy13=[]
for m in mats:
    t=(m-base).days/365.25; yy=y(c6,t)/100
    p=50000/(1+yy/2)**(2*(t-0.24)); pv.append(p); dur.append(t/(1+yy/2))
    dy9.append(y(c9,t)-y(c6,t)); dy13.append(y(c13,t)-y(c6,t))
pv=np.array(pv); scale=cost/pv.sum(); pv*=scale; dur=np.array(dur)
dv01=(pv*dur).sum()*1e-4
for name,dy in (('9 Oct',dy9),('13 Oct',dy13)):
    dcost=-(pv*dur*np.array(dy)).sum()*1e-4*100
    avg=(pv*dur*np.array(dy)).sum()/(pv*dur).sum()
    print(f"{name}: DV01-weighted avg yield change {avg*100:+.1f}bp; cost change {dcost:+,.0f}; est cost {cost+dcost:,.0f}; headroom left ~{(300000-cost-dcost)/dv01:.1f}bp (DV01 ${dv01:,.0f}/bp)")
print("headroom at 6 Oct implied:", round((300000-cost)/dv01,1),"bp")
