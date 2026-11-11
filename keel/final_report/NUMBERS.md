# The number register (Tue 10 Nov 2026)

Every figure the Final Report may use comes from this page. It uses one curve, one engine and Caplet's design as
submitted. These are research notes, not report text.

**What changed on Tue 10 Nov.**
- **Morning.** Keel made two calls at 07:04 (`../pm/ASK_HUMANS.md`), and every script that depends on them was re-run.
  - **The completion standard is "sufficient without reinvestment"** (design H_plain, card Q20). It replaces Mon 9 Nov's "design A sized for rates 3 points lower", which is kept as the alternative.
  - **The 2031 range follows one rule** (card Q19): each end is what its fund pays if no more interest is earned; there is a cap; and no figure is stated before the move.
- **Afternoon.** An independent bond desk check (`research/panel/2026-11-10_bond_desk_register_check.md`) confirmed the central sums and found looser words around them. Every finding is applied:
  - **A fee cushion (finding 3).** The backstop is now sized so the ten are paid if no coupon earns anything, after the fee of the Treasury-bill ETF where every waiting dollar sits. It costs $885 more; at 0% it has $1,414 to spare.
  - **The range on the fund's own holdings (finding 1).** Each stated end is worked out from the late-2032 fund's own holdings on the trade day and cut by 0.5% before rounding down. It is then re-tested on holdings and frictions the rule does not assume, and "certain" is worded only as far as that test supports.
  - **Keel's reading of "most" (finding 2).** The floor gets the larger of 73.3% of what is left and $75,001 (section 4).
  - **Smaller items.** The escrow release counts coupons waiting in the ETF at their value that day (finding 4). Money left after 2042 is put into 2033 money at each world's own rates (finding 5). Wording items 6 to 12 are applied.
- **Re-run:** sections 2, 3, 4 and 5, and 8a, 8b, 8c, 8d, 8f, 8h and 8i. **Unchanged:** section 1, 8e and 8g. Section 0 gains rows. Section 6 lists every figure now void, this morning's included, and section 10 lists the files that still quote one.
- **Evening (numbers owner).** Two sections added; nothing is re-sized and no earlier figure moves.
  - **8j, the Taiwan dollar test,** re-run on section 4's one definition of the gift (the 2033 contribution after the cap). The half kept alone covers a 10% stronger Taiwan dollar in 93.2% of house paths; with the excess the cap sends to it, in 99.77%; on the real Taiwan dollar since 1983, in 98.1% and 99.8% of windows.
  - **8k, what returns to Laura:** $75,298 in 1 Jan 2033 money at today's forwards (the backstop's $45,456, the excess $8,476, the half kept $21,347), 12.8% of all the money. A second calculation by value conservation (`numbers/returns_check.py`) agrees to $1.48.
  - Two loose lines fixed: 8g's VT share (6.63% of the $450,000, not 7.45%) and section 3's fee, now with its money year.
  - `joint_stress` re-run: only its `twd_test` block changed, and it gains `returns_to_laura`; every other figure in it is identical.
- **The headline now:**
  - completion **$38,282** in January 2028; floor payout **$103,178**;
  - central range **$95,000 to $115,000** (unrounded $98,729 to $118,443); contribution **$115,000**; excess **$8,476**; half kept **$21,347**;
  - reserve **$444,545** on 1 Jan 2033, **111.4%** funded;
  - **$74,123** left by 2042 if forward rates hold, or $45,456 in 2033 money.

