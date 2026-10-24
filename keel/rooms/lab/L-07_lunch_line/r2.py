"""FICTION (Genius Lab L-07, rung 2). MODEL on the 22 Oct 2026 close. Adapts keel/scripts/ladder_pv.py and the
floor/fund lines of keel/library/ips_numbers_2026-10/ips_numbers.py (fwd_rate line 60; ibtm_cost line 183; B0 line 192;
top line 208; gift line 227). Run: python3 r2.py"""
import sys, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'scripts'))
import ladder_pv as L
import numpy as np
from datetime import date
L.VAL = date(2026, 10, 22)
CUR = {1/12: 4.11, 2/12: 4.16, .25: 4.22, .5: 4.29, 1: 4.41, 2: 4.65, 3: 4.72, 5: 4.78, 7: 4.86, 10: 4.96, 20: 5.32, 30: 5.29}
L.CURVE = dict(CUR)
T28 = date(2028, 1, 2)
def yrs(a, b): return (b - a).days / 365.25

# ---- ips_numbers.py method: par yield used as zero rate, semiannual, forward yield (line 60) ----
xs = np.array(sorted(CUR)); ys = np.array([CUR[k] for k in xs])
curve = lambda t: np.interp(t, xs, ys)
def fwd_rate(t0, t1):
    z0, z1 = curve(t0)/100, curve(t1)/100
    a0, a1 = (1+z0/2)**(2*t0), (1+z1/2)**(2*t1)
    return 200*((a1/a0)**(1/(2*(t1-t0)))-1)
t0 = yrs(L.VAL, T28)
for label, mat in (("15 Dec 2032 (model date)", date(2032,12,15)), ("31 Dec 2032 (IBTM)", date(2032,12,31))):
    tm = yrs(T28, mat)
    y = float(fwd_rate(t0, t0+tm))
    print(f"\n== A1/A2 forward yield for a 2 Jan 2028 buy of a {label}: {y:.3f}% (ips_numbers method)")
    # bootstrapped method (ladder_pv): forward discount factor
    f = L.build(L.CURVE)
    dfw = float(f(yrs(L.VAL, mat))/f(t0))
    print(f"   bootstrapped forward discount factor {dfw:.4f} -> ETF price per $1 payout {dfw:.4f}")
    for R in (150000, 149000, 140000, 120000):
        for sh in (0, -1, +1, -2):
            yy = max(y+sh, .25)
            cost = R/(1+yy/200)**(2*tm)
            print(f"   R={R:>7} yield {yy:5.2f}% ({sh:+d}pt): ETF {cost:9,.0f} ({cost/R*100:5.1f}%)  fund {R-cost:8,.0f} ({(R-cost)/R*100:4.1f}%)") if R in (150000,120000) or sh==0 else None
    # bootstrapped version at base
    R=150000; print(f"   bootstrapped base: ETF {R*dfw:,.0f} fund {R*(1-dfw):,.0f}")
    # ETF all-in alternative: 150k grows to
    y_=y; print(f"   all-in-ETF end value of 150k: {150000*(1+y_/200)**(2*tm):,.0f}; interest forgone if stocks go to 0: {150000*((1+y_/200)**(2*tm)-1):,.0f}")
    print(f"   fund per 1pt of yield (arith): {(150000/(1+(y-1)/200)**(2*tm)-150000/(1+(y+1)/200)**(2*tm))/2:,.0f} dollars of ETF cost -> inverse for fund")

# ---- combined: yields shift now and stay to Jan 2028: 2027 gap AND dearer/cheaper floor ----
print("\n== combined: parallel shift of the whole curve from 22 Oct, stays to the Jan 2028 buy")
for sh in (-2,-1,-.5,0,.5,1,2):
    gap = max(L.cost(sh) - 300000, 0)
    R = 150000 - gap
    CC = {k: v+sh for k, v in CUR.items()}
    xs_ = np.array(sorted(CC)); ys_ = np.array([CC[k] for k in xs_])
    c2 = lambda t: np.interp(t, xs_, ys_)
    tm = yrs(T28, date(2032,12,15))
    z0, z1 = c2(t0)/100, c2(t0+tm)/100
    y = 200*(((1+z1/2)**(2*(t0+tm))/(1+z0/2)**(2*t0))**(1/(2*tm))-1)
    cost = R/(1+y/200)**(2*tm)
    print(f"  shift {sh:+4}pt: 2027 gap {gap:8,.0f}  R {R:9,.0f}  fwd yield {y:5.2f}%  ETF {cost:9,.0f}  fund {R-cost:8,.0f}")

