# Trading Notes Analysis (TNA): merged recommendation from 3 judge reviews and the execution reader findings

This review was done against commit 2affd4c on 14 Oct 2026. It is not submission text. The students write every reflection in their own words.

## 1. Decision

**Feature these three notes, in this order: roots first, then the floor, then the branch.**

1. **IBTR.** Filled order 10/07/2026 04:42:53 AM ET. Label: **tested**.
2. **IBTM.** Filled order 10/06/2026 10:01:41 PM ET. Label: **refined**, if gate G3 confirms it. Otherwise label it "aligned".
3. **VT.** Filled order 10/07/2026 08:27:19 PM ET. Label: **aligned/supported**.

**Alternate: B-T-4.750-15022037** (the 4.750% Treasury maturing Feb 2037). Filled order 10/07/2026 12:24:09 AM ET, per the export at 05_trading_note_reflection_wins_trading_notes.md:16. One review wrote :11 seconds, so copy the time from WInS. Swap rules:
- It replaces IBTM only if the team cannot settle one floor wording shared with the IPS by Mon 19 Oct.
- It replaces IBTR only if the team cannot explain IBTR's basis by Mon 19 Oct.
- It never replaces VT. VT is the only growth trade, and the TNA purpose opens with "approach to growth" (TNA instructions:5).

**Never use these:**
- The four notes on cancelled orders (05_...md:37-40). This includes the IBTR "0.3" note.
- B-T-4.500-15052038 (May 2038): muddled wording, and it is the mis-clicked order.
- IBTP: its 0.07% premium figure is unrecorded.
- IBTQ: it duplicates IBTO.
- Do not place any new trade just to create a pick (archive/rab/trades/notes.md:337).

**Average judge scores (out of 10):**

| Note | Average | The three scores |
|---|---|---|
| IBTR | 8.2 | 8, 8, 8.5 |
| IBTM | 8.2 | 8.5, 8, 8 |
| VT | 7.0 | 7, 7, 7 |
| Nov-2040 | 6.2 | |
| Feb-2037 | 6.0 | |
| IBTO | 6.0 | |
| Nov-2041 | 5.8 | |
| Nov-2039 | 5.7 | |
| IBTP | 4.7 | |
| May-2038 | 4.2 | |
| IBTQ | 4.0 | |

**Why this trio** (all three judges ranked it first):
- IBTR is the only note with a test set before trading. It has a threshold and a response fixed in advance, and its wording is the most independent of the AI examples (2%).
- IBTM is the only trade serving both objectives: the first payment and the facility floor. That links it to the case's 2031 co-sponsor need.
- VT is the only growth decision.
- Together they use all three verbs in the instructions, cover the payments, floor and growth, and follow the IPS order.

## 2. Gates to clear before anyone drafts (target Mon 19 Oct, the internal mock-judge date)

- **G1. Freeze the facts the TNA and IPS share.** The TNA cannot be edited after 23 Oct, so the IPS has to follow it.
  - **Strategy name: Root-and-Branch.** It was settled on 1 Oct (caplet/google_drive/final_report.md:21). COMPETITION.md:147 and :204 still say "Roots First".
  - **Floor wording.** The floor is quoted rounded down below IBTM's projected payout; this is one of the two readings listed in 15_tab_15.md:30. Delete "never below the floor" (01_version_5.md:28), "she cannot miss the range" (:30) and "a floor Laura can promise" (:20). Note that "promised" is on the kit's banned list (archive/rab/trades/notes.md:30), and the case warns against promising (Client Profile:114-116).
  - **Order for covering a shortfall:** first the 2027 leftover, then Laura's half, then the part above the floor (01_version_5.md:26).
  - **Where the roughly $8k 2027 leftover is held** (15_tab_15.md:34). If it sits in VT, the first backstop is stocks.
  - **Ladder-cost basis and date:** WInS-listed holdings, each rung sized to its end date, yields held unchanged to January 2027. IPS V5:16 and :24 still say "about $292,000 at late-September yields", which is the old STRIPS basis.
- **G2. Re-run the ladder check on the latest Treasury curve** around 21-22 Oct. Commit the short script and its dated output.
  - The 6 Oct figure ($293,447 and a 22.7bp break-even, keel/routines/tasks/MONITOR.md:22) has no committed script.
  - Two verifiers reproduced it to within $1 using the committed archive/rab/models/m1_ladder.py and the instrument end dates.
  - On the 13 Oct curve the same method gives $295,290 and 16.3bp of room (MODEL; scratchpad oct14/wins4/results_2026-10-14.txt).
