# Range audit: an independent re-build of Laura's plan simulation (20 Oct 2026)

AI-generated research (Claude Code) for Team Caplet. These are MODEL numbers for checking, not text to submit. Any figure the team uses goes in the Works Cited as AI help. Folder: `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/rangeaudit/` (scripts in `scripts/`, outputs in `data/results.json`, `data/compare.json`, `data/compare_extra.json`, `data/extra2.json`, re-runs of the three earlier models in `rerun/`).

## 0. Summary for the team

- **Robust (every model agrees within about 2-3%):** the ladder costs about $297-300k on 1 Jan 2027. The floor is $150k in the typical case. The quoted bottom is $145k in the typical case. The median top and the median gift are both about $165-169k. The gift reaches at least the midpoint about 98-100% of the time. Each 1-point permanent fall in yields costs about $10-12k of coupon income. The stock-yield correlation changes almost nothing.
- **Fragile (the models disagree by a factor of 2 or more, for reasons the plan has not decided):** the room under $300k ($-0.8k to +$7.1k), the chance a top-up is needed (32-47%), the chance a payment is short under each coupon option, and the chance the gift reaches the top once option 3r is added.
- **New 1: 3r's "0.02%" depends on one unstated sizing choice.** The coupon study's result for option 3r (payments short in 0.02% of paths) assumes cash waiting between a rung's maturity and the 1 January payment earns 0%. If the rungs are sized counting bill interest on that cash, which is how they cost about $1-2k less, 3r leaves a payment short in **about 6%** of paths. The gaps are small: 1-in-100 about $3.2k, worst about $9.7k.
- **New 2: 3r as written cuts the chance of reaching the top from about 3 in 4 to about 1 in 3.** The reserve is counted in the top, but in 2033 only the part above "need + $5k" is released. The coupon study's own code shows the same effect (68% falls to 41%; this was not reported in its tables).
- **New 3: "the gift falls inside the range ~99%" depends on the net-minimum rule.** It is about 99.9% with the rule COMPETITION.md s7 already states ("rounded down after any expected shortfall"), and 98.4-99.4% without it.

## 1. What I built (independent of the earlier code)

The engine is `scripts/laura_sim.py`. I wrote it from the plan text (`/home/user/snap/main/COMPETITION.md:150-167`) and the case (`/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:88-120`). I did not reuse any earlier model code.

**Plan as modelled:**
1. **1 Jan 2027.** $300k buys ten rungs: IBTM-IBTR, then the T-bonds 4.750% Feb-37, 4.500% May-38, 4.375% Nov-39, 4.250% Nov-40 and 3.125% Nov-41 (`/home/user/snap/main/team/google_drive/sheets/portfolio_and_trading_notes/book_l.csv:14-23`).
   - Each rung is sized to put $50,000 in cash on its 1 January payment date.
   - Coupons are reinvested to the rung's maturity at the yield of the day.
   - After maturity the cash waits in Treasury bills until the payment.
   - If the ladder costs more than $300k, the longest rungs are bought first.
   - Any leftover is held in a Treasury to Dec 2032.
2. **1 Jan 2028.** The $150k is used in this order:
   - (1) top up any missing rung at Jan 2028 prices;
   - (2) optional 3r reserve in the Nov-41 bond;
   - (3) the floor in IBTM, sized to pay back what is left (rule F1). Rule F2, a fixed $150k, is tested too;
   - (4) VT with the rest.
3. **1 Jan 2031: the range.**
   - **Bottom** = the projected IBTM payout × 98%, minus any projected shortfall that the leftover and Laura's half cannot cover, rounded down to $5k.
   - **Top** = the projected payout + half of VT, minus the same uncovered shortfall, rounded down to $1k. Under option 3r, plus the reserve.
4. **1 Jan 2033.**
   - **Gift** = IBTM payout + half of VT (+ the 3r release), capped at the top.
   - **Projected payment shortfall:** valued in today's dollars on the 2033 curve. It is covered first by the 2027 leftover, then by the 3r reserve (which keeps need + $5k), then by Laura's half and anything above the cap, then by the gift above the floor, then by the floor itself.
   - Cover money buys Treasuries that pay out on the dates of the projected gaps.
