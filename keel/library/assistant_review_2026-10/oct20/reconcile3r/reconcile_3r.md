# Reconciling option 3r: the red team versus the range audit

> **Verified 20 Oct (`oct20/verify_reconcile/verify_reconcile.md`, independent engine, two seeds): payment numbers CONFIRMED within ~0.4 points** (option 1 14.4-14.8%; 3r 0.59-0.65%, worst $3.1-3.3k; all condition rows match; scripts re-run byte-identical). Caveats: (1) top reach 77/45/76% depends on two unstated conventions ($1k rounding of the top; 17 days of floor interest missing from the 2031 projection) - without them 72/40/72.5%; say "about three in four" / "under half", not exact figures. (2) **BIGGEST open reading:** V5 para 4 says "an uncovered payment is funded from the equity Laura retains" (ips_report_live.md:28). If Laura's retained half stays on call after 2033, option 1 falls to ~1.4% short and 3r to ~0.07% - the team must decide this on 27 Oct before quoting 14% vs 0.6%. (3) New bug: the agreed basis prices the 0.07% iBond fee as free; counted properly the ladder is ~$300.4k (not $299.9k) and option 1's median minimum sits on the $140k/$145k edge. (4) Bug 9 partly wrong: the leftover is worth ~0 for 3r only once both plan rules are in place (~1 point in the range-audit frame); for option 1 it is worth ~3.4 points on the agreed basis (not 7.9). (5) Reserve returned to Laura in 2042: median ~$10-15k (not $19k). (6) Falls BEFORE 2033 never short a payment under the plan as written - they cost the gift and Laura's free money; payment shortfalls come from falls after 2033.


AI-generated research (Claude Code) for Team Caplet, Tue 20 Oct 2026 (Sydney). These are MODEL numbers for the 27 Oct vote. They are not text to submit. Any figure the team uses goes in the AI-use log and the Final Report's Works Cited (Wharton AI policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). Nothing here is drafted IPS, TNA or Final Report prose.

Folder: `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/reconcile3r/` (from here on `R/`). In this file, `oct19/` and `oct20/` are the sibling scratchpad folders.

## 0. Verdict in five lines
1. **Neither model is wrong, and neither number answers the question.** The 0.02% and the 6.2% are both correct outputs of their own code. Each one rests on a different unstated rule, and the plan as the team wrote it supports neither.
2. **What the gap is made of** (3r, 6.05 points, 19 Oct curve, same random paths):
   - +2.0: the 2033 need measured in today's value instead of dollars.
   - +1.0: rungs sized counting T-bill interest. A further −1.2 and +1.0 cancel each other out.
   - +2.7: the range audit's real iBond holdings.
   - +0.4: engine detail.
   - The rest is under 0.6 net.
   - The "leftover kept to 2042" rule that the range audit blamed adds **0.00** for 3r. It matters only for option 1 (+7.9).
3. **One agreed basis** (plan text read literally; range-audit pricing, which is more realistic; 19 Oct curve; 100,000 paths; two seeds):

   | | Option 1 | 3r as written | 3r with the top fix |
   |---|---|---|---|
   | Payment short | 14.4% | **0.6%** | **0.6%** |
   | Worst shortfall | about $10k | about $3.3k | about $3.3k |
   | Gift reaches the 2031 top | 77% | **45%** | **76%** |
   | Gift median | $165k | $162k | $159k |
   | 2031 minimum | $145k | $135k | $135k |

4. **Two plan rules move 3r from 0.6% to 2-6%,** so the team must write them down if it adopts 3r:
   - (a) rungs are sized to each holding's own maturity value, with no credit for interest after maturity. That costs about $2.5k more and makes a top-up a coin flip (50%).
   - (b) the 2033 reserve keeps the projected shortfall *in dollars* plus $5k.
5. **Bugs and misattributions (section 6):** two small bugs in the study, one shortcut in the study and the red team that flatters the reserve, a mislabelled "consistent" case in the red team, and a wrong attribution in the range audit.

