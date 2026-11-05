# 04b Wide research: new, verified ideas for tonight's IPS writer

> AI-generated research (Claude, Thu 5 Nov 2026, Sydney). Not for submission and not IPS text. Keel proposes,
> Caplet decides. The "point" lines are ideas in plain English for the writer to put in the team's own words; they
> are not sentences to paste.

**How this was checked.** Every source marked VERIFIED was read with WebFetch on 5 Nov 2026 (curl is blocked); the
quote or figure given is what the page said. UNVERIFIED means search-result title only, or not found.

**What I checked so as not to repeat ideas.** FINAL `ips.txt` (V57), `D38/ips_V58.txt`, `creativity/2026-11-05_shortlist.md`,
the three `creativity/ladder_*.md` rungs, `IDEA_BANK.md` (by grep), `research/R07_synergies/COVERED.md`, and the
headings of R05, R06, R11 and the six R07 scouts. `keel/final_report/ERUDITION_PLAN.md` **does not exist** in the repo
(searched by name), so I could not check against it.

**What the earlier rounds already cover** (I don't propose these again): cash-flow matching vs immunisation (Redington,
Fisher-Weil), defeasance and in-substance defeasance, SLGS and escrow verification in general, lottery annuities and
structured settlements (R11 #5-6, titles only), pension hibernation and buy-out, contingent immunisation, barbell vs
ladder, pull to par, Bodie, Samuelson, Roy, Merton and Campbell-Viceira, human capital, time diversification,
CPPI/portfolio insurance, capital-protected notes, gift range charts and the quiet phase, Tobin vs spend-down, pledge
law and ASC 958/ASU 2018-08, Kornai, Andreoni-Payne, Gneezy 2014, Novy-Marx-Rauh, Harvard's paused Allston building
(#95), Taiwan's insurer FX losses of May 2025 (R05 #20), Perry v US and the 1979 bill delay, Pitt's sinking fund,
reference-class forecasting, real options, newsvendor, focal points, assurance contracts, Townsend's costly
verification, fail-safe defaults.

**What this file adds.** Ten findings the bank doesn't have at all (ranks 1-10), two that are partly new (11, 15), one
that backs the shortlist (12), and verified sources for two ideas the bank had only as search-result titles (13, 14).
The strongest finding: US municipal escrows are written to be sufficient "without
reinvestment". That is the zero-interest test Caplet uses for the ladder's coupon gap, and until now the bank had it
only as UNVERIFIED general practice.

---

## Ranked top 15 for the IPS

| # | Idea (no metaphor) | Field | What it sharpens in the IPS | New? |
|---|---|---|---|---|
| 1 | Escrows that repay old city bonds must be sufficient "without reinvestment"; the purest pension dedication is "assumption-free" | Municipal finance; pension dedication | The reinvestment paragraph: zero is the professional standard and a bound, not a guess | New (R05 #2 had it UNVERIFIED) |
| 2 | Experts' 80% ranges hold the outcome only about a third of the time | Behavioural finance (CFO surveys) | Why the range is built from holdings, not a forecast | New (0 hits) |
| 3 | Scientists keep "how likely" apart from "how good is the evidence" | Science communication (IPCC) | How to state the confidence level the case asks for | New (0 hits) |
| 4 | Gifts promised from a donor's own fortune fail when that fortune falls (2008-10; FTX 2022) | Philanthropy history | Why the top moves into Treasuries before she names it; why her gift is the residency's least correlated money | New (0 hits Lehman, Spelman, FTX) |
| 5 | Breaking a promise costs trust; beating it earns nothing extra | Social psychology; corporate payout policy | The top is a promise to keep, and any surplus is never announced as upside | New (0 hits Epley, Slovic) |
| 6 | Building overruns are large and fat-tailed, so a share of the cost is an open-ended promise and a fixed dollar range isn't | Megaproject research; UK Treasury guidance | The facility-cost and inflation answer; why kept money is never the building's backstop | New (0 hits; critiques Haiku #16) |
| 7 | Trust law judges each holding by its role in the whole portfolio and counts the beneficiary's other income | US prudent-investor law | "Appropriate diversification" answered against her book income and the co-sponsors' money | New (0 hits) |
| 8 | People who hear a range are pulled by both ends, not just the one they like | Negotiation psychology | Both ends are owned because co-sponsors plan on the top too | New (0 hits) |
| 9 | Optimists' hidden difficulties usually aren't rescued by ingenuity | Project economics (Hirschman vs Flyvbjerg-Sunstein) | Why no money is held back "in case the building needs it" | New (0 hits) |
| 10 | The UK pension crisis of 2022 hit borrowed matching that faced collateral calls | Central banking; LDI | One bond per payment, owned outright, so nothing can force a sale | New to the bank (one rival used it) |
| 11 | Callable bonds are repaid early just when rates fall, which is reinvestment risk at the worst moment | Bond market structure | A further reason the ladder holds Treasuries | Partly new |
| 12 | Funders underpay running costs and charities learn to hide them ("starvation cycle") | Nonprofit finance | Supports the shortlist's "her ten payments are already bought" | Support for shortlist #2 |
| 13 | The jackpot a lottery advertises rises with interest rates, because Treasuries pay for it | Lottery finance | Fixed payments are priced on the day they are bought, so waiting is a bet on rates | Covered (R11 #5); now VERIFIED |
| 14 | US tax law accepts only two assets to fund fixed court-ordered payments: an insurer's annuity or a US Treasury obligation | Tax law; insurance failure (Executive Life 1991) | Why Treasuries are held directly and not as an insurer's promise | Covered (R11 #6); now VERIFIED, with a failure case added |
| 15 | Building funders often give all-or-nothing challenge grants | Capital campaigns (Kresge) | Owned money counts toward other funders' thresholds without doubt | Partly new (overlaps the assurance contract, S5 #4) |

---

## 1. "Sufficient without reinvestment": the escrow standard is Caplet's zero-interest test

**What it is (VERIFIED).** When a US city pays off old bonds early, it puts Treasuries in an escrow. The escrow
agreement promises they are enough to pay every remaining instalment, and an independent accountant (the
"verification agent") checks the arithmetic.
- Massachusetts Water Resources Authority, 2025 defeasance escrow agreement, s.3: the securities "will be sufficient,
  without reinvestment, together with any uninvested moneys remaining in the Defeasance Escrow Fund", relying "solely
  on the Verification Report". https://www.mwra.com/media/file/2025-2-defeasance-escrow-agreement
- Wisconsin general obligation defeasance, April 2015, s.4.1(b): any substitution must leave amounts "sufficient after
  such action to pay when due without further reinvestment"; s.2.4: "the Escrow Agent shall not invest the proceeds
  thereof, except as directed in writing by the Issuer". https://doa.wi.gov/DEBFCapitalFinance/2015/EventFiling2015-09_GeneralObligations_Defeasance_April2015.pdf
- NABL (bond lawyers' association): the verification agent, a CPA, independently confirms "that the investments
  purchased for the Escrow Fund will be sufficient". https://www.nabl.org/bond-basics/verification-agent/
- Leibowitz, "The Dedicated Bond Portfolio in Pension Funds, Part I", *Financial Analysts Journal* 1986: dedication is
  "largely assumption-free", and "Reinvestment at positive interest rates, however, can lower pension fund costs
  without substantially increasing risk or complexity." https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/the-dedicated-bond-portfolio-in-pension-fundspart-i-motivations-and-basics
- Why zero is a floor: US 1-, 2- and 3-month bill yields "all turned negative" in the March 2020 flight to safety
  (Axios, 24 Mar 2020, https://www.axios.com/2020/03/24/us-bond-markets-negative-coronavirus). Bonds can yield below
  zero, but cash simply left as cash cannot earn less than nothing.

**Fit.** Strong. Caplet prices the coupon-reinvestment gap "as if every dollar waiting for a payment earned nothing".
That is the test US escrows are written to: enough with no reinvestment at all. Leibowitz's line separates the
assumption-free version from the cheaper one that counts on reinvesting. Caplet does both: it buys the cheaper ladder,
then sets aside the difference, so what she holds passes the assumption-free test.

**What it changes in the IPS.** No change to the trades. The reinvestment paragraph gains a reason. "Earned nothing"
stops looking like an arbitrary worst case and becomes a known professional standard, and a bound: the one rate that
cannot turn out too hopeful. That also answers the case's "explain how they evaluated that level of certainty".

**Point.** Cities that set aside Treasuries to repay old bonds must show the money is enough even if none of it is
reinvested, and we hold Laura's ladder to the same test.

**Honest weakness.** A city escrow is usually built (often with custom SLGS) so that coupons arrive on the payment
dates. Laura's long bonds pay coupons years ahead, so the same test costs her more. Leibowitz himself says reinvesting
"can lower costs without substantially increasing risk", which is a fair argument that zero is over-cautious. The
answer is the case's "high degree of certainty", which is worth what the set-aside costs.

---

## 2. Forecast ranges are usually far too narrow

**What it is (VERIFIED).** In more than a decade of Duke CFO surveys (over 13,000 predictions), "only 36% of future
stock market realisations fall within their 80% confidence intervals". The average interval was 9.4% wide, against
about 40% implied by history. Ben-David, Graham and Harvey, "Managerial Miscalibration", summarised on VoxEU:
https://cepr.org/voxeu/columns/managers-are-miscalibrated (journal: *Quarterly Journal of Economics*, 2013,
UNVERIFIED this session; NBER w16215 seen in search).

**Fit.** Strong for the case's "credible range plus a confidence level". A team that reads its range off model
percentiles ("80% confident") is doing what the CFOs did, and the evidence is that such ranges are overconfident.
Caplet's range is a list of holdings, not a forecast: the bottom is owned, and the top is owned before it is named.

**What it changes.** One clause in the 2031 paragraph: the range comes from what she owns because forecast ranges
tend to miss. It also prepares an answer for the judge who asks "why not give a 90% interval?".

**Point.** When finance chiefs give a range they are 80% sure of, the result lands inside only about a third of the
time, so Laura's range is built from bonds she owns rather than from a forecast.

**Honest weakness.** The CFOs forecast one year of the stock market; Laura's range is a five-year contribution. The
lesson carries (forecast intervals are too narrow), but it is borrowed. Earlier Keel work found the RBA's ranges did
hold about 90% of the time (FRB-56), so the claim is "often too narrow", not "always".

---

## 3. Likelihood and confidence are different things

**What it is (VERIFIED).** The IPCC's guidance for its authors uses two separate measures. *Confidence* is "in the
validity of a finding, based on the type, amount, quality, and consistency of evidence", judged on evidence and
agreement. *Likelihood* is a calibrated probability: "Virtually certain 99-100%", "Very likely 90-100%", and so on.
"Confidence should not be interpreted probabilistically." AR5 Uncertainty Guidance Note (Mastrandrea et al. 2010):
https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf

**Fit.** Good. The case asks for "a confidence level", and most teams will give a model's probability. Caplet can give
both, kept apart: how likely (the bottom fails only if the US Treasury doesn't pay) and what that rests on (bonds
already owned, the strongest kind of evidence). This turns the plan's main idea into the case's own vocabulary.

**What it changes.** In the 2031 paragraph, the confidence level is stated as resting on ownership, not on a
simulation. No numbers are needed in the IPS.

**Point.** Scientists separate how likely something is from how good the evidence is, and Laura's confidence rests on
the best evidence there is: bonds she already owns.

**Honest weakness.** It is a borrowed framework from climate science. Named in the IPS it would read as decoration, so
use only the distinction, never the IPCC words. If the top is fully owned, the range's two ends have the same
evidence, and the writer must make clear what could still move the contribution between them.

---

## 4. Gifts promised from a donor's own fortune fail when it falls

**What it is (VERIFIED).** *Chronicle of Philanthropy*, "As Pledges Fall Short, Colleges Face the Music", 8 Oct 2010
(https://www.philanthropy.com/news/as-pledges-fall-short-colleges-face-the-music/):
- Spelman College received $3 million of a $10 million Lehman Brothers pledge after Lehman collapsed.
- Duke put a Nicholas School building on hold when a $70 million pledge from 2003 did not come through. It expected to
  write off $46.5 million of pledges, up from $14 million in 2008.
- Otterbein lost $1.5 million of a $5 million pledge for a facility, and its debt rose.
- Colleges normally expect 2-5% of pledges to go uncollected. Middle Tennessee State recommended having 50% of gifts in
  hand before building. A South Carolina fundraiser: "You can't pay the contractor with a pledge."
- FTX Future Fund (Reuters via Kitco, 6 Apr 2023): by June 2022 it had spent $132 million across 262 grants. On
  11 Nov 2022 its team said it was "unlikely to honour their commitments", and FTX later asked grantees to return
  money. https://www.kitco.com/news/off-the-wire/2023-04-06/update-1-collapse-ftx-deprives-academics-grants-stokes-fears-forced

**Fit.** Strong, in two ways.
1. The shares backing the top of Laura's range are like a donor's own fortune: they fall exactly when co-sponsors most
   need her number to hold. That is why the top moves into Treasuries before she names it.
2. The residency's other money (co-sponsors, grants, program fees) is a bundle of promises that fail together in a
   downturn. Laura's Treasury-backed contribution is the part of the bundle that doesn't. This gives hard cases to the
   shortlist's idea 3 ("diversify the residency").

**What it changes.** A reason in the 2031 paragraph for owning the top before naming it. It can replace or back up
"co-sponsors count on a number once she says it" (V58).

**Point.** In the 2008 crash, universities lost gifts promised by donors whose own wealth had collapsed, and some
buildings stopped, so Laura owns every dollar she names before she names it.

**Honest weakness.** These are anecdotes from US universities, not Taiwan arts residencies, and the Lehman pledge was a
corporate one. Harvard's paused building (IDEA_BANK #95) already covers "a building promised from a growth pool
waits"; what this adds is the donor's side and the 2-5% norm.

---

## 5. Breaking a promise costs; exceeding it earns nothing

**What it is (VERIFIED).**
- Epley and Gneezy, "Worth Keeping but Not Exceeding", *Social Psychological and Personality Science*, 2014. People
  were happier when a promise was kept than when it was broken, but "exceeding a promise did not make participants any
  happier than simply keeping it". https://www.chicagobooth.edu/review/dont-bother-doing-more-than-you-promised
- Slovic's asymmetry principle: "trust is much easier to destroy than to create" (as summarised in Poortinga and
  Pidgeon, *Risk Analysis*, 2004). https://orca.cardiff.ac.uk/id/eprint/9495/
- Corporate payouts: in a survey of 384 financial executives, managers see a small reward for dividend increases but
  "huge penalties for cuts". 65% of dividend payers would raise new funds for a profitable project rather than cut the
  dividend ("Payout Policy in the 21st Century", CFA digest).
  https://rpc.cfainstitute.org/research/cfa-digest/2006/02/payout-policy-in-the-21st-century-digest-summary

**Fit.** Strong. The case's costs are lopsided: promising too little only "fails to signal viability", while
promising too much damages "credibility". Three separate fields agree that a miss is punished and a beat is not
rewarded. So the range is set where she can surely keep it, and any surplus stays hers and unannounced, never offered
as "possibly more". This is independent support for the newsvendor ratio (IDEA_BANK #5) and the soft-budget idea
(shortlist #4).

**What it changes.** It backs the rule that the top is owned when named. It also argues against any "more if markets
are kind" wording in the co-sponsor text, which matches ladder_opus #4.

**Point.** People punish a broken promise but give no extra credit for beating one, so Laura names only what she can
keep, and what she keeps back stays unannounced.

**Honest weakness.** Epley-Gneezy is a lab study of 60 students solving puzzles. The dividend survey is about firms,
not donors. Taken together they are suggestive, not proof. Under-promising has a cost too (a smaller lead gift draws
less giving: List and Lucking-Reiley, IDEA_BANK #6).

---

## 6. Promise fixed dollars, never a share of the building's cost

**What it is (VERIFIED).**
- Flyvbjerg's "iron law of megaprojects: Over budget, over time, over and over again"; "Nine out of ten such projects
  have cost overruns"; the Sydney Opera House overran by "1,400 percent". https://arxiv.org/pdf/1409.0003
- Sydney Opera House (official site): estimated at $7 million and four years; it cost $102 million, took 14 years, and
  was "largely paid for by a State Lottery". https://www.sydneyoperahouse.com/our-story/sydney-opera-house-facts.html
- Elbphilharmonie, Hamburg: budgeted at €77 million, cost €789 million, "925 per cent over budget", six years late,
  with taxpayers paying all but 10%. https://www.irishtimes.com/news/world/europe/curtain-finally-raised-on-hamburg-concert-hall-at-925-over-budget-1.2856882
- "Set in Stone" (University of Chicago Cultural Policy Center, 2012; more than 700 US arts building projects
  1994-2008): "More than 80 percent of the projects studied ran over budget, some by as much as 200 percent." Some
  institutions later had to "reduce access ... and lay off staff".
  https://macfound.org/media/article_pdfs/cultural_policy_press_release_06_28_2012.pdf
- UK Treasury Green Book: the optimism-bias upper bound for non-standard buildings is +51% on capital cost and +39% on
  duration (standard buildings +24% / +4%), to be reduced only with evidence.
  https://nwssp.nhs.wales/ourservices/specialist-estates-services/specialist-estates-services-documents/ircf-business-case-and-scrutiny-guidance-misc-docs/optimism-bias/
- Fat tails: overruns in 5,392 IT projects have "a fat tail" (https://arxiv.org/abs/2210.01573). Olympic cost
  overruns "follow a power-law distribution"; every Games since 1960 ran over, by 172% on average in real terms
  (https://econpapers.repec.org/paper/arxpapers/2009.14682.htm).
- Taiwan: Weiwuying (National Kaohsiung Center for the Arts) had a total budget of NT$10.58 billion. Building began in
  2010 for completion in 2014, it was "repeatedly delayed" and it opened in 2018. A court awarded the architects
  NT$128.88 million for design changes (CNA, 28 Jul 2020, https://www.cna.com.tw/news/acul/202007280049.aspx). A key
  foreign stage-equipment contractor pulled out mid-build (Mirror Media, 2018,
  https://www.mirrormedia.mg/story/20181109insight007). No overrun percentage was found.

**Fit.** Strong, and it corrects a live suggestion. Haiku's rung (#16) proposed stating her contribution as a share of
the gap. With overruns this large and fat-tailed, a share of the cost is an open-ended promise: a Hamburg-sized
overrun would multiply her bill. A fixed dollar range (which the case asks for) caps her exposure, so an overrun lands
on the project's budget, never on her payments. For the same reason the kept money cannot be "a cushion if the
building costs more" (V57). With fat tails, no cushion of her size covers the overrun that matters.

**What it changes.** It answers the case's "effect of inflation on ... facility costs" with a reason rather than a
forecast. It also supports the shortlist's change from "cushion" to "never promised". In the IPS this is a principle
only, with no figures.

**Point.** Arts buildings usually cost far more than planned, sometimes many times more, so Laura promises a fixed
number of dollars and never a share of whatever the building ends up costing.

**Honest weakness.** The fat-tail findings are for IT projects and the Olympics; for cultural buildings they are a few
famous cases plus "Set in Stone". Laura's residency may be far smaller than a concert hall. The case's own wording
("dollar range") already fixes the form, so this is a reason for a choice the case makes, not a new choice.

---

## 7. The prudent-investor test: the whole portfolio and the beneficiary's other resources

**What it is (VERIFIED).** The Uniform Prudent Investor Act, as enacted in North Carolina (G.S. 36C-9-902/903). A
trustee judges each investment "in the context of the trust portfolio as a whole". Among other things it considers
"Other resources of the beneficiaries known to the trustee", "Needs for liquidity, regularity of income, and
preservation or appreciation of capital", and "The possible effect of inflation or deflation". It "shall diversify ...
unless ... because of special circumstances" the purposes are better served otherwise.
https://ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_36C/Article_9.html

**Fit.** Good, for Wharton's "uses appropriate diversification". The law's test is diversification across everything
the beneficiary relies on, not within one account. Laura's other resources are her book, speaking and licensing
income, which falls in the same slumps as shares; the residency's other resources are co-sponsors' and grant money,
which falls too. So a Treasury-heavy portfolio with one world share fund is diversified where it counts. "Regularity of
income" is the ladder's job, and a liability is the textbook "special circumstance".

**What it changes.** It gives the diversification answer one principle that joins the human-capital point (V57/V58)
and the residency-wide point (shortlist #3): her shares are judged against her income and the co-sponsors' money, not
on their own.

**Point.** Trust law judges each holding by the job it does in the whole picture, including the client's other
income, so we size Laura's shares against her book income and the co-sponsors' money, not on their own.

**Honest weakness.** Laura isn't a trust, and US state law isn't Taiwan's. This is a standard of reasoning, never a
legal claim. If pressed for space, it is the first of these to cut.

---

## 8. Both ends of a range move the listener

**What it is (VERIFIED).** Ames and Mason, "Tandem Anchoring: Informational and Politeness Effects of Range Offers in
Social Exchange", *Journal of Personality and Social Psychology* 108 (2015): 254-274. Against the view that listeners
"focus overwhelmingly on the attractive endpoint", they find "offer-recipients are often influenced by both
endpoints". https://business.columbia.edu/faculty/research/tandem-anchoring-informational-and-politeness-effects-range-offers-social-exchange

**Fit.** Medium-good. Co-sponsors who hear Laura's range will plan partly on its top. So the top cannot be a stretch
figure; it must be as solid as the bottom. That is the plan's lock, here with a reason from how people hear ranges.
It also tells the writer to keep the range narrow and both ends owned, rather than widening the top for show.

**What it changes.** A reason, not a change: why the top is owned before it is named.

**Point.** People who hear a range are pulled by both numbers, not just the lower one, so co-sponsors will plan on
Laura's top figure and it has to be money she already holds.

**Honest weakness.** The research is about price negotiation, where the listener wants a good deal. Co-sponsors
aren't bargaining with Laura, so the "politeness" half of the finding doesn't transfer.

---

## 9. Hidden difficulties usually aren't rescued (the Malevolent Hiding Hand)

**What it is (VERIFIED).** Hirschman (*Development Projects Observed*, 1967) argued that optimism helps, because it
hides difficulties and human creativity then solves them. Flyvbjerg and Sunstein, "The Principle of the Malevolent
Hiding Hand; or, the Planning Fallacy Writ Large", *Social Research* 83(4), 2016, pp. 979-1004, find in a far larger
sample that the malevolent version (hidden costs, no rescue) is common and Hirschman's kind version is rare.
https://arxiv.org/abs/1509.01526 ; https://en.wikipedia.org/wiki/Hiding_hand_principle (sample of 2,062 projects:
UNVERIFIED this session).

**Fit.** Good, as the reason behind idea 6 and the shortlist's "never promised" kept money. A co-sponsor, or Laura,
may reason "start the building and the money will turn up". The evidence says it usually doesn't. Her contribution is
fixed in dollars, and her unpromised money is not quietly earmarked for rescues.

**What it changes.** It supports, and doesn't add, a sentence. Best used in the Final Report, fused with idea 6.

**Point.** Projects started on hopeful numbers are usually not rescued by later cleverness, so Laura's plan never
counts on money turning up after the building starts.

**Honest weakness.** It overlaps reference-class forecasting (R05 #19) and soft budgets (shortlist #4); its value is the
named debate. Don't name it in the IPS.

---

## 10. What broke UK pension matching in 2022 was borrowed money, not matching

**What it is (VERIFIED).** After the September 2022 mini-budget, "the interest rate on UK gilts rose by over 100 basis
points in four days". Leveraged liability-driven funds (assets about 2.7 times equity at the peak) had to post cash,
sold about £25 billion of gilts in five weeks, and caused about half the fall in gilt prices (Bank Underground, 26 Jul
2024, https://bankunderground.co.uk/2024/07/26/what-caused-the-ldi-crisis/). Pension funds with leveraged strategies
faced "margin and collateral calls" that "contributed to fire-sales" (https://wiki.treasurers.org/wiki/UK_LDI_crisis).
On 28 Sep 2022 the Bank of England began temporary gilt purchases "on whatever scale is necessary", citing "a material
risk to UK financial stability" (https://www.bankofengland.co.uk/news/2022/september/bank-of-england-announces-gilt-market-operation).

**Fit.** Good as a pre-emptive answer. A judge who knows "LDI" may think of 2022. The failure needed borrowing:
duration was matched with repo and derivatives, which call for cash when prices fall. Laura holds one bond per payment,
bought outright, so a price fall can't force a sale. This adds force to the V57 sentence contrasting the two pension
methods.

**What it changes.** The "never needs rebalancing" clause could also say that nothing she holds can be called on for
cash.

**Point.** The UK pension funds that nearly failed in 2022 had borrowed to match their payments and were forced to
sell, while Laura owns her bonds outright and never has to sell one.

**Honest weakness.** It doesn't differentiate: a rival entry in Keel's rival panel (entry 04) already cites the 2022
gilt crisis "correctly attributed to leverage". Use it as defence, not as an original idea.

---

## 11. Callable bonds are repaid early just when rates fall

**What it is (partly VERIFIED).** The US Treasury once issued callable bonds. For example, it called "the 11-3/4%
Treasury Bonds of 2009-14", first issued in 1984, at par on 15 November 2009, and "the 12-1/2% Treasury Bonds of
2009-14" on 15 August 2009, years after rates had fallen far below those coupons.
https://webarchive.library.unt.edu/eot2008/20090814010659/http://savingsbonds.gov/news/pressroom/pressroom_comcall071509.htm ;
https://bondpro.gov/news/2009/release-04-15. That the Treasury has issued no callable bonds since the mid-1980s is
UNVERIFIED this session (treasurydirect.gov blocks the fetch). The S2 scout already notes Laura's T-bonds are
"non-callable".

**Fit.** Medium. An issuer calls a bond when rates have fallen, which is exactly when the holder can't reinvest at the
old rate. A corporate or municipal ladder would carry that risk, at its worst moment, on top of coupon reinvestment.
Today's Treasuries can't be called, so the only reinvestment exposure left is the coupons, and the zero-interest
set-aside prices that.

**What it changes.** Nothing in the trades. At most a clause on why Treasuries rather than other high-grade bonds.

**Point.** Many bonds can be repaid early by the borrower when rates fall, just when the money is hardest to reinvest;
the Treasuries in Laura's ladder can't be, so her only reinvestment risk is the interest, and we've set that aside.

**Honest weakness.** WInS allows only Treasuries anyway, so this explains a constraint more than a choice.

---

## 12. The nonprofit starvation cycle: why her bought payments are the gift funders won't give

**What it is (VERIFIED).** Gregory and Howard (Bridgespan, 24 Aug 2009; *Stanford Social Innovation Review*). It
starts with "funders' unrealistic expectations about how much it costs to run a nonprofit". Charities then spend too
little on overhead and underreport it. Foundation allowances for indirect costs averaged 10-15% of a grant, against
about 25% average overhead across for-profit industries. https://bridgespan.org/insights/the-nonprofit-starvation-cycle

**Fit.** Supports the shortlist's idea 2 (Gneezy 2014). Running money is what funders most avoid paying, and Laura's
ten payments cover exactly that before anyone is asked.

**What it changes.** Nothing new; it is a second source for the shortlist's sentence, for the Final Report.

**Point.** Funders like paying for buildings and avoid paying for running costs, so Laura's ten bought payments cover
the part co-sponsors least want to fund.

**Honest weakness.** US evidence, and her $50,000 a year covers only part of the running costs. Don't overclaim.

---

## 13. Rates on the day you buy set the price of fixed payments (lottery jackpots)

**What it is (VERIFIED).** Powerball's FAQ: "The higher the interest rates, the higher the advertised Grand Prize";
the annuity is funded with "U.S. Treasury bonds" (Marketplace, 8 Nov 2022,
https://marketplace.org/2022/11/08/why-high-interest-rates-are-partly-responsible-for-the-2-04-powerball-jackpot). The
annuity is 30 payments, each 5% bigger than the last
(https://www.fool.com/retirement/2017/09/13/how-does-the-powerball-annuity-work.aspx). A state rule sets the cash
value as the annuity amount divided by the "MUSL Annuity Factor"
(https://regulations.justia.com/states/maine/18/553/chapter-20/part-ii/section-553-20-ii-6-0).

**Fit.** Medium, as a real-world twin (R11 #5 had it only as a search title). The advertised jackpot is the sum of the
payments; its price is what Treasuries charge that day. Laura's ten $50,000 payments work the same way, which is why
the ladder is bought in January 2027 and the bottom in 2028, instead of waiting for "better" rates.

**What it changes.** Supports V58's opening rule ("priced at what Treasuries charge"). FR first.

**Point.** A lottery can advertise a bigger jackpot when interest rates are high because Treasuries make the same cash
pay more later, and Laura's payments are priced the same way, on the day she buys.

**Honest weakness.** Already covered as an idea; a lottery is an odd image for a children's author. The funding
instrument may be zero-coupon (banned for Laura), which doesn't change the pricing point.

---

## 14. Two assets US law accepts for fixed court-ordered payments, and the one that failed

**What it is (VERIFIED).** 26 U.S.C. §130(d): a "qualified funding asset" for a structured settlement is "any annuity
contract issued by a company licensed to do business as an insurance company ... or any obligation of the United
States". The payments must be "fixed and determinable as to amount and time of payment" (§130(c)(2)(A)).
https://law.justia.com/codes/us/2012/title-26/subtitle-a/chapter-1/subchapter-b/part-iii/section-130 . Executive Life
of California, seized in April 1991 after junk-bond losses, cut annuity payments 30% for more than 373,000 customers
(https://www.immediateannuities.com/state-guaranty-associations/worse-than-my-worst-nightmare.html, a commercial site;
medium reliability). Executive Life of New York's remaining business was "mostly non-surrenderable annuities that
funded structured settlement agreements" (https://www.nolhga.com/executive-life-insurance-company-of-new-york).

**Fit.** Good for the Final Report. Laura's ten payments are "fixed and determinable as to amount and time". Of the two
assets the law accepts for such schedules, the Treasury held directly is the one with no middleman who can fail.

**What it changes.** For the IPS, at most the idea that she holds the Treasuries herself rather than buying a promise
from an insurer. WInS offers no annuities, so this is a reason, not a choice.

**Point.** US law lets fixed court-ordered payments be funded with an insurer's annuity or a US Treasury bond, and when
one insurer failed in 1991 its annuity holders lost almost a third, so Laura holds the Treasuries herself.

**Honest weakness.** Insurers' guaranty associations softened many Executive Life losses (not checked here). The point
works only as a comparison, since annuities aren't allowed.

---

## 15. Building funders often give all-or-nothing challenge grants

**What it is (VERIFIED).** Washington University's Sam Fox Arts Center got a $1 million Kresge challenge grant. It had
to raise $4.4 million more "by July 1, 2005", and "This is an all-or-nothing challenge—if we fail to meet the goals,
we will not receive the grant."
https://source.washu.edu/2004/02/sam-fox-arts-center-receives-1-million-challenge-grant-from-the-kresge-foundation/

**Fit.** Medium. When other funders' gifts depend on a total being reached, a contribution that might shrink can sink
the whole package. Laura's owned bottom counts toward such thresholds without doubt. It overlaps the assurance contract
(S5 #4) and the threshold point in ladder_opus #4.

**What it changes.** Final Report (co-sponsor section). In the IPS it only backs "money she already owns".

**Point.** Some building funders give only if the rest of the money is raised by a deadline, so an amount Laura already
owns is worth more to the project than a bigger amount she might not have.

**Honest weakness.** One example. Kresge's general practice is not verified.

---

## Fusions (where the intellectual creativity is)

**A. No forecast anywhere in what she promises (1 + 2 + 3, with the owned bottom).** Every safety number in the plan
is a bound that the market can only beat: the bottom is owned and rounded down; the coupon gap is priced at the one
rate waiting cash can always earn (zero, the escrow standard); the top is owned before it is named. That is why the
confidence level can describe evidence (what she holds) and not a model's odds, which experts usually set too narrow.
It extends IDEA_BANK #4 ("no number rests on a share price") to the set-aside and to the confidence statement. In the
IPS this is one idea to state once, not three citations.

**B. Promises are lopsided, so the top is a promise and the surplus is a secret (4 + 5 + 8, with shortlist #4).** A
miss destroys trust and a beat earns nothing (Epley-Gneezy, Slovic, dividends); listeners plan on both ends of a range
(Ames-Mason); fortunes behind pledges fall together (2008-10, FTX). So the top is owned, and the rest stays unpromised
and unannounced. It also supplies the reason the shortlist's soft-budget idea lacked from the co-sponsors' side.

**C. Diversify the residency, judged the way trust law judges it (4 + 7, with shortlist #3 and human capital).** The
residency's money is a portfolio of promises: Laura's career income, co-sponsors' pledges, grants and program fees,
most of which fall in the same recession. Trust law's test is the whole portfolio including "other resources". On
that test, her Treasury-backed contribution is the uncorrelated asset, and one world share fund is enough.

**D. Dollars cap the tail (6 + 9).** Building overruns are big, frequent and fat-tailed, and optimism rarely rescues
them. A fixed dollar range caps her exposure, and keeping her spare money unpromised stops it becoming the building's
open-ended backstop. This answers the case's facility-cost inflation question without forecasting Taiwan's building
costs.

---

## Looks relevant but isn't (critiques)

- **Endowment spending rules (Tobin; Yale's rule).** VERIFIED quote: "The trustees of an endowed institution are the
  guardians of the future against the claims of the present"; Yale blends 80% of last year's spending (inflation-
  adjusted) with 20% of 5% of market value (https://www.ctphilanthropy.org/sites/default/files/resources/Principles-of-Investment-Management.pdf).
  These rules are built for money meant to last forever. Laura's operating money is meant to be spent to zero by 2042,
  so a ladder fits and a spending rule doesn't. (Covered in R07 S3 #3; restated because it is the obvious rival
  framing.)
- **Nonprofit operating-reserve norms (months of expenses).** Those reserves are for the unexpected. Laura's "operating
  reserve" in the case is a schedule of known payments, closer to a defeasance escrow than a rainy-day fund.
- **Redington immunisation for ten fixed payments.** VERIFIED: immunisation "requires that the average durations of
  assets and liabilities be kept equal at all times" and assumes parallel shifts (https://en.wikipedia.org/wiki/Immunization_(finance)).
  For a short list of fixed payments, buying one bond per payment removes the rebalancing. Already in V57.
- **Bodie's insurance argument with a TIPS ladder.** VERIFIED: the cost of insuring against earning less than the
  risk-free rate does not fall with the horizon; "the opposite is true" (https://rpc.cfainstitute.org/research/financial-analysts-journal/1995/on-the-risk-of-stocks-in-the-long-run).
  Bodie's own safe asset is inflation-linked because his goals are real. Laura's payments are fixed nominal dollars, so
  ordinary Treasuries are the exact match, and the TIPS ban costs her nothing.
- **UK pension buy-in.** VERIFIED: a buy-in "ties up a significant proportion of the scheme assets and cannot be
  reversed", and usually leaves "the longer-dated and most risky liabilities" uninsured
  (https://www.insightinvestment.com/uk/perspectives/comparing-buy-outs-and-buy-ins). Laura's ladder is a home-made
  buy-in covering all ten payments with no insurer; nothing to copy.
- **Currency hedging the Taiwan dollar.** The payments are fixed in US dollars by the case; hedges are derivatives
  (banned); no TWD instrument is checked on WInS. The insurers' 2025 losses (R05 #20) show that a matched bond matches
  only in its own currency, which is why the kept money, not the ladder, carries the Taiwan-dollar risk.
- **A share-of-cost pledge** (Haiku #16). See idea 6: an open-ended promise against a fat-tailed cost.
- **"LDI blew up in 2022, so avoid it."** Wrong reading. Leverage and collateral failed (idea 10); unleveraged cash-flow
  matching has no such channel.
- **Hirschman's (benevolent) Hiding Hand as a reason to promise big.** The evidence runs the other way (idea 9).
- **Akerlof's market for lemons.** True (a funder discounts promises it can't check), but it adds nothing to
  signalling (R02 #43) and costly verification (ladder_opus #7). Not re-read; UNVERIFIED this session.
- **Real options.** Correct and already in the bank (R02 #51). As a phrase it sounds clever, but it changes no
  decision beyond "keep some money unpromised".

---

## For the Final Report (cited, with numbers)

- The escrow clauses (MWRA 2025, Wisconsin 2015) and Leibowitz 1986, as the method section's standard for "high
  certainty": a one-line-per-payment schedule checked "without reinvestment" (extends R05 #2's verification schedule).
- Ben-David/Graham/Harvey (36% inside 80% ranges) and the IPCC split between likelihood and confidence, for the
  co-sponsor text and its stated confidence.
- The pledge failures of 2008-10 (Spelman, Duke, Otterbein; 2-5% normal write-offs; the 50% before building) and FTX,
  for the co-sponsor section.
- Overruns: Opera House ($7m to $102m, lottery-funded: an Australian fact that also illustrates a soft budget, since
  an open-ended lottery paid the overrun), Elbphilharmonie (€77m to €789m), "Set in Stone" (over 80% over budget),
  Green Book (+51%), Weiwuying (NT$10.58bn budget; 2014 to 2018; architects' NT$128.88m award), IT and Olympic power
  laws.
- Epley-Gneezy, Slovic and the dividend survey, as the evidence behind the over/under-promise ratio.
- §130(d) and Executive Life, in the "why not buy an annuity?" box.
- Merton (HBR, 2014): measured by the income it buys, "the T-bill is actually quite risky"; T-bills "preserve
  principal at all times, but the income received on them can vary enormously"
  (https://www.firstlinks.com.au/uploads/wp/The-Crisis-in-Retirement-Planning-HBR-July-2014.pdf). Already the basis of
  V58's "Cash only looks safer"; this is the verified quote.
- Australian angle, if the team wants one: exchange-traded Australian Government Bonds have traded on the ASX for
  retail investors since 21 May 2013 (https://www.aofm.gov.au/node/915), so the same ladder can be built at home. Keel's
  standing advice is no "Australia" in the IPS.
- UPIA wording, for the diversification section.

---

## Current numbers re-checked tonight (for the writer's facts, not for the IPS)

| Fact | Value | Source (read 5 Nov 2026) |
|---|---|---|
| Taiwan CPI, Sep 2026 | +2.7% y/y (Aug 2.05%) | https://tradingeconomics.com/taiwan/inflation-cpi/news/590136 (7 Oct 2026) |
| USD/TWD | 32.59 TWD per USD on 30 Oct 2026 | https://fred.stlouisfed.org/series/DEXTAUS |
| Taichung construction cost index, Jun 2026 | +8.35% y/y (Taichung CPI +2.28%) | Taichung DBAS price report 115/06, https://www.dbas.taichung.gov.tw/media/1439319/11506物價月報.pdf |
| Taiwan construction materials sub-index, Apr 2026 | +4.91% y/y (plastics +17.7%, asphalt +13.2%; oil and soil-disposal costs) | China Times, 29 May 2026, https://wantrich.chinatimes.com/news/20260529900140-420101 |
| Taiwan construction cost index, Aug 2025 | +0.3% y/y | UDN, 6 Oct 2025, https://money.udn.com/money/amp/story/5621/9052048 |

**Reading.** Taiwan building costs are rising again in 2026 and faster than general prices (Taichung +8.35% against
CPI +2.28%), after a flat 2025. This supports keeping the facility number in fixed dollars and the kept money
unpromised (idea 6). The repo's "+6.53% y/y, Aug 2026" national figure (CLAUDE.md, from insight_v1) was **not
re-verified** tonight; I found no national total for 2026 that I could read. The Taiwan dollar is slightly weaker than
the repo's 31.82 (18 Sep).

---

## Unverified, so don't state as fact

- Ben-David et al.'s journal and year (QJE 2013): seen in search, not read.
- Flyvbjerg-Sunstein's sample of 2,062 projects.
- That the Treasury has issued no callable bonds since the mid-1980s.
- That Powerball buys zero-coupon Treasuries specifically.
- Kresge's general challenge-grant policy (one example read).
- Guaranty-association recovery for Executive Life annuitants.
- The national Taiwan construction cost index for 2026 (only the Taichung index and the national materials sub-index
  were read).
- Akerlof (not re-read).
