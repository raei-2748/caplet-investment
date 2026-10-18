# L03: Investment strategy red team ("Roots First" / Root-and-Branch and the WInS book)

Prepared Fri 16 Oct 2026 (Sydney). AI-prepared review for planning only, not submission text. Record it in the AI-use log. Do not copy its wording into the TNA, IPS or Final Report.

**Lens:** a hostile CFA-level portfolio manager plus a fixed-income specialist. The questions: does the plan really do what it says, would a judge find the gaps, and what must change before the strategy locks on 6 Nov?

**Why timing matters:** the official IPS brief says: "Once submitted, the IPS becomes the official record of your team's investment strategy. Your team may not revise its investment strategy after the submission deadline." (competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt:73-74). So every strategy fix below has to be decided and reflected in the IPS by **Fri 6 Nov 5:00 pm ET (Sat 7 Nov 09:00 Sydney)**. After that, the Final Report can only explain the strategy, not repair it.

**Labels:** MODEL = my computed estimate, not a market price. UNVERIFIED = I could not confirm it. "new / known-deeper / known-repeat" compares each finding with the 15 Oct team brief (scratchpad/oct14/final.md).

---

## 0. Bottom line (read this if nothing else)

The plan's skeleton is sound and defensible: Treasuries for every promise, stocks only for money nobody has been promised, and a 2031 range whose bottom is already owned. A professional would respect it. But a fixed-income specialist would find five technical holes, and all five are fixable before 6 Nov.

1. **"High degree of certainty" has not been tested on the securities Laura is actually allowed to buy.** The kit's "never short" results all use zero-coupon STRIPS, which have been banned since 6 Oct. On the WInS-listed holdings, about $45k of the $500k depends on reinvesting coupons. In the kit's own historical replay, at least one payment falls short in 65% of start months (STRAT-02).
2. **Most of that reinvestment risk arrives after the 2033 gift has been paid** (about $33k of the $45k). Yet IPS V5's shortfall order only handles a shortfall "expected in 2033". After 2033, the only cover left is Laura's kept half, and the kit's chain ends in "her own money", which the case forbids (STRAT-03).
3. **The ladder is sized rung by rung, with each rung's coupons reinvested in itself.** That is the most reinvestment-hungry way to build it. A standard cash-flow-matched (dedicated) portfolio that assumes waiting cash earns **0%** costs about **$309.6k** on the 15 Oct curve, and about **$304.1k** at 2%. So "certain even if coupons earn nothing" costs roughly $5-10k more than the $300k deposit, which the 2028 deposit can cover before the floor (STRAT-04). This is the cleanest available upgrade.
4. **The room under $300k has almost gone.** On the 15 Oct close the WInS-listed ladder costs **$298,628**, leaving **$1,372 (4.7bp)**. In 2026 it cost more than $300k on **182 of 198** trading days. The chance it is over $300k at year-end is about **44%** (MODEL). The IBTR note's "about 0.2 points" is now about 0.05. The "2027 money buys the payments, 2028 money buys the facility" story is now a coin flip (STRAT-01).
5. **The growth "branch" is economically tiny, and the team's own rival model shows All-Treasury giving the facility more at every percentile.** VT is about $35k, or 7.8% of all money. Its median gain over Treasuries by 2033 is about **$4.2k** (MODEL). Unless the branch is reframed as *Laura's flexibility fund* (which the case does ask for), a judge can call it decorative. Both COMPETITION.md:164 and V5:28 state the floor-vs-stocks trade-off backwards for the gift (STRAT-06).

---

## 1. Numbers I recomputed (all MODEL unless marked)

