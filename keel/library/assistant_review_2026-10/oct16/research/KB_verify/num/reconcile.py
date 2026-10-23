# Reconcile ladder-cost figures on the 15 Oct 2026 curve: 2 date sets x 2 curve bases. Same bootstrap as oct14/factcheck/ladder.py.
import csv, math, sys
from datetime import date
import numpy as np
T={"6 Mo":.5,"1 Yr":1,"2 Yr":2,"3 Yr":3,"5 Yr":5,"7 Yr":7,"10 Yr":10,"20 Yr":20,"30 Yr":30}
rows={r["Date"]:r for r in csv.DictReader(open(sys.argv[1]))}
def boot(day,shift=0):
    p=sorted((T[k],float(rows[day][k])/100) for k in T); ts=np.array([a for a,b in p]); ys=np.array([b for a,b in p])+shift
    g=np.arange(0.5,30.0001,0.5); par=np.interp(g,ts,ys); d=[]
    for c in par: d.append((1-c/2*sum(d))/(1+c/2))
    return g,np.array(d)
def df(g,d,t):
    if t<=0: return 1.0
    z=-np.log(d)/g; return math.exp(-np.interp(t,g,z)*t)
yf=lambda a,b:(b-a).days/365.25
J27=date(2027,1,1)
WINS=[date(2032,12,15),date(2033,12,15),date(2034,12,15),date(2035,12,15),date(2036,12,15),date(2037,2,15),date(2038,5,15),date(2039,11,15),date(2040,11,15),date(2041,11,15)]
PAYD=[date(y,1,1) for y in range(2033,2043)]
def cost(day,dates,mode,shift=0):
    g,d=boot(day,shift); m,dd,y=map(int,day.split("/")); d0=date(y,m,dd)
    if mode=="unch": return sum(50000*df(g,d,yf(J27,x)) for x in dates)
    return sum(50000*df(g,d,yf(d0,x)) for x in dates)/df(g,d,yf(d0,J27))
day=sys.argv[2] if len(sys.argv)>2 else "10/15/2026"
for nm,dates in (("payment dates (1 Jan 2033-42)",PAYD),("WInS-listed maturities",WINS)):
    for mode in ("fwd","unch"):
        c=cost(day,dates,mode); dv=(cost(day,dates,mode,-0.0001)-c)
        print(f"{day} | {nm:32s} | {mode:4s} | cost ${c:,.0f} | room ${300000-c:,.0f} | {((300000-c)/dv):.1f}bp")
