> **CHECKED COPY (verify_runbook, wave H, Tue 20 Oct 2026 about 11:50 Sydney).** Adversarial check of
> `oct20/runbook/runbooks.md`. All Google and SurveyMonkey help pages were re-fetched live (plain curl, cache-busting
> query, 19 Oct 23:27-23:31 UTC, all HTTP 200; text identical to the runbook's 23:08 copies) and saved in
> `oct20/verify_runbook/web/`. **Material fix:** the SMApply decision rule (§0 item 2, §3.5) was rewritten. SMApply's own
> help says "Submit" only works once every required task is complete, and that stages move an application on at
> submit. So a 22 Oct "Submit" locking the IPS and Final Report is unlikely. The bigger risk is the opposite: not
> pressing a Submit that is the TNA's real submission. Other fixes: a scope guard before "Reject all", corrected SMD
> line numbers, "Restore this version" reworded, IPS:101-102 added, house checks labelled as house checks, a
> provenance.py reader fix (`oct20/verify_runbook/provenance_fixed.py`), and a line-break-safe grep. Every changed
> place is marked **[fixed 20 Oct]**. The full error table is in `oct20/verify_runbook/verify_runbook.md`.

# Submission-day runbooks: (A) Trading Notes Analysis and (B) IPS

AI-generated process checklist (Claude Code, wave F, Tue 20 Oct 2026, about 10:10 Sydney). It holds steps, roles,
times, commands and checks only. It drafts no TNA reflection, pitch, IPS or Final Report wording. If the team uses it,
log it in the AI-use record as a "process/tooling" row (Wharton: "If you use AI to assist you in any way during the
competition, how you use it must be recorded in your Works Cited pages", `oct19/office/web/ai_policy_2026-10-19.txt:377`).
The three scripts in `tools/` were written by the same AI session; they contain no AI and change no file, but log
them too.

**Short names.** `oct19/`, `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`.
`RB/` = `oct20/runbook/` (this folder). `OFF/` = `/home/user/caplet-investment/competition/official/2026_27/`.
`TNA:n` = `OFF/2026_WGY_Trading_Notes_Analysis-FINAL.txt` line n. `IPS:n` = `OFF/2026_WGY_Investment_Policy-FINAL.txt`
line n. `SMD:n` = `OFF/smapply_public_2026-10-14/deliverables.txt`. `SMF:n` = `OFF/smapply_public_2026-10-14/faqs.txt`.
`OPS` = `oct20/ops/operating_plan.md` (with the verifier fixes in `oct20/verify_admin/verify_admin.md` §1b). `QV2` =
`oct20/askwharton2/questions_v2.md`. `U19` = `oct19/out/Caplet_Update_19Oct2026.md`. `VK2` = `oct20/verify_tnakit2/verify_tnakit2.md`. `K2c` =
`oct20/verify_tnakit2/tna_fact_kits_v2_checked.md`. `AIR` = `oct20/ailog/ai_use_register.md` / `.csv`. `GYF`, `CU`,
`RR` = `oct20/askwharton2/web/gy_faq.txt`, `contactus.txt`, `rules_roles.txt` (live 19 Oct 22:40 UTC).
Help pages fetched live with plain curl and a cache-busting query on **19 Oct 2026 23:08-23:10 UTC (Tue 20 Oct
10:08-10:10 Sydney)**, all HTTP 200, saved as text in `RB/web/` (log: `RB/web/fetch_log.txt`):
- **G-SUG** Suggest edits in Google Docs, https://support.google.com/docs/answer/6033474 (`gdocs_suggest.txt`)
- **G-TAB** Use document tabs in Google Docs, https://support.google.com/docs/answer/15499791 (`g_15499791.txt`)
- **G-VER** Find what's changed in a file (version history), https://support.google.com/docs/answer/190843 (`gdocs_versions.txt`)
- **G-DL** Create, view, or download a file, https://support.google.com/docs/answer/49114 (`g_49114.txt`)
- **G-PRN** Print a file, https://support.google.com/docs/answer/143346 (`g_143346.txt`)
- **G-WC** Count the words in a document, https://support.google.com/docs/answer/39003 (`gdocs_wordcount.txt`)
- **G-PG** Pages or pageless, https://support.google.com/docs/answer/11528737; **G-PS** Change page settings, https://support.google.com/docs/answer/10296604; **G-FMT** Paragraphs & fonts, https://support.google.com/docs/answer/1663349; **G-HF** Headers, footers & footnotes, https://support.google.com/docs/answer/86629; **G-KEY** Keyboard shortcuts, https://support.google.com/docs/answer/179738; **G-CMT** Comments, https://support.google.com/docs/answer/65129
- **SMA** SurveyMonkey Apply "Completing an Application FAQ", https://help.surveymonkey.com/en/apply/faqs/application-faq/ (`smapply_appfaq.txt`, page dated "February 2026")

Line numbers below (e.g. G-SUG:44-49) refer to those `.txt` files.

---

## 0. Read this first: five things that change what the team does

1. **The TNA has no published format rule.** TNA:40-54 lists only: three notes from executed WInS trades, each quoted
   "exactly as it appears in WInS" (TNA:44), a reflection of "100 words or fewer" each (TNA:46), submitted "via the
   SurveyMonkey Apply form" (TNA:54). Times New Roman 12, double spacing, a title page, "First Name, Last Initial" and
   the 5 MB PDF limit are **IPS rules** (IPS:84-123). They are not TNA rules. If the TNA form asks for an upload, use
   the IPS format as a house style. That is the team's choice, not a Wharton rule, so do not say it is one.
2. **On SurveyMonkey Apply, "Mark as Complete" and "Submit" are different buttons. [fixed 20 Oct]** "If you have
   previously pressed Marked as Complete on a form, but have not yet Submitted your application, you can choose to make
   Edits to your task" (SMA:233). Submitting is a separate step: "select Review & Submit ... click to Submit Your
   Application" (SMA:208-210). It is only possible once "you ... complete all required tasks within your application"
   (SMA:205). And "It's not possible to delete an application after you submit" (SMA:191). Sites can have several
   applicant stages. A new stage comes with the automation "On submit -> Move to stage" by default, and once an
   application has moved on at submit, "the applicants will no longer be able to make edits" (SMApply help "How to Set Up
   an Application Stage", `oct20/verify_runbook/web/sma_app-stage.txt`). So **one Submit on 22 Oct is unlikely to lock
   the IPS and Final Report.** If they are required tasks in the same stage, Submit stays blocked until they are done.
   If they sit in later stages, Submit moves the application on to them. The real risk runs **both ways**: (a) pressing
   Submit too early, which locks the TNA text; (b) **not pressing a Submit that is the TNA's real submission**, so the
   TNA is never delivered. How Wharton set this up is **UNVERIFIED** until the form is opened. **Self-check C (QV2 §3)
   must happen before Thursday**, together with the roster evidence (§3.5 item 7). Use the decision rule in §3.5.
3. **Suggestions print. Comments: unknown.** The 19 Oct whole-Doc PDF export printed both wordings in suggestion green
   (`verify_admin.md` C1). No Google page fetched says whether a PDF download prints comments: **UNVERIFIED**. So
   accept or reject every suggestion, resolve every comment, export **one tab**, then check the PDF itself
   (`tools/pdfgate.py` plus a person reading it on a second device). The IPS Report Doc is still unchanged since
   18 Oct 00:49:32 UTC (Drive metadata re-read 20 Oct 10:15 Sydney), so the 10 v12 suggestions are still pending.
4. **Never use "Delete history" and never start a clean copy with "Make a copy".** Google lets the owner delete
   version history ("Deleting version history is permanent and cannot be undone", G-VER:66-67, 69). Version history is the
   team's evidence of who typed what. A copy is a new file; Google's pages do not say that version history comes
   with it (only comments and suggestions are offered, G-DL:59), so treat a copy as having **no history**
   (UNVERIFIED). Move the AI text **out**, and leave the students' writing where it was typed.
5. **Submitting Thursday evening Sydney gives Wharton two working days to fix a problem.** Thu 22 Oct 20:00 Sydney
   is Thu 05:00 ET. Wharton's Thursday and Friday working days (hours **UNVERIFIED**; 9 am-5 pm ET assumed) run
   Fri 00:00-08:00 and Sat 00:00-08:00 Sydney (§2). A Saturday-morning submit leaves none, and "We will not grant any
   deadline extensions" (SMD:29) [fixed 20 Oct: was SMD:31].

---

## 1. Roles on submit days (from OPS §1, with the verifier's fixes)

| Role | Who | Submit-day job | Cannot also be |
|---|---|---|---|
| **Submitter** | **Ray (team leader)**. "The student team leader is responsible for submitting all team deliverables via our designated submission platform. They must be at least 16 years of age in order to comply with the platform's terms of use." (GYF:252; also RR:230) | Logs into SMApply on their own device and account; pastes or uploads; presses the buttons; takes the confirmation screenshots | the paste checker; the deputy |
| **Deputy / submit watcher** | picked at M1 (DL-02) | Watches the whole submit on screen-share; reads each checklist line aloud; holds the clock; keeps the failure-mode table (§3.7) open | the leader; the historian (OPS fix: "deputy ≠ historian", because the deputy chairs when the leader is away and "historian ≠ chair") |
| **Paste & numbers checker** | picked at M1 (DL-04) | Copies the three notes fresh from the WInS Trade Notes page; runs `textcheck.py --compare`; checks ticker, ET time and key phrase; copies the text back out of the form and re-checks | the submitter; the author of any text checked (OPS:72) |
| **Editor** | picked at M1 | Owns the Doc; names versions; rejects or accepts suggestions; moves AI text out; runs the word counts (counter 1) and `provenance.py`; exports the PDF | - |
| **Rules & format lead** | picked at M1 | Form screenshots (self-check C); runs `pdfgate.py`; checks the rules list (TNA:42-53; IPS:84-123); second word counter | - |
| **Historian / AI-log keeper** | picked at M1 | Completes the AI-use rows (§3.6) before the approve vote; logs DL-15/16 (TNA) and DL-36/38 (IPS) with times | the chair |
| **Authors** (one per reflection; IPS paragraph owners) | DL-04, DL-17 | Confirm in the decision log "written by me from my own notes"; fix only what a check flags, in their own words | the paste checker or scorer of their own text |
| **Advisor & school liaison** | picked at M1 | On standby: if the leader cannot submit, the advisor contacts Wharton through Contact Us at once (OPS R2) | - |

Other fixes from `verify_admin.md` §1b that touch these days: the backup trader is not the trade-log keeper (P2).
"Don't use AI for personal reflection" (AIP:465 in the 19 Oct copy) is Wharton advice for Pre-baccalaureate courses,
not a competition rule (P3); the competition rule is AIP:377 ("You may not submit any work generated by an AI
program as your own"). The Thu 5 Nov 09:00 IPS text lock falls during the HSC Physics exam (9:25-12:30). Anyone
sitting it does the lock tasks the evening before or hands them to their backup (P7; whether any member sits the HSC
is UNVERIFIED).

**Two-person rule on submit day:** nothing is pasted, exported or submitted unless a second named person watches it
happen and ticks it here.

---

## 2. Time-zone table (Python `zoneinfo`, `RB/tools/tz_table.py`; output saved in `RB/tests/tz_table_out.md`)

| Deliverable | Event | Sydney | US Eastern | UTC | Hours to deadline |
|---|---|---|---|---|---|
| TNA | Text lock | Thu 22 Oct 16:00 AEDT | Thu 22 Oct 01:00 EDT | Thu 22 Oct 05:00 UTC | +40.0 |
| TNA | Paste and word-count gate ends | Thu 22 Oct 18:30 AEDT | Thu 22 Oct 03:30 EDT | Thu 22 Oct 07:30 UTC | +37.5 |
| TNA | M3 starts (submit on screen-share) | Thu 22 Oct 19:00 AEDT | Thu 22 Oct 04:00 EDT | Thu 22 Oct 08:00 UTC | +37.0 |
| TNA | **Team submit target** | **Thu 22 Oct 20:00 AEDT** | Thu 22 Oct 05:00 EDT | Thu 22 Oct 09:00 UTC | +36.0 |
| TNA | Wharton Thu working day starts (hours UNVERIFIED, 9 am ET) | Fri 23 Oct 00:00 AEDT | Thu 22 Oct 09:00 EDT | Thu 22 Oct 13:00 UTC | +32.0 |
| TNA | Wharton Thu working day ends (UNVERIFIED, 5 pm ET) | Fri 23 Oct 08:00 AEDT | Thu 22 Oct 17:00 EDT | Thu 22 Oct 21:00 UTC | +24.0 |
| TNA | Fallback: absolute latest team submit | Fri 23 Oct 18:00 AEDT | Fri 23 Oct 03:00 EDT | Fri 23 Oct 07:00 UTC | +14.0 |
| TNA | Wharton Fri working day starts (UNVERIFIED, 9 am ET) | Sat 24 Oct 00:00 AEDT | Fri 23 Oct 09:00 EDT | Fri 23 Oct 13:00 UTC | +8.0 |
| TNA | **Wharton deadline 5:00 pm ET** (SMD:22) | **Sat 24 Oct 08:00 AEDT** | Fri 23 Oct 17:00 EDT | Fri 23 Oct 21:00 UTC | 0 |
| TNA | Status re-check | Sat 24 Oct 09:00 AEDT | Fri 23 Oct 18:00 EDT | Fri 23 Oct 22:00 UTC | -1.0 |
| IPS | US clocks go back (02:00 EDT becomes 01:00 EST) | Sun 01 Nov 17:00 AEDT | Sun 01 Nov 01:00 EST | Sun 01 Nov 06:00 UTC | +136.0 |
| IPS | Format gate on exported PDF (M8 pre-read) | Tue 03 Nov 18:00 AEDT | Tue 03 Nov 02:00 EST | Tue 03 Nov 07:00 UTC | +87.0 |
| IPS | Last fallback WInS order: Wed 4 Nov ET close | Thu 05 Nov 08:00 AEDT | Wed 04 Nov 16:00 EST | Wed 04 Nov 21:00 UTC | +49.0 |
| IPS | Text lock | Thu 05 Nov 09:00 AEDT | Wed 04 Nov 17:00 EST | Wed 04 Nov 22:00 UTC | +48.0 |
| IPS | M9 starts (submit on screen-share) | Thu 05 Nov 19:00 AEDT | Thu 05 Nov 03:00 EST | Thu 05 Nov 08:00 UTC | +38.0 |
| IPS | **Team submit target** | **Thu 05 Nov 20:00 AEDT** | Thu 05 Nov 04:00 EST | Thu 05 Nov 09:00 UTC | +37.0 |
| IPS | Wharton Thu working day starts (UNVERIFIED, 9 am ET) | Fri 06 Nov 01:00 AEDT | Thu 05 Nov 09:00 EST | Thu 05 Nov 14:00 UTC | +32.0 |
| IPS | Wharton Thu working day ends (UNVERIFIED, 5 pm ET) | Fri 06 Nov 09:00 AEDT | Thu 05 Nov 17:00 EST | Thu 05 Nov 22:00 UTC | +24.0 |
| IPS | Fallback: absolute latest team submit | Fri 06 Nov 18:00 AEDT | Fri 06 Nov 02:00 EST | Fri 06 Nov 07:00 UTC | +15.0 |
| IPS | Wharton Fri working day starts (UNVERIFIED, 9 am ET) | Sat 07 Nov 01:00 AEDT | Fri 06 Nov 09:00 EST | Fri 06 Nov 14:00 UTC | +8.0 |
| IPS | WInS market close, trading ends (4:00 pm ET; exact freeze time UNVERIFIED) | Sat 07 Nov 08:00 AEDT | Fri 06 Nov 16:00 EST | Fri 06 Nov 21:00 UTC | +1.0 |
| IPS | **Wharton deadline 5:00 pm ET** (SMD:23) | **Sat 07 Nov 09:00 AEDT** | Fri 06 Nov 17:00 EST | Fri 06 Nov 22:00 UTC | 0 |
| IPS | Status re-check | Sat 07 Nov 09:30 AEDT | Fri 06 Nov 17:30 EST | Fri 06 Nov 22:30 UTC | -0.5 |

Offsets: Sydney is 15 h ahead of New York until Sun 1 Nov 16:59 Sydney and 16 h ahead from 17:00 (script probe).
These match OPS §7 and the verifier (`verify_admin.md` §2b). Rule: write every time as **Sydney first, ET in
brackets**. Quote WInS order times **in ET exactly as WInS shows them** (K2c:745).

---

## 3. Shared mechanics (both runbooks use these)

### 3.1 Google Docs

**a. Before anyone touches the Doc: name a version (editor).**
Last edit (top right) → choose the current version → More → **Name this version** (G-VER:56-61). Names: "Before
clean-up 20 Oct", "TNA text lock 22 Oct 16:00", "IPS text lock 5 Nov 09:00". Named versions "aren't merged"
(G-VER:57), and "Delete all versions" removes only versions "that have not been explicitly named" (G-VER:69).
Limit: 40 named versions per document (G-VER:62). You need edit permission to see history (G-VER:30).

**b. Reject or accept ALL suggestions (editor, deputy watching; a person clicks, no AI tool).**
Google's steps (G-SUG:44-49): "Click Tools Review suggested edits. A box will appear in the top right. To preview
what your document will look like with or without the changes, click the Down arrow and choose an option. Click
Accept all or Reject all." One at a time: open the suggestion card, then "Click Accept or Reject" (G-SUG:39-42).
- Use the preview in the box first ("with or without the changes") to confirm what remains.
- **Scope with tabs is UNVERIFIED** (re-checked 20 Oct: G-SUG:44-49 and G-TAB say nothing about it, and a web search
  of Google's help found nothing either). So open each tab that held suggestions ("Version 5", "Trading Note
  Reflection") and run it there. Done when Tools → Review suggested edits shows no suggestions on every tab.
- **[fixed 20 Oct] Guard before any "Reject all" or "Accept all":** it may act on **the whole document**, every tab
  included. So first open the Comments panel ("To see all edits, go to the top right and click Comments", G-SUG:43).
  List every pending suggestion with its author and tab. Settle each **student** suggestion one at a time (G-SUG:39-42),
  with its author deciding. Then name a version (3.1a). Only after that, press Reject all for the AI suggestions.
- **For the 20 Oct clean-up** (OPS DL-05; U19 §3a item 2): **Reject all** the 10 pending v12 suggestions. That leaves
  the accepted V5 text, which is still AI text (exemplar v11, `oct19/out/Caplet_Update_19Oct2026.md` §4a), so step c
  must follow. Never "just strip the [AI] tag" (U19 §3a item 2).
- **On lock days**, the Doc must hold **zero** suggestions. If a student made a suggestion in Suggesting mode, its
  author decides and the editor accepts or rejects it, then names a version.

**c. Move AI text out without losing version history (editor, deputy watching).**
Version history belongs to the document, and it keeps the deleted AI text and who inserted it. Nothing in the
options below loses it, as long as nobody uses Delete history (G-VER:66-80). **[fixed 20 Oct]** Google's only
history-clearing warning about restoring is for **spreadsheets** (G-VER:46). Avoid "Restore this version" because it
brings back old text over the students' work, not because it erases history. Note that "The revisions for your file may
occasionally be merged" (G-VER:94). Named versions "aren't merged" (G-VER:57), so name a version at every milestone.

| Option | Steps | For | Against |
|---|---|---|---|
| **1 (recommended for submission safety): separate file** | (1) Name a version (a). (2) In Drive, create a new Doc titled "AI reference - do not copy (AI, not for submission)" in the AI Outputs folder. (3) In the IPS Report Doc, select the AI text (accepted V5 body; the three "[AI]" reflections, tag included) → Copy → paste into the new Doc under a heading that says which tab and version it came from. (4) Back in the IPS Report Doc, delete that AI text. (5) Name a version "AI text moved out 20 Oct". | An "All tabs" export, or exporting the wrong tab, can no longer print AI text. Authors are not one click away from it | Two files to manage |
| 2: AI-reference tab in the same Doc | Switch to **Editing** mode first, because "In suggestion mode, you can view tabs, but you can't add, move, or remove them" (G-TAB:35). Show tabs & outlines → Add tab (G-TAB:26-30), or Tab options → Duplicate on "Version 5" (G-TAB:53-60). Rename it "AI reference - do not copy" (G-TAB:62-70). Move the AI text there and delete it from the writing tabs. Name a version | Everything stays in one file and one history | A download with "All Tabs" prints it (G-TAB:85-90); the AI text stays next to the writing |

Rules for either option:
- Students write **in a tab that holds no AI text, signed in as themselves**, so the history shows who typed what
  (OPS §5A). Don't paste big blocks from elsewhere.
- **Do not** use File → Make a copy to get a "clean" Doc for the students' text. Google says only that comments and
  suggestions can be copied (G-DL:54-59), and a copy is a new file, so treat it as having no history (UNVERIFIED).
- **Do not** use Delete history ("Deleting version history is permanent and cannot be undone", G-VER:66-67; only the
  file owner can, G-VER:66). Do not use "Restore this version" (G-VER:41-45) on the deliverable Doc either, because it
  overwrites the students' current text [fixed 20 Oct].
- If the team voted (DL-05) to delete the AI text instead of keeping a copy, delete it in the Doc. History still
  holds it. Never keep the AI text with the "[AI]" label removed.

**d. Format settings (IPS; TNA only if uploaded, as house style).**
- **[fixed 20 Oct]** Wharton: "Formatting choices not specified below are left to the team's discretion" (IPS:101-102).
  Paper size and the no-header rule below are the team's choices, not Wharton rules. Say so if anyone asks.
- File → Page setup → **Pages** (not Pageless) (G-PG:27-29). Do this before the header/footer check. In a pageless Doc,
  headers, footers and footnotes left over from Pages format are hidden but "will still print" (G-PRN:32; G-PG:33). Margins "aren't available in documents that are in
  pageless format" (G-PS:23). Set margins to 1 inch on all four sides and paper size to Letter (G-PS:26-35). The 19 Oct V5
  pages were already Letter with 1-inch margins (U19 §4a). Whether page setup is per tab or per document is UNVERIFIED,
  so check the exported PDF.
- Font: Times New Roman 12 for every line, headings included.
- Format → Line & paragraph spacing → **Double** (G-FMT:45-52), applied to every paragraph (select all first).
- No header, footer, page-number text or footnotes. Footnotes are banned (IPS:123). No header, footer or page number
  is a house rule (IPS:101-102). Docs word count also leaves out
  "headers, footers, and footnotes" (G-WC:26), so text there would escape the count.
- No "Help me write"/Gemini or rewrite features on (OPS §5A).

**e. Export ONE tab to PDF and confirm nothing extra prints (editor exports; rules lead checks).**
1. Open the submission tab. Tools → Review suggested edits shows no suggestions. Comments: resolve every open
   comment on that tab ("Resolved comments remain accessible in your original document", G-CMT:84).
2. File → Download → **PDF Document**. "When you download or print in Google Docs, you must choose the current tab
   or all tabs ... In the dialog that opens, the default is 'Current Tab.' ... Click Export." (G-TAB:85-90). Leave it
   on **Current Tab**. Fallback: File → Print → "Print current tab", Destination "Save as PDF" (G-TAB:92-94;
   G-DL:68-72).
3. Name the file plainly, for example `Caplet_IPS_2026-11-05.pdf`. Use no personal data in the name.
4. Run the PDF gate (§3.4). With `--locked`, it compares every word in the PDF with the locked text. Printed
   suggestions show up as extra words, and a wrong tab as different words.
5. **Second device.** The rules lead opens the PDF on a different device and app (for example a phone's PDF viewer,
   not the laptop that exported it). They read every page and tick: no coloured or struck-through text; no comment
   bubbles or margin notes; no "[AI]"; page count; title page; the end of the text is not cut off. They also search
   the PDF for a word that appears only in a comment or a rejected suggestion. It must not be found.

### 3.2 Word counting (two counters, two people, strictest result wins)

**Counter 1: `textcheck.py`** (`/home/user/snap/main/office/tools/textcheck.py`; in the repo at `keel/office/tools/textcheck.py`).
It is read-only and uses the standard library only. Read before use:
- It prints two counts: "by spaces" (runs of non-whitespace, :27-29) and "strict" (also splits on hyphens, slashes
  and en/em dashes, :32-34). With `--limit` it judges on the **larger** of the two (:80-83).
- It also reports the character count, every non-ASCII character (:37-39, :89-92) and its own overclaim words (:21-24).
  It does exact-match checking with `--compare` (:99-108).
- A trailing newline is ignored, but trailing spaces are not (:63).
- Its overclaim list is shorter than the kit's banned-word list (K2c:750: guaranteed, risk-free, safe, locked,
  secured/secures, promised, never, cannot miss, matched, owns/owned, triggered, gift, building). Run a grep for the kit list as well:
  `tr '\n' ' ' < final.txt | grep -o -i -w -E "guaranteed|risk-free|safe|locked|secured|secures|promised|never|cannot miss|matched|owns|owned|triggered|gift|building"`
  [fixed 20 Oct: the line-by-line grep missed "cannot / miss" split across two lines; tested in `oct20/verify_runbook/tests/grep_sample.txt`]

How it counts (tested 20 Oct, `RB/tests`):

| Text | by spaces | strict |
|---|---|---|
| co-sponsors | 1 | 2 |
| 2033-2042 | 1 | 2 |
| IBTM/IBTR | 1 | 2 |
| rates—and (no spaces) | 1 | 2 |
| rates — and (spaced dash) | 3 | 2 |
| $50,000 / 5.1% / U.S. | 1 each | 1 each |
| 1 Jan 2037 | 3 | 3 |
| Investment Strategy Elevator Pitch (heading) | 4 | 4 |
| Investment Policy Statement (heading) | 3 | 3 |

**Counter 2: Google Docs, Tools → Word count, on a selection** (G-WC:26, 30). Select exactly the text being counted.
"Unless you select a section of the document, word count applies to everything except headers, footers, and
footnotes" (G-WC:26). Google does not say how it counts hyphens, slashes or dashes: **UNVERIFIED**.

**Defaults (QV2 Q2, strictest reading, until Wharton answers in writing):**
- Headings count. Hyphenated words split. Each number is one word, and a range such as 2033-2042 is two (strict).
- **Pitch:** 50 or fewer **including** the heading "Investment Strategy Elevator Pitch" (4 words). Target 45.
- **IPS:** 500 or fewer **including** "Investment Policy Statement" (3 words) and every sub-heading. Target 470.
- **TNA reflection:** 100 or fewer (TNA:46). The quoted note is not counted, because the limit is on "a reflection".
  That is a reading of the text, so keep a margin: **target 95**.
- The title page is not part of the pitch or IPS count (IPS:84-109).
- Two people count each text, one with each counter. Record both numbers in the decision log. **If counts differ,
  cut to the highest count** (the strictest reading; OPS R9's mitigation cell literally says "Cut to the lower count",
  which reads the other way. Fix OPS R9 to match, [fixed 20 Oct]).

### 3.3 AI provenance check (5-word runs; `RB/tools/provenance.py`, tested)

`oct19/exemplars/overlap.py` exists but is hard-wired to the 19 Oct IPS Doc files (its lines 18-25 read fixed file
names), so it cannot check a new text. `provenance.py` is a general version of the same method. It uses the
standard library only, and it accepts any final text and any AI files or folders (.txt/.md/.csv/.html/.docx).

```
python3 provenance.py final_reflection_IBTM.txt \
  --ai AI_corpus/ \
  --allow wins_notes/ --allow competition/official/2026_27/
```

- **Output:** coverage %, then each shared span marked **FLAG** (shared with an AI file and not in an allowed file)
  or **ALLOWED** (also in an allowed file, for example the WInS note the TNA must quote, TNA:44). Each span names the
  AI file and line it came from. Exit code 0 means CLEAN; 1 means at least one FLAG.
- **Tests run 20 Oct (`RB/tests/`):**
  - The accepted "[AI]" VT reflection against the exemplar versions: 100% covered, one 87-word FLAG traced to v12
    `1ed9130.md:52`. Expected, since it is exemplar v11/v12 text.
  - The same text with curly apostrophes and an em dash: same result, so normalisation works.
  - The .docx reader: same result.
  - The executed WInS VT note against the Sheet's exemplar notes: 44% covered, including the 11-word run "a rise
    before 2031 lifts the top of the range co-sponsors" (the known AI overlap, AIR R12, R21).
  - The note plus the AI reflection with `--allow` set to the note: the note's spans are ALLOWED and the reflection is FLAGGED.
  - Negative controls (lorem ipsum; the official TNA instructions): CLEAN.
  - A 489-file corpus ran in 2.9 s.
  - **[fixed 20 Oct] Reader defect found by the verifier:** in `.docx` AI files, `<w:tab/>` and `<w:br/>` glued words
    together and `&amp;` stayed as text. In `.html` AI files, tags and entities stayed in the words. Matches next to
    them were missed (docx test: 9 of 16 copied words caught; html: 9 of 13). Use
    `oct20/verify_runbook/provenance_fixed.py` (diff in `provenance_fix.diff`; 16/16 and 13/13 caught; the runbook's own
    tests give the same results). Or convert every AI file to .txt first.
- **What counts as the AI corpus** (gather on Wed 21 Oct; save everything as .txt or .docx in one private folder,
  never in the public repo):
  1. IPS Report Doc tabs, each via File → Download → Plain text with "Current Tab": Version 5 (the accepted text,
     and also the text with all suggestions accepted, using the preview of step 3.1b), Trading Note Reflection ([AI]
     reflections), V1, V2, V3, V4, Tab 10, Tab 15. If option 1 of 3.1c is used, the "AI reference" Doc.
  2. Drive "AI Outputs" folder: exemplar .docx v3, v7, v12, v13, v14; trading_notes_pack, ips_spec, why_us,
     strategy_changes, securities_and_allocation, open_questions.
  3. Sheet "Portfolio and Trading Notes": the Trading Notes tab via File → Download → CSV (the "Exemplar note" and
     "Proposed note - AI draft" columns), and R&B Tickets.
  4. The repo, cloned: `keel/library/`, `archive/rab/`, `caplet/ai_outputs/`, `keel/office/`, `toolkit/docs/`, and the unmerged branch file
     `keel/library/blueprints/04_exemplar_ips_tna_17Oct.md` on `claude/trusting-euler-gms43m` (exemplar v1-v12).
  5. The 19-20 Oct AI packs (TNA fact kits, IPS writing kit, update, Q&A bank and so on), saved as text.
  6. Every student's own AI chats about the competition, each copied into a .txt file.
- **Allowed** (`--allow`): a folder holding the three WInS notes exactly as copied from WInS, plus the official files
  `competition/official/2026_27/*.txt`. Matching official words is quoting the rules, not AI wording. A long quote of
  the rules in a reflection is still a content question for the scorers.
- **Rule** (OPS §5B step 9): every FLAG span that is not an official quote goes back to its author, who rewrites it
  **from their own notes** or cuts it. **Cutting is the safe fix on submit day.** Never ask an AI to reword it, and
  never "humanise" it. A proper name (for example "iShares iBonds Dec 2032 Term Treasury ETF") may stay. The editor
  writes "proper name, kept" next to it in the log. A CLEAN result does not prove authorship, and a FLAG does not
  prove copying. The script is a tripwire. The authors' sign-off and the version history are the record.

### 3.4 PDF gate (`RB/tools/pdfgate.py`, tested; needs `pypdf`, which is in the scratchpad venv)

```
python3 pdfgate.py Caplet_IPS.pdf --max-pages 3 --locked ips_locked.txt     # IPS
python3 pdfgate.py Caplet_TNA.pdf --locked tna_locked.txt                   # TNA, only if uploaded
```
- **Checks:**
  - Size against 5 MB. It reports both 5,000,000 bytes and 5 MiB and passes only under the stricter
    (IPS:122 "Maximum file size: 5 MB").
  - Not encrypted. SMApply "won't accept encrypted files" (SMA:257).
  - Page count. Page size. Fonts actually used are Times.
  - Every text run is 12 pt. The median line gap is at least 22 pt: single-spaced Times 12 is about 13.8 pt and
    double about 27.6 pt, so 1.5 spacing (about 20.7 pt) fails.
  - Text no closer than 1 inch to the left, top and bottom edges. No images. No link annotations. No "http"/"www"
    text. No "[AI]".
  - With `--locked`, PDF words = locked words, title-page lines included.
- **Tests (20 Oct):**
  - A Times 12, double-spaced, 1-inch PDF passes every check and exits 0.
  - A Helvetica 11, single-spaced, 0.7-inch PDF with a link, a URL, an "[AI]" tag and four extra words fails 9
    checks and exits 1.
  - An encrypted PDF is stopped.
  - The official IPS instruction PDF (6 pages, Whitney font) fails as it should.
- **[fixed 20 Oct]** The top-margin check uses the first **baseline**, so it lets text start about 0.13 in (the height
  of a capital) inside the 1-inch margin. The script's docstring also lists a right-margin check that the code does not
  do. Re-tested 20 Oct on hand-built PDFs that use Skia-style flipped and scaled matrices, like Google's exporter: font
  size, line gap and margins read correctly in all 5 variants. A real Docs export is still untested (§6).
- **It cannot see** colour, comments or the right margin. The second-device read (3.1e step 5) is still required.
  The line-spacing check is a heuristic. The Docs "Double" setting is the real check.

### 3.5 SurveyMonkey Apply mechanics

**What SurveyMonkey Apply's own help says (SMA, fetched 20 Oct):**
- **Submit is an application-level step.** "To be able to submit your application you will first need to complete
  all required tasks within your application. Additionally, you will need to ensure that you've verified your
  email." "Within the application to submit, select Review & Submit ... Once you've reviewed all your completed
  tasks, you can click to Submit Your Application." (SMA:205-210)
- **Mark as Complete is a task-level step.** You can edit a completed task "If you have previously pressed Marked as
  Complete on a form, but have not yet Submitted your application" (SMA:233). The steps are: task → More Options (...)
  → Edit → Previous/Next → "press Mark as Complete" again (SMA:234-239).
- **Why a task cannot be edited:** "The deadline has passed ...", "You've completed your task and the administrators
  don't wish for you to be able to make changes.", "Your application is locked." Then "Contact the administrator of
  the site" (SMA:242-247).
- **After submitting:** "It's not possible to delete an application after you submit." (SMA:191)
- **Preview and download:** More Options (...) → Preview, or Download (SMA:212-231). **Use Download to keep a copy of
  exactly what was submitted.**
- **Upload errors:** "The file is in an incompatible format." / "The file is too large." / "You've reached the file
  upload limit." / "The file is encrypted ... won't accept encrypted files" / "The file is corrupted. Save the file
  to a different folder on your computer and try the upload again." / "the task settings don't allow editing"
  (SMA:248-261).
- **Confirmation email:** "A confirmation email is part of the configuration of the site set by the administrators.
  If you submit your application and haven't received an email, check your spam/junk folder." (SMA:277-278). Add
  the platform's no-reply sender (SMA:312) to safe senders. Verify the account email: an unverified email can block
  submission (SMA:205-206) and other emails (SMA:313).
- **Deadline passed:** "The administrators may set deadlines when they wish to restrict access to the application
  after that date." (SMA:265)

**Wharton's own pages:**
- "All deliverables must be submitted via your team's SurveyMonkey Apply account." (SMD:28) [fixed 20 Oct: was SMD:30]
- "We will not grant any deadline extensions." (SMD:29) [fixed 20 Oct: was SMD:31]
- "Your team will submit their trading notes via the SurveyMonkey Apply form." (TNA:54)
- The IPS goes in "as a PDF through SurveyMonkey Apply" with a "Maximum file size: 5 MB" (IPS:120-122).
- Every SMApply page header has "Contact the site administrator" and "Ask questions about a program or application
  on this site", both opening email (SMD:3-6).

**UNVERIFIED until the leader opens the forms (self-check C, QV2 §3, due Tue 20 Oct; screenshot every screen):**
1. Whether the TNA, IPS and Final Report are tasks in **one** application or separate ones, and whether "Review &
   Submit" exists now. This also tells you whether a submit on 22 Oct could lock the later tasks.
2. Whether the TNA task takes text boxes (how many; any character limit; separate ticker, date or time fields) or a
   file upload (which types; size limit).
3. Whether "Mark as Complete" is the TNA's final step, or "Submit" is.
4. Whether a completed task can be reopened before the deadline (QV2 Q5).
5. Whether a confirmation message or email appears.
6. Whether there is a place for an AI-use line (QV2 Q1), and whether there is any AI, integrity, "own work" or terms checkbox or statement on the TNA task or the submitted roster task: screenshot its exact text; do not tick it before the vote [consistency fix 20 Oct, G3].
7. The roster was already submitted ("Roster submitted (locked)", `/home/user/caplet-investment/CLAUDE.md` Current
   status). **The leader writes down which buttons that took and what the My Applications page shows now.** It is
   the best evidence of how this site is set up.

**Decision rule for 22 Oct (default unless the form or Wharton says otherwise) [fixed 20 Oct]:**
- **Read the status first.** On the application's task list, note for each of TNA, IPS and Final Report: visible or
  not; "Not started", "Complete" or "The task cannot be started at this time" (SMA:242-243). Note whether
  "Review & Submit" is shown and whether it is active. Screenshot all of it.
- **Case 1: the TNA is the only open task, and Review & Submit is active.** IPS and Final Report are not listed, or
  show "cannot be started at this time", or sit under a later stage. That Submit **is** the TNA submission. Press it
  after A11. Not pressing it risks a TNA that was never delivered.
- **Case 2: Review & Submit is not shown, or is blocked because IPS/FR tasks are required and incomplete.** Then
  "Mark as Complete" on the TNA task is the only action the platform allows, and it is the submission step. Press it.
  Check that the TNA task's status changes to complete. In the same session, send Contact Us: "TNA marked complete;
  please confirm it is received" (QV2 Q5).
- **Case 3: IPS/FR tasks are open and editable now, and Review & Submit is also active.** This means they are optional,
  so a Submit could lock them. Press only "Mark as Complete" on the TNA. Ask Wharton (QV2 Q5) at once and decide at M3
  from the answer. With no answer, the team votes at M3 and logs the vote and the reason (DL-15).
- In every case: if the form's own wording says how the TNA is submitted, follow the form. If the TNA is its own
  application, complete it and Submit.
- **Deadline display:** SMApply shows deadlines "converted to display in the user's time zone" (SMApply help "How to
  Set a Deadline on a Stage", `oct20/verify_runbook/web/sma_stage-deadline.txt`). Check that the form shows Sat 24 Oct
  08:00 Sydney (Fri 5:00 pm ET). If it shows anything else, screenshot it and ask. "Once a deadline for a stage passes,
  users can no longer access or edit the tasks within the stage" (same page).

### 3.6 AI-use log rows to complete first (historian; each student confirms their own rows)

The log columns are OPS §5C. Before any approve vote, the rows below must have **who, what, and what the student did
with it**. "unknown - team to fill" is not allowed in a row that touches the deliverable being submitted. Before
copying from AIR, apply its verifier fixes A1-A11 (`verify_admin.md` §1a). For example, R29 "No row anywhere" becomes
"no row in any caplet/docs/AI_USE.md; recorded only in a branch CLAUDE.md and the PR #9 description" (A1).

| Before | AIR rows | Why it must be done first | Fields still blank today (AIR) |
|---|---|---|---|
| **TNA (by Thu 22 Oct 16:00, DL-16)** | **R12** (30 Sep AI EXAMPLE notes; the WInS notes overlap them: VT 28%, IBTM 30%, IBTR 2%, VK2 #2); **R21** (the 15 executed notes were written with AI examples open); **R19** (6 Oct "AUDIT REVIEW" AI drafts; low overlap, 0-9%) | The TNA must quote these notes exactly (TNA:44), and they cannot be edited. Their AI help can only be disclosed, not removed | who typed each note; which exemplar each writer read; the D6 vote |
| | **R20** (7 Oct AI browser agent on WInS screens; mis-click cancelled the May-2038 order) | The cancelled and re-placed orders appear in the WInS record Wharton checks (TNA:53) | product name; who found the error |
| | **R29** (17-18 Oct AI exemplar v1-v12; the three "[AI]" reflections in the Doc; v12 Doc suggestions) | The current reflection text in the Doc is AI text. The row must say it was moved out or rejected and not submitted (3.1b-c) | what was kept; who accepted the v11 text |
| | **R24, R28, R32, R33**, and this wave's files (TNA fact kits v2, the checked kit, this runbook and its scripts) | These AI reviews and kits informed the TNA (INDIRECT) | what the team did with each |
| | Any AI issues-only check on the drafts (only if DL-01 allows it) | Each prompt and output must be saved (OPS §5B step 8) | - |
| **IPS (by Thu 5 Nov 09:00, DL-36)** | **R03** (Cowork outlines), **R10** (exemplars v3-v14; V1 and V2 tabs), **R17** (V3, V4, V5 of 14 Oct, Tab 10), **R18** (Tab 15, unknown tool), **R27** (16 Oct [AI] suggestions), **R29**, **R31** (WO-0002 IPS memo), plus every oct20 IPS item (IPS kit, ipsfix, rubric, votepack) and any issues-only check | The IPS bans citations (IPS:123), so the log and later the Final Report's Works Cited are the only record (AIR §6.2 item 1) | tool and user for R17 and R18; editor of the v11 cuts |

The disclosure line in the deliverable itself:
- **IPS:** none, because "formal citations are not permitted" (IPS:123).
- **TNA:** a line only if self-check C shows a field for it **and** the team votes for it (QV2 Q1 default).
- Logging AI text does not make it the students' work. The only fix is rewriting it from their own understanding
  (OPS §5C).

### 3.7 Failure modes and what to do

**Standing rule: never resubmit blindly.** Screenshot the problem with the clock visible, then follow the row
below. Contact Us is the Wharton channel ("WHOM DO I CONTACT IF I HAVE A QUESTION ABOUT THE COMPETITION? Please use
the Contact Us form.", SMF:93-94). Its fields are Full Name, Email, Subject Line, Describe your Question/Comment, and
optionally Team Username and Team User ID (CU:203-208). "If you do not see a form above, please turn off your ad
block for this site and refresh the page." (CU:212). The fallback is the SMApply header link "Contact the site
administrator" (SMD:3-4; SMA:266-269).

| Failure | First sign | Do this (who) | Do not |
|---|---|---|---|
| **Form or page error** (won't load, button does nothing, "Whoops! We couldn't find what you were looking for.") | error on screen | Ray: screenshot; reload once; try a second browser, then a second device or network (OPS R17). Turn off ad block. If it still fails, Ray sends Contact Us with the screenshot, the time in ET and Sydney, and the deliverable name. Deputy logs it. Re-try every 2 hours until the Fri 18:00 (TNA) / Fri 6 Nov 18:00 (IPS) fallback | invent a workaround such as emailing the file without being asked |
| **Upload rejected** | SMA:248-261 messages | Rules lead: run `pdfgate.py`. **Too big:** a text-only Docs PDF should be far under 5 MB (the 6-page official IPS PDF is 0.18 MB), so look for an embedded image or a wrong file; re-export the current tab only. **Encrypted:** export again with no password. **Wrong type:** PDF only (IPS:120). **Corrupted:** "Save the file to a different folder ... and try the upload again" (SMA:259) | compress with an online tool (it may rasterise text or add a watermark) |
| **Leader unavailable** (ill, no login, no device) | no reply 24 h before the internal deadline (OPS R2) | Deputy phones the leader and the advisor. The advisor sends Contact Us **at once**, saying the leader cannot submit and asking what the team should do (QV2 Q6). Leader changes need "the Advisor submits a written request due to extenuating circumstances" (RR:218, via QV2 Q6). Keep the locked files ready on two drives | share the leader's SMApply password (the platform terms are why only the leader submits, GYF:252); let anyone else log in as the leader |
| **Typo or wrong file found after Mark as Complete** | anyone | If the application is not yet submitted and the task is editable: task → More Options → Edit → fix → Mark as Complete (SMA:233-239), with the paste checker and deputy re-running every check. If it is locked: Contact Us with the exact error and a corrected file ready. Log it | press application Submit to "fix" it; delete the application (SMA:191-203) |
| **Typo found after Submit** | anyone | Contact Us once, factually, saying what is wrong. Ask whether a correction is accepted. Accept the answer. Log it | resubmit in a new application |
| **"Marked as Complete" but no "Submitted" status**, or the reverse | status screenshot | Compare with the self-check C screenshots and the decision rule (3.5). If still unclear, Contact Us before the Fri 23 Oct 08:00 Sydney end of Wharton's Thursday | guess |
| **No confirmation email** | after submit | Check spam/junk; add the no-reply sender (SMA:312). The **status screenshot plus the downloaded application** is the record. Contact Us only if the status itself is unclear (SMA:277-278) | assume it failed and resubmit |
| **Paste mismatch** (`exact match: NO`) | textcheck | Paste checker: re-copy from the **WInS Trade Notes page** with Ctrl+Shift+V / ⌘+Shift+V ("Paste without formatting", G-KEY:35-36, 430-431; that page lists **Google Docs** shortcuts. In a browser form, Chrome
and Edge also paste plain text with Ctrl+Shift+V, and a plain-text editor pastes plain text anyway; the copy-back check
is the real test [fixed 20 Oct]). Check for curly quotes, non-breaking spaces, a double space, or a trailing space (all shown by the tests in `RB/tests`) | retype the note; "tidy" it; copy it from a Google Doc (K2c:743) |
| **Form changes the text** (strips line breaks, cuts at a character limit, curls quotes) | copy-back check (A11) | If a field limit cuts a note (WInS notes run 288-294 characters), stop. Screenshot it and Contact Us before submitting. Paste the note in full in the field Wharton points to | shorten a note: it must be exact (TNA:44) |
| **Word count over, or counters disagree** | 3.2 | The author cuts (does not rephrase) to the strictest count. Both counters are run again | argue for the looser count |
| **Provenance FLAG at the last minute** | 3.3 | The author cuts the span or rewrites it from their own notes. Re-run 3.2 and 3.3 | ask an AI to reword it |
| **Time confusion** | anyone quoting ET without Sydney | Deputy reads out §2. The deadline is **5:00 pm ET** (SMD:22-23) | use "5 pm" without a zone |
| **Device or internet failure** | - | Use the second device and network (phone hotspot or school network). The locked files are on two drives | wait it out |

---

## 4. Runbook A: Trading Notes Analysis

**Team submit Thu 22 Oct 20:00 Sydney (05:00 EDT). Deadline Sat 24 Oct 08:00 Sydney (Fri 23 Oct 5:00 pm EDT).**
Picks on record (U19 §3a item 3; VK2): IBTM (10/06/2026 10:01:41 PM ET), IBTR (10/07/2026 04:42:53 AM ET, the
re-placed order, **not** the cancelled 10/06 08:31:27 PM one), VT (10/07/2026 08:27:19 PM ET). The picks are voted
at M1 (DL-03).

### A-pre. Gates that must already be done before the 16:00 lock (deputy checks each one off at 15:30)

| # | Gate | Owner | Source |
|---|---|---|---|
| P1 | Self-check C done: TNA form screenshots (fields, buttons, limits, upload or text, task statuses, Review & Submit state); decision rule 3.5 applied; QV2 Q4/Q5 sent if unclear. **Also self-check A [fixed 20 Oct]:** the logged-in Pages → Deliverables page. The Guide says "the complete Trading Notes Analysis Requirements" are there (Guide:92-94), and §0 item 1 rests on the public copy only | rules lead + Ray | QV2 §3 A, C; OPS R7 |
| P2 | Doc clean-up done: v12 suggestions rejected; AI text moved out (3.1b-c); versions named | editor, deputy watching | U19 §3a item 2; DL-05 |
| P3 | Reflections written by their authors in the student tab, signed in as themselves; two non-author scorers have marked them | authors; 2 scorers | OPS §5B |
| P4 | Fill and order times confirmed in WInS Order and Transaction History (self-check J) | trader reads; trade-log keeper records | QV2 §3 J |
| P5 | IBTR number rule applied (no dollar level, or one re-price Thu morning) | rates analyst | OPS §4a; U19 §3a item 8 |
| P6 | Provenance check run once on each draft (3.3); every FLAG resolved by its author | editor | OPS §5B step 9 |
| P7 | AI-use rows for the TNA complete (3.6) | historian; each student | DL-16 |
| P8 | The AI corpus folder exists (3.3); the three WInS reference notes are copied (A3) | editor; paste checker | - |

If P1, P2 or P3 is not done by Thu 12:00, the deputy moves the lock to Fri 23 Oct 12:00 and the submit to Fri 18:00
[fixed 20 Oct: the HSC Maths Extension 1 exam is Fri 23 Oct afternoon (OPS:34). Anyone sitting it hands their fallback
tasks to their backup; whether any member sits it is UNVERIFIED]
(the fallback). Never move it to Saturday.

### A-steps (from "text locked" to "confirmation screenshot saved")

| # | When (Sydney) | Who | How | Done when |
|---|---|---|---|---|
| A1 | **Thu 22 Oct 16:00** | editor | Announce "TNA text locked" in the team chat. Name the version "TNA text lock 22 Oct 16:00" (3.1a). After this, a change is allowed only to fix a failed check, and then the editor names a new version | named version visible in history; chat message posted |
| A2 | 16:00-16:15 | editor; deputy watching | Tools → Review suggested edits on the TNA tab shows none (3.1b). Resolve all comments on that tab. The tab holds no "[AI]" text, no AI-reference text, no kit text | zero suggestions and zero open comments (screenshot) |
| A3 | 16:15-16:45 | **paste checker** (not an author, not Ray) | (1) Open WInS → Trade Notes, read-only. Find each pick by **security + ET order time**. (2) Copy each note with paste-without-formatting into `ref_IBTM.txt`, `ref_IBTR.txt`, `ref_VT.txt`, so the references come from WInS, not the Doc. (3) Copy the note as it stands in the locked TNA text into `paste_IBTM.txt` and so on. (4) Run `python3 keel/office/tools/textcheck.py paste_X.txt --compare ref_X.txt --chars 300` for each | three outputs say **"exact match: YES"** and "non-ASCII characters: 0"; characters **IBTM 292, IBTR 294, VT 288** (re-verified 20 Oct from the 13 Oct WInS copy, `RB/tests`). Outputs saved |
| A4 | same | paste checker; deputy ticks | **Trap checks (length is no proof):** three notes are 288 characters (VT, the cancelled IBTR, the filled Nov-2041 bond) and two are 294 (the filled IBTR and IBTO) (VK2 #1). So tick each: IBTR note has "**about 0.2**" (the cancelled one says "0.3"; the first difference is at character 182) and time **04:42:53 AM**. VT time 08:27:19 PM on 10/07. IBTM time 10:01:41 PM on 10/06. Each prefix kept exactly ("Growth:", "Future funding:", "Future funding and risk management:"). The ET times are written as WInS shows them, labelled as order times, never converted to Sydney time (K2c:745). Ticker and quantity, if the form asks: VT 167, IBTR 853, IBTM 4,503 (K2c:747). Never use the Sheet's "Trade #" values (K2c:748) | all ticks |
| A5 | 16:45-17:15 | editor (counter 1) + rules lead (counter 2) | 3.2: each reflection on its own, without the note. `textcheck.py refl_X.txt --limit 100`, then Docs Tools → Word count on the selection. Kit banned-word grep (3.2) | each reflection **≤ 95** on the strictest count (hard limit 100, TNA:46); both counts logged; 0 banned words, or each one approved by the author with a reason |
| A6 | 17:15-17:45 | rules lead | Rules check against TNA:42-53, one line each: three notes; trades **executed** (filled, not cancelled; TNA:42, 53); note quoted exactly (TNA:44); each reflection says why, how it fits the strategy and how it serves the client's goals, funding needs or risk (TNA:47-52); nothing presented as the final reserve size, projections, facility contribution or co-sponsor text (TNA:20-23 says these are "not expected", so this is a **house check**); no WInS gain, loss or rank (**house check**: TNA:15-16 says the focus is "not simply whether an investment gained or lost value"; K2c:752) [fixed 20 Oct]; consistent with what the IPS will say (TNA:30-31) | each line ticked, with the reflection and line number |
| A7 | 17:45-18:00 | editor | Final provenance run (3.3) on each locked reflection, with `--allow` set to the three ref notes and the official files | **CLEAN**, or every FLAG marked "proper name, kept" by its author. If a FLAG means a cut: cut, name a new version, redo A5 |
| A8 | 18:00-18:30 | editor; rules lead | **Build what the form needs** (from P1). **Text boxes:** one plain-text file per field, holding exactly what will be pasted (the note fields copied from `ref_X.txt`). **Upload:** export the TNA tab to PDF (3.1e), run `pdfgate.py Caplet_TNA.pdf --locked tna_locked.txt`, then do the second-device read. The house style is the IPS format, but no TNA format rule exists (§0 item 1) | files ready in the private Drive submit folder; gate output saved |
| A9 | 18:30 | deputy | Go/no-go. Read A1-A8 aloud. Any open item means no-go and the fallback (Fri 23 Oct; lock 12:00, submit 18:00) | "GO" logged with time |
| A10 | **19:00-19:15 (M3)** | Ray chairs; all | Approve vote (DL-15). Each author says "written by me from my own notes" and it is logged. DL-16: the AI rows are complete (3.6), with any disclosure line decided (QV2 Q1 default: none unless the form has a field and the team votes) | DL-15 and DL-16 logged with the vote |
| A11 | 19:15-19:45 | **Ray submits**; deputy watches on screen-share; paste checker watches | Ray logs into SMApply in a normal browser window, with no AI tool or browser agent running (QV2 Q10 default). Ray opens the TNA task and pastes each field from the A8 files with paste-without-formatting, or uploads the PDF. **Copy-back check:** for each pasted note, Ray selects the text in the form field and copies it back. The paste checker pastes it into `form_X.txt` and runs `--compare ref_X.txt`. Then Preview the application (SMA:212-220) and read it on screen | three "exact match: YES" from the form copy-back; the preview shows the three notes and reflections complete |
| A12 | 19:45-20:00 | **Ray**; deputy reads the rule aloud | Press the button the three-case rule (§3.5) picks: Case 1 **Submit**; Case 2 **Mark as Complete**, then check the status and confirm receipt via Contact Us; Case 3 **Mark as Complete** only, as voted at M3 [fixed 20 Oct, A12 aligned with the three-case rule]. Deputy notes the time | the status shows complete or submitted |
| A13 | by 20:00 | Ray; deputy checks | **Confirmation screenshots:** (1) the message shown after the button; (2) the task list showing the TNA's status; (3) the My Applications page. Keep the computer clock visible. Then More Options → **Download** (SMA:227-231) the application as the copy of record | 3 screenshots + 1 download |
| A14 | by 20:15 | Ray uploads; deputy confirms | Save to the private Drive folder "Submitted/TNA" with names like `TNA_submitted_2026-10-22_2000AEDT_0500EDT_1.png`. A second copy goes to the deputy's drive (OPS R4). Crop any personal email or the WInS username before the files go anywhere except that private folder. **Never commit them to the public repo** | files in two places; **confirmation screenshot saved** = done |
| A15 | by 21:00 | historian | Log DL "TNA submitted", with the time in Sydney and ET, the button pressed, the screenshot file names and the status text | logged |
| A16 | Fri 23 Oct morning, then **Sat 24 Oct 09:00** | Ray | Check email (spam too) for a confirmation. Check the SMApply status is unchanged. If anything looks wrong, use §3.7 | status screenshot added |

---

## 5. Runbook B: IPS

**Team submit Thu 5 Nov 20:00 Sydney (04:00 EST). Deadline Sat 7 Nov 09:00 Sydney (Fri 6 Nov 5:00 pm EST). The
same day ends trading: "IMPORTANT: Trading ends and your portfolio is locked" (SMD:24).** The rule is HARD:
"Submissions that do not meet the requirements below will not be considered for semifinal selection." (IPS:82-83).
After the deadline, "Your team may not revise its investment strategy" (IPS:73-74).

### B-pre. Format gate (Tue 3 Nov 18:00, before M8): every line ticked on the exported PDF

| # | Requirement (exact source) | How to check | Owner |
|---|---|---|---|
| F1 | Page 1 title page, "1 page maximum" (IPS:84-85) | `pdfgate` page 1; read it | rules lead |
| F2 | "Official team name ... the same as what you submitted with your official team roster" (IPS:88-90) | Copy character by character from the roster confirmation (self-check I, due Tue 3 Nov, QV2 §3 I). Not from memory, not from this repo | rules lead + Ray |
| F3 | "Finalized team member names ... the same as what was submitted with your official roster" and "Format: First Name, Last Initial" (IPS:92-96). Sample layout: "Jordan A. \| Taylor B. \| Casey C. \| Morgan D." (IPS:130) | Six names, each first name exactly as on the roster plus last initial and full stop, from the roster confirmation. Order: the roster's (the team leader first is the school letter's rule, `competition/COMPETITION.md` §5; a free choice here) | rules lead |
| F4 | "WInS username ... the team's username for logging into the WInS platform" (IPS:98-100); sample "WInS Username: sample_team-1234567" (IPS:131). "Your team username is NOT the same as your team name" (SMF:32) | Copy from the WInS login screen. **Private:** this line appears only in the PDF sent to SMApply and in the private Drive, never in the public repo | Ray |
| F5 | Pages 2 and 3: "2-page maximum" (IPS:103-104), so **3 pages in all** | `pdfgate --max-pages 3` | rules lead |
| F6 | Pitch "maximum 50 words"; IPS "maximum 500 words" (IPS:107-109; also IPS:33, 39) | 3.2, headings counted: pitch ≤ 45 target, IPS ≤ 470 target, by two people and two counters | editor + rules lead |
| F7 | "Font: Times New Roman", "Size: 12-point", "Spacing: Double-spaced", "Margins: 1 inch on all sides" (IPS:112-118) | 3.1d settings; `pdfgate` fonts, size, line gap and margins; the second-device read. Apply to all three pages, the title page included (strictest reading: the list does not limit itself to pages 2-3) | rules lead |
| F8 | "Submit as a PDF through SurveyMonkey Apply." "Maximum file size: 5 MB." (IPS:120-122) | `pdfgate` size and encryption | rules lead |
| F9 | "Graphics, charts, images, attachments, external links, footnotes, and formal citations are not permitted." (IPS:123) | `pdfgate` images, links and URLs; eye check for footnote numbers, a "Works Cited", "(Source, year)" or "[1]" | rules lead |
| F10 | No suggestions, comments or AI text print (§0 item 3) | `pdfgate --locked` word match; the second-device read (3.1e step 5) | rules lead + one more |
| F11 | Consistent with the TNA as submitted (TNA:30-31; DL M4 "TNA claims the IPS must keep") | Editor reads the submitted TNA download (A13) next to the IPS | editor |
| F12 | The headings used in the sample, "Investment Strategy Elevator Pitch" and "Investment Policy Statement" (IPS:135, 139) | present, and counted in F6 | editor |

### B-steps (from "text locked" to "confirmation screenshot saved")

| # | When (Sydney) | Who | How | Done when |
|---|---|---|---|---|
| B1 | **Thu 5 Nov 09:00** (anyone in the Physics HSC does this Wed evening or hands it to a backup) | editor | Announce "IPS text locked". Name the version "IPS text lock 5 Nov 09:00" (3.1a). After this, changes are allowed only for failed checks | named version; chat message |
| B2 | 09:00-10:00 (or Wed 4 Nov evening) | editor; deputy watching | 3.1b: zero suggestions on the IPS tab. Resolve every comment. Page setup Pages, Letter, 1-inch margins; TNR 12; Double (3.1d). No header or footer text | screenshot of the empty "Review suggested edits" box |
| B3 | Thu 5 Nov 16:00-16:30 | editor (counter 1) + rules lead (counter 2) | 3.2 on three separate selections: the pitch with its heading; the IPS with its heading and sub-headings; the title page (for the record). Run the kit banned-word grep | pitch ≤ 50 (target 45) and IPS ≤ 500 (target 470), strictest count, both counts logged |
| B4 | 16:30-17:00 | editor | Final provenance run (3.3) on the pitch and the IPS against the full AI corpus. Add every IPS-era AI file, for example the IPS writing kit, the ipsfix outputs and any AI issues-only check outputs. `--allow` = the official files | CLEAN, or every FLAG resolved (cut, or "proper name, kept") and re-counted |
| B5 | 17:00-17:30 | editor exports; rules lead checks | 3.1e: File → Download → PDF, **Current Tab**. Run `python3 pdfgate.py Caplet_IPS.pdf --max-pages 3 --locked ips_locked.txt`. `ips_locked.txt` is the locked tab downloaded as plain text (Current Tab), title page included | pdfgate exit 0 (every PASS); output saved |
| B6 | 17:30-18:00 | rules lead + one more student, on a **second device** | Read all three pages (3.1e step 5). Tick F1-F12. Compare the title-page names, team name and WInS username with the roster confirmation and the WInS login, character by character | F1-F12 all ticked |
| B7 | 18:00-18:30 | historian; each student | AI-use rows for the IPS complete (3.6). Each paragraph owner logs "written by me from my own notes" | DL-36 rows ready |
| B8 | 18:30 | deputy | Go/no-go on B1-B7. Any open item means fallback: fix and submit by Fri 6 Nov 18:00, never Saturday | "GO" logged |
| B9 | **19:00-19:15 (M9)** | Ray chairs | Approve vote, if M8's DL-36 needs reconfirming after any fix. Confirm no WInS order is open that the IPS does not describe (the last fallback order closed Wed 4 Nov ET = Thu 5 Nov 08:00 Sydney) | DL logged |
| B10 | 19:15-19:45 | **Ray submits**; deputy and paste checker watch | Normal browser, no AI tool running. Open the IPS task. Upload `Caplet_IPS.pdf` (the exact file B5 gated: check name, size and time). If an upload error appears, go to §3.7. **Download or preview the uploaded file from SMApply and open it**, to check it is the right file and it opens. Any text fields the form has (for example a pitch box) are pasted and copy-back checked as in A11 | the uploaded file opens and matches B5 (same page count and first and last words) |
| B11 | 19:45-20:00 | **Ray** | Press the button the decision rule (3.5) picks, using whatever was learned at the TNA submit about how the site works | status shows complete or submitted |
| B12 | by 20:00 | Ray; deputy checks | **Confirmation screenshots** (message, task status, My Applications) with the clock visible. More Options → **Download** the application (SMA:227-231) | 3 screenshots + 1 download |
| B13 | by 20:15 | Ray; deputy | Save in "Submitted/IPS" in the private Drive and a second drive (A14 naming; crop personal data; never in the repo) | **confirmation screenshot saved** = done |
| B14 | by 21:00 | historian | Log DL-38 "IPS submitted", with the time in Sydney and ET, the button, the files and the status text | logged |
| B15 | Fri 6 Nov evening, and Sat 7 Nov after 08:00 | trade-log keeper (hand-off, not part of the submit) | Save WInS Order History (including cancelled orders), Transactions, Trade Notes, Portfolio Summary and Session Rules, before and after the freeze, with the username cropped (OPS §4b; QV2 Q7) | files in Drive |
| B16 | **Sat 7 Nov 09:30** | Ray | Check the status and email (spam too) | screenshot added |

---

## 6. Still UNVERIFIED (team checks; no AI tool can log in)

- Everything in 3.5's list: the structure of the SMApply forms, the buttons, field limits, reopening, confirmation,
  and how the roster submission worked.
- Whether "Accept all / Reject all" covers all tabs or only the open tab (3.1b).
- Whether a Docs PDF download ever prints comments (3.1e).
- Whether File → Make a copy carries version history (treated as no).
- How Google Docs counts hyphenated, slashed or dashed words (3.2). Whether Wharton counts headings or splits
  hyphens (QV2 Q2; strictest defaults used).
- Wharton's office hours and reply speed (assumed 9 am-5 pm ET weekdays for §2). Whether Contact Us sends a copy
  (QV2 §6).
- Whether anyone but the leader may submit (QV2 Q6).
- The exact WInS freeze time (OPS:346-348 [consistency fix 20 Oct, row 20]; `wins_notes.csv` says "ends 6 Nov 2026 4:00 pm ET", from a 29 Sep team reading).
- Whether `pdfgate.py`'s font, size and line checks behave the same on a real Google Docs PDF. They were tested on
  generated PDFs only. A LibreOffice test could not run in this container. **Run it once on Wed 21 Oct** on a test
  export of any double-spaced TNR tab, and keep the output.

## 7. Files

- `RB/runbooks.md`: this file.
- `RB/tools/provenance.py`: 5-word-run provenance check (tested; see 3.3).
- `RB/tools/pdfgate.py`: PDF format gate (tested; see 3.4).
- `RB/tools/tz_table.py`: the §2 table, built with zoneinfo. `RB/tools/totext.py` is the HTML to text converter
  (copied from `oct20/askwharton2/tools/`).
- `RB/tests/`: test inputs and outputs. These are the note copies; paste-error cases (curly apostrophe, missing
  "about", trailing space, double space, non-breaking space, the cancelled IBTR, IBTO); generated pass, fail and
  encrypted PDFs; and `tz_table_out.md`. No deliverable prose: the only reflection text in it is the AI's own
  accepted "[AI]" VT reflection, used as a positive control.
- `RB/web/`: help pages fetched live 19 Oct 23:08-23:10 UTC (raw HTML in `web/raw/`, text in `web/*.txt`,
  `fetch_log.txt`). One URL (answer/13945346) returned 404 and was replaced by answer/15499791.
