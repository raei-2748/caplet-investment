AI-generated (Claude Code), Library WO-R11, 28 Oct 2026. Not for submission; research for the IPS and Final Report.

# R11 Synergies: niche ideas from far-off fields, fused into Caplet XR, each critiqued

Asked for by Ahaan: show judges a team that knows things almost nobody knows and reasons to the end of a chain. Rule
for this file: a concept earns a place only if it changes, defends or sharpens a decision in Caplet XR. Concepts
already in R02 (60) and R05 (20) are not repeated as new; where one is built on, it is named.

**How verification works here.** On 28 Oct the proxy blocked every page fetch (irs.gov, wikipedia, cfainstitute,
nbim, cbssports: `CONNECT tunnel failed, response 403`). WebSearch worked but returns titles and URLs only, no page
text. So the tags mean:
- **LISTED** = the source exists with that title at that URL (seen in search results, 28 Oct 2026); its body was not read.
- **UNVERIFIED** = from general knowledge; the exact number or wording must be checked before any use.
- **MODEL (repo)** = a Keel model number already in the repo (THINKING_LOG, number sheet), not new.
No quote below is presented as verbatim unless marked so. Nothing here should be cited until a student or a later
run reads the primary page.

---

## Part 1. Twenty-two concepts

### Certainty: other people's numeric standards

**1. The CRAT "5% probability of exhaustion" test (Rev. Rul. 77-374; Rev. Proc. 2016-42).**
*What:* A US charitable remainder annuity trust (CRAT) pays a fixed dollar amount to a person for life, then the
rest to a charity. The IRS denies the charitable deduction if the chance that the fixed payments exhaust the trust
before the charity gets anything is more than 5%. Rev. Proc. 2016-42 gave a sample clause (end the trust early if
the next payment would leave less than 10% of the starting value) as an alternative to the test.
*Where from:* US tax law; the annuity trust vs unitrust split is already in R02's reading list (26 CFR 1.664-2/-3).
The 5% test is the new part.
*Applies to Laura:* this is a government's own written number for "how certain must fixed-dollar payments be before
we treat a charity's share as real". It is the closest official yardstick to the case's "high degree of certainty".
Keel's G rule misses a payment by more than $1k in about 1.1% of paths (1.8% under stress): roughly three to five
times inside the IRS bar.
*Critique:* the IRS test treats the interest rate as fixed (the section 7520 rate) and draws only the lifespan at
random. It is a mortality test, not a market test. Laura's term is fixed at ten payments, so under the IRS's own
method her probability is either 0% or 100%. Our 1.1% comes from a harsher test (random rates and stocks). So: a
benchmark that shows the order of magnitude officialdom calls "safe enough", never "IRS-approved".
*Verdict:* **Final Report** (a vivid anchor for "high certainty"); in the IPS only as an idea without the citation.
*Status:* VERIFIED earlier by the Library, 27 Oct (`keel/office/outbox/2026-10-27_library_sum-certain.md`, read at
source): 26 CFR 1.664-2/-3 ("a sum certain" vs "a fixed percentage ... determined annually"); Rev. Proc. 2016-42: a
sum-certain trust fails if the chance it runs dry "is greater than 5 percent", computed at one assumed rate; Parks,
Finestone and Leahy (*Tax Notes*, 2015) on trusts that failed when rates fell. Not re-verified here. Still
UNVERIFIED: the exact 10% early-termination clause wording and Rev. Rul. 77-374's own text (LISTED only).
*Built on here (new):* the *Tax Notes* point (fixed-dollar trusts failed when rates fell because the test assumed one
rate) is the same mechanism as Japan's life insurers (17) and our coupon gap. So the 5% test belongs in S5 as a
fifth, homely example of failure mode 4, as well as in S4 as a yardstick.

**2. The return-period fallacy ("design to the 100-year flood").**
*What:* A "100-year flood" has a 1% chance in any one year, not one per century. Over n years the chance of at least
one is 1 - 0.99^n: about 9.6% over ten years.
*Where from:* hydrology and civil engineering (USGS teaching page "We had a 100-year flood two years in a row").
*Applies:* "99% safe" means nothing until you say per what. Laura's risk is not per cheque but over the chain of ten
(concept 3). Any team quoting "99% per year" is quoting a 1-in-10 failure over the decade.
*Critique:* floods are close to independent year to year; Laura's cheque risks are not (they share one cause). The
lesson is the unit, not the formula.
*Verdict:* **IPS-worthy as logic** (one clause: "certainty for all ten, not each one").
*Status:* LISTED: https://www.usgs.gov/water-science-school/science/floods-and-recurrence-intervals (title only).
Arithmetic is ours and exact.

