# Amara, research note, round 2 (H-019, Mon 2 Nov 2026)

> FICTION (the speaker is simulated; the texts, counts and sources are real). (Keel is a simulated team, AI-written.)
> AI DRAFT (Claude, 2 Nov 2026). Arm D below is a test text for Tuesday's blind read, not a promotion. GPTZero: not yet checked.

**1. Arm D, exact text** (built from `../arms/A_V53.txt` on a scratch copy; never edited in the repo). `python3
keel/office/tools/textcheck.py`: **497 split on hyphens**, 496 by spaces, 2 non-ASCII (the two spaced en dashes, as in
A). sha256 begins `15695e3126bc1db6`. If Jun registers it, he should copy these lines byte for byte and re-hash.
Changes against A: P2 +12 (V50's sentence, verbatim); P3 -9 ("We don't invest toward these payments. We buy them.");
P9 "one bond" -> "one rung"; P9 reserve sentence rewritten (+10); P9 order line cut (-13). No new numbers.

```
In January 2033, Laura's portfolio writes the first of ten cheques: $50,000 each, one every January, to fund her Taiwan residency. She also hopes to contribute to the building.

We call our plan Caplet XR. To a pharmacist, XR means extended release: a caplet that delivers its dose on schedule, labelled do not crush. Crush it and the schedule is gone. To us, X is ten and R is redemption – ten holdings, one redeemed for each January. Crushing one means selling it before its January, even for the building.

In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds that mature like bonds, one rung falling due before each cheque. A Treasury held to maturity pays exactly what it promises, whatever markets do. That, to us, is what "a high degree of certainty" means.

Laura's career already behaves like a stock. Her 2028 deposit depends on publishing advances, speaking fees and licensing – income that can dry up in the kind of downturn that makes a ladder dearer to buy. If that deposit arrives smaller, the gift shrinks. A cheque funded by a Treasury already bought does not.

Her 2028 deposit first finishes any rung the first $300,000 couldn't buy. Most of the rest buys a Treasury fund maturing in late 2032. That is her floor. The remainder, roughly the interest it should earn, goes into one world index fund, spread across thousands of companies. That is under a tenth of her money. Banks sell this as a capital-protected note, but they spend that interest on an option, which expires worthless if the market stands still. Shares don't. We assume world shares earn about 7.5% a year over the long run, but the cheques never depend on it.

In 2031, Laura gives co-sponsors a range for her facility contribution. The bottom is her floor, rounded down: money she already owns. The top adds half her stocks, valued that day. Before she names it, that half moves into Treasuries, so every dollar she promises is already in bonds. The other half stays with Laura, liquid any day, as her flexibility, in case the building costs more in Taiwan dollars.

We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be quietly halved if markets turn.

The weak point is reinvestment. The ladder costs less than the cheques because its bonds pay interest along the way, which we reinvest. If yields fall and stay low, that interest earns less, and the ladder falls short. Before she names the range, we price that gap at that day's yields, add a cushion, and set it aside from the stocks Laura keeps, so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range.

From 2033, the operating reserve is the ladder plus the money set aside for its reinvestment gap. It pays out one rung per cheque.

Do not crush.
```

**2. Fallback D' (keeps "We buy them"), read by nobody.** Same as A plus V50's sentence in P2; P3 untouched; P5 cuts
"That is under a tenth of her money." (-8); P9 becomes one sentence, "From 2033, the operating reserve is the ladder plus
the money set aside for its reinvestment gap, paying out one rung per cheque.", and the order line goes. `textcheck.py`:
497 split on hyphens, 496 by spaces; sha256 begins `3ca8f4bac4514875`.

**3. Why the reserve line is written for a quoter** (`../blind/answers.md`, read 2 Nov). On Q3 the skimmer quoted the
sentence back on all three texts and added nothing: A "From 2033, the ladder becomes the operating reserve ..."
(RIGHT, because the key for A is the ladder); B and C "The ladder and everything set aside for it" (WRONG: the quote
carries no meaning). So the line has to be one whose quote is already the answer. "the money set aside for its
reinvestment gap" names what the money is for with P8's own noun ("we price that gap"). "Cushion" alone would name only
the extra on top of the gap (Nora, `../posts/r1_nora.md`; P8: "price that gap ..., add a cushion, and set it aside").

**4. What the line still doesn't say, and I won't pretend it does.** The case (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`
lines 95-96) asks for the reserve's "size and initial asset composition". D names the reserve's two parts, not what the
gap money is held in. In the Lab's model the 2031 set-aside earns a two-year Treasury yield to 2033
(`keel/rooms/lab/L-15_hold_it_then_say_it/run.py` line 32, `bill2`; L-16's `c0 = L33 + x_ * bill2`), so "in Treasuries"
would be true to the design. It costs words and nobody has read it; Final Report, or a later arm.

**5. A misquote in the results (for Felix).** `../blind/RESULTS.md` quotes the actuary as "it never says what happens if
the gap is bigger than Laura's kept stocks". The actuary's own words (`../blind/rank_opus.md`, KMGK): "it never says what
happens when the gap is larger than the stocks Laura keeps". Same meaning; my post quotes the reader's own words.

**6. The packet and the pitch** (`../blind/sayback_common.md`, `../blind/rank_common.md`). Readers got the case,
Wharton's sections and "one team's IPS (the 500-word field of the entry form)", never the pitch. The skimmer's only
score gap (A 5 v 4 on Creativity & Presentation) came from "We don't invest toward these payments. We buy them", which
V53's pitch (`keel/ips_rewrite/drafts/D33/pitch.txt`) says almost word for word: "so we don't invest for them. We buy them."
