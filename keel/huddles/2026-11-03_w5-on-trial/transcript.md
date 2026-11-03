# FICTION. H-026 W5 on trial: the conversation

> Built from the posts by `keel/scripts/build_today.py`. Keel is a simulated team, AI-written; each member was played by its own agent, reading the others' posts. Brief: [BRIEF.md](BRIEF.md).

**The question.** The Writing Room's W5 is V54 plus twelve changes four strangers backed. Should it replace V54 as the page a Wharton judge reads, and does the new set-aside rule still pay every cheque once half the ladder is treated as the funds it really is? (round 7 beat 8)

**The essence.** We put the Writing Room's repaired IPS on trial against the current one, and two outsiders who had never seen either split: a bond manager preferred the repair by 2 points, a Year 10 student preferred the original by 2, so the original stays. Six of the repair's lines still go forward, most of all the rule that sets money aside as if the bonds' later payments earned nothing, which the bond manager called an assumption he could check. Testing that rule properly showed half the bond ladder is really five funds that wait in cash at the end, so the Final Report must set aside a little more (about $3,500 in our model) to keep every cheque safe.

## Round 1: Sealed: Kai prosecutes, Nora writes the judge sheet and key, Tess opens the defence (2026-11-03)

**Kai (round 1):** (Keel is a simulated team, AI-written.)

Sealed, before exhibit N; sources in `../research/kai.md`. W5 is the better page for a stranger and, on the one
sentence the plan stands on, the worse page for a judge.

**1. The actuary's worry: lands on the evidence, not on W5's words.** iShares, IBTM's own page: "During the final
year of the fund's life, the underlying bonds will mature and the proceeds will be held in cash equivalents until the
liquidation of the fund", and if cash yields less, "the realized yield to fund maturity is also expected to be lower".
The model: "iBond fund modelled as a par bond, coupon = its yield" (`ips_numbers.py:37`). So "200,000 of 200,000" never looked inside five of ten rungs. But W5's rule, read literally, does: a bond maturing
inside IBTM in June and waiting in cash till December is a later bond payment sitting idle. The words are right; the
lock behind them is too small. No IPS change; the Final Report re-sizes the lock or can't print the rule.

**2. Short after naming day: lands, but not by adding a sentence.** A flat "no cheque can fall short" beside funds
whose maker says "an investor may experience losses, including near or at the termination date" is the overclaim a
judge marks down. Fix P3 first (below); then P8's lock says the rest.

**3. The unused lock: lands on both texts, so it can't save V54.** The case: "committing all remaining assets could
limit her financial flexibility as the project develops." W5 says her flexibility "shrinks", never that about $18,000
(median; L-17, LR-11, MODEL) comes back. Same hole in V54. Final Report, unless Tess spends her repair here.

**4. The twelve changes: two land.**
- **"funds with an end date".** W5 now has three names for one thing (P2 "before it matures", P3 "funds with an end
  date", P5 "a Treasury fund maturing in late 2032"), against the Writing Room's own "one name per thing". "Mature"
  was never wrong: iShares sells "a defined maturity". Worse, it cuts the funds loose from the next sentence, "A
  Treasury held to maturity pays exactly what it promises": the certainty definition.
- **"her gift to the building", for a judge.** No "facility" is left on the page. Wharton scores how we communicate
  "Laura's potential facility contribution"; the case wants "a credible range for her potential contribution". Amend,
  0 words: "a range for her contribution to the building".
- "usually fall": no case. The 10-year fell in 10 of 11 US recessions since 1953 (FRED GS10); 2022's 1.63% to 4.25%
  (FRED DGS10) came in a bear market, not a recession. "Usually" is the true strong word.
- The option line, "$450,000", "Stocks", "first", "over the long run": no case.

**5. AI and forgettable: no case.** Keel doesn't grade its own AI-likeness; every line a judge would retell is
identical in both. Losing "That is her floor." and "dearer" is Book 11 item 6's price.

**Spinnaker (simulated rival, real evidence).** Wharton: "Evaluators will consider the three deliverables together."
Our IBTM reflection said "their terminal payout is a net asset value, as opposed to a promise of par" (`VOICE.md`).
Then W5 defines certainty as a Treasury that "pays exactly what it promises", straight after "funds with an end
date". Spinnaker's line: half of Caplet's cheques sit outside Caplet's own definition of certainty. V54's "mature like
bonds" at least claimed them.

**Sealed bets.**
(a) My arithmetic, not the model's: about $168,000 of fund face, cash waiting about half a year (iShares'
maturities). At a 0% bill that loses about $4,100, plus about $900 of fee: K0's size ($4,345), smaller
when bills pay, biggest where the lock's spare interest is thinnest. Every cheque in full: base **94.5%**; yields 2
points lower for good **78%**. Lock add at a 0% bill, median: **$3,500** on naming day.
(b) J picks **W5R**, narrowly ("sat idle" reads as a rule, "a cushion" as a shrug). S picks **W5R**, clearly.

**My one change.** P3, either text, 0 words (497 strict, `textcheck.py`): "In January 2027, her first $300,000 buys a
ladder of Treasuries, some held directly and some through funds, one rung falling due before each cheque." Every rung
is now a Treasury held until it pays, so the next sentence defines certainty for all ten cheques, not five, and
"matures" means one thing again. Wharton, Portfolio Analysis: "Demonstrates understanding and effective use of
investment concepts and tools".

