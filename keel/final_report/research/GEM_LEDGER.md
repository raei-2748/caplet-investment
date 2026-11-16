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
| 6 | Q6-011 | 22 (adapt) | high | J.P. Morgan's 7.5% for world shares is the top of eight houses' dated forecasts, which run from about 6% to 7.5% (median about 6.5%). Changed Sun 15 Nov (card Q6b): upper third of fifteen houses, four above it. | `Q6_how_far_to_trust_7_5.md` | 3e | Edit 2: 3e area (1) says '7.5% a year (J.P. Morgan 2027), the top of published forecasts of about 6% to 7.5%', then the 4%-10% test. Adapt: never say the Trading Notes quoted the most optimistic house. |
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
| 21 | Q16-006 | 22 | med | The three iBond Treasury funds that have already ended (2023, 2024, 2025) each paid cash 10 to 14 days before 1 January [Sun 15 Nov evening, card Q3c: five have ended; cash came 29 (IBTA, which ended 15 days early), 11, 10, 13 and 14 days before 1 January; 'every one so far' holds for cash before 1 January]. | `Q16_operating_reserve_mechanics.md` | 3a | 3a's liquidity clause or Figure 1's note: 'every one so far', after checking BlackRock's count of terminations (card note). |
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
| Q31-015 | 23 | A 2% surgical risk remembered as 10% is informed consent; remembered as 0% it is not. | `Q31_escrow_standard_plain_words.md` | 3a | Too small, or a rule already applied | A wording rule, void since Book 19 (Sun 15 Nov): no exception needs to travel inside 3a's sentence. |
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
   link is strong for top earners in general and weak for the average graduate, while at the top of the author trade 2020 hit speaking and the biggest advances, not book income (card Q56 rows 9, 22, 33, Mon 16 Nov) (Q1c-005, Q1c-010, Q12-018, Q1b-002, Q1b-010,
   Q1-046). Frame it as the tested limit of IPS l.9, which CANON B4 rates PARTLY true, never as a reversal of the
   thesis.
2. 3e area (1): ~~call 7.5% "the top of published forecasts of about 6% to 7.5%" (Q6-011)~~ (killed Sun 15 Nov, card Q6b:
   fifteen houses on one basis put it in the upper third, median about 6.5%, four above it); say "upper third", with the
   4%-10% test and NUMBERS 8p's lowest-house row.
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
| Q42-017, -028 | 23 | CONCEIT guard 5 and WORDS: "inked" is read as signed, so the definition (2.0 since Sun 15 Nov night) says "owned"; the exception no longer travels with each use (Book 19) |
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

## 6. Sun 15 Nov (Day 8): cards Q6b-Q7c and the first digest

Nothing lost: every row the digest refused or merged is still in the store with its reason (`store/DIGEST_2026-11-15.md`
section 1 lists the refusals; merged rows point to the row that holds their idea). Where the day's strongest rows land:

| Ids | Score or status | Where it lands |
|---|---|---|
| Q6b-022 (with Q6-011 re-noted) | 21, keep | 3e area (1): "upper third" of fifteen houses; "the top of published forecasts" killed (section 4 edit 2 struck) |
| Q6c-015, Q6c-016, Q6c-019 | 23-24, keep | 3e area (1) or Table 2's note, one clause; NUMBERS 8p |
| Q6c-017 | 21, keep | 3e as a limit of IPS l.15's fixed move date (a fall before the move is kept even if shares recover) |
| Q6d-018, Q6d-012, Q6d-013 | 20-22, keep | 2.3 or 3b, one clause: why one world fund for money that may be spent in Taiwan dollars |
| Q6d-023, Q6d-026 | keep, adapt | Guard: never imply VT offsets the Taiwan dollar (IPS l.15) |
| Q7b-033, Q7b-034 | 21-22, keep | 3e "why only these two"; 3a "the Treasuries carry the plan" |
| Q7b-035 to Q7b-038 | adapt | 3e limit (two weak tests, no new rule); guards on Table 3 and the five-business-day definition |
| Q7c-003, Q7c-004 | 21-22, keep | 3e, one clause at most: rules kept through a shock against triggers named after one |
| Q7c-033, Q7c-035 | 22-23, keep | 3d: owed, not owned |
| Q7c-017 | keep | Guard: never call the reserve an endowment |

## 7. Sun 15 Nov evening: cards Q2d, Q3c, Q10e, Q11e and Q45 (175 rows, all rated)

