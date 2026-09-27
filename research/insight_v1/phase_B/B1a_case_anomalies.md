# B1a Case Anomalies: a line-by-line interrogation of the four official documents

Agent: B1a (lens "Case Anomalies", starting angle: read the case, IPS guide, Trading Notes guide and SMApply criteria
page line by line, in order, and ask of every sentence "why is it worded this way?"). insight_v1 run, Phase B,
written 2026-09-27. AI-generated research (Claude Code) for brainstorming by Team Caplet. **Nothing here is text to
submit.** Where a hypothesis says what a sentence "should contain", that is a checklist for the students, who write
every word themselves. Securities named here are examples for specialists to check, and every one is **PENDING WInS
AVAILABILITY + POSITION-LIMIT CHECK: confirm on this year's WInS approved list/rules before trading.**

Map used: `research/insight_v1/phase_A/case_register.md` (R-ids), `fact_register.md` (F-ids), `stakeholder_map.md`
(BS/Q-A3 ids), `wins_week1_guardrails.md` (G ids). I did not re-ask anything in brief section 8. Where I touch an item
from brief section 9 (open), I say what evidence is new.

---

## 0. Summary (read this first)

29 questions, ordered by deadline: 7 for WInS trading now and the Trading Notes (Oct 23), 9 for the IPS (Nov 6), 13
for the Final Report (Dec 4). The six I think matter most, and that I expect almost every other team to miss:

1. **Laura's 2033 facility contribution is a decision she makes, not a market outcome (Q17).** The case asks how
   confident the team is that "her 2033 contribution will fall within that range" (case p.3 L117-118). Most teams will
   answer with a forecast interval for portfolio value. But she chooses the amount in 2033. If the plan pairs a bought
   floor with a rule that caps the gift at the top of the range (anything above the cap stays with her as
   flexibility), then the contribution lands in the range whenever the portfolio can afford the bottom. For a bought
   floor, that is close to certain. This removes the "two-sided range" trap (R-AN9) and links the range rule to the
   flexibility rule (Q22).
2. **The recommended "dollar range" is computed in 2026, but Laura says it in 2031 (Q18).** A fixed number worked out
   today will be out of date by 2031. The case's own timeline supports giving her a rule to apply in 2031, with today's
   projection shown as an illustration.
3. **Wharton's own example trading note explains the bond trade in the language of lowering portfolio volatility
   (Q2).** Our hedge holds longer-duration Treasuries, and their prices swing more than the example's intermediate
   fund. So our notes must explain in a sentence that price volatility is not risk to Laura's promise: the hedge moves
   with the value of the ten payments. A team that copies the example's logic undercuts its own strategy.
4. **Once the IPS is submitted, the strategy cannot be revised, so every "what if" rule has to be written in advance
   (Q8).** "Your team may not revise its investment strategy after the submission deadline" (IPS p.2 L73-74). The Final
   Report must still give recommendations "under varying investment outcomes" (IPS p.2 L75-78). Every contingent rule
   (rates fall before January 2027; a smaller or late 2028 deposit; the 2031 floor; the 2033 gift) has to be in the IPS,
   or the Final Report will look like a revision.
5. **The WInS rules point to treating WInS as a rehearsal of Laura's 2027 deposit (Q1; new evidence on an open
   item).** WInS cash was cut from $500,000 to exactly $300,000 and "The additional $150,000 ... will not be added to
   WInS" (R-W56, R-W59). The case says WInS is implementation "during the competition", which is Year 0. That
   evidence favours the literal 2027 book, which is almost all ladder. The current draft instead mirrors the
   post-2028 target (`wins_now/securities_and_allocation_v0.md`). The team has to choose and state the choice.
6. **Past cases show how this case was designed (Q28, new primary evidence).** The 2021-22 case already had ten
   annual payments (a $5,000 scholarship "for at least 10 years", with "Should she keep $50,000 in cash?"). The 2024-25
   case gave teams facility cost estimates; this year's case removes them on purpose. The "portfolio manager ... who
   makes the final investment decisions" line is left over from older cases, where it referred to the firm's own
   $100,000,000 portfolio, not the client's (Q9). VERIFIED-PRIMARY, Wharton archive pages read 2026-09-27.

---

## 1. Method

I read each document in authority order (case, IPS guide, Trading Notes guide, SMApply page) one sentence at a time.
For each sentence I asked five things: what does it allow; what does it forbid; what does it leave undefined; what
number or word is odd; and what would a careless team get wrong because of it. Then I compared the wording with three
earlier Wharton cases (2021-22, 2022-23, 2024-25), which I read on Wharton's public archive pages. The aim was to see
which sentences are new this year, and so were probably written on purpose. I checked a few instrument facts on
primary pages (TreasuryDirect, iShares) where a sentence depends on them.

Terms used below:
- **Liability-driven investing (LDI):** investing so that assets move with the value of a promised future payment.
- **Surplus:** assets minus the market value of the promise.
- **Duration:** how much a bond's price changes when interest rates move by 1%.
- **Floor:** an amount already secured by a bought bond.
- **Residual claim:** whatever is left after a prior claim has been paid.
- **Stage gate:** a checkpoint at which a project moves on only if set conditions are met.

---

## 2. The questions, with reasoning

Status labels follow brief section 3. "Hypothesis" is always my guess, never a finding.

### Tier 1: WInS trading now and the Trading Notes (Oct 23)

**Q1. Should the WInS portfolio be the literal 2027 book (almost all ladder), not the post-2028 target mix? Seeds 3 and
4; new evidence on the brief section 9 open item.**
- Anchors: R-W56, R-W59, R-C75, R-C76, R-AN14, R-AN22, X-7, F-101, F-605.
- Official words: "The WInS portfolio represents each team’s implementation of its investment strategy during the
  competition. It does not determine Laura’s actual portfolio value at the beginning of 2027." (case p.4 L129-130);
  "The $300,000 is your team’s WInS simulator balance. The additional $150,000 contribution described in the Client
  Case Study will not be added to WInS." (S-TRADE).
- Reasoning:
  - "During the competition" is Year 0 (2026).
  - The second sentence only makes sense if the designers expected some teams to treat WInS as the period just before
    Laura's 2027 deposit.
  - Last year's cash was $500,000 (R-W98). This year's was cut to exactly the Year-1 deposit.
  - Seed 3's premise ("$500k = WInS cash") no longer holds; see R-AN14. The new link is $300k = the 2027 deposit.
  - Under lock-early, the 2027 book is about $292k of ladder and about $8k of surplus (F-101, F-104). Its equity share
    is tiny.
  - The current draft instead recommends the post-2028 mirror: hedge about 66%, VT about 20% (VT is Vanguard Total
    World Stock ETF, a global equity fund), and a floor proxy.