- **G3. Confirm the IBTM order of events** from Gmail and Google Docs version history.
  - When did the 6 Oct Wharton email arrive, relative to the 10:01 PM ET IBTM order? The primary email is not in the repo, so this is UNVERIFIED.
  - When did "rounded down" first appear? In the exported tabs it appears only in V5 and Tab 15.
  - If the email came first, the reflection can say the decision changed the strategy. If not, it can say the email confirmed it.
- **G4. Ratify "hold" explicitly.** The October trade rule's 14 Oct check has no owner and was never ratified (archive/rab/trades/october_trade.md). The IBTR reflection's "no trade was needed" point depends on this being settled.
- **G5. Fill the Trade Log from WInS Order History and Transaction History.** Today trade_log.csv:2-210 is blank and tn_analysis.csv:5-7 is empty. Keep the screenshots in the team Drive, not the public repo, because they show the username.
- **G6. Add a post-30-Sep AI-use entry** (see the checklist in section 7).

## 3. What each reflection must cover

These are objectives only, not text. Each reflection is 100 words or fewer, so aim for about 90. Items are listed in priority order; "Optional" means only if words allow.

### IBTR (tested). The note is at 05_...md:15.

**Must cover:**
- **What IBTR is.** It is the iShares iBonds Dec 2036 Term Treasury ETF: a fund of 2036 Treasuries that ends around 15 Dec 2036, used for the 5th payment on 1 Jan 2037. Its payout is not fixed. The note itself never says any of this.
- **The test.** Before ordering, the team checked the IPS's central claim that Laura's first $300,000 alone buys all ten payments. It priced them on the 6 Oct curve using only WInS-listed holdings. Name that basis once, in plain words, and use the same basis in the IPS.
- **The rule set in advance.** If yields fall past the line, the 2028 deposit completes the earliest payments and the facility gets less. Payments are never cut (IPS V5:24, :26). This shows how her two objectives are ranked.
- **The client link.** The case requires ten payments with "a high degree of certainty" and no outside money (Client Profile:91). Her tolerance for a missed payment is low (IPS V5:22). So rate risk falls on the facility, not on the artists.
- **The live, dated result.** Par yields from 6 to 13 Oct: 7y 5.15 to 5.11, 10y 5.27 to 5.21, 20y 5.68 to 5.60 (treasury.gov CSV, fetched 14 Oct). The room left is now about 0.16 percentage points (MODEL). Quote the G2 re-run figure with its date. Crossing the line would be the rule working, not the plan failing.
- **One scale clause.** WInS shows her plan after both deposits, scaled to $300k. The ladder is about two-thirds of the book, and IBTR is about 6.6%.

**Optional:**
- Falling yields raised the WInS bond values but made her real January purchase dearer. Judge the decision by her cost (TNA:15-16; faqs.txt:81). Never present this as a gain.
- The last five payments use individual bonds because no iBonds fund ends in 2037-43. This is the only way the trio shows the bond half.

### IBTM (refined, conditional on G3). The note is at 05_...md:19.

**Must cover:**
- **Why one fund does two jobs.**
  - The two jobs are the 1 Jan 2033 payment (paid from the 2027 deposit in her plan) and the facility floor (paid from the 2028 deposit).
  - WInS lists no Treasury maturing between Feb 2031 and Feb 2036 (COMPETITION.md:93).
  - Of the 4,503 shares, 1,142 are for the payment and 3,361 for the floor (portfolio.csv:38-39).
  - Explain "floor" in plain words.
- **The refinement, from the team's own dated log.** No judge cited this evidence.
  - On 5 Oct the team kept "never below the floor" on purpose: the real floor was to be zero-coupon Treasuries, and IBTM was only the WInS stand-in (final_report.md:24; IPS V2 at 11_old_versions_v2.md:26).
  - The 6 Oct email then limited Laura's real plan to WInS-listed stocks, ETFs and Treasury bonds (COMPETITION.md:87-90).
  - So IBTM became her actual floor holding. Its payout is not fixed, so the floor is now quoted rounded down.
