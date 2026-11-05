# R10 – Bible audit, final confirm (V1, Fri 6 Nov 2026, Sydney)

Draft: `R10_pitch.txt` (50), `R10_ips.txt` (496 by `wc`; the Writer reports 500 strict). Changes from R9: the pitch,
paragraph 3's "her first holding, a fund ending in late 2032", and paragraph 4's falling-shares line.

**GATE PASS – 0 ★ failures, no regressions.**

| check | result | evidence |
|---|---|---|
| R9 must-change (pitch verb + owner) | MET | "In 2028 she buys a minimum facility contribution and puts roughly its interest into world shares." There is a verb now, and "its" has one possible owner (the minimum facility contribution). B6 ★ and B7 ★ now pass for the pitch. |
| ¶3 "her first holding, a fund ending in late 2032" | PASS | Clearer than "the late-2032 fund that pays her first January": the reader is told it is the same fund that pays the 2033 payment (TNA note 2, "two jobs"). |
| ¶4 falling-shares line | PASS (true) / PARTIAL (shape) | "Falling shares alone, before 2031, lower only the top; rising shares lift it." It is true and scoped ("alone" points to the rate case, which the next paragraph covers). The semicolon mirror is back, though: the slogan shape R8 flagged and R9 had removed. It doesn't block. If the Writer touches anything else, R9's comma version read more naturally. |
| Regressions | none | Every other sentence is identical to R9 (`diff`). |
| Carried minors | not blocking | "they have taken on more risk to keep up" (with what?); liquidity is one word; the dividend sentence and the capital-protected note go to the Final Report bank. |

**Bible gate: PASS.** Nothing must change for R10 to become THE FINAL.
