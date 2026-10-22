# engine_v3: one corrected engine and one results table for the 27 Oct coupon-cover vote

> **Verified 20 Oct (`oct20/verify_engine3/verify_engine3.md`): sound on payments (no bug changes any shortfall figure); legacy check exact; fee fix +$0.85-0.93k.** Medium: the buy-only LP books pre-2033 coupons as a compounding lump (`hold_windows`, :312-315); booked as bond units, the re-match costs a median $10.4k (1-in-20 $27.2k) and **BOTH reaches the top in 73.0%, below 3r-fix 75.4%**: never quote a top-reach gain for BOTH; say "about the same as 3r-fix (73-77%)". Option 2 is NOT the D10 on-call reading: on-call gives option 1 ~1.6% short (worst ~$7k). The team documents use the (R - $3,700) minimum rule; 3r's $135k is also a knife-edge. 2042 money: BOTH ~-$2.5k vs 3r-fix (fair crediting).

AI-generated research by Claude Code for Team Caplet, Tue 20 Oct 2026 (Sydney). Every number here is MODEL output from code an AI wrote, and no student has rebuilt any of it. None of it is text to submit. If the team uses a number, log it in the AI-use log and later in the Final Report's Works Cited (Wharton AI policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). This file contains no drafted IPS, TNA or Final Report prose.

**Short forms.** `E/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/engine_v3/`. `S/` = the scratchpad folder above `oct20/`. `CO` = the coupon study `S/oct19/coupon/scripts/coupon_options.py` (copy in `E/ref/`). `engY` = `S/oct20/reconcile3r/scripts/engY.py` (copy in `E/ref/`). `v3` = `E/scripts/engine_v3.py`. Seed 20261019 comes first; seed 7 follows in brackets.

## 0. Summary in five lines
1. **One engine, checked against the old one.** v3 is engY with every listed fix, new options (2, 3a, 3b, 4, 1R, and the buy-only 1R and BOTH) and curve twists, each behind a switch. With the fixes switched off it reproduces reconcile3r's agreed numbers exactly: path-level difference 0 on 100,000 paths × 2 seeds × 12 cases, plus all four history replays (`E/data/check_legacy_seed*.txt`).
2. **Only one fix moves the numbers: the 0.07% iBond fee.** engY's fee cost almost nothing, because it took the fee off the price as well. Charged properly, the ladder costs **$300.7k on 19 Oct** (P > $300k = 52%). Option 1's chance of a short payment goes from 14.5% to 14.8%. 3r is unchanged at **0.62% (0.65%)**, worst $3.3k. The median minimum falls to $140k for options without a reserve, but that median is a knife-edge (section 5c).
3. **Canonical result (19 Oct, 100k × 2 seeds).** Chance of a short payment:
   - option 1: 14.8%;
   - option 2: 0.8% (worst $12k);
   - 3b: 3.9%;
   - 3a / 3r / 3r with the top fix: 0.6% (worst $3.3k);
   - 3r $15k: 0.03%;
   - option 4: 0.13% (worst $0.3k);
   - 1R: 0% (idealised re-match).
   
   Gift reaches the top: 3r as written 44.5%; the top fix 75.5%; options 1, 3a, 4 and 1R 77-79%.
   
   **Added at the coordinator's request:** the buy-only 2033 re-match on this basis (section 5e).
   - 1R buy-only and BOTH (3r top fix + buy-only re-match): **0.00% short** in every run (MC, history, twists, bootstrap), provided the re-match counts the funds' last months in cash at 0%. If it counts that interest: 1.9% short, worst $2.8k.
   - BOTH reaches the top in 77.3% of paths. Its median gift equals 3r-fix's ($158k).
   - The re-match costs a median $8.5k (1-in-20 high $26k). It needs 1 buy at the median, 3 at the 1-in-20 high and at most 4.
4. **Robustness.** Real curve twists hurt 3r more than parallel moves do:
   - history replay with twists: 2.8% short;
   - block bootstrap with twists: 0.77-0.82%;
   - worst case $6.1-6.8k against $3.3k.
   
   Option 4 shows many tiny gaps with twists (1.8%, worst $1.2k). 1R stays at 0%. 3r $15k stays at or below 0.9% in every row except the no-floor bound.
5. **Timing matters, and the team should state it.** $10k in the Nov-41 bond covers about a **1.0-1.25 point** permanent fall that starts during 2027, and about **1.5-1.75 points** after the January 2028 purchases. In the Monte Carlo, 3r is short in 3.4% of paths with a ≥1-point fall in 2027 and 0.7% with the same fall after 2028. No 2028 reserve rule fixes the 2027 exposure, because the reserve does not exist yet. A 2033 buy-only re-match does fix it (BOTH: 0% in both cases, §5e).

---

## 1. Reproduce (one command)
```
sh /tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/engine_v3/scripts/run_all.sh
```
- It takes about 30 minutes on 4 cores, 20 of them for the buy-only re-match LPs. It needs about 3 GB of RAM (the twisted bootstrap at 100k paths).
- In order, it runs:
  1. the deterministic timing table;
  2. the two legacy checks;
  3. Monte Carlo on the 19 Oct curve (2 seeds) and on the 16 Oct curve;
  4. sensitivities;
  5. three history replays;
  6. two bootstraps (2 seeds, twisted and parallel);
  7. the buy-only re-match suite (`run_v3.py bo`, 2 seeds);
  8. the extras;
  9. `make_csv.py`, which writes `E/results_v3.csv` (228 rows: suite × scenario × seed × option).
