# W-08c, the Window, Tue 3 Nov 2026. (Keel is a simulated team, AI-written.) AI-generated (Claude Code). MODEL, deterministic.
# Written by Kai (the round's dissent, huddle H-021) and re-run by the Window: identical output. Run from repo root:
#   python3 keel/rooms/window/W-08c_kai_no_reinvestment_lock.py
# Kai's deterministic check (no Monte Carlo): what does it cost on naming day (1 Jan 2031) to stop depending on
# reinvestment for every coupon still to come, versus pricing the gap "at that day's yields"? 22 Oct 2026 curve,
# the model's own rungs and sizing (ips_numbers.py RUNGS; par yields as zero rates, as the model does).
import datetime as dt, numpy as np, pandas as pd, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
row = pd.read_csv(ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv").iloc[0]
pts = {1/12: "1 Mo", .25: "3 Mo", .5: "6 Mo", 1: "1 Yr", 2: "2 Yr", 3: "3 Yr", 5: "5 Yr", 7: "7 Yr", 10: "10 Yr", 20: "20 Yr", 30: "30 Yr"}
xs = np.array(list(pts)); ys = np.array([float(row[k]) for k in pts.values()])
curve = lambda t: np.interp(t, xs, ys)
yrs = lambda a, b: (b - a).days / 365.25
TODAY, T27 = dt.date(2026, 10, 22), dt.date(2027, 1, 1); TOFF = yrs(TODAY, T27); PAY = 50_000.0
RUNGS = {2033: (dt.date(2032, 12, 15), None), 2034: (dt.date(2033, 12, 15), None), 2035: (dt.date(2034, 12, 15), None),
         2036: (dt.date(2035, 12, 15), None), 2037: (dt.date(2036, 12, 15), None), 2038: (dt.date(2037, 2, 15), 4.75),
         2039: (dt.date(2038, 5, 15), 4.50), 2040: (dt.date(2039, 11, 15), 4.375), 2041: (dt.date(2040, 11, 15), 4.25),
         2042: (dt.date(2041, 11, 15), 3.125)}
t31 = yrs(T27, dt.date(2031, 1, 1))
def deliver(dy_after31=0.0, zero_after31=False):
    tot = 0; per = {}
    for py, (mat, cpn) in RUNGS.items():
        T = yrs(T27, mat); y0 = curve(T + TOFF); c = (y0 if cpn is None else cpn) / 100
        k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        db = 1 + c / 2 * ((1 + y0 / 200) ** (2 * (T - k))).sum()
        face = PAY / db
        yk = np.where(k <= t31, y0, max(y0 + dy_after31, 0.25)) / 100
        g = (1 + yk / 2) ** (2 * (T - k))
        if zero_after31: g = np.where(k <= t31, g, 1.0)
        d = face * (1 + c / 2 * g.sum()); per[py] = d; tot += d
    return tot, per
base, _ = deliver()
for dy in (-1, -2):
    print(f"gap if yields fall {dy}pt from naming day, for good: ${10*PAY - deliver(dy)[0]:,.0f}")
z, per = deliver(zero_after31=True)
print(f"gap if every coupon after naming day earns 0%: ${10*PAY - z:,.0f} (nominal, undiscounted)")
# naming-day cost if that money buys Treasuries maturing before each rung's January, at the base curve
pv = 0
for py, (mat, cpn) in RUNGS.items():
    tm = yrs(dt.date(2031, 1, 1), dt.date(py, 1, 1)); y = curve(tm) / 100
    pv += (PAY - per[py]) / (1 + y / 2) ** (2 * tm)
print(f"bought on naming day in matching Treasuries (base curve): ${pv:,.0f}")
print({py: round(PAY - per[py]) for py in per})

# S6-like world: yields 2 pts lower from Jan 2027 for good. Naming day: the at-yields gap vs the no-reinvestment lock.
def deliver2(dy_all, zero_after31=False):
    tot = 0; per = {}
    for py, (mat, cpn) in RUNGS.items():
        T = yrs(T27, mat); y0 = curve(T + TOFF); c = (y0 if cpn is None else cpn) / 100
        k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        face = PAY / (1 + c / 2 * ((1 + y0 / 200) ** (2 * (T - k))).sum())
        g = (1 + max(y0 + dy_all, .25) / 200) ** (2 * (T - k))
        if zero_after31: g = np.where(k <= t31, g, 1.0)
        d = face * (1 + c / 2 * g.sum()); per[py] = d; tot += d
    return tot, per
a, _ = deliver2(-2); z2, per2 = deliver2(-2, True)
pv2 = sum((PAY - per2[py]) / (1 + max(curve(yrs(dt.date(2031,1,1), dt.date(py,1,1))) - 2, .25) / 200) ** (2 * yrs(dt.date(2031,1,1), dt.date(py,1,1))) for py in RUNGS)
print(f"-2pt world: gap at naming-day yields ${10*PAY-a:,.0f}; no-reinvestment gap ${10*PAY-z2:,.0f} nominal, ${pv2:,.0f} bought on naming day")

# Stricter: the lock bought in PAR COUPON Treasuries whose own coupons are also held at 0% (no reinvestment anywhere)
def strict_cost(per, dy):
    c = 0
    for py in RUNGS:
        m = yrs(dt.date(2031, 1, 1), dt.date(py, 1, 1)); y = max(curve(m) + dy, .25) / 100
        c += (PAY - per[py]) / (1 + y * m)
    return c
print(f"strict lock (par coupon bonds, their coupons at 0%): base ${strict_cost(per, 0):,.0f}; -2pt world ${strict_cost(per2, -2):,.0f}")
