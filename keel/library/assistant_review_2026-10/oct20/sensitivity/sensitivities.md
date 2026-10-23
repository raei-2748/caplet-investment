# Sensitivities for the Final Report: what moves Laura's payments, minimum, range and gift (20 Oct 2026)

> **Verified 20 Oct (`oct20/verify_ldi_sens/verify_ldi_sens.md`): arithmetic confirmed; framing fixes.** The room $1,554 is the coupon-study basis (each rung at its own yield); basis D gives $2,838 - name the basis; both omit the 0.07% fee (~$0.93k today). The 15.6% level is model-dependent (16.2% with the iBond coupon fix). The tornado mixes MC medians, single paths and a real-dollar line and ranks a case-fixed deposit cut against market moves: show the deposit as a robustness test, inflation as a separate real-value line, and rank market drivers at comparable 1-in-20 settings. Chain-order artefact: in falling-yield paths the gift is cut below the top while $6-7k above the cap stays with Laura; using the above-cap money first keeps the gift at the top. Date-qualify "3r rises when yields fall" (large in 2031-33, small by 2038). **Consistency fix 20 Oct (`oct20/consistency/consistency_audit.md` rows 8-9):** 0.02% is a study-engine figure: never quote it (REG D5); marked at market it is 0.08% / 0.32% / 0.72%. The payment-short odds in the headline and tables are study-engine (agreed basis option 1 14.5%, 3r 0.6%, REC §5). The room and top-reach wording in the Q&A list follows REG C1/C3.


**Status.** AI-generated research by Claude Code for Team Caplet, Tue 20 Oct 2026 (Sydney). Every number is MODEL output from scripts an AI wrote; no student has rebuilt it yet. Nothing here is text to submit: it drafts no IPS sentence, Final Report paragraph or co-sponsor wording. If the team uses any number, table or chart idea, log it in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). UNVERIFIED marks anything nobody could confirm. The Final Report instructions come out on 9 Nov ET; anything said here about what that report "should show" is a FORECAST from the case text only.

**Short forms.** `SEN/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/sensitivity/`. `oct19/`, `oct20/` = the sibling scratchpad folders. `case:n` = line n of `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`. "Gift" = Laura's 2033 facility contribution. "Minimum" and "top" = the bottom and top of the 2031 range. "Option 1" = state the coupon risk only, no reserve. "3r" = the AI-recommended $10k reinvestment reserve in the 3.125% Treasury maturing 15 Nov 2041, bought from the 2028 deposit (`oct19/coupon/coupon_risk_options.md:126-134`). The team has not voted on 3r; the vote is set for Tue 27 Oct (`oct19/out/Caplet_Update_19Oct2026.md:297-321`).

**Why this exists.** The case asks teams to "explain how favorable and unfavorable market outcomes could affect the amount she can provide" (case:117-119). It also asks them to "identify and explain their assumptions about investment performance, the timing of cash flows, outside funding, the effect of inflation on portfolio projections and facility costs ... [and] consider how favorable and unfavorable investment outcomes would affect their recommendations" (case:146-149).

---

## 0. The short version

1. **The ten payments hardly depend on the 2028 deposit. The gift depends on almost nothing else.** Cutting the deposit from $150k to $75k leaves the chance of a short payment unchanged (15.6% with option 1, 0.02% with 3r; study engine; agreed basis 14.5% / 0.6%, REC §5) [consistency fix 20 Oct, row 8] but halves the median gift ($166k to $82k). The deposit's only job for the payments is to top up the January 2027 ladder if it costs more than $300k. On today's curve that happens in 45% of model paths, and the 95th-percentile top-up is $21.6k.
2. **If the 2028 deposit never arrived, payments would be short in about 55% of model paths** (44% of the 690 history windows): typically $14k, worst $81k in the model and $35k in history. The 3r reserve can't help, because it is bought from that deposit. This is the only tested scenario where 3r doesn't protect the payments.
3. **A smaller or later deposit shrinks the range but doesn't break it,** because the range is announced in 2031, after the deposit is known. A $100k deposit gives a $95k minimum; a deposit in Jan 2029 keeps the $145k minimum but costs about $4k of median gift. What it does hurt is any **dollar** minimum quoted before 2028, such as one in the IPS.
4. **Yields at the January 2027 purchase are the biggest market driver of the gift, and they cut one way.** A 1-point fall before purchase costs about $37k of median gift and $30k of minimum. A 1-point rise adds only about $3k to the gift, because the gain goes to the 2027 leftover, which is Laura's money. Laura's total (gift plus what she keeps) moves about the same amount either way: +$46k / −$47k.
5. **A 2008-style crash never breaks the minimum, because the minimum is Treasuries.** Timing decides *where in the range* the gift lands. If the trough falls on the Jan 2031 announcement, the range itself is lower (gift $159k). If it falls just before the Jan 2033 gift, the gift lands $9.5-11k under the announced top. A 2008-style fall in yields as well, timed for 2029-31, leaves one payment $2.4k short under option 1 and nothing short under 3r.
6. **Inflation can't cause a missed payment, but it erodes real value.** The payments are fixed in dollars by case rule (case:90). At 3.5% instead of 2.0% inflation, the median gift is worth $12k less in Jan-2027 dollars ($135k vs $148k). A range quoted in 2031 loses 3.9-6.7% of its buying power by 2033.
7. **Turning 3r on costs $10k of minimum and about $3k of median gift in every scenario.** It cuts payment risk from about 16-22% (small gaps of about $1-3k) to 0.01-0.09%. It matters most when the deposit is smaller, later, or yields fall before purchase.

