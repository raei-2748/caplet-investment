# Pre-trade check pack: every WInS trade the team might vote for (Tue 20 Oct 2026, ~09:30 Sydney)

> **Verified 20 Oct (`oct20/verify_trade/verify_trade.md`): PASS WITH CORRECTIONS; use its one-page go/no-go card (§5).** No card breaks a Wharton or Stock-Trak rule; every cash line reproduces. Main fix (E1): T1b's plan table double-counts the reserve - in the 3r plan ~78% comes from the floor (IBTM) and ~22% from VT, so the plan IBTM weight is 32.01% (not 31.55%). Selling 295 IBTM widens the IBTM gap to -1.7 points; selling ~231 keeps it at -1.2 and leaves ~$2,302 cash. Both are compliant; the team picks the size before the vote. T1c (scale 0.667) is not valid (use ~0.644). Bond STOP rule: implied yield more than 0.25 points from the treasury.gov par yield at 15 years, taken from the curve before the WInS price update (a pre-open price on Thu 29 Oct predates the FOMC). An under-funded buy can be shrunk OR "System Cancelled". Fallback pair: sale Mon 2 or Tue 3 Nov, bond the next evening; nothing after Wed 4 Nov 22:00. Largest positions: T6 IBTM 34.2%; T3 all bonds 45.0%. page.py now expires its cache after 1 hour.


**AI-generated research (Claude Code) for Team Caplet. Not for submission, and not a trade instruction.** It checks candidate
trades against this year's rules and does the cash arithmetic. It drafts no trade note, TNA, IPS or Final Report text. Only Ray
places or cancels WInS orders, and only after a logged team vote; no AI goes near WInS. If the team uses this pack, log it in
the AI-use record. No surnames, emails, birthdays or WInS username appear here.

Paths: `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/` (same for
`oct19/`). This folder: `oct20/tradecheck/`. Numbers: `data/tradecheck_out.json`, made by `scripts/tradecheck.py`.

---

## 0. Bottom line

1. **The 3r "option B" trade as written in the red team (§8) and the coupon study breaks the team's own cash rule.** Selling
   130-150 IBTM and buying 8 Nov-2041 bonds leaves **$94-$531 cash**, below the "keep at least $1,000" rule (Portfolio tab R31;
   R&B Tickets R7). That is not a Wharton breach (cash stays above $0), but it breaks the house rule. The version that mirrors
   the plan **sells about 295 IBTM and buys 8 bonds**, leaving about **$3,700**. The smallest IBTM sale that keeps $1,000 is
   172-174 shares.
2. **Every candidate passes the official instrument, price, volume and trade-count rules**, on the evidence available. IBTM, VT,
   IBTO-IBTR and the five T-bonds are already held, so they are WInS-listed. The Nov-2041 bond is a nominal coupon Treasury, not
   TIPS or STRIPS (both newly banned on the FAQ). Orders are at most 3.3% of the lowest daily volume in the last 21 days.
   - **Still UNVERIFIED:** WInS bond volume and the live WInS bond price.
   - **The Session Rules screenshot is still missing.** The position limit (200% per ETF; 100% per bond and for all bonds) is
     only a typed record from 29 Sep. A screenshot is still needed.
3. **Day trading.** Stock-Trak's FAQ defines it as buying and selling "the same stock on the same day". A same-day sell of IBTM
   plus a buy of a bond is therefore **not** a day trade on the platform's definition. Wharton's session definition is
   UNVERIFIED. The plan still uses **two different evenings**. The bond buy must wait until the IBTM sale has filled: buying
   first would need cash the account doesn't have, and WInS may then quietly shrink the order.
4. **Timing.** A two-order trade cannot be done safely in the one "last planned" slot (Fri 30 Oct 22:00 Sydney).
   - **Plan:** enter the sale **Thu 29 Oct 22:00 Sydney** (after the FOMC statement, Thu 05:00 Sydney, and the M6 go/no-go) and
     the bond **Fri 30 Oct 22:00 Sydney**.
   - **Fallback:** Tue 3 / Wed 4 Nov 22:00 Sydney.
   - **The clock change:** US clocks change on Sun 1 Nov. Sydney is ET + 15 h until then and ET + 16 h after.
5. **"No trade" remains a fully compliant baseline** for D1 options 1, 2, 3b and 1R, and for 3r option A. In those cases the
   job moves to words: one "about mirrors" clause, and the decision logged with the reason.
6. **Two traps found in tools and files:**
   - The shared fetch helper `oct16/tools/page.py` caches pages forever. It still serves the pre-16 Oct Trading page (with the
     "$5" stock rule). Fetch live with plain `curl` instead.
   - `snap/main/COMPETITION.md` §8 lists the Feb-2037 bond as 5.000%. The WInS ID and the note say **4.750%**.

---

## 1. The rules used, and how fresh they are

Fetched live with plain `curl` at **19 Oct 22:19 UTC (Tue 20 Oct 09:19 Sydney)**. Copies: `web/raw/*.html`, text in `web/*.txt`.
- **Trading Details (TRD)** = https://wghsinvcomp.smapply.us/res/p/trading/ ; **FAQ (FAQ)** = .../res/p/faqs/ ;
  **WInS page (WP)** = .../res/p/wins/. All three are **byte-identical in text to the compliance desk's 21:59 UTC fetch**
  (`oct20/compliance/web/sm_*.txt`), so nothing changed overnight.
- **Stale copies.** The repo copies in `snap/main/competition/official/2026_27/smapply_public_2026-10-14/` are out of date. They
  still say "$5", "10 weeks", and do not ban TIPS/STRIPS (compliance matrix Δ2-Δ6).
- **Platform pages, fetched 19 Oct 22:22 UTC:**
  - **UG** = 2026-27 WInS User Guide, https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf
    (`web/userguide.txt`). The PDF has stacked text layers from older years; which text is visible was checked earlier by
    `snap/main/research/insight_v1/phase_A/wins_week1_guardrails.md:31-35`.
  - **PFAQ** = Stock-Trak Wharton portal FAQ, https://edu.stocktrak.com/wharton/portfolio-faq/ (`web/pfaq.txt`). It is generic
    platform text, not season-specific.
- **SESS** = the Session Rules as a student typed them on 29 Sep (`snap/main/team/google_drive/sheets/portfolio_and_trading_notes/wins_notes.csv`).
  This is a record, not a screenshot.

