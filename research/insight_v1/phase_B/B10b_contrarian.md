# B10b Contrarian: attack "lock early" from the case designers' and semifinal readers' side

Agent B10b, insight_v1 run, Phase B (question generation), written 2026-09-27. Lens: Contrarian (attack our own
strategy). Starting angle: read the case the way its designers built it, with 2031 and 2033 as decision points and
the operating reserve's "size and initial asset composition" asked for at the beginning of 2033. Then ask: does lock
early answer the question Wharton asked, or step around it? Where would a smart rival look more tailored, creative or
complete to a semifinal reader?

This file is AI-generated research for Team Caplet (Claude Code). It holds questions, evidence, numbers and
checklists. It holds no text meant for submission. The six students decide and write every deliverable in their own
words, and record AI use in the Final Report's Works Cited (R-W46). No finale material.

Status labels: VERIFIED-PRIMARY (VP), VERIFIED-REPO-FILE (VRF), SNIPPET-UNVERIFIED, ASSUMPTION (ASM),
INTERPRETATION (INT), DERIVED (my arithmetic on labelled inputs).

---

## 0. Summary (read this first)

My verdict after attacking it: **lock early survives as the right architecture. But three of the reasons we give for
it are weaker than we think, and in four places the plan could read as generic or evasive to a semifinal reader.**

1. **The designers wrote the case around a glide path, and our plan's equity path is a hump.** Wharton's own example
   note buys a Treasury fund to "begin preparing" for the commitment "as the residency funding date approaches"
   (R-T23, R-T25, VRF). The new 2026-27 Competition Guide asks "which principles will guide decisions as funding dates
   approach and payments are made" (VP, see section 5). Under lock early, whole-portfolio equity is about **1.5% on
   1 Jan 2027**, **20.4% after the 2028 deposit** (F-409) and about **4% after the 2031 floor lock** (DERIVED, script
   below). A reader expecting "less risk as the date nears" sees risk *rise* first. That is correct (risk capacity
   switches on with the 2028 deposit), but it must be explained in one clause or it reads as incoherent (Q2, Q16).
2. **NEW NUMBER: with the 2028 deposit present, "lock everything" is not what makes the payments certain.** I re-ran
   the verified model's inputs with partial locks (script `research/insight_v1/scripts/B10b_designer_checks.py`,
   ASM-based). With the full $150k deposit, which the case says she "will" make (R-C27, R-AN35), locking **70%, 80%,
   90% or 95%** of the ladder also gives **0.00% payment shortfall** in 200,000 paths, and a *slightly higher* median
   2033 surplus ($212.6k at 80% vs $210.4k at 100%). Locking nothing gives 2.1% shortfall and +$10.6k median. So the
   honest reason to lock 100% is the **facility range and the stressed deposit**, not payment certainty in the case's
   base. The p5 surplus falls from $150k (100% lock) to $128k (80%) and $117k (70%). If the IPS or Final Report
   claims "anything less than a full lock fails", a statistics-trained reader can falsify it (Q4).
3. **The case's numbers were probably not set so that $300k buys the promise.** The ladder cost more than $300k on
   173 of 185 trading days in 2026 (F-111). If the January 2027 curve looks like January-August 2026, "the first
   deposit buys the whole promise" disappears. A rate-robust headline survives: DERIVED (flat-curve ASM), the two
   deposits together still buy the full ladder unless rates fall about **420bp**; with a half-size 2028 deposit, about
   **250bp**. So "fully funded by January 2028 at the latest" is robust where "fully funded on day one" is not (Q3).
4. **The reserve answer can look like a dodge unless it answers the three things asked, in the case's words.** The
   case wants the reserve's size, initial composition and how composition changes (R-C52, R-C53). Lock early's honest
   answer is "it is the 2027 ladder, and it changes by itself". That is allowed ("if at all", R-AN27). It becomes an
   *answer* only with numbers: DERIVED (flat 5.35% ASM) the held ladder's duration rolls down from **about 4.1 years
   on 1 Jan 2033 to 0 in 2042**, with no trades. That is a glide path in maturity, not in stocks (Q1).
5. **The alternative most rivals will propose for the late payments, an equity "bucket" inside the reserve, costs
   1.8-2.6 times more.** DERIVED (JPM large-cap inputs, lognormal ASM): to pay the 2040, 2041 or 2042 payment from
   equities held from 2033 with 95% probability needs about **$59-62k** of stock per $50k payment. At 99% it needs
   about **$81k**. The Treasury price is about **$31-35k**. One line of this in the Final Report shows we tested the
   obvious rival design and why it loses (Q9).
6. **The case's premise "In 2031 ... the value of her portfolio in 2033 remains uncertain" (R-C65) is made almost
   false by our own 2031 rule.** Under an 80% floor lock the 2031 range is roughly ±5% (B6a, B6b). The case also says
   teams "must recommend the dollar range" (R-C68). A reader could see "we give Laura a rule, and the range is nearly a
   point" as avoiding the task the designers built. The fix is to give both: a dollar range from today's view and the
   2031 rule, and to say in one sentence why the range narrows (Q5).
