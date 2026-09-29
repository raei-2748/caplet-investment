# Decision memo: which fund holds the branch? (VT vs alternatives)

WS3, 2026-09-30 (Sydney). AI-generated analysis (Claude Code) for the team to ratify; no deliverable text.
**Triage label: note-in-Final-Report. Recommendation: keep VT (no change to the IPS or the Sheet).**

**Question.** The adopted plan puts the 2028 money left after the $150,000 floor (about $41,000 in Laura's plan,
`laura.stock_fund_2028_usd.strips`) into one world stock fund, VT, left alone until 2033. Would another fund do better?

**Options tested** (all bought 1 Jan 2028 and never traded): VTI + VXUS (62/38); U.S. only; VT + a small/value tilt
(70/30); VT + 10% gold + 10% REITs.

**Rule, written before any number was run** (`rab/models/M6_SPEC.md` s5): switch only if the bad-case gift (5th
percentile) rises by $2,000 or more, or the gift's spread narrows by 10% or more, in the J.P. Morgan Monte Carlo; the
same shows in history; the median gift is not cut; and the reason fits in one plain sentence and WInS can hold it.

**Evidence** (`rab/results/M6/fund_alternatives.csv`, `fund_choice_decision.csv`; MODEL):

| Fund | Bad-case gift vs VT (MC / history) | Spread vs VT (MC / history) | Median vs VT (MC / history) | Rule |
|---|---|---|---|---|
| VTI + VXUS | +$279 / +$190 | 0.98 / 0.98 | +$158 / +$363 | keep VT |
| U.S. only | -$61 / -$1,481 | 0.98 / 1.02 | -$204 / +$483 | keep VT |
| VT + small/value | -$78 / +$812 | 1.02 / 1.10 | +$102 / +$1,590 | keep VT |
| VT + gold/REIT | +$1,164 / +$1,388 | 0.899 / 0.80 | +$338 / -$737 | at the edge |

Gold/REIT meets the spread test only at the line (0.899 against 0.90), fails it on 3 of 20 other random seeds, and its
history lens flatters it (gold's price was fixed before 1971; the only long "REIT" series is home prices). With the
flattering proxies removed (one at a time or both) it still narrows the spread (0.80-0.91), with a bad-case gain of
$900-1,800. On real ETFs
(2012-2025) it gained nothing. The spec requires the same decision on any seed, so the switch is not robust.

**Choice: keep VT.** One sentence: "One fund that owns the world's stock market, left alone." The fund is about 9% of
Laura's money on 2 Jan 2028, so no alternative moves the gift by more than about $1,500 either way; each extra fund
is another $25 WInS trade and another thing to explain. GLD / VNQ listings on WInS are UNVERIFIED.

**What would change it.** A robust pass of the rule (all seeds) with a bad-case gain of $2,000 or more; or a reason to
hold no U.S. concentration risk that the team can say in one sentence. Neither applies now.
