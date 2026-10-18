# R1: What Wharton's own website says about past Investment Competitions (2021-22 to 2025-26)

Prepared 16 Oct 2026 (Sydney) for Team Caplet. Research only: no deliverable text is drafted here.

**Scope and method.** I fetched and read in full every page in `oct16/seeds_wharton.txt` (18 news articles, the
live competition page, Rules & Roles, FAQ and Archive), then followed links and searched the Wharton Global Youth
site and the web for more investment-competition pages (case studies, the AI policy, legacy guidebook pages,
a badge-criteria PDF, podcasts, a teacher blog, the academic director's profile, earlier finales). Raw text of
every page is saved in `oct16/research/R1_pages/<slug>.txt` (article bodies only in `oct16/research/R1_bodies/`).
All pages were accessed on **16 Oct 2026**. Every claim below carries a source tag like **[S6]**; the full URL for
each tag is in the source list at the end (section 8). Quotes are copied exactly from the page (curly quotes
straightened). Key quotes were re-checked word for word with `page.py --grep` on 16 Oct 2026.

**Privacy.** Students from other schools are named by first name and team only. Judges, clients, staff and
blog authors are named because they spoke publicly in a professional role and the quote needs an owner.

**What could not be reached.** web.archive.org is blocked by this session's egress policy (HTTP 403 "Blocked by
egress policy"), so the old "Previous Winners" page (which the FAQ still points to) and old "Judging and
Evaluation" page could not be read. Both now redirect to the main competition page. The 2023-24 (Hilary Ash)
and 2025-26 (Connor Barwin) case studies are not on the public site (404). YouTube video pages would not load,
so only channel video titles were seen.

---

## 0. Bottom line (what Wharton's own record says wins)

1. **Simple beats clever.** Four different voices said it in four different years: a 2022 finale judge ("less is
   more ... Cut slides, cut words, cut minutes") [S19], the 2023 champions ("less is more, and having an
   explainable strategy") [S16], a 2024 finale judge (depth and accuracy, not volume, "differentiated better
   performances") [S10], and a 2025 semifinal judge ("the best solutions are made up of simple, elegant ideas")
   [S5]. The 2026-27 academic director has said "the jargon and acronyms are just obfuscating the elegant
   simplicity of finance" [S33, S21].
2. **Tie every decision to the client.** Judges praised "the ability to connect the client's objectives to an
   investment strategy" (2024) [S9] and "the level of analysis of understanding for Nichole Jordan's
   situation" (2022) [S18]. The 2025 client thanked teams for making plans "not just about the numbers, but about
   understanding and connecting with people" [S6].
3. **Reasoning and defence decide the top places.** The 2025 finale judge from Aberdeen said what separates
   professional managers is "clear thoughtfulness and reasoning behind all the decisions" [S6]. Finales are 10
   minutes of pitch plus 5 minutes of judges' questions (stated for 2023 and 2025) [S14, S6].
4. **Quant tools are normal, not special.** Efficient frontiers, correlations, Monte Carlo, machine learning and
   stock-screening algorithms appear in finalist work almost every year [S10, S9, S37, S14]. Judges praised them
   but also pushed teams toward behavioural finance and a "holistic" view of the client [S10].
5. **Teamwork must be visible.** Semifinal and finale presentations need every member [S23]. A 2024 semifinal
   judge said the part she "enjoyed the most" was how teams "assessed each member's skills" [S9].
6. **The Top 50 is very selective and is decided on paper.** About 2-4% of submitting teams reach the Top 50
   (2.1% in 2025-26) [S3, S21]. For 2026-27 the public rules say the Top 50 is chosen "based on the strength of
   their Investment Policy Statement (IPS) and Final Reports" [S22].
7. **Non-US teams reach the Top 50 often but rarely the podium.** Roughly 40-51% of each Top 50 list is outside
   the U.S. [S17, S12, S8, S4, S3], but every champion from 2021-22 to 2025-26 was a U.S. team [S24]. An Australian
   team (Brisbane State High School) reached the Top 50 twice (2020-21 regional finalists, 2021-22 semifinalists)
   [S38, S17]. No Australian team appears in any Top 50 list from 2022-23 to 2025-26.
8. **Persistence pays.** Recent champions were often repeat finalists: DMV's Finest (finalist 2022, champion
   2023) [S14], Fig Capital / FigCapital from Stuyvesant (finalist 2025, champion 2026) [S5, S1], Bergen County
   Academies (2nd 2022, 1st 2024) [S19, S10], Nový PORG (competing "since ... 2019", 3rd in 2023) [S35, S14].
9. **The client is real.** Wharton says: "While the client is real, the financial scenario is developed
   specifically for the competition." [S21] Contacting the client means disqualification [S22].
10. **AI must be logged.** Wharton's AI policy page says: "If you use AI to assist you in any way during the
    competition, how you use it must be recorded in your Works Cited pages." [S25]

---

## 1. One-table summary by year

| Year (finale) | Client (case in one line) | Teams registered | Final reports | Top N | Finalists | Champion |
|---|---|---|---|---|---|---|
| 2021-22 (Apr 23, 2022) | Nichole Jordan, WG'08: $100k; fund a $5,000/yr scholarship for at least 10 years from 2022, plus generational wealth for six nieces and nephews [S26] | "thousands" [S19] | "nearly 1,300" from 64 countries [S17] | 50 | 10 [S18] | Sailing to Success (schools in Arizona, U.S.) [S19] |
| 2022-23 (Apr 22, 2023) | Peter Wang Hjemdahl, W'19: $100k; $20k to grow into a fund giving $5-10k a year to a start-up by age 30; yoga and wellness centre in Miami within 15 years [S27] | 3,200 from 53 countries [S14] | "nearly 1,400" from 53 countries [S12] | 55 | 10 [S13] | DMV's Finest (Thomas Jefferson HS for Science and Technology, VA) [S14] |
| 2023-24 (Apr 20, 2024) | Hilary Ash, W'13 (LA28 Olympic and Paralympic Games executive; volleyball a highlighted passion) [S9, S10]; full case not public | not stated | "more than 1,600" from 63 countries [S8] | 50 | 11 [S9] | Spark Investments (Bergen County Academies, NJ) [S10] |
| 2024-25 (Apr 26, 2025) | Ladi Ayoola, WG'22: $100k; impact hub in Abuja, Nigeria; Phase One at least five housing units by 2030 (~$10k each); Phase Two in 2040 storefront + youth centre (at least $50k) + one year of running costs [S28] | "more than 5,000" [S4] | "more than 1,800" from 66 countries [S4] | 50 | 10 [S5] | BAM Investing (Deerfield Academy, MA) [S6] |
| 2025-26 (Apr 25, 2026) | Connor Barwin, WG'23, former NFL player, founder of Make the World Better; case about "long-term community impact" [S2]; full case not public | "more than 6,300" [S3] ("more than 5,400 ... began" in a later post [S2]) | "some 2,300" from 79 countries [S3]; completion counter 2,339 teams, 79 countries, 12,145 students, 1,625 advisors [S21] | 49 listed (titled "Top 50") [S3, S2] | 11 [S2] | FigCapital (Stuyvesant HS, NY) [S1] |

Selection rates (my arithmetic from the figures above): Top N divided by final reports = 3.8% (2021-22), 3.9%
(2022-23), at most 3.1% (2023-24), at most 2.8% (2024-25), 2.1% (2025-26, 49/2,339). Finalists in 2025-26 were
11/2,339 = 0.47% of completing teams. Only 36-44% of registered teams submitted a final report in the years
where both numbers are given (1,400/3,200 in 2022-23; ~1,800/5,000 in 2024-25; ~2,300/6,300 in 2025-26).

---

## 2. Year by year

### 2.1 2021-22 (client Nichole Jordan)

Sources: [S17] [S18] [S19] [S20] [S26] [S24]

- **Client and case.** Nichole Jordan, Senior VP at Via (TransitTech), Wharton West EMBA. She wants a $5,000 a
  year scholarship for a woman of colour studying engineering at UC Davis, "for at least 10 years", starting in
  2022, and to help build generational wealth for six nieces and nephews. $100,000 to manage [S26]. The case
  itself asks: "Should she keep $50,000 in cash? Should she invest in stocks that pay dividends? Another option?
  Nichole wants to hear your plan for funding the scholarship." [S26]
  *This is the closest Wharton precedent to Laura's ten fixed $50k payments: a fixed yearly payment for ten
  years.* (My observation; the winning team's actual answer is not published.)
- **Numbers.** Trading began 27 Sep 2021 "with thousands of teams"; 1,300 teams submitted final reports on 13 Dec;
  Top 50 announced 20 Jan 2022; Top 10 named in virtual semifinals 14-16 Mar 2022 [S19]. "Nearly 1,300 final
  reports ... from students hailing from 64 countries" [S17].
- **How the Top 50 was chosen.** "After careful consideration by our internal reviewers and a group of
  professional asset managers from Aberdeen Standard Investments" [S17]. Teams could then still come from several
  schools (e.g. "BAKA Co.: Shady Side Academy, Pascack Hills High School, ..." ) [S17]; today's rules require one
  school [S22].
- **How finalists were chosen.** Top 50 "divided into five groups of 10"; five virtual events; "the top two teams
  from each group" advanced [S18]. 15 judges in five groups of three "review[ed] team presentations" [S18]. The
  article does not say whether presentations were videos (UNVERIFIED).
- **Finale.** In person at Huntsman Hall, the first on campus since 2019 [S19]. "10-minute strategy pitches";
  "panel of four judges"; "They were evaluated not only on their content, but also their delivery." [S19]
  Judges: John Zaia (Citi), Muk Rao (Wharton Research Data Services), Joe Rava (abrdn), Andrea Vittorelli
  (J.P. Morgan) [S19]. Teams' work "featured case studies that aligned with their strategies, including such
  diverse companies as Mastercard, HDFC Bank and The Hershey Company." [S19]
- **Winners.** 1st Sailing to Success (schools in Arizona), 2nd Sky Investments (Bergen County Academies),
  3rd M&R Investments (Marvin Ridge HS, defending champions) [S19].
- **What the article says the top teams did well.** Only general: "client-focused talk of dividends and growth
  stocks, ESG and risk management, all the while mindful of looming macrotrends like inflation and
  COVID-resistant economies" [S19]. Nothing specific about the winner's strategy.
- **Quotes.**
  - Judge Andrea Vittorelli: "less is more." ... "Cut slides, cut words, cut minutes…It's easier for the audience,
    who will say: 'they said five things and I remembered them all because I had time to actually process
    them.'" [S19]
  - Semifinal judge Dr. Dan Young: "The level of analysis of understanding for Nichole Jordan's situation was
    top-notch." [S18]
  - Semifinal judge Shawn Snyder (Citi): "The competition requires students to focus on quality control, the
    client experience, presentation skills, and teamwork." [S18]
  - Client Nichole Jordan "joked about the steady barrage of emails and social media requests during the
    competition from eager teams hoping to connect with their client" and said she had never felt more "seen"
    [S19]. (Contacting the client is now a disqualification offence [S22].)
  - Winning team leader (Frank, Sailing to Success): his greatest lesson was "adapting to change" [S19].
- **Criticism / mistakes.** Too much content (Vittorelli above) [S19]; teams contacting the client [S19].
- **Prizes.** Trophies for the top three; free place in Future of the Business World or Essentials of Leadership
  online programme for the winning team; certificates, t-shirts and swag for all top 10 [S19].
- **Learning Day (22 Apr 2022).** Dean Erika James; scavenger hunt; panel of past competitors now at Penn;
  session with Prof. Angela Duckworth on trial and error [S20].

### 2.2 2022-23 (client Peter Wang Hjemdahl)

Sources: [S12] [S13] [S14] [S15] [S16] [S27] [S24]

- **Client and case.** Peter Wang Hjemdahl, W'19, Chief Advocacy Officer at rePurpose Global (plastic waste).
  $100,000. Goal 1: put $20,000 in now and grow it so that by age 30 (five years) it funds a $5,000-$10,000 gift
  to a different start-up each year, "use the interest from that investment to sustain the fund". Goal 2: open a
  yoga and wellness centre in Miami within 15 years [S27]. The case asked: "how will your team stand out against
  competing teams? How will you create a compelling and clever pitch to convince Peter to choose your
  strategy?" [S27]
- **Numbers.** 3,200 registered teams from 53 countries; 1,400 final reports; 55 semifinalists [S14].
  Ten weeks of trading on WInS ended 2 Dec 2022 [S12].
- **How the Top 55 was chosen.** "internal reviewers and a group of professional asset managers from abrdn"
  [S12].
- **How finalists were chosen.** "A total of 15 judges, all finance professionals, spent a few weeks prior to the
  semifinal events evaluating semifinalist team video presentations to identify the top 10 finalists." [S13]
  Five virtual events over three days from the WAVE classroom, starting 8 a.m. on 20 Mar; "the top two teams from
  each group" advanced [S13].
- **Finale (22 Apr 2023).** "Each team had 10 minutes to pitch their unique investment strategies (tailored to
  competition client, Peter Wang Hjemdahl); detail their team analysis; make recommendations; and reflect on key
  competition takeaways. In the ensuing five minutes, they answered incisive questions from the judges." [S14]
  One team (Himalayan Melange, India) presented remotely, "the day's only remote presentation" [S14]; its advisor
  later said "we couldn't get the visa so we had to adjust and make last-moment changes to our presentation so we
  could present virtually" [S16]. Judges: Michael DeFlorio (Harvest Partners), Muk Rao (WRDS), Annie Feng
  (abrdn), Andrea Vittorelli (J.P. Morgan) [S14]. Deliberation took "the full hour and then some over lunch"
  [S14].
- **Winners.** 1st DMV's Finest (Thomas Jefferson HS for Science and Technology, VA); 2nd Amity 7 Chakras
  Investments (Amity Regional HS, CT); 3rd NovyPorg_1 (Nový PORG, Prague, Czechia) [S14].
- **What the article says the top teams did well.** About the field, not the winner: "professional slide decks,
  stock-filtering algorithms, international market analysis, carefully crafted portfolios, endless Environmental,
  Social & Governance considerations, and the "critical pillars" of their creative investment strategies" [S14].
  On the winner it says only that DMV's Finest "reached the final round in 2022" but did not place, and came back
  with "a few original members, as well as several new additions" [S14].
- **The winners' own lesson (most useful line in the archive).** DMV's Finest co-leader (Brian): "One of our
  most significant experiences during the competition was learning to trim things down. ... when we laid
  everything out in a rough draft of our final report and everything clicked — we really needed to cut things
  down. It also led us to reflect: less is more, and having an explainable strategy makes a lot more sense than
  going for so many different things at once." [S16]
- **Other quotes.**
  - Semifinal judge Dr. Wayne Williams: "Across the board, the presentations were excellent in terms of creativity
    and approach" [S13].
  - Finale judge Michael DeFlorio: "Everybody really deserved to be here." [S14]
  - DMV's Finest co-leader (Om): "Huge shoutout to the new members. We all carried our own weight." [S14]
  - Teacher-advisor Alex Lamon: "It is easier to develop a strategy first and buy stocks second. ... Remember,
    winning isn't about portfolio gains. It is about having a coherent strategy." [S16]
  - Academic director at the time, Serguei Netessine, promised "changes and new competitive experiences" for the
    next year [S14].
- **Criticism / mistakes.** Doing too many things at once; buying before having a strategy [S16].
- **Prizes.** Winners: scholarship to Future of the Business World or Essentials of Leadership; the champion
  school gets an automatic semifinal spot next year "as long as they submit all the deliverables"; trophies for
  all finalists [S14]. Top 55: certificates, swag box, digital badge [S13].
- **Learning Day (21 Apr 2023).** Dean James; Netessine on sustainable energy research; Prof. Patti Williams on
  brand purpose; scavenger hunt [S15].

### 2.3 2023-24 (client Hilary Ash)

Sources: [S8] [S9] [S10] [S11] [S36] [S24]

- **Client and case.** Hilary Ash, W'13, VP of games delivery and venue infrastructure for the LA 2028 Olympic
  and Paralympic Games [S9, S36]. Volleyball was "a passion highlighted in Hilary Ash's client profile that
  inspired great creativity among student teams' competition investment strategies" [S9]. The full case is not
  public (UNVERIFIED).
- **Numbers.** Launched 25 Sep 2023; trading ended 1 Dec; "more than 1,600 final reports from students
  representing 63 countries" [S8]. This was the year ETFs were added: team leaders spoke about "the addition of
  ETFs in this year's investment portfolios" [S9]. A midterm report existed ("Those of you who at least submitted
  midterm reports") [S8].
- **How the Top 50 was chosen.** "internal reviewers and a group of professional asset managers from abrdn in
  Philadelphia", plus one automatic spot for the previous champion's school [S8].
- **How finalists were chosen.** Judges "evaluated the teams' semifinal video presentations"; five virtual events
  in the WAVE room [S9]. Eleven teams advanced; the article does not explain why 11 rather than 10 (UNVERIFIED).
- **Finale (20 Apr 2024).** 11 presentations from teams from the U.S., India, China and Canada [S10]. Judges:
  Eric Balchunas (Bloomberg Intelligence, senior ETF analyst), Vikas Keswani (HPS Investment Partners), Zoe
  McCormick (abrdn, North American fixed income), Muk Rao (WRDS) [S10]. Presentation length not stated for this
  year (UNVERIFIED).
- **Winners.** 1st Spark Investments (Bergen County Academies, NJ); 2nd Wreckers Wealth Management (Staples HS,
  CT); 3rd DMV's Finest (Thomas Jefferson HS) [S10]. The 2nd-place leader said an ESG lecture was "integral to my
  investment strategy" [S11]. Spark's tagline: "Ignite the flame for your financial future." [S10]
- **What judges said impressed them.**
  - Vikas Keswani: "Everyone put a lot of thoughtful pieces of analysis into [your presentations], whether it was
    efficient frontier, cross correlations, diversification or portfolio theory. We enjoyed that. In some cases,
    there was a lot of it. And in some cases, there was a little bit of it, but a lot of depth and accuracy. That
    is one of the things that in my mind differentiated better performances." [S10]
  - Eric Balchunas (article's paraphrase, not a direct quote): praised the "next level" use of algorithms and
    machine learning, "while urging them (as investment advisors) to consider behavioral finance and their
    clients' emotions during a market downturn." [S10]
  - Zoe McCormick: "When analyzing someone's investments, take a look at this person holistically" (the article
    adds: "and consider their total financial picture") [S10].
  - Muk Rao: "If you all pursue the other things you love in your life with the same passion, the same honesty,
    the same rigor, you can do just about anything." [S10]
  - Semifinal judge Marcus Shaw (AltFinance): "I love the fact that people took different approaches to thinking
    about the macroeconomic factors and thinking about how do you assess that risk? How do you develop
    risk-monitoring metrics for different changes in the macro environment and other constraints around ESG? ...
    we had people that did straight fundamental bottom-up analysis, and we had people that utilized
    machine-learning algorithms to screen through a universe of securities. That's what's happening in the real
    world." [S9]
  - Semifinal judge Jeanette Ourada (retired Chevron VP and controller): "Your creative videos demonstrated your
    client focus and financial knowledge. The part I enjoyed the most was hearing about how you assessed each
    member's skills and learned to work together as a team." [S9]
  - Semifinal judge Joshua Tam (Laurel Avenue Management): "The one thing that stood out to me was the ability to
    connect the client's objectives to an investment strategy. I myself am pretty involved in volleyball, like the
    client. ... So, a lot of your creativity resonated with me." [S9]
  - Client Hilary Ash at the finale: "Congratulations to all of you because what you have done is incredibly
    impressive" [S10].
- **Criticism / mistakes (implied).** Analysis volume without depth and accuracy (Keswani); forgetting the
  client's emotions in a downturn (Balchunas); not looking at the client's whole financial picture (McCormick)
  [S10].
- **Prizes.** Winners: scholarship to an online programme; champion school's automatic semifinal spot; trophies
  for all finalists and plaques for the top three [S10]. Top 50: certificates, digital badges, swag and free
  access to PitchQuest, "a new AI-powered simulation" [S9].
- **Learning Day (19 Apr 2024).** Dean James on trust, the AI revolution and teamwork ("Establishing a set of
  common goals is really important.") [S11]; Netessine on material vs non-material ESG [S11]; BlackRock panel;
  scavenger hunt [S11].

### 2.4 2024-25 (client Ladi Ayoola)

Sources: [S4] [S5] [S6] [S7] [S28] [S24]

- **Client and case.** Ladi Ayoola, WG'22, at Visa; co-founder of Plugtent. $100,000 "a baseline". Impact hub in
  Lugbe, Abuja, Nigeria. Phase One: finance "at least five modest-income housing units by 2030" at about $10,000
  each "however, material costs and market dynamics are always changing". Phase Two in 2040: one storefront and a
  youth training centre ("at least $50,000") plus one year of operating costs ("at least a quarter of your original
  $100,000 investment or more"). Phase Three: expansion funded by returns by 2040 [S28].
- **Numbers.** "More than 5,000 registrations"; "more than 1,800 teams from 66 countries submitting final reports
  following the end of stock market trading on December 6, 2024"; launched 30 Sep 2024 [S4].
- **How the Top 50 was chosen.** "our internal reviewers and a group of professional asset managers", plus the
  automatic spot for the previous champion's school (Flame Investments, Bergen County Academies) [S4].
- **How finalists were chosen.** Client sent an encouraging video; five virtual events from 18 Mar 2025 in the
  WAVE room; "which two teams from each event would advance" [S5]. "It was a tight race for the 15 judges tasked
  with evaluating the semifinalist presentations!" The judges "reviewed and evaluated the 50 team presentation
  videos" in five groups of three [S5].
- **Finale (26 Apr 2025).** 64 students from the U.S., India and Canada [S6]. "Each team filled 10 minutes
  presenting its unique investment strategy pitch and portfolio analysis to a judging panel of four finance
  professionals, followed by five minutes of Q&A." [S6] Named judges: Chirag Jain (Aberdeen) and Muk Rao (WRDS);
  the other two are not named (UNVERIFIED). The client watched from the audience [S6].
- **Winners.** 1st BAM Investing (Deerfield Academy, MA); 2nd Finance from France (Lycée Français de Chicago,
  IL); 3rd FA Quakers (Friends Academy, NY) [S6].
- **What the article says the teams did well.** About all finalists, not the winner: "high school competitors
  flaunted 12 weeks of financial education and collaboration – rocking sentiment, SWOT and Pestel analyses,
  customized algorithms, AI innovations, portfolio optimizations, performance and readiness indices, and some
  clever house, tree and fashion metaphors." [S6] Teams created "investment strategies (and colorful slides!) to
  embrace his values and financial goals" [S6].
- **Quotes.**
  - Semifinal judge Melissa Ko Hahn (Covepoint Capital Advisors): "A lot of work went into putting your written
    reports and the videos together, and it clearly came across ... Overall, one of the tendencies of people who
    are just starting out is to fall into this trap of hiding behind fancy terms and formulas. I would encourage
    you to fight against that. Oftentimes, the best solutions are made up of simple, elegant ideas." [S5]
  - Finale judge Chirag Jain (Aberdeen; formerly reviewed manager pitches at Vanguard): "We met all kinds of
    managers with all kinds of investment philosophies and processes. What distinguished managers was clear
    thoughtfulness and reasoning behind all the decisions that they put together. I think you guys demonstrated
    that today." [S6]
  - Finale judge Muk Rao: "You're a better communicator now… you're better at advancing really complex
    arguments." The article says he "urged the students to see the power of defending their ideas." [S6]
  - Client Ladi Ayoola at the finale: "It was very evident that you put so much work into the research, analysis
    and presentations ... But beyond that was the human part. You were very impact-minded. For me, that's
    precious…Thank you for making the investment plans and proposals not just about the numbers, but about
    understanding and connecting with people." [S6]
  - Client Ladi Ayoola at the semifinals: "Success in investing and in life isn't just about the numbers; it's
    about understanding people. It's about recognizing opportunities and having the courage to make informed
    decisions." [S5]
  - 2nd-place team leader (Samuel, Finance from France): "We truly believe that it's not about what each person
    does best, but it's about the whole being greater than the sum of its parts." Advice: "Collaborate
    frequently, so you can iterate fast." [S6]
  - Semifinalist team leader (Chelsea, Nova Investments): "investing shouldn't be a gamble, rather a calculated
    decision based on sound analysis, research and hard work." [S5]
- **Criticism / mistakes.** "hiding behind fancy terms and formulas" (Ko Hahn) [S5].
- **Prizes.** Winners: scholarship to an online programme; automatic semifinal spot for the school; trophies and
  certificates for all finalists; plaques for the top three [S6]. Each Top 50 team member: paper and digital
  certificates and "a Wharton Global Youth online summer program for 50% off the tuition cost" [S5].
- **Learning Day (25 Apr 2025).** Netessine on renewable energy; Prof. Bilge Yilmaz on distressed investments and
  asset allocation; Wharton Ambassadors [S7]. The staff also announced "some reimagining of our signature
  competition" [S6].

### 2.5 2025-26 (client Connor Barwin)

Sources: [S1] [S2] [S3] [S21] [S24] [S32] [S44]

- **Client and case.** Connor Barwin, WG'23, former NFL player, founder of Make the World Better, "focuses on
  revitalizing community spaces and creating long-term impact". "Barwin's case encouraged students to think beyond
  financial returns and consider how their strategies could support long-term community impact." [S2] Full case
  not public (UNVERIFIED).
- **Changes that year.** "for the first time since the start of the competition in 2012, students were crafting
  compelling investment strategies and building investment portfolios with $500,000 in virtual cash, up from
  $100,000." [S3] Written deliverables were "a Midterm and a comprehensive Final Report" over 11 weeks [S32].
- **Numbers.** "more than 6,300 registered teams from around the world, an increase of 1,300+"; "On December 12,
  some 2,300 teams from 79 countries submitted final reports, an increase of nearly 30%" [S3]. A March post says
  "More than 5,400 high school teams ... began" [S2] (different from 6,300; not explained). The competition page
  counters (labelled "2025-2026 Participation Completion Numbers") read 2,339 teams, 79 countries, 12,145
  students, 1,625 advisors [S21].
- **How the Top 50 was chosen.** "with the help of our Wharton School student evaluators, as well as a
  professional review panel of asset managers from Aberdeen Investments in Philadelphia" [S3]. The list has 49
  teams under a "Top 50" headline, matching the later "49 semifinalist teams" [S3, S2]. The 2025 champion school
  (Deerfield) had a team in it [S3].
- **How finalists were chosen.** "49 semifinalist teams advanced to the virtual semifinal rounds, where they
  presented their strategies to panels of Wharton alumni and industry experts. This year, 11 teams have earned a
  place in the Global Finale." [S2] Teams were to "meet virtually the week of March 9 to learn the 10 teams" [S3]
  (11 went through). Fifteen semifinal judges are listed, mostly Wharton alumni running funds, family offices or
  businesses, plus the CEO of Stock-Trak (WInS runs on Stock-Trak; the FAQ's WInS login link is edu.stocktrak.com
  [S23]) and an educational consultant [S2]. Whether
  presentations were live or recorded is not stated (UNVERIFIED).
- **Finale (Saturday 25 Apr 2026).** Dates differ between posts: the January post says "April 24 and 25" [S3],
  the champions post says "April 25–26" [S1], the March post says "Saturday, April 25, 2026" [S2]. Five judges: Chirag Jain (U.S. Credit Investment Manager, Aberdeen
  Investments), Sachin Khajuria (Achilles), Kristopher Mastronardi (King Street), Valerie Ramirez Mukherjee (Zen
  Capital Partners), Mukund Rao (WRDS) [S1]. Format length not stated (UNVERIFIED). The client spoke at Learning
  Day and took students' questions "about his work and investment priorities" [S1].
- **Winners.** 1st FigCapital (Stuyvesant HS, NY); 2nd HHA Investments (Colégio Marista de Brasília, Brazil);
  3rd Riverhawk Traders (Farmington HS, CT) [S1]. (The Archive page spells it "Riverhawk Trades" [S24].)
- **What the article says the teams did well.** Only: "Each team demonstrated exceptional analytical thinking,
  creativity, and a deep understanding of their client's goals." [S1] No strategy details for any team.
- **Quotes.** Client Connor Barwin: "The biggest lesson I learned during my Wharton experience was to approach
  every problem with confidence that you can figure it out, and humility to know that you don't have all the
  answers." [S2]
- **Prizes.** Not stated in the 2026 articles (UNVERIFIED). Teams that competed "at least through the mid-term
  report submissions" got a participation badge in February [S3].

### 2.6 What is public now for 2026-27 (Laura Gao)

Sources: [S21] [S22] [S23] [S25]; repo files as cited.

- **Client.** "Each year, teams are introduced to a new case study featuring a Wharton School alum. While the
  client is real, the financial scenario is developed specifically for the competition." [S21] The case says
  Laura graduated from Wharton in 2018 (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:14-16`).
- **Evaluation in one line.** "Unlike other investment competitions, success is not determined by portfolio
  performance. Teams are evaluated on the quality of their investment strategy, how well it aligns with their
  client's objectives, the strength of their research and analysis, and their ability to clearly communicate and
  defend their recommendations." [S21]
- **Top 50.** "The top 50 teams will be selected as semifinalists based on the strength of their Investment Policy
  Statement (IPS) and Final Reports." [S22] The registered-team page says "Your Trading Notes Analysis, Investment
  Policy Statement and Final Report are evaluated." (`competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md:15`)
  So all three are scored, but the public rules name only the IPS and Final Report for semifinal selection. How
  much the TNA counts toward the Top 50 is UNVERIFIED. The IPS instructions add a hard gate: "Submissions that do
  not meet the requirements below will not be considered for semifinal selection."
  (`competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt:82-83`)
- **Semifinals and finale.** "Your team will be expected to create and deliver a short presentation (via video
  conference for the Semifinals and live or via video conference for the Global Finale) about your team's
  strategy, analysis and experience over the past 10 weeks to a live panel of judges. All team members must
  participate." [S23] "The Semifinals will be conducted virtually." Finalists "may participate either in person or
  virtually"; travel is at the team's cost; "Wharton Global Youth Program does not provide travel funding or
  sponsor visa applications." [S22] Learning Day and Global Finale: 29 and 30 April 2027 [S21] (a Thursday and a Friday by my calendar check; the
  2022-2026 finales were on Saturdays [S19, S14, S10, S6, S2]). Recording or
  posting semifinal or finale presentations is "strictly prohibited" [S22].
- **Feedback.** "Teams will not receive individual feedback." "We are looking for teams that score exceptionally
  well on all five components of the criteria, and that embrace all aspects of the competition with passion and
  creativity, which is then reflected in various ways in their final reports." [S23]
- **How to win (Wharton's own words).** "There is no single winning investment strategy. Strong teams understand
  the client, work effectively together, conduct thoughtful research and analysis, and develop a clear and creative
  strategy designed around the client's goals. Their investment decisions reflect that strategy, and their
  deliverables connect into a cohesive, well-supported submission. Just as importantly, successful teams
  communicate their reasoning, assumptions, tradeoffs, and competition experience clearly and authentically." [S23]
- **Prizes 2026-27.** Finalists: waived fee for the online course Understanding Your Money; champion team: a free
  online summer programme; the other nine finalist teams: 50% discount on a summer online programme; the champion
  school can fast-track one team to the 2027-28 semifinal; certificates for all semifinalists and finalists;
  digital credential in February 2027 for all eligible teams [S22].
- **Academic director.** Professor Michael R. Roberts (William H. Lawrence Professor of Finance) [S21]. Earlier
  years named Serguei Netessine as Global Youth's academic director [S14]. Whether Prof. Roberts judges any round
  is UNVERIFIED.

---

## 3. Wharton's standing guidance (pages that are not tied to one year)

- **Strategy must be stated up front (legacy guidebook page, undated; it links to the 2020 finale so it dates from
  about 2020-21).** "*Note: if you provide us with a team strategy that is buried somewhere in your experience,
  rather than clearly stated, defined and articulated up front, you will not be among the strongest teams.
  Defining your strategy early is essential to doing well. Can you tweak it? Absolutely!" Also: ""Buy low and
  sell high" is not an investment strategy." "Evaluators want to understand why you are doing what you are doing"
  and "We see teams buying lots of stocks and selling just as many." [S29] (Some details are outdated, e.g. it
  says only approved-list stocks are allowed.)
- **Trading from outside the U.S. (legacy page).** "We do NOT expect you to stay up in the middle of the night to
  place trades ... the Wharton Global High School Investment Competition is not a trading competition" [S30].
- **Learning objectives (2025-26 badge criteria PDF).** Includes: "Express an investment strategy clearly and
  demonstrate creative thinking to make that strategy memorable and unique." "Use stock analysis tools and
  strategies like SWOT and Porter's 5 Forces". "Demonstrate effective teamwork strategies through a collaborative
  and inclusive approach". "Communicate a clear, concise, and compelling written overview of the team's strategic
  and analytical approach to investing and investment decisions, as well as key tenets of the overall competition
  experience, such as teamwork and takeaways." [S32] (2025-26 document; whether the 2026-27 badge uses the same
  wording is UNVERIFIED.)
- **Staff statements of mission.** In a 2023 podcast, the Wharton Global Youth host called the competition's
  mission "to steer students away from risky short-term investing decisions, and help them see the value of
  analysis and long-term investing" and said "we really do stress that balance of qualitative and quantitative
  research." [S34]
- **Teacher advice published by Wharton (2021).** "If students do not know that client, they will not succeed!"
  "Developing a rationale and relating their investment decision to the potential client and a higher-level
  investment strategy is key to this competition." "The final report is the most important deliverable students
  produce." "if they are buying stocks without checking 'does this stock align with our overall thesis and/or
  investment strategy?' they are probably flying blind." [S31] (Written when the competition had a midterm and a
  final report and 4-7 member teams.)
- **Academic director's view of finance (2022 interview, about his summer course, not the competition).** "There's
  only one finance." "It rests on two intuitive principles: costs and benefits, and risk." "They realize that the
  jargon and acronyms are just obfuscating the elegant simplicity of finance." "to get 90% of it you really only
  need basic arithmetic and maybe a little bit of probability and statistics." [S33]
- **Ethics.** "We trust that you will not lie about your investment decisions and outcomes, fabricate analyses,
  invent teamwork and experiential stories, compensate advisors, education consultants, or other agents, ... or
  plagiarize existing strategies." [S22] The version on the AI policy page adds "pass AI generated writing or work
  off as your own" to that list [S25]. "All teams should review the CFA Institute's Asset Manager Code and operate
  by these standards." [S22] Advisors "may not make decisions on behalf of students or actively participate in team
  activities, trading decisions, or strategy development." [S22]
- **AI.** Rules page: "Teams may use generative AI tools (such as ChatGPT) for brainstorming and idea generation"
  ... "AI-generated work may not be submitted as your own." ... "Any AI-generated material included in your report
  must be properly cited" [S22]. The AI policy page goes further: "If you use AI to assist you in any way during
  the competition, how you use it must be recorded in your Works Cited pages." It lists checklist questions,
  including "Did I come to my current conclusion before or after using generative AI tools?" and "Did I understand
  the key learnings and how to arrive at the answers without the assistance of generative AI tools?" [S25] The same
  page's pre-baccalaureate section (not the competition section) says "Don't use AI for personal reflection or
  opinion-based tasks." [S25]

---

## 4. Cross-year patterns

### 4.1 What is praised again and again

| Theme | Evidence (year, who) |
|---|---|
| Simplicity, few clear ideas, no jargon | 2022 finale judge Vittorelli [S19]; 2023 champions "less is more" [S16]; 2024 finale judge Keswani on "depth and accuracy" [S10]; 2025 semifinal judge Ko Hahn "simple, elegant ideas" [S5]; academic director Roberts [S33] |
| Strategy linked to the client's goals and life | 2022 Young [S18]; 2024 Tam and Ourada [S9]; 2025 client Ayoola [S6, S5]; 2026 "deep understanding of their client's goals" [S1]; FAQ "designed around the client's goals" [S23] |
| Clear reasoning that survives questions | 2023 "incisive questions" [S14]; 2025 Jain and Rao [S6]; 2015 judges asked questions "to evaluate how well team members could think on their feet" [S43]; live-page criterion "communicate and defend" [S21] |
| Visible teamwork, every member contributing | 2022 Snyder [S18]; 2023 "We all carried our own weight" [S14]; 2024 Ourada [S9]; 2025 Samuel [S6]; FAQ "All team members must participate" [S23] |
| Creativity that makes the idea memorable | 2023 Williams [S13]; 2024 volleyball tie-ins [S9]; 2024 music theme (Beats from D-Street) [S9]; 2025 "house, tree and fashion metaphors" [S6]; badge objective "memorable and unique" [S32] |
| Quant tools used with depth | 2021 Monte Carlo [S37]; 2023 stock-filtering algorithms [S14]; 2024 efficient frontier, correlations, ML [S10, S9]; 2025 optimisation, algorithms, AI [S6] |
| Holistic, human view of the client | 2024 McCormick, Balchunas [S10]; 2025 Ayoola "the human part" [S6]; 2020 judge Luddy: "finance is not just about making money; it's about helping people achieve goals" [S40] |
| Discipline plus flexibility | 2021 judge Aquino: "maintain the discipline of your investment process and be flexible when things don't work out" [S37]; 2022 winner "adapting to change" [S19] |

### 4.2 Criticisms and common mistakes Wharton has published

1. Hiding behind "fancy terms and formulas" [S5].
2. Too many slides, words and minutes [S19]; trying "so many different things at once" [S16].
3. Lots of analysis without "depth and accuracy" (implied by Keswani) [S10].
4. Ignoring the client's emotions in a downturn and their total financial picture [S10].
5. A strategy "buried somewhere in your experience" instead of stated up front [S29].
6. Buying first and finding a strategy later [S16, S31]; heavy buying and selling [S29].
7. Contacting the client (a 2022 anecdote; now a disqualification offence) [S19, S22].
8. Wharton's FAQ warns that not making the Top 50 "does not necessarily mean that you did something
   "wrong."" The bar is to "score exceptionally well on all five components" [S23].

### 4.3 How the format changed

| Year | Change (source) |
|---|---|
| 2019-20 | Four regional finals, then the first virtual Global Finale (12 teams, video presentations plus judges' questions); OTIS simulator to be replaced by WInS [S40] |
| 2020-21 | Top 50 "regional finalists" in five regions; virtual finale of 10 teams answering judges' questions online; 972 final reports [S38, S39, S37] |
| 2021-22 | One global Top 50 in five virtual groups of 10, top 2 per group; in-person finale returns; multi-school teams still in the Top 50 [S17, S18, S19] |
| 2022-23 | Top 55; 15 judges score semifinal **video** presentations; finale 10 min + 5 min Q&A; one team presents remotely [S12, S13, S14] |
| 2023-24 | ETFs added; midterm report; 11 finalists [S9, S8] |
| 2024-25 | Semifinal judged on "50 team presentation videos"; finale 10 min + 5 min Q&A; "reimagining" announced [S5, S6] |
| 2025-26 | $500,000 virtual cash (first time; was $100,000); Midterm + Final Report; Top 50 read by Wharton student evaluators plus Aberdeen asset managers; semifinal teams "presented their strategies to panels"; five finale judges [S3, S32, S2, S1] |
| 2026-27 | Deliverables now Roster, Trading Notes Analysis, IPS, Final Report (no midterm); IPS freezes the strategy and trading on 6 Nov; Top 50 "based on" IPS and Final Reports; semifinal presentation "to a live panel of judges" by video conference; $300,000 virtual cash [S21, S22, S23; `competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt:60-61`; `competition/official/2026_27/smapply_public_2026-10-14/trading.txt:22`] |

Two quiet but important shifts: (a) the semifinal moved from **pre-recorded videos judged in advance**
(2022-23 to 2024-25, explicitly) [S13, S9, S5] to wording that implies a **live** video-conference presentation
(2026 "presented ... to panels" [S2]; 2026-27 FAQ "to a live panel of judges" [S23]); (b) the written strategy is
now **locked** before the Final Report (the IPS), so the Final Report evaluates, rather than designs, the strategy
(`competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt:60-61`).

### 4.4 Who judges

- **Top 50 (written).** "Internal reviewers" plus asset managers from Aberdeen / abrdn every year 2021-22 to
  2024-25 [S17, S12, S8, S4]; Wharton School student evaluators plus Aberdeen Investments in 2025-26 [S3].
- **Semifinal.** 15 judges in five groups of three (2021-22, 2024-25 lists) [S18, S5]; 15 listed in 2025-26 [S2].
  Several judges return year after year: Yanbing Qiu and Rajesh Sehgal (2022, 2025, 2026), Valerie Ramirez
  Mukherjee (2022 and 2025 semis, 2026 finale), Heather Crist (2022, 2026), and Pav Dharwarkar, Thom Phan, Roel
  Peeters, Patricia Werhahn and Mark Brookshire of Stock-Trak (2025 and 2026) [S18, S5, S2].
- **Finale.** Four judges (2022-2025), five in 2026 [S19, S14, S10, S6, S1]. Muk/Mukund Rao of WRDS sat on every
  finale panel from 2020 to 2026, seven years in a row [S40, S37, S19, S14, S10, S6, S1]; in 2025 the article
  called him a judge of "many years" standing ("who has judged the competition for many years") [S6]. There is an Aberdeen/abrdn person on every finale panel 2022-2026, and from
  2024 that person was a **fixed-income or credit specialist** (Zoe McCormick, North American fixed income, 2024;
  Chirag Jain, U.S. credit, 2025 and 2026) [S10, S6, S1].

### 4.5 International teams

- Share of each Top 50 from outside the U.S. (my count from the published lists; multi-country teams that include
  a U.S. school counted as U.S.): 2021-22 about 23 of 50 [S17]; 2022-23 28 of 55 (27 excluding Puerto Rico) [S12];
  2023-24 25 of 50 [S8]; 2024-25 20 of 50 [S4]; 2025-26 21 of 49 [S3]. India, China and Canada supply the most.
- Finalists from outside the U.S.: 2021-22 1 single-country (Indonesia) plus 2 mixed teams [S18]; 2022-23 4 of 10
  (India, South Korea, Czechia, Canada) [S13]; 2023-24 4 of 11 (China, India x2, Canada) [S9]; 2024-25 2 of 10
  (Canada, India) [S5]; 2025-26 4 of 11 (UK x2, Brazil, India) [S2].
- Podium places outside the U.S. in five years: NovyPorg_1, Czechia, 3rd in 2023 [S14]; HHA Investments, Brazil,
  2nd in 2026 [S1]. All five champions were U.S. teams [S24].
- **Australia and New Zealand.** Gryphon Group, Brisbane State High School, Australia: 2020-21 Top 50 regional
  finalist (Region 4) [S38] and 2021-22 Top 50 semifinalist [S17]. Kristin School, New Zealand: 2021-22 ("V") and
  2022-23 ("Dove Capital") semifinalists [S17, S12]. No Australian or New Zealand school appears in the 2023-24,
  2024-25 or 2025-26 lists [S8, S4, S3]. Knox Grammar does not appear in any list read for this report.
- Practical risks for far-away teams: a 2023 Indian finalist presented remotely after a visa problem [S14, S16];
  Wharton does not fund travel or sponsor visas [S22]. Past semifinal announcement events began at 8:00-8:30 a.m.
  Eastern [S18, S13], which is about 11 p.m. to midnight in Sydney in mid-March (UNVERIFIED for 2027 timings).

### 4.6 AI over time

- Judges praised machine-learning stock screens (2024) [S9, S10]; the 2025 finale article lists "AI innovations"
  among finalists' tools [S6]; Top 50 teams in 2024 got an "AI-powered simulation" as a prize [S9].
- At the same time the rules tightened: AI work "may not be submitted as your own", must be cited, and (AI policy
  page) "how you use it must be recorded in your Works Cited pages" [S22, S25]. The 2023 third-place leader said AI
  models "can't really even comprehend some of the logic of the markets" [S35].
- Nothing on the site says a team was penalised for AI use (no public record either way).

### 4.7 What the archive does NOT tell you

- No article since 2021-22 describes what the **winning** team's strategy actually was. Descriptions are of the
  whole finalist field ("teams dazzled ...", "high school competitors flaunted ...") [S14, S6], or one general
  sentence (2026) [S1].
- No public rubric weights, no scores, no example IPS or Final Report from a past winner, no list of common errors
  in written reports beyond the points in 4.2.

---

## 5. Checks against Caplet's own files (things that need fixing or care)

These are discrepancies between the team's files and Wharton's public record. Line numbers are as of 16 Oct 2026.

| # | Caplet file says | Wharton's record says | Why it matters |
|---|---|---|---|
| 1 | `docs/research_laura_gao_and_wins.md:35`: "the winner (Deerfield) combined SWOT, sentiment analysis and portfolio optimisation with a "human-centred" link to the client's values" | [S6] lists those tools for **all** finalists ("high school competitors flaunted ..."); "human-centred" does not appear (the client said "the human part"). | Misattributes field-wide tools to the winner. If repeated to the team as "what wins", it is not verified. |
| 2 | `docs/research_laura_gao_and_wins.md:37`: "the winner (TJHSST) used ESG as a "critical pillar."" and calls the 2022-23 case "the closest past analogue" | [S14] says "teams dazzled ... endless ... ESG considerations, and the "critical pillars" of their creative investment strategies" (the field, not the winner). The 2021-22 case (fixed $5,000 a year for at least 10 years) [S26] is a closer analogue to ten fixed payments. | Same misattribution; better precedent missed. |
| 3 | `COMPETITION.md:26`: "Semifinals: short video presentation" | 2026-27 FAQ: "short presentation (via video conference for the Semifinals ...) ... to a live panel of judges" [S23]; past years used pre-recorded videos [S13, S5]. | Prepare for live questions in the semifinal, not only a recorded video. Exact 2027 format UNVERIFIED. |
| 4 | `COMPETITION.md:34` and `:41`: three deliverables "judged together"; Top 50 "chosen on the written deliverables" | Rules: Top 50 "based on the strength of their ... IPS and Final Reports" [S22]; registered page: all three "are evaluated" (`SMApply_Deliverables_Page_2026-09-27.md:15`). | Both can be true, but the public rule names IPS + Final Report for semifinal selection. TNA weight UNVERIFIED. |
| 5 | `COMPETITION.md:49`: "Laura is a fictional client." | "While the client is real, the financial scenario is developed specifically for the competition." [S21] (Already flagged in the 15 Oct brief; still unfixed in the file.) | Tone and respect: judges' client is a real Wharton alum. |
| 6 | `docs/benchmark_against_previous_teams.md:44`: Amity "Successfully impressed judges by tying macroeconomic news sentiment to analyst growth expectations over three consecutive competition cycles." | Wharton's archive says nothing about Amity 7 Chakras' methods; it only lists the team as 2023 finalist and 2nd place [S13, S14]. | UNVERIFIED claim presented as fact. |
| 7 | `CLAUDE.md:40`: lesson from 2025-26, "strategy packaging was over-complex for the insight" | Matches the single most repeated judge message (section 4.1, row 1). | Confirms the team's own lesson with Wharton evidence. |

---

## 6. What this means for Caplet (pointers for the merge, not text to submit)

1. **Simplicity test for every judge-facing idea.** Past judges punished jargon and volume. A useful check: can
   each idea in the IPS be said in one plain sentence that a non-finance adult understands? Can the whole
   strategy be remembered as a few things (Vittorelli's "they said five things and I remembered them all")? [S19]
2. **Client link on every page.** Judges praised the link from client goals to strategy more than any tool
   [S9, S18]. For each holding and rule, the team should be able to say which of Laura's goals it serves.
3. **Expect a bond specialist on the finale panel.** Aberdeen's finale judge in 2025 and 2026 was a credit
   specialist; in 2024, a fixed-income manager [S6, S1, S10]. A Treasury-ladder strategy will meet expert
   questions (for example, why iBond ETFs vs individual Treasuries, reinvestment, inflation, duration). The team
   must answer these in its own words.
4. **Build for live questions.** Finales have 5 minutes of questions [S14, S6], and the 2026-27 semifinal wording
   says "live panel" [S23]. Practise defending choices, not just presenting them (Rao: "defending their ideas")
   [S6].
5. **Show the team, not just the plan.** Each member visible, with a real role and a real learning story. Ethics
   rules forbid inventing "teamwork and experiential stories" [S22].
6. **Quant is table stakes.** Monte Carlo, optimisation and ML do not differentiate on their own [S10, S37, S6].
   Depth, accuracy and a clear "so what" do [S10].
7. **Human side of the client.** Judges asked teams to consider the client's emotions in a downturn and the whole
   financial picture [S10]; the 2025 client valued the "human part" [S6]. For Laura, that points to how she (and her
   co-sponsors) would feel about the range she announces in 2031, and her total situation beyond this portfolio.
8. **A memorable, client-specific theme can help if it stays simple.** Volleyball tie-ins resonated with a 2024
   judge [S9]; 2025 finalists used house and tree metaphors [S6]. Laura is a graphic novelist and storyteller
   (`Laura_Gao_2026_Client_Profile.txt:13-23`); whether to use that is the team's call.
9. **Log AI use now.** Works Cited must record how AI was used "in any way during the competition" [S25]. Given how
   much AI research this repo holds, start the log before the TNA.
10. **Precedent.** Wharton has set a "fixed payment for ten years" problem before (2021-22) and openly asked "keep
    $50,000 in cash? ... dividends? Another option?" [S26]. A liability-matching answer is therefore an expected
    type of answer, not a surprise; the edge has to come from clarity, client insight and defence (my inference).

---

## 7. Open questions / UNVERIFIED items

- Exact 2027 semifinal format (live vs recorded, length, Q&A) and timings: UNVERIFIED beyond [S23].
- Weight of the Trading Notes Analysis in Top 50 selection: UNVERIFIED (rules name IPS + Final Report [S22]).
- Whether Wharton student evaluators read 2026-27 reports again: UNVERIFIED (stated for 2025-26 only [S3]).
- Why 11 finalists in 2023-24 and 2025-26 instead of 10: not explained [S9, S2].
- 2024 and 2026 finale presentation lengths: not stated [S10, S1].
- The 2025-26 Top 50 headline vs 49 teams listed; 6,300 registered vs 5,400 "began": not explained [S3, S2].
- Strategies of any champion since 2021-22: not published by Wharton.
- 2023-24 and 2025-26 full case studies: not public.
- Old "Previous Winners" and "Judging and Evaluation" pages: unreachable (Wayback blocked).
- Prizes for 2025-26: not stated in the articles.
- YouTube channel: lists "Investing Workshop 1-7" (Madness of Markets, Investing Strategies, Financial Statement
  Analysis, Technical Analysis, Managing Risk, Behavioral Finance, Portfolio Management) and "Meet the Experts:
  ETF Basics with Jeremy Schwartz" [S45]; dates and whether they are competition webinars: UNVERIFIED.

**Earlier years (context only, outside the 2021-26 scope).** 2015 finale: a "10-minute overview of its investment
strategy and teamwork approach" plus "a case study of one stock", then judges' questions [S43]. 2018 Region 2
finale: winners had "top scores in all areas of judging, including strength and clarity of investment strategy,
articulation of strategy and competition experience, understanding of investing concepts, presentation skills,
team member participation and creativity" [S42]; none of the teams "used notes" [S42]. 2019: a team got to know the
client on Twitter [S41] (contact is now banned [S22]). 2020: "Teams are judged on the strength and creativity of
their strategies, not on the amount of money they make in their portfolios." [S40]

---

## 8. Source list (all accessed 16 Oct 2026)

Wharton Global Youth Program news and pages (base `https://globalyouth.wharton.upenn.edu`):

| Tag | Title (date) | URL |
|---|---|---|
| S1 | Stuyvesant High School Wins the 2026 Wharton Global High School Investment Competition (30 Apr 2026) | https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/ |
| S2 | 11 Teams Advance to the 2026 ... Global Finale (20 Mar 2026) | https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/ |
| S3 | A Winning Season: Thousands of Teams, Bigger Stakes, and the Top 50 2026 ... (27 Jan 2026) | https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/ |
| S4 | Announcing the 50 Semifinalists in the 2025 ... (30 Jan 2025) | https://globalyouth.wharton.upenn.edu/news/announcing-the-semifinalists-in-the-2025-wharton-global-high-school-investment-competition/ |
| S5 | 'Let's Go!:' Announcing the Top 10 Teams ... 2025 Global Finale (24 Mar 2025) | https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/ |
| S6 | BAM Investing from Deerfield Academy, Massachusetts, Wins the 2025 ... (1 May 2025) | https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/ |
| S7 | Learning Day Is All Light and TastyKakes for this Year's Investment Competitors (5 May 2025) | https://globalyouth.wharton.upenn.edu/news/learning-day-is-all-light-and-tastykakes-for-this-years-investment-competitors/ |
| S8 | Here Are the Top 50 Teams Advancing to ... 2024 Investment Competition Semifinals (26 Jan 2024) | https://globalyouth.wharton.upenn.edu/news/here-are-the-top-50-teams-advancing-to-wharton-global-youths-2024-investment-competition-semifinals/ |
| S9 | Wharton Global Youth Hosts Five Virtual Events to Announce the 2024 ... Finalists (25 Mar 2024) | https://globalyouth.wharton.upenn.edu/news/wharton-global-youth-hosts-five-virtual-events-to-announce-the-2024-investment-competition-finalists/ |
| S10 | Spark Investments, Bergen County Academies ... 2024 ... Global Finale (23 Apr 2024) | https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/ |
| S11 | Learning Day 2024 Delivers Knowledge, Networking and Gaming on Locust Walk (1 May 2024) | https://globalyouth.wharton.upenn.edu/news/learning-day-2024-delivers-knowledge-networking-and-gaming-on-locust-walk/ |
| S12 | Congratulations to This Year's Investment Competition Semifinalists! (26 Jan 2023) | https://globalyouth.wharton.upenn.edu/news/congratulations-to-our-2023-investment-competition-semifinalists/ |
| S13 | Celebrating the Top 10 Teams in the 2022-2023 ... (23 Mar 2023) | https://globalyouth.wharton.upenn.edu/news/celebrating-the-top-10-teams-in-the-2022-2023-wharton-global-high-school-investment-competition/ |
| S14 | Our 2023 Investment Competition Global Finale Ends in Sweet Victory for DMV's Finest (26 Apr 2023) | https://globalyouth.wharton.upenn.edu/news/the-2023-investment-competition-global-finale-ends-in-sweet-victory-for-dmvs-finest/ |
| S15 | Learning Day 2023 Is a Big Hit with Investment Competitors (2 May 2023) | https://globalyouth.wharton.upenn.edu/news/learning-day-2023-big-hit-investment-competitors/ |
| S16 | Wharton Investment Competition: Tales from the 2023 Teams (6 Jun 2023) | https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/ |
| S17 | Introducing the 2022 Semifinalists ... (21 Jan 2022) | https://globalyouth.wharton.upenn.edu/news/introducing-the-2022-semifinalists-in-the-wharton-global-high-school-investment-competition/ |
| S18 | Announcing the Top 10 Teams Advancing to Our 2022 ... Grand Finale (18 Mar 2022) | https://globalyouth.wharton.upenn.edu/news/announcing-the-top-10-teams-advancing-to-our-2022-investment-competition-grand-finale/ |
| S19 | Top Teams 'Sail to Success' in the 2022 ... Global Finale (28 Apr 2022) | https://globalyouth.wharton.upenn.edu/news/top-teams-sail-to-success-in-the-2022-wharton-investment-competition-global-finale/ |
| S20 | 'Tomorrow's Thinkers and Leaders' Discover Wharton During Global Youth's Learning Day 2022 (28 Apr 2022) | https://globalyouth.wharton.upenn.edu/news/tomorrows-thinkers-and-leaders-discover-wharton-during-global-youths-learning-day-2022/ |
| S21 | Investment Competition (live page; 2026-27 dates; academic director; "Numbers from Last Year" counters in page HTML) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ |
| S22 | General Rules & Roles (live) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ |
| S23 | Frequently Asked Questions (live) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/ |
| S24 | Archive: Previous Winners and Clients (live) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/ |
| S25 | Wharton Global Youth Program Statement of AI Use / AI Policy (live) | https://globalyouth.wharton.upenn.edu/ai-policy/ |
| S26 | Case Study for 2021-2022 (Nichole Jordan) | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/ |
| S27 | Case Study for 2022-2023 (Peter Wang Hjemdahl) | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2022-2023/ |
| S28 | Case Study for 2024-2025 (Ladi Ayoola) | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/ |
| S29 | Developing a Strategy (legacy guidebook page, undated) | https://globalyouth.wharton.upenn.edu/developing-strategy/ |
| S30 | Trading Outside the U.S. (legacy guidebook page, undated) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/trading/ |
| S31 | The Essential Educator: 10 Tips for Teaching the Wharton Investment Competition (8 Sep 2021, by Alex Lamon) | https://globalyouth.wharton.upenn.edu/essential-educator-blog/the-essential-educator-10-tips-for-teaching-the-wharton-investment-competition/ |
| S32 | 2025-2026: Competition Participant Badge Criteria (PDF) | https://globalyouth.wharton.upenn.edu/wp-content/uploads/2026/01/25-26-Participant-Badge-Evidence.pdf |
| S33 | Prof. Michael Roberts Wants Global Youth Students to Discover the 'Elegant Simplicity' of Finance (31 May 2022) | https://globalyouth.wharton.upenn.edu/news/prof-michael-roberts-wants-global-youth-students-to-discover-the-elegant-simplicity-of-finance/ |
| S34 | The Minvest Mission to Empower Gen Z Investors (podcast, 30 Mar 2023) | https://globalyouth.wharton.upenn.edu/articles/future-of-the-business-world-podcast/the-minvest-mission-to-empower-gen-z-investors/ |
| S35 | The Wharton Investment Competition Sparks a Passion for Finance (podcast, 16 Apr 2024) | https://globalyouth.wharton.upenn.edu/articles/future-of-the-business-world-podcast/the-wharton-investment-competition-sparks-a-passion-for-finance/ |
| S36 | 6 Questions for Hilary Ash of the Los Angeles 2028 Olympic and Paralympic Games (2 Jan 2024) | https://globalyouth.wharton.upenn.edu/articles/sports-and-media/6-questions-for-hilary-ash-of-the-los-angeles-2028-olympic-and-paralympic-games/ |
| S37 | M&R Investments Takes First Place in Our 2021 Global Finale (11 May 2021) | https://globalyouth.wharton.upenn.edu/news/mr-investments-first-place-2021-investment-competition/ |
| S38 | Fierce 50: Meet the 2021 ... Regional Finalists (19 Jan 2021) | https://globalyouth.wharton.upenn.edu/news/meet-2021-wharton-global-high-school-investment-competition-regional-finalists/ |
| S39 | Announcing the Regional Winners of Our 2020-2021 Investment Competition! (26 Mar 2021) | https://globalyouth.wharton.upenn.edu/news/regional-winners-wharton-global_youth_2020-2021-investment-competition/ |
| S40 | Our 2020 Investment Competition Global Finale Ends in a Tie for First Place (11 May 2020) | https://globalyouth.wharton.upenn.edu/news/2020-investment-competition-global-finale-ends-tie-first-place/ |
| S41 | The 2019 Investment Competition Global Finale Showcases Financial Literacy at Its Finest (9 May 2019) | https://globalyouth.wharton.upenn.edu/news/2019-investment-competition-global-finale-showcases-financial-literacy-finest/ |
| S42 | Bangalore Is Abuzz Over the Results of the KWHS Investment Competition Region 2 Finale (8 Mar 2018) | https://globalyouth.wharton.upenn.edu/news/bangalore-abuzz-results-kwhs-investment-competition-region-2-finale/ |
| S43 | The Results Are In: Western Trade Wrangles Top Honors (8 May 2015) | https://globalyouth.wharton.upenn.edu/news/the-results-are-in-western-trade-wrangles-top-honors/ |
| S44 | Wharton Global High School Investment Competition Hosts Future Business Leaders (Wharton School story; same text as S1) | https://www.wharton.upenn.edu/story/wharton-global-high-school-investment-competition-hosts-future-business-leaders/ |
| S45 | Wharton Global Youth Program YouTube channel, videos tab (titles only) | https://www.youtube.com/user/WhartonHS/videos |

Repo files cited (read-only, 16 Oct 2026): `COMPETITION.md:26,34,41,49`; `CLAUDE.md:40`;
`docs/research_laura_gao_and_wins.md:35,37`; `docs/benchmark_against_previous_teams.md:44`;
`competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md:15,48-57`;
`competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt:60-61,74-79,180-187`;
`competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt:82-83`;
`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:13-23`;
`competition/official/2026_27/smapply_public_2026-10-14/trading.txt:22`.

Not reachable: `http://web.archive.org/...` (blocked by egress policy, HTTP 403); the 2023-24 and 2025-26 case
study URLs (404); YouTube watch pages (no description returned).
