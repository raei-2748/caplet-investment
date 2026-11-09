# The insight store: every idea for the Final Report, ranked

Caplet, Book 14: "Keep a store of every single insight you have. They should be organised or categorised ... some kind of ranking or rating system ... You must not lose a thing." This page is the front door. It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.

## How it works

- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards in `cards/` in the same format.
- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags below). An idea can sit under several.
- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is 19 or more, B 15 to 18, C below 15.
- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why); merged (a duplicate, pointing to the row that carries it).
- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies them and records which rows have been judged.

## Where it stands

- **1892 ideas** in the store; 475 judged so far, the rest on the first pass.
- Tiers: A 872, B 836, C 165; refused or merged 19.
- 406 ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).
- Rows per source: `cards/NUM_extras_2026-11-09.md` 12; `cards/Q10_inflation_inputs.md` 25; `cards/Q11a_funders_seed_assurance.md` 35; `cards/Q11b_real_case_statements.md` 35; `cards/Q12_lauras_working_life.md` 35; `cards/Q15_monitoring_and_triggers.md` 41; `cards/Q16_operating_reserve_mechanics.md` 40; `cards/Q17_judging_the_implementation.md` 40; `cards/Q1_career_as_shares.md` 50; `cards/Q1b_career_beta_horizon.md` 28; `cards/Q4b_cosponsors_in_downturns.md` 35; `cards/Q5_is_half_right.md` 34; `cards/Q6_how_far_to_trust_7_5.md` 33; `cards/Q7_precommitment_and_rules.md` 32; `cards/Q9_what_makes_a_residency_last.md` 35; `harvest/H10_why_wharton.md` 65; `harvest/H1_idea_bank_part1.md` 88; `harvest/H2_idea_bank_part2_and_ledger.md` 124; `harvest/H3_concepts_R02_R05_R06.md` 126; `harvest/H4_synergies_S1_S3_fusions.md` 190; `harvest/H5_synergies_S4_S6_R11.md` 153; `harvest/H6_shiller_damodaran.md` 171; `harvest/H7_final_night_reading.md` 118; `harvest/H8_lab_window_plans.md` 161; `harvest/H9_doc_research_tabs.md` 186.

## The parts of the plan and the case

| Tag | What it covers | Ideas | Ranked list |
|---|---|---|---|
| CAREER | Laura's career as an unsellable stock | 206 | [by_tag/CAREER.md](store/by_tag/CAREER.md) |
| CERTAINTY | A high degree of certainty | 469 | [by_tag/CERTAINTY.md](store/by_tag/CERTAINTY.md) |
| LADDER | The ten Treasuries | 367 | [by_tag/LADDER.md](store/by_tag/LADDER.md) |
| COMPLETE2028 | The 2028 deposit completes the ladder | 133 | [by_tag/COMPLETE2028.md](store/by_tag/COMPLETE2028.md) |
| FLOOR | The 2032 Treasury fund (bottom of the range) | 244 | [by_tag/FLOOR.md](store/by_tag/FLOOR.md) |
| CEILING | VT (top of the range) | 320 | [by_tag/CEILING.md](store/by_tag/CEILING.md) |
| HALFKEPT | Half the shares promised to no one | 194 | [by_tag/HALFKEPT.md](store/by_tag/HALFKEPT.md) |
| MOVE2031 | The move into Treasuries before 2031 | 178 | [by_tag/MOVE2031.md](store/by_tag/MOVE2031.md) |
| RESERVE2033 | The operating reserve from 2033 | 123 | [by_tag/RESERVE2033.md](store/by_tag/RESERVE2033.md) |
| TWOREASONS | Only two reasons to change | 181 | [by_tag/TWOREASONS.md](store/by_tag/TWOREASONS.md) |
| COSPONSOR | The 2031 range and the co-sponsors | 457 | [by_tag/COSPONSOR.md](store/by_tag/COSPONSOR.md) |
| FUNDRAISING | The fundraising text | 19 | [by_tag/FUNDRAISING.md](store/by_tag/FUNDRAISING.md) |
| RESIDENCY | The residency itself | 67 | [by_tag/RESIDENCY.md](store/by_tag/RESIDENCY.md) |
| INFLATION_TWD | Inflation, Taiwan costs, the Taiwan dollar | 100 | [by_tag/INFLATION_TWD.md](store/by_tag/INFLATION_TWD.md) |
| REINVEST | Reinvesting the ladder's interest | 157 | [by_tag/REINVEST.md](store/by_tag/REINVEST.md) |
| LAURA | Laura's working life and values | 73 | [by_tag/LAURA.md](store/by_tag/LAURA.md) |
| PROCESS | How the team decided and learned | 272 | [by_tag/PROCESS.md](store/by_tag/PROCESS.md) |
| PRESENTATION | How the report shows its work | 84 | [by_tag/PRESENTATION.md](store/by_tag/PRESENTATION.md) |
| OTHER | Other | 145 | [by_tag/OTHER.md](store/by_tag/OTHER.md) |
| HISTORY | HISTORY | 1 | [by_tag/HISTORY.md](store/by_tag/HISTORY.md) |

