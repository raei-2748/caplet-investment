# Jun's audit variations (27 Oct 2026, MODEL, 22 Oct curve; scratch copies, repo script untouched)
Scratch: /tmp/claude-0/-home-user-caplet-investment/ac69066b-a544-54f6-94f9-377e44aad104/scratchpad/jun_K.py, jun_K4.py, jun_K4b.py. Same seeds and settings as K_overnight.py (200,000 paths V25; 100,000 rivals).

**K1 re-run, ladder and floor at market value (flat 4.6%), not par.** Median stock share 2028-2032: 6.5, 6.6, 6.7, 6.9, 7.1% (K1: 4.6-5.9%). 2033: 6.2%; 2037 12.6%; 2040 29.2%; 2041 46.3% (K1: 45.2%). So par understates early years by about a third; the late rise is unchanged.
- 2042 = 1.0 because the denominator is zero after the last cheque (K1's own line does `Ky/max(Ky+0,1)`). Not meaningful.
- Laura's kept stocks: p50 $24.1k in 2033 to $44.2k in 2042 (1.8x). In 7.0% of paths she keeps $0. The 2033 p10-p90 share band is 1-13%.
- The series changes definition at 2033 (before: all VT plus the floor; after: only Laura's kept half, gift paid out).

**V25 like for like.** Total surplus above the cheques in 2033 (floor + all VT + 2027 leftover - coupon gap): p5/p50/p95 $144k/$193k/$253k. Gift + kept p50 $189k. K4's table compared the gift alone ($166k) with the rivals' whole surplus.
**K2.** Coupon gap S33 median $0 (53% of paths zero); 36% of paths over $5k; 47% over $1k. The 2027 ladder gap is over $5k in 34% of paths, p95 $24k.

**K4 with the cushion varied** (all else as K4; derisk = reserve goes 100% to the duration-6 fund after 2033):
Cushion 10% (as posted): 60/40 18.3% miss, $203k; glide 8.6%, $198k; buckets 11.4%, $194k; barbell 1.7%, $152k; bond fund 4.1%, $139k.
Cushion 25%, same post mix: 60/40 6.4%, $142k; glide 1.8%, $137k; buckets 1.9%, $133k; barbell 0%, $91k; bond fund 0%, $78k.
Smallest cushion giving a miss rate at or under 2% (same post mix): glide 25% ($137k); buckets 25% ($133k); barbell 10% ($152k, 1.7%); bond fund 15% ($119k, 0.5%); 60/40 never (floor about 2.9% at any cushion: assets fall below the payments' value before 2033).
Derisking the reserve helps 60/40 at 10% cushion (18.3% to 6.9%) but not below about 3%.
Duration 4.5 and start yield 4.6% (a fund closer to the curve): bond fund miss 0.1% at 10%, contribution $124k.
**Caveat:** V25 itself is not in this model. Its miss rate and gift come from ips_numbers.py; the comparison is across two models until V25 is built in the annual one (Jun to do).

## Round 2 (27 Oct night): does fat-tailed stock/yield dependence move K2's "0.0% gap left after the 2028 deposit"?
Scratch: /tmp/claude-0/-home-user-caplet-investment/ac69066b-a544-54f6-94f9-377e44aad104/scratchpad/jun_k2tail.py (MODEL, 22 Oct curve, ladder anchored to K_overnight's -$224 headroom).
- Structure (ips_numbers.py lines 118-123, 182; K_overnight.py line 60): `gap27 = max(ladder cost on 1 Jan 2027 - 300k, 0)` depends only on the parallel rate shift from 22 Oct to 1 Jan 2027 (0.194 yr, sd 0.44pp). Stocks enter only from 2028 (`z` for 2028-32); DEPOSIT28 is a constant $150k. R05_joint's rho links 2028-32 stock shocks to 2028-32 yield changes only. So no stock/yield dependence, Gaussian or fat, can change the 0.0%. Only (a) a fatter rate tail over ten weeks or (b) a smaller/correlated deposit can.
- Rally by 1 Jan 2027 needed for the rung gap to exceed the deposit: $150k: 402bp; $100k: 287bp; $75k: 223bp; $50k: 155bp; $25k: 80bp. Gaussian P (sd 0.44pp): 0, 4e-11, 2e-7, 2e-4, 3.4%. Student-t(3), same sd (illustration only): 0.7%, 1.7%, 3.1%, 6.8%, 18.5%.
- History, FRED DGS10 daily 1962-2026 (repo copy keel/library/insight_v1/scripts/data/D3/fred_DGS10.csv), 50-trading-day change in the 10y as a stand-in for a parallel shift: worst fall 369bp from 26 Feb 1980 (from ~13%); 2007-09 worst 192bp from 14 Oct 2008; 2020 worst 116bp from 21 Jan 2020. Falls >= 223bp: only 1980, 1981, 1982; >= 155bp: also 1985, 1986, 2008. 0.57% of windows fell >= 200bp.
- Gap at those rallies (MODEL): 116bp -> $36.7k; 192bp -> $63.4k; 223bp -> $74.9k; 369bp -> $135.1k.
- Caveats: the model fills the gap from the 2028 deposit at its 1 Jan 2027 dollar size (2027 rate moves on the unbought rungs ignored, second order for a small gap); 1980-82 falls came from 13-15% yields, so they are proportionally smaller than the same bp from 4.6%.
- The fat-tail question that does bite: the 2033 coupon gap vs Laura's half (7.67%), where stocks and yields meet. Settle with R05_joint.py rerun with Student-t (or 2007-09 replayed) shocks. Not run tonight.
