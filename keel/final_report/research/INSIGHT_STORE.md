# The insight store: every idea for the Final Report, ranked

Caplet, Book 14: "Keep a store of every single insight you have. They should be organised or categorised ... some kind of ranking or rating system ... You must not lose a thing." This page is the front door. It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.

## How it works

- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards in `cards/` in the same format.
- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags below). An idea can sit under several.
- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is 19 or more, B 15 to 18, C below 15.
- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why); merged (a duplicate, pointing to the row that carries it).
- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies them and records which rows have been judged.

## Where it stands

- **970 ideas** in the store; 0 judged so far, the rest on the first pass.
- Tiers: A 399, B 461, C 110; refused or merged 0.
- 152 ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).
- Rows per source: `harvest/H1_idea_bank_part1.md` 88; `harvest/H2_idea_bank_part2_and_ledger.md` 124; `harvest/H3_concepts_R02_R05_R06.md` 126; `harvest/H4_synergies_S1_S3_fusions.md` 190; `harvest/H5_synergies_S4_S6_R11.md` 153; `harvest/H6_shiller_damodaran.md` 171; `harvest/H7_final_night_reading.md` 118.

## The parts of the plan and the case

| Tag | What it covers | Ideas | Ranked list |
|---|---|---|---|
| CAREER | Laura's career as an unsellable stock | 56 | [by_tag/CAREER.md](store/by_tag/CAREER.md) |
| CERTAINTY | A high degree of certainty | 295 | [by_tag/CERTAINTY.md](store/by_tag/CERTAINTY.md) |
| LADDER | The ten Treasuries | 236 | [by_tag/LADDER.md](store/by_tag/LADDER.md) |
| COMPLETE2028 | The 2028 deposit completes the ladder | 66 | [by_tag/COMPLETE2028.md](store/by_tag/COMPLETE2028.md) |
| FLOOR | The 2032 Treasury fund (bottom of the range) | 144 | [by_tag/FLOOR.md](store/by_tag/FLOOR.md) |
| CEILING | VT (top of the range) | 216 | [by_tag/CEILING.md](store/by_tag/CEILING.md) |
| HALFKEPT | Half the shares promised to no one | 98 | [by_tag/HALFKEPT.md](store/by_tag/HALFKEPT.md) |
| MOVE2031 | The move into Treasuries before 2031 | 99 | [by_tag/MOVE2031.md](store/by_tag/MOVE2031.md) |
| RESERVE2033 | The operating reserve from 2033 | 54 | [by_tag/RESERVE2033.md](store/by_tag/RESERVE2033.md) |
| TWOREASONS | Only two reasons to change | 96 | [by_tag/TWOREASONS.md](store/by_tag/TWOREASONS.md) |
| COSPONSOR | The 2031 range and the co-sponsors | 231 | [by_tag/COSPONSOR.md](store/by_tag/COSPONSOR.md) |
| INFLATION_TWD | Inflation, Taiwan costs, the Taiwan dollar | 39 | [by_tag/INFLATION_TWD.md](store/by_tag/INFLATION_TWD.md) |
| REINVEST | Reinvesting the ladder's interest | 97 | [by_tag/REINVEST.md](store/by_tag/REINVEST.md) |
| PROCESS | How the team decided and learned | 128 | [by_tag/PROCESS.md](store/by_tag/PROCESS.md) |
| OTHER | Other | 114 | [by_tag/OTHER.md](store/by_tag/OTHER.md) |

## The top 40 across the store (current ratings)

