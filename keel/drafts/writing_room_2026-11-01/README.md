# Writing Room, Sun 1 Nov 2026 (round 5, beat 7): five places, one page

AI DRAFT material (Claude, 1 Nov 2026); suggestions for the rewrite thread, never a draft of record. GPTZero: not
yet checked. (Keel is a simulated team, AI-written.)

**Base:** V49 (`keel/ips_rewrite/drafts/D29/ips_V49.txt`, branch `claude/project-thread-3ahu9r`, commit 84f1c4f),
copied as `base_V49.txt` / `base_V49_pitch.txt`: pitch 49, IPS 493 strict (`keel/office/tools/textcheck.py`).
**Files:** `build.py` (every arm, counted on the whole IPS; writes `arms.json`), `make_sheets.py` (shuffled blind
sheets `blind_reader_1.txt`, `blind_reader_2.txt`, key `keys.json`; labelled `room_sheet.txt`), the two outside
readers' replies verbatim (`blind_reader_1_verdict.md`, `blind_reader_2_verdict.md`). Huddle H-012:
`../../huddles/2026-11-01_five-places-one-page/`.

## The arms (whole-IPS strict count on V49's 493)
| Place | Arm | Source | IPS |
|---|---|---|---|
| 1 opener | A | V49 own (ends "The cheques are a shopping problem, not an investing one.") | 493 |
| | B | cut that line (Laura's Room 2-1, to pay for place 2) | 483 |
| 2 bounce | A | V49 own | 493 |
| | B | + "If it halves that deposit, our model bounces a cheque once in 66." (Laura's Room 2-1, LR-09 S9) | 506 |
| | C | + "Barring default, our model pays every cheque in full over 99 times in 100; in that recession, 98." (Kai, LR-09) | 511 |
| 3 range | A | V49 own | 493 |
| | B | the Window's bridge: "..., named a little under it, since a fund's payout isn't fixed to the dollar." | 507 |
| | C | Jun's (Library) with the bridge: "– and says which money pays each end" + bridge + "to sell any day" | 516 |
| 4 catch | A | V49 own ("before naming day"; Laura's Room: mis-timed) | 493 |
| | B | Laura's Room's repair 3-0 ("So in January 2031, before any co-sponsor hears a number, ...") | 494 |
| | C | Nora's (i), the Genius Lab's order swap ("Before she names it, the half she'll promise moves ...") | 491 |
| | D | V47 own ("On the day she names it ...") | 493 |
| 5 rival | A | V49 own + the linked world's pair ($85,000 v $135,000; every arm carries it) | 493 |
| | B | Kai's (Library), repaired to Felix's spec (cost against the rival first; "in our model" on $145,000) | 519 |
| | C | the Courtroom's callback: "that morning comes mid-slump" | 499 |
| | D | the Window's flat yes (W-06): "Does our floor cost her anything, then? Yes." | 498 |
| | E | the Kitchen's agreed value: "Sounds good, on average: market-value cover is always cheaper than agreed value." | 502 |

## The two outside readers (blind, other models; never saw sources, notes or which is newest)
| Place | Reader 1 (Haiku 5.5) | Reader 2 (Sonnet 5.5, a PM who distrusts marketing) | Both first |
|---|---|---|---|
| 1 opener | A > B | A > B | **A, keep the line** |
| 2 bounce | B > A > C | B > C > A | **B** |
| 3 range | C > B > A | C > B > A | **C** |
| 4 catch | B > A > C > D | B > C > D > A | **B** |
| 5 rival | B > C > D > A > E | C > D > A > E > B | split: **C** best on both (2nd, 1st); B first and last; E 4th-5th |

They agree in four places of five, which Commandment IX says to distrust a little: both are Claude models, briefed
alike. The disagreement that matters is place 5 B (Kai's cost-first paragraph): reader 1 liked that it "defines the
set-aside"; reader 2 called "the rival has a flaw – and we can say where" "marketing voice". Both would cut "Do not
crush." (reader 1: "only a reader who knows the label will get" it; reader 2: "a punchline after a pun that has
already been explained").

**Their flags on V49's fixed text** (not in any arm): "enough to grow back into all of it" and "The rest, the interest
they should earn" (both read twice); "set-aside" appears in the rival paragraph with no introduction, and P4's "take it
from what she keeps" doesn't explain why our bottom falls (reader 2) or sounds like the 2033 reserve (reader 1); "97 in
100" unexplained if the half is already in Treasuries (reader 2); "a fund's payout" read as the stock fund (reader 2);
"We'd pay the $15,000" asserted, not argued: the case's credibility line would argue it (reader 2).

**The readers' picks together: 536 strict, 39 over the 497 cap.** What pays is the huddle's question.

## How it landed (huddle H-012: Tess, Amara, Kai; 3 rounds + two cold paraphrase readers)
Round 2 voted 1A, 2B, 3A, 5C 3-0 and 4B 2-1; round 3's cold readers (Haiku 5.5, one per package, `cold_read_K.md`,
`cold_read_T.md`) gave the move's date and reason only under 4B, followed "our rival" without its heading, and showed
the set-aside fix failing its own test. Kai checked the model and found a false line in V49 itself; Tess landed it.

**Final package W1 = `final_package_W1.txt`, 497 strict** (494 by spaces; `python3 packages.py` rebuilds it; diff
against V49 in `final_package_W1.diff`). AI DRAFT (Claude, 1 Nov 2026); GPTZero not yet checked. Pitch unchanged (49).
Changes from V49:
1. P1 kept whole: "The cheques are a shopping problem, not an investing one." (3-0; both outside readers).
2. Heading "How to bounce a cheque" cut (3-0); "The US government defaults." cut (Tess, to pay; to the Final Report).
3. Added "If the recession halves that deposit, our model bounces a cheque once in 66." (LR-09 S9, MODEL; "the
   recession" is Kai's round-3 fix: three readers of four lost "it", and the deposit halved alone is 1 in 381).
4. P4 ends "take it from what she keeps, then the gift's floor, before she names a range." (Kai's fix, Tess's words;
   L-13 run.py:29 and the slide in L-15 run.py:92: what her half can't cover comes off the floor, so both ends step down).
5. P5 "enough to grow back into all of it" -> "**whatever the ladder didn't take**" (TRUTH: if the ladder costs more
   than $300,000 the 2028 deposit tops it up first; L-10 results.json: 46.9% of modelled futures, median $9,758;
   `IPS_number_sheet.md` line 14). "The rest, the interest" -> "The rest, **worth** the interest" (4 of 4 readers read it twice).
6. P7 -> Laura's Room's repair ("A range named on stocks has a catch ... So in January 2031, before any co-sponsor hears
   a number, Laura moves the promised half into Treasuries."), V49's 97 sentence kept.
7. Heading "Know thy rival" cut; "We know this rival" -> "We know our rival".
8. P9: "Matched in our model to our typical bottom, it leaves" (the $145,000 leaves the IPS; no bridge needed);
   "Sounds good, on average." cut; "that morning comes mid-slump, and" added (the Courtroom's callback); $85,000 v
   $135,000 (the linked world, Archive A26 S1); "after the set-aside" -> "after the shortfall".
9. "Do not crush." cut (3-0 in round 2; both outside readers). "it only works whole" stays (Kai's cut of it failed 1-2).

Landed by the host with no second vote: "the gift's floor", "whatever", "worth", and the default line + ", not after"
as the payment. Seed (Tess): three readers ask why the top is 97 and not 100 once the half is in Treasuries; L-13 has
the answer (the 2033 top-up after naming, a median miss of about $1,000, sent to the Final Report in V43).
