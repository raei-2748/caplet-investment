# Final Report: SKELETON (Writing Department 1.3, Fri 6 Nov 2026)

> **This is a skeleton, to be redone once Wharton's Final Report instructions land (Mon 9 Nov, 9:00am ET = Tue 10 Nov
> 01:00 Sydney).** Section order, length limits and required parts will change to match them. Due Sat 5 Dec, 09:00
> Sydney. Built from the case's required outputs (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`),
> Wharton's five criteria (`keel/WHARTON_WORD.md`) and the final IPS (`final_night/FINAL/ips.txt`), which the report
> must reflect and evaluate. It may not redesign the strategy (Wharton: "may not revise its investment strategy").
> Every idea row is from `../FINAL_REPORT_BANK.md` (B1-B22, all placed below). Every number cites its row in
> `../FACTS.md` (C = case/holdings, N = model) and carries its date. Model numbers must be re-run on one curve,
> one date, before drafting (several are from different curves: N6 22 Oct, N7 15 Oct, the rest 4 Nov).

## How to read each section
**Job:** what the case or Wharton asks. **Spine:** the one idea the section argues. **Evidence:** bank rows and
numbers. **Watch:** words or claims that would break a fact check or the October record (`../FACTS.md` s4,
`../CONSISTENCY.md`).

---

## 1. The strategy in one page (Investment Strategy; Creativity and Presentation)
- **Job:** restate the IPS strategy and why it suits Laura, so every later section can point back to it.
- **Spine:** whenever Laura commits to a sum, she buys the Treasuries that will pay it that day; shares only ever hold
  money nobody is counting on. Caplet XR: X for the ten holdings, R for redemption.
