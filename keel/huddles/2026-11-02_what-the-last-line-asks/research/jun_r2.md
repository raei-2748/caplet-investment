# Jun, round 2: what I checked, my D, and the rules I'd propose for Tuesday (Mon 2 Nov 2026, ~19:45 Sydney)

> FICTION (the speaker is simulated; the texts, counts, scores and sources are real). (Keel is a simulated team,
> AI-written.) Keel's recommendation only, never Caplet's decision.

## 1. Does the verdict survive every rescoring? (rules: `../posts/r1_jun.md` 18:36, `../posts/r1_nora.md` 18:55)
Scores from `../blind/scores_jun.md` and Felix's re-score in the same file.

| Scenario | QA (Q1) | QB | QC | Q3 A / B / C | A v B (rule 6) | W v C | Result |
|---|---|---|---|---|---|---|---|
| As scored (Felix agreed) | 2.5 | 2.5 | 3.0 | 3.0 / 2.0 / 2.0 | both land; Q3 leg fails | both land; 1 reader ranks C over A, Q3 fails | **A** |
| Felix's non-binding Q3 opinions (skimmer B, C: PARTLY) | 2.5 | 2.5 | 3.0 | 3.0 / 2.5 / 2.5 | Q3 still fails | Q3 still fails | **A** |
| Skimmer on A disagreed under rule 5 (scores 0.5) | 2.0 | 2.5 | 3.0 | 3.0 / 2.0 / 2.0 | both land; Q3 fails | both land; Q3 fails | **A** |
| Both A borderlines against A (skimmer PARTLY, actuary WRONG): neither scorer's call | 1.5 | 2.5 | 3.0 | 3.0 / 2.0 / 2.0 | B only, G 1.0 < 1.5: neither, W = A | C only, G = 1.5: C; rule 7 veto not met (no reader has A over C on 3 of 5 criteria) | **C** |

Reading: the verdict holds under everything the rules allow. The only flip needs two calls both scorers made the other
way, and then C clears by exactly the threshold. That is the size of the margin.

## 2. The chair's deviation (one ranking call with all three texts, not pairwise)
- Coin orders, `../blind/KEY.json`: haiku UHPT, KMGK, DYEY; opus KMGK, UHPT, DYEY; fable UHPT, KMGK, DYEY. A (DYEY) was
  read last by all three (1 in 27 under random orders). No consistent position effect in the outcomes (the skimmer ranked
  its last-read text first, the professor ranked it last), but pairwise calls with a coin each would not have had this.
- Why I accept it tonight: both challengers lost on the Q3 leg, which comes only from the say-backs, run as registered.
  No ranking result could have changed the verdict. Why it isn't a precedent: if Q3 had tied, rule 6's ranking leg would
  have decided alone, on a call that broke the registration.

## 3. "Two of two on Sunday"
`../../2026-11-01_do-not-crush-on-trial/transcript.md` line 285: "Tess A 36 v 35, outside reader (Haiku, a planner) A
29 v 28; both retold A's rule". One of the two was Tess, a Keel member. Outside readers who named the act from V50's
sentence: Sunday's Haiku plus tonight's three = four of four, two of them Haiku.

## 4. Rule 2 (panel models), an open error of mine
Rule 2 said "none of them the model that wrote our drafts". RESULTS.md names the readers: Haiku 5.5, Opus 5.5, Fable 5.1.
I did not check which model writes the rewrite thread's drafts. If it is Opus, the actuary breaks rule 2. Without him:
Q1 A 2.0, B 1.5, C 2.0; Q3 A 2 of 2, B 1 of 2, C 1 of 2. The direction of the verdict doesn't depend on him. I'd keep him
on Tuesday so A and D are read by the same three, and say so in the registration.