| # | Number | Value | Method / source |
|---|---|---|---|
| N1 | Par curve 15 Oct 2026 close | 1y 4.49, 2y 4.77, 5y 4.91, 7y 5.00, 10y 5.10, 20y 5.48, 30y 5.43 | home.treasury.gov daily par yield CSV, 2026, fetched 16 Oct 2026 (saved as lenses/L03/par2026.csv). The 10y fell 9bp in one day from 14 Oct (5.19). |
| N2 | Ladder cost on 1 Jan 2027, WInS-listed dates, "yields unchanged" (the IBTR note's basis) | 6 Oct $293,453 (22.7bp room); 14 Oct $295,993 (13.9bp); **15 Oct $298,628, room $1,372, 4.7bp** | The 15 Oct brief's own pricer (oct14/factcheck/ladder.py), re-run unchanged on the new curve: zero-coupon discounting to each holding's maturity date, bootstrapped par curve. Output: lenses/L03 run log. |
| N3 | Same, forward basis | 15 Oct $297,847, room $2,153, 7.4bp | Same pricer, forward to 1 Jan 2027. |
| N4 | Days in 2026 when the ladder cost more than $300k | **182 of 198** trading days (2 Jan cost $325,241) | Same pricer on every 2026 curve (lenses/L03/gapodds.py). |
| N5 | Chance the ladder costs more than $300k at 31 Dec 2026 | **about 44%** | Daily s.d. of log cost in 2026 = 0.433%, scaled to 53 trading days = 3.15% (about $9.4k), zero drift, normal. Expected top-up from 2028 about $3k; 95th percentile about $14k. Rough; fat tails would raise it. |
| N6 | What the ten WInS-listed holdings owe in coupons + principal if nothing is reinvested (0%) | **about $455k** of $500k (kit: $447k) | lenses/L03/cf_model.py. Each iBond is modelled as one coupon bond (iShares weighted-average coupon, 28 Sep) ending 15 Dec; each rung is sized to deliver $50k if coupons earn curve forwards. The kit's $447k (rab/numbers.yaml `reinvest.bookL_delivered`) models the funds differently. Either way, about $45-53k depends on reinvestment. |
| N7 | Delivered if reinvestment earns forwards −1pt / −2pt / flat 2% | $490.0k / $480.8k / $469.5k | Same model. |
| N8 | Part of the reinvestment dependence earned **after 1 Jan 2033** | **$32.6k of $45.2k (72%)** | Same model: reinvest at forwards until 1 Jan 2033, then 0% afterwards. |
| N9 | Pooled reserve, own-rung sizes: forwards before 2033 and forwards −2pt after | **−$10.0k** at the end of 2042 (forwards −2pt before 2033 only: −$1.3k; −2pt throughout: −$17.4k; 0% throughout: −$45.2k) | lenses/L03/pooled.py: one cash ledger with the payments drawn each 1 Jan. |
| N10 | Cost of a dedicated (cash-flow-matched) portfolio from the same 10 holdings, waiting cash carried at 0% / 1% / 2% / 3% | **$309.6k / $306.9k / $304.1k / $301.3k** (6 Oct curve: $304.6k / $301.9k / $299.1k / $296.4k) | lenses/L03/lp_carry.py: linear programme minimising cost subject to cumulative cash ≥ cumulative payments at each 1 Jan. Only these 10 WInS holdings; the full 43-bond WInS list might be cheaper (UNVERIFIED). |
| N11 | Own-rung sizing scaled up so that each rung pays $50k at 0% | about $327k | Same model. |
| N12 | Floor cost in Jan 2028 for $150k by 15 Dec 2032 | $117.0k at the 15 Oct forward (5.15%/yr); $129.6k at 3%; $123.4k at 4%; $112.1k at 6% | Discounting over 4.96 years. |
| N13 | VT sleeve with a $150k floor | **$35.2k = 7.8%** of the $450k | 150k − floor cost + 2027 leftover ($2.2k on 15 Oct). |
| N14 | VT in 2033 (JPM 2026 LTCMA AC World 7.00% compound, 16.78% vol; lognormal) | p5 $26.6k / p50 $49.4k / p95 $91.5k; mean $53.0k. Same money in Treasuries: $45.1k. **Median gain from stocks $4.2k; mean $7.8k** | lenses/L03/sleeve.py. LTCMA figures from CLAUDE.md "Key facts" (verified 27 Sep from competition/official_market_data/). |
| N15 | Gift (floor + half VT) and what Laura keeps, $150k floor | gift p5 $163k / p50 $175k / p95 $196k; Laura keeps p5 $13k / p50 $25k / p95 $46k | Same; before the cap and any shortfall. |
| N16 | Same with a $100k floor | gift p50 $152k; Laura keeps p50 $52k | Same. Shows that under the half rule **a bigger floor raises the median gift**. |
| N17 | Market value of a 10 × $50k reserve on 1 Jan 2033 at flat yields of 3% / 5% / 7% | $439k / $405k / $376k | Annuity-due, first payment immediate. |
| N18 | $150k floor in 2026 Taiwan building-cost terms | $118k at 3.54%/yr (average since 2021); $96k at 6.53%/yr (latest y/y); $126k at 2.5% US CPI | Seven years of compounding (2026 to 2033). Taiwan CCI from research/insight_v1/phase_A/fact_register.md:206 (F-508, DGBAS, derived). |
| N19 | USD/TWD | 31.94 on 9 Oct 2026. Volatility of daily changes 5.3%/yr (5y), 4.9% (since 2000). 6-year change in TWD vs USD since 1990: p5 −21.7%, median −1.2%, p95 **+12.4%**, max **+20.2%** | FRED DEXTAUS, fetched 16 Oct 2026 (lenses/L03/fx.py). |
| N20 | WInS rung size against Laura's rung | iBonds 0.676×, bonds 0.654-0.667× → each WInS rung pays about **$33-34k**, not $50k | rab/trades/tickets.md Portfolio vs Book L share and face counts (e.g. IBTO 1,016 vs 1,503). The filled quantities (COMPETITION.md:176-185) are within 1% of the tickets. |

---

## 2. Findings

### STRAT-01 · The $300k room has almost gone, so "2027 buys the payments" is now a coin flip · high · new
- **Problem.** The plan's opening line is that Laura's first $300k buys all ten payments. On the 15 Oct close that is barely true ($1,372 of room, 4.7bp; N2). In 2026 it was false on 182 of 198 days (N4). The chance it is false at year-end is about 44% (N5). The IBTR note, which is a suggested TNA pick, says "If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up the ladder" (team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15). On 15 Oct the trigger is about 0.05 points. IPS V5:24 still quotes "about $292,000" (the old STRIPS basis), and COMPETITION.md:153 says "about $293k on the 6 Oct curve". A judge who checks any recent curve will find the numbers stale.
- **Why it costs us.** It is not a strategy flaw: the rule "latest payments first, the 2028 deposit completes the rest" handles it. The risk is a credibility hit: a reflection or IPS sentence that is false on the day it is read, and a plan story that says "2027 = payments, 2028 = facility" when the 2028 deposit is likely to share the job.
- **Fix: what it must achieve.** (a) Describe the 2027 purchase as a rule that works either way, not a number. (b) If a number appears, give its date and basis, and pair it with the sensitivity: about $2.9k per 10bp (N2: 6 Oct to 15 Oct). (c) In the IBTR reflection, the "tested" story becomes stronger, not weaker: the test set on 6 Oct is now close to biting. Report what happened since the trade, with a date. (d) In the Final Report, state the 1 Jan 2027 curve assumption used for projections.
- **Deadline:** TNA Fri 23 Oct ET; IPS 6 Nov.

### STRAT-02 · "High degree of certainty" is defined and tested on banned instruments · critical · known-deeper
- **Problem.** The case requires teams to "define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions" (Laura_Gao_2026_Client_Profile.txt, page 3). IPS V5 never defines it. It asserts: "once bought, each payment depends mainly on the US government paying its debts" (01_version_5.md:20). The kit's evidence is mostly on the superseded zero-coupon basis:
  - tests 1 and 2 in rab/decisions/D_certainty_definition.md (history since 2000; 149 start years; 13 episodes) price STRIPS;
  - D_rivals.md says "Every plan's payments are modelled as zero-coupon (STRIPS) Treasuries";
  - D_stress_bad_year.md says "Payments, STRIPS basis ... paid in all 13 replayed episodes".
- The only test on the WInS-listed holdings is weak. "The ten total $500,000 only if coupons earn about 5% or more" (D_certainty_definition.md test 3). In the 1962-2011 replay, "starts with any payment short 387/593 (65%); total < $500k in 47%" (rab/redteam/ws7_assumptions_reinvest_check_output.txt, section [2], single build, UNVERIFIED). My model gives about $455k owed at 0% (N6).
- The 15 Oct brief repeats a STRIPS-era claim, "no payment is missed unless yields fall about 420bp" (oct14/final.md:580, :776). On the WInS basis that is wrong: payments fall short with **no** move before January if coupons later earn less than about 5%.
- **Why it costs us.** This is the case's first requirement and drives Investment Strategy and Client Knowledge scores. A fixed-income judge will spot that coupon bonds and iBond ETFs are not zeros. Worse, the WInS notes already admit it ("reinvested coupons fund the rest", 05_…md:18; "reinvested coupons funding part of each", :24), so the IPS sentence at V5:20 contradicts the team's own notes.
- **Fix: what it must achieve.** One sentence stating a standard that is literally true for the WInS-listed holdings, named before any number. The test is shown on those holdings, and the assumptions are listed. The strongest option is STRAT-04: "covered even if waiting cash earns 0% (or 2%)". Re-run the history and stress tests on the WInS-listed holdings before quoting any "never". Delete every STRIPS-basis "never short" figure from team materials, or label it.
- **Deadline:** IPS 6 Nov (the definition and principle); Final Report 4 Dec (the tests and figures).

### STRAT-03 · Most reinvestment risk lands after the gift is paid, and the shortfall order does not cover it · high · new
- **Problem.** V5:26: "Any shortfall expected in 2033 comes first from the 2027 leftover, then the half Laura keeps, then the contribution above the floor." COMPETITION.md:161 says the same. But about **72%** ($32.6k of $45.2k) of the reinvestment dependence is earned **after 1 Jan 2033** (N8). If reinvestment rates are 2 points below forwards only after 2033, the pooled reserve ends about **$10k short** (N9). By then:
  - the 2027 leftover has gone (into the 2033 reserve);
  - "the contribution above the floor" has been **paid to the facility in 2033** and cannot be clawed back;
  - only Laura's kept half remains, and in a bad stock outcome it is about $13k (p5; N15).
- The kit's own stress rule ends the chain with "beyond it, she adds her own money" (rab/decisions/D_stress_bad_year.md, rule 3). The case says "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this requirement" (Client_Profile p.3). The 15 Oct brief flagged the "her own money" wording (final.md:718) but not the timing problem.
- **Why it costs us.** It breaks the logic between "high certainty" and "responsible facility contribution". A judge who asks "what happens if rates fall in 2035?" gets no answer from V5.
- **Fix: what it must achieve.** A rule, set in the IPS, that covers shortfalls arising **after** 2033 without outside money. Options for the team (each has a cost):
  - (a) in 2033, before the gift, measure the remaining reinvestment exposure on that day's curve and add a named buffer to the operating reserve (D_certainty_definition.md's "triage D1 alternative");
  - (b) dedicate the ladder from the start so that no post-2033 reinvestment is needed (STRAT-04);
  - (c) state openly that Laura's kept half is held in Treasuries as the backstop until 2042, and size it.
