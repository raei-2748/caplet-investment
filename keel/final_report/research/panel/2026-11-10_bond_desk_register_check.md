# Bond desk check of the number register (Tue 10 Nov 2026, Sydney)

Reviewer's stance: a fixed-income portfolio manager who has run matched liability books and municipal defeasance
escrows. Scope: `NUMBERS.md` as rewritten on Tue 10 Nov (sections 0, 2, 3, 4, 5, 8a, 8f, 8h, 8i, the rest as needed),
the engine in `numbers/`, and cards Q19, Q20 and Q24. The strategy and the frozen texts (`FINAL_IPS_as_submitted.txt`,
`tna_as_submitted.txt`) are not judged; only the numbers and the claims made with them. Nothing in the repo was
changed. Every check was run on a copy of `numbers/` with the same data files (`python3 -I -B`), so no results file
was rewritten. All figures are MODEL, on the register's 6 Nov 2026 curve.

## Verdict in one paragraph

The arithmetic of the escrow standard is right: H_plain costs $335,771, the backstop is the true least-cost solution,
all ten are paid at 0%, and the funded ratio, the overflow and the run-down are on one consistent basis. The weak
points are in the words around it. The range's "certain" rests on a par-coupon stand-in for the fund's holdings, and
the evidence offered for it is circular. The 0% test is met to the dollar, with nothing spare for fees. Under the new
completion, the IPS's "Most of the 2028 deposit" fails in about one path in seven. Several "2033 money" figures mix
worlds. None of this moves the central figures ($335,771; $37,358; $95,000 to $115,000; 111.1%; $44,286).

## Findings, most serious first

### 1. "Certain" for the stated ends rests on a stand-in for the fund's holdings, and the evidence for it is circular

- **Where.** Section 3 l.182 ("true by construction"); l.191 and section 7 l.413-416 (real coupons make the model
  cautious); section 4 l.271-277 ("The evidence": house 0%, history the same, joint replay); 8i l.746 (rates 3 points
  lower: bottom $80,000 from $80,003); 8i l.763.
- **What is loose.**
  - (a) Circular evidence. `range_rule.rule` and `completion.rule` work out the "true worst case" with the same
    deduction function that sets the stated ends. So "zero-interest value below the stated top in 0% of paths" is an
    identity, not a test. Only the rounding down separates the two numbers.
  - (b) The joint replay's "funds always paid at least the stated top" is measured at historical rates. Those are always
    well above zero, so it says nothing about the zero-interest guarantee.
  - (c) The stand-in. The deduction models the fund as one par bond at the purchase yield. That is cautious only while
    the fund's real coupons are below the purchase yield (true today: IBTM 3.50% against about 4.2%). When yields fall
    about 1 point or more before the purchase, the real holdings sit at a premium and pay less at zero interest than
    the par stand-in. Zero-interest payout per $1 put in, floor bought January 2028:

    | Purchase yield against today's forwards | -3 pt | -2 pt | -1 pt | 0 | +1 pt |
    |---|---|---|---|---|---|
    | Real holdings at 3.50% coupon, against the par stand-in | -0.30% | -0.25% | -0.05% | +0.29% | +0.75% |
    | Engine's own IBTM holdings (coupon fixed in Jan 2027, about 4.25%), against the par stand-in | -0.40% | -0.41% | -0.27% | 0.00% | |

  - (d) Is it really owned? On holdings rather than the stand-in, the stated ends are not owned at zero interest in:
    - 0.40% of house paths (3.50% coupon) to 1.2% (4.0% coupon), by up to $237 to $348;
    - 9 of 585 joint windows for the bottom (largest gap $215, start Dec 1981) and 10 for the top (largest $399, start
      Sep 2002). This uses the engine's own IBTM holdings, priced on each window's own curve, as `joint_stress.py`
      already does for the realised payout;
    - 8i's rates-3-lower row: the floor pays $79,864 at zero interest against the stated $80,000. The rule's own figure
      had only $3 spare ($80,003). On holdings that row states $75,000.
  - (e) Thin rounding headroom. A friction of 0.10% of value (an ETF bought above its net asset value, the bid-ask
    spread, a fee change the prospectus allows) breaks the stated bottom in 2.0% of house paths and the top in 2.4%. A
    friction of 0.5% breaks them in 9.9% and 12.0%. Named cases with almost nothing spare: the Jun 2006 window's top
    ($110,034 against $110,000) and the rates-3-lower bottom ($80,003).
