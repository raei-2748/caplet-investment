# Verification of L01 (Top-50 screening judge panel)

Adversarial check, Fri 16 Oct 2026 (Sydney). AI-generated (Claude). Analysis only: no deliverable prose.
Paths without a prefix are in `/home/user/caplet-investment`. `caplet-latest/` = the 16 Oct branch copy (commit 412e9e3).
Web pages were fetched on 16 Oct 2026 with the scratchpad `page.py`. Copies: `oct16/verify/L01w/rules.txt` and `ssir.txt`.
Scripts: `oct16/verify/L01w/gap.py` and `build.py`.

**Result:** 18 findings checked. 7 confirmed, 11 adjusted, 0 refuted, 0 unverifiable. I added 2 findings.
No personal data found in the lens files. No surnames, no WInS username and no fork owner are given.

## The ladder-cost conflict (re-run, and one correction to the lens)

I re-ran `oct16/research/KB_verify/num/reconcile.py` on the 15 Oct row of
`caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`. It reproduced all four figures exactly:

| Where each $50,000 is priced to | Curve basis | Cost on 1 Jan 2027 | Room under $300k |
|---|---|---|---|
| 1 Jan payment dates (the number sheet, `ips_numbers.py:70-89`) | forward | $294,461 | $5,539 (19.0bp) |
| 1 Jan payment dates | today's curve unchanged | $295,246 | $4,754 |
| Holdings' maturities; waiting cash earns the 3-month yield, 4.28% (my run, `gap.py`) | forward | **$295,329** | $4,671 |
| Holdings' maturities; waiting cash earns 0% | forward | $297,847 | $2,153 (7.4bp) |
| Holdings' maturities; waiting cash earns 0% (L03/L05/L08) | today's curve unchanged | $298,628 | $1,372 (4.7bp) |
| results.json `ladder_cost_1jan2027_today_curve` (par yields used as zero rates, `ips_numbers.py:97-103`) | carry | $295,924 | $4,076 (13.4bp) |

**Why they differ.** The curve and the ten amounts are the same in every row. About $3.4k of the gap comes from what the
cash earns after each holding matures and before its 1 January payment. The gaps are 17 days for the iBonds, 10.5 months for
Feb-2037, 7.5 months for May-2038 and about 7 weeks for the Nov bonds. Pricing to the payment dates is the same as
assuming that waiting cash earns market forward rates. The "holdings" figure assumes it earns nothing. About $0.8k comes
from the curve basis (forward against unchanged).

**Correction to the lens.** L01 says only the holdings basis fits Caplet's claims. That is too strong. $298.6k is a
cautious upper bound. It matches the team's own "executable" basis (`ops/routines/MONITOR.md:22`; `COMPETITION.md:153-154`) and the
IBTR note's 0.2-point test. But the notes say waiting cash sits "in a short-term Treasury ETF"
(`team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:16-17`). On that assumption the cost is
about $295.3k.

**Which figure for which claim:**
- "Is $300k enough?" (the IBTR reflection): use the cautious $298.6k and give its date.
- "What the plan costs if waiting cash earns interest": about $295k. Name where that cash waits.
- $294.5k: an idealised figure only.

The sheet's 35% chance of costing more than $300k is anchored to $294,453 (`ips_numbers.py:122`). The sibling lenses'
44-45% on the holdings basis was not re-run here, so it is UNVERIFIED.

## Verdicts

