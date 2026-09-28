"""S4 red-team checks for research/insight_v1/wins_now/securities_and_allocation_v0.md (agent S3's WInS plan).

PROVISIONAL week-1 research (2026-09-27). Not approved by the team. Every ticker is PENDING APPROVAL CHECK: confirm on
this year's WInS approved list/rules before trading (this season: WInS availability + Session Rules position limit).

What it checks (plain English):
1. The liability's SPOT duration today versus its FORWARD duration at 2027-01-01 (10.16y vs 9.90y), i.e. which
   number a hedge bought today should match.
2. Hedge tracking error measured two ways: S1's method (fund spot return vs liability forward change) and a
   forward-consistent method (fund forward value vs liability forward value). Shows the TLH-over-TLT ranking holds.
3. Where IEF's and TLH's bonds actually mature, compared with Laura's payment dates (share of TLH maturing after the
   last payment on 2042-01-01).
4. Simpler hedges that respect a 25% single-security cap (IEF 24 / TLH 24 / SPTL 18) versus S3's 4-fund variant.
5. Cost of S1's Nov-15 STRIPS ladder under rate falls, and the chance it costs more than $300,000 on 2027-01-01.

Inputs (status labels):
- research/insight_v1/wins_now/S1_hedge_weights.py and its data files (curve: VERIFIED-REPO-FILE treasury.gov CSV row
  09/25/2026; fund holdings snapshot 2026-09-24 and issuer durations: VERIFIED-PRIMARY per S1, iShares/Vanguard,
  downloaded 2026-09-27). Issuer durations IEF 6.86 / TLH 11.59 / TLT 14.88 re-read by S4 on ishares.com
  2026-09-27 12:28 UTC (VERIFIED-PRIMARY).
- ASSUMPTION (same as brief section 14): zero-drift lognormal ladder cost, 2026 realised volatility 7.24% a year,
  horizon 2026-09-25 to 2027-01-01.
- ASSUMPTION: instantaneous parallel/twist shocks as defined in S1; forward-consistent tracking assumes each
  instrument's forward price to 2027-01-01 is spot / DF(2027-01-01) on the shocked curve.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/S4_red_team_checks.py
"""
import csv
import math
import sys
from collections import defaultdict
from datetime import date

from scipy.stats import norm

sys.path.insert(0, "research/insight_v1/wins_now")
import S1_hedge_weights as s1  # noqa: E402

F0 = s1.build(s1.PAR)


def spot_liability(par):
    f = s1.build(par)
    return sum(50_000 * f(s1.yf(d)) for d in s1.PAY)


def fwd_track(w):
    """Hedge forward value change minus liability forward change, hedge sized at the forward value $292,264."""
    out = {}
    for k, fn in s1.SCEN.items():
        p = s1.shifted(fn)
        fp = s1.build(p)
        r = sum(wi * ((s1.fund_value(n, p) / float(fp(s1.TA))) / (s1.V0[n] / float(F0(s1.TA))) - 1)
                for n, wi in w.items())
        out[k] = s1.L0 * r - (s1.L_S[k] - s1.L0)
    return out


def worst(te):
    tw = max(abs(v) for k, v in te.items() if "parallel" not in k)
    pa = max(abs(te["+100bp parallel"]), abs(te["-100bp parallel"]))
    return tw, pa