- Hypothesis (guess):
  - The case text favours the 2027 book.
  - The criterion "uses appropriate diversification" (R-S24) and the value of showing the growth sleeve in notes pull
    the other way.
  - A defensible middle path: hold the 2027 book, and put a small, clearly labelled "surplus sleeve" (about 3% of
    $300k) in equity. Every note says which bucket the trade belongs to.
  - Either way, the IPS must say in one sentence which book WInS represents.
- Would change: a **decision** (the WInS weights now; the equity weight differs by about 15-20 points) and a sentence
  in the IPS and Final Report.

**Q2. How do our notes explain that long-duration Treasuries, whose prices swing more than the example's
intermediate fund, reduce risk to Laura's promise?**
- Anchors: R-T23, R-T24, R-T25, R-AN44, F-203, F-204, F-205.
- Official words: "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio
  volatility and begin preparing for Laura’s future operating commitment. ... This trade supports our plan to balance
  continued growth with reliable future cash flows as the residency funding date approaches." (TN p.2 L36-39).
- Reasoning:
  - The example uses two ideas:
    - "Reduce portfolio volatility": the asset-only view.
    - "As the residency funding date approaches": a glide path, the gradual shift to safer assets over time.
  - Our strategy holds long Treasuries now; the draft has TLH/TLT near 40% of WInS. TLT's 3-year standard deviation is
    13.74% (F-202), about twice IEF's 6.54% (F-201).
  - By the example's logic, that trade raises volatility. By LDI logic, it lowers surplus risk.
  - If our note copies the example's words, a judge could see a contradiction. If it explains the difference, it shows
    that we understand the promise, not just the assets.
- Hypothesis (guess): each hedge note needs one plain clause saying that the bond's value rises and falls with the
  value of the ten payments, so the gap between them stays small. Avoid "reduce volatility" as the stated purpose.
- Would change: a **sentence** in every hedge-trade WInS note written from now on (notes cannot be edited later) and
  in the Oct 23 reflections.

**Q3. Should every WInS note carry one dated, checkable data point, a link to Laura, and one named risk, going beyond
Wharton's example, which contains no number?**
- Anchors: R-T6, R-T11, R-T28, R-W82, R-AN43, G (guardrails section 0 item 6).
- Official words: "your Trading Notes should document the research, analysis, and reasoning behind your investment
  decisions" (TN p.1 L8-9); "record the reasoning, research, and intended strategic role of each decision at the time
  it is made" (S-WINS).
- Reasoning:
  - The guide asks for "research", but the example (59 words, R-T26) contains no data.
  - Notes are fixed at trade time and quoted "exactly as it appears in WInS" (TN p.2 L44).
  - A dated fact, for example "10-year Treasury 5.17% on 25 Sep" (F-001), proves the reasoning came before the
    outcome. Hindsight cannot fake that.
  - A statistics graduate client (R-C12) would value this.
- Hypothesis (guess): yes. Spec per note: action; which bucket; one dated number with its source named in words; the
  Laura goal it serves; one named risk. Aim for 60-90 words. No character limit is published (G, section a2).
- Would change: a **sentence** spec for every WInS note from day 1 (WInS-now); it feeds the TN.

**Q4. When one strategic decision takes several trades (a position limit forces a split, or two funds make up one
duration match), which trade carries the note, and should each note stand alone when quoted?**
- Anchors: R-T8, R-T27, R-T33, G (guardrails section 0 item 4), R-W66.
- Official words: "select three investment decisions that best illustrate your team’s strategic thinking" (TN p.1
  L11) versus "Select three (3) Trading Notes from trades your team executed in WInS." (TN p.2 L42).
- Reasoning:
  - The guide uses "decision" and "trade" as if they were the same thing.
  - With a possible 25% per-security position limit (UNVERIFIED for this season, G), the hedge alone needs 3 or more
    trades.
  - If the "real" decision's reasoning sits on a companion trade's note, the quoted note may look thin.
- Hypothesis (guess):
  - Write a full note on every trade.
  - On multi-trade decisions, each note names its companion trades ("one of three trades that together match...").
  - Choose the lead trade (the largest, or the first executed) as the TN candidate.
- Would change: a **decision** on how notes are written now and which trade is picked for the TN.

**Q5. Should the three TN picks between them cover the six named dimensions, and should at least one be a decision
that "tested" or "refined" the strategy rather than one that only "reflected" it? Extends seed 13.**
- Anchors: R-T3, R-T9, R-T17, R-T18, R-T20, R-C88, R-AN40.
- Official words: "including its approach to growth, risk, liquidity, funding reliability, financial flexibility, and
  future cash-flow needs" (TN p.1 L5-6); "reflected, tested, or refined the team’s developing strategy" (case p.4
  L152-153); "A decision can still demonstrate thoughtful analysis and strategic thinking even if your team later
  sells the investment or changes its approach." (TN p.1 L26-27).
- Reasoning:
  - Seed 13 asked why the notes come before the IPS. The answer the text gives: the designers want to see a strategy
    being developed.
  - The words "tested" and "refined", and the explicit protection for later sells, invite at least one note that
    shows the strategy being adjusted, for example:
    - a rebalance after a rate move;
    - a trade split forced by a rule the team discovered;
    - a sell.
  - Three "we bought X for the plan" notes read as a static list.
- Hypothesis (guess): pick one note each for the promise (funding reliability and future cash-flow needs), for growth
  and risk, and for a real refinement (liquidity or flexibility). This needs a genuine refinement trade before Oct 23.
  Never create one only for show: fabrication is banned (R-W28).
- Would change: a **decision** (which three trades; whether a planned rebalance or refinement happens before Oct 23).

**Q6. Does the WInS rule "no more than twice a security's current daily trading volume" use today's running volume,
so that an overnight order from Australia, filled at the open in a thin Treasury fund or an individual bond, could be
rejected or only partly filled?**
- Anchors: R-W62, R-W66, R-W72, R-W91, F-206.
- Official words: "Your team may trade an amount equal to no more than twice a security’s current daily trading
  volume." (S-TRADE); "Orders placed while the market is closed are filled at the security’s opening price when the
  market reopens." (S-TRADE).
