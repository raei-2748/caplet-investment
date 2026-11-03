# The Courtroom to the rewrite thread, Tue 3 Nov 2026 (round 7 beat 8): C06, V54 with six of W5's lines

(Keel is a simulated team, AI-written.) AI DRAFT (Claude, 3 Nov 2026) for every wording below; an offer only: the
rewrite thread decides and Caplet rewrites in its own words. GPTZero: not yet checked. No model number goes on the page
(Book 11). Trial C-06, huddle H-026 (`../../rooms/courtroom/C-06_w5_on_trial.md`, `../../huddles/2026-11-03_w5-on-trial/`).

## 1. The ruling in two lines
W5 (the Writing Room's twelve changes) **does not replace V54 as a whole**: two blind readers split (a bond manager
who judges school competitions preferred W5R 33 v 31; a Year 10 student preferred V54 25 v 23 and was "lost" on
"$450,000"), and Nora's sealed rule needed +3. **Keel vote B 3-0: V54 plus six of W5's lines = C06, 497 strict.**

## 2. C06: the six lines (old -> new; every other word is V54's; `textcheck.py`: 496 by spaces, 497 hyphen-split)
| P | V54 | C06 | Words | Why (readers' own words) |
|---|---|---|---|---|
| P4 | "in the kind of downturn that makes a ladder dearer to buy." | "in a downturn, when interest rates usually fall, making bonds cost more." | 0 | J: with V54 "a general judge has to supply 'rates fall, prices rise' themselves"; FRED GS10, the 10-year fell in 10 of 11 US recessions since 1953 (NBER dates UNVERIFIED) |
| P5 | "Her 2028 deposit first finishes" | "Her 2028 deposit finishes" | -1 | pays; "Most of the rest buys" keeps the order (J: "Three parts, in order.") |
| P5 | "roughly the interest it should earn," | "roughly the interest the floor should earn," | +1 | S read V54's "it" as "the expected return" |
| P5 | "which expires worthless if the market stands still." | "which expires worthless unless the market rises." | -1 | J: V54's "a reader might think the option pays off in a falling market" |
| P8 | "If yields fall and stay low," | "If interest rates fall and stay low," | +1 | one name with P4; S had to gloss "yields" |
| P8 | **"at that day's yields, plus a cushion,"** | **"as if later bond payments sat idle,"** | 0 | **The one change that matters most.** J: "an assumption I can check (coupons earn nothing) instead of an unsized 'cushion'"; S said it back ("planning for the worst case") |

**Kept from V54 on purpose:** P3 "funds that mature like bonds" (J: it "answers the question X left open"; Tess's
repair "some held directly and some through funds" drew "why funds? The page doesn't say"); "under a tenth of her
money" (S: "$450,000 ... the page doesn't say what it is"); "That is her floor."; "facility contribution" (Wharton's
phrase; J: "closer to how a client letter would read"); "over the long run"; "Shares". P2, P6, P7, P9, "Do not crush."
and the pitch are word for word.

## 3. Full text (`../../huddles/2026-11-03_w5-on-trial/exhibits/C06_ruling_ips.txt`)

```
In January 2033, Laura's portfolio writes the first of ten cheques: $50,000 each, one every January, toward running her Taiwan residency. She also hopes to contribute to the building.

We call our plan Caplet XR. To a pharmacist, XR means extended release: a caplet that delivers its dose on schedule, labelled do not crush. Crush it and the schedule is gone. To us, X is ten and R is redemption – ten holdings, one redeemed for each January. Crushing one means selling it before it matures, even for the building.

In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds that mature like bonds, one rung falling due before each cheque. A Treasury held to maturity pays exactly what it promises, whatever markets do. That, to us, is what "a high degree of certainty" means.

Laura's career already behaves like a stock. Her 2028 deposit depends on publishing advances, speaking fees and licensing – income that can dry up in a downturn, when interest rates usually fall, making bonds cost more. If that deposit arrives smaller, the gift shrinks. A cheque funded by a Treasury already bought does not.

Her 2028 deposit finishes any rung the first $300,000 couldn't buy. Most of the rest buys a Treasury fund maturing in late 2032. That is her floor. The remainder, roughly the interest the floor should earn, goes into one world index fund, spread across thousands of companies. That is under a tenth of her money. Banks sell the same idea as a capital-protected note, but they spend that interest on an option, which expires worthless unless the market rises. Shares don't expire. We assume world shares earn about 7.5% a year over the long run, but the cheques never depend on it.

In 2031, Laura gives co-sponsors a range for her facility contribution. The bottom is her floor, rounded down: money she already owns. The top adds half her stocks. Before she names it, that half moves into Treasuries, so every dollar she promises is already in bonds. The other half stays with Laura, liquid any day, as her flexibility, in case the building costs more in Taiwan dollars.

We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be quietly halved if markets turn.

The weak point is reinvestment. The ladder costs less than the cheques because its bonds pay interest along the way, which we reinvest. If interest rates fall and stay low, that interest earns less, and the ladder falls short. Before she names the range, we price that gap as if later bond payments sat idle, and move that much from the stocks Laura keeps into Treasuries, so her flexibility shrinks before her gift does. Whatever the stocks can't cover lowers the whole range.

From 2033, the ladder and the money set aside for its gap become the operating reserve, paying out one rung per cheque.

Do not crush.
```

## 4. The condition under the lock, and what the Final Report must do (exhibit N, MODEL)
"Every cheque in full in 200,000 of 200,000" (L-17) was true only of the model's par bonds. The five fund rungs
(2033-37) hold Treasuries that mature through their last year, and the cash waits for the 15 December close
(iShares: "During the final year of the fund's life, the underlying bonds will mature and the proceeds will be held in
cash equivalents until the liquidation of the fund"; "the Funds do not seek to return any predetermined amount"). As
funds, the lock as the model sized it pays every cheque in 97.02% of base futures and 82.18% if yields fall 2 points
for good; **sized as the words read** (a fund's bond repaid in June is a later bond payment sitting idle till
December), 100% in both, for $3,559 more on naming day at the median (V54's design via the L-17 chain, 22 Oct 2026
curve, J.P. Morgan 2027 LTCMA 7.5%, 200,000 paths, seed 20261016; `../../rooms/courtroom/C-06_w5_on_trial/EXHIBIT_N.md`).
So the IPS words stand, and the Final Report:
1. sizes the lock on what the funds hold (each bond idle from its maturity to the December close) plus the 0.07% fee;
2. models the range's top as the words read (the rounded-down bottom plus half her stocks), because the floor fund pays
   net asset value too (counted at face, the top is reached 91.6% v 99.3% of base futures);
3. returns "what no remaining cheque needs" to Laura (H-024, H-025);
4. names S9 (shorts only where the money was never there) and the even-spread assumption.
**Not added to the page:** a sentence that no cheque can be short after naming day (beside funds that pay net asset
value it overclaims; the bond manager read "Essentially no" from the page as it is).

## 5. Gates before the thread uses it
The Window (Wed 4 Nov 08:40), already queued: L-17 from a clean checkout (the lock line stands on it). Added tonight:
exhibit N from a clean checkout, the funds' real maturity dates against the even spread, and the NBER dates under
"usually fall". If L-17's gate fails, V54's seven words go back at no cost.
