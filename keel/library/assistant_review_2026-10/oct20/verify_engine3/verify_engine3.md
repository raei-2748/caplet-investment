# verify_engine3: adversarial check of engine_v3 (the coupon-cover vote engine)

AI-generated verification by Claude Code for Team Caplet, 20 Oct 2026 (Sydney). These are MODEL numbers for research only. They are not text to submit. If the team uses any of them, log it in the AI-use record and later in the Final Report's Works Cited.

`S/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/`. `E/` = `S/oct20/engine_v3/`. `W/` = `S/oct20/verify_engine3/`; my working copy of the engine is in `W/work/` (E/ was not edited). Scope follows the coordinator's note: I did not redo what `S/oct20/verify_vote2/verify_vote2.md` §2 already did (the seed-7 legacy check, the 12 fresh MC runs, and the §5c, $15k and "0.06%" over-statements).

## 0. Verdict: SOUND on payments. One convention moves BOTH's top-reach below 3r-fix. One framing error. Small wording fixes.
1. **Legacy check.** I re-ran `check_legacy.py 20261019 100000`. The maximum path-level difference against engY is 0 on all 12 lines, and the maximum difference against the agreed JSON is 0. The history replays match. The output is byte-identical to E/'s log (`W/check_legacy_seed20261019_100k.txt`).
2. **F2 (the 0.07% fund fee) is right.**
   - **+$848 confirmed:** at zero shift the ladder costs $299,861 with the fee switch off and $300,709 with it on (`W/zero_shift.py`).
   - **engY's fee really was free.** With the fee set to 0% the ladder costs $299,866, so engY's version cost −$5.
   - **My own cash-flow code** (`W/fee_hand.py`; it uses only the treasury.gov row and the iShares coupon, maturity and fee, which I re-read: 0.07% on all five pages, WAC 3.50/4.04/4.12/4.28/4.35):
     - +$841 when the fee is charged as v3 charges it;
     - **+$931** when the fee is charged on all the money in the fund, including reinvested coupons (= verify_ldi_sens's $0.93k);
     - the rule of thumb (cost × 0.07% × years) gives $927.
   - So v3 is about $80 light, if coupons are reinvested in the fund. That is low severity.
3. **Buy-only LP and BOTH code: no bug found.** I checked the payment-window mapping, the surplus-carry equalities, IBTM's 2033 surplus and gap, the rounding up to $1,000 face, the under-$100 dust rule, the cost passing through the chain, BOTH's chain order (leftover, then reserve with no margin, then release up to the top), and the cache key.
   - **The 1.88% case** (sizing that counts the funds' bill interest to 15 Dec) **reproduces:** 1.93% at 20k paths, re-match cost median $5.55k.
   - **Costs are tiny.** Removing bid-ask and tickets changes the median re-match cost by only $22.
   - **But v3 has the same "lump" convention that verify_rematch §2.2(a) found in rematch_lp.py.** `hold_windows` (engine_v3.py:312-315) compounds the pre-2033 reinvested coupons to each bond's maturity as one zero-coupon lump. That is a hidden reinvestment credit after 2033.
   - **Booked as extra bond units** (whose post-2033 coupons wait at 0% in the LP and in T-bills in reality; `W/units.py`, 20k paths), the results change:
     - the re-match costs **+$1.9k at the median** ($8.5k → $10.4k) and +$1.2k at the 1-in-20 high ($26.0k → $27.2k);
     - **BOTH's top-reach falls from 77.3% to 73.0%**, below 3r-fix's 75.4%;
     - BOTH's gift median falls by $0.7k;
     - payments are still **0% short**.
     This is error #8.
   - **The 2042 money is credited fairly in v3.** BOTH's waiting cash earns T-bills (`gap_real` = bill), and 3r's reserve is marked at market. The nominal total of all of Laura's money is $2.5k lower for BOTH, which is the same as verify_rematch's fair −$2k. On the units book it is −$2.5k as well.
4. **The 1.8 vs 8.4 point gap is explained (§2).**
5. **Option 2 is not the D10 "retained half on call" reading (§3).**
6. **Clean on content.** There is no submission-ready TNA, IPS or Final Report prose. The personal-data scan found 0 hits in 61 files (tokens not printed).

## 1. Error table
| # | Location | Claim | Evidence | Severity | Exact fix |
|---|---|---|---|---|---|
| 1 | engine_v3.md §5e last bullet | "I have not split the difference… UNVERIFIED which rule drives it" | §2 below: on v3, 3r-fix with a $0 margin reaches the top in 85.8% of paths; BOTH whose LP counts the funds' bill stretch reaches 82.0% | Medium (open item) | Replace with: "The driver is BOTH dropping 3r's $5k margin. BOTH gains top-reach only where the re-match premium over the projected need is below $5k: 63% of paths on v3, 92% if the LP counted the funds' bill stretch. v3's premium is larger because its iBond model has a mid-year-to-15-Dec bill stretch that the 0%-sizing LP does not count. The red-team engine has no such stretch (its funds are par bonds ending 15 Dec). Counting it lifts BOTH's gain to +6.6 points; the remaining ~1.8 points are engine-basis differences (UNVERIFIED split)." |
| 2 | Option 2 row (§2 table) and master_playbook.md:269 "(= D10 option 10b)" | Option 2 = the "retained half on call" reading | §3: on the same v3 paths, VREC's 10b reading gives 1.59% (1.56%) short, worst $6.8k ($7.1k); option 2 gives 0.82%, worst $12.2k | Medium (framing) | Call option 2 "10b, stock form: the 2033 need itself is left in VT". Quote 10b as VREC defined it as "option 1 about 1.6% (worst about $7k); 3r about 0.1%" on v3 |
| 3 | §3 "Size of the fee fix" / §8 Fees | +$848; "fee charged on the coupons received, not on income already reinvested" | `W/fee_hand.py`: $841 (v3 method) vs $931 (fee on all money in the fund, if coupons are reinvested in it) | Low | Write "+$0.85-0.93k, depending on whether reinvested coupons stay in the fund". Ladder $300.7-300.8k |
| 4 | §5e "What the rows show", bullet 1 | "The rest is bid-ask, tickets and rounding" | The no-cost run moves the re-match cost by $22. Rounding comes back as later cash | Low | "The rest is the re-match premium: it sizes post-2033 cash at 0%, without the funds' bill stretch. Bid-ask and tickets are about $20." |
| 5 | §5c table | "Median" left blank for the $135k step | 51.3% of paths are at ≥$135k. On the 16 Oct curve the CSV gives a 3r median minimum of **$130k** (mc_16oct rows) | Low | Add: "3r's $135k is also a knife-edge (51%). On the 16 Oct curve its median is $130k." |
| 6 | §2 "1 Jan 2031 range" and §4 "Not changed" | Minimum = 98% of projected floor (range-audit rule) | The team's documents use **(R − $3,700) rounded down to $5k**: `S/oct20/numbers/numbers_refresh.md:143`, `S/oct19/coupon/coupon_risk_options.md:29`, `S/oct20/votepack/votepack.md:273` | Low (labelling) | State: "The canonical runs use the range audit's 98% rule. The team's documents freeze R − $3,700. Under that rule (sens row) option 1's median is still $140k; only 4 and 1R tip to $145k." See also verify_vote2 V4 |
| 8 | engine_v3.py:312-315 (`hold_windows`); §0 item 3, §5e | BOTH reaches the top in 77.3% of paths (+1.8 points over 3r-fix); re-match median $8.5k / 1-in-20 $26.0k | `W/units_20k.txt` (20k paths, seed 20261019). Units book: cost $10.4k / $27.2k, top-reach **73.0%** against 3r-fix 75.4%, still 0% short. Same flaw as verify_rematch §2.2(a) | **Medium** (it flips "BOTH beats 3r-fix on top-reach") | Book pre-2033 coupons as extra units: my patch in `W/work/scripts/engine_v3.py` (switch `bo_units`, plus the cache key). Re-run the `bo` suite at 100k × 2 seeds. Until then, quote BOTH's top-reach as "about the same as 3r-fix (73-77%)". The engine-wide lump (used in `value_at`, for every option's reinvestment) is untested on 3r/option 1: UNVERIFIED |
| 7 | engine_v3.py:649-651, 727-737 (option 2) | Above-cap money is held in VT to 2042 | `overflow` is floor or gift money above the cap, yet it is grown at VT returns after 2033 | Low | Hold the overflow at bills or 0% under option 2, or note it. It affects only option 2's tails and its 2042 return |

## 2. Why BOTH adds 1.8 points on v3 but 8.4 on the red-team engine
Run: `W/both_gap.py` (20,000 paths, seed 20261019, 19 Oct curve, v3 basis); output in `W/both_gap_20k.txt`.

| Case | Short | Top reached |
|---|---|---|
| 3r-fix (v3) | 0.73% | 75.4% |
| 3r-fix with a $0 margin | 1.21% | **85.8%** |
| BOTH (v3) | 0.00% | 77.3% |
| BOTH, LP counts the funds' bill stretch | 1.93% | **82.0%** |
| BOTH, no bid-ask or tickets | 0.00% | 77.4% |
| BOTH / 3r-fix, no top rounding | 0.00% / 0.73% | 75.4% / 72.8% |

**The mechanism.**
- 3r-fix keeps (projected need + $5k) in the reserve. BOTH keeps the buy-only re-match cost and releases the rest.
- So BOTH releases more, and reaches the top more often, only where the re-match premium over the projected need is under $5k.
- On v3 that premium has median **$3.8k** (p25 $1.4k, p75 $6.2k) and is above $5k in 37% of paths. If the LP counts the funds' bill interest, the median is $1.6k and only 8% of paths are above $5k. That is the red-team picture: there, the premium over the frozen estimate was +$2.1k median.
- Top rounding is not the driver: without it, the gap widens slightly, to 2.6 points.
- **One plain-English rule drives it: the safe (0%) sizing of the funds' last months.** That sizing is the price of BOTH's 0% short.
- **The lump convention adds to this** (error #8). Booking pre-2033 coupons as extra bonds raises the premium by a further $1.9k at the median. That takes BOTH's gain to **−2.4 points** (73.0% against 75.4%) on v3. On the red-team engine verify_rematch found +4 points (75.8% against 71.4%).

## 3. Option 2 vs D10's "retained half on call"
VREC's 10b (`S/oct20/verify_reconcile/vr_engine.py:350-371`) keeps the 2033 chain unchanged: the projected need is set aside in cash from her half, and only what is left (plus the unused leftover) stays in VT, drawn last. v3's option 2 sets nothing aside: the whole half stays in VT, and the gift is cut only for need beyond its 2033 value.

I added the 10b reading as a switch to my copy (`W/work/scripts/engine_v3.py`, `oncall10b`) and ran it on the same v3 paths (`W/d10.py`, 100k paths, seeds 20261019 and 7; output in `W/d10_out.txt`):

| Plan | Short | Worst | Laura's 2042 return (median) |
|---|---|---|---|
| Option 1, half free after 2033 (10a) | 14.79% (14.66%) | $10.1k | $8.8k |
| **Option 1 + 10b (VREC reading)** | **1.59% (1.56%)** | $6.8k ($7.1k) | $60.3k |
| Option 2 (v3) | 0.82% (0.83%) | **$12.2k ($12.9k)** | $56.3k |
| 3r + 10b | 0.09% (0.08%) | $1.8k ($2.2k) | $66.0k |
| 3r-fix + 10b | 0.08% (0.07%) | $1.8k ($2.2k) | $71.7k |

**The difference.** Option 2 leaves even the projected need in stocks. That makes shortfalls rarer (the stocks usually grow) but larger in crashes ($12-13k against $7k). v3 reproduces VREC's ≈1.4% (1.47/1.38% on VREC's own paths) as about 1.6% under the 10b reading. Both figures are model-specific.

## 4. Canonical numbers I confirm (19 Oct curve)
- **Legacy equals engY:** seed 20261019 at 100k paths, difference 0. Seed 7 was done by verify_vote2.
- **Ladder:** $300,709 with the fee; $299,861 legacy.
- **BOTH and 1R buy-only:** 0.00% short on both books. The re-match needs 1 buy at the median and at most 4.
  - Lump book (as published): BOTH reaches the top in 77.3%, against 75.4-75.5% for 3r-fix; the re-match costs a median $8.5k.
  - Units book (more realistic): top-reach 73.0%; the re-match costs $10.4k / $27.2k (20k paths, seed 20261019).
- **If the sizing counts the funds' bill interest:** about 1.9% short.

## 5. What the team can quote safely (plain English, with conditions)
- "Charging the iBond fund fee properly adds a little under $1,000 to the ladder."
- "A 2033 top-up purchase that sizes everything at 0% interest removed every payment shortfall in our model runs. It needs one to four extra Treasury purchases in January 2033, typically about $8,500 to $10,500. Most of that money comes back later as interest."
- "With the top-up, the gift reaches the top about as often as with the reserve alone (roughly 3 times in 4)."
- "Whether Laura's kept half stays on call after 2033 changes the no-cover baseline from about 1 in 7 to about 1 in 60 to 1 in 70." Quote this with the reading stated.
- **Do not quote** "BOTH lifts top-reach by 8 points", or any top-reach gain at all. On this engine it is +1.8 points on the lump book and −2.4 points on the units book.
- **Note on the 2033 purchases:** verify_rematch §2.3 found that the 15-Nov notes for 2036-38 do not exist yet, while v3 assumes par notes for every 15 Nov from 2033 to 2041. Routine issuance is UNVERIFIED.
