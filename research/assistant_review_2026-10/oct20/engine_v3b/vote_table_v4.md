# vote_table_v4: canonical MODEL numbers for the Tue 27 Oct coupon-cover vote (engine_v3b)

AI-generated research by Claude Code for Team Caplet, Tue 20 Oct 2026 (Sydney; runs 00:12-00:35 UTC). **Every number here is MODEL output** from code an AI wrote; no student has rebuilt any of it. Nothing here is TNA, IPS, options-note or Final Report wording. If the team uses a number, log it in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). No personal data (token scan: 0 hits; tokens not printed).

**Paths.** `S/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/`. `B/` = `S/oct20/engine_v3b/` (this folder). `E/` = `S/oct20/engine_v3/` (not edited). Engine: `B/scripts/engine_v3b.py`. Every row: `B/results_v4.csv` (127 rows: suite × scenario × seed × option × D10). Raw runs: `B/data/out/`.

**Basis (v3b headline).** engine_v3's v3 basis (19 Oct treasury.gov curve; 0.07% iBond fee charged at NAV; maturity sizing; 2033 need in dollars + $5k reserve margin; 0% yield floor; set-aside cash at 0%; rates a parallel random walk of 1.0 point a year; VT 7% compound, 16.78% volatility) **plus** two changes: the buy-only re-match is booked in **bond units** (B1), and the 2031 minimum uses the **team documents' rule** (B3). D10 (B2) is not part of the basis: every row is shown **off and on**.

**The 20 Oct curve.** Not published: the treasury.gov October CSV (URL from `S/oct20/numbers/scripts/run_all.sh:7`) fetched at 00:08 and again at 03:28 UTC on 20 Oct had 10/19/2026 as its latest row (`B/data/raw/fetch_20oct*/`); New York was still on 19 Oct. No 20 Oct run. After about 22:00 UTC on 20 Oct: `run_v3b.py mc 20261019 100000 OUT.json <new csv> 10/20/2026`.

## 0. Summary in five lines
1. **Switches off = engine_v3 exactly.** Path-level difference 0 on 100,000 paths × 2 seeds (all nine options) and on the buy-only forms (20,000 paths × 2 seeds); the engY legacy check is byte-identical to engine_v3's logs. My D10 and units code also equal verify_engine3's patches exactly (§6).
2. **D10 is the biggest single reading effect.** Option 1: **14.8% → 1.6%** short (worst $10.1k → $7.1k). 3r-fix: 0.6% → 0.08%. BOTH: no shortfall either way. D10 on moves Laura's 2033 money (median about $22-25k) into stocks inside the portfolio until 2042.
3. **BOTH on the units book:** no payment short in any run (MC, history, twists, bootstrap) **given the 0% cash rule**, but its top-reach is **73.1%, below 3r-fix's 75.5%**. The re-match costs a median **$10.4k** (1-in-20 $27.3k), 1 buy at the median, at most 4.
4. **BOTH's "no shortfall" is fragile to things the re-match cannot see.** At an illustrative 0.1% iBond payout miss it is 0.20% short; at 1% it is **6.6% short, more often than 3r-fix's 5.8%** (but with smaller gaps: worst $2.1k against $5.3k). If the re-match counts the funds' own bill interest it is 1.5% short.
5. **2031 minimum, team rule:** median $140k (option 1) / $135k (3r, 3r-fix, BOTH) / $130k (3r $15k); the headline step ($145k / $135k / $130k) is reached in only **about half of paths (48-52%)**. The 98% rule gives the same medians.

---

## 1. The canonical table (MODEL; 19 Oct curve; 100,000 paths; seed 20261019, seed 7 in brackets)

Source: `B/data/out/mc_19oct_seed20261019.json`, `..._seed7.json`; rows `suite=mc, scenario=v3b basis (canonical)` in `B/results_v4.csv`.

