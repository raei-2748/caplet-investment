AI-generated (Claude Code), Genius Lab WO-R8, 27 Oct 2026

# The Genius Lab -> the rewrite: five strategy ideas, each run through the model

(Keel is a simulated team, AI-written. Research, not submission text. Every number is MODEL unless it says history.)
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA global equities 7.5% (sceptic run 6.5%) |
200,000 paths, seed 20261016 | rates 1pp/yr parallel walk; rho = how far stocks and yields fall together, 0 or 0.5 |
MODEL = `../../library/ips_numbers_2026-10/ips_numbers.py`, unchanged except the patches in `../lab/R08_core.py`.**
Scripts: `../lab/R08_core.py` (shared engine; reproduces R05: top p50 $166,292), `R08_1_haircut.py`, `R08_2_lock.py`,
`R08_3_corner.py`, `R08_4_coupons.py`, `R08_5_rematch.py`, each with a `_results.json`. No WInS trades in any of them.

**For a judge, in plain words.** We tried to break our own plan five ways and found three things worth knowing. One:
the gift's cap quietly hands Laura every stock-market gain between 2031 and 2033 and leaves the facility every loss,
so the day she announces her range we should sell the promised stocks into the Treasury fund that already holds her
floor. The top of the range then stops being a bet: it is reached about nine times in ten instead of three in four,
for an expected cost of about $1,600 out of roughly $195,000 she will hold in 2033. Two: the ten payments depend far
less on luck than on a house rule nobody had written down. If coupons sit in a cash-like fund instead of buying more
of the bond that paid them, the ladder comes up about $7,600 short on day one with no market move at all. Three: the
danger we planned to name, yields crashing before the January 2027 purchase, is a ten-week window that history has
crossed only during the Volcker years. The real soft spot is coupon reinvestment after 2033, and it closes with a
fixed $7,500 cushion set aside in January 2033 next to the ladder. That cushion is sized by how wrong a 2033
forecast of the gap can be, not by a guessed stress.

---

## Idea 1. Two dials, not one: the share of stocks pledged sets generosity, a haircut sets confidence

**One sentence.** How often the top is reached doesn't depend on how much of the stock fund Laura pledges. It depends
only on whether she quotes the stocks at full 2031 value or at a haircut, the way a lender values collateral.

**Why a judge cares.** Investment Strategy and Portfolio Analysis. It turns the 2031 top from one tuned number into a
decision framework with two independent levers. Each lever has a price, and the second one costs Laura nothing in
total wealth: it only moves money between the gift and the half she keeps.

**Test (`R08_1_haircut.py`).** Gift = floor + share s of the stocks in 2033, capped at top = floor + s x (1 - h) x
stocks in 2031. Shares 1/3, 1/2 and 2/3; haircuts 0-30%; three scenarios.

| rho 0, 7.5% | top reached (within $1k) | exact | over/under-promise ratio | median gift | mean gift | Laura keeps (median) |
|---|---|---|---|---|---|---|
| share 1/3, no haircut | 80.6% | 70.9% | 4.2 | $159,930 | $157,025 | $34,074 |
| **share 1/2, no haircut (today)** | **76.7%** | **69.9%** | **3.3** | **$165,528** | **$163,286** | **$27,745** |
| share 2/3, no haircut | 73.2% | 68.1% | 2.7 | $171,189 | $169,421 | $21,374 |
| share 1/2, 10% haircut | 86.5% | 81.6% | 6.4 | $164,186 | $161,739 | $29,304 |
| share 1/2, 20% haircut | 92.4% | 89.6% | 12.2 | $162,638 | $159,989 | $31,087 |
| share 1/2, 30% haircut | 95.2% | 93.9% | 20.0 | $160,987 | $158,113 | $32,983 |

Stocks no lower in 2033 than in 2031: 72.8% for every share (closed form 72.7%). With rho 0.5 and 6.5%, share 1/2:
72.9% with no haircut (ratio 2.7), 83.3% with 10% (ratio 5.0).

