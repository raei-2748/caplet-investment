# B5a: 2026 Macro & Markets Landscape (starting angle: U.S. rates, the Fed, fiscal position and Treasury credit)

Agent B5a, insight_v1 run, Phase B (question generation), written 2026-09-27. AI-generated research (Claude Code) for
Team Caplet, for brainstorming only. It holds **no submission-ready prose**. Where it says what a sentence "must
contain", that is a checklist; the six students write every word. Any instrument named here is **PENDING WInS
AVAILABILITY + POSITION-LIMIT CHECK** (brief section 14) and is research only.

Status labels (brief section 3): VERIFIED-PRIMARY (I read it on the page myself, 2026-09-27), VERIFIED-REPO-FILE,
SNIPPET-UNVERIFIED, ASSUMPTION, PARAPHRASE-UNVERIFIED. "Derived" = my own arithmetic on labelled inputs (script
steps are in section 5 so anyone can re-run them).

---

## 0. Summary (read this first)

I started where the plan is most exposed: the price of the ten-payment Treasury ladder and the phrase "certain,
barring U.S. default". Seven findings drive most of the 24 questions below. As far as I can tell, no file in
`research/` touches any of them (grep for "debt limit", "term premium", "Penn Wharton", "X-date" and "real yield"
on 2026-09-27 found nothing beyond snippet mentions of TIPS yields).

1. **Higher inflation expectations did not raise rates in 2026. Higher real yields and a higher term premium
   did.** From the 2026 low (Feb 27) to Sept 24 the 10-year yield rose 121bp:
   - 113bp came from the real (inflation-protected) yield: 1.72% to 2.85%.
   - Only 8bp came from breakeven inflation: 2.25% to 2.33%.
   - The Fed Board's Kim-Wright 10-year term premium rose 50bp to 0.96%.
   - Sources: FRED DFII10, T10YIE, THREEFYTP10 (VERIFIED-PRIMARY inputs, derived).
   - The 2.85% real 10-year yield is the highest since 2008-11-24. The term premium is the highest since 2011-02-11.
   - Plain English: the market is paying long-term lenders more, in real terms, than at any time in 18 years. Laura
     needs to be a long-term lender anyway, because her promise is long-dated. **The ladder became affordable
     because of a real-yield window, not an inflation scare.** That is a "why now" no other file states.
