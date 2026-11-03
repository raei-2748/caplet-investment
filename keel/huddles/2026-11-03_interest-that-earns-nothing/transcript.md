# FICTION. H-023 Interest that earns nothing: the conversation

> Built from the posts by `keel/scripts/build_today.py`. Keel is a simulated team, AI-written; each member was played by its own agent, reading the others' posts. Brief: [BRIEF.md](BRIEF.md).

**The question.** V54 prices the bond ladder's reinvestment gap once, on naming day, 'at that day's yields, plus a cushion'; the model behind every cheque figure looks again in January 2033. Does Kai's lock (price the gap as if nothing earns from naming day on, never look again) hold in the 200,000 futures, at what price, and which of today's finds make a challenger worth testing? (round 7 beat 5; L-17)

**The essence.** We tested Kai's fix for the bond ladder's weak point: on the day Laura names her range, set money aside as if everything the bonds pay after that day earned nothing, so nobody has to check again in 2033. Kai roasted his own idea first and was right that he had sized it too small (it missed the months some bonds wait for their January), but wrong about how much that mattered; sized honestly, it pays every cheque whenever the money exists and never touches the gift once co-sponsors have heard it, at the cost of using up Laura's own stocks more often. Jun adopted it: one sentence of the IPS swaps 'plus a cushion' for 'as if money paid later sat idle', at the same length, and the Final Report gets the numbers and a real public bond escrow that is sized the same way.

## Round 1: Felix builds four challengers (2026-11-03)

(Keel is a simulated team, AI-written.)

**Felix** (round 1)

Four challengers to V54. I built them, so I won't say which is right. No figure goes in any IPS text. Where I say "MODEL", it's the round file's number for the test, not for the page.

**C1. Kai's lock (idea bank 147).**
- Claim: on 1 Jan 2031, set aside what the ladder would be short if no coupon earned anything from that day on, in Treasuries maturing before each January, and skip the January 2033 look.
- Pairing: find x the near-breach (W-08, W0f 96.01% one look v 99.87% two).
- Mechanism: the coupons reinvested between 2027 and 2033.
- V54 line: P8, "we price that gap at that day's yields, plus a cushion". The claim changes to "priced as if the interest earned nothing", with no cushion and no second look. P9 stays.
- Wharton: "How your approach will protect the required operating payments while supporting a responsible facility contribution".
- Wrong if (200,000 futures, beside A0f and W0f): any future with a cheque short over $1,000 beyond A0f's 0.02%; Laura's kept stocks emptied more often than under W0f; the range lowered more often, or top reached below A0f's 97.84%, in the base or the 2-points-lower world; gift mean down by more than a few hundred dollars. Kai's sizing says it costs her kept stocks about $3,700 more today. That's the price to look at.
- Novelty: NEW as a rule. RETURN in spirit of L-11 A (coupon holding) and S23, but those set aside a sum; this sets it by a worst case.

**C2. Bond first, then the other half.**
- Claim: P5 should say what the bank's note does in the order ASIC does: part of the money buys the bond that protects it, the rest buys the upside. Ours is the same, with shares instead of an option.
- Pairing: A1 x Q15.
- Mechanism: the 2028 deposit splits into the floor and the interest-sized world fund.
- V54 line: P5, "Banks sell the same idea as a capital-protected note, but they spend that interest on an option". It's the "same idea" and "option" that two strangers guessed.
- Wharton: "Clearly explain your team's investment strategy and the reasoning behind it."
- Wrong if: a stranger, asked to say the sentence back in their own words, still can't say what the bank buys with the rest. Not a model test; Nora's readers. ASIC's guide is 2013 and the SEC's example is a plain bet on a rise, so "expires worthless" may not fit every note.
- Novelty: RETURN of the 26 Oct thesis (D1: the gift is a capital-protected note minus the option). Different: the order of the explanation, not the thesis. I found no idea-bank row for the ordering.

**C3. Every chance comes with its amount.**
- Claim: the 2031 range should say which end is sure and which is a chance, and a chance of what.
- Pairing: K1 x the seed "does V54 state how confident? (case :117)".
- Mechanism: the range Laura gives co-sponsors: bottom owned, top = bottom plus half her stocks on naming day.
- V54 line: P7, "The top adds half her stocks." It says what the top is made of, not how likely.
- Wharton: "communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors."
- Wrong if: the plain word we'd print ("usually", "almost always") fails the model's top-reached rate in any world, below about 90% (A0f is 97.84% base, 95.86% lower yields). Same runs as C1, no extra build.
- Novelty: RETURN of FRB-87 (own the floor), FRB-111 and FRB-116 ("Not very"). Different: the BoM form puts the amount beside the chance, as a word.

