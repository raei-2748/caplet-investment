# Trading-now brief: read this before the first WInS order

Agent T1 (Trading-Now editor), insight_v1 run, written 2026-09-28 about 01:00 UTC. U.S. trading for the season opens at
9:30 a.m. ET today (13:30 UTC; 11:30 p.m. AEST). **Serves: Trading Notes (TN, due Oct 23) and, where noted, the IPS
(Nov 6). No Final Report work (brief s17).** AI-generated research: decisions to take, evidence and checklists. It is
not text to submit; the six students decide and write every note, reflection and IPS sentence (Wharton AI policy).
The orders themselves are in `research/insight_v1/wins_now/securities_and_allocation_v1.md` (the ticket). No relayed
user messages arrived during this task. T1 did not commit anything.

Labels: **VP** verified on the primary page; **VRF** verified in a repo file; **SNIP** snippet or secondary, unverified;
**ASM** assumption or model output (not a forecast); **INT** our interpretation (a judgement, not a fact). A file name
means "see that file", with the label it carries there. Where a specialist file ends with "Audit corrections", the
corrections are applied here.

---

## 1. Decisions to take before the first order (all team votes; record first names, date and reason in the log)

| # | Decision | Recommendation (T1) | Must be decided by |
|---|---|---|---|
| 1 | Adopt "lock early" (gate box a) | Adopt. Growth-first misses a payment in 3.2% of modelled paths, 13.7% if the 2028 deposit is $75k and 40.8% if it is $0 (`strategy_mc.py`, VRF/ASM). Lock-early never misses **by construction** once the ladder is bought. A full lock is the only design whose certainty rests on today's prices, not a forecast; partial locks fail in 13-26% of paths if the deposit is missing (D3 M243, ASM) | Before any order |
| 2 | Which book WInS shows: (ii) the mix after both deposits, scaled to $300k, or (iii) the literal January-2027 book (gate box b) | **(ii), medium-low confidence.** Both sides are in section 3. Choose (iii) instead if the team cannot state the (ii) scaling in its own words in about 30 IPS words | Before any order |
| 3 | If (ii): growth split 50/50 or 60/40 (world stocks / short Treasuries) | **50/50, medium-low confidence**, decided now. Both evidence sets are in section 4. If the team cannot agree, buy the recorded provisional 60/40, say "provisional" in the growth note, and name a decision date | Before the VT order |
| 4 | Position-limit branch, including a cap under 25% (gate box e) | Use the pre-set branch table in the ticket (section 3 there). Also pre-decide: **under a cap below 25%, (iii) needs 5-6 Treasury funds, so switch to (ii)**, unless a separate, higher bond limit lets one listed Treasury carry the excess | Before any order |
| 5 | Note format and words (gate box d) | Draft every note to **300 characters** or fewer. Use the fixed labels and banned-word list (sections 2 and 5). A second student restates each note's role before it is submitted | Before any order |
| 6 | Optional dated Treasury "rung" (one bond near a payment date) | Under (iii): buy it if the Bonds drop-down lists a suitable bond. Under (ii): optional; skip unless the team wants it (D1 M044, corrected by AX1b) | At the gate session |
| 7 | Data owner for the "tested" evidence | One named student screenshots WInS position values on the fill date and at the Oct 20 close (D7 M002 as corrected by AY2) | Before any order |

**Timing (ASM team rule):** there is no reason to trade at today's open. SMApply says "The competition does not
require frequent or same-day trading" (VP, via `phase_A/wins_week1_guardrails.md`), and WInS gains are not judged (Guide
p.3, VRF). Target fills by **Fri Oct 2 ET** (11:30 p.m. AEST that day), with a hard stop of **Fri Oct 9**. The "first
trade by Oct 10" claim is a 2023-24 rule (SNIP); "required trading activity" is undefined on public pages (VP). Read the
logged-in Trading Details page before the first order. Earlier fills also give the "tested" window more days.

## 2. Findings that change what you do in WInS or write in a note this week

