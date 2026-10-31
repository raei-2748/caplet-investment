# Thinking log (IPS rewrite, the slow road)

AI-generated (Claude Code). One entry per day, Mon 26 Oct to Thu 29 Oct (Sydney): what was read, what was thought,
what was kept and what was killed. No drafting until Fri 30 Oct. Drafts D1-D4 are sketches, not candidates.

## Mon 26 Oct, night: reset, and what the sketches taught us

**Why the reset.** Ray (26 Oct): "THINK. That's your job. I don't want you to be hasty." Four drafts in one evening
polished one idea (the home-made capital-protected note) instead of finding the best one. The bibles are equal:
voice, motif, the extraordinary, investing knowledge, plus the refinements (subtle motif, human writing, no hedging,
judges are judges, not mini-Lauras).

**What the sketches did teach (kept as evidence, not text):**
1. Mock judges scored D2 at 35/50 and 33/50. Both found the strategy clear, and neither found a moment that made them
   stop. So the plan was not missing clarity; it was missing an aha a judge would repeat to another judge.
2. The concepts in R02 (60 of them) are mostly the standard canon (cash-flow matching, immunisation, safety-first,
   signalling). Using them correctly makes us competent. It does not make us extraordinary. What would: a concept
   used where nobody else thinks to use it, or a connection between two fields that turns out to be exact, not loose.
3. Ray's TNA averages 27 words a sentence; our sketches averaged 13 with many fragments. Short and choppy is an AI
   tell too.

**Thinking tonight: candidate ahas to test (none adopted yet).**
- **A1. Certainty, defined by the bond market's own test.** When a city sets aside Treasuries that mature in time to
  pay a debt, the market treats the debt as already paid ("defeased"; such bonds are usually rated AAA). Laura's ten
  payments are defeased in 2027-28, years before 2033. That turns "a high degree of certainty" from our opinion into
  a standard someone else already uses. (R02 has defeasance as concept 11, but as a label, not as the definition of
  certainty.) Test: is "escrowed to maturity = AAA" true and current? Is the iBond part allowed in that claim?
- **A2. The bottom of the range needs no model.** The 2031 range quotes a confidence. But the floor is bought, so it
  needs no forecast at all; only the top depends on a model. So the confidence figure attaches to one end only, and a
  co-sponsor can check the bottom themselves. That's a sharper reading of the case's "credible range + confidence".
  Test: is it true once the coupon gap is drawn from Laura's half first?
- **A3. The freeze is a feature.** Wharton forbids changing the strategy after 6 Nov. Economists call a rule you
  can't break a commitment device (rules beat discretion when your future self will be tempted). Our plan already
  trades nothing from 2028 to 2033, so the freeze costs us nothing, while it binds teams whose plans rely on judgment
  calls later. Risk: too meta for the IPS? Maybe a Final Report line.
- **A4. Every product a bank would sell Laura, we build from parts.** The ladder is a ten-year annuity-certain; the
  floor + stocks is a capital-protected note; the iBond funds are target-date funds in bond form. We unbundle all
  three and skip three sets of fees and one bank's credit risk. Motif link: a compounding pharmacist mixes one
  patient's prescription from raw ingredients instead of selling a branded pill, and "compounding" is also the
  investor's word. Test: is the pun too cute for Ray's taste? Is "annuity-certain" accurate (yes if the ten payments
  are fixed and certain; check the term)?
- **A5. Extended release is an exact fit, not a loose one.** An extended-release tablet aims for zero-order release,
  the same amount per hour, which is what ten equal cheques are. Immediate release is a lump sum; dose dumping is
  selling early. Pharmacists also measure a tablet's "mean dissolution time", the average time a dose stays in the
  tablet, and that is the same formula as a bond's Macaulay duration without the discounting. If that holds, "XR"
  isn't decoration: the duration match is literally an extended-release profile. Test: verify mean dissolution time
  and zero-order release; check the maths.

**Open questions for the next days.** Which of A1-A5 survives a sceptic? Which is about investing rather than
wordplay (north star 4 over north star 2)? Is there an aha in the case itself we keep missing (Laura's statistics
degree; her books; the Taiwan-dollar cost of the residency; the 2031 timing)?

**Started tonight.** Three background workers: a fact-check of A1-A5 plus the old queue (Lehman notes, Bodie, the
7.5% basis, iBond liquidation) -> `research/R04_fact_checks.md`; the ladder's Sonnet rung (deeper on the pharmacology
seam and on A4) -> `ideation/rung2_sonnet.md`; an Opus wide-reading rung for niche investing concepts that R02 misses
and that fit this case -> `research/R05_wide_reading.md`.

**Decided elsewhere tonight (I40, Ray: "make your own call"):** D1a the floor is the last source for a coupon gap
(yes); D1b quote the 2031 bottom with a margin, no separate $10k buffer; no re-sizing trades for the dedicated ladder
(`../pm/DECISIONS.md`). So the dedicated ladder stays a Final Report idea unless the Courtroom finds a reason.

**Fact-check back (R04, `research/R04_fact_checks.md`; most web pages blocked, so many items are title-level only).**
- A1 defeasance survives in a smaller form. Escrowed debt takes the US government's rating, and that is no longer AAA
  (AA+/Aa1). An ETF almost certainly can't sit in a defeasance escrow, so only the T-bond rungs pass the strict test.
  Say "funded the way a defeasance is funded", never "defeased" and never "AAA".
- A5 holds exactly: Macaulay duration is mean dissolution time with discounting. Laura's ten payments: 10.5 years
  undiscounted vs 9.90 years discounted. "Zero-order" fits as the same amount each year (stepped, not continuous).
  So far this is the one cross-domain link that is exact, not loose.
- A4's pun is wounded. Compounded drugs are not FDA-approved, so "compounding pharmacist" cuts against a safety story.
  The unbundling idea (annuity-certain + protected note + target-date fund, built from parts) stands without the pun.
  Say "build", not "replicate", since the iBond payout and reinvested coupons make it approximate.
- The 7.5% the locked TNA attributes to JPMorgan is the EAFE figure. AC World is 7.00% compound / 8.28% arithmetic.
  The IPS must not repeat 7.5%. If a return is quoted at all, use about 7% and check for a 2027 edition first. **[Window 27 Oct: WRONG EDITION. J.P. Morgan's 2027 LTCMA (release 19 Oct 2026) gives global equities 7.5% (USD), up from 7.0%; the TNA's 7.5% is the world-stocks figure. See `../office/outbox/2026-10-27_window_7-5-and-three-checks.md`.]**
