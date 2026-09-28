# Trading Notes pack: trades, gates, note elements and checks (insight_v1, writer W1)

**Summary (5 lines)**
1. Before any order: three recorded team votes (lock-early; REC or ALT; WInS book (ii)R), each after every student writes 3-5 own-words lines, then the Session Rules screenshot, listing checks and a zero-risk note-box test (E6 s5.4, INT).
2. Recommended book (ii)R at $300,000: IEF + TLH (the operations hedge, about 66%), the building minimum (2032 Treasury note, else IBTM, else VGIT/SPTI, about 24%), VT (about 9%), cash float about 1%; all orders in one session, hedge first (E6 s5.2, INT).
3. The three notes are TLH (supported and tested), the building minimum (refined only if the change was logged before its order, else supported) and VT (supported, carrying the growth-first story) (E6 s5.5, INT).
4. Students draft every note offline from element lists (300 characters until the box test), a second student copy-checks, and two outside readers test the drafts; reflections are student-written without AI (E6 s5.4, s5.7).
5. Submit on Thu Oct 22 AEDT; the deadline is Fri Oct 23, 5:00 p.m. ET = Sat Oct 24, 08:00 AEDT (TN guide; E6 s7).

**Serves: Trading Notes (TN).** Nothing here is note or reflection text. It is AI-generated research (Wharton AI policy: log it; students write every word). Authority: `research/insight_v1/phase_E/E6_final_spec.md` (sections 0, 2, 5, 7-9); details copied from `wins_now/securities_and_allocation_v1.md` ("ticket v1") and `phase_D/trading_now_brief.md` only where E6 points to them. **Status: PROVISIONAL until the team votes.**

**Status labels:** VP = verified on the primary page (by the named agent and date); VRF = verified in an official repo file; SNIP = snippet, unverified; ASM = assumption; MODEL = model output, never a forecast; DER = W1's arithmetic from labelled inputs; INT = judgement; UNVERIFIED = not yet checked.

**Terms (first use):**

| Term | Meaning |
|---|---|
| ETF | Exchange-traded fund: a fund bought and sold like a share |
| Treasury | A bond issued by the U.S. government |
| STRIPS / zero-coupon | A Treasury that pays one amount on one date and nothing before |
| Rung | One bond in a ladder, maturing before one payment |
| Operations hedge | IEF + TLH in WInS: funds that stand in for the ten-payment ladder |
| Building minimum | The Treasury bought with the 2028 deposit that repays its full dollar amount before 2033 |
| Stock fund | One broad world stock fund holding everything else |
| Duration | Rate sensitivity: about the % a bond fund falls if rates rise 1 percentage point |
| bp | Basis point: 0.01 percentage point |
| Position limit (cap) | The most WInS lets one security be of the portfolio (shown in Session Rules) |
| Scaling marker | The few words inside a note that say WInS shows Laura's plan "after both deposits" / "after her 2028 deposit" |
| Day trading | Buying and selling the same security on one U.S. trading day (not permitted, User Guide, VP via A4) |
| Ex-dividend date | The day a fund's price drops by the distribution it is about to pay |
| REC / ALT | E6's recommended design (minimum bought in 2028) / the alternative (E1's 2031 lock) |

---

## 1. Gate: tick every box before the first order (E6 s5.4; E5 calendar)