1. **Notes are permanent and may be cut at 300 characters.** Notes cannot be edited, only added to (Stock-Trak, VP
   vendor page, not season-specific). A sister Stock-Trak product caps notes at "300 characters" (VP for that product;
   **UNVERIFIED for WInS**, D12). Wharton's own example is 413 characters (VRF count). *Decision:* draft to 300
   characters. When typing the first note, check the box for a counter before pressing submit, and record what it
   shows. Never finish a cut sentence with an added note (it carries a later timestamp, and the note is quoted "exactly
   as it appears in WInS", TN guide L44, VRF). *Deadline:* the first order.
   - **Conflict resolved (D9 vs D12).** D9 asks for five elements in about 90 words; D12 fits four in 300 characters.
   - Resolution: a four-element core that must fit in 300 characters (role, Laura's dated need, one dated research
     fact, the risk or rule). The ticket (section 5) lists the elements.
   - The trade record already shows the ticker, side and quantity, so the note need not repeat them.
   - Add D9's extra detail only if the box visibly allows it.
2. **Under option (iii) you need a named third trade, or you may have only two executed trades on Oct 23 (AX2
   blocking, D10 C1).** The TN guide needs three notes "from trades your team executed in WInS" ("Yes, we will verify
   this", L42/L53, VRF).
   - With no cap, (iii) is two orders (IEF, TLH).
   - The plan's own rule supplies the third: the ~2% 2027 leftover "waits in T-bills". So buy SGOV or BIL (about
     $4,500) **in the same session** as the hedge, so that it reads as implementation, not a note-making trade.
   - Honest cost: it earns about $18 in the WInS window against a $25 commission (ASM, T1 script [5]). It is justified
     by the plan (about $220 over the real one-year wait), never by WInS profit.
   - *Deadline:* the gate vote.
3. **Decide the book with both sides visible (section 3).** No official rule picks a date (D10 M005, VRF). The frozen
   Nov-6 portfolio must "reflect the strategy established in your IPS" (IPS guide L75, VRF). So the IPS names the date
   WInS shows under either choice. The "middle path" is dropped: a ~1% VT sliver adds a weak note and reverses the
   T-bill rule (D10).
4. **Words that must never appear in a note (audit corrections AX2 and AY2).**
   - "known" or "locked" for the ~5.2% the curve implies for 2028-33. It is market-implied, not lockable, and forwards
     are derivatives (D2 C1).
   - "halves AI exposure": top-10 concentration falls about 44%, and VT holds Asian chip makers outside its top ten
     (D2 C5).
   - "half = the promise", "the 2031 floor", "already owned" or "the amount she can promise co-sponsors" for VGSH
     (D2 C6; D9 AY2 C1).
   - "match"/"matched", "mature in her payment years", "stable", "reduce volatility", "safe", "guaranteed",
     "risk-free", "operating reserve" for WInS funds (S4 finding 2; D9 M062). Three-quarters of TLH's bonds mature
     after 2042 (VRF, S1 snapshot).
   - "bought in January 2027" or "fits inside $300,000" stated flatly: the real ladder would cost more than $300k in
     **about 1 in 3** modelled rate paths ("1 in 4" is for the idealised exact-date ladder; AX1b item 1, ASM).
   - **No Laura quotes** in any note or reflection (D13 rule). No "floor-first leap" trait. No statistics-degree hook
     in the notes; spend it at most once, in the IPS (AY2 C6).
5. **Fixed labels, one per job (D9 M001/M062 with AY2 fixes).** Decide these once before trade 1 and never switch.
   | Label | Guide role word |
   |---|---|
   | Promise money (IEF, TLH, SPTL) | future funding (risk management only "measured against the payments") |
   | Growth money (VT) | growth |
   | Short-Treasury part of the growth money (VGSH) | risk management, then liquidity |
   | The 2027 leftover (SGOV/BIL) | liquidity |
6. **"Supported, tested, or refined" is a menu, not a quota (D7, VRF: TN guide L12, L29-30; case L152).**
   - *Tested* lives in a reflection. The window is pre-registered: fill date to the Oct 20 close. Report the rate move
     (bp), the hedge's % change and the payments' % change. A move of 10bp or more has about a 53% chance (ASM). Never
     use the "83% at some close" figure: that is cherry-picking (AY2 C2).
   - *Refined* is honest only as a pre-announced split decision under (ii), or an order rejected by a limit nobody
     could see beforehand. The pre-planned SPTL split is **not** a refinement (AY2 C1).
   - Drop the blueprint's planned "discipline/rebalance trade". No sensible band fires before Oct 23 (about 0-2% even
     in a crisis, ASM). Never stage a trade.