| # | Rule | Exact source text | How this pack applies it | Status |
|---|---|---|---|---|
| R1 | Allowed instruments | "Exchange-Traded Funds: Any ETF available on WInS." "Treasury Bonds: Bonds available on WInS." (TRD:47-48). "Any Government/Treasury Bonds from any exchange available on WInS." NOT permitted: "TIPS", "STRIPS", "Anything other than the approved investments listed above." (FAQ:47, 54-56). Applies "for BOTH contributions, the IPS and Final Report" (FAQ:44) | Only already-held securities appear in any card, so all are on WInS. The 3.125% Nov-2041 bond is a nominal coupon Treasury (CUSIP 912810QT8 per R&B Tickets R15; WInS ID B-T-3.125-15112041 per the filed note) | PASS for every card |
| R2 | Stock price floor | Public pages now say only "Stocks: Any stock available on WInS." (TRD:46; FAQ:45). The "$5" was removed 16-19 Oct. SESS: "Minimum buy price $3.00" | Applies to stocks only. No card buys a stock. The ETFs trade at $21.87-$157 | n/a (PASS) |
| R3 | Volume | "no more than twice a security's current daily trading volume" (TRD:43). Platform, stricter: "we only allow users to trade up to half of the volume of any security" and "the volume in the real markets must be double the amount you are attempting to trade" (PFAQ:94, 102). UG p.10: you must be "trying to buy fewer shares than have actually traded in the market today" | Test against the **stricter** reading: order ≤ 50% of the day's volume. I use the lowest daily volume of the last 21 sessions as the yardstick | ETFs PASS (worst 3.3%). **Bonds UNVERIFIED** (WInS shows no bond volume) |
| R4 | Commission | "Each stock transaction is charged a flat $25 commission and treasury bonds are charged $10. Commission is charged only on a trade that clears." (FAQ:65) | $25 per ETF order (buy or sell), $10 per bond order | Applied |
| R5 | Day trading | UG p.6: "Day Trading: This is not permitted." SESS: "Day trading ... Not allowed". Platform definition: "Day trading is when you are able to buy and sell the same stock on the same day." (PFAQ:128) | **Never buy and sell the same security on the same US trading day.** Selling one security and buying a different one the same day is not a day trade on the platform definition. Wharton's own definition is **UNVERIFIED**, so cards use two evenings anyway | PASS (no card trades one security both ways) |
| R6 | Position limit | UG p.6: "Position Limit: This is how much of your portfolio you can invest in one single stock." SESS: "Stocks and ETFs: 200% per position and per security. Bonds: 100% per security and for all bonds". The platform default is 25% (PFAQ:95) | The largest position after any card is IBTM at 30-33%; all bonds stay at 29-42%. Indirect evidence: the 4,503-share IBTM order filled at about 32.5% of the book, so the live limit was above 32.5% on 7 Oct | PASS on SESS. **Screenshot UNVERIFIED** |
| R7 | Trade count | "up to 200 trades" (TRD:42). "Open and cancelled orders do not count" (PFAQ:139) | 11 used. The largest card adds 11 | PASS |
| R8 | Freeze | "ends on November 6, 2026. When trading ends, your portfolio will be frozen" (TRD:26) | Team buffer: no order entered after Wed 4 Nov 22:00 Sydney (`oct20/ops/operating_plan.md:217` [consistency fix 20 Oct, row 20]) | Timing table §6 |
| R9 | No margin, no shorting | NOT permitted: "Margin trading", "Short selling" (FAQ:49-50) | Never sell more units than are held. Never place a buy before the cash is there | PASS if sequenced (§6) |
| R10 | Trade notes | WP:45: "Complete a Trading Note when your team makes an investment decision." SESS: "300-character maximum (maxlength on the note box)". Notes cannot be edited, only added (`snap/main/COMPETITION.md:84`; assumed, not confirmed: treat as final, VTR E12) [consistency fix 20 Oct, row 18]. UG p.10: enter the note at "Review Order" | One new note per order, 300 characters or fewer, written by students. Checklist only (§5 of each card) | Applied |
| R11 | Fills | Orders placed while the market is closed "are filled at the security's opening price when the market reopens" (TRD:35). "Mutual funds and bonds are executed at end of day prices" (PFAQ:137). "The bond prices are updated once daily at U.S. market open" (FAQ:63) | ETF orders entered in the Sydney evening fill at the next US open. Bond fills appear after the US close. Exact bond fill timing is UNVERIFIED | Applied |
| R12 | Cash and buying power | "If you do not have adequate cash and/or buying power, then the number of shares will be adjusted to allow the trade to be filled as best it can." "Restricted funds are also created when you place a market order when the market is closed." (PFAQ:47, 107) | A buy placed before the sale's cash arrives may be **silently cut** to a smaller size. A wrong quantity may also fill at a wrong size rather than be rejected. This conflicts with competition/COMPETITION.md:85 ("WInS does not reserve cash for open orders"), so it is UNVERIFIED either way | Drives the two-evening sequence |
| R13 | "Required trading activity" | "teams must meet the required trading activity and portfolio management guidelines throughout the competition" (FAQ:80) | Not defined anywhere public. Not a reason to trade | **UNVERIFIED** (already in the Wharton question batch, `oct19/out/Caplet_Update_19Oct2026.md:372`) |
| R14 | WInS P&L | "WInS gains and losses should not be added to or subtracted from the client's long-term portfolio projections." (TRD:29) | No card is justified by WInS gains or losses | Applied |

House rules (team, not Wharton):
- Keep at least $1,000 cash (Portfolio tab R31; R&B Tickets R7).
- Only Ray trades (`snap/main/COMPETITION.md:193`).
- A trader plus a second student check every preview (`oct20/ops/operating_plan.md:78, 86` [consistency fix 20 Oct, row 20]).
- Every bond gets a yield check (competition/COMPETITION.md:95-96).

---

## 2. Inputs (live where possible)

**Current book.** All 11 orders filled on 7-8 Oct.
- ETFs: IBTM 4,503; IBTO 1,024; IBTP 927; IBTQ 894; IBTR 853; VT 167 shares.
- T-bonds, in units of $1,000 face: 20 × 4.750% Feb-2037, 20 × 4.500% May-2038, 18 × 4.375% Nov-2039, 18 × 4.250% Nov-2040 and
  20 × 3.125% Nov-2041.
- Cash $3,513.79. 11 of 200 trades used.
- Sources: `snap/main/COMPETITION.md:174-188` and `snap/main/ops/routines/portfolio_check.py:5-18`. The Feb-2037 coupon is
  4.750% per the WInS ID in `05_..._wins_trading_notes.md:16`, not competition/COMPETITION.md's 5.000%.

**ETF prices and volume.** 19 Oct 2026 US close. Two sources:
- Yahoo chart API, fetched by the numbers desk at 19 Oct 21:45 UTC. Copied to `data/prices_numbers_2145utc/`.
- My own Yahoo calls returned HTTP 429 at 22:20-22:25 UTC. I cross-checked with the Nasdaq API at about 22:27 UTC
  (`data/alt/`): IBTM close $21.865, volume 160,242; VT close $157.12. These match Yahoo to the cent and the share count.

