# Caplet scoring sheet for 2026-27, and two AI-opinion scorings (20 Oct 2026)

> **Verified 20 Oct (`oct20/verify_rub_alt/verify_rub_alt.md`): quotes and arithmetic exact; scoring inconsistent in 6 lines.** CK3, CK5, IS4, PA3, PA4 and CP4 are scored below their own level descriptors; the "red flag = 0" rule is never applied (state a precedence rule, e.g. "a red flag caps a line at 1"). Four red flags tagged [OFF] are AI extensions (cash with no WInS home; "her other assets" (ambiguous, reads as outside money); taxes/legal/facility costs; "final range in the IPS") - re-tag [INF]. "Score CP2 0 for AI text" is this sheet's convention, not a Wharton rule. Corrected IPS content-only mean 4.7 (was 4.2), authorship-scored 4.4 (was 3.8): still below competent. No Wharton scoring sheet is published. There are 30 phrase lines (26 scored).


**Status.** AI-generated research by Claude Code for Team Caplet, Tue 20 Oct 2026 (work done 19 Oct 21:40-22:30 UTC).
It is not text to submit, and it contains no TNA, IPS or Final Report wording. **Every score in this file is AI
opinion.** Wharton has never published a scale, levels, weights or a scoring sheet. I searched its site database on
19 Oct for "feedback", "rubric", "judging", "midterm" and "evaluation" (section 1), and none exists. If the team uses
this sheet, log it in the AI-use record and later in the Final Report's Works Cited ("scoring sheet and AI-opinion
scores, 20 Oct").

**How to read the labels.**
- **[OFF]** = 2026-27 official Wharton text, quoted word for word.
- **[PAST]** = earlier official Wharton text (2021-22 to 2025-26), word for word.
- **[COPY]** = official Wharton text known only from a third-party copy (Scribd), not re-fetched today.
- **[JUDGE]** = a named judge quoted in Wharton's own news posts. These quotes were collected 16 Oct and not re-opened today.
- **[INF]** = my inference. **Every level descriptor (0-4) and every band is [INF]**, even when it is built on an
  official phrase.
- MODEL = output of an AI-built script, not a fact. UNVERIFIED = nobody has confirmed it.

**Citation short forms.**
- `S/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/`.
- `official/` = `/home/user/caplet-investment/competition/official/2026_27/`.

| Short form | File (line numbers from `cat -n`) |
|---|---|
| deliv:n | `official/smapply_public_2026-10-14/deliverables.txt` (criteria at :55-59, re-checked live 19 Oct 21:41 UTC, identical wording) |
| IPS:n / TNA:n / case:n / Guide:n | `official/2026_WGY_Investment_Policy-FINAL.txt` / `2026_WGY_Trading_Notes_Analysis-FINAL.txt` / `Laura_Gao_2026_Client_Profile.txt` / `2026_WGY_Investment_Competition_Guide.txt` |
| WP3778:n | `S/oct19/frprep/web/wp_3778_judging.txt` (text of WordPress page 3778; my 19 Oct 21:41 UTC JSON fetch, `S/oct20/rubric/web/wp_3778.json`, is byte-identical to the one it was made from) |
| WP3768:n | `S/oct19/frprep/web/wp_3768_deliverables.txt` (page 3768; my fetch differs from it only in one random spacer id, so the content is the same) |
| TF2324:n / TF2223:n / MF2122:n | `S/oct16/research/R2_pages/pdf/Technical-Feedback-23-24.txt` / `Technical-Feedback-22-23.txt` / `Midterm-Feedback.txt` (all three PDFs re-fetched 19 Oct and byte-identical) |
| RR:n | `S/oct20/rubric/web/wp_16670.txt` (2026 Rules & Roles page, WP modified 2026-09-08, fetched 19 Oct) |
| HOME:n | `S/oct20/rubric/web/wp_16648.txt` (2026 competition main page, fetched 19 Oct) |
| FAQ:n | `S/oct19/askwharton/web/faqs.txt` (live SMApply FAQ, 19 Oct; the copy that has the TIPS/STRIPS lines) |
| AIP:n | `S/oct19/askwharton/web/ai_policy.txt` (live AI policy page, 19 Oct) |
| NS2526:n | `S/oct16/research/R2_pages/pdf/25–26-Semifinalists-–-Next-Steps-FINAL.txt` |
| TG:n | `S/oct16/research/R2_pages/scribd_teacher_guide_928.txt` (2025 Teacher Guide, Scribd copy) [COPY] |
| KB § | `S/oct16/research/KB_what_wins.md` (16 Oct evidence pack) |
| U19 § | `S/oct19/out/Caplet_Update_19Oct2026.md` (fact-checked 19 Oct update) |
| KIT § / E-n / D-n | `S/oct19/ipskit/ips_writing_kit.md` (sections, error IDs, decision IDs) |
| TNAK | `S/oct19/tnakit/tna_fact_kits.md` |
| FRP § | `S/oct19/frprep/final_report_prep.md` |
| VIE:n | `S/oct19/verify/verify_ips_exemplars.md` |
| WNX:n | `/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` (WInS notes as copied 13 Oct) |
| LIVE | `S/oct19/ips/work/v5_accepted.txt` and `refl_accepted.txt` (accepted-only text of the live IPS Report Doc) |

The Doc's Drive `modifiedTime` was re-read at 19 Oct 21:45 UTC: still 2026-10-18T00:49:32Z, so LIVE is current.

---

## 0. Summary

1. **No Wharton scoring sheet exists.** The most faithful sheet possible is the five 2026-27 criterion sentences
   (deliv:55-59), split into their 26 phrases. For each phrase I have written level descriptors anchored to official
   text, plus red flags taken from Wharton's own past feedback. Five official pass/fail gates sit in front of it.
   The scale (0-4 per phrase, 0-10 per criterion) is mine.
2. **The live drafts, as they stand, fail a gate before any score applies.** The accepted IPS is 97% AI exemplar v11,
   and the reflections are 100% v11 and still carry "[AI]" (VIE:18, :22). Wharton: "You may not submit any work
   generated by an AI program as your own" (AIP:224). Scored on content alone, as if students had written them, the
   accepted IPS averages about 4.2/10 and the TNA about 4.5/10, below "competent". The design is better than the text:
   case breaches (outside money, "announce in 2031"), false statements about the notes, missing themes (0 uses of
   "flexibility", "responsible", "liquidity") and number overload pull it down.
3. **A best realistic student version** (every 19 Oct fix applied, every IPS-kit decision voted, students writing)
   scores about **7.3/10 on the IPS** (range 6.5-8.6) and **7.4/10 on the TNA** (6.1-8.1). That is the "strong" band
   on most lines and Top-50 contention, but not a safe place. The weakest criteria stay Client (7.1) and Creativity
   and Presentation (7.0), because 500 words leave little room beyond the case, and the core idea came from an AI
   council run.
4. **What separates that version from a finalist** is mostly outside the TNA and IPS:
   - a Final Report that turns every IPS rule into student-rebuilt projections, a credible co-sponsor excerpt and a
     true, dated experience story;
   - one insight that is visibly the team's own;
   - a semifinal (video plus four 250-word written answers) in which every student defends the numbers.
   Wharton says it looks for teams that "score exceptionally well on all five components" (FAQ:83). In this sheet that
   means level 4 on most phrases. The best realistic IPS reaches level 4 on none at its middle estimate.
