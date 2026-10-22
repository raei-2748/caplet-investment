# Verification of the 2033 re-match study ("1R" and "BOTH")

AI-generated verification for Team Caplet, Tue 20 Oct 2026 (Sydney). Claude Code wrote this. These are MODEL numbers for the Tue 27 Oct vote, not text to submit. If the team uses any of it, log it in the AI-use record and later in the Final Report's Works Cited (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026).

**Paths.** `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/`.
- Under test: `oct20/rematch1R/rematch_1R.md` (RM), `oct20/rematch1R/scripts/rematch_lp.py` (LP), `oct20/rematch1R/scripts/rt_engine.py` (RT), `coupon_options.py` (CO, the study engine).
- My folder: `oct20/verify_rematch/`. Scripts are in `scripts/` and outputs in `data/`. Auction-data downloads are in `web/`.
- My code is new and imports none of theirs: `my_lp.py` (LP), `my_mc.py` (Monte Carlo), `bugcheck.py`, `noround.py`, `mech.py`.

---

## Verdict

**The study's main numbers stand. Its two "costs of BOTH" are overstated, and one robustness claim is wrong.**

What holds up:
- My own LP gives the same deterministic table. Once their iBond coupon bug is copied in, buy-only matches to within $30 and trim to within $70 (full within $0.26k in every cell but one, −$0.85k).
- My own 20,000-path Monte Carlo gives the same premium: **+$2.1-2.2k median and +$5.8-5.9k for the 1-in-20 case**.
- It also confirms the ranking:
  - 1R breaks the announced minimum in **1.2-1.3%** of paths, against **0.14-0.17%** for 3r.
  - BOTH never leaves a payment short, keeps the minimum near 3r's level (0.19-0.23%), and reaches the top in **79-81%** of paths, against 71-73% for 3r.

What needs correcting:
1. **"Laura's 2042 money: −$13k" under BOTH is mostly bookkeeping.** In the model, 3r's bond income is reinvested at market yields and its unused reserve keeps earning in the Nov-2041 bond. BOTH's after-2033 cash and leftover reserve are held at **0%**. Treated the same way (waiting cash earns T-bills; the leftover reserve stays in the bond), the gap is **about $2k, not $13k**.
2. **The re-match is understated by about $1.8k at the median.** Like the study engine, it treats coupons reinvested before 2033 as one lump that keeps compounding to maturity. In reality those coupons buy extra bonds, and the extra bonds' coupons after 2033 also wait at 0% in the LP. Counted that way, the buy-only premium is **+$4.0k median / +$7.5k 1-in-20**, not +$2.1k / +$5.8k. BOTH's top-reach falls to about **76%**, still above 3r's 71%.
3. **"Trim and buy-only do not depend on this [0%-cash] artefact" (RM:191) is wrong for buy-only's cost.** At unchanged yields, buy-only costs $6-7.7k only because waiting cash is assumed to earn nothing for 9 years.
   - With T-bills at today's rate it costs **$0**.
   - The 0% rule is the right way to *size* certainty. But most of the "premium" comes back as T-bill interest. It is a worst-case reserve, not money spent.

**Safe for the vote:** BOTH (buy-only form) beats 3r on payments and on top-reach and keeps the minimum about as safe. Its real cost to Laura is small, about $2k of 2042 money with fair crediting. 1R alone is clearly worse for the minimum. That stays true even if the minimum is cut by $25k.

---

## 1. Discrepancy table

"Mine" = my independent code. Their figures are from RM. "Bug" = the study's iBond coupon convention (CO:141, copied at LP:143).

