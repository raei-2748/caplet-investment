"""A2_curve_recheck.py - independent re-check of every Treasury-curve number the team may quote.

What it does (plain English): rebuilds the verified ladder valuation (research/verified_2026-09-27/official_curve_pv.py,
same method, re-implemented here so it can run on any date), then answers the follow-up questions the fact register
needs: what the ten payments are worth at 1/1/2031 and 1/1/2033 on today's forward curve, what the same payments
would have cost on every trading day of 2026, how volatile that cost has been, what IEF/TLT mix matches the
liability using the June fact sheets vs today's iShares pages, and several small arithmetic checks from council files.

Inputs (with status labels):
- Treasury Daily Par Yield Curve, 2026 (home.treasury.gov CSV). VERIFIED-PRIMARY when downloaded live; the
  September rows are identical to the repo file competition/official_market_data/daily-treasury-rates_2026-09.csv
  (VERIFIED-REPO-FILE), which is the fallback if the download fails (then the 2026 history covers September only).
- IEF/TLT effective duration 6.95y/15.31y: VERIFIED-REPO-FILE (fact sheets as of 2026-06-30, page 1).
- IEF/TLT effective duration 6.86y/14.88y: VERIFIED-PRIMARY (ishares.com product pages, "as of Sep 24, 2026",
  accessed 2026-09-27).
- Curve method (par = semiannual bond-equivalent yield, linear interpolation on a 0.5y grid, bootstrap with DF(0)=1,
  log-linear discount-factor interpolation, value date = curve date): ASSUMPTION, identical to the verified script.
- Flat 5.26% annual rate, coupon 5.26%, "reinvest 200bp lower", 2%/2.5% inflation: ASSUMPTIONS copied from council
  files so their arithmetic can be checked; labelled where printed.
- Probability that the ladder cost exceeds $300k by 2027-01-01: ASSUMPTION-based (normal, zero-drift log changes
  with the 2026 realised volatility of the cost itself). A model number, not a forecast.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/A2_curve_recheck.py
Results on 2026-09-27 are recorded in research/insight_v1/phase_A/fact_register.md.
"""
import csv
import io
import urllib.request
from datetime import date

import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

REPO_CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
URL = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all"
       "?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv")
TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
PAY_YEARS = range(2033, 2043)
ANCHOR = date(2027, 1, 1)


def load_rows():
    try:
        with urllib.request.urlopen(URL, timeout=60) as r:
            text = r.read().decode("utf-8")
        src = "home.treasury.gov (live, full year 2026)"
    except Exception as e:  # offline fallback
        text = open(REPO_CSV).read()
        src = f"repo file (September only; download failed: {e})"
    rows = list(csv.DictReader(io.StringIO(text)))
    for r in rows:
        m, d, y = r["Date"].split("/")
        r["_date"] = date(int(y), int(m), int(d))
    rows.sort(key=lambda r: r["_date"])
    return rows, src


def curve(row):
    """Discount-factor function on the row's own date (identical method to the verified script)."""
    par = {t: float(row[k]) for k, t in TENOR.items() if row.get(k) not in (None, "", "N/A")}
    ts = sorted(par)
    grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts])
    df = []
    for y in p:
        c = y / 2
        df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]
    lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz)), par


def shifted(row, bp):
    r = dict(row)
    for k in TENOR:
        if r.get(k) not in (None, "", "N/A"):
            r[k] = str(float(r[k]) + bp / 100)
    return r


def value_at(row, when, years=PAY_YEARS, shift_bp=0.0):
    """Forward value at date `when` (locked in by the row's curve) of $50k paid on Jan 1 of each year."""
    f, _ = curve(shifted(row, shift_bp) if shift_bp else row)
    v = row["_date"]
    yf = lambda d: (d - v).days / 365.25
    return sum(50_000 * f(yf(date(y, 1, 1))) / f(yf(when)) for y in years if date(y, 1, 1) >= when)


def spot_pv(row, years=PAY_YEARS, shift_bp=0.0):
    f, _ = curve(shifted(row, shift_bp) if shift_bp else row)
    v = row["_date"]
    return sum(50_000 * f((date(y, 1, 1) - v).days / 365.25) for y in years)


