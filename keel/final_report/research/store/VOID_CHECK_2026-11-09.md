# Void-figure check of four tag pages against NUMBERS.md (Mon 9 Nov 2026)

Research notes, not report text. Checked against `keel/final_report/NUMBERS.md` (6 Nov curve, Caplet's FINAL design, Keel's margin), including its section 6, "Figures now void". Pages checked: `by_tag/REINVEST.md`, `COMPLETE2028.md`, `FLOOR.md` and `CEILING.md` (575 distinct rows; many rows sit under more than one of the four tags). Full rows were read in `insights.jsonl`.

## How rows were sorted

- **(a) consistent**: the row's figures agree with NUMBERS.md.
- **(b) void**: a figure is superseded by a NUMBERS.md figure. Marked in `ratings.csv` with status `adapt` and a note "VOID figure (NUMBERS.md 9 Nov): old is now new (section N)". F, R, S and C are left as they were, except five rows whose idea rests wholly on the void "top reached about three in four" odds (H1-024, H4-090, H5-011, H8-009, H9-087): their S is set to 1.
- **(c) not covered**: a figure NUMBERS.md does not hold. Left as it is and listed below with what the register could add.
- **No figure**: dates, names and wording only. Nothing done.
- One class per row. A row with any void figure counts as (b); otherwise a row with any uncovered figure that matters counts as (c).
- Nothing in the harvest or card files was edited. The store was rebuilt with `python3 -I build_store.py`: 1,432 ideas before and after; 166 rows now judged; rows needing reframing rose from 224 to 318.

## Counts

| Tag page | Rows | (a) consistent | (b) void | (c) not covered | No figure |
|---|---|---|---|---|---|
| REINVEST | 138 | 6 | 58 | 28 | 46 |
| COMPLETE2028 | 111 | 7 | 56 | 17 | 31 |
| FLOOR | 202 | 5 | 54 | 31 | 112 |
| CEILING | 267 | 14 | 59 | 58 | 136 |
| **Distinct rows, all four pages** | **575** | **28** | **166** | **115** | **266** |

Tag key in the tables below: RE = REINVEST, C28 = COMPLETE2028, FL = FLOOR, CE = CEILING.

## The void figures that recur most

1. **"Top reached about three times in four"** (and every 70-98% variant, with the newsvendor ratios built on it). After the 2031 move the stated range holds in every house path; what is uncertain is which range Laura can announce (top $110k-$170k house, $131k-$154k history). Sections 4 and 6.
2. **About $21,000 short if yields fall 2 points for good.** Now $23,509 for the ladder as written and $0 with Keel's margin. Sections 2 and 6.
3. **All ten paid in about 75-76% (or 96-99.9%) of futures.** Now 44% of history windows as written and 94% with Keel's margin. Sections 2 and 6.
4. **The range $145k-$170k, a bottom of $140k-$150k.** Now a stated range of about $110k-$135k central; floor payout $115,929, stated bottom $110,000. Sections 3, 4 and 6.
5. **The ladder fits under $300,000 (headroom $1k-$7.7k; "the first deposit buys all ten").** Now $302,287: $2,287 over even with no fall. Sections 1 and 6.
6. **"Shares are bought with the floor's expected interest" (a capital-protected note).** Now VT $33,515 against the floor's interest of about $23,900 ($92,010 growing to $115,929). If VT went to zero, the 2028 money left after completion ($125,525) would return $115,929. Sections 0 and 4.
7. **All-Treasury plan about $191,000.** Now $158,157 with Keel's margin and $185,987 without. Sections 4 and 6.
8. **"The first $50,000 of the 2028 deposit is payment money".** Now $2,400 at today's yields ($24,500 with margin); $70,400 after a 2-point fall ($92,000 with margin). Section 5.
9. **Caplet's bad-case bottom of $140,000 (under $100,000 about 1 time in 150).** The floor does not move with shares, so its central payout is $115,929 in any share market; but yields to 2028 move it, house 1-in-20 low $92k. Section 4.
10. **$289-$296 per basis point, 9.90 years, $30,600 per 1-point fall; 1.00x cover is enough.** Now $300, 9.94 years, $31,805; cover 1.07x with Keel's margin ($323,436 against $302,287). Sections 1, 2 and 6.

## Rows whose idea the register now backs

Five (b) rows proposed what is now Keel's call in section 2 (a margin bought from the 2028 deposit before the floor and VT): H2-035, H4-002, H4-087, H8-016, H8-085. Their old costs are void, but the idea matches the register. Two rows said the cash-flow-matched ladder costs more (H2-028, H8-078); on the 6 Nov curve it costs $258 less (section 2), though it still breaks the IPS's "buy 10 Treasuries" in January 2027.

## Points for NUMBERS.md itself

Possible errors:
1. **Section 6, first row: "$130k-$160k without" the margin.** By section 4's own rule (the top less 2.5%, rounded down to $5,000), the top without the margin, $163,147, gives $155,000. So the range without the margin is about $130k-$155k.
2. **Section 1, "Ladder duration 9.94 years / $300".** These are the ten payments' duration and price sensitivity, not those of the bonds and funds held. The held ladder's duration is much shorter (about 7.6-7.8 years on 23 Oct prices, H2-025) because coupons arrive years early. That gap is the reinvestment risk of section 2, and it is why TNA note 1's "duration-matching" is loose. Label it "the ten payments" and add the held ladder's duration.
3. **Build order.** The engine leaves the unbought $2,287 on the 2042 rung (`plan.py`: "the unbought tail is the longest rung"). Six store rows (H2-020, H3-012, H4-082, H4-093, H4-107, H5-031) buy the longest rungs first, so the 2033 rung waits and the 2028 deposit fills a five-year gap. The FINAL says neither. Section 5's "2042 payment about $4,900 short" holds only for the engine's order; with the longest bought first, the 2033 payment would be about $3,000 short. State the order.
4. **Two 5 Nov costs.** Section 1 gives $302,163 (`ladder_history.py`); section 6 gives $302,137 (`holdings_ladder.py`). Name the script beside each, or keep one.
5. **Like for like.** Section 6 replaces "75-76% of base futures" (a model share) with "44% of historical windows" (a history count). That is fine as a void, but say they measure different things. Also, `results_2026-11-06.json` reports `house_payments_full` = 1.0 for every design, even with no margin, so the house model does not test reinvestment. Section 7 should say that payment safety comes only from the history replay, so nobody quotes "every house path" for the payments.
6. **House model size.** The stamp does not give it (200,000 paths, seed 2033, in `plan.py`). Add it.
7. **IBTM yield.** Section 0 gives 4.86% dated 23 Oct, although the page was read 9 Nov; H9-072 has 4.66% on 5 Nov. The engine does not use it, but the date should match.

Additions the store asks for most:
- **Capital protection, stated plainly.** VT ($33,515) is about 1.4 times the floor's expected interest (about $23,900), so the 2028 money is not capital-protected. If VT went to zero, the money left after completion would return $115,929 of $125,525 with the margin, and $136,328 of $147,612 without it. Eleven rows say the opposite (H1-083, H2-065, H3-037, H5-069, H5-074, H5-075, H6-066, H7-027, H7-092, H8-059, H9-082).
- **A dated ladder-cost history on one engine,** from late September to 6 Nov ($301,544), in the method of `ladder_history.py`. The Articulation story needs it (H1-061, H2-093, H7-051, H8-002, H9-184).
- **The strongest rival priced on the FINAL design:** shares until 2031, with the floor bought only then. Ten rows rest on it (H2-061, H2-062, H4-061, H5-003, H7-093, H8-096, H8-117, H8-139, H9-052, H9-179). The register prices only the all-Treasury rival.
- **A low and a high VT growth case.** The 7.5% is the top of the dated range of house forecasts (H9-108); about 5.8% would be a low case (H2-088, H9-042, H9-109).
- **Inflation at 2.5% (J.P. Morgan),** with the real value of the 2042 payment and of the floor (H4-048, H9-112).
- **Per-rung figures:** each rung's reinvestment shortfall and coupon share, the zero rate for each payment year and the flat break-even yield (H2-030, H3-099, H8-080, H8-105, H9-064, H10-047).
- **What Keel's margin hands back** to Laura when rates do not fall (H2-040), and how much of any shortfall is visible by 2031 and 2033 (H8-086).
- **A one-line deletion test:** shares at zero leave all ten payments unchanged, true by construction (H1-070, H2-091, H8-123, H9-048).

