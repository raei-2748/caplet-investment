# Numbers answers to the fixed-income judge's arithmetic attacks (Fri 20 Nov 2026, Sydney)

Analysis worker for the numbers owner. Research notes, not report prose. The attacks are in
`judge_fixed_income_pm.md` (this folder). Every figure below is one of three kinds. A **register** figure is quoted
from `../../NUMBERS.md` with its section. **MODEL** is the register's engine run on the 6 Nov 2026 curve. **Keel
arithmetic** is sums on register figures. Every new figure comes from one scratch script,
`../../numbers/scratch_pooled_2026-11-20.py` (run from the repo root:
`python3 -I keel/final_report/numbers/scratch_pooled_2026-11-20.py`, about 10 seconds). It imports engine, plan and
completion and changes none of them. It writes no file, and it asserts every register figure it starts from; all the
asserts pass. No register figure moves here, and NUMBERS.md is not edited (section 9 is another worker's this
morning). "Today's forward rates" means the rates implied by today's prices on the 6 Nov 2026 curve, and the report
says "today's market rates" (WORDS l.40).

---

## Attack 9 (the most important). Is the zero-interest test run bond by bond or pooled?

**The question.** The judge asks whether the test that sizes the extra Treasuries ($36,774, NUMBERS 2) is run bond by
bond or pooled. In a pooled test all cash across the ten is netted, so from 2033 a later bond's coupons can pay the
current year's $50,000. If the test is run bond by bond, a pooled rerun should give the size.

**The answer: neither. It is a hybrid, and the ten themselves are run bond by bond.** Each of the ten Treasuries at its
plain size keeps its own coupons for its own payment. Only the extra Treasuries are pooled: their cash waits for the
next payment due and pays any rung's gap, and any surplus carries forward. The code is in `numbers/completion.py`.

- The design is stated in the docstring, l.4-8: "Design H_plain: the ten rungs at their plain size (design A sized at
  today's forward rates, each rung's own coupons reinvested for its own payment, as the Trading Notes say), plus a
  pooled backstop of extra face in the same Treasuries ... whose coupons and principal wait in a short-term Treasury
  ETF for the next payment due."
- The ten run bond by bond (l.115-118):
  ```python
  def own_amounts(units, world, insts=I):
      """Money each rung's own flows reach on its own payment date (design A), uncapped."""
      return {y: units.get(y, 0.0) * sum(a * world.grow(d, date(y, 1, 1)) for d, a, _ in E.rung_flows(insts[y], world))
              for y in Y}
  ```
- The extra Treasuries are sized against each rung's own gap (l.215-221):
  ```python
  def backstop_for(insts, base_units, r=-WAIT_FEE):
      w = Flat(c, r)
      oz = own_amounts(base_units, w, insts)
      need = np.cumsum([(E.PAYMENT - oz[y]) * _defl(date(y, 1, 1), r) for y in Y])
      return lp_min_cost(insts, np.zeros(10), need, r)
  ```
- Only the extra is pooled (`_cum`, l.176-186: `ny = E.next_payment(d)`, "held to the next payment at a flat r"). The
  linear programme requires the cumulative cash by each 1 January to cover the cumulative gap (`lp_min_cost`, l.189).
  The call is `back = backstop_for(cost_cut(insts), plain, -WAIT_FEE)` (l.242): the bill fund's 0.15% on every waiting
  dollar and every iBond fund flow 0.5% smaller.
- The register already says so in NUMBERS 2, l.233: "That is pooling confined to the extra face."

**The pooled rerun** (MODEL, scratch part A). Every other rule is kept: cash waiting earns nothing and pays the bill
fund's 0.15% a year, every iBond fund flow is 0.5% smaller, the ten are held at their plain sizes, and the extra buys
more of the same bonds and funds, sized by the same exact linear programme.

