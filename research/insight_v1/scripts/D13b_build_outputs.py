"""D13b: build the verified table of all Phase B quotes whose speaker is NOT Laura Gao.

Inputs (status labels):
- research/insight_v1/phase_B/quotes_raw.json (Phase B claims; to be checked)
- research/insight_v1/phase_D/D13_mechanical_check.json (script re-fetch: VERBATIM / NOT_FOUND / NO_URL / FETCH_FAILED)
- research/insight_v1/phase_D/_work/D13b_contexts.json (made by D13b_other_quotes_context.py: context windows)
- The per-id judgements below (speaker, source type, final status, notes) were made by D13b on 2026-09-27 after
  reading each context window and re-trying all 21 non-VERBATIM quotes (re-fetch, Wharton WordPress REST API,
  legislation.gov.uk, Europe PMC, eCFR/Cornell LII, repo official files). They are judgements, not script output.
Outputs: research/insight_v1/phase_D/D13b_other_quotes_verified.json and the table section of the .md file
(written to research/insight_v1/phase_D/_work/D13b_table.md and pasted into the .md by hand).
Run from the repo root: .venv/bin/python research/insight_v1/scripts/D13b_build_outputs.py
"""
import json
import os
from collections import Counter

ACCESS = "2026-09-27"
WPAPI = "https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages?slug="
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22{}%22&resultType=core&format=json"