- **Correct figure or wording (note).**
  - Define each end from the fund's own holdings on the trade date: the remaining coupons and principal per share, less
    the fee to 15 Dec 2032, times the shares actually bought. Take a haircut of about 0.5% before rounding down to
    $5,000. The central range is unchanged ($99,729 x 0.995 = $99,230, stated $95,000; $119,693 x 0.995 = $119,095,
    stated $115,000).
  - Replace "The evidence: house 0% ..." with "true by construction once worked out on the holdings; the market cannot
    move either end after the move".
  - Change l.191 and l.413-416 to: "cautious at today's yields; if yields fall about a point before the purchase, the
    holdings' premium makes the stand-in slightly generous, so the rule uses the holdings".
  - 8i rates-3-lower row: stated bottom $75,000 on the holdings.
- **How verified.**
  - `completion.fund_flows` with coupon 3.50% and 4.00% on curves shifted -3 to +1 points.
  - The engine's IBTM flows (`engine.Instrument(2033).flows`) repriced on each house path and each joint window's
    Jan 2028 and Jan 2031 curves, against `completion.rule`'s stated ends.
  - The share of house paths whose unrounded end, less 0.1%, 0.25% or 0.5%, drops below its stated end.

### 2. Under the escrow standard, "Most of the 2028 deposit will fund a Treasury fund" fails in about one path in seven

- **Where.** Section 4 l.206 (floor money $82,567, 55.0%: central only); section 5 l.344-353; 8i l.746 and l.765;
  card Q20 row 13 ("still takes 'most' ... in every certain design", central only).
- **What is loose.** The floor gets 73.3% of what is left after the completion. Whenever the completion exceeds
  $47,681, the floor is under $75,000, less than half of the $150,000.
  - House model: floor money 1-in-20 low / median / 1-in-20 high $70,599 / $82,525 / $93,653. Under $75,000 in 14.6% of
    paths, against 2.4% under Mon 9 Nov's design.
  - 8i rates 3 points lower: $74,556 (49.7%).
  - Joint window from Jan 2008: $70,600 (47.1%).
  - Jul 2007 window: $75,459 (50.3%, just above half).
  - A $112,500 deposit: $55,079 (49.0% of the deposit).
- **Note.** Record it as a risk against the frozen IPS. "Most" holds centrally and fails when yields fall about 1 point
  or more before January 2028. Whether the split adapts is Caplet's strategy call, not a number to fix here.
- **How verified.** `plan.house` with `completion.margin_fn()` (200,000 paths, seed 2033): 0.733 x R. Named rows from
  `joint_stress.py` outputs (`completion_jan2028`).

### 3. The 0% test is met to the dollar, so any fee or timing slip makes "paid in full in every test" untrue

