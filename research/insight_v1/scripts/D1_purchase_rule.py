"""D1_purchase_rule.py - the January 2027 ladder purchase rule if rates fall first (question M004).

Agent D1 (Rates & Fixed-Income Analyst), insight_v1 run, 2026-09-28. PROVISIONAL research, not team-approved.

What it answers (plain English):
 [1] What the ten-payment ladder costs on 2027-01-01 after parallel rate falls, for exact-date zeros (the verified
     $292,264 method) and for the real Nov-15 STRIPS ladder (S1/S3: $294,387), and how big the gap over $300,000 is.
 [2] "Longest rungs first": which payments $300,000 buys, which part waits for the 2028 deposit, and how much of the
     $150,000 deposit that uses (in 2028 dollars, on the shocked curve's forwards).
 [3] Why longest-first: how much MORE the waiting part costs if rates fall another 100bp during 2027, longest-first
     (waiting part = earliest payments) versus nearest-first (waiting part = latest payments).
 [4] Break-even rate falls: gap = 0, gap = the whole first payment, gap = the whole 2028 deposit.
 [5] The same rule on every 2026 curve date (worst 2026 day) and on the case PDF's creation date (2026-09-10).
 [6] Model distribution of the gap on 2027-01-01 (zero-drift lognormal, 2026 realised volatility).
 [7] Buy at once vs staged (4 quarterly tranches in 2027) vs a yield trigger: same expected funded ratio, more spread.
 [8] Joint tail: rates fall AND the 2028 deposit is missing/half/late - how much of which payment is unfunded.

Inputs (status labels):
- Treasury Daily Par Yield Curve 2026, all dates to 2026-09-25: research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv
  (snapshot of the home.treasury.gov CSV saved by agent D3 on 2026-09-28; VERIFIED-PRIMARY per D3). Its 09/25/2026
  row equals competition/official_market_data/daily-treasury-rates_2026-09.csv (VERIFIED-REPO-FILE); checked below.
- Curve method (par = semiannual BEY, linear interpolation on a 0.5y grid, bootstrap, log-linear DF): ASSUMPTION,
  identical to research/verified_2026-09-27/official_curve_pv.py and A2_curve_recheck.py.
- Nov-15 rung dates (payment on Jan 1 of year Y funded by a STRIP maturing Nov 15 of Y-1): from
  research/insight_v1/wins_now/S3_final_report_ladder_and_reserve.md (VERIFIED-PRIMARY MSPD Table V per S1).
  ASSUMPTION: STRIPS priced on the par-derived zero curve; dealer mark-ups ignored (UNVERIFIED, would add cost).
- Parallel shifts, the 2026 realised volatility of the ladder cost (computed here), zero drift, 4 quarterly tranches,
  a 5% "trigger" and deposit scenarios ($0, $75k, 6 months late): ASSUMPTIONS, illustrations not forecasts.
- $300,000 and $150,000 deposits, all flows on Jan 1: VERIFIED-REPO-FILE (case p.2 L43-45, L59).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D1_purchase_rule.py
"""
import csv
from datetime import date

import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

SNAP = "research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv"
REPO = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
ANCHOR, Y2028 = date(2027, 1, 1), date(2028, 1, 1)
YEARS = list(range(2033, 2043))
DEP1, DEP2 = 300_000, 150_000


def load(path):
    rows = list(csv.DictReader(open(path)))
    for r in rows:
        m, d, y = r["Date"].split("/")
        r["_date"] = date(int(y), int(m), int(d))
    return sorted(rows, key=lambda r: r["_date"])


def curve(row, bp=0.0):
    par = {t: float(row[k]) + bp / 100 for k, t in TENOR.items() if row.get(k) not in (None, "", "N/A")}
    ts = sorted(par)
    grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts])
    df = []
    for y in p:
        c = y / 2
        df.append((1 - c * sum(df)) / (1 + c))
    g, lz = np.r_[0, grid], np.log(np.r_[1, df])
    v = row["_date"]
    return lambda d: float(np.exp(np.interp((d - v).days / 365.25, g, lz)))


