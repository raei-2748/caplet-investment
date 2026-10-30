# Cold read and commandments check, V33 (D13). Written by a reader who did not write the draft, 30 Oct 2026. AI-generated (Claude Code).

Files read: D13 `pitch.txt` (48 words by `wc`) and `ips.txt` (492 words by `wc`, dashes included), the client case, `WHARTON_WORD.md`, the Ten Commandments section of `BIBLE.md`, `COMMANDMENTS_CHECK.md`, `DETECTOR_LOG.md`, and `judges/panel_V32/` (rankings.json, KEY.json, plus judge5_scores.md, because rankings.json has no judge 5). I did not read the idea ledger, the voice guide or any earlier draft.

**Verdict: FAIL on rows IV, V, VI and VIII. Rows I, II, III, VII and IX pass (IX only on inherited V32 evidence). Row X is Keel's. The draft does not go to Caplet until IV, V and VIII are fixed and VI has a score.**

---

## Job 1. Cold read of the IPS (Commandment IV)

I read the IPS once, top to bottom, as a busy judge would. Paraphrase first, then what tripped me.

**Paragraph 1 ("Laura has made her residency one promise...")**
- Says: Laura owes ten $50,000 payments every January 2033-2042, funded only from this portfolio, and she hopes to give a gift for the building; the two need different kinds of money, so the plan keeps them apart.
- Flags: "Laura has made her residency one promise" is garbled. First read it sounds like the residency made a promise, or she promised the residency something. "Cheque" is not introduced as the word for a $50,000 payment until paragraph 2 uses it.

**Paragraph 2 ("We started where most investors would...")**
- Says: Our first plan was three-quarters stocks; we modelled it and it missed a payment about one future in thirty, because she owes ten one-year bills and a crash in the wrong year forces a sale at the bottom.
- Flags: "where most investors would" is an unsourced claim about other people. "One future in thirty" is a fair number ("we modelled it"), but I could not tell how many futures, what return assumptions, or what "missed a cheque" counts (just the ten payments, or the gift too). That last point matters in paragraph 7.

**Paragraph 3 ("So we call it Caplet XR...")**
- Says: The name Caplet XR is a pharmacy joke (extended release: same dose on schedule), and also X for ten, R for redemption.
- Flags: "So we call it" has no "so" to follow. The strategy has not been described yet, so the name arrives before the thing it names. I followed it, but "redemption" is never connected to anything later.

**Paragraph 4 ("Her first $300,000 buys all ten cheques...")**
- Says: In January 2027 the first $300,000 buys Treasury bonds and "iBond Treasury funds", each maturing before the January it pays.
- Flags: "iBond Treasury funds" is jargon and is never explained. A judge who knows the case but not iShares iBonds will stop here. "Ladder" is introduced here by apposition, which is acceptable. The case says $300,000 pays in January 2027; the draft doesn't say whether $300,000 is all spent or how much is left over. I assumed a small slack.

**Paragraph 5 ("So what does a high degree of certainty mean?...")**
- Says: A payment can fail only if the US government defaults, or if yields fall two points before we buy and the 2028 deposit is under about $85,000; the one weak spot is coupons being reinvested at lower yields, which we price and set aside in 2031.
- Flags (this is the paragraph I could least follow):
  - Why does a yield drop matter? It matters because lower yields make the ladder cost more than $300,000. The draft never says so; the reader has to know bond pricing.
  - "Before we buy": we buy in January 2027, so how long a window is this? Unclear.
  - "$85,000" is meaningless without the $150,000 it is a shortfall against. The draft never states the deposit size in the IPS.
  - "Set the money aside in 2031": aside from what pot, and how much? "Before she names anything" is clear only if you remember 2031 is when she names the range.
  - "Two points", "$85,000": no source in the sentence (see row V).
  - The "leak" metaphor is fine once you have the coupon idea, but coupons haven't been introduced as a thing the ladder pays out and reinvests.

**Paragraph 6 ("Laura is willing to take thoughtful risks...")**
- Says: Laura has already taken her big risk (the residency), and her income from advances, speaking and licensing shrinks in the same recessions that make bonds expensive, so the 2028 deposit should never be what a payment depends on; it fills a gap in the ladder, then builds her gift.
- Flags: This is the best client insight in the draft, but the last two sentences are confusing. "Her 2028 deposit never carries a cheque. It plugs any gap in the ladder" sounds like a contradiction on first read: paragraph 5 says a payment can fail if the deposit is under $85,000, so the deposit does carry payments in the bad case. I resolved it as "the deposit is the backstop, never the plan", but I had to resolve it. "Dear" for expensive is idiomatic British and slows a reader down.