2. **"Barring U.S. default" has three layers, and the ladder only fully covers one.**
   - (a) **Outright default.** All three rating agencies are one notch below AAA, with stable outlooks
     (VERIFIED-PRIMARY). The ladder cannot protect against this, but no U.S.-dollar asset can.
   - (b) **Technical delay.** In 1979 some Treasury bills were paid late, amid a debt-limit fight and a
     back-office failure (SNIPPET-UNVERIFIED). Debt-limit "X-dates" (the day the Treasury can no longer pay all its
     bills on time) recur.
   - (c) **"Implicit" default through inflation.** The Penn Wharton Budget Model (Wharton's own unit) describes
     default "of either explicit (Treasury) debt or implicit (pay-as-you-go) debt" becoming "a near certainty on a
     real (inflation-adjusted) basis" at its debt outer bound. It puts "a 25% chance of reaching it in 14 years"
     (VERIFIED-PRIMARY, June 4, 2026). Fourteen years from 2026 is about 2040, inside Laura's 2033-2042 payment
     window.
   - Honest answer: the nominal dollars are close to certain. What those dollars will buy is not.
3. **The debt limit will likely bind again right at Laura's second deposit.** The National Taxpayers Union
   (Aug 20, 2026, VERIFIED-PRIMARY on ntu.org; secondary analysis) projects:
   - the limit is reached around May 2027;
   - the X-date falls in February 2028;
   - Congress "would likely need to increase the debt limit by January 1, 2028".

   That is the date the $150,000 arrives and the top-up purchase happens. It also reports that the Senate leader
   suggested handling it in the lame-duck session "after the November election". That session falls between the
   IPS lock (Nov 6) and Laura's January 2027 purchase.
4. **A dated calendar of events stands between today and the January 2027 purchase.** The ladder's cushion under
   $300k is 27bp (F-104). Events that can move it:
   - FOMC Oct 27-28 and Dec 8-9 (VERIFIED-PRIMARY);
   - Treasury refunding announcement Nov 4, two days before the IPS lock (VERIFIED-PRIMARY);
   - U.S. midterms Nov 3;
   - the stopgap funding bill (continuing resolution, CR) runs out Dec 11 (VERIFIED-PRIMARY secondary page, cra.org);
   - the Iran war / Strait of Hormuz oil shock: Brent crude $114.89 on Sept 22, up from $61.98 on Jan 2 (FRED,
     VERIFIED-PRIMARY).

   The 2-year Treasury yield sits ~100bp above the fed funds midpoint, so markets already price more hikes. A rally
   of more than 27bp probably needs a shock: de-escalation that drops oil, a growth scare, or an equity crash.
5. **Official forecasters are about 100bp below the market.**
   - CBO (Feb 2026) projected a 10-year yield averaging 4.1% in 2026 and 4.4% in 2031-35, with 2026 PCE inflation
     of 2.7% (SNIPPET-UNVERIFIED via CRFB; cbo.gov refused, HTTP 403).
   - JPM's LTCMA bond numbers were set when the 10-year was 4.16% (F-010).
   - Today: 10-year 5.17%; Fed 2026 PCE median 3.7%.
   - Any "reasonable return assumption" (R-C77) that cites these sources as they are understates bond returns and
     misstates the equity premium.
6. **Stocks and bonds fell together in 2026.** The daily correlation between S&P 500 returns and changes in the
   10-year yield was **-0.44 in 2026**, versus -0.06 in 2024 and +0.14 in 2025 (FRED SP500/DGS10, derived). So
   Treasury prices and stocks moved together: when yields rose, both fell. JPM's long-run assumption is ~0 (F-314).
   The growth sleeve's diversification is weaker in this regime than the model assumes.
7. **Taiwan construction costs, measured in U.S. dollars, barely rose.**
   - In New Taiwan dollars the cost index rose 6.53% y/y (F-508).
   - Over the same year the NT dollar weakened from 30.15 to 32.02 per USD (August averages, FRED).
   - So the **USD cost of Taiwan construction rose about +0.3% y/y**, and about **+0.8% a year since 2021**
     (3.6%/yr in TWD, less 2.7%/yr TWD depreciation). Derived, VERIFIED-PRIMARY inputs.
   - Laura's contribution is in dollars. So the case's "effect of inflation on ... facility costs" (R-C85) is, so
     far, mostly a currency story, and the currency can reverse.

Questions are ranked by deadline tier (WInS-now/TN first, then IPS, then FR) within value. The table in section 2 is
the short form; section 3 gives the reasoning and evidence for each.

---

## 1. Terms used (plain English)

- **Real yield**: the yield on inflation-protected Treasuries (TIPS), i.e. the return above inflation.
- **Breakeven inflation**: nominal yield minus real yield; roughly the inflation rate the market is pricing (it also
  contains risk premia, so it is not a pure forecast).
- **Term premium**: the extra yield investors demand for lending long instead of rolling short loans. The Kim-Wright
  estimate on FRED (THREEFYTP10) comes from a Fed Board model; it is an estimate, not an observed price.
- **Debt limit / X-date**: the legal cap on U.S. federal borrowing; the X-date is when the Treasury can no longer pay
  every bill on time without new borrowing authority.
- **Technical default**: a late or missed payment caused by a legal or operational failure, not by inability to pay.
- **Implicit default**: paying debts in full in dollars that have lost much of their value to inflation.
- **Funded ratio**: assets divided by the market price of the promise ($300,000 / $292,264 = 1.026 on 9/25, F-117).
- **CAPE**: price divided by 10-year average inflation-adjusted earnings; a slow-moving valuation gauge.
- **Stock-bond correlation**: whether stock returns and bond returns move together (+) or opposite (-).

---

## 2. The questions (short form)

| # | Question | Anchor | Would change | Deliverable | Domain | Seed |
|---|---|---|---|---|---|---|
| Q01 | Should the first Treasury trade note name the real-yield window (real 10y 2.85%, highest since 2008) as the reason the ladder is affordable now? | F-004, F-008, F-009, F-111, R-T9 | sentence (TN note #1, IPS "why") | WInS-now, TN, IPS | D1 | 21 |
| Q02 | Which dated events before Jan 2027 could erase the 27bp cushion, and should the IPS rule be a funded-ratio trigger rather than a forecast? | F-104, F-112, F-005, F-007 | decision (IPS purchase rule) | IPS, FR | D1 | 21 |
| Q03 | Which of the three layers of "default" (outright, technical delay, inflation) does the ladder cover, and which must the certainty definition name? | R-C47, R-C54, R-C55 | sentence (IPS certainty definition) | IPS, FR | D1 | 22 |
| Q04 | Should the team use Wharton's own Penn Wharton Budget Model (25% chance of the debt outer bound by ~2040) to state honestly how certain "certain" is? | R-C56, R-C85 | sentence + number (FR assumptions) | FR | D1 | 22 |
| Q05 | Does the projected Feb 2028 X-date, right at the Jan 2028 deposit, require a clause in the 2028 top-up rule? | F-601, R-C77 | decision (FR operating rule) | FR, IPS | D1 | null |
| Q06 | Do Nov-15 maturities (47 days early; 2033-01-01 is a Saturday) double as a buffer against a technical payment delay? | R-C45, R-C47 | decision (maturity choice) + sentence | FR | D1 | 22 |
| Q07 | What will the plan do if the U.S. is downgraded again, and should the IPS pre-commit to "hold, do not sell"? | R-C89, R-I10 | sentence (IPS decision rule) | IPS | D1 | 22 |
| Q08 | Since no U.S.-dollar asset is safer than a Treasury, should the IPS spend one clause on sovereign risk and use the words on risks the ladder does not cover? | R-I18, R-C54 | sentence (IPS word budget) | IPS | D9 | 22 |
| Q09 | What is the real value of the ten payments at market breakeven vs a named stress, and who bears the erosion? | R-C46, R-C85, R-C44 | number (FR) | FR | D1 | 23 |
| Q10 | Is a 1970s-style inflation regime a base case or a stress case for 2033-2042, given the 2026 evidence on Fed independence? | R-C85, F-007, F-009 | sentence (FR assumption) | FR | D1 | 23 |
| Q11 | Should the post-2033 flexibility money (not the reserve) be the named inflation buffer for the operating budget, and partly in TIPS? | R-C58, R-C84, R-C44 | decision (flexibility composition) | FR | D3 | 23 |
| Q12 | Which return source is "reasonable" when JPM and CBO sit ~100bp below today's yields: a published CMA or market yields? | R-C77, F-010, F-317 | number (projection inputs, 2031 range) | IPS, FR | D3 | null |
| Q13 | At today's yields the equity premium over Treasuries is ~1.7pp and CAPE ~41: does 60% sleeve equity still earn its p5 cost? | R-C38, F-301, F-407 | number (sleeve equity %) | IPS, FR | D3 | null |
| Q14 | Should sleeve risk and the 2031 range be stressed at a positive stock-bond return correlation, as realised in 2026? | F-314, R-S26 | number (sleeve p5, 2031 range) | FR, WInS-now | D3 | null |
| Q15 | Should the team pre-commit, in a trade note, not to trade the hedge around the Oct 28 FOMC and Nov 4 refunding? | R-T9, R-W73, R-W76 | decision (WInS conduct) | WInS-now, TN | D1 | null |
| Q16 | Should every Treasury trade note record that day's ladder cost/funded ratio as a dated test of the strategy? | R-T9, F-111, F-117 | decision (note format) | WInS-now, TN | D9 | null |
| Q17 | Does the 20-year "hump" (20y 5.54% > 30y 5.49%) make the 10-20y sector the cheapest place to buy Laura's long rungs? | F-001, F-107 | decision (instrument) | WInS-now, TN, FR | D1 | null |
| Q18 | Should the WInS book hold individual Treasuries (which lock a yield) instead of only constant-maturity ETFs, to show the ladder itself? | F-606, F-607, R-C75 | decision (WInS instrument) | WInS-now, TN | D10 | null |
| Q19 | Is a 2027 U.S. recession the common cause linking falling yields and a smaller 2028 deposit, and how big is the joint tail? | R-C86, F-403, F-404 | number (FR joint-tail row) | FR | D3 | null |
| Q20 | How does an AI-equity crash feed into Treasury yields and the Jan 2027 cushion, and which way does it cut for Laura? | R-C82, F-111 | sentence + decision | FR, IPS | D2 | null |
| Q21 | Is the growth sleeve secretly doubling Laura's Taiwan bet through AI-chip supply-chain concentration in the index? | R-C39, R-S24, R-W71 | decision (sleeve index choice) | IPS, WInS-now | D4 | 24 |
| Q22 | Measured in U.S. dollars, how fast have Taiwan construction costs risen, and does that change the facility-inflation sentence? | R-C85, F-508, F-512 | sentence + number | FR | D4 | 25 |
| Q23 | Is Taiwan's 2026 construction-cost jump an AI-boom wage spike that will fade before 2033, or a new trend? | F-508, F-504, R-C94 | number (facility inflation assumption) | FR | D4 | 25 |
| Q24 | If the residency cannot operate in Taiwan, is the USD Treasury reserve portable, and should the promise be tied to the residency rather than the place? | R-C39, R-C45, R-C48 | sentence (FR, co-sponsor draft) | FR | D4 | 24 |

---

## 3. Questions with reasoning and evidence

### Q01. Why is the ladder affordable now? (seed 21; tier 1)
- **Question:** Should the first Treasury trade note name the real-yield window as the reason the ladder became
  affordable, instead of "rates are high"? The real 10y is 2.85%, the highest since Nov 2008, and the term premium is
  the highest since 2011.
- **Anchors:** F-004 ("5.18% on 2026-09-24 is the highest daily close since 2007-07-06"), F-008, F-009, F-111, R-T9.
- **Evidence** (FRED, VERIFIED-PRIMARY inputs, derived; script in section 5):

  | Date | 10y nominal | 10y real (DFII10) | 10y breakeven | Kim-Wright term premium |
  |---|---|---|---|---|
  | 2026-01-02 | 4.19 | 1.94 | 2.25 | 0.58 |
  | 2026-02-27 (low) | 3.97 | 1.72 | 2.25 | 0.46 |
  | 2026-06-30 | 4.44 | 2.20 | 2.24 | 0.70 |
  | 2026-09-01 | 4.79 | 2.44 | 2.35 | 0.90 |
  | 2026-09-24 | 5.18 | 2.85 | 2.33 | 0.96 |

  Real 10y 2.85% last matched or beaten 2008-11-24. The term premium 0.96% last matched 2011-02-11.
- **Hypothesis (guess):** Yes. In plain terms: the market is paying lenders an unusually large reward above
  inflation, and Laura is a natural long-term lender because her promise is long-dated. So she earns the premium
  without taking on a risk she does not already have: she holds to maturity, so price swings do not matter to her.
  - This is a "why now" rooted in her liability, not a market forecast.
  - It also warns that the window may close (Q02).
- **Would change:** the sentence in Trading Note #1 (why this trade, why now) and one IPS reason. A strong sentence
  must contain: the dated real yield or funded ratio; "held to maturity"; and a link to the ten payments. It must not
  forecast rates.
- **North star:** it shows Laura that we bought her promise when the market was paying us to, and that we are not
  guessing at rates.

### Q02. What could erase the 27bp cushion before January 2027, and what form should the rule take? (seed 21, extends open item "rule if rates fall")
- **Question:** Which dated events could push long yields down by more than 27bp before Laura's cash arrives? And
  should the IPS write the rule as a funded-ratio trigger ("buy longest rungs first until funded; top up in 2028")
  rather than any rate view?
- **Anchors:** F-104 (headroom $7,736 = 27bp), F-112 (~24% chance cost > $300k, ASSUMPTION), F-005, F-007.
- **Evidence (new vs brief section 9):**
  - Event calendar (VERIFIED-PRIMARY unless noted):
    - FOMC Oct 27-28 and Dec 8-9 (federalreserve.gov calendar).
    - Treasury refunding announcement Nov 4 (treasury.gov, sb0590).
    - Midterms Nov 3 (SNIPPET-UNVERIFIED as a date; widely known).
    - CR expiry Dec 11 (cra.org, secondary; SNIPPET for congress.gov).
    - A possible lame-duck debt-limit vote (NTU, quoting Sen. Thune; PARAPHRASE-UNVERIFIED for Thune's own words).
    - Oil: Brent $114.89 on 9/22, peak $138.21 on 4/7 (FRED DCOILBRENTEU, VERIFIED-PRIMARY).
  - The 2y (4.87% on 9/24, FRED DGS2) is ~100bp above the fed funds midpoint of 3.875%. The market expects further
    tightening.
  - SEP 2027 fed funds range: 3.1-4.4 (VERIFIED-PRIMARY). Some FOMC participants already see cuts.
  - CBO's Feb 2026 path (10y at 4.1% in 2026) shows what a "return to normal" looks like. It is ~107bp below today.
- **Hypothesis (guess):**
  - The most plausible >27bp rally is energy de-escalation (Hormuz reopening), a growth scare, or an equity crash.
    Every one of these would also show up in the news before January.
  - Because no one can forecast these, the rule should be mechanical: buy on arrival; longest rungs first; the shortfall
    comes from the 2028 deposit; and state the funded ratio on the purchase date.
  - The IPS locks on Nov 6, before most of these events, so the rule must be written to survive them.
- **Would change:** the IPS purchase-rule sentence: a trigger stated as a ratio, not a date or forecast. Also the FR
  scenario table (a named "de-escalation rally" scenario at -50bp = $307,135, F-102).
- **North star:** she gets a rule she can follow without trusting anyone's rate forecast.

### Q03. What does "barring U.S. default" honestly cover? (seed 22)
- **Question:** "Default" has three layers: outright non-payment, a technical delay, and an inflation-driven
  "implicit" default. Which does the ladder cover, and which must the certainty definition name?
- **Anchors:** R-C47 "All ten payments must be funded by the investment portfolio with a high degree of certainty.";
  R-C54, R-C55.
- **Evidence:**
  - **Ratings:** Moody's downgraded the U.S. to Aa1 on May 16, 2025 (VERIFIED-PRIMARY, moodys.com). Moody's
    definition of a downgrade: the borrower is "relatively less likely to meet its debt obligations on time and in
    full" (VERIFIED-PRIMARY). S&P affirmed AA+ stable (Fortune, Jun 27, 2026, VERIFIED-PRIMARY on fortune.com,
    secondary report): "All three major ratings agencies have the US pegged one level below Triple-A with stable
    outlooks". S&P also warned the rating "could slip over the next two years if deficits increase" (paraphrase in
    the article).
  - **Technical delay:** late T-bill payments in April-May 1979 (Zivney & Marcus 1989; SNIPPET-UNVERIFIED, since
    taxpolicycenter.org refused with HTTP 403). The snippet reports that bill yields rose ~60bp afterwards.
  - **Market price of default:** U.S. 5y CDS ~36bp in week 37 of 2026 (MacroMicro snippet, SNIPPET-UNVERIFIED). This is
    a risk-neutral price. It is not a real-world probability.
  - **Implicit default:** see Q04.
- **Hypothesis (guess):**
  - Outright default is not covered, and cannot be covered by any USD plan.
  - Technical delay is largely covered by maturities that pay before the due date (Q06).
  - Implicit default is not covered, and falls on the residency's real budget (Q09).

  Checklist for the definition sentence:
  - "in nominal U.S. dollars";
  - "held to maturity";
  - that it rests on the U.S. Treasury paying on time;
  - that inflation risk to what $50k buys is disclosed, not hedged.
- **Would change:** the IPS certainty-definition sentence and the FR assumptions list (R-C56).
- **North star:** a statistics graduate will trust a definition that says exactly what it does not cover.

### Q04. Should Wharton's own budget model set the honest limit of "certain"? (seed 22)
- **Question:** Should the FR use the Penn Wharton Budget Model's June 2026 estimate to answer "how certain is
  certain" in real terms? It gives a 25% chance of reaching the U.S. debt outer bound within 14 years (~2040), and 25%
  by 2039 in its lower-openness case.
- **Anchors:** R-C56 ("identify the assumptions supporting their recommendation"), R-C85.
- **Evidence** (VERIFIED-PRIMARY, https://budgetmodel.wharton.upenn.edu/p/2026-06-02-when-does-federal-debt-reach-unsustainable-levels/,
  Smetters & He, dated June 4, 2026 on the page; quotes checked verbatim with `--grep`):
  - "Under historical excess cost growth in healthcare, this outer limit is likely reached within 20 years; there is a
    25% chance of reaching it in 14 years."
  - The bound is where "default of either explicit (Treasury) debt or implicit (pay-as-you-go) debt becomes a near
    certainty on a real (inflation-adjusted) basis."
  - Lower-openness sensitivity: "there is already a 25 percent chance of reaching the ceiling by 2039, just 13 years
    from now."
  - PWBM also says the calculation assumes capital is efficiently priced and that "a sudden devaluation (e.g., AI
    bubble burst)" would tighten the limit.
  - It is an outer bound, "not a forecast". Median closure years are 2045-2051.