- Python: `S/venv/bin/python -I`.
- Inputs:
  - `E/data/tsy_202610_reconcile3r.csv`: treasury.gov 2026 daily par curve, the same file reconcile3r used. Its 10/19/2026 row is identical to my re-fetch, `E/data/raw/tsy_202610_fetch.csv`.
  - FRED monthly TB3MS, GS1, GS3, GS5, GS10, GS20 and GS30: copies from `S/oct20/redteam3r/data/`. `fred_GS10.csv` is byte-identical to the range audit's copy.
  - Shiller monthly total-return index: byte-identical to the reconcile3r and range-audit copies.

**The 20 Oct curve.** It is not published yet.
- I fetched the treasury.gov October CSV (URL from `S/oct20/numbers/scripts/run_all.sh:7`) at 22:52 UTC on 19 Oct (`E/data/raw/tsy_202610_fetch_time.txt`). The latest row was 10/19/2026, because the US date was still 19 Oct.
- To re-run on 20 Oct, after about 22:00 UTC on 20 Oct US time:
  1. re-fetch that URL into `E/data/raw/`;
  2. run `run_v3.py mc SEED 100000 OUT.json <csv> 10/20/2026` for both seeds.
- The 16 Oct → 19 Oct comparison in section 6 shows how much one curve day moves the numbers.

## 2. The rules, in plain English (v3 basis)
Every rule is a switch in `v3 DEFAULT` / `AS_WRITTEN` / `V3` (`engine_v3.py:840-851`). The plan text behind each choice is `reconcile_3r.md` §3.

**Money in**
- $300,000 on 1 Jan 2027.
- $150,000 on 1 Jan 2028.
- Nothing else comes in.

**The ladder (1 Jan 2027)**
- Ten holdings, as the team's WInS book:
  - IBTM, IBTO, IBTP, IBTQ and IBTR for 2033-37;
  - T 4.750% Feb-37, 4.500% May-38, 4.375% Nov-39, 4.250% Nov-40 and 3.125% Nov-41 for 2038-42.
- **Rule (a), maturity sizing.** Each holding is sized so that, with its coupons reinvested in it at the yields of the day, it holds $50,000 when its money arrives. For an iBond fund that means:
  - its holdings mature mid-year (iShares weighted-average maturity);
  - the fund then sits in T-bills, less its fee, until 15 Dec.
  
  Interest earned between that date and the 1 Jan payment is **not** counted in the sizing. It really arrives, at the T-bill rate of the day, as a cushion.
- If the ladder costs more than $300k, the longest holdings are bought first. The missing near rungs are bought on 1 Jan 2028 at that day's prices.
- Any leftover sits in a Treasury to Dec 2032, as the first buffer.

**The iBond funds**
- Modelled from the iShares holdings data on 16 Oct 2026: weighted-average coupon and weighted-average maturity per fund. Source: `S/oct20/rangeaudit/data/web/p_*.html`.
- The management fee is **0.07% on all five pages**, which I re-read for this engine. The buyer pays the market value of the holdings and receives the coupons less the fee (fix F2).

**1 Jan 2028**
In this order:
1. top up any missing rung;
2. buy the reserve, if the option has one;
3. buy the floor: IBTM sized to pay back what is left of the $150k in Dec 2032;
4. put the rest in VT.

**1 Jan 2031 range**
- **Minimum** = 98% of the projected floor payout, less any projected shortfall that the leftover, the reserve and Laura's half cannot cover, rounded down to $5k.
- **Top** = projected floor payout + half of VT that day, less the same uncovered shortfall, rounded down to $1k.
- **3r adds to the top:** $10k as written; $5k with the top fix.
- **3a and 3b** do not add the reserve to the top.

