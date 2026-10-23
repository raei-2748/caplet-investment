# Operating reserve schedule for Laura's real plan, with and without option 3r (20 Oct 2026)

> **Verified 20 Oct (`oct20/verify_reserve/verify_reserve.md`): core confirmed, corrections apply.** Test M is wrong: coupons waiting in bills leave the ladder about $3.0k short (not $4.2k) and $0.9k (not $2.2k) from Laura without 3r; with 3r the gift stays $168,919; the cost is a bet on bills staying ~1 point below long yields for 15 years. SGOV WAS seen on WInS on 29 Sep (team WInS Notes tab; screenshot still needed). Leaving out the 0.07% fund fee overstates the funds by about $1.4k (ladder) and $0.5k (floor). A fall during 2027 (before 3r exists) still takes $4.8k from Laura with 3r ($16.4k without, bottom to $140k). Front-loaded figures: quote one basis (~$18.5k / $15.0k / $11.8k / $2.0k for falls to 3% from 2027 / 2028 / 2029 / 2033). 1984 path: about at the bottom ($185 above after the iBond coupon fix), not "holds". T4 3%/7% totals $439,481 / $384,044; 7% funded ratio 102.7%. IBTR is used because it matures closer than the Feb-2036 bond, not because WInS has no bond. **Consistency fix 20 Oct (`oct20/consistency/consistency_audit.md` rows 7, 26):** 0.02% / 15.6% are study-engine figures; never quote 0.02% (marked at market 0.08% / 0.32% / 0.72%); agreed basis option 1 about 14.5%, 3r about 0.6%, worst about $3.3k (REG D5; REC §5); §0 item 5 now says test M is about $3.0k; SGOV was seen on WInS 29 Sep.


**Status.** AI-generated research by Claude Code for Team Caplet, Tue 20 Oct 2026 (Sydney). Every number is MODEL output from scripts an AI wrote. None of it has been rebuilt by a student yet. Nothing here is text to submit: it drafts no IPS sentence, no Final Report paragraph and no co-sponsor wording. If the team uses any number or table, record that in the AI-use log now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). UNVERIFIED marks anything nobody could confirm.

**Short forms.** `oct19/`, `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`. `case:n` = line n of `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`. `snap/main/` = `/home/user/snap/main/` (repo `main`, 19 Oct). "V5" = the IPS Report Doc's "Version 5" tab as read live on 19 Oct (`oct19/drive/ips_report_live.md:15-31`). "3r" = the AI-recommended option from the 19 Oct coupon study: $10,000 of the 2028 deposit in extra 3.125% Treasuries maturing 15 Nov 2041 (`oct19/coupon/coupon_risk_options.md:126-134`). The team has not voted on 3r; the vote is set for Tue 27 Oct (`oct19/out/Caplet_Update_19Oct2026.md:297-321`).

---

## 0. The short version

1. **Size on 1 Jan 2033.** The reserve is the payment ladder bought in January 2027, after six years of coupons have bought more of each holding. It is not a new purchase. On the on-plan path it is worth about **$410k if yields are flat at 5% that day, $440k at 3% and $384k at 7%**. That is the $50k due that day plus nine holdings. Add about $5k more with 3r (T4).
2. **The funded ratio barely moves when its value does.** From 3% to 7%, the value swings by about $55k, but the ten rungs alone stay at **99.7% to 102.1%** of what the payments are worth at the same yield. They stay above 100% except when yields fall to 3% (T4, T5A). This is the core evidence for "high certainty". The ladder's value and the payments' value move together.
3. **The risk that is left is front-loaded.** A permanent 2-point fall costs the ladder about $19.5k if it happens in January 2027. It costs about $12-15k if it happens in 2028-29, but only about $2k if it happens in 2033 (T9; independent check 5). This is because most of the coupon reinvesting happens before 2033. So the cover must exist from 2028, which is when 3r buys it.
4. **What 3r changes in a bad path.** Take yields falling to 3% on 1 Jan 2029. Without 3r, $9.7k of Laura's kept money is locked into the reserve in 2033, and she keeps $15.6k. With 3r, nothing is taken from her and she keeps $21.6k. The cost is a gift of $161k instead of $170k, still inside the $135k-$169k range (T5-G2). In the 19 Oct Monte Carlo refresh (study engine), payments are short in 15.6% of paths without 3r and, with it, 0.08% / 0.32% / 0.72% once the reserve is marked at market (MC / bootstrap / history; never quote the at-cost 0.02%); on the agreed basis option 1 is about 14.5% and 3r about 0.6%, worst about $3.3k (REC §5; REG D5) (§6c) [consistency fix 20 Oct, row 7].
5. **The composition changes on its own.** Nothing is traded. Each December a fund matures, and from 2037 only T-bonds and cash are left. Cash waiting in a short-term Treasury ETF grows from 13% to about 50% of the reserve by 2041. Duration falls from 3.5 years to 0.4 years (T6b, T5). Three rules carry the design, and the IPS must state each one. **Income is reinvested in the holding that paid it**: if T-bond coupons sat in bills instead, the ladder would be about $3.0k short on plan, $0.9k of it from Laura (test M, as corrected by verify_reserve) [consistency fix 20 Oct, row 26]. This rule is in the V4, V3 and Tab 15 drafts but **not in the live V5 text**. **Maturity proceeds wait in a named WInS-listed short-term Treasury ETF.** **An unavailable holding is replaced by an earlier-maturing Treasury.**

**New since 19 Oct.** The treasury.gov curve for **Mon 19 Oct** is now published (fetched 19 Oct 21:41 UTC = Tue 20 Oct 08:41 Sydney). Yields beyond one year rose 3-6bp: the 10-year went from 5.09 to 5.15. On the coupon-study basis the ladder now costs **$298,446**, leaving **$1,554 of room** (a 5.4bp fall uses it up), against $300,174 (−$174) on 16 Oct. The odds that it costs more than $300k on 1 Jan 2027 are about 43-45% (MODEL, σ 0.71-1.0 pt a year; §1). All tables use the 19 Oct curve.

---

## 1. What the case asks, and where each answer is

case:94-99 says: "At the beginning of 2033, before making the first operating payment or contributing to the facility, Laura will set aside a portion of the portfolio to fund the ten payments. This set-aside is called the operating reserve. Teams must recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made. They should also define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions supporting their recommendation."

| Case element | What this file gives (evidence, not wording) | Where |
|---|---|---|
| Set aside "before making the first operating payment or contributing to the facility" (case:94-95) | The 1 Jan 2033 order: (1) the reserve is ring-fenced (ladder, 2027 leftover, kept 3r bond, any set-aside); (2) the $50k payment; (3) the gift = floor + half of VT (+ 3r release), capped at the 2031 top; (4) Laura keeps the rest | §3, T3, T4 |
| "size" (case:96) | Two ways to state it. **Holdings:** what the 2027 bonds have become (T4 face column). **Value:** $384k / $410k / $440k at 7/5/3% (+$5k with 3r). Against the value of the ten payments ($374k / $404k / $439k) | T4 |
| "initial asset composition" (case:96) | On 1 Jan 2033: about 43% in four iBond Treasury funds (2033-2036), 44% in five T-bonds (2037-2041), 13% cash ($50k being paid that day plus the leftover), 1% the 3r bond | T4, T6b |
| "how its composition should change, if at all" (case:96-97) | Run-off only, with no trading: one rung matures each year; funds are gone by 2037; waiting cash rises; duration falls. Plus three standing rules (reinvest income, park proceeds, replace if unavailable) and two optional ones the team could adopt (§7) | T5, T6, T6b, T7 |
| "define ... a high degree of funding certainty" (case:97-98) | Three ways to define it, each with its number | §6b |
| "how they evaluated" (case:98) | This deterministic ledger (flat 3/5/7% and named stress paths); the coupon study's Monte Carlo (100,000 paths) and history replay (690 windows), refreshed on 19 Oct; funded-ratio and duration tests | §5, §6a, §6c |
| "identify the assumptions" (case:98-99) | Assumptions table with sources and UNVERIFIED flags | §6d |

---

## 2. Method: how to check and rebuild every number

**Inputs.**
- **Curve.** treasury.gov daily par yield curve, row for 10/19/2026: 1m 4.11, 3m 4.27, 6m 4.37, 1y 4.50, 2y 4.77, 3y 4.85, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48. URL: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv (fetched 19 Oct 2026 21:41 UTC). Copy: `oct20/reserve/data/tsy_202610.csv`. The 16 Oct row in it is identical to the copy the 19 Oct coupon study used.
- **Holdings and coupons.** These are the real WInS holdings, all filled 7-8 Oct (`snap/main/COMPETITION.md:174-186`; Feb-2037 coupon 4.750%, not 5.000%, per `oct19/out/Caplet_Update_19Oct2026.md:86`): IBTM (Dec 2032), IBTO (Dec 2033), IBTP (Dec 2034), IBTQ (Dec 2035) and IBTR (Dec 2036), plus T 4.750% 15 Feb 2037, 4.500% 15 May 2038, 4.375% 15 Nov 2039, 4.250% 15 Nov 2040 and 3.125% 15 Nov 2041. Laura's real plan may use only WInS-listed stocks, ETFs and Treasury bonds. The FAQ says "Investments permitted (for BOTH contributions, the IPS and Final Report)" and "Anything other than the approved investments listed above" is not permitted (`oct19/askwharton/web/faqs.txt:44-56`, fetched 19 Oct).