---

## 1. Basis (MODEL, 20 Oct 2026)

**Curve.** treasury.gov daily par yield curve, **Mon 19 Oct 2026** row, the latest published. It was fetched 19 Oct 22:01 UTC (Tue 20 Oct 09:01 Sydney) from https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv. Values: 1m 4.11, 3m 4.27, 6m 4.37, 1y 4.50, 2y 4.77, 3y 4.85, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48 (copy: `SEN/data/tsy_202610.csv:2`). Yields rose 3-6bp from 16 Oct.

**Model.** This is a copy of the 19 Oct coupon study's `coupon_options.py`, imported unmodified (`SEN/scripts/coupon_options.py`, md5 matches `oct19/coupon/scripts/coupon_options.py`). It is wrapped by `SEN/scripts/sens_engine.py`, which adds only these inputs:
- the 2028 deposit's size and date;
- carrying a January 2027 ladder gap forward at the short rung's yield until the deposit arrives ($1 short in Jan 2027 costs about $1.05 a year later);
- a gap the deposit can't fill, which leaves the 2033 payment short;
- a 3r reserve capped at what is left of the deposit.

Everything else is the study's: holdings' maturity dates, each rung sized for $50k with income reinvested at its own yield, waiting cash at 0%, rates as a parallel random walk at 1.0 point a year (floor 0.25%), and VT at 7.0% compound, 16.78% volatility and a 0.06% fee (JPM 2026 LTCMA AC World). Stock-yield correlation is 0. There are 100,000 paths (seed 20261019) and 690 history windows (Apr 1953 to Sep 2010 starts). The plan rules are IPS Version 5's:
- the 2028 deposit first tops up the ladder;
- the remainder R (minus the 3r reserve) buys IBTM to repay R in Dec 2032, and the rest buys VT;
- 2031 minimum = (R − $3,700) rounded down to $5k; top = R + half of VT in Jan 2031, less any projected uncovered shortfall (plus the reserve under 3r);
- 2033 gift = floor + half of VT, capped at the top.

**Checks done (twice).**
- With gap carry-forward switched off, the wrapper equals the original `run()` path by path (maximum difference $0.00), and it reproduces the 16 Oct study's headline row: 16.4% / $3.0k / $6.1k; $145k; $166.1k; $165.3k / $135.8k; 2.1%; 3r 0.02% / $135k / $162.2k / 0.05% (`SEN/scripts/validate.py`).
- On 19 Oct, the ladder cost of $298,446 and the 15.6% / 0.02% shortfall odds (study engine; agreed basis 14.5% / 0.6%, REC §5) [consistency fix 20 Oct, row 8] match the sibling reserve study (`oct20/reserve/reserve_schedule.md:17`; the 15.6% / 0.02% refresh is in the same file).
- Gap carry-forward changes the base median gift by $44 ($166,177 without, $166,133 with).
- A second seed (7) gives the same cells to within 0.1 point and $0.4k (`SEN/data/seedcheck_out.txt`).
- Hand checks: floor cost = 150,000 / (1 + 0.051081/2)^(2 × 4.953) = $116.8k, leaving $33.2k for VT. VT × e^(3 × 0.0671) = $40.5k in Jan 2031, so the top is $150k + $20.3k = $170.3k. Inflation totals match `oct20/inflation/inflation.md:19` ($406,790 / $386,777 / $350,118).