7. **The biggest threat to what Laura's facility money buys is not markets; it is construction inflation.** DERIVED:
   Taiwan's construction cost index has risen about 3.5% a year since 2021 (F-508, F-509). Over 2026-2033 that is
   about **+27%**, against Taiwan CPI of about +15% at 2%. A two-year USD/TWD move has a standard deviation of about
   6.8% (F-513). The case asks for assumptions on "the effect of inflation on ... facility costs" (R-C85). A USD-only,
   nominal range answers the market question and misses the one the case names (Q17).
8. **Where a rival beats us on paper:** a crisp facility-and-flexibility rule (ours is "mainly leftover"), a year-by-year
   allocation picture, a stated confidence number for the payments, and a larger headline facility number bought with
   hidden payment risk. The last one we should expose, not match (Q7, Q11, Q18).

Question count: **21** (section 3). By deadline: WInS-now/TN 3, IPS 8, FR 10. Most of them change a sentence or a
chart. Q3, Q4 and Q7 could change a decision.

What is new versus Phase A and other Phase B files: the partial-lock frontier *with* the 2028 deposit (section 8
item 1 of the brief covered partial locks only with no deposit); the whole-portfolio equity path by year; the
equity-bucket cost ratio; the reserve duration roll-down; the rate fall that breaks "fully funded by 2028"; the
construction-inflation versus market-risk comparison; and a reading of the designers' glide-path language in the
Trading Notes example and the Competition Guide.

---

## 1. Method

1. Read the brief, v4 Parts 1-3, 5 and 6, CLAUDE.md, the case, both guides, the SMApply page, and the four Phase A
   files. Skimmed the summaries of all 18 Phase B files already written, so as not to repeat them (I name overlaps).
2. Read the 2026-27 Investment Competition Guide PDF myself (VP) and checked four quotes verbatim with
   `fetch_text.py --grep`.
3. Wrote down what a designer would expect from each case paragraph, then asked where lock early departs from that
   expectation, and whether the departure is (a) better and explained, (b) better but unexplained, or (c) weaker.
4. Tested four attacks with numbers, using the verified model's inputs (script in section 6).
5. Searched Wharton Global Youth's own article archive (WordPress search API) for teaching content on bond ladders,
   glide paths or liability matching that might show the designers' intended toolkit. Result: nothing relevant
   (VP negative result, section 7). My WebSearch budget for this session was already used up (the tool refused all
   calls), so a few leads below are marked for specialists to find.

---

## 2. The designer's reading of the case, paragraph by paragraph (INT unless labelled)

| Case element (VRF) | What a designer probably pictured | What lock early does | Risk to us |
|---|---|---|---|
| "$300,000 ... $150,000" (R-C26, R-C27); $450k < $500k (R-AN13) | Money must grow to cover the promise; tension between growth and protection | Rates, not growth, close the gap; promise bought in 2027 | "Solved in year 1" can look like the case was sidestepped, and it depends on September 2026 rates (F-111) |
| Example note: "begin preparing ... as the residency funding date approaches" (R-T23, R-T25) | A glide path: growth first, bonds added gradually | All at once, now; equity rises in 2028 | Reads as the opposite of the model answer unless explained |
| "set aside ... at the beginning of 2033" (R-C50) + "size and initial asset composition" (R-C52) + change "if at all" (R-C53) | A reserve built in 2033 from a pooled portfolio, with a composition to choose | Relabel the 2027 ladder in 2033; no trades | Terse answer can look like a dodge |
| "2031 is Year 5" (R-C29); range + confidence (R-C67 to R-C69); "remains uncertain" (R-C65) | A real forecasting problem two years out | Floor bought; range nearly a point | Looks like we avoided the uncertainty task |
| "no predetermined facility contribution"; "responsibly"; flexibility "as the project develops" (R-C57 to R-C60) | Teams choose a rule for how much to give and how much to keep | Facility = sleeve value; flexibility = leftover | Generic; no rule |
| "Teams may reach different conclusions about ... funding confidence" (R-C74) | Teams pick a confidence level | "Certain barring U.S. default" | No number; "how evaluated" may look thin (R-C55) |
| "the effect of inflation on portfolio projections and facility costs" (R-C85) | Real value of the facility money | USD nominal throughout | Misses a named assumption area |
| Guide: "how its components will support different needs" (VP) | Split portfolio by purpose | Ladder + sleeve | Strong fit; say it in these words |

---

## 3. Questions

Format for each: question; anchors; hypothesis (a guess, with evidence); what it would change; deliverables; domain;
seed; north-star link.

### Tier 1: WInS now and Trading Notes (Oct 23)

**Q15. Can three notes taken from a mostly-Treasury book show distinct roles, and do we already have a growth trade
with a proper note?**
- Anchors: Guide p.3 (R-new): a note should state the trade's "expected role in growth, liquidity, risk management, or
  future funding" (VP). R-T10 "Collectively, the decisions should demonstrate how your team used individual
  investments as part of a cohesive portfolio strategy" (VRF).
