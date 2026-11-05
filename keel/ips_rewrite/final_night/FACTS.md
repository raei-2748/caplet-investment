# FACTS: the fact-checker's sheet for the final-night IPS rewrite (Thu 5 Nov 2026, Sydney)

AI-generated (Claude Code, fact-checker), not submission text. Due: pitch (50 words) + IPS (500 words) on the SMApply
form by **Sat 7 Nov 09:00 Sydney** (Fri 6 Nov 5 pm ET). Branch `claude/book12-final-night`; nothing committed; WInS and
SMApply not opened. Every number below gives value, date, method, source, confidence. MODEL = our simulation, not a fact.

**Headline for the writer:**
1. On the newest curve (treasury.gov, **4 Nov close**) the ten payments cost **$300,608**, which is **$608 over**
   $300,000. On 23 Oct they cost $297,636, with $2,364 to spare. Any line saying "her first $300,000 buys the whole
   ladder" is now false on the latest close. Keep the conditional (section 3, N1).
2. The range "$145k to $170k" is stale. On the 4 Nov curve the same model gives about **$140k to $163k**. Print no
   range in the IPS: Wharton says it belongs in the Final Report.
3. The IPS needs no model number at all. Every number the FINAL prints is a case fact. Keep it that way.

---

## 1. The case, in its own words
Source: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (line numbers given).

| Term | Exact words | Line |
|---|---|---|
| Deposits | "At the beginning of 2027, Laura plans to invest $300,000 with an asset management firm. She will contribute an additional $150,000 at the beginning of 2028, using earnings from publishing advances, speaking engagements, licensing, and other entrepreneurial ventures." | 43-45 |
| Timing | "All contributions and withdrawals occur at the beginning of the applicable year. The ten operating payments are therefore spaced exactly one year apart." | 59-60 |
| No other flows | "Apart from the two contributions described above, she will neither add to nor withdraw from the portfolio before 2033." | 63-65 |
| Risk attitude | "Although she has been willing to take thoughtful risks throughout her entrepreneurial career, she wants her investment team to recommend an appropriate balance between pursuing growth and protecting the capital required for her goals." | 69-74 |
| Residency | "a small, community-oriented space where artists, writers, designers, entrepreneurs, and educators can temporarily live, work, teach, and collaborate." | 77-80 |
| Portfolio's job | "The investment portfolio must fund the operating commitment described below and may also cover part of the facility's cost." | 84-85 |
| **Operating commitment** | "Laura will make ten annual payments of $50,000 toward the residency's operating expenses, one at the beginning of each year from 2033 through 2042." | 88-89 |
| Fixed, nominal | "For purposes of the competition, each payment is a fixed $50,000 and is not adjusted for inflation." | 90 |
| **High degree of certainty** | "All ten payments must be funded by the investment portfolio with a high degree of certainty. Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this requirement." | 91-92 |
| **Operating reserve** | "At the beginning of 2033, before making the first operating payment or contributing to the facility, Laura will set aside a portion of the portfolio to fund the ten payments. This set-aside is called the operating reserve. Teams must recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made." | 94-97 |
| Certainty definition asked | "They should also define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions supporting their recommendation." | 97-99 |
| **Facility contribution** | "After establishing the operating reserve in 2033, Laura must decide how much of the remaining portfolio she can responsibly contribute toward the cost of establishing the residency facility." | 101-102 |
| **Financial flexibility** | "She recognizes that committing all remaining assets could limit her financial flexibility as the project develops." | 102-103 |
| No set answer | "There is no predetermined facility contribution." Teams "are not expected to determine the size or investment composition of a separate contingency fund or endowment." | 104-107 |
| **Co-sponsors** | "Laura plans to begin approaching potential co-sponsors in 2031, two years before the residency is established." "A meaningful personal contribution may signal that the residency is financially viable, demonstrate Laura's commitment to the project, and make potential co-sponsors more willing to contribute." | 109-112 |
| Credibility risk | "If Laura promises more than she can ultimately contribute, she could damage her credibility and lose the confidence or participation of co-sponsors." | 114-115 |
| **Credible range** | "Rather than promising one exact amount, she wants to communicate a credible range for her potential contribution." | 115-116 |
| Range test | "Teams must recommend the dollar range Laura should communicate and state how confident they are that her 2033 contribution will fall within that range. They should explain how favorable and unfavorable market outcomes could affect the amount she can provide. The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment." | 117-120 |
| WInS is not Laura's money | "Gains or losses generated during the WInS trading period should not be added to or subtracted from Laura's portfolio projections." | 132-133 |
| Assumptions to name | "investment performance, the timing of cash flows, outside funding, the effect of inflation on portfolio projections and facility costs, and the financial flexibility Laura should preserve." | 146-148 |
| Out of scope | facility cost, "construction budget", "total funding gap", "personal income taxes, capital gains taxes", Taiwan law | 164-169 |

