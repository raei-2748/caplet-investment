# Trading-now brief: read this before the first WInS order

**Every ticker named in this brief is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (listed in the team's WInS
account, and inside the Session Rules position limit; alternates are in the ticket, section 12).

Agent T1 (Trading-Now editor), insight_v1 run, written 2026-09-28 about 01:00 UTC; revised the same day after the T2
red team (`research/insight_v1/wins_now/T2_red_team.md`; see "Changes after T2 red team" at the end). U.S. trading
for the season opens at 9:30 a.m. ET today (13:30 UTC; 11:30 p.m. AEST). **Serves: Trading Notes (TN, due Oct 23)
and, where noted, the IPS (Nov 6). No Final Report work (brief s17).** AI-generated research: decisions to take, evidence and checklists. It is
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
| 1 | Adopt "lock early" (gate box a) | Adopt. Growth-first misses a payment in 3.2% of modelled paths, 13.7% if the 2028 deposit is $75k and 40.8% if it is $0 (`strategy_mc.py`, VRF/ASM). Lock-early never misses **by construction** once the ladder is bought. A full lock is the only design whose certainty rests on market prices on the purchase date, not a forecast (and, in about 1 in 3 modelled rate paths, partly on the 2028 deposit, because the ladder may cost more than $300k in January 2027; AX1b item 1, ASM); partial locks fail in 13-26% of paths if the deposit is missing (D3 M243, ASM) | Before any order |
| 2 | Which book WInS shows: (ii) the mix after both deposits, scaled to $300k, or (iii) the literal January-2027 book (gate box b) | **(ii), medium-low confidence; a close call after T2 added the official hints for (iii).** Both sides are in section 3. Choose (iii) instead if the team cannot state the (ii) scaling in its own words in about 30 IPS words, or if it reads Wharton's "$150,000 will not be added to WInS" as naming the date WInS shows | Before any order |
| 3 | If (ii): growth split 50/50 or 60/40 (world stocks / short Treasuries) | **50/50, low confidence** (downgraded after T2: D6's rule does not separate the two without a fee assumption), decided now. It is a choice of spread, not of median. Both evidence sets are in section 4. If the team cannot agree, buy the recorded provisional 60/40, say "provisional" in the growth note, and name a decision date | Before the VT order |
| 3b | If (ii): floor timing (January 2028 or January 2031) and the growth money's bonds (VGSH or a dated Dec-2032 Treasury fund) (D3 AX1 C6, C18, VRF; T2 finding 5) | Record the team's choice before the VGSH order. If undecided, the VGSH note uses only the "facility contribution and flexibility" need and never refers to a later promised amount. Both questions also go to the IPS list (section 6) | Before the VGSH order |
| 4 | Position-limit branch, including a cap under 25% (gate box e) | Use the pre-set branch table in the ticket (section 3 there). Also pre-decide: **under a cap below 25%, (iii) needs 5-6 Treasury funds, so switch to (ii)**, unless a separate, higher bond limit lets one listed Treasury carry the excess | Before any order |
| 5 | Note format and words (gate boxes c and d) | Test the note-box length **at zero risk before any real note** (ticket gate box c). Until a limit is seen or ruled out, draft every note to **300 characters** or fewer, using the ticket's trim order. The team chooses its own label words (D9's are proposals) and logs the AI source; use the banned-word list (section 2). A second student restates each note's role and checks that no clause repeats ticket wording before it is submitted | Before any order |
| 6 | Optional dated Treasury "rung" (one bond near a payment date) | Under (iii): buy it if the Bonds drop-down lists a suitable bond. Under (ii): optional; skip unless the team wants it (D1 M044, corrected by AX1b) | At the gate session |
| 7 | Data owner for the "tested" evidence | One named student screenshots WInS position values on the fill date and at the Oct 20 close (D7 M002 as corrected by AY2) | Before any order |

**Timing (ASM team rule):** there is no reason to trade at today's open. SMApply says "The competition does not
require frequent or same-day trading" (VP, via `phase_A/wins_week1_guardrails.md`), and WInS gains are not judged (Guide
p.3, VRF). Target fills by **Fri Oct 2 ET** (11:30 p.m. AEST that day), with a hard stop of **Fri Oct 9**. The "first
trade by Oct 10" claim is a 2023-24 rule (SNIP); "required trading activity" is undefined on public pages (VP). Read the
logged-in Trading Details page before the first order. Earlier fills also give the "tested" window more days: about a
52% chance of a 10bp-or-larger rate move by the Oct 20 close for an Oct 2 fill, about 40% at the Oct 9 hard stop (T2
script [4], ASM driftless model). Orders entered while the U.S. market is closed fill at the next open (SMApply Trading
Details, R-W62, VP), so recompute every share count from the last close before entering orders.