- Hypothesis (guess): if the book is about 80% hedge funds, the risk is three notes that all say "future funding".
  The four official role words give a ready test: aim for one "future funding" note, one "growth" note, one "risk
  management" note (a rule-driven rebalance or position-limit split). Overlap: B7b Q6 plans notes by "supported /
  tested / refined". This question plans them by *role*. Both can hold at once.
- Would change: which trades are placed in the next two weeks, and that each carries a role word in its note.
- Deliverables: WInS-now, TN. Domain: D9 (with D10 for rule checks). Seed: 30 (not in my list; null used).
- North star: shows Laura each dollar has a job she can name, not a pile of funds.

**Q16. Wharton's example note says "begin preparing" and "reduce portfolio volatility". What single fact lets our
hedge note explain "all at once, now" without contradicting the example?**
- Anchors: R-T23 (VRF): "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio
  volatility and begin preparing for Laura’s future operating commitment." R-T25: "as the residency funding date
  approaches".
- Hypothesis (guess): the example encodes the gradual glide path most teams will copy. Our note needs one number that
  shows why waiting is the risky choice. Candidates: the promise costs about $292k of her $300k today (F-101); a
  0.27% fall in rates uses up the headroom (F-104); and the ladder cost more than $300k on 173 of 185 days this year
  (F-111). B1a Q2 already flagged the "volatility" wording. What is new here is the word "begin" (gradualism).
- Would change: the wording checklist for the hedge note and its reflection.
- Deliverables: TN, WInS-now. Domain: D9. Seed: null.
- North star: shows we did not copy the template; we chose against it for a reason tied to her money.

**Q2. Our whole-portfolio equity share goes about 1.5% (2027) → 20% (2028) → 4% (2031). Will readers who expect a
glide path read this hump as incoherent, and what one clause explains it?**
- Anchors: R-I12 (VRF) "How will the portfolio’s asset allocation and composition change as future funding needs
  approach and payments are made?"; Guide (VP) "which principles will guide decisions as funding dates approach and
  payments are made"; F-409; R-T25.
- Evidence: DERIVED in `B10b_designer_checks.py`: 2027 sleeve $7,736 × 60% equity ÷ $300k = 1.5%. 2028: 20.4%
  (F-409). 2031 after an 80% floor lock, with a rough median sleeve of $190k (ASM) and the ladder at its forward value
  of $356,384 (F-106): 0.6 × 0.2 × 190 ÷ 546 ≈ 4.2%.
- Hypothesis (guess): the hump is right. Laura's ability to take risk exists only once the second deposit arrives
  (B9a: about 152% funded counting the 2028 money). It then falls as the facility date nears. That is a glide path
  for the *facility money*, and a zero-risk line for the *promise*. The clause must name both paths. A Final Report
  chart of "equity share by year, split promise/surplus" makes it obvious.
- Would change: an IPS sentence on how the allocation changes over time; a Final Report chart; a TN reflection if WInS
  shows about 20% equity while Laura's 2027 book is about 1.5% (already flagged in `wins_now/`; the new part is the
  whole path).
- Deliverables: IPS, FR, TN. Domain: D7 (with D3 for the chart data). Seed: 29.
- North star: a plan whose risk follows her cash flows, not a textbook age rule.

### Tier 2: IPS (Nov 6)

**Q3. Should the IPS headline promise "fully funded by January 2028 at the latest" instead of "the $300,000 buys the
promise", because the second claim is a September-2026 accident?**
- Anchors: F-111 (ladder above $300k on 173 of 185 trading days in 2026; $316.5k on Jan 2); F-112 (about 24% chance it
  costs more than $300k on 2027-01-01, ASM); R-C26, R-C27; R-AN13.
- Evidence: DERIVED (flat-curve, parallel-shift ASM, so a rough guide): the ten payments cost $300k at a flat 5.09%, a
  fall of about 27bp. $300k plus the 2028 deposit's present value ($143,230, per B9a) covers the ladder down to a
  flat 1.16%, a fall of about 420bp. With a $75k deposit the threshold is about 2.90%, a fall of about 250bp.
- Hypothesis (guess): the designers set round numbers before September's rate rise, when $300k did *not* buy the
  promise. They probably expected both deposits and some growth to be needed. A headline that depends on today's
  curve can break before the money even arrives. A funded-ratio rule ("hedge as much as the money buys, finish with
  the 2028 deposit") keeps the same plan and survives any plausible January curve. Overlap: B2a Q4 (rate-conditional
  lock rule). New here: the 420bp/250bp break points and the proposal to move the *headline*, not just the rule.
- Would change: the elevator pitch and first IPS sentence (decision on what we promise), plus one Final Report
  sensitivity line.
- Deliverables: IPS, FR. Domain: D3 (verify with the zero curve, not a flat rate), D1. Seed: 4.
- North star: she gets a promise that does not depend on luck with the calendar.

