# LDI second opinion on Caplet's design (19 Oct close)

> **Verified 20 Oct (`oct20/verify_ldi_sens/verify_ldi_sens.md`): core numbers confirmed; reserve rows WRONG (mixed timing).** On consistent timing $10k in the Nov-2041 bond covers about **1.9 points** of permanent fall after the Jan 2028 purchase ($1.35k uncovered at −2) but only about **1.3 points** if the fall comes during 2027 ($9.1k uncovered); needed $5.5k/$10.7k (post-2028, −1/−2) vs $7.4k/$15.9k (during 2027). "Locks the yield, not the price" is true by 2038; at the 2031-33 decision dates the price gain is most of 3r's edge. 110.4% funded is the most favourable basis and counts the 2028 deposit: say 108.5-110.4% (surplus $35-42k). The "$9.9k hidden cushion" is about $4k vs basis D (T-bond waits); the iBond part is exposure. Drop the $2.4k low-coupon gain (1.375% Nov-2040 not WInS-listed per the filed note; at most ~$0.75k from the 2.000% Nov-41 if listed). Floor margin spare ~$0.2k after the 0.07% fee. IBTP/IBTQ purchases are 1.1-1.4% of 30-day volume; half-spread ~$8-9 a rung. "Her other assets" is an ambiguous-wording risk, not a rule breach.


**AI-generated research (Claude Code) for Team Caplet, Tue 20 Oct 2026, about 09:20 Sydney. Not text to submit.** This file reviews the design the way a pension cash-flow-matching (LDI) desk would. It drafts no TNA reflection, IPS sentence or Final Report prose. Section 12 gives concepts and labels only. If the team uses anything here, log it in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). MODEL = a computer estimate from an AI-built script, not a fact. UNVERIFIED = not confirmed.

**What was reviewed.** `oct19/out/Caplet_Update_19Oct2026.md`; `oct20/numbers/numbers_refresh.md`; `oct19/coupon/coupon_risk_options.md` and its script (`oct20/numbers/scripts/coupon_options.py`); the WInS holdings (`snap/main/COMPETITION.md:170-190`) and notes (`snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:14-24`); the accepted IPS Version 5 text in the live Doc (`oct19/exemplars/ips_doc_live_base_text.txt:20-29`; note that the 19 Oct update shows this text is 97% AI exemplar v11); and the case (`official/Laura_Gao_2026_Client_Profile.txt`).

**New evidence.** (1) iShares live pages, prospectuses and the distribution schedule, fetched 19 Oct 2026, 22:03-22:13 UTC. (2) A new, independent cash-flow model on the 19 Oct treasury.gov curve (`oct20/ldi/scripts/ldi_model.py`), which adds things the earlier models leave out: non-parallel rate moves, the iBond funds' real final-year cash, and fair treatment of the two reserve options.

**Short forms.** `oct19/`, `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`. `snap/main/` = `/home/user/snap/main/`. `official/` = `/home/user/caplet-investment/competition/official/2026_27/`. `case:n` = the client profile text, line n.

---

## 0. Summary

