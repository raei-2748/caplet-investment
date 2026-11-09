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
| Shares | VT median growth 7.5% a year; 17.88% yearly spread | J.P. Morgan 2027 LTCMA, USD matrix (estimates as of 30 Sep 2026; row "AC World Equity 7.50 8.94 17.88", read 9 Nov 2026), the TNA's 7.5%; until 9 Nov the spread was the 2026 edition's 16.78% (house figures moved by at most $2,100) |
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
| The moved half, paid late 2032 | $22,806 | $13k / $23k / $39k | $15k / $24k / $38k |
| **Top of the range** (floor + moved half) | **$138,735** | $111k / $139k / $171k | $131k / $140k / $154k; lowest $119.9k (start Jul 1929) |
| Half kept, promised to no one, on 1 Jan 2033 | $23,986 | $12k / $24k / $47k | $15k / $26k / $46k |
| Floor + moved half + kept half | $162,721 | $128k / $164k / $211k | $148k / $166k / $195k |

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
- **The uncertainty a judge should see is earlier: which range she will be able to announce.** From today, the top she announces in 2031 is between about $111,000 and $171,000 (1-in-20 each side, house model). It is $131,000 to $154,000 on US stock history.
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
| $13k / $24k / $45k (kept half) and $14k / $23k / $38k (moved half), house model | Section 4 before the 9 Nov move to J.P. Morgan's 2027 volatility (17.88%) | $12k / $24k / $47k and $13k / $23k / $39k (section 4; history columns added) |
| $302,137 (curve) and $303,269 (instruments) | 5 Nov, `keel/scripts/holdings_ladder.py` | 6 Nov: $301,544 curve; $302,287 instruments on the curve. Market quotes for 6 Nov were not taken, and the 5 Nov gap was +$1,132 |

## 7. Limits of these numbers
- **The reinvestment history** uses 1-year yields in proportion. That is harsh on windows starting at high rates, and it is only 585 overlapping windows, roughly four independent rate eras.
- **The house model does not test reinvestment.** It moves yields only up to 2031, for the purchases. Payment safety against reinvestment comes from section 2's history replay and fixed falls. House model: 200,000 paths, seed 2033.
- **The house model** draws stocks and yields independently. In a real recession shares and yields often fall together, which would hurt the top and the margin at the same time (Q1).
- **The fund coupons** are modelled at par yields, above IBTM's real 3.50%. The reinvestment risk is therefore a little overstated, which is the safe direction.
- **Fund holdings data** comes from one day's iShares figures. Holdings and cash-wait months will drift.
- **The 73/27 split** is read from the frozen WInS book. The IPS says only "most".
- **No market quotes on 6 Nov.** Everything is priced on the curve.

## 8. Added Mon 9 Nov, later (`numbers/extras.py`, `numbers/results_extras_2026-11-06.json`)

### 8a. Where each rung's $50,000 comes from (design A, sized at today's forward rates)
| Payment | Instrument | Cost (1 Jan 2027) | Coupons received | Interest on those coupons | Share of the $50,000 that is interest on interest | Delivered if reinvested 3 pt below forwards | Delivered if money earns nothing |
|---|---|---|---|---|---|---|---|
| 2033 | IBTM | $37,908 | $8,848 | $1,719 | 3.4% | $48,880 | $48,281 |
| 2034 | IBTO | $36,065 | $10,079 | $2,180 | 4.4% | $48,595 | $47,820 |
| 2035 | IBTP | $34,300 | $11,368 | $2,949 | 5.9% | $48,098 | $47,051 |
| 2036 | IBTQ | $32,588 | $12,426 | $3,670 | 7.3% | $47,643 | $46,330 |
| 2037 | IBTR | $30,922 | $13,178 | $4,328 | 8.7% | $47,242 | $45,672 |
| 2038 | 4.750% Feb 2037 | $29,136 | $13,742 | $6,640 | 13.3% | $45,883 | $43,360 |
| 2039 | 4.500% May 2038 | $27,567 | $14,099 | $6,777 | 13.6% | $45,811 | $43,223 |
| 2040 | 4.375% Nov 2039 | $26,051 | $15,059 | $6,803 | 13.6% | $45,747 | $43,197 |
| 2041 | 4.250% Nov 2040 | $24,582 | $15,233 | $7,653 | 15.3% | $45,236 | $42,347 |
| 2042 | 3.125% Nov 2041 | $23,168 | $13,150 | $7,376 | 14.8% | $45,434 | $42,624 |

What it shows: the later the payment, the more of it is interest earned on interest (3% of the 2033 payment, about
15% of the 2041 and 2042 payments). The risk sits in the last five, the T-bonds, which is why a margin sized for
them protects the whole ladder.

**Flat break-even.** Bought at today's prices with no margin, the ladder pays all ten only if every coupon earns at least
**5.12% a year** from the day it arrives until it is needed (bisection on one flat rate for every reinvestment). Today's
forward rates are 4.67% for 2027-2033 and 5.43% for 2033-2042, so the break-even is simply the average of the forwards:
the ladder as written assumes today's forward rates come true. At a flat 4.0% the worst payment is $47,721 and the ten
fall $13,906 short in all; at 3.0%, $46,215 and $25,144; at zero, $42,347 and $54,595 (matches section 2).

