> AI-generated research (Claude Code, ideation ladder, Thu 5 Nov 2026), not for submission. Keel is a simulated team, AI-written. Read the shortlist beside this file first.

# Ladder rung 3 (Opus): wide reading that changes a decision

AI-generated research (Claude Code, Opus 5.5), Thu 5 Nov 2026 (Sydney). Not for submission. Keel proposes, Caplet
decides. Plain English; the IPS suggestions follow the D35 style list (no slogan flips, no two-word kickers, no one-line
endings) and use no numbers, names or citations.

**Read first:** the client case in full; `keel/WHARTON_WORD.md`; FINAL `ips.txt` (493 words) and `pitch.txt`;
ERUDITION_PLAN sections 3 and 5; the R07 `COVERED.md` list; IDEA_BANK by grep only; the two earlier rungs
(`ladder_haiku.md`, `ladder_sonnet.md`) so as not to repeat them.

**How the facts were checked.** `fetch_text.py` could not reach any host this session (proxy 403 on CONNECT; the shell
also had no network), so I used WebSearch and then WebFetch on the result pages. Everything below marked VERIFIED was
read at that page on 5 Nov 2026. Anything not read there is marked UNVERIFIED.

**What a judge already sees in the plan.** The ladder, the owned floor, the small share sleeve, the lock before naming
and the zero-reinvestment set-aside are all covered, and the IDEA_BANK has about 176 ideas around them. So the gaps I
looked for were in the parts of the case that the plan treats most lightly: **who else pays for the residency and how
they behave**, and **what Laura's kept money is for**. Sonnet's rung found the same soft spot (W5: flexibility is
the weakest of the five case bullets; W9: the cushion sentence).

---

## Ranked summary

| # | Idea (no metaphor) | Field | Changes | In IDEA_BANK? |
|---|---|---|---|---|
| 1 | Her ten bought cheques are her strongest fundraising fact, stronger than the facility gift | Fundraising economics; grant-maker behaviour | The co-sponsor story, and a second reason to buy the cheques first | No (0 hits: overhead, Gneezy, starvation) |
| 2 | Never announce the kept money as the building's backstop, and cap any overrun help in advance | Mechanism design (soft budget constraint); charity economics (fundraising crowd-out) | One IPS sentence, plus a written cap | No (0 hits: soft budget, Kornai, crowd-out by effort). Related to #49, FRB-102 |
| 3 | Price the reserve at what Treasuries charge, because pricing it at hoped-for returns makes every extra share look like a saving | Public-pension finance | How the reserve's size is justified (the case asks for it) | Partly (Caplet's IDEAS 3 Nov #3, "optional, unverified"); abstracts now VERIFIED, incentive mechanism new |
| 4 | Co-sponsors react together to one public number, so any error in it moves them all at once | Coordination games, information economics | What the 2031 text may say (no upside talk) | Mechanism no (0 hits Morris, Angeletos); Haiku rung #49 has the focal point |
| 5 | The kept pocket backs two claims that peak in different years; building costs fell after 2008 and jumped in 2022 | Insurance ALM (natural hedging); construction cost cycles | Defends a thin flexibility number; names its one hole | Partly (L-04 did it with US CPI; building costs and the insurance name are new) |
| 6 | If a planned step is ever missed, the default must be the safe outcome | Reliability engineering | One rule for 2027 and 2031 | No (0 hits fail-safe) |
| 7 | The bottom should be a face value anyone can check on one line | Contract theory (costly state verification) | Floor held in notes, not a fund (Final Report) | No (0 hits Townsend); IBTM's "no predetermined amount" is #123 |

Ideas I looked at and dropped are at the end.

---

## 1. The ten bought cheques are her strongest fundraising fact

**One-line claim.** Funders prefer paying for a building to paying for its running costs, and donors give much more
when someone else has covered the costs they dislike. Laura has bought ten years of running money before the first
co-sponsor is asked. That, not the size of her facility gift, is what tells a co-sponsor the residency can last.

