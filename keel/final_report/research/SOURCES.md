# Sources register: where every source label in the Final Report research leads

Built Sat 14 Nov 2026 (Sydney), after Caplet asked where to find the sources the research files call "Source W8",
"W15b", "T14" or "W7". The research files use short labels to keep their tables narrow, and some never said where the
label is defined. This page lists every label family, what it means, where it is defined and how to reach the source
itself. Section 1 answers most questions; the full lists follow. Links are relative to this folder
(`keel/final_report/research/`), so they open on the portal and on GitHub alike.

## 1. The short answer

| You see | It means | Read it here |
|---|---|---|
| "Source W8", "[W15b]", "(W7)" | One of Wharton's own web pages (or the client case), read Sun 8 Nov 2026 for the note on why Wharton runs the competition | Section 3, the full list with links (copied from the end of [meta/WHY_WHARTON.md](meta/WHY_WHARTON.md)) |
| "T14", "(T12)", "T05" (two digits, T00 to T14) | One of the fifteen tabs of the FINAL REPORT Google Doc's Research section, saved as text files on 8 Nov | Section 4, a link to each file and to each tab's own source list |
| "card Q5e", "Q9c" | A research card in `cards/` | Section 5, every card with its file and where its sources are |
| "Q2b S26" | Card Q2b, source S26 of that card's Sources list | The card's Sources section (line numbers in section 5) |
| "Q2a r6" | Card Q2a, row 6 of the card's main table | The card |
| "row 300" or "#45" in a card's sources | Entry 300 or 45 of [REFERENCES_APA.md](REFERENCES_APA.md), the APA 7 list checked at the source | REFERENCES_APA.md |
| "R1", "B7a", "BRIEF", "Guide p.3" | Older research files and official documents the notes build on | Section 6 |
| "H9", "H9-042", "Q5c-003", "LOG #874", "RL 7", "W04b" | A harvest file, a row of the insight store, or a harvest's own location code | Section 7 |
| "case p.3", "IPS l.13", "TNA l.5", "WN l.16" | A page or line of the client case, Caplet's submitted IPS, its submitted Trading Notes or the WInS trade notes | Section 8 |
| "CANON B4", "NUMBERS 8o", "CASE_MAP E", "I101", "Book 14", "EXPECTATIONS T22" | Keel's own planning files and Caplet's instructions, not outside sources | Section 8 |

## 2. Labels that look alike

- **W8, W-08 and W04b are three different things.** W8 is a Wharton page (section 3). W-08 is one of Keel's Window
  room experiments (`keel/rooms/window/`, used in harvest H8). W04b is a reading file from the
  night before the IPS, [04b_WIDE_RESEARCH.md](../../ips_rewrite/final_night/other_thread/harvest/04b_WIDE_RESEARCH.md),
  used in harvest H7.
- **T has four meanings.** T00 to T14, always two digits, are the Google Doc tabs (section 4). T1 to T33 are the
  candidate rows for the monitoring table in cards [Q26](cards/Q26_monitoring_table.md) (l.218-250) and
  [Q30](cards/Q30_table3_cut_and_xdate.md) (l.264-296); card Q4c's "T10, T11, T21" mean these. T1 to T22 in
  [keel/EXPECTATIONS.md](../../EXPECTATIONS.md) (l.758-779) are tensions between Caplet's instructions. "FUSIONS T10" in
  harvest H4 is test 10 in [R07_synergies/FUSIONS.md](../../ips_rewrite/research/R07_synergies/FUSIONS.md).
- **S has four meanings.** In a card, S1 or S26 is that card's own numbered source. In harvests H4 and H5, S1 to S6 are
  Keel's six scout files (`keel/ips_rewrite/research/R07_synergies/scouts/`). In harvest H8,
  S0 to S9 are model worlds (S0 base, S1 rates and shares fall together, and so on; H8 l.5). In harvest H6, "S" is
  READING_SHILLER.md and "S-n" after a Damodaran packet is PDF page n.
- **I101 and I-01.** I101 is Caplet's instruction 101 in [keel/INSTRUCTIONS.md](../../INSTRUCTIONS.md). I-01 is idea 1
  in [keel/IDEAS.md](../../IDEAS.md).
- **L-01 and L1.** L-01 to L-19 are Keel's lab experiments (`keel/rooms/lab/`, index [lab.md](../../rooms/lab.md)). "Shiller L-1" is
  lecture 1 of Shiller's Yale course (harvest H6).
- **CANON and CASE_MAP both use letters.** [CANON.md](../CANON.md) tables: A commitments, B facts and figures, C loose
  phrases, D tensions, E the frozen WInS book (so "CANON B4" is row 4 of table B). [CASE_MAP.md](../CASE_MAP.md)
  sections: A1-A13 the case's requirements, B Wharton's five criteria, C open analysis, D coverage, E Wharton's Final
  Report instructions.

## 3. W1 to W35: Wharton's pages, read Sun 8 Nov 2026

Defined at the end of [meta/WHY_WHARTON.md](meta/WHY_WHARTON.md) and used there, in
[meta/META_ANGLES.md](meta/META_ANGLES.md) and in [harvest/H10_why_wharton.md](harvest/H10_why_wharton.md). There is
no W11; W15b sits between W15 and W16. Each entry gives the publisher (Wharton Global Youth unless named), the title,
the date and the link, exactly as recorded on 8 Nov. These are planning sources about the competition. None is yet an
APA entry in REFERENCES_APA.md: any one the report cites is read again at the source and carded first. Three
(W33 to W35) are public pages about Laura Gao; the case wins wherever they differ, and she is never contacted.

- W1. Client Case Study (repo): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, pp.1-4.
- W2. Wharton Global Youth, 2021-2022 Annual Report (PDF), timeline "Global Youth at a Glance":
  https://globalyouth.wharton.upenn.edu/wp-content/uploads/2024/10/2021-2022-WGYP-Annual-Report_vF.pdf
- W3. Wharton Global Youth, Annual Report 2024-2025 (PDF), mission statement and "2024-25 Investment Competition at a
  Glance": https://globalyouth.wharton.upenn.edu/wp-content/uploads/2025/10/2025-WGY-Annual-Report_F.pdf
- W4. Competition Archive, "Previous Winners and Clients":
  https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/
- W5. Competition FAQ: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/
- W6. Competition page (About, Academic Director, Why Join):
  https://globalyouth.wharton.upenn.edu/competitions/investment-competition/
- W7. 2025-26 Participant Badge Evidence (PDF), learning objectives:
  https://globalyouth.wharton.upenn.edu/wp-content/uploads/2026/01/25-26-Participant-Badge-Evidence.pdf
- W8. Guidebook, "Competition Deliverables" (2020-21 season page, still live):
  https://globalyouth.wharton.upenn.edu/competition-deliverables
- W9. General Rules & Roles: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/
- W10. Statement of AI Use and competition ethics: https://globalyouth.wharton.upenn.edu/ai-policy/
- W12. "A Winning Season ... Top 50 2026" (27 Jan 2026):
  https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
- W13. "11 Teams Advance to the 2026 ... Global Finale" (20 Mar 2026), semifinal judges and Barwin quote:
  https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/
- W14. "'Let's Go!': ... Top 10 Teams ... 2025 Global Finale" (24 Mar 2025), 2025 semifinal judges, Hahn, Ayoola:
  https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/
- W15. "Stuyvesant High School Wins the 2026 ..." (30 Apr 2026), finale judges:
  https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/
- W15b. "BAM Investing from Deerfield Academy ... Wins the 2025 ..." (1 May 2025), Jain, Rao, Ayoola, "reimagining":
  https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/
- W16. "Spark Investments ... 2024 Investment Competition Global Finale" (23 Apr 2024):
  https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/
- W17. "Top Teams 'Sail to Success' in the 2022 ... Global Finale" (28 Apr 2022), Vittorelli's title and advice:
  https://globalyouth.wharton.upenn.edu/news/top-teams-sail-to-success-in-the-2022-wharton-investment-competition-global-finale/
- W18. Wharton Global, "Top Teams Face Off in 2018 KWHS Investment Competition Global Finale" (14 May 2018):
  https://global.wharton.upenn.edu/story/top-high-school-teams-face-off-2018-kwhs-investment-competition-global-finale/
- W19. KWHS, "Tapping the Entrepreneurial Spirit of Miami-Dade High School Students" (16 Apr 2012), KWHS mission:
  https://globalyouth.wharton.upenn.edu/news/tapping-the-entrepreneurial-spirit-of-miami-dade-high-school-students
- W20. "Learning Day 2023 Is a Big Hit with Investment Competitors" (2 May 2023):
  https://globalyouth.wharton.upenn.edu/news/learning-day-2023-big-hit-investment-competitors
- W21. "Prof. Michael Roberts Wants Global Youth Students to Discover the 'Elegant Simplicity' of Finance" (31 May
  2022): https://globalyouth.wharton.upenn.edu/news/prof-michael-roberts-wants-global-youth-students-to-discover-the-elegant-simplicity-of-finance/