Word note: the case says "co-sponsors" (hyphen), "operating payments", "operating reserve", "facility contribution",
"credible range", "financial flexibility". Ray's 4 Nov rule (I83): use these words, not our labels.

## 2. What the team holds, and what the locked record says (the IPS must not contradict it)

### 2a. The WInS book (export of 23 Oct; no trade since 8 Oct; last safe order time Thu 5 Nov 08:00 has passed; book freezes Sat 7 Nov 08:00-09:00)
Source: `competition/wins/2026-10-23_snapshot.md` (Ray's WInS CSV exports). Confidence: HIGH (WInS's own figures).

| Holding | Units | Market value 23 Oct | Role (payment it pays) |
|---|---|---|---|
| IBTM (iBonds Dec 2032 Treasury ETF) | 4,503 | $99,313.67 | 1 Jan 2033 payment **and** the stand-in for her minimum facility contribution (two jobs) |
| IBTO (Dec 2033) | 1,024 | $23,936.00 | 2034 |
| IBTP (Dec 2034) | 927 | $22,725.59 | 2035 |
| IBTQ (Dec 2035) | 894 | $21,594.48 | 2036 |
| IBTR (Dec 2036) | 853 | $20,450.68 | 2037 |
| T-bond 4.75% 15 Feb 2037 | 20 ($20,000 face) | $19,522.68 | 2038 (matures 10.5 months early) |
| T-bond 4.50% 15 May 2038 | 20 | $18,962.57 | 2039 (7.5 months early) |
| T-bond 4.375% 15 Nov 2039 | 18 | $16,552.34 | 2040 (47 days early) |
| T-bond 4.25% 15 Nov 2040 | 18 | $16,161.79 | 2041 |
| T-bond 3.125% 15 Nov 2041 | 20 | $15,399.25 | 2042 |
| VT (Vanguard Total World Stock ETF) | 167 | $26,138.84 | growth: only how far the facility contribution rises above its minimum |

Portfolio value $305,557.66; return 1.85%; cash $3,513.79; 11 trades used; short, margin and loan all $0. Weights:
IBTM 32.5%, other iBonds 29.0%, T-bonds 28.3%, VT 8.6%, cash 1.1%.
**What the book represents:** Laura's plan **after the 2028 deposit, scaled to $300,000** (sheet "Portfolio" tab: ladder
65.9%, facility minimum 24.3%, stock fund 8.7%, cash 1.1%; `caplet/Portfolio_and_Trading_Notes_snapshot.xlsx`). So
about 3/4 of IBTM (24.3 of 32.5 points, about 3,365 units) stands in for the facility minimum and about 1/4 (about
1,140 units) for the 2033 payment. That split is my calculation from the sheet's target weights. It is not a WInS figure.
The book is **not** the January 2027 purchase. The IPS must never say her first $300,000 bought shares (Archive A32).

### 2b. The three Trading Notes Analysis entries (submitted 23 Oct; as held in the IPS Report Doc 24 Oct; verbatim)
Source: `keel/rooms/archive.md` "The TNA as held", same as `keel/rooms/archive_checks/2026-11-03_blind_packet/F1_locked_record.md`.
A student still has to confirm that this matches what went into SMApply (`keel/pm/ASK_HUMANS.md`).