- Reasoning:
  - "Current" is undefined. At the open, today's volume is close to zero.
  - The team is in Australia, so its orders mostly arrive overnight (U.S. time).
  - Defined-maturity funds are small:
    - iShares iBonds Dec 2036 (IBTR): 30-day average volume 68,915 shares at $23.63, about $1.6m a day; net assets
      $34.2m (VERIFIED-PRIMARY, ishares.com, 2026-09-27).
    - Dec 2034 (IBTP): 111,113 shares at $24.22, about $2.7m a day (VERIFIED-PRIMARY).
  - On a daily-average basis, a $30-40k order is far inside 2x. On an intraday basis at the open, it might not be.
  - Individual Treasury bonds in WInS price once a day (R-W91). How the rule applies to them is unknown.
- Hypothesis (guess): Stock-Trak probably uses the previous day's or an average volume. Test with one small order in a
  thin fund before a large one, and read Session Rules.
- Would change: a **decision** (order type, timing and sizing in WInS now; whether thin iBonds-type funds are used).

**Q7. How do we show "appropriate diversification" when about two-thirds or more of the book is Treasuries?**
- Anchors: R-S24, R-W70, R-W71, R-AN45, X-12, F-409.
- Official words: "uses appropriate diversification" (criterion 1); "diversification across asset classes, sectors,
  industries, market capitalizations, geographic regions, risk characteristics, and funding purposes. The goal is to
  build an intentional mix ... not simply to own a large number of securities." (S-TRADE).
- Reasoning:
  - A grader skimming holdings could read "concentrated in Treasuries".
  - Wharton's own page lists "funding purposes" as a kind of diversification. The hedge and the growth sleeve are
    exactly that.
  - Inside the growth sleeve, geographic breadth (for example a global fund) covers the rest.
- Hypothesis (guess): state in the IPS and Final Report that diversification is by purpose first (promise versus
  growth), then by geography and asset within the growth sleeve. Use Wharton's own term "funding purposes".
- Would change: a **sentence** in the IPS (diversification line); the growth-sleeve **decision** (global versus U.S.
  only).

### Tier 2: the IPS (Nov 6)

**Q8. Which contingent rules must be written into the IPS now, because the strategy cannot be revised after Nov 6 and
the Final Report must cover "varying investment outcomes"? Extends seed 4.**
- Anchors: R-I34, R-I35, R-I36, R-I37, R-I27, X-5, X-23, F-111, F-112, F-403.
- Official words: "Once submitted, the IPS becomes the official record of your team’s investment strategy. Your team
  may not revise its investment strategy after the submission deadline." (IPS p.2 L73-74); "present its analysis and
  recommendations ... under varying investment outcomes" (IPS p.2 L77-78); "How your strategy will guide portfolio
  construction and investment decisions as the client’s needs change" (IPS p.2 L61-62).
- Reasoning:
  - The money arrives in January 2027, after the freeze. The ladder cost more than $300k on 173 of 185 trading days in
    2026 (F-111), and P(cost > $300k on 2027-01-01) is about 24% (F-112, ASSUMPTION).
  - A rule for that case written only in the Final Report is a revision. Written in the IPS, it is the strategy being
    applied.
  - The same holds for:
    - a smaller or late 2028 deposit (F-403);
    - the 2031 floor share;
    - the 2033 gift rule;
    - rebalancing bands.
- Hypothesis (guess): the IPS needs about 4-5 one-line "if X, then Y" rules; about 120-150 of the 500 words. Priority:
  January 2027 purchase rule; 2028 shortfall rule; 2031 floor rule; 2033 contribution rule; band rule.
- Would change: a **decision** (the IPS structure and word budget) and **numbers** (rule thresholds).

**Q9. Who decides what: which decisions are automatic rules, which does the firm make, and which does Laura make?
Extends seed 2 with new primary evidence.**
- Anchors: R-C3, R-C25, R-C57, R-AN4, R-AN53, R-W19, R-W87, X-10, R-C89.
- Official words: "Your portfolio manager (your team’s teacher/advisor who makes the final investment decisions for
  your firm’s portfolio)" (case p.1 L4-5); "Laura must decide how much of the remaining portfolio she can responsibly
  contribute" (case p.3 L101-102); "This formally establishes the strategy and the team’s decision-making framework."
  (case p.4 L155-156).
- New evidence (VERIFIED-PRIMARY, read 2026-09-27):
  - The 2021-22 and 2022-23 cases say: "The members of your [analyst] team hope to one day become portfolio managers
    who make the final investment decisions for WGAM’s portfolio".
  - In those cases the firm (Wharton Global Asset Management, WGAM) "currently manages a $100,000,000 portfolio".
  - So the portfolio manager line is inherited boilerplate. "Your firm’s portfolio" originally meant the firm's own
    $100m book, not the client's strategy.
  - This year the firm name and the $100m book were dropped, which left the phrase orphaned.
- Hypothesis (guess):
  - The IPS "decision-making framework" should allocate decision rights. Laura approves the policy and makes the two
    big choices: the 2031 announcement and the 2033 gift. Pre-set rules handle rebalancing and the hedge.
  - The team (as the firm) recommends, and reports yearly.
  - Say nothing that implies the real advisor decides.
- Would change: a **sentence** (the governance clause in the IPS).

**Q10. In an IPS that bans charts, which numbers and rules must appear in words, and are small tables or informal
source mentions allowed? Extends seed 14.**
- Anchors: R-I23, R-I31, R-I45, R-I55, R-I56, R-AN37, R-AN38, F-603.
- Official words: "Graphics, charts, images, attachments, external links, footnotes, and formal citations are not
  permitted." (IPS p.3 L123); "Focus on the strategy and decision-making framework ... rather than describing
  individual investments or presenting detailed financial calculations." (IPS p.2 L51-52); "The IPS is not expected to
  include ... a final facility-contribution range" (IPS p.2 L68-69).
- Reasoning:
  - Tables are not on the banned list, but a reader may treat a table as a "graphic". That is an exclusion risk, and
    exclusion means "will not be considered for semifinal selection".
  - "Final" in "a final facility-contribution range" implies that a provisional rule is fine.
  - Professional IPSs normally carry target weights and ranges. Those are not "detailed calculations".