- iBond end-of-life confirmed from iShares: a fund terminates around 15 Dec and pays out net assets in cash, so IBTM's
  cash arrives before 1 Jan 2033.
- Seed money: raising seed from 10% to 67% of the goal gave "nearly a sixfold increase" in giving. That's lab
  evidence for the case's own claim, but no percentage can be claimed for Laura.

**Sonnet rung back (`ideation/rung2_sonnet.md`).** The best find is an investing argument that happens to be
pharmacology, not a pun:
- **Zero-order vs first-order release = fixed dollars vs fixed percent.** A first-order drug releases a fixed
  share of what's left; an endowment spending a fixed % of its balance is first-order and can never run dry, so it
  can hold stocks. Laura's ten cheques are zero-order: $50,000 whatever the balance. A fixed-dollar draw on a volatile
  pot is exactly what sequence risk punishes. So "why Treasuries for the payments?" has a one-line answer that also
  explains XR: the case asked for zero-order release, and only a matched ladder delivers it. This is now the lead
  candidate for the motif's investing job (with A2, the bottom of the range needs no model).
- Mean residence time = Macaulay duration (10.5 years undiscounted, ~10.1 at 5%). The second moment (spread 8.25
  years squared) is why a duration match is not a funding match: the textbook case for cash-flow matching over
  immunisation, in a pharmacist's units. For the Final Report.
- 80-125% bioequivalence: 0.8 x 1.25 = 1, the same arithmetic as "a 20% fall needs a 25% rise". Final Report aside.
- Downgraded: "do not crush" and dose dumping are partial (an early sale changes the amount, not just the timing).
  Killed: half-life, flip-flop kinetics, and the target-date-fund leg of A4 (those funds rebalance; ours never do). So
  unbundling counts 2 products (a deferred period-certain annuity, a principal-protected note), and the real edge is
  a Treasury guarantee instead of an issuer's or insurer's. "Compounding pharmacist" is out.
- The R: redemption stays first ("ten redemptions"; the Treasury redeems the bond so Laura can redeem her pledge).
  Runway is true (10 years of burn) but fails "ten ___s". "Receipts"/Rx (Latin recipe; XR reversed is Rx) are
  Final Report asides at most.

**Opus wide-reading rung back (`research/R05_wide_reading.md`, 20 concepts, 3 syntheses).** Three findings change my
thinking, not just my vocabulary:
1. **The "99 in 100" figure is close to a tautology, and our sketches leaned on it.** If the gift is capped at the
   top and the bottom is bought, "the gift lands inside the range" is nearly true by construction. Goodhart and
   interval scoring both say: report the number that could fail, which is the chance of reaching the top (~70-75%).
   Every sketch that said "99 in 100" was showing off a number that measures nothing. Real correction.
