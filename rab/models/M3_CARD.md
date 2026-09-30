# M3 model card: the Branch, 2028-2033

WS2, 30 Sep 2026 (Sydney). Code `rab/models/m3_branch.py`; spec `M3_SPEC.md`; results `rab/results/M3/`.
AI-generated research (Claude Code) for Team Caplet. All figures are Laura's plan, MODEL, 28 Sep 2026 curve.

**What it does.** It follows the stock fund (about $41,000 bought on 2 Jan 2028) through 2033 under the adopted rule.
In 2031 the range is the $150,000 floor up to the floor plus half the fund's value that day. In 2033 the gift is the
floor plus half the lower of the fund's 2031 and 2033 values. It runs four return models, each on 200,000 paths
with seed 20260930, all centred on JPM's 7.00% for world stocks.

| Model | 2031 top: median (90% of paths) | 2033 gift p5 / p50 / p95 | Gift reaches the top | Gift in upper half |
|---|---|---|---|---|
| Fat tails (Student-t, nu = 4) | $175k ($166k-$189k) | $165k / $174k / $188k | 75% | 99.9% |
| History (Shiller bootstrap, 1871-2025, 24-month blocks) | $175k ($165k-$189k) | $164k / $175k / $188k | 74% | 99.2% |
| Uncertain mean (Bayesian, pymc) | $175k ($165k-$191k) | $164k / $174k / $190k | 72% | 99.9% |
| Reference lognormal (insight_v1 E6 method) | $175k ($166k-$189k) | $165k / $174k / $188k | 73% | 100% |

**Stated confidence.** The gift lands inside the 2031 range. This is **certain by construction if** (a) the floor holding
pays its face value, (b) the 2028 deposit arrived in full (known before 2031), (c) the gift is capped at the top, and
(d) no fee is taken from the floor. Across 1.6 million model paths, no gift fell outside its range. The models add only
where in the range the gift lands: at the top in about 3 of 4 cases, and in the upper half in about 99 of 100.
In about 1 in 5 cases (21-24% by model) the fund is worth less in 2031 than it cost in 2028. The range is then narrower, but its bottom
does not move.

**Checks passed.** The analytic median top ($174,952) and P(top) (73.3%) match. On E6's own basis (fund $40,443) the
reference model reproduces insight_v1 H8 within $0.4k on every figure (`reconcile_E6.csv`). The Bayesian fit converged
(r_hat <= 1.001, bulk ESS >= 2,200; posterior sd of annual log returns 0.171, tail index nu about 15 at the median).
The bootstrap shows no memory: the chance of reaching the top is 74% whether the fund is above or below its median in
2031 (`conditional_top.csv`).

**Assumptions.** Fund bought 2 Jan 2028 = $40,736 (Gate A, Nov-15 basis). $150,000 floor, no fees, s = 1/2. Returns
in U.S. dollars, with no link to interest rates. The shape comes from U.S. history, used as a stand-in for the global
fund VT.

**Data.** Shiller ie_data.xls (monthly, 1871-2026, shillerdata.com) and Damodaran histretSP (1928-2025), both fetched
30 Sep 2026 and byte-identical to WS3's copies (`rab/data/ws2_returns/MANIFEST.csv`). JPM 2026 LTCMA AC World
7.00% / 8.28% / 16.78% (repo PDF, data as of 30 Sep 2025).

**Limits and failure modes.**
- Shiller prices are monthly averages, which smooth volatility a little. The block bootstrap restores the annual sd
  (0.175 against Damodaran's 0.189 for year-end prices).
- U.S. history is a single, unusually good market (WS5 ref [15]). The bootstrap is re-centred on 7.00% for that reason.
  The raw-history variant gives a median top of $177k.
- Forecasts of the centre could be wrong by more than the Bayesian 1.5-point sd. With a 4.08% centre (Vanguard-like
  low), the median top is $173k (M8). The effect is small because only 3 years of returns on about $41k matter.
- The Student-t is truncated at 5 sd so that averages exist; 0.27% of raw draws were redrawn.
- M3 assumes no rate path. Yields at the January 2027 purchase and in January 2028 move the range far more (M8).
- The floor's own payout is taken as exactly $150,000 here; M4 relaxes this.

**What this teaches (plain English).** The choice of stock model hardly matters. It moves the typical 2031 top by less
than $1,000, the 1-in-20 low top by about $1,000 and the 1-in-20 high top by about $2,000. Only about 9% of Laura's money is in stocks, and only half of that is
promised, so model risk stays small. The bottom never depends on a model. The top is a fair "expected" figure: it is
reached about 3 times in 4, and the gift almost never lands in the lower half.

**Gate B (30 Sep 2026).** A blind rebuild from `M3_SPEC.md` agrees on every M3 key within tolerance (largest gaps in
the three decision models: median top $34, P(top) 0.12 points; `rab/gates/gate_B_ws2.md`). Each build's rule code gives the other's published
figures exactly on the other's paths, so the gaps are sampling noise. On insight_v1's own random draws the reference
model reproduces E6's printed H8 figures exactly. Wording fix at this gate: the 1-in-20 low top moves by about
$1,000 across models (it said $2,000, which is the 1-in-20 high top).
