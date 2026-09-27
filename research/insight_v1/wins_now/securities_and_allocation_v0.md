# Securities and allocation v0: WInS week 1 and Laura's long-term instrument map

Agent S3 (Allocation Architect), insight_v1 run, written 2026-09-27. **This is a PROVISIONAL recommendation for week 1.** The team has not approved the strategy yet, and Phases B-E may change it. Everything here is AI-generated research: tables, numbers, reasons and checklists. None of it is text to submit. The team decides and writes every word.

**Every WInS security in this file is PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading.** This year the approval rule is "Any ETF available on WInS" (see section 1), so the check is whether the ticker is actually available and tradable in the team's WInS account.

Inputs:
- `research/insight_v1/wins_now/S1_treasury_sleeve.md` (hedge, cash and ladder research)
- `research/insight_v1/wins_now/S2_growth_sleeve.md` (growth sleeve research)
- `research/insight_v1/phase_A/case_register.md` (A1)
- `research/insight_v1/phase_A/wins_week1_guardrails.md` (A4, which appeared while this file was being written; it adds the position-limit and day-trading constraints used in sections B-D and F)

Script: `research/insight_v1/scripts/S3_allocation_numbers.py`. Run it from the repo root with `.venv/bin/python research/insight_v1/scripts/S3_allocation_numbers.py`. It reproduces the verified $292,264 and 9.90y, then prints every allocation, share count, band trigger and reserve value used below.

---

## 0. Summary

1. **Starting cash is $300,000, not unknown.** I read the SMApply "Trading Details" page myself today (curl, VERIFIED-PRIMARY). It gives:
   - $300,000 of virtual cash;
   - any ETF available on WInS;
   - U.S. Treasury bonds tradable;
   - no sector minimum;
   - at most 200 trades;
   - no trade larger than twice a security's daily volume.

   The $300,000 column is therefore the one that counts. The $100k and $500k columns the task asked for are kept for scale only.
2. **The council's "~65% Treasuries / ~35% equity" mirror mislabels the plan.** In the verified model (`strategy_mc.py`), the growth sleeve is itself **60% equity / 40% bonds**. Rebuilding Laura's portfolio at 2028-01-01 from the plan's own numbers gives:
   - **hedge 65.9%** (the ladder, worth $306,077 on forwards);
   - **equity 20.4%**;
   - **sleeve bonds 13.6%** (script, section 3).

   So 65/35 is really hedge/sleeve, not bonds/equity. Once the sleeve is modelled correctly, the post-2028 mirror and a mirror consistent with the plan's total equity are **the same portfolio**. That is option (ii), and I recommend it.
3. **Recommended WInS mix at $300k, option (ii):**

   | Position | Weight | Dollars | Approx. shares at 9/25 prices |
   |---|---|---|---|
   | IEF | 23.6% | $70.7k | ~786 |
   | TLH | 42.4% | $127.3k | ~1,362 |
   | VT | 20.5% | $61.5k | ~384 |
   | VGSH (the 2031 floor proxy) | 12.5% | $37.5k | ~651 |
   | Cash | 1% | $3k | |

   - The hedge's duration is **9.90y**, the same as the ten payments.
   - The whole portfolio's duration is 6.77y.
4. **Trade sequence:**
   - **Day 1:** hedge first (IEF, then TLH), then VT.
   - **Week 2 (by Fri Oct 9):** VGSH, bought after the team formally decides the sleeve split and the 2031 floor rule. Until then its money sits in cash.
   - This gives three notes, each with a different job: the promise, growth, and the floor/discipline. The third decision is dated, and real.
   - It costs 4 trades and $100 in commissions.
   - Parking the waiting money in BIL instead does not pay: two commissions ($50) take about 14 days of BIL yield to recover.
5. **Rebalancing:**
   - **Hedge:** keep the hedge's duration at 9.90 ± 0.25y by trading IEF against TLH only.
   - **Growth sleeve:** keep VT at 55-65% of the sleeve by trading VT against VGSH only. That band is hit only by a fall of about 18.5% or a rise of about 23.8% in equities relative to bonds.
   - **Never move money between the hedge and the growth sleeve.** Never sell the hedge after a rate rise. Never trim it after a rate fall.
6. **Laura's real portfolio:**
   - Ten $50k Treasury STRIPS maturing each Nov 15 from 2032 to 2041, costing $294,387 (S1).
   - Jan 2028: the sleeve becomes 60% VT / 40% VGSH.
   - 2031: about 80% of the sleeve goes into the 2-year Treasury note that should mature on 2032-12-31. That maturity is an ASSUMPTION: the December 2025 note matured on 2027-12-31 (VERIFIED-PRIMARY).
   - From 2033: each Nov-15 rung waits about 47 days in T-bills and then pays that year's Jan 1 payment. The reserve then runs down with no rebalancing: $394.9k on 2033-01-01, $223.1k on 2038-01-01.
