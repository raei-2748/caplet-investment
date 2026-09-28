"""Build the complete insight_v1 research record as one PDF (main-loop utility; no model inputs).

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/build_record_pdf.py
Needs: markdown, reportlab, pypdf (in .venv) and the Playwright headless Chromium at /opt/pw-browsers.
Output: research/insight_v1/Team_Caplet_insight_v1_research_record.pdf

Every markdown document the run produced is included in full (nothing summarised away), in reading order:
cover -> contents -> executive summary -> Part 1 deliverables -> Part 2 strategy and blind contest -> Part 3 research
record (phase by phase) -> appendices (agent brief, surviving questions, scripts and data index). Each document starts
on a new page; the PDF has bookmarks for every part and document, and a running header/footer with page numbers.
Intermediate scratch files (phase_D/_work) and raw JSON are not reprinted; Appendix B/C summarise and index them.
"""
import glob
import html
import io
import json
import os
import re
import subprocess
import tempfile

import markdown
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ROOT = "research/insight_v1"
OUT = f"{ROOT}/Team_Caplet_insight_v1_research_record.pdf"
CHROME = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"
TMP = tempfile.mkdtemp(prefix="record_")

P = lambda *a: os.path.join(ROOT, *a)  # noqa: E731
PARTS = [
    ("Part 1 - The deliverables for the team", "Start here. Six working documents for the Trading Notes (Oct 23) and the IPS (Nov 6).", [
        ("Trading Notes pack", P("trading_notes_pack.md")),
        ("IPS specification", P("ips_spec.md")),
        ("Securities and allocation", P("securities_and_allocation.md")),
        ("Why Laura would choose us", P("why_us.md")),
        ("Strategy changes and top insights", P("strategy_changes.md")),
        ("Open questions and team decisions", P("open_questions.md")),
    ]),
    ("Part 2 - The final strategy and the blind contest", "The chief strategist's specification that Part 1 is built from, and the blind 'Laura's Choice' contest.", [
        ("E6 Final strategy specification (chief strategist)", P("phase_E", "E6_final_spec.md")),
        *[(f"Contest: Firm {x} one-pager", P("phase_E", "tournament", f"firm_{x}.md")) for x in "ABCDEF"],
        ("Contest: fairness audit log", P("phase_E", "tournament", "fairness_log.md")),
        *[(f"Contest: evaluator L{i} (simulated Laura)", P("phase_E", "tournament", f"eval_L{i}.md")) for i in (1, 2, 3)],
    ]),
    ("Part 3 - The research record, phase by phase", "Everything the run produced, in the order it was made. Later files and audit corrections override earlier ones.", [
        ("Run manifest (README)", P("README.md")),
        ("Phase A - Source access check", P("phase_A", "source_access.md")),
        ("Phase A - Case register (A1)", P("phase_A", "case_register.md")),
        ("Phase A - Fact register (A2)", P("phase_A", "fact_register.md")),
        ("Phase A - Stakeholder map (A3)", P("phase_A", "stakeholder_map.md")),
        ("Phase A - WInS week-1 guardrails (A4)", P("phase_A", "wins_week1_guardrails.md")),
        ("WInS - S1 Treasury and cash sleeve", P("wins_now", "S1_treasury_sleeve.md")),
        ("WInS - S2 Growth sleeve", P("wins_now", "S2_growth_sleeve.md")),
        ("WInS - S3 Ladder and reserve detail", P("wins_now", "S3_final_report_ladder_and_reserve.md")),
        ("WInS - S4 Red team of ticket v0", P("wins_now", "S4_red_team.md")),
        ("WInS - Ticket v0 (week-1 allocation)", P("wins_now", "securities_and_allocation_v0.md")),
        ("WInS - Trading-now brief", P("phase_D", "trading_now_brief.md")),
        ("WInS - Ticket v1 (both book options)", P("wins_now", "securities_and_allocation_v1.md")),
        ("WInS - T2 Red team of ticket v1", P("wins_now", "T2_red_team.md")),
        *[(f"Phase B - {c}{k} {name}", P("phase_B", f"{c}{k}_{slug}.md")) for c, slug, name in [
            ("B1", "case_anomalies", "Case anomalies"), ("B2", "why_laura_intent", "Why Laura / designer intent"),
            ("B3", "lauras_world", "Laura's world and income"), ("B4", "practice_benchmark", "Practitioner benchmark"),
            ("B5", "macro_2026", "2026 macro and markets"), ("B6", "cosponsors", "Co-sponsors and philanthropy"),
            ("B7", "competition_meta", "Competition and judges"), ("B8", "voice_of_laura", "Voice of Laura"),
            ("B9", "client_synthesis", "Client synthesis"), ("B10", "contrarian", "Contrarian")] for k in "ab"],
        ("Phase C - Filter log", P("phase_C", "filter_log.md")),
        ("Phase C - Librarian notes", P("phase_C", "librarian_notes.md")),
        ("Phase D - D1 Rates and fixed income", P("phase_D", "D1_rates.md")),
        ("Phase D - D2 Equity and AI concentration", P("phase_D", "D2_equity_ai.md")),
        ("Phase D - D3 Quant answers", P("phase_D", "D3_quant.md")),
        ("Phase D - D3 Model v2 results", P("phase_D", "D3_model_v2_results.md")),
        ("Phase D - D4 Taiwan, FX and geopolitics", P("phase_D", "D4_taiwan_fx.md")),
        ("Phase D - D5 Co-sponsors", P("phase_D", "D5_cosponsors.md")),
        ("Phase D - D6 Client psychology", P("phase_D", "D6_behavioural.md")),
        ("Phase D - D7 Wharton intent", P("phase_D", "D7_wharton_intent.md")),
        ("Phase D - D8 Professional practice", P("phase_D", "D8_practice.md")),
        ("Phase D - D9 Communication", P("phase_D", "D9_communication.md")),
        ("Phase D - D10 Compliance", P("phase_D", "D10_compliance.md")),
        ("Phase D - D12 Client-side overflow", P("phase_D", "D12_overflow_client.md")),
        ("Phase D - Audit: rates and quant (AX1)", P("phase_D", "audit_rates_quant.md")),
        ("Phase D - Audit: D1 rates (AX1b)", P("phase_D", "audit_rates_D1.md")),
        ("Phase D - Audit: markets and rules (AX2)", P("phase_D", "audit_markets_rules.md")),
        ("Phase D - Audit: client and co-sponsors (AY1)", P("phase_D", "audit_client_cosponsors.md")),
        ("Phase D - Audit: judges, practice, communication (AY2)", P("phase_D", "audit_judges_practice_comms.md")),
        ("Phase D - D13a Laura's quotes verified", P("phase_D", "D13a_laura_quotes_verified.md")),
        ("Phase D - D13b Other quotes verified", P("phase_D", "D13b_other_quotes_verified.md")),
        ("Phase D - D13c Voice-of-Laura map", P("phase_D", "D13c_voice_map.md")),
        ("Phase E - E1 Change proposals (architect)", P("phase_E", "E1_change_proposals.md")),
        ("Phase E - E2 Red team: semifinal reader", P("phase_E", "E2_judge.md")),
        ("Phase E - E3 Red team: Laura (simulation)", P("phase_E", "E3_laura.md")),
        ("Phase E - E4 Red team: rival strategist", P("phase_E", "E4_rival.md")),
        ("Phase E - E5 Pre-mortem", P("phase_E", "E5_premortem.md")),
        ("Final verification of the deliverables", P("phase_G", "verification.md")),
    ]),
    ("Appendices", "The brief every agent worked from, the surviving questions, and the index of scripts and data.", [
        ("Appendix A - The shared agent brief", P("_context", "brief.md")),
        ("Appendix B - Questions: statistics and the 48 survivors", "GEN:questions"),
        ("Appendix C - Scripts and data index", "GEN:scripts"),
    ]),
]