**Q4. With the 2028 deposit present, a 70-95% lock also shows no payment shortfall in the model. So what is our real
reason to lock 100%, and are we overstating it anywhere?**
- Anchors: R-C47 "high degree of certainty"; R-C74 "Teams may reach different conclusions about ... funding
  confidence"; R-AN35 ("will contribute"); F-401; F-410 (partial locks fail only in the no-deposit case).
- Evidence (DERIVED, `B10b_designer_checks.py`; ASM: 60/40 money outside the lock, JPM inputs, 2033 reserve at a flat
  5.26% ± 1pp, no 2031 floor):

  | Lock share | Shortfall ($150k deposit) | Surplus p5 / p50 / p95 | Shortfall ($75k deposit) |
  |---|---|---|---|
  | 100% | 0.00% | $150k / $210k / $299k | 0.00% |
  | 90% | 0.00% | $139k / $212k / $318k | 0.00% |
  | 80% | 0.00% | $128k / $213k / $337k | 0.00% |
  | 70% | 0.00% | $117k / $214k / $357k | 0.08% |
  | 50% | 0.02% | $93k / $216k / $396k | 1.74% |
  | 0% | 2.10% | $34k / $221k / $496k | 11.72% |

- Hypothesis (guess): the full lock is still the best choice. It costs about $2-3k of median against an 80% lock, and
  it buys $22k more at p5, a much narrower facility range and immunity to a smaller deposit. But "anything less
  fails" is false in the case's own base. The true sentence is about the *price of certainty*: about $11k of median
  facility money (about 5%) removes a roughly 2% chance of breaking the promise and lifts the bad-case facility money
  by about $116k. Caveat: this model's 1pp rate spread for 2033 may understate how far rates can fall (F-406 widens
  it).
- Would change: the reasoning sentence in the IPS; the Final Report comparison table (add the frontier); and the
  "why not a partial lock" answer in the Final Report.
- Deliverables: IPS, FR. Domain: D3. Seed: 26.
- North star: a statistics graduate gets the true trade-off, priced, instead of a claim she could disprove.

**Q12. Lock early settles the promise in January 2027. Does the IPS still show a full "decision-making framework"
for the six years the designers built around 2031 and 2033?**
- Anchors: R-C89 "formally establishes the strategy and the team’s decision-making framework"; R-I23; R-AN11 (the
  timeline lists only event years); Guide (VP) "planned adjustments as funding dates approach".
- Hypothesis (guess): yes, if each decision point is written as trigger → action → record. Candidates: (1) January 2027
  purchase if the ladder costs more than the money; (2) the 2028 deposit order of use; (3) sleeve rebalancing band;
  (4) the 2031 floor share; (5) the 2033 facility rule; (6) the flexibility rule; (7) what Laura is shown each year
  (funded ratio, BS-09). The council panel scored plain "static lock + sleeve" 6/10 on Creativity because it reads
  as "safe bucket plus growth bucket" (`02_judge_panel.md`, AI panel, low authority). The rules are what separate us.
- Would change: an IPS structure checklist (which rules must appear in 500 words). The Guide forbids redesign after the
  results, so every contingent rule has to be in the IPS (B1a Q8).
- Deliverables: IPS. Domain: D7, D8. Seed: 5.
- North star: she sees what we will do at each date she has marked, before it happens.

**Q13. Will a first-screen reader see about 1.5% equity in 2027 and about 20% after 2028 as timid for a client who
"has been willing to take thoughtful risks", and which single number reframes it?**
- Anchors: R-C37, R-C38; R-S25 "risk considerations"; F-409; brief section 8 item 3 (risk measured on the surplus).
- New evidence: the 2027 figure (1.5%) is the one WInS literally represents (WInS = her $300k, R-AN14), so it is the
  one readers see first. Readers include Wharton student evaluators before the asset managers (B7a).
- Hypothesis (guess): the reframing number is "60% of the money the promise does not need". Better still is one
  sentence on why the promise is not the place for her risk: career risk already sits in her income (B9a Q5, DOSPERT).
  Do not argue with total-portfolio percentages.
- Would change: an IPS sentence; the order of numbers in the Final Report.
- Deliverables: IPS, FR. Domain: D6. Seed: null.
- North star: honours her risk appetite where it cannot hurt her promise.

**Q14. Criterion 1 says "uses appropriate diversification". Which argument will a fixed-income reader accept for a
2027 book that is about 97% one issuer (the U.S. Treasury)?**
- Anchors: R-S24; R-W71 "diversification across asset classes, sectors, industries, market capitalizations,
  geographic regions, risk characteristics, and funding purposes" (VP); R-AN45.
- Hypothesis (guess): (a) diversification by *funding purpose* uses Wharton's own word list; (b) diversifying a matched
  hedge *adds* risk to a fixed-dollar promise; (c) the sleeve is broadly diversified. Say (a) and (b) in one clause.
  Do not add a foreign bond to "look diversified".