**Note 1, B-T-4.750-15022037.** Note: "Future funding: we use the 4.750% Treasury maturing 15 Feb 2037 for Laura's 1 Jan
2038 payment because it is the latest WInS bond available beforehand. The 10.5-month gap creates reinvestment-rate risk
on the proceeds held in a short-term Treasury ETF."
Reflection: "We know Treasury bonds (including this one – maturing 2037) won't create wealth, but they will remove
uncertainty, through duration-matching. In other words, we take Laura's requested 'high degree of certainty' to mean a
near-ironclad guarantee, and we provide exactly that. Every year the bonds sit untouched is a good year – one less year
of Laura's money being exposed to anything the restless markets might decide to do. Notably – Laura's payments are fixed
in nominal dollars, so a nominal Treasury matches the liability perfectly, meaning we don't need TIPS, which would hedge
against a nonexistent inflation risk."

**Note 2, IBTM.** Note: "Future funding and risk management: IBTM does two jobs in Laura's plan. It supports her first
$50,000 payment and provides a floor for her facility contribution, giving co-sponsors a minimum figure in 2031. It
holds 2032 Treasuries, so the timing fits, although the final payout is not fixed."
Reflection: "Some years, WInS lists no Treasuries maturing – so we purchased iShares iBonds (like IBTM for 2032) instead.
Defined-maturity, investment-grade, liquid, cheap and transparent about yields, these behave a lot like bonds when held
to their end – so we'll simply ignore price noise in the interim. Together, our T-Bonds and iBonds ensure each of Laura's
payments rests on a dedicated instrument (not merely a forecast). The catch is, their terminal payout is a net asset
value, as opposed to a promise of par – but in return we gain a level of liquidity which no odd-lot bond offers."

**Note 3, VT.** Note: "Growth: Vanguard Total World Stock ETF holds about 10,000 stocks at a 0.06% fee, so one cheap fund
diversifies Laura's stocks. They only set how far her gift rises above her promised minimum. A fall can shrink the
extra, and a rise before 2031 lifts the top of the range co-sponsors hear."
Reflection: "VT is where we allow ourselves to be wrong – because it's the only investment not standing between Laura
and a payment deadline. This ETF owns thousands of companies, diversified across countries and sectors, which means we
can avoid paying the price for the vain illusion that we can pick winners, instead buying the entire market's growth
premium at an expense ratio of just 0.06%, for a forecast return of about 7.5% a year (as per JPMorgan). The T-Bonds and
iBonds already cover the operating commitments, so VT answers a different question – how generous can the facility
contribution be?"

### 2c. The other eight filled-trade notes (the lines that bind the IPS)
- IBTR (7 Oct 4:42 AM ET, the **filled** one; the cancelled 6 Oct note says "0.3"): "On the 6 Oct Treasury curve, her
  first $300,000 is enough to buy Treasuries for all ten payments. If yields fall more than about 0.2 percentage points
  by January, the 2028 deposit would top up the ladder, leaving less for the facility."
- IBTO: "Its December payout is not fixed, and this is one of the first payments we would top up if yields fall before January."
- IBTP: "Its payout is not fixed, but it ends close to when Laura needs the money." IBTQ: "Its payout is not fixed, but
  it ends about two weeks before the payment is due."
- May-2038: "Its proceeds stay in a short-term Treasury ETF for 7.5 months".
- Nov-2039: "Held to maturity, its fixed coupons and principal cover most of it; reinvested coupons fund the rest."
- Nov-2040: "A lower-coupon bond would reduce reliance on reinvested coupons, but WInS lists none for that date."
- Nov-2041: "the last five payments use individual Treasuries, scaled to the model portfolio, with reinvested coupons funding part of each."

### 2d. So the IPS is bound to say, or at least not deny
Each payment has its own Treasury holding, held to the end. IBTM does two jobs: the 2033 payment and the facility
minimum. VT is the only growth asset and no payment stands on it. The funds pay their net asset value (NAV), not a fixed
par amount. Reinvesting coupons is a named risk. If yields fall, the 2028 deposit tops up the ladder first and the
facility gets less. A minimum figure goes to co-sponsors in 2031, and a rise in VT before 2031 lifts the top. No TIPS.
Archive check of 5 Nov (`keel/rooms/archive_checks/2026-11-05_what_october_allows.md`). Safe to build on: C1 (choose
where the plan may be wrong), C3 (the safe asset is the one that matches the debt), C6 (the funds trade a fixed payout
for liquidity), C7 (one fund, two jobs), C9 (a yield fall costs the facility first). These clash with the locked
record: C2, C4, C8, C10, C11, C12 (see section 4).