2. **The range is a newsvendor problem (rated 5).** A newsvendor orders stock knowing both costs: unsold papers
   and missed sales. The case names both costs of the range: too little "may" fail to signal viability; too much
   "could damage her credibility". So the top is a critical fractile. If the top is reached ~70-73% of the time
   (MODEL, R05's quick run), the plan implicitly says over-promising is about 2.3-2.7 times worse than
   under-promising. That turns "floor + half the stocks" from a taste into a stated trade-off, and it comes from the
   operations canon of Laura's own degree field. Possibly THE aha. Sceptic: the cost of lost credibility is lumpy,
   not linear. Answer: that's why the bottom is owned outright and only the top uses the ratio. Test in the Lab with
   our own model before believing the 2.3-2.7.
3. **Wrong-way risk in the buffers (S2).** The payments' one leak (coupon reinvestment) is worst when yields fall and
   stay down, which happens in a recession, when Laura's half of the stocks (the first buffer) is smallest. Our
   "draw from Laura's half first" ordering assumed the two are independent. They aren't. This needs a joint run
   (rates and stocks falling together) before D1b's margin is trusted. It may also revive R01's coupon matching.
Also kept: S3, "high certainty" as three tests that accounting, insurance rules and SVB all share (fixed cash flows
landing before each date; a wall so nothing else draws on them; no forced sale). The sketches never said the wall
part: recommend a separate account. Also: SVB 2023 as the foil (same bonds, but its depositors could run and Laura's
dates can't move), and Baumol's cost disease + the Taiwan dollar for the half Laura keeps.

**End of day 1: where my head is.** The strongest pieces so far are investing ideas, not images: zero-order release
(why fixed dollars need Treasuries), the newsvendor range (why the top sits where it does), the model-free bottom
and wrong-way buffers. XR earns its place only where it carries one of those. Tomorrow: the Lab runs the joint
scenario and the newsvendor ratio on our own model; the Courtroom tries the newsvendor and zero-order ideas;
Laura's Room checks whether co-sponsors would read a range the newsvendor way.

## Tue 27 Oct, early: corrections from The Window (PR #49) and the Noticeboard. The fresh draft must not use these
- **7.5% is right after all.** J.P. Morgan's 2027 edition (released 19 Oct 2026): "Global equities are projected to
  return 7.5% (USD), increasing from 7.0%." R04 matched 7.5% to EAFE in the 2026 edition, a coincidence of editions.
  The TNA line stands; the IPS may use about 7.5% (world stocks, 2027 edition) or no figure. My day-1 note above
  ("must not repeat 7.5%") is withdrawn.
- **The donor study cuts against rounding the bottom down.** Raising committed seed money from 10% to 67% of the goal
  gave a nearly sixfold rise in giving: size matters, so a lower quoted bottom has a real price. That is good news
  for the newsvendor idea (the under-promise cost is real, not imagined), and it means D1b's margin must be argued as
  a trade, not as free safety.
- **R05's M² ranking is backwards:** length drives the coupon leak, not coupon. The Nov-2041 rung leaks most.
- **Contac 600 launched in 1960** (the Spansule was 1952).
- **"Staying inside the range is guaranteed by design" is false at the bottom** (0.75% / 0.11% of MODEL paths fall
  below it). So my "99 in 100 is a tautology" is too strong: the top end is near-automatic (capped), the bottom isn't.
  The point stands in a corrected form: report the chance of reaching the top, plus the small chance of falling
  under the bottom, not "inside".
- A theory named wrongly somewhere in the research (The Window's PR #49 note): check every named concept against its
  source before the synthesis.

## Tue 27 Oct: the Lab tests the two day-1 ideas that are about money (WO-R5, `lab/R05_joint.py`)
Method: the unchanged 200,000-path model (`../library/ips_numbers_2026-10/ips_numbers.py`) on the 22 Oct curve, with
one change: each year's stock shock 2028-32 is correlated with that year's yield move (rho = 0, 0.3, 0.5; rho > 0
means yields and stocks fall together, a recession). Stocks at 7.5% (JPM 2027) and 6.5% (a sceptic's figure). MODEL.

| | p(top reached) | implied over/under-promise cost ratio | p(gift below quoted bottom) | p(coupon gap reaches the floor) | p(floor dented > $5k) |
|---|---|---|---|---|---|
| 7.5%, independent | 76.7% | 3.3 | 0.75% | 7.0% | 3.8% |
| 7.5%, rho 0.5 | 75.2% | 3.0 | 1.28% | 8.7% | 5.1% |
| 6.5%, rho 0.5 | 72.9% | 2.7 | 1.43% | 9.3% | 5.5% |

What it means:
1. **Wrong-way risk is real but small.** When the coupon gap is in its worst 5%, Laura's half of the stocks has a
   median of $13k at rho 0.5 against $17k with no correlation: the first buffer is thinnest exactly when it's needed.
   The chance of landing under the quoted bottom nearly doubles (0.75% -> 1.3-1.4%). Still small. But it kills one of
   my day-1 ideas in its strong form:
2. **A2 ("the bottom needs no model") is false as stated.** The bottom needs no STOCK model. It does carry rate risk,
   because in 7-9% of paths the coupon gap outruns Laura's half and eats into the floor (mean ~$7k when it does). The
   $145k quote (vs ~$150k bought) is the margin that absorbs most of it. True version: "the bottom depends on no
   share price; only on Treasuries paying what they owe and on coupon reinvestment, and we quote it below what we
   own to cover the second." Less elegant, and honest. R01's coupon matching would nearly restore the strong version
   (it halves the gap), which reopens the Courtroom's question: is the dedicated ladder an IPS principle (later
   coupons pay earlier cheques) rather than a re-sizing of the frozen book? The ten instruments don't change.
3. **The newsvendor reading holds up.** The top is reached about 73-77% of the time across all six runs, so the rule
   implicitly prices over-promising at roughly 3 times the cost of under-promising (2.7-3.3). Stable to correlation
   and to a 1pp lower return: a ratio we can state and defend, not a lucky number. And the donor-size evidence (The
   Window) supplies the other side: under-promising costs real gifts, so 3:1, not 10:1.

## Tue 27 Oct: re-reading the case slowly, for what everyone skips
1. **"explain how its composition should change, if at all"** (the reserve). Almost every team will answer with a
   glide path. Ours: not at all, because it changes itself. Each holding turns to cash in the December before its
   January and nobody touches anything. That is the honest XR line: an extended-release tablet needs nothing from
   the patient after it's swallowed. "If at all" is the case inviting exactly this answer, and it costs one sentence.
   Strong candidate for the IPS (it answers a required item AND carries the motif).
2. **Laura's degree is "Statistics & Information Decisions Management"** (Wharton, 2018). Wharton's Operations,
   Information and Decisions department teaches the newsvendor model as a core idea (to VERIFY: course name and
   that it is taught there; R05 cites the Cachon-Terwiesch textbook, Cachon at Wharton). So the newsvendor reading
   of the range isn't just clever; it is the tool her own degree field uses for exactly this choice (order too
   much and eat the waste, too little and lose the sale). A Wharton judge would recognise it at once. Must be shown,
   not name-dropped: "each end of the range is an order-size decision" in plain words.
3. **"The only person who needs to believe in something is yourself."** The case's pull quote, set against a
   brief whose whole 2031 problem is getting others to believe. The tension is lovely, but the quote is the
   case's, not verifiably Laura's (standing rule: no Laura quotes). Final Report at most, attributed to the case.
4. **"Any remaining facility cost ... may come from co-sponsors, grants, collaborators, program fees, continued
   business income."** Laura's own future income is one of the facility's sources. So the half she keeps after
   2033 isn't idle: with her income, it's the project's second cheque (R05: staged funding). This is the case's own
   reason for "flexibility", and it is stronger than "overruns or a change of plan".
5. **"Year 0 is 2026 ... spaced exactly one year apart."** The case fixes the dates to the day, so the ladder can
   match them to the day. A team that uses a rolling bond fund ignores the one gift the case gives.
6. **"Teams may reach different conclusions about ... funding confidence."** Licence to define certainty our way,
   not the textbook's. The three tests (fixed cash, a wall, no forced sale) are our definition.

Running list of the strongest material (not yet ranked; ranking is Thursday's job):
zero-order release; "composition changes itself"; the newsvendor range (with the donor-size evidence on the other
side, and the ~3:1 ratio); the three tests of certainty; unbundling (annuity + protected note, guaranteed by the
Treasury); human capital (her 2028 income and yields fall together, from day 1 of the sketches); Laura's half as the
project's second cheque.

## Tue 27 Oct, afternoon: the Courtroom rules (`inbox/2026-10-27_courtroom.md`), and I was wrong twice
- **I was wrong to drop "99 in 100".** The case asks, word for word, how confident we are the gift "will fall within
  that range". So both numbers go in: the inside figure, explained as high by design, and the chance of reaching the
  top as the number that can actually fail. Never "cannot miss".
- **I had the newsvendor backwards.** The ratio shouldn't be something the plan "implicitly" prices; it's a choice
  we state with a reason: lost trust can't be bought back, and the donor study shows a smaller gift has a real cost
  too. So we pick 3:1 and set the top to be reached three times in four. Our rule hits that because the top is
  reached whenever world stocks are no lower in 2033 than in 2031.
- **Dedicated ladder: killed for the IPS.** It contradicts four locked lines (the TNA's "dedicated instrument" line;
  the WInS notes for Nov-2039, Nov-2041 and IBTR), its $1,486 extra cost exceeds the $1,139 headroom, and all its gain
  comes from re-sizing the frozen book. Final Report only, as an alternative we priced and turned down. The quoted
  margin ($145k quoted against ~$150k owned) already covers the risk it treats.
- **The Courtroom's candidate spine (to weigh on Thursday):** every promise Laura makes is an order placed against
  an uncertain supply, set where its two costs balance. The ten payments get a fractile near 100% (only a matched
  ladder delivers zero-order release at her budget), the bottom of the range ~100% (owned), the top 3:1 (reached
  three times in four), and whatever she keeps is her flexibility. One decision rule, applied four times, from her
  own degree field's canon. That is a framework, which is exactly what the form asks the IPS to set out.
- Unbundling and the defeasance yardstick go to the Final Report (the FASB 76/125 story is a real aha there).

**History check on "three in four"** (US stocks only, Shiller total-return data in
`../../archive/rab/data/ws2_returns/shiller_monthly.csv`; every two-year window): no loss in 80% of windows since
1871, 83% since 1926, 89% since 1950. So the model's 73-77% is on the cautious side, and the US is history's
luckiest
market, so world history would sit lower; we have no world series on file. Safe claim: "about three in four"; never
"four in five".

**Still missing (Courtroom):** Ray's voice; "as needs change" (smaller or missing 2028 deposit, rates falling before
the build, stocks halving before 2031); the inflation and Taiwan-dollar assumption the case requires; liquidity
named; the reserve's composition over time (the case re-read's "it changes itself" answers this one).

**Rules check (PR #49, via the coordinator):** D4's "ten Treasuries, each redeemed" is wrong: five of the ten rungs
are iBond funds. That bears on the R. Redemption is still true underneath (every bond inside an iBond fund is
redeemed by the Treasury, and the fund then pays out its cash), but the IPS can't say "ten Treasuries". Options for
Thursday: "ten holdings, each redeemed in time for one January" (redemption of bonds and of fund shares), or let
redemption lean on its second sense, Laura redeeming her pledge, and say plainly "five Treasury bonds and five
Treasury funds". Ladder figure is still 22 Oct ($1,139 under $300k).

## Tue 27 Oct, afternoon: the Courtroom's "still missing" list, worked as thinking

**1. "As needs change": what actually happens (22 Oct curve, deterministic, `lab/D1_split.py` functions).**
| Before the Jan 2027 build, yields... | 2028 deposit | Payments left unfunded | Floor bought | Stock fund |
|---|---|---|---|---|
| don't move | $150k / $100k / $0 | 0 / 0 / 0 | $150k / $100k / 0 | $32.1k / $21.4k / 0 |
| fall 0.5pp | $150k / $75k / $0 | 0 / 0 / $14.1k | $136k / $61k / 0 | $26.5k / $11.9k / 0 |
| fall 1pp | $150k / $75k / $30k | 0 / 0 / $0.2k | $120k / $45k / 0 | $21.0k / $7.9k / 0 |
| fall 2pp | $150k / $75k | 0 / 0 | $85k / $10k | $11.4k / $1.3k |
What I take from it:
- **One rule covers every case: payments first, then the floor and the stocks shrink in proportion.** The stock
  fund is always ~21% of whatever is left (the floor's expected interest), so a smaller deposit scales the gift down
  in a straight line and changes nothing else. That's the "as needs change" answer in one sentence, and it's a rule,
  not a forecast.
- **The payments are only ever at risk in one corner: yields fall before the build AND the 2028 deposit is small.**
  That is Aha 3 (her income and yields fall together in a slump) made concrete: a 1pp fall needs ~$30k of the
  deposit; a 2pp fall needs ~$65k. A deposit as low as $75k still completes the ladder even after a 2pp fall. So the
  honest certainty statement: "the ten payments fail only if yields fall by more than about 2pp before January 2027
  and her 2028 deposit also halves". That is a far stronger, more specific claim than "high certainty", and it's
  true.
- **Stocks halve before 2031:** nothing is sold; the top comes down (bottom + half a smaller fund); the bottom
  doesn't move. Stocks halve after 2031: the gift slides toward the bottom, never under it (except the coupon-gap
  tail). The plan has no decision to make in either case, which is the point.

**2. Inflation and the Taiwan dollar (case :146-148 asks for both).** The payments are fixed in dollars (the case
says so), so inflation can't touch them. It touches what the gift BUYS: Taiwan building costs (+6.5% y/y on file;
~3.5%/yr since 2021), and an arts residency's running costs rise faster than prices generally (Baumol's cost disease:
a residency can't make a painter paint faster). The Taiwan dollar adds a second leak: dollars are converted into a
currency that has jumped sharply against the dollar before (R05 cites May 2025; to VERIFY). Where it belongs: one
clause, and it does a job. It's the case's own reason for the half Laura keeps: whatever inflation and the currency
take from the facility, her half is what pays it. That ties three required items (assumptions on inflation, on
flexibility, and the facility contribution) into one sentence.

**3. Liquidity.** The plan needs no liquidity before 2033 by design (nothing is sold), but it has it everywhere:
the iBond funds trade daily (the locked TNA: "a level of liquidity which no odd-lot bond offers"), and VT is one of
the most traded funds there is. So liquidity is where her flexibility lives: the half she keeps is in a fund she can
sell on any trading day. Name it once, in the flexibility sentence.

**4. Does the newsvendor framework fit the XR motif, or fight it?** I think they're the same idea seen from two
sides. Pharmacologists dose inside a therapeutic window: too little and the drug does nothing, too much and it does
harm. A newsvendor sets an order between two costs, waste and lost sales. The case gives the range exactly those two
costs: too little fails to "signal that the residency is financially viable"; too much and she "could damage her
credibility". So the 2031 range IS a therapeutic window, and the newsvendor tells us where to put its edges (bottom
owned, top reached three times in four). XR's other job, zero-order release, covers the payments. So one motif,
two jobs, each carrying a real investing idea:
  - **extended release** -> the ten payments: fixed dollars on fixed dates, so only matched maturities will do;
    the reserve changes itself; do not crush (nothing sold early);
  - **the window** -> the 2031 range: two costs, edges set by rule, 3:1.