- Would change: one IPS clause; the Portfolio Analysis framing in the Final Report.
- Deliverables: IPS, FR. Domain: D1. Seed: null.
- North star: shows we understand why her promise should not be spread around.

**Q20. The IPS guide names "liquidity" repeatedly. Where is liquidity in lock early, and does one clause cover it?**
- Anchors: R-I6 ("liquidity needs"), R-I11, R-I21, R-I26; R-C33, R-C34 (no withdrawals before 2033); BS-07 (plan delay).
- Hypothesis (guess): liquidity need before 2033 is nil by the case. After 2033 the reserve pays itself out each
  January. U.S. Treasuries are among the most liquid securities if the residency is delayed. STRIPS (zero-coupon
  Treasuries) trade less actively than notes; D1 should check. One clause suffices. A rival's "cash bucket" answers
  a need Laura does not have.
- Would change: one IPS clause.
- Deliverables: IPS. Domain: D1. Seed: null.
- North star: no idle cash held for needs she has told us she does not have.

**Q19. Is lock early now the textbook answer that AI tools hand every team, and what 2-3 Laura-specific decisions are
missing from a generic liability-matching plan?**
- Anchors: R-S24 "clear and creative investment thesis"; R-S28 "original thinking"; BS-10; R-W26 (AI allowed for
  brainstorming).
- Hypothesis (guess): at 5% yields, AI assistants given the case will often suggest a Treasury ladder plus a growth
  bucket plus a Monte Carlo "95%". A cheap test: paste the public case into two or three AI tools, record the
  architecture each proposes, and record this use in Works Cited. Our likely distinctive parts: the bought 2031
  floor, a certainty definition that needs no model, the funded-ratio headline (Q3), and the price-of-certainty
  frontier (Q4). Overlap: B7b's field simulation. New here: an actual test, not an assumption.
- Would change: which ideas get the IPS's scarce words (decision).
- Deliverables: IPS, FR. Domain: D7. Seed: 29.
- North star: the answer to "why us" cannot be the part every rival also has.

### Tier 3: Final Report (Dec 4)

**Q1. Does "it is the 2027 ladder, and it changes by itself" answer the case's reserve question, or will it read as a
dodge? What must the answer contain?**
- Anchors: R-C50, R-C52 ("Teams must recommend its size and initial asset composition"), R-C53 ("if at all"), R-AN27,
  R-AN28; brief section 8 item 9.
- Evidence: DERIVED (flat 5.35% ASM; the official forward value is $394,930, F-106): value before each payment and
  Macaulay duration (average time to the payments) run $399.9k / 4.07y (2033), $300.9k / 2.79y (2036), $142.5k / 0.97y
  (2040), $50k / 0y (2042).
- Hypothesis (guess): allowed and strong, *if* it names all three items: size (market value on 1 Jan 2033, plus face
  $500k), composition (ten zero-coupon rungs, one per January), change (automatic maturity roll-down, no trading,
  shown as a chart). It also needs the one sentence "funded 2027, designated 2033" (brief 8.9). A bare "the ladder"
  answer risks being scored as not engaging.
- Would change: a Final Report checklist and a roll-down chart.
- Deliverables: FR. Domain: D1, D9. Seed: 5.
- North star: she can see exactly what sits in her reserve every year.

**Q9. Should the Final Report show that the most common rival reserve design, an equity "bucket" for the late
payments, costs 1.8-2.6 times the Treasury price?**
- Anchors: R-C52, R-C53, R-C47; R-S26 "integrates quantitative and qualitative analysis".
- Evidence: DERIVED (`B10b_designer_checks.py`; JPM large cap 6.70% compound, 16.47% volatility; lognormal ASM):

  | Payment | Equity needed in 2033 at 95% | at 99% | Treasury price (flat 5.35% ASM) | Ratio |
  |---|---|---|---|---|
  | 2040 | $61.5k | $80.9k | $34.7k | 1.77x / 2.33x |
  | 2041 | $60.4k | $80.9k | $33.0k | 1.83x / 2.46x |
  | 2042 | $59.1k | $80.6k | $31.3k | 1.89x / 2.58x |

- Hypothesis (guess): one line showing "we tested it, it costs nearly double for less certainty" beats a page
  defending the ladder. The figures are model outputs, not forecasts.
- Would change: one Final Report sentence or small table; it also strengthens the Articulation story (an alternative
  tested and rejected).
- Deliverables: FR. Domain: D3. Seed: 26.
- North star: she sees we checked the tempting option with her statistics toolkit.

**Q10. Rivals who buy the reserve in 2033 at cautious rates will show reserves of about $405-440k. Will a reader read
our $395k as "smaller, so riskier"?**
- Anchors: R-C52; F-106 ($394,930 on 2033-01-01); F-110 ($405,391 at 5%, $421,767 at 4%, $439,305 at 3%); brief 8.9.
  New: the reader-comparison risk, not the choice of number.
