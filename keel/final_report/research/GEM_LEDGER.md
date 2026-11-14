# Gem ledger: where the store's strong ideas land in the Final Report

> **Second pass done the same day:** the other 862 tier-A ideas were read by hand in `gem2/` (summary in
> `gem2/README.md`): 445 carried, 390 out with a reason, 8 must land (now in SKELETON), 19 may land.

Sat 14 Nov 2026. Planning notes, not report text. Caplet asked today for proof that no strong insight is lost: "Every
single thing you research is something that should end up in the Final Report if it's good." This file checks each
strong idea in the insight store against the report plan, and names the ones that are at risk.

**Method.** I rebuilt the store in a scratch copy (the repo's store files were not touched) and took every tier-A idea
(score 19 or more out of 25, status keep or adapt): 1,186 ideas. That is 12 fewer than the store's front page
shows, because 29 later judgements of card Q5e are in `ratings.csv` but not yet built in. A script mapped each idea to the
report part its tags and SKELETON's notes point to. It then searched SKELETON (version of Sat 14 Nov morning) for the
idea's row id, names, distinctive figures and wording. The search kept four zones apart: the density-cut table that
governs, that table's "cut" column, the older reservoir rows and the exhibits. Finally I read by hand every idea scoring
22 or more (179) and every judged 21 that the search had not found (74), 253 ideas in all.
Each got one of three verdicts: landed, not carried with a recorded reason, or at risk.

## What it shows

- Of the 253 strongest ideas, **130 are landed** and **84 are out for a written
  reason**. The reasons are SKELETON's own density cut (22), a duplicate of a landed row (32), a rule already applied or
  too small for the space (17), the frozen IPS (5), a void figure (5), the case's scope (2) and the reflection's event
  pool (1). **39 are at risk**: strong, consistent with the IPS, and in no line of SKELETON. Twelve of
  the 39 are high priority.
- **The largest loss is a hand-off.** Panel 2's density cut moved the career test ("2009 and 2020") out of 2.3 "to 3e".
  On Friday evening 3e's density row was rewritten around the case's five assumption areas, and the test was dropped.
  It now sits only in the superseded long rows. So the IPS's opening thesis (IPS l.3, l.9) has no tested limit in the
  plan that governs.
- **3e (assumptions and limits) is the thinnest part against its evidence.** It holds 17 of the 39
  at-risk ideas. SKELETON never cites card Q12 (Laura's working life, 57 rows across Q12 and Q12b).
- **849 tier-A ideas were not read by hand, and the search found no trace of them in SKELETON.** 528
  have never been judged: their tier A comes from the first-pass formula, and 482 of them are harvest rows from before
  the IPS. The other 321 were judged, almost all at 19 or 20, and 59 of those carry a note marking a void or corrected
  figure. A report of about
  2,500 words cannot print most of them. They are carried only where a landed row makes the same point. Section 3 lists
  those that looked strongest on a skim.

## 1. By report part

| Part | Tier-A ideas | Landed | Not carried, reason recorded | At risk (should land) | Not reviewed by hand, not found in SKELETON |
|---|---|---|---|---|---|
| Section 2: Portfolio Implementation (2.0-2.5, Table 1) | 128 | 16 | 11 | 2 | 99 |
| 3a: ten-year commitment and operating reserve (Figure 1) | 242 | 41 | 17 | 8 | 176 |
| 3b: facility contribution and flexibility | 238 | 58 | 26 | 8 | 146 |
| 3c: 2031 range and confidence (Table 2) | 146 | 21 | 7 | 1 | 117 |
| 3d: words for co-sponsors | 158 | 26 | 15 | 2 | 115 |
| 3e: assumptions and limits | 69 | 8 | 10 | 17 | 34 |
| 3e: monitoring (Table 3) | 106 | 30 | 2 | 1 | 73 |
| 3f: Team Reflection | 63 | 6 | 1 | 0 | 56 |
| Exhibits and form | 27 | 3 | 0 | 0 | 24 |
| Other (no part) | 9 | 0 | 0 | 0 | 9 |
| **All** | **1186** | **209** | **89** | **39** | **849** |

Parts follow SKELETON. For an idea read by hand, the part is my call; for the rest it comes from the idea's tags. For
unreviewed ideas the "landed" figure is the search's own call, which held up about seven times in ten in a sample
check, so read it as an upper bound. "Not carried, reason recorded" also includes 5 unreviewed ideas the search found
only in SKELETON's cut column.

## 2. At risk: strong ideas SKELETON does not carry

### 2a. Should land (39), with the line SKELETON needs

Rows that share one clause point to the first row of their group, so one edit lands several. "Edit n" refers to
section 4. Priority is mine: high means the idea answers something Wharton requires or guards a named failure in
INTENT.

| # | Id | Score | Priority | The idea, in one sentence | Source | Part | The line SKELETON needs |
|---|---|---|---|---|---|---|---|
| 1 | Q1c-005 | 22 | high | On tax data, arts sole proprietors' receipts fell 11.6% in 2009, the year after the crash, while shares rose 26%. | `Q1c_career_and_diversification.md` | 3e | Edit 1: the career test, one clause in 3e's limits. The 2.3 density cut sent it 'to 3e'; the Fri 13 Nov rewrite of 3e's density row dropped it. |
| 2 | Q1c-010 | 22 (adapt) | high | Writers' and artists' business receipts fell 12.4% in 2020 while shares rose 18%, so her career and shares fall in the same downturn, not always in the same months. | `Q1c_career_and_diversification.md` | 3e | Same clause as Q1c-005. |
| 3 | Q12-018 | 23 (adapt) | high | Laura's own genre, graphic novels, rose 29% in 2020 and fell about a third over 2023-24 while shares boomed, so her career has a cycle of its own too. | `Q12_lauras_working_life.md` | 3e | Same clause, as the case-specific example of '2020 does not' (the case calls her a graphic novelist). Adapt: a limit, never 'her career moves against shares'. |
| 4 | Q1b-002 | 23 (adapt) | high | An average college graduate's career is less than a fifth share-like, so the IPS's thesis rests on Laura not being average: self-employed, paid in advances and fees, at the top of a hit-driven field. | `Q1b_career_beta_horizon.md` | 3e | Same clause: the condition under which IPS l.3's thesis holds. Adapt: never 'her career is not share-like' (CANON A1). |
| 5 | Q1b-010 | 22 | high | For the very top earners, income moves with GDP and shares (correlations above 0.6). | `Q1b_career_beta_horizon.md` | 3e | Same clause, paired with Q1b-002: weak link for the average graduate, strong for top earners. |
| 6 | Q6-011 | 22 (adapt) | high | J.P. Morgan's 7.5% for world shares is the top of eight houses' dated forecasts, which run from about 6% to 7.5% (median about 6.5%). | `Q6_how_far_to_trust_7_5.md` | 3e | Edit 2: 3e area (1) says '7.5% a year (J.P. Morgan 2027), the top of published forecasts of about 6% to 7.5%', then the 4%-10% test. Adapt: never say the Trading Notes quoted the most optimistic house. |
| 7 | Q6-030 | 22 | high | Finance chiefs' 80% ranges for the next year's market caught the outcome only 36% of the time; experts' ranges run about a third as wide as reality. | `Q6_how_far_to_trust_7_5.md` | 3c | Edit 3: one clause in 3c. Forecast ranges miss, so Laura's range is built from money she will own, not from a forecast (Ben-David, Graham and Harvey 2013). This gives INTENT's 'biggest strength' its evidence. |
| 8 | Q16-020 | 22 | high | A state lottery that pays fixed yearly prizes buys extra bonds 'to hold in reserve' against reinvestment risk. | `Q16_operating_reserve_mechanics.md` | 3a | Edit 4: one clause beside the extra Treasuries. A public payer of fixed prizes buys reserve bonds against reinvestment risk on purpose (California State Lottery 2025, s.VI), so the extra Treasuries read as practice, not a patch (INTENT failure 7). |
| 9 | Q16-018 | 23 | high | The same lottery's written policy is the IPS's rule: investments mature 'immediately prior' to each prize date and are held to maturity. | `Q16_operating_reserve_mechanics.md` | 3a | Same clause as Q16-020, one source (s.III). |
| 10 | Q9-009 | 22 | high | The cultural field's own first rule of capital is reserves before buildings: operating reserves 'should be an organization's first capitalization priority'. | `Q9_what_makes_a_residency_last.md` | 3a | Edit 5: 3a's evidence for Wharton's 'how your strategy supports the ten-year operating commitment'. One clause; Keel's pick of rows E, since it states the plan's order in the field's words (NFF and Helicon 2014). |
| 11 | Q9-016 | 23 | high | Founder-led private art museums that closed lasted a median of ten years and closed for lack of money, not because the founder died. | `Q9_what_makes_a_residency_last.md` | 3a | Same slot as Q9-009 (the alternative). Say that 2043 on is outside the plan. |
| 12 | Q9-013 | 22 | med | The median US arts group holds about 1.5 months of working capital, while Laura's $50,000 a year is owned ten years ahead (her share, not the residency's whole budget). | `Q9_what_makes_a_residency_last.md` | 3a | Same slot, or 3d if the funder reader wants scale. |
| 13 | Q11b-023 | 22 | low | An evaluation of 32 arts groups that built with Kresge grants found many did not plan or set aside reserves for the new building's running costs. | `Q11b_real_case_statements.md` | 3a | Same slot (the alternative); store if Q9-009 is used. |
| 14 | Q7-030 | 21 | high | Buying the floor in January 2028 rather than 2031 gives up about $7,400 at the middle but avoids the rival's roughly one chance in six of facing the 2031 meetings with less than $95,000 (NUMBERS 8c). | `Q7_precommitment_and_rules.md` | 3b | Edit 6: 3b's 'what the shares buy and cost' sentence, or 3f as a decision tested and kept. Use NUMBERS 8c's figures; this row's own figures are void ($110,000 bottom). No density row carries 8c. |
| 15 | Q11a-025 | 24 | med | Groups of funders nearly always reach a target they know and nearly always fail one they are unsure of (18 of 20 groups against none, in the lab). | `Q11a_funders_seed_assurance.md` | 3d | Edit 7: 3d fix (1), one total and one close date, gets its reason in a half-clause (Barrett and Dannenberg 2012). The owned bottom and a total set before 2031 give co-sponsors a known target. |
| 16 | Q5-018 | 22 | med | Norway's state projects give builders a median budget while the ministry holds the reserve above it, the same design as money 'promised to no one'. | `Q5_is_half_right.md` | 3b | Edit 9: in place of the optional Arrow and Fisher clause, the owner-held reserve in practice (Ministry of Finance circular R-108/2025). |
| 17 | Q5-023 | 22 | med | Taiwan's public-works costing manual lists exchange-rate moves and fundraising among the causes of cost change, and prices inflation on its own line. | `Q5_is_half_right.md` | 3b | Edit 9: one clause beside the three uses. Taiwan's own costing manual names two of the IPS's three uses (Public Construction Commission 2018, ch. 4). |
| 18 | Q5c-021 | 22 | low | NASA commits to Congress at 70% confidence and holds its reserve above the project, not inside it. | `Q5c_option_value_and_last_dollar.md` | 3b | Alternative to Q5-018 for the same clause. |
| 19 | Q5c-011 | 24 | low | A fixed minimum with full freedom above it is the best simple rule when you want commitment but expect news (Amador, Werning and Angeletos 2006). | `Q5c_option_value_and_last_dollar.md` | 3b | The theory form of the same clause, if theory is wanted over practice. Never 'optimal' (SKELETON 3b). |
| 20 | Q5-006 | 22 (adapt) | low | In cost engineers' terms the half kept is a management reserve held by the owner, not a contingency the builder expects to spend. | `Q5_is_half_right.md` | 3b | A word for 3b's clause, not a sentence. Adapt: the IPS gives one pot three jobs, which engineers price apart; never call it a 'contingency'. |
| 21 | Q16-006 | 22 | med | The three iBond Treasury funds that have already ended (2023, 2024, 2025) each paid cash 10 to 14 days before 1 January. | `Q16_operating_reserve_mechanics.md` | 3a | 3a's liquidity clause or Figure 1's note: 'every one so far', after checking BlackRock's count of terminations (card note). |
| 22 | Q16-008 | 22 | med | IBTF, a fund that has ended, returned 1.15% a year against a 1.16% five-year yield on its launch day, after a -6.4% year. | `Q16_operating_reserve_mechanics.md` | 2 | 2.2 or 3a, one clause: proof of the Trading Notes' 'behave a lot like bonds when held to their end'. WInS price moves stay noise. |
| 23 | Q17-010 | 22 | low | Before zero-coupon Treasuries existed (1985), a ladder of coupon bonds could not be a certain match, because the interest arrives early and must be reinvested. | `Q17_judging_the_implementation.md` | 3a | 3a's evidence clause: why reinvested interest needs help, said neutrally (coupon bonds pay interest early); never as blame on Wharton's rules. |
| 24 | Q15-009 | 23 | med | Pension schemes that de-risk on triggers never move back into shares after a fall. | `Q15_monitoring_and_triggers.md` | 3e | 3e's 'why only these two' clause or Table 3's note: professional de-risking is one-way, the practice behind 'a fall in the market is not one of them' and the fixed 2031 move. |
| 25 | Q7-008 | 22 | med | A shortfall from a US default would be excusable (public, shared by every holder), while one after a market fall would look like a broken promise, because the IPS ruled market falls out in advance. | `Q7_precommitment_and_rules.md` | 3e | 3e's 'why only these two', half a clause (Grossman and Van Huyck 1988), for the default only: a missed deposit is private. |
| 26 | Q15-015 | 22 | low | The one US late payment on record (1979) was a back-office delay of under three weeks on paper checks; book-entry holders, as Laura is, were unaffected. | `Q15_monitoring_and_triggers.md` | T3 | Table 3's note on row 2, or 3e's default clause beside the credit-default-swap figure. |
| 27 | Q12-001 | 22 | med | Book advances are paid in three to five instalments over years, so only some can reach a January 2028 deposit. | `Q12_lauras_working_life.md` | 3e | Edit 8: 3e area (2), one clause. The deposit comes from income paid on contract dates, which a downturn delays first, so Table 3 row 1 asks for written confirmation by 1 December 2027. SKELETON never cites card Q12. |
| 28 | Q12-004 | 22 | med | In 2020 the largest publisher stretched advance instalments rather than cancel them, so a shock reaches authors as delay first. | `Q12_lauras_working_life.md` | 3e | Same clause as Q12-001. |
| 29 | Q12-008 | 22 | med | Royalties arrive twice a year, about three months after each half, so sales after mid-2027 are paid after the deposit date. | `Q12_lauras_working_life.md` | 3e | Same clause as Q12-001. |
| 30 | Q12-034 | 21 | low | Graphic novelists earn about half their author income outside books, from the streams that fall most and latest. | `Q12_lauras_working_life.md` | 2 | Same clause, or 2.3 if room: the case's own list of her income (advances, speaking, licensing). |
| 31 | Q12-015 | 22 | low | Children's books sell to shops that hold up and to schools whose budgets fall late, and the case says her books are read in classrooms. | `Q12_lauras_working_life.md` | 3e | Same clause; store if no room. |
| 32 | Q12-024 | 21 | low | School visits are often a children's author's main income outside books, and schools were already booking fewer. | `Q12_lauras_working_life.md` | 3e | Same clause; store if no room. |
| 33 | Q9-033 | 23 | low | The private NT$4bn half of Taiwan's national arts fund, required by law, was never raised; the fund is still under 70% of its target. | `Q9_what_makes_a_residency_last.md` | 3e | 3e area (3), one clause: in Taiwan even private money promised in law did not arrive, which is why only owned money is in Laura's figures. |
| 34 | Q9-029 | 22 | low | Taichung's national theatre raised 59% of its sponsorship target in 2017, so a co-sponsor falling short is normal in Taiwan, even for a national venue. | `Q9_what_makes_a_residency_last.md` | 3e | 3e area (3), or 3b's third use, if room. |
| 35 | Q11b-014 | 22 (adapt) | low | At Fogo Island Arts a founder from elsewhere put her own capital in first, and two governments followed with $5 million each. | `Q11b_real_case_statements.md` | 3b | 3b, beside the evidence sentence, if an example is wanted; give one dated figure or none (the sources conflict). |
| 36 | Q9-005 | 22 | low | Arts groups that came through a new building were the ones that stayed flexible and realistic about revenue after opening. | `Q9_what_makes_a_residency_last.md` | 3b | 3b: field evidence for the case's own warning that committing all remaining assets could limit her flexibility (Set in Stone 2012); store if no room. |
| 37 | Q2b-008 | 22 | low | After Illinois's prize delays, the payer's fix was a standing authority; Laura's equivalent is a standing instruction with her custodian for the ten January transfers. | `Q2b_escrows_lotteries_settlements_stress.md` | 3e | 3e's custody line: name the standing instruction adopted on Thu 12 Nov (ASK_HUMANS), which SKELETON does not mention. |
| 38 | Q10-001 | 21 | low | J.P. Morgan's 2027 edition puts long-run US inflation at 2.4% a year, in the same edition as the 7.5%. | `Q10_inflation_inputs.md` | 3e | 3e area (4): name it only if a figure in today's money is printed. |
| 39 | Q11b-002 | 21 | low | Fundraising teaching says a case that leads with money ('we need a building') is 'not a convincing case expression'; it leads with the mission. | `Q11b_real_case_statements.md` | 3d | 3d: a challenge to the settled order. Test with the next funder reader whether one clause of purpose before the ten owned years helps. |

**Words.** Each addition is a clause, and SKELETON's rule is that a part needing more words takes them from another
part by name. Edits 1 to 9 add about 150 to 200 words. Section 3's measured ceiling leaves about 60 words spare (Thu 12
Nov), so each addition needs a named trade. The obvious sources are figures already sent to exhibit notes.

