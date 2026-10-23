# M6 model card: rivals on the same metrics, and the branch-fund choice

WS3, 2026-09-30. AI-generated research (Claude Code) for Team Caplet. MODEL outputs, not forecasts. Spec `M6_SPEC.md`
(switch rule written before any number was run); code `m6_rivals.py` (seed 20260930, 200,000 paths, 8 s);
outputs `rab/results/M6/`.

**What it does.** Gives every rival the same money ($300,000 in 2027, $150,000 in 2028) and the same job (ten $50,000
payments from 2033), then scores all of them on the same yardsticks: are the payments ever short, how much is left for
the facility and flexibility in 2033 (after the payments), and how much can be promised with certainty in 2031. Two
lenses: 149 historical start years (each era's yields and returns) and a Monte Carlo on J.P. Morgan's 2026 assumptions
(stocks 7.0% a year; Treasury fund reset to today's 5.06% five-year yield).

## Rivals (2033 money after the payments; $k)

| Plan | Payments short (MC / history) | MC 5th / 50th / 95th | History 10th / median / 90th | Certain in 2031 | Trades |
|---|---|---|---|---|---|
| **Root-and-Branch (adopted)** | never / 0 of 149 | 181 / 207 / 252 | 67 / 132 / 363 | $150k | 13 |
| All-Treasury | never / 0 | 191 / 202 / 213 | 67 / 132 / 304 | ~$202k | 12 |
| Ladder + 60/40 growth money | never / 0 | 154 / 216 / 307 | 79 / 145 / 372 | 0 | 21 |
| 60/40 whole portfolio | 1.3% / 2 | 53 / 245 / 527 | 83 / 222 / 527 | 0 | 24 |
| Glide path 65 -> 20 | 0.2% / 3 | 88 / 233 / 434 | 82 / 180 / 440 | 0 | 24 |
| Growth-first 75 -> 40 | 2.2% / 3 | 36 / 249 / 571 | 88 / 240 / 558 | 0 | 24 |
| CPPI, multiplier 3 | never / 0 ($150k missed in 2.0% / 94 of 149*) | 153 / 199 / 408 | 66 / 131 / 512 | 0 | up to 72 |
| CPPI, multiplier 5 | 0.01% / 0 ($150k missed in 26% / 106 of 149*) | 124 / 176 / 578 | 66 / 128 / 578 | 0 | up to 72 |
| TIPS ladder + same branch | a payment short in 60% of paths / 92 of 140 inflation paths | as adopted | as adopted | $150k | 13 |

\* History lens: at the lower yields of most past eras, even Root-and-Branch's floor came out below $150k in 91 of 149
start years (M5), so history cannot tell the two apart on this point; the Monte Carlo lens (today's yields) can. Gate B
(`rab/gates/gate_B_ws3.md`) corrected the history counts, which read "1" because of a counting bug in the summary.

insight_v1 H16 re-verified on this basis: growth-first misses a payment in 2.2% / 10.6% / 35.1% of paths with a 2028
deposit of $150k / $75k / $0 (was 3.2 / 13.7 / 40.8% on the old engine). Root-and-Branch: 0% in all three, because the
first deposit already buys the ladder. A TIPS ladder would need to be 1.43 times as big (about $125k more) to pay every
payment in full in 95% of inflation paths.

## Branch fund (pre-registered rule, M6_SPEC s5)

Alternatives to VT, all bought 1 Jan 2028 with the same $40,736 and never traded. None moves the bad-case 2033 gift by more
than about $1,400 (MC 5th percentile for VT: $165k; history 10th percentile: $169k); U.S.-only lowers it by about $1,500 in history. VTI+VXUS, U.S.-only and a small/value tilt pass no test.
VT + 10% gold + 10% REIT passes the number tests only at the edge (gift spread 0.899 of VT's against a 0.90 bar;
passes on 17 of 20 other seeds; history spread 0.80-0.91 even after removing its flattering proxies; median -$0.7k to
+$0.3k; real ETFs 2012-2025: no gain). Under the spec's own tolerance (same decision on any seed) the switch is not
robust: **VT stays**. Memo: `rab/decisions/D_fund_choice.md`. Gate B: with the seed noise removed (100 seeds x 200,000
paths, both builds' samplers) the ratio is 0.899, just 0.001 under the bar. So "not robust" means "on the line", not
"fails": with 200,000 paths the test passes on about 4 seeds in 5.

## What this teaches (plain English)

Plans that skip the ladder earn more in the middle but can leave a payment short, and they cannot promise anything in
2031. All-Treasury is certain but gives up the upside. Root-and-Branch keeps the certainty of the all-Treasury plan for
the payments and the $150,000 bottom and still keeps most of the upside. It is CPPI with a multiplier of 1 and no
trading: a bigger multiplier buys a fatter good case, a lower middle case (volatility drag) and a floor that can break.
A TIPS ladder protects purchasing power Laura did not promise, and puts at risk the dollars she did promise.

## Assumptions and limits

MC: i.i.d. lognormal annual returns fitted to JPM (compound and arithmetic returns reproduced), JPM correlations (the
9-asset block needed a tiny positive-definite fix), no fat tails (WS2's M3 has them); rates move only through the bond
fund (duration 5); REC's ladder price for 2027 is fixed (pre-2027 rate risk is WS4's M2). History: M5's data and limits;
the "REIT" is a home-price index before 2009; gold was fixed-price before 1971. The 2031 gift rule applied to rivals
is the adopted rule, not how those rivals would announce. No fees or taxes. The TIPS cost equals the nominal ladder's.

**Failure modes.** Reading the history median ($132k) as today's outlook (see M5); comparing gifts across rivals
instead of payments-short and certain-in-2031, which is what the case asks for; treating a result at the threshold as a
decision.

## Triage (nothing applied to the IPS)

| Finding | Class |
|---|---|
| Every no-ladder rival leaves a payment short in some paths and histories; Root-and-Branch never does | note-in-Final-Report (evidence for the design) |
| CPPI and TIPS ladders fail the case's "high degree of certainty" test in plain numbers | note-in-Final-Report |
| Fund: VT stays; gold/REIT is at the edge and not robust | note-in-Final-Report ("we tested four alternatives") |
| H16 superseded by 2.2% / 10.6% / 35.1% | note for WS1 (proposed numbers) |
