# Numbers refresh on the 19 Oct close (built Tue 20 Oct 2026, 08:40-09:00 Sydney)

> **Verified 20 Oct (`oct20/verify_infl_num/verify_infl_num.md`): every headline figure reproduced within $0-17, except one.** The coupon-study gap on holdings' dates is **$10,095 / $19,488 / $28,234 / $40,247** for 1/2/3/4.5-point falls (not $9,537 / $18,952 / $27,718 / $39,759): `coupon_options.py:141` paid iBond rungs at their own yield while sizing them at the par coupon ($580 phantom income). Knock-ons: option 1 short 16.2% / 30.4% (history); 3r unchanged; the 3r 1980s path passes the $135k bottom by only $185. `scripts/coupon_options.py` is now the patched version (original kept as `coupon_options_orig_bug141.py`), so `run_all.sh` gives consistent numbers. Add: basis E uses a different interpolation ($294,556 / 34.0% on the A-D method); every basis carries ~±$500 curve-method uncertainty (Treasury uses monotone convex) - quote no level. Odds of crossing $300k at either the 20 or 21 Oct close: 6.5-15.6%, about 1 in 8. WInS bond prices update once daily at the US open, so the WInS screen may differ by a few hundred dollars. For cross-model agreed shortfall odds use `oct20/reconcile3r/reconcile_3r.md` §5. **Consistency fix 20 Oct (packaudit §1d):** 3r = about 0.6% short on the agreed engine (0.08/0.32/0.72% marked at market); never quote 0.02%. The WInS scale factor is about 0.644, never 0.667 (300/450). The "7.5%" at :217 (net of waiting-cash interest) is retired: never quote it.


**AI-generated MODEL numbers (Claude Code) for Team Caplet. Not text to submit.** This file has numbers, checks and lists of stale figures. It drafts no TNA, IPS or Final Report wording. If a student uses any figure, they must re-check it themselves and log the AI help (Wharton AI Policy: "If you use AI to assist you in any way during the competition, how you use it must be recorded in your Works Cited pages", https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). MODEL = a computer estimate, not a fact. UNVERIFIED = nobody could confirm it.

**Folder:** `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/numbers/` (written `oct20/numbers/` below). `oct19/` is the same scratchpad's `oct19/` folder.

---

## 0. The short version

