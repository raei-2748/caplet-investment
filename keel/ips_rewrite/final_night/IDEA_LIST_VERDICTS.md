# IDEA LIST VERDICTS: the pasted list in BIBLE Book 12, item by item

AI-generated (Claude Code, finance researcher), Thu 5 Nov 2026 (Sydney). Not submission text. Keel is a simulated
team, AI-written. Source: `keel/BIBLE.md` lines 452-690 (the fenced "pasted list"). Line numbers below are BIBLE lines.

**The test applied to every item.** Caplet's plan is static cash-flow matching plus a growth remainder: ten Treasury
holdings bought for the ten payments, a late-2032 Treasury fund for the minimum facility contribution, about that
fund's interest in VT, a 2031 range whose bottom is owned and whose top is moved into Treasuries before it is named,
and a reinvestment gap covered from kept shares. It does **not** run CPPI, a ratchet, a glide path triggered by
markets, rebalancing bands, duration rebalancing or any rule that trades on a market move. The locked TNA and trading
notes agree (Archive check of 5 Nov: C2, C4, C8, C10, C11, C12 clash). Wharton: the IPS gives strategy and reasoning,
not "detailed financial calculations", sizes or the final range; sources need not be cited. The labels "Roots",
"Canopy", "Branch" are banned (Book 2); where an item uses them I translate them as payments / growth money /
facility money. "Ballast" is the same family of metaphor and should not be used either.

**Verdicts.** USE IN IPS = worth reasoning (no numbers) in the 500 words. FINAL REPORT ONLY = right, but it is a
number, exhibit or method. REJECT = wrong for this plan, contradicts the locked record, or is packaging.
**Accuracy** = my check of the maths and facts (recomputed in Python, flat curve, annuity due).

## A. The opening concepts (lines 452-472)

