"""D9_numbers.py - every number the D9 Communication Analyst file quotes, recomputed in one place.

Sections (run all; nothing is random except where stated):
  [1] M062  How the official documents use certainty / confidence / reliability words (counts + the object each
            word is attached to). Inputs: the six official files in competition/official/2026_27/ (VERIFIED-REPO-FILE).
  [2] M226  Chance that U.S. large-cap stocks (JPM 2026 LTCMA: 6.70% compound, 7.94% arithmetic, 16.47% vol;
            VERIFIED-REPO-FILE via brief section 6 / F-3xx) grow LESS than the Treasury rate that can be locked for the
            same horizon (forward zero rates 2027->2033/2037/2042 = 5.08%/5.24%/5.48%, brief section 6, derived from the
            VERIFIED-PRIMARY 2026-09-25 curve). Model: lognormal i.i.d. annual returns (ASSUMPTION), closed form.
            Also AC World (7.00% compound, 16.78% vol; VERIFIED-REPO-FILE) as a check.
  [3] M012  How much the price of Laura's ten payments moves: DV01 $289 per bp (VERIFIED-REPO-FILE script output,
            brief s6); realised 2026 10-year daily change sd 4.45bp/day (D7, from the VERIFIED-PRIMARY treasury.gov CSV);
            sqrt(252) annualisation and a normal approximation are ASSUMPTIONS. Also re-prices the ladder on the LATEST
            curve date available from treasury.gov (live download; falls back to the repo CSV), with the verified
            method (research/verified_2026-09-27/official_curve_pv.py), so a trade note can quote a dated number.
  [4] M121  Trade-off costs, restated from the verified strategy_mc.py run (brief section 6; F-401/F-402; ASSUMPTION-
            based model outputs) and from the curve script's rate shifts (brief section 6).
  [5] M143  How often the ten payments stop depending on the 2028 deposit in January 2027: P(ladder > $300k on
            2027-01-01) from three Phase A/wins_now/D7 runs (all ASSUMPTION-based: zero drift, 2026 realised vol).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D9_numbers.py
"""
import csv
import io
import math
import re
import subprocess
from datetime import date

import numpy as np
from scipy.stats import norm

OFF = "competition/official/2026_27/"
DOCS = {
    "case": OFF + "Laura_Gao_2026_Client_Profile.txt",
    "IPS guide": OFF + "2026_WGY_Investment_Policy-FINAL.txt",
    "TN guide": OFF + "2026_WGY_Trading_Notes_Analysis-FINAL.txt",
    "Comp. Guide": OFF + "2026_WGY_Investment_Competition_Guide.txt",
    "Infographic": OFF + "2026_WGY_Competition_Infographic.txt",
    "SMApply page": OFF + "SMApply_Deliverables_Page_2026-09-27.md",
}


def s1_vocabulary():
    print("[1] M062 certainty vocabulary in the official documents (VERIFIED-REPO-FILE)")
    pats = {
        "certain*": r"\bcertain\w*",
        "confiden*": r"\bconfiden\w*",
        "reliab*/reliable": r"\breliab\w*|\breliabl\w*",
        "guarantee*": r"\bguarantee\w*",
        "safe*": r"\bsafe\w*",
        "protect*": r"\bprotect\w*",
        "credib*": r"\bcredib\w*",
    }
    for name, path in DOCS.items():
        lines = open(path, encoding="utf-8").read().splitlines()
        counts = {k: 0 for k in pats}
        ctx = []
        for i, ln in enumerate(lines, 1):
            for k, p in pats.items():
                for m in re.finditer(p, ln, flags=re.I):
                    counts[k] += 1
                    ctx.append(f"      {name} L{i}: ...{ln.strip()[:150]}")
        print(f"  {name:13s} " + ", ".join(f"{k}={v}" for k, v in counts.items()))
        for c in ctx:
            print(c)
    print()