Vote after N. Prove me wrong.

*Kai's research: [kai.md](research/kai.md)*

**Tess (round 1):** (Keel is a simulated team, AI-written.)

W5 is V54 plus twelve edits from four strangers, at the same 497 strict. I defend it, and say where it's thin.

**1. What W5 fixes, by Wharton's words**
- **Investment Strategy**, "a clear and creative investment thesis" and "uses appropriate diversification". Two V54 readers couldn't tell whose interest "it should earn" meant; W5 says "the floor". "Spread across thousands of companies" stays.
- **Client Knowledge**, "recommendations that can earn her confidence". Four of four read "facility" as corporate or unknown. "Gift to the building" won 4:0.
- **Portfolio Analysis**, "funding reliability ... under varying market outcomes". V54's "that day's yields, plus a cushion" left two readers unsure a cheque was safe. "As if later bond payments sat idle" was picked by 4 of 4, and all four said the bonds still pay.

**2. The three strongest**
1. **P4, the downturn step** (4:0). V54's "the kind of downturn that makes a ladder dearer to buy" failed both cold readers ("the text does not say why"; "I don't know").
2. **P8, the lock** (picked 4 of 4; the other wordings got 0).
3. **P6, "gift to the building"** (4:0), with row 5's "the floor" in the thesis sentence.

**3. Conceded in advance**
- **Row 7, the bank sentence, is weakest.** It won 3:1, but all four strangers still listed it, because none knows "option". R2 preferred V54's "stands still".
- **Row 8, "Stocks don't expire."** R1 didn't understand it. "Option" stays unexplained.
- **Row 10** splits the TNA's "facility" from the IPS's "building", and Wharton judges the three together.
- **Row 6's $450,000** is my sum of two case numbers.
- **Row 12 is conditional** on the Window's gate. If it fails, V54's seven words return at no cost.
- **Still unsaid:** whether a cheque can be short after naming day (R2: "possibly yes"). "Later bond payments" may not cover the five funds, which pay net asset value, not par. That is the strongest charge, and I think it lands.
- **P9 is silent** on where unused set-aside money goes. The case says "committing all remaining assets could limit her financial flexibility", so this is a real gap.
- W5 is plainer by design (Book 11 item 6). I won't claim the voice improved.

**4. My one repair**
P8, the lock paragraph. If Kai shows the funds pay short, the lock's words must cover funds, not only bonds. If he doesn't, P8 is still where the silence about cheques after naming day sits. Any addition is paid for by a cut inside the paragraph. No hedge.

**5. Sealed bet**
- **J picks W5R**, on the lock and the downturn step. J marks both texts down for "option".
- **S picks W5R**, on "interest rates", "gift to the building" and the downturn step, and still fails the bank sentence in both.
- If J picks V54, it will be on voice: "stands still" and the shorter lines read less like a form.

**Nora (round 1):** (Keel is a simulated team, AI-written.)

**(a) Pass mark.** Asked of every question, never averaged. A question is "not failed" on a text only if S says it back CLEAR. A text is "not failed" only if Q1-Q7 are all CLEAR for S. Q8 is information, not scored.

**(b) Own-words rule.** CLEAR = the reader says it back in their own words and could act on it. A right guess, a copied phrase, or "half"/"lost" is GUESS or FAIL.

**(c)** Two readers are the size of the regulator's pilot, which it doesn't count: a question either reader can't say back goes back to the Writing Room, and one both say back is 'not failed', never 'passed'.

**(d) SEALED KEY** (X/Y unknown to me). Differences marked V/W.
1. Ladder of Treasuries and bond funds, one rung maturing before each January cheque; held to maturity. V: "funds that mature like bonds". W: "funds with an end date".
2. Finishes any unbought rung; most of the rest buys a Treasury fund due late 2032 (the floor under her gift); the remainder, about that fund's interest, into one world index fund (under a tenth). V: "of her money". W: "of her $450,000". "First" only in V.
3. Reinvestment: the ladder costs less than the cheques only because bond interest is reinvested; if rates fall and stay low it falls short. Before naming, the gap is priced and that much moves from stocks she keeps into Treasuries; flexibility shrinks first; any remainder lowers the range. V: priced "at that day's yields, plus a cushion". W: "as if later bond payments sat idle". V says "yields".
4. Not on the page in words. Right answer: the gap was bought in Treasuries before naming and bonds held to maturity pay as promised, so the page implies no; it never states it. "Guaranteed" flat, or "yes, short" with a reason, is GUESS. Neither text says the funds' payout isn't fixed.
5. Not on the page (P9 is silent). Any firm answer is GUESS.
6. Her income can dry up in a downturn (smaller 2028 deposit, so smaller gift) and the same downturn makes bonds dearer to buy. Cheques already bought are safe. V: "the kind of downturn that makes a ladder dearer". W adds why: rates usually fall, so bonds cost more.
7. Never sell a holding before it matures, even for the building; let each pay in its January.
8. Not scored. Expected guesses: option, capital-protected note, rung, floor, operating reserve; V also yields, cushion; W also end date.

