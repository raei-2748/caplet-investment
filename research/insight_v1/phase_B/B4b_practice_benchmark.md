# B4b Top-Practitioner Benchmark: questions from private wealth practice

Agent: B4b, insight_v1 run, Phase B (question generation). Written 2026-09-27. Lens: "Top-Practitioner Benchmark".
Starting angle: private wealth practice (goals-based wealth management, the wealth allocation framework, private-bank
coaching, probability-of-goal reporting, IPS governance). The other B4 agent starts from institutions; I touch
pensions only where private-wealth evidence pointed there.

This is AI-generated research (Claude Code) for brainstorming. It holds **no submission-ready prose**. Where a
question says "a sentence must contain", that is a checklist item; the six students write every word. Any practitioner
source named here must be cited in the Final Report's Works Cited, together with how AI was used (R-W46).

---

## 0. Summary (read this first)

1. **Our architecture is what top practice now recommends, and there is a fresh 2026 source that says so.** Russell
   Investments (13 July 2026) describes a "surplus glidepath": "lock down the benefits promised, then grow surplus
   assets with a prudent process". It adds that "any surplus strategy should preserve benefit security first, with
   additional risk taken only on assets above a defined surplus threshold" (VERIFIED-PRIMARY). That is lock-early plus
   a growth sleeve in a pension professional's words. The team can cite a named 2026 practitioner rather than
   asserting "this is what professionals do".
2. **The best-known critique of full hedging does not apply to Laura, and saying so is a rare, strong move.** J.P.
   Morgan Asset Management (Oct 2021) argues against pension "hibernation" (full hedging). Its reasons are credit
   downgrades of corporate bonds (about 50bp a year), rising longevity and "experience losses" (VERIFIED-PRIMARY). None
   of these exists for ten fixed nominal payments matched with U.S. Treasuries on known dates. Laura's promise is the
   textbook case where full hedging works as designed (Q07).
3. **The team's own notes mislabel Chhabra's wealth allocation framework.** They put the "aspirational" bucket on the
   flexibility money. In Chhabra's framework the aspirational bucket holds concentrated, high-risk bets such as
   "owning a small business, or leveraging unique human capital" (SNIPPET-UNVERIFIED). Laura's own creative business
   is her aspirational bucket, and so is the residency itself. A judge who knows the framework would spot the misread.
   The corrected mapping is also a Laura-specific reason for the portfolio's moderate risk (Q04).
4. **Brunel's goal-probability table gives a practitioner scale for "certainty" and for the 2031 confidence.**
   "Needs" sit at 90-95%, "wants" at 80-85%, "wishes" at 65-75% and "dreams" at 50-60% (Das et al. 2018,
   VERIFIED-PRIMARY). Our payments sit above even the "needs" level, because they are bought, not forecast. With a
   bought floor, the only way to land outside the co-sponsor range is to land *above* it. Our confidence figure
   therefore equals the percentile we choose for the top of the range, so a "wants"-level 80-85% gives a
   principled top end (Q09, Q15).
5. **The CFA Institute's own IPS standard supplies the governance and rebalancing items the case never states.** The
   case names no rebalancing rule, review cycle or risk metric (R-AN17, R-AN34). The CFA document says "If the policy
   is not to rebalance, this policy should be documented in the IPS". It also warns against "different metrics to
   highlight or disguise certain risks" (VERIFIED-PRIMARY). Both fit in one clause each of the 500 words (Q01, Q12,
   Q18).
6. **WInS now: a pre-written rebalancing band turns market noise into a "tested" trading note.** The Trading Notes guide
   asks how decisions "supported, tested, or refined" the strategy (R-T20). If the team writes a band rule before the
   first trade, any market move during the WInS window produces a rule-driven trade. That trade is concrete evidence
   of discipline, and few teams will have one (Q01).
7. **Two behavioural facts need care with a statistics-trained client.** Vanguard values "behavioural coaching" at
   about 150bp a year (VERIFIED-PRIMARY). Morningstar measures a 1.2 percentage-point "investor return gap"
   (VERIFIED-PRIMARY). But a 2026 *Financial Analysts Journal* paper finds that poor timing costs "only 0.10% per
   year" on the same sample (VERIFIED-PRIMARY abstract). Quoting the big numbers as fact would be the kind of
   unexamined statistic Laura would reject. The case for pre-commitment rules should rest on her own decision dates
   instead (Q19).

**Question count: 25** (Q01-Q25). By deadline: WInS-now/TN 4, IPS 10, FR 11. By domain: D8 11, D3 3, D1 3, D6 3,
D9 2, D10 2, D7 1.

---

## 1. How to read this file

- **Anchors**: R-ids from `phase_A/case_register.md`, F-ids from `phase_A/fact_register.md`, BS/SH ids from
  `phase_A/stakeholder_map.md`, G ids from `phase_A/wins_week1_guardrails.md`.
- **Status labels** (brief section 3): VERIFIED-PRIMARY (VP), VERIFIED-REPO-FILE (VRF), SNIPPET-UNVERIFIED (SNIP),
  ASSUMPTION (ASM), PARAPHRASE-UNVERIFIED (PARA). Every "hypothesis" below is **a guess**, labelled as such.
- **Seeds** (v4 Part 6) for this lens: 22, 26, 27, 28. Where a question extends another seed, that seed is named.
- **Not re-asked** (brief section 8): lock-early vs growth-first, tiering, surplus-based risk, curve pricing, "equity
  buys range", model-free certainty, bought floor, which number is the reserve, TIPS, STRIPS. Q07, Q08, Q09 and Q10
  touch the lock decision only through **new external evidence**, and each says what is new.

**Terms used below**
- **Goals-based wealth management (GBWM)**: splitting a client's money into separate sub-portfolios, one per goal,
  each with its own time horizon and required chance of success. "Risk" becomes the chance of missing a goal.
- **Wealth allocation framework (WAF)**: Ashvin Chhabra's version (2005). It has three "buckets": personal/safety
  (protect from disaster), market (diversified market risk) and aspirational (concentrated bets for a big upside).
- **Liability-driven investing (LDI)**: investing so that assets move like a known future obligation.
  **Hibernation**: an LDI end-state where a fully funded pension hedges its obligations completely.
- **Funded ratio**: assets divided by the market price of the promised payments (F-117: 1.026).
- **Surplus**: assets above the price of the promise.
- **Rebalancing band**: a pre-set range around a target weight. A trade happens only when the weight leaves the band.
- **Capacity for loss**: the UK regulator's term for how big a fall in value a client can absorb without harming
  their standard of living. **Risk tolerance / attitude to risk** is how much risk the client is *willing* to take.
- **AUM fee**: a yearly fee charged as a percentage of assets under management.
- **Trigger event**: a named event that forces a review of the plan.

---

## 2. The questions

Each entry gives: the question; anchors; the exact official words or fact; the hypothesis (a guess) and evidence;
what would change; deliverables; domain; seed; and the North Star link.