Nothing lost: every row is in the store with a judged score and a note; store-only rows say so in `store/ratings.csv`.
Where the evening's strongest rows land:

| Ids | Score or status | Where it lands |
|---|---|---|
| Q2d-001, Q2d-005, Q2d-007, Q2d-013 | 21-23, keep | 3a, one clause: why test with cash earning nothing (9 of 17.9 years at 0-0.25%; $48 at most on $50,000 for half a year) |
| Q2d-016, Q2d-018, Q2d-019 | 20-22, keep | Guard: never "cash cannot go below zero"; the auction and SLGS zero floors explain why escrow verifiers test at zero |
| Q2d-015, Q2d-031 | 21, keep; 20, adapt | 3e limit, store figures until NUMBERS carries them: real bill-ETF years leave money over; a fifteen-year regime below -0.15% leaves a few thousand short, late |
| Q2d-032 | 22, keep | 3a or 3e, one clause at most: zero is a forward risk in the Fed's own work (20-50% within a decade) |
| Q3c-002, Q3c-011, Q3c-013, Q3c-014 | 24-25, keep | 3e area (2) and the haircut's evidence: the funds' only cost is the fee; the floor fund's own index already assumes cash earning nothing |
| Q3c-004, Q3c-006 | 22-24, keep | 3e or Table 1's note: all five ended funds paid within 0.066% of their last price, final NAV to the cent |
| Q3c-007, Q3c-008, Q3c-010 | 22-24, keep | Table 3 row 4 and 3e: an early end has happened (IBTA, 15 days, cash before 1 January); the watch reads September-October |
| Q3c-022 | 20, keep | Table 3 row 5: read the premium before each purchase; a stressed day is outside the 0.5% |
| Q10e-002, Q10e-004, Q10e-016, Q10e-019 | 24-25, keep | 3e area (4): the pair's 1-in-20 two-year move (+28.0%, about $32,200) and worst (+38.9%), a limit, never a change |
| Q10e-021, Q10e-022, Q10e-024 | 23-24, keep | 3e: the joint moves came with rising shares; her flexibility short in 9 of 250 windows, at most $9,363 |
| Q10e-017 | 21, keep | Table 3 row 7 stays a currency watch at 10% (its own 1 in 20) |
| Q10e-025 | 21, keep | NUMBERS 8j wording (sent to the numbers owner) |
| Q11e-001, Q11e-031, Q11e-032 | 24-25, keep | 3b and 3d: founder first, co-sponsors after; "first", never "largest" |
| Q11e-016, Q11e-018 | 24, keep | 3b: overruns are the owner's to meet (Ministry rule); owners paid 48.3% |
| Q11e-033 | 22, adapt | Guard for 3b: the half held back answered by who meets overruns, never as giving less |
| Q11e-025 | 22, keep | Store only (3d if a clause is free): Laura's range in the upper half of owners' parts |
| Q45-012, Q45-014, Q45-037 | 24-25, keep | 3e or Table 3 row 5: the 2031 move costs about $6, about $267 in a March-2020 week |
| Q45-023, Q45-036, Q45-038 | 22-24, keep | 3e: selling one bond early costs tens of dollars, a few hundred in a stress |
| Q45-001, Q45-008 | 20-22, keep | 2.5 or 3e: Treasury funds stayed near value in March 2020; long Treasury funds were the exception (TLT about -5%) |
| Q45-026, Q45-027 | 21-24, adapt | Guard: the FR never repeats TNA l.15's "no odd-lot bond offers" for Treasuries (a 3bp gap) |
| Q45-017 | 22, keep | CANON B22 corrected: IBTR $112.3m |

## 8. Mon 16 Nov afternoon (overdrive): cards Q48-Q57, Q59, Q60 and Q62 (546 rows, all rated by raters A-E)

Nothing lost: every row is in the store with a judged score and a note (`store/ratings.csv`, raters' files in
`store/digest/ratings_R2_*.csv`). Cards Q58, Q61 and Q63-Q81 are landed below: every card of the day is rated and placed. Where the strongest rows land:

