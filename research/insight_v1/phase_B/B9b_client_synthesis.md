# B9b Client Synthesis: Laura as a decision-maker choosing between firms

Agent B9b, insight_v1 run, Phase B (question generation), written 2026-09-27. Lens: "Client Synthesis (deep client
understanding)". Starting angle: Laura as the person who reads competing proposals and picks one. She has a Wharton
statistics degree, was a tech product manager who ran A/B tests, is an author-illustrator and professor, and builds
community institutions. The question is how that person would judge a plan. The other B9 agent starts elsewhere.

This file is AI-generated research (Claude Code) for Team Caplet, for brainstorming only. It contains questions,
evidence, numbers and checklists. It contains **no text meant for submission**. The six students decide and write
every deliverable in their own words, and must record AI use in the Final Report's Works Cited (R-W46). Privacy: I
used only her public professional record. Her resume PDF and website also carry contact details, hobbies and
family-related comics. I left all of that out on purpose. Nothing here suggests contacting her (R-W16).

Status labels follow brief section 3: **VP** = VERIFIED-PRIMARY (read and grep-checked by me, 2026-09-27), **VRF** =
VERIFIED-REPO-FILE, **SU** = SNIPPET-UNVERIFIED, **ASM** = ASSUMPTION, **PU** = PARAPHRASE-UNVERIFIED, **INT** =
INTERPRETATION (my reading, not a fact). Every "hypothesis" is a **guess**.

---

## 0. Summary (read this first)

1. **Her own analytic work already labels its results by quality, and our plan should do the same.** In her data
   project "Rewriting Herstory" (lauragao.com) she publishes "The [unfinished] results" in a table whose last column
   is "Match Quality", with rows graded "Good", "Unsure" or "Bad" (VP). Her dance-music study ends with limitations
   and next steps ("Further probing … would provide deeper analysis") and takes its definitions from the data source
   ("For the purposes of this study, I used Spotify's definitions") (VP). Someone who works like this will trust a plan
   that grades its own numbers: which are observed market prices, which are estimates, and which are assumptions. She
   will distrust a plan that presents one model output as fact. (Q9, Q10)
2. **Her CV is a product-and-evidence CV, not a finance CV.** Her resume lists:
   - "Experimented and shipped 10 features" as a Twitter PM, in teams called "Growth ML" and "Abuse & Safety";
   - "A/B testing" as a skill;
   - as an Amazon data analyst, she "Investigated cause of 1.5M cases of transactions from unattributed ads";
   - she "Beta-tested MVP with 300K+ users of economics platform, Marginal Revolution University";
   - she ran "usability tests with nurses and doctors" with NIH researchers.

   All VP. Four habits of mind follow (INT):
   - compare against a **control**;
   - **attribute** results to their causes;
   - **test with real users** before launch;
   - protect **guardrails** while optimising one goal.

   Each gives a question below that most teams will not think to ask (Q3, Q7, Q11, Q12, Q14).
3. **At today's yields her "required return" is below the Treasury yield.** DERIVED from the case cash flows (VRF):
   - The ten payments alone need only **1.05% a year** on her $450k.
   - Each extra $50k of 2033 facility money adds about 1.05 points.
   - Payments plus a $200k facility need **5.25%**, about what Treasuries pay today (F-001, F-012).

   A professional would open the client picture with this "return objective". It reframes the whole plan. Growth is
   not needed to *meet* her goals. It is optional upside for the facility, bought with risk. (Q2)
