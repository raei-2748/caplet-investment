# Vote pack v2 for set B (Tue 27 Oct 2026, 20:00 Sydney): evidence sheets for D1-D10 and the smaller choices

> **Later correction (20 Oct, `oct20/verify_engine3/verify_engine3.md`): BOTH has no top-reach advantage.** On a realistic booking BOTH reaches the top in 73.0% vs 75.4% for 3r-fix; quote "about the same (73-77%)". Its only gain is payments (0% vs ~0.6%), at a 2033 re-match cost of ~$8.5-10.5k median in 1-4 buys and ~-$2.5k total money (fair crediting). Option 2 is not the D10 on-call reading: on-call gives option 1 ~1.6% short (worst ~$7k).

> **CHECKED COPY (verify_vote2, wave J, Tue 20 Oct 2026 ~11:10-12:30 Sydney; `oct20/verify_vote2/verify_vote2.md`).** Every V3 figure in table A, the cross-check table, the conditions table and D10 was re-read from `results_v3.csv` by script and matches (one rounding slip fixed). engine_v3 reproduces reconcile3r's agreed numbers exactly with the fixes off (re-run: seed 7, 100,000 paths, path-level difference 0), and 12 fresh re-runs (10 seeds × 20,000 paths, 2 seeds × 100,000) put option 1 at 14.2-15.0% and 3r at 0.56-0.75%, inside sampling error. **Corrections applied in this copy (each marked [checked]):** (1) LCK is now verified (CONFIRMED, `oct20/verify_lockin/`); its marked-at-market study-engine 3r odds are 0.08% / 0.32% / 0.72% (MC / bootstrap / history), not 0.02%. (2) V3 has since run buy-only 1R and BOTH (unverified): BOTH's top-reach gain is about +2 points on V3, not +8, and BOTH is 1.88% short if the re-match counts the funds' bill interest. (3) The study minimum rule does NOT move option 1's V3 median to $145k (it stays $140k; 49.9% at $145k), so SC-minrule's premise and "the rule matters more than the fee" are wrong. (4) D10: V5:29's "for flexibility" is in the pending wording only; the accepted V5:30 "before the floor" points to a draw by 2033 (fits 10a). Smaller fixes: 3r $15k robustness, gift-below-minimum maximum, conventions behind 77.8/45.7/77.0, option 2 under the study chain, safe-list ranges, case:114, NT$ ratio, deadline citation. Everything else stands.

**Status.** AI-generated research by Claude Code for Team Caplet, written Tue 20 Oct 2026, about 11:35 Sydney (wave H). It replaces `oct20/votepack/votepack.md` (v1, wave F). It is **evidence only**. It contains no options-note text and no IPS, pitch, TNA, Final Report or trade-note wording. Students write their own half-page options notes (due Mon 26 Oct 18:00, `oct20/ops/operating_plan.md:47, 115`) and decide every vote. Each "AI view" line is labelled, and it is an opinion on substance, not wording. Every model figure is MODEL output from AI-written code; no student has rebuilt any of it. If the team uses anything here, log it in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy: "If you use AI to assist you in any way during the competition, how you use it must be recorded in your Works Cited pages", https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). No surnames, emails, usernames or birthdays appear here. The only name used is Ray's, as the team's only trader (team rule after 7 Oct).

