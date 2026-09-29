# M7 model card: stress tests and the real value of the $50,000 payments

WS3, 2026-09-30. AI-generated research (Claude Code) for Team Caplet. MODEL outputs (past episodes replayed through the
adopted rules on today's curve), not forecasts. Spec `M7_SPEC.md`; code `m7_stress.py` (deterministic, 2 s); outputs
`rab/results/M7/`.

**What it does.** Moves today's Treasury curve (28 Sep 2026) up or down the way yields moved in a past episode, runs
that episode's stock returns through the world fund, and follows the adopted rules: ladder bought on 1 Jan 2027
longest-first, the 2028 deposit finishes it if needed, then buys the $150,000 floor, the rest goes into VT, the 2031
range is floor to floor + half the fund, the gift is capped. It also prices the ten payments in purchasing power.

## Stress table (Laura's plan; $k; base = JPM 7% stocks, market inflation)

| Scenario | Ladder 2027 | Floor | 2031 range | 2033 gift | Gift in 2027 dollars | Payments |
|---|---|---|---|---|---|---|
| Base | 292 | 150 | 150-175 | 175 | 152 | all paid |
| 1970s stagflation (1973-78) | 292 | 150 | 150-175 | 175 | 110 | all paid |
| Great Inflation (1966-71) | 292 | 150 | 150-179 | 179 | 138 | all paid |
| Japan's lost decade (1990-95) | 292 | 150 | 150-163 | 162 | 147 | all paid |
| Japan, and rates fall 1 point before Jan 2027 | 323 (top-up 24) | 147 | 147 | 147 | 133 | all paid |
| 2022 happens in 2028 | 292 | 150 | 150-169 | 169 | 133 | all paid |
| 2022 happens in 2027 | 292 | 150 | 150-182 | 182 | 143 | all paid |
| Great Depression (1928-33) | 292 | 150 | 150-159 | 159 | 209 | all paid |
| 2008 happens in 2028 | 292 | 150 | 150-164 | 164 | 143 | all paid |
| S&P downgrade, 2011-style (yields -56bp before purchase) | 309 (top-up 9) | 150 | 150-162 | 162 | 141 | all paid |
| Fitch 2023-style (+7bp) / Moody's 2025-style (+3bp) | 290 / 292 | 150 | 150-176 | 176 | 154 / 153 | all paid |
| Downgrade + buyers' strike (hypothetical: +1 point, stocks -20% in 2028) | 265 | 150 | 150-184 | 184 | 160 | all paid |

**Thresholds** (a parallel fall before 1 Jan 2027 that is still there in Jan 2028): a top-up is needed beyond 26.2bp
(= `laura.ladder.breakeven_fall_bp_strips`); the stock fund is used up but the floor is still $150,000 up to 109bp; a
payment would go unfunded only beyond 428bp. Downgrade moves are measured: 10-year yield change over the 20 trading
days after each announcement (FRED DGS10): 2011 -56bp, 2023 +7bp, 2025 +3bp.

## Real value of the payments (1 Jan 2027 dollars)

| Inflation path | 2033 payment | 2042 payment | All ten |
|---|---|---|---|
| Market breakeven 2.34% (FRED T10YIE, 28 Sep 2026) | $44k | $35k | $393k |
| JPM 2026 LTCMA 2.50% / Cleveland Fed 2.57% / Fed target 2.00% | $43k / $43k / $44k | $35k / $34k / $37k | $387k / $384k / $407k |
| 1970s (1973-87 CPI) / Great Inflation (1966-80) | $31k / $39k | $18k / $18k | $226k / $285k |
| Japan (1990-2004) / Great Depression (1928-42) | $45k / $66k | $46k / $51k | $450k / $607k |
| U.S. history, 140 windows since 1872 (5th / median / 95th) | | $19k / $34k / $72k | $252k / $388k / $650k |

insight_v1 H19 ($42,063 in 2033, $33,681 in 2042, in 2026 dollars at 2.5%) reproduced exactly; the 2.5% is now sourced
(JPM 2026 LTCMA U.S. inflation 2.50%).

## What this teaches (plain English)

Nothing in these scenarios stops a payment: the ladder is bought first and held to maturity, so later price swings,
crashes and downgrades change only what the Treasuries would sell for, never what they pay. The episodes change the
gift by at most about $28,000 (Japan with an early rate fall), and never below the floor once it is bought. The danger
is before the money arrives: a 2011-style flight to safety (-56bp) would push the ladder above $300,000 and trim the
stock fund. The one risk the plan leaves with Laura is inflation: at today's market expectation the last $50,000
payment buys about what $35,000 buys in 2027; in a 1970s-style decade, about $18,000.

## Assumptions and limits

Parallel shifts only (no twists); analog stock returns are annual and in each market's own currency (Japan in yen, as
if the world fund behaved like Japan's market); the fall before 2027 in S2b is an assumption, not an episode. Floor
priced with the E6 convention (5-year par, annual compounding). Bond-fund returns for the context rivals are derived
from the yield path (duration 5). A U.S. payment delay (debt-ceiling "X-date") is not modelled; STRIPS maturing 15 Nov
leave 47 days before each 1 Jan payment (the WInS iBond ETFs hold cash until about 15 Dec: UNVERIFIED for delays).

**Failure modes.** Reading the Great Depression's real gift ($209k) as good news (deflation made cash dear); forgetting
that the 2031 range is announced after the floor is bought, so its bottom is certain then, not now.

## Triage (nothing applied to the IPS)

| Finding | Class |
|---|---|
| Inflation is the risk the plan leaves with Laura (payments fixed in dollars, as the case requires). If the IPS has no sentence saying so, add one | fix-before-6-Nov (wording only, if absent); else note-in-Final-Report |
| A 2011-style flight to safety before 1 Jan 2027 costs about $20k of stock fund but no payment; WS4 owns the pre-2027 hedge memo | note-in-Final-Report |
| The $150,000 bottom holds for falls up to about 1 point before the money arrives | note-in-Final-Report (supports the "certain by construction if..." wording, PM safeguard) |

**Gate B (30 Sep 2026).** A blind rebuild from `M7_SPEC.md` reproduces every scenario, threshold, downgrade move and real value to the cent. The spec erratum for S2 (`/100` on `jpn_ltrate`) is logged in the spec changelog; both builds used percentage points. Record: `rab/gates/gate_B_ws3.md`.
