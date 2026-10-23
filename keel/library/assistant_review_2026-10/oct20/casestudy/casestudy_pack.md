# Case-study evidence pack: IBTM (main) and VT (fallback)

> **Verified 20 Oct (`oct20/verify_case/verify_case.md`): sound; apply these fixes.** (E1) IBTM's OWN SAI exists: the combined iShares Trust SAI dated 27 Feb 2026 (SEC EDGAR 485BPOS 0001193125-26-064179) lists IBTM and contains the "terminated by a majority vote of the Board" clause verbatim, plus a Board power to merge/reorganise funds without a shareholder vote - cite it as VERIFIED (the iShares-site SAI 10-31 covers no iBonds fund). (E2) STRIPS and TIPS are "NOT permitted" for both contributions in the live SMApply FAQ (changed after the 14 Oct snapshot) - cite the FAQ, not only the 6 Oct email. (E3) With the 0.07% fee the floor margin at -2 points is ~$3.4-3.5k vs $3,700: ~$0.2-0.4k spare (not $0.7k); the $145k bottom still holds by ~$1.6k. (E4) Matured 2032 notes are mostly rolled into remaining 2032 notes, then cash - "yield locked on average to ~1 Jul 2032", not a cash cliff. (E5) SGOV IS WInS-listed (team check 29 Sep). (E6) Add an intermediate Treasury ETF row (IEF/VGIT, listed): ~-$9k per 1-point rise just before the 2032 sale. (E7) "None strictly between 15 Feb 2031 and 15 Feb 2036" (the Feb-2036 bond is listed). Face per share $23.33; 1,142 shares ~$26.6k; short-ETF rates are annual-effective (5.19% annual = 5.13% s.a.); SGOV SEC yield 3.74%.


**AI-generated research (Claude Code) for Team Caplet, Tue 20 Oct 2026, about 10:05-11:30 Sydney (19 Oct 22:50-00:30 UTC). Not text to submit.** It holds facts, numbers, sources and questions. It drafts no Final Report, IPS, TNA or semifinal wording. The students choose the case-study holding and write every sentence in their own words. If they use anything here, they log it in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026).

**Labels.** VERIFIED = read today in a primary source (issuer document, treasury.gov, FDIC, official rules), with the date of the data. MODEL = a computer estimate from an AI-built script; it is not a fact. CALC = simple arithmetic on verified inputs. INFERENCE = reasoning, not confirmed by a source. UNVERIFIED = nobody has confirmed it.