**Paragraph 7 ("Most of it buys a floor...")**
- Says: Most of the 2028 deposit buys Treasuries maturing late 2032, sized to grow back to the whole amount; the interest they earn (about a fifteenth of all she owns) goes into a world index fund, like a bank's capital-protected note without the bank; a balanced 60/40 would usually leave her richer but breaks a promise about one time in four.
- Flags:
  - "Floor" is introduced here and explained by what it does, fine. But "sized to grow back to the whole remainder": remainder of what? I guessed "whatever is left of the 2028 deposit after plugging the ladder".
  - "About a fifteenth of everything she owns": a fifteenth of the portfolio at what date? No source.
  - "Capital-protected note" is named, not defined; a smart non-finance judge will follow the "minus the bank and its fee" image, which is good.
  - **Contradiction a judge will notice:** paragraph 2 says 75% stocks misses a payment about one in thirty; paragraph 7 says 60/40 "breaks a promise ... about one time in four". Less equity, more breaks? The metrics differ ("a cheque, or the gift it named" versus a payment) but the draft doesn't say so, and one in four against one in thirty reads as an error. This is the single biggest comprehension risk.

**Paragraph 8 ("In 2031 Laura gives co-sponsors a range...")**
- Says: In 2031 she tells co-sponsors a range: the bottom is the floor she owns, the top adds half her stocks, and the other half stays with her in case the building costs more.
- Flags: Clear. "Dearer building" is again British-idiomatic. No dollar figures, which Wharton says the IPS doesn't need.

**Paragraph 9 ("A capped range has a catch...")**
- Says: Once a range is public, a stock fall reduces the gift but a rise past the top is Laura's, so on the day she names the range the promised half moves into Treasuries; in our model the gift then reaches its top about 97 times in 100 and the rare miss is about $1,000.
- Flags: Clear and the cleverest paragraph. Two small things: "the gift then reaches its top" needs "the top she named"; and why it isn't 100 times in 100 (the coupon leak, I assume) is never said.

**Paragraph 10 ("From 2033 the ten holdings are the operating reserve...")**
- Says: From 2033 the ladder is the operating reserve and runs itself down, each holding turning to cash before its payment; if anything changes, payments first, then the floor, then the gift.
- Flags: "Operating reserve" is the case's term and is fine for a judge. "Ten holdings" after a ladder of bonds and funds: fine. "You don't crush an XR pill" is the wry line; it works only if you remember paragraph 3. The ordering sentence is good; it is the only statement of a decision rule.

**Wharton's questions not answered by word:** the draft never uses "liquidity", "diversification" or "flexibility", though the IPS instructions ask for how the strategy balances them. Flexibility is implied ("the other half stays hers", "for a dearer building"), liquidity is implied by "each turns to cash before its cheque", diversification is not addressed at all (one stock fund plus Treasuries). Taiwan and inflation do not appear; Wharton does not require them in the IPS.

**The three things a judge would struggle with most**
1. One-in-thirty (75% stocks, paragraph 2) against one-in-four (60/40, paragraph 7) looks like a contradiction and is not explained.
2. The certainty paragraph (5) and "never carries a cheque / plugs any gap" (6): unexplained "two points" and "$85,000" with no deposit size, and the deposit seems both needed and not needed.
3. The floor's mechanics in paragraph 7: "sized to grow back to the whole remainder", "a fifteenth of everything she owns", and "iBond Treasury funds" (paragraph 4) are never defined.

---

## Job 2. Commandments check (V33 / D13)