| # | Check | Owner (role) | Done |
|---|---|---|---|
| a1 | Every student writes 3-5 lines in their own words, no AI file open (R-W51; PM-01) | each student | [ ] |
| a2 | Vote 1: adopt lock-early, recorded with first names, date, reason (E6 D1) | team leader | [ ] |
| a3 | Vote 2: REC or ALT, using E6 s7 D2 test (values statement + two-minute explain-back of the four dates), recorded **before any building or stock order** (this dated entry is what makes a "refined" note B possible) | team leader | [ ] |
| a4 | Vote 3: WInS book (ii)R or (iii) (E6 D3); the two-reader check (row e3) is its tie-breaker | team leader | [ ] |
| b1 | Session Rules screenshot (Portfolio Summary > Session Rules): single-security limit, any bond or type limit, day-trading tooltip, trades allowed, commissions | trader | [ ] |
| b2 | Read the logged-in Trading Details page. Activity minimum or whole-type cap shown: **stop, ask Wharton (Contact Us); never add trades to meet a count** (PM-15). "First trade by Oct 10" stays UNVERIFIED until read | trader | [ ] |
| b3 | Pick the position-limit branch (section 3) before ordering | trader + rates analyst | [ ] |
| c1 | Search IEF, TLH, VT, IBTM, SPTL, VGIT: each shows as an ETF with the issuer's full name | trader | [ ] |
| c2 | Bonds drop-down: every U.S. Treasury maturing Jul-Dec 2032 (coupon, price, accrued interest); search by maturity, not a built-up symbol (AX1b item 10) | trader | [ ] |
| d1 | Note-box test at zero risk: type about 450 characters on the order-review screen, see if they are cut, clear them, **do not press Confirm**; record the result. Until a limit is seen or ruled out, draft to 300 characters (UNVERIFIED for WInS; a sister product caps at 300, VP; Wharton's own example is 413 characters, VRF) | trader | [ ] |
| e1 | Notes drafted offline by students from section 6, no research file open (PM-04) | note writers | [ ] |
| e2 | Second student restates each note's role in one sentence, then runs the five-word copy check (section 8) | second reader | [ ] |
| e3 | Two outside readers pass the "what does Laura's real money hold in January 2027?" check (section 8) | second reader | [ ] |
| f1 | Roles: one trader + backup (only they place orders); note writers; second reader; log keeper; data owner; every student drafts at least one note or reflection and one IPS block (PM-05; R-W38, VP) | team leader | [ ] |
| g1 | Cash: at least $1,000 left at the next open's prices; share counts recomputed from the last close (T2 finding 1); no sells on a day anything is bought | trader | [ ] |
| h1 | Team names its own labels for the three parts in a meeting; logs that the proposals came from an AI source (E2 F10; T2 finding 8) | log keeper | [ ] |
| i1 | Decision log and AI-use log started (section 9) | log keeper | [ ] |

Never: an order before the gate; the advisor placing a trade ("Students should place trades on WInS, NOT the advisor", VP via E6 s5.9).

---

## 2. Orders

All dollar figures: illustration at the 2026-09-25 closes (VP via ticket v1 s12; SPTL/SPTI as of 9/24), $300,000 WInS cash (VP via brief s14). Shares rounded down (DER). **Recompute every share count from the last close before entering orders** (T2 finding 1). Orders placed while the market is closed fill at the next open (R-W62, VP). Commissions: $25 per ETF trade, $10 per bond trade (VP via brief s14).

### 2.1 Recommended book (ii)R: Laura's plan on 2 January 2028, scaled to $300,000 (E6 s5.1-5.2, INT)

| Entry order | Holding | Weight | $ at $300k | ~Shares | Job / Guide role word | Primary, then alternates | Status | 2025-26 list (history only, VRF) |
|---|---|---|---|---|---|---|---|---|
| 1 | IEF (7-10y Treasuries) | 23.5% | $70,500 | ~783 | Operations: future funding | IEF; VGIT, then SPTI | PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK | IEF yes; VGIT no; SPTI no |
| 1 | TLH (10-20y Treasuries) | 42.5% | $127,500 | ~1,365 | Operations: future funding (one duration-weighted decision with IEF) | TLH; if missing, IEF 40.9% + TLT 25.1% | PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK | TLH no; TLT yes |
| 2 | Building minimum: 4.125% Treasury note 15-Nov-2032 (CUSIP 91282CFV8, VP per S1 via D1), else IBTM | 24.3% | $72,900 | note ≈ $75k face (≈ $72,570 at the model price 95.27 + 1.49 accrued, ASM); IBTM ~3,336 | Building minimum: "risk management" or "future funding" (pick one word, record it) | 1) 2032 note ($10); 2) IBTM ($25); 3) VGIT (~1,281), then SPTI (~2,669), noted as "moves like, not dated" | PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK | IBTM no; VGIT no |
| 3 | VT (world stocks) | 8.7% | $26,100 | ~163 | Stock fund: growth | VT; VTI + VXUS (62/38: ~$16,180 / ~$9,920, ~42 / ~114 sh, DER); then ITOT + IXUS | PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK | VT, VTI, VXUS yes; ITOT, IXUS not found (W1 grep of `competition/historical/2025_26/`, 2026-09-28) |
| - | Cash float | ~1% | ~$3,090 before, ~$2,990 after 4 × $25 (IBTM route, DER) | - | Liquidity | Keep at least $1,000 | - | - |

