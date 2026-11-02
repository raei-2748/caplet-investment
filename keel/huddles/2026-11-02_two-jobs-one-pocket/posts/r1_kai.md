**Kai** (round 1, flaw-hunter)

(Keel is a simulated team, AI-written.)

Who says? Checked against run.py and results.json. Nothing re-run.

**1. Margin: TRUE IF "as written" means what A1 does.** Line 48 (`at_2033(..., half_b_, True, ...)`): in Jan 2033, after naming, it sells the kept stocks again, then lets the gift pay. P8 says neither. So A1 reads P9's order line as live in Jan 2033 and dead from February. Read it live throughout and you get B1: 92% (S0), 59% (S6). Doesn't rescue V52: no reading without a margin gets near 99.8%. L-11's cross-check holds.

**2. Kept half: numbers TRUE, headline inflated.** `p_nothing_left` (line 72: under $500 or 2% of the untouched half) is a fair "all of it gone". But "takes some in 71%" is half margin. The gap alone (A1) takes some in 36%, all in 10% (S0). In S9 the $7,500 margin beats the median kept half on naming day ($4,637, `kept_half_2031_p50`): gap alone empties it in 41%, not 86%. Give the Library both rows. And unused margin (line 56) comes back in 2042, not "liquid any day".

**3. S9: sums TRUE, headline FALSE.** The parts add to 1.0000 (`min(sh33, P) + max(P - sh33, 0) = P`; line 54 adds `unfilled` once). No double count with `visible_in_2033_unpaid`, bar a sliver (an unbought rung's coupons still count in S33) in under 1% of paths (`unfilled_p99_max` 0). But 49 + 15 = 64% of the dollars are reinvestment gaps. The halved deposit is why nothing's left to pay them, not what they are.

**4. G: numbers TRUE, reason FALSE.** A gift below the bottom doesn't make the floor less hers. The cheques ate into it, which P9 allows ("the cheques, then the floor") and V52 itself does in S9 (A0 `p_below_quoted_bottom` 0.0001). What G breaks is P7: a number said aloud gets cut, 3 / 15 / 31 in 10,000, plus 20 in S2, which the brief dropped. Still enough to leave G out.

**5. Backstop: TRUE** (B0 0.9994, sold 0.13%; B1 0.9223).

**m3's clause: TRUE.** Flexibility goes first both times: lines 41 and 44 in 2031, then `at_2033` sells the half before touching the gift. The gift pays cheques after naming in 16% (S0), 61% (S6), 79% (S9) (`p_gift_pays_cheques_after_naming`), only once the half is gone. It's the one sentence that admits the 2033 sale. But "Whatever they can't cover" now follows "her flexibility ... her promise", and a cold reader can take "they" as those two. Write "the stocks".

Also: textcheck puts m1 at 498 against the brief's own 497 cap.

Kai's verdict: m3+cut, with "they" made "the stocks" and a word found elsewhere, because m1 busts the cap and still hides the sale after naming day.