| # | Commandment | Evidence | Pass? |
|---|---|---|---|
| I | Extraordinary, by our own light | The three ideas I would retell tomorrow: **(1)** "Laura doesn't owe one ten-year bill. She owes ten one-year bills, and a crash in the wrong year forces a sale at the bottom." **(2)** Her 2028 deposit is itself risk, because her income "shrinks in exactly the recessions that make bonds dear" and "The residency is her boldest bet", so the money she has buys the promise and the money she expects carries the hope. **(3)** "A capped range has a catch": once named, falls come off the gift and rises go to Laura, so "on the day she names it, the half she promised moves into Treasuries". Bonus: "It's a bank's capital-protected note, minus the bank and its fee." None of the three is the field's default (ladder plus stocks plus lock); ideas 1 and 3 are the reasoning behind the default pieces, idea 2 is not in the case at all. No comparison with other teams ("We started where most investors would" compares with investors, not teams, but see row IV). The pitch holds up the same way ("one promise ... one hope"). | PASS |
| II | Wharton's word is the only marking scheme | The V32 judges' files (the nearest evidence) score each entry on the five criteria and argue from them (judge1_scores.md, judge5_scores.md "Investment Strategy 9/10, Client Knowledge 9/10 ..."). My own read against the criteria: Investment Strategy, thesis is clear (promise vs hope) and time horizons are explicit (2027, 2028, 2031, 2033); diversification is weak (never addressed). Client Knowledge is the draft's strongest point (career income as equity-like; "willing to take thoughtful risks, but she has already taken the big one"). Portfolio Analysis has the right kind of numbers but gives no assumptions. Articulation is thin: the only team event is the failed 75% plan (paragraph 2). Creativity is high (XR, the lock at naming). Against the IPS's questions: central idea yes; principles yes (last sentence, "cheques first, then the floor, then the hope"); balance of growth, liquidity, flexibility is implicit only (no such words); changes as needs approach yes (2031, 2033); protects the commitment while leaving room for a gift yes. | PASS (with the gaps listed) |
| III | Write like us | Build-then-land: "It's a bank's capital-protected note, minus the bank and its fee." (follows a long, loaded sentence about floors and interest). Concession + but: "Laura is willing to take thoughtful risks, but she has already taken the big one." and "In our model a balanced 60/40 portfolio usually leaves her richer, but breaks a promise ..." (lower-case "but" both times; no sentence-initial "But"). Wry line: "Nothing is sold before it pays – you don't crush an XR pill –". Real event: "We started where most investors would: three-quarters in stocks. Then we modelled it, and our plan missed a cheque in about one future in thirty." (matches the repo's record of the team's own 75% plan failing). Contractions: "doesn't", "It's", "Once it's", "don't". British spelling: "cheque", "modelled". En dashes present. Flags: the last sentence is a three-step run ("the cheques come first, then the floor, then the hope") that borders on a slogan-triad, and the pitch's "one promise ... one hope" leans the same way; paragraph 7 is a dense, almost fact-sheet sentence run. Read aloud, paragraphs 3 and 9 sound human; paragraphs 5 and 7 sound like a spec. | PASS (flags noted) |
| IV | Clear on one reading | See Job 1. I paraphrased all ten paragraphs but could not follow paragraph 5 on first read (the yield/two-point/$85,000 condition), found "never carries a cheque / plugs any gap" apparently self-contradictory (paragraphs 5 and 6), found the 1-in-30 versus 1-in-4 figures look contradictory (paragraphs 2 and 7), and met "iBond Treasury funds" unexplained (paragraph 4). Paragraph 1's first sentence is ungrammatical on first read. Commandment IV says any miss is rewritten. | FAIL |
| V | Every number explains itself | Table below: of the numbers, several carry no "says who". Missing: "yields drop two points", "about $85,000", "about a fifteenth", and (partly) "60/40" and "three-quarters". The 1-in-30, 1-in-4, 97-in-100 and $1,000 figures carry "we modelled"/"in our model" and pass. | FAIL |
| VI | GPTZero before Caplet | `DETECTOR_LOG.md`: GPTZero's API needs a paid key, the free scanner is blocked by reCAPTCHA in Keel's network, every other detector is blocked, home-made detectors were judged invalid (44% accuracy). The log says each draft is labelled "GPTZero: not yet checked" until Caplet pastes it on gptzero.me (Thursday). No score, no date, no scanned text version exists for D13. The commandment's own fallback (label "not yet checked", say so, never stand in a home-made score) is the honest state; but the row's test needs a score above 50%, and there is none. | FAIL (not yet checked; label it so in the README) |
| VII | Few ideas, at full size | My three-sentence summary after one read: (1) In January 2027 the first $300,000 buys ten Treasury-maturity "cheques" that fall due just before each January payment, and the 2028 deposit is only ever the backstop if that ladder falls short. (2) The rest of the 2028 deposit builds the gift: Treasuries sized to regrow the whole amount by 2032 with only their expected interest in a world stock fund, so the bank-style capital protection is Laura's own. (3) In 2031 she names a range (bottom = the floor, top = floor + half the stocks) and on that day the promised half goes into Treasuries; from 2033 the ladder is the operating reserve and runs itself down, payments first. The strategy is statable in three sentences; the draft argues about four big ideas and one clever naming. | PASS |
| VIII | Lose no idea; critique borrowed ones | **Ledger check not done:** `IDEA_LEDGER.md` was not among my files, so I cannot confirm that no idea was lost. What I can see in the draft: costs and blind spots are stated for most concepts. The 75% stocks plan: "missed a cheque in about one future in thirty". The ladder: "one leak - coupons reinvested at lower yields". The floor-plus-interest note: "a balanced 60/40 portfolio usually leaves her richer, but breaks a promise". The lock at naming: "the rare miss is about $1,000". Not stated: the cost of the lock (it gives up the stock upside on the promised half) and the cost of the 2028 deposit never carrying a payment (a smaller early gift). | FAIL (ledger half unverifiable from these files; in-draft costs mostly pass) |
| IX | Judges who actually disagree | **Evidence is for V32, not V33.** This panel judged the previous draft V32 (and H21, A09, RV30, V31, V25), so it shows the panel's disagreement, not how D13 reads. rankings.json lists five judges (1, 2, 3, 4, 6; judge 5 is missing). Mean pairwise Kendall tau over those five: **0.17** (10 pairs; range -0.20 to 0.87). Adding judge 5, recovered from judge5_scores.md and KEY.json (ranking V32, RV30, V25, V31, H21, A09): mean tau **0.23** (15 pairs). Spread of #1 picks: H21 (judge 1), A09 (judge 2), V32 (judges 3, 4, 6, and judge 5) = three different winners among six judges, with V32 ranked first by four and second by two. Judges disagree substantially (low tau), but all of them put V32 first or second, so the panel agrees about V32 even though it disagrees about the field. V33 has not been paneled. | PASS (V32 evidence; V33 unpaneled) |
| X | Improve without being asked | For Keel to fill. | n/a (Keel) |

