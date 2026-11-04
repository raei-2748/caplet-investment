# Writing Room, Wed 4 Nov: three first-time readers on the FINAL (495 strict)

AI DRAFT (Claude, 4 Nov 2026). (Keel is a simulated team, AI-written.) Readers are simulated strangers (fresh agents
that saw no Keel file), so they are tests, never quotes. Key sealed first: `KEY_sealed.md` (commit 23d3ef3). Text:
`FINAL_as_read.txt` + `FINAL_pitch_as_read.txt`, the FINAL on main after PR #132.

| Reader | Prior | Model |
|---|---|---|
| A | Year 11 student, never studied finance, reads once | Haiku 5.5 |
| B | Retail-bank financial adviser, ten years, reads critically | Sonnet 5.5 |
| C | Business professional judging a pile of entries, reads at speed | Opus 5.5 |

## Tally against the sealed key

| Q | Asked by | A | B | C | Result |
|---|---|---|---|---|---|
| Q1 first $300,000 and why | control | pass | pass | pass | 3/3 |
| Q2 how a ladder that pays what it promised can fall short | Writing Room | pass ("the reinvestment, not a holding failing to pay") | pass (guesses the price assumed a reinvestment rate) | pass (but "at speed this felt odd" beside P3) | 3/3 |
| Q3a "as if every dollar waiting for a cheque earned nothing" said back | Library | pass ("any money waiting for a future cheque earns zero") | pass ("any money sitting idle until its cheque is due ... 0%") | pass ("any cash sitting around before it is needed for a cheque earns zero") | 3/3 |
| Q3b a fund's December payout, weeks before its January cheque | Library | No: pass | No: pass | No: pass | 3/3 |
| Q3c 2034 interest for the 2040 cheque | Library | No: pass | No: pass | No: pass | 3/3 |
| Q4 can an announced range be cut later? | Laura's Room | unsure: "can't quietly be halved", so guesses it could be lowered openly | pass (guess: "meant to be fixed") | pass ("any lowering happens before she names the range") | 2/3 |
| Q5 can the bottom fall below the floor? | Laura's Room | "only by rounding" (not the claim) | No (fail on the claim) | Yes, if the gap beats her spare shares (pass) | 1/3: card, not IPS (as sealed) |
| Q6 does she give everything left to the building? | Laura's Room | No: pass | No: pass | No: pass | 3/3 |
| Q7 her income when shares fall / recover | Window | falls / not said, guesses it returns | falls / not said, guesses it recovers | falls / not said, guesses it recovers | recorded: 3 of 3 read the fall; 3 of 3 guess the recovery the pages deny |

**Bar (sealed): a fail by two of three on Q2-Q6, or one contradiction named by two, becomes a hard issue.** None does.
Q5 fails as Kai predicted, but the IPS spends no words on the bottom, so it stays on the cards.

## Q8: sentences read twice
| Sentence | A | B | C |
|---|---|---|---|
| P5 "Banks sell this as a capital-protected note, but they spend the interest on an option that can expire worthless." | | what "this" is | what "this" is and what the option has to do with it |
| P7 "Her spare money shrinks first, and if it can't cover the gap, she names a lower range." | | what "spare money" is, and the order of cuts | |
| P7 "... and move that much from her kept shares into Treasuries." | what "that much" is | | |
| P4 "time makes a loss rarer, not smaller" | a pause | | |
| P2 "Crushing one means selling it before it matures, even for the building." | | | whether it means "never, not even for the building" |

Two of three stopped on the bank sentence's "this" (the Long Room's skimmer did too on 2 Nov). Under the bar it is
a reader note, not a hard issue: Caplet's rewrite should name the mix ("the floor and the shares") in its own words.

## Q9: contradictions named
| Reader | Named | Holds? |
|---|---|---|
| A | P4 "shouldn't bet on shares twice" beside P5 putting the rest of the 2028 money into a world fund | Not a contradiction (the cheques' money holds no shares; the fund is the gift's top), but a first-time reader can't see it. One reader: card |
| A | "A Treasury bond held to maturity pays exactly what it promised", but the ladder also holds funds | True as written (the Window chose "bond" on purpose, to match the TNA). Look-alike card row already covers it |
| B | pitch "only the interest" v IPS "roughly the interest"; P3's promise v P7's shortfall | B resolves both itself: "essentially no" |
| C | P3 "no payment depends on shares" v P7 moving her kept shares into Treasuries to cover the gap | Not a contradiction: if the shares can't cover it, the gift does ("she names a lower range"), so a cheque never waits on shares. But the IPS leaves the reader to infer it. One reader: Final Report |
| C | P3 "never needs rebalancing" v P7 "counts on reinvesting" | Rebalancing isn't reinvesting; Q2 shows C understood the mechanism |

