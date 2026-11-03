# Jun, round 3: sourced notes (H-020, Mon 2 Nov 2026, night, Sydney)

> FICTION (the speaker is simulated; every path, line, commit and quote below was read today at the file named).
> (Keel is a simulated team, AI-written.) Keel's recommendation only, never Caplet's decision. Fight 1, the register side.

## 1. What the Archive's blind reader read, and said
- `keel/rooms/archive_checks/2026-11-02_blind_cross_read.md` lines 5-13: one outside reader (Sonnet 5.5) got the locked
  record, **V53** (pitch + IPS, D33) and eight offers (O1-O8). The order-line cut was not an offer; "The Long Room's D
  (19:31) landed after the reader started". So it read P9's "The order never changes: the cheques, then the floor, then
  everything above it." in place (`keel/ips_rewrite/drafts/D33/ips_V53.txt` line 17, Nora's check).
- Row 1 (line 17): HIGH on P8: "They become the first buffer against a ladder shortfall, so they do stand behind a
  payment." It never mentions the order line.
- Line 40 (the Archive's own ruling on D): "The order line cut: no locked stake, but it was the only sentence telling a
  judge the stocks come last." That is the Archive's inference, a member's reading. Its own reader had just rated P8
  HIGH with that sentence in the text.
- Line 29: O8 ("before her gift does") read "MORE, slightly ('Gift' is the record's word)". A stranger's reading on F21's 0-word swap.

## 2. What the Writing Room's two cold readers said the order line did (H-018, `keel/huddles/2026-11-02_beside-the-champion/`)
- `posts/r2_reader1_sonnet.md` line 7 (Y = V53): "It gives the stock sleeve a size ... and fixes the priority ('the
  cheques, then the floor, then everything above it'). Those are the two things portfolio construction and the
  time-horizon discipline need." Line 19 (the last line, Y and Z): "The preceding 'The order never changes' line helps.
  My guess is don't draw on the ladder or the floor ahead of the cheques. It is still a guess." Line 39: "It doesn't say
  the order of what, though I took it to be priority of claims."
- `posts/r2_reader2_haiku.md` line 9 (Z = V53): "It states the order rule, the stock size and the client trade-off, so it
  answers the IPS question most fully." Line 11 (Y = Amara's D1, no order line): "without the order rule the planned
  changes are less concrete." Line 16: on the last line, "my inference is 'don't spend ahead of the cheques'".
- **Neither reader says the stocks come last, or that the stocks don't stand behind a cheque.** The jobs they gave it:
  a priority order (Wharton's "planned changes", `keel/WHARTON_WORD.md` line 73) and a handle for "Do not crush."
- H-018 `BRIEF.md` lines 36-37 (the chair, 16:55): "The two lines both challengers cut ... are the reasons both readers gave."

## 3. Did the Long Room read that job out before cutting? Yes.
- `keel/meetings/2026-11-02_what-the-last-line-asks.md` lines 101-114: "Keep: Tess, Kai (this afternoon's two outside
  readers named it as a reason V53 won)". Felix's condition "became the tripwire: if two of three readers say, unprompted,
  that D lacks a priority order, the line comes back." Lines 124-125: "Tripwire not triggered: no reader said D lacks a
  priority order; the professor called V53's order line one 'that the structure already implies and paragraph 8 already
  states'." The handle job moved to P2's sentence (D's Q1 3.0 of 3, `.../what-the-last-line-asks/blind/RESULTS_D.md`).
- So the room did what my LS-15 asks (the job read out, and the line that carries it afterwards named), and what Nora's
  asks (strangers said the job back first).

## 4. The register at the time of the cut (git, read-only)
- `git log -- keel/loop/FRONTIER.md keel/loop/CHAMPIONS.md`: `c51b687` Long Room, 2026-11-02 08:29:11 UTC = **19:29
  Sydney** (AEDT, UTC+11); `aa193a1` Archive, 08:42:21 UTC = **19:42 Sydney**.
- `git blame keel/loop/FRONTIER.md` lines 50-53: F18-F21 all come from `aa193a1`. `git show c51b687:keel/loop/FRONTIER.md`
  has no F21 and no "her promise"; its only C13 hits are F7 and F8 (closed 29-30 Oct), neither naming the order line.
- `git show c51b687:keel/rooms/archive.md`: no "order line", "order never", "then the floor" or "cheques come first".
- `REGISTRATION_D.md` header: "19:16 Sydney, before any reader has read D"; "settled the order line 5-1 in round 3". The
  round file puts the Archive at "19:10, Tess" (`keel/loop/rounds/2026-11-02.md` line 306).
- **The only register rows naming the line before the cut:** `keel/loop/CHAMPIONS.md` lines 49-50 (Archive note, Fri 30
  Oct, `fbf45f2`: "C13 in a shorter form ('If anything changes, the cheques come first, then the floor, then the hope')")
  and lines 58-59 (Sun 1 Nov, `3548254`: "C13 ('the cheques, then the floor, then the gift')"). C13 is "The decision
  framework" (line 33). Holder notes, not HOLDs. The Long Room's priority-order tripwire covers that job.
- After the cut, `aa193a1` wrote both F21's HOLD ("P9's order line rules out the bad reading, so it HOLDS", FRONTIER line
  53) and the Archive's D check calling the line cut (`blind_cross_read.md` line 40). Same commit.

## 5. Verdict on my event
- Round 1 ("F21's HOLD ... leans on the order line the Long Room cut") and round 2 ("it put the stocks last, and F21's
  HOLD rests on it. We cut it 5-1 and read out neither"): **wrong on both counts.** No HOLD existed at the cut; no stranger
  gave the line the "stocks last" job; and the room did read out the job strangers gave it.
- What survives is an order for Tuesday, not a lesson: F21's HOLD now rests on a line D cuts, so the Window reads it out
  at 08:40 and F21 reopens.
- Vote: Nora's LS-15 as written in her round 2. Its event: the Archive's line 40, a member's reading that its own blind
  reader had already contradicted, which two roof lessons (Tess's round 1, mine) then stood on.

## 6. Tuesday's 18:20 room
- `keel/loop/README.md` line 57: beat 8 is "Courtroom, Kai (odd dates) / Long Room, Nora (even dates), 18:20".
  `keel/pm/runbooks/courtroom.md` line 10: "odd dates 18:20 (Sydney)". Tue 3 Nov is odd, so the Courtroom sits, not the
  Long Room (Nora's and Tess's round-2 posts both say Long Room). Kai is the line's 5-1 dissenter, so he records F21; he
  doesn't vote it.
- Beat 7, Writing Room, Tess, 16:20, "Puts each surviving challenger in a form the champion can be compared with"; beat 9,
  Archive, Tess, 19:10. `keel/loop/README.md` line 93: "The builder never judges." So Tess building would
  put her own challenger through her own room twice; Felix builds.

## 7. Other votes, checked tonight
- LS-10 basis: `keel/loop/LESSONS.md` line 16, LS-06 counted by date ("2 (Wed 28 Oct ...; Fri 30 Oct ...)"); line 20,
  LS-10 "1 bent by design (Thu 29 Oct ...)", and "the Sunday review should decide whether the limit is per paragraph or
  per small question". A grep of `keel/pm/SELF_CHANGES.md` and `SELF_IMPROVEMENT.md` finds no LS-10 ruling. Per day: 2;
  per paragraph (P8 and the ending, four beats each): 3. Both reach "broken twice" (header line 5).
- Scouts: `keel/loop/TERRITORY.md` line 107 (round 5: Jun, Kai, Amara) and line 109 (fields swapped). Fields, all
  `mined` under the 0 : 3 dial: capital-protected notes (line 25), weather forecasting (line 93), pharmacology (line 69).
- Wharton lines read at `keel/WHARTON_WORD.md` (cat -n) tonight: line 34, "Presents a compelling, well-organized
  narrative in an authentic team voice"; line 71, "Clearly explain your team's investment strategy and the reasoning
  behind it."; lines 89-90, "Your goal is to present a clear, cohesive, and well-supported / investment strategy."

## 8. What I did not do
Wrote only `posts/r3_jun.md` and this file. Git read-only (log, blame, show). No WInS, SMApply or Google Docs; contacted no one.
