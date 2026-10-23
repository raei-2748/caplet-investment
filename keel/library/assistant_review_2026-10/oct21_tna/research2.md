# TNA research, second pass: what judges reward, professional standards, and where the three reflections fall short

Prepared Wed 21 Oct 2026 (Sydney) for Team Caplet. Research and checks only: **no replacement wording** for any note or
reflection. Every gap in section 6 is a requirement (what a fix must achieve), not text.

Builds on `SP/oct21/tna/research/research.md` (cited RES) and does not repeat it. Accuracy errors already logged in
`SP/oct21/tna/factcheck/factcheck.md` (cited FC + row id) are referenced, not re-derived.
SP = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad`.
Page copies: `SP/oct21/tna/research2/web/` (Wharton posts as JSON + text in `web/wp/`, standards in `web/std/`,
searches in `web/search/`). All fetched 21 Oct 2026 with curl, cache-busting `cb=` query; Scribd and some sites needed a
`curl/8.5` user agent. Other teams appear by team and school name only; no student names are copied.

Labels: OFFICIAL (Wharton page or PDF), PRESS/SCHOOL (third-party news), TEAM-DOC (another team's report),
STANDARD (regulator or CFA Institute text), INFERENCE (my reading), UNVERIFIED.

---

## 0. Bottom line

1. **I read every Wharton Global Youth news post from 2019 to 2026 about the competition** (45 posts, list in
   `web/wp/index.txt`; the site uses no tags, so I took the whole "news" category, plus a site search). None of them
   mentions trading notes. What judges praise, across eight seasons, comes down to five things: (i) reasoning behind
   *every* decision; (ii) a clear link from the client's objectives to the strategy; (iii) depth and *accuracy* rather
   than volume; (iv) simple ideas in plain words; (v) discipline in the process together with willingness to adapt
   (sections 1-2).
2. **New finding: a 2024 Global Finalist's trading-notes section is public, and it is weak.** InvestIQ quotes no note,
   calls QQQ "one of the lowest-risk investments" and "almost certain to grow" (section 3). So in the old format the notes
   section did not decide who got through. In 2026-27 the TNA is its own evaluated deliverable and is checked against
   WInS. Do not take past teams' notes as the bar.
3. **Professional standards turn into 12 tests a judge can apply** (section 4). They are CFA Standards V(A), V(B), V(C)
   and III(C), FINRA 2111, FCA COBS 9.4.7, ESMA's suitability Q&A and guidelines, and ASIC RG 90. The four that the
   current reflections fail most often: name the **specific client fact** the decision serves (no generic phrases);
   state the **specific disadvantage** the decision accepts; **separate fact from forecast**; record **what was
   reviewed and decided, even when nothing was traded**.
4. **Against that bar** (section 6), the three reflections are accurate in parts. They lean on product features and
   labels ("root", "branch", "cheap, easy to trade"), and none answers "why this and not the alternative". IBTR has a
   real pre-set test but does not report it. IBTM has the only real refinement, but it is credited to the wrong cause
   and leaves out the rule that changed. VT gives a forecast with the wrong source figure as its reason.

---

## 1. (a) Wharton Global Youth articles, 2019-2026: what judges said they rewarded

Coverage: 45 posts on competition finalists, semifinalists, finales and team stories (list in `web/wp/index.txt`; text in
`web/wp/txt/<id>.txt`). Posts with no evaluative quote are not tabled. These posts contain no comment by a judge
about trading notes (confirmed by grep for "note"). The table holds only quotes that RES does not already have
(RES §3 has Jain 2025, Ko Hahn's first sentence, the 2023 advisor and champion quotes, the 2021 tips blog and
Manetta 2019).

| # | Who (role), event | Quote (30 words or fewer) | URL, date | Bears on |
|---|---|---|---|---|
| W1 | Matthew Carlone, Region 3 finale judge | "focus on forward-looking company performance, rather than on the performance for the last 10 years" | https://globalyouth.wharton.upenn.edu/news/2019-investment-competition-region-3-finale-features-yeti-whole-lot-talent/ (21 Mar 2019) | Forward reasons, not past returns |
| W2 | Wharton write-up, Region 2 finale (NSE, India) | "their creative and thoughtful investment strategy themes – and how they expressed them – were often a key differentiator" | https://globalyouth.wharton.upenn.edu/news/kwhs-region-2-investment-competition-finals-national-stock-exchange/ (28 Feb 2019) | Expression matters, not only the analysis |
| W3 | Same post, on the 3rd-place team | "extensive research and deep understanding of its client's needs really elevated the effectiveness of its teams strategy" | same | Research + client |
| W4 | Wharton evaluators, regional finalists 2019-20 | Looked for "a deep understanding of the investment competition client ... clear and creative strategies; and extensive analysis and teamwork" | https://globalyouth.wharton.upenn.edu/news/announcing-the-regional-finalists-for-our-2019-2020-investment-competition/ (27 Jan 2020; `6109.txt:7`) | What readers of written reports scored |
| W5 | Thomas Luddy (ex-J.P. Morgan), 2020 finale judge | "the field of finance is not just about making money; it's about helping people achieve goals that they want to achieve in life" | https://globalyouth.wharton.upenn.edu/news/2020-investment-competition-global-finale-ends-tie-first-place/ (11 May 2020) | Goals, not returns |
| W6 | Jeanette Ourada (ex-Chevron), Region 3 judge | "You all did a very good job demonstrating the financial knowledge that you learned through the course of the competition." | https://globalyouth.wharton.upenn.edu/news/2020-top-3-region-3-wharton-investment-teams/ (14 Apr 2020) | Visible learning |
| W7 | Virgilio Aquino (Aberdeen), 2021 finale judge | "Advice from my seat in investing: maintain the discipline of your investment process and be flexible when things don't work out." | https://globalyouth.wharton.upenn.edu/news/mr-investments-first-place-2021-investment-competition/ (11 May 2021) | **"Tested" and "refined"**: discipline, then adapt |
| W8 | BTG Pactual partner, 2021 Region 4 | "discipline should be key to systematically being in the finals" | https://globalyouth.wharton.upenn.edu/news/regional-winners-wharton-global_youth_2020-2021-investment-competition/ (26 Mar 2021) | Process discipline |
| W9 | Dan Young (Wharton Alt-Finance), 2022 semifinal judge | "The level of analysis of understanding for Nichole Jordan's situation was top-notch." | https://globalyouth.wharton.upenn.edu/news/announcing-the-top-10-teams-advancing-to-our-2022-investment-competition-grand-finale/ (18 Mar 2022) | Client situation |
| W10 | Shawn Snyder (Citi), 2022 semifinal judge | "The competition requires students to focus on quality control, the client experience, presentation skills, and teamwork." | same | **Quality control** (accuracy) |
| W11 | Joshua Tam (Laurel Avenue), 2024 semifinal judge | "The one thing that stood out to me was the ability to connect the client's objectives to an investment strategy." | https://globalyouth.wharton.upenn.edu/news/wharton-global-youth-hosts-five-virtual-events-to-announce-the-2024-investment-competition-finalists/ (25 Mar 2024) | Client to strategy link |
| W12 | Jeanette Ourada, 2024 semifinal judge | "Your creative videos demonstrated your client focus and financial knowledge." | same | Client focus |
| W13 | Vikas Keswani (HPS), 2024 finale judge | "a lot of depth and accuracy. That is one of the things that in my mind differentiated better performances." | https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/ (23 Apr 2024) | **Accuracy** over volume |
| W14 | Zoe McCormick (abrdn fixed income), same finale | "When analyzing someone's investments, take a look at this person holistically" | same | Whole client, whole portfolio |
| W15 | Melissa Ko Hahn (Covepoint), 2025 semifinal judge (second half of the quote RES cites) | "Oftentimes, the best solutions are made up of simple, elegant ideas." | https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/ (24 Mar 2025) | Simplicity |
| W16 | Muk Rao (WRDS), long-time finale judge, 2025 | Urged students "to see the power of defending their ideas"; "you're better at advancing really complex arguments" | https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/ (1 May 2025) | Defend each decision |
| W17 | Wharton, 2026 Top 50 announcement | Selection used "Wharton School student evaluators, as well as a professional review panel of asset managers from Aberdeen Investments" | https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/ (27 Jan 2026) | **Who reads**: students first, then asset managers (INFERENCE: write for a smart non-specialist, and be exact for a professional) |
| W18 | Wharton, 2026 champions post | "Each team demonstrated exceptional analytical thinking, creativity, and a deep understanding of their client's goals." | https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/ (30 Apr 2026) | Same three themes |

Two OFFICIAL guidance pages not used in RES:
- "Developing a Strategy" (guidebook page, modified 16 Nov 2020; https://globalyouth.wharton.upenn.edu/developing-strategy/,
  `web/wp/pg_1442.txt`): "Evaluators want to understand why you are doing what you are doing". Also "Can you tweak it?
  Absolutely!" (the strategy). Also "Will certain triggers dictate ..." is in the 2023-24 feedback PDF (RES §2).
- Old FAQ (page 3780, `web/wp/pg_3780.txt:86`): "Winners are selected on the strength and articulation of their overall
  investment strategies and competition experiences, not on the percentage growth of their portfolios".

**What the articles add up to (INFERENCE, from 18 quotes over 8 seasons).** The client-to-strategy link comes up 6 times
(W3, W4, W5, W9, W11, W14). Reasoning and defending decisions comes up 3 times (W16, plus Jain 2025 and Manetta 2019 in
RES). Accuracy and quality control come up twice (W10, W13). Simplicity and plain words come up twice (W15, plus
Vittorelli 2022 in RES). Discipline together with flexibility comes up twice (W7, W8). Forward-looking reasons instead of
past returns come up once (W1). No judge praises a metaphor, a label or a feature list.

---

## 2. (b) Other public advice: school pages, press, advisors, past finalists

| # | Source (type) | What it says (quote of 30 words or fewer, or a fact) | URL, date | Reliability |
|---|---|---|---|---|
| P1 | Westminster School news (SCHOOL): Hooke Investments, **2026 Global Finalist** | "highly commended for the depth of their research, presentation skills, and capacity to adapt and pivot investment classes as they adjusted their strategy to changing economic conditions" | https://www.westminster.org.uk/news-hub/westminster-school/westminster-school-economists-pitch-their-way-to-the-final-of-global-investment-challenge/ (6 May 2026) | Medium. School paraphrase of the judges; "highly commended" by whom is not stated |
| P2 | Same page, a team member | "we had to build a coherent strategy and constantly refine it" | same | Medium |
| P3 | People Newspapers (PRESS): Liberty Capital, Parish Episcopal, **2026 Top 50**. Advisor's method | Advisor asked the team "to explain the team's strategy as if I were a fourth grader", then "pressed with questions ranging from the math to the ethical considerations" | https://www.peoplenewspapers.com/?p=314379 (8 May 2026) | Medium. A real Top 50 team's process |
| P4 | KXAN (PRESS): Vandegrift's "The Compounders", **2026 Top 50** (not on the 11-team finalist list) | Their model showed "a 70% chance of reaching the long-term goal, a number the students initially questioned until realizing that professionals rarely achieve higher odds without taking on substantial risk" | https://digital-release.kxan.com/news/local/austin/all-female-vandegrift-team-advances-to-wharton-global-high-school-investment-competition/ (22 Mar 2026) | Medium. Shows calibrated, honest odds |
| P5 | Same | Lesson: "not to get attached to any one idea or sector" | same | Medium |
| P6 | Gregory School (SCHOOL): Gregory Quant Capital, **2026 Top 50** (on the W17 list) | They wrote code to score S&P 500 stocks on "how they aligned with those of the client"; semifinalists also answered written questions and had a "virtual interview" | https://gregoryschool.org/news-and-events/tgs-team-advances-in-wharton-global-high-school-investment-competition (early 2026: mentions a 9 Feb video; exact date not in the copy) | Medium |
| P7 | Wharton School story (OFFICIAL, wharton.upenn.edu), 2026 finale | Restates the Global Youth post; no judge quotes | https://www.wharton.upenn.edu/story/wharton-global-high-school-investment-competition-hosts-future-business-leaders/ (2026) | High, but empty |
| P8 | Regis HS (SCHOOL), 2020-21 regional finalist | Chosen "for the strength and creativity of their investment strategies"; "judged based on your investment strategy" | https://regis.org/article?id=11551 (Jan 2021) | Low (no new criterion) |
| P9 | Brisbane State High School (SCHOOL): Gryphon Group, 2020-21, the last Australian Top 50 team found | Fact only: Top 50 from 972 reports; no method given | https://brisbaneshs.eq.edu.au/our-school/student-achievements/global-investment-competition | Low |

Searched and found nothing usable:
- LinkedIn articles by judges or past finalists (WebSearch: none).
- A finalist's Medium post (https://abhinav-penagalapati.medium.com/..., HTTP 403 every time).
- YouTube descriptions (watch pages return HTTP 429, as on 20 Oct).
- Wharton "Meet the Experts" pages (webinar topics only, no notes advice).
- The 2018 finale post (`web/dca.txt`, praise only).
- Stuyvesant, Perse, Farmington, BB&N and other 2026 finalists' school pages (WebSearch found no articles).

---

## 3. (c) Publicly posted past team reports: what their decision write-ups did

RES §4 covers Mochi, Sharks, Profit Gurus, Capstone, Chennai Tuskers, Dynamites and Caplet 2025-26. New here:

| # | Item | Year, result | What its trading-note / decision write-up did | Lesson for a 2026-27 judge's test |
|---|---|---|---|---|
| C1 | **InvestIQ Final Report**, "Trading notes analysis" (Scribd 1032186432; `web/scribd_1032186432.txt:59-81`) | 2023-24 (Hilary Ash case). **2024 Top 50 and Global Finalist** (Wharton lists, verified 20 Oct: `oct20/verify_pw/verify_pw.md:31`) | Two write-ups, stock and ETF, about 120 words each. **No note quoted.** The stock write-up states the client goal it serves (women's sport). It records that **the team disagreed** about the stock because of competitors, and how that was settled; it gives an allocation number (62% of the consumer-staples sleeve). The ETF write-up relies on overclaims ("one of the lowest-risk investments", "almost certain to grow") and a past-growth story | It reached the finale in spite of this section. So an old-format notes section was not decisive (INFERENCE). The one good move to note: a **recorded disagreement and how it was settled**. That counts as "tested" evidence under the 2026-27 wording |
| C2 | 2025-26 Welcome Email (OFFICIAL-COPY, Scribd 933222558; `web/scribd_933222558.txt`) | 2025-26 | No trading-notes instructions in the email | Confirms RES §6: the 2025-26 notes instructions are still NOT FOUND |
| C3 | GitHub, Google Sites, Issuu | any | GitHub search through the API is blocked in this session (403). Web search with `site:github.com` and `site:sites.google.com` returned no team reports | None found. 2026-27 Laura Gao repositories were deliberately not opened (as on 20 Oct) |

Overall (INFERENCE): of the two public reports from teams that made a cut (Mochi 2024 Top 50; InvestIQ 2024 finalist),
one has a strong notes section and one a weak one. Public evidence cannot show what a Top-50 TNA looks like in the
2026-27 format. The official text (RES §1) and the professional standards (section 4) are the safer guide.

---

## 4. (d) Professional standards for documenting an investment decision, turned into judge criteria

| Standard (STANDARD) | Key text (30 words or fewer) | Source, copy |
|---|---|---|
| CFA Standard V(A) Diligence and Reasonable Basis | "Have a reasonable and adequate basis, supported by appropriate research and investigation, for any investment analysis, recommendation, or action." Also "consider and address all pertinent issues" | https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a (`web/std/cfa_va.txt:114, :120`) |
| CFA V(A), models | Analysis "that fails to consider potentially negative outcomes or levels of risk outside the norm may not accurately measure the true economic value" | `cfa_va.txt:146` |
| CFA Standard V(B) Communication with Clients | "Distinguish between fact and opinion in the presentation of investment analysis and recommendations." "Disclose ... significant limitations and risks" | https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-b (`cfa_vb.txt:115, :117`) |
| CFA V(B), guidance | "Members and candidates must use caution when promoting the perceived accuracy of any model or process" | `cfa_vb.txt:145` |
| CFA Standard V(C) Record Retention | "retain records that substantiate the scope of their research and reasons for their actions" and this "applies to decisions to buy or sell ... as well as reviews undertaken that do not lead to a change in position" | https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-c (`cfa_vc.txt:115`) |
| CFA Standard III(C) Suitability | "Judge the suitability of investments in the context of the client's total portfolio"; consistent with "written objectives, mandates, and constraints" | https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-iii-c (`cfa_iiic.txt:114-115`) |
| FINRA Rule 2111, Supplementary .05 | Three duties: "reasonable-basis suitability, customer-specific suitability, and quantitative suitability". Quantitative: a series of trades "even if suitable when viewed in isolation" must not be unsuitable "taken together" | https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111 (`finra_2111.txt:156-159`) |
| FCA COBS 9.4.7R (UK suitability report) | Must "explain why the firm has concluded that the recommended transaction is suitable" and "explain any possible disadvantages of the transaction for the client" | https://handbook.fca.org.uk/handbook/COBS/9/4.html (`fca_cobs94.txt:130-131`) |
| ESMA MiFID II Q&A, ch. 2 Q10 (28 Mar 2019) | Firms "should state on an individualized basis how the recommendation given is suitable", and should "refer ... to the relevant client information that was used" | https://www.esma.europa.eu/publications-data/questions-answers/1765 (`esma_qa1765.txt:144-145`) |
| Same | Avoid "general statements such as 'the recommended product is suitable because it matches your risk tolerance'" | `esma_qa1765.txt:146` |
| ESMA Guidelines on suitability (ESMA35-43-3172), GL 9 and 10 | "a thorough assessment of the possible investment alternatives is undertaken"; for a switch, "an assessment of the advantages and disadvantages of the new investment(s)" | `web/std/esma_gl3172.txt` (pp. 28-30), copy from https://prod.finanssivalvonta.fi/globalassets/en/publications/supervision-releases/2023/esma35-43-3172_guidelines_on_certain_aspects_of_the_mifid_ii_suitability_requirements.pdf |
| ASIC RG 90, Example Statement of Advice (Australia, Aug 2005) | An SOA must contain "information about the basis on which the advice is or was given" (s947B(2)(b)). On risks: "We have deliberately not included generic information about risk ... We have tailored the information to the particular clients" | https://download.asic.gov.au/media/1337456/Example_SOA_guide.pdf (`asic_example_soa.txt`, pp. 6, 13) |

**Criteria a judge would apply to one 100-word reflection** (each is a yes/no check; J-numbers are used in section 6):

| # | Test | From |
|---|---|---|
| J1 | **Individualised:** names the specific case fact the decision serves (a date, an amount, a constraint), not "her goals" or "certainty" in general | ESMA Q10; W11, W14; TNA:46-52 |
| J2 | **Role in the whole portfolio:** says what job this holding does that the others do not | CFA III(C); FINRA quantitative; TNA:14-15 |
| J3 | **Reasonable basis:** names the check or research done *before* the trade (and its source) | CFA V(A); Guide:84-86; W3 |
| J4 | **Alternative rejected:** names one real alternative and the reason it lost | ESMA GL 9; advisor "Why not buy the competitor?" (RES §3) |
| J5 | **Specific disadvantage:** the cost or risk *this* decision accepts, sized if possible, not a generic risk | FCA COBS 9.4.7(3); ASIC RG 90 p.13; CFA V(B); TNA example note "although ..." |
| J6 | **Fact vs forecast:** forecasts are labelled as assumptions, with the right source and basis, and match the IPS | CFA V(B); W1; W13 |
| J7 | **Tested:** states a test or trigger set in advance, what was observed (with a date) and what was decided, including "held" | CFA V(C) "reviews that do not lead to a change"; W7; "triggers" (RES §2) |
| J8 | **Refined:** states what changed, when, the true cause, and the rule that now applies | TNA:12, :29; P1, P2; W7 |
| J9 | **Calibrated:** no promise or certainty the instruments do not give; honest odds | Case:114; CFA V(B) caution on models; P4 |
| J10 | **Plain and simple:** no label that needs explaining, no feature list standing in for a reason | W15; P3; judging page (RES §2) |
| J11 | **Consistent:** same numbers, same roles and same sequence as IPS V5 and the note itself | Case:161; deliverables "maintains consistency with the team's IPS" (`smapply_public_2026-10-14/deliverables.txt:55`) |
| J12 | **Not performance:** no gain, loss or ranking language | TNA:15-16; Guide:74-78 |

---

## 5. How the evidence ranks these tests (INFERENCE)

- **Most weight:** J1, J2, J11. They come from the official 2026-27 text plus six judge quotes, and the three deliverables
  are read together.
- **Second:** J7 and J8. "Tested" and "refined" are the official 2026-27 wording; two judges (W7, W8) and a 2026
  finalist's school (P1) single out discipline together with adapting.
- **Third:** J5, J6, J9. Accuracy and honesty (W10, W13, P4, the case's overpromising warning). An Aberdeen asset
  manager on the panel (W17) will notice a wrong number or a fund described as a bond.
- **Hygiene:** J10, J12, J3, J4. Cheap to get right; costly when missed.

---

## 6. Where each current reflection falls short (section A of `current_draft_21Oct.md`), as requirements

Word counts from FC §1: IBTM 94, VT 99, IBTR 99. **A fix that adds words must cut the same number elsewhere.**

### 6.1 IBTM (`current_draft_21Oct.md:10`). The set's "refined" decision

| Test | Shortfall | Requirement for the fix |
|---|---|---|
| J8 | The refinement is credited to the 6 Oct email, but IBTM was already the WInS stand-in on 29 Sep (FC M4). The reflection never says which rule changed as a result | Give the true sequence: what the real plan was, what the email removed, what was already in WInS. Then name the one rule that changed in Laura's plan (the floor is quoted rounded down because the payout is not fixed, IPS V5 ¶5) |
| J5, J9 | The note says "the final payout is not fixed". The reflection says the opposite three times ("clear yield", "matures on a set date", "a stock crash will not make her promise fail") (FC M8, M9, M11) | State the specific disadvantage of using a fund as the floor, and how the plan handles it. Remove every promise-style claim. The case warns overpromising "could damage her credibility" (case:114) |
| J4 | "the best alternative" gives no criterion and no rival | Name the rejected option(s): no individual 2032 Treasury listed in WInS (FC M5), and STRIPS banned. Give the one test IBTM passed |
| J10 | "root of our strategy", "ground a minimum", and a list of features ("cheap, easy to trade, has a clear yield") stand in for reasons | Every feature kept must be tied to a job for Laura. Otherwise cut it. If the metaphor stays, use it exactly as the other two reflections and the pitch do (FC M12) |
| J1, J11 | "Laura's second deposit buys a second batch": the real-plan sequence is stated as if it were the WInS trade (WInS bought one lot, FC M10) | Make clear once whether the sentence describes Laura's real plan (IPS V5 ¶3) or the WInS trade |
| J3 | No check is named | Name the check that backed the trade: the WInS bond list, or the iShares termination terms. One clause |

### 6.2 VT (`current_draft_21Oct.md:15`). Should be the clean "supported" decision

| Test | Shortfall | Requirement for the fix |
|---|---|---|
| J6, J11 | The reason given is a forecast, and it uses the wrong figure: "about 7.5% a year per JPMorgan" is the EAFE row; world stocks are 7.00%, and IPS V5 assumes 7% (FC V5) | Either drop the forecast, or use the IPS figure, its source and its basis, and say it is an assumption. The role should come before any return number |
| J2, J11 | It contradicts its own note. The note says stocks "only set how far her gift rises", but the reflection also has Laura's half "covering a payment shortfall" (FC V8). "kept small since we prioritise certainty" leaves out that VT is what remains after the payments *and* the floor are bought (FC V3; IPS "payments, then the floor, then growth") | Give one job, matching the note and IPS V5 ¶3-5. Give the sizing reason as the sequence rule, not as a feeling |
| J4 | "without costly (and risky) stock picking" names no real rival | Name one specific alternative a judge would ask about (for example a single-country index fund) and the one reason, tied to Laura, that VT beat it |
| J5 | The reflection names no downside. The note's "a fall can shrink the extra" is not developed | Give the one disadvantage in Laura's terms. IPS V5 ¶5 already has a sized case (a 40% fall during 2032 moves a typical contribution from about $169k to $162k, and no payment changes); use the same number or none |
| J1 | No case fact about her risk attitude is used | Tie the small equity share to a named trait in the case (capacity vs. willingness, or the 2028 deposit depending on her income; IPS V5 ¶2) |
| J9, J6 | "Expected return ... can raise the upper bound" gets the mechanism wrong: the bound uses VT's 2031 *value* (FC V6) | Describe the rule as the IPS does |
| J10 | "branch", the parenthetical, and "9% of the portfolio" with no basis (WInS 9% vs about 7% in the real plan) | One plain sentence on the role. Every percentage states which book it refers to |
| Format | The label "Reflection (Ray):" | Paste only the reflection text (FC §1) |

### 6.3 IBTR (`current_draft_21Oct.md:20`). The set's "tested" decision, and its strongest

| Test | Shortfall | Requirement for the fix |
|---|---|---|
| J7 | The note set a test in advance (yields falling more than about 0.2 points by January). The reflection only repeats the rule. It does not say what was observed or what was decided | Report the test. Give the trigger, what was observed with a date and stated basis (the teardown has the 19 Oct figures, `TNA_Teardown_21Oct2026.md` item 4), the decision (held, or acted), and why the rule made that decision. CFA V(C) treats "no change" as a decision that needs a record |
| J6 | False and checkable statements: "2036 Treasuries that mature in December 2036" (FC R1); "held to maturity" said of a fund; "from 2042 backwards" does not match the order times (FC R5) | Every statement about the instrument and the order must match iShares and the WInS times. Keep plan-order claims (IPS V5 ¶3) separate from what happened in WInS |
| J9 | It says the buying order "serves her operating commitment 'with a high degree of certainty'". The order of purchases does not create the certainty (FC R7) | Use the IPS definition of certainty (each payment covered by a maturity shortly before it). Do not quote the case phrase as if the trade achieved it |
| J4 | The reason for the split (iBond ETFs for payments 1-5, individual bonds for 6-10) is not given | One clause: what WInS lacked, which forced the split (FC M5) |
| J5 | The disadvantage is named but not sized | Either give one size from the numbers register with its basis and date, or leave it qualitative. Do not size the facility contribution (out of scope, TNA:20-22) |
| J10 | "a 'root' of our strategy", used differently from IBTM | The label is used the same way in all three, or dropped |

### 6.4 The set as a whole

| Test | Shortfall | Requirement |
|---|---|---|
| J7/J8 + TNA:29 | The verbs are implicit. A reader has to work out that VT supported, IBTM refined and IBTR tested | Make each reflection's verb unmistakable from its content (an event, a test, a rule), not by labelling it |
| J2, J11 | No reflection says once that WInS holds Laura's post-2028 plan scaled to $300k | One clause somewhere in the set, the same wording of fact as the IPS |
| TNA:4-6 | Liquidity, one of the six dimensions Wharton names, is never mentioned (teardown item 10) | One clause, in IBTR or IBTM, on maturities rather than sales funding payments (IPS V5 ¶4) |
| J12 | Passes: no performance language | Keep it that way |
| J10 | The labels, plus "operating commitment", "facility contribution" and "floor", all appear in under 300 words | Read the three aloud to a non-investor (the P3 method). Any term they cannot restate gets cut or explained |

---

## 7. UNVERIFIED, blocked or not found

- **No Wharton judge comment on trading notes in any of the 45 posts (2019-2026).** Absence confirmed by text search.
- YouTube video descriptions and transcripts: HTTP 429 (blocked). Medium finalist post: HTTP 403. GitHub search API:
  blocked in this session. austlii (Corporations Act s947B/s961B) and ASIC RG 175 (2024 PDF): 403/404. s947B is
  quoted from ASIC's RG 90 instead. EUR-Lex MiFID II Delegated Regulation: no text returned.
- Two old Wharton pages are now private (HTTP 401), so their wording is UNVERIFIED: 1448 (old "Competition
  Deliverables") and 16668. A search snippet of one says notes must detail a trade's "strategic purpose".
- The Gregory School article's exact date (early 2026).
- Whether Hooke's "highly commended ... adapt and pivot" (P1) is the judges' wording or the school's.
- Who reads the TNA, and its weight in the Top 50 cut. W17 describes the 2025-26 Final Report readers only.
- The ESMA and FCA texts are EU/UK retail-advice rules, used here only as a model of good practice. They do not apply to
  the competition. The CFA Standards are the closest fit to an Aberdeen asset-manager reader (INFERENCE).

## 8. Files
- `web/wp/` holds the post JSON (`news_p1-2.json`, `srch_p1.json`), the index (`index.txt`), the post texts
  (`txt/<id>.txt`) and the pages (`pg_<id>.txt`).
- `web/std/` holds cfa_va, cfa_vb, cfa_vc, cfa_iiic, finra_2111, finra_2090, fca_cobs94, esma_qa1765, esma_gl3172 (.pdf/.txt),
  asic_soa and asic_example_soa (.pdf/.txt).
- `web/` holds the school and press pages (westminster, parish, kxan, gregory, regis, brisbane, uwc, dca, whstory) and
  the Scribd copies (1032186432 InvestIQ, 933222558, 979966514).
- Tools: `tools/get.sh`, `tools/split.py`, `tools/pdf2txt.py`, `tools/bs.sh`, `tools/ddg.sh` (DDG returned a captcha).