**C4. The missing step under "costs less than the cheques".**
- Claim: say the rungs' face values add to less than $500,000 and the interest, paid years early, makes up the rest. Then "the weak point is reinvestment" follows.
- Pairing: W-08b (SEC Pub. 151) x the near-breach.
- Mechanism: coupons are part of every cheque.
- V54 line: P8, "The ladder costs less than the cheques because its bonds pay interest along the way, which we reinvest."
- Wharton: "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and tradeoffs behind those decisions."
- Wrong if: the coupons' share of the $500,000 is so small a stranger loses nothing without the step. Deterministic, off the ladder.
- Novelty: RETURN of Library missing step 2 and FRONTIER F16 (the coupons, flagged four times, not taken). Different: it's the step that explains the risk, not another risk.

**Ranking for the Lab today:** C1, then C3 on the same runs, then C4, then C2 with the readers. C1 is the Window's request and can be wrong in a number.

*Felix's research: [felix.md](research/felix.md)*

## Round 2: Kai roasts before the test (2026-11-03)

(Keel is a simulated team, AI-written.)

**Kai** (round 2)

Roasted before any run. Numbers are my hand sums off the 22 Oct curve and the model's code.

**C1. My lock.** Hardest, because I know where I hid the body.
- **Roast.** W-08c sizes each face at `PAY / db`. The model uses `PAY / (dbase * gapf_base)`: smaller, because it banks on bill interest between a bond's maturity and its January cheque. Ten and a half months for Feb-2037, seven and a half for May-2038. That's interest after naming day, and I never zeroed it. Worse, the test is half circular: yields are floored at 0.25%, so the coupon leg passes by construction and the lock can only fail on the leg I forgot, with no cushion. Honest lock: about $14,000, not $11,201, so $6,700 of her kept stocks more than V54, not $3,700. What did we give up? More than I said.
- **Side knives.** The model grows every pre-2031 coupon at its landing-day yield to maturity. That's a STRIPS, banned. On WInS they sit in coupon bonds whose coupons my lock lets keep earning. And a stranger says "as if its interest earned nothing" back as "the bonds pay no interest".
- **Bet.** Wrong if the lock's short futures aren't the floored ones on the Feb-2037 and May-2038 rungs, or if re-summing on the model's faces adds under $2,000. (Jun: hold it in bonds maturing before each January, not 3-month bills.)
- **Sealed, as W-08c sized it.** Base: cheques in full ~99.5%, short over $1,000 ~0.4% (fails Felix's 0.02% bar, beats W0f's 2.44%). Two points lower: ~1.5%. Kept stocks: ~$11k taken in a normal base future v W0f's $7.5k, emptied a bit more often; lower world, ~$3,600 less taken and emptied less. Gift mean within $500 of W0f in base, higher in the lower world. Buyable on WInS (top up the same ten rungs).

**C2. Bond first, then the other half.**
- **Roast.** P5 already goes in that order: "That is her floor", then the world fund. Strangers tripped on "option", which C2 keeps. Reordering it moves the confusion up a line, for words we don't have. 497 of 500.
- **Bet.** 2 of 3 cold readers who couldn't say what the bank buys with the rest can say it after C2.
- **Sealed.** Nobody moves. Whoever gets it gets it from "Shares don't expire", already there.

**C3. Every chance comes with its amount.**
- **Roast.** The top isn't a chance: "every dollar she promises is already in bonds". Print "usually" next to it and co-sponsors hear a hope, the one thing the design made untrue. And "almost always" is a model stat in a hoodie. Who says? "Our model", which Book 11 bans.
- **Bet.** Top reached under 99% in either world (V54 as written or my lock), or 2 of 3 readers given "usually" still say she holds the top.
- **Sealed.** ~99% both worlds. With the word, 2 of 3 call the top a maybe.

**C4. The missing step.**
- **Roast.** It'll pass Felix's test by a mile, which makes the test useless: the ten faces add to about $315,000, so interest pays about $185,000 of the $500,000. But P8 already says it: "costs less than the cheques because its bonds pay interest along the way". C4 adds "face value": one more word for the weakest stranger to guess, on the day that's the question.
- **Bet.** 2 of 3 cold readers, given P8 alone, can't say "part of every cheque is interest".
- **Sealed.** Share 35-40%; 2 of 3 say it back already. A return that costs a sentence.

**Pit ranking.** C1 is the only one that can be wrong in a number, and I think it is, by about three grand. Fix the sizing and it's the first idea today I couldn't break. C2 and C4 are returns. Write it down before I change my mind.

## Round 3: Jun judges after the test (2026-11-03)

(Keel is a simulated team, AI-written.)

**Jun** (round 3)

MODEL throughout: 22 Oct curve, 200,000 futures, seed 20261016. "Lower" is yields 2 points down for good. I re-ran `audit_c4.py`: $19,945 nominal, $14,282 to buy. Same.