| # | Line | Item | Verdict | Reason specific to Laura's case | Accurate? |
|---|---|---|---|---|---|
| 1 | 452 | Hamada leverage: surplus beta = asset beta x (1 + D/E); reserve ~$400k vs surplus ~$200k, so a 60/40 gives the facility money beta ~1.8 | **USE IN IPS** (the idea, no numbers); numbers FINAL REPORT | The fixed payments are debt on Laura's balance sheet; whatever is left is levered equity. That is the reason to buy the payments in Treasuries and put only interest in shares. Damodaran packet 1 p. 168 is the source. | **Yes.** 0.6 x (1 + 2) = 1.8. Uses the no-tax form, right because taxes are out of scope. At a flat 5.25% the 2033 reserve is $401,468 and the all-Treasury leftover $200,071, so D/E is ~2.0. Caveat: it critiques a 60/40, not our plan; in our plan the payments are hedged, so the facility money's beta is low. |
| 2 | 453 | Merton structural model; DD >= 2.33 (99%) as the IPS definition of "high degree of certainty" | **REJECT** | Our certainty is structural (each payment held in a Treasury), not probabilistic. DD assumes lognormal assets against a fixed liability; for a matched ladder it is close to infinite and says nothing, and adopting "99%" would weaken our definition and invite "why not 99.9%?". | Formula standard; N(2.33) = 0.990, correct. Inapplicable here. |
| 3 | 454 | Duration: ladder ~$295k at 5.25% in Jan 2027, modified duration ~9.6, ~$28k per 100bp; a 60/40 bond sleeve of duration 5.5 offsets ~1/4 | **FINAL REPORT ONLY** | Good for the "why not a 60/40" exhibit and to show what pre-locking removes. Not IPS: it is a calculation. | **Yes.** $295,337; modified 9.58; $28,284 per 100bp. 60/40: $120k x 5.5% = $6.6k, about 23%. Note FACTS.md: actual 4 Nov curve cost is $300,608. |
| 4 | 455 | Roy safety-first and Sharpe-Tint surplus optimisation; case wording is a safety-first problem | **FINAL REPORT ONLY** | True and the case words support it ("protecting the capital required", case 72-74). Our plan is Telser's lexicographic form: payments first, then return. Generic as an IPS sentence. | Correct as a characterisation. |
| 5 | 456 | Damodaran's implied ERP 4.23% early August, ~9% expected equity return; ~9.5% if the 10-year at 5.25% | **FINAL REPORT ONLY** (capital-market assumptions) | Needed for the projections only. Use the current figure. | August figure **UNVERIFIED**. Verified instead: Damodaran home page, 1 Nov 2026, implied ERP 4.41% (prior month 4.20%) with the US Treasury at 5.29%, so ~9.7% expected; he also nets a 0.22% US default spread. |
| 6 | 457 | Thin premium vs 5%+ Treasuries; equities beat a locked zero over 5 years only ~64% (8.5% arithmetic, 16.5% vol); Bodie beats naive "stocks for the long run"; show Siegel's side | **USE IN IPS** (the Bodie point is already there); numbers and Siegel FINAL REPORT | Directly supports "time makes a loss rarer, not smaller" and the small share sleeve. | **Roughly.** My lognormal check against a 5.25% zero gives ~61%, not 64% (depends on treating 8.5% as arithmetic). Siegel's figures are in Shiller 2011 L4 (6.8% real, 1871-2006). |
| 7 | 458-461 | CPPI governor (floor 90% of riskless 2033 value, multiplier 3, cap 60-80%, annual rebalance, tolerance band); avg equity ~11% of capital; "floor turns the pledge into a risk budget"; cash-lock failure ($168k vs $185k in a 2008 path) | **REJECT** | The team does not run CPPI. It sells shares as they fall, which contradicts "changes only on fixed dates, never on a market move", the IPS's rejection of portfolio insurance, and the locked notes ("we'll simply ignore price noise"). Shiller 2011 L21: portfolio insurance "wasn't really insurance. It was an automatic sell strategy." Uses the banned "Branch" label. | Parameters arbitrary. Cash-lock is a real CPPI failure mode (Black and Perold 1992, UNVERIFIED tonight). The $168k vs $185k result is **UNVERIFIED** (their model). |
| 8 | 462 | Hurdle rate: the facility money's hurdle is the Treasury-zero yield; risk must justify itself against it | **USE IN IPS** (one clause) | This is the plan's logic for putting only the fund's interest in shares: every dollar in VT has to beat what the matching Treasury pays for certain. Damodaran: hurdle = riskless rate + risk premium (packet 1). | Correct. |
| 9 | 463-468 | The 2033 waterfall: S = assets - payments; C = min(0.9S, max(pledge floor, 0.75S)), rounded down to $5k; retained 25% is a real option and "covers the floor"; Damodaran FCFE, Lintner, Swensen spending rules | **REJECT** the formula; Lintner part **USE IN IPS** (see #9b) | It contradicts our plan: our bottom is a fund payout already owned and our top adds half the shares, not 75% of a marked surplus; "half stays hers". It is also a detailed calculation. "Write this into the IPS" is against Wharton's instructions. | **Internally inconsistent:** if the floor exceeds 0.9S, the min() returns 0.9S, below the promised floor; and the retained 25% cannot both be kept flexibility and the floor's backstop. Uses "Roots". |
| 9b | 467 | Pledge cut punished like a dividend cut (Lintner); signaling | **USE IN IPS** | Exactly our 2031 rule: name only what is owned or moved into Treasuries first. Damodaran packet 2 pp. 150-152, 176. | Correct (Damodaran: increases far outnumber cuts; "Inertia" drives policy). |
| 10 | 469 | Newsvendor: promise the 1/(1+k) quantile; k = 4 gives the 20th percentile; loss aversion and anchoring | **FINAL REPORT ONLY** | Apply it to the top of the range only; our bottom is owned (no quantile). Needs a distribution and a chosen k. | **Maths correct** (critical ratio 1/(1+k)). "Sponsors remember a missed number far longer" is plausible but **UNVERIFIED** as an empirical claim. |
| 11 | 470 | Premium Check: 8-week window SD ~6.5% vs expected premium ~0.6%, so no skill can be inferred; Lehrer's "Truth Wears Off"; judge process not outcomes | **FINAL REPORT ONLY** (Articulation of Experience) | Fits Wharton's "do not focus on portfolio performance". | **Yes:** 16.5% x sqrt(8/52) = 6.47%; ~4% x 8/52 = 0.6%. Lehrer on "the syllabus" **UNVERIFIED** (I did not check which syllabus). |
| 12 | 471 | Diversification audit (Shiller L4, Markowitz): marginal contribution to risk, diversification ratio, Taiwan-stress screen vs a Taiwan ETF and USD/TWD | **FINAL REPORT ONLY**, one paragraph | With ~90% Treasuries, VT is nearly all the equity risk by construction, so MCR adds little. The useful part is the TWD point: the facility cost is in Taiwan dollars. | Fine as method. |
| 13 | 472 | Options as priced insurance: a 5-year zero costs ~77.4% of face, leaving ~22.6% for a call; 5-year ATM call ~23% at 17% vol and 1.3% yield; protected structures ~break-even | **USE IN IPS** (already: the "capital-protected note" paragraph); numbers FINAL REPORT | It is the reasoning behind our structure (Treasuries + growth with the interest) and why we own the shares instead of an option. Options are banned on WInS, so benchmark only. | **Yes.** 77.4% implies 5.26%; Black-Scholes gives 22.6% with r = 5.26%, q = 1.3%, vol 17%. |

## B. The IPS-template items (lines 473-488)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 14 | 473 | Mission line "Protect the commitment first; let the upside serve the dream." | **REJECT** | A slogan; Ray: "metaphors alone does not count as creativity". | n/a |
| 15 | 474 | Dual mandate, separate benchmarks (funded ratio >= 100%; riskless 2033 value + premium) | **FINAL REPORT ONLY** | Useful as liability-relative evaluation; banned labels. | Fine. |
| 16 | 475 | Risk metrics: surplus-at-risk and distance-to-default, not volatility | **FINAL REPORT ONLY** (surplus-at-risk); DD **REJECT** | See #2. | Fine. |
| 17 | 476 | Three-part certainty definition | See #53 | | |
| 18 | 477 | Hedge ratio 100% of the liability's rate sensitivity (+/-2%), rechecked when a contribution arrives | **REJECT** | "Rechecked" implies duration rebalancing, which the locked record contradicts (Archive C4). Matching each payment already hedges 100%. | Concept fine; wrong instrument for us. |
| 19 | 478 | Governor: CPPI parameters, equity cap, bands, calendar, alternative dial positions; "beyond ~50% equity the 5th percentile slides toward the floor" | **REJECT** | Same as #7. The dial positions (Treasury-only, ours, 50/50) belong in the FR rejected-alternatives table. | 50% claim **UNVERIFIED**. |
| 20 | 479 | Capital market assumptions: building blocks (riskfree + implied ERP), cross-checked with CAPE and history, haircut, Base/Low/High | **FINAL REPORT ONLY** | Needed for projections and the case's assumptions list (case 146-148). | Fine. |
| 21 | 480 | Facility contribution policy: the waterfall | **REJECT** | See #9. | |
| 22 | 481 | Co-sponsor policy: pledge ladder, annual updates, "expects" not "will", 2031 lock rule | **FINAL REPORT ONLY** (the lock rule is already in the IPS) | Fits the case's range test (case 117-120). The draft communication is FR by Wharton's rule. | Fine. |
| 23 | 482 | Decision rights: investment committee, quorum, limit on discretionary trades | **REJECT** | One client, a 500-word cap, and a template, not a thought. | n/a |
| 24 | 483 | Behavioural guardrails: Ulysses clauses, Nudge choice architecture, stay-the-course default, 48-hour cooling-off, pre-mortem | **REJECT** the apparatus; the principle is already in the IPS ("changes only on fixed dates") | The stronger evidence is Swensen's 1987 data (Shiller 2008 L9), for the FR. | n/a |
| 25 | 484 | Eligible instruments: no leverage, no shorts, no sold options, issuer limits | **FINAL REPORT ONLY** | Wharton bans all derivatives, not only sold options; "issuer limits" is meaningless when every promised dollar is a US Treasury. | Understates the rule. |
| 26 | 485 | If-then trigger table: yields +/-100bp, 20% drawdown, ERP > 5.5%, missed contribution, geopolitical shock, US downgrade | **REJECT** | Market-move triggers contradict the plan. Our only conditional rules are date-based (2028 first completes the ladder; 2031 reinvestment test). A US downgrade discussion belongs in the FR risk section. | n/a |
| 27 | 486 | Review and amendment: scheduled and event-driven reviews, version log | **REJECT** for the IPS | Wharton: the strategy cannot be revised after submission. FR can review implementation. | n/a |
| 28 | 487 | Three-number dashboard (funded ratio, surplus, pledge confidence) with traffic lights | **FINAL REPORT ONLY**, without traffic lights | Traffic lights imply acting on market states. Banned label. | n/a |
| 29 | 488 | Assumption register | **FINAL REPORT ONLY** | The case asks for assumptions (case 97-99, 146-148). | n/a |

## C. Final Report outline and exhibits (lines 489-511)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 30 | 489-499 | FR outline: executive summary, balance sheet, design logic and rejected alternatives, implementation (WInS separate), certainty tests, waterfall, co-sponsor section, uncertainty (reverse stress, tornado), inflation and FX real/nominal, what would change our mind, appendix | **FINAL REPORT ONLY**, minus the waterfall | Sound structure. Keep WInS results out of projections (case 132-133). | Fine. |
| 31 | 500-510 | Exhibits: balance-sheet reframe; reserve cost vs yield with 5.09% break-even; liability duration 10 to 0; funded-ratio fan hedged vs unhedged; surplus histogram; scenario table; tornado; cone-narrowing; pledge ladder; waterfall | **FINAL REPORT ONLY**, minus the waterfall diagram | The 5.09% break-even exhibit is the strongest: it shows why $300,000 is the right first deposit. | **5.09% verified:** at a flat 5.0867% the ten payments cost exactly $300,000 in Jan 2027. "Duration from 10 to 0" fine (it falls mechanically as rungs mature). |
| 32 | 511 | One-page "Letter to Laura" | **REJECT** | Wharton asks for a draft communication to co-sponsors, not a letter to Laura; uses FR space. | n/a |

## D. The second AI's CFA-style IPS (lines 512-529)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 33 | 512-517 | Purpose/profile, objectives, multi-stage horizon (6-year build, 1-year pivot, 10-year payout), liquidity needs, ranges with rebalancing bands, two-sleeve structure "immunized" | **REJECT** as an IPS template; the multi-horizon observation **FINAL REPORT ONLY** | Ray: no paragraph that retells the case; Wharton: points need not be addressed separately. "Immunized" is the wrong word for our dedicated ladder; bands contradict the plan. | Liquidity facts right (case 63-65). |
| 34 | 518-525 | FR contents: headline numbers, assumptions log (fixed-nominal insight), reserve evolution ("does duration shorten each year? yes"), facility range with sensitivity, co-sponsor range and confidence, fundraising excerpt, true bear case (facility can fall while the reserve is protected), flexibility discussion | **FINAL REPORT ONLY** | All required by the case (case 95-120). The bear-case point is right for our plan, except that our facility bottom does **not** go to zero: it is an owned Treasury fund. | Correct, with that exception. |
| 35 | 526-529 | Chhabra's three buckets: personal risk = operating reserve; market risk = committed facility money; aspirational = flexibility reserve | **REJECT** the mapping | Wrong for our plan: our committed facility minimum is in Treasuries (Chhabra's personal-risk bucket), and Chhabra's aspirational bucket is for lottery-like risk, whereas Laura's kept money should be the money nobody can claim, not the riskiest. A Chhabra citation could appear in the FR literature note. | Chhabra (2005) is real (UNVERIFIED tonight). |