# Defaults by URL substring: (speaker/source, source_type)
BY_URL = [
    ("case-study-for-2021-2022", ("Wharton Global Youth, 2021-22 case study (client Nichole Jordan)", "official-Wharton (past season)")),
    ("case-study-for-2024-2025", ("Wharton Global Youth, 2024-25 case study (client Ladi Ayoola)", "official-Wharton (past season)")),
    ("11-teams-advance-to-the-2026", ("Wharton Global Youth news (Kara Dunn), 2026-03-20", "official-Wharton")),
    ("treasurydirect.gov", ("U.S. Treasury (TreasuryDirect)", "official-government")),
    ("ishares.com", ("BlackRock iShares product page (IBTR)", "industry (issuer primary)")),
    ("b9kh53xila9czkyznk1xv5yegl3snlc1", ("Wharton, 2026-27 Investment Competition Guide", "official-Wharton (2026-27)")),
    ("l2p0l26svbbptmcizhmswyq5f7rbyp44", ("Wharton, 2026-27 Competition Infographic", "official-Wharton (2026-27)")),
    ("a-winning-season-thousands-of-teams", ("Wharton Global Youth news, 2026-01-27", "official-Wharton")),
    ("bam-investing-from-deerfield", ("Wharton Global Youth news, 2025-05-01", "official-Wharton")),
    ("scribd.com", ("Wharton 2025-26 case study (client Connor Barwin)", "official-Wharton (past season)")),
    ("nonprofitaccountingbasics", ("Nonprofit Accounting Basics (industry guidance site)", "industry")),
    ("top-teams-sail-to-success", ("Wharton Global Youth news (Diana Drake), 2022-04-28", "official-Wharton")),
    ("spark-investments-bergen", ("Wharton Global Youth news, 2024-04-23", "official-Wharton")),
    ("five-virtual-events-to-announce-the-2024", ("Wharton Global Youth news (Diana Drake), 2024-03-25", "official-Wharton")),
    ("competitions/investment-competition/rules-roles", ("Wharton competition Rules & Roles page", "official-Wharton (2026-27)")),
    ("competitions/investment-competition/case-study", ("Wharton 2025-26 case study (hidden section of live page)", "official-Wharton (past season)")),
    ("competitions/investment-competition/", ("Wharton competition main page", "official-Wharton (2026-27)")),
    ("investment-competition/judging-and-evaluation", ("Wharton judging page (2023-24 version, retired)", "official-Wharton (past season)")),
    ("investment-competition/deliverables", ("Wharton deliverables page (2023-24 version, retired)", "official-Wharton (past season)")),
    ("inverse.com", ("Input/Inverse reporter (not Laura's words)", "secondary (news feature)")),
    ("inputmag.com", ("Input reporter (not Laura's words)", "secondary (news feature)")),
    ("whartons-pitch-to-amazon", ("Wharton Magazine writer (not Laura's words), 2017-10-30", "secondary (Wharton Magazine)")),
    ("83911-rights-report", ("Publishers Weekly Rights Report, July 2020", "secondary (trade press)")),
    ("news.vanderbilt.edu", ("Vanderbilt University news release, 2026-01-13", "official (institution press release)")),
    ("authorsguild.org", ("Authors Guild", "industry (trade association)")),
    ("europeanwriterscouncil", ("European Writers' Council summary of Society of Authors survey", "secondary (summary of industry survey)")),
    ("42783-aap-book-sales", ("Publishers Weekly (Jim Milliot), 2010-04-12", "secondary (trade press)")),
    ("icv2.com", ("ICv2 (Milton Griepp)", "industry (market research)")),
    ("ala.org", ("American Library Association press release, 2025-12-03", "industry (association press release)")),
    ("nber.org/papers/w3954", ("Bodie, Merton & Samuelson, NBER WP 3954 (1992) abstract", "research (working paper; later peer-reviewed JEDC 1992)")),
    ("publishersweekly.com/9780063067806", ("Publishers Weekly review of Kirby's Lessons", "secondary (trade review)")),
    ("theartnewspaper", ("The Art Newspaper (Benjamin Sutton), 2026-01-13", "secondary (news)")),
    ("thepensionsregulator", ("UK Pensions Regulator, DB funding code", "official-regulator")),
    ("apra.gov.au/standard", ("APRA Prudential Standard SPS 160", "official-regulator")),
    ("ministers.treasury.gov.au", ("Australian Treasurer media release", "official-government")),
    ("provost.yale.edu", ("Yale Office of the Provost", "official (institution)")),
    ("nabl.org", ("National Association of Bond Lawyers", "industry (professional association)")),
    ("am.jpmorgan.com", ("J.P. Morgan Asset Management, 'Rethinking the pension plan endgame' (Oct 2021)", "industry")),
    ("morningstar.com", ("Morningstar, Mind the Gap 2025", "industry")),
    ("eur-lex.europa.eu", ("EU Solvency II Directive 2009/138/EC, Art. 101(3)", "official-legislation")),
    ("nasra.org", ("NASRA issue brief", "industry (association)")),
    ("investment-policy-statement-individual-investors", ("CFA Institute, Elements of an IPS for Individual Investors (2010)", "industry (professional body)")),
    ("russellinvestments.com", ("Russell Investments (Justin Owens), 2026-07-13", "industry")),
    ("squarespace.com", ("Jean L.P. Brunel, CFA Institute Conference Proceedings Quarterly (Mar 2012)", "industry (professional proceedings)")),
    ("blogs.cfainstitute.org", ("Ashvin Chhabra, quoted on CFA Institute Enterprising Investor blog (2015)", "secondary (blog quoting practitioner)")),
    ("fca.org.uk", ("UK FSA/FCA Finalised Guidance FG11/05 (Mar 2011)", "official-regulator")),
    ("kitces.com", ("Kitces.com (Michael Kitces et al.)", "industry (practitioner blog)")),
    ("financial-analysts-journal", ("Fulkerson, Jordan, Riley & Yan, Financial Analysts Journal 82(3), 2026", "peer-reviewed")),
    ("apra.gov.au/sites", ("APRA/ASIC information report, July 2023", "official-regulator")),
    ("federalreserve.gov/newsevents", ("FOMC statement, 2026-09-16", "official-central bank")),
    ("federalreserve.gov/monetarypolicy", ("FOMC Summary of Economic Projections, 2026-09-16", "official-central bank")),
    ("advantage.factset.com", ("FactSet Earnings Insight", "industry (data provider)")),
    ("insight.factset.com", ("FactSet Insight article", "industry (data provider)")),
    ("msci.com", ("MSCI press release, March 2022", "industry (index provider primary)")),
    ("moodys.com", ("Moody's Ratings U.S. rating page", "industry (rating agency primary)")),
    ("taipeitimes", ("Taipei Times (Crystal Hsu), 2026-08-14", "secondary (news)")),
    ("focustaiwan.tw", ("CNA / Focus Taiwan", "secondary (news agency)")),
    ("budgetmodel.wharton", ("Penn Wharton Budget Model (Smetters & He), 2026-06-04", "research (university policy model, not peer-reviewed)")),
    ("ntu.org", ("National Taxpayers Union", "secondary (advocacy analysis)")),
    ("fortune.com", ("Fortune, 2026-06-27", "secondary (news)")),
    ("home.treasury.gov", ("U.S. Treasury Quarterly Refunding Statement, 2026-08-05", "official-government")),
    ("kresge.org", ("Kresge Foundation, A Guide to the Challenge Grant", "industry (funder guidance)")),
    ("w13728", ("Rondeau & List, NBER WP 13728 (2008)", "research (working paper; later peer-reviewed)")),
    ("pubeco/v95y2011", ("Huck & Rasul, J. Public Economics 95(5) 2011, abstract (RePEc)", "peer-reviewed")),
    ("nber.org/papers/w12338", ("Karlan & List, NBER WP 12338 abstract", "research (working paper; published AER 2007)")),
    ("feb/natura/00301", ("List & Lucking-Reiley, abstract on RePEc (JPE 2002)", "peer-reviewed (abstract)")),
    ("storage.fasb.org", ("FASB ASU 2018-08", "official-standard setter")),
    ("viewpoint.pwc.com", ("PwC Viewpoint NFP guide 7.3.2.2", "industry (accounting firm)")),
    ("matsucc.gov.tw", ("Lienchiang County Government notice of Taiwan Ministry of Culture subsidy call (2021)", "official-government (Taiwan)")),
    ("pkfod.com", ("PKF O'Connor Davies, due-diligence guide (July 2019)", "industry (accounting firm)")),
    ("nature.com", ("Budescu, Por, Broomell & Smithson, Nature Climate Change 4 (2014)", "peer-reviewed")),
    ("ipcc.ch", ("IPCC AR5 Guidance Note on uncertainties (2010)", "official (intergovernmental body)")),
    ("30%25%20chance", ("Gigerenzer et al., Risk Analysis 25 (2005), abstract via Europe PMC", "peer-reviewed")),
    ("boundary-effect", ("Teigen, Løhre & Hohle, Judgment and Decision Making 13(4)", "peer-reviewed")),
    ("pnas.org", ("van der Bles, van der Linden, Freeman & Spiegelhalter, PNAS 2020", "peer-reviewed")),
    ("jriskr", ("Jenkins, Harris & Lark, J. Risk Research 22(5) 2019", "peer-reviewed")),
    ("0956797617739369", ("Gaertig & Simmons (Wharton), Psychological Science 2018", "peer-reviewed")),
    ("09636625241228449", ("Dries, McDowell, Rebitschek & Leuker, Public Understanding of Science 2024", "peer-reviewed")),
    ("jobhdp", ("Du, Budescu, Shelly & Omer, OBHDP 114(2) 2011", "peer-reviewed")),
    ("sciencedaily", ("ScienceDaily reprint of Chicago Booth press release on Gneezy & Epley (2014)", "secondary (press release)")),
    ("sec.gov", ("SEC Marketing Rule 206(4)-1 (17 CFR 275.206(4)-1)", "official-regulator")),
    ("lets-go-announcing-the-top-10", ("Wharton Global Youth news (Diana Drake), 2025-03-24", "official-Wharton")),
    ("yahoo.com", ("KXAN Austin (Esmeralda Zamora) via Yahoo, 2026-03-22", "secondary (local news)")),
    ("tales-from-the-2023-teams", ("Wharton Global Youth news (Diana Drake), 2023-06-06", "official-Wharton")),
    ("upenn.box.com/s/l2p0", ("Wharton, 2026-27 Competition Infographic", "official-Wharton (2026-27)")),
    ("developing-strategy", ("Wharton 'Developing a Strategy' page (older-season text)", "official-Wharton (past season)")),
    ("prof-michael-roberts", ("Prof. Michael R. Roberts (competition Academic Director), interview by Diana Drake, 2022-05-31", "official-Wharton (interview)")),
    ("region-3-finalists", ("Wharton Global Youth news (Diana Drake), 2018-04-04", "official-Wharton")),
    ("aberdeenplc.com", ("abrdn press release (2023)", "industry (competition partner primary)")),
    ("teenink.com", ("Teen Ink: a 2023-24 team's published final report", "secondary (student work)")),
    ("essential-educator", ("Alex Lamon, teacher-advisor, Wharton Essential Educator blog, 2021-09-08", "official-Wharton blog (guest teacher, past season)")),
    ("lauragao.com/kirbys", ("Publisher copy on lauragao.com (not Laura's own voice)", "secondary (publisher copy)")),
    ("effectuation.org", ("Effectuation.org, Effectuation 101 (Sarasvathy framework)", "industry/academic outreach")),
    ("dospert.org", ("DOSPERT scale site (Weber, Blais & Betz)", "research (scale home page)")),
    ("w14848", ("Chen, Miao & Wang, NBER WP 14848 (2009)", "research (working paper; later peer-reviewed)")),
    ("investor.gov", ("SEC Investor.gov", "official-regulator")),
    ("vanguard.com", ("Vanguard, VCMM return forecasts (2026-07-22)", "industry")),
    ("Laura_Gao_2026_Client_Profile", ("Wharton 2026-27 case, p.1 sidebar pull quote (NO attribution line)", "official-Wharton (2026-27, repo file)")),
    ("Trading_Notes_Analysis", ("Wharton 2026-27 Trading Notes Analysis guide, sample note (p.2)", "official-Wharton (2026-27, repo file)")),
]