### Row V detail: every number in the draft, with its "says who"

| Number (where) | Says who (in the draft's own words) |
|---|---|
| $50,000 every January, ten years (pitch; para 1) | No "says who" in the draft; it is the case's number, but the draft never writes "the case says". Acceptable as a client fact, but unlabelled. |
| 2033 to 2042 (para 1) | Same: the case's dates, unlabelled. |
| "three-quarters in stocks" (para 2) | "We started where most investors would" (the team's own first plan; "most investors" is an unsourced generalisation). |
| "about one future in thirty" (para 2) | "Then we modelled it". Passes. |
| "ten one-year bills" (para 2) | Derived from the case's ten payments; no source stated. |
| $300,000, January 2027 (para 4) | The case's numbers; unlabelled, as above. |
| "two points" (para 5) | **No source.** Not "we modelled", not "we assume". |
| "about $85,000" (para 5) | **No source.** Also no deposit size ($150,000) in the draft to measure it against. |
| 2028 deposit (paras 5, 6, 7) | Case's date; amount never stated. |
| 2031 (paras 5, 8, 9) | Case's date. |
| "late in 2032" (para 7) | A design choice stated as a fact; no source needed, but no reason given. |
| "about a fifteenth of everything she owns" (para 7) | **No source.** The draft says "should earn" but not "we calculate", and does not say the date or base. |
| "60/40" (para 7) | "In our model a balanced 60/40 portfolio ..." Passes for source; the comparison portfolio is the team's choice. |
| "about one time in four" (para 7) | "In our model". Passes, but conflicts visibly with "one in thirty". |
| "half her stocks" / "the other half" / "the half she promised" (paras 8, 9) | A design choice; no source given or needed. |
| "about 97 times in 100" (para 9) | "In our model". Passes. |
| "about $1,000" (para 9) | "In our model". Passes. |
| 2033 (para 10) | Case's date. |
| Pitch: "$50,000 every January for ten years" | Case's number, unlabelled. |

---

## One-line note for Keel on fixes that clear the FAIL rows
- IV and V: add one sentence stating why yields matter to ladder cost, the $150,000, and "we modelled" on the two-points/$85,000 and fifteenth figures; tell the reader why 1-in-30 and 1-in-4 are different measures (or align them); define "iBond Treasury funds" in six words; fix paragraph 1's first sentence.
- VI: Caplet runs gptzero.me; record score, date and text version.
- VIII: check the ledger rows and state the cost of the lock.