| # | Claim (where) | Theirs | My check | Status |
|---|---|---|---|---|
| 1 | Buy-only premium over the frozen estimate, MC median / 1-in-20 (RM:79, :167) | +$2.1k / +$5.8k | +$2.15k / +$5.83k (16 Oct, seed 11); +$2.12k / +$5.81k (seed 23); +$2.16k / +$5.86k (19 Oct) | **CONFIRMED** on their book convention |
| 1b | Same, with pre-2033 income booked as extra bonds ("units") | — | **+$4.0k / +$7.5k**; 2033 need median $7.7k (vs $5.9k) | **UNDERSTATED by ~$1.8k** (§3.1) |
| 2 | Deterministic buy-only −2/−1/0/+1/+2 (RM:131-137), 16 Oct | $20.5k / $13.4k / $5.9k / −$0.5k / −$0.9k | Patched: $20.6k / $13.5k / $6.0k / −$0.4k / −$0.7k (+$0.11-0.14k). With the bug copied: within $3-30 | **CONFIRMED** (within $0.15k) |
| 3 | Deterministic trim (same lines) | $19.7k / $10.4k / $2.2k / −$6.3k / −$14.2k | Patched: $20.2k / $11.0k / $2.7k / −$5.7k / −$13.7k (+$0.54-0.58k). With the bug: within $15-70 | **CONFIRMED**. The gap is the bug (just over $0.5k) |
| 4 | Deterministic full (same lines) | $18.3k / $8.2k / $0.1k / −$8.4k / −$15.3k | Patched: $19.0k / $8.9k / $0.8k / −$7.6k / −$14.5k (+$0.65-0.79k). With the bug: +$0.15-0.26k, one cell −$0.85k (19 Oct −2) | **CONFIRMED in shape**. About $0.7k of the gap is the bug; the rest is pricing method and the LP picking a different solution |
| 5 | Frozen estimate −2 / −1 points | $18.9k / $9.5k | Patched **$19.4k / $10.0k** (16 Oct); $19.5k / $10.1k (19 Oct) | **BUG-BIASED** by −$0.5k, as already known (`verify_reserve.md:16`) |
| 6 | The 19 Oct curve is within $50 of 16 Oct in every cell (RM:131) | ≤$50 | ≤$50 for buy-only and trim; full up to $0.9k (different LP solution) | CONFIRMED (buy-only, trim) |
| 7 | 1R below the announced minimum vs 3r (RM:16, :93) | 1.16% vs 0.11% ("~10×") | **1.31% vs 0.17%**, 1.26% vs 0.17%, 1.20% vs 0.14% (about 8×) | **CONFIRMED** (ratio 7-9×) |
| 8 | 1R with no minimum cut (RM:95) | 2.3-2.6% | 2.89% | CONFIRMED (same order) |
| 9 | 1R and BOTH: 0% of payments short (RM:13, :87) | 0% | 0% in every run; the date-by-date replay of each LP solution never falls below $0.00 | **CONFIRMED** (by construction, given 0% carry) |
| 10 | 3r payments short (RM:77) | 0.02% | 0.08-0.10% | DIFFERENT, small. My Nov-41 reserve reinvests its coupons at the day's yield and is marked at market. Theirs grows at the purchase yield (`reconcile_3r.md` §2 row 10: "flatters the reserve"). The ranking is unchanged |
| 11 | BOTH below the minimum vs 3r (RM:23) | 0.16% vs 0.15% | 0.22% vs 0.17%; 0.23% vs 0.17%; 0.19% vs 0.14% | CONFIRMED in substance: BOTH is about 0.05 point worse, not equal |
| 12 | BOTH top-reach vs 3r (RM:21) | 80.2% vs 71.7% | 79.5 / 79.1 / 80.7% vs 71.4 / 70.8 / 72.5% | **CONFIRMED** on their book |
| 12b | Same, units book | — | **75.8% vs 71.4%** | Advantage **halves** (+4 points, not +8) |
| 13 | BOTH gift median +$0.3k vs 3r (RM:21) | +$0.3k | +$0.25k | CONFIRMED |
| 14 | **Laura's 2042 money, BOTH vs 3r (RM:22, :97, :250)** | $9.7k vs $22.5k (−$13k) | Their bookkeeping: $9.5k vs $22.1k (−$12.6k). Leftover reserve kept in the Nov-41 as 3r does: $14.0k (−$8.0k). **Waiting cash at T-bills for both options: $28.6k vs $30.5k (−$1.9k)**; seed 23 −$2.1k; 19 Oct −$1.9k; units book −$2.0k | **OVERSTATED**. The $13k is an asymmetry (0% for BOTH, market reinvestment and Nov-41 carry for 3r) |
| 15 | Laura's 1-in-20, 1R vs 3r (RM:17) | $1.3k vs $13.0k | $1.3k vs $11.8k | CONFIRMED |
| 16 | "Trim and buy-only do not depend on this artefact" [0% waiting cash] (RM:191) | — | Buy-only at unchanged yields: $7.7k at 0% carry, $4.3k at 2%, **$0 at 4%** (units book) | **WRONG for buy-only's cost**. Right only for its trades |
| 17 | New 15-Nov notes 2033-41 are "10-year notes issued Nov 2023-Nov 2031; future issuance UNVERIFIED" (RM:47, :276) | — | Treasury auction data: **Nov 2033 4.500% (91282CJJ1), Nov 2034 4.250% (91282CLW9) and Nov 2035 4.000% (91282CPJ4) already exist**. **Nov 2036, 2037 and 2038 do not exist yet.** Nov 2039, 2040 and 2041 exist as 30-year bonds (the held issues) plus 20-year bonds 1.375% Nov-40 and 2.000% Nov-41 | **PARTLY WRONG** (§2.3) |
| 18 | The iBond coupon bug biases 1R vs 3r? (task item 4) | not assessed | Fixed vs bugged: 1R 1.31% vs 1.20%; 3r 0.17% vs 0.15%; BOTH 0.22% vs 0.19%. Top-reach −0.8 points for both | **No material bias**. It flatters all three by similar amounts |
| 19 | The full form's cheapness is a 0% artefact (RM:27, :185-190) | — | Full sells the whole Feb-37 and May-38 positions in every case (60-64% turnover) | CONFIRMED |
| 20 | Buy-only keeps "held to maturity", 1-2 trades (RM:180) | — | 1 trade (more Nov-41), 2 when yields fall (adds Nov-40). With no new notes allowed it costs ≤$0.5k more | **CONFIRMED** |