### A. WInS now and the Trading Notes (tier 1)

**Q01. Should the team write a rebalancing band for the WInS book before the first trade, so that a market move
produces a rule-driven trade whose note shows the strategy being "tested"?**
- Anchors: R-T20, R-I3, R-AN17, R-W73, G (day-trading ban, guardrails section 0 item 5).
- Official words: "Your reflections should clearly explain how each decision supported, tested, or refined your
  overall investment strategy." (TN p.1 L29-30, VRF). "It helps investors stay focused on long-term objectives and
  make disciplined decisions during changing market conditions." (IPS p.1 L4-5, VRF).
- Hypothesis (guess):
  - Yes. A simple band would do: equity share of the book outside target ±5 percentage points, checked once a week,
    trades never on the same U.S. day as a buy of that fund. It costs nothing to write and creates a
    note-worthy trade whenever markets move.
  - CFA Institute: "Outside boundaries of acceptable variations from targets ... should be documented in the IPS ...
    If the policy is not to rebalance, this policy should be documented in the IPS." (VP, CFA Institute,
    *Elements of an IPS for Individual Investors*, May 2010, section 4c).
  - Vanguard's rebalancing research: annual or semiannual monitoring with thresholds of "5% or so" is enough for most
    portfolios (SNIP, search summary of *Best practices for portfolio rebalancing*; PDF not opened).
  - The 10Y moved 38bp in September alone (F-003). A ±5-point band on a 35% equity sleeve can plausibly be hit in a
    six-week window, but that is not certain (ASM).
- Would change: **decision**. WInS-now: write the band into the team's decision log before the first order; the first
  band-triggered trade becomes a Trading Note candidate ("tested"). IPS: one clause on the rebalancing rule.
- Deliverables: WInS-now, TN, IPS. Domain: D8. Seed: 27.
- North Star: Laura sees a firm that already behaves by rules in week 1, not one that writes rules after the fact.

**Q02. When the market falls during WInS or in a future bear market, which of the four standard "get back on track"
levers is Laura allowed to use? Should the IPS pre-commit never to use the "add more equity to catch up" lever?**
- Anchors: R-C34, R-C38, R-C70, R-I3.
- Official words: "Apart from the two contributions described above, she will neither add to nor withdraw from the
  portfolio before 2033." (case p.2 L63-65, VRF).
- Hypothesis (guess):
  - Morgan Stanley lists four levers: "stretching your time horizon, scaling back the goal, increasing your equity
    investment, or saving more" (VP, morganstanley.com, "Goals-Based Planning: Stay on Track", read 2026-09-27).
  - For Laura, "save more" is closed by the case (no other contributions), and "stretch the horizon" is closed because
    the dates are fixed (2031, 2033). Of the two levers left, "scale back the goal" means the facility contribution,
    which is the case's designed shock absorber (R-AN6, R-AN20). "Increase equity" would be doubling down.
  - Pre-committing against it in the IPS is a clear, Laura-specific rule. WInS-now: after a WInS loss, do not add
    equity outside the band (Q01).
- Would change: **sentence**. One IPS clause: the facility contribution is the only variable that absorbs bad
  markets; the risk level is never raised to recover losses. Possible TN reflection content if a down week occurs.
- Deliverables: WInS-now, TN, IPS. Domain: D6. Seed: 27.
- North Star: it tells Laura in advance exactly what gives way in a bad market (her facility number, never her
  promise), which is the answer a founder most needs before she speaks to co-sponsors.

**Q03. Should every WInS trade note name the goal ("funding purpose") the trade serves, as goals-based practitioners
label each sub-portfolio, so that the three chosen notes read as one goals-based portfolio?**
- Anchors: R-W71, R-AN45, R-W80, R-T10.
- Official words: "Your team may consider diversification across asset classes, sectors, industries, market
  capitalizations, geographic regions, risk characteristics, and funding purposes." (SMApply Trading Details, VP via
  A1). "Each investment decision should have a clear purpose within that strategy." (R-W80, VP).
- Hypothesis (guess):
  - Yes. Wharton's own list includes "funding purposes", the core idea of goals-based practice.
  - Brunel builds "module-built portfolios, each of which is driven by a client's expressed goals" (VP, Brunel,
    "Goals-Based Wealth Management in Practice", CFA Institute Conference Proceedings, March 2012).
  - So a label on every note (promise / 2031 floor / growth) doubles as evidence of "appropriate diversification"
    (R-S24). Notes cannot be edited later (G, guardrails item 6), so the label vocabulary must be fixed before the
    first trade.
  - What is new versus the council's "say which bucket": Wharton's own wording makes goal-labelled diversification an
    official, scored idea, not only a style choice.
- Would change: **decision**: a fixed three-label vocabulary for all notes from trade 1.
- Deliverables: WInS-now, TN. Domain: D8. Seed: 28.
- North Star: every trade visibly answers "which of Laura's goals does this serve?", which is what a client chooses a
  firm for.

**Q04. Is the team's Chhabra mapping wrong? Should Laura's career (and the residency itself) be named as her
"aspirational" bucket, so the portfolio holds only the "safety" and "market" buckets?**
- Anchors: R-C37, R-AN16, R-C33, R-C27, R-C18.
- Official words: "Although she has been willing to take thoughtful risks throughout her entrepreneurial career, she
  wants her investment team to recommend an appropriate balance between pursuing growth and protecting the capital
  required for her goals." (case p.2 L69-74, VRF).
- Hypothesis (guess):
  - Yes, the mapping is wrong. The team notes (`research/council_2026-09-27/team_notes_2026-09-27.md` L15-18) map
    "Aspirational risk bucket = flexibility reserve (stays invested for growth; dry powder)".
  - In Chhabra's framework, aspirational investments include "holding concentrated stock positions ... owning a small
    business, or leveraging unique human capital" (SNIP, search summary of Chhabra's framework; SSRN and the journal
    page were blocked or rate-limited).
  - Chhabra (quoted by CFA Institute, 5 Aug 2015): "For those things you must do, the emphasis is going to be on
    lowering the risk of your not achieving these goals ... The goals you aspire to may require a somewhat higher level
    of risk." (VP, CFA Institute Enterprising Investor blog). The same blog notes his emphasis on "human alpha: your
    earning potential and expertise in your work" (VP).
  - Read that way, the case's "Although" says her aspirational risk already lives in her career and her residency, so
    the portfolio is the safety and market buckets. That is a Laura-specific, framework-backed reason for a moderate
    sleeve and no thematic bets.
- Would change: **sentence**. IPS risk-tolerance clause: why a risk-taking founder gets a moderate portfolio. The FR
  framework section: correct the bucket names. The team's notes need correcting before any deliverable uses them.
- Deliverables: IPS, FR. Domain: D8. Seed: 28.
- North Star: it shows we understood *why* a bold entrepreneur wants a careful portfolio, in a framework she may
  already know from Wharton.