| Rank | Id | Score | Tags | Idea | Status |
|---|---|---|---|---|---|
| 1 | H1-006 | 21 | COSPONSOR, FLOOR | Announced lead money drives giving: raising announced seed money from 10% to 67% of the goal gave a nearly sixfold rise in contributions; matching above 1:1 adds nothing | keep |
| 2 | H1-023 | 21 | COSPONSOR, FLOOR, CEILING | Bottom = unconditional pledge, top = a variable amount set by a rule; in US nonprofit accounting a stated condition can make a pledge conditional, so never write "only if stocks hold" | keep |
| 3 | H1-081 | 21 | CERTAINTY, LADDER, TWOREASONS | Correlation makes the chain certain: ten payments fail if any one fails; ten independent 99% bets miss at least one about one time in ten (1 - 0.99^10 = 9.6%). One shared issuer makes them stand or f… | keep |
| 4 | H2-010 | 21 | CAREER | Her income falls in the slump but doesn't come back with the market | keep |
| 5 | H2-031 | 21 | REINVEST, LADDER, CERTAINTY | Measure the ladder's weak point the way auditors do: public defeasance escrows buy Treasuries that pay enough "without reinvestment"; actuaries carry cash forward "at low or zero interest" | keep |
| 6 | H2-033 | 21 | REINVEST, LADDER | The funds' last-year wait: iBond funds hold maturing Treasuries and then cash until the 15 December close ("expected to consist almost entirely of cash"), less 0.07% a year, so a reinvestment rule wr… | keep |
| 7 | H2-060 | 21 | FLOOR, MOVE2031 | Grain in the bin: farmers pre-sell only what they are sure to grow and lock more as the crop gets surer; the 2028 deposit is grain already in the bin, so lock its share then | keep |
| 8 | H2-082 | 21 | CEILING, MOVE2031, COSPONSOR | Never more than the pot holds: Alaska's Permanent Fund draw is "limited to the ERA balance"; smoothing like a sovereign fund (Norway, Alaska's lagged average) was rejected, because a gift that ends o… | keep |
| 9 | H2-093 | 21 | PROCESS, COMPLETE2028, TWOREASONS | The plan's rule was in the trade notes before it was named: the IBTR note (7 Oct) has a dated check ("by January"), one market reading ("If yields fall more than about 0.2 percentage points") and a r… | keep |
| 10 | H2-095 | 21 | PROCESS, LADDER | The WInS book is the finished plan at about two-thirds size: VT 8.6%, IBTM as both a rung and the minimum, each rung partly filled; the Nov-2041 note says "scaled to the model portfolio" | keep |
| 11 | H3-007 | 21 | FLOOR, LADDER, CERTAINTY | A defined-maturity ETF pays out its NAV, not par: IBTM "does not seek to return any predetermined amount at maturity", terminates about 15 Dec 2032, fee 0.07%; "Government backing ... does not apply … | keep |
| 12 | H3-011 | 21 | RESERVE2033, CERTAINTY, LADDER | Defeasance, and why accounting withdrew "in-substance" defeasance: risk-free bonds set aside for a debt make it as good as paid, but FASB stopped allowing it (1996) because the borrower could still b… | keep |
| 13 | H3-013 | 21 | CERTAINTY, LADDER | A US default is really a political delay; every rung matures before its payment (IBTM about 15 Dec 2032; the Feb-2037 bond about ten months before 1 Jan 2038), so a delay of weeks would not stop a pa… | keep |
| 14 | H3-015 | 21 | LADDER, CERTAINTY | Term premium: long bonds usually pay a little extra for rate risk; for a holder with fixed long payments, long bonds are the low-risk asset, so she is paid for holding what she would hold anyway | keep |
| 15 | H3-016 | 21 | LADDER, CERTAINTY | The riskless asset depends on the liability: for a long-horizon investor cash is risky (its rate rolls over); the matched long bond is riskless | keep |
| 16 | H3-024 | 21 | CERTAINTY, LADDER | Surplus optimisation: measure risk as assets minus liabilities, not assets alone | keep |
| 17 | H3-026 | 21 | CERTAINTY, HALFKEPT | Mental accounts can be efficient: separate goal pots with a shortfall limit each map to a mean-variance solution | keep |
| 18 | H3-045 | 21 | COSPONSOR, HALFKEPT | The entrepreneur's own stake signals project quality to outside financiers | keep |
| 19 | H3-046 | 21 | COSPONSOR | Cheap talk: when interests differ, only coarse messages are credible, and they take the form of an interval | keep |
| 20 | H3-047 | 21 | COSPONSOR | Seed money and leadership gifts raise later giving: an announced seed of 67% of the goal (vs 10%) gave "a nearly sixfold increase in contributions" (donors 3.7% to 8.2%, mean gift $15.42 to $39.87); … | keep |
| 21 | H3-049 | 21 | TWOREASONS | Time inconsistency: plans that look best today are abandoned when the future self differs | keep |
| 22 | H3-061 | 21 | FLOOR, MOVE2031, COSPONSOR | Knightian uncertainty and ambiguity: risk has known odds, uncertainty does not, and people rightly avoid unknown odds | keep |
| 23 | H3-064 | 21 | OTHER, RESERVE2033 | Yale's spending rule blends a fixed-dollar draw and a fixed-share draw: "80% of the prior year's spending plus 20% of the long-term spending rate" (5.25%), bounded 4.0-6.5% | keep |
| 24 | H3-065 | 21 | CERTAINTY, RESERVE2033, CEILING | US law splits a "sum certain" trust (annuity trust; "no additional contributions ... after the initial contribution") from "a fixed percentage of the net fair market value ... determined annually" (u… | keep |
| 25 | H3-066 | 21 | CERTAINTY | A legal number for "high degree of certainty": a sum-certain charitable trust fails if the chance it runs out "is greater than 5 percent", worked out at one assumed rate with a mortality table | keep |
| 26 | H3-067 | 21 | REINVEST, CERTAINTY | The IRS test "assumes that the section 7520 rate in existence at creation will be the rate of growth ... throughout its life"; when rates fell, trusts failed it | keep |
| 27 | H3-069 | 21 | LADDER, CERTAINTY | US law's way to fund a court-ordered fixed payment schedule: a "qualified funding asset" is "any obligation of the United States" bought within 60 days of the promise | keep |
| 28 | H3-070 | 21 | FLOOR, COSPONSOR | A lottery annuity prize is "the actual amount purchased", not the advertised one | keep |
| 29 | H3-071 | 21 | FLOOR, HALFKEPT | Securities in lieu of retainage: a contractor may post securities instead of cash retention and still owns them | keep |
| 30 | H3-073 | 21 | PROCESS, OTHER | Theatre cue lists and the "Block" command; a stage-management handbook | keep |
| 31 | H3-074 | 21 | CERTAINTY, HALFKEPT | A legal order of priority between sovereign funds: Chile's bill ranks the pension fund over the stabilisation fund ("orden de prelación") | keep |
| 32 | H3-075 | 21 | TWOREASONS | Norway's budget rule: "major changes in Fund value should not immediately entail major changes in Fund spending" | keep |
| 33 | H3-077 | 21 | TWOREASONS | Escape clauses come with a repair plan: Germany's emergency exception to the debt brake "ist mit einem Tilgungsplan zu verbinden"; the EU's general escape clause (2020) | keep |
| 34 | H3-079 | 21 | COSPONSOR | IPO price ranges miss often: below/within/above the file range 33/45/22% (2001-2019) and 16/55/29% (2020-2025); underwriters adjust only partly and price up to prevent withdrawal | keep |
| 35 | H3-081 | 21 | COSPONSOR | Weather forecasts: stating uncertainty improves users' decisions; protect when the probability exceeds the cost/loss ratio | keep |
| 36 | H3-083 | 21 | MOVE2031, COSPONSOR | A university will not start a building on pledges: 100% of a capital gift in cash before the award (85% exception) | keep |
| 37 | H3-086 | 21 | HALFKEPT, MOVE2031, COSPONSOR | Farmers hedge only part of the expected crop (best ratio 20-31% of expected production): in the 2012 drought, those who sold forward more than they harvested had to buy back dear | keep |
| 38 | H3-089 | 21 | CERTAINTY, LADDER, PROCESS | Escrow sufficiency verification: when a city defeases bonds, an independent agent recomputes that the escrow meets every payment; the Treasury issues custom-dated SLGS for this, which Laura cannot buy | keep |
| 39 | H3-090 | 21 | CERTAINTY, LADDER, FLOOR | Solvency II's matching-adjustment test: matched assets must be ring-fenced, held to maturity, with fixed cash flows in the liability's currency; assets whose cash flows are not fixed are haircut | keep |
| 40 | H3-093 | 21 | COSPONSOR, MOVE2031, FLOOR | R02 Aha 2: a range is what game theory says a credible promise looks like, and owned money makes it a costly signal; seed money raises later gifts | keep |

## The thinnest parts (fewest ideas rated B or better)

- INFLATION_TWD (Inflation, Taiwan costs, the Taiwan dollar): 33 rated B or better, 39 in all.
- RESERVE2033 (The operating reserve from 2033): 48 rated B or better, 54 in all.
- CAREER (Laura's career as an unsellable stock): 51 rated B or better, 56 in all.
- COMPLETE2028 (The 2028 deposit completes the ladder): 59 rated B or better, 66 in all.
- REINVEST (Reinvesting the ladder's interest): 79 rated B or better, 97 in all.
- TWOREASONS (Only two reasons to change): 89 rated B or better, 96 in all.
- MOVE2031 (The move into Treasuries before 2031): 90 rated B or better, 99 in all.
- HALFKEPT (Half the shares promised to no one): 91 rated B or better, 98 in all.
