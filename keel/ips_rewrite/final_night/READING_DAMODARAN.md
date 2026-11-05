# Reading: Damodaran, Corporate Finance (NYU Stern), for the final-night IPS

R4 (Library – Damodaran), Thu 5 Nov 2026, ~00:05–00:40 Sydney (6 Nov). Reader only: no prose for the page.
Strategy read against: `rounds/R4_ips.txt` (each commitment bought in Treasuries on the day it is made; 2027 ladder;
2028 Treasury fund sets the smallest contribution, interest-sized slice in one world fund; both ends of the 2031 range
bought before it is said; the reinvestment gap priced as if waiting dollars earn nothing).

## What I read (all accessed Thu 5 Nov 2026, Sydney)
| Source | URL | What |
|---|---|---|
| Lecture index | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/cflect.htm | Course map; packets updated "for Spring 2026 class" |
| Packet 1 (Sessions 1-15: objectives, risk & return, hurdle rates, investment analysis) | https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket1spr26.pdf | 346 slides, full text extracted; every slide keyword-scanned, ~45 read in full |
| Packet 2 (Sessions 16-26: capital structure, debt design, dividend policy, valuation) | https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket2spr26.pdf | 263 slides, full text extracted; ~45 read in full; charts on slides 151 and 184 read as images |
| Current implied ERP | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm | "Implied ERP on November 1, 2026" line |
| Historical implied ERP table | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/implpr.html | 1960 onward (not used for a number) |
Not read: the webcasts (video), the topic PDFs (older copies of the same slides), the blog. Slide numbers below are
the page numbers of the Spring 2026 packets ("P1 S108" = packet 1, slide 108).

## The live numbers (verified from his home page, 5 Nov 2026)
- Implied ERP on 1 Nov 2026 = **4.41%** (trailing 12 months, adjusted payout), on a US Treasury rate of **5.29%**.
  Alternatives on the same line: 3.79% (cash yield), 5.81% (10-yr average CF yield), 3.43% (net cash yield), 3.39%
  (normalised). Previous month 4.20%.
- He now nets a **0.22% default spread** out of the US Treasury rate ("adjusted dollar riskfree rate of 5.07%").
  So Damodaran himself no longer treats US Treasuries as strictly default-free. That supports the never-say list:
  "near-ironclad" and "held to maturity repays what it promised" are fine; "risk-free" is not.
- Implied expected return on US stocks ≈ 5.29% + 4.41% = **9.70%** a year (arithmetic, his method, S&P 500 not VT).
  Ahaan, Book 9: don't pin a market figure on VT. Any use says "US stocks, Damodaran, 1 Nov 2026".

## The ten strongest concepts, ranked

**1. A riskfree asset needs two things: no default, and no reinvestment.** P1 S108: "There can be no uncertainty about
reinvestment rates, which implies that it is a zero-coupon security with the same maturity as the cash flow". P1 S109:
"the rate on a zero coupon default-free bond matching the time horizon of the cash flow".
- *Laura:* this is the textbook statement of the ladder's own weakness. Coupon Treasuries and the iBond funds pay
  interest before each January, so the ladder passes test one and fails test two. The plan's rule (price the gap as if
  waiting dollars earn nothing, then fund it) is exactly how you turn a coupon ladder back into a zero for this
  purpose. The weakness paragraph stops being a confession and becomes the definition applied.
- *Where:* IPS (one clause can carry the idea without the name). Final Report cites S108-109.
- *Distinctive.* Most teams will call a bond ladder "risk-free"; this shows we know why it isn't, and fixed the part
  we could. *Critique:* test one isn't perfect either (the 0.22% spread above). Say it once, flat, in the Final Report.