**Short forms.** All paths sit under `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/`.
- **V3** = `oct20/engine_v3/engine_v3.md` (one corrected engine; canonical table §5; every row in `oct20/engine_v3/results_v3.csv`). **VREC** = `oct20/verify_reconcile/verify_reconcile.md` (independent rebuild of the agreed numbers). **REC** = `oct20/reconcile3r/reconcile_3r.md` (the agreed basis, §5). **R1R** = `oct20/rematch1R/rematch_1R.md` (1R and BOTH).
- **RT** = `oct20/redteam3r/redteam_3r.md`. **RA** = `oct20/rangeaudit/range_audit.md`. **LCK** = `oct20/lockin/lockin_2031.md`. **ALT** = `oct20/alternatives/alternatives.md`; **VRA** = `oct20/verify_rub_alt/verify_rub_alt.md`.
- **LDI** = `oct20/ldi/ldi_second_opinion.md`; **VLS** = `oct20/verify_ldi_sens/verify_ldi_sens.md`. **SEN** = `oct20/sensitivity/sensitivities.md`.
- **RS** = `oct20/reserve/reserve_schedule.md`; **VR** = `oct20/verify_reserve/verify_reserve.md` (note: VR is the reserve verifier, VREC the reconcile verifier).
- **TC** = `oct20/tradecheck/trade_check_pack.md`; **VTR** = `oct20/verify_trade/verify_trade.md`.
- **INF** = `oct20/inflation/inflation.md`; **VIN** = `oct20/verify_infl_num/verify_infl_num.md` (verifies INF and `oct20/numbers/numbers_refresh.md`).
- **CR** = `oct20/clientread/client_readers.md`; **VCC** = `oct20/verify_charts_cr/verify_charts_cr.md`; **VCO** = `oct20/verify_cosponsor/verify_cosponsor.md`; **CO** = `oct19/cosponsor/cosponsor_research.md`.
- **IFX** = `oct20/verify_ipsfix/ips_fix_list_checked.md`. **NREG** = `oct20/numreg/numbers_register.md`. **UPD** = `oct19/out/Caplet_Update_19Oct2026.md` (§7b defines D1-D9). **KIT** = `oct19/ipskit/ips_writing_kit.md`.
- **case:n** = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`; **IPS:n** = `.../2026_WGY_Investment_Policy-FINAL.txt`; **TNA:n** = `.../2026_WGY_Trading_Notes_Analysis-FINAL.txt`; **deliv:n** = `.../smapply_public_2026-10-14/deliverables.txt` (criteria at :55-59).
- **Notes:n** = filed WInS trade notes, `/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` (VT :14, IBTR :15, Feb-37 :16, May-38 :17, Nov-39 :18, IBTM :19, IBTO :20, Nov-40 :23, Nov-41 :24). Notes cannot be edited (assumed, not confirmed; treat as final, VTR E12).
- **V5** = the live IPS Doc tab "Version 5" (`oct19/drive/ips_report_live.md:22-30`), 97% AI exemplar text that must not be reworded by AI (UPD §2). Each V5 paragraph appears twice (two versions) on the same line.

---

## What changed since v1 (read this first)

| # | Change | Effect on the vote | Source |
|---|---|---|---|
| 1 | **The agreed payment numbers are independently confirmed.** A from-scratch engine lands within 0.4 points on every payment figure: option 1 14.8% / 14.7% short (agreed 14.5% / 14.4%), 3r 0.59% / 0.63% (agreed 0.63% / 0.65%), worst $3.1-3.3k, and all ten "conditions" rows | The 3r-vs-option-1 payment comparison in v1 stands | VREC §0 item 1, §2 |
| 2 | **A canonical table now exists (V3), and this pack uses it as the D1 reference.** V3 is the agreed engine with every listed fix and new options (2, 3a, 3b, 3r $15k, 4, 1R) behind switches. With the fixes off it reproduces the agreed numbers exactly (path-level difference 0 on 100,000 paths × 2 seeds × 12 cases) | Numbers below move slightly from v1; the ranking does not | V3 §0, §3 |
| 3 | **iBond-fee bug found twice, independently.** The agreed engine priced the funds on their net coupon, so the 0.07% fee was nearly free. Charged properly the ladder costs **$300.4k (VREC) / $300.7k (V3)** on 19 Oct, not $299.9k; a Jan-2028 top-up is needed in **51-52%** of paths; option 1's median minimum drops from $145k to **$140k** (a rounding knife-edge); gift and Laura's free money fall about $0.6-1k | "$145k" and "$299.9k" leave the safe list | VREC §4 N1; V3 §4 F2; VLS §3 (fee about $0.93k PV) |
| 4 | **Top-reach exact figures depend on two unstated conventions** (top rounded down to $1k; floor's 15 Dec-1 Jan interest). Without them 72 / 40 / 72.5%; with them 77.8 / 44.9 / 76.4% (77.8 / 45.7 / 77.0% if the fee is also left out = engY conventions, `top_probe.txt:3-4`) [checked]; V3 76.9 / 44.5 / 75.5% | Say "about three in four" / "under half", never the exact figure. New smaller choice: is the top rounded? | VREC §0 item 2, `oct20/verify_reconcile/data/top_probe.txt` |
| 5 | **NEW decision D10: is Laura's retained half on call after 2033?** V5 para 4 says "At each January review, an uncovered payment is funded from the equity Laura retains" (V5:28, both versions). Read literally, option 1 falls from about **14.8% to 1.4%** short (worst $7.1k), and 3r from 0.6% to 0.07% | Option 1's 14% is a figure for one reading only. The team must settle D10 before quoting 14% against 0.6% | VREC §0 item 3, §3 reading A |
| 6 | **Money back to Laura in 2042 from the reserve is about $10-15k, not $19k.** The reserve left after the last payment: median $10.1k (3r, top +$10k) / $14.7k (top +$5k). V3's total 2042 money is $20.3k / $24.7k, but $8.8k of that also exists with no reserve (option 1) | Two measures, both shown in D1. "$19k" leaves the safe list | VREC §4 N3; V3 §5b |
| 7 | **1R measured (R1R) and BOTH added to D1.** A real Jan-2033 re-match (linear programme, Treasury notes only) is 0% short in every run; buy-only form costs +$2.1k median / +$5.8k 1-in-20 over the frozen estimate, 1-2 trades. 1R alone breaks the announced minimum about 10 times as often as 3r on the study engine. BOTH (3r reserve + one buy-only re-match in 2033) is 0% short, reaches the top 80% vs 72%, costs Laura about $13k of 2042 money (all study engine; on V3, since run and unverified: 77.3% vs 75.5%, about $6k less 2042 money, 1.88% short if the re-match counts fund bill interest) [checked] | D1 gains two options; "1R UNVERIFIED" is replaced by measured, single-engine figures | R1R §0, §2 |
| 8 | **The "1R alone hurts the minimum" finding depends on the cover-chain order.** V3 (above-cap money used before the gift is cut) puts 1R's gift-below-minimum at 0.06% (option 1 0.05%, 3r 0.004%); V3 run with the study chain gives 1R **1.22%**, matching R1R's 1.16% | A D5 rule (chain order) changes a D1 comparison. Both shown | V3 §4 F5, `oct20/engine_v3/data/sens_19oct_seed20261019.txt:28-36`; R1R §2 |
| 9 | **Real curve twists hurt 3r more than parallel moves.** 3r short: history with twists **2.8%** (19 overlapping windows, Aug 1983-Sep 2000 starts, worst $1.6k); block bootstrap with twists **0.77-0.82%, worst $6.1-6.8k** (vs $3.3k parallel) | "Never more than about $3k" must say "under parallel moves" | V3 §0 item 4, §6 |
| 10 | **Rate-fall timing: three measures, one direction.** $10k covers about 1.3 / 1.9 points (VLS), 1.0-1.25 / 1.5-1.75 (V3), 1.5 / 2.1 (VREC crossover) for a fall during 2027 / after Jan 2028. **But** under the plan as written a permanent fall *before* 2033 never leaves a payment short (VREC, V3 deterministic); it lands on the gift and Laura's free money. Payment shortfalls come from falls *after* Jan 2033 | The timing figure is "how much of the gap the bond absorbs", not a payment-risk number | VREC §0 item 5, §6; V3 §5d; VLS §1e |
| 11 | **Coupon gap corrected:** a permanent 2-point fall leaves **$19,488** on holdings' dates (not $18,952; line-141 fix) or $21,287 on the number-sheet basis. Study-engine knock-ons: option 1 16.2%, option 2 1.4%, the 1980s 3r path passes by only $185 | "About $19.5-21.3k depending on method" | VIN §1 E1 |
| 12 | **INF verified** (data and tables confirmed) with corrections: the NT$-building-cost correlation **widens**, not offsets, the spread; real ladder yield about 2.7-2.9%, not 2.6%; stocks' real return in high-inflation 5-year windows 0.5-0.7%/yr | D2 and D8 inflation/FX evidence is now usable, with the corrections | VIN §0, §1 I1-I8 |
| 13 | **Release-margin dial measured** (3r, top +$10k): margin $0 / $5k / $10k → short 3.0% / 0.6% / 0.6%, top reach 70% / 40% / 16% | SC-release now has agreed-family numbers | VREC §3 G, `oct20/verify_reconcile/data/readings.txt:12-13` |
| 14 | **The 2031 minimum is not one number.** The $145k step is reached in only 48.5% of V3 paths (the minimum depends on the 2028 top-up); 61-72% on the number sheet (no fee, floor − $3,700 rule). The minimum *rule* matters more than the fee | D4 rounding and minimum rule; never quote $145k as today's figure | V3 §5c; NREG F1 |
| 15 | **Leftover worth for option 1 is 3.3-3.4 points on the agreed basis, not 7.9** (REC §0.2 measured it in the study frame); for 3r about 0 only once rules (a)+(b) are in place, about 1 point in the range-audit frame | SC-left evidence corrected | VREC §4 items 3, 9; §5 |
| 16 | **Label fix.** "3r as written" means "as the coupon study wrote it". V5 contains no reserve; the team has not written 3r. This pack now says "3r (study design, top +$10k)" | Avoids implying 3r is in V5 | VREC §3 judgement |
| 17 | **New conditions:** cover money held in rolled 1-year bills (not 0%): option 1 12.0%, 3r 0.52-0.55%; curve held unchanged to 1 Jan (no pre-January move): 3r 0.84-0.88%, top reach 34.5% | Added to the D1 conditions table | VREC §3 D, H; V3 §6 |
| 18 | **NREG D5 corrected:** 3r's "0.02%" is study-engine only; agreed basis 0.6%, worst about $3.3k; never "zero", "0.02%" or "under $2k" | Safe list | NREG D5 (row 118) |
| 19 | Unchanged from v1: VTR's 295-vs-231 IBTM sizing choice for 3r option B (D7); VLS corrections. **[checked] `oct20/verify_lockin/verify_lockin.md` reported at 23:33 UTC: CONFIRMED** (every headline within about 1 point; five wording fixes; marked-at-market study-engine 3r short 0.08% / 0.32% / 0.72%). `oct20/verify_rematch/` still has no write-up (partial 20k-path data at 23:40 UTC: BOTH reaches the top 79.5%, 1R below minimum 1.31%, consistent with R1R) | R1R stays single-engine; LCK is verified | `oct20/verify_lockin/verify_lockin.md` §0, §5 |

---

## 0. Status of inputs and the engines

### 0a. Status of every input (as of 19 Oct 23:34 UTC = Tue 20 Oct 10:34 Sydney)

| Input | Verified? | How to use it here |
|---|---|---|
| **V3** canonical table | Built on the agreed engine and validated against it exactly (V3 §3). Its one material fix (the fee) is confirmed independently by VREC (+$0.79k) and VLS (fee about $0.93k PV). No third-party rerun of V3's new options yet | **The D1 reference.** Quote with its conditions |
| REC §5 (agreed numbers) | **Verified by VREC** (payments within 0.4 points; top reach convention-dependent; fee bug inherited) | Use as the "fee off" cross-check; V3 supersedes its levels |
| VREC | Independent engine (no shared code); implements REC's *rules*, not its code, so it confirms the code, not the reading (VREC §1 caveat) | Readings A-H (§3) are the source for D10 and several conditions |
| R1R (1R, BOTH) | Self-checked: independent LP check on 300 paths, seed 7, 19 Oct curve (R1R §1). **No verifier verdict yet** (`oct20/verify_rematch/` running, no write-up at 23:34 UTC). Run on the study engine only, not on V3 | Relative comparisons within its own table only. Its 0% short agrees with V3's idealised 1R (0%). [checked] V3 has since run buy-only 1R and BOTH on its own basis (`engine_v3/data/bo_tables.txt`, no write-up, unverified); see D1 |
| RT | Not separately verified; REC corrects it (hybrid "0.41%", locked-yield share) | Study-engine variants only |
| RA | Not separately verified; VREC confirms its "alone 5.3%" leftover measure (bug 9 partly wrong in REC) | Robustness table and F1 vs F2 only |
| LCK | **[checked] Verified by `oct20/verify_lockin/verify_lockin.md`: CONFIRMED** (independent engine, two seeds; five wording fixes; with the reserve marked at market the 3r +$5k lock gain is +3.1 not +3.9 points) | Lock-in and narrower-top variants, study engine; use verify_lockin §5's marked-at-market 3r odds |
| ALT | Verified with corrections by VRA | Relative comparisons between rows only |
| LDI, SEN | Verified by VLS with corrections | Corrected values only |
| RS | Verified by VR with corrections | Corrected values only |
| TC | Verified by VTR: PASS WITH CORRECTIONS | VTR go/no-go card (VTR §5) |
| CR, CO | Verified by VCC / VCO with corrections | Corrected claims only |
| IFX | Verified, no high-severity errors | Checked copy |
| INF | **Verified by VIN**: data and tables confirmed; corrections I1-I8 | Use with the corrections |
| `oct20/numbers/numbers_refresh.md` | Verified by VIN, one correction (E1: $19,488) | Corrected value |
| NREG | Self re-run identical; D5 corrected; **its D1 row ($18,952) is superseded by VIN E1** | Canonical 19 Oct values and wording rules, with that one change |

### 0b. Engines: compare numbers only inside one engine

| Engine | Used by | What it assumes | Option 1 short / 3r short (19 Oct) |
|---|---|---|---|
| **V3 canonical** | V3 | Agreed basis (below) **plus** fund fee charged at NAV, above-cap money used as cover before the gift is cut, unused leftover released to Laura in 2033, 2031 minimum = 98% of projected floor net of uncovered shortfall, rounded down to $5k; top rounded down to $1k | **14.8% / 0.62%** |
| Agreed basis (REC, = V3 "legacy") | REC | Rule (a) each rung sized to its own maturity, waiting interest extra (it really arrives); rule (b) 2033 reserve keeps the projected **dollar** shortfall + $5k; real iBond holdings; 0% yield floor | 14.5% / 0.63% |
| VREC independent | VREC | REC's rules implemented from the text, different code and random numbers, fee at NAV, top **not** rounded | 14.8% / 0.59% |
| Study engine (coupon study; RT, LCK, R1R, CR, ALT, SEN) | many | Waiting cash at 0%, iBond funds as par bonds ending 15 Dec, 0.25% yield floor, study chain order | 15.6% (16.2% with the iBond coupon fix) / 0.02% |
| Range-audit rules | RA | Rungs sized counting bill interest; need in today's value | 6.1% / 32.1% (3r / option 1) |

"Reach the top" has two definitions: **exact** (gift = the top) and **within $1k**. They differ by about 5-7 points (V3: option 1 76.9% exact vs 83.3% within $1k). Always say which.

**Every option-1 figure in this pack assumes Laura's retained half is NOT on call after 2033** (D10 option 10a) unless marked.

### 0c. How set B depends on Wed 21 Oct (D0) and the TNA

The D0 mini-vote (UPD §7a) fixes four wordings the TNA reflections freeze on Sat 24 Oct 08:00 Sydney. Set B must not contradict them (TNA:28-31; case:161-162: "Evaluators will consider the three deliverables together").
- **D0-1** (what VT is for) constrains **D10**, **D2** and D1 option 2. The VT note says stocks "only set how far her gift rises above her promised minimum" (Notes:14).
- **D0-2** (floor anchor and rounding) constrains **D4**.
- **D0-3** (why 2042 first) constrains the smaller choice on the January 2027 rule.
- **D0-4** ("sized for" vs the IBTR top-up rule) constrains **D5 S1** and the sizing rule inside D1.
- The editor's list of TNA claims (due Sat 24 Oct, UPD §3b item 1) is the checklist for every set B option.

---

## D10 (new). Laura's retained half after 2033: on call for payments, or free?

**The question in one line.** After the 2033 set-aside, if a later payment comes up short, may the plan draw on the half of VT that Laura keeps, which means that half must stay inside the portfolio until 2042?

**Why it is new.** V5 para 4 says, in both versions: "At each January review, an uncovered payment is funded from the equity Laura retains" / "an uncovered payment is funded from her retained equity" (V5:28). V5 para 6 adds "met from her retained equity" / "covered by Laura's half before the floor" (V5:30). V5 para 5 says she "retains the other half for flexibility" (V5:29, **pending wording only**; the accepted wording of :29 has no flexibility line, `oct20/verify_ipsfix/ips_fix_list_checked.md:14, 65`) [checked]. REC's option 1 figure (14.4-14.5%) reads the plan as a one-time set-aside in 2033 (`/home/user/snap/main/COMPETITION.md:161-162`), so after 2033 the half is free. VREC found that REC §3 does not mention V5:28 and that it is "the largest reading effect I found" (VREC §0 item 3).

**Reading note [checked].** Neither version of V5:28 says the January review continues after 2033, and the accepted V5:30 ("covered by Laura's half before the floor") places the draw while the floor still exists, i.e. by the 2033 gift, which fits 10a; `COMPETITION.md:161-162` also describes a one-time 2033 order. So V5 supports 10b only on a literal reading of V5:28; it is ambiguous, not a choice already made.

**This is the same mechanism as D1 option 2 and D2 option 2a**, asked of the live text: V5 read literally already chooses it (VREC §3, reading A: "It is the study's option 2 mechanism").

### D10 options

| Code | Option | What it means in the model |
|---|---|---|
| **10a** | Not on call: the 2033 set-aside is the last call on her half; after 2033 the half is hers | REC / V3 option 1 and every 3x row |
| **10b** | On call to 2042, held in VT inside the portfolio (V5:28 read literally) | VREC reading A; V3 option 2 |
| 10c | On call, but moved into Treasuries in 2033 | **Not modelled** (UNVERIFIED) |
| 10d | On call only up to a stated amount or date | **Not modelled** (UNVERIFIED) |

### D10 comparison (MODEL, 19 Oct curve, 100,000 paths, two seeds; compare within each column block)

| | 10a, no reserve (option 1) | 10b, no reserve | 10a + 3r $10k | 10b + 3r $10k | Source |
|---|---|---|---|---|---|
| A payment short (VREC engine) | 14.8% / 14.7% | **1.47% / 1.38%**, worst $7.1k | 0.59% / 0.63% | **0.08% / 0.07%** | VREC §3; `oct20/verify_reconcile/data/readings.txt:2, 16` |
| A payment short (V3 engine; option 2 = study semantics) | 14.79% (14.66%), worst $10.1k | **0.82% (0.83%)**, worst $12.2k ($12.9k) | 0.62% (0.65%) | not run | V3 §5a |
| Laura's free money in 2033, 1-in-20 / median (V3) | $0 / $25.0k | **$0 / $0** (her half stays in VT) | $6.5k / $21.7k | not run | V3 §5b |
| Money back to Laura in 2042, median (V3, total) | $8.8k | $56.3k (her half, still in stocks) | $20.3k | not run | V3 §5b |
| Stocks and yields fall together | ρ +0.3: 14.8% | ρ +0.3: **1.28%** (V3); ρ +0.5: 1.9%, worst $12.6k (study engine, NREG D7) | 0.62% | — | V3 §6; NREG D7 |
| Real curve twists (V3) | bootstrap 17.4-17.6%; history 16.1% | bootstrap **1.0%, worst $23k**; history 0.15% | bootstrap 0.77-0.82%; history 2.8% | — | V3 §6 |
| Need in today's value / payment-date sizing (VREC) | — | 1.5% / 2.3-2.4% | — | 0.21-0.22% / 0.27-0.28% | VREC §3 |

**Two verified sources, two levels for 10b.** VREC's reading A (1.4-1.5%, worst about $7k) and V3's option 2 (0.8%, worst about $12-13k) are different implementations of "the half stays on call": V3 uses the study's option-2 semantics (the gift is cut only for need beyond leftover + reserve + the half's 2033 value, `oct20/engine_v3/engine_v3.md:127`); VREC draws the half for uncovered payments year by year. Both say the same thing: **on call cuts option 1's payment risk by roughly a factor of 10-18, but the back-up is stocks, so the bad cases are larger and tied to stock crashes** (worst $7-23k across tests vs $3.3k for 3r under parallel moves).

**What the answer does to the rest of the vote** (VREC §3 judgement):
- If **10b**: the case for any D1 reserve is mostly about flexibility (Laura's 2033 money goes from $0 to about $22k) and keeping VT to one job, not about payments (1.4% → 0.07%).
- If **10a**: V5:28 and V5:30 no longer describe the plan and must change (team's words), and option 1 carries about 1 path in 7 with small post-2033 gaps paid from money Laura has already taken out (REC §7).

### What each option changes

| Option | IPS (principle only) | Final Report | WInS | Filed notes / TNA |
|---|---|---|---|---|
| 10a | V5:28 / :30 must stop naming her retained equity as the post-2033 source, or name what replaces it (D1) | Option 1's gap rate, or the chosen D1 cover's | None | Consistent with the VT note's "only" (Notes:14) |
| 10b | Keep the idea, but V5:29's pending "retains the other half for flexibility" then overstates [checked]; must say the half stays invested in the portfolio to 2042 | Must show the joint stock-and-yield stress and the $0 free money in 2033 | None | **Strains** the VT note's "only" (Notes:14): VT gets a second job. Fix in words only, never a new note (VTR §5) |
| 10c / 10d | A hybrid rule | Needs a new model run | None | Depends on wording |

### Case and rubric lines
- **Serves (10b):** case:91-92 ("All ten payments must be funded by the investment portfolio with a high degree of certainty"), as long as the half stays inside the portfolio.
- **Strains (10b):** case:102-103 ("committing all remaining assets could limit her financial flexibility as the project develops"); case:145 ("Preserves appropriate financial flexibility"); deliv:55 consistency if the VT reflection says "only".
- **Strains (10a with option 1):** case:97-99 (define and test certainty) if 1-in-7 gaps are not stated.
- **Wording risk either way:** V5:25 "covered by her other assets" can read as outside money (case:91-92). VLS §1e calls it ambiguous wording, not a breach; VREC §3 says name an in-portfolio source.

### UNVERIFIED
- 10c and 10d are not modelled.
- Whether the team ever intended V5:28 to apply after 2033: the decision log lists "job list for Laura's kept half" among set-B items with "None decided on record" (`oct19/notes/decision_log.md:85`); ask the authors.
- Neither R1R nor LCK ran under 10b.

### Dependencies
- **D0-1 → D10** (if VT's job is "only above the minimum", 10b conflicts).
- **D10 → D1** (sets the do-nothing baseline: 14.8% under 10a, 0.8-1.5% under 10b).
- **D10 → D2** (10b = D2 option 2a), **D10 → D5** (whether her half is a post-2033 step), **D10 → D3** (what certainty rests on after 2033).

**AI view (labelled; the team decides).** Settle D10 first. 10b gives the best payment figure without a new holding, but it is the only reading that makes VT a payment back-up after 2033, which the filed VT note's "only" and V5's pending "for flexibility" wording contradict [checked]. Under 10a the team needs either a D1 cover or an honest statement of the 1-in-7 gaps.

---

## D1. Coupon-reinvestment risk: how is it covered?

**The question in one line.** Part of each payment comes from coupons that must be reinvested at unknown future yields; what money, held where, covers a shortfall, so that no payment relies on money Laura has already taken out?

**Why it matters.** "All ten payments must be funded by the investment portfolio with a high degree of certainty. Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this requirement" (case:91-92). About $49k (10%) of the $500k must come from interest earned on reinvested coupons and waiting cash (VLS §1a CONFIRMED). The ladder's rate sensitivity covers about 78% of the payments' (VLS §1a). A permanent 2-point fall leaves about **$19.5k (holdings' dates, VIN E1) to $21.3k (number sheet)** to cover.

### D1 options

| Code | Option | Source |
|---|---|---|
| **1** | State the risk only: leftover, then Laura's half (one-time, 2033), then the gift above the floor | UPD §7b; V3 §2 |
| **2** | Laura's half kept in VT inside the portfolio to 2042 as the back-up (= D10 option 10b) | UPD §7b; V3 option 2 |
| **3r** | $10k of the 2028 deposit, before the floor, in the 3.125% Treasury maturing 15 Nov 2041; release above need + $5k in 2033. Sub-choices: **top +$10k** (study design), **top +$5k** (red-team fix), **top +$0** | UPD §7b; RT §3b; LCK §8 |
| 3r $15k (new in V3) | As 3r (top +$10k), $15k | V3 §2 |
| **3a** | Same $10k bond, no 2033 release, not in the top; unused reserve returns to Laura in 2042 | RT §5; V3 §2 |
| **3b** | $10k reserve in IBTM, then T-bills after 2033 | UPD §7b; V3 §2 |
| **1R** (now measured) | No reserve; re-match the Treasuries once in Jan 2033 so each later payment is met by cash arriving within the year before it; minimum cut $10k. Forms: **buy-only** (1-2 trades), **trim** (9), **full** (11, about 60% of the book) | R1R §0, §4 |
| **BOTH** (new) | 3r $10k (top +$5k) from the 2028 deposit, and in Jan 2033 one buy-only re-match **replacing** 3r's "need + $5k" release rule, funded leftover → reserve → Laura's half → gift above floor; what is left of the reserve goes to the gift up to the top | R1R §0 item 3, §5 |
| **4** | Dedicated cash-flow-matched rebuild of the ladder | UPD §7b; V3 option 4 |
| 1M (rejected) | A 2033 margin of $5-10k taken from Laura's half | RT §9 |
| **+ net-minimum rule** | The 2031 minimum is cut by any projected shortfall the named covers cannot cover | UPD §7b; V3 §2 |
| **+ two sizing rules** (required for every reserve number) | (a) each holding sized to its own maturity, waiting interest extra; (b) 2033 reserve keeps the projected **dollar** shortfall + $5k | REC §0 item 4; VREC §7 |
| **+ chain order** (new, from D5) | Money above the cap is used as cover before the gift is cut (V3 default) | V3 §4 F5 |

### D1 table A: canonical (V3, 19 Oct curve, 100,000 paths, seed 20261019, seed 7 in brackets; MODEL; D10 = 10a except option 2)

Source: V3 §5a-5b, `oct20/engine_v3/results_v3.csv` rows `suite=mc` (I re-read both seeds from the CSV; every figure below matches).

| | 1 | 2 | 3a | 3b | 3r study (top +$10k) | **3r top +$5k** | 3r $15k | 4 | 1R (idealised) |
|---|---|---|---|---|---|---|---|---|---|
| A payment short (> $100) | **14.79% (14.66%)** | 0.82% (0.83%) | 0.61% (0.64%) | 3.94% (3.79%) | **0.62% (0.65%)** | **0.61% (0.64%)** | 0.03% (0.02%) | 0.13% (0.12%) | 0.00% |
| Worst shortfall | $10.1k ($9.4k) | $12.2k ($12.9k) | $3.3k | $7.2k | $3.3k ($3.1k) | $3.3k ($3.1k) | $2.5k ($0.9k) | $0.3k | $0 |
| Ladder cost (median) / P > $300k | $300.7k / 52% | same | same | same | same | same | same | $301.2k / 54% | same as 1 |
| 2031 minimum / top (medians) | $140k* / $165k | $140k / $165k | $135k / $153k | $135k / $153k | $135k / $163k | $135k / $158k | $130k / $163k | $140k / $165k | $140k / $165k |
| Gift median / 1-in-20 low | $164.0k / $134.0k | same | $153.0k / $127.0k | $153.0k / $126.0k | $161.0k / $131.6k | $158.0k / $130.0k | $161.0k / $129.8k | $164.0k / $138.9k | $164.0k / $135.0k |
| **Gift reaches the top: exact (within $1k; brackets in this row are NOT seed 7)** | 76.9% (83.3%) | 76.9% | 78.8% (86.0%) | 78.6% (85.7%) | **44.5% (51.3%)** | **75.5% (80.1%)** | 52.4% (58.4%) | 78.7% (85.6%) [checked] | 77.7% (84.1%) |
| Gift below the announced minimum | 0.05% | 0.05% | 0.004% | 0.01% | 0.004% | 0.004% | 0.003% | 0.000% | 0.06% |
| Laura's 2033 free money: 1-in-20 / median | $0 / $25.0k | $0 / $0 | $7.7k / $25.3k | $6.6k / $25.1k | $6.5k / $21.7k | $6.7k / $22.3k | $8.3k / $21.1k | $7.4k / $27.5k | $2.0k / $33.1k |
| Money back to Laura in 2042 (median, total) | $8.8k | $56.3k | $28.4k | $26.3k | $20.3k | $24.7k | $22.4k | $10.3k | $2.9k |
| WInS orders before 6 Nov | 0 | 0 | 0 or 2 | 0 | 0 or 2 | 0 or 2 | 0 or 2 (size not trade-checked) | about 10 | 0 now; about 9-11 real-plan trades in Jan 2033 |

\* The $140k median minimum is a knife-edge: the $145k step is reached in 48.5% of paths (V3 §5c). [checked] With the study's minimum rule (floor − $3,700) option 1's median stays **$140k** (49.9% of paths at $145k; `results_v3.csv` sens row; `oct20/verify_vote2/rerun/minrule.txt`); only options 4 and 1R tip to $145k. V3 §5c's "$145k again" is wrong for option 1.

**1R in V3 is idealised** (V3 §2, §8): it sells the whole remaining ladder in 2033 and buys Treasury zeros maturing 15 Nov before each payment, which Laura's real plan cannot buy (STRIPS excluded by the 6 Oct email, `/home/user/snap/main/COMPETITION.md:87-90`). R1R's real re-match uses coupon notes (table C). V3's 1R also does **not** cut the minimum by $10k.

**Same figures on the other engines (cross-check; option 1 / 3r study / 3r top +$5k):**

| | V3 canonical | Agreed (REC = V3 legacy, fee off) | VREC independent (top not rounded) |
|---|---|---|---|
| Payment short | 14.8% / 0.62% / 0.61% | 14.5% / 0.63% / 0.62% | 14.8% / 0.59% / 0.58% |
| Worst | $10.1k / $3.3k / $3.3k | $10.1k / $3.3k / $3.3k | $10.1k / $3.2k / $3.2k |
| Ladder / P > $300k | $300.7k / 52% | $299.9k / 50% | $300.4k / 51% |
| Median minimum (option 1) | $140k | $145k | $140k (47.7% at $145k) |
| Reach top, exact | 76.9 / 44.5 / 75.5% | 77.1 / 45.4 / 76.2% | 72.1 / 39.7 / 72.5% (77.8 / 45.7 / 77.0% with REC's conventions) |
| Laura's 2033 free money (median) | $25.0k / $21.7k / $22.3k | $25.9k / $22.4k / $23.0k | $24.6k / $21.8k / $22.3k |
| Back to Laura in 2042 | total $8.8k / $20.3k / $24.7k | — | **reserve only** $0 / $10.1k / $14.7k |

Sources: V3 §5, §7; REC §5; VREC §2, `oct20/verify_reconcile/data/extras.txt:1-3`.

**Two 2042 figures, both right, different measures.** V3's "2042 return" is everything left after the last payment (carried surplus, unused cover cash, the reserve at market). VREC's is the reserve alone. The reserve-only increment (VREC: $10.1k / $14.7k) and V3's increment over option 1 ($20.3k − $8.8k = $11.5k; $24.7k − $8.8k = $15.9k) agree within about $1.5k. Medians do not add exactly. The study's "about $19k" came from a formula that kept the reserve growing at its purchase yield (VREC N3; VLS §1e: about +$0.76k per $10k by 2038) and should not be quoted.

### When these numbers hold (each line changes one condition; option 1 / 3r study design; V3 unless marked)

| Condition changed | Option 1 | 3r | 3r top +$5k | Source |
|---|---|---|---|---|
| Canonical (V3) | 14.8% | 0.62%, worst $3.3k | 0.61% | V3 §6 |
| **Laura's half on call after 2033 (D10 = 10b)** | **1.4-1.5%** (VREC) | **0.07-0.08%** (VREC) | — | VREC §3 A |
| Rule (b) dropped: need in today's value, cover as matched zeros | 21.3% | 2.4%, worst $5.5k | 2.4% | V3 §6; VREC 2.3% / 21.2% |
| Rule (a) dropped: rungs sized counting T-bill interest | 27.2% | 3.1%, worst $7.0k | 2.6% | V3 §6; VREC 3.0% |
| Both rules dropped | 31.7% | 5.4% | — | VREC §3 B+C |
| Waiting cash really at 0% | 25.9% | 0.97% | 0.96% | V3 §6 |
| 2033 set-aside cash earns T-bills (not 0%) | 12.0% | 0.55% | 0.54% | V3 §6; VREC D 11.9-12.0% / 0.52-0.55% |
| Curve held unchanged to 1 Jan 2027 (no pre-January move) | 14.9% | 0.84-0.88%, top reach 34.5% | — | VREC §3 H |
| Unused 2027 leftover kept to 2042 | 11.6% | 0.61% | 0.61% | V3 §6 |
| Yield floor 0.25% | 13.9% | 0.28% | 0.27% | V3 §6 |
| No yield floor (bound, unrealistic) | 17.4% | 4.4%, worst $19k | 4.3% | V3 §6 |
| Rate volatility 0.75 point a year | 11.7% | 0.26% | 0.26% | V3 §6 |
| Stocks and yields fall together (ρ +0.3) | 14.8% | 0.62% | 0.61% | V3 §6 |
| Release margin $0 / $10k instead of $5k (3r study) | — | 3.0% (top 70%) / 0.6% (top 16%) | — | VREC §3 G |
| History, additive, 10-year (688 windows) | 18.8% | 0.87%, worst $1.0k (6 windows, Aug 1984-May 1985) | 0.87% | V3 §6 |
| History, proportional | 7.0% | 0 | 0 | V3 §6 |
| **History, real curve twists** | 16.1% | **2.8%, worst $1.6k** (19 windows, Aug 1983-Sep 2000) | 2.8% | V3 §6 |
| **Block bootstrap, real curve twists** (2 seeds) | 17.4-17.6% | **0.77-0.82%, worst $6.1-6.8k** | 0.71-0.76% | V3 §6 |
| Study engine as published / with the agreed rules / reserve marked at market [checked] | 15.6-16.2% / 10.4% / — | 0.02% / 0.010% / 0.08% (bootstrap 0.32%, history 0.72%) | 0.02% | VIN E1; REC §5; verify_lockin §5 |
| All range-audit rules | 32.1% | 6.1% | — | REC §5; VREC 31.7% / 5.9-6.0% |

**The honest 3r range: about 0.6% of paths short under parallel moves (worst about $3.3k), 0.8% with real curve twists in the bootstrap (worst about $6-7k), 2.8% of heavily overlapping history windows with twists; 2-6% if either sizing rule is dropped.** History has about 4 independent 16-year periods (RT §1c). 3r $15k stays at or below about 0.45% in every test that keeps both sizing rules, except "no yield floor" (2.6%); it is 0.56% / 0.86% if rule (b) / rule (a) is dropped (V3 §6; V3 §0 item 4's "0.4% everywhere" is wrong) [checked].

### D1 table B: study-engine variants (compare within this table only; 19 Oct unless stated)

| Variant | Short | Minimum | Gift median | Reaches top | Laura 2042 (median) | Source |
|---|---|---|---|---|---|---|
| Option 1 | 15.6% (16.2% with the iBond fix) | $145k | $166.2k | 68.4% exact | $8.0k | LCK §2; VIN E1 |
| 3r, top +$10k | 0.02% | $135k | $163.3k | 42% exact | $19.9k | SEN §1 |
| 3r, top +$5k | 0.02% | $135k | $160.2k | 73.0% exact | $24.0k | LCK §2 |
| 3r, top +$0, release kept | 0.02% | $135k | $155.7k | 92.3% exact (bootstrap 91.7%, history 93.6%) | $27.6k | LCK §8 |
| 3a, no release, top +$0 | 0.02% | $135k | $155.0k | 78.6% within $1k | $28.9k | VCC R14 |
| 3r $5k, top +$0 (16 Oct) | 1.81% (worst $2.9k) | $140k in 53% | $160.0k | 76% | — | RT §9 |
| 3r release with no margin (16 Oct) | 1.33% | $135k | $164.1k | 78% | $14.6k | RT §5 |
| 3r release a fixed half (16 Oct) | 0.79% | $135k | $160.3k | 75% | $22.4k | RT §5 |
| 3b $10k in IBTM | 4.6% | $135k | $155.0k | — | — | RS §6c |
| Option 2 | 1.4% after the iBond fix (1.3% before); worst $11.8k | $145k | $166.2k | — | about $51k | VIN E1; NREG D7 |
| Option 4 | 0% | $145k (knife-edge) | $165.5k | 78.5% within $1k | — | NREG D7; CR:80 |

[checked] The 0.02% in the 3r and 3a rows uses the study's reserve shortcut. With the reserve marked at market the study engine gives **0.08% (MC) / 0.32% (bootstrap) / 0.72% (history, 5 of 690 windows)** (`oct20/verify_lockin/verify_lockin.md` §5: "Quote the marked-at-market figures in the vote pack, not 0.02%"). Table C's 3r rows (R1R) use the same shortcut.

### D1 table C: 1R and BOTH, measured (R1R; study engine, 16 Oct curve, seed 20261019; 100,000 paths, BOTH on the first 30,000; MODEL)

| Option | Short | 2033 re-match cost: median / 1-in-20 high | Minimum | Gift median | Reaches top (exact) | Gift below minimum / below net minimum | Laura 2033 / 2042 / total (medians) | Trades in 2033 |
|---|---|---|---|---|---|---|---|---|
| 1 state only | 16.45% | — | $145k | $165.3k | 68.1% | 2.15% / 0.59% | $19.9k / $7.0k / $30.2k | 0 |
| 3r $10k, top +$5k | 0.02% (worst $666) | — | $135k | $159.2k | 71.7% | **0.11%** / 0.01% | $20.1k / **$22.8k** / $44.2k | about 1 |
| **1R buy-only** | **0%** | $5.5k / $21.7k (**+$2.1k / +$5.8k** over the frozen estimate) | $135k | $165.2k | 67.1% | **1.16%** / 0.08% | $18.6k / $1.7k / $23.2k | **1 (2 at 1-in-20; max 4)** |
| 1R trim | 0% | $2.2k / $22.1k (+$0.4k / +$2.6k) | $135k | $165.2k | 67.6% | 1.21% / 0.11% | $19.5k / $6.3k / $29.0k | 9 |
| 1R full (do not use) | 0% | $0.2k / $21.9k | $135k | $165.2k | 68.0% | 1.13% / 0.12% | $19.9k / $8.3k / $31.1k | 11 (60% of book) |
| 3r on BOTH's 30,000 paths | 0.03% | — | $135k | $159.1k | 71.8% | 0.15% / 0.02% | $19.9k / $22.5k / $43.9k | about 1 |
| **BOTH: 3r $10k (top +$5k) + buy-only** | **0%** | (as 1R buy-only, funded from leftover then reserve) | $135k | $159.3k | **80.2%** | **0.16%** / 0.03% | $19.8k / **$9.7k** / $31.5k | 1-2 |
| BOTH + trim | 0% | — | $135k | $159.5k | 83.9% | 0.20% / 0.03% | $19.9k / $15.8k / $37.1k | 9 |
| BOTH, $5k reserve (top +$0), buy-only | 0% | — | **$140k** | $160.2k | 84.8% | **1.03%** / 0.25% | $19.8k / $5.5k / $28.1k | 1-2 |

Sources: R1R §2, `oct20/rematch1R/data/r1_extra_16oct_stdout.txt`.

**Robustness of 1R and BOTH (R1R §3):** payments 0% short in every run (both seeds, 19 Oct curve, ρ +0.5, bootstrap with twists, 690 history windows, bid-ask 0.50%, roll-down curve). BOTH buy-only reaches the top 79.9% at ρ +0.5, 80.1% on the bootstrap, 75.1% on history, against 3r's 72.8% / 71.8% / 70.9% (`r1_extra_16oct_stdout.txt`). On the 19 Oct curve, 1R buy-only is 0% short, gift below minimum 1.03% vs 3r 0.10%, premium +$2.1k / +$5.8k (`oct20/rematch1R/data/r1_19oct_stdout.txt`).

**What the re-match costs depends on where yields are in 2033** (buy-only, R1R §2): +$4.2k over frozen at unchanged yields (cost $5.7k), +$1.1k after a 3-point fall (cost $20.4k), a −$0.6k surplus after a 3-point rise. "It costs most when nothing happens" (R1R §6).

**Where two sources disagree: does 1R alone weaken the 2031 minimum?**

| Source | Engine and chain | 1R form | 1R gift below minimum | 3r | Option 1 |
|---|---|---|---|---|---|
| R1R | Study engine; study chain (above-cap money not used first); minimum cut $10k | Buy-only LP, coupon notes | **1.16%** (19 Oct: 1.03%) | 0.11% | 2.15% |
| V3 canonical | Agreed engine; above-cap money used before the gift is cut; minimum **not** cut | Idealised full re-match into zeros, surplus paid out in 2033 | **0.06%** | 0.004% | 0.05% |
| V3, study chain | Agreed engine; study chain | Idealised | **1.22%** | 0.015% (top fix 0.048%) | 1.50% |

Reading: the 1.2% level comes mainly from the chain order (D5 sub-choice), not from the re-match itself; with above-cap money used first, 1R alone is about as safe for the minimum as option 1. In both engines 3r remains the safest for the minimum, by a small absolute margin. [checked] **Since run on V3 (after this pack; unverified, no write-up):** buy-only 1R on the V3 basis (minimum not cut) puts the gift below the minimum in 0.007% (seed 7 0.008%) against 0.004% for 3r top +$5k and 0.052% for option 1 (`engine_v3/data/bo_tables.txt`), which supports the chain-order reading above.

**V3 re-run since this pack was written (19 Oct 23:37-23:46 UTC, `oct20/engine_v3/data/bo_tables.txt`, `bo_19oct_seed*.txt`; no write-up, not verified):** on the V3 basis BOTH is 0% short (seed 7 0%), reaches the top **77.3% (77.4%) vs 75.5% (75.9%)** for 3r top +$5k (not 80% vs 72%), gift below the minimum 0.000%, Laura's 2033 money median $27.0k vs $22.3k and 2042 money $18.5k vs $24.7k (about $6k less in 2042, about $5k more in 2033); re-match cost median $8.5k / 1-in-20 $26.0k, 1 trade (3 at 1-in-20, max 4). **Caveat:** if the 2033 re-match counts the iBond funds' own bill interest to 15 Dec, 1R and BOTH are **1.88% short (worst $2.8k)**, so BOTH's 0% depends on a sizing convention, like rule (a).

**BOTH on the agreed basis (as written before that run).** R1R did not run inside V3. It expects BOTH to stay at 0% short there (after the re-match nothing is reinvested) and the case for a 2033 re-match to be stronger there, because 3r alone is about 0.6% short on that basis (R1R §2 reconciliation). This is reasoning, not a run: **UNVERIFIED**.

### Other tested facts
- **Timing of a rate fall (three measures, one direction):**

| Measure | Fall during 2027 | Fall after the Jan 2028 purchase | Basis |
|---|---|---|---|
| VLS: permanent fall $10k alone covers | about 1.3 points ($9.1k uncovered at −2) | about 1.9 points ($1.35k uncovered at −2) | Own-rung sizing, waiting in T-bills |
| V3 deterministic: uncovered after leftover and reserve | 1.0-1.25 points ($8.3k at −2) | 1.5-1.75 points ($1.8k at −2) | V3 basis |
| VREC crossover (raw gap vs reserve's Jan-2033 value) | about 1.5 points | about 2.1 points | Real bill interest, maturity sizing |

  **What this is not:** a payment-risk number. Under the plan as written, a permanent fall **before 2033** never leaves a payment short (VREC tested −1, −2, −3 points in 2027, 2028 and 2033; V3: "In every deterministic path the *payments* are still met"). The 2033 projection sees the fall and the cover chain pays for it, so the timing decides **who pays** (VREC §6):

| Permanent fall (VREC deterministic, VT on its median path) | 3r: gift / Laura's free money / short | Option 1: gift / Laura / short |
|---|---|---|
| −2 points during 2027 | $152.1k / $4.3k / 0 | $152.7k / $3.4k / 0 |
| −2 points after Jan 2028 | $158.0k / $18.6k / 0 | $166.5k / $7.9k / 0 |
| −2 points after Jan 2033 | $167.4k / $20.4k / 0 | $168.7k / $24.6k / **$2.7k** |
| −3 points after Jan 2033 | $167.4k / $20.4k / 0 | $168.7k / $24.6k / **$6.3k** |

  Payment shortfalls come from falls **after** Jan 2033; about two-thirds of short paths sit in the worst 10% of post-2033 moves (VREC §6). V3's Monte Carlo conditioned on timing gives 3r short 3.35% when yields fall ≥1 point in the first year and stay within ±0.5 to 2033, against 0.71% for a calm first year then a ≥1-point fall 2028-33 (V3 §5d; `oct20/engine_v3/scripts/run_v3.py:33-46`). VREC conditioned on total fall size instead finds a smaller gap (3.2-3.6% vs 2.7-2.9% for falls above 2.5 points). Different conditioning; both show the 2027 window is the weaker one; no rule fixes it, because the reserve does not exist yet (V3 §0 item 5).
- **Mean reversion makes 3r look better** (study engine: 0.01% at an 8-year half-life) (RT §1a).
- **Why the bond works:** at the 2031 range and the 2033 set-aside mostly the price gain (+$1.7-2.1k per $10k at −2); by 2038-41 mostly the locked yield (VLS §1e). Hedge ratio 78% → about 81% (VLS §1e).
- **If the 2028 deposit never arrived:** about 55-56% of paths leave a payment short (typical $14k), with or without 3r (VLS §2: 56.3%).
- **Option 4 is fragile when sizing and reality disagree:** 23-28% small gaps if rungs are sized counting T-bill interest or waiting cash really earns 0% (worst $2.4-8.2k) (V3 §6 reading notes).

### What each option changes

| Option | IPS (principle only) | Final Report | WInS book | Filed notes / TNA |
|---|---|---|---|---|
| 1 | Must name the post-2033 cover (D10) | Admit about 1 path in 7 has small gaps (under 10a) | None (TC T0) | None |
| 2 | VT gets a second job | Joint stock-and-yield stress | None | **Conflicts** with the VT note's "only" (Notes:14); words only |
| 3r (any top rule) | One principle: a small Treasury reserve from the 2028 deposit, outside the minimum (full 3r needs 50-70 words of about 470, RT §6) | $10k, the bond, both sizing rules, the release rule, the top rule, the tests with conditions | Option A no trade ("about mirrors"); option B two trades (D7) | None contradicted (RT §7; LCK §7) |
| 3r $15k | As 3r | Minimum $130k | Larger option B (size not trade-checked: UNVERIFIED) | None |
| 3a | Same principle, plus "unused reserve returns to Laura in 2042" | Simplest rule set | As 3r | None |
| 1R | A 2033 re-match rule; buy-only keeps "held to maturity" (R1R §4) | Re-match cost distribution, trades, and that its cost falls on Laura's half then the gift | None now; 1-2 real-plan trades in 2033 (buy-only) | None filed |
| **BOTH** | 3r's principle **plus one 2033 rule** covering four points: what happens, where the money comes from, "held to maturity" still holds, and that after 2033 certainty rests only on the US government paying (R1R §5) | LP method, cost distribution, comparison table on one basis, four stated assumptions, why not the full re-match | As 3r; nothing new (R1R §4) | None |
| 3b | Reserve inside the floor fund | Weaker numbers (3.9%) | None | None |
| 4 | Dedication rule | Best numbers on most tests | About 10 orders, $175, 21 of 200 trades | **Conflicts** with 3-4 filed notes (TC T3) |

### Case and rubric lines
- **Serves:** case:91-92; case:96 ("explain how its composition should change, if at all", which a 2033 re-match answers directly, R1R §0 item 4); case:97-99; case:119-120 ("must also protect the portfolio's ability to fund" the payments); deliv:57.
- **Strains:** IPS:51-52 ("rather than ... presenting detailed financial calculations") if mechanics go into the IPS; CLAUDE.md lesson "complexity must earn its place"; case:114 ("could damage her credibility") [checked] if 1R alone leaves the minimum less safe, or if 3r (top +$10k) is quoted as "three in four".

### Open UNVERIFIED items
- BOTH and the buy-only 1R LP have not been run on V3 (agreed engine); R1R's verifier has not reported yet.
- Whether 15-Nov Treasury notes for every year 2033-41 will be outstanding in 2033 (routine 10-year issuance; R1R §8). Retail bid-ask in 2033 (R1R §8).
- When WInS credits coupons and iBond payouts; the live WInS Nov-41 price; the 2x-volume rule for bonds (VTR §4).
- Model family: parallel shifts in the MC; twists only in the bootstrap and history; iBond funds as single bonds; no taxes.

### Dependencies
- **D10 → D1:** sets option 1's baseline (14.8% vs 0.8-1.5%).
- **D1 → D4 (top rule):** 3r forces top +$10k / +$5k / +$0 / 3a; BOTH changes the top-reach odds (80% vs 72%, study engine; 77.3% vs 75.5% on V3, unverified) [checked].
- **D1 → D3:** BOTH changes the certainty definition after 2033; a named stress must match the chosen option.
- **D1 → D5:** 3r inserts the reserve after the leftover; BOTH replaces the 2033 release rule with a re-match funding order; the chain-order rule changes 1R's minimum safety.
- **D1 → D2:** with 3r, 3a, 4 or BOTH, Laura's half need not be the back-up (D2 option 2b).
- **D1 → D7:** 3r option B (and 3a, BOTH) needs two WInS trades and two new notes.
- **D1 → SC-sizing:** rule (a) means "$293k" and "her first $300,000 is enough" stop being honest figures; on maturity sizing with the fee the ladder is about $300.4-300.7k, top-up about a coin flip (51-52%).

**AI view (labelled; the team decides).** Every reserve option (3a, 3r with any top rule, BOTH) keeps payments short in under 1 path in 100 under parallel moves, so the choice among them is mostly about the top's odds and Laura's 2042 money, not payments. BOTH is 0% short in every run on both engines except one V3 sensitivity (1.88% if the re-match counts the funds' bill interest); its top-reach gain is large on the study engine (80% vs 72%) but small on V3 (77% vs 75.5%), and its cost to Laura is about $13k of 2042 money on the study engine, about $6k on V3 (where she gets about $5k more in 2033). The V3 runs are unverified [checked]. Whichever wins, it needs the two sizing rules, the net-minimum rule, the chain-order rule and a top rule in the same vote.

---

## D2. Laura's kept half: its jobs, in priority order, and where it is held to 2042

**The question in one line.** What is the half of VT that Laura keeps for (payment back-up, cost overruns and co-sponsor gaps, other ventures, inflation defence), in what order, and where does it sit from 2033 to 2042?

### Options (UPD §7b; KIT D2)
- **2a.** Payment back-up first, then overruns and ventures (= D10 option 10b; VT then has two jobs).
- **2b.** Overruns and ventures only; the payment back-up is the D1 reserve (needs 3r, 3a, BOTH or 4; = D10 option 10a).
- **2c.** A principle only, no job list (case:106-107: "Teams are not expected to determine the size or investment composition of a separate contingency fund").
- **Plus:** where it is held 2033-42 (VT, Treasuries, or Laura's choice). If it is a payment back-up, it must stay inside the portfolio (case:91-92).
- **Sub-choice SC-keep:** one definition of "Laura keeps". V3 counts her half less set-asides **plus** money above the cap, unused leftover and any 1R surplus (V3 §2 "Laura's money"; F5). The study's L33 leaves out above-cap money, understating option 1 by about $3-5k (LCK §0).

### Comparison

**V3 canonical (19 Oct; Laura's 2033 free money, 1-in-20 / median):** option 1 $0 / $25.0k; option 2 $0 / $0; 3a $7.7k / $25.3k; 3b $6.6k / $25.1k; 3r study $6.5k / $21.7k; 3r top +$5k $6.7k / $22.3k; option 4 $7.4k / $27.5k; 1R $2.0k / $33.1k (V3 §5b).

**Study engine (19 Oct; CR:82-83 verified by VCC R12):**

| | Option 1 (half is the back-up) | 3r $10k (half freed) | Option 4 |
|---|---|---|---|
| Kept money 2033: p5 / p10 / median | $0 / $4.8k / $20.5k | $8.4k / $10.8k / $20.5k | $8.5k / $11.0k / $21.6k |
| Kept money under $10k | 17.2% | 8.0% | 7.8% |

**1R and BOTH (R1R §0 item 2; study engine):** in the worst 1 path in 20, Laura keeps $1.3k under 1R buy-only against $13.0k under 3r. BOTH keeps 3r's 2033 money ($19.8k median) but cuts her 2042 money from $22.5k to $9.7k.

Other evidence:
- **Inflation defence is weak for stocks over five years (now verified):** in the highest-inflation fifth of 5-year windows since 1950, US stocks' median real return was about 0.5-0.7% a year and about 47-49% of those windows lost real value (INF §0 item 7; VIN I7: 0.5% / 48.6% on Shiller's own file to Jun 2023, 0.7% / 46.7% on the repo copy).
- **"Risk only the surplus":** VT should not be the payment backstop (LDI §12 item 5; VLS confirms the arithmetic).
- **Leftover plus half fails to cover the coupon gap** in about 1 path in 13 (6.5-8.0%; median uncovered about $3.2k) under option 1 on the number sheet (NREG F9).

### What each option changes

| Option | IPS | Final Report | WInS | Filed notes / TNA |
|---|---|---|---|---|
| 2a | VT gets two jobs | Bad-case kept figure ($0 at p5 under option 1 or 2) | None | **Strains** the VT note's "only" (Notes:14); must match D0-1 and D10 |
| 2b | VT has one job; kept half = flexibility | Kept money p5 and median under the chosen D1, on one definition | None | Consistent with Notes:14 |
| 2c | One principle line | Judges' question "what happens to the retained half after 2033?" still needs an answer (KIT D2) | None | Neutral |

### Case and rubric lines
- **Serves:** case:102-103; case:145; deliv:56; IPS:49-50 ("preserving appropriate financial flexibility").
- **Strains:** case:91-92 if the half sits outside the portfolio while serving as a back-up; deliv:55 if the VT reflection and the IPS give VT different jobs.

### UNVERIFIED
- Where the kept half is invested after 2033 (no team decision recorded; KIT D2).

### Dependencies
D0-1 → D10 → D2 (D10 = 10b forces 2a; 10a allows 2b or 2c). D1 → D2 (2b needs a reserve option). D2 → D5. D2 → D6.

**AI view (labelled).** D2 is largely answered by D10: 2b is the cleanest match to the filed VT note and "risk only the surplus", but only with a reserve option in D1.

---

## D3. One certainty standard

**The question in one line.** What does "a high degree of certainty" mean for the ten payments, how was it tested, and on what assumptions (case:97-99)?

### Options (KIT D3; RS §6b; LDI §11)

| Code | Standard | Evidence (verified sources) | Weak point |
|---|---|---|---|
| **3a / C1** | Cash-flow matched: every payment has a US Treasury or Treasury fund maturing before it; each remaining risk named with what absorbs it | Remaining risks: reinvestment (D1), iBond payout not fixed and final-year cash (7 of 10 rungs wait 6-10.5 months, VLS §1d), the 2027 pre-purchase window, a late or small 2028 deposit, US default or delay | Gives no level |
| **3b / C3** | A probability standard | V3: 3r about 0.6% short (worst $3.3k) under parallel moves, 0.8% with twists (worst $6-7k); option 1 14.8% (10a) or 0.8-1.5% (10b); BOTH 0% (study engine) | IFX G1: no measured percentage in the IPS; target in the IPS, result in the FR |
| **3c** | A named stress: "met even if yields fall N points and stay down" | **Under the plan as written, 3r pays every payment for permanent falls of 1, 2 or 3 points starting during 2027, after Jan 2028 or after Jan 2033** (VREC §6; `oct20/verify_reconcile/data/timing2.txt`); option 1 is short $0.7k / $2.7k / $6.3k for falls of 1 / 2 / 3 points after Jan 2033 and never for earlier falls. V3: payments met in every deterministic path (V3 §5d) | The stress must name *after 2033* to be a real test; "$10k covers N points" is a gap figure, not this test |
| **C2** | Funded-ratio test | With 3r: at least 101.0% at 3% on every date from Jan 2028; without 3r it fails the 3% test on every date before 2033 (RS §6b, VR §1c). Rungs alone in 2033: 99.7% / 100.9% / 102.1% at 3 / 5 / 7% (VR §3) | Needs cover from 2028 to pass |
| **C4** (new, BOTH only) | Two-stage: before 2033 certainty rests on the reserve; after the 2033 top-up, only on the US government paying | R1R §5 item 4; payments 0% in every R1R test | Needs the D1 = BOTH vote; replaces V5's "covered at purchase" (V5:25) |
| LDI pack (FR only) | Funded ratio on two bases (108.5-110.4%, surplus $35-42k), hedge ratio 78%, reliance on reinvested income ($49k), surplus at risk | VLS §1a | FR material |

Rules for any option (KIT D3; IFX §3c): no "guaranteed", "risk-free" or "cannot miss"; never print the range confidence without the payment confidence beside it; one "99%" with one meaning.

### What each option changes

| Option | IPS | Final Report | WInS | Notes |
|---|---|---|---|---|
| 3a / C1 | The standard in words plus the risk list | Stress table and model with conditions | None | IPS line "covered at purchase" overstates (coupons must be reinvested, Notes:18; IFX O3) |
| 3b | A target only | Measured figure with both sizing rules and D10's answer beside it | None | — |
| 3c | One stress level, dated after 2033 | Re-run on the chosen D1 | None | — |
| C2 | One test sentence | Funded-ratio table by year | None | — |
| C4 | Two-stage definition | Re-match method and costs | None | — |

### Case and rubric lines
- **Serves:** case:97-99; case:136; deliv:57.
- **Strains:** IPS:68-70 if a measured percentage is put in.

### UNVERIFIED
- BOTH on the agreed engine; how judges read a model claim (no Wharton guidance found).

### Dependencies
D10 → D3 (what certainty rests on after 2033). D1 → D3. D3 → D5. D3 → D8.

**AI view (labelled).** The new deterministic result makes 3c stronger than v1 said, but only if the stress is placed after 2033, which is where shortfalls actually come from. 3a/C1 in the IPS with a measured result in the Final Report still fits the brief best.

---

## D4. One floor definition and one name, plus the top rule

**The question in one line.** Is the floor "what is left of the 2028 deposit after the ladder is complete, held in IBTM" or a fixed $150k face target; how is the quoted bottom built and rounded; and how is the 2031 top built?

### Options
- **4a.** Floor = what is left of the 2028 deposit after the ladder is complete (and after any D1 reserve), held in IBTM.
- **4b.** Floor = a fixed $150k face target.
- **Minimum rule (new sub-choice, SC-minrule):** (i) floor money − $3,700, rounded down to $5k (study, number sheet); (ii) 98% of projected floor, net of uncovered shortfall, rounded down to $5k (range audit, V3). V3: "The rule choice matters here more than the fee does" (V3 §5c). [checked] V3's own CSV contradicts this: option 1's median minimum is $145k with the fee off (50.9% of paths at $145k or above) but stays $140k under the study rule (49.9%); V3 canonical 48.5%.
- **Top rule (forced by D1):** floor + half of VT on the valuation date (option 1), plus the 3r reserve at +$10k / +$5k / +$0, or 3a; or a narrower top (¾ or ½ of VT's half, LCK §2); or BOTH; or a 2031 lock (D8).
- **Top rounding (new sub-choice, SC-round):** round the top down to $1k, or not. Worth about 3.5-3.8 points of top reach (VREC §2).

### Comparison: floor rule (RA §2, own engine, 19 Oct)

| | 4a "what is left" (F1) | 4b fixed $150k (F2) |
|---|---|---|
| Gift below the announced bottom | 0.08% | **0.84%** |
| VT bought in Jan 2028, 1-in-20 low | $19.5k | **$5.2k** |
| Option 2 short | 2.2% | 3.7% |

### The 2031 minimum is not one number (where sources disagree)

| Source | Rule and conditions | Share of paths at the headline step | Median | 1-in-20 low |
|---|---|---|---|---|
| V3 (option 1, 2, 4, 1R; $145k step) | 98% rule, fee charged, maturity sizing (top-up in 52% of paths) | 48.5% | **$140k** | $120k |
| V3 (3a, 3b, 3r $10k; $135k step) | same | 51.3% | — | $110k |
| VREC (option 1) | 98% rule, fee at NAV | 47.7% (49.8% fee-free) | $140k | — |
| NREG F1 (number sheet) | (R − $3,700) rounded down, no fee, payment-date-related bases | 61% (D) to 72% (A) | $145k | — |
| V3 sensitivity [checked] | study rule (floor − $3,700) | 49.9% (option 1) | $140k (option 1) / $135k (3r); $145k only for options 4 and 1R | — |

The floor shrinks whenever the ladder needs a 2028 top-up (52% of V3 paths, median $9.6k when needed). [checked] In the V3 canonical Monte Carlo the gift is below the announced minimum in 0.06% of paths or fewer (0% in all V3 history replays), but up to 0.19% on the twisted bootstrap (option 1; 1R 0.16%) and 1.2-1.5% under the study chain (`results_v3.csv`); V3 §5c's "in every model" overstates.

Other floor facts: a half-point fall before January cuts the floor to about $137-138k and the bottom to $130k (NREG E2); the $3,700 margin leaves about $0.2k spare on the worst case once the 0.07% fee (about $0.5k) is counted (VLS §1f); the floor pays $149.2k down to $146.8k if reinvestment falls 1-4 points for good (NREG E3).

### Comparison: top rule (compare within each engine only)

| Top rule | V3 canonical (exact / within $1k) | VREC (exact, top not rounded) | Study engine (LCK, R1R) |
|---|---|---|---|
| Option 1: floor + half of VT | 76.9% / 83.3%; top $165k | 72.1% | 68.4% exact |
| 3r, top +$10k (study design) | **44.5% / 51.3%**; top $163k | 39.7% | 42% |
| 3r, top +$5k | **75.5% / 80.1%**; top $158k; gift $158.0k | 72.5% | 73.0%; gift $160.2k |
| 3r, top +$0 (release kept) | not run | not run | **92.3%**; gift $155.7k |
| 3a (no release, not in top) | 78.8% / 86.0%; top $153k | not run | 78.6% within $1k |
| 3r $15k, top +$10k | 52.4% / 58.4% | not run | — |
| **BOTH (top +$5k)** | [checked] 77.3% (seed 7 77.4%) vs 3r +$5k 75.5%; since run, unverified | not run | **80.2%** (bootstrap 80.1%, history 75.1%) vs 3r 71.8% on the same paths |
| BOTH, $5k reserve, top +$0 | not run | not run | 84.8%, but gift below minimum 1.03% |
| Option 1, narrower top (¾ / ½) | not run | not run | 90.4% / 93.9%; gift −$4.4k / −$9.5k |
| 3r +$5k, narrower top (¾) | not run | not run | 89.1%; gift $156.4k |

Reading: under 3r the reserve's share in the top is the main reason the gift misses the top (LCK §4, §8). Promising less (narrower top, top +$0) or calculating exactly in 2033 (BOTH) buys a surer top; the money moves to Laura (narrower top) or is spent on the re-match (BOTH).

### What each option changes

| Option | IPS | Final Report | WInS | Notes / TNA |
|---|---|---|---|---|
| 4a | Floor defined once as a rule; minimum rule frozen | Floor and bottom figures, dated, with the share of paths at the step | None | Matches the IBTR note ("leaving less for the facility", Notes:15) and the IBTM note ("payout is not fixed", Notes:19) |
| 4b | A fixed target | Must show how often it fails | None | Conflicts with the IBTR note (KIT D4) |
| Top rule | One line on how the top is built (no dollars, IPS:68-69) | Top, chance of reaching it (one definition, one rounding rule), central value | None | VT note "a rise before 2031 lifts the top of the range co-sponsors hear" (Notes:14) stays true under every rule |

### Case and rubric lines
- **Serves:** case:114-116 (over-promising damages credibility); case:117-118 (a range and a confidence); deliv:59.
- **Strains:** case:110-112 ("meaningful personal contribution") if the top is cut far; IFX X5 (one name for the floor; it has four today).

### UNVERIFIED
- Which floor name the team uses (D0-2 and the TNA decide).
- Whether WInS shows the IBTM split between payment rung and floor (the Sheet does, VTR §3).

### Dependencies
D0-2 → D4. D1 → D4 top rule. D4 ↔ D6. D4 → D8. D4 → D9.

**AI view (labelled).** 4a is safer on every measure tested. The top rounding is a real vote (about 4 points of top reach). The minimum rule moves the share of paths at $145k by about 1.4 points but leaves the V3 median at $140k under either rule; the fee moves it more [checked]. If D1 = 3r, top +$10k should not survive unless the team states a chance of about 2 in 5.

---

## D5. One shortfall order through 2042

**The question in one line.** If money runs short, which pot pays first, in what order, before and after 2033, with every step inside the portfolio?

### Options (KIT D5; UPD §7b)
- **S1 (Jan 2027 overrun)** is fixed by the IBTR note: the 2028 deposit tops up the ladder and the facility gets less (Notes:15). Keep S1 apart from S2.
- **S2 (later coupon gap):** **5a** leftover, then the gift above the floor, then Laura's half after 2033; **5b** the D1 reserve, then her half; **5c** her half to 2042 (option 2 = D10 10b).
- **Under 3r as modelled (V3):** leftover → reserve keeps need + $5k → Laura's half plus money above the cap → gift above the floor → floor (V3 §2).
- **Under BOTH (new):** in Jan 2033 the re-match is funded leftover → reserve → Laura's half → gift above the floor; what is left of the reserve goes to the gift up to the top (R1R §0 item 3, §5 item 2). No later reinvestment is needed.
- **Chain order (sub-choice SC-chain):** use the above-cap money before cutting the gift (V3 default, F5) or not (study chain).

### Evidence
- **The chain order matters (V3 §4 F5; `sens_19oct_seed20261019.txt:28-36`):** with the study chain, option 1's gift falls below the announced minimum in **1.50%** of paths (vs 0.05%), top reach falls to 72% (vs 77%), and 1R's to 1.22% (vs 0.06%). Payments are unchanged except option 2 (0.82% → 1.40%) [checked]. VLS §2: in a "−2 points for good" path the study chain cut the gift below the top while $6-7k above the cap stayed with Laura.
- "Floor last" cannot work after 2033: the floor has been given away (KIT D5; IFX O2). V5:30 (second version) says "covered by Laura's half before the floor".
- Banned as cover: "her other assets" read as outside money, co-sponsors (case:91-92).
- A fall during 2027 still reaches Laura's money even with 3r: VREC −2 in 2027 leaves her $4.3k; VR §1d G0 $4.8k taken.
- Option 1 under D10 = 10a leaves small post-2033 gaps in about 1 path in 7 (REC §7; VREC §7).

### What each option changes

| Option | IPS | Final Report | WInS | Notes / TNA |
|---|---|---|---|---|
| 5a | Order ends with Laura's half after 2033 (needs D10 = 10b to be a real step) | Size of the uncovered remainder | None | Must match the IBTR reflection's account of who absorbs a top-up |
| 5b | Reserve first, then her half | Release rule and tests | None (or D7 option B) | None |
| 5c | Half stays to 2042 | Joint stock-yield stress | None | Strains the VT note's "only" |
| BOTH order | One 2033 funding order | Re-match cost distribution | None | None |
| Chain order | One clause: above-cap money first | The 1.50% vs 0.05% comparison | None | None |

### Case and rubric lines
Serves case:91-92, case:119-120 and IPS:64-65 ("protect the required operating payments while supporting a responsible facility contribution"). Strains deliv:55 if the TNA reflection says "the floor absorbs" and the IPS says "floor last".

### UNVERIFIED
Whether the submitted TNA reflections (due Sat 24 Oct) describe a cover order (the editor's list will say).

### Dependencies
D0-4 and the TNA → S1. D10 → whether her half is a post-2033 step. D1 → S2 order. D2 → D5. D3 → each named risk has an absorber here. D5 chain order → D1 (1R's minimum safety).

**AI view (labelled).** Whatever D1 is, the order is easiest to defend if it is written once, ends inside the portfolio, and uses money above the cap before cutting the gift; the measured cost of not doing so is a tenfold rise in gift-below-minimum paths for option 1 and 1R.

---

## D6. "Responsible" and "appropriate flexibility"

**The question in one line.** What makes the facility contribution "responsible", what does "appropriate financial flexibility" mean, and why does Laura keep half (or another share) of VT?

### Options (KIT D6)
- "Responsible": **6a** a credibility test; **6b** a flexibility test; **6c** both, plus "meaningful" (case:110-112).
- "Flexibility": **F-i** money Laura keeps after the gift; **F-ii** liquidity; **F-iii** the range and re-quote rule leave room as the project develops.
- The share: one reason for "half", or "Laura's choice" on a dial.
- Linked: D10 (on call = less flexibility), a narrower top (D4) or a 2031 lock (D8).

### Comparison

| Share of VT's value promised in the top | 1/3 | 1/2 | 2/3 | All | Source |
|---|---|---|---|---|---|
| Gift reaches the top | 76.8% | 75.1% | 73.9% | 71.9% | RA §3 row 23 |
| Size of the top (median) | $160k | $166k | $172k | $183k | RA §3 row 23 |
| Laura's bad-case cushion | $16k | $12k | $8k | $0 | KIT D6 (R31, 16 Oct, not re-run) |

- **The share sets the size of the top and Laura's cushion, not the odds of reaching it** (RA §5).
- **D10 is a flexibility choice too:** on call (10b) leaves Laura $0 free money in 2033 (V3 option 2).
- **More stocks move money from co-sponsors to Laura** (ALT §3, verified with corrections by VRA): each extra $10k of VT cuts the minimum by about $12.8k before rounding.
- **A 2031 lock moves stock risk to Laura:** about $2.8 of her expected money per $1 of expected extra gift (LCK §5).
- **"Meaningful" scale (dated, FR only):** a US$145k bottom is about NT$4.70m at 32.445 (19 Oct; rate confirmed by VIN §3, CBC page) (NREG I5), about 5 times (5.1 at 31.94; 5.2 at 32.445) [checked] the largest 2025 grant in one NCAF scheme (VCO E1, E6).

### What each option changes

| Option | IPS | Final Report | WInS | Notes |
|---|---|---|---|---|
| 6a / 6b / 6c | One principle each; "responsible" and "flexibility" appear 0 times in V5's accepted text (IFX §0 item 7) | The dial: share vs top vs cushion | None | None |
| A different share | The rule changes | Re-run the range | None | VT note unaffected |

### Case and rubric lines
Serves case:101-107; case:110-112; case:145; IPS:49-50; deliv:56. Strains case:9 and case:126-128 only if the share is presented as fixed rather than a recommendation (CR §6 rank 9).

### UNVERIFIED
ALT's totals are undiscounted (VRA A3); R31 cushion figures not re-run on 19 Oct.

### Dependencies
D10 → D6. D2 → D6. D4 top rule ↔ D6 share. D6 → D8.

**AI view (labelled).** 6c covers both halves of the case test; the share is easiest to defend as Laura's choice with its measured trade-off.

---

## D7. What the IPS says about the WInS book (and, if a reserve option wins, whether WInS mirrors it)

**The question in one line.** How does the IPS describe what the $300k WInS book represents, and does the book change before the 6 Nov lock?

### Options (UPD §7b; TC §3, verified by VTR)
- **7a.** One clause: the WInS book is Laura's post-2028 plan scaled down ("about mirrors"). No trade.
- **7b.** Switch WInS to Laura's first $300k only ("Book L", all bonds).
- **7c.** Say nothing in the IPS; explain in the Final Report.
- **If D1 = 3r, 3a or BOTH:** option **A** no trade, "about mirrors" (the reserve is about $6.4k, 2.1% of the book, inside IBTM); option **B** two trades (sell IBTM, then buy 8 Nov-2041 bonds), sized **295 or 231 IBTM shares** (VTR E1). BOTH needs nothing beyond 3r in WInS; its re-match is a 2033 action (R1R §4). 3r $15k: same two orders, larger, not trade-checked (UNVERIFIED, V3 §5b).

### Comparison (19 Oct closes; WInS-estimated bond price; VTR §5; unchanged from v1)

| Card | Orders | Fees / trades used | Cash after | IBTM gap to plan | Notes hit |
|---|---|---|---|---|---|
| T0 no trade | 0 | $0 / 11 of 200 | $3,513.79 | −1.25 points | None |
| T1b-295 | Sell 295 IBTM; buy 8 Nov-41 | $35 / 13 | $3,702 | −1.69 | None; two new notes |
| T1b-231 | Sell 231 IBTM; buy 8 Nov-41 | $35 / 13 | $2,302 | −1.23 | None; two new notes |
| T1e exact mirror | Sell 229 IBTM and 9 VT; buy 8 Nov-41 | $60 / 14 | $3,648 | exact on every line | A third note (touches VT) |
| T1a (130-150 IBTM) | | | $94-531 | | Breaks "keep at least $1,000" |
| T2 half-measure | | | $1,169 / $390 | | Avoid |
| T3 option 4 rebuild | about 10 orders | $175 / 21 | $1,898 | | Contradicts IBTO, Nov-39, Nov-41, IBTR notes |
| T4 Book L (7b) | 11 orders | $200 / 22 | $8,521 | | Contradicts VT and IBTM notes |

- Plan with 3r: about 78% of the reserve from the floor, 22% from VT; plan IBTM 32.01%, VT 6.45% (VTR E1). Scale about 0.64-0.65, not 0.667 (NREG H5).
- **Timing** (VTR §5): sale Thu 29 Oct 22:00 Sydney (after the FOMC statement, Thu 05:00, and the M6 go/no-go); bond Fri 30 Oct 22:00; fallback Mon 2 or Tue 3 Nov; nothing after Wed 4 Nov 22:00 Sydney.
- **Bond STOP check:** implied yield within 0.25 points of the treasury.gov 15-year par yield from the curve of the trading day before the WInS price update (19 Oct curve: stop below 75.15 or above 79.50) (VTR E8).
- **Gates:** logged vote with a DL-ID; Session Rules screenshot (still missing); no open orders; student-written notes of at most 300 characters, counted by a second student; no notes on the IBTM, IBTR or VT orders before the TNA is in.
- About $600 of iBond income is due Thu 5 Nov (ex Mon 2 Nov), the first payout the book can receive; whether WInS credits it is UNVERIFIED (VLS §1b).

### What each option changes

| Option | IPS | Final Report | WInS | Notes |
|---|---|---|---|---|
| 7a | One clause, true at the lock | One scale factor | None (or option B) | Matches the VT and IBTM notes |
| 7b | Book = first deposit | Explain the reversal | 11 orders, $200 | Contradicts two notes |
| 7c | None | Must explain implementation (IPS:75-76) | None | Judges compare book and IPS |
| A | "About mirrors" | One line on where the 2% sits | None | None |
| B | "Mirrors" | Trades described | 2 orders (3 for T1e) | Two new notes |

### Case and rubric lines
Serves case:129-130; IPS:75-76; deliv:55. case:132-133: WInS gains or losses never enter Laura's projections.

### UNVERIFIED
Session Rules screenshot; live WInS Nov-41 price; 2x-volume rule for bonds; under-funded order handling; "required trading activity" (FAQ:80) (VTR §4).

### Dependencies
D1 → D7. D9 → D7. SC-scale settled at about 0.64 (NREG H5).

**AI view (labelled).** 7a is the low-risk default. If a reserve option wins and the team wants the book to show it, T1b-231 matches the plan's IBTM share; T1b-295 is simpler to explain but widens the IBTM gap. Both are compliant.

---

## D8. The 2031 valuation date, the re-quote rule, and currency

**The question in one line.** On what date is the range set, may it be re-quoted (and in which direction), in what currency, and who bears exchange-rate moves?

### Options (KIT D8; CO §3)
- **8a.** One valuation date; the range held for the whole campaign; the gift capped at the top.
- **8b.** Quote in 2031 and re-quote once, downward only.
- **8c.** A firm bottom plus a formula top on a stated date.
- **Lock-in:** keep "2031: nothing traded", or add a 2031 lock (LCK).
- **Currency:** quote in US$ (case:117 "dollar range") with a dated NT$ equivalent; state who bears FX moves. No derivatives; "no hedge" is a choice to justify (IFX K5).

### Comparison: the 2031 lock-in (LCK §2-5, study engine, 19 Oct; [checked] verified CONFIRMED by `oct20/verify_lockin/`: with the reserve marked at market, 3r +$5k full lock is 75.8% MC and 66.5% history)

| | Option 1, no lock | Option 1, full lock | 3r +$5k, no lock | 3r +$5k, full lock |
|---|---|---|---|---|
| Reach the top (MC / bootstrap / history) | 68.4 / 71.3 / 80.0% | 88.3 / 81.4 / 80.0% | 73.0 / 73.0 / 73.5% | 77.1 / 75.3 / **68.0%** |
| Gift inside the range | 98.1% | 98.1% | 99.9% | 99.9% |
| Laura's kept money, mean change | — | −$2.1k (−$11k or worse in strong markets) | — | −$1.5k |
| 2031 trades in Laura's plan | 0 | 2 | 0 | 2 |

- The lock does not change the case's own test (inside the range) and does not touch payments (LCK §0, §2). The worst historical misses are rate-driven; the lock changes none of them (LCK §4).
- BOTH (D1) raises top reach to about 80% with no 2031 trade (R1R §2, study engine; about 77% on V3, unverified [checked]), and top +$0 to 92% (LCK §8): both do more for the top than a lock under 3r.

### Other evidence (VIN-verified unless marked)
- **FX alone:** over 2-year windows since 2000, a fixed US$ amount moved −10.4% to +11.5% in NT$ (5th-95th percentile; median −0.4%) (VIN §3). Rate 32.445 on 19 Oct (CBC; VIN §3).
- **Building power of a fixed US$ (FX and Taiwan construction costs together, since 2000):** over 24 months, median −5.2%, p5 −22.0%, p95 +12.5%; down in 69% of windows, down by more than 10% in 32% (VIN §3). **Correction (VIN I1):** the FX-cost correlation (−0.26 at 24 months) *widens* this spread; it is not a "natural partial offset".
- **Buying power 2031 → 2033 at Taiwan building-cost growth:** 2-year losses of 3.7 / 4.8 / 5.6 / 6.8 / 13.1% across the INF scenarios, the 13.1% at the 2026 pace (INF §4a; VIN §3 confirmed). Taiwan CCI +7.29% y/y in Sep 2026; since 2000 about 3.1% a year (VIN §3).
- **Crash timing:** a crash after the 2031 announcement leaves the gift $5-11k under the announced top, still inside the range (SEN §4.3, verified by VLS).
- **Campaign consistency:** public funders will see the number again in late-2032 applications (CO §3 item 3).
- **Matching:** "no matching offer" rests on the design, not on "matching adds little" (VCO E4: wrong).
- **Central value beside the range** is INFERENCE (VCO E10).

### What each option changes

| Option | IPS | Final Report | WInS | Notes |
|---|---|---|---|---|
| 8a | One date, one rule | The range and its chance on that date | None | VT note (Notes:14) holds |
| 8b | Re-quote rule, downward only | Both quotes | None | Same |
| 8c | Formula top | Formula explained | None | Same |
| Lock-in | Replaces "2031: nothing traded" (`/home/user/snap/main/research/insight_v1/phase_E/E6_final_spec.md:59`) | Asymmetry and its cost to Laura | None now | No conflict (LCK §7) |
| Currency line | One labelled assumption | NT$ illustration with date, rate and the building-power spread | None | None |

### Case and rubric lines
Serves case:109-120; case:143; case:146-148 (assumptions, inflation on facility costs); deliv:59. Strains IPS:68-69 if any dollar range enters the IPS.

### UNVERIFIED
Whether a 2032-maturing Treasury will be WInS-listed in 2031 (LCK §6); LCK's numbers (verifier running, no write-up yet); Taiwan funder criteria (CO, by inference).

### Dependencies
D1 and D4 top rule → D8. D6 → D8. SC-2031 sits here.

**AI view (labelled).** 8a is simplest; if a surer top matters, the top rule or BOTH does more than a 2031 lock, at no 2031 trade.

---

## D9 (optional). Floor size

**The question in one line.** Keep the floor as "what is left" of the 2028 deposit, or make it smaller and hold more VT?

### Options (UPD §7b; KIT D9)
- **9a.** Keep it and argue the measured trade-off.
- **9b.** A smaller floor, more VT (trades by the Wed 4 Nov close = Thu 5 Nov 08:00 Sydney).
- A smaller VT (15% of the deposit) is also live: minimum about $145k on a flat curve (VRA A4).

### Comparison (ALT §3, study engine with 3r study design, 19 Oct; verified with corrections by VRA)

| VT size | Minimum: flat curve (median) | Gift median | Laura's flexibility (2033 + 2042, undiscounted) | Total median (undiscounted) | Total 1-in-20 low |
|---|---|---|---|---|---|
| 15% of the deposit ($22.5k) | $145k ($140k) | $169.3k | $35.8k | $204.5k | $154.9k |
| **Today (about 21%, $30.9k)** | **$135k** ($135k) | **$163.3k** | **$41.5k** | **$204.6k** | **$154.1k** |
| 25% ($37.5k) | $125k ($120k) | $159.1k | $48.5k | $207.1k | $153.4k |
| 40% ($60k) | $95k ($95k) | $143.2k | $66.4k | $209.6k | $148.3k |

"Total" adds 2042 money to 2033 money without discounting; the current plan's $19.9k of 2042 money is worth about $12.6k in 2033 (VRA A3). Note that the 2042 money in this table uses the study's reserve formula, which VREC N3 says overstates the reserve; the *differences between rows* are the usable part.

- Payments unchanged in every row (ALT §3). Each extra $10k of VT cuts the minimum by about $12.8k before rounding (ALT §3; VRA §2).
- All-Treasury gives the same gift and less for Laura (ALT §4(2)). IEF, VGIT, SPTI and SGOV appear in the team's logged-in WInS read of 29 Sep (VRA A6).

### What each option changes

| Option | IPS | Final Report | WInS | Notes |
|---|---|---|---|---|
| 9a | No change | The trade-off table | None (T0) | None |
| 9b | Floor and risk paragraphs change | New range | Per $10k of floor moved: sell 295 IBTM, buy 40 VT, $50, 13 trades (TC T5) | **Strains** the IBTM note (Notes:19); a strategy reopen 10 days before the freeze |

### Case and rubric lines
Serves case:68-74. Strains case:110-112 if the minimum falls far, and deliv:55 under 9b.

### Dependencies
D4 → D9. D9 → D7. D9 → D6 and D8.

**AI view (labelled).** Floor size moves money between co-sponsors and Laura rather than creating money; 9a needs no trade and no note conflict.

---

## Smaller choices (log on the same day)

| Code | Choice | Options | Evidence | Changes | Depends on |
|---|---|---|---|---|---|
| SC-sizing | How rungs are sized and the ladder cost quoted | (a) maturity sizing, waiting interest extra; (b) payment-date sizing | On maturity sizing **with the fund fee**: about **$300.4k (VREC) / $300.7k (V3)** on 19 Oct; a Jan-2028 top-up in **51-52%** of paths. Fee-free: $299.6-299.9k, 49-50%. Basis D (zero-coupon amounts at holdings' dates, no fee) $297,162, 41% odds (NREG C1, C3). **Every basis A-E leaves out the fee, about $0.85-0.93k in Jan-2027 money** (V3 F2: +$848; VLS §3: $0.93k). Curve method alone moves any basis about ±$500 (VIN E3). "$293k" and "her first $300,000 is enough" are payment-date figures (REC §3) | IPS: no level; FR: one basis | D1 |
| SC-release | 3r's 2033 release rule | Keep need + $5k; $0 margin; $10k margin; fixed half; none (3a); replaced by a re-match (BOTH) | V3-family (VREC §3 G, 3r top +$10k): margin $0 → 3.0% short, worst $7.5k, top 70%; $5k → 0.6%, top 40%; $10k → 0.6%, top 16%. Study engine: no margin 1.33%, fixed half 0.79% (RT §5). BOTH replaces the guessed margin with an exact calculation (R1R §0 item 3) | FR | D1, D4 |
| SC-2033form (new) | If 1R or BOTH: which re-match form | Buy-only; trim; full | Buy-only: 1-2 trades, keeps "held to maturity", +$2.1k / +$5.8k premium. Trim: 9 trades, sells 7-30% of each of four fund positions early, +$0.4k / +$2.6k. Full: 11 trades, about 60% of the book, its cheapness mostly an artefact of 0% waiting cash (R1R §4) | IPS one rule; FR | D1 |
| SC-chain (new) | Above-cap money used before the gift is cut | Yes (V3); no (study) | Option 1 gift below minimum 0.05% vs 1.50%; 1R 0.06% vs 1.22% (V3 F5) | IPS one clause; FR | D5, D1 |
| SC-round (new) | Is the 2031 top rounded down to $1k? | Round; do not round | Worth about +3.5-3.8 points of top reach; the floor's 15 Dec-1 Jan interest is another +1.2-1.9 (VREC §2) | FR (the stated chance) | D4 |
| SC-minrule (new) | How the 2031 minimum is computed | (R − $3,700) rounded down to $5k; 98% of projected floor, net of shortfall | [checked] Moves the share of paths at $145k by about 1.4 points (48.5% → 49.9%); option 1's V3 median stays $140k under both rules (the fee, not the rule, moved it from $145k). Number sheet: 61-72% at $145k (NREG F1) | IPS rule; FR | D4 |
| SC-reinvest | Income-reinvestment rule | Own-rung; dedication; batch at the January review | V4 had own-rung; V5 has none (VR §1e). Coupons in bills: about $3.0k short on plan, $0.9k from Laura without 3r, only if bills stay about 1 point below long yields for 15 years (VR §2). WInS: about $600 of iBond income due 5 Nov; no reinvestment trade (NREG H8) | IPS principle (case:96-97) | D3 |
| SC-park | Where waiting money sits | A WInS-listed short Treasury ETF, named in the FR | SGOV seen in the logged-in WInS on 29 Sep, screenshot still needed (VR §1g). Seven of ten rungs wait 6-10.5 months (VLS §1d). "Maturing bonds, not sales, supply every payment" is false for 2038 and 2039 (IFX H1). Whether Laura's plan may hold uninvested cash: UNVERIFIED | IPS one clause; FR | D3 |
| SC-left | Where the 2027 leftover sits | Treasury to Dec 2032 (first cover); VT; joins the floor | Leftover worth for option 1: **3.3-3.4 points** on the agreed basis (not 7.9, VREC §4 item 3); for 3r about 0 only once rules (a)+(b) are in place, about 1 point in the range-audit frame (VREC §5). Joining the floor: gift +$4.0k, Laura −$5.5k undiscounted (ALT; VRA A3) | FR | D1, D5 |
| SC-keep | One definition of "Laura keeps" | Half of VT minus set-asides; everything not given or set aside, incl. above-cap money | $3-5k apart at the median (LCK §0); V3 uses the wider definition | FR, all three deliverables | D2 |
| SC-2031 | Keep "2031: nothing traded" | Keep; lock-in | See D8 | IPS | D8 |
| SC-surplus | Yearly surplus-release test 2034-41 | None; release above a stated funded ratio | Funded ratio drifts to 108-155% by 2041-42 at 5-7% (RS §7 R5) | FR | D3 |
| SC-num | IPS number policy | Case-derived only; or one or two dated anchors | IFX §3b-3c: none beyond case-derived | IPS | all |
| SC-why | The real reason to buy in January | The money arrives then; the plan does not bet on rates | V5's "so we buy now" is a non sequitur (IFX R1); the ladder cost more than $300k on 182 of 200 trading days in 2026 on basis D (NREG C7; VIN confirmed) | IPS | — |
| SC-name / SC-meta | One strategy name, one floor name; whether *Messy Roots* carries logic | — | IFX X5, Pi3 | All | D4 |
| SC-scale | WInS scale factor | About 0.64-0.65 | NREG H5 (0.667 overstates the ladder by about $7k) | FR | D7 |
| SC-label (new) | What "3r as written" refers to | "Study design" | V5 contains no reserve (VREC §3) | Internal | D1 |

---

## Decision map (one page)

**Order to take the votes** (each row depends on the rows above it):

| Step | Decision | Must be settled first | Feeds into | Needs a WInS order? | Filed-note conflict risk | IPS words (rough) |
|---|---|---|---|---|---|---|
| 0 | D0-1 to D0-4 (Wed 21 Oct) and the editor's TNA-claims list (Sat 24 Oct) | — | D10, D2, D4, D5, SC-sizing | No | — | — |
| **1** | **D10** Laura's retained half after 2033: on call or free | D0-1 | D1 (baseline), D2, D3, D5, D6 | No | 10b vs the VT note's "only" | 1 clause (changes V5:28, :30 either way) |
| 2 | **D1** cover option (incl. 1R, BOTH) **plus** the two sizing rules, the net-minimum rule and SC-chain | D0-4, D10 | D2, D3, D4-top, D5, D7, D8, SC-sizing, SC-release, SC-2033form | Only option B (2-3 orders) or option 4 (about 10) | Option 2 / 10b (VT "only"); option 4 (3-4 notes) | 3r principle about 30 words (full 3r 50-70, RT §6) [checked]; BOTH adds one 2033 rule |
| 3 | **D4** floor rule and name, minimum rule, top rule, top rounding | D0-2, D1 | D6, D8, D9 | No | 4b vs IBTR note | 1-2 lines |
| 4 | **D5** shortfall order to 2042 (incl. chain order, BOTH's 2033 order) | D0-4, D10, D1, D2 | D3 | No | "floor absorbs" vs "floor last" | 1 line |
| 5 | **D3** certainty standard | D10, D1, D5 | D8 | No | "covered at purchase" | about 60-70 |
| 6 | **D2** kept half's jobs and home | D0-1, D10, D1 | D5, D6 | No | 2a vs VT note | 1 line |
| 7 | **D6** responsible / flexibility / share | D10, D2, D4 | D8 | No | — | 1-2 lines |
| 8 | **D8** valuation date, re-quote, currency, 2031 trade | D1, D4, D6 | FR excerpt | No | — | 1-2 lines |
| 9 | **D7** WInS clause (and option A or B; 295 or 231) | D1, D9 | FR | Option B / 7b / 9b | 7b (VT, IBTM notes) | 1 clause |
| 10 | **D9** floor size (if on the agenda) | D4 | D7 | 9b (2 orders per step) | IBTM, VT notes | — |
| 11 | Smaller choices | as listed | — | No | "maturity, not a sale" | — |

**Dependency summary (arrows = "must be decided before"):**
- D0-1 → D10 → {D1, D2, D3, D5, D6}
- D0-4 → D1 → {D4-top, D5, D3, D2, D7, D8, SC-sizing, SC-release, SC-2033form}
- D5's SC-chain ↔ D1 (changes 1R's minimum safety 0.06% vs 1.22%)
- D0-2 → D4 → {D6, D8, D9}; D4 ↔ D6
- D9 → D7

**The four couplings most likely to break consistency:**
1. **D10 × D1 × the VT note:** quoting option 1 at 14% while V5:28 keeps Laura's half on call describes a plan the IPS does not state; choosing 10b gives VT a second job that the VT note's "only" (Notes:14) denies.
2. **D1 × D4-top × D8:** 3r (study design) without a top rule makes "about three in four reach the top" false (about 2 in 5).
3. **D1 × SC-sizing × the IBTR note:** on maturity sizing with the fee the ladder is about $300.4-300.7k on 19 Oct and a top-up is about a coin flip; "her first $300,000 is enough" is not the honest figure. The note stays as filed; the IPS and FR carry the correction.
4. **D1 (1R) × D5 (chain order):** whether 1R alone weakens the minimum depends on whether above-cap money is used before the gift is cut.

**Deadlines.** Options notes Mon 26 Oct 18:00; vote Tue 27 Oct 20:00 (M5); carry-overs and order go/no-go Thu 29 Oct 20:00 (M6, only if needed); any voted order entered by Fri 30 Oct 22:00, last entry Wed 4 Nov 22:00 Sydney; internal IPS submission Thu 5 Nov 20:00 (`oct20/ops/operating_plan.md:48, 119`); Wharton deadline Fri 6 Nov 17:00 ET = Sat 7 Nov 09:00 Sydney; VTR §5 [checked].

---

## Numbers: safe to quote vs never quote

### Safe to quote (always with its date, its basis and "model"; IPS only where marked)

| Number | Where it may go | Source |
|---|---|---|
| $300k (2027) + $150k (2028) in; ten fixed $50k payments 2033-2042 out | IPS, FR, anywhere | case:43-45, 88-90 |
| About 5.1% a year needed on the 2027 deposit alone (5.087% annual; 5.024% semiannual); about 1.0% on both deposits | IPS, FR | NREG B2; VIN §2 |
| About 7% a year for world stocks (JPM 2026 LTCMA, compound, nominal); 2.5% US inflation as the stated assumption | IPS (as assumptions, source in FR) | NREG I1, I2 |
| Concept, not a sentence: rounded shares of Laura's plan after Jan 2028 (about 2/3 payment Treasuries, 1/4 floor, under 1/10 stocks), labelled [consistency fix 20 Oct, row 32] | IPS (labelled), FR | NREG E5 |
| Ladder about $297-301k on the 19 Oct close depending on basis and whether the 0.07% fund fee is counted (about $300.4-300.7k on maturity sizing with the fee); about $290 per 0.01-point move | FR, Q&A | NREG C1, C4; VREC §2; V3 §5b |
| A Jan-2028 top-up is needed in about half of model paths on maturity sizing with the fee (51-52%); about two in five on basis D without the fee | FR, Q&A | V3 §5b; VREC §2; NREG C3 |
| A permanent 2-point fall in reinvestment yields leaves about $19,500-21,300 to cover, depending on method | FR | VIN E1; NREG D1 (corrected) |
| With 3r and both sizing rules: payments short in under 1 path in 100 under parallel rate moves, worst about $3,000-4,000 (the worst of 100,000 paths varies by seed: $3.1-3.8k); about 0.8% with real curve twists in the bootstrap (worst about $6-7k) and 2.8% of overlapping history windows with twists [checked] | FR only, with the rules, D10's answer and the conditions beside it | V3 §5a, §6; VREC §7 |
| Without a reserve and with Laura's half free after 2033: small post-2033 gaps in about 1 path in 7, typically about $1,500, worst about $10,000; **about 0.8-1.5% if her half stays on call (V3 / VREC), with larger worst cases ($7-13k; $23k on the twisted bootstrap) because the back-up is stocks** [checked] | FR, with D10's answer | VREC §7; V3 §5a |
| Under the plan as written, a permanent fall before 2033 never leaves a payment short; it lowers the gift and Laura's free money | FR, Q&A | VREC §0 item 5, §6; V3 §5d |
| 3r costs about $10k of minimum and about $3k of typical gift (about $6k with the top fix); about $10-15k of the reserve returns to Laura in 2042 | FR | VREC §7; V3 §5b |
| $10k in the Nov-2041 bond covers roughly 1.0-1.5 points of permanent fall that starts during 2027 and roughly 1.5-2.1 points after Jan 2028 [checked: includes VREC's crossover measure], depending on method (a gap measure, not a payment-risk figure) | FR, Q&A | VLS §1e; V3 §5d |
| A 2033 re-match (buy-only) costs about $2,000 more at the median than the frozen estimate, about $6,000 in a 1-in-20 case, with 1-2 trades (study engine) | FR, if 1R or BOTH | R1R §2 |
| About three in four model paths reach the top: **only** for option 1 or 3r with the top fix, with "exact" or "within $1,000" named; "under half" for 3r with the top counting the full reserve | FR | VREC §7; V3 §5b |
| Gift lands inside the range in about 99 of 100 model paths (with the net-minimum rule), always beside the payment figure | FR | NREG F4 |
| A 40% world-stock fall in 2032 cuts a typical gift by about $7,000, never below the minimum | FR | NREG F7 |
| About 108.5-110.4% funded after both deposits, depending on basis (a funding test that counts the committed 2028 deposit) | FR | VLS §1a |
| The ladder's real yield about 2.7-2.9% on 19 Oct (10-year TIPS 2.80%) | FR | VIN I3 |
| The 2042 payment buys about 80% of the 2033 one at 2.5% US inflation | FR | NREG B3 |
| A fixed US$ amount moved about −10% to +12% in NT$ over 2-year windows since 2000 (5th-95th percentile); in building terms −22% to +13% | FR | VIN §3, I1 |
| WInS: about a third in IBTM, about 90% Treasuries; VT about 9% of the book, about 7% of Laura's plan; scale about 0.64 | FR | NREG H3-H5 |

### Never quote (wrong, superseded or misleading)

| Do not say | Why | Source |
|---|---|---|
| "0.02%" as 3r's payment risk; "zero in 690 history windows" | Study-engine artefacts; canonical about 0.6%; 2.8% of windows with real curve twists; even on the study engine 0.08% / 0.32% / 0.72% once the reserve is marked at market [checked] | NREG D5; V3 §6; verify_lockin §5 |
| [checked] "BOTH is 0% in every test"; "BOTH reaches the top 80% vs 72%" without "study engine" | V3 (unverified): 1.88% short if the re-match counts fund bill interest; top 77.3% vs 75.5% | `engine_v3/data/bo_tables.txt` |
| [checked] "Under the study minimum rule the option 1 minimum is $145k again" | V3: stays $140k (49.9% at $145k) | `results_v3.csv` sens row |
| "Never more than about $3k short" without "under parallel moves" | Bootstrap with twists: worst $6.1-6.8k | V3 §6 |
| "77%", "45%", "76%" (or any exact top-reach figure) | Depends on rounding and interest conventions: 72-78 / 40-46 / 72.5-77% | VREC §0 item 2 |
| "About 14%" for option 1 without saying Laura's half is free after 2033 | 1.4% if it stays on call (V5:28 read literally) | VREC §3 A |
| "$145k" as *the* option 1 minimum | Median $140k with the fee; $145k step in about half of paths | V3 §5c; VREC §2 |
| "$299.9k" or "50%" as the maturity-sized ladder | Fee left out; $300.4-300.7k, 51-52% | VREC N1; V3 F2 |
| "About $19k back to Laura in 2042" from the reserve | Reserve itself about $10-15k; $19-20k figures are totals incl. surplus or the study formula | VREC N3; V3 §5b |
| "$18,952" / "about $19,000" as the 2-point coupon gap | $19,488 after the line-141 fix | VIN E1 |
| "The leftover is worth 7.9 points" | 3.3-3.4 points on the agreed basis | VREC §4 item 3 |
| "1R alone breaks the minimum 10 times as often" without the chain order | 1.22% vs 0.06% depending on chain order | V3 F5; R1R §2 |
| "1R / BOTH has zero risk" or "the re-match is free" | Removes reinvestment risk after 2033 only; costs about $2-6k of insurance | R1R §5 |
| "6%" or "6.2%" as 3r's risk | One rule set (range-audit rules) | REC §5 |
| "0.41% if counted consistently" | A hybrid | REC §6 item 8 |
| "About three in four reach the top" under 3r with the full $10k in the top | About 2 in 5 | V3 §5b |
| "$10k there does the job of $25k in IBTM" | Artefact of 0% after 2032 | RT §2a |
| "$10k covers about 1.5 points" | Mixed timing; WRONG | VLS §1e |
| "Its price rises, so it covers the gap" | Date-qualify; covers about a fifth of the gap | RT §2b; VLS §1e |
| "16% falls to 7.5% with T-bill interest" | Not a consistent figure | RT §1b |
| "With 3r nothing is taken from Laura" (unqualified) | A 2027 fall still leaves her about $4k | VREC §6; VR §1e |
| "The 1984 path with 3r holds" | Passes by only $185 after the iBond fix | VIN E1; VR §1e |
| "$4.2k short if coupons sit in bills" | About $3.0k, $0.9k from Laura, conditional | VR §2 |
| "$293k", "$292,000", "her first $300,000 is enough" as today's cost under maturity sizing | Payment-date figures | REC §3; NREG C1 |
| "$300,174" or "$298,446" as "the cost" | Study sizing, for comparing options only | NREG §0a |
| "110.4% funded" without its basis | Most favourable basis; counts the 2028 deposit | VLS §1a |
| "$9.9k hidden cushion" | About $4k relative to basis D | VLS §1d |
| "$2.4k from lower-coupon bonds" | The 1.375% Nov-2040 is not WInS-listed per the filed note | VLS §1c |
| "2.6% real yield" | 2.7-2.9% | VIN I3 |
| "The NT$ and building costs partly offset" | They reinforce; the spread widens | VIN I1 |
| Scale "300/450" or "0.667" | Overstates the WInS ladder by about $7k | NREG H5 |
| "About 9% of all money" for Laura's plan | That is the WInS share | NREG H4 |
| "5.000% Feb-2037" | It is 4.750% | VR §1e |
| "16 times the largest NCAF grant" | About 5.1 times, one scheme | VCO E1, E6 |
| "Matching adds little"; "donor-tested message" | Wrong or by analogy only | VCO E4, E12 |
| Any ALT total that adds 2042 money to 2033 money | Undiscounted | VRA A3 |
| "Cheapest since May 2002"; "182 of 199 days" | UNVERIFIED; stale (182 of 200 to 19 Oct) | NREG C7 |
| Any "guaranteed", "risk-free", "cannot miss"; "her other assets" as cover | Over-promise; reads as outside money | KIT D3; IFX O1 |
| Any **measured or model** percentage, dollar range, ladder level, floor level or coupon-gap size **in the IPS** (case-derived figures and stated assumptions excepted) [consistency fix 20 Oct, row 32] | IPS:51-52, 68-70 | IFX §3c |

---

## Still UNVERIFIED (affects the vote)

1. **BOTH and the buy-only 1R re-match on the V3 engine:** [checked] now run (`engine_v3/data/bo_*`, 23:37-23:46 UTC) but no write-up and no verifier; R1R's verifier (`oct20/verify_rematch/`) still had no write-up at 19 Oct 23:41 UTC.
2. **LCK** (lock-in, narrower top, top +$0): [checked] verified CONFIRMED (`oct20/verify_lockin/verify_lockin.md`, 23:33 UTC); apply its five wording fixes (§4). The narrower top at ½ (93.9%) was not re-checked.
3. D10 options 10c and 10d (not modelled); whether the team intended V5:28 to apply after 2033.
4. That 15-Nov Treasury notes for 2033-41 will be outstanding in 2033; retail bid-ask then.
5. The WInS Session Rules screenshot; the live Nov-41 price and accrued interest; the 2x-volume rule for bonds; under-funded order handling; "required trading activity".
6. When WInS credits coupons and iBond payouts (about $600 of iBond income due Thu 5 Nov; T-bond coupons Mon 16 Nov).
7. Whether Laura's plan may hold uninvested cash; whether the TIPS/STRIPS ban covers ETFs built on them (Wharton batch 2).
8. How Wharton counts words; meet the strictest reading.
9. The 20 Oct curve was not published at 19 Oct 23:07 UTC (VIN §0); one curve day moved the ladder $1.7k (V3 §8). Every figure here is MODEL from AI-built code on the 19 Oct curve. Students re-derive any figure they use and re-price on the 6 Nov close for the Final Report.
