"""Card Q81's counts, as code: waiting cash at zero in the 3-month bill's record (numbers owner, Mon 16 Nov 2026, Sydney).
Outside facts (FRED TB3MS) and one MODEL replay through the register's engine. NUMBERS 8a's bullet "Waiting cash at
zero is history".

Run from the repo root:  python3 -I keel/final_report/numbers/waiting_cash_zero.py
   or from this folder:  python3 -I waiting_cash_zero.py
Writes keel/final_report/numbers/results_waiting_cash_zero_2026-11-16.json and prints every claim with the card's figure,
this script's figure and whether they agree (about 40 seconds; numpy only). Imports engine.py and completion.py and
changes neither; reads no results file.

Input: `keel/final_report/research/cards/data/Q81_bill_rate_months.csv`, FRED TB3MS (3-month bill, secondary market,
discount basis, monthly average), Jan 1934 to Jun 2026, 1,110 months, saved by card Q81 on Mon 16 Nov 2026 (copy last
updated 1 Jul 2026). Its 0/1 columns are re-derived from the rate and must agree (asserted). The card's daily rows
(27, 28) and its note on Jul-Oct 2026 read the repo's FRED daily files `archive/rab/data/fred/DGS1MO.csv` and
`DGS3MO.csv`, as the card says it did.

Conventions, as the card states them (its "How the months were counted"):
  * a month counts if its average is strictly below the line (0.07%, 0.15% or 0.25%); "at or below" is also given;
  * a spell is a run of consecutive counted months; "modern" spells start in January 2008 or later;
  * windows are consecutive months (180 for 15 years, 192 for 16, 12 for one); growth compounds each month at
    (rate - fee) / 12 and is stated as a yearly rate, (product)^(12 / months) - 1;
  * the replay maps a historical month onto January 2027 (month k of the window is month k from Jan 2027) and lets every
    waiting dollar (coupons, fund payouts, carried surplus, the iBond funds' cash in their last months) earn that month's
    bill rate less 0.15%, continuously, day by day within the month, through the register's ledger
    (completion.ledger, design H_plain: the ten rungs and the backstop as bought). Flat rates use completion.Flat.
    Continuous compounding is the one that reproduces the card's $2,454 and $7,238 to the dollar; monthly compounding
    gives $2,451 and $7,222, simple interest $2,454 and $7,232 (printed, for the record).
"""
import csv
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import completion as C    # noqa: E402

RUN = "Mon 16 Nov 2026 (Sydney)"
DATA = HERE.parent / "research/cards/data/Q81_bill_rate_months.csv"
DAILY1, DAILY3 = E.ROOT / "archive/rab/data/fred/DGS1MO.csv", E.ROOT / "archive/rab/data/fred/DGS3MO.csv"
OUTFILE = HERE / f"results_waiting_cash_zero_{C.RESULTS}.json"   # Tue 17 Nov evening re-run; the 2026-11-16 file is the record
LINES = (0.07, 0.15, 0.25)
FEE = 0.15                      # % a year: the register's waiting-ETF fee (NUMBERS 0)

rows = list(csv.DictReader(open(DATA)))
keys = [r["date"][:7] for r in rows]
rate = np.array([float(r["tb3ms_pct"]) for r in rows])
N = len(rate)
for th in LINES:                                       # the file's own flags agree with the rule "strictly below"
    col = np.array([int(r[f"below_{th:.2f}"]) for r in rows], bool)
    assert np.array_equal(col, rate < th - 1e-9), th
for f, col in ((0.07, "net_of_0.07_fee"), (0.15, "net_of_0.15_fee")):
    assert np.allclose([float(r[col]) for r in rows], rate - f, atol=0.0051), col
i08 = keys.index("2008-01")
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def lab(k):
    return f"{MON[int(k[5:7]) - 1]} {k[:4]}"


def spells(mask, lo=0, hi=None):
    """Runs of consecutive True months in mask[lo:hi]: (start index, end index, length)."""
    hi = N if hi is None else hi
    out, s = [], None
    for i in range(lo, hi):
        if mask[i] and s is None:
            s = i
        if (not mask[i] or i == hi - 1) and s is not None:
            e = i if mask[i] else i - 1
            out.append((s, e, e - s + 1))
            s = None
    return out