7. **Data capture (AY2 C5).** Only the WInS screenshots must be taken on the day: position values on the fill date and
   at the Oct 20 close. Treasury curves can be pulled later from the treasury.gov yearly CSV.
   - Value the payments with `D3_funded_status_log.py`, `A2_curve_recheck.py` or `D9_numbers.py [3]`, **not**
     `official_curve_pv.py` (fixed to 2026-09-25).
   - IEF and TLH pay monthly distributions (about 0.4%), so compare total returns or note the ex-dates.
8. **Position limit unknown; read both lines in Session Rules (A4, VP).** The 2026-27 User Guide defines the limit per
   "single stock"; a 2024 screenshot showed a separate bond limit of 100% [PRIOR]. The Stock-Trak default is 25% (VP,
   generic).
   - Lower caps hurt (iii) far more than (ii). At 25%, (iii) needs 5 Treasury funds and (ii) needs 3. At 20%, (iii)
     needs 6 and (ii) needs 4 plus a VTI/VXUS split if VT is at 20.5%. At 15%, (iii) is not feasible with the listed
     funds (T1 script [3]).
   - Every capped mix stays at about 10-10.6 years (issuer numbers), with a worst twist error of 0.5-1.1% of the hedge
     (ASM, S4's forward-consistent method). A "twist" is short and long rates moving in opposite directions.

## 3. Book (ii) vs (iii): both sides and T1's call (the team chooses, gate box b)

| | (ii) the mix after both deposits, scaled | (iii) the literal January-2027 book |
|---|---|---|
| Rules | Complies under no cap, 35% and 25% caps (D10; AX2 C2: Vanguard volumes and caps below 25% are unchecked) | Same |
| Trades before Oct 23 | 4 natural orders | 2, plus the named T-bill leftover (AX2 blocking fix); a rung only if listed |
| Note roles | Three distinct roles: future funding, growth, risk management/liquidity (D12). This fits the TN guide's first sentence, "approach to growth, risk, liquidity, funding reliability, financial flexibility, and future cash-flow needs" (VRF) | Future funding plus liquidity only; every note is a promise or cash note (D12; D10 C1) |
| Truth at a date | Holds +20.5 points of equity at 60/40 (+17.0 at 50/50) versus Laura's ~0% in January 2027 (D10, AX2 C7) | True at a stated date without scaling (D10) |
| Words needed | Three-element IPS sentence of about 25-40 words: the post-2028 mix; scaled to $300k; in January 2027 almost all of her real $300k buys the ladder. Plus a short scaling marker folded into each hedge and growth note (AY2 C1; D9 M012). Otherwise the pitch rule "no stock risk until the payments are bought" looks contradicted | About 12-20 IPS words; the hedge note sizes to the ~$292-294k promise in one clause (D9) |
| Reader risk | A reader may think the team holds about 20% stocks although the payments cost 97% of the first deposit | A reader may see about 98% Treasuries as timid for a client who "has been willing to take thoughtful risks" (case L69-71, VRF). One reflection must answer "why so little equity?" (D13c N1) |
| Leaning | S3 ticket: (ii). D12: a TN reason for (ii) | D10: (iii) at medium-low confidence, "not decision-ready" until C1 was fixed (AX2) |

**T1 call: (ii), medium-low confidence (INT).**
- The first judged deliverable is the Trading Notes. Under (ii), three notes can show three different jobs and a
  growth decision; under (iii) they cannot.
- The extra IPS words for (ii) (about 15-20 more than (iii)) fit inside AY2's word budget.
- A cap below 25% would make (iii) clumsy.
- **Where (iii) wins:** literal truth and IPS economy. If the team prefers those, or finds the scaling hard to explain in
  its own words, (iii) is fully defensible. With the T-bill trade (and a rung if listed) it can still give three notes.

## 4. Growth split if (ii): 50/50 vs 60/40 (both evidence sets; the team chooses)

- **For 50/50 (D2, as corrected by AX2; D8/AY2; D3 M034):**
  - The median 2033 facility money barely moves: -$1.5k to +$0.4k.
  - The bad case (p5) improves by $6-7.5k, and the 2031 floor's p5 by $5-6k. The good case (p95) gives up $11-14k.
  - The stock premium over the Treasury rate the curve implies for her dates is small and uncertain: about -1.2 to +2.4
    points a year across sources (AX2 C2).
  - On one input set, stocks at 50-70% add about +$11-14k in the middle but cost about $41-56k at p5 versus
    Treasuries only (ASM).
  - D6's own rule (hold the most stock that still leaves about a 19-in-20 chance that the growth money ends 2033 with
    at least every dollar Laura put in) picks 60% under JPM and 50% under Vanguard's midpoint. Applied under both
    published forecasts, it picks 50% (INT synthesis; D6, ASM).