# Per-id judgements: status, corrected wording (None if none), notes, verified_url (where the wording was confirmed)
V = "VERIFIED-PRIMARY"
OVR = {
    "B1a-Q01": dict(notes="Boilerplate about the fictional firm WGAM; context not trimmed."),
    "B1b-Q05": dict(notes="Duplicate of B1a-Q03."),
    "B1b-Q06": dict(notes="Describes 2025-26 (announced Jan 2026) semifinal selection; B7b-Q05 and B7a-Q05 are duplicates."),
    "B1b-Q07": dict(notes="2025 finale article; the 'reimagining' foreshadows the new 2026-27 format."),
    "B1b-Q08": dict(verified_url=WPAPI + "case-study",
                    notes="Scribd copy blocked the check (NOT_FOUND). Upgraded: sentence read verbatim in the official 2025-26 case text via Wharton's WordPress REST API (hidden section of the live case-study page, modified 2026-05-07). The dash is an em dash in the source. Cite the Wharton page, not Scribd."),
    "B1b-Q09": dict(verified_url=WPAPI + "case-study",
                    notes="Upgraded from SNIPPET-UNVERIFIED: read verbatim in the 2025-26 case text via Wharton's REST API. The next sentence says teams 'need to embrace a longer-term investing mindset'; context not trimmed."),
    "B1b-Q10": dict(notes="Industry rule of thumb for nonprofit reserve ratios; not an official standard."),
    "B2a-Q02": dict(speaker="Wharton writer (Diana Drake) paraphrasing past client Nichole Jordan; only the word 'seen' is hers",
                    status_note="as Wharton's article text; PARAPHRASE-UNVERIFIED if quoted as Nichole Jordan's own words",
                    notes="PAST CLIENT FLAG: the sentence is the article's paraphrase, not a direct quote. Only \"seen\" sits inside quotation marks. Cite as 'Wharton reported that she had never felt more \"seen\"'."),
    "B2a-Q03": dict(speaker="Judge Andrea Vittorelli (Wharton alum; global chairman, J.P. Morgan Insurance Investment Group), 2022 Global Finale",
                    notes="JUDGE: confirmed as a direct quote. The page text runs on 'Cut slides, cut words, cut minutes...It's easier for the audience'. This was a FINALE judge commenting on presentations; semifinal relevance is by analogy only."),
    "B2a-Q04": dict(speaker="Wharton writer paraphrasing judge Eric Balchunas (senior ETF analyst, Bloomberg Intelligence), 2024 finale",
                    status_note="as Wharton's article text; PARAPHRASE-UNVERIFIED if quoted as Balchunas's own words",
                    notes="JUDGE FLAG: NOT the judge's own words. The article paraphrases him (no quotation marks) and spells him 'Balchunus' in that sentence. Never present this as 'Balchunas said'."),
    "B2a-Q05": dict(speaker="Judge Zoe McCormick (senior investment manager, North American fixed income, abrdn), 2024 finale",
                    notes="JUDGE: direct quote confirmed. The article goes on (in its own words) 'and consider their total financial picture'. Duplicate of B7a-Q13 (longer version)."),
    "B2a-Q06": dict(speaker="Past client Ladi Ayoola, 2025 Global Finale",
                    notes="PAST CLIENT: direct quote confirmed ('Ladi told the students'). Trimmed from 'Thank you for making the investment plans and proposals not just about the numbers, but about understanding and connecting with people.' Meaning is kept."),
    "B2a-Q07": dict(speaker="Judge Chirag Jain (U.S. credit research analyst, Aberdeen Standard Investments), 2025 Global Finale",
                    notes="JUDGE: direct quote confirmed; he is describing client pitches he saw at Vanguard, then 'I think you guys demonstrated that today.'"),
    "B2a-Q08": dict(speaker="Past client Connor Barwin (2025-26), pull quote with attribution",
                    notes="PAST CLIENT: confirmed with an explicit '- Connor Barwin' attribution line. Prior cases put a name under the pull quote; this year's case does not (see B2a-Q13)."),
    "B2a-Q09": dict(speaker="Semifinal judge Joshua Tam (portfolio manager, Laurel Avenue Management), 2024",
                    notes="JUDGE: confirmed. Page date 2024-03-25. He is a SEMIFINAL judge, so this is the most relevant judge quote for our round."),
    "B2a-Q11": dict(notes="Biography of the Academic Director, Prof. Michael Roberts."),
    "B2a-Q13": dict(notes="ATTRIBUTION FLAG: the sentence is verbatim in the case (repo txt lines 31-33, in the 'MEET LAURA GAO' sidebar), but the PDF has NO attribution line. Earlier cases attributed their pull quotes ('- Nichole Jordan', '- Connor Barwin'). An exact-phrase WebSearch (2026-09-27) found only generic self-help pages, and greps of 5 Laura interview pages found nothing. Cite as 'the case profile highlights...', never as 'Laura says'. D13a owns the Laura attribution question.",
                    status_note="Wording VERIFIED-REPO-FILE; attribution to Laura PARAPHRASE-UNVERIFIED"),
    "B2b-Q01": dict(verified_url=WPAPI + "case-study",
                    notes="Rendered page does not show it (NOT_FOUND). Re-read verbatim via the WordPress REST API (page id 16651, modified 2026-05-07). Past-season text sitting on a live page."),
    "B2b-Q02": dict(speaker="Past client Connor Barwin, pull quote in the 2025-26 case",
                    verified_url=WPAPI + "case-study",
                    notes="PAST CLIENT: verbatim via the REST API. The pull quote sits in the case-study body; there is no name line inside the snippet, but the page is his case and B2a-Q08 shows Wharton attributes his pull quotes."),
    "B2b-Q03": dict(verified_url=WPAPI + "judging-and-evaluation",
                    notes="Verbatim via the REST API (page id 3778, modified 2024-06-03). The same retired page's 'Investment strategy' line reads 'portfolio is invested in at least as many sectors as there are team members' - the official source of the old sector rule. That rule is NOT in the 2026-27 rules (R-W, G1-G4)."),
    "B2b-Q04": dict(verified_url=WPAPI + "judging-and-evaluation",
                    notes="Verbatim via the REST API, under 'A Few Things to Keep in Mind' (retired 2023-24 page)."),
    "B2b-Q05": dict(verified_url=WPAPI + "deliverables",
                    corrected="Final Report Audience [heading] / Your report should be directed to Wharton Global Asset Management’s (WGAM) portfolio manager (your team’s teacher/advisor).",
                    notes="Verbatim via the REST API (page id 3768, 2023-24, due Dec 11, 2023). 'Final Report Audience' is a bold heading; Phase B joined it to the sentence with a colon. The sentence itself is exact."),
    "B2b-Q06": dict(notes="REPORTER'S words, not Laura's (context marked this correctly). The surrounding paragraph holds personal-life material; do not reuse it (privacy rule)."),
    "B2b-Q09": dict(notes="Wharton Magazine writer's words about Laura, not a quote from her."),
    "B2b-Q11": dict(notes="Duplicate of B2a-Q13 (see the attribution flag there).",
                    status_note="Wording VERIFIED-REPO-FILE; attribution to Laura PARAPHRASE-UNVERIFIED"),
    "B3a-Q01": dict(notes="Trade-press deal report (PW Rights Report, week of July 20, 2020). B3b-Q01 is a duplicate."),
    "B3a-Q05": dict(notes="Institution's own release; confirms the CCA wind-down in 2027 (the team doc's 'acquisition' lead is now confirmed only in this form: campus acquisition after the wind-down, subject to requirements)."),
    "B3a-Q08": dict(notes="Secondary: the EWC summary of the UK Society of Authors survey (9 May 2024); the SoA report itself was not read."),
    "B3b-Q07": dict(notes="ICv2 release 2024-07-15."),
    "B3b-Q08": dict(notes="NBER abstract (Jan 1992); the paper was published in J. Economic Dynamics and Control 1992 (not re-checked here)."),
    "B3b-Q12": dict(notes="PW review of a novel's plot (fiction); not about Laura herself."),
    "B3b-Q14": dict(notes="Secondary news; agrees with the Vanderbilt release (B3a-Q05)."),
    "B4a-Q04": dict(notes="Australian Treasurer's release; page shows 'won't' and '2032–33'."),
    "B4a-Q09": dict(verified_url="https://www.legislation.gov.uk/eudr/2009/138/article/101",
                    notes="EUR-Lex returned HTTP 202 with an empty body (bot challenge), so the mechanical check read nothing. Verified verbatim on legislation.gov.uk (Directive 2009/138/EC, Article 101(3), the EU text as retained by the UK). The source text writes '99,5 %' (comma decimal)."),
    "B4b-Q03": dict(notes="The PDF text layer splits the word 'differ - ent' across a line; the sentence is otherwise verbatim (section 4b). The mechanical NOT_FOUND was caused by hyphenation only."),
    "B4b-Q04": dict(notes="Author confirmed on page: Justin Owens, CFA, FSA, EA, dated 2026-07-13. B10a-Q04 is a duplicate."),
    "B4b-Q07": dict(speaker="Ashvin Chhabra, quoted on CFA Institute Enterprising Investor blog",
                    notes="Direct quote with 'Chhabra says'; the next sentence is 'The goals you aspire to may require a somewhat higher level of risk.'"),
    "B4b-Q10": dict(notes="Authors confirmed on page. It rebuts Morningstar's 'Mind the Gap' (B4a-Q08); use the two together."),
    "B5a-Q02": dict(notes="Page date is June 4, 2026 (the URL slug says 06-02). A model projection, not a forecast by an official body."),
    "B5a-Q06": dict(notes="Secondary news report of the S&P action; S&P's own release was not read."),
    "B5b-Q06": dict(notes="Secondary report of the MSCI review; MSCI's own statement was not read."),
    "B5b-Q07": dict(notes="Secondary summary of the July 2026 U.S. Treasury FX report."),
    "B5b-Q09": dict(corrected="We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin preparing for Laura’s future operating commitment.",
                    notes="Repo file line 36 (and 37). The Phase B text stops mid-sentence at 'and begin'. Use the full sentence (= B10b-Q04)."),
    "B6a-Q05": dict(notes="The double space in 'gift  is' is in the PDF text layer."),
    "B6a-Q09": dict(notes="Abstract on RePEc (the Brief #17 seed-money finding); full text still blocked."),
    "B6a-Q13": dict(notes="Taiwan county government repost of the Ministry of Culture subsidy call (ROC year 111 = 2022 programme; applications Nov 2021). Chinese original; translate with care."),
    "B6b-Q02": dict(notes="The PDF text layer breaks '90- 95%' across a line, which caused the NOT_FOUND. The wording is verbatim in the IPCC note; the paragraph number was not re-checked."),
    "B6b-Q04": dict(notes="Abstract read via the Europe PMC API (Gigerenzer, Hertwig, van den Broek, Fasolo, Katsikopoulos 2005)."),
    "B6b-Q06": dict(verified_url=EPMC.format("10.1073/pnas.1913678117"),
                    notes="pnas.org returned 403; verified verbatim in the abstract via the Europe PMC API."),
    "B6b-Q08": dict(verified_url=EPMC.format("10.1177/0956797617739369"),
                    notes="doi.org/SAGE returned 403; verified verbatim in the abstract via Europe PMC (article title 'Do People Inherently Dislike Uncertain Advice?'; authors' affiliation: The Wharton School)."),
    "B6b-Q09": dict(verified_url=EPMC.format("10.1177/09636625241228449"),
                    notes="SAGE returned 403; verified verbatim via Europe PMC ('When evidence changes: Communicating uncertainty protects against a loss of trust', 2024)."),
    "B6b-Q11": dict(notes="Press-release summary; the paper (Gneezy & Epley 2014) was not read (SSRN blocked). Cite as the press release's summary."),
    "B6b-Q18": dict(verified_url="https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-17?part=275&section=275.206(4)-1",
                    notes="sec.gov still returns 403. Upgraded from SNIPPET-UNVERIFIED: the phrase is verbatim in the rule text on eCFR (and Cornell LII): hypothetical performance may be advertised only if the adviser 'Provides sufficient information to enable the intended audience to understand the criteria used and assumptions made in calculating such hypothetical performance'. Short fragment; keep that surrounding clause when citing."),
    "B7a-Q04": dict(verified_url="https://upenn.box.com/shared/static/l2p0l26svbbptmcizhmswyq5f7rbyp44.pdf",
                    notes="The /s/ Box link is a JavaScript viewer (no text), hence NOT_FOUND. Verbatim in the direct PDF link and in the repo file competition/official/2026_27/2026_WGY_Competition_Infographic.txt lines 40-41."),
    "B7a-Q06": dict(speaker="Semifinal judge Melissa Ko Hahn (Wharton MBA; managing member, Covepoint Capital Advisors), 2025",
                    notes="JUDGE: confirmed, 'who served as a judge for the semifinals' (page 2025-03-24). A SEMIFINAL judge talking about written reports."),
    "B7a-Q07": dict(speaker="Brian Z, co-team leader, DMV's Finest (2022-23 champions), Thomas Jefferson HS",
                    notes="Past competitor (not a client or judge); first name + initial as published by Wharton."),
    "B7a-Q08": dict(notes="Older-season page (mentions 'an approved stock list', which 2026-27 does not have); the principle still holds, the rules detail does not."),
    "B7a-Q09": dict(speaker="Prof. Michael R. Roberts (now the competition's Academic Director), interview 2022-05-31",
                    notes="His own words in a Wharton interview about teaching finance, not about judging this competition."),
    "B7a-Q10": dict(speaker="Wharton writer about Brianna Leporace (Aberdeen), 2018",
                    notes="Writer's words (not a quote); 2018 Region 3 format, long retired."),
    "B7a-Q11": dict(notes="abrdn's own release: 'more than 1,400' proposals, 55 selected (2023 season)."),
    "B7a-Q12": dict(speaker="Judge Vikas Keswani (HPS Investment Partners), 2024 Global Finale",
                    notes="JUDGE: direct quote confirmed; he is talking about analysis in finale PRESENTATIONS ('[your presentations]')."),
    "B7a-Q13": dict(speaker="Judge Zoe McCormick (abrdn), 2024 Global Finale", notes="JUDGE: confirmed; longer version of B2a-Q05."),
    "B7a-Q14": dict(notes="A published report by a team NOT in that year's Top 50; use only as an example of what to avoid (returns as proof)."),
    "B7a-Q15": dict(notes="Confirms that 2025-26 had mid-term reports."),
    "B7a-Q16": dict(speaker="Alex Lamon, teacher-advisor (guest blog), 2021-09-08",
                    notes="Old-season advice, confirmed verbatim. Together with the 2023-24 judging page (see B2b-Q03 note) it explains where the 'sector minimum = team size' claim came from. It is NOT a 2026-27 rule."),
    "B7b-Q05": dict(notes="Duplicate of B1b-Q06; the context says '2026 Top 50' (= the 2025-26 season). Both labels are fine."),
    "B7b-Q06": dict(speaker="Semifinal judge Melissa Ko Hahn, 2025", notes="JUDGE: confirmed (same passage as B7a-Q06)."),
    "B7b-Q07": dict(notes="Reporter's words, not a judge's. CORRECTION to the context: the article says the Vandegrift team were Global FINALISTS ('headed to the global finals'), not only semifinalists. The article goes on: 'a number the students initially questioned until realizing that professionals rarely achieve higher odds without taking on substantial risk.' This is not evidence of what judges reward."),
    "B7b-Q09": dict(speaker="Brian Z, co-team leader, DMV's Finest (2022-23 champions)", notes="Past competitor; confirmed."),
    "B8a-Q16": dict(notes="Duplicate of B2b-Q06 (reporter's words). Privacy: do not reuse the surrounding personal material."),
    "B8a-Q39": dict(notes="Duplicate of B2a-Q13 (see the attribution flag there).",
                    status_note="Wording VERIFIED-REPO-FILE; attribution to Laura PARAPHRASE-UNVERIFIED"),
    "B8b-Q01": dict(notes="Duplicate of B2a-Q13 (see the attribution flag there).",
                    status_note="Wording VERIFIED-REPO-FILE; attribution to Laura PARAPHRASE-UNVERIFIED"),
    "B8b-Q27": dict(notes="Reporter's words (older Input URL of the same feature as B2b-Q06)."),
    "B8b-Q28": dict(notes="Reporter's words; the book came out in 2025, not 2024."),
    "B8b-Q29": dict(notes="Trade press; the first book was actually published 2022-03-08 (per context)."),
    "B9b-Q15": dict(notes="Publisher copy about a fictional character, hosted on her site; not Laura's voice (the context marked this correctly)."),
    "B10a-Q03": dict(notes="Duplicate of B2b-Q06 (reporter's words)."),
    "B10b-Q04": dict(notes="Repo official file lines 36-37; full sentence verified."),
}