def sp(t):
    s, e, n = t
    return f"{lab(keys[s])}-{lab(keys[e])} ({n})" if n > 1 else f"{lab(keys[s])} (1)"


def ann(seg, fee=0.0):
    """Yearly rate (%) of monthly compounding at (rate - fee) / 12 over the months in seg."""
    g = np.prod(1 + (np.asarray(seg) - fee) / 1200)
    return (g ** (12 / len(seg)) - 1) * 100


claims = []


def claim(cid, what, card, got, ok=None, note=""):
    """Record one claim: the card's figure (as it prints it), this script's, whether they agree, and a note."""
    if ok is None:
        ok = str(card) == str(got)
    claims.append({"id": cid, "claim": what, "card": card, "script": got, "reproduced": bool(ok), "note": note})


# ---------------------------------------------------------------- rows 1, 2 and the verdict lines 17-19, 40
claim("months", "Months in the copy, Jan 1934 to Jun 2026 / since Jan 2008", "1,110 / 222", f"{N:,} / {N - i08}")
CARD12 = {0.07: ("83", "7.5%", "12", "53", "23.9%", "19 (Jan 2014-Jul 2015)"),
          0.15: ("141", "12.7%", "9", "90", "40.5%", "58 (Feb 2011-Nov 2015)"),
          0.25: ("191", "17.2%", "7", "108", "48.6%", "82 (Mar 2009-Dec 2015)")}
for th in LINES:
    m = rate < th - 1e-9
    sps = spells(m)
    lg = max(sps, key=lambda t: t[2])
    c = CARD12[th]
    claim(f"r1_{th}_count", f"Under {th:.2f}% since 1934: months", c[0], f"{int(m.sum())}")
    claim(f"r1_{th}_share", f"Under {th:.2f}% since 1934: share", c[1], f"{m.mean():.1%}")
    claim(f"r1_{th}_spells", f"Under {th:.2f}% since 1934: spells", c[2], f"{len(sps)}")
    claim(f"r2_{th}_count", f"Under {th:.2f}% since Jan 2008: months", c[3], f"{int(m[i08:].sum())}")
    claim(f"r2_{th}_share", f"Under {th:.2f}% since Jan 2008: share of 222", c[4], f"{m[i08:].mean():.1%}")
    claim(f"r1_{th}_longest", f"Under {th:.2f}%: longest spell", c[5],
          f"{lg[2]} ({lab(keys[lg[0]])}-{lab(keys[lg[1]])})")
CARD_LE = {0.07: (90, 59), 0.15: (156, 94), 0.25: (194, 108)}
for th in LINES:
    m = rate <= th + 1e-9
    claim(f"le_{th}", f"At or below {th:.2f}%: months since 1934 / since 2008", f"{CARD_LE[th][0]} / {CARD_LE[th][1]}",
          f"{int(m.sum())} / {int(m[i08:].sum())}")
lg_le = max(spells(rate <= 0.07 + 1e-9), key=lambda t: t[2])
claim("le_0.07_longest", "At or below 0.07%: longest spell", "31 (Apr 2013-Oct 2015)",
      f"{lg_le[2]} ({lab(keys[lg_le[0]])}-{lab(keys[lg_le[1]])})")
i23 = keys.index("2023-01")
m25 = rate < 0.25 - 1e-9
lg0822 = max(spells(m25, i08, i23), key=lambda t: t[2])
claim("q2d_check", "Q2d's 0.25% counts, 2008-2022: months / longest", "108 / 82",
      f"{int(m25[i08:i23].sum())} / {lg0822[2]}")