Risk: "therapeutic window" was on rung 1's list, so another AI team could reach it. But they'd reach it as a label;
the newsvendor maths under it (and the ~3:1 we can defend) is what nobody else will have. Rung 3's rule stands:
no "dose", "toxic" or "patient" in the IPS. "Window" can carry it.

**Laura's Room (WO-R7, `inbox/2026-10-27_lauras-room.md`; the web was mostly blocked, so much of it is unverified).**
Nothing found breaks the reading "bottom = an unconditional commitment, top = a variable amount by rule". One useful
caution for the fundraising text (Final Report): don't write "only if stocks hold". Under US nonprofit accounting,
a stated condition can make a pledge "conditional"; a variable amount set by a rule is a different thing. Lead with
the bottom and give the top's rule in one clause. On the Wharton link: OID is a real Wharton department, but nothing
shows that the case's degree name ("Statistics & Information Decisions Management") sits in it, or that OIDD courses
teach the newsvendor. So no "her degree field's canon" claim anywhere until a student checks a syllabus. The
newsvendor idea stands on its own merits; it doesn't need the Wharton hook. (The sixfold seed-money figure was read
from the List and Lucking-Reiley abstract on 27 Sep, per R04.)

**End of day 2: where my head is.** A spine is emerging that I didn't have on Monday: one decision rule (set each
promise where its two costs balance) applied to the payments, the bottom and the top, with XR doing two real jobs
(release for the payments, window for the range). Plus a concrete certainty claim ("the payments fail only if
yields fall more than ~2pp before the build AND the 2028 deposit halves") and one "as needs change" rule (payments
first; floor and stocks shrink in proportion). Tomorrow (Wed): voice. Study Ray's rewritten TNA reflections and
essays again against this content: what would Ray actually say, where would he joke, which sentence would he refuse
to write? Also the R decision, the second meaning of XR, and a fresh look for anything the spine leaves out
(north star 4: concepts that are applied but not yet placed).

