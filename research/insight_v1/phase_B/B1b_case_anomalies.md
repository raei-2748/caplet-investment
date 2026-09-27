# B1b Case Anomalies: what is MISSING or CHANGED versus the last two seasons

Agent: B1b (lens "Case Anomalies", starting angle "missing or changed"), insight_v1 Phase B, written 2026-09-27.
AI-generated research (Claude Code) for Team Caplet, for brainstorming only. No submission-ready prose: where a
question says what a sentence "must contain", that is a checklist, and the six students write every word. Securities
are not named here (not needed for this lens). Scope: semifinal written deliverables only (brief section 4).

Status labels as in brief section 3. INTERPRETATION = my reading, never a fact. Every "hypothesis" is a GUESS.

---

## 0. Summary (read this first)

1. **Two official 2026-27 documents are missing from the repo.** The public SMApply page "Investment Competition
   Guide" (https://wghsinvcomp.smapply.us/res/p/guide/, read 2026-09-27) links two Box PDFs that are not in
   `competition/official/2026_27/` or `manifest.yaml`, and that no Phase A file cites:
   - a 5-page **"2026–2027 Investment Competition Guide"**
     (https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf, SHA-256
     `3638e84692ed0d826660a65e89cad0ce7eea8c1907b6a8f00ce02c0d51fb7add`);
   - a 1-page **"Competition Phases Infographic"**
     (https://upenn.box.com/shared/static/l2p0l26svbbptmcizhmswyq5f7rbyp44.pdf, SHA-256
     `2827f92a989d6d72fbc253d80d975eb06bd00c86f631e83850ae17eec544ed10`).

   Both are VERIFIED-PRIMARY (downloaded and read 2026-09-27). They add rules and wording that bear directly on the
   Trading Notes and the IPS (section 2). **Action for the main loop:** add both to `competition/official/2026_27/`
   and to the manifest (I may write only this file, so I have not).
2. **This season inverts last season's case.** In 2025-26 (Connor Barwin, MTWB) the headline goal was a **growth
   target**: grow $500,000 to at least $1.5 million by 2036. That is about 11.6% a year (DERIVED from a
   SNIPPET-UNVERIFIED copy), plus small annual grants from 2029. The case also stated a values rule: "Every dollar
   invested reflects MTWB’s values". This season the headline is a **fixed promise that must be certain**. There is
   no return target and no values language, and the capital project is the leftover amount. Last season's typical
   report habits (stock picks, "9% annualized" targets, ESG/thematic funds) are the wrong template this year. That
   is the clearest sign of what most of the ~2,300 finishing teams will get wrong (Q8, Q7).
3. **Wharton also changed the machinery, and every change points the same way.** Compared with last season:
   - the approved ETF list is gone, and "Any Government/Treasury Bonds" are now allowed;
   - WInS cash is cut from $500k to exactly Laura's $300k deposit;
   - trading now freezes on the IPS date, four weeks before the Final Report;
   - Trading Notes are a separate early deliverable, and last season's one-stock/one-ETF/team-choice pattern is gone;
   - "clever pitch" is replaced by "authentic team voice" and "earn her confidence";
   - "WInS can only accurately assess ... short-term investments" is replaced by "The WInS portfolio represents each
     team’s implementation".

   INTERPRETATION: the designers built a liability-matching case and then opened the tools and deadlines needed to
   show one.
4. **Top five questions** (ranked by effect on a deadline):
   - Q2, trade-note role tags now;
   - Q3/Q4, how the three notes should be chosen;
   - Q12, what the IPS must pre-commit, because the new Guide says "you may not redesign your strategy after
     observing the results";
   - Q5, whether WInS should show the Year-1 book;
   - Q20, whether the 2031 range is a number computed today or a rule applied in 2031.
5. **What is missing this year**, confirmed by word checks and comparison. No return target, no drawdown limit, no
   risk-tolerance number, no values/ESG preference, no living-cost figure, no facility cost, no contingency sizing,
   no inflation adjustment on the payments, no firm size or name, no "Your Investment Challenge" section, no stock/ETF
   language anywhere in the case, and no currency.
6. **What is new this year**:
   - co-sponsors;
   - a 2031 range with a confidence statement;
   - an "operating reserve" whose meaning clashes with the nonprofit term (Q18);
   - a Year-0 timing convention;
   - a residency in Taiwan;
   - a fundraising draft;
   - the IPS as a frozen "official record";
   - Trading Notes due before the IPS.

---

## 1. Comparison table: 2024-25 vs 2025-26 vs 2026-27

Sources: 2024-25 case page (VERIFIED-PRIMARY, live Wharton page). 2025-26 case: the Wharton page is retired; the text
comes from a Scribd copy of the Wharton page (SNIPPET-UNVERIFIED: a secondary copy, with some lines truncated in the
copy). 2025-26 welcome email: a Scribd copy (SNIPPET-UNVERIFIED). 2026-27: repo official files (VERIFIED-REPO-FILE) and
the new Guide (VERIFIED-PRIMARY).

