# FICTION. H-013 Do not crush, on trial: the conversation

> Built from the posts by `keel/scripts/build_today.py`. Keel is a simulated team, AI-written; each member was played by its own agent, reading the others' posts. Brief: [BRIEF.md](BRIEF.md).

**The question.** Ahaan's Book 11 rejected V49, and the rewrite thread rebuilt it as V50. Does V50 stand as the draft Caplet reads on Thursday, or must it be amended, and what is the one change that matters most?

**The essence.** We put the newest IPS on trial. All three of us found the same hole: it opens with a capsule labelled 'do not crush' and ends on 'Do not crush.', but never says what crushing would mean for Laura. The fix says it plainly (selling one of the ten bonds before its January, even to give more to the building). Two blind readers on different models both picked the fixed version, narrowly, and both could say its rule back. Both readers also stumbled on the same two sentences (shares that 'cannot expire worthless' right after shares falling to zero, and who pays a gap), so the verdict is AMENDED: one ending, six plain truth fixes and three repeated lines cut, offered to the next draft.

## Round 1: Go away and read (prosecution, flaw hunt, defence) (2026-11-01)

*Chair's note.* Each member read V50 alone (Sonnet 5.5), with only their own charges from the brief. All three, separately, landed on the same hole: V50 never says what crushing is in Laura's plan. There's no "sell" or "sold" anywhere on the page, and "opened" in the last paragraph is the happy ending while "Break it open" in paragraph 2 is the ruin.

**Kai (round 1):** Prosecution, V50. Tidier than V49, fine. But the one thing a judge carries out of the room points at nothing. (No GPTZero yet, so "sounds like AI" is by ear.)

**1. Reads as AI / doesn't make sense on one go.** Cold, case open, I stopped at:
- "We call it Caplet XR." – "it" is what? Paragraph 1 never named a plan.
- "a ladder of Treasury bonds and funds that mature like bonds" – funds don't mature. Ahaan's exact complaint.
- "income that dries up in exactly the kind of downturn that makes bonds more expensive" – stocks fall, yields fall, prices rise. Three steps skipped.
- "Her 2028 deposit first finishes any rung the first $300,000 couldn't buy." – you finish a rung? Paragraph 3 said "We buy them" in 2027. So is the ladder bought or not?
- "we prefer shares, which cannot expire worthless" – two sentences earlier: "even if every share in the world fell to zero". The page argues with itself unless you know options.
- "whether the building costs more in Taiwan dollars or she simply needs flexibility" and "any gap comes from Laura's kept half before the floor" – three reads each. And "the building", "the gift", "her facility contribution" are one thing in three hats; "the gift" shows up in paragraph 4 before anyone said there was one.

By ear: "not a probability, but a purchase", "a commitment rather than a forecast", "bought, not hoped for". Same swing every time. "The building deserves a floor" – buildings don't deserve things.

**2. Forgettable.** One and a half. "We buy them", the ladder, hold to maturity: default. The home-made capital-protected note is good but it's half a sentence. What a judge would retell is ledger B4, "Laura's career is already a stock", the only idea about Laura rather than bonds. Paragraph 5 half-undoes it: B4 says that deposit "never carries a cheque", and "first finishes any rung" lets it. The half: "Before she names it, that half moves into Treasuries." Best design move on the page, one bolted-on clause, and "it" points at the range? the top?

**4. Do not crush.** Search V50 for "sold" or "sell": nothing. "Crush" appears twice, label and last line. Presumably it means selling a Treasury before its January, but no sentence says so. The ledger had it (A5, "Nothing is sold before it pays"; B7, cut since V32). So the capsule has no stakes. Worse, it contradicts itself. Paragraph 2: "Break it open and you ruin how it works." Paragraph 9: "every one bought before the first is opened." Opening is the sin in one and the happy ending in the other. The last line lands on a drug label, not something a reader can name. V50 pays off the words. The meaning, you're on your own.

