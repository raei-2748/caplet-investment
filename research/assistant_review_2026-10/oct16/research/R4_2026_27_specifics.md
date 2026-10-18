# R4: 2026-27 official and public specifics (checked Fri 16 Oct 2026, Sydney)

Scope: everything official and public about this year's competition and its client that is not already in the repo,
plus every change since 14 Oct. All live pages were fetched on 16 Oct 2026 between 01:50 and 02:10 UTC (12:50-13:10
Sydney) with plain curl. Saved copies: `scratchpad/oct16/research/R4_pages/` (one `.txt` per page, header shows URL and
fetch time). Every page comparison is in `R4_pages/DIFFS.txt`.

Labels: VERIFIED = I read it on the source today (or in a repo file, cited by file:line). UNVERIFIED = I could not
confirm it. INTERPRETATION = my reading, not a fact. Nothing here is deliverable text. It is knowledge for the team.

---

## 0. The ten things that matter most

1. **No official page has changed since the 15 Oct brief was checked (14 Oct, 20:20-20:38 UTC).** All seven public
   SMApply pages, the Wharton main page, Rules & Roles, FAQ and AI-policy pages read word for word the same today. All
   six official PDFs on Box are byte-identical to the repo copies (same SHA-256). (DIFFS.txt sections B and D.)
2. **Against the repo snapshot (`smapply_public_2026-10-14/`) two SMApply pages differ.** These are the same two edits
   the 15 Oct brief found. The FAQ now limits investments "for BOTH contributions, the IPS and Final Report" and drops
   the $5 stock-price wording. Trading Details now says "Your team may invest in (for BOTH contributions):". Saved
   copies pin the edit to 14 Oct between 15:33 and 20:34 UTC, after the snapshot. The repo snapshot is out of date and
   the repo has no saved copy of the new wording. (Section 1.1.)
3. **The Wharton AI-policy page did change on 14 Oct, but not for us.** WordPress records an edit at 13:48:39 UTC on
   14 Oct. A copy saved at 13:22 UTC that day shows the only change: Wharton deleted the "Comment & Win" paragraph
   (that is a different competition). The Investment Competition AI text is unchanged. (Section 1.3.)
4. **Laura is a real person. COMPETITION.md:49 is wrong.** It says "Laura is a fictional client." Wharton's main page
   says: "While the client is real, the financial scenario is developed specifically for the competition." So her
   biography is real, but her money, the residency and the dates are made up for the case. (Section 3.)
5. **The Rules page names only the IPS and Final Report for Top 50 selection.** "The top 50 teams will be selected as
   semifinalists based on the strength of their Investment Policy Statement (IPS) and Final Reports." The SMApply page
   says the TNA is also evaluated, and the case says the three deliverables are read together. Treat the TNA as
   scored. Treat the IPS and Final Report as carrying the cut. (Section 5.1.)
6. **No official 2026-27 video, webinar, podcast or article about Laura or the case exists in public.** The last
   Wharton news post is dated 30 Apr 2026. The WhartonHS YouTube channel has no Laura video. If Wharton sends a
   client video, it will be inside SMApply or WInS (weekly emails are copied to WInS). (Section 2.)
7. **Last year's semifinal was a recorded 10-minute video pitch addressed to the client, plus four written answers
   of 250 words or fewer.** Any "completely new material" meant disqualification. The pitch had to include a case
   study of one stock or ETF and every member had to speak. This year's FAQ instead says "a short presentation ... to a
   live panel of judges". The 2027 format is UNVERIFIED. Either way, the Final Report must already hold everything a
   pitch would need. (Section 5.3.)
8. **Last year's Top 50 were picked "with the help of our Wharton School student evaluators, as well as a
   professional review panel of asset managers from Aberdeen Investments".** The first readers may be students, not
   only professionals. Plain English and a clear structure help with both. Who reads this year is UNVERIFIED.
   (Section 5.2.)
9. **The case biography matches public facts, with one pattern: the case keeps the business side and leaves out the
   community side.** The "small business" at Wharton was a laptop-decal shop (Draw Street Journal, 2016). The case does
   not mention that she co-organises a free comics festival that gives out mini grants. Her college teaching job ends
   when California College of the Arts closes in 2027. (Section 3.)
10. **The full AI policy is in section 4, word for word.** The strictest line: "If you use AI to assist you in any way
    during the competition, how you use it must be recorded in your Works Cited pages."

---

## 1. Official pages: what changed, with exact text

### 1.1 SMApply public pages vs the repo snapshot

Base URL: `https://wghsinvcomp.smapply.us/res/p/{slug}/` (COMPETITION.md:211). Slugs: home (redirects to the site root),
guide, client, deliverables, trading, wins, faqs. Snapshot compared: `competition/official/2026_27/smapply_public_2026-10-14/`
(committed 14 Oct 2026, 21:16 AEDT).