| Element | 2024-25 (Ladi Ayoola) | 2025-26 (Connor Barwin) | 2026-27 (Laura Gao) | Change and likely reason (INTERPRETATION) |
|---|---|---|---|---|
| Money in | "$100,000 investment a baseline" | $500,000 | $300,000 (2027) + $150,000 (2028) | First two-deposit case; timing matters |
| Headline goal | "generate a return" for 3 build phases (2030, 2040) | "at least $1.5 million" by 2036 (≈11.6%/yr, DERIVED) | 10 × $50,000 fixed, "high degree of certainty" | Flipped from a return target to a certain liability |
| Costs given | "$10,000 USD per housing unit; however, material costs and market dynamics are always changing"; centre "at least $50,000"; a year of operations "at least a quarter of your original $100,000" | Project list, no costs (from the copy) | "total cost of the facility has not been determined"; not to be estimated | Cost estimating removed; inflation *discussion* kept (R-C85) |
| Payouts | Operating year 2040 | From "the end of year three (2029)", ~$10,000 and "can rise above" | Start of each year 2033-42, "spaced exactly one year apart", Year 0 = 2026 | Last year's timing was ambiguous (end of which year?); this year's is exact |
| Values | Impact quote in the client's voice | "Every dollar invested reflects MTWB’s values — community-first, locally rooted, and sustainability-minded." | None (0 hits for ESG/values/impact/sustainab, R-AN34) | Values language removed on purpose (Q7) |
| Firm | "WGAM" named | "The firm manages a diversified portfolio currently worth $100,000,000." | "an asset management company", unnamed and unsized | Firm context removed (Q10) |
| Asset language | n/a | "analyze industries and companies to identify appropriate stocks and Exchange-traded Funds (ETFs)"; "long-term and short-term profitability" | Case never says stock, ETF or bond (0 hits); TN guide: "not simply about selecting individual stocks" | Stock picking de-emphasised (Q4, Q8) |
| Persuasion | n/a | "compelling and clever pitch to convince Connor"; "win Connor’s business" | "authentic team voice"; "recommendations that can earn her confidence" | Tone moved from pitch to trust (Q9) |
| WInS role | n/a | "your 10 weeks on WInS can only accurately assess the performance of short-term investments" | "The WInS portfolio represents each team’s implementation of its investment strategy" | WInS moved from test bed to implementation (Q5) |
| WInS cash | $100,000 | $500,000 | $300,000 (= deposit 1) | Sized to Laura's Year-1 book |
| Instruments | Approved list (70% of stocks from it, per a 2024 guide: [PRIOR]) | "ETFs and treasury bonds from the approved lists" (2025 WInS guide, VERIFIED-PRIMARY [PRIOR]) | "Any ETF"; "Any Government/Treasury Bonds from any exchange available on WInS" | Tools opened for liability matching (Q6) |
| Deliverables | Final report (trading ended Dec 6, 2024) | Roster Oct 17; "Midterm Report" Oct 31 ("will be evaluated"); final report Dec 12; "Teams will have one portfolio" | TN Analysis Oct 23; IPS Nov 6 (trading freezes); Final Report Dec 4 | Strategy frozen before the report; the notes come first (Q12, Q2) |
| Disclaimer | n/a | "investment scenarios ... have been embellished" | Web: "the financial scenario is developed specifically for the competition" (R-AN56) | Same idea |
| Portfolio-manager sentence | n/a | Identical wording: "Your portfolio manager (your team’s teacher/advisor who makes the final investment decisions for your firm’s portfolio)" | Same | Boilerplate, not a new signal (Q10) |

Evidence that the redesign is deliberate: "The Wharton Global Youth team is doing some reimagining of our signature
competition" (Wharton news, April 2025, VERIFIED-PRIMARY). Typical 2025-26 reports (SNIPPET-UNVERIFIED Scribd copies,
lower authority, used only to gauge the field):
- "Profit Gurus" had a "Trading Notes Analysis" section with "ETF Selected: SPY / Stock Selected: AAPL / Team Choice:
  GOOGL" and cash of $422k of $495k.
- Another team built an "Enhanced ESG" portfolio "targeting 9% annualized returns" with clean-energy and
  infrastructure thematic ETFs.

---

## 2. The two official documents not in the repo (VERIFIED-PRIMARY, read 2026-09-27)

What they add beyond the case and the two guides (exact words):
- The Guide, p.2, gives the list of things to consider: "Your team will need to consider the client’s goals, time
  horizons, required cash flows, funding commitments, liquidity needs, desired degree of funding certainty, risk
  tolerance, and communication with potential co-sponsors." "Risk tolerance" is named here; the case never names it
  (R-AN17).
- The Guide, p.2, endorses a portfolio split by purpose: "how its components will support different needs".
- The Guide, p.3, sets what a trade note should capture: "When your team executes a trade in WInS, the Trading Note
  should capture the reasoning behind the decision, including its alignment with your strategy, the supporting research
  or analysis, and its expected role in growth, liquidity, risk management, or future funding."
