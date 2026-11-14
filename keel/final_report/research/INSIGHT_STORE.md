# The insight store: every idea for the Final Report, ranked

Caplet, Book 14: "Keep a store of every single insight you have. They should be organised or categorised ... some kind of ranking or rating system ... You must not lose a thing." This page is the front door. It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.

## How it works

- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards in `cards/` in the same format.
- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags below). An idea can sit under several.
- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is 19 or more, B 15 to 18, C below 15.
- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why); merged (a duplicate, pointing to the row that carries it).
- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies them and records which rows have been judged.

## Where it stands

- **3515 ideas** in the store; 2681 judged so far, the rest on the first pass.
- Tiers: A 1223, B 1319, C 395; refused or merged 578.
- 586 ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).
- Rows per source: `cards/NUM_extras_2026-11-09.md` 12; `cards/Q10_inflation_inputs.md` 25; `cards/Q10b_taiwan_dollar_2025_and_insurers.md` 32; `cards/Q10c_taiwan_building_costs_and_codes.md` 40; `cards/Q10d_moc_ncaf_residency_support.md` 30; `cards/Q11a_funders_seed_assurance.md` 35; `cards/Q11b_real_case_statements.md` 35; `cards/Q11c_unequal_cosponsors_and_conditions.md` 35; `cards/Q11d_taiwan_funders_primary.md` 32; `cards/Q12_lauras_working_life.md` 35; `cards/Q12b_lauras_working_life_gaps.md` 22; `cards/Q15_monitoring_and_triggers.md` 41; `cards/Q16_operating_reserve_mechanics.md` 40; `cards/Q17_judging_the_implementation.md` 40; `cards/Q18_pledges_and_stated_confidence.md` 40; `cards/Q19_range_rule_and_confidence.md` 28; `cards/Q1_career_as_shares.md` 50; `cards/Q1b_career_beta_horizon.md` 28; `cards/Q1c_career_and_diversification.md` 40; `cards/Q20_pooled_book_or_margin.md` 31; `cards/Q21_team_reflection_events.md` 24; `cards/Q22_cosponsor_words_checklist.md` 39; `cards/Q23_exhibits_and_format.md` 34; `cards/Q24_kept_half_and_joint_stress.md` 35; `cards/Q25_what_returns_to_laura.md` 32; `cards/Q26_monitoring_table.md` 32; `cards/Q27_reflection_rubric.md` 30; `cards/Q28_exhibits_prior_art.md` 35; `cards/Q29_section2_pilot_frame.md` 34; `cards/Q2a_fixed_promises_what_broke.md` 33; `cards/Q2b_escrows_lotteries_settlements_stress.md` 29; `cards/Q2c_endowment_spending_rules.md` 35; `cards/Q30_table3_cut_and_xdate.md` 34; `cards/Q31_escrow_standard_plain_words.md` 34; `cards/Q32_meaningful_contribution.md` 35; `cards/Q33_shares_of_free_money.md` 33; `cards/Q34_policy_and_implementation.md` 35; `cards/Q35_range_forecasts_credibility.md` 32; `cards/Q36_ibonds_fund_end_powers.md` 23; `cards/Q37_stating_assumptions.md` 35; `cards/Q38_holding_identifiers.md` 20; `cards/Q39_strongest_critiques.md` 23; `cards/Q3a_floors_in_markets.md` 34; `cards/Q3b_floors_in_institutions.md` 34; `cards/Q42_analogy_and_metaphor_evidence.md` 28; `cards/Q43_when_a_promise_counts.md` 45; `cards/Q44_conceit_craft_open_items.md` 23; `cards/Q4b_cosponsors_in_downturns.md` 35; `cards/Q4c_how_sure_words_and_numbers.md` 33; `cards/Q5_is_half_right.md` 34; `cards/Q5b_kept_share_numbers.md` 11; `cards/Q5c_option_value_and_last_dollar.md` 27; `cards/Q5d_small_arts_buildings_overruns.md` 30; `cards/Q5e_does_the_reserve_fall_with_its_uses.md` 29; `cards/Q6_how_far_to_trust_7_5.md` 33; `cards/Q6b_forecast_panel_2027.md` 34; `cards/Q6c_falls_and_the_top.md` 25; `cards/Q6d_one_world_fund.md` 31; `cards/Q7_precommitment_and_rules.md` 32; `cards/Q7b_rules_and_escape_clauses.md` 42; `cards/Q7c_endowment_rules.md` 35; `cards/Q8a_certainty_in_engineering.md` 35; `cards/Q8b_certainty_standards_1in200_ALARP.md` 35; `cards/Q9_what_makes_a_residency_last.md` 35; `cards/Q9b_residencies_reserves_and_founders.md` 31; `cards/Q9c_taiwan_residencies_funding.md` 35; `harvest/H10_why_wharton.md` 65; `harvest/H1_idea_bank_part1.md` 88; `harvest/H2_idea_bank_part2_and_ledger.md` 124; `harvest/H3_concepts_R02_R05_R06.md` 126; `harvest/H4_synergies_S1_S3_fusions.md` 190; `harvest/H5_synergies_S4_S6_R11.md` 153; `harvest/H6_shiller_damodaran.md` 171; `harvest/H7_final_night_reading.md` 118; `harvest/H8_lab_window_plans.md` 161; `harvest/H9_doc_research_tabs.md` 186.