## E. "The core math" (lines 530-570)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 36 | 530-539 | 1.1 Reserve cost table (2%-6%) and formula; a 1-point fall raises the cost ~$17k (4%); unhedged rate risk can erase 10-15% of the facility | **FINAL REPORT ONLY** | Shows what locking in 2027 removes, and the risk before the 2028 purchase (IBTR note, Archive C9). | **Yes.** $458.1k, $439.3k, $421.8k, $405.4k, $390.1k all match; 5% to 4% adds $16.4k (4.0%); $16.4k / $140k = 11.7%. |
| 37 | 540-545 | 1.2 Null hypothesis: all Treasuries at 4% gives $562.1k, reserve $421.8k, facility $140.3k "with near-certainty"; "most teams will never compute it" | **FINAL REPORT ONLY** (the most important FR benchmark) | This is the "hardest question" in the 5 Nov shortlist. Every judge-facing figure must use today's curve. | **Arithmetic right, input stale.** At 4% flat: $140,327. At 5% $188,080; at 5.25% **$200,071**; the team's September-curve model says ~$190k. Using $140k would understate the riskless benchmark by ~$50-60k and make our lower bottom look better than it is. |
| 38 | 546-561 | 1.3 Master equation: facility = anchor + G0 x (M - 1.265); 7%/16% gives median 1.39, mean 1.50; table A-D; insights: risk buys little; P(underperform riskless) ~40% at any size; insuring the sleeve costs ~15.5% (Bodie put); gap-risk m ~2 | **FINAL REPORT ONLY**; the insight "sizing changes the size of regret, not its likelihood" is good enough to inform the IPS reasoning | Supports a small, deliberate share sleeve. The gap-risk/m line is CPPI: reject. | **Checked:** 1.04^6 = 1.2653; median 1.40, mean 1.50; P(M < 1.265) = 38.7%; put 2N(0.196) - 1 = 15.5%. Table percentiles **UNVERIFIED** (not re-simulated) and use the stale 4%. |
| 39 | 562-568 | 1.4 Surplus framework: PV liability $333.4k, assets $300k + 0.75 x PV($150k) = $408.2k, cushion $74.9k, funded ratio 1.22; haircut because her income falls in recessions; m = 2.0 gives 50% start | **REJECT** the haircut and m; human-capital point **USE IN IPS** (already) | The case states she "will contribute" $150k (case 43-45), so haircutting it contradicts the case; the case never links her income to recessions, so "can", not "does" (Archive C5). m is CPPI. | Arithmetic right at 4% ($333.3k; $144.2k; $408.2k; 1.22). |
| 40 | 569-570 | 1.5 Liability duration from 2027: Macaulay ~10.2, modified ~9.8, ~$326 per bp on $333k; "hedge the sensitivity, not merely sit in safe bonds" | **FINAL REPORT ONLY** | Our ladder does hedge it, payment by payment. | **Yes** at 4%: 10.18, 9.79, $326. |

