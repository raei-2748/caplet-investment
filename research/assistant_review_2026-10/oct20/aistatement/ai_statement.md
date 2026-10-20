# What is Wharton's "Statement of AI Use"? (Team Caplet, Tue 20 Oct 2026)

AI-generated research (Claude Code). Not for submission, and not wording for any deliverable or message. It quotes
Wharton's pages and checks the 20 Oct pack against them. If the team uses it, log that in the AI-use record.

## 1. Verdict

- **The "Statement of AI Use" is not a form, a checkbox or a document to sign.** It is the heading of the first
  section of the AI Policy page itself (`web/ai_policy.txt:251`). The "application integrity statement" is the
  second section, and it sits under the heading **"Applying to Programs and Courses"** (`:259-260`). It is about
  applications to summer programs, not the competition. The page links no PDF or form: its only body links are
  Penn's Code of Academic Integrity, the CFA Asset Manager Code and Wharton AI & Analytics (raw HTML, body section).
- **Wharton's own wording is "strongly encouraged to review"** (`:224`). That is a request to read the page. No
  public page says anyone must sign, tick or accept the Statement: not the AI Policy page, Rules & Roles, the
  Competition FAQ, the six public SMApply pages or the six official PDFs. A WordPress site search for "statement of AI
  use" and "integrity statement" found no separate page (`web/raw/wp_search_*.json`).
- **What binds the team** is the section headed "Participating in Global Competitions > Investment Competition"
  (`:263-270`), which has three parts: Ethics, AI Policy and the Checklist. The general Statement (`:252-257`) also
  applies, because it covers all "Wharton Global Youth Program students".
- **Where AI use is recorded:** "your Works Cited pages" (`:270`). Only the Final Report has a Works Cited. The TNA
  instructions never mention AI or citations. The IPS instructions ban "formal citations" (IPS:123-125). No public
  text requires an AI line inside the TNA or the IPS, and none forbids one in the TNA.

## 2. Sources and fetch times

All fetched with curl through the proxy with a cache-busting query on **Tue 20 Oct 2026, 00:00-00:05 UTC =
11:00-11:05 Sydney (AEDT)**. Log: `web/fetch_log.txt`. Raw copies: `web/raw/`. Text copies: `web/*.txt`. These were
made with `tools/h2t.py`, run under `venv/bin/python -I`.

| Code | URL | Fetched (UTC) | Note |
|---|---|---|---|
| AIP | https://globalyouth.wharton.upenn.edu/ai-policy/ | 00:00:37Z | `dateModified` 2026-10-14T13:48:39Z. The body text matches the 19 Oct copy (`oct20/compliance/web/ai_policy.txt`). Only the list markers differ |
| RR | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ | 00:00:41Z | modified 2026-09-08 |
| GYF | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/ | 00:00:42Z | modified 2026-09-13 |
| COMP | https://globalyouth.wharton.upenn.edu/investment-competition/ | 00:00:39Z | AI appears only in the site-wide menu teaser |
| SMF / SMD | https://wghsinvcomp.smapply.us/res/p/faqs/ , /res/p/deliverables/ | 00:00:44Z / :45Z | no AI, integrity or attestation text |
| APP | https://globalyouth.wharton.upenn.edu/application-information/ | 00:02:24Z | for program applicants |
| POL | https://globalyouth.wharton.upenn.edu/policies/ | 00:02:22Z | the menu teaser and a link only |
| TNA / IPS PDFs | Box links in `oct20/compliance/web/fetch_log.txt` | 00:04:38Z / :42Z | MD5 matches the repo copies in `competition/official/2026_27/` |
| Penn Code | https://catalog.upenn.edu/pennbook/code-of-academic-integrity/ | 00:02:10Z, 00:02:22Z | **NOT FETCHED** (TLS error from the upstream site, even with the proxy CA). Its content is UNVERIFIED here |

The other saved copies were also searched: `oct20/compliance/web/` (ethics, SMApply guide, home, trading, WInS,
client, contact, trading-outside-US) and `competition/official/2026_27/` (Guide, Infographic, School Documentation,
the client profile, `smapply_public_2026-10-14/`). None has any AI text apart from the menu teaser.

## 3. Exact requirements (≤30 words each)

**Who it is written for**
- AIP:224 (the site-wide menu teaser, also on COMP:224, RR:224 and GYF:224): "High school students applying to and
  participating in Wharton Global Youth programs, courses and competitions are strongly encouraged to review the ...
  Statement of AI Use, application integrity statement and accompanying AI policies".