## 2. Findings that change what you do in WInS or write in a note this week

1. **Notes are permanent and may be cut at 300 characters.** Notes cannot be edited, only added to (Stock-Trak, VP
   vendor page, not season-specific). A sister Stock-Trak product caps notes at "300 characters" (VP for that product;
   **UNVERIFIED for WInS**, D12; evidence mixed, D12 AY1 C2). Wharton's own example is 413 characters (VRF count),
   which is counter-evidence. *Decision:* test the box length **at zero risk before any real note** (ask Stock-Trak
   Live Chat or Wharton, or type a long test text on the order-review screen and do not press Confirm; ticket gate
   box c). Until a limit is seen or ruled out, draft to 300 characters, and use the ticket's trim order (section 5):
   keep the need (with the (ii) scaling marker), the dated fact and the Guide role word; move the risk/rule and the
   team label to the reflection (D12 AY1 C1). Never finish a cut sentence with an added note (it carries a later
   timestamp, and the note is quoted "exactly as it appears in WInS", TN guide L44, VRF). *Deadline:* the first order.
   - **Conflict resolved (D9 vs D12).** D9 asks for five elements in about 90 words; D12 fits four in 300 characters.
   - Resolution: a four-element core that must fit in 300 characters (role, Laura's dated need, one dated research
     fact, the risk or rule), with a trim order if it does not fit. The ticket (section 5) lists the elements.
   - The trade record already shows the ticker, side and quantity, so the note need not repeat them.
   - Add D9's extra detail only if the box visibly allows it.
2. **Under option (iii) you need a named third trade, or you may have only two executed trades on Oct 23 (AX2
   blocking, D10 C1).** The TN guide needs three notes "from trades your team executed in WInS" ("Yes, we will verify
   this", L42/L53, VRF).
   - With no cap, (iii) is two orders (IEF, TLH).
   - The plan's own rule supplies the third: the 2027 leftover "waits in T-bills". So buy SGOV or BIL as part of the
     same gate plan, so that it reads as implementation, not a note-making trade.
   - **The leftover is real only at trade-date prices (T2 finding 1, blocking for (iii); fixed in ticket section 2).**
     On the trade date, re-price the ladder (A2 script plus about $2.1k for the Nov-15 dates; hand check about
     $294,400 plus $292 per 1bp fall since Sep 25, ASM). Hedge = that cost. T-bill leg = $300,000 minus the cost,
     minus the $1,000 float, minus commissions. **If the leg is under $1,000** (the curve about 12bp or more below
     Sep 25: about an 11% chance by Oct 2 and 19% by Oct 9, ASM), (iii) has no genuine third trade unless a dated rung
     is listed, and the vote reverts to (ii). Never buy a token sliver.
   - **Order of entry under (iii):** IEF and TLH first; the T-bill order only after both show "Filled", sized to the
     cash actually left. The $1,400 float is used up by a 5bp overnight fall (about 1 day in 8, ASM), so entering all
     three orders at once risks the T-bill order being rejected.
   - The SGOV/BIL note gives the leftover as a dollar amount at the trade-date price, never "about 2%".
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
   - "match"/"matched", "mature in her payment years", "stable", "safe", "guaranteed", "risk-free", "operating
     reserve" for WInS funds (S4 finding 2; D9 M062). Three-quarters of TLH's bonds mature after 2042 (VRF, S1
     snapshot).
   - "reduce volatility" for the **promise money** (S4 finding 7; D9 M012). For VGSH, the idea of lower swings in the
     growth money is allowed only with its number beside it, presented as the ordinary effect of holding Treasuries
     in the growth money, not a VGSH property (D12 AY1 C10; T2 finding 14). Wharton's own example note uses the
     phrase (TN guide L36, VRF).
   - "the rule picks 50% under both forecasts" unless the fee assumption is stated (D6 AY1 C1; see section 4).
   - "bought in January 2027" or "fits inside $300,000" stated flatly: the real ladder would cost more than $300k in
     **about 1 in 3** modelled rate paths ("1 in 4" is for the idealised exact-date ladder; AX1b item 1, ASM).
   - **No Laura quotes** in any note or reflection (D13 rule). No "floor-first leap" trait. No statistics-degree hook
     in the notes; spend it at most once, in the IPS (AY2 C6).
