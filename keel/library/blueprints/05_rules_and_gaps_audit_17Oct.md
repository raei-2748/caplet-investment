# Rules and gaps audit: IPS exemplar and TNA reflections (17 Oct 2026)

AI-generated review (Claude Code) for Team Caplet. Checks the 17 Oct combined exemplar (`04_exemplar_ips_tna_17Oct.md`,
also in the IPS Report Doc as suggestions) against the official materials. The test for every line: is it **true, clear,
required, and confident without overclaiming?** Fixes are in the revised exemplar (same file, "v3").

Sources: IPS instructions (`2026_WGY_Investment_Policy-FINAL.txt`), TNA instructions
(`2026_WGY_Trading_Notes_Analysis-FINAL.txt`), client case (`Laura_Gao_2026_Client_Profile.txt`), judging criteria
(`smapply_public_2026-10-14/deliverables.txt:54-59`), 6 Oct Wharton email (competition/COMPETITION.md s4).

## 1. Rules: pass

| Rule | Status |
|---|---|
| Pitch 50 words or fewer; IPS 500 or fewer | v3: pitch 45 (47 with hyphens split); IPS 489 (494) |
| No charts, links, footnotes or citations | none (the 7% assumption names no source; cite JPM in the Final Report) |
| Strategy only, no detailed calculations or individual securities | two figures only ($21,000 test, 7% assumption); funds described by type, not ticker |
| IPS not expected to give the final range, reserve size, projections or co-sponsor text | none given; range is a rule, not a number |
| Only WInS-listed instruments in Laura's plan (6 Oct email) | Treasury bonds, defined-maturity Treasury funds, one global stock fund: all WInS-listed |
| No promise of WInS action (trading freezes 6 Nov) | none |
| WInS gains not added to projections | none used |
| TNA: 3 notes from executed trades, quoted exactly, 100 words or fewer each | reflections 90-96 words; the third Doc table still held a duplicate IBTR note (suggested swap to IBTM, 10/06/2026 10:01:41 PM; paste it from WInS itself) |

Still to check on the exported PDF: Times New Roman 12, double spacing, 1" margins, pitch + IPS on pages 2-3 only,
title page names exactly as on the roster. Non-compliant submissions are excluded from semifinal selection.

## 2. Gaps and mistakes caught in the 17 Oct combined version (all fixed in v3)

| # | Severity | What was wrong | Why it costs marks | Fix in v3 |
|---|---|---|---|---|
| 1 | **High** | The operating reserve over 2033-42 was gone (dropped when the hold paragraph was merged) | The IPS must "establish your strategic approach to ... managing the operating reserve's asset composition over time" (IPS p.2) | One sentence: the payment Treasuries become the reserve, each maturing before its payment, so it runs down by 2042 without sales |
| 2 | **High** | The 2031 range never subtracted an expected payment shortfall | "The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment" (case p.3) | Top = floor + half the fund, less any expected shortfall Laura's half cannot cover |
| 3 | **High** | The 2027 leftover was both put into the stock fund and named as the *first* cover for a shortfall | Internal contradiction; a judge who reads twice sees the same dollars used twice | Leftover dropped from the cover order; cover order is Laura's half, then the gift above the floor, then the floor |
| 4 | **High** | Certainty was defined as "not by future market returns", but the same IPS shows a $21,000 reinvestment gap | Definition contradicted by its own test; Portfolio Analysis rewards a definition that survives its test | "Each payment matched at purchase by Treasuries maturing shortly before it, with any reinvestment gap covered by her other holdings" |
| 5 | Medium | No principle for how the stock share changes as 2033 approaches | IPS p.1-2: "how will the allocation and composition change as future funding needs approach" | "We do not shift it into bonds, because the floor already protects the bottom of her gift" |
| 6 | Medium | "Holdings are kept to maturity" also covered the stock fund, which has no maturity and is half sold in 2033 | Ambiguous | Treasuries held to maturity; stock fund untouched until 2033 |
| 7 | Medium | "Root-and-Branch" named in the pitch but never explained in the IPS | A name with no meaning reads as decoration (lesson from 2025-26: packaging over insight) | "Our roots are Treasuries" / "the rest is the branch" |
| 8 | Medium | "one tenth stocks" | Overstates: on the 16 Oct curve stocks are about 8% of the 2028 portfolio (model: ~$35k of ~$461k) | "under a tenth" |
| 9 | Medium | "so the gift is designed to stay inside the range" | Hedged ("designed to") where the mechanism is certain; sounds defensive | "lands inside the range unless the payments need the floor itself": confident, with the one real condition |
| 10 | Medium | "a missed payment would let down the residency's artists" | Team inference presented as fact | Case-grounded: "the residency needs reliable operating support" (case p.3) |
| 11 | Low | "iBonds Treasury funds, which end like a bond" | Brand name plus a vague simile | "defined-maturity Treasury funds" |
| 12 | Low | Diversification shown only as "one global index fund" | Criterion: "uses appropriate diversification" | "of thousands of companies" |
| 13 | Low | January review had no trigger | A review with no rule is not a policy | "act only if a payment is no longer covered" |
| 14 | Low | The case's word "flexibility" never appeared | The case asks for "financial flexibility" five times | "The other half stays with Laura as financial flexibility" |
| 15 | Low | Pitch: "More Treasuries set her minimum" (fine) but no link to the credible range | The pitch must say how the strategy serves her goals | "growing the gift within a range she can keep" |

## 3. TNA reflections

| Reflection | Check | Change |
|---|---|---|
| IBTM | "WInS lists no individual Treasury maturing between 2031 and 2036" was looser than the verified fact | "no individual Treasury maturing in 2032" (exactly the gap IBTM fills) |
| IBTR | "longest-dated first" is verifiable from the order times (Nov-2041 at 7:55 PM, Nov-2040 at 7:59 PM, then IBTQ, IBTP, IBTO, IBTM); numbers are dated model values | No change. **Re-price the $298,000 on the day you submit** and keep "model" in the sentence |
| VT | "one tenth" and "cushion" | "under a tenth"; "flexibility" (same word as the IPS); explains it as the branch |

## 4. Still open (team decisions, not wording)

- **Cut for words in v3:** "WInS shows this mix, scaled down" (8 words). The TNA already shows the WInS book; put the
  sentence back only if another 8 words go.

- **Strategy name vote**: "Root-and-Branch" (V5) vs "Roots First" (competition/COMPETITION.md). Use one, identically, everywhere.
- **Floor size**: the IPS says "what remains" (the 2028 remainder), which is the honest rule now that the ladder headroom is $1,913.
- **Authorship**: the team writes the submitted text from its own understanding; log this exemplar in the AI-use record.
- **One confidence number?** The IPS need not quote one. If the team wants data in the IPS (Creativity: "uses data effectively"),
  the strongest single line is "in our tests the gift reached the top in about three of four market paths" (MODEL,
  `keel/library/range_2031/`), which costs about 15 words.