**1 Jan 2033 gift**
- Gift = floor payout + half of VT (+ 3r's release), capped at the top.
- **Rule (b), the 2033 need.** The shortfall still projected (yields frozen that day) is measured **in dollars**. It is covered in this order:
  1. the 2027 leftover;
  2. the reserve, which keeps the need **plus $5k**;
  3. Laura's half, plus any money above the cap (fix F5);
  4. the gift above the floor;
  5. the floor.
- 3r's release only goes into the gift if it fits under the cap. Otherwise it stays in the reserve and returns to Laura in 2042.
- The unused 2027 leftover is released to Laura (fix F4).

**2033-2042 payments**
- Each payment is met from that rung's cash plus any surplus carried forward at T-bills.
- If that is not enough, the set-aside cover cash (held at 0%) is used next, then the reserve, sold at market.
- A payment counts as **short** if any single payment misses by more than $100 after all permitted cover.

**Laura's money**
- **"Laura's 2033 free money"** = what she can take out on 1 Jan 2033: unused leftover, her half of VT, money above the cap, and option 1R's re-match surplus, less what was set aside.
- **"2042 return"** = what is left after the last payment:
  - the carried surplus;
  - unused cover cash;
  - the reserve still held, at market;
  - (option 2) the VT she kept invested.

**Rates and stocks**
- **Rates:** the whole zero curve from the treasury.gov par curve of 19 Oct 2026 moves by a parallel random walk of 1.0 point a year. The move from 19 Oct to 1 Jan is included. Yields are floored at 0%.
- **Stocks:** VT at 7% compound, 16.78% volatility (JPM 2026 LTCMA AC World), 0.06% fee, correlation 0.

**The options** (`engine_v3.py:854-872`)

| Option | What it does |
|---|---|
| **1** | State the risk only. |
| **2** | Laura's half is *not* set aside in 2033. It stays in VT inside the portfolio to 2042 as the back-up. The gift is cut only for need beyond leftover + reserve + the half's 2033 value (study semantics, CO:247-250, 265-272). |
| **3a** | $10k of the 2028 deposit in the Nov-41 bond. Not in the top, no release, unused returns in 2042. |
| **3b** | The same $10k in IBTM, then T-bills after 2033. |
| **3r as written** | $10k in Nov-41, counted in the top at $10k, release above need + $5k. |
| **3r top fix** | The top counts $5k. |
| **3r $15k** | As written, $15k. |
| **4** | Dedicated ladder: the same ten holdings resized by a linear programme on 1 Jan 2027. Coupons before 2033 are reinvested in IBTM; later coupons wait for the next payment. Sized at 0% waiting, like rule (a). |
| **1R** | On 1 Jan 2033 the remaining ladder is sold at market and replaced by Treasury zeros maturing 15 Nov before each 2034-42 payment. Cost of the re-match = zeros − market value − the 2033 rung's surplus + 0.10% per leg, charged to the same cover chain. **Idealised:** WInS-type plans cannot buy STRIPS, so a real re-match would use coupon notes (see section 8). |
| **1R buy-only** | Added 20 Oct; the form recommended by `S/oct20/rematch1R/rematch_1R.md`. On 1 Jan 2033 nothing is sold. A per-path LP buys new Treasury notes maturing 15 Nov 2033-41 at a par coupon, or more of the five held T-bonds, so that the cash arriving in each payment window, carried at 0%, meets every 2034-42 payment. After that nothing is reinvested. The book's own coupons after 2033 wait for the next payment instead of being reinvested, and funds' bill interest to 15 Dec is **not** counted in the sizing. Costs follow rematch_1R.md: 0.10% bid-ask, $10 a ticket, buys rounded up to $1,000 face, buys under $100 ignored. The cost goes through option 1's chain. Unused cash returns in 2042. |
| **BOTH** | 3r top fix, plus the buy-only re-match **replacing** the "+$5k margin" release. The reserve pays the re-match cost after the leftover; whatever is left of it is released to the gift up to the top, and the rest to Laura in 2033 (rematch_1R.md:19). |

## 3. Validation (done first)
- **Legacy reproduces engY and the agreed numbers exactly.** `check_legacy.py` runs v3 with `fee_mode="coupon"` and the AS_WRITTEN rules (= reconcile3r `agreed.py` W) against engY on the same paths. It covers six rule sets × options 1 and 3r × 2 seeds × 100,000 paths.
  - Maximum path-level difference (miss, gift, top, bottom, Laura 2033, ladder cost, floor, VT): **0**.
  - Every statistic matches `reconcile3r/data/agreed_seed*.json`: maximum difference **0**.
  - 3r as written: 0.627% (0.646%). Option 1: 14.463% (14.350%). Range-audit rules: 6.066% / 32.106%.
  - The history replays also match: additive 18.31% / 1.02%; proportional 6.98% / 0.00%. Top reached 87.06% / 55.52% / 78.49%.
  - Output: `E/data/check_legacy_seed20261019.txt`, `..._seed7.txt`.
- **Path generators are identical** (engY vs v3: `True`).
- **The twisted history uses the same 688 windows** (Apr 1953 to Jul 2010 starts) as the 10-year replay. Its 10-year node equals the GS10 replay exactly (maximum difference 0.0).
- **Size of the fee fix, checked by hand.**
  - v3 adds **$848** to the zero-shift ladder ($299,861 → $300,709).
  - Back-of-envelope: Σ fund cost × 0.07% × years ≈ $0.91k.
  - verify_ldi_sens has $0.93k (`S/oct20/verify_ldi_sens/verify_ldi_sens.md:43`).
  - The model is slightly lower because the fee is charged on the coupons received, not on income already reinvested.
- **Option 4's linear programme reproduces the study's resizing.**
  - Faces at zero shift: IBTM $0, IBTO $0, IBTP $27.1k, IBTQ $37.4k, IBTR $38.7k. T-bonds $41.6k / $43.6k / $44.6k / $46.5k / $48.5k.
  - Study: $0 / $0 / $22.5k / $36.8k / $38.7k / $41.6k / $43.6k / $44.6k / $46.5k / $48.5k (`coupon_risk_options.md` option 4).
  - Cost: $301.2k, which is $0.5k more than the own-rung ladder on this basis. The study had +$1.9k on its own basis.
- **Two seeds.** Every canonical row moved by 0.13 points or less (option 1) and 0.03 points or less (3x).

## 4. CHANGELOG: every fix, with file:line

| # | What was wrong (where) | v3 fix (where) | Switch (legacy → v3) | Effect on the canonical table |
|---|---|---|---|---|
| F1 | **Coupon study: an iBond fund paid its yield, not its coupon** (`CO:141`, `cpn = ... else ytm`; verified `S/oct20/verify_reserve/verify_reserve.md:86`) | Not present in engY or v3. The funds pay the iShares weighted-average coupon (`engine_v3.py:138-150`; `engY.py:141-143`). Option 4's linear programme uses the same coupons | none (already fixed in the base) | None vs agreed. vs CO: about +0.6 point on option 1 (verify_reserve) |
| F2 | **Fund fee cost nothing** (`engY.py:143`, `Bond(nm, wac - IBOND_FEE, ...)`). The fee came off the coupon, and the bond was then *priced* on that lower coupon, so the buyer also paid less. NEW, found while building v3; matches verify_ldi_sens §1 "both leave out the 0.07% fund fee" | Pay NAV: price on the gross coupon (`engine_v3.py:212-222`). Receive coupon less fee (`:237`). Fee charged during the fund's T-bill stretch to 15 Dec (`:253-259`), on option 4's IBTM reinvestment (`:339`) and in the 1R valuation (`:278`) | `fee_mode` "coupon" → "nav" | Ladder **+$848**. P(cost > $300k) 49.6% → 52.2%. Option 1 short 14.46% → 14.79%. 3r 0.627% → 0.620% (noise). Option 4 0.24% → 0.13% (fewer top-up artefacts). Median gift −$1k. Median minimum $145k → $140k (knife-edge, §5c) |
| F3 | **Reserve valued with its own coupons growing at the purchase yield, still growing after Nov 2041** (`CO:204-210`; copied at `rt_engine.py:174`). +$0.76k per $10k by 2038 at −2 points (verify_ldi_sens:110). The study's 3b reserve sat at 0% after 2033 (`CO:198-199`) | Nov-41 reserve marked at market, coupons reinvested at the day's yield, T-bills after maturity (`engine_v3.py:568-586`, = `engY.py:337-357`). 3b: IBTM to 1 Jan 2033 at day yields, less the fee, then T-bills (`:588-601`) | `res_reinv` "day" (kept) | Already in the agreed basis (+0.05 point for 3r in reconcile §4a) |
| F4 | **Whole 2027 leftover kept in cash to 2042** (`CO:244` vs its docstring `:21-22`) | Released to Laura in 2033 after the cover is taken (`engine_v3.py:668-670`) | `keep_leftover` False (kept) | Option 1: kept-to-2042 would show 11.6% instead of 14.8%. 3x: no change |
| F5 | **Money above the cap counted nowhere** (`CO:233-245`), and **the chain cut the gift while above-cap money stayed with Laura** (verify_ldi_sens:147, :190) | Above-cap money is part of Laura's pool, used as cover *before* the gift is cut (`engine_v3.py:649`). New: if the switch is off, v3 still counts the money in Laura's 2033 free money (`:665-666`); engY dropped it (`engY.py:402, 416`) | `overflow_cover` True (kept); the study chain is reported as a sensitivity | With the study chain: option 1 gift below the minimum **1.50%** vs 0.05%, top reached 72% vs 77%. 3b 0.30%; 3r 0.01%; 1R 1.22% |
| F6 | Rule (a): sizing counted T-bill interest (range audit) or ignored it as cash at 0% (study) | Maturity sizing; waiting interest is a cushion | `gap_size`/`gap_proj` "fund", `gap_real` "bill" (kept) | Sized counting interest: 3r 3.1%, option 1 27% |
| F7 | Rule (b): 2033 need measured in today's value (range audit) | In dollars + $5k reserve margin | `cover_pv` False, `res_margin` 5000 (kept) | Today's-value rule: 3r 2.4%, option 1 21% |
| F8 | iBond funds as par bonds ending 15 Dec (study) | iShares holdings model | `ibond_model` "wac" (kept) | +0.6 point on 3r (reconcile §4d) |
| F9 | Yield floor 0.25% (study) | 0% base. Sensitivities at 0.25% and with no floor | `yfloor` 0.0 (kept) | 0.25%: 3r 0.28%, option 1 13.9% |
| F10 | `engY.py:240` built coupon arrays with `np.shape(s)`, which breaks when shocks have a tenor dimension | `n = np.asarray(s).shape[0]` (`engine_v3.py:291-297`) | n/a | Enables twists; no effect on parallel runs |
| F11 | engY's "o2" first set aside cover from Laura's pool and then held only the remainder in VT, which is not the study's option 2 | Study semantics (`engine_v3.py:650-652, 671-672, 708-710, 726-737`) | `option` "2" | Option 2: 0.82%, worst $12.2k |
| F12 | No "2042 return to Laura"; no options 3a, 3b, 4 or 1R in the range-audit engine; no twists | `laura42` (`engine_v3.py:677-737`); reserve kinds (`:430-437, 588-601`); option 4 pools and linear programme (`:331-385`); 1R (`:497-516, 692-704`); `shock_at_tenor` (`:94-104`); `history_twist_paths`, `bootstrap_paths` (`:784-838`) | `option`, `res_kind` | New rows |
| F14 | NEW: buy-only 2033 re-match (options 1RB and BOTH) on the v3 basis. rematch_1R.md had run it only on the study engine | Own LP with rematch_lp.py's buy-only rules (`engine_v3.py:154-193` LP worker; `:300-329` cash by payment window; `:517-565` cost on 1 Jan 2033 and as projected on 1 Jan 2031; `:638` BOTH's reserve keeps the cost with no margin; `:677-691` payments after the re-match) | `option` "1RB"; `rematch` "buyonly" | §5e |
| F13 | One case only engY ever ran: `reinv="ytm"` would silently fall back | `assert p["reinv"] == "curve"` (`engine_v3.py:389`) | n/a | none |