## 3. Every number the IPS might use

**Wharton:** the IPS should not present "detailed financial calculations"; reserve calculations, projections and "a final
facility-contribution range" go in the Final Report. The FINAL (`keel/ips_rewrite/drafts/FINAL/ips.txt`) prints only
case numbers. The safest rewrite does the same. If a model number goes in anyway, it must carry its date.

### 3a. Safe: case facts and holdings (confidence HIGH)
| # | Value | Source |
|---|---|---|
| C1 | $300,000 at the start of 2027; $150,000 at the start of 2028 | case 43-45 |
| C2 | ten fixed $50,000 payments, the start of each year 2033-2042, not inflation-adjusted | case 88-90 |
| C3 | co-sponsors approached in 2031; facility contribution decided in 2033 | case 101, 109 |
| C4 | ten Treasury holdings: five iBonds Treasury funds (ending Dec 2032-Dec 2036) for 2033-37, five T-bonds (Feb 2037-Nov 2041) for 2038-42; each ends **before** its January | WInS snapshot 23 Oct |
| C5 | the 2032 fund ends "on or about December 15, 2032" | IBTM summary prospectus (27 Feb 2026), per KEEL_RECORD s2 |
| C6 | VT: about 10,000 stocks, 0.06% fee | VT note (locked) |
| C7 | 7.5% a year, world stocks | J.P. Morgan 2027 LTCMA (press release 19 Oct; matrix not read at source). Already in TNA reflection 3. If used, write it exactly as "about 7.5% a year (J.P. Morgan)", with no "compound" and no "ACWI" (Archive A1). The FINAL moved it to the Final Report. |

