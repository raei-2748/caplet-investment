# R05 Wide reading: concepts R02 missed, applied to Laura's plan

AI-generated (Claude Code), wide-reading rung (Opus), 26 Oct 2026 (Sydney). Research, not for submission; cite AI use
in the Works Cited. Every dollar figure is a MODEL figure from older lab runs and must be re-run before use.

**How to read this.** 20 concepts, none of them in R02's 60 (three sharpen an R02 label into something exact: noted).
For each: (a) meaning, (b) application with a case line, (c) changes / sharpens / only describes, (d) one-clause IPS
wording (no citation) + Final Report source, (e) aha rating for a Wharton judge (5 = would repeat it to another judge).

**Source tags.** VERIFIED = author, title, venue (and year) shown on the search-result page or URL listed, searched
26 Oct 2026; volume/pages VERIFIED only when the URL encodes them (IDEAS/RePEc). UNVERIFIED = not confirmed in a
search; do not cite until checked. The curl fetch script is blocked by the proxy today (403 on CONNECT), so no page
bodies were read: quotes and fine details below are from the author's knowledge unless stated, and are flagged.

Short names as in R02: **ladder**, **floor** (IBTM top-up, ~$150k by Dec 2032), **VT sleeve**, **rule** (2031 range =
floor rounded down to floor + half VT; 2033 gift = floor + half VT, capped at the 2031 top).

