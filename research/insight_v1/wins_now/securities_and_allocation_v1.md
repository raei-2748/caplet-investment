# WInS ticket v1: orders for options (ii) and (iii), position-limit branches and the trading-notes plan

Agent T1 (Trading-Now editor), insight_v1 run, written 2026-09-28 (before the first U.S. open of the season,
13:30 UTC). This file **supersedes** `wins_now/securities_and_allocation_v0.md` for trading. That file's internal
heading already said "v1" after the S4 red team; this is the next revision.

**Serves:** WInS trading as the source of the Trading Notes (TN, due Oct 23), plus the one IPS consistency point that
depends on it (brief s17). No Final Report work.

**Status:** PROVISIONAL. The team has not voted on the strategy. This is AI-generated research: orders, numbers,
checklists and "must contain / must not say" lists. **It contains no note, reflection or IPS text.** The students
decide and write every word.

**Every security here is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK.** There is no separate approved list this
season; "Any ETF available on WInS" is allowed (SMApply Trading Details, VP). No relayed user messages arrived during
this task. Read the decisions first in `research/insight_v1/phase_D/trading_now_brief.md`.

**Numbers:** `.venv/bin/python research/insight_v1/scripts/T1_ticket_v1_numbers.py` (run from the repo root). Section
numbers in brackets below point to its output.
- Prices are closes of **2026-09-25** (Fri), re-read on the issuers' pages on 2026-09-28 (VP). SPTL, SPTI and BIL show
  "as of Sep 24".
- Durations are issuer "effective duration": IEF 6.86y and TLH 11.58y as of Sep 25 (TLH was 11.59y on Sep 24).
- Share counts are rounded down. Recompute on the trade date.

**Labels:** VP = verified on the primary page. VRF = verified in a repo file. SNIP = snippet or secondary, unverified.
ASM = assumption or model output, not a forecast. INT = our interpretation.

**Terms:**
- *Promise money / hedge*: the Treasury funds that stand in for the ten fixed $50,000 payments (2033-2042).
- *Growth money*: everything the payments do not need.
- *Duration*: roughly the % a fund falls if rates rise 1 percentage point. About 10 years here.
- *Position limit / cap*: the most WInS allows in one security.
- *Twist*: short and long rates moving in opposite directions.
- *Rung*: one Treasury bond that matures near one payment date.

---

## THE TICKET

