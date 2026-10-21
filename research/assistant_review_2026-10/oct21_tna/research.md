# TNA research: how Wharton marks the Trading Notes Analysis, and what strong ones look like

Prepared Wed 21 Oct 2026 (Sydney) for Team Caplet. This is AI-generated research (Claude Code), for checking only.
It contains **no replacement wording** for any note or reflection. If the team uses it, log that in `office/LEDGER.md`
and the Final Report's Works Cited.

**Labels.** OFFICIAL = a Wharton page or PDF that I re-read today. OFFICIAL-COPY = Wharton text reposted by a third
party (e.g. Scribd). TEAM-DOC = a team's own document. INFERENCE = my reading. UNVERIFIED = not confirmed.
**Web copies** are in `SP/oct21/tna/research/web/` (SP = the session scratchpad). All live pages were fetched on
21 Oct 2026 with plain curl and a cache-busting `?cb=` query. The three feedback PDFs I re-downloaded have the same
md5 hash as the 16 Oct copies, so their text is reused (`*.cached.txt`). Only public, logged-out SMApply `/res/p/`
pages were read. No WInS or SMApply account was used.
**Privacy.** Other teams appear by team name only. No student names or emails are copied, even where the uploads show them.

---

## 0. Bottom line (five points)

1. **No published TNA rubric exists.** The TNA is marked against the same five criteria as the IPS and Final Report
   (`deliverables.txt:27, 55-59`). The three documents are read together (case:161). The TNA instructions
   (`2026_WGY_Trading_Notes_Analysis-FINAL.txt`, below "TNA:n") are the only marking guidance written for the TNA itself.
2. **The TNA is new as a stand-alone, early, evaluated deliverable in 2026-27.** In 2022-23 to 2025-26 it was a
   one-page section inside the Final Report (section 2). It is now due in Week 4, before the IPS. It is marked
   "evaluated", but the rules page bases the Top 50 on "IPS and Final Reports" only (`p_16670.txt:100`). Its weight in
   the cut is UNVERIFIED. Teams get no individual feedback (`p_16654.txt:142`).
3. **The 2026-27 wording moves the test** from "how did this trade shape your final strategy" (looking back, past years)
   to "show the decision **supported, tested, or refined** a strategy that matches the IPS" (TNA:12, 29-31). The
   reflection must cover three set points in at most 100 words (TNA:46-52), and Wharton checks the note text against
   WInS (TNA:53).
4. **No Top 10 or champion team's trading notes are public.** The only reflection section from a Top 50 team I could
   find is Mochi's (2023-24). It works because it admits an early momentum trade, quotes it exactly, and then shows a
   later note that follows a rule. Every non-qualifying example found fails in the same few ways: past returns as
   proof, jargon or home-made scores, generic "this taught us", no client link, and no quoted note (section 4).
5. **The most repeated official message** across years is "We want to understand WHY you are making certain
   decisions" (feedback PDFs 2021-22 to 2023-24). Next comes plain language in the team's own voice. Section 5 turns
   these into a checklist.

---

## 1. Official 2026-27 texts on Trading Notes and the TNA (all OFFICIAL, re-read 21 Oct)

Repo base: `/home/user/caplet-investment/competition/official/2026_27/`.

