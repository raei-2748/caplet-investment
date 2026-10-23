# Notes & Discussions

> Exported read-only from Google Docs on 2026-10-14. Source: https://docs.google.com/document/d/1i5JeazVh7MLcI87bbMbVKCTm48Q-KS08NtG0dCyAde4
> Text kept verbatim (formatting simplified to Markdown); personal details removed where marked.

## Tabs

- STRATEGY (`t.gg8yyv2czxcp`)
  - I'll go through the phase files on the branch and… (`t.81gut8nf145d`)
  - Strategy Log (`t.h8usmzbedai`)
- Client (`t.0`)
- Equity Research (`t.5rsnkiubp52m`)
- Money (`t.1f957s6mm4dg`)
- Evaluation Criteria (`t.rkcne6np3gzc`)
- Example IPS (`t.oovh78agsdzm`)


## Tab: STRATEGY

_Tab ID: `t.gg8yyv2czxcp`_

The Competition

Research Summary: [https://claude.ai/artifact/KSHbLEgcM3iyF3sQu8pHT9#d1cf3f9b-6fc2](https://claude.ai/artifact/KSHbLEgcM3iyF3sQu8pHT9#d1cf3f9b-6fc2)

| Due (U.S. time) | Document | What it is |
|---|---|---|
| Oct 9 | Team roster | The list of team members |
| Oct 23 | Trading Notes | 3 trades you made in a practice account, each with a short note and a reflection of 100 words or fewer |
| Nov 6 | Investment Policy Statement (IPS) | A 50-word pitch plus a 500-word statement of your plan. After this, the plan is locked |
| Dec 4 | Final Report | The full report; instructions come out Nov 9 |

Who is Laura?

- **Laura Gao** graduated from Wharton in 2018 in Statistics and Information Decisions Management.
- She worked in tech as a product manager, then left to become an author and illustrator.
- She wrote *The Wuhan I Know* (2020) and the graphic memoir *Messy Roots*. She's a bestselling author, entrepreneur and educator.
- She was born in Wuhan, China, and raised in Texas.
- **Her dream:** starting in 2033, she'll open a **creative residency in Taiwan**, a place where artists, writers and designers come to work together.
- **Her attitude to risk:** the case says she's "willing to take thoughtful risks" but wants "an appropriate balance between pursuing growth and protecting the capital required for her goals." In short, she's fine with some risk, but not with the money she really needs.

#### Laura’s Money Problem

**Money coming in**

- **Jan 2027:** $300,000
- **Jan 2028:** $150,000, from her book advances, speaking and licensing. So it depends on her career going OK.
- Nothing else comes in or goes out before 2033. Her living costs are paid from somewhere else.
**Money going out**

- **Ten payments of $50,000**, one at the start of each year from 2033 to 2042, to run the residency. That's $500,000 in total.
- These payments must be covered **"with a high degree of certainty"**, and only by her portfolio. She can't count on donors for them.
- After those are covered, she wants to give **as much as she responsibly can toward the building**. She also wants to keep some money spare in case plans change.

| Year | What happens |
|---|---|
| 2027 | $300k arrives |
| 2028 | $150k arrives |
| 2031 | She starts asking co-sponsors (partners, donors) to help fund the building. She must tell them a range, e.g. "I'll put in between $X and $Y," and how confident she is. If she promises too much and can't deliver, she damages her reputation. |
| 2033 | She sets aside an operating reserve, the money for the ten payments. The first payment is made, and she makes her building contribution |
| 2033–2042 | **One $50k payment each year** |

#### The Big Idea

Right now the US bonds are high (about 5%), this makes the bonds cheap. As of 25 Sep 2026, **Buying all ten $50,000 payments costs about $294,000**, which is almost exactly her first $300,000.

Use the first $300k to buy the ten payments in January 2027. Then the promise is done, and no market crash can break it.

The idea came from our AI council run on 27 September.

- **Catch 1:** it's very tight, with only about $5,600 to spare. If rates fall before January 2027, the ten bonds cost more than $300k. The model says that happens about 1 time in 3. Then some payments have to wait for the 2028 money.
- **Catch 2:** the payments are fixed in U.S. dollars, but costs in Taiwan rise over time. So $50k buys less in 2042 than it does today.

#### The Big Prompt

- **Main question:** "Why would Laura choose our firm's plan over 6,000 others?"
- **Aim:** make the plan so solid that no judge, donor, statistician or rival team can poke a hole in it, and make it feel like *hers*, not generic.
- **Lesson from last year:** keep it simple, follow every trading rule, and put the client first.
Total: 50-60 Agents.

| **Stage** | **Plain-English job** |
|---|---|
| **A: Foundations** | Read every official document, list every rule and number, check the facts |
| **B: Questions** | 16 agents from different angles (odd details in the case, Laura's life and words, the 2026 economy, donors, judges, what professionals would do) write hundreds of questions |
| **C: Filter** | Sceptic agents throw out questions that don't matter, are already answered, or are too complicated |
| **D: Research** | Specialist agents answer the surviving questions with sources and computer models. Auditor agents then check their work |
| **E: Attack the plan** | An agent redesigns the plan. Then it's attacked by a pretend judge, a pretend Laura and a pretend rival team. A "pre-mortem" asks: "It's January and we failed. Why?" A chief agent writes the final plan |
| **F: Completeness** | Ask what was missed and repeat until nothing new appears |

- The run took **27–28 September** and used **about 90 agents**, more than planned.
- **During the run you narrowed the scope:**
  - Specific funds may be named.
  - Semifinals only.
  - Only the **Trading Notes and the IPS**, nothing for the Final Report.
- Because of cut 3, you got **6 practical files** instead of the 12 planned.
- **Stage F (completeness) never ran.** A final error-check ran instead, which found 19 problems and fixed 18.
- In numbers: **472 questions → 48 survived** the filter → 12 specialists and 5 auditors → 6 pretend attackers → a final plan.
- **The results:**
  - Taking more stock-market risk barely raises the middle outcome this year. It mostly makes the good and bad outcomes further apart.
  - The pretend **rival team's** plan beat your own designer agent's plan, so it became the final recommendation.
  - In a blind contest, **three pretend Lauras** each read six anonymous plans, and all three ranked yours first. All three also said it looks **too timid**, with only about 9% in stocks.
  - The pretend judge said the ideas are Top-50 quality, but the writing was too dense (about 55 ideas in 500 words).

#### Final Recommended Plan

| **When** | **What happens** |
|---|---|
| **Jan 2027** | $300k buys the **ten payment bonds**. If there isn't quite enough, buy the latest ones first and let 2028 money finish the job |
| **Jan 2028** | $150k first finishes any unbought payment. Then it buys **one bond that pays back $150k just before 2033**, the **"floor"**. The rest, about $40k, goes into **one world stock fund** and is left alone *(Dream)* |
| **2031** | No trading. Laura tells partners: "At least $150k, which I already own, and up to $150k plus half of what my stock fund is worth today" |
| **2033** | The ten bonds become the operating reserve. The building gets the floor plus half the stock fund, never more than she announced. She keeps the rest |

- The research has found that all sensible plans’ differences are quite small. Mediums are within a spread of 10 percent, and more stocks just widen the range of outcomes.
- So no clever portfolio exists here that beats the others by a lot. A plan that *looks* exciting (themes, optimisers, 75% stocks) is exactly what the three simulated Lauras ranked last. And "over-complex for the insight" was your own lesson from last year.

**Laura's biggest return doesn't come from the stock market. It comes from co-sponsors.**

- Work through the numbers. The stock fund is about $40k. Even if it grows well for five years, it adds maybe $20–30k to the building. That's the entire upside markets can give her.
- Now look at what she's asking co-sponsors for: money for a building. The stakeholder research found that donors notoriously avoid funding **operations**. They like buildings, but worry about who pays the bills afterward. Laura's plan walks into her 2031 meetings with:
  - all ten years of operations already paid for, and
  - a $150k building floor she already owns.
This also answers the one criticism all three simulated Lauras made ("where's the leap?"):

- **The leap is the residency itself.** Her career and income already carry her personal risk.
- **The portfolio's job is to make the leap believable to other people.**
That's not vanilla. It's a thesis about *her* that a generic team won't have. One caution: there's no data on how much more co-sponsors give because of this. Present it as the logic behind the plan, not as a number.

#### Most Impressive Insights


## Tab: STRATEGY > I'll go through the phase files on the branch and…

_Tab ID: `t.81gut8nf145d`_

I'll go through the phase files on the branch and pull out the sharpest findings, not just the headline plan.

Most of the good material is buried in the Phase A–D research files, not the final recommendation. The final plan compressed it into rules and banned words, which is why it reads vanilla. Here are the strongest findings, grouped for your notes.

*Most Impressive Points from Claude*

---

#### **A. Wharton designed this case on purpose, and the research reverse-engineered it**

**1. This year's case is the opposite of last year's.**

- Last year (Connor Barwin): grow $500k to $1.5M, about 11.6% a year, with a values focus.
- This year: a fixed promise that must be *certain*. No return target, no values language.
- Wharton also changed the machinery, and every change points the same way:
  - Treasury bonds are now allowed.
  - WInS cash was cut to exactly Laura's $300k.
  - Trading freezes at the IPS deadline.
  - "Clever pitch" became "earn her confidence".
- *Why it matters:* most of the ~2,300 teams will copy last year's habits: stock picks, "9% return" targets, ESG themes. That's the wrong template this year.
**2. Wharton's wording moved from persuasion to trust.** Older pages (still hidden in Wharton's website code) said teams "shape the *winning* strategy" and should build a "*compelling and clever pitch*". This year that's gone. The judging criterion changed from "would win him/her over" to "**earn her confidence**". So the answer to "why would Laura choose us" is *the plan she can trust*, not the cleverest one.

**3. The case words were counted.**

| **Word** | **Hits in earlier cases** | **Hits this year** |
|---|---|---|
| "certainty" | 0 | 6 |
| "co-sponsor" | 0 | 9 |
| "credibility" | 0 | 3 |
| "stock" | 2–4 per case | 0 |

This is also the first case with **no hobbies or personal-life hooks**. Past teams turned hobbies into stock picks (for example, "Nike, because she loves sports"). This year, tailoring has to come through her cash flows and how she thinks.

**4. The question itself was asked before, in a zero-rate world.**

- The 2021-22 case (Nichole Jordan) also had ten years of payments: a scholarship "for at least 10 years", asking "should she keep $50,000 in cash?"
- Then, the 10-year yield was 1.48%, so buying ten payments cost about 95% of their face value. Today it's about 58%.
- Wharton brought back an old question at a moment when interest rates changed the answer.
**5. The timing of the case document is suspicious.** The case PDF was created on **10 Sep 2026**. That's the first day in 2026 the ten-payment ladder cost dropped under $300k; it was above $300k on 173 of 185 trading days. Interpretation: the designers meant the first deposit to buy the promise and the second to fund the building. **Her money has two jobs, one per deposit.**

**6. Committed spending grew from half the client's money to more than all of it.** Jordan's payments were 50% of her money. Laura's $500k of payments is **111%** of her $450k. This is the hardest "promise versus money" case Wharton has set.

---

#### **B. The numbers that change how you think about the plan**

**7. The promise needs almost no return.**

- With both deposits, a return of just **1.05% a year** pays for all ten payments.
- Payments plus about a $200k building gift need about 5.25%, roughly what Treasuries pay today.
- So growth isn't needed to *meet* her goals. It's optional upside, bought with risk.
**8. Stocks barely pay extra right now.**

- Safe Treasuries lock about **5.2% a year**.
- Expected extra return from stocks: +1.5 to +1.8 points a year using J.P. Morgan's forecasts. **About 0** using Vanguard's. **About 0** using the stock market's own earnings yield.
- *Why it matters:* this is the honest reason the plan is conservative. Risk isn't *paid* this year, and "thoughtful risk" means risk that is paid.
**9. The "should she take risk" question has an exact price.**

- Locking all her spare money in Treasuries gives about **$204k in 2033**, almost for sure.
- The 60%-stock version gives a middle outcome of about $207–210k, and ends *below* $204k in **42–46% of cases**.
- In other words, stocks add about $3–6k in the middle and cost about $42–45k in bad years. A former A/B tester (which Laura is) would ask exactly this "lift over the control" question.
**10. Her second deposit matters more than the stock market.** Every $1 of the 2028 deposit adds about **$1.31** to the 2033 building money. Halving the deposit moves the result by $98k, which is almost the entire market range. So "her savings buy the promise; her earnings fund the building" is literally how the numbers work.

**11. By 2031, 97% of the uncertainty is gone.** The wide ranges everyone quotes ([equation]273k) are a 2026 view. By the time Laura actually speaks to partners in 2031, her portfolio is the *least* uncertain part. What's left is the exchange rate and Taiwan building costs. So the range she says can be narrow and honest.

**12. The rates rose for a specific reason.** In 2026 the 10-year yield rose 121bp, and **113bp of that was "real" yield**, the highest since 2008. Almost none was an inflation scare. The ladder became affordable because long-term lenders are being paid unusually well. That's a clean "why now" no other team will have.

**13. By a UK regulator's standard, the promise is already "mature".** UK pension rules call a promise "mature" when its duration hits 10 years, and then expect it to be at least 90% hedged. Laura's ten payments are *already* about 10 years. That's an outside, model-free argument for locking now.

- Inspirations from Australian superannuation? (narrative)
- Growth sleeve to achieve the future dream (50K is the bare minimum, rest **the Dream** for Laura Gao to achieve big future goals)

---

#### **C. The co-sponsor research (the most original part)*****

**14. Funders count only money that's really committed.**

- Kresge Foundation counts only "written pledges or cash".
- U.S. nonprofit accounting says "an intention to give" is *not* a promise.
- **So only the bought floor of Laura's range counts as real money in any funder's books.** The rest is just information.
**15. Co-sponsors may write her bottom number into their contracts,** as in "we pay if the founder contributes at least $X". That's another outside reason the bottom must be bought, not forecast.

**16. The experiments say: announce a firm lead gift, and don't offer to match.** Field studies (Huck & Rasul; Rondeau & List) find that announcing a lead gift raises donations, while matching doesn't help and can crowd donors out. This tells Laura exactly how to structure her 2031 message.

**17. Pre-funded operations answer the building funder's biggest fear.** One of Kresge's first questions to any building applicant is how the project will sustain itself after the campaign. Laura's ten pre-funded years answer that before anyone asks. This is the thesis I suggested last time. The research found it but never made it the headline.

**18. How you state uncertainty changes whether people trust you.**

- People read "likely" as about 50% unless you add the number, and this holds across 17 languages (relevant for Taiwanese readers).
- A result just outside a range is judged "wrong" even when the range was loose.
- Keeping a promise earns as much credit as beating it, while breaking it is punished. **So the bottom of the range is her only real promise, and a high top earns her nothing.**

---

#### **D. Laura herself**

**19. Her background is more financial than the case says.** *At Wharton she interned as a* *trader (Belvedere Trading)**, at the Consumer Financial Protection Bureau (CFPB), and as a data analyst at Amazon.* She also taught financial literacy to high-schoolers. Don't write to her as if she's a novice.

**20.** **She thinks like an experimenter.** Her CV includes A/B testing, "shipped 10 features", and cause attribution. Her own data project labels its results "[unfinished]" and grades each one "Good / Unsure / Bad". *So she'll trust a plan that grades its own numbers* (price, estimate or assumption) and distrust one that presents a model output as fact.

**21. The only market crash in her career was her best year.** In 2020 stocks fell 34%, her comic went viral, and HarperCollins bought two books at auction. *Her income is driven by publishing contracts and politics (corporate diversity budget cuts, book bans), not the stock market.* So "a crash also shrinks her deposit" is mostly wrong. The real risk to the deposit is contract timing.

- Is it implying that there are not many stocks in the portfolio?
- Income sources cancel out the stock?
  - Uneven income sources
- *Loop up: Barbell strategy (Generic compared to the other teams?)*
**22. The case's pull quote may not be hers.** "The only person who needs to believe in something is yourself" didn't appear in any of 25 sources checked. Cite it as the case's words, never as Laura's. A team that writes "As Laura says…" is making a factual error.

**23. A trap the research caught itself in.** An *early agent claimed Laura "only leapt once the book deal secured a floor", which made a perfect story for this plan. Verification found it came from a reporter's sentence, not her own words, so it was* ***dropped****.* Treat it as a warning: the most tempting story about a client is often the unverified one.

---

#### **E. Process findings that protect you**

**24. Two official Wharton documents were missing.** An agent found a 5-page Competition Guide and an infographic that weren't in your files. They contain the clearest statements of what judges want, for example: judges want "the reasoning, assumptions, and tradeoffs behind those decisions."

**25. Who actually judges:** **Wharton undergraduates students first**, then asset managers from **Aberdeen**. Last year's finale included a credit (bond) investment manager. So a bond professional may read your Treasury claims, and words like "matched" or "guaranteed" will get caught.

- Barbell strategy (generic?)
- 
**26. A modelling flaw a statistician would spot.** The original model priced the bonds at about 5.08% but let spare bond money earn only 4%. That made the all-bond option look about $9k worse than it really is. It was found and corrected.

---

#### **What I'd take from this**

The strongest, most defensible story isn't about the portfolio. It's this chain:

**Wharton built a certainty case, not a growth case → this year risk barely pays and the promise needs almost no return → so lock the promise and let spare money grow → which makes Laura the rare founder whose operations are already funded and whose floor is already owned → which is exactly what building funders look for.**

Items 1–3 (case design), 7–9 (the economics) and 14–17 (co-sponsors) are the ones most teams won't have. They're what makes the plan *yours* rather than a textbook bond ladder.

Models we use

- Final report / IPS = simple textbook models e.g., monte carlo, modern portfolio theory, company metrics (sharpe, D/E, etc) (interpretible ones)
- Personally → Eric’s HAR model or some random ass quant model to see if we are right (don’t show on the report)


## Tab: STRATEGY > Strategy Log

_Tab ID: `t.h8usmzbedai`_

29th September

**Smaller-floor test (AI research notes, Claude Code, 29 Sep 2026: not for submission)**

**Question:** Several reviewers said our plan "reads as timid." Would buying a smaller floor in 2028 and putting more in stocks give Laura a better deal?

**Method:** This used the same model as our main research: 200,000 simulated paths using J.P. Morgan's 2026 return forecasts, plus a lower Vanguard-like forecast and every 6-year window of U.S. market history since 1928. Only the size of the 2028 floor changes; the rest goes into the world stock fund. The ten $50k payments are bought in 2027 in every version, so the payments are never at risk. Script: keel/library/insight_v1/scripts/F1_floor_variants.py.

**Results (money for the building plus flexibility in 2033):**

| **2028 floor** | **Bad case (5th percentile)** | **Middle** | **Good case (95th percentile)** | **Stock share, 2028–32** | **Worst history window** |
|---|---|---|---|---|---|
| $150k (our plan) | $182k | $207k | $250k | 9% | $169k |
| $125k | $173k | $209k | $274k | 13% | $153k |
| $100k | $163k | $212k | $297k | 18% | $137k |
| $75k | $154k | $214k | $321k | 22% | $121k |
| $50k | $144k | $217k | $345k | 26% | $105k |
| All Treasuries (for comparison) | $202k | $202k | $202k | 0% | $202k |

**What it means:**

- Each $25k less floor adds only about $2–3k to the middle outcome, but costs about $9–10k in a bad market and about $15k in the worst historical case.
- With Vanguard's lower forecast, the middle outcome doesn't rise at all. Only the risk increases.
- The stock fund trails plain Treasuries in about 4 out of 10 simulated futures, whatever the floor size.
- A smaller floor weakens Laura's 2031 message. With $150k she already owns 86% of the likely gift when she speaks to co-sponsors; with $100k it's 68%.
**AI recommendation:** keep the $150k floor. Answer "timid" with the price of certainty instead of adding stock. The plan already takes full stock risk with money no one relies on, and the residency itself is the leap. **Team vote needed (D2/D6).**

**Limits:** These are model results, not forecasts. The model assumes independent yearly returns and has thinner crash tails than history, which is why the history windows are included. History uses the S&P 500 as a stand-in for world stocks. The 50/50 split of the stock fund between the gift and Laura's flexibility was not changed.

- Wharton never showed the second deposit (150K later), which means we need to reconsider what the 300K mean in order to make judges easier to follow.
- **Current plan (ii)R:** WInS shows Laura's whole position *after* the second deposit (ladder about 66%, floor about 25%, stocks about 9%), scaled down to $300k. That's why it includes 8.7% in VT.
- **Book L:** WInS shows exactly Laura's first $300k, which is all bonds. The stock fund doesn't appear, because the money that buys it (the 2028 deposit) never arrives in WInS.

I priced Laura's ten payments on every Treasury yield curve since 2000 (6,688 trading days), each time with the payments the same distance ahead as they are today:

| **When** | **Cost of the ten $50k payments** |
|---|---|
| August 2020 (the most expensive day) | **$470,249**, more than all $450k Laura will ever deposit |
| 2021 (median) | $423,973 |
| 2025 (median) | $317,840 |
| **28 Sep 2026** | **$289,119, the cheapest since May 2002** |

Only 11% of days since 2000 would $300k have bought all ten payments, and no day between 2008 and today would have. **Right now, Laura's first deposit can buy every promise outright. For most of the last 25 years it couldn't have.** That's the story: *high interest rates made certainty cheap, and the plan buys it while it's cheap.*

It also explains every other choice. Why no stocks in the first $300k? Because this rare chance buys all ten promises. Why not wait? Because the chance can disappear (the model gives about a 1 in 4 chance the ladder costs more than $300k by January).

The idea: **buy certainty while it's cheap, grow only what's left, and promise only what's already owned.** The team puts this in its own words. Each rule answers one of Laura's three goals:


## Tab: Client

_Tab ID: `t.0`_

Client Portrait - Laura Gao

The main point: this isn't really a stock-picking case. It's a liability-matching problem with a growth portfolio attached to it.

- Client Values - What do they value? What do they want from the investments?
- Similar clients - big companies must have done rigorous research and processes for similar clients like her. Wharton must have picked her as the client of the competition with a specific purpose.
- Based on last year’s experience, we **should not** just stick to some obvious cues, such as… she likes industry XYZ. They are too generic. We must deeply understand the client to guide our investment decisions. This is extremely important.

**Why Wharton picked Laura Gao？**

Laura isn't the usual client who just wants to grow her money. Four things about her make the case what it is:

- **She has a Statistics degree from Wharton (2018).** Look at what the brief asks you to do: define a "high degree of certainty," say how you evaluated it, and state how confident you are in a range. Those are statistics questions. A client with her training can tell a real confidence interval from a made-up one. Teams that write "our Monte Carlo shows 95% success" without defining the model will lose points.
- **She's a storyteller, and she needs co-sponsors to believe her.** Her quote says the only person who needs to believe is yourself. The case turns that around: in 2031, other people have to believe her numbers. That's why there's a fundraising-draft deliverable. You're being tested on explaining finance to people who aren't in finance.
- **Her income is lumpy.** Advances, speaking and licensing come in unevenly. The case deliberately uses a fixed stream of payments and fixed contribution dates so you have to think about cash-flow timing, not just returns.
- **She's young and her goal is a project, not retirement.** Most high school teams build a generic growth portfolio. Here the money has a specific job: $500k of fixed payments starting in 2033. The case is built to punish the generic approach.
**1. The facility contribution swings much more than the portfolio does.** The reserve takes about two-thirds of the portfolio. That leaves a surplus of about $204k. If the portfolio drops 20% to about $501k, the surplus falls to about $79k, which is a 61% drop. A team that gives a range of "plus or minus 15%" around the contribution will promise too much. Overpromising to co-sponsors is exactly what the brief warns against.

**2. Interest rates are a second risk hiding in the reserve.** L2033L_{2033} L2033​ depends on bond yields in 2033. If yields fall to 3%, the reserve costs about $439k instead of $422k. That shrinks the surplus even if stocks do nothing. Teams that stay in stocks until 2033 and only then buy the reserve carry both stock risk and rate risk without realising it. You can avoid this by locking in the reserve early. A ladder of zero-coupon Treasuries maturing 2033–2042 matches the fixed dollar payments exactly. That also answers the "high degree of certainty" question: the funding is close to certain by construction, not a probability from a model.

This also gives you a striking result. The reserve's value in 2027 is L2033/1.046≈$333kL_{2033}/1.04^6 \approx \$333\text{k} L2033​/1.046≈$333k, which is more than her entire first contribution. So Laura has very little room for risk, and a guaranteed floor for the facility contribution is only about $140k. Everything above that depends on taking risk. Showing that you understand this is what makes a strategy look thought through rather than guessed.

**3. The 2031 promise becomes a second commitment, and your allocation has to protect it.** In 2031 Laura knows what her portfolio is worth; only two years of uncertainty are left. So your range should be a rule based on her 2031 value, not a forecast from 2026. And once she tells co-sponsors a range, the bottom of that range is effectively something she owes. The strategy should shift into safer assets after 2031 so the promise can't be broken. A team whose portfolio in 2031–33 doesn't match what it told co-sponsors has a strategy that contradicts itself. That's the kind of inconsistency across the three deliverables that evaluators look for.

**Two more things to consider**

- The residency is in Taiwan, but the payments are in US dollars. Currency risk isn't excluded the way taxes and legal issues are. Mentioning it in one careful paragraph shows maturity.
- The case asks you to consider inflation for facility costs. The operating payments are fixed in dollars, but construction costs rise with prices. So the real value of her contribution falls over time even when the dollar amount looks fine.
**How do professionals handle clients like Laura？**

- **Protect the promise first, then grow the rest.** This is how pension funds work (it's called liability-driven investing), and private banks use a similar split into a "safe" bucket and a "growth" bucket. For Laura, the $500k commitment is covered by Treasury bonds that mature in the years each payment is due; everything else is invested for the residency facility.
- **Bond yields are high right now, which changes the maths.** The 10-year Treasury is at about 5.1%, the highest since late 2023. At that rate, locking in all ten $50k payments would cost about **$297k at the start of 2027**, almost exactly her first deposit. That leaves the team with three options:
  - Lock everything in early.
  - Lock in part now and raise it over time using set rules.
  - Wait until 2033.
- I'd lean toward option 2. It's also the easiest to explain as a disciplined framework.
- **"High degree of certainty" should mean close to 100%.** Planners usually accept an 80–90% chance of success, but only for goals the client can adjust. Laura's payments are fixed and she can't use outside money, so a pension-style standard fits better. Treasuries held to maturity also don't need inflation protection, because her payments aren't inflation-adjusted.
- **In 2031, promise a floor, then protect it.** A well-known fundraising experiment found that raising the "seed" gift from 10% to 67% of the goal led to nearly six times more giving from others. So Laura should give co-sponsors a conservative floor. Then move that floor into bonds maturing in 2033, so a crash between 2031 and 2033 can't break her word.
- **Other points the case asks you to cover:**
  - Laura's 2028 $150k depends on irregular creative income, so it's worth testing what happens if it's late or smaller.
  - Facility costs rise with Taiwan inflation, which is about 1.8–2.2%.
  - The facility will be paid for in Taiwan dollars, so exchange rates affect what her contribution buys.
**More about Laura**

**Where she comes from.** Laura was born in Wuhan and grew up in Texas, so she has lived between two cultures. That tension, not fully belonging to either place, is what her work is about. Her memoir is called *Messy Roots* for that reason. When COVID hit in 2020, Wuhan became a word people used with fear and blame, and anti-Asian racism rose. She answered with a comic, *The Wuhan I Know*, showing her hometown as a real place full of real people. It spread worldwide and became a bestselling book that is now taught in schools. So her career began as a personal response to a painful moment and turned into something much larger.

**How she thinks.** She's not a typical artist. She studied statistics at Wharton, ran a small business while she was there, and worked as a product manager in tech. She approaches creative work like an entrepreneur: she spots an opportunity, takes a considered risk, and builds something. Her quote in the case, "The only person who needs to believe in something is yourself," tells you she trusts her own judgment and doesn't wait for permission. She's also numerate. She'll read your assumptions and notice if they're weak, so she's not a client you can impress with jargon.

**Her relationship with money.** Her income is uneven: book advances, speaking fees and licensing deals, not a steady salary. For someone like her, money comes in waves. The portfolio isn't what pays her bills, since the case says her living costs are covered elsewhere. **This portfolio is money for a dream, not money for survival.** That changes how she'll feel about risk. Losing some of the upside would disappoint her, but it wouldn't harm her day-to-day life.

**What the residency means to her.** Read the residency as the next chapter of her story. Her whole career has been about belonging, and now she wants to build a physical place where artists, writers, educators and entrepreneurs can belong, live and work together. It's in Taiwan, which is culturally Chinese-speaking but not mainland China. That fits someone whose identity sits between places. (That last point is my interpretation. The case doesn't explain why she chose Taiwan.) It's also a project that has to survive over time, which is why she committed to ten years of operating support rather than a one-off gift.

**What she's afraid of.** The case hints at two fears, and they're different:

- **Breaking a promise.** Once the residency opens, artists and staff will depend on those $50,000 payments. If the money runs out in year six, real people are let down and the project collapses. That's why she wants "a high degree of certainty" for that part.
- **Losing credibility.** Her reputation is her business. Her books, talks and partnerships all depend on people trusting her voice. If she tells co-sponsors in 2031 "I'll put in $200k" and then only manages $120k, the damage isn't only financial. It hurts the trust her whole career is built on. That's why she wants a range she can stand behind, not a single number.
**What she wants from you.** She isn't looking for the highest return. She wants advisors who understand that she's building something meaningful, who will protect what must be protected, let the rest grow, and explain it honestly. Remember she's Wharton-trained and a storyteller, so she'll value a plan that is both rigorous and easy to explain to other people.

**Her in one sentence:** Laura is a creative entrepreneur who turned a personal story about belonging into a career, and she now wants to build a place of belonging for others. She needs a plan that keeps her promise to the people who will depend on it, protects the credibility her work rests on, and still gives her dream room to grow.

**WHY HER???**

### **Laura Gao: What She Embodies, and Why Wharton Chose Her**

**Companion to the client profile | Wharton Global HS Investment Competition 2026–27 | 27 Sep 2026**

**How to read this.** Sections 1–2 describe what Laura stands for, using her own public record. Section 3 lays out what past competition clients show. Section 4 is **our interpretation** of what choosing her signals. Wharton has not published a rationale, so treat Section 4 as analysis, not fact. Section 5 turns all of it into strategy.

---

#### **0. Bottom line**

Laura Gao embodies **the non-linear, values-led, multi-income creative professional**: someone trained in quantitative business who chose authenticity and community over a conventional path, and who now builds institutions for people like her.

Past clients show a clear trend. Clients have moved from people with personal wealth goals to people funding **community infrastructure over many years under uncertainty**. Laura's rubric ("facility contribution", "co-sponsors", "residency goals", "changing time horizons") puts her squarely in that trend, with one new difficulty: **her own income is the least stable of any recent client.**

The test this year is not "pick good stocks". It is:

*Can you build a portfolio that reliably funds something meaningful for a client whose life is deliberately unconventional, and explain its uncertainty honestly to other people who might put money in?*

---

#### **1. The movements and values she embodies**

##### **1.1 The portfolio-career / creator-economy professional**

- **Path:** Wharton → Amazon, a trading firm and the CFPB as an intern → Twitter PM → full-time author-illustrator, freelance designer, professor and festival organiser.
- **What it represents:** The 2020s shift from one employer and one salary to **several income streams built on personal IP and reputation**. She even wrote in 2018 that she admired a classmate who supported himself from his own brand and merchandise.
- **Why it matters financially:** Income is lumpy, correlated within one sector, and hard to forecast. This is the core risk-capacity problem for her portfolio.

##### **1.2 The revolt against elite pre-professionalism**

- At Wharton she nearly transferred out. She felt pressure to become the "ideal Whartonite" when she loved building apps and art, not Excel models.
- Her response was to build alternatives: **The Sign.al** (unconventional career stories), a satirical card game about Penn culture that opened conversations on mental health and hyper-competition, and coverage in a student "anti-resume" project on normalising failure.
- **Her maxim:** *"If what you want doesn't exist, create it yourself."*
- **What it represents:** The wider Gen-Z / late-millennial critique of finance-and-consulting funnels at elite schools, and a push to redefine success.

##### **1.3 Asian-American diaspora storytelling and belonging**

- "The Wuhan I Know" (March 2020) was a direct response to COVID-era anti-Asian racism. It became *Messy Roots*.
- She calls the book a love letter to her hometown and to young readers searching for somewhere that feels like home. Its message: identity is messy and that is fine.
- **Lineage:** the Asian-American graphic memoir canon (Gene Luen Yang's *American Born Chinese* is the standard comparison), and the post-2020 AAPI visibility movement.
- **Tension she lives in:** pride in a Chinese city and heritage alongside life as an American immigrant, during years of US–China hostility.

##### **1.4 Queer DIY and community institution-building**

- Co-founded **Pride in Panels**, San Francisco's queer comics festival. It is free for artists and visitors, run with the public library, drew 2,000+ people in 2024, and grew to 125+ exhibitors in 2026.
- Comes from the **zine and indie-comics tradition** of publishing without gatekeepers (the Silver Sprocket circle in the Mission).
- She frames the festival as showing publicly that marginalised creators are not afraid to stand together.
- **What it represents:** Mutual aid and community infrastructure as a response to a hostile climate (US book challenges, arts funding cuts).

##### **1.5 The hybrid "art × data × product" mind**

- Statistics degree, SQL/R/Tableau, A/B testing at Twitter, a design-prototyping course she founded, a "Visual Data Stories" portfolio (e.g., a project using data to pair famous men in history with overlooked women).
- **What it represents:** The designer-technologist-storyteller. She will judge a report on **both** analytical honesty and narrative quality.

##### **1.6 Her personal philosophy in one line**

**Embrace the mess, fall safely, and build the place you wish existed.** Supporting threads:

- *No limits:* credits her grandmother, who taught her multiplication with rice.
- *Falling well:* her second book is structured as lessons on falling (from rock climbing) that also apply to life.
- *Authenticity over approval:* the turning point in *Messy Roots* is refusing to let others judge her identity.
- *Humour as armour:* self-deprecating, playful public voice.

---

#### **2. Culture and comparable figures**

| **Circle** | **Examples** | **What they share with her** |
|---|---|---|
| Asian-American graphic memoir | Gene Luen Yang; Malaka Gharib (*I Was Their American Dream*, a blurber) | Turning diaspora identity into widely read, school-adopted books |
| Queer comics (SF / national) | Justin Hall (*No Straight Lines*, co-organiser), Maia Kobabe (*Gender Queer*), Lee Lai (*Stone Fruit*) | DIY publishing, community festivals, frequent targets of book challenges |
| Mission-driven Penn peers | Kayvon Asemani (rapper, self-funded through his own brand; she named him her most admired classmate) | Independence, turning personal hardship into public work |
| Tech-to-creator switchers | The wider cohort of PMs, engineers and designers who left Big Tech for independent creative work after 2020 | Savings from tech years, irregular creative income, strong values |

**Events that define her world (2020–2026):**

- COVID-era anti-Asian hate, the trigger for her public voice.
- The Twitter acquisition (2022) and upheaval at her former employer.
- US book-challenge wave, heavily targeting LGBTQ+ YA and graphic novels.
- **Generative AI and illustration.** A structural threat to freelance illustration and design income across the industry. *Her personal stance is not on public record; don't assume it.*
- Arts-education consolidation: **CCA acquired by Vanderbilt**, completing 2027, with uncertainty over which programmes survive.
- US–China decoupling.

---

#### **3. The client pattern: 2021–2026**

| **Year** | **Client** | **Background** | **Case shape** |
|---|---|---|---|
| 2021–22 | Nichole Jordan WG'08 | SVP at Via (transit tech), San Francisco | Two personal financial goals, long + mid-term |
| 2022–23 | Peter Wang Hjemdahl W'19 | Co-founder of rePurpose Global (plastic action) | Personal goals; retirement explicitly already covered |
| 2023–24 | Hilary Ash W'13 | LA28 Olympics venues executive; volleyball | Goal-driven; judges rewarded tying passions to strategy |
| 2024–25 | Ladi Ayoola WG'22 | Nigerian-born, Visa, co-founder of Plugtent | **Phased community hub in Abuja**: housing by 2030, youth centre by 2040, one year of operating costs |
| 2025–26 | Connor Barwin WG'23 | Ex-NFL, founder of Make the World Better | **Community spaces and facilities construction**, $500k virtual cash, growth target to 2036 |
| **2026–27** | **Laura Gao W'18** | **Immigrant, queer author-illustrator, professor, festival organiser** | **Facility contribution + co-sponsors + residency goals + changing horizons** |

##### **Trends**

- **From personal wealth to community capital.** Three clients in a row now fund physical, community-facing infrastructure on a timeline. The portfolio is a funding engine for a mission.
- **Moving further from finance.** Corporate exec → social entrepreneur → Olympics → Visa + startup → NFL / foundation → **full-time artist**. Laura is the furthest yet from traditional finance.
- **Immigrant and diaspora stories.** Ayoola (Nigeria) and now Gao (China) bring cross-border identity and heritage into the case.
- **More complex liabilities.** Phased dates (Ayoola) → construction plus ongoing programmes (Barwin) → **shared funding with co-sponsors, where credibility under uncertainty is scored** (Gao).
- **Unstable client income is new.** Earlier clients had steady jobs or wealth. Laura's income comes from books, contract teaching and freelance work. This is the first case where **human-capital risk is central**.

---

#### **4. What choosing her signals (our interpretation)**

**Signal 1: "Business" includes creative careers.** Wharton's youth program has recently run features on business and creativity, and Wharton Magazine's 2026 alumni authors event centred on authenticity. Choosing an artist tells ~6,000+ teams worldwide that a Wharton degree can lead to a comics studio, and that such a life still needs serious financial planning. Wharton's own summary of the competition's theme: growth can come through many paths.

**Signal 2: A deliberately harder client.** Textbook portfolio construction assumes a known salary and savings rate. Laura breaks that assumption. The rubric's language (funding reliability, financial flexibility under different market outcomes, communicating uncertainty to co-sponsors) says Wharton wants **risk management and honesty**, not return-chasing.

**Signal 3: Accountability to others.** Past cases asked teams to satisfy one client. This one adds **prospective co-sponsors**. That means probability of funding, downside scenarios and clear disclosure, which is closer to how endowments and foundations raise money together.

**Signal 4: Values without tokenism.** The case requires "a thoughtful understanding of the client" across identity, heritage and community. The trap is either ignoring her values or turning her identity into a stock-picking gimmick. Wharton is testing the judgment in between.

**Signal 5: A client the competitors can relate to.** She writes YA graphic novels, so **her readers are the competitors' age**. She is about 30, the youngest client in recent years, with a public record students can research. Expect many teams to theme their reports on her books. That makes it more important that your theme carries analysis.

**Signal 6: Picking up the 2026 environment.** Wharton won't say this, but her life sits on several live risks: AI disruption of creative work, arts funding and consolidation, book challenges, US–China tension, Bay Area costs. Teams that name these as **risks to her income and to the facility**, and hedge them, will stand out.

---

#### **5. How to turn this into strategy**

##### **5.1 A possible thesis frame**

*"Strong foundations for messy roots."* The portfolio is the stable base that lets an unconventional life, and the institution she's building, keep going. It echoes her book without being a gimmick.

##### **5.2 Structure**

- **Treat the facility contribution as a dated liability.** Match it with safe, short-duration assets as the date approaches (glide path). Show a **probability of full funding**, not just an expected return.
- **Match buckets to her "changing time horizons":** near-term liquidity (income gaps, facility tranches), medium-term flexibility, long-term growth.
- **Put a larger cash buffer in the IPS** because her income is irregular.

##### **5.3 Hedge her human capital**

- She is effectively over-exposed to **publishing, education, media and the Bay Area**. Underweight these; don't "invest in what she knows".
- **The AI question (a real dilemma to present, not solve for her):** her industry's income is exposed to generative AI, so owning AI beneficiaries is a financial hedge. But many illustrators object to AI trained on artists' work. Show the trade-off and propose a way through: e.g., broad index exposure rather than concentrated AI bets, or asking her preference. That shows the "thoughtful understanding" the rubric rewards.

##### **5.4 Separate the engine from the mission**

- **Her mission is the facility.** The portfolio's job is to fund it reliably.
- Offer values alignment as **screens plus a clear explanation**, not a thematic concentrated bet. Optionally, a small, clearly labelled values-aligned sleeve.

##### **5.5 China / heritage**

Keep a small, deliberate EM/China allocation with geopolitical risk stated. Neither exclusion nor sentimental overweight.

##### **5.6 Writing for her and the co-sponsors**

- Visual, honest, human. Charts of outcome ranges. A one-page "what could go wrong and what we'd do" section.
- Avoid finance-bro tone and jargon. She left that world on purpose.

---

#### **6. Ways to misread her**

| **Misreading** | **Why it's wrong** |
|---|---|
| "She's an artist, so she doesn't get finance" | Statistics degree, trading and CFPB internships, data analyst, PM who ran A/B tests. She'll spot weak maths. |
| "Put LGBTQ/Asian-themed ETFs in and call it tailored" | Tokenism. Tailoring means her risk capacity, cash flows and goals. |
| "She's a risk-taker, so go aggressive" | Career risk-taking lowers portfolio risk capacity. |
| "The facility must be a comics centre" | Plausible from her public life, but **confirm from the case PDF**. The same goes for "residency" (an artist-residency programme vs where she lives). |

---

#### **Sources**

- [Wharton Global Youth: competition archive (past clients)](https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/)
- [Case study 2024–25: Ladi Ayoola](https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/)
- [Case study 2022–23: Peter Wang Hjemdahl](https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2022-2023/)
- [Case study 2021–22: Nichole Jordan](https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/)
- [2026 finalists: Connor Barwin's case focus](https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/)
- [2026 semifinalists: 6,300+ teams, $500k virtual cash](https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/)
- [Harvard-Westlake Chronicle: Barwin case goals](https://hwchronicle.com/112806/news/students-compete-in-yearly-wharton-stock-competition/)
- [2024 Global Finale / Hilary Ash](https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/)
- [2026–27 deliverables and evaluation criteria](https://wghsinvcomp.smapply.us/res/p/deliverables/)
- [Wharton Magazine: interview with Laura Gao](https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/)
- [Poets&Quants: 2018 Best & Brightest](https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/)
- [Laura Gao, official bio](https://lauragao.com/hey/)
- [Pulse Spikes profile](https://pulsespikes.org/story/laura-gao)
- [Local News Matters: Pride in Panels 2026](https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/)
- [48 Hills: Pride in Panels and CCA–Vanderbilt](https://48hills.org/2026/02/pride-in-panels-fest-inks-in-queer-comics-brilliance/)
- [Main Street Books: author bio and blurbs](https://mainstreetbooks.indielite.org/book/9780063067806)


## Tab: Equity Research

_Tab ID: `t.5rsnkiubp52m`_

_(empty tab)_


## Tab: Money

_Tab ID: `t.1f957s6mm4dg`_

[image]

So one pot of money has **two jobs**:

- **Job 1, the promise:** pay [equation]500k in total). It has to be near-certain.
- **Job 2, the dream:** give as much as responsibly possible to build the facility in 2033. This amount can go up or down with markets.
**How the ladder works:** we buy ten US Treasury bonds. One matures in 2033, one in 2034, and so on to 2042, each paying about $50,000 when it matures. Each year one "rung" of the ladder pays out and funds that year's payment. Nothing has to be sold, so a market crash in, say, 2036 doesn't matter. The only thing that could break it is the US government defaulting.

[image]


## Tab: Evaluation Criteria

_Tab ID: `t.rkcne6np3gzc`_

#### EVALUATION CRITERIA

Investment Strategy: Presents a clear and creative investment thesis; demonstrates disciplined planning across Laura’s changing time horizons and cash-flow needs; uses appropriate diversification; and maintains consistency with the team’s IPS.  
  
Client Knowledge and Objectives: Tailors the strategy to Laura’s circumstances, priorities, risk considerations, and residency goals; demonstrates a thoughtful understanding of the client; and presents recommendations that can earn her confidence.  
  
Portfolio Analysis: Demonstrates understanding and effective use of investment concepts and tools; integrates quantitative and qualitative analysis; and uses reasonable assumptions and projections to evaluate funding reliability, the facility contribution, and financial flexibility under varying market outcomes.  
  
Articulation of Competition Experience: Demonstrates teamwork, communication, and learning; clearly explains the team’s research and decision-making process; and reflects meaningfully on the team’s growth and response to challenges.  
  
Creativity and Presentation: Presents a compelling, well-organized narrative in an authentic team voice; uses data effectively to support conclusions; demonstrates original thinking and meaningful reflection; and communicates Laura’s potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors.


## Tab: Example IPS

_Tab ID: `t.oovh78agsdzm`_

_(empty tab)_
