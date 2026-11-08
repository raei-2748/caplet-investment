# The number register (Mon 9 Nov 2026)

Every figure the Final Report may use comes from this page. It uses one curve, one engine and Caplet's design as
submitted. These are research notes, not report text.

**Stamp.** Everything here is MODEL, meaning Keel's calculation and not a forecast or a promise.
- **Curve.** US Treasury daily par yield curve at the close on Fri 6 Nov 2026, the day trading froze. Source: treasury.gov CSV, copied to `competition/official_market_data/daily-treasury-rates_2026-11-06.csv`.
- **Valuation.** Values are forward to 1 Jan 2027 unless a line says otherwise.
- **Design.** Caplet's FINAL IPS as submitted (`FINAL_IPS_as_submitted.txt`), using the frozen WInS book's instruments.
- **Engine.** `numbers/engine.py` (curve, instruments, reinvestment), `numbers/plan.py` (2027 to 2033) and `numbers/run_numbers.py` (every figure below).
- **Results.** `numbers/results_2026-11-06.json`.
- **Rerun.** `python3 -I keel/final_report/numbers/run_numbers.py`, about 6 seconds, needs only numpy.

Rule for every later note and draft: a figure not on this page is not used. A figure here that changes is changed here first, with the date.

## 0. Inputs and where each comes from

