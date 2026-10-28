# S2: public finance, the history of debt, and project and construction finance

> Scout S2, R07 (27 Oct 2026). AI-generated research, not for submission. Keel recommends, Caplet decides.
> Domains: rung 1 [3] public finance and the history of debt, [4] project and construction finance.
> No IPS prose below: these are ideas, tests and case studies.

**Source hygiene.** Pages were read through the fetch tool, which returns a small model's summary, so "exact quotes"
below are as returned and must be re-checked against the page before anyone cites them. The fetch budget ran out
twice (shared across agents), so some pages could not be opened: noted where it matters. Everything not opened is
marked UNVERIFIED or dropped. Numbers about Laura come from `CLAUDE.md` and the repo's number sheets; Jun would need
to model anything marked so.

**Two corrections to rung 1.**
1. Seed attribution "Ricardo/Hamilton critiques" of Pitt's sinking fund: the Hamilton who attacked it is almost
   certainly **Robert Hamilton of Aberdeen** (1813), not Alexander. Alexander Hamilton designed the US sinking fund
   in 1790 and is not a critic I could verify. The two are easy to confuse; a judge who knows would notice.
2. Rung 1 called Brady bonds a precedent "which the case rules out for Laura". The *anatomy* is not ruled out. Only
   the instrument (zero-coupon Treasuries, i.e. STRIPS) is. See idea 2.

**The seven ideas, in order of strength**

| # | Idea | Verdict | Lands in |
|---|------|---------|----------|
| 1 | Brady bonds: a sovereign capital-protected note, strip-priced | fits (the anatomy), instrument banned | Final Report; one IPS clause |
| 2 | Pitt's sinking fund: a fund that promises to save versus one that buys | fits as the counter-example | Final Report; one IPS clause |
| 3 | Perry v. United States (1935): "as much bound by their contracts as are individuals" | fits, strengthens "no hedging" | IPS clause or Final Report |
| 4 | Project-finance sizing: lenders promise on the P99 and hope on the P50 | fits the 2031 range | IPS clause; Final Report |
| 5 | The cost overrun facility and the order of call (the facility) | fits the leftover money | Final Report; one IPS clause |
| 6 | Florence's Monte delle doti (1425): dated sums, and who holds the money | partly fits; best as story | Final Report (hook) |
| 7 | Muni escrows and yield burning: the price of the match | seems relevant, mostly isn't | Final Report footnote or bin |

Plus a short list of project-finance devices (DSRA, lock-up, sculpting) that look relevant and mostly are not,
with what to take from each (section 8).

---

## 1. Brady bonds (1989): a sovereign capital-protected note