Only one pairing came up twice in any form (P3's promise beside P7's shortfall, B and C), and both readers explained it
in Q2. No hard issue.

## Raw answers (verbatim)

### Reader A (Year 11 student, Haiku 5.5)
- Q1. The plan uses the first $300,000 to buy a ladder of Treasuries, one maturing before each January cheque from 2033. The text says her cheques are promises, so the money is set aside up front, and a Treasury held to maturity pays exactly what it promised, so no cheque depends on shares.
- Q2. Each holding pays what it promised, but the plan assumes the interest the holdings pay before each cheque is reinvested at a good rate. If rates fall and stay low, that reinvested interest earns less than planned, so the total may not cover the later cheques. The problem is the reinvestment, not a holding failing to pay.
- Q3a. When working out the shortfall, we assume that any money waiting for a future cheque earns zero interest. That is the worst case the plan tests against.
- Q3b. No. The money is waiting for the January cheque, so under the rule it counts as earning nothing in those weeks.
- Q3c. No. Interest paid in 2034 is waiting for the 2040 cheque, so under the rule it earns nothing from 2034 until 2040.
- Q4. The text doesn't say outright whether the range can ever be lowered. It says a number said aloud "can't quietly be halved after a bad year", so it should not be cut quietly. Guess: a lower range could be announced openly, but the text does not cover that.
- Q5. Yes, but only by rounding. The bottom is the floor "rounded down", so it can sit a little below the floor fund's value. The text doesn't say how much, and it can never be higher than the floor.
- Q6. No. Only part of what is left goes to the building: the floor and the top of the range draw on it, and "the other half stays hers and liquid". From 2033 the ladder and the money set aside become her operating reserve for the cheques.
- Q7. The text says her income (book advances, speaking fees, licensing) "can dry up in the same downturns that hit share prices", so her income may fall when shares fall. The text doesn't say what happens to her income when share prices recover. Guess: it would return as the market recovers, but this is not stated.
- Q8. (a) "Shares are called safe over ten years, but time makes a loss rarer, not smaller, and a fixed cheque can't wait for a recovery." I needed a pause on "rarer, not smaller". (b) "Before Laura names her range, we price that shortfall as if every dollar waiting for a cheque earned nothing, and move that much from her kept shares into Treasuries." I had to work out what "that much" refers to.
- Q9. Yes, one tension. The text says "her portfolio shouldn't bet on shares twice" because her 2028 deposit depends on income that falls with shares. But the plan then puts what remains of the 2028 deposit into "one world index fund holding thousands of companies". A first-time reader cannot see why that is not betting on shares twice. Also, the plan says a bond held to maturity pays exactly what it promised, but the ladder also includes Treasury funds, which the text does not say pay exactly as promised.