5. **The single biggest lever is still authorship** (gate G5, line CP2). Then come the case-rule fixes (IS4, CK2-CK4,
   PA6) and the cross-document joints (IS6). None of these needs new analysis.

---

## 1. Sources fetched today, and what exists

| Source | URL | Fetched (UTC) | Status |
|---|---|---|---|
| Judging and Evaluation (WP page 3778) | https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages/3778 | 19 Oct 21:41 | 200; WP modified 2024-06-03; byte-identical to the 19 Oct 12:50 copy |
| Deliverables (WP page 3768) | https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages/3768 | 19 Oct 21:41 | 200; WP modified 2024-05-30; content identical (one spacer id differs) |
| 2023-24 Midterm Report Feedback | https://globalyouth.wharton.upenn.edu/wp-content/uploads/2023/11/Technical-Feedback-23-24.pdf | 19 Oct 21:41 | 200; sha256 df24632b…; identical to the 16 Oct copy |
| 2022-23 Midterm Report Feedback | …/uploads/2022/11/Technical-Feedback-22-23.pdf | 19 Oct 21:41 | 200; sha256 f2a89223…; identical |
| 2021-22 Midterm Report Feedback | …/uploads/2021/11/Midterm-Feedback.pdf | 19 Oct 21:41 | 200; sha256 6179cab4…; identical |
| SMApply Deliverables (2026-27 criteria) | https://wghsinvcomp.smapply.us/res/p/deliverables/ | 19 Oct 21:41 | 200; criteria wording identical to deliv:55-59 |
| 2026 Rules & Roles (WP 16670), main page (16648), FAQ (16654), old FAQ (3780) | wp-json/wp/v2/pages/{id} | 19 Oct 21:43 | 200; judging lines extracted to `S/oct20/rubric/web/wp_*.txt` |
| Site search of WP media and pages | wp-json/wp/v2/media?search=…, pages?search=… | 19 Oct 21:43-21:44 | Only the three feedback PDFs above and unrelated classroom rubrics. **No competition scoring rubric, level descriptors or weights are published.** |

Raw files and hashes: `S/oct20/rubric/web/`. Counting script: `S/oct20/rubric/tools/count_live.py`. Level table and
score calculator: `S/oct20/rubric/tools/levels.csv` and `score.py`. I re-ran each and re-checked every criterion score
by hand.

---

## 2. Official text: what Wharton has actually said

### 2a. This year's five criteria, verbatim [OFF] (deliv:55-59; live SMApply page 19 Oct)

- **Investment Strategy:** "Presents a clear and creative investment thesis; demonstrates disciplined planning across
  Laura's changing time horizons and cash-flow needs; uses appropriate diversification; and maintains consistency with
  the team's IPS."
- **Client Knowledge and Objectives:** "Tailors the strategy to Laura's circumstances, priorities, risk considerations,
  and residency goals; demonstrates a thoughtful understanding of the client; and presents recommendations that can
  earn her confidence."
- **Portfolio Analysis:** "Demonstrates understanding and effective use of investment concepts and tools; integrates
  quantitative and qualitative analysis; and uses reasonable assumptions and projections to evaluate funding
  reliability, the facility contribution, and financial flexibility under varying market outcomes."
- **Articulation of Competition Experience:** "Demonstrates teamwork, communication, and learning; clearly explains the
  team's research and decision-making process; and reflects meaningfully on the team's growth and response to
  challenges."
- **Creativity and Presentation:** "Presents a compelling, well-organized narrative in an authentic team voice; uses data
  effectively to support conclusions; demonstrates original thinking and meaningful reflection; and communicates Laura's
  potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors."

### 2b. Which deliverables are scored, and how they connect [OFF]

- "Your Trading Notes Analysis, Investment Policy Statement and Final Report are evaluated." (deliv:27)
- "Evaluators will consider the three deliverables together. Teams should use each deliverable for its intended purpose
  while maintaining a clear and consistent investment strategy across all three." (case:161-162)
- "The top 50 teams will be selected as semifinalists based on the strength of their Investment Policy Statement (IPS)
  and Final Reports." (RR:60). **The TNA is not named there.** [INF] The TNA probably counts mainly through consistency
  ("maintains consistency", deliv:55) and as evidence of decision-making. Its separate weight is UNVERIFIED.
- "We are looking for teams that score exceptionally well on all five components of the criteria" (FAQ:83). [INF]
  This implies roughly equal criteria and no tolerance for a weak one. No weights are published.
- "Teams are evaluated on how thoughtfully they develop, implement, evaluate, and communicate a cohesive investment
  strategy designed around the client's goals." (FAQ:85)
- "successful teams communicate their reasoning, assumptions, tradeoffs, and competition experience clearly and
  authentically." (FAQ:87)
- "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and tradeoffs
  behind those decisions." (Guide:183-184)
- "Teams are evaluated on the quality of their investment strategy, how well it aligns with their client's objectives,
  the strength of their research and analysis, and their ability to clearly communicate and defend their
  recommendations." (HOME:29)

### 2c. Deliverable-specific asks [OFF] (the levels in section 3 depend on these)

- **TNA:** "select three investment decisions that best illustrate your team's strategic thinking. Explain the reasoning
  behind each decision, how it aligned with, tested, or refined your overall investment strategy, and how it supported
  the client's goals, funding needs, or risk considerations" (TNA:11-13). "The focus should be on the quality of your
  reasoning and the intended role of each decision, not simply whether an investment gained or lost value" (TNA:15-16).
  Not expected yet: the reserve size, projections, the facility contribution or the co-sponsor text (TNA:20-22).
  "consistent with the strategic approach your team ... will later articulate in its IPS" (TNA:30-31). "exactly as it
  appears in WInS" and "Yes, we will verify this" (TNA:44, 53). The reflection limit is 100 words (TNA:46).
- **IPS:** what it must make clear (IPS:53-65); "Focus on the strategy and decision-making framework ... rather than
  describing individual investments or presenting detailed financial calculations" (IPS:51-52). Not expected: final
  reserve calculations, detailed projections, a final range, or the co-sponsor draft (IPS:68-70). It is "the official
  record" and cannot be revised (IPS:73-74). Format gate: IPS:82-83, 84-123.
- **Case requirements the Final Report will be scored against:** the reserve's size and composition, the certainty
  definition, how it was evaluated and the assumptions (case:94-99); a responsible contribution that does not commit all
  remaining assets (case:101-106); a dollar range plus a confidence statement, the effect of favourable and unfavourable
  outcomes, and protection of the payments (case:117-120); the co-sponsor draft (case:123-124); five bullets
  (case:134-145); assumptions (case:146-149).

### 2d. Past criteria, verbatim [PAST] (WP3778:15-23, the 2023-24 block, same text in 2022-23)

- "Investment strategy: contains a clear and creative strategy thesis; demonstrates mid-term and long-term investment
  thinking; portfolio is invested in at least as many sectors as there are team members."
- "Client knowledge and objectives: strategy is tailored uniquely to the client's financial goals; would win him/her over
  as a client."
- "Portfolio analysis: demonstrates clear understanding of new concepts and investment tools; uses both quantitative and
  qualitative analysis."
- "Articulation of competition experience: demonstrates good teamwork and communication; team clearly explains
  decision-making process and what they learned from the competition."
- "Creativity and presentation: compelling narrative and visually pleasing presentation of data; many creative elements;
  clearly presented with an authentic team voice."