# ---------------------------------------------------------------- rows 3 and 4: the modern spells
m07, m15 = rate < 0.07 - 1e-9, rate < 0.15 - 1e-9
mod07 = [t for t in spells(m07) if t[0] >= i08]
claim("r3", "Modern spells under 0.07%",
      "Dec 2008 (1), Nov 2009-Jan 2010 (3), Apr 2011-Jan 2012 (10), Apr 2013-Oct 2013 (7), Jan 2014-Jul 2015 (19), "
      "Sep 2015-Oct 2015 (2), Feb 2021-Dec 2021 (11)", ", ".join(sp(t) for t in mod07))
claim("r3_blip", "Aug 2015's rate (the blip that breaks the 2014-15 spell)", "0.07", f"{rate[keys.index('2015-08')]:.2f}")
mod15 = [t for t in spells(m15) if t[0] >= i08]
claim("r4", "Modern spells under 0.15%",
      "Dec 2008-Jan 2009 (2), Sep 2009-Feb 2010 (6), Jun 2010 (1), Oct 2010-Dec 2010 (3), Feb 2011-Nov 2015 (58), "
      "Apr 2020-May 2020 (2), Jul 2020-Dec 2021 (18)", ", ".join(sp(t) for t in mod15))
for (s, e, n), card in zip([t for t in mod15 if t[2] in (58, 18)], ("0.052%", "0.064%")):
    claim(f"r4_avg_{n}", f"Average rate in the {n}-month spell", card, f"{rate[s:e + 1].mean():.3f}%")

# ---------------------------------------------------------------- row 5: the 1930s
i50 = keys.index("1950-01")
old07 = [t for t in spells(m07) if t[0] < i50]
claim("r5_07", "1930s under 0.07%: months, first-last month, spells, longest",
      "30, May 1938-Feb 1941, 5, 11 (Oct 1938-Aug 1939)",
      f"{sum(t[2] for t in old07)}, {lab(keys[old07[0][0]])}-{lab(keys[old07[-1][1]])}, {len(old07)}, "
      f"{max(t[2] for t in old07)} ({lab(keys[max(old07, key=lambda t: t[2])[0]])}-"
      f"{lab(keys[max(old07, key=lambda t: t[2])[1]])})")
old15 = max([t for t in spells(m15) if t[0] < i50], key=lambda t: t[2])
claim("r5_15", "1930s under 0.15% running: months, dates, average", "48, Nov 1937-Oct 1941, 0.060%",
      f"{old15[2]}, {lab(keys[old15[0]])}-{lab(keys[old15[1]])}, {rate[old15[0]:old15[1] + 1].mean():.3f}%")
lowest = [lab(keys[i]) for i in np.where(rate == rate.min())[0]]
claim("r5_low", "Lowest month on record (0.01%)", "Jan 1940, Sep 2011, Nov 2011, Dec 2011",
      f"{', '.join(lowest)} at {rate.min():.2f}%",
      ok=(lowest == ["Jan 1940", "Sep 2011", "Nov 2011", "Dec 2011"] and rate.min() == 0.01))
other15 = [sp(t) for t in spells(m15) if t[0] < i08 and t != old15]
claim("r1_015_other", "Under 0.15% before 2008 outside the 1937-41 spell (not stated on the card; shown so the 141 adds up)",
      "(not stated)", "; ".join(other15) or "none", ok=True)

# ---------------------------------------------------------------- row 6: dates of the two eras under 0.25%
e1 = [t for t in spells(m25) if t[0] >= i08]
claim("r6_eras", "Under 0.25% since 2008 (spells)", "Nov 2008 to Dec 2015 with Feb 2009 at 0.30%; Apr 2020 to Jan 2022",
      f"{'; '.join(sp(t) for t in e1)}; Feb 2009 at {rate[keys.index('2009-02')]:.2f}%",
      ok=(lab(keys[e1[0][0]]) == "Nov 2008" and rate[keys.index("2009-02")] == 0.30
          and lab(keys[e1[1][1]]) == "Dec 2015" and sp(e1[-1]).startswith("Apr 2020-Jan 2022")),
      note=f"The two eras hold. The card leaves out one stray month under 0.25%, Apr 2016 "
           f"({rate[keys.index('2016-04')]:.2f}%), which its count of 108 since 2008 includes.")