- **The client link.**
  - In 2031 co-sponsors hear a range whose bottom is money she already holds, not a forecast.
  - That lets her signal commitment without overpromising (Client Profile:109-116).
  - Give no dollar figure (TNA:20-23).
- **Alignment.** Roots before branch: every Treasury order went in before VT.

**Optional:**
- What IBTM holds: 15 Treasuries maturing Jan-Nov 2032, about 48% of them by 31 May. Their cash waits inside the fund until about 15 Dec (archive/rab/trades/notes.md:136).
- The kit model says IBTM pays about 97% of the curve case even if its income earns only 2% (notes.md:139, MODEL). Re-check this before quoting it.

### VT (aligned). The note is at 05_...md:14.

**Must cover:**
- **Why this fund.** One fund of about 10,000 stocks (10,088 on 31 Aug) at a 0.06% fee, bought in one trade (keel/library/insight_v1/securities_and_allocation.md:89). It diversifies without stock picking.
- **The sizing decision, which the note leaves out.**
  - VT gets only about 9% of all her money, because the payments and the floor come first (COMPETITION.md:156-157). In WInS it is 8.8% at cost.
  - State the trade-off: a lower median gift in exchange for a much better bad case (COMPETITION.md:164).
- **Correct the note honestly.** The fund has more than one job:
  - Half lifts the gift above the floor, which sets the top of the 2031 range.
  - The other half is Laura's cushion against cost rises, a stronger Taiwan dollar or co-sponsor gaps. It is also second in line for any payment shortfall (IPS V5:26, :28, :30).
  - Nothing is promised before 2031.
- **The client link.** Paraphrase the case's "thoughtful risks" and "an appropriate balance between pursuing growth and protecting the capital required for her goals" (Client Profile:69-74). Under IPS V5:22, her risk tolerance is above average only above the floor.
- **The risk.**
  - A fall shrinks the part above the floor and her cushion. It does not touch the payments or the floor.
  - A rise before 2031 lifts the top of the range.
  - After 2031 the gift is capped, so further gains stay with her.

**Optional:**
- Diversification removes single-company risk, not market risk.
- VT was ordered after all ten payment orders.
- The 5 Oct internal debate (stock picking, EWT, GLD) can be mentioned only after its outcome is recorded. final_report.md:22 still says "[fill in]".

### Alternate: Feb 2037 bond (aligned; an honest constraint). The note is at 05_...md:16.

**Must cover:**
- **Why this bond.** It is the latest WInS bond before the 1 Jan 2038 payment. The 5.000% May-2037 bond was not listed when checked on 5 Oct (trading_notes.csv:129, :357).
- **The wait.** The bond matures 320 days before the payment. The money waits in a short-term Treasury ETF because the 6 Oct email excluded direct T-bills.
- **Size both reinvestment exposures honestly.**
  - The wait is small: if short rates fell from about 4.1% to 2%, it would cost about $570, roughly 1% of the payment (reviewer estimate).
  - Ten years of reinvesting coupons is the larger exposure: in the kit model the rung delivers about $47,000 at 2% (notes.md:266, MODEL).
- **The client link.** Payment certainty.

**Preconditions:**
- The IPS must add the short-term ETF point, about 13 words (15_tab_15.md:35). IPS V5:26 currently says income is "reinvested in the holding that paid it".
- Never copy the "5.000% Feb-2037" label from COMPETITION.md:181. It is wrong: the 96.019 fill implies about 5.25% as the 4.750% bond.

## 4. Traps in the picked notes and how to handle them honestly

The notes cannot be edited and must be quoted exactly. Every fix happens in the reflection and the IPS.

**IBTR**
- **Two IBTR notes exist.** Quote only the filled note from 04:42:53 AM ET. The cancelled note from 6 Oct 08:31:27 PM says "0.3".
  - A likely cause: "0.3" matches the old STRIPS basis in archive/rab/trades/refresh_tickets.py:896 (30.8bp on 6 Oct, which the tool words as "about a third"), while "0.2" matches the WInS-listed basis.
  - This is the verifiers' reconstruction and is UNVERIFIED. Leave it out of the TNA, but be ready to explain it.