- **Evidence:** B20 (pricing pedigree: US public pensions may discount at expected returns; Novy-Marx & Rauh;
  Andonov, Bauer & Cremers 2017; verify before printing); B8 (order of purchase: money she has buys the payments,
  money that can shrink carries what can wait); B10 (pension-buyout discipline applied to a pledge); B21 (a "balanced"
  60/40 holds about 1.8 times the surplus in shares, so it is a geared bet on the number she names); B22 (the trade
  against all Treasuries: about $190k owned vs about $145k minimum plus shares, re-run on today's curve); B12 (the
  name: Caplet XR kept; Datum was the runner-up, Caplet's call).
- **Numbers:** C1, C2, C3; N9 (shares about 6.6% of Laura's money).
- **Watch:** "cash-flow matching" or "each payment has its own holding", never "immunised" or "duration-matched"
  (N10: average timing 7.6 vs 10.0 years); never "risk-free" or "guaranteed".

## 2. Implementation review: the WInS portfolio (Investment Strategy: "consistency with the team's IPS")
- **Job:** evaluate how well the trades implemented the IPS. WInS gains or losses are not scored and are never added
  to Laura's projections (Wharton's halfway email).
- **Spine:** the WInS book is Laura's plan after the 2028 deposit, scaled to $300,000; eleven trades built it in two
  days and nothing was traded after 8 Oct, which is what a plan that changes only on fixed dates should look like.
- **Evidence:** holdings table (C4, C6; FACTS s2a, 23 Oct export): IBTM does two jobs (first payment and the minimum
  stand-in); B3 (the funds trade a promise of par for liquidity, TNA reflection 2); the WInS pie labels the iBond
  funds "Long Equities", so explain the true mix (about 91% Treasuries).
- **Honest gaps to own:** no Treasury maturing Feb 2031-Feb 2036 on WInS, so funds stand in; the 2037 and 2038 bonds
  repay 10.5 and 7.5 months early (reinvestment, see section 4); the ladder's cost moved over $300,000 by November
  (N1, N2).
- **Watch:** never present the book as her 2027 purchase (FACTS s2a); quote the three TNA notes exactly as submitted.

## 3. The operating reserve: size, composition, and how it changes (case: "recommend its size and initial asset composition and explain how its composition should change, if at all")
- **Job:** the reserve's size on 1 Jan 2033, what it holds, and how it changes as payments are made.
- **Spine:** it changes by itself: one holding is redeemed before each January, so the reserve shortens by a year at a
  time and never needs a trade. The answer to "if at all" is "only by redemption".
- **Evidence:** B15 (the two pension methods; we use the second, one holding per payment, no rebalancing); B18 (why
  buy in 2027: $300,000 bought all ten payments on only 8.4% of trading days since 2000, and on none from 13 Jul 2007
  to 23 Sep 2026; MODEL, historical curves; reconcile with the "one month in four since 1871" figure before use);
  B6 (cover order if the gap can't be met: payments, then range, then flexibility); B3.
- **Numbers:** N1 (cost of the ten payments, 4 Nov: $300,608, payment-date basis; quote one basis only, N1b); N3
  (chance the 2028 deposit tops up the ladder, 65% on 4 Nov, MODEL with assumed rate volatility); a reserve size in
  2033 dollars, re-run.
- **Exhibit:** a ten-row table, holding by holding: what it is, when it ends, which January it pays, and its reliance on
  reinvested interest.
- **Watch:** "before each January", never "just before"; funds pay net asset value, "not fixed" (IBTM and IBTO notes).

## 4. A high degree of certainty: definition, test and evidence (case: "define … explain how they evaluated … identify the assumptions") — SAMPLE BELOW
- **Job:** define it, test it, state the assumptions.
- **Spine:** certainty is a property of what she owns, tested on the day the ladder is built; the model measures only
  the one gap left (money waiting to be reinvested).
- **Evidence:** B7 (Damodaran's two conditions for a riskless asset: no default, no reinvestment); B16 (Bodie: time
  makes a loss rarer, not smaller; shares beat a 5-year Treasury held to maturity about 55% of the time on today's
  assumptions; give Siegel's side fairly); B14 (why we never sell as prices fall: 1987 portfolio insurance; ours is
  static, so no gap risk from a fast fall; never call it CPPI); B10 (one borrower, the US government: the one
  concentration accepted on purpose).
- **Numbers:** N6 (payments met in full under the zero-reinvestment rule: 100% base, 100% if yields fall 2 points for
  good, 98.71% if yields are 1 point lower and the 2028 deposit is halved; **22 Oct curve, J.P. Morgan 2027 7.5%,
  re-run before use**); N7 (coupon shortfall if yields stay down: STALE, 15 Oct curve, do not quote until re-run).
- **Watch:** Damodaran now nets a 0.22% US default spread, so never "risk-free".

### Sample paragraph (§4)
Most plans would define a high degree of certainty as a probability: a 95 or 99 percent chance, read off a model, that
every payment is met. That hands the question to the model, and the model is only as good as its guesses about the two
things nobody can pin down six years out – how shares behave in a bad decade, and where interest rates go. So we
define it as a test the portfolio passes on the day it's built. Damodaran sets two conditions for an asset to be
riskless for a given date: it can't default, and nothing in it has to be reinvested before that date. Each of Laura's
ten holdings is a Treasury, or a fund of Treasuries, that ends before its January, which settles the first condition
about as well as any investment can. The second is where the ladder has to be honest about itself. Its bonds pay
interest along the way, and two of them repay months early, so some money sits and waits. We price that wait as if it
earned nothing at all and buy the shortfall in Treasuries before Laura names her range. On the 22 October curve, that
rule met every payment in full in our base case and in a lasting two-point fall in rates; in the harshest world we
tested, with rates a point lower and her 2028 deposit halved, it met them in 98.71 percent of paths (we modelled). The
certainty comes from what she owns. The model only measures the one gap she hasn't bought yet.

## 5. The facility contribution (case: "recommend and justify the extent to which Laura can responsibly contribute")
- **Job:** how much, why that much, and why not all.
- **Spine:** the minimum is bought in Treasuries in 2028, so falling shares alone before 2031 can lower only the top
  (not "the last money she adds": the facts check found that reason doesn't follow); the residency's other money can shrink in the same recessions, so her part is most useful as the part that
  won't.
- **Evidence:** B11 (invest her part with the residency's other income in mind; Merton 1991 on endowments, Dimmock
  2012; Giving USA 2010: arts giving fell 11.9% in real terms over 2007-09; note that total giving fell far less than
  shares); B4 (diversify the residency, not just her account); B13 (why own the shares rather than a bank's
  capital-protected note: a 5-year zero at 77.4% plus an at-the-money call at about 22.9% is roughly break-even before
  fees, re-run); B17 (the strongest rival, the minimum bought only in 2031, gives about $15,000 more on average, but
  its minimum falls under $100,000 about 1 time in 13 against our 1 in 150; MODEL); B22; B21.
- **Numbers:** N4 (facility minimum, 4 Nov: p50 $145,874, p5 $128,023, cap $150,000; costs about $114k in Jan 2028);
  N8 (world shares bought Jan 2028: p50 $30,926); C7 (about 7.5% a year, J.P. Morgan, for world shares, not VT).
- **Watch:** never "a fixed $150,000 minimum"; "can shrink", never "will".

## 6. The 2031 range and our confidence (case: "recommend the dollar range … state how confident") — SAMPLE BELOW
- **Job:** the range, the confidence that the 2033 contribution lands inside it, and how good and bad markets move it.
- **Spine:** a bought deal, not best efforts: both ends are owned in Treasuries before she names it, so the
  confidence is about Treasuries paying on time, not about a forecast.
- **Evidence:** B19 (Shiller ECON 252, 2011, Lecture 19: bought deal vs best efforts); B5 (Lintner's dividend
  smoothing: a named figure is cheap to raise and costly to cut); the two questions (will it land inside? a Treasury
  question; where inside? the only forecast left; HARVEST_ROOMS_TEAM).
- **Numbers:** N5 (old design, before the naming-day lock: bottom $140,000, median top $163,000, top p5-p95
  $140k-$184k, 4 Nov, J.P. Morgan 2026 7.0%); re-run with the final IPS rules (top bought on naming day) before use.
- **Watch:** "rounded down because a fund's final payout isn't fixed"; falling shares alone lower only the top; with
  low rates the shortfall rule can lower the bottom before she names it, never after.

### Sample paragraph (§6)
When Laura meets co-sponsors in 2031 she'll give them one range, and they'll plan around it. That's the reason the
case worries about promising too much, and it's the reason we treat the range the way a careful investment bank treats
a share sale. In a bought deal the bank buys the shares itself before it sells them on; under best efforts it only
promises to try. Most ranges are best efforts – a model's low and high outcomes, said aloud and then hoped for.
Laura's is a bought deal. Its bottom is what the extra units of her late-2032 Treasury fund will pay, bought in 2028
and rounded down, because a fund's final payout isn't fixed. Its top adds half of what her shares are worth on the day
she names it, and she moves that half into Treasuries before she says a word. The fair objection is that a range with
both ends bought is just a number in disguise. It isn't quite, since the fund's payout moves a little with rates, but
the objection gets the important part right: our confidence that her 2033 contribution lands inside the range is
our confidence that US Treasuries pay on time. The forecast hasn't disappeared. It has moved to a question that
doesn't hurt anyone if we get it wrong – how high the range starts, which depends on how her shares do before 2031.

## 7. Communicating with co-sponsors, and the draft fundraising text (case: "draft part of Laura's fundraising materials")
- **Job:** the words Laura uses, the range, the confidence, and what she says when markets move.
- **Spine:** her ten operating payments are already funded before she asks anyone, so co-sponsors' money can go to the
  facility.
- **Evidence:** B1 (Gneezy, Keenan & Gneezy, *Science* 2014: a lead gift covering overhead raised total giving about
  75% more; **untested for arts residencies and Taiwan's grants pay operating costs, so frame carefully**); B19; B4.
- **Draft text:** from Writing 1.2, `cosponsor_text_draft.md` (this folder), once reviewed.
- **Watch:** Buffett plainness, every number dated; no "guaranteed".

## 8. Financial flexibility (case: "committing all remaining assets could limit her financial flexibility")
- **Job:** what she keeps, why, and what it's for.
- **Spine:** the half of her shares she keeps first covers the ladder's one weakness; whatever it isn't needed for stays
  hers, liquid and promised to no one.
- **Evidence:** B2 (soft budgets: money a project knows it can call on tends to get spent; Kornai, Maskin & Roland 2003;
  Andreoni & Payne 2011); B6 (cover order).
- **Numbers:** the kept half's size, re-run (p5 / median), from the same model run as N5.
- **Watch:** never earmark the kept half for building overruns (V57's mistake).

## 9. Assumptions: inflation, outside funding, returns (case: "the effect of inflation … outside funding")
- **Job:** state every assumption and its source.
- **Spine:** the payments are fixed in dollars, so dollar Treasuries match them; inflation hits the facility's cost,
  not the payments.
- **Evidence:** B9 ("Inflation can make $50,000 buy less. It cannot make $50,000 cost more."; TNA reflection 1 rejects
  TIPS; Wharton bans individual TIPS); B11 and B4 (outside funding can shrink in recessions; the reserve never relies
  on it, as the case requires).
- **Numbers:** C2; C7 and the J.P. Morgan 2026 7.0% used in N5 (pick one and say why); the rate-volatility assumption
  behind N3.
- **Exhibit:** an assumption register: each assumption, its source and date, and what happens if it's wrong.

## 10. Favourable and unfavourable outcomes (case: "explain how favorable and unfavorable market outcomes could affect the amount")
- **Job:** walk the plan through good and bad markets, before and after 2031.
- **Spine:** markets can change how large a range Laura names, never whether she meets a payment or a number already
  named.
- **Evidence:** B17 (the rival's bad tail); B16; B14; B21; B22.
- **Numbers:** N5 bands (re-run); N6 (re-run); N3.
- **Exhibit:** a 2x2 (shares up or down before 2031 × rates up or down) with what happens to the bottom, the top, the
  kept half and the payments in each cell.

## 11. Our competition experience (Articulation of Competition Experience)
- **Job:** teamwork, research and decision process, learning, response to challenges (Wharton's words).
- **Spine:** real, dated team events only, in Caplet's own voice; Caplet decides what goes in.
- **Candidates (real and dated):** the plan to use STRIPS, dropped after Wharton's week-2 email (6 Oct) limited
  recommendations to WInS-listed securities; the sector-count rule that turned out to be an old rule (5 Oct); the
  ladder built in eleven trades in two days (6-8 Oct); the ladder's cost crossing $300,000 by November (N2); the
  submitted TNA reflections; the IPS rewrite and its reviews.
- **Watch:** no fiction (Keel's simulated team is not a team event); AI use is cited by Caplet as they did for the TNA.

## 12. Sources and appendix
- Every source named in sections 1-10 (the IPS could cite none; the Final Report should cite all), plus the model
  method and the curve date used for every number.

---
**Bank coverage check:** B1 §7 · B2 §8 · B3 §2, §3 · B4 §5, §7, §9 · B5 §6 · B6 §3, §8 · B7 §4 · B8 §1 · B9 §9 ·
B10 §1, §4 · B11 §5, §9 · B12 §1 · B13 §5 · B14 §4, §10 · B15 §3 · B16 §4, §10 · B17 §5, §10 · B18 §3 · B19 §6, §7 ·
B20 §1 · B21 §1, §5, §10 · B22 §1, §5, §10. All 22 placed.