| ETF | 19 Oct close | 19 Oct volume | Lowest daily volume, last 21 sessions | Median |
|---|---|---|---|---|
| IBTM | $21.865 | 159,350 | 85,700 | 268,100 |
| IBTO | $23.135 | 161,698 | 66,600 | 174,400 |
| IBTP | $24.235 | 241,308 | 51,000 | 93,000 |
| IBTQ | $23.850 | 79,222 | 45,200 | 118,600 |
| IBTR | $23.651 | 20,041 | 17,000 | 72,000 |
| VT | $157.11 | 2,101,558 | 1,167,700 | 2,629,900 |

**Bond prices are MODEL. The WInS price is UNVERIFIED.**
- **Curve:** treasury.gov par curve of **19 Oct 2026**, re-fetched 19 Oct 22:25 UTC (`data/tsy_202610_fetch.csv`). The 20 Oct row
  was not yet published.
- **Method:** a bootstrap with `scripts/indep_pricer.py`, rolled to a **30 Oct settlement**, which is when any order would fill.
- **"WInS est."** = model price + that bond's WInS fill-minus-model gap at the 7 Oct fills. The 7 Oct curve and an 8 Oct
  settlement reproduce the numbers desk's gaps exactly (−0.552 for Nov-2041).
- **Cross-check:** a second price off the interpolated par yield ("street check") lands within 0.1-0.3 points.

| Bond | Model clean | WInS est. clean | Accrued (30 Oct) | Model yield | WInS est. yield | Par curve at that maturity | Cost per unit (WInS est., incl. accrued) |
|---|---|---|---|---|---|---|---|
| 4.750% Feb-2037 | 96.666 | 97.050 | 0.981 | 5.169% | 5.120% | 5.161% | $980.31 |
| 4.500% May-2038 | 93.833 | 94.244 | 2.054 | 5.219% | 5.169% | 5.209% | $962.99 |
| 4.375% Nov-2039 | 91.553 | 91.330 | 1.997 | 5.279% | 5.305% | 5.266% | $933.27 |
| 4.250% Nov-2040 | 89.501 | 89.148 | 1.940 | 5.320% | 5.359% | 5.304% | $910.88 |
| **3.125% Nov-2041** | **76.967** | **76.415** | **1.427** | **5.377%** | **5.441%** | **5.342%** | **$778.42** (model $783.94) |

- **Check against the numbers desk:** Nov-2041 model clean 76.965 with accrued 1.342 at a 20 Oct settlement, the same as
  `oct20/numbers/data/book_value_out.txt`.
- **Rate sensitivity:** one Nov-2041 unit moves about **$0.87 per 0.01 point** of yield, so 8 units move about $7.
- **Book value now:** about **$303.5k** (Yahoo ETFs, WInS-est. bonds, accrued to 30 Oct). Whether WInS counts accrued interest
  is UNVERIFIED.

**Yield-check table for the 3.125% Nov-2041 bond** (clean price → yield to maturity, 30 Oct settlement; `t41_yield_table`):

| Clean | 75.50 | 75.75 | 76.00 | 76.25 | 76.50 | 76.75 | 77.00 | 77.25 | 77.50 | 77.75 | 78.00 | 78.50 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yield % | 5.548 | 5.518 | 5.489 | 5.460 | 5.431 | 5.402 | 5.373 | 5.345 | 5.316 | 5.288 | 5.259 | 5.203 |

**Scale.** WInS = Laura's plan on 2 Jan 2028 × **0.644** (300,000 / 465,797; `oct20/charts/charts_data_pack.md:311`). The kits
round this to about 0.643 (`oct19/ipskit/ips_writing_kit.md:318`). The coupon study used 300/450 = 0.667
(`oct19/coupon/coupon_risk_options.md:155`). **Pick one and say which.** This pack uses 0.644 [withdrawn: 0.667 is not valid per the banner; use about 0.644; consistency fix 20 Oct, row 19], with 0.667 shown where it changes
the order.

---

## 3. Summary table

"Cash after" uses 19 Oct closes and WInS-est. bond prices; recompute live. "Notes hit" = filed WInS notes the trade contradicts
or leaves incomplete. Every card passes R1-R4 and R7 (rules R2 and R5 are n/a or pass by design; bond volume is UNVERIFIED in
every bond card).