**Not changed, on purpose.**
- 2033 set-aside cover cash is held at 0%. That is cautious; T-bills is a sensitivity: 3r 0.55%, option 1 12.0%.
- The 2031 minimum uses the range audit's rule (98% of projected floor, net of shortfall). The study's floor − $3,700 rule is a sensitivity (§5c).

## 5. The canonical table (19 Oct 2026 curve, v3 basis, 100,000 paths, seed 20261019; seed 7 in brackets)
Source: `E/data/mc_19oct_seed20261019.json`, `..._seed7.json`; rows `suite=mc` in `E/results_v3.csv`. Dollar figures are nominal.

### 5a. Payments
| Option | A payment short | Short > $1k | Typical shortfall (median if short) / 1-in-100 / worst |
|---|---|---|---|
| 1 state only | **14.79% (14.66%)** | 9.53% | $1.5k / $4.6k / $10.1k ($9.4k) |
| 2 Laura's half in VT to 2042 | 0.82% (0.83%) | 0.61% | $2.0k / $0 / $12.2k ($12.9k) |
| 3a $10k Nov-41, not in top, no release | 0.61% (0.64%) | 0.12% | $0.5k / $0 / $3.3k ($3.1k) |
| 3b $10k in IBTM | 3.94% (3.79%) | 2.29% | $1.2k / $2.2k / $7.2k ($6.7k) |
| **3r $10k as written** | **0.62% (0.65%)** | 0.13% | $0.6k / $0 / $3.3k ($3.1k) |
| **3r $10k top fix (+$5k)** | **0.61% (0.64%)** | 0.12% | $0.5k / $0 / $3.3k ($3.1k) |
| 3r $15k as written | 0.03% (0.02%) | 0.00% | $0.4k / $0 / $2.5k ($0.9k) |
| 4 dedicated ladder | 0.13% (0.12%) | 0.00% | $0.1k / $0 / $0.3k ($0.3k) |
| 1R 2033 re-match (idealised) | 0.00% (0.00%) | 0.00% | $0 / $0 / $0 |