- Hedge mix IEF 35.6% / TLH 64.4% of the hedge gives "about 10 years" of rate sensitivity, like the payments' (issuer durations IEF 6.86y, TLH 11.58y on 9/25, VP via ticket v1; 9.90y liability, VRF). Formula: IEF share of hedge = (D_TLH − 9.90) / (D_TLH − D_IEF); re-read durations on the trade day (ticket v1 s10).
- Weights trace to the plan on 2 Jan 2028: ladder 65.9%, minimum 25.3%, stock fund 8.7% of about $464k (MODEL, E6 [7]); the 1% float comes out of the minimum's share (25.3 − 1.0 = 24.3, DER).
- Entry: IEF and TLH first, then the minimum, then VT, **all in one session**, so the time stamps show promise-first (D7, INT). Target fills by Fri Oct 2 ET; hard stop Fri Oct 9 ET (ASM team rule).
- Volume rule (no trade above 2× daily volume, VP): every order is tiny against volume (IBTM ~3,336 vs ~216k/day; TLH ~1,365 vs ~1.97m/day; VP via ticket v1/E4). Read Vanguard volumes in WInS.

### 2.2 Fallbacks (decided in advance; E6 s5.10)

| Trigger | Book | Orders at $300k (illustration, DER) | Notes change |
|---|---|---|---|
| No dated 2032 instrument listed (no Jul-Dec 2032 note, no IBTM) | (ii)R with a stand-in | IEF $70,500 / TLH $127,500 / VGIT $72,900 (~1,281; else SPTI ~2,669; about 4.8-4.9y) / VT $26,100 / float | Note B says it moves like a Treasury maturing in late 2032; never claims a date. Real plan unchanged |
| Two-reader check fails twice after redrafting | (iii): Laura's literal January-2027 book | Re-price the ladder on the trade date (`A2_curve_recheck.py` + about $2.1k for Nov-15 dates; hand check about $294,400 + $292 per 1bp fall since Sep 25, ASM). Sep-25 illustration: IEF 34.9% $104,700 (~1,163) / TLH 63.1% $189,300 (~2,027); then, **only after both show Filled**, SGOV (else BIL, then SHV) with the leftover if ≥ $1,000 (~$4,500, ~45 SGOV); cash ~$1,400 after 3 × $25. Leftover under $1,000: a listed dated payment rung; otherwise revert to (ii)R. Never a token sliver | One reflection answers "why so little stock" with forced-versus-chosen content. Without a rung, IEF and TLH are one decision: accept that in the vote and log it, or choose (ii)R (T2 finding 4) |
| Team votes ALT | Ticket v1 (ii) at 50/50 | IEF 23.5% $70,500 / TLH 42.5% $127,500 / VT 17.0% $51,000 (~318) / VGSH 16.0% $48,000 (~833) / cash ~1% (~$3,100 after 4 × $25, DER) | Note C becomes the VGSH note: never "the floor" or "already owned". Record the growth-money bond choice (short or dated, AX1 C18) before the VGSH order |

Every ticker in this table is **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (SGOV, BIL, SHV, VGSH, VGIT, SPTI included).

---

## 3. Position-limit branches (read both Session Rules lines first; E6 s5.3, ticket v1 s3)

