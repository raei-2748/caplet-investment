# Coherence reader 7: the Final Report plan against the frozen record (Tue 17 Nov 2026, Sydney)

Read blind. I did not open any earlier panel file, SCORECARD.md, LESSONS.md or ARGUMENT_LOG.md.

**Frozen record read in full:**
- IPS: `keel/final_report/FINAL_IPS_as_submitted.txt`.
- TNA: `keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt`.
- WInS notes (WN): `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`.
- The case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`.
- CANON and WHARTON_NORTH_STAR section 0.

**Plan files read:** SKELETON, INTENT, WORDS, CONCEIT, NUMBERS, `exhibits/tables.md`, `research/goldmine/AHA_REGISTER.md`, `research/meta/DENSITY_CUT_2026-11-17.md`, `research/meta/REBUILD_2026-11-17.md`, `research/meta/WHY_A_RANGE_2026-11-16.md`, and the two experience files (PEOPLE_IN_THE_ROOM, RANKING_5_RERANK). I also read the engine output `numbers/results_reserve_2026-11-15.json`.

**Line numbers.** Other runs were editing these files while I read. Line numbers are those of a snapshot taken during the read. Before writing, I compared the snapshot with the live files and found no differences.

**Severity:**
- HIGH: a judge holding the frozen text would see the report contradict or stretch it.
- MEDIUM: a frozen fact is blurred, or two parts of the plan would make a writer say opposite things.
- LOW: naming, dating or a stale note.

**Counts:** HIGH 1, MEDIUM 15, LOW 11.

---

## HIGH

### H1. 3f's second moment gives the model's 3.2% as the reason the share plan was dropped. The IPS gives a writer's income.

**What the plan says:**
- `SKELETON.md` l.263, moment (2): "our first plan, about three-quarters shares (team notes, 27 Sep), dropped before any trade when one date decided its misses (27 Sep model, 3.2%; 8s)".
- `CONCEIT.md` l.67 (V2.2, 3f): "The first plan ... missed one in 3.2% of simulated markets ... the fix was not better shares but printing the payments over everything (IPS l.11)".
- `research/goldmine/AHA_REGISTER.md` l.30 (row 10, version B, scored 4.0 for 3f): "3.2% meant about 1 in 31 against none".
- `research/experience/PEOPLE_IN_THE_ROOM_2026-11-16.md` l.176 keeps the IPS's reason out: "Keep out: IPS l.9's career reason as this moment's reason".

**What the frozen record says:**
- IPS l.9: "You'd think that someone with your taste for thoughtful risk and 6 years to wait would usually own shares. So, naturally, that was our plan – until we stopped and considered the actual nature of a writer's income."
- CANON A3 (l.45): "The experience section tells the same turn ... no other reason may replace it as the main one ... Ask Caplet for its own dated account."
- CONCEIT l.300 (section 4) had already sent the first plan to "Store only (coherence reader 5, Sun 15 Nov, L3 ... anywhere else it retells IPS l.9, whose reason is the team's own, not a model's miss rates)".

**Why a judge would see it:** The moment is even titled with the IPS's words ("Laura's taste for risk"). A judge would read the same turn told twice, with two different causes.

**Fix:** tell the 3.2% as the test that priced a switch the IPS already gave its reason for ("we checked it"), never as why the plan was dropped. Otherwise wait for Caplet's own dated account (CANON A3), and drop the l.176 keep-out rule.

---

## MEDIUM

### M1. The density cut removed the reserve's size, which the case requires (point 5)

**What the plan says:**
- `SKELETON.md` l.43, the 3a density row, gives only the price and the make-up: "the ten Treasuries the 2027 deposit buys plus the first dollars of the 2028 deposit". It also bans calling the $38,282 "the reserve's size".
- `DENSITY_CUT_2026-11-17.md` l.201: "$444,545 against $399,089 stays out of prose". Departure 1 (l.216-220) keeps the size out of 3a's first sentence.
- `SKELETON.md` l.257, the 3.0 reservoir, still plans "the three numbers: the reserve, the range, the confidence".

**What the case says:** l.95-97: "Teams must recommend its size and initial asset composition".

**The gap:** No prose sentence and no exhibit says what the reserve is worth on 1 January 2033. Figure 1's total row (see M2) can be misread as that figure.

**Fix:** after the Wed 18 Nov re-size, print the reserve's 1 January 2033 size once, at today's rates, in 3a or in Figure 1's note. Relabel Figure 1's total row first.

### M2. Point 7 resolved: $444,545 and $444,080 measure different things, so neither needs "reconciling"

**What the plan says:**
- `NUMBERS.md` l.2170 says the reserve's size "reads $444,545 here (111.4%) and $444,080 in Figure 1's data ... Reconcile them in the Wed 18 Nov re-run".
- `DENSITY_CUT_2026-11-17.md` l.216-220 says the same.
- `SKELETON.md` l.43 says $444,545 is "never in prose beside Figure 1's $444,080".

**What each figure is**, in `numbers/results_reserve_2026-11-15.json`:
- **$444,545 is the reserve's size.** It is `composition_1jan2033_total` (= `base[0].value_before_payment`, 444,544.60): the reserve's value on 1 January 2033 at the 6 November forwards. That is the ten own holdings, `own_rungs_value_1jan2033` = $399,089, plus the extra Treasuries, `margin_value_1jan2033_at_forwards` = $45,456.
- **$444,080 is not a value on any date.** It is the sum of `fee[i].own_holding_pays` (444,080.23): what each payment's own Treasury pays, added up over the ten payment dates 2033-2042. It is counted in the zero-interest world with fees, and nothing is discounted.
- **$55,920** is the sum of `fee[i].backstop_and_carry_cover` (55,919.77), the extra Treasuries' cover.
- **$500,000** is ten times $50,000.

The two figures agree only by chance. On Figure 1's own basis (cash waiting earns nothing, fees charged), the reserve is worth $425,319 on 1 January 2033 (`fee[0].value_before_payment`).

**Fix:**
- Relabel Figure 1's total row as "paid by each payment's own Treasury, 2033-2042, added up", so it no longer reads as a size.
- Strike "reconcile" from NUMBERS §9 l.2170, and quote $444,545 (or its re-sized value) as the size.
- After the re-size, both figures move. The extra Treasuries' column will pass $55,920.

### M3. Plan files imply the ten payments carry a cost margin. Today they carry none (point 6)

**What the plan says:**
- `SKELETON.md` l.47 (3e density): "the payments, each fund counted at what its bonds pay less its fee, its net asset value, with fund costs beyond the fee so far well inside the margin". The only margin named in that sentence is the range rule's.
- `SKELETON.md` l.76-77 and l.179 measure Trading Note 2's net-asset-value point with "the 0.5% cut". That cut sits only in the range.
- `DENSITY_CUT_2026-11-17.md` l.139 (E15) puts "well inside the margin" in prose.
- `exhibits/tables.md` l.99 (Table 3 row 4): "any gap from the extra Treasuries, re-tested (the range's from its 0.5%)".

**What the frozen record says:**
- TNA l.15: "their terminal payout is a net asset value, as opposed to a promise of par".
- NUMBERS l.2177, the known open item: "has no margin beyond it", with the re-size set for Wed 18 Nov. I am not re-reporting the open item itself, only these files that say otherwise.

**Fix:** until the re-size lands, tie "the 0.5%" and "well inside the margin" to the range only. After the re-size, say once that the payments carry the same 0.5%.

### M4. "Guaranteed" on a fund's figure: WORDS allows it, CONCEIT forbids it

**What the plan says:**
- `WORDS.md` l.24 declines "M2's ban on 'guaranteed' for a fund or a figure counted from it", citing NUMBERS l.440: "'certain' (or 'guaranteed' ...) for the stated ends after the move".
- `CONCEIT.md` l.49-50: "'Guaranteed' goes on the Treasuries, never on an iBond fund's payout".

**What the frozen record says:**
- TNA l.13: "although the final payout is not fixed".
- TNA l.15: "a net asset value, as opposed to a promise of par".

**Fix:** one rule in both files. "Guaranteed" (like "certain") takes the Treasuries, or the stated range after the move, as its subject. It is never used on a fund's payout or on a dollar figure.

### M5. Two retired conceit turns are still placed, and one carries a wrong ownership figure

**What the plan says:**
- "Let the ink dry" was retired by round 6 (`CONCEIT.md` l.192, V2.5: "failed with all three readers and is retired"). It is still placed in:
  - `SKELETON.md` l.45 (3c density row, in its list of turns);
  - `SKELETON.md` l.204 ("let the ink dry before erasing (a top stated a year early is not yet owned in about 11 of 100 futures)");
  - `CONCEIT.md` l.64 (V2.2 3c);
  - `AHA_REGISTER.md` l.27 (row 7).
- `CONCEIT.md` l.271 (section 3, 2031 row) keeps the same figure: "a top stated twelve months early is not yet owned in about 11 of 100 simulated futures". The phrase comes from `NUMBERS.md` l.453.
- "The key plate" was also retired ("stays out", `CONCEIT.md` l.193), but it is still placed in `CONCEIT.md` l.59 and `SKELETON.md` l.199.

**What the IPS says:** l.15: "Before you meet co-sponsors in 2031, the other half will move into Treasuries, so whatever figure you choose is money you already own." Before the move, no part of the top is owned in any future. "Not yet owned in 11 of 100" implies it is owned in the other 89.

**Fix:**
- Strike both turns from those rows.
- Wherever the early-statement figure survives, write "the move would buy less than a top stated a year early in about 11 of 100 futures".

### M6. $103,178 is placed in 3e's prose, against three guards

**What the plan says:**
- `CONCEIT.md` l.66 (V2.2 3e): "Shares at zero: the ten payments unchanged, the floor still pays about $103,178".
- `AHA_REGISTER.md` l.34: the deletion test, with "floor about $103,178", "serves as the proof sentence in 3e".

**What the guards say:**
- `DENSITY_CUT_2026-11-17.md` l.190 (section 4): "$103,178, what the floor pays", never in prose.
- `WORDS.md` l.30: never as "what it pays alone".
- 3e's density row (`SKELETON.md` l.47) allows only area (1) a number.

**What the frozen record says:** TNA l.13: "the final payout is not fixed".

**Fix:** the deletion test says "the payments unchanged and the range one figure, the bottom", with no payout figure.

### M7. Table 1 is described two opposite ways

**What the plan says:**
- `CONCEIT.md` l.59 and `SKELETON.md` l.199: "Table 1 as the page as it will stand after January 2028 (both deposits, scaled)".
- `SKELETON.md` l.38 (Section 2 density row): "scaled up, Table 1 is not Section 3's dollar split". Table 1 (`tables.md` l.15-30) holds no top-up and no extra Treasuries, and IBTM's lot is sized differently from Section 3's floor.

**What the frozen record says:** WN l.24: "scaled to the model portfolio". IPS l.13 and l.15 have the 2028 deposit complete the ten and buy the floor.

**Fix:** frame Table 1 as "the plan's instruments at $300,000, every Treasury row ink and VT the only pencil", never as the page after January 2028.

### M8. INTENT still says the facility is "the only thing" Laura asks anyone to share

**What the plan says:** `INTENT.md` l.23-24: "Ten years of the residency's operations are owned in Treasuries before the doors open, so the facility is the only thing Laura asks anyone to share. It leads 3.0 and the passage in 3d."

**What overrules it:**
- `SKELETON.md` l.158-161 (H9-119) corrects this: never "ten years of operations owned" or "the facility is the only ask".
- 3d asks for yearly programme money.
- The case, l.85-86: "any operating support beyond Laura's commitment, may come from co-sponsors".

**Fix:** rewrite INTENT l.23-24 as "ten years of her operating commitment owned in Treasuries, a base, not the residency's whole budget".

### M9. 3d prints $115,000 bare in a 2031 passage. 3c makes the figures travel with "on today's figures"

**What the plan says:**
- `SKELETON.md` l.46 (3d): "the top, $115,000 (no 'about') ... $95,000 of it held since January 2028, the rest since the shares moved in January 2031".
- `SKELETON.md` l.45 (3c) and l.42 (3.0): the figures "travel with 'on today's figures'".

**What the IPS says:** l.15: "markets will be able to increase or decrease the top of your planned band as we get closer to 2031".

**Fix:** keep Laura's words bare. The team's lead-in sentence to the 3d passage says once that the figures are today's, and that the rule sets them in January 2031.

### M10. "No interest" survives as shorthand (point 4)

**What the plan says:**
- `SKELETON.md` l.43 and l.162: "why test at no interest".
- `WORDS.md` l.24: "enough with no interest".
- `AHA_REGISTER.md` l.25 (row 5): "a standard that needs no interest" and "say the standard needs no interest".
- `NUMBERS.md` l.1000: "the top-up's part for no interest". This line also calls the extra Treasuries "the top-up's part", which breaks point 3.
- `NUMBERS.md` l.1014: "'If interest earns nothing', defined once".

**What overrules it:**
- `WORDS.md` l.64: "was 'if interest earns nothing', which a lay reader and a bond reader both read as false".
- WN l.18: "reinvested coupons fund the rest". Each bond's own interest counts.

**Fix:** use "if cash waiting earns nothing" in every one of these places, and call the $35,894 "the extra Treasuries" in NUMBERS l.1000.

### M11. What comes back from the extra Treasuries is described three ways

**What the plan says:**
- "Most comes back": `SKELETON.md` l.244 and l.258, `WORDS.md` l.27, `CONCEIT.md` l.62.
- "All of it by the last payment in 2042" and "at zero interest nothing comes back": `SKELETON.md` l.43 (3a density).
- `AHA_REGISTER.md` l.25 says both "most of the price comes back" and "never 'most of the extra comes back'". It also prices the extra as "$34,369 in January 2027 money", against 3a's "one form of the price, never three" (about $38,000 in January 2028 money).

**Fix:** use the 3a density row's words everywhere ("worth about $45,500 in 1 January 2033 money if rates hold, all of it Laura's by the last payment in 2042; if cash waiting earns nothing, none"). Strike "most" and the $34,369 form.

### M12. The "a policy is pencil" candidate would make Caplet's Investment Policy Statement sound non-binding

**What the plan says:**
- `CONCEIT.md` l.198 (V2.5 candidate for 3d): "a policy is pencil". It cites Kleinwort Benson v Malaysia Mining: "a statement of present fact and not a promise as to future conduct", where "the policy was reviewed when the tin market collapsed".
- `AHA_REGISTER.md` l.59 reserve: "A policy describes today".

**What the IPS says:** l.17: "There are only 2 possible reasons ... A fall in the market is not one of them."

**Why it matters:** The report sits under a document titled Investment Policy Statement. A judge would hear "a policy is pencil", "reviewed when the market collapsed", as being about Caplet's own IPS. This finding becomes HIGH if the candidate lands.

**Fix:** drop the candidate. If the comfort-letter point is kept, never put the word "policy" on Laura's side.

### M13. The inflation assumption and the yield assumption have no visible source or date (point 5)

**What the plan says:**
- `exhibits/tables.md` l.103 (Table 3 row 7): "building-cost trend 1.5% to 5.0% a year". Neither the row nor the note (l.105) names a source or a date.
- `SKELETON.md` l.47 says "Table 3 row 7 holds the band" for area (4), so a judge sees area (4) only there.
- `SKELETON.md` l.44 (3b) prints "about 93 of 100 simulated futures". The 0.9-point yield assumption is sent to the store and the 3e reservoir (`SKELETON.md` l.47), against `DENSITY_CUT_2026-11-17.md` l.127 (E3): "if any simulated-futures figure is printed ... its size returns beside it".

**What the case says:** l.146-147 asks for the assumptions on "the effect of inflation on portfolio projections and facility costs".

**Fix:**
- Add "DGBAS construction cost index, to October 2026" (or the dated source the band rests on) to Table 3's note.
- Add "yields moving about 0.9 points a year, our own assumption" beside 3b's 93 of 100, or to Table 2's note.

### M14. Liquidity, a Wharton criterion, has no place after the cut

**What the plan says:**
- In SKELETON, "Liquidity named" appears only in the 3a reservoir (l.258). No density row (l.37-47) names it, and the density rows win.
- INTENT failure 6 (l.123-124) wants "liquidity ... with a number".

**What the frozen record says:** TNA l.15: "in return we gain a level of liquidity". WHARTON_NORTH_STAR l.139 lists "liquidity needs" in the criteria.

**Fix:** one clause in 3a that names liquidity and points to Figure 1's cash dates (no new figure).

### M15. The 3b reservoir says Laura can give more than her stated top (point 1)

**What the plan says:**
- `SKELETON.md` l.259 (3b reservoir): "whatever is unused remains Laura's ..., and any further gift is a separate, announced choice".
- `SKELETON.md` l.45 (3c density): "the contribution never more than the top she states, anything above it joining her flexibility".
- "Gift" is itself banned (`SKELETON.md` l.258, l.288; WORDS).

**What the IPS says:** l.15: "half of the value of the shares will be promised to no one".

**Fix:** strike the clause. Anything above the top joins her flexibility, and the plan says nothing more.

---

## LOW

1. **WHY_A_RANGE 4d is stale but still cited by 3c.** `research/meta/WHY_A_RANGE_2026-11-16.md` l.361-362, the "one sentence" for why a range, still says "when each part was secured, the bottom in January 2028 before shares had any say". 3c cites 4d at `SKELETON.md` l.45. Both phrases are banned. Fix: replace 4d with 3c's own wording ("held since").
2. **"Cushion", banned by WORDS l.22 and l.28, survives.** It appears in `AHA_REGISTER.md` l.29 ("So her flexibility is a cushion, never a hedge"), `INTENT.md` l.33 ("a smaller cushion") and `SKELETON.md` l.260 ("passed that cushion", meaning the margin). Fix: use "her flexibility" and "the margin".
3. **Orange County is still in an aha reserve.** `AHA_REGISTER.md` l.48 names "Orange County's $13.0bn of borrowing" in the "Nobody can run" reserve, against 3e's "SVB once at most, never Orange County" (`SKELETON.md` l.47). Fix: strike it from the reserve.
4. **"Rub out" overstates IPS l.9.** `CONCEIT.md` l.60 (2.3): "three pencil lines that a single recession can rub out". IPS l.9 says "later and smaller". Fix: "can shrink in the same downturn".
5. **"Rarely" for about 1 start in 6.** `SKELETON.md` l.43 and l.227 say "short more often than not for start dates since 1981, rarely before". NUMBERS l.176 gives 17.1% for 1962-80 starts. Fix: "far less often before".
6. **3.0's notes invite a percentage and keep a banned claim.** `SKELETON.md` l.42 says "the confidence in one figure each", which a writer could fill with a percentage. Fix: "the confidence in one word, certain". Also, the 3.0 reservoir (l.257) keeps "The proposition no other founder can make", which l.42 and INTENT l.24-25 put out. Fix: strike it.
7. **INTENT has five stale lines:**
   - l.11 says "the half moved before 2031" (the move is 2 Jan 2031; say "before the 2031 meetings").
   - l.29-30 says "the 2028 deposit completes them, then buys a Treasury fund" and leaves out the extra Treasuries.
   - l.67 says "From 2033 the Treasuries are the operating reserve", a sentence SKELETON l.43 bans as a definition.
   - l.87 says "costs the range about $15,000" without naming its basis (Mon 9 Nov's call, NUMBERS l.220).
   - l.122 says "about 2,700 words".
8. **Three NUMBERS labels are stale:**
   - l.1000 calls the $35,894 "the top-up's part".
   - l.1014 heads a section "'If interest earns nothing'".
   - l.2177's sweep list has "$81,891", but the register's floor money is $81,889 (l.287).
9. **"The 2031 move" alone.** `AHA_REGISTER.md` l.21 and l.24 use it, against the ban in `tables.md` l.107 (row 6). Fix: "the move before the 2031 meetings".
10. **Two loose phrases in an aha row.** `AHA_REGISTER.md` l.32 has "what she intends to pay", against 3d's ban on "intend" (`SKELETON.md` l.46). It also has "'certain' sits on the Treasuries", where point 2 puts "certain" on the range she states. Fix: "what she gives", and "certain" on the stated range.
11. **"A click is ink" has no settled home.** It is placed in 3f (`CONCEIT.md` l.67 and l.190; `SKELETON.md` l.207), but 3f says "Buying it moves to 2.5" (`SKELETON.md` l.263). Fix: tie the click to moment (1)'s 00:30 open, or move it to 2.5.

---

## The seven points, one by one

1. **Co-sponsors count the top; 3d leads with it and says the bottom once as held since January 2028.**
   - The density rows hold (`SKELETON.md` l.45-46).
   - Table 2's last row holds ("equals the stated top").
   - Breaks: M15 (the 3b reservoir) and LOW 1 (WHY_A_RANGE 4d).
   - M9 is the one risk in 3d's own wording.
2. **"Certain" takes the stated range as its subject; no "95%", no "confidence interval" label, no default clause in 3c.**
   - This holds in 3c's density row (l.45) and in the 3.0 row.
   - Neyman is told without a label.
   - Wobbles: M4 ("guaranteed" in WORDS) and LOW 10.
3. **"Complete it" and "top up" mean the $2,388 only; the $35,894 answers the case's ask, held in Treasuries per IPS l.11.**
   - This holds in SKELETON l.43, WORDS l.21-22, INTENT, Table 3's note (l.105) and Figure 1's note.
   - Breaks: NUMBERS l.1000 (M10, LOW 8).
   - Nowhere says "inside IPS l.13's step".
4. **"If cash waiting earns nothing", never "a forecast in disguise", never a fund payout called fixed.**
   - The tables and the density prose hold.
   - The shorthand "no interest" survives in five places (M10).
   - "A forecast in disguise" survives only as a recorded ban.
   - "Fixed" is gone from NUMBERS section 4 (done Tue 17 Nov), but "guaranteed" on a fund figure is still open (M4).
5. **Did the density cut lose a required figure, and does each 3e assumption still show a source and date?**
   - Lost: the reserve's size (M1). Liquidity has no place (M14).
   - Assumptions: area (1) shows J.P. Morgan 2027 and the curve date (6 Nov 2026, Table 2's note). Area (4)'s band shows no source or date (M13), and the yield assumption is not printed beside a printed simulated figure (M13).
   - Still placed: the range and factors (Table 2), the confidence (3c), monitoring as 2031 and 2033 approach (Table 3), and the contribution and flexibility (3b).
6. **The payments' margin.** This is the known open item, not re-reported. The files that imply a margin are in M3.
7. **$444,545 against $444,080.** Resolved in M2: $444,545 is the reserve's size on 1 January 2033 at forwards. $444,080 is a ten-year sum of payouts, so the match is chance. On Figure 1's own basis, the reserve is worth $425,319.