Option 4's small gaps are a modelling artefact, not a design failure:
- the linear programme is interpolated across rate levels;
- when the ladder costs more than $300k, every holding is bought pro rata and the rest in 2028, so the 2027 coupons on that part are lost.

### 5b. Ladder, range, gift and Laura's money
| Option | Ladder cost 1 Jan 2027 (median) / P > $300k | 2031 min / top (medians) | Gift median / 1-in-20 low | Gift reaches the top | Gift below the minimum | Laura's 2033 free money 1-in-20 / median | 2042 return (median) | WInS orders before 6 Nov |
|---|---|---|---|---|---|---|---|---|
| 1 | $300.7k / 52% | $140k / $165k | $164.0k / $134.0k | 76.9% (77.1%) | 0.05% | $0 / $25.0k | $8.8k | 0 |
| 2 | $300.7k / 52% | $140k / $165k | $164.0k / $134.0k | 76.9% | 0.05% | $0 / **$0** (her half stays in VT) | **$56.3k** | 0 |
| 3a | $300.7k / 52% | $135k / $153k | $153.0k / $127.0k | 78.8% (79.1%) | 0.004% | $7.7k / $25.3k | $28.4k | 0 or 2 |
| 3b | $300.7k / 52% | $135k / $153k | $153.0k / $126.0k | 78.6% | 0.01% | $6.6k / $25.1k | $26.3k | 0 |
| **3r as written** | $300.7k / 52% | $135k / $163k | $161.0k / $131.6k | **44.5% (44.5%)** | 0.004% | $6.5k / $21.7k | $20.3k | 0 or 2 |
| **3r top fix** | $300.7k / 52% | $135k / $158k | $158.0k / $130.0k | **75.5% (75.9%)** | 0.004% | $6.7k / $22.3k | $24.7k | 0 or 2 |
| 3r $15k | $300.7k / 52% | $130k / $163k | $161.0k / $129.8k | 52.4% | 0.003% | $8.3k / $21.1k | $22.4k | 0 or 2 (larger) |
| 4 | **$301.2k / 54%** | $140k / $165k | $164.0k / **$138.9k** | 78.7% (79.1%) | 0.000% | $7.4k / $27.5k | $10.3k | **10** |
| 1R | $300.7k / 52% | $140k / $165k | $164.0k / $135.0k | 77.7% | 0.06% | $2.0k / **$33.1k** (re-match surplus paid out in 2033) | $2.9k | 0 now (about 9-11 real-plan trades in Jan 2033) |

**Where the WInS order counts come from** (`S/oct20/tradecheck/trade_check_pack.md:156-162`):
- **0** = card T0, "about mirrors".
- **2** = card T1b: sell 295 IBTM, buy 8 Nov-41, $35.
- **10** = card T3: $175.
- 3r $15k: same 2 orders but larger. That size was not checked by the trade pack: UNVERIFIED.

**Medians of gift + Laura's 2033 + 2042 money (nominal):**

| 1 | 2 | 3a | 3b | 3r | top fix | 3r $15k | 4 | 1R |
|---|---|---|---|---|---|---|---|---|
| $201.9k | $223.9k | $209.5k | $207.7k | $206.2k | $207.9k | $207.0k | $204.1k | $198.8k |

Option 2's total is higher only because more of her money stays in stocks to 2042. Its cost is $0 free money in 2033 and the stock risk shown in §6.

### 5c. The 2031 minimum is not one number (new)
The minimum is set in 2031 from the 2028 floor. The floor shrinks whenever the ladder needs a 2028 top-up: 52% of paths, median $9.6k when needed. So from today the minimum is uncertain. Source: `E/data/extras_19oct_seed20261019.txt`.

| Options | Chance the minimum is at its headline step | Median | 1-in-20 low |
|---|---|---|---|
| 1, 2, 4 and 1R ($145k step) | 48.5% (option 4: 48.3%) | $140k | $120k |
| 3a, 3b and 3r $10k ($135k step) | 51.3% | — | $110k |
| 3r $15k ($130k step) | 52.4% | — | $105k |

- With the fee left out (legacy), the share at $145k was 49.5% and the median $145k. **The "median $145k" in earlier tables sat on a knife-edge.** It is not a real $5k change.
- With the study's minimum rule (floor − $3,700), the median is $145k / $135k again (sensitivity row). The rule choice matters here more than the fee does.
- In every model the minimum still holds: the gift is below it in 0.06% of paths or fewer (and 0% in all history replays).

### 5d. Rate falls during 2027 vs after January 2028 (coordinator item 4)
**Deterministic test.** Yields fall by x points for good. Stocks earn 7%. Each cell shows the dollars left uncovered after the leftover and the reserve (`E/data/det_19oct.json`):