| Single-security limit shown | Book (ii)R |
|---|---|
| None, or 43% or more | As in 2.1 |
| 25-42% | IEF 23.5 / TLH at the cap minus 1 / SPTL the rest of the hedge. Minimum held one point under the cap if the cap is under 25.3%. **At 25%:** IEF 23.5 / TLH 24 / SPTL 18.5 / IBTM 24 / VT 8.7 / cash about 1.3%; at $300k: $70,500 / $72,000 (~771) / $55,500 (~2,286) / $72,000 (~3,295) / $26,100 (~163) / ~$3,850 after 5 × $25 (E6 [7]; $ and shares DER) |
| Under 25% | Hedge per ticket v1 s3: IEF, TLH, SPTL at the cap minus 1; VGIT, then VGLT, take the rest (at a 20% cap: IEF 19 / TLH 19 / SPTL 19 / VGIT 9, about 9.9y, ticket v1). Minimum: IBTM at the cap minus 1, the rest in VGIT. VGIT bought for both jobs counts as one holding against the cap: add the two before ordering (at 20%: 9 + 5.3 = 14.3%, DER). **If 5 or more hedge funds would be needed (a cap of about 17% or less), stop and ask Wharton (Contact Us) before trading** |
| A separate, higher bond limit is shown | The 2032 note may carry the whole minimum |
| IEF not listed | VGIT (else SPTI) re-solved: VGIT 16.6 / TLH 49.4 (SPTI 16.3 / 49.7); TLH rises, so re-check the cap row (ticket v1 s12, DER) |

- Never add to a holding within one point of the cap. A 20-24% stock fall, or a 10-12% fall with a 50bp rally, can lift TLH above a 25% cap (T2 [5]; ASM that WInS re-checks the limit).
- A pre-chosen branch (for example the SPTL split) is **not** a "refined" decision (AY2 D7 C1). An order rejected by a limit nobody could see is a genuine rule-driven trade.
- SPTL's alternate is VGLT. Describe every branch as "about 10 years"; never two decimals. Every ticker in this section is **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK**.

---

## 4. Trading calendar (ET for markets; AEST/AEDT for the team; NSW/Victoria; E6 s7, E5, ticket v1 s9)

| When | What | Owner |
|---|---|---|
| Tue Sep 29 AEST | Roles; trader + backup; AI-use log started; no-contact rule written down | team leader; log keeper |
| Wed Sep 30 AEST | Own-words lines for the votes; exam/travel calendar | all |
| Thu Oct 1 AEST | Gate (section 1): votes, Session Rules, listings, box test, labels, drafts copy-checked, two-reader check | trader; second reader; team leader |
| Fri Oct 2 ET (U.S. open 9:30 a.m. = 11:30 p.m. AEST Fri) | **Target fills**, one session. Screenshot every position (starts the tested window). Jobs report (SNIP date): check only, never trade | trader; data owner |
| Fri Oct 2 AEST | Repo-visibility decision (E6 D11) | team leader |
| Sun Oct 4 | Daylight saving starts: U.S. open = 12:30 a.m. AEDT next day. AI-use log backfilled | log keeper |
| Wed Oct 7 AEDT | Submit the roster (due Sat Oct 10, 08:00 AEDT) | team leader |
| Fri Oct 9 ET | **Hard stop for fills** (ASM team rule) | trader |
| Wed Oct 14 ET | CPI release (SNIP date): check only | - |
| Oct 19-23 | Duration check (trade only if the hedge drifts more than 0.25 years from its start, another day from any buy); choose the three notes | rates analyst |
| Tue Oct 20 close = Wed Oct 21, 07:00 AEDT | **End of the tested window**: screenshot every position | data owner |
| Oct 21-22 AEDT | Reflections written by students, without AI | note writers |
| Thu Oct 22 AEDT | Consistency table, word counts, number check; **TN submitted** | log keeper; team leader |
| **Fri Oct 23, 5:00 p.m. ET = Sat Oct 24, 08:00 AEDT** | TN deadline, no extensions (VRF) | - |
| Oct 27-28 | FOMC meeting (VP via ticket v1), after the TN deadline | - |
| Tue Nov 3 AEDT | IPS words frozen; no "tidy-up" trades after this | all |
| Fri Nov 6 ET | Trading ends, portfolio freezes (Sat Nov 7 AEDT) | - |

Brisbane is 1 hour behind Sydney from Oct 4; Perth 3 hours (E6 s7).

---

## 5. Which three executed trades become the notes (a menu, not a quota: TN guide L11-13, L29-30, VRF)