**D10 off (10a)** = after the 2033 set-aside, Laura's retained half is hers. **D10 on (10b)** = Laura's retained 2033 money (her half of VT after the 2033 cover, the unused 2027 leftover and any above-cap money) stays in VT **inside the portfolio**, on call for any payment through 2042 and drawn last (after cover cash and the reserve); what is left returns in 2042. This is the reading verify_engine3 used for its 1.59% figure (= VREC's reading A).

### 1a. Payments and the gift

| Option | D10 | A payment short (> $100) | Worst | 1-in-100 shortfall | Gift reaches the top | Gift median / 1-in-20 low | 2031 minimum: median; share at headline step | Minimum 1-in-20 low |
|---|---|---|---|---|---|---|---|---|
| **1** state the risk only | off | **14.79% (14.66%)** | $10.1k | $4.6k | 76.9% (77.1%) | $164.0k / $134.0k | $140k; 49.9% at $145k | $115k |
| 1 | **on** | **1.59% (1.56%)** | $7.1k | $0.8k | 76.9% (77.1%) | $164.0k / $134.0k | $140k; 49.9% at $145k | $115k |
| **3r** $10k as written | off | 0.62% (0.65%) | $3.3k | $0 | 44.5% (44.5%) | $161.0k / $131.6k | $135k; 51.3% at $135k | $110k |
| 3r | on | 0.09% (0.08%) | $2.2k | $0 | 44.5% (44.5%) | $161.0k / $131.6k | $135k; 51.3% at $135k | $110k |
| **3r-fix** (top counts $5k) | off | **0.61% (0.64%)** | $3.3k | $0 | 75.5% (75.9%) | $158.0k / $130.0k | $135k; 51.3% at $135k | $110k |
| 3r-fix | on | **0.08% (0.07%)** | $2.2k | $0 | 75.5% (75.9%) | $158.0k / $130.0k | $135k; 51.3% at $135k | $110k |
| **3r $15k** as written | off | 0.030% (0.024%) | $2.5k | $0 | 52.4% (52.4%) | $161.0k / $129.8k | $130k; 51.5% at $130k | $105k |
| 3r $15k | on | 0.005% (0.003%) | $0.4k | $0 | 52.4% (52.4%) | $161.0k / $129.8k | $130k; 51.5% at $130k | $105k |
| **BOTH** (3r-fix + buy-only re-match, units book) | off | **0.000% (0.000%)**¹ | under $100 | $0 | **73.1% (73.2%)** | $158.0k / $129.4k | $135k; 51.0% at $135k | $110k |
| BOTH | on | 0.000% (0.000%)¹ | under $100 | $0 | 73.1% (73.2%) | $158.0k / $129.4k | $135k; 51.0% at $135k | $110k |
| *Reference: 1R buy-only (units)* | off / on | 0.000% / 0.000%¹ | under $100 | $0 | 77.4% (77.6%) | $164.0k / $131.0k | $140k; 47.6% at $145k | $115k |
| *Option 2 (NOT D10, see note)* | — | 0.82% (0.83%) | **$12.9k** | $0 | 76.9% (77.1%) | $164.0k / $134.0k | $140k; 49.9% at $145k | $115k |

¹ **Read BOTH's 0% with its condition:** in the model, and only given the 0% cash rule (the re-match sizes all waiting cash, including the funds' last months, at 0%). After 2033 the engine pays from the same cash flows the re-match was sized on (`E/scripts/engine_v3.py:545-556` vs `:680-691`), so the 0% is partly circular. Risks the re-match cannot see (fund payout error, §3) do produce shortfalls. It is not a certainty level.

- "Worst" = the larger of the two seeds' worst path. "1-in-100 shortfall" = the 99th percentile of the total shortfall ($0 when fewer than 1 path in 100 is short).
- D10 changes payments and Laura's money only. It never changes the range, the gift or the minimum (identical columns above).
- **Option 2 is not the D10 reading.** Option 2 sets nothing aside in 2033: the whole half stays in VT and the gift is cut only for need beyond its 2033 value (study semantics). Shortfalls are rarer than under 1 + D10 (0.8% vs 1.6%) but larger in crashes (worst $12-13k here, $18-23k on the twisted bootstrap, against $7-8k).
- Gift below the announced minimum: 0.047% (options 1 and 2), 0.001% (3r forms), 0% (3r $15k, BOTH), 0.008% (1R buy-only).

### 1b. Laura's money, WInS orders and the 2033 buys (seed 20261019)

Fair crediting (as engine_v3 and verify_rematch): waiting cash earns T-bills, the 3r reserve is marked at market, BOTH's leftover cash earns T-bills. The last money column puts the two dates on one footing: Laura's 2033 money carried at 1-year T-bills to 2042, plus her 2042 money. **Compare options only within the same D10 setting**: with D10 on her money sits in stocks to 2042, so its median is higher and its spread much wider (2042 money 1-in-20 / 1-in-20 high, D10 on: about $3k-21k / $179k-197k).

