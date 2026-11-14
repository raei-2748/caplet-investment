# The insight store: every idea for the Final Report, ranked

Caplet, Book 14: "Keep a store of every single insight you have. They should be organised or categorised ... some kind of ranking or rating system ... You must not lose a thing." This page is the front door. It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.

## How it works

- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards in `cards/` in the same format.
- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags below). An idea can sit under several.
- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is 19 or more, B 15 to 18, C below 15.
- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why); merged (a duplicate, pointing to the row that carries it).
- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies them and records which rows have been judged.

## Where it stands

- **3348 ideas** in the store; 2058 judged so far, the rest on the first pass.
- Tiers: A 1247, B 1467, C 339; refused or merged 295.
- 505 ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).
- Rows per source: `cards/NUM_extras_2026-11-09.md` 12; `cards/Q10_inflation_inputs.md` 25; `cards/Q10b_taiwan_dollar_2025_and_insurers.md` 32; `cards/Q10c_taiwan_building_costs_and_codes.md` 40; `cards/Q10d_moc_ncaf_residency_support.md` 30; `cards/Q11a_funders_seed_assurance.md` 35; `cards/Q11b_real_case_statements.md` 35; `cards/Q11c_unequal_cosponsors_and_conditions.md` 35; `cards/Q11d_taiwan_funders_primary.md` 32; `cards/Q12_lauras_working_life.md` 35; `cards/Q12b_lauras_working_life_gaps.md` 22; `cards/Q15_monitoring_and_triggers.md` 41; `cards/Q16_operating_reserve_mechanics.md` 40; `cards/Q17_judging_the_implementation.md` 40; `cards/Q18_pledges_and_stated_confidence.md` 40; `cards/Q19_range_rule_and_confidence.md` 28; `cards/Q1_career_as_shares.md` 50; `cards/Q1b_career_beta_horizon.md` 28; `cards/Q1c_career_and_diversification.md` 40; `cards/Q20_pooled_book_or_margin.md` 31; `cards/Q21_team_reflection_events.md` 24; `cards/Q22_cosponsor_words_checklist.md` 39; `cards/Q23_exhibits_and_format.md` 34; `cards/Q24_kept_half_and_joint_stress.md` 35; `cards/Q25_what_returns_to_laura.md` 32; `cards/Q26_monitoring_table.md` 32; `cards/Q27_reflection_rubric.md` 30; `cards/Q28_exhibits_prior_art.md` 35; `cards/Q29_section2_pilot_frame.md` 34; `cards/Q2a_fixed_promises_what_broke.md` 33; `cards/Q2b_escrows_lotteries_settlements_stress.md` 29; `cards/Q2c_endowment_spending_rules.md` 35; `cards/Q30_table3_cut_and_xdate.md` 34; `cards/Q31_escrow_standard_plain_words.md` 34; `cards/Q32_meaningful_contribution.md` 35; `cards/Q33_shares_of_free_money.md` 33; `cards/Q34_policy_and_implementation.md` 35; `cards/Q35_range_forecasts_credibility.md` 32; `cards/Q36_ibonds_fund_end_powers.md` 23; `cards/Q37_stating_assumptions.md` 35; `cards/Q38_holding_identifiers.md` 20; `cards/Q39_strongest_critiques.md` 23; `cards/Q3a_floors_in_markets.md` 34; `cards/Q3b_floors_in_institutions.md` 34; `cards/Q42_analogy_and_metaphor_evidence.md` 28; `cards/Q43_when_a_promise_counts.md` 45; `cards/Q44_conceit_craft_open_items.md` 23; `cards/Q4b_cosponsors_in_downturns.md` 35; `cards/Q4c_how_sure_words_and_numbers.md` 33; `cards/Q5_is_half_right.md` 34; `cards/Q5b_kept_share_numbers.md` 11; `cards/Q5c_option_value_and_last_dollar.md` 27; `cards/Q5d_small_arts_buildings_overruns.md` 30; `cards/Q5e_does_the_reserve_fall_with_its_uses.md` 29; `cards/Q6_how_far_to_trust_7_5.md` 33; `cards/Q7_precommitment_and_rules.md` 32; `cards/Q8a_certainty_in_engineering.md` 35; `cards/Q8b_certainty_standards_1in200_ALARP.md` 35; `cards/Q9_what_makes_a_residency_last.md` 35; `cards/Q9b_residencies_reserves_and_founders.md` 31; `cards/Q9c_taiwan_residencies_funding.md` 35; `harvest/H10_why_wharton.md` 65; `harvest/H1_idea_bank_part1.md` 88; `harvest/H2_idea_bank_part2_and_ledger.md` 124; `harvest/H3_concepts_R02_R05_R06.md` 126; `harvest/H4_synergies_S1_S3_fusions.md` 190; `harvest/H5_synergies_S4_S6_R11.md` 153; `harvest/H6_shiller_damodaran.md` 171; `harvest/H7_final_night_reading.md` 118; `harvest/H8_lab_window_plans.md` 161; `harvest/H9_doc_research_tabs.md` 186.