---

## 2. Audit of `rematch_lp.py`, line by line

### 2.1 What is right
- **Windows** (`bucket`, LP:74-77). A flow at time t goes to the first 1 Jan payment on or after it. So cash waits less than a year: IBTO's 15 Dec 2033 flow pays 2034, and Feb-37 waits 10.5 months for 2038. The assert keeps every flow inside 2033-2042. Correct.
- **Balance equation** (LP:217-225). Inflow plus earlier surplus, minus surplus carried forward, equals $50,000. Carry is ≥ 0 and grows at 0%. Correct and conservative.
- **Objective** (LP:226). Buys are paid at price × (1 + 0.10%); sales are received at price × (1 − 0.10%). Buying and selling the same bond at once never pays, so the LP cannot churn.
- **Bounds** (LP:233-234). Sales are capped at the holding, including the reinvested part z. Buy-only and trim are enforced through `sell_ok`.
- **No arbitrage.** Every instrument is priced off one discount curve (LP:178-185). Waiting cash earns 0%, below every forward rate (the floor is 0.25%), so the LP cannot create money.
  - Their lower-bound check passes (`verify_lp_out.txt`).
  - My own date-by-date replay of my LP solutions never falls below $0.00 after any payment, on 20,000 paths × 2 dates.
- **The 2033 gap** (LP:204). IBTM's shortfall or surplus against the 2033 payment is cash, at 0% from 15 Dec. Correct.
- **Tickets and bid-ask** (LP:240-241). $10 per bond, $25 per fund, ignored below $100. The ticket sizes are a WInS-like proxy, not Laura's broker (UNVERIFIED, as RM says). Bid-ask at 0.50% adds only about $40 to buy-only. Immaterial.

### 2.2 Problems (none of them flips the verdict)

