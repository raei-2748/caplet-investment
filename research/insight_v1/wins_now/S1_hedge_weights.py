"""S1 Treasury sleeve: duration-matched ETF mixes for Laura's ten $50k payments, key-rate/cash-flow
tracking under curve shifts, and a maturity-by-maturity STRIPS ladder cost.

PROVISIONAL (week-1 WInS research, 2026-09-27). Not approved by the team. Every ticker is
PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading.

Inputs (status labels):
- competition/official_market_data/daily-treasury-rates_2026-09.csv, row 09/25/2026
  (VERIFIED-REPO-FILE: home.treasury.gov par yield curve downloaded by the team).
- research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv: every holding (par, coupon, maturity) of
  IEF TLT TLH GOVT IEI GOVZ IBTM IBTO IBTP IBTQ IBTR IBGA as of 2026-09-24 (iShares "latest-holdings.csv"
  on each ishares.com product page, downloaded 2026-09-27) and VGIT VGLT EDV as of 2026-08-31
  (investor.vanguard.com fund API, downloaded 2026-09-27). VERIFIED-PRIMARY.
- ISSUER_DUR below: effective/average durations shown on the issuer pages (VERIFIED-PRIMARY, accessed
  2026-09-27; as-of dates in the dict). SPTI/SPTL durations are SSGA "option adjusted duration".
- research/insight_v1/wins_now/S1_mspd_table5_2026-08-31_fixed_2032plus.csv: Treasury Monthly Statement
  of the Public Debt, Table V (securities held in stripped form), record date 2026-08-31, from
  api.fiscaldata.treasury.gov (VERIFIED-PRIMARY, accessed 2026-09-27).
Method (same curve method as research/verified_2026-09-27/official_curve_pv.py): par yields treated as
semiannual bond-equivalent yields, linear interpolation to a 0.5y grid, bootstrapped discount factors,
log-linear interpolation. The liability is valued at 2027-01-01 (forward value) -> $292,264.
Funds are valued from their actual holdings' cash flows on the same curve, so each fund's response to a
twist reflects WHERE its cash flows sit (key-rate exposure), not just its single duration number.
ASSUMPTIONS: instantaneous curve shocks; fund holdings fixed during the shock; no fees, bid/ask or
premium/discount; SPTI/SPTL are modelled with VGIT/VGLT holdings (same Bloomberg 3-10y / Long Treasury
index families; SSGA holdings were not downloaded); STRIPS priced on the par-derived zero curve
(real STRIPS quotes differ by a few bp).

Run from the repo root:  .venv/bin/python research/insight_v1/wins_now/S1_hedge_weights.py
"""
import csv
import itertools
from collections import defaultdict
from datetime import date

import numpy as np
from scipy.optimize import minimize

ROOT = "research/insight_v1/wins_now/"
CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
row = next(r for r in csv.DictReader(open(CSV)) if r["Date"] == "09/25/2026")
TEN = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
       "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
PAR = {t: float(row[k]) for k, t in TEN.items()}
VAL, ANCHOR = date(2026, 9, 25), date(2027, 1, 1)
yf = lambda d: (d - VAL).days / 365.25
TA = yf(ANCHOR)
PAY = [date(y, 1, 1) for y in range(2033, 2043)]

# Issuer-page durations (years) and as-of dates. VERIFIED-PRIMARY, accessed 2026-09-27.
ISSUER_DUR = {
    "IEF": (6.86, "2026-09-24"), "TLT": (14.88, "2026-09-24"), "TLH": (11.59, "2026-09-24"),
    "GOVT": (5.45, "2026-09-24"), "IEI": (4.20, "2026-09-24"), "GOVZ": (26.45, "2026-09-24"),
    "IBTM": (5.05, "2026-09-24"), "IBTO": (5.71, "2026-09-24"), "IBTP": (6.44, "2026-09-24"),
    "IBTQ": (7.08, "2026-09-24"), "IBTR": (7.59, "2026-09-24"), "IBGA": (11.74, "2026-09-24"),
    "VGIT": (4.9, "2026-08-31"), "VGLT": (13.5, "2026-08-31"), "EDV": (24.0, "2026-08-31"),
    "SPTI": (4.78, "2026-09-24"), "SPTL": (13.65, "2026-09-24"),
}
PROXY = {"SPTI": "VGIT", "SPTL": "VGLT"}  # ASSUMPTION: same index family, holdings not downloaded
ON_2025_26_LIST = {"IEF", "TLT", "GOVT", "SHY", "SHV", "BIL", "VGSH", "USFR"}  # historical list lines 1029-1124