| Page | Repo snapshot (exact) | Live 16 Oct (exact) | Status |
|---|---|---|---|
| FAQs, "DOES THE COMPETITION ALLOW ALL SECURITIES?" | "Investments permitted (for BOTH contributions):" (faqs.txt:42) | "Investments permitted (for BOTH contributions, the IPS and Final Report):" | CHANGED |
| FAQs, first permitted item | "Any stock from any exchange available on WInS priced at $5 (or the equivalent of $5 in the local currency) or higher." (faqs.txt:43) | "Any stock from any exchange available on WInS." | CHANGED ($5 wording removed) |
| Trading Details, "Approved Securities" | "Your team may invest in:" (trading.txt:43) | "Your team may invest in (for BOTH contributions):" | CHANGED |
| Trading Details, stock line | "Stocks: Any stock available on WInS priced at $5 or more, or the equivalent of $5 in its local currency." (trading.txt:44) | same | unchanged |
| home, guide, client, deliverables, wins | - | - | identical (only a duplicated site-title line differs, a text-extraction artefact) |

Source of live text: `R4_pages/smapply_faqs.txt` lines 47-50, `R4_pages/smapply_trading.txt` lines 48-51 (raw HTML in
`R4_pages/raw/`). VERIFIED 16 Oct.

When did these change? On 14 Oct, between 15:33 and 20:34 UTC (11:33 a.m. to 4:34 p.m. ET on 14 Oct; 2:33 a.m. to
7:34 a.m. Sydney on 15 Oct). Evidence: earlier assistant copies saved at 13:26, 14:10, 14:51 and 15:33 UTC still show
the old wording (scratchpad/oct14/rules/live/ok_faqs.html, ok_trading.html; oct14/ops/live/; oct14/rules-8/smfaq.html;
oct14/wins9/0980b861.html = faqs, 8a5e64f0.html = trading). The copies saved at 20:34 UTC show the new wording
(oct14/factcheck/dl/sm_faqs.html, sm_trading.html). File save times are used as fetch times. So the repo snapshot was
correct when taken; Wharton edited the pages later that day. Saved in DIFFS.txt section E.

Earlier history (from the repo, not re-checkable): the insight_v1 run recorded on 27 Sep that the FAQ list began with
"Cash" (research/insight_v1/phase_A/wins_week1_guardrails.md:194-197). Neither the 14 Oct snapshot nor today's page lists
cash. Whether Wharton deleted "Cash" or the 27 Sep capture was wrong is UNVERIFIED.

**What this means (INTERPRETATION):**
- The 6 Oct email's rule is now public, in Wharton's own words: Laura's real plan, in the IPS and in the Final Report,
  may use only stocks, ETFs and government/Treasury bonds available on WInS. Anything else is "NOT permitted":
  "Anything other than the approved investments listed above." Cash is no longer on the list.
- Where this bites: the team's own Final Report log still says "STRIPS in real life, IBTM as the WInS stand-in"
  (team/google_drive/final_report.md:24, a 5 Oct entry written before the 6 Oct email). The insight_v1 spec moves the
  kept money "to U.S. dollar Treasury bills" in 2033 (research/insight_v1/phase_E/E6_final_spec.md:268). Neither may
  appear in the IPS or Final Report as part of Laura's plan unless the instrument is a WInS-listed ETF or bond.
