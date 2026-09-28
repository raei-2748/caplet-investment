# D2: Equity & AI-concentration analyst: is sleeve equity paid enough in 2026? (question M030)

Agent D2, insight_v1 run, written 2026-09-27/28. AI-generated research for Team Caplet (brainstorming under the
Wharton AI policy; record its use in Works Cited). None of this is text to submit: it gives numbers, evidence, a
decision option and "what a strong sentence must contain" lists. The team decides and writes every word. The team has
not yet approved the lock-early strategy. Scope follows brief section 17: WInS now, Trading Notes (Oct 23) and IPS
(Nov 6) only. Final Report items appear as one-line "later (after Nov 9)" entries.

Script: `.venv/bin/python research/insight_v1/scripts/D2_equity_premium.py` (run from the repo root; the docstring
lists every input with its status label).

Terms used:
- **Growth sleeve ("sleeve")**: the money the ten $50,000 payments do not need (about $7.7k in 2027 plus the $150k
  deposit in 2028). It pays for the facility contribution and flexibility.
- **Equity premium**: how much more a year stocks are expected to earn than a Treasury held for the same period.
- **Compound (geometric) return**: the steady yearly rate that turns the start value into the end value. It is the
  number that drives the median outcome.
- **Hurdle rate**: what the same money earns with no stock risk, here a Treasury locked today for the sleeve's dates.
- **p5 / p50 / p95**: the outcome that 5% / 50% / 95% of simulated paths fall below. p50 is the median.
- **Forward P/E**: share price divided by analysts' expected earnings for the next 12 months. **CAPE** (Shiller P/E):
  price divided by the average of the last 10 years' inflation-adjusted earnings. An **earnings yield** is 1/P/E.

---

## Summary: top findings (ranked by impact on reaching the semifinals and on making the plan Laura's)

1. **The hurdle is known; the equity premium is not.** Money in the sleeve can lock about **5.2% a year** in
   Treasuries for its own dates (2028->2031: 5.20%; 2028->2033: 5.23%; forwards on the official 2026-09-25 curve,
   VERIFIED-REPO-FILE inputs, ASSUMPTION method). Against that, the expected extra return from stocks is **+1.5 to
   +1.8 points a year under J.P. Morgan** (U.S. large cap 6.70%, AC World 7.00%, data 2025-09-30), **about 0 under
   Vanguard's midpoint** (U.S. 4.2%-6.2%, a VT-like blend ~5.1%, June 30, 2026 run, VERIFIED-PRIMARY), and **about 0
   on the forward earnings yield** (1/19.2 = 5.21%, FactSet 25 Sep 2026, VERIFIED-PRIMARY). So across two houses and
   one yardstick the premium is **roughly -0.2 to +1.8 points a year; call it 0-2**. That confirms the Phase C guess.
2. **Moving sleeve equity from 60% to 50% costs almost nothing in the middle and protects the bottom.** Under all
   three return cases, 50% instead of 60% changes the 2033 median facility money by **-$1.5k to +$0.4k** (on ~$200-210k),
   raises p5 by **$6-7.5k**, raises the p5 of the 2031 bought floor by **$5-6k**, and gives up **$11-14k at p95**
   (model, ASSUMPTION-based). Going down to 40% repeats the pattern (median -$0.6k to -$3.2k vs 60%, p5 +$12-15k).
   Recommendation (for team decision): **set the sleeve at 50% world stocks / 50% short Treasuries** and say why in one
   IPS sentence. Keep 60% only if the team explicitly values the p95 upside more than the floor it promises in 2031.
3. **Tier-1 consequence: decide the split before the first VT/VGSH order, not after.** At 50/50 the WInS option (ii)
   orders become **VT 17.0% ($51,000, ~318 sh) / VGSH 16.0% ($48,000, ~833 sh)** instead of VT 20.5% / VGSH 12.5%
   (PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK). Setting it once, up front, avoids a later "we cut stocks because
   of a forecast" trade that would contradict the Guide's warning against rewriting strategy "simply because markets
   move" (Guide p.5, VERIFIED-REPO-FILE). The hedge (66%) is unchanged.
4. **"Thoughtful risk" = risk that is paid.** This is the Laura link. The case says she "has been willing to take
   thoughtful risks" but wants "an appropriate balance between pursuing growth and protecting the capital required for
   her goals" (case lines 70-73, VERIFIED-REPO-FILE). A plan that checks whether stock risk is paid before taking it,
   and takes it with exactly half of the free money, is a concrete reading of "thoughtful". It must be paired with the
   brief's goal-by-goal framing (promise: no market risk; free money: half in the world stock market), because a
   blended whole-portfolio share (17% in 2028 at 50/50) reads as timid on its own.
