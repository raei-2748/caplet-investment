# FICTION (the room) + real work. L-02: a small buffer as the third layer

Run Sat 24 Oct 2026 (Sydney) by Jun with Amara; Kai roasted first. MODEL. Criterion: Investment Strategy; Client Knowledge.

1. **Hypothesis.** A small, named Treasury buffer from the 2028 deposit closes most of the coupon-reinvestment gap
   (p95 $25,111) at a cost to the 2031 range a co-sponsor would accept.
2. **Kai's roast.** "So the safe plan needs a safety net for its safety net?"
3. **Test.** `keel/library/ips_numbers_2026-10/ips_numbers.py` unchanged except the curve (22 Oct) and five extra
   output lines: for buffers $0-25k, the share of paths where the payments need more than leftover + Laura's half +
   buffer, and where the buffer alone is short. Buffer held flat (no growth: conservative). Wrong if a buffer that
   brings the miss under 2% costs more than $20k of floor.
4. **Result (200,000 paths).**
   | Buffer | Payments need more than every backup | Buffer alone is short | Floor / quoted bottom falls by |
   |---|---|---|---|
   | $0 | 9.0% | 49% | $0 |
   | $10k | **2.9%** | 27% | $10k |
   | $15k | **1.3%** | 18% | $15k |
   | $20k | 0.5% | 10% | $20k |
   Alone, the buffer is weak; stacked as a third layer it does most of the work. It is also the only layer that does
   not shrink when yields fall (Library slip S-01, defence in depth): VT can fall in the same bad year.
5. **Verdict: ADOPT as an option** (D1 option c, $10-15k), not a decision. Kai's roast half-stands: on its own the net
   has holes; as a third net it is the cheapest certainty on the table. Caplet votes Tue 27 Oct.