**1. Verified.** Wikipedia, "Brady Bonds" (https://en.wikipedia.org/wiki/Brady_Bonds): created March 1989 "to convert
commercial bank loans, mostly in Latin America, into tradable bonds"; "The principal amount was usually collateralized
by specially issued US Treasury 30-year zero-coupon bonds"; the debtor country bought the zeros with IMF and World Bank
funds and its own reserves; "Interest payments on Brady bonds, in some cases, are guaranteed by securities of at
least double-A-rated" quality, held at the Federal Reserve Bank of New York; "rolling interest guarantees" are
mentioned (the commonly cited 12-18 month length was NOT on the pages I opened: UNVERIFIED). Ecuador defaulted on its
Brady bonds in 1999; Mexico retired its in 2003.
Pricing method: Susmel, University of Houston course page (https://bauer.uh.edu/rsusmel/7386/brady.htm): partially
collateralised Brady bonds are "part high-quality U.S. Treasury risk and part sovereign risk"; the "stripped yield"
is found by pricing the principal "as a U.S. zero-coupon bond of similar maturity", subtracting that from the total
price, and computing the yield on the remainder. For Mexican pars the stripped yield spread went from 254bp
(31 Dec 1993) to 452bp (31 Mar 1994).

**2. What it is.** A defaulted sovereign's debt was rewritten into a bond whose *principal* is locked in a vault of
Treasury zeros that mature on the same day, while the *coupons* stay exposed to the country's credit. Buyers priced
the bond as two things: a safe piece (valued like a Treasury) and a risky leftover (valued at a high yield), and
the market's own method was to strip the safe piece out and read the price of risk from what remained.

**3. Critique.** (a) The protection was partial: principal only, with coupons protected for a short rolling
window at most. Nobody sold it as "certain". (b) It did not stop the underlying defaults recurring: Wikipedia says
the bonds "did not prevent future looming debt crises". (c) The vault was built with borrowed multilateral money,
so "locked" was about *date-matching and custody*, not about whose money it was. (d) A professional would say the
trick is just a zero-coupon bond plus a risky bond: nothing new in the mathematics. True. What was new was the
packaging and the transparent pricing of each half.

**4. Fit to Laura.** Fits, and closer than any other historical instrument. Her plan's gift is "a capital-protected
note minus the option": a Treasury floor (the protected principal) plus a stock fund worth its expected interest (the
risky leftover). The Brady anatomy is exactly that, with a sovereign as the borrower. Differences that matter: (i)
Laura cannot buy zeros (STRIPS are banned), so her "vault" is coupon bonds and iBond funds, which bring
reinvestment risk Brady's zeros did not have; (ii) Laura is the *investor*, not the sovereign: she holds the safe
piece, and Brady's debtor held it as a cost. (iii) Brady's risky half was a promise from someone else; Laura's
risky half is a stock fund she owns outright, so her leftover has no default, only price risk.

**5. Fusion hook.** Brady (strip the safe part and price the leftover) + the 2031 range: the range is the Brady
"stripped yield" move applied to Laura's own balance sheet: strip what is owned and certain (the floor), then quote
only the leftover with a probability. Also with idea 4: lenders do the same two-piece split in P50/P99 sizing.

**6. Logic device.** *The 1989 twin.* "In 1989 the US Treasury and the IMF faced a debtor with a fixed dated claim and
only partial money. Their answer was: lock the part that must not fail in matched Treasuries, let the rest float,
and tell the buyer which is which." The same sentence describes the Caplet plan in January 2028. A judge who
knows markets would recognise the move; one who does not gets a clean story.

**7. Lands in.** Final Report (one paragraph as the "this has been done before at national scale" proof) and, at
most, an IPS clause that names the structure honestly: protected floor, unprotected remainder, nothing in between.
Not a name-drop: use it only if the sentence changes what the plan says (it does: it justifies stating the bottom
and the top on different confidence levels).

---

## 2. Pitt's sinking fund (1786): a promise to save is not a vault

**1. Verified (parts).**
- Wikipedia, "Sinking fund" (https://en.wikipedia.org/wiki/Sinking_fund): Walpole's fund "worked effectively in the
  1720s" but "governments rarely gave it priority, so the Treasury often raided it". Pitt's 1786 legislation
  "stopped ministers from raiding the fund in crises, raised taxes so a £1 million surplus could reduce the debt"
  and put it under the Commissioners for the Reduction of the National Debt. From 1786 to 1793 it "worked well";
  the war with France in 1793 "destroyed the rationale of the Sinking Fund" (tagged [citation needed] on the page).
- Hansard, 11 Mar 1823 (https://hansard.parliament.uk/html/Commons/1823-03-11/CommonsChamber): a speaker describes
  ministers giving loan contractors 3 percents then "invested that identical money so received in the purchase of
  3 percent stock", at a cost "equal to a perpetual annuity of 268,000l." on the last four wartime loans; another
  says ministers "had already voted away 324,000,000l. of the sinking fund". (Speakers unnamed in the transcript I
  read; the debate also says "Mr. Fox" supplied the 1786 clause on loans.)
- Ricardo, *Principles*, ch. 17 (https://www.marxists.org/reference/subject/economics/ricardo/tax/ch17.htm): "No
  sinking fund can be efficient for the purpose of diminishing the debt, if it be not derived from the excess" of
  revenue over expenditure; and "It is to be regretted, that the sinking fund in this country is only such in name;
  for there is no excess of revenue above expenditure."
- Robert Hamilton (https://en.wikipedia.org/wiki/Robert_Hamilton_(economist)): his 1813 essay on the national debt
  is credited as "the first to expose the economic fallacies involved in Pitt's policy of a sinking fund".
- A full-text of *The Industrial Revolution* on econbiz (https://digi.econbiz.de/viewer/fulltext/1027928145/321;
  author not confirmed by me) says the scheme "lulled the mind of the ministers" and the public "into a false sense
  of security in the matter of borrowing", with £271m borrowed in the Revolutionary War and £618m in the
  Napoleonic.
- Not verified: the often-told "penny at the birth of Christ" parable (Price) and Pitt's 1792 rule attaching a
  sinking fund to every new loan. UNVERIFIED, dropped.

**2. What it is.** From 1786 Britain set aside £1m a year, and its interest, to buy back national debt so that
compound interest would retire it. It worked while the government ran a real surplus. Once the government was
borrowing every year to fight France, the fund was buying debt with borrowed money: the "saving" and the
"borrowing" cancelled and only the appearance of discipline remained.

**3. Critique.** (a) Ricardo's test is the clean one: a fund is real only if it comes from revenue above spending,
not from loans. (b) The deeper fault was complacency: the fund made borrowing feel safe. (c) Defenders (the 1823
speakers) said the earlier version delivered real reductions in peacetime and that the cost lay in how the war
loans were structured; the fund was not pointless, it was mis-fed. A fair critique says "Pitt's fund failed when
its funding source turned out to be circular", not "sinking funds are fraud".

**4. Fit to Laura.** Fits as a **counter-example that explains why Caplet XR is built the way it is**. Test every
dollar the plan counts on with Ricardo's question: *does it exist, or is it promised?* The ten payments pass:
they are bought in January 2027 from the $300k that exists (cost about $298k on the 16 Oct curve, from the repo's
notes). The 2028 $150k does not pass yet: it is a hope from "publishing advances, speaking engagements, licensing",
so the plan correctly lets it fund only the floor and the stocks, never the ten payments. Pitt's lesson in one
sentence: *a payment you are counting on should be prefunded, not scheduled to be saved for.* What Pitt did right
is also worth keeping: he made the money hard to raid by law, which is what a stated rule and a public range do
for Laura against her own future self.
Careful: this is not a warning that her plan is a Pitt fund. It is not. The risk is narrower: the 2031 range's
"owned" bottom is only owned once the 2028 deposit has actually arrived.

**5. Fusion hook.** Pitt + Brady (idea 1): one promised to save, the other locked dated assets against a dated
claim. Together they give the cleanest explanation in the whole bundle of why the ladder is *bought*, not
*saved towards*. Also with idea 6 (the Monte): all three funds (Walpole, Florence, Pitt-after-1793) were raided by the
sponsor they depended on.

**6. Logic device.** *The mortgage-on-a-credit-card test* (our analogy, not from a source): paying down a loan from
a card you have not paid off is not paying down anything. Followed to its end: the only sinking fund that works
is one funded from money that would otherwise have been spent. Plus a case study with a clean date: Walpole's
fund raided (1730s) -> Pitt's law against raids (1786) -> war loans make it circular (1793 onwards) -> abandoned in
the 1820s per Wikipedia. Three generations of the same failure, one idea of what is different this time.

**7. Lands in.** Final Report (Strategy or Articulation: "what we refused to do"), plus one IPS idea: the payments
are *bought*, and the unreliable money is allowed to fund only what can wait. Idea only.

---

## 3. Perry v. United States (1935): the sovereign "is as much bound by its contracts as are individuals"

**1. Verified.** Cornell LII, 294 U.S. 330 (https://www.law.cornell.edu/supremecourt/text/294/330). Perry held a
$10,000 Fourth Liberty Loan bond whose principal was payable "in United States gold coin of the present standard of
value". The Joint Resolution of 5 June 1933 abrogated gold clauses; the Court held Congress could not nullify the
government's own gold-clause obligation: "The United States are as much bound by their contracts as are
individuals," and Congress "has not been vested with authority to alter or destroy those obligations." But Perry
recovered nothing: he "has not shown, or attempted to show, that in relation to buying power he has sustained any
loss whatever."

**2. What it is.** The one moment the US government tried to rewrite its own bond promises (1933). The Supreme Court
said the promise was binding but also said what the promise *protected*: not the metal, but the buying power
the bondholder could prove he had lost. The case therefore says two things at once: the Treasury cannot rewrite
a bond, and a holder is only made whole for what the contract actually promised. **[Window 28 Oct: overstated, partly backwards. Perry v. United States, 294 U.S. 330 (1935, Cornell LII): the Court called the abrogation invalid as applied to the bond, but Perry recovered nothing, because he could not prove loss in buying power. In practice the rewrite stood: "a right with no remedy" (S6 has it right). Never write that the Treasury "cannot rewrite a bond".]**

**3. Critique.** (a) It is a gold-clause case, not a case about ordinary nominal Treasuries; the contract Perry
held was unusual. (b) The Court's sharp line (cannot repudiate, but damages nil) was widely read as a political
compromise, since a win for the bondholders would have cost the government a great deal during a crisis.
I have not sourced that reading: UNVERIFIED. (c) It says nothing about the debt-ceiling kind of delay (a bond paid
late, not rewritten): a different risk, already covered (R02 13).

**4. Fit to Laura.** Fits, and gives the "no hedging" instruction a historical spine. Her liability is nominal dollars
($50k a year, fixed, not indexed) and the assets she is allowed are nominal Treasuries: a nominal promise matched
with a nominal promise. The only time the US ever tried to change the terms of its own bonds, the attempt failed
in court, and the instrument it was applied to was the *unusual* one (gold-indexed), not the plain dollar bond.
It also states precisely what the match does not protect: Laura's $50k in 2042 is worth less than $50k today, and
neither the court nor the contract cares, because both sides are nominal. That is what the case's "fixed nominal"
wording invites.

**5. Fusion hook.** Perry + idea 1 (Brady): Brady shows how a *weak* sovereign had to wrap its promise in collateral;
Perry shows a *strong* one cannot unwrap its own. Together they bracket the range of sovereign promises, with Laura
holding the strongest.

**6. Logic device.** *The 1933 test.* "The worst day for US bondholders in living memory was a day Congress tried
to rewrite a clause, and the Court said it could not. Everything on that day that went wrong was a feature the
plan does not hold." Followed to its end: if you want to find the weak point of a plan made of Treasuries, look
for the term in the contract that is not a plain dollar.

**7. Lands in.** IPS only if one clause is needed to defend "no hedging" (a judge will push on "near-ironclad"); the
rest in the Final Report. It is a strong answer to the predictable judge question "what if the government
changes the rules?"

---

## 4. Project-finance sizing: lenders promise on the P99 and hope on the P50

**1. Verified.** Renewables Valuation Institute, "P50 vs. P99 in Project Finance: How Lenders Size Debt"
(https://courses.renewablesvaluationinstitute.com/pages/academy/p50-vs-p99-in-project-finance-how-lenders-size-debt):
P50 is "the 'expected' case" with a 50% chance of being exceeded; lenders size at a base-case DSCR (examples 1.30x for
contracted revenues, 1.20x in the case study); P99 means "only a 1% chance actual production will fall below this
value", and "some lenders add a P99 constraint with a lower DSCR, such as 1.00x"; lenders "compute two debt
capacities, one from P50 CFADS and one from P99 CFADS, and use the lower result." Under the article's assumption
(normal, 10% standard deviation) P90 is about 87% of P50 and P99 about 77%.
Forvis Mazars, DSCR page (https://financialmodelling.forvismazars.com/resources/debt-service-coverage-ratio-dscr/):
DSCR "measures how many times a project's cash flow can cover its debt repayments"; the "around 1.30x for contracted
infrastructure" figure is a structuring target.
A search result titled "Wind P99, P90, P50 (1-year, 10-year) and Debt Sizing" (edbodmer.com) suggests lenders use
different variance horizons; I did not open it: UNVERIFIED.

**2. What it is.** A bank deciding how much a wind or solar farm can borrow does not choose one forecast. It runs the
expected case and the 1-in-100 bad case and lends the *smaller* amount that satisfies both. The bad case only has to
cover the debt (1.00x); the expected case must leave a cushion (1.20x to 1.30x). Promises are tied to the
bad case, ambition to the good one.

**3. Critique.** (a) The 77% and 87% figures assume a normal distribution; stocks have fat tails and
regime changes (Mandelbrot is already covered, R02 59), so a stock-sleeve P99 is far worse than a normal curve
says. (b) A wind farm's variance is independent between years; stock returns are not, so a 1-in-100 *year* is not a
1-in-100 *path*. (c) The coverage multiples are market convention, not theory. (d) Lenders get to walk away;
Laura cannot.

**4. Fit to Laura.** Fits the 2031 range, and gives it an institutional template that is not just "newsvendor". The
newsvendor (R05 13) tells her where within the range to put the cap. Project lenders tell her *how to state two
numbers on two confidence levels without contradiction*: a floor she can defend in the 1-in-100 case, a top she can
defend only in the expected case, and the rule that the announced gift is the *lower* of what the two tests allow.
Also: lenders ask for 1.30x because revenue varies; Laura's ladder needs only about 1.00x because every payment
is bought and fixed by contract. On the repo's 16 Oct numbers, $300,000 against a $298,087 ladder is 1.006x, which
would be reckless for a wind farm and is exactly right for a Treasury ladder. The only variance left is
coupon reinvestment (the model's ~$21k shortfall if yields fall 2pt, from the repo's number sheet), which is
where the cover premium belongs. This is a clean answer to "why is your cushion so thin?".

**5. Fusion hook.** P50/P99 two-test sizing + Brady (idea 1) + the newsvendor: strip the owned piece (Brady), cover it
at 1.0x on the bad case (P99), and place the gift where the over-promise cost balances (newsvendor). Three tools,
one range, each doing a different job.

**6. Logic device.** *"Who is allowed to be wrong?"* The bank is not allowed to be wrong in the bad case, so it
sizes on P99. The sponsor is allowed to be wrong in the good case, so it hopes on P50. Followed to its end for Laura:
the ten payments are the bank's (no wrong allowed); the gift is the sponsor's (some shortfall tolerated, and capped).

**7. Lands in.** IPS: one clause (the range has two levels because the promise has two risks). Final Report: the full
worked comparison. Jun would need to model what a 1-in-100 stock-sleeve path looks like on a fat-tailed bootstrap,
and what the lower-of-two rule gives versus the plan's current top.

---

## 5. The cost overrun facility and the order of call (the facility)

**1. Verified.**
- "Cost overrun facilities in project finance", Private Equity Bro (https://privateequitybro.com/cost-overrun-
  facilities-in-project-finance/): a cost overrun facility is "a committed source of pre-completion funding sized to
  cover construction cost increases above the base budget and contingency"; the sponsor is obliged "to fund all or a
  capped portion of overruns and shortfalls"; support is "callable only after contingency is fully used and
  contractor obligations are enforced"; the obligation "sits at the parent rather than the project company,
  which supports limited recourse"; worked example: budget 1,000, contingency 70 (7%), overrun facility 100
  (10%): illustrative, not a standard; the independent engineer recommends the size.
- IJGlobal, "Quantifying contingent support in project financings" (https://ijglobal.com/articles/125835/quantifying-
  contginent-support-in-project-financings): "Almost without exception, sponsors' financial reports ignore completion
  guarantees"; "Completion supports are largely assurances that cost overruns will be funded"; proposed capital
  charge = (50% minus probability of abandonment) x mean overrun + probability of abandonment x debt; example $500m
  project, $300m debt, $50m overrun, 1% abandonment -> $27.5m.
- Not opened (budget): rets.ai "completion guaranty", Gowling, Mondaq pieces from the search list. UNVERIFIED.
  The term "cost-to-complete undertaking" itself did not appear on the page I read (the closest were "sponsor support
  agreement" and "parent completion guarantee"); the rung 1 label is slightly off.

**2. What it is.** A big build usually costs more than the budget. Lenders protect themselves with a layered stack
for overruns: the contractor's damages and insurance first, then a contingency inside the budget, then an overrun
facility, and last a capped promise from the sponsor. The sponsor's promise is a *contingent* liability: it is
usually missing from the sponsor's own accounts even though it can be called.

**3. Critique.** (a) The size of contingency (7% in the example) is illustrative; real overruns on megaprojects are
often far larger (reference class work is already covered, R05 19). (b) A cap protects the sponsor only if
the other parties accept the cap, and lenders typically do not accept a cap on a guarantee that protects them:
lenders want completion, not a capped cheque. (c) The IJGlobal formula is a proposal by one author, not a
standard, and the 1% abandonment probability in the example is invented for illustration.

**4. Fit to Laura.** Fits the **leftover money**. The team's provisional call (CLAUDE.md, interview part 2, item 3)
is that the leftover after 2033 is "mainly project flexibility/overrun buffer", and the case says "preserving
flexibility". Project finance supplies the exact design: a capped standby, called only after everyone else's money has
gone first. Three things change in how the plan is argued. (i) Laura's gift is a *fixed capped contribution*, not a
completion undertaking, and the Final Report should say the difference out loud, because overruns arrive when costs
rise (the repo's check: Taiwan construction cost index +6.53% y/y in Aug 2026) and an open-ended promise would
call her money exactly then. (ii) The 2031 range to co-sponsors is itself a contingent commitment, the sort of
thing sponsors forget to count; pricing it (even roughly, with the IJGlobal shape) is the knowledgeable move.
(iii) Laura's "flexibility" has an *order of call*, which makes it concrete rather than a vague hope.
What it does not fit: the ten payments. They are not a facility; nothing is "called" on them.

**5. Fusion hook.** Overrun facility + Courtroom's "lock what you announce" + the dated-promise idea: the gift is what
Laura has *announced* (locked, capped); the leftover is what she has *not* promised (a standby, called last).
Announced money is a vault; unannounced money is a facility. Also with idea 4: the bad case sizes the
promise, the facility covers the rest.

**6. Logic device.** *The order of call.* Who pays first when the building comes in over budget? Contractor and
insurers, then the project's own contingency, then the facility, then (capped) the sponsor. Laura is last and
limited, by design, and that is not coldness: it is why she can promise the ten payments at all. A judge would
remember the shape: the one number in the case that floats (facility cost) is the one thing she is not obliged to
fund.

**7. Lands in.** Final Report (Strategy / Client Knowledge: "what 'flexibility' means") with one IPS idea:
the money above the announced top stays Laura's as a standby, not a promise. Idea only.

---

## 6. Florence's Monte delle doti (1425): dated sums, and who holds the money

**1. Verified (with cautions).**
- Wikipedia, "Monte delle doti" (https://en.wikipedia.org/wiki/Monte_delle_doti): "The Florentine government created
  Monte delle doti in 1425 to provide dowries for brides"; a father made the first deposit when his daughter was
  about five; terms were fixed at seven and a half or fifteen years (minimum cut to five in 1433); the original terms
  forfeited the deposit if the girl died, changed in 1433 to let the father retrieve capital; "the fund sometimes
  proved insolvent"; two depositors in the founding year, none 1426-29, successful from 1433. The page gives
  "about 11 to 12 percent".
- Unibo article on dowry funds (https://cris.unibo.it/bitstream/11585/893969/3/Financing_marriage_in_early_modern_
  Italy.pdf), quoting Molho 1994 p.31: the fund launched in winter 1425 with "cash deposits to bring the Commune's
  indebtedness under control, and (...) stimulate the city marriage market"; subscriptions ran five to fifteen years;
  advertised returns "up to 15 percent"; open for nearly 150 years; as many as 30,000 girls registered; "the list of
  Monte investors reads like the city's social register".
- Market Histories (https://www.markethistories.com/en/the-monte-comune-how-florence-built-the-first-municipal-bond-
  market-1343-1530): in the 1480s the government resorted to "deferring interest payments" and raided the dowry fund,
  and the dowry fund "could not meet its obligations to families expecting payments"; Lorenzo de' Medici
  "reportedly" drew on its money. This is a popular history site, not a scholarly source: UNVERIFIED against Molho.
- The sources disagree on the rate (11-12% vs "up to 15%"): do not quote a rate.
- The book to cite for real is Anthony Molho, *Marriage Alliance in Late Medieval Florence* (Harvard, 1994); I could
  confirm it exists and is cited, not read it. Also Kirshner and Molho, "The Dowry Fund and the Marriage Market in
  Early Quattrocento Florence" (1978): title confirmed in search results only.

**2. What it is.** A city fund where a father deposited money when a daughter was small, and the fund paid a
named sum on a future date (marriage, with minimum terms of years). It is the earliest example I could verify of
a *state-run product that pays a fixed sum on a fixed date to a named person*. It was also a way for the city to
borrow: depositors were lending to the Commune.

**3. Critique.** (a) The promised date was not fixed: payment came at marriage, so fathers fudged ages (a
Renaissance Quarterly article on women's ages in Florence is in the search results; not read). Laura's dates are
fixed by contract. (b) The borrower was the issuer: the city that held the money also needed the money, and it
raided the fund in the 1480s according to the one source I found. (c) The return was a draw, not a match: 11-15% was
what made the fund attractive; it was not sized to a liability. (d) The "600-year precedent" claim flatters the
modern plan: a dowry fund has no ladder, no duration, no matching, so "it's the same idea" would be a stretch to a
fixed-income-literate judge.

**4. Fit to Laura.** Partly. The *shape* fits (money in early, a fixed sum out on a named date for a named
person, run by a sovereign), and the *failure* fits as a warning: the money's safety depended on who was
holding it. Laura's holder is the US Treasury, the issuer is also the custodian (the bonds themselves), and
that is why she is safe. The Florentine fund is the same structure with the weakest possible issuer.
It does not fit: pooling or mortality (forfeited earnings of girls who died funded the rest: a tontine-like
feature Laura's fixed ten payments do not have).

**5. Fusion hook.** Monte + Pitt (idea 2): both were funds that the sponsor could raid. Monte + Brady (idea 1):
the Brady vault at the New York Fed is the answer 560 years later to "who holds the money".

**6. Logic device.** *Same promise, different holder.* "In 1425 a Florentine father lent the city money so that a
named girl would have a fixed sum on a fixed date. In 2027 Laura does the same thing, lending to a different
city." Followed to its end: the instrument has barely changed in 600 years, so the question that matters is the
holder. It is a story judges would remember because it is human (dowries) and the numbers are small.

**7. Lands in.** Final Report only (story hook for the "why prefund and why Treasuries" page). Not the IPS: 500 words
cannot afford an anecdote. Use it only if the Final Report has room for one human history paragraph; the Pitt and
Brady cases carry more weight.

---

## 7. Muni escrows and yield burning: the price of the match

**1. Verified.** SEC administrative proceeding 33-7835 (https://www.sec.gov/litigation/admin/33-7835.htm): the
escrow in an advance refunding is "structured to pay the principal and interest obligations on the old bonds until
the call date" and then pays off principal and any call premium, normally using Treasury or agency securities.
"Yield burning" is "Overcharging by dealers for open market escrow securities in positive arbitrage situations".
In a negative arbitrage deal an overcharge "reduces the municipality's present value savings". An example: Lehman
sold a $15.8m Treasury portfolio in 1994 with a markup and carry of ".42 percent of the prevailing interdealer
market prices"; Lehman agreed to pay $450,151.62 to certain municipal issuers and $4,520,857.29 to the US
Treasury under a separate agreement. Overlap: R05 #1-2 already cover defeasance, escrow sufficiency and SLGS; the
new thing here is the price paid for the escrow.

**2. What it is.** A city that wants to retire old bonds early buys a matched Treasury portfolio and puts it in
escrow. The portfolio's price is the whole game: if the dealer marks it up, the city's saving shrinks. In the late
1990s the SEC found dealers had done this across the industry.

**3. Critique.** The yield-burning cases were about tax arbitrage rules and dealer conduct, not about escrow
design. The escrow-matching mathematics is already in the plan.

**4. Fit to Laura.** Seems relevant, mostly isn't: WInS is a simulation with a flat $10 commission per bond trade
and $25 per stock-ETF trade, no dealer markup. The one thing that survives: a ladder with 7bp to 19bp of
headroom (from the repo's number sheets: $1,913 on the 16 Oct curve) sits in the same order of size as a real-world
execution cost. Illustration only (Jun would need to model it): a markup like the 1994 one, 0.42% of a $298k
ladder, would be about $1,250, which is roughly two-thirds of that headroom. It makes the point that "headroom" is
only real once the price of getting it is subtracted. No change to the plan; a small credibility point.

**5. Fusion hook.** Escrow price + the P50/P99 cover idea (idea 4): the true cover ratio is after costs.

**6. Logic device.** *Cover after costs.* A cushion that costs more to hold than it provides is not a cushion.

**7. Lands in.** Final Report footnote (Articulation: what we learned about real-world execution), or bin. Not IPS.

---

## 8. Project-finance devices that look relevant and mostly are not

Kept short on purpose: they show judgement. All overlap items already in COVERED.md (Lab L-10 coverage test and
waterfall; R05 #11 tranching; Courtroom "lock what you announce").

- **Debt service reserve account (DSRA).** FE Training (https://www.fe.training/free-resources/project-finance/debt-
  service-reserve-account/): "a cash reserve account set aside to make debt payments when debt services are not
  available due to cashflow disruption"; the typical balance covers "projected principal and interest for the next six
  months" (the same page also says 6 to 12 months); a bank letter of credit can replace the cash; funds are released
  in the last quarters of the loan. **Seems relevant, isn't.** A DSRA exists because *revenue* can be disrupted.
  Laura's ladder has no revenue to disrupt after January 2027: the bonds are bought. The nearest real thing is
  her "maturity before payment" buffer (bonds mature in November, the payment is in January), which is a DSRA of
  about two months. Brady's rolling interest guarantee is the same idea (idea 1). Worth one sentence: the buffer has
  a name and a convention. The trap to avoid: a DSRA is often a letter of credit (someone else's promise); here a bond
  is the vault, not a promise.
- **DSCR distribution lock-up.** Forvis Mazars page: lock-up "set below the structuring-phase target and default
  at an even lower threshold"; illustrative 1.30x lock-up and 1.10x default in the worked example (the page's
  own caution: the 1.30x sizing target is not a covenant level). **Partly relevant.** What is new beyond L-10: the
  *three-zone* design (target, lock-up, default) gives warning room before the cliff. A rule such as "nothing
  goes to the facility while funded cover is below the lock-up level" makes the 2031 and 2033 decisions automatic
  instead of discretionary. Overlap is large; fold into Courtroom's existing rule rather than adding a rule.
- **Debt sculpting.** Same page: sculpting "sets each period's principal repayment to match the project's cash flow
  profile, so the DSCR stays at the target level"; once done at structuring, the schedule is fixed. **Seems relevant,
  isn't.** Laura's payments are flat and fixed by the case: there is nothing to sculpt on the liability side. What
  is true (and is a nice phrase): the ladder is a sculpt in reverse, shaping asset maturities to a liability that
  somebody else has already shaped.
- **Equity cure, take-or-pay, hell-or-high-water, PFI availability payments, forward-starting swaps.** Not opened
  or verified: UNVERIFIED. Dropped. (The swap is banned anyway: derivatives are not permitted.)

---

## Best synergy from my domain

**"A vault, not a promise" (Pitt + Brady + Perry + Monte).** Four sovereign stories with the same hidden test:
*who holds the money, and can they touch it?* Walpole and Florence were raided; Pitt's fund became circular;
Brady locked dated Treasuries in custody; and when the US itself tried to rewrite a bond, the Court said it was "as much bound by
its contracts as are individuals". Caplet XR is the Brady design with the safest possible holder and a Pitt-style
discipline (prefund what you need, let only the hopeful money fund what can wait). Add **project finance's two-test
sizing** (promises on the P99, hopes on the P50) and the cost-overrun **order of call** and you get the plan in
one frame: ten payments bought and held (cover 1.0x because variance is bought out), a gift announced and capped at
the lower of two tests, and a leftover that stays hers as a standby, called last. No single idea alone gives
all three layers; together they are a structure judges can repeat in a sentence.