**2. Discount a cash flow at a rate that matches its risk, not its funding.** P2 S237: "the discount rate used should be
consistent with both the riskiness and the type of cashflow being discounted"; "mismatching cashflows and discount rates
can lead to serious errors". P1 S110: currency matching, a dollar cash flow takes a dollar riskfree rate.
- *Laura:* the payments are fixed, so they take the Treasury rate whatever she owns. Costing them at a share return is
  the mismatch Damodaran warns about. This is the R4 opening's "one honest cost", with a corporate-finance pedigree
  beside the pension one.
- *Where:* already the IPS spine; Final Report cites S237 and S110.
- *Generic in theory, distinctive in use:* few school teams will make it the rule that drives every move.

**3. Debt design, run backwards: match the cash flows on one side to the cash flows on the other.** P2 S109: "make the
cash flows on debt match up as closely as possible with the cash flows that the firm makes on its assets. By doing so,
we reduce our risk of default". P2 S112 lists what to match: duration, currency, inflation (fixed vs floating),
cyclicality.
- *Laura:* her liabilities are fixed, so she designs the assets instead, on the same four lines. Duration: one
  maturity before each January. Currency: dollar payments, dollar Treasuries. Inflation: fixed nominal payments, fixed
  nominal bonds (no inflation-linked need). Cyclicality: her 2028 income is cyclical, so it is not paired with a large
  share bet. The fourth line is the one teams miss, and it is in the plan already.
- *Where:* Final Report (a four-row table is the natural exhibit). The IPS already makes the cyclicality point.
- *Distinctive:* applying a CFO's debt checklist in reverse to a client's liabilities is an unusual, checkable move.
  *Critique:* the facility costs may be in Taiwan dollars (case), so the currency line is matched for the payments,
  not for the building. That is a reason the kept half stays flexible, not a flaw in the ladder.

**4. Financial flexibility is unused capacity, and the less certain the future, the more you keep.** P2 S23:
"Proposition 5: Other things remaining equal, the more uncertain a firm is about its future financing requirements and
projects, the less debt the firm will use". P2 S13 lists "Loss of Future Flexibility" as a cost of debt.
- *Laura:* a number said to co-sponsors behaves like debt: a fixed claim on her future. Committing everything is
  borrowing to capacity. Because the building's cost and timing are uncertain (the case), she should hold some claim
  capacity back. This gives the "other half stays hers" choice a reason from capital-structure theory, not just caution.
- *Where:* IPS (the half kept is already there; the reason could be one clause). Final Report cites S23.
- *Distinctive:* treating a pledge as debt capacity is a genuine synthesis. *Critique:* Prop 5 doesn't say how much to
  keep; "half" still needs its own reason (modelled in the Final Report).

**5. Dividends are sticky, and cuts are punished far more than raises are rewarded.** P2 S151 ("Dividends are sticky":
most US companies pay the same dividend as last year, every year 1988-2025). P2 S184 (chart read from the slide):
market reaction 1962-74 about **+0.8% to an increase, about −6% to a decrease**; 1975-87 about +0.6% / −3.5%; 1988-2000
about +0.2% / −1.8%. P2 S176: the signalling story.
- *Laura:* her 2031 range is a dividend announcement to co-sponsors. Once said, they anchor on it; a cut later is read
  as bad news about the project. So the range is set like a mature dividend: only at a level already bought, and with
  room to raise later rather than cut. That is the both-ends-owned rule, seen from the payer's side.
- *Where:* Final Report (cite the chart); the IPS sentence about co-sponsors planning around any number already
  carries the idea.
- *Distinctive.* *Critique, and use it honestly:* the slide's own title is "Both dividend increases and decreases are
  becoming less informative", and the asymmetry shrank over time. Co-sponsors are not a stock market; the analogy is
  about credibility, which the case states directly ("could damage her credibility"). Don't quote −6% as a fact about
  donors.