## F. "Intellectual lineage" (lines 571-578)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 41 | 572 | Contingent immunization (Leibowitz-Weinberger, "1981") | **FINAL REPORT ONLY** (rejected alternative) | We lock first and risk only the leftover; no trigger. | Published FAJ Nov/Dec **1982** (Part I) and Jan/Feb 1983 (Part II); "1981" may be a Salomon report date. |
| 42 | 573 | CPPI with a ratchet (Estep-Kritzman TIPP) | **REJECT** | See #7. | Estep and Kritzman TIPP (1988) UNVERIFIED tonight. |
| 43 | 574 | Redington immunization: match PV, match duration, asset convexity >= liability convexity | **USE IN IPS** as the contrast (immunization must be re-traded; our matching need not); detail FR | It is the concept that explains "never needs rebalancing". | Correct statement of Redington's conditions. |
| 44 | 575 | Safety-first (Roy 1952): minimise P(missing the goal), not variance | **FINAL REPORT ONLY** | See #4. | Correct. |
| 45 | 576 | Goals-based / behavioural portfolio theory (Shefrin-Statman; Das-Markowitz-Scheid-Statman; Chhabra) | **FINAL REPORT ONLY** (literature note) | Generic; our plan already gives each commitment its own asset. | Citations real (UNVERIFIED tonight). |
| 46 | 577 | Lifecycle with human capital (Bodie-Merton-Samuelson): a bond-like future contribution lets you hold more equity early | **REJECT** the direction | Our IPS argues the opposite (her income can fall with shares, so don't bet twice); and after 2028 there is no further contribution to hedge with. | The theory is right; the application here is backwards for our claim. |
| 47 | 578 | Barbell vs ladder: barbell has more convexity at the same duration; converge to a ladder by 2031 | **REJECT** | Needs rebalancing and carries twist risk; contradicts the locked one-bond-per-payment record. | Convexity claim true for parallel shifts. |

## G. The CFA-structure IPS (lines 579-602)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 48 | 580 | Governance with a Ulysses clause, supermajority, 48-hour cooling-off | **REJECT** | Single client; template. | n/a |
| 49 | 581-585 | Goal ledger: (1) payments >= 99.9% certainty; (2) facility range with one-sided confidence; (3) minimum retained liquidity; (4) credibility: "never communicate an amount that is not hedged or supported at the stated confidence" | Goal 4 **USE IN IPS** (it is our 2031 rule); 99.9% **REJECT** | Goal 4 is exactly "she owns it before she says it". A probability on the payments undercuts our structural definition. | n/a |
| 50 | 586 | Ability vs willingness, ability binds; her human capital has positive equity beta, so avoid media/publishing/consumer-discretionary stocks | **FINAL REPORT ONLY** (ability vs willingness); the no-media-tilt point consistent with the IPS | "Positive equity beta" is not in the case: write "can". VT holds no tilt. | Beta claim **UNVERIFIED** for Laura. |
| 51 | 587-591 | Constraints: multi-stage horizon, no withdrawals before 2033, taxes out of scope, TWD exposure, single-person governance | **FINAL REPORT ONLY** | Facts right (case 63-65, 164-169). TWD belongs in the flexibility discussion. | Correct. |
| 52 | 592-596 | CMAs: base (cash 3.5-4%, Treasuries 4%, equity 6.5-7%), low (5%, CAPE haircut), stagflation; arithmetic for expectations, geometric for compounding (gap ~sigma^2/2 ~1.3 points) | **FINAL REPORT ONLY**, with current yields | Treasuries at 4% are stale (the 10-year is 5.29% per Damodaran, 1 Nov 2026). | sigma^2/2 at 16% = 1.28 points: correct. |
| 53 | 597-602 | SAA table; glide path and trigger table; liability-relative benchmark; band rebalancing using the 2028 check; reserve and facility protocols; dashboard (funded ratio, cushion, m, DV01 hedge ratio, VaR/CVaR, tracking error, probability of goal, liquidity) | Using the 2028 deposit first **USE IN IPS** (already there); benchmark and some dashboard **FINAL REPORT ONLY**; triggers, bands, m **REJECT** | Only date-based moves fit the plan. | n/a |

## H. Exhibits, tests and process (lines 603-625)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 54 | 604-608 | Waterfall diagram (senior / junior / flex); reserve cost vs yield and the benefit of pre-locking; surplus distribution with the "$140k risk-free line"; fan chart; tornado | **FINAL REPORT ONLY** (drop the waterfall's 75% rule) | Senior/junior tranche language is a good plain description of our plan. | The $140k line is stale: use ~$190-200k (#37). |
| 55 | 609 | Historical stress tests: 1973-74, 2000-02, 2008, 2022, 2000-09 | **FINAL REPORT ONLY** | For a matched ladder, these only move the share money and the reinvestment gap; say so. | n/a |
| 56 | 610 | Reverse stress: what breaks the reserve (without a ratchet, ~-82% growth-sleeve loss) | **FINAL REPORT ONLY**, redone for our plan | For us the reserve breaks only on US default or on reinvestment rates near zero for years, not on a share loss. | -82% **UNVERIFIED** and refers to a different design. |
| 57 | 611 | Co-sponsor confidence ladder (Committed / Planning / Stretch) | **FINAL REPORT ONLY** | Maps to owned bottom / Treasury-backed top / kept money. | n/a |
| 58 | 612 | WInS decisions vs shadow portfolios and calibration | **FINAL REPORT ONLY** | WInS results must not enter projections (case 132-133). | n/a |
| 59 | 613 | "What would change our mind" and model-risk humility | **FINAL REPORT ONLY** | Strong for "reasoning, assumptions, and tradeoffs" (Competition Guide). | n/a |
| 60 | 614 | Decision tree for 2031, 2032, 2033 with the rule at each node | **FINAL REPORT ONLY** | Our rules are date-based, so the tree is short and clean. | n/a |
| 61 | 615 | Stochastic yields (Nelson-Siegel / two-factor), floor locked so rates drive only reinvestment and unbought pieces | **FINAL REPORT ONLY** | Right model scope for us (it is how to size the reinvestment test). | Correct framing. |
| 62 | 616 | Cite Chhabra, Das et al., Shefrin-Statman, Merton on defeasing essential goals | **FINAL REPORT ONLY** | Wharton: no citations needed in the IPS. "Merton's writings on defeasing" is vague: name the piece (e.g. Merton, "The Crisis in Retirement Planning", HBR 2014, UNVERIFIED tonight). | n/a |
| 63 | 617-622 | Strategy spectrum: A all-Treasury (zero upside beyond ~$140k); B surplus-only equity; C CPPI m~2; D static 60/40 (~5-6% shortfall); recommend C | Spectrum **FINAL REPORT ONLY**; recommending C **REJECT** | Our plan is close to B (equity only from the facility fund's interest). The spectrum exhibit is good for "rejected alternatives". | A's $140k stale (~$190-200k). D's 5-6% **UNVERIFIED**. |
| 64 | 623 | Brier-score the team's forecasts (Tetlock) | **FINAL REPORT ONLY** (Articulation of Experience) | Distinctive for the reflection section. | n/a |
| 65 | 624 | Annie Duke's "resulting", 2x2 decision vs outcome | **FINAL REPORT ONLY** | Same. | n/a |
| 66 | 625 | Liability-relative performance; a "reserve cost ticker" beside P&L | **FINAL REPORT ONLY** | Good: shows the ladder's market value moves with the payments' cost. | n/a |

## I. "Purpose and governance" IPS outline (lines 626-654)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 67 | 626-627 | Purpose/governance; client translated into quantitative constraints | **REJECT** for IPS (template); FR may use | | n/a |
| 68 | 628 | Liability in one sentence: "Ten payments of $50,000 due January 1 ... 2033 through 2042 (annuity due), fixed nominal, ... probability of at least 99%" | **REJECT** the 99%; the rest **FINAL REPORT ONLY** | Case says "at the beginning of each year" (case 88-89, 59-60); our certainty is structural. | "January 1" is not the case's wording. |
| 69 | 629-633 | Four-test certainty: structural (each payment backed by a maturity-matched Treasury, "only US government credit risk remains"); probabilistic (>= 99% of paths); stress (funded ratio >= 1 in eight scenarios); reverse stress | Structural **USE IN IPS** (already); the other three **FINAL REPORT ONLY** | The structural test is our definition; the others are evidence. | **Inaccurate:** "only US government credit risk remains" is false for our ladder. Also left: reinvestment risk on coupons and on the 2038/2039 early maturities (Damodaran's second riskless condition), and the iBond funds pay NAV, not par (Archive C10). |
| 70 | 634 | Risk tolerance: ability binds; "the reserve is 93% of contributions" | **FINAL REPORT ONLY**, corrected | | **Misleading:** 93% = $421.8k (2033 dollars at 4%) / $450k (2027-28 dollars). On today's curve the ten payments cost ~$300k in January 2027 money, i.e. about all of the first deposit and about two thirds of the two deposits. |
| 71 | 635 | SAA with Roots/Canopy/Ballast ranges, glide path, bands | **REJECT** | Banned labels; bands. | n/a |
| 72 | 636-638 | Funded-ratio traffic light as binding rules; yield-triggered ratchet; rebalance toward Roots when FR falls, never add to Canopy in Yellow/Orange/Red | **REJECT** | Market-state rules contradict the plan and the TNA. | n/a |
| 73 | 639 | Contribution-shortfall contingency: if the 2028 deposit is under $150k, fund the reserve first, facility absorbs it | **FINAL REPORT ONLY** (as a stress) | The case states the deposit as a fact; our rule "the 2028 deposit first completes the ladder" already covers the yield-fall version. | n/a |
| 74 | 640 | Instrument selection: cost, liquidity, size, tracking, counterparty | **FINAL REPORT ONLY** | The one IPS-worthy instance is the iBond trade-off (NAV for daily liquidity, Archive C6). | n/a |
| 75 | 641 | Behavioural guardrails: no discretionary increase in Red/Orange; 48-hour cooling-off | **REJECT** | See #24, #72. | n/a |
| 76 | 642-643 | Liability-relative benchmark; assumption register | **FINAL REPORT ONLY** | Duplicates #15, #29. | n/a |
| 77 | 644-654 | FR outline: one-page decision card; client translation and "Trap Register"; strategy (Roots & Canopy, the Riskless Anchor, spectrum); implementation; reserve; facility formula; flexibility ("Ballast"); co-sponsors; risk; limits; appendices | **FINAL REPORT ONLY**, with labels replaced and no formula | The decision card and the riskless benchmark are the best of it. | n/a |

## J. Stress scenarios, simulation and library (lines 655-690)

| # | Line | Item | Verdict | Reason | Accurate? |
|---|---|---|---|---|---|
| 78 | 655-663 | Eight stresses: 2008 (equities -40%, yields -150bp), 2020, 2022, 1970s, Japan-style near-zero yields ("reserve near $500k"), dot-com decade, contribution $100k, combined | **FINAL REPORT ONLY** | For our plan, Japan-style is the one that matters, and only through reinvestment: the ladder is bought in 2027, so the "$500k reserve" applies only to an unhedged plan. The $100k contribution is outside the case's facts; label it hypothetical. | Reserve at 0% = exactly $500,000: correct. |
| 79 | 664-670 | Simulation: block bootstrap from 1926 (Shiller, Damodaran, Fama-French data), regime-switching stock-bond correlation, two-factor curve, 10,000 paths plus rolling windows; report P5-P95, shortfall, funded-ratio path | **FINAL REPORT ONLY** | Sound; the reserve-on-each-path's-2033-yields step is irrelevant once the ladder is locked; model reinvestment instead. | Fine. |
| 80 | 671-678 | Python core: reserve(0.04) ~421,767; riskless_anchor(0.04) ~140,327 | **FINAL REPORT ONLY** (as a check) | Rerun at today's curve. | **Verified:** 421,767 and 140,327. |
| 81 | 679 | Average several published CMAs (Vanguard, J.P. Morgan, BlackRock, Research Affiliates) and show dispersion | **FINAL REPORT ONLY** | "Uncertainty about the assumptions is itself an insight" is right. | n/a |
| 82 | 680-689 | Research library (Redington, Fisher-Weil, Sharpe-Tint, Black-Perold, Chhabra, Das et al., Bodie-Merton-Samuelson, Campbell-Viceira, Merton, Tetlock, Duke) | **FINAL REPORT ONLY** (bibliography) | Real works; add Damodaran packet 1 pp. 108-110 and Shiller 2008 L9/L18 (see READING.md). | Citations real (UNVERIFIED tonight beyond those in READING.md). |
| 83 | 690 | Data: FRED, Treasury curve, Shiller and Damodaran datasets, Fama-French | **FINAL REPORT ONLY** | | n/a |

## Summary
- **USE IN IPS (reasoning only, no numbers):** #1 levered balance sheet (Hamada), #6 Bodie, #8 hurdle = matching
  Treasury, #9b Lintner range, #13 options-as-insurance (already there), #39 human capital as "can" (already there),
  #43 Redington as the contrast, #49 Goal 4 credibility rule, #53 2028 deposit first (already there), #69 structural
  certainty (already there).
- **REJECT (and why, in one line):** anything that trades on a market move (CPPI, ratchet, triggers, bands, traffic
  lights, hedge rechecks, barbell); probability-based certainty for the payments (DD, 99%, 99.9%); the 75% waterfall
  formula (contradicts "half stays hers" and can breach its own floor); the Chhabra mapping; the haircut on the 2028
  deposit (contradicts the case); governance apparatus; the mission slogan; the letter to Laura; banned labels.
- **Accuracy problems a judge could catch:** the $140k riskless benchmark is a 4% figure (today ~$190-200k); "only US
  government credit risk remains" ignores reinvestment and NAV; "93% of contributions" mixes 2033 and 2027 dollars;
  Leibowitz-Weinberger is 1982, not 1981; the 64% equity-beats-zero figure is nearer 61% on a lognormal check; the
  August ERP is unverified (the 1 Nov 2026 figure is 4.41%).
