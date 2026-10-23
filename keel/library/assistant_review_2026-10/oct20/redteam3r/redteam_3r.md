# Red team: option 3r ($10k reinvestment reserve in the Nov-2041 Treasury)

AI-generated research for Team Caplet, Tue 20 Oct 2026 (Sydney). Claude Code wrote this. These are MODEL numbers for the Tue 27 Oct vote, not text to submit. If the team uses any of it, log it in the AI-use record and later in the Final Report's Works Cited (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026).

**Target:** the recommendation in `oct19/coupon/coupon_risk_options.md` (option 3r, lines 125-157). 3r takes $10k of the 2028 deposit before the floor and holds it in the 3.125% Treasury maturing 15 Nov 2041. The reserve counts in the 2031 top but not the minimum. In 2033 a release rule passes on anything above "projected need + $5k", and there is a separate "net-minimum" rule.

**Verdict: MODIFY.** Keep the core idea: a small Treasury reserve, paid for from the 2028 deposit, kept out of the minimum. It survives every model I tried. But four things must be fixed, and the IPS should carry only the principle:
1. **Fix the double count in the 2031 top.** As written, the 2033 gift reaches the announced top in only 41% of paths. Without the reserve the figure is 68%, and V5 says "about three of four". The true cost to the median gift is about $6k, not $3k.
2. **Fix how it is explained.** The reserve works mainly by *locking a long yield on its own money*, not by "its price rises". The claim that "$10k there does the job of $25k in IBTM" comes from a modelling choice: after 2032 the IBTM money sits at 0%.
3. **Fix the evidence claims.** "Zero in all 690 history windows" rests on only about 4 non-overlapping 16-year periods. With real curve shapes, 2 of 690 windows go short by about $177.
4. **Move the details out of the IPS.** The holding, the $10k and the $5k margin belong in the Final Report. The IPS gets one principle.

The cheaper ideas, "income stays in Treasuries" and "a 2033 margin", do not give 90% of the benefit (section 9). A 2033 re-match (1R) is the one real rival, but its cost is not yet measured.

Paths in this file: `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/`, and `oct19/` the same with oct19.

---

## 0. How I tested it (and that the test engine is faithful)
- **The engine.** `oct20/redteam3r/scripts/rt_engine.py` is a copy of the study's `run()` with five switches added:
  - shifts that differ by tenor (curve twists);
  - more reserve holdings, including two "what-if" holdings used to split hedge from carry;
  - option 1R, a re-match in 2033;
  - cutting the announced minimum without moving money;
  - T-bill interest on waiting cash.
- **It matches the study.** With the switches off and the same seed, it reproduces the study exactly. Option 1: 16.45% short, max $6,121, gift median $165,259. 3r: 0.02%, gift median $162,190. 3b: 4.85%. Output: `oct20/redteam3r/data/validate_out.txt`.
  - One tiny difference: after Nov 2041 my reserve stops growing, while the study's keeps growing at its purchase yield for about 1.5 months. The worst shortfall moves from $659 to $666.
- **Basis.** Unless stated, I use the study's own basis: the 16 Oct curve held to 1 Jan 2027, holdings' dates, waiting cash at 0%, 100,000 paths with seed 20261019.
- **Checked twice.** A second seed (7) and the new **19 Oct 2026 curve** both give the same conclusions (`data/verify2_out.txt`):
  - the 19 Oct curve was fetched from treasury.gov on 19 Oct at 21:42 UTC (`data/tsy_202610_fetch20oct.csv`);
  - the ladder costs $298,446 on it.
- **New data.** FRED monthly yields TB3MS, GS1, GS3, GS5, GS10, GS20 and GS30, fetched 19 Oct 2026 from https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10 (and the same URL with each other id).
  - GS20 is missing from 1987-01 to 1993-09; I filled that gap with GS30.

---

## 1. Model assumptions

