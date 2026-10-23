> **Checked 20 Oct (oct20/verify_art_att/verify_art_att.md); 12 corrections applied** (15 exact text replacements, each asserted by `oct20/artic_fixed/apply_fixes.py`).
> - **A1**: §0 item 1: `numbers_refresh.md:282` -> `:285` (total row; also :18)
> - **A2**: §4 checklist: `numbers_refresh.md:57,64` -> `:60,67`
> - **A3**: §8a: daily SD cited at `numbers_refresh.md:74`, written $1.4-1.6k
> - **A4**: §0 item 2 and §4 checklist: "yields fell" limited to 5-30 years; the 2-year was unchanged
> - **A5**: §4: proxy range stated under both methods (about ±$25 same method; about ±$60 full reprice)
> - **A6**: §6 VT row: Yahoo vs Nasdaq close noted (−1.585% vs −1.579%); line 37 holds no VT figure, nothing to change there
> - **A7**: Header: writing window corrected to about 09:00-10:05 Sydney
> - **A8**: §5, §6 table A, §6c: CFA line 261 labelled as index-strategy context; liability benchmark marked as our inference; lines 285/288 carry the yardstick
> - **A9**: §1 fill timing: official rule cited as trading.txt:52; rules_readme:119 relabelled as team notes
> - **A10**: §7 synthetic test: "about $601" (cited amounts give $600.81; synthetic $600.95 not rechecked)
> - **A11**: §7 timing table: freeze close marked "exact WInS cut-off UNVERIFIED; trading.txt:24 says only 'ends on November 6'"
> - **A12**: §4 checklist: quoted example sentence replaced by fields (level + date + basis + accrued yes/no)

# WInS book: performance attribution and benchmark pack (19 Oct 2026 close)

**AI-generated MODEL numbers and checklists (Claude Code) for Team Caplet, written Tue 20 Oct 2026, about 09:00-10:05 Sydney. This is not text to submit.** It contains numbers, methods, benchmark options, traps and a re-run script. It has no Final Report wording. Wherever this file says what a good answer must contain, the team writes the answer. If a student uses any figure, they re-check it and log the AI help. Wharton's AI Policy says: "If you use AI to assist you in any way during the competition, how you use it must be recorded in your Works Cited pages" (https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026).

- **MODEL** = a computer estimate, not a fact.
- **UNVERIFIED** = nobody has confirmed it.
- **WInS screens were not read.** Every value here is rebuilt from public data. The Wharton screen may differ (section 8).

**Folder:** `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/attrib/` (written `attrib/` below). Other folders are named `oct20/<x>/` and `oct19/<x>/` in the same scratchpad.

---

## 0. The short version

