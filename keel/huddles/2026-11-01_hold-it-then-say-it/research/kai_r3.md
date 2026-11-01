# FICTION. Kai's round-3 check notes (H-010, Sun 1 Nov 2026)

> Keel is a simulated team, AI-written. Numbers are MODEL output from `lab_results.md` (L-15; curve 22 Oct 2026,
> J.P. Morgan 2027 world stocks 7.5%, 200,000 paths, seed 20261016; S0 / S1 / S6). Nothing here is a Caplet deliverable.

## Question checked
Does A's sentence ("Before she names it, the half she will promise moves into Treasuries, and in our model the gift
reaches its top about 97 times in 100") contradict a locked Trading Notes line or the case?

## What I opened, and the lines I relied on
1. `keel/ips_rewrite/00_GROUND_TRUTH.md`, section 3 (the locked TNA lines), lines 60-75:
   - l.66-67, Note 2 (IBTM): "does two jobs": first payment + "a floor for her facility contribution, giving co-sponsors
     a minimum figure in 2031".
   - l.70-71, Note 3 (VT): stocks "only set how far her gift rises above her promised minimum"; "a rise before 2031 lifts
     the top of the range co-sponsors hear".
   - l.78-79: "So the IPS is bound to: ... a promised minimum; a 2031 range whose top moves with stocks".
2. `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, lines 109-120:
   - l.109: "Laura plans to begin approaching potential co-sponsors in 2031, two years before the residency is established."
   - l.114: "If Laura promises more than she can ultimately contribute, she could damage her credibility ..."
   - l.117-118: "Teams must recommend the dollar range Laura should communicate and state how confident they are that her
     2033 contribution will fall within that range."
   - l.119-120: "The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment."
3. `keel/WHARTON_WORD.md` l.85-86: "**Not expected in the IPS** (they belong to the Final Report): "final
   operating-reserve calculations, detailed portfolio projections, a final facility-contribution range, or the draft
   communication to co-sponsors.""
4. `keel/ips_rewrite/drafts/D27/ips_V47.txt` (P6 opens "In 2031 she gives co-sponsors a range."; P7's last sentence is
   the one A replaces).
5. `keel/ips_rewrite/IDEA_BANK.md` row 106 (l.255): the clause "even in a week when stocks are rising"; its own risks
   column: "Not earned until the Lab's lock-timing and order tests run."
6. `lab_results.md`: A table (same day 97.9 / 97.6 / 96.0; a week late 97.7 / 97.4 / 95.9; wait while it rises
   97.6 / 97.4 / 95.9; inside skipped paths 85.8 / 85.1 / 89.2 v 98.5 / 98.6 / 96.4; move first, name later identical
   path for path); B table (S0 fifths -$27,896 / -$5,352 / +$11,069 / +$29,929 / +$66,837; S6 best fifth +68%,
   fifth 2 +$1,737); C table (inside the range 200,000 / 200,000 / 199,999 of 200,000). Its two corrections noted:
   the CORD on "never broken in any arm" (S6 has 1 path of 200,000 under the bottom), and the year-late arm restated
   as an identity on L-12's lock rule, not a reproduction of L-12's number.

## Finding
- **No contradiction.** Under A the half moves in 2031, just before naming, so every rise before 2031 is already in
  the half that moves: Note 3's "a rise before 2031 lifts the top" holds. Note 2's floor (the bottom) is not touched.
  The case's "begin approaching ... in 2031" (meetings, plural) is served better: every meeting hears money already
  in Treasuries. Our model: move first, name later = same day, path for path (97.9 / 97.6 / 96.0).
- **Where it could break (not proof against A, but a dependency):** A's sentence carries no year. It relies on P6's
  "In 2031". If that phrase were cut, "before she names it" could read as a move in 2030; a rise after such a move
  would not lift the top, and Note 3's line would then be false. Keep P6's "In 2031".
- **C and Wharton:** C's added claim is confidence that the gift falls inside the range, i.e. the final range's
  confidence. WHARTON_WORD l.85-86 puts "a final facility-contribution range" in the Final Report. Not banned in the
  IPS, but not expected there, and both C versions break the 497 cap.
- **B:** Jun's "outside the best fifth its lead averages under $2,000" checks in S0: (-27,896 - 5,352 + 11,069
  + 29,929) / 4 = $1,937.50. S1 is "the same within $3k a cell" (not exactly checkable from the page). S6 breaks it
  (fifth 2 +$1,737; best fifth only +68% of a $27,114 mean lead, which leaves the other four fifths averaging about
  $10,800 by my arithmetic from those two numbers).

## Counts (`keel/office/tools/textcheck.py`; the larger, hyphen-split count is the strict one)
```
A:  "Before she names it, the half she will promise moves into Treasuries, and in our model the gift reaches its top about 97 times in 100."
    words: 26 by spaces (a spaced dash counts), 26 split on hyphens; quote the larger
V47 P7 last sentence ("On the day she names it, the half she promised moves into Treasuries, and in our model the gift reaches its top about 97 times in 100.")
    words: 27 by spaces (a spaced dash counts), 27 split on hyphens; quote the larger
V47 whole file (ips_V47.txt)
    words: 494 by spaces (a spaced dash counts), 497 split on hyphens; quote the larger
Jun's C ("On the day she names it, the half she promised moves into Treasuries; in our model the gift lands inside the range in every path bar one, and at its top about 97 times in 100.")
    words: 36 by spaces, 36 split on hyphens  -> +9 -> 506
Nora's C ("On the day she names it, the half she promised moves into Treasuries, and in our model the gift lands within that range in all but one of 600,000 paths.")
    words: 30 by spaces, 30 split on hyphens  -> +3 -> 500
#106 clause ("even in a week when stocks are rising")
    words: 8 by spaces, 8 split on hyphens   -> +8 on A's 496 -> 504
Kai's r3 post: 309 by spaces, 316 split on hyphens
```
So V47 with A = 497 - 27 + 26 = **496 strict**, inside the 497 rule. C (either version) and #106's clause both break it.

## Verdicts (as posted)
A ADOPT; B PARK (Final Report); C PARK (Final Report); #106's clause BIN (a week's slip 0.2 points, wait while it
rises 0.3, under the brief's own 1-point bar; under A no promised half sits through a rising week).
