# D13c: Voice-of-Laura map (her verified words → values → strategy and communication)

Agent D13c (Voice-of-Laura mapper), insight_v1 run, Phase D. Written 2026-09-27. This is AI-generated research for
Team Caplet. It holds specifications, evidence and checklists. It holds **no text to submit**: the six students write
every deliverable in their own words and record AI use in the Final Report's Works Cited (R-W46). Laura appears here
only through the case and her public professional record. Nothing here suggests contacting her (R-W16).

**The gate for quotes.** In sections 1-4 and 6, a line appears as Laura's words only if D13a marked it
VERIFIED-PRIMARY (`phase_D/D13a_laura_quotes_verified.json`). All 50 D13a ids quoted or cited here were re-checked
verbatim by D13c on fresh copies of their pages (script: `research/insight_v1/scripts/D13c_voice_map_check.py`, 50 of
50 pass).
Everything else (the unattributed pull quote, transcript lines, private lines, reporter sentences, and 8 new lines
D13c found) is kept apart in section 7.

Inputs read in full: the brief (sections 2-4 and 13-15 with care); the case
(`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`); D13a (md and json); Phase B files B8a, B8b, B9a,
B9b and B3b; the current allocation file `wins_now/securities_and_allocation_v0.md` (S3, v1); and the Phase C questions
that touch her voice (M018, M049, M075, M100, M103, M126, M144, M216, M221, M243 and others).

---

## Summary (read this first)

1. **Her words hold two risk ideas, and the plan must honour both.** She leaps: "you should always take the jump
   because you’re always going to regret not doing it" (2021), after naming the cost, a move to "self-employed, with
   unstable income". And, as a student founder, she said letting down "people who were your earliest supporters and
   were the first to believe in you" is worse than letting yourself down (2016). INTERPRETATION: risk she carries
   herself is acceptable, even attractive, to her; risk that lands on people who trusted her is not. That split is the
   honest Laura-rooted reason for "buy the payments first, take risk only with the surplus". Neither "she is cautious"
   nor "she loves risk" fits her words.
2. **Correction to Phase B: "she leapt only after a contract secured her floor" is not in her words.** B8a, B8b, B9a,
   B9b and question M018 built on it. It rests on a reporter's sentence ("So when she got the book deal with
   HarperCollins, she gave Twitter her notice.", Input/Inverse 2022). D13a found, and D13c confirmed on a fresh copy,
   that its "So" follows personal material, not a financial plan. Stop describing "floor-first" as her trait.
3. **The candid clash.** On paper the plan is very cautious. Whole-portfolio equity is about 0-2% in 2027, about 20%
   in 2028-2030 and about 4% after the 2031 floor is bought (DER, B10b script re-run by D13c). A founder whose rule is
   "take the jump" could read that as the opposite of her. The plan can answer this, but only if the deliverables say
   it plainly:
   - the leap is the residency itself;
   - locking the payments costs about $11k at the median and about $200k at the 95th percentile of the 2033 surplus;
   - in return it removes a ~2% chance of not funding all ten payments (~12% if the 2028 deposit halves) (DER, B10b);
   - the growth money should not be set at the minimum just to look safe.
4. **Her working habits set the communication spec.**
   - Habits: a purpose statement before the work; a deadline, "finished or not"; three drafts scrapped; "prove better
     with data"; results labelled "[unfinished]".
   - Spec: purpose first; costs and gaps named; discarded drafts shown; every number graded and rounded; what the
     numbers secure stated before the numbers.
5. **Community.** Her newest words (Feb 2026) are about access: "…Our No. 1 priority is to get as many diverse voices
   and stories in the room as possible". And her festival grew after "the community really supported us". So
   "operations first" reads as hers. The 2031 message can follow the same order: her own part already bought;
   partners invited; more offered as support is proven (her festival phrase was "as the festival grows").
6. **What she would reject on sight:**
   - the case pull quote presented as "Laura said";
   - book-title puns and "falling" metaphors;
   - her identity used as a reason for a holding;
   - a finance-prestige tone;
   - numbers more precise than the model behind them;
   - hidden costs;
   - a one-sided risk story.
7. **"Falling" has no usable line.** Her 2025 book's "falling" is fiction (a climber's fall, and falling in love). The
   only first-person "falling" line (Nerd Daily 2025) sits in an answer about her family, so it is excluded. Seed 17's
   "learning to fall safely" fails.
8. **Guardrails, in short:**
   - Apply the swap test to every Laura sentence.
   - No Laura quotes in the Trading Notes or the IPS (the IPS bans "formal citations", R-I55).
   - At most 1-2 quotes in the Final Report, each dated and in context.
   - Label student-era lines (2016-2018) as such.
   - We hold no verified statement by her about investing, so never write her "investment philosophy".
9. **New for D13a to rule on:** 8 lines verified verbatim but not in D13a's register (section 7d). One corrects Phase
   B: "the Laura Gao I knew loved building apps, not excel models…" is her own first-person answer (Poets&Quants 2018),
   not the nominator's words.
10. **North Star link (INTERPRETATION).** The plan feels like hers if it:
    - makes the leap certain for the people who will rely on it;
    - takes risk only where she alone bears the cost;
    - says its costs and gaps out loud;
    - sounds like a teacher, not a trading desk.

---

## Words used in this file

- **Verified quote (VP):** D13a marked it VERIFIED-PRIMARY (her words, verbatim, meaning kept in context); D13c
  re-checked the wording on a fresh copy of the page on 2026-09-27.
- **VRF:** VERIFIED-REPO-FILE, i.e. wording checked in an official file in this repo (the case, the guides).
- **INTERPRETATION (INT):** D13c's reading of what her words show. Never a fact about her.
- **DER:** derived by a script; its inputs carry their own labels. **ASM:** ASSUMPTION.
- **Ladder:** Treasury bonds that mature on or just before each $50,000 payment date, so each payment is already
  bought. The plan uses zero-coupon Treasuries (STRIPS), which pay one lump sum at maturity.
- **Growth money (the "sleeve"):** money the ten payments do not need. It can take market risk.
- **2031 floor:** an amount bought in a 2-year Treasury in 2031, so it can be promised to co-sponsors without a
  forecast.
- **Percentile (p5, p50, p95):** in a simulation, p5 is the result that only 5% of paths fall below (a bad case), p50
  the middle (median), p95 a good case.
- **Regret rule:** choosing by asking which choice you would regret more later.
- **Price of certainty:** what buying the payments up front gives up in good markets.
- **Tokenism:** using a person's identity as decoration, or as a reason for a choice it does not justify.
- **Student-era:** her words from 2016-2018, when she was a Penn student. Still hers, but older.

---

## 1. Values and decision habits her verified words show (all readings are INTERPRETATION)

Each value has 1-3 verified quotes (exact words, source, date, and what she was answering) and a note on how strong
the evidence is. Case lines are the case's words (VRF), not hers.

### V1. Risk: she leaps toward what she would regret not doing, and names the cost first

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B1b-Q11 | “But I always tell myself, you should always take the jump because you’re always going to regret not doing it.” | Overachiever Magazine, 2021-03-15 | "What pushed you to make the jump?" (tech job to full-time comics) |
| B8b-Q18 | “It’s not an easy thing to say, “let me give up my incredibly cushy, paying job with health insurance to be self-employed, with unstable income.”” | same answer, 2021-03-15 | same |
| B8a-Q32 | “I was a bit hesitant. I was like, I know this is kind of a sensitive topic. I don't know what I'll get from it” | NPR Goats and Soda, 2020-04-04 | deciding to share The Wuhan I Know |

- Reading (INT): her risk rule is regret of *not* acting, applied to meaningful leaps. She says the downside in
  concrete words ("unstable income") and admits hesitation, then acts without knowing the outcome.
- Supporting lines (VP):
  - "I feel like I’ve been jumping almost my whole life." (B8a-Q09, 2021).
  - Her speaking guide lists the audience question "What motivated you to quit a secure job to become an
    artist-writer in the middle of a pandemic?" (B8b-Q04, guide PDF created 2024-03-24). This is a question she
    lists, not a statement, but it shows she presents her story publicly as leaving security.
- No verified line says she waits for a secured floor before leaping (see Summary item 2 and section 3.4).
- Case framing (VRF, R-C37/R-C38, p.2 L69-74): "Although she has been willing to take thoughtful risks throughout her
  entrepreneurial career, she wants her investment team to recommend an appropriate balance between pursuing growth
  and protecting the capital required for her goals."
- Strength: strong for "leaps, with the cost named" (two outlets, 2020-2021). Every one of these was a career or
  public risk that she carried herself; none is about investing.

