# D8 Professional-Practice Benchmarker: our strategy against named industry frameworks

Agent D8, insight_v1 run, Phase D. Written 2026-09-27. Questions: M081 (tier 1), M006, M235, M109, M063, M026
(tier 2, with Final Report follow-ups). This is AI-generated research for Team Caplet, for brainstorming only. It
holds **no submission-ready prose**: rule specifications, evidence, numbers and "a strong sentence must contain"
checklists. The six students decide and write every word. Any framework named here that reaches the Final Report
must go in its Works Cited, together with how AI was used (R-W46).

Status labels (brief section 3): **VP** = VERIFIED-PRIMARY (I opened the page on 2026-09-27 with
`research/insight_v1/scripts/fetch_text.py` or curl), **VRF** = VERIFIED-REPO-FILE, **SNIP** = SNIPPET-UNVERIFIED,
**ASM** = ASSUMPTION. R-, F-, BS-, SH-, X- ids point to `research/insight_v1/phase_A/`.

Numbers script: `.venv/bin/python research/insight_v1/scripts/D8_practice_numbers.py` (docstring lists inputs and
labels; it reproduces the verified $292,264 ladder cost and the $394,930 reserve value first, as a check).

**Terms used (plain English)**
- **LDI (liability-driven investing):** investing so the assets move like a known future bill. Pension funds do it.
- **Surplus:** the money above the market price of the promise. **Funded ratio:** assets divided by that price.
- **Glide path:** a pre-set plan for shifting from growth assets into matching assets. Pensions usually trigger each
  step when the funded ratio crosses a set level (a **trigger point**), not on a calendar date.
- **Goals-based wealth management (GBWM):** one sub-portfolio per goal, each with its own horizon and its own
  acceptable chance of failure. Risk means "the chance of missing the goal".
- **Required return:** the yearly return a goal needs to be met. **Hurdle:** the return a riskier choice must beat.
- **Ability vs willingness to take risk:** ability (also called capacity for loss) is how big a fall the money can
  absorb without harming the goal; willingness is how much risk the person wants to take.
- **Rebalancing band:** a range around a target weight; you trade only when the weight leaves it.

---

## 0. Top findings (ranked by impact on reaching the semifinals and on making the plan unmistakably Laura's)

1. **The IPS needs four pre-declared rules, not three and not six (M006 + M235).** Professional IPS practice says it
   directly: the IPS offers "an objective course of action to be followed during periods of market disruption", and
   the process for changing it "should be clearly identified in advance" (CFA Institute 2010, VP). The Rules page
   binds teams to the Asset Manager Code, whose B.5.a says managers "Take only investment actions that are
   consistent with the stated objectives and constraints", and whose guidance says any flexibility "should be
   expressly understood and agreed to" beforehand (VP). The minimal set that covers all five case tests
   (R-C80-R-C84) is: **(1) promise first**: buy the ten payments with the first money; if they cost more than the
   money on hand, buy the latest-dated first and complete the rest from the 2028 deposit before anything else;
   **(2) growth mix with a yearly reset**; **(3) the 2031 range = what is already bought + a stated upside**;
   **(4) the 2033 order of use**: reserve, then a stated share for the facility, then flexibility. About 120-160 of
   the 500 words. Each extra rule must show a lift in a reported number or be dropped. The rebalancing rule passes
   that test: without it, the growth money's stock share wanders to 50-73% by 2031 (p5-p95), and about half of all
   paths leave a 55-65% band (script, ASM). Four professional precedents back the pattern: pension glide-path trigger
   points (BofA, VP), APRA's "shortfall limit" and "restoration plan" (VP), Yale's two-year lagged spending rule
   (VP) and Russell's 2026 "surplus glidepath" (VP).
2. **Laura's needs can be met at today's Treasury yields; stocks are for upside, not need (M109).** Across both
   deposits the ten payments need only **1.05%/yr**. On the first deposit alone they need **5.09%/yr**, which is
   exactly what the bought ladder earns (the 27bp headroom). About **$200k of 2033 facility money needs 4.81%/yr**
   on the growth money, below today's 5-year Treasury par yield (4.98%). A surplus held only in Treasuries at today's
   forward rates reaches **~$204k** in 2033. Stocks at 50/60/70% of the growth money add only about
   **+$9k/+$11k/+$12k** in a middle-case projection (ASM: JPM 7.00% equity, bonds at the 5.23% forward). Yet at 60%
   the modelled 1-in-20 bad case is $159k (F-407). The CFA IPS standard asks for exactly this statement, a "required
   ... growth rate ... to satisfy her future obligations" (VP). This does not change the architecture. It is strong
   devil's-advocate evidence for the open 50/60/70 decision, and it tells the team what the equity is *for*.
3. **Fees must be charged to the growth money, never to the bought payments (M026).** A typical U.S. adviser charges
   **1.00%** a year on accounts up to $1M, and all-in costs run about **1.75%** up to $500k (Kitces, reporting the
   Veres survey, 2017, VP). Taken *from the ladder*, a fee eats the headroom several times over: 0.15% = 0.6x,
   0.5% = 2.1x, 1.0% = 4.2x the $7,736 headroom (script, ASM). Charged on the growth money only, a 1.0% fee costs the
   2033 facility about $10k. Charged on all assets but paid from the growth money, it costs about $34k. The Code
   (F.4.d, VP) requires fee disclosure "in plain language", including gross- and net-of-fees returns. So: one IPS
   cost principle and one Final Report fee line with a sensitivity check.