7. **Two platform limits to check on Day 1 (from A4's `phase_A/wins_week1_guardrails.md`).**
   - **Position limit.** This season's WInS user guide lists a per-security "Position Limit" but does not give the number. Stock-Trak's default is 25%.
   - If it is below about 43%, TLH at 42.4% is blocked. Use the ready-made capped mixes in section D.1b. The best one is IEF 22.6% / TLH 24.0% / the U.S. Treasury 3.125% due 2041-11-15 at 19.4%, with a worst twist error of $1,114. The ETF-only version is IEF 24 / TLH 24 / SPTL 14 / SPTI 4 ($2,083).
   - **Day trading is "not permitted".** Never buy and sell the same security on the same U.S. trading day.

---

## Terms used (plain English)
- **Hedge sleeve (the "promise" sleeve):** the Treasury funds that stand in for the ten fixed $50,000 payments due 2033-2042. Their value moves with the cost of those payments.
- **Growth sleeve:** everything the payments do not need. It pays for the facility contribution and for flexibility.
- **Duration:** roughly the % a bond fund's price falls if interest rates rise by 1 percentage point. The payments have a duration of 9.90 years, so they fall about 9.9% in value (as a cost) when rates rise 1 point.
- **Basis point (bp):** 0.01 percentage point.
- **Floor proxy:** in WInS, a 1-3 year Treasury fund that stands in for the "floor" Laura will buy in 2031. The floor is a 2-year Treasury note whose value in 2033 is known in advance, so she can promise it to co-sponsors.
- **Trading float:** cash kept for commissions. WInS forbids margin (borrowing), so cash must never go negative.
- **Rebalancing band:** a range around a target weight. The team trades only when a weight leaves the range.
- **STRIPS:** zero-coupon Treasuries. Each one pays a single amount on a single date.
- **Mirror:** the WInS portfolio's weights chosen to represent Laura's real plan.
- **Twist error:** how many dollars the hedge's change in value misses the change in the payments' value by, when short-term and long-term rates move 25bp in opposite directions. Uses S1's scenarios on a $292,264 hedge; smaller is better.
- **Position limit:** the most WInS lets you hold in any one security, as a share of the portfolio (set in Session Rules).

---

## 1. WInS rules that change the brief (read today)
All of these are VERIFIED-PRIMARY. I fetched https://wghsinvcomp.smapply.us/res/p/trading/ and https://wghsinvcomp.smapply.us/res/p/faqs/ with curl on 2026-09-27 and quoted them exactly. They agree with A1's register (R-W56 to R-W94).

| Rule (exact words) | What it means for this file |
|---|---|
| "Your team will begin the official trading period with $300,000 in virtual cash." | Brief section 6 ("this season's unknown") is superseded. $300k is the primary column. |
| "The $300,000 is your team's WInS simulator balance. The additional $150,000 contribution described in the Client Case Study will not be added to WInS." | WInS equals Laura's 2027 deposit. This is the strongest argument for option (iii) (section A.1). |
| "Official trading begins on September 28, 2026, and ends on November 6, 2026. When trading ends, your portfolio will be frozen" | The WInS mix on Nov 6 must match the IPS submitted the same day. |
| "Your team may make up to 200 trades during the competition." / "no more than twice a security's current daily trading volume." | Neither binds this plan. It uses 4-10 trades, and the largest order (TLH, ~1,362 shares) is 0.035% of TLH's volume cap. |
| "Exchange-Traded Funds: Any ETF available on WInS." / "Treasury Bonds: Bonds available on WInS. The list includes Treasury bonds from the United States, United Kingdom, Germany, France, Italy, and the Netherlands." | Availability in WInS is the approval test. Individual U.S. Treasuries are allowed (section D.3). |
| "There is no required sector allocation or minimum number of sectors." | The sector-fund fallback (section D.2) is a contingency only. CLAUDE.md and brief sections 6 and 9 still carry the old third-party claim. |
| "Each stock transaction is charged a flat $25 commission and treasury bonds are charged $10." | ASSUMPTION: an ETF trade counts as a "stock transaction" ($25). |
| "Orders placed while the market is closed are filled at the security's opening price when the market reopens." / "International equity orders … are processed at the end of the applicable trading day." | All picks are U.S.-listed, so they fill at real-time or opening prices. From Australia, daytime orders fill at the next U.S. open. |
| "The bond prices are updated once daily at U.S. market open" | Individual Treasuries in WInS show stale prices during the day. This is one reason ETFs are the primary hedge. |
| "If you make an error, we encourage you to run with it and not scramble to 'fix' it." | Record errors honestly in the decision log. Do not trade to undo them. |
| 2026-27 WInS User Guide p.6 (A4, VERIFIED-PRIMARY): "Position Limit: This is how much of your portfolio you can invest in one single stock. Day Trading: This is not permitted." Stock-Trak's generic FAQ: "The default position limit is 25%" | The limit's value is UNKNOWN. The 2024-25 screenshot showed a bond limit of 100% [PRIOR]. Read Session Rules before the first order. Under a 25% limit only TLH (42.4%) breaks: use section D.1b. Never buy and sell the same security on the same day. |
| Stock-Trak blog (2017, A4): students "cannot edit or delete their trade notes" | Treat every note as permanent. Write it before pressing submit. |

---

## A. WInS week-1 allocation

### A.1 The decision the team must make: what the $300k represents

Plan numbers at 2028-01-01 come from the script (section 3):
- The ladder is worth $306,077 on today's forward curve (ASSUMPTION: forwards are realised).
- The sleeve is ($300,000 - ladder cost) × (1 + JPM sleeve return) + $150,000.
- **At 60% sleeve equity:** hedge 65.9%, equity 20.4%, sleeve bonds 13.6%.
- **At 50% / 70% sleeve equity:** equity 17.0% / 23.9%.
- With the Nov-15 STRIPS ladder the hedge share is 66.2%.

| | (i) Brief's post-2028 mirror as written | **(ii) Post-2028 mirror built from the plan (recommended)** | (iii) Literal Jan-2027 book |
|---|---|---|---|
| Hedge (IEF/TLH, 9.90y) | 65% | **66%** | ~97.5% |
| Equity (VT) | 34% | **20.5%** | ~1.5% |
| Sleeve bonds (VGSH, 2031 floor proxy) | 0% | **12.5%** | ~0% |
| Cash float | 1% | 1% | 1% |
| VT at $300k | $102,000 | **$61,500** | ~$4,500 |
| Portfolio duration | 6.43y | 6.77y | 9.65y |
| Matches the plan's total equity (17-24%)? | No: 34% is a risk level the plan never holds | **Yes** (20.4% at 60/40) | No: that is the 2027 level only (~1-2%) |
| What the WInS portfolio shows | Promise + growth | **Promise + growth + a bought floor: three funding purposes** | Promise only. Growth is a ~$4.5k token trade |
| Strongest argument for it | Largest visible growth sleeve | Same proportions as the model and the planned IPS | WInS cash = the 2027 deposit, and "$150,000 … will not be added to WInS" (VERIFIED-PRIMARY) |
| Main weakness | Contradicts the IPS/model numbers, and judges read the notes and the IPS together | Needs one sentence saying WInS holds the target mix after both deposits, scaled to $300k | Describes 1 of the 6 pre-2033 years; the growth note would be token. Under a 25% position limit, 97.5% of Treasuries would need at least 4-5 positions |

**Recommendation: (ii).** Reasons, each tied to the case or to Trading Notes quality:
1. **It is the council's post-2028 mirror with the sleeve modelled correctly.** It follows the task's default and removes the brief's 35%-vs-20-24% inconsistency (brief section 9) with a computed number instead of a compromise.
2. **Case:** she wants "an appropriate balance between pursuing growth and protecting the capital required for her goals" (case p.2, VERIFIED-REPO-FILE).
   - Option (ii) shows the balance the plan actually holds from 2028 to 2032, which is 5 of the 6 years before 2033.
   - Option (iii) shows only 2027. Option (i) overstates her risk.
3. **Trading Notes guide:** decisions should show the team's "approach to growth, risk, liquidity, funding reliability, financial flexibility, and future cash-flow needs". They should also "demonstrate how your team used individual investments as part of a cohesive portfolio strategy".
   - Three positions with three jobs give three different, non-redundant notes.
   - SMApply lists "funding purposes" as a kind of diversification (R-W71, VERIFIED-PRIMARY). The promise, the growth sleeve and the floor are three funding purposes.
4. **IPS consistency requirement.** The Trading Notes guide says the analysis "should be consistent with the strategic approach your team is developing and will later articulate in its IPS". The case says "Evaluators will consider the three deliverables together". The WInS portfolio freezes on Nov 6, the day the IPS is due (R-W58).
   - So the weights frozen in WInS, the percentages in the IPS, and the model's inputs must be one set of numbers.
   - Under (ii), that set is "about two-thirds matched Treasuries; a growth sleeve of about 60% global stocks and 40% short Treasuries".
   - Under (i), the IPS would have to say 35% equity, which the model does not support.
5. **Honest counter-argument, which the team should weigh:** WInS holds exactly $300k, and Wharton says the $150k is not added. A reader could therefore take WInS as "the 2027 portfolio".
   - If the team picks (iii), the hedge note stays strong, but the growth and floor notes become weak or disappear.
   - Choose (iii) only if the team would rather be literal than show the whole strategy.
   - Whatever the team picks, the IPS or the Final Report must say in one sentence what the WInS portfolio represents. The team writes that sentence.

### A.2 Recommended allocation, option (ii)
All weights and share counts come from the script. Share counts use the 2026-09-25 closing prices: IEF $90.00, TLH $93.38, VT $160.03, VGSH $57.59, BIL $91.58 (9/24). **Recompute them on the trade date.**

| Position | Role in the strategy | Weight | $100k | **$300k (actual)** | $500k | Alternates (same instrument type; PENDING APPROVAL CHECK) | 2025-26 list |
|---|---|---|---|---|---|---|---|
| **IEF** iShares 7-10 Year Treasury Bond ETF (PENDING APPROVAL CHECK) | Operating-commitment hedge, part 1: owns notes maturing Aug-2033 to May-2036, the first payment years | **23.6%** (35.7% of hedge) | $23,581 (~262 sh) | **$70,744 (~786 sh)** | $117,907 (~1,310 sh) | If TLH is missing: IEF 41.0% + TLT 25.0% ($122,958 / $75,042). Or SPTI 27.9% + SPTL 38.1%, or VGIT 27.7% + VGLT 38.3% | IEF yes (#88, line 1053) |
| **TLH** iShares 10-20 Year Treasury Bond ETF (PENDING APPROVAL CHECK) | Operating-commitment hedge, part 2: owns bonds maturing Feb-2037 to May-2046, covering the later payments | **42.4%** (64.3% of hedge) | $42,419 (~454 sh) | **$127,256 (~1,362 sh)** | $212,093 (~2,271 sh) | TLT (as above; wider twist error, $3,619 vs $1,352); SPTL; VGLT | **TLH no**; TLT yes (#87, line 1041) |
| **VT** Vanguard Total World Stock ETF (PENDING APPROVAL CHECK) | Growth: money the payments do not need; funds the facility contribution and flexibility | **20.5%** (60% of the sleeve) | $20,500 (~128 sh) | **$61,500 (~384 sh)** | $102,500 (~640 sh) | VTI 12.7% + VXUS 7.8% ($38,130 / $23,370); ITOT + IXUS in the same split | VT yes (#23, line 273); VTI yes (#22, line 261); VXUS yes (#51, line 603); ITOT/IXUS no |
| **VGSH** Vanguard Short-Term Treasury ETF (PENDING APPROVAL CHECK), **bought in week 2** | 2031 floor proxy: the safe part of the growth sleeve, the money Laura will turn into a promised floor two years before 2033 | **12.5%** (40% of the sleeve, less the float) | $12,500 (~217 sh) | **$37,500 (~651 sh)** | $62,500 (~1,085 sh) | SHY (0.15%, 1.79y). Or a WInS-listed ~2-year U.S. Treasury note, e.g. CUSIP 91282CRP8, 4.75%, due 2028-09-30 (exists: VERIFIED-PRIMARY; listed in WInS: UNVERIFIED; $10 commission) | VGSH yes (#93, line 1113; 0.04% then); SHY yes (#86, line 1029) |
| **Cash** | Trading float for commissions (no margin allowed). Also where ETF distributions land (~$825/month from the hedge, ASSUMPTION ~5% yield) | **1%** | $1,000 | **$3,000** | $5,000 | BIL, only if money must wait more than about 2-3 weeks (section B.1); alternates SGOV, SHV | BIL yes (#92, line 1101); SGOV no; SHV yes (#90, line 1077) |
| **Total** | | 100% | | | | | |

**Position-limit check.** TLH at 42.4% is the only position above 25%. If Session Rules show a single-security limit below about 43%, do not trade this table. Use section D.1b instead: the hedge's share and duration stay the same, and only its split changes.

Key facts, all issuer primary pages accessed 2026-09-27. "S3" means I read the page myself today (curl). S1/S2 read the same pages today.

| Fund | Expense ratio | Duration | Holdings / index | Size and liquidity | Source, status |
|---|---|---|---|---|---|
| IEF | 0.15% | 6.86y effective (9/24) | 16 Treasury notes maturing 2033-2036 (ICE U.S. Treasury 7-10 Year) | Net assets $41.57bn (9/25); 30-day average volume 8,830,020 shares; median bid/ask spread 0.01%; 30-day SEC yield 4.84% | ishares.com/us/products/239456, VERIFIED-PRIMARY (S3; S1 for maturities) |
| TLH | 0.15% | 11.59y (9/24) | 61 bonds maturing 2037-2046 (ICE U.S. Treasury 10-20 Year) | $10.53bn; 1,969,419 shares/day; spread 0.01%; SEC yield 5.29% | ishares.com/us/products/239453, VERIFIED-PRIMARY (S3; S1) |
| TLT (alternate) | 0.15% | 14.88y (9/24) | 47 bonds maturing 2044-2056 | $45.75bn; 35,945,818 shares/day | ishares.com/us/products/239454, VERIFIED-PRIMARY (S3) |
| VT | 0.06% (as of 2026-02-27) | n/a | 10,088 stocks (8/31); FTSE Global All Cap Index; 37.7% non-U.S. (8/31); top-10 holdings 21.7% (fact sheet 6/30, S2) | ETF share class $81.9bn (8/31); market price $160.03 (9/25); **Vanguard does not publish volume** (UNVERIFIED; check in WInS) | investor.vanguard.com data API, VERIFIED-PRIMARY (S3); top-10 from S2 |
| VGSH | 0.03% (as of 2025-12-19) | 1.9y (8/31) | 92 Treasury bonds (Bloomberg U.S. 1-3 Year Treasury Index) | ETF share class $34.8bn (8/31); SEC yield 4.55% (9/24); price $57.59 (9/25); volume not published | investor.vanguard.com data API, VERIFIED-PRIMARY (S3) |
| SHY (alternate) | 0.15% | 1.79y (9/24) | 91 notes | $26.18bn; 4,892,873 shares/day; SEC yield 4.43% | ishares.com/us/products/239452, VERIFIED-PRIMARY (S3) |
| BIL (optional) | 0.1353% gross | 0.10y option-adjusted (9/24) | 33 T-bills | AUM $47.92bn (9/24); prior-day exchange volume 745,610 shares; closing price $91.58. **The page now reads "State Street SPDR Bloomberg 1-3 Month T-Bill ETF"**, a name change to watch for when searching WInS | ssga.com, VERIFIED-PRIMARY (S3) |
| SGOV (alternate) | 0.09% | 0.11y (9/24) | 0-3 month T-bills | $111.78bn; 22,532,914 shares/day | ishares.com/us/products/314116, VERIFIED-PRIMARY (S3) |

### A.3 Duration of the hedge sleeve, and what the hedge does in WInS
- **Hedge duration: 9.90y.** 0.357 × 6.86 + 0.643 × 11.59 = 9.90. This equals the ten payments' duration at 2027-01-01 (verified script; reproduced).
  - Formula for the weights: TLH weight = (9.90 - D_IEF) / (D_TLH - D_IEF), using the issuer durations on the day of the trade.
- **Why 9.90 and not 8.92.** Valued at 2028-01-01, the same payments have a duration of 8.92y (script). That would give IEF 56.5% / TLH 43.5%.
  - I recommend 9.90. During WInS (Sept-Nov 2026), the hedge's job is to track the cost of the ladder Laura buys on 2027-01-01. The sensitivity of that forward cost is 9.90 (ASSUMPTION: this reading of the WInS hedge's job).
  - The hedge's size (66%) comes from the post-2028 proportions. Its duration comes from the payments as they stand today.
  - **The team must state one anchor and keep it.** Mixing 9.90 in one note with 8.92 in another would be an inconsistency a judge could spot.
- **Expect WInS losses when rates rise, and do not react.** The hedge is $198k at a 9.90y duration (first-order estimate):
  - +50bp: about **-$9,801**;
  - +100bp: about **-$19,602**;
  - -100bp: about +$19,602.

  In each case, the cost of Laura's payments moves by about the same percentage the same way. For example, +100bp lowers the payments' cost by $27,373 (S1). Judged against the payments, the hedge is close to risk-free. Judged in dollars alone, it is not. **The notes must never call the hedge "stable" or "low-volatility" on its own terms.**
- **Twist risk (S1, VERIFIED-PRIMARY inputs):** under a 50bp curve twist, IEF/TLH misses the payments by at most $1,352, against $3,619 for IEF/TLT. This is why TLH is the second fund when WInS offers it.

### A.4 Options (i) and (iii) in dollars (only if the team rejects (ii))
| Cash | (i) IEF / TLH / VT / cash | (iii) IEF / TLH / VT / cash |
|---|---|---|
| $100k | $23,224 / $41,776 / $34,000 / $1,000 | $34,836 / $62,664 / $1,500 / $1,000 |
| **$300k** | **$69,672 (~774 sh) / $125,328 (~1,342 sh) / $102,000 (~637 sh) / $3,000** | **$104,508 (~1,161 sh) / $187,992 (~2,013 sh) / $4,500 (~28 sh) / $3,000** |
| $500k | $116,121 / $208,879 / $170,000 / $5,000 | $174,181 / $313,319 / $7,500 / $5,000 |

---

## B. First-week trade sequence

### B.1 Calendar
Times are U.S. Eastern (ET). The U.S. market opens at 9:30 a.m. ET:
- 11:30 p.m. AEST on the same date until Sat Oct 3;
- 12:30 a.m. AEDT (next date) from Sun Oct 4, when NSW and Victoria start daylight saving. Queensland does not change.

These time-zone details are an ASSUMPTION: the team's state is not recorded. Orders entered during the Australian daytime fill at the next U.S. opening price (VERIFIED-PRIMARY).

| Step | When | Trade | Size ($300k) | Why this order | Cost |
|---|---|---|---|---|---|
| 0 | Before any order (Mon Sep 28, Australian daytime) | None. Run the compliance checks (section F.2), starting with **Session Rules** (position limit, day trading). The team formally chooses option (i), (ii) or (iii) and records who decided. If the position limit is below about 43%, switch to section D.1b now. | none | Last year's lesson was trading outside the rules. Also, the strategy is not yet approved. | $0 |
| 1 | Day 1 (orders fill at the Mon Sep 28 ET open) | **BUY IEF** | 23.6%, ~786 sh | The promise comes first: protect the payments before taking any risk (the lock-early logic). The hedge is a no-regret trade: it is ≥65% under all three options. | $25 |
| 2 | Day 1 | **BUY TLH** | 42.4%, ~1,362 sh | Second half of the hedge. Recompute both weights from the issuer pages that morning. | $25 |
| 3 | Day 1, only after step 0 picked (ii) or (i) | **BUY VT** | 20.5%, ~384 sh (34% under (i)) | Risk is taken only with money the promise does not need. Its size depends on the option chosen, so it follows the decision. | $25 |
| (hold) | Days 1-10 | Keep the floor-proxy money (12.5%, $37.5k) **in cash** | none | The 2031 rule and the sleeve split (50/60/70) are open team decisions (brief section 9). | $0 |
| 4 | Week 2, target by **Fri Oct 9** (roster day), after a recorded team decision | **BUY VGSH** | 12.5%, ~651 sh | This is the planned third decision: the team buys the floor proxy only once it has agreed the rule behind it. | $25 |
| 5 | Weekly check (same weekday each week) | Only if a band in section C is breached | as needed | Rules decide trades, not reactions. | $25 per leg |
| 6 | Week 4 (Oct 19-23) | Duration refresh: recompute IEF/TLH weights. **Trade only if** the hedge's duration is outside 9.90 ± 0.25y | usually none | Tests the "recompute every time" rule. | $0-50 |
| Oct 23 | Trading Notes due | Choose the best 3 of the executed trades | | | |
| Nov 6 | IPS due; WInS freezes | No "tidy-up" trades in the last days | | The frozen mix must be the mix the IPS describes | |

Notes on the calendar:
- Trades 1-4 use 4 of the 200 trades and cost $100. Under the D.1b capped hedge, add 1-2 trades ($10-50).
- **No day trading.** No step buys and sells the same security on the same U.S. trading day. A rebalance always trades two *different* securities (VT against VGSH, or IEF against TLH). If a mistake happens, wait at least one trading day before any correcting trade, and run with it where possible (R-W94).
- **Cash vs BIL for the waiting money:** a round trip in BIL costs $50 in commissions. $37,500 earns about $3.69 a day at BIL's 3.59% SEC yield (S1), so BIL breaks even only after about 14 days.
  - For a 1-2 week wait, cash is simpler and at least as good. ASSUMPTION: WInS pays no interest on cash (UNVERIFIED; check in WInS).
  - Use BIL only if the decision will take longer than about 3 weeks.
- If the team cannot decide the sleeve split by Oct 9, buy VGSH at the provisional 60/40 anyway. The team already accepted 60% as a provisional call (CLAUDE.md, interview part 2). Record the call as provisional.
- **Do not create a decision just to get a note.** If the team has already decided everything on Day 1, buy VGSH on Day 1. The third note then has to come from a genuine band trade or the duration refresh, and neither is guaranteed.

### B.2 The three note trades: what the WInS note must contain, and what could go wrong
The WInS note is quoted "exactly as it appears in WInS", and "Yes, we will verify this" (Trading Notes guide p.2). Write it at the moment of the trade (R-W82). Straight after submitting, copy it word for word into the team's decision log. The checklists below list elements only. The team writes the words.

**Note 1: hedge purchase (TLH, trade 2).** The IEF note can be short and point to the pair.
- [ ] Action, ticker and rough share of the portfolio, and that TLH is one half of a pair with IEF.
- [ ] The job: stand in for the ten fixed $50,000 payments due 2033-2042 ("the promise"), funded by the portfolio "with a high degree of certainty" (case).
- [ ] Why this fund: its bonds mature 2037-2046, IEF's mature 2033-2036, and the payments fall 2033-2042. Say "moves like the cost of the payments when rates change", not "DV01".
- [ ] Why now: the promise before any risk, in the plain words of the plan.
- [ ] The risk accepted: the price falls when rates rise, but the payments' cost falls too. So it is not "stable" on its own. Avoid copying the guide example's phrase "reduce portfolio volatility".
- [ ] The rule the team commits to: recompute the weights from issuer durations, and never sell after a rate rise.
- [ ] At most one number, and a verified one (e.g. duration about 9.9 years).

What could go wrong:
- **Position limit below about 43%.** WInS rejects the TLH order. Switch to section D.1b before ordering, not after a rejection.
  - The note then describes a three-part hedge. If the U.S. Treasury 2041 bond is used, name it as the bond that matures just before Laura's last payment.
- **TLH not tradable in WInS.** Use IEF 62.1% / TLT 37.9% of the hedge (both were on the 2025-26 list). Say in the note that it misses a 50bp twist by up to $3.6k.
  - Under a 25% limit this pair also breaks (IEF would be 41.0%). Use D.1b row 3 instead.
- **Stale weights.** The IEF/TLT match moved 2.7 points of weight between the June fact sheets and today (S1). Always re-read the issuer page first.
- **Rates rise in WInS** (+50bp is about -$9.8k). Someone will want to sell. The pre-committed rule in the note is the defence.
- **Order entered overnight** fills at the next open, which may gap. This does not matter for the reasoning.
- **Typing error in quantity.** Run with it (R-W94) and record it as learning.
- **Volume cap.** Not a real risk: 1,362 shares against a cap of about 3.9 million.

**Note 2: growth purchase (VT, trade 3).**
- [ ] Action, ticker and share of the portfolio (about a fifth), described as 60% of the growth sleeve.
- [ ] The job: money the ten payments do not need. It serves the facility contribution and flexibility (case p.3).
- [ ] Why this size: it matches the plan's equity after 2028 (about 20% of the total), not a higher number. This is the link to the IPS.
- [ ] Why one global fund: 10,088 stocks, 0.06% fee, top-10 holdings 21.7% against 38.8% for the S&P 500 (S2). This is a concentration argument, not a return forecast.
- [ ] The risk accepted: a stock-market fall shrinks the facility range, never the payments. The honest caveat is that AI-chip exposure remains through TSMC and Korea (S2).
- [ ] What the team will not do: sell on a fall, or add a Taiwan tilt (S2: that would be tokenism and an AI bet).

What could go wrong:
- **VT unavailable.** Use VTI 62% + VXUS 38% of the equity (both were on the 2025-26 list). The note must then explain two funds.
- **Buying just before a fall.** WInS shows a loss. That is not judged (R-W75), so do not sell.
- **The team later picks 50% or 70% sleeve equity.** Resize VT in the week-2 decision and give the reason.
- **Mismatch with the model.** If VT is kept, `strategy_mc.py` should use AC World (7.00% / 16.78%) instead of U.S. large cap (S2) so the model and the IPS match.

**Note 3: discipline trade (VGSH floor-proxy purchase, trade 4).**
- [ ] Action, ticker and share of the portfolio (about an eighth); the safe 40% of the growth sleeve.
- [ ] The decision that triggered it, with a date: the team agreed the sleeve split and the 2031 rule. Name the rule in a few words (e.g. "about 80% of the sleeve locked two years before 2033").
- [ ] Why this instrument: 1-3 year Treasuries (duration 1.9y) behave like the 2-year note the floor will be.
- [ ] Link to the case: in 2031 Laura gives co-sponsors a range. The case says: "If Laura promises more than she can ultimately contribute, she could damage her credibility" (case p.3, VERIFIED-REPO-FILE). A floor that is already owned cannot be promised beyond what exists.
- [ ] Why it was not bought on Day 1: the team would not buy it before agreeing the rule. This is the process evidence (Articulation criterion).
- [ ] The risk accepted: lower expected return than equities.

What could go wrong:
- **The team disagrees.** Do not trade for the sake of a note. Keep the money in cash and record the disagreement as an Articulation item.
- **VGSH unavailable.** Use SHY, or a WInS-listed 2-year U.S. Treasury note ($10 commission, prices update once a day, coupons twice a year).
- **Wording.** The note reads as market timing if it gives a rate forecast as the reason. The reason must be the team's rule.

**Back-up notes (only if they really happen):**
- A **band rebalance** (VT against VGSH back to 60/40). The note needs: the band, the move that breached it, that the hedge was not touched, and that the rule was set in advance.
- A **duration refresh** (IEF against TLH). The note needs: the issuer durations on the day, the gap from 9.90, and that the trade restores the match rather than betting on rates.
- A **"we did not chase"** decision produces no WInS note. Log it for the Final Report instead.

---

## C. Rebalancing rule for WInS

| What | Target | Band (trade only outside it) | How to fix | Check frequency |
|---|---|---|---|---|
| Hedge's internal duration | 9.90y (payments at 2027-01-01) | 9.65-10.15y | Trade IEF against TLH only, back to the formula weights | Each weekly check, from issuer pages. A 0.25y gap on $198k is about $495 per 100bp |
| Hedge vs growth sleeve | Hedge sized once at purchase; afterwards its value moves with the payments | **No band.** The hedge's share rises when rates fall because the payments cost more, and that is correct | Never trade across the two sleeves during WInS | n/a |
| Inside the growth sleeve | VT 60% / VGSH 40% | VT at 55-65% of VT + VGSH (inside the team's 50-70% policy range) | Trade VT against VGSH only, back to 60/40 | Weekly. It triggers only if equities move about **-18.5%** or **+23.8%** relative to bonds, so expect no trade in six weeks |
| Cash float | about 1% | at least $1,000; at most about 2% | Excess from distributions goes to VGSH, only if more than 2% | Weekly |

The worked trigger sizes come from the script. The duration drifts are illustrations:
- If rates rise so that the durations become IEF 6.82 / TLH 11.40 (ASSUMPTION), the unrebalanced hedge measures 9.76y. That is inside the band, so there is no trade.
- If they become IEF 6.90 / TLH 11.78, it measures 10.04y. Also no trade.
- A band trade in six weeks would need a large move. That is fine: the rule exists so that the team does not trade on noise.

**What never to do:**
1. **Sell hedge to buy equity after a rally**, or to "buy the dip". The hedge belongs to the payments and is not a source of funds.
2. **Sell the hedge after a rate rise** because WInS shows a loss. The payments got cheaper by about the same amount.
3. **Trim the hedge after a rate fall** because it "grew too big". It grew because the payments cost more.
4. **Lengthen duration to bet on rates.** Examples: swapping into TLT alone, EDV/GOVZ/ZROZ (24-28y), or foreign government bonds. WInS allows U.K., German and other government bonds, but their currency risk does not match a USD liability.
5. **Add thematic, leveraged, inverse or single-country funds** (ARKK/MSOS-type, EWT). INTERPRETATION: leveraged and inverse ETFs are still "ETFs", so the FAQ's ban on "Derivatives" may not cover them. They fail the brief's "no leverage, inverse or thematic bets" rule either way.
6. **Trade for ranking, or trade in the last days before the Nov 6 freeze** to make the portfolio look better.
7. **Write or edit a note after the fact**, or reuse practice-account trades (they were reset, R-W77).
8. **Let the advisor place trades** (R-W87). Let cash go negative (no margin).
9. **Day-trade.** Never buy and sell the same security on the same U.S. trading day ("Day Trading: This is not permitted", 2026-27 WInS guide, via A4). Never push any position above the Session Rules position limit.
10. **Re-weight to the June fact-sheet numbers** (64.8/35.2). Use today's issuer durations.

---

## D. Substitutes if a pick is disallowed, and the sector-fund fallback

### D.1 Substitution table (every line PENDING APPROVAL CHECK)
| If this fails the WInS check | First substitute (weights of total at $300k) | Second substitute | What changes in the story | 2025-26 list |
|---|---|---|---|---|
| TLH | IEF 41.0% + TLT 25.0% ($122,958 / $75,042), duration 9.90y | SPTI 27.9% + SPTL 38.1%, or VGIT 27.7% + VGLT 38.3% (0.03% fees) | The pair now owns 20-30y bonds the payments do not need. Worst 50bp twist error $3,619 (S1) | TLT yes; SPTI/SPTL/VGIT/VGLT no |
| IEF (unlikely) | SPTI + SPTL, or VGIT + VGLT (as above) | IBTR 42.2% / TLH 57.8% of the hedge (best twist error, $1,176). But IBTR holds only $34m (S1) | Adds a thin fund | none of these |
| VT | VTI 12.7% + VXUS 7.8% | ITOT + IXUS in the same 62/38 split | Two funds; allows a U.S./international band | VTI, VXUS yes; ITOT/IXUS no |
| VGSH | SHY 12.5% (0.15%, 1.79y) | A WInS-listed ~2-year U.S. Treasury note | A literal floor instrument, but its price updates only once a day | SHY yes |
| BIL (if used) | SGOV | SHV, or plain cash | none | SGOV no; SHV yes |
| Treasury ETFs as a class (very unlikely) | A literal ladder of U.S. Treasuries from the WInS bond list (D.3) | none | Most literal; 10 trades at $10 each | n/a |

### D.1b If Session Rules cap a single security below about 43%
The hedge's share (66%) and duration (9.90y) do not change. Only its split does.
- **Source of the cap:** Stock-Trak's default is 25% (A4, generic platform page). This season's value is UNKNOWN.
- **Working cap of 24%:** each capped fund is held at 24% of the total, leaving a 1-point buffer. ASSUMPTION: the limit is checked at the fill price.
- **Method:** script section 9, using S1's holdings-based model and the same scenarios as S1. For comparison, the uncapped IEF/TLH mix has a worst twist error of $1,352.
- Every line is PENDING APPROVAL CHECK.

| Use when | Mix (share of total portfolio) | Duration | Worst 50bp twist | ±100bp worst | Notes |
|---|---|---|---|---|---|
| **1. The WInS bond list includes the 3.125% U.S. Treasury due 2041-11-15 and bonds have their own higher limit** (the 2024-25 screenshot showed 100% [PRIOR]) | IEF 22.6% / TLH 24.0% / **UST 3.125% 2041-11-15 (CUSIP 912810QT8) 19.4%** | 9.90y | **$1,114** | $693 | Better than uncapped IEF/TLH. The bond's principal STRIP is Laura's last rung (S1), so it gives a literal story. Model duration 11.35y and price 77.88 per 100 face are model values; use the WInS quote. $10 commission. Prices update once a day. Pays coupons (R-W91) |
| **2. ETFs only** | IEF 24.0% / TLH 24.0% / SPTL 14.0% / SPTI 4.0% | 9.90y | $2,083 | $899 | All liquid (SPTI/SPTL about $10bn each, S1). SPTI/SPTL were not on the 2025-26 list. VGLT/VGIT are equivalent alternates |
| 3. TLH also missing | SPTI 14.0% / SPTL 19.0% / VGIT 13.8% / VGLT 19.2% | 9.90y | $3,833 | $972 | Each pair is split across two issuers so every position is under the cap. Fees 0.03% |
| (not recommended) | IEF 24.1% / TLH 25.0% / IBGA 16.9% | 9.90y | $1,468 | $1,043 | IBGA (iBonds Dec 2044) holds only $73.7m. Only 9,537 shares traded on 2026-09-25, against a 30-day average of 84,912 (ishares.com, VERIFIED-PRIMARY). The order would be about 2,200 shares, so the WInS volume cap could bite early in the day |

### D.2 Sector-minimum fallback (contingency only)
SMApply says: "There is no required sector allocation or minimum number of sectors" (VERIFIED-PRIMARY today). Use this only if Wharton later says otherwise or WInS rejects broad ETFs.
- Replace VT with **11 Select Sector SPDRs at S&P 500 weights for the U.S. 62%, plus VXUS for the non-U.S. 38%**. VXUS keeps the global argument.
- Weights come from S2 (SPYM holdings 2026-09-24). Fees are 0.08% gross (S2, VERIFIED-PRIMARY). All tickers PENDING APPROVAL CHECK.

| Fund | Sector | Share of U.S. part | $ at $300k | 2025-26 list |
|---|---|---|---|---|
| XLK | Information Technology | 39% | $14,871 | yes (#57, line 685) |
| XLF | Financials | 12% | $4,576 | yes (#34, line 403) |
| XLC | Communication Services | 10% | $3,813 | yes (#31, line 367) |
| XLV | Health Care | 9% | $3,432 | yes (#35, line 415) |
| XLY | Consumer Discretionary | 9% | $3,432 | yes (#53, line 627) |
| XLI | Industrials | 8% | $3,050 | yes (#36, line 427) |
| XLP | Consumer Staples | 4% | $1,525 | yes (#32, line 379) |
| XLE | Energy | 3% | $1,144 | yes (#33, line 391) |
| XLU | Utilities | 2% | $763 | yes (#17, line 201) |
| XLB | Materials | 2% | $763 | yes (#52, line 615) |
| XLRE (or VNQ) | Real Estate | 2% | $763 | XLRE no; VNQ yes (#21, line 249) |
| VXUS | All non-U.S. | (38% of equity) | $23,370 | yes (#51, line 603) |

Costs of the fallback:
- 12 buys × $25 = $300. On the smallest positions, the commission is 3.3% of the position.
- Sector capping makes the mix differ from the market: active share 13.5%, and an AI basket of 29.7% against 40.7% (S2). The team would have to disclose that.
- It uses up to 12 of the 200 trades per rebalance.
- The hedge is unchanged. How WInS classifies Treasury ETFs by sector is UNVERIFIED.

### D.3 Individual U.S. Treasuries in WInS (an option to check, not the week-1 plan)
- **The rule allows them.** WInS allows "Treasury Bonds: Bonds available on WInS", chosen from a drop-down, at $10 per trade.
- **What it would give:** if the list includes notes or bonds maturing each Nov 15 from 2032 to 2041, the team could hold a literal scaled ladder. That is the most faithful picture of the real plan.
- **Why it is not the primary:**
  - availability is unknown;
  - prices update once a day;
  - they are coupon bonds, not STRIPS, so the match is approximate;
  - 10 trades and 10 notes for one idea;
  - Wharton's own example note uses a Treasury ETF.
- **Check the drop-down on Day 1** and record what exists. It could support one "tested the strategy" note later, but only if the team wants it.
- **Exception:** if a position limit blocks TLH, a single bond (the 3.125% due 2041-11-15) is the best fix (D.1b row 1). One bond in a three-part hedge is simple enough to earn its place. A ten-bond ladder is not.

---

## E. Laura's long-term portfolio instrument map (not WInS)

### E.1 Stages
| Date (start of year) | Money | Instruments | Rule |
|---|---|---|---|
| Jan 2027 | $300,000 | Ten Treasury STRIPS, $50k face each (E.2), ~$294,387. The ~$5.6k left over goes into a T-bill fund (SGOV/BIL) as the buffer for dealer mark-ups | If rates fall first and the ladder costs more than $300k, buy the longest rungs first and the rest from the 2028 deposit (brief section 7) |
| Jan 2028 | +$150,000 | Growth sleeve (~$158k): **60% VT / 40% VGSH** (E.3) | Rebalance once a year to 60/40, band 55-65 |
| Jan 2031 | Sleeve (model median floor ~$150k when bought) | **About 80% of the sleeve into a 2-year Treasury note maturing 2032-12-31** (E.4); the other 20% stays 60/40 | The floor is bought, not forecast (brief section 8 item 7) |
| Jan 2033 | Ladder market value $394,930 (forwards) + floor + remaining sleeve | Operating reserve = the STRIPS ladder (E.5). The floor matures into cash for the facility decision | Payments come from maturing rungs only |
| 2033-2042 | Reserve runs down | Each Nov-15 rung waits about 47 days in T-bills, then pays Jan 1 | No rebalancing; nothing is sold early |

### E.2 The January 2027 ladder, rung by rung
Source: S1, from Treasury MSPD Table V (record date 2026-08-31, VERIFIED-PRIMARY). Costs are valued at 2027-01-01 on the 2026-09-25 curve (model, ASSUMPTION: STRIPS price on the par-derived zero curve). STRIPS are bought "only through a financial institution, a broker, or dealer" in $100 multiples (TreasuryDirect, VERIFIED-PRIMARY per S1).

| Pays the payment on | Rung matures | Instrument | Cost at 2027-01-01 | Alternate |
|---|---|---|---|---|
| Jan 1 2033 | Nov 15 2032 | Principal STRIP 912821KC8 | $37,253 | IBTM (iBonds Dec 2032) ~$37,218 |
| Jan 1 2034 | Nov 15 2033 | Principal STRIP 912821NP6 | $35,336 | IBTO ~$35,346 |
| Jan 1 2035 | Nov 15 2034 | Principal STRIP 912821QX6 | $33,495 | IBTP ~$33,550 |
| Jan 1 2036 | Nov 15 2035 | Principal STRIP 912821TF2 | $31,720 | IBTQ ~$31,826 |
| Jan 1 2037 | Nov 15 2036 | Interest STRIP due 11/15/2036. CUSIP not in Table V: get a broker quote. Or the principal STRIP of the Nov-2026 10-year note, if issued (ASSUMPTION) | $30,007 | IBTR ~$30,227 ($34m fund); May 15 2036 principal 912821UK9 $30,861 |
| Jan 1 2038 | Nov 15 2037 | Interest STRIP due 11/15/2037 | $28,362 | May 15 2037 principal 912803DA8 ($504m stripped) $29,183 |
| Jan 1 2039 | Nov 15 2038 | Interest STRIP due 11/15/2038 | $26,779 | May 15 2038 principal 912803DD2 ($559m) $27,569 |
| Jan 1 2040 | Nov 15 2039 | Principal STRIP 912803DJ9 | $25,257 | Aug 15 2039 912803DH3 $25,635 |
| Jan 1 2041 | Nov 15 2040 | Principal STRIP 912803DP5 | $23,791 | 912803FU2 (same date) |
| Jan 1 2042 | Nov 15 2041 | Principal STRIP 912803DU4 | $22,387 | 912803GD9 (same date) |
| **Total** | | | **$294,387** | Exact-date value $292,264; headroom under $300k is **~$5.6k (~19bp)**, not $7.7k (S1) |

### E.3 Growth sleeve funds and weights (from Jan 2028)
| Part | Primary (PENDING APPROVAL CHECK if also used in WInS) | Weight in sleeve | About $ at Jan 2028 | Alternates | Model input to use |
|---|---|---|---|---|---|
| Equity | VT (0.06%) | 60% | ~$95k | VTI + VXUS 62/38; ITOT + IXUS | JPM AC World 7.00% compound / 16.78% volatility (not U.S. large cap 6.70%; S2) |
| Short Treasuries (2031 floor feedstock) | VGSH (0.03%, 1.9y) | 40% | ~$63k | SHY; a 2-year note ladder | JPM gives no pure short-Treasury line: cash 3.10%, intermediate Treasuries 4.00%, short-duration government/credit 4.00% (includes credit). The model's 4.00% is slightly generous for 1-3y Treasuries (ASSUMPTION: ~3.5-3.9%); the effect is under $1k on the median by 2031 |

The equity share (50/60/70%) is still the team's weakest call. 60% is provisional (CLAUDE.md).

### E.4 The 2031 floor instrument
- **Primary: a 2-year U.S. Treasury note maturing 2032-12-31.** It would be bought at the December 2030 auction, or in the market in early January 2031. It pays fixed interest every six months and is sold in $100 steps, with no fee at auction through TreasuryDirect (VERIFIED-PRIMARY, treasurydirect.gov notes page).
  - **Evidence for the maturity date:** Treasury's auction data show the 2-year note auctioned 2025-12-22 was issued 2025-12-31 and matures 2027-12-31 (CUSIP 91282CPS4). The September 2026 note was issued 2026-09-30 and matures 2028-09-30 at a 4.787% high yield (VERIFIED-PRIMARY, api.fiscaldata.treasury.gov auctions query, 2026-09-27).
  - That the pattern holds in December 2030 is an ASSUMPTION.
  - The note matures one day before the 2033 set-aside. At today's 2y yield of 4.81%, $1 grows to $1.0997.
  - Model sizes: the floor is worth p5/p50/p95 $127k/$165k/$217k in 2033 (verified model). That means about $115k/$150k/$197k invested in 2031.
- **Alternate 1: the principal STRIP maturing Nov 15 2032** (912821KC8, the same CUSIP as the first rung). It pays exactly one amount with no coupons to reinvest, but it is broker-only and the mark-up is unknown.
- **Alternate 2: iBonds IBTM** (Dec 2032; 15 notes maturing Apr-Sep 2032; 0.07%; S1). It is a fund, it pays out around Dec 15 2032, and it is small ($555m).
- **Alternate 3: a T-bill fund (SGOV/BIL).** It protects the principal but does not lock the 2-year rate. The floor it supports is therefore only "today's value plus whatever bills pay". It is acceptable, but the promised floor is about 10% lower than with the note.

### E.5 The operating reserve after 2033, as payments are made
The script values the payments still owed at each Jan 1, on today's forward curve. ASSUMPTIONS: forwards are realised, and rungs are treated as exact-date zeros. The Nov-15 rungs actually pay about 47 days early, and each earns about $258 of T-bill interest while it waits (ASSUMPTION: 4% bill rate).

| Jan 1 | Payments left (face) | Holdings just before the payment | Market value | Value of the STRIPS still held after paying | Duration of what is left |
|---|---|---|---|---|---|
| 2033 | 10 ($500k) | $50k in T-bills (from the Nov-2032 rung) + 9 STRIPS | $394,930 | $344,930 | 4.60y |
| 2034 | 9 ($450k) | $50k in T-bills + 8 STRIPS | $363,676 | $313,676 | 4.20y |
| 2035 | 8 ($400k) | $50k in T-bills + 7 STRIPS | $330,957 | $280,957 | 3.78y |
| 2036 | 7 ($350k) | $50k in T-bills + 6 STRIPS | $296,706 | $246,706 | 3.36y |
| 2037 | 6 ($300k) | $50k in T-bills + 5 STRIPS | $260,825 | $210,825 | 2.92y |
| 2038 | 5 ($250k) | $50k in T-bills + 4 STRIPS | $223,086 | $173,086 | 2.47y |
| 2039 | 4 ($200k) | $50k in T-bills + 3 STRIPS | $183,342 | $133,342 | 2.01y |
| 2040 | 3 ($150k) | $50k in T-bills + 2 STRIPS | $141,396 | $91,396 | 1.53y |
| 2041 | 2 ($100k) | $50k in T-bills + 1 STRIP | $97,042 | $47,042 | 1.04y |
| 2042 | 1 ($50k) | $50k in T-bills | $50,000 | $0 | 0 |

How the reserve's composition changes:
- It holds only Treasuries, and it gets shorter and more cash-like every year.
- Nothing is ever sold before maturity, so rate moves change the market value but never the payment.
- The small interest earned while each rung waits (~$258 a year) goes to project flexibility.
- Brief section 8 item 9 asks the team to report the reserve at its 2033-01-01 market value ($394.9k). That belongs in the Final Report, not the Trading Notes.

---

## F. Compliance box

### F.1 Every WInS security in this file
All are **PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading.** The 2025-26 list is historical only: `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` (VERIFIED-REPO-FILE; entry number and line, with that year's expense ratio). I searched it for each ticker and for its fund name, because some lines merge the ticker with the name (e.g. "VGSH VANGUARD SHORT-TERM TREASURY").

| Security | Role here | On 2025-26 list? | Key facts, and source date |
|---|---|---|---|
| IEF | Hedge (primary) | Yes (#88, line 1053, 0.15) | 0.15%, 6.86y, $41.6bn; ishares.com 9/24-9/25 |
| TLH | Hedge (primary) | **No** (searched ticker and "10-20") | 0.15%, 11.59y, $10.5bn; ishares.com 9/24-9/25 |
| TLT | Hedge (alternate) | Yes (#87, line 1041, 0.15) | 0.15%, 14.88y; ishares.com |
| SPTI / SPTL | Hedge (alternate) | No | 0.03%, 4.78y / 13.65y; ssga.com 9/24 (S1) |
| VGIT / VGLT | Hedge (alternate) | No | 0.03%, 4.9y / 13.5y (8/31); Vanguard (S1) |
| VT | Growth (primary) | Yes (#23, line 273, 0.06) | 0.06%, 10,088 stocks; Vanguard 8/31 |
| VTI / VXUS | Growth (alternate) | Yes (#22, line 261, 0.03) / Yes (#51, line 603, 0.07) | 0.03% ("Vanguard Morningstar Total Stock Market ETF") / 0.05%; Vanguard |
| ITOT / IXUS | Growth (alternate) | No | 0.03% / 0.07%; ishares.com (S2) |
| VGSH | Floor proxy (primary) | Yes (#93, line 1113, 0.04) | 0.03%, 1.9y; Vanguard 8/31 |
| SHY | Floor proxy (alternate) | Yes (#86, line 1029, 0.15) | 0.15%, 1.79y; ishares.com 9/24 |
| BIL | Float / holding pen (optional) | Yes (#92, line 1101, 0.135) | 0.1353%, 0.10y; ssga.com 9/24 (now named "State Street SPDR …") |
| SGOV / SHV | Float (alternate) | No / Yes (#90, line 1077, 0.15) | 0.09%, 0.11y / 0.15%, 0.28y |
| Select Sector SPDRs, VNQ | Sector fallback only | 10 of 11 yes (XLRE no); VNQ yes | 0.08% gross (S2, fact sheets 6/30) |
| U.S. Treasury notes (e.g. 91282CRP8) | Optional floor or ladder illustration | Not an ETF (the bond rule applies) | Exists: fiscaldata.treasury.gov; availability in WInS UNVERIFIED |
| U.S. Treasury 3.125% due 2041-11-15 (912810QT8) | Hedge part 3, **only under a position limit** (D.1b) | Not an ETF | Exists: MSPD Table V (S1); listed in WInS UNVERIFIED; model duration 11.35y |
| IBGA | Not recommended (thin) | No | $73.7m; 9,537 shares traded 9/25; ishares.com |

### F.2 Exact checks in WInS before the first order
- [ ] 1. Log into the **official** account, not practice. Practice trades were reset (R-W77). A student places every trade, never the advisor (R-W87).
- [ ] 1b. Open **Portfolio Simulation > Portfolio Summary > Session Rules** (2026-27 WInS guide, via A4). Record:
  - the position limit, both per single position and per security type (equity/ETF vs bond);
  - day trading;
  - trades allowed;
  - commissions;
  - the trading end time on Nov 6.

  If the single-position limit is below about 43%, use section D.1b.
- [ ] 2. Re-read the SMApply Trading Details and FAQ pages that morning, and note any change to the $300k, 200-trade, volume and commission rules.
- [ ] 3. For each ticker, search WInS and confirm:
  - it appears as an **ETF** (not a mutual fund, ETN or leveraged product);
  - the full name matches the issuer. Watch for renames: BIL is now "State Street SPDR…"; VTI is "Vanguard Morningstar Total Stock Market ETF"; search "SPYM", not "SPLG" (S2).
- [ ] 4. Confirm each order has a real-time quote and is not routed as "international" (all picks are U.S.-listed).
- [ ] 5. Read the daily volume WInS shows and confirm the order is below **twice** that volume. This matters for VT and VGSH, whose issuers do not publish volume.
- [ ] 6. Confirm the commission shown ($25 per ETF trade) and that cash stays positive after all orders (no margin).
- [ ] 7. Find the Trading Note field and check for a **character limit**. None is published anywhere. The guide's example note is 59 words / 413 characters (A4).
  - Assume the note **cannot be edited or deleted**: Stock-Trak says students "cannot edit or delete their trade notes" (2017, via A4).
  - Write the note before pressing submit.
- [ ] 8. Open the Treasury-bond drop-down. Record which U.S. maturities exist (Nov 2032-Nov 2041; a ~2-year note), the minimum face amount, and how accrued interest is shown.
- [ ] 9. Check whether WInS pays interest on cash. This decides cash vs BIL for money that waits.
- [ ] 10. Recompute the IEF/TLH weights from the issuer pages (ishares.com, "Effective Duration") on the trade date. Record the numbers and the time.
- [ ] 11. Record in the team's decision log, not in the repo: who decided, when, which option, the exact note text, and the fill price.
- [ ] 12. If anything is ambiguous, ask Wharton through the official channel. Never contact Laura (R-W16).

---

## Open issues for Phases B-E and the team
1. **Which mirror: (i), (ii) or (iii)?** S3 recommends (ii). The team decides and writes the one sentence on what WInS represents.
2. **Duration anchor: 9.90 (Jan-2027 purchase) or 8.92 (2028 view).** The weights differ a lot (TLH 64.3% vs 43.5%). S3 recommends 9.90, and the team must keep to one.
3. **Tradable in WInS?** TLH, VT and VGSH need checking. So do the note-field limit, interest on cash, and which U.S. Treasuries are in the drop-down.
3b. **Session Rules position limit, and how "day trading" is defined.** A limit below about 43% forces the D.1b hedge. The U.S. Treasury 2041 bond variant needs bonds to have their own higher limit and the bond to be listed.
4. **The sleeve's bond instrument (VGSH) has no exact JPM line.** Update `strategy_mc.py` (sleeve bonds, and AC World for equity) so the model, the IPS and WInS agree.
5. **Update the brief and CLAUDE.md (main loop):**
   - starting cash is $300k (VERIFIED-PRIMARY);
   - the sector minimum is contradicted;
   - the "~35% equity" mirror is a mislabel of hedge/sleeve.
6. **2031 floor note maturing 2032-12-31:** the pattern is verified for December 2025, and its continuation to 2030 is an ASSUMPTION.
7. **VT and VGSH daily volume:** not published by Vanguard (UNVERIFIED). The volume-cap check has to be done in WInS.
8. **Timing:** the team's Australian state (time zone) is not recorded, and there is no verified "first trade by" date. Trade in week 1 anyway.

## Sources (all accessed 2026-09-27)
- **SMApply (VERIFIED-PRIMARY, curl):** https://wghsinvcomp.smapply.us/res/p/trading/ ; https://wghsinvcomp.smapply.us/res/p/faqs/ . WebFetch was blocked by the egress proxy; curl succeeded.
- **iShares product pages (VERIFIED-PRIMARY, curl):** https://www.ishares.com/us/products/239456/ (IEF), /239453/ (TLH), /239454/ (TLT), /239452/ (SHY), /314116/ (SGOV), /337747/ (IBGA). These gave effective duration (9/24), net assets, closing price and 30-day volume (9/25), expense ratio and SEC yield.
- **Vanguard (VERIFIED-PRIMARY):** https://investor.vanguard.com/vmf/api/{VT,VGSH,VTI,VXUS}/{profile,price,expense,characteristic}, the data behind https://investor.vanguard.com/investment-products/etfs/profile/{ticker}.
- **State Street (VERIFIED-PRIMARY):** https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-bloomberg-1-3-month-t-bill-etf-bil (redirected from the old spdr-bloomberg-1-3-month-t-bill-etf-bil URL).
- **U.S. Treasury (VERIFIED-PRIMARY):**
  - https://www.treasurydirect.gov/marketable-securities/treasury-notes/
  - https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query?filter=security_term:eq:2-Year,auction_date:gte:2025-10-01
- **Repo files:**
  - `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` (pp.1-2)
  - `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`
  - `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` (lines as cited)
  - `competition/official_market_data/daily-treasury-rates_2026-09.csv` and `JPM_LTCMA_2026_US_matrix_USD.pdf` p.2
  - `research/verified_2026-09-27/official_curve_pv.py` and `strategy_mc.py`
  - `research/insight_v1/phase_A/case_register.md` and `research/insight_v1/phase_A/wins_week1_guardrails.md` (A4: the 2026-27 WInS user guide, Session Rules and the Stock-Trak FAQ/blog, all as quoted there)
  - `research/insight_v1/wins_now/S1_treasury_sleeve.md` and `S2_growth_sleeve.md`

## What this teaches
A portfolio's weights are only as meaningful as what they stand for. "65% bonds / 35% stocks" sounded like Laura's plan. Rebuilding the plan in numbers showed that the 35% was the whole growth sleeve, and the sleeve is itself only 60% stocks. Getting that label right removes an inconsistency a judge would have caught between the Trading Notes and the IPS.

The second lesson is that order and rules carry as much meaning as tickers:
- buying the promise before the growth shows what comes first;
- waiting to buy the floor until the rule behind it is agreed shows process;
- deciding in advance never to sell the hedge after a rate rise shows that risk is measured against Laura's payments, not against the WInS scoreboard.

Small costs deserve to be counted too. Parking money in a T-bill fund for a week sounds prudent, but it loses to the commissions.
