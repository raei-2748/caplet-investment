# Judge: the bond desk (Mon 9 Nov 2026)

Persona: a fixed-income portfolio manager who has run liability-matched Treasury books for insurers. I mark only on
Wharton's Final Report instructions (`WHARTON_NORTH_STAR.md` section 0) and the case. I check every claim about bonds, ETFs, rates and
certainty first, and I discount any promise that has no mechanism behind it.

Read: north star section 0, the Laura Gao case, the FINAL IPS as submitted, `INTENT.md`, `SKELETON.md`, `NUMBERS.md`
sections 1, 2, 3, 4, 8g and 8h. Nothing else in `keel/final_report/`. Where I cite section 8f or section 5 I go by their titles only.

Scale: 5 = a semifinal-grade passage a professional would not fault; 4 = strong, one fixable gap; 3 = competent, a
professional reader would mark it down; 2 = weak or partly wrong; 1 = fails a requirement.

One independent check of my own (method at the end): a pooled coupon book, sized to need no reinvestment income,
costs about the same as Keel's margin design and passes every rate test. That drives weakness 1.

---

## 1. Scores by part (if written exactly to this plan)

| Part | Score | Reasons |
|---|---|---|
| 2.1 What the book is | 3 | "Laura's whole plan in miniature" is the right key, but the IPS says the first $300,000 buys ten Treasuries and nothing else, while the WInS $300,000 holds 8.84% VT and a floor stand-in. A judge needs a three-column mapping (WInS weight, weight in Laura's plan in Jan 2028, what it pays for) in the first 120 words, or it reads as inconsistency. Bond identifiers are still "(WInS id)" and "532281 (probably)". |
| 2.2 Construction and allocation | 4 | "The allocation is the rule, not a target mix" is the strongest sentence in the plan and true to the IPS. But "no WInS bond for those years" must be shown as a WInS listing fact, with the date checked. A bond reader knows real Treasury notes mature every quarter of 2032-2036. The cost of using funds instead (fees $1,098, a cash wait of up to about 2%) belongs here too. |
| 2.3 Diversification and risk | 3 | VT's breadth is fine. "Diversified by date" is a misuse a professional would reject: spreading maturities is matching, not diversification. The risk list leaves out the duration gap (7.76 against 9.94 years) and fund-structure risk. It would drop to 2 if "diversified by date" survives into the prose. |
| 2.4 Roles of the key holdings | 2 | This is mostly the IPS and Exhibit 1 again. Wharton says "without repeating the content of your IPS". Put a "Pays for" column in Exhibit 1 and move the 120 words to 2.5. |
| 2.5 How well it was done | 3 | Right instinct: professional measures, and "WInS gains are not evidence". But 180 words is too thin for the place where Portfolio Analysis is won. Several measures are missing: the WInS book's duration and DV01 against the liabilities, coverage per rung, the fact that the book carried no reinvestment provision, the 10.5-month early Feb-2037 bond, and implementation cost in basis points. The cash row also has a fault (weakness 3). |
| 3.0 The recommendation in one paragraph | 4 | Answer first, three numbers. But "$427,000 ... against $500,000 still owed" reads as 85% funded to anyone who skims. Say "about 107% funded at today's forward rates" ($427,028 against $399,089). |
| 3a Commitment and operating reserve | 3 | The run-down with no rebalancing and Exhibit 2 answer the case's composition question well. But "high certainty" means "pays in full in 94% of 16-year rate histories, worst $12,117 short", and the plan names no Treasury backstop for the other 6%. That contradicts the IPS's "barring a US default, none of your 10 operating payments will depend on ..." A cheaper and stronger mechanism exists (weakness 1). |
| 3b Facility contribution and flexibility | 3 | It states the cost of VT against an all-Treasury plan plainly, which is rare and good. "Responsible" has no test, though, and the cap rule is missing. The kept half and the reserve's overflow are both pro-cyclical (weakness 4). The 2028 deposit funds the completion and margin, which is part of the payments' certainty, and the plan does not say so. |
| 3c The 2031 range and confidence | 3 | Two layers of confidence (owned after the move; a distribution of announceable ranges before it) is the most sophisticated idea in the plan. The arithmetic and definitions do not yet hold (weakness 2). The bottom's uncertainty from today ($93k-$140k, 1-in-20) is left out of 3c. |
| 3d Words for co-sponsors | 3 | The right elements: owned bottom, conditional top, date, what it funds, what it does not promise. Nothing yet lets a co-sponsor verify the promise. A professional reader trusts a custodian statement, a separate account and a maturity date far more than any adjective. |
| 3e Assumptions, limits, what to watch | 4 | The monitoring table ("signal, what it changes, what it never changes") is professional. Three things are missing from the assumptions: the stock-bond correlation (modelled as independent), the overlapping-window caveat on the history test, and the January 2028 curve as the single most important thing to watch. |
| 3f Team Reflection | 3 | Real events, each tied to a change in the recommendation, is the right standard. But 300-400 words is about 15% of Section 3 for a full criterion, Articulation. Make it 450-550 words, or let 3a-3c each carry one sentence of "we disagreed; this test settled it". |
| Exhibit 1, holdings table | 3 | It is required, so precision is worth points. "Cash $4,823.21" includes $1,309.42 that was spent; WInS shows $3,513.79. Two identifiers are placeholders. Both are easy to fix and could cost the "Actual holdings" requirement if left. |
| Exhibit 2, the reserve running down | 4 | It answers "how its composition should change ... as the annual payments approach and are made" directly. Add the funded ratio each year (107% falling to 100%+ at forwards) and the month each holding pays out. |
| Exhibit 3, candidates | 3 | None of the three candidates is the best one. A scenario matrix answers Wharton's "factors that could affect it" and the case's "favorable and unfavorable market outcomes" in a quarter page: rows for forwards, rates 3 points lower, a joint recession and an inflation world; columns for payments, bottom, top and kept half. |

Plan as a whole: about 3.2 out of 5. As planned, a solid top-quartile report. It is not yet a semifinal certainty, because the
two numbers a bond reader checks first (certainty and range) have holes that need numbers to close, not more words.

---

## 2. The five weakest points, most serious first

**1. The payments' certainty depends on reinvestment rates, and the IPS says it does not.**
Design A at Keel's call pays in full in 94% of historical windows and is up to $12,117 short in the rest. Section 2's
table also shows it $22,192 short if interest earns nothing. "Barring a US default, none of your 10 operating payments
will depend on a share price, or on anybody else's money" stays literally true. But the payments then depend on
something the IPS did not name, and the plan gives no Treasury backstop for the shortfall. In the 6% of windows, the money
would have to come from the kept half (shares) or from outside (banned), so the IPS sentence fails exactly there.
- *Fix:* run the reserve as one pooled book rather than ten silos. All ten are still bought in January 2027, so the IPS's
  words hold. Every coupon goes into Treasury bills, or the next rung, and pays the next payment due. The book is sized
  so that it pays all ten even if no coupon ever earns anything.
- *Cost:* Keel's own table gives this design (B, sized so interest is never needed) at $319,687, below the $323,436
  of Keel's call. My rough independent model gives $317,400 with no minimum, and $319,400 with every rung held at
  $15,000 face or more. Scaled to the engine's level, that is about $320,000-$323,000: no dearer than the margin.
- *What it buys:* certainty becomes "every payment paid even if no coupon earns a cent", by construction and in every test. The
  gift's bottom barely moves.
- *Why it is in scope:* the IPS is silent on coupons. "Each Treasury's interest buying more of the same Treasury" is
  Keel's reading, not Caplet's text, and the reserve's "initial asset composition" is a Final Report recommendation the case requires.
- *Checks still needed:* compute it in the team's engine with all ten held, and reconcile it with TNA note 2's IBTM for
  "her first $50,000 payment" (IBTM would pay part of it, with pooled coupons paying the rest).
- *If the team keeps design A:* say in 3a, with the number, what pays the shortfall in the 6% of histories. Do not let
  "barring a US default" stand alone.

**2. The 2031 range is not yet one rule, and its central case lands outside it.**
- *The top uses the wrong deduction.* The top is "the top less 2.5%": $138,735 to $135,267 to $135,000. But the floor part of the top needs its own
  4.1%: $115,929 x 0.959 + $22,806 x 0.975 = $133,412, which is $130,000 rounded down. So "both ends are money she owns" is
  not quite true at the top.
- *The central case lands outside the range.* The defined contribution is floor plus moved half, $138,735 at forwards, which is above the stated
  $135,000 top. So "falls inside it in every path" holds only if the gift is capped, and the plan states no cap.
- *The bottom understates what is owned.* After the move the bottom ($110,000) is about $23,000 below money already owned in Treasury funds. The
  case says a meaningful contribution signals viability, so under-signalling has a cost too.
- *Fix:* one written rule.
  - Announced bottom = floor payout x (1 - 4.1%), rounded down.
  - Announced top = bottom + moved half x (1 - 2.5%), rounded down.
  - The gift = the lower of the actual payout and the announced top; any excess joins the kept half.
- *Two further additions:* state in one line why the bottom stays at the floor after the move, or narrow the range. In 3c, give both ends'
  spread from today (bottom $93k-$140k, top $111k-$171k, 1-in-20), not the top's alone.

**3. Section 2 grades itself too softly, and the holdings table has an accounting slip.**
- *The cash row.* "Cash $4,823.21" includes $1,309.42 of commissions and accrued interest that were spent. A judge who compares
  this with WInS's $3,513.79 sees a table that does not match "Actual holdings".
  *Fix:* put accrued interest into each bond's amount (it was paid for that bond and comes back with the first coupon) and
  commissions into each holding's cost, or onto a separate "Trading costs" row. Cash then equals WInS cash, and the total is still
  $300,000. Fill all five bond identifiers from the final export.
- *Measures missing from 2.5.* It needs the measures a professional uses on a matched book:
  - Coverage per rung (WInS holds 67-72% of each $50,000, as scaled).
  - The duration gap: instruments 7.76 years and $234 a basis point, against liabilities at 9.94 years and $300. TNA note 1 said
    "duration-matching", so explain it here before a judge finds it.
  - The book carried no provision for reinvestment.
  - The Feb-2037 bond pays the 2038 payment 10.5 months early. If WInS listed anything maturing later in 2037, say why it was not used.
  - Implementation cost in basis points.
  Take 2.4's 120 words to pay for this.

**4. The flexibility is pro-cyclical, and the model hides it by treating rates and shares as independent.**
Think of the world the IPS itself fears: a recession. Laura's advances come late, co-sponsors cut, shares fall and rates fall. In that world:
- The kept half (VT) shrinks (1-in-20: $12,000).
- The reserve's overflow (about $28,000 at forwards) falls to nothing, because the margin is used up by lower reinvestment rates.
So both cushions fail together, in the one state the IPS says the portfolio should counterbalance. The house model's
"yield moves ... independent of shares" understates that joint state.
- *Fix:* put one joint stress row in Exhibit 3. A historical replay with rates and US stocks from the same months would do,
  starting Jul 2007 (already the worst rate window), set beside an inflation world (rates up, shares flat). Report the
  payments, the bottom, the top and the kept half for each. Name the correlation assumption in 3e.
- *Define "responsible" with a test:* for example, the kept half covers a 10% stronger Taiwan dollar on the gift in 19 of 20 paths.
  Then say plainly how often it does not. Pooling (weakness 1) also helps here: it removes the reserve's exposure to falling rates,
  which makes the IPS's "counterbalance" truer.

**5. Liquidity is never named, and the 2028 deposit's role in the payments is understated.**
- *Liquidity.* The Client Knowledge criterion lists "liquidity needs" by name, and the skeleton never uses the word.
  *Fix:* one paragraph or table row covering:
  - When each payment's cash arrives (half a month to 10.5 months early).
  - That every holding is a listed Treasury or ETF that can be sold any trading day if the plan must change.
  - That the gift is cash in December 2032.
  - Where the kept half sits.
- *The 2028 deposit.* The IPS's own thesis is that Laura's income is a risky asset, yet about $24,500 of the 2028 deposit
  (completion plus margin) is part of the payments' certainty.
  *Fix:* in 3a, one sentence and one number: what the 2027 deposit alone secures, and that the 2028 deposit's first dollars
  go to the payments before the gift. Section 5 of NUMBERS exists for this.

---

## 3. Claims that are imprecise or wrong as fixed-income practice

1. INTENT: "about $427,000 on 1 Jan 2033 at today's forward rates against $500,000 still owed". This compares a market value with an
   undiscounted sum. *Correction:* "worth about $427,000 against the $399,000 the ten payments are worth at the same rates,
   about 107% funded".
2. INTENT: "the 2033 gift falls inside it unless the US Treasury defaults". At central rates the defined gift ($138,735)
   is above the stated top ($135,000), so a cap is needed. The floor and moved half are also iBond ETF shares, not Treasuries.
   *Correction:* "... unless the US Treasury defaults or a fund fails to work as its prospectus says".
3. NUMBERS 4: "That is the top less 2.5%, rounded down to $5k". The floor part needs 4.1%.
   *Correction:* $133,412, so $130,000.
4. NUMBERS 4: "both ends are money Laura owns in Treasuries maturing late 2032". *Correction:* "in a Treasury fund that winds up in
   December 2032 and pays its net asset value". The plan says this elsewhere; keep the wording exact everywhere.
5. SKELETON 2.3: "the ladder is diversified by date (one holding per payment), not by issuer". *Correction:* the
   promised money is deliberately concentrated in the one issuer whose default is the plan's only named risk, and
   matched by date. Diversification lives in VT. If anything, the ladder diversifies structure (five funds, five
   bonds), which is worth one line.
6. TNA note 1's "duration-matching" (as quoted in NUMBERS 1). The book is maturity-matched: the instruments' duration is 7.76 years,
   against 9.94 for the payments. *Correction:* "each payment has a Treasury maturing just before it; the
   duration gap is the reinvestment risk, and [the pooling / the margin] closes it".
7. NUMBERS 2: "all ten paid in full in 94% of every 16-year stretch of US rates since 1962". These are 585 overlapping monthly
   windows, worth about three independent 16-year periods, and each one is scaled in proportion to today's forwards.
   *Correction:* present it as "paid in full in every rate era except the one that started in 2007". Do not present
   it as a 94% probability.
8. NUMBERS 8h: "Nothing is bought or sold after January 2028". Under design A every coupon buys more of its own rung.
   *Correction:* "nothing is sold, and nothing is added except each holding's own interest". Under pooling:
   "except bills bought with coupons".
9. INTENT's trade-off: "a share of world growth that is never promised to anyone". The moved half's growth is promised
   from 2031. *Correction:* "half of it".
10. The IPS pitch's "immune to markets" and the IPS's "pay what they say" (INTENT already flags both). The T-bonds held to maturity pay
    coupons and par. The funds pay net asset value. All ten, under design A, depend on reinvestment rates.
    *Correction:* "immune to share prices; held to the end, price swings do not matter". Pooling makes the rest true.
11. NUMBERS 2 calls design B a contradiction of the IPS. That holds only as B was specified (eight bought). A pooled book that
    holds all ten does not contradict "buy 10 Treasuries ... each maturing just before it's needed".
12. Exhibit 1: "Cash $4,823.21". Spent money labelled as cash (weakness 3). "532281 (probably)" cannot appear in a
    submitted table.

---

## 4. What would make this the best report among about 2,300

1. A definition of certainty a bond desk would sign: every payment paid even if no coupon earns a cent, with its cost in dollars.
2. One line of funded ratio and duration that shows the team knows matching from immunising (107% funded at forwards).
3. A range rule, not just a range: deductions, cap, where any excess goes, both ends' 1-in-20 from today.
4. One scenario matrix covering recession, inflation and forwards, with payments, bottom, top and kept half: honest about the pro-cyclical cushion.
5. Co-sponsor words that offer proof they can check: the fund, its December 2032 wind-up, a separate account, a custodian statement on request.
6. A Section 2 that grades the WInS book with professional measures and admits its gaps in numbers.
7. A reflection where every event changed a number that appears earlier in the report.
8. Exact words throughout: "Treasury fund" where it is a fund, "net asset value" not "par", no "immune".

---

## 5. Where other reasonable judges would disagree with me

- **The conservative bottom.** A co-sponsor-minded or generalist judge may reward a $110,000 bottom with near-certainty
  as exactly what the case's credibility warning asks for: under-promise, deliver the top. I mark down the unexplained
  $23,000 gap below owned money; they may mark it up.
- **Reinvestment risk.** Most judges will not know it exists. To them, "94% of histories" may read as rigour, and they
  would not reward the pooling fix. Professional judges (Aberdeen) would notice.
- **Pooling and the IPS.** A judge strict on "not an opportunity to create a new strategy" may see a new coupon policy
  as revising the IPS. I see it as the reserve composition the case asks for, on a point the IPS left open.
- **Conservatism overall.** An equity-minded judge may find 89.55% Treasuries and 8.84% shares too timid for a client who
  takes "thoughtful risks". I think the liabilities justify it, and the plan's deletion test (VT at zero leaves the
  payments untouched) answers them.