if __name__ == "__main__":
    # 1. spot vs forward duration
    s0 = spot_liability(s1.PAR)
    ds = (spot_liability(s1.shifted(lambda t: -.01)) - spot_liability(s1.shifted(lambda t: .01))) / (2 * s0 * 1e-4)
    print(f"[1] liability spot PV ${s0:,.0f}, spot duration {ds:.2f}y; forward value at 2027-01-01 ${s1.L0:,.0f}, "
          f"forward duration {s1.LIAB_DUR:.2f}y")

    # 2. tracking error, two methods
    print("\n[2] tracking error ($, hedge minus liability): S1 method vs forward-consistent method")
    mixes = {
        "IEF/TLH weighted to 9.90 (S3 primary)": s1.two_fund("IEF", "TLH"),
        "IEF/TLT weighted to 9.90 (fallback)": s1.two_fund("IEF", "TLT"),
        "SPTI/SPTL weighted to 9.90": s1.two_fund("SPTI", "SPTL"),
    }
    for tgt in (ds, 8.92):
        wt = (tgt - 6.86) / (11.59 - 6.86)
        mixes[f"IEF/TLH weighted to {tgt:.2f}"] = {"IEF": 1 - wt, "TLH": wt}
    H = 66.0
    mixes["cap 25%: IEF 24 / TLH 24 / SPTL 18 (S4 simple fallback)"] = {"IEF": 24 / H, "TLH": 24 / H, "SPTL": 18 / H}
    mixes["cap 25%: IEF 24 / TLH 24 / SPTL 14 / SPTI 4 (S3 D.1b row 2)"] = {"IEF": 24 / H, "TLH": 24 / H,
                                                                          "SPTL": 14 / H, "SPTI": 4 / H}
    mixes["cap 25%: IEF 24 / TLH 24 / TLT 18"] = {"IEF": 24 / H, "TLH": 24 / H, "TLT": 18 / H}
    for name, w in mixes.items():
        iss = sum(wi * s1.ISSUER_DUR[n][0] for n, wi in w.items())
        mod = sum(wi * s1.MODEL_DUR[n] for n, wi in w.items())
        a, b = worst(s1.tracking(w)), worst(fwd_track(w))
        print(f"   {name}: " + ", ".join(f"{n} {v:.1%}" for n, v in w.items())
              + f" | issuer dur {iss:.2f}y, model dur {mod:.2f}y | S1 method: twist ${a[0]:,.0f}, +/-100bp ${a[1]:,.0f}"
              + f" | forward-consistent: twist ${b[0]:,.0f}, +/-100bp ${b[1]:,.0f}")

    # 3. where the bonds mature
    print("\n[3] maturity profile of the hedge funds (S1 holdings snapshot, 2026-09-24; cash rows excluded)")
    rows = defaultdict(list)
    for r in csv.DictReader(open("research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv")):
        if r["maturity"] > "2027-01-01":
            rows[r["fund"]].append(r)
    for f in ("IEF", "TLH", "TLT"):
        mats = sorted(r["maturity"] for r in rows[f])
        tot = sum(float(r["weight_pct"]) for r in rows[f])
        after = sum(float(r["weight_pct"]) for r in rows[f] if r["maturity"] > "2042-01-01")
        by_year = defaultdict(float)
        for r in rows[f]:
            by_year[r["maturity"][:4]] += float(r["weight_pct"])
        print(f"   {f}: {len(mats)} bonds, {mats[0]} to {mats[-1]}; {after / tot:.1%} of bond weight matures after the "
              f"last payment (2042-01-01); by year: " + ", ".join(f"{y} {v:.1f}" for y, v in sorted(by_year.items())))
    pv = {d.year: 50_000 * F0(s1.yf(d)) / F0(s1.TA) for d in s1.PAY}
    print(f"   liability PV share of the 2033-2036 payments: {sum(v for y, v in pv.items() if y <= 2036) / s1.L0:.1%}")

    # 5. ladder cost under rate falls
    print("\n[5] S1's Nov-15 STRIPS ladder: cost at 2027-01-01 under parallel shifts")
    for sh in (0.0, -0.25, -0.5, -1.0):
        f = s1.build(s1.shifted(lambda t, sh=sh: sh))
        c = sum(50_000 * f(s1.yf(date(y - 1, 11, 15))) / f(s1.TA) for y in range(2033, 2043))
        print(f"   {sh * 100:+.0f}bp: ${c:,.0f} ({c - 300_000:+,.0f} vs the $300,000 deposit)")
    T = (date(2027, 1, 1) - date(2026, 9, 25)).days / 365.25
    sd = 0.0724 * math.sqrt(T)
    for c0, lab in ((292_264, "exact-date zeros"), (294_387, "Nov-15 STRIPS ladder")):
        z = math.log(300_000 / c0) / sd
        print(f"   P(cost > $300k on 2027-01-01), {lab}: {1 - norm.cdf(z):.1%} (ASSUMPTION: zero drift, vol 7.24%)")
