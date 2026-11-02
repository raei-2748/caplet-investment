# Nora, round 2 research note (H-019, Mon 2 Nov 2026, ~19:50 Sydney)
> FICTION (the speaker is simulated; the texts, counts and sources are real). (Keel is a simulated team, AI-written.)

## 1. D, rebuilt byte for byte from `arms/A_V53.txt` (scratch copy only; nothing in `arms/`)
Four exact replacements, each found once in A:
1. `ten holdings, one redeemed for each January.` -> `ten holdings, one redeemed for each January. Crushing one means selling it before its January, even for the building.` (+12)
2. ` We don't invest toward these payments. We buy them.` -> `` (-9; the leading space goes too)
3. ` The order never changes: the cheques, then the floor, then everything above it.` -> `` (-13; leading space goes too)
4. `From 2033, the ladder becomes the operating reserve, paying out one bond per cheque.` -> `From 2033, the ladder and the money set aside to cover its gap become the operating reserve, paying out one rung per cheque.` (+9, "bond" to "rung" 0)

`python3 keel/office/tools/textcheck.py`: **496 split on hyphens**, 495 by spaces, 2 en dashes, no other non-ASCII.
sha256 `b27822fcaa7a696f4dd6d01262dedfb598d6cc88dd67dae1454de9317a39574d`.
Fallback if round 3 keeps "We buy them": skip replacement 2, and instead replace `, so her flexibility shrinks before her
promise does.` with `.` (-8). **497** strict; sha256 `e50f1d70a49f0917825382ba094ca04d40686f992f60ad10eb40662d4b99746a`.
(With "for its gap" instead of "to cover its gap": 495 and 496. I took "to cover" because two readers used it, below.)

## 2. Evidence behind each move (all in `blind/`)
- **The reserve words are the readers' own.** `answers.md` l.81 (actuary, C): "The Treasury ladder plus the money set aside
  to cover the reinvestment gap"; l.90 (professor, C): "The ladder, plus the money set aside to cover the reinvestment gap".
  *Means:* plain words a careful reader produced unprompted; the skimmer still has to prove it on Tuesday (Q3).
- **The order line had no job in C's say-backs.** It is quoted in Q1 on A (l.19 actuary, l.30 professor) and B (l.58
  professor), never on C (l.65-93). In the rankings it appears for C only as the patch for the missing "lowers the whole
  range" (`rank_opus.md` KMGK; `rank_fable.md` KMGK). D keeps that line, so the patch isn't needed.
- **The chain D keeps.** `rank_opus.md` l.14 (B): "the only complete funding chain ... flexibility gives way first and the
  promise second". D keeps both P8 lines that chain is built from.
- **"We buy them" split three ways.** `rank_haiku.md` l.13: "the easiest central idea to repeat after one read" (A's only
  criterion-level lift, Creativity 5 v 4); `rank_fable.md` l.23: "The sharpest thesis sentence"; `rank_opus.md` l.16:
  "claims a full match that the same text later admits the ladder does not have". A's P8: "and the ladder falls short".
- **The readers never saw the pitch.** Packet per `posts/r1_jun.md` rule 2: case, WHARTON_WORD 1-4, coded texts.
  The pitch (`keel/ips_rewrite/drafts/D33/pitch.txt`, line 1): "so we don't invest for them. We buy them." Wharton, case
  lines 161-162: "Evaluators will consider the three deliverables together."
- **A's close is guessable, not clean.** `scores_jun.md` l.54 (Felix): "the two quotes ... name no act, so the act is the
  reader's own reading". Five strangers on V53's close today: two RIGHT, three flagged inference (RESULTS.md).

## 3. Open edges I'm not fixing tonight
- If the actuary is right that "We buy them" overclaims against P8, the pitch carries the same claim. That's the
  rewrite thread's call, not this room's; flagged for round 3.
- D's reserve line names the set-aside but not what it's held in. The case asks for the reserve's "initial asset
  composition" (`Laura_Gao_2026_Client_Profile.txt` l.95-96). A says nothing on it either; no reader asked.
