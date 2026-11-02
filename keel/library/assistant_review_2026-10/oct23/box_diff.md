# TNA instructions: Box check and diff, Fri 23 Oct 2026 (04:01-04:07 UTC = 15:01-15:07 Sydney)

All files in this folder are untrusted downloads. Parsers ran with `venv/bin/python -I` from `SP/oct23/scripts/`.
Fetched with curl through the session proxy, browser User-Agent, `-L` (follow redirects), cookies kept per share.

## 1. What was fetched

| # | URL | UTC time | HTTP / type / bytes | Saved as | sha256 |
|---|---|---|---|---|---|
| 1 | https://upenn.app.box.com/s/3pxn798a1lnlifkikj4g56srmg2ijuo6 (shared-link page) | 04:01:18 | 200 html 39,557 | `share_page.html` | 28e3f3bc0ead8eee4a1f91f467b265faa755c84d46520ff76ff45f930ea9160f |
| 2 | https://upenn.app.box.com/index.php?rm=box_download_shared_file&shared_name=3pxn798a1lnlifkikj4g56srmg2ijuo6&file_id=f_2466427461453 (redirects to public.boxcloud.com/.../download) | 04:01:38 | 200 application/pdf 62,427 | `dl_endpoint.bin` = `TNA_box_2026-10-23.pdf` | 72bbc4a90ba02dd17dcacc0bea4339fb261f6aa33483784a275d7b3083d05d52 |
| 3 | https://upenn.app.box.com/shared/static/3pxn798a1lnlifkikj4g56srmg2ijuo6 (redirects to boxcloud) | 04:01:39 | 200 application/pdf 62,427 | `static.bin` | 72bbc4a9... (identical to #2) |

