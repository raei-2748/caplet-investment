# AX1 audit: rates and quant (D3 model v2 and the nine D3 answers)

Agent AX1 (cluster auditor, rates and quant), insight_v1 run, 2026-09-28. This is an adversarial check of
`research/insight_v1/phase_D/D3_quant.md` and `research/insight_v1/phase_D/D3_model_v2_results.md` before they reach the
strategy team. It is AI-generated research (findings, numbers, checklists), **not text to submit**. The six students
decide and write every word, and record this AI use in the Final Report's Works Cited (Wharton AI policy).

- **Scope:** brief section 17, Trading Notes (TN, Oct 23) and IPS (Nov 6) only.
- **Relayed messages:** none arrived during this audit.

**What this task delivers**
- This file.
- An "## Audit corrections (AX1)" section at the end of each D3 file: `D3_quant.md` has C1-C25 and
  `D3_model_v2_results.md` has V1-V10. D3's own text is unchanged.
- One check script: `.venv/bin/python research/insight_v1/scripts/AX1_quant_audit.py`. It takes about 15 seconds, imports
  D3's model code unchanged, and reproduces every number AX1 adds, in sections [1]-[9].

Nothing was committed.

**Status labels** (brief section 3):
- VP = VERIFIED-PRIMARY.
- VRF = VERIFIED-REPO-FILE.
- MODEL = an ASSUMPTION-based model output, not a forecast.
- ASSUMPTION = a modelling choice.
- INTERPRETATION = our reading, not a fact.

**Terms used:**
- **Sleeve / growth money:** the money outside the ten-payment ladder.
- **Floor:** the part of the sleeve moved into a 2-year Treasury in 2031.
- **p5/p50/p95:** 5 in 100 simulated futures end below p5. p50 is the median, the middle outcome.
- **Mean:** the average over all futures. It is what "expected" means.
- **All-Treasury benchmark:** D3's "riskless control". The surplus is locked in Treasuries maturing in 2033 instead of
  being invested.
- **Barbell:** lock part of the growth money in January 2028 and put the rest 100% in stocks.
- **Cap:** a rule that Laura never gives more than the announced top of the range.

---

## Verdict (short)

**D3 passes with corrections: 0 blocking, 8 distinct important issues (10 entries across the two files), 25 minor.**

**What holds:**
- **Arithmetic:** all 10 D3 scripts reproduce every quoted number exactly. The v2 model matches the verified model path
  by path (largest difference $0.54).
- **Sources:** every source AX1 re-opened says what D3 quotes.
- **Decisions that survive:**
  - lock all ten payments (M243);
  - the contingency clause: longest-dated payments first, and the 2028 deposit's first use completes the ladder (M053);
  - one dated floor lock in 2031, with no ratchet (M055; kept on simplicity grounds);
  - lock share 80-90% (M060);
  - judge the stocks against an all-Treasury benchmark, not a stock index (M034).

**What changes:**
1. The recommended 2031/2033 contribution rule ("give 90%, capped") promises less than is bought. D3's own table has a
   rule with the same money and flexibility that announces a bottom about $17k higher.
2. "100% within the range" is a rule, not a test result.
3. "Stocks buy range, not a bigger expected facility" confuses median and mean. The expected gain under JPM is about
   $7-9k, not $3k.
4. The "riskless control" is not riskless seen from today.
5. The barbell is **not** dominated. When the floor is bought (2028 or 2031) is a genuine team choice.
6. "Demonstrably tracks" overstates a model backtest.
7. "All ten payments bought in January 2027: robust" contradicts D3's own 1-in-3 finding.
8. Much of D3 is Final Report material, which brief s17 moves to the later list.

---

## 1. Scripts re-run (2026-09-28, from the repo root)

