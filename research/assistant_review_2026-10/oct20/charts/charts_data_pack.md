# Final Report charts: data pack (Team Caplet, written Tue 20 Oct 2026, Sydney)

> **Verified 20 Oct (`oct20/verify_charts_cr/verify_charts_cr.md`): arithmetic confirmed; fix before building charts.** (C-1) C4 tracking ratio uses bootstrap PV but the template helper uses simple par PV: on the helper method 16/19 Oct = 99.75/99.85 (payments index 101.46/100.91); the "ladder lagged" finding is 0.15-0.36 points depending on method. (C-2) Scenario tables price the 2028 floor at the spot yield (4.938%, floor $117,807); the distributions and numbers desk use the forward (~5.11%, floor ~$116.8k): use one convention and name it. (C-3) iBond funds are credited with own-yield coupons: coupon shortfalls on the holdings basis are $10,095 / $19,487 / $28,233 / $40,246 (not $9,537 / $18,952 / $27,718); option 1 short 16.2% not 15.6%; no ranking changes. Scale: use 0.644 (numbers register H5). c1_cash_flow_timeline.csv: the $25,340 "Laura keeps" excludes the $3,806 leftover, and the 2032-12-15 150,000 is an internal maturity (move out of money_in). IPS:123 bans charts/citations, not numbers. Replace DATEVALUE with plain date subtraction for Excel.


**What this is.** AI-generated research (Claude Code) for the five charts planned in the Final Report prep pack
(`oct19/frprep/final_report_prep.md:378-393`). It is a **data pack, not charts and not text to submit**. For each chart it gives
the client question, the data table (CSV), the method in steps a student can redo in a spreadsheet, where each input comes
from, a chart type and axis choice with the reason, and the traps. Students build every chart themselves, rebuild the numbers
they quote (prep pack 6.1), and record this AI help in the AI-use log and the Final Report's Works Cited (Wharton AI Policy,
https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). No sentence here is meant for the report.

**Labels.** MODEL = a computer estimate from AI-built scripts, not a fact. UNVERIFIED = nobody has confirmed it.
Every dollar figure in Laura's plan is MODEL unless it comes from the case.

**Data date.** treasury.gov daily par yield curve, **Mon 19 Oct 2026 close** (published that evening ET; fetched 19 Oct
21:53 UTC = Tue 20 Oct 08:53 Sydney). Par yields: 1y 4.50, 2y 4.77, 3y 4.85, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48.
Earlier October rows were unchanged against the 19 Oct Sydney fetch. Source URL:
https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv
(saved as `data/tsy_202610_fetch20oct.csv`; the full 2026 file is `data/tsy_2026.csv`).

**Every number goes stale.** The Final Report's valuation date is the **6 Nov close** (prep pack 6). Re-run everything on that
curve (section 8). The data here are for building and testing the charts now, not for quoting.