- Hypothesis (guess):
  - No tables.
  - Allow about 6-10 numbers in words: target bucket weights and bands; the certainty test (for example "funded ratio
    of at least 100% at market prices"); the floor share; the key dates.
  - Name data sources informally in the text (for example "at September 2026 Treasury yields"); do not cite them.
  - Count words with the same tool the team will use for the final PDF, and leave a safety margin.
- Would change: a **decision** (IPS layout) and **numbers** (which figures appear).

**Q11. Should the deliverables tie each of the case's three wordings (certainty, confidence, reliability) to one
object, and use them only that way?**
- Anchors: R-C47, R-C54, R-C69, R-C74, R-I6, R-I11, X-16, R-AN1.
- Official words:
  - "a high degree of certainty" and "a high degree of funding certainty" (case p.3 L91, L97-98): the payments.
  - "state how confident they are that her 2033 contribution will fall within that range" (p.3 L117-118): the
    facility range.
  - "Teams may reach different conclusions about ... funding confidence" (p.4 L127).
  - "funding reliability" (IPS L20, L59; TN L5; S-WINS).
- Reasoning:
  - The case uses "certainty" for the payments and "confident" for the facility range.
  - "Funding confidence" appears in the list of things teams may disagree on. So the confidence level applies to the
    facility, while the payments need high certainty.
  - Mixing the words (for example "95% confidence for the payments") signals a careless reading to a statistics
    graduate.
- Hypothesis (guess): certainty goes with the payments (bought: market-consistent, not a model percentage);
  confidence goes with the facility range (a stated probability); reliability is the portfolio property the IPS
  balances.
- Would change: **sentences** throughout the IPS and Final Report (the glossary line in the Final Report).

**Q12. The case says Laura has "financial resources outside the portfolio". Does that raise her capacity to take risk
with the surplus, and should the IPS say this portfolio is a dedicated goal portfolio, not her whole wealth?**
- Anchors: R-C33, R-C34, R-C37, R-C38, R-AN16, R-AN17, F-407, F-409.
- Official words: "Laura’s living expenses and short-term financial needs will be covered by income and financial
  resources outside the portfolio." (case p.2 L61-63).
- Reasoning:
  - "Financial resources", not only "income", means she has other assets.
  - Risk capacity (the ability to bear loss) for the surplus is therefore higher than for a whole-wealth portfolio.
  - The promise is ring-fenced by the ladder. This bears on the open sleeve-equity question (50/60/70%; F-407: median
    $205k/$207k/$209k, p5 $164k/$159k/$154k).
  - Goals-based wealth management treats each goal as its own sub-portfolio.
- Hypothesis (guess): yes. This is case evidence for the upper end of the sleeve band (60-70%) and for calling the
  portfolio "goal-dedicated" in the IPS. It does not touch the payments.
- Would change: a **number** (sleeve equity weight) and a **sentence** (risk-tolerance line: willingness from the
  "thoughtful risks" line, capacity from outside resources).

**Q13. Should the Final Report give Laura one recommendation or a small menu of options?**
- Anchors: R-C8, R-C38, R-S25, R-AN5.
- Official words: "she wants her investment team to recommend an appropriate balance" (case p.2 L71-74) versus "the
  investment strategy that Laura ultimately chooses" (p.1 L9).
- Reasoning:
  - She chooses among firms; within a firm, she asked for a recommendation.
  - A menu can look like a failure to decide. A single number with no alternatives can look rigid.
  - Professional practice (D8) often shows one recommendation plus the cost of the alternatives.
- Hypothesis (guess): one recommendation, with a single line on what she would give up or gain by choosing one step
  more cautious or one step bolder (for example sleeve equity 50% versus 70%, using F-407 numbers). That respects her
  choice without abdicating.
- Would change: a **decision** (the structure of the Final Report's recommendation section).

**Q14. What liquidity need does the case actually give Laura, and what should the IPS's "liquidity" sentence
therefore say?**
- Anchors: R-I11, R-I21, R-C31, R-C33, R-C34, R-T3.
- Official words: "How does your strategy balance growth, risk, liquidity, funding reliability, and financial
  flexibility?" (IPS p.1 L20); "she will neither add to nor withdraw from the portfolio before 2033." (case p.2
  L63-65).
- Reasoning:
  - "Liquidity" appears in every guide, yet the case gives no cash need before 2033 (living costs are outside the
    portfolio).
  - Liquidity needs are therefore dated: Jan 1 each year from 2033 to 2042, plus the facility gift in 2033.
  - That lets the plan hold bonds to maturity and avoid a cash drag, but it must be said explicitly. Otherwise a reader
    may think liquidity was ignored.
- Hypothesis (guess): one sentence stating the dated liquidity needs, and that each is met by a maturing bond, not by
  selling assets at uncertain prices.
- Would change: a **sentence** in the IPS.

**Q15. Would a former tech product manager recognise the plan as hers if it were framed as stage gates with decision
dates (2027 buy, 2028 top-up, 2031 announce, 2033 gift) and conditions for each?**
- Anchors: R-C12, R-C17, R-C18, R-C29, R-AN11.
- Official words: "before beginning her career as a product manager in the technology industry" (case p.1 L16-17);
  the timeline lists only 2026, 2027, 2028, 2031 and 2033 (p.2 L49-57).
- Reasoning:
  - The case lists only the years when a decision falls (R-AN11).
  - Product managers work with roadmaps, milestones and go/no-go gates.
  - Framing the IPS as dated gates with rules is both professional (X-23) and in her own working language. It is not
    identity decoration, because the frame comes from her stated career.
- Hypothesis (guess): yes, as the organising frame for the IPS and the Final Report timeline chart. D6 should check her
  public professional writing for how she talks about product and project planning. Do not overclaim.
- Would change: a **decision** (the organising frame of the IPS and Final Report).

**Q16. The case names no values or ESG preference this year, but every recent case had a social goal. Should our
deliverables say that Laura's impact comes through the payout (the residency), not through screening the portfolio?
Extends seed 12 with new evidence.**
- Anchors: R-AN34, R-C39, R-C40, R-W52.
- Official words: 0 hits for "ESG", "values", "impact", "sustainab" in the four documents (R-AN34, VERIFIED-REPO-FILE).
- New evidence:
  - 2021-22: a scholarship for women of colour in engineering (VERIFIED-PRIMARY).
  - 2022-23: a start-up fund and a wellness centre (VERIFIED-PRIMARY).
  - 2024-25: housing and a youth centre in Nigeria (VERIFIED-PRIMARY).
  - 2025-26: "think beyond financial returns and consider how their strategies could support long-term community
    impact" (VERIFIED-PRIMARY, finalists page).
  - This year the impact is in the goal. The investment instructions are silent on it.
- Hypothesis (guess):
  - Do not add ESG screens.
  - One line in the Final Report: the promise is secured with the plainest instruments, so that every dollar of
    impact reaches the residency.
  - Tokenism rule: never pick investments by identity.
- Would change: a **decision** (no screens) and a **sentence** (the Final Report rationale).

### Tier 3: the Final Report (Dec 4)

**Q17. Because the 2033 contribution is Laura's decision rather than a market outcome, should the confidence
statement be the probability that the portfolio can afford the bottom of the range, combined with a rule that caps
the gift at the top? Extends seed 9.**
- Anchors: R-C57, R-C67, R-C68, R-C69, R-C71, R-AN9, R-AN20, F-402.
- Official words: "state how confident they are that her 2033 contribution will fall within that range" (case p.3
  L117-118); "Laura must decide how much of the remaining portfolio she can responsibly contribute" (p.3 L101-102).
- Reasoning:
  - "Her 2033 contribution" is chosen by her in 2033.
  - Rule: contribute the floor, plus a set share of anything above it, up to the top of the range. Anything beyond the
    top stays as flexibility. Under this rule, the contribution falls within the range whenever the residual is at
    least the floor.
  - If the floor is bought in 2031, that confidence is close to certain. The upper end then becomes a stated
    aspiration with its own probability, not a risk of "missing" the range.
  - Most teams will present a portfolio-value forecast interval and report something like "90% confident", which
    mixes up a decision with a forecast.
- Hypothesis (guess):
  - Report two numbers: P(contribution ≥ floor), close to 100% once bought; and P(reaching the top of the range), from
    the model.
  - Say that the range cannot be exceeded by design.
  - D3 should compute both from strategy_mc under the rule.
- Would change: **numbers** (confidence levels) and a **sentence** (the range statement in the Final Report and the
  co-sponsor draft).

**Q18. Should the recommended "dollar range" be a fixed number computed today, or a rule Laura applies in 2031, with
today's projection shown as an illustration?**
- Anchors: R-C62, R-C63, R-C65, R-C68, R-C77, F-402.
- Official words: "Laura plans to begin approaching potential co-sponsors in 2031"; "In 2031, however, the value of
  her portfolio in 2033 remains uncertain."; "Teams must recommend the dollar range Laura should communicate" (case p.3
  L109-117).