CSS = """
@page { size: A4; margin: 17mm 15mm 16mm 15mm; }
html { -webkit-print-color-adjust: exact; }
body { font-family: 'DejaVu Sans', 'Liberation Sans', Arial, sans-serif; font-size: 9.2pt; line-height: 1.38;
       color: #1d2330; }
h1 { font-size: 16pt; color: #12304f; border-bottom: 2px solid #12304f; padding-bottom: 3px; margin: 0 0 8px 0; }
h2 { font-size: 12.5pt; color: #12304f; margin: 14px 0 5px 0; border-bottom: 1px solid #c9d3df; }
h3 { font-size: 10.8pt; color: #1f4c7a; margin: 11px 0 4px 0; }
h4, h5, h6 { font-size: 9.8pt; color: #1f4c7a; margin: 9px 0 3px 0; }
p { margin: 4px 0 6px 0; }
a { color: #1f4c7a; text-decoration: none; overflow-wrap: anywhere; }
ul, ol { margin: 3px 0 6px 0; padding-left: 20px; }
li { margin: 1px 0; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 9px 0; font-size: 7.6pt; line-height: 1.28;
        page-break-inside: auto; }
tr { page-break-inside: avoid; }
th { background: #e8eef5; color: #12304f; text-align: left; }
th, td { border: 1px solid #b9c5d3; padding: 3px 4px; vertical-align: top; overflow-wrap: break-word; word-break: normal; }
tr:nth-child(even) td { background: #f7f9fc; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8pt; background: #f1f3f6; padding: 0 2px;
       overflow-wrap: anywhere; }
pre { background: #f1f3f6; padding: 6px 8px; font-size: 7.6pt; white-space: pre-wrap; overflow-wrap: anywhere;
      border-left: 3px solid #b9c5d3; }
pre code { background: none; padding: 0; }
blockquote { margin: 6px 0; padding: 4px 10px; border-left: 3px solid #1f4c7a; background: #f3f6fa; color: #2b3445; }
hr { border: none; border-top: 1px solid #c9d3df; margin: 10px 0; }
.dochead { font-size: 7.8pt; color: #6b7686; margin-bottom: 6px; }
.cover { text-align: left; padding-top: 55mm; }
.cover h1 { font-size: 26pt; border: none; margin-bottom: 4px; }
.cover .sub { font-size: 13pt; color: #1f4c7a; margin-bottom: 30px; }
.cover .meta { font-size: 10pt; color: #2b3445; line-height: 1.7; }
.cover .note { margin-top: 40px; font-size: 8.8pt; color: #4a5566; border-top: 1px solid #c9d3df; padding-top: 10px; }
.divider { padding-top: 70mm; }
.divider h1 { font-size: 22pt; border: none; }
.divider p.lead { font-size: 11pt; color: #1f4c7a; }
.toc td, .toc th { border: none; border-bottom: 1px dotted #c9d3df; font-size: 8.4pt; padding: 2px 3px; background: none !important; }
.toc td.pg { text-align: right; width: 42px; }
.toc tr.part td { font-weight: bold; color: #12304f; border-bottom: 1px solid #12304f; padding-top: 8px; font-size: 9pt; }
"""


