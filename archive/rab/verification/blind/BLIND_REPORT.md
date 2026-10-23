# WS3 blind rebuild: M5 history, M6 rivals, M7 stress (report)

Built from `rab/models/M5_SPEC.md`, `M6_SPEC.md`, `M7_SPEC.md`, `rab/data/` and the locked `rab/numbers.yaml` only (28 Sep 2026 curve). Every figure is MODEL output. Flat key list: `out/blind_headlines.json` (1392 keys). Generated 2026-09-30T09:08:45+10:00.

## M5: cost of certainty and the century backtest

- Reproduction of the locked history figures on the 1990-2026 daily curves: 9/9 agree (today $289,119; 2020 median $458,828; peak $470,249 on 2020-08-04; cheapest since 2002-05-28).
- Extended to 1871: lowest $110,214 (1981-09-30), highest $470,249 (2020-08-04). Share of months since 1871 at least as cheap as today: 23.3% (23.5% after the flat-curve correction); at or under $300,000: 26.3%. Since 1962: 51.1%. Calendar years whose median cost was below today's: 23.1% (36 of 156).
- Flat-curve check 1962-2026: flat/full - 1 median 0.76% (5th-95th -0.84% to 2.05%). FRED vs Treasury file: largest difference $0.

| view | fund | worst gift (Y) | p10 | median | p90 | best | median T33 | median real gift | top reached | windows with top-up (largest) | short |
|---|---|---|---|---|---|---|---|---|---|---|---|
| hist | world_eq | $29,498 (2020) | $66,507 | $131,555 | $227,009 | $404,067 | $131,555 | $125,200 | 96.0% | 112 ($121,027) | 0 |
| hist | us_eq | $29,498 (2020) | $66,507 | $131,555 | $230,915 | $363,376 | $131,555 | $124,682 | 94.0% | 112 ($121,027) | 0 |
| today_yields | world_eq | $158,969 (1928) | $169,056 | $175,903 | $187,368 | $200,060 | $213,571 | $156,699 | 84.6% | 0 ($0) | 0 |
| today_yields | us_eq | $157,825 (1929) | $168,131 | $175,982 | $185,556 | $195,631 | $215,211 | $155,119 | 78.5% | 0 ($0) | 0 |
| today_yields_rescaled | world_eq | $158,349 (1928) | $167,451 | $174,092 | $184,418 | $196,597 | $206,413 | $154,351 | 75.8% | 0 ($0) | 0 |
| today_yields_rescaled | us_eq | $157,364 (1929) | $166,676 | $174,246 | $183,462 | $192,944 | $208,938 | $153,603 | 73.2% | 0 ($0) | 0 |