| Fall | 3r $10k, fall starts 2 Jan 2027 | 3r $10k, starts 2 Jan 2028 | 3r $15k, 2027 / 2028 | 3b $10k, 2027 / 2028 | 1, 2027 / 2028 |
|---|---|---|---|---|---|
| −1.0 | $0 | $0 | $0 / $0 | $0 / $0 | $10.5k / $8.6k |
| −1.25 | $0.6k | $0 | $0 / $0 | $1.1k / $0 | $13.0k / $10.7k |
| −1.5 | $3.2k | $0 | $0 / $0 | $3.7k / $0.2k | $15.5k / $12.7k |
| −1.75 | $5.8k | $0.1k | $0 / $0 | $6.3k / $2.2k | $17.9k / $14.7k |
| −2.0 | $8.3k | $1.8k | $2.3k / $0 | $8.8k / $4.2k | $20.3k / $16.7k |
| −3.0 | $18.1k | $8.5k | $12.4k / $0.6k | $18.5k / $11.9k | $29.5k / $24.3k |

- **$10k covers about 1.0-1.25 points during 2027 and about 1.5-1.75 points after Jan 2028.**
- verify_ldi_sens has about 1.3 and 1.9 (`verify_ldi_sens.md:24, 108`). Its basis differs (own-rung sizing, waiting in T-bills); same direction, same size of gap.
- In every deterministic path the *payments* are still met. The uncovered dollars come out of Laura's half and then the gift. For example, 3r at −2 during 2027: gift $151k, Laura's 2033 money $4k.

**Monte Carlo, conditioned** (3r $10k; `mc.timing` in the json):

| Paths | Count | 3r short | Worst |
|---|---|---|---|
| ≥1-point fall during 2027, then calm | 2,773 | 3.35% | $3.3k |
| calm 2027, ≥1-point fall Jan 2028-Jan 2033 | 12,509 | 0.71% | $2.3k |

The same split for other options:
- 3r $15k: 0.36% / 0.01%.
- 3b: 10.9% / 9.0%. IBTM does not rise when yields fall.
- Option 1: 26.5% / 27.8%.

### 5e. The buy-only 2033 re-match on the v3 basis (coordinator request; `E/data/bo_19oct_seed*.json`, `E/data/bo_tables.txt`)
Same 100,000 paths as §5; seed 20261019, seed 7 in brackets.

| Option | Short | Worst | Gift median / 1-in-20 | Top reached | Gift < min | Min / top | Laura 2033: 1-in-20 / median | 2042 return | Gift + Laura (median) | Re-match cost: median / 1-in-20 high | 2033 buys: median / 1-in-20 / max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1R buy-only** | **0.00% (0.00%)** | $0.1k (dust) | $164.0k / $132.6k | 77.7% (78.0%) | 0.007% | $140k / $165k | $0 / $21.0k | $18.5k | $204.9k | $8.5k / $26.0k | 1 / 3 / 4 |
| **BOTH (3r fix + buy-only)** | **0.00% (0.00%)** | $0.1k | $158.0k / $130.0k | **77.3% (77.4%)** | 0.000% | $135k / $158k | **$5.1k / $27.0k** | $18.5k | $205.4k | $8.5k / $26.0k | 1 / 3 / 4 |
| 3r top fix (same paths) | 0.61% (0.64%) | $3.3k | $158.0k / $130.0k | 75.5% (75.9%) | 0.004% | $135k / $158k | $6.7k / $22.3k | $24.7k | $207.9k | — | — |
| 1 (same paths) | 14.79% (14.66%) | $10.1k | $164.0k / $134.0k | 76.9% (77.1%) | 0.05% | $140k / $165k | $0 / $25.0k | $8.8k | $201.9k | — | — |

**Robustness of the buy-only forms** (short / worst / top reached / gift < min):

| Run | 1R buy-only | BOTH | 3r fix | 1 |
|---|---|---|---|---|
| History, additive (688) | 0% / 0 / 88% / 0 | 0% / 0 / 80% / 0 | 0.87% / $1.0k / 78% / 0 | 18.8% / $3.6k / 87% / 0 |
| History, proportional | 0% / 0 / 88% / 0 | 0% / 0 / 81% / 0 | 0% / 0 / 80% / 0 | 7.0% / $2.9k / 87% / 0 |
| History, real curve twists | 0% / 0 / 87% / 0 | 0% / 0 / 80% / 0 | 2.76% / $1.6k / 76% / 0 | 16.1% / $7.6k / 85% / 0 |
| Bootstrap, twists, seed 20261021 / 8 | 0% / 0% / 81% / 0.05% | 0% / 0% / 78% / 0.01% | 0.71% / 0.76%, worst $6.1k / $6.8k / 74% / 0.05% | 17.4% / 17.6% / 80% / 0.19% |
| Timing (MC): ≥1-point fall during 2027 / after Jan 2028 | 0% / 0% | 0% / 0% | 3.35% / 0.71% | 26.5% / 27.8% |
| Sensitivity: sizing counts the funds' own bill interest to 15 Dec | 1.88% / $2.8k | 1.88% / $2.8k | — | — |

