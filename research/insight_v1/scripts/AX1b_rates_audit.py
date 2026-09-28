"""AX1b_rates_audit.py - independent checks on D1_rates.md (auditor AX1b, insight_v1 run, 2026-09-28).

PROVISIONAL audit research, not team-approved. It reuses D1's own curve code (imported, unchanged) and adds checks
that D1 did not run.

What it checks (plain English):
 [A] Worst 2026 day (Feb 27): what share of the 2033 payment waits under longest-first (D1 says ~71%).
 [B] Gap odds on 2027-01-01 under other reasonable inputs: (i) volatility from shorter 2026 windows; (ii) "unchanged
     curve" drift (today's par curve simply re-dated to 2027-01-01) instead of D1's "forwards come true" drift.
 [C] Model-free cross-check of the tail: how often the 10-year Treasury yield fell by at least 19/26/100/148bp over
     68 trading days (about the 98 calendar days from 2026-09-25 to 2027-01-01), FRED DGS10 since 1962 / 1990 / 2000.
 [D] Staging vs all-at-once when waiting money earns T-bill rates and the curve stays where it is ("unchanged curve"):
     the expected-funding "gain" of staging in D1 [7] is a Jensen's-inequality artefact of its zero-drift assumption.
 [E] Joint tail (no 2028 deposit): unfunded FACE under longest-first vs nearest-first (an extra argument for D1's
     order that D1 did not state).
 [F] Coupon vs zero on the same valuation date: STRIP 912821KC8 priced on 2026-09-25 (D1 compares a 9/25 bond price
     with a 2027-01-01 STRIP price).
 [G] Accrued interest on $50,000 face of the 4.125% 15-Nov-2032 note for realistic trade dates (Sep 29 - Oct 9).
 [H] The -421bp "whole 2028 deposit" break-even: what the short end of the curve would be.

Inputs (status labels):
- Treasury par curves 2026: research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv. AX1b re-downloaded the
  treasury.gov 2026 CSV on 2026-09-28 and it is byte-identical after line-ending normalisation (VERIFIED-PRIMARY).
- FRED DGS10 daily, 1962-01-02 to 2026-09-24: research/insight_v1/scripts/data/D3/fred_DGS10.csv (snapshot by D3;
  VERIFIED-PRIMARY per D3; not re-downloaded by AX1b).
- Curve method, Nov-15 rung dates, deposits: exactly as in D1_purchase_rule.py (ASSUMPTION / VERIFIED-REPO-FILE there).
- Drift choices ("forwards come true" vs "unchanged curve"), 68-trading-day window, T-bill carry from the same curve:
  ASSUMPTIONS for sensitivity only.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/AX1b_rates_audit.py
"""
import csv
import sys
from datetime import date

import numpy as np
from scipy.stats import norm

sys.path.insert(0, "research/insight_v1/scripts")
import D1_purchase_rule as d1  # noqa: E402

ANCHOR = d1.ANCHOR
DEP1, DEP2 = d1.DEP1, d1.DEP2


def redate(row, new_date):
    r = dict(row)
    r["_date"] = new_date
    return r