- **"About 0.2" is now out of date** (about 0.16 on 13 Oct). Give the dated update. Do not imply the note is current.
- **The 0.2 basis is the cautious one.** Sizing to end dates over-delivers: $507,479 against a $500,000 target at forward rates (archive/rab/results/M2/bookL_basis_check.txt:15). The note understates the room rather than overclaiming. Do not add false precision.
- **"Buys Treasuries."** iBonds holdings are funds. Never write "matched", "locked" or "owns" for them.
- **Use the threshold in percentage points rather than the ladder's dollar cost when words are tight.** Never call the ladder cost the operating reserve's size (TNA:20-21).

**IBTM**
- **"Provides a floor" next to "payout not fixed".** Explain that the floor is quoted rounded down. Never use "guaranteed", "secures" or "never below".
- **"Provides a floor" also reads as present tense.** In her plan the floor is a 2028 purchase.
- **"So the timing fits" is loose.** The fund ends about 17 days before the payment, but its bonds mature through 2032.
- **Two floor definitions are in circulation:** "sized to return that remainder" (IPS V5:24) and "about $150k" (COMPETITION.md:155-156). Use the IPS one, and give no dollar figure.
- **AI overlap.** The note shares wording with its exemplar ("two jobs in Laura's plan", "It holds 2032 Treasuries"; notes.md:153). Disclose this, and do not reuse exemplar or Tab 15 wording in the reflection.

**VT**
- **"They only set how far her gift rises"** is wrong under IPS V5, and "They" is unclear.
- **"Promised minimum" overclaims.** IPS V5:20 makes the same mistake, so fix both.
- **The last 13 words are verbatim from the AI exemplar** (notes.md:301). Disclose this.
- **Give no return forecast and no WInS performance figure.**

**Repo-level traps**
- Do not use the practice-account claim at caplet/google_drive/notes_and_discussions.md:29. Practice activity was reset, and only executed WInS trades count (TNA:42, :53).
- Do not draw reflection wording from IPS V5 or Tab 15. A student's comment calls V5 AI-generated (01_version_5.md:36), and Tab 15 is AI commentary.

## 5. Where the judges disagreed, and the decision