### B. The IPS (tier 2)

**Q05. Using the UK regulator's split between willingness and capacity, is Laura's capacity for loss on the growth
sleeve actually *high*? If so, is ~60% sleeve equity too low, or does the credibility risk of 2031 cap it?**
- Anchors: R-C33, R-C38, R-AN17, X-11, F-407, F-409, BS-03.
- Official words: "Laura's living expenses and short-term financial needs will be covered by income and financial
  resources outside the portfolio." (case p.2 L61-63, VRF).
- Hypothesis (guess):
  - FCA/FSA guidance FG11/05 (VP, fca.org.uk PDF): "By 'capacity for loss' we refer to the customer's ability to
    absorb falls in the value of their investment. If any loss of capital would have a materially detrimental effect
    on their standard of living, this should be taken into account".
  - Laura's living standard is outside the portfolio by case design. So on the FCA definition her capacity for loss
    on the *sleeve* is high. The team's client profile (not in repo) rates capacity "moderate to low", citing career
    risk. The two views conflict.
  - Guess at the resolution: capacity is high for money that has no promise attached. It is limited only by the 2031
    credibility statement (BS-03). So the sleeve's equity weight is set by her willingness ("thoughtful" risk) and by
    the 2031 rule, not by capacity. This would support 60% and argue against going below 50%.
- Would change: **number** (sleeve equity 50/60/70%, an open item in brief section 9) and the IPS risk sentence
  (separate willingness from capacity explicitly).
- Deliverables: IPS, FR. Domain: D6. Seed: 28.
- North Star: separating "can afford" from "wants" is exactly what a client who hires a professional expects; most
  teams will write only "moderate risk tolerance".

**Q06. Does the 2026 pension "surplus glidepath" benchmark support our ~20% total equity after 2028, or does it
imply the surplus (funded ratio ~1.5) could carry more return-seeking assets?**
- Anchors: F-409, F-117, F-106, R-C38, R-C58.
- Fact: total equity after 2028 is 17.0/20.4/23.8% for sleeve equity 50/60/70% (F-409, ASM-based).
- Hypothesis (guess):
  - Russell Investments, 2026-07-13 (VP): at 110% funded, if surplus has no value, "the optimal portfolio would be a
    20/80 ... or 30/70". Once a "meaningful surplus cushion" exists, return-seeking exposure "begins to rise
    modestly". Any increase should come "only after the plan has reached a clearly defined surplus threshold, and it
    should be implemented incrementally".
  - Laura's surplus has full value to her (it is the facility money). DERIVED (ASM inputs as in F-409): after the 2028
    deposit, assets ≈ $306.1k ladder + ≈ $158.1k sleeve ≈ $464k against a $306.1k promise, a funded ratio ≈ 1.52.
  - A pension at that level would, per Russell, run *at least* 20-30% return-seeking. So our ~20% is at the careful
    edge of practice, not beyond it.
  - Counter-weight: the sleeve's horizon is 5 years and it carries a public 2031 statement. A pension surplus has no
    announcement date. Net guess: 60% sleeve equity is defensible. The benchmark gives the team the language: "a
    defined surplus threshold, incremental risk".
- Would change: **number** (sleeve equity, possibly 60% → 65-70% if the team weighs the benchmark heavily) and an FR
  sentence that cites the practice.
- Deliverables: IPS, FR. Domain: D8 (with D3 to rerun F-407 if the weight changes). Seed: 26.
- North Star: "we did what the best pension professionals now do, adapted to your 2031 promise" is a credible reason
  to choose us over a generic 60/40 team.

**Q07. The best-known professional critique of full hedging ("hibernation") lists three structural leaks. Do any of
them apply to Laura's ten payments? If none do, should the FR say so?**
- Anchors: R-C46, R-C47, F-101, F-117.
- Official words: "each payment is a fixed $50,000 and is not adjusted for inflation." (case p.3 L90, VRF).
- Hypothesis (guess):
  - J.P. Morgan AM, "Rethinking the pension plan endgame", October 2021 (VP): hedging portfolios suffer from
    "Downgrades and defaults ... we estimate this headwind has cost approximately 50 basis points (bps) of return per
    year", "Longevity extension", and "Experience losses".
  - Laura's liability has no lives (no longevity), no benefit formula (no experience losses) and is matched with
    Treasuries (no corporate downgrades). So none of the three applies. Her case is the rare one where "a fixed income
    strategy structured to precisely match liabilities" does not leak.
  - New versus brief section 8.1: 8.1 compared lock-early with *our own* alternatives. This is the strongest *outside
    professional* objection, and it fails here for stated reasons.
- Would change: **sentence**. FR: one sentence pre-empting "professionals say full hedging is inefficient", with the
  three reasons it does not bite. IPS: none (too technical).
- Deliverables: FR. Domain: D8 (D1 to check the three reasons). Seed: 26.
- North Star: judges reward teams that answer the best counter-argument; this shows we know the professional debate,
  not just one side.

**Q08. Brunel, a leading goals-based practitioner, raises the return assumption (takes more risk) for needs 6-15
years away. Why is it right for us not to do the same for the 2037-42 payments, and what sentence says why?**
- Anchors: R-C46, R-C47, R-C48, F-107, F-108.
- Official words: "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this
  requirement." (case p.3 L91-92, VRF).
- Hypothesis (guess):
  - Brunel (VP, CFA Conference Proceedings, March 2012): for lifestyle needs in years 1-5 "we build a portfolio
    composed principally of fixed-income securities". For years 6-15 "we will raise the return assumption to 6
    percent because we can take a little more risk".
  - This is a named top practitioner doing roughly what brief section 8.2 rejected (keeping later needs in riskier
    assets). A judge who knows goals-based practice may ask.
  - Guess at the answer: Brunel's family can cut lifestyle spending and refill from other assets. Laura's payments are
    fixed, cannot draw on outside funding and are the certainty test. Brunel's own warning fits: "a random fluctuation
    in asset values can be turned into a permanent loss of capital" when a spending portfolio must be refilled after
    a fall (VP, same source).
  - New evidence: a practitioner benchmark, not a new calculation. The $20k/$43k re-pricing costs (F-108) stand.
- Would change: **sentence** (FR, where the lock is justified against goals-based practice).
- Deliverables: FR. Domain: D8. Seed: 26.
- North Star: it proves the plan is tailored (fixed, non-negotiable payments) rather than copied from a standard
  goals-based template.

**Q09. Top goals-based practice treats "needs" as 90-95% goals. We fund the payments at "bought, barring U.S.
default". How do we explain that choice as a *client* decision with a *price*, not as a model result?**
- Anchors: R-C47, R-C54, R-C55, R-AN1, F-401, F-117.
- Official words: "They should also define what they consider a high degree of funding certainty, explain how they
  evaluated that level of certainty" (case p.3 L97-98, VRF).
