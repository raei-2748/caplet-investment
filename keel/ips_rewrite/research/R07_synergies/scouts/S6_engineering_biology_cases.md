# S6 scout report: engineering reliability, biology and ecology, historic cases (R07 rung 2)

AI-generated research (Claude Code, scout S6, 27 Oct 2026). Not for submission. Keel recommends, Caplet decides.
Domains: [9] operations research and reliability engineering, [10] biology, ecology, evolution, [11] historic case
studies (Japanese insurers and Equitable Life skipped: another scout has them). No IPS prose below: ideas only.

**Source note.** The shared WebFetch budget ran out several times during this run (100 an hour across all agents), so
some checks are thinner than I wanted. Every quote below was read on the page named. Where I could not open a page I
say UNVERIFIED. Rung 1's attributions were mostly right, with one correction: it is **Dan** Cohen (not Daniel) in
the 1966 paper.

**Ranking, strongest first for this case:** (1) Studebaker, (2) Swiss cheese with common-cause failure, (3) the
pooled buffer, (4) Perry v. United States, (5) Cohen's bet-hedging, (6) Orange County, (7) FMEA. Demoted or dropped
(state defaults, Barings, k-out-of-n as such) are at the end with reasons.

---

## 1. Studebaker, 1963: a promise with no assets behind it, and the order in which claimants are paid

**Verified.** PBGC history page, https://www.pbgc.gov/about/pbgc-pensions-studebaker : in 1963 Studebaker "closed its
largest plant and terminated its pension plan". Outcomes, in PBGC's words: "about 3,600 older, retired workers
received their full benefits"; "roughly 4,000 active employees" with long service received "only about 15 percent of
the benefits they had expected"; "thousands of workers under age 40 lost their benefits entirely". Congress passed
ERISA in 1974, which created the PBGC. PBGC's insurance steps in "subject to legal limits" (so even the backstop is
capped).

**What it is.** A pension promise that the sponsor's future earnings were meant to pay. When the earnings stopped,
the assets that did exist were shared out by seniority, so the people nearest the date were paid in full and the
people furthest from it got nothing.

**Critique.**
- The PBGC page gives outcomes only. I did not verify the mechanism (how underfunded the plan was, why retirees ranked
  first). The claim "the plan leaned on the sponsor's future earnings" is my reading of the general history and is
  UNVERIFIED here. Do not state it as fact in a deliverable without a second source (the House testimony PDF of
  C. Millard, 24 Oct 2008, appeared in my search and may carry it; I did not open it).
- A pension plan has thousands of claimants and a sponsor that can fail. Laura is one person and ten payments. The
  analogy is about structure, not scale.
- Some professionals would call this a cheap scare story: ERISA fixed it, and Laura is not a pension plan.

**Fit to Laura: fits, in two precise ways, and a third that looks like a fit and is not.**
1. *Fully funded at birth, or not at all.* Studebaker's promise waited on money not yet earned. Laura's second
   deposit ($150k at the start of 2028) is exactly money not yet earned, from "publishing advances, speaking
   engagements, licensing, and other entrepreneurial ventures" (the case). The plan's design answer is that the ten
   payments are bought out of the first $300k, and the 2028 deposit is only a top-up for a gap and the source of the
   floor and stocks. So no payment waits on income that has not arrived. That is the Studebaker test and it is worth
   saying out loud: it is the one thing the 1963 plan did not pass. Caveat for Jun: the "gap" is not zero. The
   repo's number sheet has the ladder costing about $294k with headroom of a few thousand dollars, and the coupon
   reinvestment shortfall (about $21k if yields fall 2 points for good) is a funding hole that is closed only by the
   2033 re-match or the 2028 deposit. "Fully funded at birth" is true of the dated payments, not of every coupon.
   Jun would need to confirm how strong that sentence can be.
