"""E3 (Laura-as-client red team) - three client-facing numbers behind phase_E/E3_laura.md.

How to run (repo root, about 10 seconds, no network needed):
    .venv/bin/python research/insight_v1/scripts/E3_client_view_numbers.py

It re-uses E1's module (research/insight_v1/scripts/E1_split_and_slices.py), which re-uses D6's engine (same random
stream, same lognormal fit, same lock-early sleeve). So every model number here differs from E1/D6 only in what is
computed, not in the simulation. It prints:
 [1] How much of Laura's first deposit the ten payments cost (the part of the 2027 caution that is FORCED by prices,
     not chosen by the team).
 [2] Whole-portfolio stock share on Jan 1 of each year 2027-2032 (median across paths of each path's share) and the
     six-year average, for growth splits 50/50 and 60/40 and 2031 lock shares 0.8 and 0.7; plus the stock share of
     the money only she depends on (the growth money) by stage.
 [3] The 2031 message seen from the median 2031 state: the bought bottom, the likely (median) 2033 gift, the top
     (90th percentile), how much of the likely gift is already bought when she speaks, and how far the unlocked money
     would have to fall for the gift to land in the lower half of the range.

INPUTS and status labels
 - Treasury par curve 2026-09-25: competition/official_market_data/daily-treasury-rates_2026-09.csv row 09/25/2026
   (VERIFIED-REPO-FILE). Ladder forward values on Jan 1 2028-2032 use A2_curve_recheck.value_at (same method as the
   verified official_curve_pv.py; bootstrap/interpolation method is an ASSUMPTION).
 - $292,264 exact-date ladder (F-101, VERIFIED-REPO-FILE inputs + ASSUMPTION method); $294,387 real Nov-15 STRIPS ladder
   (S1/D3, same labels); $300,000 and $150,000 deposits (case p.2 L43-45, VERIFIED-REPO-FILE).
 - Equity JPM AC World 7.00% compound / 8.28% arithmetic (VERIFIED-REPO-FILE, JPM 2026 LTCMA p.2); sleeve bonds 5.00%
   (ASSUMPTION, market-consistent, as E1 [3]-[4]); 2031 two-year rate 4.81% (VERIFIED-REPO-FILE input, ASSUMPTION it
   holds in 2031); no fee.
 - The 2027 leftover waits in T-bills (ticket rule), so the real 2027 stock share is 0%. The engine itself invests the
   leftover during 2027 (a known simplification, effect under $1k; D3 audit C17).
 - i.i.d. lognormal annual returns (ASSUMPTION). Every model output is a MODEL PROPERTY, not a forecast.
"""
import csv
import importlib.util
import os
from datetime import date

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # both modules guard their printing with __main__
    return mod


E1 = load("E1_split_and_slices")
A2 = load("A2_curve_recheck")
D6 = E1.D6


def k(x):
    return f"${x / 1000:,.0f}k"


def curve_row():
    with open(os.path.join(REPO, "competition/official_market_data/daily-treasury-rates_2026-09.csv")) as fh:
        rows = list(csv.DictReader(fh))
    row = next(r for r in rows if r["Date"] == "09/25/2026")
    row["_date"] = date(2026, 9, 25)
    return row


def section1():
    print("[1] What the ten payments cost, as a share of the first $300,000 deposit (2026-09-25 curve)")
    for label, cost in (("exact-date zeros (F-101)", 292_264), ("real Nov-15 STRIPS ladder (S1/D3)", 294_387)):
        print(f"    {label:36s}: ${cost:,} = {cost / 300_000 * 100:.1f}% of $300,000; left over ${300_000 - cost:,}")


def section2(row):
    print("\n[2] Whole-portfolio stock share on Jan 1 (median of each path's share; JPM ACWI 7.00, bonds 5.0, no fee)")
    lad = {y: A2.value_at(row, date(y, 1, 1)) for y in range(2028, 2034)}
    print("    ladder forward values: " + ", ".join(f"{y} {k(v)}" for y, v in lad.items()))
    req, rbd = D6.draws(E1.JPM_ACWI, bd=D6.BD_CONSISTENT)
    for w in (0.5, 0.6):
        for a in (0.8, 0.7):
            _, _, tr = D6.lock_early(req, rbd, eq_w=w, floor_share=a)
            S31 = tr[:, 4]
            shares = [0.0]                                              # 2027: leftover in T-bills
            s28 = tr[:, 1] + D6.DEP
            shares.append(np.median(w * s28 / (lad[2028] + s28)))
            for i, y in ((2, 2029), (3, 2030)):
                shares.append(np.median(w * tr[:, i] / (lad[y] + tr[:, i])))
            shares.append(np.median(w * (1 - a) * S31 / (lad[2031] + S31)))
            floor32 = a * S31 * (1 + D6.Y2)
            rest32 = tr[:, 5] - floor32
            shares.append(np.median(w * rest32 / (lad[2032] + tr[:, 5])))
            avg = float(np.mean(shares))
            print(f"    split {int(w * 100)}/{int(100 - w * 100)}, lock {a}: " +
                  " ".join(f"{y} {s * 100:4.1f}%" for y, s in zip(range(2027, 2033), shares)) +
                  f" | six-year average {avg * 100:.1f}%")
        print(f"    growth money only (money nobody else relies on): 2028-30 {w * 100:.0f}% stocks;"
              f" 2031-32 {w * 20:.0f}% (lock 0.8) or {w * 30:.0f}% (lock 0.7) of the growth money")


def section3():
    print("\n[3] The 2031 message at the median 2031 state (50/50 split; top = p90; no cap)")
    w = 0.5
    req, rbd = D6.draws(E1.JPM_ACWI, bd=D6.BD_CONSISTENT)
    _, _, tr = D6.lock_early(req, rbd, eq_w=w, floor_share=0.8)
    S_med = float(np.median(tr[:, 4]))
    G2 = (1 + w * req[:, 4] + (1 - w) * rbd[:, 4]) * (1 + w * req[:, 5] + (1 - w) * rbd[:, 5])
    gf = (1 + D6.Y2) ** 2
    g50, g90 = float(np.median(G2)), float(np.percentile(G2, 90))
    print(f"    median 2031 growth money {k(S_med)}; unlocked money's 2-year growth p50 {g50:.3f}, p90 {g90:.3f}")
    for a, s in ((0.8, 0.5), (0.7, 0.5)):
        bottom = a * S_med * gf
        rest = (1 - a) * S_med
        likely = bottom + s * rest * g50
        top = bottom + s * rest * g90
        mid = (bottom + top) / 2
        g_mid = (mid - bottom) / (s * rest)          # growth factor that puts the gift exactly at the midpoint
        p_lower_half = float((G2 < g_mid).mean())
        print(f"    slices {a * 100:.0f}/{s * (1 - a) * 100:.0f}/{(1 - s) * (1 - a) * 100:.0f}: bottom {k(bottom)},"
              f" likely {k(likely)}, top {k(top)}; bought share of the likely gift {bottom / likely * 100:.0f}%;"
              f" lower half needs the unlocked money to fall {(1 - g_mid) * 100:.0f}% in two years"
              f" (P = {p_lower_half * 100:.1f}% of paths); kept for the project {k((1 - s) * rest * g50)}")


if __name__ == "__main__":
    section1()
    section2(curve_row())
    section3()