**Stamp.** Everything here is MODEL, meaning Keel's calculation and not a forecast or a promise.
- **Curve.** US Treasury daily par yield curve at the close on Fri 6 Nov 2026, the day trading froze. Source: treasury.gov CSV, copied to `competition/official_market_data/daily-treasury-rates_2026-11-06.csv`.
- **Valuation.** Values are forward to 1 Jan 2027 unless a line says otherwise.
- **Design.** Caplet's FINAL IPS as submitted (`FINAL_IPS_as_submitted.txt`), using the frozen WInS book's instruments.
- **Engine.** The scripts are in `numbers/`:
  - `engine.py`: the curve, the instruments and reinvestment;
  - `plan.py`: 2027 to 2033, with Keel's reading of "most";
  - `completion.py`: the completion standard (with the fee cushion) and the range rule (on the fund's holdings), which every script reads from here;
  - `run_numbers.py`: sections 1 to 5;
  - `returns_check.py` (Tue 10 Nov evening): the independent check of 8k.
- **Results.** `numbers/results_2026-11-10.json`, plus `results_reserve_`, `results_range_rule_`, `results_joint_stress_`, `results_kept_half_`, `results_extras_` and `results_real_2026-11-10.json`, all rewritten Tue 10 Nov afternoon (`results_joint_stress_` again in the evening, 8j and 8k), and `results_returns_2026-11-10.json` (evening). The Mon 9 Nov files (`results_2026-11-06.json` and the undated `results_*.json`) are kept as the record of the old call.
- **Rerun.** From the repo root, run `python3 -I keel/final_report/numbers/<script>.py` for `run_numbers`, `reserve`, `range_rule`, `joint_stress`, `returns_check`, `kept_half`, `extras` and `real_values`, in that order. Each needs only numpy; `extras` takes about two minutes, the others under a minute.
  - Adding `--design KEEL` to any of the first six reproduces Mon 9 Nov's standard on the same code and writes `*_KEEL.json`.
  - `pooled.py` (card Q20) is the record of the comparison at 0%, with the old fixed deductions.

Rule for every later note and draft: a figure not on this page is not used. A figure here that changes is changed here first, with the date.

## 0. Inputs and where each comes from

| Input | Value | Source |
|---|---|---|
| Treasury curve | 1y 4.33, 2y 4.51, 3y 4.59, 5y 4.64, 7y 4.74, 10y 4.86, 20y 5.29, 30y 5.26 (%) | treasury.gov par yield curve, 6 Nov 2026 |
| Curve method | Par yields read as semiannual, bootstrapped on a half-year grid, log-linear discount factors | Same as `keel/scripts/ladder_pv.py` and `ladder_history.py`; reproduces their $301,544 exactly |
| The ten instruments | IBTM, IBTO, IBTP, IBTQ, IBTR for 2033-37; T-bonds 4.750% 15 Feb 2037, 4.500% 15 May 2038, 4.375% 15 Nov 2039, 4.250% 15 Nov 2040, 3.125% 15 Nov 2041 for 2038-42 | Frozen WInS book (`competition/wins/2026-10-23_snapshot.md`) |
| iBond funds | End "on or about" 15 Dec of their year; "do not seek to return any predetermined amount"; monthly distributions; 0.07% fee; IBTM average coupon 3.50%, average maturity 5.69 years, yield to maturity 4.86% (23 Oct) | ishares.com IBTM page, read Mon 9 Nov 2026 |
| Fund holdings' average maturity | IBTM 5.65, IBTO 6.62, IBTP 7.66, IBTQ 8.65, IBTR 9.53 years (4 Nov) | ishares.com, recorded in `keel/scripts/holdings_ladder.py` |
| Fund coupons in the model | The curve's par yield to each fund's average maturity (IBTM: 4.2513%, fixed on the 6 Nov curve). This is higher than IBTM's real 3.50% coupon. It is the cautious choice for reinvestment and for the range rule's zero-interest payout (section 3) | Assumption |
| Floor and VT split of the 2028 money (Keel's reading of "most", Tue 10 Nov afternoon) | The floor gets the larger of 73.3% of what is left after the ladder is complete and just over half the deposit ($75,001 of $150,000; all of what is left if that is less); VT takes the rest | 73.3%: frozen WInS book, 3,361 IBTM shares as floor stand-in ($72,766 at fill) against 167 VT ($26,525). FINAL says "Most of the 2028 deposit will fund a Treasury fund maturing in late 2032" (IPS l.15); the $75,001 floor is Keel's call (section 4) |
| Shares | VT median growth 7.5% a year; 17.88% yearly spread | J.P. Morgan 2027 LTCMA, USD matrix (estimates as of 30 Sep 2026; row "AC World Equity 7.50 8.94 17.88", read 9 Nov 2026), the TNA's 7.5%; until 9 Nov the spread was the 2026 edition's 16.78% (house figures moved by at most $2,100) |
| VT fee | 0.06% | TNA note 3 |
| Yield moves, 2026-2031 | Parallel, s.d. 0.9 points a year, independent of shares | MODEL assumption, as `keel/scripts/sail_mc.py` |
| Rate history | FRED DGS1 (1-year Treasury), daily from 1962, as monthly averages | `archive/rab/data/fred/DGS1.csv` |
| Stock history | Shiller monthly S&P Composite with dividends, 1871 to Jun 2023 | `keel/models/data/shiller_monthly.csv` (mirror; `keel/models/data/SOURCES.md`) |
| Completion standard (Tue 10 Nov) | "Sufficient without reinvestment": the ten rungs at plain size plus a pooled backstop, sized so all ten are paid even if no coupon, fund payout or waiting dollar earns anything from 2027, after the waiting ETF's fee (next row) | Keel's call, `../pm/ASK_HUMANS.md` Tue 10 Nov 07:04; card Q20 (design H_plain); fee cushion: bond desk check, finding 3; `numbers/completion.py` |
| Where waiting money sits, and its fee | A Treasury-bill ETF (0 to 3 months), not a 1-3 year fund whose price can fall. Every coupon, fund payout and carried surplus waits there (TNA note 1 puts the Feb-2037 bond's proceeds in a short-term Treasury ETF). The design test charges 0.15% a year on every waiting dollar; in the forward-rate world the money earns forward short rates | Keel's call. Which ETF is UNVERIFIED: Laura's plan may use only WInS-listed ETFs (6 Oct email), so a student checks the listing |
| Range rule (Tue 10 Nov) | Each end is the money put into the late-2032 fund times what $1 of the fund's holdings pays on 15 Dec 2032 if nothing earns interest from the trade day, less 0.5%, rounded down to $5,000; capped (section 3) | Keel's call 07:04, card Q19; holdings and haircut: bond desk check, finding 1; `completion.rule` |
| The range rule's holdings | The engine's IBTM bond (coupon 4.2513%, average maturity 5.65 years), its remaining coupons and principal less the fund fee, priced on the trade day's curve (today's forwards, moved), rates floored at zero. Coupons of 3.50% (IBTM's real average) and 4.00% are test variants | Engine; ishares.com (row 4) |
| Haircut on each end | 0.5% of its zero-interest value, before rounding down. It carries the fund risks a bond does not have: an ETF bought above its net asset value, bid-ask spreads, an expense change made with notice | Bond desk check, finding 1; Keel's call |
| Percentiles of stated figures | Stated (rounded) ends are read without interpolating between two $5,000 steps (numpy method "lower") | Bond desk check, finding 9 |

## 1. The ladder's cost now (CASE_MAP C3): settled

| Figure | Value | Note |
|---|---|---|
| Ten $50,000 payments, curve basis | **$301,544** | 6 Nov close; 5 Nov $302,163; 23 Oct $297,636 (`ladder_history.py`). `holdings_ladder.py` gives $302,137 for 5 Nov by a second method (its own pricer); the $26 gap is method, not market |
| The ten instruments, with the iBond funds' 0.07% fee | **$302,287** | Engine, own-rung sizing at today's forward rates |
| Duration / cost of one basis point: the ten payments | 9.94 years / $300 | Engine |
| Duration / cost of one basis point: the instruments actually held | 7.76 years / $234 | Engine. Shorter than the payments because coupons arrive early; the gap is the reinvestment risk of section 2, and why TNA note 1's "duration-matching" needs explaining |
| If yields fall before 1 Jan 2027 by 0.25 / 0.5 / 1 / 2 points | $309,906 / $317,742 / $334,092 / $369,710 | Engine, instruments re-sized on the shifted curve |
| Chance yields fall by more than 0.5 points before 1 Jan 2027 | About 8% | House model (0.9 points a year), MODEL |
| Fall before 1 Jan 2027 that would use the whole 2028 deposit | 3.89 points | Engine |

So the FINAL's words hold as written. The ten cost "roughly $300,000", and the 2028 deposit's first dollars finish the
ladder. At the 6 Nov close that is $2,287 in 1 Jan 2027 money, or about $2,400 by Jan 2028. **Build order (Keel's reading; the IPS is silent):** longest rungs first, because they move most with yields; so any part still unbought in January 2027 is the 2033 rung (IBTM), finished in January 2028. Said once with the WInS
note on IBTO ("one of the first payments we would top up", CANON D17): earliest rungs first, IBTM then IBTO.

The rungs at today's forward rates (amount bought on 1 Jan 2027, and its cost):

| Pays | Instrument | Units (fund dollars or bond face) | Cost |
|---|---|---|---|
| 2033 | IBTM | $37,908 | $37,908 |
| 2034 | IBTO | $36,065 | $36,065 |
| 2035 | IBTP | $34,300 | $34,300 |
| 2036 | IBTQ | $32,588 | $32,588 |
| 2037 | IBTR | $30,922 | $30,922 |
| 2038 | 4.750% 15 Feb 2037 | $28,930 face | $29,136 |
| 2039 | 4.500% 15 May 2038 | $28,483 face | $27,567 |
| 2040 | 4.375% 15 Nov 2039 | $27,536 face | $26,051 |
| 2041 | 4.250% 15 Nov 2040 | $26,550 face | $24,582 |
| 2042 | 3.125% 15 Nov 2041 | $29,021 face | $23,168 |

Each rung reaches $50,000 only with its interest reinvested on the way. That is section 2.

## 2. Reinvestment (CASE_MAP C1): settled, with Keel's call of Tue 10 Nov

**What the risk is.** The ten pay interest long before the payments start. By 1 Jan 2033 that interest is worth
**$93,941**, nearly two of the ten payments. To turn today's $302,287 into ten payments of $50,000, every coupon must
be reinvested at today's forward rates. If rates later fall, the ladder pays less. The case's "high degree of
certainty" and the IPS's "pay what they say" both depend on this. TNA note 1 already names the risk for one bond's
10.5-month gap.

**How it was tested.**
- *Falls for good:* every rate after purchase is lower by 1, 2 or 3 points, floored at zero.
- *Interest earns nothing:* every coupon, every fund payout and every dollar waiting for a payment is held as cash.
- *Fee on waiting money (Tue 10 Nov afternoon):* the same, but every waiting dollar also loses a Treasury-bill ETF's fee, 0.15% a year.
- *History replay:* 585 windows of 16 years, one starting each month from Jan 1962 to Sep 2010. Each window's path of the 1-year Treasury yield is applied in proportion to today's forward rates, the method of `keel/models/ASSUMPTIONS.md` A35.
- *New York Regulation 126:* the seven interest scenarios an insurer's asset adequacy test uses (card Q20).
- *Policy:* in design A, each coupon is reinvested on the day it arrives into a Treasury maturing before its payment, and any surplus carries to the next payment. In design B and in the backstop, each coupon waits for the next payment due.
- **The history and the insurer tests are not separate evidence for a design that passes at 0%.** None of them takes a rate below zero, so they follow from the one 0% test.

| Design | Cost (1 Jan 2027) | Bought in Jan 2027 | Short in total if rates fall 1 / 2 / 3 points for good | Short if interest earns nothing | History: windows with any shortfall | History: median / 1-in-20 / worst shortfall |
|---|---|---|---|---|---|---|
| **A. The ten as written, sized at today's forward rates** | $302,287 | 10 | $12,172 / $23,509 / $34,083 | $54,595 ($55,920 with the ETF fee) | 55.6% | $1,592 / $34,555 / $45,266 (start Jul 2007) |
| A, sized for rates 1 point lower | $309,456 | 10 | $0 / $11,650 / $22,516 | $43,599 ($44,959) | 39.1% | $0 / $22,991 / $34,016 |
| A, sized for rates 2 points lower | $316,508 | 10 | $0 / $0 / $11,151 | $32,794 ($34,189) | 14.0% | $0 / $11,630 / $22,963 |
| A, sized for rates 3 points lower (Mon 9 Nov call, now the alternative) | $323,436 | 10 | $0 / $0 / $0 | $22,192 ($23,621 with the ETF fee) | 6.0% (35 of 585) | $0 / $1,225 / $12,117 (start Jul 2007) |
| A, sized so interest is never needed | $337,836 | 10 | $0 | $0 ($1,503 with the ETF fee) | 0% | $0 |
| B. Cash-flow matched (each coupon pays the next payment due), at forward rates | $302,029 | 8 | $5,500 / $10,725 / $15,690 | $25,007 ($25,674) | 58.3% | $2,913 / $15,925 / $19,584 |
| B, sized so interest is never needed | $319,687 | 8 | $0 | $0 ($714 with the ETF fee) | 0% | $0 |
| H_plain sized at exactly 0% (Tue 10 Nov morning; comparison only) | $335,771 | 10 (the backstop in Jan 2028) | $0 / $0 / $0 | $0, with nothing spare; $1,411 short with the ETF fee | 0% | $0 / $0 / $0 |
| **H_plain. The ten as written plus a pooled backstop, sized so interest is never needed after the ETF's fee (Keel's call)** | **$336,656** | **10** (the backstop in Jan 2028) | **$0 / $0 / $0** | **$0, with $1,414 spare; $0 with the ETF fee** | **0% (0 of 585)** | **$0 / $0 / $0**; all seven Regulation 126 scenarios $0 (they follow from the 0% test) |

Findings:
1. **The ladder as written needs a completion standard.** Sized at today's forward rates, it falls short somewhere in more than
   half of the historical windows. The shortfall is usually small (median $1,592), but 1 time in 20 it is $34,555,
   about 7% of the $500,000, and its worst is $45,266.
2. **The bond desk's answer (B) halves the risk at the same cost, but contradicts the IPS.** In B, the long bonds'
   coupons pay 2033 and 2034, so the 2033 and 2034 funds are never bought in January. That breaks "In January 2027
   we'll use your first deposit to buy 10 Treasuries" and TNA note 2's IBTM for "her first $50,000 payment". It stays
   in the store as the alternative a bond reader would expect, not as the plan.
3. **Keel's call (Tue 10 Nov 07:04, `../pm/ASK_HUMANS.md`; it replaces Mon 9 Nov's): "sufficient without
   reinvestment"**, the escrow verifier's arithmetic (paid even if no coupon earns anything), applied to holdings an
   escrow would not accept (card Q17; design H_plain, card Q20). A municipal escrow verifier credits only direct
   Treasuries and uninvested cash; here five rungs, $4,521 of the backstop (IBTQ and IBTR) and all waiting money are ETFs.
   - **Each payment has its own Treasury; a shared reserve of extra Treasuries pays any gap if interest earns nothing.** The ten stay exactly as written. They are bought in January 2027 at their plain size, sized at today's forward rates; the $2,287 still unbought is finished in January 2028. Each Treasury's own coupons are reinvested for its own payment, as the Trading Notes say ("reinvested coupons fund the rest").
   - **The backstop.** In January 2028 the deposit's first dollars also buy extra face in the same Treasuries. Its coupons and principal wait in the Treasury-bill ETF for the next payment due, and any money above a payment carries forward there. It is the cheapest such backstop (an exact linear programme) that pays all ten if nothing earns a cent and every waiting dollar, the own rungs' included, loses 0.15% a year:

     | Holding | IBTQ | IBTR | 4.750% Feb 2037 | 4.500% May 2038 | 4.375% Nov 2039 | 4.250% Nov 2040 | 3.125% Nov 2041 | Total |
     |---|---|---|---|---|---|---|---|---|
     | Extra (fund dollars or face) | $420 | $4,101 | $5,603 | $6,003 | $6,152 | $7,284 | $7,304 | |
     | Cost (1 Jan 2027 value) | $420 | $4,101 | $5,643 | $5,810 | $5,820 | $6,744 | $5,831 | **$34,369** |

   - **The fee cushion.** It costs $885 more than the backstop sized at exactly 0% this morning ($33,484), which would be $1,411 short if waiting money paid that fee. The bond desk's upper bound for the cushion was $1,078. At 0% the design now has **$1,414 to spare** after 2042.
   - **What it costs:**
     - $336,656 in 1 Jan 2027 money, $13,220 more than Mon 9 Nov's call;
     - the whole completion in January 2028 is **$38,282**: the $2,388 tail plus the backstop ($35,894), at January 2028 prices on today's forwards.
   - **What it buys:** all ten paid in full if no coupon earns anything, after fees on waiting cash. The history and insurer tests follow from that one test. So the ten are paid:
     - if rates are 1, 2 or 3 points lower for good;
     - if nothing earns any interest;
     - in all 585 historical windows;
     - in all seven Regulation 126 scenarios.
   - **Where the gap money comes from at 0%.** The own rungs pay what is theirs. The payments of 2033 to 2036 also take $2,587, $3,180, $3,756 and $4,451 of backstop money: distributions and coupons of the extra IBTQ, IBTR and T-bonds, which mature 2035-2041. That is pooling confined to the extra face. Do not write "no payment depends on another bond".
   - **What it costs the gift:** the floor payout is $103,178, against $115,929 under Mon 9 Nov's call and $136,328 with no margin at all. The central stated range is $95,000 to $115,000 (section 4).
   - **When rates don't fall,** the backstop is not lost. Its money waits in the ETF and is Laura's: $74,123 by 1 Jan 2042 if it all stays, worth $45,456 in 1 Jan 2033 money (8h).
   - **Why this keeps to the IPS:** "Even if yields fall and the total cost of the ladder ends up being above $300,000, we'll simply complete it with the 2028 deposit." And "barring a US default, none of your 10 operating payments will depend on a share price" now holds in every test.
   - Any student can overrule this and return to the cheaper margin.
4. **The alternative: Mon 9 Nov's call** (design A sized for reinvestment 3 points below forwards; $323,436, a margin of
   $21,149; completion $24,475 in January 2028).
   - **Why it was replaced:**
     - it leaves the ten $22,192 short if interest earns nothing ($23,621 with the ETF fee);
     - it is short in 35 of 585 historical windows (6.0%; worst $12,117, start Jul 2007);
     - in those worlds the only money left to pay the gap is the half of VT kept, so the IPS's "none of your 10 operating payments will depend on a share price" would fail there.
   - **What it would give:** under the same range rule, a stated range $15,000 higher at each end ($110,000 to $130,000 central; unrounded $110,930 to $133,081).
   - `--design KEEL` reproduces it on every script.

**The certain designs Keel weighed** (card Q20, `numbers/pooled.py`, MODEL). Each one pays all ten if interest earns
nothing; these costs are sized at exactly 0%, so the call is compared at its 0% size ($335,771) and the fee cushion adds $885:

| Design | Cost (1 Jan 2027) | Why it is not the call |
|---|---|---|
| H_plain sized at 0% (the call before its fee cushion) | $335,771 | |
| P100: all ten at full plain size, pooled (every coupon pays the next payment due) | $332,922 | $2,849 cheaper, but it pools at forward rates too: the Nov-2039 bond's own cash is 57% of the 2040 payment ($28,741), while H_plain pools only the extra face |
| P25 / P50 / P75: pooled, each rung at least that share of its plain size | $320,707 / $322,352 / $325,569 | Cheaper, for the same reason as P100, and the rungs are no longer the sizes the frozen book shows |
| A sized so interest is never needed | $337,836 | $2,065 dearer; "reinvested coupons fund the rest" becomes a rest of zero |
| The backstop on Mon 9 Nov's rung sizes | $337,000 | $1,229 dearer |
| B sized so interest is never needed | $319,687 | Buys only eight in January 2027 |

## 3. An iBond fund pays its net asset value, not par (CASE_MAP C2): settled

| Fund (pays) | Fund fee over its life, on a $50,000 rung | Months its holdings' money waits in cash before the end | Lost if that cash earns nothing |
|---|---|---|---|
| IBTM (2033) | $170 | 5.4 | $869 (1.7%) |
| IBTO (2034) | $196 | 6.4 | $1,000 (2.0%) |
| IBTP (2035) | $221 | 5.4 | $807 (1.6%) |
| IBTQ (2036) | $245 | 5.4 | $781 (1.6%) |
| IBTR (2037) | $266 | 7.4 | $1,043 (2.1%) |

- The fee is already in the engine's $302,287. Across the five funds it is $1,098 in the money of each payment year (the column above), or $743 in 1 Jan 2027 money: $302,287 against the payments' $301,544, since the T-bonds carry no fee (checked in `numbers/returns_check.py`, Tue 10 Nov evening).
- What is left is the cash wait. In its final months a fund holds cash, and that cash earns whatever short rates are then. This is why the payout "is not fixed" (TNA note 2): it moves by up to about 2%.
- The floor fund has the same feature. On its own holdings (section 0), measured from the day it is bought (January 2028 at today's forwards), its payout falls by 3.83% if every distribution and its final cash earn nothing; for money moved into it in 2031, by 2.38%.

**The range rule (Keel's call Tue 10 Nov 07:04, card Q19; worked out on the fund's holdings since the afternoon; `completion.rule`, `numbers/range_rule.py`).**
- **Bottom:** the money put into the floor fund in January 2028, times what $1 of the fund's holdings pays on 15 Dec 2032 if from that day no distribution and none of its final cash earns anything. The holdings are priced on that day's curve. Less 0.5%, rounded down to $5,000.
- **Top:** the unrounded bottom plus the moved half on the same basis, worked out on the move day (before the 2031 meetings), less 0.5%, rounded down to $5,000.
- **The 2033 contribution** is the lower of what the two funds pay and the stated top. Any excess joins the half kept (CANON D12).
- **No figure is stated before the move.**
- **Why the holdings, not one par bond.** The morning's rule modelled the fund as one par bond at the purchase yield. That stand-in is cautious at today's yields; if yields fall about a point before the purchase, the holdings' premium makes it slightly generous, so the rule uses the holdings.
- **So "the bare minimum ... without doubt" is true by construction once worked out on the holdings; the market cannot move either end after the move.** It holds barring a US default, with 0.5% of value to spare for the fund's own frictions. The 0.5% cut, not the prospectus, carries the fund risk: a fund can pay slightly less than its holdings' cash flows without breaking its prospectus (an expense change made with notice, trading costs). That this applies to IBTM's prospectus is UNVERIFIED; read its wording before quoting it.

The cut depends on the yield at purchase. The more of the payout that is interest, the more is lost if interest stops. As a share of the modelled payout, today's values are 4.312% (floor) and 2.870% (moved half), of which 0.5% is the haircut:

| Purchase yield against today's forwards for that date | -3 pt | -2 pt | -1 pt | 0 | +1 pt | +2 pt | +3 pt |
|---|---|---|---|---|---|---|---|
| Floor, bought January 2028: the rule's cut (holdings, with the 0.5%) | 1.75% | 2.60% | 3.45% | 4.31% | 5.18% | 6.04% | 6.91% |
| Moved half, bought on the move day: the rule's cut | 1.37% | 1.87% | 2.37% | 2.87% | 3.37% | 3.86% | 4.35% |
| Floor, the morning's par stand-in (void) | 1.18% | 2.03% | 3.02% | 4.14% | 5.36% | 6.68% | 8.08% |
| Moved half, the morning's par stand-in (void) | 0.92% | 1.42% | 1.92% | 2.45% | 2.98% | 3.53% | 4.09% |

- **The engine's holdings are the cautious choice of three.** A fund holding 3.50% coupons (IBTM's real average) pays 0.10% (3 points lower) to 0.51% (3 points higher) more at zero interest per dollar than the engine's 4.25% holdings; 4.00% coupons pay 0.03% to 0.17% more.
- **The test, no longer circular.** Each stated end is checked against the zero-interest payout of holdings the rule does not assume, and against frictions beyond the 0.5%. "Not owned" means that payout is below the stated end:

  | Holdings tested | House model (200,000 paths): bottom / top not owned | Stock history (1,770 windows, rates at forwards) | Joint replay (585 windows, each on its own curve) |
  |---|---|---|---|
  | The engine's IBTM (what the rule uses), no friction | 0 / 0 | 0 / 0 | 0 / 0 |
  | 3.50% coupons (IBTM's real average) | 0 / 0 | 0 / 0 | 0 / 0 |
  | 4.00% coupons | 0 / 0 | 0 / 0 | 0 / 0 |
  | Engine's holdings less a friction of 0.1%, 0.25% or 0.5% of value | 0 / 0 | 0 / 0 | 0 / 0 |
  | Less 0.75% | 5.0% / 6.0% (largest gaps $339 / $429) | 0 / 6.3% (largest $312) | 22 / 34 windows ($281 / $312) |
  | Less 1% | 10.1% / 12.0% ($678 / $881) | 0 / 13.1% ($626) | 47 / 72 windows ($570 / $664) |
  | A fund of new par bonds at the purchase yield (the morning's stand-in) | 1.8% / 1.3% ($1,969 / $2,470) | 0 / 0 | 18 / 25 windows ($2,721 / $2,953) |

  So "certain" holds on the fund's real and modelled holdings and against any friction up to 0.5% of value. It does not hold against a fund that swapped its holdings for new par bonds, or a friction above 0.5%. The joint replay's realised payouts (at historical rates, which say nothing about the zero-interest case) never fell below either end either: smallest margins $1,262 (floor against the bottom) and $934 (both funds against the top).
- **Why a rule and not the fixed 4.1% and 2.5%.**
  - On the holdings, a fixed 4.1% is too small whenever the floor is bought more than 0.31 points above today's forward yield, which happens in 37.4% of house paths.
  - Run with the fixed figures, the zero-interest payout falls below the stated top in 5.9% of house paths (median gap $517, 1-in-20 $1,903, worst $6,416), and the floor below the stated bottom in 5.2%. Under the rule, both are 0%.
- **A variant Keel did not adopt.** Re-measuring the floor in 2031, when fewer of its flows are left, would cut 3.27%. Centrally it still states $95,000 to $115,000, but its ends are above what the holdings pay at zero interest in 11% of house paths, because money received by 2031 is counted at more than its value. The rule measures the floor once, at purchase, so the bottom never moves after January 2028.

## 4. The plan from 2028, on the escrow standard and the range rule (CASE_MAP C5, C8). MODEL

Central case: today's forward rates, VT at its median 7.5%. Move date modelled as 1 Jan 2031. The house and history columns give each row's own 1-in-20 points, so the rows do not add across. Stated figures are read without interpolation (section 0).

| Item | Central | House model 1-in-20 low / median / 1-in-20 high | History (US stocks, every 3-year window since 1871; rates at today's forwards) |
|---|---|---|---|
| Completing the ladder to the escrow standard (Jan 2028) | $38,282 | $33,884 / $40,239 / $54,679 | $38,282 |
| Left for floor and VT | $111,718 | $95,321 / $111,662 / $126,897 | $111,718 |
| Floor money (Jan 2028) / share of the $150,000 | $81,889 / 54.6% | $75,001 / $81,848 / $93,015 | $81,889 |
| VT bought (Jan 2028) | $29,829 | $20,320 / $29,814 / $33,881 | $29,829 |
| Floor payout, late 2032 | $103,178 | $88,047 / $103,097 / $124,380 | $103,178 (fixed once bought) |
| Bottom before rounding (zero-interest payout of the holdings, less 0.5%; 4.312% under the payout centrally) | $98,729 | $85,359 / $98,653 / $117,614 | $98,729 |
| **Bottom Laura states** | **$95,000** | $85,000 / $95,000 / $115,000 | $95,000 in every window |
| VT on 1 Jan 2031 | $36,989 | $19,535 / $36,095 / $61,959 | $24,792 / $39,421 / $61,172 |
| The moved half, paid late 2032 | $20,298 | $10,581 / $19,828 / $34,308 | $13,604 / $21,632 / $33,568 |
| What the floor and the moved half pay | $123,476 | $101,093 / $124,008 / $152,051 | $116,782 / $124,810 / $136,746; lowest $106,683 (start Jul 1929) |
| Top before rounding (bottom plus the moved half's zero-interest payout less 0.5%) | $118,443 | $97,932 / $118,921 / $144,548 | $111,942 / $119,740 / $131,333 |
| **Top Laura states** | **$115,000** | $95,000 / $115,000 / $140,000 | $110,000 / $115,000 / $130,000; lowest $100,000 (start Jan 1929) |
| **The 2033 contribution (the lower of what the funds pay and the stated top)** | **$115,000** | Equals the stated top in every path | Equals the stated top in every window |
| Excess, joining the half kept | $8,476 | $4,340 / $7,629 / $11,218 | $5,322 / $7,524 / $9,846 |
| Half kept, promised to no one, on 1 Jan 2033 | $21,347 | $9,881 / $20,739 / $41,258 | $13,238 / $23,481 / $40,607 |
| Half kept plus excess | $29,823 | $16,193 / $28,541 / $49,924 | $20,019 / $30,902 / $48,399; lowest $12,838 |
| Contribution plus half kept plus excess | $144,823 | $113,449 / $145,687 / $187,490 | $131,548 / $148,063 / $173,858 |

**Keel's reading of "most" (Tue 10 Nov afternoon; bond desk check, finding 2).** The IPS says "Most of the 2028
deposit will fund a Treasury fund maturing in late 2032" (l.15). Under the escrow standard, 73.3% of what is left
would fall below half the deposit whenever the completion is above $47,679, which happens when yields fall about a
point or more before January 2028. **Keel reads "most" as: the floor gets the larger of 73.3% of what is left and just
over half the deposit ($75,001 in January 2028 money, or all of what is left if that is less); VT takes the rest.**
It keeps the frozen book's split wherever that split already meets the IPS's word. Caplet can overrule it.
- **How often it binds:** in 16.9% of house paths. In the joint replay, 30 of 585 windows (5.1%): starts Sep 2000 to Feb 2001, Mar and Jun 2002, Feb 2007 to Nov 2008, Aug and Sep 2010. In the stock history (rates at forwards), never. Centrally, never (floor money $81,889).
- **Without it** the floor money would be under $75,000 in 16.9% of house paths (1-in-20 low $69,870).
- **What it costs VT where it binds:** house median $3,104, 1-in-20 $10,943, at most $20,016; joint replay median $2,058, at most $5,597. VT bought where it binds: median $23,085, 1-in-20 low $12,391 (23.5% and 14.2% of what is left, against 26.7% otherwise).
- **Named cases where it binds:** rates 3 points lower for good (8i: floor $75,001, VT $25,521, squeezed by $1,318); yields 1-in-20 low in January 2028 (Exhibit 3 below); the joint windows from Jul 2007 and Jan 2008 (8i); any fall of 0.5 points or more before January 2027 (section 5); a smaller deposit takes half of itself plus $1 ($56,251 of $112,500).
- Every house, history and joint figure on this page includes the rule; the central figures and the medians are unchanged by it.

**What Laura could announce in 2031, house model:**

| | at least $80,000 | $90,000 | $95,000 | $100,000 | $110,000 | $115,000 | $120,000 | $130,000 | $140,000 | $150,000 |
|---|---|---|---|---|---|---|---|---|---|---|
| Stated bottom | 99.9% | 79.9% | 62.9% | 45.2% | 15.9% | | 3.3% | | | |
| Stated top | | 99.4% | | 92.6% | 73.6% | 60.8% | 47.0% | 22.8% | 8.5% | 2.5% |

**What certainty costs the gift (central, same rule):**

| Standard | Floor payout | Stated range | Funds pay | Contribution | Excess | Half kept |
|---|---|---|---|---|---|---|
| No margin (ladder at forwards only) | $136,328 | $130,000 to $155,000 | $163,147 | $155,000 | $8,147 | $28,206 |
| Mon 9 Nov call (A, 3 points lower) | $115,929 | $110,000 to $130,000 (unrounded $110,930 to $133,081) | $138,735 | $130,000 | $8,735 | $23,986 |
| **Escrow standard (H_plain, with the fee cushion)** | **$103,178** | **$95,000 to $115,000** | **$123,476** | **$115,000** | **$8,476** | **$21,347** |

- The escrow standard moves $33,150 of floor payout to the payments' safety against no margin, and $12,751 against Mon 9 Nov's call.
- Each step costs $15,000 to $25,000 at each stated end.

More from the same runs:
- **The return assumption barely moves the gift.** VT growth from 4% to 10% a year, central path; the bottom is $95,000 in every column:

  | VT growth a year | 4% | 6% | 7.5% | 9% | 10% |
  |---|---|---|---|---|---|
  | What the funds pay | $121,557 | $122,638 | $123,476 | $124,337 | $124,925 |
  | Top before rounding | $116,580 | $117,630 | $118,443 | $119,280 | $119,851 |
  | Stated top = contribution | $115,000 | $115,000 | $115,000 | $115,000 | $115,000 |
  | Excess to the half kept | $6,557 | $7,638 | $8,476 | $9,337 | $9,925 |
  | Half kept | $18,091 | $19,899 | $21,347 | $22,879 | $23,948 |
  | Half kept plus excess | $24,648 | $27,537 | $29,823 | $32,216 | $33,873 |

  So the 7.5% is not doing the work; the Treasuries are (EXPECTATIONS T12 asked for 4% to 10%). The top stays under $120,000 even at 10% ($149 short of it).
- **Deletion test.** If VT went to zero:
  - the ten payments would be unchanged;
  - the floor still pays $103,178;
  - the stated range would be one figure, $95,000, and the contribution $95,000;
  - the $8,178 excess is Laura's.
- **Not capital-protected.** The 2028 money is not a protected note:
  - VT ($29,829) is more than the floor's expected interest ($21,289);
  - shares at zero would return $103,178 on the $111,718 left after completing the ladder.
- **The backstop comes back if rates hold.** At today's forward rates the payments never need it, and its money is Laura's:
  - $74,123 by 1 Jan 2042 if it all waits in the ETF, worth $45,456 in 1 Jan 2033 money or $34,345 in 1 Jan 2027 money;
  - or $58,603 handed back year by year from 2033 under an escrow release (8h).

### The 2031 move and the range (C5): the rule and its confidence
- **Central today, $95,000 to $115,000** (unrounded $98,729 to $118,443). This is the rule's value on today's forwards, not a promise. The two funds pay $123,476; the contribution is $115,000; the $8,476 excess takes the half kept from $21,347 to $29,823.
- **When each end is fixed.**
  - The bottom is fixed in January 2028, when the floor is bought: that day's curve sets both its payout and its zero-interest payout.
  - The top is fixed on the day half of VT moves into Treasuries, before the 2031 meetings.
  - Good and bad markets before the move change only the top. After the move nothing changes either end (case A6).
- **The confidence Laura can state after the move: certain, barring a US default.** True by construction once worked out on the holdings; the market cannot move either end after the move. Both ends are then money she owns in Treasuries maturing late 2032, each counted at what its holdings pay if no more interest is earned, less 0.5%. What the test of section 3 supports, and no more:
  - on the engine's holdings, on 3.50% and on 4.00% coupons, both ends are owned in every house path, every history window and every joint window;
  - a fund friction of up to 0.5% of value is covered everywhere; one of 0.75% would break an end in about 1 house path in 17;
  - so the report says "certain, barring a US default" for the stated ends after the move, and never claims more for the fund than its holdings.
- **Before the move, the uncertainty is which range she will be able to announce:**

  | When | What is fixed | Stated bottom | Stated top |
  |---|---|---|---|
  | Today, house model (1-in-20 low / median / 1-in-20 high) | Nothing | $85,000 / $95,000 / $115,000 | $95,000 / $115,000 / $140,000 |
  | Today, US stock history (rates at forwards) | Nothing | $95,000 | $110,000 / $115,000 / $130,000 |
  | Today, joint replay of rates and stocks (585 windows) | Nothing | $80,000 / $95,000 / $115,000 | $95,000 / $115,000 / $140,000 |
  | January 2028, floor bought at today's forwards | The bottom | $95,000 | $110,000 / $115,000 / $130,000 (house) |
  | After the 2031 move, central | Both ends, owned | $95,000 | $115,000 |
  | December 2032, paid, central | Contribution $115,000; excess $8,476 to the half kept | | |

- **Why nothing is stated before the move.** A top stated 1, 3, 6 or 12 months before the move is not yet owned in 2.9%, 6.3%, 8.7% or 10.7% of house paths. The 1-in-20 gap is $1,756, $2,925, $3,986 or $5,289.
- **Exhibit 3, one input moved at a time** (`numbers/range_rule.py`, central otherwise; 8i moves rates and shares together):

  | Case | Stated range | What the funds pay | Excess | Half kept, 1 Jan 2033 |
  |---|---|---|---|---|
  | Shares 1-in-20 low, 2028-2031 | $95,000 to $110,000 | $115,373 | $5,373 | $12,826 |
  | Median | $95,000 to $115,000 | $123,476 | $8,476 | $21,347 |
  | Shares 1-in-20 high, 2028-2031 | $95,000 to $130,000 | $136,960 | $6,960 | $35,530 |
  | Yields 1-in-20 low in January 2028 ("most" binds: floor $75,001) | $80,000 to $100,000 | $104,585 | $4,585 | $18,710 |
  | Yields 1-in-20 high in January 2028 | $110,000 to $135,000 | $143,803 | $8,803 | $23,155 |
  | VT worthless | $95,000 | $103,178 | $8,178 | $0 |
  | US stocks from Jan 2008 (rates at forwards) | $95,000 to $110,000 | $119,497 | $9,497 | $17,841 |
  | US stocks from Jan 2000 | $95,000 to $105,000 | $113,882 | $8,882 | $13,281 |
  | US stocks from Jul 1929 | $95,000 to $100,000 | $106,683 | $6,683 | $6,752 |

- **Framing options weighed (card Q19; same money, different words).** Keel's call is A; C and D are presentation choices the report may weigh.
  - **A, the rule above:** $95,000 to $115,000.
  - **C, narrow to what is owned after the move:** $115,000 to $120,000 central. In the house model C counts $10,000, $20,000 or $35,000 (1-in-20 low, median, high) more as pledged.
  - **D, one figure:** "at least $115,000".
- **Rounding is fragile at the centre.** Rounding down to $5,000 turns small gaps into $5,000 steps:
  - The unrounded bottom ($98,729) is $1,271 under $100,000; it would take a floor payout of $104,507 to state $100,000.
  - The unrounded top ($118,443) is $1,557 under $120,000.
  - On IBTM's real 3.50% coupons the ends are $99,023 and $118,747, still stated $95,000 and $115,000.
  - So the report says "about $95,000 to $115,000 on today's figures" and gives the rule, never the figures as a promise.
- **One definition, used everywhere:** the 2033 facility contribution is the lower of what the floor and the moved half pay and the stated top, and the range above is for that. The excess and the half kept are Laura's; money she later spends on the building from them is her separate choice, outside the announced range (`CANON.md` D12).

### The all-Treasury benchmark (C8)
- **The comparison.** If everything left in January 2028 bought the floor fund instead of 73% floor and 27% VT, with the same completion, Laura would have **$140,761** in late 2032 at forward rates. Stated under the same rule, that is $130,000 (unrounded $134,691). House model: $113,169 / $140,649 / $169,686, depending on yields to 2028.
- **The FINAL's funds pay less than that benchmark in 97.6% of house paths.** Its stated top is below the benchmark's stated figure in 95.0%. Half of VT is held back from the contribution on purpose, as flexibility.
- **Counting the half kept and the excess,** the FINAL leaves Laura more in total than the benchmark in 62.8% of house paths: median $145,687 against $140,649. In its 1-in-20 low it has about the same ($113,449 against $113,169).
- **An all-Treasury plan with the same flexibility** holds back the FINAL's median half kept ($20,739) and pays $120,023, stated $110,000 with certainty: $5,000 under the FINAL's central stated top, because the moved half's cut (2.87%) is smaller than the floor's (4.31%).
- **What VT adds** is a share of world growth for the top and for the half kept, at the cost of a lower certain bottom. Keel's reading: VT costs the contribution little at the median, and it is what lets half the growth stay unpromised. The report should say so plainly, not claim that VT makes the gift bigger.

## 5. A smaller or missed 2028 deposit (CASE_MAP C6). MODEL

The order is fixed by the IPS and the call:
1. The 2028 deposit first finishes the ladder.
2. Then it buys the backstop.
3. Then "most" of what is left goes to the floor fund (Keel's reading, section 4) and the rest to VT.

Exact figures, with the instruments re-sized on each shifted curve. Smallest 2028 deposit that still does each job, by how far yields fall before 1 Jan 2027:

| Yields fall before Jan 2027 | Ladder only (payments full at forward rates) | Escrow standard (payments full at 0%, after the ETF fee) | Deposit fall the ladder survives | Deposit fall the standard survives |
|---|---|---|---|---|
| None (6 Nov close) | $2,388 | $38,282 | 98.4% | 74.5% |
| 0.25 points | $10,320 | $44,836 | 93.1% | 70.1% |
| 0.5 points | $18,439 | $51,541 | 87.7% | 65.6% |
| 1 point | $35,257 | $65,437 | 76.5% | 56.4% |
| 2 points | $71,384 | $95,316 | 52.4% | 36.5% |

- **The thresholds.**
  - The payments stay full at forward rates unless the deposit falls by more than 98.4% at today's yields: 76.5% if yields fall 1 point first, 52.4% if 2 points (Q1's "about four-fifths" is the 1-point case).
  - The escrow standard holds unless the deposit falls by more than 74.5% at today's yields: 56.4% after a 1-point fall, 36.5% after 2 points.
  - The standard takes the whole $150,000 at a 3.60-point fall; the ladder alone takes it at 3.89 points (section 1).
- **A fall during 2027,** after the ladder is bought, also raises the completion, because the tail and the backstop are repriced: 0.5 points, $39,912 (the standard then survives a deposit fall of 73.4%); 1 point, $41,630 (72.2%); 2 points, $45,347 (69.8%).
- **A deposit too small for the whole backstop** buys part of it. The shortfall at 0% is $54,595 with no backstop. Whole deposits of $10,000, $20,000 or $30,000 buy 21%, 49% or 77% of the backstop, and the ten would then be short at 0% by $42,718, $27,114 or $11,509. At forward rates the ten are still paid in full.
- **The floor shrinks almost dollar for dollar,** and "most" takes at least half of the deposit. At today's yields:

  | 2028 deposit | Floor money | VT bought | Floor payout | Stated bottom |
  |---|---|---|---|---|
  | $150,000 | $81,889 | $29,829 | $103,178 | $95,000 |
  | $112,500 | $56,251 ("most" binds) | $17,967 | $70,875 | $65,000 |
  | $75,000 | $36,718 (all of what is left) | $0 | $46,263 | $40,000 |
  | $37,500 | $0 (the standard is $782 short of complete) | $0 | $0 | $0 |

  After a 0.5-point fall before Jan 2027, the full $150,000 leaves floor money of $75,001 ("most" binds), VT $23,458, stated bottom $85,000. After a 1-point fall: $75,001, VT $9,562, floor payout $90,007, stated $85,000. After 2 points: the floor takes all $54,684 left, VT $0, stated $60,000.
- **A missed deposit** (one of the IPS's two reasons to change) leaves:
  - $2,287 of the ladder unbought. With the longest rungs bought first, the 2033 payment is $3,016 short at forward rates; the ten are $57,455 short at 0%, and short in all 585 historical windows;
  - no backstop;
  - no floor and no VT, so nothing for the building. Laura would know before 2031, because the deposit is due Jan 2028 and the meetings are in 2031.
- **A smaller deposit is not one of the two reasons.** The plan as written absorbs it: ladder first, then backstop, then floor and VT smaller.
- The Q1 card shows a recession could shrink the deposit while yields fall. The report states this as a risk, not a change.

## 6. Figures now void (do not use)

| Old figure | Where it came from | Now |
|---|---|---|
| Range $145k-$168k, $145k-$170k, top reached "about three times in four" | October numbers on older designs | Section 4: stated range $95,000 to $115,000 central (unrounded $98,729 to $118,443). After the 2031 move the stated ends are owned; what is uncertain is which range she can announce |
| About $21,000 short if yields fall 2 points for good | Old design, 23 Oct curve | $23,509 for the ladder as written; $0 on the escrow standard |
| "All ten paid in full in about 75-76% of base futures" | Old runs, H8 (model futures) | 44% of historical windows as written; all 585 on the escrow standard (history replay, not model futures) |
| All-Treasury plan about $191,000 | 4 Nov curve, `ips_rewrite/final_night/IDEA_LIST_MATHS.md` | $140,761, stated $130,000 (section 4). The Mon 9 Nov $158,157 (with margin) and $185,987 (without) are void too |
| A 1-point fall adds about $30,600 | 25 Sep curve | $31,805 before 1 Jan 2027 (6 Nov) |
| "Headroom" under $300,000 | Every curve before 5 Nov | Gone: the ten cost more than $300,000 |
| Fixed $150,000 floor | Old option 4b | No fixed floor: the floor is "most" of what is left (at least $75,001, section 4), and the payout "is not fixed" |
| $13k / $24k / $45k (kept half) and $14k / $23k / $38k (moved half), house model | Section 4 before the 9 Nov move to J.P. Morgan's 2027 volatility | $9,881 / $20,739 / $41,258 and $10,581 / $19,828 / $34,308 (section 4) |
| $302,137 (curve) and $303,269 (instruments) | 5 Nov, `keel/scripts/holdings_ladder.py` | 6 Nov: $301,544 curve; $302,287 instruments on the curve. Market quotes for 6 Nov were not taken, and the 5 Nov gap was +$1,132 |
| **Voided Tue 10 Nov morning (Mon 9 Nov's call):** | | |
| Keel's call = design A sized for rates 3 points lower: cost $323,436, margin $21,149 | Section 2, Mon 9 Nov | H_plain with the fee cushion: cost $336,656, backstop $34,369. The 9 Nov design is the alternative only |
| "All ten paid in 94% of 16-year stretches"; short in 6.0% (35 of 585), 1-in-20 $1,225, worst $12,117; $22,192 short at 0% | Section 2, Mon 9 Nov | Paid if no coupon earns anything, after fees on waiting cash; the history and insurer tests follow from that |
| Completion "about $24,500" ($24,475) | Sections 2, 4, 5 | $38,282 in January 2028 money |
| Left $125,525; floor money $92,010 (61%); VT bought $33,515 | Section 4 | $111,718; $81,889 (54.6%); $29,829 |
| VT "7.45% of the $450,000 in the plan with Keel's margin (section 4: $33,515)" | 8g, bullet "The book was built before the margin" | 6.63% ($29,829). 8g's table is unchanged; only this bullet is void |
| Floor payout $115,929; house $93k / $116k / $140k | Section 4 | $103,178; house $88,047 / $103,097 / $124,380 |
| Stated bottom $110,000 | Section 4 | $95,000 (unrounded $98,729) |
| Fixed deductions 4.1% (floor) and 2.5% (moved half); "the bottom Laura states is the floor's modelled payout less 4.1%" | Section 3 | The holdings rule (section 3); 4.31% and 2.87% are today's cuts only |
| VT on 1 Jan 2031 $41,561; moved half $22,806 (house $13k / $23k / $39k; history $15k / $24k / $38k) | Section 4 | $36,989; $20,298 (house $10,581 / $19,828 / $34,308; history $13,604 / $21,632 / $33,568) |
| Top $138,735 (house $111k / $139k / $171k; history $131k / $140k / $154k, lowest $119.9k Jul 1929) | Section 4 | What the funds pay: $123,476 (house $101,093 / $124,008 / $152,051; history $116,782 / $124,810 / $136,746, lowest $106,683). Stated top $115,000 (house $95,000 / $115,000 / $140,000; history $110,000 / $115,000 / $130,000) |
| Central range "about $110,000 to $135,000", and the panel's corrected "$110,000 to $130,000" ($133,412) | Section 4 and its "correction under review" | $95,000 to $115,000 under the rule |
| The gift $138,735, above the stated top | Section 4 | Contribution $115,000 (the cap); $8,476 joins the half kept |
| Half kept $23,986 (house $12k / $24k / $47k; history $15k / $26k / $46k) | Section 4 | $21,347 (house $9,881 / $20,739 / $41,258; history $13,238 / $23,481 / $40,607); with the excess $29,823 |
| Floor + moved half + kept half $162,721 (house $128k / $164k / $211k; history $148k / $166k / $195k) | Section 4 | $144,823 (house $113,449 / $145,687 / $187,490; history $131,548 / $148,063 / $173,858) |
| Without the margin: stated bottom $130,000, top $163,147, house $135k / $164k / $196k, kept $28,248 | Section 4 | Under the rule: $130,000 to $155,000, funds pay $163,147, kept $28,206 (section 4 cost table) |
| "The margin moves about $20,000 from the bottom, and about $24,000 from the top" | Section 4 | The escrow standard moves $33,150 of floor payout against no margin and $12,751 against Mon 9 Nov's call |
| Return sensitivity: tops $136,580 to $140,364; kept $20,327 to $26,907 | Section 4 | Funds pay $121,557 to $124,925; stated top $115,000 throughout; kept $18,091 to $23,948 (section 4) |
| Deletion test: the gift would be the floor alone, $115,929 | Section 4 | Stated $95,000, contribution $95,000, excess $8,178 |
| VT $33,515 against the floor's expected interest $23,919; $115,929 returned on $125,525 | Section 4 | $29,829 against $21,289; $103,178 on $111,718 |
| Overflow "about $27,990" / $27,939 in Jan 2033 money; each rung $1,705 (2033) to $5,266 (2041) above $50,000, $36,859 in all | Sections 4 and 8h | Each own rung pays exactly $50,000 at forwards ($0 above); the backstop's $74,123 by 1 Jan 2042 ($45,456 in 2033 money, $34,345 in 2027 money), or $58,603 released year by year (8h) |
| All-Treasury $158,157 certain; FINAL's top below it in 98%; more in total in 63%; median $164k against $158k; 1-in-20 $128k against $127k; "about $134k" with the same flexibility | Section 4 (C8) | $140,761 (stated $130,000); 97.6% (95.0% on stated figures); 62.8%; $145,687 against $140,649; $113,449 against $113,169; $120,023, stated $110,000 |
| Deposit needed with Keel's margin $24,500 / $40,400 / $56,900 / $92,000; floors about $81k / $47k / $12k for $112,500 / $75,000 / $37,500 | Section 5 | $38,282 / $51,541 / $65,437 / $95,316; floor payouts $70,875 / $46,263 / $0 (section 5) |
| "A margin sized for them protects the whole ladder" | 8a | The backstop pays what interest would have, up to every payment's full $50,000 at 0% after the ETF fee (8a) |
| 8b's "with Keel's margin" column blank on 7 and 8 Oct | 8b | Filled ($310,138, $312,024); the escrow column added |
| Rival comparison on Mon 9 Nov's call (FINAL $111,183 / $139,392 / $170,770 against $85,802 / $147,146 / $251,436, and the rest of 8c) | 8c | 8c, Tue 10 Nov afternoon |
| Range in 2027 dollars $98,253-$120,584 / $95,410-$117,094 / $89,485-$109,823; NT$3.00m-3.69m (3%), 3.29m-4.04m (1.5%), 2.67m-3.27m (5%); "$21,000-$26,000 more" for the strongest Taiwan dollar | 8d | 8d |
| Kept half $9,168 / $12,150 / $23,831 / $46,746 (house) and $9,324 / $14,874 / $26,383 / $45,626 (history), and the rest of the Mon 9 Nov 8f | 8f | 8f, Tue 10 Nov afternoon |
| Reserve $427,028 on 1 Jan 2033; "about 107% funded"; 55.7% iBond ETFs / 44.3% bonds; every row of the 9 Nov 8h table; "Keel's margin grown to 2033 ($27,939)" | 8h | $444,545; 111.4% funded; composition in 8h |
| "Keel's margin covers these [waits] at 3 points below forwards" | 8h | The escrow standard covers them at 0%, after the ETF fee |
| The pooled-book candidate table "against Keel's call" (P25 to P100) | Section 2, Mon 9 Nov night | Decided: section 2, "The certain designs Keel weighed" |
| **Voided Tue 10 Nov afternoon (this morning's figures; bond desk check):** | | |
| H_plain cost $335,771; backstop $33,484 (IBTQ $332, IBTR $3,991, then $5,458, $5,856, $6,013, $7,127, $7,152 face); "$12,335 more than Mon 9 Nov's call" | Section 2 | $336,656; $34,369 (section 2 table); $13,220 more. $335,771 stays only as the 0%-sized comparison |
| "Met exactly" at 0%; "nothing is left after 2042" in the 0% world; the ETF fee "not modelled", "tens of dollars", "rounding each purchase up covers it" | Sections 0, 2, 7, 8a, 8h | Sized with the fee: $0 short with it, $1,414 spare at 0% (section 2) |
| "A short-term Treasury ETF" for the waiting money | Sections 0, 2, 8h | A Treasury-bill ETF (0 to 3 months) |
| "All ten paid in full in every test: ... all 585 historical windows; all seven Regulation 126 scenarios" as separate evidence | Section 2 | "Paid in full if no coupon earns anything, after fees on waiting cash; the history and insurer tests follow from that one test" |
| "The municipal escrow verifier's test" | Section 2 | "The escrow verifier's arithmetic (paid even if no coupon earns anything), applied to holdings an escrow would not accept" |
| Completion $37,358 ("about $37,400") | Sections 2, 4, 5 | $38,282 ("about $38,300") |
| Left $112,642; floor money $82,567 (55.0%); VT bought $30,075 (house $25,716 / $30,060 / $34,114) | Section 4 | $111,718; $81,889 (54.6%); $29,829 (house $20,320 / $29,814 / $33,881) |
| Floor payout $104,031 (house $83,833 / $103,948 / $125,211) | Sections 2, 4, 5 | $103,178 (house $88,047 / $103,097 / $124,380) |
| Unrounded range $99,729 to $119,693; house unrounded $81,535 / $99,638 / $117,988 and $97,343 / $120,137 / $145,318 | Section 4 | $98,729 to $118,443; house $85,359 / $98,653 / $117,614 and $97,932 / $118,921 / $144,548 |
| Deductions 4.136% (floor) and 2.447% (moved half), the one-par-bond shift table, "3.85% and 2.44% with the real coupon" | Sections 3, 4, 7 | The holdings rule's cuts, 4.312% and 2.870% today with the 0.5% (section 3) |
| "True by construction ... or a fund failing to work as its prospectus says"; "The evidence: house 0%, history the same, joint replay" | Sections 3, 4 | "True by construction once worked out on the holdings; the market cannot move either end after the move"; the test of section 3 |
| Stated bottom house $80,000 / $95,000 / $115,000; stated top house $95,000 / $120,000 / $145,000; history top $110,000 / $120,000 / $130,000, lowest $100,000 Apr 1929; joint top "about $145,000" | Section 4, 8i | Bottom $85,000 / $95,000 / $115,000; top $95,000 / $115,000 / $140,000; history $110,000 / $115,000 / $130,000, lowest Jan 1929; joint $95,000 / $115,000 / $140,000 |
| VT on 1 Jan 2031 $37,295; moved half $20,465 (house $11,881 / $20,346 / $34,737; history $13,717 / $21,811 / $33,845) | Section 4 | $36,989; $20,298 (section 4) |
| Funds pay $124,497 (house $100,009 / $125,033 / $153,090; history $117,748 / $125,842 / $137,877, lowest $107,566) | Sections 4, 8c, 8i | $123,476 (section 4) |
| Excess $9,497; half kept $21,524; with the excess $31,021; total $146,021, and their house and history columns | Sections 4, 8d, 8f, 8i | $8,476; $21,347; $29,823; $144,823 (section 4) |
| The odds table (bottom 96.3% / 81.1% / 66.4% / 48.7% / 17.4% / 3.4%; top 98.6% ... 2.75%) | Section 4 | Section 4 table |
| Cost table: $32,297 and $11,898; Mon 9 Nov "unrounded $111,135 to $133,383" | Section 4 | $33,150 and $12,751; $110,930 to $133,081 |
| Return sensitivity $122,562 to $125,958, stated top $120,000 at 9% and 10%, "the step at 9% is rounding" | Section 4 | $121,557 to $124,925; stated top $115,000 at every rate |
| Deletion test excess $9,031; VT $30,075 against $21,465; $104,031 on $112,642 | Section 4 | $8,178; $29,829 against $21,289; $103,178 on $111,718 |
| Backstop back: $72,215 by 2042, $44,286 (2033 money), $33,461 (2027 money); release $56,994, first $10,496 | Sections 2, 4, 8h | $74,123; $45,456; $34,345; release $58,603, first $8,813 (8h) |
| A top stated before the move not owned in 7.2% / 10.8% / 13.1% / 14.6%; gaps $1,933 / $3,139 / $4,208 / $5,540 | Section 4 | 2.9% / 6.3% / 8.7% / 10.7%; $1,756 / $2,925 / $3,986 / $5,289 |
| The morning's Exhibit 3 rows (from $116,328 / $12,932 to $107,566 / $6,808) | Section 4 | Section 4 table |
| Rounding: $271 and $307 short of the next step; floor payout $104,314 to state $100,000; real coupon $100,023 (stated $100,000) and $119,989; "the house median stated top is $120,000" | Section 4 | $1,271 and $1,557; $104,507; $99,023 and $118,747, stated $95,000 and $115,000; house median $115,000 |
| All-Treasury $141,926 certain, stated $135,000 ($136,056), house $114,370 / $141,812 / $170,820; 95.3%; $147,037 against $141,812; $115,074 against $114,370; $120,534, stated $115,000 "equal to the FINAL's central top" | Section 4 (C8) | $140,761, stated $130,000 ($134,691), house $113,169 / $140,649 / $169,686; 95.0%; $145,687 against $140,649; $113,449 against $113,169; $120,023, stated $110,000 |
| Section 5: $37,358 / $43,900 / $50,594 / $64,469 / $94,301; 75.1% / 70.7% / 66.3% / 57.0% / 37.1%; 3.63 points; 22% / 50% / 79% and $42,712 / $27,100 / $11,487; floors $69,398 / $34,765 / $131, stated $65,000 / $30,000 / $0; after a 1-point fall $75,238, stated $70,000 | Section 5 | Section 5 |
| 8a: backstop money due $9,098, $1,516 ... $7,376 ($54,595 in all); carries $6,510 / $4,847 / $2,606; $1,517 of 2027 flows; "from 2037 the match is exact" | 8a | 8a |
| 8b escrow column ($349,317 on 2 Jan ... $335,771 on 6 Nov; cheapest $324,402) | 8b | 8b |
| 8h: reserve $443,375, 111.1%, run-down 112.7% to 244.4%; composition with IBTM's $50,000 among iBond ETFs ($230,646, 52.0%); backstop $332 ... $6,013 and $10,496; left $24,040 ($14,743) at 3 points lower; release $10,496 / $1,549 / $1,549 ... $56,994 | 8h | 8h |
| 8i: every row, including rates 3 points lower $80,000 ($80,003) to $95,000 ($97,269), floor $79,864 at zero interest; left after 2042 $44,286 / $14,743 / $6,351 / $10,797 / $75,717 at today's forwards; joint half kept $13,972 / $24,024 / $42,366, left $13,580 / $42,510 / $100,618; lowest bottom $70,000 (Dec 2007); Jan 2008 $70,000 to $90,000 (completion $53,684); Jul 2007 $99,292 against $98,015 | 8i | 8i |
| The reserve JSON key `margin_value_1jan2033_at_forwards` = $44,316 (the backstop's cost carried, ignoring the funds' fee) | `numbers/results_reserve_2026-11-10.json`, morning | The key now holds $45,456 (reserve before the payment less the own rungs); the cost carried is kept as `margin_cost_carried_to_1jan2033_at_forwards` ($45,487) |
| **Voided Tue 10 Nov evening (8j):** | | |
| Taiwan dollar test, half kept alone: 90.9% of house paths (median gap $1,583; 8.8% covered 19 in 20), history 96.5%, joint 97.4%; stricter reading 85.7% / 94.9% / 93.8%; real currency 97.1% (worst $8,942) | `twd_test` in this afternoon's `results_joint_stress_2026-11-10.json` (never in the register; quoted in the evening brief). It divided by what the funds pay before the cap | 8j, on the contribution after the cap: 93.2% ($1,407; 9.4%), 96.9%, 99.3%; stricter 89.1% / 96.0% / 97.3%; real currency 98.1% (worst $7,312). The 99.77% with the excess stands |
| Mon 9 Nov's Taiwan dollar test: 93.0%, "1 in 14", $1,590, 99.97% with the cap rule, real currency 97.1% (worst $10,048), and the gift in NT$ ($138,735 = NT$4.55m) | Card Q24 verdict 3, rows 22-25, card 4 | 8j (section 10 lists the lines) |

## 7. Limits of these numbers
- **The reinvestment history** uses 1-year yields in proportion. That is harsh on windows starting at high rates, and it is only 585 overlapping windows, roughly four independent rate eras. A design that passes at 0% passes it anyway.
- **The house model does not test reinvestment.** It moves yields only up to 2031, for the purchases and for the backstop's price in January 2028.
  - Payment safety against reinvestment comes from section 2's 0% test, and the escrow standard does not rely on any rate.
  - House model: 200,000 paths, seed 2033.
- **The house model** draws stocks and yields independently. In a real recession shares and yields often fall together, which would hurt the top and raise the completion at the same time (Q1). 8i replays rates and shares from the same months.
- **The fund coupons** are modelled at par yields (IBTM 4.25%), above IBTM's real 3.50%:
  - **reinvestment:** a little overstated;
  - **the backstop:** a lower-coupon fund pays more at 0% per dollar, so the model is cautious;
  - **the range rule:** cautious at today's yields and at every shift tested (section 3: 3.50% and 4.00% coupons pay more at zero interest). Real holdings drift; the rule is worked out on the trade day's holdings, and the 0.5% cut covers frictions up to 0.5% of value.
- **The backstop's size** is fixed by the fee-cushioned 0% test on the rungs bought in January 2027, so it depends on yields before then. The model takes that from a grid of re-sized ladders 0.25 points apart and prices the backstop on each path's January 2028 curve.
- **The fee on waiting money** is modelled as 0.15% a year on every waiting dollar, including the cash inside the iBond funds in their last months (conservative: the fund's own fee is already counted). A Treasury-bill ETF's real fee is UNVERIFIED until a student checks the WInS listing; at 0.20% a year the cushion would need about a third more (an estimate scaled from the bond desk's figures, not a run).
- **The IBTM tail.** The $2,287 still unbought in January 2027 misses its 2027 distributions ($97). The $2,388 set aside for it buys it for $2,280 in January 2028, and the $108 left goes into the waiting cash (8a).
- **Not modelled.**
  - Bond lots: the backstop's face amounts ($5,603 and so on) are not rounded to tradable lots.
  - Which Treasury-bill ETF: UNVERIFIED (section 0).
- **The escrow release** in 8h is Keel's reading, not in the IPS. Without it, the backstop's money simply waits and is Laura's after the last payment.
- **Rounding to $5,000** sits close to a step at the centre (section 4). The central ends are $1,271 and $1,557 below the next $5,000.
- **Fund holdings data** comes from one day's iShares figures. Holdings and cash-wait months will drift.
- **"Most"** is Keel's reading (section 4). The IPS gives no figure; the 73.3% comes from the frozen WInS book.
- **No market quotes on 6 Nov.** Everything is priced on the curve.

## 8. Added Mon 9 Nov, later; re-run Tue 10 Nov afternoon (`numbers/extras.py`, `numbers/results_extras_2026-11-10.json`)

### 8a. Where each payment's $50,000 comes from (the call: own rungs plus the backstop)
The own rungs are design A sized at today's forward rates (section 1's table), so under the call the first eight
columns hold as they stood on Mon 9 Nov. The last four come from the call's two tests: what each own rung delivers,
and what the backstop pays towards that payment, at 0% and with the ETF fee on every waiting dollar.

| Payment | Instrument | Cost (1 Jan 2027) | Coupons received | Interest on those coupons | Share of the $50,000 that is interest on interest | Coupons reinvested 3 points lower; fund cash in its last months at forwards | Delivered if reinvestment earns nothing (fund cash at forwards) | Own rung in the 0% test | Backstop money due that year (0% test) | Own rung, ETF fee test | Backstop money due, ETF fee test |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2033 | IBTM | $37,908 | $8,848 | $1,719 | 3.4% | $48,880 | $48,281 | $47,413 | $9,339 | $47,338 | $9,298 |
| 2034 | IBTO | $36,065 | $10,079 | $2,180 | 4.4% | $48,595 | $47,820 | $46,820 | $1,556 | $46,731 | $1,555 |
| 2035 | IBTP | $34,300 | $11,368 | $2,949 | 5.9% | $48,098 | $47,051 | $46,244 | $1,556 | $46,142 | $1,555 |
| 2036 | IBTQ | $32,588 | $12,426 | $3,670 | 7.3% | $47,643 | $46,330 | $45,549 | $1,973 | $45,431 | $1,972 |
| 2037 | IBTR | $30,922 | $13,178 | $4,328 | 8.7% | $47,242 | $45,672 | $44,629 | $5,514 | $44,491 | $5,509 |
| 2038 | 4.750% Feb 2037 | $29,136 | $13,742 | $6,640 | 13.3% | $45,883 | $43,360 | $43,360 | $6,813 | $43,195 | $6,805 |
| 2039 | 4.500% May 2038 | $27,567 | $14,099 | $6,777 | 13.6% | $45,811 | $43,223 | $43,223 | $6,945 | $43,061 | $6,939 |
| 2040 | 4.375% Nov 2039 | $26,051 | $15,059 | $6,803 | 13.6% | $45,747 | $43,197 | $43,197 | $6,959 | $43,043 | $6,957 |
| 2041 | 4.250% Nov 2040 | $24,582 | $15,233 | $7,653 | 15.3% | $45,236 | $42,347 | $42,347 | $7,822 | $42,180 | $7,820 |
| 2042 | 3.125% Nov 2041 | $23,168 | $13,150 | $7,376 | 14.8% | $45,434 | $42,624 | $42,624 | $7,532 | $42,469 | $7,531 |
| **All ten** | | **$302,287** | | | | | | **$445,405** | **$56,009** | **$444,080** | **$55,941** |

- **Two columns do not price the funds' last months the same way.** The "3 points lower" and "earns nothing" columns leave each fund's final months of cash at forward rates; the two test columns, and 8h, let that cash follow the world. The T-bond rows agree. Figure 1 uses 8h.
- **How the 2033 money flows.** At 0% the backstop's money for 2033 is $9,339: its flows to the end of 2032, including $1,557 that its holdings would have paid in 2027, which the 2028 deposit puts into the ETF as cash when it buys them. That is more than the 2033 gap ($2,587). The rest carries forward in the ETF: $6,752 after 2033, $5,128 after 2034, $2,928 after 2035. From 2036 a little is left each year ($449, rising to $1,414 after 2042): the fee cushion, spare at 0%.
- **With the ETF fee the match is exact.** The carry is $6,636, $4,912 and $2,601 after 2033-2035, then nothing, and nothing is left after 2042.
- **The IBTM tail.** The $2,287 of IBTM still unbought in January 2027 misses its 2027 distributions ($97), which both tests count. The $2,388 the completion sets aside for it buys it for $2,280 in January 2028; the $108 left goes into the waiting cash with the backstop's $1,557 and covers the $97.
- The later the payment, the more of it is interest earned on interest: 3% of the 2033 payment, about 15% of the 2041 and 2042 payments. The risk sits in the last five, the T-bonds, which is why most of the backstop is extra face in them.

**Flat break-even.** Bought at today's prices with no completion standard, the ladder pays all ten only if every coupon earns at least
**5.12% a year** from the day it arrives until it is needed (bisection on one flat rate for every reinvestment). Today's
forward rates are 4.67% for 2027-2033 and 5.43% for 2033-2042, so the break-even is simply the average of the forwards:
the ladder as written assumes today's forward rates come true. At a flat 4.0% the worst payment is $47,721 and the ten
fall $13,906 short in all; at 3.0%, $46,215 and $25,144; at zero, $42,347 and $54,595 (matches section 2). With the
backstop, the ten are paid at every flat rate down to zero, and with the ETF fee on every waiting dollar.

### 8b. The cost of the ten payments through 2026, from this one engine (every Treasury close, 2 Jan to 6 Nov)
214 closes. Value on 1 Jan 2027 of the ten payments (payment-date basis), of the ten instruments held (design A), and
of the ten with each completion standard bought that day:

| Date | Ten payments | Ten held | With Mon 9 Nov's margin (-3 pt) | With the backstop (escrow standard, fee cushion) | 10-year yield |
|---|---|---|---|---|---|
| Fri 2 Jan | $316,546 | $317,338 | $338,677 | $350,219 | 4.19% |
| Fri 27 Feb (the year's dearest) | $325,563 | $326,382 | $347,837 | $357,873 | 3.97% |
| Tue 30 Jun | $312,974 | $313,752 | $335,061 | $346,400 | 4.44% |
| Thu 10 Sep (first close under $300,000) | $297,879 | $298,612 | $319,704 | $333,534 | 4.95% |
| Fri 25 Sep | $292,264 | $292,979 | $313,976 | $328,684 | 5.17% |
| Mon 28 Sep (trading opens) | $290,291 | $291,000 | $311,968 | $326,980 | 5.24% |
| Mon 5 Oct (the year's cheapest) | $287,938 | $288,642 | $309,559 | $325,264 | 5.31% |
| Wed 7 Oct (orders filled 7-8 Oct) | $288,510 | $289,216 | $310,138 | $325,845 | 5.28% |
| Thu 8 Oct | $290,349 | $291,060 | $312,024 | $327,309 | 5.22% |
| Fri 16 Oct | $294,770 | $295,493 | $316,537 | $330,861 | 5.09% |
| Fri 23 Oct (Trading Notes due) | $297,636 | $298,367 | $319,462 | $333,207 | 5.00% |
| Fri 6 Nov (IPS in, trading froze) | $301,544 | $302,287 | $323,436 | $336,656 | 4.86% |

The ten payments cost less than $300,000 on only 37 of the 214 closes (the ten held, on 36), every one of them between
10 Sep and 3 Nov. The team's orders filled on 7-8 Oct, within two trading days of the year's cheapest close (5 Oct).
That is luck of timing, not skill, and should be told that way if it is told at all. By the IPS deadline the cost was
back over $300,000, which is the situation the IPS's completion rule was written for.
- The escrow standard cost more than $300,000 on every close of 2026; its cheapest was $325,264 on 5 Oct.
- So under this standard the 2028 deposit always had a first job before the gift, whatever the day.
- Dates are US closes.

### 8c. The strongest rival on Caplet's own design: buy the floor in 2031, not 2028
Rival: everything left in Jan 2028 after completing the ladder goes into VT; in Jan 2031 the same final mix as FINAL
after its move (FINAL's half kept, as a share of the 2028 money, stays in VT to 2033: 13.35% when "most" does not
bind; the rest goes into Treasuries maturing late 2032). Same escrow standard, same house paths (200,000, seed 2033)
and the same 1,770 history windows (US stocks with dividends, every 3-year start since 1871).

| | FINAL (floor bought Jan 2028) | Rival (floor bought Jan 2031) |
|---|---|---|
| Money owned in Jan 2031, house p5 / p50 / p95 | $101,093 / $124,008 / $152,051 | $77,102 / $131,419 / $223,957 |
| Worst 1 in 100 (house) | $94,133 | $61,399 |
| Chance it is under $95,000 (the central stated bottom), house | 1.3% | 15.8% |
| Total by 2033, house p5 / p50 / p95 | $113,449 / $145,687 / $187,490 | $88,991 / $152,726 / $261,239 |
| Money owned in 2031, history p5 / p50 / p95 | $116,782 / $124,810 / $136,746 | $88,301 / $140,405 / $217,875 |
| Lowest in history | $106,683 (start Jul 1929) | $22,752 (start Jul 1929) |
| Under $95,000 in history | 0% | 9.1% |

What it shows:
- **Waiting raises the middle by about $7,400 and the lucky end a great deal.**
- **But Laura could walk in short.** In about one path in six (house) or one window in eleven (history), she would walk into the 2031 co-sponsor meetings with less than the $95,000 she could have stated in 2028. From a July 1929 start she would have about $23,000.
- **The price of FINAL.** It ends up behind the rival in 59.8% of house paths and 68.4% of history windows. What it buys with that is a bottom named in January 2028, three years before the meetings, that cannot fall.

### 8d. What the dollars buy: inflation and the Taiwan dollar (`numbers/real_values.py`, inputs `numbers/inflation_inputs.json`)
Sources and bands in `research/cards/Q10_inflation_inputs.md` (all read 9 Nov 2026).
- **US inflation:** central 2.4% a year (J.P. Morgan 2027 matrix, the same edition as the 7.5%); band 1.9%-3.5%.
- **Taiwan construction costs:** central 3.0%, band 1.5%-5.0% (DGBAS construction cost index: September 2026 +7.29% on a year, about 3% a year since 2000).
- **USD/TWD:** 32.768 on 6 Nov (central bank of Taiwan); the strongest Taiwan dollar of the last ten years was 27.52.
- The range is read from `results_2026-11-10.json`.

| | US inflation 1.9% | 2.4% (central) | 3.5% |
|---|---|---|---|
| The 2033 payment in 1 Jan 2027 dollars | $44,661 | $43,368 | $40,675 |
| The 2042 payment in 1 Jan 2027 dollars | $37,701 | $35,032 | $29,845 |
| All ten in 1 Jan 2027 dollars | $410,937 | $390,686 | $350,118 |
| The $95,000-$115,000 range (paid 2033) in 1 Jan 2027 dollars | $84,855-$102,719 | $82,399-$99,747 | $77,283-$93,553 |

- **In Taiwan building terms,** the range buys NT$2.59m-NT$3.14m of today's construction at 3% cost growth (NT$2.84m-3.44m at 1.5%, NT$2.30m-2.79m at 5%).
- **If the Taiwan dollar went back to its ten-year strongest (27.52),** Laura would need $18,116-$21,930 more to buy the same NT$ budget. That is about the whole half kept in the middle case ($21,347), and within the half kept plus the excess ($29,823, section 4). 8j tests the half kept against a 10% stronger Taiwan dollar and against the real currency since 1983.

What it shows: the ten payments are fixed in dollars by the case, so inflation cannot make them fail; it decides what
they buy. At 2.4% the 2042 payment buys about 70% of what $50,000 buys today. The facility money is exposed twice, to
Taiwan's building costs and to the exchange rate, which is one more reason the kept half exists. Market prices on 6 Nov
(10-year breakeven 2.23%) leave the ladder's yield about 2.6 points above expected inflation (Keel arithmetic, 10-year
point). CANON check: the TNA's "nonexistent inflation risk" is about funding the payments, which holds.

### 8e. What the ten would have cost on every curve since 1962, and every month since 1871 (`numbers/price_history.py`, `numbers/results_price_history.json`)
Basis: each past curve is treated as if it were the 6 Nov 2026 curve, so the payments are always the same distance
ahead (the 1 Jan 2027 value of $50,000 on 1 Jan 2033-2042). It asks one question: would $300,000 have bought all ten on
that day's rates? Data: FRED constant-maturity Treasury yields (Treasury's own par curve) 1962-2025, treasury.gov par
curves for 2026, Shiller's long government bond yield for 1871-1961 (one rate, so a flat curve; on 1962-2026, where both
exist, the flat curve gives 53.3% of months under $300,000 against 54.4% on the full curve, so the bias is small). For
2026 this basis runs on average $1,944 above section 8b's dated values (at most $4,579, nothing on 6 Nov) and gives the
same 37 closes under $300,000, from the same first day, 10 Sep.

| Measure | Figure |
|---|---|
| Days since 2000 on which $300,000 bought all ten | 731 of 6,716 (10.9%) |
| Days since 1990 / since 1962 | 34.1% / 54.5% |
| Days from June 2007 to August 2026 | one: Thu 19 Oct 2023 ($299,293; 10-year 4.98%, 20-year 5.30% at the close) |
| Last run of days before 2026 | June 2007 (cheapest that year $291,692 on 12 Jun) |
| Dearest since 2000 | $470,217 on Tue 4 Aug 2020 (10-year at 0.52%), more than both of Laura's deposits together |
| Cheapest since 2000 | $250,757 on Thu 20 Jan 2000 |
| Mon 28 Sep 2026 (trading opened) | $290,698, cheapest since 7 Jun 2002 |
| Mon 5 Oct 2026 (the year's cheapest) | $288,333, cheapest since 21 May 2002 |
| Wed 7 Oct 2026 (orders filling) | $288,889 |
| Months since 1871 on which $300,000 bought all ten (flat curve at the long rate) | 25.2%, about one in four |
| The same by era | 1871-1913: 9.7%; 1914-1945: 1.8%; 1946-1965: 0%; 1966-1999: 94.9%; 2000-2026: 8.7% |
| Flat yield at which $300,000 buys all ten | 5.02% |
| Share by decade, daily full curve | 1960s 35%; 1970s and 1980s 100%; 1990s 96%; 2000s 28%; 2010s 0%; 2020s 2% |

What it shows: "one month in four since 1871" is true, but it is almost all one era. In the 156 years, $300,000 bought
the ten in nearly every month from 1966 to 1999 (the great inflation and its slow unwinding) and in about one month in
ten otherwise. Before this September it had happened on a single day since June 2007. The two event claims check out on
this engine with dates attached: 5 Oct 2026 was the cheapest the payments had been since May 2002 (28 Sep: since June
2002). The older line "on no day since 2008" was one day wrong (19 Oct 2023).

### 8f. How small the half kept gets in the years shares fall (`numbers/kept_half.py`, `numbers/results_kept_half_2026-11-10.json`)
Same engine, escrow standard with the fee cushion, range rule on the holdings, Keel's reading of "most", house paths and history windows as section 4.
- **The half kept** is half of the VT bought in January 2028 (about $14,914 at cost centrally), grown to 1 Jan 2033. Where "most" binds, VT is smaller and so is its half (section 4).
- **The excess** is what the floor and the moved half pay above the stated top; under the cap it joins the half kept.
- **"Shares fell"** means VT ended 2031-2033 lower than it began: the two years from the co-sponsor meetings to the contribution.

| | House model (200,000 paths) | History (US stocks, every window since 1871) |
|---|---|---|
| Half kept, 1 Jan 2033: 1-in-100 / 1-in-20 / median / 1-in-20 high | $6,670 / $9,881 / $20,739 / $41,258 | $8,299 / $13,238 / $23,481 / $40,607 |
| As a share of what the floor and the moved half pay (1-in-20 / median / 1-in-20 high) | 9% / 17% / 30% | 11% / 19% / 31% |
| Paths in which shares fell over 2031-2033 | 28.4% | 20.7% |
| Half kept, median, if shares fell over 2031-2033 | $15,423 | $16,164 |
| Half kept, median, if shares rose over 2031-2033 | $23,315 | $25,190 |
| Half kept, median, if shares fell more than 20% over 2031-2033 (7.3% / 5.2% of paths) | $12,964 | $14,481 |
| Half kept, median, if VT ends below its 2028 cost (18.3% / 10.5% of paths) | $12,208 | $13,311 |
| Half kept under $15,000 / under $10,000 | 22.7% / 5.2% of paths | 11.1% / 2.2% of windows |
| Lowest window | | $5,779 (start September 1929) |
| Named starts | | 1973: $13,832; March 2000: $13,289; October 2007: $15,508 |
| **Half kept plus excess:** 1-in-100 / 1-in-20 / median / 1-in-20 high | $12,027 / $16,193 / $28,541 / $49,924 | $15,231 / $20,019 / $30,902 / $48,399 |
| Half kept plus excess, median, if shares fell over 2031-2033 | $23,201 | $23,987 |
| Half kept plus excess, median, if VT ends below its 2028 cost | $19,508 | $20,218 |
| Half kept plus excess under $15,000 / under $10,000 | 3.3% / 0.4% of paths | 0.8% / 0% of windows |
| Half kept plus excess, named starts | | September 1929: $14,259; 1973: $22,036; March 2000: $21,478; October 2007: $22,037 |

What it shows:
- **The risk the morning research flagged is real and has a size.** In the years shares fall, when the IPS expects co-sponsors to cut, the half kept is about a third smaller than when they rise (median about $15,400 against $23,300). In a fall of more than a fifth it is about $13,000.
- **It does not vanish.** Even from September 1929 it is about $5,800, and from every other bad start named above it is close to what was put in. The house model's lowest 1 in 100 ($6,670) is lower than history's, because there "most" has also squeezed VT.
- **The cap adds a second cushion that does not move with shares.** The excess is Treasury money, so the half kept plus the excess has a median of about $23,200 even in the years shares fall, and is under $15,000 in about 3% of house paths.
- **The 2031 range itself does not move,** because the floor and the moved half are Treasuries by then.
- **The honest line:** the half kept is a cushion whose size moves with the markets, smallest in the years it is most likely to be needed. That is a cost of keeping flexibility in shares rather than in Treasuries (section 4, the all-Treasury benchmark).

### 8g. The holdings table Wharton asks for in Section 2, at cost on the original $300,000 (Mon 9 Nov, evening)
Wharton's instructions (`WHARTON_NORTH_STAR.md` section 0): every holding of the final WInS portfolio, with ticker or
identifier, name, asset type, amount and percentage, "expressed using the original $300,000 investment"; the total must
equal $300,000 and 100%; never the ending market value. Source: the WInS export of 23 Oct
(`../../competition/wins/2026-10-23_snapshot.md`): quantity times the price paid on 6-7 Oct (ET). No trade since 8 Oct,
so these are the final holdings. Not a model.

| Ticker or identifier | Name | Asset type | Amount | % of portfolio |
|---|---|---|---|---|
| IBTM | iShares iBonds Dec 2032 Term Treasury ETF | ETF (Treasury) | $97,489.95 | 32.50% |
| IBTO | iShares iBonds Dec 2033 Term Treasury ETF | ETF (Treasury) | $23,408.64 | 7.80% |
| IBTP | iShares iBonds Dec 2034 Term Treasury ETF | ETF (Treasury) | $22,155.30 | 7.39% |
| IBTQ | iShares iBonds Dec 2035 Term Treasury ETF | ETF (Treasury) | $20,973.24 | 6.99% |
| IBTR | iShares iBonds Dec 2036 Term Treasury ETF | ETF (Treasury) | $19,823.72 | 6.61% |
| (WInS id) | T-Bond 4.750% 15-Feb-2037 | Treasury bond | $19,203.80 | 6.40% |
| 532281 (probably) | T-Bond 4.500% 15-May-2038 | Treasury bond | $18,615.26 | 6.20% |
| (WInS id) | T-Bond 4.375% 15-Nov-2039 | Treasury bond | $16,200.95 | 5.40% |
| (WInS id) | T-Bond 4.250% 15-Nov-2040 | Treasury bond | $15,790.32 | 5.26% |
| (WInS id) | T-Bond 3.125% 15-Nov-2041 | Treasury bond | $14,991.00 | 5.00% |
| VT | Vanguard Total World Stock ETF | ETF (equity) | $26,524.61 | 8.84% |
| N/A | Cash | Cash | $3,513.79 | 1.17% |
| N/A | Commissions and bond interest paid at purchase | Cost | $1,309.42 | 0.44% |
| **Total** | | | **$300,000.00** | **100.00%** |

- **Version 2 (Tue 10 Nov, panel 1's bond desk):** the cash row now equals the cash WInS shows ($3,513.79), and the
  $1,309.42 that left the account at purchase has its own row: $200 of commissions (six ETF trades at $25, five bond
  trades at $10) and $1,109.42 that WInS charged on the five bonds, which should be the interest accrued since each
  bond's last coupon. It is not split by bond in the table: WInS used a 15 Aug coupon date on the May-2038 bond, so it
  charged about $225 less than standard accrual would ($1,338 at a 6 Oct settlement; card Q17 row 32, MODEL), and no WInS
  accrued-interest figure is quoted in the report (the 23 Oct snapshot, check 3). Accrued interest is not a loss: it comes
  back with each bond's next coupon. Percentages by largest remainder. The
  version 1 table (cash $4,823.21, 1.61%) is void.
- **Keel's call (logged in `../pm/ASK_HUMANS.md`, Mon 9 Nov):** amounts at cost, because Wharton asks for the "amount
  allocated" out of the original $300,000 and bars the ending value. Cash and the costs row together are $300,000 less the cost of the eleven
  holdings ($295,176.79). Percentages are rounded so that they add to exactly
  100.00% (largest remainder: the May-2038 bond shows 6.20% rather than 6.21%).
- **In groups:** Treasuries 89.55% ($268,652.18: iBond ETFs 61.28%, bonds 28.27%), VT 8.84%, cash 1.17%, costs at purchase 0.44%.
- **Identifiers.** The ETFs use their tickers. Wharton's own example row ("532281 T-Bond 4.500% 15-May-2038") is one of
  Caplet's bonds, so 532281 is probably its WInS identifier; the other four come from Caplet's final WInS export (asked
  of Ray, Mon 9 Nov). Until then the table names the bonds by coupon and date, which identifies them uniquely.
- **The rival reading,** each holding's weight at the final market value times $300,000 (accrued interest left out),
  moves no security by more than 0.25 points at 23 Oct prices (VT 8.59% instead of 8.84%) and cash by 0.02 (1.15% instead of 1.17%; the rival reading has no costs row),
  and would need the final export; Caplet may switch to it.
- **The book was built before the completion standard (card Q17 I5).** VT is 8.84% of the frozen book but 6.63% of the
  $450,000 in the plan on the escrow standard (section 4: $29,829 in January 2028; Tue 10 Nov evening, replacing the void
  7.45% of section 6). Section 2 never says the frozen weights equal the plan.
- **What the table must not be read as:** the WInS book is Laura's whole plan in miniature (the ladder rungs, the
  late-2032 floor stand-in inside IBTM, and VT), not her January 2027 purchase alone. Section 2's text explains this
  once; the evidence is in `CANON.md` and the 23 Oct snapshot's "Pays for" column.

### 8h. The operating reserve from 1 Jan 2033 (`numbers/reserve.py`, `numbers/results_reserve_2026-11-10.json`)
The IPS: "From 2033 the Treasuries are the operating reserve." These are the ten own rungs plus the backstop (Keel's call,
section 2: cost $336,656 in 1 Jan 2027 money, of which the backstop is $34,369), plus money waiting in the Treasury-bill
ETF: the backstop's, and IBTM's payout of 15 Dec 2032 for the first payment.
- **How each holding is valued on a date:** money already received, grown at the rate of each world, plus flows still to come, discounted on the 6 Nov curve's forwards. This is a forward market value if rates follow today's forwards, not a forecast.
- **What is left out:** the facility money (the late-2032 floor and the moved half) is separate and is not in these figures.

**If rates follow today's forwards:**

| 1 January | Reserve before the payment | Own holding pays | Own holding above $50,000 | Backstop covers | Reserve after | Payments still owed | Their value at today's forwards | Funded after | Bonds / iBond ETFs / Treasury-bill ETF after |
|---|---|---|---|---|---|---|---|---|---|
| 2033 | $444,545 | $50,000 | $0 | $0 | $394,545 | $450,000 | $349,089 | 113.0% | 51% / 46% / 3% |
| 2034 | $414,914 | $50,000 | $0 | $0 | $364,914 | $400,000 | $317,111 | 115.1% | 58% / 38% / 4% |
| 2035 | $383,888 | $50,000 | $0 | $0 | $333,888 | $350,000 | $283,600 | 117.7% | 66% / 29% / 5% |
| 2036 | $351,593 | $50,000 | $0 | $0 | $301,593 | $300,000 | $248,639 | 121.3% | 77% / 17% / 6% |
| 2037 | $317,975 | $50,000 | $0 | $0 | $267,975 | $250,000 | $212,144 | 126.3% | 91% / 0% / 9% |
| 2038 | $282,892 | $50,000 | $0 | $0 | $232,892 | $200,000 | $173,954 | 133.9% | 86% / 0% / 14% |
| 2039 | $246,148 | $50,000 | $0 | $0 | $196,148 | $150,000 | $133,855 | 146.5% | 78% / 0% / 22% |
| 2040 | $207,568 | $50,000 | $0 | $0 | $157,568 | $100,000 | $91,648 | 171.9% | 67% / 0% / 33% |
| 2041 | $166,984 | $50,000 | $0 | $0 | $116,984 | $50,000 | $47,124 | 248.2% | 46% / 0% / 54% |
| 2042 | $124,123 | $50,000 | $0 | $0 | $74,123 | $0 | $0 | | all in the Treasury-bill ETF |

**Each payment in four rate worlds** (for Figure 1's per-bar labels). "Own holding" is the rung bought for that payment.
"Backstop covers" is what the backstop's money and any carried surplus in the ETF pay towards it. In every world but
the first, the change starts on 1 Jan 2027 and applies to everything, including the cash inside the iBond funds in
their last months; money waits in the Treasury-bill ETF.

| Payment | Forwards: own holding pays / above $50,000 / backstop covers | Rates 3 points lower for good: own pays / backstop covers | Interest earns nothing: own pays / backstop covers | Earns nothing and the ETF's 0.15% fee: own pays / backstop covers |
|---|---|---|---|---|
| 2033 | $50,000 / $0 / $0 | $48,351 / $1,649 | $47,413 / $2,587 | $47,338 / $2,662 |
| 2034 | $50,000 / $0 / $0 | $47,998 / $2,002 | $46,820 / $3,180 | $46,731 / $3,269 |
| 2035 | $50,000 / $0 / $0 | $47,620 / $2,380 | $46,244 / $3,756 | $46,142 / $3,858 |
| 2036 | $50,000 / $0 / $0 | $47,189 / $2,811 | $45,549 / $4,451 | $45,431 / $4,569 |
| 2037 | $50,000 / $0 / $0 | $46,647 / $3,353 | $44,629 / $5,371 | $44,491 / $5,509 |
| 2038 | $50,000 / $0 / $0 | $45,883 / $4,117 | $43,360 / $6,640 | $43,195 / $6,805 |
| 2039 | $50,000 / $0 / $0 | $45,811 / $4,189 | $43,223 / $6,777 | $43,061 / $6,939 |
| 2040 | $50,000 / $0 / $0 | $45,747 / $4,253 | $43,197 / $6,803 | $43,043 / $6,957 |
| 2041 | $50,000 / $0 / $0 | $45,236 / $4,764 | $42,347 / $7,653 | $42,180 / $7,820 |
| 2042 | $50,000 / $0 / $0 | $45,434 / $4,566 | $42,624 / $7,376 | $42,469 / $7,531 |
| All ten (totals of unrounded figures) | $500,000 / $0 / $0 | $465,917 / $34,083 | $445,405 / $54,595 | $444,080 / $55,920 |
| Left after the last payment, 1 Jan 2042 | $74,123 | $25,651 | $1,414 (the fee cushion) | $0 |
| The same, in 1 Jan 2033 money at that world's own rates | $45,456 | $20,606 ($15,730 if converted at today's forwards) | $1,414 | $0 |

**Composition on 1 Jan 2033, before the first payment** (today's forwards):
- How early each pays out before its payment: the iBond ETFs about half a month (15 December); the Feb-2037 bond 10.5 months; the May-2038 bond 7.6 months; the three November bonds 1.5 months.
- IBTM has already paid out on 15 Dec 2032. On 1 Jan 2033 its $50,000 is cash waiting in the Treasury-bill ETF for that day's payment, so it is counted as cash, not as an iBond ETF.

| Payment | Holding | Own rung | Backstop in the same holding |
|---|---|---|---|
| 2033 | IBTM's payout, now cash in the Treasury-bill ETF | $50,000 | none |
| 2034 | IBTO | $47,545 | none |
| 2035 | IBTP | $45,195 | none |
| 2036 | IBTQ | $42,919 | $421 |
| 2037 | IBTR | $40,708 | $4,054 |
| 2038 | 4.750% Feb 2037 | $38,562 | $5,609 |
| 2039 | 4.500% May 2038 | $36,485 | $5,824 |
| 2040 | 4.375% Nov 2039 | $34,478 | $5,844 |
| 2041 | 4.250% Nov 2040 | $32,534 | $6,788 |
| 2042 | 3.125% Nov 2041 | $30,662 | $6,141 |
| | Treasury-bill ETF (backstop money received to 2032) | | $10,775 |
| **Total $444,545** | | **$399,089** | **$45,456** |

By type: IBTM's payout as cash $50,000 (11.2%), iBond ETFs $180,844 (40.7%), T-bonds $202,926 (45.6%), Treasury-bill ETF $10,775 (2.4%).
The backstop's cost carried to 1 Jan 2033 at forwards is $45,487; its value there is $45,456, the $31 gap being the funds' fee.

**What it shows.**
- **Size:** the reserve is about $445,000 on 1 Jan 2033 if rates follow today's forwards, against $500,000 of payments
  still owed. Those payments are worth $399,089 at the same forwards ($50,000 now plus $349,089).
- **Funded ratio: $444,545 against $399,089, 111.4% funded** on 1 Jan 2033 at today's forwards. That compares like with like, as the panel asked, not with the $500,000 face.
  - The own rungs alone are worth exactly $399,089, because they are sized at today's forwards.
  - The extra $45,456 is the backstop grown to 2033: what makes the payments safe in the world where interest earns nothing.
- **It changes only by running down,** and by the backstop's money gathering in the Treasury-bill ETF.
  - Nothing is sold after January 2028, and nothing is added except each holding's own interest.
  - Each year one own rung pays out just before its payment, so the mix moves from half iBond ETFs to mostly T-bonds by 2037, and to the ETF by the end.
  - No rebalancing: the IPS's two reasons to change are a missed deposit or a Treasury default.
- **Funded after each payment** rises from 113.0% to 248.2%: at forwards the backstop is never drawn, so it becomes a growing share of what is left.
- **Each payment, four worlds (Figure 1).**
  - At forwards, each own holding pays exactly $50,000, $0 above, and the backstop covers nothing.
  - If every reinvestment earns 3 points less, the backstop covers $1,649 (2033) to $4,764 (2041), $34,083 in all, and $25,651 is left.
  - If nothing earns interest, it covers $2,587 to $7,653, $54,595 in all, and $1,414 is left.
  - If nothing earns interest and every waiting dollar pays the ETF's fee, it covers $2,662 to $7,820, $55,920 in all, and nothing is left: the standard is met exactly.
- **What comes back to Laura if forward rates hold:** $74,123 if all of it waits to 1 Jan 2042. That is $45,456 in 1 Jan 2033 money, or $34,345 in 1 Jan 2027 money.
- **Or year by year, under an escrow release** (Keel's reading; the IPS is silent). Each 1 January, the ETF money above what every later payment needs can come back. The test counts what is already in the ETF at its value that day, and everything still to come (coupons, fund payouts and the cash inside the funds) as if it earned nothing from that day (bond desk check, finding 4):

  | Release test | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | 2040 | 2041 | 2042 | Total |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Waiting money earns nothing and pays the ETF's fee (Keel's, matching the design test) | $8,813 | $3,104 | $2,169 | $2,020 | $5,695 | $7,115 | $7,182 | $7,022 | $7,889 | $7,594 | $58,603 |
  | Waiting money earns nothing, no fee | $9,017 | $3,005 | $2,046 | $2,020 | $5,695 | $7,115 | $7,182 | $7,022 | $7,889 | $7,594 | $58,586 |

  - Both totals are the same $45,456 in 2033 money ($34,345 in 2027 money), handed back earlier.
  - The first release is $8,813, not this morning's $10,496: the morning's test counted the coupons still to come at today's forward rates. On the morning's design the corrected test gives $8,530 / $3,015 / $2,182 / $1,888 and so on, $57,126 in all, exactly the bond desk's figures.
- **The waits between payout and payment** (research card Q16, Mon 9 Nov night).
  - The Feb-2037 bond's money waits about 10.5 months for the 1 Jan 2038 payment and earns about $1,572 at today's forwards (3.1% of its payment).
  - The May-2038 bond's waits 7.6 months and earns $1,139 (2.3%).
  - Each November bond's waits 1.5 months and earns $227-$252.
  - The escrow standard covers these even if every wait earns nothing and pays the ETF's fee: the design test assumes exactly that.
  - A Treasury payment due on a weekend or holiday is made the next business day (the Feb-2037 bond pays on Tue 17 Feb 2037), which changes none of these figures materially.
- **The funds' payouts in practice** (Q16).
  - Three iBonds Treasury funds have already ended on schedule (Dec 2023, 2024, 2025), each paying its net asset value to holders 10 to 14 days before 1 January, with notice in mid-October.
  - The 2026 prospectus says money from bonds maturing in a fund's last months is typically reinvested in its remaining notes, so section 3's "earns nothing" case is a stress test, not the expected case.

### 8i. The scenario matrix for Exhibit 3 (`numbers/joint_stress.py`, `numbers/results_joint_stress_2026-11-10.json`)
Added Tue 10 Nov; re-run in the afternoon. This is the plan under the escrow standard (with the fee cushion), the range rule on the fund's holdings and Keel's reading of "most", in five worlds; rates and shares move together where history moved them together. MODEL.
- **Stated ends** are rounded down to $5,000, with the unrounded value in brackets.
- **"Funds pay"** is what the floor and the moved half actually pay along that world's path, their final months included.
- **The contribution** is the lower of what the funds pay and the stated top; the excess joins the half kept.
- **Money left after 2042** is put into 1 Jan 2033 money at that world's own rates (bond desk check, finding 5), not at today's forwards.
- **The joint replays** apply a 1962-2010 window's 1-year Treasury yields in proportion to today's forwards from 1 Jan 2027, and US stocks from the same months one year on: VT is bought in January 2028, one year into the window.

| World | Ten payments | Stated bottom | Stated top | Funds pay | Contribution | Excess | Half kept, 1 Jan 2033 | Half kept plus excess | Left after 2042 (1 Jan 2033 money; nominal) | Completion, Jan 2028 |
|---|---|---|---|---|---|---|---|---|---|---|
| Today's forwards; shares 7.5% a year | All paid | $95,000 ($98,729) | $115,000 ($118,443) | $123,476 | $115,000 | $8,476 | $21,347 | $29,823 | $45,456 ($74,123) | $38,282 |
| Rates 3 points lower for good from Jan 2027; shares 7.5% ("most" binds) | All paid | $80,000 ($80,020) | $95,000 ($96,172) | $97,822 | $95,000 | $2,822 | $18,264 | $21,086 | $20,606 ($25,651) | $49,478 |
| Joint replay from Jul 2007 (rates fall towards zero; VT bought Jul 2008; "most" binds) | All paid | $80,000 ($81,527) | $95,000 ($96,589) | $97,117 | $95,000 | $2,117 | $19,793 | $21,910 | $11,705 ($11,846) | $48,214 |
| Joint replay from Jun 2006 (VT bought Jun 2007, near the 2007 peak) | All paid | $95,000 ($97,501) | $105,000 ($108,859) | $110,053 | $105,000 | $5,053 | $14,423 | $19,476 | $18,775 ($19,114) | $38,881 |
| Inflation world: yields 3 points higher by 2031, shares flat 2028-2033, prices up 5% a year | All paid | $100,000 ($103,862) | $120,000 ($120,774) | $128,467 | $120,000 | $8,467 | $15,175 | $23,641 | $58,861 ($125,731) | $35,990 |

- **The ten are paid in every world.** The worlds differ only in what is left for the building and for Laura.
- **Each stated end is owned in each world.**
  - Rates 3 points lower: "most" sets the floor money at $75,001 (VT $25,521, $1,318 less than 73.3% would give). The floor's zero-interest payout from its trade day is $80,422 against the stated $80,000, and it actually pays $81,445. This replaces this morning's row, where the floor's zero-interest payout was $79,864 against a stated $80,000.
  - Jul 2007: floor money $75,001; the floor actually pays $81,984 against the stated $80,000.
  - Inflation world: the floor's zero-interest payout is $104,384 and it actually pays $110,786, against the stated $100,000.
- **The inflation world's contribution buys less.** It is $120,000, worth $89,546 in 1 Jan 2027 dollars at 5% a year. With shares down 20% over 2028-2031 as well (1973-74 style), the top is $115,000 ($117,392) and the half kept $12,140.
- **Money left after 2042 depends on which rates convert it.** At today's forwards the rates-3-lower world's $25,651 would read $15,730 and the inflation world's $125,731 would read $77,104; at their own rates they are $20,606 and $58,861.
- **Every one of the 585 joint windows (Jan 1962 to Sep 2010 starts):**

  | | 1-in-20 low | Median | 1-in-20 high |
  |---|---|---|---|
  | Stated bottom | $80,000 | $95,000 | $115,000 |
  | Stated top | $95,000 | $115,000 | $140,000 |
  | Half kept | $13,874 | $23,601 | $42,015 |
  | Left after 2042 (1 Jan 2033 money, own rates) | $18,053 | $43,469 | $84,845 |
  | Completion, January 2028 | $29,995 | $38,397 | $47,706 |

  - The ten are paid in full in every window.
  - The floor never paid less than the stated bottom (smallest margin $1,262), and the funds always paid at least the stated top (smallest margin $934). Measured at zero interest from each trade day, the smallest margins are $458 and $532.
  - "Most" binds in 30 windows (section 4).
  - The lowest stated bottom was $75,000 (starts including Nov 2000, Apr 2007 and Jan 2008); the lowest stated top $90,000 (starts including Oct 2000, Apr 2007 and Jan 2008).
- **Other named windows:** Jan 2000, $90,000 to $100,000; Jan 2008, $75,000 to $90,000 (completion $55,006, "most" binds); Jan 1973, $105,000 to $125,000.
- **Two figures for the Jul 2007 window.** `range_rule.py` gives $98,386 for what the funds pay there, against $97,117 here. There, the funds' final months follow today's forwards; here, they follow the window's own rates. Exhibit 3 uses this table.

### 8j. The Taiwan dollar test on the Tue 10 Nov register (`numbers/joint_stress.py`, block `twd_test` of `numbers/results_joint_stress_2026-11-10.json`). MODEL
Added Tue 10 Nov evening. Design H_plain with the fee cushion, the range rule on the fund's holdings, Keel's reading of
"most" (sections 2 to 4). It replaces card Q24's Mon 9 Nov test (verdict 3), whose figures are void (section 10).
- **The question** (bond desk, card Q24 claim 3). The contribution is fixed in US dollars at the 2031 meetings and is
  spent in Taiwan dollars from December 2032. If the Taiwan dollar strengthens in between, the same NT$ budget needs
  more US dollars. Does the money that comes back to Laura in 2033 cover that extra?
- **Which gift.** Every test uses the 2033 contribution after the cap: the lower of what the floor and the moved half
  pay and the stated top (section 4, "One definition, used everywhere"). In every house path, history window and joint
  window the funds pay at least the stated top, so the contribution equals the stated top: $115,000 centrally; house
  $95,000 / $115,000 / $140,000. It is never what the funds pay before the cap ($123,476 centrally).
  - This afternoon's JSON divided the half kept by what the funds pay before the cap. That gave the 90.9% the evening
    brief quoted; on the contribution it is 93.2%. Its 99.77% with the excess was already on the contribution.
- **"10% stronger"** means 10% more US dollars for the same NT$ budget, 8d's convention (NT$ per US$ from 32.768 to
  32.768 / 1.10 = 29.79). The stricter reading, NT$ per US$ down 10% (to 29.49), needs 11.1% more and is shown beside it.
- **Two pots.** The half kept alone (VT's market value on 1 Jan 2033, MODEL). And the half kept plus the excess the cap sends to it (paid on
  or about 15 Dec 2032, counted at face as in section 4). The need is 10% of the contribution, in December 2032 money; every gap below is the
  need less the pot, at face, in the same money.

| Test (gift = the contribution after the cap) | House model (200,000 paths, seed 2033) | US stock history (1,770 windows since 1871; rates at today's forwards) | Joint replay (585 windows, 1962-2010 starts; each on its own rates) |
|---|---|---|---|
| **Half kept alone covers a 10% stronger Taiwan dollar** | **93.2%** (fails in 13,618 paths, about 1 in 15) | **96.9%** (fails in 54) | **99.3%** (fails in 4) |
| Gap when it fails: median (95th percentile of the gaps / largest) | $1,407 ($4,553 / $8,500) | $1,795 ($4,860 / $5,756) | $746 (largest $1,022) |
| Largest move covered 19 in 20 (more US dollars needed) | 9.4% (NT$ per US$ down to 29.96) | 11.8% | 11.6% |
| Stricter reading (11.1% more): covered / median gap | 89.1% / $1,699 | 96.0% / $2,513 | 97.3% / $1,170 |
| **Half kept plus the excess covers a 10% stronger Taiwan dollar** | **99.77%** (fails in 467 paths, about 1 in 430) | **100%** | **100%** |
| Gap when it fails: median (largest) | $1,280 ($6,083) | none | none |
| Largest move covered 19 in 20 | 15.6% (NT$ per US$ down to 28.34) | 17.5% | 17.6% |
| Stricter reading: covered | 99.56% | 100% | 100% |
| The half kept, 1 Jan 2033: 1-in-20 low / median / 1-in-20 high | $9,881 / $20,739 / $41,258 | $13,238 / $23,481 / $40,607 | $13,874 / $23,601 / $42,015 |
| The half kept plus the excess: the same | $16,193 / $28,541 / $49,924 | $20,019 / $30,902 / $48,399 | $19,690 / $31,809 / $49,629 |
| Against an overrun allowance of 13% / 17% of the contribution (Q5's early-stage norms; an illustration, never a cost estimate): half kept alone | 79.7% / 54.9% | 90.1% / 67.0% | 87.5% / 67.7% |
| The same, half kept plus the excess | 98.7% / 91.0% | 99.4% / 95.8% | 100% / 96.8% |

- **Central case** (today's forwards, VT 7.5% a year). A 10% stronger Taiwan dollar on $115,000 needs $11,500 more in
  December 2032. The half kept ($21,347) covers it 1.9 times; with the excess ($29,823), 2.6 times. At the ten-year
  strongest rate (27.52, 19.1% more US dollars) the need is $21,930: the half kept alone is $583 short, and with the
  excess it is covered with $7,893 to spare (8d).
- **On the real Taiwan dollar** (Fed G.5 monthly, FRED EXTAUS, Oct 1983 to Sep 2026, the repo mirror
  `keel/models/data/twd_per_usd_monthly.csv`, VERIFIED against FRED EXTAUS, all 516 months, Wed 11 Nov, 8l; US stocks from the same months; rates at today's
  forwards). 417 windows, VT bought Oct 1983 to Jun 2018. The move is measured from the meetings (36 months after VT is
  bought; Jan 2031 in the plan) to the gift (60 months; Jan 2033), on each window's contribution after the cap ($110,000 /
  $120,000 / $130,000, 1-in-20 low / median / high).
  - The two-year move, in US dollars needed: 1-in-20 -12.7% (Taiwan dollar weaker), median +0.1%, 1-in-20 +13.7%; the
    largest +29.4% (VT bought Nov 1983: the 1986-1988 appreciation). It moved 10% or more against Laura in 11.0% of
    windows, and against her at all in 51.1%.
  - **The half kept alone covered the actual move in 98.1% of windows** (fails in 8: VT bought Oct 1983 to Mar 1984,
    and Feb and Mar 2006). Median gap when it fails $1,833; largest $7,312 (Nov 1983).
  - **With the excess: 99.8%** (fails in 1: Nov 1983, $1,755 short).
  - The move's correlation with shares over the same two years: +0.09, close to none.
- **The contribution in other money** (block `gift_terms`, on 8d's conventions; agrees with 8d to the dollar): the
  central $115,000, paid December 2032, is NT$3.77m at 32.768, NT$3.43m if the Taiwan dollar is 10% stronger, and
  NT$3.16m at 27.52. It is $99,747 in 1 Jan 2027 US dollars at 2.4% inflation, and NT$3.14m of today's building at 3%.

What it shows:
- **On the register's own definitions, "19 in 20" holds for the half kept alone on history and in the joint replay,
  but not in the house model** (93.2%: about 1 path in 15 fails, by about $1,400 at the median). The house model is the
  harshest mainly because its shares grow more slowly: a median 7.5% a year against about 9.6% in the US history windows
  (Keel arithmetic on the same Shiller series; the spreads are close, 17.88% against about 16-18%). It also moves yields
  before 2028, so "most" squeezes VT in 16.9% of its paths.
- **Counting the excess, it fails in about 1 house path in 430 and in no history or joint window.** The excess is
  Treasury money, fixed once the half is moved in 2031, so the weaker part of the pot is always the half kept.
- **On the real currency since 1983, 98 windows in 100 for the half kept alone, and all but one with the excess.** The
  one failure is the 1986-1988 appreciation, the largest two-year move in the series.
- **The test is about one use of the pot only.** The IPS names three (l.15: overruns, a stronger Taiwan dollar, a
  co-sponsor falling short); the overrun rows show how fast the pot is used when they come together.

### 8k. What returns to Laura (`numbers/joint_stress.py`, block `returns_to_laura`; checked by `numbers/returns_check.py`, `numbers/results_returns_2026-11-10.json`). MODEL
Added Tue 10 Nov evening for part 3b. Same design as 8j. Three parts come back to Laura; none is promised to anyone.

**At today's forward rates, shares at 7.5% a year:**

| Part | What it is | When it is hers | Amount in its own money | In 1 Jan 2033 money (today's forwards) | Source |
|---|---|---|---|---|---|
| The backstop's money | Section 2's backstop, never needed at forwards | After the last payment, 1 Jan 2042; or year by year under an escrow release (8h; Keel's reading, not in the IPS) | $74,123 on 1 Jan 2042 (or $58,603 released 2033-2042, nominal; $8,813 on 1 Jan 2033) | $45,456 | 8h; `results_reserve_2026-11-10.json` |
| The excess | What the floor and the moved half pay above the stated top (the cap, CANON D12) | When the funds pay, on or about 15 Dec 2032 | $8,476 on 15 Dec 2032 | $8,495 | Section 4 |
| The half kept | Half of VT, promised to no one (IPS l.15) | Always; she can sell it any trading day | $21,347 on 1 Jan 2033 (a market value at the central 7.5%) | $21,347 | Section 4 |
| **Total** | | | | **$75,298** | `returns_to_laura.forwards` |

- Counting the excess at face (17 days early), as section 4 does: $75,278; the rounded parts add to $75,279.
- In 1 Jan 2027 money: $56,894.
- **Two kinds of money, not one** (card Q25, Tue 10 Nov evening): the backstop's money is $45,456, 60.4% of what
  returns; it is the price of the payments' certainty, sized for zero interest, and comes back only because rates held.
  The flexibility (half kept plus excess) is $29,823, 39.6%. Only the second is money Laura chose not to promise.
- **What Laura can use in January 2033 is less.** It is the half kept and the excess, $29,823 (section 4). Add the first
  escrow release, $8,813 on 1 Jan 2033 (8h), if the release is used. The rest of the backstop's money comes back only as
  the payments no longer need it.

**Where Laura's $450,000 ends, at today's forwards** (1 Jan 2033 money; at forwards the shares are the same in any money year):
- The two deposits grown at forward rates to 1 Jan 2033 ($300,000 from 1 Jan 2027, $150,000 from 1 Jan 2028): $587,141.
- **Promised money: $514,357, 87.6% of that.** It is the ten payments, $399,089 (their forward value on 1 Jan 2033;
  $500,000 nominal, 2033-2042), plus the contribution, $115,268 ($115,000 paid in December 2032).
- **What returns to Laura: $75,298, 12.8%.**
- The two add to 100.4%. VT's growth above forward rates ($3,918, net of VT's fee) less every iBond fund's fee ($1,402)
  adds 0.4%.
- **Of all the money at the end ($589,655), 87.2% is promised** (payments 67.7%, contribution 19.5%) **and 12.8% returns
  to Laura.**
- Do not add nominal dollars across years ($500,000 plus $115,000 against $74,123 plus $8,476 plus $21,347): they fall
  in different years.

**Across the 585 joint windows** (rates and US stocks from the same months, as 8i). Each part is in 1 Jan 2033 money at
the window's own rates; the excess is carried 17 days at the window's rate:

| | 1-in-20 low | Median | 1-in-20 high |
|---|---|---|---|
| The backstop's money | $18,053 | $43,469 | $84,845 |
| The excess | $3,526 | $7,698 | $13,196 |
| The half kept | $13,874 | $23,601 | $42,015 |
| **Total, each window's sum** | **$40,404** | **$78,584** | **$120,375** |
| Share of all the money that returns (the rest is the payments and the contribution, at the window's own rates) | 7.0% | 13.3% | 19.1% |

- Each row's percentiles are its own, so the rows do not add.
- **Lowest total $32,148** (start Mar 2007: rates fall to near zero and VT is bought in March 2008; backstop $14,361,
  excess $2,325, half kept $15,461). 1-in-100 $33,607. Never under $25,000; under $50,000 in 9.7% of windows.
- The backstop's money and the half kept barely move together across windows (correlation -0.16), so the total is
  steadier than its parts.
- The ten are paid in full in every window (8i); only what comes back varies.

**The check by a different calculation** (`numbers/returns_check.py`; the promise is tested by a calculation other than
the one that sized it):
- **Route 1, other files.** The backstop's 1 Jan 2033 value from `reserve.py`'s composition (its holdings and waiting
  cash that day), $45,456, plus `range_rule.py`'s excess ($8,476) and half kept ($21,347): $75,279 at face, against
  joint_stress's $75,278. The $0.14 is `range_rule.py`'s rounding to the dollar. Three routes to the backstop's 2033 value
  agree to the cent: the composition, the ledger run to 2042 and brought back, and the escrow release schedule.
- **Route 2, value conservation, with no ledger, no reserve and no plan.run.** At forwards every Treasury dollar is
  bought at a forward price and earns forward rates. So, in 1 Jan 2033 money, what returns = the deposits grown
  ($587,141) + VT's growth above forwards, net of its fee ($3,918) - the iBond funds' fee on the rungs, the backstop,
  the floor and the moved half ($1,402) - the payments' forward value ($399,089) - the contribution ($115,268) =
  **$75,300**.
- **Difference from joint_stress: $1.48** (0.002%). $1.44 of it is a convention in `plan.py`. The January 2028
  completion is carried a year at the 2027 forward rate as if 2027 had 365.25 days, so it costs $1.14 more than a
  forward carry ($38,282.14 against $38,281.00, January 2028 money), and the floor and VT get that much less between them. Left as it is: it moves the
  completion and the floor money by $1 and nothing a reader sees (section 9).

### 8l. How much room the 2031 range leaves, path by path; and the Taiwan dollar file checked at FRED (`numbers/range_margin.py`, `numbers/results_range_margin_2026-11-11.json`). MODEL
Added Wed 11 Nov evening (numbers owner) for part 3c and card Q4c (its Gaps: "the smallest in-range margin across
paths"). Nothing is re-sized and no earlier figure moves. Same register as sections 3, 4 and 8i: design H_plain with
the fee cushion, the range rule on the fund's holdings, Keel's reading of "most".
- **The claim tested:** "After the 2031 move the gift stays inside the stated range with room to spare in every path,
  and the range never collapses to one figure."
- **Definitions, exactly as section 4.** Each stated end is the money put into the late-2032 fund times what $1 of the
  fund's own holdings pays on 15 Dec 2032 if nothing earns interest from the trade day, less 0.5%, rounded down to
  $5,000. The bottom is fixed when the floor is bought (January 2028); the top at the 2031 move. The 2033 contribution
  is the lower of what the floor and the moved half pay and the stated top; the excess joins the half kept.
- **What the funds pay:** house model and US stock history as section 4 (at their purchase yields); joint replay as 8i
  (realised on each window's own rates). The script builds the first two with `plan.run` and `completion.rule`, as
  `range_rule.py` does, and the joint replay by running `joint_stress.py`'s own setup code (none of its results
  blocks). It reproduces 8i to the dollar: $458, $532, $1,262 and $934, and the stated ends' 1-in-20 points.
- **Rerun:** `python3 -I keel/final_report/numbers/range_margin.py` from the repo root (about 15 seconds). It reads
  `results_joint_stress_2026-11-10.json` only to show the match, and writes nothing else.

| Measure (central case in brackets) | House model (200,000 paths, seed 2033) | US stock history (1,770 windows since 1871; rates at today's forwards) | Joint replay (585 windows, 1962-2010 starts) |
|---|---|---|---|
| **(i) Contribution less the stated bottom** ($20,000): 1-in-20 low / median / smallest | $10,000 / $20,000 / **$0** | $15,000 / $20,000 / $5,000 | $10,000 / $20,000 / $10,000 |
| Contribution equal to the bottom (no room) / below it | **254 paths (0.127%, about 1 in 790)** / none | none / none | none / none |
| **(ii) Width: stated top less stated bottom** ($20,000): 1-in-20 low / median / 1-in-20 high | $10,000 / $20,000 / $35,000 | $15,000 / $20,000 / $35,000 | $10,000 / $20,000 / $35,000 |
| Width $0, a single figure | **254 (0.127%)** | 0 | 0 |
| Width $5,000 | 3,040 (1.52%) | 13 (0.73%: VT bought Jan 1929 to Apr 1930) | 0 |
| Width $10,000 or more | 98.35% | 99.27% | 100% (narrowest $10,000) |
| **(iii) Contribution less the stated top**, funds paying as modelled ($0) | $0 in every path | $0 in every window | $0 in every window |
| The same if the funds pay only their holdings' zero-interest payout less a fund cost of 0.5% ($0) | $0 in every path | $0 | $0 |
| Fund cost 0.75%: top missed in / largest gap / median gap where missed ($0 centrally) | 11,984 paths (5.99%) / $429 / $153 | 112 windows (6.3%) / $312 / $142 | 34 windows (5.8%) / $312 / $151 |
| Fund cost 0.75%: contribution below the stated bottom | **1 path ($211 below)** | 0 | 0 |
| Fund cost 1%: top missed / largest gap; below the bottom | 12.0% / $881; 5 paths (up to $425 below) | 13.1% / $626; 0 | 12.3% / $664; 0 |
| **(iv) Excess** at face, 15 Dec 2032 ($8,476): 1-in-20 low / median / 1-in-20 high / smallest | $4,340 / $7,629 / $11,218 / $1,251 | $5,322 / $7,524 / $9,846 / $4,640 | $3,522 / $7,671 / $13,134 / $934 |
| **(v) Floor's zero-interest payout less the stated bottom** ($4,225): 1-in-20 low / median / smallest | $749 / $3,001 / **$405** | $4,225 in every window (the floor is bought at forwards) | $811 / $3,024 / **$458** (start Feb 2002) |
| **Both funds' zero-interest payout less the stated top** ($4,039): the same | $851 / $3,101 / **$430** | $848 / $3,064 / **$533** (start Dec 1929) | $872 / $3,144 / **$532** (start Aug 2010) |
| What the floor pays less the bottom; what both pay less the top: smallest | $1,063; $1,251 | $8,178; $4,640 | $1,262; $934 |
| Card Q4c's measure: both funds' zero-interest payout less 0.5%, less the stated bottom ($23,443): 1-in-20 low / median / smallest | $12,456 / $21,790 / $3 | $16,942 / $24,740 / $7,133 | $14,196 / $24,106 / $10,891 |
| Largest fund cost covered at zero interest in every path: bottom / top | 0.50% / 0.50% | 4.26% / 0.50% | 0.51% / 0.50% |

- In every path and window the funds pay at least the stated top, so (i) equals (ii) everywhere: the room above the
  bottom is the width of the range.
- **Where the range is one figure (254 house paths).**
  - Every one is a path where "most" binds. Yields fell before January 2028 (median 2.3 points), the completion took
    most of the $150,000, and VT bought was a median $3,765. In 55 paths (0.028%) nothing was left for VT at all: the
    completion took $75,000 or more.
  - The single figure is a median $80,000 (from $65,000 to $90,000). The contribution equals it, and the excess
    (median $5,998, smallest $1,917) joins the half kept.
  - Section 4's "VT worthless" row ($95,000, one figure) is the same case at the centre.
  - A range $5,000 wide: 3,040 house paths, 85% of them with "most" binding (VT a median 18% down by the move); in the
    stock history, the 13 windows with VT bought Jan 1929 to Apr 1930 (VT a median 68% down).
- **The 0.75% case.** Beyond the rule's 0.5% cut, only the top is missed, by at most $429, except where the range is
  one figure: then a missed top is a missed bottom (1 house path in 200,000 at 0.75%; 0 with seed 2034).
- **The smallest margins are the 0.5% cut, by construction.** Each end is at most 99.5% of its zero-interest value,
  so its margin is at least 0.5% of that value (about $400 to $600) plus whatever the rounding leaves. Card N-04's
  "$458 and $532 across 585 historical windows" is right as worded; keep "historical windows" in any use, since the
  house model goes to $405 and $430.

**The check by a different calculation** (functions ending in 2 in `range_margin.py`; the margins are tested by a
calculation other than the one that set them):
- **Route 2.** It takes only each path's money left after the completion, its draws or window inputs and the curve's
  discount factors. It re-derives the IBTM holdings (coupon 4.2513%, the engine's figure), the "most" split, VT and the
  moved half, each end's zero-interest payout, the rounding (whole dollars, integer division), what the funds pay (in
  the joint replay, from each window's 1-year yield ratios), the contribution and the excess. It calls none of
  `completion.rule`, `completion.zero_per_dollar`, `plan.run` or `joint_stress.py`'s functions.
  - **Result:** every stated end is identical in all 202,355 paths and windows. Every dollar figure agrees to within a
    millionth of a cent, and every count and percentile in the table is the same.
- **No-model checks.**
  - Each margin lies between 0.5% of its end's zero-interest value and that plus $5,000, in every path (no breaks).
    The lowest possible margins are $333 (house) and $386 (joint floor); the smallest found are just above them.
  - A one-figure range needs the moved half, after the cut, to be under $5,000 (693 house paths). If the rounding
    remainder were spread evenly, 247 of them would round to one figure; 254 do.
- **Sampling.** The house model drawn again with seed 2034 gives:
  - one-figure ranges 236, $5,000 ranges 3,032;
  - at 0.75%, top missed 11,951 and none below the bottom;
  - smallest margins $421 and $433;
  - excess $4,368 / $7,637 / $11,218, smallest $1,184.
  So "about 1 path in 800" holds, and the one 0.75% path below the bottom is noise around zero.
- **A stricter reading.** The rule counts the funds' monthly distributions at face. Suppose instead they wait in the
  Treasury-bill ETF at its 0.15% a year fee, section 0's rule for waiting money.
  - Centrally the floor's zero-interest payout falls by $69 and the moved half's by $3.
  - Every end is still owned in every path. The smallest margins become $349 and $370 (house), $399 and $472
    (joint) and $4,155 and $463 (history).
  - The largest fund cost covered in every path falls from 0.50% to about 0.43%.

**Verdict on the claim: CHANGE.**
- **"Inside the stated range in every path": KEEP.** It is true in all 200,000 house paths, 1,770 stock windows and 585
  joint windows. It holds at the funds' modelled payouts, and at zero interest after fund costs up to 0.5%.
- **"With room to spare in every path": CHANGE.**
  - The room above the bottom is $10,000 or more in 98.35% of house paths, 99.27% of stock windows and every joint
    window. It is $0 in 254 house paths (1-in-20 $10,000, median $20,000).
  - The room between what is owned and what is stated is at least 0.5% of each end. The smallest is $405 and $430
    (house), $458 and $532 (joint) and $4,225 and $533 (history).
- **"The range never collapses to one figure": KILL** for the house model: 254 paths in 200,000 (0.127%; 236 with
  another seed). It holds in the stock history and the joint replay.
  - One figure means yields fell about 2 points before January 2028 and left almost nothing for VT, or VT became
    worthless.
  - So "a range, not one figure" is not certain from today. From January 2028 it turns only on what VT and the
    moved half's yield are on the move day.

**The Taiwan dollar file, checked at the source (8j).**
- **Read:** FRED series EXTAUS at https://fred.stlouisfed.org/data/EXTAUS.txt, Wed 11 Nov 2026. That is FRED's own
  table page: "Last Updated 2026-11-02"; release G.5 Foreign Exchange Rates; monthly averages of daily noon buying
  rates in New York. The whole table was read through a fetch service (its copy dated 8 Nov 2026). Nine months were
  read again live the same day: Nov 1983, Dec 1987, Nov 1997, Jan 1998, Mar 2008, Dec 2020, Oct 2022, Sep and Oct 2026.
  The CSV link (`fredgraph.csv?id=EXTAUS`) did not load (binary or fetch error), and curl is refused.
- **Compared:** all 516 months of the mirror, Oct 1983 to Sep 2026. That includes every month of 1987, 1997-98, 2008,
  2020 and 2022, and the mirror's latest month (Sep 2026, 31.7381). All 516 are identical to the series' four
  decimals. FRED adds Oct 2026 (32.2695, preliminary), which 8j does not use (its last month is Jun 2023).
- **So 8j's real-currency figures are VERIFIED as to their data.** Nothing is re-run and no figure changes.
- **Label:** the monthly series comes from the Fed's G.5 release; H.10, the name 8j uses, is the daily release that
  the monthly figures average.
- **Reference:** `research/REFERENCES_APA.md` holds the daily series DEXTAUS (entry 16), not the monthly EXTAUS that 8j
  uses. Add EXTAUS before 8j's real-currency figures are cited.

### 8m. The WInS book against the targets set before trading (Section 2.5; card Q29). Team record and register, checked Wed 11 Nov evening
The book is the plan after both deposits at two-thirds scale (300/450; the WInS notes say "scaled to the model portfolio", CANON A18, D3). These are the criteria on file before the first fill (6 Oct ET) and the result against each. Sources: the Portfolio tab's target units (`caplet/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv` l.20-31; exported 14 Oct, after the fills, but priced on 2 Oct closes and 5 Oct bond checks), the pre-trade ticket file (`archive/rab/trades/tickets.md` l.7-13, trade date Fri 2 Oct) and the 23 Oct WInS snapshot (`competition/wins/2026-10-23_snapshot.md` l.22-32).

| Criterion set before trading | Result | Basis |
|---|---|---|
| Units of each Treasury holding (IBTM 4,503; IBTO 1,024; IBTP 927; IBTQ 894; IBTR 853; bonds 20, 20, 18, 18, 20 lots of $1,000) | All ten held at exactly the target units | portfolio.csv against the snapshot |
| VT sized "from the cash then left", bought last (order 11) | 167 shares against 164 at 2 Oct prices; filled last (7 Oct, 8:27 PM ET), after the two longest bonds were filled first (6 Oct) | portfolio.csv l.30; snapshot; card Q29 row 14 |
| Bonds within 25 basis points of the Treasury curve | -10 to +6 basis points at the 5 Oct check; 2.6 to 8.8 at the fills (card Q17, MODEL) | portfolio.csv l.25-29; Q17 |
| Cash never below $1,000 | $3,513.79 at the end | 8g |
| Cost | Commissions $200, 0.067% (6.7 basis points) of $300,000; 11 of 200 trades | 8g |
| Each payment has a holding that pays out before it | 10 of 10: the five iBond funds about 17 days before each 1 January; the Nov-2039, Nov-2040 and Nov-2041 bonds 47 days; the May-2038 bond 231 days ("7.5 months" in the Trading Notes' words); the Feb-2037 bond 320 days (10.5 months) | CANON B8; 8h |
| Each rung at two-thirds of a full $50,000 rung | 65.6% to 70.4% (whole ladder 68.0%); not exactly 66.7% because bonds trade in $1,000 lots | card Q17, MODEL, register engine at the 23 Oct curve |

- **What the scale changes and what it does not.** No promised money is in shares, in the book or in the plan (IPS l.11). The weights do not carry over one for one: VT is 8.84% of the book at cost and 6.63% of the $450,000 plan (8g), because the book holds no 2028 completion and no backstop. So never write that "the Treasury share is unchanged" by the scaling.
- **Measured afterwards, and labelled so.** The sufficiency standard ("sufficient without reinvestment", section 2) and Q17's measures came after the freeze (Tue 10 Nov and Mon 9 Nov). The WInS notes say the book relies on "reinvested coupons funding part of each" (CANON A18), so 2.5 never presents the escrow test as a criterion the book was built to.

## 9. Still to add (later days)
- **The exhibits are not yet re-built on these figures.** `exhibits/exhibit_data.py` reads 8h (per payment: own holding above $50,000 and backstop cover, now in four worlds), section 4 and 8i (Exhibit 3). Re-run it, then `exhibits/build_exhibits.py`; this register run did not touch them. `exhibit_data.py` should read the backstop's value on 1 Jan 2033 ($45,456), not its cost carried ($45,487).
- **Cards Q19, Q20 and Q24 refresh to these figures** (section 10). Q24's Taiwan dollar test (verdict 3, rows 22-25, card 4) is replaced by 8j.
- **8j and 8k were added Tue 10 Nov evening.** Still open from them:
  - SKELETON 3b's Taiwan dollar sentence was written "to be re-run before use"; it is now re-run (section 10 gives the replacement).
  - The Taiwan dollar file is a repo mirror (`keel/models/data/twd_per_usd_monthly.csv`), UNVERIFIED against FRED EXTAUS. A later run checks a few months against FRED before 8j's real-currency figures are quoted.
- **8l added Wed 11 Nov evening:** the Taiwan dollar item above is closed (all 516 months match FRED EXTAUS); still open from 8l: an EXTAUS entry in `research/REFERENCES_APA.md` (it holds only the daily DEXTAUS), and cards Q4c, Q19 and N-04 to quote 8l's margins with their bases. 8j's source label was corrected to G.5 the same evening.
  - An exhibit for 3b, if one is wanted, reads `returns_to_laura` in `numbers/results_joint_stress_2026-11-10.json`.
  - `plan.py` carries the January 2028 completion a year as if 2027 had 365.25 days ($1.14 too much; 8k's check). Fix it on the next full re-run, not alone: it moves the completion to $38,281 and the floor money to $81,890 in every file.
- **Two checks only a student can make:** which Treasury-bill ETF WInS lists, with its fee (section 0; the cushion is sized for 0.15% a year); and IBTM's prospectus wording on what may make the fund pay less than its holdings (section 3).
- `pooled.py` (card Q20) still compares the designs at exactly 0%, with the old fixed deductions; it is a record, not a source.
- Later days add what the research rounds and the skeleton ask for.

## 10. Files that still quote a void figure (Tue 10 Nov afternoon, with evening rows; listed, not edited)
Paths are under `keel/final_report/` unless shown. Each file's owner changes it, using the section named as the replacement. Line numbers are as of Tue 10 Nov afternoon; rows marked "(evening)" were added Tue 10 Nov evening for 8j.

**Planning files**

| File | Line | Quotes | Replace with |
|---|---|---|---|
| INTENT.md | 36-37 | Reserve "about $427,000" against "$399,000", "about 107% funded" | $444,545 against $399,089, 111.4% funded (8h) |
| INTENT.md | 43 | Range "about $110,000 to $130,000" | About $95,000 to $115,000 on today's figures (section 4) |
| SKELETON.md | 40 | 2028 deposit's first "about $24,500"; reserve "$427,000" against "$399,000", "107%" | About $38,300 (section 2); $444,545 against $399,089, 111.4% (8h) |
| SKELETON.md (evening) | 41 | Taiwan dollar test "about 93 house paths in 100 (97% in the joint history replay)", "about 1 in 14 it does not", "99.97%" with the excess (Mon 9 Nov design, "to be re-run") | On the contribution after the cap (8j): half kept alone 93.2% of house paths (about 1 in 15 fails), 96.9% of history windows, 99.3% of joint windows; with the excess 99.77% (about 1 in 430 fails), 100%, 100%; on the real Taiwan dollar since 1983, 98.1% and 99.8% |
| CASE_MAP.md | 40 | "Keel's call ... margin $21,149" (Mon 9 Nov settlement) | Escrow standard with the fee cushion: backstop $34,369, cost $336,656 (section 2) |
| CASE_MAP.md | 57 | Floor "up to 4.1%"; stated bottom "less 4.1%" | The range rule on the fund's holdings, less 0.5%; 4.31% today (section 3) |
| CASE_MAP.md | 75 | All-Treasury $158,157; 98%; 63% | $140,761 (stated $130,000); 97.6%; 62.8% (section 4) |
| SCORECARD.md | 71 | "the $21,500 half kept" | $21,347 (about $21,300), with the excess $29,823 (section 4). Line 60 is a dated note and stays |
| ARGUMENT_LOG.md | 8, 10, 14 | $24,500, 107%, $427,000 / $399,000, $21,149, 94%, 4.1%, $110,000 bottom, $110,000 to $135,000 | Dated records: leave as history; new rows use sections 2, 3, 4 and 8h |
| exhibits/specs.md | 53 | Per rung "$1,705 ... $5,266 ($36,859 in all)" above $50,000 | $0 above $50,000 for every own rung at forwards; backstop cover per payment in 8h's four-world table |
| exhibits/specs.md | 58 | "$427,028 falling to $55,025"; "107% funded" | $444,545 falling to $124,123 before the last payment; 111.4% (8h) |
| exhibits/specs.md | 68 | $110,000 to $130,000; $138,735; $115,929; $22,806; $23,986 | The 8i forwards row: $95,000 to $115,000; funds pay $123,476; contribution $115,000; excess $8,476; half kept $21,347 |
| exhibits/specs.md | 79 | Bottom $93k / $116k / $140k; top $111k / $139k / $171k | Floor payout $88,047 / $103,097 / $124,380; stated bottom $85,000 / $95,000 / $115,000; stated top $95,000 / $115,000 / $140,000 (section 4) |
| exhibits/specs.md | 93-94 | All-Treasury $158,157; median top $138,735; "$164k against $158k", "$128k against $127k" | $140,761; funds pay $123,476, stated top $115,000; $145,687 against $140,649 and $113,449 against $113,169 (section 4) |
| exhibits/exhibit_data.py | 74-77, 95 | 8h per-rung $1,705 to $5,266, $36,859 (and the check against it); `RESERVE_FIRST_PAYMENT_TOTAL = 427028` | Re-run from 8h (do not hand-edit) |
| exhibits/exhibit_data.py | 109-112 | Exhibit 3 central row: $110,000 to $130,000*, $138,735*, $23,986 | Re-run from 8i |
| exhibits/exhibit_data.py | 122-127 | House bands (93000, 115929, 140000), (111000, 138735, 171000), (12000, 23986, 47000); stated $110,000 / $130,000 | Re-run from section 4 |
| exhibits/build_exhibits.py and exhibits/exhibit2_reserve.svg (lines 553, 625 show +$1,705 and +$5,266) | | Built from exhibit_data.py | Re-run after exhibit_data.py |

**Research cards** (`research/cards/`)

| Card | Lines | Quotes | Replace with |
|---|---|---|---|
| Q5_is_half_right.md | 24, 84 | Kept half $12,150 / $23,831 / $46,746 | $9,881 / $20,739 / $41,258 (section 4) |
| Q5_is_half_right.md | 37, 84 | $23,986 as 17.8% of $135,000; shares of $110k-$135k | $21,347; 17% of what the funds pay (8f); range $95,000 to $115,000 |
| Q5_is_half_right.md | 117, 218 | Overflow $27,990; "about $134k" with certainty | $45,456 (2033 money); $120,023, stated $110,000 (section 4, C8) |
| Q6_how_far_to_trust_7_5.md | 78, 164 | VT $33,515; VT on 1 Jan 2031 $41,561 | $29,829; $36,989 |
| Q6_how_far_to_trust_7_5.md | 79, 170, 182 | Bottom / floor $115,929 | $103,178 (stated $95,000) |
| Q6_how_far_to_trust_7_5.md | 169 | Top $111k to $171k | Stated top $95,000 to $140,000; funds pay $101,093 to $152,051 (section 4) |
| Q7_precommitment_and_rules.md | 116 | Floor $93k / $116k / $140k | $88,047 / $103,097 / $124,380 |
| Q10_inflation_inputs.md | 4, 34 | $110,000 to $135,000 = $95,410 to $117,094 | $95,000 to $115,000 = $82,399 to $99,747 (8d) |
| Q10_inflation_inputs.md | 42, 45 | Kept half $23,986 | $21,347; $29,823 with the excess (8d) |
| Q12b_lauras_working_life_gaps.md | 60-61, 171 | Floor $115,929, "about $81k"; deposits $24,500 / $56,900 / $92,000 | $103,178; $70,875 for a $112,500 deposit; $38,282 / $65,437 / $95,316 (section 5) |
| Q15_monitoring_and_triggers.md | 95 | Completion about $24,500 incl. $21,149 | $38,282 incl. the backstop ($34,369 in 2027 money) |
| Q15_monitoring_and_triggers.md | 96 | Overflow about $27,990 | $45,456 in 2033 money (8h) |
| Q15_monitoring_and_triggers.md | 97 | Floor "by up to 4.1%"; bottom "4.1% below" | The range rule on the holdings (section 3) |
| Q15_monitoring_and_triggers.md | 105 | Top $138,735; half kept $23,986, 1-in-20 $12,150 | Funds pay $123,476, stated top $115,000; half kept $21,347, 1-in-20 $9,881 |
| Q16_operating_reserve_mechanics.md | 142 | Margin $21,149 | Backstop $34,369 (section 2) |
| Q17_judging_the_implementation.md | 37 | Floor deduction 4.1% | The range rule on the holdings (section 3) |
| Q17_judging_the_implementation.md | 38 | Completion cost $21,149 | $34,369 backstop; $38,282 completion |
| Q17_judging_the_implementation.md | 55 | VT $33,515 | $29,829 |
| Q17_judging_the_implementation.md | 161 | "all ten paid in 94% of 16-year windows" | Paid if no coupon earns anything, after fees on waiting cash; all 585 follow (section 2) |
| Q18_pledges_and_stated_confidence.md | 173 | "4.1% off the floor, 2.5% off the moved half" | The range rule on the holdings (section 3) |
| Q19_range_rule_and_confidence.md | 15, 21, 28-29, 51-57, 84-87, 131, 146-147, 170, 201-221 | Central figures on Mon 9 Nov's design and this morning's (floor $115,929 and $104,031, moved half $22,806, $110,000 to $130,000, $93k-$140k, the 4.14% / 2.45% shift table) | Sections 3 and 4 and 8i ($95,000 to $115,000 on the holdings rule) |
| Q20_pooled_book_or_margin.md | 19, 107, 113-119, 131, 159-162, 187, 198, 206-208, 217, 241-243, 263 | H_plain at $335,771 and $33,484; house floor $81k / $104k / $128k; fixed per-end deductions; Keel's call's $93k / $116k / $140k and $12,150 | $336,656 and $34,369 (with the fee cushion); $88,047 / $103,097 / $124,380; the rule (section 3). Its comparisons at 0% stay valid as comparisons |
| Q21_team_reflection_events.md | 80 | VT $33,515 | $29,829 |
| Q21_team_reflection_events.md | 89, 91, 173 | Floor $115,929; bottom $110,000 "less 4.1%"; range $110,000 to $135,000; "a stated bottom of $110,000 central" | $103,178; $95,000 on the holdings rule; $95,000 to $115,000 |
| Q22_cosponsor_words_checklist.md | 220 | Reserve "about 107% funded" | 111.4% (8h) |
| Q23_exhibits_and_format.md | 60, 129 | $427,028 against $500,000 | $444,545 against $500,000 owed, worth $399,089 (8h) |
| Q23_exhibits_and_format.md | 95 | "$115,929" as an example of a wide figure | Any register figure; no change needed beyond the example |
| Q24_kept_half_and_joint_stress.md | 10-12, 35, 70, 80, 86, 94-95, 167, 216, 223-224, 244 | Every figure on Mon 9 Nov's design (overflow $27,939, range $110,000 to $130,000, $138,735, $23,986, $12,150 / $23,831 / $46,746, the 4.1% / 2.6% / 2.5% deductions, the matrix) | 8f and 8i |
| Q24_kept_half_and_joint_stress.md (evening) | 55-59, 155-157, 162-164, 205-207 | Taiwan dollar test on Mon 9 Nov's design, gift = what the funds pay: house 93.0% ("1 in 14", median gap $1,590), 9.4% covered 19 in 20, history 96.5%, joint 97.4%, real currency 97.1% (worst $10,048, Nov 1983), cap rule 99.97%, "about 93 to 97 of 100" | 8j, gift = the contribution after the cap: house 93.2% (about 1 in 15; median gap $1,407), 9.4% covered 19 in 20, history 96.9%, joint 99.3%; real currency 98.1% (worst $7,312, Nov 1983); with the excess 99.77% house, 100% history and joint, 99.8% real currency |
| Q24_kept_half_and_joint_stress.md (evening) | 91 (row 22) | Stricter reading 88.4% / 94.9% / 93.8%; 19 in 20: 9.4% (house), 11.0% (history) | 8j: 89.1% / 96.0% / 97.3%; 19 in 20: 9.4% (house), 11.8% (history), 11.6% (joint) |
| Q24_kept_half_and_joint_stress.md (evening) | 92 (row 23) | Real Taiwan dollar: kept half covered 97.1%; worst $10,048 | 8j: 98.1% (fails in 8 of 417 windows), worst $7,312 (Nov 1983); 99.8% with the excess (fails in 1, $1,755). The move's distribution (-12.7% / +0.1% / +13.7%), 11.0% of windows at 10% or more and the +0.09 correlation are unchanged |
| Q24_kept_half_and_joint_stress.md (evening) | 93 (row 24), 246-248 | Cap-rule pot $19,295 / $31,727 / $55,242; surplus median $7,860; 10% covered 99.97%; 13% in 99.2% (history 98.9%), 17% in 91.3% (95.1%); kept half alone 13% in 77.9% (86.0%), 17% in 51.4% (60.6%); "93-97 of 100", "78-86", "99.97 and 99 of 100" | 8j: half kept plus excess $16,193 / $28,541 / $49,924 (house); excess median $7,629 (section 4); 10% covered 99.77%; 13% in 98.7% (history 99.4%), 17% in 91.0% (95.8%); kept half alone 13% in 79.7% (90.1%), 17% in 54.9% (67.0%) |
| Q24_kept_half_and_joint_stress.md (evening) | 94 (row 25) | The gift in other money: $138,735 = NT$4.55m, NT$4.13m, NT$3.82m; $120,334 in 2027 dollars; stated $110,000-$130,000 = NT$3.60m-4.26m | 8j and 8d: the contribution $115,000 = NT$3.77m at 32.768, NT$3.43m 10% stronger, NT$3.16m at 27.52; $99,747 in 1 Jan 2027 dollars at 2.4%; NT$3.14m of today's building at 3%; the range $95,000-$115,000 as 8d |

False positives, not void: 25.94%, 36.55% and other S&P 500 years (Q1 l.17, 51, 67, 122, 191; Q1b l.23, 104, 121; Q1c l.23, 31, 59, 137; Q4b l.23, 136, 245, 268; Q12 l.20; Q12b l.23; Q21 l.85, 90, 200); a 4.1% grant cut (Q4b l.131); "107" inside URLs (Q5 l.105; Q9 l.83, 88); 1.94% inflation (Q10 l.32); 8.94% (Q6 l.76); $111k residency budgets and $171k bucket figures (H8 l.22, H9 l.130).

**Dated records** (left as they stand; any new entry uses this register):
- the panels in `research/panel/` (4 files, 37 lines), including the bond desk check itself, which quotes this morning's figures on purpose;
- the insight store `research/store/` (16 files, 266 lines): `insights.jsonl`, `VOID_CHECK_2026-11-09.md` and the tag pages CERTAINTY, CEILING, COMPLETE2028, COSPONSOR, FLOOR, HALFKEPT, INFLATION_TWD, LIQUIDITY, MOVE2031, OTHER, PROCESS, RESERVE2033 and RESIDENCY. Several carry this morning's 4.14% / 2.45% / $33,461 from the Q19 and Q20 rows, so a store refresh adds superseding entries rather than editing old ones. (Evening) HALFKEPT.md line 71 and INFLATION_TWD.md line 29 carry Q24-022's Taiwan dollar test (93.0%); its superseding entry uses 8j;
- `research/experience/` (BLIND_POOL.md, candidates_K.md, candidates_W.md, judge_3.md, blind_key.json; 13 lines): event fact sheets quoting the figures of their day.
  - One is wrong even for its day (card Q27, Tue 10 Nov evening): BLIND_POOL X053 says the ten cost "over $300,000" on 23 Oct; at that close they cost $297,636 (8b). The corrected sheets for the 16 Nov re-rank use 8b.

**Outside `keel/final_report/`:**
- `keel/pm/ASK_HUMANS.md` (Tue 10 Nov 07:04 entry, line 19) says the call costs $335,771, "$12,335 more", and "about $44,000 comes back to Laura in 2033 (2033 money; $33,461 in 1 Jan 2027 money)". Now: $336,656, $13,220 more, about $45,000 ($45,456 in 2033 money; $34,345 in 1 Jan 2027 money).
