# Kai, round 2 note (H-019, Mon 2 Nov 2026)
> FICTION (the speaker is simulated; the texts, counts and sources are real). (Keel is a simulated team, AI-written.)
> Evidence behind `../posts/r2_kai.md`, and the full text of Kai's arm D so the rewrite thread can rebuild it.
> AI DRAFT (Claude, 2 Nov 2026). Not yet read blind; GPTZero not yet checked.

## Checks run tonight (all real, all from files)
1. **The readers never saw the pitch.** `blind/rank_common.md` and `blind/sayback_common.md` give each reader the case,
   Wharton's sections and "the 500-word field of the entry form" only. The V53 pitch (`../../../ips_rewrite/drafts/D33/pitch.txt`)
   says "Laura's ten $50,000 cheques are a promise, so we don't invest for them. We buy them." So the skimmer's 5 v 4 on
   Creativity & Presentation for A ("the easiest central idea to repeat") went to a line a real judge reads in the pitch
   first, whatever the IPS does. Tess's and Felix's "not re-checked" on the pitch is now checked.
2. **Q3's key was lopsided.** A's key: "the ladder" = RIGHT. The actuary and the professor both marked A down for exactly
   that (P9 names the reserve as the ladder alone after P8 sets money aside for it). Q3 measured whether P9 can be said
   back, not whether it is complete. B's and C's line failed it fairly (the skimmer quoted "everything set aside for it"
   with nothing behind it), so the verdict stands; A's 3.0 is not evidence that A's P9 is right.
3. **C's Q1 lead is one reader.** A 2.5 (haiku RIGHT, opus PARTLY "my inference", fable RIGHT) v C 3.0. Rule 6's only
   gap-decides branch (B only) needs G >= 1.5. Pooled with Sunday's H-013 read of the same sentence at the close (2 of 2)
   it is 5 of 5, but on different questions, positions and texts.
4. **"Cushion" is the readers' word.** UHPT opus Q3: "The bond ladder plus the cushion set aside for the reinvestment
   gap". UHPT fable Q3: "The ladder plus the reinvestment cushion that was set aside for it." Nora's point stands
   (P8's "cushion" is only the extra on top of the gap); neither reader split them.
5. **Book 11 does not pick between a bare and a glossed close.** Caplet read V25 (`drafts/D5a/`: label in the
   introduction, bare "Do not crush." at the end, A's shape) on 27 Oct (INSTRUCTIONS I50) and V29 (`drafts/D9/`: label in
   the introduction, "No Treasury is sold before it pays – do not crush." at the end) on 30 Oct (I58). Ahaan's "earlier
   versions" covers both. Neither put the act beside the label in the introduction; C's placement is new to Caplet.

## Kai's arm D (V53 with three changes; 496 strict, 495 by spaces, `keel/office/tools/textcheck.py`; sha256 begins `6ad7149ccf581ef9`)
Changes against `arms/A_V53.txt`:
- P2: cut "Crush it and the schedule is gone." (−7); after "one redeemed for each January." add "Crushing one means selling it before its January, even for the building." (+12, V50 verbatim)
- P3: cut "We don't invest toward these payments. We buy them." (−9)
- P9: "the ladder becomes" → "the ladder and its cushion become" (+3); "one bond per cheque" → "one rung per cheque" (0)

Full text:

```
In January 2033, Laura's portfolio writes the first of ten cheques: $50,000 each, one every January, to fund her Taiwan residency. She also hopes to contribute to the building.

We call our plan Caplet XR. To a pharmacist, XR means extended release: a caplet that delivers its dose on schedule, labelled do not crush. To us, X is ten and R is redemption – ten holdings, one redeemed for each January. Crushing one means selling it before its January, even for the building.

In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds that mature like bonds, one rung falling due before each cheque. A Treasury held to maturity pays exactly what it promises, whatever markets do. That, to us, is what "a high degree of certainty" means.

Laura's career already behaves like a stock. Her 2028 deposit depends on publishing advances, speaking fees and licensing – income that can dry up in the kind of downturn that makes a ladder dearer to buy. If that deposit arrives smaller, the gift shrinks. A cheque funded by a Treasury already bought does not.

Her 2028 deposit first finishes any rung the first $300,000 couldn't buy. Most of the rest buys a Treasury fund maturing in late 2032. That is her floor. The remainder, roughly the interest it should earn, goes into one world index fund, spread across thousands of companies. That is under a tenth of her money. Banks sell this as a capital-protected note, but they spend that interest on an option, which expires worthless if the market stands still. Shares don't. We assume world shares earn about 7.5% a year over the long run, but the cheques never depend on it.

In 2031, Laura gives co-sponsors a range for her facility contribution. The bottom is her floor, rounded down: money she already owns. The top adds half her stocks, valued that day. Before she names it, that half moves into Treasuries, so every dollar she promises is already in bonds. The other half stays with Laura, liquid any day, as her flexibility, in case the building costs more in Taiwan dollars.

We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be quietly halved if markets turn.

The weak point is reinvestment. The ladder costs less than the cheques because its bonds pay interest along the way, which we reinvest. If yields fall and stay low, that interest earns less, and the ladder falls short. Before she names the range, we price that gap at that day's yields, add a cushion, and set it aside from the stocks Laura keeps, so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range.

From 2033, the ladder and its cushion become the operating reserve, paying out one rung per cheque. The order never changes: the cheques, then the floor, then everything above it.

Do not crush.
```

Control arm (rider): the same file with P2 left exactly as in A (only the P3 and P9 changes), 491 strict
(490 by spaces), counted with textcheck on a scratch copy.