### 3b. Model numbers: latest value, history, and conflicts
| # | What | Latest value | Date / method | Source | Confidence | Conflict / staleness |
|---|---|---|---|---|---|---|
| **N1** | Cost on 1 Jan 2027 of the ten $50k payments (payment-date basis) | **$300,608, i.e. $608 OVER $300k (-2bp)**; DV01 $299/bp | **4 Nov 2026 close**, treasury.gov par curve, bootstrapped (method of `keel/scripts/ladder_pv.py`), re-run tonight | https://home.treasury.gov daily par yield curve CSV, Oct and Nov 2026 (fetched 5 Nov; copy in session scratchpad) | MODEL, curve VERIFIED | **CONFLICT.** Files still say "$297,636, headroom $2,364 (8bp)" (23 Oct: `00_GROUND_TRUTH.md` s5, `keel/office/checks/2026-11-05.md`, which says "No close after 23 Oct in the repo"). Since then: 26 Oct $297,787; 27 Oct $298,068; 28 Oct $296,185; 29 Oct $298,256; 30 Oct $299,332; **2 Nov $300,233 (over)**; 3 Nov $299,021; **4 Nov $300,608 (over)**. My re-run of 23 Oct gives $297,636, so the method matches. Older: 15 Oct ~$294k (`ips_numbers_2026-10`, stale); 16 Oct $298,087 (range_2031). |
| N1b | The same cost on other bases | holdings-forward basis **$303,916 (-$3,916, -14bp)** on 4 Nov | `range_2031.py` re-run on 4 Nov (scratch copy; repo file untouched) | `keel/library/range_2031/` | MODEL | Bases differ by $3-4k (22 Oct: $298,861 / $300,224 / $302,139). Quote at most one, and name its basis. |
| N2 | "Her first $300,000 buys the ladder" | **Coin-flip, now leaning no.** Over on 2 of the last 3 closes (payment-date basis) and on every close since 23 Oct (forward basis) | from N1 | as N1 | MODEL | The FINAL pitch ("her first $300,000 buys Treasuries that mature one before each January") and P3 ("her first $300,000 buys a ladder") rest on this. Safe wording, from the IBTR note and FINAL P5: the 2028 deposit "first completes the ladder, if needed". |
| N3 | Chance the 2028 deposit must top up the ladder | **65%** (4 Nov); 53% (23 Oct); about 44% (16 Oct) | range_2031 model, 90bp/yr rate vol | as N1b | MODEL (vol is assumed) | Rising as yields fall |
| N4 | Facility minimum (what IBTM is sized to pay in Dec 2032) | p50 **$145,874**; p5 $128,023; cap $150,000; costs about $114k in Jan 2028 | 4 Nov re-run | as N1b | MODEL | `00_GROUND_TRUTH` s5 says "IBTM sized to pay about $150k in 2032, quoted at $145k". That holds only if no top-up is needed. On 4 Nov a $3.9k top-up shrinks it to about $146k. **Never "a fixed $150,000"** (Archive C12) |
| N5 | 2031 range (bottom / median top), old design (no naming-day lock) | **$140,000 / $163,000** (top p5-p95 $140k-$184k); reaches the top 76%; at least halfway 100%; gift never below the quoted bottom (by construction) | 4 Nov re-run; JPM **2026** 7.0% equity, 200,000 paths | as N1b | MODEL | **STALE elsewhere:** "$145k to about $170k", 3 in 4 (16 Oct, range_2031 README); "$145k-$168k, ~99% inside" (15 Oct, `IPS_number_sheet.md`); 23 Oct re-run $145k / $166k. Also the 7.0% return here differs from the 7.5% in TNA reflection 3. The FINAL design adds a naming-day lock that lowers the range on naming day in about 27 of 100 base futures (L-17 KW). Archive A5: a printed $145k bottom is broken in 43.5% of paths before the mark. **Print no range in the IPS.** |
| N6 | Payments paid in full under the FINAL's rule ("as if every dollar waiting for a payment earned nothing") | 100% base; 100% if yields fall 2pt for good; 98.71% if yields are 1pt lower and the 2028 deposit is halved | **22 Oct curve**, JPM 2027 7.5%, 200,000 paths | `keel/rooms/lab/L-17_interest_that_earns_nothing.md` (KW arm); Archive A20, A33 | MODEL, not re-run on the Nov curve | Without the rule: 96.01% (W0f). Not 100% in every world, so this does not license "guaranteed". |
| N7 | Coupon shortfall if yields fall and stay down | ~$11k (1pt), ~$21k (2pt), ~$44k (near zero), of $500k | **15 Oct curve** | `keel/library/ips_numbers_2026-10/IPS_number_sheet.md` | MODEL, STALE | Older curve than anything beside it (SD-P02). Do not quote. |
| N8 | VT bought Jan 2028 (Laura's plan) | p50 **$30,926** (p5 $19.7k, p95 $49.6k) | 4 Nov re-run | as N1b | MODEL | Older: about $32k (15 Oct, 22 Oct); about $35k (16 Oct) |
| N9 | Shares as a share of Laura's money | about **6.6%** (Laura's plan, 30 Oct curve) vs **8.6%** in the WInS book | KEEL_RECORD s2 | `keel/ips_rewrite/drafts/FINAL/KEEL_RECORD.md` | MODEL / HIGH | "Less than a tenth" holds for both |
| N10 | Ladder's average timing vs the payments' | about 7.6 years vs 10.0 (7.61 v 9.99) | Archive re-run 4 Nov | `keel/rooms/archive.md` A34 | MODEL | This is why "duration-matched" is false (section 4) |
| N11 | IBTR note's trigger: a 0.2-point fall in yields | from the **6 Oct** curve. Tonight's headroom is already negative | IBTR note (locked) | WInS | locked words | Quote only as the note's own condition, never as today's figure |

## 4. Never say

