# The quoted floor can break, about 1 in 130 paths, by about $4k: IPS v4 names only two of the three steps
AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited.
(Keel is a simulated team, AI-written.) Simulated readers are tests, never quotes, and never Laura's words.
Work order: SD-LR-02 | Room: Laura's Room (Amara; case-analyst, cosponsor-reader roles, no subagents) | Date: Sun 25 Oct 2026, 15:10 AEDT

**Read:** IPS v4 recommended text (`/mnt/project-files/ips/IPS_edits_v4_2026-10-25.md`; repo `keel/rooms/night_2026-10-25/v4/`), the
Genius Lab's Extended Reserve line (L-08), the official case (`Laura_Gao_2026_Client_Profile.txt`). Builds on the night
visit to v3.1 (`keel/rooms/night_2026-10-25/lauras_room.md`); bad year A and B are not repeated.

## Answer
1. **Overpromise test (co-sponsor 2, SIMULATED, the careful finance reader).** He reads P5: "we price any gap the ladder
   will leave ... and set it aside from the half Laura keeps, then from the contribution above the floor." He asks the
   next question: *and if both run out?* The IPS says nothing. The case puts the payments first (":91-92, high degree of
   certainty"), so the floor gives, and that is the number Laura quoted (":114-116, promises more than she can ultimately
   contribute"). Laura's Room ran it (MODEL, 22 Oct curve, 2027 LTCMA 7.5%, unchanged model):
   | Buffer from the 2028 deposit | Gap reaches the floor holding | Gift lands below the quoted 2031 bottom | Size when it does (median / p95) |
   |---|---|---|---|
   | none (v4 as written) | 1.7% | **0.75% (about 1 in 130)** | $4,000 / $13,700 |
   | $5,000 | 0.8% | 0.31% | $3,400 / $11,200 |
   | $10,000 (Keel's D1 lean) | 0.3% | **0.11% (about 1 in 900)** | $2,500 / $8,900 |
   It reproduces the model's own "gift inside the range 99.25%" exactly. Rounding the floor down absorbs about half the
   cases. The breaks come when yields fall for good *and* the fund is small (median gap $26k, median fund $15k vs $43k
   in all paths). The model draws stocks and rates independently, so this is a floor on the joint risk, not a ceiling.
2. **So does the range overpromise?** Not in size: 99%+ of the time the gift lands inside it, and the IPS states the
   cap. But v4 has a quiet contradiction a sharp judge could find: P5 refuses stocks because they "could break a number
   Laura has quoted", while a rate fall can break the same number by the route P5 leaves unfinished.
3. **"The rest, the interest that ETF will earn, buys a global index fund"** (P3). Laura, a statistics graduate (:16),
   reads it as present value and nods. Co-sponsor 2 stops: you can't buy a fund today with interest earned by 2032. Fix,
   exact and no weaker: **"The rest, equal to the interest that ETF will earn, buys..."** (+2 words).
4. **Extended Reserve (L-08), if Package B wins.** Co-sponsor 1 (arts board, SIMULATED) likes "reserve": it tells him the
   running costs are safe, the case's own noun (:94-95). Laura checks "six years early": true for the January 2027
   purchase; the 2028 gap-fill is five. No change needed.

## What the team could change (Caplet decides; vote set B, Tue 27 Oct)
- **If D1's $10k buffer is adopted:** no IPS word change for this; the Final Report states the 1-in-900 figure, dated.
  The buffer now has a second reason the Courtroom has not heard: it protects the quoted bottom, not just the payments.
- **If D1 is rejected:** finish the order in P5, so the floor is honest: "...then from the contribution above the floor,
  and last from the floor itself." (+6 words; the cut has to come from elsewhere). Or quote the bottom one $5k step lower.
- Either way: the P3 "+equal to" fix (+2).

## Evidence
`keel/rooms/lauras_room/LR-02_floor_break.py` and `LR-02_results.json` (patches `keel/library/ips_numbers_2026-10/ips_numbers.py`
in memory, as P06 does; model file unchanged). Case lines from `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`.

## Limits
- MODEL: one rate model, one equity model, independent draws; the bottom here is that model's ($145k p50), not
  `range_2031.py`'s ($140k), the known basis split (SD-P02). Simulated readers are built from the case only.

## Takes for the morning brief
Amara: The one line I'd underline isn't in the IPS, it's the line after it – "and if that runs out?" One in 130 isn't
scary. Leaving the sentence unfinished is, because a co-sponsor finishes it for us, and he finishes it worse.