---

## 1. What I did
- **Read all three engines line by line:**
  - `oct19/coupon/scripts/coupon_options.py`, the study, called CO below.
  - `oct20/redteam3r/scripts/rt_engine.py`, the red team (RT). It is CO's `run()` with switches added; its `coupon_options.py` is byte-identical to the study's.
  - `oct20/rangeaudit/scripts/laura_sim.py`, the range audit (RA).
- **Built two switchable copies:**
  - `R/scripts/engX.py`: CO with every RA assumption exposed as a switch.
  - `R/scripts/engY.py`: RA plus seven switches.
  - **Both reproduce their originals exactly** (maximum difference 0.0 on every path):
    - engX against CO: 16 and 19 Oct, options 1 and 3r (`check_engX.py`). On 19 Oct: 15.578% and 0.016%.
    - engY against RA: 19 Oct (`check_engY.py`). 32.27% and 6.162%, which equals RA's published 6.2%.
- **Same random paths:** CO's and RA's path generators draw in the same order. With the same seed the rate and stock paths are identical (checked: maximum difference 0.0, `wf_seed20261019.json → paths_identical`). So the waterfall is a controlled experiment: only the assumptions change.
- **Basis for every run:**
  - treasury.gov par curve of **19 Oct 2026**: 1y 4.50, 2y 4.77, 5y 4.94, 10y 5.15, 20y 5.53, 30y 5.48. This is the same row as RA's `data/tsy_202610.csv` and RT's `tsy_202610_fetch20oct.csv`, which were checked identical.
  - Parallel random walk at 1.0 point a year.
  - VT at 7% compound with 16.78% volatility, correlation 0.
  - 100,000 paths. **Seed 20261019, then re-run with seed 7.** Every row of every table moved by 0.06 points or less (3r) and 0.25 points or less (option 1).
- **History replay:** RA's 688 windows (Apr 1953 to Jul 2010 starts; FRED GS10 plus Shiller, repo copies), additive and proportional.

## 2. Every assumption that differs