5. **2033-2042.** Payments are made in order and surpluses carry forward in bills. A gap above $100 that nothing permitted can fill counts as a "short payment".
   - **o1:** portfolio money only.
   - **o2:** Laura's remaining half also stays in VT inside the portfolio.
   - **o2c:** the same half, held as cash.

**Where my choices differ from all three earlier models** (each is tested as a toggle in section 3):
- iBond funds are modelled from iShares' own 16 Oct data (weighted average coupon 3.50/4.04/4.12/4.28/4.35%; weighted average maturity 5.71-9.54 years), net of the 0.07% fee. The earlier models used par bonds ending 15 Dec, with coupon = yield.
- Sizing and reinvestment use the curve's own yield at each remaining maturity ("yields unchanged", roll-down), not each bond's purchase yield.
- Waiting cash earns bills.
- Stock log-volatility is converted exactly from JPM's 16.78% arithmetic volatility (0.154, not 0.1678).
- Yields are floored at 0%, not 0.25%.
- The 2033 cover is valued in today's dollars, not as a nominal sum.

**Inputs:**
- treasury.gov par curve, **19 Oct 2026** row: 1y 4.50, 2y 4.77, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48. This was the latest row when fetched at 21:38 UTC on 19 Oct. URL: `https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv`; saved as `data/tsy_202610.csv`.
- iShares product pages (e.g. `https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf`; data as of 16 Oct, fetched 19 Oct; `data/web/p_*.html`).
- VT 7.00% compound, 16.78% volatility (JPM 2026 LTCMA AC World, VERIFIED per CLAUDE.md), 0.06% fee.
- Rates: parallel random walk, 1.0 point a year.
- 100,000 paths, seed 20261020.
- History, monthly since 1953:
  - FRED GS10, from the repo copy `fred_GS10_monthly.csv`, which runs to Sep 2026. A fresh FRED fetch failed from this container, so whether it is FRED's latest release is UNVERIFIED.
  - Shiller US total-return index (repo `rab/data/history/shiller_monthly.csv`). US stocks stand in for VT.
  - 688 windows of 16 years (start Apr 1953 to Jul 2010). "Additive" applies the historical point change to today's curve. "Proportional" applies the historical percentage change.

**Checks I ran twice:**
- (a) With no rate moves, every rung delivers exactly $50,000.
- (b) My curve reproduces the numbers desk's 16 Oct basis B ($295,559, exact) and basis D ($298,935 vs $298,940). My bootstrapped zeros at the iBond maturities are within 1-3bp of iShares' published yields to maturity.
- (c) A different seed changes no headline by more than 0.4 points or $300 (base: 75.7% vs 75.8% at the top; option-1 short 32.0% vs 32.3%).
- (d) I re-ran all three earlier models on their own curves. They reproduce byte for byte (fervent-edison `results.json`, trusting-euler `range_2031_results.csv`, coupon study `coupon_options_results.json`). I then re-ran each on the 19 Oct curve (`rerun/`).
- (e) For each one I moved my model to its assumptions one at a time (waterfalls in section 3). My emulation lands within 1-3% of every published headline except two, both explained below.

## 2. Headline numbers, 19 Oct curve (MODEL; 16 Oct in brackets, for comparison with the earlier models)