5. **One label per job (D9 M001/M062 with AY2 fixes).** The words below are D9's **proposals** ("INT: proposal, the
   team may rename", D9 M001, VRF), not fixed text. The team chooses its own label words once before trade 1, logs
   that the proposals came from an AI source, and never switches between notes.
   | Label | Guide role word |
   |---|---|
   | Promise money (IEF, TLH, SPTL) | future funding (risk management only "measured against the payments") |
   | Growth money (VT) | growth |
   | Short-Treasury part of the growth money (VGSH) | risk management, then liquidity |
   | The 2027 leftover (SGOV/BIL) | liquidity |
6. **"Supported, tested, or refined" is a menu, not a quota (D7, VRF: TN guide L12, L29-30; case L152).**
   - *Tested* lives in a reflection. The window is pre-registered: fill date to the Oct 20 close. Report the rate move
     (bp), the hedge's % change and the payments' % change: exactly three numbers, dated and labelled as the team's
     own calculation (ticket section 6). A move of 10bp or more has about a 52% chance for an Oct 2 fill and about 40%
     for an Oct 9 fill (T2 script [4], ASM). Never use the "83% at some close" figure: that is cherry-picking (AY2 C2).
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
| Trades before Oct 23 | 4 natural orders; survives a single trading session as written (T2 one-session test) | 2, plus the named T-bill leftover (AX2 blocking fix), which exists only if the leftover is at least $1,000 at trade-date prices (about 89% of modelled rate paths for an Oct 2 fill, 81% for Oct 9, ASM) and the T-bill order is entered after the hedge fills (T2 finding 1); a rung only if listed. **Without a listed rung: three trades but two decisions** (IEF and TLH are one duration-weighted decision; TN guide L11 asks for "three investment decisions"; T2 finding 4) |
| Official hints | The Investment Strategy criterion "uses appropriate diversification" (SMApply L49, VRF), and SMApply's own list of diversification kinds includes "funding purposes" (R-W71, VP): only (ii) shows three funding purposes in the WInS holdings (promise, growth, short Treasuries) | WInS cash equals Laura's first deposit, and "The additional $150,000 contribution described in the Client Case Study will not be added to WInS" (R-W56, R-W59, VP). The case: WInS "does not determine Laura's actual portfolio value at the beginning of 2027" (case L130, VRF). Read literally, these support (iii) at least as much as (ii) (S4 finding 5, INT); WInS runs on the eve of the January 2027 purchase |
| What the holdings show on their own | "Her whole plan, in miniature": three jobs side by side (D10 1.4) | "Promise first": the plan's central priority is visible in the holdings themselves, before any growth money exists (D10 1.4) |
| Note roles | Three distinct roles: future funding, growth, risk management/liquidity (D12). This fits the TN guide's first sentence, "approach to growth, risk, liquidity, funding reliability, financial flexibility, and future cash-flow needs" (VRF) | Future funding plus liquidity only; every note is a promise or cash note (D12; D10 C1) |
| Truth at a date | Holds +20.5 points of equity at 60/40 (+17.0 at 50/50) versus Laura's ~0% in January 2027 (D10, AX2 C7) | True at a stated date without scaling (D10) |
| Words needed | Three-element IPS sentence of about 25-40 words: the post-2028 mix; scaled to $300k; in January 2027 almost all of her real $300k buys the ladder. **Plus the stand-in element: WInS holds stand-in funds that move like her payments, not the ladder itself** (D10 1.5, VRF; T2 finding 16a). Plus a short scaling marker folded into each hedge and growth note (AY2 C1; D9 M012). Otherwise the pitch rule "no stock risk until the payments are bought" looks contradicted | About 12-20 IPS words for the date sentence, **including the stand-in element** (D10 1.5). **Plus a T-bill leftover clause (about 8-10 words)**, because the SGOV note relies on the rule "any leftover waits in T-bills until 2028" (T2 finding 16b). The hedge note sizes to the payments' value on the trade-date curve in one clause (D9) |
| Reader risk | A reader may think the team holds about 20% stocks although the payments cost 97% of the first deposit | A reader may see about 98% Treasuries as timid for a client who "has been willing to take thoughtful risks" (case L69-71, VRF). One reflection must answer "why so little equity?" (D13c N1) |
| Leaning | S3 ticket: (ii). D12: a TN reason for (ii) | D10: (iii) at medium-low confidence, "not decision-ready" until C1 was fixed (AX2). S4 finding 5: present the two as equals |