| # | Assumption | Study (CO) / red team (RT) | Range audit (RA) | Effect on 3r short | What the plan says (section 3) |
|---|---|---|---|---|---|
| 1 | **Rung sizing basis** | $50k on the holding's **maturity date**, coupons at its own yield; waiting cash counts 0% (`coupon_options.py:83-84`) | $50k on the **1 Jan payment date**, counting T-bill interest on the waiting cash (`laura_sim.py:216-219`, `DEFAULT gap="bill"`) | +1.1 (in sequence); +2.4 alone on the agreed basis | Maturity basis |
| 2 | **Waiting-cash rate, as it actually happens** | 0% (`:136-150`). RT's `gap_bills` adds T-bills (`rt_engine.py:92-101`) | T-bills at the rate of the maturity month | −1.2 (a cushion if not counted in the sizing) | Short Treasury ETF (filed notes) |
| 3 | **Waiting cash in the 2031/2033 projections** | 0%. RT `gap_bills`: counted | Counted | +1.0 | Not counted (it must match the sizing) |
| 4 | **Carry between payments** | 0% | 1-year yield | 0.01 | Immaterial |
| 5 | **How the 2033 need is measured and held** | Nominal sum of projected gaps, held as one cash pot at 0% (`:241-244`) | Today's value on the 2033 curve, covered by matched zeros (`laura_sim.py:308-310, 374-395`) | **+2.0** (almost all from the reserve keeping less; section 4c) | Dollars (study's 3r rule) |
| 6 | **Cover chain order** | leftover → reserve → Laura's half → whole gift (`:241-243`) | leftover → reserve → half plus anything above the cap → gift above the floor → floor (`:375-388`) | 0.00 | Same in substance (`competition/COMPETITION.md:161-162`) |
| 7 | **Unused 2027 leftover** | Kept in cash to 2042 for **every** option (`:244`) | Released to Laura in 2033 | **0.00 for 3r**; +7.9 for option 1 | Silent; "covered first from the 2027 leftover" |
| 8 | **3r release that would push the gift above the cap** | Stays in the reserve to 2042 (`:236-238`) | Leaves the reserve; the excess goes to Laura (`:378-383`) | 0.00 (0.06 at the RA end) | Stays (study: "releases the rest to the contribution", unused back in 2042) |
| 9 | **3r top rule** | Top adds the $10k bought (`:231`) | Top adds the reserve's 2031 market value, about $11.5k (`:365-366`) | 0 on payments; top reached 43.6% → 34.5% | $10k (study code) |
| 10 | **Reserve valuation** | $10k grown at its purchase yield × price ratio. Its own coupons implicitly earn the purchase yield forever, and it keeps growing after Nov 2041 (`:210`; RT copies this, `rt_engine.py:174`) | Coupons reinvested at the yield of the day, marked at market | +0.05 | Market (physics) |
| 11 | **What "short" means** | After all cover; **total** uncovered over ten payments > $100 (`:421`) | After all cover; **any one** payment > $100 (`summ.py`, `miss_any`) | 0.00 (option 1: −1.9) | Either |
| 12 | **2028 top-up cost** | Exactly the Jan-2027 gap (`:182`) | Missing rungs bought at Jan-2028 prices | 0.00 | RA |
| 13 | **iBond funds** | Par bonds ending 15 Dec, coupon = yield | iShares coupon and maturity data (holdings mature mid-year; the fund holds bills to 15 Dec; 0.07% fee) | **+2.7** under RA rules; +0.6 on the agreed basis | RA is more realistic |
| 14 | **Coupon reinvestment** | At own purchase yield + shift | At the curve yield for the remaining term (roll-down) | −0.5 | Both defensible |
| 15 | **Yield floor** | 0.25% | 0% | +0.35 | Choice; 0% is more cautious |
| 16 | **2028 floor priced on** | Forward yields | Unchanged curve | +0.09 | Either |
| 17 | **2031 range rules** | Bottom R − $3,700; top R + half VT − uncovered | Bottom 98% of projected floor less net-minimum; $1k rounding | 0.00 | Net-minimum (`competition/COMPETITION.md:158-159`) |
| 18 | **Stock model** | Log-volatility 0.1678 | Exact conversion 0.154 | 0.00 (top reach +1.6 for option 1) | — |
| 19 | **Curve date** | 16 Oct published (19 Oct re-run: 0.016%) | 19 Oct | 16 → 19 Oct: 0.020 → 0.016 (CO) | Use 19 Oct now; re-price 6 Nov |
| 20 | **Rate volatility** | 1.0 pt a year | 1.0 pt a year | none | Same |
| 21 | **Seed / paths** | 20261019 / 100k | 20261020 / 100k (compare runs 50k) | ≤0.1 | Same seed used here |
| 22 | **Cash-flow timing** | Month grid from 1 Jan 2027 | Actual dates | Part of the bridge (+0.07 on the agreed basis, +0.40 at the RA end) | — |

## 3. Which reading is the plan as the team wrote it
- **Certainty and sizing (rows 1-3).**
  - V5 defines certainty as "each payment is covered at purchase by Treasuries maturing shortly before it, with any shortfall met from her other holdings and the facility floor last" (`oct19/drive/ips_report_live.md:25`).
  - "Covered at purchase by Treasuries maturing before it" reads as: the holding's maturity value covers the payment. It does not lean on interest earned after maturity. That is CO's sizing.
  - Waiting cash does earn interest. The filed notes say the proceeds wait "in a short-term Treasury ETF" (`/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:16-17`).
  - So the literal reading is: **sizing excludes the interest, the projection excludes it too, and the interest really arrives as a cushion.**
    - CO assumes the interest never arrives.
    - RT's "consistent" case counts it in the projection but not in the sizing.
    - RA counts it everywhere.
  - None of the three is this reading.
  - **The catch:** the team's quoted ladder costs ("about $293k on the 6 Oct curve", `/home/user/snap/main/COMPETITION.md:153-154`, and the filed IBTR note "her first $300,000 is enough") are payment-date figures. Those *do* count the interest. If the team keeps maturity sizing, the honest 19 Oct cost is **about $298.5-299.9k**. A Jan-2028 top-up is then needed in about 50% of paths, against 42% on RA's basis.