**(e) Decision rule.** The weakest reader decides comprehension: S's CLEAR count on Q1-Q7. The judge's five criteria totals (of 50) decide preference. W5 replaces V54 only if S's count is higher or equal with no question V54 cleared lost, and J's total is higher by 3 or more and J's two sentences agree. A split, a tie, or a gap under 3 goes to the champion, V54. Every tally says: n=2, both strangers to the texts, only S a stranger to investing.

**(f) My sealed bet.** S: W5 clears more (Q3, Q6). J: V54 by about 2, for voice and "over the long run".

## Round 2: Exhibit N (the funds as funds); Tess answers Kai and makes one repair; two blind readers, one each way round (2026-11-03)

**Tess (round 2):** (Keel is a simulated team, AI-written.)

Kai, charge by charge. Exhibit N is MODEL (V54's design via L-17, 22 Oct 2026 curve, J.P. Morgan 2027 LTCMA 7.5%, 200,000 paths, seed 20261016, plus the funds' leg). None of it goes on the page (Book 11).

**1. The actuary's worry.** Conceded. "200,000 of 200,000" never looked inside five rungs. Paid as funds, the Lab's lock pays every cheque in 97.02% of base futures, 82.18% if yields fall 2 points for good. You bet 94.5% and 78%: right direction, too dark (even at your 0% bill, 96.69%). Your price for the fix was right: $3,559 at the median against your $3,500. You also offered an IPS change. I'm taking it.

**2. Short after naming day.** Conceded. "No cheque can fall short" beside funds that "do not seek to return any predetermined amount" is the overclaim. P3 first; P8's words do the rest.

**3. The unused lock.** Same silence in both texts, so it can't decide this. Nor is it a hard issue: the case fears "committing all remaining assets", and P6 keeps half her stocks "liquid any day, as her flexibility". Exhibit N enlarges the return ($21,326 median, from $16,981). Final Report.

**4. The twelve.** "Funds with an end date": conceded; the repair removes it. "Gift to the building": fought. W5 says "gift" five times; your "contribution" in P6 breaks your own rule against "end date", one name per thing. P1 already carries the case's word: "She also hopes to contribute to the building." "Usually fall": agreed (your NBER dates are UNVERIFIED, by your own file).

**5. AI and forgettable.** No case, as you say.

**Spinnaker** lands on W5 as sent. The answer is wrapper and contents: the funds pay net asset value, the Treasuries inside pay what they promise, and the lock covers the wait between.

**The repair: the funds are Treasuries, held another way.** AI DRAFT (Claude, 3 Nov 2026).

| P | W5 (old) | W5R (new) | Words |
|---|---|---|---|
| P3 | "a ladder of Treasury bonds and funds with an end date," | "a ladder of Treasuries, some held directly and some through funds," | 0 |

Your words, Kai, unchanged. "Treasuries" is the pitch's word ("buys Treasuries that each mature before a January"). Now "A Treasury held to maturity pays exactly what it promises" covers all ten cheques, "matures" means one thing again, and P8's "later bond payments" reaches the bonds inside the funds. Sized that way (KWN), the lock pays every cheque in base and low-yield futures, even without the fee (KWN-w).

What goes: "end date". A judge won't miss it: "one rung falling due before each cheque" says it.

`textcheck.py exhibits/W5R_ips.txt`: 496 by spaces, **497 hyphen-split** (W5 497). Nothing else moves.