2. *Shortfalls land on the last claimants.* Whoever sits at the end of the queue absorbs the shortage: the under-40s
   in 1963, the 2041 and 2042 payments here, if the ladder is ever built short. The plan's rule (buy the longest
   rungs first, let the 2028 deposit fill any gap) decides who is hurt before the shortfall exists. Studebaker's
   lesson is to decide the order in advance, by design, not by default.
3. *The PBGC as a model for Laura's backstop: seems relevant, is not.* Laura has no insurer. Her insurance is
   self-insurance: the 2028 deposit and a held-back sum. And even the PBGC pays only "subject to legal limits", so
   "insured" never meant "certain". Do not present a backstop as if it were an extra layer of certainty.

**Fusion hook.** Studebaker + the pooled buffer (idea 3): a pooled hold-back is the PBGC you build yourself, paid for
up front and with the claim order set in advance.

**Logic device.** The three-age outcome as a thought experiment: "if the pot is short, who is paid?" Then the
reversal: Laura chooses the answer before the pot exists. Memorable because it has a human count in it (3,600 paid,
4,000 shorted, thousands zeroed) and a date.

**Lands in:** IPS as one clause-sized idea: *the promise is funded at the start, and no payment waits on money not
yet earned* (it directly answers "funding reliability" in Book 7's list and the case's "no outside funding").
Final Report for the full case study (Creativity and Presentation; Client Knowledge, because the 2028 deposit is the
case's most fragile fact). Check the mechanism with a second source before the Final Report uses it.

---

## 2. Swiss cheese, common-cause failure and the single-failure rule: do Laura's defences share a hole?

**Verified.**
- J. Reason, "Human error: models and management", BMJ 2000;320:768-770 (PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/).
  Layers of defence are "more like slices of Swiss cheese, having many holes". The holes come from "active failures
  and latent conditions" and are "continually opening, shutting, and shifting their location". Harm needs the holes
  to line up in "a trajectory of accident opportunity".
- US NRC common-cause failure document, https://www.nrc.gov/docs/ML0823/ML082350989.pdf : "For highly redundant
  systems, CCFs can be a major cause of system failure."
- Fukushima Daiichi (Wikipedia, https://en.wikipedia.org/wiki/Fukushima_nuclear_accident): the tsunami damaged "10 of
  the plant's 13 cooling systems for the emergency diesel generators"; ten water-cooled generators were "placed in
  the basements about 7-8 m below the ground level". Many backups, one location, one flood. (The one air-cooled
  generator "was unaffected by the flooding and continued to operate": diversity worked where numbers did not.)
- 10 CFR Part 50 Appendix A (US nuclear General Design Criteria), https://www.law.cornell.edu/cfr/text/10/appendix-A_to_part_50 :
  "Multiple failures resulting from a single occurrence are considered to be a single failure." And Criterion 22:
  "Design techniques, such as functional diversity or diversity in component design and principles of operation,
  ... shall be used to the extent practical to prevent loss of the protection function." This is the engineering
  rule in full: count failures by *cause*, not by component, and buy diversity, not copies.

**What it is.** A set of safeguards protects you only if their failures have different causes. Two backups that
fail for the same reason are one backup. Reliability engineers call that a common-cause failure, and they design
against it with diversity (different technology, location, supplier), not with more copies.

**Critique.**
- Reason's model is a metaphor, not a calculation. It tells you what to look for, not a probability.
- Redundancy arithmetic (k-out-of-n) assumes independent failures. Once failures share a cause the arithmetic is
  wrong in the dangerous direction: the NRC line above is the engineering admission of that.
- The metaphor can be stretched to anything. It earns a place only if it finds a specific shared cause.

**Fit to Laura: fits, and it exposes a real question the plan has not answered out loud.**
The layers between Laura and a missed payment are (a) the matched ladder, (b) the 2028 deposit that fills a gap,
(c) the 2033 hold-back or re-match, (d) the stocks cushion above the floor. Ask what makes each one fail.
- The ladder's weak spot (the coupon reinvestment gap) widens when yields fall and stay low.
- The 2028 deposit rests on her publishing, speaking and licensing income, which a recession can cut.
- The stocks cushion falls in an equity bear market.
- Direction check (standard, but not a number I sourced): in a growth-scare recession, Treasury yields tend to fall
  and shares tend to fall, and discretionary income tends to fall. So the three holes may line up in one downturn.
  That is the Swiss cheese picture exactly. The mirror image (2022-style, yields up, shares down) opens a different
  pair of holes and closes the reinvestment one. Jun would need to model the joint path; I give no probability.
- Why this matters for the pitch: a "high degree of certainty" claim is a claim about independence. Counting layers
  proves nothing. Saying which hole each layer has, and which two could line up, is knowledge a mini-Laura would not
  ask for and a competition judge would.

**k-out-of-n: seems relevant, is not, and here is why.** A ladder of ten payments is a *10-out-of-10* system: every
payment is needed. Rungs do not back each other up (except the Lab's L-09 point, that later coupons can pay earlier
payments). The true redundancy is the single shared spare: engineers call one shared spare "N+1". (Standard
data-centre and plant vocabulary; I did not open a definition page, UNVERIFIED as a citation.) N+1 survives one
failure, not two at once, which is the same limit again: it works only if failures are not simultaneous.

**Fusion hook.** Swiss cheese + the pooled buffer (idea 3): size the single hold-back against the *shared* cause,
because that is the one risk pooling cannot dilute. Also + FMEA (idea 7): FMEA lists single holes, Swiss cheese asks
which pairs share a cause. Together: a failure table with a "shares a cause with" column.

**Logic device.** The Fukushima picture: the backup count was large, the location was one basement. "Three locks keyed
alike are one lock." A causal chain to follow to its end: recession, then falling yields, then a wider coupon gap, at
the same moment as a cut in her income and a drop in the cushion.

**Lands in:** Final Report (a one-page common-cause table: each layer, its driver, which layers share one; this is
Portfolio Analysis, "testing funding reliability across market outcomes"). IPS: one idea-sized clause that the
defences are chosen to fail for different reasons. Strongest if Jun's model gives one joint-scenario number.

---

## 3. Goldratt's pooled buffer: one visible hold-back versus a pad on every payment

**Verified.**
- PMI, "Critical chain buffer sizing", https://www.pmi.org/learning/library/critical-chain-project-management-theory-7118 :
  critical chain takes the safety out of each task and will "aggregate all of the safety at the end of the project".
  Also quotes a sizing rule built on "the square root of the sum of squares".
- Harvey Mudd course notes on critical chain, https://www.cs.hmc.edu/courses/2009/spring/cs121/CriticalChain.pdf :
  task estimates "contain excessive safety time"; "Work expands to fill the time available"; padding is lost because
  "The safety is wasted before we start"; "Buffers are pooled, and made explicit"; "the risk of the aggregated tasks
  is the square root of the sum of squares of the individual risks". Feeding and resource buffers protect the chain.
- Herroelen and Leus, "On the merits and pitfalls of critical chain scheduling" (abstract,
  https://www.iaorifors.com/paper/36977): "the 50% rule for buffer sizing may lead to a serious over-estimation of the
  required buffer protection."
- Not verified: the buffer "fever chart" (consumption plotted against progress, with action zones). It is standard in
  critical-chain practice but I did not open a page for it. UNVERIFIED.

**What it is.** Everyone pads their own task, the pad gets spent anyway (Parkinson's law, the student's last-night
rush), and the project still runs late. Goldratt's answer is to strip the pads and keep one pooled, visible buffer for
the whole job, then watch how fast it is used.

**Critique.**
- The saving from pooling is a statistics result: independent risks add as a square root, not in a straight line. Ten
  equal independent risks need a buffer of about 3.2 times one risk (square root of 10), not 10 times (my arithmetic).
  If the ten risks share one cause, they move together, the sizes add in a straight line, and pooling saves nothing.
  Laura's rungs share one dominant cause (the level of yields), so the square-root saving is mostly not available.
- The 50% rule is a rule of thumb and the literature says it can overshoot (quote above).
- Goldratt's buffer sits at the end of one project with one deadline. Laura has ten deadlines starting with the first
  in 2033. The honest analogy is the *feeding buffer*, one that protects a later step before it is reached.
- Critical chain is contested in project management; the Raz, Barnes and Dvir paper ("A critical look at critical
  chain project management") is a sceptical review, though the abstract I opened gave no specific criticism.

**Fit to Laura: partly fits, and the partial is the interesting part.**
- It fits as an argument for the plan's single hold-back: a pad on every rung is money tied to the wrong date. A
  cushion on the 2042 rung does nothing for a 2033 shortfall. A pooled hold-back can go wherever the gap lands. The
  gain is fungibility, not statistics.
- It does *not* fit the claim "pooling lets us hold less". Because the risks are common, the buffer has to be sized
  against the shared cause (idea 2), not shrunk by a square root. Saying so is the judgement point.
- Student syndrome and Parkinson's law are about people spending their padding. The one real behavioural risk for
  Laura is the same: a visible cushion looks spendable, which is the facility contribution's pull. A pooled buffer
  works only if it is walled off by rule (ties to "lock what you announce" and Kydland-Prescott, both covered).
- The part worth importing: buffer *consumption versus progress* as a test. Plot how much of the buffer has been used
  against how much of the horizon has elapsed. This gives a trigger for action that is neither a forecast nor a mood.
  (Fever-chart detail UNVERIFIED as noted.)

**Fusion hook.** Pooled buffer + Swiss cheese: *size it to the shared cause*. Pooled buffer + Studebaker: the
hold-back is the self-built PBGC with a claim order.

**Logic device.** A reductio: if every rung carried its own pad, the total pad would be about ten times one rung's
worry; with one pool and independent risks it would be about three times; with one shared cause it is back to about
ten. So the argument for pooling is not "less money" but "money that can move". (Arithmetic only; Jun to model.)

**Lands in:** IPS as an idea: one visible hold-back, not pads on every payment. Final Report for the sizing logic
(Portfolio Analysis), the correlation point, and the consumption-versus-time trigger. Bin: Goldratt's project
scheduling and the 50% rule itself.

---

## 4. Perry v. United States (1935) and the gold clause: what "only default risk" really leaves out

**Verified.**
- Perry v. United States, 294 U.S. 330 (1935), https://www.law.cornell.edu/supremecourt/text/294/330 : "the right to
  make binding obligations is a competence attaching to sovereignty"; Congress, having power to issue debt, "has not
  been vested with authority to alter or destroy those obligations". The Court held the 1933 joint resolution went
  beyond congressional power so far as it overrode the bond's gold clause. But the bondholder, who claimed
  $16,931.25 on a $10,000 Liberty bond, recovered nothing: damages are limited to actual loss and "Plaintiff has not
  shown, or attempted to show, that in relation to buying power he has sustained any loss whatever."
- Context: Wikipedia, Gold Clause Cases, https://en.wikipedia.org/wiki/Gold_Clause_Cases : the joint resolution
  (Pub. Res. 73-10) voided gold clauses within the United States.

**What it is.** The federal government, in the Depression, voided the gold-payment clauses in its own bonds as well
as private contracts. The Supreme Court said that was beyond Congress's power, then denied the bondholder any money
because he had suffered no loss in what a dollar buys. A right with no remedy.

**Critique.**
- It is one event, in an emergency, under a gold standard Laura's bonds do not have. Overusing it would sound like
  the hedging the BIBLE (rule 6) bans.
- The holding is narrow. It tells you nothing about inflation, which was not the problem in 1933-35 (prices had
  fallen).
- Read carefully it cuts both ways: it supports "Congress cannot rewrite a Treasury bond's terms" *and* "a court may
  still decline to compensate". I have not checked how later cases treated it.
- The 14th Amendment section 4 ("validity of the public debt") is often quoted with it. I did not open the text
  here, so UNVERIFIED in this report.

**Fit to Laura: it looks like a threat and is actually a support, plus one real limit.**
- The only Treasury term ever broken in modern times was a clause (payment in gold) that Laura's bonds do not
  contain. Her liability is "ten fixed nominal $50k payments"; the bond pays nominal dollars; so there is no clause
  to void. The match is dollar to dollar.
- That lets the plan make a firm statement with real law behind it: the highest court has already said Congress
  cannot alter a Treasury bond's terms. (Aligns with BIBLE rule 6: no hedging, one concise direct clause.)
- The limit that remains is the one the Court itself named: *buying power*. "Only default risk" is not the whole of
  the risk in a Treasury; the unprotected part is what a dollar buys. That risk belongs to the facility side, where
  Taiwan costs drift (R05 #20, covered), not to the ten matched payments, which are nominal by contract.
- A second federal case, the 1979 Treasury "technical default" on a small batch of delayed bill payments, is in my
  memory only. UNVERIFIED here and not used.

**Fusion hook.** Perry + R06 D6 (the false "only default risk" claim, covered): Perry supplies D6 with its case and
its direction of travel: the risk that survived was the one about buying power, and Laura's payments are defined in
dollars, so for the payments it is zero by contract. Perry + nominal versus real (R02 #17).

**Logic device.** A thought experiment: "which clause was broken in 1933, and does Laura's bond have it?" The answer
is a one-line reason the near-ironclad claim is *about the contract*, not about faith.

**Lands in:** Final Report (a short boxed case under "what near-ironclad rests on"; Client Knowledge and Portfolio
Analysis assumptions). IPS: no. It belongs in the Final Report's source-checked section where it can be cited.

---

## 5. Cohen's bet-hedging (1966): is the kept half of the stocks a bet-hedge?

**Verified.**
- Dan Cohen, "Optimizing reproduction in a randomly varying environment", Journal of Theoretical Biology 12(1):
  119-129, 1966, DOI 10.1016/0022-5193(66)90188-3 (record at
  https://cris.huji.ac.il/en/publications/optimizing-reproduction-in-a-randomly-varying-environment/). Opening line
  of the abstract: "A model is constructed of optimizing long-term growth rate in a randomly varying environment."
  An annual plant's seeds either germinate or stay dormant in the soil, and the paper finds the best germination
  fraction.
- Clauss and Venable, "Seed Germination in Desert Annuals: An Empirical Test of Adaptive Bet Hedging", American
  Naturalist 2000 (https://www.journals.uchicago.edu/doi/10.1086/303314): on *Plantago insularis*, populations from
  historically drier sites had lower mean germination fractions, which "is predicted by bet-hedging models". The
  abstract says the pattern is "consistent with" bet-hedging, not a proof.
- Starrfelt and Kokko, "Bet-hedging: a triple trade-off between means, variances and correlations", Biological
  Reviews 2012 (abstract at https://researchportalplus.anu.edu.au/): lower-variance strategies "can invade a
  population consisting of individuals that on average do better"; conservative and diversified bet-hedging are two
  ends of a continuum, set by the correlations in fitness among individuals.
- Wikipedia, bet hedging (biology): conservative = "individuals lower their expected fitness in exchange for a lower
  variance in fitness"; "long-term fitness is best measured using the geometric mean."

**What it is.** In a desert the rain is unpredictable. A plant that germinated every seed would beat its neighbours in
every wet year and die out in the first drought. So some seeds stay dormant: the lineage gives up some expected
growth for a much smaller chance of ruin. Compounding is the reason: long-run growth is a geometric mean, and one
zero wipes out many good years.

**Critique.**
- It is the biological twin of the Kelly criterion (R02 #34, covered), which maximises the same geometric growth. So
  the *principle* is not new to the folder. What is new is the taxonomy and the correlation point below.
- The objective is a lineage over many generations. Laura's gift is one draw over one five-year path, with a
  hard floor and a cap. For a single-shot decision the criterion is the newsvendor's asymmetric cost (R05 #13,
  covered), not geometric growth. That is Samuelson's "fallacy of large numbers" (R02 #30) in a lab coat.
- Empirical support is "consistent with", and the field itself still argues about how to define bet-hedging
  (Starrfelt-Kokko's continuum, in the source above).
- Seeds in a seed bank decay; dormancy has a running cost. The floor's analogue (a Treasury fund earning less than
  stocks) has the cost of lower expected return, and that is the right analogy, but the seed-bank decay has no
  direct counterpart.

**Fit to Laura: partly, and it settles the question asked.** Is Laura's kept half of the stocks a bet-hedge? No, the
reverse. In Cohen's picture the *floor* is the dormant seed (the part that survives any year) and the *stocks* are
the germinating seed (the bet). What the plan does is more careful than hedging: it keeps the part of the bet that
nobody has been promised. If a bad year hits those stocks, no promise breaks. That is the biology's real lesson:
put the risk where a bad year cannot end the lineage. Two further imports that are not just Kelly again:
- *Conservative versus diversified.* VT's ten thousand holdings are diversified bet-hedging (many seed types), which
  cuts firm-specific risk. It does nothing for the year in which the whole market falls, because that bad year hits
  every seed alike. Only dormancy (the floor) answers a correlated bad year. The correlation, not the number of
  holdings, decides which kind of hedge works. This is a clean way to say why the plan needs a floor *and* a world
  fund.
- *A rule, not a forecast.* The plant does not predict the rain. It uses a fixed fraction set by how bad a bad year
  can be (drier sites, lower germination). The plan's floor should be set by how bad a bad year can be for the
  promise, not by a view on returns.

**Fusion hook.** Cohen + the newsvendor (R05 #13): two ways to size the risky sleeve (growth-rate or cost of being
wrong); the plan chooses the second because Laura's game is single-shot. Also + lock-what-you-announce (Courtroom).

**Logic device.** The plant that germinates everything and the plant that keeps a seed bank, compared over ten
rainy years and then one drought. Flag: BIBLE rule 4 says nothing roots-themed, and a seed story sits close to
"Messy Roots" and the roots motif. Use only if the Final Report wants a short analogy and Ahaan approves; I would
not put it in the IPS.

**Lands in:** Final Report (the conservative-versus-diversified point is a genuine knowledge flex for Portfolio
Analysis and Creativity). IPS: at most one clause-sized idea, "the risk sits where a bad year breaks no promise",
which does not need the biology. Bin the seed imagery for the IPS.

---

## 6. Orange County, 1994: a paper loss becomes a real one only when something forces a sale

**Verified.** P. Jorion's case study, https://merage.uci.edu/~jorion/oc/case.html : the pool was "a $7.5 billion
portfolio belonging to county schools, cities, special districts and the county itself"; "The $7.5 billion of investor
equity was leveraged into a $20.5 billion portfolio" through reverse repurchase agreements, in which "Citron pledged
his securities as collateral and reinvested the cash in new securities"; the pool "had suffered a loss of $1.6
billion". The key sentences: at first the loss was a "paper" loss, then "the county declared bankruptcy and decided to
liquidate the portfolio, thereby realizing the paper loss", and "By liquidating the pool in December 1994, the county
locked in a loss of $1.6 billion." Jorion adds that "soon after the liquidation, interest rates went back down by
about 2.5 percent" and that the liquidation "entailed a huge opportunity loss, on the order of $1.4 billion", but only
"in hindsight". (Wikipedia's Robert Citron page gives different round numbers, $8 billion and about $2 billion, and
the 6 Dec 1994 Chapter 9 date; I use Jorion's. Jorion does not say collateral was seized, so I do not claim it.)

**What it is.** A public pool borrowed against its own bonds to buy more bonds, betting that rates would stay low.
The Fed raised rates in 1994, prices fell, and the leverage multiplied the damage. The county then went bankrupt and
sold the portfolio, turning a paper loss into a locked-in one, just before rates fell again.

**Critique.**
- Laura has no leverage, no margin and no counterparty, so most of the usual Orange County lessons do not apply. In a
  plan with no borrowing, a name-drop would look like padding.
- "Hold and it would have recovered" is hindsight, and Jorion says so himself. Without the leverage, holding to
  maturity would never have been in doubt. The lesson is not "hold through losses", it is "never owe anyone
  something that can force a sale".
- The mechanism (hold-to-maturity cannot be forced to sell) is already in R05 #9 (SVB) and #10.

**Fit to Laura: partly, through one precise mechanism, not the leverage.** What turned the loss real was a *date that
arrived before the bonds did*: a creditor or a bankruptcy forced a sale ahead of maturity. The plan's whole shape is
the reverse: every bond or iBond is bought to mature *before* the January payment it funds, and no one can call it.
So the sentence the case gives the plan is: a price fall on a bond held to its date is a number on a screen; it
becomes a loss only if a date forces a sale first, and the ladder is built so no date can. A second small import is
Citron's record: re-elected seven times on years of good returns (Wikipedia), which says nothing about the tail
of a rate bet. The plan sells no view on rates, so no record is needed.

**Fusion hook.** Orange County + the Swiss cheese (idea 2): its causal chain (a rate rise, then leverage, then a
creditor's clock, then forced sale) is a *common-cause* chain in which every layer failed for one reason: the rate
rise. + the pooled buffer: the one thing that could create a forced sale for Laura is a shortfall in the January
cash, so the hold-back is the clock-stopper.

**Logic device.** The "paper versus locked in" timeline: December 1994 liquidation, then rates 2.5 points lower soon
after. A concrete picture of why the order "payment date after maturity date" matters more than the price today.

**Lands in:** Final Report (Portfolio Analysis, one short case beside SVB, with Jorion cited). IPS: no. Mid-ranked:
a good memorable case only if paired with the mechanism, thin as a stand-alone.

---

## 7. FMEA (failure modes and effects analysis): the pre-mortem made into a table

**Verified.** Wikipedia, Failure mode and effects analysis, https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis :
procedures were described "in 1949 in US Armed Forces Military Procedures document MIL-P-1629"; the risk priority
number is "Severity ... x probability ... x detection"; the critique that the ratings are "ordinal scale numbers, and
multiplication is not defined for ordinal numbers", which can cause "rank reversals"; the AIAG-VDA 2019 handbook
replaced RPN with an Action Priority table; FMEA is a single-failure analysis ("Only one failure mode exists at a
time") and "is not able to discover complex failure modes involving multiple failures". The AIAG-VDA change is
confirmed by BioProcess Online, https://www.bioprocessonline.com/doc/is-it-time-to-say-goodbye-to-fmea-risk-priority-number-rpn-scores-0001 :
"The RPN has been replaced by an action priority (AP) table."

**What it is.** A worksheet that lists every way a thing can fail, how bad each failure is, how likely, and how
easily it would be noticed beforehand.

**Critique.** Multiplying three ordinal scores is the textbook error that the industry itself dropped. It cannot see
two failures together (the single-failure rule above). It also invites false precision from invented scores.

**Fit: partly, and the useful part is small.** The plan already has a pre-mortem and a risk register. FMEA adds two
things:
- *Severity first, not multiplied.* A missed payment ranks above everything, however unlikely. That is Roy's
  safety-first (R02 #21, covered), so it is not new.
- *Detection.* Rate each failure by how long before it lands that we would know. Loud failures (a bond price fall)
  are visible daily; silent ones (the coupon reinvestment gap, which only shows when it is too late to cure by
  waiting) are the dangerous ones. A column that asks "how many years of warning" is a real addition and no rival
  plan would think to include it.
- Add the unglamorous operational mode the 2025-26 team learned about (CLAUDE.md: trading outside the rules): an
  annual human step for ten years (reinvest, hold cash through the iBonds' December liquidations, pay on 1 January).
  A person missing a step is a failure mode no market model finds.

**Fusion hook.** FMEA + Swiss cheese: a failure table, with a column "shares a cause with".

**Lands in:** Final Report only (a short failure table with a warning-time column), under Portfolio Analysis. Not
the IPS. Weakest of the seven.

---

## Demoted or dropped, with reasons

- **US state bond defaults, 1841-42.** Verified (Wikipedia, https://en.wikipedia.org/wiki/U.S._state_defaults_in_the_1840s):
  Arkansas, Illinois, Indiana, Louisiana, Maryland, Michigan, Mississippi, Pennsylvania and Florida defaulted, after
  the Panic of 1837 and a "tightening of credit"; Mississippi and Florida "refused to pay their debts in full";
  Pennsylvania and Maryland "raised taxes and resumed payments fairly quickly"; most state debt was held outside the
  US, mainly in Europe. The page does *not* mention the federal government's refusal to assume the debts, so I
  cannot cite that; UNVERIFIED. Fit: municipal and state debt is not permitted in the competition, so the case
  explains a rule rather than a choice. The one extra point (states cannot print the currency they borrow in;
  the federal government can) is true but is borrowed from monetary theory and was not sourced here. Russia's 1998
  rouble default is a counter-example someone should check before leaning on it. Bin, or a single Final Report
  sentence on why the permitted list is itself a safety rule.
- **Barings, 1890.** I confirmed that sources exist (Bank of England blog, https://bankunderground.co.uk/2016/02/10/rescuing-a-sifi-halting-a-panic-the-barings-crisis-of-1890/;
  Wikipedia "Baring crisis") but could not open them under the fetch budget, so I quote nothing. From memory: a
  concentrated Argentine exposure and short-dated liabilities that could not be rolled; the problem was liquidity as
  much as solvency. If confirmed, the mirror is clean (Laura's liabilities are fixed, dated and cannot run), but it
  duplicates R05 #9 (SVB). UNVERIFIED, bin unless a later scout verifies it.
- **k-out-of-n redundancy as such.** Seems relevant, is not: the ten payments are 10-out-of-10. Folded into idea 2.
- **Others in my domains not pursued:** the portfolio effect in ecology (Doak et al. 1998; the sockeye studies),
  keystone species, the Red Queen. They restate diversification or periodic review, already covered, and none of
  them changes what the plan does. Weibull, Erlang B, Little's law, EOQ: tools in search of a problem here.

---

## Best synergy from my domain

Fuse ideas 1, 2 and 3: **"Fund it first, make the defences fail for different reasons, and hold one pooled reserve
sized to the cause they share."** Studebaker supplies the opening test (no payment waits on money not yet earned);
Swiss cheese and common-cause failure supply the audit (the 2028 deposit, the coupon gap and the stocks cushion may
all be hit by one recession, so say which layers share a cause); Goldratt supplies the shape of the reserve (one
visible hold-back, sized against the shared cause rather than shrunk by a statistician's square root). Cohen adds the
reason a floor and a world fund are both needed (diversification cuts the idiosyncratic year, dormancy answers the
correlated one). The result is an argument about *why the certainty is real*, which is stronger than a claim that it
is. Jun's model should test one thing: the joint path of yields, shares and the 2028 deposit in a recession.