- **The 2033 need (row 5).**
  - The plan says only "any expected shortfall is covered first from the 2027 leftover, then Laura's half, then the part of the contribution above the floor" (`competition/COMPETITION.md:161-162`).
  - Option 3r is the study's own design, and its rule keeps "projected need + $5k" with need as a dollar sum (`coupon_options.py:236`).
  - **As written = dollars.** Today's value is a legitimate alternative, but it is a different, weaker rule.
- **Leftover (row 7).** The plan never commits the unused leftover past 2033, and CO's own docstring says "nothing is committed after 2033" (`coupon_options.py:22`). **As written = released.** For 3r it makes no difference.
- **Release above the cap (row 8) and the top (row 9).** The study wrote 3r as "counted in the top" with the $10k (`coupon_options.py:231`), and as "releases the rest to the contribution" with "unused reserve goes back to Laura (median about $19k in 2042)" (`oct19/coupon/coupon_risk_options.md:62, 131-132, 152`). **As written = $10k in the top, and the release stays in the reserve if it does not fit under the cap.** The "top fix" means the top counts $5k (RT section 3b).
- **Physics (rows 10, 12-16).** These are not plan rules.
  - I use RA's more realistic choices: market valuation, Jan-2028 prices, iShares holdings, roll-down, 0% floor, unchanged curve.
  - I keep the study engine as the low end of the range.
- **Short (row 11).** The case asks for each payment to be funded (`Laura_Gao_2026_Client_Profile.txt:91-92`), so "any payment short by more than $100" is the reading used.

## 4. Waterfalls (19 Oct curve, 100,000 identical paths; seed 20261019 with seed 7 in brackets)

### 4a. Option 3r: study (0.016%) → range audit (6.066%), one switch at a time
"Bridge" means the same rules in the other engine; its row measures the leftover engine detail.

| Step (cumulative) | Short % | Change, points | Seed 7 change | Gift reaches top |
|---|---|---|---|---|
| Study as published | 0.016 | | (0.013) | 42.4% |
| iBond coupon bug fixed (bug 1, section 6) | 0.017 | +0.00 | +0.00 | 41.9% |
| Reserve marked at market, its coupons at day yields | 0.070 | +0.05 | +0.04 | 42.1% |
| Leftover released / release leaves / overflow counts as cover | 0.070 | 0.00 | 0.00 | 42.2% |
| **Need in today's value, matched zeros** | 2.109 | **+2.04** | +1.99 | 43.1% |
| Waiting cash really earns T-bills (cushion) | 0.938 | −1.17 | −1.11 | 43.1% |
| Projection counts that interest | 1.976 | +1.04 | +1.00 | 45.0% |
| Carry earns the 1-year yield | 1.985 | +0.01 | +0.01 | 45.0% |
| **Rungs sized counting T-bill interest** | 3.054 | **+1.07** | +1.12 | 43.6% |
| "Any one payment" metric; top-up at 2028 prices | 3.054 | 0.00 | 0.00 | 43.6% |
| Top adds the reserve's 2031 market value | 3.054 | 0.00 | 0.00 | **34.5%** |
| Engine bridge (dates, partial rungs, curve build) | 3.451 | +0.40 | +0.35 | 34.4% |
| Floor priced on unchanged curve | 3.540 | +0.09 | +0.10 | 34.0% |
| RA range rules | 3.540 | 0.00 | 0.00 | 35.6% |
| Yield floor 0% | 3.885 | +0.35 | +0.34 | 35.6% |
| Roll-down reinvestment | 3.376 | −0.51 | −0.51 | 35.7% |
| **iShares iBond holdings** | 6.066 | **+2.69** | +2.74 | 34.8% |
| Exact log-volatility | 6.066 | 0.00 | 0.00 | 34.3% |

