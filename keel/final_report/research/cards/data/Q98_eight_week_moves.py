"""Card Q98: how far Treasury yields have moved in eight weeks, and what such a move before January 2027 would do to
the top-up, the extra Treasuries, the floor money and VT. Keel arithmetic (MODEL) on the register's own engine
(`keel/final_report/numbers/engine.py`, `completion.py`); never the register's figures.

Run from the repo root:  python3 -I keel/final_report/research/cards/data/Q98_eight_week_moves.py
Writes keel/final_report/research/cards/data/Q98_eight_week_moves.csv (about four minutes; numpy only).

Method.
  1. The ten's sensitivity by tenor ("key rates"): bump each par tenor of the 6 Nov 2026 curve by 1bp and re-size the
     ten exactly as the register does (design A at that curve's forward rates). The cost of the ten is what the top-up
     turns on: top-up = max(cost of the ten - $300,000, 0), carried a year at that curve's 2027 forward rate
     (`completion.completion_exact(d, "plain")`, the register's section 5 convention).
  2. History: every start day from 2 Jan 1962 whose end day (the last close on or before start + H days) is on file.
     Data: FRED constant-maturity series DGS6MO ... DGS30 (the Treasury's own par curve) in
     `archive/rab/data/fred/` for 1962-2025; the treasury.gov par curve files in `competition/official_market_data/` for
     2026 to 6 Nov; the 9-13 Nov 2026 rows read at source on Tue 17 Nov 2026 (Sydney) from treasury.gov's TextView page
     (embedded below; the 6 Nov row there matches the repo file exactly).
     Each window's change at each tenor is added to the 6 Nov 2026 curve and the ten are re-sized EXACTLY on that
     (non-parallel) curve. Missing tenors: a tenor without data that day takes the change interpolated linearly in
     maturity between the nearest tenors that have it (6-month before Sep 1981 and 2-year before Jun 1976 from 1y/3y;
     7-year before Jul 1969 from 5y/10y; 20-year in its 1987-1993 gap from 10y/30y; 1-3 months take the 6-month or
     1-year change; their weight is zero).
     "abs": the change in points as it happened. "prop": each tenor's change scaled by (6 Nov 2026 level / start
     level, at most 3 times), the register's proportional convention for history (keel/models/ASSUMPTIONS.md A35).
  3. The parallel-equivalent fall: the parallel shift of the 6 Nov curve that gives the same cost of the ten. It is
     used ONLY to read the extra Treasuries (the backstop, `completion.shifted`) off a 0.05-point grid; the top-up
     itself is exact for every window.
  4. Floor money and VT under Keel's reading of "most" (NUMBERS 4): floor = max(73.3% of what is left,
     min(what is left, $75,001)); VT the rest. What is left = $150,000 - (top-up + extra Treasuries - money left over
     from the first deposit when the ten cost under $300,000), as `plan.run`.
  5. Recessions: NBER peak and trough months (nber.org, read 17 Nov 2026). A window is "in a recession" if its start
     month is after a peak month and no later than the trough month; "recession within 14 months" if any such month
     falls from the start month to 14 months later (6 Nov 2026 to the January 2028 deposit).
  6. Runs: H = 56 days on the 6 Nov curve (6 Nov to 1 Jan, the register's NUMBERS 5(d) span), "abs" and "prop";
     H = 59 days (6 Nov to Mon 4 Jan 2027, the first trading day); H = 52 days applied to the 13 Nov 2026 curve
     (13 Nov to 4 Jan: the stretch still to come on the read date). Also the same weeks every year (the close on or
     before 6 Nov to the first January close, 1962-2025), episodes (overlapping windows whose starts lie within 60 days
     of each other counted once), and each NBER recession's peak-to-trough change.
  CSV columns: section, sample, item, value, note. Overlapping windows are shares of windows, never probabilities.
"""
import csv
import math
import sys
from bisect import bisect_right
from datetime import date, timedelta
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "keel/final_report/numbers"))
import engine as E          # noqa: E402
import completion as C      # noqa: E402

