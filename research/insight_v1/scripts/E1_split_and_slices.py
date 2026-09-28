"""E1 (Strategy Architect) - two checks behind the change proposals in phase_E/E1_change_proposals.md.

How to run (repo root, about 20 seconds):
    .venv/bin/python research/insight_v1/scripts/E1_split_and_slices.py

It re-uses D6's engine (research/insight_v1/scripts/D6_behavioural_numbers.py: same random stream, same lognormal
fit, same lock-early sleeve), so every number differs from D6/AY1 only in what is computed, not in the simulation.

WHAT IT PRINTS
 [1] The sleeve-split test (resolves D2 "50/50" vs D6 "rule gives 55-70%"). D6's plain rule is: hold the most stock
     in the growth money such that P(2033 growth money < the money Laura put into it, $157,736) <= 5% ("about 1 in
     20"). The rule is evaluated on a 5-point grid for every combination of: equity house (JPM U.S. large cap, JPM AC
     World, Vanguard U.S. midpoint, Vanguard U.S. low end), sleeve-bond return (4.00% JPM vs 5.00% market-consistent)
     and a yearly fee on the growth money (0 / 0.5% / 1.0%). For each cell it prints the pick, P(below) at 50% and
     60%, and the median and p5 of the 2033 growth money at 50% and 60%.
 [2] Which equity shares pass the rule in EVERY cell of a stated set (the "robust" test).
 [3] Whole-portfolio stock share by stage (Jan 2027, Jan 2028 after the deposit, Jan 2031 after the floor purchase)
     at the median path, for sleeve splits 50/50 and 60/40 and 2031 lock shares 0.7 and 0.8 (brief s16 / M033: a
     first reader sees these numbers).
 [4] The 2031 "three slices" (bought floor a; promised-but-still-at-risk s(1-a); kept for project flexibility
     (1-s)(1-a)) for candidate (a, s) pairs at 50/50 and 60/40: median floor, top at the 90th percentile of the
     unlocked money's 2-year growth given the median 2031 sleeve, top/bottom width, and 2033 gift and flexibility
     p5/p50/p95 across all paths. No cap on the gift (D5 method); P(gift above top | median 2031 state) = 10% and
     P(below floor) = 0 by construction (bought; residual risk U.S. default).

INPUTS and status labels
 - $292,264 ladder at 2027-01-01 (VERIFIED-REPO-FILE inputs, official_curve_pv.py; F-101); leftover $7,736 (F-104).
 - $150,000 deposit at 2028-01-01 (VERIFIED-REPO-FILE, case p.2 L43-45).
 - 2031 two-year rate = today's 2y par 4.81% (VERIFIED-REPO-FILE input; ASSUMPTION that it holds in 2031).
 - JPM 2026 LTCMA (VERIFIED-REPO-FILE, competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf p.2):
   U.S. large cap 6.70% compound / 7.94% arithmetic; AC World 7.00% / 8.28%; intermediate Treasuries 4.00% / 4.06%;
   correlation -0.01 (D6 engine value).
 - Vanguard VCMM U.S. equities 4.2%-6.2% (midpoint 5.2%), run of 2026-06-30 (VERIFIED-PRIMARY per D2 and AX2,
   corporate.vanguard.com, re-read 2026-09-28); used with JPM U.S. volatility kept (ASSUMPTION, as D6 case C).
 - Sleeve bonds 5.00% compound (ASSUMPTION, "market-consistent": VGSH SEC yield 4.55%, one-year forwards 4.8-5.1%,
   per D2/AX2 C8).
 - Fees 0.5% / 1.0% a year on the growth money (ASSUMPTION; the case names no fee; D8/D3 v2 sensitivities).
 - Ladder forward values 2028-01-01 $306,077 and 2031-01-01 $356,384 (VERIFIED-REPO-FILE inputs + ASSUMPTION method,
   F-106) for the whole-portfolio shares in [3]; the 2027 leftover waits in T-bills (ticket rule), so 2027 stock
   share is 0% for Laura's real portfolio.
 - i.i.d. lognormal annual returns, no taxes (ASSUMPTION, as in the verified strategy_mc.py). Every output is a MODEL
   PROPERTY under these assumptions, not a forecast.
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # D6 guards its printing with __main__, so importing is silent
    return mod


D6 = load("D6_behavioural_numbers")
MONEY_IN = 300_000 - D6.LADDER + D6.DEP     # $157,736
GRID = [x / 100 for x in range(40, 81, 5)]

JPM_US = D6.lp(0.0670, 0.0794)
JPM_ACWI = D6.lp(0.0700, 0.0828)
VG_MID = D6.lp(0.052, 0.052 + (0.0794 - 0.0670))     # JPM U.S. volatility kept (ASSUMPTION, as D6 case C)
VG_LOW = D6.lp(0.042, 0.042 + (0.0794 - 0.0670))
HOUSES = (("JPM US 6.70", JPM_US), ("JPM ACWI 7.00", JPM_ACWI), ("Vg mid 5.2", VG_MID), ("Vg low 4.2", VG_LOW))
BONDS = (("bonds 4.0", D6.BD), ("bonds 5.0", D6.BD_CONSISTENT))
FEES = (0.0, 0.005, 0.010)


def k(x):
    return f"${x / 1000:,.0f}k"


def sleeve_outcomes(req, rbd, w, fee, a=0.8):
    sur, _, _ = D6.lock_early(req - fee, rbd - fee, eq_w=w, floor_share=a)
    return sur


def section1():
    print("[1] Sleeve-split test: D6 plain rule (most stock with P(2033 growth money < $157.7k) <= 5%), 5-point grid,"
          " lock 0.8")
    print("    cell                          | pick | P(below) 50% / 60% | median 50% / 60% (diff) | p5 50% / 60%")
    results = {}
    for hl, eq in HOUSES:
        for bl, bd in BONDS:
            req, rbd = D6.draws(eq, bd=bd)
            for fee in FEES:
                probs, med, p5 = {}, {}, {}
                for w in GRID:
                    sur = sleeve_outcomes(req, rbd, w, fee)
                    probs[w] = float((sur < MONEY_IN).mean())
                    med[w] = float(np.median(sur))
                    p5[w] = float(np.percentile(sur, 5))
                ok = [w for w in GRID if probs[w] <= 0.05]
                pick = max(ok) if ok else None
                results[(hl, bl, fee)] = probs
                label = f"{hl}, {bl}, fee {fee * 100:.1f}%"
                print(f"    {label:30s}| {'none' if pick is None else str(int(pick * 100)) + '%':>4s} |"
                      f" {probs[0.5] * 100:4.1f}% / {probs[0.6] * 100:4.1f}%      |"
                      f" {k(med[0.5])} / {k(med[0.6])} ({(med[0.6] - med[0.5]) / 1000:+.1f}k) |"
                      f" {k(p5[0.5])} / {k(p5[0.6])}")
    return results


def section2(results):
    print("\n[2] Robust test: equity shares that pass the rule in EVERY cell of a set")
    sets = {
        "both houses' central cases (JPM ACWI, Vg mid), bonds 5.0, no fee":
            [("JPM ACWI 7.00", "bonds 5.0", 0.0), ("Vg mid 5.2", "bonds 5.0", 0.0)],
        "same, fee up to 0.5%":
            [(h, "bonds 5.0", f) for h in ("JPM ACWI 7.00", "Vg mid 5.2") for f in (0.0, 0.005)],
        "same, fee up to 1.0%":
            [(h, "bonds 5.0", f) for h in ("JPM ACWI 7.00", "Vg mid 5.2") for f in FEES],
        "all JPM cells (US and ACWI, both bond cases, all fees)":
            [(h, b, f) for h in ("JPM US 6.70", "JPM ACWI 7.00") for b in ("bonds 4.0", "bonds 5.0") for f in FEES],
        "every cell including Vanguard's low end":
            list(results.keys()),
    }
    for name, cells in sets.items():
        passing = [w for w in GRID if all(results[c][w] <= 0.05 for c in cells)]
        print(f"    {name:62s}: pass up to {'none' if not passing else str(int(max(passing) * 100)) + '%'}")


def section3():
    print("\n[3] Whole-portfolio stock share by stage at the median path (JPM ACWI 7.00, bonds 5.0, no fee)")
    req, rbd = D6.draws(JPM_ACWI, bd=D6.BD_CONSISTENT)
    ladder_2028, ladder_2031 = 306_077, 356_384
    for w in (0.5, 0.6):
        _, _, track = D6.lock_early(req, rbd, eq_w=w, floor_share=0.8)
        s28 = float(np.median(track[:, 1])) + D6.DEP      # Jan 2028 after the deposit
        s31 = float(np.median(track[:, 4]))               # Jan 2031 before the floor purchase
        sh28 = w * s28 / (ladder_2028 + s28)
        line = f"    sleeve {int(w * 100)}/{int(100 - w * 100)}: Jan 2027 0.0% (leftover in T-bills);" \
               f" Jan 2028 {sh28 * 100:.1f}% (sleeve {k(s28)});"
        for a in (0.7, 0.8):
            sh31 = w * (1 - a) * s31 / (ladder_2031 + s31)
            line += f" after 2031 floor a={a}: {sh31 * 100:.1f}%"
        print(line + f" (sleeve {k(s31)})")


def section4():
    print("\n[4] The 2031 three slices (JPM ACWI 7.00, bonds 5.0, no fee; top = 90th pct of the unlocked money's"
          " 2-year growth, at the median 2031 sleeve; no cap)")
    print("    split | a / s | slices bought/at-risk/kept | floor | top | width | gift p5/p50/p95 | kept p5/p50/p95")
    g_floor = (1 + D6.Y2) ** 2
    for w in (0.5, 0.6):
        req, rbd = D6.draws(JPM_ACWI, bd=D6.BD_CONSISTENT)
        _, _, track = D6.lock_early(req, rbd, eq_w=w, floor_share=0.8)
        S = track[:, 4]                                    # sleeve on 2031-01-01 (the lock share does not change it)
        G2 = (1 + w * req[:, 4] + (1 - w) * rbd[:, 4]) * (1 + w * req[:, 5] + (1 - w) * rbd[:, 5])
        S_med = float(np.median(S))
        g90 = float(np.percentile(G2, 90))
        for a, s in ((0.7, 0.5), (0.8, 0.5), (0.8, 1.0), (0.9, 0.5)):
            floor_m = a * S_med * g_floor
            top_m = floor_m + s * (1 - a) * S_med * g90
            rest = (1 - a) * S * G2
            gift = a * S * g_floor + s * rest
            kept = (1 - s) * rest
            slices = f"{a * 100:.0f}/{s * (1 - a) * 100:.0f}/{(1 - s) * (1 - a) * 100:.0f}"
            print(f"    {int(w * 100)}/{int(100 - w * 100)} | {a} / {s} | {slices:>26s} | {k(floor_m)} | {k(top_m)} |"
                  f" {top_m / floor_m:.2f}x | " + " / ".join(k(np.percentile(gift, p)) for p in (5, 50, 95)) +
                  " | " + " / ".join(k(np.percentile(kept, p)) for p in (5, 50, 95)))
            # sanity: P(gift above top | median state) is 10% by construction; P(below floor) is 0 by construction


if __name__ == "__main__":
    res = section1()
    section2(res)
    section3()
    section4()