Total: +6.05 points, every step accounted for (`R/data/waterfall_tables.txt`).

**The order matters.** Each switch alone from the study, and each removed from the full rule set (`R/data/wf_seed*.json`):

| Switch | Alone from the study | Removed from the full set (3.05%) |
|---|---|---|
| Need in today's value | 0.02 → **1.24%** | 3.05 → 1.10% |
| Projection counts interest | → 1.00% | → 1.32% |
| Sizing counts interest | → 0.02% (projection still at 0%) | → 1.99% |
| Leftover released | → 0.02% | → 2.91% |
| Release leaves the reserve | → 0.02% | → 2.99% |

### 4b. Option 1: study (15.6%) → range audit (32.1%)
| Step | Change, points (seed 7) |
|---|---|
| iBond coupon bug fixed | +0.59 (+0.60) |
| **Leftover released, not kept to 2042** | **+7.85 (+7.96)** |
| Overflow counts as cover | 0.00 |
| Need in today's value / matched zeros | +0.99 (+0.94); this is the cash-pot versus zeros effect |
| Waiting cash: bills realised −14.41; counted in projection +12.27; carry −0.11; **sized counting interest +5.36** | net +3.11 |
| "Any one payment" metric | −1.92 (−1.96) |
| Engine bridge | −0.12 (−0.09) |
| Yield floor 0% / roll-down | +0.45 / −0.26 |
| **iShares iBond holdings** | **+5.84 (+5.72)** |
| **Total** | **+16.53** |

### 4c. Why "today's value" costs 3r so much
I split that switch into two parts (`R/data/diag_pv_out.txt`).