# ---- gap distribution (A16): sd of parallel move over 22 Oct -> 4 Jan 2027 ----
rng = np.random.default_rng(25102026)
T27buy = yrs(L.VAL, date(2027,1,4))
sd = 1.00*np.sqrt(T27buy)
sh = rng.normal(0, sd, 20000)
gaps = np.array([max(L.cost(s/100*100 if False else s) - 300000, 0) for s in np.linspace(-3,3,61)])
grid = np.linspace(-3,3,61)
g = np.interp(sh, grid, gaps)
print(f"\n== A16: sd of shift to buy day {sd:.2f}pt; P(gap>0) {np.mean(g>0):.2f}; mean gap {g.mean():,.0f}; p50 {np.median(g):,.0f}; p90 {np.percentile(g,90):,.0f}; p95 {np.percentile(g,95):,.0f}")
print(f"   per $1 of gap: floor falls $1.00; ETF cost falls ~0.79-0.80; fund falls ~0.20-0.21 (at 4.9% forward)")

# ---- A5 / A6: 2031 -> 2033 on the stock fund (7% compound, 16.78% vol, monthly) ----
B0 = 32296.0   # model p50 fund on 2 Jan 2028 (results.json)
mu = np.log(1.07) - 0.0006; vol = 0.1678
N = 200000
z = rng.normal(size=(N, 60))
lr = (mu - 0.5*0*vol**2) + vol*z/np.sqrt(12) * 1.0
lr = mu/12 + vol*z/np.sqrt(12)
cum = np.cumsum(lr, axis=1)
V = B0*np.exp(cum)          # months 1..60 from Jan 2028
V31 = V[:, 35]              # Jan 2031 (36 months)
path = V[:, 35:59]          # Jan 2031 .. Dec 2032
V33 = V[:, 59]
trough = path.min(axis=1)
R = 150000.0
top = R + .5*V31; gift = np.minimum(top, R + .5*V33)
print("\n== A5/A6 (MODEL, fund 32.3k median start, lognormal monthly 7%/16.78%)")
print(f"   V31 median {np.median(V31):,.0f}; top median {np.median(top):,.0f}; range width median {np.median(.5*V31):,.0f}")
print(f"   P(V33>=V31) {np.mean(V33>=V31):.3f} (gift at top); P(gift below top) {np.mean(V33<V31):.3f}")
below = V33 < V31
rise_from_trough = below & (V33 > trough*1.0001)
print(f"   P(gift below top AND fund rose from its 2031-33 low into 2033) {np.mean(rise_from_trough):.3f}")
print(f"   median gift gain from trough->2033 in those paths {np.median(.5*(V33-trough)[rise_from_trough]):,.0f}")
print(f"   median shortfall of gift vs top in those paths {np.median((top-gift)[below]):,.0f}")
Vm = 39400.0
print("   A5 at V31=39.4k: fund -20% -> gift -", .5*.2*Vm, "(", .5*.2*Vm/(R+.5*Vm)*100, "% of top)  -50% ->", .5*.5*Vm, " -100% ->", .5*Vm, "=", .5*Vm/(R+.5*Vm)*100, "% of top")
# the worked example
V31e, lowe, V33e = 40000., 20000., 30000.
print(f"   worked: V31 {V31e:,.0f} -> trough {lowe:,.0f} -> V33 {V33e:,.0f}; top {R+.5*V31e:,.0f}; gift {R+.5*V33e:,.0f}; the 10k rise from the trough lifted the gift by {.5*(V33e-lowe):,.0f}")