| # | Quote (30 words or fewer) | Source |
|---|---|---|
| O1 | Purpose: "demonstrate how your team's investment decisions reflected the strategy it developed for the client, including its approach to growth, risk, liquidity, funding reliability, financial flexibility" | TNA:4-6 |
| O2 | "select three investment decisions that best illustrate your team's strategic thinking" | TNA:11 |
| O3 | Explain "how it aligned with, tested, or refined your overall investment strategy, and how it supported the client's goals, funding needs, or risk considerations" | TNA:12-13 |
| O4 | "Collectively, the decisions should demonstrate how your team used individual investments as part of a cohesive portfolio strategy." | TNA:14-15 |
| O5 | "The focus should be on the quality of your reasoning and the intended role of each decision, not simply whether an investment gained or lost value" | TNA:15-16 |
| O6 | Not expected yet: "calculate the final size of the operating reserve, complete long-term portfolio projections, determine Laura's facility contribution, or draft her communication to co-sponsors" | TNA:20-22 |
| O7 | Notes "do not need to correspond to investments that remain in your portfolio" | TNA:25-26 |
| O8 | "The analysis should be consistent with the strategic approach your team is developing and will later articulate in its IPS." | TNA:30-31 |
| O9 | Wharton's example note has a role ("reduce portfolio volatility"), a benefit ("income and greater stability") and a stated risk ("although interest-rate changes may affect its value") | TNA:36-39 |
| O10 | "Include each Trading Note exactly as it appears in WInS." | TNA:44 |
| O11 | Reflection "100 words or fewer" on: why; how it "aligned with your overall investment strategy"; how it "supported the client's goals, funding needs, or risk considerations" | TNA:46-52 |
| O12 | "The Trading Notes must correspond to trades executed in WInS. Yes, we will verify this." | TNA:53 |
| O13 | A note should capture "the reasoning behind the decision, including its alignment with your strategy, the supporting research or analysis, and its expected role in growth, liquidity, risk management, or future funding" | Guide:84-86 |
| O14 | "Do not treat Trading Notes as an afterthought. They provide a record of how your team put its strategy into practice." | Guide:91-92 |
| O15 | "your investment decisions should already reflect a clear strategic approach" | Guide:89-90 |
| O16 | Not evaluated: "Your portfolio ranking"; "How many trades you make"; "Whether your portfolio makes money during the competition" | Guide:74-78 |
| O17 | Infographic: "Show how three investment decisions supported, tested, or refined the developing strategy." | Infographic:21-25 |
| O18 | "Evaluators will consider the three deliverables together ... maintaining a clear and consistent investment strategy across all three." | case:161-162 |
| O19 | Notes "should record the reasoning, research, and intended strategic role of each decision at the time it is made" | SMApply WInS page, live 21 Oct (`web/sm_wins.txt:35`) |
| O20 | "Each investment decision should have a clear purpose within that strategy." | `web/sm_wins.txt:29` |
| O21 | "Your Trading Notes Analysis, Investment Policy Statement and Final Report are evaluated." (live text, 21 Oct, unchanged from the 14 Oct snapshot apart from whitespace) | `web/sm_deliverables.txt:23`; `smapply_public_2026-10-14/deliverables.txt:27` |
| O22 | Criteria used for all three: Investment Strategy ("maintains consistency with the team's IPS"); Articulation ("clearly explains the team's research and decision-making process"); Creativity ("authentic team voice"; "meaningful reflection") | `deliverables.txt:55, 58, 59` |
| O23 | Public rules page: Trading Notes Analysis = "Document your team's decision-making process." | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ (`web/p_16670.txt:86`, modified 2026-09-08) |
| O24 | AI: "AI-generated work may not be submitted as your own"; included AI material "must be properly cited" | `web/p_16670.txt:112-114` |

Not found anywhere: a TNA points scale, a TNA-specific rubric, a judge's comment on 2026-27 TNAs, or the exact
SMApply form layout (whether the note and reflection go in separate fields: UNVERIFIED).

---

## 2. Past years: what Wharton asked for, year by year (the TNA's history)

| Year (client) | What was required | Source |
|---|---|---|
| 2015-16 | No notes deliverable. "We strongly recommend that each team keeps a non-graded weekly journal to record its new stock purchases and rationale." | OFFICIAL PDF, `2015/10/2015-2016-KWHS-Investment-Competition-Guidebook.Global-Regions.pdf` (oct16 cache line 125) |
| 2022-23 (Peter) | Rule: a Trading Note "that specifies the purpose of the trade and how it fits into the overall investment strategy must be included with each trade". Final Report p.4: "Choose three (3) Trading Notes ... reflect on how they contributed to or illuminated your understanding and design of your final strategy"; "Minimum/Maximum of one page" | OFFICIAL, https://globalyouth.wharton.upenn.edu/investment-competition/rules/ (`web/p_3774.txt:163`, 2022-23 block); https://globalyouth.wharton.upenn.edu/investment-competition/deliverables/ (`web/p_3768.txt:527-535`) |
| 2023-24 (Hilary) | Final Report p.3: "Choose two (2) Trading Notes ... one related to a stock and the other to an ETF ... Explain each note in 150 words or less." Notes "do not necessarily have to be for companies that you recommend" | OFFICIAL, `web/p_3768.txt:138-144` |
| 2024-25 (Ladi) | Same note rule, plus: "You will use trading notes in your Final Report." Section format NOT FOUND | OFFICIAL-COPY, Scribd 803759730 (`web/scribd_rules_roles_2024.txt:65-66`) |
| 2025-26 (Connor) | Week 8 email: "Trading Notes are essential as they clarify the purpose of each trade, how it aligns with your overall strategy, and the key risks involved ... required for the Trading Notes Analysis section of your Final Report" | OFFICIAL-COPY, https://www.scribd.com/document/974710424/25-26-Week-Eight-Email (`web/scribd_25-26_week8.txt:41-44`) |
| 2025-26 format | Three notes labelled ETF / Stock / Team Choice, about 100 words each. Seen in two unrelated team reports and in Caplet's own 2025-26 doc. The official instruction text is NOT FOUND | TEAM-DOC: `web` copy not kept; `oct20/pastwinners/scribd/980515751.txt:40-62`; `/home/user/caplet-investment/team/google_drive/2025_knox_wharton.md:90-108` |
| 2026-27 (Laura) | Separate deliverable, due 23 Oct (Week 4). Three notes of any type from executed trades, quoted exactly, 100-word reflections on three set points, checked against WInS | Section 1 |