| Don't write | Why | Source |
|---|---|---|
| "risk-free", "guaranteed" (about the payments), "to the dollar", "each payment is guaranteed" | The funds pay NAV, not par ("as opposed to a promise of par"). IBTO note: "not fixed". The lock is 98.71%, not 100%, in a bad world. Reflection 1 says "near-ironclad", so keep "near" | TNA reflection 2; IBTM/IBTO notes; Archive C10, A3; L-17 |
| "never below" (the range bottom), "the bottom never moves" | If her kept shares can't cover the gap, "she names a lower range". The bottom moves with the floor | FINAL P7; LOOK_ALIKE row K; Archive A5 |
| "a fixed $150,000 minimum" | The payout is not fixed, and a top-up shrinks it (N4) | IBTM note; Archive C12 |
| STRIPS, zero-coupon Treasuries, individual TIPS, inflation-linked bonds for the payments | Banned ("Individual TIPS", "Individual STRIPS"). Reflection 1 rejected TIPS on merit | `wharton_email_week5_2026-10.md` :30-31; Archive C8, A8 |
| Margin, shorting, options/futures/swaps as part of Laura's plan; crypto | Banned. "an option" is allowed only as what a bank's note buys | week5 email :24-32; check 2026-11-05 |
| "Treasury bills", "T-bills", "cash" alone as where waiting money sits | No bill is listed on WInS (near-breach 28 Oct). The locked note says "a short-term Treasury ETF" | `keel/office/checks/2026-10-28.md`; Archive A13 |
| CPPI, "portfolio insurance" (as ours), "dynamic" protection | The facility minimum plus VT is a static floor-plus-cushion. The FINAL rejects portfolio insurance by name | `competition/COMPETITION.md` :197; `keel/BIBLE.md` :419 |
| "immunisation/immunization", "duration-matched", "matches the payments' average timing/duration" | It is cash-flow matching (one holding per payment). Average life is 7.6 vs 10.0 years. Also don't write "we don't duration-match", which reads against reflection 1. Write "each payment has its own bond" | COMPETITION.md :197-198; Archive A34; FINAL README item 3 |
| "rebalance the bonds as rates move" | "Every year the bonds sit untouched is a good year"; "ignore price noise" | Archive C4, A4 |
| "a payment short is paid from shares", "shares cover a gap after 2033", "the stocks never touch a payment" | VT is "the only investment not standing between Laura and a payment deadline". The lock is bought from kept shares **before** naming, then held in Treasuries | Archive C2, A19, A33; LOOK_ALIKE F, J |
| "later bonds' coupons pay earlier payments" | Each payment "rests on a dedicated instrument" | Archive C11 |
| "maturing in January", "just before each January" | They end in December, February, May or November. Write "before each January" | Archive 5 Nov; LOOK_ALIKE A |
| "the funds pay exactly what they promised", "a Treasury held to maturity pays exactly" (without "bond") | Only a **bond** promises an amount | LOOK_ALIKE C; KEEL_RECORD s6 |
| "her first $300,000 secures/buys every payment" (flat) | False on the 4 Nov close (N1). Unsupported in 57% of MODEL paths without the 2028 deposit (A24) | N1; Archive A24 |
| "her income rides on / tends to dry up with shares" | The case never links her income to markets. "can" is the most we may say | Archive C5; KEEL_RECORD s7 |
| "not a forecast" (about the bottom) | Write "already bought" or the locked "not merely a forecast" | Archive A15 |
| "rates/markets can't touch a payment" | Only *price* swings are shut out. Reinvestment risk is in five notes | Archive A16 |
| Inflation threatens a payment | Payments are fixed nominal. Inflation hits facility costs | case 90; Archive A2 |
| WInS gains in Laura's projections; "the simulator is her 2027 purchase" | case 132-133; Archive A32 | |
| Coined labels: "floor", "cheques", "promises", "building gift", "Root & Branch"/"Roots First" | Ray's 4 Nov rule I83: use the case's words. Roots motif retired 24 Oct | FINAL README; KEEL_RECORD s9; Archive A9 |
| "Laura wants to take risks" | The case: she "has been willing to take thoughtful risks throughout her entrepreneurial career" | case 69-71; Archive A28 |
| Fund names/tickers, sums, facility cost, taxes, a printed range or confidence level | Wharton: not "individual investments" or "detailed financial calculations". Range and reserve calculations go in the FR | UPDATED IPS instructions; CASE_CARD |
| "7.5% compound", "ACWI" | Matrix not read at source | Archive A1 |

