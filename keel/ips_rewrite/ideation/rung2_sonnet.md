AI-generated (Claude Code), rung 2 Sonnet, 26 Oct 2026. Not for submission. Ideation only; no IPS text beyond sample sentences.

# Rung 2 (deep): three seams under Caplet XR

Read first: `rung1_haiku.md`, `rung3_opus_pharmacology.md` (its F1-F19 fact table stands; I do not re-verify it), `../00_GROUND_TRUTH.md`,
`../THINKING_LOG.md` (A4, A5), `../research/R03_voice_study.md`. Grades: EXACT = the maths or mechanism is the same;
PARTIAL = one true structural point, then it breaks; STRETCH = kill. "Insight" = what it tells an investor that plain words do not.
Verification: **V** checked this run (web titles/standard textbooks), **T** textbook-standard, **U** UNVERIFIED, do not lean on it.

**Bottom line.** Pharmacology holds two exact identities and one excellent numerical coincidence; everything else is decor. Unbundling is
a real idea, but the pharmacist pun ("compounding") is too cute and carries a regulatory sting; keep the idea, drop the pun. For the R,
**redemption stays first**, with **runway** the one challenger worth a second look. Nothing here needs more than 3 motif words in the IPS.

---

## Seam 1. Pharmacokinetics / pharmaceutics against fixed income

### 1.1 Verdict table