| Item | Mine, base (19 Oct) | Mine (16 Oct) | Same model + option 3r ($10k) |
|---|---|---|---|
| Ladder cost on 1 Jan 2027 if yields don't move (holdings, bills on waiting cash) | $297,224; room $2,776 (9.7bp) | $298,913; room $1,087 | same |
| Other bases, 19 Oct: A (payment dates, forward) / B / C (holdings, forward, 0%) / D | $292,908 / $293,767 / $296,307 / $297,158 | $294,701 / $295,559 / $298,087 / $298,935 | |
| Chance the ladder costs more than $300k | 41.7% | 46.9% | same |
| Top-up 1-in-20 | $20.4k | $22.8k | same |
| Floor, p5 / median | $129.6k / $150k | $127.2k / $150k | $119.6k / $140k |
| VT bought Jan 2028, p5 / median / p95 | $19.5k / $31.3k / $41.7k | $18.9k / $30.8k / $41.4k | $18.0k / $29.1k / $38.9k |
| IBTM payout ÷ amount it was sized for, p1 / median | 97.4% / 100.0% | same | same |
| 2031 bottom, median (share of paths exactly $145k) | $145k (54%) | $145k (50%) | $135k |
| 2031 top, p5 / median / p95 | $139k / $166k / $181k | $136k / $165k / $181k | $143k / $167k / $181k |
| 2033 gift, p5 / median / p95 (p1) | $137k / $166k / $181k ($121k) | $134k / $165k / $180k | $136k / $164k / $180k |
| Gift below the announced bottom | 0.08% | 0.09% | 0.006% |
| Gift reaches the top (exact / within $1k) | 75.8% / 82.2% | 75.7% / 82.1% | **34.0% / 40.6%** |
| Gift at least at the midpoint | 99.2% | 99.1% | 98.0% |
| Coupon shortfall before any cover: median / 1-in-20 / 1-in-100 | $0.5k / $27.7k / $35.3k | $0.5k / $27.6k / $35.1k | same |
| Yields fall 1 / 2 / 3 / 4.5 points on 2 Jan 2027 and stay | $11.5k / $22.3k / $32.4k / $46.2k | $11.5k / $22.2k / $32.3k / $46.0k | |
| A payment short, o1 (portfolio only) | 32.3% (1-in-100 size $8.2k, worst $14.4k, typical $2.1k) | 32.2% | **6.2%** (1-in-100 $3.2k, worst $9.7k) |
| A payment short, o2 (Laura's half in VT to 2042) / o2c (as cash) | 2.2% / 2.4% | 2.4% / 2.7% | 0.46% / 0.52% |
| Laura's free money in 2033, p5 / median | $1.0k / $28.0k | $0.5k / $26.4k | $7.0k / $24.8k |
| History, additive: coupon shortfall 1-in-20 / worst; o1 / o2 short; gift below bottom; reaches top | $27.6k / $49.2k (Apr 1984 start); 36% / 1.0%; 0 of 688; 87% | | o1 8.0%, o2 1.5%; top 46% |
| History, proportional | $19.4k / $26.9k (Apr 2007 start); 39% / 0%; 0 of 688; 87% | | o1 2.3%, o2 0% |

Correlation (19 Oct), 0 → +0.3 → +0.5:
- Gift p5: $137k → $136k → $135k.
- Gift below the bottom: 0.08% → 0.15% → 0.22%.
- Reaches the top: 75.8% → 74.3% → 73.5%.
- o2 short: 2.2% → 2.6% → 2.9%.
- o1 and 3r: unchanged, because they do not touch stocks.

Floor rule F2 (a fixed $150k) instead of F1:
- VT p5 falls to $5.2k.
- Gift below the bottom rises to 0.84% (F1: 0.08%).
- o2 short rises to 3.7%.

So "the floor = what is left" (D0-2 option a) is the safer rule.

## 3. Comparison with the three existing models, and every disagreement above 2%

Sources:
- **FE:** `/home/user/snap/claude_fervent-edison-sqk1ry/research/ips_numbers_2026-10/results.json` and `IPS_number_sheet.md`; 15 Oct curve.
- **TE:** `/home/user/snap/claude_trusting-euler-gms43m/research/range_2031/README.md:30-34` and `range_2031_results.csv`; 16 Oct.
- **CO:** `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/coupon/coupon_risk_options.md:36-48` and `data/coupon_options_results.json`; 16 Oct.

"Emulated" means my engine with that model's assumptions switched on (`data/compare.json`, 50,000 paths).

| # | Number | FE | TE | CO | Mine, same curve | Off by more than 2%? Why (from the waterfall) | Emulated |
|---|---|---|---|---|---|---|---|
| 1 | Ladder cost / room | $294,453 / $5,547 (basis A, payment dates) | $298,087 / $1,913 (basis C) | $300,174 / -$174 (sized to maturity, cash at 0%) | $298,624 (15 Oct) / $298,913 (16 Oct) | Cost: no (within 2%). Room: yes, by a factor of 5. Each model prices a different thing: FE = payment dates (cheapest; not buyable on WInS); TE = holdings' dates, forward; CO = cash waits at 0%; mine = holdings, waiting cash in bills, iBond funds' real maturities (mid-year, so more waiting) | FE $5,547 ✓; TE $1,913 ✓; CO -$782 (vs -$174: the gap is my iBond model) |
| 2 | Chance cost > $300k | 35.2% | 44% | n/a | 45.9% (15 Oct) / 46.9% (16 Oct) | Yes. Follows from row 1: FE prices basis A, which has $4k more room. Anchored to A, my model gives 32% | FE 32%; TE 43.9% ✓ |
| 3 | VT bought Jan 2028, median | $32.3k | $35.4k | (not reported) | $31.0k / $30.8k | FE +4%: floor priced on forward yields (+$0.8k; forward 5.05% vs unchanged-curve 4.90%) and par/own-yield sizing (+$0.6k). TE +15%: the 2027 leftover goes into VT (+$3.2k), plus forward floor pricing (+$0.9k) | FE $32.8k ✓; TE $36.0k ✓ |
| 4 | VT p95 | $42.7k | $60.1k | | $41.6k | TE +44%: the leftover goes into VT, and is large when yields rise before January. The plan says the leftover is the first shortfall buffer (`COMPETITION.md:161`), so TE's $192k top p95 reflects a different plan | TE $60.0k ✓ |
| 5 | Bottom, median | $145k | $145k | $145k | $145k | No | ✓ |
| 6 | Share of paths at exactly $145k | 68% | — | — | 54% | Yes. Fewer top-ups in FE (row 2), and my bottom also nets off projected shortfalls | — |
| 7 | Top, median | $167.8k | $169k | $166.1k | $166k / $165k | TE +2.4%: leftover in VT (+$2k) and forward floor (+$1k). FE and CO within 1.3% | ✓ all |
| 8 | Top, p5 | $144.8k | $145k | — | $136k | Yes, 6%. Mine includes coupon risk with roll-down and the net-minimum cut (paths with a top-up and falling yields). FE has no net-minimum; TE has no coupon risk | FE $149.8k (its anchor); TE $144k ✓ |
| 9 | Gift, median | $167.0k | $168k | $165.3k | $165k | TE +1.8%; within 2% | ✓ |
| 10 | Gift, p5 | $142.4k | $144k | $135.8k | $134.2k (16 Oct) | FE +6% and TE +7%: TE has no coupon risk; FE uses basis A cost (fewer, smaller top-ups) and no roll-down. CO is within 1.2% | FE $146.4k; TE $144k ✓; CO $139.5k |
| 11 | Gift inside the range (at or above the bottom) | 99.4% | 100% | 97.9% (2.1% below) | 99.9% (98.4% without the net-minimum) | Small, but the rule matters: TE is 100% by construction (no coupon risk). CO's 2.1% has no net-minimum on the bottom; with it, CO gives 0.6% | FE 99.1%; TE 100% ✓; CO 99.3% |
| 12 | Gift reaches the top | 76% (within $1k) | 76% | not reported; its code gives 68% exact / 75% within $1k | 75.8% exact / 82% within $1k | No for the plan as written: about 3 in 4 everywhere. **Yes with 3r: 34% mine, 41% in CO's own code (probe `rerun/co_top_probe.py`)** | TE 79%; FE 75% |
| 13 | Gift at least at the midpoint | 98.1% | 100% | — | 99.2% | No | ✓ |
| 14 | Coupon shortfall if yields fall 1/2/3 points | $11.0k / $21.2k / $30.8k | none modelled | $9.5k / $18.9k / $27.6k | $11.5k / $22.2k / $32.3k | Mine vs CO +18%: CO lets waiting cash earn 0%, so falling bill rates cost nothing. In mine that interest is in the plan and falls with yields (about $4.4k of the $22.2k). Mine vs FE +5%: the iBond funds' real holdings mature mid-year (more waiting cash) | FE-like $11.0k / $21.3k / $30.8k ✓; CO-like $10.0k / $19.2k / $27.9k ✓ |
| 15 | Model shortfall 1-in-20 / 1-in-100 | $25.5k / $33.2k | — | $21.2k / $28.2k | $27.6k / $35.1k | Same causes as row 14, plus a 0% vs 0.25% yield floor | FE $24.8k / $32.1k ✓; CO $21.5k / $28.3k ✓ |
| 16 | History: shortfall 1-in-20 / worst | $22.3k / $38.7k | — | $21.2k / $36.7k | $27.6k / $49.2k (additive); $19.4k / $26.9k (proportional) | Yes. The worst is the 1984 start: yields fell about 9 points from 13%. Applied additively to a 5% curve, that drives yields to about 0. My floor is 0% (theirs 0.25%), and my waiting cash loses interest too. On a proportional reading, the worst is half as big. The 1984 "worst case" is a modelling artefact either way | — |
| 17 | A payment short, option 1 | (FE: 6.3% "exceeds what Laura kept": another metric, see row 19) | — | **16.4%** | **32.3%** | Yes, 2×. (i) Waiting cash: CO sizes rungs as if it earns 0%, so real bill interest is a free cushion (about $4.5k); my rungs count that interest, so there is no cushion (22% → 32%). (ii) CO keeps the whole unused 2027 leftover in the reserve to 2042; mine releases it to Laura (18% vs 24%). Residual 18.1% vs 16.4%: payment-level vs total threshold and pricing detail | 18.1% |
| 18 | A payment short, option 2 (half in VT to 2042) | 5.6% | — | 1.4% | 2.2% | Yes, but all are "a few %". The definitions differ: FE counts only half of VT, not the money above the cap, and its 2033 projection leaves out waiting-cash interest risk that its realised path includes; CO counts the half minus what was taken | FE 2.5-2.8%; CO 1.9% |
| 19 | FE "post-2033 gap exceeds what Laura kept" | 6.3% | — | — | o2c 2.4% | Yes. FE aggregates all payments into one sum (no timing), and its kept pool is the leftover + half only. With the leftover kept and no overflow my emulation gives 3.1% | 3.1% |
| 20 | **A payment short, option 3r** | — | — | **0.02%** | **6.2%** | **Yes, by a factor of 300.** The 0.02% needs both CO assumptions from row 17: waiting cash at 0% in sizing (alone: 2.2%) and the whole leftover kept to 2042 (alone: 5.3%). With all of CO's settings my engine gives 0.32%. The rest of the gap is small pricing detail in the hedge. Larger reserves do not fix it, because the release rule keeps only need + $5k: 15k / 20k / 25k give 3.2% / 2.1% / 1.9% (worst stays $8.5k). Gaps are small (1-in-100 $3.2k) | 0.32% |
| 21 | 3r: median gift / gift below the bottom | — | — | $162.2k / 0.05% | $163.9k / 0.006% | Gift +1%. Below-bottom: both rare | ✓ |
| 22 | Laura's free money in 2033, median | $27.9k | $28.7k | $19.9k | $28.0k | CO -29%: a definition. CO keeps the leftover in the reserve and excludes money above the cap | CO-like + keep leftover: $22.0k |
| 23 | Share of VT promised vs P(top): 1/3, 1/2, 2/3, all | — | 76 / 76 / 75 / 74% | — | 76.8 / 75.1 / 73.9 / 71.9% | No. Robust: the share hardly changes the odds. It changes the size of the top ($160k / $166k / $172k / $183k) and Laura's bad-case cushion | ✓ |

Two published claims need care in the light of rows 1-2 and 20:
- (a) FE's "about $294,000, 1 case in 3" is payment-date basis A (already flagged at `oct19/out/Caplet_Update_19Oct2026.md:203`). On 19 Oct, basis A is $292,908 with odds of 32%. On WInS holdings with bills it is $297,224 with odds of 42%.
- (b) CO's recommendation for 3r rests on "0.02% / 0 of 690". That holds only if the rungs are sized as though waiting cash earns nothing **and** the unused leftover stays in the reserve to 2042. If the team adopts 3r, those two rules have to be stated as part of it. Otherwise the honest figure is "about 1 path in 16, by a few thousand dollars".

## 4. Sensitivity (19 Oct, 50,000 paths, the same random numbers; base plan, with 3r in brackets)

| Input | Low | Base | High | What moves |
|---|---|---|---|---|
| VT return 4 / 7 / 9% | top p50 $165k; gift p50 $164k; p5 $135k; reaches top 67% (25%); Laura's median $23.8k | $166k; $166k; $137k; 75% (34%); $27.7k | $167k; $167k; $138k; 80% (40%); $30.7k | Only the odds of reaching the top and Laura's money. The range itself moves ±$1-2k because VT is only about 7% of her money |
| VT volatility 12 / 17 / 22% | top p95 $179k; reaches top 82%; below bottom 0.03% | $182k; 75%; 0.07% | $185k; 70%; 0.14% | Same, smaller |
| Rate volatility 0.7 / 1.0 / 1.3 pt a year | cost > $300k 38%; floor p5 $137k; gift p5 $149k; shortfall 1-in-20 $21.0k; o1 short 33% (3r 3.6%); o2 1.4% | 42%; $129k; $137k; $27.7k; 32% (6.3%); 2.2% | 44%; $122k; $124k; $32.4k; 30% (7.1%); 2.2%; bottom median falls to $140k | The low tail of the floor, bottom and gift, and the size of coupon gaps |
| Worst combination (4%, 22%, 1.3 pt, correlation +0.5) | gift p5 $120k; below bottom 1.1%; reaches top 62%; o2 4.3% (3r: below bottom 0.14%, o1 7.1%) | | | |
| Best combination (9%, 12%, 0.7 pt) | gift p5 $151k; reaches top 89% | | | |

Option 1's chance of a short payment hardly moves with rate volatility (30-33%). It is set by the zero margin in the cover rule, not by how wild rates are. Only the *size* of the gaps scales with volatility.

## 5. Which numbers are robust

| Number | Robust? | Safe statement (MODEL, dated) | Range across models and sensitivities | What it depends on |
|---|---|---|---|---|
| Ladder cost on 1 Jan 2027 | **Yes** (within 1%) | About $297-300k at mid-October yields | $292.9k (payment dates) to $300.8k (cash at 0%) | Basis; about $290 per 0.01 point |
| Room under $300k / chance of a top-up | **No** | "Near zero; a fall of about 0.1 point uses it up; a top-up is close to a coin flip" | -$0.8k to +$7.1k; 32-47% | Basis, curve day (+$1.7k from 16 to 19 Oct) |
| Floor, typical case | **Yes** | $150k when no top-up is needed | All models | Rule F1 |
| Floor, bad case (p5) | Roughly | About $120-137k | $119.6k (3r) to $137k | Rate volatility, 3r |
| Bottom, typical | **Yes** | $145k (3r: $135k) | All models | The rounding rule. The share of paths exactly at $145k is not robust (50-68%) |
| Top, median | **Yes** (within 2.4%) | About $165-169k | $165-169k | Leftover use, floor pricing |
| Top, p5 / p95 | No | "From about $135-145k to $180-190k" | p5 $136-150k; p95 $181-192k | Coupon risk, net-minimum, leftover into VT |
| Gift, median | **Yes** | About $165-168k | $162k (3r) to $168k | — |
| Gift, 1-in-20 low | No (7%) | "About $135-145k" | $134-146k | Coupon risk, rate volatility ($124-149k) |
| Gift at or above the bottom | **Yes, if the net-minimum rule stays** | About 99%+ | 99.1-100% with the rule; 97.9-98.4% without it; 98.9% in the worst combination | Net-minimum rule; F1 vs F2 |
| Gift reaches the top | Yes for the plan as written (about 3 in 4); **No under 3r** | "About 3 in 4" | 67-82% (return/volatility); with 3r 25-46% | 3r top rule |
| Gift at least at the midpoint | **Yes** | "Almost always (about 98-100%)" | 91-100% | Only the worst combination drops below 96% |
| Share of VT promised vs odds of reaching the top | **Yes** | "The share sets the size, not the odds" | 72-77% | — |
| Coupon cost of a permanent fall of 1 / 2 / 3 points | **Yes** in shape | "About $10-12k per point" | $9.5-11.5k / $18.9-22.3k / $27.6-32.4k | Whether waiting-cash interest is counted |
| Coupon shortfall 1-in-20 | Roughly | "About $20-28k" | $21-28k model; $19-28k history | Waiting cash, rate volatility ($21-32k) |
| Worst historical shortfall | **No** | Do not quote one number | $27k-49k | Additive vs proportional replay, yield floor |
| A payment short, option 1 | **No** | "Small gaps are likely (1 in 6 to 1 in 3); typical about $2k, 1-in-100 about $3-8k" | 16-36% | Waiting-cash sizing, leftover kept or released |
| A payment short, option 2 | Roughly | "A few in 100" | 1.0-5.6% | Definitions, correlation |
| **A payment short, option 3r** | **No** | Only with its rules stated: "0.02-0.3% if rungs are sized with no interest on waiting cash and the leftover stays in the reserve; about 6% (small gaps) if not" | 0.02-8.0% | Same two rules; the release margin |
| Stock-yield correlation | **Yes** | "Makes little difference" | below bottom +0.14 points; o2 +0.7 points | — |
| Laura's free money in 2033 | No (definition) | Define it first | $20-31k median | Whether the leftover and the money above the cap count |

## 6. What the team should take from this (decisions, not wording)

1. **If 3r is voted on 27 Oct, it is a package of three rules, not one number.**
   - Size the rungs as though waiting cash earns nothing, or say it does and accept about 6% small gaps.
   - Keep the unused 2027 leftover in the reserve to 2042.
   - Decide whether the reserve counts in the top. If it counts, the chance of reaching the top falls to about 1 in 3. If it does not, the top falls about $12k (median $155k) and is reached about 95% of the time.
2. **Keep the net-minimum rule.** COMPETITION.md s7 already implies it. It is what makes "inside the range about 99%" true.
3. **Keep the floor as "what is left" (F1), not a fixed $150k.** F2 raises the chance of breaking the bottom tenfold (0.08% to 0.84%) and can leave VT near zero.
4. **In the IPS, quote only robust items.** The plan's rules, the $150k/$145k typical floor and bottom, about $165-169k typical top and gift, about 3 in 4 to reach the top (plan without 3r), and about $10-12k per point of permanent yield fall. Any probability of a short payment needs its basis named beside it.
5. **Re-price on the 6 Nov close.** The room moved by $1.7k in one trading day (16 to 19 Oct).

Limits:
- Parallel rate moves with no pull back to normal.
- iBond funds are modelled as a single bond at their average maturity.
- US stocks stand in for VT in the history replay, using monthly-average prices.
- No taxes or commissions.
- The 2031 valuation date is fixed at 1 Jan 2031.
- When WInS credits coupons is UNVERIFIED (unchanged).

*What this teaches:* a probability is only as good as its smallest hidden rule. Here, whether the cash waiting for two months earns interest changes "1 in 5,000" into "1 in 16".