- **Hypothesis (guess):**
  - Use it once in the FR as the reason the plan says "nominal" out loud. It should not be a headline.
  - Citing Wharton's own model shows research beyond the case, which matters for criterion 2.
  - Risk: over-dramatising. The sentence must say "outer bound, not a forecast".
- **Would change:** one FR assumption sentence and possibly one number (the 25%-by-~2040 tail as the named reason
  for an inflation stress case in Q09).
- **North star:** an honest limit, drawn from her own university's research, is more credible to Laura and to
  co-sponsors than "risk-free".

### Q05. The 2028 X-date: does the top-up rule need a debt-limit clause?
- **Question:** The debt limit is projected to bind around May 2027, with an X-date around Feb 2028 and a need to act
  "by January 1, 2028". Does the plan's 2028 step (deposit arrives; buy any missing long rungs) need a clause for a
  debt-limit standoff at that exact time?
- **Anchors:** F-601 ($150,000 at the beginning of 2028), R-C77.
- **Evidence:**
  - NTU (Aug 20, 2026; VERIFIED-PRIMARY on ntu.org; think-tank analysis, not official): "The X-Date is likely to be
    reached in February 2028"; "Congress would likely need to increase the debt limit by January 1, 2028"; headroom
    "under $1.4 trillion ... as of August 10, 2026"; the limit was raised to $41.104 trillion on July 4, 2025.
  - Time (Sept 23, 2026) headline: "A Debt Ceiling Fight Looms in 2027" (SNIPPET-UNVERIFIED; the page returned
    HTTP 406).
  - 2028-01-01 is a Saturday (derived).