**Source.**
- Gneezy, Keenan and Gneezy, "Avoiding overhead aversion in charity", *Science* 346 (2014), 632-635. Field experiment:
  40,000 US mailings, 10,000 per treatment (control; $10,000 seed already given; $1:$1 match up to $10,000; a private
  donor has covered all overhead). Result: telling donors "that overhead costs are covered by an initial donation
  significantly increases the donation rate by 80% (or 94%) and total donations by 75% (or 89%) compared with the seed
  (or matching) approach." Mechanism: "the importance of perceived personal impact". VERIFIED: abstract at
  https://ui.adsabs.harvard.edu/abs/2014Sci...346..632G and design at
  https://Rady.ucsd.edu/_files/faculty-research/uri-gneezy/Science-2014-Gneezy-632-5.pdf (read 5 Nov 2026).
- Gregory and Howard, "The Nonprofit Starvation Cycle", *Stanford Social Innovation Review*, Fall 2009: "funders
  routinely require nonprofits to spend unhealthily small amounts on overhead"; "Donors don't want to pay for an
  organization's rent, or phone bill, or stamps." VERIFIED at
  https://compasspoint.org/sites/default/files/documents/SSIR_Underfunding_Overhead.pdf (read 5 Nov 2026).
- *Set in Stone* (University of Chicago Cultural Policy Center, 28 Jun 2012): new arts buildings "put enormous strain
  on institutions", some had to "reduce access ... and lay off staff", and success depended on generating income after
  completion. VERIFIED at https://news.uchicago.edu/story/careful-planning-and-focus-audience-crucial-success-new-cultural-facilities
  (read 5 Nov 2026). (The repo already uses this study for overruns.)