## Every (b) row: old figure and new figure

| Id | Tags | Old figure | New figure (NUMBERS.md) | Section |
|---|---|---|---|---|
| H1-005 | CE | top reached about 3 in 4 (87-93% with the lock; ratio 2.7-3.3) | after the 2031 move the gift falls inside the stated range in every house path; stated range about $110k-$135k central | 4 and 6 |
| H1-007 | C28 | 5 Nov ladder $2,163 over $300k | $2,287 over at the 6 Nov close ($302,287 instruments) | 1 |
| H1-008 | C28 | payments fail only if yields fall >2pp before the build AND the deposit is below about $50k (0.02% at $50k) | after a 2-point fall the ladder alone needs $70,400 of the deposit ($92,000 with the margin); safe unless the deposit falls >98% at today's yields | 5 |
| H1-011 | RE | waterfall cuts payment misses 6.8% to 0.01%; 99.25% inside; >$1k short 1.1%; top reached 87% | as written any shortfall in 55.6% of history windows; 6.0% with Keel's margin; gift inside the stated range in every house path | 2 and 4 |
| H1-013 | RE C28 | kept half median $17k ($13k at correlation 0.5); gift below bottom 0.75-1.3% | kept half median $24k (house; central $23,986); gift inside the stated range in every house path; shares and yields drawn independently | 4 and 7 |
| H1-017 | RE | payments' duration 9.90 years (25 Sep curve) | 9.94 years | 1 |
| H1-022 | FL CE | inside the range about 99% | certain once the half moves (every house path inside the stated range) | 4 |
| H1-024 | CE | model's 73-77% chance of reaching the top | top reached about three in four is void: the top is fixed when half of VT moves; the announceable top is $110k-$170k (house) or $131k-$154k (history). S set to 1: the idea rests on the void odds | 4 and 6 |
| H1-026 | C28 FL | $145k floor; model puts it below $145k in 43.5% of futures | floor payout $115,929 central (house $92k-$140k); stated bottom $110,000 | 4 |
| H1-028 | CE | pledged share barely moves the odds of reaching the top; haircut moves over/under ratio 3.3 to 6.4 for $1.3k | odds of reaching the top are void: after the move the top is reached in every house path; announced top is less 2.5% rounded down | 3 4 and 6 |
| H1-043 | C28 | 5 Nov ladder $302,163 | $301,544 curve and $302,287 instruments (6 Nov) | 1 |
| H1-052 | C28 CE | headroom thin ($2k-$6k) | no headroom: the ten cost $302,287, $2,287 over | 1 and 6 |
| H1-053 | RE | about $21k short if yields fall 2 points for good | $23,509 as written; $0 with Keel's margin | 2 and 6 |
| H1-059 | RE C28 CE | about $21k short in about 6-7% of paths | $23,509 at a 2-point fall as written; history 1-in-20 $34,555; $0 and 6.0% of windows with Keel's margin | 2 and 6 |
| H1-074 | CE | equity weight 50/60/70% gives median $205k/$207k/$209k (old design) | floor + moved half + kept half central $162,721, house median $164k | 4 |
| H1-082 | C28 FL | $500,000 of payments cost about $294-298k | $302,287 (interest still pays about two-fifths: 39.5%) | 1 |
| H1-083 | FL CE | VT sized near the floor's expected interest (Merton about 21%) | VT $33,515 is 26.7% of what is left, against floor interest of about $23,900 ($92,010 to $115,929) | 0 and 4 |
| H1-084 | RE | payment more than $1k short about 1.1% (1.8% stressed) | any shortfall in 55.6% of history windows as written; 6.0% with Keel's margin | 2 |
| H2-012 | C28 | rates -2 for good and deposit halved: every payment paid in 99.96% (V57 lock); gift -$5,900 | after a 2-point fall the ladder needs $70,400 of the deposit ($92,000 with margin); -2 for good costs $23,509 as written, $0 with margin | 2 and 5 |
| H2-014 | C28 | first ~$50,000 of the 2028 deposit insures the payments; break points $85k/$125k; L-18 percentages | smallest deposit $2,400 ladder only or $24,500 with margin at today's yields; $35,000/$56,900 after a 1-point fall | 5 |
| H2-018 | RE | face $317,155, coupons $135,890, interest on interest $42,610, waiting $4,345; $19,945 still depends on yields | interest worth $93,900 by 2033; $54,595 short if interest earns nothing | 2 |
| H2-020 | C28 | 2027 ladder short in 46% of paths, always on the 2033 rung | short $2,287 at the 6 Nov close; the register leaves the gap on the 2042 rung (about $4,900 short if the deposit is missed) | 1 and 5 |
| H2-025 | RE | payments' duration 9.99 modified (10.24 Macaulay); instruments 7.61 (23 Oct prices); 70% in 2042 bond to match | payments' duration 9.94 years; instruments' duration not on the register | 1 |
| H2-028 | RE | dedicated ladder costs more than the headroom | no headroom (the ten cost $302,287); design B costs $258 less than A | 1 2 and 6 |
| H2-032 | RE | every payment paid in 96.01%/94.39% with a margin; 76% with no margin; kept shares used 28.1% | 44% of history windows paid in full as written; 94% with Keel's margin | 2 and 6 |
| H2-033 | RE | interest-only lock pays every payment in 97.02% (82.18% at -2); +$3,559 | 44% of history windows paid in full as written; 94% with margin; fund cash wait up to about 2% a rung | 2 3 and 6 |
| H2-034 | RE | gift below the bottom 4.9% to 0.03% for $160; 2.0% of payments short | gift inside the stated range in every house path; payments short in 6.0% of history windows with margin | 2 and 4 |
| H2-035 | RE C28 FL | 19% of the gap still to come: about $7.5k holding; costs minimum $10k; 2027 headroom -$224; >$1k short 5.9-7.4% | Keel's margin $21,149 (completion about $24,500 Jan 2028) costs about $20,000 off the bottom; ladder $2,287 over | 1 2 and 4 |
| H2-036 | RE | check before every payment 6.2% vs 5.9% short by >$1k; sells shares in 24% of paths | any shortfall in 55.6% of history windows as written; 6.0% with margin | 2 |
| H2-038 | RE | $7,500 capped cushion | Keel's margin $21,149 (1 Jan 2027 money) | 2 |
| H2-041 | RE | one look: payment short in 1 future in 25 (96.01%, median $1,341); two looks 99.87% | as written any shortfall in 55.6% of windows (median $1,592); 6.0% with Keel's margin | 2 |
| H2-042 | RE | kept half emptied 19.0% to 6.6%; top reached 97.9% to 99.3%; gift -$830 to -$1,700 | top reached is void: the top is fixed at the move; kept half central $23,986 | 4 and 6 |
| H2-043 | RE | median top falls $10k in the yields-down world; top reached 96-98% | top reached is void; top $138,735 central (house $110k-$170k) | 4 and 6 |
| H2-044 | RE FL | costs the top 1.4 points; half sold in 71% of paths (median $7,500); payments short 0.03-0.09% | payments short in 6.0% of history windows with margin; top reached void | 2 and 6 |
| H2-048 | FL CE | no 2028 deposit: 57% of paths short; bottom reached in 0 of 600,000 after naming | missed deposit: 2042 payment about $4,900 short at forward rates; gift inside the stated range in every house path | 4 and 5 |
| H2-055 | CE | top reached 86% with the move vs 73% without | top reached is void: after the move the gift falls inside the stated range in every house path | 4 and 6 |
| H2-061 | FL CE | rival $175k vs $160k mean gift; worst twentieth about $90k vs $140k named; owning early costs about $15k | stated bottom $110,000 central; top $138,735; the shares-until-2031 rival is not on the register | 4 |
| H2-063 | CE | ours broken under 1 in 60; payments short 6-8% (M7); 60/40 about $226k vs $30k, 1 in 3 broken | any payment shortfall in 55.6% of history windows as written; 6.0% with Keel's margin; the 60/40 rival is not on the register | 2 |
| H2-065 | FL CE | VT sized to the minimum fund's expected interest (about a fifteenth; 6.6% on 30 Oct) | VT $33,515 = 26.7% of what is left (7.4% of the $450k); the floor's interest is about $23,900 | 0 and 4 |
| H2-074 | C28 FL | top-up needed in 46.9% of futures (median $9,758) | completion $2,287 at the 6 Nov close (about $2,400 in Jan 2028); $24,475 with Keel's margin | 1 2 and 4 |
| H2-075 | FL | payments can take at most $9,768 after naming; a bottom $10k under the top | nothing changes either end after the move; stated range about $110k-$135k central (bottom = payout less 4.1% rounded down) | 3 and 4 |
| H2-076 | FL CE | newsvendor ratio about 5.7 base vs 0.8 yields-down (5-10 with the move); "three times worse" | top reached is void: the top is fixed at the 2031 move | 4 and 6 |
| H2-078 | CE | after naming only the payments' top-up (at most $9,768) can trim the gift | after the move nothing changes either end beyond the cash wait (at most 4.1% and 2.5%) already deducted | 3 and 4 |
| H2-079 | FL CE | range width about a tenth of the top (uncounted); SEC 20% test | central announced range about $110k-$135k: width about $25k, about 19% of the top | 4 |
| H2-086 | FL CE | "3 in 4" survives a 0.6pt haircut (71-75%) | top reached is void; announceable top $131k-$154k on US history | 4 and 6 |
| H2-089 | RE C28 | a 2008 replay leaves 14-18% short; correlation 0.8 grows each risk 1.7-3.8 times | worst history window starts Jul 2007: $45,266 short as written; $12,117 with margin; correlation not modelled | 2 and 7 |
| H2-090 | C28 | all ten paid in about 998 of 1,000 futures (99.82%); 98.49% with both shocks | all ten paid in 44% of history windows as written; 94% with Keel's margin | 2 and 6 |
| H2-102 | RE | $7,500 margin | Keel's margin $21,149 (1 Jan 2027 money) | 2 |
| H3-004 | RE | about $21k at a lasting 2-point fall | $23,509 as written; $0 with Keel's margin | 2 and 6 |
| H3-007 | FL | floor quoted rounded down at about $145k rather than $150k | stated bottom $110,000 (floor payout $115,929 less 4.1% rounded down) | 3 and 4 |
| H3-008 | C28 | $289 per basis point (25 Sep curve) | $300 per basis point | 1 |
| H3-023 | FL | about 99% inside the range | certain once moved: every house path inside the stated range | 4 |
| H3-037 | FL CE | VT sized to the floor fund's expected interest (capital protected) | VT $33,515 against floor interest of about $23,900 ($92,010 grows to $115,929): VT is about 1.4 times the interest | 0 and 4 |
| H3-091 | C28 | the payments reach low dependency on the $300k alone unless yields fall | the ten cost $302,287 at the 6 Nov close: $2,287 over even with no fall ($24,500 with margin) | 1 and 2 |
| H3-094 | C28 | $289 per basis point (25 Sep curve) | $300 per basis point | 1 |
| H3-104 | RE | gap about $21k vs half of a $32k VT sleeve | $23,509 as written ($0 with margin); VT on 1 Jan 2031 $41,561 | 2 and 4 |
| H3-105 | FL | top reached 70-73%; implied loss ratio 2.3-2.7 | top reached is void: the top is fixed at the 2031 move | 4 and 6 |
| H3-122 | C28 | ladder over $300k in 47% of paths (median gap $9.8k); coupon gap above $1k in 47% (p95 $22k) | ladder $2,287 over at the 6 Nov close; any shortfall in 55.6% of windows (1-in-20 $34,555) as written | 1 and 2 |
| H3-126 | RE C28 | reinvestment gap above $1k in 47%; ladder above $300k in 47% | any shortfall in 55.6% of windows as written (6.0% with margin); ladder $2,287 over now | 1 and 2 |
| H4-002 | RE C28 | coupon-gap risk 2% to 7.5% as the deposit falls $150k to $50k; fix costs about $9k of mean gift | Keel's margin $21,149 costs about $20,000 off the bottom; smallest deposits in section 5 | 2 4 and 5 |
| H4-003 | RE FL | 1.00x cover is enough; gift below the bottom 4.9% to 0.03% for $160 | cover 1.07x with Keel's margin ($323,436 vs $302,287); gift inside the stated range in every house path | 2 and 4 |
| H4-004 | FL CE | US-history top odds 84% (5:1); survivorship 4.73% | top reached is void; US history spread of the top $131k-$154k | 4 and 6 |
| H4-005 | CE | median $193k vs $119k-$152k for rivals; $170k cost at the 95th percentile | FINAL total median $164k with margin ($193k without) vs all-Treasury $158k ($186k) | 4 |
| H4-008 | FL CE | payments held at 1.0x cover | 1.07x with Keel's margin ($323,436 vs $302,287) | 2 |
| H4-011 | RE | a 2-point fall costs about $21k of the $500k; covered in 93 of 100 paths | $23,509 as written; $0 with Keel's margin | 2 and 6 |
| H4-014 | RE C28 | cover about 102% and 1.006x; headroom $1,139 (3.8bp) | cover below 1.00x at $300,000 ($302,287); 1.07x with Keel's margin | 1 2 and 6 |
| H4-019 | RE FL | $10k-$20k hold-back (number sheet decision 3) | Keel's margin $21,149 | 2 |
| H4-020 | C28 | ladder over $300k in 46-47% of paths (median $9.8k); a cheque breaks only if yields fall 2pt and the deposit falls >56%; survives a $40k deposit | ladder $2,287 over now; after a 2-point fall the deposit must stay above $70,400 (53%); $92,000 with margin | 1 and 5 |
| H4-028 | C28 | ladder over $300k in about 47% of paths | ladder $2,287 over at the 6 Nov close | 1 |
| H4-043 | CE | $25k short on a $150k lead leaves a $125k-$250k hole; over-promising 3x | no fixed $150,000 floor: stated bottom $110,000 central; top reached is void | 4 and 6 |
| H4-044 | FL CE | range $145k-$170k leads a campaign of $0.7m-$1.7m | range about $110k-$135k central: about $0.55m-$1.35m by the same rule | 4 and 6 |
| H4-081 | C28 | ladder over $300k in 47% of paths (median $9.8k); a cheque breaks only if yields fall 2pt and the deposit falls >56%; $40k with a coverage rule | ladder $2,287 over now; after a 2-point fall the deposit must stay above $70,400 (53%); $92,000 with margin | 1 and 5 |
| H4-083 | CE | top reached 87-93% under the lock; ratio 7-13x | top reached is void: the gift falls inside the stated range in every house path after the move | 4 and 6 |
| H4-087 | RE C28 FL | hold-back of the 2033 gap plus $7,500 cost about $9k of mean gift and was not adopted | Keel's margin $21,149 is now Keel's call; it costs about $20,000 off the bottom | 2 and 4 |
| H4-088 | RE | A14's fixed $3,700; P(gift below the bottom) 4.9% to 0.03% for $160 | gift inside the stated range in every house path | 4 |
| H4-090 | CE | find the VT share in the top that restores about 75% top reached | top reached is void: the top is fixed at the move and reached in every house path. S set to 1: the idea rests on the void odds | 4 and 6 |
| H4-185 | RE C28 | $10k hold-back | Keel's margin $21,149 | 2 |
| H5-001 | FL CE | "3 in 4" for the top falls to 73% (0.6pt haircut) and 68% (2pt); VT about $31k in Jan 2028; stocks beat a 5% bond 62% | top reached is void; VT bought $33,515 in Jan 2028 | 4 and 6 |
| H5-005 | C28 FL CE | headroom thin in Jan 2027 ($2k-$5k) | no headroom: the ten cost $302,287 | 1 and 6 |
| H5-007 | FL | on a "$150k floor" a 2% twist is about $3k | no fixed $150,000 floor: floor payout $115,929 central | 4 and 6 |
| H5-010 | CE | over-promising 3x; top about $16.4-17.2k above the floor (newsvendor $15.5k) | top is the floor plus the moved half: $22,806 above the floor central | 4 |
| H5-011 | CE | top reached about 3 times in 4 | top reached is void: the gift falls inside the stated range in every house path after the move. S set to 1: the idea rests on the void odds | 4 and 6 |
| H5-015 | RE | about $21k coupon gap | $23,509 as written at a 2-point fall; $0 with Keel's margin | 2 and 6 |
| H5-030 | C28 | coupon gap about $21k; ladder about $294k | $23,509 as written ($0 with margin); ladder $302,287 | 1 2 and 6 |
| H5-060 | RE FL | Keel's $7,500 cushion for 2033 | Keel's margin $21,149 bought in Jan 2028; bottom less 4.1% rounded down | 2 and 3 |
| H5-062 | C28 FL | at most about $50k of the 2028 deposit needed for the payments | $2,400 at today's yields; $70,400 after a 2-point fall ($92,000 with margin) | 5 |
| H5-069 | FL CE | about 21% of the deposit in VT; volatility about 16.5%; 7.5% source CONFLICTING | VT $33,515 = 22% of the deposit (26.7% of what is left); 16.78%; 7.5% is the 2027 LTCMA | 0 and 4 |
| H5-072 | RE | about $21k gap | $23,509 as written; $0 with Keel's margin | 2 and 6 |
| H5-074 | FL CE | VT sized to about the floor's expected interest | VT $33,515 against floor interest of about $23,900 | 0 and 4 |
| H5-075 | FL CE | roughly the floor's expected interest goes into shares; about 21% | VT $33,515 (26.7% of what is left) against floor interest of about $23,900 | 0 and 4 |
| H5-082 | RE CE | about $21k reinvestment gap | $23,509 as written at a 2-point fall; $0 with Keel's margin | 2 and 6 |
| H6-053 | C28 | flat 4% $333k and 5% $302k; 5 Nov curve $302,163 as the real price | $301,544 curve and $302,287 instruments (6 Nov); flat-yield figures not on the register | 1 and 6 |
| H6-066 | FL CE | roughly the Treasury fund's interest goes into shares; the deposit is never risked | VT $33,515 against floor interest of about $23,900; no fixed $150,000 floor | 0 4 and 6 |
| H7-014 | RE C28 | 65% chance the 2028 deposit tops up the ladder | certain at the 6 Nov close: $2,287 over ($24,475 with Keel's margin) | 1 and 4 |
| H7-026 | FL CE | share stake $32,133 = $150,000 minus $117,867 for the late-2032 fund | VT $33,515; floor money $92,010 paying $115,929 | 4 and 6 |
| H7-027 | FL CE | shares bought with roughly the fund's interest so the deposit comes back at about face value; hurdle about 5.1% | VT $33,515 vs floor interest of about $23,900; VT at zero leaves $115,929; 5-year 4.64%, 10-year 4.86% | 0 and 4 |
| H7-028 | CE | 2033: about $46k of shares on about $196k of surplus (0.23) | kept half $23,986 in shares on $162,721 (floor + moved half + kept half) | 4 |
| H7-044 | CE | VT stake $30,926: median $41.0k vs $39.6k in Treasuries; beats Treasuries 54-62% | VT $33,515 bought; $41,561 on 1 Jan 2031; FINAL ahead of all-Treasury in 63% of house paths | 4 |
| H7-045 | CE | chance shares trail the riskless plan 37.7-40.5%; adds about $19k to the median | FINAL ahead of all-Treasury in 63% of house paths (trails in 37%); medians $164k vs $158k | 4 |
| H7-046 | FL CE | all-Treasury about $191,223 (4 Nov); bottom about $145-150k; median $196k vs $191k; about $175k 1-in-20 | all-Treasury $158,157 with margin ($185,987 without); bottom $110,000; median $164k vs $158k; 1-in-20 $127k vs $126k | 4 and 6 |
| H7-047 | C28 | 5.09% break-even; 22 Oct $298,861; 4 Nov $300,608 (modified 9.61; $289-$299/bp) | $301,544 curve and $302,287 instruments (6 Nov); 9.94 years; $300 per basis point | 1 and 6 |
| H7-066 | CE | modelled top reached about 76% (p24) implies k about 3.2 | top reached is void: the announced top is reached in every house path after the move | 4 and 6 |
| H7-075 | CE | payments cost about 99.6% of $300,000 (22 Oct); cushion about $1,139 | the ten cost $302,287 (100.8%): no cushion, $2,287 short | 1 and 6 |
| H7-076 | CE | about 6.6% shares in Laura's plan (8.6% in the WInS book) | VT $33,515: 7.4% of the $450k (22% of the 2028 deposit) | 4 |
| H7-092 | CE | all Treasuries about $190-192k; Caplet invests only the interest | all-Treasury $158,157 with margin ($185,987 without); VT about 1.4 times the floor's interest | 4 and 6 |
| H7-093 | FL CE | Caplet's minimum under $100,000 about 1 time in 150 (rival 1 in 13) | floor payout house 1-in-20 low $92k: under $100k in more than 1 path in 20 | 4 |
| H7-097 | C28 | cushion in hand on 1 Jan 2027 about $1k | no cushion: the ten cost $302,287, $2,287 over | 1 and 6 |
| H7-100 | CE | TNA's 7.5% matches JPM's EAFE figure, not world equities (2026 edition 7.00%) | settled: J.P. Morgan 2027 LTCMA global equities 7.5%; 16.78% volatility | 0 |
| H7-109 | CE | money promised but not yet owned is zero at every date; funded ratio 100% by construction | $2,287 promised but unbought until Jan 2028 ($24,475 with margin): 99.2% funded at $300,000 | 1 and 4 |
| H8-003 | C28 | $300,000 first fitted on 10 Sep; on 22 Oct it fitted by $1,139 | no headroom at the 6 Nov close: the ten cost $302,287 | 1 and 6 |
| H8-005 | CE | V25 1-in-20 gift $138.8k to $138.0k in storms; 60/40 shortfall 6.1% to 7.6% | top 1-in-20 low $110k (house); storm regimes not on the register | 4 |
| H8-006 | C28 | each 0.1 point about $3,000; -0.57pt costs $16k; after a 2-point fall payment short in 84% at $50k ... 0% at $150k | 0.25 point costs $7,619; chance of a fall over 0.5 point about 8%; after a 2-point fall the ladder needs $70,400 ($92,000 with margin) | 1 and 5 |
| H8-008 | C28 | coupon-gap risk 2% with $150k and 7.5% with $50k; payments whole down to about $40k with L-10 | history: any shortfall 55.6% as written, 6.0% with margin; smallest deposits by yield fall in section 5 | 2 and 5 |
| H8-009 | CE | odds of reaching the top 75%/79%/84% (3:1, 3.6:1, 5:1) | top reached is void: the announced top is reached in every house path after the move. S set to 1: the idea rests on the void odds | 4 and 6 |
| H8-015 | C28 | about $289 per basis point (falling to $296 by 22 Oct); 22 Oct $298,841 predicted vs $298,861 | $300 per basis point; $302,287 | 1 |
| H8-016 | RE C28 | short beyond every backup 9.0% (no buffer), 2.9% ($10k), 1.3% ($15k), 0.5% ($20k) | any shortfall in 55.6% / 39.1% / 14.0% / 6.0% of history windows for margins of $0 / $7,169 / $14,221 / $21,149 | 2 |
| H8-017 | RE C28 | a lasting 1-point fall: $31,361 on purchase day vs $10,836 through reinvestment; 2 points $66,474 vs $20,960 | purchase day $31,805 (1 point) and $67,423 (2 points); reinvestment $12,172 and $23,509 (the shape holds: about three-quarters) | 1 and 2 |
| H8-024 | RE | iBond rungs mature one day early; waiting money costs about $0.8k; Feb-2037 320 days, May-2038 231, Nov bonds 47 | funds end on or about 15 Dec and their holdings' money waits 5.4-7.4 months in cash ($781-$1,043 a rung if it earns nothing) | 0 and 3 |
| H8-026 | C28 | 22 Oct: $298,861; headroom $1,139; $296/bp; 59.8 cents per dollar; 100bp fall $31.4k | $302,287 (60.5 cents per dollar); no headroom; $300/bp; 1-point fall $31,805 | 1 and 6 |
| H8-040 | C28 | yields must fall about 4-5 points for the ladder to cost both deposits | a 3.89-point fall before 1 Jan 2027 would use the whole 2028 deposit | 1 |
| H8-059 | FL CE | $117,936 at 4.915% grows to $150,000, freeing $32,064 (21.4%) for shares; floor pays 98.7% at the 1st percentile | floor money $92,010 pays $115,929; VT $33,515; payout falls at most 4.1% (all distributions earn nothing) | 3 and 4 |
| H8-060 | C28 CE | $32,064 to shares at 4.92% ($37,616 at +1, $26,208 at -1, $20,031 at -2) | VT $33,515 at the 6 Nov forwards; the yield sensitivity of the split is not on the register | 4 |
| H8-061 | C28 FL | each lost deposit dollar cuts the floor $1.00 (79 cents Treasury, 21 cents fund) | split 73.3% floor, 26.7% VT; floor payout falls about $0.92 per deposit dollar ($81k at $112,500) | 0 and 5 |
| H8-062 | CE | a share wipe-out costs at most the range's width: $19,700 (11.6% of a $170k top) | the moved half is $22,806 central on a $138,735 top | 4 |
| H8-063 | RE | any gap 0.50; mean $5,024; p90 $16,558; p95 $21,915 | any shortfall in 55.6% of history windows as written; median $1,592; 1-in-20 $34,555; worst $45,266 | 2 |
| H8-064 | CE | about 7.1% of the $450k ever sits in stocks (6.6-6.9%) | VT $33,515: 7.4% of the $450k | 4 |
| H8-078 | RE | dedicated ladder: -2pt $21,385 vs $9,616; p95 $25,112 vs $14,832; $1,486 more | design B: -2pt $10,725 vs $23,509; history 1-in-20 $15,925 vs $34,555; B costs $258 less | 2 |
| H8-079 | RE | $85,025 of coupons wait before 2033; short $11,062 / $21,385 / $31,030 at 1 / 2 / 3 points | interest worth $93,900 by 2033; short $12,172 / $23,509 / $34,083 | 2 |
| H8-081 | RE | a payment short in 6.8% of S0 futures (median $3,154) up to 98% in S5 | any shortfall in 55.6% of history windows as written (median $1,592); 6.0% with margin | 2 |
| H8-083 | RE FL | coverage test: payments short 0.01-0.02%; median gift $165,528; inside the range about 99% to 96% | 6.0% of history windows with margin; top $138,735 central; gift inside the stated range in every house path | 2 and 4 |
| H8-084 | C28 | deposit leaned on in 47% of paths (median $9,758); odds of a lower top 26% vs 25% | certain at the 6 Nov close: $2,287 ($24,475 with margin) | 1 and 4 |
| H8-085 | RE C28 | no rule 5.9% short; $7.5k bought in 2028: 0.00%, bottom $145k to $135k, gift $165.5k to $157.2k | Keel's margin $21,149: 6.0% of windows, worst $12,117; bottom $130,000 to $110,000 | 2 and 4 |
| H8-087 | RE | check before every payment: 6.2 / 7.7 / 36% short; sells stocks in 24% | any shortfall in 55.6% of history windows as written; 6.0% with margin | 2 |
| H8-090 | C28 | deposit sweep $0 57% ... $150k 0.03%; first $50k ($75k after a 1-point fall) is payment money | $2,400 ($24,500 with margin) at today's yields; $35,000 ($56,900) after a 1-point fall | 5 |
| H8-094 | RE | top reached 86.6/84.8/44.0/72.8% to 97.9%; widths 14.7-20.0% of the top | top reached is void; central announced range $110k-$135k (width about 19% of the top) | 4 and 6 |
| H8-096 | FL CE | A09 vs ours: worst 5% bottom $95k vs $140k; bottom under $100k 5.3% vs 0.9% | floor payout house 1-in-20 low $92k; stated bottom $110,000 central; A09 not on the register | 4 |
| H8-101 | RE | all ten paid: no margin 76.09 / 75.91 / 74.82%; margin $7.5k 99.82% | 44% of history windows as written; 94% with Keel's margin | 2 and 6 |
| H8-104 | RE | margin design 99.87%; zero-rate set-aside p50/p95/p99 $9,032/$23,773/$30,027 | sized so interest is never needed: $337,836; short if interest earns nothing $54,595 ($22,192 with margin) | 2 |
| H8-106 | RE | face $317,155 (63.4%), coupons $135,890, interest on interest $42,610, waiting $4,345; $19,945 still on naming day | interest worth $93,900 by 2033; $54,595 short if interest earns nothing | 2 |
| H8-107 | C28 | rates -2 for good, shares halve: $75k deposit 99.96%; $50k 96.00%; $25k 66.76%; none 18.46%; mean gift $139,045 | after a 2-point fall the ladder needs $70,400 ($92,000 with margin); missed deposit leaves 2042 about $4,900 short | 5 |
| H8-109 | FL | bottom $140k and top $165k; reach-top 76-77%; bottom $145k to $140k (15-22 Oct) | stated bottom $110,000; top $138,735 central; top reached void | 4 and 6 |
| H8-119 | RE | all ten paid: margin 99.87%; one look 96.01%; no cushion 74.70% | 44% of history windows as written; 94% with Keel's margin | 2 and 6 |
| H8-122 | C28 | joint shock 0.35-0.82% short; 2008 replay ladder $361,003, short in 14-18% | worst history window (Jul 2007): $45,266 as written, $12,117 with margin; a 2-point fall costs $369,710 | 1 and 2 |
| H8-125 | CE | 50/60/70% shares moved the median only $205-209k | FINAL total central $162,721 (house median $164k) | 4 |
| H8-126 | FL | floor pays at least 98.7% of face in 99 of 100 paths; 97% base / 82% rates-fall; $3,559 more | floor payout falls at most 4.1% (zero interest) or 2.6% (3-point fall); stated bottom deducts 4.1% | 3 |
| H8-127 | RE | 1 in 4 futures short without a margin, 1 in 550 with; about $670 of gift | 56% of history windows short as written; 6.0% with Keel's margin, which costs about $20,000 off the bottom | 2 4 and 6 |
| H8-129 | FL | printed $145,000 bottom above the 2031 number in 43.5% of futures | stated bottom $110,000 central; gift inside the stated range in every house path | 3 4 and 6 |
| H9-011 | C28 FL | the 2027 money buys all ten payments | the ten cost $302,287: $2,287 over the first deposit at the 6 Nov close | 1 |
| H9-036 | RE C28 | $306,663 as the no-reinvestment price (5 Nov) | sized so interest is never needed: $337,836; short if interest earns nothing $54,595 | 2 and 6 |
| H9-050 | CE | ours broke a promise in 0-1.6% of paths; rivals 22-36%; rivals leave $170k-$290k by 2042 vs our $31k-$56k | any payment shortfall in 6.0% of history windows with margin (55.6% as written); rivals not on the register | 2 |
| H9-052 | FL | strongest rival: worst twentieth bottom about $90,000 vs $140,000 for Caplet; cost $4k-$19k on four engines | Caplet's floor payout house 1-in-20 low is $92k; stated bottom $110,000 central | 4 |
| H9-053 | C28 | 2008 replay: ladder $361,003; a $75,000 deposit covers a $61,000 top-up with $14,000 left | a 2-point fall gives $369,710; completion needs $70,400 ($92,000 with margin) | 1 and 5 |
| H9-061 | C28 | Keel bootstrap $302,100 (6 Nov); the 2028 deposit carries about $2,000 | one engine: $301,544 curve, $302,287 instruments; completion $2,287 ($24,475 with margin) | 1 2 and 6 |
| H9-062 | RE C28 | $303,269 with instruments (5 Nov); $306,663 at zero; about $290 per bp; 0.25 fall about $7,300 | $302,287 on the 6 Nov curve; $300 per bp; 0.25 fall $7,619 | 1 and 6 |
| H9-065 | RE | 3-point fall about $31,000 short (median fall after 4.5-5.5% starts about 2.0 points) | $34,083 at 3 points as written; history replay worst $45,266 | 2 |
| H9-067 | RE | $11,000 / $21,000 / $31,000 short at 1 / 2 / 3 points | $12,172 / $23,509 / $34,083 as written; $0 with Keel's margin | 2 and 6 |
| H9-069 | RE | the dedicated ladder cut the bad case by about 40%; long-bond hedge $64-74k | design B halves it ($10,725 vs $23,509 at -2; $15,925 vs $34,555 1-in-20) at the same cost | 2 |
| H9-077 | C28 FL | each 0.1 point moves about $3,000 from floor to payments; a 0.5-point fall leaves a floor of about $136,000 | 0.5-point fall costs $15,455; floor payout $115,929 central with margin | 1 and 4 |
| H9-082 | FL CE | the share fund is roughly the floor's interest taken up front | VT $33,515 against floor interest of about $23,900 | 0 and 4 |
| H9-085 | FL | floor fund pays at least 98.7% of face in 99 paths of 100 | payout falls at most 4.1% (zero interest) or 2.6% (3-point fall); stated bottom deducts 4.1% | 3 |
| H9-086 | FL | in-range chance at least about 99% with the floor owned and half moved; top about 3 in 4 | certain unless the US defaults: every house path inside the stated range | 4 and 6 |
| H9-087 | CE | top reached about 3 in 4 (75/79/84%); at least halfway about 99 in 100 | top reached is void: after the move the gift falls inside the stated range in every house path. S set to 1: the idea rests on the void odds | 4 and 6 |
| H9-102 | FL CE | about two-thirds Treasuries for payments, a quarter floor, under a tenth shares (v12) | ladder plus completion $324,475 (72%), floor $92,010 (20%), VT $33,515 (7%) of the $450k | 1 and 4 |
| H9-137 | FL | draft paragraph: between [$145,000] and [$170,000] | stated range about $110,000 to $135,000 central ($130k-$160k without the margin) | 4 and 6 |
| H9-179 | FL | worst twentieth bottom about $90,000 (2031 version) vs $140,000; about $5,000 of median gift | floor payout house 1-in-20 low $92k; stated bottom $110,000 central | 4 |
| Q1-048 | C28 FL | a 1-point fall adds about $30,600 (25 Sep curve); safe unless the deposit falls about four-fifths | $31,805 (6 Nov); safe unless the deposit falls more than 77% after a 1-point fall | 1 5 and 6 |

## Every (c) row: the figure and what NUMBERS.md could add

### Plan figures the register could add or re-run on the FINAL design (43 rows)

| Id | Tags | Figure in the row | What NUMBERS.md could add |
|---|---|---|---|
| H1-003 | CE | $4,406 value of the cap given away by naming a capped range (old design, 22 Oct) | value of the upside given away on the FINAL design, if the covered-call point is used |
| H1-012 | RE | parking coupons in bills loses about $7.6k with no rate move (old design) | cost of holding coupons in bills instead of more of the same Treasury, on the FINAL design |
| H1-061 | C28 | headroom $7.7k (25 Sep) and $1,913 (16 Oct); ladder over $300k on most days of 2026; $302,163 on 5 Nov matches section 1 | a dated history of the ladder's cost (25 Sep to 6 Nov) from ladder_history.py |
| H1-070 | CE | deletion test: every share wiped in 600,000 paths, no payment worse off (old design) | a one-line check on the engine: shares at zero leave all ten payments unchanged (true by construction) |
| H2-027 | RE | Redington immunisation: $64-74k of a 30-year bond, 43-50% of the 2028 deposit (old design) | cost of immunising the reinvestment gap on the FINAL design (only if the rejected alternative is shown) |
| H2-030 | RE | coupons 41-46% of the long rungs' payments; 2041 rung gap at -2 for good $3,144 to $1,482 with the thin twin (old design) | per-rung reinvestment shortfall at -2 for good and coupon share per rung |
| H2-037 | RE | rule fires in 7 of 200,000 paths, always the 2042 payment (old design) | per-rung check frequency on the FINAL design |
| H2-040 | RE | median $17,953 back to Laura after 2033 (old set-aside) | what Keel's margin hands back to Laura at forward rates |
| H2-062 | FL CE | rival's lead +$66,837 in the best fifth; gifts equal at about 3%; $4k/$9k/$15k/$29k by ruler (old design) | price of the strongest rival (shares until 2031) on the FINAL design |
| H2-088 | CE | 2-point survivorship haircut: our median gift -$1k; a 60/40 -$41k; rivals broken 35-44% (old design) | the top and kept half at a lower VT return (for example 5.5% instead of 7.5%) |
| H2-091 | CE | shares wiped: 354-412 of 200,000 paths worse off (28 Oct design); 0 with the lock | a one-line check that shares at zero leave the payments unchanged on the FINAL design |
| H2-093 | C28 | IBTR trade note: "If yields fall more than about 0.2 percentage points" (6 Oct curve; submitted text) | a reconciliation line: by 6 Nov the ladder was already $2,287 over $300,000 |
| H3-099 | RE | M-squared per dollar at a flat 5%: Feb-2037 20 to Nov-2041 35 | per-rung reinvestment exposure on the 6 Nov curve |
| H4-007 | CE | kept half covers a full inflation top-up in about 5% of worlds (21% at 2% inflation; old design) | kept half against a Taiwan cost or Taiwan-dollar shock on the FINAL design |
| H4-048 | CE | inflation 2.5% (JPM LTCMA) | an inflation input and the real value of the 2042 payment (if used) |
| H4-061 | CE | Laura pays about nothing at the median for certainty (old design) | the median price of certainty against a share-heavy rival on the FINAL design |
| H4-064 | CE | M8 replay from 1923: shares about 7% for 15 years; a 60/40 bounces the 1937-38 cheques (old design) | a history replay of a share-funded rival, if the FR uses it |
| H4-086 | RE C28 | joint storm test spec; 2008 replay (yields -1.9pt, shares -40%, deposit -50%); P(coupon gap > kept half) base 7.7% (old design) | a joint-storm run (shares, yields and the deposit together), section 7's open limit |
| H5-003 | CE | certainty costs Laura almost nothing (R06 D4) | the median price of certainty against a share-heavy rival on the FINAL design |
| H7-040 | FL CE | protected note at 5.25%: zero 77.4%, call 22.6-22.9%; owning shares wins unless prices rise over about 32% | re-price on the 6 Nov curve (5-year 4.64%) if the comparison is used |
| H7-051 | C28 | ladder cost $292k (6 Oct), $298.9k (22 Oct), $300,608 (4 Nov); WInS +1.85% by 23 Oct | a dated history of the ladder's cost on one engine (ladder_history.py) |
| H7-108 | RE | Keel's lab runs 200,000 paths with parallel yield moves | the register should state its own house-model path count |
| H8-002 | C28 | $300,000 bought all ten only with the 10-year above about 5.0% (about one month in four since 1871); 2020 cost $469,000 | a history line on the 6 Nov curve (refresh the 2026 endpoint) |
| H8-080 | RE | thin-coupon twins: Nov-2040 46% coupons and $3,144 short (-2pt) vs 1.375% 22% and $1,482; Nov-2041 $3,019 vs $2,270 | per-rung reinvestment shortfall and coupon share on the 6 Nov curve |
| H8-086 | RE | 81% of the gap visible by Jan 2033 (89% in S6); 3.7% of paths see a gap after 2033; p99 $7,146 | share of the reinvestment shortfall visible by Jan 2033 (and 2031) on the FINAL design |
| H8-088 | RE | Redington: $64-74k of a 30-year bond (43-50% of the deposit; 9 times the holding) | cost of immunising the reinvestment gap on the FINAL design (rejected option) |
| H8-102 | RE C28 | short dollars: 35% a rung never bought, 49% the 2033 gap, 15% after 2033 (V52) | where the shortfall sits by year on the FINAL design |
| H8-105 | RE | honest lock $14,282 not $11,201; Feb-2037 and May-2038 waits $3,108 and $3,158 (22 Oct) | per-rung cost of the long waits at zero interest on the 6 Nov curve |
| H8-117 | FL CE | the floor gives up about $15k of growth (A26) | the price of owning the floor from 2028 vs a shares-until-2031 rival on the FINAL design |
| H8-123 | CE | deletion test: 0 of 600,000 futures worse; deposit halved shares help in 0.94% | a one-line check that shares at zero leave the payments unchanged on the FINAL design |
| H8-139 | FL CE | the floor wins on average only if shares beat Treasuries by less than about 3% a year (old design) | break-even share return between the FINAL and a shares-until-2031 rival |
| H9-012 | RE C28 | a lasting rate fall and an inflation burst together 8.6% vs 16.3% (1954-2011) | history statistic (MODEL) |
| H9-042 | RE C28 CE | tornado inputs: share return 6.5-7.5%; Taiwan cost inflation 2.5-3.5% (T08: 3.5-7%) | a sensitivity table: VT return low and high cases and Taiwan cost inflation |
| H9-048 | CE | delete-the-shares test: no payment worse in 600,000 futures (old design) | a one-line check that shares at zero leave the payments unchanged on the FINAL design |
| H9-049 | CE | clustered fat-tailed crashes moved the 1-in-20 gift by under $1,000 (old design) | a storm-regime run on the FINAL design |
| H9-054 | RE | rate fall and inflation burst together 8.6% vs 16.3% (1954-2011) | history statistic (MODEL) |
| H9-057 | RE | bond funds that never mature missed a payment in 11-13% of model paths | a duration-matched IEF/TLT rival on the FINAL design |
| H9-064 | C28 | spot rates 4.70% (2033) to 5.18% (2042) on 6 Nov; flat break-even 5.02% | the bootstrapped zero rate for each payment year and the flat break-even on the 6 Nov curve |
| H9-108 | CE | Vanguard VCMM, FP Canada, AQR and other house forecasts (about 5.8% and 6.5% blends) | a low case for VT growth beside 7.5% |
| H9-109 | CE | 7% / 7.5% / 5.8% / 6.5% bases; test 4% to 10% | a low and high VT growth case (the register gives only 7.5%) |
| H9-112 | FL | 2.5% inflation cuts the floor's real value by about 12% by 2033 | an inflation input and the floor's real value |
| H9-184 | C28 | ladder's room under $300,000 shrank to about $1,900 (16 Oct) | a dated history of the ladder's cost (ladder_history.py) |
| H10-047 | C28 | Flat-yield ladder cost: $300,000 at a flat 5.09%; $302,509 at 5%; $317,478 at 4.5%; $288,365 at 5.5% | the ladder's single equivalent yield on the 6 Nov curve (flat-yield illustration) |

### Outside facts, quotes, fund and WInS facts (a dated, sourced facts list could hold these; the engine cannot) (63 rows)

| Id | Tags | Figure in the row | What NUMBERS.md could add |
|---|---|---|---|
| H1-006 | FL | seed money raised from 10% to 67% of goal gave a nearly sixfold rise (List and Lucking-Reiley) | outside research fact (sourced fact list, not the engine) |
| H1-019 | CE | Taiwan construction cost index +6.53% y/y (Aug 2026), about 3.5% a year since 2021 | outside fact for INFLATION_TWD (sourced fact list) |
| H1-042 | CE | a 1% fee would have halved a pension's gain since 1942; "Helpers" take about 20% (Buffett); VT 0.06% matches section 0 | outside facts (Buffett); VT fee already on the register |
| H1-050 | CE | Buffett's 10/90 trust instruction | outside quote |
| H1-080 | RE | Equitable Life, Alabama PACT, Nissan Mutual details ($5.9m, 8%) | outside facts, unverified |
| H2-057 | FL | US giving fell 2.4% and 3.2% (real) in 2008-09; three to five years to recover | outside fact (sourced fact list) |
| H2-058 | FL CE | Harvard's endowment lost 30% | outside fact |
| H2-059 | FL | construction funds invested 12-36 months | outside fact |
| H2-060 | FL | farmers' 20-31% pre-sale range (never to size anything) | outside fact |
| H2-077 | CE | seed money raised from 10% to 67% of goal gave a nearly sixfold rise | outside research fact |
| H3-082 | CE | Harvard endowment fell 30% from $36.9bn; Princeton postponed $695m | outside fact |
| H4-012 | CE | Equitable Life: GAR £10 per £100; £1.5bn; £34bn assets | outside fact |
| H4-013 | CE | Dutch funding-ratio zones 104% and 110% | outside fact |
| H4-015 | CE | German maximum guaranteed rate 4.00% (1994) to 1.00% (2025); DAV 1.0% for 2027 | outside fact |
| H4-016 | RE C28 | Germany's old 4% guaranteed contracts | outside fact |
| H4-025 | FL CE | Brady 12-18 month rolling guarantee; 30-year zeros | outside fact |
| H4-026 | FL CE | Mexican par stripped spread 254bp to 452bp | outside fact |
| H4-027 | C28 | Pitt's £1m a year sinking fund | outside fact |
| H4-032 | FL CE | DSCR 1.20-1.30x at P50 and 1.00x at P99; P90 87% and P99 77% of P50 | outside fact and illustration |
| H4-041 | FL | lead gift 10-20% of the goal; leadership gifts 60% or more | outside fact |
| H4-050 | CE | Bursa cash waqfs 10.8% to 13%; about 20% survived a century | outside fact |
| H4-056 | C28 | Fukushima: 10 of 13 cooling systems in one basement | outside fact |
| H4-059 | CE | US real price appreciation 4.73% vs about 1.5% elsewhere | outside fact (unverified) |
| H4-148 | CE | VT's roughly 10,000 holdings | product fact (FINAL says "thousands") |
| H5-006 | FL | rivals lock in 2031 (9 of 12 scanned) | Keel's scan of rival plans (not a register figure) |
| H5-087 | RE | German maximum technical rate cut to 0.25% in 2022 | outside fact |
| H6-014 | CE | 25-35% in Treasuries; six, 12 or 18 months | outside quote |
| H6-024 | CE | US stocks 6.8% real vs 2.8% short bonds, 1871-2006 | outside fact |
| H6-058 | RE | home prices fell by more than half in the 1930s | outside fact |
| H6-061 | FL CE | TEPCO $25 to $5 a share | outside fact |
| H6-072 | CE | Apple beta 1.45 | outside fact |
| H6-074 | CE | Arnott's 14%; CRSP 11,232 of 30,361 funds died | outside fact |
| H6-075 | CE | Yale class of 1954: $375,000 to $90 million | outside fact |
| H6-076 | CE | Nikkei 38,000 to 10,500 (-73%) | outside fact |
| H6-077 | CE | Boston University lost 90% of $90 million | outside fact |
| H6-079 | CE | allocation explains more than 100% of returns | outside quote |
| H6-080 | CE | Damodaran US equity premium 4.41% on a 5.29% Treasury (1 Nov 2026); about 9.70% | outside fact (keep apart from VT's 7.5%) |
| H6-081 | CE | 10 or 20 years to revert to trend | outside quote |
| H6-082 | CE | random-walk run with no gain in 100 years | outside illustration |
| H6-118 | FL | Shiller's class: about 80% inside on one question, about 10% on others | outside fact |
| H6-121 | FL | 19 Oct 1987 -20.47%, 10^-71, 25 standard deviations | outside fact |
| H7-011 | RE | policy rate 0-0.25% from Dec 2008 to Dec 2015 and from Mar 2020 | outside fact |
| H7-013 | RE | Treasury called its 11.75% and 12.5% 2009-14 bonds in 2009 | outside fact |
| H7-039 | FL CE | FINRA fined UBS $2.5m and ordered $8.25m restitution | outside fact |
| H7-042 | CE | 16-market premium 4.04% vs US 4.52% (DMS 2008) | outside fact (stale edition) |
| H7-068 | FL | seed money 10% to 67% of goal: about sixfold (about 3,000 households) | outside research fact |
| H7-071 | FL | Kresge $1m challenge grant on $4.4m more | outside fact |
| H8-036 | RE | WInS bonds trade in $1,000 face units; 2x daily volume limit | competition rule facts |
| H8-113 | CE | Harvard endowment -30%, Yale -25%, Princeton $695m | outside fact |
| H8-149 | C28 | WInS hedge check: bonds +$5,967, VT -$386 (+1.85%) by 23 Oct; five T-bonds repay $96,000 face and pay $4,027.50 a year | a WInS book table (positions, face, coupons, value on 6 Nov) |
| H9-072 | FL | iBond fund facts 30 Sep (SEC yields 4.87-5.02%, durations 5.03-7.56); IBTM 5 Nov YTM 4.66% | fund facts table (register's IBTM YTM 4.86% is dated 23 Oct) |
| H9-073 | FL | iBond NAV tracking -0.03 to -0.05 points a year | fund facts table |
| H9-075 | RE | IBTR net assets $37m | fund facts table |
| H9-103 | CE | VT 10,185 stocks; $81.8bn; US 62.4%; Taiwan 3.5%; TSMC 1.6%; s.d. 11.80% | fund facts table (VT fee 0.06% matches section 0) |
| H9-104 | CE | VT holds 3.5% Taiwan; worth a few hundred dollars as a hedge | fund fact and a small hedge sizing |
| H9-110 | FL CE | FP Canada: actual rates for projections under 10 years | outside rule |
| H9-131 | FL | Kresge: raise at least 20% and sometimes 50%; pledges within five years | outside fact |
| H9-132 | FL | seed money 10% to 67% of goal: nearly sixfold (3,000 residents) | outside research fact |
| H9-134 | FL | ROM: $23M of pledges unpaid; 25% before naming | outside fact |
| H9-148 | FL CE | each WInS rung scaled to 67-72% of a full $50k rung | WInS book scaling per rung |
| H9-180 | FL | no WInS Treasury maturing Feb 2031 to Feb 2036; two bonds about 1 point off the curve; 0.25-point check rule | WInS and process facts |
| Q1-010 | C28 | human capital's stock component under 35% | outside research fact |
| Q1-044 | C28 | shares -36.55% (2008), +25.94%, +14.82%; el-hi sales -13.8%; licensing -8.7%; library -9.4% | outside facts |

### Arithmetic, illustrations, or rules not in the FINAL (nothing to add) (9 rows)

| Id | Tags | Figure in the row | What NUMBERS.md could add |
|---|---|---|---|
| H1-029 | FL | 0 of 200,000 bottom breaks vs 0.11% for a fixed $10k pad (old design) | NUMBERS.md uses a fixed 4.1% deduction instead (section 3); the pad comparison is not on the register |
| H2-017 | CE | ten separate 99% bets miss one about 9.6% of the time | arithmetic illustration (no need to add) |
| H2-045 | RE | kept half emptied by the gap in 19% / 42% / 65% / 86% (old design) | none needed: in the FINAL the kept half never backs a payment |
| H2-106 | CE | a 20% fall needs a 25% rise | arithmetic (no need to add) |
| H4-017 | FL CE | ruin falls as a power; 1-in-10 to 1-in-100 illustrations | illustration (no need to add) |
| H4-091 | CE | newsvendor fractiles at k = 3, 5, 10 (25%, 17%, 9%) | arithmetic for a test (no need to add) |
| H7-041 | CE | at-the-forward put 6.7% (1y) to 29.2% (20y) at 16.78% volatility | arithmetic (volatility matches section 0) |
| H7-107 | RE | an unhedged reserve at 0% costs its full $500,000 face; the list's -82% | arithmetic; the register's zero-interest test is $54,595 short as written (section 2) |
| H8-148 | RE | kept money borrowed for the gap 7 in 10 times; a quarter kept back cuts "empty by 2033" from 1 in 5 to 1 in 15 (old designs) | none needed: in the FINAL the kept half never backs a payment |

## (a) rows, consistent with NUMBERS.md

| Id | Tags | Figure | Matches |
|---|---|---|---|
| H1-046 | CE | bonds bought near 5% | 6 Nov curve 4.33% (1y) to 5.29% (20y); 10y 4.86% (section 0) |
| H2-067 | CE | global equities 7.5% (J.P. Morgan 2027 LTCMA) | VT median growth 7.5% (section 0) |
| H2-094 | RE | Feb-2037 bond's 10.5-month gap | TNA note 1's 10.5-month gap (section 2) |
| H3-040 | CE | co-sponsors get 50% of VT and Laura keeps 50% | moved half and kept half (section 4) |
| H3-057 | CE | J.P. Morgan 2027 LTCMA global equities 7.5% | VT median growth 7.5% (section 0) |
| H3-092 | FL CE | fees 0.06-0.07% a year; 50% participation | VT 0.06%; iBond funds 0.07%; half moved, half kept (section 0) |
| H3-095 | RE | dedicated sizing roughly halves the reinvestment risk | design B halves it at the same cost (section 2) |
| H4-089 | CE | re-run at 7.5% less 0.6 and 2.0 points | VT median 7.5% (section 0) |
| H4-092 | C28 | deposit-by-yields grid ($0 to $150k against 0, -1, -2 points) | done in section 5 (smallest deposit by yield fall) (section 5) |
| H4-100 | RE | 10.5-month gap | TNA note 1's gap (section 2) |
| H4-134 | CE | half the shares promised = 50% participation | moved half and kept half (section 4) |
| H4-149 | CE | VT fee 0.06% | VT fee 0.06% (section 0) |
| H4-151 | CE | 7.5% for VT: which edition (2026 AC World 7.00%, EAFE 7.50%) | settled: J.P. Morgan 2027 LTCMA global equities 7.5% (section 0) |
| H5-076 | CE | only half of VT counts toward the top | moved half (section 4) |
| H6-004 | RE | 10.5-month gap | TNA note 1's gap (section 2) |
| H6-047 | CE | the promised $50k a year | case fact (section 0) |
| H7-001 | RE | 2038 rung matures 10.5 months early, 2039 rung 7.5 months early | Feb 2037 and May 2038 bonds (section 0) |
| H7-061 | FL CE | half the shares as the uncommitted residual | kept half (section 4) |
| H7-074 | C28 FL | a smaller deposit comes off the bottom almost dollar for dollar | section 5: the floor shrinks almost dollar for dollar (section 5) |
| H8-138 | CE | VT fee 0.06% (eleven WInS trades in total) | VT fee 0.06% (section 0) |
| H9-038 | C28 | stresses: 0.5-point fall before 2027; a $75k deposit; payments change by $0 | 0.5-point fall costs $15,455; a $75k deposit leaves the payments whole and a floor of about $47k (section 1 and 5) |
| H9-060 | C28 | 6 Nov curve 2y 4.51 to 30y 5.26 (2026 10-year range 3.97% to 5.31% not on the register) | section 0 curve (section 0) |
| H9-070 | FL | iBond fee 0.07%; monthly payouts; end on or about 15 Dec | section 0 inputs (section 0) |
| H9-071 | RE | iBond rung pays about two weeks before 1 January | funds end on or about 15 Dec (section 0) |
| H9-078 | C28 FL | $150k / $112.5k / $75k deposits; floor shrinks almost dollar for dollar | section 5: floor about $81k at $112,500 and $47k at $75,000 (section 5) |
| H9-089 | C28 | shares fall 40% in 2032 and the range holds | after the move nothing changes either end (section 4) |
| H9-107 | CE | J.P. Morgan 2027 LTCMA global equities 7.5% (other classes not used) | VT median growth 7.5% (section 0) |
| Q1-047 | C28 | the $150,000 deposit in 2028 | case fact (section 0) |