**T1 call, re-checked after the two added rows: still (ii), medium-low confidence, and closer than before (INT).**
- The TN is scored (SMApply; case), but it may not count for semifinal selection: the Rules & Roles page says the
  Top 50 are chosen on the IPS and Final Reports (conflict X-8, `phase_A/case_register.md`). If it does count, (ii)
  gives three distinct roles and three distinct decisions; (iii) without a listed rung gives two decisions.
- (ii) is the only book that shows diversification by funding purpose in the holdings (R-W71), which the Investment
  Strategy criterion names.
- (ii) survives one trading session as written; (iii) needs a trade-date re-price, a two-step order entry and a
  fallback to (ii) in about 1 case in 9 to 1 in 5 (T2 finding 1, ASM).
- The extra IPS words for (ii) (about 15-20 more than (iii), before the (iii) T-bill clause) fit inside AY2's word
  budget, but the IPS page barely fits (AX2 C3), so (iii)'s economy may count for more than the TN if X-8 is read
  strictly.
- A cap below 25% would make (iii) clumsy.
- **Where (iii) wins:** literal truth at a stated date, Wharton's own hint (WInS holds exactly her first deposit, and
  the $150k is never added), "promise first" visible in the holdings, and IPS economy. If the team gives those more
  weight, or finds the scaling hard to explain in its own words, (iii) is fully defensible, with the section 2 item 2
  rules.

## 4. Growth split if (ii): 50/50 vs 60/40 (both evidence sets; the team chooses)

- **For 50/50 (D2, as corrected by AX2; D8/AY2; D3 M034):**
  - The median 2033 facility money barely moves: -$1.5k to +$0.4k.
  - The bad case (p5) improves by $6-7.5k, and the 2031 floor's p5 by $5-6k. The good case (p95) gives up $11-14k.
  - The stock premium over the Treasury rate the curve implies for her dates is small and uncertain: about -1.2 to +2.4
    points a year across sources (AX2 C2).
  - On one input set, stocks at 50-70% add about +$11-14k in the middle but cost about $41-56k at p5 versus
    Treasuries only (ASM).
  - The 50/50 case rests on D2's evidence alone (the four bullets above). D6's rule (hold the most stock that still
    leaves about a 19-in-20 chance that the growth money ends 2033 with at least every dollar Laura put in) does
    **not** pick 50% without a fee assumption. After its audit (D6 AY1 C1, VRF) it gives about 55-70% depending on
    inputs: 60-65% under JPM, 55% under Vanguard's midpoint, 65-70% with fat tails; 50% only if a yearly fee of 0.5%
    or more is assumed (E1 P5 found the same; the case is silent on fees). It is a reason for a choice in the 50-70%
    band and does not separate 50/50 from 60/40 (ASM model outputs).
- **For 60/40 (D6; D13c; D3 M034 with AX1; CLAUDE.md):**
  - It is the team's recorded provisional call.
  - D6's rule (as corrected, D6 AY1 C1) gives 60-65% under JPM with no fee; 60% is inside its 55-70% band.
  - Medians understate what equity is expected to add (D3 AX1 C4, VRF; MODEL): under JPM the **mean** gain of 60%
    growth-money equity over an all-Treasury benchmark is about $6.5-9.4k, against a median of about $3k; under
    Vanguard's midpoint it is about zero. (This compares 60% with 0%; the 50-vs-60 mean difference was not computed.)
  - The whole portfolio already looks cautious (17-20.5% stocks after 2028). A growth share set near the minimum "to
    look safe" should be avoided. The reason for holding stock is the case's "appropriate balance between pursuing
    growth and protecting the capital", plus the stated rule; Laura's career "take the jump" words are a tension the
    plan must answer (why so little equity), never a justification for a higher share (D6 AY1 C3; brief s16).
  - D3: 40-60% are all defensible.
- **T1 call: 50/50, low confidence (downgraded after T2).** The evidence does not separate the two; it is a choice of
  spread. The reason left for 50/50 is D2's: the median is flat across both published houses while the bad case
  (p5) and the 2031 floor's p5 improve, and the growth money feeds a promise made in 2031. It is also simpler to
  explain (stocks are exactly half of the money the promise does not need). 60/40 is equally defensible on the mean
  gain under JPM and as the team's recorded call. Never write that "the rule picks 50% under both forecasts" unless
  the fee assumption is stated.
  - The IPS reason must rest on what does not change (the 2031 promise; a flat median across houses), not on this
    year's valuations (AX2 C7).
  - The Guide's "should not be rewritten simply because markets move" applies after the IPS, so a research-based change
    before Nov 6 is allowed (AX2 C3). Never change it because prices moved.
