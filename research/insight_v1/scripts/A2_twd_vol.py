"""A2_twd_vol.py - USD/TWD level and volatility from the primary FRED series DEXTAUS.

What it does (plain English): downloads the official daily exchange rate "Taiwan dollars per one U.S. dollar"
(Federal Reserve H.10 noon buying rate, FRED series DEXTAUS), then measures how much it moves.
"Volatility" here = the standard deviation of daily log changes, scaled to one year (x sqrt(252)).
It also shows how big real 2-year and 6-year moves have been, because the co-sponsor talk is in 2031 (2 years
before 2033) and the facility money is spent from 2033 (about 6 years from now).

Inputs (with status labels):
- FRED DEXTAUS daily CSV, https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXTAUS
  VERIFIED-PRIMARY when downloaded live (source: Board of Governors of the Federal Reserve System, H.10).
  Optional: pass a local CSV path as the first argument to re-run offline on a saved copy.
- Annualisation factor 252 trading days: ASSUMPTION (market convention); the script also prints the result with
  the observed number of observations per year.
- Windows are "the last N calendar years ending on the latest observation": ASSUMPTION (convention).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/A2_twd_vol.py            # live download from FRED
    .venv/bin/python research/insight_v1/scripts/A2_twd_vol.py path.csv   # offline copy (same format)

Output on 2026-09-27 (live FRED, latest observation 2026-09-18 = 31.82) is recorded in
research/insight_v1/phase_A/fact_register.md (Taiwan/FX section).
"""
import io
import sys
import urllib.request

import numpy as np
import pandas as pd

URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXTAUS"


def load(path=None):
    if path:
        raw = open(path, encoding="utf-8").read()
    else:
        with urllib.request.urlopen(URL, timeout=60) as r:
            raw = r.read().decode("utf-8")
    df = pd.read_csv(io.StringIO(raw))
    df.columns = ["date", "twd"]
    df["date"] = pd.to_datetime(df["date"])
    df["twd"] = pd.to_numeric(df["twd"], errors="coerce")   # FRED marks holidays with "." or blank
    return df.dropna().set_index("date")["twd"]


def main():
    s = load(sys.argv[1] if len(sys.argv) > 1 else None)
    last_date, last = s.index[-1], s.iloc[-1]
    print(f"Source: {'file ' + sys.argv[1] if len(sys.argv) > 1 else URL}")
    print(f"Observations: {len(s):,} from {s.index[0].date()} to {last_date.date()}")
    print(f"Latest: {last:.4f} TWD per USD on {last_date.date()}")
    print("\nAnnualised volatility of daily log changes (window = last N years to the latest observation)")
    print(f"{'window':>7} {'start':>11} {'obs':>6} {'obs/yr':>7} {'vol x sqrt(252)':>16} {'vol x sqrt(obs/yr)':>19}"
          f" {'min':>6} {'max':>6} {'change p.a.':>12}")
    for n in (1, 3, 5, 10):
        start = last_date - pd.DateOffset(years=n)
        w = s[s.index >= start]
        lr = np.diff(np.log(w.values))
        per_yr = len(lr) / n
        v252 = lr.std(ddof=1) * np.sqrt(252)
        vobs = lr.std(ddof=1) * np.sqrt(per_yr)
        cagr = (w.iloc[-1] / w.iloc[0]) ** (1 / n) - 1
        print(f"{n:>5}y  {str(w.index[0].date()):>11} {len(lr):>6} {per_yr:>7.1f} {v252*100:>15.2f}% {vobs*100:>18.2f}%"
              f" {w.min():>6.2f} {w.max():>6.2f} {cagr*100:>+11.2f}%")

    # Monthly volatility over 10 years, as a cross-check on daily noise. Month-END values are the right input;
    # monthly AVERAGES smooth the series and understate volatility (this is why a council file showed 4.4%).
    w10 = s[s.index >= last_date - pd.DateOffset(years=10)]
    for how, m in (("month-end values", w10.resample("ME").last().dropna()),
                   ("monthly averages (smoothed, understates)", w10.resample("ME").mean().dropna())):
        mv = np.diff(np.log(m.values)).std(ddof=1) * np.sqrt(12)
        print(f"10y volatility from {how}: {mv*100:.2f}% a year")
    fv = np.diff(np.log(s.values)).std(ddof=1) * np.sqrt(252)
    print(f"Full-history (since {s.index[0].year}) daily volatility: {fv*100:.2f}% a year")

    # Historical distribution of 2-year and ~6.25-year log moves (overlapping windows)
    print("\nRealised moves over a horizon (overlapping windows; + = TWD weaker, more TWD per USD)")
    for since in (None, last_date - pd.DateOffset(years=20)):
        x = s if since is None else s[s.index >= since]
        tag = f"since {x.index[0].date()}"
        for label, days in (("2 years", 730), ("6.25 years (Sep 2026 -> Jan 2033)", 2283)):
            fut = x.reindex(x.index + pd.Timedelta(days=days), method="nearest", tolerance=pd.Timedelta(days=7))
            ch = np.log(fut.values / x.values)
            ch = ch[~np.isnan(ch)]
            pct = np.percentile(ch, [5, 50, 95]) * 100
            print(f"  {tag}, {label}: n={len(ch):,}  sd={ch.std()*100:.1f}%  p5/p50/p95 = {pct[0]:+.1f}% / "
                  f"{pct[1]:+.1f}% / {pct[2]:+.1f}%  min {ch.min()*100:+.1f}%  max {ch.max()*100:+.1f}%")
    print("  (sqrt-time scaling of the 10y daily vol would give "
          f"2y {np.diff(np.log(w10.values)).std(ddof=1)*np.sqrt(252*2)*100:.1f}% and "
          f"6.25y {np.diff(np.log(w10.values)).std(ddof=1)*np.sqrt(252*6.25)*100:.1f}%)")

    # Illustration only: what USD amount buys the same NT$ as one $50,000 payment at today's rate
    ntd = 50_000 * last
    print(f"\nIllustration: $50,000 = NT${ntd:,.0f} at {last:.2f}.")
    for f in (0.90, 0.95, 1.05, 1.10):
        print(f"  if TWD per USD moves to {last*f:.2f} ({(f-1)*100:+.0f}%): the same NT$ cost ${ntd/(last*f):,.0f}")


if __name__ == "__main__":
    main()