- AIP:258: "Additional details on AI use and policies for Wharton Global Youth programs, courses and competitions:"
  Three headed blocks follow it:
  - "Applying to Programs and Courses" (:259)
  - "Participating in Global Competitions / Investment Competition" (:263-264)
  - "Enrolling in the Wharton Pre-baccalaureate Program" (:278)

**Statement of AI Use (all WGY students, so it covers the competition too)**
- AIP:254: "When students express themselves in the Wharton Global Youth Program, they must use their voice and
  words."
- AIP:254: "AI-generated work should be cited like any other reference material, including how and where students
  used AI-generated information."
- AIP:255: "ensure their final work reflects their ideas, words, and creativity."

**Application integrity statement (program applications, not the competition)**
- AIP:261: "your work contained within this application must be your own."
- AIP:262: Wharton "may use its own proprietary and/or licensed AI solutions in order to identify AI-authored elements
  of applications."

**Investment Competition block (binding)**
- AIP:266 (Ethics): "We trust that you will not ... pass AI generated writing or work off as your own".
- AIP:268: Wharton may use "third-party private investigatory firms and/or forensic analysts".
- AIP:270 (AI Policy): "You may not submit any work generated by an AI program as your own."
- AIP:270: "If you use AI to assist you in any way during the competition, how you use it must be recorded in your
  Works Cited pages."
- AIP:272 (Checklist, advisory): "it is a good idea to ask yourself these Checklist Questions". The questions are at
  :273-277.