### 8b. The cost of the ten payments through 2026, from this one engine (every Treasury close, 2 Jan to 6 Nov)
214 closes. Value on 1 Jan 2027 of the ten payments (payment-date basis) and of the ten instruments held (design A):

| Date | Ten payments | Ten held | Ten held with Keel's margin (-3 pt) | 10-year yield |
|---|---|---|---|---|
| Fri 2 Jan | $316,546 | $317,338 | $338,677 | 4.19% |
| Fri 27 Feb (the year's dearest) | $325,563 | $326,382 | $347,837 | 3.97% |
| Tue 30 Jun | $312,974 | $313,752 | $335,061 | 4.44% |
| Thu 10 Sep (first close under $300,000) | $297,879 | $298,612 | $319,704 | 4.95% |
| Fri 25 Sep | $292,264 | $292,979 | $313,976 | 5.17% |
| Mon 28 Sep (trading opens) | $290,291 | $291,000 | $311,968 | 5.24% |
| Mon 5 Oct (the year's cheapest) | $287,938 | $288,642 | $309,559 | 5.31% |
| Wed 7 Oct (orders filled 7-8 Oct) | $288,510 | $289,216 | | |
| Thu 8 Oct | $290,349 | $291,060 | | |
| Fri 16 Oct | $294,770 | $295,493 | $316,537 | 5.09% |
| Fri 23 Oct (Trading Notes due) | $297,636 | $298,367 | $319,462 | 5.00% |
| Fri 6 Nov (IPS in, trading froze) | $301,544 | $302,287 | $323,436 | 4.86% |

The ten payments cost less than $300,000 on only 37 of the 214 closes (the ten held, on 36), every one of them between
10 Sep and 3 Nov. The team's orders filled on 7-8 Oct, within two trading days of the year's cheapest close (5 Oct).
That is luck of timing, not skill, and should be told that way if it is told at all. By the IPS deadline the cost was
back over $300,000, which is the situation the IPS's completion rule was written for. Dates are US closes.

### 8c. The strongest rival on Caplet's own design: buy the floor in 2031, not 2028
Rival: everything left in Jan 2028 after completing the ladder goes into VT; in Jan 2031 the same final mix as FINAL
after its move (86.65% into Treasuries maturing late 2032, 13.35% of VT kept to 2033). Same margin, same house paths
(200,000, seed 2033) and the same 1,770 history windows (US stocks with dividends, every 3-year start since 1871).

| | FINAL (floor bought Jan 2028) | Rival (floor bought Jan 2031) |
|---|---|---|
| Money owned in Jan 2031, house p5 / p50 / p95 | $111,183 / $139,392 / $170,770 | $85,802 / $147,146 / $251,436 |
| Worst 1 in 100 (house) | $99,941 | $68,097 |
| Chance it is under $110,000 (the stated bottom), house | 4.3% | 18.7% |
| Total by 2033, house p5 / p50 / p95 | $127,849 / $163,894 / $210,690 | $99,951 / $171,621 / $293,739 |
| Money owned in 2031, history p5 / p50 / p95 | $131,215 / $140,235 / $153,646 | $99,214 / $157,757 / $244,802 |
| Lowest in history | $119,868 (start Jul 1929) | $25,564 (start Jul 1929) |
| Under $110,000 in history | 0% | 10.7% |

What it shows: waiting to buy the floor raises the middle by about $8,000 and the lucky end a great deal, but in almost
one path in five (house) or one window in nine (history) Laura would walk into the 2031 co-sponsor meetings with less
than the bottom she could have promised in 2028; from a July 1929 start she would have about $26,000. FINAL ends up
behind the rival in about 60% of house paths and 68% of history windows, and that is its price: it can name a bottom in January 2028, three years
before the meetings, and it cannot fall below it.

### 8d. What the dollars buy: inflation and the Taiwan dollar (`numbers/real_values.py`, inputs `numbers/inflation_inputs.json`)
Sources and bands in `research/cards/Q10_inflation_inputs.md` (all read 9 Nov 2026). US central 2.4% a year (J.P. Morgan
2027 matrix, the same edition as the 7.5%); band 1.9%-3.5%. Taiwan construction costs central 3.0%, band 1.5%-5.0%
(DGBAS construction cost index: September 2026 +7.29% on a year, about 3% a year since 2000). USD/TWD 32.768 on 6 Nov
(central bank of Taiwan); strongest Taiwan dollar of the last ten years 27.52.

| | US inflation 1.9% | 2.4% (central) | 3.5% |
|---|---|---|---|
| The 2033 payment in 1 Jan 2027 dollars | $44,661 | $43,368 | $40,675 |
| The 2042 payment in 1 Jan 2027 dollars | $37,701 | $35,032 | $29,845 |
| All ten in 1 Jan 2027 dollars | $410,937 | $390,686 | $350,118 |
| The $110,000-$135,000 range (paid 2033) in 1 Jan 2027 dollars | $98,253-$120,584 | $95,410-$117,094 | $89,485-$109,823 |

In Taiwan building terms, the range buys NT$3.00m-NT$3.69m of today's construction at 3% cost growth (NT$3.29m-4.04m
at 1.5%, NT$2.67m-3.27m at 5%). If the Taiwan dollar went back to its ten-year strongest (27.52), Laura would need about
$21,000-$26,000 more to buy the same NT$ budget, roughly the whole kept half of VT in the middle case ($23,986, section 4).

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

### 8f. How small the half kept gets in the years shares fall (`numbers/kept_half.py`, `numbers/results_kept_half.json`)
Same engine, Keel's margin, house paths and history windows as section 4. The kept half is half of the VT bought in
January 2028 (about $16,757 at cost) grown to 1 Jan 2033. "Shares fell" means VT ended 2031-2033 lower than it began,
the two years from the co-sponsor meetings to the gift.

| | House model (200,000 paths) | History (US stocks, every window since 1871) |
|---|---|---|
| Kept half, 1 Jan 2033: 1-in-100 / 1-in-20 / median / 1-in-20 high | $9,168 / $12,150 / $23,831 / $46,746 | $9,324 / $14,874 / $26,383 / $45,626 |
| As a share of the top of the range (1-in-20 / median / 1-in-20 high) | 9% / 17% / 31% | 11% / 19% / 31% |
| Paths in which shares fell over 2031-2033 | 28.4% | 20.7% |
| Kept half, median, if shares fell over 2031-2033 | $17,663 | $18,162 |
| Kept half, median, if shares rose over 2031-2033 | $26,756 | $28,303 |
| Kept half, median, if shares fell more than 20% over 2031-2033 (7.3% / 5.2% of paths) | $14,839 | $16,271 |
| Kept half, median, if VT ends below its 2028 cost (18.3% / 10.5% of paths) | $13,859 | $14,956 |
| Kept half under $15,000 / under $10,000 | 12.9% / 1.7% of paths | 5.4% / 1.6% of windows |
| Lowest window | | $6,494 (start September 1929) |
| Named starts | | 1973: $15,542; March 2000: $14,931; October 2007: $17,424 |

What it shows: the risk the morning research flagged is real and has a size. In the years shares fall, when the IPS
expects co-sponsors to cut, the kept half is about a third smaller than when they rise (median about $18,000 against
$27,000), and in a fall of more than a fifth it is about $15,000. It does not vanish: even from September 1929 it is
about $6,500, and from every other bad start named above it is close to what was put in. The 2031 range itself does not
move, because the floor and the moved half are Treasuries by then. The honest line is that the kept half is a cushion
whose size moves with the markets, smallest in the years it is most likely to be needed; that is a cost of keeping
flexibility in shares rather than in Treasuries (section 4, the all-Treasury benchmark).

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
| N/A | Cash | Cash | $4,823.21 | 1.61% |
| **Total** | | | **$300,000.00** | **100.00%** |

- **Keel's call (logged in `../pm/ASK_HUMANS.md`, Mon 9 Nov):** amounts at cost, because Wharton asks for the "amount
  allocated" out of the original $300,000 and bars the ending value. Cash is $300,000 less the cost of the eleven
  holdings: WInS showed $3,513.79 in cash; the other $1,309.42 went on commissions and the interest accrued on the five
  bonds when they were bought. A table note says so in one line. Percentages are rounded so that they add to exactly
  100.00% (largest remainder: the May-2038 bond shows 6.20% rather than 6.21%).
- **In groups:** Treasuries 89.55% ($268,652.18: iBond ETFs 61.28%, bonds 28.27%), VT 8.84%, cash 1.61%.
- **Identifiers.** The ETFs use their tickers. Wharton's own example row ("532281 T-Bond 4.500% 15-May-2038") is one of
  Caplet's bonds, so 532281 is probably its WInS identifier; the other four come from Caplet's final WInS export (asked
  of Ray, Mon 9 Nov). Until then the table names the bonds by coupon and date, which identifies them uniquely.
- **The rival reading,** each holding's weight at the final market value times $300,000 (accrued interest left out),
  moves no security by more than 0.25 points at 23 Oct prices (VT 8.59% instead of 8.84%) and cash by 0.46 (1.15% instead of 1.61%),
  and would need the final export; Caplet may switch to it.
- **What the table must not be read as:** the WInS book is Laura's whole plan in miniature (the ladder rungs, the
  late-2032 floor stand-in inside IBTM, and VT), not her January 2027 purchase alone. Section 2's text explains this
  once; the evidence is in `CANON.md` and the 23 Oct snapshot's "Pays for" column.

## 9. Still to add (later days)
- **The operating reserve (case A1, Wharton's Section 3):** its size on 1 Jan 2033 on the 6 Nov curve's forwards, what
  it holds rung by rung, and how it runs down 2033-2042 with no rebalancing (Day 3, Tue 10 Nov).
- Later days add what the research rounds and the skeleton ask for.
