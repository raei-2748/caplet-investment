# Gate B, WS3 (M5 history, M6 rivals, M7 stress): reference build vs blind rebuild

WS3 Gate B reconciler, 30 Sep 2026 (Sydney). This is an AI-generated verification record (Claude Code) for Team
Caplet. It reports MODEL outputs and is not deliverable text. The strategy is not reopened (RUN_PLAN s0). Nothing was
executed externally, and `rab/numbers.yaml` is untouched (sha256 `492ed320...`, the Gate A lock).

**Verdict: PASS.** Every headline key reconciles, and none is UNRECONCILED.
- **Keys:** 278 rows (every headline key of both builds, their sub-figures, and every value in
  `WS3_numbers_proposed.yaml`). 204 are MATCH and 74 are MC NOISE.
- **Decision-relevant rows:** 235 (179 MATCH, 56 MC NOISE).
- **Deterministic figures (all of M5 and M7, and M6's history lens):** these agree to the cent. 19,685 individual rows
  (curve dates, start years, rivals, scenarios, payments) were compared. Every gap is CSV rounding: at most $0.011
  in the 2-decimal files, and $0.50 in the reference build's whole-dollar by-year file.
- **Monte Carlo figures:** percentiles agree within 0.85%, and probabilities within 0.16pp (at most 1.0 standard
  error). The gate allows 2% and 2pp.
- **Bugs in the reference build:** three were found and fixed. None changes a headline number:
  1. A wrong count on a history row for CPPI.
  2. Rounding in the proposed numbers.
  3. A decision file that showed only the base-seed test for gold/REIT.
- **Bugs in the blind build:** none.
- **Specs:** five readings are now clarified in the spec changelogs (M7 has one erratum).

**In plain English.** Two separately written programs give the same history, rival and stress results for
Root-and-Branch. The one close call is gold/REIT against VT. It is on the line in both programs, and both keep VT.

## 1. What was compared

- **Reference build:** `rab/models/m5_backtest.py`, `m6_rivals.py`, `m7_stress.py`, `ws3_numbers.py` (commits f3df738
  and 5bf7edf, specs written first). Outputs are in `rab/results/M5-M7/` and `WS3_numbers_proposed.yaml`.
- **Blind build:** `rab/verification/blind/blind_*.py` (commit 2e3a14c). It was written from `M5/M6/M7_SPEC.md`,
  `rab/data/` and `numbers.yaml` only. Its README declares one leak: it saw the STATUS tail and the reference
  commit message before coding.
- **Evidence the builds are independent:**
  - The code differs: a curve class against functions, and a different sampler layout ((paths, years, assets) against
    (years, paths, assets)). So the same seed gives different Monte Carlo draws.
  - The robustness seed sets differ (20261930-49 against 20260930-49).
  - At every ambiguous point the blind build chose its own reading and reported the alternatives (s3).
- **Reruns today:** `gateB_ws3_checks.py --rerun` copies `rab/` and re-runs both builds, including the fixes below.
  All 67 tracked outputs reproduce byte for byte, except `blind_headlines.json`, which differs only in its time
  stamp.

## 2. Key-by-key table

Every headline key of the reference build is listed; each blind key is named where it matches. All rows are (D),
i.e. decision-relevant. Deterministic tolerances follow the specs: $1 per value, $100 per summary, 0.5pp per share.
Monte Carlo tolerances follow the gate: 2% for percentiles and 2pp for probabilities. The full 278-row table is in
`rab/verification/gateB_ws3/gateB_ws3_table.md`.

| Key | Primary | Blind | Diff | Verdict |
|---|---|---|---|---|
| `m5.cost_of_certainty.today_usd` (= `M5.A.V0_D`) | $289,119.20<br>2020 median $458,828.06<br>peak $470,249.27 (4 Aug 2020)<br>cheapest since 28 May 2002 | same | $0.00 | MATCH |
| `m5.cost_of_certainty.share_months_since_1871_as_cheap` (= `M5.A.share_months_le_V0D_since_1871`) | 0.2327<br>flat-curve bias removed: 0.2354 / 0.2376<br>since 1962: 0.5109<br>cheapest day $110,213.99 (30 Sep 1981) | same | 0.00pp | MATCH |
| `m5.hist.start_years_all_payments_paid` | 149 of 149<br>dearest ladder $411,482<br>top-up in 112<br>floor below $150k in 91 | same | 0 | MATCH |
| `m5.hist.gift_median_usd` (= `M5.B.hist.world_eq.gift_median`) | $131,555.09<br>p10 $66,506.82<br>worst $29,497.94 (2020) | same | $0.00 | MATCH |
| `m5.today_yields.gift_worst_usd` | $158,969.39 (1928 start)<br>p10 $169,055.56<br>median $175,903.02 (= `M5.B.today_yields.world_eq.gift_median`)<br>top reached 84.6%<br>floor $150k in 149 of 149 | same | $0.00 | MATCH |
| `m5.H9_reverified.rescaled_total_worst_usd` | $168,730.15<br>raw $171,524.62<br>p10 $185,123.64<br>median $214,419.30 | blind has no H9 row (not in the spec); third computation here: same | $0.00 | MATCH |
| `m6.rec.mc_T33_median_usd` (= `M6.MC.REC.T33_p50`) | $206,725 (p5 $181,344, p95 $251,749)<br>gift p5 / p50 $164,589 / $173,982<br>never short; $150k certain | $206,777 ($181,352 / $252,228)<br>gift $164,579 / $173,998<br>never short; $150k | +$52 (+0.03%); p95 +0.19% | MC NOISE |
| `m6.sixty_forty_whole.mc_payment_short` (= `M6.MC.R2.unfunded_share`) | 1.272% (history 2 of 149; T33 p5 $53,342)<br>glide path 0.170%<br>growth-first 2.235% | 1.2505% (2 of 149; $53,653)<br>0.179%<br>2.2675% | -0.02pp (0.6 SE); p5 +0.58% | MC NOISE |
| `m6.H16_reverified.*` (= `M6.H16.deposit_150k`) | 2.235% / 10.621% / 35.086% | 2.268% / 10.683% / 35.242% | at most +0.16pp (1.0 SE) | MC NOISE |
| `m6.cppi3.mc_floor_broken` (T33 < $150k) | 1.986%<br>m=5: 26.25%<br>T33 median $198,871 | 1.959% (1 - `promised_150k_met_share`)<br>26.38%<br>$198,892 | -0.03pp (0.6 SE) | MC NOISE |
| `m6.tips_ladder.mc_any_payment_short` | 59.96%<br>history 92 of 140<br>1.43x ($124,584 more) for 95% delivery | 59.96%<br>92 of 140<br>1.43x / $124,584 (third computation on the blind build's paths) | 0 | MATCH |
| `m6.fund_choice.gold_reit_spread_ratio` (= `M6.fund_decision.any_switch`) | 0.8992 on seed 20260930<br>tests 1-3 pass<br>spread test passes on 17 of 20 other seeds<br>**KEEP VT** | 0.8999<br>pass<br>14 of 20<br>**KEEP VT** | +0.0008 | MC NOISE, and the decision is identical. Without noise: 0.8991 in both builds (s4) |
| `m7.threshold.floor_150k_holds_to_bp` (= `M7.threshold.b_fund0_zero_floor_150k_bp`) | 109.32bp<br>top-up starts 26.20bp<br>a payment unfunded 428.41bp | same | <0.0001bp | MATCH |
| `m7.stress.worst_gift_usd` | $147,189.01 (S2b)<br>all 13 scenarios fund every payment<br>every gift and real gift equal (S0 $174,951.79 = `M7.S0.gift`) | same | $0.00 | MATCH |
| `m7.downgrade_2011.dy_bp` (= `M7.downgrade.S4a.dgs10_change_pp`) | -56bp (Fitch +7, Moody's +3)<br>S4a: ladder $308,897.07, fund $20,357.03 | same | 0 | MATCH |
| `m7.real_value.pay_2042_breakeven_usd` (= `M7.real_value.breakeven_T10YIE_2.34.real_2042`) | $35,341.81 (all ten $393,053.08)<br>1970s path: $18,414.19 / $226,340.66<br>history p5 / p50 / p95: $18,589 / $34,190 / $71,621<br>H19 $42,063.26 / $33,681.25 | same | $0.00 | MATCH |

**Proposed numbers** (`WS3_numbers_proposed.yaml`, 28 entries): all 144 values were checked against the blind build,
giving 107 MATCH and 37 MC NOISE. These are the numbers WS1 would lock, so all are decision-relevant.

## 3. Every difference, its cause and what was done

1. **Monte Carlo noise (M6 MC lens).** Percentiles differ by at most 0.85% (CPPI m=5 p95) and probabilities by at
   most 1.0 standard error.
   - Cause: the two samplers lay out the draws differently, so seed 20260930 gives different paths in each build.
   - The TIPS inflation paths are the exception: the spec fixes their seed and draw order, so they are identical.
   - Class: ignore.
2. **Gold/REIT at the threshold.** The spread ratio is 0.8992 against 0.8999, and the seed tally is 17/20 against
   14/20.
   - Cause: noise, plus different seed sets. The large-sample check (s4) gives 0.8991 in both builds.
   - The decision is identical in both builds on all three counts: the base seed passes tests 1-3, the switch is not
     seed-robust, and VT stays.
   - Class: note-in-Final-Report. The memo now says this is a close call, not a clear loss for gold/REIT
     (`rab/decisions/D_fund_choice.md`, Gate B paragraph).
3. **Bug in the reference build: CPPI history count.** The M6 report and card said the $150k floor was "broken in 1"
   window for both multipliers. The right counts are 94 (m=3) and 106 (m=5) of 149.
   - Cause: the column is NaN for non-CPPI rows, so it is object dtype. A pandas sum of numpy bools in such a column
     is a logical OR, which gives 1.
   - The per-window CSV was always right, and so is the blind build.
   - Fixed in `m6_rivals.py`. `M6_CARD.md` is corrected, with a note that REC's own floor is below $150k in 91 of 149
     windows at history's yields, so only the MC lens separates the two.
   - Not a headline number; nothing else used it.
4. **Bug in the reference build: rounded probabilities.** `ws3_numbers.py` read the 2-decimal CSV, so the proposed
   numbers said:
   - glide path `mc_short: 0.0` (true 0.17%)
   - 60/40 `0.01` (1.27%)
   - growth-first `0.02` (2.235%)
   - CPPI `0.02` / `0.26` (1.99% / 26.25%)
   - H16 `0.022` / `0.106` / `0.351`

   Fixed: the builder now reads the full-precision JSON, and H16 carries 4 decimals. **WS1 must merge the fixed
   file**, never the earlier one. "Glide path: never short" would be false.
5. **Presentation fault in the reference build.** `fund_choice_decision.csv` recorded only the base-seed column, which
   says "SWITCH" for gold/REIT.
   - Fixed: the file now has `final` (KEEP VT / KEEP VT (not seed-robust)), the seed tallies, and
     `decision_seed_20260930`.
   - The report prints a FINAL line for each alternative.
6. **Spec readings, clarified in the changelogs (no number changed):**
   - M7 S2 erratum: "/100" on `jpn_ltrate`. Both builds used percentage points; the blind build's `S2_lit` row
     (gift $163,194) is the unused literal reading.
   - M7 downgrade base: the announcement day's close, since all three came after the close.
   - M5 "lowest since 1871": month starts ($111,249, 1 Oct 1981) against every curve date ($110,214, 30 Sep 1981).
     Both builds report both.
   - M5: the blank 11 Oct 2010 row is dropped.
   - M6 R5 "floor broken" means T33 < $150,000. The blind build's 1.60% "cushion negative 2028-32" is a different
     statistic.
   - M6 R6 "unfunded" means at least one payment below $50,000.
   - M6 robustness seeds were not fixed by the spec.
7. **H9 is not in the blind build** (the spec does not ask for it). It was recomputed here from `annual_history.csv`
   and the blind build's stock fund, and it matches to the cent.

## 4. Monte Carlo precision: the one threshold

The fund rule switches only if the gift's spread is at most 0.90 of VT's. Both builds' own samplers were re-run on 100
fresh seeds (20262000-99, used by neither build) at 200,000 paths each (`gateB_ws3_mc_precision.py`, about 50 s).

| | Reference sampler | Blind sampler |
|---|---|---|
| Mean A4/A0 spread ratio (standard error) | 0.8991 (0.0001) | 0.8991 (0.0001) |
| Pooled 10,000,000 paths | 0.8989 | 0.8992 |
| Seed-to-seed sd at 200,000 paths | 0.0010 | 0.0010 |
| Share of 200,000-path seeds at or under 0.90 | 80% | 85% |
| Bad-case (p5) gift gain / median gain | +$1,164 / +$342 | +$1,165 / +$341 |

**What this shows.** Gold/REIT is really 0.001 under the bar, so at the spec's 200,000 paths the spread test fails on
about 1 seed in 5. Under s7 (the same answer on every seed) the switch is therefore not robust, and VT stays: the
pre-registered rule, applied as written, gives KEEP VT in both builds. With 10 times more paths, tests 1-3 would pass
every time, and test 4 would decide. Test 4 asks whether WInS lists GLD and VNQ (UNVERIFIED), and whether two more
$25 trades are worth a bad-case gain of about $1,200 (0.7% of the gift). This is a note for the team, not a change:
the strategy keeps VT.

## 5. Reconciliation with insight_v1 (`rab/inventory.md` s2)

| Ref | insight_v1 | Rebuilt here | Why it differs (if it does) |
|---|---|---|---|
| H8 | REC total $182k / $207k / $250k; gift $165k / $174k / $188k; P(top) 73% (25 Sep) | Both builds: $181.3-181.4k / $206.7-206.8k / $251.7-252.2k; gift $164.6k / $174.0k / $188.6k; P(top) 73.4% | Within $2k at every point, and E6 [2] re-run today (read-only) still prints the H8 figures. Causes: the 28 Sep basis (leftover $7,582 vs $7,736; 5-year yield 5.06% vs 4.98%; bond fund 5.06% vs 5.00%), M6's 9-asset JPM draws, and seed 20260930 vs 20260927. WS2's M3 owns H8 |
| H9 | Rescaled worst $169k (1928); raw worst $171k; p10 $185k; median $214k | $168,730 / $171,525 / $185,124 / $214,419 (reference and third computation) | Reproduced. E6 [5] re-run today prints the H9 figures, with the top reached in 77%. The raw worst is $171.5k because the 28 Sep stock fund ($40,736) is about $290 larger than E6's 25 Sep figure ($40,443, from E4's constants). M5's own worst ($159k gift) is lower because it adds 1872-1927 and uses a world fund |
| H12 | Bad 2031-32: gift median $169k, never below the bottom | Not an M5-M7 output. The nearest are S6 (2008 in 2028) $164,302 and S5 (Depression) $159,298, both builds | A different question (a named episode, not the bottom decile). Both builds agree the gift never falls below the floor once it is bought. WS2 owns H12 |
| H13 | Rates fall first (25 Sep): fund $20-23k at -50bp, $1-7k at -100bp, none at -150bp (floor $127-137k) | Both M7 engines on 28 Sep: $22,590 / $3,626 / $0 (floor $130,724) | Equal to the low end of WS4's Gate B ranges ($22,590-25,419 / $3,626-9,366; floor $130,724-140,469). A fall that lasts to Jan 2028 gives the smallest fund. There is more room on 28 Sep than on 25 Sep |
| H16 | Growth-first misses 3.2% / 13.7% / 40.8% | 2.2-2.3% / 10.6-10.7% / 35.1-35.2% (both builds) | Superseded, not reproduced: M6's bond fund earns today's 5.06% (JPM 4.00% before), so the whole-portfolio plan misses less. The builds agree within 0.2pp |
| H17 | 2020 median ~$459k; max $470,249 (4 Aug 2020); cheapest since 28 May 2002; <= $300k on 11.1% of days since 2000 | $458,828; $470,249 (4 Aug 2020); 28 May 2002; 11.1% (both builds) | Identical |
| H18 | A payment partly unfunded on 197 of 6,688 days, all in 2020-21; worst $20,588 (4 Aug 2020) | Third computation with the blind curve code: 197 of 6,688 (2020, 2021); worst $20,588 (4 Aug 2020) | Identical. M5 finds 0 of 149 because no 1 January start hits these days (M5 card) |
| H19 | $42,063 (2033), $33,681 (2042) at 2.5% | $42,063.26 / $33,681.25 (both builds) | Exact with its own convention. The M7 headline ($35,342) is in 1 Jan 2027 dollars at the 2.34% breakeven, so it is a different number. The 2.5% is now sourced to JPM |

## 6. Triage (contradiction rule: strategy unchanged; nothing applied to the IPS or the Sheet)

**Fix before 6 Nov (RAB files only):**
- WS1/WS0: when numbers.yaml is next locked, merge the fixed `rab/results/WS3_numbers_proposed.yaml` (this commit),
  now Gate B reconciled. Add a changelog line.
- Unchanged by this gate, still open for the team (WS3 cards): the "certain by construction if..." wording for the
  $150k bottom, and one IPS sentence that inflation is the risk left with Laura.

**Note in the Final Report:**
- The fund choice is a close call: gold/REIT sits at the line, the pre-registered rule keeps VT, and the gain would
  be about $1,200 at the bad case.
- CPPI: its $150k promise is missed in 2.0% of MC paths (m=3). The history lens cannot separate it from REC, because
  history's lower yields put both floors below $150k in most eras.

**Ignore:** MC sampler noise, the seed-set difference, and the spec readings in s3 #6.

## 7. What Gate B cannot catch

Both builds follow the same specs, so the assumptions they share are not tested by the blind rebuild:
- Flat pre-1962 curves.
- The world-fund proxy at today's 62% U.S. weight (it beat real VT by about 1 point a year in 2009-2025).
- JST, Shiller and Damodaran history taken as the guide.
- i.i.d. lognormal JPM returns with no fat tails (WS2's M3 has them).
- The adopted 2031 rule applied to rivals that would announce differently.
- A home-price index in place of REITs before 2009.
- MODEL STRIPS prices with no mark-up.
- **Zero-coupon rungs with no coupon reinvestment** (M5 spec, M1 A5). Every "never short" and "all payments paid" key
  above (M5 149 of 149, the M6 REC lens, all 13 M7 scenarios) is reconciled *on this basis only*.
- Parallel curve shifts in M7.
- GLD and VNQ listings on WInS (UNVERIFIED).

WS7 should challenge these.

**Added 30 Sep, after WS7's challenge (outside this gate; not re-derived here).** WS7 found coupon reinvestment to be
the weakest load-bearing assumption (`rab/redteam/ws7_assumptions_reinvest_check.py` and its `_output.txt`, commit
9db8d35 on rab/ws7, MODEL). The adopted reading R1(a) means the real plan holds WInS coupon bonds and iBonds, not
STRIPS. The payments then total $500k only if coupons are reinvested at about 4.97% or more. So any memo or deliverable
that quotes a WS3 "never short" figure must say "on a zero-coupon (STRIPS) basis". This does not change any Gate B
verdict, because both builds share the basis. It is WS7's finding to triage, not this gate's.

## 8. Files and rerun

- **Record:** this file.
- **Checks:** `rab/verification/gateB_ws3/gateB_ws3_checks.py` writes `gateB_ws3_results.json` and
  `gateB_ws3_table.csv` / `.md` (278 key rows, 9 row-level comparisons, the insight_v1 table).
  `gateB_ws3_mc_precision.py` writes `gateB_ws3_mc_precision.json`.
- **Changed at this gate:**
  - `rab/models/m6_rivals.py` and `ws3_numbers.py` (s3 #3-5)
  - `rab/results/M6/` (report, JSON, summary, decision CSV; the figures are unchanged)
  - `rab/results/WS3_numbers_proposed.yaml`
  - `rab/models/M6_CARD.md`
  - `rab/decisions/D_fund_choice.md`
  - changelogs in `M5_SPEC.md`, `M6_SPEC.md` and `M7_SPEC.md`
  - The blind build is unchanged.
- **Rerun** from the worktree root (seed 20260930):
  - `/Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws3/gateB_ws3_checks.py --rerun` (about 25 s)
  - then `.../gateB_ws3_mc_precision.py` (about 50 s)
- **Re-verified 30 Sep, after the decision-memo commit 0b6b5cb:** `--rerun` again reproduces all 67 tracked outputs
  byte for byte (only the blind headlines' time stamp differs). It still gives 278 rows: 204 MATCH, 74 MC NOISE and 0
  UNRECONCILED. `numbers.yaml` is still `492ed320...`.
