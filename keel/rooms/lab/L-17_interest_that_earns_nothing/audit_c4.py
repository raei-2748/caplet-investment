"""AI-generated (Claude Code), Tue 3 Nov 2026, the Genius Lab L-17. (Keel is a simulated team, AI-written.) MODEL, deterministic.
Felix C4 (what the $500,000 of cheques is made of) and an independent re-derivation of the lock on the 22 Oct curve,
no rate moves, on the model's own rung sizing (ips_numbers.py s3). Run from repo root:
    python3 keel/rooms/lab/L-17_interest_that_earns_nothing/audit_c4.py"""
import datetime as dt, numpy as np, pandas as pd, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
row = pd.read_csv(ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv").iloc[0]
pts = {1/12: "1 Mo", .25: "3 Mo", .5: "6 Mo", 1: "1 Yr", 2: "2 Yr", 3: "3 Yr", 5: "5 Yr", 7: "7 Yr", 10: "10 Yr", 20: "20 Yr", 30: "30 Yr"}
xs = np.array(list(pts)); ys = np.array([float(row[k]) for k in pts.values()]); curve = lambda t: np.interp(t, xs, ys)
yrs = lambda a, b: (b - a).days / 365.25
TODAY, T27 = dt.date(2026, 10, 22), dt.date(2027, 1, 1); TOFF = yrs(TODAY, T27); PAY = 50_000.0
RUNGS = {2033: (dt.date(2032, 12, 15), None), 2034: (dt.date(2033, 12, 15), None), 2035: (dt.date(2034, 12, 15), None),
         2036: (dt.date(2035, 12, 15), None), 2037: (dt.date(2036, 12, 15), None), 2038: (dt.date(2037, 2, 15), 4.75),
         2039: (dt.date(2038, 5, 15), 4.50), 2040: (dt.date(2039, 11, 15), 4.375), 2041: (dt.date(2040, 11, 15), 4.25),
         2042: (dt.date(2041, 11, 15), 3.125)}
tn = yrs(T27, dt.date(2031, 1, 1))
F = C = IOI_pre = IOI_post = BW = 0
for py, (mat, cpn) in RUNGS.items():
    T = yrs(T27, mat); y0 = curve(T + TOFF); c = (y0 if cpn is None else cpn) / 100
    k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
    g = (1 + y0 / 200) ** (2 * (T - k)); db = 1 + c / 2 * g.sum()
    gw = (1 + curve(.25) / 100) ** yrs(mat, dt.date(py, 1, 1))
    face = PAY / (db * gw)
    F += face; C += face * c / 2 * len(k)
    ioi = face * c / 2 * (g - 1)
    pre = k <= tn
    # interest on interest: earned before naming day (coupon paid before) to naming day, vs the rest
    g_to_n = (1 + y0 / 200) ** (2 * np.maximum(tn - k, 0))
    IOI_pre += (face * c / 2 * (g_to_n - 1))[pre].sum()
    IOI_post += ioi.sum() - (face * c / 2 * (g_to_n - 1))[pre].sum()
    BW += face * db * (gw - 1)
print(f"faces {F:,.0f} | coupons {C:,.0f} | interest on interest: earned before naming day {IOI_pre:,.0f}, after {IOI_post:,.0f} | bill wait {BW:,.0f} | total {F+C+IOI_pre+IOI_post+BW:,.0f}")
print(f"shares of $500,000: faces {F/5e5:.1%}, coupons {C/5e5:.1%}, interest on interest {(IOI_pre+IOI_post)/5e5:.1%} (after naming day {IOI_post/5e5:.1%}), bill wait {BW/5e5:.1%}")
# independent re-derivation of the deterministic lock (numbers-auditor check)
gap = cost = 0
for py, (mat, cpn) in RUNGS.items():
    T = yrs(T27, mat); y0 = curve(T + TOFF); c = (y0 if cpn is None else cpn) / 100
    k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
    db = 1 + c / 2 * ((1 + y0 / 200) ** (2 * (T - k))).sum()
    face = PAY / (db * (1 + curve(.25) / 100) ** yrs(mat, dt.date(py, 1, 1)))
    gz = np.where(k <= tn, (1 + y0 / 200) ** (2 * (T - k)), 1.0)
    g_r = PAY - face * (1 + c / 2 * gz.sum()); gap += g_r
    m = yrs(dt.date(2031, 1, 1), dt.date(py, 1, 1)); cost += g_r / (1 + curve(m) / 100 * m)
print(f"audit: zero-rate gap {gap:,.0f} nominal; lock cost (par bonds, coupons at 0%) {cost:,.0f}")