### Reader B (bank financial adviser, Sonnet 5.5)
- Q1. It buys a ladder of Treasury bonds and Treasury funds in January 2027, each maturing before one of the ten January payments (2033-2042). The aim is that no payment depends on shares: a Treasury held to maturity pays what it promised, so the payments get "high certainty".
- Q2. The text says it counts on reinvesting the bonds' interest. Coupons paid years before a cheque is due have to be reinvested, and if rates fall and stay low they earn less than assumed. The ladder then ends up short. My guess is that the purchase price was set assuming some reinvestment rate, since the text doesn't say.
- Q3a. Be pessimistic about the interest. Any money sitting idle until its cheque is due is assumed to earn 0%. They then measure how much is missing under that assumption.
- Q3b. No. Under a strict reading, money held while waiting for a cheque earns zero. A few weeks in December is the same situation, just shorter. (The text doesn't spell out this edge case, so this is a guess at how they would treat it.)
- Q3c. No. That interest is waiting from 2034 to 2040, so it counts as earning nothing for those six years.
- Q4. The text doesn't say outright. It implies yes in a sense. The top is lowered only before she names it ("she names a lower range"), and the half of the shares moved to Treasuries is there so the number "can't quietly be halved after a bad year". So once named, the range is meant to be fixed. My guess is that it can't be cut later.
- Q5. No. The bottom is the floor fund "rounded down", and it is money she already owns. The only adjustment described is the shortfall, which comes out of her kept shares first and then lowers the range. It is unclear whether a big shortfall could cut the bottom below the floor. My guess is that it could not.
- Q6. No. Only part goes to the building. Half her shares sit in the top of the range, and the other half stays hers and liquid as a cushion. The floor is the minimum gift, and the rest is hers. After 2033 the ladder and the set-aside money become her operating reserve.
- Q7. The text doesn't say. Her income comes from book advances, speaking fees and licensing, and the text says these "can dry up in the same downturns that hit share prices". So income is likely to fall when shares fall. It says nothing about income when shares recover. My guess is that income would probably recover too.
- Q8. "Banks sell this as a capital-protected note, but they spend the interest on an option that can expire worthless." I had to work out that "this" refers to the floor-plus-index-fund structure. Also: "Her spare money shrinks first, and if it can't cover the gap, she names a lower range." It is not clear what "spare money" is (the kept shares?) or how the order of cuts works.
- Q9. Possibly a mild one. The pitch says "only the interest those would earn goes into world shares", but the plan says "Most of the rest buys a Treasury fund... What remains, roughly the interest" goes into shares. "Roughly" versus "only" is a small difference. Also the plan says "no payment depends on shares" but then says the top of the range adds half her shares. That concerns the gift, not the payments, so it isn't a real contradiction. Also, "A Treasury bond held to maturity pays exactly what it promised" sits awkwardly beside "the ladder... can fall short", but the reinvestment explanation resolves it. So essentially no.

### Reader C (competition judge at speed, Opus 5.5)
- Q1. The first $300,000 buys a "ladder" of Treasury bonds and fixed-end Treasury funds, each one maturing just before one of the ten January $50,000 payments from 2033 to 2042. The reason is that the payments are fixed promises, and a Treasury held to maturity pays what it promised whatever markets do, so no payment depends on shares.
- Q2. Each bond pays interest along the way, and that cash has to be reinvested until its cheque is due. The plan seems to count on those reinvested coupons earning a certain rate. If rates fall and stay low, the reinvested money earns less, and the total comes up short. (At speed this felt odd next to "one bond per payment, hold it, pays exactly what it promised.")
- Q3a. When working out the possible gap, they assume that any cash sitting around before it is needed for a cheque earns zero interest until it is paid out. It is a worst-case assumption for the reinvestment problem.
- Q3b. No. The money is waiting a few weeks for the January cheque, so under that rule it counts as earning nothing.
- Q3c. No. That interest is waiting from 2034 for the 2040 cheque, so under the rule it counts as earning nothing for all six years.
- Q4. No, or at least the plan is built so that it shouldn't be. Before Laura names the top, half her shares move into Treasuries, "because a number said aloud can't quietly be halved after a bad year." Any lowering happens before she names the range, not after.
- Q5. Yes, it seems so. The bottom is "the floor, rounded down", so it sits at or just under the floor fund's value. Also, if the reinvestment shortfall is bigger than her spare shares, "she names a lower range". That suggests the bottom could drop below the floor fund, presumably because some floor money goes to cover the ladder's gap. The text doesn't say this outright.
- Q6. No. The top of the range adds only half her shares; the other half "stays hers and liquid" as a cushion in case the building costs more in Taiwan dollars. Any money left in the ladder after the cheques isn't clearly given to the building either.
- Q7. When share prices fall, her income (book advances, speaking fees, licensing) can dry up too, because it is hit by the same downturns. When prices recover, the text doesn't say. Guess: her income probably recovers along with the market.
- Q8. "Banks sell this as a capital-protected note, but they spend the interest on an option that can expire worthless." I had to re-read it to work out what "this" pointed to (the floor fund plus shares) and what the option has to do with it. I also re-read "Crushing one means selling it before it matures, even for the building." It wasn't clear at first whether "even for the building" means they would never sell one, even to pay for the building.
- Q9. Yes, there is a tension. Paragraph 3 says: "A Treasury bond held to maturity pays exactly what it promised, whatever markets do. So, to us, high certainty means no payment depends on shares." Paragraph 7 says the ladder "can fall short" if rates fall, and the fix is to "move that much from her kept shares into Treasuries." So covering a payment gap can depend on shares after all. A milder one: paragraph 3 praises "buying one bond per payment and holding it ... which never needs rebalancing", but paragraph 7 says the ladder "counts on reinvesting its bonds' interest."