- **For 60/40 (D6; D13c; D3 M034; CLAUDE.md):**
  - It is the team's recorded provisional call.
  - D6's rule picks 60% under JPM, and 60% is at the edge under Vanguard (5.4% versus a 5% threshold, ASM).
  - The plan already looks cautious for someone whose risk words are about taking the jump (D13c N1; AY2 C5). A
    growth share set near the minimum "to look safe" should be avoided.
  - D3: 40-60% are all defensible.
- **T1 call: 50/50, medium-low confidence.** It holds under both published houses. It is simpler to explain (stocks are
  exactly half of the money the promise does not need). It protects the bad case that feeds the 2031 promise.
  - The IPS reason must rest on what does not change (the 2031 promise; a flat median across houses), not on this
    year's valuations (AX2 C7).
  - The Guide's "should not be rewritten simply because markets move" applies after the IPS, so a research-based change
    before Nov 6 is allowed (AX2 C3). Never change it because prices moved.
- Orders (ticket): 50/50 means VT 17.0% (~318 sh) and VGSH 16.0% (~833 sh); 60/40 means VT 20.5% (~384 sh) and VGSH
  12.5% (~651 sh). Band: 45-55 or 55-65 (ASM, 9/25 closes).

## 5. What NOT to do this week
- Do not place any order before all five gate boxes are ticked. Do not trade because the season "opened".
- Do not let the advisor place trades or appear as a decider in a note ("Students should place trades on WInS, NOT the
  advisor", VP; advisors "may not make decisions", VP).
- Do not buy anything outside cash, $5+ stocks, ETFs and government bonds listed in WInS. No leveraged, inverse,
  crypto-linked or thematic funds, no ETNs, and no Taiwan or AI tilt (A4; D8 M081; D13c R3).
- Do not day-trade, and do not "fix" an error by selling the same day ("run with it", SMApply FAQ, VP).
- Do not sell the promise money after a rate rise, trim it after a fall, or move money between promise money and growth
  money.
- Do not put a reserve size, facility amount, co-sponsor range or 2031 floor share in any note. They are not expected
  now (TN guide L20-22, VRF), and permanent notes would bind the IPS.
- Do not paste AI text into WInS. Running the D9 draft checker counts as AI use: log it (AY2 D9 C12).

## Evidence files (all under `research/insight_v1/`)
`wins_now/securities_and_allocation_v0.md`, `wins_now/S4_red_team.md`, `phase_A/wins_week1_guardrails.md`,
`phase_D/D1_rates.md` (+AX1b), `D2_equity_ai.md` (+AX2), `D3_quant.md`, `D5_cosponsors.md`, `D6_behavioural.md`,
`D7_wharton_intent.md` (+AY2), `D8_practice.md` (+AY2), `D9_communication.md` (+AY2), `D10_compliance.md` (+AX2),
`D12_overflow_client.md`, `D13c_voice_map.md`, `audit_markets_rules.md`, `audit_judges_practice_comms.md`,
`phase_C/survivors.json` (tier-1 items M001, M002, M004, M005, M012, M028, M034, M044, M062, M212, M238, M247). Official
files: `competition/official/2026_27/` (TN guide, Guide, case, IPS guide). New script:
`scripts/T1_ticket_v1_numbers.py` (fund facts re-read 2026-09-28 on ishares.com, ssga.com, investor.vanguard.com).
Notes on gaps: D5, D6, D12 and D3 had no appended audit section when this was written. D1's audit points to
`phase_D/audit_rates_D1.md`, which was not in the repo, so T1 used the AX1b corrections appended to D1 itself.

## What this teaches
A decision made at the moment of action is judged by what you knew and wrote then. This week that means three
things. Settle the few choices that make notes permanent before you trade: which book, which split, which words. Plan
your evidence in advance, and let the market supply the test instead of inventing a trade. Say plainly what your
holdings are not: stand-ins, not the ladder itself.