- Whichever is chosen, the 2031 range's bottom ("rounded down after any expected shortfall", V5:30) must use the same rule and the same stress.
- **Deadline:** IPS 6 Nov.

### STRAT-04 · The ladder is built the reinvestment-hungry way; a dedicated version makes certainty literal for about $5-10k · high · new
- **Problem.** V5:26: "income reinvested in the holding that paid it". Each rung is sized alone, assuming its own coupons compound at today's yields to its own maturity (rab/trades/tickets.md Book L; rab/decisions/D_stress_bad_year.md rule 2). Pension "dedication" is the standard way to match fixed payments with coupon bonds. It sizes the whole set together, so later bonds' coupons pay earlier payments, and only short waits need reinvesting.
  - On the 15 Oct curve, a dedicated portfolio of the **same ten holdings** with waiting cash assumed to earn **0%** costs about **$309.6k** (N10). At 2% it costs **$304.1k**.
  - The own-rung design needs about **$327k** to be safe at 0% (N11).
  - The LP drops the Feb-2037 bond and the 2033 IBTM rung, because pre-2033 coupons kept as cash cover 2033. So the holdings change.
- **Why it matters.** This turns "high degree of certainty" from a claim into a testable, conservative standard: "every payment is paid even if every coupon earns nothing while it waits; only a US default breaks it". It costs about $5-10k of the 2028 deposit before the floor (the floor falls from about $150k to about $140-145k, MODEL). It is also distinctive. Few high-school teams will know dedication, and it can be explained in one sentence.
- **Fix: what it must achieve.** The team decides between (i) own-rung + an explicit buffer (STRAT-03a), (ii) dedication at a stated carry rate (0% or 2%), and (iii) keeping the current design and saying certainty depends on coupons earning about 5%. Under (ii), the WInS book can stay as it is (it is an illustration, and trades cost $25/$10). But the IPS principle and the Final Report numbers must follow the chosen rule, and the Final Report must explain any gap between the WInS book and the rule. Re-run the LP on the full WInS bond list (record all 43 bonds first; the list is not in the repo, wins_notes.csv "2032 Treasury" row) and on the curve the team adopts.
- **Confidence:** medium-high. The LP is mine (single build, 10 instruments, iBonds approximated as one bond each). Ask a second student to rebuild it before quoting.
- **Deadline:** decide by about Tue 27 Oct (vote set B), IPS 6 Nov.

