"""Build the client-style research report PDF (plain words, diagrams, at most 30 pages).

Run from the repo root: .venv/bin/python research/insight_v1/scripts/build_client_brief.py
Output: research/insight_v1/Team_Caplet_Strategy_Brief.pdf
Every figure comes from the insight_v1 files: 00_executive_summary.md, phase_E/E6_final_spec.md (numbers reproduced by
scripts/E6_final_checks.py; "model" = a computer estimate, not a forecast), strategy_changes.md, why_us.md,
phase_C/filter_log.md, phase_D and phase_E files (distilled in brief_insights.py), phase_G/verification.md, and the
2026-27 Competition Infographic (the one quoted line). Two passes: the second fills the contents page numbers.
"""
import os
import re
import subprocess
import sys
import tempfile

import pypdfium2

sys.path.insert(0, os.path.dirname(__file__))
from brief_insights import PHASE1_EXTRA, PHASE4, PHASE5, OPEN_DECISIONS  # noqa: E402

OUT = "research/insight_v1/Team_Caplet_Strategy_Brief.pdf"
CHROME = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"
INK, MUTED, RULE, GRAY, ACCENT = "#111111", "#6b6b6b", "#e2e2e2", "#c4c4c4", "#1f5fae"
FONT = "'Liberation Sans', Arial, sans-serif"


# ---------------- diagram helpers ----------------

def svg(h, body):
    return f'<svg viewBox="0 0 800 {h}" class="fig">{body}</svg>'