- The Guide, p.3, gives the timing: "The Trading Notes Analysis is due at the end of Week 4 (October 23), two weeks
  before your IPS is due." It also says: "Do not treat Trading Notes as an afterthought."
- The Guide, p.3, says the step "UNDERSTAND" includes studying "sources of uncertainty".
- The Guide, p.5, on the freeze: "A long-term strategy may include planned adjustments as funding dates approach, but it
  should not be rewritten simply because markets move or hindsight reveals a different outcome." And: "You may identify
  decisions you would make differently, but you may not redesign your strategy after observing the results."
- The Guide, p.5, lists what is scored: "The competition recognizes thoughtful strategy, research and analysis, client
  understanding, disciplined decisions, management of risk and uncertainty, communication, and creativity." And:
  "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and tradeoffs
  behind those decisions."
- The Infographic: "Strategy guides every decision." "Strong submissions connect the client’s goals, research,
  portfolio decisions, and final recommendations through one clear and cohesive investment strategy." "There is no
  single correct strategy. Strong teams explain the reasoning, assumptions, and tradeoffs behind their decisions."
- The Guide, p.5: "September 15: Competition Materials Released" (the WInS practice period also began then).

---

## 3. The questions (ranked; the same content as the structured output)

Each entry gives: anchor, then hypothesis (a GUESS), then what would change, then the deliverable and domain, then the
North Star link.

### Q1. What do the two unrecorded official documents (the 5-page Guide and the Infographic) change in our Phase A conclusions?
- Anchor: R-new. Guide p.5: "you may not redesign your strategy after observing the results"; Guide p.3: "expected role
  in growth, liquidity, risk management, or future funding".
- Hypothesis (GUESS): they change little in the facts, but three things matter.
  - They make pre-commitment in the IPS explicit (Q12).
  - They give the four role words for trade notes (Q2).
  - They name "risk tolerance" and "tradeoffs", so the IPS should state both.
- Would change: a **decision**. Add both to the official set and re-run A1's cross-document check (X-items) against
  them. Deliverables: WInS-now, TN, IPS, FR. Domain: D10. Seed: none.
- North Star: a team that reads every official page designs to the judges' own checklist.

### Q2. Should every WInS trade note from now on name its role in the Guide's four words and link it to one dated cash flow of Laura's?
- Anchor: R-T11, R-W82, R-AN43 (notes cannot be edited). Guide p.3 quoted above.
- Hypothesis (GUESS): yes. Notes are locked when written. Any three can become the Oct 23 notes. The Guide defines the
  content: alignment, research, and role (growth / liquidity / risk management / future funding).
  - A checklist for each note: role word; which cash flow it serves (the 2033-42 payments / the 2031 range / the 2033
    facility); the research fact; the named risk.
  - Wharton's own sample note (R-AN44) has all four elements.
- Would change: a **decision**, the note template used from the next trade. Deliverables: WInS-now, TN. Domain: D10.
  Seed: 13.
- North Star: every trade visibly traces to one of Laura's dated needs, which a stock-picking team cannot show.

### Q3. Should the three Trading Notes deliberately show the three verbs "supported / tested / refined", so that at least one real trade before Oct 23 tests or refines the strategy?
- Anchor: R-C88 ("reflected, tested, or refined"), R-T9, R-T20. Infographic: "supported, tested, or refined the
  developing strategy".
- Hypothesis (GUESS): three "buy" notes for the initial allocation show only "supported".
  - A "tested" or "refined" note shows thinking. Examples: a duration-hedge rebalance after a rate move; a correction
    after learning a WInS rule.
  - It must be a real rule-triggered decision, not a trade made for the notes. The FAQ warns against "a lot of buying
    and selling". So write the rebalance rule into the notes now, and let the market trigger it.
- Would change: a **decision**, which trades to plan before Oct 23 and a rebalancing rule. Deliverables: WInS-now, TN.
  Domain: D7. Seed: 13.
- North Star: shows a firm that updates on evidence, which a statistics-trained client values.

### Q4. Does this year's Trading Notes Analysis still expect one stock, one ETF and one team choice, as last season's reports show, or may all three notes be bond/ETF trades?
- Anchor: R-T4 ("not simply about selecting individual stocks"), R-T8, R-T28. Last season's format (SNIPPET-UNVERIFIED,
  Scribd): "ETF Selected ... Stock Selected ... Team Choice".
- Hypothesis (GUESS): there is no quota this year. The official TN guide says "select three investment decisions that
  best illustrate your team’s strategic thinking", with no asset-type rule.
  - A lock-early portfolio may hold few or no single stocks, and that is allowed.
  - Confirm on the logged-in SMApply form (it may show separate fields).
- Would change: a **decision**, whether we need a stock position at all for the notes. Deliverables: WInS-now, TN.
  Domain: D10. Seed: 13.
- North Star: freed from a stock-pick ritual, every note can serve Laura's promise.