- **The holdings table.** At cost, or final weights times $300,000: both readings of Wharton's wording are defensible,
  and judges will differ. Neither will be marked down if the cash row is clean.
- **The reflection budget.** Some judges think 300 vivid words beat 550, and they may be right if every event carries a number.

---

## 6. On the skeleton's open questions (brief)

- Open Section 2 with one sentence of the governing thought: judges read Section 2 first. Keep 3.0 for the numbers.
- Keep Wharton's order (commitment, reserve, contribution, range, confidence, words). Judges mark with that checklist
  beside them, so 3b before 3c.
- Yes, the monitoring table can carry most of 3e. Spend the freed words on the joint stress and liquidity.

---

## Method of my check (rough; the team's engine must redo it)

6 Nov par curve, bootstrapped semiannually. The five iBond funds are modelled as par bonds maturing 15 Dec of their year,
and the five T-bonds at their real coupons and dates. Interest is held at zero. "Silo" sizes each rung from its own cash flows; "pooled"
solves the linear programme in which the cumulative cash by each 1 January must cover the cumulative payments, with
vertex enumeration over 10 variables and 10 constraints.
- PV of the ten: $302,108 (engine $301,544).
- Silo: $333,778 (engine, design A sized so interest is never needed: $337,836).
- Pooled, no minimum: $317,353, holding only eight (engine B: $319,687).
- Pooled with every rung at least $15,000 face: $319,370.
My model runs $1,500-$4,000 below the engine. Scaled, the pooled book holding all ten costs about $320,000-$323,000,
against $323,436 for Keel's call.
