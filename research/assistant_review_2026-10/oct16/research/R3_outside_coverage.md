# R3: What past winners, finalists and semifinalists did (sources outside Wharton's own site)

Prepared 16 Oct 2026 (Sydney) for Team Caplet. This is research only. It drafts no deliverable text.

**Scope.** The question: what did past winning, finalist and semifinalist teams actually do? I used sources outside
`globalyouth.wharton.upenn.edu`: school news pages, student newspapers, local and national news (Brazil, Czechia,
UK, US, Australia), sponsor press releases, public GitHub repositories, YouTube titles, a Medium post, prep-guide
sites and a LinkedIn post. Wharton's own pages are covered by the sibling report R1
(`oct16/research/R1_wharton_archive.md`). I cite those pages only to confirm a team's placing.

**Method.** Each page was fetched on **16 Oct 2026**. Its visible text is saved in `oct16/research/R3_pages/<file>.txt`,
with the URL and access date at the top. Public code was read but never run; it sits in `R3_pages/github/`. Tags like
**[O6]** point to the source list in section 8. Foreign-language quotes are my own translations; the original words
follow in brackets where they matter.

**Labels.** **FACT** = stated on the cited page. **SCHOOL CLAIM** = a school or newspaper praising its own team (not
checked by Wharton). **OPINION** = someone's view. **INFERENCE** = my reading of the evidence. **UNVERIFIED** = I could
not confirm it.

**Privacy.** Students from other schools appear only by team and school. Teachers, judges and staff appear by role
only. Several saved raw pages contain full names. Do not copy those names into team files.

**Could not reach.** Reddit (blocked: HTTP 403, and the PullPush archive returned 429). YouTube video pages and
descriptions (Google returned 429, and the player API said "LOGIN_REQUIRED"), so I have titles only, via oEmbed.
Medium (403; I got the post through its RSS feed instead). LinkedIn profiles (HTTP 999). Also blocked: the
Harvard-Westlake and Palos Verdes student papers (Cloudflare 1006/403), the ACP Knight Times (connection reset),
KXAN and Yahoo (429), Chandler News and Ahwatukee (429), Chicago Parent (403) and Amity Noida's site (502). One
competitor repo the team cites can no longer be reached at all (section 5).

---

## 0. Bottom line

1. **No winning strategy is public outside Wharton.** For FigCapital, BAM Investing, Spark Investments, DMV's
   Finest, Sailing to Success and M&R Investments I found no published asset mix, report or deck. Outside coverage of
   the champions is a line or two at most [O1]. The richest outside accounts come from runners-up and finalists:
   Marista Brasília, Westminster, Staples, Amity Regional and Nový PORG. Copying a winner is impossible as well as
   banned ("plagiarize existing strategies", Wharton Rules & Roles [W1]).
2. **The trait seen most often: start from the client's goal and work backwards.** A 2022-23 finalist said it
   outright [O33]. Staples (2nd, 2024) said "It was personal first" [O17]. Amity Regional (2nd, 2023) wrote code
   counting how many years the client's yearly gift could be paid at each risk level (in the repo's 2022-23 folder)
   [O19]. Vandegrift (Top 50, 2026)
   reported a probability of reaching the client's goal (search snippet only, UNVERIFIED) [O16].
3. **Top teams wrapped the plan in a frame from the client's own world.** Examples: "7 Chakras" for a client who
   wanted a yoga centre [O18]; Spark's "Ignite the flame" for an Olympics client (Wharton tagline, via R1); a
   soccer-kick close for a sports-loving client [O17]; football-themed team names and a field-goal video for an NFL
   client [O14][W7]. INFERENCE: the frame helped people remember and explain the plan. It did not pick the stocks.
4. **Custom quant tools are normal among strong teams, so on their own they do not stand out.** Marista built its
   own scoring model "based on Markowitz" [O5]. Westminster wrote a Python program for real-time data [O11]. Hotchkiss
   built a 9-phase pipeline with Monte Carlo and COVID stress tests, but stopped at the Top 50 [O15][W7].
5. **Teams that win usually come back.** DMV's Finest reached the finale in 2022 without placing and won in 2023
   (R1). Nový PORG first entered in 2019-20, took bronze in 2023 [O23] and has made every Top 50 from 2023 to 2026
   [W3-W7]. Staples placed 2nd in only the team's second year [O17]. Stuyvesant had 13 teams registered in 2023-24 [O2].
6. **They started early and prepared for a long time.** Marista: 7 months of preparation plus 8 of competition, "15
   months" in all [O6]. Haverford: "seven months" to build the report [O26]. Miramonte started the summer before
   [O39]. Westminster went "from an idea last summer" [O11].
7. **They rehearsed on outside adults, within the rules.** Nový PORG talked "tactics before the final" with bank
   professionals and pitched to the Prague Stock Exchange's director [O20][O22]. Parish's writing teacher made the
   team explain the strategy "as if I were a fourth grader" [O14]. Parents working in finance ran Q&A sessions for
   UWCSEA teams [O42]. Wharton allows an unpaid "secondary advisor" (a parent or industry professional) but bans paid
   help and outside courses that claim to teach the competition [W1].
8. **Age and team size were no barrier.** The 2024 Harker finalists were ninth graders [O27]. Westminster's 2026
   finalists were the only Year 11 team [O11]. Marista placed 2nd in 2026 with four members [O5].
9. **Outside reports on what judges valued agree with Wharton's own reports.** An abrdn semifinal judge (2024)
   praised teams that looked beyond the client's goals to "the client's personal values" [O29]. The 2026 press release
   said portfolios are judged on fit "to a client's goals, values, and risk tolerance rather than short-term market
   performance" [O13]. Westminster was "highly commended" for research depth, presentation and "capacity to adapt and
   pivot" as conditions changed (SCHOOL CLAIM) [O11].
10. **Australia has been absent since 2022.** Brisbane State High's "Gryphon Group" reached the 2021 regional finals,
    as "the only team in Australia" [O41], and the 2022 Top 50 [W2]. No Australian school is on the 2023-2026 Top 50
    lists [W3-W7]. Kristin School (New Zealand) made the top 50 in 2021, 2022 and 2023 [W10][W2][W3].

---

## 1. Source quality, briefly

- **Hard facts** used here: placings confirmed on Wharton lists (via R1's saved pages); dates; numbers stated by
  schools (team size, months of preparation, meeting schedule); code that actually exists on GitHub.
- **Soft facts** (SCHOOL CLAIM): what a school says judges praised; "firsts" claimed by national media. Three
  "firsts" turned out to be wrong (section 4.3), so treat every media superlative as UNVERIFIED.
- **Commercial guides** (Young Founders Lab, International Finance Academy, ABC Money, Aralia, Lumiere) are OPINION.
  Some of what they say about Wharton is wrong. Young Founders Lab says the Wharton archive "shares the strategies of
  previous top teams" [O50], but R1 found the archive lists names and placings, not strategies.

---

## 2. Per-team notes

Placings are confirmed against Wharton's lists (R1 pages, cited as [W#]; the archive [W11] gives the top three
for each year). "Outside sources" lists what I found
beyond Wharton.

### 2.1 2025-26 (client Connor Barwin; $500,000 virtual cash)

**FigCapital, Stuyvesant HS, New York: 1st** [W11]
- Outside sources: Stuyvesant blog, 2 May 2026 [O1]; ABC Money [O49].
- FACT: six students; "one of eleven teams invited to present at the finals ... placed 1st overall"; "nearly 6,000
  teams competed" (school's figure) [O1]. A second Stuyvesant team, Keystone Capital, also made the Top 50 [W7][O49].