- "A Few Things to Keep in Mind" (WP3778:27-31): "Excessive investing jargon doesn't necessarily dazzle the judges. Your
  report should reflect your team's voice." / "Don't use precious space repeating known facts about your client and
  defining concepts. However, it is okay to demonstrate that you understand your client beyond the case study." / "Keep
  your reader engaged. Choose active language, illustrate with examples and make your report memorable."
- Eligibility, 2023-24: "Teams that include prohibited securities in their final report are not eligible for the
  Semifinals" (WP3778:41). A report must be "within the acceptable page range" and include "all the required elements"
  (WP3778:43).
- No individual feedback, and no information on how evaluators scored (WP3778:49; same today, FAQ:82).

**What changed this year, phrase by phrase** [INF; the comparison is mine]:

| Criterion | Dropped since 2023-24 | Added in 2026-27 | What it means for scoring |
|---|---|---|---|
| Strategy | sector count | "disciplined planning across ... time horizons and cash-flow needs"; "appropriate diversification"; "consistency with the team's IPS" | Rules by date, and joints across documents, are now scored directly |
| Client | "uniquely"; "win him/her over" | "circumstances, priorities, risk considerations, and residency goals"; "earn her confidence" | Four named sub-targets; credibility over persuasion |
| Analysis | "new concepts" | "effective use"; "integrates"; "reasonable assumptions and projections ... funding reliability, the facility contribution, and financial flexibility under varying market outcomes" | The largest change: projections under good and bad outcomes, on three named targets |
| Articulation | "what they learned" (kept as "learning") | "research"; "reflects meaningfully on the team's growth and response to challenges" | Challenges and growth must be shown, not just listed |
| Creativity | "visually pleasing"; "many creative elements" | "uses data effectively"; "original thinking and meaningful reflection"; the co-sponsor sentence | Credibility and data, not decoration; "authentic team voice" is kept |

### 2e. Wharton's own written feedback to teams [PAST] (the closest thing to level descriptors)

From the 2021-22, 2022-23 and 2023-24 Midterm Report Feedback PDFs (all re-fetched 19 Oct, unchanged):
- "Teams are qualifying 'buy low and sell high' as an investment strategy as well as, 'invest in growth markets.' These
  are NOT investment strategies." (TF2324:9-10)
- "tools like Porter's Five Forces help you evaluate your choices, but on their own they are not a team strategy. Your
  strategy is a set of rules and guidelines; a plan of attack." (TF2324:13-14)
- "Will certain triggers dictate whether you buy or sell a security? ... a strategic thread? We want to understand WHY
  you are making certain decisions" (TF2324:16-18)
- "The most unique team strategies for this competition combine both strategic and creative thinking." (TF2324:20-21)
- "she likely will not want to sit through long, meandering strategy explanations. Find ways to convey your team
  strategy strongly, creatively and succinctly." (TF2324:24-25)
- "Your strategy should incorporate your potential client's objectives and risk tolerance. The construction of your
  portfolios should foremost be driven by these two variables." (TF2324:27-28)
- "If holding a lot of cash is part of your investment strategy, then you should outline why you are doing so."
  (TF2324:37-38)
- "past performance is not an indication of future results" (TF2324:43)
- "young investors make the mistake that researching, evaluating and ultimately investing ... are driven solely by
  quantitative analysis" (TF2324:47-48)
- "How will you articulate your process? ... What steps in your process come before others and what is the sequence?
  How stringent is your analytical process ...?" (TF2324:76-80)
- "consider keeping a journal of all your team's activities ... and make sure you are submitting detailed Trading Notes
  in WInS, documenting the decisions that you make based on your strategy." (TF2324:82-84)
- Closing: "If you have taken the time to understand your client's objectives, develop a strategy or plan of attack, and
  apply that strategy, plus analysis, when making investment decisions, you are on the right track." (TF2324:86-88)
- The 2021-22 and 2022-23 versions say the same in near-identical words (MF2122:10-21; TF2223:9-20). They also add
  "building out from the client case study" and "a theme" (TF2223:13, :17).

From the Teacher Guide's "Feedback for Competing Students" [COPY] (TG:266-311). These are the questions Wharton tells
advisors to ask, and they are the nearest thing to a published checklist:
- "articulate a clear and creative investment strategy thesis that for the most part makes sense for their client?"
- "research the client deeply and beyond the case study?" / "tailor their strategy uniquely to the client's short-term
  and long-term goals?" (TG:295-296)
- "use both quantitative and qualitative analysis?" (TG:302)
- "reflect on challenges and articulate what they learned and how they prevailed?" (TG:306)
- "an authentic team voice? In other words, they don't try to 'sound' smart, but convey a certain ease and comfort
  level with the material they've learned." (TG:310-311)

### 2f. Semifinal (decides the 10 finalists) [PAST] (2025-26; this year's format is UNVERIFIED)

- Judged on the five criteria plus "Written Responses" (NS2526:128-135).
- "judges will evaluate presentations based on clarity, coherence, storytelling, and alignment with the team's written
  reports" (NS2526:34-36).
- "Do NOT introduce completely new material, or your team will be disqualified." (NS2526:49)
- "Every team member must have a speaking role and briefly explain how they contributed value to the team."
  (NS2526:42-43)
- "We are looking for your authentic team voice, not generated or generic responses." (NS2526:111-112)
- 2026-27 says only "a short presentation ... All team members must participate" (FAQ:93).

### 2g. Integrity rules [OFF] (they act as a gate, section 3a)

- "You may not submit any work generated by an AI program as your own." "If you use AI to assist you in any way during
  the competition, how you use it must be recorded in your Works Cited pages." (AIP:224)
- "AI-generated work may not be submitted as your own." (RR:66)
- Teams must not "fabricate analyses, invent teamwork and experiential stories ... pass AI generated writing or work off
  as your own" (AIP:220).
- "When students express themselves ... they must use their voice and words." (AIP:208)
- Wharton "reserves the right to engage ... forensic analysts" (AIP:222).

---

## 3. The scoring sheet (faithful to the official phrases; levels and bands are [INF])

### 3a. Gates: pass or fail before any score

Failing any gate means the scores below do not matter.

| Gate | Test | Source | Applies to |
|---|---|---|---|
| G1 Time | Submitted by 5:00 pm ET; "We will not grant any deadline extensions" | deliv:29 | All |
| G2 Format (IPS) | 1-page title page with the roster team name, names as "First Name, Last Initial" and the WInS username; pitch at most 50 words and IPS at most 500, within 2 pages; TNR 12, double-spaced, 1-inch margins; PDF at most 5 MB; no graphics, links, footnotes or citations. "Submissions that do not meet the requirements below will not be considered for semifinal selection" | IPS:82-123 | IPS |
| G3 Notes (TNA) | Three notes from executed trades, each "exactly as it appears in WInS" ("we will verify this"); each reflection at most 100 words | TNA:42-53 | TNA |
| G4 Securities | Laura's plan and WInS hold only WInS-listed stocks, ETFs and Government/Treasury bonds; TIPS and STRIPS "NOT permitted"; "for BOTH contributions, the IPS and Final Report" | FAQ:44-55; past precedent WP3778:41 | IPS, FR |
| G5 Authorship | Every submitted sentence is the students' own; AI use is recorded (in the Works Cited for the FR; where to record it for the TNA and IPS is UNVERIFIED, U19 §9 Q1); no invented stories | AIP:208, 220, 224; RR:66 | All |