def annuity_due(rate, n=10, amt=50_000):
    return sum(amt / (1 + rate) ** t for t in range(n))


def main():
    rows, src = load_rows()
    last = rows[-1]
    print(f"Curve source: {src}; {len(rows)} dates from {rows[0]['_date']} to {last['_date']}")
    base = value_at(last, ANCHOR)
    print(f"\n[1] Ten payments valued at 2027-01-01 on the {last['_date']} curve: ${base:,.0f}")
    for bp in (-100, -50, -25, 25, 50, 100):
        print(f"    parallel {bp:+d}bp: ${value_at(last, ANCHOR, shift_bp=bp):,.0f}")
    dv01 = (value_at(last, ANCHOR, shift_bp=-1) - value_at(last, ANCHOR, shift_bp=1)) / 2
    dur_fwd = dv01 / base * 1e4
    print(f"    DV01 ${dv01:,.1f}/bp; duration of the 2027-01-01 value {dur_fwd:.2f}y; "
          f"headroom ${300_000 - base:,.0f} = {(300_000 - base) / dv01:.1f}bp")
    sp = spot_pv(last)
    sdv = (spot_pv(last, shift_bp=-1) - spot_pv(last, shift_bp=1)) / 2
    print(f"    Spot PV today ({last['_date']}): ${sp:,.0f}; spot duration {sdv / sp * 1e4:.2f}y "
          f"(includes the ~0.27y to Jan 2027)")

    print("\n[2] Forward values locked in by today's curve (the 'which number is the reserve' question)")
    for d in (date(2028, 1, 1), date(2031, 1, 1), date(2033, 1, 1)):
        print(f"    value of all remaining payments at {d}: ${value_at(last, d):,.0f}")
    early = value_at(last, ANCHOR, years=range(2033, 2037))
    late = value_at(last, ANCHOR, years=range(2037, 2043))
    late_dn = value_at(last, ANCHOR, years=range(2037, 2043), shift_bp=-100)
    late_dn2 = value_at(last, ANCHOR, years=range(2037, 2043), shift_bp=-200)
    print(f"    2033-36 rungs ${early:,.0f}; 2037-42 rungs ${late:,.0f} (at -100bp ${late_dn:,.0f}, "
          f"+${late_dn - late:,.0f}; at -200bp ${late_dn2:,.0f}, +${late_dn2 - late:,.0f})")
    print("    Per-rung cost at 2027-01-01: " + ", ".join(
        f"{y}: ${value_at(last, ANCHOR, years=[y]):,.0f}" for y in PAY_YEARS))

    print("\n[3] Flat-rate and annuity checks (ASSUMPTION rates, for checking council arithmetic)")
    flat = brentq(lambda r: sum(50_000 / (1 + r) ** (y - 2027) for y in PAY_YEARS) - base, 0.001, 0.2)
    print(f"    flat annual rate that reproduces ${base:,.0f}: {flat * 100:.3f}%")
    print(f"    flat 5.26% value at 2027-01-01: ${sum(50_000 / 1.0526 ** (y - 2027) for y in PAY_YEARS):,.0f}")
    for r in (0.07, 0.0526, 0.05, 0.045, 0.04, 0.03):
        print(f"    reserve needed 2033-01-01 if bought then at flat {r * 100:.2f}% (annuity-due): "
              f"${annuity_due(r):,.0f}")
    print(f"    $50k due in 6 years at 5.26%: ${50_000 / 1.0526 ** 6:,.0f}")
    r626 = brentq(lambda r: 300 * (1 + r) ** 6 + 150 * (1 + r) ** 5 - 626, 0.0, 0.3)
    print(f"    team's '$626k' in 2033 implies a flat return of {r626 * 100:.2f}% a year")
    y2 = float(last["2 Yr"]) / 100
    print(f"    2-year factor: annual (1+{y2:.4f})^2 = {(1 + y2) ** 2:.4f}; "
          f"semiannual BEY (1+{y2 / 2:.5f})^4 = {(1 + y2 / 2) ** 4:.4f}")
    print(f"    2031 floor example S=$189k, a=0.8: annual ${0.8 * 189_000 * (1 + y2) ** 2:,.0f}; "
          f"semiannual ${0.8 * 189_000 * (1 + y2 / 2) ** 4:,.0f}")

    print("\n[4] Coupon-ladder arithmetic (ASSUMPTION: flat 5.26% annual coupons, bonds bought 2027-01-01)")
    c = 0.0526
    face_full = sum(50_000 / (1 + c) ** (y - 2027) for y in PAY_YEARS) / (1 / (1 + c) ** 5)
    # fully matched from 2033: face F with F*(1 - c*a5) = PV(payments) -> F = PV / v^5
    for label, face in (("budget ladder, face = cost $295,054", 295_054), ("fully matched from 2033", face_full)):
        cpn = c * face
        fv_hi = sum(cpn * (1 + c) ** (2033 - y) for y in range(2028, 2033))
        fv_lo = sum(cpn * (1 + c - 0.02) ** (2033 - y) for y in range(2028, 2033))
        print(f"    {label}: face ${face:,.0f}; coupons 2028-32 ${cpn:,.0f}/yr; value at 2033 if reinvested at "
              f"5.26% ${fv_hi:,.0f} vs 3.26% ${fv_lo:,.0f}: shortfall ${fv_hi - fv_lo:,.0f}")

    print("\n[5] Duration-matching weights (duration match only, NOT a cash-flow match)")
    for tag, ief, tlt in (("fact sheets 2026-06-30", 6.95, 15.31), ("ishares.com as of 2026-09-24", 6.86, 14.88)):
        for dname, dval in (("2027-01-01 value", dur_fwd), ("spot PV", sdv / sp * 1e4)):
            w = (tlt - dval) / (tlt - ief)
            print(f"    {tag}, target {dname} {dval:.2f}y: {w * 100:.1f}% IEF / {(1 - w) * 100:.1f}% TLT")
    w_blog = (15.31 - dur_fwd) / (15.31 - 7.5)
    print(f"    (superseded blog IEF 7.5y with TLT 15.31y: {w_blog * 100:.1f}% / {(1 - w_blog) * 100:.1f}%)")

    print("\n[6] The same ladder priced on every 2026 curve date (value at 2027-01-01)")
    hist = [(r["_date"], value_at(r, ANCHOR), float(r["10 Yr"])) for r in rows]
    vals = np.array([h[1] for h in hist])
    i_min, i_max = vals.argmin(), vals.argmax()
    print(f"    min ${vals[i_min]:,.0f} on {hist[i_min][0]} (10y {hist[i_min][2]}%); "
          f"max ${vals[i_max]:,.0f} on {hist[i_max][0]} (10y {hist[i_max][2]}%)")
    for d0 in (date(2026, 1, 2), date(2026, 6, 30), date(2026, 9, 1)):
        h = min(hist, key=lambda x: abs((x[0] - d0).days))
        print(f"    on {h[0]}: ${h[1]:,.0f} (10y {h[2]}%)")
    days_above = sum(v > 300_000 for v in vals)
    print(f"    trading days in 2026 on which the ladder cost more than $300k: {days_above} of {len(vals)}")
    lr = np.diff(np.log(vals))
    vol = lr.std(ddof=1) * np.sqrt(252)
    t = (ANCHOR - last["_date"]).days / 365.25
    p = 1 - norm.cdf(np.log(300_000 / base) / (vol * np.sqrt(t)))
    ten = np.array([h[2] for h in hist])
    bpvol = np.diff(ten).std(ddof=1) * 100 * np.sqrt(252)
    print(f"    realised volatility of the ladder cost in 2026: {vol * 100:.2f}% a year "
          f"(10y yield: {bpvol:.0f}bp a year)")
    print(f"    ASSUMPTION-based P(cost > $300k on {ANCHOR}) with zero drift over {t:.2f}y: {p * 100:.0f}% "
          f"(1-sd move by then: {vol * np.sqrt(t) * 100:.1f}% of cost = ${base * vol * np.sqrt(t):,.0f})")

    print("\n[7] Real value of one fixed $50k payment (ASSUMPTION inflation rates)")
    for infl in (0.02, 0.025, 0.037):
        print(f"    at {infl * 100:.1f}% a year, in 2026 dollars: 2033 ${50_000 / (1 + infl) ** 7:,.0f}; "
              f"2042 ${50_000 / (1 + infl) ** 16:,.0f}")


if __name__ == "__main__":
    main()
