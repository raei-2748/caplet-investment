# Amara's working notes, round 1 (Keel is a simulated team, AI-written)

> AI-generated (Claude Code), Wed 4 Nov 2026. Notes behind `../posts/r1_amara.md`. MODEL figures are for this room and
> the Final Report only, never the IPS (Book 11). Any wording below is AI DRAFT (Claude, 4 Nov 2026).

## Evidence for the P7 finding ("the whole range comes down")
- A cold reader misread it: `../2026-11-04_checked-only-by-its-writers/posts/r3_stranger.md:18` ("I took it to mean her
  announced range gets lowered").
- The FINAL's own check flags it: `../../../ips_rewrite/drafts/FINAL/COMMANDMENTS_CHECK.md:46` ("can be read as cutting
  a range she already announced. It means the range she names is lower").
- What it means in the design: P7's sentence before begins "Before Laura names her range". In the Lab's lock runs the
  gift never pays a cheque after naming (L-17 table, column "Gift pays a cheque after naming": 0% for every arm except
  A0f, which isn't the FINAL's design; `../../../rooms/lab/L-17_interest_that_earns_nothing.md`).
- Offered fix (+0): "the whole range comes down." -> "she names a lower range." One loss: "whole" told the reader that
  the bottom can fall too. "A lower range" still lowers both ends.

## MODEL figures used (exhibit N, `../../../rooms/courtroom/C-06_w5_on_trial/EXHIBIT_N.md`; 22 Oct 2026 curve, 7.5% equities, 200,000 paths)
| What | Base | Yields 2 pts lower for good | Arm |
|---|---|---|---|
| Bottom of the range broken | never | never | every arm (line 50) |
| Gift reaches the top | 92.24% | 94.50% | KWN-w (the FINAL's lock words) |
| Kept shares all gone by naming day | 36.5% | 78.2% | KWN-w |
| Unused lock back to Laura, median | $21,326 | n/a | KWN (fee priced) |
Short of the top "always by small amounts, because the top adds the floor at its face" (line 52).

## Why it's a range (the honest answer)
At naming, both ends are in Treasuries (P6). What's left in the width is the floor fund's payout, which isn't
promised (iShares: "the Funds do not seek to return any predetermined amount", exhibit N's sources). The bottom is
rounded down against that, and the top counts the fund at its face. So the width isn't share risk. Market outcomes
move the range before 2031 (the shares grow or fall from 2028; falling rates raise the shortfall lock, P7), and after
she names it they barely move it. That answers :118-119 ("how favorable and unfavorable market outcomes could affect
the amount") in the right order: the markets move the number before she says it, not after. Final Report material,
with the confidence :117-118 asks for.

## Count test (scratch copies, `keel/office/tools/textcheck.py`, strict)
V57 493 -> +W1 "to help run" 494 -> +W2 sharpened "Part of what's left" 496 -> +L1 "before" 496 -> +P7 "she names a
lower range" 496. Cap 497. Non-ASCII 0. (The chair's W2, "Part of what is left", would be 497 with W1.)

## For the Final Report (from Laura's chair)
One line on where her flexibility goes in a bad-rate future: the money moved from her kept shares into Treasuries
isn't spent unless rates fall, and as each holding pays, what wasn't needed comes back to her, during 2033-2042, while
the project develops (:103). Pair it with the Lab's "same downturn" line (L-18).

## Not checked, open
- What happens to any headroom left from the first $300,000 after the ladder is bought. The case doesn't say, and I
  didn't trace it in the model. That's why the post says the gift is "close to" all she has outside the reserve.
- The case never says her 2028 income is cyclical. P4's "can dry up" is our reading of :44-45, not a case fact.