### STRAT-05 · Laura's kept half is promised to three jobs and is small · high · new
- **Problem.** The same money is named as:
  - (1) the payments' backstop: V5:26; D_stress rule 3, "From the 2033 gift to the last payment she holds her half in Treasuries, not stocks";
  - (2) the inflation and Taiwan-dollar defence: V5:28, "Inflation or a stronger Taiwan dollar raises facility costs, and the equity half Laura keeps is her defense";
  - (3) the cushion "if costs rise or co-sponsors fall short" (V5:30).
- Its size: median about $25k, p5 about $13k (N15). In the kit's 2008 replay it is $18.4k and the coupon gap at 2% exceeds it by $12k (D_stress table). If rule 3 holds, it sits in Treasuries until 2042, so it is not "equity" after 2033 and not free for overruns. Laura's only other money is the ten-year reserve, and selling its long bonds early takes price risk (a duration of about 11 on the Nov-2041 bond: roughly −11% per 1-point rise).
- **Why it costs us.** The case stresses "financial flexibility ... as the project develops" (Client_Profile p.3). A judge will see the flexibility money counted two or three times.
- **Fix: what it must achieve.** Give each job one named source and size. Say which job takes priority when they collide (payments first, by the case). Remove "equity half" wording if the half is moved into Treasuries in 2033.
- **Deadline:** IPS 6 Nov.

