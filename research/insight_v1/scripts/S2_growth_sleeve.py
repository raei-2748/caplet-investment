"""S2 growth-sleeve analysis (insight_v1, wins_now). AI-generated research code for Team Caplet.

What it does
  1. Concentration of the S&P 500 today (SPYM full holdings, 2026-09-24): top-1, top-10, and an "AI-linked
     mega-cap" basket (definition below is an ASSUMPTION, chosen to be transparent, not exhaustive).
  2. Current S&P 500 sector weights, built by mapping every SPYM holding to the Select Sector SPDR fund that holds it.
  3. Sector-fund fallback: an 11-fund Select Sector SPDR mix weighted like the S&P 500. Computes its look-through
     stock weights and its active share (how different it is from the index) caused by the sector funds' capping.
  4. Human-capital tilt: how much of the S&P 500 is book publishing (News Corp, owner of HarperCollins) versus the
     Communication Services sector as a whole.
  5. U.S.-only vs global using the J.P. Morgan 2026 LTCMA (repo PDF): expected compound return, volatility,
     and the dollar effect on Laura's growth sleeve.

Inputs (status labels)
  - research/insight_v1/scripts/data/S2/*_holdings.csv: State Street daily holdings files (SPYM and the 11 Select
    Sector SPDRs), holdings as of 2026-09-24, downloaded 2026-09-27 from ssga.com. VERIFIED-PRIMARY.
  - competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf (data as of 2025-09-30). VERIFIED-REPO-FILE.
    Numbers are typed below (compound, arithmetic, volatility, correlations) and were read from page 2 of that file.
  - Sleeve size (~$158k from 2028) and 60% equity: ASSUMPTION taken from the brief section 7 / strategy_mc.py.
  - Mix weights for "global" portfolios (62/28/10 U.S./EAFE/EM) are ASSUMPTION approximating VT's country mix
    (VT fact sheet 2026-06-30: United States 61.9%).

How to run (from the repo root)
  .venv/bin/python research/insight_v1/scripts/S2_growth_sleeve.py
"""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "S2")

SECTOR_FUNDS = {
    "XLK": "Information Technology", "XLF": "Financials", "XLV": "Health Care",
    "XLY": "Consumer Discretionary", "XLC": "Communication Services", "XLI": "Industrials",
    "XLP": "Consumer Staples", "XLE": "Energy", "XLU": "Utilities", "XLB": "Materials", "XLRE": "Real Estate",
}
# ASSUMPTION: "AI-linked mega-caps" = the Magnificent 7 plus the largest U.S. AI-hardware names.
AI_BASKET_US = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "META", "AVGO", "TSLA", "MU", "AMD", "ORCL"]


def load(fund):
    rows = {}
    with open(os.path.join(DATA, f"{fund.lower()}_holdings.csv")) as f:
        r = csv.reader(f)
        next(r)
        next(r)
        for name, ticker, w in r:
            if ticker in ("-", "") or "FUT" in name.upper():
                continue
            rows[ticker] = rows.get(ticker, 0.0) + float(w)
    return rows


