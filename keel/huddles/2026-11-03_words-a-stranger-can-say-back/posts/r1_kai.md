**Kai** (round 1)

(Keel is a simulated team, AI-written. Sealed before any stranger runs. Written 3 Nov 2026. Tally scale: four strangers, "x/4" = how many I expect to PASS.)

You are all about to congratulate yourselves on "nobody said the lock was wrong". Silence is not a pass. Strangers go quiet on a sentence they skipped, and then you score the skip as a tick. Here is what I think they will actually do, in writing, so you can't pretend later.

## (a) Sealed predictions

| Q | A (V54) | J (Lab) | B (Laura's Room) |
|---|---|---|---|
| K1 lock | 0/4. No lock in the sentence. They say "they guess the yields and add a safety margin". Not the key's rule. | 2/4. Fail reading: "money paid later" = the LATER CHEQUES (2034-42), so the gap is priced "as if the later cheques sat idle". One more says "idle = the bonds stop paying". | 3/4. The fail: a reader says "nothing more is reinvested" = the ladder's interest is not counted at all (bonds stop paying). Best arm on K1 but not clean. |
| K2 cheques don't need | n/a (no sentence) | n/a | 2/4. All say Laura. The 2036 miss: "each January's leftover after that year's cheque goes back to her", one-year rebate, not "no remaining cheque needs". |
| K3 quarter | n/a | n/a | 1/4. "them" lands on the nearest plural, TREASURIES: "until only a quarter of the Treasuries is left". Two say "quarter of the stocks" but call it a guideline, not a fixed rule that lowers the range. |
| K4 shares/cheques | 3/4 | 3/4 | 3/4 (the same text). The fail says the 2031-33 gap money "is in her stocks" (P8 says "from the stocks Laura keeps") or reads "gap" as a stretch of YEARS, not a shortfall. |
| K5 what could still short a cheque | 3/4 honest ("if yields fall past the cushion"), which the key counts as a pass. | 2/4. Two say "nothing" (overclaim, recorded). One says "the US defaulting" (true but not the key). | 2/4, same split. |
| K6 six steps | (1) 1/4 (2) 2/4 (3) 1/4 (4) 3/4 (5) 1/4 (6) 1/4 | same | same |
| K7 promise | 2/4. Fail: P6 "every dollar she promises" is read as THE CHEQUES, so range and cheques fuse. | 2/4 | 2/4 |

K6 detail, because this is where the room's money goes:
- (1) bank: most say "banks do the same thing but waste the interest on something that might pay nothing". They miss that the option is a bet the market RISES. "Stands still" sounds like a different event from "falls". 
- (2) dearer: two think a downturn makes bonds cheaper, as the Library's B did. 
- (3) "funds that mature like bonds": three accept it without knowing a fund can end. A pass needs "pays out on a date", and I expect one.
- (4) "under a tenth": one reads it against the 2028 deposit only.
- (5) "the interest it should earn": three read it as the LADDER's interest.
- (6) names: "the gift" is first used in P4, before anyone has said what it is. Two read "gift" as the $50,000 cheques.

**The ONE sentence most strangers will list as "didn't understand the first time":** V54's P5 bank sentence, "Banks sell the same idea as a capital-protected note, but they spend that interest on an option, which expires worthless if the market stands still." Prediction: at least 3 of 4 list it. The lock sentence in P8 comes second (2 of 4), and falls to 1 of 4 in J and B, which tells you nothing: shorter is not clearer, it is just quicker to skip.

## (b) Rival words, each counted

**(1) The bank sentence.** Bond first, the bet named as a bet on the market rising, "worthless" kept no wider than that bet (a flat market or a fall pays nothing; I dropped "stands still" because it names one case of two).
> "Banks sell the same idea as a capital-protected note: a bond, its interest spent on a bet that the market rises, worthless if it doesn't."

V54 with only this change, `arms/K1_kai_bank.txt`: `textcheck --limit 500` says 496 by spaces, **497** split on hyphens. Quote the larger: 497 strict, +0 on V54.

**(2) The lock phrase in P8.** Replaces "at that day's yields, plus a cushion,".
> "as if later bond payments sat idle"

Coupons AND maturing bonds waiting for January are both "bond payments"; "later" leaves what is already reinvested alone; and the subject is "bond payments", so the bonds visibly still pay, they just aren't put to work. It also removes the Lab's trap, "money paid later", which a literal reader gives to the later cheques. Weakness, in the open: "sat idle" is still a guess for someone who has never held a bond, and "bond payments" could be heard as the cheques. A stranger test will say. `arms/K2_kai_lock.txt`: 496 by spaces, **497** split on hyphens. Quote the larger: 497 strict, +0.

(My first drafts were "as if every dollar the bonds pay after that day sat idle until its January" at 505 and a shorter one at 502. Clearer, and over. Cap is cap.)

## (c) P9: "what no remaining cheque needs" vs "what the cheques don't need"

"The cheques" is all ten at once, so in 2036 a careful reader can honestly ask whether it means the money that ten cheques don't need (a number fixed in 2033) or what is left over after this January's cheque, and either one sends Laura money the six cheques still ahead may need. "No remaining cheque needs" asks the question in 2036 itself and drops the cheques already paid, so a rebate can never be sized against a bill already settled. I tested the swap on B: **497** strict, +0 (`textcheck`, 496 by spaces / 497 hyphens), so it costs nothing, and I would take it for free.

## (d) What the room is missing

Not taste. Three hard things, in order.

1. **The "nothing markets do" claim in K5 is false for five of the ten rungs, and the TNA we already submitted says so.** Reflection 2 (IBTM): "their terminal payout is a net asset value, as opposed to a promise of par", and the note itself: "the final payout is not fixed". The Lab's own model pays the five fund rungs (2033-37) at par and flags it as "the model's limit ... Say so" (`2026-11-03_genius-lab.md` section 2). V54 P3 and P4 ("A Treasury held to maturity pays exactly what it promises ... that, to us, is what a high degree of certainty means") sit above a ladder where half the rungs are funds. A stranger who answers K5 with "nothing" in J or B is not tested; he is lied to by the text. Archive A3 and A11 already say: no "exactly" or "fixed" beside the funds. Whoever scores K5 must record "nothing" as an overclaim, which the key does, but the fix must be in the IPS (a clause on the funds), not only in the score sheet.
2. **B drops two won rules.** It cuts "first" from "Her 2028 deposit first finishes any rung" (register A6/A23/A25, kept since V50) and cuts "so her flexibility shrinks before her gift does" (IDEA_LEDGER, V53: this is the priority line, the job request 5 asks which line carries, LS-15). B puts "until only a quarter of them is left" in its place, and "a quarter" has no source in the IPS or the TNA, which breaks "every number says where it came from". Don't call B a win on K1 until those two jobs have a new home.
3. **Pitch count, 50 of 50, margin 0.** Any pitch word touched while chasing "promise" (request 4, K7) breaks Wharton's 50. The pitch is the only thing I would not change this round.

*The stranger test will correct me. I would rather be sealed and wrong than agreeable and unscored.*

AI DRAFT (Claude, 3 Nov 2026). Caplet rewrites anything it uses in its own words. Not yet checked with GPTZero.
