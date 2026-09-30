# Rivals: why Root-and-Branch?

WS3, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws3.md`). Keys: `rab/numbers_ws3.yaml`
(W) `ws3.rivals.*`. Results: `rab/results/M6/rivals_summary.csv`, `M6_results.json`; card `rab/models/M6_CARD.md`.

**Question.** A judge will ask: why not 60/40, a glide path, CPPI, a TIPS ladder, or only Treasuries? Does the adopted
plan still win when every rival gets the same money, the same ten payments and the same 2031 rule?

**Options.** Eight rivals (`M6_SPEC.md` s3), two lenses: J.P. Morgan 2026 Monte Carlo (200,000 paths) and 149 start
years (1872-2020). "2033 money" = what is left for the facility and Laura once the payments are secured (MC 5th /
median / 95th percentile, $k). Every plan's payments are modelled as zero-coupon (STRIPS) Treasuries.

| Plan | A payment short, STRIPS basis (MC / history) | Certain in 2031 | 2033 money | Trades |
|---|---|---|---|---|
| **Root-and-Branch** | never / 0 of 149 | $150k | 181 / 207 / 252 | 13 |
| All-Treasury | never / 0 of 149 | about $202k | 191 / 202 / 213 | 12 |
| Ladder + 60/40 | never / 0 | nothing | 154 / 216 / 307 | 21 |
| CPPI, multiplier 3 | never / 0; misses the $150k in 2.0% | nothing | 153 / 199 / 408 | up to 72 |
| 60/40, whole portfolio | 1.3% / 2 of 149 | nothing | 53 / 245 / 527 | 24 |
| Glide path 65 to 20 | 0.17% / 3 of 149 | nothing | 88 / 233 / 434 | 24 |
| Growth-first 75 to 40 | 2.2% / 3 of 149 | nothing | 36 / 249 / 571 | 24 |
| TIPS ladder | 60% of paths / 92 of 140 | $150k | as Root-and-Branch | 13 |

**Evidence.**
- The case sets two hard tests: the payments "with a high degree of certainty", and a 2031 range that protects them.
  Only Root-and-Branch and All-Treasury pass both.
- Plans without dated holdings earn more in the middle but leave a payment short in some paths (up to $88k short from a
  1929 start) and can promise nothing in 2031.
- CPPI (buy after rises, sell after falls): fatter good case, lower middle, and the $150k is missed in 2.0% of paths
  (26% at multiplier 5). Root-and-Branch is CPPI with a multiplier of 1 and no trading.
- A TIPS ladder protects purchasing power Laura did not promise and risks the dollars she did (1.43 times the size,
  about $125k more, to pay every payment in 95% of paths).
- **All-Treasury, stated honestly.** About the same typical 2033 money ($202k against $207k), a better bad case (about
  $9,500 more at the 5th percentile) and a larger certain sum; Root-and-Branch trades that for about $38,000 more in a
  good case. In a 1929-style crash All-Treasury ends about $28,000 ahead ($205k against $177k, M7 S5). **For the
  facility alone it is better at every percentile** (gift $191k / $202k / $213k against $165k / $174k / $189k): it
  promises all its money, while Root-and-Branch promises the floor plus half the fund and leaves the other half (about
  $32,000 in the base case) with Laura.

**Decision: keep Root-and-Branch** (adopted, not reopened): the only plan tested that passes both hard tests and still
holds stocks with money no payment relies on. The case asks for "an appropriate balance between pursuing growth and
protecting the capital" and a strategy that "preserves appropriate financial flexibility when determining the facility
contribution". All-Treasury maximises the gift but gives up growth and leaves Laura nothing; the no-ladder plans put
the payments at risk for growth. Name All-Treasury as the closest rival.

**Confidence.** High on the two hard tests, STRIPS basis (history exact, MC agrees, both builds match). WS7 finds the
WInS book's coupon bonds deliver the full $500,000 only if coupons earn about 4.97% or more (W `ws3.external`, not
Gate-B checked); every plan holding the ladder shares this, so no ranking changes (see the stress memo). Medium on the
edge over All-Treasury: it rests on the equity premium (JPM world stocks 7.0% against today's 5.06% five-year yield;
lognormal returns, no fat tails).

**What would change it.** (1) Laura or the co-sponsors ranking a larger certain gift above growth and her flexibility:
All-Treasury. (2) Yields falling more than about 1 point before January 2027: the fund is used up and the two plans
become the same (Japan plus a fall: both $147k). (3) Payments that must keep their purchasing power: TIPS. None applies.

**Implications.**
- **IPS: none.** It already states the trade-off ("raises the expected outcome modestly but widens the range of
  results") and makes Laura's flexibility part of its second objective.
- **Final Report: note-in-Final-Report.** This table ("STRIPS basis" in the heading), the two hard tests first, the
  All-Treasury comparison including the facility-only line, and "Root-and-Branch is CPPI with a multiplier of 1". Have
  one sentence ready for "why not give the facility more with all Treasuries?"
- **Trading Notes:** no rival figure in a WInS note (none is in `numbers.yaml`). Contrasts in words are fine: a dated
  holding rather than a bond fund; stocks bought only with money no payment relies on.
