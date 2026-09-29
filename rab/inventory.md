# RAB inventory: what already exists, and what later streams reuse, re-verify or replace

WS1-inventory, 2026-09-30 (Sydney). AI-generated research (Claude Code) for Team Caplet; no deliverable text.
Read with `RUN_PLAN.md`. Paths are relative to the repo root (`/Users/ray/Research/rab-kit`, which holds the same
committed files as the main checkout; the main checkout differs only by an uncommitted `docs/AI_USE.md`).

**Verdicts.** REUSE = use as is. RE-VERIFY = sound, but re-run on the `rab/numbers.yaml` basis (28 Sep curve, WInS
instruments) or fix one named assumption first. REPLACE = built for a superseded design or book; build new, borrowing
code where noted. ARCHIVE = history only, do not use.

**Adopted-strategy test.** "Matches" means the item models Root-and-Branch as adopted: 2027 ladder bought longest
first; 2028 deposit completes the ladder, then buys a floor repaying $150,000 by late 2032, rest in one world stock
fund held to 2033; nothing traded in 2031; range = floor to floor + half the fund; gift capped at the top.
insight_v1 calls this design **REC** (E4 "dated barbell"). Its **ALT** (60/40 sleeve + 80% locked in 2031) and every
D3/D5/D6 "sleeve" model are the superseded design.

---

## 0. The current WInS book (for decision D7)

Read-only from Sheet `1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM`, 2026-09-30 00:15 AEST.

- **Confirmed: tab `Portfolio` is the current planned book** and it supersedes insight_v1's (ii)R book
  (IEF 23.5 / TLH 42.5 / IBTM 24.3 / VT 8.7 / cash 1). Nothing is executed yet: `Trade Log` is empty, every row says
  "vote pending", the header says "Provisional until the team votes on 1 Oct 2026".
- Holdings: IBTM 32.5% (2033 payment + floor), IBTO 7.8, IBTP 7.4, IBTQ 7.0, IBTR 6.6, T 4.750% 15-Feb-2037 6.6,
  T 4.500% 15-May-2038 6.2, T 4.375% 15-Nov-2039 5.7, T 4.250% 15-Nov-2040 5.3, T 3.125% 15-Nov-2041 5.1, VT 8.7,
  cash 1.1. Sums to $300,000.
- How it is built (from the cell formulas): the split 65.9 / 24.3 / 8.7 / 1.1 is typed in (E6 [7], 25 Sep curve,
  exact-date ladder). Each rung = 65.9% x that rung's share of `Book L` cost; IBTM adds the 24.3% floor. ETF prices
  are live `GOOGLEFINANCE(...,"price")` (they move whenever the Sheet recalculates); bond prices are typed-in WInS
  clean + accrued.
- `Book L` (literal ladder) discount factors: **WS1 reproduced all ten exactly** with the D1 curve method on the
  28 Sep curve, at each holding's end date (iBonds 15 Dec, bonds at maturity). Target $290,379; cost $292,226 after
  rounding up to whole shares / $1,000 face; 10 trades, $175 commission, $7,599 cash left.
- **No repo script builds either tab.** M1 must rebuild them in code and dual-price them (Gate A).

---

## 1. Model map (M1-M9 and the trade kit)

### M1 Ladder pricer