claim("r6_2022", "Jan 2022 / Feb 2022", "0.15% / 0.33%",
      f"{rate[keys.index('2022-01')]:.2f}% / {rate[keys.index('2022-02')]:.2f}%")

# ---------------------------------------------------------------- row 7: the last fifteen years
i11 = keys.index("2011-07")
w = m15[i11:]
claim("r7", "Jul 2011-Jun 2026: months under 0.15%, share, 2011-15 era, 2020-21 era", "73, 40.6%, 53, 20",
      f"{int(w.sum())} of {w.size}, {w.mean():.1%}, {int(m15[i11:keys.index('2016-01')].sum())}, "
      f"{int(m15[keys.index('2020-01'):keys.index('2022-01')].sum())}",
      ok=(int(w.sum()) == 73 and f"{w.mean():.1%}" == "40.6%" and int(m15[i11:keys.index('2016-01')].sum()) == 53
          and int(m15[keys.index('2020-01'):keys.index('2022-01')].sum()) == 20))

# ---------------------------------------------------------------- row 8: the lowest calendar years
yrs = {}
for k, r in zip(keys, rate):
    yrs.setdefault(k[:4], []).append(r)
full = {y: float(np.mean(v)) for y, v in yrs.items() if len(v) == 12}
low = sorted(full.items(), key=lambda t: t[1])[:6]
CARD8 = [("2014", 0.033), ("1940", 0.036), ("2021", 0.044), ("1939", 0.046), ("2011", 0.052), ("2015", 0.052)]
claim("r8", "Lowest calendar years (mean of monthly averages)",
      "2014 0.033%, 1940 0.036%, 2021 0.044%, 1939 0.046%, 2011 0.052%, 2015 0.052%",
      ", ".join(f"{y} {v:.4f}%" for y, v in low),
      ok=(sorted(y for y, _ in low) == sorted(y for y, _ in CARD8)
          and all(abs(full[y] - v) <= 0.0005 + 1e-12 for y, v in CARD8)),
      note="Same six years, same order (2011 and 2015 tie). 2014 is 0.0325% and 2011 and 2015 are 0.0525% each, "
           "exactly; the card rounds the first up (0.033%) and the other two down (0.052%).")

# ---------------------------------------------------------------- row 9: the most a 15- or 16-year window held
def window_max(mask, n):
    cs = np.r_[0, np.cumsum(mask)]
    cnt = cs[n:] - cs[:-n]
    mx = int(cnt.max())
    st = [keys[i] for i in np.where(cnt == mx)[0]]
    return mx, st, cnt.size


mx15_180, st15_180, nw180 = window_max(m15, 180)
mx25_180, _, _ = window_max(m25, 180)
mx15_192, st15_192, nw192 = window_max(m15, 192)
claim("r9_180", "Most months under 0.15% / 0.25% in any 180-month window", "90 (50%) / 108 (60%)",
      f"{mx15_180} ({mx15_180 / 180:.0%}) / {mx25_180} ({mx25_180 / 180:.0%})")
claim("r9_192", "Most months under 0.15% in any 192-month window", "90 of 192 (47%)",
      f"{mx15_192} of 192 ({mx15_192 / 192:.0%})")
claim("r9_starts", "The worst windows (most months under 0.15%) start: 16-year windows", "Jan 2007-Dec 2008",
      f"{lab(st15_192[0])}-{lab(st15_192[-1])} ({len(st15_192)} starts)",
      ok=(lab(st15_192[0]) == "Jan 2007" and lab(st15_192[-1]) == "Dec 2008"),
      note="The card's dates follow 'for 16 years', but they are the 15-year windows' (next line); "
           "every 16-year window from Jan 2006 to Dec 2008 holds all 90 modern months.")
claim("r9_starts_180", "The worst windows (most months under 0.15%) start: 15-year windows", "Jan 2007-Dec 2008",
      f"{lab(st15_180[0])}-{lab(st15_180[-1])} ({len(st15_180)} starts)",
      ok=(lab(st15_180[0]) == "Jan 2007" and lab(st15_180[-1]) == "Dec 2008"))

