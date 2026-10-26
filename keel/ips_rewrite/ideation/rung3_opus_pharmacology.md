AI-generated ideation (Claude Code, Opus rung), 26 Oct 2026. Not for submission.

# Rung 3 (deep): the pharmacology motif, "Caplet XR", pressure-tested

Read first: `../README.md`, `../00_GROUND_TRUTH.md`, `rung1_haiku.md` (#1 timed release, #2 blister card, #3 loading
dose, #4 therapeutic window). Plan as mapped in rung 1, with the floor taken from
`keel/library/ips_numbers_2026-10/IPS_number_sheet.md`: the floor is IBTM, a Dec-2032 iBond fund sized to repay $150k
face, so **the floor grows back to the full 2028 deposit**, and VT (~$32k, MODEL) is what is left over.

**Bottom line up front.** Keep the motif, but on a short leash. Use it in the name, one line explaining XR, and two or
three working terms ("whole", "window", "generic"). Never use "dose", "toxic" or "patient" about Laura. Add one line
that says the plan holds no options, because to a finance judge "caplet" means a derivative first.

---

## 1. The pharmacology, verified (web checked 25-26 Oct 2026)

| # | Fact a line could lean on | Status | Source |
|---|---|---|---|
| F1 | FDA definition: an extended-release dosage form is "one that allows at least a twofold reduction in dosing frequency" compared with an immediate-release form; delayed release = "releases a drug ... at a time other than promptly after administration" | VERIFIED (FDA wording quoted on a pharmacokinetics site; the FDA/HL7 SPL term ERTAB gives the same idea: "allows at least a reduction in dosing frequency as compared to that drug presented in conventional dosage form") | https://www.pharmpk.com/PK09/PK2009002.html ; https://terminology.hl7.org/1.0.0/ValueSet-v3-ExtendedReleaseTablet.json.html |
| F2 | US law (21 CFR 320.25(f)): an extended-release product must show that it "meets the extended release claims made for it", that its profile "rules out the occurrence of any dose dumping", and that it gives "consistent pharmacokinetic performance between individual dosage units" | VERIFIED | https://www.govregs.com/regulations/title21_chapterI-i4_part320_subpartB_section320.25 |
| F3 | "Modified release" as the umbrella term covering extended and delayed release (USP <1151>) | UNVERIFIED (the USP text is behind a paywall; standard usage, but don't lean on the USP name) | — |
| F4 | Release suffixes have no standard meaning: NCC MERP (adopted 3 Dec 2007, revised 30 Mar 2023) says modifiers such as "LA, CR, CD, XL and SR" have "no standard interpretation that would give a clear meaning" | VERIFIED (XR is not named, but it is the same class of suffix). **Use:** nobody owns what "XR" means, so Caplet may define it | https://nccmerp.org/promoting-safe-use-suffixes-prescription-drug-names |
| F5 | Why "do not crush": NHS Specialist Pharmacy Service: "If you crush a MR tablet, the modified-release properties will be lost. All the drug will be released at once", which can mean "higher blood levels and risk of toxic effects", or a drug released at the wrong site that "may not work" | VERIFIED | https://sps.nhs.uk/articles/checking-if-tablets-can-be-crushed-or-capsules-opened/ |
| F6 | Dose dumping = "the rapid release of the entire dose or a significant fraction thereof in a short period of time" | VERIFIED | https://www.pharmtech.com/view/regulatory-considerations-alcohol-induced-dose-dumping-oral-modified-release-formulations |
| F7 | **Palladone (hydromorphone ER, Purdue Pharma), 2005.** Withdrawn from the US market in July 2005 after tests showed alcohol could cause a "dosage dump". FDA: it would not have been approved had the interaction been known. CMAJ (27 Sep 2005): with "240 mL (8 ounces) of 40% ethanol" the average peak concentration "increased by almost 6 times compared with co-ingestion with water"; one subject showed a "16-fold increase". FDA's Steven Galson: "Even one drink could have fatal implications" | VERIFIED (withdrawal month from MDedge, 1 Sep 2005; figures from CMAJ) | https://mdedge.com/clinicalpsychiatrynews/article/22408/addiction-medicine/palladone-pulled-fda-looks-other-opioids ; https://www.cmaj.ca/content/173/7/756 ; https://www.nbcnews.com/health/health-news/fda-halts-sales-painkiller-palladone-flna1c9441709 |
| F8 | Therapeutic window: the FDA treats a drug as narrow therapeutic index (NTI) when there is "less than a twofold difference in the minimum toxic concentrations (MTC) and minimum effective concentrations (MEC)" (or LD50/ED50), and "safe and effective use of the drug requires careful titration and patient monitoring" | VERIFIED (Tamargo et al., Eur J Clin Pharmacol 2015;71:549-567, quoting FDA) | https://pmc.ncbi.nlm.nih.gov/articles/PMC4412688/ |
| F9 | **Spansule, 1952.** Science Museum: Dexedrine Spansule by Smith Kline and French, "Launched in 1952, it was the first medicine to be supplied in a sustained-release capsule known as a Spansule"; released over "8 to 10 hours" | VERIFIED | https://collection.sciencemuseumgroup.org.uk/objects/co192490/7-dexedrine-slow-release-spansules-containing-10-mg-of-the-active-ingredient-dexamphetamine |
| F10 | Spansule mechanism: hard capsules with "tiny coated granules or pellets"; pellets with different polymer thicknesses "disintegrate at staggered intervals" | VERIFIED (secondary: review article; good enough for one plain line, not a quote) | https://www.ijsrtjournal.com/article/a-review-article-on-spansule-technology |
| F11 | Loading dose: "an initial higher dose ... at the beginning of a course of treatment", then "a lower maintenance dose"; useful when a drug is eliminated slowly, because otherwise reaching the therapeutic level "would take a long time" | VERIFIED (Wikipedia; StatPearls blocked the fetch. "4-5 half-lives to steady state" is textbook but UNVERIFIED here) | https://en.wikipedia.org/wiki/Loading_dose |
| F12 | Bioequivalence (the 80-125% rule): the whole 90% confidence interval of the generic/brand ratio of exposure (AUC, Cmax) must sit within 80-125%. It is a myth that a generic may deliver "anywhere from ... 80% to ... 125%"; a gap near 20% could almost never pass | VERIFIED | https://www.pharmacytimes.com/view/debunking-a-common-pharmacy-myth-the-80-125-bioequivalence-rule |
| F13 | Generics cost "80% to 85% lower" than the brand on average; with many makers, generic prices fall to about 20% of the brand price or lower (FDA analysis cited) | VERIFIED (US Pharmacist, 2010; dated, so say "much cheaper", not a number) | https://www.uspharmacist.com/article/directions-in-generic-drugs |
| F14 | Adherence: WHO (1 Jul 2003, "Adherence to long-term therapies: evidence for action"): in developed countries "adherence among patients suffering from chronic diseases averages only 50%" | VERIFIED | https://www.who.int/news/item/01-07-2003-failure-to-take-prescribed-medicine-for-chronic-diseases-is-a-massive-world-wide-problem |
| F15 | Pre-registration: ICMJE (statement published 2004): "Trials must register at or before the onset of patient enrollment", for trials starting enrolment after 1 July 2005 (older trials by 13 Sep 2005); registries must hold "definitions of the primary and secondary outcome measures"; "selective reporting ... distorts the body of evidence" | VERIFIED | https://www.cmaj.ca/content/171/6/606 |
| F16 | FDAAA 2007 (Public Law 110-85), section 801: register applicable trials "no later than 21 days after enrollment of the first participant"; results "no later than 12 months" after the primary completion date | VERIFIED (ClinicalTrials.gov staff article; enactment 27 Sep 2007 is used there as the start threshold) | https://cdn.clinicaltrials.gov/documents/publications/Wong-Williams-RAPS-Regulatory-Focus-8May2012.html |
| F17 | The "caplet" itself: a "capsule-shaped tablet" that OTC makers developed to borrow capsules' image of potency; tablets were seen as more resistant to tampering after the 1982 Tylenol murders | VERIFIED (secondary encyclopedia; fine for a Final Report aside) | https://www.chemeurope.com/en/encyclopedia/Capsule_%28pharmacy%29.html |
| F18 | Food effect (release and exposure that change with what is in the stomach) | UNVERIFIED (not checked this run; no line below uses it) | — |
| F19 | Tighter bioequivalence limits for NTI generics | UNVERIFIED (not checked; no line below uses it) | — |

### The 1952 coincidence: VERIFIED, all four
- Markowitz, "Portfolio Selection", *Journal of Finance* 7(1), 77-91, 1952.
- Roy, "Safety First and the Holding of Assets", *Econometrica* 20(3), 431-449, July 1952. Markowitz later said Roy
  "can claim an equal share of this honor" (https://en.wikipedia.org/wiki/A._D._Roy).
- Redington, "Review of the Principles of Life-office Valuations", *Journal of the Institute of Actuaries* 78(3),
  286-340, December 1952 (immunisation) (https://www.cambridge.org/core/journals/journal-of-the-institute-of-actuaries/article/review-of-the-principles-of-lifeoffice-valuations/42DE39108ADCAD8D476B8E633F8E606F).
- Smith Kline and French launched the Spansule, also in 1952 (F9).

So the same year gave us the diversified growth sleeve (Markowitz), the shortfall-first rule (Roy: minimise the
chance of falling below a disaster level, which is our floor), bond immunisation against a liability schedule
(Redington: our ladder), and the first timed-release capsule. All three finance ideas are in the plan. **Use it in
the Final Report only** (it needs citations, and in the IPS it would read as trivia). It could carry a section
heading, for example "1952, a vintage year (for capsules too)".

---

## 2. Part-for-part mapping (drop every STRETCH)

| Plan element | Pharmacology counterpart | Grade | Honest break point |
|---|---|---|---|
| Ten rungs, one maturing a year, 2033-2042 | Spansule-type multiparticulate: beads whose coating sets, at manufacture, when each one releases (F9, F10) | **EXACT** | Beads release over hours and overlap; a rung pays one lump on one date. The key fact maps exactly: release time is fixed when the unit is made, not decided later. |
| Held to maturity; no selling | "Do not crush or chew": the release claim holds only if the unit is kept whole; crushing releases everything at once (F2, F5, F6) | **EXACT** | Selling early is not toxic. It turns a known maturity value into whatever the market pays that day. The legal parallel is strong: an ER claim is tested on the intact unit (F2), and our "high certainty" applies only to the unbroken ladder. |
| Plan built for few decisions: buy 2027, deposit 2028, range 2031, gift 2033, nothing traded in between | The FDA's own definition of extended release: "at least a twofold reduction in dosing frequency" (F1); fewer doses because adherence is poor (F14) | **EXACT** | Laura is not a non-compliant patient. The point is behavioural (fewer decision points, fewer chances to err), not that she is unreliable. Never say "adherence" about her. Check this against any annual-review clause the IPS keeps. |
| iBond ETFs (IBTM-IBTR) end at NAV, not par | Generic drug: proven to give near-identical exposure within tight limits, much cheaper and easier to get, but not the same molecule in the same packaging (F12, F13) | **GOOD** | No regulator sets an 80-125% band on an ETF. The gap (NAV vs par) is set by the market, and is small only because the fund holds Treasuries maturing near its end date. Say "near-identical", never "bioequivalent" or "guaranteed". |
| VT at 0.06% instead of stock-picking | Generic versus brand: the brand premium buys a label, not a better effect | **GOOD** | Active funds are not literally the same molecule; they hold different stocks. The claim that most underperform needs a source (e.g. SPIVA, UNVERIFIED here). Use "generic" once in the whole document: either here or for the iBonds, not both. |
| 2031 range: floor to floor + half the fund | Therapeutic window: MEC (below it, no effect) to MTC (above it, harm) (F8) | **GOOD** | A real window is set by the drug and the body; ours is chosen by a rule (half the fund) and its top floats with stocks until 2031. The harm above the top is the case's own: overpromising "could damage her credibility". "Below the floor, no signal" is our reading of "a meaningful personal contribution may signal". |
| 2033 gift capped at the 2031 top | Label maximum dose: never exceed the stated top, however well the patient feels | **GOOD** | The cap binds us, not a body. The other half kept by Laura has no pharmacology counterpart: leave that half out of the motif. |
| Uncertain 2028 deposit fills ladder gaps first (measured in Jan 2028) | Titration with monitoring: measure the level, then dose to close the gap (F8: NTI drugs need "careful titration and patient monitoring") | **GOOD** | Titration repeats; we measure once. And if the deposit is short, there is no second dose to give. Use "measure, then top up", never "dose". |
| Whole 2027 deposit buys all ten payments on day one, not over time | Loading dose: reach the target level at once rather than waiting for slow build-up (F11) | **GOOD** | A loading dose is followed by smaller maintenance doses; we add only one more deposit, and it may not come. Also "loading" can suggest overshoot. Final Report only, if at all. |
| Trade notes written at the trade and not editable; IPS frozen after submission | Trial pre-registration of endpoints before enrolment (F15, F16) | **EXACT** | Rung 1 banned "Pre-Registered" as a *motif name*. One sentence in the Final Report's articulation section is fine; don't use it as a frame. |
| Floor (IBTM sized to repay $150k = the full 2028 deposit) | Minimum effective concentration | **GOOD** | MEC is a threshold of effect; our floor is an owned asset that grows back to money she already put in. The "grows back to the deposit" idea (the North Star "commit only money she already owns") has no drug image. State it plainly. |
| Refusing to put floor money in stocks | NTI drug: don't swap in a "similar" product when the window is narrow | **STRETCH, dropped** | NTI generic-substitution rules are not verified here (F19), and the reason we refuse is a hard promise, not a narrow window. |
| 2027 ladder bought latest-dated first | Coated tablet: the core, made first, releases last | **STRETCH, dropped** | In a tablet the order is forced by physics. In the plan it is a risk choice (any gap lands in the early years, which the 2028 deposit can still fill). A judge who asks "why?" gets no pharmacology answer. |
| Coupon reinvestment risk if yields fall | Food effect / environment changing exposure (F18) | **STRETCH, dropped** | Unverified, and it is the plan's one live risk: it deserves a number, not an image. |
| ~$32k stock fund | "Active ingredient with variable response" | **STRETCH, dropped** | Says nothing a reader doesn't already know. |
| Reserve running off 2033-42 | Maintenance dose / blister calendar pack | **STRETCH, dropped** | A maintenance dose replaces what the body removes and has no end date; the reserve is a finite course that shrinks to zero. "Blister" reads as injury (rung 1). |
| WInS book as a scaled-down demonstration | Pilot study at a lower dose | **STRETCH, dropped** | The WInS book is $300k, the same size as the first deposit; it is not a lower dose. |
| Alcohol-induced dose dumping (Palladone) | A hidden trigger that breaks the release | *(no plan element)* | Nothing in the plan is a trigger like this. Keep Palladone for one Final Report sentence about why "held whole" is a rule, not a preference. |

**What survives:** timed units (the ladder), keep it whole (held to maturity), fewer decisions (extended release by
the FDA's own definition), generic (iBonds or VT), window (the 2031 range) with its label maximum (the cap), and
measure-then-top-up (2028). That is enough for 3-5 IPS sentences. Use no more than three of them in the IPS.

---

## 3. "Caplet" in finance: clever, or a misfire?

**Verified.** An interest-rate cap is "a series of European call options, known as caplets" on a reference rate; a
floor is a series of puts, "floorlets"; a borrower "can protect himself against a rise in rates by buying a cap"; a
collar is "the simultaneous purchase of an interest rate cap and sale of an interest rate floor"
(https://en.wikipedia.org/wiki/Interest_rate_cap_and_floor). A cap is also equivalent to puts on bonds.

**The plan's payoff.** Gift = min(floor + ½ × VT in 2033, 2031 top), and it is never below the floor. That is bounded
on both sides, so it is *collar-shaped*. Read properly, it is a **home-made capital-protected note**: an owned
Treasury that grows back to the $150k deposit, plus equity upside, capped. Banks sell this as a structured product
with options inside. Caplet builds it from two ETFs and a written rule, with no options. *That* is the "huh" a finance
judge will enjoy, and it is plain finance, not a pun.

**Where the pun misfires.**
1. **Wrong underlying.** A caplet caps an *interest rate*; our cap is on a *gift amount*. Calling our cap a "caplet"
   is wrong.
2. **Wrong direction.** A caplet pays when rates *rise* (it protects borrowers). Our one open risk is rates *falling*
   on reinvested coupons, which is what a *floorlet* covers. A judge who knows this will spot the mismatch at once.
3. **Compliance optics.** Derivatives are banned. A strategy named after a derivative, in a document a judge reads
   for rule breaches, invites a second look. Last year's lesson was trading outside the rules; don't make anyone
   wonder.
4. **"Collar"** strictly means bought and sold options. Say "collar-shaped" or "floor and cap", never "a collar".

**Verdict:** as a pun, it misfires; as a single disclaimer that shows we know the instrument, it earns its place.
At most two lines, both strictly true:
- **L1 (IPS-safe, 14 words):** "Despite the name, there are no caplets here: the floor is a Treasury, the cap a promise."
- **L2 (Final Report only):** "If derivatives were allowed, our one open risk – coupons reinvested at lower rates – would
  call for a floorlet, not a caplet. They aren't, so the 2028 deposit and Laura's half cover it instead." (Check L2
  against the D1a vote on what fills a coupon gap first, and the order on the number sheet: 2027 leftover, then
  Laura's half, then the gift above the floor.)

---

## 4. A second meaning for XR: shortlist of five, ranked

The licence for this comes from F4: release suffixes have no standard meaning, so the team can define its own.

| Rank | Reading | Exact one-line use | Product-tier feel | Truth test |
|---|---|---|---|---|
| **1** | **X = ten (Roman numeral): "ten releases"** | "Caplet XR: X for the ten payments, R for releases – one each January, 2033 to 2042." | Strong. Reads like a model number, and the Roman ten makes it a real tier name rather than an acronym. | **Exact.** Ten fixed releases, each from its own holding. And it keeps the original "extended release" meaning, so the name works both ways with no strain. |
| 2 | Extended Reserve | "XR also stands for Extended Reserve: from 2033 the ten holdings *are* the operating reserve, running down one a year." | Good. Sounds like a fund share class. "Extended" slightly echoes an "extended warranty" sales pitch. | **True.** It uses the case's own noun ("operating reserve") and answers the "composition over time" requirement. Weakness: "extended" might suggest the reserve is larger than needed. |
| 3 | Exact Release | "XR: exact release – $50,000 on each date, no earlier, no later." | Fair. Sounds like a precision-engineering claim. | **Mostly true.** Each T-bond pays par, but the iBond ETFs end at NAV, not par (TNA note 2). "Exact" overclaims for 2033-37. Fails a strict check. |
| 4 | Excess Return | "Everything above the floor is the XR tier: excess return, and the only part that can move." | Strong: a real finance term, so judges read it at once. | **Weak.** In finance, excess return means return above the risk-free rate or a benchmark; using it for "the gift above the floor" is loose, and judges will notice. |
| 5 | Extended Range | "XR: the extended range Laura can quote in 2031." | Fair. | **Fails.** The range is deliberately *narrow* and capped; "extended" says the opposite of the design. |

**Recommendation:** use #1 in the pitch or the opening line; keep #2 for one sentence in the reserve paragraph if
the word count allows. Don't stack both in the same paragraph. (Apple's iPhone XR used X = ten; the tier echo helps,
but don't mention Apple, and it is UNVERIFIED here anyway.)

---

## 5. Five model sentences (each under 25 words, British spelling) and a kicker

`AI DRAFT (Claude, 26 Oct 2026)`. Each one does investing work first; the motif rides along.

1. **(Opening; names it.)** "Caplet XR is an extended-release plan: ten Treasury holdings, each timed to release one $50,000 payment, from 2033 to 2042." *(20 words)* Work: liability matching, one dedicated holding per payment.
2. **(Hold to maturity.)** "Like any extended-release tablet, it works only if swallowed whole: every holding is kept to maturity, so prices along the way don't matter." *(23)* Work: held to maturity removes price risk on the payments; it sets the no-selling rule.
3. **(Few decisions.)** "The plan asks Laura for four decisions – 2027, 2028, 2031, 2033 – and nothing in between, because fewer decisions mean fewer to get wrong." *(23)* Work: rules over discretion, behavioural risk. (No drug word in it; the motif is felt, not named. Check against any annual-review clause.)
4. **(The 2031 range.)** "The 2031 range works like a therapeutic window: promise less and co-sponsors see little commitment; promise more and she risks her credibility." *(21)* Work: why a range with a floor and a top, both drawn from the case.
5. **(iBond ETFs.)** "iBond ETFs are a generic Treasury: near-identical exposure, easy to trade in small amounts, but they end at net asset value, not par." *(23)* Work: owns the instrument's one weakness, which the TNA already concedes.

**Kicker (calls back to sentence 1):** "Ten releases, one each January. Take as directed." *(8)*

Spares (Final Report or IPS swaps): "Selling a holding early is crushing the tablet: the whole dose arrives at once, at whatever price that day sets."
(*20*). "Despite the name, there are no caplets here: the floor is a Treasury, the cap a promise." (*14*)

In a 500-word IPS, use sentence 1 (or a pitch version of it), one of 2 or 5, sentence 4, L1, and the kicker. That is
4-5 motif sentences. Sentence 3 can stand anywhere as plain prose.

---

## 6. Verdict

**Keeper, conditionally.** No rung-1 alternative has both an exact mechanical fit (timed units, kept whole, fewer
decisions by the FDA's own definition, a window with a label maximum) *and* a name only Caplet could own. Drone Note
(rung-1 #1) fits P1/P3 equally well, but it isn't ours, and "drone" reads badly. Final Reserve (#3) is clean, but it
clashes with "operating reserve" and is generic. Therapeutic Window and Blister Card are this same family.

**The strongest case against it:**
1. **It's about us, not Laura.** The name ties to the *team*; the judges score Client Knowledge. A graphic novelist's
   residency dressed up in pill language is self-referential, and nothing in the case is medical.
2. **"Caplet" means a derivative to finance judges**, and derivatives are banned (section 3). Any confusion costs more
   than the wit gains.
3. **AI tell.** A sustained extended metaphor (dose, window, release, generic, label, titrate) in every paragraph is
   exactly how a language model decorates. Judges who read 2,000 AI-assisted IPSs will recognise it.
4. **Medical words near money.** "Toxic", "dose" and "patient" about a client sound flippant, and maybe insulting.

**How to defuse it:**
- **Ration it.** Name + XR line + at most three terms in the IPS ("whole", "window", one "generic"). Never "dose",
  "toxic", "patient", "adherence", "prescribe".
- **Let finance carry the "aha".** The IPS's real insight is the home-made capital-protected note: a Treasury that
  grows back to the deposit, plus capped equity, no options. The motif labels the parts and doesn't explain them.
- **Disarm the derivative reading in one line (L1).** It turns the risk into proof of knowledge.
- **Keep it dry.** Use pharmacy-label register: short, literal, no adjectives. "Take as directed" works because it is
  a real label phrase, not a lyrical one.
- **Put the depth in the Final Report.** The 1952 coincidence, Palladone, pre-registration and the Spansule history
  all go there, with citations, under one punny heading.
