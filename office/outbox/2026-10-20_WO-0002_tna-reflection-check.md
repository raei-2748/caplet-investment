# WO-0002: Check of the rewritten TNA reflections (VT, IBTR) + what IBTM is

Asked by: team lead (Ray), 20 Oct 2026. Decides: final TNA text. By: Thu 22 Oct (internal submit).
Source: Google Doc "IPS Report", tab "Trading Note Reflection", read 20 Oct 2026. Checks only: no wording given
(CHARTER; Wharton AI policy says not to use AI for personal reflection).

## Mechanical (`office/tools/textcheck.py --limit 100`)
| Reflection | Words (spaces / strict) | Margin | Non-ASCII | Overclaim words |
|---|---|---|---|---|
| VT (rewritten) | 100 / 99 | 0 | 5 curly apostrophes, 2 en dashes | 0 |
| IBTR (rewritten) | 99 / 99 | 1 | 3 curly quotes | 1: "guarantee" |
| IBTM | no student version yet | | | |

The two spaced en dashes in VT count as words on a by-spaces counter; the SurveyMonkey Apply counter is unknown.

## Content problems
**VT**
1. "set the upper bound for this contribution at half of VT's value" contradicts IPS Version 5 and COMPETITION.md
   section 7: upper bound = floor + half the fund's value (less any expected shortfall). As written, the top of the
   range would be below the floor.
2. "VT's performance will determine Laura's facility contribution" overstates VT's role. The floor (IBTM) sets the
   minimum; VT sets only how far above it the contribution goes (the VT trade note itself says this).
3. "every dollar in stocks is a dollar at risk, unlike our bond investments": the team's own IBTM/IBTO/IBTP notes say
   the fund payouts are "not fixed", and the IPS names a $21,000 reinvestment shortfall risk. Absolute contrast.
4. "reflective of our investment strategy" names no part of the strategy (payments first; the 2028 deposit is
   uncertain, so only money the payments do not need takes market risk: IPS V5 para 2).
5. Integrity: the rewrite follows the [AI] version's facts in the same order (167 shares, 10,000 companies, 0.06%,
   small by design / dollar at risk, no stock picking, half to the range, Laura keeps the rest). Own voice is required.

**IBTR**
1. "ironclad guarantee": the team's rule (COMPETITION.md s7, TNA gate) is never "guaranteed". IBTR is a fund whose
   payout is not fixed (team notes), and the IPS names residual risks. Conflicts with the IPS.
2. "the safest financial asset in the world": unsourced superlative. The IPS says "least credit risk of any dollar asset".
3. Never says which payment IBTR funds (1 Jan 2037, per the note) or why this trade; it describes the whole ladder.
   "iBonds ... which will fund Laura's 10 annual payments": iBonds fund payments 1-5; T-bonds fund 6-10.
4. Good: "operating commitment" and "high degree of certainty" are the case's exact words (Client Profile). The last
   sentence matches the note and the IPS.

## IBTM in plain English (knowledge, for the students to explain in their own words)
- iShares iBonds Dec 2032 Term Treasury ETF. A fund that holds US Treasuries maturing in 2032. In December 2032 it
  closes and pays holders cash, so it behaves like one bond with a 2032 maturity. Unlike a single bond, the cash is
  not fixed in advance (many bonds, reinvestment of early maturities in the final year, fees).
- Why it: the first payment is due 1 Jan 2033. WInS lists no individual Treasury maturing Feb 2031 to Feb 2036, and
  the 6 Oct Wharton email limits Laura's real plan to WInS securities, so STRIPS are out (COMPETITION.md s6).
- Two jobs: (a) from the 2027 deposit, it funds the 1 Jan 2033 payment; (b) in the real plan the 2028 deposit buys
  more IBTM as the floor, sized to return about $150k by 2033. That is the minimum Laura quotes co-sponsors in 2031,
  rounded down because the payout is not fixed. WInS holding: 4,503 sh at $21.65 = $97,490 ("2033 payment + 2028
  floor stand-in").
- What "teaches": a term fund trades the certainty of one exact bond for availability. Rounding the quoted floor down
  is the price of that.
- If no one can defend IBTM in their own words by Thu 22 Oct, the documented runner-up is the Feb-2037 bond.
  The IPS relies on IBTM either way (the "Treasury fund maturing in December 2032").

Before pasting: delete the [AI] versions; replace curly quotes only if the paste check shows a problem; record the
AI use (WO-0002 and the [AI] drafts) for the Works Cited.

## Follow-up (20 Oct): fix sheet, content only
Ray asked for rewritten reflections. Declined: CLAUDE.md and CHARTER say never write or rewrite submitted text,
even if asked, and the Wharton AI policy page says not to use AI for personal reflection. Given instead: the three
required points, with the facts each reflection still needs and where each fact comes from.

Instructions: the official PDF (`2026_WGY_Trading_Notes_Analysis-FINAL.txt`:46-52) says "client's goals, funding
needs, or risk considerations". The Doc's Instructions tab says "goals, objectives, or constraints" and has an extra
"Important" paragraph, source unknown. Before submitting, check which wording the form shows and cover both.

| Required point | VT: facts still missing or wrong | IBTR: facts still missing or wrong |
|---|---|---|
| Why | OK (about 10,000 stocks, 0.06%, no stock picking) | Missing: it funds the 1 Jan 2037 payment (5th); WInS has no single Treasury maturing Feb 2031 to Feb 2036 |
| Strategy fit | Missing: payments, then floor, then growth (IPS V5); VT about 9% (167 sh x $158.83 = $26.5k of about $301.9k); real plan buys it Jan 2028 with what is left after the ladder gap and floor; untouched to 2033 | Missing: ladder bought from 2042 backwards (longest first, most rate-sensitive, IPS V5); held to maturity |
| Client | Wrong: top of range = floor + half the fund (not half). Missing: 2028 deposit depends on her publishing/speaking income, so only spare money takes stock risk; other half stays hers ("flexibility", case) | Remove "guarantee" and "safest asset in the world". Name the residual risks (payout not fixed; US default). Optional: the note's 0.2pp test; any "since then" number needs a dated ladder-pricer run |