# ---------------------------------------------------------------- row 10: the two long spells, compounded
for th, n, c_g, c_n in ((0.25, 82, "0.078%", "-0.072%"), (0.15, 58, "0.052%", "-0.098%")):
    s, e, _ = max(spells(rate < th - 1e-9), key=lambda t: t[2])
    seg = rate[s:e + 1]
    claim(f"r10_{n}", f"The {n}-month spell under {th:.2f}%: a year, gross / after 0.15%", f"{c_g} / {c_n}",
          f"{ann(seg):.3f}% / {ann(seg, FEE):.3f}%")

# ---------------------------------------------------------------- rows 11 and 12: the worst windows after the fee
def worst(n, lo=0):
    best = None
    for i in range(lo, N - n + 1):
        v = ann(rate[i:i + n], FEE)
        if best is None or v < best[0]:
            best = (v, i)
    v, i = best
    return v, ann(rate[i:i + n]), f"{lab(keys[i])}-{lab(keys[i + n - 1])}"


w192 = worst(192)
claim("r11_192", "Worst 16 years: dates, a year gross, after the fee", "Jan 1934-Dec 1949, 0.36%, +0.21%",
      f"{w192[2]}, {w192[1]:.2f}%, {w192[0]:+.2f}%")
w180 = worst(180)
claim("r11_180", "Worst 15 years: dates, after the fee", "Jan 1934-Dec 1948, +0.16%", f"{w180[2]}, {w180[0]:+.2f}%")
w180b = worst(180, keys.index("1948-01"))
claim("r11_180_since48", "Worst 15 years starting 1948 or later: dates, after the fee", "Nov 2007-Oct 2022, +0.48%",
      f"{w180b[2]}, {w180b[0]:+.2f}%")
w12 = worst(12)
claim("r12", "Worst 12 months after the fee: dates, return", "Aug 2014-Jul 2015, -0.126%", f"{w12[2]}, {w12[0]:.3f}%")
claim("r12_vs_test", "The test's -0.15% sits below every 12-month span since 1934", "yes",
      "yes" if w12[0] > -FEE else "no")

# ---------------------------------------------------------------- rows 13 and 14: the register's engine
D = C.design()
OWN, POOL = D["own"], D["pool"]


class BillPath(E.Reinvest):
    """Waiting money earns a historical month's bill rate less the fee, continuously within each month (mode 'cont');
    month k of the window is month k from January 2027. 'month' and 'simple' are the record's other conventions."""

    def __init__(self, seg, fee=FEE, mode="cont"):
        super().__init__(C.c, "flat")
        self.seg, self.fee, self.mode = np.asarray(seg) / 100, fee / 100, mode

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        g, t = 1.0, d1
        while t < d2:
            k = min(max((t.year - 2027) * 12 + t.month - 1, 0), len(self.seg) - 1)
            nxt_m = date(t.year + (t.month == 12), 1 if t.month == 12 else t.month + 1, 1)
            nxt = min(nxt_m, d2)
            r, days = self.seg[k] - self.fee, (nxt - t).days
            if self.mode == "cont":
                g *= math.exp(r * days / 365.25)
            elif self.mode == "month":
                g *= (1 + r / 12) ** (days / (nxt_m - date(t.year, t.month, 1)).days)
            else:
                g *= 1 + r * days / 365.25
            t = nxt
        return g


def run_ledger(world):
    paid, _, _, left = C.ledger(world, OWN, POOL)
    return sum(paid.values()), left


replay = {}
for mode in ("cont", "month", "simple"):
    res = []
    for i in range(N - 192 + 1):
        p, left = run_ledger(BillPath(rate[i:i + 192], mode=mode))
        res.append((keys[i], p, left))
    replay[mode] = res