### 0. Gate: tick all five before the first order (unchanged in spirit from v0; items added)
- [ ] **(a) Lock-early vote** recorded: first names, date, reason. If the vote is "no", stop; this ticket does not apply.
- [ ] **(b) Book chosen:** (ii) or (iii). If (ii), also the growth split (50/50 or 60/40, or "provisional 60/40,
      decision by [date]"). T1 recommends (ii) and 50/50, both at medium-low confidence; the reasoning is in the brief.
- [ ] **(c) Session Rules screenshot** (Portfolio Summary > Session Rules). Record:
  - the single-security limit **and** any separate bond or security-type limit;
  - the day-trading definition (the "?" tooltip);
  - trades allowed and commissions.

  Also read the logged-in Trading Details page for any "required trading activity" and first-trade date.
- [ ] **(d) Each WInS note drafted by a student in the student's own words** from section 5, to **300 characters or
      fewer**. A second student restates its role in one sentence (D12), and the draft is pasted into a copy of the
      decision log first.
- [ ] **(e) Branch picked in advance** from section 3, including the cap-under-25% rule and the cap-to-option switch.

**When:** aim for fills by **Fri Oct 2 ET** (11:30 p.m. AEST that day); hard stop Fri Oct 9 (ASM team rule). All
orders go in **one session**, promise money first. Orders placed while the market is closed fill at the next U.S. open
(SMApply FAQ, VP). Screenshot every position on the fill date: this starts the "tested" window.

### 1. Option (ii): the mix Laura's portfolio reaches after both deposits, scaled to $300,000
The hedge is 66% of the book (the plan's 65.9% promise share after 2028, ASM). VT equals the plan's whole-portfolio
stock share (20.4% at 60/40, 17.0% at 50/50). The 1% cash float comes out of the short-Treasury part.

| # | Order | Split 60/40: weight, $, ~shares | Split 50/50: weight, $, ~shares | Role word (Guide) and team label |
|---|---|---|---|---|
| 1 | BUY IEF | 23.5%, $70,500, ~783 | same | future funding: promise money, part 1 |
| 2 | BUY TLH | 42.5%, $127,500, ~1,365 | same | future funding: promise money, part 2 |
| 3 | BUY VT | 20.5%, $61,500, ~384 | **17.0%, $51,000, ~318** | growth: growth money |
| 4 | BUY VGSH | 12.5%, $37,500, ~651 | **16.0%, $48,000, ~833** | risk management, then liquidity: short-Treasury part of the growth money |
| | Cash | 1.0%, $3,000 (about $2,900 after 4 x $25) | same | liquidity: cash float |

- Hedge: IEF share = (11.58 - 9.90) / (11.58 - 6.86) = 35.6% of the hedge [1]. It is "about 10 years" on issuer
  numbers, and its worst 50bp twist error is about $1.5k, 0.5% of a $292k hedge [2] (ASM).
- Band inside the growth money: VT at **45-55%** (50/50) or **55-65%** (60/40). Check weekly and trade VT against VGSH
  only. It is very unlikely to fire before Oct 23 (about 0-2% even in a crisis; D7 as corrected by AY2, ASM).

### 2. Option (iii): the literal January-2027 book, with its named third trade
The hedge is 98% of the book: the ladder's cost share, $294,387 of $300,000 on the Sep-25 curve (ASM model on a VRF
curve). The ~2% 2027 leftover **waits in T-bills**, which is the plan's own rule (v0 s8; D10 C1 / AX2 fix).

| # | Order | Weight | $ | ~Shares | Role word and team label |
|---|---|---|---|---|---|
| 1 | BUY IEF | 34.9% | $104,700 | ~1,163 | future funding: promise money, part 1 |
| 2 | BUY TLH | 63.1% | $189,300 | ~2,027 | future funding: promise money, part 2 |
| 3 | BUY SGOV (alternate BIL, then SHV) | ~1.5% | ~$4,500 | ~45 SGOV / ~49 BIL | liquidity: the 2027 leftover |
| | Cash | ~0.5% | ~$1,400 after 3 x $25 (keep at least $1,000) | | liquidity: cash float |

- Buy the T-bill ETF **in the same session** as the hedge. It is part of the book, not a trade made later to get a
  note.
- Honest cost: about $18 of interest in the WInS window against a $25 commission. In the real plan the leftover waits
  a year, about $220 (ASM; BIL yield 3.94% on Sep 24, VP) [5]. The reason is the plan's rule, never WInS profit.
- **If no T-bill ETF is listed**, the third trade must be the dated rung (section 7). If neither exists, (iii) cannot
  promise three executed trades by Oct 23, so **choose (ii)**.

### 3. Position-limit branch (read both limit lines; decided before the first order)
Each capped fund is held **one point under the cap** (ASM: the limit is checked when the order is placed). Figures are
shares of the $300,000 [3]. The twist error is the worst 50bp twist, measured forward-consistently (S4 method, ASM).

| Single-security limit shown | Option (ii): hedge 66% | Option (iii): hedge 98% |
|---|---|---|
| None, or 65%+ | IEF 23.5 / TLH 42.5 (about 9.9y; $1.5k) | IEF 34.9 / TLH 63.1 (about 9.9y; $1.5k) |
| 44-64% | same as above | IEF 34.9 / TLH at the cap minus 1 / **SPTL** the rest |
| 35% | IEF 23.5 / TLH 34 / SPTL 8.5 (10.2y; $2.1k) | IEF 34 / TLH 34 / SPTL 30 (10.6y; $3.0k) |
| 25% | IEF 23.5 / TLH 24 / SPTL 18.5 (10.5y; $2.8k) | IEF 24 / TLH 24 / SPTL 24 / VGIT 17.6 / VGLT 8.4 (9.9y; $2.8k) |
| **Under 25% (new rule)** | IEF, TLH and SPTL at the cap minus 1; VGIT, then VGLT, take the rest so the hedge stays about 10 years. At 20%: IEF 19 / TLH 19 / SPTL 19 / VGIT 9 (9.9y; $2.6k). At 60/40 VT (20.5%) exceeds 19%, so split the equity into VTI 12.7% (~100 sh) and VXUS 7.8% (~270 sh). At 50/50 VT (17%) fits down to an 18% cap. **If 5 or more hedge funds would be needed (a cap of about 17% or less), stop and ask Wharton (Contact Us) before trading.** | **Switch to (ii) and re-vote gate box (b).** (iii) needs 6 funds at 20% and is not feasible at 15% with the listed Treasury ETFs. **Exception:** Session Rules show a separate, higher bond limit **and** the Bonds drop-down lists a Jul-Dec 2037-2041 Treasury. Then keep the ETFs at the cap minus 1 and carry the rest of the hedge in that bond, re-solved to about 10 years on the trade date |

- SPTL's alternate is VGLT. Every branch is described in notes as "about 10 years"; never quote two decimals.
- **Continuous limit (ASM, D10):** a holding placed at 24% under a 25% cap crosses 25% only after rates fall about
  101bp (TLH, ii) or 118bp (SPTL, iii), or rise about 128bp (IEF, iii). Never add to a position near the cap.
- **If an order is rejected by a limit nobody could see beforehand,** the response is a genuine rule-driven trade and
  may be a "refined" note (AY2 C1). A branch chosen in advance is **not** a refinement.
- **If TLH is not listed:** (ii) IEF 40.9 / TLT 25.1; (iii) IEF 60.7 / TLT 37.3. These are recomputed at the Sep-25
  durations with the ticket's formula; TLT 14.84y. If a cap also applies, re-solve with the same fill-order rule before
  trading.

### 4. Which trades are the candidates for the three notes (choose the final three on Oct 19-20)
"Supported, tested, **or** refined" is a menu, not a quota (TN guide L12 and L29-30; Guide p.3; case L152; all VRF). A
trade is never created to fill a category.

| Slot | Option (ii) | Option (iii) | Supported / tested / refined |
|---|---|---|---|
| A | TLH (or SPTL if capped): the promise money | TLH: the promise money | Supported at the trade. Its reflection can show **tested**: the rate move from the fill to the Oct 20 close, against the hedge's % change and the payments' % change |
| B | VT: growth money | The dated rung, if listed (section 7); otherwise IEF (weaker, same role) | Supported. The VT reflection can show tested: the growth money moved, the payments did not |
| C | VGSH (a distinct role), **or** the split-decision trade if a pre-announced decision changes the split (**refined**), **or** the rung | SGOV/BIL: the 2027 leftover | Supported, or refined (ii only) |

Prefer three different role words, at least one honest "tested" reflection, and "refined" only if it really happened.
Under (iii), one reflection must answer **why so little equity**. The content: in January 2027 almost all of her real
$300,000 buys the payments, and her room for stock risk starts with the 2028 money (D13c N1; D10).

### 5. What every WInS note must contain (elements only; ≤300 characters planned)
The four elements the Guide asks for (p.3 L84-86, VRF) are the reasoning, the alignment with strategy, the supporting
research or analysis, and the expected role. D9 M001 and D12 M247 map them to a **core that fits in 300 characters**.
The trade record already shows the side, ticker and quantity, so name the instrument type in a few words at most.
- [ ] **C1 Role:** one Guide role word plus the team's fixed label (tables above). Never switch labels between notes.
- [ ] **C2 Laura's dated need:** the ten $50,000 payments 2033-2042, or the facility contribution and flexibility in
      2033, or the small 2027 leftover waiting for the 2028 deposit. **Under (ii), fold the scaling into this
      element**: "after both deposits" for promise money; "after her 2028 deposit" for growth money (AY2 C1; D9 M012).
- [ ] **C3 One research fact, dated, with its source named in words** (no link). Prefer a price or an issuer figure
      over a forecast (D12 grades).
- [ ] **C4 The main risk accepted, or the pre-set rule that governs it.**
- [ ] If the box visibly allows more than 300 characters: add D9's detail (a second fact or clause), up to about 600
      characters. Never use a second, added note to finish a sentence. Paste, check nothing is cut, then submit.

| Note | C2 need | C3 research fact (pick one) | C4 risk or rule | Must never say |
|---|---|---|---|---|
| Promise money (TLH / IEF / SPTL) | The ten payments; (ii): the promise is about two-thirds of her portfolio after both deposits | (iii): the payments cost about $292-294k for Jan 2027 at [trade-date] Treasury prices (re-price with `D9_numbers.py [3]` or `A2_curve_recheck.py`). Either option: the pair moves about 10% per 1-point rate change, as the payments do (issuer durations, dated). Why TLH (reflection if no room): its bonds sit closer to her dates than a 20+ year fund's, though about three-quarters still mature after 2042, so never imply they mature in her years | Never sold after a rate rise (the payments got cheaper too); only re-mixed to keep about 10 years | match, matched, mature in her payment years, locked, stable, reduce volatility, safe, guaranteed, operating reserve, "bought in January 2027" or "fits in $300k" as flat facts |
| Growth money (VT; ii only) | Facility contribution and flexibility in 2033, from the growth money after her 2028 deposit | The split and how it was set (if provisional: say so and give the decision date); or "one fund, about 10,000 stocks; top ten about 22% of assets" (Vanguard, Aug 31 / Jun 30 2026, VP) | A fall shrinks the facility range, never the payments. No tilts: her concentrated bets are her career, which already drives the 2028 deposit (content only, D8 AY2 item 14) | a return forecast, "overvalued", CAPE, "halves AI exposure", "known/locked 5.2%", "Laura likes risk", the statistics degree |
| Short-Treasury part (VGSH; ii only) | Facility contribution and flexibility; the kind of asset a later promised amount can be built from | Duration 1.9 years (Aug 31, VP): about -1.9% per +1 point. In a 20% stock fall the growth money falls about 10% (50/50) or 12% (60/40) instead of 20% (D12 arithmetic, ASM) | Rebalanced only against VT, within the band | "the 2031 floor", "already owned", "the amount she can promise co-sponsors", any floor %, "half = the promise" |
| 2027 leftover (SGOV/BIL; iii only) | The little left after the payments are bought waits for the 2028 deposit (case L61-65: no other flows) | The leftover is about 2% of $300k at [date] prices; the fund is about 0.1-year T-bills (issuer, dated) | Not invested for growth until 2028 | "earns", "cash buffer for living costs" (living costs are outside the portfolio), "reserve" |
| Dated rung (section 7) | The payment it stands for (e.g. 1 Jan 2033) | Its maturity date and face (Nov 15, 47 days before 1 Jan 2033; $50,000 = one payment under (iii), scaled under (ii)) | Held to maturity, so later prices do not change what it repays; the other payments' rate sensitivity sits in the ETFs (about 10 years) | "the whole ladder is in WInS", "risk-free" in WInS value terms; for IBTM only "a fund that ends in December 2032" |
| Split-decision trade (refined; ii only; only if it happens) | Same as the growth money | Which research changed the split, and that the decision date was announced in the first growth note | The reason is the 2031 promise and a flat median across two published forecasts; never a price move | "because stocks rose/fell", "overvalued" |

### 6. What every ≤100-word reflection must cover (written by students after the trades; not in WInS)
- [ ] The three official questions (TN guide L46-52, VRF): **why** the team made the decision; **how** it aligned
      with the strategy; **how** it supported Laura's goals, funding needs or risk considerations.
- [ ] Which of **supported / tested / refined** it shows, true to what happened.
- [ ] At most one number, with its kind said in words ("at [date] Treasury prices" for a price).
- [ ] **If tested:** the pre-registered window (fill date to the Oct 20 close); the rate move in bp from treasury.gov;
      the hedge's % change and the payments' % change (percentages, not dollars, under (ii)). About 20-25 words
      inside the three answers. Report small moves or poor tracking as they are (AY2 C2, C15).
- [ ] **Under (ii):** the scaling in plain words, at least in the promise-money reflection. The content: WInS shows her
      mix after both deposits, scaled to $300k; in January 2027 almost all of her real $300k buys the payments.
- [ ] **Under (iii):** the "why so little equity" answer, once (section 4).
- [ ] One case-stated trait, and it must pass the swap test (would it still be true for any client?). For the
      promise: fixed payments only her portfolio may fund (case L91-92). For growth: "thoughtful risks" within "an
      appropriate balance" (L69-74). For VGSH or the leftover: flexibility "as the project develops" (L102-103) or the
      two-deposit timing (D6 M125).
- [ ] Not in any reflection: Laura quotes; the "floor-first" trait; reserve size, facility amount, co-sponsor range or
      2031 floor share (TN guide L20-22); probabilities (a team judgement, D1); WInS profit or rank.
- [ ] The same rule names the IPS will use (decision-log column, D9 M212). The words are the students'; any AI help,
      including the D9 draft checker, is logged.

### 7. Optional dated rung (D1 M044, with the AX1b corrections)
Use it only if the Bonds drop-down lists a suitable U.S. Treasury. Search by maturity, not by a built-up symbol. $10
commission. Accrued interest is about $768-824 on $50,000 face; the buyer pays it. Bond prices update once a day.
Fund it from IEF and re-solve IEF/TLH on the trade date with the hand formula: IEF share of hedge = ((1 - r) x D_TLH +
r x D_rung - 9.90) / (D_TLH - D_IEF), where r is the rung's share of the hedge (AX1b item 16).

Order of choice: stop at the first "yes".

| Order of choice | (iii): face $50,000 | (ii): face ~$34,000 | Notes |
|---|---|---|---|
| 1. A Jul-Dec 2032 Treasury (4.125% 15-Nov-2032) | ~$48.4k (16.1%); IEF 13.6 / TLH 68.3 | ~$32.9k (11.0%); IEF 9.0 / TLH 46.0 | Pays for the first payment. **It raises TLH**, so skip it under any cap below about 69% (iii) or 47% (ii) |
| 2. A Jul-Dec 2033-2041 Treasury (likeliest 15-Nov-2039 or 15-Nov-2040) | ~$45-46k (15.1-15.5%); IEF 28-30 / TLH 53-55 | 2039: ~$31.6k (10.5%); IEF 18.8 / TLH 36.6 | About 10-year duration; **lowers TLH**. Under a cap below 44%, allowed only if the re-solve needs no new fund |
| 3. IBTM (iBonds Dec 2032) ETF | ~$37k (12.3%) | ~$25k (8.4%) | A fund, not a bond. It returns no fixed amount (iShares, VP) |
| 4. None listed | no rung | no rung | Record "no suitable dated Treasury listed". Do not force a Feb/May bond |

Figures are D1's at the Sep-25 curve (ASM model prices). Under (ii) the rung repeats the "future funding" role, so
it is optional; under (iii) it is the natural distinct note (AX1b item 7). The reason to hold it is implementation: the
promise is dated, so the book holds one dated bond where WInS lists one (AX1b item 8).

### 8. Never
- Never place an order before the gate. Never let the advisor place a trade. Never day-trade (User Guide p.6, VP): no
  buy and sell of the same security on the same U.S. trading day, and no same-day "fix" of an error.
- Never sell the promise money after a rate rise or trim it after a fall. Re-mix IEF against TLH only if the hedge's
  duration moves **more than 0.25 years from its starting value** (this band works in every cap branch). Never move
  money between promise money and growth money.
- Never lengthen the hedge to bet on rates (EDV, ZROZ, GOVZ, TLT alone). No leveraged, inverse, crypto-linked,
  thematic or single-country funds, and no ETNs. No Taiwan or AI tilt.
- Never put the reserve size, facility amount, co-sponsor range or 2031 floor share in a note. No Laura quotes. No
  words from the banned lists (section 5 and brief section 2 item 4).
- Never trade for rank, and never "tidy up" in the last days before Nov 6. Never push a position above the limit.

### 9. Calendar (U.S. Eastern Time; Australian times assume NSW/Victoria)
| Date | What |
|---|---|
| Now | Gate; logged-in checks (section 10); votes (a) and (b); notes drafted |
| By Fri Oct 2 | Fills. U.S. open 9:30 a.m. = 11:30 p.m. AEST until Sat Oct 3, then 12:30 a.m. AEDT the next day from Sun Oct 4. Screenshot the positions |
| Oct 2 jobs report, Oct 14 CPI (SNIP dates) | Check only, never trade |
| By Fri Oct 16 | Only if the split was provisional: decide, then trade once or log "decided not to trade" |
| Oct 20 close | End of the "tested" window: screenshot the positions |
| Oct 19-23 | Duration check (trade only on a >0.25y move); choose the three notes; write the reflections; team read-through |
| Fri Oct 23, 5:00 p.m. | TN due (8:00 a.m. Sat Oct 24 AEDT). Submit on Friday evening Australian time |
| Oct 27-28 | FOMC meeting (VP), after the TN deadline |
| From Mon Nov 2 | U.S. open is 1:30 a.m. AEDT |
| Fri Nov 6 | Portfolio freezes with the IPS (close = 8:00 a.m. Sat Nov 7 AEDT) |

---

## 10. WInS checks before the first order (from v0 s7, A4 and D1; tick in the session)
1. Official account (practice trades were reset). A student places every trade.
2. Session Rules screenshot (gate box c). Pick the branch in section 3.
3. Re-read SMApply Trading Details and the FAQ that morning, and the logged-in Trading Details / Getting Started pages
   (required activity; first-trade date).
4. Search each ticker: it must show as an **ETF** with the issuer's full name. SPTL and BIL now show "State Street
   SPDR ...".
5. Bonds drop-down: list every U.S. Treasury maturing 2032-2042 (maturity, coupon, accrued interest). Check whether a
   volume rule or an order-type limit appears for bonds. "No volume limit on bonds" and "market orders only" come from
   a generic Stock-Trak page (VP), UNVERIFIED for WInS.
6. Today's volume in WInS for each ETF. The rule is "no more than twice a security's current daily trading volume"
   (VP). Every planned order is below 0.2% of that cap on published volumes (D10, AX2 C5); Vanguard funds publish no
   volume. If an order is rejected, split it across days; never switch to a thinner fund.
7. The commission is shown ($25 per ETF trade, ASM that ETFs count as "stock"; $10 per bond). Cash stays positive.
8. Note box: a counter or limit? Paste the draft and confirm nothing is cut **before** submitting. Straight after,
   copy the saved note character for character into the decision log.
9. Does WInS pay interest on cash? Record it. It affects only how the T-bill leg is described, not the plan's rule.
10. Re-read the IEF and TLH effective durations on ishares.com that day. Recompute: IEF share of hedge = (D_TLH - 9.90)
    / (D_TLH - D_IEF).
11. Anything unclear: ask Wharton through Contact Us. Never contact Laura (disqualification, VP).

## 11. What WInS stands in for (so every note is true; the rule wording belongs to the IPS spec)
- **Jan 2027:** $300k buys the ten payments as a Treasury STRIPS ladder (about $294k on the Sep-25 curve, ASM). Then:
  - If it costs more, buy the longest-dated payments first. The 2028 deposit completes the ladder before any growth
    money (D1, D8 rule 1).
  - The joint tail: if rates fall **and** the deposit is smaller than the gap, part of the first payment stays
    unfunded. This must be named, not hidden (AY2 on D8).
  - Any leftover waits in T-bills.
- **Jan 2028:** the $150k plus the leftover is the growth money, at 50/50 or 60/40, reset yearly within its band.
- **Jan 2031:** a share of the growth money (an open parameter; the model uses 80%, D5 suggests 70%) is bought as a
  2-year Treasury. This never appears in a WInS note.
- **Jan 2033:** the ladder is the operating reserve. The WInS Treasury funds are never called that.

## 12. Securities (facts re-read 2026-09-28; all PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK)
| Ticker | Role | Expense | Duration (as of) | Close (as of) | Other (issuer page) | 2025-26 list (history only) |
|---|---|---|---|---|---|---|
| IEF | promise, part 1 | 0.15% | 6.86y (9/25) | $90.00 (9/25) | 16 holdings; $41.57bn; 30-day volume 8.83m | yes |
| TLH | promise, part 2 | 0.15% | 11.58y (9/25) | $93.38 (9/25) | 61 holdings, maturing 2037-2046, 74.7% after 2042 (S1 snapshot); $10.53bn; 1.97m/day | no |
| SPTL | promise, if capped | 0.03% gross | 13.65y fund OAD (9/24) | $24.27 (9/24) | 110 holdings; $10.95bn; 1.09m prior day | no |
| VGLT / VGIT | cap alternates | 0.03% | 13.5y / 4.9y (8/31) | $50.98 / $56.90 (9/25) | 101 / 102 bonds | no / no |
| TLT | only if TLH is missing | 0.15% | 14.84y (9/25) | $79.32 (9/25) | 47 holdings, maturing 2044-2056 | yes |
| VT | growth | 0.06% | n/a | $160.03 (9/25) | 10,088 stocks, 37.7% non-U.S. (8/31); top ten 21.7% (6/30) | yes |
| VTI + VXUS | VT alternate or low-cap split (62/38) | 0.03% / 0.05% (per S2) | n/a | $379.77 (9/25) / $86.35 (9/25, via S3) | | yes / yes |
| VGSH | short-Treasury part | 0.03% | 1.9y (8/31) | $57.59 (9/25) | 92 bonds; SEC yield 4.55% (9/24) | yes |
| SHY | VGSH alternate | 0.15% | 1.79y (9/25) | $81.21 (9/25) | 91 holdings | yes |
| SGOV | 2027 leftover (iii) | 0.09% | 0.10y (9/25) | $100.66 (9/25) | $111.8bn; 30-day volume 22.5m | no |
| BIL / SHV | leftover alternates | 0.1353% / 0.15% | 0.10y (9/24) / 0.28y (via S1) | $91.58 (9/24) / - | BIL yield to maturity 3.94% (9/24) | yes / yes |
| IBTM | rung fallback 3 | 0.07% | 5.05y (9/25) | $21.85 (9/25) | 15 holdings; ends Dec 2032 | no |

Sources, VP, read 2026-09-28 about 00:35 UTC with curl:
- ishares.com/us/products/239456 (IEF), 239453 (TLH), 239454 (TLT), 239452 (SHY), 314116 (SGOV), 328944 (IBTM);
- ssga.com spdr-portfolio-long-term-treasury-etf-sptl, spdr-portfolio-intermediate-term-treasury-etf-spti,
  state-street-spdr-bloomberg-1-3-month-t-bill-etf-bil;
- investor.vanguard.com/vmf/api/{VT,VGSH,VGLT,VGIT,VTI}/{price,characteristic}.

Not re-read today: VXUS (the API returned an error; S3's 9/25 read is used); VT top-ten share and expense ratios (S2
and S3, VP there); SHV (S1).

## 13. Changes from v0
| # | Change | Why (source) |
|---|---|---|
| 1 | Option (iii) gets a **named third trade**: the ~2% 2027 leftover into SGOV or BIL, bought in the same session. It falls back to the rung, then to switching to (ii) | AX2 blocking / D10 C1 |
| 2 | Option (ii) shows **both splits**: 60/40 (VT 20.5 / VGSH 12.5) and 50/50 (VT 17.0 / VGSH 16.0), with bands 55-65 or 45-55 | D2 (+AX2 C3, C4, C7), D6, D3 M034 |
| 3 | IEF/TLH re-solved at the Sep-25 durations: **23.5 / 42.5** (ii) and **34.9 / 63.1** (iii), was 23.6 / 42.4 | Issuer pages, VP |
| 4 | **Cap-under-25% rule** added, plus the cap-to-option switch ((iii) under 25% means switch to (ii)), the VT/VTI+VXUS split, a stop at 5+ hedge funds, and the individual-bond exception | AX2 C2; T1 script [3]-[4] |
| 5 | Duration band now **±0.25y from the starting mix**. The fixed 9.65-10.15 band clashed with the 25%-cap mix at 10.5y | T1 (inconsistency in v0 s3 vs s5) |
| 6 | Notes planned for **300 characters**, split into a note core and a reflection | D12 (UNVERIFIED for WInS) vs D9 |
| 7 | VGSH relabelled: role word "risk management", then "liquidity". No "already owned", no "amount she can promise", no floor % | D12; AY2 on D9 (C1); AX2 on D2 (C6) |
| 8 | Banned words extended: known or locked 5.2%; halves AI exposure; half = the promise; match; stable or reduce volatility; flat "bought in January 2027" or "fits in $300k" | AX2 C1, C5, C6; S4 finding 2; D9 M062; D7 M011; AX1b |
| 9 | Notes plan by supported / tested / refined. "Refined" only via a pre-announced split decision or an unforeseen limit, **not** SPTL. "Tested" on a pre-registered window with data capture | D7 + AY2 C1, C2, C5 |
| 10 | Planned "discipline/rebalance" trade dropped | D7 M002 |
| 11 | Optional **dated rung**, conditional and corrected: choice order, IBTM wording, cap rule, role clash under (ii) | D1 M044 + AX1b items 5-10, 14, 16 |
| 12 | Statistics degree **removed from the VT note** (one place across TN and IPS; the IPS owner decides) | AY2 C6; D6 M125 |
| 13 | Under (ii), the scaling is folded into each hedge or growth note's "need" element; under (iii), one reflection answers "why so little equity" | AY2 C1; D9 M012; D13c N1 |
| 14 | Ladder-above-$300k odds stated as "about 1 in 3" for the real Nov-15 ladder ("1 in 4" is the idealised ladder) and never put in a note | AX1b item 1; D3 |
| 15 | The Guide p.5 line ("should not be rewritten simply because markets move") is no longer cited as forbidding changes before Nov 6 | AX2 C3; AX1b item 4 |
| 16 | Gate box (c) now covers both limit lines, the day-trading tooltip and the logged-in activity rules. Box (d) adds the 300-character draft and the second student's restatement | A4; D12 |
| 17 | The long-term map is cut to four lines. The model-input note (sleeve bonds "3.5-3.9%") is withdrawn in favour of D2's market-consistent ~4.8% ASM; that is Final Report work, for later | AX2 C8; brief s17 |
| 18 | TLH-missing weights recomputed (IEF 40.9 / TLT 25.1 (ii); IEF 60.7 / TLT 37.3 (iii)) | T1, issuer durations 9/25 |

## Open items (for the team, today)
1. Votes (a) and (b), and the split if (ii). 2. The Session Rules numbers (both lines), the note-box limit, the bond
list and interest on cash. 3. Who places trades and who captures the data. 4. Ask Wharton whether an "added" trade
note counts. 5. The "first trade by Oct 10" claim stays UNVERIFIED until the logged-in page is read.

## What this teaches
1. **A snapshot needs a date.** WInS can show Laura's plan on one day only: January 2027 or after 2028. Both are
   honest if the date is said out loud, and each has a price in words or in note variety.
2. **Check that the deliverable is possible, not only allowed.** A book can obey every trading rule and still leave
   the team one executed trade short on Oct 23. The fix came from the plan itself, where the leftover already waits in
   T-bills, not from inventing a trade.
3. **A limit changes the best design.** A 25% or 20% cap costs the literal book three or four extra funds, but the
   scaled book only one or two. Deciding the branch before the session turns a midnight scramble into a look-up.
4. **Short boxes force clear thinking.** If a note may hold only 300 characters, each word must carry the role, the
   need, one fact or the rule. The fuller story belongs in the reflection, written later but never rewritten in the
   note.
