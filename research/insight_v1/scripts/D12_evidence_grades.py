"""D12 (Overflow Researcher, client side), question M231: grade each key number by the kind of evidence behind it.

What it does
1. Counts the grades in Laura's own published "Match Quality" column (Rewriting Herstory page) as the precedent.
2. Lists the key numbers the team may use in the Trading Notes (TN) or the IPS, gives each one an evidence grade, and
   records which claim rests on it (the ten-payment promise, or the facility/growth outcome).
3. Prints which grades the promise rests on and which the facility outcome rests on, and names every input to the
   promise that is NOT yet observed. That list is what the IPS must cover with a rule instead of a number.

Grades (ASSUMPTION: D12's scheme, three grades to mirror her three-level column without copying its words):
  PRICED   = read today from a market price or an official file, or plain arithmetic on such prices
  HISTORY  = estimated from past data (a statistic that could be different next time)
  ASSUMED  = a forecast, a model output or a choice the team makes
  CASE     = given by the official case (not evidence; the problem itself)

Inputs and status labels
- Laura's column: https://lauragao.com/rewriting-herstory, read 2026-09-28 by D12 (VERIFIED-PRIMARY); counts below were
  taken from that read (14 rows). Undated, student-era page (ASSUMPTION from "Wharton freshman" wording on the page).
- Every number in REGISTER carries the status label of its source (brief sections 6 and 14; wins_now ticket;
  research/verified_2026-09-27/*.py).

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D12_evidence_grades.py
"""
from collections import Counter

herstory = {"Good": 6, "Unsure": 5, "Bad": 3}  # VERIFIED-PRIMARY count, D12 read 2026-09-28
n = sum(herstory.values())
print("== 1. Laura's 'Match Quality' column (Rewriting Herstory) ==")
for k, v in herstory.items():
    print(f"  {k:6s} {v:2d} of {n} ({v / n:.0%})")
print(f"  Not 'Good': {n - herstory['Good']} of {n} ({(n - herstory['Good']) / n:.0%}); she published them anyway "
      "under 'The [unfinished] results are below.'")

# (label, value, grade, rests_on, may_appear_in, status/source)
REGISTER = [
    ("Ten payments, 2033-2042", "$50,000 each, fixed", "CASE", "promise", "TN, IPS", "VERIFIED-REPO-FILE case p.2-3"),
    ("Deposits", "$300k 2027 + $150k 2028", "CASE", "both", "IPS", "VERIFIED-REPO-FILE case p.2"),
    ("Treasury par curve 2026-09-25", "10y 5.17%", "PRICED", "promise", "none (input)", "VERIFIED-REPO-FILE treasury.gov CSV"),
    ("Cost to lock the ten payments (value at 2027-01-01)", "$292,264 (~$292k)", "PRICED", "promise", "TN (one number)",
     "VERIFIED official_curve_pv.py"),
    ("Sensitivity of the payments' value", "about 10 years ($289 per bp)", "PRICED", "promise", "TN",
     "VERIFIED official_curve_pv.py"),
    ("Hedge fund durations", "IEF 6.86y / TLH 11.59y", "PRICED", "promise (WInS stand-in)", "none (say 'about 10 years')",
     "VERIFIED-PRIMARY iShares 2026-09-24"),
    ("Price of the ladder in January 2027", "not yet known", "ASSUMED", "promise", "IPS (as a rule, not a number)",
     "unobservable until the trade date"),
    ("P(ladder costs > $300k on 2027-01-01)", "~24% (range 23-38%)", "ASSUMED", "promise", "none (internal)",
     "ASSUMPTION zero-drift lognormal, brief s14"),
    ("2026 realised rate volatility", "7.24%/yr (4.45bp/day on the 10y)", "HISTORY", "promise (timing risk)", "none",
     "VERIFIED-PRIMARY data, D7/brief s14"),
    ("Days in 2026 when the ladder cost more than $300k", "173 of 185", "PRICED", "promise (timing risk)",
     "IPS (in words: 'most of this year')", "VERIFIED brief s14"),
    ("U.S. Treasury pays in full", "residual risk", "ASSUMED", "promise", "IPS", "ASSUMPTION stated as the one residual risk"),
    ("2028 deposit arrives in full and on time", "$150k", "ASSUMED", "facility (+ promise if Jan 2027 price > $300k)",
     "IPS", "CASE gives the amount; arrival is ASSUMED"),
    ("World equity long-run return", "7.00% compound (AC World)", "ASSUMED", "facility", "IPS (in words only)",
     "VERIFIED-REPO-FILE JPM 2026 LTCMA (a forecast)"),
    ("Equity share of the growth money", "60% (provisional)", "ASSUMED", "facility", "TN, IPS", "ASSUMPTION team choice pending"),
    ("2033 surplus p5/p50/p95", "$159k/$207k/$273k", "ASSUMED", "facility", "none before FR", "model output strategy_mc.py"),
    ("Taiwan CPI Aug 2026", "+2.04% y/y", "HISTORY", "facility (real value)", "IPS (in words)", "VERIFIED-PRIMARY brief s14"),
    ("Taiwan construction costs since 2021", "~3.5%/yr", "HISTORY", "facility (real value)", "IPS (in words)",
     "VERIFIED-PRIMARY brief s14"),
    ("USD/TWD volatility", "4.0-5.6%/yr", "HISTORY", "facility and payments' TWD value", "IPS (in words)",
     "VERIFIED-PRIMARY brief s14 (FRED)"),
    ("Fund costs", "0.03-0.15%/yr", "PRICED", "both", "none", "VERIFIED-PRIMARY issuer pages, ticket s1"),
]

print("\n== 2. Register ==")
print(f"  {'grade':8s} {'rests on':32s} {'may appear in':32s} label = value")
for label, value, grade, rests, where, src in REGISTER:
    print(f"  {grade:8s} {rests:32s} {where:32s} {label} = {value}   [{src}]")

print("\n== 3. What each claim rests on ==")
for claim in ("promise", "facility"):
    rows = [r for r in REGISTER if r[3].startswith(claim) or r[3] == "both" or (claim == "promise" and "promise" in r[3])]
    c = Counter(r[2] for r in rows)
    print(f"  {claim}: {dict(c)}")
    if claim == "promise":
        print("  Non-observed inputs the promise still depends on (need a RULE in the IPS, not a number):")
        for r in rows:
            if r[2] == "ASSUMED":
                print(f"    - {r[0]} ({r[1]})")

print("\n== 4. Numbers that could go into the 50-word pitch + 500-word IPS without a forecast ==")
safe = [r for r in REGISTER if r[2] in ("CASE", "PRICED") and "IPS" in r[4]]
for r in safe:
    print(f"  {r[0]} = {r[1]}")
print(f"  ({len(safe)} of {len(REGISTER)} register rows; everything else needs words such as 'we assume' or "
      "'history suggests')")
