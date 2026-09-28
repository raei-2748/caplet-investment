# Executive summary

**Team Caplet · Wharton Global High School Investment Competition 2026-27 · client: Laura Gao**
Research run 27-28 September 2026. **Serves:** the Trading Notes Analysis (due 5 p.m. ET Fri 23 Oct = 8 a.m. AEDT
Sat 24 Oct) and the Investment Policy Statement (due 5 p.m. ET Fri 6 Nov = 9 a.m. AEDT Sat 7 Nov; trading ends and the
strategy freezes). Nothing here is for the Final Report or the finale.

> **AI-use statement.** Everything in this record was produced by an AI assistant (Claude Code) as research and
> brainstorming for the six students. None of it is text to submit. The team decides and writes every word. Wharton's
> AI policy requires any AI use to be recorded in the Works Cited pages.

## 1. The answer in one page

**The recommended strategy** (pending the team's vote; full specification in Part 2):
1. **January 2027:** the first $300,000 buys ten U.S. Treasury bonds, one maturing just before each $50,000 payment
   (2033-2042). This happens before any money takes stock-market risk. If falling rates make the ladder cost more than
   $300,000, the latest payments are bought first, and the 2028 deposit completes the rest.
2. **January 2028:** the $150,000 deposit first finishes any unbought payment. It then buys a Treasury that repays
   $150,000 just before 2033. That is the bought floor of the range Laura can tell co-sponsors. The rest (about $40,000)
   goes into one world stock fund, untouched until 2033.
3. **2031:** nothing is traded. Laura tells co-sponsors a range: the floor she already owns, up to the floor plus half
   of what the stock fund is worth that day.
4. **2033:** the ten bonds become the operating reserve. The facility gets the floor plus half the stock fund, never
   more than the announced top. The rest stays with Laura as flexibility.

**Why it is better than the earlier plan** (lock the growth money in 2031): about the same middle outcome ($207k vs
$210k total facility-plus-flexibility money), better bad cases ($182k vs $168k at the 5th percentile), and across
every six-year window of U.S. market history since 1928, a worst case of $169k vs $120k (model and history estimates;
`scripts/E6_final_checks.py`). The price: less stock (about 9% of her money in 2028-2032) and a smaller median gift.

**Why Laura would choose us (blind contest, a simulation):** three independent simulated-Laura evaluators, grounded
only in the case and her verified public words, each read six anonymised strategies (ours and five rival approaches)
in a different order. **All three ranked ours first** (Borda score 18 of 18; next best 15). They cited that the 2031
bottom is money she already owns, so she cannot overpromise; that the payments do not depend on markets (rival plans
miss a payment in up to 3.2% of model runs, 41-46% if the 2028 deposit never arrives, and that deposit comes from
income she herself called "unstable"); and that the plan names its own costs. **All three asked for one fix:** show
"appropriate balance" more visibly (the plan reads as timid), say where the leap is (the residency itself), and price
the certainty in one line.

**Before the first WInS order:** three recorded team votes (adopt lock-early; recommended design or the 2031-lock
alternative; which book WInS shows), a screenshot of WInS Session Rules (position limit), a zero-risk test of the
note-box length, and every ticker checked as listed in WInS. Target fills by Fri 2 Oct (U.S. time); hard stop 9 Oct.

## 2. Discoveries that changed the plan

- **This year's WInS rules are public** (SMApply Trading Details and FAQ): $300,000 starting cash (exactly Laura's
  2027 deposit; the $150,000 is not added), 200-trade cap, any ETF or U.S. Treasury bond listed in WInS, no sector
  minimum, no day trading, trade notes cannot be edited. A per-security position limit exists but is shown only when
  logged in.
- **The $300,000 fit is knife-edge.** The ten-payment ladder cost more than $300,000 on 173 of 185 trading days of
  2026. The real ladder (Treasury STRIPS maturing each 15 November) costs $294,387, leaving only $5,613 (0.19
  percentage points of rate) of headroom. In about 1 in 3 modelled rate paths it costs more by January 2027, so the
  rule for that case matters.
- **Two official 2026-27 documents were missing** from the repo (the Investment Competition Guide and Infographic).
  They are now filed. The Guide says judges want "the reasoning, assumptions, and tradeoffs behind those decisions."
- **Laura's words, verified.** 91 of her public quotes were confirmed word for word and in context; 7 were excluded
  for privacy. The case's pull quote ("The only person who needs to believe in something is yourself.") cannot be
  verified as hers, so cite it as the case's words. A popular reading (she "only leapt once a contract secured a
  floor") comes from a reporter, not from her, and was dropped. No Laura quotes go into the Trading Notes or the IPS.
- **The real field is smaller than 6,000.** In 2025-26, 6,300+ teams registered but about 2,300 submitted final
  reports.

## 3. How the run worked (about 90 agent runs, every step audited)

| Phase | What happened | Output in this record |
|---|---|---|
| A. Foundations | Official documents catalogued (324 entries), every number traced to a source, stakeholders mapped, WInS rules found | Part 3, Phase A |
| WInS week 1 | Fund research, allocation, red team, revision; later v1 with both book options | Part 3, WInS |
| B. Questions | 20 agents, 10 lenses (incl. client synthesis and a contrarian lens): 472 questions, 271 quotes | Part 3, Phase B |
| C. Filter | Merged to 248; three skeptics per question; 48 survived (so-what, anchor, 2-of-3, simplicity) | Part 3, Phase C; Appendix B |
| D. Research | 12 specialists (with Python models), 5 audits, quote verification (91 Laura quotes verified) | Part 3, Phase D |
| E. Strategy | Architect, 4 red teams (judge, Laura, rival, pre-mortem), chief strategist | Part 2; Part 3, Phase E |
| Contest | Blind Laura's Choice: 6 anonymised strategies, 3 evaluators | Part 2 |
| Outputs | 3 writers, 1 verifier (19 problems found, 18 fixed) | Part 1; Part 3, verification |

## 4. How to read this record

- **Part 1** holds the six working documents for the team, and is all most students need. Start with the
  *Trading Notes pack* (due first), then the *IPS specification*.
- **Part 2** holds the final strategy specification and the blind contest (the reasoning behind Part 1).
- **Part 3** is the full research record, phase by phase, for anyone who wants to check a claim or learn the method.
  Every claim carries a status label: VERIFIED-PRIMARY (checked on the original page), VERIFIED-REPO-FILE (from an
  official file in the repo), SNIPPET-UNVERIFIED, ASSUMPTION or MODEL (a model estimate, not a forecast),
  PARAPHRASE-UNVERIFIED.
- **Appendices:** the brief every agent worked from, the 48 surviving questions, and the index of all Python scripts
  (every model number can be re-run from the repo).
- Later files override earlier ones. Where a specialist file ends with "Audit corrections", the corrections win.

## What this teaches
A long research effort is only useful if its conclusions fit on one page and every number can be traced back. The
work behind this plan was large; the plan itself is simple: buy the promises when the money arrives, let the rest
grow, and never tell anyone a number you do not already own.