Page JSON (#1): file name "2026_WGY_Trading Notes Analysis-FINAL.pdf", id 2466427461453, file_version 2735172571053,
etag "1" (never re-uploaded), size 62,427, Box sha1 b7fa353d153ad93d525fee20ac4609476373acbf = sha1 of both downloads.
PDF metadata: 2 pages, InDesign 21.4, Created = Modified = 2026-09-10 15:21:36 -04:00.

**The Box PDF is byte-identical to the repo copy** `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.pdf`
(sha256 72bbc4a9..., same as `manifest.yaml:66`, received 2026-09-27).

## 2. Word-by-word diffs (script `SP/oct23/scripts/wdiff.py`)

### 2a. Box PDF text (`box_pypdf.txt`, pypdf) vs repo `2026_WGY_Trading_Notes_Analysis-FINAL.txt`
553 vs 551 words; 2 differences, both text-extraction artefacts (letter-spacing split), not wording:
- box L3 "T eam's" | repo L3 "Team's"
- box L32 "ANAL YSIS" | repo L32 "ANALYSIS"
Nothing else differs (bullets/tabs ignored). The repo .txt is a faithful transcript.

### 2b. Official "Instructions" (box L40-46) vs the team Doc's copy
`SP/oct21/tna/current_draft_21Oct.md` holds **no "Instructions" tab text** (only the Rewritten table, older rewrites,
[AI] versions and other facts), so it could not be diffed. The nearest team copy is the prompt at the top of the Doc's
"Trading Note Reflection" tab, `SP/oct19/drive/ips_report_live.md:66-69` (Doc as of 18 Oct 00:49 UTC). Differences:

| Official (TNA PDF p.2, box L43-46) | Team Doc (ips_report_live.md:66-69) |
|---|---|
| "For **EACH** Trading Note, write a reflection" (L43) | "For **the** Trading Note, **please** write a reflection" (L66) |
| en dashes "–" (L44-46) | hyphens "-" (L67-69) (cosmetic) |
| "How the **decision** supported" (L46) | "How the **trade** supported" (L69) |
| "**the client's** goals, **funding needs, or risk considerations**." (L46) | "**your client's** goals, **objectives, or constraints**." (L69) |

Lines 1-2 of the three questions ("Why your team made the investment decision." / "How the decision aligned with your
overall investment strategy.") match exactly. The Doc's copy also omits the three surrounding rules: select three notes
from executed WInS trades; include each note exactly as it appears in WInS (box L41-42); "Yes, we will verify this" (L47).

### 2c. "how those decisions ultimately shaped the IPS"
**Not in the official PDF** (no "ultimately" or "shaped" anywhere in box text). Also absent from the Competition Guide
PDF, the IPS PDF, the infographic, and the live public SMApply deliverables, FAQ, guide, client and WInS pages fetched
today (the only "ultimately" hits are three unrelated uses in the client case). Nor is it in any saved copy of the Doc
I could find (repo `team/google_drive/`, `SP/oct19/drive/ips_report_live.md`); its only other appearance is the
21 Oct panel note (`research/assistant_review_2026-10/oct21_tna/panel.md:25`), which already flagged it as unofficial.
Official equivalents: "how each decision supported, tested, or refined your overall investment strategy" and
"consistent with the strategic approach your team is developing and will later articulate in its IPS" (box L28-31);
Guide: "reflect on how those decisions supported, tested, or refined your strategy" (Guide .txt L88-89). The Guide
sentence starts with the same words ("how those decisions"), which may be where the paraphrase came from (UNVERIFIED).

## 3. Other public Wharton Box links (SMApply pages, cache-busted `?cb=<ns>`, 04:05:46-04:05:49 UTC, all HTTP 200)

| Link (page) | File (Box JSON) | UTC | sha256 of download | Same as repo? |
|---|---|---|---|---|
| upenn.box.com/s/0iib496jhswp30c12zhn6b2fret8dl30 (deliverables, IPS "Click Here") | "2026_WGY_Investment Policy-FINAL.pdf", 6 pp, PDF dated 2026-09-09 | 04:06:07 | d4aeaca75c2875fb7c6b59833f94606b729404ad0d983e34e7fe13188800df6a | yes, `manifest.yaml:54` |
| upenn.box.com/s/ullruymjf12ohi1uupqx4j6y8w4u5p06 (deliverables, sample documentation) | "26-27 School Documentation Template.pdf" | 04:06:10 | 56960d752bbbd6b87a9971dc588fa13c2f7511963831b69ee53ffa4e11eed55c | yes, `manifest.yaml:6` |
| upenn.box.com/s/i4t4b2n4ycjkev7p78mhyjsvypombkxo (client) | "2026_WGY_Gao Case Study-FINAL.pdf", 4 pp | 04:06:12 | bfb653cb9d530322b41d5290748e552d30e2db97798fa6dfb78fb80e2e1fead7 | yes, `manifest.yaml:42` |
| upenn.box.com/s/l2p0l26svbbptmcizhmswyq5f7rbyp44 (guide, infographic) | "2026_WGY_Competition Inforgraphic-FINAL.pdf", 1 p | 04:06:15 | 2827f92a989d6d72fbc253d80d975eb06bd00c86f631e83850ae17eec544ed10 | yes, `manifest.yaml:30` |
| upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf (guide) | Competition Guide, 5 pp | 04:06:27 | 3638e84692ed0d826660a65e89cad0ce7eea8c1907b6a8f00ce02c0d51fb7add | yes, `manifest.yaml:18` |

Page HTML hashes: deliverables 7791c18f35282cc1ef1a5ef9227fbbfe61d933ab1a4dbbb7aa66e89c8d27f9f7,
faqs 3e055b32ac4395f91dde3039d8254ed13e3dcd474a4554edea0d6d5903e403dc, guide bfb903fbbde4321609aa098c5f615d5d7746a1c82e35b22c6d4f4048fe7e6286,
client d7d38da9e40a72fe7df5fc780ed2a0deec9db87a3c86de4070d7bd742faca96e, wins 09c019961f2870ba2492620f36bc31b821b04b454a74d7efa04c2d210afcf4b9.

**No IPS form spec is public.** The only IPS document is the 9 Sep PDF, which still says "Submit as a PDF through
SurveyMonkey Apply" and "Maximum file size: 5 MB" (`file_0iib...txt` L92-93). The Week 4 email (Doc "Letters" tab)
supersedes that: IPS is now an SMApply form, "All other requirements remain the same." The form's fields are only
visible inside SMApply, which this office does not use; a student must read them.

### Public page text vs repo snapshots
- deliverables (vs 14 Oct), guide, client, wins (vs 14 Oct): no wording change (only "9." / "6," tokenisation).
- **FAQ changed since the 20 Oct snapshot** (`smapply_public_2026-10-20/faqs.txt:42-53` vs live `smapply_faqs.txt:42-53`):
  - "Any stock **from any exchange** available on WInS." -> "Any stock available on WInS."
  - "Any Exchange-Traded **Funds** (ETFs)" -> "Any Exchange-Traded **Fund** (ETFs)"
  - "Any Government/Treasury **Bonds from any exchange** available on WInS." -> "Any Government/Treasury **Bond** available on WInS."
  - NOT permitted: "TIPS (...)" -> "**Individual** TIPS (...)"; "STRIPS (...)" -> "**Individual** STRIPS (...)".
  Reading: the ban now targets individual TIPS/STRIPS bonds; an ETF holding them is not named as banned (interpretation,
  UNVERIFIED with Wharton). No current holding is affected (iBonds, Treasury notes/bonds, VT). `COMPETITION.md` section 4
  and CLAUDE.md "Current status" describe the 20 Oct wording and need updating; a dated snapshot should be filed.

## 4. Is the team's instructions copy current?
- **The official TNA requirements are unchanged** since the repo copy (byte-identical PDF, Box etag 1, dated 10 Sep).
- **The team Doc's prompt is not an exact copy**: it says "the trade" and "goals, objectives, or constraints" where the
  official text says "the decision" and "goals, funding needs, or risk considerations", and it drops "EACH", the
  three-notes / exact-WInS-text / "we will verify" rules. The phrase "how those decisions ultimately shaped the IPS" is
  not official. The team should score its reflections against box L41-47 (= repo .txt L42-54), not the Doc prompt.
