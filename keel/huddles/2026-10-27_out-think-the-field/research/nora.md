# Nora's checks before round 3 (27 Oct 2026, night; MODEL, 22 Oct curve)

AI-generated (Claude Code). Keel is fiction; the checks are real.

1. **Kai's top-tail question (K4 rerun with p95; Jun's annual rival model, 100,000 paths, same seeds).**
   | Rival plan | cushion | misses a payment | 2033 contribution p5 / p50 / p95 |
   |---|---|---|---|
   | 60/40 | 10% | 18.3% | $0 / $203k / $522k |
   | 60/40 | 25% | 6.4% | $0 / $142k / $461k |
   | Glide 70->30 | 25% | 1.8% | $0 / $137k / $424k |
   | Three buckets | 25% | 1.9% | $0 / $133k / $390k |
   | Barbell 90/10 | 10% | 1.7% | $91k / $152k / $216k |
   | Bond fund | 15% | 0.5% | $66k / $119k / $169k |
   | **V25 total surplus (ips_numbers.py, Jun's note)** | - | ~0 after the 2033 re-match | **$144k / $193k / $253k** |
   Reading: matched on misses, certainty costs nothing at the median and wins the bottom tail outright ($144k against
   $0). What it gives up is the best years: about $170k at the 95th percentile against the glide plan. Caveat: V25 is
   not in the annual model yet, so these sit across two models.
2. **"Treasury bills" in V25 (line 13).** `competition/COMPETITION.md` (Week-2 email, 6 Oct): "STRIPS, single
   zero-coupon Treasuries and direct T-bills are out." V25's 2033 set-aside must name a permitted holding (a short
   Treasury bond or Treasury ETF on WInS). Rule risk confirmed.
3. **"A small gap" (V25 line 13).** K_overnight_results.json: the post-2033 coupon shortfall is larger than what Laura
   kept in 7.67% of paths; the median uncovered amount when it happens is $3,154 (p99 of the whole shortfall $7,146).
   Lab L-10 already has the fix: hold $10,000 back for the payments before the gift (payment short 6.8% -> about 0.01%),
   on trial Thu 29 Oct. Amara's "never the bottom" order collides with it: L-10's hold-back comes out of the gift.
4. **Human capital (Tess, Felix).** Case lines 44-45 name the 2028 sources ("publishing advances, speaking engagements,
   licensing, and other entrepreneurial ventures"). Nothing in the case links them to markets. "Can shrink" is safe;
   "moves with stocks" is our inference.
5. **Longin and Solnik (2001)** is stocks against stocks across countries (Felix). It backs "diversification thins in
   a crash", not a stock-yield or income-yield link.
6. **Book 7 asks the composition question twice** (Felix: lines 21 and 47-51 of the updated instructions).