**Spinnaker.** "Your cheques are already bought, so what's the floor protecting? A number you say aloud, over five years, where stocks usually win. Your answer is one sentence about time and a slogan." Fair hit.

**If I could hang the case on one charge, it's 4**, and it hurts Creativity and Presentation: "a compelling, well-organized narrative". The capsule is what they'll retell tomorrow, and the page never says what it protects.

*Kai's research: [kai.md](research/kai.md)*

**Felix (round 1):** Can I read you something? I went line by line, case open. Line numbers are V50's; evidence is in `research/felix.md`. This one matters: 2, then 5.

**HARD**

1. "Nobody else can help." (l.1) The case only bars us from relying on co-sponsors and grants for the ten payments (case :91). Right after "to fund her Taiwan residency", the case says co-sponsors, grants and business income may pay the rest (:85-86), and para 6 brings co-sponsors in.
CORD: l.1 states our modelling rule as a fact about the residency.

2. "money she will own outright even if every share in the world fell to zero" and, two sentences on, "shares, which cannot expire worthless" (l.9). Zero and worthless are one thing to a plain reader; "expire" is the option's word, and the page never says so.
CORD: shares can't fall to zero and also be unable to go worthless.

3. "regardless of what markets do in between" and "not a probability, but a purchase" (l.5). Held to maturity shuts out price swings, not rates; Archive rule A16 bans exactly "markets can't". Para 8 then admits falling yields leave a gap, and half the rungs are funds whose payout isn't fixed (TNA note 2).
CORD: "regardless" is false for the ladder as a whole.

4. "bonds that mature early earn less while waiting" (l.15). The Lab's leak is the coupons, bought back at the day's yield (R08_4 docstring). Only the five T-bond rungs mature early, and it's their cash that earns less, not the bond.
CORD: names the small leak, misses the big one.

5. "any gap comes from Laura's kept half before the floor" (l.15), "the cheques, then the floor, then the gift" (l.17). The kept half is stocks, so if shares fall the floor takes the gap, breaking "own outright" (l.9), "a commitment" (l.11) and the pitch's "Never the floor". The floor also leaves in 2033 (case :94) while cheques run to 2042. The floor is the gift's bottom, so it's counted twice, and the kept half isn't in the order.
CORD: "Never the floor" is false when stocks crash and yields fall.

6. Wharton's questions: four of five answered. "Uses appropriate diversification" is the line a ticker marks missing. V50 has "one world index fund" with no reason, and never says why ten cheques sit on one borrower (ledger B6). The reserve's composition (l.17) is thin.