| # | Pharma idea | Plan counterpart | Grade | Why / where it breaks |
|---|---|---|---|---|
| 1 | **Zero-order release** (constant amount per unit time, independent of what is left in the unit) | Ten equal fixed-dollar payments | **EXACT** | Zero-order: dM/dt = k0. The contrast is **first-order release** (rate proportional to what remains, dM/dt = -kM): that is a fixed-percentage withdrawal, whose cheques shrink with the balance and never reach zero. Breaks only in being lumpy (annual cheques, not a continuous flow). (T) |
| 2 | **Immediate release** vs lump sum | One bullet payment / all in 2033 | EXACT but empty | True by definition, carries no insight. Use only as the foil that defines ER (FDA: ER = at least twofold fewer doses, F1). |
| 3 | **Mean residence / dissolution time** vs **Macaulay duration** | Duration of the ten payments | **EXACT** | MRT = AUMC/AUC (first moment over zeroth) (V: standard statistical-moment analysis). Macaulay duration is the same ratio with the discounted cash flows as the "curve". Undiscounted it is literally mean dissolution time. Check: payments at t = 6..15 years (Jan 2027 to Jan 2033..2042) have mean time **10.5** years undiscounted, about **10.1** at a flat 5% (my calc; the repo's 9.90 uses the real curve). Discounting pulls the mean earlier. Pharmacy also has the **second moment** (variance of residence time) = the finance **dispersion** (M-squared). Here the variance is **8.25 years squared** (SD about 2.9 years), my calc. |
| 4 | **Dose dumping** vs selling early | Sell a holding before maturity | PARTIAL | Dumping releases the whole amount too fast, but you still receive all of it. A forced sale delivers a *different* amount (market price). Real point: Palladone failed on an **interaction with the environment** (alcohol), not on the tablet in isolation; the ladder's matching trigger is a cash need at the bad moment (forced seller). Rung 3 graded this EXACT; I downgrade it. |
| 5 | **"Do not crush"** vs no early sales | Held to maturity | PARTIAL | Exact in logic only: the claim holds for the *intact* unit (F2). But crushing changes only the timing, while an early sale changes the total. The closer bond act to crushing is **breaking the schedule** (rolling, rebalancing the ladder). |
| 6 | **Therapeutic window** (MEC to MTC) vs the 2031 range | Floor to top | PARTIAL | A real window is fixed by the drug and the body; ours is chosen. Better: the harm sits on the *promise*, not the outcome. Too low a promise gives no signal ("below MEC"); too high is the case's "damage her credibility". Cute number: top/floor = 170/145 = **1.17**, far under the FDA's narrow-index line of 2 (F8). That is a joke, not a finding: a narrow window is usually a bad thing, and ours is narrow by design of the floor. |
| 7 | **Loading dose / maintenance dose** vs 2027 / 2028 deposits | Fill the ladder on day one; 2028 tops up | PARTIAL, near STRETCH | Loading dose = target level x volume of distribution, i.e. the present value of the whole liability, bought at once. True and neat. But maintenance doses replace *elimination*; the 2028 deposit replaces nothing, it builds the floor. Real insight is only "buy the whole liability now, lock the rate, don't accumulate into it" (plain words do that). |
| 8 | **Spansule** graded coatings vs maturities | One holding per year | **EXACT** (construction) | Same engineering problem: approximate a flat rate from *discrete, individually simple, time-set units*; the delay is fixed at manufacture; flatness emerges from the set, no unit does anything clever (F9, F10). Breaks: beads overlap, rungs do not. |
| 9 | **Bioavailability** (F) vs fees | Net delivered / cash paid in | PARTIAL | F = fraction reaching circulation, measured on the **area** (total exposure), not the peak. So fees belong on the area: a 1% annual drag over 15 years removes about 14% of the area ((0.99)^15 = 0.86). Plain words ("net of fees, over the life") carry it. |
| 10 | **Bioequivalence 80-125%** vs index tracking | iBonds / VT as generic | PARTIAL (mapping), **EXACT** (the number) | See finding 3: the band is log-symmetric, 0.8 x 1.25 = 1. And the test is on a **90% confidence interval**, not the point estimate (F12). No such band exists for ETFs. |
| 11 | **Half-life** | -- | STRETCH, killed | Half-life is a first-order idea; the ladder is zero-order, whose "half-life" depends on the starting amount. The only live use is the contrast in finding 1. |
| 12 | **Flip-flop kinetics** (release rate, not elimination, controls the curve) | -- | STRETCH, killed | Interesting (the release schedule is the boss) but nothing in the plan eliminates. |

### 1.2 The 3 best findings

**F-A. Zero-order against first-order is the difference between "fixed dollars" and "fixed percent" (EXACT).**
Laura asked for ten $50,000 cheques. A portfolio that pays a percentage of what is left (the family of the 4% rule) is first-order:
the cheque falls when the market falls, and there is always something left, so the stream never has a definite end. A ladder is zero-order:
each cheque is independent of the reservoir. Investing insight: **payment certainty is a property of the release law, not of how much you hold**.
A reservoir that is twice as big under a first-order law still fails Laura's test. Plain words say "fixed dollars", but the pairing
explains why a larger, riskier pot cannot buy what a dedicated holding buys. Where used: IPS, one clause, no jargon; Final Report, the two laws side by side.

**F-B. Duration is a first moment; the second moment is why a duration match is not a funding match (EXACT).**
AUMC/AUC is the cash-weighted mean time; the variance is the cash-weighted spread. Matching the mean (what IEF/TLT did in the early council
work) leaves the spread free, so a barbell and the ladder with the same 10-year centre behave differently when the curve twists.
The ladder's spread equals the liability's spread by construction. This is the real finance content behind "dedicate, don't just duration-match"
(Redington's third condition, M-squared). Plain words ("matching the average is not matching the schedule") say it, but the moment language
makes it checkable: 10.5 years centre, 2.9 years spread. Final Report only; the IPS has no room.

**F-C. The bioequivalence band is a rule about an interval, set in advance, and it is log-symmetric (numerically EXACT, mapping PARTIAL).**
Three points in one: (i) a generic passes only if the **whole 90% confidence interval** of exposure lies inside 80-125%, not its midpoint;
(ii) the band is fixed **before** the data (pre-registration, F15); (iii) 80% and 125% are reciprocals, 0.8 x 1.25 = 1, so the band is symmetric in logs.
Investing insight: **the same arithmetic as drawdown**: -20% needs +25% to get back, which is why a floor protects more than a symmetric
percentage band looks as if it should. And on the 2031 range: the case asks for "a range with a confidence"; the clean standard is
*state the interval, with its confidence, against a limit you named before you looked*. Our range (p5 to p95, so 90%, MODEL) is that object.
Use: Final Report, one paragraph; the log-symmetry line is a Ray-style aside, if the team likes it.

Honourable: F-D, Spansule's "no unit does anything clever" (row 8) is the cleanest bridge into Seam 2.

### 1.3 Sample sentences (AI DRAFT, at most 3)

1. "Pay a fixed share of the pot and the cheques shrink with the market; pay a fixed 50,000 and they cannot." (zero- against first-order, no jargon)
2. "Matching the average date of the payments is not matching their schedule: ten dates, ten holdings." (moments, no jargon)
3. (Final Report aside) "A drop of 20% needs a rise of 25% to undo; the generics regulator's 80-125% band is the same sum in reverse."

### 1.4 The case against Seam 1

- Every exact identity is a **well-known finance fact in other clothes**. A judge gets nothing from "the pharmacy calls it mean residence time". The value is a *new test or distinction* (F-A, F-B), and both could be written with no pharmacy word at all. That is the honest reading of "tool, not crutch".
- F-B and F-C are **Final Report material**; the IPS (500 words, no calculations) has no room, so the seam may buy nothing in the document that is scored first.
- Rows 4 to 7 look like fits and are not; anyone who checks (a pharmacist judge, an actuary judge) will find the break point in seconds. Keep them out.
- Pharmacy words in a money document risk the "AI decorates" reading (rung 3 section 6). The identities help only if each is used once, with the plain version first.

---

## Seam 2. Unbundling, and the compounding pharmacist

### 2.1 Verdict table

| Bank / insurer product | What it really is | Plan's version | Grade | Notes |
|---|---|---|---|---|
| Ten years of fixed payments from 2033 | A **deferred income annuity with a period certain** (insurer): premium now, ten guaranteed payments starting in 6 years, regardless of life. "Annuity-certain" is the actuarial term. | Ten dated Treasury / iBond holdings | **EXACT** | Better than "10-year annuity-certain": say *deferred*, since payment 1 is 6 years out. Counterparty: the insurer. Plan's counterparty: the US Treasury. Insurer failure protection varies by state (U: not checked; do not quote a limit). |
| Floor plus capped share of stocks in 2031-2033 | A **principal-protected note** = zero-coupon bond + call option, issuer credit behind both. | Treasury floor + ETF; gift = floor + half the fund, capped | **EXACT** in shape, PARTIAL in method | Ours has **no option**: the upside is real stock exposure, not bought with the bond's interest. So it is "a capital-protected note minus the option", the thesis already on file. The bank's fee is hidden in the option price; the issuer's credit is the guarantee (the Lehman point is on the R04 fact-check queue; do not use it until it is checked). |
| "Target-date fund" (rung 1/A4) | Glide-path stock/bond fund that de-risks on a calendar | iBonds are **target-maturity** bond funds | **STRETCH** | A target-date fund *rebalances along a glide path*; the plan **never rebalances**. iBonds are target-*maturity*, a different product. Drop the third product, or replace it with a **defined-outcome (buffer) ETF**, which is the exchange-traded cousin of the protected note (U: confirm the product category before use). Honest count is **two products, not three**. |

### 2.2 Is "compounding pharmacist" clever or too cute?

- **Mechanism: fits.** A compounding pharmacist makes a medicine to one person's order when no commercial product suits (V: FDA page on pharmacy compounding). The justification is the same one the plan needs: **no off-the-shelf product fits Laura's three needs at once** (payments, a range in 2031, a reserve shape). That is the true core: the value is the *joint design*, not any one ingredient.
- **The word.** "Compound" in "compound interest" and in "compounding pharmacy" come from the same Latin root (*componere*, put together) (T). So it is not a homonym pun, it is a shared origin, which is better, but still a pun: the plan's own compounding is **reinvested coupons**, which is the plan's one live risk (rates falling). A "compounding" motif would put a spotlight on the weak joint.
- **The sting.** Compounded drugs are **not FDA-approved** (V: FDA). The implication "your plan is unapproved" is easy to draw; in the other direction the ingredients are as standard as they come (Treasuries, a registered ETF), which is a good defence but takes words. The 2012 New England Compounding Center meningitis outbreak is the first thing many people link to compounding (U: details unchecked; do not mention).
- **Verdict: too cute for the IPS, defensible as one Final Report aside.** The pharmacist adds no insight that "built from parts, sized to her case" lacks.

### 2.3 Better versions (ranked)

1. **Plain finance, no pharmacy: "unbundled".** It is already finance language (airline, telecom, software), and judges will read it once and move on. Keep the three-products list as two.
2. **The fixed-dose combination foil.** A bank sells a pill with the ratios locked (a fixed-dose combination, "polypill"); each part cannot be changed without the others. Laura's 2028 deposit is uncertain, so she needs a ratio that can move *after* she learns it (ladder sized first, floor second, stock last). The insight is **"the ratio is the product"**: it is the bundle's lock-in that costs, not its fee. Exact on the mechanism; a pharmacy word, but of the sort that earns its place (Final Report).
3. **"No off-the-shelf product fits"** as the argument, with no metaphor at all. This is the only version that survives a hostile reading.

### 2.4 The 3 best findings

- **U-A. Two products, not three, and name the first correctly.** "Deferred income annuity (period certain)" + "principal-protected note": these are what a bank or insurer would sell. The third (target-date) is false; saying it would give a judge an easy "who says?".
- **U-B. The bundle's real price is the counterparty and the ratio lock, not just the fee.** Insurer credit sits behind the annuity; issuer credit behind the note. The plan swaps both for the Treasury and an ETF. This answers "high degree of certainty" with the same logic as the defeasance idea (A1): the guarantee comes from the stronger name.
- **U-C. Spansule logic again: no unit does anything clever** (Seam 1, row 8). The unbundled plan is ten simple holdings plus one simple rule, so every part can be checked by the co-sponsor in the room. It is also the answer to last year's lesson (over-complex packaging): complexity is the bank's product, not ours.

### 2.5 Sample sentences (AI DRAFT, at most 3)

1. "A bank would sell Laura two products, a deferred annuity and a protected note; we build both from Treasuries and one index fund, so the guarantee is the government's, not an issuer's."
2. "No off-the-shelf product fits all three jobs at once, which is the only reason to build one."
3. (Final Report) "A bank's version is a fixed-dose combination: the ratio is locked before we know the 2028 deposit."

### 2.6 The case against Seam 2

- It is **reasoning from marketing**: "banks would sell her this" cannot be sourced from the case, and fees saved cannot be quantified here (U: no numbers, none invented).
- A skeptical judge: "you replaced a regulated product with a home-made one and called it a feature." The defence (Treasury beats insurer credit) is strong but must be stated; the metaphor cannot do it.
- The compounding pun puts the plan's weakest point (reinvestment) under the motif's spotlight.

---

## Seam 3. The R, and how the name reads

### 3.1 Ten-plus candidates, tested

Criteria: **True** (of the strategy); **Ten ___s** (works with X = 10, plural); **Plain** (not weird); **Pun** (a second-level echo with pharmacy or finance, and ideally one that does not stay pharmacy-only, since the pharmacy meaning is the *first* XR).

| R word | True | "Ten ___s" | Plain | Second-level echo | Verdict |
|---|---|---|---|---|---|
| **Redemption** | Yes: bond repayment at maturity (5 T-bonds literally redeem at par; the 5 iBonds are fund terminations, whose bonds redeem) | "Ten redemptions": yes | Yes (a little formal) | Finance: the bond is redeemed, **so Laura can redeem her pledge**; both are real senses. Also the UK/Aus "redemption yield". Fund "redemptions" mean outflows (small confusion). | **Keep, #1** |
| **Runway** | **Exactly**: a reserve divided by yearly burn is a start-up/non-profit "runway": ten holdings / $50,000 = **10 years** | Poor: "ten-year runway", not "ten runways" | Yes | Finance and start-up speak (Laura is a product manager, her ventures are start-ups). The take-off reading (the six years before the first payment) is a bonus. No pharmacy echo. Aviation extensions invite AI-style over-extension. | **Best challenger, #2** (use as X-year) |
| **Residency** | Yes: the whole plan funds one; "ten residency years" | Fair | Yes | Pharmacy and medicine have *residencies* (training posts); finance: tax residency, the Taiwan residency rule. Client-first, but not a finance word. | #3, better as an aside than a name |
| **Reserve** | Yes: the case's "operating reserve" | **Fails** ("ten reserves") | Yes | Overloaded (Federal Reserve, reserve price). Pharmacy: "Reserve" is a last-resort antibiotic class (U: WHO AWaRe, not verified here). | Runner-up only as "Extended Reserve" (X not ten) |
| **Receipts** | Weak: Laura pays, the facility receives | "Ten receipts": yes | Fine | **Best pun in the list**: "receipt" once meant a recipe or prescription (T: from Latin *recipe*), as in Rx, and now means proof of payment. Also "bring the receipts" = evidence (the Trading Notes). | Good wink, wrong noun. Final Report aside only |
| **Remittance** | Partly: money sent | Yes | Stiff; connotes migrant transfers | None | Reject |
| **Regimen** | Yes (a fixed schedule) | Poor | Fine | Pharmacy only: doubles the first meaning instead of adding one | Reject |
| **Reliance** | Weak | "Ten reliances": no | Legal flavour | None | Reject |
| **Ration** | Yes (fixed allowance per period = zero-order) | "Ten rations": yes | **Tone wrong**: scarcity, wartime | None | Reject |
| **Rota** | Weak (duty roster) | Poor | British, odd | None | Reject |
| **Run-off** | Exactly: an insurer's closed book that pays out until it is zero | Poor | Negative ("bad bank") | None | Reject (strong word, wrong smell) |
| **Return** | Weak; "return **of** capital" is true, but our message is certainty | "Ten returns": yes | Yes | "Excess return" is the stock sleeve (rung 1 ranks it weak) | Reject |
| **Repayment** | Yes but who repays? The Treasury, not Laura | Yes | Plain | None | Plain fallback |
| **Retirement** | Bonds "retire" at maturity | Fair | Misleads: Laura is not retiring | None | Reject |

Side note: "XR" already means **extended reality** to a general reader and, probably, ex-rights on some price lists (U). Neither does harm; do not mention.

### 3.2 The 3 best findings

- **R-A. Redemption carries two true senses in one chain.** The Treasury redeems a bond, so Laura can redeem a pledge: each January is both. Few R words let the team say "this is what the plan does" without a metaphor.
- **R-B. Runway is the exactly-true challenger.** It is a defined ratio (reserve / annual burn = 10), it is in Laura's own professional vocabulary, and it is an operating-reserve concept, so it answers the case's requirement. It loses only on "ten ___s" and by being an aviation word that tempts over-extension. If the team prefers the *sense* to the plural, use X = ten years, R = runway.
- **R-C. The name already reads like a tier.** "XR" is a real model suffix in consumer products (Plus / Pro / Max feel) and the original pharmacy one (the sort of suffix that NCC MERP says has no standard meaning, F4, so we may define it). "Caplet" is itself a dosage-form word. So "Caplet XR" sounds like an OTC medicine with a premium tier, which is the right joke at the right size. Mirror fact (T): reversed it is **Rx**, the prescription mark, from Latin *recipe*, "take". Optional bracket wink.

### 3.3 How to show both meanings in a sentence or two (voice: concede, then turn; numeral; bracket; kicker)

Sample sentences (AI DRAFT, exactly 3):

1. "We called it Caplet XR: on a pharmacy shelf XR means extended release, and here X is the Roman 10 and R is redemption (10 holdings, each redeemed once, each redeeming a pledge)."
2. "Yes, a tablet in a bond plan is on the nose; but take the joke away and 10 dated redemptions is simply what the plan is."
3. (Runway alternative) "X is 10 and R is runway: reserve over yearly burn, which here comes to exactly 10 years, and then the reserve is spent, as planned."

### 3.4 The case against

- **Any named R is an after-the-fact backronym**, and judges will see that. Defence: say it lightly, once, in a bracket, and let the plan carry weight.
- Redemption is **formal**, slightly churchy, and in fund language means investors leaving. Runway is **more fun and more exact** but fails "ten ___s". There is no R that is true, plural and punny at once.
- "Receipts" has the best wordplay and the weakest truth, which is the whole risk of this seam: a good pun beating a true word.
- If the reveal needs more than two sentences, the name is working too hard: the safest alternative is **no stated R at all**, just "X for ten".

---

## What I would take forward

1. Seam 1: **F-A (zero-order, fixed dollars) in the IPS as plain words; F-B and F-C in the Final Report.**
2. Seam 2: **say "two products", name the annuity correctly, drop compounding**; the fixed-dose combination foil only in the Final Report.
3. Seam 3: **keep redemption**; hold runway in reserve for the Final Report's reserve section; "receipts" as a Final Report heading pun if wanted.
4. Open for fact-check (Felix): Adderall-style IR/ER bead mixes (U, not used), NECC 2012 (U, not used), insurer guaranty limits (U, not used), Lehman principal-protected notes (R04 queue).