| Ids | Score or status | Where it lands |
|---|---|---|
| Q50-008, Q55-001, Q55-009, Q55-010, Q55-045 | 22-23; Q50-008 adapt (drop its 70%; ink means owned, never paid) | 3d, and aha reserves "In Taiwan a promise to pay later fades": the national arts foundation's five-year donors fell from 137 payers to 46 to none; Arts Council England calls later years "indicative"; 5 of 93 top Taiwan troupes hold any multi-year operating promise, at most three years; no arts funder read fixes more than seven. Laura's ten are owned |
| Q51-035, Q51-010, Q51-004 | 20-22; Q51-035 adapt | 3a (aha reserves): of 399 subsidised Taiwan culture halls, all 22 changes of use came after the subsidies ended; the field's 1994 diagnosis "arts managers lack early money" (her bottom is early money); 3e: in 2008 about three-quarters of Kresge's capital grantees asked for more time |
| Q52-003, Q52-023, Q52-002 | 21-22; Q52-002 adapt (never "narrower than every one") | 3c slot 5 (aha register, the biggest question): counsel gives confidence only in words; boards' feasibility ranges ran 22-50% of their midpoint, hers is 19.0% and owned; the Lilly gift to Poetry, "well in excess of $100 million", sat in one share and lost $102 million in 2002 (3c or 3e, one clause) |
| Q53-030, Q53-016, Q53-017 | 19-21, keep | Table 3 row 1 and 3e: 31 March 2028 is 90 days after 1 January, the line bank supervisors use for a non-performing loan; gift offices review pledges on 1 December and act at 90 days; silence keeps the file open, so no word by 1 December is a question, never a reason |
| Q54-003, Q54-038, Q54-004 | 19-21, keep | 2.2 and 3a: S&P's "fixed principal amount due at its maturity" is the line Trading Note 2 drew; a BBB- company's bonds became AA+ once Treasuries were owned against each payment (3.0 or 3d, aha candidate); honest limit: no rated escrow may hold a fund, so the plan meets the escrow's sufficiency test, never "escrow-grade holdings" (NUMBERS 3 corrected the same afternoon) |
| Q48-011, Q48-016, Q48-024; Q49-010, Q49-012, Q49-027 | 20, keep | 3d: Taiwan proves an owner's share by receipts at each instalment and a public funder's by a budget vote a later vote can cut; the state's own grant is a provisional sum (a pencil figure); Table 3 and 3e: the budget passed on time in 0 of 11 years, and a late budget holds back new capital; a private residency's public capital line is equipment-sized |
| Q50-019, Q50-012 | 20, keep | 2.3 and CANON B4: a Taiwanese firm's arts budget follows this year's profit, not last year's; the one multi-year gift the foundation could count on was paid on day one |
| Q56-009, Q56-005, Q56-016 | 20-21, keep | 2.3 and 3e area (2): SKELETON row 4 corrected the same afternoon (the top of the author trade held in 2020; the risk is a quiet year more than a share-market fall); 17% of UK writers in print every year still had a zero year |
| Q57-010, Q57-011, Q57-015, Q57-042 | 20-21, keep | 2.3 and the lineage of the central idea (EXPECTATIONS 2.4): behavioural portfolio theory's layers filled with the textbook's two funds, for a covariance reason BPT investors overlook; Chhabra's aspirational bucket; Waring and Whitney's liability-matching asset; Roy (1952), "the standard error of this estimate is zero" |
| Q59-026, Q59-014, Q59-025; Q59-003, Q59-011 | 22; 014, 025 and 003 adapt | 3a or 3b: aha candidate for the open slot, "every margin has a job and a spender" (aviation's contingency, alternate and discretionary fuel = the 0.5% cut, the extra Treasuries, her flexibility); who bears the loss sets the dam standard (3b); the 1890 load line drawn by law from tables, not the owner's intention (3c) |
| Q60-042, Q60-015, Q60-006 | 20-21, keep | 3.0 and 3d: fewer than half of 7,684 EU investors could pick the guaranteed product, so the owned ten must be impossible to miss; method for every reader panel: never self-rated understanding; a "heard as Caplet's" claim needs about 60 judgements to prove (voice README) |
| Q62-002, Q62-008, Q62-015, Q62-027, Q62-037 | 20; 015 adapt | 3a (aha candidates): a separate account is not what makes a reserve real; New York cancelled $774 million of its own bonds in its sinking funds in 1932; trust-fund Treasuries are legal claims to the holder (OMB) and net out only for the government as a whole; Ireland's locked reserve was redirected by its own owner, so Laura's guard is her two-reason rule (3e) |
| Q58-014 | 22, adapt | 3c, one bridge sentence beside aha row 7: a note needs backing only once it leaves the issuer (Scottish notes printed but not collected need none), so the top needs owning only when she states it; Q58's other money parallels stay in the store (F 2 or lower: too close to the subject for a conceit turn) |
| Q63-016, Q63-026, Q63-034, Q63-043 | 21-22; 043 adapt (say "every cap we found, six", never "every cap in US law") | 2.3 and aha row 2 (added the same afternoon): GIW Industries faulted an all-Treasury fund's dates, never its issuer, and the remedy was staggered maturities; a pension buying fixed payments adds money, never risk (IB 95-1), as the IPS's 2028 completion does, said as a parallel; the tax code deems Treasuries "adequately diversified" |
| Q61-011, Q61-012, Q61-031, Q61-008 | 18-20; 008 adapt (fix the ending-in-a-loss share) | Table 2's note and 3c: a 40% fall is about twice the 1-in-20 three-year loss of world shares (-19.7% on month-end MSCI World since 2001); "living through" a 40% fall and "ending" 40% down are two events, said in one sentence; long-horizon loss estimates are mostly noise, so the top rests on history and moves while the bottom rests on Treasuries (3c's split) |
| Q64-009, Q64-012, Q64-013, Q64-005 | 21-22; 005 adapt | 3a and aha row 5 (applied the same afternoon in NUMBERS 2 finding 1): the forward rate forecasts least well of four methods; the 55.6% is one rate cycle (17.1% of starts 1962-80, 80.1% from 1981), always "585 starting months"; when short, a median $16,055; the 6 Nov term premium (0.87) is the ten-year yield's, never a single forward's |
| Q65-009, Q65-012, Q65-016, Q65-019 | 19-20; 009 adapt (never "the least flattering assumption") | Aha row 5b's rework (the nine-pattern map now names the plan's real exposures; rater I: fix the $589,655 broker-balance reading and say the payment funds pay net asset value before it returns to the spine) and 3a or 3e: Laura's under-reserving shown and priced ($54,595 at 0%); the S&L's cheap moment missed; each payment's money arrives 0.5 to 10.5 months early, the safe way round; Executive Life took two years to restart payments |
| Q66-011, Q66-037, Q66-002, Q66-008 | 20-23; 011 and 002 adapt | Aha row 9 and SKELETON 3e (rewritten the same afternoon): no general tendency, only a shape of window that can hurt; world shares (MSCI ACWI, never VT, which launched in 2008) bought January 2000 were 6.6% down after five years while Taiwan's costs rose 17.9%; the 28-of-35 counts wait on the 1970-2000 table being verified; never the 2008 example |
| Q85 (all rows), correcting Q66-011, -037, -002, -008 | rated tonight (rater AG) | Verified at source Mon 16 Nov evening: aha row 9 and SKELETON 3e corrected the same evening (counts on the MSCI-checkable years 18 of 25 against 76 of 99; 28 of 36 against 149 of 181 with the UK's 1980s added; "140 of 172" was years shares rose, not "other years"; 6 of 9 fell the year after 1974 and 2008, never 7 of 9; January 2000 shares about 10% down on Laura's calendar, never 6.6%; costs 27-28% in US dollars; the cushion was smallest at the meetings). Placed: aha row 9, SKELETON 3e aha row |
| Q68-008, Q68-025, Q68-037, Q68-021 | 20-21; 037 adapt | Aha reserves "she starts where pensions end" (Tue 17 Nov cold test, worded "the state a pension reaches last", never "fully funded on day one"): Boots sold every share for long bonds in 2000-01; UK law's objective "does not apply to any surplus", IPS l.11's rule in law (2.0 or 3b); the floor is a second matched block for a promise stated in 2031, only VT seeks return (3b) |
| Q70-002, Q70-015, Q70-024, Q70-004, Q70-036 | 20-22; 004, 024 and 036 adapt | Aha row 5 (added the same afternoon): a lead trust's "guaranteed annuity" is a fixed amount, not money that will be there; no test asks if a lead trust can pay (say "the residency's payments", never "charity"); the IRS sizes them at 120% of mid-term Treasury yields; one real trust moved its last payments into bonds in year eight, where Laura starts. Never "ink in the deed" (ink means owned) |
| Q73-036, Q73-011, Q73-025, Q73-035, Q73-037 | 21-22; 037 adapt (never "about 89%") | Figure 1's three fixes in `charts/DESIGNS.md` section 2 for the next rebuild (the sum in the heads with a total row that adds up; one world per exhibit; the condition first in the title); aha row 5: stricter than the UK insurance regulator on rate and shortfall; Figure 1's form is rare, not standard |
| Q67-043, Q67-017, Q67-016, Q67-020, Q67-023 | 21-24; 016, 017 and 023 adapt | 3c and the register's biggest question: a gift office will not count a pledge resting on "some future event", so she states no figure before the move (043); 3d words: an auditor called anonymous pledges "fragile", hers is named and listed by identifier (020); Tai Kwun's budget became a floor and its funder covered running deficits too, but her flexibility cannot cover a 2.1-times overrun (016, 017: 3e's honest limit, never a promise); the Garden Bridge closed over a maintenance guarantee with a £70m capital gap too (023). Wording from rater K: "her ten operating payments", a base, never "running money" or "asks co-sponsors nothing yearly" (the case lets co-sponsors fund operations beyond her commitment). Card's verdict "no precedent" is said only as "none found in the sources card Q67 read" |
| Q71-002, Q71-001, Q71-017, Q71-004, Q71-033 | 19-25; 004 adapt | SKELETON 3c the same afternoon: "certain" on the Treasuries, never on "$115,000" (three in four sentence-completers pair "certain" plus an amount with "at least"; a choice study, not a listening one, rater N); name the best and the worst figure, then stop (017); the top with its reason (004); why a range: what co-sponsors count and what she pays, both owned (033). Rows 21-22's accounting rules are an obligor's, so SKELETON no longer says a bare range "counts at its bottom" |
| Q74-036, Q74-002, Q74-019, Q74-021, Q74-024 | 22-24, keep | 3c (register's biggest question): the case's three senses of "confidence"; Neyman's zero-or-one for one interval; no "95%" or "confidence interval" on the owned range; Basel's 99.9% pads against model error, the 0.5% cut's job (3c or 3e); APRA's 75% sufficiency for insurers' claims money against her bottom, sufficient in every tested future (3a or 3c); S&P's AAA scenario is the Great Depression and the 1929 replay still gives $95,000 to $100,000 (NUMBERS 4 Exhibit 3; US stocks only, rates at forwards) |
| Q69-002, Q69-011, Q69-017, Q69-024, Q69-010 | 21-22; 010 adapt (the $970m cap is a different defence account) | 3e area (4) and Table 3 row 7: why the plan does not lock the Taiwan dollar in 2031: firms and governments fix a currency only once the bill is certain (NZ Treasury: "at the contract stage"), and her 2031 figure is an approval-stage number (002); the Defense Department may not hedge by law, so it keeps a capped pot, a cushion, never a hedge, which is her flexibility's role (011; aha row 9); budgeting at the day's rate, which GAO called nonjudgmental, is Table 3 row 7's base (017); a US-dollar gift with a backstop at the funder's discretion, not a guarantee, is where Laura sits (024). Converting in 2031 would forgo about $6,300 to $8,500 of interest (Keel arithmetic, not in NUMBERS: adapt) and selling her Treasuries early to do it clashes with IPS l.17. A non-resident needs central bank approval to convert more than US$100,000 at once, one more reason the residency converts |
| Q72-016, Q72-013, Q72-008, Q72-022, Q72-004 | 20-22; 013 adapt | CONCEIT V2.1 the same afternoon: "owned" is the law's word (UCC 8-503), "held for her", never "in her name"; at Lehman's broker customers got 100%, general creditors 41.28% (3e or the conceit's 2.0 definition); SIPC's $500,000 caps only its top-up, so store row Q30-034's "custody above SIPC is the weakest row" is corrected (drop "$89,655 at risk"); custody is one line of 3e prose; a fund share is a share of a pool of Treasuries |
| Q76-003, Q76-020, Q76-015, Q76-018, Q76-032 | 21-22; 032 adapt (cite Annex V Part 1 point 3(b)) | 3d: regulators allow projections only for an audience whose situation is known (the SEC's 15 Oct 2026 approval of FINRA's rule; never "brokers may now"), the plan's own split: models for Laura and the judge, owned figures for co-sponsors (003); "guaranteed" on the Treasuries, never an iBond fund's payout (020, CONCEIT V2.1); the same $95,000 is modelled today and owned from January 2028, so IPS l.15's constant bottom is read from January 2028 and shares never move it (015, CANON C6/D10); EU law states a guaranteed minimum in money with the payer's default in its own section, Book 19's form written by a regulator (032) |
| Q75-020, Q75-013, Q75-025, Q75-021, Q75-034 | 20-21, keep (no row above F 3: parallels, since in Taiwan the founder's own money is the match, card Q48) | 3d, one clause at most: Asia's matching funds let a project in on money that is "secured and deliverable" but match only cash received (Hong Kong), so Laura passes every door test years before her money is counted (bottom owned January 2028, top before the 2031 meetings, paid December 2032); Korea checks whether the giver can keep supporting the group; Hong Kong pays for buildings but gives two years of start-up help (3.0 or 3a: running costs come first, her ten operating payments are owned before any building money is asked for) |
| Q81-016, Q81-015, Q81-002, Q81-017, Q81-021 | 20-23, keep | NUMBERS beside 8a the same evening ("Waiting cash at zero is history, not only a stress"): the bill under 0.15% in 90 of 222 months since 2008; 54 bill auctions at exactly 0.000%; the Fed's 2026 stress test holds the 3-month bill at 0.1% for 12 quarters; BIL's filings correct store Q2d-014 (2015 was -0.11%); 3a: the standard's condition has really happened, in two eras, and the standard is still harsher than history (a fee held for sixteen years). Row 9 adapt (worst windows start Jan 2006); row 13's $2,454 margin needs its script in the repo before use |
| Q79-013, Q79-004, Q79-024, Q79-036, Q79-031 | 19-21; 004, 031 and 036 adapt (17 rows merged as twins or repeats of V2.2) | CONCEIT V2.3's candidate turns the same evening, each to be read cold before it joins V2.2: geology's "numerical ages do not define units" for 3c (the range is a rule, today's figures a reading); Taiwan Civil Code art. 758 for 2.0 (ink is the register entry, never the deed); golf Rule 3.3b(3) for 3b-3c (overstating disqualifies, understating stands); land title's order of claims for the 2028 deposit (3b). The holotype dropped (art. 16.4.2 accepts intent to deposit, which is pencil) |
| Q78-041, Q78-035, Q78-016, Q78-012, Q78-026 | 17-18; 016 and 012 adapt | 3e's one line of custody prose (CONCEIT V2.1, card Q72): the honest risk is delay, never loss. The 1979 bill delay cost holders about 0.10% and book-entry holders were untouched (041); a failed custodian bank's assets stay the owner's (035); a broker failure costs weeks, not holdings (016; reconcile MF Global's 318 accounts with Q72-017's "about 330" before use); a frozen Treasury fund would pay late and pro rata without losing Treasuries (026). The 2026 custodians are checked in the SAIs: JPMorgan for IBTM, IBTO, IBTQ and IBTR, State Street for IBTP and VT; every holding sits at one broker, so never "three keepers" (row 31). Store Q65-025's "lost most" for Peregrine is out of date (customers got 72% and 100%) |
| Q80-015, Q80-007, Q80-010, Q80-031, Q80-032 | 19-21; 031 and 032 adapt | 3f's method (`research/experience/RANKING_5_RERANK.md`): owning a lapse of skill raised integrity ratings (5.32 against 4.27) while owning a lapse of honesty cut them (2.73 against 4.39), so the moments are mistakes of judgement told first and plainly (015); markers cannot check most reflections, but Caplet's dated figures can be, so each moment carries one checkable figure (007); readers average, so three moments beat four (010, abstract only); Wharton's guide welcomes a strategy that "may evolve as you learn more" (p. 1) and treats results as no evidence, so a change of mind is told from learning, never from results (031, 032). Jenkinson's 1.12% is about consultants' recommendations in general, not process judging (row 26 adapt) |
| Q77-033, Q77-002, Q77-023, Q77-003, Q77-001 | 17-19; 003 and 001 adapt; row 4 refused | 3d and 3e, and aha reserve "In Taiwan a promise to pay later fades" (added the same evening: Taichung's Guggenheim died when the central government withdrew its promised NT$5bn); the case's verb for 2031 is "expects to contribute" (002) and it ties no payment to the building, the contribution dated 2033 (001); because she owns the figure until she pays it in December 2032, it stays hers if the building is cancelled ("held for her", from the 2031 move; 003); a Taiwan foundation's money never goes back to its founder once given (art. 33; store only). Guards from rater Y: a cancelled or delayed facility is never a third reason to change and the reserve never "returns to her" (row 4 refused: IPS l.17, and the case says she "will make" the ten payments); no condition or lapse date on her figure, which 3d keeps "first and unconditional" (rows 9, 35, 39); Allegheny College is not a promissory-estoppel holding (row 7); $3,450 a year of delay is Keel arithmetic, not NUMBERS (row 6) |