## The top 40 across the store (current ratings)

| Rank | Id | Score | Tags | Idea | Status |
|---|---|---|---|---|---|
| 1 | Q11a-025 | 24 | COSPONSOR, FLOOR, MOVE2031 | Uncertainty about how much is needed breaks group funding; uncertainty about the size of the benefit does not. Threshold known: catastrophe avoided in 18 of 20 groups (8/10 with known impact, 10/10 w… | keep |
| 2 | Q11b-032 | 24 | COSPONSOR, FLOOR, CEILING, MOVE2031 | CASE's counting rules split firm and soft money: "Do not include conditional pledges where conditions may not be met by the institution, until such time that it is anticipated the conditions will be … | keep |
| 3 | Q5-014 | 24 | HALFKEPT, CERTAINTY | England's housing agency split buildings by risk (Table 4): "Uncomplex Buildings (low risk)", "residential, schools, community buildings, GP practices, car parks, small sports centres", n=64: P50 4%,… | keep |
| 4 | Q12-018 | 23 | CAREER, LAURA | Laura's own genre, graphic novels: +29% in 2020 (Q1 row 32), then -22.4% in 2023 ("the biggest decline") and -11.5% in 2024 (24.4m copies), then +0.7% in the first nine months of 2025. Keel arithmeti… | adapt |
| 5 | Q1b-002 | 23 | CAREER | The average career is mostly a bond: "The bond component averages more than 80 percent of the value of human capital"; the stock component "averages below 35 percent at all ages for high school agent… | adapt |
| 6 | Q4b-001 | 23 | COSPONSOR, HALFKEPT | US foundation giving ROSE in the crash year: foundation assets fell 17.2% in 2008 ($682.2bn to $565.0bn) while foundation giving rose 5.4% ($44.4bn to $46.8bn). The yearbook says funders cut operatin… | adapt |
| 7 | Q7-031 | 23 | TWOREASONS, COSPONSOR, FLOOR | After January 2028 only one of the two reasons can still happen. The case allows no money in or out before 2033 except the two deposits (case p.2), so "a missed deposit" can only occur in Jan 2028, b… | keep |
| 8 | Q9-016 | 23 | RESIDENCY, RESERVE2033, CERTAINTY | One-founder cultural institutions are fragile: private art museums that closed had been open a median of 10 years; closure was "usually related to financial difficulties, rather than the founder's de… | keep |
| 9 | Q9-020 | 23 | RESIDENCY, CERTAINTY, TWOREASONS, CAREER | Yaddo nearly ended before its first guest: after Spencer Trask died in 1909 "the Trasks' financial investments depreciated the following year, jeopardizing Yaddo's future"; Katrina Trask closed the m… | keep |
| 10 | Q9-022 | 23 | RESERVE2033, CERTAINTY, TWOREASONS | Even a large residency endowment can fall 15% in a year: MacDowell's went from $33.1M to $28.2M in 2022 (investment return -$5.6M, after +$7.0M in 2021), while it ran a $3.4M gap before investment re… | keep |
| 11 | Q9-033 | 23 | COSPONSOR, RESIDENCY | Taiwan's national arts grant-maker never got its endowment: the law set a NT$10bn fund to be reached within 10 years; government gave its NT$6bn share by 2003, but the NT$4bn private share was never … | keep |
| 12 | Q11a-004 | 22 | FLOOR, COSPONSOR | Seed money matters only when fixed costs are high: with a high fixed cost, giving in sequence raised the provision rate from 40% (simultaneous) to 76%; with a low fixed cost both were above 80% and "… | keep |
| 13 | Q11b-005 | 22 | COSPONSOR, RESIDENCY, MOVE2031 | MacDowell announced a $13 million campaign in Aug 2010 when "more than $10 million has already been raised", then said what it buys: a library center, endowed Fellowships "in perpetuity", and stipend… | keep |
| 14 | Q11b-014 | 22 | COSPONSOR, LAURA, RESIDENCY | Fogo Island Arts (Canada): Zita Cobb, who made her money in technology and returned home, "personally committed about $30 million of her own capital to build the Inn and the Fogo Island artist studio… | adapt |
| 15 | Q11b-022 | 22 | COSPONSOR, HALFKEPT, RESIDENCY | Kresge's arts program required "a building reserves policy" with every facility grant; a comprehensive campaign should include "transitional operating funding to help the organization adapt to higher… | adapt |
| 16 | Q11b-023 | 22 | COSPONSOR, RESERVE2033, RESIDENCY | NFF's evaluation of Kresge's 32 facility grantees (2010-12 grants): organisations did not plan "for the costs associated with operating new or expanded facilities"; "Many organizations do not plan fo… | keep |
| 17 | Q11b-026 | 22 | INFLATION_TWD, HALFKEPT, MOVE2031, RESIDENCY | Set in Stone (US cultural building 1994-2008, about $16 billion): "More than 80 percent of the projects studied ran over budget, some by as much as 200 percent"; theatres' end cost was about 92 perce… | keep |
| 18 | Q12-001 | 22 | CAREER, COMPLETE2028 | An advance is not one cheque: the model contract pays it "on the execution of this Agreement", "on acceptance of the complete manuscript" and "on Publisher's initial publication of the Work"; "paymen… | keep |
| 19 | Q12-004 | 22 | CAREER, COMPLETE2028 | In the 2020 shock the biggest publisher stretched payments rather than cancelling: Penguin Random House "lengthened the period of payment on the first installments of significant advances"; "While th… | keep |
| 20 | Q12-006 | 22 | CAREER, LAURA | In 2009 the cuts fell on new deals for midlist and new authors, not on proven sellers: "No one had said, 'let's go the extra £50,000'"; "Midlist authors will be squeezed again, perhaps dropped, while… | adapt |
| 21 | Q12-008 | 22 | CAREER, COMPLETE2028 | Royalties arrive twice a year, three months after each half: "Publisher shall prepare a statement of account semi-annually", paid "within three months following the end of the period". Keel arithmeti… | keep |
| 22 | Q12-015 | 22 | CAREER, LAURA | Children's books sell into two markets "and those markets do not cycle together"; institutional cuts "take time to take effect"; worked example: "If a publisher makes 60% of its sales in the institut… | keep |
| 23 | Q1b-001 | 22 | CAREER, COMPLETE2028 | Shares lead pay by about a year: the aggregate part of US earnings growth correlates 0.184 with the same year's share return and 0.372 with the previous year's (college 0.248 and 0.377; high school 0… | keep |
| 24 | Q1b-010 | 22 | CAREER, CERTAINTY | At the very top, pay and shares move together fast: "The co-movement of income growth for top earners with GDP growth and stock returns is quite striking. In fact, the correlation with all three seri… | keep |
| 25 | Q1b-021 | 22 | CAREER, LAURA | Writers' unemployment rose after the crash and peaked while shares rose: writers and authors 4.4% (Q4 2007), 6.6% (Q4 2008); annual 4.5% (2007), 6.4% (2008), 7.9% (2009), and 10.0% in Q4 2009, the ye… | keep |
| 26 | Q1b-026 | 22 | COMPLETE2028, FLOOR, CERTAINTY, CAREER | The deposit's market year is one in which the plan owns no shares (Keel inference): under the measured lag (rows 1, 4, 7), earnings in 2027 respond most to the 2026 share market and partly to 2027's.… | adapt |
| 27 | Q4b-016 | 22 | COSPONSOR, CAREER | Corporate giving follows profits, not share prices, and the previous year's profits at that. "Corporate giving is tied more closely to corporate profits than stock market performance". Giving as a sh… | adapt |
| 28 | Q4b-027 | 22 | COSPONSOR, HALFKEPT, RESIDENCY | ...but NCAF's grants ROSE that year. Grant expenses went from NT$153,598,721 (2014) to NT$160,462,639 (2015), +4.5%, and regular grants from NT$109,988,100 to NT$112,538,905, +2.3%. It ran a NT$54.7m… | keep |
| 29 | Q5-006 | 22 | HALFKEPT, INFLATION_TWD, COSPONSOR | In cost engineering a contingency is a narrow thing. It "usually excludes: a) Major scope changes such as changes in end product specification, capacities, building sizes, and location ...; b) Extrao… | adapt |
| 30 | Q5-011 | 22 | HALFKEPT, CERTAINTY, COSPONSOR | Flyvbjerg's 2004 guidance for UK transport: uplifts at 50% / 80% confidence, roads 15% / 32%, rail 40% / 57%, fixed links 23% / 55%. Who should use which: "the 50% percentile should be used only in i… | keep |
| 31 | Q5-012 | 22 | HALFKEPT, CERTAINTY, MOVE2031 | Updated reference classes (Table 5, international): Buildings ("Stations, depots, concert halls, office buildings, museums", n=149) mean / 50% certainty (RCF50) / 80% certainty (RCF80): full business… | adapt |
| 32 | Q5-016 | 22 | HALFKEPT, CERTAINTY | Denmark's 110 cultural buildings delivered 2000-2007 (DKK 5.8bn in all, average DKK 53m; 63 new, 47 repairs): 40% at or under the decision budget; 75% within +10%; to be 80% sure the budget holds add… | keep |
| 33 | Q5-018 | 22 | HALFKEPT, COSPONSOR, MOVE2031 | Norway's state project model gives the agency a P50 steering frame and sets the cost frame at P85; the difference is a reserve held by the ministry, not the project | keep |
| 34 | Q5-022 | 22 | HALFKEPT, INFLATION_TWD, MOVE2031 | Taiwan's public works manual: allowable cost variation (經費變動率) by stage, feasibility 15%-30%, comprehensive planning 10%-25%, basic design 3%-10%, detailed design 3%-5%; contingency (工程預備費) for major… | keep |
| 35 | Q5-023 | 22 | INFLATION_TWD, COSPONSOR | The same manual prices escalation (物價調整費) separately, from the average of the construction cost index (10 years in 2018; 3-10 years in the 2023 revision), and lists causes of cost change including ex… | keep |
| 36 | Q6-011 | 22 | CEILING, COSPONSOR | Ranked, the eight houses with a dated world-share figure are J.P. Morgan 7.5%, Aon 7.5%, Northern Trust 7.1%, AQR about 6.6%, Invesco 6.4%, Janus Henderson 6.2%, Capital Group 6.0% (20 years) and Van… | adapt |
| 37 | Q6-027 | 22 | CEILING, MOVE2031, COSPONSOR | In dollars, the forecast matters little and luck matters a lot. Assuming 4% instead of 10% for VT moves the top of the range only from $136,580 to $140,364 ($3,784). At a fixed 7.5%, the moved half r… | keep |
| 38 | Q6-030 | 22 | COSPONSOR, MOVE2031 | In 13,300+ forecasts by US finance chiefs over a ten-year panel, the realised one-year S&P 500 return fell inside their 80% confidence intervals only 36.3% of the time (59% even in the calmest quarte… | keep |
| 39 | Q7-008 | 22 | TWOREASONS, COSPONSOR, CERTAINTY | Lenders separate "excusable" default in "identifiably bad states of the world" from repudiation; "although sovereigns sometimes excusably default, they never repudiate their debts", because the long-… | keep |
| 40 | Q7-009 | 22 | TWOREASONS | A well-designed escape clause names "(i) a limited and clearly defined set of events triggering the operation of the clause, (ii) the authority to activate it, (iii) the timeline and procedures to re… | adapt |

## The thinnest parts (fewest ideas rated B or better)

- FUNDRAISING (The fundraising text): 18 rated B or better, 19 in all.
- RESIDENCY (The residency itself): 66 rated B or better, 67 in all.
- LAURA (Laura's working life and values): 72 rated B or better, 73 in all.
- PRESENTATION (How the report shows its work): 83 rated B or better, 84 in all.
- INFLATION_TWD (Inflation, Taiwan costs, the Taiwan dollar): 93 rated B or better, 100 in all.
- RESERVE2033 (The operating reserve from 2033): 116 rated B or better, 123 in all.
- OTHER (Other): 121 rated B or better, 145 in all.
- COMPLETE2028 (The 2028 deposit completes the ladder): 123 rated B or better, 133 in all.