### Q5. Given the WInS cash cut from $500k to exactly Laura's $300k deposit, and "WInS ... short-term" replaced by "represents each team's implementation", should the WInS book show her Year-1 (2027) portfolio rather than the post-2028 target?
- Anchor: R-AN14, R-C75, R-W85, X-7. The item is open in brief section 9. **New evidence:** the change in wording from
  the 2025-26 case, and the Guide p.3: "your portfolio provides evidence of the decisions your team made".
- Hypothesis (GUESS): the designers sized WInS to the first deposit.
  - A Year-1 mirror is the most literal "implementation": about 97% in liability-matching bonds, the surplus in growth.
  - It is also the easiest to defend in the IPS.
  - The post-2028 mirror (~65/35) is defensible only if it is stated as "the target mix after the second deposit".
  - The team must pick one, and the Final Report must say which, in one sentence.
- Would change: a **decision** (the WInS weights now) and a **sentence** in the IPS. Deliverables: WInS-now, TN, IPS,
  FR. Domain: D7. Seed: 3.
- North Star: the portfolio judges see is Laura's own first year, not a generic model.

### Q6. Did Wharton open "Any Government/Treasury Bonds from any exchange" and drop the approved list so that liability-matching instruments can be used, and which 2032-2042 maturities does the WInS bond list actually offer?
- Anchor: R-W67-R-W69, R-AN48, F-606. [PRIOR] 2025 WInS guide: "ETFs and treasury bonds from the approved lists"
  (VERIFIED-PRIMARY). The 2025-26 list had no defined-maturity or zero-coupon funds (historical README).
- Hypothesis (GUESS): the opening was deliberate. The WInS bond drop-down may still list only some maturities. Check
  inside WInS before relying on a cash-flow match.
- Would change: a **decision**, individual bonds versus a fund mix in WInS. Deliverables: WInS-now, TN. Domain: D1.
  Seed: none.
- North Star: using the tools Wharton just opened shows we understood why they opened them.

### Q7. Why did Wharton remove all values language, and should our deliverables say explicitly that no values screen is applied, or stay silent?
- Anchor: R-AN34. 2025-26: "Every dollar invested reflects MTWB’s values" (SNIPPET-UNVERIFIED). 2024-25: "When I’m
  working or doing anything, I want to feel like I’m making an impact" (VERIFIED-PRIMARY). 2026-27: none.
- Hypothesis (GUESS): removed on purpose, to keep the case about certainty.
  - Teams that carry over ESG or thematic funds impose an unstated preference on the client.
  - Recommendation: say nothing in the IPS (words are scarce).
  - In the Final Report, one clause under client knowledge: we imposed no screen the case does not name, and gave the
    reason (cost and tracking of a fixed liability).
  - Never cite her identity as a reason for a screen.
- Would change: a **sentence** (FR client-knowledge section) and a **decision** (no thematic sleeve). Deliverables: IPS,
  FR. Domain: D6. Seed: 12.
- North Star: it respects Laura's actual stated wishes over a template.

### Q8. How many teams will reuse last season's growth-target template, and what one visible feature of our deliverables proves we did not?
- Anchor: R-AN17, R-C73. 2025-26 goal "$1.5 million by 2036" (SNIPPET-UNVERIFIED); ≈11.6%/yr (DERIVED).
- Hypothesis (GUESS): most teams will. Last year's sample reports lead with return targets and stock names.
  - Our visible difference: the first line of the pitch states the promise as already bought, with its price and date,
    and no return target.
  - A strong pitch must contain: who it serves; the promise; how it is secured; what the surplus is for.
- Would change: a **sentence** (the elevator pitch specification). Deliverables: IPS. Domain: D7. Seed: 1.
- North Star: the direct answer to "why us": we solved her case, not last year's.

### Q9. Since "compelling and clever pitch" and "win Connor's business" became "authentic team voice" and "earn her confidence", should our deliverables drop pitch devices in favour of adviser-style disclosure?
- Anchor: R-S25, R-S28, R-C8. 2025-26 wording (SNIPPET-UNVERIFIED).
- Hypothesis (GUESS): yes. Replace metaphors and branded framework names with three plain parts: what we know, what we
  assume, what could go wrong.
  - This fits a client whose first public work answered misinformation (R-AN33).
  - Judge Hahn's "hiding behind fancy terms" remark (SNIPPET-UNVERIFIED, winners.md) agrees.
- Would change: a **sentence**, the style checklist for the IPS and FR. Deliverables: IPS, FR. Domain: D9. Seed: none.
- North Star: Laura chooses the firm she can trust, not the firm with the best slogan.

### Q10. Since the "portfolio manager ... makes the final investment decisions" sentence is copied word for word from 2025-26, and the firm is now nameless and sizeless, should the IPS spend any words on governance beyond rules that any reviewer can apply?
- Anchor: R-C2, R-C3, R-AN4, X-10, BS-01, BS-02.
- Hypothesis (GUESS): the sentence is boilerplate.
  - The IPS should not describe an org chart or the advisor.
  - Its "decision-making framework" should be pre-committed rules (Q12).
  - Firm terms (fee, reporting) belong in the FR as ASSUMPTIONs, following CFA Asset Manager Code F.4.d.