## The parts of the plan and the case

| Tag | What it covers | Ideas | Ranked list |
|---|---|---|---|
| CAREER | Laura's career as an unsellable stock | 231 | [by_tag/CAREER.md](store/by_tag/CAREER.md) |
| CERTAINTY | A high degree of certainty | 721 | [by_tag/CERTAINTY.md](store/by_tag/CERTAINTY.md) |
| LADDER | The ten Treasuries | 431 | [by_tag/LADDER.md](store/by_tag/LADDER.md) |
| COMPLETE2028 | The 2028 deposit completes the ladder | 171 | [by_tag/COMPLETE2028.md](store/by_tag/COMPLETE2028.md) |
| FLOOR | The 2032 Treasury fund (bottom of the range) | 355 | [by_tag/FLOOR.md](store/by_tag/FLOOR.md) |
| CEILING | VT (top of the range) | 426 | [by_tag/CEILING.md](store/by_tag/CEILING.md) |
| HALFKEPT | Half the shares promised to no one | 344 | [by_tag/HALFKEPT.md](store/by_tag/HALFKEPT.md) |
| MOVE2031 | The move into Treasuries before 2031 | 249 | [by_tag/MOVE2031.md](store/by_tag/MOVE2031.md) |
| RESERVE2033 | The operating reserve from 2033 | 201 | [by_tag/RESERVE2033.md](store/by_tag/RESERVE2033.md) |
| TWOREASONS | Only two reasons to change | 263 | [by_tag/TWOREASONS.md](store/by_tag/TWOREASONS.md) |
| COSPONSOR | The 2031 range and the co-sponsors | 731 | [by_tag/COSPONSOR.md](store/by_tag/COSPONSOR.md) |
| FUNDRAISING | The fundraising text | 106 | [by_tag/FUNDRAISING.md](store/by_tag/FUNDRAISING.md) |
| RESIDENCY | The residency itself | 196 | [by_tag/RESIDENCY.md](store/by_tag/RESIDENCY.md) |
| INFLATION_TWD | Inflation, Taiwan costs, the Taiwan dollar | 173 | [by_tag/INFLATION_TWD.md](store/by_tag/INFLATION_TWD.md) |
| REINVEST | Reinvesting the ladder's interest | 180 | [by_tag/REINVEST.md](store/by_tag/REINVEST.md) |
| LAURA | Laura's working life and values | 115 | [by_tag/LAURA.md](store/by_tag/LAURA.md) |
| PROCESS | How the team decided and learned | 477 | [by_tag/PROCESS.md](store/by_tag/PROCESS.md) |
| PRESENTATION | How the report shows its work | 313 | [by_tag/PRESENTATION.md](store/by_tag/PRESENTATION.md) |
| OTHER | Other | 178 | [by_tag/OTHER.md](store/by_tag/OTHER.md) |
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
| 1 | Q12-018 | 25 | CAREER, LAURA | Laura's own genre, graphic novels: +29% in 2020 (Q1 row 32), then -22.4% in 2023 ("the biggest decline") and -11.5% in 2024 (24.4m copies), then +0.7% in the first nine months of 2025. Keel arithmeti… | adapt |
| 2 | Q16-018 | 25 | LADDER, RESERVE2033, CERTAINTY | A state lottery funds fixed annual prizes with the same rule as the IPS: "The Lottery's investment portfolio shall be structured so that investments mature in amounts sufficient to meet required priz… | keep |
| 3 | Q5c-015 | 25 | HALFKEPT, COSPONSOR, FUNDRAISING | The unannounced form: "a donor makes a lead gift and decides later to give another gift", when a campaign "is falling short of its goal" or "cost overruns have made the goal too low"; "Donors will on… | keep |
| 4 | Q5e-028 | 25 | HALFKEPT, COSPONSOR, INFLATION_TWD | The uses take turns: slump 2008-09, giving fell and building costs fell a year later; inflationary 2022, building costs rose while giving held in dollars; stagflation 1973-75, both (giving -9.2%; Tur… | adapt |
| 5 | Q9-016 | 25 | RESIDENCY, RESERVE2033, CERTAINTY | One-founder cultural institutions are fragile: private art museums that closed had been open a median of 10 years; closure was "usually related to financial difficulties, rather than the founder's de… | keep |
| 6 | H7-081 | 24 | CAREER, CERTAINTY, COSPONSOR | Trust law judges each holding "in the context of the trust portfolio as a whole", counting "Other resources of the beneficiaries", "regularity of income" and "the possible effect of inflation or defl… | keep |
| 7 | NUM-001 | 24 | REINVEST, LADDER, CERTAINTY | The ladder as written pays all ten only if every coupon earns at least 5.12% a year until needed, which is just the average of today's forward rates (4.67% for 2027-33, 5.43% for 2033-42): buying at … | keep |
| 8 | Q1-022 | 24 | CAREER, LAURA | Revealed hedging: a household that moves to an industry with high wage volatility "will ceteris paribus decrease its portfolio share of risky assets by up to 35%, or USD 15,575" (Sweden, 3,815 switch… | keep |
| 9 | Q1-046 | 24 | LAURA, CAREER | Laura's own breakout came in the crash year: "In 2020, Laura published The Wuhan I Know", which "ultimately inspired her bestselling graphic memoir, Messy Roots" (case p.1); graphic novels +29% that … | adapt |
| 10 | Q10c-002 | 24 | INFLATION_TWD, HISTORY | Costs rise in bursts: six of 25 years (2004 +14.1%, 2006 +7.3%, 2007 +9.0%, 2008 +14.0%, 2021 +10.9%, 2022 +7.4%) carried about 80% of the index's 2000-2025 rise; the other 19 years averaged 0.8% a y… | keep |
| 11 | Q10d-020 | 24 | COSPONSOR, CAREER | Taiwan's 2008-09 recession: the Council for Cultural Affairs' spending was NT$5.31bn in 2008 (+0.9%), NT$6.86bn in 2009 (+29.1%), NT$8.40bn in 2010 (+22.5%) and NT$10.75bn in 2011 (+28.0%), then NT$9… | adapt |
| 12 | Q11a-025 | 24 | COSPONSOR, FLOOR, MOVE2031 | Uncertainty about how much is needed breaks group funding; uncertainty about the size of the benefit does not. Threshold known: catastrophe avoided in 18 of 20 groups (8/10 with known impact, 10/10 w… | keep |
| 13 | Q11b-032 | 24 | COSPONSOR, FLOOR, CEILING, MOVE2031 | CASE's counting rules split firm and soft money: "Do not include conditional pledges where conditions may not be met by the institution, until such time that it is anticipated the conditions will be … | keep |
| 14 | Q12-001 | 24 | CAREER, COMPLETE2028 | An advance is not one cheque: the model contract pays it "on the execution of this Agreement", "on acceptance of the complete manuscript" and "on Publisher's initial publication of the Work"; "paymen… | keep |
| 15 | Q12-004 | 24 | CAREER, COMPLETE2028 | In the 2020 shock the biggest publisher stretched payments rather than cancelling: Penguin Random House "lengthened the period of payment on the first installments of significant advances"; "While th… | keep |
| 16 | Q12-008 | 24 | CAREER, COMPLETE2028 | Royalties arrive twice a year, three months after each half: "Publisher shall prepare a statement of account semi-annually", paid "within three months following the end of the period". Keel arithmeti… | keep |
| 17 | Q16-020 | 24 | REINVEST, COMPLETE2028 | The same policy mitigates reinvestment risk by "holding bonds until maturity; reinvesting using available funds ...; and purchasing bonds to hold in reserve to serve as an additional financial resour… | keep |
| 18 | Q17-024 | 24 | LADDER, FLOOR, CEILING | The WInS book is plan "(ii)R": Laura's position after both deposits scaled by 300/450. At cost: ladder $195,886.53 (65.3%), floor stand-in $72,765.65 (24.3%), VT $26,524.61 (8.84%), cash $4,823.21 (1… | adapt |
| 19 | Q1b-010 | 24 | CAREER, CERTAINTY | At the very top, pay and shares move together fast: "The co-movement of income growth for top earners with GDP growth and stock returns is quite striking. In fact, the correlation with all three seri… | keep |
| 20 | Q1c-005 | 24 | CAREER, COMPLETE2028 | Tax returns show 2009, the year after the crash, as the bad year: arts, entertainment and recreation sole proprietors' receipts $33.1bn to $29.2bn (-11.6%), profits $8.1bn to $6.8bn (-15.0%), with re… | keep |
| 21 | Q1c-010 | 24 | CAREER, TWOREASONS | 2020 hit the career while shares rose: Census 7115 receipts $23,595.6m (2019) to $20,674.5m (2020), -12.4%; establishments 969,978 to 874,421 (-9.9%); receipts per establishment $24,326 to $23,644 (-… | adapt |
| 22 | Q25-001 | 24 | CEILING, COSPONSOR, HALFKEPT | Real promises: receivers rated a broken promise 8.32, a kept one 9.88 and an exceeded one 9.77 (1-11); d .74 against .06; delivering 15 puzzle tables instead of 10 earned no credit, nor any more perc… | keep |
| 23 | Q26-014 | 24 | LADDER, FLOOR, CERTAINTY | A fund can pay less than its holdings while doing what its prospectus says: costs outside the 0.07% fee (interest, taxes, transaction costs, "litigation expenses and any extraordinary expenses"), sec… | keep |
| 24 | Q29-012 | 24 | PROCESS, LADDER | Pilots measure fidelity and adherence: "Fidelity rates per unit monitored"; "Rates of adherence to protocol" | keep |
| 25 | Q29-019 | 24 | LADDER, COMPLETE2028, FLOOR, PROCESS | Test what scales, calculate what does not, add an allowance. The model is towed "at speeds corresponding to the same Froude numbers as for the full-scale ship"; the wave part is measured on the model… | keep |
| 26 | Q29-032 | 24 | CERTAINTY, HALFKEPT, CEILING | Criterion D: the IPS's rule survives the scaling, worded as "promised money held in shares: $0, in the book and in the plan" | keep |
| 27 | Q37-002 | 24 | PRESENTATION, LAURA | Use the case's own five assumption areas as 3e's list, in the case's order | keep |
| 28 | Q37-016 | 24 | COMPLETE2028, TWOREASONS | The deposit assumption is "in full at the start of 2028"; 31 March 2028 is reason 1's trigger, not the assumption | adapt |
| 29 | Q37-018 | 24 | CEILING, HALFKEPT | The 7.5% moves only the top and her flexibility; at 4% to 10% the stated top is $115,000 in every column | adapt |
| 30 | Q37-019 | 24 | FLOOR, CEILING, CERTAINTY | The 0.5% is a one-time cut of each end's value for fund frictions, not "half a percent a year" | adapt |
| 31 | Q39-019 | 24 | LADDER, CEILING | Outside the US, long-run shares fail more often: across 39 developed markets since 1841, "a 12% chance that a diversified investor with a 30-year investment horizon will lose relative to inflation" (… | keep |
| 32 | Q43-009 | 24 | OTHER | "the law is violated not just when there are insufficient funds in an account when a payment becomes due. The very act of obligating the United States to make a payment when the necessary funds are n… | keep |
| 33 | Q43-039 | 24 | MOVE2031 | "Gifts of cash and marketable securities will be considered available for the project upon receipt. Foundation policies provide that marketable securities will be sold upon receipt"; an exception if … | keep |
| 34 | Q5-014 | 24 | HALFKEPT, CERTAINTY | England's housing agency split buildings by risk (Table 4): "Uncomplex Buildings (low risk)", "residential, schools, community buildings, GP practices, car parks, small sports centres", n=64: P50 4%,… | keep |
| 35 | Q5-018 | 24 | HALFKEPT, COSPONSOR, MOVE2031 | Norway's state project model gives the agency a P50 steering frame and sets the cost frame at P85; the difference is a reserve held by the ministry, not the project | keep |
| 36 | Q5-023 | 24 | INFLATION_TWD, COSPONSOR | The same manual prices escalation (物價調整費) separately, from the average of the construction cost index (10 years in 2018; 3-10 years in the 2023 revision), and lists causes of cost change including ex… | keep |
| 37 | Q5b-002 | 24 | HALFKEPT, MOVE2031, RANGE2031 | Each $5,000 more of stated top costs about $5,266 of what she keeps (her flexibility plus anything above the top): $35,272 / $30,006 / $24,740 where the $110,000 / $115,000 / $120,000 steps start (28… | keep |
| 38 | Q5c-004 | 24 | HALFKEPT, CEILING, COSPONSOR | Quasi-option value exists without risk aversion when a choice cannot be undone and "realizations in one period affect expectations in the next"; "we should err on the side of under-investment ... und… | keep |
| 39 | Q5c-011 | 24 | FLOOR, HALFKEPT | A floor with full freedom above it is the best simple rule when you want commitment but expect news: "a minimum-savings rule, which restricts individuals to save above some level, allowing complete f… | keep |
| 40 | Q5d-001 | 24 | HALFKEPT, RESIDENCY | Norway, 215 finished public buildings from three public owners (2003-2020; 90% under 11,000 m²), final cost against the budget at the investment decision. Smallest-area quarter: P10 -5% / P50 12% / P… | keep |

## The thinnest parts (fewest ideas rated B or better)

- FUNDRAISING (The fundraising text): 90 rated B or better, 106 in all.
- OTHER (Other): 91 rated B or better, 178 in all.
- LAURA (Laura's working life and values): 105 rated B or better, 115 in all.
- REINVEST (Reinvesting the ladder's interest): 146 rated B or better, 180 in all.
- INFLATION_TWD (Inflation, Taiwan costs, the Taiwan dollar): 155 rated B or better, 173 in all.
- COMPLETE2028 (The 2028 deposit completes the ladder): 158 rated B or better, 171 in all.
- RESIDENCY (The residency itself): 161 rated B or better, 196 in all.
- RESERVE2033 (The operating reserve from 2033): 187 rated B or better, 201 in all.