- **Where.** Section 2 l.108 and l.131-135; section 0 l.47 and l.49; section 7 l.419; 8a l.450; 8h l.717 ("met
  exactly").
- **What is loose.**
  - At 0%, the carry after 2036 is $0, and 2037 to 2042 are each met to the dollar. Nothing is spare.
  - Fees on waiting money. The ETF fee on the backstop's waiting money costs $53, $89 or $117 at 0.09%, 0.15% or 0.20%
    a year (mostly in 2036). The register's "tens of dollars" is right. But TNA note 1 puts the Feb-2037 bond's
    proceeds in a short-term Treasury ETF, and in practice the own rungs' many small coupons and the funds' monthly
    distributions will wait there too. If they do, the shortfall is $850, $1,412 or $1,877.
  - The IBTM tail. The 0% test counts the 2027 distributions of the whole IBTM rung. But the $2,287 tail is bought in
    January 2028, so its 2027 distributions ($97) are never received. The completion money does cover them: $2,388
    carried a year, against a January 2028 price of $2,280, leaves $109. Unless that $109 goes into the waiting cash
    the way 8a sends the backstop's $1,517, 2036 is $97 short at 0%.
  - Redundant evidence. The 585 history windows and the seven Regulation 126 scenarios are implied by the 0% test,
    because none of them takes a rate below zero. They are not separate evidence.
- **Note.**
  - Size the backstop with waiting money at -0.15% a year, not 0%. That costs about $154 in 1 Jan 2027 money for the
    backstop's money alone, or about $1,078 if all waiting money sits in the ETF (scaling the backstop, an upper
    bound).
  - Name the instrument as a Treasury-bill ETF (0 to 3 months), not a 1 to 3 year fund, whose price can fall.
  - Add one line to 8a: the tail's $97 also goes into cash in January 2028.
  - Word it as: "paid in full if no coupon earns anything, after fees on waiting cash; the history and insurer tests
    follow from that one test".
- **How verified.** The `completion.ledger` logic with a world that shrinks waiting money at a fixed rate (for the
  backstop only, then for all waiting money); the IBTM rung's 2027 flows from `engine.rung_flows`; `C._P0` against
  the carried completion.

### 4. The escrow release in 8h assumes each coupon is locked in a Treasury maturing on its payment date

- **Where.** 8h l.719-725 ($10,496 in 2033, then $1,549, $1,549, $1,888 ...); `reserve.release_schedule`.
- **What is loose.** The release test counts money already received at the value it is locked to reach on its payment
  date. That holds only if each own-rung coupon was put into a Treasury maturing before its payment (section 2's
  policy). If the coupons wait in the floating short-term ETF (TNA note 1's wording), the test overstates what is
  safe to release.
  - With the register's schedule, if rates follow the forwards to 1 Jan 2033 and then earn nothing, 2034-2036 are
    $170, $687 and $1,108 short ($1,965).
  - Released through 2034 and then zero: $601 short.
- **Correct figure (note).** Re-checked at 0% each 1 January, with received money counted at its value that day, the
  release is $8,530 (2033), $3,015 (2034), $2,182 (2035), then the register's figures from 2036 ($1,888, $5,547,
  $6,935, $7,009, $6,865, $7,719, $7,436). That totals $57,126, the same $44,286 in 2033 money, and it passes the
  switch-to-zero test in every year. Use it, or state the locking assumption beside the table.
- **How verified.** The register's ledger was replayed on the forward path to each year from 2033 to 2038, the
  release taken, then zero interest from that date; once with locked reinvestment (the register's schedule passes)
  and once with floating waiting money (it fails 2033 and 2034).

### 5. "Left after 2042 (1 Jan 2033 money)" discounts other worlds' money at today's forwards

- **Where.** 8h l.680 ("$24,040 ($14,743)"); 8i l.746 and l.749 (the "Left after 2042" column); 8i l.760; the joint
  replay's overflow (`joint_stress.payments` uses `c.P`).
- **What is wrong.** A 2042 dollar in a world 3 points lower, or 3 points higher, is discounted at today's forward rates.
  - Rates 3 points lower: $14,743 on today's forwards; **$19,312** on that world's own rates.
  - Inflation world: $75,717 on today's forwards; **$57,802** on its own rates (nominal $123,469).
  - The forwards row ($44,286) is right.
- **Note.** Show nominal 1 Jan 2042 dollars, or discount on each world's own path, and say which.
- **How verified.** Each world's nominal 2042 sum divided by its own `grow(1 Jan 2033, 1 Jan 2042)` from
  `joint_stress.py`'s world objects.

### 6. "Each rung funds its own payment": true at forwards; in the 0% world 2033-2036 lean on later bonds' coupons

- **Where.** Section 2 l.120 and l.154 (P100 rejected because "later bonds' coupons pay earlier payments"); 8a l.450.
- **What is loose.** At forwards each own rung pays exactly $50,000 and the backstop pays nothing (verified). At 0%:
  - The own rungs still pay what is theirs. But 2033 to 2036 take $2,587, $3,180, $3,756 and $4,451 from backstop
    money.
  - By 2033 that money ($9,098) is distributions and coupons of extra IBTQ and IBTR and the five T-bonds, all maturing
    2035-2041.
  - That is the feature for which P100 was set aside, confined to the extra face. Nothing contradicts the Trading
    Notes as the register words it.
- **Note.** Keep "Each Treasury's own coupons are reinvested for its own payment". Do not write "no payment depends on
  another bond". Suggested line: "each payment has its own Treasury; a shared reserve of extra Treasuries pays any gap
  if interest earns nothing". In Q20, give P100's real difference: it pools at forwards too (its own cash is 57% of
  the 2040 payment), while H_plain pools only the extra.