Era table (history's yields, world stocks): 1872-1913: ladder $346,303, median gift $122,016, worst $97,286 (1899); 1914-1945: ladder $356,228, median gift $110,715, worst $46,879 (1941); 1946-1981: ladder $328,108, median gift $149,896, worst $54,169 (1946); 1982-2020: ladder $301,211, median gift $168,310, worst $29,498 (2020).
Today-yields check: fund0 40,736.20 vs 40,736; floor cost 117,193.70 vs 117,194 (both within $1).

## M6: rivals on the same metrics, and the branch-fund rule

History lens, 149 start years 1872-2020 (R6: 140 inflation paths):

| rival | unfunded share (largest shortfall) | T33 worst / p10 / median / p90 | gift worst / p10 / median / p90 | certain in 2031 (median) | top reached | trades |
|---|---|---|---|---|---|---|
| REC | 0.0% ($0) | $29,498 / $66,507 / $131,555 / $362,797 | $29,498 / $66,507 / $131,555 / $227,009 | $131,555 | 96.0% | 13 |
| R1 | 0.0% ($0) | $29,498 / $66,507 / $131,555 / $303,630 | $29,498 / $66,507 / $131,555 / $303,630 | $131,555 | 100.0% | 12 |
| R3 | 0.0% ($0) | $41,569 / $78,789 / $144,719 / $372,289 | $16,130 / $34,442 / $62,582 / $143,373 | $0 | 85.9% | 21 |
| R2 | 1.3% ($35,341) | $-35,341 / $83,431 / $221,833 / $527,149 | $0 / $33,885 / $82,003 / $186,472 | $0 | 74.5% | 24 |
| R4 | 2.0% ($58,161) | $-58,161 / $81,714 / $180,302 / $440,016 | $0 / $35,596 / $78,904 / $179,763 | $0 | 71.8% | 24 |
| R4b | 2.0% ($88,182) | $-88,182 / $88,461 / $239,961 / $557,699 | $0 / $30,930 / $93,423 / $212,751 | $0 | 73.8% | 24 |
| R5_m3 | 0.0% ($0) | $33,117 / $66,389 / $130,982 / $511,595 | $15,058 / $30,874 / $60,831 / $168,444 | $0 | 94.0% | 72 |
| R5_m5 | 0.0% ($0) | $33,117 / $66,389 / $127,622 / $577,738 | $15,058 / $30,874 / $59,421 / $191,091 | $0 | 93.3% | 72 |
| R6 TIPS ladder | 65.7% of paths have at least one payment short (largest total gap $107,935; 47.6% of payments short; 45.7% pay less than $500,000 in total) | = REC | n/a | n/a | n/a | 13 |

MC lens (JPM 2026 LTCMA, 200,000 paths, seed 20260930):

| rival | unfunded share | T33 p5 / p50 / p95 | gift p5 / p50 / p95 | top reached | notes |
|---|---|---|---|---|---|
| REC | 0.00% | $181,352 / $206,777 / $252,228 | $164,579 / $173,998 / $188,629 | 73.4% |  |
| R1 | 0.00% | $190,892 / $202,188 / $213,317 | $190,892 / $202,188 / $213,317 | 100.0% |  |
| R3 | 0.00% | $154,135 / $216,349 / $307,645 | $72,007 / $94,284 / $124,454 | 83.0% |  |
| R2 | 1.25% | $53,653 / $244,730 / $527,953 | $21,061 / $96,152 / $194,954 | 66.8% |  |
| R4 | 0.18% | $87,668 / $232,700 / $434,200 | $36,621 / $100,271 / $184,928 | 77.0% |  |
| R4b | 2.27% | $35,675 / $247,845 / $572,493 | $10,985 / $100,047 / $226,328 | 68.9% |  |
| R4b_dep75k | 10.68% | $-37,778 / $144,678 / $424,197 | $0 / $54,216 / $164,443 | 68.5% |  |
| R4b_dep0 | 35.24% | $-112,446 / $41,250 / $277,886 | $0 / $8,211 / $103,349 | 75.3% |  |
| R5_m3 | 0.00% | $153,284 / $198,892 / $411,314 | $70,931 / $88,682 / $141,526 | 78.0% | $150,000 promise met in 98.0% of paths (cushion negative at some 1 Jan 2028-32 in 1.6%) |
| R5_m5 | 0.01% | $123,928 / $175,381 / $582,972 | $56,983 / $79,794 / $189,470 | 75.7% | $150,000 promise met in 73.6% of paths (cushion negative at some 1 Jan 2028-32 in 22.6%) |
| R6 TIPS ladder | 60.0% (any payment short) | = REC | n/a | n/a | 44.4% of payments short; 44.3% of paths pay less than $500,000 in total; median gap $4,400 |

H16 re-verified (growth-first R4b, share of paths where the money cannot buy the reserve): 2028 deposit $150k 2.3%, $75k 10.7%, none 35.2% (insight_v1 on the 25 Sep curve: 3.2% / 13.7% / 40.8%).

Branch-fund alternatives (REC fixed except the fund; fund0 $40,736; buy-and-hold):

| fund | MC gift p5 / p50 / p95 (spread90) | MC P(top) | history 1928-2020 gift p10 / p50 / p90 (spread80) | ETF 2011-2020 gift p50 | rule |
|---|---|---|---|---|---|
| A0 VT (baseline) | $165,150 / $174,171 / $187,907 ($22,757) | 73.4% | $168,863 / $177,613 / $187,368 ($18,506) | $175,915 | baseline |
| A1 VTI + VXUS 62/38 | $165,432 / $174,326 / $187,768 ($22,336) | 74.4% | $169,053 / $177,976 / $187,160 ($18,107) | $177,182 | KEEP VT (tests 1-3 fail; 0/20 seeds) |
| A2 U.S. only (VTI) | $165,105 / $173,940 / $187,313 ($22,208) | 72.8% | $167,382 / $178,096 / $186,268 ($18,887) | $179,245 | KEEP VT (tests 1-3 fail; 0/20 seeds) |
| A3 VT + small/value tilt | $165,091 / $174,256 / $188,354 ($23,263) | 73.5% | $169,675 / $179,203 / $190,099 ($20,424) | n/a | KEEP VT (tests 1-3 fail; 0/20 seeds) |
| A4 VT + gold/REIT | $166,300 / $174,501 / $186,780 ($20,480) | 76.5% | $170,251 / $176,876 / $185,031 ($14,780) | $175,334 | KEEP VT (not seed-robust) (tests 1-3 pass; 14/20 seeds) |

Pre-registered switch rule outcome: VT stays. A1: KEEP VT; A2: KEEP VT; A3: KEEP VT; A4: KEEP VT (not seed-robust).
R6 inputs: breakevens 6-15y 2.34-2.39%; inflation AR(1) phi 0.741, sigma 1.87pp, mean 2.34%, start 3.40%.

## M7: stress scenarios and the real value of the payments

| scenario | shift before purchase (pp) | ladder cost 1 Jan 2027 | top-up 2028 | floor face | fund0 | 2031 range bottom-top | 2033 gift | T33 | payments funded | real gift (2027 $) | real 2042 payment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S0 Base | +0.00 | $292,418 | $0 | $150,000 | $40,736 | $150,000-$174,952 | $174,952 | $207,135 | yes | $152,281 | $35,342 |
| S1 1970s stagflation (1973 plays 2027) | +0.00 | $292,418 | $0 | $150,000 | $43,540 | $150,000-$175,372 | $175,372 | $210,315 | yes | $110,093 | $18,414 |
| S2 Japan's lost decade (1990 plays 2027) | +0.00 | $292,418 | $0 | $150,000 | $35,956 | $150,000-$162,678 | $161,659 | $173,319 | yes | $146,551 | $45,534 |
| S2b Japan, rates fall first (-1.00 pp before the | -1.00 | $322,582 | $24,401 | $147,189 | $0 | $147,189-$147,189 | $147,189 | $147,189 | yes | $133,433 | $45,534 |
| S3 2022 in 2028 | +0.00 | $292,418 | $0 | $150,000 | $40,736 | $150,000-$169,315 | $169,315 | $194,228 | yes | $132,984 | $31,891 |
| S3b 2022 in 2027 | +0.00 | $292,418 | $0 | $150,000 | $52,075 | $150,000-$181,897 | $181,897 | $223,037 | yes | $142,865 | $31,891 |
| S4a Downgrade, S&P (5 Aug 2011, after the close) | -0.56 | $308,897 | $9,275 | $150,000 | $20,357 | $150,000-$162,469 | $162,469 | $178,552 | yes | $141,416 | $35,342 |
| S4b Downgrade, Fitch (1 Aug 2023, after the clos | +0.07 | $290,429 | $0 | $150,000 | $43,213 | $150,000-$176,469 | $176,469 | $210,609 | yes | $153,602 | $35,342 |
| S4c Downgrade, Moody's (16 May 2025, after the c | +0.03 | $291,564 | $0 | $150,000 | $41,800 | $150,000-$175,603 | $175,603 | $208,626 | yes | $152,848 | $35,342 |
| S4d Downgrade plus buyers' strike (hypothetical) | +1.00 | $265,401 | $0 | $150,000 | $74,761 | $150,000-$184,238 | $184,238 | $228,397 | yes | $160,364 | $35,342 |
| S5 Great Depression (1928 plays 2027) | +0.00 | $292,418 | $0 | $150,000 | $42,231 | $150,000-$159,298 | $159,298 | $176,632 | yes | $208,777 | $51,183 |
| S6 2008 in 2028 | +0.00 | $292,418 | $0 | $150,000 | $40,736 | $150,000-$164,302 | $164,302 | $182,748 | yes | $143,011 | $35,342 |
| S7 Great Inflation (1966 plays 2027) | +0.00 | $292,418 | $0 | $150,000 | $41,070 | $150,000-$178,826 | $178,826 | $217,614 | yes | $138,362 | $18,424 |

Thresholds on the base path (yields fall x before 1 Jan 2027 and stay there): top-up starts at 26.2bp; the stock fund reaches $0 with the $150,000 floor intact at 109.3bp; a payment is unfunded at 428.4bp.
Measured downgrade moves (FRED DGS10, announcement-day close to 20 trading days later): S4a -0.56pp (S&P 500 -2.1%); S4b +0.07pp (S&P 500 -1.7%); S4c +0.03pp (S&P 500 +1.3%).

Real value of the $50,000 payments in 1 Jan 2027 dollars: breakeven (2.3%/yr): 2033 $43,521, 2042 $35,342, ten payments $393,053; cleveland (2.6%/yr): 2033 $42,932, 2042 $34,158, ten payments $383,967; jpm (2.5%/yr): 2033 $43,115, 2042 $34,523, ten payments $386,777; fed (2.0%/yr): 2033 $44,399, 2042 $37,151, ten payments $406,790; S1 (6.9%/yr): 2033 $31,388, 2042 $18,414, ten payments $226,341; S2 (0.6%/yr): 2033 $45,327, 2042 $45,534, ten payments $449,779; S3 (3.0%/yr): 2033 $39,271, 2042 $31,891, ten payments $354,671; S5 (-0.2%/yr): 2033 $65,530, 2042 $51,183, ten payments $606,527; S7 (6.9%/yr): 2033 $38,686, 2042 $18,424, ten payments $285,362.
History, every 15-year window 1872-2011 (140): ten-payment real total p5 $251,913, median $387,761, p95 $650,012; worst window starts 1973 ($226,341). H19 reproduced: $42,063 / $33,681 (reference $42,063 / $33,681), convention 2.5% a year, 7 and 16 years from 2026 (insight_v1 I4); sourced input: JPM 2026 LTCMA U.S. Inflation 2.50% (jpm_ltcma_2026_usd.csv).

## Flags for the reconciler (spec readings chosen here)

1. M7 S2: the spec writes the Japan rate change as `(jpn_ltrate ... )/100`, but `jpn_ltrate` is already in percent, so the literal reading gives a near-zero shift while S1 (10 Yr differences) is in percentage points. Headline S2 uses percentage points (gift $161,659, s1 -0.84pp); the literal reading is kept as row `S2_lit` (gift $163,194, s1 -0.0084pp).
2. M6 R6 `unfunded`: read as 'at least one of the ten payments paid below $50,000' (the spec: 'a payment is short when paid < 50,000'). Two alternates are reported next to it: share of payments short, and share of paths whose ten payments total under $500,000.
3. M6 R5 (CPPI): the gift rule uses bottom = certain31 = 0 as the spec's metric list says; the $150,000 promise is scored separately (`promised_150k_met_share`). `floor_broken_share` counts a negative cushion at any 1 Jan from 2028 on (at 1 Jan 2027 the floor exceeds the first deposit by construction, since the 2028 deposit is not counted).
4. M7 downgrade windows start at the close of the announcement day (all three were announced after the close); the prior-day reading is in `downgrade_events.csv` as `alt_prior_close_change_pp`.
5. M5 H1: the published 11 Oct 2010 row has every tenor blank and is dropped (noted in `M5_results.json`).

Disclosure: before this session's work the tail of `rab-ws/STATUS.md` and the primary's commit message (`git log`) were seen; they carry one-sentence headline figures. They were not used to write or tune any code here; the code was written from the specs and re-run unchanged except for the additions listed above (S2_lit, R6 alternates, this report).
