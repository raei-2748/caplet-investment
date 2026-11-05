# READING: what was read for the final-night IPS, and the 15 concepts that matter most for Caplet's plan

AI-generated (Claude Code, finance researcher), Thu 5 Nov 2026 (Sydney). Not submission text and not IPS prose. Keel
is a simulated team, AI-written. Everything below is for the one writer and for the Final Report. "UNVERIFIED" means
I did not read the primary text myself; the claim comes from memory or a secondary source and must be checked before
anyone quotes it.

The plan this reading serves (from `drafts/FINAL/ips.txt`, `CASE_CARD.md`, `FACTS.md`): the first $300,000 buys ten
Treasury holdings (iBonds IBTM-IBTR plus T-bonds maturing 2037-2041), one maturing before each January payment
2033-2042; the 2028 $150,000 first completes the ladder if needed, then mostly buys a late-2032 Treasury fund that sets
the minimum facility contribution, with about that fund's interest in VT; in 2031 the bottom of the range is money
already owned, and the top adds half the shares, moved into Treasuries before it is named; the coupon-reinvestment gap
is priced as if waiting money earned nothing and covered from the kept shares. Static cash-flow matching plus a growth
remainder. No CPPI, no rebalancing on market moves.

---

## Part 1. What I read (all accessed Thu 5 Nov 2026)

### 1a. Damodaran, Corporate Finance (NYU Stern), course page
Index: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/cflect.htm (fetched with `fetch_text.py` and curl; link
list extracted). Read as text (pypdf extraction; page numbers below are PDF page numbers, which match the printed
slide numbers in packet 2 and are close to them in packet 1):

| File | URL | What I used |
|---|---|---|
| Lecture note packet 1 (Sessions 1-15, Spring 2026), 5,029 lines of text | https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket1spr26.pdf | Riskfree-rate conditions (pp. 108-110), hurdle rate (text near "Hurdle rate = Riskless Rate + Risk Premium"), implied ERP method (pp. ~122-125), operating and financial leverage (pp. 167-168), real options to delay/expand/abandon (pp. 333-337) |
| Lecture note packet 2 (Sessions 16-26, Spring 2026), 4,378 lines | https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket2spr26.pdf | CFO survey ranking financial flexibility first (p. 24), pecking order and "managers value flexibility" (p. 30), debt design "match cash flows on debt to cash flows on assets" (p. 112), project-specific financing (p. 123), duration matching the theme-park example (pp. 124-125), dividend inertia (p. 150), dividend changes data (pp. 151-152), Miller-Modigliani assumptions incl. "signaling consequences" (p. 165), signaling story (p. 176) |
| Estimating Hurdle Rates | https://www.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/hurdlerate.pdf | Cross-check of packet 1 |
| Dividend Policy (intro) | https://www.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/divintro.pdf | Phone-company dividend-cut puzzle (slide 35) |
| Assessing Cash Returned | https://www.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/divassessment.pdf | FCFE vs dividends decision matrix ("give managers the flexibility to keep cash") |
| Optimal Capital Structure | https://www.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/capstr.pdf | Cross-check only |
| Damodaran home page, ERP box | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm | "Implied ERP on November 1, 2026 = 4.41%" (trailing 12m, adjusted payout), previous month 4.20%, US Treasury 5.29%, and a US **default spread of 0.22%** netted out to an "adjusted dollar riskfree rate of 5.07%" |