| Item | What it computes | Inputs / date | Matches adopted + current book? | Verdict |
|---|---|---|---|---|
| `research/insight_v1/scripts/D1_purchase_rule.py` | Ladder cost forward to 1 Jan 2027 (exact-date and Nov-15 STRIPS), rate-fall table, longest-first split, break-evens, every-2026-date replay, lognormal gap odds, joint tail | Any par-curve CSV (default 25 Sep snapshot); method: 0.5y bootstrap, log-linear DF, days/365.25 | Yes for Laura's real ladder; not the WInS instruments | **REUSE** as the reference curve method. Re-ran today: exit 0, reproduces $294,387 / 19bp (25 Sep) |
| `research/insight_v1/verification/ladder_2026-09-28/` (commit 84e7010: README, `reconcile.py`, curve CSV, D1 output, `gpt/`) | 28 Sep rerun ($289,119 today / $292,418 fwd, 26bp) and blind GPT check ($289,003 / $292,214, 26.9bp); gap explained by day count + short nodes | Treasury par curve 28 Sep 2026 (home.treasury.gov, fetched 29 Sep) | Yes (real ladder) | **REUSE**. `reconcile.py` re-ran today, identical to the cent |
| Sheet tab `Book L` | WInS literal ladder: 5 iBonds + 5 coupon bonds sized to $50k x DF(end date) | 28 Sep curve; WInS 28 Sep clean prices + accrued typed in; ETF prices live | Yes (this is the current rung set) | **RE-VERIFY**: accrued typed for one date (e.g. 0.560 on the Feb-2037) must be recomputed for the trade date; ETF prices unstamped |
| Sheet tab `Portfolio` | Current book (section 0) | as above | Yes | **RE-VERIFY**: 65.9/24.3/8.7 split is on the 25 Sep curve and exact-date ladder; recompute on the 28 Sep basis |
| `research/insight_v1/scripts/D1_wins_rung.py` | Coupon-bond model price, accrued, yield, duration from the curve (4.125% 2032, 4.375% Nov-2039, 4.25% Nov-2040) | 25 Sep curve | Two of its bonds are in the current book | **REUSE** the bond pricer for the WInS yield check; its hedge sections are superseded |
| `research/insight_v1/scripts/D3_funded_status_log.py` | Values ETFs bond by bond from holdings on any curve; payments' value; log mode | Holdings 24 Sep (`wins_now/S1_fund_holdings_snapshot.csv`, includes IBTM-IBTR); 2026 curves | Code filters to IEF/TLH/TLT only | **RE-VERIFY**: extend to IBTM-IBTR for look-through iBond pricing and the tested-window log |
| `research/insight_v1/wins_now/S1_hedge_weights.py` + `S1_mspd_table5_2026-08-31_fixed_2032plus.csv` | STRIPS ladder by CUSIP (Treasury MSPD Table V), liability value $292,264, duration 9.90y, DV01 $289/bp | 25 Sep curve; MSPD 31 Aug | Real-ladder CUSIPs yes; IEF/TLH hedge weights no | **REUSE** CUSIP map and DV01 method; hedge-weight part REPLACE |
| `research/insight_v1/scripts/A2_curve_recheck.py` | Exact-date ladder on any date, 2026 history and volatility, forward values at 2031/2033 | Live treasury.gov CSV (writes/fetches) | Yes (exact-date) | **REUSE** for cross-check only |
| `research/verified_2026-09-27/official_curve_pv.py` | First verified ladder value $292,264 (exact dates) | Fixed to 25 Sep | Yes, but fixed date | **ARCHIVE** (trading_notes_pack s7 already forbids it for new dates) |
| `research/insight_v1/scripts/D9_numbers.py` [3] | Re-prices the ladder on the latest curve; DV01; daily 10y vol 4.45bp | 25 Sep + latest | Yes | **REUSE** for the Friday refresh |
| `rab/rescued/ladder_history_2000_2026.py` (new today) + `rab/data/treasury_par_2000_2026/` | Ladder cost on all 6,688 curves since 2000; unfunded-part check | 27 treasury.gov files, byte-identical to a fresh download 30 Sep | Yes | **REUSE** (rescued from an uncommitted /tmp script; see section 3) |

**M1 gaps (nothing exists):** (1) code that prices every `Portfolio` holding (iBonds by look-through, bonds from the
curve, VT/cash); (2) an automated yield check of WInS bond prices (the Book L "-8bp ... +15bp" checks and the two
stale prices have no code); (3) a blind second pricer of the WInS book (the GPT check covered only the STRIPS ladder).

### M2 Rate paths to Jan 2027