def build(par):
    ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts]); df = []
    for y in p:
        c = y / 2; df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]; lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))


def shifted(fn):
    """Par curve with shift fn(tenor) in percentage points."""
    return {t: v + fn(t) for t, v in PAR.items()}


def liability(par):
    f = build(par)
    return sum(50000 * f(yf(d)) / f(TA) for d in PAY)


# ---- fund cash flows from holdings -------------------------------------------------------------
def add_months(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    return date(d.year + y, mo + 1, min(d.day, 28) if d.day > 28 else d.day)


def cashflows(par_amt, cpn, mat):
    """(time, amount) list: semiannual coupons stepping back from maturity + principal."""
    mat = date.fromisoformat(mat)
    if mat <= VAL:
        return [(0.0, par_amt)]  # cash / T-bill sweep: no rate sensitivity
    cfs = [(yf(mat), par_amt * (1 + cpn / 200))] if cpn else [(yf(mat), par_amt)]
    k = 1
    while cpn:
        d = add_months(mat, -6 * k)
        if d <= VAL:
            break
        cfs.append((yf(d), par_amt * cpn / 200)); k += 1
    return cfs


FUND_CF = defaultdict(list)
for r in csv.DictReader(open(ROOT + "S1_fund_holdings_snapshot.csv")):
    FUND_CF[r["fund"]] += cashflows(float(r["par"]), float(r["coupon_pct"]), r["maturity"])
for k, v in PROXY.items():
    FUND_CF[k] = FUND_CF[v]


def fund_value(name, par):
    f = build(par)
    t, a = np.array(FUND_CF[name]).T
    return float((a * f(t)).sum())


L0 = liability(PAR)
BP = 0.01


def eff_dur(val):
    up, dn = val(shifted(lambda t: BP)), val(shifted(lambda t: -BP))
    return (dn - up) / (2 * val(PAR) * 1e-4)


def krd(val):
    """Key-rate durations: bump one par node by 1bp (linear interpolation = triangular bump)."""
    base, out = val(PAR), {}
    for t in sorted(PAR):
        up = dict(PAR); up[t] += BP; dn = dict(PAR); dn[t] -= BP
        out[t] = (val(dn) - val(up)) / (2 * base * 1e-4)
    return out


# ---- scenarios (par-yield shifts, percentage points) -------------------------------------------
def twist_2s30s(sign):  # 2y moves -25bp*sign, 30y +25bp*sign, straight line between, flat outside
    return lambda t: sign * (-0.25 + 0.50 * (min(max(t, 2), 30) - 2) / 28)


def twist_2s10s(sign):  # 2y -25bp*sign, 10y +25bp*sign, flat beyond 10y and below 2y
    return lambda t: sign * (-0.25 + 0.50 * (min(max(t, 2), 10) - 2) / 8)


SCEN = {
    "+100bp parallel": lambda t: 1.0, "-100bp parallel": lambda t: -1.0,
    "steepener 50bp (2s30s)": twist_2s30s(+1), "flattener 50bp (2s30s)": twist_2s30s(-1),
    "steepener 50bp (2s10s)": twist_2s10s(+1), "flattener 50bp (2s10s)": twist_2s10s(-1),
}
L_S = {k: liability(shifted(fn)) for k, fn in SCEN.items()}
FUNDS = sorted(FUND_CF)
V0 = {n: fund_value(n, PAR) for n in FUNDS}
R_S = {n: {k: fund_value(n, shifted(fn)) / V0[n] - 1 for k, fn in SCEN.items()} for n in FUNDS}
MODEL_DUR = {n: eff_dur(lambda p, n=n: fund_value(n, p)) for n in FUNDS}
LIAB_DUR = eff_dur(liability)
KRD_L = krd(liability)
KRD_F = {n: krd(lambda p, n=n: fund_value(n, p)) for n in FUNDS}


def tracking(weights):
    """$ tracking error (hedge change minus liability change), hedge sized at L0 = $292,264."""
    return {k: L0 * sum(w * R_S[n][k] for n, w in weights.items()) - (L_S[k] - L0) for k in SCEN}


def krd_gap(weights):
    return {t: sum(w * KRD_F[n][t] for n, w in weights.items()) - KRD_L[t] for t in KRD_L}


def two_fund(a, b, dur=None):
    da, db = (dur or {}).get(a, ISSUER_DUR[a][0]), (dur or {}).get(b, ISSUER_DUR[b][0])
    wa = (db - LIAB_TARGET) / (db - da)
    return {a: wa, b: 1 - wa}


LIAB_TARGET = 9.90  # verified liability duration (brief section 6)


def three_fund(a, b, c):
    """Weights >=0 summing to 1 with issuer-duration-weighted duration = 9.90, minimising squared
    key-rate-duration gaps versus the liability."""
    names = [a, b, c]; D = np.array([ISSUER_DUR[n][0] for n in names])
    K = np.array([[KRD_F[n][t] for t in sorted(KRD_L)] for n in names]).T
    kl = np.array([KRD_L[t] for t in sorted(KRD_L)])
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1}, {"type": "eq", "fun": lambda w: w @ D - LIAB_TARGET}]
    best = None
    for x0 in ([1/3] * 3, [.6, .2, .2], [.2, .6, .2], [.2, .2, .6]):
        r = minimize(lambda w: ((K @ w - kl) ** 2).sum(), np.array(x0), bounds=[(0, 1)] * 3,
                     constraints=cons, method="SLSQP")
        if r.success and (best is None or r.fun < best.fun):
            best = r
    return None if best is None else dict(zip(names, best.x))