4. **This is a goal-dedicated pool, and her ability to take risk differs by goal (M063).** The case puts her living
   costs "outside the portfolio" (R-C33). Under the Code's IPS guidance ("both the ability and willingness of the
   client to bear risk", VP) and the UK regulator's "capacity for loss" definition (VP), a loss on the surplus does not
   touch her standard of living. The payments, however, have **zero** capacity for loss, because the case bans
   outside money for them (R-C48). The IPS should say so and assume nothing about the size of her other wealth. It
   gives the risk-tolerance sentence a reason that belongs to her, without raising the equity weight.
5. **Chhabra's own words fix the team's bucket mapping and confirm "no tilts" in WInS now (M081).** In a 2016
   interview (VP), Chhabra says an aspirational portfolio needs "a certain skill set" and "doesn't have to be an
   investment ... being really good at what you do, your passion—that could be part of your aspirational
   portfolio". Laura's career, books and the residency are her aspirational bucket. Her 2028 deposit already rides on
   them (R-AN31). The portfolio should hold only safety (the ladder) and market (broad funds). The team notes map
   "aspirational = flexibility reserve (stays invested for growth)". That puts the most risk on the money whose job
   is to absorb surprises. That is backwards, and a judge who knows the framework would notice.

**Framework map (for the Final Report's strategy section; one table, cited there, not named in the IPS):**

| Framework (source, status) | What practitioners do | Our plan | Match? |
|---|---|---|---|
| Pension LDI, "surplus glidepath" (Russell, 2026-07, VP) | "lock down the benefits promised, then grow surplus assets"; "additional risk taken only on assets above a defined surplus threshold" | Ladder bought first; risk only in the growth money | Match |
| Pension glide-path triggers (BofA, VP; NISA, VP) | De-risk "at set trigger points" chosen in advance | Rules 1-4 are triggers fixed on Nov 6 | Match (rules are dated events plus one cost trigger, not funded-ratio levels, because the promise is already 100% hedged from day one) |
| APRA SPS 160 (VP) | Board-set "shortfall limit"; a "restoration plan" back to full funding within at most three years | Rule 1: if the ladder costs more than the cash, complete it from the 2028 deposit, first call on that money | Match in logic; our deadline is shorter (one year) |
| Yale spending rule (VP) | Spending set from the value "from two years ago", for predictable budgets | 2031 range built from money already bought, applied in 2033 | Match (ours is stricter: bought, not smoothed) |
| Goals-based WM (Brunel table in Das et al. 2018, VP; Chhabra 2015/2016, VP) | Needs at 90-95% success; aspirations in a separate risky bucket | Payments bought (above "needs"); no aspirational bucket in the portfolio | Match; deliberate difference explained in M081 |
| Brunel: longer-dated needs may take more risk (via B4b, VP) | Time-segmented buckets | We hedge all ten payments now, including 2042 | Deliberate difference: fixed nominal payments, no outside money (R-C48), duration already ~10y |
| CFA IPS elements, individual (2010, VP) | Required return; ability and willingness; known liabilities; rebalancing policy "documented"; review process "identified in advance"; a spending calculus that includes fees | M109 / M063 / M006 / M026 | Match once these items are added |
| CFA Asset Manager Code (VP; named in the Rules, R-W29) | Know the client (B.6.a); act within the stated mandate (B.5.a); plain fee disclosure (F.4.d) | Pre-set rules; fee principle | Match once the fee principle is added |

---

## 1. M081 (tier 1: WInS now; then IPS and FR). Is Laura's aspirational bucket already filled by her career?

**Question (canonical):** Under Chhabra's risk-allocation buckets, is Laura's aspirational bucket already filled by her
career, future books and the residency, so the portfolio should hold only safety (reserve) and market (broad sleeve)
assets and refuse thematic, single-stock or country tilts?

**One-sentence answer:** Yes. Chhabra's own published words put skill-based bets ("being really good at what you do,
your passion") in the aspirational bucket. Laura's creative business, her next books and the residency are that
bucket, and her 2028 deposit already depends on them. So the portfolio holds only a safety part (the bought payments)
and a market part (broad index funds): no Taiwan, AI, publishing or other themed tilt.

**Is it already answered?** The *decision* is. The wins_now ticket (section 1: "No leverage, inverse, thematic or
single-country funds ... A Taiwan tilt would be tokenism") and `S2_growth_sleeve.md` already drop EWT and tilts. What
is new: (a) primary-source wording replaces the SNIPPET used in Phase B; (b) the team's own notes mislabel the buckets,
and that must be fixed before any teammate uses the framework in writing.

**Evidence**
| Claim | Source | Status |
|---|---|---|
| "you should only have an aspirational portfolio if you have a certain skill set. Your education could be your aspirational portfolio. It doesn't have to be an investment. Specializing, being really good at what you do, your passion—that could be part of your aspirational portfolio." | Chhabra interview, WealthManagement.com, published 2016-05-13 (datePublished in page metadata): https://www.wealthmanagement.com/investment-news/q-a-with-ashvin-chhabra-you-re-investing-all-wrong (accessed 2026-09-27) | VP |
| "Everybody needs a safety portfolio. You should have a market portfolio because it's too expensive to have a safety portfolio. And then you may have an aspirational portfolio." | same | VP |
| "For those things you must do, the emphasis is going to be on lowering the risk of your not achieving these goals ... The goals you aspire to may require a somewhat higher level of risk." Three questions: safety / comfortable / aspire | CFA Institute Enterprising Investor, 2015-08-05: https://blogs.cfainstitute.org/investor/2015/08/05/ashvin-chhabra-on-wealth-management-the-value-proposition-lies-in-understanding-client-goals/ (accessed 2026-09-27) | VP |
| The 2005 paper: "risk allocation must precede asset allocation"; it includes "human capital" among the assets | Quoted by Princeton Info (secondary): https://princetoninfo.com/business/beat-the-market-consider-your-risks-and-asset-allocation/ (accessed 2026-09-27). Original paper: SSRN 403 / pm-research blocked | VP for the secondary page; the paper text itself is SNIP |
| Aspirational examples "owning a small business, or leveraging unique human capital ... entrepreneur" | Search summary only | SNIP (do not quote) |
| Team notes map "Aspirational risk bucket = flexibility reserve (stays invested for growth; dry powder)" | `research/council_2026-09-27/team_notes_2026-09-27.md` L15-18 | VRF |
| Case: "Although she has been willing to take thoughtful risks throughout her entrepreneurial career, she wants her investment team to recommend an appropriate balance between pursuing growth and protecting the capital required for her goals." | case p.2 (R-C37, R-AN16) | VRF |
| The 2028 deposit comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures", all from her own work | case p.2 (R-C27, R-AN31) | VRF |
| Flexibility is for "as the project develops" | case p.3 (R-C58) | VRF |

**Numbers:** $150,000 of the $450,000 in contributions (33%) comes from her own career (case, arithmetic). In a
middle-case projection that share is 100% of the money above the ladder (F-409: the sleeve is ~34% of assets after
2028). So the facility money already rides on her human capital before any stock is bought.

**Why the team mapping is backwards (devil's advocate):** flexibility money exists to absorb surprises "as the project
develops" (overruns, delays). In Chhabra's scheme it is closer to *safety* than to *aspiration*. Putting it in the
riskiest bucket means the money for bad news is most likely to be down when bad news arrives. Corrected mapping:
safety = the bought payments (and, from 2031, the bought facility floor); market = the growth money (broad index +
short Treasuries); aspirational = outside the portfolio (her career, books, the residency itself).

**Implication**
- **WInS-now (decision, unchanged):** no tilts. Keep VT (or VTI+VXUS) and VGSH as in the ticket, PENDING WInS
  AVAILABILITY + POSITION-LIMIT CHECK; alternates in the ticket's section 6. Nothing to trade differently.
- **TN (checklist):** the growth-note reflection can carry the reason in one clause: "one broad index because her own
  career already carries her concentrated bets". No framework name, no quote (D13 rules: no Laura quotes in TN/IPS).
- **IPS (sentence spec):** the risk-tolerance sentence must contain (1) her willingness ("thoughtful risks", the
  case's words), (2) where her big bets already are (career, and hence the 2028 deposit), (3) the consequence (the
  portfolio protects the promise and holds broad market risk only). No framework names (no citations allowed).
- **FR (sentence + table):** name Chhabra once, with the corrected mapping, cited to the 2016 interview and the 2015
  CFA piece. Fix the team notes before anyone uses them.

**Deadline tier:** 1 (confirms WInS now; nothing to change). **Confidence:** high on the direction; medium on
presenting the framework (the 2005 paper was not read directly). **Changes current strategy:** no. **Criterion:**
Client Knowledge and Objectives. **What this teaches:** a framework is only as good as its mapping. Put each bucket
where its *job* is, not where its *name* sounds right.

---

## 2. M006 (tier 2: IPS; applied in FR). Which "if X, then Y" rules must the IPS pre-declare?

**Question (canonical):** Which contingent rules (rates fall before Jan 2027; 2028 deposit smaller or late; 2031 floor;
2033 reserve; facility share), each with trigger, action and record, must the IPS pre-declare before the Nov 6 freeze
so the Final Report's numbers read as applications of the IPS rather than a redesign after results?

**One-sentence answer:** Four rules, each a trigger, an action and a record, about 120-160 words in total: (1) promise
first (with the rates-fall and 2028-shortfall branches inside it), (2) the growth mix and its yearly reset, (3) the
2031 range = bought floor + stated upside, (4) the 2033 order of use (reserve, facility share, flexibility), plus one
governance line (rules change only at a scheduled review, never because markets moved).

**Evidence (professional practice)**
| Claim | Source | Status |
|---|---|---|
| "Perhaps most importantly, the IPS serves as a policy guide that can offer an objective course of action to be followed during periods of market disruption when emotional or instinctive responses might otherwise motivate less prudent actions." | CFA Institute, *Elements of an Investment Policy Statement for Individual Investors*, May 2010, p.1: https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf (accessed 2026-09-27) | VP |
| "A process for refreshing the IPS as investor circumstances and/or market conditions change should be clearly identified in advance." (element 2b) | same, p.6 | VP |
| "Outside boundaries of acceptable variations from targets ... should be documented in the IPS ... If the policy is not to rebalance, this policy should be documented in the IPS." (element 4c) | same, p.17 | VP |
| B.5.a "Take only investment actions that are consistent with the stated objectives and constraints of that portfolio or fund." Guidance: flexibility "is not improper but should be expressly understood and agreed to by Managers and clients." | CFA Institute *Asset Manager Code*, 2nd ed. (©2009, 2010), p.11-12: https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/amc/asset-manager-code-and-guidance-2nd-ed.pdf (accessed 2026-09-27) | VP |
| Rules page: "All teams should review the CFA Institute's Asset Manager Code and operate by these standards." | R-W29 via Phase A | VP (via A1) |
| Glide paths: "Meet fiduciary obligations without constant committee oversight by establishing a long-term framework for future de-risking at set trigger points." | BofA, "What You Need to Know About Glidepaths for Pension Plans": https://business.bofa.com/en-us/content/workplace-benefits/glidepaths-for-pension-plans.html (accessed 2026-09-27) | VP |
| "Fiduciaries must determine the appropriate trigger points for de-risking trades." | NISA, Dynamic LDI overview: https://www.nisa.com/perspectives/dldi/ (accessed 2026-09-27) | VP |
| Shortfall limit: the fund "can be restored to a satisfactory financial position within one year"; restoration plan within a period that "must not exceed three years" | APRA SPS 160: https://handbook.apra.gov.au/standard/sps-160 (accessed 2026-09-27) | VP |
| "we apply the targeted spending rate (5.25%) to the endowment's year-end value from two years ago" | Yale Provost: https://provost.yale.edu/how-exactly-does-spending-policy-work (accessed 2026-09-27) | VP |
| "lock down the benefits promised, then grow surplus assets with a prudent process"; "Any surplus strategy should preserve benefit security first, with additional risk taken only on assets above a defined surplus threshold." | Russell Investments, 2026-07: https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html (accessed 2026-09-27) | VP |
| "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten simply because markets move or hindsight reveals a different outcome." / "you may not redesign your strategy after observing the results" | `competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt` L156-158 (Guide p.5) | VRF |
| "Your team may not revise its investment strategy after the submission deadline." | IPS guide L73-74 (R-I35) | VRF |
| Laura's money arrives 2027-01-01, after the freeze; the ladder cost > $300k on 173 of 185 trading days of 2026; P(cost > $300k on 2027-01-01) ~24% | F-111 (VP inputs); F-112 (ASM) | as labelled |

**The rule specification (trigger / action / record). Parameters in [brackets] are team decisions; the words are the
team's own.**
| # | Trigger | Action | Record (what the FR later shows "fired as written") | Case test covered |
|---|---|---|---|---|
| 1 Promise first | Cash arrives (Jan 2027; Jan 2028) | Buy Treasuries maturing for the ten payments before anything else. If they cost more than the cash on hand: buy the latest-dated payments first; the 2028 deposit completes the rest before any money goes to growth. If the 2028 deposit is smaller or late: the promise is still completed first; only the facility range shrinks; the bought payments are never sold | Purchase-day cost vs cash (trigger = observed cost, not a model probability: stats skeptic, M006); funded ratio on each date | 1 (certainty), 3 (uncertainty for the payments) |
| 2 Growth mix | Once a year [or when outside the band] | Reset the growth money to [60/40] stocks/short Treasuries; band [55-65] | Yearly weights | 3 (the risk held is the risk stated) |
| 3 The 2031 range | 2031-01-01 | Buy [share] of the growth money as a 2-year Treasury maturing before 2033; that bought amount is the bottom of the range; the top = [stated percentile] of the rest; confidence stated | Floor bought; range; confidence | 3, 4 (communicate) |
| 4 2033 order of use | 2033-01-01 | Reserve = the ladder, held to maturity (nothing sold; this is the "no rebalancing" policy CFA 4c asks to be written down); facility = the bought floor + [share] of what is left; the rest kept as project flexibility | Reserve value, facility amount, flexibility kept | 2 (responsible), 5 (flexibility) |
| G Governance | A scheduled yearly review | Rules change only at the review, for a change in Laura's circumstances, never because markets moved | Dated decision log (M021) | Guide p.5; Code B.5.a |

**Numbers:** word budget ASM: 4 rules x 25-35 words + governance 10-15 words ≈ 110-155 of 500. The rates-fall branch
matters in ~24% of modelled paths (F-112, ASM) and in 173 of 185 real 2026 trading days (F-111, VP inputs).

**Implication**
- **IPS (decision):** adopt the four-rule structure. Fix every bracketed parameter by Nov 6. The IPS guide does not
  expect the final range or reserve numbers (L68-70), but a *rule* whose parameter is chosen after Nov 6 is a
  redesign. The IPS should name the parameter (for example "a fixed share of the growth money") even if the dollar
  outcome comes in the FR.
- **FR (sentence + table):** one table, "rule / what happened / what it produced", for the Articulation criterion.
  The Final Report applies the rules; it never adds one. Compare the four precedents in one line each at most.
- **WInS-now:** none new; the ticket's "never" rules and band are the WInS version of rules 1-2.
- **Open parameter left to the team:** latest-dated-first vs nearest-first (brief s9). Practice evidence (APRA) is
  about *having* a restoration rule, not its order. The ordering argument stays with D1/D3.

**Deadline tier:** 2. **Confidence:** high (the structure); medium (parameter values are team choices).
**Changes current strategy:** no (it formalises it). **Criterion:** Investment Strategy (with Articulation in the FR).
**What this teaches:** a professional plan decides what it will do in bad times *before* they happen. That is the
whole purpose of an IPS, and it is what protects a client from her adviser's hindsight.

---

## 3. M235 (tier 2: IPS). What is the smallest rule set that passes all five case tests?

**Question (canonical):** What is the smallest set of rules that still passes all five case tests, and can each extra
rule show a measurable improvement?

**One-sentence answer:** Four rules (M006 table: promise first, growth mix, 2031 range, 2033 order of use). Three is
too few, because without the 2033 order-of-use rule, tests 2 and 5 (responsible facility, flexibility) have no rule and
the 2033 decision would be made after results. Every other candidate (a TWD quote, a Taiwan tilt, calendar glide
paths, ratchets, extra bands) is either Final Report presentation or must show a lift in a reported number.

**Is it mis-posed?** Partly. The stats skeptic is right that "measurable lift" is false precision for wording choices.
So the test applies to *rules* (things that move money), not to *presentation* (a second-currency quote is FR
communication, not a rule). Merged with M006 in practice; kept separate here only for the lift test.

**Test matrix (case p.4 tests, R-C80-R-C84, VRF)**
| Test | Rule 1 promise first | Rule 2 growth mix | Rule 3 2031 range | Rule 4 2033 order | Covered without the rule? |
|---|---|---|---|---|---|
| 1 Payments with high certainty | Yes | - | - | (holds ladder to maturity) | No |
| 2 Responsible facility contribution | - | - | (feeds) | Yes | No: dropping rule 4 fails test 2 |
| 3 Uncertainty for both goals | Payments | Facility risk as stated | Facility | - | Partly |
| 4 Communicate clearly and credibly | - | - | Yes | - | No |
| 5 Preserve flexibility | - | - | - | Yes | No: dropping rule 4 fails test 5 |

**Lift of each candidate extra rule**
| Candidate | Lift (number) | Verdict |
|---|---|---|
| Rebalancing band (rule 2) | Without it, the growth money's stock share on 2031-01-01 is p5 50% / p50 62% / p95 73%, and 49% of paths sit outside 55-65% (script, ASM: JPM AC World 7.00% compound, 16.78% vol; bonds 3.9%, 2% vol; 100k paths) | Keep (one clause). It makes the risk held equal the risk stated (CFA 4c; Code B.5.a). Its *median* lift is ~0 (F-407: 50-70% moves the median by only $2-4k) |
| Calendar glide path on the reserve | None: the ladder already shortens itself as rungs mature | Drop as a rule. Answer the IPS prompt ("composition change as payments approach") with rule 4's hold-to-maturity line |
| Funded-status ratchet 2028-2031 (B4a Q16) | Not modelled; a lift of a few $k at p5 would not earn its place | Drop unless D3 shows ≥ ~$10k at p5 |
| Taiwan/AI tilt | Negative (M081) | Drop |
| TWD second quote of the range | Not a money rule | FR communication only |
| Yearly funded-ratio report | Not a money rule | FR presentation (Code F.2 clarity) |

**Implication:** IPS decision: four rules plus one governance line. FR: a one-line "why no other rules" note in the
Articulation section, which also answers last year's lesson (complexity must earn its place).

**Deadline tier:** 2. **Confidence:** medium-high. **Changes current strategy:** no. **Criterion:** Investment
Strategy. **What this teaches:** a rule earns its place by covering a test nothing else covers, or by moving a number
you report. Everything else is decoration.

---

## 4. M109 (tier 2: IPS; FR numbers). Required return per goal instead of one portfolio target?

**Question (canonical):** What is Laura's required return per goal (payments: the locked Treasury rate, only ~1.05%/yr
across both deposits; facility: a stated hurdle), and should the IPS say her needs can be met below today's Treasury
yield instead of setting one portfolio return target?

**One-sentence answer:** Yes. The payments need 1.05%/yr across both deposits (5.09%/yr on the first deposit alone,
which the bought ladder earns). About $200k of facility money needs 4.81%/yr on the growth money, below today's 5-year
Treasury par yield of 4.98%. So stocks are there for facility money *above* roughly $200k and for the case's
"pursuing growth". The IPS should state a required return for the promise and a hoped-for return for the facility,
not one portfolio target.

**Evidence**
| Claim | Source | Status |
|---|---|---|
| IPS element 3b: "State the overall investment performance objective ... likely to incorporate descriptions of general funding needs"; example: "a required real growth rate of 4 percent to satisfy her future obligations" | CFA IPS elements 2010, p.9 (URL above) | VP |
| The case states no return target (R-AN17); an IPS "outlines an investor's financial goals, risk tolerance" (R-I2) | case; IPS guide L3 | VRF |
| Case flows | F-601 | VRF |
| Treasury par curve 2026-09-25: 5y 4.98%, 7y 5.06% | `competition/official_market_data/daily-treasury-rates_2026-09.csv` | VRF |
| JPM 2026 LTCMA AC World 7.00% compound; data as of 2025-09-30, when the 10y was ~100bp lower than today, so its bond numbers look ~1pp conservative | brief s6/s14 | VRF / as labelled |

**Numbers** (`D8_practice_numbers.py`; IRRs are exact arithmetic on VRF flows; projections ASM)
| Goal | Required return |
|---|---|
| Ten payments, both deposits | 1.05%/yr |
| Ten payments, first deposit only | 5.09%/yr (= the ladder's own yield; the 27bp headroom) |
| Payments + facility $50k / $100k / $150k / $165k / $200k / $250k | 2.10 / 3.15 / 4.20 / 4.52 / 5.25 / 6.28%/yr (whole portfolio) |
| Growth money only, for facility money of $175k / $200k / $207k / $225k / $250k in 2033 | 2.08 / 4.81 / 5.53 / 7.29 / 9.55%/yr |
| Surplus held only in Treasuries at today's forwards (2027 leftover x 1.3513; 2028 deposit x 1.2903 = 5.23%/yr) | **$203,998** in 2033 |
| Middle case, growth money 50/60/70% stocks (JPM 7.00%) + bonds at the 5.23% forward | $212.9k / $214.7k / $216.5k (**+$8.9k / +$10.7k / +$12.5k** vs Treasury-only) |
| Verified model, 60% stocks (JPM bonds, lower than today's yields) | p5/p50/p95 $159k / $207k / $273k (F-401, F-407) |

**Caveats (must travel with the numbers):** the 5.23% forward for 2028-2033 is the market's break-even today, *not*
lockable for the 2028 deposit (no derivatives; she does not have that money yet). The IRRs assume the 2028 deposit
arrives in full (F-403/F-404 cover the shortfall cases). The verified model's median ($207k) sits almost exactly at the
Treasury-only figure because its bond inputs (JPM, 2025 data) are about 1pp below today's yields (brief s14). A
consistent-input comparison is the +$9-12k line above.

**Devil's advocate (for the open 50/60/70 decision, brief s9):** at today's yields, 60% stocks buy about +$11k of
middle-case facility money and cost about $45k in a 1-in-20 bad case (≈ $204k Treasury-forward vs $159k model p5;
the two figures come from different input sets, so read this as an order of magnitude). This does **not** decide the
weight. The case explicitly asks for "an appropriate balance between pursuing growth and protecting the capital"
(R-C37), and some growth exposure answers that. But it is the strongest single argument for the low end of the band,
and the team should be able to say it in their own words.

**Implication**
- **IPS (sentence spec):** the return-objective sentence must contain (1) the promise's required return = what the
  bought Treasuries earn (no number needed); (2) the facility's hoped-for return, with stocks named as the source of
  upside above what Treasuries alone would provide; (3) that no single portfolio return target is used, because the
  goals differ.
- **FR (number + chart):** a "required return per goal" line in the client picture. Chart candidate: a bar chart of
  the 2033 facility money under Treasury-only vs 50/60/70% stocks (median and p5), from one consistent model run
  (D3 to align the model's bond inputs with today's curve first).
- **Decision input:** sleeve equity weight (open); the 2031 range top.

**Deadline tier:** 2. **Confidence:** high on the IRRs; medium on the projections (ASM returns). **Changes current
strategy:** not the architecture. It weakens the case for 60-70% stocks and should be put to the team as a devil's
advocate point before Nov 6. **Criterion:** Client Knowledge and Objectives (with Investment Strategy). **What this
teaches:** first ask what return each goal *needs*. Only then decide how much risk to take to earn more than that.

---

## 5. M063 (tier 2: IPS). One goal-dedicated pool, or all her wealth?

**Question (canonical):** Is this portfolio all of Laura's investable wealth or one goal-dedicated pool (the case says she
has resources outside it), and should the IPS say so and let that raise her capacity to take risk with the surplus?

**One-sentence answer:** It is a goal-dedicated pool. The IPS should say so and split her ability to take risk by goal:
none for the ten payments (the case forbids outside money for them), real but bounded for the surplus (no living cost
depends on it). It should assume nothing about the size of her outside wealth, so this sharpens the risk-tolerance
sentence without raising the stock weight.

**Evidence**
| Claim | Source | Status |
|---|---|---|
| "Laura's living expenses and short-term financial needs will be covered by income and financial resources outside the portfolio." | case p.2 (R-C33) | VRF |
| "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this requirement." | case p.3 (R-C48) | VRF |
| An IPS should discuss "risk tolerances (both the ability and willingness of the client to bear risk), return objectives, time horizon, liquidity requirements, liabilities"; suitability is judged "in the context of the rest of the client's portfolio" | Asset Manager Code, B.6.a guidance, p.12 | VP |
| "Where possible, the IPS should account for known liabilities to lend some quantitative basis to the risk tolerance assessment." Multiple risk levels: "avoiding financial catastrophe, maintaining a current standard of living, meeting a specific future financial goal, or developing significant further wealth" | CFA IPS elements 2010, element 3c, p.11 | VP |
| "By 'capacity for loss' we refer to the customer's ability to absorb falls in the value of their investment. If any loss of capital would have a materially detrimental effect on their standard of living, this should be taken into account" | UK FSA FG11/05 *Assessing suitability* (2011), footnote 3: https://www.fca.org.uk/publication/finalised-guidance/fsa-fg11-05.pdf (accessed 2026-09-27) | VP |
| GBWM treats goals as separate "mental accounts" | Das et al. 2018, JOIM 16(3): https://srdas.github.io/Papers/GBWM.pdf (accessed 2026-09-27) | VP |
| "While the client is real, the financial scenario is developed specifically for the competition." | R-W4 | VP (via A1) |

**Numbers:** no new number is needed. F-407: stocks at 50/60/70% of the growth money give a median of
$205k/$207k/$209k and a p5 of $164k/$159k/$154k (VRF script). Whatever the outside wealth, the choice moves the median
by about ±$2k. One limit on capacity: in 2027 the only surplus is $7,736 (F-104), and the 2028 deposit depends on her
career, which is the same risk as a bad year for publishing and speaking (wrong-way risk, R-AN31). So her capacity is
lowest *before* the deposit arrives, and that is exactly when the plan holds almost no stocks (F-409).

**Implication**
- **IPS (sentence spec):** the risk-tolerance sentence must contain (1) the pool's single purpose (the residency
  goals; her living costs are met elsewhere); (2) ability by goal (none for the payments; bounded for the surplus);
  (3) willingness in the case's words ("thoughtful risks", "appropriate balance"); (4) no reliance on unstated outside
  wealth.
- **FR:** one line in the client picture; pair it with M081 (her big bets are outside the portfolio).
- **Kill:** any argument like "she can afford losses because she has other money". The case gives no size, and the
  scenario is fictional (R-W4).

**Deadline tier:** 2. **Confidence:** high. **Changes current strategy:** no. **Criterion:** Client Knowledge and
Objectives. **What this teaches:** risk tolerance is not one number per person. It is one number per goal, and
"ability" and "willingness" can point in different directions.

---

## 6. M026 (tier 2: IPS principle; FR numbers). What fee, and who pays it?

**Question (canonical):** What fee would a real adviser disclose for Laura's ~$450k, and should the IPS say the reserve
is held as directly owned Treasuries needing almost no management, with fees charged on or paid only from the growth
sleeve so the ladder's ~$7.7k headroom is never eroded?

**One-sentence answer:** A typical U.S. adviser would quote about 1.00% a year at this size (all-in about 1.75% with
fund and platform costs, per the Veres survey reported by Kitces). Because a fee taken from the bought payments would
exceed the $7,736 headroom (0.5%/yr ≈ 2.1x it), the IPS should state one cost principle: the bought payments carry no
ongoing fee and all costs are paid from the growth money. The Final Report should show projections net of a stated
fee, with a sensitivity check.

**Evidence**
| Claim | Source | Status |
|---|---|---|
| "the median advisory fee up to $1M of assets under management really is 1%"; under $250k the median is "almost 1.25%"; median all-in cost "1.75% for portfolios up to $500k, 1.65% up to $1M"; "the typical 1% AUM fee is really more of a 0.50% investment management fee, plus a 0.50% financial planning fee" | Kitces, "Financial Advisor Fees Comparison – All-In Costs For The Typical Financial Advisor?", 2017-07-31 (reporting Bob Veres' Inside Information survey of nearly 1,000 advisors): https://www.kitces.com/blog/independent-financial-advisor-fees-comparison-typical-aum-wealth-management-fee/ (accessed 2026-09-27) | VP for what Kitces reports; the survey is 2017 (dated; a current level is ASM) |
| F.4.d "Management fees and other investment costs charged to investors ..."; guidance: "At a minimum, Managers should provide clients with gross- and net-of-fees returns"; "Managers must not only use plain language ..."; "must disclose to prospective clients the average or expected expenses or fees clients are likely to incur" | Asset Manager Code, p.21 | VP |
| A "spending calculus" that "reconciles investment return objectives, fees, taxes, inflation, and anticipated spending"; the example uses "fees of 1.2 percent" | CFA IPS elements 2010, p.10 | VP |
| Case: "At the beginning of 2027, Laura plans to invest $300,000 with an asset management firm." Fees are not mentioned; taxes are excluded | case p.2 (R-C26), p.4 | VRF |
| Fund costs: IEF 0.15%; VT 0.06%; VGSH 0.03% | wins_now ticket s1 (issuer pages) | VP (via S3) |
| No projection in the repo includes a fee | BS-01 | VRF |

**Numbers** (`D8_practice_numbers.py`, ASM: growth money 60% stocks at 7.00% + 40% short Treasuries at 3.9% =
5.76%/yr; fee charged at the start of each year; ladder at forward values)
| Fee | On growth money only | On all assets, paid from growth money | Taken from the ladder, 2027-42 (PV at 2027) |
|---|---|---|---|
| 0 | facility money 2033 $209.3k | - | - |
| 0.15% (IEF-type fund expense) | - | - | $4.8k = 0.6x headroom |
| 0.25% | -$2.6k | -$8.6k | - |
| 0.50% | -$5.2k | -$17.1k | $16.1k = 2.1x headroom |
| 1.00% | -$10.4k | -$33.9k | $32.3k = 4.2x headroom |
Other checks: in 2027, a 1.0% fee on all assets is $3,000 against a $7,736 surplus, so it fits for one year. Product
cost of the growth money with VT/VGSH: about 0.05%/yr. The STRIPS ladder has no ongoing fund fee.

**Implication**
- **IPS (sentence spec, one clause):** it must contain (1) the bought payments are held directly to maturity, with no
  ongoing management charge; (2) every cost is paid from the growth money, so costs can never reduce the promise;
  (3) low cost as a principle. Do not state a fee number in the IPS.
- **FR (number):** state one base-case fee assumption and show the facility range net of it. Suggested base (ASM, team
  decides): 1.0% on the growth money plus fund costs (≈ -$10k); sensitivity: 1.0% on all assets paid from the growth
  money (≈ -$34k). Show gross and net per Code F.4.d. The 2031 range must be quoted net of fees, or it overpromises
  (R-C66).
- **WInS-now:** nothing new. The real WInS cost is $25 per ETF trade (F-607), covered by the 1% cash float.

**Deadline tier:** 2 (IPS clause); numbers tier 3. **Confidence:** high on the principle; medium on the level (the fee
survey is from 2017). **Changes current strategy:** no. It adds a principle and lowers FR facility figures by ~$5-34k
depending on the stated fee. **Criterion:** Portfolio Analysis (with Investment Strategy). **What this teaches:** a
fee that looks small in percent can be large next to a thin margin of safety. Always compare costs with the headroom
they eat, not with the whole balance.

---

## 7. Sources (all accessed 2026-09-27 with `fetch_text.py` or curl unless marked)
| Source | URL / path | Status |
|---|---|---|
| CFA Institute, *Elements of an IPS for Individual Investors* (May 2010) | https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf | VP |
| CFA Institute, *Asset Manager Code*, 2nd ed. (©2009, 2010) | https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/amc/asset-manager-code-and-guidance-2nd-ed.pdf | VP |
| Kitces, Financial Advisor Fees Comparison (2017-07-31) | https://www.kitces.com/blog/independent-financial-advisor-fees-comparison-typical-aum-wealth-management-fee/ | VP |
| Chhabra interview, WealthManagement.com (2016-05-13) | https://www.wealthmanagement.com/investment-news/q-a-with-ashvin-chhabra-you-re-investing-all-wrong | VP |
| CFA Institute Enterprising Investor on Chhabra (2015-08-05) | https://blogs.cfainstitute.org/investor/2015/08/05/ashvin-chhabra-on-wealth-management-the-value-proposition-lies-in-understanding-client-goals/ | VP |
| Princeton Info on "Beyond Markowitz" (secondary) | https://princetoninfo.com/business/beat-the-market-consider-your-risks-and-asset-allocation/ | VP (secondary) |
| Chhabra (2005), *Journal of Wealth Management* 7(4) | https://www.ssrn.com/abstract=925138 | Blocked (SSRN 403); SNIP |
| Das, Ostrov, Radhakrishnan & Srivastav (2018), JOIM 16(3) | https://srdas.github.io/Papers/GBWM.pdf | VP |
| Russell Investments, pension surplus investing (2026-07) | https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html | VP |
| BofA, glidepaths for pension plans | https://business.bofa.com/en-us/content/workplace-benefits/glidepaths-for-pension-plans.html | VP |
| NISA, Dynamic LDI | https://www.nisa.com/perspectives/dldi/ | VP |
| APRA SPS 160 | https://handbook.apra.gov.au/standard/sps-160 | VP |
| Yale Provost, spending policy | https://provost.yale.edu/how-exactly-does-spending-policy-work | VP |
| UK FSA FG11/05, *Assessing suitability* | https://www.fca.org.uk/publication/finalised-guidance/fsa-fg11-05.pdf | VP |
| Search results used only to find URLs (Kitces, Chhabra, glide paths) | WebSearch 2026-09-27 | SNIP where not re-opened |
| Case, IPS guide, Competition Guide | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`; `2026_WGY_Investment_Policy-FINAL.txt`; `2026_WGY_Investment_Competition_Guide.txt` L156-158 | VRF |
| Curve, verified model outputs | `competition/official_market_data/daily-treasury-rates_2026-09.csv`; `research/insight_v1/phase_A/fact_register.md` F-101-F-112, F-401-F-409 | VRF |
| Prior agents reused (and re-verified here where marked VP) | `research/insight_v1/phase_B/B4a_practice_benchmark.md`, `B4b_practice_benchmark.md`; `phase_A/stakeholder_map.md` BS-01, BS-02, SH-25; `wins_now/securities_and_allocation_v0.md` | VRF |

## What this teaches
1. **Professionals write the rules before the storm.** Every framework checked here (the CFA IPS standard, pension
   glide paths, Australia's restoration plans, Yale's spending rule) fixes its triggers in advance. Laura's plan
   earns trust the same way: four rules set on Nov 6 and applied, not invented, in December.
2. **Ask what each goal needs before asking how much risk to take.** Her promise needs about 1% a year; about $200k of
   facility money needs less than today's Treasury yield. Stocks are a choice for upside, and the team should say so
   plainly.
3. **Risk tolerance is per goal.** No outside money may fund the payments, so they can bear no loss. The surplus can
   bear some, because her living costs do not depend on it.
4. **Map frameworks by job, not by name.** Her career is her aspirational bucket; money kept for surprises belongs
   with safety.
5. **Compare costs with the margin they eat.** 0.5% a year sounds small. Taken from the ladder, it is twice the
   ladder's safety margin.