### V2. Failing people who believed in you is worse than failing yourself

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| D13a-N01 | “It’s actually harder as an entrepreneur because not only are you letting yourself down, but more importantly, you’re also letting other people down — people who were your earliest supporters and were the first to believe in you.” | The Daily Pennsylvanian, 2016-01-28 | "What were some major challenges you've had with Draw Street Journal?" (her student laptop-decal business) |

- Reading (INT): she separates risk she carries from risk that falls on early backers, and ranks the second as worse.
  It is the only verified line where she uses "believe" about other people's support (D13a).
- The case makes the same point for 2031 (VRF, R-C66, p.3 L114-115): "If Laura promises more than she can ultimately
  contribute, she could damage her credibility and lose the confidence or participation of co-sponsors."
- Strength: moderate. It is one source from her student years, about a small business, not a residency. It matches
  the case, which is the stronger authority.

### V3. Failure and imperfection: ship on a deadline, learn from feedback, scrap what is wrong

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8b-Q31 | “I give myself a deadline for when I must post the art, finished or not.” | Geeks OUT, 2022-05-11 (also The Honey POP, 2022-06-02) | advice to aspiring creators ("Post terrible work!") |
| B8b-Q30 | “The quicker you get over your perfectionism, the faster you’ll finish projects, get feedback, improve, and overcome imposter syndrome or “artist stage fright”.” | Geeks OUT, 2022-05-11 | same answer |
| B8b-Q12 | “I scrapped three completely different drafts before landing on this one.” | The Nerd Daily, 2025-03-08 | challenges writing her first fiction book |

- Reading (INT): failure is a normal step in how she works. She sets deadlines, ships imperfect work, uses feedback,
  and throws away drafts that do not work. What she avoids is perfectionism that stops her shipping.
- Also VP:
  - “Ultimately my goal is to tell a story; I don’t need to be perfect to be impactful.” (B8b-Q32, Geeks OUT
    2022-05-11, same answer);
  - “Soon enough, I had a comics diary that I could not only decompress into, but also take pride in how far I’d come
    when I reread it.” (B2b-Q10, Wharton Magazine 2022-04-06, about a nightly 10-minute comic she drew while working
    in tech). A dated record of small steps is what a team decision log is (M021).
- Note: "helped launch the Anti-Resume Project ... to normalize failure" is a reporter's description (Pulse Spikes),
  not her words (section 7c). Her own line on it is candidate D13c-C8 (section 7d).
- Strength: strong (three answers, 2022-2025, one repeated word for word in two outlets).

### V4. "Falling": no usable line in her own professional words

- Her 2025 book *Kirby's Lessons for Falling (In Love)* is fiction. Its "falling" is a climber's fall and falling in
  love. "Queen of Balance" is copy about the fictional heroine (B9b, VP there).
- The only first-person "falling" line in her interviews (The Nerd Daily, 2025-03-08) sits in an answer about her
  family and identity. It is **EXCLUDE-PRIVACY** (D13c; section 7b). This file does not reproduce it.
- So seed 17's "learning to fall safely" has no basis in her words (B9b Q22 found the same). There is no value to map
  here; the only consequence is a guardrail (section 5).

