# Red team: BOTH (3r top fix + buy-only 2033 re-match) against 3r alone and option 1

AI-generated devil's-advocate analysis by Claude Code for Team Caplet, Tue 20 Oct 2026 (Sydney), for the Tue 27 Oct vote on covering the coupon gap. Every figure is MODEL output from AI-written code; no student has rebuilt any of it. Nothing here is text to submit. There are no drafted IPS, TNA or Final Report sentences: deliverable content is named only as elements. Every "AI view" is opinion, and the team decides. If the team uses anything here, log it in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). No personal data appears. Ray is named only as the team's sole WInS trader.

**Paths.** `S/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/`. This folder is `S/oct20/redteam_both/`: attack scripts are in `scripts/` and outputs in `toolkit/data/`. **case:n** = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`. **IPS:n** = `.../2026_WGY_Investment_Policy-FINAL.txt`. **Notes:n** = `/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`, the filed WInS notes, which cannot be edited. **V5:n** = `S/oct19/drive/ips_report_live.md`. Each V5 line holds two runs, and the **accepted** run is the second one (`S/oct20/verify_ipsfix/ips_fix_list_checked.md:14`). **VP** = `S/oct20/verify_vote2/votepack_v2_checked.md`. I use the checked copy, not v2, as the coordinator instructed. **E3** = `S/oct20/engine_v3/engine_v3.md`. **BO** = `S/oct20/engine_v3/data/bo_tables.txt`. **VE3** = `S/oct20/verify_engine3/verify_engine3.md`. **VRM** = `S/oct20/verify_rematch/verify_rematch.md`. **VV2** = `S/oct20/verify_vote2/verify_vote2.md`. **R1R** = `S/oct20/rematch1R/rematch_1R.md`. **ATT** = my runs, `S/oct20/redteam_both/data/attack_N20000_s20261019.txt` and `..._s7.txt`.

---

## 0. Verdict in seven lines

1. **BOTH's only verified gain is on payments.** It is 0% short against about 0.6% for 3r-fix under parallel moves (0.7-0.8% on the twisted bootstrap, 2.8% in the twisted history). It has **no top-reach advantage**: 73.0% against 75.4% on a realistic bond-units booking (VE3:22-23). Its median minimum and gift equal 3r-fix's (BO:3-4).
2. **Its cost is small.** It needs a 2033 purchase of about $8.5-10.5k at the median (about $26-27k at the 1-in-20 high) in 1-4 buys (E3:281; VE3:22). Laura's total money is about $2.5k less than under 3r-fix when both are credited fairly (VE3:27).
3. **The "0% in every run" holds by construction, so it is not evidence of robustness.** After 2033 the model pays the payments from the same cash-flow function the re-match was sized on (section 5a). Every robustness run therefore tests only whether the 2033 funding chain can pay the bill. **Do not quote "0%" or "in every run" as a certainty level.**
4. **New attack (ATT).** BOTH drops 3r's $5k safety margin (`S/oct20/engine_v3/scripts/engine_v3.py:638`), so anything the model does not see hits it at once.
   - If the four iBond funds IBTO-IBTR pay out 0.1% (about $50 each) less than modelled, BOTH is short in about 0.2% of paths.
   - At 1% less, BOTH is short **more often than 3r-fix** (6.7-6.8% against 5.7-5.9%), though by smaller amounts.
   - So BOTH removes rate risk. It does not remove all risk.
5. **The instrument attack fails, which is good for BOTH.** Limited to bonds already held and WInS-listed (Nov-40 and Nov-41), the re-match is still 0% short at the same cost (ATT). In practice it often just re-labels reserve bonds as ladder bonds (VRM 2.2(g)).
6. **As an IPS element it is a real rule, and it is close to cheap in words.** It replaces 3r's guessed release margin with an exact 2033 check, which answers case:95-97 and IPS:47-49 directly. My estimate is +10-20 words over 3r's principle, or +25-35 with a two-stage certainty definition. Section 3 explains why it is a real rule and not an execution detail.
7. **Option 1 with Laura's half on call after 2033 (D10 = 10b) is simpler to hold but not simpler to defend.**
   - It is about 1.6% short, worst about $7k (VE3:36), or 0.8% with a worst of $12-23k in the stock form (VV2:46).
   - Its back-up is stocks, and it locks Laura's flexibility money in the portfolio to 2042.
   - It strains the filed VT note (Notes:14) and the accepted V5:30, which fits 10a (VV2:24).

---

## 1. What is being compared (one basis: engine_v3, 19 Oct curve, 100,000 paths, seed 20261019, seed 7 in brackets)

| | Option 1, half free after 2033 (10a) | Option 1, half on call (10b) | 3r top fix | BOTH |
|---|---|---|---|---|
| A payment short (> $100) | 14.79% (14.66%), worst $10.1k (BO:5) | about 1.6%, worst about $7k (VREC reading on v3, VE3:36); stock form 0.82%, worst $12.2k (VP:122) | 0.61% (0.64%), worst $3.3k (BO:4) | 0.00% (0.00%), residual dust $0.1k (BO:3) |
| Twisted bootstrap / twisted history | 17.4-17.6% / 16.1% (E3:289-292) | stock form 1.0%, worst $23k (VV2:46) | 0.71-0.76%, worst $6.1-6.8k / 2.76% (E3:289-292) | 0% / 0% (E3:289-292) |
| Gift reaches the top | 76.9% | not run | 75.5% (lump) / 75.4% | 77.3% lump; **73.0% units book** (VE3:22-23) |
| 2031 minimum (median) / gift below it | $140k / 0.05% | — | $135k / 0.004% | $135k / 0.000% (BO:3-4) |
| Laura's 2033 money, 1-in-20 / median | $0 / $25.0k | $0 / $0 in the stock form (VP:123) | $6.7k / $22.3k | $5.1k / $27.0k (BO:3-4) |
| Laura's 2042 money (median) | $8.8k | $56.3k, still in stocks (VP:124) | $24.7k | $18.5k (BO:3-4); the fair total is about −$2.5k against 3r-fix (VE3:27) |
| New holdings / WInS orders before 6 Nov | none / 0 | none / 0 | Nov-41 reserve / 0 or 2 (VP:333) | as 3r / as 3r (VP:337) |
| 2033 real-plan trades | 0 | 0 | about 1 (reserve sale) | 1-4 buys, median 1 (BO:3) |

Reading notes:
- **10b has two forms.** "Option 2" (the projected need also left in stocks) is not the VREC on-call reading. Quote 10b as about 1.6%, worst about $7k (VE3:36, :77).
- **The top-reach gap between the engines is explained.** BOTH drops 3r's $5k margin, so it gains top-reach only where the re-match premium is under $5k. That is 63% of paths on v3 (VE3:35, :55-60). On the more realistic units booking the gain turns into a 2.4-point loss (VE3:62).

---

## 2. (a) The plain-English test: can a 16-year-old explain it in two sentences and defend it?

**The two-sentence content (elements, not wording):**
- Sentence 1: what is set aside, when and why. A small extra long Treasury, bought from the 2028 deposit, as cover for low interest rates.
- Sentence 2: what happens in January 2033. An exact check, payment by payment, of the cash that will arrive before each payment, counting no interest. Then the team keeps the reserve bonds that check needs, buys more of the same long bonds if needed, and releases the rest to the gift.

**Verdict: it passes the two-sentence test, if the team frames it as a running balance and not as a "linear programme".**
- The constraint the model solves is a running balance at 0% interest that must never go negative at a payment date. Surplus only carries forward (`engine_v3.py:164-169`, the carry equalities).
- A student can do that in a spreadsheet: nine rows, one per payment, with cumulative cash minus cumulative payments.
- With only held bonds allowed, the fix is "buy more Nov-41, sometimes Nov-40" (ATT: Nov-41 in 85% of paths, Nov-40 in 48-49%).
- UNVERIFIED: whether a simple "buy the longest held bond" rule matches the LP's cost. I did not test it.

**Where defence under questioning gets hard (each needs a rehearsed answer):**
1. **"Why 0% interest?"** Because the sizing must work even if cash earns nothing. That convention carries the whole 0% result: if the check counts the funds' own bill interest, BOTH is 1.88-1.93% short, worst $2.8k (E3:294, :299; VE3:21). A student has to understand that a deliberately pessimistic rule is the source of the certainty.
2. **"Why keep a reserve if you re-match anyway?"** Because the 2033 bill can reach about $26-27k at the 1-in-20 high (E3:281; VE3:22). The $10k reserve grows to $13-16k by 2033 (VRM:180). Without it the cost falls on Laura's half and then the gift, and 1R alone breaks the minimum about 8 times as often (VRM:47, :240).
3. **"So is it 0% or not?"** See section 5. The defensible answer is "no dependence on future interest rates after 2033", not "zero risk".
4. **"Isn't that what your $5k margin did?"** Yes, approximately. BOTH swaps a guessed margin for a calculated one, and loses the margin's cushion against things the model cannot see (section 5c).

**AI view (labelled).** 3r alone is easier to defend in one breath: "a small spare bond for low rates". BOTH is easier to defend against "why $5k?", because there is no guessed number. 3r's margin is exactly the kind of unexplained figure a judge picks at. Each option carries one weak spot: 3r's is its arbitrary margin, and BOTH's is the knife-edge 0%.

---

## 3. (b) IPS word cost and (c) is it a real IPS rule?

**Budget.** The limit is 500 words (IPS:39, :109). The kit targets 470 or fewer with headings counted (`S/oct19/ipskit/ips_writing_kit.md:55-56`). The IPS bans citations and calculations and asks for "strategy and decision-making framework ... rather than ... detailed financial calculations" (IPS:51-52, :123).

**Element counts.** These are AI estimates of how many words each element needs in the students' own words. No sentences are drafted.

| Option | Elements the IPS must carry | Already in accepted V5? | Estimated net words |
|---|---|---|---|
| 1 (10a) | (E1) reinvestment named as the residual risk; (E2) a one-time 2033 cover order that ends inside the portfolio (leftover → her half → gift above the floor); (E3) a limit making clear the January review's call on her half ends in 2033 | E1 and E2: largely, at V5:25 and V5:30 accepted ("covered by Laura's half before the floor"); E3 no (V5:28 is silent on after 2033, VV2:24) | +0-10, but the certainty standard is then hard to state honestly (section 7) |
| 1 (10b) | E1; (E2') her half stays invested inside the portfolio to 2042 as the payment back-up; (E4) what that does to flexibility | No. It changes the meaning of "retained" | +15-25 |
| 3r top fix | (R1) a small Treasury reserve from the 2028 deposit; (R2) kept outside the announced minimum; (R3) a 2033 release rule (keep the need plus a margin); (R4) the top counts part of it; (R5) the reserve as the one holding that may be sold | No | About 30 for the principle; 50-70 in full (VP:333; `S/oct20/redteam3r/redteam_3r.md:199`) |
| BOTH | R1, R2, R4; **R3' replaces R3**: a once-only 2033 cash check, buy-only, sized assuming idle cash earns nothing; R5 shrinks to "only the released part is sold" (VRM 2.2(g)); optional (C4) a two-stage certainty definition (before 2033 the reserve, after 2033 only the Treasury paying) (VP:427; R1R:205) | V5:28 accepted already has a "January review" with Laura (V5:28), so R3' can attach to an existing element | +10-20 over 3r's principle (about 40-50 in all); +25-35 with C4 |

**(c) A real rule or an execution detail?**
- **The once-only 2033 composition change is a real IPS rule.** It is a pre-committed, dated change to the operating reserve's make-up, set off by a known event. The brief asks for this directly:
  - "planned changes in the portfolio as future funding needs approach" (IPS:47);
  - "managing the operating reserve's asset composition over time" (IPS:49);
  - "How will the portfolio's asset allocation and composition change" (IPS:22-23);
  - the case: "explain how its composition should change, if at all" (case:95-97).
  
  Of all the options it is the most IPS-native answer to that question. 3r's release rule is also a composition change, but with a guessed parameter.
- **Execution details stay out of the IPS:** the LP, the choice between Nov-40 and Nov-41, bid-ask, tickets, rounding, and any dollar size. IPS:51-52 and IPS:68-70 put calculations in the Final Report.
- **One assumption sits on the line:** idle cash counted at 0%. It is a policy choice, not a calculation, and the 0% result depends on it (E3:299). AI view: it earns a short clause if the team adopts BOTH. Without it, the rule is underspecified.
- **The trap: the strategy freezes at the IPS** ("may not revise its investment strategy after the submission deadline", IPS:73-74). If the team wants the 2033 check, the IPS must name it at element level by 6 Nov. It cannot be added to the Final Report later as a new rule.

---

## 4. (d) Conflicts with the filed WInS notes and the TNA story

Notes cannot be edited (VP:19). The TNA picks are VT, IBTR and IBTM (Notes:28-31). The TNA freezes before the vote: it is due 23 Oct ET, which is Sat 24 Oct 08:00 Sydney (`/home/user/caplet-investment/CLAUDE.md`, current status).

| Filed note | What it says (quoted) | BOTH | 3r alone | Option 1, 10b |
|---|---|---|---|---|
| VT (Notes:14), a TNA pick | Stocks "only set how far her gift rises above her promised minimum" | Mild strain, shared by every option: the funding order reaches "Laura's half" when leftover plus reserve fall short (VP:180) | The same mild strain | **Strong strain.** VT gets a standing payment back-up job to 2042 (VP:140 row 10b) |
| IBTR (Notes:15), a TNA pick | Falling yields → "the 2028 deposit would top up the ladder, leaving less for the facility" | **Consistent.** The same logic extends to 2033: falling yields cost the facility side first, never the payments | Consistent | Consistent before 2033; after 2033 the cost lands on Laura's stocks |
| IBTM (Notes:19), a TNA pick | A floor "giving co-sponsors a minimum figure in 2031"; "final payout is not fixed" | Consistent: gift below the minimum 0.000% (BO:3). But "payout not fixed" is the very risk BOTH's 0% ignores (section 5c) | Consistent | Consistent |
| Feb-37 (Notes:16) | "reinvestment-rate risk on the proceeds held in a short-term Treasury ETF" | **Answers it directly.** BOTH sizes that waiting cash at 0% | Answers it in part | Leaves it to stocks |
| Nov-39 (Notes:18), Nov-41 (Notes:24) | "reinvested coupons fund the rest" / "with reinvested coupons funding part of each" | **Soft tension.** After 2033 BOTH relies on no reinvestment. The notes describe the plan at purchase in 2027, so this is a change of method in 2033, not a contradiction. A judge may still ask (section 8, Q9) | None | None |
| IBTO-IBTQ (Notes:20-22) | "Its payout is not fixed" (three notes) | Same as the IBTM row: the team's own notes flag the residual risk that BOTH's headline leaves out | — | — |

**WInS:** BOTH needs nothing beyond what 3r needs (option A, no trade; or option B, two trades; VP:337, :622; R1R:193). The re-match is a 2033 real-plan action, after the 6 Nov freeze.

**For the TNA, written before the vote:** element-level advice only.
- A reflection should not commit to any one cover for reinvestment risk. Do not claim it is "covered by Laura's half" or "covered by a reserve".
- The fact kit already warns that "covered by Laura's half" is a model claim, not a certainty (`S/oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md:162-163`).
- Naming the risk, and saying the team will set its cover in the IPS, is consistent with every option.

---

## 5. (e) Model risk: what has to be true for "0%", and is it quotable?

### 5a. The 0% holds by construction
- The re-match is sized with `hold_windows` (`engine_v3.py:300-329`) inside `bo_cost` (`:545-556`).
- The payments after 2033 are then realised with the **same** `hold_windows` on the same holdings (`:680-691`).
- Waiting cash is sized at 0% and realised at T-bill rates floored at 0% (yield floor 0%: E3:176, F9). Realised cash after 2033 can therefore only equal or beat the sizing.
- So a payment can be short only if the 2033 funding chain cannot pay the re-match bill (VE3:20; R1R:144).
- The history, bootstrap and twist runs vary what happens **before** 2033. They do not test the after-2033 promise at all.
- So "0% in every run" is a property of the bookkeeping, not an empirical finding.

### 5b. Conditions for the 0%, tested where possible

| Condition | Status | Effect if it fails | Source |
|---|---|---|---|
| Idle cash, including the iBond funds' last months to 15 Dec, sized at 0% | A plan rule the team must adopt | 1.88-1.93% short, worst $2.8k | E3:294, :299; VE3:21 |
| Bonds to buy exist and are WInS-eligible | **PASSES.** Held bonds only (Nov-40, Nov-41, rarely Nov-39 or Feb-37): 0% short, re-match median $8.5k / $8.4k, 1-in-20 $25.8k / $25.6k, the same as with new notes | none | ATT (both seeds); VRM:114-135 (2033-35 Nov notes exist but are not WInS-listed; Nov-36 to Nov-38 do not exist yet) |
| Bid-ask and tickets | Negligible | Median cost +$22 with costs removed; about +$40 at 0.50% bid-ask | VE3:20; R1R:171 |
| Rounding | Buys round **up** to $1,000 face, which only adds cash. Buys under $100 are ignored, leaving dust | Residual shortfall up to $0.1k, under the $100 "short" threshold (ATT: worst $38 / $92) | E3:280; `engine_v3.py:553-554` |
| Pre-2033 coupons booked as a lump, not as bond units | A convention | Cost +$1.9k median; top reach 73.0% against 75.4%; payments still 0% | VE3:20-23 |
| The 2033 chain does not run dry (leftover → reserve → her half → gift above floor) | Never ran dry in any run | If it did, the floor would be hit, which breaks the IBTM note's promise | E3:142; BO:3 |
| **iBond fund payouts (IBTO-IBTR) arrive exactly as modelled** | **The model treats each fund as one bond at its weighted coupon and maturity** (E3:366). The team's own notes say "payout not fixed" (Notes:19-22) | **See 5c: the 0% breaks at a $50-per-fund miss** | ATT |
| The US Treasury pays on time | Assumed | Not modelled | — |
| Someone runs the check in January 2033 | A real-life step for Laura or her adviser | Not modelled | R1R:195 |

### 5c. The new attack: iBond payouts below the model, applied after 2033 only
Method: each of IBTO, IBTP, IBTQ and IBTR delivers h × $50,000 less cash than modelled. The haircut is applied to realised cash only, never to the 2033 sizing, because it is a risk the plan cannot see. Applied to BOTH and to 3r-fix alike. Setup: v3 basis, 19 Oct curve, 20,000 paths, two seeds, lump booking. Code: `scripts/attack.py`, which runs a patched copy of engine_v3 with switches `fund_haircut` and `bo_universe` that default to the original behaviour. The diff is the only change; `scripts/engine_v3_orig.py` is the untouched copy.

| Haircut per fund | BOTH short (seed 20261019 / 7) | BOTH worst | 3r-fix short | 3r-fix worst |
|---|---|---|---|---|
| none | 0.000% / 0.000% | $38 / $92 (under the threshold) | 0.725% / 0.665% | $2.06k / $2.00k |
| 0.10% (about $50) | 0.170% / 0.235% | $238 / $292 | 1.925% / 1.955% | $2.27k / $2.20k |
| 0.25% (about $125) | 1.110% / 1.175% | $538 / $592 | 2.925% / 2.890% | $2.59k / $2.50k |
| 0.50% (about $250) | 3.280% / 3.515% | $1.04k / $1.09k | 4.015% / 3.970% | $3.12k / $3.03k |
| 1.00% (about $500) | **6.800% / 6.730%** | $2.04k / $2.09k | **5.860% / 5.710%** | $4.19k / $4.10k |

What it shows:
- **BOTH's 0% is knife-edge.** The check leaves no slack in low-rate paths, where the real T-bill cushion is about zero.
- **BOTH's shortfalls stay smaller than 3r's**: about half the worst case at every level.
- **At a 1% miss BOTH is short slightly more often than 3r.** BOTH released 3r's $5k margin (`engine_v3.py:638`).
- The real size of fund payout error is **UNVERIFIED**. The haircut sizes are illustrative stresses, not estimates.
- By 2033 the funds' holdings will be known exactly, so the error is probably small for IBTO and larger for IBTR. That too is UNVERIFIED.
- **Inference, not run:** a kept cash cushion of about $2-2.5k (the worst total gap at a 1% miss) would absorb this stress. It would cost some top-reach, by the margin mechanism in VE3:55-60.

### 5d. How to say it
- **Never** quote "0%", "zero risk", "guaranteed", "in every run" or "no payment can be short" (R1R:221; VP:854).
- **Claim (element level):** after the 2033 check, the remaining payments no longer depend on future interest rates.
- **Conditions to state with it:** idle cash assumed to earn nothing; the Treasury funds pay out as their holdings imply; the US government pays.
- **Final Report quoting rule:** "no modelled path short by more than $100", always with:
  - the engine, curve date and paths (v3, 19 Oct, 100,000 × 2 seeds, history, bootstrap);
  - the two sensitivities that break it (1.9% if fund bill interest is counted; small gaps from a fund payout miss of 0.1% or more);
  - the note that the 0% is by construction after 2033.
- **The IPS carries no number** (IPS:51-52, :123).
- **Payment gap against 3r:** quote "about 0.6% against about 0 under parallel moves; 0.7-0.8% (bootstrap) or 2.8% (history) for 3r with real curve twists". Never use the study-engine gap (VRM:247). If the study engine must be cited, use the reserve marked at market: 0.08% / 0.32% / 0.72% (VV2:17).

---

## 6. (f) Does BOTH change anything Laura cares about, compared with 3r alone?

| Case test | BOTH vs 3r-fix | Material? |
|---|---|---|
| "high degree of certainty" (case:91-92), defined and tested (case:97-99) | 0% against 0.6% (parallel), 0.7-0.8% (bootstrap), 2.8% (twisted history); worst $3.3-6.8k for 3r (E3:289-292). The gap shrinks or reverses under unmodelled fund error (5c) | **Real but small.** Its main value is a cleaner certainty definition after 2033 (C4) |
| A credible 2031 range (case:114-120) | No top-reach gain (73.0% vs 75.4% units; 77.3% vs 75.5% lump); the same $135k minimum; below the minimum 0.000% vs 0.004% (VE3:22-23; BO:3-4). Both are "about three in four" | **No.** Co-sponsors would hear the same range |
| "protect the portfolio's ability to fund" the payments (case:119-120) | Both protect the floor; the chain reaches the gift above the floor before the floor | No difference |
| Flexibility (case:102-103, :145) | +$4.7k in 2033 (median $27.0k vs $22.3k), −$6.2k in 2042; fair total about −$2.5k (BO:3-4; VE3:27). In bad paths the re-match bill (up to about $27k) draws her half, as 3r's chain does | **Small.** Slightly more early flexibility, slightly less total |
| Composition change asked for (case:95-97) | BOTH gives a concrete, dated answer; 3r gives a release rule with a guessed margin | **Presentation value**, not money |

**AI view (labelled).** For Laura the visible outcome is almost the same. BOTH's value is in how the team can define and defend "high certainty" after 2033, and in answering case:95-97 with a rule rather than a guess. That is a Client Knowledge and Investment Strategy argument (evaluation criteria, `competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt:55-59`), not a better result for her.

---

## 7. (h) Is option 1 under the on-call reading (10b) simpler and good enough?

**Simpler:** yes, in what it holds. There is no reserve, no 2028 purchase, no 2033 check and no WInS trade.

**Good enough:** AI view, no. The reasons:
1. **Frequency is only somewhat worse than 3r, but the tail is worse.** About 1.6% short, worst about $7k (VE3:36). In the stock form 0.82%, worst $12.2k, and $23k on the twisted bootstrap (VV2:46). 3r is 0.6%, worst $3.3k.
2. **The back-up is stocks**, so its bad cases come with stock crashes (VP:129).
3. **It contradicts what the team has filed.** The VT note says stocks "only" decide the gift's rise above the minimum (Notes:14). The accepted V5:30 places the draw "before the floor", which fits 10a, not 10b (VV2:24). V5 is ambiguous, not a choice already made (VP:104).
4. **Flexibility is the casualty.** Her half must stay invested in the portfolio to 2042. In the stock form Laura has $0 free money in 2033 (VP:123), against case:102-103 and :145.
5. **It needs IPS words too**, about +15-25 (section 3), to say her half stays in.

**Option 1 under 10a** is about 1 path in 7 short (14.8%; BO:5). AI view: that is not defensible as a "high degree of certainty" standard (case:91-92) unless the team states it openly, and a judge will see the gap.

---

## 8. (g) What a sceptical Wharton judge would ask, and which option it hurts

| # | Question | Hurts |
|---|---|---|
| 1 | "You claim certainty. What could still make a payment short after 2033?" | BOTH if it says "0%"; option 1 under either reading |
| 2 | "Why hold a spare bond and re-match? Isn't that belt and braces?" (answer: the reserve pre-funds a bill of up to about $27k and grows to $13-16k; VRM:180) | BOTH |
| 3 | "Why does your reserve keep exactly $5k extra?" | 3r |
| 4 | "Why assume cash earns nothing? Isn't that unrealistic?" (answer: it is the sizing rule; most of the cost returns as interest, VRM:27-28) | BOTH |
| 5 | "What will Laura buy in 2033, and does it exist?" (answer: more of the bonds she already holds) | none, once rehearsed |
| 6 | "You say held to maturity. Do you sell anything in 2033?" (buy-only sells only the released part of the reserve) | BOTH, 3r |
| 7 | "Who does this in 2033, and how?" | BOTH |
| 8 | "Why not just make the reserve bigger?" (3r $15k: 0.03%, but the minimum falls to $130k and top-reach to 52%; E3:199, :216) | BOTH and 3r: be ready with this comparison |
| 9 | "Your Nov-39 and Nov-41 notes say reinvested coupons fund part of each payment. Your IPS says nothing depends on reinvestment after 2033. Which is it?" | BOTH |
| 10 | "Does any of this change the range Laura gives co-sponsors?" (no) | none |
| 11 | "Your stocks only set the gift's upside, yet they back the payments?" | option 1 (10b) most; every option's chain, slightly |
| 12 | "Who built the model, and can you reproduce it?" (AI policy: Works Cited; students must be able to explain it) | BOTH most (an LP), then 3r |

---

## 9. Recommendation framework (AI opinion; the team decides)

| If the team's top priority is... | AI pick | Condition |
|---|---|---|
| Fewest IPS words and the simplest story judges can follow | **3r top fix alone** | State its principle (about 30 words) and the honest residual in the Final Report: about 0.6%, worst about $3.3k under parallel moves, worse under twists. Have an answer ready for "why $5k?" |
| The strongest certainty definition, and an explicit answer to "how the reserve's composition changes" (case:95-97; IPS:47-49) | **BOTH, framed minimally** | As 3r, with the release margin replaced by an exact 2033 cash check (+10-20 words). Adopt it only if: (1) a student can do the 2033 check by hand as a running balance and explain the 0%-cash rule; (2) the team quotes "no dependence on future rates after 2033", never "0%"; (3) it decides openly whether to keep a small cushion for fund payout error (5c) |
| No new holdings and no new rules | **Option 1, 10b** | Only if the team accepts VT's second job, re-reads the VT note (Notes:14) and the accepted V5:30, and accepts Laura's flexibility money being locked to 2042. AI view: the weakest for judges |
| — | **Option 1, 10a** | AI view: not a defensible "high degree of certainty" unless the 1-in-7 gap is stated, and then it invites the obvious question |

**AI lean (labelled, weak).** BOTH in the minimal form if the plain-English and hand-check conditions are met by 27 Oct. Otherwise 3r-fix alone. The gap between them is small for Laura (section 6). The choice is about which defence the team can carry in its own words: "why $5k?" or "why 0%?". "Complexity must earn its place" (CLAUDE.md, Team). BOTH earns it only as a replacement rule, never as an extra one.

**Decide in the same vote:**
- the idle-cash-at-0% sizing rule (BOTH depends on it);
- whether the IPS carries the two-stage certainty definition (C4);
- the cushion question (5c);
- D10 first, because it sets option 1's baseline (VP:156).

---

## 10. What this teaches (for Ray)
- **A result that holds by construction can't be evidence.** If a model checks a plan against the same cash flows it bought, it will always pass. Robustness runs only test the parts that can still vary.
- **Margins protect against what you didn't model.** Swapping a guessed margin for an exact calculation fixes the risk you measured and leaves the ones you didn't.
- **Simplicity is about the defence, not the word count.** Each option leaves one question a judge will ask. Pick the one your team can answer best in its own words.

## 11. Limits and UNVERIFIED
- All figures are model output: parallel MC, iBond funds as single bonds, about 4 independent history periods (E3:346-350).
- My attack runs use 20,000 paths × 2 seeds on the lump booking. The fund-haircut sizes are illustrative, and real iBond payout error is UNVERIFIED.
- Not run: BOTH with a kept cushion; a "buy the longest held bond" rule against the LP; BOTH under 10b.
- Word estimates are AI judgement, not counts of any draft.
- Whether Wharton counts headings toward the 500 words is UNVERIFIED (`S/oct20/ipsstruct/ipsstruct.md:363`).

## 12. Reproduce
From `S/oct20/redteam_both/scripts/`:

`S/venv/bin/python -I attack.py 20000 20261019` (and with seed `7`). Outputs go to `../data/attack_N20000_s*.txt` and `.json`, about 3 minutes each on 4 cores.

The only changes from engine_v3 are the two switches. Check them with `diff engine_v3_orig.py engine_v3.py`.