| Slot | Trade | Shows (only if true) | Why this trade (INT) | The reflection's one extra job (E2 F9) |
|---|---|---|---|---|
| A | TLH (IEF bought with it as one decision) | **Supported and tested** | The operations job: the ten payments only her portfolio may fund | Tested: the three pre-registered numbers (section 7), then what the rule said to do (hold); small moves and poor tracking reported as they are |
| B | The building minimum (2032 note, IBTM or stand-in) | **Refined**, only if the decision log shows, dated before this order, the change from "a floor bought in 2031" to "the minimum bought when the 2028 money arrives", with the reason in students' words; otherwise **supported** | The most Laura-specific holding: a figure partners will rely on, sized by her own second deposit (E4 L6) | Refined: what changed and the research that changed it (at equal stock risk, about the same middle, better bad cases; at most one number). Supported: why a dated holding (an amount on a date, not only a moving price) |
| C | VT | **Supported** (carries out the plan as refined) | The growth job: money nobody else relies on | The true refinement story: growth-first (about 75% stocks) was tested and dropped because it could miss a payment (about 3 in 100 modelled futures; about 4 in 10 if the 2028 deposit never came; F-401, F-404, VRF, MODEL); now all money nobody relies on is in stocks, the "why so little stock" answer by goal. One number at most |

- Never create a trade to fill a category. Three different jobs, three different role words (TN guide L11 "three investment decisions", VRF).
- Fallback (iii): A = TLH; B = a listed dated rung, else IEF only if the "one decision" acceptance is logged; C = SGOV/BIL leftover. Fallback ALT: A = TLH; B = VT; C = VGSH (ticket v1 s4).
- Final choice made Oct 19-20 from executed trades only (ticket v1 s4).

---

## 6. Per-note checklists (elements in noun phrases, never wording)

### 6.1 WInS note: common rules (E6 s5.6; Guide p.3 L84-86, VRF)
- [ ] **C1** one Guide role word + the team's own label (same label in every note, the log and the IPS).
- [ ] **C2** Laura's dated need, **with the scaling marker**.
- [ ] **C3** one dated, checkable fact, source named in words (no link).
- [ ] **C4** the rule or risk.
- [ ] **≤300 characters** until the box test says otherwise; if the box visibly allows more, extra detail up to about 600.
- [ ] **Trim order** if over: keep C2 (with marker), C3 and the role word; move C4 and the label to the reflection (AY1 D12 C1; T2 finding 6).
- [ ] No ticker, side or quantity needed (the trade record shows them).
- [ ] Paste, confirm nothing is cut **before** submitting; never finish a cut sentence with an added note (it carries a later time stamp); copy the saved note character for character into the decision log straight after.

### 6.2 Note elements and banned words by note