1. **Keep the design.** A pension desk would call it a dedicated Treasury ladder plus a surplus-only growth sleeve, and would sign off on the structure. Payments come first, then the floor, then growth. It holds only Treasuries and runs to maturity, and the equity risk is the size of the surplus. Funded ratio: about 101-102% on a market basis for the payments alone, and **110% for payments plus a $145k floor once the 2028 deposit counts** (MODEL, 19 Oct).
2. **The real gap is reinvestment. In the IPS it is a policy gap, not just a number.** About 36% of the $500k depends on coupons, and **about $49k (10%) on interest earned on reinvested coupons**. The ladder's rate sensitivity covers only **78% of the payments'** (it is 7.6 years long against the payments' 9.9). V5 has no reinvestment rule (V4 had one) and covers shortfalls with "her other assets", which the case bans (case:91-92).
3. **Option 3r is the right kind of fix, but the reason given is wrong and the comparison with 3b is biased.** The Nov-2041 reserve works mainly because it **locks today's yield to 2041**. Its price rising when yields fall adds only about $0.4k. In the coupon study, the IBTM reserve (3b) is left earning **0% from 2033** (`coupon_options.py:198`); that, not the reserve choice, drives the "$10k does the job of $25k" claim. On its own, $10k covers a permanent fall of about **1.5 points** (it needs $12.9k for 2 points). The rest relies on a 2033 re-pricing step that the IPS never names.
4. **iBond mechanics, checked live, add three small but real points.** (a) Each fund's yield is locked only to its bonds' average maturity, about **5.4-7.4 months before** its mid-December end. After that it holds cash ("Declining Yield Risk"), so **seven of ten rungs**, not two, have a waiting gap. (b) Proceeds arrive about **18 Dec** (the IBTG 2026 precedent), and the 2033 payment and the floor both ride on IBTM's one payout. (c) Payouts vary month to month (IBTQ $0.064-0.088). Liquidity, premiums and spreads are fine.
5. **What a professional would add (for the IPS, as principles).** (1) A surplus-release test: nothing above the floor leaves until the remaining payments are fully funded at market prices. (2) A written reinvestment rule. (3) Named residual risks, each with a named cover sized to a stated stress. (4) Pre-set triggers at a fixed January review. (5) Equity risk limited to the surplus. Document "high degree of certainty" with four measures: funded ratio on two bases, hedge ratio, reliance on reinvested income, and a stress table.

---

## 1. Verdict: keep, change, add

| | Item | Professional view | Section |
|---|---|---|---|
| **Keep** | Cash-flow matching with US Treasuries only, held to maturity | Textbook dedication. Credit risk is the US government only. Correct for fixed nominal payments with "high degree of certainty" (case:91) | 2 |
| Keep | Order: payments → floor → growth | A funding waterfall; trustees call this "funding priority" | 12 |
| Keep | iBond ETFs for the 2033-37 payments | The only WInS-listed way to reach 2031-36: WInS lists no Treasury maturing Feb 2031 to Feb 2036 (`snap/main/COMPETITION.md:93`) | 3, 4 |
| Keep | Floor in IBTM, rounded down, with a $3,700 margin | Term-matched to the 2033 gift. The margin covers the floor's own reinvestment and final-year cash risk at −2 points, with about $0.7k to spare | 7 |
| Keep | One VT fund, no rebalancing | A static floor-plus-cushion. VT (about $33.5k) is smaller than the $42k surplus, so equity risk never reaches the payments or the floor if VT stays out of the payment backstop | 8 |
| Keep | 2028 deposit tops up the ladder first | The right first use of new money. It is also the only honest answer to the pre-purchase gap (Section 2c) | 2 |
| Keep | No WInS trades before the TNA | Weights are within about 0.2 points of target (`oct20/numbers/numbers_refresh.md:299-300`) | 13 |
| **Change** | "covered by her other assets" (V5) | Outside money is banned (case:91-92). The cover must be inside the portfolio: a reserve plus a 2033 re-pricing | 6 |
| Change | No reinvestment rule in V5 | V4 had one ("reinvest income in the holding that generated it", `ips_doc_live_base_text.txt:63`). V5 dropped it. Put the concept back | 6a |
| Change | "Retained equity" funds an uncovered payment (V5 :25) | This turns Laura's flexibility money into a stock-dependent payment reserve (option 2, worst in joint stress). Use the reserve and the 2033 re-pricing instead | 6, 8 |
| Change | The 3r explanation ("price rises when yields fall") | The main mechanism is locking the long yield to 2041 for the reserve money. Say that | 6c |
| Change | The coupon study's 3r-vs-3b gap | 3b is penalised by 0% cash after 2033. A fair comparison shrinks the gap at −2 points to about $2.8k | 6c |
| Change | Waiting gaps named on two notes only | Seven rungs wait 6-10.5 months, including all five iBond funds | 5 |
| **Add** | 2033 surplus-release test (and optionally a yearly one to 2042) | The step that makes "high certainty" true beyond what the reserve covers | 10, 12 |
| Add | Trigger list with owner and date | Section 9 | 9 |
| Add | Certainty evidence pack (Final Report) | Section 11 answers case:97-99 directly | 11 |
| Consider | Lower-coupon bonds for the 2041/2042 payments, if WInS lists them | About $2.4k less shortfall at −2 points. Listing UNVERIFIED. Laura's real plan only, not WInS | 4 |
| Consider (Final Report alternative only) | A lock-in of the promised top after 2031 | From 2031 to 2033, the gift's half of VT can fall but cannot rise past the cap | 8 |

---

## 2. The funding position, reported the way a pension actuary would

All MODEL, on the 19 Oct treasury.gov par curve (`oct20/ldi/data/funding_19oct.json`; curve row in `oct20/numbers/numbers_refresh.md:25`). Ten $50,000 payments are valued at 1 Jan 2027.

### 2a. Funded ratio on several bases (assets ÷ liabilities)

| Basis | Liabilities (or cost) | Funded ratio | What it means |
|---|---|---|---|
| Market value of the payments (payment dates, yields unchanged; equals numbers-desk basis B, $293,767) | $293,767 | **102.1%** | What the promise is worth. Not what can be bought on WInS |
| Numbers-desk basis D (holdings' dates) | $297,162 | 101.0% | The IBTR note's cautious test |
| Cost to buy the WInS-listed ladder, waiting money in a short Treasury fund (new model) | $298,126 | 100.6% | The closest thing to a "buy-out" (implementation) basis |
| Same, waiting money at 0% | $300,678 | **99.8%** | The most cautious. Under 100% |
| Payments vs the 2027 deposit plus the 2028 deposit (PV $143,474) | $293,767 | 151% | Payments are well covered once both deposits count |
| **Payments plus a $145k minimum in Jan 2033 (PV $107,755)** | $401,522 | **110.4%** | Surplus about **$42.0k**: roughly what funds VT and the margins |

**What this teaches.** On payments alone the plan is only just funded (about 100-102%), and the answer flips with the basis. On payments plus the floor, it has a clear 10% surplus, and the equity sleeve is that surplus. That is why "the 2027 deposit alone is sized for the payments" (V5 :23) is fragile and "the plan is funded after both deposits" is robust. This supports option (b) of vote item D0-4 (`oct19/out/Caplet_Update_19Oct2026.md:285`).

### 2b. Hedge ratio and reliance on reinvested income

- **Rate sensitivity (PV01).** Assets $226 per 0.01 point; liabilities $291. **Hedge ratio 78%.** Duration 7.6 years for the assets against 9.9 for the liabilities (new model, real coupons). Coupons arrive years before the payments they fund, so the assets are shorter than the promise.
- **Where the $500k comes from** (base case, own-rung sizing): principal **$320k (64%)**, coupons **$130k (26%)**, interest on reinvested coupons and waiting money **$49k (10%)**. Only the $49k is truly at risk, since coupons themselves are fixed. By rung: iBond rungs 21-36% from coupons and reinvestment; T-bond rungs 41-47% (`oct20/ldi/data/ldi_19oct_stdout.txt`).
- **Closing the gap fully by duration** would need about **$57k** more of the Nov-2041 bond at market value ($11.3 PV01 per $10k). That is out of budget, so a professional would not try to immunise in mark-to-market terms. They would hold a sized contingency reserve plus a re-pricing rule (Section 6).

### 2c. Surplus at risk (how much the surplus can move)

| Window | Exposure | 1 standard deviation | 95% one-sided |
|---|---|---|---|
| Now → 1 Jan 2027 (all cash; the full liability is unhedged) | $291/0.01 pt | $13.0k (1.0 pt/yr) / $9.2k (0.71 pt/yr, 2026 realised) | **$21.4k / $15.2k** |
| First year after purchase (PV01 gap $65/0.01 pt) | $65/0.01 pt | $6.5k / $4.6k | $10.7k / $7.6k |

- **Before 1 Jan 2027** the room is $2.8k (D) to $7.0k (A) against a one-standard-deviation move of about $13k. That is the source of the 30-41% odds in `numbers_refresh.md:91-97`. Nothing can hedge this window: Laura's money arrives in January 2027 (case:43). The only answer is the top-up rule.
- **After purchase** surplus risk falls by about 78%. What is left is reinvestment (Section 6) and the waiting gaps (Section 5).

---

## 3. iBond ETF mechanics (live iShares, fetched 19 Oct 2026, 22:03-22:13 UTC)

Sources: product pages `https://www.ishares.com/us/products/{328944,332291,337745,342105,350028}/...` (data "as of Oct 16, 2026"; copies and extract in `oct20/ldi/web/` and `oct20/ldi/data/ibond_keyfacts_live.txt`); IBTM summary prospectus dated 27 Feb 2026 (`oct20/ldi/web/docs/sp_ibtm.txt`); IBTR summary prospectus dated 25 Mar 2026 (`sp_ibtr.txt`); trust prospectus with its 15 Oct 2026 supplement (`prosp_ibt.txt`); 2026-28 distribution schedule dated 16 Oct 2026 (`distsched.txt`).

### 3a. Key facts

| Fund | Assets | Launched | Holdings | Avg maturity (WAM) | Months the holdings end before 15 Dec | YTM / SEC yield / 12m paid | Premium | Median spread | 30-day avg volume |
|---|---|---|---|---|---|---|---|---|---|
| IBTM (Dec 2032) | $593.0m | 6 Jul 2022 | 15 | 5.71 y | 5.4 | 4.94% / 4.98% / 4.05% | 0.01 | 0.05% | 283,407 |
| IBTO (2033) | $502.3m | 27 Jun 2023 | 13 | 6.68 y | 5.8 | 4.97 / 5.03 / 4.29 | 0.03 | 0.04% | 231,992 |
| IBTP (2034) | $336.7m | 11 Jun 2024 | 4 | 7.71 y | 5.4 | 5.02 / 5.08 / 4.18 | 0.05 | 0.04% | 103,075 |
| IBTQ (2035) | $284.8m | 25 Mar 2025 | 4 | 8.70 y | 5.5 | 5.06 / 5.10 / 4.06 | 0.09 | 0.04% | 122,905 |
| IBTR (2036) | $109.2m | 25 Mar 2026 | 4 | 9.54 y | 7.4 | 5.08 / 5.02 / – | 0.02 | 0.04% | 178,127 (32,238 on 16 Oct) |

Expense ratio 0.07% for all five. "Months before 15 Dec" = (years from 16 Oct 2026 to 15 Dec of the maturity year) − WAM (CALC).

### 3b. What each point means for Laura

- **No fixed payout.** "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions" (`sp_ibtm.txt:104-106`; the same in `sp_ibtr.txt`). Keep the rounded-down floor and the "not fixed" wording already in the IBTM, IBTO, IBTP and IBTQ notes.
- **Final-year cash.** "In the last six months of operation, as the bonds held by the Fund mature, the proceeds will typically be reinvested ... in investments already in the Underlying Index but may also be invested in other cash and cash equivalents" (`sp_ibtm.txt:152-156`). By 15 Dec "the Fund is expected to consist almost entirely of cash" (`:159-160`). Its "yield may move toward prevailing money market rates" ("Declining Yield Risk", `:294-298`).
  - So each fund's yield is locked only to its bonds' average maturity, about 5.4-7.4 months early.
  - The coupon study models the funds as par bonds ending 15 Dec (`coupon_options.py:9`), which locks about six months too long. The effect is small: about $250 per rung for each point bill rates fall (Section 5).
- **Termination and payout timing (precedent).** The 15 Oct 2026 supplement for IBTG (the Dec 2026 fund) gives the real sequence: last trading day 15 Dec; trading suspended from 16 Dec; liquidation proceeds "scheduled to be sent to shareholders on December 18", "subject to their brokerage firm's processes"; "we cannot assure you that there will be a trading market" from 16 to 18 Dec; the final NAV includes liquidation costs (`prosp_ibt.txt:24-43`). For Laura that means **cash about 14 days before each 1 Jan payment.** IBTM carries both the 2033 payment and the floor, about **one third of all her money in one payout**.
- **Termination can move.** "The Board may extend the termination date if a majority of the Board determines the extension to be in the best interest of the Fund" (`sp_ibtm.txt:166-168`). Also, "Each Fund's investment objective and its Underlying Index may be changed without shareholder approval" (`prosp_ibt.txt`, page 101). Early closure of a small fund before its term: the prospectus text read here does not cover it (the SAI was not read; **UNVERIFIED**). V5's substitution rule ("an unavailable holding is replaced by an earlier-maturing Treasury", `ips_doc_live_base_text.txt:25`) is the right defence. Keep the concept.
- **Distributions vary.** All five pay monthly (ex-date the first business day of each month; `distsched.txt:60-61, 457`). Payouts over the last 12 months (Yahoo monthly data, `oct20/ldi/data/div_summary.txt`): IBTM $0.069-0.076; IBTO $0.076-0.086; IBTP $0.080-0.090; IBTQ $0.064-0.088; IBTR $0.064-0.094 (6 payouts since its first on 1 May 2026, `distsched.txt:477`).
  - Paid income (about 4.1-4.3% a year) is well below the yield to maturity (4.9-5.1%). The rest comes from pull-to-par inside the fund.
  - **So never size a rung from its payouts.** The liquidation value is the payment source, and the payouts are income that must be reinvested (Section 6a).
- **NAV vs price, spreads, liquidity.** Premiums were 0.01-0.09% and median spreads 0.04-0.05% on 16 Oct. Laura's real January 2027 purchase is about 1,300-1,700 shares per fund (new model: $30.5k-$37.5k a rung), under 1% of 30-day average volume. Spread cost is about $15 a rung. The only liquidity rule needed is limit orders during US market hours (after-hours spreads are wide: `snap/main/COMPETITION.md:100`).
- **Concentration inside the funds.** IBTP, IBTQ and IBTR each hold only 4 Treasury notes. That is no credit issue (all US Treasury) but explains why their payouts vary more.
- **No iBond Treasury fund exists for 2037-2043.** The iShares schedule of 16 Oct 2026 lists Treasury iBonds IBTG-IBTR (2026-2036), then IBGA-IBGC (2044-46) and IBGK-IBGM (2054-56) (`distsched.txt:79-107`). That confirms the Nov-2041 note's "no iBonds Treasury funds maturing in 2037-43".
- **Next payout and the WInS freeze.** Ex/record date Mon 2 Nov, pay date Thu 5 Nov 2026 (`distsched.txt:60-61`), one day before trading freezes. At the October rates the book would get about **$600** (4,503×0.070 + 1,024×0.079 + 927×0.083 + 894×0.082 + 853×0.064; CALC). Whether WInS credits it is UNVERIFIED. A trade to reinvest it ($25 commission) is not worth it.

---

## 4. Treasury rung selection under WInS listing limits

| Payment | Holding | Why this one | Professional check |
|---|---|---|---|
| 2033-2037 | IBTM-IBTR | WInS lists no Treasury maturing Feb 2031 to Feb 2036 (`COMPETITION.md:93`) | Correct and the only choice |
| 2038 | 4.750% Feb-2037 | "the latest WInS bond available beforehand" (note, `05_...notes.md:16`) | The real market also has a 5.000% May-2037 (CUSIP 912810PU6; `snap/main/rab/trades/notes.md:263`). Per the note it is not on WInS (UNVERIFIED by me). The gap costs little (Section 5) |
| 2039 | 4.500% May-2038 | the latest WInS bond before the payment (`:17`) | Fine |
| 2040-2042 | 4.375% Nov-39, 4.250% Nov-40, 3.125% Nov-41 | 47 days before each payment | Good timing. Coupons are the issue (below) |

**Lower-coupon bonds** (20-year issues: 1.375% Nov-2040 and 2.000% Nov-2041, named in `snap/main/rab/trades/notes.md:9`):
- The Nov-2040 note says "WInS lists none for that date" (`05_...notes.md:23`). Whether the 2.000% Nov-2041 is listed has no recorded answer (UNVERIFIED).
- MODEL (`oct20/ldi/data/alt_coupons_19oct.txt`), at about the same cost:
  - 1.375% Nov-40: the share of the 2041 payment from coupons and reinvestment falls from 46% to 22%, and its −2-point shortfall from $3,283 to $1,612;
  - 2.000% Nov-41: from 41% to 31%, and $3,152 to $2,399;
  - together about **$2.4k less** at −2 points.
- **Verdict:** worth one line in the Final Report as a selection rule ("lowest coupon among listed bonds of the right date"). **Do not trade WInS for it.**

---

## 5. Timing gaps (maturity to 1 Jan)

MODEL, 19 Oct curve, $50,000 delivered per payment (`oct20/ldi/data/gap_check_19oct.txt`). "Wait" for an iBond fund runs from its holdings' average maturity to 1 Jan.

| Rung | Wait | Interest earned while waiting (base) | If bill rates are 1 / 2 points lower |
|---|---|---|---|
| IBTM, IBTO, IBTP, IBTQ | 6.0-6.4 months each | about $1.07-1.14k each | about −$0.25k / −$0.5k each |
| IBTR | 8.1 months | $1,456 | $1,135 / $809 |
| Feb-2037 | 10.5 months | $1,905 | $1,490 / $1,069 |
| May-2038 | 7.6 months | $1,365 | $1,062 / $756 |
| Nov-2039, Nov-2040, Nov-2041 | 1.5 months each | $264 each | $201 / $138 each |
| **Total** | 7 of 10 rungs wait 6+ months | **$9.9k** | **−$2.2k / −$4.4k** |

- **Relative to the cautious bases** (D and the coupon study both assume 0% while waiting), this $9.9k is a hidden cushion. **Relative to a realistic basis**, it is an exposure of about $2.2k per point that bill rates fall. About $5.8k of the $9.9k sits inside the iBond funds, where the TNA notes and the models treat the yield as locked to 15 Dec.
- **Fix:** one principle (waiting money goes to a named, WInS-listed short-term Treasury fund; re-check that SGOV is listed, `oct19/out/Caplet_Update_19Oct2026.md:381`), plus a Final Report table of all seven gaps. **Do not change any holding.**

---

## 6. Reinvestment: policy, risk and the 3r reserve

### 6a. The policy gap

- The case requires the reserve's "initial asset composition" and how it "should change, if at all" (case:95-97). Every coupon and every monthly payout before 2033 must go somewhere.
- V5 says "Hold to maturity" but has no reinvestment rule (`ips_doc_live_base_text.txt:25`). V4's "reinvest income in the holding that generated it" (`:63`) was dropped.
- **A professional would put a concept back.** The options, in order of simplicity:
  - (i) **Own-rung:** income goes back into the holding that produced it, or the next listed Treasury of the same date. This is the current design's own logic. It keeps each payment's money with its payment.
  - (ii) **Dedication:** later bonds' income pays earlier payments. This is option 4 in the coupon study; it cuts the −2-point gap from about $19k to about $5.6k (`oct19/coupon/coupon_risk_options.md:136-140`) but needs about 10 WInS trades and clashes with 3-4 filed notes.
  - (iii) **Batch** small amounts at the January review, with waiting money parked in a short-term Treasury fund in between.
- **For WInS:** a de minimis rule (no trade to reinvest a few hundred dollars) is enough.

### 6b. How big the risk is, including moves that are not parallel

Independent model; shifts are permanent from 1 Jan 2027 (`oct20/ldi/data/ldi_19oct.json`). Shortfall = how far the ten payments fall short with own-rung sizing:

| Scenario | Shortfall | Where it lands |
|---|---|---|
| Parallel −1 point | $11.7k | Spread out, rising toward 2042 |
| **Parallel −2 points** | **$22.7k** | $1.0k (2033) rising to $3.3k (2041) |
| Parallel +1 point | −$12.5k (surplus) | – |
| Bull steepener (−2 at ≤2 years, 0 at ≥10 years: rate cuts) | $9.2k | Front-loaded: 2033-2038 |
| Bull flattener (0 at ≤2 years, −2 at ≥10 years) | $13.3k | Back-loaded: 2039-2042 |
| Short end only (−2 at ≤1 year) | $5.4k | Mostly the waiting gaps |

These agree with the earlier desks in size (−2 points: $19.0k on holdings' dates and $21.3k on basis E, `numbers_refresh.md:170`). This model is a little higher because it lets waiting money and the iBond final-year cash earn shocked bill rates, and charges fund fees.

### 6c. What the 3r reserve really does

$10k bought 2 Jan 2028, MODEL (`oct20/ldi/data/ldi_19oct.json`, "reserve"):

| | Nov-2041 bond (3r) | IBTM, then reinvested at market from 2033 | IBTM, then 0% (the coupon study's 3b) |
|---|---|---|---|
| Value in 2038, no shock | $17,016 | $16,255 | $12,702 |
| Value in 2038, rates −2 after Jan 2028 | $17,406 | $14,722 | $12,702 |
| Uncovered after the reserve, −2 points, shock after Jan 2028 | **$5.6k** | $8.5k | $10.0k |
| Same, shock during 2027 (before the reserve is bought) | $9.3k | $9.9k | $11.2k |
| −1 point, steepener, flattener, short end only | All covered | All covered (except flattener with 0%: $0.6k) | – |
| Reserve needed to cover alone: −1 / −2 / steepener / flattener | **$6.7k / $12.9k / $5.6k / $7.4k** | | |

What this shows:
1. **The mechanism is locking the yield, not the price.** A 2-point fall lifts the reserve's 2038 value by only about **$0.4k** ($17,016 → $17,406): by then the bond is short, and its own coupons earn less. The real advantage over IBTM (+$2.7k at 2038 under −2 points) is that it **keeps earning about 5% to 2041 instead of being reinvested after 2032.** The explanation in `coupon_risk_options.md:67` and `:151` ("its price rises when yields fall") should be corrected before anyone defends it to a judge.
2. **The 3b comparison is biased.** The script holds the IBTM reserve at **0% from 2033** (`coupon_options.py:198`) and values the Nov-41 reserve with its own coupons growing at the purchase yield (`:204`). Fairly compared, the gap at −2 points is about $2.8k, not "$10k does the job of $25k" (`coupon_risk_options.md:67`). The ranking survives; the size of the advantage does not.
3. **$10k alone covers about a 1.5-point permanent fall.** The study's "short in 0.02% of paths" counts the whole chain: leftover → reserve → a 2033 set-aside from Laura's half → the gift above the floor (`coupon_options.py:27`). The 2033 step is doing real work in bad paths. The IPS must therefore name it as a principle: the 2033 surplus-release test, Section 12.
4. **Timing lag.** The reserve is bought in January 2028, so it cannot hedge rate moves during 2027. A professional would state this as a named residual risk. Nothing is available to fix it: the 2027 deposit has only $2.8-7.0k of room.
5. **Hedge ratio effect.** About +$10.5 PV01, so the hedge ratio rises only from 78% to about 81%. Present 3r as a **contingency reserve sized by stress**, not as a "hedge".

**Professional verdict on D1.** 3r at $10k plus the net-minimum rule is defensible, provided three things hold:
- (a) the 2033 surplus-release test is a written principle;
- (b) the reason given is "locks today's long yield for the money that may be needed in 2038-42";
- (c) the size is described as covering about a 1.5-point permanent fall by itself, with the 2033 re-pricing covering more.

On the evidence here, $15k would cover about 2 points by itself, at $5k more off the minimum. That is the team's trade-off to vote on.

---

## 7. The floor in IBTM

- **Keep it.** It is term-matched to the 2033 gift date, Treasury-only, and quoted rounded down.
- **Two small risks are inside the $3,700 margin** (bottom = (R − $3,700) rounded down to $5k, `numbers_refresh.md:140`):
  - reinvestment of its monthly payouts: −$1.6k if yields fall 2 points (`numbers_refresh.md:119`);
  - about 5.4 months of final-year cash on about $150k: −$1.4k if bill rates are 2 points lower (CALC: 150,000 × 2% × 5.5/12).
  - Together about $3.0k against $3.7k.
- **The floor and the 2033 payment share one payout date** (about 18 Dec 2032; Section 3b). A professional trigger: if IBTM's termination date or payout timing changes, sell on the exchange before its last trading day (spread about 0.05%).

---

## 8. VT sleeve size, no rebalancing, and one asymmetry

- **Size.** About $33.5k in January 2028 (`numbers_refresh.md:118`), about 7% of the $465k, against a $42k surplus over payments plus a $145k minimum (Section 2a). In pension terms this is risking only the surplus. A 50% fall costs Laura gift and flexibility money, never a payment or the minimum, **as long as VT is not also the payment backstop**. V5's "an uncovered payment is funded from her retained equity" (`:25`) breaks that. Drop it in favour of 3r plus the 2033 test (D2 option 2b, `oct19/out/Caplet_Update_19Oct2026.md:328`).
- **No rebalancing** is correct for a static floor-plus-cushion, and it is cheap and simple. "No rebalancing" must still come with a review date and triggers (Section 9).
- **The asymmetry a professional would spot.** The 2033 gift = min(top announced in 2031, floor + half of VT in 2033).
  - From 2031 to 2033, the gift's half of VT can fall (40% in 2032: typical gift $170.5k → $163.2k, `numbers_refresh.md:147`) but cannot rise past the cap. Gains above the cap go to Laura's kept half.
  - So for the co-sponsor promise, that half carries downside only. A lock-in (moving the promised amount above the floor into a Dec-2032 Treasury once the top is announced) would make the top close to certain.
  - It changes the 2031 "trade nothing" rule. The 28 Sep research recommended against a larger 2031 lock (ALT). No team vote on it is recorded (`/home/user/caplet-investment/CLAUDE.md`, insight_v1 section, "MODEL vs ALT").
  - **Keep it as a tested alternative for the Final Report's "what we would do differently".** Do not change the IPS unless the team votes for it.

---

## 9. Monitoring triggers a professional would set (concepts; owner = role)

| # | Trigger | Test | Pre-set action | When / who |
|---|---|---|---|---|
| T1 | **Funding test** | Market value of the matched holdings, plus reserve and leftover, against the remaining payments priced on the Treasury curve | Under 100%: nothing above the floor is released; the minimum is cut first (net-minimum rule) | Each January; rates analyst computes, Laura decides |
| T2 | **Reinvestment projection** | Projected shortfall in reinvested income, with rates held at that day's curve, against reserve plus leftover | Exceeds them: the 2031 minimum is reduced before announcement | 2031 valuation date; January each year |
| T3 | **Fund event** | iBond termination date, index or objective changes; fund closure; payout timing after about 28 Dec | Replace with the next earlier-maturing listed Treasury, or sell on exchange before the last trading day | As announced; rules lead watches |
| T4 | **Purchase price check** | ETF price within about ±0.15% of NAV; bond price within its yield band (the team's 25bp check) | Limit orders only; skip the day if outside | Every purchase; trader |
| T5 | **Waiting money** | Any proceeds idle more than a few days before a payment | Move to the named short-term Treasury fund | At each maturity; trader |
| T6 | **2033 surplus release** | Remaining nine payments re-priced at market; reserve need plus margin | Release only the excess to the gift (capped at the top), the rest to Laura | Jan 2033; Laura on the team's recommendation |
| T7 (optional) | **Yearly release 2034-41** | Same test each January | Release excess above need plus margin; else hold | Each January |

---

## 10. Governance: who decides what, and when

Map it to pension roles. Laura is the trustee and sponsor: she approves the policy, the 2031 range and the 2033 gift. Caplet is the investment manager: it implements by rule, reports and recommends. The case adds two limits: no outside money for the payments (case:91-92), and the advisor handles admin only (`/home/user/caplet-investment/CLAUDE.md`, Team).

| Date | Decision | Decided by | Rule or discretion |
|---|---|---|---|
| Jan 2027 | Buy the ladder (2042 rung first); any shortfall falls on the nearest rungs | Manager | Rule |
| Jan 2028 | Top up the ladder → 3r reserve (if voted) → floor in IBTM → VT | Manager | Rule |
| Each January | Funding test, reinvestment batch, fund-event check (T1-T5) | Manager reports; Laura acts on any breach | Rule-triggered |
| 2031 valuation date | Range = minimum net of projected shortfall, up to floor + half of VT (+ 3r if voted) | Laura, on Caplet's recommendation | Rule plus one judgement: the confidence statement |
| Dec 2032 to Jan 2033 | IBTM payout; T6 test; pay 2033; then the gift | Laura | Rule |
| 2033-2042 | Run-off; T7 if adopted; anything left after 2042 is Laura's | Laura | Rule |

**For the team now (competition governance).** Only the team leader trades (team rule after 7 Oct). The IPS is the frozen strategy (IPS instructions; `oct19/out/Caplet_Update_19Oct2026.md:77`). Every change above is a vote set B item for 27 Oct (D1, D2, D3, D5), not a WInS action.

---

## 11. How a professional would document "high degree of certainty"

The case asks teams to "define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions" (case:97-99). A pension desk would supply four things. All belong in the Final Report; the IPS states only the standard (D3).

1. **A definition that a test can check.** For example: every payment is matched by a US Treasury holding maturing within about 11 months before it; the plan is at least 100% funded on a stated market basis after both deposits; each remaining risk is named with a cover sized to a stated stress. Never "guaranteed" or "risk-free" (`snap/main/COMPETITION.md:168`).
2. **Four measures, each dated and with its basis named:**
   - funded ratio on a market basis and on an implementation basis (Section 2a);
   - hedge ratio, 78%, and what covers the other 22% (2b);
   - reliance on reinvested income, about $49k of $500k (2b);
   - surplus at risk, before and after purchase (2c).
3. **A stress table, one row per named risk:**
   - parallel ±1 and ±2 points;
   - one steepener and one flattener (6b);
   - the history replay since 1953 (coupon study);
   - a joint stock-and-rates fall (coupon study §2);
   - an iBond event (payout delayed or termination extended: covered by the sell-before-last-trading-day rule);
   - the 2028 deposit late or short (sponsor risk: it affects the top-up, the reserve and the floor, not the 2027 ladder);
   - US payment delay (named as the residual risk).
4. **Assumptions.** WInS-listed securities only (6 Oct email, `snap/main/COMPETITION.md:87-90`); rates model and its limits (parallel random walk, `coupon_risk_options.md:184-192`); payouts reinvested at that day's curve; no taxes (case:168).

**Probability statements.** Give at most one number, with its model and date, next to the payment result, and with range confidence kept apart from payment certainty (`oct19/out/Caplet_Update_19Oct2026.md:329`).

---

## 12. Five concepts a pension trustee would want in the IPS principles

These are labels and what each must contain. They are not sentences; the team words them, or decides not to use them.

1. **"Funding priority."** Payments first, then the floor, then growth. Each later layer is funded only after the earlier one is complete at market prices, so the 2028 top-up rule follows from this concept.
2. **"Matched and held to maturity."** A matching tolerance (how early a holding may mature before its payment), Treasury-only credit, a substitution rule for unavailable holdings, **and a reinvestment rule** (Section 6a).
3. **"Named residual risks, each with a named cover."** Reinvestment risk with its reserve and stress size; the 2027 timing lag; fund payout timing; US government risk. All covers stay inside the portfolio (case:91-92).
4. **"Surplus release test."** Nothing above the floor is announced or paid until the remaining payments are fully funded at market prices. In 2031 this is the net-minimum rule; in 2033 it is the re-pricing; optionally yearly to 2042.
5. **"Risk only the surplus."** The growth fund is never the payment backstop. Its size is limited to what is left after funding priority, and its outcome changes only the gift above the floor and Laura's flexibility.

How they map to the drill's killer questions: K1, certainty with reinvested coupons → concepts 2, 3 and 4. K2/K4 → concept 4. K5 → concept 5 (`oct19/drill/defence_drill.md:250-261`).

---

## 13. WInS: what to do (and not do) before 6 Nov

- **Before the TNA: nothing.** No holding changes; the notes cannot be edited.
- **The 5 Nov iBond payout (about $600, if WInS credits it): no reinvestment trade.** At $25 a trade, the plan's de minimis rule covers it.
- **If the team adopts 3r on 27 Oct:** either mirror it (about 8-9 more Nov-2041 bonds; yield-check first, `numbers_refresh.md:257`; at least two trades and new notes; only the team leader trades), or state once that WInS "about mirrors" Laura's plan. A professional slightly prefers mirroring, because Portfolio Analysis reads the implementation. Either is defensible if stated.
- **Last close for any voted order:** Wed 4 Nov, 4:00 pm EST (Thu 5 Nov 08:00 Sydney) (`oct19/out/Caplet_Update_19Oct2026.md:67`).

---

## 14. Limits and UNVERIFIED

- **MODEL limits.**
  - Rate shocks are permanent and instant.
  - The curve is static: cash earns the zero rate for the time remaining.
  - Each iBond fund is modelled as one bond with its average coupon and average maturity (iShares, 16 Oct), then cash at bill rates.
  - Own-rung sizing; no taxes; no WInS commissions.
  - The reserve chain draws pro rata.
- **Cross-checks passed.**
  - Liability PV $293,767 equals the numbers desk's basis B to the dollar.
  - PV01 $291 matches the desk's DV01 of $288-291.
  - The ladder cost at 0% waiting ($300,678) is within about $600 of the coupon study's $298,446 plus its own $1,627 roll-down figure (`coupon_risk_options.md:196`); the difference is about the funds' 0.07% fee.
  - Waiting-gap months from the WAM data match the model's gap column.
- **UNVERIFIED.**
  - Early-closure powers (the SAI was not read).
  - Whether WInS lists the 5.000% May-2037, the 1.375% Nov-2040 or the 2.000% Nov-2041.
  - Whether WInS credits the 5 Nov payout.
  - Whether SGOV is WInS-listed.
  - iShares page data are "as of Oct 16, 2026" even though fetched 19 Oct.
  - The real 2032 payout date (the 2026 precedent is 18 Dec).
- **Not re-run here.** The Monte Carlo and the history replay (coupon study, refreshed in `numbers_refresh.md` §6). The new model is a deterministic stress check that complements them; it does not replace them.
- **Parallel work.** Other Wave A folders (`oct20/reserve/`, `oct20/redteam3r/`) may cover 3r. Their outputs were not read for this file.

## 15. Files (all under `oct20/ldi/`)

- `ldi_second_opinion.md` (this file)
- `scripts/ldi_model.py`: independent cash-flow, PV01, scenario and reserve model. Run: `venv/bin/python -I scripts/ldi_model.py data/tsy_202610.csv 10/19/2026 data/ldi_19oct.json`
- `scripts/funding.py` (funded ratios, surplus at risk), `scripts/gap_check.py` (waiting gaps), `scripts/alt_coupons.py` (low-coupon alternates), `scripts/divs.py` (payout variability), `scripts/keyfacts.py` and `html2txt.py` and `pdf2txt.py` (page extraction)
- `data/ldi_19oct.json` and `ldi_19oct_stdout.txt`, `data/funding_19oct.json`, `data/gap_check_19oct.txt`, `data/alt_coupons_19oct.txt`, `data/div_summary.txt` and `data/div/*.json`, `data/ibond_keyfacts_live.txt`, `data/tsy_202610.csv` (copy of `oct20/numbers/data/tsy_202610.csv`)
- `web/p_*.html` and `.txt` (iShares product pages); `web/docs/` (IBTM and IBTR summary prospectuses, trust prospectus with the 15 Oct 2026 supplement, IBTM fact sheet, 2026-28 distribution schedule; PDF plus text)
