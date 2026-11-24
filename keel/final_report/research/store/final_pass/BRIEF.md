# The store's final judgement pass: the brief for raters (Wed 25 Nov 2026, morning)

The writing session starts Fri 27 Nov. Before then every idea in the store must be kept, adapted, merged or refused
with a reason, so nothing is lost and nothing stale reaches the writers. Of 10,876 rows, 828 were never judged: they
carry only the first pass (fit from the old clash column, clarity set at 3, no note). They come from the early harvest
files (`../../harvest/H1`-`H10`, 9-10 Nov) and a few early cards (Q1, Q6b-Q6d, Q7b-Q7c, Q39, NUM_extras). Many were
written before Caplet's own IPS was final or before the numbers were re-sized, so expect a good share to be twins of
later, stronger rows (merged) or superseded (refused, with the reason).

## Read first

1. `RATER_BRIEF_R2.md` (this folder's parent): the scale (F, R, S, C, each 1-5; score = 2F + R + S + C), the four
   statuses and the CSV format. Follow it exactly, except that your note starts **"Wed 25 Nov (final pass):"**.
2. The plan as it now stands: `../../../ARGUMENT_TREE.md` (wins over SKELETON where they differ), `../../../SKELETON.md`
   (the parts 2.0-2.5, 3.0, 3a-3f), `../../../WORDS.md` (the one plain name for each thing), `../../../NUMBERS.md`
   sections 0-5 (the figures), `../../../CANON.md` (what the submitted IPS, Trading Notes and portfolio commit Caplet
   to), and `../../../FINAL_IPS_as_submitted.txt` whole.

## Your rows

Your batch file (`batch_<your letter>.txt`, here in `final_pass/`) lists one store id per line. For each id, read its
row in `../insights.jsonl` (fields idea, sources, use, critique, verified, clash, where, file) and, where the row is
unclear, the source table row in its `file`. Judge it as it stands today:

- **keep**: true, fits a part, and says something no stronger row already says. Name the part in the note.
- **adapt**: true and useful, but a figure, a name or the plan it assumes has changed. Say exactly what changes (for
  example: "uses the 9 Nov $21,000 margin, void since 10 Nov; the standard is now NUMBERS 2").
- **merged**: a twin of a stronger row. Find that row (grep `../insights.jsonl` for its key words; later cards from
  Q40 onward usually hold the stronger version) and put its id in merged_into.
- **refuse**: false, or built on a design Caplet did not submit (STRIPS, TIPS, a 2031 lock or cushion, a growth-first
  plan, a fixed $150,000 floor, Caplet XR, the tablet motif), or breaks a standing ban. Say which, in a few words.

Ideas are judged, not words: an old row with a good idea in old words is adapt or merged, never refuse. A row about
Keel's own office, rooms or process with no use in the report is keep at F 1 with the note "store only: office
process, no part", so it stays findable.

## Write

`../digest/ratings_R2_<your letter>.csv`, no header, one line per id in your batch, in the batch's order. Do not edit
any other file. Report back in under 150 words: rows rated, counts by status, and the five highest-scoring ids with
one line each.