## The parts of the plan and the case

| Tag | What it covers | Ideas | Ranked list |
|---|---|---|---|
| CAREER | Laura's career as an unsellable stock | 264 | [by_tag/CAREER.md](store/by_tag/CAREER.md) |
| CERTAINTY | A high degree of certainty | 773 | [by_tag/CERTAINTY.md](store/by_tag/CERTAINTY.md) |
| LADDER | The ten Treasuries | 488 | [by_tag/LADDER.md](store/by_tag/LADDER.md) |
| COMPLETE2028 | The 2028 deposit completes the ladder | 189 | [by_tag/COMPLETE2028.md](store/by_tag/COMPLETE2028.md) |
| FLOOR | The 2032 Treasury fund (bottom of the range) | 392 | [by_tag/FLOOR.md](store/by_tag/FLOOR.md) |
| CEILING | VT (top of the range) | 411 | [by_tag/CEILING.md](store/by_tag/CEILING.md) |
| HALFKEPT | Half the shares promised to no one | 334 | [by_tag/HALFKEPT.md](store/by_tag/HALFKEPT.md) |
| MOVE2031 | The move into Treasuries before 2031 | 232 | [by_tag/MOVE2031.md](store/by_tag/MOVE2031.md) |
| RESERVE2033 | The operating reserve from 2033 | 202 | [by_tag/RESERVE2033.md](store/by_tag/RESERVE2033.md) |
| TWOREASONS | Only two reasons to change | 246 | [by_tag/TWOREASONS.md](store/by_tag/TWOREASONS.md) |
| COSPONSOR | The 2031 range and the co-sponsors | 768 | [by_tag/COSPONSOR.md](store/by_tag/COSPONSOR.md) |
| FUNDRAISING | The fundraising text | 102 | [by_tag/FUNDRAISING.md](store/by_tag/FUNDRAISING.md) |
| RESIDENCY | The residency itself | 190 | [by_tag/RESIDENCY.md](store/by_tag/RESIDENCY.md) |
| INFLATION_TWD | Inflation, Taiwan costs, the Taiwan dollar | 183 | [by_tag/INFLATION_TWD.md](store/by_tag/INFLATION_TWD.md) |
| REINVEST | Reinvesting the ladder's interest | 202 | [by_tag/REINVEST.md](store/by_tag/REINVEST.md) |
| LAURA | Laura's working life and values | 111 | [by_tag/LAURA.md](store/by_tag/LAURA.md) |
| PROCESS | How the team decided and learned | 458 | [by_tag/PROCESS.md](store/by_tag/PROCESS.md) |
| PRESENTATION | How the report shows its work | 302 | [by_tag/PRESENTATION.md](store/by_tag/PRESENTATION.md) |
| OTHER | Other | 193 | [by_tag/OTHER.md](store/by_tag/OTHER.md) |
| CASE | CASE | 1 | [by_tag/CASE.md](store/by_tag/CASE.md) |
| CLIENT | CLIENT | 1 | [by_tag/CLIENT.md](store/by_tag/CLIENT.md) |
| EDUCATION | EDUCATION | 5 | [by_tag/EDUCATION.md](store/by_tag/EDUCATION.md) |
| HISTORY | HISTORY | 5 | [by_tag/HISTORY.md](store/by_tag/HISTORY.md) |
| JUDGE | JUDGE | 2 | [by_tag/JUDGE.md](store/by_tag/JUDGE.md) |
| LIQUIDITY | LIQUIDITY | 1 | [by_tag/LIQUIDITY.md](store/by_tag/LIQUIDITY.md) |
| MINREQ | MINREQ | 3 | [by_tag/MINREQ.md](store/by_tag/MINREQ.md) |
| MONITOR | MONITOR | 5 | [by_tag/MONITOR.md](store/by_tag/MONITOR.md) |
| RANGE2031 | RANGE2031 | 6 | [by_tag/RANGE2031.md](store/by_tag/RANGE2031.md) |
| RULE | RULE | 4 | [by_tag/RULE.md](store/by_tag/RULE.md) |