**Base results on 19 Oct (MODEL; payment odds: study engine; agreed basis 14.5% / 0.6%, REC §5) [consistency fix 20 Oct, row 8].**

| | Option 1 | 3r |
|---|---|---|
| Ladder cost on 1 Jan 2027 (yields unchanged) | $298,446; room $1,554 (5.4bp) | same |
| Chance the ladder costs more than $300k on 1 Jan | 45.3% | same |
| Some payment short (model / history) | 15.6% / 29.3%; median $1.1k when short; 1-in-100 $3.0k; worst $6.2k | 0.02% / 0.0%; worst $0.6k |
| 2031 minimum (median) / top (median) | $145k / $167.0k | $135k / $165.8k |
| 2033 gift: median / 1-in-20 low / 1-in-20 high | $166.1k / $137.7k / $182.6k | $163.3k / $135.5k / $180.0k |
| Gift below the minimum (model / history) | 1.97% / 2.61% | 0.06% / 0.43% |
| Gift reaches the top | 68% | 42% |
| Laura's free money in 2033 (median, study measure) | $20.4k | $20.4k (+ about $19.9k back in 2042) |
| Single path, yields flat and stocks at 7% ("DET base") | minimum $145k, top = gift $170.3k, Laura keeps $23.2k + $2.9k above the cap | $135k, $168.9k, $21.6k |

---

## 2. One table: favourable, base, unfavourable (MODEL, 19 Oct curve)

Each cell shows **option 1 | 3r**. "MC" = median of 100,000 paths. "DET" = one path with everything else at base (yields flat at 19 Oct, stocks 7%/yr). Payment figures for MC rows are the chance some payment is short (study engine; agreed basis 14.5% / 0.6%, REC §5) [consistency fix 20 Oct, row 8]; for DET rows, the dollar shortfall after cover.