## 5. What Wharton asks of the IPS (verbatim from `keel/WHARTON_WORD.md`)

**Form** (`competition/official/2026_27/UPDATED_2026_WGY_Investment_Policy_FINAL.txt`, page 3): "1. Investment Strategy
Elevator Pitch / Maximum 50 words / Quickly summarize your team's investment strategy. Clearly communicate the central
idea behind your approach and how it is designed to support your client's financial goals and future funding needs."
"2. Investment Policy Statement / Maximum 500 words / Clearly explain your team's investment strategy and decision-making
framework, including how the strategy addresses Laura's financial goals, funding needs, and risk considerations."
"Graphics, charts, images, attachments, external links, footnotes, and formal citations are not permitted." Plain text in
a form box. Count with the strict count (hyphenated words split) and aim for about 490.

**Purpose:** "Your strategy should explain how you will invest your client's money to support their financial goals and
future cash flow needs while managing risk and uncertainty. It should reflect your client's goals, time horizons,
liquidity needs, desired degree of funding certainty, and need for financial flexibility."

**The questions:** "What is the central idea behind your investment strategy? / What principles will guide your
investment decisions? / How does your strategy balance growth, risk, liquidity, funding reliability, and financial
flexibility? / How will the portfolio's asset allocation and composition change as future funding needs approach and
payments are made? / How will your strategy protect the operating commitment while preserving flexibility for a
responsible facility contribution?" "Always remember who your strategy is designed to serve."

**The IPS:** "Clearly explain your team's investment strategy and the reasoning behind it. Your IPS should demonstrate how
your strategy is tailored to your client's financial goals, time horizons, and needs. Explain how your team will
approach risk and return, liquidity, portfolio construction and diversification, and planned changes in the portfolio
as future funding needs approach." It should "establish your strategic approach to preparing for the operating
commitment, managing the operating reserve's asset composition over time, determining a responsible facility
contribution, and preserving appropriate financial flexibility."
"Focus on the strategy and decision-making framework that guide your portfolio rather than describing individual
investments or presenting detailed financial calculations."
"Your IPS should make it clear: What your team is trying to accomplish for the client / Why your strategy is appropriate
for the client and their financial goals / How your strategy balances growth, liquidity, funding reliability, risk, and
financial flexibility / How your strategy will guide portfolio construction and investment decisions as the client's
needs change / How your approach will protect the required operating payments while supporting a responsible facility
contribution." "You do not need to address these points separately."
**Not expected:** "final operating-reserve calculations, detailed portfolio projections, a final facility-contribution
range, or the draft communication to co-sponsors." "sources do not need to be cited in the IPS."
**Binding:** "Once submitted, the IPS becomes the official record of your team's investment strategy. Your team may not
revise its investment strategy after the submission deadline." "Your portfolio and Final Report should reflect the
strategy established in your IPS."
**Judging (all three deliverables together):** Investment Strategy: "a clear and creative investment thesis ...
disciplined planning across Laura's changing time horizons and cash-flow needs; uses appropriate diversification; and
maintains consistency with the team's IPS." Client Knowledge: "Tailors the strategy to Laura's circumstances,
priorities, risk considerations, and residency goals". Portfolio Analysis: "reasonable assumptions and projections to
evaluate funding reliability, the facility contribution, and financial flexibility under varying market outcomes."
Creativity and Presentation: "an authentic team voice ... communicates Laura's potential facility contribution and
investment uncertainty clearly and credibly to prospective co-sponsors." Guide: "Judges want to understand not only what
your team decided to do, but also the reasoning, assumptions, and tradeoffs behind those decisions." "A long-term
strategy may include planned adjustments as funding dates approach, but it should not be rewritten simply because
markets move". Tips: "Let your investment strategy lead"; "Explain why each investment belongs in your strategy".
**Permitted only:** "Any stock available on WInS. / Any Exchange-Traded Fund (ETF) available on WInS. / Any
Government/Treasury Bond available on WInS."