### STRAT-06 · The growth branch is tiny, and the trade-off is stated backwards · high · known-deeper
- **Problem.**
  - VT is about $35k, 7.8% of all money (N13). Its median gain over Treasuries by 2033 is about $4.2k (mean $7.8k) (N14): about 1% of Laura's money.
  - The team's own rival model says All-Treasury "**For the facility alone it is better at every percentile** (gift $191k / $202k / $213k against $165k / $174k / $189k)" (rab/decisions/D_rivals.md, STRIPS basis).
  - Under the half rule, a bigger floor **raises** the median gift ($175k at a $150k floor vs $152k at $100k; N15-N16). Yet COMPETITION.md:164 says "less stock means a lower median contribution", and V5:28 says "Moving floor money into equities would raise the expected contribution". Both are wrong for the gift; they are only true for total money.
  - Darren's "too timid" challenge is still open (team/google_drive/strategy_notes.md: "the 'timid plan' criticism is still open"). The case describes Laura as "willing to take thoughtful risks" (Client_Profile p.2).
- **Why it costs us.** A hostile judge says: "91% Treasuries; the 'branch' adds $4k; your own model says drop it." It hits Investment Strategy and Client Knowledge.
- **Fix: what it must achieve.** Reframe the branch honestly: it is *Laura's flexibility money*, which the case asks for ("preserves appropriate financial flexibility", Client_Profile p.4). It is 100% stocks because nobody has been promised it, so her stated risk appetite applies there in full. Give the facility trade-off the right sign. Have one prepared answer to "why not all Treasuries?" (flexibility; the case says committing everything "could limit her financial flexibility"). Decide the floor size as a principle (STRAT-08), not by default.
- **Deadline:** IPS 6 Nov.

### STRAT-07 · "Confidence by construction" in the 2031 range can read as a tautology · medium · new
- **Problem.** The kit's chosen answer is that the gift lands in the range "by construction, if five things hold" (rab/decisions/D_range_confidence_2031.md). The gift is *defined* as floor + half the fund, capped at the top, so it cannot fall outside the range unless the floor fails. The case asks the team to "state how confident they are that her 2033 contribution will fall within that range" **and** "explain how favorable and unfavorable market outcomes could affect the amount" (Client_Profile p.3). The kit's own figures:
  - the range is narrow: typical top about $175k, so about $145k-$175k;
  - the gift lands at or near the top about 3 times in 4.
- **Why it costs us.** A judge may read "about 100%" as dodging the probability question. The co-sponsor reader also needs to know where in the range to plan.
- **Fix: what it must achieve.** In the Final Report, give both: the structural guarantee with its conditions, **and** where the gift is likely to land, with what moves it (stocks 2031-33; post-2031 coupon shortfall under STRAT-03's rule). All on the WInS-listed basis.
- **Deadline:** Final Report 4 Dec. The IPS needs only the principle.

### STRAT-08 · The floor-size rule and the 2027 → 2028 sequence can make the branch vanish · medium · known-deeper
- **Problem.** Two readings are still live: the floor is "sized to return that remainder" (V5:24) or "sized to return about $150k" (COMPETITION.md:155-156). The 15 Oct brief flagged this (final.md:431). The numbers show what is at stake. In Jan 2028 the floor costs $112k-$130k depending on yields (N12). Add a 2027 top-up of up to about $14k (p95, N5), and in a low-yield path VT can shrink to under $10k (for example $150k − $129.6k − $14k ≈ $6k at a 3% five-year yield). The 2031 range then collapses to almost a point. The kit's own stress memo says a fall of more than about 1 point before investing means "the fund is used up" (D_rivals.md, "What would change it").
- **Fix: what it must achieve.** One priority order written in the IPS: payments, then [floor or a minimum branch], then the rest. Also say what happens to the range and the 2031 message if the branch is very small. Test it at the Jan 2026 curve (ladder $325k; N4) as a real-world bad case.
- **Deadline:** IPS 6 Nov.

### STRAT-09 · iBond ETF mechanics are glossed · medium · known-deeper
- **Problem.** These are verified facts the IPS and notes treat loosely (iShares IBTR page, fetched 16 Oct 2026):
  - "the Funds do not seek to return any predetermined amount";
  - "In the final months of each Fund's operation, as the bonds it holds mature, its portfolio will transition to cash and cash-like instruments. As a result, its yield will tend to move toward prevailing money market rates";
  - the funds "will terminate on or about October or December 15";
  - expense ratio 0.07%.
- Consequences:
  - Each iBond rung has its *own* early-maturity wait. Weighted average maturity is 5.71 years for IBTM (about Jun 2032) and 9.55 years for IBTR (about May 2036), as of 14 Oct. So cash sits in money-market instruments for roughly 6-7 months, like the Feb-2037 bond's 10.5-month gap.
  - The 0.07% fee is not in any curve-based ladder cost: roughly $1-1.5k over the life of Laura's iBond rungs and floor (my rough estimate). That is the same size as today's whole $1.4k room.
  - About 60% of Laura's money (five rungs plus the floor) sits in one sponsor's iBond trusts. The credit is still Treasuries; the risk is operational or closure.
  - IBTR is young (inception 25 Mar 2026), but its net assets grew from $37.6m (28 Sep, rab/data/ishares/ibonds_facts.csv) to $109.1m (15 Oct). Early closure risk is low, but the fund prospectus terms on early termination are UNVERIFIED here.
- **Fix: what it must achieve.** One honest clause on what an iBond pays. Fees included in the ladder cost. V5's substitution rule ("substitute a Treasury maturing earlier", V5:26) checked against the fact that WInS lists no Treasury maturing between Feb 2031 and Feb 2036 (COMPETITION.md:93): for IBTO-IBTQ, the substitute is an earlier iBond, which means a longer wait in cash.
- **Deadline:** IPS 6 Nov (one clause); Final Report 4 Dec (detail).

### STRAT-10 · The WInS book is a scaled picture, but the notes read as if each holding pays $50k · medium · known-deeper
- **Problem.** Each WInS rung is about 0.65-0.68 of Laura's rung, so it pays about $33-34k, not $50k (N20). The notes say, for example, "IBTO is for Laura's second $50,000 payment" (05_…md:20), "IBTQ is for Laura's fourth $50,000 payment" (:22) and "IBTR is for Laura's fifth payment" (:15). Only the Nov-2041 note says "scaled to the model portfolio" (:24). VT was bought in Oct 2026, but in Laura's plan it is bought in Jan 2028. IBTM's 4,503 shares mix the 2033 rung with a 2028-floor stand-in bought 15 months early (COMPETITION.md:176).
- **Why it costs us.** A judge who multiplies shares by about $25 sees about $25k of face value, not $50k. Without one clear sentence the book looks wrong.
- **Fix: what it must achieve.** Every reflection and the IPS make the mapping explicit once: the WInS book = Laura's allocation after both deposits, scaled to $300k, so each rung is about two-thirds of a payment. The Final Report has a mapping table (WInS holding → Laura's holding → which payment or job).
- **Deadline:** TNA 23 Oct ET (the reflections are the first place a judge sees it).