**(a) The book flatters the LP by ~$1.8k at the median (LP:150-161, the "lump").**
- Pre-2033 coupons are booked as one amount A, paid at maturity: `face × Σ c/2 × (1+r/2)^(2(T−t))`.
- That formula assumes the reinvested money's own later coupons are reinvested at the locked rate r **after 2033 as well**. The study engine uses the same convention (CO:146-149). There it is harmless, because everything is reinvested anyway.
- Inside a re-match whose rule is "nothing is reinvested after 2033", it is a hidden reinvestment credit.
- Booked as what really happens (extra bonds whose post-2033 coupons wait at 0%), my LP costs more:

| Shift | −3 | −2 | −1 | 0 | +1 | +2 |
|---|---|---|---|---|---|---|
| Extra cost, buy-only, no round-up, 16 Oct | +$0.6k | +$1.0k | +$1.3k | +$1.75k | +$2.1k | $0 |

- Trim and full move by only $0.03-0.24k, because they sell the funds that carry most of the extra bonds.
- In the MC (units book), buy-only need rises from $5.9k to $7.7k at the median.
- **This does not create a real shortfall.** In 2033 the re-match would be computed from the actual holdings, so it would size the extra bonds correctly. The error is only in the modelled cost, and so in the minimum-breach and top-reach numbers. 1R's breach rate rises from 1.31% to 1.65%. BOTH's top-reach falls from 79.5% to 75.8%.

**(b) The iBond coupon bug is copied (LP:143).** `cpn = ... else ytm` makes IBTO-IBTR (and IBTM, through D0) pay their yield rather than the coupon they were sized on. That is the same flaw as CO:141. See §4.

**(c) The round-up is counted as a 2033 cost (LP:245-251).**
- Buys are rounded up to $1,000 face. The extra cost is added to the 2033 need, and the extra face is credited to Laura in 2042 at 0% (`round_back`).
- That is money moved from the gift side to Laura, not money lost.
- It adds $0.1-1.3k to buy-only and about $2.2k to trim at unchanged yields: trim's no-round-up cost is $0.5k, against $2.7k with it.
- So trim's quoted "+$0.4k premium" is mostly round-up. A smaller increment (Treasuries trade in $100 face at TreasuryDirect; broker minimums are UNVERIFIED) would make trim look cheaper still.

**(d) After-2033 waiting cash at 0%: the right sizing rule, but used unevenly.**
- Correct for certainty: the re-match must work even if T-bills pay nothing.
- But the same 0% is then used to measure **Laura's 2042 money** under 1R and BOTH (RT:202, :228). Under 3r that money comes from bonds whose coupons are reinvested at market yields (CO:152 `ladder_delivery`), plus a reserve that keeps its Nov-41 yield to 2041 (RT:274).
- Under BOTH, the unused reserve is even turned into 0% cash (RT:228 `+ Bleft`) instead of staying in the bond.
- That asymmetry is most of the "−$13k" (row 14).

**(e) Instrument universe B.** The LP may buy "new" par notes maturing 15 Nov 2033-2041. Buy-only uses them only in falling-rate paths (one Nov-40 note). Barring them costs ≤$0.5k (19 Oct, −2 points). Trim and full rely on **Nov-2037 and Nov-2038 notes, which do not exist yet** (§2.3).

**(f) Selling the reinvested part as a zero** (z variables, LP:206, :226). In trim and full mode the lump is sold at the zero-coupon discount factor. The real asset is extra coupon-bond units. This is consistent within the model but not an instrument Laura could sell separately. Small.