- Reasoning:
  - The Final Report is written in 2026. The 2031 portfolio value will be known in 2031.
  - A fixed 2026 range (for example "$150-250k") will almost certainly be wrong in 2031, one way or the other.
    F-402: the floor's p5/p50/p95 are $127k/$165k/$217k.
  - The case asks for "the dollar range", so a rule alone is not enough.
- Hypothesis (guess):
  - Give the rule. For example: announce the bought floor as the bottom; the top is the floor plus a share of the
    remaining sleeve.
  - Also give the 2026-vantage illustration: the median case range, and how the range shifts in a bad or good
    2027-2031, using p5/p95 from F-402.
  - This answers "favorable and unfavorable market outcomes" (L118-119) directly.
- Would change: a **decision** (the form of the recommendation) and **numbers** (the illustrative range).

**Q19. The case says Laura will "begin" approaching co-sponsors in 2031. Should the plan schedule range updates that
narrow the range between 2031 and 2033, and when would the rest of the floor be bought? Extends seed 8.**
- Anchors: R-C62, R-AN7, F-013, F-402.
- Official words: "Laura plans to begin approaching potential co-sponsors in 2031, two years before the residency is
  established." (case p.3 L109).
- Reasoning:
  - "Begin" implies that fundraising runs from 2031 to 2033, with more conversations along the way.
  - Seed 8's point (a 2-year Treasury matches the gap) is settled in brief section 8.7.
  - New angle: a range that narrows at pre-announced dates (for example in 2032) matches how capital campaigns update
    donors. It lets more of the sleeve be locked as the date nears, and it keeps credibility because updates only move
    upward from a bought floor.
- Hypothesis (guess):
  - One pre-announced update in 2032. The floor never falls.
  - The top of the range can narrow.
  - D5 should check fundraising practice for pledge updates.
- Would change: a **decision** (the 2031-2033 rule in the IPS) and a **sentence** (the co-sponsor draft).

**Q20. With the facility cost unknown, what makes Laura's contribution "meaningful" to co-sponsors: its dollar size,
its share of her capacity, or the certainty that it will be delivered? Extends seed 6.**
- Anchors: R-C64, R-C94, R-C95, R-AN6, BS-17, Q-A3-06, Q-A3-13.
- Official words: "A meaningful personal contribution may signal that the residency is financially viable, demonstrate
  Laura’s commitment to the project, and make potential co-sponsors more willing to contribute." (case p.3 L110-112).
- Reasoning:
  - "Meaningful" is undefined. The cost is deliberately unknown (R-C94).
  - The three signals the case lists are viability, commitment and willingness. They depend on credibility and on
    "skin in the game" (a personal stake) relative to what she has, not on share of cost.
  - Seed 6 (why co-sponsors may fund the building but not operations) is partly answered by BS-17: funders avoid
    running costs.
  - New link: Laura's secured ten years of operations is itself a "meaningful" contribution, because a building with
    no operating money is a stranded asset. So the operating promise counts in the co-sponsor message, not only the
    facility gift.
- Hypothesis (guess): the co-sponsor draft should lead with total secured support: $500,000 of operating payments
  (nominal), plus the facility floor. It should state her gift as a share of her investable portfolio, never as a
  share of the (unknown) cost.
- Would change: a **sentence** (the headline of the fundraising draft) and a **decision** (whether to express the gift
  as a share of her capacity).

**Q21. Since the facility money is only what is left after the reserve, is it a residual claim? And should the Final
Report show co-sponsors that matching the reserve removes the leverage that would otherwise make the gift swing more
than the whole portfolio? Extends seed 5.**
- Anchors: R-C50, R-C57, R-AN2, R-AN26, F-401, F-106.
- Official words: "At the beginning of 2033, before making the first operating payment or contributing to the
  facility, Laura will set aside a portion of the portfolio to fund the ten payments." (case p.3 L94-95); "how much of
  the remaining portfolio" (L101).