- Hypothesis (guess):
  - Brunel's goal-probability table (VP, Das, Ostrov, Radhakrishnan & Srivastav, *Journal of Investment Management*
    2018, Table 1): Needs/Nightmares 90-95; Wants/Fears 80-85; Wishes/Worries 65-75; Dreams/Concerns 50-60.
  - Our certainty sits above the top of that scale. Its price is visible in the verified model: growth-first median
    surplus $226k vs lock-early $207k, i.e. about $19k of median facility money to go from a ~96.8% model pass rate to
    "bought" (F-401). What it protects: p5 surplus $159k vs $20k.
  - New versus section 8.6: 8.6 defines certainty. This question places it on a practitioner scale and names its
    price in the client's own terms. That is what a goals-based adviser would show her.
- Would change: **sentence**. IPS: the certainty definition gains a phrase showing it is her "needs" goal. FR: one
  line with the ~$19k median price and the p5 protection.
- Deliverables: IPS, FR. Domain: D8 (D3 for the numbers). Seed: 22, 26.
- North Star: a statistics graduate sees a certainty level chosen on purpose and priced, not a "95%" pulled from
  software.

**Q10. What does insisting on U.S. Treasuries (rather than high-grade corporate bonds, which many liability hedgers
use) cost Laura, and does the saving survive expected downgrade losses?**
- Anchors: R-C47, F-101, F-102, F-313.
- Fact: ICE BofA U.S. Corporate index option-adjusted spread 0.79%; AA sub-index 0.58% (FRED BAMLC0A0CM,
  BAMLC0A2CAA, 2026-09-24, VP).
- Hypothesis (guess):
  - DERIVED (ASM: a flat spread added to the Treasury curve, interpolating F-102): a ladder yielding 58-79bp more
    would cost about $16k-22k less than $292,264.
  - J.P. Morgan's downgrade-and-default drag of "approximately 50 basis points (bps) of return per year" for
    high-grade hedge portfolios (VP, Oct 2021) would eat most of that. The expected saving is maybe $2-8k (ASM), and it
    adds real default risk to the one goal that must not fail.
  - So "Treasuries only" is a deliberate choice costing little in expectation. The FR can state it with a number.
    WInS permits corporate bond ETFs but only government bonds as individual bonds (R-W68, R-W69).
- Would change: **sentence** (FR: "why Treasuries" with its price) and confirms a **decision** (no corporates in the
  reserve).
- Deliverables: FR. Domain: D1. Seed: 22.
- North Star: showing the price of each safety choice is how a professional earns trust; almost no team will quantify
  what "safe" costs.

**Q11. After Moody's downgraded the U.S. to Aa1 in May 2025, all three major agencies rate the U.S. below AAA. How do
top practitioners word "risk-free" today, and what honest sentence should replace "certain barring U.S. default"?**
- Anchors: R-C47, R-C54, R-AN32, BS-18, brief section 7 wording.
- Fact: Moody's downgraded the United States to Aa1 from Aaa on 2025-05-16 (SNIP; moodys.com press release not opened).
  The S&P (2011) and Fitch (2023) downgrades are background knowledge, UNVERIFIED in this run.
- Hypothesis (guess):
  - Practitioners still use Treasuries as the liability-hedge and "risk-free" benchmark. Their wording shifts to
    "backed by the U.S. government, the highest-quality and most liquid asset available in U.S. dollars", with default
    named as a remote residual rather than denied.
  - Honest version for Laura: certain in nominal U.S. dollars, with the remaining risks named (U.S. default, the
    operational errors in BS-18, and loss of buying power to inflation). Each risk is one clause.
- Would change: **sentence** (the certainty definition in IPS and FR).
- Deliverables: IPS, FR. Domain: D1 (D10 for wording). Seed: 22.
- North Star: honest uncertainty language is the case's core skill (credibility with co-sponsors) and what a
  statistician trusts.

**Q12. What governance section would a CFA-standard IPS contain here? Specifically: who decides, how often the IPS is
reviewed, and which trigger events force a review (2028 deposit late or smaller; rates fall before purchase;
residency delayed; the 2031 announcement)?**
- Anchors: R-C3, R-C89, R-I27, R-AN4, R-W19, BS-08, BS-13.
- Official words: "Investment Policy Statement. This formally establishes the strategy and the team's decision-making
  framework." (case p.4 L155-156, VRF).
- Hypothesis (guess):
  - The CFA standard's section 2 covers "who is responsible for determining investment policy, executing investment
    policy, and monitoring the results", and "the process for reviewing and updating the IPS". Its example is to
    review "no less frequently than annually" (VP, CFA 2010).
  - One IPS sentence can carry four things: the firm recommends and the PM approves (case fiction, consistent with the
    real rules because the students write it); an annual review; three to four named triggers; and each rule written
    so any PM could apply it (BS-08).
  - The case's "decision-making framework" wording invites exactly this, and few teams will name triggers.
- Would change: **sentence** (IPS governance clause) and a **decision**: which triggers to name.
- Deliverables: IPS, FR. Domain: D10 (with D8). Seed: 2 (case design), 27.
- North Star: Laura is choosing a firm to trust for 16 years; a named review process is what she would be signing.

**Q13. Which fee assumption would a real adviser disclose for a $450k client, and must the IPS say that fees come out
of the growth sleeve so the locked payments are never touched?**
- Anchors: R-C26, BS-01, Q-A3-01, F-401.
- Official words: "At the beginning of 2027, Laura plans to invest $300,000 with an asset management firm." (case
  p.2 L43, VRF).
- Hypothesis (guess):
  - The median human-adviser AUM fee is around 1.0% at $500k-$1M (SNIP: search summary citing Kitces Research and
    Cerulli). Private banks such as J.P. Morgan Private Bank and Goldman Sachs Private Wealth generally require about
    $10 million (SNIP). So Laura is a wealth-management client, not a private-bank client. The realistic benchmark is
    a fee-only adviser or an asset manager's managed account.
  - A3 estimated that a 0.5% or 1.0% fee lowers the median 2033 surplus by about $17k or $34k (ASM).
  - Practitioner logic suggests a split: a held-to-maturity Treasury ladder needs little management, so a full AUM fee
    on it would be hard to justify (ASM/judgement).
  - The IPS must say fees are paid from the surplus. If they came from the ladder, the lock would break.
