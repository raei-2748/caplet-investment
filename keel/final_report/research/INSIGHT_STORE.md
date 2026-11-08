# The insight store: every idea for the Final Report, ranked

Caplet, Book 14: "Keep a store of every single insight you have. They should be organised or categorised ... some kind of ranking or rating system ... You must not lose a thing." This page is the front door. It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.

## How it works

- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards in `cards/` in the same format.
- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags below). An idea can sit under several.
- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is 19 or more, B 15 to 18, C below 15.
- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why); merged (a duplicate, pointing to the row that carries it).
- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies them and records which rows have been judged.

## Where it stands

- **1607 ideas** in the store; 167 judged so far, the rest on the first pass.
- Tiers: A 747, B 709, C 151; refused or merged 0.
- 332 ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).
- Rows per source: `cards/NUM_extras_2026-11-09.md` 10; `cards/Q10_inflation_inputs.md` 25; `cards/Q11a_funders_seed_assurance.md` 35; `cards/Q11b_real_case_statements.md` 35; `cards/Q12_lauras_working_life.md` 35; `cards/Q1_career_as_shares.md` 50; `cards/Q9_what_makes_a_residency_last.md` 35; `harvest/H10_why_wharton.md` 65; `harvest/H1_idea_bank_part1.md` 88; `harvest/H2_idea_bank_part2_and_ledger.md` 124; `harvest/H3_concepts_R02_R05_R06.md` 126; `harvest/H4_synergies_S1_S3_fusions.md` 190; `harvest/H5_synergies_S4_S6_R11.md` 153; `harvest/H6_shiller_damodaran.md` 171; `harvest/H7_final_night_reading.md` 118; `harvest/H8_lab_window_plans.md` 161; `harvest/H9_doc_research_tabs.md` 186.

## The parts of the plan and the case

| Tag | What it covers | Ideas | Ranked list |
|---|---|---|---|
| CAREER | Laura's career as an unsellable stock | 177 | [by_tag/CAREER.md](store/by_tag/CAREER.md) |
| CERTAINTY | A high degree of certainty | 418 | [by_tag/CERTAINTY.md](store/by_tag/CERTAINTY.md) |
| LADDER | The ten Treasuries | 316 | [by_tag/LADDER.md](store/by_tag/LADDER.md) |
| COMPLETE2028 | The 2028 deposit completes the ladder | 122 | [by_tag/COMPLETE2028.md](store/by_tag/COMPLETE2028.md) |
| FLOOR | The 2032 Treasury fund (bottom of the range) | 221 | [by_tag/FLOOR.md](store/by_tag/FLOOR.md) |
| CEILING | VT (top of the range) | 276 | [by_tag/CEILING.md](store/by_tag/CEILING.md) |
| HALFKEPT | Half the shares promised to no one | 155 | [by_tag/HALFKEPT.md](store/by_tag/HALFKEPT.md) |
| MOVE2031 | The move into Treasuries before 2031 | 139 | [by_tag/MOVE2031.md](store/by_tag/MOVE2031.md) |
| RESERVE2033 | The operating reserve from 2033 | 92 | [by_tag/RESERVE2033.md](store/by_tag/RESERVE2033.md) |
| TWOREASONS | Only two reasons to change | 136 | [by_tag/TWOREASONS.md](store/by_tag/TWOREASONS.md) |
| COSPONSOR | The 2031 range and the co-sponsors | 400 | [by_tag/COSPONSOR.md](store/by_tag/COSPONSOR.md) |
| FUNDRAISING | The fundraising text | 19 | [by_tag/FUNDRAISING.md](store/by_tag/FUNDRAISING.md) |
| RESIDENCY | The residency itself | 60 | [by_tag/RESIDENCY.md](store/by_tag/RESIDENCY.md) |
| INFLATION_TWD | Inflation, Taiwan costs, the Taiwan dollar | 92 | [by_tag/INFLATION_TWD.md](store/by_tag/INFLATION_TWD.md) |
| REINVEST | Reinvesting the ladder's interest | 140 | [by_tag/REINVEST.md](store/by_tag/REINVEST.md) |
| LAURA | Laura's working life and values | 63 | [by_tag/LAURA.md](store/by_tag/LAURA.md) |
| PROCESS | How the team decided and learned | 215 | [by_tag/PROCESS.md](store/by_tag/PROCESS.md) |
| PRESENTATION | How the report shows its work | 84 | [by_tag/PRESENTATION.md](store/by_tag/PRESENTATION.md) |
| OTHER | Other | 140 | [by_tag/OTHER.md](store/by_tag/OTHER.md) |
| HISTORY | HISTORY | 1 | [by_tag/HISTORY.md](store/by_tag/HISTORY.md) |