rc = replay["cont"]
all_paid = all(abs(p - len(E.YEARS) * E.PAYMENT) < 1e-6 for _, p, _ in rc)
lo = min(rc, key=lambda t: t[2])
nov08 = next(t for t in rc if t[0] == "2008-11")
claim("r13_n", "Replay: start months, first-last", "919, Jan 1934-Jul 2010", f"{len(rc)}, {lab(rc[0][0])}-{lab(rc[-1][0])}")
claim("r13_paid", "Replay: all ten paid in every start month", "yes", "yes" if all_paid else "no")
claim("r13_least", "Replay: least left after 2042, and its start", "$2,454 (start Jan 1934)",
      f"{C.fmt(lo[2])} (start {lab(lo[0])})")
claim("r13_nov08", "Replay: left after 2042, start Nov 2008", "$7,238", C.fmt(nov08[2]))
left0 = run_ledger(C.Flat(C.c, 0.0))[1]
leftf = run_ledger(C.Flat(C.c, -C.WAIT_FEE))[1]
claim("r13_flat", "Flat 0% / flat -0.15%: left after 2042 (NUMBERS 2)", "$1,414 / $0", f"{C.fmt(left0)} / {C.fmt(leftf)}")
for r, card in ((-0.0007, "$751"), (-0.0008, "$656"), (-0.0011, "$374"), (0.0016, "$2,957"), (0.0048, "$6,149")):
    v = run_ledger(C.Flat(C.c, r))[1]
    claim(f"r14_{r:+.4f}", f"Flat {r:+.2%} held 2027-2042: left after 2042", card, f"${round(v, 2):,.2f}",
          ok=abs(v - float(card.strip("$").replace(",", ""))) <= 0.5)
other = {m: (C.fmt(min(replay[m], key=lambda t: t[2])[2]), C.fmt(next(t for t in replay[m] if t[0] == "2008-11")[2]))
         for m in ("month", "simple")}

# ---------------------------------------------------------------- the card's note on Jul-Oct 2026 (line 39)
n4 = N + 4
shares = {}
for th in LINES:
    m = rate < th - 1e-9
    shares[th] = {"since_1934": (m.mean() * 100, m.sum() / n4 * 100), "since_2008": (m[i08:].mean() * 100,
                                                                                   m[i08:].sum() / (N - i08 + 4) * 100)}
moves = {th: {k: round(a - b, 2) for k, (a, b) in v.items()} for th, v in shares.items()}
mx_move = max(abs(x) for v in moves.values() for x in v.values())
mx_move_1934 = max(abs(v["since_1934"]) for v in moves.values())


def daily(path, col):
    out = []
    for r in csv.DictReader(open(path)):
        if r[col] not in ("", "."):
            out.append((r["observation_date"], float(r[col])))
    return out


d3 = daily(DAILY3, "DGS3MO")
jul_sep = [v for d, v in d3 if "2026-07-01" <= d <= "2026-09-30"]
claim("note_1114", "Months to Oct 2026 with Jul-Oct 2026 added", "1,114", f"{n4:,}")
claim("note_dgs3mo", "Daily DGS3MO, Jul to 25 Sep 2026: lowest", "never below 3.82%", f"{min(jul_sep):.2f}%",
      ok=min(jul_sep) >= 3.82)
claim("note_04", "Shares change by at most 0.4 points with four more months above every line",
      "at most 0.4 points", f"at most {mx_move:.2f} points (since 1934: {mx_move_1934:.2f}; since 2008: "
      f"0.07% {moves[0.07]['since_2008']:.2f}, 0.15% {moves[0.15]['since_2008']:.2f}, 0.25% {moves[0.25]['since_2008']:.2f})",
      ok=mx_move <= 0.4 + 1e-9,
      note=f"Holds for the since-1934 shares (at most {mx_move_1934:.2f} points). Not for the since-2008 shares: "
           f"with Jul-Oct 2026 the 0.15% share is {shares[0.15]['since_2008'][1]:.1f}% (90 of 226), not 40.5%, "
           f"and the 0.25% share {shares[0.25]['since_2008'][1]:.1f}% (108 of 226), not 48.6%.")

# ---------------------------------------------------------------- rows 27 and 28: the repo's daily files
d1m = [(d, v) for d, v in daily(DAILY1, "DGS1MO") if d >= "2008-01-01"]
z1 = [d for d, v in d1m if v == 0.0]
by_y = {}
for d in z1:
    by_y[d[:4]] = by_y.get(d[:4], 0) + 1