| Card | Comes from | Orders (each needs a new note) | Fees | Trades after | Cash after | ≥ $1,000? | Mirrors the plan? | Notes hit | Verdict (AI view; the team decides) |
|---|---|---|---|---|---|---|---|---|---|
| **T0** No trade | D1 options 1, 2, 3b, 1R; 3r option A; D7 7a/7c; D9 9a | 0 | $0 | 11 | $3,514 | Yes | Yes for 1, 2, 3b, 1R. "About mirrors" for 3r (the reserve's 2.1% sits inside IBTM) | Option 2 only: the VT note's "only" (words, not a trade) | **Compliant baseline** |
| T1a 3r-B as written | Red team §8; coupon study :156 | Sell 130-150 IBTM; buy 8 Nov-41 | $35 | 13 | **$94-$531** | **No** | Partly (the reserve is funded half from cash) | None | **Do not enter as sized** |
| **T1b** 3r-B, plan-mirror sizing | This pack | Sell 295 IBTM; buy 8 Nov-41 | $35 | 13 | **$3,702** | Yes | Yes (IBTM 30.3% vs plan 31.5%, the same −1.2-point gap as today; Nov-41 7.18% vs 7.25%) | None (the new job needs the new note) | **Use this if option B wins** |
| [withdrawn: banner; consistency fix 20 Oct, row 19] T1c 3r-B at scale 0.667 | Coupon study scale | Sell 322 IBTM; buy 9 Nov-41 | $35 | 13 | $3,514 | Yes | Yes at 0.667 | None | Only if the team adopts 0.667 everywhere |
| T1e 3r-B, exact split | Coupon model funding (§4) | Sell 229 IBTM; sell 9 VT; buy 8 Nov-41 | $60 | 14 | $3,648 | Yes | Exactly (the model takes about 78% from the floor, 22% from VT) | Touches VT (a third note) | More exact, one more trade and note. Complexity probably does not earn its place |
| T2 3r half-measure | Red team §8 "avoid" | Buy 3 (or 4) Nov-41 from cash | $10 | 12 | $1,169 (4 bonds: **$390**) | 3 Yes / 4 **No** | No (matches neither the plan nor the book) | None | **Avoid** |
| T3 Option 4, dedicated rebuild | Coupon study :160-162 | Sell 1,138 IBTM, all 1,024 IBTO, 310 IBTP; buy 131 IBTQ, 233 IBTR, +8/+9/+12/+13/+12 bonds | $175 | 21 | $1,898 | Yes | Yes, but to a different plan | **IBTO, Nov-39, Nov-41, IBTR** (study §4) | Compliant but high-risk to execute; keep as the Final Report alternative |
| T4 D7 7b, Book L | Update D7; Book L tab | Sell 2,820 IBTM and all 167 VT; buy 485 IBTO, 440 IBTP, 423 IBTQ, 404 IBTR, +10/+9/+9/+8/+9 bonds | $200 | 22 | $8,521 | Yes | Mirrors Laura's **2027** book, not the 2028 plan | **VT, IBTM** (floor) | Compliant; contradicts two filed notes and the 29 Sep choice |
| T5 D9 9b, smaller floor | Update D9 | Per $10k of Laura's floor moved: sell 295 IBTM, buy 40 VT | $50 | 13 | $3,630 | Yes | Yes, if D9b is voted | **IBTM, VT** (Update D9) | Compliant; a strategy reopen 10 days before the freeze |
| T6 Trim VT to 6.9% | c5 mapping (+1.7 points); not proposed by any file | Sell 34 VT; buy 242 IBTM | $50 | 13 | $3,514 | Yes | Matches the 19 Oct model weights | None directly | Not recommended ("about 9% is WInS, about 7% is Laura" is already explained) |

---

## 4. Cards

Each card follows the same five checks: (1) rules, (2) cash, (3) consistency with the filed notes and the plan ratio, (4) what
a new trade note must cover (a checklist, not text), (5) order entry. The common order-entry steps and the timing table are in
§6; cards list only what differs.

### T0: No trade (baseline)

**Covers:** D1 option 1 (state only), option 2 (Laura's half in VT to 2042), 3b (reserve in IBTM), 1R (re-match in 2033) and
3r option A ("about mirrors"); D7 7a/7c; D9 9a.

**(1) Rules.**
- Nothing to check in WInS.
- Holding is allowed. The WInS page says teams are not judged on "How many trades you make" (WP:25), and the FAQ warns against
  "a lot of buying and selling" (FAQ:41).
- The undefined "required trading activity" (FAQ:80, R13) is UNVERIFIED. Do not trade just to meet it; ask Wharton (batch 2).

**(2) Cash.**
- $3,513.79 = 1.16% of about $303.5k. That is within the 1.1% target (Portfolio tab R13).
- Cash will rise slightly if WInS credits the early-November iBond distributions. Their size and date in WInS are UNVERIFIED
  (`oct19/out/Caplet_Update_19Oct2026.md:430`). Don't count on them.

**(3) Consistency.**
- **Options 1, 3b and 1R:** WInS already mirrors the plan.
  - 3b keeps the reserve in IBTM, the same holding as the floor, so only the Sheet's IBTM split (R37-39) changes.
  - 1R changes nothing until 2033.
- **3r option A:** WInS does not show the reserve.
  - In the plan it is about $10k × 0.644 = $6.4k, or **2.1% of the book**, sitting inside IBTM in WInS.
  - The IPS must say "about mirrors", not "matches" (red team §8; `oct19/ipskit/ips_writing_kit.md:327`).
  - The Final Report needs one line saying where the 2% sits.
  - The risk a judge finds: a named reserve that isn't in the book.
- **Option 2:** no trade is needed, but the filed VT note says the stocks "only set how far her gift rises above her promised
  minimum" (`05_...notes.md:14`). Under option 2, VT also backs the payments to 2042. That conflict is fixed in words (the VT
  reflection or the Final Report), never by editing the note (notes cannot be edited).
- **"Add Note" to an existing trade.** WInS allows notes to be added to past orders (SESS "Adding notes"; PFAQ:29). Do **not** add
  any note to the IBTM, IBTR or VT trades before the TNA is submitted (23 Oct ET). The TNA quotes notes "exactly as it appears
  in WInS" (TNA:44), and an added note could change what "exactly" means. After 24 Oct, how an added note displays and whether
  judges see it is UNVERIFIED. Treat it as permanent.

**(4) What to record instead of a note.** A decision-log entry, which is what WP:45 asks for in spirit:
- [ ] Date and meeting (M5, Tue 27 Oct, or M6, Thu 29 Oct).
- [ ] The option chosen and the alternatives voted down.
- [ ] Why no trade (for example: the strategy is unchanged in WInS terms, or the cost and note risk outweigh a 2% difference).
- [ ] How the IPS and Final Report will describe any gap between plan and book.
- [ ] Any dissent, by role.

**(5) Order entry.** None. Still do the freeze-day saves (§6, step 9).

### T1a: 3r option B as written (sell about 130-150 IBTM, buy about 8 Nov-41): do not enter as sized

**(1) Rules:** the same as T1b; every Wharton rule passes.

**(2) Cash: fails the house rule.**

| Step | Amount | Cash after |
|---|---|---|
| Start | | $3,513.79 |
| Sell 150 IBTM at $21.865, less $25 | +$3,254.75 | $6,768.54 |
| Buy 8 × 3.125% Nov-2041 at $778.42 (WInS est., incl. accrued), plus $10 | −$6,237.36 | **$531.18** |

- With 130 IBTM, cash ends at **$93.88**. At the model bond price ($783.94) it is about $44 lower.
- **Where the figure came from:** "buy 4 from idle cash and sell about 150 IBTM" (`oct19/coupon/coupon_risk_options.md:156`). It
  uses idle cash as if it were spare. The red team itself notes that cash alone breaks the rule "past about 3 bonds" (§8). The
  combined plan breaks it too.

**(3) Plan ratio:** about half the reserve comes from WInS cash, the analogue of the 2027 leftover, rather than from the floor.
That is not what 3r says ("$10k of the 2028 deposit before the floor").

**Fix:** use T1b.

### T1b: 3r option B, plan-mirror sizing (sell 295 IBTM, then buy 8 Nov-41): the version to use if option B wins

**(1) Rule check.**

| Rule | Check | Result |
|---|---|---|
| R1 instrument | IBTM is an ETF on WInS (held; name "iShares iBonds Dec 2032 Term Treasury ETF", SEEN 29 Sep, R&B Tickets R14). The 3.125% 15-Nov-2041 is a US Treasury bond on WInS (held, B-T-3.125-15112041), nominal, not TIPS or STRIPS | PASS |
| R2 price floor | Stock rule only; IBTM $21.87 | n/a |
| R3 volume | 295 shares = 0.34% of IBTM's lowest daily volume in 21 sessions (85,700) and 0.18% of 19 Oct volume. Far inside both the 2× and the stricter 50% rule. An order entered before the open fills "shortly after the market opens and contingent to trading volume" (PFAQ:114), so it may wait a few minutes after 09:30 ET while volume builds | PASS |
| R3 bond volume | WInS shows none. Earlier orders of 18-20 units filled. 8 units is smaller | **UNVERIFIED** (low risk) |
| R4 fees | $25 + $10 = $35 | Applied |
| R5 day trading | The sale (IBTM) and the buy (bond) are different securities. Planned on two different US days anyway. Never buy back IBTM on the sale day (for example to "fix" an error) | PASS |
| R6 position limit | After the trade: IBTM 30.3%, Nov-41 7.2%, all bonds about 31% | PASS on SESS (screenshot UNVERIFIED) |
| R7 trades | 13 of 200 | PASS |
| R8 freeze | Both fills by Fri 30 Oct ET in the base plan | PASS if timed per §6 |
| R9 shorting | Sell 295 ≤ 4,503 held. Choose **Sell**, never "Short" | PASS if checked |
| R12 buying power | The bond buy is placed only after the sale shows Filled and cash ≥ $7,300 | Sequenced |

**(2) Cash arithmetic** (19 Oct closes; WInS-est. bond; recompute on the night).

| Step | Amount | Cash after |
|---|---|---|
| Start | | $3,513.79 |
| Sell 295 IBTM at $21.865 (= $6,450.17), less $25 | +$6,425.17 | $9,938.96 |
| Buy 8 units (= $8,000 face) of the 3.125% Nov-2041 at 76.415 + 1.427 accrued = $778.42 each (= $6,227.36), plus $10 | −$6,237.36 | **$3,701.60** |

- **At the model price** ($783.94): **$3,657**.
- **Stress:** if WInS quotes the bond 1.5 points richer than estimated (a stale or rich price), cash is still **$3,582**.
- **Sizing:** $10,000 × 0.644 = $6,440 ÷ $778 = 8.27 → **8 bonds**, rounded down as the Sheet does (R19 note). 295 IBTM shares =
  the same $6,440, so cash ends about where it is now.
- [withdrawn: banner; consistency fix 20 Oct, row 19] **At scale 0.667:** 8.56 bonds, so either 8 bonds (T1b) or 9 bonds with 322 IBTM (T1c). Both keep about $3.5k cash.
- **Smallest IBTM sale that keeps $1,000 with 8 bonds:** 172 shares (WInS est.) to 174 (model). Anything between 174 and 295 is
  compliant but shifts part of the reserve's funding onto cash (see T1a).

**(3) Consistency.**
- **With the filed notes:**
  - IBTM (10/06 10:01:41 PM ET): "does two jobs ... supports her first $50,000 payment and provides a floor". It stays true. The
    Sheet's split becomes 1,142 payment shares + **3,066** floor shares, down from 3,361 (Portfolio tab R38-39).
  - Nov-2041 (10/06 07:55:45 PM ET): "supports her final $50,000 payment ... with reinvested coupons funding part of each". It
    stays true for the original 20 units. The 8 new units carry a new job that this note does not mention, so the new note must
    say it.
  - VT: unaffected.
  - The three TNA picks (IBTM, IBTR, VT) are unaffected. The trade comes after the TNA is due (23 Oct ET).
- **With the plan ratio (scale 0.644):**

| | Plan with 3r, scaled | WInS before | WInS after T1b |
|---|---|---|---|
| IBTM (payment + floor) | 31.55% ((156,947 − 10,000) / 465,797) | 32.44% (plan without 3r: 33.69%) | 30.32% |
| Nov-2041 (2042 rung + reserve) | 7.25% ((23,779 + 10,000) / 465,797) | 5.13% | 7.18% |
| VT | 6.44% (plan VT less the $2.2k the model takes from it; see T1e) | 8.65% | 8.65% |
| Cash | 0.64% (2027 leftover) | 1.16% | 1.22% |

  - IBTM's gap to the plan is about −1.2 points before and after, so the trade moves WInS with the plan.
  - VT's +1.7-point gap is older and unrelated: the book was sized on the insight_v1 weights (Portfolio tab R10-R12; `oct20/charts/charts_data_pack.md:311-314`).
  - Plan figures are from `oct20/charts/c5_wins_vs_plan_mapping.csv` (MODEL).
- **With the IPS text.** V5 says each payment's liquidity "comes from a maturity, not a sale" (red team §7). The reserve is a sale
  exception, so the words must change whether or not the team trades. The trade itself does not create the conflict.

**(4) What each new note must factually cover** (two notes, one per order; 300 characters or fewer including spaces; students
write them; a second student counts the characters; paste as plain text with straight apostrophes; cannot be edited).

Sell IBTM:
- [ ] What: a sale of part of IBTM (say it is a re-allocation inside Laura's plan, not a view on rates or profit-taking).
- [ ] Why now: the logged team decision (the date and the option's name as the team calls it).
- [ ] Where the money goes: the paired Nov-2041 Treasury order.
- [ ] What IBTM still does: both jobs (the 2033 payment and the floor), with a smaller floor. This keeps the filed IBTM note true.
- [ ] That WInS mirrors Laura's 2028 plan scaled down (one clause), if room allows.
- [ ] No WInS gain or loss as a reason (TRD:29).

Buy Nov-2041:
- [ ] Which bond, named as in the filed note (3.125% Treasury maturing 15 Nov 2041) and the quantity.
- [ ] Its new job: a reserve against reinvested income earning less than planned, protecting the ten payments.
- [ ] That it is separate from the 2042 rung already held (20 units), so there are two jobs in one holding, like IBTM.
- [ ] Where it comes from in Laura's plan: the 2028 deposit, before the floor. It is not counted in the 2031 minimum (if that is
  what the team voted).
- [ ] Why this holding, in words the team can defend: it is held to 2041 so its own money keeps today's yield. The red team says
  the locked yield, not the price rise, is the main effect (§2a).
- [ ] What happens to any unused part (released in 2033 or returned to Laura), per the vote.
- [ ] A yield check was done, **only if it was** (as in the Nov-2040 note's "consistent with the Treasury yield curve").
- [ ] **Do not claim** "guaranteed", "risk-free", "zero shortfalls in history", "does the job of $25k", "its price rise covers the
  gap" or any Laura quote (red team §10; `snap/main/COMPETITION.md:166-168`).
- [ ] 300 characters cannot hold all of this. Prioritise the job, the source and why this bond. The Final Report carries the rest.

**(5) Order entry.**
- Common steps are in §6.
- **Sale:** a Day **limit** sell at about 0.3% below the last close (for example $21.80 on a $21.865 close). It fills at the open
  in a normal market. If it does not fill, it expires and is re-entered the next evening. Whether a Day limit entered before the
  open stays valid for that session is UNVERIFIED; check it shows "Open" in Order History. A market order is acceptable for a
  $6k ETF sale (295 × $0.05 = $15 of price risk), but the house quirk list says iBond quotes outside hours are wide
  (competition/COMPETITION.md:100), so a limit is the safer habit.
- **Bond:**
  - Bond order types in WInS are UNVERIFIED (probably market at the daily price). The yield check replaces a limit.
  - **Pass** if the WInS clean price is in roughly **76.0-77.5** on a 19-Oct-like curve. That is a 5.49-5.32% yield against about
    5.34% on the par curve and 5.38% on the bootstrap. Re-read both on the night.
  - **Stop** if the implied yield is more than 0.25 points from the curve. Two WInS bonds had stale prices about 1 point off
    (competition/COMPETITION.md:95-96).
  - Check the last coupon date shows **15 May 2026** and the accrued is about $14.3 per $1,000. WInS mis-dated the May-2038 bond's
    coupon (competition/COMPETITION.md:97).
- **Timing:** sale Thu 29 Oct 22:00 Sydney → check the fill and cash Fri 30 Oct after 07:00 Sydney → bond Fri 30 Oct 22:00 Sydney
  → check Sat 31 Oct after 07:00 Sydney. Fallback: Tue 3 Nov and Wed 4 Nov, 22:00 Sydney.
- **Do not sell IBTM if the bond fails the check that evening.** Check the bond screen first: a pre-open check shows the previous
  day's price. A sale with no bond buy leaves about $9.9k (3.3%) idle cash and a sale note that is no longer true.

### [withdrawn: banner; consistency fix 20 Oct, row 19] T1c: 3r option B at scale 0.667 (sell 322 IBTM, buy 9 Nov-41)
- **Rules:** as T1b (322 shares = 0.38% of the lowest volume).
- **Cash:** $3,513.79 + $7,040.53 − $25 − $7,005.78 − $10 = **$3,513.54**.
- **Plan:** mirrors the plan only at 0.667. The book was built at about 0.644 (charts pack §5), so using 0.667 for one holding
  mixes two scales. Choose this only if the team states 0.667 everywhere.
- **Notes and entry:** as T1b, with 9 bonds.

### T1e: 3r option B, exact model split (sell 229 IBTM and 9 VT, then buy 8 Nov-41)
- **Why it exists.** In the coupon model the reserve cuts the floor's face target by $10k, and IBTM is bought at its present
  value: `R = 150_000 - gap27 - buffer`; `ibtm_cost = R / (1 + yF/200)**(2*tF)`; VT gets the rest
  (`oct19/coupon/scripts/coupon_options.py:181-191`).
  - With the floor cost ratio 116,830 / 150,000 (`oct19/out/Caplet_Update_19Oct2026.md:256`), about 78% of the $10k comes out of
    IBTM ($7.8k) and 22% out of VT ($2.2k).
  - Scaled: IBTM −$5,016 (229 shares) and VT −$1,424 (9 shares).
- **Rules:** as T1b, plus a VT sale (9 shares, well under 0.01% of volume). Sell 9 ≤ 167 held. Still no security bought and sold
  on the same day.
- **Cash:** $3,513.79 + $5,007.08 − $25 + $1,413.99 − $25 − $6,237.36 = **$3,647.50**. Fees $60, 14 trades used.
- **Consistency:**
  - This is the most exact mirror.
  - It touches VT, so a **third** note is needed. That note must reconcile with the filed VT note ("A fall can shrink the extra").
- **AI view:** the ~$1.4k precision gain is small next to VT's existing +1.7-point gap, so it probably does not earn a third trade
  and note. Say "about mirrors" instead.

### T2: 3r half-measure (buy 3-4 Nov-41 from cash only): avoid
- **Rules:** pass (a bond buy only).
- **Cash:** 3 bonds leave **$1,168.53** (passes, barely); 4 bonds leave **$390.11** (fails the house rule).
- **Consistency:** it matches neither the plan nor the book (red team §8: "Avoid the half-measure"). The note would have to explain
  a reserve at half size.

### T3: Option 4, dedicated (cash-flow-matched) rebuild: compliant, but expensive to execute and in words

**Orders.** From `oct19/coupon/coupon_risk_options.md:160-162` (16 Oct prices, scale 0.667 [withdrawn: banner; recompute at about 0.644; consistency fix 20 Oct, row 19]). **Recompute the linear programme
live at the chosen scale before any vote.**
- Sell 1,138 IBTM, all 1,024 IBTO and 310 IBTP.
- Buy 131 IBTQ and 233 IBTR.
- Buy +8 Feb-37, +9 May-38, +12 Nov-39, +13 Nov-40 and +12 Nov-41 bonds.

**(1) Rules.**
- All instruments are held, so they are listed.
- **Volume:** the largest is 1.5% of the lowest 21-session volume (IBTO 1,024 vs 66,600; IBTR 233 vs 17,000 = 1.4%), so ETFs pass.
  Bonds of 8-13 units are UNVERIFIED.
- **Fees:** 5 ETF orders × $25 + 5 bond orders × $10 = **$175**. 21 of 200 trades.
- **Day trading:** no security is on both sides.
- **Position limit:** passes.
- **Sequencing:** all three sales must fill before any buy (R12).

**(2) Cash.** +$56,010 net from the sales, then −$8,685 on ETFs and −$48,941 on bonds, both including fees. Cash ends at
**$1,898.07** (passes). The ladder costs about $1.9k × scale more, so cash falls.

**(3) Consistency.**
- **It contradicts four filed notes:**
  - IBTO "is for Laura's second $50,000 payment" (`05_...notes.md:20`; the whole holding would be sold);
  - Nov-2039 "reinvested coupons fund the rest" (`:18`);
  - Nov-2041 "with reinvested coupons funding part of each" (`:24`);
  - the IBTR rung changes size (`:15`).
- The frozen book would show **no holding for the 2034 payment** and only part of 2033. Judges compare WInS with the notes, so
  each of the 10 new notes must explain a reversal.
- **Execution risk:** 10 orders across at least two evenings, by one trader, after the 7 Oct mis-click.
- The May-2038 bond's accrued interest in WInS is mis-dated (competition/COMPETITION.md:97), so its preview total will differ from the model.
  Check it.

**(4) Notes (10).**
- [ ] Each sale names the payment it used to fund and why that money now comes from later coupons.
- [ ] Each buy names its payment.
- [ ] The principle "income from later Treasuries pays earlier payments" appears consistently.
- [ ] Nothing says a filed note was wrong unless the team believes it.

**(5) Entry.**
- Two evenings at least: sales first, then buys.
- Twenty preview checks.
- Not feasible inside the single Fri 30 Oct slot.

**AI view:** keep it as the Final Report's tested alternative (coupon study §4).

### T4: D7 option 7b, switch to "Book L" (Laura's first $300k only, all bonds)

**Orders.** Book L share and face counts (Book L tab R14-R23) were sized on **28 Sep prices**; recompute live.
- Sell 2,820 IBTM and all 167 VT.
- Buy 485 IBTO, 440 IBTP, 423 IBTQ and 404 IBTR.
- Buy +10/+9/+9/+8/+9 units of the five bonds.

**(1) Rules.**
- All listed.
- **Volume:** largest 3.3% (IBTM 2,820 vs 85,700) and IBTR 2.4% (404 vs 17,000). ETFs pass; bonds UNVERIFIED.
- **Fees:** 6 × $25 + 5 × $10 = **$200**. 22 of 200 trades.
- No security on both sides. Sales before buys.

**(2) Cash.** +$87,897 gross from the sales, −$82,690 on purchases, −$200 fees. Cash ends at **$8,520.60** (2.8% of the book; Book
L's own design leaves 2.9%).

**(3) Consistency.**
- **Contradicts:**
  - the VT note (the whole stock fund is sold);
  - the IBTM note (the "floor for her facility contribution" leaves the book);
  - the 29 Sep choice of book (ii)R (`oct19/ipskit/ips_writing_kit.md:328`).
- **Plan ratio:** WInS would mirror Laura's 1 Jan 2027 book (scale 1.0), not the 2028 plan. That is a defensible alternative only
  if the IPS says so in one clause.

**(4) Notes (11).** Each must say the book now shows Laura's first deposit, not the 2028 plan, and why the team changed its mind.
- [ ] Never cite the WInS loss on VT (−$287 at 19 Oct) as a reason (TRD:29).

**(5) Entry.** As T3: at least two evenings and 22 preview checks.

**AI view:** compliant, but a late reversal with two contradicted notes.

### T5: D9 option 9b, smaller floor, more VT (per $10k of Laura's floor moved)
- **Orders:** sell 295 IBTM, buy 40 VT. Scale linearly for other sizes; the size is unknown until voted.
- **Rules:**
  - Both listed.
  - Volume is tiny (VT 40 vs 1.17m).
  - $50 in fees; 13 trades.
  - Different securities on each side.
- **Cash:** $3,513.79 + $6,425.17 − $6,309.40 = **$3,629.56**.
- **Consistency:**
  - The Update flags conflicts with the IBTM and VT notes (`oct19/out/Caplet_Update_19Oct2026.md:335`).
  - The IBTM floor shrinks and VT's role grows, so the VT note's "only set how far her gift rises" stays true, but the IBTM
    note's floor becomes smaller than the minimum figure argued in the TNA.
  - It is a strategy reopen 10 days before the freeze (risk R11 in `oct20/ops/operating_plan.md:328` [consistency fix 20 Oct, row 20]).
- **Notes:**
  - [ ] Each note says the decision changes the floor-versus-growth split.
  - [ ] Each says why: the team's own trade-off argument.
  - [ ] Each says what it costs in the bad case.
- **Entry:** sale first, then buy, on different evenings.

### T6: Trim VT to the 19 Oct model weight (6.9%): not proposed by any file; listed for completeness
- **Orders:** sell 34 VT, buy 242 IBTM. $50 in fees; 13 trades.
- **Cash:** **$3,514.20**.
- **Rules:** pass.
- **Consistency:**
  - The book was sized on the insight_v1 weights (VT 8.7%, Portfolio tab R12). The 19 Oct model plan has VT at 6.9%. The
    difference comes from model vintages, not drift.
  - The team's line "about 9% is WInS, about 7% is Laura" (`oct19/out/Caplet_Update_19Oct2026.md:261`) already explains it.
  - A trade now would need a note admitting the target changed.
- **AI view:** not worth a trade.

---

## 5. Note checklist for any new order (applies to every card)
- [ ] Students write it, not AI (Wharton AI policy; `snap/main/CLAUDE.md:12-14`). AI may only check facts after it is written.
- [ ] 300 characters or fewer, including spaces. Count it twice in a plain-text editor. Curly apostrophes count as one character,
  but they cause paste mismatches later (`oct19/out/Caplet_Update_19Oct2026.md:61`).
- [ ] It records "the reasoning, research, and intended strategic role of each decision at the time it is made" (WP:45). Write it
  for the order, not for the TNA.
- [ ] It links to Laura's goal (which payment, or the floor, or the reserve) and to the logged decision.
- [ ] Every number in it is one the team can source in the Final Report. Otherwise, no number.
- [ ] Saved in the Sheet (Trade Log, note column) **before** entry, and pasted from there into WInS.
- [ ] It does not contradict a filed note. If it reverses one, it says so honestly.

---

## 6. Order-entry checklist and timing

**Before the evening (trader + second student = the trade-log keeper):**
1. **A logged vote exists.** The order has a decision-log ID with the date, option, count and dissent (`oct20/ops/operating_plan.md:322`, R5 [consistency fix 20 Oct, row 20]).
2. **Session Rules screenshot,** with the username cropped. Capture the position limit, day-trading line, minimum price,
   commission and trade count. It is still missing, and the public rules changed twice in 14-19 Oct (compliance matrix row 43).
3. **Search each security in WInS.** Read the full name (IBTM = "Dec 2032"; not IBTN, which is a different company). For the bond,
   check the coupon (3.125%, not the 2.000% of the same date), maturity 15 Nov 2041, last coupon 15 May 2026 and accrued.
4. **Re-run** `scripts/tradecheck.py` with that day's treasury.gov curve and closes. Write the expected quantities, the preview
   totals (±$100) and the cash after each order on the ticket.
5. **Order History shows no open orders.** The FAQ's "restricted funds" versus the team's observation that cash is not reserved is
   UNVERIFIED.
6. **The notes are final** in the Sheet and character-counted.

**At entry (each order):**
7. **Preview check, read aloud to the second student** (in person or on a call). The second student says "confirm" before the
   trader presses it. They check:
   - action **Sell** or **Buy** (never Short or Cover);
   - the ticker or bond ID;
   - the quantity;
   - for bonds, the unit: competition/COMPETITION.md:82 says units of $1,000 face, but the Sheet's R19 note says face dollars. The **preview
     total** decides: about $6.2k for 8 bonds, not $62 or $6.2m. The platform may fill a wrong quantity "as best it can" rather
     than reject it (PFAQ:47);
   - the order type and limit;
   - commission ($25 or $10);
   - the estimated total within ±$100 of the ticket;
   - the note pasted.
8. **For a sell-then-buy pair, place the buy only after the sale shows Filled** and cash ≥ buy total + $1,000.

**After:**
9. Screenshot Order History (Filled), Transaction History and the Trade Notes page.
10. Fill the Trade Log row. Use the Portfolio tab's exact holding names so the "Trades outside the plan" counter (R7) does not
    miscount: its formula matches names, and bond strings differ (`oct19/out/Caplet_Update_19Oct2026.md:162`).
11. Update units held. For T1b: IBTM 4,208; Nov-2041 28 units, split 20 (2042 rung) and 8 (reserve).
12. Compare WInS cash with the ticket. Log any difference.
13. Save all WInS records before the 6 Nov close and again after the freeze.

**Timing (US clocks change Sun 1 Nov; Sydney is on AEDT throughout).** Conversions computed with the IANA zones
America/New_York and Australia/Sydney.

| Sydney | ET | What happens |
|---|---|---|
| Tue 27 Oct 20:00 | Tue 27 Oct 05:00 EDT | M5 vote set B (D1, D7, D9) |
| Thu 29 Oct 05:00 | Wed 28 Oct 14:00 EDT | FOMC statement, usually 2:00 pm EDT (the time is UNVERIFIED; the calendar gives dates only; meeting 27-28 Oct, federalreserve.gov calendar, read 19 Oct 22:30 UTC) [consistency fix 20 Oct, row 21] |
| Thu 29 Oct 20:00 | Thu 29 Oct 05:00 EDT | M6 go/no-go and re-price (`operating_plan.md:116` [consistency fix 20 Oct, row 20]) |
| **Thu 29 Oct 22:00** | Thu 29 Oct 07:00 EDT | **Enter order 1 (the sale).** It fills at the 09:30 EDT open = Fri 30 Oct 00:30 Sydney |
| Fri 30 Oct after 07:00 | after Thu 16:00 EDT close | Check the fill and cash |
| **Fri 30 Oct 22:00** | Fri 30 Oct 07:00 EDT | **Enter order 2 (the bond),** the team's last planned slot. The fill shows after the 16:00 EDT close = Sat 31 Oct 07:00 Sydney |
| Sun 1 Nov | 02:00 EDT → 01:00 EST | US clocks go back. From now on Sydney = ET + 16 h; the US open is 01:30 and the close 08:00 Sydney |
| Mon 2 / Tue 3 Nov 22:00 | 06:00 EST the same day | Fallback slots (fills that ET day; check the next morning after 08:00 Sydney) |
| **Wed 4 Nov 22:00** | Wed 4 Nov 06:00 EST | **Last fallback entry** (`operating_plan.md:217` [consistency fix 20 Oct, row 20]). Fill confirmed Thu 5 Nov 08:00 Sydney |
| Sat 7 Nov 08:00 | Fri 6 Nov 16:00 EST | WInS freezes. Any order still open never fills |
| Sat 7 Nov 09:00 | Fri 6 Nov 17:00 EST | IPS deadline |

---

## 7. What is still UNVERIFIED (and who checks it, by role)
1. **Session Rules:** the position limit, the day-trading definition and the $3 minimum, as of now (rules lead + trader;
   screenshot before any order).
2. **Live WInS price, accrued interest and last coupon date** of the 3.125% Nov-2041 (trader, on the night). Every bond price in
   this pack is MODEL.
3. **The WInS volume rule for bonds** (no data visible). Earlier fills of 18-20 units suggest 8-13 is fine.
4. **Buying-power behaviour:** whether WInS reserves cash for open orders, and whether it shrinks or rejects an order that is too
   large (PFAQ:47, 107 against competition/COMPETITION.md:85).
5. **Whether a pre-open Day limit order stays valid** for that session, and which order types WInS offers for bonds.
6. **"Required trading activity"** (FAQ:80). Ask Wharton; never trade to meet an unknown count.
7. **When WInS credits the early-November iBond distributions.** This affects cash only slightly.
8. **How an "Add Note" on an old order displays,** and whether judges see it.
9. **The reconcile3r and rematch1R desks** had no finished .md at 22:31 UTC (their folders hold only `toolkit/data/` and `scripts/`). Any
   new WInS implication from them is not in this pack. Re-check before M5.

## 8. Corrections other files need
- **3r WInS sizing.** "Sell about 150 IBTM" (`oct19/coupon/coupon_risk_options.md:156`; `oct19/out/Caplet_Update_19Oct2026.md:319`)
  and "130-150 IBTM" (`oct20/redteam3r/redteam_3r.md` §8) leave $94-$531 cash. To mirror the plan and keep the $1,000 rule, sell
  about 295 (or at least 174).
- **competition/COMPETITION.md:181.** The Feb-2037 bond is 4.750%, not 5.000% (WInS ID B-T-4.750-15022037).
- **competition/COMPETITION.md:13.** "The gap changes from 14 to 16 hours" should be **15 to 16** while Sydney is on AEDT (since 4 Oct).
- **`oct16/tools/page.py`.** It caches every URL with no expiry (lines 7-14), so re-runs return old rules pages. Fetch rules with
  plain `curl` (as here and in `oct20/compliance/`).
- **Repo copies of the SMApply pages** (`smapply_public_2026-10-14/`) are stale on the stock floor, the TIPS/STRIPS ban and the
  "six weeks" wording.

## 9. What this teaches (for Ray)
- A trade has three parts: the order, the cash it needs, and the record that explains it.
- The two errors this pack catches are both cash-and-record errors, not market errors:
  - a sale sized too small to keep the cash rule;
  - a buy placed before the cash exists, which the platform may silently shrink.
- The habit that prevents both: size from the plan, sequence sale before buy, and let a second person read the preview total
  aloud.

## 10. Reproduce
From `oct20/tradecheck/scripts/`:
`/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I tradecheck.py ../data/tsy_202610_fetch.csv ../data/prices_numbers_2145utc ../data/tradecheck_out.json`
- **Inputs:** the treasury.gov October 2026 CSV (fetched 19 Oct 22:25 UTC) and Yahoo chart JSON (the numbers desk's 21:45 UTC
  fetch; Nasdaq cross-check in `data/alt/`).
- **Outputs:** `data/tradecheck_out.json` and `data/tradecheck_stdout.txt`.
- **Checked twice:** every card's cash line was re-added by hand. The bond model matches the numbers desk at a 20 Oct settlement
  (76.965 / 1.342).
- **Rules pages:** `web/` (curl, 19 Oct 22:19-22:23 UTC).
