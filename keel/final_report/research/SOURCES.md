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