- Reasoning:
  - Seed 5 (promise first, then the facility) is confirmed by the word order and by "remaining".
  - New angle: if the reserve is bought only in 2033 at an unknown price (about $395k on today's forwards, F-106), the
    residual is total assets minus a moving claim. A 10% move in total assets moves the residual by roughly 3 times as
    much in percentage terms.
  - Brief section 8 already gives the growth-first surplus: p5/p50/p95 $20k/$226k/$540k, versus lock-early
    $159k/$207k/$273k.
  - The co-sponsor-facing explanation of why the range is narrow is new: "the promise is already paid for, so her gift
    depends only on the growth money".
- Hypothesis (guess): one Final Report chart (the waterfall on 1 Jan 2033: reserve, then first payment, then gift,
  then flexibility) and one sentence for co-sponsors. Data: F-106 and F-401.
- Would change: a **sentence** and a Final Report **chart** specification.

**Q22. How should "financial flexibility" be expressed when teams need not size a contingency fund? Is the flexibility
simply the upside above the top of the range? Extends seed 11.**
- Anchors: R-C58, R-C61, R-C84, R-AN19, R-AN20, R-AN59.
- Official words: "She recognizes that committing all remaining assets could limit her financial flexibility as the
  project develops." (case p.3 L102-103); "Teams are not expected to determine the size or investment composition of a
  separate contingency fund or endowment." (L106-107).
- Reasoning:
  - "Not expected" is not the same as "not allowed". But a fund sized with no cost estimate would be arbitrary.
  - "The extent to which" (L104-105) permits a share or a rule as the answer.
  - With the Q17 cap rule, flexibility falls out automatically: whatever exceeds the capped gift stays with Laura for
    "as the project develops" (overruns, a slower start, needs after 2042).
  - One rule then answers two case requirements: a responsible contribution, and preserved flexibility.
- Hypothesis (guess): state flexibility as a rule (for example, "at least X% of the post-reserve surplus is never
  pledged"). Report its dollar value at p5/p50/p95. D3 should pick X from F-401 so that p5 still leaves a buffer.
- Would change: a **number** (X) and a **decision** (flexibility defined by rule, not by a separate fund).

**Q23. What would it cost to make the ten payments inflation-indexed, and should the Final Report show that the phrase
"not adjusted for inflation" is what makes the promise affordable? Extends seed 10.**
- Anchors: R-C46, R-AN3, R-AN8, F-008, F-009, F-101, F-109, F-114.
- Official words: "For purposes of the competition, each payment is a fixed $50,000 and is not adjusted for
  inflation." (case p.3 L90).
- Reasoning:
  - Brief section 8.10 settles that TIPS are not the core hedge. That is not what this question asks.
  - The qualifier "For purposes of the competition" appears three times in the case (timeline, payments, taxes). It
    marks simplifications that the designers know are unrealistic.
  - Quick arithmetic (ASSUMPTION: flat 5.359% nominal, which reproduces $292k per F-109, and 2.35% inflation, close to
    the 2.33-2.34% breakevens in F-009):
    - fixed payments cost **$292,273** at 2027-01-01;
    - payments indexed from 2033 (first payment $50k, then rising with inflation) cost **$321,971**, about **+$30k**,
      more than the $300k deposit;
    - payments indexed in 2027 dollars cost **$370,121** (+$78k);
    - the real value of the 2042 payment in 2033 dollars is $40,568.
  - So the fixed nominal design is what makes the promise fit inside the first deposit. The cost of inflation passes
    to "any operating support beyond Laura’s commitment" (L85-86).
- Hypothesis (guess):
  - One Final Report sentence and one number pair: real value falls from $50k to about $40.6k (2033 dollars) by 2042.
  - Indexing would have cost about $30k more than she has in 2027.
  - Say it plainly to co-sponsors (brief section 9 says this "must be said aloud").
  - D1 should re-price on the actual TIPS real curve (F-008) instead of the flat-rate shortcut.
- Would change: a **number** and a **sentence** (Final Report assumptions; co-sponsor draft).

**Q24. Funding after 2042 is out of scope, but a co-sponsor reading a ten-year pledge will ask about year eleven.
What should the Final Report say without solving it? Extends seed 7.**
- Anchors: R-C49, R-C41, R-AN25, R-AN59.
- Official words: "Funding the residency beyond the final payment in 2042 is outside the scope of the competition."
  (case p.3 L92-93); "reliable support for its early operations" (L83).
- Reasoning:
  - The case calls the ten years "early operations", which assumes other money comes later.
  - A matched reserve runs to exactly zero in 2042 by design.
  - Silence could read as a cliff. Solving it breaks scope.
- Hypothesis (guess): one sentence marking the boundary: the commitment is start-up support, and it ends on schedule.
  Point to the unpledged flexibility (Q22) as her optional capacity, not a promise. No numbers after 2042.
- Would change: a **sentence** (the co-sponsor draft; the Final Report scope note).

**Q25. The case fixes every payment date, yet asks teams to state assumptions about "the timing of cash flows". Which
timing assumptions does it want?**
- Anchors: R-C31, R-C32, R-C85, R-AN12, F-107, F-113.
- Official words: "All contributions and withdrawals occur at the beginning of the applicable year." (case p.2 L59);
  "Teams should identify and explain their assumptions about investment performance, the timing of cash flows, outside
  funding..." (p.4 L146-147).
- Reasoning:
  - Real Treasuries do not mature on 1 January.
  - TreasuryDirect (VERIFIED-PRIMARY, 2026-09-27): 2-, 5- and 7-year notes are issued on the last day of the month.
    10-year notes and 30-year bonds are issued on the 15th of Feb/May/Aug/Nov. Maturity equals issue date plus term,
    so matching instruments pay out on Nov 15 or Dec 31. S1 already costs the Nov-15 gap at +$2,124 (about 47 days of
    bill reinvestment).
  - iBonds funds "terminate on or about October or December 15" of their year (VERIFIED-PRIMARY, ishares.com).
  - The other timing items the case leaves open:
    - whether the 2028 deposit arrives on time (Q-A3-11 flags that it could be late);
    - whether the facility gift is one payment in 2033 or instalments during construction.
- Hypothesis (guess): list four timing assumptions in the Final Report:
  - maturities about 6 weeks before each payment, with cash held in bills;
  - the 2028 deposit on 1 Jan, plus a late-deposit stress;
  - the facility gift paid in one lump in 2033;
  - the 2031 floor note maturing 31 Dec 2032.
- Would change: a **sentence** (the assumptions list) and a **number** (the ladder cost, $294.4k versus $292.3k).

**Q26. Which market date should the Final Report's numbers be priced on: 25 Sep, 6 Nov (the freeze), or the latest
curve before 4 Dec?**
- Anchors: R-I36, R-AN36, X-6, F-001, F-002, F-111.
- Official words: "Your portfolio and Final Report should reflect the strategy established in your IPS." (IPS p.2
  L75); "Trading ends and your portfolio is locked." (SMApply).
- Reasoning:
  - The 10-year Treasury yield moved about 120bp in 2026 (F-003). The ladder cost ranged from $292k to $326k (F-111).
  - If the Final Report's numbers come from a different date than the IPS and the WInS freeze, the three deliverables
    may disagree. For example, the IPS says "fits within $300k" but the late-November curve says it doesn't. That
    breaks "a clear and consistent investment strategy across all three" (case p.4 L162).
- Hypothesis (guess): price the base case on 6 Nov (the freeze date, matching the frozen WInS book). Add one line
  showing the latest curve before submission as a sensitivity. The IPS should avoid a hard dollar claim that one rate
  move could falsify.
- Would change: **numbers** (every Final Report figure) and a **sentence** (the IPS "fits inside" wording).

**Q27. The case never says why the residency is in Taiwan. Should our deliverables refuse to supply a reason, and
guard against confusing Taiwan with her Wuhan birthplace?**
- Anchors: R-C10, R-C39, R-AN10, R-AN56.
- Official words: "Born in Wuhan, China, and raised in Texas" (case p.1 L13); "In 2033, Laura plans to establish a
  collaborative creative residency in Taiwan." (p.2 L76).
- Reasoning:
  - The case gives a place but no reason.
  - A tempting sentence (for example "returning to her roots") would:
    - invent a motive;
    - risk tokenism;
    - conflate China and Taiwan, which is factually wrong and politically sensitive.
  - Wharton says the financial scenario is invented (R-W4).
  - Public interviews mention time she spent working in Taiwan (SNIPPET-UNVERIFIED). Even if verified, it bears only on
    currency and cost context, not on motive.
- Hypothesis (guess): use no motive sentence. Treat Taiwan as a location with currency (Q-A3-04) and cost facts only
  (F-508, F-510).
- Would change: a **sentence** (deleted or never written: the client-knowledge section and the co-sponsor draft).

**Q28. What does the way cases have changed across seasons reveal about what this year's designers want rewarded?**
- Anchors: R-W52, R-AN34, R-C94, R-C95, R-C61, F-609.
- Evidence (VERIFIED-PRIMARY, Wharton archive pages, 2026-09-27, unless noted):
  - 2021-22: "provide a small scholarship of $5,000 per year ... for at least 10 years. ... Should she keep $50,000 in
    cash? Should she invest in stocks that pay dividends?"
  - 2022-23: "use the interest from that investment to sustain the fund".
  - 2024-25: "it will cost about $10,000 USD per housing unit; however, material costs and market dynamics are always
    changing" and "Operating the youth center for one year should cost at least a quarter of your original $100,000".
  - 2025-26: grow $500,000 to at least $1.5m by 2036 (SNIPPET-UNVERIFIED, Scribd summary; page blocked).
  - 2026-27: a promise with "a high degree of certainty", no cost estimate, and no contingency fund or endowment
    expected.
- Reasoning:
  - Four years ago, ten payments were a side goal. This year, the promise is the core.
  - The designers removed:
    - the cost estimates teams used to anchor on;
    - endowment-style "live off interest" framing (explicitly not expected);
    - last year's growth target.
- Hypothesis (guess): the designers want to reward:
  - a precise definition of certainty;
  - honest communication of uncertainty;
  - restraint (a responsible, not maximal, gift).

  They do not want to reward return-chasing or construction budgeting. D7 should find how 2021-22's winners funded the
  scholarship, and whether judges then preferred bonds or dividend stocks.
- Would change: a **decision** (where Final Report pages are spent: less projection theatre, more on the definition
  and communication).

**Q29. Should the fundraising draft be written as a 2031 document, using clearly labelled illustrative figures from
today's projection, or as a template with blanks?**
- Anchors: R-C72, R-AN21, R-S28, X-14.
- Official words: "Each team must also draft part of Laura’s fundraising materials describing this potential
  contribution for prospective co-sponsors." (case p.4 L123-124); criterion 5: "communicates Laura's potential
  facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors".
- Reasoning:
  - The draft is used in 2031 but written in 2026.
  - A template with blanks is safe but lifeless. A dated 2031 document with invented "actual" numbers would be
    fabrication, unless it is labelled as an illustration.
  - "Part" means the team chooses which part: probably the paragraph on her financial commitment.
- Hypothesis (guess): write it as a 2031 draft with every figure marked as an illustration from the median case, plus
  one line on how the figures will be updated. Students write it themselves (R-W26). Confirm against the Nov 9
  instructions.
- Would change: a **decision** (the draft's form) and **sentences** (the labelling line).

---

## 3. Parked (asked, but failing the "would it change anything?" test or already covered)

- Why the case says "plans to invest" for 2027 and "will contribute" for 2028. There is no strategic consequence
  beyond R-AN35.
- Headers ("Investment Competition Guide" versus "IPS"), PDF creation dates, typos on the web pages (R-AN47). These are
  editing artefacts.
- The "Wuhanese American" subtitle in the case image (R-C22). It shows her public work and has no investment
  consequence.
- The wording of the Nov-15 maturity gap. Solved by S1 (`wins_now/S1_treasury_sleeve.md`); kept only as part of Q25.
- Word counts, and whether the 100-word reflection includes the quoted note. Covered by R-T36 and the guardrails; add
  to the day-1 checklist.

---

## 4. Evidence found in this pass (with status)

| # | Fact | Source | Status |
|---|---|---|---|
| E1 | 2021-22 case: $5,000 scholarship "for at least 10 years"; "Should she keep $50,000 in cash? Should she invest in stocks that pay dividends?"; firm WGAM "currently manages a $100,000,000 portfolio"; "hope to one day become portfolio managers who make the final investment decisions for WGAM’s portfolio" | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/ (accessed 2026-09-27) | VERIFIED-PRIMARY |
| E2 | 2022-23 case: same WGAM boilerplate; "use the interest from that investment to sustain the fund"; "compete against other student teams ... trying to land the same client"; "How will you create a compelling and clever pitch to convince Peter to choose your strategy?" | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2022-2023/ (2026-09-27) | VERIFIED-PRIMARY |
| E3 | 2024-25 case: "$10,000 USD per housing unit; however, material costs and market dynamics are always changing"; youth centre operations "at least a quarter of your original $100,000 investment" | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/ (2026-09-27) | VERIFIED-PRIMARY |
| E4 | 2025-26 case: grow $500,000 into at least $1.5m by 2036 | Scribd summary via search (https://www.scribd.com/document/965855349/Case-Study-Wharton-Global-Youth-Program); page would not load | SNIPPET-UNVERIFIED |
| E5 | 2025-26 finalists page: "think beyond financial returns and consider how their strategies could support long-term community impact"; 49 semifinalists; semifinal judges include Stock-Trak's CEO, a UBS wealth-management director and a family-office COO | https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/ (2026-09-27) | VERIFIED-PRIMARY |
| E6 | Treasury issue pattern: 2-, 5-, 7-year notes issued on the last day of the month; 3-year on the 15th; 10-year notes and 30-year bonds on the 15th of Feb/May/Aug/Nov | https://www.treasurydirect.gov/auctions/general-auction-timing/ (2026-09-27) | VERIFIED-PRIMARY (maturity = issue + term is an ASSUMPTION) |
| E7 | IBTR (iBonds Dec 2036): net assets $34,216,407; close $23.63; daily volume 85,109; 30-day average 68,915; 4 holdings; funds "terminate on or about October or December 15 of the year in each Fund’s name" | https://www.ishares.com/us/products/350028/ishares-ibonds-dec-2036-term-treasury-etf (2026-09-27; data as of 2026-09-25) | VERIFIED-PRIMARY |
| E8 | IBTP (iBonds Dec 2034): net assets $316,979,783; close $24.22; daily volume 51,024; 30-day average 111,113; expense 0.07% | https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf (2026-09-27) | VERIFIED-PRIMARY |
| E9 | Cost of indexing the payments: fixed $292,273; indexed from 2033 $321,971; indexed in 2027 dollars $370,121; 2042 payment worth $40,568 in 2033 dollars | inline Python in this pass: flat 5.359% nominal (F-109), 2.35% inflation (about F-009) | ASSUMPTION (flat rates) |
| E10 | "For purposes of the competition" appears 3 times in the case (L46, L90, L168) | case `.txt` | VERIFIED-REPO-FILE |

Reproduce E9 (repo root):
`.venv/bin/python -c "r=0.05359;pi=0.0235;print(round(sum(50000/(1+r)**(6+k) for k in range(10))),round(sum(50000*(1+pi)**k/(1+r)**(6+k) for k in range(10))),round(sum(50000*(1+pi)**(6+k)/(1+r)**(6+k) for k in range(10))))"`

---

## 5. Leads for the specialists

- **D1 (rates):**
  - Re-price Q23 on the real TIPS curve (F-008, Treasury real-yield CSV) instead of the flat shortcut.
  - For Q26, compute the ladder cost on the 6 Nov curve as soon as it is published (same Treasury CSV, F-001).
  - For Q2, give the correlation between a duration-matched hedge and the liability value versus a cash benchmark, as
    one number a note can quote.
- **D3 (quant):**
  - Q17/Q18/Q22: add a contribution rule to `strategy_mc.py`: gift = min(top, floor + s × (residual − floor)); the
    remainder is flexibility.
  - Report P(gift ≥ floor), P(gift = top), and flexibility at p5/p50/p95 for s = 0.5/0.7/1.0.
  - Q21: show the residual's percentage volatility under growth-first versus lock-early.
- **D4 (Taiwan/FX):**
  - Q27: confine Taiwan to currency and cost facts (F-508, F-510, F-514).
  - Check her public professional pages only for any stated reason for Taiwan, and record none unless it is a
    professional statement she made publicly.
- **D5 (philanthropy):**
  - Q19: find how capital campaigns update donors on pledges between announcement and payment.
  - Q20: find what "lead gift" or "meaningful founder commitment" means in capacity terms. Sources to try: CCS
    Fundraising and the Giving USA public summaries (not yet checked).
- **D6 (client psychology):**
  - Q15: find her own public words on product management, planning and milestones (lauragao.com, reachable).
  - Q12: goals-based wealth management literature (Chhabra's "wealth allocation framework"; Das, Markowitz et al.
    2010 on mental accounting) for "dedicated goal portfolio" language.
- **D7 (Wharton intent):**
  - Q28: the 2021-22 winners' approach to the ten scholarship payments (archive page; news items from 2022).
  - Retry the 2025-26 case on an accessible mirror.
  - Note that the 2023-24 and 2025-26 archive URLs return 404 in the `previous-winners/case-study-for-YYYY-YYYY/`
    pattern.
- **D8 (professional practice):**
  - Q10/Q13: CFA Institute IPS elements (a sample IPS with target weights and ranges).
  - Private-bank practice of one recommendation plus alternatives.
- **D9 (plain English):**
  - Q11: a three-word glossary (certainty, confidence, reliability).
  - Q2: a one-clause explanation of surplus risk that a 16-year-old can say aloud.
- **D10 (compliance):**
  - Q6: read the Session Rules tooltip for the volume rule; test one small overnight order in a thin fund.
  - Q4: note-writing protocol for split trades.
  - Q10: the tables question. If in doubt, no tables.

---

## 6. Sources (all accessed 2026-09-27)

- Official repo files (VERIFIED-REPO-FILE): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`,
  `2026_WGY_Investment_Policy-FINAL.txt`, `2026_WGY_Trading_Notes_Analysis-FINAL.txt`,
  `SMApply_Deliverables_Page_2026-09-27.md`.
- Phase A files: `research/insight_v1/phase_A/case_register.md`, `fact_register.md`, `stakeholder_map.md`,
  `wins_week1_guardrails.md`. Also `research/insight_v1/wins_now/securities_and_allocation_v0.md` and
  `S1_treasury_sleeve.md`.
- Wharton archive pages (VERIFIED-PRIMARY):
  - https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/
  - https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2022-2023/
  - https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/
  - https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/
  - https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/
- TreasuryDirect (VERIFIED-PRIMARY): https://www.treasurydirect.gov/auctions/general-auction-timing/
- iShares (VERIFIED-PRIMARY): https://www.ishares.com/us/products/350028/ishares-ibonds-dec-2036-term-treasury-etf ;
  https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf
- Blocked or not loaded: Scribd 2025-26 case (the page script would not load, so only the snippet is used).
- Search-only leads (SNIPPET-UNVERIFIED): interview snippets about Laura's time in Taiwan (for example
  themaverickshow.com podcast 190). Not used as fact. No personal details recorded.

---

## What this teaches

- **Read an official document like a contract, then like a designer.** The contract reading finds the rules
  ("must", "may not"). The designer reading asks why this sentence is here this year. Comparing with older cases
  showed which lines are inherited boilerplate (the portfolio manager "who makes the final investment decisions") and
  which were deliberately added or removed (no cost estimate, no endowment, "a high degree of certainty").
- **Watch for words that hide a decision.** "Her 2033 contribution" sounds like a forecast, but it is a choice Laura
  makes. When the thing being forecast is partly under the client's control, a rule can turn a risky forecast into a
  near-certain promise.
- **Timing words matter.** "During the competition", "begin approaching in 2031", "may not revise after the submission
  deadline": each one tells you when a decision happens, and so where in the three deliverables it has to be written.
- **An official example is a sample, not a template.** Wharton's example note is well built, but it rests on an
  asset-only view of risk. Copying it would contradict a strategy built around Laura's promise.