**(g) A simplification the team could use.** Under BOTH, buy-only usually means "sell part of the Nov-41 reserve, then buy more Nov-41". That is a round trip in the same bond (the bond the study's own option 3a also uses). In practice it is **re-labelling reserve bonds as ladder bonds**: no trade, no bid-ask, no ticket. Only the release to the gift is a sale. This is an insight for the team's Final Report, not a number to quote.

### 2.3 Do the instruments exist? (Treasury auction data)
Source: Treasury's auction dataset, which also feeds TreasuryDirect's auction history. Fetched 19 Oct 2026 23:46 UTC (20 Oct Sydney). Base URL: `https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query`, filtered by `maturity_date`. Raw JSON is in `verify_rematch/web/nov15_20xx.json` and `mat_2036_2038.json`.

| Matures 15 Nov | Exists today? | Issue |
|---|---|---|
| 2033 | **Yes** | 4.500% note, CUSIP 91282CJJ1, 10-year auctioned 8 Nov 2023 |
| 2034 | **Yes** | 4.250% note, 91282CLW9, auctioned 5 Nov 2024 |
| 2035 | **Yes** | 4.000% note, 91282CPJ4, auctioned 12 Nov 2025 |
| 2036 | **No** | Due from the Nov 2026 10-year auction, not yet in the data (the latest scheduled auction is 22 Oct 2026). 2036 maturities that do exist: Feb (4.500% bond and 4.125% note), May 4.375%, Aug 4.625%, plus the inflation-protected Jan and Jul notes |
| 2037 | **No** | Only Feb-37 4.750% (held) and May-37 5.000% exist. A Nov-37 needs the Nov 2027 auction (UNVERIFIED, routine) |
| 2038 | **No** | Only Feb-38 4.375% and May-38 4.500% (held) exist. A Nov-38 needs the Nov 2028 auction (UNVERIFIED) |
| 2039 | Yes | 4.375% bond 912810QD3 (held) |
| 2040 | Yes | 4.250% 912810QL5 (held); 1.375% 20-year bond 912810ST6 |
| 2041 | Yes | 3.125% 912810QT8 (held); 2.000% 20-year bond 912810TC2 |

**Two consequences:**
- **Buy-only needs nothing new.** It buys the held Nov-41 and Nov-40, which exist and are WInS-listed holdings.
- **Trim and full depend on future auctions.** They need Nov-37 and Nov-38 notes, which do not exist yet. And under the 6 Oct rule that the real plan may use only WInS-listed securities (`/home/user/snap/main/COMPETITION.md:86-89`), they would have to be WInS-listed as well. WInS lists no Treasury maturing Feb 2031-Feb 2036 (`COMPETITION.md:93`).
- So the 2033-2035 notes, though real, are not WInS-eligible today. That is one more reason to reject trim and full.

---

## 3. Independent checks

### 3.1 Deterministic table: my LP on T1 holdings (shift in Feb 2027, permanent)
Inputs:
- Holdings: faces, coupons and own yields from T1 (`oct20/reserve/reserve_schedule.md:72-85` for 19 Oct; `oct20/reserve/out16/tables.md:1-14` for 16 Oct).
- Every T1 cost is reproduced from the sizing rule 50,000 / (1+y/2)^(2T): totals $300,174 and $298,446, each rung within $2.
- 2033 pricing is by each instrument's own yield to maturity. Theirs uses a bootstrapped curve.

16 Oct curve, with round-up, as their table (the 19 Oct curve is within $0.15k for buy-only and trim):

| Shift | Frozen (patched) | Buy-only | Trim | Full | Buy-only, units book | Buy-only, units, T-bills at 4.27% + shift − 0.09% fee |
|---|---|---|---|---|---|---|
| −2 | $19.4k | $20.6k (2 trades) | $20.2k (9) | $19.0k (11) | $21.6k | $16.6k |
| −1 | $10.0k | $13.5k (2) | $11.0k (9) | $8.9k (11) | $14.3k | $7.7k |
| 0 | $0 | $6.0k (1) | $2.7k (9) | $0.8k (11) | $7.7k | **$0** |
| +1 | $0 | −$0.4k (0) | −$5.7k (8) | −$7.6k (11) | +$2.0k | −$0.4k |
| +2 | $0 | −$0.7k (0) | −$13.7k (8) | −$14.5k (11) | −$0.7k | −$0.7k |

Sources: `data/my_lp_det.json`, `data/bugcheck_out.txt`, `data/noround_out.txt`.

**Reading:**
- Their table holds within $0.15k for buy-only once the bug is accounted for.
- For a realistic book with waiting cash at today's T-bill rate, the "insurance premium" at unchanged yields vanishes. The units book matches their lump/0% cost at a waiting-cash rate of only **0.1-0.9%**.

### 3.2 Small independent Monte Carlo (`my_mc.py`, 20,000 paths)
Design:
- My own random numbers and code.
- The study's shared assumptions: 1.0 point a year random walk with a 0.25% floor; VT at 7% compound, 16.78% volatility, 0.06% fee; correlation 0.
- The plan rules as RT `run2` (3r: $10k Nov-41, top +$5k, release above need + $5k; 1R: minimum −$10k; BOTH: as RT:206-229).
- The re-match is my buy-only LP per path, at both the 2033 and the 2031 projection.

| Run | Premium p50 / p95 | 3r short / below min / top-reach | 1R below min | BOTH short / below min / top-reach | Laura 2042 p50, 3r vs BOTH: 0% (theirs) → reserve kept → fair T-bills |
|---|---|---|---|---|---|
| 16 Oct, seed 11 | $2.15k / $5.83k | 0.10% / 0.17% / 71.4% | 1.31% | 0% / 0.22% / 79.5% | $22.1k vs $9.5k → $14.0k → **$30.5k vs $28.6k** |
| 16 Oct, seed 23 | $2.12k / $5.81k | 0.085% / 0.17% / 70.8% | 1.26% | 0% / 0.23% / 79.1% | $22.2k vs $9.3k → $14.0k → $30.7k vs $28.6k |
| 19 Oct, seed 11 | $2.16k / $5.86k | 0.08% / 0.14% / 72.5% | 1.20% | 0% / 0.19% / 80.7% | $23.2k vs $10.4k → $15.4k → $32.1k vs $30.3k |
| 16 Oct, units book | **$4.00k / $7.53k** | same as above | **1.65%** | 0% / 0.26% / **75.8%** | $22.1k vs $7.6k → $11.4k → $30.5k vs $28.5k |
| 16 Oct, bug copied | $2.04k / $5.82k | 0.10% / 0.15% / 72.2% | 1.20% | 0% / 0.19% / 80.3% | $22.7k vs $9.9k → $14.6k → $31.3k vs $29.4k |

Sources: `data/mc_summary.txt` and `data/mc*.json`.

**Why 1R hurts the minimum** (`data/mech_out.txt`).
- 220 of the 262 1R breaches happen in the 12% of paths where yields have fallen more than 3 points by 2033. In those paths the re-match need is about $27k, and Laura's VT is $18k against a $43.6k median, so her half cannot cover the need.
- RM's explanation (the top-up "is drawn from Laura's stock half first", RM:94) names the trigger but not the difference. 3r also draws on Laura's half, but only after its reserve.
- The $10k reserve bought in 2028 is worth **$13-16k in 2033**: five years of locked interest, plus a price gain exactly when yields have fallen. 1R's extra $10k of floor is worth $10k.
- On top of that, 1R pays the re-match premium. So 3r's cushion is about $6-7k larger in the paths that matter.
- Cutting 1R's minimum does not close the gap:

| 1R minimum cut | $0 | $5k | $10k | $15k | $20k | $25k | 3r |
|---|---|---|---|---|---|---|---|
| Gift below the minimum | 2.89% | 1.94% | 1.31% | 0.86% | 0.53% | 0.33% | 0.17% |

- **Conclusion:** a reserve set aside early is worth more than the same dollars added to the floor.

---

## 4. The iBond coupon bug (CO:141, copied at LP:143): does it bias 1R against 3r?
- **Mechanism.** The funds are sized at their par coupon (about 4.94-5.12%) but paid their yield (about 4.98-5.15%). They over-deliver about $580 in total on plan (`verify_infl_num.md:28`).
  - The LP's book copies it: post-2033 fund coupons are also paid at the yield, so the existing flows are overstated in the windows too.
- **Size.**

| | Bug effect |
|---|---|
| Deterministic, buy-only | −$0.1k |
| Deterministic, trim | −$0.55k |
| Deterministic, full | −$0.7k |
| Frozen estimate | −$0.5k |
| MC, 2033 need, median | −$0.36k |
| MC, premium | −$0.1k |

- **Bias between options: none that matters.**

| | Fixed | Bugged |
|---|---|---|
| 1R below the minimum | 1.31% | 1.20% |
| 3r below the minimum | 0.17% | 0.15% |
| Ratio 1R / 3r | 7.7× | 8.0× |
| BOTH below the minimum | 0.22% | 0.19% |
| BOTH top-reach | 79.5% | 80.3% |
| 3r top-reach | 71.4% | 72.2% |

- The bug flatters every option by about the same amount and changes no ranking.
- **Fix:** patch LP:143 the same way as CO:141 (pay the sizing coupon) before any number is quoted. Expect each option's minimum breaches to rise by about 0.02-0.1 point.

---

## 5. Against the agreed basis (`reconcile_3r.md` §5): should BOTH's advantage grow or shrink?

The agreed basis is engY pricing, the plan read literally, and the 19 Oct curve. On it, option 1 is 14.5% short, 3r is **0.6% short (worst about $3.3k)**, 3r-fixed reaches the top in 76%, and the gift is below the minimum in 0.01-0.04% of paths for every option. I did **not** run BOTH on engY. The direction below is reasoned from the mechanisms, and every level is UNVERIFIED.

| Measure | Study engine (RM and mine) | Expected on the agreed basis | Why |
|---|---|---|---|
| **Payments short, BOTH vs 3r** | 0% vs 0.02-0.10% | **Advantage GROWS**: about 0% vs 0.6% | On that basis 3r's shortfalls come from yield falls *after* 2033 (`reconcile_3r.md`, banner point 6). A 2033 re-match removes exactly that risk. Exception: if the team reads V5 as keeping Laura's retained half on call after 2033, 3r falls to about 0.07% (banner point 2) and the gain is small again |
| **Gift below the minimum** | BOTH ≈ 3r (+0.05 point); 1R 8× worse | **Gap SHRINKS in absolute terms.** BOTH ≈ 3r; 1R still worse, but at a much lower level | The literal cover order spends Laura's half and any VT above the cap before the gift above the floor, so every option sits near 0.01-0.04% |
| **Top-reach, BOTH vs 3r-fixed** | +8 points (+4 on the units book) | **Probably SHRINKS** | 3r-fixed already reaches 76% there. The gain comes from swapping a $5k guessed margin for an exact need that costs $2-4k, so at most a few points remain. The agreed basis's reach figures also hang on two conventions (verify_reconcile, banner point 1) |
| **Laura's 2042 money** | −$13k as RM books it; about −$2k with fair crediting | **About −$2k if credited fairly; worse if not** | The agreed basis counts T-bill interest on waiting cash as it actually arrives. Leaving BOTH at 0% there would make the asymmetry larger |
| **Re-match premium** | +$2.1k median (+$4.0k units book) | About the same order; its upper tail is UNVERIFIED (0% yield floor) | RM's roll-down sensitivity gave the same +$2.2k. The agreed basis's 0% yield floor allows deeper falls, so larger 2033 needs in the tail |

**Bottom line:** on the agreed basis the case for BOTH over 3r gets **stronger on payments**. It probably gets weaker on top-reach, and its cost to Laura stays small if credited fairly. Before any of this is quoted, the LP must be run inside engY, with the units book and the coupon fix.

---

## 6. Conclusions safe for the 27 Oct vote
1. **A once-only, buy-only 2033 re-match makes every remaining payment independent of reinvestment.** It needs 1-2 orders in existing, held, WInS-listed bonds (Nov-41, sometimes Nov-40), and nothing is sold. Confirmed independently.
2. **1R alone is weaker than 3r for the 2031 minimum**, about 8 times as many breaches in this model. A $25k cut in the minimum still does not close the gap. Confirmed. The cause is that 3r's reserve is pre-funded and grows. "Laura's half first" is only the trigger.
3. **BOTH (3r reserve + buy-only re-match) is the strongest of the three on payments.** It keeps the minimum about as safe as 3r (about 0.05 point worse) and reaches the top more often: +8 points on the study's book, about +4 on a realistic book.
4. **The re-match is a worst-case reserve, not money spent.**
   - It costs about **$2-4k at the median** in 2033 (up to $6-8k in a bad 1-in-20 case) if waiting cash earns nothing.
   - With T-bills at today's rates most of it comes back as interest by 2042.
   - Laura's 2042 money under BOTH is about **$2k** lower than under 3r when both are credited the same way. **Do not quote "$13k" or "$8k in 2033 money".**
5. **Reject the full form**, and the trim form too. Full sells about 60% of the book; trim sells parts of four funds. Both depend on Nov-2037/2038 notes that do not exist yet and are not WInS-listed.
6. **Do not quote** "0.02% vs 0%" as the payment gap. On the agreed basis it is about 0.6% vs about 0% (UNVERIFIED for BOTH). On the study engine it is 0.02-0.10%.

## 7. What must change in RM before it is reused
- Replace RM:22, :97 and :250 ("−$13k", "$8k in 2033 money") with "about $2k with waiting cash credited at T-bill rates for both options; $13k only if BOTH's cash earns 0% while 3r's reinvests".
- Replace RM:191 with: "Buy-only's trades do not depend on the 0% artefact, but its cost does. At today's T-bill rates the top-up at unchanged yields is about $0."
- Add the units-book range: premium +$2-4k median, +$6-8k 1-in-20. BOTH's top-reach is 76-80%.
- Correct RM:47 and :276 using the §2.3 table: Nov-33/34/35 already exist; Nov-36/37/38 do not yet.
- Patch LP:143 (coupon fix). Stop counting the round-up as a 2033 cost, or say that it is money moved, not lost.
- "BOTH: same minimum protection" should read "about 0.05 point more breaches than 3r".

## 8. What this teaches (for Ray)
- **Check what an optimiser is allowed to assume about cash.**
  - At 0% interest, any "lock it in" plan looks expensive.
  - At a realistic rate the same plan is nearly free.
  - Both views are correct: one sizes a guarantee, the other estimates what really happens. Say which one a number is.
- **Compare like with like.** One option's money was counted at market yields, the other's at 0%. That alone made a $2k difference look like $13k.
- **Money set aside early beats the same money promised later.** The 2028 reserve has five years to earn interest, and it gains exactly when yields fall. That is why 3r protects the minimum better than a bigger floor does.

## 9. Limits and UNVERIFIED
- **Same model family as the study.** That covers parallel moves only in my MC, iBond funds as par bonds, lognormal stocks, and no taxes. The bootstrap and history runs were not repeated.
- **My MC** uses 20,000 paths, about ±0.1 point on the 1R breach rate and ±0.05 on 3r.
- **My 3r reserve valuation** is market-based, so 3r's payment shortfall is 0.08-0.10%, not 0.02%.
- **UNVERIFIED:**
  - future Nov-36/37/38 auctions;
  - WInS listing of any security in 2033;
  - retail bid-ask and minimum increments;
  - Laura's broker fees;
  - every agreed-basis figure for 1R and BOTH (not run in engY).
- **The fair-T-bill comparison** credits waiting cash at the 3-month par yield plus the path's shift, less a 0.09% fund fee. It changes no plan rule; it only measures Laura's money.

## 10. Reproduce
From `oct20/verify_rematch/scripts/`, with `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I`:
- `my_lp.py ../data/my_lp_det.json`: the T1 checks and the deterministic table, in both book conventions, with carry, no-new-notes and bid-ask variants.
- `bugcheck.py`: the bug reproduction against their table, trade lists and break-even carry (`../data/bugcheck_out.txt`).
- `noround.py`: costs without the round-up (`../data/noround_out.txt`).
- `my_mc.py "16 Oct" 20000 11 ../data/mc16_s11.json [units] [bug]`: about 70 seconds on 4 cores (summary in `../data/mc_summary.txt`).
- `mech.py`: the minimum-cut sweep and breach anatomy (`../data/mech_out.txt`).