**Courtroom (PR #49, via the coordinator): don't print "$145k" as the floor.** On the model, the floor ends up
below $145k in 43.5% of futures, because the 2028 deposit tops up the ladder first (the ladder costs more than
$300k in ~47% of rate paths). That fits the day-2 table: the floor is whatever the 2028 deposit has left after
completing the payments. It's known exactly in January 2028, three years before Laura names the range. So the IPS
states the bottom as a rule, not a number: "what the 2028 deposit leaves after the payments, rounded down". The
2031 range is a number, but Laura names it in 2031, not us in 2026. This also tidies the newsvendor story: the
bottom's fractile is near 100% because by 2031 it is already bought and known.

**Archive (via the coordinator): a clash with the locked TNA.** Reflection 3 calls VT "the only investment not
standing between Laura and a payment deadline". But "cover a coupon gap from Laura's half first" means selling
stocks to meet a payment, which happens in about a third of model paths (some gap, mostly small). Proposed fix,
with no trades now: in January 2033, when the reserve is set aside, any projected gap plus a cushion for the
coupons still to be reinvested moves into T-bills alongside the ladder, before the gift is paid. My view: right, and
it's better than a patch. It makes January 2033 a single, scheduled re-matching (the case's own moment: "at the
beginning of 2033 ... set aside a portion of the portfolio"), after which no share is ever sold to meet a deadline.
VT then stands between Laura and the gift's size, never between her and a payment date, so the TNA line holds.
It also answers the case's "how its composition should change, if at all": once, on a known date, and then not at
all. For Thursday: check against R05's wrong-way result (the gap is biggest when stocks are low, so the 2033 move
is a forced-ish sale in bad years; it's small, ~$7k mean when it bites, and quoted under the floor's margin).

