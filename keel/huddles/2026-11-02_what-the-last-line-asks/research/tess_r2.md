# Tess, round 2 research note (H-019, Mon 2 Nov 2026)
> FICTION (the speaker is simulated; the sources and counts are real). (Keel is a simulated team, AI-written.)

1. **What:** strict counts of D and its neighbours, built from `arms/A_V53.txt` by exact string replacement (each old
   string asserted to occur once). **Where:** `keel/office/tools/textcheck.py` on copies in
   `/tmp/claude-0/-home-user-caplet-investment/03dc3032-2d9e-57f6-91b4-70cc152ed434/scratchpad/r2/tess/` (`make.py`;
   nothing in the repo but this note and the post). Run 2 Nov 2026.
   **Numbers (split on hyphens / by spaces):**

   | Text | Strict | Spaces |
   |---|---|---|
   | A (V53) | 497 | 496 |
   | A + V50's sentence in P2, minus "We buy them" pair, "one rung" | 500 | 499 |
   | ... and minus the "so her flexibility ..." clause | 492 | 491 |
   | **D (Tess): ... and "the ladder and the money set aside become"** | **497** | 496 |
   | D with Kai's "the ladder and its cushion become" | 495 | 494 |
   | D with "the ladder and the money set aside for its gap become" | 500 | 499 |
   | D (money set aside) keeping the clause | 505 | 504 |

   sha256 (first 16): D `72d7069d5b47fee5`; cushion variant `cdaa15b71dac01e8`; "for its gap" variant `b247d97dc3ba40f1`.
   **Means:** with the four protected lines untouched, the payers are "We buy them" (9) and the clause (8) = 17;
   V50 takes 12, so the reserve line gets 5 words at most.
2. **What:** D against C. **Where:** `diff` of sentence splits, 2 Nov 2026. **Means:** D = C with "Whatever the stocks
   can't cover lowers the whole range." restored, the "so her flexibility ..." clause cut, and P9's "everything set aside
   for it" replaced by "the money set aside". P2 is identical to C's.
3. **What:** the pitch carries "We buy them". **Where:** `keel/ips_rewrite/drafts/D33/pitch.txt` (read 2 Nov 2026).
   **Words:** "Laura's ten $50,000 cheques are a promise, so we don't invest for them. We buy them." **Means:** closes my
   round-1 "not checked" item; the blind packet (case, Wharton s1-4, coded texts) did not include the pitch.
4. **What:** what "cushion" is in the design. **Where:** `keel/ips_rewrite/drafts/D33/README.md`, P8 row (read 2 Nov
   2026). **Words:** "Genius Lab L-16: V52's words dropped the design's safety margin ... 'Cushion' not 'margin'".
   **Means:** the cushion is the margin added on top of the priced gap, so "the ladder and its cushion" leaves out the
   gap money itself.
5. **What:** who leaned on which line. **Where:** `blind/rank_haiku.md`, `rank_opus.md`, `rank_fable.md`,
   `answers.md` (read 2 Nov 2026). **Means:** "We buy them": all three singled it out (skimmer's only Creativity 5;
   the actuary also called it an overclaim). The clause: quoted once, by the professor, as where C "stops" ("never says
   what happens if the stocks she keeps cannot cover the gap"). "Whatever the stocks can't cover...": the reason the
   skimmer and the actuary put C last. Opus and Fable both used "cushion" for the whole set-aside in their B say-backs.
6. **Not checked:** whether a skimmer can say back "the money set aside" with content behind it. That is what the
   Tuesday read is for; under tonight's key, quoting it with nothing behind it scores WRONG, as B and C did.