Folder (`P/` below) = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/charts/`.

---

## 0. Five things to know before building anything

1. **The room under $300k came back a little.** Yields rose on 19 Oct (10y 5.09 to 5.15). On Caplet's holdings with yields
   unchanged (basis D) the 1 Jan 2027 ladder cost is **$297,162**: room $2,838, a 0.098-point fall uses it up. Model odds that it
   costs more than $300k on 1 Jan 2027: 41% (σ 1.0 point/yr; 38% at the 2026 realised 0.71). On 16 Oct it was $298,940 / $1,060 / 47%.
   It moved $1,778 in one trading day. This is why no chart should carry a ladder-cost level as a fact.
2. **Every chart is about Laura's real plan except C4.** C1, C2, C3 and C5 use her $300k (2027) + $150k (2028) (case:129-133).
   C4 is the WInS book, which is that plan **scaled down by about 0.64**. Never put a WInS dollar on a Laura chart, and never
   add WInS gains to her projections (Guide:70-73; case:132-133).
3. **One basis per chart, named on the chart.** Five ladder-cost bases exist (A-E, `oct19/numbers/findings.md`). This pack uses
   **basis D** (each $50,000 discounted from its holding's end date, 19 Oct curve treated as the 1 Jan 2027 curve) for costs, and
   the coupon study's **holdings basis** (each rung sized to hold $50,000 on its own end date if income is reinvested at its own
   yield; waiting cash at 0%) for reinvestment shortfalls. Both are cautious and match each other.
4. **New finding for C3: the cover shrinks exactly when the shortfall grows.** If yields fall for good, the coupon shortfall
   rises, but the 2028 floor also costs more, so less goes into VT and Laura's half of VT is smaller. A 2-point permanent fall:
   shortfall $18,952; Laura's half of VT about $14,109 (not the $22.5k of the middle case). Draw C3 as paired bars, not as a
   flat "what Laura keeps" line (section 3).
5. **New finding for C4: the ladder lagged its payments slightly as yields fell.** 8 to 16 Oct (back-filled, MODEL and Yahoo
   prices): ladder holdings +1.21%, value of the payments they cover +1.57%; tracking ratio 99.64. Likely reason (MODEL): the
   holdings pay coupons and monthly distributions, so they are a little less rate-sensitive than single $50,000 amounts. That is
   reinvestment risk showing up in real time, worth one line in the implementation section if it persists to 6 Nov.

---

## 1. C1 (core): "What pays each $50,000, and when?"

**Files.** `P/c1_payment_map.csv` (one row per payment), `P/c1_cash_flow_timeline.csv` (dated events 2027-2042).

**Table (Laura's plan; costs MODEL, 19 Oct curve).**

| # | Payment | Holding that pays it | Ends | Cash waits | Simple cost | Basis D cost | WInS units |
|---|---|---|---|---|---|---|---|
| 1 | 1 Jan 2033 | IBTM (iBonds Dec 2032) | on or about 15 Dec 2032 | 17 days | $37,287 | $37,248 | 1,142 of 4,503 sh |
| 2 | 1 Jan 2034 | IBTO (Dec 2033) | ~15 Dec 2033 | 17 days | $35,376 | $35,318 | 1,024 sh |
| 3 | 1 Jan 2035 | IBTP (Dec 2034) | ~15 Dec 2034 | 17 days | $33,563 | $33,489 | 927 sh |
| 4 | 1 Jan 2036 | IBTQ (Dec 2035) | ~15 Dec 2035 | 17 days | $31,822 | $31,726 | 894 sh |
| 5 | 1 Jan 2037 | IBTR (Dec 2036) | ~15 Dec 2036 | 17 days | $30,144 | $30,024 | 853 sh |
| 6 | 1 Jan 2038 | T 4.750% 15 Feb 2037 | 15 Feb 2037 | 320 days (10.5 months) | $29,867 | $29,742 | 20 ($20k face) |
| 7 | 1 Jan 2039 | T 4.500% 15 May 2038 | 15 May 2038 | 231 days (7.6 months) | $27,889 | $27,725 | 20 |
| 8 | 1 Jan 2040 | T 4.375% 15 Nov 2039 | 15 Nov 2039 | 47 days | $25,633 | $25,411 | 18 |
| 9 | 1 Jan 2041 | T 4.250% 15 Nov 2040 | 15 Nov 2040 | 47 days | $24,209 | $23,943 | 18 |
| 10 | 1 Jan 2042 | T 3.125% 15 Nov 2041 | 15 Nov 2041 | 47 days | $22,851 | $22,536 | 20 |
| | | **Total** | | | **$298,641** | **$297,162** | WInS value $200,154 |

The coupon study's figure on the same day is $298,446 (room $1,554), close to the simple method.

**Method (spreadsheet).**
1. One row per payment: payment date (1 Jan 2033 to 1 Jan 2042, case:88-89), holding, end date.
2. `t` = (end date − 1 Jan 2027) / 365.25.
3. Par yield at `t`: take the two treasury.gov tenors either side (5/7, 7/10 or 10/20 years) and interpolate in a straight line.
4. Cost = 50,000 / (1 + y/200)^(2t), with y in percent. Sum the ten rows. That gives the "simple" column.
5. Cash waits = payment date − end date, in days.
6. Optional exact method (basis D): bootstrap the curve in a 60-row sheet. Column A holds t = 0.5 ... 30. Column B holds the par
   yield interpolated at t. Column C holds the discount factor: d_n = (1 − c/2 × (sum of the earlier d's)) / (1 + c/2), with
   c = B/100. Then discount each $50,000 at the zero rate interpolated at `t`. This reproduces $297,162.

**Sources.** Payments and dates: case:43-45, 59-60, 88-90. Holdings, units and fills: the WInS fills of 7-8 Oct
(`/home/user/snap/main/ops/routines/portfolio_check.py`, `/home/user/snap/main/COMPETITION.md` section 8). Note that its Feb-2037
coupon is wrong: 4.750%, not 5.000%. Fund end dates: iShares, "will terminate on or about October or December 15 of the year in
each Fund's name" (IBTM and IBTR product pages, read 19 Oct 2026 21:57 UTC:
https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf and .../350028/...-dec-2036-...).
Yields: the treasury.gov CSV.

**Chart type.** A timeline with one row per payment (a dumbbell). The x axis is calendar years 2027-2043, linear. Draw a thin
bar from purchase (Jan 2027) to the holding's end date, and a dot on the payment date; the gap between them is the waiting
time. Put two "money in" markers at the top (1 Jan 2027 $300k; Jan 2028 $150k). Colour by type (Treasury ETF / Treasury bond).
*Why:* the question is "what and when", and time on one axis answers both in one look. Bars of cost would answer a different
question.

**Traps.**
- **IBTM has two jobs.** In WInS, 1,142 of its 4,503 shares are the 2033 payment and 3,361 are the facility floor (Sheet
  Portfolio rows 38-39). In Laura's plan the floor is bought only in Jan 2028. Do not draw all of IBTM as payment 1.
- **"Ends on or about".** iShares: the funds "do not seek to return any predetermined amount". Never label a fund bar
  "pays $50,000".
- **The two long waits.** Feb 2037 to Jan 2038 and May 2038 to Jan 2039: the cash must sit in a WInS-listed short-term Treasury
  ETF. Which ETF is UNVERIFIED (SGOV to be re-checked; prep pack W9), and cash itself is not on the 2026-27 permitted list
  (prep pack 0.2).
- **Scale.** WInS units are not Laura's. WInS value ÷ plan cost is about 0.66-0.69 per rung (0.674 overall). Show WInS units
  only in a footnote, if at all.
- **Dates.** The case says "beginning of" each year. The models use 1 Jan 2027 and 2 Jan 2028. Write one convention under the chart.

---

## 2. C2 (core): "What can I tell co-sponsors in 2031, and how sure is it?"

**Files.** `P/c2_range_scenarios.csv` (7 named cases × 2 coupon options, every input listed),
`P/c2_range_model_distribution.csv` (MODEL percentiles and probabilities).

**Scenario table (option 1 = the current V5 rule; MODEL, 19 Oct curve; dollars rounded).**

| Case | Inputs | Bottom | Top (2031) | Gift (2033) | Laura keeps 2033 |
|---|---|---|---|---|---|
| Middle | yields unchanged; VT +6.94%/yr | $145,000 | $169,686 | $169,686 (at top) | $25,340 |
| Favourable | VT +10%/yr | $145,000 | $171,425 | $171,425 | $30,423 |
| Stocks −40% in 2032 | range set, then crash | $145,000 | $169,686 | $162,631 | $12,631 |
| Stocks −40% in 2028 | crash after VT bought | $145,000 | $161,045 | $161,045 | $14,218 |
| Yields −0.5 before Jan 2027 | gap $11,991 filled first | $130,000 | $154,498 | $154,498 | $21,225 |
| Yields −2 for good from 2 Jan 2027 | coupon shortfall $18,952 | $145,000 | $162,337 | $161,300 | $1,772 |
| Combined bad | −0.5, then −2 more, stocks −40% in 2032 | $130,000 | $147,553 | $132,129 | $0 |

The gift lands inside the range in every case. Under **option 3r** ($10k reserve in the Nov-2041 bond) the middle case is a
bottom of $135,000, a top of $168,374 and a gift of $168,374; the combined bad case is a bottom of $120,000, a top of $146,861
and a gift of $132,731. All 14 rows are in the CSV.

**MODEL distribution (number sheet anchored on basis D, 200,000 paths).**
- Bottom: $145,000 in 61.1% of paths.
- Top in 2031, p5/p50/p95: $141,730 / $167,229 / $183,815.
- Gift in 2033, p5/p50/p95: $139,260 / $166,411 / $182,868.
- Gift inside the range: 99.33%. Gift within $1k of the top: 75.8%.

**Coupon study (100,000 paths; history since 1953).**
- Option 1: gift below the announced bottom 1.95% (history 2.61%); some payment short 15.6% (history 29.3%).
- Option 3r $10k: gift below the bottom 0.06% (history 0.43%); payment short about 0.6% (worst about $3.3k) under parallel moves on the V3 engine (study engine marked at market 0.08% / 0.32% / 0.72%; never 0.02%) [consistency fix 20 Oct, packaudit §1d].

**Method (spreadsheet; one row per case).**
1. Ladder cost on 1 Jan 2027 = the C1 total, with every yield moved by the case's "before" move.
2. Gap = MAX(cost − 300,000, 0). Leftover = MAX(300,000 − cost, 0).
3. R (the amount the floor repays in Dec 2032) = 150,000 − gap (− 10,000 under 3r).
4. Floor yield in Jan 2028 = the par yield at 4.953 years (2 Jan 2028 to 15 Dec 2032), plus all moves so far. Middle: 4.938%.
   Floor cost = R / (1 + y/200)^(2 × 4.953).
5. VT bought = 150,000 − gap − buffer − floor cost.
6. VT on 1 Jan 2031 = VT × (1+r2028)(1+r2029)(1+r2030). VT on 1 Jan 2033 = that × (1+r2031)(1+r2032).
7. Bottom = FLOOR((R − 3,700)/5,000) × 5,000. Top = R + ½ × VT2031 (+ 10,000 under 3r).
8. Gift = MIN(top, R + ½ × VT2033). The coupon shortfall (C3) is paid first from the leftover, then Laura's half, then the gift.
9. Laura keeps = VT2033 − the VT used by the gift − the VT set aside for any shortfall.

**Sources.** Deposits and the 2031 requirements: case:43-45, 109-120. The plan rule ("floor + half the fund, capped at the
announced top"): IPS V5 as summarised in `/home/user/caplet-investment/CLAUDE.md` (insight_v1 section) and
`oct19/ipskit/ips_writing_kit.md` D4/D6. VT return: JPM 2026 LTCMA AC World 7.00% compound, 16.78% vol
(`/home/user/caplet-investment/competition/official_market_data/`, verified 27 Sep). Fee: 0.06% (the VT note). Curve: treasury.gov.

**Chart type.** Horizontal range bars, one per case. A solid segment runs from $0 to the bottom (the firm part), a lighter
segment from the bottom to the top (the part that can be reached), and a dot marks the 2033 gift. The x axis runs from $0 to
$200,000. Put the MODEL confidence beside the chart ("inside the range in about 99 of 100 model paths"), with its method.
*Why start at $0:* it shows honestly that most of the gift is the firm floor and the uncertain part is small. A truncated axis
would make the range look wide and shaky, which is the opposite of the client's need (case:114-116).

**Traps.**
- **Show only the option the team votes on 27 Oct** (D1). The two options have different bottoms ($145k vs $135k).
- **The bottom is a rule, not a number.** It is $145k only if the Jan 2027 ladder costs under about $301.3k (61% of paths). Label
  it "bottom set by rule on [valuation date]".
- **The 2031 valuation date is undecided (D8).** The table uses 1 Jan 2031.
- **Two different confidences.** "The gift lands in the range" (99.3%) is not "the payments are safe". Never print one without
  naming which it is (case:91 vs case:117-118).
- **The scenario returns are the team's choice.** +10% and −40% are illustrations. The team must define its own favourable /
  middle / unfavourable cases and list every input (prep pack 6.3).
- **Laura's kept money is counted two ways.** The models count only "half of VT". Under "the rest stays hers" she also keeps
  the part of the giving half above the cap ($2.8k more in the middle case). Pick one definition.
- **US dollars only.** Over 2 years a fixed US$ amount moved −15% to +17% in NT$ (`oct19/cosponsor/cosponsor_research.md:154-162`).
  Do not convert the bars. Put any NT$ figure in a dated footnote.
- **No chart or numbers in the IPS** (IPS:123). This chart is for the Final Report and the co-sponsor excerpt.

---

## 3. C3 (core): "What could still go wrong with the payments, and who covers it?"

**Files.** `P/c3_shortfall_and_cover.csv` (main), `P/c3_rungs_at_minus2.csv` (where the −2 shortfall sits, rung by rung),
`P/c3_one_rung_rebuild_Nov2041.csv` (a full rebuild of one rung that a student can copy).

**Table (MODEL; yields fall on 2 Jan 2027 and stay down; total shortfall over 2033-2042).**

| Fall | Shortfall (holdings basis) | Basis E (number sheet) | Leftover (2033) | $10k reserve (3r) in 2033 | Laura's half of VT (stocks normal / −40% in 2032) | Uncovered after leftover + half, option 1 (normal / crash) |
|---|---|---|---|---|---|---|
| 0 | $0 | $0 | $3,806 | $12,988 | $22,513 / $12,631 | $0 / $0 |
| −1 | $9,537 | $11,005 | $3,806 | $12,369 (or $13,773*) | $18,423 / $10,337 | $0 / $0 |
| −2 | $18,952 | $21,287 | $3,806 | $11,776 (or $14,636*) | $14,109 / $7,916 | $1,037 / $7,229 |
| −3 | $27,718 | $30,902 | $3,806 | $11,210 (or $15,585*) | $9,556 / $5,361 | $14,355 / $18,550 |

\* if the fall comes just **after** the reserve is bought in Jan 2028 (its price rises). Option 4 (dedicated rebuild) shortfalls:
$2,846 / $5,596 / $8,254. Unconditional MODEL figures for Laura's kept money in 2033: p50 $25,605, p5 $0. History since 1953
(basis E): p95 shortfall $22,387, worst $39,020 (start June 1984).

**One rung (Nov-2041 3.125% bond, holdings basis).**
- 29,303 face, bought 1 Jan 2027 for $22,751 at its own yield of 5.365% (MODEL; the simple check is the par yield at 14.87 years, 5.335%).
- Thirty $1.5625 coupons per $100 face. Reinvested at the own yield they grow to 170.63 per 100, which is $50,000.
- At own −1/−2/−3 points they grow to $48,418 / $46,982 / $45,677: short $1,582 / $3,018 / $4,323. At 0%: $43,039.
- This rung is about $3.0k of the $19.0k total at −2. The longest bonds carry the most (`c3_rungs_at_minus2.csv`).

**Method (spreadsheet).**
1. Rebuild the Nov-2041 rung from `c3_one_rung_rebuild_Nov2041.csv`. One row per coupon date. Value at maturity =
   coupon × (1 + r/2)^(half-years left). Sum, add 100, and size the face so the own-yield total is $50,000.
2. Repeat the sum with r − 1, r − 2 and r − 3. The shortfall = 50,000 − face × total / 100.
3. Scale up: either rebuild all ten rungs (the iBond funds count as bonds whose coupon equals their yield, ending 15 Dec), or
   take the ratio of your one-rung result to the MODEL rung value and apply it to the MODEL total (say which).
4. Cover: leftover in 2033 = leftover × (1 + y6/200)^(2 × 5.96). Half of VT comes from the C2 method run with the same yield
   fall. The 3r reserve = 10,000 × (1 + y/200)^10, where y = the par yield at 13.9 years plus the fall.
5. Uncovered = MAX(shortfall − leftover − reserve − half, 0).

**Sources.** Coupons and maturities: the WInS listing and `portfolio_check.py`. Curve: treasury.gov. Models: copies of
`oct19/coupon/scripts/coupon_options.py` (holdings basis) and `oct19/numbers/scripts/ips_numbers_oct19.py` (basis E, history
replay on FRED GS10 monthly, `scripts/fred_GS10_monthly.csv`). The equity history in the coupon study is Shiller's monthly total
return (`data/shiller_monthly.csv`, copied from oct19; original source as cited in `oct19/coupon/coupon_risk_options.md`).

**Chart type.** Grouped columns. The x axis is the four permanent falls (0, −1, −2, −3 points) in order. The y axis runs from $0
to about $35,000 and must start at zero, because dollars are compared as lengths. For each fall, draw two columns side by side:
the shortfall, and a stacked "cover" column (leftover, reserve if 3r, Laura's half with stocks normal). Mark the stocks-crash
half with a dash on the cover column.
*Why not one horizontal "what Laura keeps" line (the prep pack's first idea):* the cover is not fixed. It falls as yields fall,
and a flat line would overstate it by $4-13k in exactly the cases that matter.

**Traps.**
- **Basis.** At −2 the shortfall is $18,952 on the holdings basis but $21,287 on basis E, because E also loses interest on
  waiting cash. Quote one, and say which.
- **A stress, not a forecast.** "Yields fall 2 points on 2 Jan 2027 and never recover" is a named stress. The model and history
  odds are separate facts (`oct19/coupon/coupon_risk_options.md:36-48`).
- **The reserve's timing.** The reserve gains only if yields fall after it is bought in Jan 2028.
- **Option 1's chain uses money Laura has already taken out.** Gaps after 2033 paid from released money fail "funded by the
  investment portfolio" (case:91-92). Co-sponsors and "her other assets" are banned as cover.
- **The D1 vote decides which bars appear.** Draw the chosen option only, and keep the others for an alternatives table.

---

## 4. C4 (optional): "Did the bonds do their job while we held them?"

**Files.** `P/c4_wins_backfill_8-19Oct.csv` (back-filled 8, 9, 13, 14, 15, 16 and 19 Oct, MODEL/public data),
`P/wins_tracking_template.csv`, `P/wins_tracking_pv_helper.csv` (section 7).

**Back-fill (WInS book, scaled; ETFs at Yahoo closes; T-bonds = curve model + the fill-day gap + accrued; cash $3,513.79 as WInS reported).**

| Close (ET) | Book total | Ladder holdings | Payments index | Ladder index | Tracking ratio | VT index | 10y | Plan ladder cost (D) |
|---|---|---|---|---|---|---|---|---|
| 8 Oct | $301,848 | $198,641 | 100.00 | 100.00 | 100.00 | 100.00 | 5.22 | $294,805 |
| 9 Oct | $301,832 | $198,491 | 99.85 | 99.92 | 100.07 | 100.69 | 5.24 | $294,321 |
| 16 Oct | $304,429 | $201,037 | 101.57 | 101.21 | 99.64 | 98.80 | 5.09 | $298,940 |
| 19 Oct | $303,393 | $200,154 | 101.00 | 100.76 | 99.77 | 98.98 | 5.15 | $297,162 |

The book total matches the 16 Oct desk figure (about $304.4k, `oct19/numbers/findings.md`).

**Method.**
1. Ladder holdings = 1,142 × IBTM + 1,024 × IBTO + 927 × IBTP + 894 × IBTQ + 853 × IBTR + 200 × T37 + 200 × T38 + 180 × T39 +
   180 × T40 + 200 × T41, where bond prices are per $100 and the multiplier is units × 10. Then add bond accrued interest and
   all ladder income received.
2. Value of the payments they cover = ten $50,000 amounts discounted from the close date to each holding's end date, using
   that day's par yields (the helper sheet). The scale cancels in an index, so use the unscaled $50,000.
3. Index both to 100 on the first row. Tracking ratio = 100 × (ladder ÷ PV) ÷ (first-row ladder ÷ first-row PV).

**Sources.** WInS Portfolio Summary and positions (W1/W2), Transaction History (W4), treasury.gov. The back-fill uses Yahoo
(query1.finance.yahoo.com/v8/finance/chart, fetched 19 Oct 21:56 UTC), which is not an official source and not what WInS shows.
Replace it with WInS screen values.

**Chart type.** A line chart. The x axis is close dates (a real time axis). Two lines: ladder holdings (index) and the value of
the payments they cover (index). Optionally add VT (index) in a muted colour to show what "not matched" looks like. The y axis
can run 97-104: a non-zero baseline is fine for index lines; state the base date. If the page budget is tight, plot only the
tracking ratio.
*Why:* the question is "did they move together", and two indexed lines answer it directly.

**Traps.**
- **Coupons leave the ladder as cash.** On Mon 16 Nov the four Nov/May bonds pay $1,538.75 (May-2038 $450.00, Nov-2039
  $393.75, Nov-2040 $382.50, Nov-2041 $312.50). The iBond funds pay monthly ("Distribution Frequency Monthly", iShares, read
  19 Oct). Without adding income back (template column AH) the ladder will look as if it fell. Whether WInS credits coupons and
  when is UNVERIFIED.
- **Scale.** In dollars, the payments the WInS ladder covers = PV × 0.678 (the WInS ladder's fill cost $195,886 ÷ PV $289,091 on
  7 Oct). Prefer the index.
- **Not a scorecard.** Measure the ladder against the payments, not against the market or other teams (Guide:74-78). Never call
  the bond gain good news for Laura: falling yields make her January purchase dearer (`oct19/tnakit/tna_fact_kits.md:350`).
- **Accrued interest.** Whether the WInS total counts it is UNVERIFIED. Column W of the template shows the difference.
- **Missing curve days.** treasury.gov skips bond-market holidays (12 Oct; Wed 11 Nov Veterans Day). Use Friday rows.

---

## 5. C5 (optional): "How does my portfolio change as the payments approach?"

**Files.** `P/c5_plan_composition.csv` (option 1 and option 3r), `P/c5_wins_vs_plan_mapping.csv`.

**Table (option 1; MODEL; middle case; held-to-maturity values at each holding's purchase yield).**

| Point | Ladder ETFs | Ladder bonds | Floor | VT | Leftover | Paid out | In portfolio |
|---|---|---|---|---|---|---|---|
| 1 Jan 2027 after purchase | $167,806 | $129,357 | – | – | $2,838 | – | $300,000 |
| 2 Jan 2028 after deposit 2 | $176,485 | $136,331 | $117,807 | $32,193 | $2,981 | – | $465,797 |
| 1 Jan 2031 range announced | $205,226 | $159,525 | $136,358 | $39,372 | $3,456 | – | $543,937 |
| 1 Jan 2033 before set-aside | $226,860 | $177,166 | $150,000 | $45,027 | $3,806 | – | $602,859 |
| 1 Jan 2033 after payment 1, reserve, gift | $176,860 | $177,166 | – | – | $3,806 | gift $169,686; Laura $25,340 | $357,832 |
| 1 Jan 2037 after payment 5 | – | $218,488 | – | – | $3,806 | | $222,295 |
| 1 Jan 2042 after payment 10 | – | – | – | – | $3,806 | | $3,806 |

All yearly rows, and the 3r variant (with a reserve column: $10,000 in 2028, $5,000 kept after the 2033 release, rising to
$8,003 by 2042), are in the CSV. Cross-check: ten $50,000 payments on 1 Jan 2033 at a flat 5% = $405,391 (annuity due), and the
2033 reserve here is $404,026.

**Method.** Each rung's value at date t = 50,000 / (1 + z/200)^(2 × (years from t to the end date)), with z = its zero yield on
1 Jan 2027. After the end date it is $50,000 cash until the payment. The floor = floor cost × (1 + yF/200)^(2h), reaching R in
Dec 2032. VT is grown at 6.94%/yr. The leftover is grown at the 6-year par yield.

**Mapping to WInS (2 Jan 2028 plan, MODEL).**
- Plan total $465,797, so the scale is 300,000 / 465,797 = **0.644**.
- Plan weights: IBTM (payment + floor) 33.7%; IBTO-IBTR 6.8-8.0% each; T-bonds 5.1-6.7%; VT 6.9%; leftover 0.6%.
- WInS on 19 Oct: IBTM 32.5%; VT 8.65%; cash 1.2%. Every rung is within about 1.3 points of the plan. VT is the largest
  difference (+1.7 points), as already known ("about 9%" is WInS, "about 7%" is Laura).

**Chart type.** Stacked columns from $0. Segments: ladder ETFs, ladder bonds, floor, VT, leftover (and the 3r reserve). The x axis
is the points in time. Mark 2033 with a callout for the gift and for what Laura keeps.
*Why:* the question is about composition over time, and stacks show both the mix and the run-off.
*Axis:* use a true time axis, or mark the 2028 to 2031 and 2031 to 2033 gaps clearly. Evenly spaced categories make the
2028-2033 growth look like a few months.

**Traps.**
- **The 2033 fall is not a loss.** About $195k leaves as the gift and Laura's release. Label it so.
- **Book values, not market values.** Say "held-to-maturity value at purchase yields (MODEL)".
- **Nominal dollars.** The 2042 payment is worth about $40,036 in 2033 dollars at 2.5% inflation, and $33,681 in 2026 dollars
  (C22 in the prep pack).
- **Answers case:96-97 (reserve composition and how it changes).** The CSV shows the iBond funds running out in 2037 and only
  T-bonds after. Keep the chart consistent with the IPS run-off and parking rule.
- **The mapping table** belongs in Portfolio-at-a-Glance as a table (prep pack F6), not as a chart.

---

## 6. Sources by input (all charts)

| Input | Official or primary source | Used in |
|---|---|---|
| Deposits, payments, timing, 2031 range, outside-money ban, WInS P&L excluded | Case `official/2026_27/Laura_Gao_2026_Client_Profile.txt`:43-60, 88-120, 129-133; Guide:70-78 | all |
| Treasury par yields (each date) | treasury.gov daily par yield curve CSV (URL above) | all |
| iBond fund end dates, "no predetermined amount", monthly distributions, 0.07% fee | iShares IBTM / IBTR product pages, read 19 Oct 2026 21:57 UTC | C1, C3, C4 |
| T-bond coupons and maturities, units, fills, cash | WInS fills 7-8 Oct (`snap/main/ops/routines/portfolio_check.py`); students confirm on WInS W2/W4 | C1, C4 |
| VT return and volatility | JPM 2026 LTCMA (AC World 7.00% compound, 16.78% vol), repo `competition/official_market_data/` | C2, C3, C5 |
| Rate history | FRED GS10 monthly (`scripts/fred_GS10_monthly.csv`) | C3 |
| ETF closes (back-fill only) | Yahoo Finance chart API: not official; replace with WInS screens | C4 |
| US inflation 2.5% | JPM 2026 LTCMA (CLAUDE.md, verified 27 Sep) | C5 note |

The models are AI-built: Works Cited, one entry per tool, with students' own 1-2 sentences on how it was used.

---

## 7. WInS weekly tracking template (7 Nov to 4 Dec, Sydney)

**Files.** `P/wins_tracking_template.csv` (header row plus six rows with live formulas) and `P/wins_tracking_pv_helper.csv`
(computes the payments' value from five typed par yields; tested: it gives $295,356 for 19 Oct, the same as the AI value).

**Rows (ET close → when to capture in Sydney):**
- Fri 6 Nov (freeze) → Sat 7 Nov from 08:00. US clocks change on 1 Nov, so Sydney is 16 hours ahead; 4 pm ET = 08:00 Sydney.
- Fri 13 Nov → Sat 14 Nov.
- Fri 20 Nov → Sat 21 Nov. This is the first row after the 16 Nov coupons.
- Fri 27 Nov → Sat 28 Nov. Markets are closed Thu 26 Nov (Thanksgiving) and close early on the 27th; the exact times are
  UNVERIFIED (check NYSE/SIFMA).
- Tue 1 Dec → Wed 2 Dec. This is the last row for the planned Wed 2 Dec submit.
- Optional: Thu 3 Dec → Fri 4 Dec, only if the team submits later (deadline Fri 4 Dec 5 pm ET = Sat 5 Dec 09:00 Sydney).

**Columns.**

| Columns | What | Source / formula (row r) |
|---|---|---|
| A-D | close date ET, Sydney capture time, recorded by, checked by (first names) | typed |
| E, F | WInS total value, WInS cash | W1, typed |
| G | ladder income this week (T-bond coupons + iBond distributions on ladder shares; IBTM 1,142 of 4,503) | W4, typed |
| H-M | IBTM, IBTO, IBTP, IBTQ, IBTR, VT prices | W2, typed |
| N-R | T37-T41 clean prices per 100 | W2, typed |
| S | bond accrued interest total (0 if WInS shows none) | W2/W4 |
| T | ladder value | `=1142*Hr+1024*Ir+927*Jr+894*Kr+853*Lr+200*Nr+200*Or+180*Pr+180*Qr+200*Rr+Sr` |
| U, V | IBTM floor value, VT value | `=3361*Hr`, `=167*Mr` |
| W | check against the WInS total (near 0; the difference is accrued interest or price timing) | `=Tr+Ur+Vr+Fr-Er` |
| X | PV of the ten $50,000 payments | helper sheet total, pasted |
| Y, Z, AA | ladder index, payments index, tracking ratio | `=100*AHr/AH$2`, `=100*Xr/X$2`, `=100*(AHr/Xr)/(AH$2/X$2)` |
| AB | VT index | `=100*Vr/V$2` |
| AC, AD | 2y and 10y par yields | treasury.gov, typed |
| AE | cumulative ladder income | `=SUM(G$2:Gr)` |
| AF | WInS return vs $300k (for the record only, never a Laura figure) | `=Er/300000-1` |
| AG | events and notes (coupons, distributions, Fed, anything odd) | typed |
| AH | ladder plus its income | `=Tr+AEr` |

**Helper sheet.** Type the close date and the 5y, 7y, 10y and 20y par yields. For each holding: years
t = (end date − close date)/365.25; the yield is interpolated between the two bracketing tenors (pre-filled, valid for every
close from 19 Oct to 3 Dec); PV = 50,000/(1+y/200)^(2t). The total goes into column X.

**Rules.** Capture after the US close. Name screenshots `YYYY-MM-DD_ET_<screen>.png` and crop the username and account number.
Have a second student check every typed value. Keep the back-fill rows (`c4_wins_backfill_8-19Oct.csv`) on a separate tab
labelled "back-filled, public data, AI".

---

## 8. Re-running on the 6 Nov close (rates analyst + checker)

1. Download the treasury.gov November CSV. Check the 6 Nov row exists.
2. From the folder, run with `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I`:
   1. `scripts/refresh_oct20.py <curve.csv> <2026.csv> <out.csv>` (add the date to its `days` list).
   2. `ips_numbers_oct19.py`, with CURVE_CSV, CURVE_DATE, ANCHOR_COST = the new basis-D cost, and OUT_JSON set.
   3. `scripts/coupon_options.py <curve> 11/06/2026 scripts/fred_GS10_monthly.csv data/shiller_monthly.csv <dir>` (NPATHS=100000).
   4. Fetch new closes into `data/prices/`.
   5. In `scripts/charts_data.py`, change `CURVE`/`DAY`, then run `scripts/charts_data.py <folder>`.
3. A student re-derives the simple C1 total, the C2 middle row and the C3 one-rung table by hand, and checks they are within a
   few dollars of the CSVs (19 Oct checks: $298,641; $169,686; $3,018).

**Verification done here (19 Oct).**
- The basis A-E costs are identical to the parallel numbers desk (`oct20/numbers/ladder_cost_by_basis_6-19Oct.csv`). The 16 Oct
  rows reproduce the 19 Oct synthesis exactly ($298,940 / $1,060).
- The number-sheet JSON is identical to `oct20/numbers/data/sheet/s19_D.json` (top p50 $167,229, inside 0.9933).
- The 100,000-path coupon study matches `oct20/numbers/coupon_options_comparison_19Oct.csv` (option 1: p_miss 0.1558, top $166,996).
- The deterministic shortfalls match the study's own fixed-path output ($9,537 / $18,952 / $27,718).
- The book total for 16 Oct matches $304.4k.
- An independent recomputation gave the same simple total ($298,641), C2 middle row, annuity ($405,391) and coupons ($1,538.75).

**Limits (MODEL).**
- Rates move in parallel only.
- iBond funds are modelled as par bonds ending 15 Dec, ignoring the 0.07% fee and monthly payouts.
- The VT returns in C2 are illustrative.
- The bottom rule's $3,700 allowance is the model's choice, not a decision.
- WInS coupon crediting and accrued-interest treatment are UNVERIFIED.

---

## 9. Files

- Pack: `P/charts_data_pack.md`.
- C1: `P/c1_payment_map.csv`, `P/c1_cash_flow_timeline.csv`.
- C2: `P/c2_range_scenarios.csv`, `P/c2_range_model_distribution.csv`.
- C3: `P/c3_shortfall_and_cover.csv`, `P/c3_rungs_at_minus2.csv`, `P/c3_one_rung_rebuild_Nov2041.csv`.
- C4: `P/c4_wins_backfill_8-19Oct.csv`.
- C5: `P/c5_plan_composition.csv`, `P/c5_wins_vs_plan_mapping.csv`.
- Template: `P/wins_tracking_template.csv`, `P/wins_tracking_pv_helper.csv`.
- Scripts: `P/scripts/charts_data.py` and `P/scripts/tracking_template.py` (new); `refresh_oct20.py` (copied plus one date);
  `ips_numbers_oct19.py`, `coupon_options.py`, `indep_pricer.py`, `book_value.py`, `v5_*` (copied unchanged).
- Data: `P/data/` (curves, prices, `sheet_19oct_D.json`, `sheet_19oct_E.json`, `coupon19_100k/`, `ladder_cost_by_basis_6-19Oct.csv`,
  `v5_*_out.txt`); iShares pages in `P/web/`.
