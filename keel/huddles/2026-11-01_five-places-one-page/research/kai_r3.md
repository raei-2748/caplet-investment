# Kai, round 3 research note (H-012, Sun 1 Nov 2026)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. MODEL = curve 22 Oct
2026, J.P. Morgan 2027 world stocks 7.5%, 200,000 paths, seed 20261016. Every number below is copied from the file
named; none is new. Package counts: `packages.py` copied to `/tmp/kai_r3/pk.py`, outputs written to /tmp only,
counted with `keel/office/tools/textcheck.py` `words_limit`.

## 1. What the 2031 shortfall cuts on V47/V49's design

| File, line | What it says | What it means for the sentence |
|---|---|---|
| `keel/rooms/lab/L-13_slide_the_range/run.py:29` | `u31 = ceil5(np.maximum(S31 + C - L33 - 0.5 * V31, 0))        # the 2031 mark's uncovered gap (cuts q_mc)` | Order: the 2027 leftover (`L33`), then her half (`0.5 * V31`); only the rest is "uncovered", and it cuts the quoted bottom. "What she keeps" covers the first two |
| `keel/rooms/long_room/LR8_banked_at_the_mark/run.py:31` | `q_mc = bottom - ceil5(np.maximum(S31 + C - L33 - 0.5 * V31, 0))` | The quoted bottom is the floor rule less that gap: the bottom goes under the floor |
| `keel/rooms/lab/L-13_slide_the_range/run.py:64` | `out13["A slide (top cut like the bottom)"] = arm(f5(top - u31), q_mc)` | Arm A, the slide: the same dollars come off the top too |
| `keel/rooms/lab/L-15_hold_it_then_say_it.md:9` | "V47's design = the L-13 slide + lock" | V47/V49 run arm A, so both ends drop |
| `keel/rooms/lab/L-15_hold_it_then_say_it/run.py:92` | `topN = f5(top - u31)` | Confirmed in the chain V49's 97-in-100 comes from |
| `keel/rooms/lab/L-13_slide_the_range/run.py:28` | `fg = np.minimum(nb - fh, lockd)` | In Jan 2033 the money physically leaves the gift's Treasuries (`lockd` = floor + moved half). This is why round 2's "the gift" was true but never said which end; nothing is sold from the floor in 2031 |
| `keel/rooms/lab/L-13_slide_the_range.md:51` | S1: "mark cut the bottom (median)" 18.4% ($10k) | The cut reaches the floor in about 18 linked futures in 100; the rest, what she keeps covers |
| `keel/rooms/lab/L-13_slide_the_range.md:91` | "the whole range steps down together, before she says it" | "The range" is the code's own word; zero words in P4, but it doesn't name the floor the readers asked about |

**Verdict:** "then the floor" is TRUE: V49's P6 builds both ends on the floor (bottom = floor, top adds half her stocks),
so taking the gap off the floor is the slide in the reader's own arithmetic. "The bottom" alone describes V29's bug
(L-13 base). Deduction in 2031, payment in 2033.

## 2. Does the 2028 floor grow back into "the full $150,000"?

| File, line | What it says | What it means |
|---|---|---|
| `keel/library/ips_numbers_2026-10/ips_numbers.py:10` | "$150k first fills any rung gap; the remainder R buys IBTM (Dec 2032) sized to pay back R (the floor)" | The floor's face is R, not $150,000 |
| `keel/rooms/lab/L-10_last_in_line/run.py:88` | `R = np.maximum(DEPOSIT28 - gap27, 0)` | Same rule in V47's chain (L-15 -> L-14 -> L-13 -> LR8 -> LR-05 -> L-11 -> L-10) |
| `keel/rooms/lab/L-10_last_in_line/results.json:23-24` | `"p_ladder_over_300k": 0.4693`, `"jan2027_gap_p50_when_positive": 9758` (S0, S1; 0.973 / $30,486 in S4, yields a point lower) | The floor is under $150,000 in about 47 futures in 100, by a median $9,758 when it is |
| `keel/library/ips_numbers_2026-10/IPS_number_sheet.md:14` | "$150,000 face, quoted as $145,000 ... If the ladder costs more than $300k, the 2028 deposit fills the gap first and the floor is lower by the same amount" | The office's own rule says no |
| V49 P2 / P4 (`keel/drafts/writing_room_2026-11-01/base_V49.txt`) | "all ten, or nearly"; "the 2028 deposit that was meant to top it up" | The IPS already tells the reader a top-up can come first, so "all of it" contradicts it |

**Verdict:** FALSE in about 47 of 100 futures. No floor figure. V49's "all of it" makes the same claim. True
replacement: "all the ladder didn't take" (+2).

## 3. "If it halves that deposit"

| File, line | What it says | What it means |
|---|---|---|
| `keel/rooms/lauras_room/LR-09_the_promise_has_no_number.md:55` | S9 "S4 and S2 together, linked": 98.49% paid in full, 1 in 66 | The 1 in 66 needs both: yields a point lower before the build AND the deposit halved |
| same, line 52 | S2 deposit halved alone: 1 in 381 | A wording without the recession is false |
| same, line 53 | S4 yields a point lower alone: 1 in 1,905 | |
| same, line 57 | "Identical with or without the 2031 lock in five worlds of six" | The cheques don't need the 2031 step: used against "it only works whole" |

**Verdict:** "If the recession halves that deposit" (+1) is true to S9: "the recession" is P4's own, already pushing
yields down. Open, not fixed here: the IPS never says how far yields fall (the model's is a point); Final Report.

## 4. Counts (strict, `words_limit`)
Package K 497 -> +1 (recession) +1 (floor, "a range") +2 ("all the ladder didn't take") = 501 -> drop ", and it only
works whole" (-5) = **496**. Second back: drop "that morning comes mid-slump, and" (495), but that overturns place 5 C (3-0).