| Driver (basis) | Setting: favourable / base / unfavourable | Payments short | 2031 minimum | 2033 gift (median) | Laura's free money 2033 |
|---|---|---|---|---|---|
| **2028 deposit size** (MC) | — / $150k (case) / $75k. Extreme: $0 | base 15.6% \| 0.02%; $75k 15.6% \| 0.02%; **$0: 55.3% \| 55.3%** | $145k \| $135k → $70k \| $60k; $0: none | $166.1k \| $163.3k → $82.2k \| $78.7k; $0: $0 | $20.4k \| $20.4k → $9.6k \| $9.1k |
| **2028 deposit timing** (MC) | — / 2 Jan 2028 (case) / 2 Jan 2029 (mid-2028 in §4.1) | 15.6% \| 0.02% → 15.6% \| 0.09% | unchanged: $145k \| $135k | → $161.9k \| $158.8k | → $15.7k \| $15.5k |
| **Yields at the Jan 2027 purchase** (MC; base = buy at today's curve) | +1.0 pt / 0 / −1.0 pt | 0.00% \| 0.00% / 20.6% \| 0.01% / 21.7% \| 0.08% | $145k \| $135k / $145k \| $135k / **$115k \| $105k** | $172.5k \| $170.6k / $169.2k \| $166.0k / **$132.5k \| $128.6k** | $26.8k \| $25.0k / $20.3k \| $21.1k / $12.4k \| $13.5k |
| **Yields after purchase, for good** (DET; coupon risk) | +2 pts / flat / −2 pts | none / none / coupon gap $19.0k, all covered (option 1 uses all of Laura's half) | unchanged | $176.8k \| $175.0k / $170.3k \| $168.9k / $156.9k \| $153.9k | $30.7k \| $28.6k / $23.2k \| $21.6k / **$0 \| $8.8k** |
| **Stocks 2028-33** (DET; 1-in-20 good/bad five years) | +21.0%/yr / +7.0% / −5.5%/yr | none | unchanged | $179.4k \| $177.4k / $170.3k \| $168.9k / $162.5k \| $159.7k | $43.0k \| $40.1k / $23.2k \| $21.6k / $12.5k \| $11.7k |
| **2008-style crash** (DET; worst timing for the gift = trough at the Jan 2031 announcement) | no crash / no crash / crash Aug 2029-Mar 2031 | none with flat yields; with 2008 yields too: **$2.4k \| $0** | unchanged | $170.3k \| $168.9k → $159.4k \| $158.8k (see §4.3 for the other timings) | → $16.9k \| $15.7k (+$7.5k above the cap under option 1) |
| **Inflation, real value** (MC medians in Jan-2027 dollars) | 2.0% / 2.5% (JPM 2026) / 3.5% | none: payments are nominal (case:90) | $128.8k \| $119.9k / $125.0k \| $116.4k / $118.0k \| $109.8k | $147.5k \| $145.0k / $143.3k \| $140.8k / $135.1k \| $132.9k | $18.1k \| $18.2k / $17.6k \| $17.6k / $16.6k \| $16.6k |

The case fixes both the deposit's timing ("All contributions and withdrawals occur at the beginning of the applicable year", case:59) and its size (case:43-45). The deposit rows are robustness tests of a career-income risk the team's own client analysis raises (the deposit comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures", case:44-45). They are not a claim that the case is wrong.

---

## 3. Tornado: what matters most (MODEL)

Bar = how far the **median 2033 gift** moves between the unfavourable and favourable setting. Left of `|` = loss from base; right = gain. Each `#` is about $2k. Option 1 is shown; 3r ranks the same, with swings within $2k (`SEN/data/tornado_out.txt`).

```
Driver                                    loss from base                 | gain     swing   unfav .. base .. fav
2028 deposit $150k -> $75k                ##########################################|          83.9k   82.2 .. 166.1 .. 166.1 (MC)
Yields at Jan-2027 purchase +/-1.0 pt                       ##################|##        40.0k  132.5 .. 169.2 .. 172.5 (MC)
Yields after purchase +/-2 pts (coupon)                            #######|###       19.9k  156.9 .. 170.3 .. 176.8 (DET)
Stocks 2028-33, 1-in-20 bad/good                                      ####|#####     16.9k  162.5 .. 170.3 .. 179.4 (DET)
Inflation 3.5% vs 2.0% (real $)                                       ####|##        12.4k  135.1 .. 143.3 .. 147.5 (MC, real)
2008-style crash, worst timing                                       #####|          10.9k  159.4 .. 170.3 .. 170.3 (DET)
2028 deposit 1 year late                                                ##|           4.2k  161.9 .. 166.1 .. 166.1 (MC)
```

**Ranking for the payments** (what can make a payment short; study engine; agreed basis 14.5% / 0.6%, REC §5) [consistency fix 20 Oct, row 8] is different:

| Rank | Driver | Option 1 | 3r |
|---|---|---|---|
| 1 | 2028 deposit missing ($0) | 55.3% short (typical $14k) | 55.3% (3r can't be bought) |
| 2 | Yields fall before the Jan 2027 purchase (−0.5 to −1.0 pt) | 22-23% (small gaps) | 0.04-0.08% |
| 3 | Coupon risk with no reserve (base) | 15.6% (median $1.1k, worst $6.2k) | 0.02% |
| 4 | 2008-style joint crash (stocks and yields, 2029-31) | $2.4k short | $0 |
| 5 | Deposit one year late | 15.6% (unchanged) | 0.09% (reserve bought later) |
| — | Equity alone, inflation | none | none |

**How to read it.** The gift is a deposit-and-yields story; the stock market is third or fourth. Payments are a "did the 2028 deposit come, and is there a reserve" story.

---

## 4. Detail

### 4.1 The 2028 deposit arrives late or smaller (MC, 100,000 paths; history = 690 windows; study engine; agreed basis 14.5% / 0.6%, REC §5) [consistency fix 20 Oct, row 8]

| Scenario | Payments short: option 1 (model / history) | 3r (model / history) | Minimum 1 \| 3r | Top (median) 1 \| 3r | Gift median 1 \| 3r | Gift 1-in-20 low 1 \| 3r | Gift below minimum 1 \| 3r | Free money 2033, 1 \| 3r |
|---|---|---|---|---|---|---|---|---|
| On time, $150k (case) | 15.6% / 29.3% | 0.02% / 0.00% | $145k \| $135k | $167.0k \| $165.8k | $166.1k \| $163.3k | $137.7k \| $135.5k | 1.97% \| 0.06% | $20.4k \| $20.4k |
| Mid-2028 (1 Jul), $150k | 15.6% / 29.3% | 0.04% / 0.29% | $145k \| $135k | $164.8k \| $163.7k | $164.0k \| $161.0k | $133.2k \| $132.6k | 3.52% \| 0.24% | $18.1k \| $18.0k |
| 2 Jan 2029, $150k | 15.6% / 29.3% | 0.09% / 0.87% | $145k \| $135k | $162.5k \| $161.7k | $161.9k \| $158.8k | $128.2k \| $129.7k | 5.34% \| 0.61% | $15.7k \| $15.5k |
| On time, $100k | 15.6% / 29.3% | 0.02% / 0.00% | $95k \| $85k | $110.7k \| $109.7k | $110.2k \| $107.0k | $79.0k \| $79.8k | 4.93% \| 0.21% | $13.1k \| $12.9k |
| On time, $75k | 15.6% / 29.3% | 0.02% / 0.00% | $70k \| $60k | $82.7k \| $81.8k | $82.2k \| $78.7k | $48.5k \| $51.7k | 7.82% \| 0.44% | $9.6k \| $9.1k |
| On time, $0 | **55.3% / 44.4%** (median $13.9k when short; worst $80.9k / $35.0k) | same (no reserve possible) | none | none | $0 | $0 | — | $0 |
| 2 Jan 2029, $75k (both) | 15.7% / 29.3% | 0.09% / 0.87% | $70k \| $60k | $80.6k \| $80.0k | $80.2k \| $76.2k | $41.3k \| $47.9k | 11.8% \| 1.50% | $7.4k \| $6.9k |

**The top-up in one path** (DET, yields 0.5 point lower at purchase; ladder $313.3k):
- The gap is $13.9k if the deposit is on time, $14.2k in mid-2028 and $14.5k in Jan 2029. A late deposit costs more because the hole grows at the short rung's yield.
- With a $0 deposit, the 2033 payment is **$17.2k short** (the $13.3k hole grown to Dec 2032).

**What it shows.**
- **Payments:** a late or smaller deposit changes nothing as long as the deposit covers the top-up (95th percentile $21.6k). The single $19.3k worst path in the $75k row is a 1-in-100,000 path where yields fell by about 2 points before January 2027.
- **Floor and range:** these scale with the deposit, because the floor is "what is left after the top-up". The range is set in 2031, after the deposit, so nothing promised is broken.
- **Gift:** the gift is about floor + half of VT. A late deposit has two effects: the floor bond earns for fewer years, so less money is left over for VT, and VT has less time to grow. VT starts at $33.2k on time, $30.3k in mid-2028 and $27.2k in Jan 2029 (DET).
- **The gift falls below the minimum more often** with a smaller or later deposit (option 1: 2.0% → 7.8% at $75k, 11.8% at $75k a year late). The coupon risk is the same size, but Laura's half, the first cushion, is smaller. 3r keeps it at or below 1.5%. **So 3r matters most when the deposit disappoints.**
- Late deposit plus 3r: the reserve is bought later, so coupon losses in 2027-28 are not hedged. That is why payment risk rises from 0.02% to 0.09% (history 0.87%) on the study engine (never quote 0.02% alone; REG D5) [consistency fix 20 Oct, row 8].

### 4.2 Yields at the January 2027 purchase, ±0.5 and ±1.0 point from the 19 Oct curve

MC rows fix the 1 Jan 2027 shift and let rates wander after it. DET rows hold the shifted level for good.

| Shift on 1 Jan 2027 | Ladder cost (DET) | Top-up from 2028 / 2027 leftover | Minimum 1 \| 3r | Top (median) 1 \| 3r | Gift median 1 \| 3r | Gift 1-in-20 low 1 \| 3r | Payments short 1 \| 3r | Gift below minimum 1 \| 3r | Free money 2033 1 \| 3r | Gift + free + 2042 money (median), option 1 |
|---|---|---|---|---|---|---|---|---|---|---|
| −1.0 | $328.9k | $30.1k / $0 | $115k \| $105k | $133.1k \| $132.1k | $132.5k \| $128.6k | $108.9k \| $114.8k | 21.7% \| 0.08% | 5.93% \| 0.19% | $12.4k \| $13.5k | $150.0k |
| −0.5 | $313.3k | $13.9k / $0 | $130k \| $120k | $152.7k \| $151.5k | $152.0k \| $148.3k | $132.9k \| $134.5k | 22.7% \| 0.04% | 4.14% \| 0.17% | $16.0k \| $17.2k | $173.6k |
| 0 | $298.4k | $0 / $1.6k | $145k \| $135k | $170.0k \| $168.7k | $169.2k \| $166.0k | $156.7k \| $152.1k | 20.6% \| 0.01% | 2.00% \| 0.05% | $20.3k \| $21.1k | $196.9k |
| +0.5 | $284.4k | $0 / $15.6k | $145k \| $135k | $171.8k \| $170.3k | $170.9k \| $169.0k | $161.5k \| $158.6k | 2.5% \| 0.00% | 0.03% \| 0.00% | $24.7k \| $23.2k | $219.9k |
| +1.0 | $271.1k | $0 / $28.9k | $145k \| $135k | $173.4k \| $171.9k | $172.5k \| $170.6k | $162.6k \| $160.6k | 0.00% \| 0.00% | 0.00% \| 0.00% | $26.8k \| $25.0k | $243.1k |

**What it shows.**
- **Asymmetry.** Falls come out of the floor, since the top-up is taken from the 2028 deposit. The minimum drops $15k per half point. Rises stop at the $150k floor: the extra goes into the 2027 leftover, which the plan holds as first cover and returns to Laura. Laura's total moves about the same either way: +$46k / −$47k for ±1 point.
- **Payments.** With option 1, payment risk is about 21-23% whenever there is no 2027 leftover (shift 0 or below), and near zero when yields rise and a leftover exists. 3r keeps it at or below 0.08% throughout.
- **Room.** The room under $300k is $1,554, used up by a 5.4bp fall. The ladder moves about $290 per 0.01 point.

### 4.3 A 2008-style crash: timing 2028-30 vs 2031-32 (DET)

**Crash path.** Shiller monthly total-return index from Oct 2007, run for 60 months: trough 0.509 after 17 months (Mar 2009), back to 1.04 by Oct 2012. After that, 7%/yr.
- Source: Shiller data via `snap/main/rab/data/history/shiller_monthly.csv`, copied as `SEN/data/shiller_monthly.csv`.
- Monthly averages smooth the crash. The daily peak-to-trough fall was deeper (size UNVERIFIED here).

**"2008 yields."** The same months' change in the 10-year yield from that file's GS10 column (−3.0 points at worst, −2.78 at the end), added to the curve from the crash start and then held.

| Timing (plan dates) | VT vs purchase: Jan 2031 / Jan 2033 | Range 1 \| 3r | Gift 1 \| 3r | Gift vs announced top 1 \| 3r | With 2008 yields too: payment short 1 \| 3r; gift 1 \| 3r | Free money 2033 (flat yields) 1 \| 3r |
|---|---|---|---|---|---|---|
| No crash | ×1.22 / ×1.40 | $145-170.3k \| $135-168.9k | $170.3k \| $168.9k | at top \| at top | — | $23.2k \| $21.6k |
| T1: crash starts Jan 2028, right after VT is bought (trough Jun 2029) | ×0.82 / ×1.04 | $145-163.5k \| $135-162.6k | $163.5k \| $162.6k | at top \| at top | $0 \| $0 (coupon gap $12.7k: option 1 takes it from Laura's half, which falls to $6.6k; 3r gift $155.7k) | $17.2k \| $16.1k |
| T2: crash Aug 2029, trough at the Jan 2031 announcement | ×0.57 / ×1.02 | $145-159.4k \| $135-158.8k | **$159.4k \| $158.8k** | at top \| at top (option 1: $7.5k above the cap stays Laura's) | **$2.4k \| $0** ($159.4k \| $158.8k) | $16.9k \| $15.7k |
| T4: crash starts Jan 2031, just after the announcement (trough Jun 2032) | ×1.22 / ×0.89 | $145-170.3k \| $135-168.9k | $164.8k \| $161.8k | −$5.5k \| −$7.1k | $1.4k \| $0 ($164.7k \| $161.7k) | $14.8k \| $13.8k |
| T3: crash Aug 2031, trough at the Jan 2033 gift | ×1.22 / ×0.65 | $145-170.3k \| $135-168.9k | $160.7k \| $158.0k | **−$9.5k \| −$10.9k** | $0 \| $0 ($160.7k \| $158.2k) | $10.7k \| $10.0k |

**What it shows.**
- **The minimum survives every timing,** because it is a Treasury floor and only half of VT is promised above it.
- **A 2028-30 crash (T1, T2)** mostly lowers the *range itself*: the top is set when VT is down. The gift then reaches that lower top, and any recovery goes to Laura (T2: $7.5k above the cap).
- **A 2031-32 crash (T4, T3)** keeps the high announced top but delivers a gift $5-11k under it. That is still inside the range, but it is the "promised more than she gave" pattern the case warns about (case:114-115). It is the reason for showing the top with its probability beside it: the gift reaches the top in 68% of paths under option 1 and 42% under 3r.
- **With 2008-style yield falls as well,** option 1 leaves a payment short in T2 ($2.4k) and T4 ($1.4k). The 2033 projection freezes yields while they are still falling, so Laura's half is released too early. 3r covers both. This is the clearest single-path case for a standing reserve over a one-off 2033 set-aside.

### 4.4 Inflation at 2.0% and 3.5% (real value in Jan-2027 dollars; base 2.5% = JPM 2026 LTCMA)

| Item (Jan-2027 dollars) | 2.0% | 2.5% | 3.5% |
|---|---|---|---|
| Ten payments ($500k nominal) | $406.8k | $386.8k | $350.1k |
| 2033 payment / 2042 payment | $44.4k / $37.2k | $43.1k / $34.5k | $40.7k / $29.8k |
| 2042 payment's buying power vs 2033's | 84% | 80% | 73% |
| 2031 minimum, option 1 \| 3r (real at Jan 2033) | $128.8k \| $119.9k | $125.0k \| $116.4k | $118.0k \| $109.8k |
| Median gift, option 1 \| 3r (MC) | $147.5k \| $145.0k | $143.3k \| $140.8k | $135.1k \| $132.9k |
| Gift 1-in-20 low, option 1 \| 3r | $122.2k \| $120.3k | $118.7k \| $116.8k | $112.0k \| $110.2k |
| Buying power a 2031 range loses by the 2033 gift | 3.9% | 4.8% | 6.7% |

**What it shows.**
- Inflation can't make a payment short: the payments are nominal (case:90), and so is the ladder.
- Inflation sets what the money buys: about $12k of median gift between 2.0% and 3.5%.
- These are US-CPI deflators. For buying power in Taiwan, the sibling study finds a fixed US$ amount has lost value at roughly Taiwan's lower CPI rate (1.25%/yr since 2000), while Taiwan building costs ran 2.5-3.6%/yr over long windows and +7.29% y/y in Sep 2026 (`oct20/inflation/inflation.md:20-27`). **State one deflator and one base date.**
- Higher inflation usually comes with higher yields, which help the January purchase (§4.2). That link is an interpretation and is not modelled here.

### 4.5 The 3r reserve on and off, across every scenario (study engine; agreed basis 14.5% / 0.6%, REC §5) [consistency fix 20 Oct, row 8]

| Scenario | Payments short: 1 → 3r | Gift below minimum: 1 → 3r | Cost of 3r: minimum / median gift |
|---|---|---|---|
| Base | 15.6% → 0.02% (history 29.3% → 0%) | 1.97% → 0.06% | −$10k / −$2.8k |
| Deposit $75k | 15.6% → 0.02% | 7.82% → 0.44% | −$10k / −$3.5k |
| Deposit Jan 2029 | 15.6% → 0.09% (history 29.3% → 0.87%) | 5.34% → 0.61% | −$10k / −$3.1k |
| Deposit $0 | 55.3% → 55.3% (can't be bought) | — | — |
| Yields −1.0 at purchase | 21.7% → 0.08% | 5.93% → 0.19% | −$10k / −$3.9k |
| Yields −2 pts after purchase (DET) | covered either way; Laura's free money $0 → $8.8k | — | gift −$3.0k |
| 2008 crash with 2008 yields, T2 (DET) | $2.4k short → $0 | — | gift −$0.6k |
| Inflation 3.5% (real) | — | — | minimum −$8.2k real |

The net-minimum rule from the coupon study (cut the 2031 minimum by any shortfall the named reserves can't cover) is not applied in these tables. With it, option 1's "gift below minimum" figures would fall (`oct19/coupon/coupon_risk_options.md:101-104`).

---

## 5. What students must be able to explain (without notes)

1. **Why the payments barely depend on the 2028 deposit,** and the one case where they do: the deposit only tops up the January 2027 ladder. Know today's room ($2,838 / 9.8bp on basis D, or $1,554 on the coupon-study basis; about two in five odds of a top-up, 19 Oct, fee-free) [consistency fix 20 Oct, row 9] and what a missing deposit would do (payments short in about half of model paths).
2. **Why a late or smaller deposit shrinks the range instead of breaking it:** the range is announced in 2031, after the deposit is known, and the floor is "what is left". Be ready for "you quoted $145k in November 2026: is that a promise?"
3. **The asymmetry in §4.2:** a yield fall before purchase costs the floor and gift; a rise goes to Laura's leftover. Who gains and who loses is a design choice the team made, and the team should be able to defend it in its own words.
4. **The difference between the two rate risks:** yields *at* purchase (changes what the ladder costs) and yields *after* purchase (changes what coupons earn when reinvested; the 3r bond rises when yields fall).
5. **Crash timing:** why no crash breaks the minimum, why a crash after the announcement is the credibility risk, and what the top's probability means (about two in three / about two in five on the study engine; say round figures and name the convention) [consistency fix 20 Oct, row 9].
6. **Inflation:** why it cannot cause a missed payment under case:90, and which deflator and base date the team uses. Be ready for "is $150k in 2033 the same as $150k today?"
7. **The 3r trade, in Laura's terms:** $10k off the minimum and about $3k off the typical gift, for payment risk near zero. Know when it helps most (smaller or late deposit, falling yields) and when it can't help (no deposit).
8. **What "MODEL" means here:** one curve date (19 Oct), a random-walk rate model with no pull back to normal, 7% stocks, monthly-average history, holdings basis with 0% on waiting cash. These are scenarios, not forecasts. Each student should rebuild at least the table in §2 on the 6 Nov close before quoting it (`oct19/out/Caplet_Update_19Oct2026.md:100`).
9. **That the case fixes the cash-flow timing (case:59)** and the amounts (case:43-45). The late or small deposit rows are robustness tests the team chose, not alternative case facts.

---

## 6. What a Final Report sensitivity section would need (FORECAST, blueprint only, no wording)

- One table of favourable / base / unfavourable outcomes (§2 is the content), labelled MODEL with the curve date and the basis in one line.
- One tornado chart ranking the drivers by their effect on the gift, with a separate note for the payments ranking (§3).
- For each unfavourable row: what absorbs it (top-up, Laura's half, reserve, gift above the minimum) and what is never touched (the minimum Treasuries; no outside money, case:91-92).
- The cash-flow-timing assumption stated once, with the case line (case:59), and the late-deposit test as a robustness check.
- One inflation line with the deflator and base date.
- Every number re-run on the 6 Nov close by a student, then checked by a second student.

---

## 7. Limits and UNVERIFIED

**Model choices.**
- Rates move in parallel as a random walk with no pull back to normal (1.0 point a year).
- The 2033 shortfall is projected with yields frozen; T2 and T4 show where that misleads.
- Waiting cash earns 0% (about $4.5k of uncounted cushion at bill rates; `oct19/coupon/coupon_risk_options.md:195`).
- iBond funds are modelled as par bonds; the release margin is $5k.

**Inputs.**
- Stocks are lognormal at 7.0% (JPM 2026 LTCMA). The 2027 LTCMA figures are UNVERIFIED (`oct20/inflation/inflation.md:48`).
- The crash path uses US monthly-average data; VT is global.

**Scenario design.**
- Late deposit: the floor is bought at the forward yield for the later date. Laura's money waiting outside the portfolio earns nothing in the model.
- The deposit-size rows keep the plan's rule (top-up first, then floor = remainder). A team could choose another rule; that would change the numbers.

**Measures.**
- "Laura's free money" is the study's measure. It leaves out any amount above the announced top, which also stays hers: $2.9k in the DET base and $7.5k in T2 (`laura_kept33` in the JSON).
- The 1-in-20 stock band is a constant-return path, not a full distribution.

**Not modelled.** Taxes, FX, and the net-minimum rule.

**WInS** is not modelled. These are Laura's real-plan numbers; WInS gains never enter projections (case:131-133).

---

## 8. Files and how to rebuild

- **Scripts** (in `SEN/scripts/`):
  - `coupon_options.py` and `indep_pricer.py`: unmodified copies.
  - `sens_engine.py`: the wrapper.
  - `sens_run.py`: all scenarios.
  - `validate.py`: exact-match test against the 16 Oct study.
  - `seedcheck.py`: re-run on a second seed.
  - `tornado.py`: builds the tornado.
  - `show.py`: prints the tables.
  - `check_base.py`: ladder cost on 16 and 19 Oct.
- **Data** (in `SEN/data/`): `tsy_202610.csv` (fetched 19 Oct 22:01 UTC), `shiller_monthly.csv`, `sens_results.json` (every number), `tornado.csv`, `show_out.txt`, `tornado_out.txt`, `seedcheck_out.txt`, `sens_stdout.txt`.
- **Rebuild:** `cd SEN/scripts && CURVE_DAY=10/19/2026 NPATHS=100000 <venv>/bin/python -I sens_run.py && <venv>/bin/python -I show.py && <venv>/bin/python -I tornado.py` (about 1 minute). For the 6 Nov close, re-fetch the curve CSV and set `CURVE_DAY=11/06/2026`.