**Correction to THINKING_LOG A1 found on the way.** "Escrowed bonds are usually rated AAA" is out of date. Escrowed /
pre-refunded municipal bonds are rated at the level of the US government's own rating: when S&P cut the US to AA+ in
2011 it cut the AAA ratings of munis linked to the US the same week (fa-mag.com, "S&P cuts AAA muni ratings linked to
US after federal downgrade"); Fitch once used an "AAApre" notation (Bond Buyer). No agency now rates the US AAA (S&P
AA+ 2011, Fitch AA+ 2023, Moody's Aa1 2025; R02 items 15-16). So A1 must say "the bond market treats such a debt as
already paid, rated as the US itself", not "AAA".

---

## Part 1. Twenty concepts

### Certainty: what other professions accept as "already paid"

**1. In-substance defeasance, and why accounting withdrew it** (sharpens R02 #11)
- (a) A borrower who puts risk-free bonds in an irrevocable trust to cover a debt may treat the debt as gone; US
  accounting allowed this even when the lender had not released the borrower (FASB Statement 76, 1983), then stopped
  allowing it (Statement 125, 1996): a debt is extinguished only when legally released, because the borrower could
  still be made to pay.
- (b) Laura's ten payments are defeased in Jan 2027-28, years before "At the beginning of 2033 ... Laura will set aside
  a portion of the portfolio". But her ladder is not in a trust: she could sell it. Accounting's own history says the
  bonds are necessary but not sufficient; certainty also needs a rule that no other need may draw on them.
- (c) **Sharpens**: the load-bearing clause in the IPS is not "we bought Treasuries" but "nothing else may ever be paid
  from them" (the D1 sketch has "Until 2033 each holding is kept whole to its date"; it should also say no other cost
  is ever met from them). Possible Final Report refinement: hold the ladder in a separate account.
- (d) IPS: "the payment bonds are walled off: no other need is ever met from them". Source: FASB (1983), Statement of
  Financial Accounting Standards No. 76, *Extinguishment of Debt* (in-substance defeasance survey record at
  libcat.library.tamu.edu "Illustrations of accounting for in substance defeasance of debt ... FASB statement no. 76",
  VERIFIED existence). FASB (1996) Statement No. 125 superseding it: UNVERIFIED in this run (from knowledge; check
  viewpoint.pwc.com NFP guide "Extinguishment", which appeared in the search).
- (e) **4.** Few teams know defeasance; none will know it was once allowed and then withdrawn, and why.

**2. Escrow sufficiency verification and SLGS (the Treasury's custom bonds for exactly this job)**
- (a) When a city defeases bonds, an independent verification agent (a CPA) recomputes that the escrow's cash flows
  meet every payment; the US Treasury even issues special non-marketable securities (State and Local Government
  Series, SLGS) with custom dates so escrows can match exactly.
- (b) Laura cannot buy SLGS (only state and local issuers can), and WInS lists only marketable Treasuries; that is why
  her rungs mature days to months before each 1 January instead of on it. "define what they consider a high degree of
  funding certainty, explain how they evaluated that level of certainty": the evaluation is a verification schedule,
  one line per payment: which holding, maturity date, expected cash, payment, surplus or gap.
- (c) **Changes the Final Report** (adds a one-table "verification schedule" as the evaluation method); in the IPS only
  a clause.
- (d) IPS: "we test certainty the way a defeasance escrow is verified: payment by payment, not on average". Source:
  31 C.F.R. Part 344 (SLGS) and Treasury Federal Register notices (govinfo FR 2005-06-30, 70 FR 37904, on
  treasurydirect.gov; VERIFIED existence); Baker Tilly, "Investment options for advance refunding escrow" (VERIFIED
  existence, bakertilly.com). Verification-agent practice: VERIFIED only as general practice from knowledge; cite a
  primary MSRB/GFOA page after checking (UNVERIFIED).
- (e) **3.**

**3. The Solvency II "matching adjustment" eligibility test**
- (a) EU/UK insurers matching annuities with bonds get capital relief only if the asset portfolio is ring-fenced, held
  to maturity, and its cash flows are fixed and cannot be changed by the issuer or third parties, and matched in
  currency to the liabilities.
- (b) This is a regulator's written definition of "matched", and Laura's book can be graded against it: the five
  T-bonds pass (fixed, non-callable, USD); the five iBond funds strictly fail "fixed cash flows" (TNA Note 2: "final
  payout is not fixed"; it is NAV). The test names the honest weak spot precisely: 2033-37 rest on funds that behave
  like bonds held to the end, not on fixed cash flows.
- (c) **Sharpens** the certainty definition and the IBTM caveat (vote D1b's margin on the bottom has a regulatory
  analogue: insurers must haircut assets whose cash flows are not fixed).
- (d) IPS: "where a bond's payout is fixed we rely on it; where a fund's payout floats, we count less than we expect".
  Source: Directive 2009/138/EC, Article 77b (EIOPA Solvency II Single Rulebook, eiopa.europa.eu, VERIFIED existence);
  Bank of England PRA (June 2014) letter, "Solvency II: matching adjustment asset eligibility" (bankofengland.co.uk,
  VERIFIED existence). Exact wording of the criteria: from knowledge, check the Article text before quoting.
- (e) **4.** Precise, unusual, and it turns a weakness into a stated haircut.

**4. "Low dependency" funding (UK defined-benefit pensions, 2024 code)**
- (a) UK pension trustees must plan to reach, by "significant maturity", a funding level where the scheme is invested
  in low-risk, cash-flow-matched assets and is not expected to need further money from the sponsoring employer.
- (b) Laura is the sponsor; her 2028 deposit is the "employer contribution" whose size depends on "publishing
  advances, speaking engagements, licensing". The plan reaches low dependency for the payments on the $300k alone
  (subject to the IBTR note's 0.2-point condition), i.e. a state UK schemes aim for over decades.
- (c) **Describes** (strong framing); it also names the one condition under which the plan is not low-dependency (if
  yields fell before the Jan 2027 build, the 2028 deposit tops up the ladder).
- (d) IPS: "the payments depend on no future contribution, not even Laura's own". Source: The Pensions Regulator,
  *General Code / DB Funding Code of Practice* (laid before Parliament 29 Aug 2024 **[Window 27 Oct: 29 JULY 2024 (TPR press release "New DB funding code laid in parliament", Mon 29 Jul 2024, read 27 Oct 2026); in force for valuations from 22 Sep 2024; the General Code is a separate code]**; Addleshaw Goddard briefing
  "DB funding code laid in Parliament", 29 Aug 2024, and Hymans Robertson "DB Funding Code Glossary", VERIFIED
  existence). In-force date and the exact "low dependency" definition: UNVERIFIED (check TPR's own page).
- (e) **3.**

**5. Asset adequacy testing on prescribed rate paths (New York Regulation 126, the "New York 7")**
- (a) US life insurers' appointed actuaries must show reserves stay adequate under a fixed set of interest-rate
  scenarios (seven deterministic paths: level, steady rises, steady falls, pops and drops), not only under a
  Monte Carlo average.
- (b) Laura's only leak is coupon reinvestment ("reinvested coupons fund the rest", Nov-2039 note). Instead of "~6-7%
  of paths", run the ladder through seven named paths and print the coupon gap on each; a judge can follow seven
  rows, and the worst row (steady fall) sizes the margin on the 2031 bottom.
- (c) **Changes** the evaluation method (deterministic stress table beside the Monte Carlo) and gives vote D1b a
  number.
- (d) IPS: "we test the payments against named rate paths, including a long fall, not only an average". Source:
  American Academy of Actuaries, Life Practice Note (actuary.org/pdf/practnotes/life4.pdf, VERIFIED existence as a
  search hit); SOA Valuation Actuary Symposium proceedings 1990 (soa.org, VERIFIED existence). Scenario definitions:
  from knowledge, check the Regulation text before quoting.
- (e) **3.**

**6. Coherent risk measures: certainty is a probability AND a severity**
- (a) A probability of failure (value-at-risk style) says nothing about how bad the failure is; expected shortfall
  (the average loss in the bad tail) does, and satisfies sensible axioms VaR breaks.
- (b) The case asks teams to "define what they consider a high degree of funding certainty". A two-part definition:
  the chance any payment is short, and how short it would be if so. For Laura's ladder the honest answer is "small
  chance, and the miss is a few thousand dollars of reinvested coupons, covered by her own half first" — which is far
  stronger than a growth plan with the same headline probability but a tail of tens of thousands.
- (c) **Sharpens** the definition of certainty (currently probability only).
- (d) IPS: "certainty means both how rarely a payment could fall short and how little it would miss by". Source:
  Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1999). Coherent measures of risk. *Mathematical Finance*, 9(3),
  203-228 (VERIFIED, ideas.repec.org/a/bla/mathfi/v9y1999i3p203-228.html).
- (e) **3.**

### The ladder's bonds: microstructure and banking

**7. Fong-Vasicek M-squared: the residual risk of an immunised portfolio has a size**
- (a) For a matched portfolio, the loss from a non-parallel rate move is bounded by a constant times M², the spread of
  the assets' cash-flow dates around the payment date; a zero-coupon bond on the date has M² = 0.
- (b) STRIPS are banned, so each rung has M² > 0, and the highest-coupon, longest bonds carry most (the Feb-2037 4.75%
  bond's coupons sit far from its payment date; the Nov-2041 3.125% bond less per dollar). **[Window 27 Oct: BACKWARDS. Length drives M², not coupon: per dollar at a flat 5% from Jan 2027, Feb-2037 ~20, May-2038 ~23, Nov-2039 ~28, Nov-2040 ~34, Nov-2041 ~35. The Nov-2041 rung leaks most. `../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`.]** This ranks which rungs leak
  and gives the coupon gap a structural measure instead of only a simulation.
- (c) **Sharpens** R02 aha 4 (dedication): the coupons that matter are the ones landing far from any payment; using
  them to pay the next payment directly (dedication) is precisely an M²-reducing move.
- (d) IPS: none needed beyond "coupons pay the next payment first". Source: Fong, H. G., & Vasicek, O. A. (1984). A
  risk minimizing strategy for portfolio immunization. *Journal of Finance*, 39(5), 1541-1546 (VERIFIED,
  ideas.repec.org/a/bla/jfinan/v39y1984i5p1541-46.html).
- (e) **3** (deep, but a judge must know immunisation to feel it).

**8. The off-the-run discount: Laura is the natural owner of bonds traders don't want**
- (a) Newly issued ("on-the-run") Treasuries trade at a premium for liquidity; older bonds with similar maturity yield a
  little more. Investors who never need to sell earn that spread for liquidity they never use.
- (b) Laura's 2038-42 rungs are old 30-year bonds (Feb-2037 4.75%, Nov-2041 3.125%, CUSIP 912810QT8 per repo files;
  first issued around 2007-2011: issue years from knowledge, check TreasuryDirect). A buy-and-hold liability matcher
  is exactly who should own them. It also sharpens the liquidity line: the plan's liquidity is the liquidity it never
  needs, so paying for it would be waste.
- (c) **Sharpens** security selection and the "liquidity" part of the form's growth/liquidity/reliability balance.
- (d) IPS: "we buy the older bonds traders pass over, because Laura never needs to sell and is paid a little for
  that". Source: Krishnamurthy, A. (2002). The bond/old-bond spread. *Journal of Financial Economics*, 66(2-3),
  463-506 (VERIFIED, ideas.repec.org/a/eee/jfinec/v66y2002i2-3p463-506.html).
- (e) **4.** Expert-level, true to the actual holdings, and nobody else will say it. Size of the spread for these
  specific bonds: not measured; do not quote a number.

**9. Silicon Valley Bank, 2023: hold-to-maturity is safe only when the liabilities cannot run**
- (a) SVB held long Treasuries and agency bonds "to maturity"; when rates rose and depositors withdrew, it had to sell
  at a loss and failed. The bonds did not default; the liabilities ran.
- (b) Laura holds the same kind of bonds for the opposite kind of liability: ten fixed dates that cannot be called
  early ("one at the beginning of each year from 2033 through 2042"). Price falls between now and then are irrelevant
  unless something forces a sale; the plan's ordering (any coupon gap from Laura's half first, floor last, never the
  ladder) removes the only forced-sale route.
- (c) **Sharpens** the risk paragraph: the risk to name is "a forced sale", and the plan shows why it cannot happen.
- (d) IPS: "a bond held for a date that cannot move has no price risk, only the risk of being forced to sell, which
  this plan rules out". Source: Board of Governors of the Federal Reserve System (28 Apr 2023), *Review of the Federal
  Reserve's Supervision and Regulation of Silicon Valley Bank* (Barr review) (VERIFIED, federalreserve.gov).
- (e) **4.** Judges know SVB; the inversion (same bonds, opposite liability) is clean.

**10. The March 2020 "dash for cash": Treasuries can be hard to sell, so never plan to sell them**
- (a) In March 2020 even the Treasury market seized up for days; dealers could not absorb sales and the Fed bought
  heavily.
- (b) The D1 sketch says "the funds sell any day". True in normal markets, not always at fair value in a panic. The
  plan does not need to sell; each payment is met by a maturity. So liquidity should be claimed as "something matures
  before every payment", not "we can sell".
- (c) **Sharpens** one IPS sentence (and removes an overclaim).
- (d) IPS: "each payment is met by a bond maturing, never by a sale". Source: Duffie, D. (2020). *Still the World's
  Safe Haven? Redesigning the U.S. Treasury Market After the COVID-19 Crisis*. Hutchins Center Working Paper 62,
  Brookings (VERIFIED, brookings.edu WP62_Duffie_v2.pdf).
- (e) **2.**

### The buffers: who absorbs losses, and when

**11. Tranching and the waterfall: the plan is a three-tranche structure**
- (a) Securitisations split one pool into senior, mezzanine and junior (equity) slices; losses hit the junior first.
- (b) The plan already has a waterfall if vote D1a passes: senior = the ten payments; mezzanine = the 2031 floor said
  aloud to co-sponsors; junior = Laura's retained half of VT and anything above the cap. "committing all remaining
  assets could limit her financial flexibility": the junior tranche is that flexibility, and it is also the first-loss
  piece that protects the public promise.
- (c) **Sharpens** D1a with a reason (seniority of the public promise over Laura's private upside) and gives one
  sentence for the "balance of flexibility and reliability".
- (d) IPS: "losses fall first on what Laura keeps, then on the gift, and never on the payments". Source: Coval, J.,
  Jurek, J., & Stafford, E. (2009). The economics of structured finance. *Journal of Economic Perspectives*, 23(1),
  3-25 (VERIFIED author/title/venue via hbs.edu and aeaweb.org issue 94; vol/pages from knowledge).
- (e) **3** alone; **5** in synthesis S2.

**12. Wrong-way risk (and the stock-bond correlation regime)**
- (a) In counterparty risk, wrong-way risk is when your protection is weakest exactly when you need it. Whether nominal
  bonds rise or fall when stocks crash depends on the regime: in deflationary recessions they hedge; in inflationary
  ones (e.g. 2022) they fall together.
- (b) The ladder's only leak (coupon gap) grows when yields fall and stay down: typically a recession. The first-loss
  buffer (Laura's half of VT) shrinks in the same recession. So the junior tranche is wrong-way to the senior's leak.
  In an inflation regime the opposite: yields up, gap shrinks, stocks may fall but are not needed.
- (c) **Changes** the margin logic for D1b: the bottom quote must survive "yields fall 2 points AND stocks halve"
  together, not each alone. Lab test proposed: R01 with joint scenario (rates -2pt for good + VT -50% by 2031),
  measure the draw on the floor. MODEL hint only (stale 15 Oct numbers): gap ~$21k undedicated vs Laura's half of
  a ~$32k VT sleeve (~$16k, ~$8k after a halving); if R01's dedication halves the gap (~$10k), the halves cover it.
- (d) IPS: "the margin under the floor is sized for falling rates and falling stocks at once". Source: Campbell, J. Y.,
  Sunderam, A., & Viceira, L. M. (2017). Inflation bets or deflation hedges? The changing risks of nominal bonds.
  *Critical Finance Review* 6(2) (VERIFIED as NBER w14701 and Harvard page; CFR volume/year from knowledge,
  UNVERIFIED). Wrong-way risk definition: Basel/CVA textbooks, e.g. Gregory, J., *The xVA Challenge* (Wiley)
  (UNVERIFIED edition).
- (e) **4.** It is a genuine flaw-finder, not decoration.

### The 2031 range: an inventory decision, a forecast, an expectation

**13. The newsvendor critical fractile** (operations research)
- (a) Order Q copies of a newspaper with uncertain demand D. If being short costs c_u per unit and being over costs
  c_o, the best Q is the quantile of D at c_u/(c_u + c_o). Asymmetric costs move you to a low or high quantile.
- (b) The case states both costs: under-announcing has a cost ("A meaningful personal contribution may signal that the
  residency is financially viable ... make potential co-sponsors more willing"), over-announcing has a cost ("could
  damage her credibility and lose the confidence or participation of co-sponsors"). So each end of the range is a
  newsvendor quantity. The bottom carries a very large over-cost (a broken minimum), so it sits near the 0th
  percentile: the owned floor. The top is softer (missing the top of a range is a disappointment, not a breach).
- (c) **Sharpens, with an exact number**: the rule's top (floor + ½VT at 2031) is reached only if world stocks do not
  fall over 2031-33: about 70-73% (MODEL: lognormal, 6-7% compound, 16.8-20% vol; 65% at 5%/18%). So the top sits at
  the ~27-30th percentile of the uncapped gift, which is the newsvendor answer when over-announcing is judged about
  2.3-2.7 times as costly as under-announcing (1.9 at the pessimistic inputs). The team can now state and defend the
  loss ratio its rule implies, rather than present the rule as arbitrary.
- (d) IPS: "the bottom is set as if breaking it were ruinous, the top as if missing it were costly but survivable".
  Sources: Arrow, K. J., Harris, T., & Marschak, J. (1951). Optimal inventory policy. *Econometrica*, 19(3), 250-272
  (VERIFIED title/journal/date July 1951, econometricsociety.org; pages from knowledge). Cachon, G., & Terwiesch, C.
  *Matching Supply with Demand: An Introduction to Operations Management* (McGraw-Hill; 5th ed. listed) (VERIFIED,
  mheducation.com); Cachon is Wharton faculty (VERIFIED, faculty.wharton.upenn.edu CV). Terwiesch's Wharton post:
  from knowledge.
- (e) **5.** A core Wharton operations model, applied exactly to the case's two sentences about costs, with a number.
  Do NOT claim Laura took this course; her degree name ("Statistics & Information Decisions Management") is the
  case's, and the link is only that the model is standard in that field.

**14. Interval scoring, calibration and Goodhart: the cap makes "inside the range" true by construction**
- (a) A forecast interval is scored on width plus a penalty for misses; a "99% interval" that is right because it is
  defined to be right carries no information. Goodhart: a measure that becomes a target stops measuring.
- (b) The rule caps the gift at the top and owns the bottom, so "~99% inside the range" (number sheet) is close to a
  tautology: the only ways out are the floor fund's NAV falling short or a coupon gap. A statistically trained client
  (her degree is in statistics) or judge will see it. The informative numbers are where inside: chance of reaching
  the top (~70-73% MODEL) and the size of any shortfall under the bottom.
- (c) **Changes** what confidence the Final Report states (two numbers, as R02 aha 5 suggested; this supplies the
  reason: the single "99%" is manufactured by the cap).
- (d) IPS: "we state the chance of reaching the top, because staying inside is guaranteed by design". Source:
  Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the
  American Statistical Association*, 102(477), 359-378 (VERIFIED title and DTIC technical-report version; JASA
  volume/pages from knowledge). Goodhart, C. A. E. (1975), "Problems of monetary management: the U.K. experience",
  Reserve Bank of Australia conference papers (UNVERIFIED in this run).
- (e) **5** for honesty points: it pre-empts the sharpest judge objection to the range.

**15. Expectations as reference points (Kőszegi-Rabin)**
- (a) People judge an outcome against what they expected; a result below the expected point is felt as a loss even if
  it is good in absolute terms.
- (b) Once Laura says "$145k-$170k", co-sponsors' expectation sits inside it, often near the top. A $150k gift then
  feels like a $20k loss although it is inside the range. Wording sets the reference point: "at least $X, and up to
  $Y if markets are kind" anchors on X; a bare range anchors in the middle.
- (c) **Changes the co-sponsor text** (lead with the minimum, present the top as conditional) and favours a narrower
  top (supports half, not all, of VT going into the range).
- (d) IPS: "Laura leads with the minimum she owns; the top is offered as an upside, not a target". Source: Kőszegi, B.,
  & Rabin, M. (2006). A model of reference-dependent preferences. *Quarterly Journal of Economics*, 121(4),
  1133-1165 (VERIFIED author/title/journal/issue via rabin.scholars.harvard.edu and QJE 121(4) listing; pages from
  knowledge).
- (e) **4.**

**16. Earnings guidance: Laura's range is corporate guidance, and firms walk it down to beatable**
- (a) Listed companies give earnings guidance, often as ranges; research finds managers steer expectations to levels
  they can beat, and firms pre-announce bad news early to protect credibility.
- (b) The 2031 statement is guidance in all but name, made two years ahead to people who will rely on it. Practice
  adds one thing the case does not mention: guidance is reaffirmed or updated. A 2032 note to co-sponsors
  ("on track / lower, here is why") under the same rule keeps credibility if stocks fall before 2033, instead of a
  surprise at the gift.
- (c) **Sharpens** the decision framework "as needs change": an annual reaffirmation, never raising the 2031 top
  (consistent with the cap), only confirming or lowering it.
- (d) IPS: "each year Laura reaffirms the range to co-sponsors; it can be confirmed or lowered, never raised". Sources:
  Richardson, S., Teoh, S. H., & Wysocki, P. (2004). The walk-down to beatable analyst forecasts: the role of equity
  issuance and insider trading incentives. *Contemporary Accounting Research*, 21(4), 885-924 (VERIFIED title via
  london.edu; volume/pages from knowledge). Skinner, D. J. (1994). Why firms voluntarily disclose bad news. *Journal
  of Accounting Research*, 32(1), 38-60 (title appears on Skinner's CV pages in search; vol/pages UNVERIFIED).
- (e) **3.** Note: "never raised" is a team decision, not a fact; put it on the ballot.

**17. Conditional vs unconditional promises to give (US nonprofit accounting, ASU 2018-08), and pledge law**
- (a) A US nonprofit books an unconditional promise to give as revenue when made; a promise with a "barrier" (a
  condition outside the donor's control) and a right of release is not booked until the barrier is met. Separately,
  US contract law lets courts enforce charitable pledges without proof the charity relied on them (Restatement (Second)
  of Contracts §90(2)).
- (b) The rule's split matches the accounting split exactly: the floor is the unconditional part (a residency's books,
  if kept under US standards, could show it as a receivable: a visible, costly signal); the stretch to the top is
  conditional on markets, a barrier, so it would not be booked. That is why the bottom is a commitment and the top is
  an expectation. Caveat: the residency is in Taiwan and the case puts "legal and regulatory requirements of
  establishing a residency in Taiwan" out of scope; use this as an analogy for credibility, not as legal advice.
- (c) **Sharpens** the co-sponsor wording (call the floor a commitment, the top an expected range) and warns against
  phrasing the top as a pledge.
- (d) IPS: "the minimum is a commitment; the rest depends on markets and is described, not pledged". Sources: FASB
  (2018), Accounting Standards Update No. 2018-08, *Not-for-Profit Entities (Topic 958): Clarifying the Scope and the
  Accounting Guidance for Contributions Received and Contributions Made* (VERIFIED existence, storage.fasb.org/
  ASU_2018-08.pdf; subtitle from knowledge). American Law Institute (1981), *Restatement (Second) of Contracts* §90(2)
  (VERIFIED existence, opencasebook.org resource "Restatement 2d §90"; Salsbury v. Northwestern Bell is the leading case).
- (e) **4.** Nobody will connect a nonprofit accounting standard to the shape of the range.

**18. Matching gifts: the 1:1 result (Karlan-List)**
- (a) In a 50,000-letter field experiment, offering a match raised revenue per letter (about 19%) and response
  (about 22%); larger match ratios (2:1, 3:1) raised no more than 1:1 (figures from knowledge, check the paper).
- (b) Laura's upside could be framed for co-sponsors as a match: "my minimum is committed; above it I will match
  co-sponsor money 1:1 up to the top". The evidence says 1:1 does the work, so she need not promise more. It also turns
  her market-dependent upside into a lever on others' giving, which is what "make potential co-sponsors more willing
  to contribute" asks for.
- (c) **Changes** the co-sponsor text option set (a match is one framing to vote on). It does not change the
  portfolio; the top is still capped by the rule (min of the market amount and the match).
- (d) IPS: none (co-sponsor text is Final Report). Source: Karlan, D., & List, J. A. (2007). Does price matter in
  charitable giving? Evidence from a large-scale natural field experiment. *American Economic Review*, 97(5),
  1774-1793 (VERIFIED title via isps.yale.edu and J-PAL summary; vol/pages from knowledge).
- (e) **3.** Risk: a match ties the gift to co-sponsors' behaviour, adding a second uncertainty; flag it.

### The facility and the residency's costs

**19. Staged commitment (venture capital) plus reference-class forecasting (megaprojects)**
- (a) VCs fund in stages so they can stop or double down as the venture reveals itself; megaproject research finds
  cost overruns are the norm, not bad luck, and recommends forecasting from the record of similar projects.
- (b) Laura is an entrepreneur ("willing to take thoughtful risks", "turning ideas into opportunities"), and the case
  says "committing all remaining assets could limit her financial flexibility as the project develops". The half of
  VT she keeps is not idle caution: it is the second-stage cheque, released if the build overruns or the project
  proves itself. Building projects overrun more often than they come in under, so the reserve's likely use is on the
  facility side, not on her lifestyle (living costs are outside the portfolio).
- (c) **Sharpens** the purpose of the retained half (from "buffer" to "second tranche for the project") without
  changing the numbers; may change Final Report wording on flexibility.
- (d) IPS: "what Laura keeps is the project's second cheque, for when a building costs more than planned". Sources:
  Gompers, P. A. (1995). Optimal investment, monitoring, and the staging of venture capital. *Journal of Finance*,
  50(5), 1461-1489 (title cited widely in search results; direct record not reached: UNVERIFIED vol/pages).
  Flyvbjerg, B., Holm, M. S., & Buhl, S. (2002). Underestimating costs in public works projects: error or lie?
  *Journal of the American Planning Association*, 68(3), 279-295 (VERIFIED title/journal via ppp.worldbank.org;
  vol/pages from knowledge). Do not quote overrun percentages without reading the paper.
- (e) **4.** Entrepreneur client, entrepreneur's tool.

**20. Baumol's cost disease, and the Taiwan-dollar shock of May 2025**
- (a) Baumol and Bowen showed that labour-heavy arts organisations face costs rising faster than general prices,
  because their productivity cannot rise like manufacturing's. Separately, the Taiwan dollar jumped more than 6% in
  two days in May 2025, the most since the 1980s, inflicting large FX losses on Taiwan's life insurers that hold US
  dollar bonds.
- (b) The residency is a labour-heavy arts organisation in Taiwan funded with fixed US dollars. Two forces cut what each
  $50k buys: arts-sector cost growth above CPI (Baumol) and any rise of the Taiwan dollar against the US dollar. The
  case asks teams to state "the effect of inflation on portfolio projections and facility costs". Honest answer: the
  fixed payments are safe in dollars, but their purchasing power in Taiwan is not, which is exactly why the facility
  gift is left partly in stocks (a world fund holds some Taiwan stocks), and why "outside funding" will be needed
  for operating costs the case already places "beyond Laura's commitment".
- (c) **Sharpens** the assumptions paragraph (two named reasons the facility's real cost rises), no portfolio change
  (the case fixes the payments in nominal USD; TIPS banned; FX hedges are derivatives, banned).
- (d) IPS: "the payments are fixed in US dollars; what they buy in Taiwan can shrink, and the facility gift, held
  partly in stocks, carries that risk". Sources: Baumol, W. J., & Bowen, W. G. (1966). *Performing Arts: The Economic
  Dilemma*. Twentieth Century Fund (VERIFIED title/authors via library catalogues and a music.org review).
  Bloomberg (5 May 2025), "Taiwan dollar surges another 4%, jumping most since 1988" (VERIFIED headline via
  bloomberg.com URL); Bloomberg Law, "Taiwan life insurer losses swell to $1.2 billion in May on FX" (VERIFIED
  headline). Two-day size ">6%" per Zerodha Daily Brief headline (secondary). VT's Taiwan weight: not checked.
- (e) **4.** Arts economics for an arts residency is the kind of fit judges remember.

**Rejected after checking (so nobody re-proposes them):** tontines (no mortality pooling in the case); prize-linked
savings (no saver behaviour to fix); Bühlmann actuarial credibility (a pun on "credible", little substance);
ergodicity economics (adds nothing to R02 #30 Samuelson); dollar-cost averaging (the ladder is a match, not a market
bet); municipal debt-service reserve funds (they cover one year; contrast only, folded into #2); superstar economics
(Rosen 1981, a nice description of Laura's skewed income, but R02 aha 3 already covers the 2028-deposit risk).

---

## Part 2. Three new aha syntheses

### S1. The range is a newsvendor order, and the plan's rule implies a loss ratio the team can defend
**Combines** #13 (newsvendor), #14 (interval calibration), #15 (reference points).
**Mechanism.** Each end of Laura's range is an order quantity under asymmetric costs that the case itself names
(signal value if she announces more, credibility loss if she cannot deliver). For the bottom, the over-cost is a broken
public minimum: the optimal quantile is near zero, which a bought floor delivers without any model. For the top, the
rule (floor + ½VT at 2031, capped) sits at the ~27-30th percentile of the uncapped 2033 amount (reached ~70-73% of the
time, MODEL), which is the newsvendor answer if over-announcing is ~2.3-2.7 times as costly as under-announcing. So the
team can write: "we treat disappointing co-sponsors as about two and a half times worse than understating; that, not
taste, is why the top includes half the stocks and not all". Including all of VT in the top would put the top near the
same percentile but double its spread; including none would make the top equal the floor and waste the signal.
The reference-point result (#15) then says how to word it, and #14 says what confidence to quote (chance of reaching
the top, not "99% inside").
**Why it matters.** It converts the only discretionary number in the plan (the "half") into a stated preference with
a known trade-off, which is what a decision framework is. It uses a Wharton operations staple on the case's own two
sentences.
**Sceptic's best objection.** "Newsvendor costs are linear and per unit; credibility loss is lumpy (one broken promise
ends a relationship) and the top of a range is not a promise." Answer: that is why the bottom and top get different
treatment: lumpy, near-infinite cost at the bottom (hence owned floor, ~0th percentile), mild linear cost at the top.
Second objection: the 70-73% depends on assumed returns. Answer: true, and the implied ratio moves only from ~1.9 to
~2.7 across reasonable inputs; the point is the order of magnitude and the asymmetry, not the decimal.

### S2. The plan's buffers are tranched, and the junior tranche is wrong-way to the senior's only leak
**Combines** #11 (waterfall), #12 (wrong-way risk), #7 (Fong-Vasicek M²).
**Mechanism.** If D1a passes, losses run: Laura's half of VT first, then the gift's floor, never the payments. The
payments' only leak is coupon reinvestment, which is measurable per rung (M²) and largest when yields fall and stay
low: a deflationary recession, the same state in which the junior tranche (stocks) is smallest. So the plan's first
line of defence is weakest exactly when it is called. Two consequences follow. (1) The leak should be cut at source
(dedicate coupons to the next payment, R02 aha 4; favour low-M² rungs) rather than buffered, because buffers in this
plan are pro-cyclical. (2) The 2031 bottom's margin (vote D1b) must be sized on the joint scenario (rates down for
good AND stocks down), and the lab should test it. In an inflationary regime (2022-style) the correlation flips and the
leak shrinks, so the joint scenario is the binding one.
**Why it matters.** It is a real, checkable flaw-finder that tightens the plan, not a metaphor; and it explains in one
line why "floor last" is a seniority choice, not an accounting convenience.
**Sceptic's best objection.** "By 2031 most of a lasting rate fall is already visible, so the range is quoted knowing
the gap; the joint tail after 2031 is small." Partly right: the 2031 quote can net out the gap to date. But coupons on
the 2038-42 rungs keep being reinvested until 2041 (Nov-2039 note: "reinvested coupons fund the rest"), so some of the
gap is only known after the gift. The answer is a modest, stated margin, not a big one; magnitudes must come from R01.

### S3. Three professions, one test of "already paid": matched cash flows, ring-fenced, never a forced seller
**Combines** #1 (in-substance defeasance withdrawn), #3 (Solvency II matching adjustment), #9 (SVB).
**Mechanism.** Accounting (FASB withdrew in-substance defeasance because the borrower could still be made to pay),
insurance regulation (the matching adjustment requires fixed cash flows, a ring-fenced portfolio and no sale) and
banking (SVB's bonds were fine; the forced sale killed it) converge on the same three-part test for "this liability is
as good as paid": (i) assets whose cash flows are fixed and land before each payment; (ii) a wall so no other need can
draw on them; (iii) no route by which the holder is ever forced to sell. Laura's plan passes (i) for the T-bonds and
only approximately for the iBond funds (NAV, not par), passes (iii) by its loss order, and passes (ii) only if the IPS
says so. That gives the team a definition of "high degree of certainty" that is not its own opinion: three tests used
by people who define certainty for a living, with the one partial failure (the funds' floating payout) named and
haircut.
**Why it matters.** The case demands a definition and an evaluation method. This supplies both, and it changes the IPS
text: the ring-fence sentence becomes load-bearing.
**Sceptic's best objection.** "An IPS is not a trust; Laura can sell anything, so (ii) is a promise, not a wall, which
is exactly why FASB said no." Answer: correct, and the IPS should say so plainly: certainty is conditional on Laura
following the policy, and a separate account for the payment bonds (Final Report recommendation) makes the wall
visible. Second objection: the iBond funds fail (i). Answer: yes for strict fixed cash flows; their holdings are
Treasuries maturing in the target year, so the miss is small and covered by counting less than the expected payout,
the same haircut insurers apply.

---

## Sources searched (26 Oct 2026, WebSearch; page bodies not fetched)
- fa-mag.com, "S&P cuts AAA muni ratings linked to US after federal downgrade"; bondbuyer.com, "Fitch debuts 'AAApre'
  notation to indicate prerefunded debt"
- libcat.library.tamu.edu (FASB 76 in-substance defeasance survey record); viewpoint.pwc.com NFP guide "Extinguishment"
- treasurydirect.gov/files/laws-and-regulations/law-guide-70-fr-37904.pdf; bakertilly.com advance refunding escrow
- eiopa.europa.eu Solvency II Single Rulebook; bankofengland.co.uk PRA MA asset eligibility letter (June 2014)
- addleshawgoddard.com (DB funding code laid 29 Aug 2024); hymans.co.uk DB Funding Code Glossary
- actuary.org/pdf/practnotes/life4.pdf; soa.org Valuation Actuary Symposium 1990
- ideas.repec.org: mathfi v9 i3 p203-228; jfinan v39 i5 p1541-46; jfinec v66 i2-3 p463-506
- federalreserve.gov SVB review (28 Apr 2023); brookings.edu WP62 Duffie (2020)
- hbs.edu / aeaweb.org JEP issue 94 (Coval-Jurek-Stafford); nber.org w14701 (Campbell-Sunderam-Viceira)
- econometricsociety.org Econometrica July 1951 "Optimal inventory policy"; mheducation.com Cachon-Terwiesch;
  faculty.wharton.upenn.edu Cachon CV
- apps.dtic.mil ADA459827 (Gneiting-Raftery); rabin.scholars.harvard.edu (Kőszegi-Rabin)
- london.edu (Richardson-Teoh-Wysocki); storage.fasb.org/ASU_2018-08.pdf; opencasebook.org Restatement 2d §90
- isps.yale.edu, povertyactionlab.org (Karlan-List); ppp.worldbank.org (Flyvbjerg et al.)
- symposium.music.org review (Baumol-Bowen); bloomberg.com 5 May 2025; news.bloomberglaw.com Taiwan insurers FX
- poetsandquantsforundergrads.com, "2018 Best & Brightest: Laura Gao, Wharton School" (not read; could confirm the
  real person's concentrations, but the case text is the only source the IPS may use)