def main():
    rows = d1.load(d1.SNAP)
    last = rows[-1]

    # [A]
    feb = next(r for r in rows if r["_date"] == date(2026, 2, 27))
    c = d1.rung_costs(feb, ANCHOR, 0, True)
    bought, part, share, gap = d1.longest_first(c, DEP1)
    print(f"[A] 2026-02-27 Nov-15 ladder: cost ${sum(c.values()):,.0f}; gap ${gap:,.0f}; 2033 rung ${c[2033]:,.0f}; "
          f"waiting {(1 - share) * 100:.1f}% of the {part} payment")

    # [B] gap odds sensitivity
    print("\n[B] P(gap on 2027-01-01), Nov-15 ladder and exact-date, under other inputs")
    t = (ANCHOR - last["_date"]).days / 365.25
    for nov in (False, True):
        hist = np.array([sum(d1.rung_costs(r, ANCHOR, 0, nov).values()) for r in rows])
        lr = np.diff(np.log(hist))
        base_fwd = sum(d1.rung_costs(last, ANCHOR, 0, nov).values())
        # unchanged curve: the 2026-09-25 par curve re-dated to 2027-01-01 prices the ladder on that day
        base_unch = sum(d1.rung_costs(redate(last, ANCHOR), ANCHOR, 0, nov).values())
        tag = "Nov-15" if nov else "exact "
        print(f"  {tag}: base (forwards come true) ${base_fwd:,.0f}; base (unchanged curve) ${base_unch:,.0f} "
              f"(+${base_unch - base_fwd:,.0f})")
        for label, window in (("all 2026", len(lr)), ("last 63 days", 63), ("last 21 days", 21)):
            vol = lr[-window:].std(ddof=1) * np.sqrt(252)
            s = vol * np.sqrt(t)
            p_f = 1 - norm.cdf(np.log(DEP1 / base_fwd) / s)
            p_u = 1 - norm.cdf(np.log(DEP1 / base_unch) / s)
            print(f"     vol {label:13s} {vol * 100:5.2f}%: P(gap) forwards {p_f * 100:4.1f}% | unchanged curve "
                  f"{p_u * 100:4.1f}%")

    # [C] model-free frequency from FRED DGS10
    print("\n[C] FRED DGS10: share of 68-trading-day windows in which the 10-year yield FELL by at least X bp")
    dates, ys = [], []
    for r in csv.DictReader(open("research/insight_v1/scripts/data/D3/fred_DGS10.csv")):
        v = r["DGS10"]
        if v not in ("", "."):
            dates.append(date.fromisoformat(r["observation_date"]))
            ys.append(float(v))
    ys = np.array(ys)
    dates = np.array(dates)
    h = 68
    chg = ys[h:] - ys[:-h]
    start = dates[:-h]
    for since in (date(1962, 1, 1), date(1990, 1, 1), date(2000, 1, 1)):
        m = start >= since
        cc = chg[m]
        out = ", ".join(f">= {x}bp {(cc <= -x / 100).mean() * 100:.1f}%" for x in (19, 26, 100, 148))
        print(f"  since {since.year}: {m.sum():,} windows; {out}; largest fall {-cc.min() * 100:.0f}bp")
    big = [(start[i], chg[i]) for i in range(len(chg)) if chg[i] <= -1.48 and start[i] >= date(1990, 1, 1)]
    yrs = sorted({d.year for d, _ in big})
    print(f"  windows since 1990 with a fall >= 148bp start in years: {yrs}")

    # [D] staging vs at once with an 'unchanged curve' drift
    print("\n[D] Staging vs all at once when the curve stays put and waiting cash earns the curve's own short rates")
    f0 = d1.curve(redate(last, ANCHOR))  # today's curve re-dated to 2027-01-01 (unchanged-curve world)
    cost0 = sum(d1.rung_costs(redate(last, ANCHOR), ANCHOR, 0, True).values())
    fr = []
    for q in (0, 0.25, 0.5, 0.75, 1.0):
        when = date(2027, 1, 1) if q == 0 else date(2027, 1 + int(q * 12), 1) if q < 1 else date(2028, 1, 1)
        cash_growth = 1 / f0(when)  # T-bill-like carry from the same curve
        cost_q = sum(d1.rung_costs(redate(last, when), when, 0, True).values())
        fr.append(DEP1 * cash_growth / cost_q)
        print(f"  buy on {when}: funded ratio {fr[-1]:.4f} (at once on 2027-01-01: {fr[0]:.4f})")
    staged = np.mean(fr[:4])
    mu = np.log(fr[0] / fr[4])  # yearly drift of ln(cost / cash) in the unchanged-curve world
    print(f"  four quarterly tranches, no noise: {staged:.4f} ({(staged - fr[0]) * 100:+.2f} points vs at once); "
          f"drift of ln(cost/cash) {mu * 100:+.2f}%/yr")
    rng = np.random.default_rng(20260928)
    sig = 0.0716
    n, steps = 200_000, 252
    dt = 1 / steps
    z = rng.standard_normal((n, steps)) * sig * np.sqrt(dt) + (mu - 0.5 * sig ** 2) * dt
    x = np.c_[np.zeros(n), np.cumsum(z, axis=1)]
    F0 = fr[0]
    st = F0 * np.mean(np.exp(-x[:, [0, 63, 126, 189]]), axis=1)
    frp = F0 * np.exp(-x)
    hit = frp >= 1.05
    first = np.where(hit.any(axis=1), hit.argmax(axis=1), steps)
    trig = frp[np.arange(n), first]
    for name, arr in (("4 quarterly tranches", st), ("5% trigger / year-end", trig)):
        print(f"  with noise (vol 7.16%, drift above): {name:22s} mean {arr.mean():.4f} "
              f"({(arr.mean() - F0) * 100:+.2f} points); P(<1.00) {(arr < 1).mean() * 100:.1f}%; "
              f"p5 {np.percentile(arr, 5):.4f}")

    # [E] unfunded face if no 2028 deposit: longest-first vs nearest-first
    print("\n[E] No 2028 deposit: unfunded FACE by buying order (Nov-15 ladder)")
    for bp in (-50, -100):
        c = d1.rung_costs(last, ANCHOR, bp, True)
        gap = sum(c.values()) - DEP1
        lf = gap / c[2033] * 50_000
        nf = gap / c[2042] * 50_000 if gap < c[2042] else None
        print(f"  {bp:+d}bp: gap ${gap:,.0f}. Longest-first leaves ${lf:,.0f} of the 2033 payment unfunded; "
              f"nearest-first leaves ${nf:,.0f} of the 2042 payment unfunded (+${nf - lf:,.0f} face)")

    # [F] coupon vs zero on the same date
    f_today = d1.curve(last)
    strip_today = 50_000 * f_today(date(2032, 11, 15))
    strip_jan = 50_000 * f_today(date(2032, 11, 15)) / f_today(ANCHOR)
    print(f"\n[F] Principal STRIP 912821KC8, $50,000 face (model): ${strip_today:,.0f} on 2026-09-25; "
          f"${strip_jan:,.0f} on 2027-01-01 forward (D1/S3 quote $37,253)")

    # [G] accrued interest on $50,000 face of the 4.125% Nov-2032 note
    print("\n[G] Accrued interest, $50,000 face of 4.125% 15-Nov-2032 (actual/actual, last coupon 2026-05-15)")
    for d in (date(2026, 9, 25), date(2026, 9, 29), date(2026, 10, 2), date(2026, 10, 9)):
        ai = 50_000 * 0.04125 / 2 * (d - date(2026, 5, 15)).days / (date(2026, 11, 15) - date(2026, 5, 15)).days
        print(f"  settle {d}: ${ai:,.0f}")

    # [H] short end at the -421bp break-even
    sh = {k: float(last[k]) - 4.21 for k in ("1 Mo", "3 Mo", "1 Yr", "2 Yr", "10 Yr")}
    print("\n[H] Par yields after a -421bp parallel shift: " + ", ".join(f"{k} {v:.2f}%" for k, v in sh.items()))


if __name__ == "__main__":
    main()