| Script | Result |
|---|---|
| `strategy_mc_v2.py` | Reproduces sections 2-4 exactly: the reproduction check, central case $152k/$204k/$277k, the tornado rows, (a)-(g). Path-by-path match with `research/verified_2026-09-27/strategy_mc.py`: lock-early $0.54 max difference, growth-first $0.00 (AX1 [1]) |
| `D3_control_and_equity.py` | All M034 tables and the 13.6/17.0/20.4/23.8% whole-portfolio equity shares reproduce |
| `D3_lock_frontier.py` | All M243 cells reproduce (e.g. deposit missing: 95/90/80/70% locks short 2.34/12.75/25.78/31.57%) |
| `D3_range_rules.py` | All M039/M060 tables reproduce (floor share 50-100%; bad/middle/good 2031 announcements; P(within) 61.9-92.6%) |
| `D3_barbell.py` | All M238 rows reproduce, including history (plan worst $105k; barbell 80% $176k) |
| `D3_joint_tail.py` | The conditional-dollar table, probabilities (30.2%; 8.2%; 30.17%; 44.4%/69.0%), rule check and Damodaran/FRED evidence all reproduce |
| `D3_ratchet.py` | Reproduces the premise (-22%), the designs and the dominance test (42% equity: $169k/$204k/$250k; step-down = 51%) |
| `D3_history_stress.py` | Crash frequencies (0.29% / 1.16% / 3.1%), named episodes and window tables reproduce |
| `D3_funded_status_log.py --backtest` and `--date 09/25/2026 --since 09/01/2026` | ±$827 / 0.42%; payments' value -5.5% vs hedge -4.7%; $288,924, 10.16y, $293/bp; funded ratio 1.019; since 1 Sep -3.18% vs -2.85% (+$648) |
| `D3_data_snapshot.py --offline` | Re-parses: Damodaran 98 years to 2025; 185 curve dates; FRED DGS2/5/10 to 2026-09-24 |
| `AX1_quant_audit.py` (new) | [1] path match; [2] mean vs median equity lift; [3] benchmark range; [4] barbell vs the plan's equity frontier; [5] 2026 days the ladder fit under $300k; [6] FRED 98-day fall base rates and the 2008 worst case; [7] gap in cost vs face dollars; [8] contribution rules at equal flexibility; [9] unbought face by buying order |

---

## 2. Sources re-opened (the claims that matter most for decisions)