def lognormal_params(geo, arith):
    m = math.log(1 + geo)
    s2 = 2 * (math.log(1 + arith) - m)
    return m, math.sqrt(s2)


def s2_horizon():
    print("[2] M226 P(stocks compound below the Treasury rate locked for the same horizon), lognormal ASSUMPTION")
    # AC World: only the compound return and vol are in the brief; the log-sd is backed out from the vol with the
    # arithmetic mean approximated as geo + s^2/2 (ASSUMPTION).
    s_ac = math.sqrt(math.log(1 + 0.1678 ** 2 / (1.07 + 0.1678 ** 2 / 2) ** 2))
    cases = {
        "US large cap (JPM 6.70% geo / 7.94% arith)": lognormal_params(0.0670, 0.0794),
        "AC World (JPM 7.00% geo, 16.78% vol)": (math.log(1.07), s_ac),
    }
    targets = [("2027->2033 (6 yrs, first payment)", 6, 0.0508),
               ("2027->2037 (10 yrs, middle payment)", 10, 0.0524),
               ("2027->2042 (15 yrs, last payment)", 15, 0.0548)]
    for cname, (m, s) in cases.items():
        print(f"  {cname}: log-mean {m:.4f}, log-sd {s:.4f}")
        for tname, T, r in targets:
            z = (math.log(1 + r) - m) * math.sqrt(T) / s
            print(f"    {tname}: locked {r:.2%}/yr -> P(stocks end below the locked amount) = {norm.cdf(z):.1%}")
    # Check by simulation (seeded) for the 10-year case.
    rng = np.random.default_rng(20260927)
    m, s = cases["US large cap (JPM 6.70% geo / 7.94% arith)"]
    sims = rng.normal(m, s, size=(200_000, 10)).sum(axis=1)
    print(f"  simulation check (US large cap, 10 yrs, 200k paths, seed 20260927): "
          f"{np.mean(sims < 10 * math.log(1.0524)):.1%}")
    print("  Equity premium over the locked rate (compound, US large cap): "
          f"{0.0670 - 0.0508:.2%} (6y), {0.0670 - 0.0524:.2%} (10y), {0.0670 - 0.0548:.2%} (15y)")
    print()


def fetch_curve_rows():
    url = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/"
           "all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv")
    try:
        r = subprocess.run(["curl", "-sSL", "-m", "40", url], capture_output=True, text=True)
        rows = list(csv.DictReader(io.StringIO(r.stdout)))
        if rows and "Date" in rows[0]:
            return rows, "LIVE treasury.gov CSV (VERIFIED-PRIMARY)"
    except Exception:
        pass
    rows = list(csv.DictReader(open("competition/official_market_data/daily-treasury-rates_2026-09.csv")))
    return rows, "repo CSV competition/official_market_data/daily-treasury-rates_2026-09.csv (VERIFIED-REPO-FILE)"


TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}


def ladder_cost(row):
    """Same method as research/verified_2026-09-27/official_curve_pv.py (value date = curve date)."""
    par = {t: float(row[k]) for k, t in TENOR.items() if row.get(k) not in (None, "")}
    mm, dd, yy = map(int, row["Date"].split("/"))
    val, anchor = date(yy, mm, dd), date(2027, 1, 1)
    yf = lambda d: (d - val).days / 365.25
    ts = sorted(par)
    grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts])
    df = []
    for y in p:
        c = y / 2
        df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]
    lz = np.log(np.r_[1, df])
    f = lambda t: np.exp(np.interp(t, g, lz))
    ta = yf(anchor)
    return sum(50000 * f(yf(date(y, 1, 1))) / f(ta) for y in range(2033, 2043))