claim("r27_zero", "DGS1MO at exactly 0.00 since 2008: days, first, last, 2015, 2011", "100, 2008-12-10, 2021-06-03, 39, 34",
      f"{len(z1)}, {z1[0]}, {z1[-1]}, {by_y.get('2015', 0)}, {by_y.get('2011', 0)}")
u07 = [v < 0.07 - 1e-9 for _, v in d1m]
run, best, bs, s = 0, 0, None, None
for (d, _), u in zip(d1m, u07):
    if u:
        run += 1
        s = d if run == 1 else s
        if run > best:
            best, bs, be = run, s, d
    else:
        run = 0
claim("r27_07", "DGS1MO under 0.07% since 2008: days of all, share, longest run", "1,415 of 4,687, 30.2%, 398 (2014-03-20 to 2015-10-19)",
      f"{sum(u07):,} of {len(d1m):,}, {sum(u07) / len(d1m):.1%}, {best} ({bs} to {be})")
d3m = [(d, v) for d, v in d3 if d >= "2008-01-01"]
run, best, s = 0, 0, None
for d, v in d3m:
    if v < 0.15 - 1e-9:
        run += 1
        s = d if run == 1 else s
        if run > best:
            best, bs, be = run, s, d
    else:
        run = 0
z3 = sorted({d[:4] for d, v in d3m if v == 0.0})
claim("r28", "DGS3MO since 2008: longest run under 0.15%; days at exactly 0.00 (years)",
      "1,180 (2011-03-01 to 2015-11-13); 21 (2008, 2011, 2013, 2015, 2020)",
      f"{best:,} ({bs} to {be}); {sum(1 for _, v in d3m if v == 0.0)} ({', '.join(z3)})")

# ---------------------------------------------------------------- Q2d row 8, cited by row 31
m50 = rate < 0.50 - 1e-9
s50 = max([t for t in spells(m50) if t[0] < i50], key=lambda t: t[2])
claim("r31_q2d", "Longest spell under 0.50% in the 1930s-40s (Q2d row 8, cited by row 31)", "122",
      f"{s50[2]} ({lab(keys[s50[0]])}-{lab(keys[s50[1]])})", ok=(s50[2] == 122))

# ---------------------------------------------------------------- write and print
bad = [c for c in claims if not c["reproduced"]]
out = {"stamp": {"run": RUN, "data": str(DATA.relative_to(E.ROOT)), "months": N, "first": keys[0], "last": keys[-1],
                 "status": "Outside facts (FRED TB3MS) and Keel arithmetic; rows 13-14 MODEL on the register's engine",
                 "card": "keel/final_report/research/cards/Q81_waiting_cash_at_zero.md",
                 "replay_convention": "continuous within each month at (bill rate - 0.15%); month k of the window = "
                                      "month k from Jan 2027; completion.ledger, design H_plain"},
       "claims": claims, "not_reproduced": [c["id"] for c in bad],
       "replay": {"windows": len(rc), "all_paid": all_paid, "least_left": lo[2], "least_start": lo[0],
                  "left_nov2008": nov08[2], "left_p5_p50_p95": [float(np.percentile([t[2] for t in rc], q)) for q in (5, 50, 95)],
                  "other_conventions_least_and_nov2008": other, "flat_0pct": left0, "flat_minus_fee": leftf},
       "share_moves_with_jul_oct_2026": moves}
OUTFILE.write_text(json.dumps(out, indent=1, default=float))
for c in claims:
    print(("OK  " if c["reproduced"] else "NO  ") + f"{c['id']}: {c['claim']}\n      card:   {c['card']}\n      script: {c['script']}"
          + (f"\n      note:   {c['note']}" if c["note"] else ""))
print(f"\n{len(claims) - len(bad)} of {len(claims)} reproduced; not reproduced: {[c['id'] for c in bad] or 'none'}")
print("replay, other conventions (least / Nov 2008):", other)
