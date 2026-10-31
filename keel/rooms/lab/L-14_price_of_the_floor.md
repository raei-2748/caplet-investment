# FICTION (the room) + real work (the test). L-14: the price of the floor (Q12, why not a safe ladder and the rest in stocks?)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Sat 31 Oct
2026, 13:40 Sydney, round 4 beat 5 (Felix builds; Kai roasts; Jun and Kai give the verdicts; huddle H-005). Script
`L-14_price_of_the_floor/run.py`; results `L-14_price_of_the_floor/results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | V39's design = LR8 "MB+T +lock" with L-13's slide, via L-13's chain, unchanged, one block
appended | MODEL.** Reproduction: XR's row matches L-13's "A slide" exactly in every world (S0: top 97.9%, gift p5/p50
$130k/$165k, cheques short >$1k 0.03%, quoted bottom broken 0 of 200,000).

**For a judge, in plain words.** We built the plan a growth-minded judge would write: the same Treasury ladder for the
ten cheques, the 2028 deposit 80% in world stocks, and the gift's bottom bought in Treasuries only in 2031, when Laura
names her range. We ran it on the same 200,000 model paths as ours. It never misses a cheque either. Its typical gift is
about $5,000 bigger and its average about $15,000 bigger, and every dollar of that is the stock premium: give stocks only
the Treasury yield and the gap disappears. What it's paid for is carrying a crash in 2028-30. In the worst one market in
twenty before she names it, the bottom Laura can promise co-sponsors comes in about $45,000 lower than ours. That's the
year giving usually falls too.

**Why this, today.** Q12 (round 4, Nora's gather): two of six blind panel-4 judges put A09 first; V39 beats a 60/40 and
three-quarters stocks in words, never A09. Requests closed: Rooftop (A09 beside V36's design, same paths), Library (the
price of the floor, out loud), Window (W-04's number; R06's "a fifteenth" on this design). North stars 3 and 4;
Investment Strategy ("balance growth, risk, liquidity, funding reliability, and financial flexibility"), Portfolio
Analysis. IPS line that could change: V39 para 7, "In our model, with world stocks at 7.5% a year, a 60/40 portfolio
usually leaves her richer. But about one time in three ..." (aimed at the wrong rival).

## A09 as built (at its strongest)
Same ladder and the same 2027 gap rule. The 2028 remainder R goes 80% world stocks (the same VT draws as XR's fund, fee
included) and 20% intermediate Treasuries (5-year yield, duration 4.5), rebalanced yearly. On 1 Jan 2031 a share k of the
pot buys a 2-year Treasury held to January 2033: that is the bottom. The rest stays 80/20; the gift is the bottom plus
half the rest, capped at the top; the other half is Laura's. A09 is given every XR rule as well: the 2031 mark (cushion
$7,500, the 2031 sale from Laura's half into bills), the slide. **k = 0.8** keeps about the same fifth in stocks after
naming as XR (XR's median 22.2%), so Laura's own money in 2042 comes out level (S0 median $38k v $36k): the plans differ
in when the floor is bought, not in how much she keeps. k = 0.65 is the sensitivity.

## Pairings tried
- **J2 (farmers lock each bushel the day it's sure) x A09's timing:** Laura's 2028 deposit is sure in 2028; A09 locks in
  2031 for no reason the farmers would accept. (-> A)
- **J3 (for a farmer the hedge is nearly free; for Laura it isn't) x the premium:** what exactly does XR give up, and is
  it a cost or a price? (-> B, the premium test)
- **W-04 (giving falls in recessions) x N1 (Harvard paused when the pool fell 30%) x the worst-5% slice:** how far does
  A09's bottom fall in the market that shrinks everyone else's giving? (-> C)
- **A2 (no city may put building money in shares) x XR's stock slice:** convicts XR too (a fifteenth in stocks). Kept as
  the honest weakness, not a challenger.

## Challengers, with the novelty check
(`../../IDEAS.md`, this book, the Library's slips, R02, R05, `../../loop/FRONTIER.md` s3, the binned list, the bank)

| # | Challenger | Novelty | Builder |
|---|---|---|---|
| A | **Grain in the bin:** buy the floor the year the money is sure (2028), not the year it's named (2031); answer A09 by name in the IPS | **Return** of #4, #45, #93, #97; new step: the number beside it | Felix |
| B | **Same price, different risk:** both plans start with the same $150,000; A09's extra average is the stock premium, pay for carrying a 2028-30 crash, and Laura is the wrong person to be paid for it (her income, #7; her co-sponsors, #94) | **New step** on FRB-13 (a bank sells the same protection) and #36 (risk only the interest): nobody has shown the gap IS the premium | Felix |
| C | **Harvard at a smaller scale:** A09's 1-in-20 bottom is about a third below its typical bottom, the fall that stopped Harvard's science building | **Return** of #95 with a number | Felix |

## Results (MODEL; S0 base / S1 recession-linked; S6 yields -2pt for good; S2 2028 deposit halved)

| | XR (V39) | A09 (k = 0.8) | A09 (k = 0.65) |
|---|---|---|---|
| Cheque >$1k short, S0 / S1 / S6 / S2 | 0.03 / 0.03 / 0.05 / 0.05% | 0.02 / 0.02 / 0.03 / 0.05% | 0.02 / 0.02 / 0.02 / 0.03% |
| Gift p5 / p50 / p95, S0 | $130k / $165k / $180k | $110k / $170k / $257k | $100k / $155k / $235k |
| Gift mean, S0 / S1 / S6 / S2 | $160k / $160k / $142k / $72k | $175k / $175k / $161k / $79k | $159k / $160k / $150k / $73k |
| Quoted bottom p5 / p50, S0 | $115k / $145k | $95k / $150k | $80k / $125k |
| Quoted bottom below $100k, S0 / S1 / S6 | 0.9 / 1.0 / 7.9% | 5.3 / 6.7 / 16.3% | 17.5 / 18.5 / 27.6% |
| Top reached, S0 / S6 | 97.9 / 96.0% | 92.0 / 92.1% | 87.4 / 88.3% |
| **Worst 5% of 2028-30 stock markets: bottom / gift (median), S0** | **$140k / $155k** | **$95k / $105k** | $80k / $95k |
| same, S1 / S6 | $135k / $150k; $115k / $125k | $90k / $100k; $70k / $80k | |
| Best 5%: gift (median), S0 | $180k | $280k | $250k |
| Laura's own money in 2042, median, S0 | $38k | $36k | $67k |

**The price, path by path (XR minus A09 k = 0.8):**
| | S0 | S1 | S6 | S2 |
|---|---|---|---|---|
| Median gift | -$5k | -$5k | -$10k | $0 |
| Mean gift | -$14.7k | -$15.3k | -$18.9k | -$7.3k |
| Mean gift + Laura's 2042 money | -$10.1k | -$10.6k | -$23.9k | -$5.0k |
| XR's gift higher in | 35.5% of paths | 35.8% | 32.0% | 33.2% |
| Worst 5% of 2028-30: bottom, median difference | +$40k | +$45k | +$45k | +$20k |
| Worst 5%: gift, median difference | +$45k | +$45k | +$45k | +$25k |
| Best 5%: gift, median difference | -$100k | -$105k | -$110k | -$50k |

**The premium test** (the gift money alone in 2033, no halves, no cap; same shocks): with stocks at 7.5%, A09 is
**$11.3k / $11.9k / $21.2k / $5.7k** richer on average (S0 / S1 / S6 / S2). Give stocks only the 2028 five-year Treasury
yield and the gap is **-$1.0k / -$0.4k / -$0.3k / -$0.2k**. So the whole of A09's average lead is the stock premium. Its
1-in-20 low is $23k below XR's at 7.5% and $31-33k below with the premium removed.

**Window R06 ("about a fifteenth"):** on this design the stock fund on 2 Jan 2028 is $31,082 (median), **6.6% of the
portfolio, one part in 15.1** (S0, S1); 6.9% of both deposits; 20.7% of the 2028 deposit. After a 2-point fall (S6) it
is one in 24; with half a deposit (S2) one in 26. So "a fifteenth" holds, but of the **portfolio**, not "everything she
owns" (V40 cold read (b)), and only on today's yields.

**Reconciling the gaps (Jun's loose end, H-005 r1):** the mean *gift* gap ($14.7k, S0) is bigger than the premium test's
gift-money gap ($11.3k) because XR's cap binds more often (top reached 98%) and the money above its top stays with
Laura; the gap in gift + Laura's own 2042 money is $10.1k. With every rule in (halves, cap, 2031 sale), the full model
at about 3% world stocks gives a mean gift gap of -$0.4k (below). The premium test's answer holds.

## Checks asked for in the huddle (H-005 r2; `../../huddles/2026-10-31_the-price-of-the-floor/research/lab_checks_r3.md`)
- **Kai: the break-even stock return.** Average gifts are equal at about **3% a year** compound (S0 $157.2k v $156.8k;
  S1 and S2 the same; in S6 A09 is ahead even at 3%, by $3.3k). Medians cross between 5% and 6%. At 3% compound with
  16.78% volatility, the average yearly return is about the Treasury yield: the premium test from the other side.
  So A09's lead needs only that stocks beat Treasuries; it is not an artefact of J.P. Morgan's 7.5%. What 7.5% sets is
  its size ($15k).
- **Felix: do A09's low bottoms come from stock losses?** Of its 2031 bottoms under $100k, **93% (S0) / 94% (S1)** are
  paths where world stocks lost money over 2028-30 (23% of all paths); 75% / 73% sit in the worst tenth; median 2028-30
  stock return **-25% / -24%**. A09's broken bottom *is* a 2028-30 bear market, the years giving "typically ... stays
  flat or falls" (Giving USA 2010, W-04) and Laura's advances and licensing income shrink (bank #7).
- **Jun: reconcile.** Above.

**Headline check (numbers-auditor's method, done in the run):** (a) deterministic: re-runs with the same seed give
identical numbers (three runs today); XR's row equals L-13's "A slide" to the dollar in all four worlds. (b) Back of the
envelope for the $11.3k premium-test gap: A09 holds about $89k more in stocks than XR for three years (80% v 20.7% of
$150k); at about 9.0% arithmetic (7.5% compound plus half the variance) against the 2028 five-year yield (about 4.3%),
that is 4.7% x 3 x $89k = $12.5k before compounding and the 2031-33 tail: the same size. (c) Sanity: A09 misses no more
cheques than XR (0.02 v 0.03%), as A09.md claims.

## The huddle (H-005, `../../huddles/2026-10-31_the-price-of-the-floor/transcript.md`)
Round 1: Felix played A09's advocate (the cheques are as safe, the gift is bigger, a top you always reach is set too
low); Jun read the numbers (A09 is fair, even generous; the honest pair is unsliced; the worst-5% slice flatters XR by
construction); Kai roasted (we built A09's cousin, we picked the slice, the farmers' hedge is free and ours costs
$15k; bet: XR wins only if A09's low bottoms cluster in crash years). Round 2: Kai moved to Felix's link (Laura's own
income, not strangers' giving); Felix dropped the slice and "98 v 92"; Jun called "same price, different risk" a trick
unless it says "pay for carrying the crash". Round 3: the checks above; Kai lost the bet and said so; 3-0 ADOPT.

## Verdicts (the builder doesn't judge)
- **B, the price of the floor: ADOPT, 3-0, as one IPS paragraph** (A's timing inside it): answer "why not a safe ladder
  and the rest in stocks?" with the unsliced pair (bottom under $100k about 1 in 15-20 v 1 in 100) and the price out
  loud (about $15,000 of average gift at 7.5%). Replaces V39 para 7's 60/40 sentences plus one 18-19-word cut the
  rewrite thread picks. Jun: "Called 'same price', it's a trick. Called 'pay for carrying the crash', it's true." Kai:
  "I lost. Write it down."
- **A, grain in the bin: folded into B** (the farmers' calendar goes to the FR).
- **C, Harvard at a smaller scale: PARK** (FR beside the table; one picture in the IPS is XR's).
- **Not adopted:** the worst-5% slice, "98% v 92%", "same price, different risk" as words.

**Ninety-second rule:** "You can keep the rest in stocks till 2031 and the cheques are still safe. What you can't keep
safe is the number she tells co-sponsors. About one time in twenty it's under $100,000, nearly always after a crash.
We pay about $15,000 of average gift so that's one in a hundred."
