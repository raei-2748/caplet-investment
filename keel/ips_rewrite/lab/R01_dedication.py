"""R01: does sizing the ladder as a *dedicated* portfolio (later rungs' coupons pay earlier payments) shrink the
coupon-reinvestment risk that the IPS number sheet flags ($21k if yields fall 2pt for good)?

AI-generated (Claude Code) for the IPS rewrite, 26 Oct 2026 (Sydney). MODEL numbers on the 15 Oct 2026 par curve
(competition/official_market_data/daily-treasury-rates_2026-10.csv), par yields used as zero rates, semiannual coupons,
iBond ETFs modelled as par bonds maturing 15 Dec (coupon = yield), as in keel/library/ips_numbers_2026-10/ips_numbers.py.
A = current policy: each rung sized alone, its coupons reinvested in itself until it matures.
B = dedicated: solve from 2042 backwards; every coupon paid on or after 1 Jan 2033 goes straight to the next payment,
    coupons paid before 2033 wait in a short Treasury fund until 1 Jan 2033.
Stress: yields jump by dy on 2 Jan 2027 and stay there (only reinvestment changes; purchases already made).
Run: python3 keel/ips_rewrite/lab/R01_dedication.py
"""
import datetime as dt
import numpy as np
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
row = pd.read_csv(ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv").iloc[0]
TEN = {1/12: "1 Mo", .25: "3 Mo", .5: "6 Mo", 1: "1 Yr", 2: "2 Yr", 3: "3 Yr", 5: "5 Yr", 7: "7 Yr", 10: "10 Yr", 20: "20 Yr", 30: "30 Yr"}
xs = np.array(list(TEN)); ys = np.array([float(row[v]) for v in TEN.values()])
curve = lambda t: float(np.interp(t, xs, ys))
T0 = dt.date(2027, 1, 1)
yrs = lambda a, b: (b - a).days / 365.25
PAY = 50_000.0
RUNGS = {2033: (dt.date(2032, 12, 15), None), 2034: (dt.date(2033, 12, 15), None), 2035: (dt.date(2034, 12, 15), None),
         2036: (dt.date(2035, 12, 15), None), 2037: (dt.date(2036, 12, 15), None), 2038: (dt.date(2037, 2, 15), 4.75),
         2039: (dt.date(2038, 5, 15), 4.50), 2040: (dt.date(2039, 11, 15), 4.375), 2041: (dt.date(2040, 11, 15), 4.25),
         2042: (dt.date(2041, 11, 15), 3.125)}

def coupon_dates(mat):
    d = []; y, m = mat.year, mat.month
    while True:
        dd = dt.date(y, m, 15)
        if dd <= T0: break
        d.append(dd); m -= 6
        if m <= 0: m += 12; y -= 1
    return sorted(d)

def price(mat, cpn):
    """Clean-ish price per $1 face on 1 Jan 2027 at the curve (zero = par yield)."""
    y = curve(yrs(T0, mat)) / 100; c = (y if cpn is None else cpn / 100)
    pv = 0.0
    for d in coupon_dates(mat):
        t = yrs(T0, d); pv += c / 2 / (1 + y / 2) ** (2 * t)
    return pv + 1 / (1 + y / 2) ** (2 * yrs(T0, mat)), c

def grow(t_from, t_to, dy):
    r = max(curve(.25) + dy, 0.25) / 100  # short Treasury fund rate
    return (1 + r) ** max(yrs(t_from, t_to), 0)

def ladder_A(dy):
    cost = deliv = 0.0
    for py, (mat, cpn) in RUNGS.items():
        p, c = price(mat, cpn); y0 = curve(yrs(T0, mat))
        def deliver(d):
            v = 1.0
            for cd in coupon_dates(mat):
                yk = max(y0 + d, 0.25) / 100
                v += c / 2 * (1 + yk / 2) ** (2 * yrs(cd, mat))
            return v * grow(mat, dt.date(py, 1, 1), d)
        face = PAY / deliver(0)
        cost += face * p; deliv += face * deliver(dy)
    return cost, deliv

def ladder_B(dy, size_dy=0.0):
    faces = {}; years = sorted(RUNGS, reverse=True)
    def cash_for(py, faces, d):
        """cash available at 1 Jan py from the faces chosen so far."""
        lo = dt.date(py - 1, 1, 1) if py > 2033 else dt.date(1900, 1, 1)
        hi = dt.date(py, 1, 1); tot = 0.0
        for q, f in faces.items():
            mat, cpn = RUNGS[q]; _, c = price(mat, cpn)
            for cd in coupon_dates(mat):
                if lo < cd <= hi: tot += f * c / 2 * grow(cd, hi, d)
            if lo < mat <= hi: tot += f * grow(mat, hi, d)
        return tot
    for py in years:  # backwards: the rung for py covers what later rungs' coupons don't
        mat, cpn = RUNGS[py]
        have = cash_for(py, faces, size_dy)
        unit = cash_for(py, {py: 1.0}, size_dy)
        faces[py] = max(PAY - have, 0) / unit
    cost = sum(f * price(*RUNGS[q])[0] for q, f in faces.items())
    deliv = sum(min(cash_for(py, faces, dy), 10 * PAY) for py in RUNGS)
    short = sum(max(PAY - cash_for(py, faces, dy), 0) for py in RUNGS)
    return cost, deliv, short, faces

if __name__ == "__main__":
    print("curve date", row["Date"])
    for dy in (0, -1, -2, -3, -4.5, +1):
        ca, da = ladder_A(dy); cb, db, sb, _ = ladder_B(dy)
        print(f"dy {dy:+5.1f}pp | A cost {ca:9,.0f} delivers {da:9,.0f} short {max(500000-da,0):7,.0f} | "
              f"B cost {cb:9,.0f} short (sum of per-payment gaps) {sb:7,.0f}")
    _, _, _, f = ladder_B(0)
    print("B faces:", {k: round(v) for k, v in sorted(f.items())})


# ---- B2: dedicated ladder solved as a linear programme, surplus carried forward in a short Treasury fund ----
def flows(q, d):
    """Cash per $1 face of rung q landing in each payment window, grown at the short rate to that 1 Jan."""
    mat, cpn = RUNGS[q]; _, c = price(mat, cpn); out = {}
    for py in RUNGS:
        lo = dt.date(py - 1, 1, 1) if py > 2033 else dt.date(1900, 1, 1); hi = dt.date(py, 1, 1); v = 0.0
        for cd in coupon_dates(mat):
            if lo < cd <= hi: v += c / 2 * grow(cd, hi, d)
        if lo < mat <= hi: v += grow(mat, hi, d)
        out[py] = v
    return out

def ladder_B2(size_dy=0.0):
    from scipy.optimize import linprog
    Q = sorted(RUNGS); P = sorted(RUNGS); nq = len(Q)
    # vars: faces (nq) + carry after each payment (len P)
    cobj = [price(*RUNGS[q])[0] for q in Q] + [0.0] * len(P)
    A_eq, b_eq = [], []
    F = {q: flows(q, size_dy) for q in Q}
    for i, py in enumerate(P):
        row_ = [F[q][py] for q in Q] + [0.0] * len(P)
        row_[nq + i] = -1.0                       # carry out
        if i > 0: row_[nq + i - 1] = grow(dt.date(P[i-1], 1, 1), dt.date(py, 1, 1), size_dy)  # carry in
        A_eq.append(row_); b_eq.append(PAY)
    r = linprog(cobj, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * (nq + len(P)), method="highs")
    return dict(zip(Q, r.x[:nq])), r.fun

def run_B2(faces, dy):
    carry = 0.0; short = 0.0; prev = None
    for py in sorted(RUNGS):
        cash = sum(f * flows(q, dy)[py] for q, f in faces.items())
        if prev: carry *= grow(dt.date(prev, 1, 1), dt.date(py, 1, 1), dy)
        cash += carry
        short += max(PAY - cash, 0); carry = max(cash - PAY, 0); prev = py
    return short

if __name__ == "__main__":
    faces, cost = ladder_B2()
    print(f"\nB2 dedicated (LP, sized at today's short rate): cost {cost:,.0f}")
    print("faces:", {k: round(v) for k, v in faces.items()})
    for dy in (0, -1, -2, -3, -4.5):
        print(f"  dy {dy:+.1f}pp  shortfall {run_B2(faces, dy):7,.0f}")


def ladder_B3(lb, size_dy=0.0):
    """B2 with every one of the ten holdings kept (face >= lb), so the WInS book and the TNA notes still describe it."""
    from scipy.optimize import linprog
    Q = sorted(RUNGS); nq = len(Q); P = Q
    F = {q: flows(q, size_dy) for q in Q}
    cobj = [price(*RUNGS[q])[0] for q in Q] + [0.0] * len(P)
    A_eq, b_eq = [], []
    for i, py in enumerate(P):
        r_ = [F[q][py] for q in Q] + [0.0] * len(P); r_[nq + i] = -1.0
        if i > 0: r_[nq + i - 1] = grow(dt.date(P[i-1], 1, 1), dt.date(py, 1, 1), size_dy)
        A_eq.append(r_); b_eq.append(PAY)
    r = linprog(cobj, A_eq=A_eq, b_eq=b_eq, bounds=[(lb, None)] * nq + [(0, None)] * len(P), method="highs")
    return dict(zip(Q, r.x[:nq])), r.fun

if __name__ == "__main__":
    for lb in (10_000, 20_000, 30_000):
        faces, cost = ladder_B3(lb)
        s = {dy: run_B2(faces, dy) for dy in (-1, -2, -3)}
        print(f"B3 lb {lb:,}: cost {cost:,.0f}; short -1/-2/-3pp {s[-1]:,.0f}/{s[-2]:,.0f}/{s[-3]:,.0f}; faces "
              + str({k: round(v) for k, v in faces.items()}))
    for sd in (-1.0, -2.0):
        faces, cost = ladder_B3(10_000, size_dy=sd)
        print(f"B3 sized for a {sd:+.0f}pp world: cost {cost:,.0f}; short at -2pp {run_B2(faces, -2):,.0f}, at -3pp {run_B2(faces, -3):,.0f}")