def s3_sensitivity():
    print("[3] M012 how the price of the ten payments moves")
    dv01 = 289.0
    for bp in (10, 25, 27, 50, 100):
        print(f"  a {bp:3d}bp move in rates changes the 2027 price of the payments by about ${dv01 * bp:,.0f}")
    daily = 4.45
    ann = daily * math.sqrt(252)
    print(f"  2026 realised 10y daily sd {daily}bp -> about {ann:.0f}bp a year (sqrt-time ASSUMPTION) -> "
          f"about ${dv01 * ann:,.0f} one-standard-deviation yearly change in the price of the promise")
    print(f"  over 3 weeks (15 trading days): about {daily * math.sqrt(15):.0f}bp -> ${dv01 * daily * math.sqrt(15):,.0f}")
    rows, src = fetch_curve_rows()
    rows = [r for r in rows if r.get("Date")]
    rows.sort(key=lambda r: (int(r["Date"][6:]), int(r["Date"][:2]), int(r["Date"][3:5])))
    last = rows[-1]
    ref = next((r for r in rows if r["Date"] == "09/25/2026"), None)
    print(f"  source: {src}; latest curve date {last['Date']} (10y {last['10 Yr']}%)")
    if ref:
        print(f"  check vs verified script on 09/25/2026: ${ladder_cost(ref):,.0f} (verified $292,264)")
    c = ladder_cost(last)
    print(f"  ladder cost for 2027-01-01 on {last['Date']}: ${c:,.0f}; headroom under $300,000: ${300000 - c:,.0f} "
          f"(~{(300000 - c) / dv01:.0f}bp)")
    print("  NOTE: re-run on the trade date and quote that day's figure, dated, in the note.")
    print()


def s4_tradeoffs():
    print("[4] M121 trade-off costs (verified model outputs, brief section 6; ASSUMPTION-based model)")
    L = {"p5": 159, "p50": 207, "p95": 273}
    G = {"p5": 20, "p50": 226, "p95": 540}
    print(f"  T1 certainty vs size: lock-early 2033 surplus p5/p50/p95 ${L['p5']}k/${L['p50']}k/${L['p95']}k, never misses "
          f"(by construction); growth-first ${G['p5']}k/${G['p50']}k/${G['p95']}k, misses a payment in 3.2% of paths "
          f"(13.7% if the 2028 deposit is $75k; 40.8% if $0).")
    print(f"     median given up: ${G['p50'] - L['p50']}k; good-market (p95) upside given up: ${G['p95'] - L['p95']}k; "
          f"bad-market (p5) gain: +${L['p5'] - G['p5']}k")
    print("     (D13c's re-run of B10b gives about $11k at the median on a different design; use ONE source consistently.)")
    print("  T2 floor vs growth (D5 script, ASSUMPTION model): each 10 points of 2031 lock share moves ~$20k into the "
          "bought floor and takes ~$10k each from kept flexibility and from the upside.")
    base = 292264
    for bp, v in ((-100, 322864), (-50, 307135), (-25, 299596), (50, 278198), (100, 264890)):
        print(f"  T3 lock now vs wait: if rates move {bp:+d}bp before purchase the payments cost ${v:,} "
              f"({v - base:+,} vs today)")
    print("     Waiting is a rate bet in both directions; the verified curve script gives no expected gain from waiting "
          "(zero-drift ASSUMPTION).")
    print()


def s5_independence():
    print("[5] M143 when the promise stops depending on Laura's future earnings")
    for name, p in (("A2 (brief s14)", 0.243), ("D7 script", 0.23), ("S4 red team", 0.307)):
        print(f"  {name}: P(ladder costs > $300k on 2027-01-01) = {p:.1%} -> promise independent of 2028 income "
              f"in January 2027 in about {1 - p:.0%} of modelled paths; otherwise from January 2028")
    print(f"  2028 deposit share of all money Laura puts in: {150 / 450:.0%} ($150k of $450k, case lines 43-45)")
    print()


if __name__ == "__main__":
    s1_vocabulary()
    s2_horizon()
    s3_sensitivity()
    s4_tradeoffs()
    s5_independence()
