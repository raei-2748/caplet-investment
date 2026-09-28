# Fairness audit of the six firm summaries (firm_A.md ... firm_F.md)

Serves: IPS (a fair comparison before the team picks the strategy the IPS freezes on Nov 6).
Relayed user message during this task: "just cut off the unncessary bits." Applied: every file was trimmed, and filler
shared by several firms was removed evenly. No scope change.
Originals backed up outside the repo (scratchpad `tournament_orig/`).

## Summary
- All six now have the same 7 section headings in the same order and exactly 3 risk bullets each.
- Word counts after the edits (Python `len(text.split())`, headings included): A 368, B 359, C 365, D 378, E 354,
  F 375. All are within 300-380. Before the edits: A 368, B 372, C 373, D 378 (428 after the first rewrite), E 379, F 376.
- Numbers checked against brief sections 6 and 14, re-running `research/insight_v1/scripts/E7_tournament_field_numbers.py`
  (A, B, C, E, F) and against `phase_E/E6_final_spec.md` / `ips_spec.md` R1-R5 (D). A, B, C and E matched exactly.
  One unsupported number was found and corrected (F's 97.5%, see F below). Every model output now carries a
  "model estimate" label.

## Edits common to several firms
1. A, B, C, E, F: removed "Reserve bonds are held to maturity." from section 5. It was filler that said the same thing in every file.
2. A, B, C, E, F: added "(model estimate)" to the "$16k per one-point rate fall" risk line. Rechecked: flat 5.26% ->
   4.26% annuity-due of ten $50k adds $16,089, the same flat-curve method as strategy_mc.py.
3. A, C, F (which buy the reserve in stages): "A one-point rate fall by 2033 adds about $16k" became "A one-point
   rate fall before the staged purchases adds up to about $16k". The original overstated their rate risk, because
   buying in stages locks in part of the cost earlier. B and E buy in 2033, so their wording is unchanged.

## Firm-by-firm edits
**A**: "safe bucket" / "growth bucket" -> "Treasury bucket" / "stock bucket" ("safe" is a loaded word).
**B**: removed the quoted case line "has been willing to take thoughtful risks". It was the only direct quote in any
file, which made B stand out. It is replaced by a neutral paraphrase ("The case describes her as willing to take risks"),
and the reason now gives JPM's numbers (6.7% vs 4.0%), so the argument stays at full strength. Removed the "95th
percentile $540k" (section 3) and the "5th percentile $20k" risk bullet. No other firm gives tail percentiles of the
money left over, and they gave B one number that makes it look better and one that makes it look worse. The
"money left over" figures are now equally specific: every firm gives only the median.
**C**: reordered section 1 so the glide path comes first, as in A, B, E and F, and added "the rest is intermediate
U.S. Treasuries". Added "a one-point uncertainty in 2033 interest rates" to the check description: it is true of the
engine (strategy_mc.py rate_sd = 0.010), and A, B and E already said it. Removed the duplicated modelling caveat
(it is kept in the risk bullet) and the phrase "They carry a values narrative alongside the core" (a sales line, not a
mechanism).
**D**: "The payments are bought, not forecast" (the council's own slogan) -> a plain definition in the same "High
certainty means ..." form as the other firms. "building minimum" (a term the project invented) -> "minimum
facility contribution". "gift" -> "contribution" / "to the facility", the terms the other firms use. Removed "U.S. stocks'
two-year return was non-negative in 84% of periods since 1928": no other firm cites history, so it was extra evidence
only D had. Added "Model estimate: median money left after the reserve is $207k" to section 3, so D has the same
number as the others (E6 total p50 $207k). Section 5: 5th/50th/95th percentile figures -> median only ($174k / $32k), as
for the other firms. Section 6: added the trade count and commissions ($25 per ETF, $10 per Treasury note), as every
other firm has. Dropped "(duration-matched)" and "about 1%" (cash is exactly 1%: 23.5 + 42.5 + 24.3 + 8.7 = 99). Risks:
dropped "A fixed $50,000 buys less each year in Taiwan". It applies equally to all six plans, and only D disclosed
it. The vague ladder-cost bullet was replaced with the model's joint-tail amounts ($12k at -50bp, $31k at -100bp,
from E6 R2) so that it has numbers like the other firms' miss rates. Kept: $294,387 (the real 15-November ladder,
E6 R1, VRF inputs; it is higher than the brief's $292,264 because the bonds mature about 6 weeks early), "about 1 in 3"
(MODEL 30-34%), $118k, ~$40k, 7.5%, $175k, 73%, $250k.
**E**: removed "balanced" and "conservative" (loaded words), leaving a neutral description of the range. Removed the
fourth risk bullet ("A low range may lead co-sponsors...") so that E has 3 bullets like the rest. Section 4 already
states the 50% chance of exceeding the top.
**F**: CORRECTED A NUMBER. "funded in 97.5% of paths" (regime-switching model) had no source: no script or file
computes a regime-switching result. The engine used for all five model firms gives 99.7% funded (0.3% miss) and
93.1% at a $75k deposit (E7 output). F now reports those figures and the same method sentence as A, B, C and E. The
regime-model claim and its risk bullet ("Results depend on the regime model's parameters") were removed. The base
miss rate (0.3%) was added to F's first risk bullet, which A, B, C and E already had. Jargon defined or removed:
"mean-variance optimiser" -> "an optimiser (a formula that picks weights from expected returns, volatilities and
correlations)"; "CVaR limit" -> "loss limit"; "dynamic risk parity" -> "bond funds are weighted so each adds equal
risk". Section 4: dropped the 25th and 75th percentiles so that F gives low / high / median like the other firms. Section 6:
added "The 2027 allocation:" to match.

## Checks that passed with no edit
Glide-path averages (A 44.2%, B 66.7%, C 52.5%, E 50.8%, F 38.3%); WInS weights sum to 100% and the stock shares match
each 2027 glide weight; trade counts match the number of funds; miss rates, funded rates and medians match the E7 run
(seed 20260927, 200k paths); ranges match the E7 gift percentiles (A $75k/$302k/$175k; B $118k/$304k/$203k;
C $65k/$335k/$182k; E $66k/$170k; F $59k/$317k/$171k); $395k reserve = brief s14 $394,930; JPM 6.7%/4.0% = brief s6.

## Known modelling differences NOT fixed (these are content, not presentation; flagged for whoever reads the results)
- The engine prices the 2033 reserve at a flat 5.26% (~$401k), not the ~$395k implied by forward rates (brief s11).
  This slightly overstates the miss rates of A, B, C, E and F. D buys its bonds directly and is not affected.
- The engine models A, C, E and F as plain stock/Treasury glide paths. C's themes, F's tilts and optimiser, E's bond
  fund (treated as Treasuries), and the staged purchases of A, C and F are not modelled. C and F state this in
  their risk bullets. E's and A's model numbers ignore it.
- D's numbers come from a different script (E6_final_checks.py). The same seed and JPM inputs are used, but the
  ladder is bought in 2027 rather than simulated to 2033.
- Stocks in every model are U.S. large cap only (JPM 6.7%/16.47%), including the international funds.

## What this teaches
A fair comparison checks presentation as well as numbers. A quote, a slogan, an extra statistic or a single adjective
can make one option look stronger before anyone reads the numbers. Keeping the structure, the level of numerical
detail and the labels the same lets a reader judge the ideas themselves.