| ID | Verdict | Severity (in → out) | Reason |
|---|---|---|---|
| JUDGE-01 | adjusted | critical → critical | **Verified:** the bar quote ("score exceptionally well on all five components", faqs.txt:79). **Weak:** the 350-700 rank and the 4.2 average are uncalibrated AI opinion. The 15 Oct brief's panel scored the same V5 7/6/5/4/5 (oct14/final.md:440-449), so the scale is not stable. **Changed:** I dropped the rank, set confidence to low, and added the Rules page (16 Oct): the Top 50 is chosen "based on the strength of their Investment Policy Statement (IPS) and Final Reports". |
| JUDGE-02 | adjusted | critical → critical | **Verified:** V5:36, caplet-latest/CLAUDE.md:27-30, deliverables.txt:59, IPS:123-125. **Corrected:** the IPS bans "formal citations" but sends sources to the Final Report (IPS:124-125), so AI use *can* be disclosed later. The real issue is the Rules page: "AI-generated work may not be submitted as your own". Citing does not make AI wording the students' own, and Creativity scores "an authentic team voice". **Note:** the "not generated or generic responses" quote is from the 2025-26 *semifinal* written responses, not the screening round. I re-fetched the PDF. |
| JUDGE-03 | confirmed | high | **Verified in results.json:** gift inside the range 0.9941; payment needs more than Laura kept 0.063; 0.0708 including the leftover. Also checked: number sheet :47-54, suggestion 12, case:91, 119-120. All MODEL. L02, L06 and L08 reach the same point. |
| JUDGE-04 | confirmed | high | **Verified:** all cites. **New evidence:** the journal says the team "kept 'never below the floor' on purpose (STRIPS in real life, IBTM as the WInS stand-in)" (final_report.md:24). The 6 Oct email ended STRIPS, so that reason is gone. Also results.json floor_paid.p5 = $130,738. |
| JUDGE-05 | adjusted | high → medium | **Verified:** "diversif" appears 0 times in V5; the V3 line, the V2 comment and suggestion 8 are as stated. **Overstated:** V5 *does* argue it briefly. It has the one-issuer sentence and "a global index fund of thousands of companies" (V5:24). **Corrected:** the one-issuer share is 92.3%, not 93%. |
| JUDGE-06 | adjusted | high | **Verified:** the counts. **Corrected:** IPS:66 says "You do not need to address these points separately", and V5 covers some themes without naming them (V5:22, 28, 30). The brief asks for an *approach* to "risk and return" (IPS:46). Numeric return assumptions are for the Final Report's projections (case:130-132). **Changed fix:** a return objective in words is enough for the IPS; a number is optional there. |
| JUDGE-07 | adjusted | high → medium | **Refuted part:** the claim of "no source anywhere in the repo" is false. The line traces to stakeholder_map.md:726-727 (BS-17, citing SSIR 2009 at :828) and notes_and_discussions.md:217 (item 17, Kresge). **Still true:** the SSIR article is about overhead in general (re-fetched 16 Oct), so "rarely pay to run it" overstates it, and the IPS cannot cite. The stale $292,000 and the missing cap rule are confirmed. **Severity:** matched to L06 IPS-16 and L02 CLIENT-08. |
| JUDGE-08 | adjusted | high | **Verified:** the figures reproduced exactly, and the code lines check out. **Corrected:** see the section above. The holdings basis is a cautious bound, not the only valid basis. I added $295,329 for waiting cash earning the 3-month yield. The 44-45% figure is UNVERIFIED here. |
| JUDGE-09 | adjusted | high | **Verified:** suggestions 5, 8, 9, 11, 12 and IPS:68-70. **Corrected:** cutting 13 is defensible, because V5:28 already covers rising costs. Suggestion 5 uses the same basis as V5's $292k, so its problem is an unnamed basis, not a wrong one. **Missed:** suggestion 2, which the lens praised, adds a new absolute ("depends only on the US government"). That is false for the five iBond rungs, whose notes say the payout "is not fixed" (05:19-22). |
| JUDGE-10 | confirmed | high | **Verified:** final_report.md:16-27 and CLAUDE.md:40-41, 75. **Caveat:** the 2025-26 lesson is Ray's account, so the year-over-year story fits returning members only. Tell it without criticising named students (L09 INT-20). |
| JUDGE-11 | confirmed | high | **Verified:** the outline is on the superseded plan (lines 5, 13, 15; last commit 29 Sep). 9 Nov to 4 Dec is 25 days. S3_final_report_ladder_and_reserve.md is a STRIPS-era section, not an outline. |
| JUDGE-12 | confirmed | medium | **Verified:** the figures. "About 86%" is a ratio of two medians, not a per-path figure. MODEL. |
| JUDGE-13 | adjusted | medium | **Verified:** the Kresge, notes and strategy-notes lines. **Corrected:** the pitch already uses one strand of this research (notes item 17), in an overstated form. The unused parts are the lead-gift / no-match evidence and the "written pledges or cash" point. I did not re-verify "nearly six times". |
| JUDGE-14 | adjusted | medium | **Verified:** the rows. **Weaker:** row 3 is a gap, not a contradiction. V5:26 covers income until 2033; the 2037-38 proceeds come later, and V5 names no home for them. Row 6 mixes WInS order times with the plan rule. |
| JUDGE-15 | confirmed | medium | **Verified:** five names for the stock fund and three for the floor. "Defined-maturity Treasury ETF" is never explained. |
| JUDGE-16 | confirmed | medium | **Verified:** the 11 fills span about 24.5 hours. TNA:11-13 is quoted correctly. **Note:** TNA:20-23 says no reserve calculations are expected yet, so a dated figure is optional, and it must name its basis if used. |
| JUDGE-17 | adjusted | medium → low | **Verified:** the bond seat and the 2025-26 semifinal case-study and "no new material" rules. **Weak:** the 2026-27 semifinal rules are UNVERIFIED, and this matters only after the Top 50. |
| JUDGE-18 | adjusted | low | **Verified:** 47 / 497 by whitespace. A stricter counter gives 514. **Corrected:** the team name *is* on file in the team's record (COMPETITION.md:117). It still needs checking against the submitted roster. |

## Findings the lens missed (added)

- **JUDGE-V01 (high, new). The lens's own advice breaks the 500-word cap.**
  - The [AI] suggestions add about 59 words and cut about 58, so they only fit as a package.
  - L01 says to reject 8, 9 and 13 and favours 2, 7 and 10. Doing that takes V5 to about 528-542 words.
  - A submission that does not meet the format rules "will not be considered for semifinal selection" (IPS:82-83).
  - L01's other fixes add words too.
  - The suggestions file misstates its own total: "494 after all twelve", but it has 13 rows and the whitespace total is 498.
  - **What the fix must achieve:** a word budget per section with a total of 470 or less (L06 §13 has one).
- **JUDGE-V02 (medium, new). Strategy fixes must reach WInS before the freeze.**
  - The buffer option (JUDGE-03) and a new give/keep split (JUDGE-12) both change the 2028 mix.
  - V5:26 says "Our WInS portfolio shows this allocation, scaled down". The criterion scores "consistency with the team's IPS".
  - WInS freezes on 6 Nov (Guide:172-175).
  - The number sheet says no option "is a WInS trade". That is true for keeping Laura's half to 2042, but not clearly true for a 2028 buffer.
  - **What the fix must achieve:** the vote also decides whether WInS still matches. If not, Ray places a checked trade in good time, or the IPS's WInS sentence is changed.
