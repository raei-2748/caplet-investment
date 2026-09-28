"""D3_joint_tail.py - M053: how large is the joint tail in which rates fall before the January 2027 purchase (the ladder
costs more than $300,000, so the longest payments are bought first) AND the 2028 deposit is late, smaller or missing?

What it computes:
 1. A conditional dollar table (no probabilities needed): for parallel rate moves between 2026-09-25 and 2027-01-01,
    the cost of the real Nov-15 STRIPS ladder, the gap above $300,000, which payment is left partly unbought under
    "longest rungs first", what completing it costs in January 2028 (no further rate move), and how much of the
    payments stays unfunded if the deposit is $0, $10k or $25k.
 2. Model probabilities (strategy_mc_v2): P(gap), and P(payments short | deposit cut) when the deposit cut is
    independent of markets vs linked to a 2027 recession that markets start pricing before January (correlations are
    ASSUMPTION scenarios; the case says she "will" contribute, R-AN35).
 3. Rule check: "longest rungs first" vs "nearest rungs first" - how much the 2028 top-up bill can move if rates keep
    falling during 2027 (yearly sd 0.71pp, F-014).
 4. Evidence on the recession link: in U.S. stock-market down years since 1928, what did 10-year Treasuries do
    (Damodaran annual returns); 10-year yield changes in 2001, 2008, 2020 and 2022 (FRED DGS10).
Inputs and status: official curve 2026-09-25 (VERIFIED-REPO-FILE) and the Nov-15 STRIPS dates (S1, VERIFIED-PRIMARY
Treasury MSPD); pre-purchase sd 0.37pp (F-014 2026 vol; VERIFIED-PRIMARY inputs, derived) and 0.48pp (FRED DGS10
98-day changes since 1990, derived); Damodaran histretSP (VERIFIED-PRIMARY dataset page, accessed 2026-09-28); FRED
DGS10 (VERIFIED-PRIMARY, accessed 2026-09-28). Deposit-cut probability, size and correlations: ASSUMPTION.
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_joint_tail.py
"""
import csv
import sys

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
from strategy_mc_v2 import TABLES, Cfg, interp_rows, simulate  # noqa: E402

FRED10 = "research/insight_v1/scripts/data/D3/fred_DGS10.csv"
HIST = "research/insight_v1/scripts/data/D3/damodaran_histretSP_1928_2025.csv"


def ladder_fill(rung_costs, budget=300_000):
    """Longest rungs first; returns funded fraction per rung (2033..2042)."""
    frac = np.zeros(10)
    left = budget
    for i in range(9, -1, -1):
        take = min(1.0, max(left, 0) / rung_costs[i])
        frac[i] = take
        left -= take * rung_costs[i]
    return frac