**What the rows show**
- **BOTH removes 3r-fix's residual 0.6% (and the 2.8% in the twisted history) at the same gift and the same minimum.** The cost is timing, not total: Laura gets about $4.7k more in 2033 (median $27.0k against $22.3k) and $6.2k less in 2042 ($18.5k against $24.7k). The median of all her money, in nominal dollars, is $2.5k lower ($205.4k against $207.9k). Part of that is timing: under 3r-fix the reserve keeps growing in the bond to 2042, while under BOTH it is paid out in 2033. The rest is bid-ask, tickets and rounding, and buy-only buys a little more than the bare need.
- **The re-match fixes the 2027 timing gap.** It is sized on the actual 2033 shortfall, so a fall during 2027 no longer leaves 3r short (3.35% → 0%).
- **The sizing must not count the funds' bill interest.** If it does, the re-match is cheaper (median about $5.4k, matching rematch_1R.md's $5.5k on the study engine). But 1.9% of paths are then short by up to $2.8k, because the funds' cash stretch to 15 Dec is not locked. **For 0%, the re-match must size the funds' last months at 0%.** That is a plan rule.
- **Cross-check.** rematch_1R.md (study engine, 16 Oct curve) had BOTH at 0% short, top reached 80.2%, buy-only cost +$2.1k / +$5.8k over the frozen estimate and 1-4 trades (`rematch_1R.md:12, 79, 87`). v3 agrees on the 0%, the trade count and the size of the cost. The top-reach gain is smaller in v3: BOTH adds 1.8 points over 3r-fix (75.5% → 77.3%), against 8.4 points there (71.8% → 80.2%). I have not split the difference between the two engines: UNVERIFIED which rule drives it.

## 6. Robustness (payment short % / worst, all options)
Sources: `E/data/sens_19oct_seed20261019.json`, `hist_19oct.json`, `boot_19oct_seed*.json`, `mc_16oct_seed20261019.json`. MC rows use 100k paths, seed 20261019. Bootstraps use 100k paths, seeds 20261021 and 8.

| Scenario | 1 | 2 | 3a | 3b | 3r | 3r fix | 3r $15k | 4 | 1R |
|---|---|---|---|---|---|---|---|---|---|
| **Canonical (v3, 19 Oct)** | 14.8% / $10.1k | 0.82% / $12.2k | 0.61% / $3.3k | 3.9% / $7.2k | 0.62% / $3.3k | 0.61% / $3.3k | 0.03% / $2.5k | 0.13% / $0.3k | 0 |
| Legacy (fee fix off = agreed basis) | 14.5% / $10.1k | 0.78% | 0.61% | 3.7% | 0.63% / $3.3k | 0.62% | 0.03% | 0.24% | 0 |
| 16 Oct curve (ladder $302.4k, P > $300k 57%) | 14.8% | 0.90% | 0.68% | 4.1% | 0.69% / $3.3k | 0.68% | 0.03% | 0.15% | 0 |
| Yield floor 0.25% | 13.9% | 0.74% | 0.27% | 2.9% | 0.28% / $2.6k | 0.27% | 0.01% | 0.00% | 0 |
| No yield floor (cash below 0%: unrealistic bound) | 17.4% / $20k | 1.5% | 4.2% | 7.1% | 4.4% / $19k | 4.3% | 2.6% | 7.8% / $16k | 0 |
| Study chain (above-cap money not used first) | 14.8% | 1.40% | 0.61% | 3.9% | 0.62% | 0.61% | 0.03% | 0.13% | 0 |
| 2033 need in today's value, matched zeros | 21.3% | 1.0% | 2.3% / $5.5k | 5.2% | 2.4% / $5.5k | 2.4% | 0.56% | 0.13% | 0 |
| Rungs sized counting T-bill interest | 27.2% | 1.4% | 2.4% | 6.4% | 3.1% / $7.0k | 2.6% | 0.86% | 28.2% / $8.2k | 0 |
| Waiting cash really at 0% | 25.9% | 1.1% | 0.95% | 7.1% | 0.97% / $3.3k | 0.96% | 0.12% | 23.4% / $2.4k | 0 |
| 2033 set-aside cash earns T-bills | 12.0% | 0.78% | 0.53% | 3.8% | 0.55% | 0.54% | 0.03% | 0.01% | 0 |
| Leftover kept to 2042 | 11.6% | 0.82% | 0.61% | 3.9% | 0.61% | 0.61% | 0.02% | 0.11% | 0 |
| Stocks and yields fall together (ρ +0.3) | 14.8% | **1.28%** | 0.61% | 3.9% | 0.62% | 0.61% | 0.03% | 0.13% | 0 |
| Rate volatility 0.75 point a year | 11.7% | 0.50% | 0.26% | 2.5% | 0.26% / $1.8k | 0.26% | 0.00% | 0.02% | 0 |
| History, additive, 10-year (688 windows) | 18.8% / $3.6k | 0 | 0.87% / $1.0k | 4.9% | 0.87% / $1.0k (6 windows, Aug 1984-May 1985) | 0.87% | 0 | 0 | 0 |
| History, proportional | 7.0% | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **History, additive, real curve twists** | 16.1% / $7.6k | 0.15% | 2.8% / $1.6k | 5.5% | **2.8% / $1.6k** (19 windows, Aug 1983-Sep 2000) | 2.8% | 0.44% / $1.5k | 4.5% / $0.7k | 0 |
| **Bootstrap, twists** (seed 20261021 / 8) | 17.4% / 17.6% | 1.0% / $23k | 0.70% / 0.74% | 4.4% | **0.77% / 0.82%, worst $6.1k / $6.8k** | 0.71% / 0.76% | 0.27% / 0.28% | 1.8% / $1.2k | 0 |
| Bootstrap, 10-year only | 14.3% / 14.4% | 0.79% | 0.64% | 3.7% | 0.71% / 0.72%, worst $4.9k | 0.65% | 0.10% | 0.31% | 0 |

