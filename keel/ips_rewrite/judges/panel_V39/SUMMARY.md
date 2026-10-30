# Panel 6 (Fri 30 Oct 2026, late night): V39 against V37a and the new rival

AI-generated (Claude Code), not for submission. Same six judges, blind, new orders (seeds 6001-6006). Field: **V39**
(`../drafts/D19/`), **V37a** (`../drafts/D17/ips_V37a.txt`, panel 5's winner), **S01** (the CPPI rival that took three
#1s in panel 5), A09, CV5 and H24. Rivals now cut at "## SIMULATOR NOTES" (the panel-5 leak is fixed; checked).

| Judge | Ranking (best first) |
|---|---|
| J1 skimmer (Haiku) | V39 > A09 > V37a > H24 > CV5 > S01 |
| J2 growth hawk (Sonnet) | S01 > A09 > V37a > V39 > CV5 > H24 |
| J3 actuary (Opus) | V39 > V37a > S01 > CV5 > A09 > H24 |
| J4 teacher (Sonnet) | V37a > V39 > CV5 > S01 > A09 > H24 |
| J5 professor (Fable) | V37a > V39 > S01 > CV5 > H24 > A09 |
| J6 programme manager (Haiku) | S01 > V39 > V37a > CV5 > A09 > H24 |

**Agreement:** mean Kendall tau 0.34. **Mean rank:** V39 2.0, V37a 2.17, S01 3.0, A09 4.17, CV5 4.17, H24 5.5.
\#1 picks split two each: V39, V37a, S01.

**Verdict: V39 is the current best, by a hair and by truth.** It splits 3-3 with V37a head to head, but has the best
mean rank, and it fixes two things V37a gets wrong: V37a's "a cheque fails only if ... yields drop two points ... and
her deposit comes in under about $125,000" is false on the Archive's own grid (a $40,000 deposit with no yield fall
leaves a cheque short in 1.8% of model paths), and its "one time in four" for a 60/40 plan is one time in three in the
7.5% worlds (M7: 32-36%). J3 (the actuary), who put S01 first in panel 5, now puts V39 first: it names the ladder's leak
and sees that the 2028 deposit is weakest in the same years the ladder costs most, and it now states its assumption.

## Open for the next round (what judges still could not follow, or still want)
1. **"$125,000 of its $150,000"** (J6): say what it is measured against (the smallest deposit that still fills the
   gap after a two-point fall).
2. **"Only two things break a cheque" vs the 60/40 that "misses a cheque"** (J4): a reader can blur our plan's failure
   with the rival's. Make the 60/40 sentence's subject impossible to miss.
3. **The cost of safety in dollars** (J2, J5): what Laura gives up for the certainty. M7 (lognormal, 7.5%): a 60/40
   plan's median gift is about $159k against ours $166k, but it leaves her about $226k by 2042 against ours $30k. That
   gap is the real price, and it is large; it is a strategy question for the Lab's A09 run (Sat 31 Oct) before it is a
   sentence.
4. **Small growth share** (J2, J6 again). The capacity argument (para 6) is the answer; no judge said it was wrong.