def summary(weights):
    te = tracking(weights)
    twist = max(abs(v) for k, v in te.items() if "parallel" not in k)
    par_ = max(abs(te["+100bp parallel"]), abs(te["-100bp parallel"]))
    fee = sum(w * FEE.get(n, np.nan) for n, w in weights.items())
    return te, twist, par_, fee


# Expense ratios (%), issuer pages, accessed 2026-09-27 (VERIFIED-PRIMARY; GOVZ = net after waiver)
FEE = {"IEF": .15, "TLT": .15, "TLH": .15, "GOVT": .05, "IEI": .15, "GOVZ": .10, "IBTM": .07, "IBTO": .07,
       "IBTP": .07, "IBTQ": .07, "IBTR": .07, "IBGA": .07, "VGIT": .03, "VGLT": .03, "EDV": .05,
       "SPTI": .03, "SPTL": .03}

if __name__ == "__main__":
    print(f"Liability value at 2027-01-01: ${L0:,.0f}; model duration {LIAB_DUR:.2f}y; "
          f"DV01 ${L0 * LIAB_DUR * 1e-4:,.0f}/bp")
    print("Liability change by scenario:", {k: f"{L_S[k] - L0:+,.0f}" for k in SCEN})
    print("\nKey-rate durations (years per 1bp at each par node; sum ~= duration)")
    nodes = [t for t in sorted(KRD_L) if t >= 1]
    hdr = "".join(f"{t:>7g}" for t in nodes)
    print(f"{'':6}{'<1y':>7}{hdr}   model  issuer")
    def krow(name, k, md, idur=""):
        short = sum(v for t, v in k.items() if t < 1)
        print(f"{name:6}{short:7.2f}" + "".join(f"{k[t]:7.2f}" for t in nodes) + f"{md:8.2f}  {idur}")
    krow("LIAB", KRD_L, LIAB_DUR)
    for n in FUNDS:
        krow(n, KRD_F[n], MODEL_DUR[n], f"{ISSUER_DUR[n][0]} ({ISSUER_DUR[n][1]})")

    print("\n=== 2-fund duration matches (issuer durations), $ tracking error = hedge change - liability change ===")
    shorts = [n for n in FUNDS if ISSUER_DUR[n][0] < LIAB_TARGET]
    longs = [n for n in FUNDS if ISSUER_DUR[n][0] > LIAB_TARGET]
    res2 = []
    for a, b in itertools.product(shorts, longs):
        w = two_fund(a, b); te, tw, pa, fee = summary(w)
        res2.append((tw, a, b, w, te, pa, fee))
    res2.sort(key=lambda x: x[0])
    for tw, a, b, w, te, pa, fee in res2:
        on = "".join("*" if n in ON_2025_26_LIST else "" for n in (a, b))
        print(f"{a:5}{w[a]*100:5.1f}% / {b:5}{w[b]*100:5.1f}%  fee {fee:.3f}%  worst twist ${tw:6,.0f}  "
              f"worst ±100 ${pa:6,.0f}  " + "  ".join(f"{k.split(' (')[0][:5]}{'/'+k.split('(')[1][:-1] if '(' in k else ''}:{v:+,.0f}" for k, v in te.items())
              + f"  on25-26:{on}")

    print("\n=== 3-fund matches (duration = 9.90 on issuer durations, min key-rate gap) ===")
    pool = [n for n in FUNDS if n not in ("SPTI", "SPTL")]
    res3 = []
    for combo in itertools.combinations(pool, 3):
        ds = [ISSUER_DUR[n][0] for n in combo]
        if not (min(ds) < LIAB_TARGET < max(ds)):
            continue
        w = three_fund(*combo)
        if w is None or min(w.values()) < 0.02:
            continue  # effectively a 2-fund mix
        te, tw, pa, fee = summary(w)
        res3.append((tw, combo, w, te, pa, fee))
    res3.sort(key=lambda x: x[0])
    for tw, combo, w, te, pa, fee in res3[:15]:
        print("  ".join(f"{n} {w[n]*100:4.1f}%" for n in combo) + f"  fee {fee:.3f}%  worst twist ${tw:,.0f}  "
              f"worst ±100 ${pa:,.0f}  " + "  ".join(f"{v:+,.0f}" for v in te.values()))

    print("\n=== 3-fund matches solving value, duration AND zero 2s30s-twist error exactly (weights >= 0) ===")
    res3b = []
    k30 = "steepener 50bp (2s30s)"
    for combo in itertools.combinations(pool, 3):
        A = np.array([[1, 1, 1], [ISSUER_DUR[n][0] for n in combo], [R_S[n][k30] for n in combo]])
        b = np.array([1, LIAB_TARGET, (L_S[k30] - L0) / L0])
        try:
            w = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            continue
        if w.min() < 0.02:
            continue
        w = dict(zip(combo, w)); te, tw, pa, fee = summary(w)
        res3b.append((tw, combo, w, te, pa, fee))
    res3b.sort(key=lambda x: x[0])
    for tw, combo, w, te, pa, fee in res3b[:12]:
        print("  ".join(f"{n} {w[n]*100:4.1f}%" for n in combo) + f"  fee {fee:.3f}%  worst twist ${tw:,.0f}  "
              f"worst ±100 ${pa:,.0f}  " + "  ".join(f"{v:+,.0f}" for v in te.values()))

    print("\n=== Named mixes for the write-up ===")
    named = {
        "IEF/TLT (brief, 2026-06-30 durations 64.8/35.2)": {"IEF": .648, "TLT": .352},
        "IEF/TLT (today's durations)": two_fund("IEF", "TLT"),
        "IEF/TLH": two_fund("IEF", "TLH"),
        "GOVT/TLT": two_fund("GOVT", "TLT"),
        "SPTI/SPTL (VGIT/VGLT holdings proxy)": two_fund("SPTI", "SPTL"),
        "VGIT/VGLT": two_fund("VGIT", "VGLT"),
        "IEF/TLH/TLT (3-fund, min KRD gap)": three_fund("IEF", "TLH", "TLT"),
        "IEI/TLH/TLT (3-fund, min KRD gap)": three_fund("IEI", "TLH", "TLT"),
        "IEF/TLH/IBGA": three_fund("IEF", "TLH", "IBGA"),
    }
    for name, w in named.items():
        te, tw, pa, fee = summary(w)
        g = krd_gap(w)
        print(f"{name}: " + ", ".join(f"{n} {v*100:.1f}%" for n, v in w.items()) + f"; fee {fee:.3f}%")
        print("    TE $: " + ", ".join(f"{k} {v:+,.0f}" for k, v in te.items()))
        print("    KRD gap (mix - liability): " + ", ".join(f"{t:g}y {v:+.2f}" for t, v in g.items() if abs(v) > .005))

    # ---- Laura's real ladder: payment -> STRIPS maturity -> cost at 2027-01-01 -----------------
    print("\n=== Laura's ladder: $50,000 face per payment, valued at 2027-01-01 on the 2026-09-25 curve ===")
    f = build(PAR)
    mspd = list(csv.DictReader(open(ROOT + "S1_mspd_table5_2026-08-31_fixed_2032plus.csv")))
    cost = lambda d: 50000 * f(yf(d)) / f(TA)
    tot_rec = 0.0
    print("payment | principal STRIPS available in the 8 months before it (maturity, CUSIP, underlying, $m already "
          "stripped) | cost at 2027-01-01 | Nov-15 coupon STRIP cost | exact-date zero")
    for pay in PAY:
        yr = pay.year - 1
        nov15 = date(yr, 11, 15)
        win = [r for r in mspd if f"{yr}-05-01" <= r["maturity_date"] <= f"{yr}-12-31"]
        opts = "; ".join(f"{r['maturity_date']} {r['principal_strip_cusip']} ({r['coupon_pct']}% "
                         f"{r['security_class'].split()[1][:-1].lower()}, ${float(r['stripped_thousands'])/1e3:,.0f}m) "
                         f"${cost(date.fromisoformat(r['maturity_date'])):,.0f}" for r in win) or "none"
        has_nov = any(r["maturity_date"] == nov15.isoformat() for r in win)
        rec = cost(nov15)  # recommended rung: Nov-15 principal STRIP if it exists, else Nov-15 coupon STRIP
        tot_rec += rec
        print(f"{pay} | {opts} | Nov-15 rung ({'principal' if has_nov else 'coupon/interest'} STRIP) ${rec:,.0f} "
              f"| exact ${cost(pay):,.0f}")
    print(f"Total, ten Nov-15 rungs: ${tot_rec:,.0f} vs exact-date liability ${L0:,.0f} "
          f"(extra ${tot_rec - L0:,.0f} = cost of receiving each $50k ~47 days early, before T-bill reinvestment)")
    # Nov 15 2036 note: not yet issued at record date 2026-08-31 (ASSUMPTION: 10-year note issued Nov 2026)
    print(f"If the Nov-15-2036 10-year note (expected Nov 2026 refunding; ASSUMPTION) is used for Jan-2037: "
          f"${cost(date(2036, 11, 15)):,.0f} instead of Aug-15-2036 ${cost(date(2036, 8, 15)):,.0f}")
    # iBonds alternative for 2033-2037: fund terminates ~Dec 15 of its year; YTM net of 0.07% fee (9/24)
    ib = {"IBTM": (2032, 5.09), "IBTO": (2033, 5.12), "IBTP": (2034, 5.15), "IBTQ": (2035, 5.18), "IBTR": (2036, 5.19)}
    print("iBonds alternative (hold to ~Dec 15; YTM from issuer page 9/24 less 0.07% fee; ASSUMPTION: YTM earned):")
    for n, (y, ytm) in ib.items():
        T = (date(y, 12, 15) - ANCHOR).days / 365.25
        print(f"   Jan-{y+1} payment: {n} ~${50000 / (1 + (ytm - .07) / 200) ** (2 * T):,.0f} at 2027-01-01")