| Input | Value | Source |
|---|---|---|
| Treasury curve | 1y 4.33, 2y 4.51, 3y 4.59, 5y 4.64, 7y 4.74, 10y 4.86, 20y 5.29, 30y 5.26 (%) | treasury.gov par yield curve, 6 Nov 2026 |
| Curve method | Par yields read as semiannual, bootstrapped on a half-year grid, log-linear discount factors | Same as `keel/scripts/ladder_pv.py` and `ladder_history.py`; reproduces their $301,544 exactly |
| The ten instruments | IBTM, IBTO, IBTP, IBTQ, IBTR for 2033-37; T-bonds 4.750% 15 Feb 2037, 4.500% 15 May 2038, 4.375% 15 Nov 2039, 4.250% 15 Nov 2040, 3.125% 15 Nov 2041 for 2038-42 | Frozen WInS book (`competition/wins/2026-10-23_snapshot.md`) |
| iBond funds | End "on or about" 15 Dec of their year; "do not seek to return any predetermined amount"; monthly distributions; 0.07% fee; IBTM average coupon 3.50%, average maturity 5.69 years, yield to maturity 4.86% (23 Oct) | ishares.com IBTM page, read Mon 9 Nov 2026 |
| Fund holdings' average maturity | IBTM 5.65, IBTO 6.62, IBTP 7.66, IBTQ 8.65, IBTR 9.53 years (4 Nov) | ishares.com, recorded in `keel/scripts/holdings_ladder.py` |
| Fund coupons in the model | The curve's par yield to each fund's average maturity. This is higher than IBTM's real 3.50% coupon, so the reinvestment test is conservative | Assumption |
| Floor and VT split of the 2028 money | 73.3% floor, 26.7% VT, of what is left after the ladder is complete | Frozen WInS book: 3,361 IBTM shares as floor stand-in ($72,766 at fill) against 167 VT ($26,525). FINAL says only "most" |
| Shares | VT median growth 7.5% a year; 16.78% yearly spread | J.P. Morgan 2027 LTCMA press release (19 Oct 2026), global equities 7.5%, the TNA's figure; J.P. Morgan 2026 matrix, AC World volatility |
| VT fee | 0.06% | TNA note 3 |
| Yield moves, 2026-2031 | Parallel, s.d. 0.9 points a year, independent of shares | MODEL assumption, as `keel/scripts/sail_mc.py` |
| Rate history | FRED DGS1 (1-year Treasury), daily from 1962, as monthly averages | `archive/rab/data/fred/DGS1.csv` |
| Stock history | Shiller monthly S&P Composite with dividends, 1871 to Jun 2023 | `keel/models/data/shiller_monthly.csv` (mirror; `keel/models/data/SOURCES.md`) |

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
ladder. At the 6 Nov close that is $2,287 in 1 Jan 2027 money, or about $2,400 by Jan 2028. **Build order (Keel's reading; the IPS is silent):** longest rungs first, because they move most with yields; so any part still unbought in January 2027 is the 2033 rung (IBTM), finished in January 2028.

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

## 2. Reinvestment (CASE_MAP C1): settled, with Keel's call

**What the risk is.** The ten pay interest long before the payments start. By 1 Jan 2033 that interest is worth
**$93,900**, nearly two of the ten payments. To turn today's $302,287 into ten payments of $50,000, every coupon must
be reinvested at today's forward rates. If rates later fall, the ladder pays less. The case's "high degree of
certainty" and the IPS's "pay what they say" both depend on this. TNA note 1 already names the risk for one bond's
10.5-month gap.

**How it was tested.**
- *Falls for good:* every rate after purchase is lower by 1, 2 or 3 points, floored at zero.
- *Interest earns nothing:* every coupon and every fund payout is held as cash.
- *History replay:* 585 windows of 16 years, one starting each month from Jan 1962 to Sep 2010. Each window's path of the 1-year Treasury yield is applied in proportion to today's forward rates, the method of `keel/models/ASSUMPTIONS.md` A35.
- *Policy:* in all three tests, each coupon is reinvested on the day it arrives into a Treasury maturing before its payment, and any surplus carries to the next payment.

| Design | Cost (1 Jan 2027) | Bought in Jan 2027 | Short in total if rates fall 1 / 2 / 3 points for good | Short if interest earns nothing | History: windows with any shortfall | History: median / 1-in-20 / worst shortfall |
|---|---|---|---|---|---|---|
| **A. The ten as written, sized at today's forward rates** | $302,287 | 10 | $12,172 / $23,509 / $34,083 | $54,595 | 55.6% | $1,592 / $34,555 / $45,266 (start Jul 2007) |
| A, sized for rates 1 point lower | $309,456 | 10 | $0 / $11,650 / $22,516 | $43,599 | 39.1% | $0 / $22,991 / $34,016 |
| A, sized for rates 2 points lower | $316,508 | 10 | $0 / $0 / $11,151 | $32,794 | 14.0% | $0 / $11,630 / $22,963 |
| **A, sized for rates 3 points lower (Keel's call)** | **$323,436** | 10 | **$0 / $0 / $0** | $22,192 | **6.0%** | **$0 / $1,225 / $12,117** (start Jul 2007) |
| A, sized so interest is never needed | $337,836 | 10 | $0 | $0 | 0% | $0 |
| B. Cash-flow matched (each coupon pays the next payment due), at forward rates | $302,029 | 8 | $5,500 / $10,725 / $15,690 | $25,007 | 58.3% | $2,913 / $15,925 / $19,584 |
| B, sized so interest is never needed | $319,687 | 8 | $0 | $0 | 0% | $0 |

Findings:
1. **The ladder as written needs a margin.** Sized at today's forward rates, it falls short somewhere in more than
   half of the historical windows. The shortfall is usually small (median $1,592), but 1 time in 20 it is $34,555,
   about 7% of the $500,000, and its worst is $45,266.
2. **The bond desk's answer (B) halves the risk at the same cost, but contradicts the IPS.** In B, the long bonds'
   coupons pay 2033 and 2034, so the 2033 and 2034 funds are never bought in January. That breaks "In January 2027
   we'll use your first deposit to buy 10 Treasuries" and TNA note 2's IBTM for "her first $50,000 payment". It stays
   in the store as the alternative a bond reader would expect, not as the plan.
3. **Keel's call (logged in `../pm/ASK_HUMANS.md`, Mon 9 Nov).** Keep design A exactly as the IPS says: ten bought in
   January 2027, each Treasury's interest buying more of the same Treasury. In January 2028, the 2028 deposit's first
   dollars "complete" the ladder to a stated standard: it pays all ten even if, from 2027, every coupon is reinvested
   3 points below today's forward rates (about 1.3% to 2%).
   - **What it costs:** a margin of **$21,149** (1 Jan 2027 money). The whole completion is about $24,500 in January 2028, the margin plus the $2,287 still to buy.
   - **What it buys:** all ten paid in full in 94% of every 16-year stretch of US rates since 1962. In the rest, the worst is $12,117 short of $500,000 (2.4%).
   - **What it costs the gift:** about $20,000 off the bottom of the 2033 range (section 4).
   - **When rates don't fall,** the margin is not lost. The payments overflow, and the surplus is Laura's.
   - **Why this keeps to the IPS:** "Even if yields fall and the total cost of the ladder ends up being above $300,000, we'll simply complete it with the 2028 deposit." Falling yields are exactly what raises the true cost of a coupon ladder.
   - Revisit only if Caplet disagrees, or if the FR instructions (Tue 10) change what the report may recommend.

## 3. An iBond fund pays its net asset value, not par (CASE_MAP C2): settled

| Fund (pays) | Fund fee over its life, on a $50,000 rung | Months its holdings' money waits in cash before the end | Lost if that cash earns nothing |
|---|---|---|---|
| IBTM (2033) | $170 | 5.4 | $869 (1.7%) |
| IBTO (2034) | $196 | 6.4 | $1,000 (2.0%) |
| IBTP (2035) | $221 | 5.4 | $807 (1.6%) |
| IBTQ (2036) | $245 | 5.4 | $781 (1.6%) |
| IBTR (2037) | $266 | 7.4 | $1,043 (2.1%) |

- The fee is already in the engine's $302,287, at $1,098 across the five funds.
- What is left is the cash wait. In its final months a fund holds cash, and that cash earns whatever short rates are then. This is why the payout "is not fixed" (TNA note 2): it moves by up to about 2%.
- The floor fund has the same feature. Measured on its own from the day it is bought, its payout falls by:
  - 2.6% if rates fall 3 points for good right after Jan 2028;
  - 4.1% if every distribution and its final cash earn nothing;
  - 1.5% and 2.5% respectively for money moved into it in 2031.
- **So the bottom Laura states is the floor's modelled payout less 4.1%, rounded down to the nearest $5,000.** That keeps "the bare minimum ... without doubt" true in every rate world short of a default. For the moved half in 2031, the deduction is 2.5%.

## 4. The plan from 2028, with Keel's call (CASE_MAP C5, C8)

Central case: today's forward rates, VT at its median 7.5%. Move date modelled as 1 Jan 2031.

| Item | Central | House model 1-in-20 low / median / 1-in-20 high | History (US stocks, every 3-year window since 1871; rates at today's forwards) |
|---|---|---|---|
| Completing the ladder (Jan 2028) | $24,475 | | |
| Left for floor and VT | $125,525 | | |
| Floor money (Jan 2028) / share of the $150,000 | $92,010 / 61% | | |
| VT bought (Jan 2028) | $33,515 | | |
| **Floor payout, late 2032 (bottom)** | **$115,929** | $93k / $116k / $140k | (fixed once bought in Jan 2028) |
| **Bottom Laura states** (less 4.1%, down to $5k) | **$110,000** | | |
| VT on 1 Jan 2031 | $41,561 | | |
| The moved half, paid late 2032 | $22,806 | $14k / $23k / $38k | |
| **Top of the range** (floor + moved half) | **$138,735** | $111k / $139k / $170k | $131k / $140k / $154k; lowest $119.9k (start Jul 1929) |
| Half kept, promised to no one, on 1 Jan 2033 | $23,986 | $13k / $24k / $45k | |
| Floor + moved half + kept half | $162,721 | $128k / $164k / $209k | $148k / $166k / $195k |

**Without the margin**, for comparison:
- Floor payout $136,328, stated bottom $130,000.
- Top $163,147 (house $135k / $164k / $196k).
- Kept half $28,248.

The margin moves about $20,000 from the bottom, and about $24,000 from the top, to the ten payments' safety.

More from the same runs:
- **The return assumption barely moves the gift.** With VT growing 4%, 6%, 7.5%, 9% or 10% a year (central path), the top is $136,580, $137,794, $138,735, $139,703 or $140,364. The kept half is $20,327 to $26,907. So the 7.5% is not doing the work; the Treasuries are (EXPECTATIONS T12 asked for 4% to 10%).
- **Deletion test.** If VT went to zero, the ten payments would be unchanged, and the gift would be the floor alone, $115,929.
- **Not capital-protected.** The 2028 money is not a protected note: VT ($33,515) is more than the floor's expected interest ($23,919). Shares at zero would return $115,929 on the $125,525 left after completing the ladder.
- **The margin comes back if rates hold.** At today's forward rates the payments overflow by about $27,990 in Jan 2033 money, which is Laura's from 2033.

### The 2031 move and the range (C5)
- **Today the range is not known.** Its bottom is fixed in January 2028, when the floor is bought (yields and the completion set it). Its top is fixed on the day half of VT moves into Treasuries, before the 2031 meetings.
- **Once the move is made, both ends are money Laura owns in Treasuries maturing late 2032.** What can still move them is only interest on their final months in cash and on their last distributions. That is at most 4.1% for the floor and 2.5% for the moved half, and both are already deducted from the figures she states.
- **So the confidence she can state in 2031 is "certain unless the US Treasury defaults".** That is the IPS's own standard ("barring a US default"). In the house model the 2033 gift falls inside the stated range in every path.
- **The uncertainty a judge should see is earlier: which range she will be able to announce.** From today, the top she announces in 2031 is between about $111,000 and $170,000 (1-in-20 each side, house model). It is $131,000 to $154,000 on US stock history.
- **Central, the 2031 announcement is about $110,000 to $135,000.** That is the top less 2.5%, rounded down to $5k.
- Good and bad markets before the move change only the top. After the move nothing changes either end (case A6).
- **One definition, used everywhere:** the 2033 facility contribution is the floor plus the moved half, and the range above is for that. Money Laura later spends on the building from the half kept is her separate choice, outside the announced range (`CANON.md` D12). Without this, the kept half could push the money reaching the facility above the range and make the stated confidence look wrong.

### The all-Treasury benchmark (C8)
- **The comparison.** If everything left in January 2028 bought the floor fund instead of 73% floor and 27% VT, Laura would have a certain **$158,157** in late 2032 with Keel's margin (house $127k / $158k / $190k, depending on yields to 2028). Without the margin it would be **$185,987**.
- **The FINAL's gift top is below that benchmark in 98% of house paths.** Half of VT is held back from the gift on purpose, as flexibility.
- **Counting the half kept,** the FINAL leaves Laura more in total than the benchmark in 63% of house paths: median $164k against $158k with the margin, and $193k against $186k without it. In its 1-in-20 low it has about the same ($128k against $127k).
- **What VT adds is a share of world growth for the top and for the kept half, at the cost of a lower certain bottom.** An all-Treasury plan with the same flexibility (holding back the FINAL's median kept half) would promise about $134k with certainty. The FINAL's range is $110k to $135k central, with $139k as the median top. Keel's reading: VT costs the gift little at the median, and it is what lets half the growth stay unpromised. The report should say so plainly, not claim that VT makes the gift bigger.

## 5. A smaller or missed 2028 deposit (CASE_MAP C6)

Smallest 2028 deposit that still completes the ladder, by how far yields fall before 1 Jan 2027:

| Yields fall before Jan 2027 | Ladder only (payments full at forward rates) | Ladder plus Keel's margin |
|---|---|---|
| None (6 Nov close) | $2,400 | $24,500 |
| 0.5 points | $18,400 | $40,400 |
| 1 point | $35,000 | $56,900 |
| 2 points | $70,400 | $92,000 |

- **The payments are safe unless the deposit falls by more than about 98% at today's yields.** That threshold is 77% if yields fall 1 point first, and 53% if they fall 2 points (Q1's "about four-fifths" is the 1-point case).
- **The floor shrinks almost dollar for dollar.** At today's yields and with Keel's margin, the floor payout is about $81k for a $112,500 deposit, $47k for $75,000 and $12k for $37,500.
- **A missed deposit** (one of the IPS's two reasons to change) leaves:
  - $2,287 of the ladder unbought; with the longest rungs bought first, the 2033 payment is about $3,000 short at forward rates;
  - no margin;
  - no floor and no VT, so nothing for the building. Laura would know before 2031, because the deposit is due Jan 2028 and the meetings are in 2031.
- **A smaller deposit is not one of the two reasons.** The plan as written absorbs it: ladder first, then floor and VT smaller.
- The Q1 card shows a recession could shrink the deposit while yields fall. The report states this as a risk, not a change.

## 6. Figures now void (do not use)

| Old figure | Where it came from | Now |
|---|---|---|
| Range $145k-$168k, $145k-$170k, top reached "about three times in four" | October numbers on older designs | Section 4: stated range about $110k-$135k central with Keel's margin ($130k-$155k without). After the 2031 move the stated range holds in every house path; what is uncertain is which top she can announce |
| About $21,000 short if yields fall 2 points for good | Old design, 23 Oct curve | $23,509 for the ladder as written; $0 with Keel's margin |
| "All ten paid in full in about 75-76% of base futures" | Old runs, H8 (model futures) | 44% of historical windows as written; 94% with Keel's margin (a different measure: history replay, not model futures) |
| All-Treasury plan about $191,000 | 4 Nov curve, `ips_rewrite/final_night/IDEA_LIST_MATHS.md` | $185,987 without margin; $158,157 with it (6 Nov) |
| A 1-point fall adds about $30,600 | 25 Sep curve | $31,805 before 1 Jan 2027 (6 Nov) |
| "Headroom" under $300,000 | Every curve before 5 Nov | Gone: the ten cost more than $300,000 |
| Fixed $150,000 floor | Old option 4b | No fixed floor: the FINAL's floor is "most" of what is left, and the payout "is not fixed" |
| $302,137 (curve) and $303,269 (instruments) | 5 Nov, `keel/scripts/holdings_ladder.py` | 6 Nov: $301,544 curve; $302,287 instruments on the curve. Market quotes for 6 Nov were not taken, and the 5 Nov gap was +$1,132 |

## 7. Limits of these numbers
- **The reinvestment history** uses 1-year yields in proportion. That is harsh on windows starting at high rates, and it is only 585 overlapping windows, roughly four independent rate eras.
- **The house model does not test reinvestment.** It moves yields only up to 2031, for the purchases. Payment safety against reinvestment comes from section 2's history replay and fixed falls. House model: 200,000 paths, seed 2033.
- **The house model** draws stocks and yields independently. In a real recession shares and yields often fall together, which would hurt the top and the margin at the same time (Q1).
- **The fund coupons** are modelled at par yields, above IBTM's real 3.50%. The reinvestment risk is therefore a little overstated, which is the safe direction.
- **Fund holdings data** comes from one day's iShares figures. Holdings and cash-wait months will drift.
- **The 73/27 split** is read from the frozen WInS book. The IPS says only "most".
- **No market quotes on 6 Nov.** Everything is priced on the curve.

## 8. Still to add (later days)
- Inflation (US and Taiwan) and real values of the payments, the floor and the range.
- The strongest rival priced on the FINAL's own design (shares held until 2031, the floor bought only then).
- A dated ladder-cost history from this one engine (for the Articulation story).
- Per-rung reinvestment figures and the flat break-even yield.