### V5. Build what is missing, with other people, and grow after support shows up

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B2b-Q07 | “If what you want doesn’t exist, create it yourself.” | Poets&Quants, 2018-03-30 (student-era) | "What is the biggest lesson you gained from studying business?" |
| B8b-Q10 | “Only after we realized EVERY student deserved to hear their words of wisdom did we decide to build something to cultivate it.” | The Sign.al 5-year page, founder's note signed by her, c. 2022 (date ASM) | how her student club began |
| B8b-Q37 | “All of it is way beyond our initial passion project. We’re thrilled that the community really supported us and wanted us to continue to grow the festival” | Local News Matters, 2026-02-12 | growth of the free comics festival she co-organises (page's trailing comma dropped) |

- Reading (INT): her founder habit runs in stages: see a gap, check that the need is real, build it with others, then
  grow once the community backs it. The residency in the case fits this pattern (VRF, R-C18, p.1 L25-26: "she has
  combined artistic passion with strategic thinking and a willingness to pursue unconventional opportunities.").
- Also VP: "Well, if people aren’t gonna give it to us, I’ll just make one." (B8a-Q14, 2021, about her next book).
- Also VP: “I couldn’t be more proud of the current team keeping the legacy strong.” (B8b-Q11, the same founder's
  note). She handed her club to a team that kept it running. INT: she values institutions that outlast their
  founder. At most one clause, if co-sponsors ask about life after 2042; funding beyond 2042 is out of scope (case
  p.3 L92-93).
- Strength: strong. The pattern spans 2018 to 2026 across a club, a book and a festival.

### V6. Community and access: money serves getting people "in the room"

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8b-Q38 | “…Our No. 1 priority is to get as many diverse voices and stories in the room as possible, no matter the grounds that they start off on” | Local News Matters, 2026-02-12 | the festival's new mini grants to 20 creators (the paper prints the leading ellipsis) |
| B8b-Q39 | “We definitely hope to offer more as the festival grows.” | same, 2026-02-12 | same passage |
| B8b-Q05 | “Pro-bono visits can be offered on need-basis.” | her Publicity & Speaking Guide (PDF created 2024-03-24) | the booking panel of her own guide |

- Reading (INT): where she controls money, she spends it on access (grants, free entry, need-based pro-bono visits).
  The reporter adds that the festival is "remaining free for exhibitors and attendees" (fact, not her words).
- Limit: this says nothing certain about the residency's fees. The case lists "program fees" as one possible outside
  source (R-C44). Any fee assumption must be labelled ASM.
- Strength: strong and recent (2024-2026).

### V7. Authenticity: personal connection over clever concepts

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8b-Q13 | “But in the process, I lost the heart of my writing—authentic, personal connections.” | The Nerd Daily, 2025-03-08 | why she scrapped her early fiction drafts |
| B8a-Q28 | “So, I scrapped everything and went back to my roots. No more gimmicks.” | same answer | same |

- Reading (INT): she judges her own work by whether it keeps "authentic, personal connections", and she drops
  high-concept framing that loses them.
- "Gimmicks" meant fantasy premises in her drafts (D13a). Applying the test to a portfolio document is our extension,
  and it should be called that. Never quote "No more gimmicks." on its own (B8b-Q14): cut down to three words, it
  invites meanings the page does not support.
- Strength: strong for her own craft (2025); interpretive when applied to us.

### V8. Money and success: meaning over metrics, and freedom as the payoff

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8b-Q21 | “it’s great having thousands of likes, but at the end of the day, it’s just a number. You never really understand the human connection behind it” | Overachiever, 2021-03-15 | why one reader's thank-you note mattered more than metrics |
| B8b-Q22 | “I’d just be like, “Hey, this is why you made this. This is who you’re trying to help, and this is the positive effect you actually have.”” | same interview | what she told herself when she reread a reader's supportive comment |
| B8b-Q26 | “Now I get to fit work around life instead of the other way around, which is such a game-changer” | Input (Inverse), 2022-03-07 | her working life after leaving tech |

- Reading (INT): she measures success by who is helped and by freedom over her time, not by the size of a number.
  When things go badly she anchors on purpose (B8b-Q22).
- Her few verified words about money:
  - she gave up a well-paid job with benefits for "unstable income" (V1);
  - she offers pro-bono visits (V6);
  - she once taught financial literacy (V12).
- **We hold no verified statement by Laura about investing, markets or wealth.** Any "her investment philosophy"
  sentence would be invented.
- Also: her "I did 50 things…" answer (B8b-Q20, quoted in full under V10) frames success as breadth of experience.
- Strength: strong for "meaning over metrics"; the evidence on money is thin by nature.

### V9. Data inside a story; honest about what is unfinished

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8b-Q35 | “I can’t think of many art pieces that I didn’t also write some kind of purpose statement for.” | Pulse Spikes, 2021-06-18 | how writing and art go together for her |
| B8a-Q19 | “That [story] was something I could prove better with data” | Pulse Spikes, 2021-06-18 (the bracket is the outlet's) | her data project Rewriting Herstory |
| B9b-Q09 | “The [unfinished] results are below.” | lauragao.com/rewriting-herstory (undated; student-era, ASM) | her own project page; the bracket is hers, and her table grades each match "Good", "Unsure" or "Bad" |

- Reading (INT): data serves a stated purpose and proves a point inside a story. She labels her own results as
  unfinished and grades their quality.
- Also VP:
  - “I’ve always said that my main purpose is to tell a story” (B8a-Q18, Pulse Spikes 2021-06-18; D13a notes that
    she goes on to say the medium does not matter). Purpose is fixed; the tool can change;
  - she states limits and next steps: "Further probing of other song metrics' effects on danceability would provide
    deeper analysis." (B9b-Q11);
  - she defines terms by their source: "For the purposes of this study, I used Spotify's definitions and values for
    different song attributes." (B9b-Q10);
  - her résumé lists "Experimented and shipped 10 features that resulted in +4.5M DAU" (B9b-Q01) and "Product
    Management: JIRA, Confluence, A/B testing" (B9b-Q02). An A/B test compares a new version against a control.
- The case records a statistics degree (VRF, R-C12).
- Strength: strong (her own published data work plus her résumé). Dates are mostly undated or student-era.

### V10. Keep options open

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8a-Q04 | “My advice is to avoid siloing yourself into an end-all-be-all career situation.” | Poets&Quants, 2018-03-30 (student-era) | advice to a student choosing a business major |
| B8b-Q20 | “I did 50 things, and maybe I didn’t like fully excel at each, but I got to try all of them and have so much fun with them.” | Overachiever, 2021-03-15 | how she hopes to look back at 80 |

- Reading (INT): she resists locking herself into one path. The case gives this value its financial form (VRF, R-C58,
  p.3 L102-103): "She recognizes that committing all remaining assets could limit her financial flexibility as the
  project develops."
- Limit (D13a): these are career statements. Do not turn "50 things" into a diversification formula.
- Strength: moderate for her own words; strong once paired with the case.

### V11. Healthy doubt about hype

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8a-Q37 | “how long will this novelty factor last?” | The Daily Pennsylvanian, 2016-01-28 (student-era) | her goals for her business in its first week; she answered her own question with a plan (D13a) |

- Reading (INT): even about her own early success, she asked whether the excitement would last, and planned for when
  it faded.
- Strength: weak to moderate (one student-era line).

### V12. She has taught money basics to teenagers, and she designs learning to be less daunting

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B2b-Q08 | “Mentor for Tech It Out Philly and MoneyThink, two organizations in which I taught web development and financial literacy to high school students in West Philadelphia.” | Poets&Quants, 2018-03-30 (student-era) | her list of college activities |
| B3b-Q13 | “exercise students’ creativity in less daunting ways than traditional essay writing” | her Educators & Book Clubs Guide (PDF created 2024-03-24) | her signed author's note on the activities she designed |
| B8b-Q06 | “Tired of authors talking your students to sleep? Choose an interactive hands-on activity!” | her Publicity & Speaking Guide (2024) | promotional copy to schools |

- Reading (INT): a team of high-school students is writing for someone who has taught financial literacy to
  high-school students. For her, plain explanation is a professional standard, not a courtesy.
- Related professional facts (VP, D13c check on Poets&Quants 2018, her questionnaire list of internships): "Trading
  Intern at Belvedere Trading in Chicago" and "Policy Analyst Intern at Consumer Financial Protection Bureau". These are
  facts, not value quotes. Her 2024 résumé does not list them (B8b).
- Strength: moderate. The facts are firm; the reading of her standards is inference.

### V13. Tell the whole story, not only the frightening headline

| id | her exact words | source, date | what she was answering |
|---|---|---|---|
| B8a-Q34 | “There wasn’t much that was incorrect as much as there just wasn’t any news about the overall picture of Wuhan outside of the coronavirus” | HuffPost, 2020-04-29 | media coverage early in the pandemic |
| B8a-Q33 | “It's disheartening to know that all they know are the bad parts of it” | NPR, 2020-04-04 | how people knew the city only through virus headlines |

- Reading (INT): she objects more to incomplete framing than to outright error. The case says her first public work
  was "Originally intended as a response to misinformation and anti-Asian racism" (VRF, p.1 L19-20).
- Limit: use this as a principle for how to present risk. Never put these lines, or Wuhan, next to Taiwan in a
  deliverable: that would join two different places (B3b Q08).
- Strength: moderate (two 2020 sources on one topic).

### Decision habits at a glance (INTERPRETATION)

| habit | her words (id) | where it shows up in our plan |
|---|---|---|
| decides a leap by asking what she would regret not doing | B1b-Q11 | the residency is the leap; growth money is not set to the minimum |
| names the cost before leaping | B8b-Q18 | the price of certainty is stated in dollars |
| expects the worst reaction before going public | B8a-Q13 “When I first posted the comic, I expected a way worse reaction” (2021) | bad-case numbers shown beside good ones |
| steadies herself by recalling who the work helps | B8b-Q22 | a bad-year rule: the payments are already bought; the purpose is restated |
| writes a purpose statement for the work | B8b-Q35 | the IPS opens with the purpose; each Trading Note names the holding's job |
| ships to a deadline, finished or not | B8b-Q31 | purchase dates set by rule (no rate-timing); early WInS trades, then refinement |
| scraps drafts that lose the heart | B8b-Q12, B8b-Q13 | show the discarded growth-first plan; cut gimmicks |
| builds once the need is proven, with a team | B8b-Q10, B8b-Q37 | "proof before promise": the 2031 floor is bought, partners come on top |
| uses data as proof and labels unfinished results | B8a-Q19, B9b-Q09 | evidence grades; every probability names its model |
| tests against a control | B9b-Q01, B9b-Q02 | show the all-Treasury "control" next to the chosen mix |

---

## 2. What each value means for the strategy and for how we talk to her

Format per value:
- **Strategy:** a decision the value supports (+) or challenges (−).
- **Earns trust / Feels inauthentic:** what earns her confidence, and what would feel inauthentic or "finance-bro"
  (show-off finance talk: bravado, jargon, chasing returns).
- **Affects:** the deliverable (TN = Trading Notes, Oct 23; IPS = Nov 6; FR = Final Report, Dec 4) and the scored
  criterion (R-S24 strategy, R-S25 client knowledge, R-S26 analysis, R-S27 articulation, R-S28 creativity and
  presentation).

Everything below is specification, not text to submit.

**V1 Risk (leaps, with the cost named)**
- Strategy:
  - (−) It challenges how cautious the plan looks. Whole-portfolio equity is about 0-2% (2027), about 20%
    (2028-2030) and about 4% after the 2031 floor (DER, B10b).
  - (+) It supports a real, not minimal, equity share in the growth money (open item: 50/60/70%; M075).
  - (+) It supports stating the price of certainty, so she can apply her own regret test (section 3.3, N1).
- Earns trust: for each big choice, one plain sentence of the form "we chose X; its price is Y".
- Feels inauthentic:
  - "a conservative portfolio for a cautious client";
  - "Laura has a high risk appetite, so we hold more stocks";
  - calling her "risk-averse" on the strength of B8a-Q03, which is about students choosing a business major;
  - "safe" or "guaranteed" used as selling words.
- Affects: IPS (risk sentence: willingness vs ability, stated as the team's inference); FR (price-of-certainty table);
  TN (the growth note says what the equity is for). R-S25, R-S26.

**V2 Failing others is worse than failing yourself**
- Strategy:
  - (+) No market risk on money other people will rely on: the ten payments and, from 2031, the announced low end.
  - (+) Announce only what is already bought; the floor never falls.
  - (+) This is the Laura-rooted answer to M126 (residents rely on the payments) and M221 (risk sits only on money
    nobody else relies on).
- Earns trust: say, in her terms, which money others will rely on and show that it is owned before it is promised.
- Feels inauthentic:
  - leading with the top of the range;
  - "we expect to deliver $X" with no floor;
  - a confidence number with no model named.
- Affects: IPS (principle: who relies on which money); FR (co-sponsor draft; the range = bought floor plus labelled
  upside); TN (the first Treasury note names the promise it stands for). R-S25, R-S28.

**V3 Failure and iteration**
- Strategy:
  - (+) Place the core WInS trades early and refine them later (M032).
  - (+) Keep a dated decision log.
  - (+) Show rejected options with one number each: growth-first, partial locks, all-Treasury (M108).
  - (−) It challenges any claim that the plan is final and perfect.
  - (−) It sits uneasily with the frozen IPS (section 3.3, N2).
- Earns trust: dated "first version, what we learned, what changed" (for example, the team's original ~75%-equity
  growth-first plan, dropped after testing; CLAUDE.md).
- Feels inauthentic: a polished success story with no mistakes; hindsight edits (WInS notes cannot be edited anyway,
  G-ids).
- Affects: TN (the guide allows a decision that "tested, or refined" the strategy, TN p.1 L12); FR Articulation.
  R-S27.

**V4 "Falling"**
- Strategy: none.
- Communication: never use "falling", "Queen of Balance" or "lessons for falling" frames (section 5). The case's own
  phrase "an appropriate balance" (R-C38) is fine; a book-derived "balance" metaphor is not.
- Affects: all three deliverables. R-S28.

**V5 Build with others, in stages**
- Strategy:
  - (+) The 2031 structure: floor bought, upside stated with its model, partners invited on top (M008).
  - (+) A facility contribution that can grow with results; committed in 2033 and possibly drawn in stages (M027,
    open).
  - (+) Keeping flexibility "as the project develops" (R-C58).
- Earns trust: her secured part presented as the first contribution that invites partners; more offered as support
  is proven.
- Feels inauthentic: casting her as a lone funder of "the dream"; promising growth before any proof.
- Affects: FR (co-sponsor draft; the form of the facility recommendation). R-S25, R-S28.

**V6 Community and access**
- Strategy:
  - (+) The case's own order, reserve before facility (R-C57), reads as her priority: the payments keep the doors
    open.
  - (+) If a fee assumption is needed, label it ASM (M105). Do not state a fee policy for her.
- Earns trust: describe the payments by what they secure: "ten years of operating money".
- Feels inauthentic:
  - charity-speak about residents;
  - an invented budget or resident count (the case expects no business plan, R-C95);
  - lifting the festival's identity focus into a residency programme.
- Affects: FR (co-sponsor draft; assumptions table); IPS (one clause on why operations come first). R-S25.

**V7 Authenticity**
- Strategy (+): cut anything that exists only for show (M103):
  - a Taiwan equity tilt (EWT);
  - identity- or interest-themed funds;
  - branded framework names;
  - book puns;
  - model layers in the main text where "bought, not forecast" already answers the question.
- Earns trust: plain names for the parts of the plan ("the payments", "the growth money"); one idea per section.
- Feels inauthentic: "Messy Roots Portfolio"; "lessons for falling (in rates)"; comic-style layouts; AI images.
- Affects: all three. R-S28.

**V8 Meaning over metrics; freedom**
- Strategy:
  - (+) The headline measure is what is secured ("10 of 10 years of operating payments bought"), then dollars (M057).
  - (+) A real flexibility share after 2033 rather than everything into the building (R-C58, B8b-Q26).
- Earns trust: numbers translated into what they do (years funded; the facility range in 2033 US$ and in today's
  building-cost terms).
- Feels inauthentic:
  - "maximise returns";
  - bragging about WInS gains or rank (the Guide p.3: WInS "is not the competition scorecard");
  - reporting only portfolio dollars.
- Affects: FR headline; TN ("reasoning ... not simply whether an investment gained or lost value", TN p.1 L15-16);
  IPS objective written as goals, not a return target. R-S25, R-S28.

**V9 Data inside a story; honest uncertainty**
- Strategy:
  - (+) Define "high degree of certainty" by what can be observed (payments bought at market prices), not by a model
    percentage (brief section 8 item 6).
  - (+) Show the control, an all-Treasury growth money, and the lift equity adds (B9b Q3).
  - (+) Grade each number: market price, estimate or assumption (M231).
  - (+) Round to the model's real precision (B9b Q10).
- Earns trust: every probability names its model; each chart proves one claim; unfinished parts are labelled.
- Feels inauthentic:
  - "95% confident" with no model named;
  - "$207,413";
  - "200,000 simulated paths" in the main text;
  - a lock-early "0% miss" without the words "by construction" (brief section 11).
- Affects: FR (charts, assumptions table); IPS (certainty defined in words; no charts allowed, R-I55); TN (one
  checkable data point). R-S26, R-S28.

**V10 Keep options open**
- Strategy (+): keep part of the post-reserve surplus uncommitted (the share is open, M003); never "committing all
  remaining assets" (R-C58).
- Earns trust: say what the held-back money is for (an overrun buffer, or the chance to expand what works) and when
  it could be used.
- Feels inauthentic: a "rainy-day fund" with no purpose; the facility gift treated as the only goal.
- Affects: FR. R-S25.

**V11 Doubt about hype**
- Strategy (+): a broad index, not thematic or AI funds; state concentration plainly; no "AI hedge" story (M010).
- Earns trust: one plain concentration sentence using the fund's own published numbers.
- Feels inauthentic: trend-chasing trades; "the AI revolution"; buying what is hot in WInS.
- Affects: TN (growth note); FR. R-S24.

**V12 Teacher of teenagers; plain words**
- Strategy (+):
  - the fewest rules that do the job;
  - low-cost funds with costs disclosed (WInS commissions now; a fee assumption in the FR projections, BS-01; M052).
  - Reason: she taught financial literacy and interned at a consumer-protection agency and at a trading firm (V12
    facts).
- Earns trust:
  - each term defined once;
  - a classmate could restate every rule;
  - costs named.
- Feels inauthentic: jargon in the main text ("alpha", "DV01", "convexity"); a sales tone; costs left out.
- Affects: all three. R-S25, R-S28.

**V13 Whole story**
- Strategy (+):
  - show both good and bad outcomes for every projection (the case asks for "favorable and unfavorable market
    outcomes", p.3 L118-119);
  - name Taiwan-related risks once and precisely (currency, construction costs, continuity), without caricature
    (M215).
- Earns trust: good case, middle, bad case, and what the plan does in each.
- Feels inauthentic: drama (war scenarios as spectacle), or silence about risks.
- Affects: FR (scenario table; co-sponsor draft). R-S26, R-S28.

### Communication checklist (one page, drawn from sections 1-2)

**Earns her confidence** (R-S25 "recommendations that can earn her confidence"):
- [ ] The purpose comes first, in one sentence, before any instrument.
- [ ] Which money others rely on, and proof that it is bought before it is promised.
- [ ] The price of each big choice in one number, and the good-market give-up as well as the bad-market protection.
- [ ] The discarded drafts, with one number each and why they were dropped.
- [ ] Each number graded (market price / estimate / assumption), rounded, with its model named.
- [ ] What the numbers secure ("10 of 10 years") before portfolio dollars.
- [ ] The gaps in "certainty" named (section 3.3, N4).
- [ ] Costs named.
- [ ] Plain words; every term defined once.
- [ ] Her facts exactly right ("bestselling"; "finalist", not "winner", for the Harvey and Goodreads awards; D13a
      note on B3a-Q03).

**Feels inauthentic or "finance-bro"**, as examples to avoid, with the reason:
- "beat the market", "alpha", "crush", "aggressive growth", "conviction picks": metric-chasing (V8, V12);
- "guaranteed", "risk-free", "95% sure" with no model: false precision (V9);
- WInS rank, P&L or "our winning trade": the Guide says WInS "is not the competition scorecard";
- book-title or plot puns: gimmicks (V7) and tokenism (section 5);
- "Laura says…" followed by the case pull quote: misattribution (section 4, R1);
- "Laura is risk-averse" or "Laura loves risk": each misreads her (V1, V2);
- walls of text and unexplained acronyms (V12).

---

## 3. Where our current strategy echoes her ideas honestly, and where it does not

### 3.1 The plan being compared (not yet approved by the team; CLAUDE.md, brief section 7, S3 allocation v1)

- **January 2027:** buy Treasuries (a STRIPS ladder) matching the ten $50,000 payments, about $292k-$294k of the
  $300k (brief section 6; S3). The small leftover waits in T-bills. If rates fall first, buy the longest-dated
  payments first and complete the ladder from the 2028 deposit.
- **January 2028:** the $150k plus the leftover (about $158k) becomes the growth money: 60% global equity (VT) and
  40% short Treasuries (VGSH), provisional.
- **2031:** part of the growth money (80% in the model; an open parameter) moves into a 2-year Treasury. That is the
  floor Laura can promise co-sponsors, plus an upside with a stated probability.
- **2033:** the ladder is the operating reserve; the facility contribution comes from the rest; the leftover is kept
  mainly as project flexibility.
- **WInS:** either option (ii), 66% Treasury hedge (IEF/TLH), 20.5% VT, 12.5% VGSH and 1% cash, or option (iii),
  about 98% Treasuries (S3).

### 3.2 Honest echoes

| # | plan element | her words | why the echo is honest | limit |
|---|---|---|---|---|
| E1 | No market risk on money others will rely on (payments; the announced 2031 low end) | D13a-N01 | Her words and the case (R-C66) point the same way | 2016 student line about a small business |
| E2 | Risk taken only where she alone bears the cost (the upside of the facility; post-2033 flexibility) | B1b-Q11, B8b-Q18 with D13a-N01 | The risks she describes taking were career or public risks she carried herself; she ranks failing backers as worse. This is the true replacement for "floor-first" | Joins two sources; it is INT |
| E3 | Proof before promise: floor bought in 2031, partners invited on top, more if markets allow | B8b-Q10, B8b-Q37, B8b-Q39 | Her club and festival grew after the need and the support were shown | A club or festival is not a residency |
| E4 | Operations first (reserve before facility) | B8b-Q38, B8b-Q05 | Her record spends money on access; the order itself is the case's (R-C57) | Says nothing about fees |
| E5 | "High certainty" = bought at market prices, not forecast; model numbers labelled | B9b-Q09, B8a-Q19 | She labels her own results "[unfinished]" and uses data as proof | Honest only if the FR really grades its numbers |
| E6 | The team scrapped its growth-first draft after testing | B8b-Q12 | True event, not a metaphor (CLAUDE.md: growth-first "failed: 3-8% payment shortfall") | Only if Articulation tells it as it happened |
| E7 | Buy on the date, by rule; no rate-timing | B8b-Q31 | Same working habit: a deadline, "finished or not" | Her line is about posting art |
| E8 | Keep flexibility; never commit everything | B8b-Q26, B8a-Q04 | Consistent with her record | The case says it first (R-C58); cite the case |
| E9 | No fund covers the 2038-2042 payments, so the ladder is built from individual Treasuries | B2b-Q07 | A true fact: no iBonds Treasury fund exists for Dec 2037-2043 (brief section 14) | Trivial; keep it as a private design note, never as a slogan |

### 3.3 Where it does not echo (candid), and how the plan could answer

These are options for the team and for Phase E, not decisions.

**N1. The leap.** Her risk words are "always take the jump". The plan:
- about 0-2% whole-portfolio equity in 2027;
- about 20% in 2028-2030 (at median values; more after strong markets);
- about 4% after the 2031 floor (DER, B10b re-run; ASM: sleeve at median values, 60/40 sleeve, 80% floor share);
- WInS option (iii): about 98% Treasuries.

S3 already names the weakness: "A reader may see about 98% Treasuries as timid for a client who 'has been willing to
take thoughtful risks'". Unexplained, the plan reads as generic safety, which is the opposite of her voice.

What the numbers say (DER: the B10b frontier that question M243 cites; 2028 deposit $150k; re-run by D13c
2026-09-27; ASM inputs: JPM returns, lognormal, no fees):

| | 2033 surplus p5 | p50 | p95 | P(ten payments not fully funded) |
|---|---|---|---|---|
| Payments 100% locked in 2027 | $150k | $210k | $299k | 0.00% |
| Nothing locked (60/40 until 2033) | $34k | $221k | $496k | 2.10% (11.72% if the 2028 deposit is $75k) |

So locking costs about $11k at the median and about $200k at the 95th percentile, and protects about $116k at the
5th percentile.

Other labelled figures:
- B9b's scratch runs (ASM, not re-run by D13c): 60% equity in the growth money adds about +$9k at p50 and +$55k at
  p95 and costs about −$22k at p5, against an all-Treasury growth money.
- B9a (DER, not re-run): locking the surplus as well would give about $204k in 2033 with almost no market risk.

How the plan could answer:
- (a) **Say where the leap is** (IPS and FR). A strong sentence must contain:
  - the residency is the leap;
  - the money residents and partners will rely on is bought first;
  - the growth money takes a deliberate risk for a bigger facility;
  - what that risk can cost: the facility range, never the payments.
- (b) **Run her regret test both ways, with numbers** (FR, one small table). Rows: lock / no lock. Columns: strong
  markets / weak markets. Each cell says what she would regret. In strong markets locking gives up upside; in weak
  markets not locking could leave payments unfunded. That second regret falls on the people she said matter most
  (D13a-N01).
- (c) **Defend the growth-money equity weight in her terms** (IPS and FR). The median barely moves at 50/60/70%
  ($205k/$207k/$209k, brief section 6), so the choice is about the tails.
  - Her regret rule argues against the minimum.
  - The case's "appropriate balance" (R-C38) argues against the maximum.
  - Never justify it with "she is cautious".
- (d) **The 2031 floor share is open** (brief section 9). Her festival words ("We definitely hope to offer more as the
  festival grows.") fit a floor she can always keep, plus a labelled "more if markets allow".
  - A smaller floor share keeps more growth money invested until 2033: a lower announced number, but more upside.
  - The case wants "a meaningful personal contribution" (R-C64), so the trade-off needs pricing by D3/E1.
  - Her words do not pick the number.
- (e) **WInS (ii) or (iii).** Either way, one Trading Note reflection must answer "why so little equity?" in her
  terms: in 2027 almost all of her real $300k buys the payments, and her ability to take risk starts with the 2028
  money (B9a Q1).

Affects: IPS, FR, TN; R-S24, R-S25.

**N2. Iteration versus a frozen plan.**
- Her habit: ship, get feedback, revise, scrap (V3). A stronger line is waiting for D13a's ruling: "never be
  finished" (candidate D13c-C2).
- The plan: a ladder held to maturity, and an IPS that "becomes the official record" and cannot be revised after
  Nov 6. The Guide p.5 L156-157 (VRF) says a strategy "should not be rewritten simply because markets move or
  hindsight reveals a different outcome."
- How it could answer: fixed rules, with review points planned in advance:
  - the 2028 deposit;
  - the 2031 floor and announcement;
  - the 2033 reserve and facility decision;
  - yearly rebalancing of the growth money within bands.

  The Guide itself allows "planned adjustments as funding dates approach". Show the refinement history in the TN and
  FR. Do not pretend the first version was right.
- Affects: IPS (planned-changes clause), TN, FR. R-S24, R-S27.

**N3. "It's just a number" versus a number-heavy plan.**
- The plan's working files speak in p5/p50/p95, "$289 per basis point", "duration 9.90 years", "27bp headroom" and
  "200,000 paths".
- How it could answer:
  - lead with what the numbers secure;
  - keep mechanics in an appendix or in the team's notes;
  - round;
  - one chart per claim.
- She is also a data person (V9), so the answer is translation, not removing numbers.
- Affects: FR mostly; IPS wording. R-S28.

**N4. Certainty language with holes in it.** The definition "certain in nominal USD, barring U.S. Treasury default"
is precise, but it is not the whole story. Two gaps a client who labels her own results "[unfinished]" would expect
to see named:
- **Gap (i), the purchase price.** The lock is complete in January 2027 only if the ladder costs $300k or less. In
  roughly 1 in 4 to 1 in 3 modelled rate paths it costs more (ASM-based: brief section 14; S3/S4). Part of the promise
  then waits on the 2028 deposit, which comes from income she herself called "unstable" (B8b-Q18). The joint tail,
  rates fall and the deposit is late or smaller, is still unanswered (brief section 9).
- **Gap (ii), nominal dollars.** The dollars are nominal US dollars. The residency pays costs in Taiwan, and a fixed
  $50k buys less each year. Real erosion is also unanswered (brief section 9). Her No. 1 priority is people in the
  room (B8b-Q38); nominal certainty does not guarantee the same number of people.

How it could answer:
- one IPS clause and one FR box with the definition and both gaps in plain words;
- the rule if rates fall first;
- amounts in US$ with a today's-cost equivalent.

Affects: IPS, FR. R-S26, R-S28.

**N5. A self-sufficient fortress versus her partnership habit.**
- The case requires her to fund the payments alone (R-C48), and the plan complies. But her institutions grew with
  partners (V5, V6).
- How it could answer: describe co-sponsors' role positively. They may fund the facility and extra operations
  (R-C44). Her secured part is the first commitment, and it invites theirs.
- Affects: FR (co-sponsor draft). R-S28.

**N6. "50 things" versus one issuer.** The 2027 book is almost entirely U.S. Treasuries. This is **not a real clash**:
her line is about careers (D13a), so claim neither a clash nor an echo. If asked:
- the promise is concentrated on purpose, to match its currency and dates;
- diversification lives in the growth money (VT holds about 10,088 stocks, S3).

Affects: FR. R-S24.

**N7. Creativity.**
- Her record: "create it yourself" (B2b-Q07), and the case's "willingness to pursue unconventional opportunities"
  (R-C18).
- The plan: standard liability matching, which is what pension funds do. Say so.
- Its originality is fit, not invention, for example:
  - a floor bought so the 2031 range never has to be walked back;
  - the 2028 deposit treated as the moment her ability to take risk begins (B9a Q1).
- Do not call the plan "innovative".
- Affects: FR, IPS pitch. R-S24, R-S28.

### 3.4 Echoes proposed in Phase B that do not survive checking

| Phase B echo | why it fails | use instead |
|---|---|---|
| "Floor-first leap" (B8a Q02, B8b Q3, B9a/B9b grids, M018) | Rests on a reporter's sentence (D13c-R1, section 7c); its "So" follows personal material (D13a; D13c re-read). Not her decision rule | E2 (risk she bears vs risk others bear) |
| "risk-adverse" as her profile (B8a-Q03) | About students choosing a business major | Do not describe her risk tolerance with it |
| "Both, not either-or" as an allocation rule (B8b-Q07) | About graphic vs prose novels in class (D13a) | The case's own "appropriate balance" (R-C38) |
| "Diminishing returns" (B9b-Q12) | About dance songs | Nothing |
| Wish for a trade-offs "author's note" as her rule for explaining decisions (B8b-Q17) | About translation choices; in the same answer she says "But at the same time, I wish I didn’t always have to explain myself." (D13a) | Keep the trade-offs box short for readability, not "because she asked" |
| "Write a letter to Future You." as her planning habit (B8b-Q08) | A writing prompt for students | A plain pre-committed bad-year rule, no letter |
| Co-living, Yilan art residencies, Taiwan as a top place (Maverick Show) | Transcript lines: PARAPHRASE-UNVERIFIED or EXCLUDE-PRIVACY (D13a) | The case's residency description (R-C39, R-C40) |
| B3b-Q09 (a line on which languages her memoir appears in) used as a market fact | Answer to a family question: EXCLUDE-PRIVACY (D13a). Its text is not repeated here | State any market fact in our own words from a non-private source |
| Kirby's fall, "Queen of Balance" (B3b Q13, M144) | Fiction and publisher copy; the one first-person "fall" line is private | Nothing: no metaphor |
| The pull quote as "her motto" | Unattributed (D13a: 8 searches, 36 pages) | Cite it as the case's line (section 5) |

---

## 4. What she would reject on sight (with evidence)

"Strength" rates how directly the evidence supports the claim. The team decides.

| # | what | evidence | strength | where it bites |
|---|---|---|---|---|
| R1 | The case pull quote presented as her words ("Laura said", "her motto") | D13a: no speaker line on the case page, and no source in 36 pages. Her first public work was "Originally intended as a response to misinformation" (case p.1, VRF) | strong | IPS pitch, FR |
| R2 | Book-title puns and plot metaphors ("messy roots", "lessons for falling", "Queen of Balance", "fall safely") | B8b-Q13 and B8a-Q28 on her own drafts (extension, INT); the fiction and privacy findings (V4) | moderate, and costs nothing to follow | all |
| R3 | Her identity as a reason for a holding (Taiwan or China tilt "for her heritage"; identity-themed funds; "returning to her roots") | Brief section 4 tokenism rule; the case gives no background-to-portfolio link and names no values screen (brief section 8 item 19); "Born in Wuhan, China, and raised in Texas" (case p.1): Taiwan is neither (B3b Q08); M045 | strong | WInS now, TN, IPS, FR |
| R4 | A finance-prestige tone (bravado, "beat the market", rank and P&L talk) | Her D13a-verified words: B8b-Q21 ("just a number") and B8b-Q41 (her "bankers" joke). Stronger lines await D13a's ruling (D13c-C3 "excel models" / "corporate coffee chats"; D13c-C4 "McKinsey or Goldman Sachs"). She is **not** anti-finance: Wharton degree, a trading internship and a consumer-protection internship (V12 facts). She would reject the tone, not finance | moderate | all |
| R5 | False precision and unlabelled probabilities ("guaranteed", "95%" with no model, "$207,413", "0% miss" without "by construction") | B9b-Q09 ("[unfinished]", Good/Unsure/Bad grades); B9b-Q11 (limits stated); B9b-Q02 (A/B testing); statistics degree (R-C12) | moderate to strong | IPS, FR, TN |
| R6 | Hidden costs or a sales tone | Consumer-protection internship and financial-literacy teaching (V12); the CFA Institute Asset Manager Code the Rules page points to (R-W29) | moderate (inference from her record) | IPS, FR |
| R7 | A one-sided risk story (drama, or silence) | B8a-Q34, B8a-Q33; case p.1 on misinformation | moderate (a principle carried over) | FR |
| R8 | A wall of text; talking down | B8b-Q06, B3b-Q13 | weak to moderate (promotional copy), but easy to follow | FR |
| R9 | AI-generated images or imitation comic art in the FR | **No verified statement by her on AI** (B3b, B9b). This is an ASSUMPTION from her profession. She has worked for an AI product client ("AI-powered online learning software", B9b-Q06), so never call her anti-AI | ASM | FR |
| R10 | Guessing at her real life or finances (her teaching job's future, a writing break, where she lives), or treating the case as her real plan | "While the client is real, the financial scenario is developed specifically for the competition" (R-W4); brief section 4 privacy rule | strong (rule) | FR |
| R11 | Overpromising: leading with the top of the range, or a range with no floor | Case R-C66; D13a-N01 | strong | FR co-sponsor draft |
| R12 | Hype trades (AI or thematic funds bought because they are hot) | B8a-Q37 (2016) | weak to moderate | WInS now, TN |

---

## 5. Tokenism and privacy guardrails

### 5.1 Rules (checklist for every deliverable)

- [ ] **Swap test** (B3b Q12). Keep a Laura-specific sentence only if it rests on her professional record or the case:
      the statistics degree, income she called "unstable", institution-building, credibility with backers. Cut it if
      it only works because of her ethnicity, sexuality, gender or birthplace.
- [ ] **Themes, not reasons.** Identity, belonging, immigration and community may be named as what her books and
      public work are about, as context for whom the residency serves. They are never a reason for a security, a
      weight, a tilt or a screen.
- [ ] **No "falling", "Queen of Balance" or book-title metaphors** anywhere (V4, R2). The case's own "appropriate
      balance" (R-C38) is fine.
- [ ] **No invented philosophy.** We hold no verified statement by her on investing, markets or wealth (V8).
- [ ] **Pull quote.** Cite "The only person who needs to believe in something is yourself." as the case's line
      (Client Profile p.1). Never "Laura said", "in an interview" or "her motto" (D13a).
  - If it is used at all, pair it with one dated line of hers (D13a-N01, 2016, student-era) and tie both to a promise
    she can keep (a floor already bought).
  - The other near-match, D13a-N02 (2016), carries a gender framing that is hers. Leave it out of deliverables.
- [ ] **Date and context.** Every quote carries its outlet, year and topic. Say "as a student" for 2016-2018 lines.
- [ ] **No trimming into new meaning.** These lines are fragile: "risk-adverse" (B8a-Q03); "No more gimmicks." alone
      (B8b-Q14); "diminishing returns" (B9b-Q12); "explain myself" (B8b-Q17). B8a-Q05 describes other people, not
      her.
- [ ] **Pronoun:** "she", as the case uses. Her site lists she/her and they/them (D13a note on B8b-Q03).
- [ ] **Facts exactly as she states them:** "bestselling" (case); "finalist" for the Harvey and Goodreads awards
      (D13a note on B3a-Q03).
- [ ] **Real-life news stays out** (her college's future, a writing break, her home). Use industry-level facts only,
      to motivate labelled stress tests (B3b Q15).
- [ ] **Visuals:** no AI images and no comic-style pastiche (ASM, R9). Record AI use exactly (R-W46).
- [ ] **Never suggest contacting her** (R-W16: contact means disqualification).

### 5.2 Using her public work themes without decoration

| allowed (spec) | not allowed |
|---|---|
| Her record as an institution-builder (a club, a festival) as evidence for how the 2031 message is ordered | Her identity as the reason Taiwan was chosen, or as the plan's theme |
| Her own word "unstable" for self-employed income, once, as her public statement, to justify why the payments are bought from the first deposit (M216) | Any guess at her actual finances, contracts or earnings |
| Her data habits (purpose, proof, "[unfinished]") as the reason every number is graded | Imitating her comics or data projects in the FR's design |
| One or two quotes in the FR, each tied to one decision | Quotes as decoration at the top of sections |
| The case's own description of her work's themes (R-C10: "identity, belonging, and the power of storytelling") | Linking those themes to an asset, a country weight or an ESG screen the case never names |

### 5.3 Where a Laura quote may appear (spec; the cap is ASM)

- **TN:** none. There are 100 words for the reasoning behind a trade (TN p.2).
- **IPS:** none. "Formal citations are not permitted" (R-I55), and 500 words are scarce. Echo her principles in the
  team's own words (for example, the promise comes first; risk sits with money nobody else relies on).
- **FR:** at most 1-2, each with its outlet, year, what she was answering and the decision it supports. Suggested
  pair: D13a-N01 with the co-sponsor floor; B8b-Q12 with the growth-first draft the team scrapped.

### 5.4 Do-not-use list (ids and descriptions only; this file does not reproduce private text)

The full list is in section 7b: D13a's seven EXCLUDE-PRIVACY ids plus four more lines D13c flags.

---

## 6. The 15 strongest verified quotes for the team (all D13a VERIFIED-PRIMARY; re-checked by D13c)

| # | id | exact words | source, date | why it matters (one line) |
|---|---|---|---|---|
| 1 | D13a-N01 | “It’s actually harder as an entrepreneur because not only are you letting yourself down, but more importantly, you’re also letting other people down — people who were your earliest supporters and were the first to believe in you.” | Daily Pennsylvanian, 2016-01-28 (student-era) | The only verified line on others' belief. It grounds "no risk on money others rely on" and "announce only what is bought" |
| 2 | B1b-Q11 | “But I always tell myself, you should always take the jump because you’re always going to regret not doing it.” | Overachiever, 2021-03-15 | Her own risk rule. The plan must answer it, or look timid (N1) |
| 3 | B8b-Q18 | “It’s not an easy thing to say, “let me give up my incredibly cushy, paying job with health insurance to be self-employed, with unstable income.”” | Overachiever, 2021-03-15 | She named her own income "unstable". This is why the 2028 deposit is uncertain and the promise is bought first. Use once; never speculate |
| 4 | B8b-Q38 | “…Our No. 1 priority is to get as many diverse voices and stories in the room as possible, no matter the grounds that they start off on” | Local News Matters, 2026-02-12 | Her newest stated priority is access, which makes "operations first" hers. It is about festival grants |
| 5 | B8b-Q37 | “All of it is way beyond our initial passion project. We’re thrilled that the community really supported us and wanted us to continue to grow the festival” | Local News Matters, 2026-02-12 | Growth came after community support. This is the shape of the 2031 message |
| 6 | B8b-Q10 | “Only after we realized EVERY student deserved to hear their words of wisdom did we decide to build something to cultivate it.” | Sign.al founder's note, c. 2022 (date ASM) | Validate, then build: "proof before promise" |
| 7 | B2b-Q07 | “If what you want doesn’t exist, create it yourself.” | Poets&Quants, 2018-03-30 (student-era) | Her founder method, and the residency itself. Many teams will quote it, so it is not distinctive |
| 8 | B8b-Q21 | “it’s great having thousands of likes, but at the end of the day, it’s just a number. You never really understand the human connection behind it” | Overachiever, 2021-03-15 | Report what numbers secure ("10 of 10 years"), not bare dollars |
| 9 | B8b-Q13 | “But in the process, I lost the heart of my writing—authentic, personal connections.” | The Nerd Daily, 2025-03-08 | Her own authenticity test. Cut what is only for show. Pair with B8a-Q28, never "No more gimmicks." alone |
| 10 | B8b-Q12 | “I scrapped three completely different drafts before landing on this one.” | The Nerd Daily, 2025-03-08 | Showing the discarded growth-first draft is her own habit (Articulation) |
| 11 | B8b-Q31 | “I give myself a deadline for when I must post the art, finished or not.” | Geeks OUT, 2022-05-11 | Purchase dates set by rule; early WInS trades refined later |
| 12 | B8b-Q35 | “I can’t think of many art pieces that I didn’t also write some kind of purpose statement for.” | Pulse Spikes, 2021-06-18 | The IPS opens with a purpose; every Trading Note names the holding's job |
| 13 | B8a-Q19 | “That [story] was something I could prove better with data” | Pulse Spikes, 2021-06-18 | Each FR chart proves one claim; data serves the story |
| 14 | B9b-Q09 | “The [unfinished] results are below.” | lauragao.com/rewriting-herstory (undated) | She labels unfinished results and grades them: grade our numbers and name the certainty gaps |
| 15 | B2b-Q08 | “Mentor for Tech It Out Philly and MoneyThink, two organizations in which I taught web development and financial literacy to high school students in West Philadelphia.” | Poets&Quants, 2018-03-30 (student-era) | She taught financial literacy to high-schoolers, so a high-school team must be plain and honest about costs |

---

## 7. Separate labelled lists: lines NOT usable as her words (or not yet)

### 7a. PARAPHRASE-UNVERIFIED (never in quotation marks as hers)

| id(s) | what | how it may be used |
|---|---|---|
| B2a-Q13 = B2b-Q11 = B8b-Q01 = B8a-Q39 | The case pull quote "The only person who needs to believe in something is yourself." | As the case's words (VRF, Client Profile p.1; R-C21, R-AN30). Never as hers |
| B8a-Q21, B8a-Q24 | Maverick Show transcript lines (a transcript with visible errors, not checked against the audio) | Not at all as quotes. For the career-leap idea use B8b-Q18 / B1b-Q11 |

### 7b. EXCLUDE-PRIVACY or do-not-use (never use, however accurate; text not reproduced)

- **D13a's seven EXCLUDE-PRIVACY ids:** B3b-Q09, B8b-Q23, B8b-Q24, B8b-Q34, B8a-Q20, B8a-Q22, B8a-Q23. Their topics
  are family, home and travel life, coming out, and her personal identity story.
- **Added by D13c (these were not in D13a's scope):**
  - The Nerd Daily 2025-03-08: the only first-person line about falling (and climbing back). It sits in an answer
    about her family and identity: EXCLUDE-PRIVACY.
  - Pulse Spikes 2021-06-18: the sentence about how her parents saw her student choices: EXCLUDE-PRIVACY. It sits
    directly before candidate C4.
  - Geeks OUT 2022-05-11: a line about where she lived and travelled (B8b V35): EXCLUDE-PRIVACY (home and travel
    life).
  - Mission Chronicle 2025 (B8b V44): a line about growing up between cultures. Identity context: do not use for
    finance (tokenism), as B8b itself advised.

### 7c. Not her words (reporter, publisher or case text that Phase B leaned on)

| text (short) | real author | status and use |
|---|---|---|
| "So when she got the book deal with HarperCollins, she gave Twitter her notice." (D13c-R1) | Input/Inverse reporter, 2022-03-07 | Verbatim on the page (D13c), but it is the reporter's words, and its "So" follows personal material. Not evidence of a floor-first rule |
| "Even before her comic went viral on Twitter, she’d made a tentative plan…" | same reporter | Reporter's account; do not present it as her plan |
| "remaining free for exhibitors and attendees" (D13c-R2) | Local News Matters reporter, 2026-02-12 | Usable as a fact about the festival, not as her words |
| "helped launch the Anti-Resume Project … normalize failure"; "her anti-resume includes receiving 33 job rejections" | Pulse Spikes reporter (2021); Daily Pennsylvanian reporter (2019-03-17) | Reporter paraphrase. The 2019 article says The Signal launched the project in 2019 and profiled her as an alumna. Cite as the reporters' account |
| "Once dubbed the Queen of Balance…" | book copy about the fictional heroine | Never about Laura |
| "Laura Gao believes stories have the power to change how people see the world." | the case (R-C9), in Wharton's house template (M136) | The case's framing (VRF). Never "Laura says" |
| "Laura Gao cares so passionately about making a difference…" | Wharton staff nominator on the Poets&Quants page | Not hers |
| B8a-Q05 "each has juggled passion against practicality…" | her words, but about other people | Never as a self-description |

### 7d. D13c new finds: verbatim on fresh copies (2026-09-27), NOT in D13a's register

These need D13a's speaker, context and privacy ruling before anyone uses them as her words. D13c's reading is given
for each.

| id | exact words | source, date | why it matters | D13c caution |
|---|---|---|---|---|
| D13c-C1 | “I think for me, that took a lot of fear out of it.” | Overachiever, 2021-03-15 (same answer as B1b-Q11) | Her regret rule is how she manages fear | Quote only together with B1b-Q11 ("that" points back to it) |
| D13c-C2 | “My biggest advice is to be OK with the fact that your significant projects will never be finished. It must constantly be sketched, erased, dropped in rain, ripped apart and sketched again.” | Daily Pennsylvanian, 2016-01-28 (student-era; same answer as D13a-N02) | Iteration; the tension with a frozen IPS (N2) | Do not continue into the next sentence, which carries a gender framing |
| D13c-C3 | “After all, the Laura Gao I knew loved building apps, not excel models; perfected her artwork, not her resume; and devoted herself to art galleries, not corporate coffee chats.” | Poets&Quants, 2018-03-30 (student-era; her first-person answer) | Corrects Phase B, which credited it to the nominator. Her own contrast with finance-prestige culture (R4) | D13a's note on B8a-Q02 says "the sentence before it contains family material". On the page C3 is the sentence directly before B8a-Q02, and the family reference is in the sentence before C3, not in C3 itself. D13a to confirm; never quote or paraphrase that earlier sentence |
| D13c-C4 | “And to my peers, who were like ‘why aren’t you going for McKinsey or Goldman Sachs instead of wasting your time doing art,’ it seemed like a failure, too.” | Pulse Spikes, 2021-06-18 | Peer pressure toward prestige finance, told as "failure" (R4) | Its "And … too" points back to the private sentence about her parents. D13a to rule whether it can stand alone. Until then, background only |
| D13c-C5 | “There’s a vibrant community of queer comic creators here in San Francisco, but why wasn’t there any single event where we could celebrate that community and bring everyone together?” | Local News Matters, 2026-02-12 | Build what is missing, in 2026 (V5) | Not needed: B2b-Q07 and B8a-Q14 carry the idea without naming an identity group |
| D13c-C6 | “When we discuss COVID and how it connects with Chinese or Wuhanese people, we have to be mindful of how our perspective may negatively bias us against people from that region, and instead, focus on the full human story.” | HuffPost, 2020-04-29 | Complete framing (V13) | Principle only. Never quote it near Taiwan |
| D13c-C7 | “mainly because I’m so interested in them and I don’t want to pigeon-hole myself into one thing.” | Pulse Spikes, 2021-06-18 | Keeping options open (V10) | It starts mid-sentence: quote it with the outlet's preceding words "I have done a lot of different things," |
| D13c-C8 | “[I shared an anti-resume] mainly because I started off in business school, and then I ended up gravitating towards other things,” | Pulse Spikes, 2021-06-18 (the bracket is the outlet's) | Her own account of making failures public (V3) | The sentences after it are about her parents: never continue the quote |

Two professional facts were also verified (D13c-F1, D13c-F2; section 1, V12): the Belvedere Trading and Consumer
Financial Protection Bureau internships, as listed in 2018.

---

## 8. Method and verification record

1. Read the brief, the case and D13a in full. D13a decided each quote's status; D13c did not overrule any D13a
   verdict.
2. Read B8a, B8b, B9a, B9b and B3b in full. Took their value readings as hypotheses and kept only those that D13a-VP
   words support.
3. Re-read, on primary pages, the passages behind the two biggest Phase B claims:
   - the Input/Inverse "So when she got the book deal…" paragraph (confirming D13a);
   - the Overachiever "take the jump" answer.

   Also read The Nerd Daily Q&A, Pulse Spikes, the Daily Pennsylvanian (2016 and 2019) and Poets&Quants for "falling",
   "failure" and finance lines. Private material on those pages was read but not recorded.
4. `research/insight_v1/scripts/D13c_voice_map_check.py` (run 2026-09-27, fresh copies via curl, default user agent):
   - 50 of 50 D13a ids quoted or cited here are D13a VERIFIED-PRIMARY and verbatim (a coverage check confirmed that
     every verified line quoted in full in this file is among them, or is a same-text copy of one);
   - 8 candidates (C1-C8), 2 facts (F1-F2), 2 reporter lines (R1-R2) and the ellipsis form of B8b-Q38 (P1) are
     verbatim;
   - 8 case lines are VRF.

   The script prints no page text (privacy); fresh copies went only to the session scratchpad.
5. Re-ran `research/insight_v1/scripts/B10b_designer_checks.py` (seed 20260927). It reproduced the price-of-certainty
   frontier and the whole-portfolio equity path used in N1 (2027 1.5%, 2028 20.4%, 2031 4.2%). The 2027 figure is
   about 0% if the leftover waits in T-bills, as S3 plans.
6. Figures taken from other files without re-running them are labelled with their source: brief section 6 (lock-early
   and growth-first percentiles), B9a (the $204k locked alternative) and B9b (the control runs).

## 9. Sources (all accessed 2026-09-27)

Laura's words (VP via D13a; wording re-checked by D13c):
- Overachiever Magazine, 2021-03-15: https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid
- The Daily Pennsylvanian, 2016-01-28: https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a
- Poets&Quants for Undergrads, 2018-03-30:
  https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/
- The Nerd Daily, 2025-03-08: https://thenerddaily.com/laura-gao-kirbys-lessons-for-falling-in-love-interview/
- Geeks OUT, 2022-05-11: https://www.geeksout.org/2022/05/11/interview-with-creator-laura-gao/
- Pulse Spikes, 2021-06-18: https://pulsespikes.org/story/laura-gao
- Local News Matters, 2026-02-12: https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/
- Input/Inverse, 2022-03-07: https://www.inverse.com/input/culture/laura-gao-messy-roots-viral-tweet-comic-graphic-novel
- NPR, 2020-04-04: https://www.npr.org/sections/goatsandsoda/2020/04/04/823825436/the-wuhan-i-know-a-comic-about-the-city-behind-the-coronavirus-headlines
- HuffPost, 2020-04-29: https://www.huffpost.com/entry/chinese-american-illustrator-life-in-wuhan_n_5ea9c739c5b63115cec2be5a
- Wharton Magazine, 2022-04-06: https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/
- BookWeb (ABA), 2022-02-07: https://www.bookweb.org/news/indies-introduce-qa-laura-gao-1627512
- The Sign.al 5-year page (c. 2022, ASM): https://signaltemp.github.io/
- Her site and documents: https://lauragao.com/rewriting-herstory, https://lauragao.com/the-evolution-of-dance-music,
  https://lauragao.com/s/Laura-Gao-Resume.pdf (PDF created 2024-10-24),
  https://lauragao.com/s/Publicity-and-Speaking-Guide-Laura-Gao-e5n7.pdf (PDF created 2024-03-24),
  https://lauragao.com/s/Educators-Book-Clubs-Guide-Messy-Roots-klc2.pdf (PDF created 2024-03-24)

Other pages read (not her words, or context only):
- The Daily Pennsylvanian, 2019-03-17: https://www.thedp.com/article/2019/03/penn-anti-resume-ocr-recruiting-failure-signal

Repo files (VRF or labelled):
- Case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (p.1 L12, L13-14, L19-20, L25-26,
  L31-33; p.2 L69-74; p.3 L101-103, L110-120).
- IPS guide `2026_WGY_Investment_Policy-FINAL.txt` L123 (R-I55).
- TN guide `2026_WGY_Trading_Notes_Analysis-FINAL.txt` L12, L15-16.
- Competition Guide `2026_WGY_Investment_Competition_Guide.txt` L70, L156-157.
- `SMApply_Deliverables_Page_2026-09-27.md` L49-57 (R-S24 to R-S28).
- `research/insight_v1/phase_D/D13a_laura_quotes_verified.{md,json}`; `phase_B/B8a, B8b, B9a, B9b, B3b`;
  `wins_now/securities_and_allocation_v0.md`; `phase_C/merged_questions.json`; brief sections 6-9 and 14.
- Scripts: `research/insight_v1/scripts/D13c_voice_map_check.py` (new);
  `research/insight_v1/scripts/B10b_designer_checks.py` (re-run).

---

## What this teaches

- **A quote is evidence of a value only when you know the question it answered.** "risk-adverse", "No more gimmicks."
  and "diminishing returns" all mean something narrower on the page than they seem to on their own.
- **Behaviour claims need the person's own words, not a reporter's "So".** The most-repeated Phase B insight ("she
  leaps only after securing a floor") turned out to rest on a journalist's link between two events. Her own words say
  something different, and more interesting: she jumps, she names the cost, and she treats letting down her backers
  as worse than failing herself.
- **A client can hold two risk ideas at once.** A good plan does not pick one of them; it shows which money each idea
  governs. Here that means payments others rely on are bought, and money only she depends on can take the leap.
- **Echoing a client honestly includes saying where you differ.** A plan that holds about 20% stocks in its riskiest
  years must explain itself to someone who tells herself to "take the jump". It should do so with numbers, not
  flattery.
- **Respect is accuracy, privacy and plain words.** The best-fitting "falling" line was private, so it stays out. The
  best tone for a former financial-literacy teacher is the one a classmate could follow.