## Tue 27 Oct, evening: Ray's note (the account is shared by Ray and Ahaan)
Ray says the long "bible" messages are Ahaan's, and they were being stored, not digested. Prose is paused until a
new voice thread produces a voice guide. Ray also wants more initiative and original ideas from the Lab. Done:
`BIBLE_TRACE.md` breaks the five books into 41 single expectations, each with a test, where it stands now and what's
open (8 met, 14 partly, 9 open, 9 ways of working, 1 on track). Work pushed to the office: WO-R8 (the Genius Lab must bring 5
original, model-tested strategy ideas) and WO-R9 (the Courtroom audits the trace). The Wed plan drops the voice
study (now the voice thread's job) and keeps strategy: the R, the 2033 re-match, the north-star-4 placement.

## Tue 27 Oct, night: V25 sent to Ray; then "judges are shark tanks"
V25 (`drafts/D5a/`, an assessment draft) is the first draft written to the voice guide and the two-box form. Ray's
next note: it needs emotional appeal, because judges are sharks being pitched, not examiners. Reading V25 again with
that eye, it argues but never makes anyone care. Laura appears as a set of cheques, and the residency (the whole point)
gets one word. The Shark Tank beats (hook, stakes, why us, the number, the ask) are now section 7 of the voice guide.
For the synthesis: put the residency's people in the stakes (the case names "artists, writers, designers,
entrepreneurs, and educators" who "live, work, teach, and collaborate"); give Laura's word to co-sponsors a face
(a missed January breaks a promise she made in person in 2031); add one real "why us" (the STRIPS plan we built and
then killed when the rules changed on 6 Oct, to be confirmed by a student as told); end on the ask (what Laura can
say in 2031), not on "do not crush". Ahaan's Book 3 still holds: the emotion is for the judges, not a pitch to Laura.

## Tue 27 Oct, late: the Shark Tank panel on V25 (`reviews/V25_shark_tank.md`): 34/50, and the reasons are useful
Scores: Strategy 8, Client Knowledge 6, Portfolio Analysis 7, Articulation 5, Creativity 8. No better than D2-D4 in
total, but the losses are specific and fixable, which the earlier 35/33 weren't.
- **Kept:** the opener (the strongest the panel has seen), "debts paid with debts owed to her", the human-capital
  line ("income that shrinks in the same slump that makes bonds dearer"), and the inflation line as the one a judge
  repeats.
- **A real hole (accuracy, not style): the cap.** V25 never says the contribution stops at the top and the rest stays
  Laura's. Without it, a boom lands the contribution ABOVE the range, which fails the case's own "within that range".
  It has to be in the next draft.
- **"Before the purchase" is unclear** (rungs are bought in Jan 2027 and Jan 2028), and "exactly where it breaks"
  sits badly next to "the one soft spot". The certainty claim needs one honest frame: the payments break in one
  place, and the contribution has one soft spot.
- **The aha is hidden.** "Three times worse" and "three times in four" are the same idea (the newsvendor) but read as
  two facts. One clause has to join them: the top sits where the odds of reaching it match the cost ratio.
- **Weakest beat: why this team (Articulation 5).** Best real material: the team's own first plan was about 75%
  stocks and failed the funding test, so we started where the sceptic stands (evidence:
  `../library/council_2026-09-27/02_judge_panel.md`, `01_chair_memo.md`). Alternative: the STRIPS plan killed by the 6
  Oct email. One only, told as it happened (students confirm).
- **Voice housekeeping:** five kicker endings (the guide allows 3), about 15 numerals (ceiling 6), the XR decoder-ring
  sentence. End on the ask (what Laura can say in 2031), not on "Do not crush". Use the case's word "contribution",
  not "gift".
These go to Thursday's synthesis as must-fixes, together with the Shark Tank stakes clause.

**Book 7 weighting (coordinator):** "Focus on the strategy and decision-making framework ... rather than describing
individual investments or presenting detailed financial calculations." V25's ~15 numerals are a real cost, not just
style. Rule for the next draft: at most one or two numbers in the IPS (the cheques' $50,000 and one felt figure),
models prove the decision rules behind the scenes, and the creativity goes into the central idea and the rules.
Passed to the model-suite and rival-team threads.

## Wed 28 Oct, small hours: the Genius Lab's five ideas (WO-R8, `inbox/2026-10-28_genius-lab.md`, `lab/R08_*.py`)
All MODEL (22 Oct curve, 7.5% stocks, 200,000 paths). None needs a WInS trade; all fit the locked lines.
1. **Lock what you announce.** On 1 January 2031, the day Laura names the range, sell the promised half of VT into
   Treasuries maturing before 2033. The top is then reached ~93% of the time instead of ~77% (91% under stress), for
   an expected cost of about $1.6k out of ~$193k. This is the night's big one, and I think it is bigger than the Lab
   says. It turns the plan into one sentence: **every promise Laura makes is bought on the day she makes it.** The
   cheques in 2027, the floor in 2028, the top of the range in 2031. That is a decision-making framework (Book 7), it
   is "commit only money she already owns" (the 16 Oct North Star memo) grown up, and it is exactly what extended
   release means: each dose is coated and fixed the moment it's made. It also answers the case directly: the range
   "must protect" the payments and her credibility, and here nothing is promised that isn't already owned in
   Treasuries.
   Tension for Thursday: it partly replaces the newsvendor spine (3:1 by choice). With the lock, the trade-off moves
   to the size of the top (how much stock she pledges), not the odds of reaching it. Maybe the two combine: the
   newsvendor still sets how much she pledges; the lock makes the pledge real.
   Limit: raising the quoted bottom as well was killed (below it in 3-5% of paths).
2. **Definitions:** "three in four" must be the event "stocks no lower in 2033 than in 2031" (72.8%); the top is reached
   to the dollar 69.9% (76.7% is with a $1k tolerance). The share pledged (1/3, 1/2, 2/3) barely moves the odds; a
   haircut on the 2031 stock value does (10% haircut: ratio 3.3 -> 6.4 for $1.3k of median gift).
3. **The failure corner is ~10 weeks wide.** A 2pp fall before the build is ~0.23% of two-month windows in history
   (all 1980-82). The payments need at most ~$50k of the 2028 deposit in nearly all paths (unfunded: 2.9% at $25k,
   0.02% at $50k, none at $75k+). The IBTR note's "0.2pp" headroom is now ~0.04pp: don't repeat it as current.
4. **Coupons must buy more of their own bond.** Every number we've published quietly assumes it; parking coupons in
   a bill fund loses ~$7.6k even with no rate move. Half a sentence in the IPS: "coupons are reinvested in the bond
   that paid them".
5. **The 2033 re-match needs a cushion sized by the forecast's own error:** projected gap + $7,500 cuts later stock
   sales from 31% of paths to 0.15%, for ~$0.7k of mean gift. Cost: stock is sold in January 2033 in most paths, a
   planned sale on a known date, not a forced one at a deadline.
Not tested: Taiwan dollar and inflation (no series on file).

**Courtroom on the lock (`inbox/2026-10-28_courtroom.md`): ADOPT as the central idea, in true words.** "Every promise
is bought on the day she makes it" is false three ways (the floor is bought in 2028, not on naming day; the payments
lean on the 2028 top-up, coupons and iBond payouts; the top is a ceiling, not a promise). The true version: **"No
number Laura names rests on a share price: each is owned in Treasuries by the day she names it."** It must go in the
IPS or nowhere ("may not be revised"). No locked line breaks; two drafted lines die ("nothing is sold early" becomes
"no Treasury is sold before it pays", which keeps "do not crush"). Not market timing: a date triggers it, not a
price. The prosecution's best point: the lock doesn't change the case's confidence test (0.75% below the bottom
either way). It moves where she lands inside the range (top 93% vs 77%), and costs Laura ~$2.2k of what she keeps.
The newsvendor 3:1 drops from spine to test (the lock passes it, narrowly at base). Name it plainly
(liability-driven de-risking), never CPPI. The aha to state is the diagnosis: after 2031 the cap leaves the
contribution with every fall and Laura with every rise, and the lock fixes that. Condition: re-run the lock together
with the 2033 cushion (2.2-3.6% of paths below the bottom combined) and draw the cushion from leftover cash and
Laura's half first.
**WO-R9 audit applied to `BIBLE_TRACE.md`:** now seven books (G1-G10 for Wharton's two), B7 and E3 down to PART,
C2/C3 rewritten for the lock and the corrected failure map, four new pulls.

**WO-R10, the Courtroom's condition: lock + 2033 cushion (`lab/R10_lock_cushion.py`, MODEL, 22 Oct curve).** R08_2's E
already drew the cushion from cash and Laura's half first; it failed because when Laura's side ran dry the $7,500
came out of the gift, even below the bottom (97.8% inside). Three orders tried, all with the lock:

| Rule | Inside the range | Top reached | Payments >$1k short, 2033-42 | Worst shortfall |
|---|---|---|---|---|
| E: cushion from anyone, bottom included | 97.8% (96.4% stress) | 87% | 0.15% | $3.5k |
| F: cushion only from Laura's side | 99.25% (98.6%) | 93% | 6.7% (8.6%) | $8.8k |
| **G: cash, Laura's half, then the gift down to the bottom, never below** | **99.25% (98.6%)** | **87% (84%)** | **1.1% (1.8%)** | **$6.8k** |

G is the rule. It costs no confidence (same 99.25% as the lock alone) and buys most of the cushion's protection; the
remaining misses are a few thousand dollars over ten years of $50,000 cheques. The stress row is rho 0.5 and 6.5%
stocks. (B's "31% short" in the JSON is not a miss: without a set-aside the gap is drawn from Laura's stocks as it
appears, which the metric can't see.) What it gives the IPS is a rule, not a number, the Book 7 way: **"Every dollar
above the bottom serves the cheques first; the bottom itself serves only the gift."** Top-reached drops from 93% to
87%, so the Final Report says "about nine in ten" only for the lock alone and "more than four in five" with the
cushion. The condition is met; the lock goes into Thursday's synthesis as the central idea.

**Rival scan lands (coordinator, from "Out-think every rival team for semis", 28 Oct): the lock is the crowd's default.**
Nine of twelve fresh-AI rivals move stocks into Treasuries around the 2031 announcement; one even uses the Courtroom's
"a date triggers it, not a price" defence. So the lock can't be the aha. It stays as a rule (G8 says every future action
goes in the IPS) and the central idea moves upstream to what nobody else wrote:
- **The diagnosis:** after 2031 the cap leaves the contribution with every fall and Laura with every rise. Rivals lock
  out of caution; we lock because we found the asymmetry.
- **The order:** the floor is bought in 2028, three years before Laura names it. "No number Laura names rests on a share
  price" survives, but as a consequence, not the headline.
- **Protect** the lines blind judges ranked V25 first of 13 for (85/85/84 vs 72): human capital, sequence risk
  (fixed dollars vs fixed percent), the break point, and the two-cost range. Zero of 36 rivals have human capital or a
  two-cost range, so the newsvendor comes back as a named idea in the IPS (one clause), not only as the lock's test.
This reverses half of this morning's Courtroom ruling (newsvendor "retired as the spine"). It's Keel's call, logged:
evidence about the field beats a ruling made without it.

## Tue 27 Oct, late: Ahaan's message (now BIBLE Book 9) and what changes
What I take from it, in order of weight:
1. **The prize is looking intelligent and knowledgeable**, two ways: niche strategies FUSED and CRITIQUED into ours,
   and logic (thought experiments, causal chains to the end). Our best material already works this way (zero-order
   release = sequence risk; newsvendor + donor study = a two-cost range; human capital + the failure corner), but we
   have been presenting single concepts, not syntheses. The Library is now on a far-field synergy wave (WO-R11).
2. **Nothing good vanishes.** `IDEA_BANK.md` now holds 31 ideas with a destination (IPS / Final Report / both) and a
   critique, plus the dropped list with reasons. The synthesis is checked against it.
3. **Big picture over minutiae.** I have spent too much of the last day on decimals (0.2pp vs 0.04pp, "to the
   dollar" vs "within $1k"). Those were worth fixing once, but they're not the work. From here, accuracy fixes go in one
   line in the log and the time goes to strategy and argument.
4. **No timeline rule but Saturday.** I had read "near-final Sat 31" as "no prose until Fri 30". Ahaan says that was
   never a rule. So I'll draft when the thinking is ready, and expect to write a first synthesis-led draft once R11
   lands, rather than waiting for Friday.
5. **7.5%:** the models keep a world-stocks assumption (it's what they need), but no deliverable calls it VT's return,
   and the IPS has no return figure at all.
6. **Voice:** qualitative, not counted. Ahaan's essays set the tone; the witty Wall Street writers sit beside them.
   `fingerprint.py` is retired as a gate. AI detection only via real web detectors, briefly, if at all.
7. **AI-use logging stops**: Caplet will handle citations.

## Wed 28 Oct, early: the Library's synergy wave (R11) lands, and the central idea sharpens
Twenty-two concepts, seven fusions, four logic moves (`research/R11_synergies.md`; most new case figures are LISTED,
not read, so verify before the Final Report). Into `IDEA_BANK.md` as rows 32-44, each with my critique. What it does to
the spine:
- **The central idea becomes "make each promise safe on or before its birthday" (S1), opened by the diagnosis (#3).**
  It's the first idea that explains all three dates (2027 cheques, 2028 floor, 2031 top) with one principle, and it
  turns the lock (which 9 of 12 rivals share) into the consequence of a framework (which none have). A price trigger
  is a guess about markets; a birthday is a fact about the promise. The builder who buys the timber when the contract
  is signed is the picture.
- **"High certainty" becomes an inventory (S5):** the four ways fixed promises have failed, three shut by design, the
  fourth (coupons at falling rates) measured and re-matched in 2033. The IPS names the mechanisms, not the stories.
- **L1 is the best single sentence on offer:** for the cheques we don't diversify, on purpose, because a chain of ten
  is only as certain as its links are correlated. It's true and it will make a judge stop.
- **S3 + the newsvendor is the growth answer:** keep the seed, risk the harvest; and the harvest's top is set where its
  two costs balance (~3:1, the donor study on the other side).
My one correction to R11: L3's "one forecast in sixteen years" overclaims (coupon reinvestment is a second, smaller
forecast). "One market forecast that matters" is true.
Next: the synthesis (`01_SYNTHESIS.md`): central idea, the order of beats, which bank rows the IPS carries and which
go to the Final Report, then a draft.

## Wed 28 Oct, Day 3: V26 checked against the rivals-and-panel brief; V27
The Day 3 routine's list was mostly done overnight (WO-R8, R9, the 2033 re-match sizing in R10, the R decision, every
concept placed in the idea bank). Its "no prose" line is superseded by Book 9. What the day added:
- **A rule risk in V26:** the 2033 set-aside went "into Treasury bills", and the Week-2 email says direct T-bills are
  out. Now "the shortest Treasuries" (a short Treasury bond or Treasury ETF on WInS).
- **"VT" named** where Book 7 wants a framework: now "a world index fund".
- **Articulation:** V25 scored 5-7 for having no team story. The real one, on file since 27 Sep: our first plan was
  about three-quarters stocks and the model had it missing cheques. One sentence, flagged for a student to confirm.
- **The ending:** the panel said "Do not crush" answers none of Wharton's points. V27 keeps it, but ends on the stakes:
  ten Januaries for certain, a building built on money Laura already owns. That is the birthday rule said as an outcome.
- **The risk I'm watching:** V26/V27 dropped two of V25's winning lines (the break point in numbers; the protected note)
  to make room for the birthday rule and the four-failure inventory. A blind panel (V25, V27 and three rivals; three
  judges) is running to see whether that trade was right.

## Thu 29 Oct: fresh eyes on V28, the rooms' first round, V29
The rooms ran their first research round on V28 overnight (Library, Genius Lab, Laura's Room, Writing Room, Long Room,
Archive). The one finding that mattered: V28 broke its own headline. "Each promise is made safe no later than the day
it becomes one" sat beside a coupon gap that could "still trim the gift" after it was named, with the fix waiting until
2033. Cold readers put that line last. V29 settles the gap in 2031, before the range is spoken, and lets anything spare
money can't cover come off the quoted bottom, so the rule has no exception. The Archive then earned the best new line by
test, not argument: wipe out every share and no cheque is worse off, only the gift (600,000 MODEL paths). Both blind
head-to-head judges advanced V29. The four-failure inventory left the IPS for words; the Final Report gets it whole,
now with all four doors shut. Web AI detectors are blocked here; a student can run one in a minute.

## Fri 30 Oct: Book 10, five drafts, three panels, and a lesson about adding things
Caplet's Book 10 landed at 18:15. The honest summary of the day is in `BIBLE_AUDIT.md`: we had written the rules down
and mostly not applied them. So the rules became ten Commandments with a check a cold reader fills for every draft,
the judges were rebuilt so they could actually disagree, and every idea from every version went into `IDEA_LEDGER.md`.

What the panels taught, in order. V31 (fresh) lost to V25 with the analytic judges. V32 took V25's best ideas
(certainty defined by where it breaks, the cost of safety with a number) and came first with four of six. V33 fixed
what judges couldn't follow and told our first plan's failure as our own story. V34 then took the Bible audit's fifteen
fixes, and it got *worse*: denser, harder to read once, and without the range's confidence figure. V35 goes back to
V33's shape and adds only what earned its place. The lesson for the next four days is Book 10's own: cut whole ideas,
never add to a full page without taking one out.

The detector: GPTZero can't be reached (paid API; the free scan needs reCAPTCHA, which our network blocks). We built
open-source detectors and tested them properly, and they were worse than a coin, so they decide nothing
(`DETECTOR_LOG.md`).

**What Caplet would say (Commandment X):** "Did you run it through GPTZero?" (No, and here's exactly why, plus the
one-minute check.) "The pitch is still a slogan" (V34's plain pitch replaced it). "Where's diversification?" (one
borrower on purpose, stocks spread worldwide). "Why so many numbers?" (each now says it's our model's). "Is this
extraordinary yet?" Not yet: it's clear and honest, but the aha is still the protected-note floor, and V35 had to cut
its label for room. **The fix:** tomorrow's round tests whether one sharper idea (the capacity-vs-willingness turn, or
the one-borrower paradox) can carry the "aha" that the label used to.

## Fri 30 Oct, night: the Archive was right, and a rival from outside nearly won
Two things moved the draft tonight, and neither came from us. The Archive reran the break point on V33's own design and
found our "$85,000" belonged to an older plan; on this one it's about $125,000. And a brand-new rival, written by a
different model from nothing but the case and Wharton's word (a Singapore team running CPPI over a ladder), took first
place from three of six judges. What they liked about it is what we'd dropped: the assumptions on the page, a stated
confidence for the range, a rule for the growth money. So V38 put the 7.5% back, and checking that number against the
Model Suite showed our 60/40 line was wrong too: at 7.5% a balanced plan breaks a promise about one time in three, not
four. V39 then took the cold reader's and the voice editor's fixes. It ties V37a head to head and leads on mean rank;
we keep it because it's also the one that's true.

**What Caplet would say (Commandment X):** "Did the number you were proudest of turn out wrong?" (Twice, tonight; both
fixed, both sourced in D19's README.) "Why does a CPPI team beat you?" (It shows its working; V39 now shows ours.)
"You're timid with her money." (Two judges again. The answer is para 6, capacity not willingness, but J2 and J5 want the
price in dollars, and the honest price is large: M7 has a 60/40 leaving her ~$226k by 2042 against our ~$30k.) **The
fix:** Saturday's round puts that price beside the Lab's A09 run and decides, by test, whether the IPS should say it.

## Sat 31 Oct, morning: V40, and the price we haven't said
V40 changes two sentences, both because a judge said so: the $125,000 now says what it does ("still does", i.e. fills
the gap), and the 60/40's miss is clearly that portfolio's, not ours. The cold read checked every number on the
Archive's grid (all true) and caught three over-claims we'd stopped seeing: "buys all ten" (it's "or nearly"),
"everything she owns" (she has money outside the portfolio), and "In our model" sitting over a US default the model
doesn't model. Those go in the mid-day draft.

**What Caplet would say (Commandment X):** "You keep saying 'usually leaves her richer'. How much richer?" Almost
$200,000 by 2042, in our own model, and we haven't said it because it's uncomfortable. That's the wrong reason. The
mid-day round tests V41, which says it, against V41b, which doesn't, and lets six judges decide whether naming the
price makes the case stronger or weaker. "Is the 7.5% back in?" Yes, as the model's assumption for world stocks only,
logged in ASK_HUMANS with a one-line undo.

## Sat 31 Oct, afternoon: the voice-first round, and what it cost
Caplet said this morning that we are "chronically incapable of writing like a human" and that every Bible message is
being ignored. Both were true in one way: every round since Thursday optimised for clarity and the word count, and
each cut sanded off a little more voice. So this round started from voice: a brief from the essays' moves and the
finance writers, four drafts written for voice first, three blind readers. Draft A won on voice. Then I merged A with
B, C and D into V42, cut it from 693 words to 495, and it came back as "the squeezed sibling" of A, with riddles made
by deleting small words. Six judges put it third, behind V40, because the merge also lost the leak, the lock and the
97-in-100. The lesson is the one Book 10 already gave: cut whole ideas, never squeeze. V43 starts again from A and
puts back V40's substance by dropping seven whole ideas, each listed in the ledger.

**What Caplet would say (Commandment X):** "Why did your first voice draft lose to the plain one?" Because the
judges mark on Wharton's criteria and the voice drafts left out mechanism. Voice and substance are not a trade: the
fix was to stop squeezing, not to stop joking. "Is it human yet?" We can't say: GPTZero still can't be reached from
here, and our own agents are not detectors. The draft says "GPTZero: not yet checked".

## Sat 31 Oct, evening: V44 and V45
V44 did what the V43 Bible check asked and won the actuary, but the teacher, the skimmer and the professor all put V40
first for the same reason in different words: it tells the story of the plan we threw away. V45 put that sentence back
("our first plan was three-quarters stocks, until our own model sank it") and became first with two judges and never
worse than third (mean rank 2.33 against V40's 2.17). On voice it is second only to draft A, and V40 is last with
every voice reader who saw it. That is the first draft that is close to the plain one on Wharton's criteria and well
ahead of it on voice, so it is the one Caplet sees tonight, with its check, open misses and all.

**What Caplet would say (Commandment X):** "Six commandments fail. Why am I seeing it?" Because I promised a voice-first
draft and its checklist tonight, and an honest list of what's still wrong is more use to you than another unseen
round. One of the six (GPTZero) can't pass from here; the other five have exact fixes in section E of the check, and
they're Sunday's first job. "Is this the final?" No: the final is due to you at the end of Wed 4 Nov.

## Sun 1 Nov, morning: the rooms' paragraph wins
Last night the Courtroom and the Archive said the 60/40 is the wrong rival: nobody serious would run Laura's promise
on a 60/40. The serious rival keeps our ladder and gambles only the 2028 deposit. I wrote V46 with that rival in V45's
voice and paid for it with 97 in 100 and the priority line. The panel took V46 apart on exactly those two cuts, and
put the rooms' own version (LR3, which keeps both) first with five of six judges. The voice reader went the other
way: LR3 last, "a results table". So V47 is LR3, and the voice now has to be won back without losing an idea.

**What Caplet would say (Commandment X):** "You dropped the line that tells co-sponsors what gives way first, to fit
a joke?" Yes, and the judges caught it. The rule I take from it: a voice line can only replace words, never an idea.
