# Branch fund: VT or an alternative?

WS3, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws3.md`). Keys: `rab/numbers_ws3.yaml`
(W), `rab/numbers.yaml` (N). Results: `rab/results/M6/fund_choice_decision.csv`, `fund_alternatives.csv`.

**Decision: keep VT.** No change to the IPS or the Sheet.

**Question.** Once the ten payments and the $150,000 floor are paid for, about $41,000 of Laura's 2028 money (N
`laura.stock_fund_2028_usd.strips`, about 9% of her deposits, W) goes into one world stock fund held to 2033. Would
another fund give a better bad case or a narrower spread for her 2033 gift?

**Options** (each bought 1 Jan 2028, never traded): VT; VTI + VXUS (62/38); U.S. only; VT + small/value tilt (70/30);
VT + 10% gold + 10% REITs.

**Rule, written before any number was run** (`rab/models/M6_SPEC.md` s5, s7). Switch only if: (1) the bad-case gift
rises by $2,000 or more, or its spread narrows by 10% or more (J.P. Morgan 2026 Monte Carlo, 200,000 paths); (2) history
agrees; (3) the median is not cut; (4) the reason fits one plain sentence and WInS can hold it; and (1) holds on every seed.

**Evidence** (W `ws3.fund.*`). Change against VT's gift. Bad case = MC 5th / history 10th percentile; history = today's
yields with the returns of 1928-2020. VT itself: bad case about $165,000, typical about $174,000 (MC).

| Alternative | Bad case, MC / history | Spread vs VT, MC / history | Median, MC / history | Rule gives |
|---|---|---|---|---|
| VTI + VXUS | +$279 / +$190 | 0.98 / 0.98 | +$158 / +$363 | keep VT |
| U.S. only | -$61 / -$1,481 | 0.98 / 1.02 | -$204 / +$483 | keep VT |
| Small/value tilt | -$78 / +$812 | 1.02 / 1.10 | +$102 / +$1,590 | keep VT |
| Gold + REITs | +$1,164 / +$1,388 | 0.899 / 0.80 | +$338 / -$737 | keep VT (not seed-robust) |

- No alternative moves the bad case by more than about $1,500 either way. The fund is small on purpose.
- Gold/REIT is the close call. With the seed noise removed its spread ratio is 0.8991 in both builds (100 seeds of
  200,000 paths each), 0.001 under the 0.90 bar. At the rule's 200,000 paths it passes on 80-85% of seeds (17 of 20 in
  the reference build, 14 of 20 in the blind build), so it fails the every-seed clause.
- It narrows the spread partly by trimming the good case: about half of the narrowing in the MC ($1,128 off the 95th
  percentile) and about two-thirds in history ($2,338 off the 90th), where it also leaves about $4,400 less total 2033
  money at the median (W `gold_reit_good_case`). A narrower range bought with Laura's upside is a weak reason to switch.
- Its history case is flattered: gold's price was fixed before 1971, and the only long "REIT" series is home prices.
  With those removed it still narrows the spread (0.80-0.91) and gains $873-1,801 in the bad case. On real ETF prices
  (10 windows, 2012-2025) its bad case was $110 lower and its median $581 lower.

**Decision.** Keep VT: "one fund that owns the world's stock market, left alone until 2033." Both builds apply the
pre-registered rule as written and both get KEEP VT. Beyond the rule, the kit's judgement is that about $1,200 of
bad-case gain (about 0.7% of the gift) is not worth two more holdings, two more $25 trades and two more things to
explain. GLD and VNQ on WInS: UNVERIFIED.

**Confidence.** High that the choice barely matters (both lenses, both builds). Medium that VT is strictly best:
gold/REIT sits on the line, and the MC has no fat tails and relies on JPM's gold and REIT correlations.

**What would change it.** (1) A pass on every seed with a bad-case gain of $2,000 or more. (2) VT not tradable in WInS on
the day, or over its 2x-volume limit: then VTI + VXUS, the same stocks in two funds. (3) A one-sentence reason, which the team
believes, to hold less than VT's U.S. weight. None applies now.

**Implications.**
- **IPS: none.** "A global index fund of thousands of companies held to 2033" already describes VT without naming it.
- **Final Report: note-in-Final-Report.** One line and this table: "We tested four alternatives against a rule written
  first; none moved the bad case by more than about $1,500; gold/REIT came closest."
- **Trading Notes:** VT stays the only stock trade: no VTI, VXUS, GLD or VNQ. The VT note can give the one-sentence
  reason. No fund-choice figure goes in a WInS note (none is in `numbers.yaml`). The TN Analysis VT pick ("supported")
  may mention the comparison in words only.