**3. Series reliability and common-cause failure.**
*What:* A system that fails if any one part fails (parts "in series") has reliability equal to the product of its
parts. Ten links each 99% reliable and independent give 0.99^10, about 90%. Engineers also know that redundancy is
defeated by common-cause failure: one event that knocks out every part at once.
*Where from:* reliability engineering (nuclear safety, aviation).
*Applies:* Laura's ten cheques are in series: missing any one breaks the promise. If each rested on its own
independent 99% bet, she would miss one in about one decade in ten. The ladder makes the rungs fail together or not
at all: they share one issuer (the US Treasury) and one residual cause (falling rates on reinvested coupons). That
converts ten small risks into one named risk. This is the deepest reason "certainty defined by where it breaks" works.
*Critique:* the plan does have one common cause it does not control (US default, debt-ceiling timing; R02 #13). A
judge may say the plan has merely concentrated risk. Answer: it concentrated it into the one place every
"risk-free" benchmark in finance already assumes away.
*Verdict:* **IPS-worthy** (Part 3, L1).
*Status:* textbook mathematics; no citation needed.

**4. Safety factor vs probability of failure.**
*What:* Engineers often design with a deterministic margin (a beam rated for 1.5 times the expected load) rather
than a probability. The margin covers what the model does not know.
*Applies:* the range bottom is "what the 2028 deposit leaves after the payments, rounded down". The rounding is a
safety factor, and the 2033 cushion ($7,500 on top of the projected gap, MODEL (repo)) is another. Both are margins
for model error, not for known risk.
*Critique:* safety factors can hide ignorance: nobody knows why 1.5. Ours is sized by the forecast's own error
(R08_5), which is better than a round number, so say that.
*Verdict:* **Final Report** (Portfolio Analysis: why the cushion is $7,500 and not $5,000).
*Status:* general engineering practice; the 1.5 figure is illustrative, UNVERIFIED as any specific code's number.

### The ladder: who else pays fixed dollars from Treasuries

**5. Lottery jackpot annuities: the headline is the cheques, the price is the bonds.**
*What:* A US lottery's advertised jackpot is the sum of the annuity payments (Powerball: 30 graduated payments); the
"cash option" is roughly what it costs to buy the Treasury securities that fund them.
*Applies:* Laura's ten cheques total $500,000; the ladder that pays them cost about $294k on the 16 Oct curve (MODEL
(repo), number sheet). About 40% of the cheques will be paid by the US government's interest, not by Laura. That is
the cleanest one-line explanation of the plan a non-specialist judge could hear.
*Critique:* lotteries fund with zero-coupon STRIPS, which Wharton banned this year. That is exactly why our plan has
a coupon-reinvestment problem a lottery doesn't: a nice way to show the team understands what the ban cost.
*Verdict:* **Final Report** (analogy), possibly a half-line in the pitch.
*Status:* LISTED: Motley Fool "How does the Powerball annuity work" (fool.com, 13 Sep 2017). The 30 payments and
the Treasury funding are UNVERIFIED details; the 5%-a-year growth is UNVERIFIED.