- Hypothesis (guess): yes, for a first-screen reader. The fix is to show three numbers side by side once (cost $292k
  in 2027, value $395k in 2033, face $500k) and the phrase "the interest rate was locked in 2027".
- Would change: one Final Report sentence or table.
- Deliverables: FR. Domain: D9. Seed: null.
- North star: her promise looks as safe as it is.

**Q11. A certainty definition that needs no model can look as if we skipped "explain how they evaluated". What stress
table and residual-risk list prove it, and should the residual U.S. default risk carry a market-based number?**
- Anchors: R-C54, R-C55, R-C56; R-C82 "Addresses how investment uncertainty could affect both the operating
  commitment and the facility contribution"; R-S26 "evaluate funding reliability ... under varying market outcomes";
  R-C74 "funding confidence".
- Hypothesis (guess): the evaluation should be a table in which the payment row does not move: rates ±200bp, equities
  −40%, 2028 deposit $0 or late, TWD ±12%. The residuals are listed (Treasury default, operations, the rate move before
  purchase, coupon reinvestment if STRIPS are unavailable). A market-implied default probability from U.S. credit
  default swap (CDS) prices would give a number. I could not read one: the page I tried loads its data by JavaScript
  (section 7). Named models give probabilities to two significant figures at most (brief 8.6).
- Would change: a Final Report table; possibly one IPS clause giving a confidence number.
- Deliverables: FR, IPS. Domain: D3, D1. Seed: 9.
- North star: a statistics graduate sees the certainty claim tested, not asserted.

**Q5. The case says teams "must recommend the dollar range" and says the 2033 value "remains uncertain" in 2031. Our
2031 rule nearly removes that uncertainty. Do we give a dollar range today, a rule, or both, and how do we avoid the
"one exact amount" the case rejects?**
- Anchors: R-C65, R-C67 ("Rather than promising one exact amount"), R-C68 ("Teams must recommend the dollar range"),
  R-C69, R-C71, R-AN29 ("must").
- Evidence: 2031 floor p5/p50/p95 in today's view $127k / $165k / $217k (F-402). In a 2031 view the band is about
  ±4-5% (B6b). At 80% lock the range is about US$199-218k (B6a).
- Hypothesis (guess): both. Today's dollar range (with the model named) satisfies the "must". The 2031 rule shows how
  she will say it. One sentence explains why the range narrows: most of the uncertainty is gone by 2031, because the
  floor is bought. The width that remains should come from a *stated choice* (how much to keep flexible), not from
  markets. Overlap: B1a Q18, B6a Q7, B6b. New: the designer-premise framing and the literal "must".
- Would change: Final Report structure for the range section; the lock-share parameter (decision).
- Deliverables: FR. Domain: D5, D3. Seed: 9.
- North star: she can say one sentence to funders that stays true in 2033.

**Q6. Under a floor + cap rule, what happens to good-market money, and does sending it to "flexibility" weaken the
"meaningful contribution" signal the case describes?**
- Anchors: R-C64 "A meaningful personal contribution may signal that the residency is financially viable"; R-C70
  "explain how favorable and unfavorable market outcomes could affect the amount she can provide"; R-AN9.
- Hypothesis (guess): the case wants the favourable case to *affect the amount*. A hard cap makes the favourable case
  change only the leftover. A clean version: the range top is a promise ceiling, and upside above it is her choice in
  2033 (an extra gift or flexibility), stated as such. Funders count only the unconditional part (B6a Q1), so the cap
  costs nothing with them.
- Would change: the favourable-outcome sentence in the fundraising draft checklist and in the facility rule.
- Deliverables: FR. Domain: D5. Seed: 9.
- North star: good luck is hers to direct, and she never has to walk a number back.

