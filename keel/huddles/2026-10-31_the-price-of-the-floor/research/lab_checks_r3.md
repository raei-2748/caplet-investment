# The Lab's three checks for round 3 (Sat 31 Oct 2026)

AI-generated (Claude Code). MODEL: curve 22 Oct 2026, 200,000 paths, seed 20261016, same paths for both plans; A09 at
k = 0.8. Script `../../../rooms/lab/L-14_price_of_the_floor/run.py`, results `results.json` beside it.

**1. Kai's check: at what world-stock return are the average gifts equal?** (compound a year, before the 0.06% fee;
same shocks, only the drift moves)
| World-stock return | XR mean gift | A09 mean gift | XR median | A09 median | A09 bottom under $100k |
|---|---|---|---|---|---|
| 3.0% | $157.2k | $156.8k | $160k | $153k | 10.8% |
| 4.0% | $157.8k | $160.7k | $160k | $155k | 9.3% |
| 5.0% | $158.4k | $164.6k | $160k | $160k | 8.0% |
| 6.0% | $159.0k | $168.6k | $165k | $165k | 6.8% |
| 7.5% (J.P. Morgan 2027) | $160.0k | $174.7k | $165k | $170k | 5.3% |
(S0. S1 the same to within $0.5k; S2 equal at 3.0%; S6 A09 ahead even at 3.0%, by $3.3k.) **Break-even: about 3% a
year.** Below it XR's average gift is bigger too; at 3% compound, stocks' average yearly return is about the Treasury
yield, which is the premium test again. Medians cross between 5% and 6%.

**2. Felix's check: do A09's bottoms under $100k come from stock losses?** Of A09's 2031 bottoms under $100,000:
**93% (S0) / 94% (S1)** are paths where world stocks lost money over 2028-30 (23% of all paths do); 75% / 73% sit in the
worst tenth of those three years; their median 2028-30 stock return is **-25% / -24%**. In S6 (yields -2pt) 82%; in S2
(half a deposit) the bottom is under $100k almost everywhere for both plans, so the test says nothing there.

**3. Jun's check: reconcile the premium test with the gift gap.** With halves, cap and the 2031 sale (S0): mean gift
gap $14.7k; mean gift + Laura's own 2042 money gap $10.1k; the gift money alone (premium test) $11.3k. The gift gap is
the biggest because XR's cap binds more often (top reached 98%), and the money above XR's top stays with Laura. The full
model at ~3% stocks (table above) gives a mean gift gap of -$0.4k, so the premium test's answer holds with every rule in.