1. **Book at the 19 Oct close: $303,393, up $3,393 (+1.13%) on the $300,000 start.** That counts bond accrued interest. It is $301,902 without accrued interest. The bond prices are MODEL. This matches the 19 Oct numbers pack to the dollar (`oct20/numbers/numbers_refresh.md:285`, total row; also :18).
2. **Why it rose: mostly falling yields.** The decomposition, which adds up:

   | Effect | Amount |
   |---|---|
   | Rates (DV01 × each holding's own yield change) | +$2,421 |
   | Fill-day effect (the ETFs filled below that day's close) | +$771 |
   | Carry (income at the purchase yield) | +$464 |
   | Unexplained WInS cash credit | +$251 |
   | VT | −$270 |
   | Commissions | −$200 |
   | Fees inside the fund prices | −$5 |
   | **Residual** | **−$39** |

   - The residual is inside the $50 target. It equals less than one cent on IBTM's price (1 cent × 4,503 shares = $45).
   - 5- to 30-year yields fell 9-19bp from 7 to 19 Oct; the 2-year was unchanged (5y 5.03 → 4.94, 10y 5.28 → 5.15, 20y 5.71 → 5.53). Long yields fell most.
3. **Against the right yardstick, the bonds lagged slightly.** The ten ladder rungs gained 1.21%. The ten $50,000 payments they serve gained 1.64% in value (scaled to WInS). That gives a **tracking ratio of 99.58** and a surplus change of **−$844** in WInS dollars.
   - $810 of the −$844 is rates. The ladder has **$150.6 of rate sensitivity per 0.01 point against $196.7 for the payments: a hedge ratio of about 77%**. That matches the LDI desk's 78% for Laura's plan (`oct20/ldi/ldi_second_opinion.md` §2b).
   - Coupons and monthly distributions arrive before the payments, so the holdings are shorter than the promise. This is coupon-reinvestment risk showing up live.
4. **Against a policy benchmark, the book is 29bp behind (−$874 from the 7 Oct close).**
   - The benchmark: ladder → payments, floor → $150k in Dec 2032, VT → VT, cash → 0%.
   - The parts of the gap: ladder −$844, floor −$163, VT bought below the 7 Oct close +$133.
   - Against the S&P 500 (−1.37%) the book looks 2.2-2.5 points "ahead" (measured from the 7 Oct mark or from $300,000). That comparison is meaningless here (section 6c): it measures 12 days of bonds against stocks, not the plan.
5. **Traps before 6 Nov and 4 Dec.**
   - **Bond prices on WInS.** The FAQ says WInS updates bond prices "once daily at U.S. market open" (`competition/official/2026_27/smapply_public_2026-10-14/faqs.txt:59`), so the WInS bond marks lag the curve.
   - **The $251 cash gap.** $225.00 of it is explained if WInS runs the May-2038 bond on a Feb/Aug coupon schedule. If WInS also marks that bond on the same schedule, the WInS total is about $225 below this model.
   - **iBond distribution.** The ex-date is Mon 2 Nov and it is paid Thu 5 Nov (about $601 at October rates). Prices drop on the 2nd; the cash arrives on the 5th.
   - **T-bond coupons:** $1,538.75 on Mon 16 Nov. If WInS treats May-2038 as a Feb/Aug bond, only $1,088.75 arrives.
   - **December:** distribution ex 1 Dec, paid 4 Dec (the deadline day).
   - **Clocks:** US clocks change on 1 Nov, so Sydney becomes 16 hours ahead of ET. The 6 Nov close is Sat 7 Nov 08:00 Sydney, and the 6 Nov Treasury curve probably appears after the IPS deadline of 09:00.
6. **Re-run:** `sh attrib/scripts/run_attrib.sh 11/06/2026` (and `12/03/2026`) fetches everything and rebuilds every table. It also appends a row to `attrib/attribution_tracking.csv` (section 7).

---

## 1. Inputs, conventions and what is MODEL

| Input | Source (fetch time) | Status |
|---|---|---|
| Holdings, fills, commissions | WInS fills 7-8 Oct: `snap/main/COMPETITION.md:174-188`; `snap/main/ops/routines/portfolio_check.py:5-17`; `attrib/scripts/trades.csv` | WInS-reported (team) |
| Cash after all fills | $3,513.79, `competition/COMPETITION.md:188` | WInS-reported; reconciliation disputed (8b) |
| ETF closes | Yahoo chart API, saved by `oct20/numbers` on 19 Oct 21:45 UTC (`attrib/data/raw/yahoo/`); Nasdaq API history + "Closed at Oct 19, 2026 4:00 PM ET" quotes, fetched 19 Oct 22:31 UTC (`attrib/data/raw/nasdaq/`) | Public, not official. **Second source:** of 54 Yahoo/Nasdaq pairs since 7 Oct, IBTM-IBTQ agree exactly. IBTR differs by up to half a cent on 8 days, because Yahoo rounds (for example 23.37 vs 23.365 on 7 Oct, about $4). VT differs by one cent on 19 Oct (157.11 vs 157.12) |
| Fill timing | Yahoo opens: iBond ETFs 7 Oct open = fills (IBTR 23.23 vs fill 23.24); VT 8 Oct open 158.83 = fill. Official rule: "Orders may be entered while the U.S. market is closed and will be filled when the market reopens" (`competition/official/2026_27/smapply_public_2026-10-14/trading.txt:52`; it does not say "opening price"). Team notes (a team Drive doc, not Wharton's text) say "at the security's opening price when the market reopens" (`snap/main/team/google_drive/rules_readme.md:119`) | Consistent with the fills |
| Treasury curve | treasury.gov daily par yield curve, October 2026 CSV, fetched 19 Oct 22:27 UTC (`attrib/data/raw/tsy/`); byte-identical to `oct20/numbers/data/tsy_202610.csv` | Official |
| iBond fund facts | iShares product pages "as of Oct 16, 2026": effective duration IBTM 5.02 / IBTO 5.68 / IBTP 6.39 / IBTQ 7.03 / IBTR 7.56 years; average coupon 3.50 / 4.04 / 4.12 / 4.28 / 4.35; YTM 4.94-5.08%; fee 0.07% (`oct20/ldi/data/ibond_keyfacts_live.txt`) | Official fund data |
| IEF / TLT | iShares pages read 19 Oct 2026: effective duration 6.84 / 14.84 years, YTM 5.05% / 5.49%, "as of Oct 16, 2026" (`attrib/web/ishares_239456.txt:420-433`, `ishares_239454.txt:420-433`) | Official fund data |
| Distributions | iShares 2026-28 schedule: ex 2-Nov-26 → pay 5-Nov-26; ex 1-Dec-26 → pay 4-Dec-26 (`oct20/ldi/web/docs/distsched.txt:60-61`). October amounts (Nasdaq dividends API, `attrib/data/raw/nasdaq/*_div.json`): IBTM $0.070012, IBTO $0.07904, IBTP $0.083029, IBTQ $0.08183, IBTR $0.063873 | Official schedule; future amounts UNVERIFIED |

**Conventions (the same as `oct20/numbers/scripts/book_value_oct20.py`, so the totals reconcile):**

1. **T-bonds** are valued by bootstrapping the day's par curve (`indep_pricer.py`). Each bond's **fill-day gap** (WInS fill minus model on the 7 Oct curve) is held constant. Accrued interest runs to T+1 settlement, skipping the 12 Oct bond holiday.
   - The fill gaps per $100: Feb-37 +0.384, May-38 +0.412, Nov-39 −0.223, Nov-40 −0.353, Nov-41 −0.552. They net to −$55 on the sleeve (`attrib/out_1019/extras_out_2026-10-19.txt`).
   - In yield terms the fills were −5.0 to +6.5bp from the model.
2. **Start point.** Total P&L is measured from $300,000 cash. The market attribution starts at the **7 Oct close** (iBond ETFs filled at the 7 Oct open; bonds at the 7 Oct end-of-day). VT starts at the **8 Oct close** (filled at the 8 Oct open). The gap between each fill price and that first close is the **fill-day effect**.
3. **Income** counts once we are entitled to it. For ETFs that is the ex-date; for bonds it is when the settlement date passes the coupon date. Cash shows it on the pay date (`--credit pay`). The FAQ says dividends and coupons appear "at the time they are issued" (`faqs.txt:62-63`). The exact WInS timing is UNVERIFIED.
4. **Cash earns 0%** in WInS (`competition/COMPETITION.md:80`).

---

## 2. Daily book value, 7 → 19 Oct (MODEL bonds; ETFs at closes)

Source: `attrib/out_1019/book_daily.csv`.
- On 7 Oct VT is shown at cost, because its order was still open.
- 12 Oct was Columbus Day: stocks traded, the bond market was closed, so the bonds keep their 9 Oct curve.
- The tracking ratio is ladder ÷ payments, indexed to 100 at the 7 Oct close.

| Close (ET) | Curve | iBond ETFs | T-bonds (incl. accrued) | VT | Cash | **Total** | vs $300k | Day change | Total ex-accrued | 2y / 10y par | Ladder job | Ten payments, PV (basis D) | Tracking ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 Oct | 10-07 | $184,639 | $86,162 | $26,525 (cost) | $3,514 | **$300,839** | +0.28% | – | $299,478 | 4.77 / 5.28 | $197,766 | $289,083 | 100.00 |
| 8 Oct | 10-08 | $185,128 | $86,698 | $26,508 | $3,514 | **$301,848** | +0.62% | +1,010 | $300,477 | 4.75 / 5.22 | $198,641 | $290,903 | 99.81 |
| 9 Oct | 10-09 | $185,022 | $86,604 | $26,692 | $3,514 | **$301,832** | +0.61% | −17 | $300,416 | 4.80 / 5.24 | $198,491 | $290,468 | 99.89 |
| 12 Oct | 10-09 (bond holiday) | $185,009 | $86,604 | $26,636 | $3,514 | **$301,763** | +0.59% | −68 | $300,348 | 4.80 / 5.24 | $198,488 | $290,468 | 99.89 |
| 13 Oct | 10-13 | $185,218 | $86,930 | $26,680 | $3,514 | **$302,342** | +0.78% | +578 | $300,916 | 4.79 / 5.21 | $198,962 | $291,650 | 99.72 |
| 14 Oct | 10-14 | $185,468 | $87,137 | $26,331 | $3,514 | **$302,450** | +0.82% | +108 | $301,013 | 4.82 / 5.19 | $199,352 | $292,410 | 99.66 |
| 15 Oct | 10-15 | $186,496 | $87,898 | $26,438 | $3,514 | **$304,345** | +1.45% | +1,895 | $302,897 | 4.77 / 5.10 | $200,804 | $295,116 | 99.46 |
| 16 Oct | 10-16 | $186,715 | $88,012 | $26,189 | $3,514 | **$304,429** | +1.48% | +84 | $302,948 | 4.74 / 5.09 | $201,037 | $295,470 | 99.46 |
| **19 Oct** | 10-19 | $186,111 | $87,532 | $26,237 | $3,514 | **$303,393** | **+1.13%** | −1,036 | $301,902 | 4.77 / 5.15 | $200,154 | $293,808 | **99.58** |

- **Check against earlier work:** 8, 13, 14, 15, 16 and 19 Oct are identical to `oct20/numbers/wins_book_value_series.csv`.
  - 9 Oct is $10 higher here, because settlement is 13 Oct (the 12 Oct holiday is skipped) rather than 12 Oct.
  - Measured from an 8 Oct base, the tracking ratio on 19 Oct is 99.77, the same as `oct20/charts/charts_data_pack.md:253`.
- **Pattern:** the tracking ratio falls on days yields fall (15 Oct: 10y −9bp, ratio 99.66 → 99.46). It recovers when they rise (19 Oct: +6bp, 99.46 → 99.58). That is the under-hedge in section 5.

---

## 3. Return by holding, by sleeve, and contribution to the total (7 Oct fill → 19 Oct close)

Source: `attrib/out_1019/attribution_2026-10-19.csv`.
- Cost includes the accrued interest paid on bonds (model, at 8 Oct settlement), but not commissions.
- Contribution = P&L ÷ $300,000.

| Holding | Job | Cost | Value 19 Oct | P&L | Return | Contribution (points of $300k) |
|---|---|---|---|---|---|---|
| IBTM 4,503 sh | Jan 2033 payment (1,142 sh) + floor stand-in (3,361 sh) | $97,489.95 | $98,458.09 | +$968.14 | +0.99% | +0.32 |
| IBTO 1,024 sh | Jan 2034 | $23,408.64 | $23,690.24 | +$281.60 | +1.20% | +0.09 |
| IBTP 927 sh | Jan 2035 | $22,155.30 | $22,465.94 | +$310.64 | +1.40% | +0.10 |
| IBTQ 894 sh | Jan 2036 | $20,973.24 | $21,321.90 | +$348.66 | +1.66% | +0.12 |
| IBTR 853 sh | Jan 2037 | $19,823.72 | $20,174.56 | +$350.84 | +1.77% | +0.12 |
| T 4.750% Feb-2037 ($20k) | Jan 2038 | $19,343.20 | $19,584.50 | +$241.30 | +1.25% | +0.08 |
| T 4.500% May-2038 ($20k) | Jan 2039 | $18,972.27 | $19,238.39 | +$266.12 | +1.40% | +0.09 |
| T 4.375% Nov-2039 ($18k) | Jan 2040 | $16,513.33 | $16,780.17 | +$266.84 | +1.62% | +0.09 |
| T 4.250% Nov-2040 ($18k) | Jan 2041 | $16,093.83 | $16,377.57 | +$283.74 | +1.76% | +0.09 |
| T 3.125% Nov-2041 ($20k) | Jan 2042 | $15,238.96 | $15,550.95 | +$311.98 | +2.05% | +0.10 |
| VT 167 sh | Growth | $26,524.61 | $26,237.37 | −$287.24 | −1.08% | −0.10 |
| Cash | Fees and rounding | – | $3,513.79 | – | 0% | – |
| Commissions (11 trades) | | | | −$200.00 | | −0.07 |
| Cash gap (8b) | | | | +$250.84 | | +0.08 |
| **Total** | | | **$303,393.47** | **+$3,393.47** | **+1.13%** | **+1.13** |

| Sleeve | Cost | Value | P&L | Return | Contribution |
|---|---|---|---|---|---|
| iBond ladder (IBTM-IBTR) | $183,850.85 | $186,110.73 | +$2,259.88 | +1.23% | +0.75 points |
| T-bond ladder (5 bonds) | $86,161.59 | $87,531.58 | +$1,369.99 | +1.59% | +0.46 points |
| VT | $26,524.61 | $26,237.37 | −$287.24 | −1.08% | −0.10 points |
| Commissions + cash gap | | | +$50.84 | | +0.02 points |

- **Read-across:** returns rise with maturity (IBTM +0.99% → Nov-2041 +2.05%). That is what a fall in yields does to a ladder. The long end fell most (20y −18bp).
- **IBTM's return is the lowest of the bonds**, for two reasons:
  - it is the shortest holding (duration 5.0);
  - its fill-day gain was large ($360) but its residual was the largest (−$59, about 1.3 cents a share).
- **By job (section 5):**

  | Job | Value | Return |
  |---|---|---|
  | Payment ladder (10 rungs including 1,142 IBTM) | $200,154 | +1.21% from 7 Oct close |
  | Floor stand-in (3,361 IBTM) | $73,488 | +0.62% |
  | VT | $26,237 | −1.08% from fill |

---

## 4. Attribution: what explains the +$3,393

Script: `attrib/scripts/attrib.py`. Output: `attrib/out_1019/attrib_out_2026-10-19.txt` and `attribution_daily.csv`.

**Definitions** (plain English first):
- **Rates** = how much each holding's price moves for a 0.01-point yield change (its DV01), times the change in its own yield since the fill. For T-bonds, DV01 comes from the model at the fill. For iBond funds it is iShares' effective duration × value at the 7 Oct close; the yield change is measured on a proxy Treasury (fund's average coupon, maturing 15 Aug of the fund's year).
- **Carry** = the income the holding earns if yields don't move.
  - For a T-bond: the coupon accrual plus the drift of a discount bond toward $100 ("pull to par").
  - For an iBond fund: value × proxy yield × days ÷ 365.
- **Fill-day effect** = (that day's close − fill price) × units.
- **Fund fees** = 0.07% (iBonds) and 0.06% (VT) a year. They are already inside the prices, so they are shown as a memo line with the equity/carry figures grossed up.
- **Cash gap** = WInS-reported cash minus cash rebuilt from the fills.

| Component | iBond ladder | T-bond ladder | VT | Book | Share of P&L |
|---|---|---|---|---|---|
| Rates (DV01 × own-yield change) | +$1,211.37 | +$1,209.55 | – | **+$2,420.92** | 71% |
| Carry (income at purchase yield) | +$312.46 | +$151.40 (coupon accrual $131.34 + pull to par $20.06) | – | **+$463.86** | 14% |
| Fill-day effect | +$788.01 | $0 (by construction) | −$16.70 | **+$771.31** | 23% |
| Equity (VT price move, gross of fund fee) | – | – | −$270.06 | **−$270.06** | −8% |
| Fund fees inside prices (memo) | −$4.25 | – | −$0.48 | **−$4.73** | 0% |
| Commissions (6 × $25 + 5 × $10) | | | | **−$200.00** | −6% |
| Cash gap (WInS cash − rebuilt cash) | | | | **+$250.84** | 7% |
| **Explained** | | | | **+$3,432.13** | |
| **Residual** | −$47.71 | +$9.05 (convexity: full reprice minus DV01) | $0.00 | **−$38.66** | −1% |
| **Total P&L vs $300,000** | +$2,259.88 | +$1,369.99 | −$287.24 | **+$3,393.47** | 100% |

**Rate sensitivity at the start (MODEL):**
- Book DV01 is **$187.2 per 0.01 point**: iBond ETFs $106.6, T-bonds $80.6.
- Yield changes by holding, 7 → 19 Oct: IBTM −10.3bp, IBTO −11.2, IBTP −11.9, IBTQ −12.6, IBTR −13.3, Feb-37 −13.5, May-38 −14.2, Nov-39 −15.0, Nov-40 −15.6, Nov-41 −16.5.

**Reconciliation and how firm it is:**
- **On 19 Oct the residual is −$38.66, inside the ±$50 target.** Bond convexity accounts for +$9. The rest is iBond price noise: one cent on IBTM is $45.03, and the fund's closing price is not its NAV.
- **The rates/residual split for the iBond funds depends on the proxy.** The proxy month moves the iBond rates line by about ±$25 under the headline method (effective duration × proxy Δy: a May or November proxy gives about $1,188 or $1,234; independent check, `oct20/verify_art_att/verify_art_att.md` A5), or by about ±$60 with a full reprice of the proxy ($1,144 May / $1,263 Nov, total residual about +$28 / −$90; `attrib/out_1019/verify_out_2026-10-19.txt`, rows "proxy"). So **say "about $2.4k from rates", not "$2,420.92"**.
- **Daily residuals vary.** Across the eight days the residual ran from −$78 (13 Oct) to +$93 (9 Oct) (`attribution_daily.csv`). The ±$50 test holds on 19 Oct but not every day. On a typical day a $50-100 gap is ETF closing-price noise, not a missing effect.
- **What the fill-day effect is.**
  - The five iBond orders and VT filled at opening prices below that day's close: +$788 for the iBonds, −$17 for VT.
  - Against the previous close, the price the team saw when ordering, they filled $856 cheaper (iBonds $720, VT $135; `extras_out_2026-10-19.txt`).
  - Yields barely moved from 6 to 7 Oct (5y 5.03 → 5.03, 10y 5.27 → 5.28), so this was the opening print, not rates. **It was luck, and it can go the other way.** An order placed while the market is closed fills at whatever the open is.
- **Carry check:** the book's carry ($464 in 12 days) ≈ $270k of bonds × about 5.1-5.3% × 12/365 ≈ $455-470. ✓

**Checklist for a team answer to "how did your portfolio do and why?"** (components only; the team writes the words)
- [ ] The level, as fields: level + date + basis (model or WInS screen) + accrued interest yes/no. Never undated.
- [ ] The main driver: 5- to 30-year yields fell about 0.1-0.2 points (the 2-year was unchanged), and the book is about 90% Treasuries.
- [ ] Equity was a small drag; VT is under 9% of the book.
- [ ] Costs: commissions $200 and fund fees.
- [ ] Luck: the opening fills.
- [ ] The LDI verdict (section 5): the bonds moved with the payments but lagged slightly, and why.
- [ ] Why the WInS gain is **not** good news for Laura: in her real plan, falling yields make the January 2027 ladder dearer (basis D $293,066 on 7 Oct → $297,162 on 19 Oct, `oct20/numbers/numbers_refresh.md:60,67`).
- [ ] That WInS P&L is not added to her projections (case:132-133; Guide:70-73).

---

## 5. The LDI view: did the bonds do their job? (ladder vs the payments it serves)

**Set-up (MODEL).**
- **Liability:** ten $50,000 amounts on each holding's end date (basis D: 15 Dec 2032-36 for the funds, then each bond's maturity). They are valued every day on the bootstrapped treasury.gov curve.
- **Scaling:** the liability is multiplied by **0.6841**, the ladder's 7 Oct close value ($197,766) ÷ the liability PV ($289,083). Both lines then start at the same dollars.
- **Ladder job:** 1,142 IBTM shares + all of IBTO-IBTR + the five T-bonds, income included.

| 7 Oct close → 19 Oct close | Ladder (assets) | Payments (liability, scaled) | Gap (surplus change) |
|---|---|---|---|
| Change | **+$2,388.13 (+1.21%)** | **+$3,232.49 (+1.64%)** | **−$844.36** |
| of which rates | +$2,043.65 | +$2,854.02 | **−$810.37** |
| of which carry / accretion | +$339.08 (net of fund fees) | +$378.47 (accretion and roll-down) | −$39.39 |
| of which ETF residual | +$5.40 | – | +$5.40 |
| Rate sensitivity (DV01, per 0.01 point) | **$150.6** | **$196.7** | hedge ratio **76.5%** |
| Duration | about 7.6 years | 9.95 years (basis D, 7 Oct) | |

- **Tracking ratio** (ladder index ÷ payments index × 100): **99.58** on basis D. On payment dates (basis A, liability +1.68%) it is **99.54**.
- **Floor stand-in** (3,361 IBTM): +0.62% against the value of $150,000 at 15 Dec 2032, +0.84%. Ratio 99.78, gap −$163. The cause is the same: IBTM's 5.0-year duration against about 6.0 for a Dec-2032 zero.
- **What it means.** The holdings pay coupons and monthly distributions years before the payments. So they are less rate-sensitive than the ten single $50,000 amounts. When yields fall, the payments' value rises about 30% more than the ladder: $196.7 against $150.6 per 0.01 point.
  - This is the WInS-scale view of the coupon-reinvestment gap in Laura's plan: about $19.5-21.3k if yields fall 2 points for good (holdings' dates after the fix / number-sheet basis) [consistency fix 20 Oct, row 33] (`oct20/numbers/numbers_refresh.md:167-183`).
  - It is also the LDI desk's "hedge ratio 78% ... the assets are shorter than the promise" (`oct20/ldi/ldi_second_opinion.md` §2b).
- **The reverse also holds:** if yields rise before 6 Nov, the ratio rises back above 100. Over 12 days the gap is small (−0.42%). The point is the direction and the mechanism, not the size.
- **Source for the yardstick:** CFA Institute, "Liability-Driven and Index-Based Strategies" (2026 refresher reading, https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/liability-driven-index-based-strategies, read 19 Oct 2026; copy `attrib/web/cfa_ldi_2026.txt`). It defines:
  - surplus as "the difference between the asset and liability market values" (line 288);
  - one immunisation condition as "the asset basis point value (BPV) equals the liability BPV" (line 285);
  - and it says it is "critical to select a benchmark that is most relevant to a specific investor based on factors such as the targeted duration profile and risk appetite" (line 261). That sentence closes the reading's summary of *index-based* strategies (choosing a bond index), not liability benchmarks. Applying it here is our inference: for a liability-driven investor the relevant benchmark is the liability. Lines 285 and 288 carry the LDI yardstick.
- **Caveat.** Cash-flow matching does not aim at equal BPV. The plan holds each rung to its date and accepts the reinvestment gap, with a named cover. The 77% hedge ratio describes the risk; it does not grade the plan. Do not call the plan "immunised" (`competition/COMPETITION.md:168`: "cash-flow matching (**not** immunisation)").

---

## 6. Benchmark options and how defensible each is (7 Oct close → 19 Oct close)

Source: `attrib/out_1019/benchmarks_2026-10-19.csv`.
- ETF benchmark figures are price returns. No ex-date fell inside the window for IEF, TLT, BND, SPY, SGOV or VT (checked in the Yahoo/Nasdaq event data; the iShares bond funds go ex on 1 Oct and 2 Nov).
- The book returns +0.849% from its 7 Oct close mark ($300,839) and +1.131% from $300,000 cash.

| Benchmark | Return | Same return on the 7 Oct mark | Book minus benchmark | Defensible for this plan? |
|---|---|---|---|---|
| **A. The liability itself:** ten payments, scaled (tracking ratio). Ladder job only | Payments +1.635% (D) / +1.677% (A) vs ladder +1.208% | – | **Ratio 99.58 (D) / 99.54 (A); −$844** | **Best.** It measures the one thing the plan promises: the payments are covered (case:91, "high degree of certainty"; CFA lines 285 and 288; our inference: for a liability-driven investor the relevant benchmark is the liability). Weaknesses: MODEL (curve bootstrap), the basis choice (A or D) moves it by 0.04, and it is not something you can buy |
| **A+. Policy benchmark:** ladder → payments, floor → $150k Dec 2032, VT → VT, cash → 0% (weights 65.7 / 24.3 / 8.8 / 1.2% of the 7 Oct mark) | +1.140% | +$3,429 | **−29.1bp (−$874)**: ladder −$844, floor −$163, VT timing +$133 | **Best whole-book yardstick.** Every dollar is compared with its own job. VT is benchmarked to itself, so it adds nothing except its fill timing |
| **B. Duration-matched IEF/TLT:** 61.2% IEF (6.84y) + 38.8% TLT (14.84y), matched to the liability's 9.95 years | +1.831% (IEF +1.089%, TLT +3.001%) | +$5,509 | Ladder −0.62 points | **Good as a "cheap alternative we rejected" check.** It is investable, simple, and gives a money-weighted duration match. But it matches one number (duration), not dates or curve shape. In this bull flattening (30y −19bp) it beat the liability itself (+1.83% vs +1.64%) because TLT holds 20-30-year bonds. It is not a promise to pay $50,000 on a date. Whether WInS lists IEF/TLT was not checked here (UNVERIFIED) |
| **B+. IEF/TLT mix for the bond money + VT for the VT money** | +1.509% | +$4,538 | −66bp | As B |
| **C. 60/40 VT/BND** | −0.608% (BND +0.857%) | −$1,829 | +146bp | **Weak.** The risk profile is wrong (60% stocks against about 9%). BND holds corporate bonds and mortgages and has a shorter duration. Use it only as "what a textbook balanced fund did", never as a target |
| **D. Cash (3-month bill accrual, 4.22-4.27%)** | +0.140% (SGOV +0.119%) | +$421 | +71bp | **Useful as the "do nothing" baseline.** It shows why cash is risky here: the payments' value rose 1.64% while cash rose 0.14%. Holding cash would have lost about 1.5% of funding in 12 days. WInS cash earns 0% (`competition/COMPETITION.md:80`) |
| **E. S&P 500 (SPY)** | −1.366% | −$4,111 | +2.2 points ("ahead") | **Wrong yardstick** (6c) |
| VT alone, from the 7 Oct close | −1.585% (Yahoo close 157.11; Nasdaq 157.12 gives −1.579%) | | Book's VT −1.08% from its 8 Oct fill | Only for the VT sleeve. Bought at the 8 Oct open, below the 7 Oct close: +$133 |

### 6a. Which to use where (recommendation, not a decision)
- **Final Report "evaluate how it implemented its investment strategy"** (`smapply_public_2026-10-14/deliverables.txt:50`): use **A (tracking ratio) and A+ (policy)**. Keep B as a one-line "simpler alternative". Mention C, D and E at most as context, or not at all.
- **The "Portfolio Analysis" criterion** asks for projections that "evaluate funding reliability, the facility contribution, and financial flexibility under varying market outcomes" (`deliverables.txt:57`). That is about Laura's plan, not WInS P&L. This pack supports the implementation story only.
- Any chart of A: one line for the ladder index and one for the payments index (the C4 design, `oct20/charts/charts_data_pack.md:238-297`). Name the basis.

### 6b. What each yardstick would have "said" over these 12 days
- The S&P frame says the team "won" by 2.2-2.5 points.
- The 60/40 frame says it was 1.5 points ahead.
- The liability frame says the ladder fell 0.42% behind its promise.
- **Only the third is about Laura.** The first two would reverse in any month when yields rise and stocks rally, even if the plan did exactly its job.

### 6c. Why "beat the S&P" is the wrong yardstick (facts with citations)
- **The competition says so.**
  - "WInS is a tool for implementing your investment strategy. It is not the competition scorecard" (Guide:70).
  - Teams are "not being evaluated based on: ... Whether you outperform other teams ... Whether your portfolio makes money during the competition" (Guide:74-78).
  - "A long-term investment strategy cannot be judged solely by what happens in the market over a few weeks" (Guide:79).
  - The WInS portfolio "does not determine Laura's actual portfolio value", and its gains "should not be added to or subtracted from Laura's portfolio projections" (case:129-133).
- **The IPS instructions point the same way:** "Focus on the strategy and decision-making framework that guide your portfolio rather than describing individual investments or presenting detailed financial calculations" (IPS:51-52).
- **The client's goal is a liability, not a market index.** "All ten payments must be funded by the investment portfolio with a high degree of certainty" (case:91). The book is about 90% Treasuries (`oct20/numbers/numbers_refresh.md:302`) because of that goal. An equity index measures a risk the plan deliberately does not take.
- **The LDI source supports the yardstick.** It defines surplus = asset value − liability value (CFA line 288) and an immunisation condition of asset BPV = liability BPV (CFA line 285). Its advice to pick the benchmark that fits the investor's "targeted duration profile and risk appetite" (CFA line 261) closes its summary of index-based strategies (our inference: for a liability-driven investor the relevant benchmark is the liability).
- **A trap inside the trap.** A WInS gain from falling yields coincides with Laura's real January purchase getting dearer: basis D +$4,096, 7 → 19 Oct. So "we made money" can never be framed as good news for her (`oct19/tnakit/tna_fact_kits.md:350`).

---

## 7. Re-running on any later date (6 Nov freeze, 4 Dec)

**One command** (it fetches treasury.gov for Oct-Dec 2026, Yahoo with retries, Nasdaq history, quotes and dividends, then runs everything):
```
sh /tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/attrib/scripts/run_attrib.sh 11/06/2026
```

**Outputs** go in `attrib/out_2026-11-06/`:
- `book_daily.csv`, the daily value series from 7 Oct;
- `attribution_<date>.csv`, by holding;
- `attribution_daily.csv`, the components by day;
- `benchmarks_<date>.csv`;
- `summary_<date>.json`;
- `attrib_out_<date>.txt`, the full printout;
- `verify_out_<date>.txt`, the independent check.

A model row is added to `attrib/attribution_tracking.csv`.

**Options:**
- `--credit pay|ex|none` sets when income enters cash (default `pay`). Use `none` to model "WInS never credits".
- `--wins-cash X` takes a newer WInS cash figure.
- `prices_override.csv` (`date,ticker,close`) takes WInS screen prices.
- `income_events.csv` (`ticker,ex_date,pay_date,amount_per_share`) takes WInS-shown distributions.
- `trades.csv`: add a row for any new trade (there should be none: the plan is hold).

**Timing in Sydney** (computed with the IANA time zones; US clocks go back on Sun 1 Nov, so ET becomes UTC−5 and Sydney stays UTC+11):

| Event | ET | Sydney |
|---|---|---|
| TNA deadline | Fri 23 Oct 5:00 pm | Sat 24 Oct 08:00 |
| iBond ex-date (price drops about $0.064-0.083 a share) | Mon 2 Nov open | Tue 3 Nov 01:30 |
| iBond distribution paid | Thu 5 Nov | Fri 6 Nov |
| **Freeze close** (exact WInS cut-off UNVERIFIED; trading.txt:24 says only "ends on November 6") | **Fri 6 Nov 4:00 pm** | **Sat 7 Nov 08:00** |
| IPS deadline | Fri 6 Nov 5:00 pm | Sat 7 Nov 09:00 |
| 6 Nov Treasury curve published | evening ET (on 19 Oct it was already up at 5:38 pm ET; the exact posting time is UNVERIFIED) | about 09:30-10:00 Sat 7 Nov if posted at the same time, so after the 09:00 IPS deadline (UNVERIFIED) |
| T-bond coupons (15 Nov is a Sunday) | Mon 16 Nov | Tue 17 Nov |
| Distribution ex / pay | Tue 1 Dec / Fri 4 Dec | Wed 2 Dec / Sat 5 Dec |
| Last full close before the deadline | Thu 3 Dec 4:00 pm | Fri 4 Dec 08:00 |
| Final Report deadline | Fri 4 Dec 5:00 pm | Sat 5 Dec 09:00 |

So run `run_attrib.sh 11/06/2026` on Sat 7 Nov after about 10:00 Sydney, which is after the IPS has gone in. The IPS needs none of these numbers. For the Final Report, run `11/06/2026` on Sat 7 Nov after about 10:00 Sydney (the one valuation date, the Fri 6 Nov close, OPS:228; vote D8 at M5 confirms it). Never run after the Mon 30 Nov 20:00 final-text lock; never on Fri 4 Dec [consistency fix 20 Oct, row 16].

**Tracking template** (`attrib/attribution_tracking_template.csv`): one row per date.
- Rows: 7 Oct start (filled), 19 Oct (filled, model) and blank rows for 23 Oct, 30 Oct, 6 Nov, 20 Nov, 1 Dec and 3 Dec.
- Columns:
  - WInS total and cash, typed from the W1 screen;
  - the model total, ex-accrued total and WInS − model;
  - the components: fill-day, rates, carry, VT, fees, commissions, cash gap, residual;
  - income received and receivable;
  - book DV01;
  - ladder, liability, tracking ratio, hedge ratio and surplus change;
  - the policy benchmark and the gap to it;
  - IEF/TLT, 60/40, cash and SPY;
  - notes.

  It complements the weekly screen-capture template in `oct20/charts/wins_tracking_template.csv`, which records the WInS prices themselves.

**Self-tests.** `attrib/scripts/make_synthetic_test.py` builds a fake 20 Oct-20 Nov with yields and prices frozen, the 2 Nov ex-date and the 16 Nov coupons (`attrib/test_synthetic/out/`). Results:
- the value with income is smooth through 2 Nov and 13 Nov (no false drop);
- about $601 of distributions lands in cash on 5 Nov (the cited October amounts × holdings give $600.81; the synthetic run's $600.95 is 14 cents higher, and its input was not rechecked);
- $1,538.75 of coupons lands on 16 Nov;
- the independent script agrees within $32, the same structural gap as on 19 Oct.

---

## 8. Traps

### 8a. The WInS screen value vs this model (all UNVERIFIED until the team screenshots W1/W2)

| Possible WInS difference | Size on 19 Oct | Evidence |
|---|---|---|
| WInS bond prices are set **once a day at the US open** ("The bond prices are updated once daily at U.S. market open", `faqs.txt:59`), not at the treasury.gov close | A one-day lag on $87.5k of bonds is about $80 per 0.01 point. On 15 Oct (10y −9bp) the bond sleeve moved $761 | Official FAQ |
| WInS shows **clean bond prices without accrued interest** in the total | −$1,492 (the ex-accrued total is $301,902) | FAQ says WInS shows "the interest accrued since" the last coupon (`faqs.txt:59`), but not whether the total counts it |
| WInS accrues **May-2038 from 15 Aug** (a Feb/Aug schedule) | −$225.00 on its value; offsets most of the cash gap (8b) | WInS showed last coupon 15 Aug (`competition/COMPETITION.md:97`) |
| WInS marks bonds **at its own feed**, not curve + fill gap | ±$55 if marks go to the curve; more if the feed's spread moves | Fill gaps −5.0 to +6.5bp (section 1) |
| WInS ETF prices **intraday or the previous close** when the screen is read | One day is about $1.0-1.6k (daily SD $1.4-1.6k: "$1,365 over the year and $1,616 over the last 21 days", `oct20/numbers/numbers_refresh.md:74`) | Trading notes: "WInS shows the previous close" (`oct19/drive/sheets/trading_notes.md:95`) |

**Rule:** quote a WInS total only with its date, its source (WInS screen or model) and its accrued basis. On 19 Oct a WInS display could plausibly be anywhere from about $301.9k (no accrued) through $303.2k (May-2038 on WInS's schedule) to $303.4k (this model). Add a few hundred dollars either way for bond-mark timing, and about $1-1.6k if the screen shows a different day's ETF prices.

### 8b. The cash reconciliation gap (about $251, DISPUTED)
- **Rebuilt cash** = $300,000 − ETFs $210,375.46 − bond clean $84,801.22 − accrued (model) − commissions $200.

  | Accrued settlement date | Accrued | Rebuilt cash |
  |---|---|---|
  | 8 Oct | $1,360.37 | $3,262.95 |
  | 7 Oct | $1,349.42 | $3,273.90 |

  WInS shows $3,513.79, so **$239.89-250.84 is unexplained by standard bond maths**. This reproduces `snap/main/research/assistant_review_2026-10/01_Caplet_Team_Brief_15Oct2026.md:293`.
- **Leading explanation (UNVERIFIED).** WInS treats the May-2038 bond as paying 15 Feb / 15 Aug. Its accrued is then 54 of 184 days, not 146 of 184: **exactly $225.00 less**. What is left over depends on the accrual date:

  | Accrued to | Unexplained |
  |---|---|
  | 6 Oct (order day) | $3.95 |
  | 7 Oct | $14.89 |
  | 8 Oct | $25.84 |

  30/360 and actual/365 day counts change this by under $10 (`attrib/out_1019/verify_out_2026-10-19.txt`; inline test in this session).
- **In the attribution** the gap is a separate line (+$250.84), never "return". If WInS also marks May-2038 on its own schedule, the gap cancels inside the WInS total (cash +$225, bond −$225).
- **Two checks that settle it:**
  - Transaction History (accrued charged per bond);
  - whether WInS pays the May-2038 coupon ($450) on 16 Nov or not until 15 Feb.

### 8c. The 2 Nov ex-date / 5 Nov pay date (iBond funds) and the 6 Nov freeze
- **The price drops on 2 Nov.** At October rates it is $0.064-0.083 a share, about **$601** on the book. Over the last 12 months monthly payouts imply about $575-670 (`oct20/ldi/data/div_summary.txt`).
- **The cash arrives 5 Nov** (`distsched.txt:60-61`), if WInS credits it then (UNVERIFIED; FAQ "at the time they are issued", `faqs.txt:63`).
- **On 2-4 Nov a price-only WInS total looks about $600 lower.** That is not a loss. The script's `total_incl_receivable` keeps it. The freeze snapshot on 6 Nov should already include the cash; if WInS has not credited it, record that.
- **Do not trade to reinvest it.** It costs $25 and breaks "hold" (`oct20/ldi/ldi_second_opinion.md`, "Next payout and the WInS freeze").
- `competition/COMPETITION.md:190` says the November distributions "may pay around 6 Nov". The iShares schedule says **5 Nov**. Update it.

### 8d. 16 Nov coupons and the 1 Dec / 4 Dec distribution
- **Coupons:** $1,538.75 on Mon 16 Nov. Accrued interest resets at the same moment, so a total without income will look about $1,540 lower from the 13 Nov row (settlement 16 Nov) until the cash appears.
- **The December distribution** goes ex 1 Dec and is paid 4 Dec, the deadline day. A 3 Dec valuation should show it as receivable, not cash.

### 8e. The clock change (DST)
- **From 1 Nov Sydney is 16 hours ahead of ET** (15 before). The close becomes 08:00 Sydney, not 07:00.
- `portfolio_check.py:19` already has the freeze at Sat 7 Nov 08:00 AEDT (correct).
- The older `book_value*.py` scripts convert Yahoo dates with a fixed −4 hours. That still gives the right date after 1 Nov, because Yahoo's daily stamps are 9:30 am local. `attrib.py` uses the America/New_York zone, so it is safe either way.
- Any "fetched at hh:mm Sydney" note after 1 Nov is one hour later in ET terms than in October.

### 8f. Data traps
- **Holidays:** treasury.gov has no curve on bond-market holidays (12 Oct; **Wed 11 Nov** Veterans Day; Thu 26 Nov). The script prices bonds on the last curve and flags it "STALE". Stocks trade on 11 Nov. Thanksgiving week times: see `oct20/charts/charts_data_pack.md` §7 (UNVERIFIED).
- **Yahoo throttling:** Yahoo returned HTTP 429 for every request this morning (19 Oct 22:25-23:00 UTC). `fetch_yahoo.sh` retries the first ticker 3 times, then tries each of the others once, then falls back to Nasdaq. Nasdaq's history lags; its "Closed at ... 4:00 PM ET" quote gives the latest close.
- **Wrong coupon in competition/COMPETITION.md:** it lists "5.000% T-bond Feb-2037" (`competition/COMPETITION.md:181`), but WInS shows 4.750% (CUSIP 912810PT9; `01_Caplet_Team_Brief_15Oct2026.md` §5). All scripts here use 4.750%. Fix it in the repo.
- **IBTR fill:** WInS says 23.24; Yahoo's 7 Oct open is 23.23. That is $8.53 per cent. Use the WInS figure.

---

## 9. Verification log ("verify twice")

1. **Check 1: reproduction.** `attrib.py` reproduces `oct20/numbers` exactly: book $303,393 (19 Oct), the series for 8 and 13-19 Oct, ex-accrued $301,902, accrued $1,491.70. The charts pack's tracking ratio (99.77, 8 Oct base) is also reproduced. The cash rebuild reproduces the 15 Oct brief's $3,273.90 / $3,262.95 and the "one reader" $3,498.90 / $3,509.84.
2. **Check 2: independent script.** `verify_attrib.py` (`attrib/out_1019/verify_out_2026-10-19.txt`) shares no pricing code. It uses yield-to-maturity at interpolated par yields and street-convention accrued interest.

   | Item | Independent | Main | Gap |
   |---|---|---|---|
   | Total | $303,360.17 | $303,393.47 | −$33 (bond sleeve; the known gap between interpolation and bootstrap, as in `numbers_refresh.md:38-40`) |
   | Bond rates | $1,186.6 | $1,209.6 | |
   | ETF rates (proxy full reprice) | $1,216.2 | $1,211.4 | |
   | Carry | $455.9 | $463.9 | |
   | Fill-day effect | $771.3 | $771.3 | same |
   | Cash gap | +$250.84 | +$250.84 | same |

3. **Prices, and a third run on the fallback path.** Yahoo and Nasdaq closes agree (half a cent on IBTR, one cent on VT on 19 Oct; `scripts/cmp_sources.py`). The full pipeline `run_attrib.sh 10/19/2026` was run live. Yahoo was throttled (HTTP 429), so it used Nasdaq only, and it gave **$303,395.14**: +$1.67 against the main run, which is VT's one cent. That confirms the fallback works (`out_2026-10-19/`).
4. **Hand checks.**
   - Commissions 6 × $25 + 5 × $10 = $200.
   - Coupons 450 + 393.75 + 382.50 + 312.50 = $1,538.75.
   - May-2038 Feb/Aug accrued difference: 20,000 × 2.25% × 92/184 = $225.00.
   - Book DV01 106.59 + 80.64 = $187.2.
   - Policy gap: −844.36 − 163.08 + 133.12 = −$874.32 (the script gives −$874).
5. **Synthetic future test.** Section 7: income timing, coupon reset and holiday settlement behave as intended.

---

## 10. What this teaches (for Ray's learning goal)
- **A return needs a "compared with what".** The same +1.13% is "great" against stocks and "slightly behind" against the payments. The client's goal picks the yardstick.
- **Attribution = splitting a change into causes you can name.** Rates, income, luck and costs. Whatever is left over (the residual) tells you how good your explanation is.
- **DV01 is the one number that explains most bond P&L:** dollars per 0.01 point × how far yields moved.
- **Coupon bonds are "shorter" than the dates they mature on.** That is why a cash-flow-matched ladder still lags its payments when yields fall.

---

## 11. Files (all under `attrib/`)
- `attribution_pack.md`: this file.
- **Tracking:** `attribution_tracking_template.csv` (template with the 7 and 19 Oct rows filled) and `attribution_tracking.csv` (appended by each run).
- **Scripts (`scripts/`):**
  - `attrib.py`, the main script, and `run_attrib.sh`, the one-command re-run;
  - `fetch_yahoo.sh`, `tracking_row.py`, `verify_attrib.py` (the independent check), `extras.py`, `make_synthetic_test.py`;
  - `indep_pricer.py` (copied unchanged from `oct20/numbers/scripts/`) and `trades.csv`.
- **19 Oct outputs (`out_1019/`):** `book_daily.csv`, `attribution_2026-10-19.csv`, `attribution_daily.csv`, `benchmarks_2026-10-19.csv`, `summary_2026-10-19.json`, `attrib_out_2026-10-19.txt`, `verify_out_2026-10-19.txt`, `extras_out_2026-10-19.txt`. The full-pipeline run (live re-fetch) is in `out_2026-10-19/`. The 7 Oct start is in `out_1007/`.
- **Data:**
  - `data/raw/tsy/` (treasury.gov, 19 Oct 22:27 UTC);
  - `data/raw/yahoo/` (copied from `oct20/numbers/data/prices/`, fetched 19 Oct 21:45 UTC);
  - `data/raw/nasdaq/` (history, quotes, dividends, 19 Oct 22:31-22:45 UTC);
  - `data/raw/run_*/` (the pipeline's own fetches);
  - `web/` (the CFA page and the iShares IEF and TLT pages).