| Option | D10 | Laura's 2033 free money: 1-in-20 / median | Laura's 2042 money: median (1-in-20 low) | All Laura's money valued in 2042, median (1-in-20 low) | WInS orders before 6 Nov | 2033 real-plan buys: median / 1-in-20 / max |
|---|---|---|---|---|---|---|
| 1 | off | $0 / $25.0k | $8.8k ($0) | $51.7k ($3.1k) | 0 | none |
| 1 | on | $0 / $0 (kept on call) | $60.3k ($3.3k) | $60.3k ($3.3k) | 0 | none |
| 3r | off | $6.5k / $21.7k | $20.3k ($1.4k) | $56.1k ($11.4k) | 0 or 2 | none |
| 3r | on | $0 / $0 | $66.0k ($15.0k) | $66.0k ($15.0k) | 0 or 2 | none |
| 3r-fix | off | $6.7k / $22.3k | $24.7k ($1.5k) | $62.0k ($11.6k) | 0 or 2 | none |
| 3r-fix | on | $0 / $0 | $71.7k ($15.5k) | $71.7k ($15.5k) | 0 or 2 | none |
| 3r $15k | off | $8.3k / $21.1k | $22.4k ($4.3k) | $56.8k ($17.1k) | 0 or 2 (larger; UNVERIFIED size) | none |
| 3r $15k | on | $0 / $0 | $66.7k ($21.4k) | $66.7k ($21.4k) | 0 or 2 (larger) | none |
| BOTH | off | $3.7k / $25.3k | $20.4k ($2.0k) | $60.7k ($10.5k) | 0 or 2 now | **1 / 2 / 4** (re-match cost median $10.4k, 1-in-20 $27.3k) |
| BOTH | on | $0 / $0 | $70.2k ($13.2k) | $70.2k ($13.2k) | 0 or 2 now | 1 / 2 / 4 |
| *Option 2* | — | $0 / $0 | $56.3k ($9.1k) | $63.2k ($9.2k) | 0 | none |