| Note | C2 need (with marker) | C3 one fact (pick one) | C4 rule / risk | Banned in this note |
|---|---|---|---|---|
| A operations | The ten $50,000 payments 2033-2042; her operations money after both deposits (about two-thirds of her **total** money, never "of the payments", E3-10) | The pair's rate sensitivity about 10 years, set to the payments' (issuer durations, dated; team's calculation); or TLH's own effective duration (iShares, dated) | Never sold after a rate rise or trimmed after a fall; re-mixed only if sensitivity drifts more than a quarter-year | match, matched, "mature in her payment years" (74.7% of TLH matures after 2042, VRF via ticket v1), stable, safe, reduce volatility, guaranteed, locked, operating reserve, "bought in January 2027", "fits in $300k" |
| B building minimum | The least she will put toward the building in 2033, sized to repay her second deposit; "after her 2028 deposit" | The note matures 15 Nov 2032, 47 days before 1 Jan 2033 (Treasury, dated); or IBTM holds Treasuries maturing Apr-Sep 2032 and ends around December 2032 (iShares, dated). Stand-in: moves like a late-2032 Treasury, no date | Held to its end; never sold because rates moved | "repays $X" for IBTM; guaranteed; risk-free; "locked 5%"; any 2031 range or top; promised; pledged; any date claim for a stand-in |
| C stock fund | The building's stretch and her flexibility in 2033, from money nobody else relies on; "after her 2028 deposit" | All of the plan's stock money, about 9% of her money after both deposits (team's calculation); or VT's stock count and share outside the U.S. (Vanguard, dated) | Held until 2033, never sold for market reasons; a fall shrinks only the stretch above the minimum, never the payments or the minimum | a return forecast, overvalued, CAPE, "halves AI exposure", "known/locked 5.2%", "Laura likes risk", the statistics degree, promised |

**Banned in every note and reflection** (E6 s2, s5.1, s5.7, s5.9, s6.1 rank 6; ticket v1 s8): Laura quotes or the case pull quote as hers; "Laura's portfolio" for the WInS holdings; reserve size, facility range, co-sponsor range or any 2031 figure; "promised"/"pledged" for anything above the minimum; "guaranteed", "risk-free", "safe", "100%", "certain" without its qualifier; identity, heritage or Taiwan as a reason; "falling" or book-title puns; the statistics degree (E6 D8: zero uses); "our portfolio manager approves"; WInS profit or rank; probabilities (team judgement). Vocabulary to keep consistent: "certainty" for the payments, "confident" for the range, "credibility" for her standing, "moves like / stands in for" for WInS funds.

### 6.3 What each ≤100-word reflection must cover (students, after the trades, without AI; TN guide L46-52, VRF; E6 s5.7)
- [ ] The three official answers: **why** the decision; **how it aligned** with the strategy; **how it served** her goals, funding needs or risk.
- [ ] Which of supported / tested / refined it shows, true to what happened (section 5).
- [ ] Exactly one extra job (section 5).
- [ ] ≤95 words by two counters (higher count wins). At most one number, except the tested reflection (exactly three); every number dated and graded in words.
- [ ] One case-stated trait that passes the swap test (would it be true of any client?): A = fixed payments only her portfolio may fund (case L91-92); B = a figure partners will rely on (L114-116); C = "thoughtful risks" within "an appropriate balance" (L69-74) (VRF).
- [ ] Reflection A also covers the scaling in plain words: WInS shows her plan after both deposits, scaled; the funds stand in for the bonds she buys; in January 2027 almost all of her real first deposit buys the payments.
- [ ] Not in any reflection: Laura quotes; the pull quote as hers; her career story or regret line as a reason; "loss tolerance", "break-even", "house money", "composure"; the statistics degree; reserve size, facility range or 2031 figure; WInS profit or rank.
- [ ] Same rule names as the IPS will use (decision-log column).

---

## 7. Pre-registered "tested" data capture (E6 s5.5, s5.8; ticket v1 s0)

| Item | Rule |
|---|---|
| Pre-register | Before the first fill, log: window = fill-date close to the Tue Oct 20 close; the three measures below; the rule's expected action (hold) |
| Measure 1 | 10-year Treasury rate move in bp (treasury.gov daily par curve) |
| Measure 2 | The hedge's (IEF + TLH) % change, from WInS screenshots |
| Measure 3 | The payments' % change: value the ten payments on each date's curve with `A2_curve_recheck.py` or `D9_numbers.py` [3]; **never** `official_curve_pv.py` (fixed to 2026-09-25; AY2 D7 C5) |
| Screenshots | Every WInS position on the fill date and at the Oct 20 close (Wed Oct 21, 07:00 AEDT) |
| Distributions | Check IEF and TLH ex-dividend dates in the window; a ~0.4% distribution is large next to a ~1% signal |
| Labels | All three numbers: the team's own calculation from the WInS screen and the treasury.gov curve; percentages, not dollars |
| Odds | A 10bp-or-larger move: about 52% for an Oct 2 fill, about 40% for Oct 9 (T2 [4], ASM). Small moves are reported as they are; "tested" is optional |

---

## 8. Student-written notes and outside readers (E6 s5.4e; ticket v1 s0d; PM-04)

| Step | Check |
|---|---|
| 1 | A named student drafts offline from section 6 elements, with no research file or AI tool open |
| 2 | Second student restates the note's role in one sentence; mismatch = redraft |
| 3 | Five-word copy check: every five-word run of the draft searched in `research/`; any hit rewritten. Example: `set -- $DRAFT; while [ $# -ge 5 ]; do grep -rliF "$1 $2 $3 $4 $5" research/ && echo "HIT: $1 $2 $3 $4 $5"; shift; done` (strip punctuation first) |
| 4 | Draft pasted into a copy of the decision log before the order |
| 5 | Two readers outside the team read all three drafts and say what Laura's real money holds in January 2027. Either says "stocks" or "a building bond": fix the drafts. Two failures after redrafting: switch to (iii) (E6 D3) |
| 6 | Readers are also asked whether the WInS stocks contradict the plan (E6 s2 tests) |
| 7 | Reflections (Oct 21-22): same steps 1-3; no AI "polish" |

---

## 9. Decision log and AI-use log (first names only; no surnames, emails or birthdays)

**Decision log** (start before the gate; E6 R7, R10; M021):

| Column | Content |
|---|---|
| Date and time | AEST/AEDT and ET |
| Decision / trade | Includes every "decided not to trade" moment |
| Options considered | e.g. REC vs ALT; (ii)R vs (iii) |
| Vote | First names for/against |
| Reason | Students' own words |
| Rule name | Same name the IPS will use |
| Evidence and grade | Source and status label |
| Numbers | Prices, shares, $ at fill |
| Saved WInS note | Character-for-character copy |
| Refined flag | For note B: the dated REC decision entry, written before the minimum order |

**AI-use log** (start Tue Sep 29, backfill by Sun Oct 4; PM-08; Wharton AI policy: record in the Final Report's Works Cited, VP via brief):

| Column | Content |
|---|---|
| Date | When used |
| Student | First name |
| Tool / file | e.g. Claude sessions, this pack, E6 spec, ticket v1, D9 draft checker |
| Purpose | Brainstorm, research, check |
| What was used | Ideas, numbers, labels proposed |
| What was not | Confirms no AI wording in notes or reflections |

---

## 10. Submission checklist (TN guide L42-53, VRF; SMApply)

- [ ] Exactly three notes, each from a trade **executed** in WInS ("Yes, we will verify this").
- [ ] Each note quoted **exactly as it appears in WInS** (copied from the WInS screen, not from a draft). Ask Wharton whether an "added" note counts (ticket v1 open item 4).
- [ ] Each reflection ≤100 words (planned ≤95 by two counters) and answers the three questions.
- [ ] No reserve size, facility contribution, projections or co-sponsor text (TN guide L20-22, VRF).
- [ ] Notes and reflections consistent with the IPS central idea (split of jobs) and labels (PM-06 consistency table).
- [ ] Submitted via the SMApply (SurveyMonkey Apply) form on **Thu Oct 22 AEDT**; deadline Fri Oct 23, 5:00 p.m. ET = Sat Oct 24, 08:00 AEDT; no extensions (VRF).
- [ ] Screenshot of the submission confirmation logged.

---

## 11. Top TN risks and preventions (E5 top 10; T2; INT)

| Risk | Prevention |
|---|---|
| PM-01 strategy not owned; voice reads AI-made | Own-words lines before each vote; explain-back; students draft from a blank page |
| PM-04 AI wording in permanent notes | Offline drafting from elements; five-word copy check; no AI polish |
| PM-06 notes contradict the IPS (book date, scaling, labels) | Split-of-jobs idea; scaling marker in notes; two-reader check; consistency table Oct 22 |
| PM-08 AI use not logged | Dated AI-use log from Sep 29, backfilled |
| PM-05 process breakdown | Roles Sep 29; internal deadlines two days early |
| PM-09 generic notes (fail the swap test; the hedge note looks like Wharton's example) | One case-stated trait per reflection; Laura-specific building-minimum note |
| Note cut at an unseen limit | Zero-risk box test; 300-character drafts; trim order |
| Fewer than three executed trades (iii) or an order rejected at the open | (ii)R default; ≥$1,000 float; recompute shares from the last close; (iii) T-bill order only after fills |
| Position-limit breach or rejection | Branch chosen before ordering; one point under the cap; never add near the cap |
| Day-trading or advisor-trade breach | Buys only on the first day; no same-day fixes ("run with it", VP); only the trader places orders |
| Overclaim words ("guaranteed", "match", "promised") | Banned-word lists in section 6.2 |
| Late or wrong-time-zone submission | Submit Thu Oct 22 AEDT; deadline written in both zones |

---

## What this teaches
1. A trade note is permanent evidence: the reasoning is written before the trade, so the thinking has to be finished first.
2. Separating jobs (money others rely on vs money nobody relies on) makes three trades read as one plan, not three bets.
3. Deciding branches and tests in advance turns surprises (a cap, a small rate move) into honest evidence instead of scrambles.
