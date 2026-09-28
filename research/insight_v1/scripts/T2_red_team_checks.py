"""T2_red_team_checks.py - arithmetic behind research/insight_v1/wins_now/T2_red_team.md (agent T2, adversarial red
team of the WInS ticket v1 and the trading-now brief, insight_v1 run, 2026-09-28).

PROVISIONAL research for Team Caplet, not approved by the team. Every ticker is PENDING WInS AVAILABILITY +
POSITION-LIMIT CHECK. Nothing here is text to submit. It re-computes the ticket's numbers and tests where they break.

What it does (plain English):
[1] Re-computes every order in the ticket (options (ii) 60/40 and 50/50, option (iii)) with whole shares at the
    2026-09-25 closes, adds the commissions and prints the cash left, so the tables can be checked to the dollar.
[2] Option (iii)'s third trade (the 2027 leftover in a T-bill fund) depends on the ladder costing less than $300,000
    on the trade date. Re-prices the real Nov-15 STRIPS ladder for a parallel rate move and prints the rate fall that
    shrinks the T-bill leg below $1,000 or to zero, and the chance of that fall before a fill on Oct 2 or Oct 9.
[3] Overnight-gap check: orders placed while the U.S. market is closed fill at the next open. How big a rate fall at
    the open would make the planned orders cost more than the cash float (options (ii) and (iii)), and how often a
    one-day move that large happens.
[4] The "tested" window: the chance of a 10bp-or-larger move in the 10-year yield from the fill date to the Oct 20
    close, for fills on Oct 1, Oct 2 and Oct 9.
[5] Continuous position-limit check with a stock fall (not only a rate fall): under option (ii) with a 25% cap, how far
    stocks must fall (rates unchanged) before TLH at 24% crosses 25%.
[6] Dated-rung table: re-solves IEF/TLH with the ticket's own hand formula for the rung rows it prints.
[7] Characters used by the ticket's own required note elements (element phrases taken from the ticket's section 5
    table, not a drafted note), to see whether the four-element core fits 300 characters.

Inputs (status labels):
- Closes 2026-09-25 and issuer durations: as listed in research/insight_v1/scripts/T1_ticket_v1_numbers.py
  (VERIFIED-PRIMARY there: ishares.com, ssga.com, Vanguard API, read 2026-09-28).
- Nov-15 STRIPS ladder cost for 2027-01-01 on the 2026-09-25 curve: $294,387; at -25/-50/-100bp: $301,676 / $309,169 /
  $324,793 (S4_red_team.md finding 9; model on a VERIFIED-REPO-FILE curve; ASSUMPTION: parallel shifts).
- Realised 2026 volatility of daily 10-year yield changes: 4.45bp/day (D7_wharton_intent.md, VERIFIED-PRIMARY data;
  driftless normal ASSUMPTION; fatter tails would raise every tail probability here).
- Ticket weights and rules: research/insight_v1/wins_now/securities_and_allocation_v1.md (PROVISIONAL).
- Commission $25 per ETF trade (SMApply FAQ, VERIFIED-PRIMARY; ASSUMPTION that ETFs count as "stock"); $10 per bond.
- Equity one-day move for the gap test: 1% (ASSUMPTION, roughly one daily standard deviation at 16.8% a year).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/T2_red_team_checks.py
"""
import math

import numpy as np
from scipy.stats import norm

CASH, COMM = 300_000, 25
PRICE = {"IEF": 90.00, "TLH": 93.38, "VT": 160.03, "VGSH": 57.59, "SGOV": 100.66, "BIL": 91.58, "SPTL": 24.27,
         "VTI": 379.77, "VXUS": 86.35}
DUR = {"IEF": 6.86, "TLH": 11.58, "SPTL": 13.65, "VGSH": 1.9, "SGOV": 0.10, "VGIT": 4.9, "VGLT": 13.5}
VOL_BP = 4.45
LADDER = {0: 294_387, -25: 301_676, -50: 309_169, -100: 324_793}


def ladder_cost(shift_bp):
    """Quadratic fit through S4's four model prices (parallel shift in bp; negative = rates fall)."""
    x = np.array(list(LADDER.keys()), dtype=float)
    y = np.array(list(LADDER.values()), dtype=float)
    c = np.polyfit(x, y, 2)
    return float(np.polyval(c, shift_bp))