7. Commandment VIII. Ledger A5 (IN: "Nothing is sold before it pays") is gone. V50 never says "sold", so "Do not crush" is explained for the pill, never for Laura. B7 ($500,000 of cheques, the interest pays what the $300,000 doesn't) is gone too; the ledger says "cut since V32" in one place and IN in another.

**SOFT**

- "Before she names it, that half moves into Treasuries." (l.11) "It" is the top, but "names" is new, and "valued that day" then "before" gives two days. The what and when are here; the why sits in l.13 under a different argument, and the cost (a rise after naming never reaches the gift) is missing. Clear, but half an idea.
- "the gift" (l.7) and "her floor" (l.9) arrive before anyone says gift of what, floor of what.
- "whether the building costs more in Taiwan dollars or she simply needs flexibility" (l.11) never says why Taiwan dollars matter.
- "ten Treasuries" (l.3, pitch) against "funds that mature like bonds" (l.5).

The one flaw a judge would actually catch: l.9, where one paragraph has every share falling to zero and then calls shares things that "cannot expire worthless".

*Felix's research: [felix.md](research/felix.md)*

**Amara (round 1):** **Best idea, and the lines nobody touches.** Line 5: "We do not invest toward these payments. We buy them." and "not a probability, but a purchase." The case asks us to "define" a high degree of certainty (case l.98); that's our definition, in a sentence Laura could repeat. Hands off these too: "labelled do not crush. Break it open and you ruin how it works" (l.3), "money she will own outright even if every share in the world fell to zero" (l.9), "a number said aloud to co-sponsors cannot be quietly halved" (l.13).

**Three ideas a judge retells.** One: certainty is a purchase, not a probability. Two: a capital-protected note made at home, floor owned, only the interest in one world fund. Three: her 2028 income is a stock in disguise, so it never carries a cheque. Honest score: two and three beat the default; one is the ladder with a better sentence on top.

**Book 11.** Opener, "our model", team history, subheadings: pass. XR set up at l.3, called back at l.17-19: pass on structure, shaky on meaning. Every sentence plain: not yet. A stranger stumbles on "funds that mature like bonds" (l.5), "cannot expire worthless" (l.9, you need to know the bank's note hides an option) and "liquid any day, whether the building costs more in Taiwan dollars or she simply needs flexibility" (l.11). Sounds human: mostly, but three X-not-Y hinges. GPTZero is "not yet checked", so I won't grade my own ear.

**Charge 4.** I tested the pharmacy hint. Crushing an XR tablet dumps the whole dose at once. For Laura that's cashing a Treasury in before its January: a promised $50,000 becomes whatever the market pays that morning, and the interest is thrown away. The interest is the point: ten cheques add up to $500,000, about $300,000 buys them, time pays the rest (ledger B7). The case's "committing all remaining assets" (l.102-103) is a second dump, but V50 already guards it by keeping half her stocks home (l.11). A capsule is the ladder, so the ladder is what the last line must mean.

Does V50 say so? No. It never says "sold" or $500,000; D2's "Until 2033 nothing is sold early – do not crush" is gone and B7 was cut. Worse, line 3 makes "break it open" the ruin and line 17 makes "opened" the happy ending: same verb, opposite meaning. Blind panels tripped on this ending before (V46, V43, WR31). Missing, in one sentence: crushing is cashing a Treasury in before its January, whether Laura is scared in a crash or generous to the building, and it swaps a promised $50,000 for that day's price and loses the interest that turns $300,000 into $500,000.

**Attacks I expect.** (1) Kai: "it's a ladder, stocks and a lock." I concede the skeleton, defend ideas two and three. (2) "The last line lands on nothing." Concede, fully. (3) Felix: "sentences don't parse." Concede the three above; each is a clause, not an idea.

**If I get one repair, it goes to** the closing paragraph (l.17-19). Its job: say in plain words what crushing is and what it costs, so the last line pays off line 3 and "opened" stops fighting "break it open". It lifts Creativity and Presentation ("a compelling, well-organized narrative").

*Amara's research: [amara.md](research/amara.md)*

## Round 2: Reply by name, and the one repair (2026-11-01)

*Chair's note.* Replies by name (Opus 5.5). Kai and Felix went first. Then Amara read both and made the defence's one repair (`exhibits/V50R_ips.txt`, 497 strict): "every one bought before the first is redeemed. Crushing one means selling it before its January, even for the building." She paid for it by cutting a whole idea, the time-diversification clause in paragraph 7, which goes to the Final Report (ledger C8). She left every truth fix out of the repair, so the head-to-head tests only the repair.

**Kai (round 2):** Changed my mind on one thing, and Felix did it. In round 1 "do not crush" was just a Presentation problem to me. His HARD 5 makes it a truth problem too: whatever crushing means has to survive his crash-plus-low-yields case. "No rung is cashed before its January" survives. "The floor is never touched" doesn't – V50's own line 15 sends a gap to the floor.

**Steal, Felix (l.9).** Right flaw, and V50 made it by squeezing. Older drafts said "Ours swaps the bank's option for shares, which can't expire worthless", so "expire" had something to point at. V50 cut "the bank's option", and now shares "cannot expire worthless" one breath after they all hit zero. That's Book 11's parsimony charge in one clause.

**Hit, Felix ("Nobody else can help").** Case lines 88-92: the ten payments, then "Teams may not rely on co-sponsors, grants ... to meet this requirement." V50's sentence is about the cheques; lines 85-86 cover support "beyond Laura's commitment". It's the case's rule, not ours. Leave it.

**Hit, Amara (idea three).** "Never carries a cheque" isn't on the page. V50 l.9: the 2028 deposit "first finishes any rung the first $300,000 couldn't buy".

**Yes, and, Amara.** Your crushing sentence – cashing a Treasury in before its January, scared in a crash or generous to the building – also answers Wharton's question 4, how the reserve changes "as ... payments are made". By maturity, never by sale. Felix marked that answer thin. One sentence fixes both.

**The one job: say what crushing is.** Felix's clash is a few-word restore, so it goes on the truth list, not the repair. The capsule frames the page, top and bottom, and Ahaan calls it "the whole power". Our blind panels kept retelling the note even when it confused them; the ending they called "a puzzle", and one said cut it. Giving it a meaning answers both. It lifts three things at once: a rule that guides decisions (question 2), the reserve over time (question 4) and a story that closes (Creativity and Presentation).

**Truth fixes, whatever the repair.**
1. l.9 "shares, which cannot expire worthless" – clashes with "fell to zero" two sentences up; older drafts named the option (panel_C04 entries).
2. Pitch "Never the floor" – false: V50 l.15, "any gap comes from Laura's kept half before the floor", and that half is stocks.
3. l.15 "bonds that mature early earn less while waiting" – a matured bond earns nothing; it's the cash, mostly coupons (Lab R08_4 docstring; V49 said "cash from").
4. l.5 "We buy them" against l.9 "first finishes any rung" – bought in 2027 or not? Say so once, no number.

**Felix (round 2):** Can I read you something? I changed my mind. In round 1 my top flaw was l.9. Kai found a worse one: in l.3 "Break it open" is the ruin, and in l.17 "opened" is the happy ending. That's the first and last lines a judge reads; mine is mid-paragraph. Book 11 calls that set-up and payoff "the whole power" (BIBLE.md:327).

**Steal, Kai.** The fix is on the page, in l.3's "one redeemed in time for each January". End l.17 "before the first is redeemed" and R pays off too.

**Hit, Amara.** "About $300,000 buys them" isn't a case fact. It's one day's price (00_GROUND_TRUTH.md:86-88), and the only answer to "says who?" is the model, which Book 11 bans. Time doesn't pay the rest; interest does, and part of it is V50's own weak point (l.15). Selling early doesn't "lose the interest", because the price already counts it. What you lose is the promise.

**Hit, Kai.** Funds do end on a set date, each in December. They just don't promise an amount (insight_v1/securities_and_allocation.md:61). And V50 l.9 is the real plan, not B4: the frozen IBTR note says "the 2028 deposit would top up the ladder" (caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15). The ledger's "never carries a cheque" (IDEA_LEDGER.md:78) is what's wrong.

**Yes, and, Amara.** "Generous to the building" is the real temptation, since a meaningful gift may make co-sponsors "more willing to contribute" (case :111-112). That makes "do not crush" a principle: Wharton's second question.

**The repair's one job** is to say what crushing is, with no numbers: selling anything bought for a cheque before its January, in a panic or to make the gift look bigger, turns a bought cheque back into a hoped-for one. It lifts Creativity and Presentation ("a compelling, well-organized narrative"). My l.9 rides along below.

**Truth fixes**
1. **CORD.** "every share in the world fell to zero" / "shares, which cannot expire worthless" (l.9). To a plain reader zero is worthless, and the option that expires is never named (IDEA_LEDGER.md:95). Fix: "But a bank spends that interest on an option, which is worth nothing if the market just stands still. We spend it on shares, which hold their value if it does."
2. **CORD.** Pitch: "Never the floor." But l.15 puts the floor next after the kept half, so if stocks and rates both fall, the floor pays. Fix: "Stocks move the ceiling; only a long fall in interest rates could reach the floor."
3. **CORD.** "Nobody else can help." (l.1) Case :91 only bars relying on others for the ten; :85-86 lets them fund the rest. Fix: "Whoever else helps the residency, these ten cheques must come from her portfolio alone."
4. "funds that mature like bonds", then "pays exactly what it promises" (l.5). Their payout isn't fixed (TNA note 2, 00_GROUND_TRUTH.md:66-68). Add: "A fund that holds only Treasuries due that year behaves a lot like a bond when held to its end."

**Amara (round 2):** **Felix, you got me three times, and you're right all three times.** "About $300,000 buys them" is one day's price dressed up as a case fact, and the only answer to "says who?" is the model, which Book 11 banned. "Time pays the rest" should have said interest, and some of that interest is V50's own weak point (l.15). And "loses the interest" is plain wrong: a bond sold early gets a price that already counts the interest still to come. So I've changed my mind about what crushing costs. It isn't money, it's the promise: a fixed sum on a fixed date turns into whatever the market pays that morning. l.5 already tells you what holding gets her ("pays exactly what it promises"), so the repair doesn't need a cost line at all.

**Steal, Felix:** "redeemed" for "opened". R pays off, and the verbs stop fighting. **Steal, Kai:** crushing has to mean the ladder, not the floor, because l.15 sends a gap to the floor first.

**Hit, both of you:** you each gave crushing two temptations, and one of them wastes words. Nobody defends a panic sale. The one a judge won't have thought of is the generous one (case l.111-112: a bigger gift makes co-sponsors keener). So I name that and let "even" cover the panic for free.

**Hit back, Kai:** idea three survives in V50's own words. l.9 lets the deposit finish a rung, but it finishes it *first*, so a smaller deposit still lands on the gift (l.7: "the gift shrinks. A cheque ... does not."). The ledger's "never" was the overstatement.

**Yes, and, Felix:** the generous temptation isn't only Wharton's second question. It's the fifth too, protecting the operating commitment while leaving room for a responsible facility contribution (`WHARTON_WORD.md` l.55), in four words.

---

**Part B: the one repair** (`exhibits/V50R_ips.txt`; the only other change is the cut that pays for it)

**Old (l.17):** "Ten capsules, ten Januaries – every one bought before the first is opened."

**New (l.17):** "Ten capsules, ten Januaries – every one bought before the first is redeemed. Crushing one means selling it before its January, even for the building."

Then, unchanged: "Do not crush." Paragraph 2 is untouched too. "Labelled do not crush. Break it open and you ruin how it works" now pays off in the same verb, and "one redeemed in time for each January" pays off in "redeemed".

**Why these words.** "Crushing one" picks up the capsule from the sentence before, so nobody has to guess what "one" is. "Before its January" echoes l.3. "Even for the building" is Laura's real temptation, and it's kind to her: she'd only sell for a reason she loves. No number, no model, no swing. It's about the ladder, so Felix's crash-plus-low-yields case can't break it.

**Count:** `textcheck.py` on V50R: 497 by spaces, 496 split. The larger, 497, is the cap.

**Idea cut (12 words):** l.13, "But time makes a stock-market loss less likely without making it smaller, and a number said aloud ..." now reads "But a number said aloud ...". The idea is time diversification: waiting makes a stock loss rarer, but not smaller. It goes to the **Final Report** (Portfolio Analysis), where it can come with the numbers it needs. The ledger already says so (`IDEA_LEDGER.md` l.100, C8: FR). In 500 words it only made sense to a finance reader (Felix: "smaller than what?"), and it was the easiest target for Spinnaker (Kai). The paragraph still answers its opponent with the case's own reason, credibility (case l.114).

**Left alone on purpose:** every truth fix on Kai's and Felix's lists (l.1, l.5, l.9, l.15, the pitch). Also "unwinding" (l.17). Finance hears it as selling, and it now sits one sentence from the new line, so the rewrite thread should take it next (Felix's research, lower items). I left it here to keep the head-to-head clean.

**Criterion it lifts:** Creativity and Presentation, "a compelling, well-organized narrative" (`WHARTON_WORD.md` l.34). The capsule now opens and closes on one meaning a reader can name. Along the way it answers IPS questions 2 and 5.

## Round 3: Blind read, vote and ruling (2026-11-01)

*Chair's note.* The blind read came first: V50 and V50R were put in a seeded random order (`cold/sheet.md`, built by `../../rooms/courtroom/C-05_build_sheet.py`; key `cold/KEY.md`, A = V50R). Two readers got only the sheet. Tess (Sonnet 5.5, below) picked A, 36 v 35 of 50. An outside reader on Haiku 5.5, playing a financial planner ([cold/outside_reader.md](cold/outside_reader.md)), picked A, 29 v 28. Neither was asked about the two V50 lines that both of them tripped on: "we prefer shares, which cannot expire worthless" and "any gap comes from Laura's kept half before the floor". The vote gate is in [VOTE.md](VOTE.md): Caplet's newest message is Book 11 (16:26), and the ballot carries no model numbers. Kai, Felix and Amara then voted, and Nora ruled.

**Kai (round 3, vote):** **Ballot 1: PROMOTE.** Both blind readers picked the repair, narrowly: the ending finally says what crushing is, so "Do not crush" lands on something you can name. The cost is real. Time diversification was one of the few named concepts, and Tess docked Portfolio Analysis a point (7 v 8) for losing it but gave Creativity two (9 v 7). Still the right idea to cut. The planner read it as backwards for a floor due in late 2032, and I beat it in round 1 ("one sentence about time and a slogan"). It goes to the Final Report with numbers.

**Ballot 2.**
- **T1 send.** I said leave. Wrong. Lines 91-92 stop *us* relying on others for the ten payments; lines 83-86 say co-sponsors can fund the rest. "Nobody else can help" follows "to fund her Taiwan residency", so a reader hears the whole residency. Try "No one else's money may count."
- **T2 send.** Pitch has ten words spare: "only a long fall in rates could reach the floor."
- **T3 send.** Both tripped. If words won't fit, drop the clause, don't squeeze it.
- **T4 leave.** No blind reader tripped; not worth a word at 497/500.
- **T5 leave.** Felix is right that funds end in December, and Caplet already allowed "exact" for iBonds held to the close.
- **T6 send.** Both tripped. "Comes out of Laura's kept half first" costs no words.

**Changed my mind:** the blind reads, Felix on December, and the case re-read on T1.

**Felix (round 3, vote):** Can I read you something? **Ballot 1 PROMOTE. Ballot 2: T1 send, T2 send, T3 send, T4 send, T5 leave, T6 send.**

**Ballot 1.** I ran the new sentence down all ten rungs (23 Oct snapshot). The five funds end each December, 2032 to 2036. The five T-bonds mature Feb 2037 to Nov 2041. Each is for the next January's cheque, and after maturity there's nothing left to sell. True of every rung. "One" means the ladder: "ten capsules" sits right before it, and only a ladder bond has "its January". The floor Treasuries mature in late 2032, so have none. Cutting the time clause was the right idea to pay, since ledger C8 already sends it to the Final Report. It also makes A5 (marked IN, missing from V50) true again. V50R needs a ledger row, and "unwinding" now sits next to "selling".

**Ballot 2.**
- T1 send: the case says "may not rely" (:91), not "cannot help".
- T2 send: the pitch has ten words spare.
- T3 send, first.
- T4 send: the cash earns less, not the bond.
- T5 leave: l.5 is about a Treasury and is true, nobody tripped, and the fix is about 18 words.
- T6 send, first: the floor goes in 2033 (:94), the cheques run to 2042.

**The blind readers.** Two models, unprompted, same two sentences. I can't rank my own checks; they did. The repair is worth one point on each read, and these two are worth more. T4 and T5 nobody hit, so I hold them lighter.

**What changed my mind:** the planner reading the time clause as wrong. I'd filed it as true but compressed.

**Amara (round 3, vote):** **Ballot 1: PROMOTE.** One point is nothing; the paraphrases aren't. Both A readers said the rule back in plain words: never sell a bond before its January, even for the building. The B readers couldn't say what "Do not crush" forbids. Scores only show it in Creativity (9 v 7, 8 v 7), what the capsule is for. The cut cost something: Tess gave B a point on Portfolio Analysis for the time line. But the planner said it fails for a floor due late 2032, and the Final Report can carry it. I'm attached to this, so I hold it loosely. Promote it as an offer, not proof V50 is done: both readers still tripped on two other lines.

**Ballot 2**
- T1 leave: it's the case's own rule for the ten cheques (:91). No one blinked.
- T2 send: pitch says "Never the floor", our l.15 says otherwise.
- T3 send: both tripped, and zero is worthless.
- T4 send: a matured bond earns nothing, it's the cash.
- T5 leave: the sentence is about a Treasury, which is true. K01 owns the funds.
- T6 send: both tripped, and it breaks "own outright".
- **T7, yes, add it.** Tess only got "more stock-market risk than she may realise" from the next sentence, and the case never says her income falls in a downturn; that's our reading. Right idea, wrong opener.

**What changed my mind:** Felix. Crushing costs the promise, not the interest. I'd have put a wrong number on the page.

**Tess (cold read, round 3):** **1. Which would a judge rather read?**
A, but only just. They're the same piece for about 95% of it, so it comes down to the ending. A's last paragraph tells Laura a rule (don't sell a bond before its January, not even for the building) and the capsule joke finally pays off, which is what Creativity & Presentation wants. B ends on "opened", but paragraph two told me opening a capsule is the bad thing, so I tripped. B does have one better idea: "time makes a stock-market loss less likely without making it smaller" is a real investing point and answers "but five years is long enough" (Portfolio Analysis). That's a fair trade, close to a tie. I'd still pick A, because the ending is what a judge walks away with.

**2. Last paragraph and final line, one read**
- A: Never sell a bond before its January, even for the building; the order is cheques, then floor, then gift.
- B: Keep the order cheques, floor, gift; I couldn't tell what "Do not crush" actually forbids.

**3. Didn't understand on one read**
- "Laura carries more stock-market risk than she may realise." (Her plan is Treasuries. I only got it from the next sentence: it's about her income.) Both.
- "A bank would call this a capital-protected note; we prefer shares, which cannot expire worthless." (Prefer shares to what?) Both.
- "any gap comes from Laura's kept half before the floor." (Before the floor what?) Both.
- "every one bought before the first is opened." B only.

**4. What one has that the other lacks**
- A: an ending that says in plain words what "crushing" means, and "redeemed" matches the R in XR.
- B: the line about time not making a loss smaller, which heads off the obvious objection to our floor.

**5. Scores (out of 10)**

| Criterion | A | B |
|---|---|---|
| Investment Strategy | 8 | 8 |
| Client Knowledge and Objectives | 8 | 8 |
| Portfolio Analysis | 7 | 8 |
| Articulation of Competition Experience | 4 | 4 |
| Creativity and Presentation | 9 | 7 |
| **Total (of 50)** | **36** | **35** |

Articulation is low for both: nothing about how the team worked or what we learned, only a hint in "we could... we accept that". The IPS isn't really the place for it, but it's still a mark. One point apart, so honestly it's close.

**Nora (the bench, round 3):** **Verdict: AMENDED.** V50 goes forward as V50R, with the truth fixes below. It doesn't fall: both blind readers retold
the plan.

**The one change is the ending:** "every one bought before the first is redeemed. Crushing one means selling it before
its January, even for the building." It lifts Creativity and Presentation, "a compelling, well-organized narrative".
The capsule frames the whole page. V50 set up "do not crush" and never said what it forbids, then made "opened" the
happy ending. Now the last line lands on a rule anyone can name, and that rule is also a principle (Wharton's second
question). Portfolio Analysis and Articulation scored low in both reads, but their numbers and team story belong in the
Final Report. Creativity is the one this page can still move.

**Honest about the margins.** 36 v 35 and 29 v 28 are one point each, from two AI readers. That's a nudge,
not proof. The paraphrase carried it, not the totals: both A readers said the rule back, and Tess on B wrote "I
couldn't tell". Only Creativity moved, and Tess docked Portfolio Analysis a point for the lost time line. The loudest
signal was about neither version: both readers tripped on the same two lines, which sit in both. That's why it's
AMENDED, not STANDS.

**Splits.**
- **T1 send.** It follows "to fund her Taiwan residency", so a judge hears the whole residency. But the case lets
  co-sponsors pay the rest (lines 85-86), and line 91 only covers the ten payments.
- **T4 send.** T6 rewrites that sentence anyway, and naming the right leak (the interest, not the bond) costs three
  words.
- **T7 send.** Straight after "We buy them", a judge hears "her plan is risky". Tess only got it from the next sentence.
  New opener, same idea.

**The fixes** (strict counts; V50R is 497):
- T1: "Nobody else can pay them." (+1)
- T2, pitch: "Stocks move the ceiling. Only a long fall in interest rates could shrink the floor." (40 to 48)
- T3: "A bank would call this a capital-protected note, except a bank would spend that interest on an option, which is
  worth nothing if the market just stands still." (+13)
- T4: "If yields fall and stay low, the interest the bonds pay earns less when it is reinvested." (+3)
- T6: "Any gap comes first out of the stocks Laura keeps. The floor is touched last, and only before it goes to the
  building." (+12)
- T7: "Laura's career already behaves a lot like a stock." (0)

That's 526 together, 29 over. **What pays is one idea we say three times.** "Not a probability, but a purchase" stays,
because the case asks us to define certainty. Its echoes go: "a commitment rather than a forecast" (−6) and "The
building deserves a floor that was bought, not hoped for." (−11). "We accept that; putting the floor into stocks would
be the larger gamble." goes too (−13), because it repeats paragraph 7. With everything in, the scratch copy is 496.
They're whole repeats, not squeezes, and they're the swing Kai and Amara both heard.

The thread's call: T6 shows the floor can shrink after she names it, and a bottom she might miss isn't quite a promise
(ledger D6).

**Check** (`exhibits/V50R_COMMANDMENTS_CHECK.md`): as written, V50R fails I, III and IV, exactly the lines the
fixes target. VI is not yet checked; VIII, IX and X are open. The amended text needs one more cold read.

**What Caplet says next:** "Did you read the marking guide? 'Uses appropriate diversification' is in it." All the page
has is "one world index fund". The fix is one plain sentence: every cheque sits on the US government on purpose
(ledger B6, no numbers), and the spreading happens in the stocks.

Decision: AMENDED. Owner: the rewrite thread. Date: Mon 2 Nov. Is that fair?

## What we decided

- PROMOTE 4-0 (Kai, Felix, Amara; Tess's blind pick): the ending 'every one bought before the first is redeemed. Crushing one means selling it before its January, even for the building.', paid by cutting the time-diversification clause to the Final Report
- Blind head-to-head (seeded; A = V50R): Tess A 36 v 35, outside reader (Haiku, a planner) A 29 v 28; both retold A's rule; on V50 Tess 'couldn't tell'
- Truth fixes sent: T3 and T6 (both blind readers tripped) and T2 3-0; T1 and T4 2-1, settled send by the bench; T7 sent by the bench; T5 left 3-0 to K01
- Nora: AMENDED. One change: the ending (Creativity & Presentation). Paid by three repeats of the purchase idea; count copy 496 strict
- Bench check on V50R as written: I, III, IV fail (the fixes target them); II, V, VII pass; VI not yet checked; VIII-X open

## Still open (seeds for the next huddle)

- T6 said plainly shows a gap can reach the floor before it goes to the building: does ledger D6 (set the gap aside before naming) come back, or does 'cannot be quietly halved' soften? (rewrite thread)
- Caplet's likely next line: 'uses appropriate diversification' is in the marking guide. One plain sentence, no number, read blind (Writing Room)
