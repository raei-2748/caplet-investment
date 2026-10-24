import sys, datetime as dt
from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'scripts'))
import ladder_pv as L
import numpy as np
from datetime import date
L.VAL=date(2026,10,22)
L.CURVE={1/12:4.11,2/12:4.16,.25:4.22,.5:4.29,1:4.41,2:4.65,3:4.72,5:4.78,7:4.86,10:4.96,20:5.32,30:5.29}
c=L.cost(); d=(L.cost(-.01)-L.cost(.01))/2
print("cost",round(c),"head",round(300000-c),"dv01",round(d),"bp",(300000-c)/d)
for s in (-1,-.5,.5,1,2): print("shift",s,round(L.cost(s)-c))
# per-payment cost & dv01
f=L.build(L.CURVE); a=L.yf(L.ANCHOR)
tot=0
for y in range(2033,2043):
    pv=lambda sh:50000*L.build({k:v+sh for k,v in L.CURVE.items()})(L.yf(date(y,1,1)))/L.build({k:v+sh for k,v in L.CURVE.items()})(a)
    dv=(pv(-.01)-pv(.01))/2; tot+=dv
    print(y,round(pv(0)),round(dv,1),round(pv(0)/50000,3))
# reserve DV01 by year: remaining payments valued at 1 Jan Y
print("reserve dv01 by year (parallel shift of curve, remaining payments, fwd valued)")
for Y in range(2027,2043):
    def val(sh):
        g=L.build({k:v+sh for k,v in L.CURVE.items()})
        return sum(50000*g(L.yf(date(y,1,1)))/g(L.yf(date(Y,1,1))) for y in range(max(2033,Y),2043))
    print(Y,round((val(-.01)-val(.01))/2),round(val(0)))
# cost per dollar, IRR
print("cost/$",c/500000)

def brentq(fn,a,b):
    for _ in range(100):
        m=(a+b)/2
        if fn(a)*fn(m)<=0: b=m
        else: a=m
    return m

irr=brentq(lambda r:sum(50000/(1+r)**t for t in range(6,16))-300000,0.001,.2); print("irr 300k",irr)
irr2=brentq(lambda r:sum(50000/(1+r)**t for t in range(6,16))-c,0.001,.2); print("irr at cost",irr2)
# duration-weighted avg yield: zero rates
for t in (6,9,10.5,12,15):
    print(t,"zero",(1/f(L.yf(date(2027,1,1))+t) *f(L.yf(date(2027,1,1))))**(-1/t)-1 if False else (f(a)/f(a+t))**(1/t)-1)
# fund breakeven: floor 140-145, top 168, fund 32-40
for fund in (32,35,40):
  for floor,top in ((145,168),(140,168)):
    room=top-floor; need=2*room
    print("fund",fund,"floor",floor,"top",top,"needs",need,"growth",need/fund-1,"cagr5y",(need/fund)**(1/5)-1,"cagr 3y(2028-31 or to 2033 5y)")
# range top conditional: quote 2031 top =floor+half fund_2031; gift cap -> reach top if no fall 2031-33
# 5y 7%/16.8%: P(fund_2033 >= fund_2031 target)? not needed
# cap binds: P(fund_2033 half >= room) with room defined as top-floor where top defined from fund at 2031 => only 2031-33
# lognormal P(fund_5y*0.5>=28) 
from math import log,sqrt
from math import erf
class norm:
    cdf=staticmethod(lambda x:0.5*(1+erf(x/sqrt(2))))
for fund,room in ((40,28),(32,23),(35,28)):
  mu=log(1.07)-0.5*0.168**2; s=0.168
  T=5; x=log(2*room/fund)
  print("P(half fund>=room)",fund,room,1-norm.cdf((x-mu*T)/(s*sqrt(T))))
# actual maturities vs payment date
print(dt.date(2027,1,1).strftime('%A'), dt.date(2033,1,1).strftime('%A'))
mat=[("IBTM",date(2032,12,31)),("IBTO",date(2033,12,31)),("IBTP",date(2034,12,31)),("IBTQ",date(2035,12,31)),("IBTR",date(2036,12,31)),("Feb37",date(2037,2,15)),("May38",date(2038,5,15)),("Nov39",date(2039,11,15)),("Nov40",date(2040,11,15)),("Nov41",date(2041,11,15))]
for i,(n,m) in enumerate(mat):
    p=date(2033+i,1,1); print(n,m,p,(p-m).days)