OUT = Path(__file__).with_suffix(".csv")
FRED = ROOT / "archive/rab/data/fred"
MD = ROOT / "competition/official_market_data"
c = C.c
PAR0 = dict(c.par)
DEP, SHARE, HALF1 = 150_000.0, E.ASSUMPTIONS["floor_share"], 75_001.0
PROP_CAP = 3.0     # "prop" scales a change by at most 3 (start levels under a third of today's), as engine.history_windows caps

# engine tenors (years) and the FRED series for each
SER = {0.5: "DGS6MO", 1: "DGS1", 2: "DGS2", 3: "DGS3", 5: "DGS5", 7: "DGS7", 10: "DGS10", 20: "DGS20", 30: "DGS30"}
TCOLS = {"6 Mo": 0.5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3, "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
# treasury.gov TextView, November 2026, read Tue 17 Nov 2026 (Sydney): 6 Mo, 1, 2, 3, 5, 7, 10, 20, 30 years
NOV_AT_SOURCE = {
    date(2026, 11, 9): (4.26, 4.38, 4.56, 4.58, 4.67, 4.76, 4.88, 5.29, 5.26),
    date(2026, 11, 10): (4.38, 4.56, 4.73, 4.74, 4.81, 4.89, 4.98, 5.39, 5.35),
    date(2026, 11, 12): (4.42, 4.65, 4.86, 4.90, 4.95, 5.02, 5.10, 5.48, 5.43),
    date(2026, 11, 13): (4.42, 4.65, 4.88, 4.92, 4.98, 5.05, 5.15, 5.52, 5.47),
}
NOV13_FULL = {1 / 12: 4.10, 2 / 12: 4.26, .25: 4.32, .5: 4.42, 1: 4.65, 2: 4.88, 3: 4.92, 5: 4.98, 7: 5.05, 10: 5.15,
              20: 5.52, 30: 5.47}   # same page; 1.5 and 4 months are not engine tenors
# NBER business cycle reference dates (peak month, trough month), nber.org, read 17 Nov 2026 ("last updated 03/14/2023")
NBER = [((1960, 4), (1961, 2)), ((1969, 12), (1970, 11)), ((1973, 11), (1975, 3)), ((1980, 1), (1980, 7)),
        ((1981, 7), (1982, 11)), ((1990, 7), (1991, 3)), ((2001, 3), (2001, 11)), ((2007, 12), (2009, 6)),
        ((2020, 2), (2020, 4))]
REC = set()
for (py, pm), (ty, tm) in NBER:
    k = py * 12 + pm - 1 + 1
    while k <= ty * 12 + tm - 1:
        REC.add(k)
        k += 1


def mk(d):
    return d.year * 12 + d.month - 1


def month_end(y, m):
    return date(y + (m == 12), m % 12 + 1, 1) - timedelta(days=1)


# ---------------------------------------------------------------- data
def load():
    data = {t: {} for t in SER}
    for t, s in SER.items():
        for r in csv.DictReader(open(FRED / f"{s}.csv")):
            v = r[s]
            d = date.fromisoformat(r["observation_date"])
            if v not in ("", ".") and d.year <= 2025:
                data[t][d] = float(v)
    for f in ("daily-treasury-rates_2026-10-23.csv", "daily-treasury-rates_2026-11-06.csv"):
        for r in csv.DictReader(open(MD / f)):
            m, dd, y = r["Date"].split("/")
            d = date(int(y), int(m), int(dd))
            for col, t in TCOLS.items():
                if r.get(col) not in (None, "", "N/A"):
                    data[t][d] = float(r[col])
    for d, row in NOV_AT_SOURCE.items():
        for t, v in zip(SER, row):
            data[t][d] = v
    days = sorted(data[10])
    return data, days


DATA, DAYS = load()
TEN = sorted(SER)


def changes(i, j):
    """Change in each engine tenor from DAYS[i] to DAYS[j], with the fill rules in the docstring; also start levels."""
    d0, d1 = DAYS[i], DAYS[j]
    have = {t: (DATA[t][d0], DATA[t][d1]) for t in TEN if d0 in DATA[t] and d1 in DATA[t]}
    ts = sorted(have)
    dlt = np.array([have[t][1] - have[t][0] for t in ts])
    lev = np.array([have[t][0] for t in ts])
    full_t = TEN
    dch = np.interp(full_t, ts, dlt)       # flat beyond the ends, linear inside
    lvl = np.interp(full_t, ts, lev)
    return dict(zip(full_t, dch)), dict(zip(full_t, lvl)), len(ts)


def curve_from(dch, prop=False, lvl=None, base=None):
    base = base or PAR0
    par = {}
    for t, v in base.items():
        if t < 0.5:
            key = 0.5
        elif t in dch:
            key = t
        else:
            key = min(dch, key=lambda x: abs(x - t))
        d = dch[key]
        if prop:
            d = d * min(base[key] / lvl[key], PROP_CAP)
        par[t] = v + d
    return par


def ten_cost(par=None, curve=None):
    cv = curve or E.Curve(par)
    ins = E.instruments(cv)
    return E.cost(ins, E.size_own_rung(ins, E.Reinvest(cv))), cv


BASE_COST, _ = ten_cost(curve=c)

# ---------------------------------------------------------------- 1. key rates
KR = {}
for t in sorted(PAR0):
    p = dict(PAR0)
    p[t] += 0.01
    KR[t] = BASE_COST - ten_cost(p)[0]
up, dn = ten_cost(curve=E.Curve(PAR0, shift=0.0001))[0], ten_cost(curve=E.Curve(PAR0, shift=-0.0001))[0]
DV01 = (dn - up) / 2

# ---------------------------------------------------------------- 3. parallel grids
PG = np.round(np.arange(-0.07, 0.0601, 0.0001), 6)          # parallel shifts, decimal
PCOST = np.array([ten_cost(curve=E.Curve(PAR0, shift=s))[0] if s else BASE_COST for s in PG])


def s_equiv(cost):
    """Parallel shift (decimal) that gives this cost of the ten (cost falls as s rises)."""
    return float(np.interp(-cost, -PCOST, PG))


BG = np.round(np.arange(-0.045, 0.0201, 0.0005), 6)
BACK = np.array([C.shifted(float(s))["H_plain"]["margin"] for s in BG])   # 1 Jan 2027 money, on that curve


def plan_at(cost, curve):
    """The January 2028 money on one curve: top-up, extra Treasuries, money left from the first deposit, completion,
    floor money, VT. Keel arithmetic on the register's conventions."""
    carry = math.exp(curve.fwd(E.J27, E.J28))
    s = s_equiv(cost)
    back = float(np.interp(s, BG, BACK))
    topup = max(cost - 300_000.0, 0.0) * carry
    leftover = max(300_000.0 - cost, 0.0) * carry
    extra = back * carry
    comp = topup + extra - leftover
    left = max(DEP - comp, 0.0)
    floor = max(SHARE * left, min(left, HALF1))
    return dict(s=s, topup=topup, extra=extra, leftover=leftover, completion=comp, left=left, floor=floor,
                vt=left - floor)


P0 = plan_at(BASE_COST, c)

# thresholds as parallel falls (points), exact on the engine
def solve(f, target, lo, hi):
    for _ in range(80):
        mid = (lo + hi) / 2
        if (f(mid) - target) * (f(lo) - target) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def topup_par(s):
    cv = E.Curve(PAR0, shift=s)
    return max(ten_cost(curve=cv)[0] - 300_000, 0) * math.exp(cv.fwd(E.J27, E.J28))


def comp_par(s):
    cv = E.Curve(PAR0, shift=s)
    return plan_at(ten_cost(curve=cv)[0], cv)["completion"]


THR = {
    "topup_zero (rise)": -100 * solve(lambda s: ten_cost(curve=E.Curve(PAR0, shift=s))[0], 300_000, 0.0, 0.01),
    "topup_10000": 100 * -solve(topup_par, 10_000, -0.01, 0.0),
    "topup_20000": 100 * -solve(topup_par, 20_000, -0.02, 0.0),
    "topup_38282": 100 * -solve(topup_par, 38_282, -0.03, 0.0),
    "completion_47679 (Keel's $75,001 binds)": 100 * -solve(comp_par, DEP - HALF1 / SHARE, -0.02, 0.0),
    "completion_75001 (most fails, VT nil)": 100 * -solve(comp_par, 75_001, -0.03, 0.0),
    "completion_150000 (whole deposit)": 100 * -solve(comp_par, 150_000, -0.045, -0.02),
}


# ---------------------------------------------------------------- 2. history
def windows(H, prop=False, base=None):
    rows = []
    for i, d in enumerate(DAYS):
        tgt = d + timedelta(days=H)
        if tgt > DAYS[-1]:
            break
        j = bisect_right(DAYS, tgt) - 1
        dch, lvl, n = changes(i, j)
        par = curve_from(dch, prop, lvl, base)
        cost, cv = ten_cost(par)
        p = plan_at(cost, cv)
        months = range(mk(d), mk(d) + 15)
        rows.append(dict(start=d, end=DAYS[j], d1=dch[1], d10=dch[10], d20=dch[20], lvl10=lvl[10], cost=cost,
                         rec_now=mk(d) in REC, rec_14=any(m in REC for m in months), n=n, **p))
    return rows


def share(rows, f):
    return (sum(1 for r in rows if f(r)) / len(rows)) if rows else float("nan")


def episodes(rows, f, gap=60):
    eps, last = [], None
    for r in rows:
        if not f(r):
            continue
        if last is not None and (r["start"] - last).days <= gap:
            e = eps[-1]
            e["last"] = r["start"]
            if r["topup"] > e["max_topup"]:
                e.update(max_topup=r["topup"], fall=-100 * r["s"], at=r["start"], lvl10=r["lvl10"])
            e["rec_now"] |= r["rec_now"]
            e["rec_14"] |= r["rec_14"]
        else:
            eps.append(dict(first=r["start"], last=r["start"], max_topup=r["topup"], fall=-100 * r["s"],
                            at=r["start"], lvl10=r["lvl10"], rec_now=r["rec_now"], rec_14=r["rec_14"]))
        last = r["start"]
    return eps


TESTS = [
    ("topup > $10,000", lambda r: r["topup"] > 10_000),
    ("topup > $20,000", lambda r: r["topup"] > 20_000),
    ("topup > $38,282", lambda r: r["topup"] > 38_282),
    ("completion > $47,679 (Keel's $75,001 binds; VT squeezed)", lambda r: r["completion"] > DEP - HALF1 / SHARE),
    ("completion > $75,001 (most fails; VT nil)", lambda r: r["completion"] > 75_001),
    ("topup = $0 (ten cost under $300,000)", lambda r: r["topup"] == 0),
    ("parallel-equivalent fall >= 0.5 point", lambda r: r["s"] <= -0.005),
]

out = []


def emit(section, sample, item, value, note=""):
    out.append([section, sample, item, value if isinstance(value, str) else f"{value:.6g}", note])


emit("engine", "6 Nov 2026 curve", "cost of the ten (engine, register)", BASE_COST)
emit("engine", "6 Nov 2026 curve", "dollars per basis point, parallel", DV01)
for t, v in KR.items():
    emit("key_rate", "6 Nov 2026 curve", f"tenor {t:.4g}y: dollars per bp", v, f"share {v / DV01:.3f}")
for k, v in THR.items():
    emit("threshold", "parallel fall in points", k, v)
for k, v in P0.items():
    emit("central", "6 Nov 2026 curve (Keel arithmetic; register: top-up $2,388, extra $35,894)", k, v)

# the week already seen: 13 Nov 2026 close, read at source
cost13, cv13 = ten_cost(NOV13_FULL)
p13 = plan_at(cost13, cv13)
emit("current", "13 Nov 2026 curve (treasury.gov, read 17 Nov)", "cost of the ten", cost13)
for k, v in p13.items():
    emit("current", "13 Nov 2026 curve (treasury.gov, read 17 Nov)", k, v)
for k in ("topup_10000", "topup_20000", "topup_38282", "completion_47679 (Keel's $75,001 binds)",
          "completion_75001 (most fails, VT nil)"):
    emit("current", "further parallel fall needed from 13 Nov levels", k, THR[k] + 100 * p13["s"])

RUNS = {}
for H, prop, base in ((56, False, None), (56, True, None), (59, False, None), (52, False, NOV13_FULL)):
    rows = windows(H, prop, base)
    RUNS[(H, prop)] = rows
    tag = f"{H} days {'prop' if prop else 'abs'}" + (" from the 13 Nov 2026 curve" if base else "")
    samples = {
        "all starts 1962-": rows,
        "starts 1990-": [r for r in rows if r["start"].year >= 1990],
        "starts 2000-": [r for r in rows if r["start"].year >= 2000],
        "10y at start 3.5%-6.5%": [r for r in rows if 3.5 <= r["lvl10"] <= 6.5],
        "starts in an NBER recession": [r for r in rows if r["rec_now"]],
        "starts with no recession within 14 months": [r for r in rows if not r["rec_14"]],
        "starts with a recession within 14 months": [r for r in rows if r["rec_14"]],
    }
    for sname, srows in samples.items():
        emit("history", f"{tag}; {sname}", "windows", len(srows), f"{srows[0]['start']} to {srows[-1]['start']}" if srows else "")
        for name, f in TESTS:
            emit("history", f"{tag}; {sname}", name, share(srows, f))
        if srows:
            tu = np.array([r["topup"] for r in srows])
            ss = -100 * np.array([r["s"] for r in srows])
            for q in (50, 90, 95, 99):
                emit("history", f"{tag}; {sname}", f"top-up percentile {q}", float(np.percentile(tu, q)))
            emit("history", f"{tag}; {sname}", "top-up largest", float(tu.max()), str(srows[int(tu.argmax())]["start"]))
            emit("history", f"{tag}; {sname}", "parallel-equivalent fall: s.d. (points)", float(ss.std()))
            for name, f in TESTS[:5]:
                k = [r for r in srows if f(r)]
                emit("history", f"{tag}; {sname}", f"{name}: share starting in a recession",
                     share(k, lambda r: r["rec_now"]) if k else float("nan"), f"{len(k)} windows")
                emit("history", f"{tag}; {sname}", f"{name}: share with a recession within 14 months",
                     share(k, lambda r: r["rec_14"]) if k else float("nan"))
    # the 1-year and 10-year alone, against the exact cost (56 days abs only)
    if (H, prop) == (56, False):
        allr = rows
        d1 = np.array([r["d1"] for r in allr])
        d10 = np.array([r["d10"] for r in allr])
        ss = 100 * np.array([r["s"] for r in allr])
        emit("tenor_check", tag, "corr(parallel-equivalent, 10y change)", float(np.corrcoef(ss, d10)[0, 1]))
        emit("tenor_check", tag, "corr(parallel-equivalent, 1y change)", float(np.corrcoef(ss, d1)[0, 1]))
        emit("tenor_check", tag, "share 1y fell >= 1.33 pt (register NUMBERS 5d test)", float((d1 <= -1.33075).mean()))
        emit("tenor_check", tag, "share parallel-equivalent fell >= 1.33 pt", float((ss <= -THR["completion_75001 (most fails, VT nil)"]).mean()))
        emit("tenor_check", tag, "share 10y fell >= 1.33 pt", float((d10 <= -1.33075).mean()))
        emit("tenor_check", tag, "s.d. 1y change", float(d1.std()))
        emit("tenor_check", tag, "s.d. 10y change", float(d10.std()))
        emit("tenor_check", tag, "s.d. parallel-equivalent", float(ss.std()))
        r90 = [r for r in allr if r["start"].year >= 1990]
        emit("tenor_check", tag + " 1990-", "s.d. 1y change", float(np.std([r["d1"] for r in r90])))
        emit("tenor_check", tag + " 1990-", "s.d. 10y change", float(np.std([r["d10"] for r in r90])))
        emit("tenor_check", tag + " 1990-", "s.d. parallel-equivalent", float(np.std([100 * r["s"] for r in r90])))
        emit("tenor_check", tag, "house model s.d. over 56 days (0.9 pt a year)", 0.9 * math.sqrt(56 / 365.25))
        for name, f in TESTS[:5]:
            for e in episodes(allr, f):
                emit("episode", f"{tag}; {name}", f"{e['first']} to {e['last']}", e["max_topup"],
                     f"largest at {e['at']}: fall {e['fall']:.2f} pt, 10y at start {e['lvl10']:.2f}%, "
                     f"in recession {e['rec_now']}, recession within 14 months {e['rec_14']}")

# the same eight weeks every year: close on or before 6 Nov to the first January close
for y in range(1962, 2026):
    i = bisect_right(DAYS, date(y, 11, 6)) - 1
    j = next(k for k in range(i, len(DAYS)) if DAYS[k] >= date(y + 1, 1, 2))
    dch, lvl, n = changes(i, j)
    cost, cv = ten_cost(curve_from(dch))
    p = plan_at(cost, cv)
    cost_p, cvp = ten_cost(curve_from(dch, True, lvl))
    pp = plan_at(cost_p, cvp)
    emit("same_weeks", f"{DAYS[i]} to {DAYS[j]}", "top-up / completion / VT (abs); top-up (prop)",
         f"{p['topup']:.0f} / {p['completion']:.0f} / {p['vt']:.0f}; {pp['topup']:.0f}",
         f"fall {-100 * p['s']:.2f} pt; 10y {dch[10]:+.2f}, 20y {dch[20]:+.2f}, 1y {dch[1]:+.2f}; 10y at start "
         f"{lvl[10]:.2f}%; recession at start {mk(DAYS[i]) in REC}; within 14 months "
         f"{any(m in REC for m in range(mk(DAYS[i]), mk(DAYS[i]) + 15))}")

SW = [x for x in out if x[0] == "same_weeks"]
for lab, y0 in (("1962-2025", 1962), ("1990-2025", 1990)):
    tu = [float(x[3].split(" / ")[0]) for x in SW if int(x[1][:4]) >= y0]
    vt = [float(x[3].split("; ")[0].split(" / ")[2]) for x in SW if int(x[1][:4]) >= y0]
    for k, f in (("years", lambda v: True), ("top-up $0", lambda v: v == 0), ("top-up > $10,000", lambda v: v > 10_000),
                 ("top-up > $20,000", lambda v: v > 20_000), ("top-up > $38,282", lambda v: v > 38_282)):
        emit("same_weeks_summary", lab, k, sum(1 for v in tu if f(v)))
    emit("same_weeks_summary", lab, "median top-up", float(np.median(tu)))
    emit("same_weeks_summary", lab, "smallest VT bought", min(vt))

# episodes counted (clusters of overlapping windows whose starts lie within 60 days), 56 days abs
r56 = RUNS[(56, False)]
for name, f in TESTS[:5]:
    eps = episodes(r56, f)
    for lab, y0 in (("1962-", 1962), ("1990-", 1990)):
        e2 = [e for e in eps if e["first"].year >= y0]
        emit("episode_count", f"56 days abs; {lab}", name, len(e2),
             f"in a recession at the start {sum(e['rec_now'] for e in e2)}; recession within 14 months "
             f"{sum(e['rec_14'] for e in e2)}")

# recessions: the parallel-equivalent change from the peak month's last close to the trough month's last close, and
# the largest 56-day fall starting inside each
rows56 = RUNS[(56, False)]
for (py, pm), (ty, tm) in NBER:
    if py < 1962:
        continue                                      # before the data
    i = bisect_right(DAYS, month_end(py, pm)) - 1     # last close of the peak month
    j = bisect_right(DAYS, month_end(ty, tm)) - 1     # last close of the trough month
    dch, lvl, n = changes(i, j)
    cost, cv = ten_cost(curve_from(dch))
    inside = [r for r in rows56 if mk(r["start"]) in range(py * 12 + pm, ty * 12 + tm)]
    best = max(inside, key=lambda r: r["topup"]) if inside else None
    emit("recession", f"peak {py}-{pm:02d} to trough {ty}-{tm:02d}", "10y change peak-to-trough (points)", dch[10],
         f"parallel-equivalent {100 * s_equiv(cost):+.2f} pt; 1y {dch[1]:+.2f}; largest 56-day top-up starting inside "
         + (f"${best['topup']:,.0f} (start {best['start']}, fall {-100 * best['s']:.2f} pt)" if best else "n/a"))

with open(OUT, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["section", "sample", "item", "value", "note"])
    w.writerows(out)

print(f"cost {BASE_COST:,.0f}  dv01 {DV01:.1f}  key rates", {k: round(v, 1) for k, v in KR.items()})
print("thresholds (points)", {k: round(v, 3) for k, v in THR.items()})
print("central", {k: round(v) if abs(v) > 1 else round(v, 5) for k, v in P0.items()})
print("13 Nov", round(cost13), {k: round(v) if abs(v) > 1 else round(v, 5) for k, v in p13.items()})
print(f"wrote {OUT} ({len(out)} rows)")