### 1a. "Parallel random walk, no mean reversion": the attack mostly FAILS
- **History is close to the model.** Real 10-year yield changes, 1953-2026, versus the model's 1.0 point × √years (`data/hist_changes_out.txt`):

| Horizon | History sd | Model sd |
|---|---|---|
| 1 year | 1.08 pts | 1.00 |
| 6 years | 2.35 pts | 2.45 |
| 15 years | 4.04 pts | 3.87 |

- **Mean reversion is mild.** The variance ratio is 0.79-0.93, where 1.0 means a pure random walk. A yearly AR(1) fit gives a half-life of about 8 years.
- **With mean reversion added** (same 1-point yearly volatility), payments still never go meaningfully short under 3r:

| Model | Option 1 short | 3r $10k short | A $5k reserve short |
|---|---|---|---|
| Random walk (the study) | 16.4% | 0.02% | 1.81% |
| Half-life 8 years | 12.8% | 0.01% | 0.73% |
| Half-life 4 years | 10.4% | 0.00% | 0.29% |

- **Verdict.** The $10k size holds up. Mean reversion only makes the case for something smaller.
- **What the random walk does get wrong:** it lets yields drop to the 0.25% floor from today's 5%. A judge could fairly call that pessimistic for the tails, but it errs on the safe side.

### 1b. "0% on waiting cash": not simply cautious
- **What the study claimed.** Counting 4.26% T-bill interest cuts option 1's short chance from 16% to 7.5% (`oct19/coupon/coupon_risk_options.md:54`).
  - That figure subtracts *total* waiting interest from *total* shortfall.
- **What a consistent plan would do.** It would also count that interest in the 2033 projection. Then the interest becomes a new risk, because bill rates can fall after 2033 (`data/redteam_results_16oct.json`, suite "T-bills"):

| | Cash waits at 0% | Plan counts T-bill interest |
|---|---|---|
| Option 1 short | 16.45% (worst $6.1k) | **14.2%** (worst $10.8k) |
| 3r $10k short | 0.02% (worst $0.7k) | **0.41%** (worst $3.5k) |

- **Why it matters.** The filed Feb-2037 and May-2038 notes say the proceeds wait "in a short-term Treasury ETF" (`snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:16-17`). If the team quotes 3r's 0.02%, it must also say the sizing *does not count* that interest: it is a bonus, not part of the plan. Otherwise the honest figure is about 0.4%.

### 1c. "0 of 690 history windows" overstates the evidence
- **The windows overlap.** 690 monthly start dates for 16-year windows in 882 months of data give only **4 non-overlapping windows** (`data/redteam_results_16oct.json` → `history_windows`).
- **With real curve shapes**, not 10-year-only parallel moves, 3r $10k is short in **2 of 690 windows**:
  - start Apr 1985: $178 short;
  - start Nov 1994: $176 short.
  - Source: `data/alternatives_stdout_16oct.txt`, last line.
- **The 12-month block bootstrap** (20,000 paths built from 1953-2026 curve and stock months) gives 3r $10k **0.18%** short, worst $1.8k.
- **Fair wording:** "rare and small (under $2k in our worst modelled case)", not "zero".

### 1d. Minor model quirk (small, slightly optimistic)
- The engine sizes iBond funds with one coupon (e.g. IBTM 4.89%) but pays them out at their yield (4.93%).
- So with no rate change each iBond rung delivers about $108-118 too much: roughly $560 across the five.
- That surplus soaks up small shortfalls on later payments. It does not change any conclusion.
- Source: `rt_engine.py`, the copied line `cpn = r["cpn"] if ... else ytm`.

---

## 2. The hedge logic

### 2a. Most of the protection is the locked yield, not the price rise
I held the study's rules fixed and changed only *what the $10k is held in* (100k random-walk paths; `data/redteam_results_16oct.json`, re-checked with seed 7):