**6. Structured settlements and the "qualified funding asset".**
*What:* When a court awards injury damages as fixed periodic payments, the payer can assign the obligation to a
company that funds it with a "qualified funding asset": under US tax law (IRC section 130), an annuity or an
obligation of the United States.
*Applies:* US law, for people who depend on fixed future payments for their lives, names Treasury obligations as an
acceptable way to fund them. That is the legal mirror of "debts paid with debts owed to her" (the V25 line).
*Critique:* most settlements are funded with life-company annuities, not Treasuries, because annuities can carry
life contingency and are cheaper. Laura has no life contingency (ten fixed years), so Treasuries are the natural
choice here, not a second best.
*Verdict:* **Final Report** (one sentence in Investment Strategy).
*Status:* LISTED: IRS written determinations on qualified assignments (e.g. https://www.irs.gov/pub/irs-wd/202416001.pdf);
Wikipedia "Structured settlement". The section 130(d) wording is UNVERIFIED.

**7. Escrowed-to-maturity municipal bonds: priced like the escrow, not the borrower.**
*What:* When a US city refunds old bonds, it places Treasuries (often SLGS) in an escrow that pays every remaining
coupon and principal. The old bonds then trade as near-Treasuries, whatever the city's own credit.
*Builds on:* R05 #2 (escrow sufficiency, SLGS). New here: the market's verdict that a promise backed by a matched
escrow is worth the escrow's credit, not the promiser's.
*Applies:* the range bottom is owned in Treasuries from January 2028. A co-sponsor who saw the account would rationally
value Laura's bottom like a Treasury, not like a fundraiser's word. That is a costly signal (Spence, R02 #43) that
markets already price.
*Critique:* municipal escrows are legally irrevocable with a trustee; Laura's bottom is her own account and she
could, in law, sell it. The credibility comes from the IPS rule plus her reputation, not a trust deed.
*Verdict:* **IPS-worthy as an idea** (synergy S2).
*Status:* LISTED: Wisconsin DOA defeasance event filings (doa.wi.gov, 2014-2022) and escrow agreements; the
"trades as Treasuries" market pricing is UNVERIFIED as a cited fact (standard market knowledge).

**8. Pension "hibernation" vs buy-out.**
*What:* A fully funded pension scheme either pays an insurer to take the promises (buy-out) or runs them off itself
with a cash-flow-matched bond portfolio ("hibernation"). Funded-status glide paths sell growth assets as the funding
ratio rises.
*Applies:* WInS offers no insurer, so Laura's ladder is hibernation from day one: the plan self-insures by matching.
*Critique:* pension de-risking is triggered by funded status (a price); ours is triggered by dates. A price trigger
on Laura's stocks before 2031 would lock a number nobody has asked for yet and make the plan path-dependent. The
contrast is the useful part (S1).
*Verdict:* **Final Report** (rejected-alternative paragraph).
*Status:* LISTED: plansponsor.com "Pension Hibernation Can Be a Bridge to PRT"; insightinvestment.com "Hibernation
season coming"; GSAM "Beyond buy-out" (2024).

**9. Contingent immunisation (Leibowitz and Weinberger, 1982).**
*What:* A manager may manage actively while the portfolio stays above a "safety net" value; if it falls to the
trigger, the whole portfolio is immunised for the rest of the horizon.
*Applies:* Caplet XR runs the opposite way round. It immunises first (the ladder, then the floor) and takes risk only
with what is left; then it locks on a date (2031). Contingent immunisation protects a liability that exists from the
start against a shrinking cushion; our lock protects a liability that does not exist until Laura names it.
*Critique:* contingent immunisation is a price trigger and so is path-dependent and can whipsaw. Ours cannot whipsaw.
But a judge could say the 2031 lock is "contingent immunisation with a calendar". Fine: say we chose the calendar
because the liability is born on a date.
*Verdict:* **Final Report**; its lesson goes into the IPS through S1.
*Status:* LISTED: CFA Institute, FAJ 1982 "Contingent Immunization, Part I: Risk Control Procedures" and 1983 "Part
II: Problem Areas" (rpc.cfainstitute.org). Already in R02's reading list; the critique here is new.

### Where flooring fits and breaks

**10. The floor-leverage rule (Scott and Watson, FAJ 2013).**
*What:* For a retiree, buy a safe floor for essential spending, put the remainder in a leveraged stock position, and
ratchet the floor up when stocks do well.
*Applies:* the closest academic cousin of Caplet XR: floor first, upside with the rest, gains locked into the floor.
Our 2031 lock is a one-time ratchet.
*Critique:* it needs leverage (banned) and an inflation-linked floor (TIPS, banned). Without leverage, the upside
sleeve is small (our ~21% of the 2028 deposit), which is why our top is modest. It also ratchets repeatedly; we
ratchet once because there is only one announcement.
*Verdict:* **Final Report** (shows we know the frontier and why the rules force a simpler version).
*Status:* LISTED: FAJ 2013 vol 69 issue 5 pp 45-60 (https://ideas.repec.org/a/taf/ufajxx/v69y2013i5p45-60.html;
rpc.cfainstitute.org "The Floor-Leverage Rule for Retirement"; SIEPR working paper). Authors (Jason Scott, John
Watson) UNVERIFIED from the page body.

**11. Flooring and buckets (Zwecher, *Retirement Portfolios*, 2010).**
*What:* Spend from a guaranteed floor; hold upside separately; buckets by time to spending.
*Applies:* the ladder is a bucket per year (ten of them), the floor a bucket for 2033, VT the upside.
*Critique:* bucket strategies usually refill buckets by selling stocks, which reintroduces sequence risk. Laura's
buckets are never refilled from stocks except once, on a known date (January 2033 re-match). Mostly overlaps R02
#24-26, so low marginal value.
*Verdict:* **reject** (overlap; mention at most in Works Cited).
*Status:* UNVERIFIED publication details (not searched).

**12. The bond tent / rising-equity glide path (Kitces; Pfau and Kitces).**
*What:* Hold most bonds around the retirement date, when sequence risk is highest, then let the stock share rise.
*Applies:* after 2033 the ladder pays out a rung a year and Laura's half of VT stays put, so her stock share rises
with no trade. Caplet XR builds a bond tent by itself (S7).
*Critique:* outside the case's window (the case cares about the payments and the contribution, not her wealth mix
after 2033). A selling point for the Final Report only.
*Verdict:* **Final Report**.
*Status:* LISTED: investmentnews.com "Michael Kitces says traditional retirement investment strategy is wrong";
FPA Journal Sep 2015 "Initial Conditions and Optimal Retirement Glide Paths".

**13. Barbell (Taleb) vs ours.**
*What:* Very safe assets plus small, very risky convex bets, nothing in the middle.
*Applies:* Caplet XR is a barbell in shape (Treasuries plus one stock fund).
*Critique:* Taleb's risky end is convex (options: small loss, big gain). VT is linear, and for the contribution the
cap makes it concave (full downside to the bottom, capped upside). So calling the plan a "barbell" would be wrong
in the way that matters. The honest name is a protected note (R02 Aha 1).
*Verdict:* **reject** for the IPS; a "considered and why not" line for the Final Report.
*Status:* UNVERIFIED (not searched; Taleb, *Antifragile*, 2012, from general knowledge).

**14. The Merton share as a cross-check on 21%.**
*What:* Merton's (1969) optimal stock share = (expected excess return) / (risk aversion x variance).
*Applies:* with a stock premium of about 3 points over the floor's yield (Lab's 7.5% stocks vs ~4.5% Treasuries) and
volatility ~16.5% (JPM LTCMA, in CLAUDE.md), a 21% stock share implies a risk-aversion coefficient of about 5
(0.03 / (0.21 x 0.0272)). Economists usually put plausible values between about 2 and 10. So "the floor's expected
interest" and "a mainstream risk appetite" land on the same number by two roads.
*Critique:* Merton uses arithmetic returns (which would imply γ nearer 6-7), applies to total wealth without
liabilities, and ignores human capital. The match is a coincidence of inputs, not a proof. Use it as a sanity check.
*Verdict:* **Final Report** (Portfolio Analysis).
*Status:* arithmetic ours; inputs from repo (JPM vol VERIFIED 27 Sep in CLAUDE.md; 7.5% is the Lab's assumption).
The "2 to 10" range is UNVERIFIED as a citation.

### Promises that broke: four case studies

**15. Alabama PACT (2008-09): a promise invested against the wrong liability.**
*What:* Alabama's prepaid tuition plan promised to pay future tuition (a liability that grows with tuition) and
invested heavily in stocks. The 2008 crash left a shortfall; families sued; a settlement froze payments at 2010
tuition levels.
*Applies:* the textbook case of a fixed promise funded by a growth bet. Laura's promises are fixed nominal and
funded by matched bonds, so the PACT failure is shut by design.
*Critique:* tuition is a real (growing) liability, Laura's cheques are nominal; the parallel is the mismatch, not the
inflation. Also, PACT had new money coming in; Laura has none after 2028, which makes her case stricter.
*Verdict:* **IPS-worthy as one of the four failure modes** (S5); the story itself in the Final Report.
*Status:* LISTED: NPR 18 May 2009 "Market slide snags Alabama tuition program"; Diverse Education "Alabama PACT
settlement freezes tuition payments at 2010 mark"; The Plainsman Nov 2009 "Study predicts PACT may run out in 10
years". Sizes of the shortfall UNVERIFIED.

**16. Equitable Life (UK, 2000): a promise priced as free.**
*What:* Equitable sold pensions with guaranteed annuity rates when interest rates were high, effectively giving
customers a free option. When rates fell the option became very valuable; the House of Lords (Equitable Life v
Hyman, 2000) held that it had to be honoured, and the society closed to new business.
*Applies:* Laura's range is the anti-Equitable. A promise of "at least the bottom, and the stock value if higher"
would hand co-sponsors a free call option on her stocks. The cap prices it: the contribution never exceeds the top,
and the other half of VT stays hers.
*Critique:* Equitable was a mutual with thousands of policyholders and actuarial misjudgement; Laura is one person.
The lesson is narrow: any guarantee has a price, and the cap is how she declines to pay it.
*Verdict:* **IPS-worthy as one failure mode** (S5).
*Status:* LISTED: Wikipedia "Equitable Life Assurance Society v Hyman"; HM Treasury Penrose report (national
archives); Geneva Association 2016 Equitable Life case study PDF. Details UNVERIFIED from page bodies.

**17. Japan's life insurers and Nissan Mutual (1997): reinvestment risk on a fixed promise.**
*What:* Japanese life insurers sold policies with high guaranteed yields in the late 1980s. As Japanese government
bond yields fell through the 1990s, they could not reinvest at the promised rates (the "negative spread"). Nissan
Mutual Life was the first post-war life insurer to fail (1997).
*Applies:* the plan's one open door is the same mechanism in miniature: coupons reinvested at lower yields than
assumed (~$21k gap if yields fall 2 points for good, MODEL (repo)). The 2033 re-match is the guard.
*Critique:* insurers' liabilities ran for decades; ours run ten years and the gap is small and measured. Do not
overdramatise.
*Verdict:* **IPS-worthy as one failure mode** (S5); story in the Final Report.
*Status:* LISTED: Wikipedia "Nissan Life"; NLI Research report 51079; Gen Re "ri16-9"; SOA newsletters (2016-17).
Year 1997 and "first post-war failure" UNVERIFIED from page bodies (strong general knowledge).

**18. Bobby Bonilla's deferred contract: a promise funded by an assumed return.**
*What:* In 2000 the New York Mets agreed to defer about $5.9m owed to Bonilla, paying instead about $1.19m every 1
July from 2011 to 2035 at an implied 8% interest; the owners were widely reported to expect higher returns from
investments with Bernard Madoff.
*Applies:* a fixed nominal payment schedule, like Laura's, funded by an expected return rather than a matched
asset. Laura's plan does the opposite: the rate is locked the day the bond is bought.
*Critique:* the Mets have kept paying (the club, not the fund, bore the risk), so it is a story about a bad funding
assumption, not a default. Do not say the Mets failed.
*Verdict:* **Final Report** (memorable; judges remember baseball more than actuarial science).
*Status:* LISTED: CBS Sports and CNBC "Bobby Bonilla Day" articles ("$1.19 million a year until he's 72", "every July 1
until 2035"). The $5.9m, 8% and Madoff details are UNVERIFIED.

### Reserve funds of nations

**19. Norway's fiscal rule: spend the expected return, not the capital.**
*What:* Norway's government spends from its oil fund roughly the fund's expected real return, cut from 4% to 3% in
2017.
*Applies:* Caplet XR's VT sleeve is sized to about the floor's expected interest: it puts at risk roughly what the
safe money is expected to earn, never the safe money itself. A sovereign rule and our sizing rule share one logic:
risk or spend the yield, keep the seed.
*Critique:* Norway is perpetual and spends on average (it can overspend in bad years); Laura is finite and the
floor is never spent on stocks. The analogy is about the size of the risk bucket, not timing.
*Verdict:* **IPS-worthy as an idea** (S3).
*Status:* LISTED: regjeringen.no press release 16 Feb 2017 "Increased equity share in the Government Pension Fund
Global and adjustment to the expected rate of return in the fiscal policy guidelines"; IPE "Norway slashes SWF's
expected return to 3%".

**20. Chile's structural balance rule: announce off a reference price, not the spot price.**
*What:* Chile sets its spending using a long-term copper price fixed by an independent expert panel, saving windfalls
when copper is above it (Economic and Social Stabilization Fund).
*Applies:* in 2031 the top of Laura's range is set from half of VT's value that day, not all of it. R08_2 found a
haircut on the 2031 stock value is the lever that most moves the odds of reaching the top. Chile's lesson: never
announce from a windfall as if it were permanent.
*Critique:* Chile smooths year after year with an outside panel; Laura names one number once, herself. The "half"
is a crude reference price.
*Verdict:* **Final Report** (S6).
*Status:* LISTED: Danmarks Nationalbank 2008 "The Chilean Fiscal Rule"; Banco Central de Chile working papers 340 and
604; World Bank "Fiscal Councils: the Chilean experience".

**21. Central-bank reserve tranching (liquidity vs investment tranche).**
*What:* Central banks split reserves into a liquid tranche for likely needs and an investment tranche for return.
*Critique:* central banks size the liquid tranche against unknown outflows. Laura's outflows are known to the dollar
and date, so she can do better than a tranche: a match. Mostly covered by R05 #11 (tranching).
*Verdict:* **reject** (overlap, and weaker than what we do).
*Status:* LISTED: ADB blog "Understanding How Central Banks Manage Foreign Exchange Reserves"; IMF WP 2019/052.

### Two that look relevant and aren't

**22. Islamic finance and sukuk ALM; Black-Litterman.**
*Sukuk:* asset-backed, profit-sharing instruments; not on WInS, and the case gives no religious mandate for Laura.
Using it would be name-dropping. *Black-Litterman:* a way to blend views into many-asset weights; we hold one stock
fund, so there are no weights to blend. Both **reject**: relevance would be invented.
*Status:* general knowledge, not searched.

**Already in Keel's thinking, used as building blocks below (not new):** therapeutic window (THINKING_LOG,
ideation rung 3), newsvendor (R05 #13), protected note (R02 Aha 1), tranching and wrong-way risk (R05 #11-12),
zero-order vs first-order release, the lock and the 2033 re-match.

---

## Part 2. Seven synergies

### S1. Immunise each promise on its birthday
*Fusion:* contingent immunisation (9) + pension hibernation (8) + the 2031 lock + Kydland-Prescott (R02 #47).
*Chain:* a promise is a liability the day it is made. Before that it is only a hope, and hopes can carry risk.
The ten cheques are promises from the start (the case states them), so they are matched first, in 2027 and 2028.
The contribution becomes a promise only when Laura names the range in 2031, so that is when its top is moved into
Treasuries. Pension funds and contingent immunisation use a price trigger, which is a guess about markets. A
birthday trigger is a fact about the promise. This is why the lock is not market timing and not CPPI.
*Thought experiment:* a builder quotes a fixed price for a house. Sensible builders buy the timber when they sign
the contract, not when timber looks cheap, and not before anyone has asked for a house.
*Weakness:* the floor is bought in 2028, three years before its birthday, so the rule is "on or before", not "on".
Rivals lock in 2031 too (9 of 12), so the action is common; the principle that explains all three dates is ours.

### S2. Rated like the escrow, not the promiser
*Fusion:* escrowed-to-maturity munis (7) + Spence signalling (R02 #43) + conditional pledges (R05 #17).
*Chain:* co-sponsors discount promises by the promiser's credibility. A city's refunded bonds trade like
Treasuries because the money is already set aside in Treasuries. Laura's bottom is already set aside in Treasuries in
2028. So the bottom can be judged on its escrow, not on her optimism, and a promise whose cost is already paid is
the most costly (therefore most believable) signal she can send.
*Analogy:* two people promise to cover your rent next year. One shows you a term deposit maturing the week before.
You believe the second without needing to like them more.
*Weakness:* no trustee or legal escrow: she could sell. Its force depends on the IPS rule ("no Treasury is sold
before it pays") and on co-sponsors being shown the holdings.

### S3. Risk only the interest
*Fusion:* Norway's rule (19) + protected note (R02 Aha 1) + Merton cross-check (14) + floor-leverage (10).
*Chain:* the 2028 deposit buys a floor; the floor will earn interest by 2033; the plan puts roughly that interest
into stocks today. If stocks go to zero, Laura is back to the deposit's floor; if they do well, she shares the gain.
Three unrelated traditions land near the same size: a sovereign fund's spending rule, a bank's protected note, and
Merton's formula at an ordinary risk appetite.
*Analogy:* a farmer who sows the seed corn and gambles only the harvest. The worst year leaves next year's seed.
*Weakness:* the "expected interest" is a forecast at one curve; the Merton match depends on inputs. And it frames
21% as cautious, which a growth-minded judge may call timid. Answer with the two-cost (newsvendor) logic: the cost
of over-promising is about three times the cost of under-promising.

### S4. A government's yardstick for fixed-dollar giving, passed under a harder test
*Fusion:* CRAT 5% test (1) + return period (2) + series reliability (3).
*Chain:* the US tax code already asks "how sure must fixed-dollar payments be before a charity's share counts as
real?" and answers 5%. But it measures that with a fixed interest rate and a random lifespan. Laura's case is the
mirror: fixed lifespan (ten years), random markets. Keel's models put the chance of any payment more than $1k short at
about 1.1% across all ten (1.8% under stress, MODEL (repo)), counted over the whole chain, not per cheque.
*Thought experiment:* if a regulator who assumes the bonds always earn their rate would accept 1 in 20, a plan that
lets rates move and still misses fewer than 1 in 50 is safer than the law requires for the same kind of promise.
*Weakness:* a tax deduction test is not an investment standard; the legal context differs. Use it to calibrate
"high degree of certainty", never as authority. (The 5% wording itself was read at source on 27 Oct, see concept 1.)
Keep the numbers apart: the 27 Oct memo compared the IRS 5% with the bottom breaking (0.75%); this file compares it
with a payment more than $1k short (1.1%, G rule). Both are MODEL (repo); the Lab should confirm which the Final
Report uses.

### S5. Fixed promises have failed four ways; three doors are shut and the fourth is guarded
*Fusion:* Alabama PACT (15) + Equitable Life (16) + Nissan Mutual (17) + Bonilla (18) + "certainty defined by where it
breaks" (THINKING_LOG).
*Chain:* each famous failure of a fixed promise has one cause:
1. the liability outgrew the assets (PACT: tuition vs stocks), shut: Laura's cheques are fixed and matched;
2. an option was given away free (Equitable), shut: the cap, so the contribution never exceeds the top;
3. the promise leaned on an assumed return (Bonilla), shut: rates are locked when the bonds are bought;
4. coupons had to be reinvested at falling rates (Japan), open: measured (~$21k if yields fall 2 points for good,
   MODEL (repo)) and re-matched once, in January 2033, with a cushion.
That turns "high certainty" from an adjective into an inventory.
*Analogy:* a house inspector's report: three doors locked, one window open and alarmed, and here is the alarm.
*Weakness:* four cases are our selection; a judge can name a fifth (US default; R02 #13). Add it honestly as the
risk every Treasury plan shares. Story detail must be verified before the Final Report.

### S6. A therapeutic window set from a reference price
*Fusion:* therapeutic window (Keel's) + Chile's reference price (20) + newsvendor (R05 #13).
*Chain:* the range must sit inside a window: below it the residency looks unviable, above it Laura looks unreliable
(the case's two costs). Where the top sits depends on what you count VT as worth. Chile learned not to set spending
from a boom-time copper price; Laura counts only half of VT, a built-in reference price. The newsvendor then says
the top should be reached about three times in four if over-promising hurts three times more.
*Analogy:* a doctor doses for the patient's normal weight, not the weight after a big lunch.
*Weakness:* "half" is a rule of thumb, not an expert panel; it should be defended by the R08_2 haircut result.

### S7. The bond tent that builds itself
*Fusion:* bond tent (12) + run-off (8) + sequence risk (R02 #32) + zero-order release.
*Chain:* sequence risk is highest when the most cheques are still ahead. In 2033 Laura is most bond-heavy; each
January a rung pays out and her untouched half of VT becomes a bigger share. So risk rises exactly as the number of
cheques left (and sequence risk) falls, and it costs no trades. The thing advisers engineer with rebalancing, the
ladder does by melting.
*Analogy:* an ice sculpture of a fence around a garden: it protects while it must and melts away as the garden
grows.
*Weakness:* after 2033 is outside what the case asks about; Final Report only.

---

## Part 3. Four logic moves for the IPS

**L1. Correlation is what makes the chain certain.** Ten cheques in series fail if any one fails; if each were a
separate 99% bet, she would miss one about one decade in ten. Spreading bets cannot fix a chain; only a single shared
source can, because then the links stand or fall together. Every rung is a debt of the same issuer, so the ten
risks collapse into one, and it is the one every "risk-free" rate in finance already assumes. The conclusion runs
against the textbook: for the cheques, we deliberately did not diversify.

**L2. The cheques are already paid for by someone else's interest.** $500,000 of cheques cost about $294k in bonds
(MODEL (repo)); the gap is the US Treasury's interest, locked on purchase. Follow it: the 2028 deposit is not needed
for the cheques in nearly all paths (MODEL (repo): at most ~$50k), so almost all of it belongs to the contribution.
The plan never asks one dollar to do two jobs, which is why the bottom can be known in 2028.

**L3. The plan makes exactly one forecast in sixteen years.** The cheques are bought, the bottom is bought in 2028,
and the top is bought on the day it is named. The only number anyone must predict is how far VT moves between 2028
and 2031, and even that only decides where inside the range she lands. A plan that forecasts once can be wrong only
once, and in only one direction.

**L4. The scenario the plan fears is the one bondholders cheer.** Held to maturity, a falling bond price costs Laura
nothing and lets each coupon buy more bond. Its only weakness is the opposite: rates falling for good, so coupons buy
less (the Japanese insurers' trap). That world usually arrives with a slump, the same slump that would shrink a
founder's 2028 income (human capital). So the 2033 re-match is placed exactly where the client's two risks meet.

---

## Part 4. Top five for the IPS, ranked

1. **S5, four failure modes, three shut, one guarded.** It turns "high certainty" into a checklist a judge can
   test, shows deep reading without citing anything, and ends on the 2033 re-match, a rule (Book 7) rather than a
   calculation. It also answers "where does it break?" before a judge asks.
2. **L1, correlation makes the chain certain.** The most surprising sentence on offer: the plan does not diversify
   the cheques, on purpose. It is logic, not trivia, and no rival scanned has it.
3. **S1, immunise each promise on its birthday.** It explains all three dates (2027, 2028, 2031) with one principle
   and lifts the 2031 lock, which rivals share, into a framework rivals lack.
4. **L2, the cheques are paid by the Treasury's interest.** One felt number (the gap between $500,000 and the
   bonds' price) that a non-specialist gets instantly, and it explains why the bottom is known in 2028.
5. **S3, risk only the interest.** It justifies the stock share with a rule (risk the harvest, keep the seed), the
   kind of decision framework Book 7 asks for, with Norway and Merton held back for the Final Report.

Final Report reserve: S4 (the IRS 5% yardstick, already verified 27 Oct), S2, S6, S7, and the four case
stories (PACT, Equitable, Nissan, Bonilla), each to be verified from primary pages before use.

## Sources seen in search (28 Oct 2026, titles only; bodies not read: proxy 403)
- https://www.irs.gov/pub/irs-drop/rp-16-42.pdf ; https://pgcalc.com/support/knowledge-base/taxation/revenue-ruling-77-374 ;
  https://taxnews.ey.com/news/2016-1368-irs-issues-sample-provision-for-charitable-remainder-annuity-trusts-as-alternative-to-probability-of-exhaustion-test ;
  https://pgcalc.com/support/knowledge-base/pg-calc-feature-articles/new-ruling-irs-offers-5-solution-crats
- https://www.usgs.gov/water-science-school/science/floods-and-recurrence-intervals
- https://www.fool.com/retirement/2017/09/13/how-does-the-powerball-annuity-work.aspx
- https://www.irs.gov/pub/irs-wd/202416001.pdf ; https://en.wikipedia.org/wiki/Structured_settlement
- https://doa.wi.gov/DEBFCapitalFinance/2015/EventFiling2015-10_TransRevBonds_Defeasance_April2015.pdf
- https://www.plansponsor.com/pension-hibernation-can-be-a-bridge-to-prt/ ; https://www.insightinvestment.com/united-states/perspectives/hibernation-season-coming/
- https://rpc.cfainstitute.org/research/financial-analysts-journal/1982/contingent-immunizationpart-i-risk-control-procedures
- https://ideas.repec.org/a/taf/ufajxx/v69y2013i5p45-60.html ; https://rpc.cfainstitute.org/research/financial-analysts-journal/2013/the-floor-leverage-rule-for-retirement
- https://investmentnews.com/retirement-planning/michael-kitces-says-traditional-retirement-investment-strategy-is-wrong/79561 ;
  https://financialplanningassociation.org/article/journal/SEP15-initial-conditions-and-optimal-retirement-glide-paths
- https://www.npr.org/2009/05/18/104268001/market-slide-snags-alabama-tuition-program ;
  https://www.diverseeducation.com/home/article/15090527/alabama-pact-settlement-freezes-tuition-payments-at-2010-mark
- https://en.wikipedia.org/wiki/Equitable_Life_Assurance_Society_v_Hyman ; https://www.genevaassociation.org/sites/default/files/research-topics-document-type/pdf_public//20161006_equitablelife_full.pdf
- https://en.wikipedia.org/wiki/Nissan_Life ; https://www.nli-research.co.jp/en/report/detail/id=51079?site=nli
- https://www.cbssports.com/mlb/news/july-1-is-bobby-bonilla-day-why-the-mets-are-still-on-the-hook-for-1-19-million-until-hes-72-years-old ;
  https://www.cnbc.com/2017/07/01/bobby-bonilla-day-means-1-point-19-million-payment-for-the-retired-mets-star.html
- https://www.regjeringen.no/en/aktuelt/increased-equity-share-in-the-government-pension-fund-global-and-adjustment-to-the-expected-rate-of-return-in-the-fiscal-policy-guidelines/id2539303/ ;
  https://www.ipe.com/news/norway-slashes-swfs-expected-return-to-3/10017611.article
- https://www.nationalbanken.dk/en/publications/Pages/2008/09/The-Chilean-Fiscal-Rule.aspx ; https://www.bcentral.cl/en/content/-/detalle/documento-de-trabajo-n-604
- https://blogs.adb.org/node/4541
