import sys
from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'scripts'))
import ladder_pv as L
from datetime import date
L.VAL=date(2026,10,22)
L.CURVE={1/12:4.11,2/12:4.16,.25:4.22,.5:4.29,1:4.41,2:4.65,3:4.72,5:4.78,7:4.86,10:4.96,20:5.32,30:5.29}
f=L.build(L.CURVE); a=L.yf(L.ANCHOR)
mat={2037:date(2037,2,15),2038:date(2038,5,15),2040:date(2039,11,15),2041:date(2040,11,15),2042:date(2041,11,15)}
mat={2038:date(2037,2,15),2039:date(2038,5,15),2040:date(2039,11,15),2041:date(2040,11,15),2042:date(2041,11,15)}
extra=0
for y,m in mat.items():
    p=date(y,1,1); gap=(p-m).days/365.25
    model=50000*f(L.yf(p))/f(a)
    for rb in (0.04,):
        real=50000*f(L.yf(m))/f(a)/(1+rb*gap)
        print(y,m,round(gap,2),round(model),round(real),round(real-model)); extra+=real-model
print("extra cost vs model",round(extra))
print("22Oct model", round(L.cost()), " 21Oct curve:")
L.VAL=date(2026,10,21)
L.CURVE={1/12:4.09,2/12:4.16,.25:4.25,.5:4.35,1:4.52,2:4.81,3:4.89,5:4.95,7:5.03,10:5.13,20:5.47,30:5.42}
print(round(L.cost()))