Not read: the webcasts, the weekly puzzles, the project files, the blog posts (the brief said "posts"; the blog is
at http://aswathdamodaran.blogspot.com and I did not open it tonight).

### 1b. Shiller, ECON 252 Financial Markets (Open Yale Courses)
https://oyc.yale.edu/economics/econ-252 now opens the **2011** course (`econ-252-11`, 23 lectures). The **2008** course
(`econ-252-08`, 26 lectures) is a different set. I fetched all 49 lecture pages, each of which carries the full
transcript, and searched them all; the ones below I read in the passages cited.

| Lecture | URL | What I used |
|---|---|---|
| 2008 L4, Portfolio Diversification (CAPM), Ch. 6 "Implications of the Equity Premium" | https://oyc.yale.edu/economics/econ-252-08/lecture-4 | Siegel's 4% equity premium and the "very heavily into stocks" implication, presented as framework, not endorsement |
| 2008 L5, Insurance, Ch. 1 "Circumventing Selection Bias in the Equity Premium Puzzle" | https://oyc.yale.edu/economics/econ-252-08/lecture-5 | Survivorship: the US is "one of the most successful countries", so its premium may not generalise |
| 2008 L7, Behavioral Finance | https://oyc.yale.edu/economics/econ-252-08/lecture-7 | "Mental compartments" passage |
| 2008 L9, Guest Lecture by David Swensen | https://oyc.yale.edu/economics/econ-252-08/lecture-9 | 1987: endowments held a 15-year-high equity weight in June 1987, sold after the crash, and took "until 1993 — a full six years" to restore bonds to the pre-crash weight; "avoid market timing" |
| 2008 L10, Debt Markets: Term Structure | https://oyc.yale.edu/economics/econ-252-08/lecture-10 | Discount bonds, forward rates, expectations theory (background only) |
| 2008 L18, Professional Money Managers, Ch. 5-6 (pensions, ERISA) | https://oyc.yale.edu/economics/econ-252-08/lecture-18 | GM pension 1950: funds should "invest in something other than their own stock"; Studebaker 1963 underfunding; 1990s firms cut contributions because stocks "made their plans look very rich"; PBGC; DB vs DC |
| 2011 L3, Technology and Invention in Finance | https://oyc.yale.edu/economics/econ-252-11/lecture-3 | Chile's Unidad de Fomento (1967), indexed unit of account |
| 2011 L4, Portfolio Diversification | https://oyc.yale.edu/economics/econ-252-11/lecture-4 | Siegel: 6.8% real geometric US return 1871-2006 vs 2.8% on short governments |
| 2011 L6, Guest Speaker David Swensen | https://oyc.yale.edu/economics/econ-252-11/lecture-6 | Diversification defended after the crisis; 1987 "25 standard deviation" event |
| 2011 L21, Exchanges, Brokers, Dealers, Clearinghouses | https://oyc.yale.edu/economics/econ-252-11/lecture-21 | "They called it portfolio insurance, but it wasn't really insurance. It was an automatic sell strategy"; Brady Commission; circuit breakers |
| 2011 L22, Public and Non-Profit Finance | https://oyc.yale.edu/economics/econ-252-11/lecture-22 | Rainy-day funds exhausted in the crisis; Yale borrowing against its endowment |

Searched and found nothing useful for this plan: 2011 L1, L2, L5, L7-L20 except as above, L23; 2008 L1-L3, L6, L8,
L11-L17, L19-L26. I found no transcript that uses "time diversification", "immunization", "duration matching" or
"money illusion".

### 1c. Beyond the two courses (checked tonight by web search; abstracts or bibliographic records only)
| Source | Status |
|---|---|
| Andonov, Bauer and Cremers (2017), "Pension Fund Asset Allocation and Liability Discount Rates", *Review of Financial Studies* 30(8): 2555-2595, https://ideas.repec.org/a/oup/rfinst/v30y2017i8p2555-2595..html | Verified (abstract): US public plans' discount rate is tied to expected asset returns, which rewards more risk; more risk went with worse performance |
| Bodie (1995), "On the Risk of Stocks in the Long Run", *FAJ* 51(3): 18-22 | Verified via secondary sources: the price of a put insuring stocks against underperforming the riskfree bond rises with horizon. Full text not read |
| Samuelson (1963), "Risk and Uncertainty: A Fallacy of Large Numbers", *Scientia* 98: 108-113 | Verified via Ross (1999, JFQA) summary: the colleague who refuses one 50-50 bet but accepts 100 of them |
| Leibowitz and Weinberger (1982), "Contingent Immunization, Part I", *FAJ* 38(6); Part II *FAJ* 39(1), 1983, https://rpc.cfainstitute.org/research/financial-analysts-journal/1982/contingent-immunizationpart-i-risk-control-procedures | Verified (abstract) |
| Yale spending policy, https://your.yale.edu/policies-procedures/2202-endowment-spending-and-distributions | Verified (search summary of Yale's page): 80% of prior-year spending plus 20% of the long-term rate times endowment value, inflation-adjusted, 4.0-6.5% band; 70/30 before 2004 |
| Tobin (1974), "What Is Permanent Endowment Income?", *AER* 64(2): 427-432 | Paper verified; the famous "guardians of the future against the claims of the present" line is **UNVERIFIED** (not found in any result) |
| Milliman (2024), "Frozen pension plan with a surplus? Four strategies", https://www.milliman.com/en-GB/insight/frozen-pension-plan-surplus-four-strategies ; NeuGroup, "Bears in winter", https://connect.neugroup.com/public/blogs/bears-in-winter-well-funded-pension-plans-warm-to-hibernation | Verified (summaries): hibernation = LDI on a frozen plan, payouts shrink it; cash-flow matching vs duration matching defined |
| Redington (1952) JIA; Fisher and Weil (1971) *J. Business*; Roy (1952) *Econometrica* 20(3); Telser (1955) *RES*; Lintner (1956) *AER* 46(2); Bodie, Merton and Samuelson (1992) *JEDC*; Chhabra (2005) *J. Wealth Mgmt*; Das, Markowitz, Scheid and Statman (2010) *JFQA*; Arrow, Harris and Marschak (1951) *Econometrica*; Black and Perold (1992) *JEDC*; Novy-Marx and Rauh (2011) *J. Finance* | Standard citations from memory, **UNVERIFIED tonight** (details as I know them; check before quoting any wording) |

### 1d. Numbers I recomputed (Python, flat-curve, annuity due of ten $50,000)
- Cost of the ten payments in January 2027 at a flat 5.25%: **$295,337**; modified duration 9.58; about **$28,300 per
  100bp**. At 4%: $333,328, Macaulay 10.18, modified 9.79, $326 per bp. The flat **break-even is 5.09%**: above it the
  first $300,000 covers the ten payments, below it it does not. (FACTS.md: on the actual 4 Nov curve they cost
  $300,608, i.e. we are sitting on the break-even.)
- Reserve value in January 2033: 2% $458,112; 4% $421,767; 5% $405,391; 5.25% $401,468; 6% $390,085.
- All-Treasury facility capacity in 2033 ("riskless anchor"): 4% flat $140,327; 4.5% $164,166; 5% $188,080; 5.25%
  **$200,071**. The pasted list's $140k is a 4% number and is stale by about $50-60k; the team's September-curve model
  says about $190k.

---

## Part 2. The 15 concepts, ranked by power for THIS plan

"Distinctive" = a strong rival team is unlikely to have it, or it is applied in a way a judge has not seen. "Generic" =
correct and useful, but every good LDI-flavoured team will say it. Placement: IPS = worth a sentence or clause of
reasoning (no numbers, no citation; Wharton: "sources do not need to be cited in the IPS"); FR = Final Report.

### 1. A riskless asset has two conditions, and the ladder meets one exactly and the other almost (DISTINCTIVE)
- **Concept.** An asset is riskless only if (a) there is no default risk and (b) "there can be no uncertainty about
  reinvestment rates, which implies that it is a zero-coupon security with the same maturity as the cash flow being
  analyzed". So "riskless" is defined per cash flow, not per asset class.
- **Source.** Damodaran, lecture note packet 1 (Spring 2026), PDF pp. 108-109, https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket1spr26.pdf
- **Laura.** It turns "high degree of certainty" into a definition the case asks for (case 97-99): each payment rests on
  a US-government security, which settles condition (a), and the only thing between the plan and condition (b) is the
  coupons and early maturities that must be reinvested, which is exactly the weakness the plan already prices "as if
  every dollar waiting for a payment earned nothing". The test stops being a patch and becomes the measured gap from a
  textbook definition.
- **Where.** IPS: one sentence defining certainty this way. FR: the size of the gap (2038's bond matures 10.5 months
  early, 2039's 7.5 months; Note 1 of the TNA already calls it "reinvestment-rate risk").

### 2. Price every commitment at what Treasuries charge, on the day it is made (DISTINCTIVE in this framing; the economics is standard LDI)
- **Concept.** A fixed promise's honest discount rate is the riskless one. US public pensions discount at expected asset
  returns, which makes a riskier portfolio make the same promise look cheaper; Andonov, Bauer and Cremers find this
  pushed them into more risk and worse results. Shiller tells the same story from the 1990s: rising stocks made plans
  "look very rich", firms cut contributions, and the PBGC was exposed when the market fell; Studebaker (1963) left its
  pension underfunded when it failed.
- **Source.** Andonov, Bauer and Cremers (2017) RFS 30(8) (abstract verified); Shiller, ECON 252 (2008) Lecture 18,
  Ch. 5-6, https://oyc.yale.edu/economics/econ-252-08/lecture-18 ; background Novy-Marx and Rauh (2011) UNVERIFIED tonight.
- **Laura.** Laura makes three commitments on three dates (the ten payments in 2027, the minimum in 2028, the range in
  2031) and each is bought in Treasuries when it is made, so no commitment is ever valued at a return nobody has earned.
  At a flat 5.09% the ten payments cost exactly her first $300,000, which is why the first deposit and the operating
  commitment line up.
- **Where.** IPS: the central idea (the shortlist's idea 1). FR: the Shiller/pension history and the 5.09% break-even exhibit.

### 3. Dedication, not immunization: match each cash flow rather than the average timing (GENERIC concept, DISTINCTIVE if the trade-off is stated)
- **Concept.** Redington (1952) immunization matches present value and duration and needs asset convexity at least
  equal to the liability's; it holds only for small parallel shifts and must be rebalanced as rates and time move.
  Cash-flow matching (a dedicated portfolio) needs no rebalancing and is immune to curve twists, at the price of being
  slightly more expensive and harder to buy exactly. Milliman's 2024 note on frozen ("hibernating") pension plans uses
  the same two-way split.
- **Source.** Redington (1952) and Fisher and Weil (1971) UNVERIFIED tonight; Milliman (2024), URL above; Damodaran
  packet 2 pp. 112 and 123-125 (design the financing so its cash flows match the project's; "project specific
  financing ... match the financing choices to the project being funded").
- **Laura.** Her payments are ten fixed dates, so the plan buys one Treasury per date and never trades on a rate move,
  which is what "each payment has its own bond" means; the README warns not to write "we don't duration-match", so say
  "matched payment by payment".
- **Where.** IPS: already present (para 3); add the reason in a clause (immunization must be re-traded; ours does not).
  FR: the convexity/twist argument and the residual mismatch of 2038/2039.

### 4. Lintner's dividend smoothing: never name a number you might have to cut (DISTINCTIVE)
- **Concept.** Firms raise dividends only to levels they believe they can sustain, adjust slowly, and are punished hard
  for cuts because a dividend is read as a signal of future cash flow. Damodaran's data: most US firms pay the same
  dividend as last year; increases vastly outnumber cuts; "Inertia" is the first driver of dividend policy.
- **Source.** Damodaran packet 2 pp. 150-152 (inertia; 298 increases vs 69 cuts/suspensions in 2020) and p. 176
  ("Dividends can be signals to the market"); Lintner (1956) AER UNVERIFIED tonight. Yale's 80/20 spending rule
  (verified, URL above) is a partial-adjustment rule of the same family.
- **Laura.** Her 2031 range is a dividend announced to co-sponsors: the case says over-promising "could damage her
  credibility" (case 114-115), so the plan names only what it already owns at the bottom and moves the top into
  Treasuries before saying it, as a firm only raises a dividend it can keep paying.
- **Where.** IPS: one clause in the 2031 sentence (the plan's rule "a number said aloud can't quietly be halved" gets
  its pedigree). FR: the signaling data.

### 5. Laura's balance sheet is levered: fixed payments are debt, the facility money is equity (DISTINCTIVE)
- **Concept.** Fixed costs make the residual claim more volatile: levered beta = unlevered beta x (1 + (1 - t) D/E).
- **Source.** Damodaran packet 1, PDF p. 168 ("As firms borrow, they create fixed costs ... that make their earnings to
  equity investors more volatile"); p. 167 (operating leverage).
- **Laura.** With about $400,000 of payments against about $200,000 left over in 2033, D/E is about 2, so a "moderate"
  60/40 portfolio (beta about 0.6) would give the facility money a beta of about 1.8 (0.6 x 3; no tax term, taxes are
  out of scope). Buying the payments in Treasuries removes the leverage, which is why the plan can put only the
  leftover's interest in shares and still be sensible about growth.
- **Where.** IPS: the idea in plain words is worth a clause ("what is left after fixed payments carries all the risk").
  FR: the numbers and a 60/40 comparison.

### 6. Time makes a loss rarer, not smaller: Bodie's put and Samuelson's colleague (GENERIC among experts; the IPS already uses it)
- **Concept.** The cost of insuring stocks against underperforming the riskfree bond rises with horizon (Bodie 1995);
  repeating a bet you would refuse once does not make it safe (Samuelson 1963). Shiller presents Siegel's long-run
  premium as a framework and then warns of selection bias: the US is "one of the most successful countries".
- **Source.** Bodie (1995) FAJ 51(3); Samuelson (1963) Scientia 98; Shiller 2008 L4 Ch. 6 and L5 Ch. 1,
  https://oyc.yale.edu/economics/econ-252-08/lecture-5 ; 2011 L4.
- **Laura.** A fixed $50,000 due in a given January cannot wait for a recovery, so ten years does not make shares safe
  for it. Recomputed: the Bodie put for 6 years at 16% vol is 15.5% of the sleeve (2N(0.16 x sqrt6 / 2) - 1).
- **Where.** IPS: keep the existing sentence. FR: the put figure and Siegel's side, with Shiller's survivorship caveat
  (which also justifies VT over a US-only fund).

### 7. Her income is not a bond: don't hold the risk you already earn (MODERATELY DISTINCTIVE)
- **Concept.** Human capital is an asset; a portfolio should hedge it, not double it (Bodie, Merton and Samuelson 1992).
  Shiller: it took until GM in 1950 for pension funds to "invest in something other than their own stock".
- **Source.** Shiller 2008 L18 Ch. 5 (GM pension, 1950); Bodie-Merton-Samuelson (1992) UNVERIFIED tonight.
- **Laura.** Her 2028 deposit comes from "publishing advances, speaking engagements, licensing" (case 43-45), which can
  dry up in the same downturns that hit shares, so the plan doesn't bet on shares twice and holds no media or publishing
  tilt. The case never says her income tracks stocks, so the IPS can say "can", not "does" (Archive C5).
- **Where.** IPS: already present; the GM-pension example is FR colour.

### 8. Pre-committed dates beat discretion: the 1987 evidence (DISTINCTIVE detail)
- **Concept.** Swensen showed endowments entered 1987 at a 15-year-high equity weight, sold stocks after the crash,
  and needed six years (to 1993) to restore their pre-crash bond weight; "Emotion ruled the decisions". Shiller on the
  same crash: "portfolio insurance ... wasn't really insurance. It was an automatic sell strategy."
- **Source.** Shiller 2008 L9 (Swensen guest lecture), https://oyc.yale.edu/economics/econ-252-08/lecture-9 ; Shiller
  2011 L21, https://oyc.yale.edu/economics/econ-252-11/lecture-21
- **Laura.** The plan changes only on fixed dates, never on a market move, and rejects CPPI-style rules, so it is
  protected both from the institutions that panicked and from the mechanical sellers that helped cause the crash.
- **Where.** IPS: already has the 1987 line; the Shiller wording ("an automatic sell strategy") is sharper than
  "sells shares as they fall". FR: the Swensen data.

### 9. Newsvendor for the top of the range only (DISTINCTIVE; numbers belong in the FR)
- **Concept.** When ordering too much costs k times ordering too little, order the 1/(1+k) quantile of demand (critical
  ratio c_under / (c_under + c_over)). Maths checked: k = 4 gives the 20th percentile.
- **Source.** Arrow, Harris and Marschak (1951) UNVERIFIED tonight; standard operations-research result.
- **Laura.** In this plan the bottom of the range has no quantile at all (it is owned), so the newsvendor rule applies
  only to the top, and it says how far above the owned bottom she can go given that a missed number costs her far more
  than an exceeded one (case 114-115).
- **Where.** FR only (it needs a distribution and a chosen k).

### 10. Match the currency and the cash-flow shape; hold the mismatch where it can be afforded (MODERATELY DISTINCTIVE)
- **Concept.** "The riskfree rate that you use in an analysis should be in the same currency that your cashflows are
  estimated in"; and debt should be designed so its cash flows match the assets' (duration, currency, fixed vs floating,
  "more floating rate if CF move with inflation").
- **Source.** Damodaran packet 1 p. 110; packet 2 p. 112.
- **Laura.** The payments are fixed US dollars, so fixed-rate US Treasuries are the matching asset and indexed bonds
  would add risk (TIPS are banned anyway, and the TNA already argues this, Archive C3); the Taiwan-dollar cost risk sits
  with the facility money and the kept half, never with the payments.
- **Where.** IPS: one clause (the plan already says "in Taiwan dollars"). FR: inflation and FX tables (case 147).

### 11. The kept half is a real option to expand, delay or abandon (GENERIC concept, case-specific use)
- **Concept.** Static analysis misses options to delay, expand and abandon; their value rises with the volatility of
  the underlying. CFOs rank "maintain financial flexibility" first of their financing goals (4.55 of 5).
- **Source.** Damodaran packet 1 pp. 333-337; packet 2 p. 24 (CFO survey) and p. 30 ("Managers value flexibility").
- **Laura.** The more uncertain the building's final cost, the more the unpromised half is worth kept liquid, which
  answers the case's "committing all remaining assets could limit her financial flexibility" (case 102-103) with a
  reason rather than a cushion.
- **Where.** IPS: a clause at most. FR: the reasoning.

### 12. Safety-first, done lexicographically (Roy, Telser) (GENERIC)
- **Concept.** Roy: minimise the probability of falling below a disaster level. Telser: maximise expected return
  subject to that probability being at most alpha.
- **Source.** Roy (1952) Econometrica 20(3); Telser (1955-56). UNVERIFIED tonight.
- **Laura.** The plan sets the shortfall probability on the payments structurally (Treasuries), then lets only the
  leftover seek return, which is Telser's ordering; the case's own words ("protecting the capital required", case 72-74)
  are a safety-first problem.
- **Where.** FR.

### 13. Even the "riskless" asset now carries a priced default spread (DISTINCTIVE, and honest)
- **Concept.** Damodaran's own November 2026 ERP update nets a 0.22% US default spread out of the 5.29% Treasury rate.
- **Source.** https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm (read 5 Nov 2026).
- **Laura.** The plan's one concentrated risk is that every promised dollar is lent to the US government; naming it,
  and saying why it is still the best available match for dollar payments, answers "appropriate diversification"
  better than "thousands of companies" (CASE_CARD flags that row as thin).
- **Where.** FR (the IPS has no room for the number; a clause is possible).

### 14. Contingent immunization and CPPI: the road not taken (GENERIC; useful as contrast)
- **Concept.** Leibowitz-Weinberger: manage actively while a cushion exists, switch to immunization at a trigger. CPPI:
  equity = multiplier x cushion, sold as it falls.
- **Source.** Leibowitz and Weinberger (1982/83) FAJ (verified abstract); Black and Perold (1992) UNVERIFIED tonight;
  Shiller 2011 L21 on portfolio insurance.
- **Laura.** Caplet does the reverse: lock the payments first and risk only what is left, so there is never a trigger,
  never a forced sale and no gap risk.
- **Where.** FR (rejected alternatives). The IPS already rejects portfolio insurance.

### 15. Tobin's intergenerational equity and Yale's 80/20 rule (GENERIC to endowment people; weak link here)
- **Concept.** An endowment should spend what keeps future claimants as well off as present ones; Yale smooths spending
  as 80% of last year's plus 20% of a long-run rate on value.
- **Source.** Tobin (1974) AER 64(2) (quote UNVERIFIED); Yale policy page (verified summary).
- **Laura.** The ten payments are fixed, so no spending rule applies to them; the idea only supports keeping part of the
  leftover unpromised for the residency's later years.
- **Where.** FR only, if at all.

### Considered and left out
- Chhabra's three risk buckets / Shiller's "mental compartments" (2008 L7): generic, and the mapping in the pasted list
  is wrong for this plan (see verdicts).
- Pension hibernation vs buyout: apt as a label for the 2033-2042 phase (no annuity purchase is allowed, so Laura
  self-settles with the ladder), but it adds a term, not an idea. FR at most.
- Shiller's Unidad de Fomento (2011 L3): interesting, but the payments are nominal by the case's rule.
- Merton's distance-to-default as the certainty metric: see verdicts (rejected).

---

## Part 3. Which are genuinely distinctive
Distinctive for this plan: 1 (riskless = per-cash-flow, two conditions), 2 (price commitments at Treasuries, bought
on the day), 4 (Lintner range), 5 (Laura's levered balance sheet), 8 (Swensen's 1987 numbers), 9 (newsvendor for the
top only), 13 (priced US default spread). Generic but necessary: 3, 6, 7, 10, 11, 12, 14, 15.

The strongest single move for the IPS is to put 1, 2 and 4 together: certainty defined by Damodaran's two conditions,
each commitment bought at the riskless price when it is made, and a range announced like a dividend. All three are
already the plan's mechanics; the reading supplies the reasons. None needs a number or a trade.