### STRAT-11 · The operating reserve's "size" and how it changes are not pinned down · medium · new
- **Problem.** The case asks teams to "recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made" (Client_Profile p.3). The IPS brief asks for "managing the operating reserve's asset composition over time" (IPS-FINAL.txt:48-49). V5 says only: "In 2033 the payment Treasuries become the operating reserve, shrinking as each payment is made" (V5:26).
  - The reserve's market value on 1 Jan 2033 depends on 2033 yields: about $376k at 7%, $405k at 5%, $439k at 3% (N17). Yet it pays exactly $500k whatever happens (plus or minus reinvestment).
  - Cash from early maturities (iBond final months; Feb-2037 10.5 months early; May-2038 7.5 months early) needs a stated home. SGOV was on WInS on 28 Sep (wins_notes.csv ticker list), but cash is not on the 14 Oct permitted list (final.md:107).
  - Post-2033 coupons need a rule (STRAT-03/04).
- **Fix: what it must achieve.** In the IPS, the composition-change principle in plain words (runs off; waiting cash goes to [named type]; coupons go to [rule]). In the Final Report, the reserve size given two ways (face cash flows, and market value at a stated 2033 yield), with a per-year table.
- **Deadline:** IPS 6 Nov (principle); Final Report 4 Dec (size).

### STRAT-12 · Facility-cost inflation is named but not measured · medium · new
- **Problem.** The case asks teams to explain "the effect of inflation on portfolio projections and facility costs" (Client_Profile p.4). V5 has one clause (V5:28). The floor is nominal. $150k in 2033 buys what about **$118k** bought in 2026 at Taiwan's average building-cost inflation since 2021 (3.54%/yr), or about **$96k** at the latest +6.53% y/y (N18). The ten payments lose value too: the kit says the 2042 payment buys what $35,342 buys in 2027 at 2.34% inflation (D_stress_bad_year.md). That is out of scope for funding, since the case fixes them, but worth one line.
- **Fix: what it must achieve.** In the Final Report, state the inflation assumption (US CPI for projections; Taiwan construction cost for the facility), show the floor and the range in both nominal and 2026-cost terms, and say plainly that the nominal ladder is deliberate because the payments are nominal.
- **Deadline:** IPS (one principle) 6 Nov; Final Report 4 Dec.