- Would change: **number** (fee line in FR projections and the 2031 range) and an IPS **sentence** ("costs are paid
  from the growth money; the reserve is never sold to pay fees").
- Deliverables: IPS, FR. Domain: D8 (D3 to model). Seed: null.
- North Star: the CFA Asset Manager Code requires fee disclosure (BS-02). A firm that shows its own cost is the one
  she can trust.

**Q14. If rates fall before January 2027 so the ladder costs more than $300k, what do professional hedgers
actually do: hedge in full when affordable, buy in stages, or wait for yield triggers?**
- Anchors: F-104, F-111, F-112, R-C26, brief section 9 (open rule).
- Fact: the ladder cost more than $300k on 173 of 185 trading days of 2026, and fits only since 2026-09-10 (F-111).
  P(cost > $300k on 2027-01-01) ≈ 24% (F-112, ASM).
- Hypothesis (guess):
  - Pension practice uses funded-status and yield triggers to raise the hedge ratio step by step (SNIP: Russell and
    Milliman search results).
  - Russell 2026 (VP) stresses a "clearly defined" threshold, implemented "incrementally".
  - For Laura the professional default would be: hedge the longest rungs first up to the $300k available, buy the rest
    from the 2028 deposit, and never wait for a better yield (waiting is a rate bet). This matches the current
    longest-first rule (S-31). The benchmark adds a named, practitioner-style rule format: trigger, action, record.
- Would change: **decision** (confirm or replace the "rates fall first" rule) and an IPS clause.
- Deliverables: IPS. Domain: D1 (with D8). Seed: 4 (case design), 26.
- North Star: a pre-written rule for the one market move that could break the plan before it starts shows foresight
  most teams lack.

**Q15. Should the IPS state the risk tolerance the way the CFA standard's example does: a stated loss the client
finds intolerable, plus an anchor to her known liabilities?**
- Anchors: R-I2, R-AN17, X-11, R-W22.
- Official words: "An Investment Policy Statement (IPS) outlines an investor's financial goals, risk tolerance, and
  guidelines for managing a portfolio." (IPS p.1 L3-4, VRF).
- Hypothesis (guess):
  - CFA 2010 (VP): "Where possible, the IPS should account for known liabilities to lend some quantitative basis to
    the risk tolerance assessment." It adds that approaches may "define multiple levels of risk associated with
    avoiding financial catastrophe, maintaining a current standard of living, meeting a specific future financial goal,
    or developing significant further wealth". Its example: "an absolute loss in any 12-month period of more than 33
    percent is intolerable".
  - For Laura: risk tolerance = zero for the payments (bought); for the sleeve, a stated tolerable fall. For example,
    the sleeve can fall about a third without touching the payments or the bought 2031 floor (ASM; D3 to size).
  - The CFA's "multiple levels of risk" line is a professional endorsement of goal-by-goal risk. It is quotable
    evidence that our structure is standard, not invented.
- Would change: **sentence** (IPS risk tolerance) and possibly a **number** (the sleeve loss we say is tolerable).
- Deliverables: IPS. Domain: D8 (D3 for the number). Seed: 28.
- North Star: the case never states her risk tolerance (R-AN17). Deriving it in a measurable form shows client
  knowledge.

**Q16. From 2027, should the promise assets be held and reported as a separate account, as goals-based practice
does, so that "set aside in 2033" is a label on money already segregated?**
- Anchors: R-C50, R-AN28, R-AN26, brief section 8.9.
- Official words: "At the beginning of 2033, before making the first operating payment or contributing to the
  facility, Laura will set aside a portion of the portfolio to fund the ten payments." (case p.3 L94-95, VRF).
- Hypothesis (guess):
  - Yes. Goals-based practice runs "module-built portfolios" per goal (Brunel 2012, VP). UBS's "Liquidity" strategy is
    likewise a separate pot "to fund expenditure and meet liabilities for the next two to five years" (SNIP; UBS pages
    returned HTTP 403).
  - Brief section 8.9 settled *which number* is the reserve. This asks about *governance*: a separate sub-account from
    2027 makes the reconciliation sentence concrete and gives Laura one line to watch.
- Would change: **sentence** (IPS: the reserve is a separate sub-account from purchase). It also fixes how FR charts
  show two pots.
- Deliverables: IPS, FR. Domain: D8. Seed: 28.
- North Star: Laura can point to "the money for the residency's first ten years" as a thing that exists, which is
  also what co-sponsors want to see (BS-17).

**Q17. Which named frameworks fit which part of the plan? Which would a semifinal reader recognise, and which should
be left out (for example endowment spending rules)?**
- Anchors: R-S24, R-S26, R-W43, R-I46, v4 Part 2 lesson 1.
- Official words: "Demonstrates understanding and effective use of investment concepts and tools" (Portfolio
  Analysis criterion, R-S26, VRF). "Keep the presentation simple" (IPS p.3 L101-102, VRF).
- Hypothesis (guess), a proposed map:
  - Goals-based wealth management (Brunel; Das et al.) fits the overall structure.
  - Cash-flow matching or LDI fits the reserve.
  - Chhabra's framework fits the risk budget (corrected per Q04).
  - A surplus glidepath (Russell 2026) fits the sleeve.
  - The CFA IPS elements fit governance.
  - Endowment spending rules do *not* fit. They spend a percentage of a fluctuating fund forever, while Laura owes
    fixed dollars for ten years. Leave them out, and at most say why in the FR.
  - IPS: no framework names (jargon, R-I46). FR: one table with at most four.
- Would change: **sentence** (FR framework table; IPS stays jargon-free) and a **decision** (which names to drop).
- Deliverables: IPS, FR. Domain: D7 (D8 support). Seed: 28.
- North Star: using the right tool for each goal, and saying why one famous tool does not fit, shows judgement rather
  than name-dropping.

### C. The Final Report (tier 3)

**Q18. Should the plan commit to one progress measure (for example "payments covered: yes; funded ratio") and use it
the same way in every deliverable and every future report to Laura, as the CFA standard asks?**
- Anchors: R-C92, R-S24, BS-09, Q-A3-08.
- Official words: "Teams should use each deliverable for its intended purpose while maintaining a clear and
  consistent investment strategy across all three." (case p.4 L161-162, VRF).
- Hypothesis (guess):
  - CFA 2010 (VP): "Consistent use of metrics to assess and evaluate the risk profile of investment portfolios is
    important for meaningful comparisons to be made over time. Inappropriate use of different metrics to highlight or
    disguise certain risks should be avoided."
  - Morgan Stanley's goals system reports "Progress to Goals" (VP, same article as Q02).
  - One goal-progress metric, stated in the IPS and reused in TN reflections and FR charts, answers BS-09: bond price
    falls do not look like broken promises. It also prevents "metric shopping".
- Would change: **sentence** (IPS: the one measure) and FR chart design (the same metric each year 2027-2033).
- Deliverables: TN, IPS, FR. Domain: D9 (D8 support). Seed: 27.
- North Star: a single honest gauge that Laura can read in five seconds is what separates a trusted adviser from a
  report generator.

**Q19. Should the FR cite "behaviour gap" or "adviser's alpha" figures to justify pre-commitment rules, given that a
2026 peer-reviewed paper says the famous 1.2%-a-year gap overstates timing losses about twelvefold?**
- Anchors: R-AN32, R-S26, R-W47.
- Fact:
  - Morningstar *Mind the Gap 2025* (VP): the average dollar earned "about 1.2 percentage points per year less than
    these funds' 8.2% aggregate annual total return".
  - Vanguard (VP, *Putting a value on your value*, June 2020 brief): "Behavioural coaching 150" bps.
  - Fulkerson, Jordan, Riley & Yan, *Financial Analysts Journal* 2026 (VP abstract): "poor timing by mutual fund
    investors costs them only 0.10% per year".
- Hypothesis (guess):
  - Do not lean on either big number. Laura is a statistics graduate (R-AN32), and the AI policy warns about
    reference quality (R-W47).
  - Justify rules by her own decision dates instead: 2031 (public statement) and 2033 (reserve and facility). Those
    are the moments when an emotional decision would be costly.
  - Vanguard's own line can support the idea without the number: the IPS "sows the seed for future behavioural
    coaching opportunities ... Having a clearly set out investment policy will allow you to defend against these common
    behavioural pitfalls" (VP).
- Would change: **sentence** (FR behavioural rationale). It removes a statistic that could backfire.
- Deliverables: FR. Domain: D6. Seed: 27.
- North Star: refusing a flattering but contested statistic is itself evidence of the rigour a statistics-trained
  client is looking for.

**Q20. With the 2031 floor bought, the only way to land outside the co-sponsor range is to land *above* it. Should
the top of the range therefore be set at a stated percentile (for example Brunel's "wants" level, 80-85%), making
the confidence figure equal to that percentile?**
- Anchors: R-C69, R-AN9, R-C66, F-402, brief section 8.7.
- Official words: "state how confident they are that her 2033 contribution will fall within that range." (case p.3
  L117-118, VRF).
- Hypothesis (guess):
  - Yes. P(below floor) ≈ 0 by purchase, so P(within) = P(at or below the top end). Choosing the top at the 80th-85th
    percentile of the 2033 outcome distribution (computed in 2031) gives an 80-85% confidence statement.
  - This is Brunel's "wants" band (VP, Das et al. 2018 Table 1), and it links directly to the case's two-sided wording.
  - Planning software treats 75-90% as the "Confidence Zone" for adjustable goals (SNIP: MoneyGuidePro description
    via search; primary page not opened).
  - A 95% top would make the range wide and less useful; a 50% top would make "outside" too likely. This turns an open
    parameter into a principled number.
- Would change: **number** (the 2031 range's top end and the stated confidence) in the FR.
- Deliverables: FR. Domain: D3 (D8 support). Seed: 9 (case design), 26.
- North Star: a range whose confidence comes from a stated, professional rule is the most credible thing Laura can say
  to co-sponsors.

**Q21. How should the fundraising draft report uncertainty: dollar outcomes in named scenarios (practice now prefers
"outcomes, not probabilities"), with one probability at most, and wording that pre-empts the "wrong side of maybe"
reaction?**
- Anchors: R-S28, R-C70, R-C72, X-14, BS-05.
- Official words: "communicates Laura's potential facility contribution and investment uncertainty clearly and
  credibly to prospective co-sponsors." (criterion 5, R-S28, VRF).
- Hypothesis (guess):
  - Kitces (VP, kitces.com): "outcomes, not probabilities, are what matter to clients". The "wrong side of maybe
    fallacy" is "our tendency to interpret a projection as 'wrong' if the outcome is inconsistent with the most likely
    outcome forecasted" (VP).
  - Das et al. (VP) frame goals with two reference points: a Target Wealth and a Loss Threshold. These map onto the
    range's two ends.
  - Guess at the recipe:
    - The floor is stated as money already set aside (a fact).
    - The top end is stated as an expectation with its percentile.
    - Two or three dollar scenarios (weak, typical, strong markets) are each tied to what the residency can do.
    - "Never below" is used only for the bought part.
- Would change: **sentence** (the structure of the FR fundraising draft; the students write it).
- Deliverables: FR. Domain: D9 (D5 support). Seed: 9, 15.
- North Star: co-sponsors are not statisticians. A draft that gives them outcomes they can plan around protects
  Laura's credibility, which the case names as the key risk.

**Q22. Once the range is communicated in 2031, what may change it before 2033? Should the IPS pre-commit that the
floor never moves down and only the upside is revisited, like a guardrail rule?**
- Anchors: R-C66, R-C67, R-C71, BS-03.
- Official words: "If Laura promises more than she can ultimately contribute, she could damage her credibility and
  lose the confidence or participation of co-sponsors." (case p.3 L114-115, VRF).
- Hypothesis (guess):
  - Yes. With Kitces-style "guardrails", advisors give clients in advance "the portfolio value that would trigger
    spending changes and the magnitude that would be prescribed for such changes", instead of recomputing a
    probability each year (VP, https://www.kitces.com/blog/retirement-income-guardrails-monte-carlo-client-communication/).
  - For Laura: the floor is fixed because it is bought. The top end is revised only upward, or at one pre-announced
    date. The downside can never become a broken promise. This turns BS-03 (credibility as income) into a rule.
- Would change: **sentence** (IPS clause on the 2031 rule; FR communication plan).
- Deliverables: IPS, FR. Domain: D8 (D5 support). Seed: 27.
- North Star: a promise designed so it can only be beaten, never broken, is what a public figure would choose.

**Q23. How much should Laura hold back after the facility contribution? Do practitioner benchmarks (Brunel's 10% for
"opportunistic goals"; UBS's "Legacy" pot for assets beyond needs) give a defensible rule?**
- Anchors: R-C58, R-C84, R-AN19, R-C61, brief section 9 (post-2033 flexibility).
- Official words: "She recognizes that committing all remaining assets could limit her financial flexibility as the
  project develops." (case p.3 L102-103, VRF).
- Hypothesis (guess):
  - Brunel's worked example (VP, 2012): "The family also wants to reserve 10 percent of their total wealth ($3.5
    million) for what they call 'opportunistic goals.'"
  - UBS's Legacy strategy covers "assets in excess of what is needed" (SNIP).
  - One case study is weak evidence. Guess: state flexibility as a share of the post-reserve surplus (for example 10-25%)
    held back from the facility. Justify it by project risk (overruns, delay), not by a benchmark alone. The case says
    no contingency fund need be sized (R-C61), so a percentage rule stays within scope.
- Would change: **number** (share held back; the facility contribution) in the FR.
- Deliverables: FR. Domain: D8. Seed: 11 (case design).
- North Star: it shows we protect her ability to keep acting like an entrepreneur after 2033, which is who she is.

**Q24. After the 2031 floor is locked, should the rest of the sleeve still hold equities, given that goals-based
practitioners keep money needed within about 3-5 years mainly in fixed income?**
- Anchors: R-C62, R-C63, R-C65, F-402, brief section 9 (2031 rule parameters).
- Fact: the model locks 80% of the sleeve in a 2-year Treasury in 2031 (F-402). The other 20% stays invested to 2033.
- Hypothesis (guess):
  - Brunel (VP, 2012): "To provide for immediate lifestyle needs (within the next three to five years), we build a
    portfolio composed principally of fixed-income securities." UBS's Liquidity strategy covers "the next two to five
    years" (SNIP).
  - The unlocked 20% is not a *need*. It is upside she has not promised. So keeping it in equities is consistent with
    practice as long as the range's top end is set by rule (Q20), not by hope.
  - New versus brief section 9: the benchmark says the *promised* part must be out of equities (already done), and
    lets the unpromised part stay in. So the 80% parameter should equal "whatever is promised as the floor", not an
    arbitrary share.
- Would change: **number** (2031 lock share, defined by the floor promised) and an IPS clause.
- Deliverables: IPS, FR. Domain: D3 (D8 support). Seed: 26.
- North Star: a rule that links "what she says in 2031" to "what is locked in 2031" makes her words and her money
  match, which is what credibility is.

**Q25. Does an Australian practitioner benchmark earn a place? Australia's Retirement Income Covenant makes
superannuation trustees "balance" three objectives that mirror the IPS guide's trio. The Future Fund shows why a
long-dated promise *without* government backing must be matched.**
- Anchors: R-I11, R-I26, X-16, R-S27, v4 Part 2 lesson 4.
- Official words: "How does your strategy balance growth, risk, liquidity, funding reliability, and financial
  flexibility?" (IPS p.1 L20, VRF).
- Hypothesis (guess):
  - APRA/ASIC 2023 report (VP): trustees must "achieve and balance the three objectives of: maximising expected
    retirement income; managing expected risks to the sustainability and stability of retirement income; and having
    flexible access to expected funds during retirement". That is growth, funding reliability and flexibility, the
    case's own words, written into Australian law since 2022.
  - The Future Fund (Wikipedia, verbatim check, VP of the article text; futurefund.gov.au refused with 403) was set up
    to provide for public-servant pension liabilities. Its mandate targets "at least the Consumer Price Index + 4 to 5
    per cent per annum". It can take growth risk against a long-dated promise because the Commonwealth stands behind
    it; Laura has no taxing power behind her. That contrast explains lock-early in one sentence.
  - Guess: one sentence in the FR's Articulation section ("as Australians we noticed..."), true and short. No more.
- Would change: **sentence** (FR Articulation / authentic voice).
- Deliverables: FR. Domain: D8. Seed: null (v4 Part 2 lesson 4).
- North Star: an authentic team voice (R-S28) grounded in a real regulatory parallel is distinctive among ~2,300
  finishers and is honest about who we are.

---

## 3. Where our plan matches or falls short of top practice (benchmark table)

| Practice element (source, status) | Our plan today | Match? | Gap to close (question) |
|---|---|---|---|
| Goal-by-goal sub-portfolios (Brunel 2012, VP; Das et al. 2018, VP) | Reserve + growth sleeve | Match | Label every trade by goal (Q03); separate account (Q16) |
| Risk = chance of missing a goal (Das et al., VP) | Certainty market-consistent; sleeve measured on surplus | Match | Place on the practitioner scale and price it (Q09) |
| Risk allocation before asset allocation (Chhabra via princetoninfo.com, SNIP) | Implicit | Partial | Correct the bucket mapping (Q04) |
| Lock benefits, grow surplus (Russell 2026, VP) | Lock-early + sleeve | Match | Cite it; test the equity weight against it (Q06) |
| Answer the hibernation critique (JPM 2021, VP) | Not addressed | Gap | Q07 |
| Willingness vs capacity assessed separately (FCA FG11/05, VP) | Team docs conflate them | Gap | Q05, Q15 |
| Governance, review cycle, triggers (CFA 2010 section 2, VP) | None written | Gap | Q12 |
| Rebalancing policy documented (CFA 2010 section 4c, VP) | None written | Gap | Q01 |
| One consistent risk/progress metric (CFA 2010 section 4b, VP) | Not fixed | Gap | Q18 |
| Fee disclosure (CFA Asset Manager Code F.4.d, VP via A3) | No fee in model | Gap | Q13 |
| Outcomes, not bare probabilities, to clients (Kitces, VP) | Probability-led in council drafts | Partial | Q21 |
| Pre-committed response to bad markets (Morgan Stanley levers, VP; Vanguard, VP) | Implied | Partial | Q02, Q22 |
| Near-term needs in fixed income (Brunel, VP) | Floor bought in 2031 | Match | Tie the lock share to the promised floor (Q24) |
| Longer needs take more risk (Brunel, VP) | We do not | Deliberate difference | Explain why (Q08) |

---

## 4. Leads for the specialists

Sources read in this run (access 2026-09-27, UTC ~12:00-12:30), with what each is good for:

- **CFA Institute, *Elements of an Investment Policy Statement for Individual Investors*, May 2010** (VP):
  https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf
  - Sections: 1 Scope and Purpose; 2 Governance (2a-2e); 3 Objectives (3c risk tolerance); 4 Risk Management (4a
    reporting, 4b metrics, 4c rebalancing).
  - Key lines: "Perhaps most importantly, the IPS serves as a policy guide that can offer an objective course of
    action to be followed during periods of market disruption when emotional or instinctive responses might otherwise
    motivate less prudent actions." / "Where possible, the IPS should account for known liabilities to lend some
    quantitative basis to the risk tolerance assessment." / "If the policy is not to rebalance, this policy should be
    documented in the IPS." For D8, D10.
- **Brunel, "Goals-Based Wealth Management in Practice", CFA Institute Conference Proceedings Quarterly, March 2012**
  (VP; a copy hosted on squarespace):
  https://static1.squarespace.com/static/59e8d89d914e6b37450c946a/t/5c643e15104c7b43f7b84187/1550073366884/CFA+Goals+Based+WM_PDOC.pdf
  - Useful content: 3-5-year needs in fixed income; 6-15 years at a higher return assumption; the
    "declining-balance portfolio"; "a random fluctuation in asset values can be turned into a permanent loss of
    capital"; the 10% for "opportunistic goals"; and the risk definition as "the probability of not achieving goals"
    (reporting Das, Markowitz, Scheid & Statman 2010). For D8, D3.
- **Das, Ostrov, Radhakrishnan & Srivastav, "A New Approach to Goals-Based Wealth Management", *Journal of Investment
  Management* 16(3), 2018** (VP, author's site): https://srdas.github.io/Papers/GBWM.pdf
  - Table 1, Brunel's goal-probability table (Needs 90-95, Wants 80-85, Wishes 65-75, Dreams 50-60). Also the two
    reference points, Target Wealth and Loss Threshold. For D3, D8, D9.
- **CFA Institute Enterprising Investor, "Ashvin B. Chhabra: Understanding Goals Is the Value Proposition", 2015-08-05**
  (VP): https://blogs.cfainstitute.org/investor/2015/08/05/ashvin-chhabra-on-wealth-management-the-value-proposition-lies-in-understanding-client-goals/
  - Includes the three questions "What do you need for immediate safety? / What do you need to be comfortable? /
    What do you aspire to?" and the "human alpha" point.
- **Princeton Info, on Chhabra's "Beyond Markowitz"** (read verbatim, secondary source; quotes the 2005 paper:
  "risk allocation must precede asset allocation"):
  https://princetoninfo.com/business/beat-the-market-consider-your-risks-and-asset-allocation/
  - The original paper (*Journal of Wealth Management* 7(4), Spring 2005, pp. 8-34) was blocked: SSRN 403 and
    pm-research 429. Treat the quotes as SNIPPET-UNVERIFIED until D8 reads the paper or the book *The Aspirational
    Investor* (2015).
- **Russell Investments, "Pension surplus investing: Rethinking the value of overfunding", 2026-07-13** (VP):
  https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html
  - Key lines: "lock down the benefits promised, then grow surplus assets with a prudent process"; the 20/80-30/70
    optimum at 110% funded; incremental re-risking above a defined threshold. For D8, D3.
- **J.P. Morgan AM, "Rethinking the pension plan endgame: Hibernation, termination or stabilization?", October
  2021** (VP):
  https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/institutional/insights/portfolio-insights/portfolio-strategy/Rethinking-the-pension-plan-endgame.pdf
  - Structural impediments: downgrades (~50bp a year), longevity, experience losses. For D1, D8.
- **FRED corporate spreads** (VP): BAMLC0A0CM 0.79 and BAMLC0A2CAA 0.58 on 2026-09-24,
  https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM. For D1 (Q10).
- **FSA/FCA FG11/05, *Assessing suitability*, 2011** (VP): https://www.fca.org.uk/publication/finalised-guidance/fsa-fg11-05.pdf
  (capacity-for-loss definition, footnote 3). For D6.
- **Morgan Stanley, "Goals-Based Planning: Stay on Track"** (VP; undated on the page as read):
  https://www.morganstanley.com/articles/goals-based-financial-planning-stay-on-track (four levers; "Progress to
  Goals Reporting"). The GPS sample-report PDF gave an empty reply (unread). For D6, D9.
- **Kitces.com** (VP): https://www.kitces.com/blog/monte-carlo-guardrails-probability-of-adjustment-success-client-communication-dynamic-retirement-spending/
  ("outcomes, not probabilities") and
  https://www.kitces.com/blog/the-wrong-side-of-maybe-fallacy-and-the-interpretation-of-monte-carlo-analysis/
  ("wrong side of maybe"). For D9.
- **Vanguard, *Putting a value on your value: Quantifying Vanguard Adviser's Alpha*, research brief June 2020** (VP):
  https://www.ch.vanguard/content/dam/intl/europe/documents/en/putting-a-value-on-your-value-quantifying-vanguard-adviser-alpha-eu-en-pro.pdf
  (behavioural coaching 150bp; the IPS "sows the seed" passage). For D6.
- **Morningstar, *Mind the Gap 2025*** (VP):
  https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/blt2c5c4d9171638c42/689b424311f3880edc4b4813/US_Mind_the_Gap_2025.pdf
  - Contrast it with Fulkerson et al., *FAJ* 2026 (VP abstract):
    https://rpc.cfainstitute.org/research/financial-analysts-journal/2026/bad-timing-does-not-cost-investors-funds-returns
  - For D6.
- **APRA/ASIC, *Implementation of the retirement income covenant*, July 2023** (VP):
  https://www.apra.gov.au/sites/default/files/2023-07/Information%20report%20-%20Implementation%20of%20the%20retirement%20income%20covenant-Findings%20from%20the%20APRA%20and%20ASIC%20thematic%20review%20July%202023.pdf
  (the three objectives). For D8 (Q25).
- **Wikipedia, "Future Fund"** (VP of article text only; futurefund.gov.au refused with 403):
  https://en.wikipedia.org/wiki/Future_Fund ("CPI + 4 to 5 per cent"). D8 should confirm on the Future Fund's own
  mandate page or legislation.gov.au if Q25 is used.

Blocked or unread (do not guess their content):
- UBS Wealth Way PDFs (HTTP 403); the "two to five years" Liquidity wording is SNIPPET-UNVERIFIED.
- Chhabra 2005 on SSRN (403) and on pm-research (429).
- The Morgan Stanley GPS sample report (empty reply).
- MoneyGuidePro "Confidence Zone" 75-90% (search snippets only).
- Vanguard *Best practices for portfolio rebalancing* (not opened; "5% or so" is SNIPPET-UNVERIFIED).
- Moody's 2025 downgrade press release (not opened; SNIP).
- Kitces/Cerulli "~1% median fee at $500k-$1M" and "private bank minimum $10M" (SNIP).

Facts for researchers to reuse:
- DERIVED from F-102 (ASM: a flat spread over the Treasury curve): Treasury ladder at +58bp ≈ $276k, at +79bp ≈ $270.5k.
- Post-2028 funded ratio ≈ 1.52 (F-106 + F-409 inputs).
- Brunel's table (percentages) is in section 2, Q09.

Suggested owner hand-offs:
- D8: Q04, Q06, Q07, Q08, Q12-Q17, Q22, Q23, Q25.
- D3: Q20, Q24 (compute the 80th-85th percentile top end on the 2031 conditional distribution; size the tolerable
  sleeve loss in Q15).
- D1: Q10, Q11, Q14.
- D6: Q02, Q05, Q19.
- D9: Q18, Q21.
- D10: Q12 wording.
- D7: Q17.

---

## 5. Parked (logged, not pursued; failed the "would change something" filter or out of scope)

- Endowment smoothing rules (e.g., Yale-style) for the 2031 stretch. It adds complexity, and the floor is bought.
  Folded into Q17 as "does not fit".
- Private-bank structured products or "principal-protected notes" for the floor. Derivative-based and banned in WInS
  (R-W90); simpler Treasuries already do the job.
- The family-office "family governance/education" modules in Brunel. They do not fit a single client with a fixed
  project.
- Finale presentation framing of the benchmark (out of scope: semifinals only).

---

## What this teaches

Top professionals do not beat markets by guessing. They win client trust by doing four things that fit on one page:
- give every goal its own pot and its own required chance of success;
- lock what must happen and take risk only with what is left over;
- write down in advance what they will do when markets fall, and what changes (here: only the facility amount);
- report one honest measure the same way every time.

Our plan already does the first two. The gaps are mostly in writing the rules down: governance, rebalancing, fees and
one progress measure. Those gaps are cheap to close and rare among competitors.

Two further lessons:
- Borrowing a famous framework only helps if you use it correctly. Chhabra's "aspirational" bucket is Laura's career
  and her residency, not her spare cash.
- A popular statistic (the "behaviour gap") can be much weaker than it looks. Checking the counter-evidence before
  quoting it is what a client with a statistics degree would expect from the firm she chooses.
