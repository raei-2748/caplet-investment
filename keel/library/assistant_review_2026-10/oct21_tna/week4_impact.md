# Week 4 email: what the IPS-as-a-form change does to the 20 Oct pack

AI-generated research (Claude Code, Wed 21 Oct 2026, about 18:20 Sydney). Not for submission. Log it as AI use.
It contains no IPS, pitch or title-page wording. The fixes below are to the team's process documents only.

SP = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad`.
Raw fetches and text copies: `SP/oct21/tna/week4/fetch/` (fetch times in `fetch_time.txt`).

## 0. Bottom line

1. **The change is not public.** The only source is the team's copy of the Week 4 email in the IPS Report Doc's
   "Letters" tab (`SP/oct21/tna/current_draft_21Oct.md:37`). Neither the public SMApply pages nor the Wharton site carry it.
   The IPS instructions file linked from the public Deliverables page is byte-identical to the September file, and that
   file still says "Submit as a PDF" (section 1).
2. **What still holds:** the 50- and 500-word caps, the title-page content (team name, names as "First Name, Last
   Initial", WInS username), the bans on graphics, links, footnotes and citations, the focus rules, and the strategy
   freeze. **What goes:** the PDF, the 5 MB limit, the export and `pdfgate.py` steps for the IPS, and the Docs page
   setup. **What can no longer be checked:** Times New Roman 12, double spacing, 1-inch margins, "1 page maximum" and
   "2-page maximum". A plain text box has no font, spacing, margins or pages. Whether Wharton still means them under "all
   other requirements remain the same" is **UNVERIFIED**.
3. **The binding limit is now the form.** SMApply text boxes can enforce a word limit or a character limit, and the
   character limit counts spaces (section 4). The team must open the IPS form early to see its fields and limits.
4. **The Final Report instructions post Tue 10 Nov 01:00 Sydney**, not "Mon 9 Nov 16:00", which the pack uses in 8 places.

## 1. Is it published? (task 1)

Fetched with plain curl, `Cache-Control: no-cache` and a `?cb=<epoch>` query, **Wed 21 Oct 2026 07:12:23 UTC (18:12 Sydney)**.
The Wharton pages were fetched at 07:13:24 UTC and the SMApply help pages at 07:16:00 UTC.

| Page | Result | What it says about IPS format or FR timing |
|---|---|---|
| https://wghsinvcomp.smapply.us/res/p/deliverables/ (HTTP 200) | **Not published.** The text is word-for-word the same as the 14 Oct snapshot (`competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt`) apart from the page title line and a split "9 ." | "Investment Policy Statement (Due: November 6; no later than 5:00 p.m. ET)" (`fetch/deliverables.txt:28-29`); "All deliverables must be submitted via your team's SurveyMonkey Apply account." (:36); IPS "Instructions: Click Here" (:57-58) links to https://upenn.box.com/s/0iib496jhswp30c12zhn6b2fret8dl30; FR: "Detailed Final Report instructions and requirements will be shared on November 9" (:62-63). **No hour is given.** The words "PDF" and "SurveyMonkey Apply form" do not appear. |
| The Box file behind that IPS link | **Unchanged.** Box reports the name "2026_WGY_Investment Policy-FINAL.pdf", 183,328 bytes, sha1 `099114e7b540d20bffe85924f2f8490f666b086a` (`fetch/box_ips.html`). That is the same sha1 and size as the repo copy, `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.pdf` | That file still says "Submit as a PDF through SurveyMonkey Apply." and "Maximum file size: 5 MB." (`2026_WGY_Investment_Policy-FINAL.txt:120-122`). **The public instructions now contradict the email.** |
| https://wghsinvcomp.smapply.us/res/p/faqs/ (HTTP 200) | **Not published.** The text matches the 20 Oct snapshot apart from line breaks. "PDF" appears 0 times | IPS: "Define your client's investment objectives, risk tolerance, and overall investment strategy." (`fetch/faqs.txt:95-96`). Nothing on format. |
| https://globalyouth.wharton.upenn.edu/investment-competition/, `/competitions/investment-competition/faq/`, `/rules-roles/`, `/investment-competition/competitor-resources/`, `/more-info/` (all HTTP 200) | **Not published.** None mentions "PDF", "Times New Roman", "double-spaced" or "November 9" | The FAQ says: "All communications and notifications will be sent via SurveyMonkey Apply. Copies of the weekly emails will also be posted on the Wharton Investment Simulator (WInS) for all team members to view." (`fetch/competitions_investment-competition_faq.txt:319`) |

**Status of the two new facts: TEAM-REPORTED, not public.** The date and time the email arrived are UNVERIFIED.
Before the team acts on it, someone should (a) check the original email in the team inbox or SMApply messages, and
(b) check the copy posted in WInS. A student does this; AI tools never open SMApply or WInS (CLAUDE.md). They should
also check the logged-in Pages → Deliverables page for a new IPS instructions file. Until then, the public PDF
instruction and the email conflict. The email is newer and more specific, so the team should follow it and ask Wharton
to confirm (section 5, Q1).

## 2. Sydney times (task 2)

Computed with Python `zoneinfo` (America/New_York → Australia/Sydney). US clocks go back Sun 1 Nov at 02:00 EDT,
which is 17:00 Sydney. After that, Sydney is 16 h ahead.

| Event (ET) | Sydney |
|---|---|
| TNA due Fri 23 Oct 5:00 pm EDT | Sat 24 Oct 08:00 AEDT (unchanged) |
| IPS due Fri 6 Nov 5:00 pm EST | Sat 7 Nov 09:00 AEDT (unchanged) |
| **FR instructions Mon 9 Nov 9:00 am EST** | **Tue 10 Nov 01:00 AEDT** |
| FR due Fri 4 Dec 5:00 pm EST | Sat 5 Dec 09:00 AEDT (unchanged) |

The pack's "from Mon 9 Nov 16:00 Sydney" equals 9 Nov 00:00 EST, the earliest possible moment on 9 Nov ET. With the
hour now given, the earliest release is **9 hours later**. Nobody needs to watch SMApply on Monday afternoon or
evening. The first useful look is Tue 10 Nov before school, around 07:00. M11 on Tue 10 Nov 20:00 is now 19 h after
release, so the fallback move to Wed 11 Nov is needed only if Wharton posts late.

## 3. Sweep of the 20 Oct pack (task 3)

Search terms: PDF, export, Times New Roman/TNR, double-spaced, page(s), 5 MB, title page, footnote, header, 9 Nov,
16:00, Mon 9 Nov, November 9. I read 370 hits. Hits that the change does not touch are grouped at the end of each
file's table. Verdicts:
- **OBSOLETE**: no longer true for the IPS.
- **UNCHECKABLE**: the rule may still stand, but a form cannot show it. UNVERIFIED until Wharton or the form says.
- **CHANGED**: needs a new time or a new mechanic.
- **VALID**: unchanged.

"16:00" hits about the TNA text lock (Thu 22 Oct 16:00) are all **VALID**. The TNA was always a form (TNA:54).

### 3.1 `oct20/verify_runbook/runbooks_checked.md` (Runbook B and `pdfgate.py`)

| Line(s) | Hit | Verdict | Exact fix |
|---|---|---|---|
| 48-50 (§0 item 1) | "TNR 12 … title page … 5 MB PDF limit are IPS rules" | CHANGED | Add: "Week 4 email (team copy): the IPS is now a SurveyMonkey Apply form; no PDF. TNR, spacing, margins and page caps cannot be checked in a form, and whether they still apply is UNVERIFIED. The 5 MB limit is gone." |
| 186-204 (§3.1d) | Format settings: Pages, Letter, 1-inch margins, TNR 12, Double, no header/footer | OBSOLETE for the IPS | Retitle it "TNA/FR upload only (house style)". For the IPS, replace it with a **paste-file** step. The locked text goes to plain text (File → Download → Plain text, Current Tab), one `.txt` per form field. Check it with `keel/office/tools/textcheck.py` for words, characters (with spaces), curly quotes and non-ASCII characters. |
| 206-219 (§3.1e) | Export one tab to PDF; second-device read of the PDF | OBSOLETE for the IPS (keep for the FR) | Replace it for the IPS with a check on the form itself. Paste each field without formatting. Copy each field back out of the form into a file and run `textcheck.py --compare`. Then open the SMApply **Preview** and **Download** (SMA:212-231) on a second device. Check paragraph breaks, characters ($ % – ’), no "[AI]", and no text from a suggestion or comment. The existing "search for a word only in a rejected suggestion" test moves to the copy-back file. |
| 250-251, 259 (§3.2) | Docs word count leaves out headers/footers; "title page is not part of the pitch or IPS count" | VALID, with an addition | Add: "**The form's own counter wins.** If the field has an SMApply word or character validator, it decides, and how it counts hyphens, numbers and dashes is UNVERIFIED. Paste a test passage into the field, read the count it shows, and do not save." |
| 316-341 (§3.4) | `pdfgate.py` for the IPS (`--max-pages 3`, 5 MB, Times, 12 pt, double, margins) | OBSOLETE for the IPS | Strike the IPS command line at 319. Keep the tool for the TNA (only if uploaded) and the FR (FORECAST). Note that its docstring cites IPS:110-123 as the source of its checks; for the FR, the rules come from the 9 Nov instructions. |
| 573-575 (§6) | "Run it once on Wed 21 Oct" on a real Docs export | CHANGED | This is no longer urgent. Move it to before FR Draft 1 (Sat 21 Nov), and only if the 9 Nov instructions ask for a PDF. |
| 376 (§3.5) | "The IPS goes in 'as a PDF through SurveyMonkey Apply' with a 'Maximum file size: 5 MB' (IPS:120-122)" | OBSOLETE | Replace it with the Week 4 email quote, marked "team copy, not on the public pages as of 21 Oct 07:12 UTC". Note that the public IPS PDF still says PDF. |
| 380-391 (§3.5 UNVERIFIED list) | Form structure items 1-7 | CHANGED | Add an item 8: "IPS form: number of fields; whether the title page, pitch and IPS are separate fields; any word or character validator per field; whether field labels are the official headings; whether a file upload is also offered." |
| 448 (§3.7) | Upload rejected: "a text-only Docs PDF should be far under 5 MB" | OBSOLETE for the IPS | Restrict the row to the TNA/FR. Add a new failure row for the IPS: "**Validator blocks the field** ('Invalid Entry' or a count message, per SMApply text-validation help). Do not trim at the keyboard. Return to the Doc, cut by an author's decision, re-lock, re-paste." |
| 515-518 | Runbook B header and the hard rule (IPS:82-83) | VALID | none |
| 520-535 (B-pre, F1-F12) | Format gate "on the exported PDF" | Mixed. See the next rows | Retitle it "Form-text gate (Tue 3 Nov 18:00)" and run it on the paste files. |
| 524 F1 | Title page "1 page maximum" | UNCHECKABLE | Replace it with: "title-page items go where the form puts them (fields, or the top of the text box). If there are no title-page fields, ask Wharton (section 5, Q2)." |
| 525-527 F2-F4 | Team name, names as "First Name, Last Initial", WInS username | VALID (content) | Keep. Add: "the username goes only into the form, never into the repo, a public file or a screenshot kept outside the private Drive." |
| 528 F5 | "2-page maximum … 3 pages in all"; `pdfgate --max-pages 3` | UNCHECKABLE | Delete the pdfgate check. Mark it "UNVERIFIED whether a page cap survives (section 5, Q1)". The word caps are the binding test. |
| 529 F6 | Pitch ≤ 50, IPS ≤ 500; targets 45/470 "headings counted" | VALID, with an addition | Keep the targets. Add: "if the form gives each part its own labelled field, the label is not typed into the field. Any sub-heading typed inside a field counts against that field's limit." |
| 530 F7 | TNR 12, double, 1-inch margins | UNCHECKABLE | Mark it "Not checkable in a form; UNVERIFIED whether it applies (Q1)". Do not spend gate time on it. |
| 531 F8 | "Submit as a PDF … 5 MB" | OBSOLETE | Replace it with: "submitted in the SMApply IPS form (Week 4 email)". |
| 532 F9 | No graphics, charts, links, footnotes, citations | VALID | Keep. Add: "a typed URL may be turned into a link by the form or the reviewer view, so type no URL or 'www'." Footnote markers such as "¹" or "[1]" are still banned. |
| 533 F10 | No suggestions, comments or AI text "print" | CHANGED | Change it to: "none in the paste files or the copy-back". Whether copying from a Doc with pending suggestions carries the suggested text is UNVERIFIED, so reject or accept every suggestion before the plain-text download. |
| 534 F11 | Consistent with the submitted TNA | VALID | none |
| 535 F12 | The two official headings "present, and counted in F6" | CHANGED | Make it depend on the form. If the fields are labelled with the headings, they are not typed in. If there is one box, the team decides (Q3). |
| 541-546 (B1-B6) | B2 page setup; B5 PDF export plus `pdfgate`; B6 second-device read of three pages | OBSOLETE (B2 page setup, B5) / CHANGED (B6) | B2: drop the page-setup clause and keep "zero suggestions; resolve comments". B5: download the locked tab as plain text, split it into per-field `.txt` files, and run `textcheck.py` with word and character counts. B6: the second person reads the paste files against the Doc and compares the title-page items with the roster confirmation. |
| 550 (B10) | "Upload `Caplet_IPS.pdf` … download or preview the uploaded file" | OBSOLETE | Replace it with: paste each field without formatting, copy it back with `textcheck.py --compare` until "exact match: YES", save (without Mark as Complete), then Preview and Download and read them on a second device. This is the same mechanic as A11 for the TNA. |
| 552-553 (B12-B13) | Download the application; save the files | VALID | Add the per-field paste files and the copy-back files to the saved set. |
| 121, 130 (§2 table) | "Format gate on exported PDF" Tue 3 Nov 18:00 | CHANGED (label only) | Rename it "Form-text gate". The times stand. |
| 17, 29, 37-38, 64-71, 87-89, 101, 146, 177, 193-199, 213, 390, 412, 423, 442, 447, 454, 472-506, 565, 581-588 | Help-page cites, roles ("exports the PDF"), TNA-day rows, AI-provenance rows | VALID, except two | Line 88 (editor "exports the PDF") and line 89 (rules lead "runs `pdfgate.py`") become "prepares and checks the paste files" for the IPS. |

### 3.2 `oct20/master/master_playbook_checked.md`

| Line(s) | Hit | Verdict | Exact fix |
|---|---|---|---|
| 53 | "'9 Nov ET' can start Mon 9 Nov 16:00 Sydney" | CHANGED | Replace it with: "FR instructions Mon 9 Nov 9:00 am EST = **Tue 10 Nov 01:00 Sydney** (Week 4 email, team copy)". |
| 65 | Wed 21: `pdfgate.py` tested on a real Docs export | CHANGED | Move it to "before FR Draft 1, only if the FR is a PDF". |
| 90 | Tue 3 Nov 18:00 "PDF format gate" | CHANGED | Change it to "form-text gate (paste files, counts, title-page items)". |
| 96 | M11 Tue 10 Nov; "instructions may appear from Mon 9 Nov 16:00" | CHANGED | Change it to "instructions due Tue 10 Nov 01:00 Sydney". |
| 336 | "Three pages: a one-page title page … then a two-page maximum" | UNCHECKABLE | Mark the page structure "superseded by the form (Week 4 email); page caps UNVERIFIED". Keep the title-page *content*. |
| 337 | Length 45/470 including headings | VALID | Add the field-label rule (F12 above). |
| 338 | "Format: TNR 12, double-spaced, 1-inch margins; one PDF, 5 MB or less" | OBSOLETE (PDF, 5 MB) / UNCHECKABLE (TNR, spacing, margins) | Rewrite the bullet to keep only the banned-content list and "tables not named". Add a note: a table cannot be built in a plain text box (INFERENCE: SMApply's 16 question types include no rich-text editor, https://help.surveymonkey.com/en/apply/build/question-types/, fetched 07:16 UTC), so the question of whether a table counts as a chart is moot. |
| 340 | "AT RISK … whole-document export printed both wordings; export the IPS tab alone" | CHANGED | The export risk is gone. The suggestion risk remains: reject or accept all 10 suggestions before the plain-text download (copying suggested text is UNVERIFIED). |
| 348 | "One clean text that fits the strict caps on two pages" | CHANGED | Drop "on two pages". The caps are words (plus any form character limit). |
| 377 | "Seven body paragraphs or fewer help the two-page fit" | OBSOLETE (reason) | The reason is gone. Keep the paragraph count only as a readability choice, or drop it. |
| 385-390 (§5f) | The PDF-export check, pdfgate, three pages on a second device, "downloads the uploaded file" | OBSOLETE | Replace it with the form mechanics from 3.1 (B5/B6/B10 fixes): paste files, copy-back, Preview/Download. |
| 392 | "Wharton's is 500 words with none" | VALID | none |
| 488 | FR structure FORECAST "(from Mon 9 Nov 16:00 Sydney)" | CHANGED | Change it to "from Tue 10 Nov 01:00 Sydney". Add: "the IPS moving to a form lowers confidence that the FR is a page-ranged PDF; keep modules flexible". |
| 638 | Tools row lists `pdfgate.py` for "Submit-day steps (TNA and IPS)" | CHANGED | Change it to "PDF gate (TNA upload only, FR if PDF)". |
| 5, 13, 27, 30, 34, 62, 69, 82, 108, 116, 125-126, 139, 143, 167, 171, 473, 509, 534, 552, 586, 593, 620, 637, 640, 646, 675, 677, 688 | Banner, TNA rows, AI policy, links | VALID | Line 139 ("TNR 12 … are IPS rules") gets the 3.1 §0 note. Line 473 "last curve before export (Tue 3 Nov)" becomes "before the paste files lock". |

### 3.3 `oct20/verify_ipsfix/ips_fix_list_checked.md`

| Line(s) | Hit | Verdict | Exact fix |
|---|---|---|---|
| 60, 83 (G, X2) | "Reject the pending suggestions so the PDF stops printing both wordings (… over 4 pages)"; "2-page maximum" | CHANGED | Keep "one wording only" (the doubled text is still a fault in the paste). Drop "over 4 pages vs 2-page maximum" as the measure; the measure is the word caps. |
| 93, 95 (T1, T3) | "[AI]" tag; username "on the PDF only" | VALID / CHANGED | T3: change "on the PDF only" to "in the SMApply form only". |
| 96 (T4) | One-page title page plus two strategy pages; TNR 12, double, 1-inch margins | UNCHECKABLE | Mark it "superseded by the form; UNVERIFIED (Q1)". |
| 97 (T5) | "Doc tab title 'Version 5' and stray headings risk printing" | CHANGED | The risk moves to the paste. No tab title, instruction line or "[AI]" goes into a paste file. Headings follow the field-label rule. |
| 231 | "Seven body paragraphs or fewer help the two-page fit" | OBSOLETE (reason) | As master:377. |
| 246 | "last curve before export (Tue 3 Nov)" | CHANGED (wording) | Change it to "before the paste files lock (Tue 3 Nov)". |
| 270 (checklist 1) | Font and spacing | UNCHECKABLE | Mark it UNVERIFIED (Q1). Delete "Letter paper". |
| 271 (checklist 2) | "one PDF, 5 MB or smaller" | OBSOLETE | Replace it with "submitted in the SMApply IPS form; Preview and Download saved". |
| 272-273 (3, 4) | Bans; title-page content | VALID | Item 4: drop "1 page"; add "in the form's title-page fields if any". |
| 274 (5) | "pages 2-3 hold both, two pages at most" | CHANGED | Drop the page clause. Add "and within any form character limit". |
| 275 (6) | "no suggestion colour … no 'Version 5' tab title … only the two official headings" | CHANGED | Drop "colour"; apply the field-label rule. |
| 268 | "tick on the exported PDF" | CHANGED | Change it to "tick on the paste files and the SMApply Preview". |
| 292 | "two-page fit … UNVERIFIED" | OBSOLETE | Replace it with "IPS form fields and limits UNVERIFIED until opened". |
| 5, 16, 20, 37 | Banner, line map, sources | VALID | none |

### 3.4 `oct20/verify_ipsstruct/ipsstruct_checked.md`

| Line(s) | Hit | Verdict | Exact fix |
|---|---|---|---|
| 131 | Bans (IPS:123-124) | VALID | none |
| 216 | "Seven body paragraphs … two-page fit" | OBSOLETE (reason) | As master:377. |
| 316 (O5) | "500 words; two pages for pitch + IPS" | CHANGED | Change it to "500 words (form)". |
| 323 (O12) | Title page needs name, members, username | VALID (content) | Add "in the form". |
| 366 | "Two-page fit is UNVERIFIED until … exported" | OBSOLETE | Replace it with the form-field check. |
| 6, 9, 24, 31, 46-57, 312, 363, 374 | Sources, footnotes in professional IPSs (O1 is still correct: none allowed) | VALID | none |

### 3.5 `oct20/out/Caplet_Login_Checks_v2_20Oct2026.md`

| Row | Hit | Verdict | Exact fix |
|---|---|---|---|
| 2 | Task list; "open the TNA task without pressing anything" | CHANGED | Extend it: also **open the IPS task without pressing anything** and screenshot every field, label, limit message, upload box (if any) and button. Do this on Thu 22 Oct during the TNA session if the task is visible, or the first day it appears. Record whether opening it alone changes its status to "In progress" (UNVERIFIED). |
| 12 | Docs test (a): TNR 12 … PDF Current Tab … `pdfgate.py`, due Wed 21 Oct 22:00 | CHANGED | Drop (a) for the IPS; keep it only as FR preparation, no deadline before 9 Nov. Add a test: download a test tab as plain text; check what survives (bold, italics, bullets "•", tabs, curly quotes, em dashes, blank lines between paragraphs); run `textcheck.py` on it. (b) and (d) stay. |
| 24 | Roster confirmation for "the IPS title page" | VALID | Change "title page" to "title-page items (form fields)". |
| 26 | IPS submit: "before the upload … download or preview the uploaded file … `2026-11-05_smapply_ips_download.pdf`"; "Uploaded file differs from the gated PDF" | OBSOLETE (upload) | Replace the upload with: paste each field; copy-back check; save; Preview; Download (the SMApply application download is still a file, keep it); then the button the three-case rule picks. Change "Uploaded file differs" to "Copy-back differs from the paste file: stop, re-paste". The "Contact Us before Sat 7 Nov 01:00 Sydney = Fri 6 Nov 9:00 am EST" conversion is correct (zoneinfo). |
| 28 | "Instructions 'shared on November 9' may appear from Mon 9 Nov 16:00 Sydney"; "From Mon 9 Nov 16:00; by Tue 10 Nov 18:00" | CHANGED | Change it to "posted Mon 9 Nov 9:00 am EST = **Tue 10 Nov 01:00 Sydney** (Week 4 email, team copy; the public page gives no hour)". The window becomes "from Tue 10 Nov 07:00; by Tue 10 Nov 18:00". Add to the row: "note whether the FR is a form, an upload, or both". |
| 29 | FR and school-letter "upload checks as in row 26, for two files" | CHANGED | Change it to "as the 9 Nov instructions require (upload, form or both); the school letter is 'a separate file' (`fetch/deliverables.txt:65`)". |
| 1, 6, 9, 27, 57, 59-63, 68, 70, 73-76, 83, 85-88, 108 | Banner, other rows | VALID | none |

### 3.6 `oct20/ops/operating_plan.md`

| Line(s) | Hit | Verdict | Exact fix |
|---|---|---|---|
| 37 | "Final Report instructions 'shared on November 9' (Tue 10 Nov Sydney; hour UNVERIFIED)" | CHANGED | Change it to "Mon 9 Nov 9:00 am EST = Tue 10 Nov 01:00 AEDT (Week 4 email, team copy)". |
| 81 | Editor "exports the PDF" | CHANGED | Change it to "IPS: prepares the paste files; FR: exports if a PDF". |
| 118 (M8) | "format gate on the exported PDF"; "Exported PDF (18:00)" | CHANGED | Change it to "form-text gate on the paste files"; the input becomes "paste files + counts (18:00)". |
| 119 (M9) | Input "Locked PDF" | CHANGED | Change it to "locked paste files". |
| 125 (M15) | FR "Exported PDF + letter file" | VALID (FORECAST) | Add "if the FR is a PDF". |
| 215 | Tue 3 18:00 "PDF export and format gate: … TNR 12, double-spaced, 1-inch margins … ≤5 MB … second device" | OBSOLETE / UNCHECKABLE | Keep: caps 50/500 (aim 45/470), the bans, names as on the roster. Drop: export, TNR, spacing, margins, 5 MB. Add: field limits from the IPS form screenshots. |
| 230 | Tue 10 "Instructions out (Mon 9 Nov ET): paste them verbatim … by 18:00" | VALID | Add "posted 01:00 Sydney". |
| 324 (R7) | Submission tech: "the PDF prints suggestions … file >5 MB; wrong file" | CHANGED | Rewrite the risk: "IPS form fields and limits unknown; validator blocks the paste; paragraph breaks or characters lost; text from a suggestion pasted". Trigger: "IPS form not seen by Tue 27 Oct". |
| 334 (R17) | "final PDF on two devices" | CHANGED | Change it to "paste files on two devices". |
| 3, 10, 24, 33-36, 50, 112-116, 134, 193-194, 206, 212, 234, 250, 345 | TNA rows, HSC PDF, other | VALID | none |

### 3.7 `oct20/verify_frblue/fr_prep_v2_checked.md`

| Line(s) | Hit | Verdict | Exact fix |
|---|---|---|---|
| 28-31 | "9 Nov ET runs from Mon 9 Nov 16:00 to Tue 10 Nov 16:00 Sydney" | CHANGED | Change it to "posted Mon 9 Nov 9:00 am EST = Tue 10 Nov 01:00 Sydney (Week 4 email, team copy)". |
| 158 (F1) | "TNR 12, double-spaced, 1-inch margins, PDF, size cap … 2026-27 IPS:112-122 … 95%" | CHANGED | Remove the 2026-27 IPS as evidence (it is no longer a PDF). Lower the likelihood (the AI's guess: about 70%). Keep the 2022-24 specs and the school letter as "a separate file". Prepare-now becomes "template ready, but also keep a plain-text master". |
| 161 (F4) | Title page evidence "IPS:84-100" | CHANGED | Mark the evidence as weaker: the IPS title page may now be form fields. |
| 163, 166, 177-182, 371 (F6, F9, §2.1) | Portfolio-at-a-Glance tables/charts; page budget "One double-spaced TNR 12 page holds about 250-280 words" | VALID (FORECAST) | Add one line: "if the FR is also a form, page budgets and charts may not apply; keep word budgets per module as the primary unit". |
| 173 (F16), 257 | "Instructions out Mon 9 Nov ET" | VALID | Add "9:00 am EST". |
| 575 (W1) | "Mon 9 16:00 onward … (9 Nov 00:00 EST)" | CHANGED | Change it to "Tue 10 Nov 01:00 onward (9 Nov 09:00 EST); first look Tue 07:00". |
| 644 (row 132) | "Instructions may appear from Mon 9 Nov 16:00 Sydney" | CHANGED | As 575. |
| 704 | UNVERIFIED: "Release hour of the 9 Nov instructions" | CHANGED | Move it to "team-reported (Week 4 email): 9:00 am ET; not on the public page as of 21 Oct". |
| 6, 12, 20, 38, 69, 106-108, 142, 160, 304, 388, 401, 428-437, 475, 586, 615, 635, 640, 694 | Past specs, Works Cited, page ranges (FORECAST) | VALID | none |

### 3.8 `oct20/out/` (other files), `timeline/timeline.md`, `semis/semis_playbook.md`

| File:line | Hit | Verdict | Exact fix |
|---|---|---|---|
| `out/Caplet_M1_Meeting_Pack_v2_20Oct2026.md:74` | "A whole-Doc PDF printed both wordings … one-tab export untested" | CHANGED | For the IPS, change it to "suggestions must still be cleared before the plain-text download". |
| `out/Caplet_Wharton_Questions_SendToday_20Oct2026.md:49` | Batch 2: "the IPS-tables question if a student draft uses a table" | OBSOLETE | A plain text box cannot hold a table (INFERENCE, section 4). Replace it with Q1-Q4 in section 5 below. Send them in batch 2, or now. |
| `out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md` (18 hits) | TNA facts, WInS page, plain-text paste | VALID | none. The TNA is unchanged. |
| `out/Caplet_Login_Checks_20Oct2026.md`, `out/Caplet_M1_Meeting_Pack_20Oct2026.md` (v1) | Superseded by v2 | n/a | none |
| `timeline/timeline.md:190-191` | Deadlines (TNA, freeze, IPS, FR) | VALID | Add a row: "Week 4 email (date and arrival UNVERIFIED): IPS by SMApply form, no PDF; FR instructions Mon 9 Nov 9:00 am ET". Other hits (rows 4, 34, 39, 41, 113-159, L4-L14) are historical: VALID. |
| `semis/semis_playbook.md:8, 282` | "Until the IPS is in (Sat 7 Nov 09:00)"; "9 Nov to 4 Dec: use Part 4" | VALID | Line 282: "from Tue 10 Nov 01:00 Sydney". Other hits (NS PDFs, page refs, video format) are not affected. |

### 3.9 Outside the pack (flag only; the brief bars me from editing the repo)

These read-only repo files still state the PDF format and need updating by whoever commits:
- `COMPETITION.md:131` ("PDF <= 5 MB") and `:23` ("~Tue 10 Nov" → "Tue 10 Nov 01:00").
- `keel/office/workstreams/2_IPS.md:16, 43, 55`.
- `CLAUDE.md`, the "Official deadlines" paragraph ("TNR 12 double-spaced"), and its "Next:" line.

The scratchpad zips `oct20/out/Caplet_pack_20Oct2026_*.zip` carry the old text. Tell the team with a one-line errata
note rather than rebuilding them.

## 4. New risks of a form submission (task 4)

SMApply facts below are from SurveyMonkey Apply help, fetched 21 Oct 07:16 UTC:
- **TR**: https://help.surveymonkey.com/en/apply/build/text-response/
- **TV**: https://help.surveymonkey.com/en/apply/build/text-validation/
- **QT**: https://help.surveymonkey.com/en/apply/build/question-types/

Text copies are in `fetch/sm_*.txt`.

1. **Limits set by the form, not by Docs.**
   - A text field can carry "Word Limits: Set the minimum and maximum length of words that your user must enter in order
     to proceed" (TV:154-156).
   - It can also carry "All Characters: Set a character limit … This validation will also include any spaces entered"
     (TV:159-160).
   - Whether Wharton set either limit, and at what value, is UNVERIFIED.
   - How SMApply counts "2033-2042", "$50,000" or "rates—and" is UNVERIFIED and may differ from Docs and `textcheck.py`.
   - A character cap would bind before 500 words if it is set near 3,000 characters. 500 words of this kind of text
     run roughly 3,000-3,500 characters with spaces (CALC estimate; measure the real draft with `textcheck.py`).
   - Risk: the form blocks the paste at 19:30 on submit night. Fix: learn the limits weeks ahead (item 5).
2. **Formatting is lost.** A Text Response is a plain single-line or "Multiline" box (TR:24; "up to a maximum of 25"
   rows shown, TR:66). SMApply's 16 question types list no rich-text editor (QT). INFERENCE: bold, italics, underline,
   font, size, spacing, bullets-as-formatting and tables do not survive.
   - Paragraph breaks probably survive as line breaks: check this in Preview and Download.
   - Curly quotes and dashes may display differently in the reviewer's view.
   - The judges will read whatever the SMApply reviewer view or PDF renders, in a font the team does not choose.
   - Consequence: structure must come from paragraphing and plain words, not from layout.
   - Secondary risk: typed URLs could be auto-linked (banned "external links").
3. **Where the title page, pitch and IPS go: UNVERIFIED.** There are four possibilities, each with a different
   word-count consequence:
   - (a) separate fields for the team name, members and username, then a pitch field and an IPS field;
   - (b) one box for everything;
   - (c) text fields plus an optional upload;
   - (d) the title-page items taken from the roster automatically.

   If (b), the team must decide how to separate the parts and whether the title lines count; ask Wharton (Q2/Q3). The
   WInS username must go in exactly, but never into a public file.
4. **Whether headings count.**
   - If the fields are labelled "Investment Strategy Elevator Pitch" and "Investment Policy Statement", typing the label
     again wastes 4 + 3 words and could push a validator over.
   - Sub-headings typed inside the IPS field count against it.
   - The pack's strict targets (45/470, headings included) stay safe in every case.
   - What changes is only whether the official headings are typed at all (decide once the form is seen).
5. **Open the IPS form early.** Screenshot every field, label, help text, limit message and button. Note any AI,
   integrity or terms box, and do not tick it.
   - Best time: Thu 22 Oct, in the same logged-in TNA session (Login Checks row 2). Latest: before M5 on Tue 27 Oct,
     because the structure votes depend on it.
   - If the IPS task shows "cannot be started at this time", screenshot that and re-check daily from Mon 26 Oct.
   - Do not save text in it until the lock, and do not press Mark as Complete.
   - Whether merely opening it creates a draft or "In progress" status is UNVERIFIED.
6. **Lost or stale text.** Keep the Doc as the master and paste only the locked paste files. A timed-out session could
   lose text typed into the form (UNVERIFIED). If the team saves a test paste, the form now holds a second copy that
   can go stale; clear it or overwrite it at submission.
7. **Suggestions leaking into the paste.** The 10 pending suggestions in the live Doc
   (`SP/oct21/tna/current_draft_21Oct.md`; CLAUDE.md Current status) could travel with a copy-paste. Whether Docs
   copies suggested text is UNVERIFIED. Clear all of them before the plain-text download, then run the copy-back
   compare.
8. **Conflicting official sources.** The public IPS PDF still says "Submit as a PDF" (IPS:120). If a judge or the form
   still expects TNR or a two-page look, the team cannot show it. The form is the only route the email allows, so keep
   the dated email copy and Wharton's answer as evidence.
9. **The FR may follow.** One deliverable moved to a form "with all other requirements the same". The FR could too, or
   could be a mixed form and upload (the school letter is "a separate file", `fetch/deliverables.txt:65`). This is
   FORECAST: do not commit FR effort to page layout or charts until Tue 10 Nov 01:00.

## 5. Questions for Wharton (topics only; the team writes and sends them)

- **Q1.** With the IPS as a form, do Times New Roman 12, double spacing, 1-inch margins, "1 page maximum" and
  "2-page maximum" still apply, or are the 50/500-word caps the only length rules?
- **Q2.** Where do the title-page items (team name, "First Name, Last Initial", WInS username) go?
- **Q3.** Do the headings count toward 50/500, and should they be typed into the fields?
- **Q4.** Do the form's own word or character counters define the limit?

Batch them with any form screenshots the team has.

## 6. What this does not change

The TNA (form, three exact notes, 100-word reflections, Thu 22 Oct 20:00 Sydney submit) is unchanged. So are the IPS
deadline (Sat 7 Nov 09:00 Sydney), the trading freeze, the content requirements (IPS:8-70), the bans (IPS:123), the
strategy lock (IPS:73-74), the three-case Submit rule and the AI-use rules.