### STRAT-13 · Taiwan-dollar risk is as big as the whole equity half and is not quantified · medium · new
- **Problem.** The money is in USD; the facility is in Taiwan. Over 6-year windows since 1990, the TWD rose against the USD by up to 20.2% (p95 +12.4%) and fell by up to about 22% (p5) (N19). A 12.4% TWD rise cuts the TWD value of a $175k gift by about 11%, roughly $19k. That is similar to the whole p5-p95 spread of the equity half ($13k-$46k; N15). Hedging is not available: derivatives are banned (COMPETITION.md:78). The kit noted this only as a Final Report item (rab/assumptions.md L10). The case never names a currency ("$").
- **Fix: what it must achieve.** In the Final Report, one stated assumption (amounts in USD; the range quoted in USD), one sentence on the size of the FX risk, and why it is not hedged. Note it as a co-sponsor-message point (quote in USD; co-sponsors bear conversion).
- **Deadline:** Final Report 4 Dec. One IPS clause is optional.

### STRAT-14 · TIPS and tax: easy points to bank · low · new
- **Problem/opportunity.** The obvious judge question "why not inflation-protected bonds?" has a strong answer the team already owns. The payments are fixed nominal ("each payment is a fixed $50,000 and is not adjusted for inflation", Client_Profile p.3), so nominal Treasuries match them exactly. The kit found a TIPS ladder would need to be "1.43 times the size, about $125k more" (D_rivals.md, STRIPS basis; re-run before quoting). Tax is out of scope: "teams do not need to account for personal income taxes, capital gains taxes, or the legal and regulatory requirements of establishing a residency in Taiwan" (Client_Profile p.4). So no words should be spent on iBond tax treatment.
- **Fix: what it must achieve.** One "considered and rejected" line each, in the Final Report.
- **Deadline:** Final Report 4 Dec.

### STRAT-15 · Overbuilt behind the scenes, under-explained on the page · medium · known-deeper
- **Problem.** The kit has 10 decision memos (rab/decisions/), about nine models (rab/models/M1-M9), gates A-D, and "1.6 million paths" (D_range_confidence_2031.md), mostly on the STRIPS basis. IPS V5 is missing items the IPS brief names: liquidity, return assumptions, the certainty definition, and reserve composition over time (IPS-FINAL.txt:45-50). The 2025-26 lesson in CLAUDE.md is "strategy packaging was over-complex for the insight".
- **Why it costs us.** Two failure modes. (1) The IPS reads as a bond ladder with no reasoning shown: "anyone could do this". (2) The Final Report drowns in model outputs that are on the wrong basis.
- **Fix: what it must achieve.** Pick three numbers that carry the argument and rebuild only those on the WInS basis: cost against the deposit; the certainty test; where the gift lands. Everything else goes to an appendix or is dropped. The "special" part is not the ladder. It is (a) a certainty standard that holds even if coupons earn nothing, (b) a range whose bottom is already owned and whose top is capped, so Laura cannot overpromise, and (c) every promise matched by a Treasury, with stocks only where nothing is promised. Each can be said in one sentence.
- **Deadline:** IPS 6 Nov; Final Report 4 Dec.

### STRAT-16 · Return assumptions rest on one house view, a year old · low · known-deeper
- **Problem.** All equity projections use the JPM 2026 LTCMA (data to 30 Sep 2025; CLAUDE.md "Key facts"; rab/assumptions.md E1 notes "the 2027 edition is due about October 2026"). I could not find a 2027 edition on 16 Oct (UNVERIFIED; web search returned only the 2026 edition). If it appears before 4 Dec, judges from asset managers may expect the current one. The 7.00% is a compound (median-type) figure; means are higher (N14).
- **Fix: what it must achieve.** In the Final Report, name the source and date, say compound vs arithmetic, and run one cross-check from a second house (the kit used a Vanguard-like 5.08%; rab/assumptions.md E1). Check JPM's page in late November.
- **Deadline:** Final Report 4 Dec.

### STRAT-17 · Long-bond timing and price risk: fine, but say why · low · known-repeat
- **Problem.** The Feb-2037 bond ends 10.5 months before its payment and May-2038 7.5 months before (05_…md:16-17). Waiting cash at 0-5% changes the outcome by only about $0-2k per rung (my estimate). Held to maturity, price swings do not matter. But the WInS book's value will swing with rates (the 15 Oct brief: about ±$9.5k for 0.5 points, final.md:592), and the Final Report's portfolio analysis will show it.
- **Fix: what it must achieve.** One sentence in the Final Report: value moves, the cash flows do not. Name where waiting cash sits.
- **Deadline:** Final Report 4 Dec.

---

## 3. "Is this just a bond ladder anyone could do?"

- **Yes, at the core.** Matching fixed payments with dated Treasuries is textbook liability-driven investing. Many teams will propose "bonds for the payments, stocks for growth".
- **What makes Caplet different, if the team says it:**
  - (1) It works inside the WInS-only rule: iBond ETFs fill the 2031-36 gap in the WInS bond list (COMPETITION.md:93).
  - (2) A certainty standard that is testable and conservative (STRAT-04).
  - (3) A 2031 range built so Laura cannot overpromise: owned bottom, capped top.
  - (4) It names its one real residual risk (coupon reinvestment) with a cover rule (STRAT-03).