**Mechanism.** Donors and grant-makers want their money to land on something visible (a building, a programme), and
they avoid running costs. A lead donor who has already paid the part they avoid makes each new gift feel like it goes
straight to the visible goal. In the one field test that compared them head to head, covering overhead beat seed money,
which is the evidence the team leans on most (List and Lucking-Reiley, IDEA_BANK #6).

**Mapping to the case.**
- Line 88: "Laura will make ten annual payments of $50,000 toward the residency's operating expenses".
- Lines 85-86: "Any remaining facility cost, and any operating support beyond Laura's commitment, may come from
  co-sponsors, grants, collaborators, program fees".
- Lines 111-112: "A meaningful personal contribution may signal that the residency is financially viable".
- The case treats the facility gift as the signal. But "financially viable" for a new residency means it can keep
  running, and the running money is what funders least like to give and what Laura has already bought in 2027.
  Her operating commitment ($500,000 in total) is about three times her likely facility gift (MODEL, repo: range
  roughly $145k-$170k on older designs).

**What it changes.**
- The 2031 co-sponsor text should open with the bought operating reserve, then the facility range.
- It gives a second reason for the plan's order (cheques bought first in 2027, even at a cost to the gift): the
  cheques' certainty is itself fundraising capital, not just Laura's own promise.
- It answers the strongest rival (A09/L-14: a growth plan with a typical gift about $5k bigger). A slightly bigger
  building gift buys less fundraising power than certain running money does.

**Honest weakness.** In the experiment "overhead" meant the costs of that fundraising campaign, covered by a $10,000
donor, and the donors were US individuals answering a mailing. Laura's co-sponsors are likely institutions, and
"operating expenses" are wider than overhead. Some large foundations have moved towards general operating support since
2020 (UNVERIFIED), which weakens the starvation-cycle premise. And the $50,000 is fixed in dollars, so in real terms it
covers less each year (repo M4: the 2042 cheque buys about 60% of today's at 3.5% building inflation), so co-sponsors
may still be asked for operating support (line 85). The claim must be "the base running money is bought", not "running
costs are covered".

**IDEA_BANK check.** grep "overhead" 0, "Gneezy" 0, "starvation" 0, "running cost" in the bank's sense 0. FRB-102
("Don't let the building own her") is about Laura's own flexibility, not co-sponsors. NEW.

**IPS change (one sentence).** "Funders would rather pay for a building than for running it, so the strongest thing
Laura can tell co-sponsors is that ten years of running money is already bought." This could replace the closing
tablet line ("Like the tablet it is named after ..."), which is the packaging Ray objected to.

---

## 2. Never announce the kept money as the building's backstop

**One-line claim.** Money a project knows it can call on tends to get spent: managers plan to it and fundraisers ease
off. So the half of the shares Laura keeps is not promised to the building, and any help she might give with overruns
has a limit set before construction starts.

**Source.**
- The soft budget constraint (Kornai; Kornai, Maskin and Roland, "Understanding the Soft Budget Constraint", *Journal of
  Economic Literature* 41(4), 2003, 1095-1136). It "occurs if one or more supporting organizations ... are ready to
  cover all or part of the deficit"; it matters because "organizations can expect to be rescued from trouble, and those
  expectations in turn affect their behavior"; the main effect is "the attenuation of managerial effort". In the
  Dewatripont-Maskin model, the budget constraint "is soft ... if the center opts for refinancing". VERIFIED at
  https://eml.berkeley.edu/~groland/pubs/understanding.pdf and the abstract at
  https://econpapers.repec.org/RePEc:aea:jeclit:v:41:y:2003:i:4:p:1095-1136 (read 5 Nov 2026).
- Andreoni and Payne, "Is crowding out due entirely to fundraising?", *Journal of Public Economics* 95(5), 2011: in
  "a panel of more than 8000 charities", crowding out of private gifts by government grants is "about 75%" and "due
  primarily to reduced fundraising" (fundraising crowd-out is "70% to over 100% of all crowd-out"). VERIFIED at
  https://econpapers.repec.org/RePEc:eee:pubeco:v:95:y:2011:i:5:p:334-343 (read 5 Nov 2026).
- Project context: *Set in Stone*: "More than 80 percent of the projects studied ran over budget, some by as much as
  200 percent" (VERIFIED, UChicago page above). Escalation of commitment (Staw 1976) is the psychology often cited,
  but its lab result replicates poorly: one mixed and one failed replication (FORRT atlas,
  https://forrt.org/flora-replication-atlas/doi/10.1016/0030-5073(76)90005-2/, read 5 Nov 2026). So lean on the
  incentive argument, not on Staw.

**Mechanism.** A backstop changes the behaviour of the people it protects. If builders, the residency's managers and
co-sponsors know a founder's spare money will cover an overrun, budgets are set more loosely, fundraising effort falls,
and the overrun becomes likelier. A backstop that is private and capped keeps everyone else's budget hard. This is about
the project's incentives, not Laura's character, which matters given the owner's point that the plan must not read as
fixing Laura.

**Mapping to the case.**
- Lines 102-103: "She recognizes that committing all remaining assets could limit her financial flexibility as the
  project develops."
- Lines 85-86: remaining facility cost "may come from co-sponsors, grants, collaborators, program fees, continued
  business income": the case does not make Laura the residual payer.
- Line 145: "Preserves appropriate financial flexibility when determining the facility contribution."
- The FINAL IPS says the opposite: "The other half stays hers and liquid, as a cushion if the building costs more in
  Taiwan dollars." That sentence announces the backstop.

**What it changes.**
- The kept half stays Laura's flexibility and is never described to the residency or co-sponsors as overrun money.
- A written cap, set in 2031 with the range, on how much of the kept money the building could ever receive. The
  number is a Final Report item; LR-11's "keep a quarter back" is a natural starting point.
- It refines IDEA_BANK #49 ("Laura's half: a standby, called last"): keep the order of call, but don't publish the
  standby, and give it a ceiling. It also fits Sonnet's Move 2 (the top released only as co-sponsors match), which
  makes co-sponsors' money the condition for Laura's, the opposite of a soft budget.
- It reframes the thin flexibility number (the plan's weakest against rivals, ERUDITION_PLAN K): flexibility is
  measured not only by the dollars kept but by what Laura is never obliged to pay.

**Honest weakness.** Kornai's evidence is from state firms and banks, and Andreoni and Payne's is from government
grants, not a founder's gift. Many arts overruns come from poor demand and cost estimates, not slack (*Set in Stone*'s
own reading). A cap on her own money binds nobody legally, and co-sponsors may prefer a founder who will back
overruns. And the case leaves facility costs out of scope, so the cap cannot be sized in the IPS.

**IDEA_BANK check.** "soft budget" 0, "Kornai" 0, "moral hazard" 0, "Andreoni and Payne" 0. Related: #49 (standby
called last), FRB-102, S2 scout s5 (capped overrun facility, a project-finance view that keeps the standby public).
The incentive mechanism is NEW.

**IPS change.** Replace the cushion sentence with: "The other half stays hers and is never promised to the building,
because money a project knows it can call on tends to get spent, so any help with an overrun has a limit set before
building starts." (+19 words.)

---

## 3. Price the reserve at what Treasuries charge, never at hoped-for returns

**One-line claim.** If a fixed promise is priced at the return you hope your assets earn, every extra share makes the
promise look cheaper. That rule pushed American public pensions into more risk, and it is why we size Laura's reserve
at the Treasury price.

**Source.**
- Novy-Marx and Rauh, "Public Pension Promises: How Big Are They and What Are They Worth?", *Journal of Finance*
  (2011). Abstract: state pension liabilities "based on current salary and service is $3.20 trillion" if discounted
  like state general-obligation debt, and "Using zero-coupon Treasury yields ... promised liabilities are $4.43
  trillion." VERIFIED (abstract only) at
  https://www.kellogg.northwestern.edu/academics-research/research/detail/2011/public-pension-promises-how-big-are-they-and-what/?p=1
  (read 5 Nov 2026). The figure the states themselves reported is not in the abstract: UNVERIFIED, do not quote.
- Andonov, Bauer and Cremers, "Pension Fund Asset Allocation and Liability Discount Rates", *Review of Financial
  Studies* 30(8), 2017: "The unique regulation of U.S. public pension funds links their liability discount rate to the
  expected return on assets"; funds with that incentive take more risk and use higher discount rates, and the extra
  risk goes with weaker performance. VERIFIED (abstract) at
  https://ideas.repec.org/a/oup/rfinst/v30y2017i8p2555-2595..html (read 5 Nov 2026).

**Mechanism.** The price of a certain payment does not depend on what you hold against it. Discounting it at an expected
equity return lowers its "cost" exactly as fast as you add equities, so the accounting rewards the risk it should
charge for. Andonov, Bauer and Cremers show real funds responding to that reward.

**Mapping to the case.** Lines 94-96: Laura "will set aside a portion of the portfolio to fund the ten payments ...
Teams must recommend its size". Lines 90-91: payments funded "with a high degree of certainty". The team's own
three prices (Caplet IDEAS 3 Nov #3): about $500,000 added up, about $298,000 as Treasuries, about $239,000 at 7.5%
(MODEL, repo).

**What it changes.** Nothing in the holdings; it gives the reserve's size a principle a finance judge recognises, and
it explains why a rival plan that sizes the reserve from share returns will also tend to hold more shares: the method
pays it to. It also answers Caplet's 3 Nov caveat ("drop any public-pension framing unless read from the primary
source"): the abstracts are now read; the paper bodies are not.

**Honest weakness.** Partly covered already (Caplet's own idea #3). Pension discount rates are set by accounting
standards, not by a team's choice, so the parallel is about incentives, not identical mechanics. The IPS can carry no
names or numbers, so the sentence must stand without the evidence. A judge may find "public pensions got it wrong"
preachy: say it as a rule, not a sermon.

**IDEA_BANK check.** "Novy-Marx" 0 in the bank (1 mention in `caplet/IDEAS_2026-11-03.md`, unverified), "Andonov" 0.
PARTLY COVERED; the incentive mechanism and the verification are new.

**IPS change.** "We size the reserve at what Treasuries charge for the ten cheques, not at what shares might earn,
because pricing a fixed promise at a hoped-for return makes every extra share look like a saving." (35 words.) It
fits after "So, to us, high certainty means no payment depends on shares."

---

## 4. Co-sponsors react together to one public number

**One-line claim.** Most co-sponsors of a building give only if enough others do. When choices depend on each other,
everyone leans hard on the one number they all hear, so an error in Laura's number does not disappoint one funder: it
moves the whole group at once.

**Source.**
- Morris and Shin, "Social Value of Public Information", *American Economic Review* 92(5), 2002: agents who act on
  fundamentals and also want to coordinate overweight public information; "greater provision of public information
  always increases welfare" only when agents have no valuable private information, otherwise "the welfare effect of
  increased public disclosures is ambiguous." VERIFIED (abstract) at
  https://econpapers.repec.org/RePEc:aea:aecrev:v:92:y:2002:i:5:p:1521-1534 (read 5 Nov 2026).
- Angeletos and Pavan, "Efficient Use of Information and Social Value of Information", *Econometrica* 75(4), 2007:
  "complementarity heightens the sensitivity of equilibrium actions to public information, raising aggregate
  volatility". VERIFIED (abstract) at https://econpapers.repec.org/RePEc:ecm:emetrp:v:75:y:2007:i:4:p:1103-1142 (read
  5 Nov 2026). (Svensson's NBER paper, w11537, argues Morris-Shin is in fact pro-transparency: title seen in search, not
  read, UNVERIFIED.)

**Mechanism.** A building is a threshold project: it is built only if enough money arrives, so each co-sponsor's gift
is worth more when others give. That complementarity makes every co-sponsor weight the public signal more than its
accuracy alone would justify, and their errors become correlated. An overstated number then produces a coalition that
has committed on money that is not there; in a threshold project that is the difference between a building and a
half-funded one, so the cost of overstating is convex.

**Mapping to the case.** Lines 111-112: a contribution may "make potential co-sponsors more willing to contribute".
Lines 114-115: overpromising could "lose the confidence or participation of co-sponsors" (plural). Line 143:
"Communicates Laura's potential facility contribution to co-sponsors clearly and credibly."

**What it changes.**
- The fundraising text says nothing about upside ("more if markets are kind"): any soft extra would be read by all
  co-sponsors together and coordinate them on money Laura does not own. This sits well with idea 2: the kept half is
  never mentioned.
- In the team's newsvendor framing (#5, M6), the cost of overstating the top should be treated as larger than the cost
  of understating it, because a shortfall hits the whole coalition at a threshold. That is one more reason the top is
  locked before it is named.

**Honest weakness.** The plan already names only owned money, so this is mostly a reason for an existing design.
Fundraising is usually sequential (lead gifts first), which weakens the simultaneous-game picture; Vesterlund's
sequential giving is already covered. Understating also gets amplified (a small number seeds less), so the case for
erring low rests on the threshold, not on amplification alone. Haiku's rung #49 already has the "focal point" version.

**IDEA_BANK check.** "Morris" 0, "coordination" 0, "Angeletos" 0. #77 has "every co-sponsor hears the same number" as
a fairness point. Mechanism NEW; the focal-point idea is in Haiku's rung.

**IPS change.** "Co-sponsors decide partly on what the others do, so one wrong number from Laura would mislead them
all at once, and every figure she names is money she already owns." (30 words; could replace "because a number said
aloud can't quietly be halved after a bad year".)

---

## 5. One pocket, two claims that peak in different years

**One-line claim.** Laura's kept money has two jobs: covering the ladder's interest gap, which grows when rates fall in
a slump, and helping if building costs run high. US building costs fell for two years after 2008 and jumped in 2022, so
the two calls tend to arrive in different years. Insurers who write both life and annuity business get the same
offset and charge less for it.

**Source.**
- Turner Building Cost Index: "Unchanged From Second Quarter 2010 and 13.16% Below Its 2008 Peak", because "The economic
  environment has constrained demand" (PR Newswire, 30 Aug 2010). VERIFIED at
  https://prnewswire.com/news-releases/turner-building-cost-index-unchanged-from-second-quarter-2010-and-1316-below-its-2008-peak-101795798.html
  (read 5 Nov 2026). Turner's Q4 2022 sheet: average index up 8.0% in 2022 and 1.9% in 2021. VERIFIED at
  https://turnerconstruction.com/uploads/Q4-2022.pdf (read 5 Nov 2026). The share falls in 2008 and 2022 are standard
  history, not re-read here (UNVERIFIED this session). Taiwan's construction cost index in 2009: not found (two Taiwan
  government PDFs failed or did not hold it), UNVERIFIED.
- Cox and Lin, "Natural Hedging of Life and Annuity Mortality Risks", *North American Actuarial Journal* 11(3), 2007:
  insurers "who have more balanced business in life and annuity risks also tend to charge lower premiums" and
  "insurers who have a natural hedge have a competitive advantage." VERIFIED (abstract) at
  https://econpapers.repec.org/RePEc:taf:uaajxx:v:11:y:2007:i:3:p:1-15 (read 5 Nov 2026).

**Mechanism.** A reserve backing two claims that rarely fall due together needs less money than two separate reserves.
In a deflationary slump (2008-10) the interest gap grows but building costs fall; in a demand boom building costs rise
while shares are usually up. The one bad year for the pocket is an inflation burst (2022): building costs up and
shares down. In that year, though, rates rise and the ladder's interest gap shrinks, so no cheque needs the pocket.

**Mapping to the case.** Line 147: teams must identify "the effect of inflation on portfolio projections and facility
costs, and the financial flexibility Laura should preserve". Line 103: flexibility "as the project develops". IPS:
"The other half stays hers and liquid".

**What it changes.** It defends keeping the pocket small and single (about $26k by 2033, MODEL, ERUDITION_PLAN L)
rather than splitting it into a coupon reserve and a building reserve, and it names the one state where the pocket
fails the building. Final Report: rerun L-04 with a building-cost index instead of US CPI.

**Honest weakness.** Mostly covered: L-04 already found the two claims arrived together about half as often as chance
(1954-2011, US CPI), and the Courtroom kept it out of the IPS. Turner is a US index, three episodes are anecdotes, and the
pocket is tiny next to any building. With idea 2 in place the pocket is not promised to the building at all, so this is
about what Laura might choose, not what she owes.

**IDEA_BANK check.** "natural hedg" 0, "Cox" 0, "Turner" 0; L-04 and R05 #12 (wrong-way risk) cover the core.
PARTLY COVERED.

**IPS change.** None recommended (L-04's verdict stands: the claim needs evidence the IPS can't cite). Final Report
only.

---

## 6. If a planned step is missed, the default must be the safe outcome

**One-line claim.** In safety engineering a system is fail-safe when doing nothing leaves it in its safe state. The plan
has dated actions (the January 2027 build, the 2028 split, the 2031 lock); each should be written so that missing it can
only shrink a promise, never put one at risk.

**Source.** The fail-safe design principle is standard engineering practice; the classic examples (reactor control rods
held up by electromagnets that drop when power fails; a train's dead-man control) are UNVERIFIED this session, and the
IPS would not use them anyway.

**Mechanism.** Rules fail through omission more often than through bad judgement. If the default of every step is the
conservative state, an illness, a missed date or an adviser's mistake costs upside, not a cheque.

**Mapping to the case.** Lines 90-91 ("a high degree of certainty") and 114-115 ("promises more than she can ultimately
contribute"). L-15 already worries that the 2031 lock could be skipped after a boom.

**What it changes.** Two default rules. (a) If the ladder is not bought in January 2027, the money waits in Treasury
bills, never shares. (b) If the 2031 lock and pricing are not done before she names a range, she names only the
bottom.

**Honest weakness.** Small; it adds words to a full IPS, and the plan's dates are already fixed. It guards against an
event the case does not raise.

**IDEA_BANK check.** "fail-safe" 0, "default" in this sense 0. NEW, minor.

**IPS change.** "If a step is ever missed, the money waits in Treasury bills and she names only the bottom, so a step
nobody takes can only make her promise smaller." (27 words; Final Report if there is no room.)

---

## 7. The bottom should be a face value anyone can check

**One-line claim.** Fixed promises exist partly because they are cheap to check: you only look closely when one isn't
paid. A Treasury note's face value is the most checkable number in finance, while a fund's payout has to be estimated.

**Source.** Townsend, "Optimal contracts and competitive markets with costly state verification", *Journal of Economic
Theory* 21(2), 1979: "any realization of an endowment is known only by its owner unless a verification cost is borne";
the paper explains "seemingly simple as opposed to contingent forms of debt". VERIFIED (abstract) at
https://minneapolisfed.org/research/staff-reports/optimal-contracts-and-competitive-markets-with-costly-state-verification
(read 5 Nov 2026). The textbook result that standard debt is optimal (Gale and Hellwig 1985) is UNVERIFIED here. IBTM's
prospectus: "The Fund does not seek to return any predetermined amount at maturity" (IDEA_BANK #123, read by the team
1 Nov).

**Mechanism.** A co-sponsor can verify "face value $X of Treasury notes maturing 15 November 2032" from one statement
line with no model; "a fund's payout, rounded down" needs trust in an estimate.

**Mapping to the case.** Line 116: "a credible range"; line 143: "clearly and credibly". IPS: "The bottom is that fund's
payout, rounded down: money she already owns."

**What it changes.** For Laura's real 2028 purchase, hold the floor in notes maturing in late 2032 and quote their face
value as the bottom; the coupons are extra.

**Honest weakness.** The WInS book uses IBTM as the floor, and Wharton judges the three deliverables together, so the
IPS should not switch now. iBond holdings are public, so the checking cost is small in practice. Best as a Final Report
"what we would do with Laura's real money" line.

**IDEA_BANK check.** "Townsend" 0, "costly state" 0. NEW, minor.

**IPS change.** None now (consistency with WInS). Final Report only.

---

## Looked at and dropped

| Idea | Why dropped |
|---|---|
| Hong Kong currency board's backing band (release above a ceiling, top up below a floor) | Same rule as the escrow hand-back already adopted (row 19, LR-11) |
| Swiss National Bank's franc floor, abandoned Jan 2015 | Vivid, but adds nothing to "hold it, then say it" (L-15) |
| Load and resistance factor design (margin per load type) | Covered by R11 #4 (safety factors) |
| Moral-obligation municipal bonds rated below general obligations | Mirror image of escrowed-to-maturity munis, already covered (R11 #7) |
| Rogoff's "conservative central banker" | Reads as correcting Laura; the owner has said she needs no rehab |
| Custody concentration and SIPC limits | Operational, not strategy; tiny risk with segregated Treasuries |
| Certainty effect (Allais) | Covered (FUSIONS, S4) |
| Off-the-run cheapness, Dutch funding-ratio averaging, NY Regulation 126, Solvency II | All in R05 / S1 |
| Foundation payout lag (5% of prior-year assets) | Real, but its only use is the bust half of idea 5; legal sources (irs.gov, law.cornell.edu) were blocked |

## Fusions worth a paragraph in the Final Report

- **Ideas 1 + 2: what Laura pays for, and what she doesn't.** She pays in advance for the part funders avoid (running
  money) and refuses the part that would soften everyone else's budget (an open overrun backstop). Both make
  co-sponsors' money go further.
- **Ideas 2 + 4: say only what is owned, keep the rest unnamed.** One reason comes from the co-sponsors (they react
  together to a public number), the other from the project (a known backstop gets spent).