def t(x, y, s, cls="n", anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{s}</text>'


def hbars(rows, vmax, label_w=250, bar_w=420, h_row=32):
    """rows: (label, value, highlighted, value_label). One accent colour for our plan; gray for the rest."""
    out = []
    for i, (lab, v, hi, vl) in enumerate(rows):
        y = 6 + i * h_row
        w = max(v / vmax * bar_w, 2)
        out.append(t(label_w - 12, y + 15, lab, "b" if hi else "n", "end"))
        out.append(f'<rect x="{label_w}" y="{y + 3}" width="{w:.1f}" height="16" fill="{ACCENT if hi else GRAY}"/>')
        out.append(t(label_w + w + 8, y + 15, vl, "b" if hi else "n"))
    return svg(12 + len(rows) * h_row, "".join(out))


def process_flow():
    steps = [("1  Foundations", "324 official lines logged"), ("2  Questions", "472 questions, 10 angles"),
             ("3  Filter", "48 questions kept"), ("4  Research", "12 specialists, 5 auditors"),
             ("5  Stress tests", "4 red teams"), ("6  Decision", "1 final plan"),
             ("7  Blind test", "ranked 1st by 3 of 3"), ("8  Final check", "19 problems found, 18 fixed")]
    out, bw, bh = [], 170, 62
    for i, (a, b) in enumerate(steps):
        row, col = divmod(i, 4)
        x, y = 10 + col * 198, 10 + row * 100
        out.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="none" stroke="{INK}"/>')
        out.append(t(x + 12, y + 26, a, "b") + t(x + 12, y + 46, b, "s"))
        if col < 3:
            out.append(f'<line x1="{x + bw + 4}" y1="{y + bh / 2}" x2="{x + 194}" y2="{y + bh / 2}" stroke="{INK}" marker-end="url(#ar)"/>')
    out.append(f'<path d="M {10 + 3 * 198 + bw / 2} {10 + bh} V 90 H {10 + bw / 2} V 108" fill="none" stroke="{INK}" marker-end="url(#ar)"/>')
    defs = f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="{INK}"/></marker></defs>'
    return svg(185, defs + "".join(out))


def funnel():
    rows = [("Questions asked", 472), ("After merging duplicates", 248), ("Passed every test", 48)]
    out = []
    for i, (lab, v) in enumerate(rows):
        y = 6 + i * 40
        w = v / 472 * 460
        x = 270 + (460 - w) / 2
        last = i == len(rows) - 1
        out.append(t(250, y + 21, lab, "b" if last else "n", "end"))
        out.append(f'<rect x="{x:.1f}" y="{y + 4}" width="{w:.1f}" height="24" fill="{ACCENT if last else GRAY}"/>')
        out.append(t(500, y + 21, str(v), "b", "middle") if w > 60 else t(x + w + 8, y + 21, str(v), "b"))
    return svg(130, "".join(out))


def knife_edge():
    W, x0 = 700, 50
    over = 173 / 185 * W
    return svg(84, f'<rect x="{x0}" y="30" width="{over:.1f}" height="22" fill="{GRAY}"/>'
                   f'<rect x="{x0 + over + 2:.1f}" y="30" width="{W - over - 2:.1f}" height="22" fill="{ACCENT}"/>'
               + t(x0, 20, "173 days: the ten bonds cost more than $300,000")
               + t(x0 + W, 72, "12 days: under $300,000 (only since 10 September)", "b", "end"))


def ladder():
    out, x0, gap, bw = [], 60, 70, 46
    for i in range(10):
        x = x0 + i * gap
        out.append(f'<rect x="{x}" y="40" width="{bw}" height="70" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>')
        out.append(t(x + bw / 2, 80, "$50k", "s", "middle") + t(x + bw / 2, 128, str(2033 + i), "s", "middle"))
    out.append(f'<path d="M {x0} 28 V 20 H {x0 + 9 * gap + bw} V 28" fill="none" stroke="{INK}"/>')
    out.append(t(x0 + (9 * gap + bw) / 2, 13, "Bought together in January 2027 for about $294,000", "b", "middle"))
    return svg(140, "".join(out))


def timeline():
    pts = [(80, "Jan 2027", "$300k arrives.", "Buy the ten payment bonds."),
           (235, "Jan 2028", "$150k arrives.", "Buy the $150k building floor;", "~$40k into world stocks."),
           (400, "2031", "Talk to partners.", "Range: the floor she owns", "up to floor + half of stocks."),
           (565, "Jan 2033", "Residency opens.", "Bonds become the reserve;", "building gift is paid."),
           (720, "2042", "Last payment.", "Ten $50k payments made.")]
    out = [f'<line x1="30" y1="46" x2="770" y2="46" stroke="{INK}"/>']
    for x, yr, *lines in pts:
        out.append(f'<circle cx="{x}" cy="46" r="5" fill="{ACCENT}"/>' + t(x, 28, yr, "b", "middle"))
        for j, ln in enumerate(lines):
            out.append(t(x, 76 + 17 * j, ln, "n" if j == 0 else "s", "middle"))
    return svg(130, "".join(out))


def money_split():
    parts = [(294, "Ten payment bonds", "$294k"), (118, "Building-floor bond", "$118k"), (40, "World stocks", "~$40k")]
    total, x, W, out = sum(p[0] for p in parts), 20, 760, []
    for i, (v, name, lab) in enumerate(parts):
        w = W * v / total
        out.append(f'<rect x="{x:.1f}" y="10" width="{w - 3:.1f}" height="26" fill="{ACCENT if i == 2 else GRAY}"/>')
        tx, anc = (x + w - 3, "end") if i == len(parts) - 1 else (x, "start")
        out.append(t(tx, 56, name, "n", anc) + t(tx, 73, lab, "s", anc))
        x += w
    return svg(84, "".join(out))


def outcome_ranges():
    rows = [("Our plan", 182, 207, 250, True), ("Earlier plan (lock in 2031)", 168, 210, 266, False)]
    lo, hi, X0, W = 140, 280, 250, 510
    sx = lambda v: X0 + (v - lo) / (hi - lo) * W  # noqa: E731
    out = []
    for v in range(140, 281, 20):
        out.append(f'<line x1="{sx(v):.1f}" y1="14" x2="{sx(v):.1f}" y2="128" stroke="{RULE}"/>' + t(sx(v), 146, f"${v}k", "s", "middle"))
    for i, (name, a, m, b, ours) in enumerate(rows):
        y, col = 48 + i * 52, (ACCENT if ours else "#8a8a8a")
        out.append(t(X0 - 14, y + 5, name, "b" if ours else "n", "end"))
        out.append(f'<line x1="{sx(a):.1f}" y1="{y}" x2="{sx(b):.1f}" y2="{y}" stroke="{col}" stroke-width="3"/>')
        out.append(f'<circle cx="{sx(m):.1f}" cy="{y}" r="6" fill="white" stroke="{col}" stroke-width="2"/>')
        out.append(t(sx(a), y - 12, f"${a}k", "s", "middle") + t(sx(m), y - 12, f"${m}k", "b", "middle") + t(sx(b), y - 12, f"${b}k", "s", "middle"))
    return svg(156, "".join(out))


def cosponsor_range():
    X0, W, hi = 40, 640, 190
    sx = lambda v: X0 + v / hi * W  # noqa: E731
    out = [f'<rect x="{sx(0)}" y="44" width="{sx(150) - sx(0):.1f}" height="28" fill="{GRAY}"/>',
           f'<rect x="{sx(150) + 2:.1f}" y="44" width="{sx(175) - sx(150) - 2:.1f}" height="28" fill="{ACCENT}"/>',
           t(sx(75), 63, "Already owned: a bond bought in 2028", "n", "middle")]
    for v, lab, anc, dx in [(0, "$0", "start", 0), (150, "Floor $150k", "end", -5), (175, "Top ≈ $175k (typical)", "start", 5)]:
        out.append(f'<line x1="{sx(v):.1f}" y1="38" x2="{sx(v):.1f}" y2="80" stroke="{INK}"/>' + t(sx(v) + dx, 34, lab, "b", anc))
    out.append(t(sx(175), 96, "+ half of the stock fund, valued on the day she speaks", "s", "end"))
    return svg(106, "".join(out))


def wins_bar():
    parts = [(23.5, "IEF", "medium-term government bonds"), (42.5, "TLH", "long-term government bonds"),
             (24.3, "2032 note", "the building floor"), (8.7, "VT", "world stocks"), (1.0, "", "")]
    x, W, out = 20, 760, []
    for v, tk, sub in parts:
        w = W * v / 100
        out.append(f'<rect x="{x:.1f}" y="10" width="{max(w - 3, 1):.1f}" height="26" fill="{ACCENT if tk == "VT" else GRAY}"/>')
        if tk:
            tx, anc = (x + w - 3, "end") if tk == "VT" else (x, "start")
            out.append(t(tx, 56, f"{tk}  {v}%", "b", anc) + t(tx, 73, sub, "s", anc))
        x += w
    return svg(84, "".join(out))


# ---------------- page content ----------------

CSS = f"""
@page {{ size: A4; margin: 22mm 24mm 20mm 24mm;
  @bottom-left {{ content: "Team Caplet · Strategy and research report · Laura Gao"; font: 7.5pt {FONT}; color: {MUTED}; }}
  @bottom-right {{ content: counter(page); font: 7.5pt {FONT}; color: {MUTED}; }} }}
@page cover {{ margin: 0; @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: {FONT}; color: {INK}; font-size: 10.3pt; line-height: 1.55; }}
section {{ break-before: page; }}
.part {{ font-size: 8pt; letter-spacing: .14em; text-transform: uppercase; color: {MUTED}; margin-bottom: 6px; }}
h1 {{ font-size: 19pt; font-weight: normal; margin: 0 0 14px 0; line-height: 1.25; }}
h2 {{ font-size: 10.3pt; font-weight: bold; margin: 16px 0 4px 0; break-after: avoid; }}
p {{ margin: 0 0 8px 0; }}
.lead {{ font-size: 11.3pt; line-height: 1.6; }}
.fig {{ width: 100%; margin: 6px 0 2px 0; font-family: {FONT}; break-inside: avoid; }}
.cap {{ font-size: 8pt; color: {MUTED}; margin: 0 0 12px 0; }}
.n {{ font-size: 12.5px; fill: {INK}; }} .b {{ font-size: 12.5px; font-weight: bold; fill: {INK}; }}
.s {{ font-size: 11px; fill: {MUTED}; }}
table {{ width: 100%; border-collapse: collapse; font-size: 9.3pt; margin: 6px 0 12px 0; }}
tr {{ break-inside: avoid; }}
th {{ text-align: left; font-weight: bold; border-bottom: 1px solid {INK}; padding: 4px 10px 4px 0; }}
td {{ border-bottom: 1px solid {RULE}; padding: 5px 10px 5px 0; vertical-align: top; }}
ul, ol {{ margin: 0 0 8px 0; padding-left: 17px; }} li {{ margin: 3px 0; break-inside: avoid; }}
.note {{ border-left: 2px solid {ACCENT}; padding: 2px 0 2px 12px; margin: 12px 0; break-inside: avoid; }}
.big {{ display: flex; gap: 24px; margin: 14px 0 8px 0; break-inside: avoid; }}
.big div {{ flex: 1; border-top: 1px solid {INK}; padding-top: 8px; }}
.big b {{ display: block; font-size: 16pt; font-weight: normal; }}
.big span {{ font-size: 8.3pt; color: {MUTED}; }}
.muted {{ color: {MUTED}; }}
.toc td {{ padding: 6px 10px 6px 0; }} .toc td:last-child {{ text-align: right; width: 12%; color: {MUTED}; }}
.toc tr.p td {{ font-weight: bold; border-bottom: 1px solid {INK}; padding-top: 14px; }}
.cover {{ page: cover; height: 296mm; padding: 24mm; position: relative; }}
.cover h1 {{ font-size: 28pt; margin-top: 70mm; }}
.cover .sub {{ font-size: 12pt; color: {MUTED}; }}
.cover .rule {{ width: 40mm; border-top: 2px solid {ACCENT}; margin: 10mm 0; }}
.cover .fine {{ position: absolute; bottom: 24mm; left: 24mm; right: 24mm; font-size: 8pt; color: {MUTED}; }}
"""

SECTIONS = []  # (part, title, body)


def sec(part, title, body):
    SECTIONS.append((part, title, body))


def bullets(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ---- Executive summary ----
sec("Executive summary", "Executive summary", f"""
<p class="lead">Laura Gao has asked us to invest $450,000 so that she can fund her creative residency in Taiwan. She
needs ten payments of $50,000 a year from 2033, made "with a high degree of certainty", and she wants to contribute
responsibly to the residency's building while keeping some flexibility.</p>
<h2>Our recommendation: keep every promise, grow the rest</h2>
<ol><li><b>January 2027.</b> Her first $300,000 buys ten U.S. government bonds, one maturing just before each $50,000
payment. From that day, the payments no longer depend on markets.</li>
<li><b>January 2028.</b> Her second deposit of $150,000 buys a bond that repays $150,000 before 2033. This is money for
the building that she owns outright. The remaining ~$40,000 goes into one global stock fund.</li>
<li><b>2031 and 2033.</b> She tells partners a range: the $150,000 she owns, up to that plus half of the stock fund. In
2033 the bonds pay the residency and the building gift is made. No trades are needed after 2028.</li></ol>
<div class="big"><div><b>10 of 10</b><span>payments secured in January 2027</span></div>
<div><b>$150k</b><span>building money owned three years before partners are asked</span></div>
<div><b>$207k</b><span>typical money for the building and flexibility in 2033 (model)</span></div>
<div><b>$169k</b><span>the same figure in the worst six years of U.S. market history</span></div></div>
<h2>Why this is the right plan for Laura</h2>
{bullets(["<b>Her promises do not depend on markets.</b> Plans that rely on markets miss a payment up to 46% of the time if her second deposit never arrives (model). Ours does not, once the bonds are bought.",
          "<b>She never has to take a number back.</b> The bottom of her 2031 range is money she already owns, and the gift can never exceed the top she announces.",
          "<b>Bad years hurt less.</b> In the worst stretch of market history, our plan still leaves $169,000 for the building, against $120,000 for the next-best design.",
          "<b>It is simple.</b> Two purchases on two dates. Nothing to manage in 2031."])}
<h2>What it costs her</h2>
<p>Less exposure to the stock market (about 9% of her money from 2028 to 2032) and a smaller share of a boom. For a
founder whose public name rides on these promises, we believe this is the right trade, and we say so openly.</p>
<h2>How we reached it</h2>
<p>We ran a research program in eight phases: we logged every official rule, asked 472 questions from ten angles, kept
the 48 that could change a decision, had twelve specialists answer them with auditors checking the work, asked four
teams to attack the plan, settled one final design, tested it blind against five other common approaches, and checked
every number one last time. In the blind test, all three reviewers playing Laura ranked our plan first.</p>
<h2>What we discovered along the way</h2>
{bullets(["This year's trading rules are public, and the $300,000 is only just enough to buy the ten payments. On most days of 2026 it would not have been.",
          "Two official competition documents were missing from our files; they are now filed.",
          "The famous quote in the case cannot be traced to Laura, and a popular story about her comes from a reporter. Neither is used.",
          "The real field is about 2,300 finishing teams, not 6,300."])}
<h2>What we need from the team</h2>
<p>Three recorded votes before the first trade, a check of the trading platform's limits, and trades placed by
2 October. The Trading Notes are due 23 October and the Investment Policy Statement on 6 November.</p>""")

# ---- Part 1: the recommendation ----
P1 = "Part 1 · Our recommendation"
sec(P1, "Understanding Laura", f"""
<p class="lead">Laura is a bestselling graphic novelist, illustrator, entrepreneur and educator. Her income comes from
publishing advances, speaking and licensing. She plans a creative residency in Taiwan and wants to fund it reliably.</p>
<table><tr><th style="width:38%">What she asked for</th><th>What it means for her portfolio</th></tr>
<tr><td>Ten payments of $50,000, 2033-2042, with "a high degree of certainty", from the portfolio alone</td><td>These come first. Secure them with bonds rather than hope markets cover them.</td></tr>
<tr><td>A responsible contribution to the building</td><td>Own a floor early, then add a share of the growth that actually happens.</td></tr>
<tr><td>A credible range for partners in 2031</td><td>The bottom of the range must be money she already has.</td></tr>
<tr><td>Flexibility as the project develops</td><td>Some money stays hers after 2033.</td></tr>
<tr><td>Balance growth with protecting capital</td><td>Take market risk only with money nobody depends on.</td></tr></table>
<h2>The insight that shaped everything</h2>
<p>Laura's career is already her biggest risk. A weak year for her books would also shrink her second deposit. So her
portfolio should not add the same kind of risk to the money her promises depend on. We protect first and grow second.</p>
<h2>Her money, in and out</h2>
{bullets(["<b>In:</b> $300,000 in January 2027 and $150,000 in January 2028. Nothing else before 2033.",
          "<b>Out:</b> $50,000 every January from 2033 to 2042, plus the building contribution in 2033.",
          "Her living costs, taxes and Taiwan's legal questions are handled elsewhere."])}""")

sec(P1, "The plan, year by year", f"""
{timeline()}
<p class="cap">Only the first two dates need trades. After that the plan runs itself.</p>
<h2>Where her $450,000 goes</h2>
{money_split()}
<p class="cap">Approximate amounts at September 2026 prices. The building-floor bond costs about $118,000 in 2028 and repays
$150,000 just before 2033. Blue marks the only money exposed to the stock market.</p>
<div class="note"><b>If the bonds cost more than $300,000 in January</b> (this happens if interest rates fall first), we
buy the latest payments first and use the 2028 deposit to finish the rest before anything else. Our model says this is
needed in about 1 case in 3. The payments are still fully secured once the 2028 money arrives.</div>""")

sec(P1, "How safe are the payments?", f"""
<p>Each bond pays out just before its payment date. Stock-market crashes, a slow year for Laura's books, or changes in
interest rates do not change what these bonds pay.</p>
{ladder()}
<p class="cap">One bond for each $50,000 payment: a "ladder".</p>
<h2>Chance of missing a payment if the 2028 deposit never arrives</h2>
{hbars([("Our plan", 0, True, "0% (secured up front)"), ("Growth-first (75% stocks)", 40.8, False, "41%"),
        ("Other market-based plans", 46, False, "up to 46%")], 50, label_w=230, bar_w=380)}
<p class="cap">Model estimates.</p>
<h2>What we are open about</h2>
<table><tr><th style="width:42%">Remaining risk</th><th>How the plan handles it</th></tr>
<tr><td>Interest rates fall before January 2027</td><td>Buy the latest payments first; the 2028 deposit completes the rest.</td></tr>
<tr><td>Rates fall <i>and</i> the 2028 deposit never comes</td><td>Up to about $31,000 of the first payment would be missing. We state this.</td></tr>
<tr><td>Building costs in Taiwan rise, so $50,000 buys less each year</td><td>Payments are fixed in U.S. dollars. We name this gap rather than hide it.</td></tr>
<tr><td>The U.S. government fails to pay</td><td>The only risk to secured payments. Remote, but named.</td></tr></table>""")

sec(P1, "What Laura can tell partners in 2031", f"""
<p class="lead">Partners who help fund a building want to know that the founder's number is real. With this plan Laura
can say, truthfully, that the first $150,000 is already owned, and that more is likely if markets hold.</p>
{cosponsor_range()}
<p class="cap">A typical case. The top of the range is fixed on the day she speaks, from what the stock fund is worth then.</p>
<div class="big"><div><b>$150k</b><span>the floor, owned three years before she speaks</span></div>
<div><b>~$174k</b><span>typical building gift in 2033 (model)</span></div>
<div><b>~$32k</b><span>typical money she keeps for flexibility (model)</span></div></div>
{bullets(["The gift is the floor plus half of the stock fund, never more than the top she announced. She cannot overpromise.",
          "The top is reached in about 7 of 10 model cases, and in 84% of two-year periods of U.S. market history.",
          "In a strong market the extra stays with her, rather than raising expectations she may not meet next time."])}""")

sec(P1, "Results in good years and bad", f"""
<h2>Money for the building and flexibility in 2033</h2>
{outcome_ranges()}
<p class="cap">Left end: a bad case (1 in 20 is worse). Circle: the typical case. Right end: a good case (1 in 20 is better).
Model estimates on JPMorgan's 2026 long-term market assumptions.</p>
<h2>The worst six years in U.S. market history since 1928</h2>
{hbars([("Our plan", 169, True, "$169k"), ("Earlier plan", 120, False, "$120k")], 220, label_w=230, bar_w=420)}
<p class="cap">Every six-year period from 1928 to 2025, replayed as 2027-2032 and adjusted to today's assumptions.</p>
<div class="note">The typical result is almost the same either way. Our plan gives up a little of the best case in
return for a much better worst case, and a building floor that is fixed years before Laura speaks to partners.</div>""")

sec(P1, "Would Laura choose this plan?", f"""
<p>We tested the plan blind. Six one-page plans, ours and five common approaches, were stripped of names and style.
Three separate reviewers, each asked to think like Laura using only the case and her own checked public words, ranked
all six. Each read them in a different order.</p>
{hbars([("Our plan", 18, True, "18"), ("Typical strong team", 15, False, "15"), ("Balanced 60/40", 12, False, "12"),
        ("Complex optimiser", 8, False, "8"), ("Growth-first (75% stocks)", 5, False, "5"),
        ("Themed / values funds", 5, False, "5")], 18, label_w=230, bar_w=420)}
<p class="cap">Ranking points: 6 for first place down to 1 for last, added across three reviewers (18 is the maximum). A
simulation, not Laura's real opinion.</p>
<h2>What the reviewers said</h2>
{bullets(["The bottom of the range is money she already owns, so she cannot overpromise.",
          "The other plans leave her promises depending on markets until 2033.",
          "The plan is honest about its own costs and gaps."])}
<div class="note"><b>Their one criticism:</b> it can read as too cautious. The answer is to say clearly where the bold
move is (the residency itself) and to state the price of certainty in one line.</div>""")

sec(P1, "The competition portfolio", f"""
<p>In the competition's trading game ($300,000, 28 September to 6 November) we recommend holding Laura's plan as it
would look in January 2028, scaled to $300,000. Every trade then shows a real part of the strategy.</p>
{wins_bar()}
<p class="cap">Recommended mix, about 1% in cash. Each fund must first be confirmed as available on the platform and within
its holding limit; alternatives are ready.</p>
<table><tr><th style="width:30%">Holding</th><th>Its job in Laura's plan</th><th style="width:22%">Trading note</th></tr>
<tr><td>Government bond funds</td><td>Stand in for the ten payment bonds</td><td>The promise</td></tr>
<tr><td>A 2032 government note</td><td>Stands in for the $150,000 building floor</td><td>The floor</td></tr>
<tr><td>A world stock fund</td><td>The growth money nobody depends on</td><td>Growth</td></tr></table>""")

# ---- Part 2: research phase by phase ----
P2 = "Part 2 · Our research, phase by phase"
sec(P2, "How the research was organised", f"""
<p>We treated the case as a real client file. The work ran in eight phases. Each handed a smaller, better set of
material to the next, and nothing moved on without a source.</p>
{process_flow()}
<p class="cap">The eight phases and what each produced.</p>
<h2>From many questions to the few that matter</h2>
{funnel()}
<p class="cap">A question survived only if its answer could change a decision, it pointed to a real source, it was not
trivial or already answered, and at least two of three sceptics agreed it should stay.</p>
<div class="note">Why work this way? It stops a clever plan being built on an unchecked fact. Every figure in this report
can be traced to an official document, a checked source, or a model we can re-run.</div>""")

sec(P2, "Phase 1 · Foundations: what the rules and facts really say", f"""
<p>We broke every official document into 324 numbered lines so that any claim can point to its exact sentence, checked
market facts at their original sources, mapped everyone with a stake in the plan, and set trading guardrails.</p>
<h2>This year's trading rules are public</h2>
<p>$300,000 of virtual cash (the same as Laura's first deposit), up to 200 trades, any listed fund or U.S. government
bond, no minimum number of sectors, no day trading, and notes that cannot be edited once saved. The limit on any one
holding is visible only after logging in.</p>
<h2>$300,000 is only just enough</h2>
<p>The ten payment bonds cost about $294,000, leaving about $5,600 spare. Earlier in 2026 the same bonds cost more.</p>
{knife_edge()}
<p class="cap">Trading days in 2026 up to 25 September.</p>
<h2>Market facts, checked at the source</h2>
{bullets(["The U.S. central bank raised its rate to 3.75-4.00% on 16 September 2026. The 10-year government bond yield was 5.17% on 25 September (an online summary claiming 4.22% was wrong).",
          "Taiwan: prices up 2.04% over the year to August; building costs up 6.53% over the year but about 3.5% a year since 2021.",
          "JPMorgan expects world stocks to return about 7.0% a year over the long run, and cash about 3.1%."])}
{PHASE1_EXTRA}
<h2>Two official documents were missing</h2>
<p>The 2026-27 Competition Guide and Infographic are now filed. The Infographic says what judges reward: "Strong teams
explain the reasoning, assumptions, and tradeoffs behind their decisions." Last year about 2,300 of 6,300+ registered
teams finished.</p>""")

sec(P2, "Phase 2 · Questions: looking from every angle", f"""
<p>Twenty question-writers, working in pairs from ten angles, produced 472 questions and collected 271 quotes.</p>
<table><tr><th style="width:32%">Angle</th><th>What it looked for</th></tr>
<tr><td>The case, line by line</td><td>What the case says, leaves out, or changed from past years</td></tr>
<tr><td>Laura's own story</td><td>Her public interviews, books and talks, and how Wharton frames her</td></tr>
<tr><td>Her career and income</td><td>How steady her income is, and what that means for the 2028 deposit</td></tr>
<tr><td>Professional practice</td><td>How pension funds and private-wealth advisers handle promises like hers</td></tr>
<tr><td>Markets in 2026</td><td>Interest rates, stocks, AI, Taiwan and currency</td></tr>
<tr><td>Future partners</td><td>What a co-funder checks before trusting a founder's number</td></tr>
<tr><td>Judges and past winners</td><td>What strong teams do, and what a "typical strong team" will submit</td></tr>
<tr><td>Her own words</td><td>Quotes collected so they can be checked word for word</td></tr>
<tr><td>Client synthesis</td><td>Her goals and limits in one picture; Laura as a buyer choosing between firms</td></tr>
<tr><td>Contrarian</td><td>The strongest case against our own plan</td></tr></table>
<h2>The questions that mattered most</h2>
{bullets(["How much money should stay free for flexibility after the reserve, and by what rule?",
          "Which \"if this happens, we do that\" rules must be fixed in advance?",
          "What do we do if interest rates fall before January 2027 and the bonds cost more than $300,000?",
          "Should the trading game show Laura's first-year portfolio, or the plan once all three jobs exist?",
          "What does \"thoughtful risk\" mean for a founder like Laura?",
          "How should a range be told to partners without overpromising?"])}""")

sec(P2, "Phase 3 · Filter: keeping only what changes a decision", f"""
<p>Duplicates were merged, leaving 248 questions. Each then faced three sceptics: a competition judge, a checker for
questions already answered, and a statistician hunting for wrong assumptions. 48 survived.</p>
<h2>Why questions were cut</h2>
{hbars([("Already answered by earlier work", 318, False, "318"), ("Trivial", 95, False, "95"),
        ("Would not change any decision", 55, False, "55"), ("Built on a wrong assumption", 27, False, "27"),
        ("Cannot be answered", 26, False, "26"), ("Too complex for its value", 11, False, "11")], 318, label_w=280, bar_w=400)}
<p class="cap">Reasons the sceptics gave (one question can receive several).</p>
<h2>Where the 48 surviving questions landed</h2>
{hbars([("Communication and wording", 15, True, "15"), ("The computer model", 9, True, "9"),
        ("Laura's behaviour and risk", 6, True, "6"), ("Professional practice", 6, True, "6"),
        ("Co-sponsors and the 2031 range", 4, True, "4"), ("Interest rates", 2, True, "2"),
        ("Competition rules", 2, True, "2"), ("What Wharton is testing", 2, True, "2"),
        ("Stocks", 1, True, "1"), ("Taiwan and currency", 1, True, "1")], 15, label_w=280, bar_w=400, h_row=28)}
<div class="note">The lesson: most questions that sound important fail a plain test. The biggest group of survivors was
about how to explain the plan, not about the investments themselves.</div>""")

for title, body in PHASE4:
    sec(P2, title, body)
for title, body in PHASE5:
    sec(P2, title, body)

sec(P2, "Phase 6 · Decision: the ten insights behind the plan", f"""
<table><tr><th style="width:36%">Question</th><th>What we concluded</th></tr>
<tr><td>When two designs give the same typical result, which wins?</td><td>The one with the better bad case and fewer rules: $182k vs $168k in a bad case, $207k vs $210k typically (model); $169k vs $120k in the worst historical stretch.</td></tr>
<tr><td>What job is Laura hiring a firm for?</td><td>To make promises no market or future contract can take back: payments first, then a building floor from her own earnings.</td></tr>
<tr><td>Is "high certainty" true?</td><td>Yes, because it is bought, not forecast, with two honest gaps: the January 2027 price can exceed $300,000 (about 1 case in 3), and fixed dollars buy less as prices rise (at 2.5% inflation, the 2042 payment is worth about $33,700 in today's money).</td></tr>
<tr><td>Why so little stock for a founder who likes bold moves?</td><td>The caution is forced by arithmetic, not chosen for her personality: the payments use about 98% of the first deposit. All money nobody relies on is fully in stocks.</td></tr>
<tr><td>How is the 2031 range set without overpromising?</td><td>By a rule: bottom = what she owns; top = a market value on the day, capped; any extra stays hers; the chance of reaching the top is stated.</td></tr>
<tr><td>What makes this more than a textbook plan?</td><td>Each deposit buys one promise when it arrives. The second deposit's own $150,000 becomes the building floor. That rule is specific to Laura.</td></tr>
<tr><td>What should the trading game show?</td><td>Her plan on the first day all three jobs exist (January 2028), scaled to $300,000, and every note says so.</td></tr>
<tr><td>Which words survive a permanent note?</td><td>Never "match", "promised" or "guaranteed". Say "moves like" or "stands in for": most bonds in the long bond fund mature after 2042.</td></tr>
<tr><td>How do the three notes show "supported, tested, refined" honestly?</td><td>One is tested against numbers written down before the trade; one is "refined" only if the team's log shows the change was decided first; one tells the true story of dropping growth-first after testing.</td></tr>
<tr><td>How much fits in a 500-word IPS?</td><td>About 12 ideas in 10 short blocks, one number, then tested on six outside readers.</td></tr></table>""")

sec(P2, "Phase 6 · Decision: what changed from the earlier plan", f"""
<table><tr><th style="width:34%">Change</th><th>Why</th></tr>
<tr><td><b>Vote before any trade</b></td><td>Notes are permanent. Trading before the team decides could contradict the plan later.</td></tr>
<tr><td><b>Central idea: a split of jobs</b>, not a ban on stocks until 2028</td><td>A ban is broken on day one by the stock fund in the trading game.</td></tr>
<tr><td><b>Game portfolio: three jobs</b> instead of roughly 65% bonds and 35% stocks</td><td>Three jobs give three distinct, honest notes. Four trades cost $100 in fees.</td></tr>
<tr><td><b>Notes written by students</b>, short, checked by two outside readers</td><td>Notes cannot be edited, and the AI policy requires the students' own words.</td></tr>
<tr><td><b>Building floor bought in 2028</b>, not 80% of a stock sleeve locked in 2031</td><td>Same typical result, better bad cases, fewer rules. Cost: a smaller typical gift ($174k vs about $186-188k).</td></tr>
<tr><td><b>A capped 2031 range</b> with the chance of reaching the top</td><td>A top taken from a model landed in the range only 62-93% of the time.</td></tr>
<tr><td><b>Certainty defined by price, with two named gaps</b></td><td>"Fits inside $300,000" and "bought in January 2027" fail in about 1 case in 3, so they cannot be headlines.</td></tr>
<tr><td><b>Buy on arrival, latest payments first</b></td><td>If short of money, this leaves less unfunded ($31.4k vs $47.7k if rates fall 1 point and the deposit never comes).</td></tr>
<tr><td><b>2028: finish the payments first</b></td><td>The joint worst case is named once: $11,957 or $31,413 of the first payment unfunded if rates fall 0.5 or 1 point.</td></tr>
<tr><td><b>2033: no currency conversion or hedge</b></td><td>Currency contracts are derivatives, banned in the game; a hedge would cost about 5.9%.</td></tr>
<tr><td><b>Costs paid from the stock fund only</b></td><td>A 1% fee on the stock fund costs about $3k (typical); on everything, about $31k.</td></tr>
<tr><td><b>A simple IPS</b>: 10 blocks, about 12 ideas, one number</td><td>An early draft had about 55 ideas; last year's lesson was "over-complex".</td></tr></table>
<h2>What we considered and rejected</h2>
{bullets(["Waiting for better bond prices or buying in stages: no reliable gain.",
          "Inflation-linked U.S. bonds: they track U.S. prices, not Taiwan building costs.",
          "A Taiwan fund, AI or theme tilts: concentration and tokenism.",
          "Locking growth in 2031 (the earlier design): kept as the documented alternative for the team's vote."])}
<p class="muted">Kept unchanged from the team's original thinking: buy all ten payments first and hold them to the end;
latest payments first; the only remaining risk is a U.S. default; flexibility after 2033; the pre-mortem discipline.</p>""")

sec(P2, "Phases 7 and 8 · Blind test and final check", f"""
<h2>Phase 7 · Blind test</h2>
<p>Six anonymous plans were written to the same length and layout, and a fairness checker removed loaded words. Three
reviewers playing Laura ranked all six; ours was first every time (full results on the "Would Laura choose this plan?"
page). Their shared request, to show the balance between caution and ambition more clearly, is now on the team's list.</p>
<h2>Phase 8 · Final check</h2>
<p>A final checker compared every output with the plan and re-ran the numbers.</p>
{hbars([("Serious", 1, False, "1: a privacy slip"), ("Important", 7, False, "7"), ("Minor", 11, False, "11")], 12, label_w=200, bar_w=400)}
<p class="cap">Problems found. 18 of 19 were fixed; one minor item was correct as an illustration and left.</p>
{bullets(["<b>Serious:</b> one filed question quoted a line we had excluded for privacy. The text was removed.",
          "<b>Important:</b> outdated figures that had since been corrected; one of Laura's own words placed where only the case's words belong; a claim that the plan \"never misses\" without its stated exception; and funds named without the \"check availability first\" warning.",
          "After the fixes, every figure matches the final plan, and all files agree on dates, portfolio, notes and rules."])}""")

# ---- Part 3 ----
P3 = "Part 3 · Next steps"
sec(P3, "Decisions for the team", f"""
{OPEN_DECISIONS}
<h2>Timeline</h2>
<table><tr><th style="width:24%">When</th><th>Action</th></tr>
<tr><td>Before trading</td><td>Record the three votes. Log in to the platform: record the holding limit, check each fund is listed, test the note length safely.</td></tr>
<tr><td>By 2 October (U.S.)</td><td>Place the trades. Each note is written by one student and checked by another.</td></tr>
<tr><td>23 October</td><td>Submit the Trading Notes Analysis.</td></tr>
<tr><td>6 November</td><td>Submit the Investment Policy Statement. Trading ends and the strategy is final.</td></tr></table>""")

sec(P3, "Lessons and plain-word glossary", f"""
<h2>Three lessons from this work</h2>
<ol><li><b>Match money to its job.</b> Money someone relies on is protected; only spare money takes risk.</li>
<li><b>Check before you build.</b> Several popular "facts" (a quote, a story about Laura, a rule, a market figure) were wrong.</li>
<li><b>Simple beats clever.</b> The recommended plan has two purchase dates and nothing to manage afterwards.</li></ol>
<h2>Glossary</h2>
<table>
<tr><td style="width:26%"><b>Bond</b></td><td>A loan to the U.S. government that repays a fixed amount on a fixed date.</td></tr>
<tr><td><b>Ladder</b></td><td>Several bonds maturing in different years, one for each payment.</td></tr>
<tr><td><b>Building floor</b></td><td>The $150,000 for the building that Laura owns from 2028, whatever markets do.</td></tr>
<tr><td><b>Stock fund</b></td><td>One fund that owns thousands of companies around the world.</td></tr>
<tr><td><b>Interest rates fall</b></td><td>Bonds become more expensive to buy; this is why the January price matters.</td></tr>
<tr><td><b>Model</b></td><td>A computer simulation of thousands of possible futures. It gives estimates, not forecasts.</td></tr>
<tr><td><b>Bad / typical / good case</b></td><td>The result that 1 in 20 futures is worse than / the middle result / 1 in 20 is better than.</td></tr>
<tr><td><b>Red team</b></td><td>A group asked to attack a plan and find its weaknesses.</td></tr>
<tr><td><b>Trading game (WInS)</b></td><td>The competition's simulator, with $300,000 of virtual cash.</td></tr>
<tr><td><b>IPS</b></td><td>Investment Policy Statement: the rules the portfolio will follow.</td></tr></table>
<p class="muted" style="margin-top:14px">Where the detail is: the Trading Notes pack and IPS specification are the working checklists; the
831-page research record holds every question, source, model and check behind this report.</p>""")


# ---------------- assemble and render ----------------

def build(page_of):
    rows, last_part = [], None
    for part, title, _ in SECTIONS:
        if part != last_part:
            rows.append(f'<tr class="p"><td>{part}</td><td></td></tr>')
            last_part = part
        rows.append(f'<tr><td>{title}</td><td>{page_of.get(title, "")}</td></tr>')
    cover = f"""<div class="cover"><h1>Keep every promise,<br>grow the rest</h1>
<div class="sub">Investment strategy and research report for Laura Gao<br>Wharton Global High School Investment Competition 2026-27</div>
<div class="rule"></div><div class="sub" style="font-size:10pt">Team Caplet · September 2026</div>
<div class="fine">Prepared for Team Caplet with an AI research assistant (Claude Code). It is research and inspiration,
not text to submit: the team decides the strategy, writes its Trading Notes and IPS in its own words, and records AI use
as Wharton requires. "Model" figures are computer estimates, not forecasts. Every trade is subject to the team's vote
and a check of the trading platform.</div></div>"""
    toc = f'<section style="break-before:auto"><div class="part">Contents</div><h1>Contents</h1><table class="toc">{"".join(rows)}</table></section>'
    body = "".join(f'<section><div class="part">{p}</div><h1>{ti}</h1>{b}</section>' for p, ti, b in SECTIONS)
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{cover}{toc}{body}</body></html>"


def render(html):
    h = os.path.join(tempfile.mkdtemp(), "brief.html")
    open(h, "w", encoding="utf-8").write(html)
    subprocess.run([CHROME, "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + h],
                   check=True, capture_output=True)


def find_pages():
    doc, found = pypdfium2.PdfDocument(OUT), {}
    texts = [re.sub(r"\s+", " ", doc[i].get_textpage().get_text_range()) for i in range(len(doc))]
    for _, title, _ in SECTIONS:
        key = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", title)).replace("&amp;", "&")
        for i in range(2, len(texts)):
            if key in texts[i]:
                found[title] = i + 1
                break
    return found, len(doc)


render(build({}))
pages, n = find_pages()
render(build(pages))
pages2, n = find_pages()
missing = [ti for _, ti, _ in SECTIONS if ti not in pages2]
print("wrote", OUT, os.path.getsize(OUT) // 1024, "KB,", n, "pages; missing in contents:", missing)