- Strategy, presentation, judges' comments: **not found.** The Stuyvesant Spectator's site search returned nothing
  on the competition.
- Background FACT: Stuyvesant's "Big Apple Investments" reached the 2024 finale [O2][W5]. Two helpers (one a
  senior student) "helped with their video deliverables" [O2]. Thirteen Stuyvesant teams registered that year [O2].

**HHA Investments, Colégio Marista de Brasília, Brazil: 2nd** [W11]. This is the best-documented 2026 finalist.
- Outside sources: Correio Braziliense, Mar 2026 ×2, Apr 2026 and Sep 2026 [O4-O7]; Blog do Amarildo ×2 [O8][O9];
  Jornal de Brasília [O10].
- **Team:** four students, aged 16-17. The leader found the competition online and invited friends. They said
  having only four members put them at a disadvantage ("Ficamos bem desfavorecidos ... por ter menos membros") [O5].
- **Preparation (FACT, school's figures):** began in April 2025, "months before the official start", with an
  entrepreneurship teacher as mentor and an English teacher helping with technical English [O8]. "The competition
  lasted eight months, not counting the other seven of preparation ... 15 months dedicated to Wharton" [O6].
- **How they prepared:** "We started researching teams from past editions". Their strategy was inspired by "an
  Indian team that had been a finalist in previous editions" [O5]. INFERENCE: they studied past teams' patterns; how
  much they borrowed is unknown.
- **Strategy (FACT, as reported):** chose "which companies, sectors and countries" suited the client. The client's
  stated concern for the environment shaped their choices [O5]. Their "differentiator" was their own "artificial
  intelligence model": a formula, "based on the models of Harry Markowitz", that scores each company on public
  numbers such as profit and debt, then sets how much to invest, with a 10-year view [O5][O9]. INFERENCE: this reads
  like a factor-scoring screen plus mean-variance weights, which a newspaper called "AI". Its exact method is
  UNVERIFIED.
- **Presentation:** semifinal "by video", in which "all members took part in the explanation and told their
  experiences" [O5]. Before the final they planned "to train a lot to replicate the video we presented, now in
  person" [O5]. The final was a 10-minute pitch on day 2, after a Learning Day on day 1 [O6].
- **After the competition:** they set up a school finance club and then the free "Brasília Finance Challenge" for
  students (5-page report, 8-minute final pitch to professionals) [O6][O7].
- **Mistakes mentioned:** "When we started we knew practically nothing about finance ... we learned a lot on the
  job" [O7].

**Riverhawk Traders, Farmington HS, Connecticut: 3rd** [W11] (the archive spells it "Riverhawk Trades")
- Outside sources: none loadable. A search snippet of a team member's LinkedIn post says "3rd out of 6,300+ teams"
  and mentions a "macroeconomic strategy". UNVERIFIED; the page was not loadable.

**Other 2026 finalists with outside coverage** (all 11 finalists are listed in [W7])
- **Hooke Investments, Westminster School, London** [O11] (school news, 6 May 2026):
  - FACT: five Year 11 (GCSE) pupils, "the only Year 11 team amongst a field of sixth formers"; flew to the
    final in person.
  - SCHOOL CLAIM about the case: the task was to grow the client's holdings "to $1.5 million by 2036 and to
    generate a regular, steady income for the Foundation". UNVERIFIED against the case, which is not public (R1).
  - Strategy (teacher's account): "a programme in Python to take real-time data and interrogate it, allowing them
    to adopt an interventionist investment strategy".
  - Roles: some members on data, some on the quantitative side, "the final group worked on the presentations".
  - SCHOOL CLAIM: "highly commended for the depth of their research, presentation skills, and capacity to adapt and
    pivot investment classes as they adjusted their strategy to changing economic conditions."
  - A student: "It's not about being the best; it's about selling yourself and your work with indisputable
    confidence and enthusiasm."
- **Perse Capital Group, The Perse School, Cambridge** [O12]:
  - FACT: six pupils; Learning Day on day 1 (lectures by the Dean and Vice Dean).
  - The final was "a confident and professional presentation under pressure, responding thoughtfully to judges'
    questions". No strategy detail.
- **End Zone Equity, Ramaz School, New York** [O13]: six juniors. Their joint statement was about financial-literacy
  workshops and "student-to-student mentorship" for underserved students. INFERENCE: this echoes the client's
  community mission.

**2026 semifinalists with outside coverage**
- **Liberty Capital, Parish Episcopal, Texas** [O14]:
  - The club began in 2023 and grew to three teams. The team "refined their strategy in the school's Writing Lab".
  - The writing teacher: "I routinely asked (Daniel) to explain the team's strategy as if I were a fourth grader ...
    I pressed with questions ranging from the math to the ethical considerations."
  - They filmed their video on the football field (NFL client), after a "near all-nighter".
- **The Compounders, Vandegrift HS, Texas** [O16]:
  - KXAN's headline said "headed to global finals". **Wrong:** Wharton lists them in the Top 50, not the 11
    finalists [W7].
  - Search snippet only (page blocked, UNVERIFIED): a screen of U.S. securities for growth, low volatility and fit
    with the client's mission; a model giving "a 70% chance" of reaching the long-term goal; tests against
    simulations and historic downturns.
- **Bullish Bearcats, The Hotchkiss School, Connecticut** [O15][W7] (public GitHub README):
  - FACT: "Data Collection ... Fundamental Screening ... Quantitative Factor Analysis ... Correlation &
    Diversification ... Portfolio Optimization ... Projection [Monte Carlo] ... Backtesting ... Monitoring", with
    COVID-style stress-test folders.
  - FACT: "This repository will go public after the final report submission date." They kept their work private
    during the competition.
  - Result: Top 50, not a finalist [W7].

### 2.2 2024-25 (client Ladi Ayoola; $100,000)

**BAM Investing, Deerfield Academy: 1st** [W11].
- No outside coverage found (searched Deerfield's site, the Deerfield Scroll and general web).
- Deerfield returned with "ARC Investing" in the 2026 Top 50 [W7].

**Finance From France, Lycée Français de Chicago: 2nd** [W11].
- Only a sponsored Chicago Parent piece (blocked, 403). Its search snippet says the business club "placed second out
  of 5,000 teams". SCHOOL CLAIM; no strategy detail.

**FA Quakers, Friends Academy, New York: 3rd** [W11] [O25]
- School news (27 Mar 2025): seven juniors from the Stock and Finance Club; advisor a US History teacher.
- "From there, the team had to create a video explaining their philosophy and making a further pitch to sway the
  judge's decision."
- No strategy detail.

**Other 2025 finalists and semifinalists**
- **Cornerstone Capital, Delbarton School, NJ** (finalist) [O24]:
  - Seven members, guided by a club moderator who is a Penn graduate.
  - The school had earlier semifinal results, but this was "the first time a Delbarton team made the cut as a
    finalist". Delbarton had two Top 50 teams in 2025 [W6].
- **Fordman Sachs, The Haverford School, PA** (Top 50) [O26]:
  - "a fourteen-page report"; "the long seven months that it took us".
  - "The hardest part ... was getting a group of seven people together, all with different levels of education in
    finance."
  - Preparing the 10-minute presentation: "trying to visualize all of the writing ... and make a very concise and
    eye-appealing presentation."
- **Mango, The Harker School, CA** (Top 50) [O28]: four sophomores. The school says the 50 were split into "five
  groups of 10", with the top two from each advancing.
- **Croton Securities Council, Croton-Harmon HS, NY** (Top 50 in 2024 and 2025) [O29][O30][W5][W6].
- **$tockSnipers, American International School Dhaka, Bangladesh** (Top 50) [W6]: posted a YouTube video titled
  "$tockSnipers Semi-Final Video | Wharton Global High School Investment Competition 2024-2025" [O51]. Content not
  viewable here.

### 2.3 2023-24 (client Hilary Ash; first year with an ETF requirement)

**Spark Investments, Bergen County Academies: 1st** [W11].
- No outside coverage loaded (BCA pages returned 404/406).
- Wharton's tagline for them: "Ignite the flame for your financial future" (R1). INFERENCE: an Olympic-flame image
  for a client working on LA28.

**Wreckers Wealth Management, Staples HS, Connecticut: 2nd** [W11] [O17] (Inklings News, 20 May 2024)
- **Team:** seven juniors. It was "the second year of the team's existence"; in year one the club "was something
  that was, to put it quite frankly, a little unserious". It became an official club, which "added a sense of
  seriousness".
- **Strategy (FACT, as told):**
  - "The team realized that many other groups' strategies revolved around doing whatever it took to make the most
    money."
  - They chose instead to invest in "stocks relating to the interests of the case study".
  - "We built [our strategy] choosing stocks for her and not just choosing stocks based on an algorithm ... the
    right social initiatives ... After that, we made sure that the financials lined up. It was personal first."
- **How they worked:** divided research by sector. "For two full months, the team met over a video call every
  Monday and Thursday at 8:30 p.m."
- **Presentation:** the client "listened in" at the final. Their closing line linked investing to goals "scored",
  with a mimed soccer kick that drew laughs and cheers.
- **Mistakes:** "When you start from scratch, you have to fail, and your hope is that you fail fast and pick
  yourself back up ... we've learned from past mistakes."
- SCHOOL CLAIM: the first team from a public, non-magnet school to be first runner-up.

**DMV's Finest, TJHSST: 3rd** [W11]. No outside coverage found.

**Other 2024 finalists and semifinalists**
- **Big Apple Investments, Stuyvesant** (finalist) [O2][W5]: two helpers are thanked for the "video deliverables".
- **Finance Bros, The Harker School** (finalist; all ninth graders) [O27][W5]: after making the Top 50 they were
  "tasked with preparing a video for the next stage".
- **InvestIQ, Jayshree Periwal International School, Jaipur** (finalist) [W5]: uploaded "InvestIQ Global Finale
  Pitch" to YouTube [O51]. Content not viewable here.
- **Croton Securities Council** (Top 50) [O29]. Wharton's semifinal press release, reprinted by the local paper,
  quotes an abrdn judge: "It was positive to see the effort taken by the students to not only understand the
  client's investment goals, but also take into account the client's personal values, and use these insights to
  build some really well thought out portfolios".
- **Team Mochi, Newton North HS** (Top 50 [W5]): its report is on Scribd. R2 recorded its headings only; it contains
  personal data.
- **Contrast: a team that did not make the Top 50.** "Profiteering Peninsula Panthers" published its full 2023-24
  final report on Teen Ink [O32]. It is not on the 2024 Top 50 list [W5]. Its approach matched stocks to the
  client's interests: "companies that sponsored the LA2028 Olympics"; Marriott because of "her love of real estate
  and travel"; energy stocks "of the Latin American market" to "directly fund Hilary's investment property"; and
  "the highest returns possible with minimal risk". INFERENCE: matching stocks to interests appears in a 2nd-place
  team (Staples) and in a team outside the Top 50. On its own it is not what separates them. What Staples added was
  "the financials lined up" and a defended plan; this report mixes goals and holdings loosely.

### 2.4 2022-23 (client Peter Wang Hjemdahl; start-up gift fund plus a yoga and wellness centre)

**DMV's Finest, TJHSST: 1st** [W11]. No outside coverage found; R1 has the team's own lessons.

**Amity 7 Chakras Investments, Amity Regional HS, Connecticut: 2nd** [W11] [O18][O19]
- **Team (FACT):** seven students; the club began "two years ago" [O18].
- **Strategy (FACT, as reported):** "an investing strategy ... with several 'chakras,' or stages, which utilize
  data-driven analysis to ensure peace-of-mind investing" [O18]. INFERENCE: chakras are a yoga idea, and the client
  wanted a yoga centre. The frame came from the client's world.
- **Code (FACT, read from the public repo; the README says the strategy "enabled us to place 2nd out of 3,200 teams
  in 2022-2023") [O19]:**
  - The 2022-23 folder holds sector weights for about 13 stocks with betas noted [`PortfolioNotes.txt`].
  - It also holds a "Startup MonteCarlo" script: 100,000 runs counting how many years a $20,000 fund could keep
    paying a $5,000 gift at each beta from 0 to 2. It uses CAPM for expected return.
  - Other scripts: a growth-estimate scraper and a simple sentiment score.
- **Finale format:** "10 minutes to pitch ... followed by 5 minutes of questioning"; "For four hours, teams took turns
  presenting economic analysis, custom algorithms, ESG considerations, and more" [O18].

**NovyPorg_1, Nový PORG, Prague: 3rd** [W11] [O20-O23]
- **Team (FACT):** five 18-year-olds from a student investment society founded in 2019. They first entered in
  2019-20 [O23].
- **Preparation:** before the final they met three J&T Banka professionals "to discuss experience and tactics before
  the final" ("probrat zkušenosti a taktiku před finále") [O20]. The Prague Stock Exchange director "heard their
  competition idea and strategy" [O22].
- **Semifinal format, in their words:** "We had to film a video summarising our strategy and answer follow-up
  questions linked to it" ("natočit video, které naši strategii shrnuje, a odpovědět na doplňující otázky") [O22].
- **Final:** "15 minutes" to defend, including judges' questions [O21][O22].
- **Mistakes (personal investing, not the competition):** early COVID trading made them overconfident ("we told
  ourselves we were probably very good at it"), and some lost money on a fast-rising crypto coin [O23].
- **Afterwards:** "Most proud ... that our investment platform open to all secondary-school students is growing";
  about 90 members [O23]. Nový PORG has made the Top 50 every year since: "NPIS_1" (2024), "IT IS" (2025), "NP
  FundaQuants" (2026) [W5-W7].

**Other 2023 finalists and semifinalists**
- **K-Turtles, Cheongshim International Academy, South Korea** (finalist) [W4].
- **Two 2022-23 finalists, interviewed on Wharton Global Youth's LinkedIn** [O33], on the skill they used most:
  - "starting with the goal and creating a portfolio, going backwards. Because before doing the competition I thought
    that doing investing was just a game to see who could make the most money."
  - They then added "GARP strategy, which is growth at reasonable price ... and then ... an efficient frontier
    strategy on top of that."
- **AICA, Akademeia High School, Poland** (Top 55) [O34]: six members. They invested across "stocks ... government
  bonds and cash holdings".
- **Baldwin Bulls, Baldwin School of Puerto Rico** (Top 55) [O35]: the school says "judges were impressed by the
  strength of their investing knowledge, creativity and teamwork" (SCHOOL CLAIM). Its claim to be the only team from
  Latin America is checked in 4.3.

### 2.5 2021-22 (client Nichole Jordan: fixed $5,000 a year for at least 10 years)

**Sailing to Success, several Arizona schools: 1st** [W11]. Multi-school teams were then allowed.
- Outside sources: abrdn press release [O36] (confirms the win; an abrdn analyst attended); ABC15 [O37].
- A member later founded "Investing Insights", a student non-profit teaching younger children about money. She said:
  "Last year I was on the team that won the Wharton Global High School Investment Competition" [O37].
- A search snippet of a school-paper article (ACP Knight Times, blocked) says the name came from a "Compass" method
  the team used to analyse stocks. UNVERIFIED.
- Strategy for the fixed $5,000 payments: **not found.** This is the closest precedent to Laura's case.

**Sky Investments (BCA): 2nd; M&R Investments (Marvin Ridge): 3rd** [W11]. No outside coverage found.

**Other 2022 finalists and semifinalists**
- **Brazen Bulls Capital, American Heritage School, Florida** (finalist) [O38]: five students, from sophomores to a
  senior. It was "the first time in American Heritage School's history that our students are part of this
  prestigious competition". INFERENCE: a first-year team can reach the finale.
- **MATADORS-OF1, Miramonte HS plus two other schools** (Top 50) [O39][O40]:
  - "the team worked for several months, beginning last summer"; "We spent countless hours just scrutinizing every
    single detail of the case study."
  - The leader was shown "recording their virtual presentation for the semi-finals".
  - The advisor said he had "very little to do with these kids' success": paperwork, a room, emails. This fits the
    rule that advisors don't make decisions.
- **Gryphon Group, Brisbane State High School** (Top 50; see 4.2).

### 2.6 Earlier seasons (context only; different format)

- **2019-20:** a tie for 1st between East Capital K (UWCSEA, Singapore) and Over the Moon Investments (Maclay School,
  US) [W8]. The Singapore leader said they had entered "free of any pressure to win" [W8]. Wharton's YouTube channel
  hosts a talk by the Maclay co-champions, two siblings, titled "... on Winning the Wharton Investment Competition"
  [O51]; content not viewable here.
  - Conflict: a UWCSEA East teacher's page says UWCSEA East teams "were global champions for the 2020-21
    competition" [O42]. Wharton names M&R Investments as 2020-21 champion (R1). The page probably means 2019-20.
    UNVERIFIED.
- **2018-19:** Filter Coffee Investments (Amity International, Noida, India) won the Global Finale, and Scion Capital
  (Jayshree Periwal, Jaipur) came 2nd [W9]. Non-US teams have won. R1 notes that every champion from 2021-22 onward
  has been from the US.
- **2016-17:** UWC Red Cross Nordic (Norway) says its team "came third" in a final of "15 top teams", starting from
  "more than 600 competing teams" (post dated 8 May 2017) [O43]. The strategy was built on "sustainable and ethical
  investing" and UWC values. Whether this was the global final is UNVERIFIED.

---

## 3. Patterns in what winners did

Each pattern lists its evidence and how strong it is. These are patterns, not rules. The judges' official tests are
the five criteria in the 2026-27 deliverables page (`competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt:55-59`).

**P1. Goal first, portfolio second (strong).** Evidence: the finalists' "going backwards" quote [O33]; Staples'
"personal first", then "the financials lined up" [O17]; Amity's script counting how many years the client's gift
lasts [O19]; Vandegrift's goal probability (snippet) [O16]; Miramonte "scrutinizing every single detail of the case
study" [O39]. *This maps to "Client Knowledge" and "Portfolio Analysis ... funding reliability"
(`deliverables.txt:56-57`).*

**P2. A memorable frame from the client's world (moderate; INFERENCE).** Evidence: "7 Chakras" for a yoga-centre
client [O18]; "Ignite the flame" for an Olympics client (R1); a soccer-kick close [O17]; NFL-themed names and video
settings in 2026 [O14][W7]. Caution: in 2026 at least six Top 50 names used football or "better future" themes
(End Zone Equity, Endzone Investments, Lumen Field Investments, Tackling the Market, LEDger & Turf, Better Future
Fund) [W7], so a themed name on its own is common. A team outside the Top 50 also used a theme (Olympic sponsors), but to
pick stocks [O32]. Where the frame earns its place is in organising and explaining the plan.

**P3. One custom analytical tool, tied to a client question (strong that it is common; weak that it decides).**
Evidence: Marista's scoring model [O5]; Westminster's real-time Python tool [O11]; Amity's Monte Carlo [O19];
Hotchkiss's 9-phase pipeline [O15]; Vandegrift's screen and stress tests [O16]. Hotchkiss had the heaviest public
quant work and stopped at the Top 50 [W7]. R1 records a 2024 finale judge saying depth and accuracy, not volume,
"differentiated better performances". *INFERENCE: tools are now expected. The edge is one tool that answers one
client question, explained simply.*

**P4. Visible division of labour by strength (moderate).** Staples split by sector [O17]. Westminster split into
data, quant and presentations [O11]. Marista: all four presented in the video [O5]. Haverford named aligning seven
people of different levels as the hardest part [O26]. *Maps to "Articulation of Competition Experience"
(`deliverables.txt:58`). The 2026-27 FAQ says "All team members must participate" in semifinal and finale
presentations (`smapply_public_2026-10-14/faqs.txt:89`).*

**P5. Persistence and pipelines (strong).** DMV's Finest (2022 finalist, 2023 1st, 2024 3rd, 2025 finalist; R1 and
[O24]). Nový PORG: entered 2019-20, bronze 2023, Top 50 2023-26 [O23][W4-W7]. Staples: 2nd in the team's second year
[O17]. Stuyvesant: 13 teams in 2023-24, finalists in 2024, champions in 2026 [O1][O2]. Schools that are often in the
Top 50: Delbarton, Harker, Croton-Harmon, Podar (India) and the Amity International network in India (6, 5, 4 and 3 teams in
the 2023, 2024, 2025 and 2026 Top 50 lists) [W3][W5-W7]. *INFERENCE: much of the "winner pattern" is clubs that learn year to year.
Knox also competed in 2025-26 (`team/google_drive/2025_knox_wharton.md`). The lesson is to apply last year's
lessons, which CLAUDE.md:39-42 already lists.*

**P6. Long preparation and a fixed meeting rhythm (moderate).** 7 to 15 months of total effort [O6][O26][O39];
Staples met twice a week for two months [O17]; Vandegrift held weekly sessions (snippet) [O16]. Several teams worked
on their semifinal material right after the Top 50 announcement and practised it [O5][O26][O27].

**P7. Rehearsal with outside adults, without handing over decisions (moderate).** Bank and stock-exchange
professionals for Nový PORG [O20][O22]; a writing teacher's "fourth grader" test at Parish [O14]; finance parents'
Q&A at UWCSEA [O42]. Rules: unpaid secondary advisors are allowed; paid advisors, education consultants and
"non-Wharton extracurricular course[s] ... that claim to teach the Investment Competition" are banned, and Wharton
may use "private investigatory firms" [W1]. *INFERENCE: commercial coaching aimed at this competition exists. For
example, `wghs.org.cn` mirrors Wharton news and carries a Hanlin tutoring footer ("I am a Hanlin teacher") [O48], and New Oriental
(`liuxue.xdf.cn`) posts student testimonials about it (search snippet). Enrolling in such a course is a
disqualification risk. Reading free public pages is not enrolling.*

**P8. Presentation habits (moderate).** All members speak [O5][faqs.txt:89]. A strong closing image tied to the
client [O17]. Practise so the live pitch matches the video [O5]. "Confident and professional ... under pressure,
responding thoughtfully to judges' questions" [O12]. "Selling yourself and your work with indisputable confidence"
(a student's OPINION) [O11]. Cut the written report down to a "very concise and eye-appealing presentation" [O26].
*Semifinal format: in 2023 a video plus follow-up questions [O22]; in 2025-26 videos were still filmed [O14]. For
2026-27 the FAQ says a presentation "via video conference for the Semifinals ... to a live panel of judges"
(`faqs.txt:89`). Whether a pre-recorded video is also needed in 2026-27 is UNVERIFIED.*

**P9. Showing that the plan adapts (weak to moderate).** Westminster was praised (SCHOOL CLAIM) for its "capacity to
adapt and pivot investment classes" [O11]. The 2022 winning leader's biggest lesson was "adapting to change" (R1).
*INFERENCE for a buy-and-hold plan: judges may ask "what would make you change it?" The answer has to be a rule,
not a promise to trade. Caplet already has a real adaptation story. The 6 Oct Wharton email limited Laura's plan to
WInS-listed stocks, ETFs and Treasury bonds, and the team switched off STRIPS (CLAUDE.md "Current status").*

**P10. Youth and team size do not decide (strong).** Ninth-grade finalists [O27]; a Year 11 finalist team [O11]; a
four-member team in 2nd place [O5]; a freshman led the 2022 winners (R1).

**P11. Mistakes that past teams named.**
- Chasing returns and the leaderboard. The 2020 Medium author was "4th place in the ROI standings" and later
  admitted "over-trading ... panic selling" [O44]. Kingswood Oxford's school story boasted of a "top 60 out of 4,000"
  return ranking [O45]. Neither team reached a Top 50 that I could find.
- Uneven work: "it was still me doing the heavy lifting" [O44].
- An unserious first year [O17].
- Doing too much at once, and trimming late (DMV's Finest, R1).
- Taking media "firsts" on trust (section 4.3).

**P12. What winners did NOT leave behind.** No public winning report, deck or asset mix. No outside account of the
judges' actual questions. No outside account of how the 2021-22 teams funded the fixed $5,000 payments. *So any claim
in team files that "winners did X" beyond the above is UNVERIFIED.*

---

## 4. International and non-US teams

### 4.1 Summary by country (outside sources, placings checked on Wharton lists)

| Country | Team / school (best result) | What the outside coverage says they did |
|---|---|---|
| Brazil | HHA Investments, Marista Brasília (2nd 2026) | 15 months of effort; studied past teams; own Markowitz-based scoring model; all four in the video [O4-O9] |
| Brazil | Eagles Value Added, Graded School São Paulo (2019 finalist; 2nd 2019-20) | Wharton only [W8][W9] |
| Czechia | NovyPorg_1, Nový PORG (3rd 2023; Top 50 2023-26) | Student society since 2019; first entered 2019-20; rehearsed with bank professionals; video plus follow-up questions in the semifinal [O20-O23] |
| UK | Hooke Investments, Westminster (finalist 2026) | Year 11; Python real-time data tool; split data / quant / presentation; praised for adapting [O11] |
| UK | Perse Capital Group (finalist 2026) | Confident delivery and Q&A [O12] |
| India | Amity International network; Jayshree Periwal; Neerja Modi | Many Top 50 places every year [W4-W7]; finalists 2023-26 (Himalayan Melange presented remotely in 2023 after visa trouble, R1); won 2018-19 [W9]. Outside pages mostly unreachable |
| Singapore | UWCSEA (co-champion 2019-20; Top 50 2023-24) | Weekly peer-led prep; a top-down value method ("macroeconomics, sector and industry analysis, and then valuation"); finance parents ran Q&A [O42] |
| Singapore | Raffles, Hwa Chong, ACS | Top 50 in 2022, 2024, 2025, 2026 [W2][W5-W7]; no outside detail found |
| South Korea | K-Turtles, Cheongshim (finalist 2023) | Wharton only [W4] |
| China | Dulwich College Beijing (finalist 2024) and others | A tutoring brand reports "only 8" Chinese teams in the 2023 Top 55 [O47] |
| Canada | Evergreen Asset Management, St Robert (finalist 2025) | Wharton and Delbarton list only [O24][W6] |
| Poland | AICA, Akademeia (Top 55 2023) | Stocks, government bonds and cash [O34] |
| Puerto Rico | Baldwin Bulls (Top 55 2023) | School claims judges praised knowledge, creativity, teamwork [O35] |
| Bangladesh | $tockSnipers, AIS Dhaka (Top 50 2025) | Posted its semifinal video on YouTube [O51] |
| Norway | UWC Red Cross Nordic (3rd, 2016-17 per school) | Ethical and sustainable investing [O43] |
| New Zealand | Kristin School (top 50 in 2021, 2022, 2023) | No outside detail found |
| **Australia** | **Brisbane State High, Gryphon Group** (2021 regional finalist; Top 50 2022) | See 4.2 |

### 4.2 Australia and New Zealand

- **Brisbane State High School, "Gryphon Group"** [O41] (school newsletter and achievements page, early 2021):
  - FACT: five Year 11 students, advised by an Economics teacher.
  - "After more than 15 weeks of participation, Gryphon Group has been selected in the top 10 teams in the region
    (Oceania, Europe and South America), and is the only team in Australia to progress to the Virtual Regional Finals
    in March 2021 ... one of 50 teams around the world selected from 972 submitted final competition reports across
    35 countries."
  - Team motto: "Knowledge is power—even in the market."
  - The same team name is in the 2022 Top 50 [W2], so the team came back a second year.
  - Strategy: not described. Their 2021-22 regional finals and semifinal results beyond the Top 50 are UNVERIFIED.
- **Since then:** no Australian school appears on the 2023, 2024, 2025 or 2026 Top 50 lists [W3-W7]. I checked every
  saved list for "Australia", "Brisbane", "Sydney", "Melbourne" and "New Zealand". Searches of Australian school sites
  found nothing newer. This agrees with the team's own note in `team/Winning Team Portrait and Scoresheet.md:45`.
- **Kristin School, Auckland:** 2021 regional finalists ("YHL Unlimited", the top 50 of that year) [W10], Top 50 in
  2022 ("V") [W2] and 2023 ("Dove Capital") [W3].
- **What this means:**
  - INFERENCE: there is no Australian playbook to copy, and recent Australian success has been rare.
  - Logistics FACT (2026-27 FAQ): Wharton does not cover finale costs, and teams "can choose to attend virtually via
    videoconference" (`faqs.txt:87`).
  - The semifinal is a live video conference (`faqs.txt:89`). The time of day is UNVERIFIED and could fall at night
    in Sydney.

### 4.3 Three media "firsts" that are wrong (why every claim needs checking)

1. Correio Braziliense says HHA was "the only team from Latin America in history to reach the final" [O6]. **Wrong:**
   Brazil's Graded School presented at the 2019 Global Finale and placed 2nd in 2019-20 [W8][W9].
2. Czech outlets call Nový PORG "the most successful European team in history" [O20][O21]. **Doubtful:** UWC Red
   Cross Nordic (Norway) reports a 3rd place in 2017 [O43], and Dulwich College London presented at the 2019 finale
   [W9]. FeedIT's narrower claim, the first *Central European* finalist [O22], may be right.
3. KXAN says Vandegrift was "headed to global finals" [O16]. **Wrong:** Wharton lists them in the Top 50 only [W7].

---

## 5. Re-checking the competitor references in Caplet's own files

The team's docs cite public GitHub repos as "past semifinalist/finalist" work (`team/google_drive/resource.md:14-29`;
`docs/THIRD_PARTY.md:35-37`; `docs/reference_audit.md:9-96`; `docs/wharton_reference_patterns_v2_1.md:6-8`).
Status on 16 Oct 2026:

| Repo | Claim in team docs | Status |
|---|---|---|
| `aaravp6/All-Wharton-Investment-Competition` | Amity, 2nd 2022-23 (`THIRD_PARTY.md:36`) | **Verified.** The README says "place 2nd out of 3,200 teams in 2022-2023" [O19], and Wharton lists Amity 7 Chakras 2nd [W11]. **But** the "client liability survival simulation" the team doc credits to that season (`wharton_reference_patterns_v2_1.md:36`) is in the repo's *2023-2024* folder (`monte_carlo_consulting.py`). Its rent/salary payments start after year 15, which fits the 2023-24 client's consulting-firm goal [O32]. Amity Regional is not on the 2024 Top 50 [W5]. The 2nd-place season used a simpler "Startup MonteCarlo" (years the gift fund lasts by beta). INFERENCE from folder order and content: the doc mixes up the season. |
| `gavin-ho1/wharton-investment-comp` | Hotchkiss Top 50 2025-26 (`THIRD_PARTY.md:35`) | **Verified** Top 50 [W7]; **not** a finalist [W7]. The README says the repo stayed private until after the final report [O15]. |
| `davidliu-2008/wharton-investment-competition25-26` | "Semifinalist 2025-26" (`THIRD_PARTY.md:37`, `resource.md:26-29`) | **Not reachable.** The README returns 404 on `main` and `master`, and `git clone` asks for credentials (private or deleted). The semifinalist claim is **UNVERIFIED**; no team name links it to the Top 50 list. |
| `IrajShroff/Wharton-Investment-Competition---Blast-Strategy` | "Semifinalist (Top 50, 2024-2025)" (`reference_audit.md:96`) | The README says only "Programs to help manage stocks for Wharton 2024". Semifinalist claim **UNVERIFIED**. |
| Scribd "Mochi" report | "Semifinalist 2023-2024" (`resource.md:14-19`) | "Team Mochi: Newton North High School" is on the 2024 Top 50 [W5]. The name match is plausible; R2 recorded headings only. |

Also OPINION in team docs: "Wharton judges prize client-centricity above all else, and this tool proved that the
portfolio directly supported the client's life goals" (`wharton_reference_patterns_v2_1.md:36`). No source shows
judges saw or rewarded that tool.

---

## 6. What this means for Caplet (knowledge, not text)

Each item says what a fix must achieve. The team decides and writes.

1. **Caplet's core design already follows the most consistent winner trait (P1).** The ten payments are bought
   first, from goal to portfolio. The risk is that a reader can't see it. *The fix must make the goal-backwards
   logic visible in one sentence that a non-finance adult can repeat (the Parish "fourth grader" test [O14]).*
2. **Being different should come from the client's problem, not from tools or names (P2, P3).** Themed names and
   custom models are now common [W7][O5][O11][O15]. None of the outside sources I found describes a plan that buys
   fixed future payments with owned Treasuries. INFERENCE: this is rare among public examples, but winners' plans are
   not public (P12), so "rare" is UNVERIFIED. *The fix must state why Laura's case (payments larger than deposits,
   "high degree of certainty") forces this design, so it reads as client-driven rather than clever.*
3. **A frame from Laura's world could help, if it explains and does not pick stocks (P2).** Past frames came from the
   client's passions: yoga, the Olympics, football. *Test: does the frame make the plan easier to remember, and does
   it lead to any holding that the numbers don't support? If it does, drop it.* (Don't name a frame from memory; use
   only verified client facts from the case.)
4. **Rehearse with outside adults before the semifinals (P7).** Rules allow an unpaid secondary advisor (a parent or
   industry professional) [W1]. *Must achieve: practice Q&A with someone who does not know the plan, logged honestly
   for the Articulation section. No decisions by them, no paid help, no outside course.*
5. **Plan semifinal work now, before the Top 50 announcement (late January in past years; the 2026-27 date is
   UNVERIFIED) (P6, P8).** All six must take part
   (`faqs.txt:89`). Past teams had a video ready within weeks [O5][O26][O27]. *Must achieve: a speaking part for each
   member, a 10-minute version of the plan, and a list of likely judge questions with answers backed by numbers.*
   Sydney time-zone clashes are UNVERIFIED but likely.
6. **A hold strategy needs an "adaptation" story (P9).** *Must achieve: the Final Report shows real decisions that
   changed (for example, STRIPS to WInS-listed securities after the 6 Oct email) and the rule for when the plan
   would change. It must not suggest trading that did not happen.*
7. **Repo visibility: one new data point.** Hotchkiss kept its competition code private until after its final
   report [O15]. Caplet's repo is public (CLAUDE.md:29). The 15 Oct brief already covers this decision, so I don't
   repeat it. The new fact is that at least one Top 50 team chose privacy during the competition.
8. **Fix the team's own reference docs (section 5).** *Must achieve: mark the two unverified "semifinalist" repos
   (rows 3 and 4 of the section 5 table) UNVERIFIED, and correct the Amity season attribution, before anyone cites
   them in the Final Report.*
9. **Avoid the named mistakes (P11):** talking about returns or WInS rank; trading for activity; uneven workload
   (the Articulation section should show real roles); unverified "first Australian ..." claims (4.3).

---

## 7. Gaps and next checks (for the team, if wanted)

- Watch the Wharton Global Youth YouTube videos listed in [O51]: the 2020 co-champions' talk, the "Competition
  Insider Information" champion Q&A, and the InvestIQ finale pitch. They may show real finale slides and Q&A. I
  could see titles only.
- Read the 2026-27 Final Report instructions when they are released on 9 Nov. They may change what the semifinal
  needs.
- Try to confirm the 2026-27 semifinal format and time (pre-recorded video or live only). The FAQ wording is in
  `faqs.txt:89`.
- Pages I could not load are listed in the header. Their search-snippet content is marked UNVERIFIED above.

---

## 8. Sources (all accessed 16 Oct 2026; saved text in `oct16/research/R3_pages/`)

**Outside sources**
- [O1] Stuyvesant HS blog, "Stuyvesant High School Wins the 2026 Wharton ... Competition '26!", 2 May 2026. https://talos.stuy.edu/cms/pages/stuyvesant-blog/stuyvesant-high-school-wins-the-2026-wharton-global-high-school-investment-competition-26/ (`stuy_talos_2026_win.txt`)
- [O2] Stuyvesant HS blog, "Stuy team advances to International Finals ...", 22 Mar 2024. https://talos.stuy.edu/cms/pages/stuyvesant-blog/stuy-team-advances-international-finals-wharton-investment-competition/ (`stuy_talos_finals.txt`)
- [O3] Stuyvesant HS blog, "Congrats to seniors ...", 9 Feb 2024. https://talos.stuy.edu/cms/pages/stuyvesant-blog/congrats-seniors-wharton-global-high-school-investment-competition/ (`stuy_talos_seniors.txt`)
- [O4] Correio Braziliense, "Estudantes brasilienses são semifinalistas ...", Mar 2026. https://www.correiobraziliense.com.br/euestudante/educacao-basica/2026/03/7369145-estudantes-brasilienses-sao-semifinalistas-em-competicao-internacional-de-financas.html (`correio_2026_03_semis.txt`)
- [O5] Correio Braziliense, "Brasilienses são finalistas ...", Mar 2026. https://www.correiobraziliense.com.br/euestudante/educacao-basica/2026/03/7375281-brasilienses-sao-finalistas-em-competicao-internacional-de-financas.html (`correio_2026_03_finalists.txt`)
- [O6] Correio Braziliense, "Brasilienses conquistam a 2ª colocação ...", Apr 2026. https://www.correiobraziliense.com.br/euestudante/educacao-basica/2026/04/7407204-brasilienses-conquistam-a-2-colocacao-em-competicao-nos-estados-unidos.html (`correio_2026_04_second.txt`)
- [O7] Correio Braziliense, "Estudantes criam competição de investimentos em Brasília", Sep 2026. https://www.correiobraziliense.com.br/euestudante/educacao-basica/2026/09/7505083-estudantes-criam-competicao-de-investimentos-em-brasilia.html (`correio_2026_09_bfc.txt`)
- [O8] Blog do Amarildo, semifinal article. https://blogdoamarildo.com.br/estudantes-de-brasilia-sao-os-unicos-da-america-latina-em-semifinal-de-prestigiada-competicao-financeira-internacional/ (`blogdoamarildo_semi.txt`)
- [O9] Blog do Amarildo, finalist article (11 Mar). https://blogdoamarildo.com.br/estudantes-do-colegio-marista-brasilia-avancam-para-a-final-da-maior-competicao-de-investimentos-do-mundo/ (`blogdoamarildo_final.txt`)
- [O10] Jornal de Brasília column. https://jornaldebrasilia.com.br/entretenimento/katia-flavia/marista-brasilia-coloca-brasil-na-semi-da-wharton/ (`jornaldebrasilia_semi.txt`)
- [O11] Westminster School news, "Westminster School economists pitch their way to the final ...", 6 May 2026. https://www.westminster.org.uk/news-hub/westminster-school/westminster-school-economists-pitch-their-way-to-the-final-of-global-investment-challenge/ (`westminster_hooke_2026.txt`)
- [O12] The Perse School news, "Perse pupils reach global finals ...", May 2026. https://www.perse.co.uk/news/2026/05/perse-pupils-reach-global-finals-at-wharton-investment-competition/ (`perse_2026_finals.txt`)
- [O13] Ramaz School news, "The Six-Student 'End Zone Equity' Team is Top 50 ...". https://www.ramaz.org/multimedia/latest-news/post-details/~board/us-news/post/the-six-student-end-zone-equity-is-top-50-in-the-wharton-global-high-school-investment-competition (`ramaz_endzone_top50.txt`)
- [O14] People Newspapers, "Local Investment Team Advances to Wharton Top 50", May 2026. https://www.peoplenewspapers.com/schools/2026/05/local-investment-team-advances-to-wharton-top-50/ (`peoplenews_2026_top50.txt`)
- [O15] Hotchkiss team repo README (MIT). https://github.com/gavin-ho1/wharton-investment-comp via https://raw.githubusercontent.com/gavin-ho1/wharton-investment-comp/main/README.md (`github/gavin-ho1_wharton-investment-comp_README.md`)
- [O16] KXAN, "All-female Vandegrift team advances to Wharton ..." (page blocked, HTTP 429; content from search snippet, UNVERIFIED). https://www.kxan.com/news/local/austin/all-female-vandegrift-team-advances-to-wharton-global-high-school-investment-competition/ ; YouTube "Five Vandegrift High School juniors headed to global finals | KXAN" https://www.youtube.com/watch?v=d4k5tDLGZmE
- [O17] Inklings News (Staples HS), "Everyone's Investing in Wreckers Wealth Management", 20 May 2024. https://www.inklingsnews.com/b/2024/05/20/everyones-investing-in-wreckers-wealth-management/ (`inklings_wreckers_2024.txt`)
- [O18] Orange Town News, "Amity Students Place 2nd in Wharton's Global High School Investment Competition" (2023). https://www.orangetownnews.com/news/amity-students-place-2nd-in-whartons-global-high-school-investment-competition (`orangetown_amity_2023.txt`)
- [O19] Amity team repo (no licence; read only; last commit 1 Sep 2024). https://github.com/aaravp6/All-Wharton-Investment-Competition (`github/aaravp6_..._README.md`; files read in `github/clones/aarav/WhartonInvestmentCompetition2022/PortfolioNotes.txt`, `.../monteCarlo/Startup MonteCarlo.py`, `.../WhartonInvestmentCompetition2023/monte_carlo_consulting.py`)
- [O20] Echo24.cz, "Český historický úspěch ..." (Apr 2023). https://www.echo24.cz/a/HB5Ud/zpravy-ekonomika-cesky-historicky-uspech-stredoskolaci-ziskali-3-misto-nejvetsi-soutez-investori-sveta-porazili-evropa (`echo24_porg_2023.txt`)
- [O21] CzechCrunch, "Úspěch českých studentů ... získala bronz". https://cc.cz/uspech-ceskych-studentu-na-nejvetsi-investicni-soutezi-na-svete-petice-stredoskolaku-ziskala-bronz/ (`cc_porg_bronz.txt`)
- [O22] FeedIT.cz, "Čeští studenti jsou poprvé v historii ve finále ...", 5 Apr 2023. https://feedit.cz/2023/04/05/cesti-studenti-jsou-poprve-v-historii-ve-finale-nejvetsi-investicni-souteze-na-svete/ (`feedit_porg_finals.txt`)
- [O23] J&T Banka, "Mladí investoři z PORG ...". https://www.jtbank.cz/clanky/investovani/j3ix3rdo2v-mladi-investori-z-porg-behem-covidu-slo-vydelat-i-na-kapesnem-od-babicky-kratkodobe (`jtbank_porg.txt`)
- [O24] Delbarton School news, "Delbarton is Finalist in Wharton Investment Competition", 27 Mar 2025. https://www.delbarton.org/about-us/news-detail/~board/homepage/post/delbarton-is-finalist-in-whartoninvestment-competition (`delbarton_finalist.txt`)
- [O25] Friends Academy news, "FA heads to worlds! ...", 27 Mar 2025. https://www.friendsacademy.org/news/fa-heads-to-worlds-scores-top-10-place-in-wharton-contest (`friendsacademy_top10.txt`)
- [O26] The Index (Haverford School), 20 Feb 2025. https://thsindex.org/2025/02/20/wharton-global-high-school-investment-competition-group-a-advances-to-semi-finals/ (`thsindex_semis.txt`)
- [O27] Harker News, 1 Apr 2024. https://news.harker.org/harker-team-reaches-semifinals-of-wharton-investment-competition/ (`harker_semis_a.txt`)
- [O28] Harker News, 4 Feb 2025. https://news.harker.org/harker-team-named-semifinalist-in-wharton-investment-competition/ (`harker_semis_b.txt`)
- [O29] River Journal Online (reprint of Wharton's 2024 semifinal press release). https://riverjournalonline.com/schools/croton-harmon-high-school-team-to-compete-in-semifinals-of-the-wharton-investment-competition/98701/ (`croton_semis.txt`)
- [O30] The Croton Chronicle (Substack), 2025 (truncated). https://thecrotonchronicle.substack.com/p/croton-harmon-high-school-team-among (`crotonchronicle_2025.txt`)
- [O31] Podar Education news (2024 Top 50). https://www.podareducation.org/podarnews/34765 (`podar_2024_top50.txt`)
- [O32] Teen Ink, "Profiteering Peninsula Panthers 2023-2024 ... Final Report". https://www.teenink.com/opinion/all/article/1215809/Profiteering-Peninsula-Panthers-2023-2024-Wharton-Global-High-School-Investment-Competition-Final-Report (`teenink_peninsula.txt`)
- [O33] Wharton Global Youth Program on LinkedIn, 2022-23 finalists on skills (2023). https://www.linkedin.com/posts/wharton-global-youth_wharton-global-high-school-investment-competition-activity-7071566940762206210-3xUm (`linkedin_wgy_students_share.txt`)
- [O34] Akademeia High School news, 3 Feb 2023. https://www.akademeia.edu.pl/news/2023-02-03/wharton-global-high-school-investment-competition (`akademeia_2023.txt`)
- [O35] Baldwin School of Puerto Rico news. https://www.baldwin-school.org/apps/news/article/1719169 (`baldwin_pr.txt`)
- [O36] abrdn press release, 31 Jan 2023. https://www.abrdn.com/en-gb/corporate/news/all-news/abrdn-enters-second-decade-supporting-wharton-investment-competition-for-students (`abrdn_2023.txt`)
- [O37] ABC15 Arizona, "Valley students teaching financial literacy to younger generations". https://abc15.com/news/local-news/valley-students-teaching-financial-literacy-to-younger-generations (`abc15_investing_insights.txt`)
- [O38] American Heritage School (Broward) blog, 2022. https://www.ahschool.com/broward-campus/blog-highlights/~board/life-at-heritage/post/investors-society-club-as-top-10-global-finalists (`ahschool_top10.txt`)
- [O39] The Orinda News, 25 Mar 2022. https://theorindanews.com/2022/03/25/students-work-towards-winning-wharton-global-investment-competition/ (`orindanews_2022.txt`)
- [O40] Lamorinda Weekly. https://lamorindaweekly.com/archive/issue1526/Miramonte-students-make-it-to-Wharton-Schools-Global-High-School-Investment-Competition-semifinals.html (`lamorinda_miramonte.txt`)
- [O41] Brisbane State High School newsletter and achievements page (2021). https://brisbaneshs.schoolzineplus.com/newsletter/article/666?skin=1 ; https://brisbaneshs.eq.edu.au/our-school/student-achievements/global-investment-competition (`brisbaneshs_newsletter_666.txt`, `brisbaneshs_achievements.txt`)
- [O42] UWCSEA East, "Leading the Way for Financial Wellbeing" (Dragons Investment Society). https://stories.uwcsea.edu.sg/dragons-investment-society/index.html (`uwcsea_dragons.txt`)
- [O43] UWC Red Cross Nordic, "Wharton investment competition", 8 May 2017. https://uwcrcn.no/wharton-investment-competition/ (`uwcrcn.txt`)
- [O44] Medium post, "My experience with the Wharton Global High School Investment Competition", 18 Dec 2020 (read via the author's Medium RSS feed; the page itself returned 403). https://medium.com/p/8a228f4936c0 (`medium_abhinav_2020_rss.txt`)
- [O45] Kingswood Oxford news, "KO Students Invest in Wharton's Stock Market Competition". https://www.kingswoodoxford.org/news/ko-students-invest-in-whartons-stock-market-competition/ (`kingswood_oxford.txt`)
- [O46] Colégio Bandeirantes (Brazil regional final, older format). https://colband.net.br/o-aluno-band/band-no-knowledgewharton-high-school-investment-competition/ (`colband.txt`)
- [O47] Hanlin (Chinese tutoring brand), 30 Jan 2023, 2023 semifinal list commentary. https://www.hanlin.com/archives/782684 (`hanlin_782684.txt`)
- [O48] wghs.org.cn mirror pages of Wharton news (with tutoring-brand footer). https://wghs.org.cn/news/1077/ ; https://wghs.org.cn/news/1139/ ; https://wghs.org.cn/news/345/ (`wghs_cn_*.txt`)
- [O49] ABC Money, "The Wharton Investment Competition Is Free ...", Sep 2026 (OPINION). https://www.abcmoney.co.uk/2026/09/the-wharton-investment-competition-is-free-open-to-any-high-schooler-and-more-competitive-than-most-people-realize/ (`abcmoney_2026.txt`)
- [O50] Young Founders Lab guide (OPINION; contains errors). https://www.youngfounderslab.org/blog/wharton-global-high-school-investment-competition (`youngfounderslab.txt`)
- [O51] YouTube titles confirmed by oEmbed (videos not viewable here): $tockSnipers semifinal video https://www.youtube.com/watch?v=6R8R7QJI2DA ; InvestIQ Global Finale Pitch 2023-24 https://www.youtube.com/watch?v=cTkSKcuGTv8 ; 2020 co-champions talk (Wharton Global Youth channel) https://www.youtube.com/watch?v=x-e2hym9Imo ; "Competition Insider Information from Champ ..." (Wharton Global Youth channel) https://www.youtube.com/watch?v=aqPtV3e5jBU ; UWC student profile ("The Brief No 2") https://www.youtube.com/watch?v=mY18B25BE0k

**Wharton pages (saved by R1 in `oct16/research/R1_pages/`, accessed 16 Oct 2026), used only to confirm placings and rules**
- [W1] Rules & Roles: `rules-roles.txt:427` (secondary advisors allowed; paid help and outside courses banned; investigators), `:557` ("plagiarize existing strategies"). https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/
- [W2] 2022 Top 50: `introducing-the-2022-semifinalists-in-the-wharton-global-high-school-investment-competition.txt`
- [W3] 2023 Top 55: `congratulations-to-our-2023-investment-competition-semifinalists.txt`
- [W4] 2023 finalists: `celebrating-the-top-10-teams-in-the-2022-2023-wharton-global-high-school-investment-competition.txt`
- [W5] 2024 Top 50 and finalists: `here-are-the-top-50-teams-advancing-to-wharton-global-youths-2024-investment-competition-semifinals.txt`; `wharton-global-youth-hosts-five-virtual-events-to-announce-the-2024-investment-competition-finalists.txt`
- [W6] 2025 Top 50: `announcing-the-semifinalists-in-the-2025-wharton-global-high-school-investment-competition.txt`
- [W7] 2026 Top 50 and finalists: `a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed.txt`; `11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale.txt`
- [W8] 2020 finale (tie): `2020-investment-competition-global-finale-ends-tie-first-place.txt`
- [W9] 2019 finale: `2019-investment-competition-global-finale-showcases-financial-literacy-finest.txt`
- [W11] 2026 champions article and competition archive (top three per year): `2026-investment-competition-global-champions.txt`; `archive.txt`. https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/
- [W10] 2021 regional finalists (top 50 of 2020-21): `meet-2021-wharton-global-high-school-investment-competition-regional-finalists.txt`

**Official 2026-27 materials (repo)**
- `competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt:55-59` (five Final Report criteria)
- `competition/official/2026_27/smapply_public_2026-10-14/faqs.txt:87` (finale costs; virtual option), `:89` (semifinal by video conference to a live panel; all members must take part)