- **Hypothesis (guess):**
  - Mostly a non-issue for STRIPS maturing 2032-2041, since X-date risk sits in bills maturing near the X-date.
  - The 2028 cash, if parked in T-bills while waiting, should avoid bills maturing in the X-date window.
  - Long yields in past standoffs often fell (flight to quality), which would make the top-up dearer (ASSUMPTION;
    needs 2011/2023 data).
  - Probably one FR line, not an IPS rule.
- **Would change:** an FR operating rule (where 2028 cash waits; buy long rungs promptly).
- **North star:** shows we checked the real 2027-28 calendar against her cash-flow dates.

### Q06. Do early maturities buffer a technical delay? (seed 22)
- **Question:** The reserve's Nov-15 maturities pay ~47 days before each Jan-1 payment (S1 file). Do they also act
  as a buffer against a technical Treasury payment delay? Should that be the stated reason to prefer them over
  instruments that pay on or after Jan 1?
- **Anchors:** R-C45 ("one at the beginning of each year from 2033 through 2042"), R-C47.
- **Evidence:**
  - S1 found the STRIPS ladder costs $2,124 more because the cash arrives early (`wins_now/S1_treasury_sleeve.md`,
    VERIFIED-PRIMARY inputs).
  - 2033-01-01 is a Saturday, so the first payment date is not a business day (derived).
  - 1979 delays lasted days to weeks (SNIPPET-UNVERIFIED).
- **Hypothesis (guess):** Yes, and it is nearly free. The 47-day lead turns "early cash" from a $2k cost into a
  control against both the non-business-day problem and a short technical delay. It fits the operational-risk gap
  flagged in BS-18.
- **Would change:** the maturity-choice decision (Nov 15 vs Dec funds vs Feb 15) and one FR line.
- **North star:** her operators get paid on time even if Washington is late.

### Q07. What does the plan do after another downgrade?
- **Question:** If an agency cuts the U.S. again (for example to AA), what will the plan do, and should the IPS
  pre-commit to "no forced selling of held-to-maturity Treasuries on a rating change"?
- **Anchors:** R-C89 ("formally establishes the strategy and the team's decision-making framework"), R-I10.
- **Evidence:** S&P says the rating could slip "over the next two years if deficits increase" (Fortune, Jun 27,
  2026). CBO's baseline deficit is 5.8% of GDP in 2026, rising to 6.7% by 2036 (SNIPPET-UNVERIFIED; cbo.gov 403;
  CRFB summary read, secondary).
- **Hypothesis (guess):**
  - A downgrade changes none of the ladder's cash flows. Selling would turn a headline into a real loss.
  - One clause of pre-commitment shows decision discipline, and it costs ~15 words.
  - Private-banker coaching logic (seed 27) applies here.
- **Would change:** an IPS decision-rule clause (or leave it to the FR if words are short).
- **North star:** Laura sees we will not panic on her behalf.

### Q08. How many IPS words should sovereign risk get?
- **Question:** Every U.S.-dollar plan from every rival shares the Treasury as its floor of certainty. Should the
  IPS spend one clause on sovereign risk and use the saved words on risks the ladder does not cover (inflation, TWD,
  operations)?
- **Anchors:** R-I18 (500-word maximum), R-C54.
- **Evidence:** INTERPRETATION. Bank deposits above the insured limit are riskier than Treasuries. Deposit insurance
  itself relies on the U.S. government. Ratings: sovereign AA+/Aa1/AA+ (Q03).
- **Hypothesis (guess):** Yes: one clause in the IPS, one paragraph in the FR. Most teams will either ignore the
  risk or over-dramatise it.
- **Would change:** the IPS word budget.
- **North star:** clear priorities read as judgement, not jargon.

### Q09. Who bears inflation's erosion of the fixed $50k? (seed 23)
- **Question:** What is the real value of the ten payments at the market's own inflation price (breakeven), and at
  one named stress case? Who bears the gap: the residency, co-sponsors, or Laura's flexibility money?
- **Anchors:** R-C46 ("each payment is a fixed $50,000 and is not adjusted for inflation"), R-C85, R-C44
  ("operating support beyond Laura's commitment, may come from co-sponsors, grants ...").