**Short forms.** `oct19/`, `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`. `CS/` = this folder, `oct20/casestudy/`. `case:n` = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` line n. `TRD:n` = official trading page, `/home/user/caplet-investment/competition/official/2026_27/smapply_public_2026-10-14/trading.txt` line n (the same sentence is `oct20/tradecheck/web/trading.txt:29`). `COMP:n` = `/home/user/snap/main/COMPETITION.md`. `NOTES:n` = `/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` (the filed WInS notes, exported 14 Oct). `PORT:n` = `/home/user/snap/main/team/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv`. `REG` = `oct20/numreg/numbers_register.md` (row id). `LDI` = `oct20/ldi/ldi_second_opinion.md` (section). `PB` = `oct20/semis/semis_playbook.md`. `VPW` = `oct20/verify_pw/verify_pw.md`. `DRILL` = `oct19/drill/defence_drill.md`. `ALT` = `oct20/alternatives/alternatives.md`. `SP:n` = IBTM summary prospectus text, `CS/web/sp_ibtm.txt`. `FS:n` = IBTM fact sheet text, `CS/web/fs_ibtm.txt`. `PG:n` = live IBTM product page text, `CS/web/p_ibtm.txt`. `SAI:n` = `CS/web/sai.txt`. `TRUST:n` = trust prospectus with the 15 Oct 2026 supplement, `oct20/ldi/web/docs/prosp_ibt.txt`.

---

## 0. Summary

1. **IBTM is still the stronger case-study holding; VT is the safe fallback.** IBTM does both of Laura's jobs (the 2033 payment and the facility floor). It is about a third of the WInS book and of Laura's real plan. A judge is less likely to have seen it, and it answers the hardest question in advance: "why is a fund whose payout is not fixed your floor?" (PB §5). The students decide.
2. **The alternatives cost almost the same; what differs is what can vary.** On the 19 Oct curve, every Treasury way of turning about $117k (Jan 2028) into $150k (1 Jan 2033) costs $116.4k-$117.2k (MODEL). The real differences are three. (a) Is it allowed? The Nov-2032 note is not on WInS, STRIPS and CDs are banned, and the Feb-2036 bond is listed. (b) How much of the payout is fixed when bought? (c) What can go wrong? If rates fall 2 points for good: STRIPS/CD $0, Nov-2032 note −$1.3k, IBTM −$1.5k to −$2.5k, IBTL −$3.9k, Feb-2036 bond +$5.5k (but −$4.9k if rates rise), short Treasury ETF −$13.6k. A CD at the national average rate (1.41%, FDIC) would cost about $23k more.
3. **Prospectus facts (VERIFIED today; data dated 16 Oct).**
   - The fund ends "on or about December 15, 2032" and "does not seek to return any predetermined amount".
   - In its last six months it moves into cash. Its holdings mature, on average, about 1 Jul 2032 (5.5 months early).
   - Fee 0.07%. It holds 15 Treasury notes maturing 31 Jan to 30 Nov 2032.
   - Yields: YTM 4.94%, 30-day SEC yield 4.98%, 12-month trailing yield 4.05%.
   - Each share has about $23.34 of 2032 Treasury face value behind it (CALC from the holdings file).
   - Two powers sit with the fund's Board. The Board "may extend the termination date". The iShares Trust SAI also allows a fund to be terminated (in some cases by Board vote alone): this was read in the SAI for other iShares Trust funds (IBTM's own SAI is not linked on its page).
4. **Since the 7 Oct fill (VERIFIED prices).** IBTM 21.65 → 21.865 (+0.99%, +$968 on 4,503 shares). VT 158.83 → 157.11 (−1.08%, −$287). Both are at the 19 Oct close; Yahoo and Nasdaq agree. Neither is a reason for anything (TRD:27). The IBTM gain came from falling yields, and the same fall made Laura's real ladder dearer: about $293.5k on 6 Oct, about $297.2k on 19 Oct (basis D, REG C1).
5. **What must be in the Final Report by 4 Dec, so the case study is not "new material".**
   - The life of an IBTM share.
   - The payout drivers with their sizes.
   - The two-job split (1,142 / 3,361 shares).
   - The alternatives table.
   - The risk list with covers.
   - One dated performance line.
   - A shorter VT section.
   - The ten judge questions in §8 show where each fact is needed.

---

## 1. Why this pack, and the rule it serves

- **Past semifinal wording** (2023-24 to 2025-26): "Include a case study of one stock or ETF in your portfolio and explain how it aligns with your overall strategy" (PB:168, quoting NS26:59-60). It was "one company" before 2023-24 (VPW:72, CONFIRMED). The suggested time was about 90 seconds, and it "may span two slides" (PB:168).
- **The no-new-material rule.** From 2022-23 onward: "DO NOT introduce completely new material or you will be disqualified" (NS23-NS25). NS26 says "or your team will be disqualified". NS22 (2021-22) has no disqualification sentence; it says only "not introduce completely new material" (VPW:32, correcting an earlier "5/5" claim). The Guide adds: "you may not redesign your strategy after observing the results" (Guide:158-159, via VPW:169).
- **So:** if the rule comes back in 2026-27 (UNVERIFIED until the semifinal instructions appear), every fact in the case study must already be in the IPS or Final Report. That makes this pack a Final Report checklist, due 4 Dec.
- **Eligibility.** IBTM and VT are both ETFs. A single T-bond is "probably not" a "stock or ETF" (PB §5). That is why the T-bonds are not offered here.

---

## 2. IBTM: what it is (facts card)

All VERIFIED from iShares sources fetched 19 Oct 2026 at 22:53 UTC, with cache-busting. The product page still showed data "as of Oct 16, 2026", because the 19 Oct update had not posted.

| Fact | Value | Source |
|---|---|---|
| Name, ticker, exchange | iShares iBonds Dec 2032 Term Treasury ETF, IBTM, Nasdaq; CUSIP 46436E296 | FS key facts; PG:153 |
| Objective | "seeks to track the investment results of an index composed of U.S. Treasury bonds maturing in 2032" | SP:24 |
| Index | ICE 2032 Maturity US Treasury Index (Bloomberg ticker G32Q). Treasuries "scheduled to mature between January 1, 2032 and December 15, 2032, inclusive" | SP:97-100; PG key facts |
| Index exclusions | "Excluded from the Underlying Index are inflation-linked securities, Treasury bills and Separate Trading of Registered Interest and Principal of Securities (STRIPS)" | SP:112-114 |
| Launched | 6 Jul 2022 | PG; FS |
| Size | Net assets $593,033,061; 27,050,000 shares (16 Oct) | PG key facts |
| Fee | **0.07%** a year (management fee 0.07%, other 0.00%, acquired-fund fees 0.00%). Cost example: $7 / $23 / $40 / **$56 per $10,000 "to maturity"** at a 5% return | SP:72, SP example; FS fees |
| Distributions | Monthly; last $0.070012 a share (ex-date 1 Oct, paid 6 Oct 2026). Next ex/record date Mon 2 Nov, paid Thu 5 Nov 2026. The year-end schedule has two December dates | PG:536-; `oct20/ldi/web/docs/distsched.txt:60-61` |
| Credit | Treasuries 99.97%; cash and derivatives 0.03%. Shown as "AA Rated 99.97%" (BlackRock uses the median of S&P, Moody's and Fitch) | PG sector and credit tables (16 Oct) |
| Rates (16 Oct) | Average YTM **4.94%**; 30-day SEC yield **4.98%**; 12-month trailing yield **4.05%**; weighted average coupon 3.50; effective duration 5.02 years; weighted average maturity 5.71 years; convexity 0.30; option-adjusted spread −0.41bp | PG:272-310 |
| Risk statistics (30 Sep) | 3-year standard deviation 6.20%; 3-year equity beta 0.21 | PG:280-297 |
| Trading (16 Oct) | Close $21.93; NAV $21.92; premium 0.01%; 30-day median bid/ask spread 0.05%; volume 332,785; 30-day average volume 283,407 | PG key facts |
| Premium/discount record | Days at premium / at NAV / at discount: 2025: 197 / 14 / 39. 2026: Q1 55 / 4 / 2; Q2 57 / 0 / 5; Q3 49 / 9 / 6 | PG:504-527 |
| Managers | BlackRock Fund Advisors; representative sampling; turnover 70% in the last fiscal year | SP:91, :179; SP p.7 |

**What this teaches.** A term ETF is a bond fund with an end date. It holds bonds that all mature in one year, then winds up and hands out the cash. Laura gets a bond-like end date without having to buy 15 separate notes.

---

## 3. How a term ETF works (the life of an IBTM share)

### 3a. Prospectus and issuer quotes (VERIFIED, verbatim)

| Topic | Quote | Source |
|---|---|---|
| Termination | "The Fund is a term fund that will terminate on or about December 15, 2032, at which time it will distribute its remaining net assets to shareholders pursuant to a plan of liquidation." | SP:101-104 |
| No fixed payout | "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions." | SP:104-106 |
| No fixed payout (issuer disclosure) | "Unlike a direct investment in a bond that has a level coupon payment and a fixed payment at maturity, the Fund(s) will make distributions of income that vary over time." "The Funds' distributions and liquidation proceeds are not predictable at the time of investment and the Funds do not seek to return any predetermined amount." | FS:163-172; PG:805-806 |
| Final-year cash | "In the last six months of operation, as the bonds held by the Fund mature, the proceeds will typically be reinvested by the Fund in investments already in the Underlying Index but may also be invested in other cash and cash equivalents as determined by BFA." | SP:151-156 |
| End state | "By December 15, 2032, the Fund is expected to consist almost entirely of cash. On or around this date, the Fund will wind up and terminate." | SP:159-161 |
| Declining yield | "Declining Yield Risk. In the months leading up to the Fund's planned termination date, the Fund's yield may move toward prevailing money market rates and may be lower than the yields of the bonds previously held by the Fund and lower than prevailing yields for bonds in the market." | SP:294-298 |
| YTM vs realised yield | "During the final year of the fund's life, the underlying bonds will mature and the proceeds will be held in cash equivalents until the liquidation of the fund. The investor's total realized yield to fund maturity will be influenced by the yield earned on these proceeds during the final year." | PG:636 |
| Index cash | "Cash flows from bond payments that are received during the month are retained in the Underlying Index until the end of the month ... Cash does not earn any reinvestment income while it is held in the Underlying Index." | SP:131-140 |
| Date can move | "The Board may extend the termination date if a majority of the Board determines the extension to be in the best interest of the Fund." | SP:166-168 |
| Early termination power (Trust level) | "The Trust or a fund may be terminated by a majority vote of the Board, subject to the affirmative vote of a majority of the shareholders of the Trust or such fund entitled to vote on termination; however, in certain circumstances described in the Declaration of Trust, only a majority vote of the Board is required." | SAI:7574-7576 (iShares Trust SAI dated 27 Feb 2026, for other iShares Trust bond funds such as GOVT and TIP). IBTM's own SAI was not found; its page does not link one. Same Trust, so probably the same clause (INFERENCE) |
| Objective can change | "Each Fund's investment objective and its Underlying Index may be changed without shareholder approval" | TRUST p.101 (via LDI §3b) |
| Treasury risk | "Although U.S. Treasury obligations are backed by the full faith and credit of the United States, circumstances could arise that could prevent the timely payment of interest or principal." | SP:221-224 |
| Payout sequence (precedent: IBTG, Dec 2026 fund) | Last trading day 15 Dec; trading suspended from 16 Dec; proceeds "scheduled to be sent to shareholders on December 18, 2026"; "we cannot assure you that there will be a trading market" 16-18 Dec; final NAV "will include any costs associated with the liquidation"; proceeds arrive "subject to their brokerage firm's processes" | TRUST:24-43 (supplement dated 15 Oct 2026) |

### 3b. Holdings (VERIFIED, iShares holdings file "as of Oct 16, 2026", `CS/web/hold_ibtm.csv`; parsed by `CS/scripts/holdings.py` → `CS/data/holdings_ibtm_16oct.txt`)

| Matures | Coupon | Price | YTM | Weight | Cumulative |
|---|---|---|---|---|---|
| 31 Jan 2032 | 4.375% | 97.48 | 4.92 | 5.02% | 5.0% |
| **15 Feb 2032** | **1.875%** | **85.84** | 4.93 | 10.82% | 15.8% |
| 29 Feb 2032 | 4.125% | 96.28 | 4.92 | 5.10% | 20.9% |
| 31 Mar 2032 | 4.125% | 96.23 | 4.92 | 5.08% | 26.0% |
| 30 Apr 2032 | 4.000% | 95.56 | 4.92 | 5.13% | 31.2% |
| **15 May 2032** | **2.875%** | **90.05** | 4.94 | 11.13% | 42.3% |
| 31 May 2032 | 4.125% | 96.09 | 4.93 | 5.17% | 47.5% |
| 30 Jun 2032 | 4.000% | 95.41 | 4.93 | 5.12% | **52.6%** |
| 31 Jul 2032 | 4.000% | 95.32 | 4.94 | 5.09% | 57.7% |
| **15 Aug 2032** | **2.750%** | **89.01** | 4.94 | 10.47% | 68.1% |
| 31 Aug 2032 | 3.875% | 94.62 | 4.94 | 5.04% | 73.2% |
| 30 Sep 2032 | 3.875% | 94.53 | 4.95 | 5.02% | 78.2% |
| 31 Oct 2032 | 3.750% | 93.81 | 4.95 | 5.06% | 83.3% |
| **15 Nov 2032** | **4.125%** | 95.71 | 4.95 | 11.63% | 94.9% |
| 30 Nov 2032 | 3.750% | 93.71 | 4.95 | 5.10% | 100.0% |
| Money market fund + cash | – | – | 3.83 | 0.03% | |

CALC from the same file:
- **Average maturity date about 1 Jul 2032, 5.5 months before 15 Dec 2032.** About 53% of the fund matures by 30 Jun 2032, so that money waits as cash for the second half of 2032. LDI §3a gives 5.4 months from the WAM; the two agree.
- **Face value behind each share: about $23.34**: $631.3m of par ÷ 27.05m shares. The price is $21.92, because the low-coupon notes trade below par (85.84-90.05). The gap is the "pull to par": return that comes as price growth, not as payouts.
- Coupon cash on the current holdings is about $0.82 a share a year (about $0.068 a month). Recent payouts were $0.069-$0.076 a month (Yahoo, last 12 months). That they are close is a sanity check, not an exact match (the reason for the small gap is UNVERIFIED).
- **Trap:** an older team file says the fund holds "15 notes, Apr-Sep 2032". The holdings run **Jan to Nov 2032** (DRILL §2b). Quote the file of the day.

### 3c. The four "yields" (what each means; 16 Oct values)

| Yield | Value | What it measures | Use it for | Source |
|---|---|---|---|---|
| Average yield to maturity | 4.94% | Weighted YTM of the bonds, before the fee and before the cash phase | The best single guide to what the bonds earn if held to their maturities | PG:300-303, :636 |
| Estimated Net Acquisition (ENA) yield | about 4.87% at NAV (CALC: 4.94 − 0.07) | The issuer's calculator: YTM at your purchase price, minus the 7bp fee | The closest to "what I lock in if I buy today". The calculator itself was not run (needs the page script) | PG:632-634 |
| 30-day SEC yield | 4.98% | Standard SEC formula: income earned over the last 30 days, after expenses | Comparing funds. It sits above the YTM probably because yields were higher earlier in the 30-day window (7 Oct 7-year 5.15% vs 16 Oct 4.98%) (INFERENCE) | PG:272-275; FS glossary |
| 12-month trailing (distribution) yield | 4.05% | Payouts over the last 12 months ÷ price ($0.887 ÷ $21.92, CALC; Yahoo payouts) | **Not** the return. It leaves out the pull to par | PG:276-279 |
| Latest payout, annualised | 3.83% (CALC: 0.070012 × 12 ÷ 21.93) | One month's payout × 12 | Nothing; it moves month to month | PG distributions |

**Trap:** "IBTM yields 4%" (the payout yield) and "IBTM yields 5%" (the YTM) are both heard. Only the YTM-type figure links to the floor maths, and the plan's own figure is the forward yield in January 2028: **5.12% on the 19 Oct curve** (REG E1, MODEL).

### 3d. The life of one share (timeline to say aloud; facts only)

1. **Jan 2027:** Laura's first deposit buys IBTM for the 2033 payment. In WInS the payment holding was bought on 7 Oct 2026.
2. **Jan 2028:** the second deposit first tops up any ladder gap, then buys more IBTM as the floor (COMP §7).
3. **2028-2031:** the fund holds 2032 notes and pays monthly income, which Laura's plan must reinvest (LDI §6a). Its price still moves with rates, but less each year (§6, row R1).
4. **Jan-Nov 2032:** the notes mature (about half by 30 Jun). The cash is reinvested in the remaining index notes or in cash equivalents (SP:151-156).
5. **About 15 Dec 2032:** last trading day; the fund terminates. Proceeds about 18 Dec, on the IBTG precedent (TRUST:24-43).
6. **1 Jan 2033:** first $50,000 payment. The gap is about 14-17 days (17 from the termination date, about 14 from the precedent's payout date). Where the cash waits must be stated (LDI §9 T5 says a named short-term Treasury fund).
7. **Then the 2033 gift:** floor + half of VT, capped at the announced top (COMP §7, item 4).

---

## 4. Why Caplet holds it

### 4a. The filed WInS note (VERIFIED, verbatim; 6 Oct 2026, 10:01:41 PM ET, 292 characters, REG A9)

> "Future funding and risk management: IBTM does two jobs in Laura's plan. It supports her first $50,000 payment and provides a floor for her facility contribution, giving co-sponsors a minimum figure in 2031. It holds 2032 Treasuries, so the timing fits, although the final payout is not fixed." (NOTES:19)

- The team marks it as a suggested TNA pick (NOTES:26-28). If it is chosen, the TNA reflection also becomes "existing material" that the case study must not contradict (PB:162).
- Notes cannot be edited (COMP §4).

### 4b. The two jobs, in numbers

| | WInS (scaled book) | Laura's real plan (19 Oct curve, MODEL) |
|---|---|---|
| Job 1: the 1 Jan 2033 payment | **1,142 shares**, "set aside first: the payment comes before the facility" (PORT:38) | About **$37.1k** on 1 Jan 2027 buys IBTM expected to return $50,000 (CS/data/extra_19oct.txt; forward method of REG E1) |
| Job 2: the facility floor | **3,361 shares**; "Income from these shares stays with the floor" (PORT:39) | About **$116,485** on 1 Jan 2028 buys IBTM expected to return about $150,000 by Dec 2032 at a forward yield of 5.12% (REG E1). The 2031 bottom = (floor money − $3,700) rounded down to $5k = **$145k**, while the ladder fits (REG F1) |
| Total | **4,503 shares**, filled at $21.65 on 7 Oct (COMP §8). About 32.45% of the 19 Oct book (REG H3) | About a third of all her money. The payment and the floor share **one payout date** (LDI §3b, §7) |
| Face value behind it | About $105.1k of 2032 Treasuries (1,142 shares ≈ $26.7k; 3,361 ≈ $78.4k) (CALC: shares × $23.34) | – |

### 4c. Why IBTM rather than something else (the chain of constraints, with sources)

1. The payments and the gift are fixed dollar amounts, due 1 Jan 2033 (case:88-92, 109-120).
2. Since the 6 Oct email, Laura's real plan may use only "eligible stocks, ETFs and Treasury bonds available on WInS" (COMP:87-90). So STRIPS, single zero-coupon bonds, bills and CDs are out.
3. WInS lists 43 US T-bonds, **none maturing Feb 2031 to Feb 2036** (COMP:93; team check, SEEN 29 Sep; not re-checked by this agent, UNVERIFIED today). So no single 2032 Treasury can be bought.
4. IBTM is the WInS-listed Treasury holding that ends closest before 1 Jan 2033. Its credit is US Treasury only (99.97%), and its price risk shrinks to near zero by late 2032.
5. Its payout is not fixed (SP:104-106), so the range's bottom is rounded down with a $3,700 margin (REG F1). That margin covers the floor's own reinvestment and cash-phase risk at −2 points, with about $0.7k to spare (LDI §7).
- **Trap:** IBTN on WInS is INSCORP Inc, not an iBond. There is no 2033 IBTN (COMP:94).

---

## 5. Alternatives considered (19 Oct curve; MODEL)

**Method** (`CS/scripts/alts.py` → `CS/data/alts_19oct.txt`):
- The curve is the treasury.gov par curve of **19 Oct 2026** (1y 4.50, 2y 4.77, 5y 4.94, 7y 5.04, 10y 5.15), fetched 19 Oct 22:5x UTC: `CS/data/tsy_202610.csv`.
- Each instrument is priced forward to its purchase date. Income is reinvested at the instrument's own yield. Money that arrives before 1 Jan 2033 waits at 0%.
- On this convention IBTM costs $116.7k. The register's $116,485 (E1) lets the money earn its yield for the last 17 days too. The comparison between rows is what matters.
- "−2 / +2 points" = all reinvestment and roll rates move 2 points for good, right after purchase. For the Feb-2036 bond, the sale yield moves too.

### 5a. Job 2, the floor (buy 1 Jan 2028, $150,000 by 1 Jan 2033)

| Option | Allowed for Laura's plan? | Cost Jan 2028 | Fixed cash at purchase (principal + coupons) | Delivered if rates −2 for good | If +2 | What can go wrong |
|---|---|---|---|---|---|---|
| **IBTM** (as in the register: a par bond to 15 Dec 2032, no fee) | **Yes** (held) | **$116.7k** (register $116,485) | about 98% | $148.5k (−$1.5k) | $151.6k | Reinvestment of payouts; payout not fixed; termination date |
| **IBTM, realistic** (bonds mature about 1 Jul 2032; 5.5 months of cash at the forward bill rate 5.40%; 0.07% fee) | Yes | $117.2k | – | **$147.5k (−$2.5k)** | $152.6k | Adds the cash-phase risk. The −2 loss is about $1k larger than the simple model's |
| 4.125% Treasury note 15 Nov 2032 (CUSIP 91282CFV8; IBTM's biggest holding, 11.63%) | **No: not listed on WInS** (COMP:93) | $117.1k | about 98% | $148.7k (−$1.3k) | $151.4k | Coupon reinvestment; 47 days of cash before 1 Jan |
| Treasury STRIPS (zero coupon), 15 Nov 2032 | **No: banned** since the 6 Oct email (COMP:87-90); STRIPS are also excluded from IBTM's own index (SP:112-114) | $117.2k (zero rate 5.12%) | 100% | $150.0k | $150.0k | Nothing until maturity, except selling early. This is the "perfect" match the rules took away |
| Bank CD to 1 Jan 2033 at the **national average 60-month rate, 1.41%** | **No: not a WInS security** | **$139.9k (+$23k)** | 100% | $150.0k | $150.0k | Bank credit beyond the FDIC's "$250,000 per depositor, per ownership category at each FDIC-insured bank"; early-withdrawal penalty (terms UNVERIFIED) |
| Bank CD at a rate equal to the Treasury zero rate (hypothetical best CD) | No | $116.8k | 100% | $150.0k | $150.0k | Whether such CDs exist for $117k is UNVERIFIED |
| 4.500% Treasury bond 15 Feb 2036, sold 15 Dec 2032 | **Listed on WInS** (stale WInS price on 29 Sep, COMP:95) | $116.7k (forward yield 5.23%) | – | $155.5k (+$5.5k) | **$145.1k (−$4.9k)** | Reinvestment risk is swapped for **price risk at the sale**: if only the sale yield is 1 point higher, it delivers $146.7k (−$3.3k). The team's own sheet called this bond the "strongest challenge" to IBTR (`trading_notes.csv:9`), not to IBTM |
| Short Treasury ETF (e.g. SGOV, 0-3 months, fee 0.09%) rolled to Dec 2032 | Listing on WInS UNVERIFIED (any listed ETF is allowed, COMP §4) | $117.2k, **if** bills average the forward rate of 5.19% | **0%** | **$136.4k (−$13.6k)** | $164.7k | Nothing is locked in. At today's 6-month bill (4.37%) held flat: $144.3k; at 3%: $135.1k |
| IBTL (Dec 2031 iBond), then about 12.5 months in cash | Listed on WInS (COMP:94) | $116.4k | – | $146.1k (−$3.9k) | $154.0k | A whole year of cash-rate risk |

### 5b. Job 1, the 2033 payment (buy 1 Jan 2027, $50,000 by 1 Jan 2033)

| Option | Cost Jan 2027 | If −2 | If +2 |
|---|---|---|---|
| IBTM (register method) | $37.2k (extra script: $37,112 when the 17 days earn interest) | $49.3k | $50.8k |
| IBTM realistic | $37.3k | $49.0k | $51.1k |
| Nov-2032 note (not on WInS) | $37.3k | $49.4k | $50.7k |
| STRIPS (banned) | $37.3k | $50.0k | $50.0k |
| CD at 1.41% (not allowed) | **$46.0k (+$8.8k)** | $50.0k | $50.0k |
| Feb-2036 bond, sold Dec 2032 | $37.2k | $51.5k | $48.7k |
| Short Treasury ETF | $37.4k | $44.6k | $55.9k |
| IBTL then cash | $37.1k | $48.5k | $51.5k |

### 5c. What the table shows (notes, not wording)

- **Price is not the reason. Allowed or not, and what can vary, are the reasons.** All the Treasury options are priced off one curve, so they cost within about $0.8k of each other (MODEL; real market prices differ a little: iBond premium, STRIPS richness; UNVERIFIED).
- **IBTM is the best allowed option for both jobs.** It loses less in a rate fall than IBTL or a short Treasury ETF, and it has no price risk at a forced 2032 sale, unlike the Feb-2036 bond.
- **What IBTM gives up against a single note:** 1-2% of the payout is not fixed (payouts must be reinvested, plus the cash phase). This is why the bottom of the range is rounded down.
- **CDs are not a near miss.** They are not allowed, and at the national average rate they would cost $23k more for the floor. Best-market CD rates are UNVERIFIED. The FDIC rate table is "as of October 19, 2026", built on data from the last business day of September.
- **The STRIPS row is the honest benchmark.** It is the zero-risk version the 6 Oct email took away. IBTM's −$1.5k to −$2.5k at −2 points is the cost of that rule.

**What this teaches.** When bonds are priced off the same curve, the cheaper option is usually not the better one. The question is which risk you are left holding.

---

## 6. Risks (each with its size, its cover and its source)

| # | Risk | Mechanism | Size (MODEL unless stated) | Cover in the plan | Source |
|---|---|---|---|---|---|
| R1 | **Rate risk before maturity** | The price falls when yields rise. It matters only if sold early (or for WInS marks) | 1-point rise: today −5.0% (about −$4.9k on the WInS position; DV01 about $49/bp); in Jan 2028 −4.2%; Jan 2030 −2.7%; Jan 2031 −1.8%; Jan 2032 −0.9% | Hold to the end; no planned sale | CS/data/extra_19oct.txt; PG duration 5.02 |
| R2 | **Purchase-price risk** (Laura's real plan) | Falling yields before Jan 2028 make the floor dearer | The $150k target costs $119.4k at −50bp and $122.3k at −100bp (vs $116.5k). Through the ladder top-up, a half-point fall before Jan 2027 cuts the floor to about $138k (REG E2) | 2028 deposit tops up the ladder first; the range is set from what is owned | REG E1-E2 |
| R3 | **Reinvestment of distributions** | Monthly payouts must be reinvested at future rates | Floor: −$821 / −$1,622 / −$2,404 / −$3,166 at −1 / −2 / −3 / −4 points for good (REG E3: $149,179 … $146,834). Payment rung: −$0.7k at −2 | The $3,700 margin; "income stays with the floor" (PORT:39). **V5 has no reinvestment rule** (LDI §6a) | REG E3; LDI §6-7 |
| R4 | **Final-year cash yield** | About 53% of the fund is cash by July 2032; the yield drifts to money-market rates | About 5.5 months on about $150k: −$1.4k if bill rates are 2 points lower (LDI §7). The realistic model adds about −$1k at −2 over the simple one (§5a) | Inside the $3,700 margin with the reinvestment risk (about $3.0k against $3.7k, LDI §7) | SP:151-161, :294-298; PG:636 |
| R5 | **No predetermined payout** | Fund design: income varies, the end value is not promised | All of R3 + R4 + fees + costs in the final NAV ("will include any costs associated with the liquidation", TRUST:24-43) | Bottom rounded down; never "$150k owned" (REG E1 rule) | SP:104-106; FS:163-172 |
| R6 | **Termination date change or early closure** | The Board may extend the date (SP:166-168). The Trust can terminate a fund, sometimes by Board vote alone (SAI:7574-7576, another fund family's SAI). The objective or index can change without a shareholder vote (TRUST p.101) | No size. Assets $593m in Oct 2026, up from $546.8m on 30 Jun (FS), so a small-fund closure looks unlikely (INFERENCE) | V5's substitution rule (an earlier-maturing Treasury). LDI §9 T3 trigger: if the date or payout timing changes, sell on the exchange before the last trading day (spread about 0.05%) | LDI §3b, §9 |
| R7 | **Payout timing** | Proceeds about 3 days after the last trading day, "subject to their brokerage firm's processes"; no trading market from 16 to 18 Dec | About 14 days of slack before 1 Jan, on the 2026 precedent | Know the date; name where the cash waits (LDI §9 T5) | TRUST:24-43 |
| R8 | **Tracking** | Representative sampling, fees, index cash earning nothing | 1-year NAV −2.28% vs index −2.23% (to 30 Sep 2026); since inception 0.39% vs 0.43% a year: about −0.05 points a year, roughly the fee | None needed | PG performance table |
| R9 | **Liquidity, spreads and premium** | ETF price vs NAV; after-hours quotes are wide | Premium 0.01%, median spread 0.05% (16 Oct). **After hours on 19 Oct (6:56 PM ET) Nasdaq showed bid $19.16 / ask $24.31**. Laura's real orders: about 1,700 shares (2027) and about 5,300 (2028) at today's price, against 283k shares of average daily volume | Limit orders in US market hours only (COMP:100; LDI §9 T4) | PG; `CS/data/nasdaqinfo_IBTM.json`; CALC |
| R10 | **Concentration** | One fund carries two jobs and one payout date; one sponsor runs all five iBond funds | IBTM about 32% of the WInS book; iBond ETFs 61.3%; Treasuries about 90% (REG H3). In Laura's plan, about a third of her money depends on one December payout | US Treasury credit only; T3 trigger. The IBTM split puts the payment first (PORT:38) | REG H3; LDI §3b |
| R11 | **US Treasury itself** | Delay or default; ratings shown as "AA" | Not sized. The prospectus names "timely payment" risk | Named as the residual risk (LDI §11) | SP:221-224; PG credit table |
| R12 | **WInS-only quirks** | WInS shows the iBond ETFs as "Long Equities"; WInS pays 0% on cash, so WInS payouts sit idle | Label: 61.6% "Long Equities" on the WInS pie (COMP:98). Next payout about $315 (4,503 × $0.070012; ex 2 Nov, paid 5 Nov), if WInS credits it (UNVERIFIED) | Explain the label once in the Final Report. No reinvestment trade: $25 commission (LDI §13) | COMP §4, §8 |

---

## 7. Performance since the fill (VERIFIED prices; P&L is CALC)

| | IBTM | VT |
|---|---|---|
| Order placed (ET) | 6 Oct 10:01:41 PM, so it filled at the next open (TRD: orders placed while the market is closed fill at the opening price) | 7 Oct 8:27:19 PM, filled at the next open |
| Fill | **$21.65** × 4,503 = $97,489.95 (+$25 commission). The open of 7 Oct, 0.37% below that day's close of $21.73 | **$158.83** × 167 = $26,524.61. The open of 8 Oct (close $158.73) |
| 16 Oct close | $21.925 (Nasdaq and Yahoo); NAV $21.92 (iShares) | $156.82 |
| **19 Oct close** | **$21.865** (Yahoo; Nasdaq "Closed at Oct 19, 2026 4:00 PM ET" $21.865) | **$157.11** (Yahoo) / $157.12 (Nasdaq) |
| Change since fill | **+$968 (+0.99%)**; no payout yet (ex-date 1 Oct came before the fill) | **−$287 (−1.08%)**; no dividend yet (next quarterly ex-date is probably mid-December, after the 6 Nov freeze; INFERENCE from the Yahoo dates 19 Dec 2025, 20 Mar, 18 Jun, 18 Sep 2026) |
| Why | Yields fell: the 5-year from 5.03% (7 Oct) to 4.94% (19 Oct), the 7-year from 5.15% to 5.04%. Duration 5.0 × about 0.1 point is about +0.5%, plus about two weeks of accrual. From the 7 Oct close it is +0.62%; the rest is the good fill at the open | World stocks fell slightly (one week's noise) |
| 1-year context | Price $23.34 → $21.865 (Yahoo; yields rose over the year); NAV total return to 30 Sep 2026: 1 year −2.28%, 3 years 3.59% a year; year to date to 16 Oct −2.12% | Price $139.45 → $157.11; realised daily volatility about 13.9% a year (CALC, Yahoo) against 16.78% assumed (JPM 2026) |

Sources: `CS/data/yahoo/*.json`, `CS/data/yahoo_prices.txt`, `CS/data/nasdaq_IBTM.json`, `nasdaq_VT.json`, `nasdaqinfo_*.json` (all fetched 19 Oct 22:5x-23:1x UTC); iShares PG performance table. The register agrees: WInS clean P&L +$3,211 in total, with VT −$287 the only loser (REG H2).

**How to use it (rule, not wording).**
- "WInS gains and losses should not be added to or subtracted from the client's long-term portfolio projections" (TRD:27).
- A WInS bond gain is **not good news for Laura**. The same fall in yields made her real ladder dearer: basis D cost about $293.5k on 6 Oct and $297,162 on 19 Oct, leaving $2,838 of room (REG C1).
- If one performance line is used, date it, give the basis, and say what it means for the plan (nothing, for a held-to-end holding).

---

## 8. What a judge would ask (10 for IBTM)

Each row gives the facts needed and the trap. Tags follow DRILL: F = fixed-income judge, P = portfolio manager, Y = youth/generalist.

| # | Question | Facts needed (where) | Trap |
|---|---|---|---|
| Q1 [P] | "In 90 seconds: what is IBTM, why do you own it, what can go wrong?" | §2 card; §4b two jobs; §6 R3-R6 sizes | More than one number per slide (PB §5); saying "guaranteed" or "risk-free" (COMP §7 wording rules) |
| Q2 [F] | "Why not just buy the 15 Nov 2032 note?" | WInS lists none from Feb 2031 to Feb 2036 (COMP:93); 6 Oct email; §5a row (it would save only about $0.2k of rate-fall risk, and it is IBTM's largest holding anyway) | Claiming the note is "worse". It is better on fixed payout, just not available |
| Q3 [F] | "Your payout isn't fixed. How can a fund be a floor?" (killer question K3) | SP:104-106 quote; R3+R4 sizes (about $3.0k at −2); $3,700 margin and rounding down (REG F1; LDI §7) | Quoting "$150,000" as owned (REG E1); forgetting the cash phase |
| Q4 [F] | "Why is the payout yield 4.05% when the YTM is 4.94%?" | §3c table; low-coupon notes at 85.84-90.05; pull to par; about $23.34 of face per share | Using the 4.05% as the return, or 4.94% as a net figure (it is before the fee) |
| Q5 [F] | "What does the fund do in 2032, and what if money-market rates collapse?" | §3b: 53% matures by 30 Jun; SP:151-161, :294-298; R4 = −$1.4k at −2 on bills | Saying the yield is locked to 15 Dec. It is locked only to about 1 Jul 2032 (LDI §3b) |
| Q6 [Y] | "IBTM ends on 15 Dec, the payment is 1 Jan. Where is the money for those two weeks, and what if the fund is late?" | Precedent: proceeds about 18 Dec, "subject to their brokerage firm's processes" (TRUST:24-43); "may extend" (SP:166-168); T3/T5 triggers | "17 days" vs "about 14 days": say which date each counts from |
| Q7 [P] | "One holding, two jobs: if the payout comes in 2% low, which job loses?" | Payment shares first: 1,142 / 3,361 (PORT:38-39); the floor absorbs it; the bottom is rounded down | Double counting the same shares for both jobs |
| Q8 [P] | "Isn't a fund riskier than the bonds? What could go wrong with the fund itself?" | R6-R10: Board powers (SP:166-168; SAI:7574-7576); tracking −0.05 points a year; premium 0.01%; $593m in assets; one sponsor for 61% of WInS | Calling the SAI clause IBTM's own. It was read in a sister SAI (UNVERIFIED for IBTM) |
| Q9 [Y] | "IBTM is up about 1% since you bought it. Good call?" | §7: WInS P&L is not counted (TRD:27); the same yield fall made Laura's ladder about $3.7k dearer (REG C1) | Celebrating a gain; mixing WInS and plan figures |
| Q10 [F/P] | "What alternatives did you reject, and with what numbers?" | §5a table (same cost; different risk; allowed or not); CD +$23k; short ETF −$13.6k at −2; Feb-2036 −$4.9k at +2 | Citing STRIPS as an option (banned since 6 Oct); claiming any undated price |

**Also likely** (from DRILL C1-C10, PB W5):
- "Why IBTM and not VT for the case study?" (S1). The answer is the decision-log reason, which is not yet recorded.
- "WInS calls it 'Long Equities': is it a stock?" (C10).

---

## 9. One-page data table (IBTM)

| Item | Value | Date | Label | Source |
|---|---|---|---|---|
| Ticker / CUSIP / exchange | IBTM / 46436E296 / Nasdaq | – | VERIFIED | FS; PG |
| Index | ICE 2032 Maturity US Treasury Index (G32Q) | – | VERIFIED | PG; SP:97-100 |
| Terminates | "on or about December 15, 2032" | Prospectus 27 Feb 2026 | VERIFIED | SP:101-104 |
| Fee | 0.07% ($56 per $10k to maturity) | Prospectus | VERIFIED | SP:72 |
| Net assets / shares | $593.0m / 27.05m | 16 Oct | VERIFIED | PG |
| Holdings | 15 Treasury notes, 31 Jan-30 Nov 2032; 0.03% cash | 16 Oct | VERIFIED | holdings CSV |
| Average maturity | 5.71 years (about 1 Jul 2032; 5.5 months before termination) | 16 Oct | VERIFIED / CALC | PG; CS/data/holdings_ibtm_16oct.txt |
| Share maturing by 30 Jun 2032 | 52.6% | 16 Oct | CALC | holdings CSV |
| Face value per share | about $23.34 | 16 Oct | CALC | holdings CSV |
| YTM / SEC / 12m trailing | 4.94% / 4.98% / 4.05% | 16 Oct | VERIFIED | PG |
| Effective duration / coupon | 5.02 years / 3.50% | 16 Oct | VERIFIED | PG |
| Premium / median spread | 0.01% / 0.05% | 16 Oct | VERIFIED | PG |
| 30-day average volume | 283,407 shares | 16 Oct | VERIFIED | PG |
| Last payout / next | $0.070012 (ex 1 Oct, paid 6 Oct) / ex 2 Nov, paid 5 Nov | 2026 | VERIFIED | PG; distsched |
| Tracking (1 year to 30 Sep) | NAV −2.28% vs index −2.23% | 30 Sep | VERIFIED | PG |
| WInS position | 4,503 shares at $21.65 (7 Oct); 1,142 payment / 3,361 floor | 7 Oct | VERIFIED (team records) | COMP §8; PORT:38-39 |
| WInS value / change | $98,458 / +$968 (+0.99%) | 19 Oct close $21.865 | CALC | Yahoo; Nasdaq |
| WInS weight | 32.45% of the book | 19 Oct | MODEL | REG H3 |
| Floor cost (Laura's plan) | $116,485 in Jan 2028 → about $150k; forward yield 5.12% | 19 Oct curve | MODEL | REG E1 |
| 2033 payment rung (Laura's plan) | about $37.1k in Jan 2027 → $50k | 19 Oct curve | MODEL | CS/data/extra_19oct.txt |
| 2031 bottom rule | (floor money − $3,700) rounded down to $5k = $145k | 19 Oct | MODEL (rule = team choice) | REG F1 |
| Floor if reinvestment −2 for good | $148,378 (−$1.6k); about $147.5k with the cash phase | 19 Oct curve | MODEL | REG E3; §5a |
| Floor if yields −0.5 before Jan 2027 | about $138k | 19 Oct curve | MODEL | REG E2 |
| Price change per 1-point rise | −5.0% now; −4.2% in Jan 2028; −1.8% in Jan 2031 | 19 Oct | MODEL | CS/data/extra_19oct.txt |
| Best allowed alternative | None that is better: Nov-2032 note not listed; STRIPS/CD banned; IBTL −$3.9k and short ETF −$13.6k at −2; Feb-2036 −$4.9k at +2 | 19 Oct curve | MODEL | §5a |

---

## 10. VT in brief (the fallback case study)

### 10a. Facts (VERIFIED: Vanguard fact sheet "As of June 30, 2026", `CS/web/vt_F3141.txt`, fetched 19 Oct 2026; the Vanguard web pages need JavaScript and could not be read)

| Fact | Value |
|---|---|
| Name / ticker / exchange | Vanguard Total World Stock ETF / VT / NYSE Arca; CUSIP 922042742 |
| Index | FTSE Global All Cap Index: "large-, mid- and small-capitalization stocks"; "more than 98% of the global investable market capitalization" |
| Holdings | **10,048 stocks** (index 10,138) |
| Fee | **0.06%** (peer average 0.84%, Lipper, 31 Dec 2025) |
| Size | ETF share class $77.6bn; whole fund $97.0bn |
| Dividends | Quarterly. Last 12 months: $1.115 (19 Dec 2025), $0.327, $0.563, $0.408 (18 Sep 2026) = $2.41, about 1.5% of the 19 Oct price (Yahoo; CALC) |
| Countries (% of stocks) | US 61.9, Japan 5.9, **Taiwan 3.5**, UK 3.1, Canada 2.9, Korea 2.8, China 2.6 |
| Top 10 | 21.7% of assets; NVIDIA 4.0, Apple 3.6, Alphabet 3.2, Microsoft 2.4, Amazon 2.0, **TSMC 1.7** |
| Sectors | Technology 33.3%, Financials 14.6%, Industrials 13.4% |
| Returns (NAV, to 30 Jun 2026) | 1 year 24.28%; 5 years 10.89% a year; 10 years 12.82% a year; since 2008 8.87% a year |

The WInS note's "about 10,000 stocks at a 0.06% fee" checks out against the primary source.

### 10b. Why Caplet holds it (filed note, VERIFIED verbatim; 7 Oct 2026, 8:27:19 PM ET)

> "Growth: Vanguard Total World Stock ETF holds about 10,000 stocks at a 0.06% fee, so one cheap fund diversifies Laura's stocks. They only set how far her gift rises above her promised minimum. A fall can shrink the extra, and a rise before 2031 lifts the top of the range co-sponsors hear." (NOTES:14)

- **Size:**
  - WInS: 167 shares at $158.83 = $26,525; 8.84% at cost, 8.65% of the 19 Oct book (REG H4).
  - Laura's plan: about $33.5k in Jan 2028, about 7% of her money (REG E6, H4). Never swap the two.
- **Open decision:** the note gives VT one job ("only set how far her gift rises"). IPS V5 also makes "retained equity" the payment backstop (LDI §1, §8; DRILL E10, K5). The case study must match whichever job list is voted (D0-1/D2).

### 10c. Alternatives (MODEL figures from ALT §3, 19 Oct curve, 100,000 paths. ALT's base plan includes the 3r reserve, which is not yet voted)

| Option | Effect | Source |
|---|---|---|
| No stocks (VT money into a Dec-2032 Treasury) | Payments the same; gift median the same ($163.7k vs $163.3k, because the gift is capped); Laura's flexibility −$4.9k at the median; in history the minimum breaks more often (1.16% vs 0.43% of windows) | ALT §4(2) |
| More VT: 25% of the 2028 deposit | Minimum −$15k (to $120k) for about +$2.5k of median total | ALT §3 |
| S&P 500 (e.g. VOO, 0.03% fee, 506 stocks; Vanguard fact sheet 30 Jun 2026) | Cheaper by 0.03 points; US only (VT is already 61.9% US); no simulation run | `CS/web/voo_F0968.txt` |
| iShares MSCI ACWI (0.32% fee, iShares page 16 Oct) | Same idea as VT at a higher fee | iShares product page 239600 |
| Taiwan stocks | Would add correlation with Laura's own Taiwan project (career and project risk; the client-insight "don't add correlated risk" point, `/home/user/caplet-investment/CLAUDE.md`). VT's Taiwan weight is only 3.5% (about $1.2k of the plan's $33.5k, CALC) | Fact sheet; CLAUDE.md |

### 10d. VT risks (notes)

- **Equity fall.** A 40% fall in 2032 cuts a typical gift by about $7k ($170.5k → $163.2k), never below the minimum, because the floor is owned (REG F7). It never touches the payments, as long as VT is not the payment backstop (LDI §8).
- **Currency.** About 38% of VT is in non-US stocks (fact sheet), so the dollar value moves with exchange rates.
- **Concentration inside VT.** The top 10 are 21.7% and technology 33.3%: broad, but tilted.
- **The cap asymmetry.** From 2031 to 2033 the gift's half of VT can fall but cannot rise past the announced top (LDI §8).
- **Return assumption.** 7.00% compound, 16.78% volatility (JPM 2026 LTCMA, AC World; REG I1). Realised 1-year volatility was about 13.9% (CALC).

### 10e. Judge questions for VT (5)

| # | Question | Facts needed | Trap |
|---|---|---|---|
| V1 [P] | "Under 10% in stocks: timid for a risk-taking entrepreneur?" (K4) | REG H4 (about 7% of Laura's plan); ALT §4(3): more VT moves money from the minimum to Laura almost dollar for dollar; case:68-74 | Saying "9%" for Laura's plan (that is WInS) |
| V2 [P] | "Why one world fund and not the S&P 500 or Taiwan stocks?" | §10a-c (10,048 stocks, 0.06%, US 61.9%, Taiwan 3.5%); the Oct 5 challenge outcome (record it first: DRILL E4) | Inventing a debate that was not logged |
| V3 [P/Y] | "Which job does VT do: the gift's upside, Laura's flexibility, or the payment backstop?" | The note (NOTES:14) vs V5 (LDI §8) | Giving two different answers in two documents |
| V4 [Y] | "Stocks crash 40% in 2032, after the range is announced. What happens?" | REG F7; the floor is owned | Saying the payments are affected |
| V5 [Y] | "VT is down since you bought it. Does that matter?" | −$287 (−1.08%) on 19 Oct; TRD:27; horizon to 2033 | Treating WInS P&L as evidence |

### 10f. VT data table

| Item | Value | Date | Label |
|---|---|---|---|
| Fee / holdings | 0.06% / 10,048 stocks | 30 Jun 2026 | VERIFIED (fact sheet) |
| US / Taiwan / TSMC | 61.9% / 3.5% / 1.7% | 30 Jun 2026 | VERIFIED |
| WInS position | 167 shares at $158.83 (8 Oct open) | 8 Oct | VERIFIED (team records + Yahoo open) |
| WInS value / change | $26,237 / −$287 (−1.08%) | 19 Oct close $157.11 | CALC |
| Laura's plan VT | about $33.5k in Jan 2028 (about 7%) | 19 Oct curve | MODEL (REG E6) |
| Return assumption | 7.00% compound, 16.78% volatility | JPM 2026 | VERIFIED source (REG I1) |
| 40% fall in 2032 | typical gift −$7.3k | 19 Oct | MODEL (REG F7) |
| Next dividend | probably mid-December (after the freeze) | – | INFERENCE |

---

## 11. Final Report checklist for the case study (so nothing is "new" at the semifinal)

| # | Must already be in the Final Report (students' words) | Evidence here |
|---|---|---|
| C1 | What IBTM is, its index and end date, the "no predetermined amount" fact | §2, §3a |
| C2 | The life of a share (from the 2027/2028 purchases to the 1 Jan 2033 payment), including where the cash waits | §3d |
| C3 | The two jobs and the share split, with the payment first | §4b |
| C4 | Why there is no single 2032 Treasury (WInS gap, 6 Oct email) | §4c |
| C5 | The alternatives table, with at least the Nov-2032 note, STRIPS, a short Treasury ETF and the Feb-2036 bond | §5 |
| C6 | Payout drivers with sizes (reinvestment, cash phase, fee) and why the bottom is rounded down | §6 R3-R5; REG F1 |
| C7 | Fund-level risks and the trigger (extension, closure, timing) | §6 R6-R7; LDI §9 T3 |
| C8 | One dated performance line, and the rule that WInS P&L does not count | §7 |
| C9 | The "Long Equities" label explained once | §6 R12 |
| C10 | A shorter VT section whose job list matches the IPS | §10 |
| C11 | The decision-log entry: why IBTM (or VT) is the case study | PB §5; DRILL S1 |

**Team decisions this pack depends on** (not AI decisions):
- D0-1/D2: VT's job list.
- A reinvestment rule (LDI §6a).
- 3r reserve yes or no (it changes the floor to "repays $140k" and the bottom to $135k, REG F1, ALT §4(1)).
- Which holding is the case study. Log it with the reason.

---

## 12. Consistency checks against the register and the LDI file

| Item | This pack | Register / LDI | Verdict |
|---|---|---|---|
| Floor cost | $116.7k (money waits at 0% for the last 17 days) | REG E1 $116,485 (re-run here: identical) | Same model; a $213 convention difference. Quote $116,485 or "about $116-118k" |
| Floor −2 reinvestment | $148.5k (0% wait) / $147.5k (realistic) | REG E3 $148,378; LDI §7: about −$3.0k in total incl. the cash phase | Consistent. The realistic figure adds the cash phase |
| Months of cash before termination | 5.5 months (holdings file) | LDI §3a 5.4 months (WAM) | Consistent |
| YTM / SEC / trailing | 4.94 / 4.98 / 4.05 (16 Oct) | LDI §3a: same. DRILL §2a: 5.05 / 5.00 / 4.07 (14 Oct) | DRILL is two days older. Always date the yield |
| Days to payment | 17 (from 15 Dec) / about 14 (from the 18 Dec precedent) | PB "17 days"; LDI "about 14 days" | Both right; name the starting date |
| WInS IBTM value | $98,458 (19 Oct) | PB:170 "about $98.7k" (16 Oct) | Date difference |
| VT P&L | −$287 | REG H2 −$287 | Same |
| Ladder cost after the fill | $293.5k (6 Oct) → $297,162 (19 Oct), basis D | REG C1 | Same |
| VT share | 7% (Laura) / 8.65-8.84% (WInS) | REG H4 | Same |

---

## 13. UNVERIFIED and limits

- **UNVERIFIED:**
  - The 2026-27 semifinal wording (case study, no new material).
  - That WInS still lists no Treasury from Feb 2031 to Feb 2036 (team check of 29 Sep, not repeated).
  - Whether WInS lists SGOV, the 2.000% Nov-2041 or the 5.000% May-2037.
  - Whether WInS credits the 5 Nov payout.
  - IBTM's own SAI text (the termination clause was read in a sister iShares Trust SAI).
  - The real 2032 payout date (2026 precedent: 18 Dec).
  - Best-market 5-year CD rates and penalties.
  - Why the 12-month payouts ($0.887) run a little above today's coupon cash ($0.82 a share).
  - The ENA calculator (not run).
- **MODEL limits:**
  - One static curve, forward-priced; parallel, permanent shocks.
  - IBTM is modelled as one bond (simple) or as one bond to 1 Jul 2032 plus cash (realistic).
  - No taxes, commissions or bid/ask, and no STRIPS or iBond premium to the curve.
  - CD costs use annual compounding at the national-average rate.
- **Dates:** iShares page data "as of Oct 16, 2026", fetched 19 Oct 22:53 UTC. VT fact sheet as of 30 Jun 2026. IBTM fact sheet as of 30 Jun 2026: its SEC yield 4.24% and 5.98-year WAM are older than the 16 Oct page figures, so use the page. Prices as of the 19 Oct close. **Refresh everything on the 6 Nov close, and again for the Final Report.**

---

## 14. Sources and files

**Web (all fetched 19 Oct 2026, 22:53 UTC to 20 Oct 00:30 UTC, plain curl with a cache-busting query; copies in `CS/web/` and `CS/data/`):**
- IBTM product page: https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (`p_ibtm.html/.txt`)
- IBTM holdings: …/328944/ishares-ibonds-dec-2032-term-treasury-etf/latest-holdings.csv (`hold_ibtm.csv`, "as of Oct 16, 2026")
- IBTM fact sheet (30 Jun 2026): https://www.ishares.com/us/literature/fact-sheet/ibtm-ishares-ibonds-dec-2032-term-treasury-etf-fund-fact-sheet-en-us.pdf (`fs_ibtm.pdf/.txt`)
- IBTM summary prospectus (27 Feb 2026): https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf (`sp_ibtm.pdf/.txt`)
- iShares Trust SAI (27 Feb 2026, other funds): https://www.ishares.com/us/literature/sai/sai-ishares-trust-10-31.pdf (`sai.pdf/.txt`)
- Trust prospectus + 15 Oct 2026 supplement and the 2026-28 distribution schedule: from LDI (`oct20/ldi/web/docs/`), fetched 19 Oct
- SGOV page (fee 0.09%, SEC yield 3.74%, 16 Oct): https://www.ishares.com/us/products/314116/ishares-0-3-month-treasury-bond-etf
- ACWI page (fee 0.32%): https://www.ishares.com/us/products/239600/ishares-msci-acwi-etf
- Vanguard fact sheets (30 Jun 2026): https://fund-docs.vanguard.com/F3141.pdf (VT), https://fund-docs.vanguard.com/F0968.pdf (VOO)
- Treasury par and bill curves, Oct 2026: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv (`tsy_202610.csv`; bills `bill_202610.csv`)
- FDIC national rates (as of 19 Oct 2026): https://www.fdic.gov/national-rates-and-rate-caps (`fdic_rates.txt`; 60-month CD 1.41%, rate cap 6.86%); FDIC deposit insurance: https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance
- Prices: Yahoo chart API (`query1.finance.yahoo.com/v8/finance/chart/{IBTM,VT,SGOV,SHV,BIL,IBTL}`); Nasdaq (`api.nasdaq.com/api/quote/{IBTM,VT}/historical` and `/info`)

**Scripts (in `CS/scripts/`; run with `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I`):**
- `holdings.py web/hold_ibtm.csv`
- `alts.py data/tsy_202610.csv 10/19/2026`
- `extra.py data/tsy_202610.csv 10/19/2026`
- `v5_floor_range_16oct.py data/tsy_202610.csv 10/19/2026` (a copy of the numbers desk's script; reproduces REG E1 exactly)
- `yh.py`, `pdf2txt.py`, `html2txt.py`
- `indep_pricer.py` (a copy of the numbers desk's pricer)

**Outputs:** `CS/data/holdings_ibtm_16oct.txt`, `alts_19oct.txt`, `extra_19oct.txt`, `yahoo_prices.txt`.