**Rules & Roles (the competition's own page; softer wording)**
- RR:322-326: AI tools are allowed "for brainstorming and idea generation"; "AI-generated work may not be submitted
  as your own"; "Any AI-generated material included in your report must be properly cited".
- RR:365: "If you include material generated by an AI program, it should be cited like any other reference
  material". RR has **no** "Works Cited" sentence.
- RR:368 (Ethics): **omits** the "pass AI generated writing" clause that AIP:266 contains. On these two points the
  AIP text is the stricter one.
- RR:374: "Each team is required to properly cite any sources used".
- RR:336: the only signature in the rules is a "signed Consent and Waiver of Liability" for semifinalists and
  finalists. It is a media and liability consent, not an AI statement.

**Deliverable instructions**
- IPS:123-125 (repo PDF text): "formal citations are not permitted"; "sources do not need to be cited in the IPS";
  "Relevant sources and supporting evidence must be included in the Final Report."
- TNA PDF: 0 matches for AI, generative or cite. SMD:59: judges score "an authentic team voice".
- APP:297-303 (applications only): "Cite any AI-generated material appropriately"; "To read Wharton Global Youth's
  Statement of AI Use, visit our AI policy webpage."

## 4. Signed or accepted? By whom? When? Where is AI disclosed?

- **Signed or accepted:** no public text requires it. The public wording is "strongly encouraged to review"
  (AIP:224). Whether the logged-in SMApply TNA form, or the roster task already submitted, shows an AI, integrity or
  terms checkbox is **UNVERIFIED**. Only a logged-in screenshot can settle it.
- **By whom:** the obligations are written to every student ("you", "students", "team members": AIP:254, :266,
  :270) and to the team (RR:374). No advisor role is stated. The team leader submits the deliverables "through
  SurveyMonkey Apply" (RR:285).
- **When:** the obligations apply throughout ("from the moment you register", AIP:266; "in any way during the
  competition", AIP:270). No per-deliverable acceptance is stated.
- **Where disclosed:** in the "Works Cited pages" (AIP:270), which in practice means the Final Report (IPS:125). The
  IPS bans formal citations. The TNA is silent. A TNA-level line is neither required nor banned: this is UNKNOWN
  until batch-1 Q1 is answered or form check C shows a field.

## 5. What applies to the TNA on Thu 22 Oct

1. The reflections must be the students' own words and voice (AIP:254, :255, :270; RR:325). AI text cannot be
   submitted as the team's own, even if it is tagged or logged (AIP:266).
2. Every AI use behind the TNA must be recorded "in any way" and "how" (AIP:270). The record's final home is the
   Final Report Works Cited. Log it now so that it can be written up later.
3. The quoted notes are fixed. Where a quoted note contains AI words (the 13-word clauses in VT and Nov-2040), the
   policy text says AI material "should be cited" (RR:365; AIP:254 "how and where"). Where that citation goes for the
   TNA is the open Q1(b).
4. Nothing needs to be signed or ticked, based on the public pages. Check the form (section 6, G3).
5. The Checklist (AIP:273-277) is advice, not a rule. It is still worth each author asking themselves before the
   text lock.

## 6. Gaps against the 20 Oct pack (file:line, exact fix)

The paths below are under `oct20/`. The pack's core reading is **right**: it uses the stricter AIP wording, it
treats AIP:465 as pre-baccalaureate advice, and it treats the Works Cited as the place where AI use is recorded. No
quote that was checked is wrong. Four gaps:

| # | Where | Gap | Exact fix |
|---|---|---|---|
| G1 | `ops/operating_plan.md:113` (M3, DL-16 "and any disclosure decision"); `verify_pm2/premortem2_checked.md:111` ("decide at M3 whether the TNA submission carries a one-line factual disclosure") | M3 is Thu 22 at 19:00, but the text lock is Thu 22 at 16:00 (`ops/operating_plan.md:193`; pack `out/Caplet_M1_Meeting_Pack_20Oct2026.md:48`). A disclosure line decided at 19:00 could not be student-written and paste-checked before the lock | Move the decision to a logged vote at **M2 (Wed 21, 20:00)**, or a chat vote by **Thu 22, 12:00** after any Wharton reply (expected by about 08:00). Any line is written by a student before 16:00. M3 only confirms it |
| G2 | `compliance/compliance_matrix.md:136` (row 29: "UNKNOWN (how to disclose AI in the IPS)" ... "Ask Wharton question 1") | Batch-1 Q1 no longer asks about the IPS. It was narrowed to the TNA (`out/Caplet_Wharton_Questions_SendToday_20Oct2026.md:16-19`; `verify_ask2/verify_ask2.md:155`, E9). Row 29 points to a question that will not be asked | Change row 29's action to: "IPS answered by IPS:123-125 + AIP:270: no citation line in the IPS; record in the FR Works Cited (verify_ask2 E9). Not in batch 1." Alternatively, use the optional Q1 change below |
| G3 | `out/Caplet_M1_Meeting_Pack_20Oct2026.md:87` ("Is there an AI field?"); `out/Caplet_Wharton_Questions_SendToday_20Oct2026.md:7` (check C) | Only the logged-in form can show whether any acceptance of the Statement of AI Use, or of an integrity or terms statement, exists | Extend the check to: "Is there an AI field, or any AI, integrity, 'own work' or terms checkbox or statement, on the TNA task or the submitted roster task? Screenshot its exact text; do not tick it before the vote." |
| G4 | `ailog/ai_use_register.md:15-18` (banner) | The banner is correct, but it quotes only the AIP page. It does not say that the competition's own Rules & Roles page is softer: no Works Cited sentence (RR:365), and no "pass off" clause (RR:368) | Optional: add "This is the stricter of two live Wharton texts; Rules & Roles (RR:322-326, :365) says AI material 'included' must be cited. Caplet follows the stricter one." |

Not gaps:
- No pack file mentions the "Statement of AI Use" or the application integrity statement. That is correct, because
  neither creates a separate duty for the competition.
- The pack's AIP:377 / :370 / :465 references (to `oct19/office/web/ai_policy_2026-10-19.txt`) and RR:270-271 / :315
  (`compliance/web/rules_roles.txt`) were checked and point to the quoted lines.

## 7. Should batch-1 Q1 change before 22:00 Sydney?

- **No change is required.** Q1(a) and (b) still ask the one thing the public pages leave open: whether the TNA needs
  anything beyond the Final Report Works Cited, including for AI words inside quoted notes.
- **Do not add a question about signing the Statement of AI Use.** The public text answers it: the Statement is to be
  reviewed, not signed. Ask only if check C shows an attestation whose meaning is unclear.
- **Do not ask about the application integrity statement.** It covers program applications.
- **Optional:**
  - Have the student anchor Q1 to the sentence "recorded in your Works Cited pages" (AIP:270), so that the reply
    addresses that exact text.
  - If the team prefers one round-trip over G2's matrix fix, add "and the IPS, where formal citations are not
    permitted (IPS:123)" to Q1(a). verify_ask2 E9 judged that part already answered, so this is the team's choice.

## 8. UNVERIFIED

- What the logged-in SMApply TNA and IPS forms, and the submitted roster task, show: any AI field, attestation
  checkbox or terms text.
- Whether the logged-in SMApply Pages tab or the WInS weekly emails add AI rules.
- The content of Penn's Code of Academic Integrity, which could not be fetched (TLS error).
- How Wharton reconciles the AIP "Works Cited pages" sentence with the TNA, which has no Works Cited. That is Q1.