1. **Mon 19 Oct is published; Tue 20 Oct is not.** Long yields rose about 0.06 points on 19 Oct (10y 5.09 → 5.15). The ladder got about $1,780 cheaper in one day.
2. **On the cautious holdings basis (D), the ladder now costs $297,162: $2,838 under $300k, a 0.098-point fall** (16 Oct: $298,940 / $1,060 / 0.036). The odds it costs more than $300k on 1 Jan are now **41%** (38-43% for any volatility from 0.71 to 1.2 points a year), down from 47%. On payment dates (A) it is $293,001 and 30%.
3. **The coupon study's own sizing now prices the ladder at $298,446, $1,554 under $300k** (16 Oct: $300,174, $174 over). So its claim that the IBTR note's "her first $300,000 is enough" is "already false on this basis" no longer holds on the 19 Oct close. Option 4's median minimum rises from $140k to $145k. Every option keeps its rank. 3r ($10k in the Nov-2041 bond) is still short in 0.02% of model paths and in 0 of 690 history windows.
4. **Floor:** IBTM bought in Jan 2028 to repay $150k now costs $116,485 (forward yield 5.12%), which leaves $33,515 for VT. A half-point fall before January would cut the floor to about $138k (D), not "about $136k". The $145k bottom now survives to 2031 in 61-72% of paths (was 56-67%). The coupon gap barely moved: a 2-point permanent fall costs $21.3k (E) or $19.0k (holdings' dates).
5. **WInS book: about $303.4k (+1.13%) at the 19 Oct close** with accrued interest; about $301.9k without. The bonds are MODEL prices. That is down $1.0k from 16 Oct. Clean P&L is +$3,211, and VT (−$287) is still the only loser. **The room is now one to two days' normal move** (daily standard deviation about $1.6k). So the rule from 19 Oct stands: quote no level in the TNA or IPS. State the rule.

---

## 1. Inputs and reproduction checks

- **Curve.** treasury.gov daily par yield curve, October 2026 file, fetched 19 Oct 2026 at 21:38 UTC (Tue 20 Oct 08:38 Sydney = Mon 19 Oct 17:38 ET). It was re-fetched at about 21:52 UTC and was identical.
  - URL: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv
  - The 2026 full-year file is from the same site (`.../daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv`).
  - Copies: `oct20/numbers/data/raw/tsy_202610_fetch20oct.csv` and `tsy_2026_fetch20oct.csv`; the working copies are `data/tsy_202610.csv` and `data/tsy_2026.csv`.
- **New row:** 10/19/2026 = 1y 4.50, 2y 4.77, 3y 4.85, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48. 3-month bill 4.27.
  - 16 Oct was 4.46 / 4.74 / 4.82 / 4.89 / 4.98 / 5.09 / 5.47 / 5.43.
  - 6 Oct was 4.46 / 4.79 / 4.88 / 5.03 / 5.15 / 5.27 / 5.68 / 5.64.
- **No revisions:** every earlier October and 2026 row is byte-identical to the 19 Oct fetch (`diff` of sorted files; only the 10/19 line is new).
- **20 Oct is not published** (checked twice). Expect it after the US close on Tue 20 Oct, about Wed 21 Oct morning Sydney (timing UNVERIFIED). Re-run with `sh oct20/numbers/scripts/run_all.sh 10/20/2026` (about 2 minutes). It prints "not published yet" until the row exists.
- **Scripts.** Every script in `oct19/numbers/scripts` and `oct19/coupon/scripts` was copied to `oct20/numbers/scripts/`. The shared files (indep_pricer, reconcile, ips_numbers_oct19, refresh_oct19, v5_*) were identical in both folders.
  - Changes are limited to dates and day lists. `refresh_oct20.py` and `v5_live_checks_oct20.py` add 10/19, and refresh also takes `EXTRA_DAYS`. `book_value_oct20.py` values at the 19 Oct close with 20 Oct settlement. `book_series_oct20.py` adds 10/19.
  - New helpers: `anchor_table.py`, `days_over.py`, `daily_moves.py`, `v5_stress_oct20.py` and `run_all.sh`.
- **Reproduction (check 1).** On the 16 Oct curve:
  - The coupon model (`coupon_options.py`, 100,000 paths) reproduces `oct19/coupon/coupon_options_comparison.csv` exactly: `diff` is empty.
  - The number sheet reproduces `oct19/numbers/data/sheet_results_16oct.json` on every key. The only difference is the added `meta.anchor_cost` field.
  - `refresh_oct20.py` gives the same 6-16 Oct rows as `oct19/numbers/data/refresh_out.txt`. One exception: the 63-day realised-vol odds move by 0.001, because the window now ends 19 Oct.
- **Independent cross-checks (check 2), 19 Oct:**
  - The from-scratch pricer (`indep_pricer.py`) gives payment dates forward $292,908 (A $293,001), holdings forward $296,307 (C $296,399) and holdings unchanged $297,158 (D $297,162). That is within $4-93, the same known interpolation gap as on 16 Oct.
  - The number sheet's own bootstrap headline is $292,993.
  - The five T-bond model prices were also re-priced by simple yield-to-maturity at interpolated par yields. They agree within 0.04-0.28 per 100, about $100 on the whole bond sleeve (script run inline; output in this file only).
  - The ETF values were re-multiplied by hand: 4,503 × $21.865 = $98,458; 167 × $157.11 = $26,237.

---

## 2. The five-basis ladder table, 6-19 Oct (cost on 1 Jan 2027 / room under $300k / yield fall that uses it up)

Bases, as defined on 19 Oct (`oct19/numbers/findings.md`):
- **A:** payment dates, forward.
- **B:** payment dates, yields unchanged.
- **C:** holdings' maturity dates, forward; waiting cash earns 0%.
- **D:** holdings' dates, yields unchanged. This is the most cautious basis, and the IBTR note's "about 0.2".
- **E:** coupon basis. Real coupons; each rung is sized to deliver $50k with income reinvested at its own yield.

| Close | A | B | C | D | E |
|---|---|---|---|---|---|
| 6 Oct | $288,938 / $11,062 / 38bp | $290,005 / $9,995 / 34bp | $292,388 / $7,612 / 26bp | $293,453 / $6,547 / 23bp | $290,606 / $9,394 / 32bp |
| 7 Oct | $288,519 / $11,481 / 39bp | $289,599 / $10,401 / 36bp | $291,988 / $8,012 / 28bp | $293,066 / $6,934 / 24bp | $290,293 / $9,707 / 33bp |
| 8 Oct | $290,358 / $9,642 / 33bp | $291,360 / $8,640 / 30bp | $293,805 / $6,195 / 21bp | $294,805 / $5,195 / 18bp | $292,008 / $7,992 / 27bp |
| 9 Oct | $289,902 / $10,098 / 35bp | $290,881 / $9,119 / 31bp | $293,345 / $6,655 / 23bp | $294,321 / $5,679 / 20bp | $291,488 / $8,512 / 29bp |
| 13 Oct | $290,994 / $9,006 / 31bp | $291,878 / $8,122 / 28bp | $294,412 / $5,588 / 19bp | $295,295 / $4,705 / 16bp | $292,469 / $7,531 / 26bp |
| 14 Oct | $291,758 / $8,242 / 28bp | $292,590 / $7,410 / 25bp | $295,163 / $4,837 / 17bp | $295,993 / $4,007 / 14bp | $293,123 / $6,877 / 24bp |
| 15 Oct | $294,461 / $5,539 / 19bp | $295,246 / $4,754 / 16bp | $297,847 / $2,153 / 7bp | $298,628 / $1,372 / 5bp | $295,828 / $4,172 / 14bp |
| 16 Oct | $294,779 / $5,221 / 18bp | $295,559 / $4,441 / 15bp | $298,163 / $1,837 / 6bp | $298,940 / $1,060 / 3.6bp | $296,189 / $3,811 / 13bp |
| **19 Oct** | **$293,001 / $6,999 / 24bp** | $293,767 / $6,233 / 21bp | $296,399 / $3,601 / 12bp | **$297,162 / $2,838 / 9.8bp** | **$294,437 / $5,563 / 19bp** |

Source: `oct20/numbers/ladder_cost_by_basis_6-19Oct.csv` (every column, including DV01 and odds); `data/refresh_out.txt`; `data/reconcile_out_19oct.txt`.

- **One-day move, 16 → 19 Oct:** −$1,778 on A and −$1,777 on D. Yields rose 5-6bp along the curve.
- **DV01 on 19 Oct:** $288-291 per 0.01 point (about $290, unchanged).
- **How big a day is** (`data/daily_moves_out.txt`, 2026 to 19 Oct, basis D):
  - The daily change has a standard deviation of $1,365 over the year and $1,616 over the last 21 days.
  - The median absolute change is $944.
  - The biggest one-day move this year was −$4,539 (20 Mar).
  - A move bigger than today's $2,838 room happened on 4% of days.
  - So **the room is about 1.75 typical recent days**. Any dollar level quoted on Thu 22 Oct will already be stale.
- **Days in 2026 when the ladder cost more than $300k** (`data/days_over_out.txt`):
  - **D: 182 of 200** (under every day since 23 Sep);
  - **A: 173 of 200** (under since 10 Sep);
  - **E: 174 of 200** (under since 18 Sep).
  - The 2026 low was 5 Oct: A $287,948 / D $292,466 (`data/ladder_cost_2026_daily_A_D.csv`).
- **IBTR note trail on its own basis (D):** 6 Oct $293,453 (room 0.23 points), 16 Oct $298,940 (0.04), **19 Oct $297,162 (0.10)**. The note's "about 0.2" test was not crossed at any published close.

---

## 3. Odds the 1 Jan 2027 cost exceeds $300k (MODEL)

Method: as on 19 Oct (`refresh_oct20.py`). The curve shifts in parallel by a normal amount over the 0.20 years to 1 Jan, with full repricing to the break-even shift.
- Realised 10-year volatility in 2026 is 0.71 points a year (0.76 over the last 63 days), unchanged.
- The number sheet's own assumption is 1.0 points a year.

| Basis | σ 0.71 (2026) | σ 0.76 (63 days) | σ 0.8 | **σ 1.0 (sheet)** | σ 1.2 | 16 Oct at σ 1.0 |
|---|---|---|---|---|---|---|
| A | 22.7% | 24.4% | 25.4% | **29.8%** | 33.0% | 35.0% |
| B | 25.3% | 26.8% | 27.8% | 31.9% | 34.7% | 37.2% |
| C | 34.8% | 35.9% | 36.5% | 39.1% | 40.9% | 44.5% |
| D | 37.9% | 38.8% | 39.3% | **41.4%** | 42.8% | 46.8% |
| E | 27.6% | 29.0% | 29.9% | **33.7%** | 36.3% | 38.9% |

- **Cross-check (the number sheet's own Monte Carlo, 200,000 paths, anchored to each basis):** A 31.6%, E 35.2%, C 40.3%, D 42.4% (`data/anchor_comparison_19oct.txt`). These agree with the table within 1-2 points.
- **Odds the line is crossed before the TNA goes in** (new; MODEL). The team target is Thu 22 Oct evening Sydney. The last closes it can see then are 20 Oct and perhaps 21 Oct, so this covers 1-2 trading days on D. A 0.098-point fall is needed:
  - 1 day: 1.4-6.0%;
  - 2 days: 6.1-13.6% (σ 0.71 to 1.0);
  - empirical dollar volatility, 2 days: 10.7%.
  - **About 1 in 10.** So the "wording ready for either outcome" advice still applies, but "probably not crossed by Thursday" is the likely case.

---

## 4. Floor, 2031 range and VT (19 Oct curve, MODEL)

### 4a. Floor (IBTM bought Jan 2028)

From `data/v5_floor_range_out.txt` and `data/v5_live_checks_out.txt`.

| Item | 16 Oct | **19 Oct** |
|---|---|---|
| Forward yield for IBTM (Jan 2028 to Dec 2032) | 5.06% | **5.12%** |
| Cost in Jan 2028 to repay $150k | $116,830 | **$116,485** |
| Left for VT (no top-up, no leftover) | $33,170 | **$33,515** |
| Floor paid if reinvestment yields fall for good by 1 / 2 / 3 / 4 points | $149,187 / $148,393 / $147,619 / $146,864 | **$149,179 / $148,378 / $147,596 / $146,834** |
| Floor after a half-point fall before January (A / B / C / **D** / E) | $140.2k / $139.4k / $136.9k / **$136.1k** / $138.8k | $142.1k / $141.3k / $138.8k / **$138.0k** / $140.6k |

**Number sheet** (`data/sheet/s19_*.json`; anchored A → D):
- Floor paid p1/p5/p50: $121.5k / $132.3k / $149.5k (A) to $116.8k / $127.8k / $149.2k (D).
- VT on 2 Jan 2028 p5/p50/p95: $20.8k / $32.6k / $42.9k (A) to $20.3k / $32.3k / $42.8k (D).

### 4b. 2031 range and 2033 gift

| Item | Anchored A | E | C | **D** | 16 Oct (A to D) |
|---|---|---|---|---|---|
| Chance the bottom is still $145k in 2031 | 71.5% | 68.0% | 63.1% | **61.1%** | 67.2% to 56.3% |
| Top of range p5 / p50 / p95 | $146.7k / $168.3k / $184.3k | $145.0k / $168.0k / $184.1k | $142.6k / $167.4k / $183.9k | $141.7k / $167.2k / $183.8k | $144.4k / $167.7k / $183.8k to $139.4k / $166.4k / $183.3k |
| Gift p5 / p50 / p95 | $144.3k / $167.5k / $183.3k | $142.5k / $167.1k / $183.2k | $140.2k / $166.6k / $183.0k | $139.3k / $166.4k / $182.9k | $141.9k / $166.9k / $182.9k to $136.9k / $165.6k / $182.3k |
| Gift inside the range | 99.46% | 99.41% | 99.36% | 99.33% | 99.40% to 99.25% |
| Gift at the top (within $1k) | 76.3% | 76.1% | 75.9% | 75.8% | 76.1% to 75.6% |
| Payment-cover chain fails (shortfall above leftover + Laura's half) | 6.5% | 7.0% | 7.7% | 8.0% | 7.2% to 8.75% |
| Post-2033 gap exceeds what Laura kept / same if kept in VT to 2042 | 5.8% / 5.2% | 6.2% / 5.6% | 6.9% / 6.1% | 7.1% / 6.3% | 6.4-7.7% / – |
| Median gap when it happens | $3,111 | $3,146 | $3,169 | $3,167 | about $3.2k |
| Laura keeps in 2033: p5 / median | $0 / $29.5k | $0 / $28.0k | $0 / $26.2k | $0 / $25.6k | $0 / $27.5k to $24.0k |

- **The $145k rule is unchanged.** The bottom is $145k only if the 1 Jan 2027 ladder costs under about $301,300 (bottom = (R − $3,700) rounded down to $5k, so R ≥ $148,700). Its survival odds rose only because the room grew.
- **Dreamy-planck method** (2027 leftover put into VT, floor stressed −2 points). The range "today" is $145,000 to:
  - $166,757 with no leftover;
  - $168,176 with the D leftover;
  - $170,257 with the A leftover.
  - The gift is below $145k in 0.000% of paths and at the cap in 59-62% (16 Oct: $167.1k-$169.2k).
- **40% stock fall during 2032** (`data/v5_stress_out.txt`). The typical gift goes:
  - **$170.5k → $163.2k** at the 19 Oct floor cost (16 Oct: $170.3k → $163.0k);
  - $170.0k → $162.8k on the number-sheet median (A); $169.8k → $162.7k on the median (D).
  - V5's "$169k → $162k" is still fine as rounding.
- **Typical Jan 2028 split** (number sheet): 66.5% payment Treasuries / 24.4-24.7% floor / 1.2% leftover / 6.9-7.0% VT, of about $465k. On 16 Oct it was 66.9 / 24.4-24.6 / 0.8 / 6.8-6.9. Leftover rises with the room.

### 4c. Required return and ladder yield (`data/v5_live_checks_out.txt`)

- **Required return on $300k: 5.087% a year** (5.024% semiannual). This is case-derived and does not change.
- **Ladder IRR on 19 Oct:**
  - D 5.186% (5.120% semiannual);
  - C 5.213%;
  - E 5.282%;
  - A 5.333%.
- **Margin over the required return:** **0.10-0.13 points on D/C** (16 Oct: 0.03-0.06), or 0.10 on the semiannual convention.
- V5's "Treasuries currently yield about 5.15%" now equals the 19 Oct **10-year par yield** by coincidence. It is still an undated figure, and it is not the ladder yield.

---

## 5. Coupon-reinvestment shortfall (19 Oct)

| Yields fall for good by | Number sheet (payment-date sizing, E-type) | Coupon study (holdings' dates, waiting cash at 0%) | 16 Oct (sheet / study) |
|---|---|---|---|
| 1 point | $11,005 | $9,537 | $10,952 / $9,490 |
| **2 points** | **$21,287** | **$18,952** | $21,185 / $18,854 |
| 3 points | $30,902 | $27,718 | $30,753 / $27,572 |
| 4.5 points | $43,731 | $39,759 | $43,509 / $39,549 |
| 0% reinvestment (dreamy-planck `v5_figures`) | $50,691 | – | $49,960 |

- **Dreamy-planck's 2-point figure:** $21,526 (16 Oct $21,422).
- **Number sheet Monte Carlo:** p95 $25.6k, p99 $33.3k. **History replay** (701 start months since 1953): p95 $22.4k, worst $39.0k (June 1984 start).
- **Coupon study:** model 1-in-20 $21.3k, 1-in-100 $28.4k; history worst $37.1k (July 1984 start). Proportional replay worst $19.6k (June 2007).
- **The rest of the coupon study's outputs:**
  - Gap upside: interest on waiting cash at the 4.27% bill rate is worth $4,492.
  - Curve held flat with roll-down: $1,627 short.
  - Share of the raw shortfall visible by Jan 2033: 1.00.
  - Source: `data/coupon19/extra_checks_out.txt`, `coupon_options_results.json`.
- **Verdict:** every figure moved by $50-730, so this table stays close to 16 Oct's. "About $21,000 (E) / about $19,000 (holdings' dates)" still holds. Always name the basis.

---

## 6. Coupon-option table on the 19 Oct curve (options 1 / 2 / 3r / 4)

Same model, same basis definitions as `oct19/coupon/coupon_risk_options.md` §"The basis", with the curve date changed to 19 Oct. 100,000 paths, plus 690 history windows (start months Apr 1953 to Sep 2010).

**The study's own ladder cost on 19 Oct: $298,446, room $1,554.** On 16 Oct it was $300,174, $174 over. Rung faces:

| Rung | Face |
|---|---|
| IBTM | $37,287 |
| IBTO | $35,375 |
| IBTP | $33,562 |
| IBTQ | $31,821 |
| IBTR | $30,144 |
| Feb-37 | $30,282 |
| May-38 | $29,471 |
| Nov-39 | $27,743 |
| Nov-40 | $26,785 |
| Nov-41 | $29,302 |

Use this cost only to compare options with each other.

Files: `oct20/numbers/coupon_options_comparison_19Oct.csv`; full grids in `data/coupon19/` (`coupon_options_summary.csv`, `coupon_options_named_paths.csv`, `coupon_options_results.json`).

| (correlation 0) | 1 State only | 2 Laura's half in VT to 2042 | **3r $10k in Nov-2041 bond** | 4 Dedicated rebuild | 16 Oct (1 / 2 / 3r / 4) |
|---|---|---|---|---|---|
| Chance a payment is short (model / history) | 15.6% / 29.3% | 1.3% / 0.0% | **0.02% / 0.0%** | 0.0% / 0.0% | 16.4/31.4; 1.4/0.0; 0.02/0.0; 0/0 |
| Size if short: 1-in-100 / model worst / history worst | $3.0k / $6.2k / $2.9k | $0.7k / $11.8k / $0 | **$0 / $0.6k / $0** | $0 / $0 / $0 | 3.0/6.1/2.9; 0.9/11.5/0.1; 0/0.7/0; 0 |
| Same, net of interest on waiting cash | 7.1% short | 0.8% | 0.0% | 0.0% | 7.5% / 0.9% / 0 / 0 |
| Coupon shortfall before cover: 1-in-20 / 1-in-100 / history worst | $21.3k / $28.4k / $37.1k | same | same | $5.0k / $6.9k / $10.0k | 21.2/28.2/36.7; 4: 5.0/6.9/9.9 |
| 2031 minimum (median) | $145k | $145k | **$135k** | **$145k** (was $140k) | 145 / 145 / 135 / **140** |
| 2031 top (median) | $167.0k | $167.0k | $165.8k | $166.3k | 166.1 / 166.1 / 164.9 / 165.3 |
| 2033 gift: median / 1-in-20 | $166.2k / $138.8k | $166.2k / $138.8k | **$163.3k / $136.7k** | $165.5k / $140.7k | 165.3/135.8; same; 162.2/133.9; 164.4/138.0 |
| Gift below the announced minimum (model / history) | 1.95% / 2.6% | 1.95% / 2.6% | **0.06% / 0.4%** | 0.01% / 0.0% | 2.1/2.8; 2.1/2.8; 0.05/0.9; 0.0/0.0 |
| Same with the net-minimum rule | 0.54% | 0.54% | 0.0% | 0.0% | 0.59% / 0.59% / 0 / 0 |
| Laura's free money 2033 (median) / back in 2042 | $20.5k / $8.0k | $0 / $51.1k | $20.5k / $19.9k | $21.6k / $9.0k | 19.9/7.0; 0/49.1; 20.1/18.7; 21.1/7.9 |
| Correlation +0.5: short / worst / gift 1-in-20 / below minimum | 15.6% / $6.2k / $137.0k / 2.9% | **1.9% / $12.6k** / $137.0k / 2.9% | 0.02% / $0.6k / $136.2k / 0.08% | 0% / $0 / $140.7k / 0.01% | option 2 was 2.0% / $12.2k |
| Dedicated ladder cost | – | – | – | $300,439 (+$1,993) | $302,116 (+$1,942) |

**Option 3b ($10k in IBTM)** for reference: short 4.6% (model) / 9.3% (history); minimum $135k; gift median $155.0k.

**Buffer size, option 3r (reserve from the 2028 deposit):**

| Reserve | Short (model / history) | Minimum | Top | Gift median 3r (3a, no release) | Gift 1-in-20 3r (3a) | Gift below min | Same in IBTM (3b) |
|---|---|---|---|---|---|---|---|
| $0 (option 1) | 15.6% / 29.3% | $145k | $167.0k | $166.2k | $138.8k | 1.95% | – |
| $5k | 1.6% / 2.9% | $140k | $166.4k | $163.8k ($160.6k) | $138.3k ($135.9k) | 0.47% | 9.4% short |
| **$10k** | **0.02% / 0%** | **$135k** | **$165.8k** | **$163.3k ($155.0k)** | **$136.7k ($131.5k)** | **0.06%** | 4.6% short |
| $15k | 0% / 0% | $130k | $165.2k | $163.2k ($149.5k) | $135.2k ($126.4k) | 0.01% | 1.7% short |
| $20k | 0% / 0% | $125k | $164.6k | $163.1k ($143.9k) | $134.5k ($120.9k) | 0% | 0.4% short |
| $25k | 0% / 0% | $120k | $164.0k | $162.8k ($138.3k) | $134.6k ($115.4k) | 0% | 0.04% short |

$10k is still the smallest reserve with no modelled payment shortfall in history.

**Named paths (gift vs minimum; payments covered unless stated):**

| Path | Coupon short | 1 and 2 | 3r $10k | 4 | Change vs 16 Oct |
|---|---|---|---|---|---|
| 2008 (Jan 2007 start) | $14.3k | $163.6k vs $145k | $154.9k vs $135k | $163.1k vs $145k | 4: minimum now $145k |
| 2020 (Jan 2019 start) | $0.7k | $167.5k vs $145k (option 1 no longer short; was $48) | $166.3k vs $135k | $167.0k vs $145k | small |
| 1980s absolute (Jun 1984) | $36.7k | **$114.0k vs $145k (broken)**; net-minimum rule cuts the announced minimum to $120k | **$136.2k vs $135k: now passes, by $1.2k** ($20k: $141.5k vs $125k) | $159.0k vs $145k | **3r flips from broken by $3.5k to passing by $1.2k** |
| 1980s proportional | $16.7k (option 1 short $751) | $170.3k vs $145k | $166.6k vs $135k | $169.8k vs $145k | small |
| Storm (yields −3 pts by 2029; VT −50% in 2032) | $22.9k | **$144.3k vs $145k (broken, by $0.7k)**; rule cuts the minimum to $140k | $146.7k vs $135k | $156.8k vs $145k | 1 and 2: broken by $0.7k (was $3.7k); 4's minimum was $140k |

**What changes in the conclusions:**
1. **Nothing about the ranking.** 3r is still the only option that makes payments near-certain without stocks, trades or conflicts with filed notes. Option 4 still has the best raw numbers.
2. **Two "knife-edge" results flipped** with a $1,728 move in the study's ladder cost. They will flip back if yields fall about 6bp.
   - (a) Option 4's minimum, $140k → $145k. It depends on whether the dedicated ladder costs above $301,300.
   - (b) 3r in the 1980s absolute path, broken → passing. It turns on about $1.5k of 2027 leftover.
   - **Do not cite either as a property of the option.** Cite them as "within a few thousand dollars of the line".
3. **The IBTR note's "her first $300,000 is enough"** is true on every basis on the 19 Oct close, including the study's stricter sizing ($298,446).
4. **WInS reserve size for 3r.** About $6.7k at scale 0.667. The Nov-2041 bond is now about $778 a bond, dirty: model clean 76.965 + fill gap −0.552 + accrued 1.342. So about 8-9 bonds, against "about 8 at about $783" on 16 Oct. Yield-check the WInS price first (UNVERIFIED).

---

## 7. WInS book value, 19 Oct close

- **ETF prices:** Yahoo Finance daily closes for 19 Oct, `query1.finance.yahoo.com/v8/finance/chart/<ticker>?range=1mo&interval=1d&events=div`, fetched 19 Oct 21:45 UTC. regularMarketTime is 20:00 UTC = 16:00 ET. Saved in `data/prices/`.
- **T-bonds:** MODEL. The 19 Oct curve, plus each bond's model-vs-fill gap at the 7 Oct fills, plus accrued interest to 20 Oct settlement.
- **Holdings and fills:** as in `oct19/numbers/scripts/book_value.py` (from snap/main `keel/routines/tasks/portfolio_check.py`).
- **Cash:** $3,513.79, as WInS reports it. The reconciliation is disputed.

| Holding | Units | Fill | 19 Oct price | Value | P&L vs fill | 16 Oct value |
|---|---|---|---|---|---|---|
| IBTM | 4,503 | 21.65 | 21.865 | $98,458 | +$968 | $98,728 |
| IBTO | 1,024 | 22.86 | 23.135 | $23,690 | +$282 | $23,767 |
| IBTP | 927 | 23.90 | 24.235 | $22,466 | +$311 | $22,549 |
| IBTQ | 894 | 23.46 | 23.85 | $21,322 | +$349 | $21,411 |
| IBTR | 853 | 23.24 | 23.651 | $20,175 | +$351 | $20,259 |
| VT | 167 | 158.83 | 157.11 | $26,237 | −$287 | $26,189 |
| T 4.750% Feb-2037 (20) | MODEL | 96.019 | 96.69 + gap | $19,585 | +$210 | $19,675 |
| T 4.500% May-2038 (20) | MODEL | 93.076 | 93.85 + gap | $19,238 | +$237 | $19,335 |
| T 4.375% Nov-2039 (18) | MODEL | 90.005 | 91.57 + gap | $16,780 | +$241 | $16,874 |
| T 4.250% Nov-2040 (18) | MODEL | 87.724 | 89.52 + gap | $16,378 | +$259 | $16,474 |
| T 3.125% Nov-2041 (20) | MODEL | 74.955 | 76.97 + gap | $15,551 | +$292 | $15,654 |
| Cash | | | | $3,514 | | $3,514 |
| **Total** | | | | **$303,393 (+1.13%)** | **+$3,211 clean** | $304,429 (+1.48%) |

Sources: `oct20/numbers/wins_book_value_19Oct.csv`; `data/book_value_out.txt`.

- **Without accrued interest:** $301,902. Whether WInS counts accrued interest is UNVERIFIED. Coincidence: CLAUDE.md's "~$301.9k" now matches this ex-accrued model figure. It was written for an earlier date, so it still needs a date beside it.
- **By day** (with accrued; `oct20/numbers/wins_book_value_series.csv`):

| Day | Value |
|---|---|
| 8 Oct | $301.8k |
| 9 Oct | $301.8k |
| 13 Oct | $302.3k |
| 14 Oct | $302.5k |
| 15 Oct | $304.3k |
| 16 Oct | $304.4k |
| **19 Oct** | **$303.4k** |

- **Weights now** (at cost): IBTM 32.45% (32.64%), VT 8.65% (8.84% of $300k), five T-bonds 28.9%, cash 1.16%.
  - Every weight is within about 0.2 points of its at-cost weight (largest gap: VT −0.19 to −0.23, depending on the denominator).
  - The iBond ETFs are 61.3% of the book. WInS's own "Long Equities" label figure is UNVERIFIED today.
  - Treasuries of all kinds are about 90.2%.
- **Distributions:** Yahoo shows the 1 Oct ex-date payouts (IBTM $0.070, IBTO $0.079, IBTP $0.083, IBTQ $0.082, IBTR $0.064 a share). That date came before the 7-8 Oct fills, so the book has received none. The next ex-date is probably early November (UNVERIFIED).
- **Trap (unchanged):** in Laura's real plan, falling yields make the January purchase dearer. WInS gains are not good news, and they never enter her projections.

---

## 8. The numbers card, refreshed (15 figures; 19 Oct close unless stated)

Golden rule unchanged: **say every number with its date and basis, or not at all. If unsure, state the rule, not the level.** Refresh again on the 6 Nov close. At the semifinal, use only the Final Report's own figures.

| # | Number | Date | Basis | Source | Trap |
|---|---|---|---|---|---|
| 1 | **$450,000 in, $500,000 out:** $300k (Jan 2027) + $150k (Jan 2028); ten fixed $50k payments, 1 Jan 2033-42 | Case | Nominal | case:43-45, 88-90 | Only the portfolio may fund the payments (case:91-92); time value matters |
| 2 | **5.09% a year required** on the 2027 deposit alone (5.02% semiannual) | Valued 1 Jan 2027 | Annual compounding | `data/v5_live_checks_out.txt:1` | Compare on one convention |
| 3 | **Ladder yields about 5.19% (D) to 5.21% (C): 0.10-0.13 points above the required return** (was 0.03-0.06 on 16 Oct) | 19 Oct | D / C, annual | `v5_live_checks_out.txt` | V5's "about 5.15%" is undated; on 19 Oct that is the 10-year par yield, not the ladder yield. The margin moves 0.07 points in one day |
| 4 | **Ladder costs $297,162; room $2,838 (9.8bp)** | 19 Oct close | D: holdings, yields unchanged to 1 Jan 2027 | §2 | 16 Oct was $298,940 / $1,060. A is $293,001. The room is about 1.75 typical days' moves, so never quote a level as current |
| 5 | **About $290 per 0.01 point** (DV01 $288-291) | 19 Oct | Parallel shift, full repricing | §2 | Per 0.01 point, not per point |
| 6 | **41% chance the ladder costs more than $300k on 1 Jan 2027** (A 30%, E 34%; 38-43% on D for σ 0.71-1.2) | 19 Oct | MODEL, σ 1.0 point a year | §3 | Was 47% on 16 Oct. "1 in 3" and "1 in 4" in team notes are other dates and bases |
| 7 | **In 2026 the ladder cost more than $300k on 182 of 200 trading days** (D; under every day since 23 Sep) | To 19 Oct | MODEL | `data/days_over_out.txt` | The "8.4% of days since 2000 / none 13 Jul 2007-23 Sep 2026" figure (R16 K7) was **not re-run**. "Cheapest since May 2002" stays UNVERIFIED |
| 8 | **About $21,000 short if reinvestment yields fall 2 points for good** ($11,005 at 1 point; $50,691 at 0%; MC p95 $25.6k; history p95 $22.4k, worst $39.0k). **About $19,000 on holdings' dates** | 19 Oct | E (sheet) / holdings' dates (coupon study) | §5 | Two bases give $19k and $21k. Name the basis. This is why "covered at purchase" is wrong for coupons |
| 9 | **Jan 2028 mix: 66.5% payment Treasuries / 24.5% floor / 1.2% leftover / 7.0% VT** | Typical path, 19 Oct | MODEL | §4b | WInS VT is 8.84% at cost (8.65% now). "About 9%" is WInS, "about 7%" is Laura |
| 10 | **Floor: $116,485 in Jan 2028 buys about $150,000 in IBTM** (forward yield 5.12%), leaving $33,515 for VT. A half-point fall before Jan 2027 cuts the floor to about **$138,000** (D) | 19 Oct | MODEL; D for the stress | §4a | "$136,000" was 16 Oct. "$150k" is a target, not owned; IBTM's payout is not fixed |
| 11 | **2031 range about $145k to about $167-168k** (median top). Gift inside the range 99.3-99.5% of paths, at the top about 76%. **The $145k bottom survives to 2031 in 61-72% of paths** | 19 Oct | MODEL, number sheet re-anchored A-D | §4b | Never quote "$145,000" as today's figure. It holds only while the January ladder costs under about $301,300. Range confidence is not payment certainty |
| 12 | **A 40% world-stock fall during 2032:** typical gift about $170.5k → $163.2k | 19 Oct | MODEL | `data/v5_stress_out.txt` | V5's "$169k → $162k" is fine as rounding |
| 13 | **Stocks assumed 7.00% a year, compound** (16.78% volatility), JPM 2026 LTCMA AC World | 30 Sep 2025 data | Compound, before inflation | CLAUDE.md Key facts | Not arithmetic, not real |
| 14 | **Inflation 2.5%:** the floor loses 11.6% of real value over 2028-33; the 2042 payment is worth about $40,000 in 2033 dollars | Computed | CALC | `v5_live_checks_out.txt` last line | Building costs are not the CPI (not re-checked today) |
| 15 | **WInS book about $303.4k (+1.13%); about $301.9k without accrued interest; 11 of 200 trades; cash $3,514** | 19 Oct (bond prices MODEL) | With accrued interest | §7 | It moves about $1k a day. WInS gains never enter Laura's projections. "$304.4k" was 16 Oct |

---

## 9. Which statements in the 19 Oct update and kits change

Line numbers are `grep -n` on the files as they stand. "Holds" means the statement is still true on 19 Oct, so no edit is needed.

### 9a. `oct19/out/Caplet_Update_19Oct2026.md`

| Line | Statement now | 19 Oct close | Action |
|---|---|---|---|
| 30 | "room ... almost gone": $298,940, $1,060, a 0.036-point fall; odds "about even (46-47%) for any volatility from 0.71 to 1.2" | $297,162, **$2,838, 0.098 points; 38-43%** (41% at σ 1.0) | Update the numbers. Keep "write the TNA so it is true either way" (about 1 in 10 chance of crossing by Thursday, §3) |
| 31 | 2-point fall "about $19-21k"; 3r "0.02%"; minimum "$145k to $135k" | $19.0-21.5k; 0.02%; $145k → $135k | Holds |
| 57 | "the cost moved $2.7k in one day, more than the room left" | The room ($2,838) is now just above October's largest one-day move ($2,635), but below 2026's largest ($4,539); 16→19 Oct moved $1.8k | Reword the reason; the rule (quote no level) holds |
| 143 | "the 10-year was 5.09% on 16 Oct, against 5.087% required" | 10-year **5.15%** on 19 Oct; ladder 5.19-5.21% | Add the date. V5's 5.15% now matches the 10-year by chance, so "undated" is still the fault |
| 154, 336 | "182 of 199 trading days" | 182 of 200 | Minor |
| 224-228 (table 6a) | A $294,779 / $5,221 / 18bp / 35%; B $295,559; C $298,163 / 45%; **D $298,940 / $1,060 / 3.6bp / 47%**; E $296,189 / $3,811 / 13bp / 39% | A $293,001 / $6,999 / 24bp / 30%; B $293,767 / 32%; C $296,399 / 39%; **D $297,162 / $2,838 / 9.8bp / 41%** (38-43%); E $294,437 / $5,563 / 19bp / 34% | Replace the row values |
| 234 | "$2.6-2.7k in one day (14 to 15 Oct)"; "182 of 199" | Add "16→19 Oct −$1.8k"; 182 of 200 | Minor |
| 235 | IBTR trail on D: $293,453 → $298,628 → $298,940 | Add **19 Oct $297,162 (room 0.10 points)** | Extend |
| 237-247 (6b) | "the study prices the ladder at **$300,174**, $174 over $300k" | **$298,446, $1,554 under** | Replace. The point stands: a different sizing method, for comparing options only |
| 255 | Ladder yield 5.12-5.15%, margin 0.03-0.06 | 5.19-5.21%, **margin 0.10-0.13** | Replace |
| 256 | Floor $116,830 at 5.06%, leaving $33,170; half-point fall → "about $135-136k" | **$116,485 at 5.12%, leaving $33,515; about $138k** | Replace |
| 257 | $145k bottom holds in 56% (D) to 67% (A) | **61% (D) to 72% (A)**; the $301.3k threshold is unchanged | Replace |
| 258 | Inside the range 99.25-99.4%; at the top 76% / 60-61%; option 1 gift below minimum 2.1% | 99.33-99.46%; 76% / 59-62%; 1.95% | Minor |
| 259 | $10,952 / $21,185 / $30,753 (E); $9.5k / $18.9k / $27.6k (holdings); history p95 $22.3k, worst $38.6k | $11,005 / $21,287 / $30,902; $9.5k / $19.0k / $27.7k; p95 $22.4k, worst $39.0k | Minor (stable) |
| 260 | Cover chain fails in 7-9%; option 1 short 16.4% | 6.5-8.0%; 15.6% | Minor |
| 261 | 66.9 / 24.6 / 0.8 / 6.9 | 66.5 / 24.4-24.7 / 1.2 / 6.9-7.0 | Minor |
| 265-266 | Book $304.4k (+1.48%), $302.9k ex-accrued; clean P&L +$4,257; VT −$336 | **$303.4k (+1.13%), $301.9k; +$3,211; VT −$287** | Replace |
| 285 (D0-4) | "Room is $1,060 on D (47% odds)" | **$2,838 (41%)** | Replace. The decision is unaffected: "sized for" still depends on the top-up rule |
| 301-311 (D1 table) | Option 1 16.4% / 31.4%; 4 minimum $140k; 3r gift $162.2k / $133.9k; 3r gift below minimum 0.05% / 0.9%; option 2 at +0.5: 2.0%, $12.2k | 15.6% / 29.3%; **4 minimum $145k**; 3r $163.3k / $136.7k; 0.06% / **0.4%**; 1.9%, $12.6k | Replace (see §6). The ranking holds |
| 316 | 3r "does not fully pass the 1980s absolute-yield path ... misses the $135k minimum by $3.5k (0.9% of history windows break the minimum)" | Passes by $1.2k on 19 Oct; 0.4% of windows break it | Re-word as "within a few thousand dollars of the line either way". Don't claim pass or fail |
| 319 | "about 8 more Nov-2041 bonds" | About 8-9 at about $778 | Minor |
| 330 (D4) | "$145k (holds in 56-67% ..." | 61-72% | Replace |
| 418 (11a item 10) | "about $135,000-136,000" | about $138,000 (D, 19 Oct) | Date it |

### 9b. `oct19/coupon/coupon_risk_options.md` (and `agent_final.md` summary line 1)

| Line | Now | 19 Oct | Action |
|---|---|---|---|
| agent_final:2 | "the ladder costs $300,174, which is $174 over" | $298,446, $1,554 under | Replace |
| 12 | "16 Oct ... 19 Oct was not yet published" | 19 Oct published; refresh in `oct20/numbers/data/coupon19/` | Note |
| 36-48 (table) | 16 Oct values | §6 values | Replace |
| 41, 50 | Option 4 minimum "$140k *"; footnote "pushes the 2028 top-up past a $5k rounding step" | **$145k**; the dedicated ladder ($300,439) is now under the $301.3k step | Drop the footnote or make it conditional |
| 54 | Gap interest: "16% to 7.5%" at 4.26% | 15.6% → 7.1% at 4.27% | Minor |
| 56-70 (buffer table) | 16 Oct | §6 buffer table | Replace; "$10k is the smallest" holds |
| 95-99 (named paths) | 1980s 3r "broken by $3.5k"; storm options 1/2 $141.3k vs $145k; option 4 vs $140k | 3r $136.2k vs $135k (passes); storm $144.3k vs $145k (broken by $0.7k); 4 vs $145k | Replace; flag both as knife-edge |
| 103 | Net rule: "2.1% to 0.6%" | 1.95% → 0.54% | Minor |
| 138-139 | Dedicated ladder $302,116 (+$1.9k) | $300,439 (+$2.0k); IBTP rung $22.0k | Minor |
| 155 | "about 8 more ... at about $783 each" | About 8-9 at about $778 | Minor |
| 159 | Option 4 "minimum $140k, gift 1-in-20 low $138.0k" | $145k; $140.7k | Replace |
| 168 | IBTR "her first $300,000 is enough ... **already false on this basis ($300,174)**" | **True on every basis on 19 Oct**, including this one ($298,446) | Remove "already false". The note is "true at 19 Oct, by $1.5-7.0k depending on basis" |
| 177 | "$9.5k/$18.9k/$27.6k; 1-in-20 $21.2k; history worst $36.7k" | $9.5k / $19.0k / $27.7k; $21.3k; $37.1k | Minor |
| 195-196 | Waiting-cash cushion "about $4.5k at 4.26%"; roll-down "$1.6k short" | $4.5k at 4.27%; $1.6k | Holds |

### 9c. `oct19/tnakit/tna_fact_kits.md` (live this week)

| Line | Now | 19 Oct | Action |
|---|---|---|---|
| 101 | Half-point fall → floor "about $136k" (D) | About $138k | Date it, or drop it: no floor figure goes in the TNA anyway (TNA:20-22) |
| 287 | Margin "only 0.03-0.06 points on 16 Oct" | 0.10-0.13 points on 19 Oct | Replace; still "date it if you use it" |
| 293-299 (2E table) | Last row 16 Oct $298,940 / $1,060 / 3.6bp | **Add 19 Oct $297,162 / $2,838 / 9.8bp** | Extend |
| 301-305 | "The same day on other bases (16 Oct)": A $294,779 / C $298,163 / E $296,189 | 19 Oct: A $293,001 / C $296,399 / E $294,437 | Replace |
| 306 | "par yields fell about 0.2 points 6 → 16 Oct ... The 19 Oct curve is not published yet" | 6 → 19 Oct: 10y 5.27 → 5.15, 20y 5.68 → 5.53, 30y 5.64 → 5.48 (about 0.12-0.16 points); 19 Oct is published | Replace |
| 307 | "about 47% of modelled paths on basis D at 16 Oct" | 41% at 19 Oct (38-43%) | Replace |
| 2H traps / 2I Q3 | "The line may be crossed by 22 Oct, or not" | About 1 in 10 by the 21 Oct close (§3). Both outcomes still need preparing | Holds |
| E21 (IPS kit) / any IBTR reflection plan | "about $293k → about $299k, room 0.23 → 0.04" | On 19 Oct: $293.5k → $297.2k, room 0.23 → 0.10 | Any "room fell to almost nothing" sentence is a 16 Oct statement: date it or drop it |

### 9d. `oct19/ipskit/ips_writing_kit.md`

| Line / ID | Now | 19 Oct | Action |
|---|---|---|---|
| 192-200 (D1 table) | $10,952 / $21,185 / $30,753 / $43,509 / $49,960; MC p95 $25.4k, p99 $33.1k; history p95 $22.3k, worst $38.6k | $11,005 / $21,287 / $30,902 / $43,731 / $50,691; $25.6k / $33.3k; $22.4k / $39.0k | Minor; "stable" holds |
| 205 (1a) | Chain fails 7.2-8.75%; post-2033 7.74%, median gap $3,181 | 6.5-8.0%; 7.1% (D), median $3,167 | Minor |
| 206 (1b) | Kept-to-2042 6.88%; Laura keeps median $24k (D) | 6.3%; $25.6k | Minor |
| 240 (3a) | "room $1,060 on basis D, 16 Oct" | $2,838, 19 Oct | Replace |
| 242 (3c) | "A 2-point fall leaves a $21,185 gap" | $21,287 | Minor |
| 251-255 (D4 facts) | $116,830 / 5.06% / $33,170; half-point fall $136.1k (D) to $140.2k (A); top-up "35-47%"; floor paid p1/p5/p50 $119.4k / $130.4k / $149.4k; reinvest $149,187 to $146,864 | $116,485 / 5.12% / $33,515; $138.0k to $142.1k; **30-41%**; $121.5k / $132.3k / $149.5k (A) to $116.8k / $127.8k / $149.2k (D); $149,179 to $146,834 | Replace |
| 261 | "$145k holds to 2031 in only 56-67%" | 61-72% | Replace; the "freeze the rule, not the dollars" conclusion holds |
| 320-321 (D7) | Book $304.4k / $302.9k; VT 8.60% | $303.4k / $301.9k; VT 8.65% | Replace |
| 340-345 (D8) | R31 top p5/p50/p95 $145k / $169k / $192k; 76/79/85% at top; 99.25-99.4%; $170.3k → $163.0k | **R31 (trusting-euler range_2031) not re-run** (outside the copied scripts); number sheet 99.33-99.46%; $170.5k → $163.2k | Update the number-sheet items; mark R31 items "16 Oct" |
| 383 | "182 of 199" | 182 of 200 | Minor |
| F20 (588) | 16 Oct par yields | 19 Oct: 1y 4.50, 2y 4.77, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48 | Replace |
| F21 (589) | D $298,940 / $1,060 / 3.6bp; A, C, E as 16 Oct | D $297,162 / $2,838 / 9.8bp; A $293,001 / $6,999 / 24bp; C $296,399 / $3,601 / 12bp; E $294,437 / $5,563 / 19bp | Replace |
| F22 | DV01 $284-293 | $288-291 | Holds ("about $290") |
| F23 | A 35%, E 39%, D 47% | A 30%, E 34%, D 41% | Replace |
| F24 | 182 of 199 (D), 173 of 199 (A) | 182 of 200, 173 of 200 | Minor |
| F25 | 5.15% (C) / 5.12% (D); margin 0.03-0.06 | 5.21% / 5.19%; 0.10-0.13 | Replace |
| F26 | 16 Oct coupon figures | §5 | Minor |
| F28 | 7.2-8.75%; 7.74%; 6.88%; $3,181 | 6.5-8.0%; 7.1%; 6.3%; $3,167 (D) | Minor |
| F29 | $116,830; $33,170; VT median $32,174 (band $20.3k-$42.6k) | $116,485; $33,515; $32.3-32.6k ($20.3-20.8k to $42.8-42.9k) | Replace |
| F30 | $136.1k (D) to $140.2k (A) | $138.0k to $142.1k | Replace |
| F31-F32 | 16 Oct floor figures | §4a | Replace |
| F33, F35, F36 (R31 parts), F38-F39 (R31) | R31 model figures | **Not re-run**: the range_2031 scripts are not in the copied folders | Keep, labelled 16 Oct |
| F34 | 56-67% | 61-72% | Replace |
| F37 | $170.3k → $163.0k (sheet median $169.7k → $162.7k) | $170.5k → $163.2k ($170.0k → $162.8k) | Minor |
| F40 | 66.9 / 24.6 / 0.8 / 6.9 | 66.5 / 24.4-24.7 / 1.2 / 6.9-7.0 | Minor |
| F56 | $304.4k (+1.48%), $302.9k | $303.4k (+1.13%), $301.9k | Replace |
| F58 | VT 8.60% on 16 Oct | 8.65% on 19 Oct | Minor |
| F59 | About 90% of the book in one issuer; IBTM 32.6% | 90.2%; IBTM 32.45% | Holds |
| E3 (668) | "the 10-year was 5.09%; margin 0.03-0.06" | 10-year 5.15% (19 Oct); margin 0.10-0.13 | Replace |
| E6 (671) | "room $1,060 ... 47% chance" | $2,838 ... 41% | Replace. The error stands: "covered at purchase" is still not guaranteed |
| E28 (684) | "about $116.8k IBTM and $33.2k VT" | About $116.5k and $33.5k | Minor |
| E21 (693) | D: about $293.5k → $298.9k, room 0.23 → 0.04 | ... → $297.2k, room 0.23 → 0.10 (19 Oct) | Replace, with the date |

### 9e. `oct19/drill/defence_drill.md`

| Line | Now | Action |
|---|---|---|
| 26-46 (card) | 16 Oct card | Replace with §8. Rows 3, 4, 6, 10, 11 and 15 change materially; rows 7 and 8 change slightly; rows 1, 2, 5, 13 and 14 hold |
| 89-91 (IBTM 2d) | "about $136k"; "Forward yield 5.06% ... $116,830"; "$149.2k / $148.4k / $147.6k / $146.9k" | About $138k; 5.12% / $116,485; $149.2k / $148.4k / $147.6k / $146.8k |
| 107 (2f) | "about $98,728 at the 16 Oct close of $21.925" | About $98,458 at the 19 Oct close of $21.865 (32.45% of the book) |

### 9f. Live IPS Version 5 figures (Drive copy `oct19/numbers/data/ips_report_live_19oct.txt`, not re-read today)

| V5 figure | 19 Oct check |
|---|---|
| "5.1%" needed | Holds (5.09%) |
| "about 5.15%" | Now equals the 10-year par yield (5.15%). The ladder is 5.19-5.21%. Still undated |
| "about $136,000" after a half-point fall | About $138,000 (D). It moves about $290 per 0.01 point |
| "$169k → $162k" | Fine as rounding ($170.5k → $163.2k) |
| "two-thirds / one quarter / under one tenth" | Holds (66.5 / 24.5 / 7.0) |
| "$21,000" | Holds ($21.3k on E; $19.0k on holdings' dates) |
| "covered at purchase" / "the 2027 deposit alone is sized" | On D the first deposit covers the ladder by $2,838 on 19 Oct, with a 41% chance it won't by January. Still true only through the top-up rule |

---

## 10. Limits and what is still UNVERIFIED

- **Models.** All ladder, floor, range and option figures are MODEL. They rest on:
  - parallel random-walk rates;
  - iBond funds modelled as par bonds ending 15 Dec;
  - VT at 7.0% compound, 16.78% volatility;
  - no taxes.
  The limits listed in `oct19/coupon/coupon_risk_options.md` §6 and `oct19/numbers/findings.md` apply unchanged.
- **Not re-run** (their scripts are not in `oct19/numbers` or `oct19/coupon`):
  - the trusting-euler `range_2031` (R31) figures;
  - R16's "8.4% of days since 2000";
  - the 2008 replay "Laura keeps $18,446";
  - the 15 Oct "$309.6k / $304.1k" dedicated-rebuild costs (the coupon study's own dedicated cost, $300,439, is re-run).
- **Book value.** The T-bond prices are MODEL. Unverified: whether WInS counts accrued interest; WInS's own displayed prices and total; when coupons and distributions are credited; the $6-15 cash residual.
- **The 20 Oct close.** It was not published at either fetch (21:38 and about 21:52 UTC, 19 Oct). Re-run `sh oct20/numbers/scripts/run_all.sh 10/20/2026` when it appears. A one-day move of about $1.6k is normal, so re-check before any dated figure is used.

## 11. Files (all under `oct20/numbers/`)

- **This file:** `numbers_refresh.md`.
- **Tables:**
  - `ladder_cost_by_basis_6-19Oct.csv` (5 bases × 9 days: cost, room, DV01, break-even, odds at five volatilities);
  - `coupon_options_comparison_19Oct.csv`;
  - `wins_book_value_19Oct.csv`;
  - `wins_book_value_series.csv`.
- **Data:**
  - `data/raw/` (treasury.gov fetches), `data/prices/` (Yahoo JSON);
  - `data/refresh_out.txt`, `reconcile_out_19oct.txt`, `indep_pricer_out.txt`, `indep_holdings.txt`;
  - `data/v5_figures_out.txt`, `v5_floor_range_out.txt`, `v5_live_checks_out.txt`, `v5_stress_out.txt`;
  - `data/days_over_out.txt`, `daily_moves_out.txt`, `ladder_cost_2026_daily_A_D.csv`;
  - `data/sheet/s19_{A,E,C,D}.json` with `data/anchor_comparison_19oct.txt`;
  - `data/coupon19/` (coupon model results, summary and named-path CSVs, extra checks);
  - `data/repro16/` and `data/sheet/repro16_A.json` (reproduction of 16 Oct);
  - `data/run_1019/` (test of `run_all.sh`).
- **Scripts:** `scripts/`, the copied originals plus `refresh_oct20.py`, `v5_live_checks_oct20.py`, `book_value_oct20.py`, `book_series_oct20.py`, `anchor_table.py`, `days_over.py`, `daily_moves.py`, `v5_stress_oct20.py` and `run_all.sh`.