**6. Miller-Modigliani says payout doesn't matter only under assumptions that fail for Laura.** P2 S165: dividends are
irrelevant if a firm can "issue new stock, with no flotation costs or signaling consequences, to replace this cash" and
doesn't waste retained cash.
- *Laura:* both assumptions break. She can't raise money later without cost (no outside money for the payments,
  case), and a shortfall has a signalling cost (credibility, case). So for her the payout decision, how much to promise
  and when, really does matter. That is why the IPS spends a paragraph on the range.
- *Where:* Final Report (a neat "why the range is a real decision" paragraph).
- *Distinctive:* turning MM's assumptions into the reason a policy matters is the kind of logic Book 9 asks for.

**7. "Companies don't have cash. They hold cash for their stockholders."** P2 S147, with P2 S202-205 (Disney "frittered
away this flexibility" on Capital Cities and Go.com).
- *Laura:* the kept half is held for Laura, not for the building. Damodaran's Disney case is the corporate version of
  the soft-budget point in the creativity shortlist (idea 4): spare cash that management can call on gets spent.
- *Where:* Final Report. Supports "promised to no one" in the IPS.
- *Generic quote, clever pairing.*

**8. The hurdle rate: every risky dollar must beat the riskless rate plus a premium.** P1 S87: "Hurdle rate = Riskless
Rate + Risk Premium". With his 1 Nov numbers, US stocks are priced for about 4.4 points a year above Treasuries.
- *Laura:* the share slice is judged against the Treasury it replaces, not against zero. It earns its place only as
  the part of her money allowed to be wrong, which is how R4 already frames it. The premium is real but it is not huge
  next to 5%+ Treasuries, which is the reason the slice is interest-sized and not larger.
- *Where:* Final Report (with the ERP number and date). IPS: no number (Book 11).
- *Generic.* *Critique:* implied ERP is a US-market estimate and moves monthly (4.20% to 4.41% in one month).

**9. Real options: the option to delay has value, more so when the future is volatile.** P1 S333-335: "the option to
delay taking a project... The value of these rights increases with the volatility of the underlying business";
S337: the option to abandon.
- *Laura:* she doesn't name a range until 2031 and doesn't hand money over until 2033. Waiting to commit is an option
  she owns; the plan keeps it rather than pledging in 2027 off a forecast. The unpromised half keeps a second option
  (to give more later, or to fund something else).
- *Where:* Final Report. *Critique:* the option has a cost (co-sponsors want a number early), which the case fixes at
  2031, so the plan isn't choosing the delay; it is using the delay it is given well. Don't oversell it.

**10. The risk of an asset is the risk it adds to what you already hold.** P1 S101: "The risk of any asset is the risk
that it adds to the market portfolio".
- *Laura:* her 2028 income already moves with the economy, so shares add more risk to her than to a salaried saver.
  That is the formal version of R4's "Laura's fortunes already ride on the economy".
- *Where:* Final Report citation for an idea already in the IPS. *Generic.*

## Checked and set aside
- **Hamada / leverage of the surplus** (pasted list): not in these packets as applied to liabilities; the capital
  structure slides lever a firm's equity beta. The idea is sound, but our plan holds almost no shares against the
  payments, so the "60/40 is secretly aggressive" warning describes a plan we didn't choose. Final Report at most, as
  the reason we refused a balanced fund.
- **IRR's reinvestment assumption** (P1 S308): the same point as concept 1, weaker. Use S108 instead.
- **Country risk premiums / Taiwan ERP:** irrelevant; nothing is invested in Taiwan.

## For the Writer, in one line each
1. S108: a bond is riskless for a date only if there is nothing to reinvest. That is precisely the ladder's gap, and
   the plan's fix (priced as if waiting money earns nothing) is the textbook remedy.
2. S23: a number said to co-sponsors is debt, and the less certain the future, the less debt you take on. That's why
   half stays unpromised.
3. S151/S184: dividends are sticky because cuts are punished, so a range is set like a dividend, only where it is
   already paid for. (The slide warns the effect has faded, so treat it as an analogy, not donor evidence.)