- **Evidence** (derived, section 5; inflation rates are ASSUMPTIONS except the breakeven, which is VERIFIED-PRIMARY):

  | U.S. inflation a year | 2033 payment in 2026 $ | 2042 payment in 2026 $ | Ten payments in 2026 $ |
  |---|---|---|---|
  | 2.34% (10y breakeven, 9/25) | 42,526 | 34,534 | 384,066 |
  | 3.7% (Fed 2026 PCE median, stress) | 38,772 | 27,958 | 331,037 |
  | 5.0% | 35,534 | 22,906 | 288,104 |
  | 7.0% (≈ worst post-war 16-year U.S. CPI rate, 7.12% to 1982) | 31,137 | 16,937 | 234,005 |

  The worst rolling 16-year CPI rate (7.12%/yr) and 10-year rate (8.84%/yr), both ending 1982, come from FRED
  CPIAUCSL (derived). Headline CPI is 3.71% y/y (Aug 2026) but core CPI only 2.76% (derived, FRED), so the energy
  shock drives the gap.
- **Hypothesis (guess):**
  - The residency bears it by design: the payment is fixed, and co-sponsors may fund operating support beyond
    Laura's commitment.
  - The plan's honest move is to state the real value at market breakeven, plus one stress, and say who covers the
    gap.
  - F-114 already has 2.0/2.5/3.7%. New here: the market-implied rate and a historically grounded worst case.
- **Would change:** the FR inflation-assumption numbers (R-C85) and one co-sponsor-draft fact.
- **North star:** she sees we told her what $50k will really buy in 2042.

### Q10. Is high inflation the base case or the stress case?
- **Question:** Does the 2026 evidence support treating 1970s-style inflation as a stress, not a base case, for
  2033-2042?
  - Fed independence was upheld in *Trump v. Cook* (June 29, 2026).
  - The FOMC hiked 12-0 and wrote "The Committee will deliver price stability."
  - The 5y5y forward inflation rate is anchored at 2.34%.
  - Against that: Kevin Warsh was confirmed in the most partisan chair vote on record.
- **Anchors:** R-C85, F-007, F-009.
- **Evidence:**
  - FOMC statement 2026-09-16 (VERIFIED-PRIMARY; quote checked).
  - *Trump v. Cook*, decided June 29, 2026; "The Government's application is denied" (VERIFIED-PRIMARY,
    supremecourt.gov PDF). News reports a 5-4 vote and for-cause protections upheld (SNIPPET-UNVERIFIED).
  - Warsh confirmed 54-45 on May 13, 2026 (SNIPPET-UNVERIFIED, CNN/CNBC). The Fed press release of May 15, 2026
    names Powell chair pro tempore "until Kevin M. Warsh is sworn in" (VERIFIED-PRIMARY).
  - 5y5y (T5YIFR) 2.34% on 9/25; its 2026 range was 2.05-2.36 (FRED, VERIFIED-PRIMARY).
  - SEP longer-run PCE 2.0% (F-007).
- **Hypothesis (guess):** Market and institutional evidence says stress, not base. PWBM (Q04) says the tail is real
  and lies inside the window. Recommended framing: base = market breakeven; stress = one named high-inflation path.
- **Would change:** the FR assumption sentence and the choice of stress rate in Q09.
- **North star:** balanced, sourced realism instead of doom or complacency.

### Q11. Is the flexibility money the inflation buffer? (seed 23; NEW angle, not a re-ask of settled item 8.10)
- **Question:** Should the post-2033 flexibility money be named as the buffer that lets Laura top up the operating
  budget if inflation erodes it? And should part of it sit in TIPS? The reserve stays nominal: brief 8.10 is not
  reopened.