- Would change: a **decision**, the IPS word budget. Deliverables: IPS, FR. Domain: D10. Seed: 2.
- North Star: rules Laura can check herself beat an authority she must trust.

### Q11. Why does every official document list "liquidity" when the case removes every liquidity need before 2033, and what should "liquidity" mean in our IPS?
- Anchor: R-I6, R-I11, R-I21, R-C33, R-C34, R-C74; Guide p.2 "liquidity needs".
- Hypothesis (GUESS): here "liquidity" means two things:
  - (a) each Jan 1 payment 2033-42 is paid on time from maturing bonds;
  - (b) the growth sleeve can be turned into cash for the 2033 facility without a forced sale in a bad year.

  There is no cash buffer before 2033, since living costs are outside the portfolio. A generic "keep 5% cash for
  liquidity" shows the team did not read the case. The WInS cash weight should be small and explained.
- Would change: a **sentence** in the IPS and a **number** (the WInS cash weight). Deliverables: WInS-now, IPS.
  Domain: D10. Seed: none.
- North Star: shows we read her case line by line.

### Q12. Which rules must the IPS pre-commit so the Final Report can "evaluate" them without "redesign[ing] your strategy after observing the results"?
- Anchor: R-I34, R-I35, X-5, X-23; Guide p.5 (quoted in section 2).
- Hypothesis (GUESS): the IPS needs one-line rules for:
  - (1) rates moving before the January 2027 purchase;
  - (2) a smaller or late 2028 deposit;
  - (3) how the 2031 range is set;
  - (4) the 2033 order of use: reserve including payment 1, then facility, then flexibility (seed 5);
  - (5) sleeve rebalancing bands;
  - (6) what happens to money left over after 2033.

  The Final Report may then show "the rule fired as written". Anything not pre-committed and later changed looks like
  a redesign.
- Would change: a **decision**, the IPS content checklist. Deliverables: IPS, FR. Domain: D10. Seed: 5.
- North Star: a firm that commits in advance protects Laura from its own hindsight.

### Q13. The case gives no 2027 prices ("Year 0 ... before any money has been invested"), so what price date should projections use, and how is that stated?
- Anchor: R-C28, R-C77, R-AN22, F-101, F-111, F-112.
- Hypothesis (GUESS): use the latest official curve (2026-09-25: $292,264) as a labelled ASSUMPTION. Show the ±50bp
  band ($278k-$307k) and P(cost > $300k) ≈ 24% (ASSUMPTION model). Point to rule (1) in Q12.
- Would change: a **number** and a **sentence** in the FR assumptions. Deliverables: FR, IPS. Domain: D1. Seed: 4.
- North Star: honest about the one thing we cannot know yet.