- **WInS orders** (`S/oct20/tradecheck/trade_check_pack.md:156-162`): 0 = card T0 "about mirrors"; 2 = card T1b (sell 295 IBTM, buy 8 Nov-41, $35). D10 needs no order. BOTH adds no WInS order now; its 1-4 buys are real-plan purchases in January 2033 (held Nov-41 / Nov-40 bonds or new 15-Nov notes; notes for 2036-38 do not exist yet, verify_rematch §2.3).
- **BOTH vs 3r-fix, D10 off:** gift median the same ($158k), 1-in-20 gift $0.6k lower; Laura about **$3k more in 2033** ($25.3k vs $22.3k) and **$4.3k less in 2042** ($20.4k vs $24.7k); valued together in 2042, about **$1.3k less** ($60.7k vs $62.0k). With D10 on, about $1.5k less ($70.2k vs $71.7k).
- Ladder on 1 Jan 2027 (all options here): median $300.7k, above $300k in 52% of paths; a 2028 top-up is needed in 52% (unchanged from engine_v3; verify_forward's independent fee-counted figure is $300,652).

---

## 2. Robustness: payment short % / worst (top reach) (MODEL)

Sources: `B/data/out/hist_19oct.json` (688 overlapping 16-year windows, start months Apr 1953 to Jul 2010; US stocks stand in for VT), `boot_19oct_seed20261021.json`, `boot_19oct_seed8.json` (100,000 paths each; 12-month blocks of 1953-2026 monthly changes at six tenors with the same months' stock returns). Both seeds were run for the bootstrap; nothing was cut.

| Option | D10 | MC, seed 7 | History, additive | History, proportional | History, real curve twists | Bootstrap with twists, seed 20261021 | Bootstrap with twists, seed 8 |
|---|---|---|---|---|---|---|---|
| 1 | off | 14.66% / $9.4k | 18.75% / $3.6k (87%) | 6.98% / $2.9k (87%) | 16.13% / $7.6k (85%) | 17.42% / $11.9k (80%) | 17.58% / $12.0k (80%) |
| 1 | on | 1.56% / $7.1k | 1.02% / $2.2k (87%) | 0 / $0 (87%) | 1.31% / $2.3k (85%) | 1.46% / $8.0k (80%) | 1.57% / $8.1k (80%) |
| 3r | off | 0.65% / $3.1k | 0.87% / $1.0k (55%) | 0 / $0 (58%) | 2.76% / $1.6k (54%) | 0.77% / $6.1k (46%) | 0.82% / $6.8k (45%) |
| 3r | on | 0.08% / $2.2k | 0.73% / $0.8k (55%) | 0 / $0 (58%) | 1.16% / $1.6k (54%) | 0.16% / $6.1k (46%) | 0.16% / $5.3k (45%) |
| 3r-fix | off | 0.64% / $3.1k | 0.87% / $1.0k (78%) | 0 / $0 (80%) | 2.76% / $1.6k (76%) | 0.71% / $6.1k (74%) | 0.76% / $6.8k (74%) |
| 3r-fix | on | 0.07% / $2.2k | 0.73% / $0.8k (78%) | 0 / $0 (80%) | 1.02% / $1.0k (76%) | 0.13% / $6.1k (74%) | 0.14% / $5.3k (74%) |
| 3r $15k | off | 0.024% / $0.9k | 0 / $0 (60%) | 0 / $0 (64%) | 0.44% / $1.5k (59%) | 0.27% / $5.4k (52%) | 0.28% / $4.2k (52%) |
| 3r $15k | on | 0.003% / $0.2k | 0 / $0 (60%) | 0 / $0 (64%) | 0.44% / $1.5k (59%) | 0.07% / $5.4k (52%) | 0.08% / $3.9k (52%) |
| BOTH (units) | off | 0.000%¹ | 0¹ (77%) | 0¹ (78%) | 0¹ (77%) | 0.000%¹ (74%) | 0.000%¹ (74%) |
| BOTH (units) | on | 0.000%¹ | 0¹ (77%) | 0¹ (78%) | 0¹ (77%) | 0.000%¹ (74%) | 0.000%¹ (74%) |
| *Option 2* | — | 0.83% / $12.9k | 0 (87%) | 0 (87%) | 0.15% / $0.2k (85%) | 1.01% / $23.3k (80%) | 1.05% / $18.1k (80%) |

- History rows are about 4 independent 16-year periods, not 688 independent tests; "0" there means no window failed, not "zero risk".
- **D10 helps less where stocks and bonds fall together.** On the bootstrap, D10 cuts option 1 from 17.4-17.6% to 1.5-1.6%, but the worst case stays $8k; for 3r-fix the worst case does not move ($6.1k).
- BOTH's re-match on these runs: median $10.4-10.7k; 1-in-20 $20.8k (proportional history) to $30.3k (bootstrap); 1-4 buys.

## 3. Sensitivities on the canonical MC paths (seed 20261019 [seed 7]; MODEL)

| Scenario | Option | D10 | Short | Worst | Top reach | Minimum median; share at step | Laura 2033 / 2042 median | Re-match cost median / 1-in-20 |
|---|---|---|---|---|---|---|---|---|
| **Minimum by the 98% rule** (engine_v3's rule) | 1 | off | 14.79% | $10.1k | 76.9% | **$140k; 48.5%** at $145k | $25.0k / $8.8k | — |
| same | 3r / 3r-fix | off | 0.62% / 0.61% | $3.3k | 44.5% / 75.5% | $135k; 51.3% | $21.7k / $22.3k | — |
| same | 3r $15k | off | 0.030% | $2.5k | 52.4% | $130k; 52.4% | $21.1k | — |
| same | BOTH | off | 0.000%¹ | under $100 | 73.1% | $135k; 51.1% | $25.3k / $20.4k | $10.4k / $27.3k |
| **iBond payout haircut 0.1% per fund** (illustrative size) | 3r-fix | off / on | 1.81% [1.91%] / 0.40% [0.44%] | $3.5k / $2.0k | 75.5% | unchanged | — | — |
| same | BOTH | off / on | **0.20% [0.20%]** / 0.06% [0.06%] | $0.3k | 73.1% | unchanged | — | $10.4k / $27.3k |
| **iBond payout haircut 1% per fund** (illustrative size) | 3r-fix | off / on | **5.83% [5.74%]** / 1.11% [1.15%] | $5.3k / $4.0k | 75.5% | unchanged | — | — |
| same | BOTH | off / on | **6.61% [6.55%]** / 1.31% [1.40%] | $2.1k | 73.1% | unchanged | — | $10.4k / $27.3k |
| Re-match counts the funds' own bill interest to 15 Dec (unsafe sizing) | BOTH | off / on | **1.52%** / 0.04% | $2.9k / $1.3k | 78.6% | unchanged | $27.5k / $16.3k | $7.6k / $27.1k |
| **Old behaviour: lump book** (engine_v3) | BOTH | off | 0.000%¹ | under $100 | **77.3%** | $135k; 51.2% | $27.0k / $18.5k | **$8.5k / $26.0k** |

- **Haircut method** (coordinator request; same as `S/oct20/redteam_both/redteam_both.md` §5c): each of IBTO, IBTP, IBTQ and IBTR delivers h × $50,000 less cash than modelled in its payment year; realised cash only, never seen by any sizing or the re-match. **The sizes are illustrative stresses, not estimates; real iBond payout error is UNVERIFIED.** On the units book this reproduces the red team's lump-book result (BOTH 0.17-0.24% at 0.1%; 6.7-6.8% vs 3r-fix 5.7-5.9% at 1%).
- **Why BOTH loses at a 1% miss:** it releases 3r-fix's $5k margin and sizes exactly, so any unseen shortfall becomes a gap; its gaps stay smaller (worst $2.1k against $5.3k).
- **Minimum rule:** the team rule and the 98% rule give the same medians for every option; the share at the step moves by 1.4 points for option 1 (49.9% vs 48.5%) and by 0-0.1 point for the reserve options. The rule choice is not a $5k question; the knife-edge is the 2028 top-up (52% of paths).

---

## 4. Safe to quote / never quote (plain English; every number is MODEL, 19 Oct curve, and needs its basis beside it; no measured number goes in the IPS)

### Safe to quote (with "model", the date and the condition)
- **No cover, Laura's half free after 2033 (D10 off):** small payment gaps in about **1 model path in 7**, typically about $1,500, worst about $10,000.
- **No cover, Laura's half on call inside the portfolio to 2042 (D10 on):** about **1 path in 60 to 1 in 70** (about 1.6%), worst about $7,000; about 1.5% with real curve twists in the bootstrap, worst about $8,000. Always say which D10 reading the figure assumes.
- **3r (either top rule):** payments short in **under 1 path in 100** under parallel rate moves (about 0.6%), worst about $3,000-4,000; about 0.8% with real curve twists in the bootstrap (worst about $6,000-7,000) and about 2.8% of overlapping history windows with twists. With D10 on: about 1 path in 1,000 under parallel moves (about 0.1%), about 0.15% in the bootstrap.
- **BOTH (3r-fix plus a buy-only 2033 re-match):** the 2033 re-match **"removes reinvestment risk in the model, given the 0% cash rule"**: no payment was short in any of our model runs under that rule. It needs **1 to 4 extra Treasury purchases in January 2033** (usually 1), costing about **$10,500 at the median** and about $27,000-30,000 in a 1-in-20 case; part of that comes back to Laura by 2042 as interest and unused cash. It is fragile to payouts the check cannot see: an illustrative 1% shortfall in each iBond fund's payout leaves it short about as often as 3r-fix (about 6-7% vs about 6%), with smaller gaps.
- **Top reach:** "about three in four" Monte Carlo paths reach the top for option 1, 3r-fix and BOTH (73-77%); **BOTH reaches it about as often as 3r-fix, not more** (73-77%). About two in five to one in two for 3r with the full $10k counted in the top (44-46%).
- **2031 minimum:** the team freezes a **rule** (floor money − $3,700, rounded down to $5k, net of any projected uncovered shortfall), not a number. In the model the minimum lands on its headline step in only **about half of paths**; its typical value is $140k without a reserve and $135k with the $10k reserve.
- **Laura's money, BOTH vs 3r-fix:** about $3,000 more in 2033 and about $4,000 less in 2042; valued together in 2042 with waiting cash credited at T-bill rates, about $1,000-1,500 less.
- **D10 on** turns Laura's 2033 free money (typically about $22,000-25,000) into money held in stocks inside the portfolio until 2042: more money in a typical 2042, much wider range, $0 to spend in 2033.

### Never quote
| Do not say | Why |
|---|---|
| "0.02%" or "zero in 690 history windows" / "zero in history" for 3r | Study-engine artefacts; canonical about 0.6%; 2.8% of windows with twists |
| "worst under $2k" / "under $2k" | Worst cases are $3.3k (MC) to $6-7k (bootstrap) |
| "$18,952" (or "about $19,000") as the 2-point coupon gap | $19,488 after the line-141 fix (VIN E1) |
| "7.5%" (16% falls to 7.5%) | Not a consistent figure |
| "300/450" or "0.667" as the WInS scale | Deposit ratio; scale about 0.64 |
| "BOTH is 0% in every test", "BOTH has zero risk", "guaranteed", "certain", or any certainty level for BOTH | The 0% is given the 0% cash rule and partly circular; 1.5% if the sizing counts fund bill interest; 6.6% at an illustrative 1% payout miss |
| Any top-reach **gain** for BOTH ("+8 points", "80% vs 72%", "77.3% vs 75.5%") | Units book: 73.1% vs 75.5% (BOTH lower) |
| "$8,500" as the re-match's typical cost | Lump book; about $10,400 on the units book |
| Option 2's 0.82% as "the on-call figure" | Different mechanism (need left in stocks; worst $12-23k); the D10 on-call figure for option 1 is about 1.6% |
| "About 14%" for option 1 without saying Laura's half is free after 2033 | 1.6% if it stays on call |
| "$145k" as the option 1 minimum, or "$145k again under the team rule" | Median $140k under both rules; $145k in about half of paths |
| Any total that adds 2033 and 2042 money undiscounted (e.g. "all money $205k") | Use the T-bill-credited comparison |
| Haircut results as estimates of real iBond error | Illustrative stress sizes; real error UNVERIFIED |
| Any exact percentage from this file (e.g. "73.1%", "1.59%") without "model" and its basis; any measured number in the IPS | Seed and convention sensitive; IPS:51-52, 68-70 |

---

## 5. Changelog against engine_v3

Every change is a switch; with all of them off, engine_v3b is engine_v3 (§6).

| # | Change (where) | Switch: old → v3b headline | Why | Effect on the numbers |
|---|---|---|---|---|
| B1 | **Units book in the buy-only re-match.** `hold_windows` (engine_v3.py:312-315) booked each held rung's pre-2033 reinvested coupons as one zero-coupon lump paid at maturity, compounding after 2033 although the re-match rule reinvests nothing after 2033. v3b books them as extra units of the same bond bought at that day's ex-coupon price; the extra units' post-2033 coupons wait (0% in the LP, T-bills in reality). Code = verify_engine3's patch, reviewed and reproduced exactly (`engine_v3b.py` `hold_windows`; LP cache key) | `bo_units` False → **True** | verify_engine3 error #8; verify_rematch §2.2(a) | BOTH: re-match cost $8.5k / $26.0k → **$10.4k / $27.3k**; top reach 77.3% → **73.1%**; Laura 2033 $27.0k → $25.3k, 2042 $18.5k → $20.4k; gift 1-in-20 $130.0k → $129.4k; still no payment short. Same on 1R buy-only (77.7% → 77.4%) |
| B2 | **D10 on-call reading (10b) as a first-class flag.** Laura's retained 2033 money stays in VT inside the portfolio and is drawn last for any 2033-2042 gap; what is left returns in 2042. Works with every standard option (1, 3a, 3b, 3r forms, 4) and, new, with the buy-only branch (1RB, BOTH). Refused for option 2 (its own mechanism) and the idealised 1R | `d10_oncall` False → **every row run off and on** | verify_engine3 §3; VREC reading A; votepack D10 | New "on" rows (§1-§3). The "off" rows equal engine_v3 |
| B3 | **2031 minimum headline = team documents' rule**: (R − $3,700 − projected uncovered shortfall) rounded down to $5k (`S/oct20/numbers/numbers_refresh.md:143`; the study's `bottom_adj`, `coupon_options.py:213-224`). The switch already existed in engine_v3 as a sensitivity | `bottom_rule` proj98 → **R3700** (98% rule = §3 sensitivity) | verify_engine3 error #6; verify_vote2 V4 | Medians unchanged ($140k / $135k / $130k); option 1 share at $145k 48.5% → 49.9%; gift below the minimum 0.052% → 0.047% (option 1) |
| S1 | **iBond payout haircut** (sensitivity only; illustrative sizes; method of `S/oct20/redteam_both/`) | `fund_haircut` 0 (always 0 in the headline) | Coordinator request from the BOTH red team | §3 |
| R1 | Reporting only: `bill33_42` (1-year T-bill growth 2033 → 2042), both minimum rules, Laura's retained 2033 money | none | Fair crediting; the rule sensitivity | No path changes |

**Not changed, on purpose:** the lump convention inside `value_at` (rule (a) sizing and every option's realised ladder cash) is untouched; verify_engine3 flagged it as untested for 3r and option 1 (UNVERIFIED). Option 2 keeps engine_v3's study semantics, including holding above-cap money in VT (verify_engine3 error #7). Everything else is engine_v3.

## 6. Validation (done before any number above was used)
- **Switches off = engine_v3, path by path** (`B/scripts/check_v3b.py`, `B/data/out/check_v3b_seed*.txt`): all nine options at 100,000 paths and the buy-only 1R and BOTH (lump) at 20,000 paths, seeds 20261019 and 7, compared with an untouched copy of engine_v3 (`B/ref/engine_v3_orig.py`) on miss, shortfall flag, gift, top, minimum, Laura's 2033 and 2042 money, ladder cost, floor, VT and the projected needs: **maximum difference 0**.
- **D10 = verify_engine3's `oncall10b`** on options 1, 3r, 3r-fix, 3r $15k and 4 (100,000 paths × 2 seeds): maximum difference 0 (option 1: 1.594% / 1.561%, as verify_engine3's 1.59% / 1.56%).
- **Units book = verify_engine3's `bo_units`** (20,000 paths × 2 seeds): maximum difference 0. Independent sanity check (`B/data/out/units_sanity.txt`): at constant shifts of −2/0/+2 points, the units book's value on 1 Jan 2033 is within 0.01-0.35 per 100 face of the lump's (same value, less hidden post-2033 compounding).
- **engY legacy check** (`check_legacy.py`, 100,000 × 2 seeds): byte-identical to engine_v3's logs; path-level difference 0.
- **Cross-checks:** the units-book BOTH figures match verify_engine3's 20,000-path run (73.0%, $10.4k / $27.2k); the haircut rows match the red team's (above).
- **Personal data:** token scan of this file, the CSV, the scripts and the run logs: 0 hits (tokens not printed).

## 7. Reproduce (one command, about 25 minutes on 4 cores)
```
sh /tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/engine_v3b/scripts/run_all_v3b.sh
```
It runs the two legacy checks, `check_v3b.py` (2 seeds), `units_sanity.py`, `run_v3b.py mc` (seeds 20261019 and 7; sensitivities on the same paths), `run_v3b.py hist`, `run_v3b.py boot` (seeds 20261021 and 8), then `make_v4.py`, which writes `B/results_v4.csv` and `B/data/out/tables_v4.md`. Python: `S/venv/bin/python -I -B`. Inputs are byte copies of engine_v3's (`B/data/`).

## 8. Limits and UNVERIFIED
- Same model family as engine_v3: parallel random-walk rates with no mean reversion in the MC; six FRED tenors with linear interpolation for twists; de-meaned bootstrap; US stocks for VT in history; no taxes.
- BOTH assumes the re-match is run in January 2033 from the actual holdings, with the 0% cash rule; new 15-Nov notes for 2036-38 do not exist yet (routine issuance UNVERIFIED); retail bid-ask and tickets UNVERIFIED.
- The fair-crediting total is a convention (2033 money carried at T-bills); it is not risk-adjusted, so D10 on/off totals are not comparable with each other.
- Single-day curve (19 Oct); one curve day moved the ladder by about $1.7k (16 → 19 Oct). Re-price on the 6 Nov close.
- D10 options 10c (on call but moved into Treasuries) and 10d (on call up to a stated amount or date) are not modelled.

## 9. Files (all under `B/`)
`vote_table_v4.md` (this file); `results_v4.csv`; `scripts/engine_v3b.py`, `run_v3b.py`, `check_v3b.py`, `check_legacy.py`, `units_sanity.py`, `make_v4.py`, `run_all_v3b.sh`; `data/out/*.json|txt` (raw runs and checks), `data/out/tables_v4.md` (machine-built tables); `data/raw/fetch_20oct*/` (the two 20 Oct fetches); `ref/` (engine_v3 original, verify_engine3 patch, engY and the agreed JSONs).