- Orders (ticket): 50/50 means VT 17.0% (~318 sh) and VGSH 16.0% (~833 sh); 60/40 means VT 20.5% (~384 sh) and VGSH
  12.5% (~651 sh). Band: 45-55 or 55-65, measured as VT ÷ (VT + VGSH + cash float), starting at about 50% or 60%
  (ASM, 9/25 closes; recompute from the last close).

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
- Do not paste AI text into WInS, and do not copy ticket phrases into a note. Running the D9 draft checker counts as AI
  use: log it (AY2 D9 C12).
- Under (iii), do not buy a token T-bill sliver to get a third note: if the trade-date leftover is under $1,000, the
  vote reverts to (ii) unless a dated rung is listed (section 2 item 2).

## 6. Hand-off to the IPS spec: rules to fix before Nov 6 (owner: ips_spec; serves IPS, and TN consistency)
Items raised by T2 and by the audit sections T1 had not applied. Specifications only; the team writes the words.
1. **Floor timing:** is the facility floor bought in January 2028 or January 2031? (D3 AX1 C6, VRF: the barbell is not
   dominated; "no barbell" survives only as a judgement.) Under (ii), settle it before the VGSH order, or keep the VGSH note
   away from any later promised amount (decision 3b).
2. **Growth-money bonds:** short Treasuries (VGSH-type) or a dated Dec-2032 Treasury fund? (D3 AX1 C18, VRF; any fund
   named is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK.)
3. **Date sentence, either option:** it must contain that WInS holds stand-in funds that move like her payments, not
   the ladder itself (D10 1.5, VRF; T2 finding 16a).
4. **(iii) only:** a T-bill leftover clause, about 8-10 words ("any leftover waits in T-bills until 2028" as content,
   D1 M004 rule 7), added to AY2's IPS word budget (`audit_judges_practice_comms.md` s5; T2 finding 16b).
5. **Growth split reason:** state D6's rule only with its fee assumption, or rest the reason on D2's flat median and
   better bad case (D6 AY1 C1; E1 P5). IPS: "about 50%" or "about 60%", never a decimal.
6. **Whole-portfolio stock share by stage** (about 0% in 2027, 17-20% in 2028-30, a few percent after the 2031 floor),
   so a first reader sees where the risk is (D6 AY1 C4 item 8; parked M033; E1 P6).
7. **Pitch/IPS item "the payments are bought in January 2027"** only with its condition: if prices have risen, the
   rest is completed from the 2028 deposit before any growth money (D6 AY1 C4; D8 rule 1). And the second certainty
   gap named in one clause: "certain" is in nominal US$, and a fixed $50,000 buys less each year in Taiwan (D12 AY1 C4;
   brief s16).
8. **2031 range method wording:** the bottom is "the amount already bought", "bought, not forecast", "in US$, barring a
   U.S. Treasury default", never "guaranteed" (D5 AY1 C1, C3; D3 AX1 C3, C14); one top percentile across files (D5 AY1
   C10). Method only; no dollar figures (brief s17).

## Evidence files (all under `research/insight_v1/`)
`wins_now/securities_and_allocation_v0.md`, `wins_now/S4_red_team.md`, `phase_A/wins_week1_guardrails.md`,
`phase_D/D1_rates.md` (+AX1b), `D2_equity_ai.md` (+AX2), `D3_quant.md` (+AX1), `D5_cosponsors.md` (+AY1),
`D6_behavioural.md` (+AY1),
`D7_wharton_intent.md` (+AY2), `D8_practice.md` (+AY2), `D9_communication.md` (+AY2), `D10_compliance.md` (+AX2),
`D12_overflow_client.md` (+AY1), `D13c_voice_map.md`, `audit_markets_rules.md`, `audit_judges_practice_comms.md`,
`phase_C/survivors.json` (tier-1 items M001, M002, M004, M005, M012, M028, M034, M044, M062, M212, M238, M247). Official
files: `competition/official/2026_27/` (TN guide, Guide, case, IPS guide). New script:
`scripts/T1_ticket_v1_numbers.py` (fund facts re-read 2026-09-28 on ishares.com, ssga.com, investor.vanguard.com).
Notes on gaps (corrected after T2 finding 2): the first version said D5, D6, D12 and D3 had no appended audit
section and that `phase_D/audit_rates_D1.md` was not in the repo. That was wrong for all but D3: file times show the AY1
sections on D5, D6 and D12 and `audit_rates_D1.md` saved at 00:34-00:37 UTC, 11-14 minutes before T1's files (00:48).
Only D3's AX1 section (about 01:00) came later. The AX1b section appended to D1 (24 items) is the digest of
`audit_rates_D1.md`, so D1's corrections were applied. After T2, T1 re-read D5 AY1, D6 AY1, D12 AY1 and D3 AX1; what
changed is listed in "Changes after T2 red team" below. Added evidence files: `audit_client_cosponsors.md`,
`audit_rates_D1.md`, `audit_rates_quant.md`, `phase_E/E1_change_proposals.md` (P5, P6; written after T1, not yet
audited), `wins_now/T2_red_team.md`, `scripts/T2_red_team_checks.py`.