## The top 40 across the store (current ratings)

| Rank | Id | Score | Tags | Idea | Status |
|---|---|---|---|---|---|
| 1 | H1-081 | 21 | CERTAINTY, LADDER, TWOREASONS | Correlation makes the chain certain: ten payments fail if any one fails; ten independent 99% bets miss at least one about one time in ten (1 - 0.99^10 = 9.6%). One shared issuer makes them stand or f… | keep |
| 2 | H10-001 | 21 | PROCESS, OTHER | The competition began in 2012 with three Philadelphia teams and 15 students, inside Knowledge@Wharton High School, whose mission was "to promote financial literacy and a deeper understanding of how b… | keep |
| 3 | H10-008 | 21 | PRESENTATION, CERTAINTY | The academic director's whole philosophy: "There's one finance. It rests on two intuitive principles: costs and benefits, and risk." | keep |
| 4 | H10-009 | 21 | PRESENTATION, COSPONSOR | Roberts wants to "level the playing field ... by replacing ignorance and fear with knowledge and confidence"; jargon is "obfuscating the elegant simplicity of finance" | keep |
| 5 | H10-010 | 21 | LADDER, REINVEST | Roberts directs Wharton's executive course "Fixed Income and Credit Market Investing" and researches interest rates and bank lending | keep |
| 6 | H10-013 | 21 | PRESENTATION | Wharton's older guidebook: "Remember your reader ... You want your report to stand out from the hundreds we are reading." | keep |
| 7 | H10-014 | 21 | PRESENTATION | "We encourage a narrative format, rather than strictly a list of bullet points accompanied by charts and graphs." | keep |
| 8 | H10-015 | 21 | PRESENTATION | "Overly technical strategies will not necessarily impress us. We want both qualitative and quantitative analysis." | keep |
| 9 | H10-016 | 21 | PRESENTATION | "Too many charts, graphs, photos, images and over-the-top formatting will not dazzle your readers, but instead confuse and overwhelm them." | keep |
| 10 | H10-017 | 21 | PROCESS, PRESENTATION | "Evaluators don't want to read pages of defined terms as proof that you've learned something"; the page adds "show, don't tell" | keep |
| 11 | H10-020 | 21 | COSPONSOR, RESIDENCY, PRESENTATION | The 2026 semifinal panel: 11 of 15 hold Wharton designations; they are owners and allocators of money (private funds, a family office, two real-estate firms, wealth management, investment banking) | keep |
| 12 | H10-021 | 21 | LADDER, RESERVE2033 | Andrea Vittorelli, 2026 semifinal judge, was "global chairman of J.P. Morgan's Insurance Investment Group" when he judged the 2022 finale | keep |
| 13 | H10-023 | 21 | LAURA, CAREER, HALFKEPT | Two family-office judges recur: Thom Phan (2025 and 2026 semifinals) and Valerie Mukherjee (2025 semifinal, 2026 finale) | keep |
| 14 | H10-025 | 21 | PROCESS | Muk Rao (2025): "You're a better communicator now... you're better at advancing really complex arguments." | keep |
| 15 | H10-028 | 21 | COSPONSOR, CERTAINTY | Connor Barwin (2026): "confidence that you can figure it out, and humility to know that you don't have all the answers" | keep |
| 16 | H10-031 | 21 | OTHER, PRESENTATION | The 2025-26 participant badge still lists SWOT and Porter's Five Forces among learning objectives | keep |
| 17 | H10-033 | 21 | PRESENTATION, LAURA | Earlier cases framed teams as rivals "trying to land the same client" and asked "What sets you and your strategy apart from other teams?" | keep |
| 18 | H10-036 | 21 | PROCESS | Wharton bans paid advisers and outside courses that "claim to teach the Investment Competition", and may use "third-party private investigatory firms and/or forensic analysts" | keep |
| 19 | H10-042 | 21 | OTHER | The prize is more Wharton: champions get Wharton youth-programme scholarships, and Wharton hires 239 students across its youth programmes | keep |
| 20 | H10-044 | 21 | LAURA, PRESENTATION | As a student Laura ran a 30-day case competition, recruited Wharton judges, and wrote of "sculpting a simple idea into a spectacle" | keep |
| 21 | H10-055 | 21 | COSPONSOR, FUNDRAISING | IPCC rule for a quantity: give the range, its likelihood, the basis, what sets the outer bounds, assumptions, structural uncertainty, and the likelihood of values outside the range | keep |
| 22 | H10-056 | 21 | COSPONSOR, CERTAINTY | IPCC likelihood scale: virtually certain 99-100%, very likely 90-100%, likely 66-100%, about as likely as not 33-66%, unlikely 0-33%, very unlikely 0-10%, exceptionally unlikely 0-1% | keep |
| 23 | H10-057 | 21 | COSPONSOR, FUNDRAISING | Readers "systematically underestimate the probability" of high-likelihood statements, so put the number beside the word | keep |
| 24 | H10-058 | 21 | COSPONSOR | Sherman Kent: "We promise to speak, not in discrete figures, but in ranges of figures and ranges of our uncertainty regarding them." | keep |
| 25 | H10-064 | 21 | PRESENTATION | A Wharton teacher blog: "Thesis isn't just for English class" (the team's "guiding light") and "Chunk the final report" | keep |
| 26 | H2-010 | 21 | CAREER | Her income falls in the slump but doesn't come back with the market | keep |
| 27 | H2-031 | 21 | REINVEST, LADDER, CERTAINTY | Measure the ladder's weak point the way auditors do: public defeasance escrows buy Treasuries that pay enough "without reinvestment"; actuaries carry cash forward "at low or zero interest" | keep |
| 28 | H2-033 | 21 | REINVEST, LADDER | The funds' last-year wait: iBond funds hold maturing Treasuries and then cash until the 15 December close ("expected to consist almost entirely of cash"), less 0.07% a year, so a reinvestment rule wr… | adapt |
| 29 | H2-060 | 21 | FLOOR, MOVE2031 | Grain in the bin: farmers pre-sell only what they are sure to grow and lock more as the crop gets surer; the 2028 deposit is grain already in the bin, so lock its share then | keep |
| 30 | H2-082 | 21 | CEILING, MOVE2031, COSPONSOR | Never more than the pot holds: Alaska's Permanent Fund draw is "limited to the ERA balance"; smoothing like a sovereign fund (Norway, Alaska's lagged average) was rejected, because a gift that ends o… | keep |
| 31 | H2-093 | 21 | PROCESS, COMPLETE2028, TWOREASONS | The plan's rule was in the trade notes before it was named: the IBTR note (7 Oct) has a dated check ("by January"), one market reading ("If yields fall more than about 0.2 percentage points") and a r… | keep |
| 32 | H2-095 | 21 | PROCESS, LADDER | The WInS book is the finished plan at about two-thirds size: VT 8.6%, IBTM as both a rung and the minimum, each rung partly filled; the Nov-2041 note says "scaled to the model portfolio" | keep |
| 33 | H3-007 | 21 | FLOOR, LADDER, CERTAINTY | A defined-maturity ETF pays out its NAV, not par: IBTM "does not seek to return any predetermined amount at maturity", terminates about 15 Dec 2032, fee 0.07%; "Government backing ... does not apply … | adapt |
| 34 | H3-013 | 21 | CERTAINTY, LADDER | A US default is really a political delay; every rung matures before its payment (IBTM about 15 Dec 2032; the Feb-2037 bond about ten months before 1 Jan 2038), so a delay of weeks would not stop a pa… | keep |
| 35 | H3-015 | 21 | LADDER, CERTAINTY | Term premium: long bonds usually pay a little extra for rate risk; for a holder with fixed long payments, long bonds are the low-risk asset, so she is paid for holding what she would hold anyway | keep |
| 36 | H3-016 | 21 | LADDER, CERTAINTY | The riskless asset depends on the liability: for a long-horizon investor cash is risky (its rate rolls over); the matched long bond is riskless | keep |
| 37 | H3-024 | 21 | CERTAINTY, LADDER | Surplus optimisation: measure risk as assets minus liabilities, not assets alone | keep |
| 38 | H3-026 | 21 | CERTAINTY, HALFKEPT | Mental accounts can be efficient: separate goal pots with a shortfall limit each map to a mean-variance solution | keep |
| 39 | H3-045 | 21 | COSPONSOR, HALFKEPT | The entrepreneur's own stake signals project quality to outside financiers | keep |
| 40 | H3-046 | 21 | COSPONSOR | Cheap talk: when interests differ, only coarse messages are credible, and they take the form of an interval | keep |

## The thinnest parts (fewest ideas rated B or better)

- FUNDRAISING (The fundraising text): 18 rated B or better, 19 in all.
- RESIDENCY (The residency itself): 60 rated B or better, 60 in all.
- LAURA (Laura's working life and values): 62 rated B or better, 63 in all.
- PRESENTATION (How the report shows its work): 83 rated B or better, 84 in all.
- RESERVE2033 (The operating reserve from 2033): 85 rated B or better, 92 in all.
- INFLATION_TWD (Inflation, Taiwan costs, the Taiwan dollar): 85 rated B or better, 92 in all.
- REINVEST (Reinvesting the ladder's interest): 108 rated B or better, 140 in all.
- COMPLETE2028 (The 2028 deposit completes the ladder): 112 rated B or better, 122 in all.