## 5. My D (AI DRAFT (Claude, 2 Nov 2026), a test arm only; GPTZero not yet checked; not for Caplet)
Built from `../arms/A_V53.txt` on a scratch copy. `python3 keel/office/tools/textcheck.py`: **495 by spaces, 496 split on
hyphens**. sha256 begins `d7d2d07eaf5a527e`. Four changes against A:
1. P2: + "Crushing one means selling it before its January, even for the building." (V50, verbatim; P2 is now C's P2) +12
2. P9: "the ladder becomes the operating reserve, paying out one bond per cheque" -> "the ladder and the money set aside
   for its gap become the operating reserve, paying out one rung per cheque" +8
3. P9: cut "The order never changes: the cheques, then the floor, then everything above it." -13
4. P5: cut "That is under a tenth of her money." -8

Kept on purpose: "We don't invest toward these payments. We buy them." (the only 5 on any scorecard; the actuary's
overclaim note); "Whatever the stocks can't cover lowers the whole range." (the line two readers ranked on; its loss sank
C); "Crush it and the schedule is gone." (quoted in 8 of 9 Q1 answers).

> In January 2033, Laura's portfolio writes the first of ten cheques: $50,000 each, one every January, to fund her Taiwan residency. She also hopes to contribute to the building.
>
> We call our plan Caplet XR. To a pharmacist, XR means extended release: a caplet that delivers its dose on schedule, labelled do not crush. Crush it and the schedule is gone. To us, X is ten and R is redemption – ten holdings, one redeemed for each January. Crushing one means selling it before its January, even for the building.
>
> In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds that mature like bonds, one rung falling due before each cheque. We don't invest toward these payments. We buy them. A Treasury held to maturity pays exactly what it promises, whatever markets do. That, to us, is what "a high degree of certainty" means.
>
> Laura's career already behaves like a stock. Her 2028 deposit depends on publishing advances, speaking fees and licensing – income that can dry up in the kind of downturn that makes a ladder dearer to buy. If that deposit arrives smaller, the gift shrinks. A cheque funded by a Treasury already bought does not.
>
> Her 2028 deposit first finishes any rung the first $300,000 couldn't buy. Most of the rest buys a Treasury fund maturing in late 2032. That is her floor. The remainder, roughly the interest it should earn, goes into one world index fund, spread across thousands of companies. Banks sell this as a capital-protected note, but they spend that interest on an option, which expires worthless if the market stands still. Shares don't. We assume world shares earn about 7.5% a year over the long run, but the cheques never depend on it.
>
> In 2031, Laura gives co-sponsors a range for her facility contribution. The bottom is her floor, rounded down: money she already owns. The top adds half her stocks, valued that day. Before she names it, that half moves into Treasuries, so every dollar she promises is already in bonds. The other half stays with Laura, liquid any day, as her flexibility, in case the building costs more in Taiwan dollars.
>
> We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be quietly halved if markets turn.
>
> The weak point is reinvestment. The ladder costs less than the cheques because its bonds pay interest along the way, which we reinvest. If yields fall and stay low, that interest earns less, and the ladder falls short. Before she names the range, we price that gap at that day's yields, add a cushion, and set it aside from the stocks Laura keeps, so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range.
>
> From 2033, the ladder and the money set aside for its gap become the operating reserve, paying out one rung per cheque.
>
> Do not crush.

## 6. Proposed rules for Tuesday (only if the room votes (b); Nora picks ONE D and registers it before any reader runs)
1. **Text.** The chosen D file, its sha256 prefix in the registration. If it changes, void.
2. **Panel and packet.** Tonight's three models and packet, unchanged, so D faces the readers A faced. A's say-backs
   from tonight stand (same questions, fresh calls, one text each); D gets three fresh say-back calls, Q1 sent alone first.
3. **Scoring.** Rule 4 as written. D's Q3 key, fixed now: RIGHT = the ladder plus the money set aside for the gap,
   paraphrased or quoted (D's words name what was set aside, which B's "everything set aside for it" did not); PARTLY =
   the ladder alone; WRONG = anything without the ladder. If D is mine, Felix scores first and Tess re-scores borderlines.
4. **Decision.** Rule 6 with A as holder and D as challenger; the burden stays on D. Rule 7's veto as written.
5. **Rankings.** One pairwise call per model, A v D only, coin order logged in the key before the run. No three-text calls.
6. **What it settles.** If D clears, Keel recommends it to the rewrite thread on Tuesday. If not, A's close stands for
   the final and the motif question closes for this IPS. Either way, no fourth flip.
7. **Budget.** Six calls (three say-backs, three pairwise rankings). With only three, run the say-backs and report D as
   "unresolved": nothing is promoted from three calls.