### Q14. Does "objectives that reflect ... her passion for innovation" justify any innovation, tech or AI tilt, or does "innovation" describe the residency?
- Anchor: R-C25 (case p.2 L39-41; the only use of "innovation").
- Hypothesis (GUESS): it describes her goals, not asset choices. Many teams will buy AI or tech names on this word.
  Any tech weight should come only from broad-market weights (section 9's AI-exposure item).
- Would change: a **decision**, the sleeve composition (no thematic tilt). Deliverables: WInS-now, IPS. Domain: D2.
  Seed: 20.
- North Star: we invest for her goals, not for her adjectives.

### Q15. Why may co-sponsors fund the facility but not her commitment, and should the fundraising draft lead with the fully pre-funded ten years of operations, putting the facility range second?
- Anchor: R-C44, R-C48, R-AN6, BS-17.
- Hypothesis (GUESS): funders least like to pay for operations. Her covering them removes their biggest worry. So the
  pre-funded operations are the credibility anchor, and the facility range is the invitation.
- Would change: a **sentence**, the order of the fundraising draft. Deliverables: FR. Domain: D5. Seed: 6.
- North Star: turns a case rule into Laura's strongest fundraising fact.

### Q16. Will co-sponsors read "operating reserve" in its nonprofit sense (months of expenses held by the organisation), and should the fundraising draft use a different label?
- Anchor: R-C51, R-new.
- Evidence: the nonprofit benchmark ratio is "above 25% (equivalent to three months) is better" (nonprofitaccountingbasics.org, VERIFIED-PRIMARY).
- Hypothesis (GUESS): yes, there is a risk of misreading.
  - The case's reserve is ten years of her personal commitment, about 40 times the sector norm.
  - Keep "operating reserve" in the IPS and FR, because it is the case term.
  - In co-sponsor text, describe it plainly: ten payments already funded.
  - Note that the residency may still need its own short-term reserve, which is outside her commitment.
- Would change: a **sentence** (the vocabulary of the fundraising draft). Deliverables: FR. Domain: D5. Seed: none.
- North Star: we speak the co-sponsors' language on Laura's behalf.

### Q17. Why does the case name an "endowment" next to the contingency fund, and how should money left over after 2033 be described so co-sponsors do not assume it is a perpetual fund for years after 2042?
- Anchor: R-C61, R-C49, R-AN59.
- Hypothesis (GUESS): the designers expected teams to propose endowments. Describe the leftover as uncommitted
  flexibility governed by a rule, with no promise beyond 2042.
- Would change: a **sentence** in the FR and the fundraising draft. Deliverables: FR. Domain: D5. Seed: 7.
- North Star: it prevents an accidental overpromise, which is exactly what the case warns about.

### Q18. Does "recommend the dollar range Laura should communicate" in 2031 ask for a range computed today (a 5-7-year forecast) or a rule Laura applies in 2031 (a 2-year forecast), and how do we give both without looking evasive?
- Anchor: R-C62, R-C65, R-C68, R-AN7.
- Hypothesis (GUESS): the case wants numbers ("dollar range"), but the true decision happens in 2031.
  - Give the 2031 rule: floor = what is already secured in a 2-year Treasury; top = a stated percentile.
  - Also give today's projected range under that rule, e.g. median floor ≈ $165k (F-402, ASSUMPTION model), with the
    spread across scenarios.
  - The two differ a lot in width.
- Would change: a **number**, the headline range in the FR. Deliverables: FR. Domain: D3. Seed: 8, 9.
- North Star: gives Laura a method she can reuse, not a guess that ages.

### Q19. Because Laura decides her 2033 contribution, can "will fall within that range" be made partly a policy outcome, so that the stated confidence depends only on the low end?
- Anchor: R-C69, R-AN9, R-C58, R-C84.
- Hypothesis (GUESS): yes, with a rule: contribute at least the floor, and at most the top of the range. Anything above
  the top stays as flexibility.
  - "Above the range" then cannot happen by design.
  - Confidence = P(available ≥ floor). With a bought floor, that is near-certain (barring U.S. default).
  - Disclose that the top is a cap Laura chooses, not a forecast.
- Would change: a **number** (the confidence %) and a **sentence** (range definition). Deliverables: FR. Domain: D3.
  Seed: 9.
- North Star: a confidence statement that a statistician would accept.

### Q20. Given that the payments are nominal, where exactly must inflation appear, and should every co-sponsor dollar figure be tagged "2033 dollars" or "today's dollars"?
- Anchor: R-C46, R-C85, R-AN3, R-AN8, F-114, F-508.
- Evidence: 2024-25 "material costs and market dynamics are always changing" (VERIFIED-PRIMARY).
- Hypothesis (GUESS): inflation belongs in three places:
  - (1) the real value of the projections;
  - (2) facility costs: Taiwan construction costs ≈3.5%/yr since 2021, not the 6.5% spike;
  - (3) the real erosion of the fixed $50k: $42.1k in 2033 and $33.7k in 2042 at 2.5% (in 2026 dollars). Who absorbs
    that loss is open in section 9.
- Would change: a **sentence** and a **number** (a two-column range in the FR). Deliverables: FR. Domain: D4. Seed: 10.
- North Star: shows Laura what her money will actually buy in Taiwan.

### Q21. How do we express "financial flexibility" as a rule or ratio, instead of a contingency fund the case says we need not size?
- Anchor: R-C58, R-C61, R-C84, R-AN19.
- Hypothesis (GUESS): use a share of the post-reserve surplus kept uncommitted until named project milestones, stated
  in the IPS as a rule and sized in the FR.
- Would change: a **number** (the share) and a **decision**. Deliverables: IPS, FR. Domain: D8. Seed: 11.
- North Star: flexibility "as the project develops" expressed in Laura's own words.

### Q22. With charts, citations and "detailed financial calculations" excluded, which few numbers must the 500-word IPS still carry to be testable, and what counts as "detailed"?
- Anchor: R-I55, R-C92, X-3.
- Hypothesis (GUESS): 3-6 numbers are enough, e.g. $50,000 × 10 from 2033, the funded-ratio test, the sleeve equity
  band, rebalancing bands and the flexibility share. Leave out tables and projections.
- Would change: a **sentence**, the IPS numbers list. Deliverables: IPS. Domain: D9. Seed: 14.
- North Star: words alone must prove the plan is checkable.

### Q23. Which three tradeoffs should the IPS name, since the Guide, the Infographic and the FAQ all say that strong teams explain "reasoning, assumptions, and tradeoffs"?
- Anchor: R-W43, R-AN17, X-11; Infographic quote.
- Hypothesis (GUESS):
  - (a) certainty of the promise vs the size of the facility;
  - (b) sleeve growth vs a higher 2031 floor;
  - (c) locking now vs waiting for rates.

  Each tradeoff must say what Laura gives up.
- Would change: a **sentence**, the IPS content checklist. Deliverables: IPS. Domain: D9. Seed: none.
- North Star: shows Laura the choices were hers to see.

### Q24. What makes a personal contribution "meaningful" to co-sponsors when no facility cost exists: its dollar size, its share of Laura's own post-reserve assets, or how certain it is?
- Anchor: R-C64, BS-06.
- Hypothesis (GUESS): funders read a lead gift by commitment relative to capacity, and by how firm it is. So present
  the floor as a share of what remains after the ten-year commitment is secured.
- Would change: a **sentence** (the framing of the fundraising draft). Deliverables: FR. Domain: D5. Seed: none.
- North Star: a contribution that is meaningful because it is certain, which matches her credibility.

### Q25. Given that the FAQ still says "10 weeks of trading" and "long-term portion of your portfolio" (recycled text), does "Investments permitted (for BOTH contributions)" really limit Laura's long-term plan to instruments listed in WInS?
- Anchor: R-AN15, R-AN46, F-606.
- **New evidence:**
  - Trading this year is about 6 weeks, so the FAQ text is recycled.
  - The 2025-26 welcome email says "Teams will have one portfolio" (SNIPPET-UNVERIFIED), which implies that earlier
    seasons had more than one.
- Hypothesis (GUESS): "BOTH" is probably a leftover. The safe course is still to name instrument types available in
  WInS, and to mark any STRIPS recommendation for the real plan as not tradable in WInS.
- Would change: a **decision** (whether the long-term plan names STRIPS). Deliverables: FR, IPS. Domain: D10. Seed:
  none.
- North Star: stay compliant without crippling the real-world plan.

### Q26. Last season's written reports were screened by "Wharton School student evaluators" plus "a professional review panel of asset managers from Aberdeen Investments": how much fixed-income precision and plain English should our written deliverables target?
- Anchor: F-611, R-W24 (the Rules page on Top 50 selection). The news quote is VERIFIED-PRIMARY.
- Hypothesis (GUESS): two readers.
  - A student screener: needs plain English, one glossary line per term.
  - A bond professional: will check durations, cash-flow match and Treasury maturity dates. So precision matters and
    errors are costly.
  - Confirm whether the same set-up holds for 2026-27 (not stated).
- Would change: a **decision** about the depth and the glossary in the FR. Deliverables: FR, IPS. Domain: D7. Seed:
  none.
- North Star: written for the people who actually decide the Top 50.

### Q27. Which "sources of uncertainty" should our deliverables name, and does the case's list of where the 2028 money comes from invite a deposit stress test despite "will"?
- Anchor: R-C27, R-AN31, R-AN35, BS-13; Guide p.3 "sources of uncertainty".
- Hypothesis (GUESS): name five:
  - markets;
  - rates before 2027;
  - the size and timing of the 2028 deposit;
  - inflation and facility costs;
  - the currency.

  Stress the deposit only as a labelled team scenario.
- Would change: a **decision** (the FR scenario set) and a **sentence** in the IPS. Deliverables: IPS, FR. Domain: D6.
  Seed: 16.
- North Star: shows we understand her income comes from her own brand.

### Q28. Why is the residency in Taiwan when the case gives Laura no link to Taiwan, and may we cite her public professional statement that she worked as a comic artist from Taipei?
- Anchor: R-C39, R-AN10.
- Evidence: the 2021 Overachiever Magazine interview (VERIFIED-PRIMARY, 2021-03-15): "I’m currently in Taiwan, Taipei.
  My current day job is as a comic artist."
- Hypothesis (GUESS): Taiwan is a real professional link, not tokenism.
  - Use it at most as one client-knowledge clause.
  - The interview also contains personal-life material; do not use it (brief privacy rule).
- Would change: a **sentence** in the FR client section. Deliverables: FR. Domain: D6. Seed: 19.
- North Star: shows we researched her beyond the case, without using her identity as decoration.

---

## 4. Parked (logged, not pursued)
- The case's "Investment Competition Guide" page header (R-C1) also names the new Guide. Probably shared branding; no
  deliverable effect.
- 2025-26 had a first-trade deadline (Oct 10, 2025, SNIPPET-UNVERIFIED welcome email). No 2026-27 primary page states
  one (guardrails b3). Trading in week 1 makes it moot.
- The field-size wording differs: 2025-26 "more than 5,400 high school teams ... began" (finalist article,
  VERIFIED-PRIMARY) vs "more than 6,300 registered" vs ~2,300 finished. The effect on deliverables is nil; R-AN60
  covers it.
- The "Year numbers" convention itself (R-AN12) is answered. The only residual is a dated cash-flow table as the FR's
  first exhibit (FR chart spec for D9).

## 5. Leads for the specialists
- **D10 (compliance):**
  - Ingest the Guide and Infographic (section 0.1 URLs and hashes).
  - Check the logged-in TN form for asset-type fields (Q4) and the WInS bond drop-down for 2032-42 maturities (Q6).
  - The FAQ's recycled phrases ("10 weeks of trading", "long-term portion", "for BOTH contributions") support reading
    2 of R-AN15.
- **D7 (Wharton intent):**
  - 2024-25 case page (live, VERIFIED-PRIMARY): https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/
  - The 2025-26 case text survives only as a Scribd copy: https://www.scribd.com/document/965855349/Case-Study-Wharton-Global-Youth-Program
    (curl works; the text is in the HTML `<p>` blocks, some lines truncated).
  - 2025-26 welcome email copy: https://www.scribd.com/document/933222558/25-26-Welcome-Email
  - Sample 2025-26 team reports (field-habit evidence only): https://www.scribd.com/document/980515751/Full-Report-Connor-MTWB
    and https://www.scribd.com/document/977481046/Updated-Investment-Strategy-for-Connor-Barwin
  - "Reimagining" quote: the BAM 2025 article.
- **D5 (philanthropy):**
  - Nonprofit operating-reserve norm (3 months = 25%): https://www.nonprofitaccountingbasics.org/internal-reporting/operating-reserve-ratio
    (VERIFIED-PRIMARY). Also the NORI definition (SNIPPET-UNVERIFIED via search; the candid.org page is blocked).
  - Needed: lead-gift and "leadership gift" practice for how a founder's pledge is stated as a range.
- **D6 (client):**
  - The Overachiever interview (2021-03-15, VERIFIED-PRIMARY) has professional risk-attitude lines: "you should always
    take the jump because you’re always going to regret not doing it"; and, on leaving tech, "It’s not an easy thing
    to say, “let me give up my incredibly cushy, paying job with health insurance to be self-employed, with unstable
    income.”"
  - Use only these professional lines; the page also has private material.
  - The case pull quote is still unattributed. It was not found in this interview or by search (SNIPPET search,
    2026-09-27).
- **D3 (quant):** Q18/Q19 need the 2031 range computed two ways: from 2027 (today's view) and as a 2031 rule
  (conditional two-year view). They also need a confidence definition under a contribution cap.
- **D1 (rates):** the price-date assumption (Q13) and a list of the WInS bonds available.
- **D4 (Taiwan):** use the construction-cost trend of ~3.5%/yr (F-508), not the one-year 6.5% spike, for the
  two-currency, two-dollar-date tags (Q20).
- **D9 (communication):** the tone shift (Q9); the tradeoff sentences (Q23); the IPS numbers list (Q22); the
  reserve-label clash (Q16).

## 6. Sources (all accessed 2026-09-27)
| Source | URL / path | Status |
|---|---|---|
| 2026-27 case, IPS guide, TN guide, SMApply page | `competition/official/2026_27/` | VERIFIED-REPO-FILE |
| 2026-27 Investment Competition Guide (5 pp) | https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf via https://wghsinvcomp.smapply.us/res/p/guide/ | VERIFIED-PRIMARY |
| 2026-27 Competition Phases Infographic | https://upenn.box.com/shared/static/l2p0l26svbbptmcizhmswyq5f7rbyp44.pdf | VERIFIED-PRIMARY |
| SMApply FAQ ("10 weeks of trading", "BOTH contributions") | https://wghsinvcomp.smapply.us/res/p/faqs/ | VERIFIED-PRIMARY |
| 2024-25 case (Ladi Ayoola) | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/ | VERIFIED-PRIMARY |
| Archive of clients and winners | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/ | VERIFIED-PRIMARY |
| 2025-26 case text (Connor Barwin) | https://www.scribd.com/document/965855349/Case-Study-Wharton-Global-Youth-Program | SNIPPET-UNVERIFIED (secondary copy; the Wharton original is retired) |
| 2025-26 welcome email | https://www.scribd.com/document/933222558/25-26-Welcome-Email | SNIPPET-UNVERIFIED |
| 2025-26 sample team reports | Scribd 980515751, 977481046 | SNIPPET-UNVERIFIED (field evidence only) |
| 2025-26 season article (evaluators; 6,300; 2,300) | https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/ (Jan 27, 2026) | VERIFIED-PRIMARY |
| 2026 finalists article ("5,400 ... began") | https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/ | VERIFIED-PRIMARY |
| 2026 champions article | https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/ | VERIFIED-PRIMARY |
| 2025 BAM article ("reimagining") | https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/ | VERIFIED-PRIMARY |
| 2025 WInS User Guide [PRIOR] | https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2025/09/2025-WInS-User-Guide.pdf | VERIFIED-PRIMARY [PRIOR] |
| Nonprofit operating-reserve ratio | https://www.nonprofitaccountingbasics.org/internal-reporting/operating-reserve-ratio | VERIFIED-PRIMARY |
| Overachiever interview with Laura Gao (2021-03-15) | https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid | VERIFIED-PRIMARY (professional lines only) |
| Blocked or failed | Wayback CDX (connection reset); the 2025-26 Wharton case page (retired, 404 on the guessed slug); lauragao.com/about (404) | — |

## What this teaches
- Comparing a document with its earlier versions is one of the fastest ways to find what the authors care about. What
  they **removed** (return targets, values language, stock-picking instructions, cost figures) tells you which old
  habits they now want you to drop. What they **added** (certainty, co-sponsors, a frozen strategy) tells you what
  will be scored.
- Always check every link on an official page. Two official documents were sitting one click away, unread.
- A word can mean different things to different readers ("operating reserve" to a nonprofit, "liquidity" in a case
  with no cash needs). Good advisers translate for each audience rather than copying the source's wording.
