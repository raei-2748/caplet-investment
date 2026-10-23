# Semifinal preparation blueprint (Team Caplet, built Tue 20 Oct 2026, finished about 10:50 Sydney [fixed 20 Oct, E7])

> **Checked copy (20 Oct 2026): this is `oct20/semiblue/semiblue.md` with the fixes from `oct20/verify_semiblue/verify_semiblue.md` applied, each change marked "[fixed 20 Oct, E#]".**
> **School name:** the school is named on 9 lines (its term-dates page and the citations to it); the leader decides before any public-repo use.

**AI-generated planning material (Claude Code), not for submission.** It holds requirements, a time budget, schedules,
checklists and risks. It holds **no script, no speech, no slide text, no value-statement wording and no model written
answers**, and none should be written from it by AI. Students write and say every word. If the team uses this file,
log it in the AI-use record now and in the Final Report's Works Cited later (Wharton: "If you use AI to assist you in
any way during the competition, how you use it must be recorded in your Works Cited pages",
https://globalyouth.wharton.upenn.edu/ai-policy/, `oct20/verify_pw/txt/AIP.txt`). Roles, not names; nothing here ranks
teammates.

**When to use it.** Before Sat 7 Nov 09:00 Sydney (IPS due): nothing. From 9 Nov to Sat 5 Dec 09:00 Sydney: only
Part 1 (the Final Report checklist). Everything else starts after the Final Report is in. RR:459 names the
IPS and Final Report: "The top 50 teams will be selected as semifinalists based on the strength of their
Investment Policy Statement (IPS) and Final Reports" (RR:459); the case says the three deliverables are judged
together (case:161-162), so the TNA may count as well (UNVERIFIED for selection) [fixed 20 Oct, E2]. Semifinal prep must never take time from those two.

**Labels.**
- **OFFICIAL-26/27** = in a live 2026-27 Wharton text.
- **PAST-OFFICIAL** = in an official Wharton text from a past year (2021-22 to 2025-26). It is not a 2026-27 rule.
- **FORECAST** = a prediction from the past pattern.
- **INFERENCE** = reasoning, not confirmed by any source.
- **UNVERIFIED** = nobody has confirmed it.
- **TEAM RULE** = a convention this blueprint proposes; the team may change it.
- **VERIFIED** = checked on a primary source or computed with zoneinfo. [fixed 20 Oct, E8]
- **MODEL** = computer estimate, not a fact. [fixed 20 Oct, E8]