- A fix must achieve: every instrument named for Laura (2027, 2028, 2031, 2033 and the reserve's run-down) is either a
  WInS-listed ETF, a WInS-listed Treasury bond or a WInS-listed stock, and the team can show it is listed (screenshot
  or WInS search). "Cash" in the plan should be described only as WInS cash or a listed short-Treasury ETF; whether
  plain cash is allowed in Laura's plan is UNVERIFIED (ask through Contact Us if it matters).
- The $5 stock minimum now appears only on Trading Details. Caplet holds no single stocks, so nothing is affected.

### 1.2 Pages not in the repo snapshot

- **SMApply programme page** (public): https://wghsinvcomp.smapply.us/prog/2026-2027_wharton_global_high_school_investment_competition_/
  It shows "Opens Aug 15 2026 12:00 AM (EDT)" and "Deadline Oct 9 2026 05:00 PM (EDT)", and lists the five key dates
  ("November 6: Investment Policy Statement Due and Trading Ends"). The "Deadline Oct 9" is the roster date. Whether it
  affects access to later tasks is UNVERIFIED; the team has already submitted the roster, so it is likely harmless.
  Saved: `R4_pages/smapply_prog.txt`.
- **Other SMApply slugs:** I tried 27 likely slugs (final-report, resources, rules, ai-policy, semifinals, judging,
  announcements and others). All return 404. There is no hidden public page for the Final Report instructions yet.
  The Deliverables page still says "Detailed Final Report instructions and requirements will be shared on November 9."
- **The client case is public.** The SMApply Client page links to a public Box file named "2026_WGY_Gao Case
  Study-FINAL.pdf" (523,259 bytes). It downloads without logging in and matches the repo copy exactly. The PDF's
  internal creation date is 10 Sep 2026. (R4_pages/box/.)
- **Box file names and dates** (from the Box pages and PDF metadata, VERIFIED): TNA instructions "2026_WGY_Trading
  Notes Analysis-FINAL.pdf" (created 10 Sep 2026); IPS instructions "2026_WGY_Investment Policy-FINAL.pdf" (9 Sep);
  Guide (9 Sep); Infographic "2026_WGY_Competition Inforgraphic-FINAL.pdf" (14 Sep); school template "26-27 School
  Documentation Template.pdf" (11 Sep).

### 1.3 Wharton Global Youth pages

Last-modified times from the site's own WordPress API (site timezone America/New_York), VERIFIED 16 Oct:

| Page | Last modified (ET) | Changed since 14 Oct? |
|---|---|---|
| Competition main page `/competitions/investment-competition/` | 11 Sep 2026 17:06 | no |
| Rules & Roles `/competitions/investment-competition/rules-roles/` | 8 Sep 2026 19:39 | no |
| FAQ `/competitions/investment-competition/faq/` | 13 Sep 2026 19:57 | no |
| Register Now | 11 Sep 2026 17:05 | no |
| Archive | 7 Jul 2026 15:01 | no |
| Case Study page | 7 May 2026 11:50 (says only "More information coming soon.") | no |
| Contact Us form | 21 Sep 2026 16:27 | no |
| **AI Policy `/ai-policy/`** | **14 Oct 2026 09:48 (13:48:39 UTC)** | yes, see below |

**The AI-policy change.** A copy saved by the previous review at 13:22 UTC on 14 Oct (before the edit) and today's page
differ in one place only. This paragraph was deleted:

> "Comment & Win
> Commenting on content is, by nature, expressing personal views, sentiments and opinions. Comments should reflect
> students' voices and your ideas, not those generated by AI. Often, the most authentic comments stand out and succeed.
> AI has little relevance or purpose within the context of the Wharton Global Youth Comment & Win competition."

Comment & Win is a separate Wharton contest. The Investment Competition section is unchanged. All 51 Wharton-page quotes
the insight_v1 run recorded on 27 Sep (research/insight_v1/phase_A/case_register.md:675-831, items R-W1 to R-W51) are
still present word for word today (my script check, 16 Oct).

**2026-27 news posts:** none. The newest post on the whole site is "Stuyvesant High School Wins the 2026 Wharton Global
High School Investment Competition" (30 Apr 2026). No events or stories are listed. Media uploads since June 2026
include no 2026-27 competition documents and nothing about Laura (only photos from last year's finale, site graphics
and three image-only "Untitled" PDFs from 1 Jul 2026). (WordPress API, 16 Oct.)

**Old pages that still load but are out of date:** `/competitions/investment-competition/trading/` redirects to a 2020
page, "Trading Outside the U.S." (last modified 16 Nov 2020). It says things like "especially since the client has a
short-term need". Do not cite it. The SMApply Trading Details page is this year's rule.

---

## 2. Official media about Laura or the case

**Finding: none in public.** Checks made on 16 Oct:
- Wharton Global Youth site: posts list (newest 30 Apr 2026); site search for "Gao", "Laura", "Messy Roots", "Wuhan"
  (no relevant hit); events and stories (empty); media uploads since June 2026 (nothing on Laura); the Case Study page
  still says "More information coming soon."
- YouTube, Wharton Global Youth channel (https://www.youtube.com/channel/UCYDmBnoF6ux7r5R_NwK9iug): newest video is
  about 8 months old ("A Neurodivergent Teen Launches a Line of Fidget Jewelry"). Channel search for "Laura Gao"
  returns nothing. The only competition webinar a channel search for "investment competition" shows is "2020-2021
  Wharton Global High School Investment Competition: Informational Webinar" (about 6 years old).
- Wharton Magazine tag "Laura Gao": two items only, a 2022 alumni Q&A and a 2022 book round-up, plus a 2020 mention.
  None is about the competition.
- Web search for LinkedIn or Instagram posts naming Laura as the client found nothing indexed. These sites need a
  login, so a post could exist without showing up. UNVERIFIED.

So the only official words about Laura this year are the case PDF, the SMApply Client page and the main page sentence
about real clients. The FAQ says "Copies of the weekly emails will also be posted on the Wharton Investment Simulator
(WInS) for all team members to view" (R4_pages/wg_faq.txt:273). The team should read those weekly emails in WInS for
any client message. That needs a login, so it is the team's job, not mine.

**What official material reveals about what the client values and how she will be "heard" (INTERPRETATION unless
quoted):**
- The case frames her as someone who takes "thoughtful risks" but wants "an appropriate balance between pursuing
  growth and protecting the capital required for her goals" (Laura_Gao_2026_Client_Profile.txt:68-74).
- Her credibility with co-sponsors is the stated risk: "If Laura promises more than she can ultimately contribute, she
  could damage her credibility" (case:114-115).
- Last year the client came to Learning Day: "Students also had the opportunity to hear directly from this year's
  competition client, Connor Barwin ... During an engaging Q&A, students asked thoughtful questions about his work and
  investment priorities" (https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/,
  accessed 16 Oct 2026). So Laura may meet the finalists in April 2027 (UNVERIFIED for this year). She may also hear
  the pitches: last year's semifinal pitch had to "Be a pitch to Connor Barwin, your potential client" (section 5.3).
- Last year's guidance treated the client as a non-expert listener: "Do not assume Connor or the judges will understand
  all technical investment concepts without explanation" and "Practice your presentation with someone who has no prior
  investing knowledge" (2025-26 Semifinalists Next Steps PDF, section 5.3).
- Laura is unusually data-literate for a client. Her website menu has a "Visual Data Stories" section
  (https://lauragao.com/hey/, accessed 16 Oct), her degree is in statistics (case:16) and her CV lists SQL, R and
  Tableau. INTERPRETATION: honest, simple charts that tell one story will land; dense or misleading charts will not.

---

## 3. Laura's real background vs the case

### 3.1 Real or fictional? What the repo says and what Wharton says

- Repo: "Laura is a fictional client." (COMPETITION.md:49). This is the team's "single source of truth"
  (COMPETITION.md:5-6). It is wrong.
- Wharton main page: "Each year, teams are introduced to a new case study featuring a Wharton School alum. While the
  client is real, the financial scenario is developed specifically for the competition."
  (https://globalyouth.wharton.upenn.edu/competitions/investment-competition/, accessed 16 Oct 2026; R4_pages/wg_ic.txt:242)
- Archive page: "Since 2012, the Wharton Global High School Investment Competition has featured Wharton alumni as the
  competition client, giving student teams the opportunity to apply their investment knowledge to a real-world client
  case." (https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/, accessed 16 Oct 2026)
- Contact ban: "IMPORTANT: Teams are not permitted to contact Laura Gao." (smapply_public_2026-10-14/client.txt:23) and
  "Teams may not contact the Competition client. Teams that violate this rule will be disqualified."
  (Rules & Roles, R4_pages/wg_rules_roles.txt:235)
- The repo's research already knew the right version: "the financial scenario is fictional (R-W4)" appears across
  research/insight_v1/phase_C/. Only COMPETITION.md:49 merges the two ideas.

What a fix must achieve: the team's source of truth should say the person is real and the scenario is invented, and
remind every member never to contact her (or tag her online). The deliverables should not present her real finances or
real plans as case facts, and should not present case facts (the residency, the $450k) as her real life.

### 3.2 Case facts checked against public sources

| Case says (file:line) | Public record (source, accessed 16 Oct 2026) | Match? |
|---|---|---|
| "Born in Wuhan, China, and raised in Texas" (case:13) | Born in Wuhan, grew up in a Texas town (Wikipedia, R4_pages/lg_wikipedia.txt:110); "immigrated to Texas from Wuhan as a child" (Wharton Magazine, 6 Apr 2022) | Yes |
| "While studying at the Wharton School ... launched a small business" (case:14-15) | "Wharton sophomore Laura Gao recently launched her own company Draw Street Journal which designs and sells laptop decals, many of which are Penn-themed." (The Daily Pennsylvanian, Jan 2016, https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a) | Yes. The case's "small business" is this decal shop |
| "graduated in 2018 with a degree in Statistics & Information Decisions Management" (case:16) | Her CV: "Bachelor of Science in Statistics and Information Decisions, Concentration in Product Design" (https://lauragao.com/s/Laura-Gao-Resume.pdf, line 30 of saved text). Wharton Magazine (her words): "a degree in business analytics". Poets&Quants 2018: "Major: Economics with a concentration in Business Analytics" | Year matches ("W18"). The degree name differs between sources. Use the case wording |
| "product manager in the technology industry" (case:16-17) | CV: "Twitter, Product Manager 2018-2020"; "Amazon.com, Data Analyst 2017" (CV lines 19, 24); Wikipedia: hired by Twitter, left after the book offer (lg_wikipedia.txt:110, 113) | Yes |
| "In 2020, Laura published The Wuhan I Know" (case:18) | Published on Twitter in March 2020 (Wharton Magazine; Wikipedia:112); NPR story 4 Apr 2020 | Yes |
| "bestselling graphic memoir, Messy Roots" (case:21-22) | Published 8 Mar 2022 by HarperCollins (Wikipedia, Messy Roots); imprint Balzer + Bray (Wharton Magazine). "a spot on the Indie Bestseller List" (her words, Wharton Magazine); "Debuted on #9 on Indies Bestsellers List" (her CV, self-reported) | Yes, on the indie list. A New York Times list place is UNVERIFIED; do not claim it |
| author, illustrator, entrepreneur, educator, public speaker (case:5, 24-25) | "Professor of Comics at California College of the Arts" (her site, lg_site_hey.txt:30); freelance studio "LG Studios ... 2020 - Present" (CV line 8); a speaking guide on her site (repo: research/insight_v1/phase_D/D13a_laura_quotes_verified.md:168) | Yes |
| (not in case) | Second book: "Kirby's Lessons for Falling (in Love)", 2025 (Local News Matters, 12 Feb 2026) | Case omits it |
| (not in case) | Co-organiser of Pride in Panels, a free San Francisco LGBTQ+ comics festival: first one in 2024 drew "More than 2,000 people"; 2026 edition "remaining free for exhibitors and attendees", run with a public-library partner, with "mini grants to 20 comic creators" (Local News Matters, https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/) | Case omits it |
| (not in case) | 2020: "joined a volunteer effort to create PPE via open-source 3-D printing through MyMaskMovement.org" (Wharton Magazine Fall/Winter 2020, "Answering the Call"); as a student she "taught web development and financial literacy to high school students in West Philadelphia" (Poets&Quants 2018, line 68) | Case omits it |
| Educator role (case:5) | California College of the Arts "will 'wind down its current operations' and close by the end of the 2026-2027 academic year"; Vanderbilt will buy the campus (KQED, Jan 2026, https://www.kqed.org/arts/13985359/california-college-of-the-arts-closing-vanderbilt-university) | Her real teaching post is ending. The case does not depend on it |
| The Taiwan residency in 2033 (case:75-80) | No public plan found (web searches 16 Oct). A 2022 podcast episode (transcript made in 2025, with visible transcription errors) has her describing time spent in Taiwan and mentioning "some art residencies at the top of the mountains there" (https://www.themaverickshow.com/wp-content/uploads/2025/10/190_Laura_Gao_Transcript.pdf). Wording UNVERIFIED against the audio | The residency looks inspired by a real tie, but it is part of the invented scenario |
| $300k, $150k from "publishing advances, speaking engagements, licensing" (case:43-45) | Not public. Her speaking guide publishes no fees (repo D13a:168) | Invented for the case. Do not guess her real finances |
| Pull quote "The only person who needs to believe in something is yourself." (case:31-33) | The repo's 27 Sep check found no source in 36 pages (research/insight_v1/phase_D/D13a_laura_quotes_verified.md:23-26). Not re-run today | Cite as the case's words, never as hers |
| The case uses "she/her" | Her site: she uses "she/her and they/them pronouns" (lg_site_hey.txt:31) | Consistent. Follow the case |

**Pattern worth knowing (INTERPRETATION):** the case keeps her business and data side (Wharton, product manager,
small business, bestseller) and adds an invented community project. Her real public life already includes running a
free community event with partners and small grants. That is a real-world parallel to co-sponsors and grants in the
case (case:83-86, 108-124). It can help the team understand her world. It cannot be used to guess the residency's fees,
budget or her real money (the repo's own rule: research/insight_v1/phase_C/parked.json, R-AN56).

**Privacy rules for using any of this (from the brief and the repo's screen):** no contact details (her CV and website
publish them; they are redacted in my saved copies); nothing about family, relationships, home or identity as a reason
for an investment choice; no quotes that cannot be traced to her (the pull quote; podcast transcript lines). Cite the
outlet and year for anything used.

---

## 4. Wharton's AI policy, word for word

All four texts VERIFIED 16 Oct 2026. They have not changed since at least 27 Sep (section 1.3).

**A. Rules & Roles, "Use of Generative AI"** (https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/; R4_pages/wg_rules_roles.txt:271-275):
> "Teams may use generative AI tools (such as ChatGPT) for brainstorming and idea generation. However:
> AI-generated content may be inaccurate, incomplete, or misleading and should be used with caution.
> AI-generated work may not be submitted as your own.
> Any AI-generated material included in your report must be properly cited, just like any other reference source.
> Plagiarism, misuse of AI, or any other form of academic dishonesty will be handled in accordance with the Competition
> Ethics and Code of Conduct policies."

**B. Rules & Roles, "AI Policy"** (same page, line 313):
> "You may use generative AI programs (e.g., tools like ChatGPT) to help generate ideas and to brainstorm. However, you
> should note that the material generated by these programs may be inaccurate, incomplete, or otherwise problematic.
> Beware that use may also stifle your own independent thinking and creativity. You may not submit any work generated
> by an AI program as your own. If you include material generated by an AI program, it should be cited like any other
> reference material (with due consideration for the quality of the reference, which may be poor). Any plagiarism or
> other form of cheating will be dealt with severely under relevant Investment Competition policies. See Ethics and
> Code of Conduct section above."

**C. AI Policy page, Investment Competition section** (https://globalyouth.wharton.upenn.edu/ai-policy/; R4_pages/wg_ai_policy.txt:227). This is the strictest version:
> "You may use generative AI programs (e.g., tools like ChatGPT) to help generate ideas and to brainstorm. However, you
> should note that the material generated by these programs may be inaccurate, incomplete, or otherwise problematic.
> Beware that use may also stifle your own independent thinking and creativity. You may not submit any work generated
> by an AI program as your own. All material referenced or generated by AI should be cited like any other reference
> material (with due consideration for the quality of the reference, which may be poor). If you use AI to assist you in
> any way during the competition, how you use it must be recorded in your Works Cited pages. Any plagiarism or other
> form of cheating will be dealt with severely under relevant Investment Competition policies."

Its Ethics paragraph (line 223) adds a clause the Rules-page version lacks: "We trust that you will not lie about your
investment decisions and outcomes, fabricate analyses, invent teamwork and experiential stories, compensate advisors,
education consultants, or other agents, enroll in non-Wharton extracurricular courses that claim to "teach" the
competition, pass AI generated writing or work off as your own, or plagiarize existing strategies."

**D. Statement of AI Use** (same page, line 211):
> "When students express themselves in the Wharton Global Youth Program, they must use their voice and words. Using
> somebody else's work without crediting the source – including generative AI — is plagiarism. Guided by the policies
> of faculty, instructional teams, and staff, AI-generated work should be cited like any other reference material,
> including how and where students used AI-generated information."

**Checklist Questions** (same page, lines 228-235), exact:
- "Does this submission represent my voice, my opinion, my research? Did I come to my current conclusion before or
  after using generative AI tools? Does using the tools still allow me to come to my own conclusions?"
- "Did I verify the information I gathered from generative AI tools, whether it is the research it mentions, or the
  source it cites? Can I trace all of my citations to academically recognized publications?"
- "Did I double check the numbers and information are most up-to-date?"
- "Did I understand the key learnings and how to arrive at the answers without the assistance of generative AI tools?"
- "Have I checked all the limitations of generative AI tools to make sure my work is credible?"

Related lines on the same page that are written for other programmes (scope matters):
- Pre-baccalaureate courses: "Don't use AI for personal reflection or opinion-based tasks. We are interested in hearing
  your opinions, your stories and your thoughts." (line 271). Not a competition rule, but a strong signal for the TNA
  reflections and the Final Report's experience section.
- Applications to Wharton programmes: Wharton "may use its own proprietary and/or licensed AI solutions in order to
  identify AI-authored elements of applications" (line 219). Whether anything similar is used on competition entries is
  UNVERIFIED. The Rules page does say Wharton "reserves the right to engage its employees and third-party private
  investigatory firms and/or forensic analysts to ensure compliance ... and to ensure that all teams are competing
  fairly" (wg_rules_roles.txt:318).
- Last year's semifinal written answers: "We are looking for your authentic team voice, not generated or generic
  responses." (2025-26 Semifinalists Next Steps PDF, page 4.)

**What the policy requires, as a checklist (no wording supplied):**
- [ ] AI used only for ideas, brainstorming, checking and questions. No AI-written sentences in the TNA, IPS, pitch or
      Final Report (A, B, C, D).
- [ ] Every AI use during the competition recorded in the Final Report's Works Cited, including "how and where" (C, D).
      This covers research, number checks, the strategy brief, IPS drafts the team rewrote, and AI help in WInS.
- [ ] Any AI-generated material that is included (a chart, a table, a figure) is cited like a source (A, C).
- [ ] Every AI-sourced number re-checked against a primary source (Checklist 2-3).
- [ ] Reflections and the experience story are true and the students' own (Ethics: no "invent teamwork and experiential
      stories").
- [ ] The IPS allows no citations, so its sources and any AI use go in the Final Report
      (2026_WGY_Investment_Policy-FINAL.txt:123-125).

---

## 5. How judging works this year (what is public)

### 5.1 This year's official statements

| Topic | Exact text | Source (accessed 16 Oct 2026) |
|---|---|---|
| Who picks the 50 | "Following the submission of final reports, a panel of judges selects 50 semifinalist teams. Those teams are invited to present their investment strategies during the virtual Semifinals. The top 10 teams advance to the Global Finale at the Wharton School in Philadelphia, where they compete for the title of Global Champion." | Main page (wg_ic.txt:246) |
| What the 50 are picked on | "The top 50 teams will be selected as semifinalists based on the strength of their Investment Policy Statement (IPS) and Final Reports." | Rules & Roles (wg_rules_roles.txt:267) |
| What is evaluated | "Your Trading Notes Analysis, Investment Policy Statement and Final Report are evaluated." | SMApply Deliverables (deliverables.txt:27) |
| Read together | "Evaluators will consider the three deliverables together." | Case (Laura_Gao_2026_Client_Profile.txt:161) |
| IPS format gate | "Submissions that do not meet the requirements below will not be considered for semifinal selection." | IPS instructions (2026_WGY_Investment_Policy-FINAL.txt:82-83) |
| TNA check | "The Trading Notes must correspond to trades executed in WInS. Yes, we will verify this." | TNA instructions (2026_WGY_Trading_Notes_Analysis-FINAL.txt:53) |
| All five criteria | "We are looking for teams that score exceptionally well on all five components of the criteria" | Wharton FAQ (wg_faq.txt:286) |
| WInS results | "your team's standings on WInS have little to do with the final outcome" | Wharton FAQ (wg_faq.txt:288) |
| WInS results (SMApply version) | "Gains and losses generated in WInS are not used to select winning teams" | SMApply FAQ (faqs.txt:81) |
| What judges reward | "Teams are evaluated on the quality of their investment strategy, how well it aligns with their client's objectives, the strength of their research and analysis, and their ability to clearly communicate and defend their recommendations." | Main page (wg_ic.txt:245) |
| Semifinal format | "a short presentation (via video conference for the Semifinals and live or via video conference for the Global Finale) about your team's strategy, analysis and experience over the past 10 weeks to a live panel of judges. All team members must participate." | Wharton FAQ (wg_faq.txt:296); SMApply FAQ (faqs.txt:89) |
| Semifinal paperwork | "Semifinalists must also submit documentation on official school letterhead confirming that: The team has permission to participate in the Competition. All students and the advisor are affiliated with the school." | Rules & Roles (wg_rules_roles.txt:267-269) |
| Consent | "All semifinalists and global finalists must submit a signed Consent and Waiver of Liability (or a parent/guardian signature if the student is under 18)." | Rules & Roles (:284) |
| No recording | "Video recording, audio recording, photography, screenshots, or posting presentations or participants online during the Semifinals or Global Finale is strictly prohibited. Unauthorized recording or sharing may result in dismissal from the Competition." | Rules & Roles (:286) |
| A judging committee exists | children of Penn staff may enter "provided their parent or guardian is not a member of the Competition judging committee" | Rules & Roles (:227) |
| Feedback | "No. Teams will not receive individual feedback." | Wharton FAQ; SMApply FAQ (faqs.txt:78) |
| Dates | "TBD Semifinalists (top 50 teams) announced"; "TBD Virtual Semifinals"; "April 29 & 30 Learning Day & Global Finale at the Wharton School, University of Pennsylvania, Philadelphia" | Main page (wg_ic.txt:236-239). In the 2026-2027 date list, so 2027: Thursday 29 and Friday 30 April (my calendar check). The year is implied, not printed |
| Finale travel | "Teams advancing to the Global Finale in Philadelphia may participate either in person or virtually." In person: "At least one adult (advisor, another school representative, or parent/guardian) must accompany the team." | Rules & Roles |
| Prizes | Digital Credential "in February 2027" for all teams that submit the required deliverables and meet minimum requirements; certificates for semifinalists and finalists; each Global Finalist student: "A waived course fee for the online course Understanding Your Money"; Champion students: a free online summer programme place (Future of the Business World, Financial Decision Making, Essentials of Leadership, Moneyball FLEX or Moneyball: Training Camp); other finalists: "a 50% discount" on one summer online programme; the Champion school may "fast-track one team to the semifinal round of the 2027-2028 competition" | Rules & Roles (:292-307) |
| Scale | Last year's completion numbers on the main page (from the HTML counters): 2,339 teams, 79 countries, 12,145 students, 1,625 advisors ("2025-2026 Participation Completion Numbers") | Main page HTML; Top 50 = about 2.1% of 2,339 (my arithmetic) |

**Discrepancy to manage (INTERPRETATION):** the Rules page names only the IPS and Final Report for the Top 50 cut. The
SMApply page and the case say the TNA is evaluated and read with the others. Safest reading: the TNA is scored and sets
the first impression of the strategy, and its notes must agree with the IPS; but the IPS and Final Report decide the
cut. An inconsistent TNA can still hurt the "consistency with the team's IPS" part of Investment Strategy
(deliverables.txt:31).

### 5.2 Who judged last year (2025-26), as a guide only

All from official Wharton news posts, accessed 16 Oct 2026. Whether 2026-27 uses the same people is UNVERIFIED.

- **Top 50 (written reports):** "with the help of our Wharton School student evaluators, as well as a professional
  review panel of asset managers from Aberdeen Investments in Philadelphia, we have arrived at ... the announcement of
  this year's semifinalist teams" (27 Jan 2026,
  https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/).
  Final reports were submitted 12 Dec 2025 and the 50 were announced 27 Jan 2026 (about 6.5 weeks).
- **Semifinals:** "49 semifinalist teams advanced to the virtual semifinal rounds, where they presented their strategies
  to panels of Wharton alumni and industry experts." Fifteen judges were named; 11 of the 15 list a Wharton degree.
  They are a mix of investment managers, family-office and company heads, plus the CEO of Stock-Trak (WInS's
  provider), a UBS wealth-management market director, a J.P. Morgan investment banker and an educational consultant
  (20 Mar 2026,
  https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/).
- **Finale:** 11 teams presented "to a panel of industry leaders": five judges from Aberdeen Investments, Achilles,
  King Street, Zen Capital Partners and Wharton Research Data Services (30 Apr 2026,
  https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/).
- **The client** spoke at Learning Day and took student questions (same 30 Apr post).

INTERPRETATION: the first readers of the written reports may include Wharton students. Their scoring rules are not
public. Reports that are easy to follow on a first read, with the answer up front, are safer with mixed readers.

### 5.3 Last year's semifinal format (official PDF, 2025-26)

Source: "2025-2026 Semifinalists - Next Steps" (https://globalyouth.wharton.upenn.edu/wp-content/uploads/2026/01/25%E2%80%9326-Semifinalists-%E2%80%93-Next-Steps-FINAL.pdf,
uploaded 23 Jan 2026, accessed 16 Oct 2026; saved R4_pages/wg_2025_26_semifinalists_next_steps.txt). The 2024-25
version had the same structure. The 2026-27 version is not published; FORMAT UNVERIFIED for this year.

Exact requirements last year:
- "You have 10 minutes for your team presentation. We will not watch presentations beyond 10 minutes."
- "Teams may include up to 15 slides." Guidance: "approximately 9–11 core slides".
- "The video should begin with an on-screen introduction of each team member."
- "Every team member must have a speaking role and briefly explain how they contributed value to the team."
- "Be a pitch to Connor Barwin, your potential client."
- "Build upon information and insights presented in your midterm and final competition reports. Do NOT introduce
  completely new material, or your team will be disqualified." "Teams are not permitted to present a partially or
  entirely new strategy." Teams "may reflect on strategic weaknesses, limitations, or missed opportunities without
  changing the original strategy."
- Must include: "a snapshot of your team's recommended investment portfolio"; "a case study of one stock or ETF in your
  portfolio and explain how it aligns with your overall strategy"; "details of your analytical approach and overall
  competition experience".
- "Avoid excessive technical jargon. Your presentation should reflect your team's authentic voice rather than trying to
  sound overly complex or impressive." "Why use 25 words when three will do?"
- Written response: four questions, "Each response must be 250 words or fewer", "You will not be able to include
  graphics or visuals", about four days to answer.
- Deadlines were 8:00 a.m. ET (video due Monday 9 Feb; questions Thursday 19 Feb; answers Monday 23 Feb). In February
  8:00 a.m. ET is 00:00 (midnight) Sydney time the next day. If repeated, those are midnight deadlines for Caplet.
- Judged on the five criteria "• Written Responses" as a sixth item.
- "The top two teams from each semifinal group will be announced the week of March 9".

Note the mismatch: this year's FAQ says "a live panel of judges" by video conference, while last year's process was a
recorded video plus written answers. Which one 2027 uses is UNVERIFIED.

**What this means for the Final Report (knowledge, not text):**
- [ ] Everything the team might want to say in a semifinal pitch must already be in the Final Report or IPS, because
      new material was a disqualification risk last year.
- [ ] The Final Report should contain a full, plain analysis of at least one ETF the team holds (for Caplet: VT or one
      iBond ETF such as IBTM), showing its role in the strategy. Last year this was a required pitch element.
- [ ] The experience section should record what each of the six members actually did, without ranking anyone, because
      each member had to explain their own contribution.
- [ ] A one-screen "portfolio snapshot" must be possible from the report's numbers.
- [ ] The strategy must survive questions without changing (written answers or live Q&A test "defend").

---

## 6. Still UNVERIFIED (could not confirm on 16 Oct)

- The exact minute on 14 Oct when the SMApply FAQ and Trading Details edits went live (known window: 15:33-20:34 UTC).
- Whether the 27 Sep "Cash" line on the SMApply FAQ was real, and whether plain cash is allowed in Laura's plan now.
- Whether a client video, webinar or message exists inside SMApply or WInS (login needed; the team should check).
- Any LinkedIn or Instagram posts by Wharton Global Youth about Laura (not indexed; login walls).
- Who judges in 2026-27 at each stage; whether Wharton students read the written reports again.
- The 2026-27 semifinal format (recorded video vs live panel), dates and length.
- Whether the Top 50 cut weighs the TNA (Rules page omits it; SMApply and case include it).
- Whether the semifinal letterhead request is a second letter or the same one sent on 4 Dec.
- Whether "Deadline Oct 9" on the SMApply programme page affects later submissions (likely not).
- The year "April 29 & 30" refers to (implied 2027 from the 2026-2027 date list).
- Podcast transcript wording about Taiwan art residencies (AI-style transcript; not checked against audio).
- Any New York Times bestseller status for Messy Roots (only the indie list is supported).

---

## 7. Sources and saved files (all accessed 16 Oct 2026)

Official, live:
- SMApply: https://wghsinvcomp.smapply.us/ and /res/p/{guide, client, deliverables, trading, wins, faqs}/;
  programme page https://wghsinvcomp.smapply.us/prog/2026-2027_wharton_global_high_school_investment_competition_/
  -> R4_pages/smapply_*.txt
- Box PDFs linked from SMApply (case, TNA, IPS, school template, guide, infographic) -> R4_pages/box/ (hashes match the
  repo, DIFFS.txt section D)
- Wharton Global Youth: /competitions/investment-competition/ (main), /rules-roles/, /faq/, /archive/, /case-study/,
  /register-now/, /ai-policy/, /investment-competition-contact-us/, /competitions/ -> R4_pages/wg_*.txt
- WordPress API (page modified times, posts, search, media): https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/ ->
  R4_pages/raw/wp_*.json
- 2025-26 news posts: 27 Jan, 20 Mar and 30 Apr 2026 -> R4_pages/news_2026_*.txt
- 2025-26 Semifinalists Next Steps PDF -> R4_pages/wg_2025_26_semifinalists_next_steps.txt
- YouTube channel UCYDmBnoF6ux7r5R_NwK9iug (videos tab and channel search) -> R4_pages/raw/yt_*.html
- Public WInS landing page https://edu.stocktrak.com/wharton/ (nothing new) -> R4_pages/wins_public.txt

About Laura (public, reputable):
- Wharton Magazine Q&A, 6 Apr 2022: https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/
- Wharton Magazine, Fall/Winter 2020, "Answering the Call": https://magazine.wharton.upenn.edu/issues/fall-winter-2020/answering-the-call/
- NPR, 4 Apr 2020: https://www.npr.org/sections/goatsandsoda/2020/04/04/823825436/the-wuhan-i-know-a-comic-about-the-city-behind-the-coronavirus-headlines
- Poets&Quants, 30 Mar 2018: https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/
- The Daily Pennsylvanian, Jan 2016: https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a
- Local News Matters (Bay City News), 12 Feb 2026: https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/
- KQED, Jan 2026: https://www.kqed.org/arts/13985359/california-college-of-the-arts-closing-vanderbilt-university
- Her website https://lauragao.com/hey/ and CV https://lauragao.com/s/Laura-Gao-Resume.pdf (self-published; contact
  details redacted in saved copies)
- Wikipedia: https://en.wikipedia.org/wiki/Laura_Gao and https://en.wikipedia.org/wiki/Messy_Roots (secondary; used only
  where it matches primary sources)
- The Maverick Show transcript PDF (see 3.2; wording UNVERIFIED)

Earlier copies used for comparisons: scratchpad/oct14/factcheck/dl/*.html (14 Oct 20:20-20:38 UTC) and
scratchpad/oct14/rules/wgy/ai-policy_.html (14 Oct 13:22 UTC). Tools: R4_tools/fetch.py (fresh fetch, no cache),
R4_tools/h2t.py (HTML to text).

Blocked: web.archive.org, archive.ph and timetravel.mementoweb.org (connection reset or refused), so no older archive
copies; HarperCollins (403).
