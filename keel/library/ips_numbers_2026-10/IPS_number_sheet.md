# IPS number sheet (15 Oct 2026 curve)

AI-generated (Claude Code) for Team Caplet, 16 Oct 2026. These are MODEL numbers, not promises. Re-run
`python3 keel/library/ips_numbers_2026-10/ips_numbers.py` after any curve change; every figure below is in `results.json`.
The plan modelled is IPS Version 5 exactly (Root-and-Branch on WInS-listed holdings: IBTM-IBTR + five T-bonds, IBTM
floor, VT). Inputs and their sources are in `inputs.md`.

## 1. Headline numbers for the IPS

| What | Number | Note |
|---|---|---|
| Cost of the ten payments on 1 Jan 2027 | **about $294,000** (15 Oct curve) | It was $290-292k a week ago. Each 0.1 point fall in yields adds about $3,000 |
| Headroom under the $300k deposit | **about $5,500** (about 0.19 points of yield) | The ladder costs more than $300k on 1 Jan 2027 in about **1 case in 3** (35%) |
| Floor (facility minimum) | **$150,000 face, quoted as $145,000** | Rounded down for the IBTM fund's coupon drift (it pays at least 98.7% of face in 99 of 100 paths). If the ladder costs more than $300k, the 2028 deposit fills the gap first and the floor is lower by the same amount |
| Stock fund (VT) bought Jan 2028 | **about $32,000** (90% band $20k-$43k) | What is left of $150k after buying IBTM sized to repay the floor |
| **2031 range Laura announces** | **about $145,000 to $168,000** today | Top = floor + half of VT's 2031 value; 90% band for the top $145k-$184k |
| **Confidence the 2033 gift falls inside it** | **about 99%** (99.4% of 200,000 paths) | The top cannot be exceeded (cap). The gift falls below the bottom only when a coupon shortfall is larger than the 2027 leftover + Laura's half |
| Typical 2033 gift | **about $167,000** (90% band $142k-$183k) | At or within $1,000 of the top in about 3 cases in 4 |
| Below the middle of the range | about 1 in 50 | |

## 2. Good and bad markets (for the "how markets affect it" sentence)

- **Good market:** VT grows; the gift reaches the announced top and stops there. Everything above the cap stays
  with Laura as flexibility.
- **Bad stock market:** VT falls. The top was set in 2031, so a fall before 2031 lowers the announced range itself; a
  fall between 2031 and 2033 lowers the gift towards the floor, never below it on its own.
- **Falling interest rates (the real risk):** the coupons the ladder pays must be reinvested at lower yields. If yields
  fall and stay down, the ten holdings deliver:

| Yields after Jan 2027 | Ladder delivers (target $500,000) | Shortfall |
|---|---|---|
| unchanged | $500,000 | 0 |
| 1 point lower | $489,000 | $11,000 |
| 2 points lower | $479,000 | $21,000 |
| 3 points lower | $469,000 | $31,000 |
| down to near zero | $456,000 | $44,000 |

## 3. The weakness the IPS must disclose (coupon reinvestment)

- "Once bought, each payment depends mainly on the US government" is true for the $50,000 principal but **not for the
  coupons**: iBond ETFs and T-bonds pay income that must be reinvested at unknown future yields.
- In the model a shortfall above $1,000 happens in about half the paths (rates drift down as often as up); the median
  shortfall is 0, the 1-in-20 case about **$25,000**, the 1-in-100 case about $33,000. Replaying every US 10-year
  yield path since 1953 gives a similar 1-in-20 figure ($22,000); the worst start (June 1984, yields fell from ~13%)
  gives $39,000.
- The IPS's own order covers it: 2027 leftover, then Laura's half, then the gift above the floor. That chain covers
  the whole shortfall in about **93 of 100** paths. In about **6-7 of 100** paths a small part of a later payment
  (typically about $3,000, after 2033) is not covered by what Laura kept, so "cannot miss" is not literally true.
- **Team decision needed before 6 Nov** (pick one; each is a small change and none is a WInS trade):
  1. Keep the design and *state* the risk: "payments are secure in about 93-95 cases in 100 from the plan alone; the
     rest needs a few thousand dollars from Laura's kept half after 2033."
  2. Keep Laura's half in reserve until 2042 (not just 2033) as the named back-up for the payments.
  3. Hold back a dedicated buffer from the 2028 deposit (about $10-20k, which lowers the floor by the same amount).
     A $20k buffer covers a 2-point fall in yields.

## 4. Allocation (for "how the allocation changes")

| Date | Payment Treasuries | Floor Treasury (IBTM) | Leftover Treasury | World stocks (VT) |
|---|---|---|---|---|
| Jan 2027 | ~98% | 0 | ~2% | 0 |
| Jan 2028 (typical) | ~67% | ~25% | ~1% | ~7% |
| Jan 2033 | the floor matures and is given; the ladder becomes the operating reserve and shrinks by $50k a year; Laura's half of VT is hers |

Return assumptions to state in one line: Treasuries earn the yield at purchase (about 4.9-5.5% today) if held to the
end; world stocks about **7% a year** (J.P. Morgan 2026 long-term estimate for global stocks, 16.8% volatility).

## 5. Limits of these numbers

- Rates move in parallel and are independent of stocks. In the last year VT and the iBond ladder rose and fell together
  (correlation about +0.5), so a bad 2031 could combine weak stocks and low yields.
- iBond funds are modelled as bonds whose coupon equals their yield. This overstates their coupon risk slightly.
- No taxes, no commissions (each trade is $10-25), no fund closure risk (iShares: an iBond ETF "does not seek to
  return any predetermined amount").
- Older `archive/rab/` figures (top ~$175k, VT ~$41k) were on the 28 Sep curve and put the 2027 leftover into VT; Version 5
  keeps the leftover as the first buffer, and yields are lower, so the top is about $8k lower here.
