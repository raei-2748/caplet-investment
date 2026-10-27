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
  The IPS must not repeat 7.5%. If a return is quoted at all, use about 7% and check for a 2027 edition first.
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
