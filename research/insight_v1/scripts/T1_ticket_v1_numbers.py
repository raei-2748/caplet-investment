"""T1_ticket_v1_numbers.py - numbers behind research/insight_v1/wins_now/securities_and_allocation_v1.md and
research/insight_v1/phase_D/trading_now_brief.md (agent T1, Trading-Now editor, insight_v1 run, 2026-09-28).

PROVISIONAL research for Team Caplet. Not approved by the team. Every ticker is PENDING WInS AVAILABILITY +
POSITION-LIMIT CHECK. Nothing here is text to submit.

What it does (plain English):
1. Re-solves the IEF/TLH hedge mix from the issuer "effective duration" numbers dated 2026-09-25 (target 9.90 years on
   issuer numbers, the ticket's convention, which is about 10.1 years in full-revaluation terms; S4 finding 8).
2. Builds the order tables for option (ii) (post-2028 mix scaled to $300,000) at a 60/40 and a 50/50 growth split, and
   for option (iii) (literal January-2027 book) with its named third trade: the ~2% 2027 leftover in a T-bill ETF.
3. Builds the position-limit branches for both options: no cap, 35%, 25%, and a rule for caps under 25% (each capped
   fund one point under the cap, fewest funds, hedge about 10 years), with forward-consistent tracking error from
   research/insight_v1/scripts/S4_red_team_checks.py (fund forward value vs the ten payments' forward value).
4. Shows the equity side of a low cap (VT above cap-1 is split into VTI/VXUS 62/38 of the equity, the ticket's
   alternate) and the T-bill trade's economics inside the WInS window (interest vs the $25 commission).

Inputs (status labels; all issuer pages re-read by T1 with curl on 2026-09-28 ~00:35 UTC unless noted):
- Closing prices 2026-09-25 (VERIFIED-PRIMARY): IEF 90.00, TLH 93.38, TLT 79.32, SHY 81.21, SGOV 100.66, IBTM 21.85
  (ishares.com product pages); VT 160.03, VGSH 57.59, VGLT 50.98, VGIT 56.90, VTI 379.77 (Vanguard price API, "market"
  price). SPTL 24.27, SPTI 27.31 and BIL 91.58 are the closes shown "as of Sep 24 2026" on ssga.com (VERIFIED-PRIMARY). VXUS 86.35
  (2026-09-25) is from S3's read of the Vanguard API on 2026-09-27 (VERIFIED-PRIMARY via S3; T1's re-read failed).
- Effective durations (VERIFIED-PRIMARY): IEF 6.86, TLH 11.58, TLT 14.84, SHY 1.79, SGOV 0.10 (as of 2026-09-25,
  ishares.com); SPTL 13.65 (OAD, as of 2026-09-24, ssga.com); VGIT 4.9, VGLT 13.5, VGSH 1.9 (as of 2026-08-31,
  Vanguard API); SPTI 4.78 (fund OAD, as of 2026-09-24, ssga.com, re-read by T1). TLH was 11.59 on 2026-09-24 (v0); 11.58 on 2026-09-25.
- BIL yield to maturity 3.94% (as of 2026-09-24, ssga.com, VERIFIED-PRIMARY) for the T-bill interest arithmetic.
- $300,000 WInS starting cash (SMApply Trading Details, VERIFIED-PRIMARY via phase_A). Commission $25 per ETF trade
  (SMApply FAQ "Each stock transaction is charged a flat $25"; ASSUMPTION that ETFs count as stock transactions).
- Nov-15 STRIPS ladder cost $294,387 for 2027-01-01 on the 2026-09-25 curve (S1/S3, model on VERIFIED-REPO-FILE curve).
- Plan shares after the 2028 deposit (S3 script section 3; ASSUMPTION-based): hedge 65.9%, equity 20.4% at a 60/40
  growth split; 17.0% at 50/50 (D2 / AX2 C7). The ticket rounds the hedge to 66% and takes the 1% cash float out of
  the short-Treasury part, so VT = the plan's whole-portfolio stock share.
- ASSUMPTIONS: the position limit is checked when an order is placed; a 1-point buffer under any cap; the cash float
  is at least $1,000; forward-consistent tracking as in S4 (instantaneous shocks; SPTL modelled with VGLT holdings).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/T1_ticket_v1_numbers.py
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, "research/insight_v1/wins_now")
sys.path.insert(0, "research/insight_v1/scripts")
import S1_hedge_weights as s1  # noqa: E402
from S4_red_team_checks import fwd_track, worst  # noqa: E402

CASH = 300_000
COMM = 25
TARGET = 9.90
PRICE = {"IEF": 90.00, "TLH": 93.38, "TLT": 79.32, "SHY": 81.21, "SGOV": 100.66, "IBTM": 21.85, "VT": 160.03,
         "VGSH": 57.59, "VGLT": 50.98, "VGIT": 56.90, "VTI": 379.77, "SPTL": 24.27, "BIL": 91.58, "VXUS": 86.35,
         "SPTI": 27.31}
DUR = {"IEF": 6.86, "TLH": 11.58, "TLT": 14.84, "SPTL": 13.65, "VGIT": 4.9, "VGLT": 13.5, "SPTI": 4.78}
# preference order for hedge funds under a cap (ticket rule: IEF, TLH, then SPTL; then the Vanguard pair; SPTI; TLT last
# because it is the longest and furthest from the payment dates)
PREF = ["IEF", "TLH", "SPTL", "VGIT", "VGLT", "SPTI", "TLT"]


def shares(tot_pct, tkr):
    p = PRICE.get(tkr)
    if not p:
        return "n/a"
    return f"{math.floor(tot_pct / 100 * CASH / p):,}"


def track(tot):
    h = sum(tot.values())
    w = {k: v / h for k, v in tot.items()}
    tw, pa = worst(fwd_track(w))
    return tw, pa


def dur_of(tot):
    h = sum(tot.values())
    return sum(v * DUR[k] for k, v in tot.items()) / h


def row(label, tot, extra=None):
    d = dur_of(tot)
    tw, pa = track(tot)
    orders = " / ".join(f"{k} {v:.1f}% (${v / 100 * CASH:,.0f}, ~{shares(v, k)} sh)" for k, v in tot.items())
    print(f"   {label}: {orders} | hedge {sum(tot.values()):.1f}% | issuer duration {d:.2f}y | worst 50bp twist "
          f"${tw:,.0f} ({tw / s1.L0:.2%} of a $292k hedge) | worst +/-100bp ${pa:,.0f}" + (extra or ""))


def capped(hedge, cap):
    """Fewest hedge funds, each <= cap-1 (share of the total), duration = TARGET on issuer numbers, always keeping IEF
    and TLH; among feasible sets take the earliest in PREF order and fill preferred funds first."""
    work = cap - 1.0
    nmin = max(2, math.ceil(hedge / work - 1e-9))
    for n in range(nmin, len(PREF) + 1):
        for rest in itertools.combinations(PREF[2:], n - 2):
            combo = ("IEF", "TLH") + rest          # the ticket keeps IEF and TLH and adds funds after them
            d = np.array([DUR[k] for k in combo])
            c = -np.array([len(PREF) - PREF.index(k) for k in combo], dtype=float)   # prefer earlier funds
            r = linprog(c, A_eq=np.vstack([np.ones(n), d]), b_eq=[hedge, TARGET * hedge],
                        bounds=[(0, work)] * n, method="highs")
            if r.status == 0:
                tot = {k: round(v, 1) for k, v in zip(combo, r.x) if v > 0.05}
                return tot
    return None


if __name__ == "__main__":
    w_ief = (DUR["TLH"] - TARGET) / (DUR["TLH"] - DUR["IEF"])
    print(f"[1] IEF share of the hedge = (11.58 - 9.90)/(11.58 - 6.86) = {w_ief:.4f}; TLH {1 - w_ief:.4f} "
          f"(v0 at TLH 11.59: 0.3569)")

    print("\n[2] Orders at $300,000 (share counts at the closes listed in the docstring; recompute on the trade date)")
    h2 = 66.0
    ief2, tlh2 = round(h2 * w_ief, 1), round(h2 * (1 - w_ief), 1)
    for split, vt, vgsh in (("60/40", 20.5, 12.5), ("50/50", 17.0, 16.0)):
        tot = {"IEF": ief2, "TLH": tlh2, "VT": vt, "VGSH": vgsh}
        print(f"   (ii) {split}: " + " / ".join(f"{k} {v:.1f}% ${v / 100 * CASH:,.0f} ~{shares(v, k)} sh"
                                                  for k, v in tot.items()) +
              f" / cash {100 - sum(tot.values()):.1f}% ${(100 - sum(tot.values())) / 100 * CASH:,.0f}; "
              f"4 trades ${4 * COMM}; VT share of growth money {vt / (vt + vgsh):.0%}")
    h3 = 98.0
    ief3, tlh3 = round(h3 * w_ief, 1), round(h3 * (1 - w_ief), 1)
    leftover = CASH - 294_387
    tb = leftover - 1_000 - 3 * COMM
    print(f"   (iii): IEF {ief3}% ${ief3 / 100 * CASH:,.0f} ~{shares(ief3, 'IEF')} sh / TLH {tlh3}% "
          f"${tlh3 / 100 * CASH:,.0f} ~{shares(tlh3, 'TLH')} sh / T-bill ETF about ${tb:,.0f} "
          f"({tb / CASH:.1%}): SGOV ~{math.floor(tb / PRICE['SGOV'])} sh or BIL ~{math.floor(tb / PRICE['BIL'])} sh / "
          f"cash about ${CASH * (1 - (ief3 + tlh3) / 100) - tb - 3 * COMM:,.0f} after 3 trades (${3 * COMM})")
    print(f"      2027 leftover in the real plan: $300,000 - $294,387 = ${leftover:,} ({leftover / CASH:.2%})")
    row("(ii) no cap", {"IEF": ief2, "TLH": tlh2})
    row("(iii) no cap", {"IEF": ief3, "TLH": tlh3})

    print("\n[3] Position-limit branches (share of the TOTAL; each capped fund 1 point under the cap)")
    print("  option (ii), hedge 66%:")
    row("35% cap", {"IEF": ief2, "TLH": 34.0, "SPTL": round(h2 - ief2 - 34.0, 1)})
    row("25% cap (3-fund rule, S4)", {"IEF": ief2, "TLH": 24.0, "SPTL": round(h2 - ief2 - 24.0, 1)})
    for cap in (20, 15):
        t = capped(h2, cap)
        row(f"{cap}% cap (fewest funds)", t)
    print("  option (iii), hedge 98%:")
    row("35% cap", {"IEF": 34.0, "TLH": 34.0, "SPTL": 30.0})
    row("25% cap (D10/v0)", {"IEF": 24.0, "TLH": 24.0, "SPTL": 24.0, "VGIT": 17.6, "VGLT": 8.4})
    for cap in (20, 15):
        t = capped(h3, cap)
        if t is None:
            print(f"   {cap}% cap: NOT FEASIBLE with the 7 listed Treasury ETFs at about 10 years")
        else:
            row(f"{cap}% cap (fewest funds)", t)
    for hedge, lab in ((h2, "(ii)"), (h3, "(iii)")):
        need = {}
        for cap in (65, 44, 35, 30, 25, 22, 20, 17, 15, 12):
            t = capped(hedge, cap)
            need[cap] = len(t) if t else "infeasible"
        print(f"   hedge funds needed {lab}: " + ", ".join(f"cap {c}%: {n}" for c, n in need.items()))

    print("\n[4] Equity side of a low cap, option (ii)")
    for vt in (20.5, 17.0):
        for cap in (25, 20, 18, 15):
            if vt > cap - 1:
                print(f"   VT {vt}% under a {cap}% cap -> VTI {vt * .62:.1f}% (~{shares(vt * .62, 'VTI')} sh) + "
                      f"VXUS {vt * .38:.1f}% (~{shares(vt * .38, 'VXUS')} sh)")
            else:
                print(f"   VT {vt}% under a {cap}% cap: fits")

    print("\n[5] T-bill leg of option (iii): interest inside the WInS window vs the $25 commission (ASSUMPTION: "
          "3.94% BIL YTM, simple interest)")
    for days, lab in ((36, "fill Oct 1 -> freeze Nov 6"), (365, "the real plan: Jan 2027 -> Jan 2028")):
        amt = tb if days < 100 else leftover
        print(f"   {lab}: ${amt:,.0f} x 3.94% x {days}/365 = ${amt * .0394 * days / 365:,.0f}")