def pay_date(y, nov):
    return date(y - 1, 11, 15) if nov else date(y, 1, 1)


def rung_costs(row, when, bp=0.0, nov=False):
    """Cost at `when` (forward, locked by the row's curve) of $50k delivered for each payment year."""
    f = curve(row, bp)
    return {y: 50_000 * f(pay_date(y, nov)) / f(when) for y in YEARS}


def longest_first(costs, cash):
    """Buy rungs from 2042 backwards with `cash`. Returns (fully bought years, partial year, share bought, gap $)."""
    left, bought = cash, []
    for y in sorted(costs, reverse=True):
        if left >= costs[y]:
            bought.append(y)
            left -= costs[y]
        else:
            return bought, y, left / costs[y], sum(costs.values()) - cash
    return bought, None, 1.0, sum(costs.values()) - cash


def main():
    rows = load(SNAP)
    last = rows[-1]
    repo = next(r for r in load(REPO) if r["_date"] == last["_date"])
    same = all(abs(float(last[k]) - float(repo[k])) < 1e-9 for k in TENOR)
    print(f"Curve snapshot {rows[0]['_date']}..{last['_date']} ({len(rows)} dates); 09/25 row equals repo file: {same}")

    # [1] + [2]
    print("\n[1]-[2] Cost at 2027-01-01, gap over $300k, and the longest-first split")
    print("  shift | ladder | exact-date cost | gap | fully bought | waiting part (2027 $) | 2028 $ needed | % of $150k")
    shifts = (0, -25, -50, -75, -100, -150, -200)
    for nov in (False, True):
        for bp in shifts:
            c = rung_costs(last, ANCHOR, bp, nov)
            tot = sum(c.values())
            bought, part, share, gap = longest_first(c, DEP1)
            f = curve(last, bp)
            need28 = max(gap, 0) * f(ANCHOR) / f(Y2028)
            desc = (f"{min(bought) if bought else '-'}-2042; {part}: {share * 100:.0f}% bought" if part
                    else "all ten")
            print(f"  {bp:+4d}bp | {'Nov-15 STRIPS' if nov else 'exact-date   '} | ${tot:,.0f} | ${gap:,.0f} | {desc} | "
                  f"${max(gap, 0):,.0f} | ${need28:,.0f} | {need28 / DEP2 * 100:.1f}%")

    # [3] sensitivity of the waiting part to a further fall during 2027
    print("\n[3] If rates first fall 100bp (gap exists) and then fall ANOTHER 100bp during 2027:")
    for nov in (False, True):
        c1 = rung_costs(last, ANCHOR, -100, nov)
        gap = sum(c1.values()) - DEP1
        # longest-first: waiting part is the earliest payments; nearest-first: the latest payments
        for label, order in (("longest-first (waiting = earliest payments)", sorted(YEARS)),
                             ("nearest-first (waiting = latest payments)", sorted(YEARS, reverse=True))):
            # waiting set: walk from the end of the buying order backwards until the gap is covered
            buy_order = list(reversed(order))  # longest-first buys 2042 first
            left, waiting = DEP1, {}
            for y in buy_order:
                take = min(1.0, max(left, 0) / c1[y])
                left -= take * c1[y]
                if take < 1:
                    waiting[y] = 1 - take
            f_a, f_b = curve(last, -100), curve(last, -200)
            w28_a = sum(s * 50_000 * f_a(pay_date(y, nov)) / f_a(Y2028) for y, s in waiting.items())
            w28_b = sum(s * 50_000 * f_b(pay_date(y, nov)) / f_b(Y2028) for y, s in waiting.items())
            print(f"  {'Nov15' if nov else 'exact'} {label}: waiting ${gap:,.0f} (2027 $); needed Jan 2028 "
                  f"${w28_a:,.0f}; after a further -100bp ${w28_b:,.0f} (+${w28_b - w28_a:,.0f}, "
                  f"+{(w28_b / w28_a - 1) * 100:.0f}%)")

    # [4] break-evens
    print("\n[4] Break-even parallel falls (Jan 2027 purchase)")
    for nov in (False, True):
        tot = lambda bp: sum(rung_costs(last, ANCHOR, bp, nov).values())
        b0 = brentq(lambda bp: tot(bp) - DEP1, -400, 200)
        first = lambda bp: tot(bp) - DEP1 - rung_costs(last, ANCHOR, bp, nov)[2033]
        b1 = brentq(first, -500, 200)
        def dep(bp):
            f = curve(last, bp)
            return (tot(bp) - DEP1) * f(ANCHOR) / f(Y2028) - DEP2
        b2 = brentq(dep, -600, 0)
        print(f"  {'Nov-15 STRIPS' if nov else 'exact-date'}: gap>0 below {b0:+.0f}bp; gap > whole first payment below "
              f"{b1:+.0f}bp; gap > whole 2028 deposit below {b2:+.0f}bp (10y would be {5.17 + b2 / 100:.2f}%)")

    # [5] 2026 history
    print("\n[5] Longest-first on every 2026 curve date")
    for nov in (False, True):
        hist = []
        for r in rows:
            c = rung_costs(r, ANCHOR, 0, nov)
            f = curve(r)
            gap = sum(c.values()) - DEP1
            hist.append((r["_date"], sum(c.values()), gap, max(gap, 0) * f(ANCHOR) / f(Y2028), float(r["10 Yr"])))
        w = max(hist, key=lambda h: h[1])
        tag = "Nov-15" if nov else "exact"
        print(f"  {tag}: worst day {w[0]} (10y {w[4]}%): cost ${w[1]:,.0f}, gap ${w[2]:,.0f}, 2028 $ ${w[3]:,.0f} "
              f"= {w[3] / DEP2 * 100:.1f}% of the deposit; days with a gap: {sum(h[2] > 0 for h in hist)}/{len(hist)}")
        for d0 in (date(2026, 1, 2), date(2026, 6, 30), date(2026, 9, 10), date(2026, 9, 25)):
            h = next(x for x in hist if x[0] == d0)
            c = rung_costs(next(r for r in rows if r["_date"] == d0), ANCHOR, 0, nov)
            bought, part, share, _ = longest_first(c, DEP1)
            print(f"     {d0}: cost ${h[1]:,.0f}; gap ${h[2]:,.0f}; "
                  + (f"waiting: {(1 - share) * 100:.0f}% of the {part} payment"
                     + (f" plus {min(bought) - 2033 - 1} earlier payment(s)" if bought and min(bought) - 1 > part else "")
                     if part else "all ten bought"))
        vals = np.array([h[1] for h in hist])
        vol = np.diff(np.log(vals)).std(ddof=1) * np.sqrt(252)
        print(f"     realised volatility of this ladder's cost in 2026: {vol * 100:.2f}%/yr")
        if not nov:
            vol_exact = vol
        else:
            vol_nov = vol

    # [6] distribution of the gap
    t = (ANCHOR - last["_date"]).days / 365.25
    print(f"\n[6] Model gap on 2027-01-01 (ASSUMPTION: zero-drift lognormal cost, horizon {t:.2f}y)")
    for nov, vol in ((False, vol_exact), (True, vol_nov)):
        base = sum(rung_costs(last, ANCHOR, 0, nov).values())
        s = vol * np.sqrt(t)
        p_gap = 1 - norm.cdf(np.log(DEP1 / base) / s)
        first = rung_costs(last, ANCHOR, 0, nov)[2033]
        p_first = 1 - norm.cdf(np.log((DEP1 + first) / base) / s)
        qs = {q: base * np.exp(s * norm.ppf(q)) - DEP1 for q in (0.75, 0.90, 0.95, 0.99)}
        print(f"  {'Nov-15' if nov else 'exact '}: base ${base:,.0f}, vol {vol * 100:.2f}%: P(gap>0) {p_gap * 100:.1f}%; "
              f"P(gap > whole first payment) {p_first * 100:.3f}%; gap at p75/p90/p95/p99: "
              + ", ".join(f"${max(v, 0):,.0f}" for v in qs.values()))

    # [7] at once vs staged vs trigger (funded ratio = rungs bought / rungs needed)
    print("\n[7] Buy all on 2027-01-01 vs 4 quarterly tranches in 2027 vs 'wait for a 5% funded margin, else buy on "
          "2027-12-31' (ASSUMPTION: ladder cost relative to T-bills is zero-drift lognormal, vol as above)")
    rng = np.random.default_rng(20260928)
    base = sum(rung_costs(last, ANCHOR, 0, True).values())
    F0 = DEP1 / base
    for label, sig in (("Nov-15 ladder, 2026 vol", vol_nov),):
        n, steps = 200_000, 252
        dt = 1 / steps
        # X_t = log(price relative to cash); price at t0 known (we price on today's curve for 2027-01-01)
        z = rng.standard_normal((n, steps)) * sig * np.sqrt(dt) - 0.5 * sig ** 2 * dt
        x = np.c_[np.zeros(n), np.cumsum(z, axis=1)]
        at_once = np.full(n, F0)
        idx = [0, 63, 126, 189]
        staged = F0 * np.mean(np.exp(-x[:, idx]), axis=1)
        # trigger: buy everything the first day funded ratio >= 1.05, else at the end of 2027
        fr = F0 * np.exp(-x)
        hit = fr >= 1.05
        first_hit = np.where(hit.any(axis=1), hit.argmax(axis=1), steps)
        trig = fr[np.arange(n), first_hit]
        for name, arr in (("buy at once", at_once), ("4 quarterly tranches", staged), ("5% trigger / year-end", trig)):
            print(f"  {name:22s}: mean funded ratio {arr.mean():.4f}; sd {arr.std():.4f}; P(<1.00) "
                  f"{(arr < 1).mean() * 100:.1f}%; p5 {np.percentile(arr, 5):.4f}")
        print(f"  (starting funded ratio on today's curve, Nov-15 ladder: {F0:.4f}; the at-once row assumes the "
              f"curve on the purchase day equals today's, so its spread is zero by construction; the spread of the "
              f"purchase-day cost itself is item [6])")

    # [8] joint tail
    print("\n[8] Joint tail: rates fall before Jan 2027 AND the 2028 deposit is missing, half or late")
    for bp in (-50, -100, 0):
        rows_bp = [("shift", bp)]
        c = rung_costs(last, ANCHOR, bp, True)
        f = curve(last, bp)
        gap = max(sum(c.values()) - DEP1, 0)
        need28 = gap * f(ANCHOR) / f(Y2028)
        face_unfunded = gap / c[2033] * 50_000 if gap < c[2033] else None
        late = gap * f(ANCHOR) / f(date(2028, 7, 1))
        print(f"  {bp:+d}bp: gap ${gap:,.0f} (2027 $) -> needed Jan 2028 ${need28:,.0f}. Deposit $0: "
              + (f"${face_unfunded:,.0f} of the $50,000 Jan-2033 payment unfunded ({face_unfunded / 500_000 * 100:.1f}% "
                 f"of the $500k promised)" if face_unfunded else "none") +
              f". Deposit $75k: {'covered' if need28 <= 75_000 else 'not covered'}. Deposit 6 months late "
              f"(1 Jul 2028, rates unchanged): needs ${late:,.0f} (+${late - need28:,.0f}).")


if __name__ == "__main__":
    main()