[INF] How Wharton treats a G5 breach is not published beyond "dealt with severely" (AIP:224). Treat it as fatal. Even a
non-fatal outcome would leave CP2 (authentic voice) at 0.

### 3b. Scale [INF]

- **Phrase level (0-4):**
  - 0 = absent, wrong, or a red flag present;
  - 1 = weak (asserted, decorative or partly wrong);
  - 2 = competent (present and mostly correct, the typical finisher);
  - 3 = strong (complete, true, tied to Laura, consistent: the standard a Top-50 entry probably needs);
  - 4 = exceptional (as 3, plus depth or originality few entries show: finalist standard).
- **Criterion score (0-10)** = 2.5 × the mean of the phrase levels scored for that deliverable. Lines marked "N/E" (not
  expected in that deliverable, from 2c) are left out.
- **Bands:**

  | Criterion score | Band |
  |---|---|
  | under 5 | below competent |
  | 5-7.4 | competent |
  | 7.5-8.9 | strong (Top-50 contention) |
  | 9-10 | exceptional |

- **Calibration** [INF]: the Top 50 was 49 of about 2,339 final reports in 2025-26, or 2.1% (KB §1.1). "Score
  exceptionally well on all five components" (FAQ:83), so a likely Top-50 IPS + Final Report averages 8 or more with no
  criterion under 7.5. Finalists are chosen at the semifinal, so paper alone does not decide them.
- **Deliverables:** T = TNA, I = IPS, F = Final Report. Each line says where the phrase can be shown.

### 3c. Investment Strategy (deliv:55)

