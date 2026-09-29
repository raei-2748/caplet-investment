# D6 memo: how much of the stock fund Laura promises in 2031

WS2, 30 Sep 2026 (Sydney). AI-generated analysis (Claude Code) for Team Caplet; the team decides and writes every
deliverable. Nothing here is applied to the IPS or the Sheet. Evidence: M3, M4 and M8 (`rab/models/*_CARD.md`,
`rab/results/`). All dollar figures are **Laura's plan**, MODEL, on the 28 Sep 2026 curve, rounded. None of them may
go in a Trading Note, and none is in `rab/numbers.yaml` yet (proposed: `rab/results/M3/numbers_proposed.yaml`).

**Decision to ratify (Mon 26 Oct):** keep "half". **Triage: ignore** (no IPS change needed). Three related items in
section 4 are **fix-before-6-Nov** (IPS wording only; the team's call).

## 1. What was tested

The share s of the stock fund's 2031 value added to the floor to make the top of the range (and the cap on the gift).
It was tested under three return models (fat tails; Shiller history 1871-2025; Bayesian with an uncertain centre),
200,000 paths each. The floor may pay slightly less than $150,000 because its income has to be reinvested. The decision
rule was **written and committed before any result existed** (`M4_SPEC.md` section 5, commit 3d98ce0):
1. the gift must stay above the announced low end in 99.5% of paths;
2. Laura must keep at least 10% of her gift in 95% of paths (about three years of Taiwan building-cost rises);
3. take the largest share that passes in all three models;
4. change "half" only if that share falls outside 0.40-0.60.

## 2. Result

- The largest passing share is **0.47-0.50** (0.50 fat tails, 0.47 history, 0.47 Bayesian). That is inside 0.40-0.60,
  so the rule **keeps half**.
- In plain words: half is about the most Laura can promise and still keep a tenth of her gift aside in 19 of 20
  outcomes. At half she keeps about $33,000 in a typical case and at least about $15,000 in a bad (1-in-20) case.
- The share does **not** change the chance of letting co-sponsors down. Whatever the share, the gift reaches the top
  about 3 times in 4, and lands below the middle of the range at most about 1 time in 200 (history model). The share
  decides only who gets the upside, the building or Laura's reserve, dollar for dollar in expectation.
- **What would change it:** the size of the reserve Laura wants. If a 5% reserve is enough, the rule gives about 2/3.
  If she wants 15%, it gives about 1/5 (largest passing share 0.23; PR-7 rounds down to 0.20). The stock model hardly matters (`rule_sensitivity.csv`).

## 3. Confidence statement for the IPS method (PM-25)

The 2033 gift lands inside the 2031 range. This is **certain by construction if** the floor holdings pay, the 2028
deposit arrives, the gift is capped, and no fee is taken from the floor. In 1.6 million model paths no gift fell
outside its range. The models add only where it lands: at the top about 3 in 4 times, and in the upper half about
99 in 100 times (all three models).

## 4. Other findings, with triage

| # | Finding | Evidence | Triage |
|---|---|---|---|
| 1 | **Announce the floor rounded down, to $145,000.** In Laura's real plan (strict FAQ reading), the floor is a coupon Treasury or an iBond fund whose income must be reinvested. It pays about $149,000 in a typical case and about $146,000 at worst, and falls short of $150,000 in about 2 of 3 cases. The gift itself stays at or above $150,000 in every path of the fat-tail and Bayesian models and in all but a handful (3 to 5) of 200,000 history paths, because half the fund covers the shortfall. Only the claim "already owned" needs the round-down. | M4 `floor_delivery.csv`, `fig_M4_floor.png` | **fix-before-6-Nov**, optional wording in the IPS range method ("the floor she owns, rounded down to the nearest $5,000") |
| 2 | **Name the three assumptions that move the range**: yields on 1 Jan 2027 (the ladder purchase), the 5-year yield in Jan 2028 (the floor's price), and costs paid from the stock fund. January-2027 yields alone explain about 90% of the variation in the typical top. The stock-return assumption moves it by under $3k. | M8 `must_state.csv`, `fig_M8_tornado.png` | **fix-before-6-Nov** (the case requires the assumptions to be stated; IPS assumptions paragraph) |
| 3 | **Floor wording (F4):** "the whole remainder" and "keep $150,000" differ only if yields fall before January 2027. After a 0.5-point (50bp) fall they give a floor of $143k with a $29k fund against $150k with a $23k fund. | M8 `floor_reading.csv` | **fix-before-6-Nov** (already flagged; the team picks one reading) |
| 4 | Option for the 2031 wording: announce both ends from the rounded-down floor ($145k to $145k + half the fund). The top is then reached 9 times in 10 instead of 3 in 4, with a gift about $3,500 lower on average. Exploratory, not pre-registered. | M4 `run_log.txt` | **note-in-Final-Report** |
| 5 | A narrower range is possible but no longer "owned". Raising the low end to about $160k breaks the promise in up to about 40 of 10,000 history paths, and to $165k in up to about 2%. The owned floor keeps the bottom free of any model. | M4 `narrower_range.csv`, `fig_M4_narrower.png` | **note-in-Final-Report** (why the bottom is the floor) |
| 6 | The return model barely matters: the typical 2031 top is about $175k in every model (90% of paths $165k-$190k), because only about 9% of Laura's money is in stocks and half of that is promised. | M3 `summary.csv`, `fig_M3_top2031.png` | **note-in-Final-Report** |

## 5. What would make this memo wrong

- Laura needs a much larger or much smaller reserve than a tenth of her gift. Ask her (or state the team's reading).
- Fees much higher than 1% a year, or charged to the floor.
- Yields fall sharply before 1 Jan 2027. The range then starts from a smaller floor and fund; the share question is
  unchanged.
- A model with stocks and yields falling together would widen the bad cases a little. It is not built here (WS3/M7).

## 6. Gate B (30 Sep 2026)

A blind rebuild of M3, M4 and M8 from their specs reaches the same decision: robust share 0.47, keep half, announce
$145,000, and the same three assumptions to state. Every figure in this memo agrees within tolerance
(`rab/gates/gate_B_ws2.md`). Four wording fixes were made here: 15% reserve -> about 1/5 (was 1/4); "all but 5"
-> "a handful (3 to 5)"; the announced-basis gift is about $3,500 lower (was $3,000); and about 40 (was 42) in
10,000 at a $160k low end.
