"""D1_wins_rung.py - one dated "demonstration rung" in the WInS hedge (question M044).

Agent D1 (Rates & Fixed-Income Analyst), insight_v1 run, 2026-09-28. PROVISIONAL research, not team-approved.
Every security here is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK.

What it computes (plain English):
 [1] Model price, accrued interest, yield and duration today of three individual U.S. Treasuries whose maturity falls
     just before one of Laura's Jan-1 payments: 4.125% 15-Nov-2032 (pays for Jan 2033), 4.375% 15-Nov-2039 (Jan 2040),
     4.25% 15-Nov-2040 (Jan 2041). Each is the parent bond of a principal STRIP in S1's real ladder.
 [2] How big one rung is in WInS under option (iii) (literal Jan-2027 book: face $50,000 = one payment) and option (ii)
     (post-2028 mix scaled to $300k: face scaled to the hedge), and what it costs versus the STRIP rung.
 [3] New IEF/TLH weights so the whole hedge keeps the same model duration as the S3 ticket's IEF/TLH mix, and the
     position sizes as shares of the $300,000 (for a 25% single-security cap check).
 [4] Forward-consistent tracking error (S4 method) of each hedge versus the ten payments under +/-100bp and 50bp twists:
     does adding a dated rung help or hurt the fit?
 [5] The same with the ETF alternate IBTM (iShares iBonds Dec 2032 Term Treasury ETF) instead of an individual bond.

Inputs (status labels):
- Curve 2026-09-25, liability, scenarios, fund cash flows (IEF, TLH, IBTM holdings as of 2026-09-24) and issuer
  durations: research/insight_v1/wins_now/S1_hedge_weights.py (VERIFIED-REPO-FILE curve; holdings VERIFIED-PRIMARY per
  S1, iShares, downloaded 2026-09-27) and S4_red_team_checks.py (forward-consistent tracking method).
- Bond coupons/maturities/CUSIPs: Treasury MSPD Table V, record date 2026-08-31
  (research/insight_v1/wins_now/S1_mspd_table5_2026-08-31_fixed_2032plus.csv; VERIFIED-PRIMARY per S1).
- Coupon dates May 15 / Nov 15 and accrued interest actual/actual from 2026-05-15 to the value date: standard Treasury
  convention (ASSUMPTION for WInS, which shows its own accrued figure).
- Model prices use the par-derived zero curve (ASSUMPTION; real quotes differ by a few bp). WInS prices update once a
  day at the U.S. open (SMApply FAQ, VERIFIED-PRIMARY, R-W91).
- Hedge sizes: option (iii) IEF 35.0% + TLH 63.0% of $300,000 = $294,000; option (ii) 66% = $198,000
  (research/insight_v1/wins_now/securities_and_allocation_v0.md; PROVISIONAL S3 ticket).
- IBTM close $21.85 on 2026-09-25, effective duration 5.05y, expense 0.07%, "will terminate on or about October or
  December 15 of the year in each Fund's name" (ishares.com/us/products/328944, read 2026-09-28, VERIFIED-PRIMARY).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D1_wins_rung.py
"""
import sys
from datetime import date

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, "research/insight_v1/wins_now")
sys.path.insert(0, "research/insight_v1/scripts")
import S1_hedge_weights as s1  # noqa: E402
import S4_red_team_checks as s4  # noqa: E402

BONDS = {  # name: (coupon %, maturity, CUSIP, payment it pays for)
    "T32": (4.125, "2032-11-15", "91282CFV8", "1 Jan 2033"),
    "T39": (4.375, "2039-11-15", "912810QD3", "1 Jan 2040"),
    "T40": (4.25, "2040-11-15", "912810QL5", "1 Jan 2041"),
}
for n, (c, m, _, _) in BONDS.items():
    s1.FUND_CF[n] = s1.cashflows(100.0, c, m)
    s1.V0[n] = s1.fund_value(n, s1.PAR)
    s1.MODEL_DUR[n] = s1.eff_dur(lambda p, n=n: s1.fund_value(n, p))

LAST_CPN = date(2026, 5, 15)
NEXT_CPN = date(2026, 11, 15)
H3, H2 = 294_000, 198_000
SPOT_PV = s4.spot_liability(s1.PAR)


def accrued(cpn, d=s1.VAL):
    return cpn / 2 * (d - LAST_CPN).days / (NEXT_CPN - LAST_CPN).days


def ytm(n):
    c, m, _, _ = BONDS[n]
    cfs = s1.FUND_CF[n]
    dirty = s1.V0[n]
    return brentq(lambda y: sum(a / (1 + y / 2) ** (2 * t) for t, a in cfs) - dirty, 0.0, 0.2)