**Q7. Our facility rule is "whatever the sleeve becomes" and flexibility is "mainly leftover". What crisp split rule
would a rival state, and what should ours be anchored to?**
- Anchors: R-C57, R-C58 ("committing all remaining assets could limit her financial flexibility as the project
  develops"), R-C60, R-C84, R-AN18, R-AN19, R-AN20 ("extent" may be a share or rule).
- Hypothesis (guess): a rule such as "contribute the bought floor plus a stated share of the rest; keep the remainder
  as project flexibility". Candidate anchors: the case's own words about the project developing; Laura's staged
  scaling (B9a Q8); goal tiers (needs / wants / wishes, B4b). The share is the team's decision. Without a rule, the
  "responsible" criterion is met by assertion only.
- Would change: a decision (the split), an IPS clause, a Final Report table.
- Deliverables: IPS, FR. Domain: D5, D6. Seed: 11.
- North star: she keeps room to act as the residency grows, which is how she has built everything.

**Q8. Could part of the facility money be given in a second tranche after 2033, tied to project milestones, or does
the case's 2033 framing rule that out?**
- Anchors: R-C63 "how much she expects to contribute toward the facility in 2033"; R-C57; R-C58 "as the project
  develops"; R-C61 (no contingency fund needed).
- Hypothesis (guess): the co-sponsor range must describe the 2033 contribution, so a staged gift cannot be part of the
  range. It can be named as one possible use of the flexibility money. More than one sentence risks looking like a
  misread of the case.
- Would change: one Final Report sentence (or a decision not to mention it).
- Deliverables: FR. Domain: D5, D7. Seed: 11.
- North star: fits a founder who ships in stages, without bending the case.

**Q17. Which is bigger for what Laura's facility money buys by 2033: market risk, USD/TWD risk, or Taiwan
construction inflation? Does a USD-only nominal range miss the assumption the case names?**
- Anchors: R-C85 "the effect of inflation on portfolio projections and facility costs"; R-AN8; R-AN10; F-508, F-509,
  F-513, F-501.
- Evidence (DERIVED): construction cost index about 3.5%/yr since 2021 → about +27% over 2026-2033 (1.035^7 = 1.272).
  Taiwan CPI at 2% → about +15%. Two-year USD/TWD standard deviation about 6.8% (since 2006). The 2031-view market band
  is about ±5% (B6b).
- Hypothesis (guess): construction inflation dominates. A fixed US$ figure buys roughly a fifth less building in 2033
  than today if that trend holds (ASM: trend continues). The range stays in US$ (it protects the promise), but the
  Final Report needs one assumption line stating the purchasing-power effect. It does not need a facility-cost
  estimate (R-C95). Overlap: brief section 9 (TWD quote), B6b Q5. New: the ranking of the three risks.
- Would change: an assumption sentence and a possible small chart in the Final Report.
- Deliverables: FR. Domain: D4. Seed: null.
- North star: she is told what her gift will really buy, in the place she is building it.

**Q18. If rivals show $300k+ facility contributions from 8-10% return assumptions, should the Final Report show a
same-assumptions comparison (ours vs growth-first vs partial lock) so a first-screen reader sees what those numbers
cost in payment risk?**
- Anchors: R-S26 "uses reasonable assumptions and projections"; R-C77 "reasonable return assumptions"; F-401; F-301;
  B7b (a 2025-26 semifinalist reported "a 70% chance of reaching the long-term goal"); B1b (last season's "9%
  annualized" habit).
- Hypothesis (guess): yes, as one chart: median and p5 facility money against the chance of breaking the promise, for
  3-4 designs on the same JPM inputs (the Q4 frontier is the data). It turns "our number is smaller" into "our number
  is real".
- Would change: a Final Report chart (decision to include).
- Deliverables: FR. Domain: D3, D7. Seed: 29.
- North star: shows her the honest price of a bigger promise.

**Q21. Lock early decides early, so where is the genuine "challenge and adaptation" story that the Articulation
criterion scores?**
- Anchors: R-S27 "reflects meaningfully on the team's growth and response to challenges"; Guide (VP) "You may
  identify decisions you would make differently"; R-C88 "reflected, tested, or refined".
- Hypothesis (guess): real candidates already exist. The team's original growth-first plan was dropped on evidence.
  The September rate rise changed whether $300k buys the promise. A possible 25% position limit could force a
  three-fund hedge (G4). The WInS book was changed from the post-2028 mirror to the 2027 reality. Each needs a dated
  decision-log entry now. The council's AI panel scored the static version 6/10 on Articulation ("little process to
  narrate"; low authority).
- Would change: start a dated decision log this week; pick one Trading Note as "refined".
- Deliverables: WInS-now, TN, FR. Domain: D7. Seed: 31 (null used in the summary).
- North star: she hires people who changed their minds for good reasons.

---

## 4. Attacks I tested that failed (parked, with reasons)

- **"An equity bucket inside the reserve would honour her risk appetite."** Fails on cost (Q9: 1.8-2.6x).
- **"Wait until 2033 and buy the reserve then."** Already answered (brief 8.1). No new evidence.
- **"Tiering: roll 2037-42 short."** Already answered (brief 8.2).
- **"TIPS for the reserve."** Already answered (brief 8.10).
- **"More equity in the sleeve would lift the facility enough to matter."** Already answered (brief 8.5); B9b adds
  the 0% control. Not re-asked.
- **"WInS should hold 35% equity."** Already dropped in `wins_now/securities_and_allocation_v0.md` (no plan version
  holds it).

---

## 5. Evidence found (with status)

1. **2026-27 Investment Competition Guide** (5 pages), https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf,
   read 2026-09-27, VERIFIED-PRIMARY. Verbatim checks passed for:
   - "you will need to decide how to construct and diversify the portfolio, how its components will support different
     needs, how the portfolio's asset composition may change over time, and which principles will guide decisions as
     funding dates approach and payments are made." (p.2)
   - "the Trading Note should capture the reasoning behind the decision, including its alignment with your strategy,
     the supporting research or analysis, and its expected role in growth, liquidity, risk management, or future
     funding." (p.3)
   - "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten
     simply because markets move or hindsight reveals a different outcome." (p.5)
   - Also on p.2: "The goal is to develop a cohesive strategy in which your investment decisions work together to
     support the client's objectives across a range of possible market outcomes."
   First found by B1b/B7a/B7b. Not yet in `competition/official/2026_27/` (main loop's decision).
2. **Trading Notes example** (R-T23 to R-T25), VRF: "begin preparing", "as the residency funding date approaches".
3. **Model outputs** (DERIVED, ASM inputs as labelled): `research/insight_v1/scripts/B10b_designer_checks.py`, run
   2026-09-27, runtime about 1 second, seed 20260927, 200,000 paths. Results in section 3 (Q2, Q4, Q9, Q1).
4. **Break-even rate falls** (DERIVED, flat-curve ASM, inline Python run 2026-09-27): cost $300k at 5.09% (−27bp);
   $371,615 at 2.90% (−246bp); $443,230 at 1.16% (−420bp).

## 6. Script

`research/insight_v1/scripts/B10b_designer_checks.py`. Run from the repo root with
`.venv/bin/python research/insight_v1/scripts/B10b_designer_checks.py`. The docstring lists inputs and status. Main
limits: no 2031 floor in the frontier (so the 100% row's p5 is $150k, not the verified $159k); the 2033 reserve uses a
flat 5.26% ± 1pp, which slightly overstates its cost (F-408); sleeve bonds earn JPM's 4.0%, which is conservative
against today's yields (F-317; B9a Q4); i.i.d. lognormal returns; no fees.

## 7. Sources (all accessed 2026-09-27)

| Source | URL / path | Status |
|---|---|---|
| Investment Competition Guide 2026-27 | https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf | VERIFIED-PRIMARY |
| Client case | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` | VERIFIED-REPO-FILE |
| IPS guide | `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` | VERIFIED-REPO-FILE |
| Trading Notes guide | `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` | VERIFIED-REPO-FILE |
| SMApply criteria | `competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md` | VERIFIED-REPO-FILE |
| Phase A registers | `research/insight_v1/phase_A/*.md` (R-, F-, BS-, G- ids) | as labelled there |
| Verified model | `research/verified_2026-09-27/strategy_mc.py` | VERIFIED-REPO-FILE inputs |
| Wharton Global Youth article search (WordPress API) | https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/posts?search=... ("bond ladder", "glide path", "liability", "treasury", "target date") | VERIFIED-PRIMARY negative result: no teaching article on these topics found |
| U.S. 5-year CDS page | https://www.worldgovernmentbonds.com/cds-historical-data/united-states/5-years/ | Not usable: values load by JavaScript, the text shows "----" |
| WebSearch | tool | Refused: session search budget (200) already used |
| Council AI panel | `research/council_2026-09-27/02_judge_panel.md` | AI brainstorming, low authority |

## 8. Leads for the specialists

- **D3 (quant):** re-run the Q4 frontier with (a) the 2031 floor included, (b) sleeve bonds at a current yield
  (about 5%), (c) the 2033 rate spread widened to 1.5-2pp, and (d) the 2028 deposit correlated with a bad 2027 equity
  year. Check whether 70-95% locks stay at 0% shortfall. Re-do the Q3 break-even with the zero curve (not a flat
  rate) and with the 2028 top-up bought at 2028 prices.
- **D3/D9:** build the chart data for Q2 (equity share by year, promise vs surplus), Q1 (reserve roll-down), Q18
  (facility median and p5 against shortfall probability, 3-4 designs).
- **D1:** find a primary or official source for a market-implied U.S. default probability (for example a U.S. 5-year
  CDS level from a data vendor's static page or a central-bank publication). Check STRIPS liquidity (bid-ask) against
  on-the-run notes for the Q20 clause.
- **D4:** confirm the construction cost index trend (F-508) and whether DGBAS publishes a forecast. Compute the NT$
  purchasing power of a US$ floor in 2033 under trend CCI and ±1 standard-deviation FX moves (Q17).
- **D5:** a precedent for "floor promise, upside at the donor's discretion" wording (Q6), and whether staged gifts are
  common for founders of small residencies (Q8). Do not name organisations in deliverables (BS-15).
- **D7:** run the Q19 test (two or three AI tools, the public case text, record the architecture each proposes and log
  the use for Works Cited). Check whether any Wharton Global Youth teaching page covers liability matching; my API
  search found none.
- **D10:** confirm that a note naming a "role" word in WInS fits any character limit (G-ids; not published).

## What this teaches

A good contrarian doesn't try to knock the plan down. It asks where a careful reader could fairly mark the plan down.
Here the architecture held up under every attack: buying the promise with Treasuries beat each rival design we
priced. Three of our *reasons* did not hold up as well. "Anything less than a full lock fails" is false when the
second deposit arrives. "The $300,000 buys the promise" depended on September's interest rates. And "the reserve
doesn't change" answers the case's question only if we show how its maturities shorten each year. The lesson for
investing is that being right is not enough when someone else checks your work: the argument has to be right too.
The lesson about case writing is that the designers imagined a glide path (growth first, safety later), and a plan
that departs from their picture has to say why, in their own words, before the reader has to ask.