## Changes after T2 red team (2026-09-28)
T2 found 1 blocking, 7 important and 12 minor issues in this brief and the ticket. All blocking and important ones are
fixed; the minor ones are fixed where they touch this file. The ticket has its own list.

| T2 # | Severity | What changed in this brief |
|---|---|---|
| 1 | blocking (iii) | Section 2 item 2: the (iii) leftover is re-priced on the trade date; T-bill leg formula; "under $1,000 = no genuine third trade unless a rung is listed, revert to (ii)"; IEF and TLH first, T-bill only after both fill; dollar leftover in the note. Timing: recompute share counts from the last close. Section 5: no token sliver |
| 2 | important | Section 4: D6's rule restated as 55-70% (50% only with a 0.5%+ fee); the 50/50 case rests on D2 alone; D3 AX1 C4 (mean vs median) added to the 60/40 side; T1's 50/50 lean downgraded to low confidence; "Notes on gaps" corrected |
| 3 | important | Section 3: rows "Official hints" and "What the holdings show on their own"; the TN-first reason re-worded around X-8; lean re-checked (still (ii), medium-low, closer) |
| 4 | important | Section 3, (iii) "Trades before Oct 23": three trades but two decisions without a rung |
| 5 | important | Decision 3b (floor timing, growth-money bonds before the VGSH order); section 6 items 1-2 |
| 6 | important | Decision 5 and section 2 item 1: zero-risk length test before any real note; trim order |
| 7 | important | Section 2 item 6: a tested reflection carries exactly three numbers (details in ticket section 6) |
| 8 | important | Decision 5 and section 2 item 5: labels are D9's proposals; the team picks its own words, logs the AI source; second-student check against ticket wording |
| 10 | minor | Availability label line under the title |
| 12 | minor | Section 4: band denominator |
| 14 | minor | Section 2 item 4: "reduce volatility" banned for the promise money only |
| 15 | minor | Decision 1: "market prices on the purchase date ... partly on the 2028 deposit in about 1 in 3 paths" |
| 16a-b | minor | Section 3 "Words needed" (stand-in element, (iii) T-bill clause); section 6 items 3-4 |
| 18 | minor | Timing paragraph and section 2 item 6: 52% (Oct 2 fill) vs 40% (Oct 9) |
| 20 | minor | "Notes on gaps" corrected; fill-at-next-open cited to Trading Details (R-W62) |
| 9, 11, 13, 16c, 17, 19 | minor | Ticket only |

What else changed after re-reading the audits T1 had missed (beyond T2's list):
- D6 AY1 C3: Laura's "take the jump" words removed as a reason for a higher stock share (section 4); they are a
  tension to answer.
- D6 AY1 C4, D12 AY1 C4, D5 AY1 C1/C3/C10, D3 AX1 C3/C14: IPS items handed off in section 6 (items 6-8).
- D6 AY1 C2: already consistent (under (ii) the promise note gives rate sensitivity and the scaling, not ~$292k; the
  dollar cost is (iii)-only or reflection material).
- D12 AY1 C3: already addressed by the named T-bill trade, now with T2's re-price rule.
- D3 AX1 C8 ("about 1 in 3"; the ladder cost more than $300k on almost every day of 2026): already used; unchanged.

## What this teaches
A decision made at the moment of action is judged by what you knew and wrote then, so read the corrections, not
just the conclusions: one stale sentence about a rule tilted a vote here, and the audit that fixed it was already in
the repo. This week that means three
things. Settle the few choices that make notes permanent before you trade: which book, which split, which words. Plan
your evidence in advance, and let the market supply the test instead of inventing a trade. Say plainly what your
holdings are not: stand-ins, not the ladder itself.