def main():
    print("== 1. Conditional dollars (Nov-15 STRIPS ladder; move = parallel par-curve shift before 1 Jan 2027)")
    print("  move | ladder cost | gap over $300k | unbought face (payment years) | Jan-2028 cost to finish | "
          "unfunded face if deposit $0 / $10k / $25k")
    for bp in (0, -19, -25, -50, -75, -100, -125, -150):
        s = np.array([bp / 100])
        c27 = interp_rows(TABLES["strip"][1], s)[0]
        c28 = interp_rows(TABLES["strip"][2], s)[0]
        frac = ladder_fill(c27)
        unb = (1 - frac) * 50_000
        need28 = ((1 - frac) * c28).sum()
        yrs = [2033 + i for i in range(10) if unb[i] > 1]
        shorts = []
        for dep in (0, 10_000, 25_000):
            paid = min(dep, need28)
            shorts.append(unb.sum() * (1 - paid / need28) if need28 > 0 else 0.0)
        print(f"  {bp:+4d}bp | ${c27.sum():,.0f} | ${max(c27.sum() - 300_000, 0):,.0f} | ${unb.sum():,.0f} {yrs} | "
              f"${need28:,.0f} | " + " / ".join(f"${x:,.0f}" for x in shorts))

    print("\n== 2. Model probabilities (Nov-15 STRIPS; payments short = some face of a payment not bought)")
    print("  scenario | P(gap in Jan 2027) | P(short) | P(short | deposit cut) | short if short: mean / p95 / max")
    rows = [("deposit arrives ($150k, 2028)", dict()),
            ("deposit late ($150k in 2029)", dict(deposit_year=2)),
            ("deposit $10k", dict(deposit=10_000)),
            ("deposit missing, markets independent", dict(deposit=0.0)),
            ("deposit missing, pre-purchase sd 0.48pp", dict(deposit=0.0, pre_rate_sd=0.48)),
            ("cut to $0 in 25%: independent", dict(cut_prob=0.25, cut_frac=1.0)),
            ("cut to $0 in 25%: rho 0.6 with 2027 stocks, link 0.5", dict(cut_prob=0.25, cut_frac=1.0,
                                                                         rho_deposit=0.6, rho_pre_stock=0.5)),
            ("cut to $0 in 25%: rho 0.9, link 0.8 (extreme)", dict(cut_prob=0.25, cut_frac=1.0, rho_deposit=0.9,
                                                                   rho_pre_stock=0.8))]
    for name, kw in rows:
        cfg = Cfg(ladder="strips", pre_rate_sd=kw.pop("pre_rate_sd", 0.37), **kw)
        r = simulate(cfg)
        sh = r["short_face"]
        cut = r["deposit"] < cfg.deposit - 1
        pc = f"{np.mean(sh[cut] > 0) * 100:5.1f}%" if cut.any() else "  n/a"
        s_pos = sh[sh > 0]
        st = (f"${s_pos.mean():,.0f} / ${np.percentile(s_pos, 95):,.0f} / ${s_pos.max():,.0f}" if s_pos.size else "-")
        print(f"  {name:52s} | {np.mean(r['gap27'] > 0) * 100:4.1f}% | {np.mean(sh > 0) * 100:5.2f}% | "
              f"{pc} | {st}")

    print("\n== 3. Which rungs to leave for 2028: longest-first (plan) vs nearest-first, given the gap at -50bp")
    s = np.array([-0.5])
    c27 = interp_rows(TABLES["strip"][1], s)[0]
    rng = np.random.default_rng(7)
    dy27 = 0.71 * rng.standard_normal(100_000)                    # further parallel move during 2027 (F-014)
    c28 = interp_rows(TABLES["strip"][2], -0.5 + dy27)            # (n, 10) January-2028 prices
    for lab, order in (("longest first (plan)", range(9, -1, -1)), ("nearest first", range(10))):
        frac, left = np.zeros(10), 300_000.0
        for i in order:
            take = min(1.0, max(left, 0) / c27[i])
            frac[i] = take
            left -= take * c27[i]
        bill = ((1 - frac) * c28).sum(1)
        print(f"  {lab:22s}: 2028 bill median ${np.median(bill):,.0f}, 5-95% ${np.percentile(bill, 5):,.0f} to "
              f"${np.percentile(bill, 95):,.0f} (unbought: {[2033 + i for i in range(10) if frac[i] < 1]})")

    print("\n== 4. Evidence: do Treasuries rally when U.S. stocks fall? (annual, Damodaran 1928-2025)")
    h = [r for r in csv.DictReader(l for l in open(HIST) if not l.startswith("#"))]
    down = [(int(r["year"]), float(r["sp500_tr"]), float(r["tbond_10y_tr"])) for r in h if float(r["sp500_tr"]) < -0.10]
    pos = sum(1 for _, _, b in down if b > 0)
    print(f"  S&P 500 years below -10%: {len(down)}; 10-year Treasury return positive in {pos} of them: " +
          ", ".join(f"{y} ({e:+.0%}/{b:+.0%})" for y, e, b in down))
    eq = np.array([float(r["sp500_tr"]) for r in h])
    bd = np.array([float(r["tbond_10y_tr"]) for r in h])
    yr = np.array([int(r["year"]) for r in h])
    for a, b in ((1928, 2025), (1966, 1999), (2000, 2021), (2022, 2025)):
        m = (yr >= a) & (yr <= b)
        print(f"  corr(stocks, 10y Treasury returns) {a}-{b}: {np.corrcoef(eq[m], bd[m])[0, 1]:+.2f} (n={m.sum()})")
    ys = {}
    for r in csv.DictReader(open(FRED10)):
        if r["DGS10"] not in (".", ""):
            ys[r["observation_date"]] = float(r["DGS10"])
    ends = {}
    for d, v in ys.items():
        ends[int(d[:4])] = v                                   # last observation of each year
    for y in (2001, 2002, 2008, 2020, 2022):
        print(f"  10-year yield {y}: {ends[y - 1]:.2f}% -> {ends[y]:.2f}% ({(ends[y] - ends[y - 1]) * 100:+.0f}bp)")


if __name__ == "__main__":
    main()
