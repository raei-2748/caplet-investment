# FICTION (the room) + real drafts. The Writing Room

## Now
- **Doing:** round 2 beat 7 (29 Oct): the four doors as claims and as three counted V29 texts, read blind by three cold readers (`../ips_rewrite/inbox/2026-10-29_writing-room.md`)
- **Decided:** lean B for Saturday: V29's needs line becomes an order and a clock ("Every rule here fires in a year the case already set, never on a hunch; if needs change, the gift takes it before it is named, her half after, a cheque last"); 3 of 3 readers advanced it. Price: the range's two embarrassments go FR-first
- **Next:** Fri 30 Oct: the Courtroom's verdict and the Lab's door-4 count into B; Sat 31 Oct review read of the near-final
- **For the judges:** four hard fixes in V29 ("never changes", "carries risk", "$300,000 buys them", "three times worse") and a framework a judge can point to
- **Updated:** 2026-10-29 17:20 Sydney


> AI DRAFT material throughout (Claude); not for submission as written. (Keel is a simulated team, AI-written.)

> Room card: `../OFFICE.md`. Host: Tess (cuts the fat, runs the counts); Amara writes first drafts. Agents:
> `format-gatekeeper`, `final-report-planner`. Tools: `../office/tools/textcheck.py`, `../VOICE.md`.
> Rule: flag only hard issues (limits, rule breaches, facts, numbers, formatting) with minimal edits; never reword
> for taste or soften a confident claim. Suggestions stay in the repo; never touch the Google Docs.

> **State (Thu 29 Oct, 16:20 run):** beat 7 done; texts + `build.py` + `cold_reads.md` in `../drafts/writing_room_2026-10-29/` (rerun `build.py` after any V29 change). Open to this room: nothing.
>
> **State (Wed 28 Oct, 16:20 run):** beat 7 done; splices + script in `../drafts/writing_room_2026-10-28/` (rerun `splice_arms.py` after any V28 change). Open to this room: nothing; the Long Room's verdict tonight decides which splice the rewrite gets.
>
> **State (Tue 27 Oct, 17:10 run):** P06 done on the day-2 spine (not D4: the thinking moved). Kept lines and the
> "three kickers only" rule are in the 27 Oct inbox note. `textcheck.py` now says to quote the LARGER count (spaced
> dashes count by spaces). Open to this room: nothing urgent; Sat 31 Oct review.
>
> **State (Mon 26 Oct, 16:30 run):** v4/v4.1 work stopped (Ray, 26 Oct); the room serves the rewrite
> (`../ips_rewrite/`). Built `textcheck.py --voice` (R03 habits flagged, rhythm info only; Orwell control 0 flags, TNA 4,
> v4.1 1). Open to this room: the Lab's one-line explanation (after WO-R2, Thu 29 Oct). Next: Draft 1 lands Fri 30 Oct;
> on 31 Oct run counts + `--voice` + the "and so?" read (HOLE/FAT list, no rewording) and list at most 5 hard issues.

## Runs
| Date | Draft checked | Counts (strict) | Hard issues | Memo |
|---|---|---|---|---|
| Sat 24 Oct | IPS edits v2 (E1-E12 + K1-K5) | pitch 47; IPS 494; +A 508; +A +package 1 +fix 2 = 467 | 4: option A over 500; K4 dates; "secures"; "bond" for ETFs | `../office/outbox/2026-10-24_writing-room_option-a-cut.md` |
| Sat 24 Oct (evening) | IPS v3 (v2 + Lab C1-C3, roots-free, [NAME] placeholder) | pitch 45; IPS 471 (467 by spaces); 0 overclaim; 2 en dashes | K4 dates and "holding" fixed; option A now fits under 500 with no cut; pitch "held to maturity" loose for ETFs; 2 lines flagged as still AI-sounding, both rewritten | `lab/L-05_ips_push/ips_v3.md`, `/mnt/project-files/ips/IPS_edits_v3_2026-10-24.md` |
| Sun 25 Oct (16:30) | IPS v4 R + Package B, five rooms' requests | pitch 37; IPS 480 (486 with P5 finish) | 5: F1 creative residency; F2 coupons trade; "equal to"; P5 order if no D1; B's "built six years early" and "each January" | `../office/outbox/2026-10-25_writing-room_v4-1-vote-copy.md` |
| Mon 26 Oct (16:30) | rewrite inbox lines (Laura's Room item 8, Lab item 5); voice meter on TNA, v4.1, Orwell | 22 / 23 strict | 3: "in the bank" vs NAV payout; line D1b-only; Lab line vs frozen WInS book (WO-R2) | `../office/outbox/2026-10-26_writing-room_voice-meter.md` |

| Tue 27 Oct (17:10) | 18 candidate lines for six spine slots + D4 | D4 498 by spaces (494 split; earlier runs quoted the smaller) | 5: "ten Treasuries"; counts quoted low; "We buy the rate"; "the one way it fails"; D4 inflation/TWD HOLE | `../office/outbox/2026-10-27_writing-room_cold-read.md` |
| Wed 28 Oct (16:20) | V28 (D8) + three soft-spot splices (C6, C6+MC, A) | V28 499 by spaces, pitch 50; splices 495 / 498 / 500 | 5: count margin 1/0; first $300k one-close fact; Laura's half double-booked; 2031 lock 'Treasuries maturing before 2033' (none on WInS); six quotable endings (cut one) | `../office/outbox/2026-10-28_writing-room_three-cures-side-by-side.md` |
| Thu 29 Oct (16:20) | V29 (D9) + three texts (A hard fixes; B four doors; C B with the range kept) | V29 495, pitch 48; A 499, B 498, C 497 | 4 + reader notes: "never changes"; "carries risk" (57%); "$300,000 buys them" (3 readers); "three times" stale (six); "what's left", "one dollar in fifteen" | `../office/outbox/2026-10-29_writing-room_the-order-and-the-clock.md` |

## Tool changes
- 27 Oct: `words_limit()` = the larger of the two counts; the summary line says "quote the larger"; the portal's IPS
  word counts use it (a spaced en dash is a word by spaces, so the split count was the SMALLER one: D4 494 vs 498).
- 26 Oct: `--voice` meter (R03 habits). Rhythm metrics were dropped as flags after they fired 5 times on Orwell.
- 24 Oct: `textcheck.py` overclaim list now also catches "secures" and "guarantees" (it matched whole words only, so
  "secured" missed "secures").