1. **IBTM label.** One judge said refined. One said refined only if confirmed. One said "supported, plus an honest refinement". **Decision: refined.** It is backed by final_report.md:24 plus the 6 Oct email, and depends on G3 for "changed" versus "confirmed".
2. **Alternate.** The candidates were Nov-2039 (one judge, swapping out IBTR), a Nov-2041 trio, a Nov-2040 trio, and Feb-2037 (the team's own runner-up). **Decision: Feb-2037.**
   - Nov-2040 scores slightly higher (6.2 against 6.0), but it has the highest AI overlap: 41%, with an 11-word shared run.
   - Nov-2040's price claim reproduces only if the price includes accrued interest.
   - Feb-2037 passes the team's own overlap check (13%), rests on a recorded 5 Oct listing check, and adds liquidity and timing.
   - Its cost is one line in the IPS.
3. **Room left on IBTR.** Estimates were about 15bp and about 16bp. **Decision: about 16bp** (16.3bp, reproduced). Quote the G2 re-run.
4. **AI-overlap figures.** The measures differ: 3-word phrases (29-43%) against 4-word runs (31-55%). **Decision: use the team's own checker** (archive/rab/trades/note_check.py; notes.md:41).
   - WARN: Nov-2040 41%, Nov-2039 33%, IBTM 30%, VT 28%, IBTO 18%.
   - None FAIL. IBTR (2%), Feb-2037 (13%) and May-2038 (9%) pass.
   - This means disclose, not disqualify. When two options are close, prefer the cleaner note.
5. **The "0.3 to 0.2" story.** One judge would tell it; two say only if documented. **Decision: keep it out of the TNA.** There are no spare words and the cause is unconfirmed. It belongs in the Final Report.
6. **Scale clause.** **Decision: once, in IBTR.** IBTM's "which deposit pays for which job" point covers the rest.
7. **"Aligned" versus "supported".** The instructions use both words (TNA:12, :29). Either is fine.
8. **Submission date.** **Decision: submit by Thu 22 Oct**, one day before the hard deadline.

## 6. True stories and where each belongs

**TNA:**
- Yields fell after the trades (for IBTR).
- The 5-6 Oct change of the floor holding from zero-coupon Treasuries to IBTM (for IBTM).
- The order of the trades: roots before branch (IBTM and VT).

**Final Report only:**
- The switch from IEF/TLH to dated holdings by 30 Sep (archive/rab/inventory.md:20-22). Tell it only if it matches the team's real reasoning.
- The WInS bond gap, and IBTN turning out to be INSCORP Inc.
- Stale bond prices, which led to the 25bp rule.
- The sector-rule myth.
- Orders placed at Sydney midnight filling at the next US open.
- The pie chart labelling the iBonds "Long Equities".
- The 0.3 to 0.2 basis change.
- The VT debate.
- The 7 Oct AI-browser mis-click. Use it only in the Articulation section and the AI disclosure.

## 7. Pre-submission checklist

**Exact quoting**
- [ ] On submission day, copy each note straight from the WInS Trade Notes page. Do not use the export, and do not retype.
- [ ] Compare each note character by character with 05_...md:14, :15 and :19: apostrophes, hyphens, % signs and spaces.
- [ ] Do not "fix" anything inside a note.
- [ ] Confirm the notes are complete. They are 288-294 characters long, under the 300-character limit.

**ET timestamps**
- [ ] Use the order dates and times exactly as WInS shows them, in ET. Do not convert to Sydney time.
- [ ] If the form asks for the executed date, take it from WInS Transaction History. The iBonds are expected 7 Oct and VT 8 Oct; these match the next-open prices on Yahoo, but are not yet confirmed in WInS.
- [ ] Check the SMApply form's fields by 19 Oct. Whether it asks for date or symbol fields is UNVERIFIED.

**Filled trades only**
- [ ] Each pick shows as executed, not cancelled or open. Wharton verifies this (TNA:53).
- [ ] No cancelled-order notes. No practice-account trades.

**100-word limit**
- [ ] Each reflection is 100 words or fewer by the Google Docs count and by a second person's hand count. Aim for 95 or fewer, because figures like "$300,000", "1 Jan 2037" and "0.06%" count differently in different counters.
- [ ] Keep the quoted note separate from the reflection.
- [ ] Each reflection answers why, the alignment, and the client goals/funding/risk link.

**Banned content**
- [ ] No 2031 dollar range, operating reserve size, facility amount or projection.
- [ ] No WInS gain, loss or rank.
- [ ] None of: guaranteed, risk-free, locked, safe, promised, never, cannot miss, matched.
- [ ] No quotes attributed to Laura.
- [ ] No "bp" or "duration" without a plain gloss.
- [ ] Never call the WInS book "Laura's portfolio".

**Consistency with the IPS draft**
- [ ] The G1 items match the IPS: name, floor wording, shortfall order, cost basis and date, and the scaling statement.
- [ ] If Feb-2037 is used, the IPS includes the short-term-ETF line.
- [ ] Check against the IPS the team will actually submit, not V5.
- [ ] List the IPS edits these choices force, due 6 Nov.

**AI-use logging**
- [ ] Add a dated entry. caplet/docs/AI_USE.md was last updated on 30 Sep, and research/insight_v1/AI_USE* (named in COMPETITION.md:144) does not exist. Record:
  - who wrote and who typed each picked note;
  - which exemplars they read;
  - the 6 Oct "AI draft" column in trading_notes.csv;
  - the AI browser filling tickets up to Preview, and the 7 Oct mis-click;
  - the Tab 15 AI edits;
  - this review.
- [ ] Find out whether AI typed any note text at the Preview step (UNVERIFIED).
- [ ] Students write all three reflections themselves, with no pasted AI text.
- [ ] Disclose all of this in the Final Report's Works Cited (due 4 Dec).

**Records and submission**
- [ ] The Trade Log is filled and the screenshots are in the Drive (G5).
- [ ] Submit by Thu 22 Oct. The hard deadline is Fri 23 Oct, 5:00 pm ET (Sat 24 Oct, 08:00 Sydney).

## 8. Still UNVERIFIED

- The text and arrival time of the 6 Oct Wharton email (the primary email is not in the repo).
- The cause of the 0.3 to 0.2 change.
- The IBTP 0.07% figure for 2 Oct.
- Who wrote each note.
- Whether AI typed any notes.
- The SMApply TNA form's fields.
- Whether WInS stays viewable after 6 Nov.
- Which short-term Treasury ETF would hold the Feb-2037 proceeds.

The reviewers' working files stayed in the session's temporary folder and are not in the repo; the independent checks are in `../checks/`.