| Test | Extra Treasuries, 1 Jan 2027 money | **January 2028 money** | Less than the call | What the extra holds (face) |
|---|---|---|---|---|
| The call (ten bond by bond, extra pooled; NUMBERS 2) | $35,213 | **$36,774** | | IBTQ $1,023, IBTR $4,342, Feb-2037 $5,603, May-2038 $6,003, Nov-2039 $6,152, Nov-2040 $7,284, Nov-2041 $7,304 |
| Pooled from 2033 only (the judge's own words: "From 2033 the later bonds' coupons can pay the current year's $50,000"; to 2032 each coupon stays with its own payment) | $32,658 | **$34,106** | $2,668 | Nov-2039 $9,021, Nov-2040 $13,734, Nov-2041 $14,290 |
| All cash pooled across the ten (a dedicated book, the escrow verifier's way) | $32,040 | **$33,460** | **$3,313** | Nov-2040 $17,814, Nov-2041 $19,474 |

- **Check against the register.** At exactly 0% (no bill fee, no 0.5%), the same rerun gives the register's own pair:
  the call's twin $33,484 against the pooled $30,636. That is $2,849, NUMBERS 2's "P100 ... $2,849 cheaper" (l.257).
- **Under the standard, each variant pays all ten with nothing left over.** Left after 2042 if cash waiting earns
  nothing (no fee): call $2,604, from 2033 $2,450, all pooled $2,420. At today's forward rates the money that comes back
  is $75,934, $70,481 and $69,147 on 1 Jan 2042, which is $46,566, $43,222 and $42,404 in 1 Jan 2033 money.
- **The reinvestment exposure is the same either way.** At zero interest, the ten as written, with no extra, fall short
  by **$54,595** whether they are run bond by bond or pooled. Run bond by bond, the gap is spread over all ten years,
  from 2033 $2,587 to 2042 $7,376 (NUMBERS 8h). Pooled, it all lands at the end: 2040 $13,108, 2041 $21,415 and 2042
  $20,072 (MODEL, scratch A6). Pooling makes no money (card Q20 row 1). The judge's "overstates the reinvestment
  exposure" is wrong for the total. What the bond-by-bond test overstates is the cost of covering the gap, because an
  early gap needs holdings that pay early, and those cost more for each dollar they pay at zero interest than the long
  bonds do.

**The timing, which shows whether pooling is legitimate** (MODEL, scratch A3, under the standard).

| 1 January | All pooled: cash counted for this payment | All pooled: balance carried after it | The call: own rung plus extra cash | The call: carried after |
|---|---|---|---|---|
| 2033 | $126,880 | $76,880 | $56,621 | $6,621 |
| 2034 | $48,191 | $74,956 | $48,089 | $4,701 |
| 2035 | $45,586 | $70,430 | $47,503 | $2,196 |
| 2036 | $42,366 | $62,691 | $47,807 | $0 |
| 2037 | $38,519 | $51,115 | $50,000 | $0 |
| 2038 | $35,463 | $36,501 | $50,000 | $0 |
| 2039 | $33,699 | $20,146 | $50,000 | $0 |
| 2040 | $32,134 | $2,249 | $50,000 | $0 |
| 2041 | $47,754 | $0 | $50,000 | $0 |
| 2042 | $50,000 | $0 | $50,000 | $0 |

- **The judge's example.** Take the 2042 payment's own bond, the 3.125% Nov-2041, at its plain face of $29,021. Under the
  call all of its $42,624 at zero interest waits for 2042. Pooled, $5,441 of its 2027-2032 coupons count for 2033,
  $907 a year pays each payment from 2034 to 2041, and 2042 gets only its principal and last coupon, $29,928. Its 2034
  coupon pays the 2035 payment. That is allowed only if no later 1 January is left short, and the cumulative test
  checks exactly that: by every 1 January, the cash received must cover the payments due, and cash can only be carried
  forward, never borrowed back. Pooled, the balance stays positive through 2040 and is nil after 2041 and 2042, so those
  two payments are the ones the extra is sized for. That is why all the pooled extra sits in the Nov-2040 and Nov-2041
  bonds, whose principal arrives 47 days before each of those payments.
- **So pooling is legitimate as finance.** It is the escrow verifier's own convention. Card Q20 row 20 says "Escrows
  pool every security's cash against one schedule", and verification reports "assume that all cash balances are not
  reinvested". The call's hybrid is stricter than the test it cites, by $3,313 in January 2028 money.
- **What pooling costs is the record's words, not safety.** Pooled at today's forward rates, the 2034-2040 payments get
  only 58% to 76% of their $50,000 from their own Treasury's cash of that year. $40,826 of the 2033 payment would come
  from the 2038-2042 bonds' coupons (MODEL, A5). Neither sits well with the WInS notes' "Held to maturity, its fixed
  coupons and principal cover most of it; reinvested coupons fund the rest" (WN l.18, l.24; CANON A17, C17, D7). That
  is the reason NUMBERS 2 gives for rejecting the pooled ten (P100) at exactly 0%. IPS l.13's words ("10 Treasuries ...
  each maturing just before it's needed") hold either way. Pooling from 2033 only keeps the WInS notes' words true up to
  2033 and nets the reserve from then, which reads naturally under IPS l.17 ("From 2033 the Treasuries are the
  operating reserve").

**What the re-size would do to the range** (MODEL, central path, today's forward rates, VT at 7.5%, the same range
rule; scratch A4). Only the central path was rerun, not the house model or the history.

| | First slice of the 2028 deposit | Floor money | VT | Bottom before rounding, stated | Top before rounding, stated | Excess | Half kept | Half kept plus excess |
|---|---|---|---|---|---|---|---|---|
| The call (register, section 4) | $39,162 | $81,244 | $29,594 | $97,605, **$95,000** | $117,142, **$115,000** | $7,503 | $21,179 | $28,682 |
| Pooled from 2033 | $36,494 | $83,200 | $30,306 | $99,954, **$95,000** | $119,962, **$115,000** | $10,452 | $21,689 | $32,141 |
| All pooled | $35,849 | $83,673 | $30,478 | $100,523, **$100,000** | $120,644, **$120,000** | $6,165 | $21,812 | $27,978 |

- **Full pooling moves both stated ends up one $5,000 step**, to $100,000-$120,000. Both clear their steps by little,
  $523 and $644. Pooling from 2033 keeps $95,000-$115,000, by $46 at the bottom and $38 at the top. So pooling is not a
  one-figure change. If the lead adopts it, every section of the register has to be re-sized (sections 2, 4 and 5,
  8a-8w), and the stated range would sit on a knife edge.

**Design B, "about $16,000 less", checked.** Card Q20's design B costs $319,687 at exactly 0%, against the call's
$335,771 at exactly 0%: **$16,084 less** (MODEL; register NUMBERS 2), so the arithmetic is right. But design B buys
nothing for 2033 or 2034. It holds no IBTM or IBTO rung, and it re-sizes the other eight (scratch A0). The store row the
judge cites (pack C row 5) says so itself: "only eight Treasuries in January 2027". So the $16,084 is the price of
dropping two of IPS l.13's ten, not the price of pooling. With the ten bought as the IPS says, pooling saves $2,849 at
exactly 0% and $3,313 in January 2028 money on today's standard.

**What the report should say.** This is the lead's call; Keel's register call is the hybrid (NUMBERS 2, ASK_HUMANS Tue
10 Nov 07:04).
- *If the hybrid stays:* one clause for a bond reader. In substance: the test pools the extra Treasuries' cash across
  all ten payments, while each payment's own Treasury keeps its own coupons, as the trading notes describe. Netting
  those too, as an escrow verifier would, would need about $3,300 less. Never "the test pools all cash". Never "design
  B ... $16,000 less" without "only eight Treasuries in January 2027".
- *If the lead pools from 2033:* the extra Treasuries become about $34,100 and the stated range is unchanged (thinly).
- *If the lead pools fully:* the extra Treasuries become about $33,500 and the range becomes $100,000-$120,000 (thinly).
  Both are register-wide re-runs.

---

## Attack 3. The WInS book scaled to $450,000 beside the plan in January 2028

**The question.** Reconcile Table 1, scaled up, with Section 3, and check the judge's figures.

**The answer** (register 8g, 8m, section 4 and card Q17 row 24; the bridge is Keel arithmetic, scratch part B). Both
sides are at cost: the money put in, the basis Wharton asks for in Table 1.

| | WInS book at cost (8g) | Book x 1.5 | Plan in January 2028 at cost (section 4) | Plan less book x 1.5 |
|---|---|---|---|---|
| Payment Treasuries (the ten; in the plan also the top-up and the extra Treasuries) | $195,886.53, 65.30% | $293,830 | $339,162, **75.37%** ($300,000 + $2,388 + $36,774) | **+$45,332, +10.07 points** |
| Floor (book: 3,361 IBTM shares as the floor stand-in) | $72,765.65, 24.26% | $109,148 | $81,244, **18.05%** | **-$27,904, -6.20 points** |
| VT | $26,524.61, 8.84% | $39,787 | $29,594, **6.58%** | -$10,193, -2.27 points |
| Cash and purchase costs (WInS only) | $4,823.21, 1.61% (cash $3,513.79, 1.17%, and purchase costs $1,309.42, 0.44%) | $7,235 | $0 | -$7,235, -1.61 points |
| Total | $300,000, 100% | $450,000 | $450,000, 100% | |

- **The judge's figures all check**: 65.3%, 24.3%, 8.84% and 1.61%; 75.4%, 18.1% and 6.6%; $109,148 against $81,244.
  One caveat: 1.61% is the void version 1 cash row (8g). Table 1 shows it as cash 1.17% plus purchase costs 0.44%.
- **The floor and VT are split the same way in both: 73.29% and 73.30% of what is left.** The floor is smaller in the
  plan only because less is left: $110,838 against $148,935.
- **The one reason.** The plan's first $39,162 of the 2028 deposit goes to the payments before the floor and the
  shares, and the book holds neither part of it. Of the +$45,332:
  - **$36,774 is the extra Treasuries.** They were sized after the book was built (NUMBERS 2).
  - **$8,558 is the ten's price.** Yields fell between the fills (6-7 Oct ET) and the IPS's curve (6 Nov). The engine's
    ten held cost $289,216 on 7 Oct and $302,287 on 6 Nov (8b), $13,071 more. The tail's year of carry adds $101 (the
    top-up is $2,388 against $2,287). The book scaled up sits $4,614 above the engine's 7 Oct value: each rung holds
    65.6-70.4% of a full rung, 68.0% in all against two-thirds (8m), and WInS fill prices differ from the curve.
  - The WInS cash and purchase costs, $7,235 scaled, have no counterpart in the plan.

**What the report should say.** Add one reconciliation row or note under Table 1 that says once: Table 1 times 1.5
holds $293,830 in payment Treasuries, $109,148 in the floor and $39,787 in VT; the plan in January 2028 holds $339,162,
$81,244 and $29,594. Give one reason: the book was built before the reserve was sized, so it holds neither the top-up
nor the extra Treasuries, which come first in the plan. Then add one fact: what is left splits the same, about 73% to
the floor and 27% to VT. This is INTENT's own sentence (l.155-158) with the figures added. Never write "after the
freeze", "new standard" or "we changed" (INTENT l.159).

---

## Attack 11. How much of all Laura's money sits in the late-2032 fund (IBTM) in December 2032

**The answer: register, 8w part A, quoted.**

| Tue 30 Nov 2032 (8t's peak month-end) | Own lot (2033 payment) | Floor lot | Moved half's lot | **IBTM in all** | Everything she holds | **Share** |
|---|---|---|---|---|---|---|
| At net asset value | $39,352 | $84,340 | $18,861 | **$142,553** | $587,231 | **24.3%** |
| With IBTM's distributions already paid, waiting in the bill fund ($29,522) | | | | **$172,075** | | **29.3%** |

- **What the three lots pay** (sections 4 and 8h, at today's forward rates): the 2033 payment's own lot $50,000, the
  floor $102,365 and the moved half $20,138, so **$172,503** in all.
- So the judge's "roughly $170,000 ... close to 30%" checks, but only when IBTM's distributions already paid are counted.
  The part a fund event can still touch is 24.3%, and 25.7% to 25.9% from January 2028 to January 2031.
- **Promised dollars** (8w): $165,000 of the $615,000 she will owe or state (26.8%) rests on IBTM from the move: the
  2033 payment and the whole $115,000 top.
- **IBTM is the largest single holding on every date.** It is 3.3 to 3.9 times the next of the ten payments' own
  holdings.
- **Her share of the fund is 0.019% to 0.022%** at its 17 Nov 2026 net assets of $641,351,942 (read at source, 8w B).
  The judge's "$603m" is the 27 Oct figure.
- **What one fund event does** (8w C, section 3): an early end, a merger or a moved end, with cash waiting earning
  nothing, leaves the top at worst $4,589 short, the bottom $2,887 short and the ten $1,827 short (exit 2 Jan 2031).
  At today's market rates nothing is short.

**What the report should say.** One Section 2 sentence that names the concentration: one fund, IBTM, holds about a
quarter of all Laura owns from 2028 to 2032 and carries the 2033 payment, the bottom and the top. Its risks are a
fund's, not the Treasury's: an early end, a merger or a moved end. Pair it with Table 3 row 4's watch and the
$4,589. Never set it against Table 1's 32.50%, which is IBTM in the $300,000 WInS book at cost (8w).

---

## Attack 12. The per-payment table for the WInS book

**The question.** For each payment: the instrument, its maturity, the face or units, the yield at fill, the payout
against the scaled $50,000 ($33,333), the gap between payout and 1 January, and the book's DV01 against the
liability's on the 6 Nov curve.

**The answer** (8g, 8h and 8m for units, prices and dates; the rest is new and labelled; scratch part D).

| Payment | Holding (identifier) | Ends or matures | Held (8m) | Yield at fill | Share of a full rung | Pays at today's forward rates (against $33,333) | Pays if cash waiting earns nothing (against $33,333) | Cash before 1 January (8h) |
|---|---|---|---|---|---|---|---|---|
| 2033 | IBTM, rung lot | on or about 15 Dec 2032 | 1,142 shares at $21.65 | (stand-in 5.07%) | about 67.6-67.7% | about $33,800-$33,850 (+$470 to +$520) | about $32,050-$32,100 (-$1,260) | 10-12 days |
| 2034 | IBTO | on or about 15 Dec 2033 | 1,024 shares at $22.86 | (5.13%) | about 67.6-67.7% | about $33,800-$33,850 (+$470 to +$520) | about $31,650-$31,700 (-$1,660) | 10-13 days |
| 2035 | IBTP | on or about 15 Dec 2034 | 927 shares at $23.90 | (5.18%) | about 67.6-67.7% | about $33,800-$33,850 (+$470 to +$520) | about $31,260-$31,310 (-$2,050) | 10-14 days |
| 2036 | IBTQ | on or about 15 Dec 2035 | 894 shares at $23.46 | (5.23%) | about 67.6-67.7% | about $33,800-$33,850 (+$470 to +$520) | about $30,790-$30,840 (-$2,520) | 8-12 days |
| 2037 | IBTR | on or about 15 Dec 2036 | 853 shares at $23.24 | (5.26%) | about 67.6-67.7% | about $33,800-$33,850 (+$470 to +$520) | about $30,170-$30,210 (-$3,140) | 10-14 days |
| 2038 | 4.750% T-bond (912810PT9) | 15 Feb 2037 | $20,000 face at 96.019 | **5.25%** | 69.13% | $34,566 (+$1,232) | $29,975 (-$3,358) | 318 days (10.4 months; 10.5 from maturity) |
| 2039 | 4.500% T-bond (912810PX0) | 15 May 2038 | $20,000 at 93.076 | **5.31%** | 70.22% | $35,109 (+$1,775) | $30,350 (-$2,983) | 229 days (7.5 months) |
| 2040 | 4.375% T-bond (912810QD3) | 15 Nov 2039 | $18,000 at 90.005 | **5.45%** | 65.37% | $32,684 (**-$649**) | $28,238 (-$5,096) | 47 days (1.5 months) |
| 2041 | 4.250% T-bond (912810QL5) | 15 Nov 2040 | $18,000 at 87.724 | **5.51%** | 67.80% | $33,899 (+$565) | $28,710 (-$4,623) | 47 days (1.5 months) |
| 2042 | 3.125% T-bond (912810QT8) | 15 Nov 2041 | $20,000 at 74.955 | **5.60%** | 68.92% | $34,458 (+$1,125) | $29,375 (-$3,958) | 47 days (1.5 months) |

- **Bond yields at fill** (MODEL: street yield from the WInS clean fill price, settlement 7 Oct 2026, standard
  accrual). They reproduce card Q17 row 33's 5.25-5.60%, which sits 2.6 to 8.8 basis points from the 6-7 Oct curve,
  inside the team's 25-basis-point rule.
- **Fund yields at fill are not in the repo.** The bracketed figures are the engine's stand-in, the 7 Oct par curve at
  each fund's average maturity, and are not iShares' yield to maturity. IBTM's published figure was 4.86% on 23 Oct,
  after yields had fallen (section 0). Do not print the stand-ins as the funds' yields.
- **Shares of a full rung and payouts.** For the bonds, the share is WInS face over the register's 6 Nov face (section
  1), exact on that curve. The payouts are that share times $50,000 at today's forward rates, and times the own rung's
  zero-interest payout (8h). For the funds, the share is card Q17's 67.6-67.7% on the 23 Oct curve, because the funds'
  6 Nov prices are not in the repo, so the fund payouts are approximate. Keel arithmetic.
- **In all,** the book's ladder pays about $339,800 against $333,333 at today's forward rates, about 102%. Card Q17 got
  $510,396 against $500,000 when scaled up on the 23 Oct curve. If cash waiting earns nothing it pays about $302,700,
  some $30,600 short, because the book was built to need reinvestment ("reinvested coupons funding part of each", WN
  l.24). It holds no extra Treasuries. The 2040 bond is the one rung below scale, because bonds trade in $1,000 lots
  (8m).
- **The gaps.** The judge's "about 1.5 months elsewhere" holds only for the three November bonds. The May-2038 bond pays
  7.5 months early and the five funds 8 to 14 days early, with IBTA's one early end 29 days early (8h).
- **DV01** (MODEL, scratch D). This is the change in 1 Jan 2027 value for a 1-basis-point parallel move of the 6 Nov
  par curve, with fixed flows; the method reproduces section 1's $234.

  | | DV01 | Against the liability's |
  |---|---|---|
  | The payments, scaled (ten x $33,333) | $200 | |
  | The WInS book's ten rungs | about $159 | 80% |
  | The book's floor stand-in (3,361 IBTM shares) | about $38 more | no liability against it |
  | The plan's ten at plain size (section 1) | $234 | 78% of $300 |
  | The plan's ten plus the extra Treasuries | $267 | 89% of $300 |

  The shortfall in DV01 is the coupons arriving early, the reinvestment risk of section 2. The plan does not answer it
  by matching DV01. It answers it with the zero-interest sizing, which also brings the DV01 closer.

**What the report should say.** If Section 2 gets the table, use one row per payment with the bond yields at fill, the
funds' share and payout marked approximate, and the gap column taken from 8h, not "1.5 months elsewhere". Put the DV01
pair in one clause: the book moves about $159 for each basis point against the payments' $200. The difference is the
coupons that arrive early, which is the risk the extra Treasuries cover in Laura's plan. The register must adopt these
figures before the report prints them (NUMBERS section 9 is the owner's).

---

## Attack 25. The band between no deposit and about $39,000

**The question.** For 2028 deposits of $0, $10,000, $20,000, $30,000 and $39,162, what fails, and by how much on each
basis?

**The answer.** The register's section 5 holds the $0 row and the zero-interest column for $10,000-$30,000. The other
columns are new, from the same ledger (MODEL, scratch part E). The order is the IPS's and the call's: first the $2,388
that finishes the ten, then the extra Treasuries bought pro rata. Yields are today's.

| 2028 deposit | Extra Treasuries bought | At today's forward rates | Cash waiting earns nothing (section 5) | And the bill fund's 0.15% | And every fund flow 0.5% smaller (the standard), years short | Floor and VT |
|---|---|---|---|---|---|---|
| $0 (missed) | none; $2,287 of the ten unbought | 2033 payment **$3,016 short** | $57,455 short, all ten | $58,775 | $59,912, all ten (2033 $5,740; largest 2041, $7,820) | nothing |
| $10,000 | 21% | all ten paid | $42,756 short, all ten | $44,095 | $45,253, all ten (2033 $928; largest 2041, $6,201) | nothing |
| $20,000 | 48% | all ten paid | $27,201 short | $28,562 | $29,731, 2034-2042 | nothing |
| $30,000 | 75% | all ten paid | $11,647 short | $13,034 | $14,213, 2035-2042 | nothing |
| $39,162 | all | all ten paid ($75,934 left by 2042) | paid, $2,604 left | paid, $1,177 left | paid, nothing left | the first dollar above this goes to the floor |

- **From $2,388 up, the ten are paid at today's market rates.** Below $39,162 they fall short only if cash waiting earns
  nothing. Each dollar of deposit above $2,388 cuts that shortfall by about $1.55, because each dollar of extra
  Treasuries pays about $1.55 at zero interest (8h: $57,200 for $36,774). The building gets nothing.
- **Above $39,162** the floor shrinks almost dollar for dollar (section 5). The floor takes all of what is left until
  the deposit reaches $78,324, from which "most" holds (5(c)).
- **A smaller deposit is not one of the IPS's two reasons to change** (section 5). The plan absorbs it in its own order.
- **The 31 March 2028 test date is the report's own.** It is Table 3's reading, never the IPS's date (CLAUDE.md, Day
  12).

**What the report should say.** One sentence for 3e. A 2028 deposit smaller than about $39,000 still completes the ten
at today's market rates, but leaves them short if cash waiting earns nothing: by about $43,000 at $10,000, falling to
about $12,000 at $30,000. It leaves nothing for the building. It lowers what Laura can state without being a reason to
change the plan. Each basis is named before its figure, and no odds are given.

---

## Attack 27. Does the register hold an all-Treasury plan that keeps back the same flexibility and could state about $110,000 in January 2028?

**The answer: yes, in section 4, "The all-Treasury benchmark (C8)", l.677:** "An all-Treasury plan with the same
flexibility holds back the FINAL's median half kept ($20,486, was $20,739) and pays $119,166 ($120,023), stated
$110,000 with certainty: $5,000 under the FINAL's central stated top, because the moved half's cut (2.98%) is smaller
than the floor's (4.65%)." The code is `run_numbers.py` l.281-293 (`same_flexibility_payout`,
`same_flexibility_stated`).

- **"In January 2028" is not in the register's words, but the rule fixes it then.** The range rule measures the floor
  once, at its purchase in January 2028 (section 0), and this plan's stated figure is all floor. Unpacked (Keel
  arithmetic, scratch part F):
  - January 2028: $94,579 to the late-2032 fund, and $16,259 held back. The held-back money grows to $20,486 at the
    floor's forward rate.
  - The fund pays $119,166. Its zero-interest value less 0.5% is $113,625, which is stated as **$110,000**.
  - $9,166 is paid above the stated figure, so her flexibility in all is $29,653, against the FINAL's central $28,682.
- **One caveat for the comparison.** The benchmark holds back the FINAL's house-model median half kept ($20,486), not
  its central path's $21,179. Its flexibility is in Treasuries, not shares.

**What the report should say.** The judge's comparison is supported: "an all-Treasury plan holding back the same
flexibility states $110,000, known from January 2028, against the plan's $115,000 at the move". The $5,000 comes from
the moved half's smaller cut (section 4). Note that under attack 9's full pooling this comparison would move too. It
was not rerun.

---

## Attack 28. The reserve as a schedule

**The answer.** These are register figures (section 1's rung sizes, section 2's extra face, and 8a and 8h's
zero-interest columns), reproduced to the dollar by scratch part G. All are at zero reinvestment, with no bill fee.

| Payment | Own Treasury | Own rung (fund dollars or face) | Own rung pays at zero | Extra Treasuries in the same holding (face) | That extra pays over its life at zero | Extra Treasuries' cash counted for this payment | Extra covers | Carried after |
|---|---|---|---|---|---|---|---|---|
| 2033 | IBTM (ends about 15 Dec 2032) | $37,908 | $47,413 | | | $9,570 | $2,587 | $6,982 |
| 2034 | IBTO | $36,065 | $46,820 | | | $1,594 | $3,180 | $5,397 |
| 2035 | IBTP | $34,300 | $46,244 | | | $1,594 | $3,756 | $3,235 |
| 2036 | IBTQ | $32,588 | $45,549 | $1,023 | $1,430 | $2,611 | $4,451 | $1,395 |
| 2037 | IBTR | $30,922 | $44,629 | $4,342 | $6,266 | $5,759 | $5,371 | $1,782 |
| 2038 | 4.750% 15 Feb 2037 | $28,930 | $43,360 | $5,603 | $8,397 | $6,813 | $6,640 | $1,955 |
| 2039 | 4.500% 15 May 2038 | $28,483 | $43,223 | $6,003 | $9,110 | $6,945 | $6,777 | $2,123 |
| 2040 | 4.375% 15 Nov 2039 | $27,536 | $43,197 | $6,152 | $9,650 | $6,959 | $6,803 | $2,279 |
| 2041 | 4.250% 15 Nov 2040 | $26,550 | $42,347 | $7,284 | $11,618 | $7,822 | $7,653 | $2,448 |
| 2042 | 3.125% 15 Nov 2041 | $29,021 | $42,624 | $7,304 | $10,728 | $7,532 | $7,376 | $2,604 |
| **All** | | $302,287 cost | **$445,405** | $37,711 face, $36,774 in January 2028 | **$57,200** | **$57,200** | $54,595 | **$2,604 left** |

- **The reserve pays $502,605 at zero reinvestment** against $500,000 owed, so $2,604 is left. With the bill fund's
  0.15% on waiting cash, $1,177 is left; with that fee and every fund flow 0.5% smaller, nothing is left. This is the
  standard it is sized to (8h).
- **The two cash columns are the same money counted two ways.** One counts each extra holding's coupons and principal
  over its life; the other counts the cash that has arrived by each payment date. The extra's coupons are pooled
  (attack 9), so the 2033 payment draws on $9,570 of cash that arrived to 2032.
- **The market value is a by-product, with its basis named** (8h). On 1 Jan 2033 the reserve is worth about $445,700
  at today's market rates: money already received grown at today's forward rates, plus flows still to come discounted
  at them. The payments still owed are worth $399,089 on the same basis, so 111.7% is like for like. On Figure 1's zero
  basis it is worth $426,371. Never print 111.7% against the $500,000 face.

**What the report should say.** State the reserve by what it pays: ten Treasuries, one per payment, plus about $37,700
of extra face in the later seven holdings. Together they pay about $502,600 over 2033-2042 even if cash waiting earns
nothing, against $500,000 owed. If the about $445,700 is printed, say once that it is a value at today's market rates
and set it against the payments' $399,089 on the same basis, not against $500,000.

---

## New figures in this file, with their labels

All come from `numbers/scratch_pooled_2026-11-20.py`. None is in the register until the numbers owner adopts it.

- **Attack 9** (MODEL): $33,460, $34,106, $3,313 and $2,668; $32,040 and $32,658 in 2027 money; the pooled extra's
  holdings; the timing table; $54,595 split 2040-2042 when pooled; the A4 central rows ($100,523, $120,644, $99,954,
  $119,962 and their companions); 58-76% and $40,826; $69,147, $70,481, $42,404 and $43,222; $2,420 and $2,450.
- **Attack 3** (Keel arithmetic): the x1.5 column, the differences, 73.29% and 73.30%, and the bridge $8,558 = $13,071 +
  $101 - $4,614.
- **Attack 12** (MODEL and Keel arithmetic): the bond yields at fill; the funds' stand-in yields; the shares of a full
  rung on 6 Nov faces; the payouts against $33,333; about $339,800 and $302,700; DV01s $159, $38 and $267.
- **Attack 25** (MODEL): the bill-fee and standard columns, and the years short.
- **Attack 27** (Keel arithmetic): $94,579, $16,259, $113,625, $9,166 and $29,653.
- **Attack 28** (Keel arithmetic on register figures): each extra holding's lifetime payout at zero; $502,605.
