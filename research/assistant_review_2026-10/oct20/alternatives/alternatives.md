# "Why not X?": priced alternatives to Laura's real plan, on one basis

> **Verified 20 Oct (`oct20/verify_rub_alt/verify_rub_alt.md`): numbers reproduce; re-base before quoting.** The current-plan headline "0.02% / 0 of 690 windows" is the study engine's LOW END: agreed basis (reconcile_3r §5) = 3r ~0.6% short (range 0.01-0.6%), worst ~$3.3k, 1% of 688 additive history windows; option 1 = 14.4-14.5% (not 15.6%). Totals add undiscounted 2042 money to 2033 money (flatters ladder rows ~$7k at the median; 6b glide then leads by ~$7k at the median but has a far worse bad case). VT-share minimums are medians one $5k step below their flat values (15% of deposit: $145k flat; 25%: $125k; 15% of all money: $85k). IEF/VGIT/SPTI (and SGOV) ARE WInS-listed (team WInS read 29 Sep). Corporate 2033-36 saving ~$9.0k (not $9.3k). Growth-first payment miss confirmed ~4-5% by three independent codes.


**AI-generated research for Team Caplet (Claude Code), written Tue 20 Oct 2026 (Sydney).** These are MODEL numbers, not facts and not text to submit. Nothing here is drafted wording for the TNA, IPS or Final Report. The "reason" lines are reasons in note form. If a student uses an idea or figure, they must re-derive it, say it in their own words, and log the AI use (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, quoted in `oct19/out/Caplet_Update_19Oct2026.md:7`). Short forms: `oct19/` and `oct20/` = the scratchpad folders `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`. `case:n` = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`. `FAQ:n` = `oct19/askwharton/web/faqs.txt` (the correct 19 Oct live copy). `TNA:n` = `.../official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt`.

## 1. The answer in short

- **Nothing tested beats the current plan on the case's first test: payments funded "with a high degree of certainty" from inside the portfolio (case:91-92).** The current plan (Root-and-Branch plus the recommended 3r reserve) leaves a payment short in 0.02% of 100,000 model paths (worst $0.6k) and in 0 of 690 history windows.
- **Growth-first fails worst.** It misses payments in 4.6% of model paths (6.4% when stocks and yields fall together, 15.3% if the 2028 deposit is only $75k), and the worst miss is about $238k. The whole-portfolio glide is the only other option with large misses (worst $67.5k). History since 1953 shows no miss, but its gift falls below its own minimum in 3.5% of windows.
- **All-Treasury (no VT) does not raise the co-sponsor numbers.** The median gift is the same ($163.7k against $163.3k), because the gift is capped at the 2031 top. What it loses is Laura's upside: her flexibility money falls about $5k at the median, and the 1-in-20 good total falls about $15k. In history it breaks the minimum more often (1.2% of windows against 0.4%), because stocks are the cushion when falling yields shrink coupon income.
- **More stocks with the ladder unchanged moves money from the co-sponsor minimum to Laura, almost dollar for dollar.** At VT = 25% of the 2028 deposit the minimum falls $15k, to $120k, and Laura gains about $7k at the median. At 15% of all her money the minimum falls to $80k. 40% of all her money cannot be done without selling the ladder: the most VT can be is about 30%.
- **Corporate iBond funds for the 2033-36 payments are the closest call.** They are about $9.3k cheaper on FRED spreads, and the median total rises about $10k (mostly to Laura, under the plan's own rules). The price: four payments carry company credit risk (model short 0.37% instead of 0.02%, with the assumed losses), WInS listing is UNVERIFIED, about 8 trades after the TNA, and two filed notes say "a fund holding 2033/2035 Treasuries".
- **Both glide paths lose.** The sleeve glide (VT into Treasuries 2029-32) costs about $3k of median total and buys nothing: in history it breaks the minimum *more* often (0.9% against 0.4%). The whole-portfolio glide (Wharton's example-note idea, 50% stocks falling to 0%, ladder bought in 2033) has the same median total as the current plan ($205k), but its 1-in-20 total is $86k against $154k, and its gift falls below its own minimum about 1 time in 20.
- **TIPS are not allowed** (FAQ:54). Even if they were, a TIPS ladder sure to pay $50k at zero inflation would cost about 1.27 times as much, more than the $300k deposit.

## 2. The one basis (every number below uses it)

| Item | Basis |
|---|---|
| Curve | treasury.gov daily par yield curve, **Mon 19 Oct 2026 close** (latest row; fetched 19 Oct 21:40 UTC = Tue 20 Oct 08:40 Sydney). 1y 4.50, 2y 4.77, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48. URL: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv (copy: `oct20/alternatives/data/tsy_202610_fetch20oct.csv`). Yields rose about 5-6bp from 16 Oct |
| Ladder | Caplet's real WInS holdings' maturity dates (IBTM-IBTR as par bonds ending 15 Dec; T-bonds 4.750% Feb-37, 4.500% May-38, 4.375% Nov-39, 4.250% Nov-40, 3.125% Nov-41 with real coupons). Each rung is sized to hold $50,000 on its own maturity date with income reinvested at its own yield; the cash then waits at 0% to 1 Jan. Curve held unchanged to 1 Jan 2027, then a random move. **Cost $298,446, room $1,554** under $300k on this basis (16 Oct: $300,174) |
| Model | The 19 Oct coupon-study Monte Carlo, **copied unchanged** (`oct19/coupon/scripts/coupon_options.py`). The copy reproduces the study's results file byte for byte on the 16 Oct curve (`cmp` = identical). The new engine (`alt_engine.run_alt`) is a generalised copy of the study's `run()`; with default settings it matches the study's option 3r and option 1 path by path (maximum difference 0.0). Rates: parallel random walk, 1.0 point a year, floor 0.25%. Stocks (VT): 7.0% compound, 16.78% volatility, 0.06% fee (JPM 2026 LTCMA AC World). Seed 20261019, **100,000 paths** |
| History | **690 windows**: plan Jan 2027 = each month from Apr 1953 to Sep 2010 (FRED GS10 + Shiller US total return). Additive yield moves (main) and proportional (check) |
| Joint stress | Stock-yield correlation +0.5 (positive = stocks and yields fall together; it was +0.32 in 2000-21, `oct19/coupon/coupon_risk_options.md:73-82`); named paths 2008, 2020, 1980s (absolute), 1973-74 and "storm" (yields −3 points by 2029, VT −50% in 2032); the 2028 deposit at $75k or missing |
| Plan rules (current plan) | Jan 2027: the ladder. Jan 2028: fill any ladder gap, then $10k into the Nov-2041 Treasury (3r reserve), then IBTM sized to repay the rest in Dec 2032 (the floor), then VT with what is left (about $30.9k on this curve). 2031 range: minimum = floor − $3,700 rounded down to $5k; top = floor + half of VT + the reserve. 2033: gift = floor + half of VT, capped at the top, plus any reserve release; Laura keeps the other half. The 2027 leftover is the first cover, then the reserve, then Laura's half, then the gift above the floor (`oct19/coupon/coupon_risk_options.md:26-31, 126-134`) |

**What each column means.**
- *Short* = some payment cannot be paid in full from money the plan commits (more than $100 short).
- *2031 range* = the median minimum and top Laura would announce. *Inside* = the share of paths where the 2033 gift is at least the announced minimum (the gift can never exceed the top).
- *Gift* = the 2033 facility contribution: median, and 1-in-20 low (5th percentile).
- *Laura's flexibility* = what stays hers: her free money in 2033 plus what comes back after the last payment in 2042.
- *Total* = gift + flexibility money.

**Rules for the strategies that do not buy the ladder in 2027** (growth-first, whole glide). These are stated choices that mirror the current plan, so only the investing differs:
- Jan 2033: the ten payments are bought at that day's curve, priced at payment dates. This flatters them by about 1.6%, since there are no WInS date gaps and no coupon risk; a variant adds that premium back.
- Minimum = the model's 1-in-20 low of the 2033 free money, given the Jan 2031 state (inner Monte Carlo, same model), rounded down to $5k.
- Top = minimum + half of (the free money if the payments were locked in Jan 2031, less the minimum).
- Gift = minimum + half of the excess, capped at the top.

## 3. The table judges would ask for (Monte Carlo, correlation 0; history = 690 windows)

| Alternative | Payment short: chance (model / history) | Size if short (model worst / history worst) | 2031 range (median) and chance the gift is inside (model / history) | Gift median / 1-in-20 low | Laura's flexibility (median) | Total median / 1-in-20 low / 1-in-20 high | Complexity (5 = simplest) and WInS trades to mirror it | Rule compliance | Reason it wins or loses (note form) |
|---|---|---|---|---|---|---|---|---|---|
| **1 Current plan: Root-and-Branch + 3r $10k reserve** | **0.02% / 0%** | **$0.6k / $0** | **$135k-$166k; 99.94% / 99.57%** | **$163.3k / $136.7k** | **$41.5k** ($20.5k in 2033 + $19.9k in 2042) | **$204.6k / $154.1k / $270.4k** | 4; 0-2 trades (reserve) | All holdings WInS-listed Treasuries, Treasury ETFs and VT (FAQ:44-47); payments funded inside the portfolio (case:91-92) | Wins: the only design with near-zero payment risk *and* a minimum that holds in history |
| 1x Same plan without the reserve (IPS V5 as written) | 15.6% / 29.3% | $6.2k / $2.9k | $145k-$167k; 98.05% / 97.39% | $166.2k / $138.8k | $31.6k | $197.0k / $146.2k / $256.3k | 5; 0 | Small gaps after 2033 are paid from money Laura has already taken out, which fails case:91-92 (`oct19/coupon/coupon_risk_options.md:106-111`) | Loses: frequent small payment gaps |
| 2 All-Treasury (VT replaced by a Dec-2032 Treasury; same minimum) | 0.02% / 0% | $0.6k / $0 | $135k-$166k; 99.95% / 98.84% | $163.7k / $135.6k | $36.6k | $199.7k / $152.1k / $255.7k | 4.5; 2 trades (sell VT, buy IBTM) | Allowed; contradicts the filed VT note, a likely TNA pick (TNA:25-31 allows a sold position, but it must be explained) | Loses: same gift and payments, less for Laura; in history the minimum breaks more often (1980s path: $123.6k gift against a $135k minimum) |
| 2b All-Treasury, locked half counted in the minimum | 0.02% / 0% | $0.6k / $0 | **$150k**-$166k; 99.67% / 97.68% | $163.7k / $135.6k | $36.6k | $199.7k / $152.1k / $255.7k | 4.5; 2 | As 2 | The one real gain of all-Treasury is a $15k higher announced minimum, but it breaks 1 window in 43 in history |
| 3 More stocks: VT = 25% of the 2028 deposit ($37.5k) | 0.02% / 0% | $0.6k / $0 | $120k-$162k; 100% / 100% | $159.1k / $127.0k | $48.5k | $207.1k / $153.4k / $272.3k | 4; 2 trades (sell IBTM, buy VT) | Allowed | Neutral: the minimum drops $15k for +$2.5k median total |
| 3 VT = 40% of the 2028 deposit ($60k) | 0.02% / 0% | $0.6k / $0 | $95k-$146k; 100% / 100% | $143.2k / $111.2k | $66.4k | $209.6k / $148.3k / $286.8k | 4; 2 | Allowed | Loses for co-sponsors: minimum −$40k; worse 1-in-20 total |
| 3 VT = 15% of all money after Jan 2028 (~$69.5k) | 0.02% / 0% | $0.6k / $0 | $80k-$139k; 100% / 100% | $136.4k / $104.2k | $73.7k | $210.3k / $145.6k / $293.5k | 4; 2 | Allowed | Loses: minimum −$55k for +$5.7k median |
| 3 VT = 25% of all money (~$115.9k) | 0.02% / 0% | $0.6k / $0 | $25k-$107k | $103.3k / $67.8k | $108.0k | $212.2k / $128.4k / $330.0k | 4; 2 | Allowed | Loses: a $25k minimum is not a "meaningful" lead gift (case:110-112) |
| 3 VT = 40% of all money | not possible | | VT capped at the whole 2028 remainder ($140k, about 30%): minimum $0 | $88.4k / $54.2k | $121.9k | $211.9k / $120.5k / $347.8k | | Needs ladder sales to reach 40%, which breaks the payment match | Not feasible with the ladder unchanged |
| 4 Growth-first (team's original idea: 75% stocks 2027-30, 60% 2031, 40% 2032; ladder bought Jan 2033) | **4.55% / 0%** | **$238k / $0** | $115k-$159k; 96.84% / 96.52% | $151.5k / **$0** | $73.5k | **$239.0k / $5.0k / $604.2k** | 3; about 11-12 trades (sell all 10 bond holdings, buy an intermediate Treasury ETF) | Securities allowed (intermediate Treasury ETF listing UNVERIFIED); fails "high degree of certainty" | Loses: the highest median, but a 1-in-22 chance of missing payments, and the 1-in-20 total is about $5k |
| 4 Growth-first, 75% stocks to 2033 | 5.97% / 0% | $254k / $0 | $70k-$136k | $122.1k / $0 | $98.5k | $244.4k / $0 / $660.2k | 3; about 12 | As above | Loses (worse) |
| 5 Corporate iBond funds for 2033-36 (IBDX, IBDY, IBDZ, IBCA in place of IBTM-IBTQ rungs; FRED spreads; credit losses assumed) | 0.37% / 0% | $5.0k / $0 | $135k-$168k; 99.90% / 100% | $165.9k / $146.1k | $47.9k | $214.4k / $161.9k / $280.9k | 3; about 8 trades (partial IBTM sale, IBTO, IBTP, IBTQ out; four corporate funds in) | Allowed only if WInS lists the funds (UNVERIFIED); individual corporate bonds are not allowed (FAQ:44-47, 56); conflicts with the filed IBTO/IBTQ notes | Closest call: about +$10k total, but credit risk enters four payments, and it needs 8 trades and a listing check after the TNA |
| 6a Glide inside the sleeve (VT moved into a Dec-2032 Treasury, a quarter each Jan 2029-32) | 0.02% / 0% | $0.6k / $0 | $135k-$166k; 99.95% / 99.13% | $163.9k / $136.4k | $38.1k | $201.9k / $153.1k / $262.1k | 3; 0 now, 4 later in the real plan | Allowed; conflicts with "left unrebalanced until 2033" in V5 (`oct19/drill/defence_drill.md:187`) | Loses: costs Laura about $3k at the median, and the minimum holds *less* often in history |
| 6b Whole-portfolio glide (Wharton example-note style: 50% stocks falling 10 points a year to 0% in 2032, intermediate Treasury fund, ladder bought Jan 2033) | 0.12% / 0% | $67.5k / $0 | $160k-$173k; **95.36% / 95.94%** | $171.5k / **$69.6k** | $31.0k | $205.1k / **$85.8k** / $357.8k | 2.5; about 12 trades | Securities allowed (fund listing UNVERIFIED) | Loses: same median as the current plan; the range looks better but breaks 1 time in 20, and the bad case is far worse |
| 7 TIPS | — | — | — | — | — | — | — | **Not permitted** (FAQ:54) | Excluded by rule; also the wrong match for fixed nominal payments (case:90) |

Notes on the table:
- **History shows no growth-first payment miss.** In the 1953-2010 windows the worst 6-year US stock runs were never bad enough. The model's miss comes from the wider tails of its rate random walk: a 2.5-point standard deviation of the 2033 yield move, which reprices a $370k-plus ladder. This is one reason the team should quote both.
- **Growth-first, with the 1.6% holdings premium added back:** short 5.14%, gift median $145.2k.
- **Corporate variants:**
  - No credit losses: short 0.02%, total median $216.7k.
  - iShares per-fund spreads (72/78/87/90bp, 14-15 Oct): saving $8.0k, short 0.41%.
  - Adding IBCB for 2037 (5 rungs): saving $12.2k, short 0.59%, worst $5.9k.
  - If the saving is put into the floor instead of kept as cover: minimum $145k, gift median $177.5k, but short 0.88% (model) and 0.72% (history), because the first layer of cover is gone.
- **Current plan with the 2027 leftover added to the floor (1y):** gift median $167.3k, Laura's flexibility $36.0k, total unchanged. This is a split choice, not a better plan.

## 4. Each alternative: what was tested, what it shows, what the team must decide

### (1) Current plan: Root-and-Branch + 3r reserve
- **Sizes on this curve (no rate move):** ladder $298,446; the Jan 2028 split is $10k reserve / IBTM floor repaying $140,000 / VT $30,948; announced minimum $135,000 (`oct20/alternatives/data/run19oct/stage_meta.json`). This mirrors the 19 Oct study (`oct19/coupon/coupon_risk_options.md:33-48`), now on the 19 Oct curve.
- **Why it holds up:**
  - The payments are bought before anything risky.
  - The reserve sits in the long bond, whose price rises when yields fall, the same time coupons earn less.
  - Stocks only decide how far above the minimum the gift goes and how much Laura keeps.
- **Gift reaches the top in 42% of paths.** The top is "floor + half of today's VT + reserve", so it is ambitious by design. If the team wants "usually reaches the top", that is a rule change (D6, `oct19/out/Caplet_Update_19Oct2026.md:332`).
- **Weak spot:** the 1980s absolute path (yields fall about 5 points): gift $136.2k against $135k. It holds, by about $1k on this curve; on 16 Oct it broke by $3.5k (`oct19/coupon/coupon_risk_options.md:97`). History breaks the minimum in 3 of 690 windows (0.43%; worst −$8.7k, Oct 1981 start).

### (2) All-Treasury (no VT)
- **What it means:** the ~$31k VT money buys a Treasury maturing Dec 2032 (IBTM) instead. Same reserve, same split rule (half to the gift, half to Laura), same minimum. Variant 2b also counts the locked half in the minimum.
- **What it shows:**
  - Payments are unchanged (0.02%). VT never touches the payments.
  - The gift is unchanged (median $163.7k against $163.3k). The gift is capped at the 2031 top, so stock gains after 2031 go to Laura.
  - The losses are Laura's: flexibility −$4.9k median, total 1-in-20 high −$14.7k ($255.7k against $270.4k).
  - In history, the minimum breaks in 1.16% of windows against 0.43%. In falling-yield decades stocks usually rose, so Laura's half covered the coupon gap. A locked Treasury bought at low 2028 yields does not.
  - Under the joint stress (correlation +0.5) the two are equal (0.05% against 0.08%).
- **Its one real advantage:** a firmer, higher announced minimum (2b: $150k against $135k). That minimum breaks in 2.3% of history windows, because the coupon gap can still eat it.
- **The judge question it answers:** "Why hold stocks at all when the client needs certainty?" The evidence: stocks cost the payments nothing (they sit only above the floor), they give Laura upside and flexibility (case:101-103, "flexibility as the project develops"), and in history they protected the minimum better than Treasuries did. The case also says she "has been willing to take thoughtful risks" (case:68-72).

### (3) More stocks in the growth sleeve (ladder unchanged)
- **What "post-2028 money" means.** It is ambiguous, so both readings are run.
  - (a) The share of the 2028 deposit. Today's VT is about 21% of it.
  - (b) The share of all Laura's money after Jan 2028, about $463.5k (= $300k grown one year at the 1-year yield + $150k). On this reading today's VT is about 7%, the figure WInS mirrors as about 9% (`oct19/out/Caplet_Update_19Oct2026.md:261`).
  - Every extra VT dollar comes out of the IBTM floor, since the ladder and reserve stay fixed.
- **Results** (minimum / gift median / Laura median / total median / total 1-in-20):

| VT size | Minimum | Gift median | Laura's flexibility | Total median | Total 1-in-20 low |
|---|---|---|---|---|---|
| 15% of the 2028 deposit ($22.5k; less than today) | $140k | $169.3k | $35.8k | $204.5k | $154.9k |
| **Today (~21%, $30.9k)** | **$135k** | **$163.3k** | **$41.5k** | **$204.6k** | **$154.1k** |
| 25% of the 2028 deposit ($37.5k) | $120k | $159.1k | $48.5k | $207.1k | $153.4k |
| 40% of the 2028 deposit ($60k) | $95k | $143.2k | $66.4k | $209.6k | $148.3k |
| 15% of all money ($69.5k) | $80k | $136.4k | $73.7k | $210.3k | $145.6k |
| 25% of all money ($115.9k) | $25k | $103.3k | $108.0k | $212.2k | $128.4k |
| 40% of all money | not possible (capped at $140k, about 30%) | $88.4k | $121.9k | $211.9k | $120.5k |

- **Payments are unchanged in every row** (0.02%). More VT also never broke the minimum in history (0 of 690). A smaller floor leaves more slack, and in target mode the floor floats down automatically when yields fall before 2028.
- **The trade-off is a split, not a better plan.** Each extra $10k of VT cuts the minimum by about $13k, because a floor dollar bought in 2028 repays about $1.28 in Dec 2032. It adds only about $1-2k to the median total. The 1-in-20 total gets worse as soon as VT grows past today's size.
- **The consistent finding:** equity weight barely moves the median total. This echoes the 27 Sep result, where a 50-70% sleeve gave medians of $205k-$209k (`/home/user/caplet-investment/CLAUDE.md`, open items).
- **Team decision this informs:** D6/D9 (floor size), `oct19/out/Caplet_Update_19Oct2026.md:332-335`. Smaller VT (15% of the deposit) is also a live option: minimum $140k, gift median $169.3k, Laura −$5.7k.

### (4) Growth-first (the team's original ~75% equity idea)
- **Definition:** the team's 27 Sep model, re-run on this basis.
  - Glide: 75% VT in 2027-30, 60% in 2031, 40% in 2032 (`/home/user/caplet-investment/research/verified_2026-09-27/strategy_mc.py:41-42`).
  - The rest is in an intermediate Treasury fund (IEF-type: duration 6.86, 8.5-year yield, 0.15% fee).
  - Rebalanced every January; the 2028 deposit is added; the ladder is bought on 1 Jan 2033.
- **Results:**
  - Payment miss 4.55% (independent annual-step check with different code: 4.71%, `oct20/alternatives/scripts/indep_check_growth_first.py`).
  - Missing more than $10k: 3.8%. The 1-in-100 miss is $69k.
  - Correlation +0.5: 6.38%, worst $273k.
  - 2028 deposit only $75k: 15.3%. Missing: 39.2%.
  - Free money in 2033: 1-in-20 $5.0k, median $239.0k, 1-in-20 high $604.2k.
- **Compared with the 27 Sep run** (3.2% miss; 13.7% at $75k; 40.8% at $0): higher here, because the ladder now costs more relative to $300k (room $1.6k against $7.7k on 25 Sep) and the rate model is monthly with a 0.25% floor.
- **History:** 0 misses in 690 windows. But the gift falls below its own minimum in 3.5% of windows (worst −$62.5k, Sep 1996 start: bought near the top and crashed in 2000-02), and the 1-in-20 gift is $17k.
- **Why it loses** (evidence for the team's own words):
  - "High degree of certainty" means the payments' price must not depend on 2033 markets. Here it does, and the case bans outside money to fill a gap (case:91-92).
  - Its 2031 range must be built from a model forecast, so it breaks about 1 time in 20 by construction. The case warns that overpromising damages credibility (case:114-116).
  - It is the team's own earlier idea. Moving from it to lock-early is a true, dated decision for the Articulation section (`oct19/judges/qa_bank.md:54`, Q36), if a student records who argued what.

### (5) Corporate iBond funds for the 2033-36 rungs
- **What exists** (stockanalysis.com BlackRock fund list, read 19 Oct 2026, `oct20/alternatives/web/sa_blackrock_provider_19oct.html`):
  - IBDX (Dec 2032), IBDY (Dec 2033), IBDZ (Dec 2034), IBCA (Dec 2035) and IBCB (Dec 2036) Term Corporate ETFs, each 0.10% a year, against 0.07% for the Treasury iBonds.
  - No dated corporate fund exists for 2037-41 (`/home/user/snap/main/research/assistant_review_2026-10/oct16/lenses/G2.md:44-56`).
  - **WInS listing of every one is UNVERIFIED.** WInS ticker names can clash: "IBTN on WInS is INSCORP Inc" (`/home/user/snap/main/COMPETITION.md:94`).
- **Spreads (FRED, ICE BofA option-adjusted spreads, 16 Oct 2026, the latest FRED value; accessed 19 Oct 2026):**
  - 3-5y 0.75%; 5-7y 0.88% (BAMLC3A0C57Y), used for the Dec 2032/2033 funds; 7-10y 1.04% (BAMLC4A0C710Y), used for Dec 2034/2035.
  - All IG 0.85%; A 0.71%; BBB 1.06%; AA 0.61%.
  - URLs: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC3A0C57Y (and the same pattern for each id).
  - FRED now carries only about 3 years of ICE data (from 20 Oct 2023), so no long spread history was available there.
  - Net spread = spread − 0.03% fee gap. iShares' own per-fund OAS (72/78/87/90bp, 14-15 Oct) is the check.
- **Credit losses (ASSUMPTION; the S&P primary study returned HTTP 403):**
  - Expected loss 0.10% a year, plus a 3% stress loss on each corporate rung if VT falls more than 30% over any 12 months before that rung matures.
  - That trigger fires in 18.5% of model paths by Dec 2035 and in 29% of history windows.
  - Basis: S&P data as reproduced by FIIG. An A− bond has a 0.41% historical 5-year default incidence, BBB− 2.31%, and global investment-grade defaults "peaked at 14 in 2008" (https://thewire.fiig.com.au/article/2026/07/15/attempting-to-quantify-the-risk-of-bonds-with-credit-ratings, accessed 19 Oct 2026). A 40% recovery is UNVERIFIED.
  - The 3% stress is meant to cover defaults plus forced sales of downgraded bonds. Whether the funds sell fallen angels is UNVERIFIED.
- **Results:**
  - Ladder $289,121 (−$9,325).
  - Short 0.37% (worst $5.0k), against 0.02%.
  - Gift median +$2.6k; 1-in-20 gift +$9.4k ($146.1k against $136.7k), because the bigger 2027 leftover is the first cover.
  - Laura +$6.4k; total +$9.8k median, +$7.8k at 1-in-20.
  - History: no shortfall, and the minimum never broke.
  - Joint stress (+0.5): short 0.40%, worst $5.7k.
- **Cross-check with the 16 Oct review:** it found about $10.7k freed for five funds (2033-37) before losses (G2.md:31). Here, five funds on FRED spreads free $12.2k; four on iShares spreads free $8.0k. These agree in size.
- **The judgement:**
  - It is real money, but it moves the payments' risk from "the US Treasury" to "about 400 company bonds per fund, about half rated BBB" (G2.md:41-43).
  - Under the current split rules most of the gain goes to Laura, not the co-sponsors.
  - Executing it before 6 Nov means about 8 trades after the TNA, a listing check, and new notes. The filed IBTO note ("we use a fund holding 2033 Treasuries instead") and IBTQ note stay on record (`/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:20, :22`).
  - **Best use:** the priced "why not corporates" answer in the Final Report, not a trade (same conclusion as R16 K6, `/home/user/snap/main/research/assistant_review_2026-10/04_What_Stops_Us_Winning_16Oct2026.md:273`). A team vote is needed if anyone wants it in the real plan.

### (6) Glide paths
**Wharton's example note** says to buy "an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin preparing for Laura's future operating commitment ... as the residency funding date approaches" (TNA:36-39). It is an example of note style, not a recommended strategy. Two readings were tested:
- **6a, a glide inside the growth sleeve.**
  - The ladder and floor are unchanged. VT moves into a Treasury maturing Dec 2032 in four equal steps (Jan 2029, 2030, 2031, 2032).
  - Result: gift median $163.9k (+$0.6k); Laura −$3.4k; total −$2.7k median and −$8.3k at 1-in-20 high. The minimum breaks in 0.87% of history windows against 0.43%: selling VT removes the cushion in the falling-yield decades.
  - The 2031 range is the same, because the top is set on 2031 values either way.
  - **Reason it loses:** the minimum is already in Treasuries, so de-risking the part above it buys almost nothing and costs Laura's upside.
- **6b, a whole-portfolio glide** (the target-date idea).
  - 50% VT in 2027, falling 10 points a year to 0% in 2032; the rest in an intermediate Treasury fund; the ladder bought Jan 2033.
  - Result: payment miss 0.12% (worst $67.5k); 0.50% (worst $106k) under joint stress; 4.6% if the 2028 deposit is $75k; 43.8% if it is missing.
  - The median total ($205.1k) matches the current plan, but the 1-in-20 total is $85.8k against $154.1k.
  - Its announced range ($160k-$173k) looks better, but the gift falls below the minimum in 4.6% of paths (model) and 4.1% (history). The worst history window is −$65k (Sep 1975 start).
  - **Reason it loses:** the payments' price stays unknown until 2033, so the range has to be a forecast.

### (7) TIPS: explained, not modelled
- **The rule.** The live FAQ lists "TIPS (Treasury Inflation-Protected Securities)" under "NOT permitted" (FAQ:54), and also STRIPS (FAQ:55). Whether the ban also covers WInS-listed TIPS ETFs (TIP 0.18%, STIP, on the same fund list) is UNVERIFIED; ask in batch 2 (`oct19/out/Caplet_Update_19Oct2026.md:379`). Meanwhile, name none.
- **Why TIPS would be the wrong match even if allowed.** Each payment "is a fixed $50,000 and is not adjusted for inflation" (case:90). Illustration on the 19 Oct treasury.gov curves (real yields 5y 2.56, 7y 2.67, 10y 2.80, 20y 3.06; https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_real_yield_curve&field_tdr_date_value_month=202610&page&_format=csv; rough annual compounding, `oct20/alternatives/scripts/tips_illustration.py`):
  - The market's breakeven inflation is about 2.3% a year for 2033-42.
  - A TIPS ladder sure to pay $50k even at zero inflation would cost about $372k against $294k for nominal Treasuries (1.27 times). That is more than the $300k deposit.
  - Sized at breakeven inflation it costs the same as nominal Treasuries, but every payment comes up short whenever inflation runs below 2.3%. At 1 point below, every year, the ten payments would be about $50k short in total: roughly one whole payment.
- **Where inflation does matter:** the facility's cost and Laura's flexibility money (case:147). That is a sentence about risk, not a holding.

## 5. Historical replay (690 windows, starts Apr 1953-Sep 2010, additive yields)

| Alternative | Payment short | Gift median / 1-in-20 | Gift below minimum | Worst gift minus minimum (start) | Laura's flexibility (median) |
|---|---|---|---|---|---|
| 1 Current plan + 3r | 0% | $168.7k / $153.7k | 0.43% | −$8.7k (Oct 1981) | $43.3k |
| 1x Without the reserve | 29.3% (worst $2.9k) | $171.3k / $160.7k | 2.61% | −$39.7k (Oct 1981) | $33.4k |
| 2 All-Treasury | 0% | $166.7k / $151.8k | 1.16% | −$16.6k (Oct 1981) | $33.9k |
| 3 VT 25% of deposit | 0% | $165.2k / $147.9k | 0% | +$19.7k | $49.8k |
| 3 VT 15% of all money | 0% | $145.9k / $125.3k | 0% | +$34.8k | $79.2k |
| 4 Growth-first | 0% | $212.0k / $17.2k | 3.48% | −$62.5k (Sep 1996) | $111.2k |
| 5 Corporate 2033-36 | 0% | $169.5k / $157.3k | 0% | +$8.8k | $52.4k |
| 6a Sleeve glide | 0% | $167.8k / $152.1k | 0.87% | −$12.1k (Oct 1981) | $38.5k |
| 6b Whole glide | 0% | $189.6k / $97.1k | 4.06% | −$65.1k (Sep 1975) | $39.5k |

- **Proportional replay** (yields scaled, not shifted): no option breaks a payment except 1x (30.7%) and corporate-with-saving-in-the-floor (0.87%). The current plan never breaks its minimum (0%), against growth-first 3.5% and the whole glide 2.6% (full table in the appendix).
- **Caution:** history uses US stocks (not world), monthly-average prices (which smooth crashes) and the 10-year yield moved in parallel. 690 overlapping windows are not 690 independent tests.

## 6. Joint stress

**Stocks and yields falling together (correlation +0.5, 100,000 paths):**

| Alternative | Short | Worst short | Gift below minimum | Any promise broken | Gift median / 1-in-20 |
|---|---|---|---|---|---|
| 1 Current plan + 3r | 0.02% | $0.6k | 0.08% | 0.10% | $163.8k / $136.2k |
| 2 All-Treasury | 0.02% | $0.6k | 0.05% | 0.07% | $163.7k / $135.6k |
| 3 VT 25% of deposit | 0.02% | $0.6k | 0% | 0.02% | $159.5k / $126.6k |
| 4 Growth-first | 6.38% | $273.0k | 3.06% | 9.28% | $153.9k / $0 |
| 5 Corporate 2033-36 | 0.40% | $5.7k | 0.20% | 0.60% | $166.3k / $145.6k |
| 6a Sleeve glide | 0.02% | $0.6k | 0.08% | 0.10% | $164.3k / $135.9k |
| 6b Whole glide | 0.50% | $106.0k | 3.98% | 4.48% | $175.0k / $55.8k |

**Named paths (gift against announced minimum; payments paid unless stated):**

| Alternative | 2008 (Jan 2007 start) | 1980s (yields −5 pts) | 1973-74 (Jan 1972 start) | Storm (yields −3, VT −50% in 2032) |
|---|---|---|---|---|
| 1 Current plan + 3r | $154.9k vs $135k | $136.2k vs $135k | $163.3k vs $135k | $146.7k vs $135k |
| 2 All-Treasury | $155.2k vs $135k | **$123.6k vs $135k (broken)** | $169.8k vs $135k | $152.8k vs $135k |
| 4 Growth-first | $49.9k vs $10k | $236.9k vs $180k | $107.4k vs $70k | **$35.6k vs $50k (broken)** |
| 5 Corporate 2033-36 | $155.6k vs $135k | $151.9k vs $135k | $163.3k vs $135k | $146.7k vs $135k |
| 6a Sleeve glide | $151.8k vs $135k | **$132.5k vs $135k (broken)** | $164.4k vs $135k | $153.4k vs $135k |
| 6b Whole glide | $87.5k vs $75k | $174.7k vs $155k | $147.9k vs $140k | $115.1k vs $100k |

Under growth-first a co-sponsor would have heard a minimum of $10k after 2008, against $135k under the current plan. A "range" that low is not a meaningful lead gift (case:110-112).

**The 2028 deposit (case:44-45: earnings from "publishing advances, speaking engagements, licensing").**

| Alternative | Deposit $75k: short / worst / minimum / gift median | Deposit missing: short / mean if short / worst |
|---|---|---|
| 1 Current plan + 3r | 0.02% / $0.6k / $60k / $78.8k | 51.5% / $16.7k / $89.0k |
| 2 All-Treasury | 0.02% / $0.6k / $60k / $78.6k | 51.5% / $16.7k / $89.0k |
| 4 Growth-first | 15.3% / $276.2k / $30k / $64.2k | 39.2% / $74.5k / $327.8k |
| 6b Whole glide | 4.63% / $143.8k / $75k / $84.1k | 43.8% / $42.3k / $220.2k |

**Read the "missing" column carefully.**
- With no 2028 deposit, the current plan misses some payment in about half of the paths, more often than growth-first. On this curve the Jan 2027 ladder costs more than $300k about half the time (room $1.6k), and nothing tops it up.
- But the typical gap is $16.7k (about a third of one payment), against $74.5k for growth-first. The worst case is $89k against $328k.
- **Honest summary:** the current plan depends on the 2028 deposit only for a small top-up and the facility; growth-first depends on it for the payments themselves. Never claim "no payment risk even without the 2028 deposit".

## 7. What a strong "why not X?" answer needs (for the Final Report and any Q&A; students write the words)

1. **One basis, named and dated**: the curve date, holdings' dates, "MODEL", 100,000 paths, 690 windows. Never mix it with the payment-date basis or the 16 Oct numbers (`oct19/out/Caplet_Update_19Oct2026.md:221-248`).
2. **For each alternative, three numbers:** the payment risk, the minimum Laura can announce, and what Laura keeps. Judges care about the trade-off, not the median.
3. **The surprising facts are the strongest:**
   - all-Treasury does not raise the gift;
   - more stocks moves money from co-sponsors to Laura;
   - the sleeve glide makes the minimum *less* safe in history;
   - the target-date glide has the same median and a much worse bad case;
   - corporates are worth about $10k and are rejected for a stated reason, not ignored.
4. **Rule facts quoted exactly:** FAQ:44-47 and 54-56 (permitted and banned); case:90 (nominal payments); case:91-92 (no outside money).
5. **AI use logged:** these models are AI-built. Any figure used must be re-run or re-checked by a student and recorded in the Works Cited.

## 8. Limits and UNVERIFIED items

- **Model limits:**
  - Rates: a parallel random walk with no pull back, which gives wider tails than history.
  - The iBond funds are treated as par bonds.
  - Stocks: lognormal, with JPM's 7.0% and 16.78%.
  - The 2031 range rule for growth-first and the whole glide is my stated choice (mirroring "firm floor + half of today's upside"). A different rule changes their range numbers, but not their payment risk.
  - The corporate credit-loss model (0.10% a year + 3% stress on a stock crash) is an ASSUMPTION; FIIG is a secondary source for S&P.
  - Growth-first's 2033 ladder is priced on the cheaper payment-date basis (a variant with the premium is shown).
  - No taxes; WInS commissions not counted.
- **UNVERIFIED:**
  - WInS listing of IBDX/IBDY/IBDZ/IBCA/IBCB, of any intermediate Treasury ETF (IEF-type) and of TIP/STIP.
  - Whether the TIPS ban covers TIPS ETFs.
  - Whether the corporate iBonds sell downgraded bonds.
  - Recovery rates.
  - The WInS price of the Nov-2041 bond for the reserve.
  - All WInS trade counts are approximate and must be recomputed live by the trader.
- **The curve moves.** Room under $300k is $1,554 on 19 Oct (it was −$174 on 16 Oct on the same basis). Re-run the whole set on the 6 Nov close before any number goes in the Final Report (`oct19/out/Caplet_Update_19Oct2026.md:100`).

## 9. Files and how to re-run (all in `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/alternatives/`)

- `scripts/coupon_options.py`, `scripts/indep_pricer.py`: copied unchanged from `oct19/coupon/scripts/`. `data/repro16/coupon_options_results.json` is byte-identical to the 19 Oct study output.
- `scripts/alt_engine.py`: generalised engine (`run_alt`) plus the growth-first/glide engine (`run_wealth`). `scripts/check_equivalence.py` proves `run_alt` equals the study's options 3r and 1 path by path.
- `scripts/run_alternatives.py`: all options and scenarios. It is resumable and writes `data/run19oct/stage_*.json`, `alternatives_results.json` and `alternatives_table.csv`.
  - Command: `NPATHS=100000 ../../venv/bin/python -I scripts/run_alternatives.py data/tsy_202610_fetch20oct.csv 10/19/2026 scripts/fred_GS10_monthly.csv data/shiller_monthly.csv data/run19oct` (about 40 minutes).
- `scripts/tables.py`: prints every table in the appendix from the JSON (`data/tables_19oct.md`).
- Checks:
  - `scripts/indep_check_growth_first.py`: independent growth-first check, 4.71%.
  - `scripts/flat_check.py`: deterministic paths.
  - `scripts/crash_freq.py`: how often the credit-stress trigger fires.
  - `scripts/tips_illustration.py`: the TIPS illustration.
- Downloaded sources: `web/` (treasury.gov nominal and real curves, FRED spread CSVs, the stockanalysis fund list).

## Appendix: full generated tables (`scripts/tables.py`, 19 Oct curve, 100,000 paths)

### Monte Carlo, correlation 0 (100,000 paths), with history (additive) columns

| Option | Short: model / history | Worst short: model / history | 2031 range (median) | Gift median / 1-in-20 low | Gift below minimum: model / history | Gift reaches top | Laura's flexibility (median: 2033 + 2042) | Total facility + flexibility: median / 1-in-20 / 1-in-20 high |
|---|---|---|---|---|---|---|---|---|
| 1 Current plan (Root-and-Branch + 3r $10k reserve) | 0.02% / 0.00% | $0.6k / $0.0k | $135.0k-$165.8k | $163.3k / $136.7k | 0.06% / 0.43% | 42.4% | $41.5k ($20.5k + $19.9k) | $204.6k / $154.1k / $270.4k |
| 1x Current plan without the reserve (V5 as written) | 15.6% / 29.3% | $6.2k / $2.9k | $145.0k-$167.0k | $166.2k / $138.8k | 1.95% / 2.61% | 68.4% | $31.6k ($20.5k + $8.0k) | $197.0k / $146.2k / $256.3k |
| 1y Current plan, 2027 leftover joins the floor | 0.02% / 0.00% | $0.6k / $0.0k | $135.0k-$171.1k | $167.3k / $136.7k | 0.08% / 0.58% | 36.7% | $36.0k ($21.0k + $13.0k) | $204.7k / $154.0k / $272.4k |
| 2 All-Treasury (sleeve in a Dec-2032 Treasury; same minimum) | 0.02% / 0.00% | $0.6k / $0.0k | $135.0k-$165.9k | $163.7k / $135.6k | 0.05% / 1.16% | 36.8% | $36.6k ($19.3k + $17.3k) | $199.7k / $152.1k / $255.7k |
| 2b All-Treasury, locked half counted in the minimum | 0.02% / 0.00% | $0.6k / $0.0k | $150.0k-$165.9k | $163.7k / $135.6k | 0.33% / 2.32% | 36.8% | $36.6k ($19.3k + $17.3k) | $199.7k / $152.1k / $255.7k |
| 3 VT = 15% of the 2028 deposit ($22.5k) | 0.02% / 0.00% | $0.6k / $0.0k | $140.0k-$171.7k | $169.3k / $136.4k | 0.00% / 0.00% | 38.7% | $35.8k ($15.5k + $19.0k) | $204.5k / $154.9k / $263.5k |
| 3 VT = 25% of the 2028 deposit ($37.5k) | 0.02% / 0.00% | $0.6k / $0.0k | $120.0k-$161.5k | $159.1k / $127.0k | 0.00% / 0.00% | 47.8% | $48.5k ($25.9k + $20.7k) | $207.1k / $153.4k / $272.3k |
| 3 VT = 40% of the 2028 deposit ($60k) | 0.02% / 0.00% | $0.6k / $0.0k | $95.0k-$145.9k | $143.2k / $111.2k | 0.00% / 0.00% | 55.4% | $66.4k ($41.6k + $22.2k) | $209.6k / $148.3k / $286.8k |
| 3 VT = 15% of all money after Jan 2028 (~$69.5k) | 0.02% / 0.00% | $0.6k / $0.0k | $80.0k-$139.3k | $136.4k / $104.2k | 0.00% / 0.00% | 57.4% | $73.7k ($48.3k + $22.6k) | $210.3k / $145.6k / $293.5k |
| 3 VT = 25% of all money (~$115.9k) | 0.02% / 0.00% | $0.6k / $0.0k | $25.0k-$107.1k | $103.3k / $67.8k | 0.00% / 0.00% | 62.7% | $108.0k ($80.6k + $23.7k) | $212.2k / $128.4k / $330.0k |
| 3 VT = 40% of all money (not possible: capped at ~30%, $140k) | 0.02% / 0.00% | $0.6k / $0.0k | $0.0k-$92.8k | $88.4k / $54.2k | 0.00% / 0.00% | 63.8% | $121.9k ($94.2k + $24.0k) | $211.9k / $120.5k / $347.8k |
| 4 Growth-first (75/75/75/75/60/40% stocks, ladder bought 2033) | 4.55% / 0.00% | $238.2k / $0.0k | $115.0k-$158.7k | $151.5k / $0.0k | 3.16% / 3.48% | 69.2% | $73.5k ($73.5k + $0.0k) | $239.0k / $5.0k / $604.2k |
| 4 Growth-first, 75% stocks to 2033 | 5.97% / 0.00% | $253.7k / $0.0k | $70.0k-$135.5k | $122.1k / $0.0k | 2.72% / 4.06% | 65.7% | $98.5k ($98.5k + $0.0k) | $244.4k / $0.0k / $660.2k |
| 4 Growth-first, with the same WInS-holdings premium on the 2033 ladder | 5.14% / 0.00% | $245.7k / $0.0k | $110.0k-$152.7k | $145.2k / $0.0k | 3.10% / 3.48% | 69.2% | $72.7k ($72.7k + $0.0k) | $232.6k / $0.0k / $597.6k |
| 5 Corporate iBonds for 2033-36 (FRED spreads, credit losses) | 0.37% / 0.00% | $5.0k / $0.0k | $135.0k-$167.8k | $165.9k / $146.1k | 0.10% / 0.00% | 45.6% | $47.9k ($21.0k + $25.8k) | $214.4k / $161.9k / $280.9k |
| 5 Corporate 2033-36, no credit losses | 0.02% / 0.00% | $0.6k / $0.0k | $135.0k-$167.8k | $166.1k / $147.1k | 0.05% / 0.00% | 47.3% | $50.3k ($21.0k + $28.2k) | $216.7k / $165.1k / $282.9k |
| 5 Corporate 2033-36, iShares per-fund spreads, losses | 0.41% / 0.00% | $5.0k / $0.0k | $135.0k-$167.7k | $165.7k / $144.6k | 0.11% / 0.00% | 44.7% | $46.4k ($20.9k + $24.4k) | $212.6k / $160.2k / $279.1k |
| 5 Corporate 2033-36, saving joins the floor | 0.88% / 0.72% | $5.0k / $3.5k | $145.0k-$182.0k | $177.5k / $146.1k | 0.24% / 1.01% | 33.5% | $35.7k ($22.2k + $11.4k) | $214.3k / $161.3k / $284.4k |
| 5 Corporate 2033-37 (adds IBCB), losses | 0.59% / 0.00% | $5.9k / $0.0k | $135.0k-$168.1k | $166.4k / $148.6k | 0.12% / 0.00% | 47.1% | $50.5k ($21.1k + $28.3k) | $217.4k / $164.4k / $284.2k |
| 6a Glide inside the sleeve (VT into a Dec-2032 Treasury, 1/4 a year 2029-32) | 0.02% / 0.00% | $0.6k / $0.0k | $135.0k-$166.0k | $163.9k / $136.4k | 0.05% / 0.87% | 39.1% | $38.1k ($19.8k + $17.5k) | $201.9k / $153.1k / $262.1k |
| 6b Whole-portfolio glide (50% stocks to 0% by 2032, ladder bought 2033) | 0.12% / 0.00% | $67.5k / $0.0k | $160.0k-$173.3k | $171.5k / $69.6k | 4.64% / 4.06% | 75.5% | $31.0k ($31.0k + $0.0k) | $205.1k / $85.8k / $357.8k |

Free money in Jan 2033 after buying the ladder (p5 / median / p95): growth-first $5.0k / $239.0k / $604.2k (shortfall above $10k in 3.8% of paths; 1-in-100 shortfall $69.1k); growth-first 75% flat −$10.3k / $244.4k / $660.2k (5.0%; $88.6k); whole glide $85.8k / $205.1k / $357.8k (0.07%; $0).

### Joint stress: stock-yield correlation +0.5

| Option | Short | Worst short | Mean short if short | Minimum (median) | Gift median / 1-in-20 | Gift below minimum | Any promise broken | Flexibility median |
|---|---|---|---|---|---|---|---|---|
| 1 Current plan (Root-and-Branch + 3r $10k reserve) | 0.02% | $0.6k | $0.3k | $135.0k | $163.8k / $136.2k | 0.08% | 0.10% | $40.6k |
| 1x Current plan without the reserve (V5 as written) | 15.6% | $6.2k | $1.3k | $145.0k | $166.2k / $137.0k | 2.87% | 17.7% | $31.2k |
| 1y Current plan, 2027 leftover joins the floor | 0.02% | $0.6k | $0.3k | $135.0k | $167.2k / $136.1k | 0.13% | 0.15% | $35.0k |
| 2 All-Treasury (sleeve in a Dec-2032 Treasury; same minimum) | 0.02% | $0.6k | $0.3k | $135.0k | $163.7k / $135.6k | 0.05% | 0.07% | $36.6k |
| 2b All-Treasury, locked half counted in the minimum | 0.02% | $0.6k | $0.3k | $150.0k | $163.7k / $135.6k | 0.33% | 0.35% | $36.6k |
| 3 VT = 15% of the 2028 deposit ($22.5k) | 0.02% | $0.6k | $0.3k | $140.0k | $169.7k / $135.9k | 0.01% | 0.02% | $35.0k |
| 3 VT = 25% of the 2028 deposit ($37.5k) | 0.02% | $0.6k | $0.3k | $120.0k | $159.5k / $126.6k | 0.00% | 0.02% | $47.7k |
| 3 VT = 40% of the 2028 deposit ($60k) | 0.02% | $0.6k | $0.3k | $95.0k | $143.5k / $110.8k | 0.00% | 0.02% | $65.6k |
| 3 VT = 15% of all money after Jan 2028 (~$69.5k) | 0.02% | $0.6k | $0.3k | $80.0k | $136.6k / $103.7k | 0.00% | 0.02% | $72.9k |
| 3 VT = 25% of all money (~$115.9k) | 0.02% | $0.6k | $0.3k | $25.0k | $103.3k / $67.5k | 0.00% | 0.02% | $107.0k |
| 3 VT = 40% of all money (not possible: capped at ~30%, $140k) | 0.02% | $0.6k | $0.3k | $0.0k | $88.5k / $54.2k | 0.00% | 0.02% | $120.8k |
| 4 Growth-first (75/75/75/75/60/40% stocks, ladder bought 2033) | 6.38% | $273.0k | $56.7k | $120.0k | $153.9k / $0.0k | 3.06% | 9.28% | $73.4k |
| 4 Growth-first, 75% stocks to 2033 | 7.74% | $296.5k | $62.8k | $60.0k | $117.3k / $0.0k | 2.36% | 9.77% | $101.3k |
| 4 Growth-first, with the same WInS-holdings premium on the 2033 ladder | 7.04% | $281.0k | $58.5k | $110.0k | $147.5k / $0.0k | 3.01% | 9.87% | $72.5k |
| 5 Corporate iBonds for 2033-36 (FRED spreads, credit losses) | 0.40% | $5.7k | $1.8k | $135.0k | $166.3k / $145.6k | 0.20% | 0.60% | $47.2k |
| 5 Corporate 2033-36, no credit losses | 0.02% | $0.6k | $0.3k | $135.0k | $166.4k / $146.6k | 0.07% | 0.09% | $49.5k |
| 5 Corporate 2033-36, iShares per-fund spreads, losses | 0.43% | $5.7k | $1.8k | $135.0k | $166.0k / $144.1k | 0.22% | 0.65% | $45.7k |
| 5 Corporate 2033-36, saving joins the floor | 0.99% | $5.7k | $1.9k | $145.0k | $177.5k / $145.4k | 0.48% | 1.46% | $34.8k |
| 5 Corporate 2033-37 (adds IBCB), losses | 0.63% | $7.2k | $2.2k | $135.0k | $166.7k / $148.0k | 0.23% | 0.85% | $49.7k |
| 6a Glide inside the sleeve (VT into a Dec-2032 Treasury, 1/4 a year 2029-32) | 0.02% | $0.6k | $0.3k | $135.0k | $164.3k / $135.9k | 0.08% | 0.10% | $37.6k |
| 6b Whole-portfolio glide (50% stocks to 0% by 2032, ladder bought 2033) | 0.50% | $106.0k | $22.0k | $165.0k | $175.0k / $55.8k | 3.98% | 4.48% | $30.4k |

### 2028 deposit only $75k

| Option | Short | Worst short | Mean short if short | Minimum (median) | Gift median / 1-in-20 | Gift below minimum | Any promise broken | Flexibility median |
|---|---|---|---|---|---|---|---|---|
| 1 Current plan (Root-and-Branch + 3r $10k reserve) | 0.02% | $0.6k | $0.3k | $60.0k | $78.8k / $52.9k | 0.43% | 0.45% | $27.5k |
| 1x Current plan without the reserve (V5 as written) | 15.6% | $11.7k | $1.3k | $70.0k | $82.2k / $49.5k | 7.75% | 20.5% | $19.5k |
| 1y Current plan, 2027 leftover joins the floor | 0.02% | $0.6k | $0.3k | $60.0k | $81.4k / $52.9k | 0.58% | 0.59% | $23.1k |
| 2 All-Treasury (sleeve in a Dec-2032 Treasury; same minimum) | 0.02% | $0.6k | $0.3k | $60.0k | $78.6k / $52.1k | 0.46% | 0.48% | $25.4k |
| 2b All-Treasury, locked half counted in the minimum | 0.02% | $0.6k | $0.3k | $65.0k | $78.6k / $52.1k | 1.11% | 1.13% | $25.4k |
| 3 VT = 15% of the 2028 deposit ($22.5k) | 0.02% | $0.6k | $0.3k | $45.0k | $73.3k / $45.3k | 0.00% | 0.02% | $35.9k |
| 3 VT = 25% of the 2028 deposit ($37.5k) | 0.02% | $0.6k | $0.3k | $30.0k | $62.6k / $35.5k | 0.00% | 0.02% | $48.5k |
| 3 VT = 40% of the 2028 deposit ($60k) | 0.02% | $0.6k | $0.3k | $0.0k | $46.8k / $26.7k | 0.00% | 0.02% | $64.2k |
| 3 VT = 15% of all money after Jan 2028 (~$69.5k) | 0.02% | $0.6k | $0.3k | $0.0k | $44.2k / $25.7k | 0.00% | 0.02% | $66.5k |
| 3 VT = 25% of all money (~$115.9k) | 0.02% | $0.6k | $0.3k | $0.0k | $44.2k / $25.7k | 0.00% | 0.02% | $66.5k |
| 3 VT = 40% of all money (not possible: capped at ~30%, $140k) | 0.02% | $0.6k | $0.3k | $0.0k | $44.2k / $25.7k | 0.00% | 0.02% | $66.5k |
| 4 Growth-first (75/75/75/75/60/40% stocks, ladder bought 2033) | 15.3% | $276.2k | $54.5k | $30.0k | $64.2k / $0.0k | 2.29% | 17.4% | $49.4k |
| 4 Growth-first, 75% stocks to 2033 | 16.9% | $300.1k | $60.6k | $0.0k | $47.1k / $0.0k | 1.70% | 18.2% | $65.9k |
| 4 Growth-first, with the same WInS-holdings premium on the 2033 ladder | 16.7% | $283.9k | $56.4k | $25.0k | $58.4k / $0.0k | 2.19% | 18.6% | $47.7k |
| 5 Corporate iBonds for 2033-36 (FRED spreads, credit losses) | 0.37% | $5.0k | $1.7k | $60.0k | $81.3k / $62.5k | 0.52% | 0.87% | $34.1k |
| 5 Corporate 2033-36, no credit losses | 0.02% | $0.6k | $0.3k | $60.0k | $81.4k / $63.8k | 0.28% | 0.29% | $36.4k |
| 5 Corporate 2033-36, iShares per-fund spreads, losses | 0.41% | $5.0k | $1.7k | $60.0k | $81.1k / $60.9k | 0.56% | 0.95% | $32.6k |
| 5 Corporate 2033-36, saving joins the floor | 0.88% | $5.0k | $1.6k | $70.0k | $91.6k / $62.2k | 1.16% | 2.00% | $23.3k |
| 5 Corporate 2033-37 (adds IBCB), losses | 0.60% | $5.9k | $2.1k | $60.0k | $81.6k / $65.6k | 0.55% | 1.12% | $36.6k |
| 6a Glide inside the sleeve (VT into a Dec-2032 Treasury, 1/4 a year 2029-32) | 0.02% | $0.6k | $0.3k | $60.0k | $78.9k / $52.5k | 0.43% | 0.45% | $26.0k |
| 6b Whole-portfolio glide (50% stocks to 0% by 2032, ladder bought 2033) | 4.63% | $143.8k | $23.9k | $75.0k | $84.1k / $0.0k | 3.97% | 8.56% | $20.4k |

### 2028 deposit missing

| Option | Short | Worst short | Mean short if short | Minimum (median) | Gift median / 1-in-20 | Gift below minimum | Any promise broken | Flexibility median |
|---|---|---|---|---|---|---|---|---|
| 1 Current plan (Root-and-Branch + 3r $10k reserve) | 51.5% | $89.0k | $16.7k | $0.0k | $0.0k / $0.0k | 0.00% | 51.5% | $3.3k |
| 2 All-Treasury (sleeve in a Dec-2032 Treasury; same minimum) | 51.5% | $89.0k | $16.7k | $0.0k | $0.0k / $0.0k | 0.00% | 51.5% | $3.3k |
| 4 Growth-first (75/75/75/75/60/40% stocks, ladder bought 2033) | 39.2% | $327.8k | $74.5k | $0.0k | $3.1k / $0.0k | 1.10% | 40.2% | $16.4k |
| 6b Whole-portfolio glide (50% stocks to 0% by 2032, ladder bought 2033) | 43.8% | $220.2k | $42.3k | $0.0k | $2.0k / $0.0k | 1.65% | 45.3% | $2.9k |

### History replay, add (1953-04-01..2010-09-01 (690))

| Option | Short | Worst short (start) | Gift median / 1-in-20 | Gift below minimum | Worst gift minus minimum (start) | Flexibility median |
|---|---|---|---|---|---|---|
| 1 Current plan (Root-and-Branch + 3r $10k reserve) | 0.00% | $0.0k (1953-04) | $168.7k / $153.7k | 0.43% | $-8.7k (1981-10) | $43.3k |
| 1x Current plan without the reserve (V5 as written) | 29.3% | $2.9k (2001-06) | $171.3k / $160.7k | 2.61% | $-39.7k (1981-10) | $33.4k |
| 1y Current plan, 2027 leftover joins the floor | 0.00% | $0.0k (1953-04) | $170.3k / $154.9k | 0.58% | $-10.9k (1981-10) | $41.7k |
| 2 All-Treasury (sleeve in a Dec-2032 Treasury; same minimum) | 0.00% | $0.0k (1953-04) | $166.7k / $151.8k | 1.16% | $-16.6k (1981-10) | $33.9k |
| 2b All-Treasury, locked half counted in the minimum | 0.00% | $0.0k (1953-04) | $166.7k / $151.8k | 2.32% | $-16.6k (1981-10) | $33.9k |
| 3 VT = 15% of the 2028 deposit ($22.5k) | 0.00% | $0.0k (1953-04) | $174.5k / $155.1k | 0.00% | $14.5k (1997-06) | $35.4k |
| 3 VT = 25% of the 2028 deposit ($37.5k) | 0.00% | $0.0k (1953-04) | $165.2k / $147.9k | 0.00% | $19.7k (1997-04) | $49.8k |
| 3 VT = 40% of the 2028 deposit ($60k) | 0.00% | $0.0k (1953-04) | $151.4k / $132.4k | 0.00% | $32.2k (1997-04) | $70.5k |
| 3 VT = 15% of all money after Jan 2028 (~$69.5k) | 0.00% | $0.0k (1953-04) | $145.9k / $125.3k | 0.00% | $34.8k (1997-04) | $79.2k |
| 3 VT = 25% of all money (~$115.9k) | 0.00% | $0.0k (1953-04) | $118.4k / $85.5k | 0.00% | $51.9k (1999-01) | $120.8k |
| 3 VT = 40% of all money (not possible: capped at ~30%, $140k) | 0.00% | $0.0k (1953-04) | $103.3k / $65.1k | 0.00% | $52.8k (1999-03) | $141.2k |
| 4 Growth-first (75/75/75/75/60/40% stocks, ladder bought 2033) | 0.00% | $0.0k (1953-04) | $212.0k / $17.2k | 3.48% | $-62.5k (1996-09) | $111.2k |
| 4 Growth-first, 75% stocks to 2033 | 0.00% | $0.0k (1953-04) | $182.4k / $17.2k | 4.06% | $-109.0k (2003-03) | $157.8k |
| 4 Growth-first, with the same WInS-holdings premium on the 2033 ladder | 0.00% | $0.0k (1953-04) | $204.9k / $13.9k | 3.48% | $-64.8k (1996-09) | $109.9k |
| 5 Corporate iBonds for 2033-36 (FRED spreads, credit losses) | 0.00% | $0.0k (1953-04) | $169.5k / $157.3k | 0.00% | $8.8k (1981-10) | $52.4k |
| 5 Corporate 2033-36, no credit losses | 0.00% | $0.0k (1953-04) | $169.5k / $159.2k | 0.00% | $10.4k (1982-01) | $55.3k |
| 5 Corporate 2033-36, iShares per-fund spreads, losses | 0.00% | $0.0k (1953-04) | $169.4k / $156.1k | 0.00% | $5.7k (1981-10) | $50.8k |
| 5 Corporate 2033-36, saving joins the floor | 0.72% | $3.5k (2002-05) | $180.8k / $165.2k | 1.01% | $-16.3k (1981-10) | $41.3k |
| 5 Corporate 2033-37 (adds IBCB), losses | 0.00% | $0.0k (1985-03) | $169.5k / $158.2k | 0.00% | $11.4k (1985-04) | $55.2k |
| 6a Glide inside the sleeve (VT into a Dec-2032 Treasury, 1/4 a year 2029-32) | 0.00% | $0.0k (1953-04) | $167.8k / $152.1k | 0.87% | $-12.1k (1981-10) | $38.5k |
| 6b Whole-portfolio glide (50% stocks to 0% by 2032, ladder bought 2033) | 0.00% | $0.0k (1953-04) | $189.6k / $97.1k | 4.06% | $-65.1k (1975-09) | $39.5k |

### History replay, prop (1953-04-01..2010-09-01 (690))

| Option | Short | Worst short (start) | Gift median / 1-in-20 | Gift below minimum | Worst gift minus minimum (start) | Flexibility median |
|---|---|---|---|---|---|---|
| 1 Current plan (Root-and-Branch + 3r $10k reserve) | 0.00% | $0.0k (1953-04) | $169.1k / $155.7k | 0.00% | $15.9k (1997-04) | $45.1k |
| 1x Current plan without the reserve (V5 as written) | 30.7% | $2.9k (2001-06) | $171.7k / $162.9k | 0.00% | $15.6k (1970-09) | $34.3k |
| 1y Current plan, 2027 leftover joins the floor | 0.00% | $0.0k (1953-04) | $170.7k / $156.8k | 0.00% | $17.7k (1997-04) | $43.3k |
| 2 All-Treasury (sleeve in a Dec-2032 Treasury; same minimum) | 0.00% | $0.0k (1953-04) | $166.7k / $154.9k | 0.00% | $16.6k (2007-12) | $33.8k |
| 2b All-Treasury, locked half counted in the minimum | 0.00% | $0.0k (1953-04) | $166.7k / $154.9k | 0.00% | $2.7k (2010-02) | $33.8k |
| 3 VT = 15% of the 2028 deposit ($22.5k) | 0.00% | $0.0k (1953-04) | $174.2k / $159.2k | 0.00% | $13.7k (1997-04) | $37.0k |
| 3 VT = 25% of the 2028 deposit ($37.5k) | 0.00% | $0.0k (1953-04) | $165.4k / $149.0k | 0.00% | $21.7k (1997-04) | $51.5k |
| 3 VT = 40% of the 2028 deposit ($60k) | 0.00% | $0.0k (1953-04) | $152.5k / $132.8k | 0.00% | $29.0k (1997-03) | $71.5k |
| 3 VT = 15% of all money after Jan 2028 (~$69.5k) | 0.00% | $0.0k (1953-04) | $147.1k / $125.4k | 0.00% | $36.1k (1999-04) | $80.8k |
| 3 VT = 25% of all money (~$115.9k) | 0.00% | $0.0k (1953-04) | $118.8k / $85.8k | 0.00% | $51.7k (1998-12) | $122.5k |
| 3 VT = 40% of all money (not possible: capped at ~30%, $140k) | 0.00% | $0.0k (1953-04) | $103.4k / $65.1k | 0.00% | $52.8k (1999-03) | $143.1k |
| 4 Growth-first (75/75/75/75/60/40% stocks, ladder bought 2033) | 0.00% | $0.0k (1953-04) | $217.8k / $17.5k | 3.48% | $-63.9k (1996-09) | $112.1k |
| 4 Growth-first, 75% stocks to 2033 | 0.00% | $0.0k (1953-04) | $187.2k / $17.5k | 4.20% | $-110.6k (2003-03) | $156.4k |
| 4 Growth-first, with the same WInS-holdings premium on the 2033 ladder | 0.00% | $0.0k (1953-04) | $212.5k / $14.3k | 3.48% | $-65.9k (1996-09) | $110.1k |
| 5 Corporate iBonds for 2033-36 (FRED spreads, credit losses) | 0.00% | $0.0k (1953-04) | $169.9k / $161.0k | 0.00% | $18.8k (2006-05) | $53.9k |
| 5 Corporate 2033-36, no credit losses | 0.00% | $0.0k (1953-04) | $169.9k / $161.5k | 0.00% | $23.8k (2007-06) | $57.4k |
| 5 Corporate 2033-36, iShares per-fund spreads, losses | 0.00% | $0.0k (1953-04) | $169.8k / $160.7k | 0.00% | $18.6k (2006-05) | $52.1k |
| 5 Corporate 2033-36, saving joins the floor | 0.87% | $3.6k (2002-05) | $181.3k / $167.0k | 0.00% | $18.2k (1997-04) | $42.8k |
| 5 Corporate 2033-37 (adds IBCB), losses | 0.00% | $0.0k (1953-04) | $169.9k / $161.1k | 0.00% | $19.7k (2007-01) | $56.5k |
| 6a Glide inside the sleeve (VT into a Dec-2032 Treasury, 1/4 a year 2029-32) | 0.00% | $0.0k (1953-04) | $168.2k / $155.0k | 0.00% | $16.1k (2000-01) | $38.8k |
| 6b Whole-portfolio glide (50% stocks to 0% by 2032, ladder bought 2033) | 0.00% | $0.0k (1953-04) | $199.1k / $97.1k | 2.61% | $-16.8k (1974-02) | $41.3k |

### Named paths: short / gift vs minimum / Laura's flexibility

| Option | 2008 | 2020 | 1980s_abs | 1973_74 | storm |
|---|---|---|---|---|---|
| 1 Current plan (Root-and-Branch + 3r $10k reserve) | $154.9k vs $135.0k; flex $20.3k | $166.3k vs $135.0k; flex $45.5k | $136.2k vs $135.0k; flex $0.5k | $163.3k vs $135.0k; flex $47.2k | $146.7k vs $135.0k; flex $3.1k |
| 1x Current plan without the reserve (V5 as written) | $163.6k vs $145.0k; flex $4.1k | $167.5k vs $145.0k; flex $30.7k | $114.0k vs $145.0k; flex $0.0k | $166.5k vs $145.0k; flex $39.0k | $144.3k vs $145.0k; flex $0.0k |
| 1y Current plan, 2027 leftover joins the floor | $156.7k vs $135.0k; flex $18.1k | $168.1k vs $135.0k; flex $43.4k | $134.2k vs $135.0k; flex $0.5k | $165.1k vs $135.0k; flex $45.3k | $146.6k vs $135.0k; flex $2.9k |
| 2 All-Treasury (sleeve in a Dec-2032 Treasury; same minimum) | $155.2k vs $135.0k; flex $20.6k | $160.9k vs $135.0k; flex $28.5k | $123.6k vs $135.0k; flex $0.5k | $169.8k vs $135.0k; flex $54.1k | $152.8k vs $135.0k; flex $9.1k |
| 2b All-Treasury, locked half counted in the minimum | $155.2k vs $150.0k; flex $20.6k | $160.9k vs $150.0k; flex $28.5k | $123.6k vs $140.0k; flex $0.5k | $169.8k vs $155.0k; flex $54.1k | $152.8k vs $145.0k; flex $9.1k |
| 3 VT = 15% of the 2028 deposit ($22.5k) | $156.8k vs $135.0k; flex $18.5k | $168.3k vs $140.0k; flex $40.1k | $151.2k vs $120.0k; flex $3.7k | $172.8k vs $150.0k; flex $42.1k | $146.9k vs $135.0k; flex $3.0k |
| 3 VT = 25% of the 2028 deposit ($37.5k) | $147.4k vs $120.0k; flex $27.5k | $159.4k vs $120.0k; flex $58.6k | $151.2k vs $105.0k; flex $20.6k | $160.0k vs $130.0k; flex $49.0k | $134.0k vs $115.0k; flex $7.9k |
| 3 VT = 40% of the 2028 deposit ($60k) | $133.5k vs $90.0k; flex $41.0k | $146.0k vs $90.0k; flex $80.7k | $144.6k vs $80.0k; flex $45.9k | $140.6k vs $100.0k; flex $59.5k | $114.6k vs $90.0k; flex $15.3k |
| 3 VT = 15% of all money after Jan 2028 (~$69.5k) | $127.5k vs $80.0k; flex $46.7k | $140.4k vs $80.0k; flex $90.1k | $141.7k vs $70.0k; flex $56.6k | $132.5k vs $85.0k; flex $63.9k | $106.4k vs $80.0k; flex $18.4k |
| 3 VT = 25% of all money (~$115.9k) | $97.2k vs $25.0k; flex $74.4k | $112.9k vs $25.0k; flex $135.6k | $128.0k vs $20.0k; flex $108.8k | $92.7k vs $25.0k; flex $85.4k | $66.5k vs $25.0k; flex $33.5k |
| 3 VT = 40% of all money (not possible: capped at ~30%, $140k) | $79.8k vs $0.0k; flex $88.8k | $98.6k vs $0.0k; flex $159.3k | $120.9k vs $0.0k; flex $135.9k | $71.9k vs $0.0k; flex $96.6k | $45.8k vs $0.0k; flex $41.4k |
| 4 Growth-first (75/75/75/75/60/40% stocks, ladder bought 2033) | $49.9k vs $10.0k; flex $61.9k | $229.4k vs $185.0k; flex $198.2k | $236.9k vs $180.0k; flex $215.7k | $107.4k vs $70.0k; flex $37.4k | $35.6k vs $50.0k; flex $0.0k |
| 4 Growth-first, 75% stocks to 2033 | $44.9k vs $0.0k; flex $84.0k | $199.4k vs $125.0k; flex $310.5k | $216.9k vs $140.0k; flex $311.0k | $75.5k vs $25.0k; flex $50.5k | short $72.3k; $0.0k vs $10.0k; flex $0.0k |
| 4 Growth-first, with the same WInS-holdings premium on the 2033 ladder | $44.3k vs $5.0k; flex $60.3k | $224.2k vs $180.0k; flex $197.5k | $230.5k vs $175.0k; flex $214.1k | $101.9k vs $65.0k; flex $36.9k | $28.3k vs $40.0k; flex $0.0k |
| 5 Corporate iBonds for 2033-36 (FRED spreads, credit losses) | $155.6k vs $135.0k; flex $24.4k | $166.3k vs $135.0k; flex $55.9k | $151.9k vs $135.0k; flex $0.5k | $163.3k vs $135.0k; flex $52.1k | $146.7k vs $135.0k; flex $7.1k |
| 5 Corporate 2033-36, no credit losses | $162.7k vs $135.0k; flex $22.9k | $166.3k vs $135.0k; flex $57.3k | $152.4k vs $135.0k; flex $1.3k | $163.3k vs $135.0k; flex $59.7k | $146.7k vs $135.0k; flex $14.6k |
| 5 Corporate 2033-36, iShares per-fund spreads, losses | $154.9k vs $135.0k; flex $23.3k | $166.3k vs $135.0k; flex $54.1k | $150.0k vs $135.0k; flex $0.5k | $163.3k vs $135.0k; flex $50.2k | $146.7k vs $135.0k; flex $5.4k |
| 5 Corporate 2033-36, saving joins the floor | $167.5k vs $145.0k; flex $11.0k | $179.0k vs $145.0k; flex $42.8k | $138.9k vs $145.0k; flex $0.5k | $171.4k vs $145.0k; flex $43.3k | $148.8k vs $145.0k; flex $2.9k |
| 5 Corporate 2033-37 (adds IBCB), losses | $157.2k vs $135.0k; flex $24.1k | $166.3k vs $135.0k; flex $59.1k | $152.4k vs $135.0k; flex $2.4k | $163.3k vs $135.0k; flex $53.9k | $146.7k vs $135.0k; flex $8.6k |
| 6a Glide inside the sleeve (VT into a Dec-2032 Treasury, 1/4 a year 2029-32) | $151.8k vs $135.0k; flex $17.1k | $164.5k vs $135.0k; flex $32.0k | $132.5k vs $135.0k; flex $0.5k | $164.4k vs $135.0k; flex $48.3k | $153.4k vs $135.0k; flex $9.7k |
| 6b Whole-portfolio glide (50% stocks to 0% by 2032, ladder bought 2033) | $87.5k vs $75.0k; flex $31.9k | $194.8k vs $185.0k; flex $24.3k | $174.7k vs $155.0k; flex $35.2k | $147.9k vs $140.0k; flex $24.0k | $115.1k vs $100.0k; flex $24.9k |

Generated-table notes: "Gift reaches top" = the gift equals the announced top. Growth-first and whole-glide have no 2042 money by construction. "Any promise broken" = a payment short or the gift below the announced minimum.