**Kai, bet by bet.** Your roast beat your seal.
- Honest lock "about $14,000": $14,282. "$6,700 more than V54": $6,782. Re-summing adds over $2,000: $3,081. Won all three. Which rungs K0's shorts sit on isn't split in results.json, so that half is unscored.
- Sealed K0: ~99.5% every cheque, ~0.4% short over $1,000, beating W0f. Actual 95.16% and 3.30%, worse than W0f's 2.44%. Lower: ~1.5%, actual 15.63%. Lost both, the second by ten times.
- K0 kept stocks: ~$11k taken, emptied more often. Median $6,176, emptied 16.3% v 17.5%. Lost. Lower world, less taken: $2,234, not $3,600. Half.
- Gift within $500 of W0f: +$552, lost by $52. Higher in the lower world: +$2,754, won.
- STRIPS knife: real. KW costs $2,603 more than K at the median. It's why KW is the rule.
- C3, top at least 99%: lowest 99.29%. C4, share 35-40%: 36.6%. Both won.

**Felix, your C1 wrong-ifs, on KW.** Cheques: 0% short over $1,000 v A0f's 0.02%, passed. Top reached 99.33% v 97.84%, passed. Kept stocks emptied 28.1% v W0f's 17.5%, failed. Range lowered 26.9% v 16.9%, failed. Gift mean $670 under A0f, $1,481 in S9, failed there. Your hypothesis is wrong. I'm adopting it anyway: your tests priced it fairly.

**Verdicts**
- **C1: ADOPT, KW as the rule.** IPS (the rule in words, no figure) and Final Report (table, escrow source). Price against A0f, base: gift mean $670 lower; kept stocks run out in 28.1% of futures as opposed to 19.0%; range lowered on naming day 26.9% as opposed to 16.9%. If yields fall: $191, 72.8% v 65.4%, 71.9% v 62.9%. Worth it. W0f misses a cheque by over $1,000 in 1 in 41 futures. A0f reaches 99.87% only by paying cheques out of a gift co-sponsors have already heard, in 8.1% of futures and 24.1% if yields fall, which is what P6 is there to rule out. KW, once bought, never misses a cheque, never touches a named range, and has no cushion to guess. K needs STRIPS, KK empties her stocks in 68.5% of futures, K0 fails.
- **C2: BIN.** P5 already goes floor, then fund. The trip is "option", which C2 keeps: a word for the Writing Room.
- **C3: BIN for the IPS; Final Report.** Felix's test passed, but once named the top is bonds, and "almost always" could only cite the model (Book 11). The confidence goes beside its amount in the co-sponsor draft.
- **C4: Final Report only.** The useful part isn't 36.6%. It's that about a tenth of the cheques rides on future yields, $19,945 on naming day. That's how small the weak point is.

**What would worry an actuary.** "0 of 200,000" is true by construction: yields are floored at 0.25% and the lock assumes zero. K0 is the real evidence: one leg nobody zeroed, the months bonds wait for January (0.9% of the cheques), took 100% to 95.16%. An actuary asks what else is unzeroed. One: the model pays the five fund rungs (2033-37) at par (`audit_c4.py`, RUNGS), and IBTM and friends pay out net asset value.

**The count copy.** "As if that interest earned nothing more" says KK. Read literally, "that interest" is everything already reinvested, and "nothing more" stops it on the day. A literal reader, and actuaries are literal, gets the dear lock. It also misses the wait for January, which isn't interest. One alternative, same 13 words: "we price that gap as if money paid later sat idle, and move". Money paid after she names the range sits at zero, money already working keeps working, the bonds still pay. That's KW. The rest of P8 stays true: her kept stocks first, then the range, before it's said aloud. P9 stays true word for word, with no second look to name, as opposed to A0f, which needs a new sentence there.

**Seeds**
1. Writing Room, 16:20: ask strangers "Do the bonds still pay their interest?" (Kai's knife) and "Does money already reinvested stop earning?" (KK). 2 of 3 right, or it isn't the claim.
2. Courtroom tonight: where does the unneeded lock go? Median $17,953 back to Laura as the rungs pay; P9 is silent. And does "pays exactly what it promises" stretch to the fund rungs?

## What we decided

- C1 ADOPT, KW (the WInS-true lock) as the rule: every cheque 100% / 100% / 98.71% (base / yields 2 pts lower / deposit halved; shorts only where the money isn't there); gift never pays a cheque after naming; gift mean -$670 base v A0f; kept stocks all gone 28.1% v 19.0% (MODEL)
- CORD: W-08c's $11,201 is $14,282 on the model's own sizing (the wait for January); as sized (K0) the lock pays every cheque in only 95.16% of base futures
- C2 BIN; C3 BIN for the IPS, Final Report; C4 Final Report only (about a tenth of the cheques rides on future yields, 4.0% on naming day)
- Count copy: 'as if that interest earned nothing more' reads as the strictest lock (Jun); offer 'as if money paid later sat idle' (497 strict)

## Still open (seeds for the next huddle)

- Do strangers say 'as if money paid later sat idle' back right: do the bonds still pay their interest, and does money already reinvested stop earning? (Writing Room, 16:20)
- Where does the unused lock go (about $18,000 at the median), and does 'pays exactly what it promises' stretch to the fund rungs, which pay net asset value? (Courtroom, 18:20; Final Report)
