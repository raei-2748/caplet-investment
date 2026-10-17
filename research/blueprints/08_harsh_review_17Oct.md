# Harsh review of the IPS and Trading Notes (17 Oct 2026)

AI-generated review (Claude Code). Reviewed: the IPS as accepted in the Doc (v8) and the three reflections (v7/v8).
Each item says what is wrong and what v9 (now in the Doc as suggestions) does about it. Items marked **OPEN** are not
fixed by wording; they need analysis or a team decision.

## A. Tone (why v8 read as casual)
"finishes the job", "does the growing", "not the place for them", "Why half? It is a judgement.", "a crash", "runs
down to nothing", "if the gap opens", "far payments swing most with rates", "the bonds WInS actually lists". v9 uses
the IPS register of the CFA guide and university IPSs: objectives, return requirement, capacity and willingness,
allocation, monitoring, risks; "primary/secondary objective", "lower/upper bound", "expense ratio", "modelled cost".

## B. Mistakes and regressions in v8
| # | Flaw | Why it costs marks | v9 |
|---|---|---|---|
| 1 | Certainty defined without the reinvestment caveat, then a $21,000 reinvestment shortfall two paragraphs later | Definition contradicts its own test (fixed in v3, lost in v8) | "with any reinvestment shortfall covered by her other assets" |
| 2 | No return requirement | CFA s3b: state the return requirement; judges' Portfolio Analysis criterion | "about 5.1% on the 2027 deposit, which Treasuries currently provide with little margin" (5.09% required vs 5.15% locked on the 16 Oct curve; it was 5.36% on 6 Oct) |
| 3 | Capacity vs willingness never named | Standard IPS vocabulary; judges trained on it | Named explicitly |
| 4 | Inflation and the Taiwan dollar dropped | The case asks teams to state inflation's effect on facility costs | Restored in one line |
| 5 | Ordering rule had no reason ("starting with 2042") | Principles, not steps, are what the IPS is for | "the most rate-sensitive payment" |
| 6 | No rebalancing policy stated | CFA s4c | "remains invested without rebalancing until 2033" |
| 7 | "In our tests" with no method | Vague evidence reads as unsupported | "Our simulations ... market paths" |
| 8 | "Every January we check" mixed with "we will" elsewhere | Inconsistent policy voice | "we will" throughout |
| 9 | VT "about 9% of our portfolio" | Ambiguous: 8.8% of WInS, about 7.6% of Laura's post-2028 plan | "of our WInS portfolio" |
| 10 | Pitch had no credibility idea | The case's central test is a credible 2031 range | "within a range she can credibly announce" |

## C. Flaws that wording cannot fix (OPEN)
1. **The margin is almost gone.** The ladder needs 5.09% a year and the curve gives 5.15%; headroom $1,913 on 16 Oct
   (`research/range_2031/`). A 0.5-point fall costs about $13k of floor. The policy handles it, but the team must be
   ready for a judge asking "what if yields fall before January?" Re-price weekly to 6 Nov.
2. **The equity share looks timid.** Under one tenth in stocks for a client "willing to take thoughtful risks". The
   IPS asserts the trade-off but shows no comparison. Strongest evidence available: the growth-first plan missed a
   payment in about 3% of paths (`research/verified_2026-09-27/strategy_mc.py`, 27 Sep, STRIPS-era inputs). Re-run on
   the WInS-only basis before quoting it anywhere.
3. **"Half" is weakly justified.** The earlier rule test gave 0.47 (`rab/decisions/D6_cap_share.md`). The IPS calls it
   a judgement; the Final Report must show why 0.4 or 0.6 is not better.
4. **The $21,000 test is dated.** It was computed on 28 Sep for a ladder sized dollar for dollar (`rab/numbers.yaml`
   reinvest.bookL_delivered). Re-run on the actual holdings and the 16 Oct curve.
5. **The floor is nominal.** At 2.5% inflation it buys about 12% less in 2033 than in 2028. Not in the IPS (no room);
   it must be in the Final Report.
6. **The 2027 leftover is unassigned.** About $1,900 today. It is not in v9; the Final Report must say where it goes.
7. **Bonds that mature early** (Feb 2037, May 2038) leave cash idle for 10.5 and 7.5 months. Covered by "reinvestment
   risk" only implicitly.

## D. Trading Notes risks
1. **IBTR's 0.3 to 0.2 story must be confirmed.** The figures match (0.3 = idealised $292k ladder in V2/V3; 0.2 =
   WInS-listed $293k ladder), but if the team changed it for another reason, the reflection states something false.
2. **IBTM "the zero-coupon Treasury we had planned"**: confirm this was the team's plan, not only an AI proposal.
3. **Re-price IBTR's $292,000 and $298,000** on the day of submission and keep "modelled".
4. All three notes must be pasted from WInS itself; the third table still needs the IBTM note.

## E. Compliance
v9: pitch 46 words, IPS 492 (496 split), reflections 91-97; no colons; no tickers in the IPS. The live "[AI]" label
in the Version 5 tab must be deleted before export. All other format checks: `06_ips_wharton_compliance_17Oct.md`.
