# The insight store: every idea for the Final Report, ranked

Caplet, Book 14: "Keep a store of every single insight you have. They should be organised or categorised ... some kind of ranking or rating system ... You must not lose a thing." This page is the front door. It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.

## How it works

- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards in `cards/` in the same format.
- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags below). An idea can sit under several.
- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is 19 or more, B 15 to 18, C below 15.
- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why); merged (a duplicate, pointing to the row that carries it).
- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies them and records which rows have been judged.

## Where it stands

- **2314 ideas** in the store; 1043 judged so far, the rest on the first pass.
- Tiers: A 956, B 1009, C 212; refused or merged 137.
- 445 ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).
- Rows per source: `cards/NUM_extras_2026-11-09.md` 12; `cards/Q10_inflation_inputs.md` 25; `cards/Q11a_funders_seed_assurance.md` 35; `cards/Q11b_real_case_statements.md` 35; `cards/Q12_lauras_working_life.md` 35; `cards/Q12b_lauras_working_life_gaps.md` 22; `cards/Q15_monitoring_and_triggers.md` 41; `cards/Q16_operating_reserve_mechanics.md` 40; `cards/Q17_judging_the_implementation.md` 40; `cards/Q18_pledges_and_stated_confidence.md` 40; `cards/Q19_range_rule_and_confidence.md` 28; `cards/Q1_career_as_shares.md` 50; `cards/Q1b_career_beta_horizon.md` 28; `cards/Q1c_career_and_diversification.md` 40; `cards/Q20_pooled_book_or_margin.md` 31; `cards/Q21_team_reflection_events.md` 24; `cards/Q22_cosponsor_words_checklist.md` 39; `cards/Q23_exhibits_and_format.md` 34; `cards/Q24_kept_half_and_joint_stress.md` 35; `cards/Q25_what_returns_to_laura.md` 32; `cards/Q26_monitoring_table.md` 32; `cards/Q27_reflection_rubric.md` 30; `cards/Q28_exhibits_prior_art.md` 35; `cards/Q4b_cosponsors_in_downturns.md` 35; `cards/Q5_is_half_right.md` 34; `cards/Q6_how_far_to_trust_7_5.md` 33; `cards/Q7_precommitment_and_rules.md` 32; `cards/Q9_what_makes_a_residency_last.md` 35; `harvest/H10_why_wharton.md` 65; `harvest/H1_idea_bank_part1.md` 88; `harvest/H2_idea_bank_part2_and_ledger.md` 124; `harvest/H3_concepts_R02_R05_R06.md` 126; `harvest/H4_synergies_S1_S3_fusions.md` 190; `harvest/H5_synergies_S4_S6_R11.md` 153; `harvest/H6_shiller_damodaran.md` 171; `harvest/H7_final_night_reading.md` 118; `harvest/H8_lab_window_plans.md` 161; `harvest/H9_doc_research_tabs.md` 186.

## The parts of the plan and the case