- **What would look "stupid":** absolute words (already flagged in the 15 Oct brief); STRIPS-basis "never" figures; a growth story for a 7.8% sleeve; counting Laura's half three times; numbers that a curve from the last week contradicts.
- **What would be "special but not stupid":** say, in plain words, that coupons were treated as earning nothing and the payments still hold. Show one table where the facility gift, Laura's flexibility money and the payments each have their own source and their own worst case.

---

## 4. The five most dangerous technical weaknesses, and how to defend or fix each

| # | Weakness | Judge's attack | Fix (strategy, by 6 Nov) | Defence (if not fixed) |
|---|---|---|---|---|
| 1 | Certainty untested on WInS-listed holdings (STRAT-02) | "Your 'never short' figures use bonds you're not allowed to buy." | Adopt a stated standard (for example, covered even if waiting cash earns 0% or 2%) and test it on the real holdings | Admit about $45k depends on reinvestment, give the break-even (about 5%) and name the cover |
| 2 | Post-2033 reinvestment risk uncovered (STRAT-03) | "What pays a 2038 shortfall after the gift is gone?" | 2033 buffer set aside before the gift, or dedication from the start | Laura's half held in Treasuries to 2042 and sized; never "her own money" |
| 3 | Own-rung ladder vs dedication (STRAT-04) | "Why compound coupons for 15 years instead of using them for the next payment?" | Dedicate: about $304-310k (15 Oct), extra from the 2028 deposit before the floor | Show the reinvestment table and the cover rule |
| 4 | The $300k room has gone (STRAT-01) | "On today's curve your opening claim is false." | State the purchase as a rule; date every figure | The rule already says the 2028 deposit completes the ladder; give the about-44% chance openly |
| 5 | A tiny branch and a backwards trade-off (STRAT-06) | "Your own model says All-Treasury gives the facility more in every case." | Reframe the branch as Laura's flexibility money; fix the sign; decide the floor size by principle | Cite the case's flexibility requirement; show what Laura keeps (median about $25k) |

---

## 5. Checklist for the team (decisions, not wording)

- [ ] Re-run the ladder cost on the curve you will quote; date it (Mon 19 Oct).
- [ ] Vote: certainty standard (0% carry / 2% carry / "coupons at about 5%") and the ladder build (own-rung + buffer, or dedicated) (Tue 27 Oct).
- [ ] Vote: post-2033 shortfall rule, with no outside money (Tue 27 Oct).
- [ ] Vote: floor-size principle and priority order when yields are low (Tue 27 Oct).
- [ ] One source and one size for each of: payment backstop, overrun cushion, inflation/FX defence.
- [ ] A student rebuilds N2, N8, N10 and N14 independently before any is quoted.
- [ ] Record the full 43-bond WInS list (read-only) so the dedication can use the best bonds.
- [ ] Remove or label every STRIPS-basis "never short" claim in team files, including the 15 Oct brief's "420bp" line.
- [ ] TNA reflections: say the WInS book is scaled; date any room figure.

---

## Appendix: files and sources

- Scripts and outputs (all mine, MODEL): scratchpad/oct16/lenses/L03/ (cf_model.py + cf_1015.txt; pooled.py + pooled_1015.txt; lp_carry.py + lp_carry.txt; gapodds.py + gapodds.txt; sleeve.py + sleeve.txt; fx.py + fx.txt; ladder_prev.py, which is the 15 Oct pricer re-pointed at new dates).
- Data fetched 16 Oct 2026: home.treasury.gov daily par yield curve CSV (2026, through the 15 Oct close); FRED DEXTAUS CSV (through 9 Oct 2026); iShares IBTR, IBTM and IBTO product pages (key facts as of 14-15 Oct; risk text quoted from the IBTR page).
- Repo: competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt; 2026_WGY_Investment_Policy-FINAL.txt:41-78; team/google_drive/ips_report/01_version_5.md:16-30; 05_trading_note_reflection_wins_trading_notes.md:14-24; COMPETITION.md:93, :148-167, :172-190; rab/assumptions.md; rab/decisions/D_certainty_definition.md, D_range_confidence_2031.md, D_stress_bad_year.md, D_rivals.md, D_fund_choice.md; rab/redteam/ws7_assumptions_reinvest_check_output.txt; rab/trades/tickets.md; rab/data/ishares/ibonds_facts.csv; team/google_drive/sheets/portfolio_and_trading_notes/wins_notes.csv; research/insight_v1/phase_A/fact_register.md:206; team/google_drive/strategy_notes.md.
- UNVERIFIED: the 2027 JPM LTCMA; iBond early-termination terms; the full WInS bond list; whether cash or SGOV is permitted in Laura's real plan; the kit's 65%/47% replay figures (single build).
