# Jun, round 3 check notes (H-010, Sun 1 Nov 2026; FICTION, Keel is a simulated team, AI-written; numbers are MODEL output)

Stamp for every model number: curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% | 200,000 paths, seed 20261016
(bridge draws 20261101) | V47's design | S0 unless named | MODEL. Model not re-run; numbers read from `results.json`.

## Files opened
- `keel/members/jun.md` (above "## Agent profile")
- `keel/huddles/2026-11-01_hold-it-then-say-it/BRIEF.md`; posts `r1_jun/kai/nora.md`, `r2_jun/kai/nora.md`
- `keel/huddles/2026-11-01_hold-it-then-say-it/research/lab_results.md` (both fixes seen: line 8, the year-late arm is
  "an identity ... not a reproduction of L-12's number" (my round-2 audit); line 28, CORD (Kai, round 2), "never broken
  in any arm" corrected to S6's one path)
- `keel/WHARTON_WORD.md` (lines 49-56 the questions; 71-72 "rather than ... detailed financial calculations"; 85-86
  "Not expected in the IPS")
- `competition/official/2026_27/UPDATED_2026_WGY_Investment_Policy_FINAL.txt` lines 50-75
- `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` lines 68-72 and 105-122
- `keel/ips_rewrite/drafts/D27/ips_V47.txt` and `README.md`; `keel/ips_rewrite/README.md` line 13 (word rule)
- `keel/ips_rewrite/judges/panel_V46/SUMMARY.md` line 22; `keel/ips_rewrite/IDEA_BANK.md` line 255 (#106)
- `keel/rooms/lab/L-15_hold_it_then_say_it/results.json`

## Exact lines relied on
- IPS instructions lines 69-71: "The IPS is not expected to include final operating-reserve calculations, detailed
  portfolio projections, a final facility-contribution range, or the draft communication to co-sponsors. These elements
  will be developed and supported in the Final Report using the strategy established in the IPS."
- Lines 54-55: "Focus on the strategy and decision-making framework that guide your portfolio rather than describing
  individual investments or presenting detailed financial calculations."
- Lines 50-52: the IPS should "establish your strategic approach to ... determining a responsible facility contribution".
- Case lines 117-118: "Teams must recommend the dollar range Laura should communicate and state how confident they are
  that her 2033 contribution will fall within that range." Case line 70: "willing to take thoughtful risks throughout
  her entrepreneurial career".
- `keel/ips_rewrite/README.md` line 13: "the final IPS stays at most 497 words on the stricter count".
- Panel V46 SUMMARY line 22: 97 in 100 named by J3, J4, J5.

## Verdict on the check
- A confidence-within-the-range number answers the case's requirement attached to the final range, which lines 69-71
  defer to the Final Report. "Not expected" is not "banned", but it spends IPS words on Final Report work, and inside
  the IPS it is near-true by construction (owned bottom, capped top). This goes against my round-2 lean (C).
- V47's "97 in 100" names no range and no dollar figure; it is one rounded reliability number for one rule (the lock),
  i.e. framework, not "detailed financial calculations". Inside what Wharton asks, at the edge. Keep.
- Round-2 error: I wrote "506, six to cut" against a 500 cap; the cap is 497, so nine to cut.

## Counts (`keel/office/tools/textcheck.py`, strict = hyphen-split)
| Text | Strict |
|---|---|
| V47 whole | 497 (494 by spaces) |
| V47 P7 last sentence ("On the day she names it, ...") | 27 |
| A, Kai's: "Before she names it, the half she will promise moves into Treasuries, and in our model the gift reaches its top about 97 times in 100." | 26 |
| C, Jun's full sentence ("On the day ... Treasuries; in our model the gift lands inside the range in every path bar one, and at its top about 97 times in 100.") | 36 (+9) |
| C, Nora's ("... lands within that range in all but one of 600,000 paths.") | 30 (+3) |
| V47 with A | 496 |
| V47 with Jun's C | 506 |
| V47 with Jun's C, minus "Laura has taken thoughtful risks all her career, so" (9) | 497 |
| Other whole ideas checked: "and we made it first: our first plan was three-quarters stocks, until our own model sank it." | 18 (too big; the only learning line) |
| "The US government defaults." | 4 (too small; the residual risk) |
The idea C costs: the rival's reason in the case's own words (Client Knowledge). Nora's +3 version instead costs the
97 in 100 itself.

## Numbers checked in results.json (S0 / S1 / S6)
- Top reached: same day 0.979 / 0.976 / 0.9602; week late 0.9773 (S0: 0.17 points, shown 97.9 to 97.7); wait while it
  rises 0.976 (0.3 points); move first, name later: identical_to_same_day true.
- Skipped after a top-fifth 2030, inside the skipped paths: 0.8581 v 0.9845 if moved (S0).
- B, primary 2028-30 sort, mean lead of fifths 1-4 (equal fifths, so their average is the mean outside the best fifth):
  S0 (-27,896 - 5,352 + 11,069 + 29,929)/4 = $1,938; S1 (-28,869 - 5,740 + 11,363 + 30,815)/4 = $1,892;
  S6 (-24,361 + 1,737 + 21,487 + 44,643)/4 = $10,877. Under $2,000 holds in S0 and S1 only.
- C: p_inside_range 1.0 / 1.0 / 1.0 (rounded); paths below the quoted bottom 0 / 0 / 1 of 200,000; misses under $5,000
  98.38 / 98.69 / 98.19%. Also noted: p_below_unrounded_top 0.9998 (S0), so "reaches its top" is the top rounded down;
  the 97 in 100 is honest only because the quoted top is the rounded one. Not for the IPS.