| $10k held in | Short (random walk) | Short (history, real curves) | Short (bootstrap, twists) |
|---|---|---|---|
| IBTM, then 0% after Dec 2032 (the study's 3b) | 4.87% | 11.9% | 4.48% |
| IBTM, then rolling T-bills | 2.92% | 7.5% | 2.17% |
| Locked at the Nov-41 purchase yield, **no price change** (what-if) | 0.10% | 1.16% | 0.28% |
| **The Nov-41 bond (3r)** | **0.02%** | **0.29%** | **0.18%** |

- **First step: 4.9% → 2.9%.** This is the 0% artefact being removed.
- **Second step: 2.9% → 0.1%.** The reserve money itself earns a locked ~5.3% until 2041 instead of falling bill rates. That is the main effect.
- **Last step: 0.1% → 0.02%.** This is the price gain.
- **The IBTM comparison is wrong.** At honest T-bill rates, $15k in IBTM is still short 1.0%. So "$10k there does the job of $25k in IBTM" (`coupon_risk_options.md:67`) should be dropped.
- **The plain-English point:** "the reserve's own money cannot suffer the reinvestment problem, because it is locked in a 2041 bond." "Its price rises when yields fall" is true, but it is the smaller part.

### 2b. The price gain fades and covers little of the risk
- **The gain shrinks toward maturity.** If yields fall 2 points right after the Jan 2028 purchase, the $10k gains about $2.4k by mid-2028. As the bond nears maturity that becomes $2.1k (2033), $1.0k (2039) and $0.3k (2041) (`reserve_gain_fades`).
- **It is small next to the ladder's exposure.**
  - The ladder's interest sensitivity (DV01) is $232 per basis point (bp); the payments' is $293. The gap is **$61/bp** (`data/dv01_gap_out.txt`; 16 Oct curve, 1 Jan 2027).
  - $10k of Nov-41 adds $11.3/bp, so it covers **about 19%** of the gap. Closing the whole gap would take about $54k of the bond.
- **So 3r is a cushion, not a hedge.** Most of the work is done by the cover chain (leftover → reserve → Laura's half → gift above the floor).
- **The model agrees.** The reserve's 2033 price gain correlates −0.07 with post-2033 surprises and +0.59 with the 2033 projected need (`hedge_diag`).
- **And if yields fall before Jan 2028,** the reserve is bought after the fall and gains nothing (scenario A, section 2c).

### 2c. Curve twists: a real but small weakness
- **Where the ladder's exposure sits.** Ladder income lost for a 1-point fall at one tenor only (`key_rate_minus1pp`):

| Tenor | 3 months | 1 year | 3 years | 5 years | 10 years | 20 years |
|---|---|---|---|---|---|---|
| Income lost | $24 | $300 | $989 | $3,357 | $4,949 | $558 |

- **About 46%** of the exposure is at 5 years or shorter. Between 2028 and 2031 the reserve has **no** sensitivity there; it only reacts to 10-20-year yields.
- **In history,** when the 10-year fell more than 1 point within 2 years, the 1-year fell on average 2.66 points against 1.91 for the 10-year. "Bull steepeners" (short rates fall far more than long rates) appear in 3.8% of 2-year windows: 1974-75, 1980, 2001, 2008, 2019, 2023 (`data/hist_changes_out.txt`).
- **Deterministic tests** (stocks at 7%; reserve value in 2033 against the same reserve with no price change; `scenarios`):

| Scenario (spread over 2028-31) | Ladder short before cover | Reserve price gain | Option 1 gift | 3r gift |
|---|---|---|---|---|
| Parallel −2 | $9.4k | +$2.1k | $169.9k | $161.3k |
| Bull steepener | $7.0k | +$1.0k | $169.9k | $162.5k |
| Bull flattener | $6.3k | +$1.9k | $169.9k | $164.5k |
| −2 only after 2033 | $2.4k (option 1 pays $2.4k short) | n/a | $169.9k | $168.5k (3r short $0) |

- **Reading the table.** In every case 3r still pays every payment. The twist only weakens the "hedge" story. Section 2a showed the twist effect in the paths: 0% → 0.29% (history) and 0.07% → 0.18% (bootstrap).

---

## 3. Double counting

### 3a. The bond is also the 2042 payment rung: no double count of money, but a labelling risk
- **No double count in the money.** In the model the reserve is *extra* face value on top of the 2042 rung.
- **The labelling risk.** In WInS and in Laura's account, the rung and the reserve are one position (WInS now holds 20 × $1,000 face; `oct19/drive/sheets/portfolio.md` R29).
  - A judge will see one Nov-41 holding described as both "for the 2042 payment" and "a reserve".
  - The team already handles this for IBTM by splitting shares between two jobs (`portfolio.md` R37-39). The same split, stated as face amounts, is needed here.
- **Concentration is not an issue.** Treasuries carry no meaningful issuer risk.

### 3b. The real double count: the reserve is counted twice in the 2031 top
- **How it happens in the study's code** (`rt_engine.py`, copied from `coupon_options.py:227-231`):
  - The reserve first *reduces* the projected uncovered shortfall in 2031.
  - Then it is *added in full* (+$10k) to the top.
  - But the 2033 release rule holds back the projected need plus a $5k margin. So the gift almost never gets the full $10k back.
- **The effect** (`data/topcheck_out.txt`, `data/release_rules_stdout_16oct.txt`):

| | Gift reaches the 2031 top | Gift ends >$5k below top | Gift median | Top median |
|---|---|---|---|---|
| Option 1 | 68% | 8% | $165.3k | $166.1k |
| **3r as written** | **41%** | **28%** | $162.2k | $164.9k |
| 3r, top counts $5k (not $10k) | 72% | — | **$159.2k** | $159.9k |
| 3r, top counts what 2031 projects will be released | 78% | — | $159.3k | $159.8k |

- **What follows.**
  - V5's line "the contribution reached the upper bound in about three of four simulated paths" (`oct19/drive/ips_report_live.md:29`) would be false under 3r as written.
  - The range also widens: the median gap between minimum and top is $33k, against $25k for option 1.
  - Once the top is fixed, the honest cost of 3r is: **minimum −$10k, median gift −$6k (not −$3k), and about +$16k returned to Laura in 2042** (median $22.8k against $7.0k).
  - So most of the money is not lost. It moves from the 2033 gift to Laura in 2042.
  - The same holds on the bootstrap with twists (top +$5k: reach 72%, gift median $159.3k) and on the 19 Oct curve (reach 73%, gift median $160.2k).

---

## 4. Liquidity of selling the bond: a weak attack
- **The market.** Treasuries are the deepest bond market. A sale would be a few thousand dollars in $1,000 face steps, years from now, in Laura's real account.
  - Retail bid-ask costs were not measured (UNVERIFIED); they are likely tens of dollars.
- **Sales tend to happen when the price is up.** The reserve is only needed when yields have *fallen*. That is exactly when its price is above its locked-yield value (positive gains in every falling-yield scenario in section 2c). If yields rise there is no shortfall and nothing to sell.
- **WInS.** No sale is needed before the 6 Nov freeze. The WInS limit of 2× a security's daily volume has not been checked for bonds (UNVERIFIED), but earlier fills of 18-20 bonds went through.
- **The real issue is wording.** V5 says "each payment's liquidity comes from a maturity, not a sale" (`ips_report_live.md:28`). 3r adds an exception, and the IPS has to say so.

---

## 5. The release rule: load-bearing but complex
I tested simpler rules for what happens to the reserve in 2033 (100k random-walk paths; `data/release_rules_stdout_16oct.txt`):

| Rule | Short | Gift median | Reaches top | Gift below minimum | Laura 2042 |
|---|---|---|---|---|---|
| Study: release above need + $5k; top + $10k | 0.02% | $162.2k | 41% | 0.05% | $18.6k |
| Same release; **top + $5k** | 0.02% | $159.2k | 72% | 0.11% | $22.8k |
| Release above need, **no margin** | 1.33% | $164.1k | 78% | 0.24% | $14.6k |
| Release **half** the reserve, fixed | 0.79% | $160.3k | 75% | 0.10% | $22.4k |
| **No release**, top + $0 (3a: all back to Laura in 2042) | 0.02% | $154.2k | 71% | 0.24% | $27.6k |

- **What this shows.** The $5k margin does real work: without it, shortfalls jump to 1.3%. The "fixed half" rule is simpler but 40 times worse on payments.
- **The simplest honest version** is "3a": no release, and the reserve returns to Laura in 2042. It costs the gift about $11k at the median but needs no 2033 projection at all.
- **The best compromise** is the study's release rule with the top counting only $5k of the reserve. That is still three rules: source, release and top.

---

## 6. Over-engineering for the judges
- **The IPS instructions** ask teams to "focus on the strategy and decision-making framework ... rather than describing individual investments or presenting detailed financial calculations" (`competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt:51-52`).
- **Last year's lesson:** "complexity must earn its place" (`snap/main/CLAUDE.md:62-63`).
- **3r in full is too much for the IPS.** It needs a holding, a size, a source, a top rule, a release rule with a margin, a sale exception and a return-to-Laura line. That is roughly 50-70 words of a ~470-word budget (target in `oct19/ipskit/ips_writing_kit.md:56`).
- **Does it earn its place? Yes, at principle level.** It closes the post-2033 gap that option 1 leaves on money Laura has already taken out. That gap fails "funded by the investment portfolio ... may not rely on ... other outside funding" (case:91-92).
- **The split that fixes it:** the IPS states one principle; the Final Report carries the $10k, the Nov-41 bond, the $5k margin and the test evidence. The IPS may not have citations, and the Final Report is where evidence goes (IPS instructions: 123-126).

---

## 7. Consistency with the filed WInS notes and with V5
- **Filed WInS notes: no conflict.**
  - The Nov-41 note ("supports her final $50,000 payment ... with reinvested coupons funding part of each", `05_...notes.md:24`) and the IBTM note (`:19`) stay true. Nothing filed is contradicted, so the TNA (due 23 Oct) is unaffected.
- **V5 text: four sentences would need changing** (`ips_report_live.md:25-30`):
  1. "any shortfall met from her other holdings and the facility floor last" → the reserve comes first.
  2. "liquidity comes from a maturity, not a sale" → an exception for the reserve.
  3. "reached the upper bound in about three of four simulated paths" → false under 3r as written (41%); about 72% with the fix in 3b.
  4. "a permanent two-point fall ... about $21,000 short, met from her retained equity" → met first from the reserve. Also restate the figure on one basis: about $19k on holdings' dates (`coupon_risk_options.md:174`).

---

## 8. Does the WInS book have to change?
**No, it does not have to.** It is a choice the team should make on purpose.
- **Size at WInS scale.** The reserve is $10k × about 0.64-0.65 (0.644; never 0.667 = 300/450, REG H5) [consistency fix 20 Oct, packaudit §1d]. That is about $6.4-6.5k, or about 2.2% of the book: about 8 more Nov-41 bonds at about 78 per 100 (WInS clean price 76.695 on 5 Oct, `portfolio.md` R29; recheck live).
- **Option A: no trade.** The IPS already says the WInS book "shows this allocation ... scaled down" (`ips_report_live.md:45`). Use "about mirrors" and put one Final Report line saying the reserve's 2% sits inside IBTM in WInS.
  - Risk: a judge comparing the IPS with WInS finds a named reserve that isn't there.
- **Option B: two trades after the vote, before Fri 6 Nov 5pm ET.**
  - Sell about 130-150 IBTM ($25) and buy about 8 Nov-41 bonds ($10). Each needs a new note: 300 characters or fewer, and notes cannot be edited (`portfolio.md` R15).
  - Only Ray trades. Check the yield and the live price first.
  - Funding from idle cash alone ($3,514) breaks the sheet's own "keep at least $1,000" rule (`portfolio.md` R31) once you go past about 3 bonds.
  - The 2× daily-volume check for bonds is UNVERIFIED.
- **Avoid the half-measure** of buying 3-4 bonds only: it matches neither the plan nor the book.

---

## 9. Simpler alternatives: do any give 90% of the benefit?
All rows use the same 100k random-walk paths. "Gift < min" is shown as raw / with the net-minimum rule. `data/alternatives_stdout_16oct.txt`, `data/release_rules_stdout_16oct.txt`, `data/sizes_out.txt`.

| Alternative | Short | Worst | Minimum | Gift median | Reaches top | Gift < min | Verdict |
|---|---|---|---|---|---|---|---|
| 1 "income stays in Treasuries" (state only) | 16.4% (avg $219) | $6.1k | $145k | $165.3k | 68% | 2.15% / 0.59% | **No.** Post-2033 gaps hit money Laura has taken out (case:91-92) |
| 1 + count waiting interest | 14.2% | $10.8k | $145k | $165.3k | — | 1.79% / 0.53% | **No** (section 1b) |
| 1 + announce $10k less (no money moved) | 16.4% | $6.1k | $135k | $165.3k | 68% | 1.00% / 0.06% | **No.** Protects the minimum, not the payments |
| 1M: 2033 margin of $5-10k taken from Laura's half | 2.7% | $4.9k | $145k | $165.3k | 68% | 2.15% / 0.59% | **No.** A bigger margin does not help: when stocks crash her half is too small (stock-dependent, like option 2) |
| Smaller buffer: 3r $5k, top + $0 | 1.81% | $2.9k | $140k (53% of paths) | $160.0k | 76% | 0.81% / — | **Close.** About 89% of the drop in short chance (random walk) but only 78% on real-curve history (5.5% short) |
| 3r $7.5k, top + $2.5k | 0.25% | $1.8k | $135k | $159.6k | 73% | 0.35% | Pointless: the $5k rounding gives the same minimum as $10k |
| 3r $6k, top + $1k | 0.93% | $2.4k | $140k (50%) | $159.8k | 74% | 0.60% | The largest reserve that keeps a $140k minimum in about half of paths |
| **1R: re-match the reserve once in Jan 2033** at that day's yields, top-up from leftover → Laura's half → gift above the floor; announce $10k less | 0% (modelled) | $0 | $135k | **$165.3k** | 68% | 1.00% / 0.06% | **The one real rival.** See below |
| **3r $10k with the top fixed (+$5k)** | 0.02% | $0.7k | $135k | $159.2k | 72% | 0.11% / 0.01% | **Recommended form of 3r** |

**About 1R.** It answers the case's own question directly: "explain how its composition should change, if at all" (case:94-96). It needs no 2028 change and no WInS trade, and it adds no holding. But:
- **Its 0% is modelled, not proven.** It assumes a 2033 re-match locks 2033 yields.
  - The naive version, where income simply waits for the next payment, costs **$6.8k** in 2033 at unchanged yields with cash at 0%, and $0 at T-bill rates (`data/rematch_cost_out.txt`).
  - A real re-match must re-size the holdings so waiting is under a year: the dedication linear programme of option 4. Its 2033 cost is UNVERIFIED.
- **It conflicts with V5's "held to maturity"** and needs several trades in 2033.
- **It protects the minimum less well** on bootstrap twists: 2.20% / 0.66% against 3r's 0.80% / 0.21%.
- **It returns about $16k less to Laura in 2042.**

Treat 1R as the documented alternative, or as a reason to test the 2033 re-match cost properly before 27 Oct.

---

## 10. Explaining it in one sentence: a test, not a draft
- **What the sentence must contain:**
  - where the money comes from (2028 deposit, before the floor);
  - where it is held (a long Treasury held to 2041);
  - what it protects (payments if reinvested income earns less);
  - what happens to any unused part (released up to the announced top in 2033, or back to Laura).
- **Word limits.** If the team cannot say that in its own words in about 30 words, the IPS should state only the principle.
- **Do not claim:**
  - "its price rises, so it covers the gap" (it covers about a fifth of the rate gap; section 2b);
  - "zero shortfalls in history" (section 1c);
  - "does the job of $25k" (section 2a).
- **What this teaches (for Ray):** a bond held to maturity locks a yield on *its own* money. A coupon bond's coupons do not get that lock, so a ladder of coupon bonds is "shorter" than the payments it serves. That is the whole coupon problem in one line, and why a little extra long bond helps.

---

## 11. What the team must decide on 27 Oct (student decisions; AI suggests, the team decides)
1. **Is the case met?** Is "payments short in about 2 in 10,000 modelled paths (about 1 in 550 in the real-curve bootstrap and 2 of 690 overlapping history windows), never by more than about $2k" enough for "high degree of certainty"? Or do you prefer 1R's modelled 0%, at an unmeasured 2033 cost?
2. **The top rule.** Count $5k of the reserve in the 2031 top (gift reaches the top about 72%; median gift −$6k vs option 1), or the full $10k (reaches the top 41%)?
3. **Who carries the cost?** The 2033 gift (3r) or Laura's 2042 money (1R and option 1 leave her less)?
4. **WInS.** Option A (state "about mirrors") or option B (two trades by 6 Nov), decided on purpose.
5. **The waiting cash.** Will the IPS sizing ignore T-bill interest on waiting cash (keeps 0.02%) or count it (about 0.4%)? Say which.

## 12. Corrections the oct19 study needs before anyone quotes it
- **`coupon_risk_options.md:67`:** "does the job of $25k in IBTM" comes from IBTM money sitting at 0% after 2032. At T-bill rates, $15k in IBTM is still short 1.0%.
- **`:54`:** the 16% → 7.5% figure depends on method. Counted consistently, it is 14.2%.
- **`:148`:** "zero in all 690 history windows" → about 4 independent periods; 2 of 690 short by about $177 with real curves.
- **`:127` and the comparison table:** add "gift reaches the 2031 top": 68% (option 1) against 41% (3r as written). The −$3k gift cost is −$6k once the top is equally credible.
- **`:151`:** the hedge is mainly a locked yield; the price gain is the smaller part.

## 13. Limits and UNVERIFIED
- **Same model family as the study.** Bonds are priced off one yield plus shifts, with no roll-down. iBond funds are treated as par bonds. Stocks are lognormal or bootstrapped. There are no taxes and no costs outside WInS.
- **The twist runs** use 6 tenor nodes, linear between them. The bootstrap uses 12-month blocks, with yield changes demeaned and stock returns re-centred to 7%.
- **1R** is modelled as "post-2033 cash flows equal the frozen 2033 projection". Its true cost is UNVERIFIED.
- **Other UNVERIFIED items:** WInS coupon crediting dates; the WInS 2×-volume rule for bonds; the live WInS price of the Nov-41 bond; retail bid-ask spreads.

## 14. Reproduce
Run from `oct20/redteam3r/scripts/` with `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I`:
- `validate.py ../data`
- `experiments.py ../data ../data/tsy_202610.csv 10/16/2026 ../data/redteam_results_16oct.json` (from the folder above)
- `alternatives.py ../data ../data/tsy_202610.csv 10/16/2026 ../data/alternatives_16oct.json`
- `release_rules.py`, `topcheck.py`, `sizes.py`, `rematch_cost.py`
- `verify2.py <curve csv> <date> <seed>`
- `dv01_gap.py ../data ../data/tsy_202610.csv 10/16/2026`
- `hist_changes.py ../data`

All outputs are in `oct20/redteam3r/data/`.