def book(weights):
    """Whole shares at the 9/25 closes; returns ({ticker: (shares, dollars)}, cash left after commissions)."""
    out, spent = {}, 0.0
    for k, w in weights.items():
        sh = math.floor(w / 100 * CASH / PRICE[k])
        out[k] = (sh, sh * PRICE[k])
        spent += sh * PRICE[k]
    return out, CASH - spent - COMM * len(weights)


def dollars_per_bp(pos):
    """First-order dollar gain of the listed positions for a 1bp fall in rates."""
    return sum(v * DUR.get(k, 0) * 1e-4 for k, (_, v) in pos.items())


if __name__ == "__main__":
    print("[1] Orders with whole shares at 2026-09-25 closes")
    books = {
        "(ii) 60/40": {"IEF": 23.5, "TLH": 42.5, "VT": 20.5, "VGSH": 12.5},
        "(ii) 50/50": {"IEF": 23.5, "TLH": 42.5, "VT": 17.0, "VGSH": 16.0},
        "(iii)": {"IEF": 34.9, "TLH": 63.1, "SGOV": 4538 / CASH * 100},
    }
    res = {}
    for lab, w in books.items():
        pos, left = book(w)
        res[lab] = (pos, left)
        print(f"   {lab}: " + " / ".join(f"{k} {s:,} sh ${v:,.0f}" for k, (s, v) in pos.items())
              + f" | commissions ${COMM * len(w)} | cash left ${left:,.0f}")
    vt, vg = res["(ii) 60/40"][0]["VT"][1], res["(ii) 60/40"][0]["VGSH"][1]
    print(f"   VT share of growth money at 60/40: {vt / (vt + vg):.1%} of VT+VGSH, "
          f"{vt / (vt + vg + res['(ii) 60/40'][1]):.1%} including the cash float")
    vt, vg = res["(ii) 50/50"][0]["VT"][1], res["(ii) 50/50"][0]["VGSH"][1]
    print(f"   VT share of growth money at 50/50: {vt / (vt + vg):.1%} of VT+VGSH, "
          f"{vt / (vt + vg + res['(ii) 50/50'][1]):.1%} including the cash float")

    print("\n[2] Option (iii): the T-bill leg as rates move before the trade date (Nov-15 ladder, parallel shift)")
    for s in (+20, +10, 0, -5, -10, -12, -15, -20, -25):
        leftover = CASH - ladder_cost(s)
        tb = leftover - 1_000 - 3 * COMM
        print(f"   shift {s:+4d}bp: ladder ${ladder_cost(s):,.0f}; leftover ${leftover:,.0f}; "
              f"T-bill leg after $1,000 float and 3 commissions ${tb:,.0f}")
    # find thresholds
    grid = np.arange(0, -40, -0.01)
    t_zero = next(g for g in grid if CASH - ladder_cost(g) - 1_075 <= 0)
    t_1k = next(g for g in grid if CASH - ladder_cost(g) - 1_075 <= 1_000)
    t_gap = next(g for g in grid if CASH - ladder_cost(g) <= 0)
    print(f"   T-bill leg under $1,000 after a fall of {abs(t_1k):.1f}bp; zero after {abs(t_zero):.1f}bp; "
          f"ladder above $300k after {abs(t_gap):.1f}bp")
    for days, lab in ((5, "Sep 25 close -> Oct 2 open (5 trading days)"),
                      (10, "Sep 25 close -> Oct 9 open (10 trading days)")):
        sd = VOL_BP * math.sqrt(days)
        print(f"   {lab}: sd {sd:.1f}bp; P(T-bill leg < $1,000) {norm.cdf(t_1k / sd):.0%}; "
              f"P(no leftover at all) {norm.cdf(t_zero / sd):.0%}; P(ladder > $300k) {norm.cdf(t_gap / sd):.0%}")

    print("\n[3] Overnight gap: orders sized at the last close, filled at the next open")
    for lab in ("(ii) 60/40", "(ii) 50/50", "(iii)"):
        pos, left = res[lab]
        bp = dollars_per_bp(pos)
        eq = pos.get("VT", (0, 0))[1] * 0.01
        need = (left - eq) / bp
        print(f"   {lab}: cash float ${left:,.0f}; the bond orders cost ${bp:,.0f} more per 1bp fall; with VT +1% "
              f"(${eq:,.0f}) the float is used up by a rate fall of {need:.1f}bp at the open; "
              f"P(one-day fall that large) {norm.cdf(-need / VOL_BP):.0%}; if sized at the Sep 25 closes and filled "
              f"Oct 1 (4 days) {norm.cdf(-need / (VOL_BP * 2)):.0%}")

    print("\n[4] 'Tested' window: P(|10y move| >= 10bp) from the fill to the Oct 20 close (driftless normal)")
    for days, lab in ((13, "fill Oct 1"), (12, "fill Oct 2"), (7, "fill Oct 9")):
        sd = VOL_BP * math.sqrt(days)
        print(f"   {lab}: {days} trading days, sd {sd:.1f}bp, P = {2 * norm.cdf(-10 / sd):.0%}")

    print("\n[5] Option (ii) at a 25% cap, 60/40: stock fall (rates unchanged) that lifts TLH from 24% to 25%")
    for vt_w in (20.5, 17.0):
        # TLH / (100 - vt_w * f) = 25%  ->  f = (100 - 24/0.25) / vt_w
        f = (100 - 24 / 0.25) / vt_w
        print(f"   VT {vt_w}% of the book: stocks must fall {f:.0%}")
    # combined: 10bp fall plus stock fall
    print("   With a 50bp rate fall at the same time (TLH +5.8%, IEF +3.4%, SPTL +6.8%, VGSH +1.0%):")
    for vt_w, vgsh in ((20.5, 12.5), (17.0, 16.0)):
        tlh = 24 * 1.0579
        others = 23.5 * 1.0343 + 18.5 * 1.06825 + vgsh * 1.0095 + 1.0
        f = (others + tlh - tlh / 0.25 + vt_w) / vt_w
        print(f"   VT {vt_w}%: stocks must fall {max(f, 0):.0%}")

    print("\n[6] Rung rows re-solved with the ticket's hand formula (target 9.90 on issuer durations)")
    for lab, hedge, rung, d_r in (("(iii) 2032 note", 98.0, 16.1, 5.3), ("(ii) 2032 note", 66.0, 11.0, 5.3),
                                  ("(iii) IBTM", 98.0, 12.3, 5.05), ("(ii) IBTM", 66.0, 8.4, 5.05)):
        r = rung / hedge
        ief = ((1 - r) * DUR["TLH"] + r * d_r - 9.90) / (DUR["TLH"] - DUR["IEF"])
        print(f"   {lab}: rung {rung}% -> IEF {ief * hedge:.1f}% / TLH {hedge - rung - ief * hedge:.1f}% of the book "
              f"(rung duration {d_r}y is an ASSUMPTION for the 2032 note; IBTM 5.05y issuer)")

    print("\n[7] Characters used by the ticket's required element phrases (not a note; phrases from ticket s5)")
    elements = {
        "promise (ii)": ["future funding", "promise money", "the ten $50,000 payments 2033-2042",
                         "about two-thirds of her portfolio after both deposits",
                         "moves about 10% per 1-point rate change, as the payments do",
                         "iShares effective durations as of 25 Sep 2026", "never sold after a rate rise"],
        "promise (iii)": ["future funding", "promise money", "the ten $50,000 payments 2033-2042",
                          "the payments cost about $294k for Jan 2027 at 1 Oct 2026 Treasury prices",
                          "never sold after a rate rise"],
        "growth (ii), provisional": ["growth", "growth money", "facility contribution and flexibility in 2033",
                                     "after her 2028 deposit", "provisional 60/40 split, decision by 16 Oct",
                                     "a fall shrinks the facility range, never the payments"],
    }
    for lab, parts in elements.items():
        n = sum(len(p) for p in parts) + 2 * (len(parts) - 1)
        print(f"   {lab}: {len(parts)} phrases, {n} characters before any connecting words "
              f"({300 - n} left under a 300-character cap)")