**Conventions (the same as the 19 Oct coupon study, so its vote numbers and these tables agree).**
1. **The 19 Oct curve is treated as the 1 Jan 2027 curve.** Yields are held unchanged. The curve is bootstrapped with `indep_pricer.py`.
2. **Rung sizing.** Each rung is sized so that, with its income reinvested at its own purchase yield *y*, it holds exactly $50,000 on its own maturity date. **Hand formula:** cost of a rung = 50,000 / (1 + y/2)^(2T), where T is the years from 1 Jan 2027 to maturity. Face = cost / (dirty price / 100). Check, Nov-2041: 22,751 × (1.026825)^(29.74) ≈ $50,0xx.
3. **iBond funds** are modelled as semiannual par bonds that end on 15 Dec. iShares says the funds "will terminate on or about October or December 15" and "do not seek to return any predetermined amount" (iShares IBTM page, https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf, read 20 Oct 2026; copy `oct20/reserve/web/IBTM_328944.txt:966-968`).
4. **Before 2033** every holding's income buys more of the same holding at that holding's yield. That is the drafts' rule, "income reinvested in the holding that paid it" (V4 `oct19/drive/ips_report_live.md:45`, V3 :156, Tab 15 :277). **The live V5 text (:25-31) has no reinvestment rule**: it mentions reinvestment only as a risk.
5. **2 Jan 2028.** The 2028 deposit first fills any 2027 gap. Under 3r, $10k then buys the Nov-2041 bond at the curve's 13.87-year par yield (5.297%). The floor R (what is left) buys IBTM at the forward yield (5.108%), sized to repay R on 15 Dec 2032. The rest goes into VT.
6. **2031 range.** Bottom = (R − $3,700), rounded down to the nearest $5k, less any projected shortfall that the named cover cannot meet (the "net-minimum rule"). Top = R + half of VT, plus $10k under 3r, less the same amount (`oct19/coupon/coupon_risk_options.md:26-31`).
7. **1 Jan 2033.** The projected shortfall (yields frozen at that day's level) is covered by the 2027 leftover first. Under 3r the bond comes next: it keeps what is needed plus $5k and releases the rest to the gift. Then Laura's kept money is set aside, then the gift above the floor. Gift = min(top, floor paid + half of VT + 3r release). **"Laura keeps" here means everything not given and not set aside.** That includes the part of VT above the cap, so it is larger than the coupon study's "free money", which counts only half of VT.
8. **After 2033.** Maturity proceeds and the $50k paid out on 15 Dec wait in a short-term Treasury ETF (SGOV named; §6d) and earn the scenario's yield less SGOV's 0.09% fee. In a year when that pool cannot pay $50k, the cover order is: leftover → 3r bond (sold at market) → 2033 set-aside.
9. **Flat-yield scenarios.** On 1 Jan 2033 the whole curve jumps to a flat 3%, 5% or 7% and stays there. All reinvesting and all valuing use that yield.
10. **Valuation.** Value = the price of the remaining cash flows at the flat yield, compounded semiannually. The value of the payments uses the same convention. **Funded ratio** = (holdings + waiting cash + cover pots) / (value of the payments still due, today's counted at $50,000).
11. **VT** grows at 7% compound less its 0.06% fee (JPM 2026 LTCMA AC World 7.00% compound; `snap/main/CLAUDE.md` key facts). This deterministic path is the Monte Carlo's median path.

**Spreadsheet rebuild (for students).**
- **Payments' value on date d at yield X:** `=PV((1+X/2)^2-1, n, -50000, 0, 1)` with n payments left. For example, on 1 Jan 2033 at 5% it is $404,404. The script gives $404,422; the $18 gap is because the script counts actual days. The plain annual-compounding `=PV(5%,10,-50000,0,1)` gives $405,391. That is the "$405k" in the Final Report prep pack (`oct19/frprep/final_report_prep.md:214`). Pick one convention and say which.
- **A T-bond's value:** face (from T6) × (`PRICE(settle, maturity, coupon, X, 100, 2)` + accrued interest) / 100. **A fund's value:** about 50,000 / (1+X/2)^(2t) for years-to-end t. For example, IBTO on 1 Jan 2033 at 3% is $48,6xx by hand; T4 gives $48,590.
- **Run-off:** each year, waiting cash before the payment = last year's cash after the payment, grown at the cash rate, plus this year's maturities. Then pay $50k. Any shortfall comes from the cover pots in order.
- **Reproduce:** `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I oct20/reserve/scripts/make_tables.py oct20/reserve/data/tsy_202610.csv 10/19/2026 oct20/reserve/out19`. It writes `tables.md`, `runoff_schedules.csv` (every row of every run-off) and `key_numbers.json`. Run time is about 2 seconds. Re-run on the 1 Jan 2027 curve when the real purchase is priced (any other date can be put in the date argument).
- **Checks done (twice).** `oct20/reserve/checks/independent_checks.py` re-derives several figures without the engine: the payments' value by closed form; the Nov-41 face path by a hand loop (36,884 matches); floor cost, VT, the 2031 top and the 3r value by hand (all match). The engine also reproduces the coupon study's ladder cost exactly ($300,174 on 16 Oct; $298,446 on 19 Oct). For a permanent fall from January 2027 with cash at 0%, the engine gives $10.1k / $19.5k / $28.2k for 1/2/3 points. The coupon study gives $9.5k / $19.0k / $27.7k. The $0.5k gap has a cause: in the study's ledger the iBond funds pay a coupon at their yield (about 4.99-5.15%) instead of their coupon rate (about 4.94-5.12%) (`oct19/coupon/scripts/coupon_options.py:141`). That slightly overstates what the funds deliver. The study's option ranking is unaffected.

**Breakeven and odds (19 Oct, this basis).** A ladder DV01 of $288 per 0.01 point gives a breakeven fall of 5.4bp. At 74 days to 1 Jan and σ 0.71-1.0 points a year, P(cost > $300k) is 43%-45% (MODEL; same method as `oct19/numbers/findings.md:62`). On 16 Oct the same basis gave 50.5-50.7%. These odds move every day, so quote the rule, not the level (`oct19/out/Caplet_Update_19Oct2026.md:245-247`).

---

## 3. Build-up 2027-2033 (Jan 2027 purchase, Jan 2028 deposit, 2031 announcement)

#### T1. The ten rungs bought on 1 Jan 2027 (curve 10/19/2026 treated as the 1 Jan 2027 curve)
| Rung | Pays 1 Jan | Matures | Coupon | Own yield | Face (fund: $ at par) | Price /100 (dirty) | Cost |
|---|---|---|---|---|---|---|---|
| IBTM | 2033 | 2032-12-15 | 4.944% | 4.988% | $37,287 | 100.000 | $37,287 |
| IBTO | 2034 | 2033-12-15 | 4.999% | 5.038% | $35,375 | 100.000 | $35,375 |
| IBTP | 2035 | 2034-12-15 | 5.039% | 5.075% | $33,562 | 100.000 | $33,562 |
| IBTQ | 2036 | 2035-12-15 | 5.079% | 5.112% | $31,821 | 100.000 | $31,821 |
| IBTR | 2037 | 2036-12-15 | 5.119% | 5.149% | $30,144 | 100.000 | $30,144 |
| T4.750 Feb37 | 2038 | 2037-02-15 | 4.750% | 5.157% | $30,282 | 98.601 | $29,859 |
| T4.500 May38 | 2039 | 2038-05-15 | 4.500% | 5.208% | $29,471 | 94.573 | $27,872 |
| T4.375 Nov39 | 2040 | 2039-11-15 | 4.375% | 5.268% | $27,743 | 92.294 | $25,605 |
| T4.250 Nov40 | 2041 | 2040-11-15 | 4.250% | 5.309% | $26,785 | 90.239 | $24,171 |
| T3.125 Nov41 | 2042 | 2041-11-15 | 3.125% | 5.365% | $29,302 | 77.644 | $22,751 |
| Total |  |  |  |  |  |  | **$298,446** |

Reading T1. The ten rungs cost $298,446 on this basis. The $1,554 left over waits in IBTM to Dec 2032 (one plan choice; Tab 15 still lists where it sits as a team decision, `oct19/drive/ips_report_live.md:287`). The longest rung is bought first (V5). If the ladder costs more than $300k on the day, the unbought part is the nearest rungs (IBTM, IBTO), and the 2028 deposit completes them first. Test L in T9 shows a curve 0.5 points lower: the ladder costs $313,267, the floor R drops to $136,733 and the 2031 bottom to $130k.

#### T2a. Build-up 2027-2033, on plan, without 3r (IPS V5 as live)
Values at each holding's own purchase yield (no market move). 1 Jan 2033 is before the payment and before the gift.
| Date | Ladder (incl. matured cash) | 2027 leftover | Floor (IBTM) | 3r bond | VT | Total |
|---|---|---|---|---|---|---|
| 2027-01-01 | $298.4k | $1.6k | $0.0k | - | $0.0k | $300.0k |
| 2028-01-02 | $314.0k | $1.6k | $116.8k | - | $33.2k | $465.7k |
| 2029-01-01 | $330.4k | $1.7k | $122.9k | - | $35.5k | $490.5k |
| 2030-01-01 | $347.6k | $1.8k | $129.2k | - | $37.9k | $516.6k |
| 2031-01-01 | $365.8k | $1.9k | $135.9k | - | $40.5k | $544.1k |
| 2032-01-01 | $384.8k | $2.0k | $142.9k | - | $43.4k | $573.1k |
| 2033-01-01 | $404.9k | $2.1k | $150.3k | - | $46.4k | $603.7k |

#### T2b. Build-up 2027-2033, on plan, with 3r ($10k in the Nov-2041 bond)
Values at each holding's own purchase yield (no market move). 1 Jan 2033 is before the payment and before the gift.
| Date | Ladder (incl. matured cash) | 2027 leftover | Floor (IBTM) | 3r bond | VT | Total |
|---|---|---|---|---|---|---|
| 2027-01-01 | $298.4k | $1.6k | $0.0k | $0.0k | $0.0k | $300.0k |
| 2028-01-02 | $314.0k | $1.6k | $109.1k | $10.0k | $30.9k | $465.7k |
| 2029-01-01 | $330.4k | $1.7k | $114.7k | $10.5k | $33.1k | $490.4k |
| 2030-01-01 | $347.6k | $1.8k | $120.6k | $11.1k | $35.4k | $516.5k |
| 2031-01-01 | $365.8k | $1.9k | $126.9k | $11.7k | $37.8k | $544.0k |
| 2032-01-01 | $384.8k | $2.0k | $133.4k | $12.3k | $40.5k | $573.0k |
| 2033-01-01 | $404.9k | $2.1k | $140.3k | $13.0k | $43.3k | $603.5k |

#### T3. Key plan numbers, on plan (no market move; VT at 7% compound less 0.06% fee)
| Item | Without 3r | With 3r |
|---|---|---|
| Ladder cost 1 Jan 2027 | $298,446 | $298,446 |
| Leftover 1 Jan 2027 (waits in IBTM) | $1,554 | $1,554 |
| 2028: 3r bond bought | $0 | $10,000 |
| 2028: floor R (repaid 15 Dec 2032) | $150,000 | $140,000 |
| 2028: floor cost (IBTM) | $116,842 | $109,052 |
| 2028: IBTM forward yield used | 5.108% | 5.108% |
| 2028: VT bought | $33,158 | $30,948 |
| 2031: VT value | $40,542 | $37,839 |
| 2031: projected payment shortfall (yields frozen) | $0 | $0 |
| 2031: announced bottom | $145,000 | $135,000 |
| 2031: announced top | $170,271 | $168,919 |
| 2033: floor paid out | $150,286 | $140,267 |
| 2033: VT value | $46,365 | $43,274 |
| 2033: 3r value / released to gift | $0 / $0 | $12,987 / $7,987 |
| 2033: gift | $170,271 | $168,919 |
| 2033: Laura keeps | $26,380 | $22,608 |
| 2042: left over for Laura after the last payment | $8,115 | $16,107 |

**The 2031 announcement (1 Jan 2031, nothing traded).**
- **On plan.** The range is $145,000-$170,271 without 3r and $135,000-$168,919 with 3r. The projected shortfall is $0.
- **The bottom depends only on R** (what the 2028 deposit has left after the ladder and 3r). It does not depend on markets after January 2028. So it is known from January 2028, three years before the announcement, except for the iBond payout and the reinvestment risk on the floor itself. In G2 the floor pays $139.2k against R = $140k, which is why there is a $3,700 rounding allowance.
- **The top depends on VT on 1 Jan 2031.** It is cut only if the projected shortfall is bigger than the leftover + 3r + half of VT. That happened in no deterministic test here. It happened on the 16 Oct curve in path G: without 3r the bottom became $140k (`oct20/reserve/out16/tables.md`, T9 row G).
- **Stress at the announcement.** In path G (yields at a flat 3% from 2 Jan 2028, before the floor is bought), the floor costs more, so VT is only $20.6k and the top is $162k. In path H (G plus VT −40% in 2032), the gift is $154.5k without 3r and $148.2k with it. Both are inside their ranges, and both bottoms hold (T9).

**1 Jan 2033, in order.** (1) IBTM's payment rung paid $50,000 (plus about $112 of interest over 17 days) on 15 Dec 2032. The floor paid $150,286 ($140,267 under 3r), and the leftover $2,087. (2) The reserve is ring-fenced (T4). (3) $50,000 is paid. (4) Gift: $170,271 without 3r, $168,919 with 3r, both capped at the top. (5) Laura keeps $26,380 / $22,608. On plan she also gets $8.1k / $16.1k back after the last payment in 2042. Under 3r the extra comes from the kept part of the 3r bond (T3).

---

## 4. The reserve on 1 Jan 2033: size and initial composition

#### T4. The operating reserve on 1 Jan 2033 (before the first payment): size and initial composition
Holdings after the on-plan build-up, valued on 1 Jan 2033 if the whole curve were flat at 3%, 5% or 7% that day. 'Face' for a T-bond is the face owned after six years of coupons bought more of it.
**T4a. Without 3r.** In each column the yield is flat at that level from 1 Jan 2033 on (the set-aside and release are worked out at that yield).
| Holding | Pays | Face | Value at 3% | Value at 5% | Value at 7% |
|---|---|---|---|---|---|
| Cash from the IBTM payment rung (in SGOV, paid out today) | 2033 | $50,112 | $50,112 | $50,112 | $50,112 |
| IBTO | 2034 | fund | $48,590 | $47,702 | $46,838 |
| IBTP | 2035 | fund | $47,108 | $45,402 | $43,776 |
| IBTQ | 2036 | fund | $45,626 | $43,210 | $40,948 |
| IBTR | 2037 | fund | $44,144 | $41,112 | $38,326 |
| T4.750 Feb37 | 2038 | $40,414 | $43,860 | $40,763 | $37,927 |
| T4.500 May38 | 2039 | $38,991 | $42,103 | $38,315 | $34,923 |
| T4.375 Nov39 | 2040 | $36,640 | $39,955 | $35,530 | $31,672 |
| T4.250 Nov40 | 2041 | $35,288 | $38,553 | $33,776 | $29,683 |
| T3.125 Nov41 | 2042 | $36,884 | $37,390 | $32,126 | $27,705 |
| 2027 leftover (cash, SGOV) | cover |  | $2,086 | $2,088 | $2,090 |
| **Reserve total** |  |  | **$439,526** | **$410,137** | **$383,999** |
| Value of the ten payments (same yield) |  |  | $438,909 | $404,422 | $374,093 |
| Funded ratio, ten rungs only |  |  | 99.7% | 100.9% | 102.1% |
| Funded ratio, whole reserve |  |  | 100.1% | 101.4% | 102.6% |

**T4b. With 3r.** In each column the yield is flat at that level from 1 Jan 2033 on (the set-aside and release are worked out at that yield).
| Holding | Pays | Face | Value at 3% | Value at 5% | Value at 7% |
|---|---|---|---|---|---|
| Cash from the IBTM payment rung (in SGOV, paid out today) | 2033 | $50,112 | $50,112 | $50,112 | $50,112 |
| IBTO | 2034 | fund | $48,590 | $47,702 | $46,838 |
| IBTP | 2035 | fund | $47,108 | $45,402 | $43,776 |
| IBTQ | 2036 | fund | $45,626 | $43,210 | $40,948 |
| IBTR | 2037 | fund | $44,144 | $41,112 | $38,326 |
| T4.750 Feb37 | 2038 | $40,414 | $43,860 | $40,763 | $37,927 |
| T4.500 May38 | 2039 | $38,991 | $42,103 | $38,315 | $34,923 |
| T4.375 Nov39 | 2040 | $36,640 | $39,955 | $35,530 | $31,672 |
| T4.250 Nov40 | 2041 | $35,288 | $38,553 | $33,776 | $29,683 |
| T3.125 Nov41 | 2042 | $36,884 | $37,390 | $32,126 | $27,705 |
| 2027 leftover (cash, SGOV) | cover |  | $2,086 | $2,088 | $2,090 |
| 3r bond kept (T3.125 Nov41: need + $5k) | cover |  | $5,000 (released $10,454) | $5,000 (released $8,279) | $5,000 (released $6,451) |
| **Reserve total** |  |  | **$444,526** | **$415,137** | **$388,999** |
| Value of the ten payments (same yield) |  |  | $438,909 | $404,422 | $374,093 |
| Funded ratio, ten rungs only |  |  | 99.7% | 100.9% | 102.1% |
| Funded ratio, whole reserve |  |  | 101.3% | 102.6% | 104.0% |

**How to read T4.**
- **The rungs alone are 99.7% funded at 3%, 100.9% at 5% and 102.1% at 7%.** In other words, if yields fall to 3% and stay there, the ten rungs are about $1.5k short in today's money. The leftover covers that.
- **The size in dollars is not a target.** It is whatever the 2027 bonds have grown into. Stating it as a dollar figure without a yield and date is meaningless: it moves about $29k for a 2-point move (T10).
- **The 3r line under a fall to 3% is not a typo.** The 3r bond jumps in value, the projected need is still covered by the leftover, so the release rule frees $10.5k. The gift is capped at the top, so most of that goes to Laura.

---

## 5. Run-off 2033-2042: holdings, value, cash flows, funded ratio

#### T5A. Reserve value and funded ratio each 1 Jan (before the payment), yields flat at 3%, 5% or 7% from 1 Jan 2033
Reserve = ladder holdings + SGOV pool + cover pots (2027 leftover; under 3r the kept 3r bond). Funded ratio = reserve value / value of the payments still due, both at the same flat yield.
| 1 Jan | No 3r @3% | No 3r @5% | No 3r @7% | 3r @3% | 3r @5% | 3r @7% | Payments left, value @3/5/7% |
|---|---|---|---|---|---|---|---|
| 2033 | $439.5k / 100.1% | $410.1k / 101.4% | $384.0k / 102.7% | $444.5k / 101.3% | $415.1k / 102.6% | $389.0k / 104.0% | $438.9k / $404.4k / $374.1k |
| 2034 | $401.2k / 100.2% | $378.3k / 101.6% | $357.8k / 103.1% | $406.4k / 101.4% | $383.6k / 103.0% | $363.2k / 104.6% | $400.7k / $372.4k / $347.2k |
| 2035 | $361.8k / 100.2% | $345.0k / 101.9% | $329.7k / 103.6% | $367.1k / 101.6% | $350.5k / 103.5% | $335.4k / 105.4% | $361.2k / $338.7k / $318.3k |
| 2036 | $321.3k / 100.2% | $309.9k / 102.2% | $299.6k / 104.2% | $326.7k / 101.9% | $315.7k / 104.1% | $305.8k / 106.4% | $320.6k / $303.3k / $287.4k |
| 2037 | $279.5k / 100.2% | $273.0k / 102.6% | $267.4k / 105.1% | $285.1k / 102.2% | $279.1k / 104.9% | $274.0k / 107.7% | $278.8k / $266.1k / $254.4k |
| 2038 | $236.3k / 100.2% | $234.3k / 103.2% | $232.8k / 106.3% | $242.2k / 102.7% | $240.7k / 106.0% | $239.8k / 109.6% | $235.8k / $227.0k / $218.9k |
| 2039 | $191.9k / 100.3% | $193.5k / 104.0% | $195.7k / 108.2% | $197.9k / 103.4% | $200.2k / 107.7% | $203.3k / 112.3% | $191.4k / $186.0k / $180.9k |
| 2040 | $146.2k / 100.4% | $150.8k / 105.5% | $156.0k / 111.3% | $152.4k / 104.6% | $157.8k / 110.5% | $164.1k / 117.0% | $145.6k / $142.9k / $140.2k |
| 2041 | $99.1k / 100.6% | $105.9k / 108.5% | $113.6k / 117.5% | $105.5k / 107.0% | $113.3k / 116.1% | $122.2k / 126.4% | $98.5k / $97.6k / $96.7k |
| 2042 | $50.6k / 101.2% | $58.7k / 117.3% | $68.0k / 136.1% | $57.1k / 114.3% | $66.5k / 132.9% | $77.3k / 154.7% | $50.0k / $50.0k / $50.0k |

**Reading T5A.**
- **The funded ratio rises over time** in every case except the ladder alone at 3%. Waiting cash earns interest in SGOV, and the T-bonds bought at 5.2-5.4% are reinvesting at the flat yield.
- **At 3% the ladder alone drifts down to 97.7% by 2042.** It is $2.0k short in total, and the 2027 leftover covers exactly that (T5-3a). With 3r there is about $5-7k of spare cover behind it.
- **At 7% the surplus builds to $18-27k by 2042.** It goes back to Laura after the last payment. Whether to release a surplus earlier is an optional rule (§7).

#### T5-5b. Cash-flow run-off, yields flat at 5% from 1 Jan 2033, with 3r
2033: set-aside $0 (from Laura $0, from gift $0); 3r value $13,279, released $8,279; gift $168,919; Laura keeps $22,946 in 2033 and $16,453 after the last payment.
| 1 Jan | Ladder holdings left (before payment) | Coupons reinvested, prior year | Maturities into SGOV, prior year | SGOV pool before payment | Pool short of $50k | Cover used | Cover pots before payment (leftover + 3r + set-aside) | Reserve value before payment | Value of payments left (incl. today's) | Funded ratio: ladder only / whole reserve | Payments left after / nominal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2033 | IBTO IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $17,452 | $50,000 | $50,112 | $0 | none | $7,088 | $415,137 | $404,422 | 100.9% / 102.6% | 9 / $450,000 |
| 2034 | IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $15,847 | $50,000 | $50,229 | $0 | none | $7,444 | $383,602 | $372,352 | 101.0% / 103.0% | 8 / $400,000 |
| 2035 | IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $14,130 | $49,997 | $50,349 | $0 | none | $7,817 | $350,472 | $338,659 | 101.2% / 103.5% | 7 / $350,000 |
| 2036 | IBTR Feb37 May38 Nov39 Nov40 Nov41 | $12,303 | $49,990 | $50,468 | $0 | none | $8,209 | $315,665 | $303,262 | 101.4% / 104.1% | 6 / $300,000 |
| 2037 | Feb37 May38 Nov39 Nov40 Nov41 | $10,359 | $49,976 | $50,578 | $0 | none | $8,621 | $279,135 | $266,111 | 101.7% / 104.9% | 5 / $250,000 |
| 2038 | May38 Nov39 Nov40 Nov41 | $7,202 | $49,969 | $52,719 | $0 | none | $9,054 | $240,656 | $227,044 | 102.0% / 106.0% | 4 / $200,000 |
| 2039 | Nov39 Nov40 Nov41 | $5,287 | $49,942 | $54,331 | $0 | none | $9,508 | $200,245 | $186,000 | 102.5% / 107.7% | 3 / $150,000 |
| 2040 | Nov40 Nov41 | $4,438 | $49,880 | $54,733 | $0 | none | $9,985 | $157,826 | $142,880 | 103.5% / 110.5% | 2 / $100,000 |
| 2041 | Nov41 | $2,488 | $49,823 | $55,097 | $0 | none | $10,487 | $113,275 | $97,592 | 105.3% / 116.1% | 1 / $50,000 |
| 2042 | cash only | $754 | $49,787 | $55,442 | $0 | none | $11,011 | $66,453 | $50,000 | 110.9% / 132.9% | 0 / $0 |

#### T5-5a. Cash-flow run-off, yields flat at 5% from 1 Jan 2033, without 3r
2033: set-aside $0 (from Laura $0, from gift $0); 3r value $0, released $0; gift $170,271; Laura keeps $26,429 in 2033 and $8,656 after the last payment.
| 1 Jan | Ladder holdings left (before payment) | Coupons reinvested, prior year | Maturities into SGOV, prior year | SGOV pool before payment | Pool short of $50k | Cover used | Cover pots before payment (leftover + 3r + set-aside) | Reserve value before payment | Value of payments left (incl. today's) | Funded ratio: ladder only / whole reserve | Payments left after / nominal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2033 | IBTO IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $17,452 | $50,000 | $50,112 | $0 | none | $2,088 | $410,137 | $404,422 | 100.9% / 101.4% | 9 / $450,000 |
| 2034 | IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $15,847 | $50,000 | $50,229 | $0 | none | $2,191 | $378,349 | $372,352 | 101.0% / 101.6% | 8 / $400,000 |
| 2035 | IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $14,130 | $49,997 | $50,349 | $0 | none | $2,298 | $344,953 | $338,659 | 101.2% / 101.9% | 7 / $350,000 |
| 2036 | IBTR Feb37 May38 Nov39 Nov40 Nov41 | $12,303 | $49,990 | $50,468 | $0 | none | $2,411 | $309,867 | $303,262 | 101.4% / 102.2% | 6 / $300,000 |
| 2037 | Feb37 May38 Nov39 Nov40 Nov41 | $10,359 | $49,976 | $50,578 | $0 | none | $2,529 | $273,043 | $266,111 | 101.7% / 102.6% | 5 / $250,000 |
| 2038 | May38 Nov39 Nov40 Nov41 | $7,202 | $49,969 | $52,719 | $0 | none | $2,654 | $234,255 | $227,044 | 102.0% / 103.2% | 4 / $200,000 |
| 2039 | Nov39 Nov40 Nov41 | $5,287 | $49,942 | $54,331 | $0 | none | $2,784 | $193,521 | $186,000 | 102.5% / 104.0% | 3 / $150,000 |
| 2040 | Nov40 Nov41 | $4,438 | $49,880 | $54,733 | $0 | none | $2,920 | $150,762 | $142,880 | 103.5% / 105.5% | 2 / $100,000 |
| 2041 | Nov41 | $2,488 | $49,823 | $55,097 | $0 | none | $3,064 | $105,852 | $97,592 | 105.3% / 108.5% | 1 / $50,000 |
| 2042 | cash only | $754 | $49,787 | $55,442 | $0 | none | $3,214 | $58,656 | $50,000 | 110.9% / 117.3% | 0 / $0 |

#### T5-3a. Cash-flow run-off, yields flat at 3% from 1 Jan 2033, without 3r
2033: set-aside $0 (from Laura $0, from gift $0); 3r value $0, released $0; gift $170,271; Laura keeps $26,294 in 2033 and $593 after the last payment.
| 1 Jan | Ladder holdings left (before payment) | Coupons reinvested, prior year | Maturities into SGOV, prior year | SGOV pool before payment | Pool short of $50k | Cover used | Cover pots before payment (leftover + 3r + set-aside) | Reserve value before payment | Value of payments left (incl. today's) | Funded ratio: ladder only / whole reserve | Payments left after / nominal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2033 | IBTO IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $17,452 | $50,000 | $50,067 | $0 | none | $2,086 | $439,481 | $438,909 | 99.7% / 100.1% | 9 / $450,000 |
| 2034 | IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $15,834 | $49,988 | $50,123 | $0 | none | $2,147 | $401,240 | $400,655 | 99.6% / 100.1% | 8 / $400,000 |
| 2035 | IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $14,073 | $49,927 | $50,121 | $0 | none | $2,209 | $361,843 | $361,247 | 99.6% / 100.2% | 7 / $350,000 |
| 2036 | IBTR Feb37 May38 Nov39 Nov40 Nov41 | $12,214 | $49,817 | $50,008 | $0 | none | $2,274 | $321,257 | $320,648 | 99.5% / 100.2% | 6 / $300,000 |
| 2037 | Feb37 May38 Nov39 Nov40 Nov41 | $10,253 | $49,659 | $49,733 | $267 | leftover $267 | $2,340 | $279,468 | $278,845 | 99.4% / 100.2% | 5 / $250,000 |
| 2038 | May38 Nov39 Nov40 Nov41 | $7,099 | $49,590 | $50,852 | $0 | none | $2,134 | $236,348 | $235,757 | 99.3% / 100.3% | 4 / $200,000 |
| 2039 | Nov39 Nov40 Nov41 | $5,193 | $49,398 | $51,179 | $0 | none | $2,196 | $191,938 | $191,368 | 99.2% / 100.3% | 3 / $150,000 |
| 2040 | Nov40 Nov41 | $4,350 | $49,023 | $50,418 | $0 | none | $2,260 | $146,214 | $145,637 | 98.8% / 100.4% | 2 / $100,000 |
| 2041 | Nov41 | $2,435 | $48,736 | $49,346 | $654 | leftover $654 | $2,325 | $99,119 | $98,534 | 98.2% / 100.6% | 1 / $50,000 |
| 2042 | cash only | $738 | $48,693 | $48,873 | $1,127 | leftover $1,127 | $1,720 | $50,593 | $50,000 | 97.7% / 101.2% | 0 / $0 |

#### T6. Holdings each 1 Jan (before the payment), yields flat at 5% from 2033, with 3r
T-bonds: face owned ($). Funds: market value ($) at 5%. Shows the face growing as coupons buy more of the same bond, then falling to zero at maturity.
| Date | IBTM | IBTO | IBTP | IBTQ | IBTR | 4.750 Feb37 | 4.500 May38 | 4.375 Nov39 | 4.250 Nov40 | 3.125 Nov41 | 3r (3.125 Nov41) | SGOV pool |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027-01-01 | $37,287 | $35,375 | $33,562 | $31,821 | $30,144 | $30,282 | $29,471 | $27,743 | $26,785 | $29,302 | - | $0 |
| 2030-01-01 | $43,227 | $41,071 | $39,009 | $37,025 | $35,111 | $35,004 | $33,933 | $31,920 | $30,785 | $32,958 | $13,631 | $0 |
| 2033-01-01 | - | $47,702 | $45,402 | $43,210 | $41,112 | $40,414 | $38,991 | $36,640 | $35,288 | $36,884 | $5,740 | $50,112 |
| 2034-01-01 | - | - | $47,699 | $45,396 | $43,192 | $42,373 | $40,804 | $38,316 | $36,876 | $38,214 | $5,947 | $50,229 |
| 2035-01-01 | - | - | - | $47,692 | $45,377 | $44,423 | $42,692 | $40,061 | $38,527 | $39,572 | $6,159 | $50,349 |
| 2036-01-01 | - | - | - | - | $47,672 | $46,567 | $44,660 | $41,877 | $40,241 | $40,958 | $6,374 | $50,468 |
| 2037-01-01 | - | - | - | - | - | $48,810 | $46,710 | $43,764 | $42,021 | $42,369 | $6,594 | $50,578 |
| 2038-01-01 | - | - | - | - | - | - | $48,843 | $45,726 | $43,867 | $43,807 | $6,818 | $52,719 |
| 2039-01-01 | - | - | - | - | - | - | - | $47,764 | $45,782 | $45,268 | $7,045 | $54,331 |
| 2040-01-01 | - | - | - | - | - | - | - | - | $47,767 | $46,753 | $7,276 | $54,733 |
| 2041-01-01 | - | - | - | - | - | - | - | - | - | $48,260 | $7,511 | $55,097 |
| 2042-01-01 | - | - | - | - | - | - | - | - | - | - | - | $55,442 |

#### T6b. How the reserve's mix changes (share of reserve value before each payment; flat 5% from 2033, with 3r)
| 1 Jan | iBond Treasury funds | T-bonds (payment rungs) | 3r bond (kept) | Cash in SGOV (incl. today's $50k and leftover) | Total |
|---|---|---|---|---|---|
| 2033 | 42.7% | 43.5% | 1.2% | 12.6% | $415,137 |
| 2034 | 35.5% | 49.4% | 1.4% | 13.7% | $383,602 |
| 2035 | 26.6% | 56.8% | 1.6% | 15.0% | $350,472 |
| 2036 | 15.1% | 66.3% | 1.8% | 16.8% | $315,665 |
| 2037 | 0.0% | 78.8% | 2.2% | 19.0% | $279,135 |
| 2038 | 0.0% | 74.3% | 2.7% | 23.0% | $240,656 |
| 2039 | 0.0% | 68.1% | 3.4% | 28.5% | $200,245 |
| 2040 | 0.0% | 59.0% | 4.5% | 36.5% | $157,826 |
| 2041 | 0.0% | 42.1% | 6.6% | 51.3% | $113,275 |
| 2042 | 0.0% | 0.0% | 11.7% | 88.3% | $66,453 |

#### T7. Income received each year and where it goes (yields flat at 5% from 2033, with 3r)
Coupon = reinvested in the same holding (fund distributions buy more fund shares; T-bond coupons buy more of the same bond). Maturity = principal into SGOV until the next 1 Jan payment.
| Calendar year | Ladder coupons reinvested | 3r coupons reinvested (kept part after 2033) | Floor + leftover income reinvested (to 2032) | Maturities into SGOV |
|---|---|---|---|---|
| 2027 | $14,672 | $0 | $78 | - |
| 2028 | $15,398 | $398 | $5,710 | - |
| 2029 | $16,158 | $414 | $6,005 | - |
| 2030 | $16,954 | $430 | $6,316 | - |
| 2031 | $17,786 | $447 | $6,642 | - |
| 2032 | $17,452 | $464 | $3,449 | IBTM $50,000 |
| 2033 | $15,847 | $181 | $0 | IBTO $50,000 |
| 2034 | $14,130 | $188 | $0 | IBTP $49,997 |
| 2035 | $12,303 | $194 | $0 | IBTQ $49,990 |
| 2036 | $10,359 | $201 | $0 | IBTR $49,976 |
| 2037 | $7,202 | $208 | $0 | T4.750 Feb37 $49,969 |
| 2038 | $5,287 | $215 | $0 | T4.500 May38 $49,942 |
| 2039 | $4,438 | $222 | $0 | T4.375 Nov39 $49,880 |
| 2040 | $2,488 | $229 | $0 | T4.250 Nov40 $49,823 |
| 2041 | $754 | $117 | $0 | T3.125 Nov41 $49,787 |

**Where income goes (the rule this schedule assumes, and why it matters).**
- **Fund distributions** (monthly, per the iShares IBTM page `oct20/reserve/web/IBTM_328944.txt:384`) buy more shares of the same fund.
- **T-bond coupons** buy more of the same bond. On WInS, bonds trade in $1,000 face units (`snap/main/COMPETITION.md:82`). A coupon of a few hundred dollars therefore has to wait in the short-term Treasury ETF until a whole unit can be bought. The minimum unit in Laura's real account is UNVERIFIED.
- **Test M** (T9) shows that if T-bond coupons simply sat in bills at today's 4.27% instead of being reinvested in the bond, the ladder would be **$4.2k short on plan**. Without 3r, $2.2k of that would come out of Laura's money in 2033. So "reinvest in the holding that paid it" carries real weight. The unit problem needs one line of rule: for example, coupons are pooled and swept into the bond once a unit can be bought. That is a decision for the team, not wording.
- **The waiting holding.** The model names **SGOV** (iShares 0-3 Month Treasury Bond ETF: 0.09% fee, monthly distributions, 30-day SEC yield 3.74% on 16 Oct; `oct20/reserve/web/ishares-0-3-month-treasury-bond-etf.txt:315-317, 392`). The fallback is **BIL** (SPDR Bloomberg 1-3 Month T-Bill ETF: gross fee 0.1353%, monthly; `oct20/reserve/web/BIL_ssga.txt:86, 157`). **Whether either is on WInS for 2026-27 is UNVERIFIED.** BIL and SHV were on the 2025-26 WGHIC approved ETF list (`snap/main/competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt:1077, 1101`); SGOV was not. Whichever one a WInS search shows, screenshot it (Caplet update item 3c-3, `oct19/out/Caplet_Update_19Oct2026.md:98`).
- **If no such ETF is allowed.** If waiting cash earns 0% (WInS cash pays 0%, `snap/main/COMPETITION.md:80`), the cost is $0.6k at 5% and $5.2k at 3% (tests I and J). Without 3r, the $3.1k in J is set aside from Laura's money.

---

## 6. Stress, certainty and assumptions

### 6a. Stress tests

#### T9. Stress tests (deterministic; each changes one thing unless stated)
| Test | Ladder short before cover (total) | No 3r: 2033 set-aside / uncovered | No 3r: 2031 range | No 3r: gift | No 3r: Laura keeps 2033 | 3r: set-aside / uncovered | 3r: 2031 range | 3r: gift | 3r: Laura keeps 2033 |
|---|---|---|---|---|---|---|---|---|---|
| A. On plan (own yields; SGOV at today's bill) | $0 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,380 | $0 / $0 | $135,000-$168,919 | $168,919 | $22,608 |
| B. Flat 5% from 2033 | $0 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,429 | $0 / $0 | $135,000-$168,919 | $168,919 | $22,946 |
| C. Flat 3% from 2033 (about 2 points down, for good) | $2,047 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,294 | $0 / $0 | $135,000-$168,919 | $168,919 | $24,996 |
| D. Flat 7% from 2033 | $0 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,561 | $0 / $0 | $135,000-$168,919 | $168,524 | $21,637 |
| E. Stress year 2036: 5% to 3% on 1 Jan 2036, for good | $0 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,429 | $0 / $0 | $135,000-$168,919 | $168,919 | $22,946 |
| F. Stress year 2036: 5% to 7% on 1 Jan 2036 | $0 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,429 | $0 / $0 | $135,000-$168,919 | $168,919 | $22,946 |
| G. Flat 3% from 2 Jan 2028 (fall before the floor and 3r are bought) | $14,978 | $12,912 / $0 | $145,000-$162,117 | $162,117 | $3,932 | $1,306 / $0 | $135,000-$161,736 | $153,608 | $12,115 |
| G2. Flat 3% from 1 Jan 2029 (fall after the 2028 purchases) | $11,772 | $9,698 / $0 | $145,000-$170,271 | $170,271 | $15,592 | $0 / $0 | $135,000-$168,919 | $161,221 | $21,637 |
| H. G plus VT -40% in 2032 | $14,978 | $12,912 / $0 | $145,000-$162,117 | $154,545 | $0 | $1,306 / $0 | $135,000-$161,736 | $148,240 | $6,746 |
| I. Flat 5% from 2033, but waiting cash earns 0% (no SGOV) | $636 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,094 | $0 / $0 | $135,000-$168,919 | $168,919 | $22,633 |
| J. Flat 3% from 2033 and waiting cash 0% | $5,169 | $3,085 / $0 | $145,000-$170,271 | $170,271 | $23,009 | $0 / $0 | $135,000-$168,919 | $168,919 | $21,724 |
| K. Flat 5% from 2033; IBTQ pays out 2% less than modelled (Dec 2035) | $534 | $0 / $0 | $145,000-$170,271 | $170,271 | $26,429 | $0 / $0 | $135,000-$168,919 | $168,919 | $22,946 |
| L. Curve 0.5 pts lower on 1 Jan 2027, then on plan | $0 | $0 / $0 | $130,000-$153,610 | $153,610 | $21,986 | $0 / $0 | $120,000-$152,376 | $152,376 | $18,053 |
| M. On plan, but T-bond coupons wait in SGOV at today's bill rate (not reinvested in the bond) | $4,239 | $2,152 / $0 | $145,000-$170,271 | $170,271 | $24,228 | $0 / $0 | $135,000-$168,919 | $167,460 | $21,637 |

**What happens in a stress year (worked out for 1 Jan 2036).**
- **Yields fall from 5% to 3% overnight on 1 Jan 2036 and stay there.** On the day, the ladder's value rises by about $14.7k (+4.8%). The value of the payments rises by about $17.4k. That leaves a paper gap of about $2.7k (T10). In cash terms, no payment is short (T9-E): the surplus built up in SGOV during 2033-35 at 5% absorbs it, and the 3r bond is not touched. Nothing is sold. The January review re-runs the projection, and the cover order is already set. No gift is affected, because the gift was paid in 2033.
- **Yields rise from 5% to 7% on 1 Jan 2036.** The ladder's value falls by about $13.4k (−4.4%). The payments' value falls by about $15.9k, so the funded ratio *rises*. The loss is never realised, because nothing is sold before it matures (T9-F, T10).
- **A fund pays out 2% less than modelled** (IBTQ, Dec 2035). The pool is $1k short that year. Earlier interest in SGOV absorbs about half; the leftover covers the rest (T9-K).
- **A holding becomes unavailable** (delisted, or a fund closes early). The drafts' rule (V5's pending wording, `oct19/drive/ips_report_live.md:28`; V3 :156; Tab 15 :277) replaces it with a Treasury maturing earlier, and the proceeds wait in SGOV/BIL. This is not modelled. Its cost is the lost yield between the replacement's maturity and the payment, about $50k × the yield gap × the months early.
- **Worst real-world case named in the coupon study.** History since 1953, a June 1984 start, with a 5-point absolute fall. With 3r on the 19 Oct curve: payments are met and the gift is $136.2k against the $135k bottom. On 16 Oct the same path broke the bottom by $3.5k (§6c).

#### T10. What a one-day yield jump does to the reserve's value (on-plan holdings, 1 Jan of each year, 5% to 3% or 7%)
| 1 Jan | Ladder value at 5% | Change if 3% | Change if 7% | Change in value of payments (3% / 7%) |
|---|---|---|---|---|
| 2033 | $408,032 | $29,391 (+7.2%) | $-26,139 (-6.4%) | $34,487 / $-30,328 |
| 2036 | $307,729 | $14,651 (+4.8%) | $-13,430 (-4.4%) | $17,385 / $-15,855 |
| 2039 | $190,616 | $4,871 (+2.6%) | $-4,624 (-2.4%) | $5,367 / $-5,081 |
| 2041 | $102,534 | $817 (+0.8%) | $-796 (-0.8%) | $942 / $-915 |

#### T5-G2a. Stress path: yields fall to a flat 3% on 1 Jan 2029 (after the 2028 purchases) and stay, without 3r
Ladder short before cover $11,772 in total. 2031 range $145,000-$170,271. 2033: set-aside $9,698 (from Laura $9,698, from gift $0); 3r value $0, released $0; gift $170,271; Laura keeps $15,592 in 2033 and $2,464 after the last payment.
| 1 Jan | Ladder holdings left (before payment) | Coupons reinvested, prior year | Maturities into SGOV, prior year | SGOV pool before payment | Pool short of $50k | Cover used | Cover pots before payment (leftover + 3r + set-aside) | Reserve value before payment | Value of payments left (incl. today's) | Funded ratio: ladder only / whole reserve | Payments left after / nominal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2033 | IBTO IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $17,170 | $49,693 | $49,760 | $240 | leftover $240 | $11,772 | $440,971 | $438,909 | 97.8% / 100.5% | 9 / $450,000 |
| 2034 | IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $15,511 | $49,502 | $49,568 | $432 | leftover $432 | $11,867 | $402,765 | $400,655 | 97.6% / 100.5% | 8 / $400,000 |
| 2035 | IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $13,764 | $49,268 | $49,333 | $667 | leftover $667 | $11,767 | $363,404 | $361,247 | 97.3% / 100.6% | 7 / $350,000 |
| 2036 | IBTR Feb37 May38 Nov39 Nov40 Nov41 | $11,928 | $48,990 | $49,055 | $945 | leftover $854, set-aside $91 | $11,423 | $322,856 | $320,648 | 97.1% / 100.7% | 6 / $300,000 |
| 2037 | Feb37 May38 Nov39 Nov40 Nov41 | $10,000 | $48,667 | $48,732 | $1,268 | set-aside $1,268 | $10,784 | $281,105 | $278,845 | 96.9% / 100.8% | 5 / $250,000 |
| 2038 | May38 Nov39 Nov40 Nov41 | $6,909 | $48,572 | $49,808 | $192 | set-aside $192 | $9,793 | $238,027 | $235,757 | 96.8% / 101.0% | 4 / $200,000 |
| 2039 | Nov39 Nov40 Nov41 | $5,046 | $48,262 | $49,145 | $855 | set-aside $855 | $9,879 | $193,662 | $191,368 | 96.0% / 101.2% | 3 / $150,000 |
| 2040 | Nov40 Nov41 | $4,226 | $47,692 | $47,868 | $2,132 | set-aside $2,132 | $9,287 | $147,984 | $145,637 | 95.2% / 101.6% | 2 / $100,000 |
| 2041 | Nov41 | $2,364 | $47,287 | $47,462 | $2,538 | set-aside $2,538 | $7,364 | $100,937 | $98,534 | 95.0% / 102.4% | 1 / $50,000 |
| 2042 | cash only | $717 | $47,323 | $47,498 | $2,502 | set-aside $2,502 | $4,966 | $52,464 | $50,000 | 95.0% / 104.9% | 0 / $0 |

#### T5-G2b. Stress path: yields fall to a flat 3% on 1 Jan 2029 (after the 2028 purchases) and stay, with 3r
Ladder short before cover $11,772 in total. 2031 range $135,000-$168,919. 2033: set-aside $0 (from Laura $0, from gift $0); 3r value $15,033, released $335; gift $161,221; Laura keeps $21,637 in 2033 and $9,102 after the last payment.
| 1 Jan | Ladder holdings left (before payment) | Coupons reinvested, prior year | Maturities into SGOV, prior year | SGOV pool before payment | Pool short of $50k | Cover used | Cover pots before payment (leftover + 3r + set-aside) | Reserve value before payment | Value of payments left (incl. today's) | Funded ratio: ladder only / whole reserve | Payments left after / nominal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2033 | IBTO IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $17,170 | $49,693 | $49,760 | $240 | leftover $240 | $16,772 | $445,971 | $438,909 | 97.8% / 101.6% | 9 / $450,000 |
| 2034 | IBTP IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $15,511 | $49,502 | $49,568 | $432 | leftover $432 | $17,029 | $407,927 | $400,655 | 97.6% / 101.8% | 8 / $400,000 |
| 2035 | IBTQ IBTR Feb37 May38 Nov39 Nov40 Nov41 | $13,764 | $49,268 | $49,333 | $667 | leftover $667 | $17,096 | $368,734 | $361,247 | 97.3% / 102.1% | 7 / $350,000 |
| 2036 | IBTR Feb37 May38 Nov39 Nov40 Nov41 | $11,928 | $48,990 | $49,055 | $945 | leftover $854, 3r $91 | $16,925 | $328,357 | $320,648 | 97.1% / 102.4% | 6 / $300,000 |
| 2037 | Feb37 May38 Nov39 Nov40 Nov41 | $10,000 | $48,667 | $48,732 | $1,268 | 3r $1,268 | $16,464 | $286,786 | $278,845 | 96.9% / 102.8% | 5 / $250,000 |
| 2038 | May38 Nov39 Nov40 Nov41 | $6,909 | $48,572 | $49,808 | $192 | 3r $192 | $15,655 | $243,890 | $235,757 | 96.8% / 103.4% | 4 / $200,000 |
| 2039 | Nov39 Nov40 Nov41 | $5,046 | $48,262 | $49,145 | $855 | 3r $855 | $15,930 | $199,712 | $191,368 | 96.0% / 104.4% | 3 / $150,000 |
| 2040 | Nov40 Nov41 | $4,226 | $47,692 | $47,868 | $2,132 | 3r $2,132 | $15,530 | $154,227 | $145,637 | 95.2% / 105.9% | 2 / $100,000 |
| 2041 | Nov41 | $2,364 | $47,287 | $47,462 | $2,538 | 3r $2,538 | $13,804 | $107,377 | $98,534 | 95.0% / 109.0% | 1 / $50,000 |
| 2042 | cash only | $717 | $47,323 | $47,498 | $2,502 | 3r $2,502 | $11,604 | $59,102 | $50,000 | 95.0% / 118.2% | 0 / $0 |

**What the stress paths show (T9 G, G2, H; T5-G2).**
- **The ladder is shorter than the payments.** In January 2027 its duration is 7.9 years against 10.1 years for the payments (T8b). It gets cash back sooner than it pays out, so a fall in yields leaves it reinvesting at lower rates.
- **Where 3r's protection comes from** in a 2-point fall: mostly from its $10k being extra money set aside in 2028, and partly from its price rise. Its duration covers about $1.1k of the $5.6k-per-point gap at January 2028. Closing the gap fully would take about $51k of the long bond (T8b), which is not proposed. This is why $10k in the long bond beats $25k in IBTM in the coupon study (`oct19/coupon/coupon_risk_options.md:56-70`): at the same size, the long bond adds the price rise exactly when coupons earn less.
- **Without 3r** the shortfall is paid from Laura's kept money. In G2 it takes $9.7k of her $25.3k; in G, $12.9k of $16.8k; in H, all $5.3k of it, plus $7.6k from the gift. That is the case's flexibility concern (case:102-103). V5's own words, "an uncovered payment is funded from the equity Laura retains" (`oct19/drive/ips_report_live.md:28`), describe exactly this mechanism.
- **With 3r** Laura keeps more in every falling-yield path. The gift is lower (G2: $161.2k vs $170.3k), but still inside its smaller announced range.

#### T8. Funded ratio each 1 Jan if the curve were flat at 3/5/7% that day and stayed there (on-plan path to that date)
'No 3r' = the ten rungs, their matured cash in SGOV and the 2027 leftover. '3r' adds the reinvestment reserve: all of it before 2033, then the part kept after the on-plan 2033 release (about $5k). Before the payment.
| Date | No 3r @3% | No 3r @5% | No 3r @7% | 3r @3% | 3r @5% | 3r @7% |
|---|---|---|---|---|---|---|
| 2027-01-01 | 96.9% | 101.1% | 105.7% | 96.9% | 101.1% | 105.7% |
| 2028-01-02 | 97.6% | 101.2% | 105.0% | 101.0% | 104.5% | 108.1% |
| 2029-01-01 | 98.3% | 101.2% | 104.4% | 101.7% | 104.5% | 107.5% |
| 2030-01-01 | 98.8% | 101.3% | 103.8% | 102.3% | 104.6% | 106.9% |
| 2031-01-01 | 99.3% | 101.3% | 103.4% | 102.8% | 104.6% | 106.5% |
| 2032-01-01 | 99.8% | 101.4% | 103.0% | 103.3% | 104.7% | 106.0% |
| 2033-01-01 | 100.1% | 101.4% | 102.6% | 101.5% | 102.7% | 103.8% |
| 2034-01-01 | 100.5% | 101.6% | 102.7% | 102.0% | 103.1% | 104.1% |
| 2035-01-01 | 100.9% | 101.9% | 102.9% | 102.6% | 103.6% | 104.5% |
| 2036-01-01 | 101.3% | 102.3% | 103.2% | 103.3% | 104.2% | 105.1% |
| 2037-01-01 | 101.7% | 102.7% | 103.7% | 104.2% | 105.1% | 105.9% |
| 2038-01-01 | 102.5% | 103.2% | 103.8% | 105.5% | 106.1% | 106.6% |
| 2039-01-01 | 103.5% | 103.9% | 104.3% | 107.4% | 107.6% | 107.9% |
| 2040-01-01 | 105.0% | 105.3% | 105.6% | 110.2% | 110.4% | 110.6% |
| 2041-01-01 | 107.8% | 108.0% | 108.2% | 115.7% | 115.8% | 116.0% |
| 2042-01-01 | 116.2% | 116.2% | 116.2% | 132.2% | 132.2% | 132.2% |

#### T8b. Why the 3r bond works: duration of the reserve vs the payments (on-plan holdings, flat 5%)
| Date | Ladder duration (yrs) | Payments duration (yrs) | Dollar-duration gap per 1 pt (payments minus ladder, approx.) | 3r bond duration | 3r dollar duration per 1 pt | Long-bond value that would close the whole gap |
|---|---|---|---|---|---|---|
| 2027-01-01 | 7.88 | 10.09 | $6,378 | - | - | - |
| 2028-01-02 | 7.23 | 9.09 | $5,610 | 10.97 | $1,132 | $51,130 |
| 2030-01-01 | 5.83 | 7.09 | $4,144 | 9.74 | $1,112 | $42,536 |
| 2033-01-01 | 3.46 | 4.09 | $2,365 | 7.68 | $393 | $30,787 |
| 2036-01-01 | 2.32 | 2.80 | $1,319 | 5.36 | $318 | $24,614 |
| 2039-01-01 | 1.26 | 1.44 | $244 | 2.76 | $190 | $8,858 |

### 6b. How certainty can be defined (three options; the team picks one)

Each option needs one stated basis and one date. None of these is wording.

| Option | What it claims | Evidence from this file and the coupon study (19 Oct curve) | Weak point |
|---|---|---|---|
| **C1 Cash-flow matched, named residual risks** | Every payment has a US Treasury or Treasury fund maturing before it. The remaining risks are named (reinvestment, fund payout, US default/delay, a holding becoming unavailable), each with what absorbs it | T1, T4, T5, T9; cover order §2 step 7-8 | Gives no number for how much is left. A judge may ask "how certain?" |
| **C2 Funded ratio test** | On the valuation date the reserve is ≥ 100% funded at the market curve, and still ≥ 100% (with the named cover) if yields fall to 3% and stay | T8: ladder + leftover is 96.9% at 3% in January 2027 and 99.8% in January 2032. With 3r it is ≥ 101.0% at 3% on every date from January 2028. T4, 1 Jan 2033: rungs alone 99.7%, whole reserve 100.1% (no 3r) / 101.3% (3r) | Needs cover from 2028 to pass. Without 3r it fails the 3% test on every date before 2033 |
| **C3 Probability with history** | Payments short in X of 100,000 model paths and Y of 690 history windows | Agreed basis with both plan rules: option 1 about 14.5% (about 1.6%, worst about $7k, if Laura's half stays on call, D10); 3r about 0.6%, worst about $3.3k (REC §5). Study engine (19 Oct refresh, §6c): option 1 15.6% / 29.3%; 3r 0.08% / 0.32% / 0.72% marked at market, never 0.02% [consistency fix 20 Oct, row 7] | Model limits (§6d). Never quote "99%" without saying what it means (`oct19/out/Caplet_Update_19Oct2026.md:329`) |

Banned words, whatever is chosen: "guaranteed", "risk-free", "cannot miss" (`oct19/out/Caplet_Update_19Oct2026.md:329`).

### 6c. Monte Carlo and history, refreshed on the 19 Oct curve

Re-run of `oct19/coupon/scripts/coupon_options.py`, unchanged, on the 19 Oct row (100,000 paths; stock-yield correlation 0). Output: `oct20/reserve/data/mc19/coupon_options_results.json`.

| Option | Payment short (model / history) | Worst model short | 2031 bottom (median) | Gift median / 1-in-20 | Gift below bottom (model / history) | 16 Oct, for comparison |
|---|---|---|---|---|---|---|
| 1 State only (V5 as live) | 15.6% / 29.3% | $6.2k | $145k | $166.2k / $138.8k | 1.95% / 2.6% | 16.4% / 31.4%; gift below bottom 2.1% / 2.8% |
| 3r $10k Nov-2041 | **0.02% / 0.0%** (study engine, reserve at cost; never quote: marked at market 0.08% / 0.32% / 0.72%; agreed basis about 0.6%, REG D5) [consistency fix 20 Oct, row 7] | $0.6k | $135k | $163.3k / $136.7k | **0.06% / 0.4%** | 0.02% / 0.0%; 0.05% / 0.9% |
| 3b $10k in IBTM | 4.6% / n/a | $4.9k | $135k | $155.0k / $131.3k | 0.34% / n/a | 4.9% |
| 4 Dedicated rebuild | 0.0% / n/a | $0 | $145k | $165.5k / $140.7k | 0.01% / n/a | 0.0% (bottom $140k on 16 Oct) |

The 1984 absolute path with 3r: the gift is $136.2k against the $135k bottom, so it now holds (16 Oct: $131.5k, broken by $3.5k). Shortfall before cover if yields fall for good from January 2027 (coupon study ledger): 1 point $9.5k, 2 points $19.0k, 3 points $27.7k (16 Oct: $9.5k / $18.9k / $27.6k). The ranking of the options does not change.

### 6d. Assumptions (each one should appear in the Final Report)

| # | Assumption | Value used | Source / status |
|---|---|---|---|
| A1 | Purchase curve | treasury.gov par curve 19 Oct 2026, treated as 1 Jan 2027 | URL in §2; must be re-run on the real purchase date |
| A2 | Rung sizing | $50k at each holding's maturity if income earns its own yield | Number sheet and coupon study convention (`oct19/numbers/findings.md:43`); on-plan maturities check out at exactly $50,000 (independent check 6) |
| A3 | iBond funds behave like par bonds ending 15 Dec | Payout at the modelled level | UNVERIFIED by design: iShares says payouts "are not predictable" and the funds "do not seek to return any predetermined amount" (`IBTM_328944.txt:968`). Test K covers −2% |
| A4 | iBond final-year cash | Not modelled | iShares: in the final year, maturing bonds' proceeds "will be held in cash equivalents" (`IBTM_328944.txt:672`). IBTM's weighted average maturity is 5.71 years against about 6.2 years to its end (14 Oct, `:419-431` block), so about 5-6 months in cash on average. Rough size if money-market rates sit 1-2 points below the bond yields: $0.2-0.5k per $50k rung (my arithmetic, UNVERIFIED) |
| A5 | Fund fees | Not deducted from curve yields | IBTM fee 0.07%; its 30-day SEC yield (net of fees) was 5.00% on 14 Oct, against the model's 4.93-4.99% for that rung (`IBTM_328944.txt:315-317`), so leaving the fee out is not obviously optimistic. Re-check on the purchase date |
| A6 | Reinvestment of income | Same holding, at its yield (before 2033); at the flat scenario yield (after) | Drafts' rule (V4 :45, V3 :156, Tab 15 :277); absent from live V5. If coupons sit in bills: −$4.2k (test M). WInS/real unit size: §5 |
| A7 | Waiting cash | Short-term Treasury ETF at the scenario yield less 0.09% | SGOV seen on WInS 29 Sep (no screenshot); BIL, SHV unchecked (§5) [consistency fix 20 Oct, row 26]. At 0%: tests I, J |
| A8 | Rates | Flat 3/5/7% from 2033; named paths; Monte Carlo is a parallel random walk, 1.0 pt a year, floor 0.25% | Coupon study §6 limits (`oct19/coupon/coupon_risk_options.md:184-198`) |
| A9 | Stocks | VT 7.0% compound, 16.78% vol, 0.06% fee | JPM 2026 LTCMA AC World (`snap/main/CLAUDE.md` key facts) |
| A10 | Timing | All flows on 1 Jan (case:59-60); funds end 15 Dec; T-bonds 15 Feb / 15 May / 15 Nov | case; WInS holdings |
| A11 | Credit | The US Treasury pays on time | Residual risk named in V5 ("Beyond a US default", `ips_report_live.md:30`). A short delay to a 15 Nov or 15 Dec payout still lands before 1 Jan; longer is not modelled |
| A12 | No outside money for the payments | Every cover pot sits inside the portfolio | case:91-92. Banned as cover: "her other assets", co-sponsors (`oct19/out/Caplet_Update_19Oct2026.md:139, 331`) |
| A13 | Taxes, Taiwan legal costs, facility cost | Ignored | case:164-169 |
| A14 | Inflation | Payments fixed at $50k nominal (case:90); real value falls | At 2.5% a year the 2042 payment is worth about $40.0k in 2033 dollars (`oct19/frprep/final_report_prep.md:234`) |
| A15 | WInS book | Laura's plan scaled down (about 0.64-0.67). WInS holds no 3r position | `oct19/out/Caplet_Update_19Oct2026.md:270`. If 3r wins: about 8 more Nov-41 bonds, or say "about mirrors" (`oct19/coupon/coupon_risk_options.md:155-156`) |

---

## 7. Decisions this schedule exposes (options and evidence only; the team decides and words them)

| # | Decision | Options | Evidence |
|---|---|---|---|
| R1 | 3r or not (vote set B, D1, Tue 27 Oct) | 3r $10k; option 1; option 4; others in the coupon study | §6c; T5-G2; T9. Without 3r the reserve depends on Laura's kept money in any early fall in yields |
| R2 | How coupons are reinvested when a unit can't be bought | Pool and sweep into the same bond; send to the next payment via SGOV/BIL (then size for bill rates); dedicate (option 4) | Test M: −$4.2k on plan if coupons only earn bill rates |
| R3 | Which ETF holds waiting cash | SGOV; BIL; SHV; WInS cash at 0% | §5. SGOV seen on WInS 29 Sep (no screenshot); BIL, SHV unchecked [consistency fix 20 Oct, row 26]; the FAQ lists no cash as "permitted" (`faqs.txt:44-56`) |
| R4 | The 2033 3r release rule | Keep need + $5k, release the rest (coupon study); keep it all to 2042; release nothing until 2037 | On plan it releases $8.3k at 5% (T4b). A fall to 3% releases *more* ($10.5k), because the bond's price rises |
| R5 | A surplus rule after 2033 (optional) | None, with the surplus back to Laura in 2042 (assumed here); release above a stated funded ratio at each January review | T5A: the funded ratio drifts up to 108-155% by 2041-42 at 5-7%; surpluses of $8-27k |
| R6 | One definition of "Laura keeps" | All money not given (this file); half of VT (coupon study) | T3: $26.4k vs about $20.5k median; mixing them breaks consistency between deliverables |
| R7 | One certainty standard | C1 / C2 / C3 (§6b) | C2 passes at 3% only with cover from 2028 |

None of these needs a WInS trade before 6 Nov, except R1 if the team wants WInS to hold the 3r bonds (2 trades, about $35; `oct19/coupon/coupon_risk_options.md:155-156`).

---

## 8. What the Final Report must show about the reserve (one-page checklist)

Tick each item against the student draft. Use one basis and one curve date throughout, re-priced on the 6 Nov close or the date the team picks (`oct19/out/Caplet_Update_19Oct2026.md:248`).

**Case requirements (case:94-99)**
- [ ] The order on 1 Jan 2033: reserve set aside **first**, then the $50k payment, then the gift, then what Laura keeps (case:94-95).
- [ ] **Size**, stated both ways: the holdings (which fund or bond pays which year), and the value on 1 Jan 2033 at a stated yield. Give a range across at least two yields (for example T4: $384k-$440k), with the value of the payments beside it.
- [ ] **Initial composition** on 1 Jan 2033: four iBond Treasury funds (2033-36), five T-bonds (2037-41), waiting cash, and the 3r bond if voted. Give the shares (T6b) and say why each type: funds where WInS has no bond (2031-36 gap, `snap/main/COMPETITION.md:93-94`), bonds after that.
- [ ] **How it changes, "if at all"**: run-off with no trading; each year's maturity; where income goes; the 10.5-month (Feb-37) and 7.5-month (May-38) waits in a named short-term Treasury ETF; the replace-if-unavailable rule; duration falling from about 3.5 to 0.4 years; no move into stocks.
- [ ] A **run-off table** 2033-2042 (T5-style): holdings left, cash in and out, payment, any shortfall and what covered it, value, value of payments left, funded ratio.
- [ ] **Certainty defined** in one standard (§6b), with its number and its basis, and kept separate from the confidence in the 2031 range (`oct19/frprep/final_report_prep.md:227`).
- [ ] **How it was evaluated**: name the tools honestly (a deterministic ledger at flat yields, stress paths, a Monte Carlo and a history replay; that AI wrote the code; which numbers students rebuilt).
- [ ] **Assumptions** listed (§6d A1-A15), each with a source and date.

**Consistency with the IPS and TNA (TNA:30-31; strategy frozen at the IPS)**
- [ ] The IPS states where income goes (live V5 does not). The Final Report's run-off uses the same rule.
- [ ] The cover order is the same as in the IPS, including after 2033 (with 3r: leftover → 3r → set-aside; without: leftover → Laura's kept money → gift above the floor).
- [ ] The IBTR note's top-up rule (the 2028 deposit completes the ladder first) is honoured in the build-up (T3).
- [ ] The floor is outside the reserve. IBTM holds both the 2033 payment rung and the floor, and the report says which is which (the IBTM note, `snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:19`).
- [ ] The Feb-37 and May-38 notes' "short-term Treasury ETF" is named, and its WInS listing is shown by screenshot.
- [ ] No "maturing bonds, not sales, supply every payment" if any proceeds wait in an ETF, or 3r may be sold (`oct19/out/Caplet_Update_19Oct2026.md:142`).

**Stress and honesty**
- [ ] One "yields fall and stay down" test, on the stated basis, with what covers it. One "yields rise" test showing that a fall in value is not a loss when bonds are held to maturity. One fund-payout test.
- [ ] Say that the risk is front-loaded (most coupons are reinvested before 2033), so the cover has to be in place from 2028.
- [ ] Name the residual risks: US default or delay, fund payouts not fixed, iBond final-year cash, listing of the waiting ETF, inflation eroding the fixed $50k.
- [ ] No "guaranteed", "risk-free" or "cannot miss". One "99%" at most, with its meaning.
- [ ] Every number dated and rebuilt by a student (Caplet update §3c-5, `oct19/out/Caplet_Update_19Oct2026.md:100`). Charts (if allowed) answer one question each, for example "how the reserve runs off" (`oct19/frprep/final_report_prep.md:390`).
- [ ] The AI use is recorded in the Works Cited: these tables, scripts and the coupon study.

---

## 9. Files

All under `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/reserve/`:
- `scripts/reserve_schedule.py`: the ledger engine (plan rules, scenarios, valuation, cover order).
- `scripts/make_tables.py`: builds every table here.
- `scripts/indep_pricer.py` and `scripts/coupon_options.py`: copied unchanged from `oct19/coupon/scripts/`.
- `out19/tables.md`, `out19/runoff_schedules.csv` (100 run-off rows: 3 yields × 2 variants plus 2 stress paths × 2 variants), `out19/key_numbers.json`.
- `out16/`: the same tables on the 16 Oct curve, to compare with the coupon study.
- `checks/independent_checks.py`: hand re-derivations.
- `data/tsy_202610.csv`: curve fetched 19 Oct 21:41 UTC.
- `data/mc19/`: Monte Carlo refresh output.
- `web/`: iShares IBTM and SGOV and SSGA BIL page text, read 20 Oct 2026 Sydney.
