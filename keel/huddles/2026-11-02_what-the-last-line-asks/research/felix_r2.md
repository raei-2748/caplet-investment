# Felix, round 2 research note (H-019, Mon 2 Nov 2026)
> FICTION (the speaker is simulated; the texts, counts and quotes are real). (Keel is a simulated team, AI-written.) Not for submission.

## 1. Which lines each reader quoted to answer Q1 (from `../blind/answers.md`, verbatim lines only)

| Text | Reader | "Crush it and the schedule is gone." | The act's own words in the text | P9 order line |
|---|---|---|---|---|
| A (DYEY) | haiku | yes | none (act given as "so I read it as") | no |
| A (DYEY) | opus | yes | none ("The text never says outright ... my inference") | **yes** |
| A (DYEY) | fable | yes | none | **yes** ("reinforced by") |
| B (UHPT) | haiku | yes | none ("breaking the schedule") | no |
| B (UHPT) | opus | yes | "none sold" | no |
| B (UHPT) | fable | yes | "none sold" | **yes** ("reinforced by the penultimate line") |
| C (KMGK) | haiku | yes | "Crushing one means selling it before its January" | no |
| C (KMGK) | opus | no | "Crushing one means selling it before its January" | no |
| C (KMGK) | fable | yes | "Crushing one means selling it before its January" | no |

What it shows:
- **The harm line is not the repeat.** With V50's sentence beside it (C), two of three readers still quoted "Crush it
  and the schedule is gone." with it, as the reason next to the act. The leaflet has the same shape: "Do not suck,
  crush or chew the caplets because that may affect its sustained release properties." (Panadol Osteo CMI, Haleon
  Australia, Jan 2026, as read by the Library, `keel/rooms/library/2026-11-02_scouts/felix.md`; second-hand, see my
  round-1 note).
- **The order line was a crutch for "crush".** It was quoted for Q1 by 2 of 3 readers on A and 1 of 3 on B, where P2
  never names the act, and by 0 of 3 on C, where it does. On C, the two rankers who leaned on it (opus, fable) did so
  only because C had cut "Whatever the stocks can't cover lowers the whole range." D keeps that sentence.
- **Full circle, measured.** On C every reader explained the last line from P2 alone. That is Book 11 item 4.
- **A's 2.5 came from the readers, not the page.** On A no reader quoted words that name the act.

## 2. The blind packet had no pitch
`../blind/rank_common.md` and `../blind/sayback_common.md` give each reader the case, `wharton.md` and the IPS text
only; `grep "We buy them" ../blind/text_*.txt` finds it only in DYEY (A). The pitch (`keel/ips_rewrite/drafts/D33/pitch.txt`)
says "We buy them." word for word. So the skimmer's Creativity 5 for A's "We buy them" was given to a line the real
entry form also prints in its first field.

## 3. Arm D (Felix), built on a scratch copy of `../arms/A_V53.txt`
Strict count **496** (`python3 keel/office/tools/textcheck.py`; 495 by spaces). sha256 begins `d8be2e370edaa597`.
Against A:
1. P2, after "one redeemed for each January.": add V50's sentence verbatim, "Crushing one means selling it before its
   January, even for the building." (+12)
2. P9: "the ladder becomes the operating reserve, paying out one bond per cheque" becomes "the ladder and the money set
   aside to fill its gap become the operating reserve, paying out one rung per cheque" (+9). "Set aside" is the case's
   own verb for the reserve (case lines 94-95: "Laura will set aside a portion of the portfolio to fund the ten payments.
   This set-aside is called the operating reserve."); "gap" is P8's word.
3. Cut P9 "The order never changes: the cheques, then the floor, then everything above it." (-13)
4. Cut P3 "We don't invest toward these payments. We buy them." (-9)

497 + 12 + 9 - 13 - 9 = 496. Against C, D is C with C's cut sentence ("Whatever the stocks can't cover lowers the whole
range.") restored, B/C's reserve phrase rewritten, and the order line cut. Only change 2's words are unread.

Full text of D:

> In January 2033, Laura's portfolio writes the first of ten cheques: $50,000 each, one every January, to fund her
> Taiwan residency. She also hopes to contribute to the building.
>
> We call our plan Caplet XR. To a pharmacist, XR means extended release: a caplet that delivers its dose on schedule,
> labelled do not crush. Crush it and the schedule is gone. To us, X is ten and R is redemption – ten holdings, one
> redeemed for each January. Crushing one means selling it before its January, even for the building.
>
> In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds that mature like bonds, one rung
> falling due before each cheque. A Treasury held to maturity pays exactly what it promises, whatever markets do.
> That, to us, is what "a high degree of certainty" means.
>
> Laura's career already behaves like a stock. Her 2028 deposit depends on publishing advances, speaking fees and
> licensing – income that can dry up in the kind of downturn that makes a ladder dearer to buy. If that deposit arrives
> smaller, the gift shrinks. A cheque funded by a Treasury already bought does not.
>
> Her 2028 deposit first finishes any rung the first $300,000 couldn't buy. Most of the rest buys a Treasury fund
> maturing in late 2032. That is her floor. The remainder, roughly the interest it should earn, goes into one world
> index fund, spread across thousands of companies. That is under a tenth of her money. Banks sell this as a
> capital-protected note, but they spend that interest on an option, which expires worthless if the market stands
> still. Shares don't. We assume world shares earn about 7.5% a year over the long run, but the cheques never depend
> on it.
>
> In 2031, Laura gives co-sponsors a range for her facility contribution. The bottom is her floor, rounded down: money
> she already owns. The top adds half her stocks, valued that day. Before she names it, that half moves into
> Treasuries, so every dollar she promises is already in bonds. The other half stays with Laura, liquid any day, as
> her flexibility, in case the building costs more in Taiwan dollars.
>
> We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be quietly
> halved if markets turn.
>
> The weak point is reinvestment. The ladder costs less than the cheques because its bonds pay interest along the way,
> which we reinvest. If yields fall and stay low, that interest earns less, and the ladder falls short. Before she
> names the range, we price that gap at that day's yields, add a cushion, and set it aside from the stocks Laura keeps,
> so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range.
>
> From 2033, the ladder and the money set aside to fill its gap become the operating reserve, paying out one rung per
> cheque.
>
> Do not crush.

(The quoted block above wraps lines for reading; the arm file, if the chair builds one, uses one line per paragraph
exactly as in `../arms/A_V53.txt`. Rebuild it from A with the four changes and re-run textcheck before registering.)