def mix_with_rung(rung, w_rung, target_model_dur):
    """IEF/TLH weights (fractions of the hedge) that keep the hedge's model duration at the target."""
    di, dt, db = s1.MODEL_DUR["IEF"], s1.MODEL_DUR["TLH"], s1.MODEL_DUR[rung]
    rest = 1 - w_rung
    # w_i*di + (rest-w_i)*dt + w_rung*db = target
    w_i = (rest * dt + w_rung * db - target_model_dur) / (dt - di)
    return {rung: w_rung, "IEF": w_i, "TLH": rest - w_i}


def main():
    print(f"Liability spot PV today ${SPOT_PV:,.0f}; value at 2027-01-01 ${s1.L0:,.0f}")
    print("\n[1] Individual Treasuries (model, 2026-09-25 curve; per $100 face)")
    for n, (c, m, cusip, pay) in BONDS.items():
        dirty = s1.V0[n]
        ai = accrued(c)
        print(f"  {c}% {m} (CUSIP {cusip}, pays for {pay}): dirty {dirty:.2f}, accrued {ai:.2f}, clean {dirty - ai:.2f}, "
              f"yield {ytm(n) * 100:.2f}% (s.a.), model duration {s1.MODEL_DUR[n]:.2f}y; next coupon {NEXT_CPN} "
              f"(after the Nov 6 WInS freeze)")

    base = s1.two_fund("IEF", "TLH")
    target = sum(w * s1.MODEL_DUR[k] for k, w in base.items())
    print(f"\n  S3 ticket hedge (issuer-duration 9.90): IEF {base['IEF'] * 100:.1f}% / TLH {base['TLH'] * 100:.1f}% of the "
          f"hedge; model duration {target:.2f}y (issuer IEF {s1.ISSUER_DUR['IEF'][0]}, TLH {s1.ISSUER_DUR['TLH'][0]}; "
          f"model IEF {s1.MODEL_DUR['IEF']:.2f}, TLH {s1.MODEL_DUR['TLH']:.2f}, IBTM {s1.MODEL_DUR['IBTM']:.2f})")

    print("\n[2]-[4] One rung inside the hedge; weights keep the model duration; tracking vs the ten payments "
          "(S4 forward-consistent method, hedge sized at $292,264)")
    tw0, pa0 = s4.worst(s4.fwd_track(base))
    print(f"  ETF-only (S3 ticket): worst 50bp twist ${tw0:,.0f}; worst +/-100bp ${pa0:,.0f}")
    strip_cost = 37_253  # S3: principal STRIP 912821KC8 cost at 2027-01-01 (model)
    for opt, H, face in (("(iii) literal Jan-2027 book", H3, 50_000),
                         ("(ii) post-2028 mix scaled", H2, round(50_000 * H2 / SPOT_PV, -3))):
        print(f"\n  Option {opt}: hedge ${H:,.0f}; rung face ${face:,.0f}")
        for n in ("T32", "T39", "T40", "IBTM"):
            if n == "IBTM":
                # size so the fund's value grows to about the rung face by mid-Dec 2032 at its YTM 5.03%
                val = face / (1.0503 ** ((date(2032, 12, 15) - s1.VAL).days / 365.25))
                label = f"IBTM ${val:,.0f} (~{val / 21.85:,.0f} sh at $21.85)"
            else:
                val = face * s1.V0[n] / 100
                label = f"{n} ${val:,.0f} incl. accrued ${face * accrued(BONDS[n][0]) / 100:,.0f}"
            w = mix_with_rung(n, val / H, target)
            tw, pa = s4.worst(s4.fwd_track(w))
            tlh_pct = w["TLH"] * H / 300_000 * 100
            ief_pct = w["IEF"] * H / 300_000 * 100
            print(f"    + {label}: rung {val / 300_000 * 100:.1f}% of $300k; IEF {ief_pct:.1f}% / TLH {tlh_pct:.1f}% of "
                  f"$300k; worst twist ${tw:,.0f} ({tw - tw0:+,.0f}); worst +/-100bp ${pa:,.0f} ({pa - pa0:+,.0f})")
        if opt.startswith("(iii)"):
            c = BONDS["T32"][0]
            n_cpn = 13  # Nov 2026 .. Nov 2032 inclusive
            print(f"    T32 face $50,000 pays {n_cpn} coupons of ${50_000 * c / 200:,.2f} (${n_cpn * 50_000 * c / 200:,.0f}) "
                  f"before its $50,000 principal on 2032-11-15; the principal STRIP of the same bond (912821KC8) "
                  f"costs ~${strip_cost:,} and pays only the $50,000")


if __name__ == "__main__":
    main()