def fix_md(t):
    """Make GitHub-style markdown parse cleanly with python-markdown (blank lines before tables/lists; list indents)."""
    out, prev = [], ""
    for line in t.splitlines():
        m = re.match(r"^( +)([-*+]|\d{1,2}\.)\s", line)
        if m:
            n = len(m.group(1))
            new = 4 if n <= 4 else 8 if n <= 7 else 12
            line = " " * new + line[n:]
        is_table = line.lstrip().startswith("|")
        is_list = bool(re.match(r"^\s*([-*+]|\d{1,2}\.)\s", line))
        prev_table = prev.lstrip().startswith("|")
        prev_list = bool(re.match(r"^\s*([-*+]|\d{1,2}\.)\s", prev)) or prev.startswith("    ")
        if prev.strip() and ((is_table and not prev_table) or (is_list and not prev_list and not is_table)):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def soft_breaks(h):
    """Let long tokens (URLs, file paths, ids) wrap at natural points without squeezing table columns."""
    def fix(seg):
        seg = re.sub(r"\S{22,}", lambda m: re.sub(r"([/._\-?&=:,])", "\\1\u200b", m.group(0)), seg)
        return re.sub(r"[A-Za-z0-9]{24,}", lambda m: "\u200b".join(m.group(0)[i:i + 16] for i in range(0, len(m.group(0)), 16)), seg)
    parts = re.split(r"(<[^>]+>)", h)
    return "".join(p if p.startswith("<") else fix(p) for p in parts)