| Item | What it computes | Inputs / date | Matches? | Verdict |
|---|---|---|---|---|
| `D1_purchase_rule.py` [6] (and the 28 Sep rerun) | P(gap > 0) with a zero-drift lognormal on 2026 realised vol (7.2%/yr) | 25 Sep: 30.5% Nov-15, 24.3% exact; 28 Sep: 24.2% Nov-15, 18.7% exact | Yes | **RE-VERIFY** (horizon now 93 days from 30 Sep) |
| `AX1b_rates_audit.py` [B], [C] | Gap odds under other vols and "unchanged curve" drift (+$1,044, lifts odds ~3pp); FRED DGS10 68-trading-day windows | FRED DGS10 to 24 Sep (`scripts/data/D3/fred_DGS10.csv`) | Yes | **REUSE** as the model-free check. Re-ran today: falls >= 26bp in 27.6% (since 1962), 31.1% (since 1990), 28.5% (since 2000) of windows |
| `strategy_mc_v2.py` switch (a) | Pre-2027 rate move, sd 0.37pp / 0.48pp -> 30.2% / 34.4% (25 Sep) | JPM + assumed sd | Yes | **RE-VERIFY** |
| `D1_purchase_rule.py` [7], `AX1b` [D] | Buy at once vs 4 tranches vs trigger (staging has no reliable gain) | 25 Sep | Yes (R1 rule) | **REUSE** for the hedge memo |
| `T2_red_team_checks.py` [2]-[4], `D7_rule_trigger_odds.py` | Odds of a >=10bp move in the tested window (52% for an Oct 2 fill, 40% for Oct 9); 10y daily vol | 2026 curve | Yes | **REUSE** for the tested note |
| `model/laura/engine.py` (commit 2b9376c only) | Annual discrete Vasicek on one flat yield | 23 Sep assumptions | Old strategies A/B/C | **ARCHIVE** for M2 (annual step too coarse for 3 months) |

**M2 gaps:** no AR(1)/Vasicek fitted to daily data; no reconciliation table across the five estimates. The "1 in 3"
headline was built on the 25 Sep 19bp headroom; at 26-27bp (28 Sep) every method gives lower odds (see section 2).

### M3 Branch Monte Carlo (2028-2033)

| Item | What it computes | Inputs / date | Matches? | Verdict |
|---|---|---|---|---|
| `research/insight_v1/scripts/E4_rival_numbers.py` (`rival_design`) | REC engine: floor, stock fund, 2031 range, capped gift, kept money; also E1/ALT | D6 engine: seed 20260927, 200,000 paths, lognormal fitted to JPM ACWI 7.00% compound / 8.28% arithmetic / 16.78% vol; ladder $292,264 (25 Sep exact-date), leftover $7,736; floor at 5y 4.98% | **Yes, this is Root-and-Branch** | **RE-VERIFY** on the 28 Sep basis (5y 5.06%; leftover per the WInS ladder) |
| `research/insight_v1/scripts/E6_final_checks.py` | Headline REC numbers [1]-[8] | as above; Vanguard-like 5.08% variant; history rescaled | Yes | **REUSE** as the reference to reconcile against. Re-ran today with the rab-ws env: every figure identical |
| `research/insight_v1/scripts/F1_floor_variants.py` | Floor $150k/125k/100k/75k/50k/0 + all-Treasury control | E4 engine | Yes | **REUSE** (feeds M4/M8). Re-ran today: identical |
| `strategy_mc_v2.py` switches (e) fat tails (t, nu=4), fees | Old sleeve design | 25 Sep | No (ALT) | **REPLACE**; borrow the t-tail switch |
| `D2_equity_premium.py` | Equity premium vs locked Treasuries: JPM 2026 LTCMA, Vanguard VCMM (30 Jun 2026 run), FactSet P/E 25 Sep | as dated | Inputs yes | **REUSE** inputs; check whether JPM's 2027 LTCMA is out (UNVERIFIED) |