- W22. Wharton Executive Education, "Investing in Wisdom: Michael Roberts' Loyal Following" (Mar 2026), courses he
  directs: https://executiveeducation.wharton.upenn.edu/thought-leadership/wharton-at-work/2026/03/the-secrets-behind-michael-roberts-loyal-following/
- W23. PR Newswire, "Aberdeen Invests in Philadelphia's Future" (24 May 2012):
  https://www.prnewswire.com/news-releases/aberdeen-invests-in-philadelphias-future-153740865.html
- W24. "The 2014 Investment Competition Finale Goes Global" (30 May 2014), Gary Marshall quote:
  https://globalyouth.wharton.upenn.edu/news/2014-investment-competition-finale-goes-global
- W25. PR Newswire, "Aberdeen Asset Management Embarks on a Mission of Financial Literacy" (5 Apr 2016):
  https://www.prnewswire.com/news-releases/aberdeen-asset-management-embarks-on-a-mission-of-financial-literacy-300246315.html
- W26. Wharton Alumni, "A Wharton Program that Engages High School Students from Around the World" (6 Nov 2019):
  https://alumni.wharton.upenn.edu/all-stories/a-wharton-program-that-engages-high-school-students-from-around-the-world
- W27. en.wghs.org.cn (a third-party Chinese site, not Wharton's), home page: https://en.wghs.org.cn/ [Secondary;
  cited only as evidence of the coaching market; several of its "rules" are out of date]
- W28. River Journal Online, "Croton Harmon High School Team to Compete in Semifinals ..." (6 Feb 2024), reprinting
  Wharton's announcement with quotes from Netessine, Fionna Ross (abrdn) and Lesser:
  http://riverjournalonline.com/schools/croton-harmon-high-school-team-to-compete-in-semifinals-of-the-wharton-investment-competition/98701
- W29. Case Study for 2021-2022 (Nichole Jordan):
  https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022
- W30. Case Study for 2023-2024 (Hilary Ash):
  https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2023-2024
- W31. Case Study for 2024-2025 (Ladi Ayoola):
  https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025
- W32. Wharton Global Youth Program, Facebook post (7 Oct 2026):
  https://www.facebook.com/whartonyouth/posts/the-2026-2027investment-competition-is-officially-underway-this-year-student-tea/1562895109213335
  [Snippet]
- W33. Wharton Magazine, "A Wharton Grad From Wuhan's Exploration of Identity" (6 Apr 2022):
  https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/
- W34. Wharton Stories, "How (Not) to Plan a Case Competition in 30 Days" (9 Jan 2018), by Laura Gao W'18:
  https://www.wharton.upenn.edu/story/not-plan-case-competition-30-days/
- W35. Poets&Quants for Undergrads, "2018 Best & Brightest: Laura Gao, Wharton School" (30 Mar 2018):
  https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/ [Secondary]

## 4. T00 to T14: the FINAL REPORT Google Doc's Research tabs, saved Sun 8 Nov 2026

Plain-text copies of every tab under "Research" in Caplet's FINAL REPORT Google Doc, plus the "Winning Team Portrait"
tab, in [keel/library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/README.md).
The key was first given in [harvest/H9_doc_research_tabs.md](harvest/H9_doc_research_tabs.md) l.4. Tabs 07 to 13
each end with their own source list and a fact-check log; "T12 l.92" means line 92 of that file. T00 to T06 hold no
web links of their own.

| Label | File | What it is | Its own source list |
|---|---|---|---|
| T00 | [00_criteria_map.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/00_criteria_map.txt) | Criteria map: where each judging criterion is served | - |
| T01 | [01_experience_with_caplet_edits.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/01_experience_with_caplet_edits.txt) | Caplet's own edits to the Experience tab (first person) | - |
| T02 | [02_client.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/02_client.txt) | Client: Laura Gao, inside out (corrected to the IPS on 8 Nov) | - |
| T03 | [03_numbers_and_models.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/03_numbers_and_models.txt) | Numbers and models (old designs; NUMBERS.md replaces it) | - |
| T04 | [04_ideas_and_sources.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/04_ideas_and_sources.txt) | Ideas and sources behind the strategy | - |
| T05 | [05_cosponsor_brief.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/05_cosponsor_brief.txt) | Co-sponsor brief: the 2031 range, confidence and draft text | - |
| T06 | [06_max_out_plan.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/06_max_out_plan.txt) | Max-out plan, criterion by criterion | - |
| T07 | [07_deep_laura_gao.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/07_deep_laura_gao.txt) | Deep research: Laura Gao, inside out | l.93; fact-check log l.115 |
| T08 | [08_deep_taiwan.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/08_deep_taiwan.txt) | Deep research: the Taiwan residency landscape | l.99; fact-check log l.123 |
| T09 | [09_deep_markets_assumptions.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/09_deep_markets_assumptions.txt) | Deep research: markets and assumptions, Nov 2026 | l.72; fact-check log l.87 |
| T10 | [10_deep_methods_charts.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/10_deep_methods_charts.txt) | Deep research: analysis methods and charts | l.103; fact-check log l.129 |
| T11 | [11_deep_cosponsors_uncertainty.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/11_deep_cosponsors_uncertainty.txt) | Deep research: co-sponsors and communicating uncertainty | l.79; fact-check log l.102 |
| T12 | [12_deep_competition_intel.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/12_deep_competition_intel.txt) | Deep research: competition intelligence (criteria wording, rules, CFA Code, past teams) | l.92; fact-check log l.112 |
| T13 | [13_deep_experience_episodes.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/13_deep_experience_episodes.txt) | Deep research: articulating the competition experience | l.83; fact-check log l.100 |
| T14 | [14_docs_winning_team_portrait.txt](../../library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/14_docs_winning_team_portrait.txt) | What a winning team looks like, and how to score ourselves (2015-16 guidebook, past finales) | l.80, 17 public pages read 29 Sep (listed below) |

**T14's source list** (all accessed 29 Sep 2026, copied from the file). The meta notes cite T14 for the 2015-16
guidebook ("ROI ... important" but not the main factor), for "no Australian team in the Top 50 in 2024, 2025 or 2026",
for the 2024 winner's efficient frontier and for "no winning written report is public".

- Competition archive: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/
- FAQ: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/
- Rules & roles: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/
- 2015-16 guidebook: https://globalyouth.wharton.upenn.edu/wp-content/uploads/2015/10/2015-2016-KWHS-Investment-Competition-Guidebook.Global-Regions.pdf
- Eli Lesser interview: https://alumni.wharton.upenn.edu/all-stories/a-wharton-program-that-engages-high-school-students-from-around-the-world/
- abrdn release (2023): https://www.aberdeenplc.com/en-gb/news/all-news/abrdn-enters-second-decade-supporting-wharton-investment-competition-for-students
- 2020 finale: https://globalyouth.wharton.upenn.edu/news/2020-investment-competition-global-finale-ends-tie-first-place/
- 2021 finale: https://globalyouth.wharton.upenn.edu/news/mr-investments-first-place-2021-investment-competition/
- 2021-22 case: https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/
- 2022 finale: https://globalyouth.wharton.upenn.edu/news/top-teams-sail-to-success-in-the-2022-wharton-investment-competition-global-finale/
- 2023 finale: https://globalyouth.wharton.upenn.edu/news/the-2023-investment-competition-global-finale-ends-in-sweet-victory-for-dmvs-finest/
- 2024 finale: https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/
- 2024 finalists: https://globalyouth.wharton.upenn.edu/news/wharton-global-youth-hosts-five-virtual-events-to-announce-the-2024-investment-competition-finalists/
- 2025 finale: https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/
- 2025 top 10: https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/
- 2026 Top 50: https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
- 2026 champions: https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/

## 5. The research cards

Every card is in `keel/final_report/research/cards/`. A card with a Sources section (the fourth column gives its line)
lists its sources there, in APA 7, numbered S1, S2 or 1, 2, with the date each was read. The other cards cite each
source in the row that uses it, by author, title and link. The last column counts the entries
[REFERENCES_APA.md](REFERENCES_APA.md) already holds for the card, each read again at the source; its section 6
lists the card sources still unchecked. Where it says "none yet", the card itself is the record until the next
references run reads those sources again and merges them.

