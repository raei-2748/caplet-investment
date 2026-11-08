# The insight store: every idea for the Final Report, ranked

Caplet, Book 14: "Keep a store of every single insight you have. They should be organised or categorised ... some kind of ranking or rating system ... You must not lose a thing." This page is the front door. It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.

## How it works

- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards in `cards/` in the same format.
- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags below). An idea can sit under several.
- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is 19 or more, B 15 to 18, C below 15.
- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why); merged (a duplicate, pointing to the row that carries it).
- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies them and records which rows have been judged.

## Where it stands

- **557 ideas** in the store; 0 judged so far, the rest on the first pass.
- Tiers: A 159, B 325, C 73; refused or merged 0.
- 86 ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).
- Rows per source: `harvest/H1_idea_bank_part1.md` 88; `harvest/H3_concepts_R02_R05_R06.md` 126; `harvest/H4_synergies_S1_S3_fusions.md` 190; `harvest/H5_synergies_S4_S6_R11.md` 153.

## The parts of the plan and the case

| Tag | What it covers | Ideas | Ranked list |
|---|---|---|---|
| CAREER | Laura's career as an unsellable stock | 29 | [by_tag/CAREER.md](store/by_tag/CAREER.md) |
| CERTAINTY | A high degree of certainty | 172 | [by_tag/CERTAINTY.md](store/by_tag/CERTAINTY.md) |
| LADDER | The ten Treasuries | 149 | [by_tag/LADDER.md](store/by_tag/LADDER.md) |
| COMPLETE2028 | The 2028 deposit completes the ladder | 47 | [by_tag/COMPLETE2028.md](store/by_tag/COMPLETE2028.md) |
| FLOOR | The 2032 Treasury fund (bottom of the range) | 84 | [by_tag/FLOOR.md](store/by_tag/FLOOR.md) |
| CEILING | VT (top of the range) | 127 | [by_tag/CEILING.md](store/by_tag/CEILING.md) |
| HALFKEPT | Half the shares promised to no one | 63 | [by_tag/HALFKEPT.md](store/by_tag/HALFKEPT.md) |
| MOVE2031 | The move into Treasuries before 2031 | 48 | [by_tag/MOVE2031.md](store/by_tag/MOVE2031.md) |
| RESERVE2033 | The operating reserve from 2033 | 28 | [by_tag/RESERVE2033.md](store/by_tag/RESERVE2033.md) |
| TWOREASONS | Only two reasons to change | 47 | [by_tag/TWOREASONS.md](store/by_tag/TWOREASONS.md) |
| COSPONSOR | The 2031 range and the co-sponsors | 131 | [by_tag/COSPONSOR.md](store/by_tag/COSPONSOR.md) |
| INFLATION_TWD | Inflation, Taiwan costs, the Taiwan dollar | 24 | [by_tag/INFLATION_TWD.md](store/by_tag/INFLATION_TWD.md) |
| REINVEST | Reinvesting the ladder's interest | 53 | [by_tag/REINVEST.md](store/by_tag/REINVEST.md) |
| PROCESS | How the team decided and learned | 62 | [by_tag/PROCESS.md](store/by_tag/PROCESS.md) |
| OTHER | Other | 79 | [by_tag/OTHER.md](store/by_tag/OTHER.md) |

## The top 40 across the store (current ratings)