| Part | 3r short | Option 1 short |
|---|---|---|
| Cash pot vs matched zeros | 0.07 → 0.12% | +1.0 point (a pot can pay any year's gap) |
| Dollar vs today's-value measure of need | 0.12 → **2.11%** | 0 |
| Same split on the as-written rules | 0.02 → **0.94%** | — |

- **The mechanism.** Under the dollar rule the reserve keeps "projected gaps in dollars + $5k". That is 25-35% more than their present value, and the kept bond keeps earning about 5%. So the true margin grows with the size of the problem. Under the today's-value rule the only margin is the flat $5k.
- **Comparison.** RA's own run with a $10k margin and today's value still gives 4.6% (`oct20/rangeaudit/data/extra2.json`). So the dollar rule is worth more than another $5k of margin.

### 4d. Physics on the as-written rules: study engine (0.010%) → range-audit pricing (0.627%)
| Step | 3r change, points (seed 7) | Option 1 change, points |
|---|---|---|
| Carry at 1-year yield | 0.000 | −0.05 |
| Engine bridge | +0.070 (+0.073) | −0.49 |
| Unchanged-curve 2028 purchases | +0.012 | 0 |
| RA range rules | 0 | 0 |
| Yield floor 0% | +0.345 (+0.329) | +0.86 |
| Roll-down | −0.402 (−0.387) | −0.35 |
| **iShares iBond holdings** | **+0.592 (+0.620)** | **+4.12** |
| Exact volatility | 0 | 0 |
| **Total** | 0.010 → 0.627 (seed 7: 0.006 → 0.646) | 10.37 → 14.46 |

**Why the iBond model matters.** Real IBTM-IBTR holdings mature through the year. The fund then sits in bills until 15 Dec. If bill rates fall, that money earns less, and the par-bond shortcut hides it. It is the largest single physics item in both options.

### 4e. Top reached (3r as written)
| Model | Top reached |
|---|---|
| Study (CO) | 42.4% |
| Study rules in the range-audit engine | 45% |
| Range audit (RA) | 34% |

- **The whole RA gap is row 9:** its top adds the reserve's 2031 market value, about $11.5k, instead of $10k (43.6% → 34.5%, section 4a).
- **The top fix** (+$5k) gives 76% (RA engine) or 73% (study engine; RT 72-73%).

## 5. The agreed numbers (19 Oct curve; MODEL)
**Agreed basis:**
- Plan rules read as in section 3.
- engY pricing.
- 100,000 paths. The first figure is seed 20261019, the bracket is seed 7.
- Source: `R/data/agreed_seed*.json`.

| | Option 1 (state only) | 3r as written | 3r with top fix (+$5k) |
|---|---|---|---|
| Ladder cost on 1 Jan 2027 (median) / chance it exceeds $300k | $299.9k / 50% | same | same |
| 2031 minimum (median) | $145k | $135k | $135k |
| 2031 top (median) | $165k | $164k | $159k |
| Gift median / 1-in-20 low | $165k / $135k | $162k / $133k | $159k / $131k |
| **Gift reaches the 2031 top** | **77%** (77%) | **45%** (45%) | **76%** (77%) |
| Gift below the announced minimum | 0.04% | 0.01% | 0.01% |
| **A payment short** | **14.5% (14.4%)** | **0.63% (0.65%)** | **0.62% (0.64%)** |
| Short by more than $1k | 9.4% | 0.13% | 0.13% |
| Typical / 1-in-100 / worst shortfall | $1.6k / $4.6k / $10.1k ($9.4k) | $0.55k / $0 / $3.3k ($3.2k) | same as 3r |
| History, additive (688 overlapping windows) | 18.3% | 1.0%: 7 windows, all starts Aug 1984-May 1985, worst $1.0k | 1.0%; top reached 78.5% |
| History, proportional | 7.0% | 0 of 688 | 0 of 688 |
| Laura's free money in 2033 (median) | $25.9k | $22.4k | $23.0k |

The history replay is deterministic, so it is identical on both seeds.

**The same rules in the study engine** (low end):

| | Option 1 | 3r as written | 3r with top fix |
|---|---|---|---|
| Payment short | 10.4% | 0.010% (0.006%), worst $0.3-0.4k | 0.010% |
| Top reached | — | 42% | 73% |
| Gift median | — | $163.2k | $160.1k |

**The honest range for 3r on the plan as written: about 0.01-0.6% of paths short, never more than about $3.3k.**

**When each number holds.** Each line changes one condition from the as-written basis (3r / option 1):

| Condition changed | 3r | Option 1 |
|---|---|---|
| Need measured in today's value, cover as matched zeros | 2.2% | 20.7% |
| Rungs sized counting T-bill interest (RA sizing) | 3.0% (worst $7.0k) | 27.2% |
| Projection counts interest, sizing does not (RT's "consistent") | 2.1% | 24.2% |
| Both of the first two, plus RA's top and release (= range audit) | 6.1% | 32.1% |
| Waiting cash after maturity really at 0% | 1.0% | 25.9% |
| Everything sized to the iBond holdings' own maturities at 0% (harshest) | 0.06% | 23.6% |

The last line costs about $3.8k more and drops the median gift to $158k.

| Other conditions | 3r | Option 1 |
|---|---|---|
| Unused leftover kept to 2042 | 0.61% | 11.0% |
| Yield floor 0.25% instead of 0% | 0.28% | 13.6% |

**Unchanged across every model:** 3r roughly halves the chance of reaching the top unless the top is fixed. It cuts the minimum by $10k. It cuts the median gift by about $3k as written, or about $6k with the fix.

## 6. Bugs and misattributions found

**In the study (CO), and copied by the red team:**
1. **`coupon_options.py:141` (bug, small).**
   - iBond rungs are *sized* with the par coupon (`:76-84`), but *pay* a coupon equal to their yield to maturity, which is higher.
   - Each fund over-delivers by about $110. Option 1 short is understated by 0.6 points; 3r by 0.001.
   - The red team noted it (RT section 1d) but kept it.
2. **`coupon_options.py:210` (optimistic shortcut).**
   - The reserve's value is `$ × (1+y0/2)^(2h) × price ratio`. In falling-yield paths, which are exactly when it is needed, that assumes its own coupons keep earning the purchase yield. It also keeps growing after Nov 2041.
   - Effect on 3r: +0.05 points.
   - **The red team's main hedge finding** ("most of the protection is the locked yield", RT section 2a) is measured with this same formula (`rt_engine.py:174`, `carry41` at `:158-159`). Its "locked yield" share is therefore somewhat overstated. With market valuation the reserve's own coupons do face reinvestment risk.
3. **`coupon_options.py:244` versus `:21-22` (text-code mismatch).**
   - The docstring says option 1 commits nothing after 2033 and sets aside the projected shortfall *from* the leftover.
   - The code keeps the *whole* leftover to 2042 for every option.
   - This is worth 7.9 points of option 1's figure. With the leftover released, option 1 is 24% on the study's own basis, not 16%.
   - Once interest on waiting cash is counted as a cushion, option 1 is 10.4% (study engine) to 14.5% (range-audit engine).
4. **`coupon_options.py:233-245` (accounting gap).** The part of floor + half VT above the cap is counted nowhere: not in the gift, not in Laura's 2033 money, not as cover. "Laura's free money" is understated. Payments are unaffected (0.00).
5. **`coupon_options.py:182` (simplification).** The 2028 top-up costs the Jan-2027 gap with no interest. Effect 0.00.
6. **`coupon_options.py:227-231` (design flaw, already found by the red team).** The reserve reduces the 2031 uncovered shortfall *and* adds $10k to the top, so the top is reached about 42-45% of the time. Confirmed here in both engines.
7. **`coupon_options.py:284`.** `unc_net` subtracts total waiting interest from total shortfall: the study's "16% → 7.5%" line. It is not a plan rule. The consistent figures are in section 5.

**In the red team (RT):**

8. **`redteam_3r.md:63-68` (mislabel).**
   - "0.41% if the plan counts T-bill interest consistently" is measured with `gap_bills` (`rt_engine.py:92-101`). That counts the interest in the projections but *not* in the rung sizing. It is a hybrid, not a consistent plan.
   - With the study's par iBonds it gives 0.37-0.41%. With realistic iBond holdings it gives 2.1%.
   - The two coherent versions are: interest a cushion (0.01-0.6%), or interest counted in sizing and projection (3.0% with dollar need, 6.1% with today's value).

**In the range audit (RA):**

9. **`range_audit.md:136` (wrong attribution).**
   - It says the 0.02% "needs both CO assumptions: waiting cash at 0% in sizing (alone 2.2%) and the whole leftover kept to 2042 (alone 5.3%)", and calls the rest "small pricing detail".
   - The leftover is worth 0.00 for 3r in every frame I tested (0.627 → 0.614% on the agreed basis; 0.070 → 0.070% in the study frame).
   - RA's own `data/compare.json` shows its largest 3r steps were "cover at nominal, cash 0%" (2.83 → 0.35%) and "iBond funds as par bonds" (6.61 → 3.92%). The text does not mention either.
   - The real drivers are the dollar-versus-today's-value need, the sizing basis and the iBond model (section 4a).
10. **`laura_sim.py:251-267` (emulation bug, small).** With `j28_curve="forward"`, the 3r reserve is bought on the forward curve (`:263`, while `self.c` is the forward curve), then valued on the base curve (`:267` restores it; `res_mv` uses it). That books an instant price change. It affects only RA's emulation step 8, by about 0.03 points.
11. **`laura_sim.py:216-219, 241` (not a bug, but a trap).** With `gap="zero"` and the iShares iBond model, rungs are sized to the holdings' mid-year maturities with nothing earned to 15 Dec. On 19 Oct the ladder then costs $303.7k. Any "maturity sizing" run in RA's engine must credit the fund's own bill income to 15 Dec. I added that as `gap_*="fund"` in engY.
12. **`laura_sim.py:378-383`.** RA's 3r sends the whole release above "need + $5k" out of the reserve, even when the gift cannot use it. That contradicts 3r as the study wrote it. It is a reading choice, with 0.06 points of effect.

**Not bugs, but labels to fix:**
- RA's "0% vs bills" toggle in its compare runs moves sizing *and* realised cash together.
- RT's "0.02% vs 0.41%" and RA's "0.02% vs 6.2%" each change several rules at once. Neither says so.

## 7. What the team may safely say (claims, not wording)
- **On the payments.** "With the reserve, our model left a payment short in under 1 path in 100, never by more than about $3,000." Name the conditions beside it:
  - maturity sizing;
  - the reserve keeps the dollar shortfall plus $5k;
  - a parallel random walk, 1 point a year;
  - 19 Oct curve.
- **What not to say:**
  - not "0.02%";
  - not "zero in history" (1% of overlapping additive windows, all from 1984-85 starts);
  - not "6%".
- **On option 1.** Without a reserve, small post-2033 gaps are likely: about 1 path in 7, typically about $1.5k, worst about $10k. Those gaps fall on money Laura has already taken out (case lines 91-92).
- **The cost of 3r, in Laura's terms:**
  - minimum −$10k ($145k → $135k);
  - median gift −$3k as written, or −$6k with the top fix;
  - the money is mostly returned to Laura in 2042, not lost.
- **The top.**
  - "About three in four paths reach the top" (V5, `ips_report_live.md:29`) stays true for option 1 (77%) and for 3r with the top fix (76%).
  - It is **false for 3r as written (45%).**
- **The ladder cost.** If the team adopts maturity sizing, stop quoting the payment-date cost:
  - about $300k on 19 Oct, with a top-up about a coin flip (50%);
  - not "$293k" and not "her first $300,000 is enough".
  - The filed IBTR note cannot be edited; the IPS and Final Report can carry the correction.
- **The two rules (plain principle in the IPS, detail in the Final Report).** Without them, the numbers above do not hold:
  - (a) each holding is sized to cover its payment by its own maturity, and any interest while the cash waits is extra;
  - (b) in 2033 the reserve keeps the projected dollar shortfall plus $5k, and only the rest goes to the contribution.
- **Decisions for the students on 27 Oct:**
  - adopt both rules, or accept about 2-6%;
  - top +$5k or +$10k;
  - leftover released or kept (immaterial for 3r).

## 8. Limits
- **Model family.** Both engines share one model family: parallel shifts only, no mean reversion and no twists. RT found that twists and a bootstrap add about 0.2-0.3 points to 3r on the study basis (`redteam_3r.md` section 1c). Not re-run here.
- **iBond funds** are one bond each at the fund's average maturity. Real funds hold several bonds.
- **Engine detail (the "bridge").** 0.07 points on the agreed basis, 0.40 points at RA's end. These are timing, partial-rung top-ups and curve construction. I measured them but did not split them further.
- **History.** Overlapping windows, about 4 independent periods. US stocks stand in for VT. The 1984-85 additive windows push yields to the floor, a known artefact.
- **No taxes; no costs outside WInS.**
- **UNVERIFIED (unchanged):** when WInS credits coupons; the WInS price of the Nov-41 bond; the WInS 2×-volume rule for bonds; actual iBond distribution timing.
- **Re-price on the 6 Nov close.** The ladder cost moved about $1.6k between 16 and 19 Oct.

## 9. Reproduce
Run from `R/scripts/` with `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I`:
- `check_engX.py` and `check_engY.py` (exactness checks).
- `wf.py SEED 100000 ../data/wf_seedSEED.json` (section 4a-b, with alone and removed).
- `diag_pv.py SEED` (section 4c).
- `phys.py SEED 100000 ../data/phys_seedSEED.json` (section 4d).
- `agreed.py SEED 100000 ../data/agreed_seedSEED.json` (section 5, plus history).

Seeds used: 20261019 and 7. Tables: `R/data/waterfall_tables.txt`. Inputs: `R/data/tsy_202610.csv` (19 Oct row; copy of RA's treasury.gov fetch, 19 Oct 21:38 UTC) and `R/data/shiller_monthly.csv`.