def md_to_html(text):
    return soft_breaks(markdown.markdown(fix_md(text), extensions=["tables", "fenced_code", "sane_lists"], output_format="html5"))


def page(body, title=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{body}</body></html>"


def render(html_str, name):
    h = os.path.join(TMP, name + ".html")
    pdf = os.path.join(TMP, name + ".pdf")
    open(h, "w", encoding="utf-8").write(html_str)
    subprocess.run([CHROME, "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                    f"--print-to-pdf={pdf}", "file://" + h], check=True, capture_output=True, timeout=600)
    return pdf


def gen_questions():
    qs = json.load(open(P("phase_B", "questions.json")))
    merged = json.load(open(P("phase_C", "merged_questions.json")))
    surv = json.load(open(P("phase_C", "survivors.json")))
    parked = json.load(open(P("phase_C", "parked.json")))
    quotes = json.load(open(P("phase_B", "quotes_raw.json")))
    by_lens = {}
    for q in qs:
        by_lens[q["lens"]] = by_lens.get(q["lens"], 0) + 1
    names = {"B1": "Case anomalies", "B2": "Why Laura / designer intent", "B3": "Laura's world and income", "B4": "Practitioner benchmark",
             "B5": "2026 macro and markets", "B6": "Co-sponsors", "B7": "Competition and judges", "B8": "Voice of Laura",
             "B9": "Client synthesis", "B10": "Contrarian"}
    s = ["# Appendix B - Questions: statistics and the 48 survivors", "",
         "**Serves:** background for the Trading Notes and IPS. Generated from the run's JSON files "
         "(`phase_B/questions.json`, `phase_C/merged_questions.json`, `survivors.json`, `parked.json`, `phase_B/quotes_raw.json`).", "",
         "## B.1 How many questions and quotes", "",
         f"- Phase B produced **{len(qs)} questions** from 20 agents and **{len(quotes)} quotes** (verified in Phase D13).",
         f"- The librarian merged them into **{len(merged)} distinct questions**; three skeptics judged each one.",
         f"- **{len(surv)} survived** all four filters and went to the specialists; **{len(parked)} were parked** "
         "(listed one line each in *Open questions*, Part 1).", "",
         "| Lens | Questions |", "|---|---|"]
    s += [f"| {k} {names.get(k, '')} | {v} |" for k, v in sorted(by_lens.items(), key=lambda x: int(x[0][1:]))]
    s += ["", "## B.2 The 48 questions that survived (ranked by the skeptics' priority, 1-5)", "",
          "| # | Question (merged) | Specialist | Priority | Deliverables |", "|---|---|---|---|---|"]
    for r in surv:
        t = r["canonical_text"].replace("|", "/")
        s.append(f"| {r['mid']} | {t} | {r['domain_tag']} | {r['priority']} | {', '.join(r['deliverables'])} |")
    s += ["", "## What this teaches", "Most questions that sound important fail a plain test. Filtering hard before researching is how a small team spends its time on the few that matter."]
    return "\n".join(s)


def gen_scripts():
    rows = []
    for f in sorted(glob.glob(P("scripts", "*.py"))) + sorted(glob.glob("research/verified_2026-09-27/*.py")):
        src = open(f, encoding="utf-8", errors="replace").read()
        m = re.search(r'^\s*(?:"""|\'\'\')(.*?)(?:"""|\'\'\')', src, re.S)
        doc = " ".join(m.group(1).split())[:300] if m else "(no docstring)"
        rows.append(f"| `{f.replace('research/', '')}` | {doc.replace('|', '/')} |")
    data = []
    for f in sorted(glob.glob(P("**", "*.json"), recursive=True)) + sorted(glob.glob(P("**", "*.csv"), recursive=True)):
        if "/_work/" in f:
            continue
        data.append(f"| `{f.replace('research/insight_v1/', '')}` | {os.path.getsize(f) // 1024} KB |")
    s = ["# Appendix C - Scripts and data index", "",
         "**Serves:** checking any number in this record. Every model number can be re-run from the repository root with "
         "`.venv/bin/python <script>`. The final strategy's numbers come from `insight_v1/scripts/E6_final_checks.py`; the "
         "verified base case from `verified_2026-09-27/strategy_mc.py` and `official_curve_pv.py`.", "",
         f"## C.1 Python scripts ({len(rows)})", "", "| Script | What it does (from its docstring) |", "|---|---|", *rows, "",
         f"## C.2 Data files ({len(data)})", "", "| File | Size |", "|---|---|", *data, "",
         "## What this teaches", "A number you cannot re-run is an opinion. Keeping every script beside the claim it supports is what lets a reader trust the result."]
    return "\n".join(s)


def main():
    docs = []  # (part_idx, title, path, pdf, pages)
    for pi, (ptitle, plead, items) in enumerate(PARTS):
        for di, (title, path) in enumerate(items):
            if path.startswith("GEN:"):
                text = gen_questions() if path == "GEN:questions" else gen_scripts()
                shown = "generated from the run's files"
            else:
                text = open(path, encoding="utf-8").read()
                shown = path
            body = f"<div class='dochead'>{html.escape(ptitle)} &nbsp;·&nbsp; {html.escape(shown)}</div>" + md_to_html(text)
            pdf = render(page(body, title), f"p{pi}_{di:02d}")
            docs.append((pi, title, shown, pdf, len(PdfReader(pdf).pages)))
            print(f"{len(PdfReader(pdf).pages):4d}  {title}", flush=True)

    cover = page("""<div class='cover'><h1>Team Caplet</h1><div class='sub'>insight_v1 research record: strategy for Laura Gao</div>
    <div class='meta'>Wharton Global High School Investment Competition 2026-27<br>
    Research run 27-28 September 2026 &nbsp;·&nbsp; about 90 AI agent runs, every step audited<br>
    Scope: the Trading Notes Analysis (23 Oct) and the Investment Policy Statement (6 Nov)</div>
    <div class='note'><b>AI-use statement.</b> Everything in this record was produced by an AI assistant (Claude Code) as
    research and brainstorming for the six students of Team Caplet. None of it is text to submit: the team decides and
    writes every word, and records its AI use in the Works Cited pages as Wharton's AI policy requires. Laura Gao's public
    professional record only; the team's own client documents are not included.</div></div>""", "cover")
    cover_pdf = render(cover, "a_cover")
    summ_pdf = render(page(md_to_html(open(P("00_executive_summary.md"), encoding="utf-8").read()), "summary"), "b_summary")

    dividers = {}
    for pi, (ptitle, plead, items) in enumerate(PARTS):
        lis = "".join(f"<li>{html.escape(t)}</li>" for t, _ in items)
        dividers[pi] = render(page(f"<div class='divider'><h1>{html.escape(ptitle)}</h1><p class='lead'>{html.escape(plead)}</p><ol>{lis}</ol></div>", ptitle), f"c_div{pi}")

    def toc_html(starts):
        rows = []
        rows.append(f"<tr class='part'><td>Executive summary</td><td class='pg'>{starts['summary']}</td></tr>")
        for pi, (ptitle, _, items) in enumerate(PARTS):
            rows.append(f"<tr class='part'><td>{html.escape(ptitle)}</td><td class='pg'>{starts[('div', pi)]}</td></tr>")
            for di, (t, _) in enumerate(items):
                rows.append(f"<tr><td>{html.escape(t)}</td><td class='pg'>{starts[(pi, di)]}</td></tr>")
        return page("<h1>Contents</h1><table class='toc'>" + "".join(rows) + "</table>", "contents")

    def layout(toc_pages):
        starts, n = {}, 1 + toc_pages  # cover is page 1
        starts["summary"] = n + 1
        n += len(PdfReader(summ_pdf).pages)
        k = 0
        for pi, (_, _, items) in enumerate(PARTS):
            starts[("div", pi)] = n + 1
            n += len(PdfReader(dividers[pi]).pages)
            for di in range(len(items)):
                starts[(pi, di)] = n + 1
                n += docs[k][4]
                k += 1
        return starts, n

    dummy = {k: 999 for k in layout(1)[0]}
    toc_pages = len(PdfReader(render(toc_html(dummy), "t_toc0")).pages)
    starts, total = layout(toc_pages)
    toc_pdf = render(toc_html(starts), "t_toc")
    assert len(PdfReader(toc_pdf).pages) == toc_pages

    # merge + outline
    w = PdfWriter()
    labels = []  # running header text per page

    def add(pdf, label):
        for pg in PdfReader(pdf).pages:
            w.add_page(pg)
            labels.append(label)
    add(cover_pdf, "")
    add(toc_pdf, "Contents")
    add(summ_pdf, "Executive summary")
    k = 0
    part_pages = {}
    for pi, (ptitle, _, items) in enumerate(PARTS):
        part_pages[pi] = len(w.pages)
        add(dividers[pi], ptitle)
        for di, (t, _) in enumerate(items):
            docs[k] = docs[k] + (len(w.pages),)
            add(docs[k][3], f"{ptitle.split(' - ')[0]}  ·  {t}")
            k += 1
    w.add_outline_item("Contents", 1)
    w.add_outline_item("Executive summary", starts["summary"] - 1)
    k = 0
    for pi, (ptitle, _, items) in enumerate(PARTS):
        parent = w.add_outline_item(ptitle, part_pages[pi])
        for di, (t, _) in enumerate(items):
            w.add_outline_item(t, docs[k][5], parent=parent)
            k += 1

    # running header/footer overlay
    N = len(w.pages)
    for i, pg in enumerate(w.pages):
        if i == 0:
            continue
        buf = io.BytesIO()
        pw, ph = float(pg.mediabox.width), float(pg.mediabox.height)
        c = canvas.Canvas(buf, pagesize=(pw, ph))
        c.setFont("Helvetica", 7)
        c.setFillColorRGB(0.42, 0.46, 0.53)
        c.drawString(42, ph - 26, labels[i][:120])
        c.drawString(42, 20, "Team Caplet  ·  insight_v1 research record  ·  AI-generated research, not text to submit")
        c.drawRightString(pw - 42, 20, f"page {i + 1} of {N}")
        c.save()
        buf.seek(0)
        pg.merge_page(PdfReader(buf).pages[0])
        pg.compress_content_streams(level=9)
    w.add_metadata({"/Title": "Team Caplet - insight_v1 research record (Laura Gao, Wharton 2026-27)",
                    "/Author": "Team Caplet, with AI research assistance (Claude Code)",
                    "/Subject": "Strategy research for the Trading Notes Analysis and the IPS"})
    w.page_mode = "/UseOutlines"
    w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    with open(OUT, "wb") as f:
        w.write(f)
    print(f"WROTE {OUT}: {N} pages, {os.path.getsize(OUT) / 1e6:.1f} MB; expected {total}")


if __name__ == "__main__":
    main()