Repeated official advice in the midterm and technical feedback PDFs (OFFICIAL; PDFs re-downloaded 21 Oct, hashes
match the 16 Oct copies):
- "We want to understand WHY you are making certain decisions" (2023-24, `Technical-Feedback-23-24.cached.txt:18`;
  the same in 2021-22 and 2022-23: `Midterm-Feedback.cached.txt:18`, `Technical-Feedback-22-23.cached.txt:17`).
  URL: https://globalyouth.wharton.upenn.edu/wp-content/uploads/2023/11/Technical-Feedback-23-24.pdf
- "make sure you are submitting detailed Trading Notes in WInS, documenting the decisions that you make based on your
  strategy" (2023-24 :82-84; 2022-23 :86-87; 2021-22 says only "keeping a journal", :86).
- "past performance is not an indication of future results" (2021-22 :45; 2022-23 :44).

Judging page, 2022-23 and 2023-24 ("A Few Things to Keep in Mind"; OFFICIAL,
https://globalyouth.wharton.upenn.edu/investment-competition/judging-and-evaluation/, `web/p_3778.txt:28-32`, modified 2024-06-03):
- "Excessive investing jargon doesn't necessarily dazzle the judges. Your report should reflect your team's voice."
- "Don't use precious space repeating known facts about your client and defining concepts."
- "Choose active language, illustrate with examples and make your report memorable."

**What changed in 2026-27 (comparison of the rows above):**

| Feature | 2022-23 to 2025-26 | 2026-27 | So what for Caplet (INFERENCE) |
|---|---|---|---|
| Where it sits | A section inside the Final Report | Its own deliverable, before the IPS | It is read as evidence of the strategy before the IPS fixes it. It must not contradict the IPS (O8, O18) |
| When written | After trading ended, looking back | Mid-trading, Week 4 | "Refined" and "tested" can only point to things that really happened by 23 Oct |
| Notes chosen | 3; then 2 (stock + ETF); then 3 (ETF / stock / team choice) | 3, any type | Bonds and bond ETFs are fine. Wharton's own example is a Treasury ETF (O9) |
| Length | One page; 150 words each (2023-24); about 100 (2025-26, TEAM-DOC) | 100 words or fewer each | Tighter than 2023-24 |
| Content test | "informed your understanding and design of your final strategy" | why + alignment + client goals, funding or risk; "supported, tested, or refined" | Three required points, each checkable. Missing one is a visible gap |
| Exact quoting | Implied | "exactly as it appears ... we will verify this" | A typo fix counts as a change. Copy from the WInS export, not a working copy (draft §D notes a "here"/"hear" mismatch) |
| Performance | "not determined by portfolio performance" | Said in the TNA itself (O5) plus the Guide list (O16) | Any gain or loss language works against the reflection |
| Scope fence | None | Reserve size, projections, facility contribution, co-sponsor text "not expected" (O6) | A reflection that sizes the reserve or the gift goes beyond the brief. It also locks numbers the Final Report may change |
| Official example note | None | Yes (O9: role, benefit, risk) | The example shows the expected depth: one sentence each |

---

## 3. Judge, staff and advisor comments that bear on notes or reflections

I found **no Wharton article in which a judge talks about trading notes by name** (I searched the WordPress site for
"trading note(s)", "trade notes", "trading notes analysis" and "reflection trading", and read every hit:
`web/s_*.json`). The closest comments, all OFFICIAL Wharton pages:

| Who (role) | Quote (30 words or fewer) | URL, date |
|---|---|---|
| Aberdeen credit analyst, 2025 finale judge | "What distinguished managers was clear thoughtfulness and reasoning behind all the decisions that they put together." | https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/ (1 May 2025; `web/x_finale2025.txt:145`) |
| 2025 semifinal judge (Covepoint Capital) | "one of the tendencies of people who are just starting out is to fall into this trap of hiding behind fancy terms and formulas" | same page, `:151` |
| Teacher advisor, "Tales from the 2023 Teams" | "If you do it in reverse, you'll find yourself questioning why your team ever made certain decisions." Also: "check to make sure each stock meets that strategy before you click 'buy'" | https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/ (6 Jun 2023; `web/x_tales.txt:141`) |
| 2023 champions' co-team leader (same article) | "less is more, and having an explainable strategy makes a lot more sense than going for so many different things at once" | same, `:138` |
| Same advisor, Essential Educator blog | "Why does your team want to buy this stock? Why not buy the competitor?"; "relating their investment decision to the potential client and a higher-level investment strategy is key" | https://globalyouth.wharton.upenn.edu/essential-educator-blog/the-essential-educator-10-tips-for-teaching-the-wharton-investment-competition/ (8 Sep 2021; `web/x_tips.txt:144`) |
| Same blog | "if they are buying stocks without checking 'does this stock align with our overall thesis and/or investment strategy?' they are probably flying blind" | `web/x_tips.txt:149` |
| Aberdeen judging lead, 2019 | "made sure they provided a good level of detail in their research process and their experience" | https://globalyouth.wharton.upenn.edu/news/2019-kwhs-investment-competition-finalists-ready-regionals/ (`web/n_6081.txt:10`) |

Third party, LOW reliability (not Wharton): a Young Founders Lab blog advises "Write notes as you trade ... far easier
than rebuilding your reasons later" (https://www.youngfounderslab.org/blog/wharton-global-high-school-investment-competition, `web/x_yfl.txt:106`).

---

## 4. Past examples found (reflection sections only)

Searches: the Wharton WordPress REST search; web search (Scribd, LinkedIn, Issuu, Teen Ink, school news, YouTube); and
the 20 Oct pack (`oct20/pastwinners/past_winners_deep.md` §1 lists every artefact). Results: **no 2026-27-format TNA
from any team is public, and no Top 10 or champion team's notes are public** (Wharton: "We do not release final
reports from previous winners", page 3782, FROM 20 Oct pack). Other 2026-27 teams' Laura Gao GitHub repos exist but
were deliberately **not opened** (plagiarism risk, `past_winners_deep.md` G2). YouTube transcripts stayed blocked
(captcha/429, 20 Oct). LinkedIn, Issuu and Teen Ink searches returned nothing relevant.

| # | Example | Year, result | What the team did in its notes or reflections | Good | Weak | Reliability |
|---|---|---|---|---|---|---|
| E1 | **Mochi Investments**, Final Report section "Trading Notes and Decision-Making Process" (Scribd 802841191; text `oct20/pastwinners/scribd/mochi.txt:62-82`) | 2023-24, **Top 50** (on Wharton's 2024 list, verified 20 Oct) | Quotes two notes exactly, one stock and one ETF as required: an early chip-stock note bought on momentum ("Semiconductors are doing very well right now"), then a late ETF note tied to its own targets ("equal spread across sectors"; "12% target in ESG"). It explains the change: a rubric and process built between the two | A true growth arc: a named mistake, then a rule. Exact quotes. The later note cites numbers from the strategy (target weights) | About 255 words as one block, not two 150-word pieces (format was loose and it still qualified). Self-praise ("adaptability and learning agility"). The client is not named in the section. Vague ending ("holistic understanding of the market dynamics") | Medium: real Top 50 report, Scribd preview read. But n = 1, the whole report was judged, the format was different, and why it qualified is not known |
| E2 | **The Sharks** (Scribd 978004509; `scribd/978004509.txt:57-90`) | 2025-26, not Top 50 | Each note is a home-made "P.R.E.D.A.T.O.R. score" plus revenue figures, then a paragraph on sector fit | Says each holding's sector role and the ETF's job ("diversification and risk mitigation") | First-person conviction ("I'm confident holding this"); jargon (Kelly Criterion, "Blue Ocean"); overclaim ("rendering competition irrelevant"); company stats in place of client needs | Medium (preview); qualification checked against Wharton's list |
| E3 | **Profit Gurus** (Scribd 980515751; `scribd/980515751.txt:40-62`) | 2025-26, not Top 50 | ETF / Stock / Team Choice, about 80 words each; **no note quoted** | Names the client's goal and date in each | Past returns as proof ("Historically ... consistent growth"); a false claim (the S&P fund gives "low volatility"); a stock-picking story. Each ends with a generic lesson ("This trade taught us how ..."). Says nothing about the 85% cash shown in the report | Medium |
| E4 | **Capstone Investments** (Scribd 813669963; `scribd/813669963.txt:36-56`) | 2024-25, not Top 50 | "Analysis of trades": three ETFs (gold, dividend, tech) described in turn | Links each to the doubling goal; admits gold adds little growth | Past returns as reasons ("past yearly return of 6%-8%", "around 10%", "approximately 13% in the last twenty years"); gold called "secure, low-risk"; no note text; no tested or refined decision | Medium |
| E5 | **Chennai Tuskers** (Scribd 883041552; `scribd/883041552.txt:62-76`) | 2023-24, not Top 50 | Two notes (Amazon; S&P 500 ETF), about 50 words each | Follows the stock + ETF split | No note quoted; vague ("valuable insights into broader market trends"); no client; no evidence | Medium |
| E6 | **Dynamites** (Scribd 942363888; `scribd/942363888.txt:45-58`) | 2023-24 (INFERENCE: the Hilary case and notes dated Oct 2023), not on any list | Quotes its WInS notes, which are wishes ("fly high to the sky"), then retells the purchase | Quoted exactly and dated | The notes have no strategy, so no reflection could rescue them. Price hopes in place of a role | Medium |
| E7 | **Caplet's own 2025-26 entry** (team doc, Section 3; `/home/user/caplet-investment/team/google_drive/2025_knox_wharton.md:90-108`) | 2025-26, not Top 50, no feedback (CLAUDE.md "Lessons") | ETF / Stock / Team Choice, about 93-100 words each; notes pasted as images | Each names a portfolio role ("Foundation holding") and the client's cash need ($10,000 distributions) | Theme language ("Renovation philosophy", "human infrastructure", "capex supercycle"); stat-heavy (beta 0.52, 3.1% yield); trades justified by sector stories. Ray's own lesson: "strategy packaging was over-complex for the insight" | High for the text (own file); the result's cause is unknown |

What the group shows (INFERENCE, weak sample: 1 qualifier against 6 others):

| Dimension | E1 (Top 50) | E2-E7 (not Top 50) |
|---|---|---|
| Note text quoted exactly | Yes, both | Rarely (E2 and E6 only; E7 as images) |
| Shows a decision that tested or refined the strategy | Yes: mistake, then rule | No (E4 admits a limit but changes nothing) |
| Ties the trade to a stated rule or number from the strategy | Yes (target weights) | Mostly sector or theme stories |
| Reason given | Process and rule | Past returns, company stats, conviction |
| Language | Plain, but self-praising | Jargon, home-made scores, slogans |

---

## 5. Synthesis: what strong reflections do (each item sourced)

Evidence strength: **A** = a direct 2026-27 instruction; **B** = repeated official advice from past years;
**C** = inferred from examples (weak sample).

| # | A strong reflection... | Evidence | Strength |
|---|---|---|---|
| S1 | Quotes the note exactly as WInS shows it, from an executed trade (not a cancelled order), with a matching ticker and date | O10, O12 | A |
| S2 | Answers all three required points in 100 words or fewer: why this decision; how it fits the overall strategy; which client goal, funding need or risk it serves | O11 | A |
| S3 | States the decision's **intended role** in plain words (growth, liquidity, risk management, future funding) and why this security fills it better than an alternative | O5, O13, O20; advisor "Why not buy the competitor?" | A / B |
| S4 | Shows at least one decision that **tested or refined** the strategy: what changed, when, and why, using only events that really happened | TNA:12, :29; O17; E1 | A / C |
| S5 | Names the risk or trade-off the decision accepts, and how it is managed | O9 (the example's "although ..."); 2025-26 email "key risks involved" | A / B |
| S6 | Makes the three picks read as **one strategy**, each with a different job, not three stand-alone stories | O4, O15; 2023 champions "explainable strategy" | A / B |
| S7 | Agrees with the IPS (same strategy name, same job for each holding, same order of priorities, same number basis) | O8, O18, O22 | A |
| S8 | Uses evidence or a check that came before the trade (research, a rule, a test) rather than past returns or price hopes | Guide:84-86; feedback "past performance is not an indication"; E3, E4, E6 | A / B |
| S9 | Avoids performance, ranking and "since we bought" talk | O5, O16 | A |
| S10 | Stays inside the scope fence: no reserve size, projections, facility amount or co-sponsor wording | O6 | A |
| S11 | Plain, active language in the students' own voice; no defined textbook terms; no home-made labels that need explaining | Judging page :28-32; 2025 judge "fancy terms and formulas"; O22 "authentic team voice"; O24; E2, E7 | A / B |
| S12 | Specific over generic: a named fact or number from the team's own work, not "this taught us the importance of diversification" | Judging page "illustrate with examples"; E3, E5 | B / C |
| S13 | Honest about limits (e.g. "the payout is not fixed") rather than promising certainty | O9; case's overpromising warning (CLAUDE.md, case p.3); E1 | A / C |

**Common failure modes** (with where each was seen):
1. Note not quoted, paraphrased, or "corrected" (E3, E4, E5, E7 as images). Under 2026-27 rules this risks failing the check (O10, O12).
2. Past returns or company statistics used as the reason (E2, E3, E4). Wharton has warned against this every year it published feedback.
3. Generic lesson endings ("this trade taught us ...") with no event behind them (E3, E5).
4. Jargon, home-made scores and themes (E2, E7). Judges call it "hiding behind fancy terms".
5. No client link, or the client named only as a slogan (E5, E6).
6. Three separate trade stories with no common strategy (E2-E5).
7. Claims of safety or certainty that are not true (E3 "low volatility"; E4 gold "low-risk").
8. Performance and gain or loss talk (O5, O16; the Guide lists it as not evaluated).
9. Going beyond scope: sizing the reserve or the gift in October (O6). Specific to 2026-27.
10. AI-written text submitted as the team's own (O24; 2025-26 team doc copy of the judging tips: "inauthenticity will be obvious", TEAM-DOC, `2025_knox_wharton.md:258`).

**How far to trust this checklist.** Items marked A restate Wharton's own 2026-27 words and are safe. Items B and C
are reasonable but unproven. No Top 50 TNA in the 2026-27 format exists to compare against, and Wharton gives no
feedback.

---

## 6. UNVERIFIED or not found

- The TNA's weight in the Top 50 cut. Deliverables say "evaluated"; the rules page names only the IPS and Final Reports (`p_16670.txt:100`).
- The SMApply TNA form layout (separate fields for note and reflection; whether formatting or images are kept).
- The official 2024-25 and 2025-26 instruction text for the Trading Notes section (only rule-page and email copies, plus team documents).
- Any judge, staff or webinar comment about trading notes specifically. None was found in Wharton news (2019-2026) or on the public pages.
- Any champion's or Top 10 team's notes. Not public. The two team videos found on 20 Oct (InvestIQ 2024, $tockSnipers 2025) are title-only; transcripts blocked.

## 7. Files saved (`SP/oct21/tna/research/web/`)
`p_3768.txt` (deliverables 2022-24), `p_3774.txt` (rules 2022-25), `p_3778.txt` (judging), `p_16648/16654/16670.txt`
(2026-27 main, FAQ, rules), `sm_*.txt` (public SMApply, 21 Oct), `x_finale2025.txt`, `x_tales.txt`, `x_tips.txt`,
`x_yfl.txt`, the feedback PDFs and their `*.cached.txt` text, `scribd_25-26_week8.txt`, `scribd_rules_roles_2024.txt`,
and the search results `s_*.json`. Scripts: `../wp2txt.py`, `../bing.py`, `../bsearch.sh`.
