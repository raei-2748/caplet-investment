"""D12 (Overflow Researcher, client side), question M247: can three Trading Notes show distinct official roles?

What it computes
1. Length of Wharton's own example Trading Note (words, characters) against the 300-character Trade Note limit that
   Stock-Trak's HowTheMarketWorks product states, and a character budget for the team's notes.
2. Which of the Guide's four role words (growth, liquidity, risk management, future funding) each WInS book option can
   honestly support.
3. A "role test": how each planned position moves in two plain shocks (rates +1 percentage point; world stocks -20%),
   next to how the value of Laura's ten payments moves. Distinct roles should show up as distinct behaviour.
4. U.S. trading days left for a note-trade to be placed and filled before the Oct 23 deadline.

Inputs and status labels
- Example note text: competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt lines 36-39
  (VERIFIED-REPO-FILE).
- 300 characters: https://www.howthemarketworks.com/updates/trade-notes-justify-trades/ ("we allow up to 300
  characters"), a Stock-Trak, Inc. property, read 2026-09-28 (VERIFIED-PRIMARY for that product; UNVERIFIED for the
  2026-27 WInS session: WInS runs on edu.stocktrak.com but no WInS page states a limit).
- Role words: 2026_WGY_Investment_Competition_Guide.txt lines 84-86 (VERIFIED-REPO-FILE).
- Weights (option ii: IEF 23.6 / TLH 42.4 / VT 20.5 / VGSH 12.5 / cash 1; option iii: IEF 35.0 / TLH 63.0 / cash 2):
  research/insight_v1/wins_now/securities_and_allocation_v0.md (provisional ticket; ASSUMPTION = team not yet decided).
- Durations: IEF 6.86y, TLH 11.59y (iShares, as of 2026-09-24), VGSH 1.9y (Vanguard, as of 2026-08-31); spot duration
  of the ten payments 10.16y (brief section 14). VERIFIED-PRIMARY via the S3 ticket / brief.
- Equity shock: VT assumed to fall 20% (ASSUMPTION: an illustrative bad year, a bit over one JPM AC World volatility,
  16.78%); Treasury funds assumed unchanged in the equity shock (ASSUMPTION; JPM correlation about 0).
- First-order duration arithmetic only (ASSUMPTION: no convexity), enough for a plain-English role test.

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D12_note_roles.py
"""
from datetime import date, timedelta

EXAMPLE_NOTE = (
    "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin "
    "preparing for Laura’s future operating commitment. The position provides income and greater stability than "
    "equities, although interest-rate changes may affect its value. This trade supports our plan to balance continued "
    "growth with reliable future cash flows as the residency funding date approaches."
)
LIMIT = 300
BOOK = 300_000

print("== 1. Note length ==")
words = len(EXAMPLE_NOTE.split())
chars = len(EXAMPLE_NOTE)
print(f"Wharton example note: {words} words, {chars} characters (limit to plan for: {LIMIT})")
cpw = chars / words
print(f"Characters per word incl. spaces: {cpw:.2f} -> {LIMIT} chars is about {LIMIT / cpw:.0f} words")
# where would a 300-character cut fall?
cut = EXAMPLE_NOTE[:LIMIT]
print(f"The example cut at {LIMIT} chars ends: ...{cut[-60:]!r}")
print(f"Share of the example that would not fit: {1 - LIMIT / chars:.0%}")

print("\n== 2. Role words the example itself uses ==")
role_hits = {
    "risk management (\"reduce portfolio volatility\", \"greater stability\")": True,
    "future funding (\"future operating commitment\", \"reliable future cash flows\")": True,
    "growth (\"balance continued growth\" as the plan, not this trade)": True,
    "liquidity": "liquid" in EXAMPLE_NOTE.lower(),
}
for k, v in role_hits.items():
    print(f"  {k}: {v}")

print("\n== 3. Role test: position moves in two shocks (first-order) ==")
dur = {"IEF": 6.86, "TLH": 11.59, "VGSH": 1.9, "VT": 0.0, "cash": 0.0}
eq_shock = {"IEF": 0.0, "TLH": 0.0, "VGSH": 0.0, "VT": -0.20, "cash": 0.0}
PAY_DUR = 10.16
options = {
    "(ii) post-2028 mix": {"IEF": 23.6, "TLH": 42.4, "VT": 20.5, "VGSH": 12.5, "cash": 1.0},
    "(iii) literal Jan-2027 book": {"IEF": 35.0, "TLH": 63.0, "VT": 0.0, "VGSH": 0.0, "cash": 2.0},
}
role_of = {"IEF": "future funding", "TLH": "future funding", "VT": "growth", "VGSH": "liquidity", "cash": "liquidity"}
for name, w in options.items():
    print(f"\n{name}")
    print(f"  {'pos':5s} {'weight':>7s} {'$':>9s} {'rates+1pp %':>12s} {'rates+1pp $':>12s} {'stocks-20% $':>13s}  role")
    tot_r = tot_e = 0.0
    for k, wt in w.items():
        if wt == 0:
            continue
        d = BOOK * wt / 100
        r = -dur[k] * 0.01 + 0.0
        tot_r += d * r
        tot_e += d * eq_shock[k]
        print(f"  {k:5s} {wt:6.1f}% {d:9,.0f} {r:12.1%} {d * r:12,.0f} {d * eq_shock[k]:13,.0f}  {role_of[k]}")
    hedge = BOOK * (w["IEF"] + w["TLH"]) / 100
    hedge_dur = (w["IEF"] * dur["IEF"] + w["TLH"] * dur["TLH"]) / (w["IEF"] + w["TLH"])
    roles = sorted({role_of[k] for k, wt in w.items() if wt > 0})
    print(f"  book: rates+1pp {tot_r:,.0f} ({tot_r / BOOK:.1%}); stocks-20% {tot_e:,.0f} ({tot_e / BOOK:.1%})")
    print(f"  hedge ${hedge:,.0f}, issuer duration {hedge_dur:.2f}y vs payments {PAY_DUR}y "
          f"(payments' value moves about {-PAY_DUR:.1f}% per +1pp)")
    print(f"  distinct role words available from positions: {roles} ({len(roles)} of 4)")
    free = BOOK * (w["VT"] + w["VGSH"]) / 100
    if free:
        vt = BOOK * w["VT"] / 100
        print(f"  growth money (VT+VGSH) ${free:,.0f}: stocks-20% costs {vt * 0.20 / free:.1%} of it "
              f"(vs 20.0% if it were all VT) -> VGSH's job is risk management of the facility money")

print("\n== 4. Time left for a note-trade ==")
today = date(2026, 9, 28)
deadline = date(2026, 10, 23)
holidays = set()  # Columbus Day Oct 12: NYSE open (bond market closed) -> counts as an ETF trading day (ASSUMPTION)
d, n = today, 0
while d < deadline:  # trades must be filled before the day the analysis is due
    if d.weekday() < 5 and d not in holidays:
        n += 1
    d += timedelta(days=1)
print(f"U.S. weekdays from Mon {today} to Thu {deadline - timedelta(days=1)} inclusive: {n}")
last_safe = date(2026, 10, 16)
d, m = today, 0
while d <= last_safe:
    if d.weekday() < 5:
        m += 1
    d += timedelta(days=1)
print(f"...of which up to Fri {last_safe} (leaves a week to write reflections): {m}")