| ID | Official phrase | Shown in | 1 looks like | 2 looks like | 3 looks like | 4 looks like |
|---|---|---|---|---|---|---|
| IS1 | "clear ... investment thesis" | T, I, F | A label or aim ("balanced growth"), or a tool presented as the strategy | Central idea stated, but late, or only *what* is bought without *why* it serves Laura, or it contains an untrue claim | In the pitch and the first two IPS sentences; one name; what it does and why only this works for her (the portfolio alone must fund the payments, case:91-92); true; a cold reader can repeat it | As 3, and every later rule visibly follows from it; the TNA, IPS and FR reuse it unchanged |
| IS2 | "creative" | I, F | A theme or metaphor that decorates | A sound but standard design stated as a formula | A design choice that comes from this client's own problem (a range in 2031 before the 2033 money exists; fixed nominal payments), explained as a mechanism | An idea few entries have, plainly the team's own, that resolves a stated tension (credibility vs flexibility) and survives the team's own tests |
| IS3 | "disciplined planning across Laura's changing time horizons" | T, I, F | Dates listed with no rules | Rules for most dates; gaps (after 2033; a late or small 2028 deposit) | A rule and its trigger for Jan 2027, Jan 2028, each January review, 2031, Jan 2033 and 2033-42, including the two likeliest events (ladder over $300k; a late or small deposit) | As 3, plus the FR shows each rule applied and logs decisions not to trade |
| IS4 | "... and cash-flow needs" | T, I, F | "Safe assets" in vague terms | Payments matched, but timing gaps or reinvestment unstated, or a cover step from outside the portfolio | Each payment's money is there by its 1 January; where waiting money sits (a WInS-listed fund type); coupon-reinvestment risk named with what covers it; every cover step inside the portfolio (case:91-92) | As 3, plus sized and stress-tested in the FR on one named basis |
| IS5 | "uses appropriate diversification" | T, I, F | Asserted only, or the old sector-count idea | Treasuries plus a broad equity fund stated | Diversification by funding purpose; the single issuer stated as deliberate, with its residual risk named; one broad, cheap growth fund | As 3, plus alternatives weighed (more equity, other bonds, TIPS excluded by rule) and the WInS label quirk explained (FR) |
| IS6 | "maintains consistency with the team's IPS" (and, by case:161-162, across all three) | T, I, F | Several contradictions (the equity's job, the shortfall order, figures on different bases) | Minor drift in wording or numbers | A joints check passes: one name, one floor definition, one shortfall order, one job list for VT, one number basis, one WInS-scale statement; notes, reflections and IPS agree | As 3, and the FR evaluates implementation against each IPS rule explicitly |

**Red flags:**
- "buy low and sell high" or "invest in growth markets" offered as a strategy [PAST TF2324:9-10];
- a tool (Porter, SWOT) presented as the strategy [PAST TF2324:13-14];
- the strategy "buried somewhere ... rather than clearly stated ... up front" [PAST, guidebook c.2020, KB §4.1];
- "long, meandering strategy explanations" [PAST TF2324:24];
- strategy changes after 6 Nov presented as the plan [OFF IPS:73-74; Guide:156-159];
- uninvested cash in Laura's plan with no WInS-listed home [OFF FAQ:44-55; PAST TF2324:37-38];
- any TIPS or STRIPS in the plan [OFF FAQ:54-55].

### 3d. Client Knowledge and Objectives (deliv:56)

| ID | Official phrase | Shown in | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| CK1 | "Tailors the strategy to Laura's circumstances" | T, I, F | Case facts restated with no link to the design | One or two fact-to-design links | Each key fact drives a choice: living costs covered outside (case:61-63) → risk capacity; 2028 deposit from ventures (case:43-45) → the 2027 deposit sized for the payments; no flows before 2033 (case:64-65) → hold | As 3, plus links most entries miss, each sourced, none invented |
| CK2 | "priorities" | T, I, F | Growth first, or the payments treated as one goal among many | Payments first; the rest vague | Explicit order: payments with a high degree of certainty; then a *responsible* contribution; then *flexibility* (case:91, 101-106), each with its rule | As 3, plus it shows what gives way first under stress |
| CK3 | "risk considerations" | T, I, F | Risk tolerance as a label ("moderate") | Capacity or willingness, not both | Willingness ("thoughtful risks", "appropriate balance", case:69-74) and capacity, goal by goal; the 2028 deposit's dependence on her income | As 3, plus how Laura is likely to react in a downturn and why the rules stop a panic sale [JUDGE 2024, KB §4.2] |
| CK4 | "residency goals" | (T), I, F | Taiwan mentioned as decoration | Payments linked to the residency | The facility, "reliable support for its early operations" (case:83) and 2031 credibility with co-sponsors (case:110-116), each tied to a specific rule | As 3, plus sourced Taiwan context (currency, how local funders work) used in a decision (FR) |
| CK5 | "demonstrates a thoughtful understanding of the client" | I, F | Invented traits, or quotes put in Laura's mouth | Case read closely; nothing invented | One or two sourced facts beyond the case that change a choice ("it is okay to demonstrate that you understand your client beyond the case study", WP3778:29) | Deep, sourced, and shaping the recommendation; the human side included because it matters, not as padding [JUDGE 2025, KB §4.1] |
| CK6 | "presents recommendations that can earn her confidence" | I, F | "Guaranteed", "cannot miss" | Clear but with trade-offs unstated | Recommendations Laura could check herself; trade-offs and residual risks stated honestly; no absolutes | As 3, plus an alternatives table and a recommendation she could defend to co-sponsors (FR) |

**Red flags:**
- relying on co-sponsors, grants or "other outside funding" for the payments, including "her other assets" [OFF case:91-92];
- committing all remaining assets [OFF case:102-103];
- "Don't use precious space repeating known facts about your client" [PAST WP3778:29];
- Laura "quotes" (the pull quote, case:31-33, is the case's words);
- claims about her the case does not make (KIT E31);
- taxes, Taiwan legal requirements or facility-cost estimates [OFF case:164-169: not expected].

### 3e. Portfolio Analysis (deliv:57)

| ID | Official phrase | Shown in | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| PA1 | "understanding and effective use of investment concepts and tools" | T, I, F | Tools that do not fit this problem (DCF, Sharpe); misused terms | Right concepts, some errors (a non sequitur, "covered at purchase") | Cash-flow matching, rate sensitivity, reinvestment risk, defined-maturity fund payouts and scenario or Monte Carlo methods used correctly and in plain words | As 3, and each student explains each tool without notes; each tool answers one named client question |
| PA2 | "integrates quantitative and qualitative analysis" | T, I, F | Numbers only, or words only | Some pairing | Each number tied to a judgement (credibility, Taiwan costs, income risk) | The judgement visibly changes a decision |
| PA3 | "reasonable assumptions" | I, F | One assumption with no basis | Several, undated or on mixed bases | Return, inflation, cash-flow timing, outside funding (none) and flexibility assumptions named (case:146-148), sourced and dated, on one basis | As 3, plus sensitivity to each key assumption (FR) |
| PA4 | "projections to evaluate funding reliability" | I (words), F | "Safe" asserted; "guaranteed" | A definition with no method, or a circular one | One certainty standard; how it was tested (method type, scenarios); the assumptions; what absorbs each remaining risk (case:96-99) | As 3, rebuilt by students; model and history agree; each figure stated with its meaning |
| PA5 | "... the facility contribution" | I (rule), F | One exact number | A range with no confidence, or one that does not protect the payments | IPS: the rule. FR: range + confidence + what good and bad markets do + protection of the payments (case:117-120) | As 3, plus a re-quote rule and the currency risk |
| PA6 | "... and financial flexibility" | I, F | Mentioned only | An amount kept with no purpose | What she keeps, why, where it is held, and its trade-off with the contribution | As 3, plus tested in bad cases |
| PA7 | "under varying market outcomes" | I (words), F | One forecast | One stress test | Named favourable, middle and unfavourable cases with every input listed, including rates falling for good (coupon reinvestment), an equity fall before 2031/2033, inflation and the currency | As 3, plus history windows and a joint stress (stocks and yields falling together) |

**Red flags:**
- adding WInS gains or losses to Laura's projections [OFF case:132-133; Guide:70-73];
- "past performance is not an indication of future results" [PAST TF2324:43];
- quantitative analysis only [PAST TF2324:47-48];
- detailed calculations or the final range in the IPS [OFF IPS:51-52, 68-70];
- a figure with no date or basis;
- two different "99%"s;
- "in our simulations" with no model named (KIT E18-E19);
- jargon: "Excessive investing jargon doesn't necessarily dazzle the judges" [PAST WP3778:27]; "hiding behind fancy terms and formulas" [JUDGE 2025, KB §4.2].

### 3f. Articulation of Competition Experience (deliv:58; mostly the FR; the TNA shows AR3 and AR5)

| ID | Official phrase | Shown in | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| AR1 | "teamwork, communication, and learning" | F | "We worked well together" | Roles listed | Who owned what, how disagreements were settled, how the team worked across time zones, what each student learned: all true and dated | As 3, with specific moments; every student can speak to it (semifinal, NS2526:42-43) |
| AR2 | "clearly explains the team's research ... process" | F | Sources listed | Process described | What was checked against primary sources, and what changed because of it; AI's role stated honestly | As 3, plus research that misled the team and how it was caught |
| AR3 | "... and decision-making process" | T, F | Outcomes only | Reasons given | Options, evidence, who argued what, the vote and the date. In the TNA: why this trade, in this form, at that time | As 3, plus decisions *not* to trade shown as discipline |
| AR4 | "reflects meaningfully on the team's growth" | F | Platitudes | One change named | Before and after, with the cause (last year's lessons → this year's checks; first plan → final plan) | As 3, plus what the team would do differently, without redesigning the plan (Guide:156-159) |
| AR5 | "... and response to challenges" | T, F | A complaint | A challenge named | Challenge → response → result (for example, the 6 Oct WInS-only rule moved the floor to IBTM) | As 3, plus the lesson applied again later |

**Red flags:**
- invented teamwork or experience stories [OFF AIP:220];
- an advisor shown making decisions;
- stories found only in AI files;
- no journal [PAST TF2324:82-84].

### 3g. Creativity and Presentation (deliv:59)

| ID | Official phrase | Shown in | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| CP1 | "compelling, well-organized narrative" | T, I, F | Lists | Organised but dense | One storyline (problem, idea, proof, trade-off); each paragraph has one job; a cold reader can follow it | Memorable, active language and examples (WP3778:31) |
| CP2 | "in an authentic team voice" | T, I, F | Jargon, "sounding smart" (TG:310-311) | The students' words, but stilted | The students' own words; every author can defend every sentence | As 3, with "a certain ease and comfort level with the material" (TG:311) |
| CP3 | "uses data effectively to support conclusions" | T, I, F | Numbers dumped or undated | Useful numbers, some stale or on mixed bases | Few numbers, each dated with its basis, each supporting a conclusion; in the FR, each chart answers one client question | As 3, plus visuals a non-investor reads in seconds (FR) |
| CP4 | "demonstrates original thinking" | T, I, F | A decorative theme | Sound but conventional; or original but not the team's (AI-originated, uncredited) | An insight the team can show is its own (through its votes and reasoning), with AI help credited | An insight judges rarely see, and it works |
| CP5 | "and meaningful reflection" | (T), F | Generic | One lesson | Specific lessons tied to events | Lessons that changed later behaviour |
| CP6 | "communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors" | I (principle), F | One exact promise; overpromising (case:114-116) | A range with no confidence, or nothing on what moves it | A firm bottom and a "can reach" top with its chance beside it; a valuation date; the currency; nothing that endangers the payments | As 3, written so that a co-sponsor would trust it: plain, honest about uncertainty, and matching the numbers |

Score CP2 as 0 for any text generated by AI.

**Red flags:**
- AI-generated or "generic responses" [OFF AIP:224; PAST NS2526:111-112];
- slogans in place of reasoning;
- leftover drafting instructions;
- "many creative elements" pursued as a goal (dropped from the criterion this year) [INF];
- charts, images or links in the IPS [OFF IPS:123].

### 3h. How each deliverable is scored (from 2c)

- **TNA:** IS1, IS3-IS6, CK1-CK3, PA1-PA2, AR3, AR5, CP1-CP4. The rest are N/E (TNA:20-22). CK4 is credited only if a
  reflection uses it.
- **IPS:** IS1-IS6, CK1-CK6, PA1-PA7 (PA4, PA5 and PA7 as principles in words), CP1-CP4 and CP6 (as a principle).
  AR1-AR5 and CP5 are N/E. The IPS brief never asks for the team's experience, though the design can show AR5.
- **Final Report:** every line.

Two students score separately, then compare. An outside reader gives scores and questions, never wording. AI checks come
only after the students' scores (KIT §7; U19 §3b item 8).

**How this relates to KIT §7.** It keeps KIT §7's 21 lines, splits some (IS3/IS4, PA4-PA7), adds level descriptors, red
flags, gates and the TNA and FR columns, and changes the scale from 0-2 to 0-4. The two can be used together.

---

## 4. Score (a): the current live drafts, accepted text only (AI opinion)

**What was scored.**
- LIVE accepted text (the Doc is unchanged since 18 Oct 00:49:32 UTC): pitch 31 words, IPS body 453 (456 with the
  heading); reflections VT 87, IBTR 92 and IBTM 88 words without the "[AI]" tag. I re-counted all of these with
  `S/oct20/rubric/tools/count_live.py`, and they match VIE:41.
- The three executed WInS notes as quoted at WNX:14, :15 and :19.
- Pending v12 suggestions are left out, as asked.

### 4a. Gates, as the drafts stand today

| Gate | IPS | TNA |
|---|---|---|
| G2 Format | **FAIL as exported today.** The PDF prints the pending wording too: about 77 + 939 words over 4 pages (U19 §3a item 2). With the suggestions rejected, the length passes (31 ≤ 50; 456 ≤ 500), but the page still shows "[AI]", the tab title and the meta-line "Name the residual risks." | n/a |
| G3 Notes | n/a | Passes if the right note is pasted; the cancelled IBTR note is the same length as the VT note (U19 §3a item 10) |
| G4 Securities | Passes (no TIPS or STRIPS named) | Passes |
| G5 Authorship | **FAIL.** The accepted body is 97% AI exemplar v11, and no sentence lacks a v11 counterpart (VIE:18-20) | **FAIL.** Word for word v11, still tagged "[AI]" (VIE:22) |

**As-submitted verdict (AI opinion):** not scoreable. There is a material risk of removal under AIP:224 and RR:66.
Stripping the "[AI]" tag would turn a disclosed problem into "pass[ing] AI generated writing ... off as your own"
(AIP:220).

### 4b. Diagnostic: what the same content would score if students had written it

This shows where the ideas and the wording lose marks, so that a fresh student draft avoids the same losses. Short
quotes appear only to name each error.

**IPS (LIVE accepted text):**

| Line | Level | Evidence |
|---|---|---|
| IS1 | 2 | The pitch says what is bought ("the ten operating payments first in Treasuries, then a Treasury floor ... One global equity fund grows the rest") but not why it serves her goals (IPS:35-36). "Promise only what is owned" is untrue: the floor is bought in Jan 2028 and its payout is not fixed (KIT E12) |
| IS2 | 2 | Floor plus a share of the fund, capped, is a real mechanism, but it is stated as a formula. "Root-and-Branch, echoing her memoir" decorates rather than explains |
| IS3 | 2 | Rules exist for 2027, 2028, 2031 and 2033. "with the floor used last" cannot work after 2033, when the floor has been given away (E11). No rule for a late or small 2028 deposit |
| IS4 | 1 | "Maturing bonds, not sales, supply every payment" is false for 2038 and 2039: the notes park proceeds in a short-term Treasury ETF (WNX:16-17). "maturing shortly before it" hides 10.5- and 7.5-month gaps. A reinvestment shortfall is "covered by her other assets", which is outside money (case:91-92) |
| IS5 | 2 | "Concentration in one issuer is deliberate" is good. "the least credit risk of any dollar asset" is absolute and unsourced (E13) |
| IS6 | 1 | The VT note says stocks "only set how far her gift rises" (WNX:14), while the IPS gives the equity a backstop job too. The parking contradiction above. "the 2027 deposit alone is sized for the payments" sits uneasily beside the IBTR note's top-up rule (E39) |
| CK1 | 3 | The best client line: the 2028 deposit depends on publishing and speaking income, so the 2027 deposit is sized for the payments; other income covers living costs |
| CK2 | 2 | A primary and a secondary objective are stated. Flexibility is not an objective ("flexibility" 0 times; the case uses it 5 times, VIE:45) |
| CK3 | 1 | Capacity only. Willingness ("thoughtful risks") was cut (VIE:44) |
| CK4 | 1 | "residency" appears once. "a facility contribution Laura can announce in 2031" misreads the case: in 2031 she gives a range, and the contribution comes in 2033 (case:109-117; E7) |
| CK5 | 1 | Nothing beyond the case; the memoir link is decoration |
| CK6 | 2 | Residual risks are named, which helps. But "No payment changes" sits beside an admitted $21,000 shortfall (E15), and the cover from "her other assets" would not earn trust |
| PA1 | 2 | Matching, rate sensitivity and reinvestment risk are used. "Treasuries currently yield about 5.15%, so we buy now rather than wait" does not follow: the money arrives in January whatever the yield (E2) |
| PA2 | 2 | Some pairing of numbers with judgement |
| PA3 | 1 | A 7% equity return is stated; "5.15%" is an undated model ladder yield (VIE:74); no basis, no inflation assumption for the projections |
| PA4 | 1 | The certainty definition rests on outside money; "simulated paths" names no method (E18) |
| PA5 | 2 | A bound rule exists, but "less any expected payment shortfall her half cannot cover" is hard to follow (E27), and "three of four simulated paths" is a figure the IPS need not give (IPS:68-69) |
| PA6 | 1 | "flexibility" 0 times; Laura's kept half is implied, not explained |
| PA7 | 2 | Named stresses: a 40% equity fall in 2032, a two-point rate fall, inflation, a stronger Taiwan dollar |
| CP1 | 2 | Principle headings give structure, but the meta-line "Name the residual risks." and the slogan close "We decline that trade." remain |
| CP2 | **0** | AI text (G5) |
| CP3 | 1 | 10 dollar or percentage figures in 453 words (my count, matching VIE:72), several undated; this is against IPS:51-52 |
| CP4 | 1 | The core idea came from an AI council run (FRP §8 S1), and the wording is the exemplar's |
| CP6 | 2 | "floor, rounded down because a fund's payout is not fixed" is credible; the upper-bound wording is not |

**TNA (LIVE accepted reflections plus the fixed notes):**

| Line | Level | Evidence |
|---|---|---|
| IS1 | 2 | Payments, floor and growth all appear, but no reflection states the thesis |
| IS3 | 2 | The IBTR top-up rule for Jan 2027; IBTM's December 2032 timing |
| IS4 | 2 | IBTM "also funds her first $50,000 payment". "The minimum she quotes is one she already owns" overclaims: in Laura's plan IBTM is bought in 2028 and its payout is not fixed |
| IS5 | 2 | VT's breadth and cost. "avoids concentrating in any industry her income already depends on" is a reason no note records (E22) |
| IS6 | 1 | "VT decides one thing only" against the IPS's two jobs (E17); "We bought the ladder from 2042 backwards" is only half true of the timestamps (VIE:68); "This note first warned of a 0.3-point fall" is false: 0.3 was in the cancelled order's note (VIE:69) |
| CK1 | 1 | Little of Laura's circumstances, apart from the unrecorded industry reason |
| CK2 | 2 | "the facility floor, not the payments, absorbs the difference" shows the order |
| CK3 | 2 | Rate risk and an unfixed payout are named |
| PA1 | 2 | Correct concepts, but "$292,000 to $298,000" mixes two bases (U19 §6a) |
| PA2 | 2 | Some pairing |
| AR3 | 1 | "We did not trade. The policy already answers the risk." is a good decision record, but the 0.3-to-0.2 story attached to it is AI-inferred and false as written |
| AR5 | 2 | The 6 Oct WInS-only rule moved the floor to IBTM: real (CLAUDE.md, current status). "refined" depends on the email's arrival time (UNVERIFIED, U19 §3a item 6). "the zero-coupon Treasury we had planned" is unconfirmed (E22) |
| CP1 | 2 | Tight, but each reflection reads as a slogan chain |
| CP2 | **0** | AI text, tagged |
| CP3 | 2 | Specific figures, one on mixed bases |
| CP4 | 1 | As for the IPS |

**Strength the drafts already have:** the WInS notes themselves are specific, dated and purpose-tagged ("Future
funding", "Growth"), and each states a role and a limit ("Its payout is not fixed"). They meet the Guide's ask that a
note capture "its expected role in growth, liquidity, risk management, or future funding" (Guide:84-86). The notes, not
the reflections, are the best thing in the TNA.

### 4c. Scores (a) (AI opinion; 0-10 per criterion)

| Deliverable | Strategy | Client | Analysis | Articulation | Creativity & Presentation | Mean of scored |
|---|---|---|---|---|---|---|
| IPS, with authorship scored (CP2 = 0) | 4.2 | 4.2 | 3.9 | N/E | 3.0 | **3.8** |
| IPS, content only (CP2 left out, CP4 at 2) | 4.2 | 4.2 | 3.9 | N/E | 4.4 | **4.2** |
| TNA, with authorship scored | 4.5 | 4.2 | 5.0 | 3.8 | 3.1 | **4.1** |
| TNA, content only | 4.5 | 4.2 | 5.0 | 3.8 | 5.0 | **4.5** |

**Why this is lower than the 19 Oct mock judges** (who gave the IPS Strategy 8/8/7, Client 6/6/6 and Analysis 7/7/6,
`S/oct19/judges/findings.md:40-91`):
- The mock judges scored holistically and assumed the text was cleaned up. This sheet scores each official phrase and
  puts a 0 or 1 wherever a case rule is broken (outside money, IS4/CK6/PA4) or the documents contradict each other
  (IS6).
- Both readings are AI opinion. Both agree the design is better than the text, and that the weak criteria are Client and
  Creativity.

[INF] Against the field, the design idea would probably beat a typical finisher's "balanced growth" strategy. The
written text is what pulls it into the "below competent" band.

---

## 5. Score (b): a hypothetical "best realistic" student version (AI opinion)

### 5a. What is assumed done

Everything below is a fix already specified in U19 §3a-3b and KIT §1-§5. Nothing here is drafted wording.
1. **G5 met.** Students write every word, with the exemplars, the [AI] Doc text and AI chat closed (U19 §3a items 2-4;
   §3b item 6). The v12 suggestions are rejected, and the AI text is moved to a labelled AI tab. AI use is logged (U19
   §3a item 12; §3b item 2).
2. **G2-G4 met.** The PDF passes every KIT §1a gate on Letter paper; pitch at most 45 and IPS at most 470 words; no
   TIPS or STRIPS.
3. **D0 voted before the TNA** (U19 §7a): what VT is for; the floor definition and rounding; why 2042 first; "sized
   for" vs the top-up rule.
4. **Vote set B logged by 27 Oct** (U19 §7b): D1 coupon cover (any option, stated honestly; the AI recommendation is
   3r); D2 Laura's kept half; D3 one certainty standard; D4 one floor definition; D5 one shortfall order inside the
   portfolio; D6 "responsible" and "flexibility" principles; D7 one WInS-scale clause; D8 the 2031 valuation date and
   re-quote rule. D9 floor size kept or changed by vote.
5. **Every KIT §5 error removed** (E1-E40). The parking rule is stated. No outside money. "Announce" is used only for
   the range. At most two dated anchor figures. One strategy name; the memoir link either carries the logic or is
   dropped.
6. **Willingness and capacity covered goal by goal; one link to the residency's operations** (KIT P2; mock-judge fix 5).
7. **Reflections that are true either way**: whether the Jan 2027 ladder costs above or below $300k (about 47% odds of
   above on the cautious basis, U19 §2); "refined" for IBTM only if the email time checks out; the 0.3-to-0.2 story only
   if a student remembers it and it is logged; VT's role reconciled with the note's "only" honestly.
8. **The two students' self-score, the outside reader and the defend-aloud test** done before submission (U19 §3b
   item 8).

### 5b. What the best version cannot change (these cap its scores)

| # | Constraint | Evidence | Lines capped |
|---|---|---|---|
| C1 | The notes are fixed. The VT note says stocks "only set how far her gift rises"; a careful reader will see any later job given to the equity | WNX:14; TNA:44 | IS6 in the TNA at most 3 |
| C2 | Two picked notes carry AI-exemplar wording (VT's last 12 words word for word; IBTM about 30% overlap) | TNAK:214, :472 | CP2 in the TNA at most 3 |
| C3 | The IPS bans detailed calculations, projections, the final range and charts, so the analysis is mostly scored in the FR | IPS:51-52, 68-70, 123 | PA lines in the IPS at most 3 in most cases |
| C4 | 500 words must cover every IPS:45-70 theme | KIT §3 budgets | CK4 and CK5 in the IPS at most 3 |
| C5 | Liability matching is an expected kind of answer; Wharton set a fixed-payment problem in 2021-22 | KB §3.3 | IS2 at most 3 without a team-own angle |
| C6 | The core idea came from an AI council run, so originality has to be shown in the team's own choices (D1-D9) and credited | FRP §8 S1 | CP4 2-3 |
| C7 | The decision record is thin before 20 Oct (no votes or authors recorded; the journal stops 7 Oct) | U19 §2 bullet 3 | AR3 and AR5 in the TNA at most 3 unless logged now |
| C8 | Seventeen days to the IPS; student prose of unknown quality | U19 §3b timeline | The low end of every range |
| C9 | The record risk persists: a public repo with exemplars for the exact three notes until it is made private, and heavy AI use that the Works Cited must disclose | U19 §3a item 11; AIP:224 | [INF] Could colour how readers see CP2 and CP4 |

### 5c. Line levels (b) (low / middle / high)

**IPS:**
- IS1 3 (3-4), IS2 3 (2-3), IS3 3 (3-4), IS4 3 (3-4), IS5 3 (3), IS6 3 (3-4).
- CK1 3 (3-4), CK2 3, CK3 3, CK4 3 (2-3), CK5 2 (2-3), CK6 3 (3-4).
- PA1 3 (3-4), PA2 3 (2-3), PA3 3 (2-3), PA4 3 (3-4), PA5 3, PA6 3 (2-3), PA7 3 (2-3).
- CP1 3 (2-3), CP2 3 (3-4), CP3 3 (3-4), CP4 2 (2-3), CP6 3 (2-3).

**TNA:**
- IS1 3, IS3 3 (3-4), IS4 3, IS5 3 (2-3), IS6 3 (C1).
- CK1 3 (2-3), CK2 3, CK3 3.
- PA1 3 (3-4), PA2 3 (2-3).
- AR3 3 (2-3), AR5 3 (2-4; level 4 only if the email timing and the IBTR decision to hold are both on record).
- CP1 3 (2-3), CP2 3 (2-3; C2), CP3 3, CP4 2 (2-3).

### 5d. Scores (b) (AI opinion; 0-10 per criterion)

| Deliverable | Strategy | Client | Analysis | Articulation | Creativity & Presentation | Mean |
|---|---|---|---|---|---|---|
| IPS low | 7.1 | 6.7 | 6.1 | N/E | 6.0 | 6.5 |
| **IPS middle** | **7.5** | **7.1** | **7.5** | N/E | **7.0** | **7.3** |
| IPS high | 9.2 | 8.3 | 8.2 | N/E | 8.5 | 8.6 |
| TNA low | 7.0 | 6.7 | 6.2 | 5.0 | 5.6 | 6.1 |
| **TNA middle** | **7.5** | **7.5** | **7.5** | **7.5** | **6.9** | **7.4** |
| TNA high | 8.0 | 7.5 | 8.8 | 8.8 | 7.5 | 8.1 |

**Reading it** [INF]:
- The middle estimate puts every IPS criterion in or just under the strong band. Client (7.1) and Creativity (7.0) sit
  just under 7.5. By FAQ:83 ("all five components"), that is contention, not a safe place.
- The gain from (a) to (b) is about +3.3 (TNA) to +3.5 (IPS) points on the mean. Authorship alone (CP2 0 → 3) adds
  1.5 to Creativity, or about 0.4 of the IPS mean's 3.5 gain. It matters more as a gate than as points. The rest comes
  from removing case breaches and contradictions and covering the missing themes. None of it needs new analysis.
- The Top-50 decision also rests on the Final Report (RR:60), which does not yet exist. A middle-case IPS can be
  carried in or dragged out by it.

### 5e. Which fixes move the IPS score most (AI opinion; measured on the 0-10 criterion scores)

| Fix | Lines | Criterion gain |
|---|---|---|
| Students write it (G5) | CP2 0 → 3 | Creativity +1.5; also removes the gate failure |
| No outside money; a real post-2033 order; the parking rule | IS4 1 → 3, IS3 2 → 3, PA4 1 → 3, CK6 2 → 3 | Strategy +1.3, Analysis +0.7, Client +0.4 |
| "responsible", "flexibility" and willingness covered, plus the residency link | CK2-CK4 1-2 → 3, PA6 1 → 3 | Client +2.1, Analysis +0.7 |
| Joints check against the notes and reflections | IS6 1 → 3 | Strategy +0.8 |
| At most two dated figures; no undated model yield | CP3 1 → 3, PA3 1 → 3 | Creativity +1.0, Analysis +0.7 |

---

## 6. What separates the best version from a finalist

A finalist is about 1 in 210 final reports: 11 of 2,339 in 2025-26 (KB §1.1). Finalists are picked at the semifinal,
from the top two of each group of judges (NS2526:115-117). In this sheet a finalist needs level 4 on most lines across
the IPS and FR, and then a semifinal in the same voice. The middle-case IPS has level 4 on none.

| Gap | Lines at stake | What level 4 needs (no wording; what must be true) | Where it is shown | Achievable by 4 Dec? (AI opinion) |
|---|---|---|---|---|
| 1. Projections the students built and can defend | PA3-PA7, IS4, CP3 | One named basis, re-priced on the 6 Nov close. A certainty standard tested by model and history. Coupon cover sized. Favourable, middle and unfavourable cases with every input listed. A joint stocks-and-yields stress. Each student able to rebuild a number without AI (U19 §3c item 5) | FR | Yes, if rebuilding starts 7 Nov (FRP §6, §9) |
| 2. The co-sponsor excerpt | CP6, PA5, CK4 | A firm bottom tied to the floor rule. A top labelled "can reach" with its chance beside it. A valuation date. The range in US$ with a dated NT$ equivalent and who bears the currency risk. No claims about co-sponsor behaviour that the evidence does not support (U19 §8) | FR | Yes; the facts are gathered (`S/oct19/cosponsor/cosponsor_research.md`) |
| 3. One insight that is visibly the team's | IS2, CP4 | Not "ladder + floor + growth" (an expected answer, C5), but the team's own resolution of a tension the case sets, such as how the 2031 range is built to hold, with a downward-only re-quote rule. It must be shown working and traced to the team's votes. The 19 Oct desk review called the mechanism behind the North Star memo, "a range built to hold", the most original idea on any branch (U19 §5b) | IPS principle; FR proof | Possible. It must come from the 27 Oct votes, not from an AI file |
| 4. Client depth beyond the case | CK5, CK3, CK4 | Sourced Taiwan context that changes a choice (floor size against local grant scales; currency); Laura's likely behaviour in a downturn; the artists and the community as the people the payments protect, without inventing traits | FR | Yes; partly researched |
| 5. A true, dated experience story | AR1-AR5, CP5 | Built from FRP §8's 21 candidates, completed from students' own memory: the 6 Oct rule change, the 7 Oct mis-click and the one-trader rule, the stale bond prices and the yield-check rule, the accrued-interest error, the IBTR test that nearly fired and the decision to hold, the challenge to the world fund and its outcome | FR | Yes, if the decision log is back-filled by 25 Oct (U19 §3c item 2) |
| 6. Voice that survives the semifinal | CP2, Written Responses | "authentic team voice, not generated or generic responses" (NS2526:111-112). Every student speaks and explains their contribution (NS2526:42-43). No new material (NS2526:49). The numbers card known cold (`S/oct19/drill/defence_drill.md` §1) | Semifinal | Only if the students write the IPS and FR themselves; it cannot be added later |
| 7. Integrity record | G5, CP2, CP4 | An honest Works Cited of AI use; the repo and fork private; no AI wording anywhere in the submissions. [INF] A finalist panel can ask "how do we know this is yours?" (drill K9); only the students' own text answers it | All | Yes, and urgent (U19 §3a item 11) |
| 8. Simplicity | CP1, IS1 | "less is more" [JUDGE 2022, 2023 champions, KB §4.1]; the cold-reader test with no word "Treasury" (KIT §7) | All | Yes |

**Context, not a scoring factor:** non-US teams make 40-51% of each Top 50 but have not won since at least 2021-22, and
no Australian team has made a Top 50 since 2021-22 (KB §0 item 9).

**Bottom line (AI opinion).** The best realistic TNA and IPS put Caplet in contention for the Top 50, as long as the
Final Report is at least as strong. Moving from contention to finalist depends on gaps 1-3 and 6. Gap 6 depends entirely
on the students doing the writing now: a voice written for them now cannot become their own at the semifinal.

---

## 7. Limits

- Wharton publishes no scale or weights. The levels, bands and the 2.5 × mean formula are my construction. The equal
  weighting follows FAQ:83 ("all five components") but is UNVERIFIED.
- The TNA's weight in the Top-50 cut is UNVERIFIED: RR:60 names only the IPS and the Final Report, while deliv:27 says
  all three are evaluated.
- Past criteria and feedback are from 2021-24. The 2024-25 and 2025-26 final-report criteria were not found on
  Wharton's site; the semifinal lists for those years name only the five headings plus Written Responses.
- Judge quotes [JUDGE] and the Teacher Guide [COPY] were collected 16 Oct and not re-opened today.
- Scores (a) rely on the 19 Oct verification of the Doc (VIE). The Doc's modifiedTime was re-checked today and is
  unchanged. The account behind the edits is UNVERIFIED and not relevant to the scores.
- Scores (b) score a hypothetical. Real student prose may land anywhere in the low-high range. The middle estimate
  assumes competent writing of correct content.
- All scores are one AI's opinion. Two students and the outside reader should score their own drafts with section 3
  before any AI check.
