import importlib.util, glob, csv
from datetime import date, timedelta
import numpy as np
spec = importlib.util.spec_from_file_location("d1", "research/insight_v1/scripts/D1_purchase_rule.py")
d1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(d1)
H="/private/tmp/claude-501/-Users-ray-Library-CloudStorage-GoogleDrive-jiwang27-knox-nsw-edu-au-My-Drive-Knox-Wharton-2026/03ebd134-68e1-4be3-9581-d23c653d03df/scratchpad/hist/"
rows=[]
for f in sorted(glob.glob(H+"*.csv")): rows+=d1.load(f)
new=d1.load("research/insight_v1/verification/ladder_2026-09-28/treasury_par_2026_to_09-28.csv")
have={r["_date"] for r in rows}
rows+=[r for r in new if r["_date"] not in have]
rows=sorted({r["_date"]:r for r in rows}.values(), key=lambda r:r["_date"])
T0=date(2026,9,28)
offs=[(date(y-1,11,15)-T0) for y in d1.YEARS]
res=[]
for r in rows:
    try:
        f=d1.curve(r)
    except Exception as e: continue
    d=r["_date"]
    same_ttm=sum(50000*f(d+o) for o in offs)
    # forward-to-1Jan-style: same offsets measured from anchor 2027-01-01 -> maturities d+(mat-anchor), priced forward from d+(anchor-T0)
    offsA=[(date(y-1,11,15)-d1.ANCHOR) for y in d1.YEARS]; a=d+(d1.ANCHOR-T0)
    fwd=sum(50000*f(a+o) for o in offsA)/f(a)
    same_cal=sum(50000*f(date(y-1,11,15)) for y in d1.YEARS) if d<date(2031,1,1) else None
    res.append((d,same_ttm,fwd,same_cal))
import statistics as st
print("n days",len(res), res[0][0], res[-1][0])
for lab,i in (("spot same-ttm",1),("fwd same-ttm",2)):
    s=[x for x in res if x[0]>=date(2000,1,1)]
    print(lab, "share<=300k %.1f%%"%(100*sum(x[i]<=300000 for x in s)/len(s)),
          "max", max(s,key=lambda x:x[i])[0], round(max(x[i] for x in s)),
          "2020 median", round(st.median([x[i] for x in s if x[0].year==2020])),
          "2020 min", round(min(x[i] for x in s if x[0].year==2020)),
          "last", round(s[-1][i]))
    ok=[x[0] for x in s if x[i]<=300000]
    print("  days<=300k after 2008-01-01 before 2026-09-01:", [str(x) for x in ok if date(2008,1,1)<=x<date(2026,9,1)][:10])
    print("  last day <=300k before 2026:", max([x for x in ok if x.year<2026], default=None))
    cheaper=[x for x in s if x[i]<=s[-1][i] and x[0]<date(2026,9,28)]
    print("  last day cheaper than 28Sep26:", cheaper[-1][0] if cheaper else None)
    # by year share
    yrs={}
    for x in s: yrs.setdefault(x[0].year,[]).append(x[i]<=300000)
    print("  share by year:", {y:round(100*sum(v)/len(v)) for y,v in yrs.items() if sum(v)})
# same calendar maturities (literal "same promises" in 2020)
s20=[x for x in res if x[0].year==2020]
print("2020 same-calendar-maturity cost: median", round(st.median([x[3] for x in s20])), "max", round(max(x[3] for x in s20)), "min", round(min(x[3] for x in s20)))
# 2020-08-04
for x in res:
    if x[0]==date(2020,8,4): print("2020-08-04", [round(v) for v in x[1:]])