def main():
    spx = load("SPYM")
    tot = sum(spx.values())
    spx = {k: v * 100.0 / tot for k, v in spx.items()}  # renormalise to 100% of stocks
    ranked = sorted(spx.items(), key=lambda x: -x[1])
    print("== 1. S&P 500 concentration (SPYM holdings 2026-09-24)")
    print(f"   holdings: {len(spx)}; top-1 {ranked[0][0]} {ranked[0][1]:.2f}%; "
          f"top-10 {sum(v for _, v in ranked[:10]):.2f}%")
    for t, v in ranked[:12]:
        print(f"     {t:6s} {v:5.2f}%")
    ai = sum(spx.get(t, 0) for t in AI_BASKET_US)
    print(f"   AI-linked mega-cap basket ({len(AI_BASKET_US)} tickers): {ai:.2f}% of the S&P 500")
    print(f"   equal weight would give each stock {100/len(spx):.2f}% (RSP idea)")

    # 2. sector map
    sec_hold = {f: load(f) for f in SECTOR_FUNDS}
    tick2sec = {}
    for f, h in sec_hold.items():
        for t in h:
            tick2sec[t] = f
    sec_w = {f: 0.0 for f in SECTOR_FUNDS}
    unmapped = 0.0
    for t, w in spx.items():
        if t in tick2sec:
            sec_w[tick2sec[t]] += w
        else:
            unmapped += w
    print("\n== 2. S&P 500 sector weights today (mapped via Select Sector SPDR holdings)")
    for f, w in sorted(sec_w.items(), key=lambda x: -x[1]):
        print(f"   {f:5s} {SECTOR_FUNDS[f]:24s} {w:5.2f}%")
    print(f"   unmapped: {unmapped:.2f}%")

    # 3. sector-fund fallback look-through
    mapped = sum(sec_w.values())
    target = {f: w / mapped for f, w in sec_w.items()}  # weights of the 11-fund mix (sum 1)
    look = {}
    for f, wf in target.items():
        h = sec_hold[f]
        ht = sum(h.values())
        for t, w in h.items():
            look[t] = look.get(t, 0.0) + wf * w / ht * 100.0
    active = 0.5 * sum(abs(look.get(t, 0) - spx.get(t, 0)) for t in set(look) | set(spx))
    print("\n== 3. 11-fund sector mix weighted like the S&P 500: look-through vs the index")
    for t in ["NVDA", "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "META", "AVGO", "TSLA", "MU", "AMD", "LLY", "BRK.B",
              "JPM", "XOM"]:
        print(f"   {t:6s} index {spx.get(t, 0):5.2f}%  sector-mix {look.get(t, 0):5.2f}%")
    ai_look = sum(look.get(t, 0) for t in AI_BASKET_US)
    top10_look = sum(sorted(look.values(), reverse=True)[:10])
    print(f"   AI basket: index {ai:.2f}% vs sector-mix {ai_look:.2f}%; top-10 sector-mix {top10_look:.2f}%")
    print(f"   active share vs S&P 500: {active:.1f}%")
    rounded = {f: round(w * 100) for f, w in target.items()}
    print(f"   whole-percent weights: {rounded} (sum {sum(rounded.values())})")
    er_mix = 0.08
    print(f"   blended expense ratio: {er_mix:.2f}% (all 11 funds 0.08% gross, fact sheets 2026-06-30)")
    print(f"   WInS commissions: 11 buys x $25 = $275 vs 1-2 buys = $25-50 (SMApply FAQ)")

    # 4. human-capital tilt
    news = spx.get("NWSA", 0) + spx.get("NWS", 0)
    xlc = sec_w["XLC"]
    goog_meta = spx.get("GOOGL", 0) + spx.get("GOOG", 0) + spx.get("META", 0)
    print("\n== 4. Human-capital tilt")
    print(f"   News Corp (NWSA+NWS, owner of HarperCollins): {news:.3f}% of the S&P 500")
    print(f"   Communication Services sector: {xlc:.2f}%, of which Alphabet+Meta {goog_meta:.2f}% "
          f"({goog_meta / xlc * 100:.0f}% of the sector)")
    sleeve = 158_000
    eq = 0.60 * sleeve
    print(f"   On a ${eq:,.0f} equity sleeve: News Corp = ${eq * news / 100:,.0f}; "
          f"halving Communication Services moves ${eq * xlc / 200:,.0f}, "
          f"~{goog_meta / xlc * 100:.0f}% of it out of Alphabet/Meta, not publishing")

    # 5. JPM LTCMA 2026 (USD), page 2 of the repo PDF
    jpm = {  # compound, arithmetic, vol
        "US_LC": (6.70, 7.94, 16.47), "EAFE": (7.50, 8.90, 17.63), "EM": (7.80, 9.74, 20.93),
        "ACWI": (7.00, 8.28, 16.78), "CASH": (3.10, 3.10, 0.67),
    }
    corr = {("US_LC", "EAFE"): 0.87, ("US_LC", "EM"): 0.73, ("EAFE", "EM"): 0.86}

    def c(a, b):
        return 1.0 if a == b else corr.get((a, b), corr.get((b, a)))

    def mix(ws):
        ar = sum(w * jpm[k][1] for k, w in ws.items())
        var = sum(ws[a] * ws[b] * jpm[a][2] * jpm[b][2] * c(a, b) for a in ws for b in ws)
        vol = math.sqrt(var)
        geo = ar - var / 200.0  # approx compound = arithmetic - variance/2 (in %)
        return ar, vol, geo

    print("\n== 5. U.S.-only vs global (JPM 2026 LTCMA, USD, data 2025-09-30)")
    for k in ["US_LC", "ACWI", "EAFE", "EM"]:
        cg, ar, v = jpm[k]
        print(f"   {k:6s} compound {cg:.2f}%  arithmetic {ar:.2f}%  vol {v:.2f}%  "
              f"(arith - cash)/vol {(ar - 3.10) / v:.3f}")
    for name, ws in [("100% U.S. large cap", {"US_LC": 1.0}),
                     ("62/28/10 U.S./EAFE/EM (VT-like)", {"US_LC": .62, "EAFE": .28, "EM": .10}),
                     ("70/30 U.S./EAFE (VTI+VEA-like)", {"US_LC": .70, "EAFE": .30})]:
        ar, vol, geo = mix(ws)
        print(f"   {name:34s} arithmetic {ar:.2f}%  vol {vol:.2f}%  approx compound {geo:.2f}%")
    # dollar effect on the sleeve, 2028 -> 2033 (5 years), equity part only
    for g_us, g_gl, lab in [(6.70, 7.00, "JPM compound US LC vs AC World")]:
        eq0 = 0.60 * sleeve
        a = eq0 * (1 + g_us / 100) ** 5
        b = eq0 * (1 + g_gl / 100) ** 5
        print(f"   {lab}: ${eq0:,.0f} equity for 5 yrs -> ${a:,.0f} vs ${b:,.0f}; difference ${b - a:,.0f}")


if __name__ == "__main__":
    main()