- **Anchors:** R-C58 ("committing all remaining assets could limit her financial flexibility as the project
  develops"), R-C84, R-C44.
- **Evidence:**
  - TIPS real par yields: 5Y 2.64%, 7Y 2.73%, 10Y 2.83% (F-008).
  - A top-up to the operating budget is voluntary, since only the $50k is committed (R-C45).
  - Brief 8.10 says TIPS are not the core hedge because the liability is nominal. That still holds for the reserve.
- **Hypothesis (guess):**
  - Possibly yes, as a principle ("flexibility money is partly real-return protected") rather than a sized fund. The
    case says teams need not size a contingency fund (R-C61).
  - Complexity test: it must fit in one FR sentence, or drop it.
- **Would change:** the decision on the composition of flexibility money, plus one FR sentence.
- **North star:** it answers the question a co-sponsor will ask ("what if $50k is not enough in 2040?") without
  touching the promise.

### Q12. Which return assumptions are "reasonable" when forecasters lag the market?
- **Question:** JPM (set when the 10y was 4.16%) and CBO (10y 4.1% for 2026) both sit ~100bp below today's yields.
  Should projections take sleeve bond returns from today's market yields and cite JPM only for equities, or wait for
  the 2027 LTCMA?
- **Anchors:** R-C77 ("use reasonable return assumptions consistent with their strategy"), F-010, F-317.
- **Evidence:**
  - IEF YTM 5.17%, TLT 5.54% (F-203, F-204).
  - JPM intermediate Treasuries 4.00% (F-307).
  - CBO 10y 4.1% (2026) and 4.4% (2031-35) (SNIPPET-UNVERIFIED via CRFB).
  - The 2027 JPM LTCMA is not yet out (F-315). Last year's edition came out ~Oct 20, which is before the IPS.
- **Hypothesis (guess):**
  - Use market yields for bonds (a held bond's return is roughly its yield) and JPM for equities. Say so in one line.
  - Mixing sources needs one sentence of justification.
  - This likely raises the sleeve's median and the 2031 floor slightly (F-317: ~1pp/yr on the bond part).
- **Would change:** the projection inputs; the 2031 range and facility numbers (FR); one IPS phrase on assumptions.
- **North star:** assumptions tied to prices she can check, not to a stale forecast.

### Q13. Does 60% sleeve equity still earn its p5 cost? (extends open item 9, with NEW evidence)
- **Question:** At today's yields, JPM's 6.70% equity return beats a ~5.0% 6-year Treasury by only ~1.7pp, and the
  S&P 500 CAPE is ~41. Does 60% sleeve equity still earn its downside cost, or is 40-50% the "thoughtful risk"
  answer?
- **Anchors:** R-C38 ("recommend an appropriate balance between pursuing growth and protecting the capital required
  for her goals"), F-301, F-407.
- **Evidence:**
  - CAPE 41.48 (multpl.com, read on page; secondary data site; mean 17.42).
  - Forward P/E 19.32 on 9/24 (StreetStats snippet, SNIPPET-UNVERIFIED). That is an earnings yield of ~5.2%, roughly
    equal to the 10y nominal.
  - S&P 500 7,743 on 9/25, +17.2% over 1y, record 7,799 on 8/13 (FRED SP500, VERIFIED-PRIMARY).
  - Brief 8.5: more sleeve equity buys range, not median. New here: at today's yields, the expected premium itself
    is thin.
  - Rough arithmetic (ASSUMPTION): moving 20% of a ~$158k sleeve from equity to bonds for ~5 years at a 1.7pp
    premium costs ~$2-3k of median wealth.
- **Hypothesis (guess):** 50% may be the better-balanced number, with a small median cost and a better p5. But
  complexity and consistency with WInS matter more than 10pp either way. Phase D should re-run `strategy_mc.py` with
  bond returns at market yields.
- **Would change:** the sleeve equity % (IPS) and the 2031 range (FR).
- **North star:** "thoughtful risk" means taking equity risk only where it is paid.

### Q14. Should risk be stressed at a positive stock-bond correlation? (extends open item 9, with NEW evidence)
- **Question:** In 2026, stocks and Treasury prices fell together (daily corr(S&P return, Δ10y) = -0.44). Should the
  sleeve's p5 and the 2031 range be stressed at a positive stock-bond return correlation instead of JPM's ~0?
- **Anchors:** F-314 (JPM large cap vs intermediate Treasuries -0.01), R-S26.
- **Evidence:** 2024 -0.06, 2025 +0.14, 2026 -0.44, since June 2026 -0.48 (FRED SP500 and DGS10, derived). A negative
  number here means stocks fell when yields rose, i.e. both fell together.
- **Hypothesis (guess):**
  - A +0.3 to +0.4 stress lowers the sleeve's p5 by a few thousand dollars. The ladder is unaffected, because it is
    held to maturity.
  - WInS: the equity and Treasury holdings will fall together on inflation news. Expect it, and do not "fix" it by
    trading.
- **Would change:** the FR sleeve p5 and 2031 range numbers; the WInS expectation-setting note.
- **North star:** we tested the plan against the market she actually lives in.

### Q15. Should the team pre-commit not to trade around the big October-November events?
- **Question:** Should the team state in a trade note, before the fact, that the Treasury hedge will not be traded
  around the Oct 28 FOMC or the Nov 4 refunding? Then any mark-to-market loss becomes evidence that the strategy was
  "tested", not a regret.
- **Anchors:** R-T9 ("how it aligned with, tested, or refined your overall investment strategy"), R-W73 ("does not
  require frequent or same-day trading"), R-W76.
- **Evidence:** FOMC Oct 27-28 (no new projections; the next SEP is Dec 9) and refunding Nov 4 both fall inside the
  WInS window (VERIFIED-PRIMARY). TLT sits at its 52-week low (F-204).
- **Hypothesis (guess):** Yes. It costs nothing and gives a ready "tested" note. The day-trading ban also argues for
  holding (brief section 14).
- **Would change:** a WInS conduct decision and the choice of the three notes.
- **North star:** she sees discipline under pressure, the behaviour she is hiring for.

### Q16. Should each Treasury note record the day's funded ratio?
- **Question:** Should every WInS Treasury trade note record that day's ladder cost and funded ratio? The three
  notes would then show a live, dated test of the strategy.
- **Anchors:** R-T9, F-111 (ladder > $300k on 173 of 185 days), F-117 (1.026).
- **Evidence:** The ladder was above $300k for most of 2026 and below it only since Sept 10 (F-111). A note written
  at trade time is permanent (brief section 14).
- **Hypothesis (guess):** Yes, as one number per note, from the treasury.gov curve run through `official_curve_pv.py`.
  It is the simplest quantitative thread linking the TN, IPS and FR.
- **Would change:** the format of the trade notes (WInS-now) and the TN reflections.
- **North star:** one number Laura could track herself, since she is a statistics graduate.

### Q17. Is the 10-20 year sector the cheapest place for Laura's long rungs?
- **Question:** The 20y par yield (5.54%) is above the 30y (5.49%). Does that make the 10-20y sector the cheapest
  point on the curve for the 2037-2042 rungs? Does it add a price reason, not only a matching reason, to S1's
  IEF+TLH hedge?
- **Anchors:** F-001, F-107 (2037-42 rungs cost $155,408).
- **Evidence:** 20Y 5.54 vs 30Y 5.49 on 9/25 (F-001, VERIFIED-REPO-FILE). S1 recommends IEF+TLH on matching grounds
  (PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK).
- **Hypothesis (guess):** Yes. The 20y sector has traded cheap (higher yield) since the 20y bond was re-introduced
  (SNIPPET-level knowledge; verify with the treasury.gov history). Laura's long rungs fall exactly there.
- **Would change:** the instrument decision (supports TLH-type exposure) and a TN reason.
- **North star:** her money buys the promise at the best available price.

### Q18. Should WInS hold individual Treasuries, not only ETFs?
- **Question:** WInS permits "Any Government/Treasury Bonds ... available on WInS" at $10 a trade. Should the WInS
  book buy one or more individual Treasuries maturing Nov 2032-Nov 2041? That would show a locked yield (a ladder)
  rather than only constant-maturity ETFs, whose yield never locks.
- **Anchors:** F-606 ("Any Government/Treasury Bonds from any exchange available on WInS"), F-607, R-C75.
- **Evidence:** permitted type VERIFIED-PRIMARY; which issues are listed is UNVERIFIED (logged-in check). An ETF's
  duration and yield drift (F-205), while an individual bond's yield to maturity is fixed at purchase.
- **Hypothesis (guess):** Yes, if WInS lists them: one or two individual bonds, as a "demonstration rung". The trade
  note is then literally the strategy. Check the position limit and the 2x-daily-volume rule for bonds.
- **Would change:** the WInS instrument decision; Trading Note choice.
- **North star:** the WInS book shows her the ladder itself, not a proxy.

### Q19. Is a 2027 recession the common cause of the joint tail? (extends unanswered open item)
- **Question:** Is a 2027 U.S. recession the common cause that both lowers yields (dearer long rungs) and shrinks the
  2028 deposit (advances, speaking)? If so, how large is the joint tail?
- **Anchors:** R-C86, F-403, F-404.
- **Evidence:** needs data. The 10y fell sharply in 2001, 2008 and 2020 (FRED DGS10, known pattern; not computed
  here). Publishing and speaking income in recessions: no source found yet.
- **Hypothesis (guess):**
  - Yes, the recession link is plausible.
  - Lock-early limits the damage: only rungs not yet bought are exposed. In January 2027, with a 27bp cushion, that
    is none unless rates fall first.
  - The joint tail is Jan 2027 rally + 2028 deposit cut. Up to ~$23-33k is unfunded (brief section 9, unverified).
    Phase D should price it with a scenario, not a correlation guess.
- **Would change:** the FR joint-tail row, and whether the 2031 floor must hold back money for unfunded rungs.
- **North star:** we tested the one scenario where her income and her markets fail together.

### Q20. What does an AI-equity crash do to Treasuries and to Laura?
- **Question:** How does an AI-equity crash feed into Treasury yields and the January 2027 cushion, and which way does
  it cut for Laura?
- **Anchors:** R-C82 ("how investment uncertainty could affect both the operating commitment and the facility
  contribution"), F-111.
- **Evidence:**
  - Top 10 ≈ 38-41% of the S&P 500 (SNIPPET-UNVERIFIED).
  - PWBM: "a sudden devaluation (e.g., AI bubble burst)" tightens U.S. debt capacity (VERIFIED-PRIMARY).
  - The 2026 correlation regime (Q14).
- **Hypothesis (guess):**
  - Before Jan 2027: a crash probably lowers yields (flight to quality), so the ladder gets dearer. Laura holds cash,
    not stocks, so her only exposure is the cushion.
  - After 2027: a crash hits only the sleeve, while the ladder's market value rises (a good hedge).
  - Long run: a crash worsens fiscal capacity (PWBM), which argues for "nominal" honesty.
- **Would change:** one FR scenario sentence; possibly the IPS "buy on arrival" rationale.
- **North star:** she sees how her promise behaves in the scenario everyone fears in 2026.

### Q21. Is the sleeve doubling Laura's Taiwan bet? (seed 24; sleeve decision; open item "EWT keep or drop")
- **Question:** A cap-weighted U.S. index is heavy in AI firms that depend on Taiwan chip supply, and the residency is
  in Taiwan. Should the sleeve deliberately avoid adding Taiwan exposure (drop any Taiwan tilt; consider broader or
  global equity)?
- **Anchors:** R-C39 ("In 2033, Laura plans to establish a collaborative creative residency in Taiwan."); R-S24 ("uses
  appropriate diversification"); R-W71 (diversification by "funding purposes").
- **Evidence:**
  - Taiwan's defence ministry (Sept 2026) says PLA drills focus on blockade (SNIPPET-UNVERIFIED, Taiwan News /
    Seoul Economic Daily).
  - Taiwan real GDP forecast +11.05% in 2026 on the AI boom (F-504).
  - Index concentration (Q20).
- **Hypothesis (guess):**
  - Drop the Taiwan tilt. The project already carries Taiwan risk. The case gives no reason for identity-based
    tilts, and brief section 4 bans tokenism.
  - A global or broad index lowers AI concentration (D2 to size).
- **Would change:** the sleeve index decision (IPS; WInS-now).
- **North star:** her portfolio does not bet twice on the place her dream already depends on.

### Q22. Measured in dollars, how fast have Taiwan construction costs risen? (seed 25)
- **Question:** Measured in U.S. dollars (Laura's currency), how fast have Taiwan construction costs risen? Does that
  change how the FR explains "the effect of inflation on ... facility costs"?
- **Anchors:** R-C85 ("the effect of inflation on portfolio projections and facility costs"), F-508, F-512.
- **Evidence** (derived; inputs VERIFIED-PRIMARY):
  - CCI Aug 2026 +6.53% y/y in TWD (F-508).
  - USD/TWD monthly averages: Aug 2025 30.154, Aug 2026 32.023, 2021 average 27.937 (FRED DEXTAUS).
  - Result: USD-measured CCI **+0.31% y/y**. Since the 2021 base: **3.57%/yr in TWD** less **2.72%/yr TWD
    depreciation**, which gives **+0.82%/yr in USD**.
  - ASSUMPTION: monthly-average FX is matched to the monthly index, and the 2021 annual average is the base.
- **Hypothesis (guess):**
  - The headline "costs up 6.5%" overstates the pressure on a USD contribution.
  - But the offset depends on the TWD staying weak. A TWD rebound, e.g. the Fed cutting while the CBC holds (F-515),
    would reverse it.
  - A strong FR sentence contains: both currencies, the offset, and the reversal risk.
  - This refines brief 8.15; it does not contradict it.
- **Would change:** the FR facility-inflation sentence and numbers; the co-sponsor range explanation.
- **North star:** co-sponsors in Taiwan and a USD donor both see their own number.

### Q23. Will Taiwan's 2026 construction-cost jump fade before 2033? (seed 25)
- **Question:** Is the 2026 jump an AI-boom wage spike that will fade before 2033, or a new trend?
- **Anchors:** F-508 (wage class +8.12% y/y; the index was flat in 2024-25), F-504, R-C94 ("The total cost of the
  facility has not been determined.").
- **Evidence:** Taiwan real GDP 2026 +11.05% (F-504). The energy shock (F-517) and Hormuz (Q02) raise material costs.
  Taiwan imports most of its energy (general knowledge; not verified here).
- **Hypothesis (guess):** A mix: the wage pressure from fab construction may persist while AI capex lasts, and energy
  may fade. Use the since-2021 rate (~3.5%/yr in TWD) as the base, not the 2026 spike.
- **Would change:** the facility-inflation assumption number (FR).
- **North star:** realistic, sourced facility expectations protect her credibility.

### Q24. What happens to the payments if the residency cannot operate in Taiwan? (seed 24)
- **Question:** If a blockade or quarantine stops the residency operating in Taiwan, is the USD Treasury reserve
  portable? Should the plan tie the promise to the residency's operating expenses rather than to the place?
- **Anchors:** R-C39; R-C45 ("toward the residency's operating expenses"); R-C48.
- **Evidence:** The case promises payments to the residency's operating expenses; it does not name a Taiwan bank or
  currency (R-AN10). Treasuries are held in USD and can be paid anywhere.
- **Hypothesis (guess):** The reserve is location-agnostic by construction, which is a strength worth one FR line. A
  relocation plan is out of scope (Taiwan legal issues are excluded, R-C97). Do not dramatise.
- **Would change:** one FR sentence; the co-sponsor draft (what happens in a disruption).
- **North star:** her promise survives even the worst geopolitical case, calmly stated.

### Parked (logged; failed the "would it change something" filter)
- 2031 2y yield uncertainty for the floor growth factor (±~$5k; F-013 already labels it an ASSUMPTION).
- Treasury auction-size changes "in early 2027" (Yahoo snippet): no decision depends on it.
- U.S. dollar broad index: -8.1% from its Jan 2025 high but flat over 1y (FRED DTWEXBGS). It matters only through
  TWD (Q22).
- Investment-grade credit spreads 0.79% (FRED BAMLC0A0CM): calm. The stress is in rates, not credit. No plan change.

---

## 4. Sources (all accessed 2026-09-27 from this container)

**Primary (read on the page; VERIFIED-PRIMARY)**
- FOMC statement 2026-09-16: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm (quote
  "The Committee will deliver price stability." checked verbatim).
- SEP tables 2026-09-16 (June comparison rows): https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm
  - Fed funds medians 4.1/4.1/3.9/3.6/LR 3.2 (June: 3.8/3.6/3.4/LR 3.1).
  - 2027 range 3.1-4.4.
  - PCE 2026 range 2.9-3.8.
- FOMC calendar: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm (Oct 27-28; Dec 8-9 with SEP).
- Fed press release 2026-05-15 (Powell chair pro tempore pending Warsh): https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm
- Treasury quarterly refunding statement Aug 5, 2026: https://home.treasury.gov/news/press-releases/sb0590 (sizes
  steady "for at least the next several quarters"; next announcement Nov 4, 2026).
- Moody's U.S. rating page: https://www.moodys.com/web/en/us/about-us/usrating.html (downgrade to Aa1, May 16, 2025;
  downgrade definition quote checked).
- Supreme Court, *Trump v. Cook*, No. 25A312, decided June 29, 2026: https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf
- Penn Wharton Budget Model, "When Does Federal Debt Reach Unsustainable Levels? Spring 2026 - Onward", Smetters &
  He, June 4, 2026: https://budgetmodel.wharton.upenn.edu/p/2026-06-02-when-does-federal-debt-reach-unsustainable-levels/
  (three quotes checked verbatim).
- PWBM, "Supreme Court Tariff Ruling: IEEPA Revenue and Potential Refunds", Feb 20, 2026: https://budgetmodel.wharton.upenn.edu/p/2026-02-20-supreme-court-tariff-ruling/
  (6-3 ruling; up to $175bn refunds).
- FRED CSVs (https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES): THREEFYTP10, DFII10, T10YIE, T5YIFR,
  DGS2, DGS10, DGS30, SP500, DTWEXBGS, DEXTAUS, CPIAUCSL, CPILFESL, PCEPILFE, DFEDTARU, DCOILBRENTEU, BAMLC0A0CM.

**Secondary but read on the page** (the claim is the author's, not official):
- National Taxpayers Union, "Projecting the Debt Limit", Aug 20, 2026: https://www.ntu.org/publications/detail/projecting-the-debt-limit
  (quotes checked verbatim).
- Fortune, "S&P keeps U.S. sovereign rating at AA+ with stable outlook", Jun 27, 2026: https://fortune.com/2026/06/27/sp-global-us-sovereign-credit-rating-aa-stable-outlook-debt-deficits/
- CRFB summary of CBO Feb 2026 outlook: https://www.crfb.org/papers/cbos-february-2026-budget-and-economic-outlook
- CRA government-affairs blog on the FY27 CR (to Dec 11): https://cra.org/govaffairs/blog/2026/09/fy2027-sept-update/
- multpl.com Shiller PE (41.48; mean 17.42): https://www.multpl.com/shiller-pe

**Blocked or refused (not read; nothing inferred from them)**
- cbo.gov publication page and PDF (HTTP 403).
- bipartisanpolicy.org (403).
- congress.gov CRS (403).
- time.com (406).
- taxpolicycenter.org (403).
- streetstats.finance (no text returned).

**SNIPPET-UNVERIFIED (search results only)**
- Warsh confirmed 54-45 on May 13, 2026 (CNN, CNBC).
- *Trump v. Cook* 5-4 majority details.
- U.S. 5y CDS ~36bp (MacroMicro).
- Forward P/E 19.32 (StreetStats).
- S&P 500 top-10 ≈ 38-41% (various).
- Iran war since Feb 28, 2026, and Hormuz closure (Wikipedia, World Bank blog titles).
- PLA blockade focus (Taiwan News, Sept 3, 2026).
- 1979 T-bill delays (+~60bp; Zivney & Marcus 1989).
- Treasury auction sizes expected to change early 2027 (Yahoo).

---

## 5. How the derived numbers were made (re-runnable)

1. Download the FRED CSVs listed above with `curl -sSL "https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES"`.
2. Yield decomposition (Q01): values of DGS10, DFII10, T10YIE and THREEFYTP10 on or before each date. The "last
   time" checks find the latest earlier date with a value at or above today's.
3. Correlation (Q14): daily `SP500.pct_change()` against daily `DGS10.diff()`, aligned on common dates, by calendar
   year.
4. Real value (Q09): `50000/(1+i)**(year-2026)`. Worst rolling U.S. CPI: `(CPI_t/CPI_{t-12k})**(1/k)-1` for k = 10
   and 16 years.
5. USD construction cost (Q22): `CCI/FX` with the monthly-average DEXTAUS. CCI Aug 2025 = 119.50/1.0653 (F-508).
   Base 2021 = 100 against the 2021 average FX. Period length 5.08 years (mid-2021 to Aug 2026).

These were run inline in the scratchpad. Phase D should save a script under `research/insight_v1/scripts/` before
any number goes into a deliverable.

---

## 6. Leads for the specialists

**D1 (rates and fixed income)**
- Use the FRED decomposition (Q01) as the "why now" fact base. Add NY Fed ACM term premium as a second estimate
  (newyorkfed.org, not tried).
- Price the event calendar (Q02): the ladder cost at -25/-50bp is already in F-102.
- Q03-Q07 need one table: layer of default → covered? → control → words used.
- Check the 20y "hump" history on treasury.gov (Q17).
- Price the 2028 X-date: find 2011 and 2023 10y/30y moves around the X-dates (FRED DGS10/DGS30).
- CBO's current outlook: try the CBO data page via another route, or the CBO GitHub data (not tried). The Aug/Sept
  2026 CBO update, if any, was not found.

**D2 (equity and AI concentration)**
- Get primary index weights: S&P DJI fact sheet or an iShares IVV holdings CSV, the same method as S2. Get the
  earnings yield from a primary source.
- PWBM's "AI bubble burst" line links AI to fiscal capacity (Q20).

**D3 (quant)**
- Re-run `strategy_mc.py` with sleeve bonds at market yields (~5.0%) and a stock-bond return correlation of +0.3/+0.4
  (Q12-Q14).
- Build the joint-tail scenario (Q19).

**D4 (Taiwan, FX, geopolitics)**
- Q22 is the headline: repeat it with DGBAS monthly CCI levels via `A2_taiwan_cci.py`, not the y/y ratio.
- Test windows (1y, 3y, since 2021) and the reversal case (TWD at 28-29 as in 2021).
- Check Taiwan's energy import share on a primary page (Bureau of Energy).

**D6 / D9**
- Q07, Q08, Q15 and Q16 are pre-commitment and communication choices. Each should fit in ≤15 words of IPS or one TN
  line.

**D10**
- Q18 needs the logged-in WInS check: are individual U.S. Treasuries listed, and do bonds count toward the position
  limit?

**D7**
- Citing the Penn Wharton Budget Model (Q04) in a Wharton competition is unusual. Check whether past winners cited
  Wharton research.

---

## What this teaches

A yield is not one number. It is a stack: what the market expects the Fed to do, plus inflation expectations, plus
a term premium for lending long. In 2026 almost all of the rise came from the real part, not from inflation fears.
That tells you something useful: Laura was being paid well to lend long at exactly the moment her promise required
it.

"Risk-free" is also a stack. Treasuries are as safe as U.S. dollars get:
- in nominal terms, near certain;
- against a late payment, mostly protected if the money arrives early;
- against inflation, not protected at all.

The honest skill is to say which layer your plan covers and which it does not. Then back each claim with a primary
source you read yourself, whether that is the Fed's own statement, the Treasury's own schedule or Wharton's own
budget model.