## The top 40 across the store (current ratings)

| Rank | Id | Score | Tags | Idea | Status |
|---|---|---|---|---|---|
| 1 | Q5c-015 | 25 | HALFKEPT, COSPONSOR, FUNDRAISING | The unannounced form: "a donor makes a lead gift and decides later to give another gift", when a campaign "is falling short of its goal" or "cost overruns have made the goal too low"; "Donors will on… | keep |
| 2 | Q5e-028 | 25 | HALFKEPT, COSPONSOR, INFLATION_TWD | The uses take turns: slump 2008-09, giving fell and building costs fell a year later; inflationary 2022, building costs rose while giving held in dollars; stagflation 1973-75, both (giving -9.2%; Tur… | adapt |
| 3 | Q10c-002 | 24 | INFLATION_TWD, HISTORY | Costs rise in bursts: six of 25 years (2004 +14.1%, 2006 +7.3%, 2007 +9.0%, 2008 +14.0%, 2021 +10.9%, 2022 +7.4%) carried about 80% of the index's 2000-2025 rise; the other 19 years averaged 0.8% a y… | keep |
| 4 | Q10d-020 | 24 | COSPONSOR, CAREER | Taiwan's 2008-09 recession: the Council for Cultural Affairs' spending was NT$5.31bn in 2008 (+0.9%), NT$6.86bn in 2009 (+29.1%), NT$8.40bn in 2010 (+22.5%) and NT$10.75bn in 2011 (+28.0%), then NT$9… | adapt |
| 5 | Q11a-025 | 24 | COSPONSOR, FLOOR, MOVE2031 | Uncertainty about how much is needed breaks group funding; uncertainty about the size of the benefit does not. Threshold known: catastrophe avoided in 18 of 20 groups (8/10 with known impact, 10/10 w… | keep |
| 6 | Q11b-032 | 24 | COSPONSOR, FLOOR, CEILING, MOVE2031 | CASE's counting rules split firm and soft money: "Do not include conditional pledges where conditions may not be met by the institution, until such time that it is anticipated the conditions will be … | keep |
| 7 | Q17-024 | 24 | LADDER, FLOOR, CEILING | The WInS book is plan "(ii)R": Laura's position after both deposits scaled by 300/450. At cost: ladder $195,886.53 (65.3%), floor stand-in $72,765.65 (24.3%), VT $26,524.61 (8.84%), cash $4,823.21 (1… | adapt |
| 8 | Q20-020 | 24 | CERTAINTY, LADDER | The escrow verifier's test: escrow cash flows "sufficient, without further reinvestment, to pay the debt service due on the transaction in full and on time", with maturities "on or prior to" each pay… | keep |
| 9 | Q25-001 | 24 | CEILING, COSPONSOR, HALFKEPT | Real promises: receivers rated a broken promise 8.32, a kept one 9.88 and an exceeded one 9.77 (1-11); d .74 against .06; delivering 15 puzzle tables instead of 10 earned no credit, nor any more perc… | keep |
| 10 | Q26-014 | 24 | LADDER, FLOOR, CERTAINTY | A fund can pay less than its holdings while doing what its prospectus says: costs outside the 0.07% fee (interest, taxes, transaction costs, "litigation expenses and any extraordinary expenses"), sec… | keep |
| 11 | Q29-012 | 24 | PROCESS, LADDER | Pilots measure fidelity and adherence: "Fidelity rates per unit monitored"; "Rates of adherence to protocol" | keep |
| 12 | Q29-019 | 24 | LADDER, COMPLETE2028, FLOOR, PROCESS | Test what scales, calculate what does not, add an allowance. The model is towed "at speeds corresponding to the same Froude numbers as for the full-scale ship"; the wave part is measured on the model… | keep |
| 13 | Q29-032 | 24 | CERTAINTY, HALFKEPT, CEILING | Criterion D: the IPS's rule survives the scaling, worded as "promised money held in shares: $0, in the book and in the plan" | keep |
| 14 | Q37-002 | 24 | PRESENTATION, LAURA | Use the case's own five assumption areas as 3e's list, in the case's order | keep |
| 15 | Q37-016 | 24 | COMPLETE2028, TWOREASONS | The deposit assumption is "in full at the start of 2028"; 31 March 2028 is reason 1's trigger, not the assumption | adapt |
| 16 | Q37-018 | 24 | CEILING, HALFKEPT | The 7.5% moves only the top and her flexibility; at 4% to 10% the stated top is $115,000 in every column | keep |
| 17 | Q37-019 | 24 | FLOOR, CEILING, CERTAINTY | The 0.5% is a one-time cut of each end's value for fund frictions, not "half a percent a year" | adapt |
| 18 | Q43-009 | 24 | OTHER | "the law is violated not just when there are insufficient funds in an account when a payment becomes due. The very act of obligating the United States to make a payment when the necessary funds are n… | keep |
| 19 | Q43-039 | 24 | MOVE2031 | "Gifts of cash and marketable securities will be considered available for the project upon receipt. Foundation policies provide that marketable securities will be sold upon receipt"; an exception if … | keep |
| 20 | Q5-014 | 24 | HALFKEPT, CERTAINTY | England's housing agency split buildings by risk (Table 4): "Uncomplex Buildings (low risk)", "residential, schools, community buildings, GP practices, car parks, small sports centres", n=64: P50 4%,… | keep |
| 21 | Q5b-002 | 24 | HALFKEPT, MOVE2031, RANGE2031 | Each $5,000 more of stated top costs about $5,266 of what she keeps (her flexibility plus anything above the top): $35,272 / $30,006 / $24,740 where the $110,000 / $115,000 / $120,000 steps start (28… | keep |
| 22 | Q5c-004 | 24 | HALFKEPT, CEILING, COSPONSOR | Quasi-option value exists without risk aversion when a choice cannot be undone and "realizations in one period affect expectations in the next"; "we should err on the side of under-investment ... und… | keep |
| 23 | Q5c-011 | 24 | FLOOR, HALFKEPT | A floor with full freedom above it is the best simple rule when you want commitment but expect news: "a minimum-savings rule, which restricts individuals to save above some level, allowing complete f… | keep |
| 24 | Q5d-001 | 24 | HALFKEPT, RESIDENCY | Norway, 215 finished public buildings from three public owners (2003-2020; 90% under 11,000 m²), final cost against the budget at the investment decision. Smallest-area quarter: P10 -5% / P50 12% / P… | keep |
| 25 | Q5d-008 | 24 | COSPONSOR, HALFKEPT | Same report. ACE's programme contingency of 5% was not enough and was raised to 7%. Supplementary grants met about 35% of the overrun, so about two thirds fell on the organisations. The two projects … | keep |
| 26 | Q5e-005 | 24 | HALFKEPT, INFLATION_TWD, OTHER | Regime decides the sign: US years with inflation of 4% or more: Turner -0.51 same year, -0.39 a year later; BEA -0.30, -0.28. Under 4%: Turner -0.11, +0.22; BEA +0.02, +0.31 | adapt |
| 27 | Q8a-030 | 24 | TWOREASONS, CERTAINTY | "The existence of multiple levels of defence is not a basis for continued operation in the absence of one level" | keep |
| 28 | Q10-021 | 23 | COSPONSOR, INFLATION_TWD | At 32.768 the range is NT$3.60m to NT$4.42m; by Jan 2033 it buys NT$3.02m to NT$3.70m of today's construction at 3% a year (84%), NT$2.69m to NT$3.30m at 5% (75%), and NT$2.54m to NT$3.11m if the Tai… | adapt |
| 29 | Q10-025 | 23 | INFLATION_TWD, COSPONSOR, CERTAINTY | Over the last 10 years the rate ran from 27.52 (4 Jan 2022, strongest Taiwan dollar) to 33.21 (1 Apr 2025); over 25 years from 27.52 to 35.21 (2 Mar 2009). A return to 27.52 makes a fixed NT$ budget … | keep |
| 30 | Q10b-001 | 23 | INFLATION_TWD, HALFKEPT, MOVE2031 | A two-year rise of 10% or more in the US dollars a NT$ budget needs came in 9.0% of two-year windows starting since Nov 2001 (stricter reading 6.1%; median +0.9%; 1 in 20 at +11.9%); 8.3% since 2000;… | keep |
| 31 | Q10b-031 | 23 | INFLATION_TWD, HALFKEPT, CERTAINTY | The direction comes from the exposure: the contribution is fixed in US dollars and spent in NT$, so only a stronger NT$ costs; at the 25-year weakest (35.21) $115,000 buys 7.5% more NT$ than at 32.76… | keep |
| 32 | Q12-018 | 23 | CAREER, LAURA | Laura's own genre, graphic novels: +29% in 2020 (Q1 row 32), then -22.4% in 2023 ("the biggest decline") and -11.5% in 2024 (24.4m copies), then +0.7% in the first nine months of 2025. Keel arithmeti… | adapt |
| 33 | Q15-009 | 23 | MOVE2031, TWOREASONS | De-risking is one-way: the switch "is automatically made by Mercer as and when a trigger level is reached", and "once the funding level has moved through a trigger, the asset allocation will not be a… | keep |
| 34 | Q16-018 | 23 | LADDER, RESERVE2033, CERTAINTY | A state lottery funds fixed annual prizes with the same rule as the IPS: "The Lottery's investment portfolio shall be structured so that investments mature in amounts sufficient to meet required priz… | keep |
| 35 | Q17-008 | 23 | CERTAINTY, LADDER | Moody's two tests: escrow cash flows "sufficient, without further reinvestment, to pay the debt service ... in full and on time"; securities with "scheduled maturities on or prior to dates on which a… | adapt |
| 36 | Q17-025 | 23 | PROCESS | The team rejected "Book L" (WInS shows only the first $300,000, all bonds, no VT) so that the book would show the whole strategy | keep |
| 37 | Q17-040 | 23 | LADDER, CERTAINTY | In the hedging part one issuer is the point: 89.55% of the book at cost in US Treasury obligations ($268,652.18; IBTM itself 99.45% Treasuries); other issuers would add default risk against fixed dol… | keep |
| 38 | Q1b-002 | 23 | CAREER | The average career is mostly a bond: "The bond component averages more than 80 percent of the value of human capital"; the stock component "averages below 35 percent at all ages for high school agent… | adapt |
| 39 | Q28-023 | 23 | COSPONSOR, FLOOR, CEILING, HALFKEPT, PRESENTATION | Table 2 holds two different ranges: the stated range (a rule-based promise, 8i: $95,000 to $115,000 at forwards) and the spread across 585 history windows (uncertainty: stated bottom $80,000 / $95,00… | keep |
| 40 | Q29-015 | 23 | PROCESS, REINVEST | Honesty test: which criteria came before trading and which after | keep |

## The thinnest parts (fewest ideas rated B or better)

- FUNDRAISING (The fundraising text): 86 rated B or better, 102 in all.
- LAURA (Laura's working life and values): 104 rated B or better, 111 in all.
- OTHER (Other): 156 rated B or better, 193 in all.
- RESIDENCY (The residency itself): 157 rated B or better, 190 in all.
- REINVEST (Reinvesting the ladder's interest): 163 rated B or better, 202 in all.
- INFLATION_TWD (Inflation, Taiwan costs, the Taiwan dollar): 168 rated B or better, 183 in all.
- COMPLETE2028 (The 2028 deposit completes the ladder): 175 rated B or better, 189 in all.
- RESERVE2033 (The operating reserve from 2033): 188 rated B or better, 202 in all.
