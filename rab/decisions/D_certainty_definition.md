# D5: what "a high degree of certainty" means, how it was tested, what it rests on

Completeness critic (WS7), 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet; the team decides and
writes every deliverable. Written because Gate D (`rab/redteam/triage.md` D5) found no memo that defines the case's
primary requirement, although pick 2's reflection publishes a definition on 22 Oct. It collects evidence the streams
already built; it adds no rule and does not change the strategy. MODEL, 28 Sep 2026 curve. Keys: `rab/numbers.yaml`
(N), `rab/numbers_ws3.yaml` (W3).

**Decision to ratify (by 20 Oct, before the Trading Notes draft; IPS by 6 Nov).** The one sentence that defines a
high degree of funding certainty. The case asks teams to *define* it, *explain how they evaluated* it and *identify
the assumptions* behind it (Client Profile p.3), and not to rely on outside funding for the ten payments.

**Options**

| Option | Verdict |
|---|---|
| A. As drafted: each payment "matched by a dated Treasury ETF or bond maturing just before it", so that "it depends essentially on the US government" | **Keep the idea, fix the words.** True for zero-coupon Treasuries (STRIPS) only. Under rule reading R1(a) (`rab/assumptions.md`) Laura buys the WInS-listed holdings: dated funds and coupon bonds. For those the U.S. government owes at least about $42,000 of each $50,000 in set coupons and principal (N `reinvest.rung.*` at 0%); the rest comes from reinvesting coupons. Two bonds end about 7.6 and 10.5 months early, not "just before". |
| B. A probability ("99 in 100 simulated paths pay every payment") | **Reject.** The model becomes the promise, and no model here simulates coupon reinvestment and stock returns together. Judges reward stated structure over false precision. |
| C. Structure plus a named cover | **Kit recommendation.** "Treasuries maturing before each payment, bought in January 2027 and held to maturity: the U.S. government owes most of each payment, the rest depends on reinvesting coupons, and a named part of the portfolio covers any shortfall before the facility gift." Same meaning as pick 2's certainty phrase (`rab/trades/notes.md` s6), plus the cover. |

**How it was evaluated: three tests**

1. **Cost against history** (Gate A, four pricers agree to the cent). The ten payments were priced on every daily
   Treasury curve since 2000 (about 6,700 days). Only at 2020-21 yields would part of one payment have been left
   unfunded, worst about $21,000 (N `history.unfunded_days`). On 28 Sep they cost about $289,000
   (N `laura.ladder.cost_today_strips`).
2. **Markets and rates** (Gate B, two blind builds; zero-coupon basis). With today's yields and history's returns, no
   payment is short in any of 149 start years, 1872-2020 (W3 `ws3.stress.today_yields_backtest`), nor in any of the
   13 stress episodes (W3 `ws3.stress.*`; `rab/results/M7/M7_results.json` shortfall 0 in all 13). A payment goes
   unfunded only if yields fall over 4 points before January 2027 (W3 `ws3.stress.thresholds_bp`).
3. **Coupons on the ladder Laura can buy** (Book L). Coupons reinvested at today's yields deliver about $503,000; at
   2%, about $466,000; at 0%, about $447,000 (N `reinvest.bookL_delivered`). The ten total $500,000 only if coupons earn
   about 5% or more (W3 `ws3.external.ws7_coupon_reinvestment`). That figure was single-build until today; the blind M1
   build now reproduces it to within two hundredths of a point (`rab/verification/blind_m1_2/breakeven_check.txt`), so
   quote "about 5%". Replaying 1962-2011 yield changes, some payment falls short in 387 of 593 start months, with the
   worst total about $458,000 (W3, same key; WS7 single build, UNVERIFIED). Keeping every payment whole at 2% costs
   about $20,000 more today (N `reinvest.bookL_buffer_cost`), more than the about $7,600 of room under $300,000
   (N `laura.ladder.headroom_2027_strips`).

**What "high" means, in figures the team can defend.** On the government's promise alone: at least about $42,000 of
every $50,000. With coupons reinvested near today's yields: every payment in full. The difference is the one
uncertainty left: about $30,000 in 2033 money if coupons earn only 2% for years (W3
`ws3.stress.coupon_gap_vs_laura_half`). The definition is honest only if it names who covers that.

**Assumptions it rests on** (the case's third ask)

1. The U.S. Treasury pays coupons and principal on time.
2. Every holding is held to maturity; nothing is sold to fund the facility gift.
3. Coupons are reinvested in Treasuries for the same payment (stress rule 2, `D_stress_bad_year.md`) at about 5%,
   or the named cover pays the difference.
4. Rule reading R1(a): Laura's real plan uses WInS-listed securities. Under reading (b), zero-coupon Treasuries remove
   assumption 3 (triage D15: one Contact Us question could settle it; the team decides whether to ask).
5. January 2027 yields are no more than about a quarter of a point below 28 Sep's; otherwise the 2028 deposit
   completes the earliest payments (N `laura.ladder.breakeven_fall_bp_strips`).
6. "The beginning of the year" is 1 January.

**Not decided here.** Who the named cover is: rule 3 as the memos stand (Laura's kept half first, then the gift above
the floor, then the floor) or triage D1's alternative (in January 2033, measure the coupon gap on that day's curve,
set that amount aside in the operating reserve and release the rest of her half). The team decides with D6 on 26 Oct.
Either way the chain ends inside the portfolio: never "her own money" (the case forbids relying on outside funding).
The operating reserve's size in January 2033 is then the ten holdings' value plus that measured amount; its dollar
figure belongs in the Final Report.

**What would change it.** Wharton answers the R1 question and STRIPS are allowed: the definition becomes "owed in full
by the U.S. government". A low-coupon swap on Friday (SW40/SW41) raises the owed share on one rung only. Yields fall
more than about a quarter of a point before January 2027: the 2028 deposit tops up, and less is left for the facility.

**Where it goes.** IPS: a word-neutral replacement of the sentence "By high certainty we mean..."
(`rab/decisions/D_ips_edit_ledger.md` L1). Pick 2 reflection: the certainty phrase, once. Final Report: the three
tests, the per-rung table (N `reinvest.rung.*`, appendix only) and the cover.
