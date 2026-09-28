"""D7_rule_trigger_odds.py - can a pre-written WInS rule genuinely fire before the Oct 23 Trading Notes deadline?

Agent D7 (Wharton Intent Historian), insight_v1 run, 2026-09-27. Question M002 (and one truthfulness check for M011).

What it does (plain English):
1. Measures how much the 10-year Treasury yield moved per day in 2026 (realised volatility).
2. Simulates the WInS window (first fills ~Thu Oct 1 to the reflection-writing date Tue Oct 20) and asks how likely
   each candidate rule is to fire:
   a. the growth-money band in the current ticket (VT 60% of VT+VGSH, band 55-65), and a tighter 57-63 band;
   b. a whole-portfolio equity band (VT 20.5% of $300k, +/-5 points and +/-3 points);
   c. the hedge-duration band (9.65-10.15 years on issuer numbers);
   d. a pure "rate event" (10-year yield moves 10bp / 25bp from the trade date), which under lock-early triggers a
      CHECK, never a trade (the ticket's "never" rules).
3. Reports how big a rate move the hedge note's reflection could honestly describe as a live "test" (the hedge and
   the payments moving together), which needs no extra trade.
4. (M011) Cross-checks how often "the ten payments are bought with the first deposit" would be FALSE, using the
   27bp headroom and the realised rate volatility (a crude one-factor check of the A2/S4 numbers).

Inputs (with status labels):
- Treasury daily par yield curve 2026 (home.treasury.gov CSV). VERIFIED-PRIMARY when downloaded live; fallback is the
  repo file competition/official_market_data/daily-treasury-rates_2026-09.csv (VERIFIED-REPO-FILE, September only).
- Equity volatility 16.78%/yr: JPM 2026 LTCMA AC World (VERIFIED-REPO-FILE via brief section 6). Using it for VT's
  short-run volatility is an ASSUMPTION (realised short-run vol can be higher or lower).
- VGSH volatility 1.8%/yr and hedge-fund volatility from duration x rate vol: ASSUMPTION (1-3y Treasuries; duration
  1.9y per Vanguard page via the wins_now ticket).
- Stock-bond correlation 0 (JPM large cap vs intermediate Treasuries -0.01): VERIFIED-REPO-FILE number, used as an
  ASSUMPTION for the next three weeks.
- Weights: hedge 66% (IEF 23.6 / TLH 42.4), VT 20.5%, VGSH 12.5%, cash 1% (wins_now ticket option (ii)),
  VERIFIED-REPO-FILE as a plan, not a fact.
- Issuer durations: IEF 6.95 (2026-06-30) -> 6.86 (2026-09-24); TLT 15.31 -> 14.88; TLH 11.59 (2026-09-24).
  VERIFIED-REPO-FILE / VERIFIED-PRIMARY (brief sections 6 and 14, ticket section 1). TLH's quarterly drift is an
  ASSUMPTION (set between IEF's and TLT's).
- Ladder headroom under $300k: 27bp; DV01 $289/bp (brief section 6, VERIFIED-REPO-FILE via the verified script).
- Window dates and U.S. trading days: DERIVED from the NYSE calendar (no NYSE holiday between Sep 28 and Oct 23;
  Columbus Day Oct 12 closes the bond market but not stock exchanges - ASSUMPTION that WInS ETF prices update that day).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D7_rule_trigger_odds.py
Results are recorded in research/insight_v1/phase_D/D7_wharton_intent.md.
"""
import csv
import io
import urllib.request
from datetime import date, timedelta

import numpy as np
from scipy.stats import norm

REPO_CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
URL = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all"
       "?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv")
SEED = 20260927
N_PATHS = 200_000


def load_10y():
    """Return (dates, 10y yields in %) sorted by date, and a label saying where they came from."""
    try:
        with urllib.request.urlopen(URL, timeout=60) as r:
            text = r.read().decode("utf-8")
        label = "live treasury.gov 2026 CSV (VERIFIED-PRIMARY)"
    except Exception as exc:  # network blocked -> repo fallback
        with open(REPO_CSV, encoding="utf-8") as f:
            text = f.read()
        label = f"repo September CSV (VERIFIED-REPO-FILE; live download failed: {type(exc).__name__})"
    rows = list(csv.DictReader(io.StringIO(text)))
    pts = []
    for row in rows:
        m, d, y = row["Date"].split("/")
        if row.get("10 Yr"):
            pts.append((date(int(y), int(m), int(d)), float(row["10 Yr"])))
    pts.sort()
    return [p[0] for p in pts], np.array([p[1] for p in pts]), label