**Short forms.** `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/`.
- `NS22`..`NS26` = Wharton "Semifinalists Next Steps" PDFs 2021-22 to 2025-26, text copies `oct20/verify_pw/txt/NS2x.txt` (line numbers from `cat -n` of those copies; NS26 lines re-read for this file).
- `RR` / `FAQ` / `MAIN` = live Rules & Roles page, live SMApply FAQ, live competition main page, copies `oct20/verify_pw/txt/RR.txt`, `FAQ.txt`, `MAIN.txt` (fetched 19-20 Oct 2026).
- `crit:n` = `/home/user/caplet-investment/competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt` (criteria :55-59).
- `case:n` = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`; `Guide:n` = `2026_WGY_Investment_Competition_Guide.txt` in the same folder.
- `KNOX:n` = Knox term-dates page, re-fetched with plain curl for this file on 19 Oct 2026 23:40 UTC (Tue 20 Oct 10:40 Sydney), `oct20/semiblue/web/knox_terms.txt` (https://www.knox.nsw.edu.au/about/public-information/term-dates/).
- `PB` = `oct20/semis/semis_playbook.md` (with its verify banner). `VPW` = `oct20/verify_pw/verify_pw.md`.
- `CS` = `oct20/casestudy/casestudy_pack.md` (with its banner). `VC` = `oct20/verify_case/verify_case.md`.
- `DR2` = `oct20/verify_drill2/drill_v2_checked.md`. `LG` = `oct20/verify_learn/learn_guide_checked.md`.
- `AB` = `oct20/artic_fixed/artic_bank_checked.md` (the checked copy only). `FRP` = `oct20/verify_frblue/fr_prep_v2_checked.md`.
- `WIN` = `oct20/semiblue/window_out.txt` (date and time-zone calculations for this file, Python zoneinfo; scripts in `oct20/semiblue/scripts/`).

---

## 0. What is fixed and what is forecast (read first)

| # | Item | Status | Evidence |
|---|---|---|---|
| 0.1 | Top 50 chosen on the IPS and Final Report (RR:459 names these two); the case says the three deliverables are judged together, so the TNA may count as well [fixed 20 Oct, E2] | OFFICIAL-26/27 (RR wording); UNVERIFIED whether the TNA counts for selection | RR:459; case:161-162 |
| 0.2 | "The Semifinals will be conducted virtually." | OFFICIAL-26/27 | RR:479 |
| 0.3 | Semifinal date: "TBD"; announcement date "TBD" | OFFICIAL-26/27 | MAIN:386-390 |
| 0.4 | A "short presentation (via video conference for the Semifinals …) … to a live panel of judges. All team members must participate." | OFFICIAL-26/27 (wording); the same wording ran beside recorded videos in past years, and the 2024-25 FAQ said "10-minute" (VPW E12) | FAQ:109 |
| 0.5 | Finale: "April 29 & 30 Learning Day & Global Finale" = Thu 29 and Fri 30 Apr 2027; in person or virtual; no travel funding | OFFICIAL-26/27 | MAIN:392; RR:481, 489; WIN |
| 0.6 | Consent and waiver for every semifinalist (parent/guardian signature under 18) | OFFICIAL-26/27 | RR:493 |
| 0.7 | No recording, screenshots or posting of presentations or participants during the Semifinals or Finale | OFFICIAL-26/27 | RR:495-497 |
| 0.8 | No invented "teamwork and experiential stories"; no plagiarised strategies | OFFICIAL-26/27 | RR:557 |
| 0.9 | Credit every image or medium the team did not make, in a deliverable "or a presentation" | OFFICIAL-26/27 | RR:569 |
| 0.10 | Format in every year 2021-22 to 2025-26: a **recorded 10-minute video** ("We will not watch presentations beyond 10 minutes"), then **four written answers of 250 words or fewer** | PAST-OFFICIAL (5/5 years) | NS22:13-14; NS23:14-15; NS24:14-15; NS25:14; NS26:12; NS26:104-108 |
| 0.11 | Video opens with "an on-screen introduction of each team member"; "voice-only narration is recommended" afterwards | PAST-OFFICIAL (5/5) | NS26:37-40; NS22:15-16 |
| 0.12 | "Every team member must have a speaking role" (5/5) "and briefly explain how they contributed value to the team" (3/3 since 2023-24) | PAST-OFFICIAL | NS22:19; NS24:20-21; NS25:20-21; NS26:41-42 |
| 0.13 | Case study of "one stock or ETF" (since 2023-24; "one company" before) | PAST-OFFICIAL | NS26:58-59; VPW §3a |
| 0.14 | "Do NOT introduce completely new material, or your team will be disqualified" (disqualification wording 4 of 5 years, from 2022-23); "not permitted to present a partially or entirely new strategy"; reflection on "weaknesses, limitations, or missed opportunities" allowed | PAST-OFFICIAL | NS26:46-54; VPW E2 |
| 0.15 | "you may not redesign your strategy after observing the results" | OFFICIAL-26/27 (Guide, for the Final Report; applies by INFERENCE to the semifinal) | Guide:158-159 |
| 0.16 | 2025-26: "up to 15 slides"; "approximately 9–11 core slides"; optional nine-part timed flow | PAST-OFFICIAL (2025-26 only) | NS26:16-18, 74-88 |
| 0.17 | Judged on "clarity, coherence, storytelling, and alignment with the team's written reports"; five criteria **plus "Written Responses"** (2024-25 and 2025-26) | PAST-OFFICIAL | NS26:33-35, 127-134; VPW §3a |
| 0.18 | Video submitted as a **link** (YouTube "UNLISTED" or a file host such as Dropbox), never an attachment; via SMApply in 2025-26, by email before | PAST-OFFICIAL (5/5) | NS22:34-37; NS26:97-101 |
| 0.19 | **No file format, resolution, size or codec was ever specified** in NS22-NS26 | PAST-OFFICIAL (absence; grep of all five PDFs, 20 Oct) | NS22-NS26 |
| 0.20 | Written answers: "You will not be able to include graphics or visuals"; "We are looking for your authentic team voice, not generated or generic responses" | PAST-OFFICIAL (2025-26; the authenticity line since 2023-24) | NS26:107, 110-111 |
| 0.21 | Live element at the semifinal (interview or Zoom questions) | UNVERIFIED: two school/student write-ups only; no NS PDF lists one | PB §2c; VPW §3e |
| 0.22 | 2026-27 semifinal wording (length, slide cap, case-study wording, deadlines, channel) | UNVERIFIED until Wharton publishes it | PB §14c |

**Planning assumption (FORECAST): a recorded 10-minute video plus four ≤250-word written answers, with a live
contingency.** Every part below says what changes if the format is live instead.

---

## 1. Deliverable 1: what must already be in the Final Report by Fri 4 Dec (Sat 5 Dec 09:00 Sydney)

**The test (PAST-OFFICIAL rule, applied by INFERENCE):** for every fact, number, chart and story the video or a
written answer might use, a judge must be able to find it in the IPS or the Final Report. If it is not there by
4 Dec, it goes in before 4 Dec or it is never used. After 4 Dec only three things may be added: (a) reflection on a
weakness or missed opportunity "without changing the original strategy" (NS26:52-54); (b) delivery (pace, clarity,
simpler wording); (c) a simpler drawing of content already in the report (INFERENCE, grey zone G3 below).

**How to use the table.** The owner role ticks each row only when the item is in the student-written Final Report
draft with a page reference. "Feeds" names the video segment (Part 2) or written-answer type (Part 4) that needs it.
Status is as of 20 Oct (from the cited files).

| # | Must be in the Final Report (students' own words) | Feeds | Source of the need | Status 20 Oct | Owner role |
|---|---|---|---|---|---|
| N1 | **IBTM case-study section**: what it is (index, 15 notes maturing 31 Jan-30 Nov 2032, 0.07% fee, ends "on or about December 15, 2032", "does not seek to return any predetermined amount"); the life of a share to the 1 Jan 2033 payment, including where the cash waits (17 days from 15 Dec, about 14 on the 2026 precedent); its two jobs and the split (1,142 payment / 3,361 floor of 4,503 WInS shares) | S5; W5 | NS26:58-59; CS §11 C1-C3; FRP §6 | Facts verified (CS, VC); no student text | Case-study owner |
| N2 | **Why no single 2032 Treasury**: WInS lists none strictly between 15 Feb 2031 and 15 Feb 2036 (the 15 Feb 2036 bond itself is listed); STRIPS and TIPS "NOT permitted" for both contributions (live FAQ) | S5; W5 | CS §11 C4; VC E2, E7 | Team check of 29 Sep only: re-check WInS before 5 Nov | Case-study owner + rules lead |
| N3 | **Payout drivers with sizes** and why the 2031 range's bottom is rounded down. Use the corrected margin: with the 0.07% fee, about $3.4-3.5k at −2 points against the $3,700 margin (about $0.2-0.4k spare); the $145k bottom holds by about $1.6k (MODEL). Matured 2032 notes are mostly rolled into the remaining 2032 notes, then cash: "yield locked on average to about 1 Jul 2032", not a cash cliff | S5, S6; W1, W5 | CS §11 C6; VC E3, E4 | MODEL only; a student must rebuild on the 6 Nov close | Case-study owner + rates analyst |
| N4 | **Fund-level risks**: Board may extend the termination date; termination and merger/reorganisation powers, cited to IBTM's own SAI dated 27 Feb 2026 (SEC EDGAR 485BPOS 0001193125-26-064179) | S5; W5 | CS §11 C7; VC E1 | VERIFIED source exists; no student text | Case-study owner |
| N5 | **Alternatives table** for the floor: Nov-2032 note (not on WInS), STRIPS (excluded by the rules), a short Treasury ETF (SGOV is WInS-listed), an intermediate Treasury ETF such as IEF/VGIT (about −$9k per 1-point rise just before the 2032 sale, MODEL), the Feb-2036 bond, a CD | S5, S6; W1, W5 | CS §11 C5; VC E5, E6 | MODEL only | Growth & risk analyst |
| N6 | **A shorter VT section** (the fallback case study): what it is (fact sheet dated 30 Jun 2026: 0.06% fee; "Number of stocks" 10,048, not the "approximately 8,000" bullet), why one fund, its job list **identical** to the IPS and the TNA reflection | S4, S5 (fallback); W5 | CS §11 C10; VC E14; DR2 Q29 | Job list undecided (vote D0-1/D2) | Growth & risk analyst |
| N7 | **The case-study decision**: why IBTM (or VT), logged with the date and any dissent | S5; W4, W5 | CS §11 C11; PB §5 | Not logged | Historian |
| N8 | **Two portfolio snapshots**: Laura's recommended plan (Jan 2027 ladder; Jan 2028 completion, floor and VT) and the frozen WInS book, with **one** stated scale factor (about 0.64-0.65; not 0.667) and the WInS "Long Equities" label explained once | S4; W1 | NS26:57; DR2 C5; CS §11 C9 | Trade Log tab empty | Trade-log keeper + rates analyst |
| N9 | **Every number a student will say**, each with its date and basis, rebuilt by a student on the 6 Nov close (the numbers card), and the rule "WInS gains and losses do not count" | all segments; all W types | DR2 §2-§3; Guide:70-73; case:132-133 | Card exists (MODEL, 19 Oct) | Rates analyst; a second student checks |
| N10 | **The certainty definition**, its test method, the assumptions (including coupon reinvestment) and the cover order for any shortfall, every step inside the portfolio (no "her other assets") | S3, S6; W1 | case:91-92; DR2 §0 items 4, 6; DR2 §8 checks 1-3 | Vote set B (Tue 27 Oct); V5 wording risk | Rates analyst |
| N11 | **Stress tests and good/middle/bad cases**: permanent yield falls (holdings basis $10,095 / $19,488 / $28,234 / $40,247 for 1 / 2 / 3 / 4.5 points, MODEL), a history replay, an equity crash before 2031/2033, the 2028 deposit late or short | S6; W1, W3 | crit:57 "under varying market outcomes"; FRP §0 item 3 | MODEL only | Growth & risk analyst |
| N12 | **The 2031 range**: the rule for bottom and top, one confidence figure with its method (kept apart from payment certainty), the valuation date, the re-quote rule, US$ with a dated NT$ equivalent, who bears FX | S7; W3 | case:109-120; FRP §9 X1-X4, X11, X17 | Undecided (D4, D8) | Client & co-sponsor lead |
| N13 | **The co-sponsor excerpt** (students' own text), checked against FRP §9 X1-X22 | S7; W3 | case:123-124; crit:59 | Not started (correctly) | Client & co-sponsor lead |
| N14 | **Client-fit reasoning in the case's own words** ("thoughtful risks", "appropriate balance", "flexibility", "responsible", "credible range") and the priority order (payments; responsible contribution; flexibility) | S1, S10; W2 | case:68-74, 101-103, 114-116; crit:56 | V5 uses "flexibility" 0 times | Client & co-sponsor lead |
| N15 | **Alternatives at strategy level, with priced reasons**: smaller floor or more stock; corporates; TIPS (not permitted this year); S&P 500 vs VT | S3, S6; W1, W2 | DR2 K4/K8-type questions; FAQ:69-70 | Numbers in AI files only | Growth & risk analyst |
| N16 | **Weaknesses and "what we would do differently"** (implementation, not redesign): e.g. the STRIPS plan before the WInS-only rule was checked; after-hours spreads; the 7 Oct mis-click; roles and votes logged late; AI over-reliance and how it was corrected. Each story's *facts* must be in the report | S8; W4 | NS26:52-54; Guide:158-159; AB E09, E15, E19 | Needs students' memories (AB §6) | Historian + editor |
| N17 | **A dated decision log with dissent** (who argued what, how it was settled) and one real disagreement the video can name | S9; W4 | crit:58 "decision-making process", "response to challenges"; AB §1 item 3 | No vote or dissent outcome on record | Historian |
| N18 | **Each student's role and at least one dated product** they can point to (a decision-log entry, an analysis they rebuilt, a check they ran), in the per-student template, each student filling only their own row | value lines (Part 2) | NS26:41-42; RR:557; AB §4 | All six rows blank | Each student (own row) |
| N19 | **The AI-use record in the Works Cited**, complete and honest, including AI-originated insights credited as such (iBond idea, IBTN trap, yield-check rule, sector-minimum fact check, core "buy the payments" idea) | S9; W6 | AIP; RR:467-475; AB §1 item 4; FRP §7 | 33-row register; gaps; `caplet/docs/AI_USE.md:49` false line | Historian; each student approves own rows |
| N20 | **Every chart or picture the video will show, or the data behind it** | S2-S7 | INFERENCE from NS26:46-51 | Chart pack exists (AI) | Editor |
| N21 | **One dated performance line** for IBTM and VT, framed as not counting (and noting that falling yields made Laura's ladder dearer) | S4, S5 | CS §11 C8; Guide:70-73 | Prices verified to 19 Oct | Trade-log keeper |
| N22 | **Consistency across TNA, IPS and Final Report** (VT's job, the shortfall order, figures on one basis). The TNA reflections may count as "existing material" too | all | case:161-162; crit:55 "consistency with the team's IPS"; PB §4 grey zones | Joints check planned (FRP §10 W3) | Editor |

**Grey zones (decide when the 2026-27 instructions arrive; ask Wharton if unclear):**
- **G1 Real January 2027 prices.** By February they are known. A new "what it really cost" calculation is new
  analysis (Guide:158-159). Answer with the rule the plan already set (the 2028 deposit completes the ladder first;
  the floor absorbs the difference). INFERENCE.
- **G2 Market moves after 4 Dec.** Context only, no new numbers. INFERENCE.
- **G3 New drawings of old content** (a timeline of an IBTM share, a ladder picture): probably fine if every element is
  in the report. Keep the FR page under each slide in the rehearsal copy. INFERENCE.
- **G4 "Midterm" wording.** Past instructions said "midterm and final competition reports" (NS26:46). This year has no
  midterm; expect "IPS" (and maybe the TNA). FORECAST.

**What this teaches:** the semifinal is not a new piece of work. It is the Final Report, said out loud in 10 minutes.
Anything you want to say in February has to be written down in November.

---

## 2. Deliverable 2: role map for a 10-minute video in which all six speak

### 2a. Time budget (TEAM RULE; built on the 2025-26 optional flow, NS26:74-88)

Target running time **9:30** (band 9:20-9:40). The uploaded file must be **≤ 9:45**. Nothing after 10:00 is watched
(NS26:12; PAST-OFFICIAL, 5/5 years; FORECAST for 2026-27) [fixed 20 Oct, E9]. The on-screen introductions count toward the 10 minutes (INFERENCE from NS26:37-40).

| Seg | Job of the segment (one idea; no wording given) | Time | Role who speaks | Criteria it mainly serves (crit:55-59) | FR rows it draws on (Part 1) |
|---|---|---|---|---|---|
| 0 | On-screen introductions: all six faces, first names and roles only | 0:30 (≈5 s each) | All; Team leader chairs | Articulation ("teamwork"); Creativity & Presentation | N18 |
| 1 | Laura and the tension in her problem (money in vs money out; payments first "with a high degree of certainty"; then a responsible gift and a credible 2031 range), not her biography | 0:35 | Client & co-sponsor lead | Client Knowledge ("Tailors … circumstances, priorities") | N14 |
| 2 | The strategy in one picture: the order (payments, then floor, then growth), each part with its job | 0:55 | Team leader | Investment Strategy ("clear and creative investment thesis") | N8, N10 |
| 3 | Why this strategy (rationale and market context): required return vs ladder yield, both dated; what "high certainty" means and the residual risks named | 0:40 | Rates analyst | Investment Strategy ("disciplined planning … cash-flow needs"); Portfolio Analysis | N9, N10, N15 |
| 4 | Portfolio snapshot: Laura's plan beside the frozen WInS book, one scale factor | 0:45 | Rates analyst | Investment Strategy ("appropriate diversification"); Portfolio Analysis | N8, N21 |
| 5 | Case study (two slides): IBTM, what it is and why it is the floor; how it ends and what can vary | 1:20 | Case-study owner | Portfolio Analysis ("investment concepts and tools"); Creativity ("original thinking") | N1-N7 |
| 6 | Analytical approach: how certainty and the range were tested (method, key assumptions, good/middle/bad cases), one or two results | 1:05 | Growth & risk analyst | Portfolio Analysis ("reasonable assumptions and projections … under varying market outcomes") | N9-N11, N15 |
| 7 | The 2031 range and the co-sponsor message: what is firm and what "can reach", one confidence figure, currency | 0:45 | Client & co-sponsor lead | Creativity & Presentation ("investment uncertainty clearly and credibly to prospective co-sponsors"); Portfolio Analysis ("the facility contribution") | N12, N13 |
| 8 | Reflection and learning: one or two real weaknesses and what the team would do differently (no redesign) | 0:45 | Historian & AI-record keeper | Articulation ("response to challenges"); Creativity ("meaningful reflection") | N16 |
| 9 | Competition experience: how decisions were made (one real disagreement and how evidence settled it), how AI was used and checked | 0:35 | Historian & AI-record keeper | Articulation ("research and decision-making process") | N17, N19 |
| 10 | Close: back to Laura's goals | 0:25 | Team leader | Client Knowledge ("recommendations that can earn her confidence") | N14 |
| — | Value lines: one per member, about 9 s, spoken at that member's **first** turn (not in a block) | 0:55 | Each member | Articulation; the NS speaking rule | N18 |
| — | Hand-offs (about 10 × 1-2 s) | 0:15 | — | — | — |
| | **Total** | **9:30** | | | |

Arithmetic: segments 0-10 = 500 s; value lines 55 s; hand-offs 15 s; total 570 s = 9:30. Re-add after every change.

**Airtime per role (content + value line; each also has about 5 s in Segment 0):**

| Role | Segments | Airtime | Natural fit (the team's own role list: lead, trader, rates analyst, growth/risk analyst, client/co-sponsor lead, Taiwan/inflation researcher; FRP owner roles) |
|---|---|---|---|
| R1 Team leader | 2, 10 (+ chairs 0) | 1:29 | Team leader (also the only WInS trader, an existing team rule, and the submitter, TEAM RULE proposed here) [fixed 20 Oct, E11] |
| R2 Client & co-sponsor lead | 1, 7 | 1:29 | Client/co-sponsor lead; could absorb the Taiwan/inflation researcher |
| R3 Rates analyst | 3, 4 | 1:34 | Rates analyst; trade-log keeper |
| R4 Case-study owner | 5 | 1:29 | Whoever writes the FR IBTM section (N1) |
| R5 Growth & risk analyst | 6 | 1:14 | Growth/risk analyst; may take 10 s more from Segment 3 if needed |
| R6 Historian & AI-record keeper | 8, 9 | 1:29 | Historian / editor |

**Owner labels used elsewhere in this file (TEAM RULE proposed here):** trade-log keeper = R3; historian and
editor = R6; "rules lead" and "deputy" map to no R-role yet: assigned 27 Oct. [fixed 20 Oct, E11]

**Rules for the map (TEAM RULE unless cited):**
1. **Real roles only.** A video role must be the role the student actually held in the Final Report work, shown by
   their own row in the AB §4 template. RR:557 bans invented "teamwork and experiential stories". Assign roles now
   (roles have been blank since 20 Aug, AB E01) so they are true by February.
2. **Value lines** (NS26:41-42): one sentence, about 9 s, *what I did* + *what it changed for the team*, pointing to a
   dated item (journal line, decision-log entry, AI-use row, FR section). No evidence, no claim. If AI built something
   and the student checked or rebuilt it, say so (DR2 Q41: proof of understanding, not authorship).
3. **Airtime within about ±15 s** of the mean (about 1:27). Nobody is introduced as "the best at" anything.
4. **One number per slide at most, with its date or "model" label** (CS slide guidance; DR2 §2).
5. **Backups.** Pairs rehearse each other's segments: R1↔R2, R3↔R4, R5↔R6. A backup never replaces a member: every
   member must speak (NS26:41). If a member cannot attend the group recording, they record their intro, value line and
   segment separately.
6. **Case-study switch rule (from PB §5; the team decides):** keep IBTM unless (a) the 2026-27 instructions say "stock"
   or "company"; (b) no student passes the IBTM drill (DR2 Part 4 section B questions) by
   sprint day D+3 (bar from PB §5: the v1 drill's IBTM checks CS1-CS5, `oct19/drill/defence_drill.md` §2g, 8/10 twice); or (c) the team votes VT a second job and wants the case study to show it. Then R4 presents VT from
   N6. An individual T-bond is probably not "one stock or ETF" (PB §5; FRP §6).

### 2b. Criterion coverage check (every criterion is covered at least twice)

| Criterion (crit:55-59) | Segments | Written-answer types (Part 4) |
|---|---|---|
| Investment Strategy | 2, 3, 4 | W1 |
| Client Knowledge and Objectives | 1, 10 [fixed 20 Oct, E10] | W2 |
| Portfolio Analysis | 3, 4, 5, 6, 7 | W1, W3, W5 |
| Articulation of Competition Experience | 0, value lines, 8, 9 | W4, W6 |
| Creativity and Presentation | 5, 7, 8; the whole deck's clarity | W3; every answer's "authentic team voice" |
| Written Responses (PAST-OFFICIAL 2024-25, 2025-26) | — | all four answers |

### 2c. If the 2026-27 format is live instead (contingency; UNVERIFIED)
- Same segments and times; the leader keeps a visible timer; one member signals 2:00 and 0:30 left.
- Q&A routing (PB §7): rates and bonds → R3; IBTM → R4; equity, stress tests → R5; client and co-sponsors → R2; process
  and AI → R6; "why" questions → R1, who routes. One 45-60 s answer plus at most one short add-on. Every member answers
  at least one question across the mocks.
- Every student must still take part (FAQ:109; RR:485 is a Global Finale rule, not a semifinal one) [fixed 20 Oct, E3].

---

## 3. Deliverable 3: rehearsal schedule, Top 50 announcement to video deadline

### 3a. The past pattern (PAST-OFFICIAL dates; gaps re-computed, WIN)

| Season | FR due → Top 50 | Top 50 (weekday) | Top 50 → video due (Mon) | Video → questions | Questions → answers (Mon) | Top 50 → results week |
|---|---|---|---|---|---|---|
| 2021-22 | 38 days | 20 Jan (Thu, stated date) | 18 days | 10 (Thu) | 4 | 53 |
| 2022-23 | 44 | 26 Jan (Thu) | 18 | 10 (Thu) | 4 | 53 |
| 2023-24 | n/a | 26 Jan (Fri) | 17 | 10 (Thu) | 4 | 52 |
| 2024-25 | 48 | 30 Jan (Thu) | 11 | 9 (Wed) | 5 | 46 |
| 2025-26 | 46 | 27 Jan (Tue) | 13 | 10 (Thu) | 4 | 41 |

Sources: VPW §3a (dates and gaps confirmed), §3c; WIN. Video deadlines 9:00 am ET to 2023-24, **8:00 am ET** in 2024-25
and 2025-26. The instruction PDFs went up 1-4 days before the public news post (media dates 20 Jan 2022, 24 Jan 2023,
25 Jan 2024, 28 Jan 2025, 23 Jan 2026; VPW §3a), so teams may hear before the public post (INFERENCE).

### 3b. The 2026-27 forecast window on the Sydney clock (FORECAST; conversions zoneinfo, WIN)

**Clock facts (VERIFIED, zoneinfo):** US Eastern goes to EST on Sun 1 Nov 2026 and to EDT on Sun 14 Mar 2027.
Sydney is on AEDT until Sun 4 Apr 2027 03:00, then AEST. So Sydney is 15 h ahead of ET until 1 Nov (the TNA, Sat 24 Oct
08:00 Sydney, is +15), **16 h from 1 Nov 2026 to 14 Mar 2027**, 15 h from 14 Mar to 4 Apr, and 14 h from 4 Apr
[fixed 20 Oct, E6]. **The whole semifinal window (January-February) is +16 h.**

**Two forecast methods disagree this year** because the Final Report is due on 4 Dec, about 8-9 days earlier than in past years
(13 Dec 2021, 13 Dec 2022, 13 Dec 2024, 12 Dec 2025):
- FR-gap method (38-48 days after 4 Dec): Top 50 between **Mon 11 Jan and Thu 21 Jan 2027**. Its centre (mean gap 44 days = Sun 17 Jan;
  median 45 = Mon 18 Jan; the 2025-26 gap of 46 = Tue 19 Jan) gives a video due **Mon 1 Feb** [fixed 20 Oct, E1].
- Calendar habit (every year 20-30 Jan; four of five 26-30 Jan): Top 50 between **about 20 and 30 Jan 2027**.
- Plan on the calendar habit, but watch SMApply and email from Mon 11 Jan (INFERENCE).

| Scenario (FORECAST) | Top 50 (ET) | Video due (ET) | = Sydney | Team deadline (TEAM RULE) | Questions out (Thu 09:00 ET; Wed in a 2024-25-type year) | Answers due (Mon 08:00 ET) | Results week (Top 50 + 41-53 days) |
|---|---|---|---|---|---|---|---|
| Early (FR-gap low end, ~11-14 Jan) [fixed 20 Oct, E1] | ~Mon 11 to Thu 14 Jan | Mon 25 Jan 08:00 EST | **Tue 26 Jan 00:00 AEDT** (Australia Day public holiday, KNOX:439) | Sun 24 Jan 18:00 | Thu 4 Feb = Fri 5 Feb 01:00 (or Thu 4 Feb 01:00) | Mon 8 Feb = Tue 9 Feb 00:00 | ~21 Feb-8 Mar [fixed 20 Oct, E1] |
| FR-gap central (~17-19 Jan) [fixed 20 Oct, E1] | ~Sun 17 to Tue 19 Jan | Mon 1 Feb 08:00 EST | **Tue 2 Feb 00:00 AEDT** | Sun 31 Jan 18:00 (hard: Mon 1 Feb 18:00) | Thu 11 Feb = **Fri 12 Feb 01:00** (or Wed 10 Feb = Thu 11 Feb 01:00) | Mon 15 Feb = **Tue 16 Feb 00:00** | ~27 Feb-13 Mar |
| Central (most likely) | ~Tue 26 to Thu 28 Jan | Mon 8 Feb 08:00 EST | **Tue 9 Feb 00:00 AEDT** | Sun 7 Feb 18:00 (hard: Mon 8 Feb 18:00) | Thu 18 Feb = **Fri 19 Feb 01:00** (or Thu 18 Feb 01:00) | Mon 22 Feb = **Tue 23 Feb 00:00** | ~8-22 Mar (straddles the 14 Mar US clock change) |
| Late | ~Fri 29 Jan | Mon 15 Feb 08:00 EST | **Tue 16 Feb 00:00 AEDT** | Sun 14 Feb 18:00 | Thu 25 Feb = Fri 26 Feb 01:00 | Mon 1 Mar = Tue 2 Mar 00:00 | ~11-23 Mar |

Days from first reading in Sydney to the Monday 18:00 hard team deadline: about 10.4-13.4 (early), 12.4-13.4 (FR-gap central,
video due 1 Feb; weekday announcement Mon 18-Tue 19 Jan), 10.4-12.4 (central), 16.4 (late) (WIN;
`oct20/verify_semiblue/fix_out.txt`) [fixed 20 Oct, E1]. **Build for 10 days**, whether the video is due 25 Jan, 1 Feb,
8 Feb or 15 Feb [fixed 20 Oct, E1].

**Knox calendar (VERIFIED, KNOX re-fetched 20 Oct):** Term 4 2026 ends with Presentation Day **Thu 3 Dec** (KNOX:425);
Fri 4 Dec is a staff PD day (KNOX:427). 2027: Australia Day **Tue 26 Jan** (KNOX:439); Years 5 and 7, and new Years
8-11 students, start Thu 28 Jan (KNOX:444-447) [fixed 20 Oct, E12]; **Term 1 commences Fri 29 Jan** (KNOX:449); Good Friday 26 Mar, Easter Monday 29 Mar;
Term 1 concludes **Fri 9 Apr** (KNOX:455); Anzac Day observed Mon 26 Apr (KNOX:458); **Term 2 commences Tue 27 Apr**
(KNOX:460). So the early scenario's video sprint falls in the holidays; its written round (Fri 5-Tue 9 Feb Sydney) is in
Term 1 [fixed 20 Oct, E13]. The FR-gap central sprint (about 19 Jan-1 Feb) straddles the start of Term 1 on Fri 29 Jan
[fixed 20 Oct, E1]; the central one runs through Term 1 weeks 1-2.

**Later steps (FORECAST unless marked):**
- Results events (live, virtual), "week of" early to mid March. Past start times "8:00-8:30 am ET" are from a secondary
  file only (KB, not re-checked; DR2 §9). That is **00:00-00:30 Sydney (next day) before 14 Mar**, **23:00-23:30 Sydney
  from 14 Mar**.
- Finale (OFFICIAL dates): Thu 29 and Fri 30 Apr 2027. An 08:00 EDT start is **22:00 AEST the same day**; 13:00 EDT is
  Sat 1 May 03:00 AEST (WIN). Which day holds the pitches: UNVERIFIED.

### 3c. Phase plan (TEAM RULE)

**Phase 0 (now to Sat 5 Dec): no rehearsal.** Only Part 1's table, used as a Final Report checklist from 9 Nov.
Two cheap exceptions: (1) roles assigned and logged at the next vote meeting (Tue 27 Oct); (2) the weekly journal
(AB §7) from now on, so value lines have evidence.

**Phase 1 (Sat 5 Dec to the announcement; summer holidays; about 45 min a week by video call; this is a bet, since
about 2% of teams are picked: 49 of 2,339 in 2025-26, VPW §3b):**

| When (Sydney) | What | Who |
|---|---|---|
| By Sun 6 Dec | Availability sheet: each student enters their own travel dates and whether they can record or join a call from there, 5 Dec-29 Jan (kept in the team's own sheet, not the repo) | Each student |
| By Sun 6 Dec | Log the case-study holding vote (N7) and the six video roles | Historian |
| Mon 7-Sun 20 Dec | Each role owner sketches their own segment from the submitted Final Report (own bullet notes, no AI text). The editor builds a rehearsal copy with the FR page under each planned slide | Role owners; editor |
| Mon 7-Sun 20 Dec | Learning: each student does LG chapters 1, 4, 5, 8 and 12 and their self-tests ("matter most for the semifinal questions", LG intro) | Each student |
| Mon 21 Dec-Sun 3 Jan | Off | — |
| Weeks of 4, 11 and 18 Jan | One 45-min session a week, rotating: (a) full timed run-through (stopwatch, 9:30 target); (b) rapid-fire drill (DR2 §7, 20 questions, cold, every member); (c) a written round (Part 4 format P-A) | All |
| One session in January | Private **tech test take** (Part 5): test recording, assembly, upload to an unlisted link and the logged-out check, using a non-presentation clip; delete it after | Editor + leader |
| One session in January | **No-investor test**: one run to an adult with no investing knowledge (NS26:72-73), who gives questions and scores only, never wording | All |
| One weekend in January | **Full four-question written mock**, Friday to Monday (Part 4 format P-C) | All |
| From Mon 11 Jan | Leader checks SMApply and email daily (announcement may come earlier than past years; INFERENCE) | Leader; deputy |

**Phase 2: the sprint, D0 (instructions read in Sydney) to the video deadline.** Built for 10 days; for a longer
window, add days at D+4 to D+6 (a second outside mock) and keep submission about 30 h early (Sun 18:00 target vs the Tue 00:00 Sydney deadline) [fixed 20 Oct, E5].

| Day | What | Who | Gate |
|---|---|---|---|
| D0 | Read the instructions verbatim; one shared table converting every date to Sydney; list every change from 2025-26 (format, length, slide cap, case-study wording, channel, any live element, "midterm"/"IPS" wording). Consent forms home (RR:493). Draft Wharton questions (Part 7b) if anything is unclear | Leader + rules lead | Change list posted |
| D+1 | 45-min call: confirm format; confirm case study (log it); confirm the role map, backups, recording method, team deadline and who is away | All | Decision-log entry |
| D+2 | Each role owner builds their own slides from the FR (own words; no AI text, no AI images passed off as the team's). Editor: layout only, never content | Role owners; editor | Draft deck |
| D+3 | **No-new-material audit**: every fact, number and image on every slide has an FR page (or IPS line) and a date/basis; credits for any image not made by the team (RR:569). IBTM drill check (switch rule, 2a item 6) | Rules lead + a second student | Audit sheet complete |
| D+4 | First full timed run on a call. Cut to ≤ 9:40. Name the three weakest segments | All | Time logged |
| D+5 | Fix weak segments; practise value lines aloud (each student's own notes) | Role owners | — |
| D+6 | Outside mock: an adult (teacher, parent) watches; questions and scores only | All | Score sheet |
| D+7 | **Record take 1** (Part 5). Watch back at 1× speed: sound, pace ("Slow down", NS26:64), time | All | Take 1 file |
| D+8 | Re-record weak segments; assemble; second audit (dates, credits, banned absolutes: "guaranteed", "risk-free", "cannot miss") | Editor + rules lead | File ≤ 9:45 |
| D+9 | **Lock**. Upload Unlisted; test the link logged-out and on a phone; prepare the fallback host link; **submit the link by the Sunday 18:00 target** (in a 10.4-day window D0 is a Friday, so D+9 is the Sunday); screenshot the confirmation [fixed 20 Oct, E5] | Leader; deputy watches | Link tested; confirmation saved |
| D+10 | **Monday reserve only** (hard team stop 18:00 Sydney); used only if D+9 slipped [fixed 20 Oct, E5] | Leader; deputy watches | Confirmation saved |
| Official | Mon 08:00 ET = **Tue 00:00 Sydney** | — | — |

**Phase 3: video to written questions (about 9-10 days, PAST-OFFICIAL).** Assign the four author-checker pairs
(Part 4). Two 30-min sprints a week on DR2 §6 likely types and §7 rapid-fire. Re-read the submitted video once
together, so the answers will not contradict it.

**Phase 4: the written window** (Part 4c).

**Phase 5: results event (March).** Join on camera if allowed; a short team introduction (the leader speaks; others say
names and roles; the team writes its own words). Plan for about 23:00-00:30 Sydney on a school night: parent
permission, a quiet room, a school adult if the advisor arranges one. Never record, screenshot or post (RR:497).

**What this teaches:** a US "8:00 am Monday" deadline is midnight at the *end* of Monday in Sydney, and the
announcement lands in the US working day, which is Sydney's night. Mis-read either and the 10-day window loses a day.

---

## 4. Deliverable 4: written-answer practice method (no model answers)

### 4a. Format facts (PAST-OFFICIAL, NS22-NS26)
- Four questions "related to your presentation", released about 9-10 days after the video (Thu 09:00 ET = **Fri 01:00
  Sydney**; Wed in 2024-25 = Thu 01:00), due 4-5 days later (Mon 08:00 ET = **Tue 00:00 Sydney**) (NS26:104-108).
- Each "250 words or fewer"; "You will not be able to include graphics or visuals" (NS26:106-107).
- Judged as a sixth item, "Written Responses" (2024-25, 2025-26). No descriptor for that item has been published
  (UNVERIFIED).
- "We strongly encourage you to draw upon your own competition experience and analysis. We are looking for your
  authentic team voice, not generated or generic responses" (NS26:110-111).
- Past questions have never been published (PB §8, searched 20 Oct). Any topic list is FORECAST.
- How SMApply counts words is UNVERIFIED. Aim for **225-240 words** on two different counters.

### 4b. Practice formats (TEAM RULE)

| Format | Time | How | Who |
|---|---|---|---|
| **P-A Sprint** (one question) | 20 min: 3 min read and list the FR pages to use; 14 min write; 3 min count and check numbers | Alone, offline, no AI tool open; only the FR, the numbers card and own notes; plain paragraphs, no bullets or tables | Every student |
| **P-B Pair round** | 45 min: author 20 min; checker 15 min scoring with the sheet below; author 10 min fixing | The checker marks and asks questions only; never writes replacement sentences | Pairs (rotate every round) |
| **P-C Weekend mock** (real-window rehearsal) | Fri to Mon | An outside adult or a teammate releases four questions at Fri 07:00 Sydney; pairs assigned by Fri lunch; author drafts Sat; checker scores Sun; a third student reads all four for contradictions with each other and the video; author reads aloud and finalises by Mon 18:00 | All six (four authors, the other two as checker and cross-reader; rotate) |
| **Read-aloud test** (inside every format) | 2 min | The author reads the answer aloud. Any phrase they would not say in their own voice is rewritten by them | Author |

**Question sources, best first:** (1) questions written by outside adults (teacher, parent, a former judge if one helps
again; questions only); (2) questions students write for another pair, which also tests understanding; (3) the DR2 bank
(§4 priority 43, §6 likely types, §7 rapid-fire). DR2 is AI-made: log its use. **No AI drafts, edits, shortens or
"polishes" any answer**, in practice or for real. If AI is used only to generate practice questions, log it.

**Likely question types to practise (FORECAST; PB §8 / DR2 §6, ranked):** W1 probe a claim in the video (certainty,
floor); W3 uncertainty and co-sponsors; W2 client fit or a client scenario; W4 team process, a challenge, a lesson;
W6 AI and authenticity; W5 the case study ("why this holding, what is its biggest risk?"). Practise each type at
least twice per student over Phase 1-3.

### 4c. The real window (TEAM RULE; times Sydney)
- **Fri (or Thu) 01:00 release.** Leader downloads at breakfast and posts the questions verbatim to the team.
- **Fri lunchtime, 15 min:** each question goes to an author-checker pair; the author lists the FR pages they will draw on.
- **Sat:** authors write alone, with a word counter, from their own notes, the FR and the numbers card.
- **Sun:** checkers score with the sheet; every number checked against the FR; anything not in the FR is flagged as
  possible new material. A cross-reader checks all four against each other and the video.
- **Mon by 18:00:** read-aloud by each author; the leader pastes as plain text, counts again, submits and screenshots.
- **Hard stop: Tue 00:00 Sydney.**
- Before pasting, run the team's provenance check (the 5-word overlap against AI files, FRP §7 / OPS §5B step 9).
- Keep drafts in Google Docs, so version history shows the students' own writing.

### 4d. Peer scoring sheet (the team's own scale; phrases quoted from Wharton texts)

**Gates (any fail = the answer fails; the author rewrites it):**

| Gate | Pass only if | Source of the gate |
|---|---|---|
| G-1 Length | ≤ 250 words on two counters (target 225-240) | NS26:106 |
| G-2 No visuals | Plain text only | NS26:107 |
| G-3 Existing material | Every fact and number has an FR/IPS page, with its date and basis | NS26:46-51; Part 1 |
| G-4 No redesign | Weaknesses reflected on, strategy unchanged | NS26:52-54; Guide:158-159 |
| G-5 No absolutes | No "guaranteed", "risk-free", "cannot miss", "can't break" | case:114-116; FRP §9 X10, X15 |
| G-6 Nothing invented | No invented story, feeling or conversation; no quote put in Laura's mouth | RR:557; CLAUDE.md "Verified corrections" |
| G-7 Own work | Written with no AI tool open; the author can explain every sentence aloud | NS26:110-111; AI policy |

**Scored lines (0-3 each; a failed gate caps every line at 1):**

| Line | Phrase to score against | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| L1 Answers the question | The question as asked (TEAM RULE: the answer is in the first sentence) | Off the question | Answer buried | Answer early, mostly on point | Answer first; every sentence serves it |
| L2 Voice | "authentic team voice, not generated or generic responses" (NS26:111) | Generic or AI-sounding | The students' words, stilted | Natural, plain | Plain, specific, sounds like the author |
| L3 Criterion fit | The criterion phrase(s) the question targets, e.g. "reasonable assumptions and projections to evaluate funding reliability" (crit:57); "Tailors the strategy to Laura's circumstances" (crit:56); "clearly explains the team's research and decision-making process" (crit:58); "investment uncertainty clearly and credibly to prospective co-sponsors" (crit:59); "maintains consistency with the team's IPS" (crit:55) | Not addressed | Touched | Addressed with one reason | Addressed with reason, evidence and the trade-off |
| L4 Data | "uses data effectively to support conclusions" (crit:59) | Numbers missing or wrong | Numbers undated or mixed bases | Few numbers, dated | Few numbers, each dated with its basis, each supporting the point |
| L5 Alignment | "alignment with the team's written reports" (NS26:33-35; a presentation criterion, applied to answers by INFERENCE) | Contradicts the FR or video | Drifts | Consistent | Consistent and cites the plan's own rule |
| L6 Plain English | "Why use 25 words when three will do?" (NS26:71); "Avoid excessive technical jargon" (NS26:67) | Jargon-heavy | Some jargon unexplained | Clear | A non-finance adult follows it first time |

**Scoring rules (TEAM RULE):**
1. Two scorers per practice answer. If they differ by 2 or more on a line, discuss the line's phrase, not the person.
2. Score answers, not people (DR2 protocol). Keep scores by question type, never a league table of students.
3. Scorers write marks, flags and questions only. No replacement wording from anyone but the author.
4. Track the lowest-scoring line across rounds; the next practice targets it.
5. An answer that scores 3 on every line in practice is still not reused verbatim: the real questions will differ, and
   memorised paragraphs read as "generic" (INFERENCE).

**What this teaches:** a 250-word answer is about one double-spaced page (FRP §2.1). It has room for one claim, one
reason, one dated number and one limit, not for a summary of the whole report.

---

## 5. Deliverable 5: recording and tech checklist

**File format (PAST-OFFICIAL by absence):** NS22-NS26 never specified a format, resolution, size or codec. They asked only
for a link to a streaming service (YouTube, set to UNLISTED) or a file host (e.g. Dropbox), not an attachment
(NS22:34-37; NS26:97-101). Everything in the "setting" column below is INFERENCE (widely playable choices), not a
Wharton rule.

### 5a. Before recording

| ✓ | Item | Setting / check | Why |
|---|---|---|---|
| ☐ | Time zone | One shared calendar in Australia/Sydney, ET shown beside each deadline; team deadline events at Sun 18:00 and Mon 18:00; official deadline at Tue 00:00 | Part 3b |
| ☐ | Recording method (one, chosen in January) | PowerPoint/Keynote "record slide show" with narration per segment, or Zoom/Teams local recording (gallery for the intros, then shared slides), or OBS | Remote members can record their own segment |
| ☐ | Intros | All six on screen at the start (gallery recording or six short clips); first names and roles on screen; no surnames | NS26:37; CLAUDE.md privacy rule |
| ☐ | Audio | Wired headset or USB mic per speaker; quiet, soft-furnished room; 10-second test played back on headphones; same input level for all | Bad audio is the most common amateur flaw (INFERENCE) |
| ☐ | Slides | 16:9; ≥ 24 pt text; slide numbers; contrast checked; one idea per slide; ≤ 15 slides if the 2025-26 cap repeats (plan 11-12 content slides) | NS26:16-19 |
| ☐ | Credits | Every image not made by the team credited on the slide or a final credits slide; prefer the team's own diagrams | RR:569 |
| ☐ | AI | No AI-written slide text, no AI voice, no AI images passed off as the team's; any AI image cited | NS26:67-68; RR:569; AI policy |
| ☐ | Rehearsal copy | A non-submitted copy with the FR page and the date/basis under each slide | Part 1 test |
| ☐ | School and consent | Advisor confirms whether the school crest or uniform may appear (UNVERIFIED school policy); every family has read and signed the consent and waiver, which lets Wharton use names, schools and cities | RR:493 |
| ☐ | Accounts | Confirm the upload account works: a school-managed Google account may block YouTube uploads or "anyone with the link" sharing outside the school (INFERENCE). Test in January from a non-school device | Phase 1 tech test |

### 5b. Recording and assembly

| ✓ | Item | Setting / check |
|---|---|---|
| ☐ | Export | MP4 (H.264 video, AAC audio), 1920×1080, 30 fps (INFERENCE) |
| ☐ | Duration | Check the **file's** duration (not the slide timer): ≤ 9:45 including intros |
| ☐ | Editing | Simple cuts only; no music under speech; no transitions that hide content |
| ☐ | Watch-back | Whole team watches the assembled file at 1× once before upload; one student checks every on-screen number against the rehearsal copy |
| ☐ | Remote segments | Same mic distance and room type; a 2-second pause at each start and end for clean cuts |

### 5c. Upload, submit, back up

| ✓ | Item | Setting / check |
|---|---|---|
| ☐ | Host | YouTube **Unlisted** (never Public: public posting risks the posting ban, RR:497). Fallback: Google Drive or Dropbox with "anyone with the link can view" |
| ☐ | Timing | Upload at least 24 h before the team deadline; HD processing can take time after upload (INFERENCE) |
| ☐ | Link test | Open the link logged out (private window) and on a phone on mobile data; check it plays to the end and the duration matches |
| ☐ | Fallback link | A second host already uploaded and tested, ready if the first fails |
| ☐ | Submit | Paste the link where the 2026-27 instructions say (SMApply in 2025-26, NS26:97); leader submits, deputy watches; screenshot the confirmation with the Sydney time visible |
| ☐ | Back-ups | Three copies of the final file (presenter laptop, external drive or USB, team Drive), plus the deck as PDF and native file |
| ☐ | After submission | Do not delete, replace or edit the uploaded video until results are out (a changed upload may break the link; INFERENCE). Keep the link out of the public repo |

### 5d. If any part is live (results event, a live semifinal, a virtual finale)
- One school room with wired internet if possible; a 4G/5G hotspot on a separate network as backup (RR:489, a Global Finale rule,
  applied to other live events by INFERENCE [fixed 20 Oct, E4]: the team provides "the equipment and internet connection needed to participate live").
- Presenter laptop with the deck stored locally; a second laptop already in the call, deck open, ready to share.
- All members visible; only the speaker's mic open (echo); an external speakerphone if in one room.
- Test call with the advisor at the real Sydney hour a week before; check screen share on the platform used.
- No recording, screenshots or posting by anyone, parents included (RR:495-497).
- A school adult or parent present for late-night sessions (advisor arranges; admin only).

---

## 6. Deliverable 6: risks and mitigations

Likelihood and impact are judgements (H/M/L), not data.

| # | Risk | L | I | Mitigation | Trigger / owner |
|---|---|---|---|---|---|
| K1 | **New material in the video or an answer → disqualification** (PAST-OFFICIAL, 4/5 years) | M | H | Part 1 checklist complete by 4 Dec; D+3 and D+8 audits; G-3 gate on every answer | Rules lead |
| K2 | **Hindsight trap**: real Jan 2027 prices used as new analysis | M | H | Grey zone G1; answer with the plan's rule; DR2 §0 item 3 | Rates analyst |
| K3 | **Format differs** (live, longer or shorter, no written round) | M | M | D0 change list; live contingency (2c, 5d); ask Wharton (7b) | Leader |
| K4 | **Window shorter than planned** (11 days in 2024-25) or announcement earlier (FR-gap method: 11-21 Jan) | M | H | Build for 10 days; Phase 1 sketches; monitor from 11 Jan | Leader; deputy |
| K5 | **Deadline mis-read** (Mon 08:00 ET read as Monday morning Sydney, or the wrong DST offset) | M | H | Shared Sydney calendar; team deadlines 30 h early; every conversion re-done with a converter on D0 | Rules lead |
| K6 | **A member travelling or unavailable** in the holidays or Term 1 week 1 | H | M | Availability sheet by 6 Dec; separate segment recording; backup pairs; never drop a member (NS26:41) | Each student; leader |
| K7 | **Value lines with no evidence**, or vague, or overstated | H | M | AB §4 template and weekly journal from now; value line must point to a dated item; RR:557 | Historian; each student |
| K8 | **AI authenticity**: AI-sounding answers, or an AI story that is not in the Works Cited | M | H | G-7 gate; no AI open while drafting; provenance check; Works Cited complete (N19); answer AI questions with the true record | Historian; each student |
| K9 | **Overrun past 10:00** (nothing after is watched: PAST-OFFICIAL, 5/5 years; FORECAST for 2026-27 [fixed 20 Oct, E9]) | M | H | 9:30 target; file ≤ 9:45; timed runs at D+4 and D+7 | Editor |
| K10 | **Case-study holding fails** (IBTM too hard to explain cold, or wording says "stock") | L-M | M | Switch rule (2a item 6); N6 VT section ready in the FR | Case-study owner |
| K11 | **Inconsistency** between TNA, IPS, FR and video (VT's job, scale factor, number bases) | M | H | N22 joints check; one numbers card; one scale factor; one VT job list | Editor |
| K12 | **Stale or mixed numbers** (yields quoted without date; MODEL figures as facts) | H | M | Only FR numbers, each dated with basis; "MODEL" spoken where it applies; DR2 §3 fragile-number rules | Rates analyst |
| K13 | **Upload or link failure** (processing, private setting, school account block) | M | H | January tech test; upload 24 h early; logged-out and phone test; fallback host | Leader; editor |
| K14 | **Poor audio or pace** ("Slow down", NS26:64) | M | M | Mic per speaker; watch-back at 1×; no-investor test | Editor |
| K15 | **Consent forms late** | L | H | Send home on D0; advisor tracks | Advisor (admin); leader |
| K16 | **Written window clashes with school days** (Fri-Mon in term) | H | M | Fri lunchtime assignment; Sat/Sun writing; Mon 18:00 stop; the P-C weekend mock rehearses it | Leader |
| K17 | **Privacy**: surnames, faces or the video link reach the public repo or the open web | L | H | First names only; link kept out of the repo; Unlisted; no recording or posting of Wharton events | All |
| K18 | **Semifinal prep eats IPS / Final Report time** | M | H | Phase 0 = nothing; Phase 1 capped at 45 min a week | Leader |
| K19 | **Late-night live events** (results ~23:00-00:30 Sydney; virtual finale ~22:00-03:00) | H | L-M | Parent permission; school adult; quiet room; sleep shift for a finale | Advisor (admin); families |
| K20 | **Ranking or comparing teammates** in files or the video | L | M | Identical templates; roles not ranks; no "best at" | All |

---

## 7. Decisions and questions

### 7a. For the team (log each with the date, who argued what, and any dissent)
1. Six video roles assigned to real FR roles (by Tue 27 Oct with the other roles; confirm on sprint D+1).
2. Case-study holding (IBTM recommended by CS/PB; VT fallback), logged by early December so the FR carries both
   sections (N1-N7).
3. Recording method (test in January).
4. Team deadlines (this file proposes Sun 18:00 target, Mon 18:00 hard stop, for each Tue 00:00 Sydney deadline).
5. Whether to run Phase 1 at all, and how much time it gets (a bet; TEAM RULE proposes 45 min a week).

### 7b. For Wharton, only if the 2026-27 instructions leave it unclear (a student words it; the leader sends)
1. Is the semifinal a recorded video plus written answers, or a live presentation (FAQ:109 says "live panel")?
2. Which documents count as existing material: the IPS and Final Report only, or the TNA too?
3. May the presentation mention market events or prices after 4 Dec as context if the strategy and analysis are
   unchanged?
4. May an individual Treasury bond be the case-study holding?
5. Is there a required file format or host?

---

## 8. Still UNVERIFIED
- The whole 2026-27 semifinal format: length, slide cap, case-study wording, no-new-material wording, channel, dates.
- Any live interview at the semifinal (two school claims only).
- The Top 50 announcement date (FORECAST range 11-30 Jan 2027) and the hour it reaches teams; so the video deadline
  (FORECAST: Mon 25 Jan, 1 Feb, 8 Feb or 15 Feb ET) [fixed 20 Oct, E1].
- How SMApply counts words; whether the 2026-27 written round exists and has four questions.
- Results-event start times (secondary source only); the finale's day order and start time.
- Whether school-managed accounts allow unlisted uploads and external link sharing; school policy on crest and uniform.
- WInS listings for N2 and N5 (team check of 29 Sep only).

## 9. Sources and checks
- Official 2026-27: RR:459, 467-475, 479-497, 557, 569; FAQ:69-70, 109; MAIN:386-392 (copies `oct20/verify_pw/txt/`,
  fetched 19-20 Oct 2026); crit:50-59; case and Guide lines as cited.
- Past official: NS22-NS26 (`oct20/verify_pw/txt/`, downloaded 19-20 Oct 2026 from
  https://globalyouth.wharton.upenn.edu/wp-content/uploads/); NS26 lines re-read for this file; NS22-NS25 grepped for
  any file-format rule (none).
- Knox term dates: https://www.knox.nsw.edu.au/about/public-information/term-dates/, re-fetched with plain curl
  19 Oct 2026 23:40 UTC (HTTP 200 after a 301 redirect), text `oct20/semiblue/web/knox_terms.txt`.
- Built on (checked copies): PB + banner, VPW, CS + banner, VC, DR2, LG, AB (checked copy only), FRP.
- Calculations (Python zoneinfo, this session): `oct20/semiblue/scripts/window.py`, `scen.py` → `oct20/semiblue/window_out.txt`
  (past gaps, weekdays, three scenarios, every ET→Sydney conversion, DST transitions 1 Nov 2026, 14 Mar 2027, 4 Apr 2027).
  Re-run 20 Oct (`-I`, zoneinfo): output identical. Supplement for the fixed rows (FR-gap low end and central, D+9/D+10
  weekdays, offsets): `oct20/verify_semiblue/scripts/scen_fix.py` → `oct20/verify_semiblue/fix_out.txt` [fixed 20 Oct, E1].
- Personal data: checked against the tokens in `oct16/tools/.pii_tokens` (tokens not printed); first names do not
  appear; roles only.
