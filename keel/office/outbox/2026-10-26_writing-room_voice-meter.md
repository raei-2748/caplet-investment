# The Writing Room, Mon 26 Oct 2026: a voice meter for Draft 1, tested on a human, and three hard issues

(Keel is a simulated team, AI-written.) AI DRAFT material (Claude, 26 Oct 2026); not for submission. Suggestions stay
in the repo; no Google Doc touched. Serves the IPS rewrite (`../../ips_rewrite/`), Draft 1 due Fri 30 Oct.

## Why this, today
No rewrite draft exists yet, and Ray stopped all work on v4/v4.1 (26 Oct). WO-R3 (the voice study) was done in the
rewrite thread (`../../ips_rewrite/research/R03_voice_study.md`, now on the day branch too). So the room's best move
was to turn R03 into a check Draft 1 can be run through on 31 Oct in seconds, and to test that check honestly first.

## What was built
`textcheck.py --voice` (two new tests; `toolkit/tests/office/test_textcheck.py`, 7 pass). It prints sentence rhythm
as information and flags only R03 habits: "X, not Y" / "rather than", lists of three, stock connectives ("notably",
"in other words", "meaning"), abstract-noun density, a thesis-first opening ("This policy ..."), and no turn (no
sentence opens with But, Yet or Still: no sceptic voiced and answered).

## The test, and the surprise
| Text | Who wrote it | Rhythm spread | Habit flags |
|---|---|---|---|
| Locked TNA reflections (3, 297 words) | AI-assisted; detectors said 100% AI | 36% | 4: two "X, not Y", two lists of three, four stock connectives, no turn |
| IPS v4.1 `ips.txt` (480 strict) | AI | 38% | 1: opens on "This policy governs" |
| Orwell, opening of "Politics and the English Language" (228 words; scratch only, not committed) | Human | 34% | 0 |

1. **Rhythm is not the tell.** Orwell's sentences are as even as the TNA's (34% vs 36% spread, no line under 7
   words). The first build flagged him five times, so rhythm is now printed, never flagged. "Vary your sentence
   length" is advice detectors made popular; it is not what separates these texts.
2. **Argument moves are the tell.** Every flag that fired on the TNA and not on Orwell is a move, not a measure:
   the stacked contrast, the tricolon, the "in other words" that explains the sentence just written, and the
   missing "But".
3. **The meter passes v4.1, and Ray rejected v4.1.** So the meter is a floor, not a target. A clean Draft 1 can still
   miss every north star; that is Nora's panel's call on 31 Oct, not a script's.

## Three hard issues in the newest draft lines filed to the rewrite (minimal edits only)
| # | Line (room) | Issue | Minimal edit |
|---|---|---|---|
| H1 | "The bottom of her range is in the bank" (Laura's Room, inbox 26 Oct, item 8) | Fact vs locked TNA 2: the floor is IBTM, whose payout is "a net asset value, as opposed to a promise of par" and "not fixed"; "in the bank" says a fixed deposit | "in the bank" -> "already bought" (-1 word; 22 strict). Same strength, true |
| H2 | Same line, "Laura pledges only what she already holds" | True only if D1b wins: under D1a the floor is the last source for a coupon gap, so a pledged floor can be drawn (LR-03 point 4 says so) | No word change; tag the line "D1b only" in the synthesis memo |
| H3 | "We size the ladder from 2042 backwards, so every coupon pays a named payment ..." (Genius Lab, inbox 26 Oct, item 5; 23 strict) | Coherence: form :75 says the portfolio should reflect the IPS; the frozen WInS book is sized rung by rung unless ~10 trades move ~$52k before the freeze (Keel default: no trades). Already before the Courtroom (WO-R2, Lab request, Wed 28 Oct) | If the Courtroom clears it with no trades, open with "In January 2027," (+3) so the line describes Laura's real build, not the WInS book. The Courtroom decides; this is the shortest true fix if it says yes |

Overclaim words in both lines: 0. Non-ASCII: 0.

## Requests closed as superseded (Ray, 26 Oct: no counts, cuts or reads of v4/v4.1)
The D1b cut in `ips_two_dials.txt`; the "and so?" read on v4.1 (re-aimed: the room runs it on Draft 1 on 31 Oct);
the Archive's Package B "release" check.

## Takes for Nora's 07:00 brief
Tess: I built a lie detector and the first person it caught was George Orwell. Good. Now we know the even rhythm
was never the problem; the TNA's problem was that it explained itself twice and never once said "But".

Amara: Fair cop on "in the bank". It's a Treasury fund that pays what it's worth, and the locked note already says
so. "Already bought" is shorter and still lands. Tag it D1b; if the floor can be raided, I'm not letting Laura
pledge it.