| Rank | Id | Score | Tags | Idea | Status |
|---|---|---|---|---|---|
| 1 | H1-006 | 21 | COSPONSOR, FLOOR | Announced lead money drives giving: raising announced seed money from 10% to 67% of the goal gave a nearly sixfold rise in contributions; matching above 1:1 adds nothing | keep |
| 2 | H1-023 | 21 | COSPONSOR, FLOOR, CEILING | Bottom = unconditional pledge, top = a variable amount set by a rule; in US nonprofit accounting a stated condition can make a pledge conditional, so never write "only if stocks hold" | keep |
| 3 | H1-081 | 21 | CERTAINTY, LADDER, TWOREASONS | Correlation makes the chain certain: ten payments fail if any one fails; ten independent 99% bets miss at least one about one time in ten (1 - 0.99^10 = 9.6%). One shared issuer makes them stand or f… | keep |
| 4 | H3-007 | 21 | FLOOR, LADDER, CERTAINTY | A defined-maturity ETF pays out its NAV, not par: IBTM "does not seek to return any predetermined amount at maturity", terminates about 15 Dec 2032, fee 0.07%; "Government backing ... does not apply … | keep |
| 5 | H3-011 | 21 | RESERVE2033, CERTAINTY, LADDER | Defeasance, and why accounting withdrew "in-substance" defeasance: risk-free bonds set aside for a debt make it as good as paid, but FASB stopped allowing it (1996) because the borrower could still b… | keep |
| 6 | H3-013 | 21 | CERTAINTY, LADDER | A US default is really a political delay; every rung matures before its payment (IBTM about 15 Dec 2032; the Feb-2037 bond about ten months before 1 Jan 2038), so a delay of weeks would not stop a pa… | keep |
| 7 | H3-015 | 21 | LADDER, CERTAINTY | Term premium: long bonds usually pay a little extra for rate risk; for a holder with fixed long payments, long bonds are the low-risk asset, so she is paid for holding what she would hold anyway | keep |
| 8 | H3-016 | 21 | LADDER, CERTAINTY | The riskless asset depends on the liability: for a long-horizon investor cash is risky (its rate rolls over); the matched long bond is riskless | keep |
| 9 | H3-024 | 21 | CERTAINTY, LADDER | Surplus optimisation: measure risk as assets minus liabilities, not assets alone | keep |
| 10 | H3-026 | 21 | CERTAINTY, HALFKEPT | Mental accounts can be efficient: separate goal pots with a shortfall limit each map to a mean-variance solution | keep |
| 11 | H3-045 | 21 | COSPONSOR, HALFKEPT | The entrepreneur's own stake signals project quality to outside financiers | keep |
| 12 | H3-046 | 21 | COSPONSOR | Cheap talk: when interests differ, only coarse messages are credible, and they take the form of an interval | keep |
| 13 | H3-047 | 21 | COSPONSOR | Seed money and leadership gifts raise later giving: an announced seed of 67% of the goal (vs 10%) gave "a nearly sixfold increase in contributions" (donors 3.7% to 8.2%, mean gift $15.42 to $39.87); … | keep |
| 14 | H3-049 | 21 | TWOREASONS | Time inconsistency: plans that look best today are abandoned when the future self differs | keep |
| 15 | H3-061 | 21 | FLOOR, MOVE2031, COSPONSOR | Knightian uncertainty and ambiguity: risk has known odds, uncertainty does not, and people rightly avoid unknown odds | keep |
| 16 | H3-064 | 21 | OTHER, RESERVE2033 | Yale's spending rule blends a fixed-dollar draw and a fixed-share draw: "80% of the prior year's spending plus 20% of the long-term spending rate" (5.25%), bounded 4.0-6.5% | keep |
| 17 | H3-065 | 21 | CERTAINTY, RESERVE2033, CEILING | US law splits a "sum certain" trust (annuity trust; "no additional contributions ... after the initial contribution") from "a fixed percentage of the net fair market value ... determined annually" (u… | keep |
| 18 | H3-066 | 21 | CERTAINTY | A legal number for "high degree of certainty": a sum-certain charitable trust fails if the chance it runs out "is greater than 5 percent", worked out at one assumed rate with a mortality table | keep |
| 19 | H3-067 | 21 | REINVEST, CERTAINTY | The IRS test "assumes that the section 7520 rate in existence at creation will be the rate of growth ... throughout its life"; when rates fell, trusts failed it | keep |
| 20 | H3-069 | 21 | LADDER, CERTAINTY | US law's way to fund a court-ordered fixed payment schedule: a "qualified funding asset" is "any obligation of the United States" bought within 60 days of the promise | keep |
| 21 | H3-070 | 21 | FLOOR, COSPONSOR | A lottery annuity prize is "the actual amount purchased", not the advertised one | keep |
| 22 | H3-071 | 21 | FLOOR, HALFKEPT | Securities in lieu of retainage: a contractor may post securities instead of cash retention and still owns them | keep |
| 23 | H3-073 | 21 | PROCESS, OTHER | Theatre cue lists and the "Block" command; a stage-management handbook | keep |
| 24 | H3-074 | 21 | CERTAINTY, HALFKEPT | A legal order of priority between sovereign funds: Chile's bill ranks the pension fund over the stabilisation fund ("orden de prelación") | keep |
| 25 | H3-075 | 21 | TWOREASONS | Norway's budget rule: "major changes in Fund value should not immediately entail major changes in Fund spending" | keep |
| 26 | H3-077 | 21 | TWOREASONS | Escape clauses come with a repair plan: Germany's emergency exception to the debt brake "ist mit einem Tilgungsplan zu verbinden"; the EU's general escape clause (2020) | keep |
| 27 | H3-079 | 21 | COSPONSOR | IPO price ranges miss often: below/within/above the file range 33/45/22% (2001-2019) and 16/55/29% (2020-2025); underwriters adjust only partly and price up to prevent withdrawal | keep |
| 28 | H3-081 | 21 | COSPONSOR | Weather forecasts: stating uncertainty improves users' decisions; protect when the probability exceeds the cost/loss ratio | keep |
| 29 | H3-083 | 21 | MOVE2031, COSPONSOR | A university will not start a building on pledges: 100% of a capital gift in cash before the award (85% exception) | keep |
| 30 | H3-086 | 21 | HALFKEPT, MOVE2031, COSPONSOR | Farmers hedge only part of the expected crop (best ratio 20-31% of expected production): in the 2012 drought, those who sold forward more than they harvested had to buy back dear | keep |
| 31 | H3-089 | 21 | CERTAINTY, LADDER, PROCESS | Escrow sufficiency verification: when a city defeases bonds, an independent agent recomputes that the escrow meets every payment; the Treasury issues custom-dated SLGS for this, which Laura cannot buy | keep |
| 32 | H3-090 | 21 | CERTAINTY, LADDER, FLOOR | Solvency II's matching-adjustment test: matched assets must be ring-fenced, held to maturity, with fixed cash flows in the liability's currency; assets whose cash flows are not fixed are haircut | keep |
| 33 | H3-093 | 21 | COSPONSOR, MOVE2031, FLOOR | R02 Aha 2: a range is what game theory says a credible promise looks like, and owned money makes it a costly signal; seed money raises later gifts | keep |
| 34 | H3-094 | 21 | CAREER, COMPLETE2028 | R02 Aha 3: the 2028 deposit and the ladder's main risk move together: yields fall in a weak economy (the ladder costs more) just when advances, speaking and licensing shrink | keep |
| 35 | H3-100 | 21 | LADDER | The off-the-run discount: older Treasuries yield a little more than new ones because traders pay for liquidity; a buyer who never sells earns that spread | keep |
| 36 | H3-104 | 21 | CAREER, REINVEST, HALFKEPT | Wrong-way risk and the stock-bond regime: Treasuries rise when shares crash in deflationary recessions but fall with them in inflationary ones (2022); the ladder's coupon leak is largest in the same … | keep |
| 37 | H3-106 | 21 | COSPONSOR, CERTAINTY | Interval scoring and Goodhart: a "99% inside the range" figure that is right by construction carries no information; state the chance of reaching the top and the size of any shortfall instead | keep |
| 38 | H3-109 | 21 | FLOOR, COSPONSOR | Conditional vs unconditional promises to give: a US nonprofit books an unconditional pledge at once but not one with a "barrier"; courts may enforce charitable pledges without proof of reliance | keep |
| 39 | H3-112 | 21 | INFLATION_TWD, HALFKEPT | Baumol's cost disease and the Taiwan-dollar shock: labour-heavy arts organisations face costs rising faster than prices; the Taiwan dollar jumped more than 6% in two days in May 2025, the most since … | keep |
| 40 | H3-120 | 21 | CERTAINTY, LADDER | R05 S3: three professions use one test of "already paid": fixed cash flows landing before each payment, a wall so nothing else draws on them, and no route to a forced sale | keep |

## The thinnest parts (fewest ideas rated B or better)

- INFLATION_TWD (Inflation, Taiwan costs, the Taiwan dollar): 19 rated B or better, 24 in all.
- RESERVE2033 (The operating reserve from 2033): 24 rated B or better, 28 in all.
- CAREER (Laura's career as an unsellable stock): 26 rated B or better, 29 in all.
- REINVEST (Reinvesting the ladder's interest): 42 rated B or better, 53 in all.
- COMPLETE2028 (The 2028 deposit completes the ladder): 43 rated B or better, 47 in all.
- MOVE2031 (The move into Treasuries before 2031): 43 rated B or better, 48 in all.
- TWOREASONS (Only two reasons to change): 43 rated B or better, 47 in all.
- PROCESS (How the team decided and learned): 57 rated B or better, 62 in all.