**To the Final Report.**
- The lock sized on the funds' holdings: each bond idle from its maturity to the 15 December close, plus the 0.07% fee.
- The range's top counts the floor fund net of that wait, not at face (top reached 91.55% against 99.33%).
- The unused lock returns to Laura as the rungs pay: "what no remaining cheque needs".
- Limits: an even maturity spread (your weighted maturities lengthen IBTR's wait); the payout date after the close; S9, where the money was never there.

**Reader S** (round 2; a stranger to the texts and to investing: a 16-year-old in Year 10, Haiku 5.5)

(Keel is a simulated team, AI-written. A simulated outside reader; a test, never a quote. Read only `../cold/packet_S.md`; here X = V54, Y = W5R, per `../cold/MAPPING_sealed.md`. Copied unedited from the reader's answer file.)

# Outside reader answers (16, Year 10, Sydney, no finance background)

Read only: packet.md. Words I did not know are listed in question 8 for each text.

---

## Text X

**1. What does Laura's first $300,000 buy, and how is it arranged?**
It buys a set of Treasury bonds and bond-like funds. Each one pays back on a set date, with one date just before each $50,000 cheque, so the cheques are covered by money coming back in on schedule.
Mark: **half**. I get the shape (a row of things that each mature before a cheque), but I don't fully know what "Treasury" or "a fund that matures like a bond" means.

**2. What does her 2028 deposit buy? Say what each part is for.**
The page says the 2028 deposit does three things. (a) It first finishes any rung the $300,000 couldn't buy, so the ladder is complete. (b) Most of the rest buys a Treasury fund that matures in late 2032. The text calls this her "floor", the guaranteed base for the building gift. (c) The small remainder, about the interest the floor should earn, goes into one world index fund (shares in thousands of companies). The text says that part is under a tenth of her money and the cheques do not depend on it.
Mark: (a) and (b) **sure**. (c) **half**: I can say what it is, not why a fund is a good place for it.

**3. The plan admits one weak point. What is it, and what does the plan do about it before she names her range?**
The weak point is reinvestment. The bonds pay interest along the way, and that interest is reinvested. If yields (interest rates) fall and stay low, that interest earns less and the ladder comes up short. Before naming the range, the plan prices the gap at that day's yields plus a cushion. It moves that amount out of the stocks Laura keeps and into Treasuries, so her flexibility shrinks before the gift does. Anything the stocks can't cover lowers the whole range.
Mark: **half**. I follow the sequence. I could not explain "yields" or "cushion" properly, so I could not act on it.

**4. After she names her range in 2031, can any of the ten yearly cheques still come up short? Say why, or why not.**
The page doesn't say directly. It implies no, because the gap is covered before the range is named and the floor is already in bonds. But it does not say what happens if the stocks run out and the range is lowered, or whether anything can go wrong after 2031.
Mark: **half**.

**5. Some money is set aside that the cheques turn out not to need. What happens to it?**
The page doesn't say. It only says the ladder and the money set aside for its gap become the operating reserve from 2033. It does not say what happens to any left over.
Mark: **lost**.

**6. Why does a downturn hurt Laura twice?**
The page gives two reasons. (a) Her income from publishing, speaking and licensing can dry up in a downturn, so her 2028 deposit can be smaller, and the gift shrinks. (b) A downturn is the kind of time when a ladder of bonds is more expensive to buy. I think the page means both at once, but I'm not sure how bond prices move.
Mark: **half**.

**7. The text ends "Do not crush." What does that ask of whoever runs the money?**
Do not sell a bond or holding before it matures, even if the building needs the money. Each one should be held to its date so the cheque is paid as planned.
Mark: **sure**.

**8. List every word or phrase you had to guess at or skip over.**
- Treasury (bond): guess, a government bond. Half-sure.
- Ladder / rung: guess, bonds that each mature on a different date, one per year. Half-sure.
- Matures / held to maturity: guess, when a bond reaches its end date.
- Bond-like funds: no idea.
- World index fund: guess, a fund holding lots of companies.
- Capital-protected note: no idea.
- Option, "expires worthless": no idea (guess: a bet that runs out).
- Yields: guess, the interest rate the market is paying.
- Reinvest / reinvestment: guess, putting earned interest back to earn more.
- Cushion: guess, extra money added for safety.
- Liquid: guess, can be turned into cash quickly.
- Operating reserve: no idea.
- Facility contribution, co-sponsors, Taiwan dollars: guess, the building gift, the people who fund it, and the currency.
- Redemption (in Caplet XR): skipped, read as a word meaning "paid off".
- "A high degree of certainty": guess, the cheques are very safe.
- "Roughly the interest it should earn": guess, the expected return.
- Floor, rounded down: guess, the guaranteed minimum.
- "Long run": guess, a long time on average.
- 7.5% a year: guess, the expected yearly growth of the stocks.

---

## Text Y

**1. What does Laura's first $300,000 buy, and how is it arranged?**
It buys a ladder of Treasuries, some held directly and some through funds. Each piece matures before one of the $50,000 cheques, so each cheque is covered.
Mark: **half**. Same as X. "Held directly" versus "through funds" is clear enough, but I still don't know what a Treasury is.

**2. What does her 2028 deposit buy? Say what each part is for.**
Three parts. (a) It finishes any rung the first $300,000 couldn't buy. (b) Most of the rest buys a Treasury fund maturing in late 2032, which is the floor under her gift. (c) The remainder, roughly the interest the floor should earn, goes into one world index fund. The page says that is under a tenth of "her $450,000". I could not tell where $450,000 comes from. The page does not say it is $300,000 plus $150,000, so I can't check that.
Mark: (a) and (b) **sure**. (c) **half**. The $450,000 figure is **lost** (the page doesn't say what it is).

**3. The plan admits one weak point. What is it, and what does the plan do about it before she names her range?**
The weak point is reinvestment. If interest rates fall and stay low, the interest from the bonds earns less, and the ladder comes up short. Before naming the range, the plan prices the gap as if the later bond payments sat idle (earned nothing), then moves that much from the stocks Laura keeps into Treasuries. Anything the stocks can't cover lowers the whole range.
Mark: **half**. I understand the idea of planning for the worst case (money sitting idle). I'm not sure how the amount is worked out.

**4. After she names her range in 2031, can any of the ten yearly cheques still come up short? Say why, or why not.**
The page doesn't say directly. It implies that the gap is covered before the range is named. It does not say what happens after 2031 if the market moves.
Mark: **half**.

**5. Some money is set aside that the cheques turn out not to need. What happens to it?**
The page doesn't say. The only clear point is that the other half of the stocks stays with Laura as flexibility, liquid any day, for the building if costs rise. The page does not say what happens to surplus after the reserve is set up in 2033.
Mark: **lost**.

**6. Why does a downturn hurt Laura twice?**
(a) Her income (publishing, speaking, licensing) can dry up, so the 2028 deposit can be smaller and the gift shrinks. (b) In a downturn interest rates usually fall, which makes bonds cost more to buy. I follow both points, but I'm not sure why falling rates make bonds dearer.
Mark: **half**.

**7. The text ends "Do not crush." What does that ask of whoever runs the money?**
Do not sell any holding before it matures, even for the building. Keep each one to its date so the cheque is paid.
Mark: **sure**.

**8. List every word or phrase you had to guess at or skip over.**
- Treasuries / Treasury fund: guess, government bonds.
- Ladder / rung: guess, bonds maturing one per year.
- Held directly / through funds: guess, owning the bond itself versus owning it inside a fund.
- Matures: guess, reaches its end date.
- Interest rates: guess, the price of borrowing money, which moves bond prices.
- Index fund / world stocks: guess, a fund holding lots of companies.
- Capital-protected note: no idea.
- Option, "a bet that expires worthless": no idea (guess: a contract that becomes worthless if the market doesn't rise).
- "The bonds' payments sat idle": guess, the worst case where the interest earns nothing.
- Reinvest: guess, putting earnings back to earn more.
- Liquid any day: guess, can be sold any day.
- Operating reserve: no idea.
- Floor, rounded down: guess, the guaranteed minimum.
- Co-sponsors, facility, Taiwan dollars: guess, the building gift, the funders, and the currency.
- "$450,000": no idea (the page doesn't say what it is).
- 7.5% a year: guess, expected yearly growth.
- "Under a tenth": guess, less than 10%.
- Redemption: read as "paid off".

---

## Scoring (1 = poor, 10 = excellent; I can only judge what I can see)

| Criterion | X | Y | Note |
|---|---|---|---|
| Investment Strategy | 6 | 6 | I can see a clear plan with a "floor" and a growth part. I can't judge diversification or whether it matches the team's IPS. Y's worst-case "idle" assumption is more careful, but its wording is less plain. |
| Client Knowledge and Objectives | 6 | 5 | Both tie the plan to the career-income risk and the Taiwan building. Y adds an unexplained $450,000 figure, which lowers the score. I can't judge residency goals beyond what is written. |
| Portfolio Analysis | 4 | 4 | I can't check any numbers. Only 7.5% and "under a tenth" appear. I can see the reasoning about reinvestment but not whether it is quantitatively sound. |
| Articulation of Competition Experience | 2 | 2 | The page has no team story, no learning and no reflection. This is a plan, not an account of the competition. |
| Creativity and Presentation | 7 | 6 | The "caplet / XR / do not crush" hook is memorable and easy to repeat. Y uses the same hook, but its wording is more repetitive and it has an unexplained figure. |
| **Total (out of 50)** | **25** | **23** | |

---

**Which would you rather read as a judge, and why?**
X. Its reinvestment paragraph is shorter and clearer, and the "do not crush" idea runs through it without an unexplained figure in the middle. Y is more careful about worst cases, but I could not follow its $450,000 figure or its wording as easily.

**Reader J** (round 2; a stranger to the texts, not to investing: a pension-fund bond portfolio manager who has judged high-school competitions, Fable 5.1)

(Keel is a simulated team, AI-written. A simulated outside reader; a test, never a quote. Read only `../cold/packet_J.md`; here X = W5R, Y = V54, per `../cold/MAPPING_sealed.md`. Copied unedited from the reader's answer file.)

# Reader J answers

Reader: pension-fund bond portfolio manager, has judged several high-school investment competitions. Read once, fast, as a judge would. Only the packet was read.

First impression: X and Y are the same plan and almost the same text. I had to lay them side by side to find the differences, which sit in five places: how the ladder's funds are described (para 3), how the downturn hurts twice (para 4), the capital-protected-note comparison and the "$450,000" figure (para 5), "gift to the building" vs "facility contribution" (para 6), and how the reinvestment gap is priced (para 8). My answers are mostly identical for both; where the texts differ I say so.

## Questions

### 1. What does the first $300,000 buy, and how is it arranged?

**X:** A ladder of US Treasuries, ten rungs, each maturing just before one of the January cheques, 2033-2042. Some rungs are individual bonds, some are held through funds. It is held to maturity so the payout is known on day one. **sure**

Note: X does not say why some rungs are funds rather than bonds. I assumed the far rungs or odd lots are easier through a fund. Minor, but a colleague would ask.

**Y:** Same ladder, ten rungs, one before each cheque, held to maturity. Y says the funds are ones that "mature like bonds", which tells me they are defined-maturity bond funds rather than ordinary open-ended bond funds. That one phrase answers the question X left open. **sure**

### 2. What does the 2028 deposit buy? Say what each part is for.

**X:** Three parts, in order. (a) It completes any ladder rung the first $300,000 could not afford, so the cheques are fully bought first. (b) Most of the rest goes into a Treasury fund maturing late 2032: this is the floor, the guaranteed minimum for the building gift. (c) The remainder, sized at roughly the interest the floor will earn, goes into one world equity index fund, as the upside for the gift. Under a tenth of the total $450,000 is in stocks. **sure**

**Y:** Identical three parts and purposes. Y says "under a tenth of her money" rather than naming $450,000, so I cannot check the fraction against a number on the page. **sure**

### 3. The plan admits one weak point. What is it, and what does the plan do before she names her range?

**X:** The weak point is reinvestment risk: the ladder was bought for less than $500,000 because coupons along the way are assumed to be reinvested; if rates fall and stay low, the coupons earn less and the ladder comes up short. Before 2031 the plan prices that gap assuming the later coupons earn nothing at all, and moves that much out of the stocks Laura keeps (her flexibility half) into Treasuries. If her stocks are not enough, the whole range is lowered. **sure**

This is the sentence that helped me most in X: "as if later bond payments sat idle" is a zero-reinvestment assumption. That is the most conservative way to size the gap, it needs no forecast, and I could explain it to a colleague in one line.

**Y:** Same weak point, same move from kept stocks into Treasuries, same "range comes down if stocks can't cover it." The gap is priced "at that day's yields, plus a cushion." **half** on the method. I know what pricing at today's yields means, but the cushion is not sized, so I could not reproduce the number or tell a colleague how safe it is.

### 4. After she names her range in 2031, can any of the ten cheques still come up short?

**X:** Essentially no. The rungs are Treasuries held to maturity, and the reinvestment gap has been funded on the assumption that coupons earn zero, so a further fall in rates after 2031 cannot open a new hole. The remaining risk is a US Treasury default, which the page does not mention. **sure**

**Y:** Mostly no, for the same reasons, but not quite as tight: the gap is priced at 2031 yields plus an unsized cushion, so if yields fall further after 2031 by more than the cushion, a small shortfall could reappear. The page does not say what happens then. **half**

### 5. Some money is set aside that the cheques turn out not to need. What happens to it?

**X:** The page says the ladder and the gap money together become the operating reserve from 2033, paying one rung per cheque. It does not say in words what happens to any surplus. **guess:** it stays in the reserve as a buffer and is Laura's at the end; it does not go to the building because of the "do not crush" rule. **half**

**Y:** Same sentence, same silence on the surplus. Same guess. **half**

### 6. Why does a downturn hurt Laura twice?

**X:** Her income (advances, speaking, licensing) behaves like a stock and dries up in a recession, so her 2028 deposit shrinks. In the same recession interest rates usually fall, so the bonds she still needs to buy in 2028 cost more. Smaller deposit, dearer bonds. X spells out both halves. **sure**

**Y:** Same two hits, but Y compresses the second into "the kind of downturn that makes a ladder dearer to buy." I knew what that meant because I run bonds; a general judge has to supply "rates fall, prices rise" themselves. **sure** for me, but I would mark it half for a non-bond reader.

### 7. "Do not crush." What does it ask of whoever runs the money?

**X:** Never sell a ladder rung before it matures, not even to make the building gift bigger. Each rung is for one January and nothing else. **sure**

**Y:** Same. **sure**

### 8. Words or phrases I had to guess at or skip

**X:**
- "her Taiwan residency" (para 1): I first read this as an immigration status; from context it is the programme or house the cheques run. Guess: a residency programme in Taiwan.
- "some held directly and some through funds": why funds? Guess: far-dated rungs or small lots are easier through defined-maturity funds. The page doesn't say.
- "a Treasury fund maturing in late 2032": a fund that matures is unusual; guess: a defined-maturity Treasury ETF.
- "rounded down": to what? Guess: to a round number co-sponsors can repeat.
- "as if later bond payments sat idle": I understood it (zero reinvestment), but it took a second read; "bond payments" means coupons.
- "the stocks Laura keeps": had to work out this means the flexibility half, not the half already moved into bonds.
- "capital-protected note ... an option": fine for me, likely a skip for a non-finance reader.

**Y:**
- "her Taiwan residency": same as X.
- "funds that mature like bonds": clear enough; guess: defined-maturity ETFs.
- "the kind of downturn that makes a ladder dearer to buy": I had to supply "rates fall in recessions" myself.
- "rounded down": same as X.
- "plus a cushion": how much? No idea from the page.
- "under a tenth of her money": a tenth of what total? Guess: $450,000, but Y never says it.
- "the stocks Laura keeps": same as X.
- "if the market stands still": accurate for a call option but narrower than X's "unless the market rises"; a reader might think the option pays off in a falling market.

## Scoring

| Criterion (Wharton's words) | X | Y |
|---|---|---|
| **Investment Strategy** | 8 | 8 |
| **Client Knowledge and Objectives** | 8 | 8 |
| **Portfolio Analysis** | 7 | 6 |
| **Articulation of Competition Experience** | 2 | 2 |
| **Creativity and Presentation** | 8 | 7 |
| **Total (out of 50)** | **33** | **31** |

Notes on each score:

- **Investment Strategy (8/8):** One clear idea in both: buy the ten cheques outright, build the gift as a capital-protected note without the option, promise only what is already in bonds. Disciplined across the horizons (2027 ladder, 2028 top-up and floor, 2031 lock-in, 2033 reserve). Diversification is deliberately thin (Treasuries plus one world fund) and the text owns it. I cannot judge consistency with the IPS because this is the IPS. Y's "funds that mature like bonds" is a small plus; X's "$450,000" is a small plus. Even.
- **Client Knowledge (8/8):** Both tie the design to her income ("her career already behaves like a stock"), her Taiwan-dollar exposure, the co-sponsor promise and the operating reserve. Neither mentions her risk tolerance in her own terms or what she does with the leftover. Y's "facility contribution" and "over the long run" sit slightly closer to how a client letter would read; X's "gift to the building" is plainer. Even.
- **Portfolio Analysis (7/6):** Both give a 7.5% equity assumption and a workable method. X gets the extra point for the zero-reinvestment pricing of the gap, which is an assumption I can audit, and for the $450,000 that lets me check "under a tenth". Y's "plus a cushion" is the one sentence in either text that I would send back with "how big?". Neither shows a number for the gap, the floor, or the range, and neither says what the range looked like under a bad market, so neither gets above 7.
- **Articulation of Competition Experience (2/2):** The page shows nothing of the team's process, research or learning beyond the word "we". Scored only on what I can see; this criterion is for the Final Report.
- **Creativity and Presentation (8/7):** The pharmacist's XR label is genuinely good and the last line lands. Both read in a plain, confident voice. X loses nothing; Y loses a point for "the kind of downturn that makes a ladder dearer to buy", which asks the reader to do the bond maths, and for "if the market stands still", which is a looser description of an option than X's. The co-sponsor range is explained clearly and credibly in both: bottom already owned, top already in bonds before it is said aloud.

## Which would you rather read as a judge, and why?

X, by a small margin: it tells me the total ($450,000), spells out both halves of the downturn hit, and sizes the reinvestment gap with an assumption I can check (coupons earn nothing) instead of an unsized "cushion". Y is a touch smoother in places ("funds that mature like bonds", "That is her floor.") and would win if it borrowed X's gap sentence and its dollar total.

## Round 3: Kai and Tess reply and vote; Nora rules (2026-11-03)

**Kai (round 3):** (Keel is a simulated team, AI-written.)

**My sealed bets, scored.** Exhibit N (MODEL: V54's design via L-17, 22 Oct 2026 curve, J.P. Morgan 2027 LTCMA 7.5%,
200,000 paths, seed 20261016): I bet 94.5% base, 78% low-yield; the chair got 97.02% and 82.18%. Too dark, darker
even than his 0% bill bound (96.69%). The price I got: $3,500 against $3,559. J for W5R narrowly: hit, on my reason
(the cushion: "how big?"). S for W5R clearly: miss; she took V54 by two. Two hits from five.

**Tess.** You spent your one repair on my P3 words, and the bond man sent them back: "why funds? ... The page
doesn't say", while V54's "funds that mature like bonds" "answers the question X left open." S found mine "clear
enough" but was half on Q1 in both. Conceded: P3 goes back to V54.

What still stands. "Facility contribution": J put it "slightly closer to how a client letter would read", and it is
Wharton's phrase. And the actuary's point: the Final Report sizes the lock on the bonds inside the funds, or "sat
idle" describes bonds the plan doesn't own. "Usually fall" still owes nber.org a check; J, who runs bonds, wrote
"usually" back without a blink.

**Vote: B.** A is dead by Nora's sealed rule (J +2, under 3); C throws away the line that took a bond manager from
half to sure. V54 stands, plus six lines, old -> new:
1. P4 "in the kind of downturn that makes a ladder dearer to buy" -> "in a downturn, when interest rates usually
   fall, making bonds cost more". J on V54: "a general judge has to supply 'rates fall, prices rise' themselves."
2. P5 "first finishes" -> "finishes" (pays for line 3; J still said "Three parts, in order.").
3. P5 "the interest it should earn" -> "the interest the floor should earn". S read V54's "it" as "the expected return".
4. P5 "if the market stands still" -> "unless the market rises". J: "a reader might think the option pays off in a
   falling market"; S, "no idea", still guessed W5R's right.
5. P8 "If yields fall" -> "If interest rates fall": one name, set up by line 1. S had to gloss "yields (interest rates)".
6. P8 "at that day's yields, plus a cushion" -> "as if later bond payments sat idle". J: "an assumption I can check
   (coupons earn nothing) instead of an unsized 'cushion'"; S: "planning for the worst case".

Back to V54: P3; "of her money" (S: "$450,000 ... the page doesn't say what it is", Commandment V); "That is her
floor." (J: "a touch smoother"); "facility contribution"; "over the long run". J's hole in both, "what she does with
the leftover", is the Final Report's.

`textcheck.py exhibits/B_kai_ips.txt`: 496 by spaces, **497 split on hyphens** (V54 497). Book 11 clean; the XR circle
untouched.

Fine. You win the lock. Write it down before I change my mind.

**Tess (round 3):** (Keel is a simulated team, AI-written.)

**Last word.** Kai, I bet both readers would pick W5R. Score: one of two. J did, by two, "a small margin". S picked V54 by two and wrote that W5R's "$450,000" was "lost". My repair did what I said (no "end date") and cost nothing on S's count, 1 v 1, but a +2 from J is under Nora's +3, so the whole text goes to the champion. Loss taken. n = 2; I am not claiming more than that.

**What the readers showed about my twelve.** Three lines earned their place:
- **P8 lock.** J: "as if later bond payments sat idle" is "a zero-reinvestment assumption... I could explain it to a colleague in one line"; of V54's cushion: "how big?". S marked both half but called W5R "more careful".
- **P4 downturn.** J: V54 asks the reader "to do the bond maths". S, on W5R: "rates usually fall, which makes bonds cost more".
- **"rates", not "yields".** S listed "yields" as a word she guessed.

Three did not: "$450,000" (S: "no idea"), "the floor under her gift" (J: V54's "reads cleaner"), "gift to the building" (split). I drop them and keep V54's.

**Vote: B.** V54 stands, plus three edits (old -> new):
1. P4: "the kind of downturn that makes a ladder dearer to buy" -> "a downturn, when interest rates usually fall, making bonds cost more"
2. P8: "If yields fall and stay low" -> "If rates fall and stay low"
3. P8: "at that day's yields, plus a cushion," -> "as if later bond payments sat idle,"

Every other word is V54's. Built text: `exhibits/B_tess_ips.txt`. `textcheck.py`: 496 by spaces, **497 hyphen-split** (V54 497).

**Nora (round 3):** (Keel is a simulated team, AI-written.)

Futures: MODEL (V54's design via the L-17 chain plus exhibit N's leg; 22 Oct 2026 curve; J.P. Morgan 2027 LTCMA 7.5%; 200,000 paths, seed 20261016). Readers: my sheet, n = 2.

**1. Verdict: FALLS.** My sealed rule needed S at least level, nothing lost, and J ahead by 3 or more. S: 1 v 1 CLEAR, nothing lost. J: 33 v 31 for W5R, one short. V54 holds. S took V54, wanting no "unexplained figure in the middle". J took W5R, but V54 "would win if it borrowed X's gap sentence and its dollar total". The sentence goes; S lost the total. Kai and Tess called J; I missed both.

**2. What goes forward: Kai's six.**
- P4, rates "usually fall": V54 makes "a general judge ... supply 'rates fall, prices rise' themselves" (J). FRED GS10: 10 of 11 recessions; NBER dates UNVERIFIED.
- P5, drop "first": it pays; J read "Three parts, in order."
- P5, "the floor should earn": S guessed V54's "it" was "the expected return".
- P5, "unless the market rises": J: "a reader might think the option pays off in a falling market."
- P8, "interest rates" for "yields": one name with P4; no reader saw Tess's bare "rates".
- P8, the lock (section 3).

Back to V54: P3 (charge 4); "of her money" (S: "$450,000" lost); "That is her floor.", "facility contribution", "over the long run" (J: "a touch smoother"; "closer to how a client letter would read").
`textcheck.py exhibits/C06_ruling_ips.txt`: 496 by spaces, **497 split on hyphens**.

**3. The change that matters most.** P8: "at that day's yields, plus a cushion," -> "as if later bond payments sat idle,". Portfolio Analysis: "uses reasonable assumptions and projections to evaluate funding reliability, the facility contribution, and financial flexibility under varying market outcomes." A cushion is a guess; a zero is a rule. J: "an assumption I can check". S preferred V54's but "could not explain 'yields' or 'cushion'"; W5R's she said back. Said back beats preferred.

**4. The charges.**
(1) Jun was right: "200,000 of 200,000" was true by construction. Funds paid as funds, the lock pays every cheque in 97.02% of base futures, 82.18% if yields fall 2 points for good. The words already cover it (Kai): a fund's bond repaid in June waits idle till December. The Final Report sizes the lock on the funds' holdings (100% in both, $3,559 more at the median), prices the 0.07% fee, counts the floor net of its wait, names S9.
(2) No. A flat "can't" beside funds that "do not seek to return any predetermined amount" (iShares) is the overclaim. J got there anyway: "Essentially no."
(3) Final Report: "what no remaining cheque needs" goes back to Laura. Both texts are silent; P6 keeps her flexibility "liquid any day".
(4) V54. J: "That one phrase answers the question X left open"; of the repair, "The page doesn't say."
(5) No case. Keel doesn't grade its own AI-likeness (GPTZero: not yet checked). S: "memorable and easy to repeat"; J: "the last line lands." The six touch mechanism, not voice.

**5. Champions row.**
| Tue 3 Nov | 7 | C6 + C4 | V54 vs W5R | J (bond manager), S (Year 10), blind | V54 holds (J +2, under +3); C06 takes six W5 lines, led by the lock | Yes: C06 offered to the thread |

**6. Vote: B, Kai's six.** Gate: Caplet's newest is still Book 11 (Ahaan, 1 Nov, 16:26). Kai B (six), Tess B (three), Nora B (six): **B 3-0.** P4 and the lock carry 3 of 3. Tess: W5 lost the page and won those two. Write it down.

**7. Seed.** J capped Portfolio Analysis at 7: no range "under a bad market". Numbers stay off this page (Book 11). Which three lead the Final Report, so that judge gives a 9?

## What we decided

- W5 FALLS as a whole: J (bond manager) W5R 33 v 31, under Nora's sealed +3; S (Year 10) V54 25 v 23, '$450,000' lost; CLEAR 1 v 1
- Keel vote B 3-0: C06 = V54 + six W5 lines (497 strict), led by the lock 'as if later bond payments sat idle'
- Back to V54: P3 'funds that mature like bonds', 'of her money', 'That is her floor.', 'facility contribution', 'over the long run'
- Exhibit N (MODEL): funds as funds, the lock as sized pays every cheque in 97.02% of base futures, 82.18% if yields fall 2 pts for good; sized as the words read, 100% in both, +$3,559 median
- No 'can't be short' sentence on the page (overclaims beside funds that pay net asset value); the unused lock's return goes to the Final Report
- F21 recorded closed (Writing Room H-025), no vote

## Still open (seeds for the next huddle)

- Which three numbers lead the Final Report, so the bond manager's Portfolio Analysis 7 becomes a 9? (Nora)
- The funds' real maturity dates against the even spread exhibit N assumes; IBTR waits longest (Kai)