- **How verified.** `reserve.py` base and zero tables; `completion.pool_buckets` by source.

### 7. Two different figures for "3 points lower" on the five fund rungs

- **Where.** 8a l.437-441 ("Delivered if reinvested 3 pt below forwards", e.g. 2033 $48,880) against 8h l.669-673
  (e.g. 2033 $48,351).
- **What is loose.**
  - 8a's column (`extras.py`) leaves each fund's final months of cash at forward rates; 8h reprices them. The T-bond
    rows agree.
  - 8a's "Delivered if reinvestment earns nothing" has the same feature. The register explains this for the 0% column
    (l.449) but not for the 3-point column.
- **Note.** Relabel 8a's column "coupons reinvested 3 points lower; fund cash in its last months at forwards", or quote
  8h's figure. Figure 1 must use 8h.
- **How verified.** `extras.py` per-rung code uses `rung_flows(I[y], base)` for both columns.

### 8. Composition on 1 Jan 2033 counts IBTM's paid-out $50,000 as an iBond ETF

- **Where.** 8h l.688 and l.701 ("iBond ETFs $230,646 (52.0%)").
- **What is loose.** IBTM ended on 15 Dec 2032, and l.684 says its money is waiting as cash.
- **Correct figure (note).** iBond ETFs $180,646 (40.7%), cash from IBTM waiting for the payment $50,000 (11.3%),
  T-bonds $202,232 (45.6%), short-term Treasury ETF $10,496 (2.4%).
- **How verified.** Sum of 8h's composition rows.

### 9. "About $145,000" is an interpolated $144,000

- **Where.** Section 4 l.284; 8i l.758.
- **What is loose.** `np.percentile` interpolates between two $5,000 steps. The joint 1-in-20 high top is
  $143,999.99, which no one would state.
- **Note.** Use a non-interpolating percentile (method "lower" gives $140,000), or write "$140,000 to $145,000".
- **How verified.** `results_range_rule_2026-11-10.json`, `history_joint_rates_and_stocks.stated_top_p5_p50_p95`.

### 10. Section 5's thresholds hold yields still through 2027

- **Where.** Section 5 l.330-343.
- **What is loose.** The table is labelled "before 1 Jan 2027" and is right on that basis. A fall during 2027, after the
  ladder is bought, also raises the completion, because the tail and the backstop are repriced:
  - 1 point: $40,625 (the standard then survives a deposit fall of 72.9%);
  - 2 points: $44,254 (70.5%).
- **Note.** Add one line.
- **How verified.** `plan.run` with `d1` = -0.01 and -0.02 and `completion.margin_fn()`.

### 11. Two phrases claim more than the instruments give