**What it shows.**
1. Hypothesis confirmed. On the exact test the share moves the fractile by under 3 points (70.9 / 69.9 / 68.1%). The
   wider spread on the "within $1k" test is the $1,000 tolerance, which is a bigger allowance on a smaller pledge.
2. **The number that changes a decision:** a 10% haircut doubles the implied ratio (3.3 -> 6.4) for $1,342 off the
   median gift, and that money isn't lost: it stays with Laura. So if Thursday prefers "over-promising is six times
   worse" to "three times worse", it's a cheap switch.
3. **A definition to settle before any text:** "three in four" is true only with the $1k tolerance. The exact event,
   "stocks no lower in 2033 than in 2031", is 72.8%, and the top reached to the dollar is 69.9%. Say "about three
   times in four, whenever world stocks are no lower in 2033 than in 2031" (the event, which is 72.8%), never
   "three in four to the dollar". This settles the open "seven in ten vs three in four" item from Trial 3.

**Fits the locked lines?** Yes. TNA Note 3 ("a rise before 2031 lifts the top") holds under any haircut. No trades.
**Verdict: IPS, one clause** (the two levers, with "no haircut, because we judge over-promising about three times
worse" as the stated choice); the table goes to the Final Report.

---

## Idea 2. Lock what you announce: the day Laura names the range, the promised stocks move into the floor fund

**One sentence.** Under today's cap, the gift's half of the stocks keeps every fall between 2031 and 2033 and hands
every rise back to Laura, so once the top is public, selling that half into IBTM (which matures Dec 2032) makes the
top owned rather than hoped for.

**Why a judge cares.** This is the most "investing" idea here, because it finds an option nobody priced. The cap means
the facility has written Laura a free call: in the model she collects **$4,406** a path on average above the cap,
while the facility's expected miss below the top is **$1,144**. Locking extends the plan's one principle to its last
promise: every dollar Laura promises is matched with Treasuries on the day she promises it (the payments in 2027, the
floor in 2028, the top in 2031). That is liability-driven investing applied to a pledge, and it answers the case's
"how favourable and unfavourable market outcomes could affect the amount" with "before 2031 they move the range;
after she speaks, nothing does."

**Test (`R08_2_lock.py`).** On 1 Jan 2031, sell half of the stock fund's value into IBTM at that day's ~2-year
forward yield plus the path's rate shift (median growth to Dec 2032: 1.1007). Laura's own half stays in stocks. The
coupon gap is handled as today.

| | top reached (within $1k) | gift below quoted bottom | quoted bottom (median) | mean gift | Laura keeps (mean) | expected cost to Laura's total (median) |
|---|---|---|---|---|---|---|
| A today | 76.7% | 0.75% | $145,000 | $163,286 | $31,718 | - |
| **B lock the promised half** | **92.9%** | 0.75% | $145,000 | $163,901 | $29,490 | **$1,613 ($917)** |
| C = B, bottom raised to floor + locked half | 92.9% | 3.38% | $160,000 | $163,901 | $29,490 | $1,613 |
| D lock a quarter, bottom + that quarter | 87.9% | 1.53% | $150,000 | $163,781 | $30,417 | $807 |
| E = B + Idea 5's 2033 cushion | 86.7% | 2.21% | $145,000 | $163,156 | (n/a) | (n/a) |

Robust: B reaches the top 91.2% (rho 0.5) and 90.7% (rho 0.5, 6.5%), with expected costs of $1,504 and $1,036.
Median total in 2033 (gift + kept) is about $192,800 today, so the cost is under 1%. The residual 7% of misses
come from the bond side (the floor fund's own reinvestment and the coupon gap), not from stocks.

**The number that changes a decision:** +16 points of top-reach (76.7% -> 92.9%) for $1,613 expected, paid out of
Laura's upside, not the facility's. Raising the bottom too (C) is a step too far: with the office's $3,700 rounding
margin, the gift falls below a $160k bottom in 3.4-4.9% of paths. D is the cautious middle.

**Fits the locked lines?** Yes for the TNA: Note 3 ("stocks only set how far her gift rises above her promised
minimum"; "a rise before 2031 lifts the top") is exactly what B keeps. Note 2 ("IBTM ... a floor for her facility
contribution") is strengthened: IBTM ends up holding the whole announced amount. **No WInS trade:** it's a future rule
for Laura's real plan (one sale in Jan 2031), so the frozen book is untouched. It does cost two things in the
narrative: "nothing is traded from 2028 to 2033" becomes "one trade, on the day she speaks", and the Courtroom's
"top reached three times in four by choice" becomes "nine in ten, because we stop betting once she has spoken".
**Verdict: IPS, the strongest of the five.** Thursday's synthesis has to choose between "3:1 by choice" (Idea 1) and
"lock what you announce" (B). Keel's lean is B, with the bottom unchanged. The free-call arithmetic goes to the Final
Report.

---

## Idea 3. The failure corner is ten weeks wide: name the real weak point instead

**One sentence.** V25's "we can name exactly where it breaks" names a corner (yields falling ~2 points in the 71 days
before the January 2027 purchase while the 2028 deposit halves) that history crossed only in 1980-82. The plan's real
dependency is on the first sixth of the 2028 deposit, not on luck in rates.

**Why a judge cares.** Client Knowledge and the "high degree of certainty" requirement. A precise, checkable statement
of what the payments need beats a scary corner that a rates judge will see is almost empty.

**Test (`R08_3_corner.py`).** A deterministic map on the bootstrapped 22 Oct curve (the same as `D1_split.py`), the
model's chance of each move in 71 days, every 2- and 3-month change in FRED GS10 since 1953 (monthly averages, 880
windows), and a Monte Carlo that carries any unfunded slice through 2027 until the 2028 deposit buys it.

| yields before the build | 2028 deposit needed to finish the ladder | model chance in 71 days | history, any 2-month window |
|---|---|---|---|
| -0.25pp | $6,375 | 29% | - |
| -0.5pp | $14,102 | 13% | 8.5% |
| -1.0pp | $30,223 | 1.2% | 1.7% |
| -1.5pp | $47,280 | 0.033% | 0.68% |
| -2.0pp | $65,335 | 3 in a million | 0.23% (worst -2.57pp, to May 1980) |

The fall that uses up a deposit of $75k (V25's "more than halves") is 2.26pp; of $50k, 1.58pp; of $25k, 0.84pp; of
$0, **0.04pp**. Monte Carlo with 2027 carried: payments left unfunded with a deposit of **$0: 46.6%; $25k: 2.9%;
$50k: 0.02%; $75k or more: 0**. The gap the deposit fills: p95 $21,367, p99 $31,239, maximum $60,124.

**The numbers that change a decision:**
1. The certainty sentence can be positive and exact: "the payments need at most a third of her 2028 deposit in all
   but 2 of 10,000 modelled futures" ($50k, 0.02%), which is stronger than a corner and true.
2. The IBTR note's "about 0.2 percentage points" was right on its day (6-7 Oct ET). On the 22 Oct curve the threshold
   is 0.04pp ($1,139 headroom). Don't repeat "0.2" as current in the IPS; the conditional wording is safe.
3. Without the 2028 deposit, the ladder is short in about half of futures. The deposit is load-bearing as the
   ladder's backstop, which is Aha 3 (her income and yields fall together) in one number.

**Fits the locked lines?** Yes (IBTR note: "the 2028 deposit would top up the ladder"). No trades.
**Verdict: IPS (it fixes V25's "where it breaks" sentence) + Final Report (the map and the 1980 history).**

---

## Idea 4. Coupons buy more of the bond that paid them, never a cash-like fund

**One sentence.** Every number the office has published silently assumes each coupon buys more of its own rung on the
day it arrives. Write that as a rule, because the easy alternative, sweeping coupons into a short Treasury fund,
leaves the ladder short with no market move at all.

**Why a judge cares.** Portfolio Analysis and "how it guides construction and decisions". The rungs were sized
assuming coupons earn the rung's own yield (4.7-5.3% on 22 Oct). A sweep earns the 3-month yield (4.22%), so it gives
away the term premium on ten years of coupons. A practitioner judge knows reinvestment policy is where matched
ladders really leak.

**Test (`R08_4_coupons.py`).** Same 200,000 rate paths; coupons rolled monthly in a 3-month bill fund, against own-rung
reinvestment (the model's default), against holding cash (a bound).

| ten-payment shortfall | own rung (default) | bill-fund sweep | cash |
|---|---|---|---|
| median / p95 / p99 | $0 / $25,111 / $32,604 | **$7,793** / $39,455 / $46,125 | $42,906 / $53,189 / $57,511 |
| chance short > $1k | 47.1% | 60.0% | 100% |
| chance it outruns leftover cash + Laura's half (rho 0 / 0.5) | 8.7% / 10.6% | **21.0% / 23.5%** | 80% |
| no rate move at all (deterministic) | $500,000 delivered | **$492,429** | - |
| yields -1pp / -2pp for good | $489,164 / $479,040 | $482,004 / $472,302 | - |

**The number that changes a decision:** a sweep costs **$7,571 on day one** and more than doubles the chance that the
gap reaches the facility gift (8.7% -> 21.0%). Caveat: the model ignores roll-down, so own-rung reinvestment is a
little optimistic and part of the gap is the curve's slope. The direction and the order of magnitude stand.

**Fits the locked lines?** Yes. "Reinvested coupons fund the rest" (Nov-2039) and "reinvested coupons funding part of
each" (Nov-2041) are exactly this rule. Note 1's "proceeds held in a short-term Treasury ETF" is about principal for
the 11 months between the Feb-2037 maturity and the Jan-2038 payment, not about coupons, so it doesn't clash. No WInS
trade: the next coupons fall after the 6 Nov freeze.
**Verdict: IPS, half a sentence** ("each coupon buys more of the bond that paid it"); the table goes to the Final Report.

---

## Idea 5. The January 2033 re-match: set aside the gap plus a cushion sized by the forecast's own error

**One sentence.** In January 2033, set aside the coupon gap projected from that day's yields plus a flat $7,500 in
T-bills next to the ladder, so that no share is ever sold to meet a payment again. A cushion sized by a rate stress
doesn't work.

**Why a judge cares.** The case asks how the reserve's composition "should change, if at all". The answer becomes
"once, on a date we name, by a sized amount, and never again", and it is what makes the locked TNA line ("VT ... not
standing between Laura and a payment deadline") true. Today's rule sells stock to meet payments in **44.5%** of
paths, 31.1% of them after 2033.

**Test (`R08_5_rematch.py`).** Set-aside A is drawn from leftover cash, then Laura's half, then the gift. The bills earn
nothing (conservative). "Short" = the 2033-42 shortfall above A by more than $1k, which is when stock would have to be
sold after 2033.

| rho 0, 7.5% | stock must be sold after 2033 | stock sold in Jan 2033 (median) | top reached | gift below bottom | gift cost (mean) | unused, back to Laura (mean) |
|---|---|---|---|---|---|---|
| today (no set-aside) | 31.1% | - | 76.7% | 0.75% | - | - |
| projected gap only (Archive) | 31.1% | 33.5% ($8,027) | 76.7% | 0.75% | $0 | $367 |
| gap after a further 1pp stress | 23.5% | 37.1% | 76.2% | 0.86% | $68 | $714 |
| gap after a further 2pp stress | 17.1% | 40.6% | 75.7% | 0.95% | $123 | $1,191 |
| gap + $5,000 | 3.25% | 66.3% | 74.3% | 1.57% | $396 | $4,266 |
| **gap + $7,500** | **0.15%** | 70.8% ($7,500) | 72.7% | 2.15% | **$676** | $6,691 |
| gap + $10,000 (about L-10's test) | 0% | 74.7% | 70.7% | 2.91% | $1,028 | $9,187 |

With rho 0.5, the $7,500 row reads 0.15% / 71.0% / 3.27% / $830. The error of a 2033 projection (true minus projected
gap) is p95 **$5,462**, p99 **$7,146**.

**What it shows.**
1. The Archive's "set aside the projected gap" is necessary but not enough: it leaves post-2033 stock sales in 31% of
   paths, the same as today, because rates keep moving for nine more years.
2. A stress-based cushion (the way banks size capital) fails here: a further 1-2pp fall adds only $1-2k, because by
   2033 most coupons are already reinvested and locked. The forecast's own error is the right ruler.
3. **The number that changes a decision:** $7,500 is the p99 of that error, and it takes post-2033 stock sales from
   31% to 0.15% for $676 of mean gift. $10,000 (L-10) buys the last 0.15% for another $350 and 2 more points of
   top-reach.
4. The cost: a stock sale in January 2033 in ~71% of paths (small, median $7,500), and the bottom is missed in 2.2%
   rather than 0.75% *in this accounting*, because unused cushion returns to Laura. If unused cushion is returned to
   the gift once the payments no longer need it (L-10's design), part of that comes back.

**Fits the locked lines?** It is what makes TNA Reflection 3 true. It refines V25's 2033 sentence ("setting any such
gap aside") into "the gap plus a fixed cushion". It is a 2033 action in Laura's real plan, so no WInS trades.
**Verdict: IPS (amend the 2033 sentence: gap + a fixed cushion) + Final Report (why stress-sizing fails; the error
table).**

---

## Not tested: the Taiwan dollar and inflation on the half Laura keeps
There's no USD/TWD or Taiwan construction-cost series on file (only point figures: USD/TWD 31.82 on 18 Sep, 4.0-5.6%
daily-change vol; construction +6.53% y/y, ~3.5%/yr since 2021). A model run would mean inventing a path, so the Lab
didn't. The case-level point stands without a model: Laura's kept half (median ~$28k in 2033, in VT, which holds
stocks in many currencies) is the only money that moves with world prices rather than in fixed dollars.

## Summary table (rho 0, 7.5% unless noted; all MODEL)

| # | Idea | Headline number | Decision it moves | Fits TNA / WInS freeze | Trades? | Verdict |
|---|---|---|---|---|---|---|
| 1 | Two dials: share = generosity, haircut = confidence | share moves exact top-reach < 3 pts; 10% haircut: ratio 3.3 -> 6.4 for -$1,342 median gift (kept by Laura); "three in four" = within $1k (exact 69.9%, event 72.8%) | the stated over-promise ratio; the definition of "three in four" | yes | none | **IPS** (one clause) + Final Report |
| 2 | Lock what you announce (2031 sale of the promised half into IBTM) | top reached 76.7% -> 92.9% (90.7-91.2% under stress) for $1,613 expected ($917 median) of a ~$193k total; the cap hands Laura $4,406 a path on average | replaces "3:1 by choice" with "stop betting once she speaks"; one trade in 2031 | yes (strengthens Notes 2-3) | none in WInS; one in Laura's 2031 plan | **IPS** (strongest) |
| 3 | The failure corner is ten weeks wide | 2pp fall in 71 days: 3 in a million (history 0.23%, only 1980-82); payments unfunded: deposit $25k 2.9%, $50k 0.02%, $0 46.6%; threshold now 0.04pp, not 0.2 | rewrite V25's "where it breaks" sentence; don't repeat "0.2" | yes | none | **IPS** (sentence fix) + Final Report |
| 4 | Coupons buy more of their own bond | a bill sweep: -$7,571 with no rate move; median short $7,793; reaches the gift 8.7% -> 21.0% | add the reinvestment rule | yes (it is the WInS notes' rule) | none | **IPS** (half sentence) |
| 5 | 2033 re-match = projected gap + $7,500 | post-2033 stock sales 31.1% -> 0.15% for $676 mean gift; a stress-sized cushion fails (23.5% / 17.1%) | size of the 2033 set-aside (vs L-10's $10k) | yes (makes Reflection 3 true) | none in WInS; one in Laura's 2033 plan | **IPS** + Final Report |

Killed on the way: raising the 2031 bottom to "floor + locked half" (C: 3.4-4.9% below the bottom); stress-sized 2033
cushions (they don't cover the forecast error).