5. **Don't argue CAPE vs forward P/E: show why they disagree, then decide by robustness.** CAPE is 41.48, second only
   to Dec 1999's 44.19 (multpl.com, SECONDARY-READ); the forward P/E is 19.2, between its 10-year (19.0) and 5-year
   (19.8) averages (FactSet, VERIFIED-PRIMARY). They disagree because earnings are surging: CY2026 S&P 500 earnings
   +32.0%, with semiconductors +126% in Q3 and Q2 2027 growth expected at only +1.7% (FactSet 25 Sep 2026,
   VERIFIED-PRIMARY). Forward P/E looks normal only if AI-driven profits persist; CAPE looks extreme because it averages
   ten years of lower profits. Neither settles the premium, so the plan should not depend on either being right.
6. **What the broad fund really owns (AI in dollars).** At 50/50 the 2028 sleeve holds ~$79k of VT; VT's top ten
   (21.7%, all AI-linked, a lower bound) is **~$17k, about 3.7% of Laura's whole portfolio**. The same money in an
   S&P 500 fund would carry ~$32k in its 12-name AI basket (40.7%). So Laura's AI exposure is real but small, and a
   world fund halves it without any tilt (S2 figures, VERIFIED-PRIMARY issuer data; arithmetic ASSUMPTION inputs).
7. **Model hygiene before the IPS numbers are quoted anywhere.** `strategy_mc.py` gives sleeve bonds 4.00% (JPM,
   set when the 10-year was 4.16%, F-317), about 1 point below what short Treasuries pay today. That understates the
   no-stock alternative and overstates the reward for equity. The D2 script uses 4.8% (ASSUMPTION, anchored to VGSH's
   4.55% SEC yield and 4.8-5.1% one-year forwards). With market-consistent bonds, even JPM's case gives 60% equity
   only +$1.5k median over 50%.

---

## M030 (tier 1 for the split decision; tier 2 for the IPS rule and sentence)

**Canonical question:** How many extra points a year does sleeve equity really expect over simply buying Treasuries in
2026 (JPM 6.7% vs Vanguard 4.2-6.2%; CAPE ~41 vs forward P/E 19.1; ~5.0% on a 6-year Treasury), and does that move the
sleeve equity weight from 60% toward 40-50%?

**Anchors:** R-C37/R-C38 (case lines 69-74, "thoughtful risks", "appropriate balance"), R-C77 and Guide line 73
("use reasonable return assumptions consistent with your strategy"), R-S26 (Portfolio Analysis), F-004, F-008, F-012,
F-301, F-315, F-317, F-405, F-407. IPS guide line 46: "Explain how your team will approach risk and return"
(VERIFIED-REPO-FILE).

**Is it already answered?** Partly. Brief section 8 item 5 ("more sleeve equity buys range, not median") rested on JPM
alone, with sleeve bonds at a stale 4.00%. New here: a second house (Vanguard) and a market-consistent hurdle, which
remove most of the median gain and turn the weight into a pure choice of spread. The question is well posed; one
correction: the right hurdle is not "a 6-year Treasury today" (5.10% spot) but the forward rate for the sleeve's own
dates, 2028->2031/2033 (5.20-5.23%), because the sleeve money only arrives in 2028.

### One-sentence answer
Stocks are expected to beat a Treasury locked for the sleeve's own dates by only about 0-2 points a year (JPM +1.5 to
+1.8, Vanguard and the forward earnings yield about 0), so cutting sleeve equity from 60% to 50% leaves the median
facility money within about $1.5k while raising the bad-case (p5) outcome by $6-7.5k and the 2031 floor's p5 by
$5-6k: 50% is the better "thoughtful risk" setting, decided once, now.