def lookup(url):
    for key, val in BY_URL:
        if key in url:
            return val
    return ("UNMAPPED", "UNMAPPED")


def main():
    quotes = {q["id"]: q for q in json.load(open("research/insight_v1/phase_B/quotes_raw.json"))}
    ctx = json.load(open("research/insight_v1/phase_D/_work/D13b_contexts.json"))
    rows = []
    for qid, c in ctx.items():
        q = quotes[qid]
        speaker, stype = lookup(q["url"])
        o = OVR.get(qid, {})
        mech = c["mechanical"]
        status = o.get("status", V)
        verified_url = o.get("verified_url", q["url"] if q["url"].startswith("http") else q["url"] + " (repo)")
        rows.append({
            "id": qid, "agent": q["agent"], "exact_text": q["exact_text"],
            "speaker_source": o.get("speaker", speaker), "source_type": stype,
            "url_given": q["url"], "url_verified": verified_url, "access_date": ACCESS,
            "mechanical_result": mech, "claimed_status": q["fetch_status"],
            "final_status": status, "status_note": o.get("status_note", ""),
            "corrected_wording": o.get("corrected"),
            "flag": ("PAST-CLIENT" if "Past client" in o.get("speaker", "") or "past client" in o.get("speaker", "") else
                     "JUDGE" if "udge" in o.get("speaker", "") else
                     "ATTRIBUTION" if "status_note" in o else ""),
            "notes": o.get("notes", ""),
        })
    os.makedirs("research/insight_v1/phase_D/_work", exist_ok=True)
    counts = Counter(r["final_status"] for r in rows)
    summary = {
        "scope": "All Phase B quotes whose speaker is NOT Laura Gao (reporters, publishers and the case's unattributed pull quote included)",
        "n_in_scope": len(rows), "n_laura_excluded": len(quotes) - len(rows),
        "final_status_counts": dict(counts),
        "mechanical_counts_in_scope": dict(Counter(r["mechanical_result"] for r in rows)),
        "upgraded_from_non_verbatim": [r["id"] for r in rows if r["mechanical_result"] != "VERBATIM"],
        "with_corrected_wording": [r["id"] for r in rows if r["corrected_wording"]],
        "unmapped": [r["id"] for r in rows if r["speaker_source"] == "UNMAPPED"],
        "access_date": ACCESS,
    }
    json.dump({"summary": summary, "quotes": rows},
              open("research/insight_v1/phase_D/D13b_other_quotes_verified.json", "w"), indent=1, ensure_ascii=False)
    # Markdown table
    def esc(s):
        return (s or "").replace("|", "/").replace("\n", " ")
    lines = ["| id | exact text | speaker / source | source type | URL (where verified) | status | corrected wording | notes |",
             "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        st = r["final_status"] + (f" ({r['status_note']})" if r["status_note"] else "")
        mech = "" if r["mechanical_result"] == "VERBATIM" else f"[mechanical: {r['mechanical_result']}] "
        lines.append(f"| {r['id']} | {esc(r['exact_text'])} | {esc(r['speaker_source'])} | {esc(r['source_type'])} | "
                     f"{esc(r['url_verified'])} | {st} | {esc(r['corrected_wording']) or '-'} | {mech}{esc(r['notes']) or 'Verbatim; context checked.'} |")
    open("research/insight_v1/phase_D/_work/D13b_table.md", "w").write("\n".join(lines) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