**Reading notes**
- **Which rows are bounds.** "No floor" and "waiting cash really at 0%" are bounds, not forecasts. No floor means waiting cash earns negative rates, which nobody would accept when cash can be held. WInS cash pays 0% (`S/oct20/verify_reserve/verify_reserve.md:104`), but the plan's waiting money is in a short Treasury fund.
- **Option 4 is fragile when the sizing basis and reality disagree.** If rungs are sized counting T-bill interest, or waiting cash really earns 0%, it shows many small gaps (23-28%). Because it pools every coupon, it has no cushion: it is sized exactly. The worst gaps stay small ($2.4-8.2k).
- **Top reached and gift below the minimum.** On the twisted bootstrap: option 1 80% / 0.19%; 3r 46% / 0.05%; top fix 74% / 0.05%; option 4 82% / 0.00%; 1R 80% / 0.16%. Under the study chain the "gift below the minimum" figure for option 1 jumps to 1.50%: this is F5's chain-order artefact.
- **The bootstrap sample.** 881 monthly changes, May 1953 to Sep 2026. Monthly correlation of stocks with the 10-year change −0.08.

## 7. What changed against the earlier agreed numbers (reconcile_3r.md §5)

| | Agreed (19 Oct) | v3 (19 Oct) | Why |
|---|---|---|---|
| Ladder cost / P > $300k | $299.9k / 50% | **$300.7k / 52%** | Fund fee (F2) |
| Option 1 short | 14.5% (14.4%) | 14.8% (14.7%) | F2 |
| 3r as written: short / worst | 0.63% / $3.3k | 0.62% / $3.3k | No real change |
| 3r top reached (as written / fix) | 45% / 76% | 44.5% / 75.5% | Rounding |
| Option 1 / 3r gift median | $165k / $162k | $164k / $161k | F2 (floor and VT about $0.6k smaller) |
| Option 1 median minimum | $145k | $140k | Knife-edge (§5c) |
| Laura's 2033 money (median, 1 / 3r) | $25.9k / $22.4k | $25.0k / $21.7k | F2 |
| New rows | — | 2, 3a, 3b, 3r $15k, 4, 1R, 1R buy-only, BOTH; 2042 return; timing; twists | — |

## 8. Limits and UNVERIFIED
**Model family**
- MC rates: parallel random walk with no mean reversion.
- The twist runs use six FRED tenors, with linear interpolation between them.
- The bootstrap de-means rate changes, so it has no drift.
- History: about 4 non-overlapping 16-year periods. US stocks stand in for VT. Monthly-average prices smooth crashes.

**1R (zero-coupon form) is idealised; the buy-only form (§5e) is not**
- It buys zeros maturing 15 Nov before each payment, with no rounding and 0.10% per leg.
- The real plan may hold only WInS-listed Treasuries and ETFs (CLAUDE.md, 6 Oct email), so a real re-match uses coupon notes.
- `S/oct20/rematch1R/` ran a real linear programme on new Nov notes on the red-team engine (16 Oct curve): also 0.00% short, 11 tickets, 2033 cost p95 about $21.9k (`S/oct20/rematch1R/data/r1_base_16oct_stdout.txt`).
- Its write-up `S/oct20/rematch1R/rematch_1R.md` is now finished. v3 re-implements its buy-only form on the v3 basis (§5e) with its own LP. v3 does not import rematch_lp.py; the rules are the same. Universe: new Nov notes plus the held T-bonds. Not included: buying more of the held iBond funds (allowed in rematch_lp.py's universe B). That can only make v3's cost a little higher.
- Unverified inputs: whether new 10-year notes maturing 15 Nov 2033-41 will exist (routine issuance, UNVERIFIED), and the retail bid-ask and ticket costs.

**Option 4**
- The faces are interpolated from 161 linear-programme solutions across rate levels.
- Pro-rata purchase if over budget.
- About 10 WInS orders after the TNA, and they contradict 3-4 filed notes (study §4).

**Fees and data**
- **Fund fee:** 0.07% on all five iShares pages (16 Oct snapshots). The fee is charged on coupons and on the fund's T-bill stretch, not on income already reinvested.
- **iBond holdings:** one bond per fund at the weighted-average coupon and maturity. Real funds hold several bonds.

**Unchanged and UNVERIFIED**
- when WInS credits coupons;
- the WInS price of the Nov-41 bond;
- actual iBond distribution timing;
- whether SGOV, BIL or SHV is the waiting fund (SGOV was seen on WInS on 29 Sep; verify_reserve §1g).

**Not modelled:** taxes, and costs outside WInS.

**Curve**
- 19 Oct. The 20 Oct curve was not published when fetched (§1).
- One curve day moved the ladder by $1.7k (16 → 19 Oct).
- Re-price on the 6 Nov close.

## 9. Files (all under `E/`)
- `scripts/engine_v3.py`: the engine (switches, options, scenario generators).
- `scripts/common.py`: summary statistics.
- `scripts/check_legacy.py`: the validation.
- `scripts/run_v3.py`: suites mc, sens, hist, boot, det, bo.
- `scripts/extras.py`: minimum steps, top-up odds.
- `scripts/diag_min_steps.py`: the minimum's distribution under three bases.
- `scripts/make_csv.py`: builds the CSV.
- `scripts/show_bo.py`: prints the §5e tables.
- `scripts/run_all.sh`: the one-command reproduce.
- `results_v3.csv`: every MC, sensitivity, history, bootstrap and buy-only re-match row (228 rows, 34 metrics).
- `data/bo_19oct_seed*.json` and `data/bo_tables.txt`: the buy-only re-match runs.
- `data/*.json` and `data/*.txt`: raw outputs.
- `data/det_19oct.json`: the timing table.
- `data/check_legacy_seed*.txt`: the validation output.
- `ref/`: copies of engY.py, engX.py, coupon_options.py and the agreed JSONs used by the check.