| Tag | What it covers | Ideas | Ranked list |
|---|---|---|---|
| CAREER | Laura's career as an unsellable stock | 236 | [by_tag/CAREER.md](store/by_tag/CAREER.md) |
| CERTAINTY | A high degree of certainty | 531 | [by_tag/CERTAINTY.md](store/by_tag/CERTAINTY.md) |
| LADDER | The ten Treasuries | 393 | [by_tag/LADDER.md](store/by_tag/LADDER.md) |
| COMPLETE2028 | The 2028 deposit completes the ladder | 151 | [by_tag/COMPLETE2028.md](store/by_tag/COMPLETE2028.md) |
| FLOOR | The 2032 Treasury fund (bottom of the range) | 305 | [by_tag/FLOOR.md](store/by_tag/FLOOR.md) |
| CEILING | VT (top of the range) | 356 | [by_tag/CEILING.md](store/by_tag/CEILING.md) |
| HALFKEPT | Half the shares promised to no one | 237 | [by_tag/HALFKEPT.md](store/by_tag/HALFKEPT.md) |
| MOVE2031 | The move into Treasuries before 2031 | 194 | [by_tag/MOVE2031.md](store/by_tag/MOVE2031.md) |
| RESERVE2033 | The operating reserve from 2033 | 139 | [by_tag/RESERVE2033.md](store/by_tag/RESERVE2033.md) |
| TWOREASONS | Only two reasons to change | 187 | [by_tag/TWOREASONS.md](store/by_tag/TWOREASONS.md) |
| COSPONSOR | The 2031 range and the co-sponsors | 549 | [by_tag/COSPONSOR.md](store/by_tag/COSPONSOR.md) |
| FUNDRAISING | The fundraising text | 45 | [by_tag/FUNDRAISING.md](store/by_tag/FUNDRAISING.md) |
| RESIDENCY | The residency itself | 72 | [by_tag/RESIDENCY.md](store/by_tag/RESIDENCY.md) |
| INFLATION_TWD | Inflation, Taiwan costs, the Taiwan dollar | 110 | [by_tag/INFLATION_TWD.md](store/by_tag/INFLATION_TWD.md) |
| REINVEST | Reinvesting the ladder's interest | 171 | [by_tag/REINVEST.md](store/by_tag/REINVEST.md) |
| LAURA | Laura's working life and values | 86 | [by_tag/LAURA.md](store/by_tag/LAURA.md) |
| PROCESS | How the team decided and learned | 362 | [by_tag/PROCESS.md](store/by_tag/PROCESS.md) |
| PRESENTATION | How the report shows its work | 119 | [by_tag/PRESENTATION.md](store/by_tag/PRESENTATION.md) |
| OTHER | Other | 153 | [by_tag/OTHER.md](store/by_tag/OTHER.md) |
| CASE | CASE | 1 | [by_tag/CASE.md](store/by_tag/CASE.md) |
| CLIENT | CLIENT | 1 | [by_tag/CLIENT.md](store/by_tag/CLIENT.md) |
| EDUCATION | EDUCATION | 5 | [by_tag/EDUCATION.md](store/by_tag/EDUCATION.md) |
| HISTORY | HISTORY | 1 | [by_tag/HISTORY.md](store/by_tag/HISTORY.md) |
| JUDGE | JUDGE | 2 | [by_tag/JUDGE.md](store/by_tag/JUDGE.md) |
| LIQUIDITY | LIQUIDITY | 1 | [by_tag/LIQUIDITY.md](store/by_tag/LIQUIDITY.md) |
| MINREQ | MINREQ | 3 | [by_tag/MINREQ.md](store/by_tag/MINREQ.md) |
| MONITOR | MONITOR | 1 | [by_tag/MONITOR.md](store/by_tag/MONITOR.md) |
| RANGE2031 | RANGE2031 | 2 | [by_tag/RANGE2031.md](store/by_tag/RANGE2031.md) |
| RULE | RULE | 4 | [by_tag/RULE.md](store/by_tag/RULE.md) |

## The top 40 across the store (current ratings)