**M3 gaps:** no Shiller/historical bootstrap engine for REC (only E6 [5] window replay); no Bayesian model with an
uncertain mean. Seed differs (20260927 vs the run's 20260930): report MC noise when comparing.

### M4 Cap optimiser (D6: the share s of the fund added to the gift)

| Item | What it computes | Matches? | Verdict |
|---|---|---|---|
| `E4_rival_numbers.py` / `E6_final_checks.py` | s = 1/2 default; s = 3/4 and 1 tested (s = 1 keeps nothing when stocks fall; s = 3/4 keeps $8k at p5) | Yes | **RE-VERIFY**; the grid is three points, no frontier |
| `F1_floor_variants.py` | Floor size trade-off (each $25k less floor: median +$2-3k, p5 -$9-10k) | Yes | **REUSE** |
| `D3_range_rules.py`, `D5_range_and_flexibility.py`, `AY1_audit_checks.py` | Range/confidence rules for the 2031-lock sleeve (floor share a, top percentile q) | No (ALT) | **REPLACE**; reuse only the P(below/within/above range) bookkeeping idea |

**M4 gap:** no multi-objective search (pymoo) over s, floor and cap. `open_questions.md` D6 default: s = 1/2.

### M5 Century backtest

| Item | What it computes | Matches? | Verdict |
|---|---|---|---|
| `E6_final_checks.py` [5] / `E4` section 5 | Every 6-year window 1928-2025 (93) placed in 2027-32, raw and rescaled: REC worst $171k raw / $169k rescaled (1928 start) | Yes, but returns only; today's yields throughout | **REUSE**; extend |
| `rab/rescued/ladder_history_2000_2026.py` | Ladder cost with historical curves since 2000 | Yes (ladder leg) | **REUSE** |
| `D3_history_stress.py` | Named episodes + 93 windows | No (old plan, ratchet, barbell) | **REPLACE** (borrow the episode placement code) |
| `model/laura/data/us_history_1928_2025.csv` (commit 2b9376c, branch `local/laura-work-2026-09-25`; main checkout has only `.pyc`) | Damodaran 1928-2025 incl. 10y yield start/end and CPI | Data only | **RE-VERIFY** then reuse (the insight_v1 snapshot lacks yields and CPI) |
| `scripts/data/D3/damodaran_histretSP_1928_2025.csv`, `fred_DGS2/5/10.csv` | S&P 500 TR, T-bill, 10y TR, Baa, real estate, gold; daily CMT yields to 24 Sep | Data | **REUSE** |

**M5 gap:** no backtest that uses each start year's own yields for the ladder and floor together with that period's
returns (RUN_PLAN M5). Only U.S. stock data; no world-index history in the repo.

### M6 Rivals

| Item | What it computes | Matches? | Verdict |
|---|---|---|---|
| `E4_rival_numbers.py`, `E6_final_checks.py` [2] | REC vs ALT (2031 lock), equal-stock variant | Yes | **REUSE** |
| `E7_tournament_field_numbers.py` + `phase_E/tournament/firm_*.md` | Five glide paths (65->20, growth-first 75%, themed, 60/40->40/60, optimiser) on `strategy_mc.py`; growth-first misses a payment 3.2% / 13.7% / 40.8% (deposit $150k / $75k / $0) | Rivals, old engine (25 Sep, $292,264) | **RE-VERIFY** on the M3 basis |
| `D3_lock_frontier.py`, `B10b_designer_checks.py` | Partial lock 70-95% ("price of certainty" frontier) | Rival | **RE-VERIFY** |
| `D3_barbell.py` | Barbell (lock 50/65/80% in 2028, rest equity), precursor of REC | Near-REC | **ARCHIVE** (E4/E6 supersede) |
| `S2_growth_sleeve.py`, `wins_now/S2_growth_sleeve.md` | VT vs U.S.-only (JPM), S&P 500 concentration, sector-fund fallback | Fund choice | **REUSE** for "VT vs alternatives" |

**M6 gaps:** TIPS ladder, CPPI, VTI+VXUS / tilt / +gold/REIT (Damodaran has gold and real-estate columns) scored on
the M3 metrics.

### M7 Stress

| Item | What it computes | Matches? | Verdict |
|---|---|---|---|
| `E6_final_checks.py` [3], [8] | Bottom-decile 2028-30 / 2031-32; rates fall before Jan 2027 (fund $20-23k at -50bp, $1-7k at -100bp, none at -150bp) | Yes | **RE-VERIFY** (25 Sep basis) |
| `D3_joint_tail.py`, `D1_purchase_rule.py` [8] | Rates fall AND the 2028 deposit is late/small/missing | Yes (ladder leg) | **REUSE**; 28 Sep figures in the verification folder |
| `D4_facility_purchasing_power.py`, `A2_twd_vol.py`, `A2_taiwan_cci.py` | USD/TWD and Taiwan construction-cost risk vs market risk | Built on the old sleeve for the market leg | **RE-VERIFY** (FX and CCI legs reusable) |
| `strategy_changes.md` I4 | Real value of $50k at 2.5% inflation: $42,063 (2033), $33,681 (2042) (ASSUMPTION) | Yes | **REUSE** (recompute with a sourced inflation input) |

**M7 gaps:** no scenario engine for 1970s-type yields, Japan, 2022 or a U.S. downgrade applied to REC.

### M8 Sensitivity

Nothing exists. One-way pieces to seed the tornado: E6 [4] (lower return house), [6] (fees), [8] (rates fall);
F1 (floor); E1 grid (equity house x bond return x fee). **Build new** (SALib is in the env).

### M9 Security selection

| Item | What it covers | Date | Verdict |
|---|---|---|---|
| `wins_now/S1_treasury_sleeve.md` s1c | iBonds table: holdings, duration, YTM, assets, volume (IBTM 216k, IBTO 226k, IBTP 111k, IBTQ 100k, IBTR 69k shares/day; IBTR $34m assets); no iBonds 2037-2043 exist | issuer pages 24-25 Sep | **RE-VERIFY** volumes and assets |
| `wins_now/S1_fund_holdings_snapshot.csv` | Every bond held by 15 funds incl. IBTM-IBTR | 24 Sep | **REUSE** (refresh before Friday if possible) |
| `securities_and_allocation.md` s6, `wins_now/securities_and_allocation_v1.md` s12 | Fund facts (expense, duration, closes) for IEF, TLH, VT, VTI, VXUS, IBTM ... | 24-25 Sep | **REUSE** facts; the book in s1-s4 is **REPLACE** |
| Sheet `WInS Notes` | Names and 28 Sep close/volume for IEF, TLH, IBTM, VT, VGIT, SPTI, VTI, VXUS, TLT, SPTL, SGOV; rules; 2032 note not listed | read in WInS 29 Sep | **REUSE**; missing IBTO, IBTP, IBTQ, IBTR and the five bonds |
| `D10_wins_book_compliance.py`, `T1_ticket_v1_numbers.py` | Volume and trade-count checks, share counts, cash float | 25 Sep, old book | **REPLACE** (borrow the checks) |

**M9 gap:** no screen per slot (best security + runner-up) for the current rung set; no recorded WInS name/volume for
IBTO-IBTR; no alternates listed for the five bonds.

### Trade kit (WS6)

| Item | What it covers | Matches current book? | Verdict |
|---|---|---|---|
| `research/insight_v1/trading_notes_pack.md` | Gate, calendar, order tables, 3-note menu (A TLH, B building minimum, C VT), per-note elements and banned words, 300-char rule, tested-window capture, reflection and submission checklists | Orders and note A are for (ii)R (TLH no longer held); B (IBTM floor) and C (VT) still fit | **RE-VERIFY**: keep gate, calendar, checklists; rebuild orders and note A; re-check the ban on "match" (it was TLH-specific; the IPS now says "matched by a dated Treasury ETF or bond"); tested-window measure 2 must switch from IEF+TLH to the dated holdings |
| `wins_now/T2_red_team.md` + `T2_red_team_checks.py` | Overnight-gap and cash-float checks, share counts from last close | Old book | **RE-VERIFY** (methods reusable) |
| `research/insight_v1/scripts/D9_draft_checker.py` | Counts words/characters and flags banned words in team drafts | `LIMITS["note"] = None` | **RE-VERIFY**: set the note limit to 300 characters (WInS maxlength, `WInS Notes`) |
| `research/insight_v1/scripts/D12_note_roles.py` | Role-word test per holding | Old book | **RE-VERIFY** |
| `research/insight_v1/scripts/E5_premortem_checks.py` | Deadline clock in AEST/AEDT (DST starts 4 Oct Sydney, ends 1 Nov U.S.) | Dates still valid | **REUSE** |
| Sheet `Trade Log` | Columns incl. note copied exactly, note length, within limit | Ready, empty | **REUSE** |
| `phase_D/trading_now_brief.md`, `wins_now/securities_and_allocation_v0.md`, `_v1.md` s1-s11 | Earlier tickets | Superseded | **ARCHIVE** |

### Outside insight_v1

| Item | Verdict and reason |
|---|---|
| `src/wharton_ic/` (93 modules: DCF, comps, optimizer, backtest, stress, rules registry) | **ARCHIVE** for RAB: a stock-picking framework; no liability or ladder logic. `config/competition.yaml` on this branch has `starting_capital_usd: null` and trading rules "AWAITING_OFFICIAL_MATERIAL" (not the $100k/$0 noted as stale; still unfilled) |
| `model/laura/` (source only in commit 2b9376c on `local/laura-work-2026-09-25`) | **ARCHIVE** the engine (strategies A/B/C, flat-yield Vasicek, 80/20 sleeve); **RE-VERIFY** and reuse its history CSV (yields + CPI) |
| `research/council_2026-09-27/` (quant, actuary, referee scripts) | **ARCHIVE** (pre-insight_v1; superseded by `verified_2026-09-27` and insight_v1) |
| `research/verified_2026-09-27/strategy_mc.py` | **REUSE** only as the engine behind E7 rivals and D6/E4 reproduction |
| `docs/wharton_workflow_v2.md` l.115-116, `docs/wharton_rule_system.md` l.53-68, `docs/trading_notes_and_journal.md` l.14 | Stale "Dec 4" trading/notes dates: **ignore** (never cite) |

---

## 2. insight_v1 headline numbers later streams must reconcile with

All MODEL outputs unless marked. "Today" = re-run by WS1 on 2026-09-30 with `/Users/ray/Research/rab-ws/.venv/bin/python`.

| # | Number | Basis | Source | Re-run today | Must reconcile |
|---|---|---|---|---|---|
| H1 | Ladder $294,387 fwd 1 Jan 2027, headroom $5,613 = 19bp (Nov-15 STRIPS) | 25 Sep curve | `D1_purchase_rule.py` [1], [4] | yes, identical | WS1 M1 |
| H2 | Ladder $292,264 fwd (exact dates); 9.90y duration; DV01 $289/bp | 25 Sep | `official_curve_pv.py`, `S1_hedge_weights.py` | $292,264 yes | WS1 M1 |
| H3 | Ladder $289,119 today / $292,418 fwd; 26bp; GPT $289,003 / $292,214 / 26.9bp | 28 Sep | `verification/ladder_2026-09-28/` | yes, identical | WS1 M1 (Gate A anchor) |
| H4 | WInS literal ladder cost $292,226, 10 trades, $175 commission, $7,599 cash | 28 Sep curve, 28 Sep WInS prices, live ETF prices | Sheet `Book L` | DFs reproduced exactly; prices not re-checked | WS1 M1, WS6 |
| H5 | "About 1 in 3" rate paths cost > $300k by Jan 2027 (MODEL 30-34%; history 32-36%) | 25 Sep, 19bp | `D3_model_v2_results.md` (30.2% / 34.4%), `S4_red_team.md` (30.7%), `D1` [6] (30.5%), `AX1b` [C] (31.8-36.1%) | D1 30.5% yes | WS4 |
| H6 | Same odds at 28 Sep: 24.2% (Nov-15), 18.7% (exact); history falls >= 26bp: 27.6-31.1% of 68-day windows | 28 Sep, 26bp | D1 rerun [6]; `AX1b` [C] | AX1b yes | WS4: model odds fell to about 1 in 4, history still 28-31%; restate the "1 in 3" line (section 3, F2) |
| H7 | Ladder > $300k on 173/185 (exact) and 176/185 (Nov-15) trading days of 2026; worst 27 Feb $327,631 | 2026 curves | `D1_purchase_rule.py` [5] | yes | WS3/WS4 |
| H8 | REC total p5/p50/p95 **$182k / $207k / $250k**; ALT $168k / $210k / $266k; bottom $150k; top median $175k; gift $165k / $174k / $188k; kept $16k / $32k / $66k; P(top reached) 73% | JPM ACWI 7.00%, 25 Sep, 200k paths, seed 20260927 | `E6_final_checks.py` [1]-[2] | yes, identical | WS2 M3/M4 |
| H9 | History worst **$169k** (rescaled, 1928 start) vs ALT $120k; raw worst $171k; p10 $185k; median $214k; top reached in 77% of windows | 93 windows 1928-2025 | `E6_final_checks.py` [5] | yes | WS3 M5 |
| H10 | Stock fund $40k = 8.7% of ~$464k on 2 Jan 2028; plan split 65.9 / 25.3 / 8.7 | 25 Sep exact-date | `E6_final_checks.py` [2], [7] | yes | WS1 (Portfolio split), WS6 |
| H11 | Vanguard-like 5.08%: REC $179k / $202k / $242k; P(top) 67% | hybrid assumption | `E6_final_checks.py` [4] | yes | WS2 |
| H12 | Bad 2031-32: gift median $169k, never below the announced bottom | bottom-decile returns | `E6_final_checks.py` [3] | yes | WS2/WS3 |
| H13 | Rates fall first: fund $20-23k (-50bp), $1-7k (-100bp), none and floor $127-137k (-150bp) | 25 Sep | `E6_final_checks.py` [8] | yes | WS4 |
| H14 | Joint tail, no 2028 deposit: $11,957 (-50bp) / $31,413 (-100bp) of the 2033 payment unfunded; on 28 Sep: $9,281 / $28,753 | 25 / 28 Sep | `D1_purchase_rule.py` [8], rerun | yes | WS4 |
| H15 | Floor variants: each $25k less floor, median +$2-3k, p5 -$9-10k | E4 engine | `F1_floor_variants.py` | yes | WS2 D6 memo |
| H16 | Growth-first misses a payment 3.2% / 13.7% / 40.8% (deposit $150k / $75k / $0) | 25 Sep | `strategy_mc.py` via `why_us.md` | not re-run | WS3 M6 |
| H17 | 2020 yields: ladder about **$459k** (2020 median; max $470,249 on 4 Aug 2020); 28 Sep 2026 is the cheapest since **2002** (last cheaper day 28 May 2002 spot / 10 Jun 2002 fwd); cost <= $300k on 11.1% of days since 2000 | 6,688 curves 2000-2026 | `rab/rescued/ladder_history_2000_2026.py` | yes (new) | WS3 M5 |
| H18 | A payment is left partly unfunded (gap > 2028 deposit) on 197 of 6,688 days, all in 2020-2021; worst $20,588 on 4 Aug 2020 (2027 dollars) | same; deposit on time | same script (new check) | yes (new) | WS3/WS4: supports the IPS line "only 2020-level yields ... could leave part of one unfunded" |
| H19 | Real value of $50k at 2.5% inflation: $42,063 (2033), $33,681 (2042) | ASSUMPTION | `strategy_changes.md` I4 | not re-run | WS3 M7 |

---

## 3. Flags (contradiction rule: nothing here changes the strategy)

| # | Finding | Evidence | Class |
|---|---|---|---|
| F1 | The IPS history claims ($460k at 2020 yields; "every Treasury curve since 2000") rested on an uncommitted /tmp script and data | original copied to `rab/rescued/r4_hist_original.py`; data verified and committed; H17-H18 reproduce it | **fix-before-6-Nov** (done here: evidence now in the repo; WS3 to confirm) |
| F2 | "About 1 in 3 paths cost > $300k" is a 25 Sep (19bp) figure; at 28 Sep (26bp) the same methods give 19-31% | H5, H6 | **note-in-Final-Report** (the IPS draft does not quote it; keep it out of notes; WS4 restates) |
| F3 | Volume rule: official docs say an order may be "no more than twice a security's current daily trading volume"; the WInS Portfolio FAQ (Sheet `WInS Notes`) says orders can take at most half of market volume and larger orders wait. "Current daily" volume at the open is small for thin funds (IBTR ~69k shares/day, $34m assets) | `research/insight_v1/phase_A/case_register.md` R-W66; `WInS Notes` row "Volume rule" | **fix-before-6-Nov** for WS6: check each order against half of the volume WInS shows at order time; avoid the first minutes for IBTO-IBTR |
| F4 | IPS floor wording vs model: the IPS says the late-2032 Treasuries "repay the whole remainder" (the 2028 deposit after completing the ladder); E6 keeps the floor at $150k face and shrinks the fund when rates fall first (E6 [8]: -50bp, top-up $10k, floor $150k). Same in the base case, different only if rates fall before Jan 2027 | IPS Report doc (read 30 Sep; currently headed "EXEMPLAR ONLY"); `E6_final_checks.py` [8] | **fix-before-6-Nov** (team picks one reading; WS2 models the IPS wording) |
| F5 | iBond ETFs "do not seek to return any predetermined amount" and hold notes maturing Feb-Nov of their year, then cash until about 15 Dec | `securities_and_allocation.md` s4 (iShares, read 28 Sep); S1 s1c | **note-in-Final-Report**; WS6 notes must never say an iBond "repays $50,000" |
| F6 | Five 2038-2042 rungs are coupon bonds maturing 1.5 to 10.5 months before their payment (e.g. Feb-2037 bond for 1 Jan 2038); coupons must be reinvested; WInS cash earns 0% | `Book L`; WInS Notes | **note-in-Final-Report** (Laura's real plan uses STRIPS; WInS is the stand-in) |
| F7 | `Portfolio` split 65.9/24.3/8.7 is from the 25 Sep exact-date ladder; ETF prices in both tabs are live and unstamped | cell formulas | **fix-before-6-Nov** (WS1 M1: recompute on `numbers.yaml`, stamp prices) |
| F8 | E6 seed 20260927 vs run seed 20260930 | `D6_behavioural_numbers.py` | **ignore** (report MC noise when comparing) |
| F9 | JPM 2026 LTCMA (data as of 30 Sep 2025) is the return anchor; a 2027 edition may now be published | `D2_equity_premium.py` inputs | **note-in-Final-Report** unless WS2/WS3 finds it (UNVERIFIED) |
| F10 | `Book L` / `Portfolio` construction (29 Sep) has no entry in `docs/AI_USE.md` | AI_USE diff in the main checkout | **note** for WS8's AI-use log |
| F11 | The "IPS Report" Google Doc currently holds the AI exemplar (headed "EXEMPLAR ONLY. NOT FOR SUBMISSION."); its strategy text matches the adopted design | doc read 30 Sep 00:25 AEST | **ignore** for modelling; WS7/WS8 treat its wording as AI text |

## 4. Reproduction log (2026-09-30, rab-ws env, repo root, all exit 0)

`verification/ladder_2026-09-28/reconcile.py` (identical), `scripts/E6_final_checks.py` (identical, 3 s),
`scripts/F1_floor_variants.py` (identical), `scripts/D1_purchase_rule.py` (identical), `scripts/D1_wins_rung.py`,
`scripts/AX1b_rates_audit.py`, `rab/rescued/ladder_history_2000_2026.py`. Outputs are not committed (re-run to see).