4. **The "control arm" shows the growth sleeve's lift is modest.** Scratch runs of the verified model (ASM inputs,
   see Q3) give the lock-early 2033 surplus p5/p50/p95 by sleeve equity weight:

   | Sleeve equity | Sleeve bonds at 4.0% (JPM, as in the verified model) | Sleeve bonds at 5.0% (ASM, near today's 5y) |
   |---|---|---|
   | 0% | $177k / $195k / $215k | $183k / $201k / $222k |
   | 30% | $174k / $202k / $235k | $178k / $206k / $241k |
   | 60% | $159k / $207k / $273k | $161k / $210k / $277k |

   So 60% equity buys about **+$9k at the median** and **+$55k at the 95th percentile**, and costs about **-$22k at
   the 5th percentile**, against an all-bond sleeve. A former A/B tester will ask "what is the lift over the
   control?", and this is the answer. It sharpens the open equity-weight decision (brief section 9) with the
   0%-equity end, which the verified runs did not show (F-407 covers 50/60/70% only).
5. **The best answer to "why choose us" may be a job, not a return.** The job she hires a firm to do (INT): let her
   make public promises in 2031 that she never has to walk back. Her 2028 money comes from reputation-driven work
   (R-C27). The case warns that overpromising "could damage her credibility" (R-C66). The 2026-27 criterion asks for
   recommendations "that can earn her confidence" (R-S25). B2b found that Wharton moved the criterion from "win
   him/her over" to "earn her confidence". A plan built around that job reads as understanding, not analysis. (Q1)
6. **One seed-bank premise fails verification.** Seed 17 speaks of "learning to fall safely". Her second book's own
   page says the heroine, "Once dubbed the Queen of Balance as her school’s top rock climber", "suffers an injury that
   sidelines her". The "Falling" in the title is falling in love. This is publisher copy about a fictional
   character, not Laura's words (VP). Any "fall safely" or "Queen of Balance" metaphor would be both a misreading and
   the gimmick she rejects ("No more gimmicks.", B8a #21). (Q22)
7. **Do not assume she is anti-AI.** She worked on "Growth ML" at Twitter. Her studio lists a client described as
   "AI-powered online learning software" (VP). How the index's AI concentration is described, and how the team
   records its own AI use, should be neutral and exact. It should not be written as a values statement on her
   behalf. (Q18)

Counts: **25 questions** (section 3), plus a client-picture table (section 2), 20 verified phrases from her own
professional pages (section 4), and leads for the specialists (section 5).

---

## 1. Method and what is new versus B8a/B8b

- **Read first:** the brief, v4 Parts 1-3, 5 and 6, CLAUDE.md, the case, and the Phase A registers. I also skimmed
  B2a/B2b, B4a/B4b, B7a/B7b and B8a/B8b so that I do not repeat them. B8a and B8b already cover her quotes on risk,
  gimmicks, purpose statements, staged institutions, late books and the pull quote. I cite their findings by number
  (e.g. "B8a #21") and do not re-ask their questions.
- **New primary reading (all 2026-09-27, `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL --grep`,
  each returned `PHRASE FOUND VERBATIM: YES`):**
  - her resume PDF (work history, skills);
  - four "Visual Data Stories" pages (/data-journalism, /rewriting-herstory, /the-evolution-of-dance-music,
    /philly-happy-hours);
  - /projects, /editorial, /hey, and the Kirby book page.

  These show *how she analyses and presents evidence*. That is the question my starting angle poses, and B8a/B8b did
  not mine these pages.
- **Web search:** the session's WebSearch budget was used up (200/200) before this agent started. So I found no new
  URLs by search. I read only pages linked from her own site, and I could not check two leads: her public statements
  on generative AI, and #PublishingPaidMe. Both are listed as open leads (section 5).
- **Numbers:** two small derivations, both reproducible:
  - The required-return IRRs: scipy root-find on the case cash flows.
  - The control-arm table: runs `research/verified_2026-09-27/strategy_mc.py` unchanged. The only changes are the
    sleeve equity weight (0/30/60%) and, in one column, the sleeve-bond compound return (5.0%). The script is in the
    session scratchpad, not the repo. I was told to write only this file, so D3 should rebuild it under
    `research/insight_v1/scripts/`.
- **Not re-asked (brief section 8):** lock-early vs growth-first, tiering, one curve, surplus-only risk and the other
  settled items. Q3 touches item 5 ("more sleeve equity buys range, not median"). The **new evidence** is the 0%
  equity control and the 5% bond variant.

---

## 2. The professional client picture (CFA-style objectives and constraints)

This is the frame a top adviser fills in first. The CFA Asset Manager Code B.6.a asks managers to "Evaluate and
understand the client's investment objectives, tolerance for risk, time horizon, liquidity needs, financial
constraints, any unique circumstances" (via A3 SH-25, VP). The Rules page tells teams to operate by that Code (R-W29).
The IPS guide's own definition names "risk tolerance" (R-I2). Each cell says what we know, its status, and what we
still do not know (the gap becomes a question).

| Element | What we know | Status | What we still do not understand (question) |
|---|---|---|---|
| Return objective | Payments alone need 1.05%/yr on $450k; payments + $100k facility 3.15%; + $200k 5.25%; + $250k 6.28% | Derived from R-C26, R-C27, R-C45 (VRF) | Is the facility a "need", a "want" or a "wish" for her? (Q2, Q25) |
| Risk willingness | "willing to take thoughtful risks"; "Although…" she wants a balance (R-C37, R-C38). Revealed pattern: she leapt only after a contract secured the base (B8a #4-#5) | VRF + VP via B8a | Is her risk budget already spent on her career and the residency? We cannot interview her (R-W16), so every inference must be labelled (Q4) |
| Risk ability | Payments: none needed once bought. Sleeve 2027-30: high (living costs outside, R-C33). Pledged floor after 2031: close to nil (R-C66). Post-2033: tied to project needs | VRF + INT | How big are her "financial resources outside the portfolio" (R-C33)? Unknown; state an assumption (Q6) |
| Time horizon | Five dated points: 2027, 2028, 2031, 2033, 2033-42 (R-C29; X-1). Multistage | VRF | Where does risk capacity step down, and does the IPS name each stage? (Q5) |
| Liquidity | None before 2033 (R-C34). $50k on each 1 Jan 2033-42. Facility "after establishing the operating reserve in 2033" (R-C57) | VRF | Lump sum on 1 Jan 2033, or committed then and drawn in stages? (Q25) |
| Legal/regulatory | Taxes and Taiwan law out of scope (R-C97). CFA Code applies (R-W29). No-contact rule (R-W16) | VRF/VP | Should the IPS say in one clause what it deliberately does not cover? (Q8) |
| Unique circumstances | Public credibility is part of her income (BS-03). Self-employed, lumpy income (B8a #1). USD promise for a Taiwan project (R-AN10). Educator, "Professor of Comics" (VP). Data/PM background (VP) | Mixed | How does each one change a number or a sentence? (Q1, Q13, Q17, Q18) |

**What this frame says about the plan (INT):** her *need* is small and can be bought. Her *want* (the facility) is
where risk earns anything. Her *credibility* is the binding constraint after 2031. So the most "hers" plan fits one
sentence (the team's own words, later): buy the need, take measured risk only for the want, and never announce what is
not yet bought.

---

## 3. Questions (25), with reasoning

Format for each: question · anchor · hypothesis (a GUESS; evidence and status) · what would change and where ·
deliverables · domain · seed.

### A. What she is buying, and the return objective

**Q1. What "job" is Laura hiring an asset-management firm to do: grow her money, or let her make promises she never
has to walk back?**
- Anchors: R-C8 ("the investment strategy that Laura ultimately chooses"), R-C66 ("If Laura promises more than she can
  ultimately contribute, she could damage her credibility"), R-S25 ("presents recommendations that can earn her
  confidence").
- Hypothesis (guess): the second.
  - Her 2028 money comes from "publishing advances, speaking engagements, licensing" (R-C27, VRF). All of that depends
    on her reputation (BS-03).
  - B2b found (VP) that Wharton replaced "would win him/her over as a client" with "earn her confidence".
  - A product manager thinks in "jobs to be done": what the customer is really trying to get done (INT; a standard
    product idea, not a case fact).
- What changes (sentence):
  - The central idea of the 50-word pitch (R-I17) and the first line of the IPS (R-I9) would name her promise, not
    the portfolio.
  - The FR opening would be written from the 2031 conversation backwards.
  - This also answers the North Star directly.
- Deliverables: IPS, FR · Domain: D6 · Seed: 1.

**Q2. What is Laura's required return, and should the IPS say that her needs can be met at below today's Treasury
yield?**
- Anchors: R-C26, R-C27, R-C45, F-601 (cash flows); R-I2 (the IPS "outlines an investor’s financial goals, risk
  tolerance").
- Hypothesis (guess, with numbers): yes. The internal rate of return (IRR: the single yearly return that turns the
  deposits into the withdrawals) on the case flows is:
  - 1.05% for the payments alone;
  - 2.10% with a $50k facility in 2033;
  - 3.15% with $100k;
  - 4.20% with $150k;
  - 5.25% with $200k;
  - 6.28% with $250k.

  Derived by scipy root-find; inputs VRF. The Treasury curve is 4.98-5.54% from 5 to 20 years (F-001, VP).
  So the payments plus roughly $190-200k of facility money are reachable at close to Treasury yields. Equity risk
  pays only for amounts above that.
- What changes:
  - (number) A "required return" line in the FR client picture.
  - (sentence) The IPS risk/return sentence could say that growth is for the facility, not for the promise.
  - It also gives the team a principled top end for the 2031 range.
- Deliverables: IPS, FR · Domain: D3 · Seed: 26.

**Q3. Should every recommendation be shown against a simple "control": the same plan with an all-Treasury sleeve?
And is the lift from 60% sleeve equity worth its cost at the 5th percentile to Laura?**
- Anchors: R-C38 ("an appropriate balance between pursuing growth and protecting the capital required for her
  goals"); F-407; brief section 9 (sleeve equity 50/60/70% open).
- New evidence:
  - The verified model (F-407) only compares 50/60/70% equity.
  - Adding 0% and 30% (scratch run, ASM inputs as in the model) gives the table in the summary: 60% vs 0% adds +$9k
    at p50 and +$55k at p95, and costs -$22k at p5 (bond 4.0%); about the same at bond 5.0%.
  - 30% equity costs almost nothing at p5 (-$5k) and adds +$5k at p50 and +$19k at p95.
  - Caveat: the "all-bond" sleeve here is an intermediate-Treasury fund with price risk. A sleeve of matched
    zero-coupon bonds would be even narrower.
- Hypothesis (guess):
  - A former A/B tester (resume: "A/B testing", "Experimented and shipped 10 features", VP) will look first for the
    control and the lift.
  - The honest case for 60% is the upside tail for the facility, not the median. The team may find 30-40% the better
    "thoughtful risk".
- What changes:
  - (decision) The sleeve equity weight; it also changes the WInS mix now (brief section 9 mirror).
  - (number) FR scenario table.
  - (sentence) The IPS names the trade-off as "upside for the facility vs a lower floor".
- Deliverables: WInS-now, IPS, FR · Domain: D3 · Seed: 26.

### B. Risk willingness vs risk ability, horizons, constraints

**Q4. How should the IPS state Laura's risk tolerance, given that we must infer it without ever speaking to her? And
which evidence would change our inference?**
- Anchors: R-C37/R-C38; R-AN17 (the case gives no risk-tolerance number); R-W16 (no contact); R-I2.
- Hypothesis (guess):
  - Willingness is **high for her career and the residency**. It is **moderate for this money**: her career leaps
    were taken only after a secured base (B8a #4-#5, VP). The words "Although … balance" point the same way.
  - Ability is **zero for the payments**, **high for the sleeve until 2031**, and **low for whatever she announces in
    2031**.
  - A statistics graduate will expect the inference to be *stated as an inference*: "we infer X from Y; if Z, we
    would change it". It should not be asserted as a trait.
- What changes:
  - (sentence) One IPS clause splitting willingness from ability.
  - (decision) The sleeve equity weight (with Q3).
  - (sentence) FR: "what would change our view" (e.g. if the 2028 deposit is late).
- Deliverables: IPS, FR · Domain: D6 · Seed: 18.

**Q5. Which time-horizon stages should the IPS name, and at which boundary does her ability to take risk step
down?**
- Anchors: R-S24 ("disciplined planning across Laura's changing time horizons and cash-flow needs"); R-C29; R-I12
  ("How will the portfolio’s asset allocation and composition change as future funding needs approach").
- Hypothesis (guess): five stages:
  1. 2026 to Jan 2027: rate risk before the money arrives (F-111, F-112).
  2. 2027-2030: the sleeve grows; ability is high.
  3. 2031-2033: the announced floor is bought; ability is close to nil on that part.
  4. 2033-2042: the reserve pays itself out; no trading needed ("if at all", R-AN27).
  5. The flexibility pool after 2033: its horizon is the project's needs.

  Most teams will write "long-term" once (INT).
- What changes: (sentence) the IPS's "planned changes" clause; (decision) the share of the sleeve locked in 2031,
  which brief section 9 lists as open.
- Deliverables: IPS, FR · Domain: D8 · Seed: null.

**Q6. Is this portfolio all of Laura's investable wealth, or one goal-dedicated pool? What should the team assume and
say?**
- Anchor: R-C33 ("Laura’s living expenses and short-term financial needs will be covered by income and financial
  resources outside the portfolio").
- Hypothesis (guess): one dedicated pool.
  - The case says outside "financial resources" exist but gives no size.
  - The honest move is to assume nothing about their size. Treat this pool's risk capacity on its own terms, and say
    so in one clause.
  - Do not use the unknown outside wealth to justify extra risk (INT). The case is fiction about a real person
    (R-W4), so her real finances must not be guessed.
- What changes: (sentence) an IPS assumption clause; (decision) it rules out arguments like "she can afford losses
  because she has other money".
- Deliverables: IPS, FR · Domain: D8 · Seed: null.

**Q7. Should the IPS state one primary goal plus explicit guardrails (limits that are never breached), in plain
words? For example: maximise the responsible facility contribution, subject to (1) all ten payments bought and (2) no
2031 announcement above what is already bought.**
- Anchors: R-I10 ("What principles will guide your investment decisions?"); R-I28; R-C71 ("The proposed range must
  also protect the portfolio’s ability to fund the ten-year operating commitment").
- Hypothesis (guess): yes.
  - "Primary metric plus guardrail metrics" is how product teams set up experiments (INT; general product practice).
  - Laura's Twitter team was "Abuse & Safety" (VP), a function built around not causing harm while shipping growth.
  - The structure is short enough for the 500 words, and a judge can read it as the CFA "objectives and
    constraints".
- What changes: (sentence) the order and shape of the IPS principles paragraph; (sentence) each TN reflection says
  which goal or guardrail the trade serves.
- Deliverables: TN, IPS · Domain: D9 · Seed: null.

**Q8. Should the IPS include one "non-goals" clause, i.e. what the plan deliberately does not try to do?**
- Examples of non-goals: beat the market, time interest rates, fund beyond 2042, estimate the facility cost.
- Anchors: R-C49 (after 2042 out of scope); R-C95 (no facility cost estimate); R-C97 (taxes, Taiwan law); R-I23 (focus
  on "strategy and decision-making framework … rather than describing individual investments").
- Hypothesis (guess): yes, but in about 15 words.
  - Product specs routinely list non-goals (INT).
  - It shows the reader that scope was a choice, not an oversight.
  - It also protects against a rival's "but what about X" framing.
  - Risk: wasted words. Test it against the 500-word budget (R-AN39).
- What changes: (sentence) the IPS; (sentence) the FR scope line.
- Deliverables: IPS, FR · Domain: D10 · Seed: null.

### C. What evidence she trusts, and what she rejects on sight

**Q9. Should every key number in the Final Report carry an evidence grade: observed market price, historical
estimate, or assumption, with an honest quality word? This is how her own "Match Quality" column works.**
- Anchors: R-C56 ("identify the assumptions supporting their recommendation"); R-C85; R-S26 ("uses reasonable
  assumptions and projections"); R-S28 ("uses data effectively to support conclusions").
- Evidence (VP, lauragao.com/rewriting-herstory):
  - "The [unfinished] results are below."
  - A table with a final "Match Quality" column graded "Good", "Unsure" or "Bad".
  - The dance study defines terms from the data source: "For the purposes of this study, I used Spotify's
    definitions and values for different song attributes."
  - The dance study ends with limits: "Further probing of other song metrics' effects on danceability would provide
    deeper analysis."
- Hypothesis (guess): yes.
  - The team already uses status labels internally (brief section 3). A client-facing version is 3 grades in one
    column of the FR assumptions table.
  - It matches her own habit, and it is the opposite of false precision.
- What changes: (sentence and table) the FR assumptions table format; (sentence) the IPS can say in words that
  "certainty" rests on prices you can observe, not on a forecast.
- Deliverables: FR · Domain: D9 · Seed: 18.

**Q10. What rounding rule should the deliverables use, so that no number looks more precise than the model behind
it?**
- Anchors: R-AN32 (statistics degree); R-C69 (confidence statement); F-405, F-407, brief section 8.6.
- Evidence (derived):
  - Changing the equity assumption from 6.7% to 5.0% moves the lock-early median from $207k to $200k (F-405).
  - Changing the sleeve-bond assumption from 4% to 5% moves it from $207k to $210k (Q3 table).
  - The Monte Carlo sampling error is tiny by comparison.
  - So model uncertainty at the median is about ±$7-10k.
- Hypothesis (guess):
  - Dollar outcomes to the nearest $10k, and ranges as round figures.
  - Probabilities to the nearest 5 points, with the model named.
  - Treasury-priced amounts, such as the ladder cost ($292,264, bought at market), may keep more digits: they are
    prices, not forecasts.
  - A statistician rejects "$207,413" on sight (INT, from SH-04).
- What changes: (number) every figure in the FR, the 2031 range and the co-sponsor draft; (sentence) one line in the
  FR stating the rounding rule.
- Deliverables: TN, FR · Domain: D3 · Seed: 18.

**Q11. What can six weeks of WInS results honestly show a statistics graduate? Should the Trading Notes say that the
P&L is noise, and point to a metric that is not?**
- Anchors:
  - R-T11 ("The focus should be on the quality of your reasoning and the intended role of each decision").
  - R-W81 ("Gains and losses generated in WInS do not determine how your team is evaluated").
  - R-T20 ("supported, tested, or refined").
- Evidence (derived, ASM: JPM equity volatility 16.47%, 2026 realised volatility of the ladder value 7.24%, F-014):
  - One standard deviation of a 6-week return is about **5.6%** for equities.
  - It is about **2.5% (~$7.6k on $300k)** for a 65/35 mix.
  - It is about **$7.2k** for the ladder value alone.
  - So a WInS gain or loss smaller than about $15k (two standard deviations) is indistinguishable from chance.
- Hypothesis (guess):
  - Yes. The testable claim in six weeks is **hedge tracking**: does the Treasury holding move with the present value
    of the ten payments (about $289 per 0.01%, F-103)? B4a Q20 proposes that log.
  - My addition is the reason a statistics-trained client would demand it: it is the only WInS claim with a
    signal-to-noise ratio above 1.
- What changes:
  - (sentence) TN reflections avoid "the trade worked" language.
  - (decision) Start the tracking log with the first trade (WInS-now).
- Deliverables: WInS-now, TN, FR · Domain: D3 · Seed: 18.

**Q12. Should the Final Report attribute the WInS result to its causes (rate moves on the Treasury part, equity moves,
commissions, cash drag), the way she once attributed 1.5M unexplained ad transactions?**
- Anchors: R-C90 ("This evaluates how that strategy was implemented"); R-S26 ("integrates quantitative and qualitative
  analysis"); Guide p.5 "reasoning, assumptions, and tradeoffs" (R-new, VP per B7a/B7b).
- Evidence: resume, "Investigated cause of 1.5M cases of transactions from unattributed ads using SQL, R, and Excel"
  and "Created weekly reports for leadership of findings and data visualizations using Tableau" (VP).
- Hypothesis (guess):
  - Yes. A four-bar attribution chart is one of the few FR charts that "uses data effectively" without claiming
    skill from noise.
  - It also shows that the Treasury loss or gain was offset by the liability's change, as designed.
  - Data needed: daily holdings, trade log, the Treasury curve on the start and end dates, and commission count
    ($25/$10, F-607).
- What changes:
  - (decision) Record daily or weekly snapshots now; WInS closes Nov 6 (R-W58).
  - (FR chart) The FR chart list.
- Deliverables: WInS-now, FR · Domain: D3 · Seed: null.

**Q13. Should her "wrong-way" income risk be shown as named scenarios (late, smaller, both) rather than as a modelled
correlation between her income and markets? No data exists to estimate that correlation.**
- Anchors: R-C27 ("She will contribute an additional $150,000 at the beginning of 2028"); R-AN35 (the case says
  "will"); brief section 9 (wrong-way risk open); B8a Q08-Q09 (late books; political and budget exposure).
- Hypothesis (guess): scenarios.
  - Any correlation number for one person's creative income against the S&P 500 would be invented.
  - A statistician would see through a made-up coefficient (INT).
  - Three labelled team scenarios beyond the case are honest and simple:
    - deposit 12 months late;
    - deposit $75k;
    - rates fall before January 2027 *and* the deposit is late (the joint tail, brief section 9).
- What changes: (decision) D3's modelling approach; (number) the FR stress table; (sentence) the assumption on "timing
  of cash flows" (R-C85).
- Deliverables: FR · Domain: D3 · Seed: 16.

### D. How she would test and explain the plan to others

**Q14. Before submitting, should the team "usability-test" the co-sponsor paragraph and the IPS's core rules with real
non-finance readers, and report what changed, as she did with nurses and doctors?**
- Non-finance readers here means, for example, school staff or parents. This involves no contact with Laura.
- Anchors: R-C72 ("draft part of Laura’s fundraising materials"); R-S28 ("clearly and credibly to prospective
  co-sponsors"); R-S27 ("reflects meaningfully on the team's growth and response to challenges").
- Evidence (resume, VP):
  - "Collaborated with researchers at National Institute of Health for usability tests with nurses and doctors".
  - "Beta-tested MVP with 300K+ users".
  - Her editorial list includes NPR explainer comics, e.g. "There's a way to get healthier without even going to a
    gym. It's called NEAT" (VP).
  - She wrote "Recruiting for Tech for Non-Technical Students" (VP, title only).
- Hypothesis (guess):
  - Yes. A test takes about 30 minutes: 5 readers restate the range and the confidence in their own words, and the
    team counts the errors.
  - It is cheap, it is real process evidence for the Articulation criterion, and it catches jargon.
  - Few teams will do it (INT).
- What changes: (decision) add a test step before Dec 4; (sentence) the Articulation section reports the result, e.g.
  "3 of 5 misread X, so we changed Y".
- Deliverables: FR · Domain: D9 · Seed: 32.

**Q15. Who exactly will read her 2031 fundraising material? Should the draft be built for 2-3 named reader types
(her own habit of writing for personas) rather than for "co-sponsors" in general?**
- Anchors: R-C64 ("A meaningful personal contribution may signal that the residency is financially viable"); R-C44
  (co-sponsors, grants, collaborators); R-AN21.
- Evidence (VP, lauragao.com/philly-happy-hours): "we set out to build a guide for various types of students to
  select the best happy hour for any occasion", with sections such as "For the student drowning in debt". Her record
  of running Pride in Panels with a public-library partner, free and with mini-grants, is in B8a #14-#18 and B8b.
- Hypothesis (guess): three reader types are enough:
  1. A public or cultural grant-maker, who needs proof of viability and a floor.
  2. An institutional partner (e.g. a university or arts organisation), who needs to know the operations are funded.
  3. A private donor, who needs to see the size of her own commitment ("skin in the game").

  One paragraph can serve all three if it answers each one's first question. This is D5's research to confirm.
- What changes: (sentence) the content checklist for the FR fundraising draft.
- Deliverables: FR · Domain: D5 · Seed: null.

**Q16. Should the Final Report include one simple visual of the promise that she, an illustrator, could redraw for
co-sponsors? For example: ten blocks for the ten funded years, plus a bar for the facility range.**
- Anchors: R-C72; R-S28 ("uses data effectively to support conclusions"); R-I55 (no graphics in the IPS, so the FR
  only).
- Evidence: she made "Interactive visualizations of career pathways" and uses Tableau (VP). "The Wuhan I Know" began
  as a short comic. Her view that comics "marry imagery with the power of words" is in B8a #25 (VP).
- Hypothesis (guess):
  - Yes, one visual only.
  - It must be simple enough to redraw by hand, and it must carry the core claim: bought vs estimated.
  - A decorative infographic would fail her "No more gimmicks." test (B8a #21).
- What changes: (FR chart) spec: data = ten payment dates marked "bought", plus the 2031 floor and the p50/p95 band
  from D3.
- Deliverables: FR · Domain: D9 · Seed: 32.

**Q17. Should the co-sponsor wording be written so it survives translation into Mandarin? That means no idioms, "US$"
every time, an NT$ reference with its date, and "confidence" defined in words.**
- Anchors: R-AN10 (no currency named); R-C68 ("the dollar range"); BS-04 ("dollar" is ambiguous in Taiwan).
- Evidence: her resume lists "Languages: Mandarin Chinese" (VP). The residency is in Taiwan (R-C39). B8a #33 records
  her own care over translation choices in *Messy Roots* (VP).
- Hypothesis (guess):
  - Yes. Taiwanese partners may read her material in Chinese.
  - Idioms such as "skin in the game", "upside" or "downside" translate badly.
  - The cost is near zero.
  - The team should not translate anything itself; it only writes translatable English.
- What changes: (sentence) the FR fundraising draft style checklist.
- Deliverables: FR · Domain: D9 · Seed: null.

**Q18. How should the team describe (a) the growth sleeve's AI and mega-cap concentration and (b) its own AI use,
given that she has built ML and AI products and is not a known AI critic?**
- Anchors: R-W46 ("how you use it must be recorded in your Works Cited pages"); R-S24 ("uses appropriate
  diversification"); seed 20.
- Evidence (VP): "Growth ML (2018-2019)" at Twitter; her studio client "Retainit, AI-powered online learning
  software". I could not search for her public statements on generative AI in art (search budget used up). That is
  an open lead (section 5).
- Hypothesis (guess):
  - Describe index concentration as a plain diversification fact, with the share from the fund's own holdings page.
    It should not be a values judgement made on her behalf.
  - Describe AI use exactly and modestly: what AI did, and what the students did.
  - Someone who shipped ML features knows how AI output fails. Overclaiming is the risk, not using AI.
- What changes: (sentence) the FR concentration sentence and the Works Cited AI statement; (decision) no "AI
  avoidance" tilt without her stated preference.
- Deliverables: FR · Domain: D2 · Seed: null.

### E. Simplicity, failure and the evaluation of alternatives

**Q19. What is the smallest set of rules (a "minimum viable plan") that still passes all five case tests? Can each
extra rule show a measurable improvement?**
- Anchors: R-C79 to R-C84 (the five tests); R-I30 ("clear, cohesive, and well-supported"); R-I23; design principle
  (brief).
- Hypothesis (guess):
  - Three rules may be enough:
    1. Buy the ten payments when the money arrives (with the rates-fall variant).
    2. The sleeve keeps a fixed mix, rebalanced by a band.
    3. In 2031, announce only what is bought, plus a stated upside.
  - Everything else (TWD quote, Taiwan tilt, glide paths) must show a lift in a number, or go.
  - This is her "Always start small" (B8a #26) and last year's lesson in one test.
- What changes: (decision) the rule list in the IPS; (number) a "lift" line per extra rule in the FR.
- Deliverables: IPS, FR · Domain: D8 · Seed: null.

**Q20. Does the plan show her, in one table, how each goal "fails softly": the worst realistic outcome for the
payments, the 2031 announcement, the facility and flexibility, and who would notice?**
- Anchors: R-C70 ("how favorable and unfavorable market outcomes could affect the amount she can provide"); R-C86;
  R-S26 ("under varying market outcomes").
- Evidence:
  - Her "Anti-Resume Project" to "normalize failure" and "33 job rejections" (B8a 2f, VP/reporter).
  - Her Twitter safety work (VP).
  - Brief section 8.8: under lock-early a missing 2028 deposit leaves the payments safe and the facility ~$7-11k
    ("correct failure mode").
- Hypothesis (guess):
  - Yes, a four-row table.
  - Payments: fail only if the U.S. Treasury defaults.
  - Announcement: fails only if she announces more than is bought.
  - Facility: gets smaller, but never negative.
  - Flexibility: absorbs overruns.
  - Someone who normalises failure will trust a plan that shows its failures calmly, more than one that hides them
    (INT).
- What changes: (FR table); (sentence) a bad-case line in the co-sponsor draft.
- Deliverables: FR · Domain: D6 · Seed: null.

**Q21. Which rejected alternatives should the Final Report show, with their numbers, as the team's "experiment log"?
Candidates: growth-first, rolling short, equity-heavy, all-Treasury.**
- Anchors: R-S27 ("clearly explains the team's research and decision-making process"); Guide p.5 "reasoning,
  assumptions, and tradeoffs" (R-new, VP per B7a); R-T9 ("aligned with, tested, or refined").
- Evidence: brief section 8.1-8.2 (growth-first misses 3-8%, tiering +$20k per -100bp); Q3 table (all-Treasury
  control).
- Hypothesis (guess):
  - Show three rejected arms with one number each, and why they were rejected.
  - A product person reads a decision without its alternatives as untested (INT).
  - It is also the most honest evidence for the Articulation criterion.
- What changes: (FR section and chart) a small "options we tested" table; (sentence) one TN reflection can reference
  the test.
- Deliverables: TN, FR · Domain: D7 · Seed: null.

**Q22. Which of Laura's own verified ideas can the strategy echo honestly? And which proposed echoes fail verification
or turn into tokenism?**
- Anchors: R-C21 (pull quote, unattributed per B8a/B8b); R-C10 (themes of her work); brief tokenism rule; seeds 15 and
  17.
- Evidence (VP):
  - **Fails:** "fall safely" and "Queen of Balance". Her book page says the heroine is a "top rock climber" who
    "suffers an injury that sidelines her". "Falling" means falling in love. "Queen of Balance" is publisher copy
    about a fictional character.
  - **Fails as her words:** the pull quote (B8a Q01, B8b).
  - **Passes as a factual parallel, used sparingly:**
    - "If what you want doesn’t exist, create it yourself" (B8a #11, PQ). Parallel: no iBonds-style fund exists for
      the 2038-2042 payments (F-206), so those rungs are built from individual Treasuries.
    - Her published "Match Quality" grades. Parallel: our evidence grades (Q9).
    - Her "floor-first" career leap (B8a #4-#5).
- Hypothesis (guess):
  - Echo at most one of her ideas in the FR, in the team's own words, with a citation.
  - Never echo in the IPS pitch, where it would read as flattery.
- What changes: (sentence) FR narrative; removes any book-title metaphor from all deliverables.
- Deliverables: IPS, FR · Domain: D6 · Seed: 15.

**Q23. When she compares firms, would she trust one that says plainly which parts of the plan need almost no
management (the bought payments) and which parts it actively manages (the sleeve)? And that charges or discloses fees
accordingly?**
- Anchors: R-C26 ("with an asset management firm"); R-W29 (CFA Code; F.4.d fee disclosure via SH-25); BS-01 (no fee
  modelled); B4a Q5 (fees on the reserve eat the $7.7k headroom).
- Hypothesis (guess):
  - Yes. Saying "this part runs itself" is a costly honesty signal: the firm gives up a fee argument.
  - It also matches her CFPB internship and her financial-literacy teaching (B8a 2f, VP).
- What changes:
  - (sentence) An IPS clause on which parts are "set and hold" and which are "managed".
  - (number) The fee assumption in FR projections (A3: -$17k median at 0.5%/yr).
- Deliverables: IPS, FR · Domain: D8 · Seed: 1.

**Q24. How many sentences in the deliverables should describe Laura as a person (as opposed to her goals)? What may
each rest on, so that she feels understood rather than analysed?**
- Anchors: R-S25 ("demonstrates a thoughtful understanding of the client"); R-W4 ("While the client is real, the
  financial scenario is developed specifically for the competition"); privacy and tokenism rules (brief section 4).
- Hypothesis (guess):
  - Very few: perhaps 2-3 in the FR and 1 in the IPS.
  - Each one must link a *verified professional fact or the case's words* to a *decision*, for example "because her
    2028 money depends on reputation, we …".
  - Psychological readings of her identity, or claims about her real plans, would feel like being analysed. They
    also break the brief's rules (INT).
  - Understanding shows in how well the plan fits her, not in how much it says about her.
- What changes: (sentence) a checklist rule for all three deliverables: each Laura sentence = fact + source + decision.
- Deliverables: TN, IPS, FR · Domain: D10 · Seed: 32.

**Q25. Should the facility contribution be framed as an amount committed in 2033 and paid as the project needs it,
rather than a lump sum paid on 1 January 2033? Her own institutions scale in stages.**
- Anchors:
  - R-C57 ("After establishing the operating reserve in 2033, Laura must decide how much of the remaining portfolio
    she can responsibly contribute").
  - R-C58 ("committing all remaining assets could limit her financial flexibility as the project develops").
  - R-C84.
- Evidence: Pride in Panels grew in stages, e.g. "We definitely hope to offer more as the festival grows" (B8a #16,
  VP). B8b summary item 7.
- Hypothesis (guess):
  - A committed-but-drawn contribution keeps the undrawn part invested in short Treasuries. That preserves
    flexibility at little cost, fits her pattern, and stays inside the case, which fixes the *decision* in 2033, not
    the payment date.
  - Risk: it adds a moving part. Use it only if D5 finds that co-sponsors accept staged pledges.
- What changes: (decision) the FR facility recommendation's form; (sentence) the co-sponsor draft's verb ("commits …,
  drawn as construction proceeds").
- Deliverables: FR · Domain: D5 · Seed: null.

---

## 4. Evidence register (new primary reading by B9b; all VP, grep-verified 2026-09-27)

Professional content only. Contact details, hobbies and family-related pages on the same site were read but not
recorded.

| # | Exact text | Source | Date of piece | What it shows (INT) |
|---|---|---|---|---|
| 1 | "Experimented and shipped 10 features that resulted in +4.5M DAU" | https://lauragao.com/s/Laura-Gao-Resume.pdf | undated, current | Experiment-driven decisions |
| 2 | "Product Management: JIRA, Confluence, A/B testing" | same | same | Control-vs-variant thinking |
| 3 | "Growth ML (2018-2019)" | same | same | Hands-on ML product work |
| 4 | "Abuse & Safety (2019-2020)" (as printed: "Abuse & Safety (2019-2020), Growth ML (2018-2019)") | same | same | Harm-limiting guardrails |
| 5 | "Investigated cause of 1.5M cases of transactions from unattributed ads using SQL, R, and Excel" | same | same | Attribution analysis |
| 6 | "Created weekly reports for leadership of findings and data visualizations using Tableau" | same | same | Regular reporting to decision-makers |
| 7 | "Beta-tested MVP with 300K+ users of economics platform, Marginal Revolution University" | same | same | Tests with real users; exposure to economics teaching |
| 8 | "Collaborated with researchers at National Institute of Health for usability tests with nurses and doctors" | same | same | Usability testing with non-specialists |
| 9 | "AI-powered online learning software" | same | same | Worked for an AI-product client |
| 10 | "Languages: Mandarin Chinese" | same | same | Can work with Taiwanese partners in Mandarin |
| 11 | "Bachelor of Science in Statistics and Information Decisions, Concentration in Product Design" (read on page; B8a also records it) | same | same | Statistics plus design |
| 12 | "The [unfinished] results are below." and the column "Match Quality" (rows "Good", "Unsure", "Bad") | https://lauragao.com/rewriting-herstory | undated (student-era project) | Publishes uncertain results with quality grades |
| 13 | "Using text analysis to explore powerful female counterparts of well-known men in history." | same | same | Data used to reframe a story |
| 14 | "For the purposes of this study, I used Spotify's definitions and values for different song attributes." | https://lauragao.com/the-evolution-of-dance-music | undated | Defines terms from the source |
| 15 | "However, tempo and speechiness display a diminishing returns relationship." | same | same | Comfortable with "sweet spot" findings |
| 16 | "Further probing of other song metrics' effects on danceability would provide deeper analysis." | same | same | States limits and next steps |
| 17 | "we set out to build a guide for various types of students to select the best happy hour for any occasion" and "For the student drowning in debt" | https://lauragao.com/philly-happy-hours | undated | Designs for reader personas |
| 18 | "Only restaurants with Happy Hours on Thursday, Friday or Saturday have been included in this dataset." | same | same | Discloses data scope |
| 19 | "shapes the next generation of creators as a Professor of Comics at California College of the Arts" | https://lauragao.com/hey | current | Educator who assesses student work |
| 20 | "Once dubbed the Queen of Balance as her school’s top rock climber, Kirby Tan suffers an injury that sidelines her for the rest of the season." | https://lauragao.com/kirbys-lessons-for-falling-in-love | current (book 2025) | Publisher copy about a fictional character; corrects seed 17's premise |

Also seen (VP, titles only): "Recruiting for Tech for Non-Technical Students" and "There's a way to get healthier
without even going to a gym. It's called NEAT" (NPR), both on https://lauragao.com/editorial. The same page describes
The Sign.al: "Our bold interactive projects aim to help students discover their passions and live deliberately."

---

## 5. Leads for the specialists

- **D3 (quant):**
  - Rebuild the control-arm runs (Q3) as `research/insight_v1/scripts/` code, with a docstring.
    - Inputs: `strategy_mc.simulate("L", eq_w=w)` for w in {0, 0.3, 0.6}.
    - Sleeve-bond compound 4.0% (JPM) and 5.0% (ASM).
    - Add a zero-coupon-matched sleeve variant, where the sleeve buys 2033 STRIPS for the facility.
  - Compute the required-return table (Q2).
  - Compute the 6-week noise figures (Q11) with IEF/TLT realised volatility, if it can be fetched from iShares.
  - Build the attribution template (Q12).
  - Build scenario rows, not a correlation (Q13).
- **D6 (client psychology):**
  - Write the willingness-vs-ability paragraph spec (Q4) using B8a #1-#10 plus section 2 here.
  - Build the fail-softly table (Q20).
  - Check that each Laura sentence meets "fact + source + decision" (Q24).
- **D9 (communication):**
  - Usability-test protocol (Q14): 5 non-finance readers, restate-in-own-words scoring.
  - Translation-safe style list (Q17).
  - One-visual spec (Q16).
  - Evidence-grade column (Q9).
- **D5 (co-sponsors):**
  - Reader types for Taiwan arts funding (Q15).
  - Whether funders accept staged founder pledges (Q25).
  - Taiwan's arts-funding bodies were not researched here; their sites (e.g. the Ministry of Culture) were refused
    earlier in this run (brief section 2: artres.moc.gov.tw 403).
- **D2:** the concentration share for the chosen broad fund, from the issuer's holdings page (Q18).
- **D13 (quotes):** re-check rows 1-20 before any are quoted in a deliverable. The resume and the data pages are
  undated. Cite them as "lauragao.com, accessed [date]".
- **Open leads I could not reach (search budget exhausted):**
  - Laura's public statements, if any, on generative AI in illustration.
  - Whether she took part in 2020's #PublishingPaidMe advance-transparency campaign (would show how she talks about
    money in public).
  - The Sign.al "Deconstructing Penn Pathways" page: https://thesign.al/pages/deconstructing-penn-pathways/ (B8b: empty
    page).
  - The Medium post "Your Freshman Summer, Demystified" (medium.com returned 403 to B8b).

---

## 6. Sources (all accessed 2026-09-27)

| Source | URL | Status |
|---|---|---|
| Laura Gao resume (PDF) | https://lauragao.com/s/Laura-Gao-Resume.pdf | VP (grep) |
| Visual Data Stories index | https://lauragao.com/data-journalism | VP |
| Rewriting Herstory | https://lauragao.com/rewriting-herstory | VP |
| The Evolution of Dance Music | https://lauragao.com/the-evolution-of-dance-music | VP |
| Philly Happy Hours, Deconstructed | https://lauragao.com/philly-happy-hours | VP |
| Projects | https://lauragao.com/projects | VP |
| Editorial | https://lauragao.com/editorial | VP |
| About ("Hey") | https://lauragao.com/hey | VP |
| Kirby's Lessons for Falling (In Love) page | https://lauragao.com/kirbys-lessons-for-falling-in-love | VP (publisher copy) |
| Case, IPS guide, TN guide, SMApply page | `competition/official/2026_27/` | VRF |
| Verified model | `research/verified_2026-09-27/strategy_mc.py` | VRF (script); my variants ASM |
| B8a, B8b, B2b, B4a, B4b, B7a, B7b | `research/insight_v1/phase_B/` | Cited for their findings; their status labels apply |
| Phase A registers | `research/insight_v1/phase_A/` | VRF |

---

## What this teaches

A professional adviser does not start with a portfolio. The first step is a client picture:
- what return she *needs* (here only about 1% a year for the payments);
- how much risk she is *willing* to take, and how much she *can* take (two different things);
- when she needs money, and what makes her situation unusual.

Reading how a client works also tells you what she will trust. Laura grades her own results "Good/Unsure/Bad", tests
products with real users and compares every change against a control. So the plan most likely to earn her confidence:
- shows the simple alternative (all Treasuries) next to ours, with the difference in plain numbers;
- labels what is known, estimated or assumed;
- rounds to the precision the model deserves;
- says calmly how each goal would fail.

Understanding a client shows in how well the plan fits her, not in how much it says about her.