| Rank | Id | Score | Tags | Idea | Status |
|---|---|---|---|---|---|
| 1 | Q11a-025 | 24 | COSPONSOR, FLOOR, MOVE2031 | Uncertainty about how much is needed breaks group funding; uncertainty about the size of the benefit does not. Threshold known: catastrophe avoided in 18 of 20 groups (8/10 with known impact, 10/10 w… | keep |
| 2 | Q11b-032 | 24 | COSPONSOR, FLOOR, CEILING, MOVE2031 | CASE's counting rules split firm and soft money: "Do not include conditional pledges where conditions may not be met by the institution, until such time that it is anticipated the conditions will be … | keep |
| 3 | Q17-024 | 24 | LADDER, FLOOR, CEILING | The WInS book is plan "(ii)R": Laura's position after both deposits scaled by 300/450. At cost: ladder $195,886.53 (65.3%), floor stand-in $72,765.65 (24.3%), VT $26,524.61 (8.84%), cash $4,823.21 (1… | adapt |
| 4 | Q20-020 | 24 | CERTAINTY, LADDER | The escrow verifier's test: escrow cash flows "sufficient, without further reinvestment, to pay the debt service due on the transaction in full and on time", with maturities "on or prior to" each pay… | keep |
| 5 | Q25-001 | 24 | CEILING, COSPONSOR, HALFKEPT | Real promises: receivers rated a broken promise 8.32, a kept one 9.88 and an exceeded one 9.77 (1-11); d .74 against .06; delivering 15 puzzle tables instead of 10 earned no credit, nor any more perc… | keep |
| 6 | Q26-014 | 24 | LADDER, FLOOR, CERTAINTY | A fund can pay less than its holdings while doing what its prospectus says: costs outside the 0.07% fee (interest, taxes, transaction costs, "litigation expenses and any extraordinary expenses"), sec… | keep |
| 7 | Q5-014 | 24 | HALFKEPT, CERTAINTY | England's housing agency split buildings by risk (Table 4): "Uncomplex Buildings (low risk)", "residential, schools, community buildings, GP practices, car parks, small sports centres", n=64: P50 4%,… | keep |
| 8 | Q10-021 | 23 | COSPONSOR, INFLATION_TWD | At 32.768 the range is NT$3.60m to NT$4.42m; by Jan 2033 it buys NT$3.02m to NT$3.70m of today's construction at 3% a year (84%), NT$2.69m to NT$3.30m at 5% (75%), and NT$2.54m to NT$3.11m if the Tai… | adapt |
| 9 | Q10-025 | 23 | INFLATION_TWD, COSPONSOR, CERTAINTY | Over the last 10 years the rate ran from 27.52 (4 Jan 2022, strongest Taiwan dollar) to 33.21 (1 Apr 2025); over 25 years from 27.52 to 35.21 (2 Mar 2009). A return to 27.52 makes a fixed NT$ budget … | keep |
| 10 | Q12-018 | 23 | CAREER, LAURA | Laura's own genre, graphic novels: +29% in 2020 (Q1 row 32), then -22.4% in 2023 ("the biggest decline") and -11.5% in 2024 (24.4m copies), then +0.7% in the first nine months of 2025. Keel arithmeti… | adapt |
| 11 | Q15-009 | 23 | MOVE2031, TWOREASONS | De-risking is one-way: the switch "is automatically made by Mercer as and when a trigger level is reached", and "once the funding level has moved through a trigger, the asset allocation will not be a… | keep |
| 12 | Q16-018 | 23 | LADDER, RESERVE2033, CERTAINTY | A state lottery funds fixed annual prizes with the same rule as the IPS: "The Lottery's investment portfolio shall be structured so that investments mature in amounts sufficient to meet required priz… | keep |
| 13 | Q17-008 | 23 | CERTAINTY, LADDER | Moody's two tests: escrow cash flows "sufficient, without further reinvestment, to pay the debt service ... in full and on time"; securities with "scheduled maturities on or prior to dates on which a… | adapt |
| 14 | Q17-025 | 23 | PROCESS | The team rejected "Book L" (WInS shows only the first $300,000, all bonds, no VT) so that the book would show the whole strategy | keep |
| 15 | Q17-040 | 23 | LADDER, CERTAINTY | In the hedging part one issuer is the point: 89.55% of the book at cost in US Treasury obligations ($268,652.18; IBTM itself 99.45% Treasuries); other issuers would add default risk against fixed dol… | keep |
| 16 | Q1b-002 | 23 | CAREER | The average career is mostly a bond: "The bond component averages more than 80 percent of the value of human capital"; the stock component "averages below 35 percent at all ages for high school agent… | adapt |
| 17 | Q28-023 | 23 | COSPONSOR, FLOOR, CEILING, HALFKEPT, PRESENTATION | Table 2 holds two different ranges: the stated range (a rule-based promise, 8i: $95,000 to $115,000 at forwards) and the spread across 585 history windows (uncertainty: stated bottom $80,000 / $95,00… | keep |
| 18 | Q4b-001 | 23 | COSPONSOR, HALFKEPT | US foundation giving ROSE in the crash year: foundation assets fell 17.2% in 2008 ($682.2bn to $565.0bn) while foundation giving rose 5.4% ($44.4bn to $46.8bn). The yearbook says funders cut operatin… | adapt |
| 19 | Q7-031 | 23 | TWOREASONS, COSPONSOR, FLOOR | After January 2028 only one of the two reasons can still happen. The case allows no money in or out before 2033 except the two deposits (case p.2), so "a missed deposit" can only occur in Jan 2028, b… | keep |
| 20 | Q9-016 | 23 | RESIDENCY, RESERVE2033, CERTAINTY | One-founder cultural institutions are fragile: private art museums that closed had been open a median of 10 years; closure was "usually related to financial difficulties, rather than the founder's de… | keep |
| 21 | Q9-020 | 23 | RESIDENCY, CERTAINTY, TWOREASONS, CAREER | Yaddo nearly ended before its first guest: after Spencer Trask died in 1909 "the Trasks' financial investments depreciated the following year, jeopardizing Yaddo's future"; Katrina Trask closed the m… | keep |
| 22 | Q9-022 | 23 | RESERVE2033, CERTAINTY, TWOREASONS | Even a large residency endowment can fall 15% in a year: MacDowell's went from $33.1M to $28.2M in 2022 (investment return -$5.6M, after +$7.0M in 2021), while it ran a $3.4M gap before investment re… | keep |
| 23 | Q9-033 | 23 | COSPONSOR, RESIDENCY | Taiwan's national arts grant-maker never got its endowment: the law set a NT$10bn fund to be reached within 10 years; government gave its NT$6bn share by 2003, but the NT$4bn private share was never … | keep |
| 24 | Q11a-004 | 22 | FLOOR, COSPONSOR | Seed money matters only when fixed costs are high: with a high fixed cost, giving in sequence raised the provision rate from 40% (simultaneous) to 76%; with a low fixed cost both were above 80% and "… | keep |
| 25 | Q11b-005 | 22 | COSPONSOR, RESIDENCY, MOVE2031 | MacDowell announced a $13 million campaign in Aug 2010 when "more than $10 million has already been raised", then said what it buys: a library center, endowed Fellowships "in perpetuity", and stipend… | keep |
| 26 | Q11b-014 | 22 | COSPONSOR, LAURA, RESIDENCY | Fogo Island Arts (Canada): Zita Cobb, who made her money in technology and returned home, "personally committed about $30 million of her own capital to build the Inn and the Fogo Island artist studio… | adapt |
| 27 | Q11b-022 | 22 | COSPONSOR, HALFKEPT, RESIDENCY | Kresge's arts program required "a building reserves policy" with every facility grant; a comprehensive campaign should include "transitional operating funding to help the organization adapt to higher… | adapt |
| 28 | Q11b-023 | 22 | COSPONSOR, RESERVE2033, RESIDENCY | NFF's evaluation of Kresge's 32 facility grantees (2010-12 grants): organisations did not plan "for the costs associated with operating new or expanded facilities"; "Many organizations do not plan fo… | keep |
| 29 | Q11b-026 | 22 | INFLATION_TWD, HALFKEPT, MOVE2031, RESIDENCY | Set in Stone (US cultural building 1994-2008, about $16 billion): "More than 80 percent of the projects studied ran over budget, some by as much as 200 percent"; theatres' end cost was about 92 perce… | keep |
| 30 | Q12-001 | 22 | CAREER, COMPLETE2028 | An advance is not one cheque: the model contract pays it "on the execution of this Agreement", "on acceptance of the complete manuscript" and "on Publisher's initial publication of the Work"; "paymen… | keep |
| 31 | Q12-004 | 22 | CAREER, COMPLETE2028 | In the 2020 shock the biggest publisher stretched payments rather than cancelling: Penguin Random House "lengthened the period of payment on the first installments of significant advances"; "While th… | keep |
| 32 | Q12-006 | 22 | CAREER, LAURA | In 2009 the cuts fell on new deals for midlist and new authors, not on proven sellers: "No one had said, 'let's go the extra £50,000'"; "Midlist authors will be squeezed again, perhaps dropped, while… | adapt |
| 33 | Q12-008 | 22 | CAREER, COMPLETE2028 | Royalties arrive twice a year, three months after each half: "Publisher shall prepare a statement of account semi-annually", paid "within three months following the end of the period". Keel arithmeti… | keep |
| 34 | Q12-015 | 22 | CAREER, LAURA | Children's books sell into two markets "and those markets do not cycle together"; institutional cuts "take time to take effect"; worked example: "If a publisher makes 60% of its sales in the institut… | keep |
| 35 | Q15-004 | 22 | TWOREASONS, LADDER, CERTAINTY | Insurers' matching adjustment: the assigned bonds keep their assignment "over the lifetime of the obligations", changed only to maintain the cash-flow match "where the cash flows have materially chan… | adapt |
| 36 | Q15-006 | 22 | LADDER, TWOREASONS, CERTAINTY, REINVEST | A municipal defeasance escrow holds Treasuries to pay old bonds: irrevocable; the agent has no power to invest or swap; a swap needs "a new verification report ... assuming a zero percent reinvestmen… | adapt |
| 37 | Q15-015 | 22 | TWOREASONS, CERTAINTY | 1979 in detail: about 4,000 checks worth about $122 million were late; book-entry holders (over 90% of marketable Treasuries) were unaffected; bills maturing 26 Apr, 3 May and 10 May; "Check processi… | keep |
| 38 | Q15-024 | 22 | TWOREASONS, COMPLETE2028, CERTAINTY | Thirteen debt-limit impasses from 2011 to 2025 all ended by suspension or increase; extra borrowing cost $107m-$161m (2024 dollars) for 2011-2023; at-risk securities were $1.3-5.9 trillion (9-26% of … | keep |
| 39 | Q15-026 | 22 | TWOREASONS, COMPLETE2028, FLOOR | The next standoff: the limit is projected to bind "between late winter and mid-summer of 2027", with resources lasting "roughly six to nine months" more (BPC); limit about May 2027, X-date "February … | keep |
| 40 | Q16-006 | 22 | LADDER, RESERVE2033 | Three iBond Treasury funds have already ended on schedule. IBTD: last trading 15 Dec 2023, proceeds 22 Dec 2023. IBTE: last trading Mon 16 Dec 2024 (15 Dec was a Sunday), proceeds 19 Dec 2024. IBTF: … | keep |

## The thinnest parts (fewest ideas rated B or better)

- FUNDRAISING (The fundraising text): 39 rated B or better, 45 in all.
- RESIDENCY (The residency itself): 70 rated B or better, 72 in all.
- LAURA (Laura's working life and values): 83 rated B or better, 86 in all.
- INFLATION_TWD (Inflation, Taiwan costs, the Taiwan dollar): 102 rated B or better, 110 in all.
- PRESENTATION (How the report shows its work): 114 rated B or better, 119 in all.
- OTHER (Other): 125 rated B or better, 153 in all.
- RESERVE2033 (The operating reserve from 2033): 130 rated B or better, 139 in all.
- REINVEST (Reinvesting the ladder's interest): 136 rated B or better, 171 in all.
