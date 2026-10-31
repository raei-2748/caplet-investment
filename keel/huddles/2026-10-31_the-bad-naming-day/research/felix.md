# Felix, round 1: what I checked (MODEL, curve 22 Oct 2026, J.P. Morgan 7.5%)

**Re-ran LR-08 functions, house world, N=20,000, seed 1** (nothing written to LR-08_results.json; scratch script in /tmp).
- XR median bottom $145k; A09 at f=0.74 median bottom $145k; `calibrate()` on my sample gave f=0.7395. Holds.
- Worst 5% of Jan 2028-Jan 2031 stock returns: cutoff -23.1% (the JSON only stores the worst-tenth cutoff, -14.5%). XR median bottom $145k, A09 $90k, A09 median gift $106.9k vs the JSON's $106.7k. Holds.
- Bottom under $100k: A09 6.3%, JSON 6.16%. Holds (sampling).
- `np.allclose(xr["R"], a09["R"])` is True: same reserve, same ladder, same cushion code. A09 differs only in 2028-31 (80/20 VT/IEF) and in locking at naming day.

**Sensitivity to f (house):** the slice bottom for A09 runs $80k (f=0.65), $90k (0.74), $100k (0.80), $110k (0.90), $125k (1.0). It never reaches XR's $145k, so the direction survives any f. But "even locking its whole pot, $120k" should read $125k when run directly (90/0.74 is only a proxy). Note f=1.0 has a median bottom of $195k, a different promise.

**Calibration is a choice.** Matching the median makes A09's mean bottom higher ($146.8k vs XR $139.7k). Matching p5 instead would push f near 0.95 and change the price. The brief should say "matched on the median", not "the same promise".

**History:** f was set in the house world and held, so history's A09 median bottom is $150k, not $145k. Recalibrated to $145k (f=0.70) the price in history is still about $16.1k (unmatched $15.9k). Calibration slack does not explain the high end of the $9-16k price.

**History slice:** 82 of 1,636 paths are in the worst 5%, in about 8 separate episodes (gaps over 12 months). Overlapping start months are not independent worlds.

**Price (median gift + kept, A09 minus XR):** house $9.4k, storms $12.8k, bootstrap $13.0k, history $15.9k. Matches the brief's $9-16k.

## What it means
- Fair build: yes. Fair slice: a stress test, not a likelihood. Call it that, and prefer the unconditional "under $100k" frequency (house 1 in 16; four worlds 1 in 30 to 1 in 13).
- Judge-facing: the under-$100k comparison only, with "our model" and 50,000 worlds. Final Report: slice, correlation, p_top_reached (tops defined differently, R vs locked face), price range, and the against-us cheque-miss rate (0.19% vs 0.004%) and engine caveat (13 / 666 gifts below the named bottom predates the 2031 mark).

## Round 2 (31 Oct 2026; MODEL, house world, gens.lognormal(20000) default seed, LR-08 functions imported; LR-08_results.json untouched; scratch in /tmp)
**Cheque misses, XR (lock, cush $7,500) vs A09 (f = 0.74):**
- Any shortfall: XR 0.415% (83 paths), A09 0.025% (5). Over $1k: XR 0.155%, A09 0.005% (the brief's 0.19% / 0.004% are the over-$1k metric at N = 50,000; sampling).
- Size when XR misses (total over all ten cheques): median $680, largest $5,647; 63% under $1k, 90% under $2.5k. A09's largest $3,133.
- Cause: none from an unfilled 2027 gap (0 paths); all from the post-2033 coupon gap beyond the 2033 projection, in paths where Laura kept $0 in 2033 (median kept in misses $0).
- Bigger cushion: $15k and $25k both give XR 0.395%; it can't draw on money that isn't there. Median gift + kept falls $182.3k -> $174.8k -> $164.8k.
- Holdback (engine `trap`, gift held back and released later): $3k -> XR 0.030%; $6k -> 0 misses. Median 2033 gift $165.8k -> $165.4k, median eventual gift unchanged. Cost: 2033 gift below the named bottom 1,168 paths (5.8%) vs 243 (1.2%); after release 255. Engine predates the 2031 mark, so these below-bottom counts are not the design's.
- For V45: the leak V45 names ("coupons paid early earn less if yields fall") is what misses; V45 prices it in 2031, the engine in 2033, so the post-pricing residual exists in V45's design too.

**Amara's offer through round-1 rule:** $145k median (matched by construction; say so) passes; $90k worst-5% is a chosen slice, Final Report only; $9-16k price moves into the IPS (changed my round-1 call, after Kai). Case :110-112 is the only on-page line linking co-sponsor willingness to the size of her contribution; it is not evidence about the bottom number specifically.