- **Where.** Section 2 l.119 ("the municipal escrow verifier's test"); section 4 l.271 ("a fund failing to work as its
  prospectus says").
- **What is loose.**
  - An escrow verifier credits direct Treasuries (or SLGS) and uninvested cash only. Here five rungs, $4,323 of the
    backstop (IBTQ, IBTR) and all waiting money are ETFs.
  - A fund can pay slightly less than its holdings' cash flows without breaking its prospectus: an expense change made
    with notice, or trading costs on index changes and flows. That this applies to IBTM's prospectus is UNVERIFIED;
    read the wording before quoting it.
- **Note.**
  - Write "the escrow verifier's arithmetic (paid even if no coupon earns anything), applied to holdings an escrow
    would not accept".
  - Keep the prospectus clause, but let the 0.5% haircut of finding 1 carry the fund risk, not the clause.

### 12. Minor reconciling item

- `results_reserve_2026-11-10.json` key `margin_value_1jan2033_at_forwards` is $44,316. That is the backstop's cost
  grown, which ignores the 0.07% fee on its IBTQ and IBTR. The register's $44,286 (the composition, and the 2042
  money discounted) is the right figure. `exhibits/exhibit_data.py` should read $44,286, not that key.

## Where the register is right (re-run or re-derived)

- **Cost and completion.**
  - H_plain costs $335,771 and the backstop $33,484. Its units are IBTQ $332, IBTR $3,991, then $5,458, $5,856, $6,013,
    $7,127 and $7,152 face.
  - Short at 0% is $0. The Mon 9 Nov design is $22,192 short at 0%.
  - The completion is $37,358: $2,388 for the tail plus $34,970 for the backstop carried a year. The backstop's January
    2028 price, including the $1,517 of 2027 flows put in as cash, is $34,916.
- **The backstop is exact.** Checked by hand:
  - 2042 gets $7,152 x 1.03125 = $7,376;
  - 2041 gets the Nov-2040 bond's $7,127 x 1.0425 plus $223.50 of Nov-2041 coupons = $7,653;
  - the backstop's money by year adds to exactly $54,595.
  - Own rungs at 0% check against coupon counts: Feb-2037 bond 21 coupons, $43,359; Nov-2041 bond 30 coupons, $42,625.
- **Cash timing.**
  - Coupon calendars are right (15 Feb/Aug, 15 May/Nov).
  - 15 Feb 2037 is a Sunday and 16 Feb is Presidents' Day, so the bond pays on Tue 17 Feb 2037, as 8h says. 15 May
    2038 is a Saturday (paid Mon 17 May). Every T-bond and iBond payout lands before its 1 January payment.
  - The funds' cash waits (5.4 to 7.4 months) follow from the WAM dates. Their fee total ($1,098) is inside $302,287.
- **Funded ratio and run-down.**
  - $443,375 against $399,089 (111.1%) is like for like: both are on 1 Jan 2033 on the same 6 Nov forwards, and the
    own rungs equal the liabilities exactly.
  - The run-down from 112.7% to 244.4%, the $72,215 left in 2042, the $44,286 in 2033 money and the $33,461 in 2027
    money all reproduce. The last is $23 under the backstop's cost because of the funds' fee.
  - The escrow release total of $56,994 is the same $44,286 in 2033 money, under the register's locking convention.
- **Deductions.**
  - Today's values are 4.136% and 2.447%, and the shift table reproduces from -3 to +3 points.
  - The real-coupon deductions of 3.85% and 2.44% are right at today's yields.
  - The fixed-figure failure rates (12.6% and 11.6%) and the house tables of what Laura could announce reproduce.
- **Section 5.**
  - 98.4% and 75.1%; the escrow standard takes the whole deposit at a 3.63-point fall and the ladder alone at 3.89
    points.
  - Partial backstops of 22%, 50% and 79% leave the ten short at 0% by $42,712, $27,100 and $11,487. The shortfall is
    linear because the scaled backstop is spent in full.
  - A missed deposit leaves 2033 $3,016 short at forwards and the ten $57,455 short at 0%.
  - After a 1-point fall the floor pays $75,238, stated $70,000.
- **8i's worlds are internally consistent on rates.**
  - The rates-3-lower row prices the backstop, the tail, the floor (forward less 3 points, about 1.7%) and the moved
    half on the same lowered curve, and reinvests at forwards less 3 points from 2027.
  - The inflation world's ramp puts the January 2028 purchase 0.75 points higher (completion $35,121) and the 2031
    move 3 points higher.
  - The only faults are findings 1, 2 and 5.