### Evidence
| # | Claim | Source (access date) | Status |
|---|---|---|---|
| E1 | Treasury par curve 2026-09-25: 1y 4.50, 2y 4.81, 3y 4.94, 5y 4.98, 7y 5.06, 10y 5.17 | `competition/official_market_data/daily-treasury-rates_2026-09.csv` | VERIFIED-REPO-FILE |
| E2 | Forward rates locked today: 2027->2033 5.14%, 2028->2031 5.20%, 2028->2033 5.23%, 6-year spot 5.10% (annual compounding) | D2 script section 1 (bootstrap method from `official_curve_pv.py`) | VERIFIED-REPO-FILE inputs; ASSUMPTION method |
| E3 | JPM 2026 LTCMA: U.S. large cap 6.70% compound / 7.94% arith / 16.47% vol; AC World 7.00 / 8.28 / 16.78; AC World vs intermediate Treasuries correlation 0.00; data 2025-09-30 | `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` p.2 (extracted 2026-09-27) | VERIFIED-REPO-FILE |
| E4 | Vanguard, July 22, 2026: "our 10-year expected annualized return for U.S. equities declined from a range of 4.9%–6.9% to a range of 4.2%–6.2%"; developed ex-U.S. "4.5%-6.5%"; emerging markets "2%–4%"; forecasts are geometric; June 30, 2026 VCMM run | https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html (read 2026-09-27) | VERIFIED-PRIMARY |
| E5 | Vanguard on the same page: "valuations tend to be poor predictors of performance over the short or even intermediate term and should not serve as a primary reason for changing portfolio allocations" | same page | VERIFIED-PRIMARY |
| E6 | 10-year Treasury 4.44% on 2026-06-30 (Vanguard's run date) vs 5.17-5.18% now: bonds got ~0.7 points more attractive after Vanguard's run | FRED DGS10 CSV (read 2026-09-27); E1 | VERIFIED-PRIMARY |
| E7 | S&P 500 forward 12-month P/E 19.2 (5-yr avg 19.8, 10-yr avg 19.0; 20.4 on June 30); price +2.7% and forward EPS +8.9% since June 30; trailing P/E 25.8 | FactSet Earnings Insight, 25 Sep 2026, https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_092526.pdf (read 2026-09-27) | VERIFIED-PRIMARY |
| E8 | CY2026 earnings growth 32.0%; CY2027 15.4%; Q2 2027 1.7%; Q3 2026 IT sector +63.5%, semiconductors +126%, IT ex-semis +24.2% | same FactSet issue | VERIFIED-PRIMARY |
| E9 | Shiller CAPE 41.48 (Sep 25, 2026); mean 17.42; max 44.19 (Dec 1999) | https://www.multpl.com/shiller-pe (read 2026-09-27) | SECONDARY-READ (aggregator; Shiller's own file not read) |
| E10 | 10-year TIPS real yield 2.83%; 10-year breakeven 2.34% | F-008, F-009 (`phase_A/fact_register.md`) | VERIFIED-PRIMARY |
| E11 | VT top-10 21.7% (all AI-linked names, lower bound); S&P 500 top-10 38.8%, 12-name AI basket 40.7%; VT 37.7% non-U.S. | `wins_now/S2_growth_sleeve.md` sections 1-2; S3 ticket section 1 (issuer pages) | VERIFIED-PRIMARY (via S2/S3) |
| E12 | VGSH SEC yield 4.55% [9/24]; VT $160.03, VGSH $57.59 closes [9/25] | `wins_now/securities_and_allocation_v0.md` section 1 | VERIFIED-PRIMARY (via S3) |
| E13 | Case: "willing to take thoughtful risks" ... "an appropriate balance between pursuing growth and protecting the capital required for her goals" | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` lines 69-74 | VERIFIED-REPO-FILE |
| E14 | Guide p.5: a long-term strategy "should not be rewritten simply because markets move or hindsight reveals a different outcome" | `competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt` line 156-157 | VERIFIED-REPO-FILE |

### Numbers (D2 script; model outputs are ASSUMPTION-based)

**Expected premium over the 2028->2033 Treasury hurdle (5.23%)**

| Source | Compound equity return | Premium, points a year |
|---|---|---|
| JPM AC World (VT-like) | 7.00% | +1.77 |
| JPM U.S. large cap | 6.70% | +1.47 |
| Vanguard U.S. low / mid / high | 4.2 / 5.2 / 6.2% | -1.03 / -0.03 / +0.97 |
| Vanguard VT-like blend low / mid / high (62.3% U.S.; non-U.S. 75% developed, 25% EM: ASSUMPTION) | 4.08 / 5.08 / 6.08% | -1.15 / -0.15 / +0.85 |
| Yardstick: forward earnings yield 1/19.2 | 5.21% | -0.02 |
| Yardstick: CAPE earnings yield + breakeven (crude) | 4.75% | -0.48 |

The yardsticks are not forecasts; they only show that valuation measures do not point to a large premium either.

**2033 facility money and 2031 bought floor by sleeve equity weight** (200,000 paths, seed 20260927; plan as in
brief section 7; sleeve bonds 4.8%/2% vol; equity vol 16.78%; payments are funded by the ladder in every row)

| Sleeve equity | JPM 7.00%: p5 / p50 / p95 | Vanguard blend 5.08%: p5 / p50 / p95 | Vanguard U.S. low 4.2%: p5 / p50 / p95 | 2031 floor p5 (JPM / Vg mid) |
|---|---|---|---|---|
| 0% | $189k / $200k / $211k | same | same | $151k / $151k |
| 40% | $173k / $208k / $252k | $169k / $202k / $246k | $167k / $200k / $243k | $138k / $135k |
| **50%** | **$167k / $209k / $265k** | **$162k / $203k / $258k** | **$160k / $200k / $254k** | **$133k / $130k** |
| 60% (current) | $161k / $211k / $279k | $155k / $203k / $270k | $152k / $200k / $266k | $129k / $124k |
| 70% | $155k / $212k / $294k | $148k / $203k / $282k | $145k / $199k / $277k | $124k / $119k |

**Moving 50% -> 60%:** median +$1.5k (JPM), +$0.2k (Vanguard mid), -$0.4k (Vanguard low); p5 -$6.2k / -$7.1k /
-$7.5k; p95 +$11-14k; 2031 floor p5 -$4.9k to -$5.9k. **Crash stress** (stocks -35% in 2030, the year before the floor
is bought; JPM otherwise): floor median $133k at 50% vs $127k at 60%. Under JPM, 37% of paths at any weight from 40% to
70% end below the all-Treasury median ($200k); under Vanguard, 46-47%. (That comparison is D3's M034; noted only.)

**Whole-portfolio equity in 2028:** 40% sleeve -> 13.7%; 50% -> 17.1%; 60% -> 20.5% (ladder ~$305k + sleeve ~$158k,
S2 arithmetic, ASSUMPTION).

### Implications

| Deliverable | Type | Implication |
|---|---|---|
| **WInS now** (tier 1) | decision + number | Before the first growth orders, the team picks the sleeve split once. D2 option: **50/50** -> option (ii) orders **VT 17.0% (~$51,000, ~318 sh) / VGSH 16.0% (~$48,000, ~833 sh)**, cash 1%, hedge 66% unchanged. Rebalancing band inside the sleeve **VT 45-55%** (replaces 55-65). Option (iii) (literal 2027 book) is unaffected. Securities: VT, alternates VTI+VXUS (62/38) or ITOT+IXUS; VGSH, alternates SHY or a WInS-listed ~2-year Treasury note. **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** for every ticker. VT, VTI, VXUS, VGSH, SHY were on the 2025-26 list (historical only). |
| **Trading Notes** (tier 1) | sentence elements | If the VT or VGSH buy becomes a note, its reflection can carry the reason for the split. Elements only: (a) the growth money is what the payments do not need; (b) Treasuries for the same dates pay about 5%, known today; (c) two major forecasters disagree whether stocks will beat that (one says ~1.5-2 points more, one says about the same); (d) so half goes to world stocks for upside and half stays in short Treasuries for the amount Laura may promise co-sponsors; (e) the risk accepted: a fall shrinks the facility range, never the payments. **Never** say stocks are "overvalued" or predict a crash; never quote CAPE in a note (a note is ≤100 words and must be consistent with the IPS). |
| **IPS** (tier 2) | sentence + rule | "Rules to fix before Nov 6": (1) sleeve = 50% broad world stocks / 50% short Treasuries, band 45-55, rebalanced once a year (WInS: weekly check); (2) the weight is set once on today's known Treasury yields and does **not** change with market forecasts or valuation readings afterwards (Guide p.5; Vanguard's own warning, E5); (3) returns are stated as a range across two published houses, not one point. What a strong IPS risk/return sentence must contain: the known Treasury rate for her dates (~5%); that expected extra reward for stocks is small this year (0-2 points); that stock risk is taken only with money the promise does not need; that this is how the firm reads "thoughtful risk". No citations or house names are needed in the IPS (formal citations are banned); "two major published forecasts" is enough. |
| **Later (after Nov 9)** | one-liners | FR: two-house projection table with returns as a range. FR: model sleeve bonds at market-consistent ~4.8-5.2%, not 4.00%. FR: one valuation sentence explaining CAPE vs forward P/E (earnings surge). FR: re-check whether JPM's 2027 LTCMA has appeared (F-315) and freeze one dated edition. |

**Deadline tier:** 1 for the WInS split (orders are imminent; the ticket's 60/40 is marked provisional); 2 for the IPS
rule and sentence.

**Confidence:** medium. High that the premium is small and uncertain (two primary houses plus a primary yardstick
agree on "small"); medium on 50% specifically, because the model is lognormal, i.i.d., fee-free and uses one volatility
for every house; 40% is equally defensible on the same numbers, and 60% is defensible only on JPM's view.

**Changes the current strategy?** Yes, modestly: sleeve equity 60% -> 50% (brief section 7 and the wins_now ticket's
VT 20.5% / VGSH 12.5% -> 17.0% / 16.0%; band 55-65 -> 45-55). The lock-early structure, the hedge and the 2031 method do
not change.

**Criterion served most:** Investment Strategy (a clear rule, set once, traced to her words); second, Portfolio
Analysis (quantitative and qualitative reason for each holding's size).

**What this teaches:** Before taking a risk, ask what the safe choice pays: when a Treasury locks 5% for your dates,
stocks have to beat 5%, not 0%, and this year nobody can promise they will by much.

### Devil's advocate (and answers)
- *"Laura took leaps; 50% is timid."* Her verified words praise taking the jump (D13a VERIFIED-PRIMARY; read the D13a context note before any use, and
  no Laura quotes in the Trading Notes or IPS), but the case asks
  for "thoughtful" risk and "balance". At 50% the p95 is still $254-265k; the whole portfolio is 17% stocks only
  because 66% is a promise she has already made. Show risk goal by goal, not blended.
- *"Vanguard's 4.2-6.2% is from June; stocks got cheaper since (forward P/E 20.4 -> 19.2)."* True (E7), but Treasury
  yields rose ~0.7 points in the same period (E6), so the premium over bonds moved against stocks, not for them
  (forward earnings yield +0.3 points, 10-year yield +0.7).
- *"This is market timing."* It is a one-time strategic setting based on a known number (today's Treasury yields), not
  a forecast of a fall, and it is frozen afterwards. Changing it later because stocks rallied or fell would be timing.
- *"JPM is newer in format and official in the repo; use it alone."* JPM's data date is 2025-09-30, when the 10-year was
  4.16% (F-010): its bond numbers are ~1 point stale. A 2027 edition may appear in October (F-315). Relying on one house
  whose inputs are a year old is the weaker position.
- *"The difference is only ~$6k at p5; why bother?"* Because it is free: the median barely moves. When a change costs
  nothing in the middle and helps the promise to co-sponsors, it earns its (zero) complexity. If the team disagrees,
  keeping 60/40 is not wrong; it is a choice of spread and should be written as one.

---

## Sources (all accessed 2026-09-27 unless stated)
- Vanguard, "Vanguard Capital Markets Model forecasts", July 22, 2026 (June 30, 2026 run):
  https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html (VERIFIED-PRIMARY,
  read with `fetch_text.py`).
- FactSet Earnings Insight, 25 Sep 2026 (also 18 and 11 Sep issues checked):
  https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_092526.pdf
  (VERIFIED-PRIMARY).
- multpl.com Shiller PE: https://www.multpl.com/shiller-pe (SECONDARY-READ).
- FRED DGS10/DGS5/DGS7/DFII10: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10,DGS5,DGS7,DFII10
  (VERIFIED-PRIMARY).
- Repo files (VERIFIED-REPO-FILE): `competition/official_market_data/daily-treasury-rates_2026-09.csv`;
  `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` p.2;
  `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` lines 69-74, 130-132;
  `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` lines 20, 46, 68;
  `competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt` lines 73, 156-157.
- Prior run files: `research/insight_v1/wins_now/S2_growth_sleeve.md`, `securities_and_allocation_v0.md`;
  `research/insight_v1/phase_A/fact_register.md` (F-004, F-008-F-012, F-301, F-315, F-317, F-405, F-407);
  `research/insight_v1/phase_B/B5b_macro_2026.md`, `B10a_contrarian.md`; `research/insight_v1/phase_C/survivors.json`
  (M030).
- Script: `research/insight_v1/scripts/D2_equity_premium.py`.

## What this teaches
1. **Compare risk with the safe alternative, not with zero.** A stock return of 6-7% sounds generous until you notice
   that a Treasury for the same dates already pays 5.2%. The reward for risk is the gap, and this year it is small.
2. **When experts disagree, pick the choice that is fine under all of them.** JPM and Vanguard differ by about 2 points
   a year on stocks. At 50% equity, Laura's median barely moves whichever is right, and her bad case is better.
3. **Two valuation numbers can both be true.** CAPE (41) and forward P/E (19) disagree because profits jumped 32% in a
   year, led by AI chips. Knowing why they disagree is more useful than picking a side.
4. **Decide once, then stop.** Setting the stock share from today's known bond yields is planning; changing it every
   time markets move is guessing. The competition guide rewards the first and warns against the second.