### 2b. Not carried, with a recorded reason (84)

| Id | Score | The idea, in one sentence | Source | Part | Verdict | Reason |
|---|---|---|---|---|---|---|
| Q20-020 | 24 | The escrow verifier's test, 'sufficient, without further reinvestment', is the professional name for 3a's standard. | `Q20_pooled_book_or_margin.md` | 3a | Cut by SKELETON | SKELETON density cut: MSRB's 'full cash' name lost the finalist judge; never 'sufficient without reinvestment'. The standard itself lands in 3a. |
| Q25-001 | 24 | Receivers rate a broken promise 8.32, a kept one 9.88 and an exceeded one 9.77 (out of 11). | `Q25_what_returns_to_laura.md` | 3b | Cut by SKELETON | SKELETON density cut: Gneezy and Epley's point goes to 3d's 'never offered'. |
| Q11b-032 | 24 | The profession's counting standard (CASE) counts a conditional pledge only once its conditions will be met. | `Q11b_real_case_statements.md` | 3d | Duplicate | Duplicate of Q32-020 (Kresge counts only written pledges or cash), landed in 3d. CASE could replace Kresge if a profession-wide rule reads better. |
| Q5-014 | 24 | England's housing agency's overrun classes: low-risk buildings P50 4%, P80 32%. | `Q5_is_half_right.md` | 3b | Duplicate | 3b's overrun illustration uses card Q5d's classes; one class is enough. |
| Q10-025 | 23 | A return of the Taiwan dollar to its 10-year strongest would raise a fixed NT$ budget by 19.1% in US dollars ($21,000-$26,000). | `Q10_inflation_inputs.md` | 3b | Cut by SKELETON | SKELETON density cut: 3b keeps one currency figure (the 10% test, about 93 in 100). |
| Q10b-001 | 23 | A 10% rise in the US-dollar cost of a NT$ budget over two years came in about 9% of windows since 2001. | `Q10b_taiwan_dollar_2025_and_insurers.md` | 3b | Cut by SKELETON | Same as Q10-025. |
| Q17-008 | 23 | Moody's two escrow tests (maturities before each payment; enough without reinvestment) applied to the book. | `Q17_judging_the_implementation.md` | 3a | Cut by SKELETON | Same as Q20-020; the card asks to merge the two. |
| Q5e-029 | 23 | The part of her flexibility that does not move with shares is the excess above the stated top. | `Q5e_does_the_reserve_fall_with_its_uses.md` | 3b | Duplicate | Carried by 3b's two named parts of what she keeps. |
| Q9-020 | 23 | Yaddo nearly closed before its first guest when its founders' investments fell. | `Q9_what_makes_a_residency_last.md` | 3a | Duplicate | An anecdote in the same slot as Q9-016 (at risk); one evidence clause. |
| Q31-015 | 23 | A 2% surgical risk remembered as 10% is informed consent; remembered as 0% it is not. | `Q31_escrow_standard_plain_words.md` | 3a | Too small, or a rule already applied | A wording rule, already applied: the exception travels inside 3a's sentence. |
| Q9-022 | 23 | MacDowell's endowment fell 15% in 2022 while it ran a deficit. | `Q9_what_makes_a_residency_last.md` | T3 | Too small, or a rule already applied | Too small: 3e's argument is structural (a market fall moves a number inside the design). |
| Q4b-001 | 23 | US foundation giving rose 5.4% in 2008 while foundation assets fell 17.2%. | `Q4b_cosponsors_in_downturns.md` | 3e | Conflicts with the frozen IPS | Cuts against IPS l.9's 'co-sponsors cut their budgets' (CANON B4). Store. |
| Q17-025 | 23 | The team rejected an all-bond WInS book so the book would show the whole strategy. | `Q17_judging_the_implementation.md` | 3f | Carried elsewhere | Carried by the Team Reflection's event pool (research/experience/candidates_W.md l.376) and by 2.1's reason. |
| Q15-006 | 22 | A municipal defeasance escrow is irrevocable; Laura's separation of her money is her own policy, not law. | `Q15_monitoring_and_triggers.md` | 3e | Cut by SKELETON | SKELETON 3e keeps it in the store, not the report. |
| Q17-013 | 22 | New York Regulation 126 tests seven rate scenarios, including an immediate 3-point fall. | `Q17_judging_the_implementation.md` | 3a | Cut by SKELETON | SKELETON density cut (the finalist was lost on it). |
| Q1b-001 | 22 | Shares lead pay by about a year (earnings correlate 0.37 with last year's market, 0.18 with this year's). | `Q1b_career_beta_horizon.md` | 2 | Cut by SKELETON | SKELETON 2.3: 'never a lag rule or a beta'. |
| Q1b-021 | 22 | Writers' unemployment peaked one to two years after the share low, in two recessions. | `Q1b_career_beta_horizon.md` | 2 | Cut by SKELETON | Same as Q1b-001. |
| Q1c-029 | 22 | Leibowitz (1986): a dedicated portfolio is the 'least-risk asset' for nominal-dollar liabilities. | `Q1c_career_and_diversification.md` | 2 | Cut by SKELETON | SKELETON density cut: one citation in 2.3 is enough. |
| Q25-003 | 22 | Exceeding an expectation is rewarded; exceeding a promise is not. | `Q25_what_returns_to_laura.md` | 3d | Cut by SKELETON | Same as Q25-001. |
| Q4c-020 | 22 | Readers agree with a stated scale 40 times in 100 on words alone and 75 on numbers. | `Q4c_how_sure_words_and_numbers.md` | 3c | Cut by SKELETON | SKELETON density cut: the decision stays (no likelihood word), the evidence goes. |
| Q5d-025 | 22 | A Taiwan heritage roof repair overran by 22.47% once the roof came off. | `Q5d_small_arts_buildings_overruns.md` | 3b | Cut by SKELETON | Store only by the card's own call (density cut; no NUMBERS entry). |
| Q11a-004 | 22 | Seed money matters only when fixed costs are high, as a building's are. | `Q11a_funders_seed_assurance.md` | 3b | Duplicate | Carried by 3b's landed Q11a clause (an announced first gift raised others' giving). |
| Q11b-026 | 22 | More than 80% of US cultural buildings ran over budget (Set in Stone). | `Q11b_real_case_statements.md` | 3b | Duplicate | 3b's overrun base rate is carried by England's arts lottery (Q5d-006, landed). |
| Q15-004 | 22 | Insurers' matching rules let a bond book change only when its cash flows change. | `Q15_monitoring_and_triggers.md` | T3 | Duplicate | Carried by Q3b-034 (the two reasons are the only two flows not owned), landed; an iBond rung pays net asset value, so the analogy is loose. |
| Q16-038 | 22 | To funders an 'operating reserve' means months of expenses for emergencies. | `Q16_operating_reserve_mechanics.md` | 3a | Duplicate | 3a defines the term at first use; the funders' meaning belongs in WORDS.md. |
| Q18-024 | 22 | Once outcomes are known, calibration beats confidence. | `Q18_pledges_and_stated_confidence.md` | 3c | Duplicate | 3c states each end below what the funds will pay; the evidence (Gneezy and Epley's family) was cut. |
| Q5-012 | 22 | UK reference classes for buildings: 50% certainty 13%, 80% certainty 84%. | `Q5_is_half_right.md` | 3b | Duplicate | Same as Q5-014. |
| Q5-016 | 22 | Denmark's 110 cultural buildings: to be 80% sure add 13%, for 90% about 28%. | `Q5_is_half_right.md` | 3b | Duplicate | Same as Q5-014. |
| Q7-022 | 22 | UK pension law's 'low dependency' end state describes the ladder from 2027 and the floor from 2028. | `Q7_precommitment_and_rules.md` | 3a | Duplicate | The pension frame is carried by card Q2a in 3a. |
| Q7-023 | 22 | In the regulator's terms Laura's plan is stepped de-risking, and her 'reliability period' ends in January 2028. | `Q7_precommitment_and_rules.md` | 3b | Duplicate | 3b names the design once (Perold and Sharpe's buy-and-hold); one name is enough. |
| Q7-026 | 22 | The ladder and floor work like a home-made pension buy-in, with Treasuries in place of an insurer. | `Q7_precommitment_and_rules.md` | 3b | Duplicate | Same as Q7-023. |
| Q7-029 | 22 | Dutch pension funds that cut promises after 2008 lost trust: promise firmly only what cannot bend. | `Q7_precommitment_and_rules.md` | 3d | Duplicate | Carried by 3d's 'co-sponsors count the bottom' (card Q35). |
| Q9-010 | 22 | Capital not held apart gets spent on deficits, so the half kept protects only while named. | `Q9_what_makes_a_residency_last.md` | 3b | Duplicate | 3b and 3d both name the half kept and its uses. |
| Q11b-005 | 22 | MacDowell announced its campaign with 77% already in hand. | `Q11b_real_case_statements.md` | 3d | Too small, or a rule already applied | A model for 3d's order, already applied. |
| Q11b-022 | 22 | Kresge required a building reserves policy with every facility grant. | `Q11b_real_case_statements.md` | 3d | Too small, or a rule already applied | 3d already leads with the ten owned years. |
| Q18-003 | 22 | Ambiguous pledge wording is presumed conditional. | `Q18_pledges_and_stated_confidence.md` | 3d | Too small, or a rule already applied | A wording rule, applied: 3d states the bottom unconditionally, on its own. |
| Q18-026 | 22 | Securities law's form for a forward figure: label it and name the factors that could move it. | `Q18_pledges_and_stated_confidence.md` | 3c | Too small, or a rule already applied | The shape Wharton asks for, applied in 3c. |
| Q19-025 | 22 | Outcomes inside a range, even at its edge, are judged correct. | `Q19_range_rule_and_confidence.md` | 3c | Too small, or a rule already applied | Store: 3c's 'why state a bottom' clause carries the point. |
| Q19-027 | 22 | One-sided statements imply a direction ('more than 100' against 'less than 200'). | `Q19_range_rule_and_confidence.md` | 3d | Too small, or a rule already applied | A wording rule, applied (both ends labelled). |
| Q22-026 | 22 | Artpace's founder text gives the building, twelve years of operations, then a dated end. | `Q22_cosponsor_words_checklist.md` | 3d | Too small, or a rule already applied | A model for 3d, already applied (dated to 2042). |
| Q22-037 | 22 | Real opening paragraphs that state committed money run about 75-125 words. | `Q22_cosponsor_words_checklist.md` | 3d | Too small, or a rule already applied | A budget check, already applied. |
| Q4b-027 | 22 | Taiwan's national arts foundation drew on money set aside to keep grants rising in a bad year. | `Q4b_cosponsors_in_downturns.md` | 3b | Too small, or a rule already applied | An analogy on the funder's side; no room in 3b. |
| Q5-011 | 22 | For a stand-alone pledge, use an 80-90% confidence level, not 50%. | `Q5_is_half_right.md` | 3c | Too small, or a rule already applied | 3c's confidence already exceeds it; store. |
| Q5-022 | 22 | Taiwan's manual lets a feasibility-stage estimate move by up to 30%. | `Q5_is_half_right.md` | 3b | Too small, or a rule already applied | 3b has its Taiwan clause; facility cost estimates are out of scope. |
| Q5d-014 | 22 | The owner's own changes are the largest cause of overruns (about 55%). | `Q5d_small_arts_buildings_overruns.md` | 3b | Too small, or a rule already applied | Store and defence by the card's own call. |
| Q9-026 | 22 | Weiwuying, Kaohsiung's national arts centre, ran 28.64% over and more than seven years late. | `Q9_what_makes_a_residency_last.md` | 3b | Too small, or a rule already applied | The wrong reference class (a national venue); card Q5d's small-building classes carry 3b. |
| Q9-004 | 22 | A new building's lasting cost to a residency is the running cost it adds every year. | `Q9_what_makes_a_residency_last.md` | 3d | Out of scope | Facility cost estimates are out of scope (case); 3d's yearly programme ask covers it. |
| Q12-006 | 22 | In 2009 the cuts fell on midlist and new authors, not on proven sellers. | `Q12_lauras_working_life.md` | 2 | Conflicts with the frozen IPS | Weakens IPS l.9's 'smaller' for a bestselling author (CANON B4: PARTLY). Store; never print against the IPS. |
| Q4b-016 | 22 | Corporate giving follows last year's profits, not share prices. | `Q4b_cosponsors_in_downturns.md` | 3e | Conflicts with the frozen IPS | A timing clash with IPS l.9's 'during that same period'. Store. |
| Q10b-021 | 21 | Taiwan insurers' currency hedge ratios are at a record low, so another sudden move stays possible. | `Q10b_taiwan_dollar_2025_and_insurers.md` | 3e | Cut by SKELETON | Store only by the card's own call; never in Table 3. |
| Q11a-031 | 21 | Numeric ranges cost little trust; vague words cost more (n = 5,780). | `Q11a_funders_seed_assurance.md` | 3c | Cut by SKELETON | Same as Q4c-020. |
| Q17-014 | 21 | The ladder's interest-rate hedge ratio is $234/$300, about 78%, while cash on dates is matched 100%. | `Q17_judging_the_implementation.md` | 2 | Cut by SKELETON | SKELETON density cut: duration figures leave Section 2 (CANON C12 keeps them for questions). |
| Q18-020 | 21 | Numbers cut trust far less than words (d = -0.15 against -0.55). | `Q18_pledges_and_stated_confidence.md` | 3c | Cut by SKELETON | Same as Q4c-020. |
| Q1b-007 | 21 | Worker betas are measured on last year's share return; top earners lose most the following year. | `Q1b_career_beta_horizon.md` | 2 | Cut by SKELETON | Same as Q1b-001. |
| Q31-003 | 21 | A 'full cash or gross refunding' is the exact name of Caplet's no-interest test. | `Q31_escrow_standard_plain_words.md` | 3a | Cut by SKELETON | Same as Q20-020. |
| Q4b-011 | 21 | Foundations cut payouts more after losses than they raise them after gains; founder-family foundations cut most. | `Q4b_cosponsors_in_downturns.md` | 3e | Cut by SKELETON | SKELETON density cut: Q11c's pledges releasing together, beyond one clause. |
| Q5e-003 | 21 | Over Laura's two-year windows the link between shares and building costs is about nothing. | `Q5e_does_the_reserve_fall_with_its_uses.md` | 3b | Cut by SKELETON | Store and defence by the card's own call. |
| Q5e-011 | 21 | Taiwan's public works contracts pass building-cost index rises during the build to the owner. | `Q5e_does_the_reserve_fall_with_its_uses.md` | 3b | Cut by SKELETON | Same as Q5e-003. |
| H9-013 | 21 | Arts giving fell hardest in the 2008-09 recession. | `H9_doc_research_tabs.md` | 3e | Duplicate | Corrected and carried by card Q4b. |
| Q1-016 | 21 | Earnings sensitivity to GDP is U-shaped in income (3.70 at the very top). | `Q1_career_as_shares.md` | 2 | Duplicate | Corrected and carried by card Q1b. |
| Q11a-013 | 21 | Leading by example works only when followers cannot see the project's value. | `Q11a_funders_seed_assurance.md` | 3b | Duplicate | Carried by 3b's landed Levati clause. |
| Q16-019 | 21 | The same lottery holds every security to maturity by rule. | `Q16_operating_reserve_mechanics.md` | 3a | Duplicate | Same source as Q16-018 (at risk); one citation. |
| Q18-008 | 21 | Facility funders sort money as committed, pledged or projected. | `Q18_pledges_and_stated_confidence.md` | 3d | Duplicate | Duplicate of Q32-020, landed in 3d. |
| Q18-019 | 21 | A $20m lead pledge collapsed when its form changed after a state match relied on it. | `Q18_pledges_and_stated_confidence.md` | 3d | Duplicate | 3d states one date and one form. |
| Q18-034 | 21 | An author's founder money opened a writers' residency campaign as one exact sum. | `Q18_pledges_and_stated_confidence.md` | 3d | Duplicate | 3d's 'one figure to count'. |
| Q1b-012 | 21 | Top-1% incomes have been 2.4 times as cyclical as average. | `Q1b_career_beta_horizon.md` | 2 | Duplicate | Carried by Q1b-010 (at risk). |
| Q1b-013 | 21 | The broad market is a poor hedge for ordinary jobs, yet a 0.2 correlation halves the gain from shares. | `Q1b_career_beta_horizon.md` | 2 | Duplicate | Carried by 2.3's 'every source says fewer shares, not none' (card Q33). |
| Q4b-033 | 21 | The half kept is hit first and recovers first; co-sponsor cuts come one to three years later. | `Q4b_cosponsors_in_downturns.md` | 3e | Duplicate | Carried by Q5e-028, 'the uses take turns'. |
| Q5-032 | 21 | The three named uses together could need about twice the middle-case half kept. | `Q5_is_half_right.md` | 3b | Duplicate | 3e area (5)'s 'the uses take turns' (Q5e-028, landed) answers it; printing the sum would read as IPS l.15 undersized. |
| Q5c-001 | 21 | Waiting is worth something only because bad news may come. | `Q5c_option_value_and_last_dollar.md` | 3b | Duplicate | Same family as Arrow and Fisher (optional in 3b). |
| Q5c-007 | 21 | Venture capitalists never commit all the money a company will need. | `Q5c_option_value_and_last_dollar.md` | 3b | Duplicate | Carried by 3b's Klein clause (keep the rest unpromised). |
| Q6-004 | 21 | Three consultants put world shares 2.25 points apart in the same month. | `Q6_how_far_to_trust_7_5.md` | 3e | Duplicate | Carried by Q6-011 (at risk). |
| Q7-007 | 21 | An escape clause keeps credibility only if outsiders can verify the event. | `Q7_precommitment_and_rules.md` | 3e | Duplicate | Carried by Q7-008 (at risk). |
| Q9-002 | 21 | Black Mountain College died of running costs paid by borrowing. | `Q9_what_makes_a_residency_last.md` | 3a | Duplicate | Same slot as Q9-016. |
| Q17-003 | 21 | For bonds, interest-rate moves are most of the cost of execution. | `Q17_judging_the_implementation.md` | 2 | Too small, or a rule already applied | Too small for 2.5's 150 words. |
| Q31-014 | 21 | Adults judge catastrophic risks as safe or risky, nothing in between. | `Q31_escrow_standard_plain_words.md` | 3a | Too small, or a rule already applied | Same as Q31-015. |
| Q5-021 | 21 | Building estimates grow by about half from a project's first mention. | `Q5_is_half_right.md` | 3b | Out of scope | Facility cost estimating is out of scope (case). |
| Q12-019 | 21 | School book budgets fell hardest three to four years after the crash. | `Q12_lauras_working_life.md` | 2 | Conflicts with the frozen IPS | Same timing clash; textbook sales, not author income. Store. |
| Q4b-019 | 21 | UK business money for culture fell four years running after 2008, while trusts rose. | `Q4b_cosponsors_in_downturns.md` | 3e | Conflicts with the frozen IPS | Same timing clash; press reports. Store. |
| H2-033 | 21 | iBond funds hold cash in their last months, which an interest-only reinvestment rule misses. | `H2_idea_bank_part2_and_ledger.md` | 3a | Void figure | Its figures are void (NUMBERS section 6); the point is carried by the no-interest standard. |
| H4-014 | 21 | About 1.00 times cover is right for bought cash flows; buffers exist for unmatched risk. | `H4_synergies_S1_S3_fusions.md` | 3a | Void figure | Void figures (cover 102%). |
| H4-028 | 21 | Ricardo: a sinking fund works only if it comes from a real surplus; ask of every dollar whether it exists. | `H4_synergies_S1_S3_fusions.md` | 3a | Void figure | Void figures; the idea is the governing thought, landed. |
| H7-028 | 21 | Laura's balance sheet is levered: her fixed payments are debt in front of the facility money. | `H7_final_night_reading.md` | 3b | Void figure | Void figures (NUMBERS section 6). |
| Q15-037 | 21 | With Keel's old margin the ladder was still short in 6.0% of history windows. | `Q15_monitoring_and_triggers.md` | 3a | Void figure | Superseded on Tue 10 Nov: under the no-interest standard no window is short (NUMBERS 2). |

## 3. Strong ideas with no judged home in the store

**(a) Cards never judged.** Card `Q1_career_as_shares.md` has 47 of its 50 rows, and `NUM_extras_2026-11-09.md` 10 of
its 12, on first-pass ratings only, with no row in `ratings.csv`. The strongest of them that SKELETON does not carry:
- NUM-007: $300,000 bought all ten payments in about one month in four since 1871, but nearly all of those months fell
  in 1966-1999; since June 2007 it did so on a single day. Home: 3a or 2.0 (why the IPS buys the ten first). Figures in
  NUMBERS 8e, which no density row cites.
- NUM-009: on 4 Aug 2020 the ten would have cost $470,217, more than both deposits together. Home: Table 3 row 6's
  note, to show in history how far the 3.60-point bound is.
- NUM-004: the orders filled within two trading days of 2026's cheapest close, and by 6 Nov the ten cost more than
  $300,000 again. Home: 3f, as the success told with its luck that SKELETON asks for. Check the Mon 16 Nov pool.
- NUM-002: interest on interest is 3% of the 2033 payment but about 15% of the 2041 and 2042 payments, so the
  reinvestment risk sits in the five T-bonds. Home: 3a's evidence clause or Figure 1's note.
- NUM-005 and NUM-006: the 2028-or-2031 floor test. See at-risk row Q7-030, and use NUMBERS 8c's figures, never these
  rows' void $110,000 bottom.
- Q1-046 (adapt): Laura's breakout came in 2020, the crash year ("In 2020, Laura published The Wuhan I Know", case
  p.1). Home: edit 1's career clause.
- Q1-030, Q1-033, Q1-035, Q1-036: each income source the case names fell in 2008-09. Advances were cut to a quarter,
  speaking budgets were cut, and licensing royalties fell 8.7% in 2009. Home: edit 8's clause, or 2.3.

**(b) Rows the parser skips.** Tables without an "Idea" column get no store id: card Q20 (14 rows, the pooled-book
verdicts and its per-payment table), Q22 (12 must-say rows), Q30 (8 Table 3 rows), Q17 (5 verdicts), Q11d (3), Q9c (3)
and Q5e (a 17-year data table). I checked them. Q22's and Q30's rows are carried by SKELETON 3d's checklist and by
exhibit 4, and the verdict rows restate store rows. Nothing strong is lost here.

**(c) Stale store pages.** `INSIGHT_STORE.md` and `store/by_tag/` predate the 29 Q5e judgements in `ratings.csv`. The
page shows tier A at 1,198; the rebuild gives 1,186. Rerun `store/build_store.py` before anyone reads the next ranking.

**(d) Never-judged harvest rows that looked strongest on a skim.** Judge these in the next store pass.
- H5-041: in Perry v. United States (1935), the only Treasury term broken in modern times was a gold clause, which
  Laura's bonds do not have. Home: 3e's default clause.
- H7-070: pledges from donors' own fortunes failed with Lehman. Spelman received $3m of a $10m pledge, and Duke paused
  a building. Home: 3e area (3), with Q9-033.
- H8-111: the SEC treats a price range wider than 20% of its top as not bona fide. Laura's $95,000 to $115,000 is about
  17% of its top at today's rates. Home: 3c, only after checking every row of Table 2, since rounding to $5,000 can
  push a range past 20%.
- H3-069 and H7-038: US law funds fixed court-ordered payment schedules with an insurer's annuity or a US Treasury
  obligation. Home: 3a, beside the lottery precedent (edit 4).
- H8-114: the GFOA says bond proceeds should mature by their drawdown date. Home: same as H3-069.
- H9-122: Taiwan Comic Base runs a comic artists' residency, a natural partner for a comics creator. Home: 3d, only as
  an example of who might co-sponsor, never as a contact.
- H9-008: in a public interview Laura calls each book a gamble she cannot judge "until the day it hits the shelves".
  Home: 2.3, cited to the dated public source, never as the case's words.
- H3-066 and H6-010: a legal 5% test and a joint ten-payment test of "high certainty". Flag: CANON A4 makes IPS l.11
  the only definition, so these can serve at most as a check, never as a second definition.

**(e) Outside the store by design.** These folders hold no store rows, and none is the only home of a strong idea:
- `research/experience/`: the Team Reflection's event pool, re-ranked on Mon 16 Nov. It carries the WInS-book vote,
  Q17-025.
- `research/panel/`: readers' findings, already applied as SKELETON changes.
- `research/meta/`: how to plan and how Wharton judges.
- `NUMBERS.md`: figures. The exception is 8c and 8e, which no density row carries (see Q7-030 and NUM-007 above).

## 4. Ten SKELETON edits, in order of importance

1. 3e's density row, limits: restore the career test in one clause. It holds "in the same downturn, not always the
   same months": tax data show 2009 at -11.6%; 2020 fell 12.4% while shares rose; her own genre rose in 2020; the
   link is strong for top earners and weak for the average graduate (Q1c-005, Q1c-010, Q12-018, Q1b-002, Q1b-010,
   Q1-046). Frame it as the tested limit of IPS l.9, which CANON B4 rates PARTLY true, never as a reversal of the
   thesis.
2. 3e area (1): call 7.5% "the top of published forecasts of about 6% to 7.5%" (Q6-011), so the 4%-10% test reads as
   covering every house's view.
3. 3c: add one clause that forecast ranges miss (finance chiefs' 80% ranges held 36% of the time, Q6-030), so Laura's
   range comes from owned money. INTENT's "biggest strength" then has its evidence.
4. 3a: add one public precedent beside the extra Treasuries. A state lottery that pays fixed prizes matures its holdings
   just before each payment and buys reserve bonds against reinvestment risk on purpose (Q16-018, Q16-020); this guards
   INTENT failure 7.
5. 3a: add one clause from the cultural field for Wharton's "how your strategy supports the ten-year operating
   commitment": reserves come before buildings (Q9-009), or founder-led institutions close within about ten years, for
   money (Q9-016).
6. 3b: add NUMBERS 8c, the IPS's decision to buy the floor in January 2028, tested against buying it in 2031 and kept.
   Waiting gains about $7,400 at the middle but leaves about one chance in six of facing the 2031 meetings under
   $95,000 (Q7-030). No density row carries 8c.
7. 3d fix (1): give "one total, one close date" its reason: funders reach a known target and fail an uncertain one
   (Q11a-025).
8. 3e area (2): cite card Q12. The deposit comes from income paid on contract dates, and a downturn delays it first
   (Q12-001, Q12-004, Q12-008); this is why Table 3 row 1 asks for written confirmation by 1 December 2027.
9. 3b: swap the optional Arrow and Fisher clause for practice. Owners hold the reserve above what builders see
   (Norway's state project model, Q5-018), and Taiwan's own costing manual lists exchange rates and fundraising among
   the causes of cost change (Q5-023).
10. Housekeeping:
    - Exhibit item 1 still waits for "Caplet's final export" and names 532281, which NUMBERS 8g replaced with CUSIPs on
      Fri 13 Nov and says is never printed.
    - 3e's density row holds two versions (the five-area spine and the "Before Fri 13 Nov evening" limits). Say which
      limits survive: net asset value, the model's limits and the site.
    - Close the open questions already settled (Q20 and Q19 on Tue 10 Nov; Q23 measured).

## 5. Sat 14 Nov evening: cards Q42, Q43 and Q44 (96 rows, all rated; 51 in tier A)

Every strong row has a place or a reason. Places are notes in `CONCEIT.md`, `SKELETON.md` and `WORDS.md`; nothing is prose.

| Row | Score | Where it lands, or why not |
|---|---|---|
| Q43-009 | 24 | 3c or 3d, one clause at most: the Antideficiency Act's "very act of obligating" before the money is in the account is the closest public rule to Laura's (GAO Red Book, 2006); investing-literature references stay first |
| Q43-039 | 24 | 3c: a university counts gifted shares for a building only once sold, the 2031 move in another institution's words |
| Q42-001, -005, -006, -012 | 23 | CONCEIT sections 6 and 7: small effect, one mapping, at most five images, never the last line, the image before or with its number |
| Q42-017, -028 | 23 | CONCEIT guard 5 and WORDS: "inked" is read as signed, so 3.0 says "owned" and the exception travels inside each use |
| Q43-028 | 23 | CONCEIT 5b rank 1 and WORDS: Watts (2003), the lenders' "asymmetrical verification requirements"; never "prudent" |
| Q43-003 | 22 | 3b: the deletion test in public-budget form |
| Q43-006 | 22 | 3d: building on promised but late money cost one DOE project 33% and three years |
| Q42-014, -022, -025 | 22 | 3.0's explicit comparison; the image never explains finance to experts; round 2 scores restatement, not preference |
| Q43-037, -040, -043, -045 | 21-22 | 3d: builders count binding pledges plus part cash; when money falls short the building shrinks or someone else pays; the charity regulator asks where surplus goes in advance |
| Q43-032, -034 | adapt | WORDS bans "prudent", "prudence" and "conservative estimate" for the range rule (IASB 2018, FASB) |
| Q43-001, -005 | adapt | The idea lands in 3a and 3d; the phrase "full funding" is banned for the facility |
| Q44-006, -011 | 20-21 | CONCEIT 5 and 5b: Martin (2019, p. 6) verified in print; Richmond (2006) for "never taken off cleanly" |
| Q44-001, -002, -004 | store | Process pages: not in 3f (card Q42: a second mapping that would call a plan pencil) |
| Q44-017, -019 | store | Non-photo blue: a third term, store only unless the trim/bleed image fails the blind read |