def trading_days(start, end):
    """Weekdays from start to end inclusive (no NYSE holiday falls in this window in 2026)."""
    out, d = [], start
    while d <= end:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def band_hit_prob(w0, lo, hi, rel_vol_daily, days, check_idx, rng):
    """Probability that weight w = w0*R/(w0*R + (1-w0)) leaves [lo, hi] on any check day.

    R = relative price of the risky asset vs the other asset, a driftless lognormal walk (ASSUMPTION)."""
    steps = rng.normal(0.0, rel_vol_daily, size=(N_PATHS, len(days)))
    logr = np.cumsum(steps, axis=1)[:, check_idx]
    r = np.exp(logr)
    w = w0 * r / (w0 * r + (1 - w0))
    hit = ((w < lo) | (w > hi)).any(axis=1)
    return hit.mean()


def main():
    rng = np.random.default_rng(SEED)
    dates, y10, label = load_10y()
    ch_bp = np.diff(y10) * 100
    sd_bp = ch_bp.std(ddof=1)
    print(f"[1] 10y par yield source: {label}; {len(y10)} days {dates[0]} to {dates[-1]}")
    print(f"    realised sd of daily 10y change: {sd_bp:.2f} bp/day (annualised {sd_bp*np.sqrt(252):.0f} bp)")
    sept = [i for i, d in enumerate(dates) if d.month == 9]
    if len(sept) > 2:
        print(f"    10y on {dates[sept[0]]}: {y10[sept[0]]:.2f}%, on {dates[sept[-1]]}: {y10[sept[-1]]:.2f}% "
              f"(move {100*(y10[sept[-1]]-y10[sept[0]]):+.0f}bp)")

    # Window: fills Thu Oct 1 (ticket target "fills by Fri Oct 2"), reflection data cut-off Tue Oct 20.
    days = trading_days(date(2026, 10, 2), date(2026, 10, 20))  # moves AFTER the Oct 1 fill
    all_days = trading_days(date(2026, 9, 28), date(2026, 10, 22))
    print(f"\n[2] Trading days Sep 28-Oct 22: {len(all_days)}; days of market moves after an Oct 1 fill up to "
          f"Oct 20: {len(days)}")
    weekly = [i for i, d in enumerate(days) if d.weekday() == 4] + [len(days) - 1]  # Fridays + Oct 20
    weekly = sorted(set(weekly))
    daily = list(range(len(days)))
    print(f"    weekly check dates: {[str(days[i]) for i in weekly]}")

    eq_vol, vgsh_vol = 0.1678, 0.018
    rel_growth = np.sqrt(eq_vol**2 + vgsh_vol**2) / np.sqrt(252)
    # hedge fund volatility ~ duration 10y x realised rate vol
    hedge_vol = 10 * sd_bp / 10000 * np.sqrt(252)
    rest_vol = np.sqrt((0.66 * hedge_vol) ** 2 + (0.125 * vgsh_vol) ** 2) / 0.795  # non-VT part, ~uncorrelated
    rel_total = np.sqrt(eq_vol**2 + rest_vol**2) / np.sqrt(252)
    print(f"\n[3] Band rules (ASSUMPTION: equity vol {eq_vol:.2%}, VGSH vol {vgsh_vol:.1%}, hedge vol "
          f"{hedge_vol:.1%} from duration 10 x realised rate vol, correlation 0)")
    for name, w0, lo, hi, rv in [
        ("VT share of growth money 60%, band 55-65 (ticket)", 0.60, 0.55, 0.65, rel_growth),
        ("VT share of growth money 60%, band 57-63", 0.60, 0.57, 0.63, rel_growth),
        ("VT share of whole book 20.5%, band +/-5 pts", 0.205, 0.155, 0.255, rel_total),
        ("VT share of whole book 20.5%, band +/-3 pts", 0.205, 0.175, 0.235, rel_total),
        ("VT share of whole book 20.5%, band +/-2 pts", 0.205, 0.185, 0.225, rel_total),
    ]:
        pw = band_hit_prob(w0, lo, hi, rv, days, weekly, rng)
        pd = band_hit_prob(w0, lo, hi, rv, days, daily, rng)
        up = hi * (1 - w0) / (w0 * (1 - hi)) - 1
        dn = lo * (1 - w0) / (w0 * (1 - lo)) - 1
        print(f"    {name}: needs relative move {dn:+.1%} / {up:+.1%}; P(fires by Oct 20) weekly checks "
              f"{pw:.2%}, daily checks {pd:.2%}")

    # Hedge duration band: drift from issuer duration changes + rate-driven weight drift
    q_weeks = (date(2026, 9, 24) - date(2026, 6, 30)).days / 7
    ief_drift = (6.86 - 6.95) / q_weeks * 3
    tlt_drift = (14.88 - 15.31) / q_weeks * 3
    tlh_drift = 0.5 * (ief_drift + tlt_drift)  # ASSUMPTION
    w_ief, w_tlh, d_ief, d_tlh = 0.357, 0.643, 6.86, 11.59
    comp = w_ief * ief_drift + w_tlh * tlh_drift
    worst = 0.0
    for shift_bp in (-50, 50):
        g_ief = 1 - d_ief * shift_bp / 10000
        g_tlh = 1 - d_tlh * shift_bp / 10000
        w2 = w_tlh * g_tlh / (w_ief * g_ief + w_tlh * g_tlh)
        dmix = (w2 - w_tlh) * (d_tlh - d_ief)
        worst = max(worst, abs(dmix))
        print(f"\n[4] Hedge duration: rates {shift_bp:+d}bp moves the mix by {dmix:+.3f}y through weight drift"
              if shift_bp == -50 else f"    rates {shift_bp:+d}bp: {dmix:+.3f}y")
    print(f"    issuer-duration drift over 3 weeks (from Jun30->Sep24 pace): IEF {ief_drift:+.3f}y, "
          f"TLT {tlt_drift:+.3f}y, TLH (assumed) {tlh_drift:+.3f}y -> mix {comp:+.3f}y")
    print(f"    worst combined drift ~{abs(comp)+worst:.2f}y vs band half-width 0.25y -> the duration refresh "
          f"almost surely finds NO trade needed")

    # Rate events (check triggers, not trades)
    steps = rng.normal(0, sd_bp, size=(N_PATHS, len(days)))
    path = np.cumsum(steps, axis=1)
    end = path[:, -1]
    mx = np.abs(path).max(axis=1)
    print(f"\n[5] 10y rate moves between Oct 1 fill and Oct 20 (driftless normal, sd {sd_bp:.2f}bp/day):")
    for thr in (5, 10, 15, 25):
        print(f"    |move| >= {thr}bp at Oct 20: {np.mean(np.abs(end) >= thr):.0%}; touched at any close: "
              f"{np.mean(mx >= thr):.0%}")
    print(f"    median |move| at Oct 20: {np.median(np.abs(end)):.1f}bp; 10bp moves the payments' value by about "
          f"{10*289/292264:.1%} (~${10*289:,.0f} on the 2027 value; DV01 $289/bp)")

    # M011 truthfulness cross-check
    n_to_jan = len(trading_days(date(2026, 9, 28), date(2026, 12, 31)))
    sd_to_jan = sd_bp * np.sqrt(n_to_jan)
    p_fall = norm.cdf(-27 / sd_to_jan)
    print(f"\n[6] M011 check: trading days to 2026-12-31: {n_to_jan}; sd of 10y change ~{sd_to_jan:.0f}bp; "
          f"P(rates fall >27bp, so ladder > $300k) ~{p_fall:.0%} (one-factor, driftless; compare A2 24.3%, S4 30.7%)")
    print("    -> 'bought with her first deposit' is false in roughly 1 in 4 to 1 in 3 modelled paths;")
    print("       'no dollar takes market risk until all ten payments are bought' is true in every path (it is a rule).")


if __name__ == "__main__":
    main()