| Card | File | Question | Where its sources are | Entries in REFERENCES_APA.md |
|---|---|---|---|---|
| NUM | [NUM_extras_2026-11-09.md](cards/NUM_extras_2026-11-09.md) | Number cards from the engine, Mon 9 Nov 2026 (later run) | Keel's own model runs (inputs named in the rows, no links) | 10 |
| Q1 | [Q1_career_as_shares.md](cards/Q1_career_as_shares.md) | is Laura's career really like a stock, and what kind? | in the row that uses it (author, title, link) | 24 |
| Q1b | [Q1b_career_beta_horizon.md](cards/Q1b_career_beta_horizon.md) | does Laura's income fall with share prices over the horizon the plan cares about? | in the row that uses it (author, title, link) | 10 |
| Q1c | [Q1c_career_and_diversification.md](cards/Q1c_career_and_diversification.md) | Laura's career, the promised money and what "diversified" means in this plan | in the row that uses it (author, title, link) | none yet |
| Q2a | [Q2a_fixed_promises_what_broke.md](cards/Q2a_fixed_promises_what_broke.md) | how fixed promises are made certain, and what broke when they failed (pensions, LDI, insurers' annuities) | Sources section, l.296 | 37 |
| Q2b | [Q2b_escrows_lotteries_settlements_stress.md](cards/Q2b_escrows_lotteries_settlements_stress.md) | refunding escrows, lottery annuities and structured settlements under stress | Sources section, l.239 | 28 |
| Q2c | [Q2c_endowment_spending_rules.md](cards/Q2c_endowment_spending_rules.md) | endowment spending rules against a dedicated reserve | Sources section, l.252 | 22 |
| Q3a | [Q3a_floors_in_markets.md](cards/Q3a_floors_in_markets.md) | floors in markets, what made them real or false (portfolio insurance 1987, principal-protected notes 2008, target-date 2010 funds, iBond term funds) | Sources section, l.251 | 25 |
| Q3b | [Q3b_floors_in_institutions.md](cards/Q3b_floors_in_institutions.md) | Floors in institutions: why "safe" holdings broke at Orange County (1994), in the UK gilt crisis (2022) and at SVB (2023), and what stops Laura's plan breaking the same way | Sources section, l.193 | 10 |
| Q4b | [Q4b_cosponsors_in_downturns.md](cards/Q4b_cosponsors_in_downturns.md) | do co-sponsors cut their giving when share prices fall, by how much, and how late? | in the row that uses it (author, title, link) | 8 |
| Q4c | [Q4c_how_sure_words_and_numbers.md](cards/Q4c_how_sure_words_and_numbers.md) | how sure, in words and in numbers (the 2031 range and its confidence) | Sources section, l.341 | 20 |
| Q5 | [Q5_is_half_right.md](cards/Q5_is_half_right.md) | is keeping half of the shares the right amount of flexibility? | in the row that uses it (author, title, link) | 3 |
| Q5b | [Q5b_kept_share_numbers.md](cards/Q5b_kept_share_numbers.md) | keeping 30%, half or 70% of the shares, in numbers | Keel's own model runs (inputs named in the rows, no links) | none yet |
| Q5c | [Q5c_option_value_and_last_dollar.md](cards/Q5c_option_value_and_last_dollar.md) | is the value of waiting real, do lead donors keep money for the end, and where do owners hold the reserve? | Sources section, l.248 | none yet |
| Q5d | [Q5d_small_arts_buildings_overruns.md](cards/Q5d_small_arts_buildings_overruns.md) | what small arts and residency buildings overrun, and where a fifth to a quarter sits | Sources section, l.237 | none yet |
| Q5e | [Q5e_does_the_reserve_fall_with_its_uses.md](cards/Q5e_does_the_reserve_fall_with_its_uses.md) | does her flexibility fall when the claims on it rise? | Sources section, l.375 | none yet |
| Q6 | [Q6_how_far_to_trust_7_5.md](cards/Q6_how_far_to_trust_7_5.md) | how far can Caplet trust 7.5% for world shares? | in the row that uses it (author, title, link) | 9 |
| Q7 | [Q7_precommitment_and_rules.md](cards/Q7_precommitment_and_rules.md) | is buying the floor early, with only two reasons to change, a precommitment, and what is it worth? | in the row that uses it (author, title, link) | 14 |
| Q8a | [Q8a_certainty_in_engineering.md](cards/Q8a_certainty_in_engineering.md) | what "certain" means in engineering safety, and what Laura's report can borrow (3a, 3e) | Sources section, l.267 | 13 |
| Q8b | [Q8b_certainty_standards_1in200_ALARP.md](cards/Q8b_certainty_standards_1in200_ALARP.md) | "a high degree of certainty" against regulators' numbers (Solvency II 1-in-200, HSE's tolerability of risk and ALARP, rating agencies' default tables) | Sources section, l.276 | 17 |
| Q9 | [Q9_what_makes_a_residency_last.md](cards/Q9_what_makes_a_residency_last.md) | what makes an artist residency or small arts institution last? | in the row that uses it (author, title, link) | 5 |
| Q9b | [Q9b_residencies_reserves_and_founders.md](cards/Q9b_residencies_reserves_and_founders.md) | how residencies keep running money, pay for buildings, and outlive a founder | Sources section, l.285 | 20 |
| Q9c | [Q9c_taiwan_residencies_funding.md](cards/Q9c_taiwan_residencies_funding.md) | how Taiwan's residencies are funded, and how they opened, shrank and closed | Sources section, l.235 | 30 |
| Q10 | [Q10_inflation_inputs.md](cards/Q10_inflation_inputs.md) | inflation, Taiwan costs and the Taiwan dollar | Keel's own model runs (inputs named in the rows, no links) | 15 |
| Q10b | [Q10b_taiwan_dollar_2025_and_insurers.md](cards/Q10b_taiwan_dollar_2025_and_insurers.md) | how hard a test is a 10% stronger Taiwan dollar, what May 2025 shows, and why test that side | Sources section, l.310 | none yet |
| Q10c | [Q10c_taiwan_building_costs_and_codes.md](cards/Q10c_taiwan_building_costs_and_codes.md) | Taiwan building costs, seismic codes, and where a small residency's building risk sits | Sources section, l.370 | none yet |
| Q10d | [Q10d_moc_ncaf_residency_support.md](cards/Q10d_moc_ncaf_residency_support.md) | what Taiwan's public arts money gives a residency, when, and how it behaved in bad years | Sources section, l.285 | none yet |
| Q11a | [Q11a_funders_seed_assurance.md](cards/Q11a_funders_seed_assurance.md) | getting several funders to commit to one project (seed money, all-or-nothing pledges, ranges) | in the row that uses it (author, title, link) | 19 |
| Q11b | [Q11b_real_case_statements.md](cards/Q11b_real_case_statements.md) | what real fundraising texts for arts buildings and residencies look like | in the row that uses it (author, title, link) | 4 |
| Q11c | [Q11c_unequal_cosponsors_and_conditions.md](cards/Q11c_unequal_cosponsors_and_conditions.md) | unequal co-sponsors, the order of commitments, and conditional pledges | Sources section, l.306 | 18 |
| Q11d | [Q11d_taiwan_funders_primary.md](cards/Q11d_taiwan_funders_primary.md) | how Taiwan's arts funders actually pay, what they can promise, and how founders' building gifts were stated | Sources section, l.258 | 22 |
| Q12 | [Q12_lauras_working_life.md](cards/Q12_lauras_working_life.md) | Laura's working life, income by income, and the risk to the 2028 deposit | in the row that uses it (author, title, link) | none yet |
| Q12b | [Q12b_lauras_working_life_gaps.md](cards/Q12b_lauras_working_life_gaps.md) | Laura's working life, the gaps closed | in the row that uses it (author, title, link) | none yet |
| Q15 | [Q15_monitoring_and_triggers.md](cards/Q15_monitoring_and_triggers.md) | what should Laura watch as 2031 and 2033 approach, and what would make her act? | in the row that uses it (author, title, link) | 7 |
| Q16 | [Q16_operating_reserve_mechanics.md](cards/Q16_operating_reserve_mechanics.md) | how the operating reserve pays out (size, composition, how it changes) | in the row that uses it (author, title, link) | 6 |
| Q17 | [Q17_judging_the_implementation.md](cards/Q17_judging_the_implementation.md) | Judging the implementation (Final Report Section 2, Portfolio Implementation) | in the row that uses it (author, title, link) | 6 |
| Q18 | [Q18_pledges_and_stated_confidence.md](cards/Q18_pledges_and_stated_confidence.md) | how funders count, trust and act on a promised gift, and what a stated range and confidence do to trust | in the row that uses it (author, title, link) | 7 |
| Q19 | [Q19_range_rule_and_confidence.md](cards/Q19_range_rule_and_confidence.md) | the 2031 range as one rule, and its confidence | in the row that uses it (author, title, link) | 14 |
| Q20 | [Q20_pooled_book_or_margin.md](cards/Q20_pooled_book_or_margin.md) | A pooled book or Keel's margin for the ten payments (Final Report part 3a) | in the row that uses it (author, title, link) | 19 |
| Q21 | [Q21_team_reflection_events.md](cards/Q21_team_reflection_events.md) | which real events can the Team Reflection tell, what did each change, and what makes a reflection score 5? | Sources section, l.29 | 4 |
| Q22 | [Q22_cosponsor_words_checklist.md](cards/Q22_cosponsor_words_checklist.md) | what the 2031 words for co-sponsors must cover, in what order, at what length, and how to test them | in the row that uses it (author, title, link) | 43 |
| Q23 | [Q23_exhibits_and_format.md](cards/Q23_exhibits_and_format.md) | Wharton's page format measured, and the exhibits designed | in the row that uses it (author, title, link) | 8 |
| Q24 | [Q24_kept_half_and_joint_stress.md](cards/Q24_kept_half_and_joint_stress.md) | the kept half, the joint stress of rates and shares, and Exhibit 3's scenario matrix | Sources section, l.290 | 16 |
| Q25 | [Q25_what_returns_to_laura.md](cards/Q25_what_returns_to_laura.md) | what returns to Laura, and whether holding it back under-signals | Sources section, l.320 | 11 |
| Q26 | [Q26_monitoring_table.md](cards/Q26_monitoring_table.md) | what to monitor as 2031 and 2033 approach (Table 3) | Sources section, l.282 | 19 |
| Q27 | [Q27_reflection_rubric.md](cards/Q27_reflection_rubric.md) | what makes a team reflection score well, and how should the 16 Nov readers score events? | Sources section, l.282 | 12 |
| Q28 | [Q28_exhibits_prior_art.md](cards/Q28_exhibits_prior_art.md) | prior art for the three exhibits (how professionals show a matched bond book, a plan under several markets, and a holdings list) | Sources section, l.289 | 21 |
| Q29 | [Q29_section2_pilot_frame.md](cards/Q29_section2_pilot_frame.md) | One frame for Section 2 that judges the WInS book as a build, not a bet | Sources section, l.240 | none yet |
| Q30 | [Q30_table3_cut_and_xdate.md](cards/Q30_table3_cut_and_xdate.md) | cutting Table 3 from 33 rows to eight, and settling the next debt-limit X-date | Sources section, l.336 | none yet |
| Q31 | [Q31_escrow_standard_plain_words.md](cards/Q31_escrow_standard_plain_words.md) | how the payments' standard is said to a reader outside finance (3a) | Sources section, l.299 | none yet |
| Q32 | [Q32_meaningful_contribution.md](cards/Q32_meaningful_contribution.md) | why her facility contribution is "meaningful" | Sources section, l.287 | none yet |
| Q33 | [Q33_shares_of_free_money.md](cards/Q33_shares_of_free_money.md) | how many shares the money promised to no one should hold, and how to say why (2.3, 3b) | Sources section, l.261 | none yet |
| Q34 | [Q34_policy_and_implementation.md](cards/Q34_policy_and_implementation.md) | where policy ends and implementation begins, and how a decision made inside a frozen IPS is recorded | Sources section, l.263 | none yet |
| Q35 | [Q35_range_forecasts_credibility.md](cards/Q35_range_forecasts_credibility.md) | how readers judge a stated range, and what that means for the 2031 range (3c, 3d) | Sources section, l.293 | none yet |
| Q36 | [Q36_ibonds_fund_end_powers.md](cards/Q36_ibonds_fund_end_powers.md) | can an iBonds Treasury fund's end date move, and who decides? | Sources section, l.270 | none yet |
| Q37 | [Q37_stating_assumptions.md](cards/Q37_stating_assumptions.md) | stating the plan's assumptions and limits so a judge trusts them | Sources section, l.264 | none yet |
| Q38 | [Q38_holding_identifiers.md](cards/Q38_holding_identifiers.md) | a verified public identifier for every holding in Table 1 | Sources section, l.223 | none yet |
| Q39 | [Q39_strongest_critiques.md](cards/Q39_strongest_critiques.md) | the strongest published critiques of the plan's ideas, and the answer to each | its source table | none yet |
| Q40 | [Q40_pencil_and_ink_craft.md](cards/Q40_pencil_and_ink_craft.md) | the comics craft behind the conceit "pencil and ink": stages, pencils erased, ink corrections, bleed and safe area, finished issues before solicitation, non-returnable shop orders, advances in instalments, art drawn larger than printed, Laura's Climbing quote | "Quotes by item" sections, each with its link and date | the conceit (`../CONCEIT.md`) |
| Q41 | [Q41_conceit_audit.md](cards/Q41_conceit_audit.md) | an independent audit of the conceit: the AI mapping's errors against the register, errors in Keel's own notes, where the image misleads, twelve ranked parallels, placement and guards | Parts A-D, each citing file and line | the conceit (`../CONCEIT.md` 5b, 6, 7) |
| Q42 | [Q42_analogy_and_metaphor_evidence.md](cards/Q42_analogy_and_metaphor_evidence.md) | does a conceit carried through a report help its readers, and how should "pencil and ink" be used? (metaphor meta-analysis, framing experiments, analogy research, expertise reversal) | Sources section, l.302 | the conceit (`../CONCEIT.md` 6, 7, 10) |
| Q43 | [Q43_when_a_promise_counts.md](cards/Q43_when_a_promise_counts.md) | when do public budgets, accountants and builders count a promise as made? (OMB full funding, the Antideficiency Act, Taiwan's Budget Act, conservatism and prudence, university building-gift rules) | Sources section, l.363 | 3c, 3d; `../WORDS.md` bans |
| Q44 | [Q44_conceit_craft_open_items.md](cards/Q44_conceit_craft_open_items.md) | the conceit's open craft checks: process pages, Martin's printed sentence, correcting ink, erasing pencils, non-photo blue, Laura's tools | Sources table, l.163 | the conceit (`../CONCEIT.md` 5, 5b) |
| Q6b | [Q6b_forecast_panel_2027.md](cards/Q6b_forecast_panel_2027.md) | where J.P. Morgan's 7.5% sits among fifteen houses' 2026-27 forecasts, and how far forecasters' own five-year figures missed (Sun 15 Nov) | Sources (APA 7), l.210 | 3e area (1); NUMBERS 8p |
| Q6c | [Q6c_falls_and_the_top.md](cards/Q6c_falls_and_the_top.md) | what a 40% fall in world shares before or after the 2031 move does to the range, the contribution and her flexibility (Sun 15 Nov; engine `numbers/fall40.py`) | Sources (APA 7), l.287 | 3e area (1), Table 2; NUMBERS 8p |
| Q6d | [Q6d_one_world_fund.md](cards/Q6d_one_world_fund.md) | the case for one world share fund against home bias, crash-month and long-slump evidence, Taiwan's weight in VT (Sun 15 Nov) | Sources (APA 7), l.292 | 2.3, 3b |
| Q7b | [Q7b_rules_and_escape_clauses.md](cards/Q7b_rules_and_escape_clauses.md) | precommitment and escape clauses in central banking and fiscal rules, tested against IPS l.17's two reasons (Sun 15 Nov) | Sources (APA 7), l.199 | 3e, 3a, Table 3 |
| Q7c | [Q7c_endowment_rules.md](cards/Q7c_endowment_rules.md) | endowment spending rules and their exits (Yale, Stanford, Harvard, UPMIFA), capital projects in 2009, how foundations book pledges (Sun 15 Nov) | Sources (APA 7), l.147 | 3e, 3d, 3b |
| Q2d | [Q2d_cash_at_zero_and_below.md](cards/Q2d_cash_at_zero_and_below.md) | how often waiting cash has earned nothing, why US cash stops near zero, and what lies under it | Sources section, l.173 | none yet |
| Q3c | [Q3c_ended_ibond_funds_payouts.md](cards/Q3c_ended_ibond_funds_payouts.md) | what the five ended Treasury iBonds funds actually paid, and whether the 0.5% held back is the right size | Sources section, l.183 | none yet |
| Q10e | [Q10e_taiwan_two_risks_together.md](cards/Q10e_taiwan_two_risks_together.md) | Taiwan's two risks together: building costs and the Taiwan dollar against a US-dollar contribution | Sources section, l.204 | none yet |
| Q11e | [Q11e_founders_share_taiwan.md](cards/Q11e_founders_share_taiwan.md) | a founder's share in Taiwan: who pays first for a small arts place, how much the state matches, and how big Laura's range is in local terms | Sources section, l.203 | none yet |
| Q13 | [Q13_how_the_team_learned.md](cards/Q13_how_the_team_learned.md) | how the team learned (pre-mortems, decision journals, outcome bias, Tetlock, Kahneman and Lovallo) and how each of the three moments is told | Sources section, l.127 | none yet |
| Q14a | [Q14a_showing_work_graphics.md](cards/Q14a_showing_work_graphics.md) | how the report shows its work in exhibits: Cleveland and McGill, Tufte, icon arrays and natural frequencies, drawn boundaries, McCloud | Sources section, l.114 | none yet |
| Q14b | [Q14b_showing_work_plain_english.md](cards/Q14b_showing_work_plain_english.md) | how the report shows its work in words: the SEC Plain English Handbook with Buffett's preface, Berkshire's letters, SSA, the Bank of England, the IPCC, past teams | Sources section, l.114 | none yet |
| Q45 | [Q45_selling_in_a_stress.md](cards/Q45_selling_in_a_stress.md) | selling in a stress: what the plan's three trade moments and TNA l.15's "liquid" cost when markets seize | Sources section, l.155 | none yet |
| Q46 | [Q46_world_fund_case_and_moments.md](cards/Q46_world_fund_case_and_moments.md) | the strongest case for keeping one world fund, and the literature behind the three moments | Sources section, l.43 | none yet |
| Q47 | [Q47_conceit_intricate.md](cards/Q47_conceit_intricate.md) | the conceit made intricate (craft facts checked at source, parallels, arc) | Sources section, l.140 | none yet |
| Q48 | [Q48_taiwan_proof_of_committed_money.md](cards/Q48_taiwan_proof_of_committed_money.md) | what a Taiwanese funder asks a founder to prove about her own share of a building or residency, when, in what form, and what happens if it falls short (Mon 16 Nov) | Sources, l.125 | none yet |
| Q49 | [Q49_taiwan_capital_lines_and_budget_calendar.md](cards/Q49_taiwan_capital_lines_and_budget_calendar.md) | does Taiwan's public arts money pay for residency buildings, and on what dates each year does Laura first see, then know, next year's Taiwan arts money? (Mon 16 Nov) | Sources, l.111 | none yet |
| Q50 | [Q50_taiwan_sponsors_in_downturns.md](cards/Q50_taiwan_sponsors_in_downturns.md) | when Taiwan's economy turned (2008-09) and when the arts shut down (2020-21), what did Taiwanese companies, foundations and public bodies give, and do they make multi-year pledges? (Mon 16 Nov) | Sources, l.176 | none yet |
| Q51 | [Q51_small_arts_capital_shortfalls.md](cards/Q51_small_arts_capital_shortfalls.md) | how often, and by how much, do small arts building projects run short of money, and is Laura's flexibility big or small beside that? (Mon 16 Nov) | Sources, l.121 | none yet |
| Q52 | [Q52_feasibility_ranges_and_floors.md](cards/Q52_feasibility_ranges_and_floors.md) | what fundraisers tell a board before a campaign (one figure or a range, how wide, how sure), and what happened to gifts announced as "at least" with more to follow (Mon 16 Nov) | Sources, l.128 | none yet |
| Q53 | [Q53_notice_periods_for_money.md](cards/Q53_notice_periods_for_money.md) | how much warning do real money promises carry, and is one month enough for the 2028 deposit? (Mon 16 Nov) | Sources, l.111 | none yet |
| Q54 | [Q54_defeasance_escrow_rules.md](cards/Q54_defeasance_escrow_rules.md) | what do S&P, Moody's and Fitch require of a defeasance escrow before they rate it like the US government, and could such an escrow hold an iShares iBonds Treasury fund? (Mon 16 Nov) | Sources, l.127 | none yet |
| Q55 | [Q55_multiyear_operating_support.md](cards/Q55_multiyear_operating_support.md) | how are real multi-year operating promises written down and made reliable, and what should the residency see to rely on Laura's ten payments? (Mon 16 Nov) | Sources, l.125 | none yet |
| Q56 | [Q56_author_incomes_at_the_top.md](cards/Q56_author_incomes_at_the_top.md) | when recessions hit, what happens to the incomes of successful authors and speakers (the top tenth, not the typical author), how lumpy is that income, and how fast does it come back? (Mon 16 Nov) | Sources, l.111 | none yet |
| Q57 | [Q57_the_plans_academic_family.md](cards/Q57_the_plans_academic_family.md) | where does Caplet's plan sit in the investing literature, and which citations would a Wharton finance professor expect? (Mon 16 Nov) | Sources, l.149 | none yet |
| Q58 | [Q58_issue_only_against_what_is_owned.md](cards/Q58_issue_only_against_what_is_owned.md) | rules that let you promise only against what you already hold: what they covered, what broke, and what they say about Laura's rule (Mon 16 Nov) | Sources, l.182 | none yet |
| Q59 | [Q59_margins_that_hold.md](cards/Q59_margins_that_hold.md) | how do other fields size, state and guard a margin that must hold, and what does that say about Laura's extra Treasuries, her flexibility and the range rule? (Mon 16 Nov) | Sources, l.121 | none yet |
| Q60 | [Q60_reader_tests_for_a_headline.md](cards/Q60_reader_tests_for_a_headline.md) | how do the fields that test documents on real readers check that a reader got the point, how do they score it, how many readers do they need, and how would they test a dollar range with a confidence level? (Mon 16 Nov) | Sources, l.125 | none yet |
| Q62 | [Q62_sinking_funds_and_trust_funds.md](cards/Q62_sinking_funds_and_trust_funds.md) | history's reserves for fixed future sums: which held, which were raided or proved empty, and why (and is Laura's different?) (Mon 16 Nov) | Sources, l.150 | none yet |
| Q61 | [Q61_world_shares_four_to_six_years.md](cards/Q61_world_shares_four_to_six_years.md) | how often, and how badly, do world shares lose money over three to six years, and how rare is the 40% fall the report tests? (Mon 16 Nov) | Sources, l.169 | none yet |
| Q63 | [Q63_the_duty_to_diversify_and_its_exception.md](cards/Q63_the_duty_to_diversify_and_its_exception.md) | the law tells a fiduciary to diversify: what does it say to one who holds only US Treasuries for a fixed set of payments? (Mon 16 Nov) | Sources, l.172 | none yet |
| Q64 | [Q64_forward_rates_and_overlapping_windows.md](cards/Q64_forward_rates_and_overlapping_windows.md) | are forward rates fair forecasts, how much do 585 overlapping windows really tell us, and how do regulators size reinvestment risk? (Mon 16 Nov) | Sources, l.104 | none yet |
| Q65 | [Q65_how_fixed_promises_broke_recut.md](cards/Q65_how_fixed_promises_broke_recut.md) | how have high-grade fixed promises of money actually broken, and which of those failures does Laura's plan carry, in what size? (Mon 16 Nov) | Sources, l.153 | none yet |
| Q68 | [Q68_pension_hibernation_and_endgames.md](cards/Q68_pension_hibernation_and_endgames.md) | does Laura "start where pensions end"? Pension hibernation, endgames and the ten payments on day one (Mon 16 Nov) | Sources, l.105 | none yet |
| Q66 | [Q66_building_costs_when_world_shares_fall.md](cards/Q66_building_costs_when_world_shares_fall.md) | do building costs rise in the years world shares fall, so that her flexibility is smallest when a building costs more than planned? (Mon 16 Nov) | Sources, l.106 | none yet |
| Q67 | [Q67_founders_who_stated_a_floor.md](cards/Q67_founders_who_stated_a_floor.md) | have real founders and lead donors stated their own share as a range, or as "at least X, with more to follow", before others gave? How was it worded, what stood behind it, and how did it go? (Mon 16 Nov) | Sources, l.125 | none yet |
| Q69 | [Q69_converting_dollars_for_a_taiwan_building.md](cards/Q69_converting_dollars_for_a_taiwan_building.md) | converting US dollars for a Taiwan building: when and how do real institutions fix the rate, and who carries the move? (Mon 16 Nov) | Sources, l.163 | none yet |
| Q70 | [Q70_charitable_lead_annuity_trusts.md](cards/Q70_charitable_lead_annuity_trusts.md) | charitable lead annuity trusts: what the legal twin of Laura's ten payments knows about funding a fixed charitable annuity (a parallel, never tax or legal advice) (Mon 16 Nov) | Sources, l.121 | none yet |
| Q73 | [Q73_how_institutions_draw_a_matched_ladder.md](cards/Q73_how_institutions_draw_a_matched_ladder.md) | how do real institutions show, in one exhibit, that their assets pay their fixed future payments date by date, and what does that say about Figure 1 and Table 1? (Mon 16 Nov) | Sources, l.105 | none yet |
| Q74 | [Q74_what_confidence_means.md](cards/Q74_what_confidence_means.md) | what does "confidence" mean to statisticians, forecasters, regulators and finance, and which meaning should the report use for a range whose two ends Laura owns before she names them? (Mon 16 Nov) | Sources, l.100 | none yet |
| Q71 | [Q71_how_listeners_hear_a_range.md](cards/Q71_how_listeners_hear_a_range.md) | when Laura says "$95,000 to $115,000" in 2031, which end will co-sponsors hear as the promise, and what wording makes them hear it right? (Mon 16 Nov) | Sources, l.104 | none yet |
| Q72 | [Q72_what_owning_a_treasury_means.md](cards/Q72_what_owning_a_treasury_means.md) | what does Laura actually own when a broker holds her Treasury bonds, her iShares iBonds Treasury fund shares and VT, and is "owned" in the conceit's definition of ink true in law and in the plumbing? (Mon 16 Nov) | Sources, l.121 | none yet |
| Q76 | [Q76_rules_for_stating_future_figures.md](cards/Q76_rules_for_stating_future_figures.md) | what do the rules that govern how advisers and firms state future money figures say, and what do they teach the Final Report about how it states its own figures? (Mon 16 Nov) | Sources, l.91 | none yet |
| Q75 | [Q75_matching_funds_in_asia.md](cards/Q75_matching_funds_in_asia.md) | near Taiwan, when does a founder's private money unlock public or institutional money for an arts building or programme, what proof of it is asked for, and is it counted when pledged, received or spent? (Mon 16 Nov) | Sources, l.104 | none yet |
| Q81 | [Q81_waiting_cash_at_zero.md](cards/Q81_waiting_cash_at_zero.md) | waiting cash at zero: how often has it really happened, what did short Treasury funds pay, and is "safe at zero" a test against history or a stress beyond it? (Mon 16 Nov) | Sources, l.102 | none yet |
| Q79 | [Q79_new_conceit_parallels.md](cards/Q79_new_conceit_parallels.md) | in fields far from finance, where does a provisional figure become fixed only by a dated act of owning or holding it, not by signing or announcing it? (Mon 16 Nov) | Sources, l.130 | none yet |
| Q78 | [Q78_waiting_when_a_custodian_fails.md](cards/Q78_waiting_when_a_custodian_fails.md) | how long did investors wait, and what did they get back, when a broker, a fund, its sponsor or its custodian failed? (Mon 16 Nov) | Sources, l.160 | none yet |
| Q80 | [Q80_what_makes_a_reflection_convincing.md](cards/Q80_what_makes_a_reflection_convincing.md) | what makes a written reflection convincing to the people who assess it? (Mon 16 Nov) | Sources, l.205 | none yet |
| Q77 | [Q77_if_the_building_does_not_happen.md](cards/Q77_if_the_building_does_not_happen.md) | if the building does not happen: what becomes of money stated, pledged or given for a capital project that is cancelled, delayed or shrunk (Mon 16 Nov) | Sources, l.139 | none yet |
| Q82 | [Q82_contract_proofs_and_trade_customs.md](cards/Q82_contract_proofs_and_trade_customs.md) | do the printing trade's written standards and customs (contract proofs and their tolerances, over- and under-runs, the press check, "OK to print", stet) give true turns for the conceit, and where does each one break? (Mon 16 Nov) | Sources, l.104 | none yet |
| Q84 | [Q84_forecast_correction_rules_taiwan_japan.md](cards/Q84_forecast_correction_rules_taiwan_japan.md) | Taiwan and Japan make companies change their forecasts by rule: what do those rules really say, and does Laura's range need one? (Mon 16 Nov) | Sources, l.137 | none yet |
| Q86 | [Q86_responsible_giving_against_means.md](cards/Q86_responsible_giving_against_means.md) | is about $115,000 a responsible facility contribution by the yardsticks fundraisers and wealth advisers use to judge a gift against a donor's means: timid, generous or reckless, and is keeping her flexibility stingy? (Mon 16 Nov) | Sources, l.125 | none yet |
| Q87 | [Q87_price_of_certainty_against_buyouts.md](cards/Q87_price_of_certainty_against_buyouts.md) | is $1.11 for each $1 of payments a dear price for certainty, against what insurers charge to take a fixed promise? (Mon 16 Nov) | Sources, l.99 | none yet |
| Q89 | [Q89_series_promises_and_one_issuer.md](cards/Q89_series_promises_and_one_issuer.md) | ten promises that must all be paid: does holding them in one issuer make them safer, and what does the one shared risk cost? (Mon 16 Nov) | Sources, l.145 | none yet |
| Q90 | [Q90_pledges_counted_at_a_discount.md](cards/Q90_pledges_counted_at_a_discount.md) | how do charities count other people's pledges, do pledges fail more in downturns, and where would Laura's 2031 figure and a co-sponsor's conditional pledge sit in a residency's books? (Mon 16 Nov) | Sources, l.118 | none yet |
| Q93 | [Q93_why_no_bonds_mature_2031_to_2036.md](cards/Q93_why_no_bonds_mature_2031_to_2036.md) | why does no Treasury bond mature between February 2031 and February 2036, and is that a true 'aha' for Section 2.2? (Mon 16 Nov) | Sources, l.79 | none yet |
| Q85 | [Q85_building_costs_and_world_shares_verified.md](cards/Q85_building_costs_and_world_shares_verified.md) | do card Q66's counts and its January 2000 example survive a rebuild from the publishers' own tables? (Mon 16 Nov) | Sources, l.105 | none yet |
| Q94 | [Q94_guidance_heard_as_a_promise.md](cards/Q94_guidance_heard_as_a_promise.md) | guidance heard as a promise: when a central bank's conditional forecast was heard as a commitment, what did it cost, and what does that say about a figure Laura states in 2031? (Mon 16 Nov) | Sources, l.88 | none yet |
| Q83 | [Q83_seals_and_pledges_in_taiwan.md](cards/Q83_seals_and_pledges_in_taiwan.md) | what does a seal really do in Taiwan, and is a co-sponsor's sealed pledge ink or pencil? (Mon 16 Nov) | Sources, l.130 | none yet |
| Q91 | [Q91_dissent_and_team_decisions.md](cards/Q91_dissent_and_team_decisions.md) | does disagreement make a team's decision better, and how can the reflection judge its three disagreements instead of only telling them? (Mon 16 Nov) | Sources, l.193 | none yet |
| Q92 | [Q92_taiwan_political_calendar_2030_2033.md](cards/Q92_taiwan_political_calendar_2030_2033.md) | which Taiwanese elections and changes of government fall between the 2031 meetings and Laura's December 2032 payment, and what do they do to a public co-sponsor's pledge? (Mon 16 Nov) | Sources, l.101 | none yet |
| Q88 | [Q88_implementation_shortfall_for_the_book.md](cards/Q88_implementation_shortfall_for_the_book.md) | how would a professional measure how well the WInS portfolio was bought, and what can Section 2.5 honestly claim? (Mon 16 Nov) | Sources, l.144 | none yet |
| Q96 | [Q96_career_as_bond_stock_and_option.md](cards/Q96_career_as_bond_stock_and_option.md) | is a creative career one asset or three: a bond (the backlist), a stock (new advances) and an option (licences and screen deals)? (Tue 17 Nov) | Sources, l.105 | none yet |
| Q100 | [Q100_taiwan_artist_founded_museums.md](cards/Q100_taiwan_artist_founded_museums.md) | Taiwan's artist-founded and founder-funded art institutions: who paid to build them, who paid to run them, and what happened when that money stopped (Tue 17 Nov) | Sources, l.156 | none yet |
| Q101 | [Q101_artist_endowed_foundations.md](cards/Q101_artist_endowed_foundations.md) | when artists turn a career's earnings into a lasting institution, how do they pay for running it against its buildings, what reserves do they keep, and what happens when the money is mostly the artist's own works? (Tue 17 Nov) | Sources, l.118 | none yet |
| Q103 | [Q103_taiwan_price_adjustment_and_cci.md](cards/Q103_taiwan_price_adjustment_and_cci.md) | who carries a Taiwan building-cost burst once a building contract is signed, and what does October 2026's index say? (Tue 17 Nov) | Sources, l.119 | none yet |
| Q104 | [Q104_coupon_reinvestment_history.md](cards/Q104_coupon_reinvestment_history.md) | coupon reinvestment: how did the people who first matched dated payments with coupon bonds handle the interest on the coupons, and what did the market build when that was not enough? (Tue 17 Nov) | Sources, l.102 | none yet |
| Q107 | [Q107_aha_moments_and_memory.md](cards/Q107_aha_moments_and_memory.md) | what does cognitive science know about aha moments in a reader, and how should a written report set them so a judge remembers them? (Tue 17 Nov) | Sources, l.133 | none yet |
| Q108 | [Q108_graphic_novels_through_downturns.md](cards/Q108_graphic_novels_through_downturns.md) | how did graphic novels, the genre Laura works in, come through 2008-12 and 2023-25, and what did publishers cut first: lists, imprints or advances? (Tue 17 Nov) | Sources, l.93 | none yet |
| Q99 | [Q99_comfort_letters_and_pledges.md](cards/Q99_comfort_letters_and_pledges.md) | which words bind, and which words do funders count? Comfort letters, charitable pledges and Taiwan's letters of intent (Tue 17 Nov) | Sources, l.110 | none yet |
| Q105 | [Q105_fewer_numbers_better_understood.md](cards/Q105_fewer_numbers_better_understood.md) | how many figures can a passage carry for a lay reader, and where should the rest go? (Tue 17 Nov) | Sources, l.108 | none yet |
| Q97 | [Q97_sponsor_covenant_and_recovery_plans.md](cards/Q97_sponsor_covenant_and_recovery_plans.md) | when the person paying in can falter in the same downturn that hurts the fund: what pension regulators say about the "employer covenant" and recovery plans, and what it means for the 2028 deposit (Tue 17 Nov) | Sources, l.120 | none yet |
| Q95 | [Q95_authors_and_lumpy_advances.md](cards/Q95_authors_and_lumpy_advances.md) | how authors and graphic novelists are really paid, and what their advisers tell them to do with lumpy money (Tue 17 Nov) | Sources, l.145 | none yet |
| Q102 | [Q102_what_fifty_thousand_buys_in_taiwan.md](cards/Q102_what_fifty_thousand_buys_in_taiwan.md) | what will a fixed $50,000 a year (January 2033 to January 2042, "not adjusted for inflation", case l.90) buy in Taiwan, counted in people's time rather than in prices? (Tue 17 Nov) | Sources, l.102 | none yet |
| Q106 | [Q106_ink_in_the_ledger.md](cards/Q106_ink_in_the_ledger.md) | does bookkeeping have its own ink rule, and where does it match or break pencil and ink? (Tue 17 Nov) | Sources, l.247 | none yet |
| Q98 | [Q98_top_up_before_january_2027.md](cards/Q98_top_up_before_january_2027.md) | how far can Treasury yields move in the eight weeks before January 2027, and what would that do to the top-up, the extra Treasuries, the floor and VT? (Tue 17 Nov) | Sources, l.117 | none yet |
| Q109 | [Q109_reverse_stress_tests_for_3e.md](cards/Q109_reverse_stress_tests_for_3e.md) | how do the fields that must say what would break a promise say it, and does Laura's plan have exactly the few failure conditions it claims? (Tue 17 Nov evening) | Sources, l.113 | none yet |
| Q110 | [Q110_reservoir_firm_yield.md](cards/Q110_reservoir_firm_yield.md) | do water engineers size a reservoir the way the plan sizes the operating reserve? (Tue 17 Nov evening) | Sources, l.121 | none yet |
| Q111 | [Q111_aviation_fuel_categories.md](cards/Q111_aviation_fuel_categories.md) | does aviation's fuel planning divide a store of fuel the way the plan divides Laura's money? (Tue 17 Nov evening) | Sources, l.124 | none yet |
| Q112 | [Q112_taiwan_hui_and_others_money.md](cards/Q112_taiwan_hui_and_others_money.md) | what does Taiwan's own history of promises resting on other people's money (the hui, 合會 / 標會 / 會仔, and its collapses, 倒會) say about IPS l.11's "none of your 10 operating payments will depend on a share price, or on anybody else's money"? (Tue 17 Nov evening) | Sources, l.118 | none yet |
| Q113 | [Q113_taiwan_donor_lists_and_exact_sums.md](cards/Q113_taiwan_donor_lists_and_exact_sums.md) | when a Taiwanese community pays for a building, how are the gifts made public (exact sums by name, ranges or tiers), and what must the receiver disclose by law? (Tue 17 Nov evening) | Sources, l.180 | none yet |
| Q114 | [Q114_pencil_and_ink_in_law_and_archives.md](cards/Q114_pencil_and_ink_in_law_and_archives.md) | how do the law and the archive treat pencil and ink, and does that strengthen or strain the report's conceit? (Tue 17 Nov evening) | Sources, l.109 | none yet |
| Q115 | [Q115_one_day_move_or_averaging_out.md](cards/Q115_one_day_move_or_averaging_out.md) | is moving half the shares into Treasuries on one day better or worse than averaging out over a year? (Tue 17 Nov evening) | Sources, l.148 | none yet |
| Q116 | [Q116_owned_before_the_bid_olympic_guarantees.md](cards/Q116_owned_before_the_bid_olympic_guarantees.md) | what must an Olympic or World Expo host prove it owns or has guaranteed before it is chosen, and what happened when the guarantees rested on other people's money? (Tue 17 Nov evening) | Sources, l.102 | none yet |
| Q117 | [Q117_data_freshness_2026-11-17.md](cards/Q117_data_freshness_2026-11-17.md) | has any input the report relies on changed since the register read it? (Tue 17 Nov evening) | Sources, l.115 | none yet |
| Q118 | [Q118_illustrators_who_founded_places.md](cards/Q118_illustrators_who_founded_places.md) | how did picture-book and comics creators who founded places pay to run them, and did any set the running money aside before opening? (Tue 17 Nov evening) | Sources, l.157 | none yet |
| Q119 | [Q119_taiwan_promises_cut_and_floors.md](cards/Q119_taiwan_promises_cut_and_floors.md) | when Taiwan promised retirees a fixed rate or a floor paid from public money, what happened, and what does that tell a Taiwanese co-sponsor about promises that rest on someone else's money? (Tue 17 Nov evening) | Sources, l.130 | none yet |
| Q120 | [Q120_standards_of_proof_as_numbers.md](cards/Q120_standards_of_proof_as_numbers.md) | how high is "high"? What the professions that turn certainty words into numbers put on them, and what that says about "a high degree of certainty" (Tue 17 Nov evening) | Sources, l.105 | none yet |
| Q121 | [Q121_taiwanese_ink_and_type_craft.md](cards/Q121_taiwanese_ink_and_type_craft.md) | what does Taiwan's own craft of ink, seal and type offer the pencil-and-ink conceit, strikingly and truly? (Tue 17 Nov evening) | Sources, l.125 | none yet |
| Q122 | [Q122_material_adverse_change_and_the_two_reasons.md](cards/Q122_material_adverse_change_and_the_two_reasons.md) | do the IPS's two reasons work like a merger agreement's exit clause, and is "a fall in the market is not one of them" the standard exception? (Wed 18 Nov morning) | Sources, l.123 | none yet |
| Q123 | [Q123_fractional_kelly_and_the_half_kept.md](cards/Q123_fractional_kelly_and_the_half_kept.md) | is half what a careful bettor would keep? Fractional Kelly, doubt about the edge, and the half promised to no one (Wed 18 Nov morning) | Sources, l.110 | none yet |
| Q124 | [Q124_building_blocks_for_world_shares.md](cards/Q124_building_blocks_for_world_shares.md) | built from world shares' own numbers today (yield, inflation, growth, buybacks, valuation), what return do the building blocks give, and how does it compare with J.P. Morgan's 7.5%? (Wed 18 Nov morning) | Sources, l.112 | none yet |
| Q125 | [Q125_yield_triggers_that_never_fired.md](cards/Q125_yield_triggers_that_never_fired.md) | when UK pension schemes waited for higher gilt yields before hedging, how long did they wait, what did it cost, and does that make buying the ten on a date (January 2027) rather than at a price the disciplined choice? (Wed 18 Nov morning) | Sources, l.216 | none yet |
| Q126 | [Q126_prepaid_tuition_plans_and_fixed_promises.md](cards/Q126_prepaid_tuition_plans_and_fixed_promises.md) | when US states promised families future tuition and invested the money partly in shares, what broke in 2008-09, who paid, and which promises held? (Wed 18 Nov morning) | Sources, l.114 | none yet |
| Q127 | [Q127_the_advance_against_royalties.md](cards/Q127_the_advance_against_royalties.md) | in Laura's own trade, is a publisher's advance against royalties the same shape as her 2031 range, and what does the parallel teach? (Wed 18 Nov morning) | Sources, l.136 | none yet |
| Q128 | [Q128_certainty_words_in_chinese_for_taiwan.md](cards/Q128_certainty_words_in_chinese_for_taiwan.md) | when Laura's range and its confidence are heard in Mandarin in Taiwan, which English words keep their meaning, which change, and which Taiwanese words for "at least", "cap", "guarantee" and "promise" are fixed by law or practice? (Wed 18 Nov morning) | Sources, l.116 | none yet |
| Q129 | [Q129_founders_own_commitment_letters.md](cards/Q129_founders_own_commitment_letters.md) | how do founders write their own commitment, in their own voice, so that others believe it? (Wed 18 Nov morning) | Sources, l.133 | none yet |
| Q130 | [Q130_failure_first_in_three_sentences.md](cards/Q130_failure_first_in_three_sentences.md) | how do the fields that must explain a failure in a few sentences say it, do lay readers keep a risk better when the outcome comes first, and should 3e's limits follow the case's five areas or the ways a promise fails? (Wed 18 Nov morning) | Sources, l.101 | none yet |
| Q131 | [Q131_taiwan_materials_labour_and_the_nt_dollar.md](cards/Q131_taiwan_materials_labour_and_the_nt_dollar.md) | inside Taiwan's building-cost index: does a stronger Taiwan dollar make the materials cheaper, and do wages never fall? (Wed 18 Nov morning) | Sources, l.173 | none yet |
| Q132 | [Q132_gift_annuity_and_preneed_reserves.md](cards/Q132_gift_annuity_and_preneed_reserves.md) | when US law lets someone promise fixed future payments (a charity's gift annuity, a funeral paid in advance, a court's payment schedule), what reserve must stand behind the promise, and what does that say about Laura's operating reserve? (Wed 18 Nov morning) | Sources, l.121 | none yet |
| Q133 | [Q133_who_holds_and_releases_a_reserve.md](cards/Q133_who_holds_and_releases_a_reserve.md) | who holds a reserve, who releases each payment from it, and who signs the yearly report: what real set-asides do, and what Laura's plan already answers (Wed 18 Nov morning) | Sources, l.113 | none yet |
| Q134 | [Q134_can_a_creator_sell_her_career.md](cards/Q134_can_a_creator_sell_her_career.md) | can a creator sell her career? A devil's-advocate test of the word "can't" in "a giant stock she can't sell" (IPS l.3) (Wed 18 Nov morning) | Sources, l.103 | none yet |
| Q135 | [Q135_months_of_running_money_in_arts_groups.md](cards/Q135_months_of_running_money_in_arts_groups.md) | how many months of running money do arts groups really hold, what does the field ask for, and how does "ten years of the founder's own payments owned in advance" compare? (Wed 18 Nov morning) | Sources, l.117 | none yet |
| DIGEST | [DIGEST_2026-11-15.md](store/DIGEST_2026-11-15.md) | the first digest of the whole store: per tag the three strongest ideas and the biggest hole, mapped to SKELETON; worker files D1-D3 in `store/digest/` | cites store ids, which resolve in `store/insights.jsonl` | SKELETON (Sun 15 Nov block); the second research round |

## 6. Older research files and official documents cited by short name

| Label | File | What it is |
|---|---|---|
| R1 | [R1_wharton_archive.md](../../library/assistant_review_2026-10/oct16/research/R1_wharton_archive.md) | What Wharton's own website says about every season from 2021-22 to 2025-26 (16 Oct): clients, finalists, returning judges. "R1 section 4.4" is its section 4.4; its own links are inside it. |
| B7a | [B7a_competition_meta.md](../../library/insight_v1/phase_B/B7a_competition_meta.md) | Competition meta and judges: who reads, the odds, past semifinalists (27 Sep). "B7a section 3.2" quotes the abrdn release of 30 Jan 2023 (link in T14's list). |
| BRIEF | [keel/library/wharton_culture/BRIEF.md](../../library/wharton_culture/BRIEF.md) | Wharton's history, values and the 2023-2025 judge quotes (23 Oct), with its own links. |
| Guide p.N | [2026_WGY_Investment_Competition_Guide.pdf](../../../competition/official/2026_27/2026_WGY_Investment_Competition_Guide.pdf) (text copy alongside) | Wharton's 2026-27 Competition Guide, page N. |
| Final Report instructions | [2026_WGY_Final_Report_Instructions.pdf](../../../competition/official/2026_27/2026_WGY_Final_Report_Instructions.pdf) | Wharton's instructions, filed 9 Nov; verbatim in [WHARTON_NORTH_STAR.md](../WHARTON_NORTH_STAR.md) section 0. |
| WHARTON_WORD | [keel/WHARTON_WORD.md](../../WHARTON_WORD.md) | Everything in Wharton's documents that bears on the deliverables, verbatim. |
| Week N email | `competition/official/2026_27/wharton_email_weekN_*.md`, e.g. [week 6](../../../competition/official/2026_27/wharton_email_week6_2026-11.md) | Wharton's weekly emails to teams, filed as received. |

## 7. Harvest files, the insight store and the experience pool

The ten harvests in `harvest/` read Keel's older research into one format ([HARVEST_BRIEF.md](HARVEST_BRIEF.md)).
Each row's "Where found" column uses the codes below; the row's own sources are in its "Source(s)" column.

| Harvest | What it read | Its codes |
|---|---|---|
| H1 | [IDEA_BANK.md](../../ips_rewrite/IDEA_BANK.md) l.1-186 | "LOG #n" = entry n of the voice reading log [keel/voice/reading/LOG.md](../../voice/reading/LOG.md); "FRB-n" = item n of the Final Report bank inside IDEA_BANK.md |
| H2 | IDEA_BANK.md l.187-385 and [IDEA_LEDGER.md](../../ips_rewrite/IDEA_LEDGER.md) | "IB #n" = IDEA_BANK item n; "IL A1" = IDEA_LEDGER row A1; "TNA 1/2/3" = the three Trading Note reflections |
| H3 | [R02](../../ips_rewrite/research/R02_concepts_and_reading_list.md), [R05](../../ips_rewrite/research/R05_wide_reading.md), [R06](../../ips_rewrite/research/R06_overnight_dig.md) | "RL n" = item n of R02's Part 2 reading list |
| H4 | [R07_synergies/](../../ips_rewrite/research/R07_synergies/FUSIONS.md): scouts S1 to S3, FUSIONS, COVERED | "S1" to "S3" = the scout files; "C R02 n" = item n of R02 as listed in COVERED.md; "FUSIONS Tn" = test n |
| H5 | Scouts S4 to S6, rung1_haiku_wide.md, [R11_synergies.md](../../ips_rewrite/research/R11_synergies.md) | "RG1" = rung1_haiku_wide.md; "R11" = R11_synergies.md |
| H6 | [READING_SHILLER.md](../../ips_rewrite/final_night/READING_SHILLER.md), [READING_DAMODARAN.md](../../ips_rewrite/final_night/READING_DAMODARAN.md) | "Shiller L-N" = lecture N of Robert J. Shiller, *Financial Markets* (ECON 252), Yale, 2011: https://oyc.yale.edu/economics/econ-252-11/lecture-N; "Damodaran P1/P2 S-n" = page n of his NYU Stern Corporate Finance packets, Spring 2026: P1 https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket1spr26.pdf, P2 https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket2spr26.pdf |
| H7 | [keel/ips_rewrite/final_night/](../../ips_rewrite/final_night/FINAL_REPORT_BANK.md) reading files | RD = READING.md; RB = READING_BEYOND.md; FRB = FINAL_REPORT_BANK.md (rows B1-B22); ILV = IDEA_LIST_VERDICTS.md; ILM = IDEA_LIST_MATHS.md; SS = STRATEGY_SPINE.md; OTV = other_thread/IDEA_LIST_VERDICTS.md; L04a and W04b = other_thread/harvest/04a and 04b |
| H8 | [lab](../../rooms/lab.md), Window room, [models](../../models/README.md), [IDEAS.md](../../IDEAS.md) | L-01 to L-19 = lab experiments; W-01 to W-09 = Window experiments; I-01 to I-25 = ideas; S0 to S9 = model worlds |
| H9 | The Google Doc's Research tabs | T00 to T14 (section 4) |
| H10 | [meta/WHY_WHARTON.md](meta/WHY_WHARTON.md) and [meta/META_ANGLES.md](meta/META_ANGLES.md) | WW = WHY_WHARTON (section number); MA = META_ANGLES (angle number); W1 to W35 (section 3) |

- **The insight store.** [INSIGHT_STORE.md](INSIGHT_STORE.md) ranks every row from the harvests and cards. An id is the
  file's prefix and the row number: H9-042 is harvest H9 row 42, Q5c-003 is card Q5c row 3. Ratings are in
  [store/ratings.csv](store/ratings.csv); lists by topic in [store/by_tag/](store/by_tag/CERTAINTY.md).
- **The experience pool.** X-numbers are real events in [experience/BLIND_POOL.md](experience/BLIND_POOL.md), drawn
  from [EXPERIENCE_RECORD.md](EXPERIENCE_RECORD.md) and the three candidates files in `experience/`, where each
  event's evidence (commits, dates, files) is given.

## 8. Line references and Keel's own files

| Label | Means | File |
|---|---|---|
| case p.N, case l.N | The client case, PDF page N or line N of the text copy (also W1) | [Laura_Gao_2026_Client_Profile.txt](../../../competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt) |
| IPS l.N, FINAL l.N | Line N of the IPS Caplet submitted on 7 Nov | [FINAL_IPS_as_submitted.txt](../FINAL_IPS_as_submitted.txt) |
| TNA l.N | Line N of the Trading Notes Analysis as submitted | [tna_as_submitted.txt](../../drafts/writing_room_2026-11-03/tna_as_submitted.txt) |
| WN l.N | Line N of the WInS trade notes as copied on 13 Oct | [05_trading_note_reflection_wins_trading_notes.md](../../../caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md) |
| CANON A-E | Everything the submitted work commits Caplet to, quoted with its line | [CANON.md](../CANON.md) |
| CASE_MAP A-E | The case's requirements and Wharton's instructions, mapped to the report | [CASE_MAP.md](../CASE_MAP.md) |
| NUMBERS 8o | Section 8o of the number register, the only source of the report's figures | [NUMBERS.md](../NUMBERS.md) |
| WORDS | One plain name for each thing in the report | [WORDS.md](../WORDS.md) |
| 3a to 3e, exhibits | Parts of the report plan | [SKELETON.md](../SKELETON.md), [INTENT.md](../INTENT.md) |
| MODEL | A figure from Keel's own model, never a forecast | `keel/final_report/numbers/` (engine), results in [NUMBERS.md](../NUMBERS.md) |
| I-number (I101) | Caplet's instruction n to Keel | [keel/INSTRUCTIONS.md](../../INSTRUCTIONS.md) |
| Book n | Book n of Caplet's expectations ("the Bible") | [keel/EXPECTATIONS.md](../../EXPECTATIONS.md) (notes), [archive/bible_2026-11-08/BIBLE.md](../../../archive/bible_2026-11-08/BIBLE.md) (verbatim) |
| EXPECTATIONS Tn | Tension n between Caplet's instructions | [keel/EXPECTATIONS.md](../../EXPECTATIONS.md) l.758-779 |
| ASK_HUMANS | Keel's decisions, each with a reason and a default | [keel/pm/ASK_HUMANS.md](../../pm/ASK_HUMANS.md) |

## 9. Labels fixed on Sat 14 Nov

- [meta/WHY_WHARTON.md](meta/WHY_WHARTON.md): the header said "W1-W34"; it now says W1 to W35 with W15b and no W11,
  and points here. "T12" and "T14" were never defined in that file; each now names its tab.
- [meta/META_ANGLES.md](meta/META_ANGLES.md): "T05", "T07" and "T14" now name their tabs, and the header points here.
- [meta/HOW_STRATEGISTS_PLAN.md](meta/HOW_STRATEGISTS_PLAN.md): "T22" is now "EXPECTATIONS T22", so it cannot be read
  as a Google Doc tab.