| # | Claim in D3 | Re-opened | Result |
|---|---|---|---|
| 1 | Par curve 2026-09-25: 2y 4.81, 5y 4.98, 10y 5.17, 20y 5.54 | treasury.gov 2026 CSV, curl 2026-09-28 | **Confirmed** (VP). The live 09/25/2026 row equals `competition/official_market_data/daily-treasury-rates_2026-09.csv` (VRF). No newer curve yet |
| 2 | 10y rate vol 70.6bp a year in 2026; 0.48pp sd of 98-day moves since 1990 | FRED DGS10 snapshot, recomputed; live spot checks (2008-12-31 2.25; 2026-09-24 5.18) | **Confirmed** (VP inputs, derived): 70.58bp; 0.477pp |
| 3 | 10y yield: 2002 -124bp, 2008 -179bp (4.04 → 2.25), 2020 -99bp, 2022 +236bp | FRED DGS10 | **Confirmed** (VP, derived) |
| 4 | USD/TWD 31.82 (2026-09-18); two-year sd 6.8% since 2006 | FRED DEXTAUS, curl 2026-09-28, recomputed | **Confirmed**: 31.82; 6.74% since 2006, 9.41% since 1983 (VP, derived; F-513) |
| 5 | Damodaran histretSP "page dated January 2026"; 2008 S&P -36.55%, 10y bond +20.10%; 2022 -18.04% / -17.83% | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html, fetch helper 2026-09-28 | **Confirmed** (VP, dataset page). The page title still reads "1928-2024", but rows run to 2025 (2025 S&P +17.78%). The snapshot equals the live rows |
| 6 | Vanguard U.S. equities "declined from a range of 4.9%–6.9% to a range of 4.2%–6.2%" (run of 30 June 2026) | https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html, `--grep`, 2026-09-28 | **Verbatim** (VP). New context: developed ex-U.S. "4.5%-6.5%", emerging markets "2%–4%". So a VT-weighted Vanguard midpoint is about 5.1% (D2's blend: 5.08%). D3's 5.2% U.S. figure is slightly generous for a world fund |
| 7 | "the VCMM may be underestimating extreme negative scenarios unobserved in the historical period" | same page, `--grep` | **Verbatim** (VP) |
| 8 | Brunel goal-probability table: Needs 90-95, Wants 80-85, Wishes 65-75, Dreams 50-60 | https://srdas.github.io/Papers/GBWM.pdf, fetch helper | **Confirmed** (VP): Table 1, *Journal of Investment Management* 16(3), 2018. It is one practitioner scale, not a rule |
| 9 | JPM 2026 LTCMA: U.S. large cap 6.70/7.94/16.47; AC World 7.00/8.28/16.78; intermediate Treasuries 4.00/4.06/3.48; short government/credit 4.00/4.01/1.63; correlations -0.01 / 0.00 / 0.16 / 0.21 | `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` p.2 (pypdf) | **Confirmed** (VRF) |
| 10 | Case lines: "will contribute an additional $150,000" (L43-45); "thoughtful risks ... appropriate balance" (L69-74); "high degree of certainty" and the definition task (L91, L97-99); "must decide how much" and "financial flexibility" (L101-103); range, confidence and "favorable and unfavorable market outcomes" (L110-120); WInS gains not added (L129-133); statistics degree (L16) | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` | **Confirmed** (VRF). Note L118: the range must come with an explanation of how good and bad markets change "the amount she can provide". This matters for the cap (C2-C3) |
| 11 | IPS guide: "planned changes in the portfolio as future funding needs approach" (L46-47); "Focus on the strategy and decision-making framework" (L51-52); no final reserve, projections or range in the IPS (L68-70) | `2026_WGY_Investment_Policy-FINAL.txt` | **Confirmed** (VRF) |
| 12 | Guide p.3: "A long-term investment strategy cannot be judged solely by what happens in the market over a few weeks." (L79); Trading Note "should capture the reasoning behind the decision ..." (L84-86); TN guide reflection elements (L46-52) | `2026_WGY_Investment_Competition_Guide.txt`, `2026_WGY_Trading_Notes_Analysis-FINAL.txt` | **Confirmed** (VRF) |
| 13 | Laura's words used: B9b-Q02 ("A/B testing", résumé), B8b-Q18 ("unstable income", 2021), B9b-Q09 ("[unfinished]") | `phase_D/D13a_laura_quotes_verified.json` | All three are **VERIFIED-PRIMARY in D13a** (AX1 did not re-fetch them). The *readings* D3 attaches to two of them are over-read (C19). All three are Final-Report-only, so out of scope now |
| 14 | IEF/TLH hedge weights 35.7/64.3 | Ticket: issuer durations 6.86y / 11.59y (VP per S3) | Arithmetic confirmed: (11.59 - 9.90) / (11.59 - 6.86) = 35.7%. The iShares pages were not re-opened by AX1 (S3 re-read them on 2026-09-27) |

Nothing had to be downgraded for a failed source check. Downgrades are about interpretation (section 3).

---

## 3. Does each implication follow from its evidence and the case? (the case wins)

| Question | D3 conclusion | AX1 finding |
|---|---|---|
| M034, stocks vs benchmark | 60% equity "buys range, not a bigger expected facility"; +$3k median | **Partly.** The numbers are medians. The **mean** lift is +$6.5-7.0k (JPM), +$9.4k (bonds 4.9%) and -$0.4k (Vanguard) (AX1 [2]). The +$3.3k nets two effects. Equity adds +$12.5-12.9k at the median over the same plan with 0% equity. The plan's non-stock money then trails locking by about $9k, because JPM's bond assumption (4.0%) sits below today's ~5.1% lock yields (F-317). The benchmark is not riskless from today: central case $170k/$201k/$233k (AX1 [3]). The direction stands (stocks add a modest gain and a lot of spread); the wording changes (C4-C5). |
| M028, WInS hedge log | "Demonstrably tracks" within ±0.42% | A **model** backtest: fixed holdings valued on the same curve as the payments, and 155 overlapping windows from one year. Keep it as "about ±0.4% in a model backtest". It is optional for a Trading Note and must not read as performance (C7). |
| M238, barbell | Reject: "larger barbells are just lower-equity points on the same frontier" | **Does not follow.** At the same 2028 equity share, barbell 80% beats the plan at every percentile, under both 4.0% and 5.0% bond assumptions. Its worst historical window is $176k against the plan's $105k (AX1 [4]). The "$101k vs $165k" comparison mixes lock shares (50% vs 80%). "No barbell" can stand only as a judgement: the barbell holds 100% stocks after Laura has spoken in 2031, and the plan keeps more growth in 2028-30. Lock timing becomes a team choice for the IPS (C6). |
| M243, full lock | The certainty is bought and cheap; partial locks fail only without the deposit | **Follows.** Minor point: the 2033 price convention ($6.4k dear, F-408) understates the cost of certainty; on forwards it is about $0.9-5.2k, not $0.6-3.3k (C16). The "~30%" is also supported by history. The real ladder fit under $300k on only 9 of 185 days in 2026, and 98-day 10-year falls of ≥19bp occurred in 35.8% of windows since 1990 (AX1 [5]-[6]) (C8). |
| M039, range as a policy | Adopt "floor bought; give ~90%; never above the top" | **Logic right, rule choice wrong.** "100% within" is by construction (C2). "Give 90%, capped" promises less than is bought. The uncapped "bought floor + half of the rest" gives the same contribution and flexibility with a bottom about $17k higher ($165k vs $148k median; AX1 [8]). It also answers case L118 and matches D5 (C3). |
| M060, lock share | 80-90%; 100% is the "one exact amount" the case rules out | **Follows for 80-90%.** "The case says Laura does not want one exact amount" is an INTERPRETATION: her reason is credibility. At 90% with the cap/share rule, the range is only about $21k wide. The NT$ claim holds only at 90% (C13). |
| M053, joint tail | Conditional dollars; longest-first "settles" the order | **Follows**, with small fixes. The shortfall size rises with the recession link ($9.1k → $11.3k). $25k → about $26k. "Settles" → "supports": longest-first leaves part of the *first* payment exposed, but less face ($12.0k vs $19.0k at -50bp; AX1 [9]) and less price risk (C9-C10). |
| M055, ratchet | Reject; a constant 42% "gets the same bad case" | **Follows on simplicity grounds only.** At the same p5, the ratchet is $2k better at the median and $6k better at p95, so it is not dominated (C11). |
| M059, history | Named rows; the model understates crash years "about tenfold" | Numbers reproduce. "Tenfold" rests on 3 bad years and becomes about 2x at a -20% cut-off (C12). **Final Report material:** later list. |
| v2 section 5 | "All ten payments bought in January 2027 at a known price: Robust" | **Contradicts v2 section 4(a).** It holds in about 2 of 3 rate paths; otherwise completion waits for January 2028 (V1). "$43k robust" becomes about $51k at the 2008 worst 98-day fall of -174bp (V4). |

---

## 4. Contradictions

**Between specialists**

1. **D3 vs D5 on the cap.**
   - D3 M039 recommends a capped "give 90%" rule.
   - D5 finding 5 says "Do not cap the gift at the top", because a 100% in-range figure is empty. D5 audit C11 also flagged
     this.
   - AX1 adds a number that settles most of it. At equal flexibility, D5's uncapped "floor + share of the rest" rule
     announces a higher bought bottom (AX1 [8]).
   - Resolution: one IPS method with two parameters (lock share; give-back share), uncapped by default. The capped variant
     is offered only with P(top reached).
2. **D3 vs D2 on sleeve equity.**
   - D2 recommends 50% (band 45-55) as an IPS rule.
   - D3 says 40-60% are all defensible, and the evidence "does not force a move from 60%".
   - The two files' numbers agree (C23). One team decision is needed before the VT order.
3. **Top percentile.** D3 uses p80, D5 p85, D6 p90 (D5 audit C10). Pick one.
4. **D3 vs D1 on the WInS bond slot.**
   - D3 M238: "VGSH, not IBTM".
   - D1: a dated Nov-2032 Treasury rung could replace the VGSH note.
   - These are different roles (growth money's bonds vs the promise), but the untested question "VGSH or a dated bond for
     the growth money's bonds?" should go to the team once (C18).
5. **D3 vs D1 on the odds.** The two agree (D1 30.5%, D3 30.2% for the real ladder). AX1b and AX1 both say "about 1 in
   3".

**With brief section 14 (facts)**
- No factual contradiction.
- D3 updates two brief figures, correctly:
  - P(ladder > $300k) goes from ~24% (exact-date ladder) to ~30% (real ladder);
  - the fee effect is $16.6k / $32.4k (brief: ~$17k / ~$34k).
- D3's 20.4% equity share in 2028 matches brief s16 ("~20% in 2028-30").
- Brief s16 asks the plan to answer why whole-portfolio equity is so low. D3's corrected M034 wording (a modest expected
  gain, a lot of spread) is the honest input to that.

**With the wins_now ticket**
- **Which ticket:** checked against v0 (as assigned) and against `wins_now/securities_and_allocation_v1.md`, which
  another agent wrote in parallel and which now supersedes v0 for trading. v1 already adopts three things:
  - both splits (60/40: VT 20.5 / VGSH 12.5; 50/50: VT 17.0 / VGSH 16.0);
  - "about 1 in 3" for the ladder odds;
  - T-bills for the 2027 leftover.
- **VT/VGSH weights** at 60%: D3 has 19.8/13.2% (cash outside the growth money); both tickets have 20.5/12.5% with 1%
  cash taken from the short-Treasury part (C17).
- **The 2027 leftover:** the model invests it 60/40, while the ticket holds it in T-bills until 2028 (effect under $1k).
- **No ticket rule is contradicted.** D3 respects the ticket's "never claim 'stable'/'reduced volatility'" and "never say
  'match'" rules. D3 uses "tracks" and "stand-in", not "matched".

---

## 5. Overclaims, jargon, false precision, complexity, privacy, tokenism, submission prose

- **Overclaims** (each corrected in the appended lists):
  - "100% of modelled futures ... in every test" (C2);
  - "not a bigger expected facility" (C4);
  - "riskless control" and "best sure thing" (C5);
  - "just lower-equity points on the same frontier" (C6);
  - "demonstrably tracks" (C7);
  - "Robust: all ten bought in January 2027" (V1);
  - "$43k ... robust" (V4);
  - "settles" (C10);
  - "certain by 2033" without "nominal US$, barring default" (C20);
  - "about tenfold" (C12).
- **"Guaranteed" and "matched" for funds:** none found. Good.
- **Jargon:**
  - undefined in `D3_quant.md`: i.i.d., lognormal, Student-t/nu, multivariate, dominance test, forward zero, bootstrap;
  - undefined in v2: "tornado table" (C22, V10).
- **False precision:** dollar-exact model outputs ($203,997; ±$827; 30.2%; 83.7%). Round in anything the team drafts from
  (C22).
- **Unearned complexity:**
  - the weekly six-column funded-status log is optional (C7);
  - the M039 rule stacks four parameters (lock share, top percentile, give share, cap). D5's two-parameter uncapped rule
    delivers the same money (C3). The IPS has 500 words.
- **Privacy:** no problems found. No family, home or personal details; no student surnames.
- **Tokenism:** two over-read single words from Laura's public record ("A/B testing"; "[unfinished]"), and a persuasion
  use of her degree (C19). All are Final-Report-only and out of scope now.
- **Submission-shaped prose:** two fill-in sentences (C21). Otherwise D3 keeps to "must contain" specifications.

---

## 6. What goes forward to the strategy team (brief s17: TN or IPS only)

**TN (Oct 23)**
- **Before the VT order, fix the sleeve equity share** (D2: 50%; D3: 60% is defensible). The VT note records it. Notes
  cannot be edited.
- **Optional: a hedge-tracking number.** If the team keeps a weekly log, one reflection may cite one pair of numbers:
  the payments' value change (model, the team's calculation) and the WInS hedge change (screen). It must be labelled and
  must never be framed as a gain. PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK applies to IEF, TLH and VT as in the
  ticket.

**IPS (Nov 6): rules to fix before the freeze**
1. **Full lock.** Buy all ten payments on arrival of the first deposit. The reason: prices today, not a forecast. The
   cost: a few thousand dollars of median facility money under JPM, about zero under Vanguard. It protects against a
   smaller or late 2028 income. Never say a partial lock "fails" in the base case.
2. **Contingency clause.** Buy the longest-dated payments first. The first use of the 2028 deposit completes the ladder.
   No facility floor is announced until all ten payments are bought. About 1 in 3 rate paths need this (model and 2026
   history).
3. **Lock timing and share.** One dated lock of 80-90% of the growth money into a 2-year Treasury in January 2031.
   **Open team choice (new):** January 2031 (plan) or January 2028 (barbell-type). Both are defensible (C6).
4. **Contribution rule (method, no dollar figures).** The bottom is the amount already bought. The gift is the bought
   floor plus a share of what the rest becomes. Choose uncapped (two-sided confidence) or capped (report only P(top
   reached)). Pick one top percentile. Laura decides the use of any money above the top (C2, C3, C14, C15).
5. **Stocks.** The "why any stocks" sentence must contain four things: that the all-Treasury alternative exists; a modest
   expected gain plus upside; a lower bad case; and that the payments never depend on stocks (C4). Say what any fee is
   charged on. A fee on the ladder is a claim on the promise money (v2 (c)).
6. **No ratchet.** One lock date only (C11).

**Later (after Nov 9), one line each:**
- M034 benchmark fan chart;
- M028 two-line chart;
- M243 price-of-certainty chart;
- M060 funnel chart and NT$ range;
- M238/M055 alternatives-considered sentences;
- M039 co-sponsor checklist and three-figure 2031 ranges;
- M053 risk-register row;
- M059 named-history rows;
- v2 purchasing-power line;
- the three Laura-quote uses.

---

## 7. Corrections list (full wording in the appended sections)

`D3_quant.md`:
- **Important (7):**
  - C1 scope;
  - C2 "100% within" is a rule;
  - C3 "give 90%, capped" promises less than is bought;
  - C4 median is not expected;
  - C5 the benchmark is not riskless;
  - C6 the barbell is not dominated;
  - C7 "demonstrably tracks" overstates a model backtest.
- **Minor (18):** C8-C25. They cover history support for the 1-in-3 odds, cost vs face, shortfall size, buying-order
  trade-off, ratchet not dominated, "tenfold", M060 interpretation and width, lopsided range, excess wording, 2033 price
  convention, ticket weights, VGSH vs dated bond, Laura-word readings, "certain" wording, fill-in sentences, jargon and
  precision, D2 harmonisation, Vanguard U.S.-only midpoint, and the STRIPS model price.

`D3_model_v2_results.md`:
- **Important (3):**
  - V1 "all ten bought in January 2027: robust" contradicts section 4(a);
  - V2 capped rules shown as "P(within) 100%";
  - V3 riskless control and median-only fee claim.
- **Minor (7):** V4 $43k → about $51k at the 2008 worst; V5 "about 1 in 3"; V6 robustness ranges; V7 purchasing power;
  V8 twist error not computed; V9 scope header; V10 jargon.

---

## Sources (accessed 2026-09-28)
- **Official (VRF):**
  - `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L16, L43-45, L69-74, L88-120, L129-133,
    L146-149);
  - `2026_WGY_Investment_Policy-FINAL.txt` (L45-52, L68-70);
  - `2026_WGY_Investment_Competition_Guide.txt` (L17, L70, L79, L84);
  - `2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L42-53).
- **Market data (VRF):**
  - `competition/official_market_data/daily-treasury-rates_2026-09.csv`;
  - `JPM_LTCMA_2026_US_matrix_USD.pdf` p.2.
- **Primary web (VP):**
  - U.S. Treasury Daily Par Yield Curve 2026:
    https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
  - FRED DGS10: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
  - FRED DEXTAUS: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXTAUS
  - Damodaran histretSP: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
  - Vanguard VCMM forecasts (run of 30 June 2026):
    https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html
  - Das, Ostrov, Radhakrishnan & Srivastav (2018), *Journal of Investment Management* 16(3), Table 1:
    https://srdas.github.io/Papers/GBWM.pdf
- **Repo research (lower authority):**
  - `research/verified_2026-09-27/strategy_mc.py`;
  - `research/insight_v1/phase_A/fact_register.md` (F-012, F-014, F-106, F-112, F-317, F-408, F-508, F-513);
  - `wins_now/securities_and_allocation_v0.md`;
  - `phase_D/D1_rates.md` and `audit_rates_D1.md`;
  - `phase_D/D2_equity_ai.md`, `D5_cosponsors.md`, `D6_behavioural.md`;
  - `phase_D/D13a_laura_quotes_verified.json`.

## What this teaches
1. **A number can be exactly right and still described wrongly.** Every D3 figure reproduced. The errors were in the
   words around them: "expected" for a median, "riskless" for something that is riskless only after it is bought,
   "robust" for something true in 2 of 3 futures.
2. **When a table says 100%, ask whether a rule made it 100%.** A cap makes "within the range" true by definition.
   The honest number is the one the rule does not control: the chance of reaching the top.
3. **To call an option "dominated", line the options up at the same risk.** Compared at the same stock exposure, the
   barbell was not worse. It was a different bet on *when* to take risk. That is a choice for the team, not a mistake
   to reject.
4. **Two rules that deliver the same money can promise different things.** "Give 90%, capped" and "floor plus half of
   the rest" leave Laura the same flexibility. Only one of them lets her announce everything she has already bought.
5. **Check a model's odds against history.** The model's "about 30%" chance that the ladder costs more than $300k looked
   like a guess until 2026 itself showed the ladder above $300k on 176 of 185 days.
