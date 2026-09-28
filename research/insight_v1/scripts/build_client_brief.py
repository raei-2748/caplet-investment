"""Build the client-style strategy briefing PDF (short, plain language, diagrams) from the verified run numbers.

Run from the repo root: .venv/bin/python research/insight_v1/scripts/build_client_brief.py
Output: research/insight_v1/Team_Caplet_Strategy_Brief.pdf
All numbers come from research/insight_v1/phase_E/E6_final_spec.md and scripts/E6_final_checks.py (MODEL = a model
estimate, not a forecast), the tournament files, and wins_now/securities_and_allocation_v1.md.
"""
import os
import subprocess
import tempfile

OUT = "research/insight_v1/Team_Caplet_Strategy_Brief.pdf"
CHROME = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"

NAVY, BLUE, ORANGE, AQUA, GRAY, LIGHT, INK, MUTED = "#12304f", "#2a78d6", "#eb6834", "#1baf7a", "#9aa5b1", "#e9eef4", "#1d2330", "#5b6675"


def timeline():
    pts = [(95, "Jan 2027", "$300k arrives", "Buys 10 bonds, one for each $50k payment"),
           (247, "Jan 2028", "$150k arrives", "Buys the $150k building floor; ~$40k into world stocks"),
           (400, "2031", "Talk to partners", "Announce: floor she owns, up to floor + half of stocks"),
           (553, "Jan 2033", "Residency opens", "Bonds become the operating reserve; facility gift paid"),
           (705, "2042", "Last payment", "Ten $50k payments made, one per year")]
    s = [f'<svg viewBox="0 0 800 210" class="fig"><line x1="40" y1="70" x2="770" y2="70" stroke="{GRAY}" stroke-width="3"/>']
    for x, yr, head, sub in pts:
        s.append(f'<circle cx="{x}" cy="70" r="11" fill="{BLUE}"/><text x="{x}" y="40" text-anchor="middle" class="t-b">{yr}</text>')
        s.append(f'<text x="{x}" y="105" text-anchor="middle" class="t-h">{head}</text>')
        words, line, lines = sub.split(), "", []
        for w in words:
            if len(line + " " + w) > 22:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for i, l in enumerate(lines):
            s.append(f'<text x="{x}" y="{126 + 15 * i}" text-anchor="middle" class="t-s">{l}</text>')
    s.append('</svg>')
    return "".join(s)


def money_split():
    # $450k of deposits: ladder $294k, building floor ~$118k (cost; repays $150k), stocks ~$38-40k
    parts = [(294, "Ten payment bonds", "$294k", NAVY), (118, "Building-floor bond", "$118k", BLUE), (40, "World stock fund", "~$40k", AQUA)]
    total, x, W = 452, 20, 760
    s = ['<svg viewBox="0 0 800 150" class="fig">']
    for v, name, lab, col in parts:
        w = W * v / total
        s.append(f'<rect x="{x}" y="30" width="{w - 3}" height="46" rx="4" fill="{col}"/>')
        s.append(f'<text x="{x + w / 2}" y="59" text-anchor="middle" class="t-w">{lab if w > 60 else ""}</text>')
        last = name == parts[-1][1]
        tx, anc = (x + w - 3, "end") if last else (x + 2, "start")
        s.append(f'<text x="{tx}" y="100" text-anchor="{anc}" class="t-h">{name}</text><text x="{tx}" y="118" text-anchor="{anc}" class="t-s">{lab}</text>')
        x += w
    s.append(f'<text x="20" y="18" class="t-s">Laura\'s $450,000 of deposits (2027 + 2028), by job</text></svg>')
    return "".join(s)


def outcome_ranges():
    rows = [("Our plan", 182, 207, 250, BLUE), ("Earlier plan (lock growth in 2031)", 168, 210, 266, ORANGE)]
    lo, hi, X0, W = 140, 280, 250, 520
    sx = lambda v: X0 + (v - lo) / (hi - lo) * W  # noqa: E731
    s = ['<svg viewBox="0 0 800 190" class="fig">']
    for t in range(140, 281, 20):
        s.append(f'<line x1="{sx(t)}" y1="20" x2="{sx(t)}" y2="150" stroke="{LIGHT}"/><text x="{sx(t)}" y="170" text-anchor="middle" class="t-s">${t}k</text>')
    for i, (name, a, m, b, col) in enumerate(rows):
        y = 55 + i * 60
        s.append(f'<text x="{X0 - 12}" y="{y + 5}" text-anchor="end" class="t-h">{name}</text>')
        s.append(f'<line x1="{sx(a)}" y1="{y}" x2="{sx(b)}" y2="{y}" stroke="{col}" stroke-width="10" stroke-linecap="round"/>')
        s.append(f'<circle cx="{sx(m)}" cy="{y}" r="9" fill="white" stroke="{col}" stroke-width="3"/>')
        s.append(f'<text x="{sx(a)}" y="{y - 14}" text-anchor="middle" class="t-s">${a}k</text><text x="{sx(m)}" y="{y - 14}" text-anchor="middle" class="t-b">${m}k</text><text x="{sx(b)}" y="{y - 14}" text-anchor="middle" class="t-s">${b}k</text>')
    s.append('</svg>')
    return "".join(s)


def history_worst():
    rows = [("Our plan", 169, BLUE), ("Earlier plan", 120, ORANGE)]
    s = ['<svg viewBox="0 0 800 110" class="fig">']
    for i, (n, v, c) in enumerate(rows):
        y = 20 + i * 42
        w = v / 220 * 520
        s.append(f'<text x="238" y="{y + 19}" text-anchor="end" class="t-h">{n}</text><rect x="250" y="{y}" width="{w}" height="28" rx="4" fill="{c}"/><text x="{258 + w}" y="{y + 19}" class="t-b">${v}k</text>')
    s.append('</svg>')
    return "".join(s)


def cosponsor_range():
    s = ['<svg viewBox="0 0 800 170" class="fig">']
    X0, W, lo, hi = 60, 680, 0, 190
    sx = lambda v: X0 + (v - lo) / (hi - lo) * W  # noqa: E731
    s.append(f'<rect x="{sx(0)}" y="50" width="{sx(150) - sx(0)}" height="44" rx="4" fill="{NAVY}"/>')
    s.append(f'<text x="{(sx(0) + sx(150)) / 2}" y="77" text-anchor="middle" class="t-w">$150k: already owned (a bond bought in 2028)</text>')
    s.append(f'<rect x="{sx(150) + 2}" y="50" width="{sx(175) - sx(150) - 2}" height="44" rx="4" fill="{AQUA}"/>')
    s.append(f'<text x="{sx(175)}" y="120" text-anchor="end" class="t-s">green = half of the stock fund on the day she speaks</text>')
    for v, lab, anc, y in [(0, "$0", "start", 30), (150, "Floor $150k", "end", 30), (175, "Top: floor + half the fund (about $175k typical)", "end", 18)]:
        s.append(f'<line x1="{sx(v)}" y1="{y + 6}" x2="{sx(v)}" y2="104" stroke="{INK}" stroke-width="1"/><text x="{sx(v) + (4 if anc == "start" else -4)}" y="{y}" text-anchor="{anc}" class="t-b">{lab}</text>')
    s.append(f'<text x="{X0}" y="150" class="t-s">The 2033 gift always lands inside the announced range. The top is reached in about 7 of 10 model paths (84% of historical windows).</text></svg>')
    return "".join(s)


def contest():
    rows = [("Our plan", 18, BLUE), ("Typical strong team (Monte Carlo 95%)", 15, GRAY), ("Balanced 60/40", 12, GRAY),
            ("Complex optimiser", 8, GRAY), ("Growth-first (75% stocks)", 5, GRAY), ("Themed / values funds", 5, GRAY)]
    s = ['<svg viewBox="0 0 800 250" class="fig">']
    for i, (n, v, c) in enumerate(rows):
        y = 12 + i * 38
        w = v / 18 * 430
        s.append(f'<text x="298" y="{y + 19}" text-anchor="end" class="{"t-b" if i == 0 else "t-h"}">{n}</text><rect x="310" y="{y}" width="{w}" height="26" rx="4" fill="{c}"/><text x="{318 + w}" y="{y + 18}" class="t-b">{v}</text>')
    s.append('</svg>')
    return "".join(s)


def miss_risk():
    rows = [("Our plan", 0, BLUE, "0% (payments bought up front)"), ("Growth-first", 40.8, ORANGE, "41%"), ("Other market-based plans", 43.5, ORANGE, "about 41-46%")]
    s = ['<svg viewBox="0 0 800 140" class="fig">']
    for i, (n, v, c, lab) in enumerate(rows):
        y = 10 + i * 42
        w = max(v / 50 * 440, 3)
        s.append(f'<text x="268" y="{y + 19}" text-anchor="end" class="t-h">{n}</text><rect x="280" y="{y}" width="{w}" height="28" rx="4" fill="{c}"/><text x="{288 + w}" y="{y + 19}" class="t-b">{lab}</text>')
    s.append('</svg>')
    return "".join(s)


def wins_bar():
    parts = [(23.5, "IEF", "7-10y Treasuries", NAVY), (42.5, "TLH", "10-20y Treasuries", "#1f4c7a"),
             (24.3, "2032 note / IBTM", "building floor", BLUE), (8.7, "VT", "world stocks", AQUA), (1.0, "", "cash", GRAY)]
    s = ['<svg viewBox="0 0 800 140" class="fig">']
    x, W = 20, 760
    for v, t, sub, c in parts:
        w = W * v / 100
        s.append(f'<rect x="{x}" y="20" width="{max(w - 3, 2)}" height="46" rx="4" fill="{c}"/>')
        if w > 50:
            s.append(f'<text x="{x + w / 2}" y="48" text-anchor="middle" class="t-w">{v}%</text>')
            s.append(f'<text x="{x + 2}" y="88" class="t-h">{t}</text><text x="{x + 2}" y="106" class="t-s">{sub}</text>')
        x += w
    s.append('</svg>')
    return "".join(s)


CSS = f"""
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'DejaVu Sans', Arial, sans-serif; color: {INK}; font-size: 10.2pt; line-height: 1.5; }}
.pg {{ width: 210mm; height: 297mm; padding: 20mm 20mm 18mm 20mm; position: relative; page-break-after: always; overflow: hidden; }}
.pg:last-child {{ page-break-after: auto; }}
.foot {{ position: absolute; bottom: 9mm; left: 20mm; right: 20mm; font-size: 7.5pt; color: {MUTED};
         display: flex; justify-content: space-between; border-top: 1px solid {LIGHT}; padding-top: 5px; }}
.kicker {{ font-size: 8.5pt; letter-spacing: .12em; text-transform: uppercase; color: {BLUE}; font-weight: bold; margin-bottom: 4px; }}
h1 {{ font-size: 21pt; color: {NAVY}; margin: 0 0 12px 0; line-height: 1.2; }}
h2 {{ font-size: 12pt; color: {NAVY}; margin: 16px 0 6px 0; }}
p {{ margin: 0 0 9px 0; }}
.lead {{ font-size: 12pt; color: #2b3445; line-height: 1.55; }}
.fig {{ width: 100%; margin: 6px 0 4px 0; }}
.caption {{ font-size: 8.2pt; color: {MUTED}; margin-bottom: 12px; }}
.t-b {{ font: bold 13px 'DejaVu Sans'; fill: {INK}; }} .t-h {{ font: 12.5px 'DejaVu Sans'; fill: {INK}; }}
.t-s {{ font: 11px 'DejaVu Sans'; fill: {MUTED}; }} .t-w {{ font: bold 12.5px 'DejaVu Sans'; fill: white; }}
.cards {{ display: flex; gap: 10px; margin: 12px 0; }}
.card {{ flex: 1; background: #f4f7fb; border-top: 3px solid {BLUE}; border-radius: 4px; padding: 10px 12px; }}
.card .num {{ font-size: 19pt; font-weight: bold; color: {NAVY}; line-height: 1.1; }}
.card .lab {{ font-size: 8.4pt; color: {MUTED}; margin-top: 3px; }}
.callout {{ background: #f4f7fb; border-left: 4px solid {BLUE}; padding: 10px 14px; border-radius: 3px; margin: 10px 0; }}
table {{ width: 100%; border-collapse: collapse; font-size: 9pt; margin: 8px 0 10px 0; }}
th {{ text-align: left; color: {NAVY}; border-bottom: 2px solid {NAVY}; padding: 5px 6px; }}
td {{ border-bottom: 1px solid {LIGHT}; padding: 6px; vertical-align: top; }}
ul {{ margin: 0 0 8px 0; padding-left: 18px; }} li {{ margin: 3px 0; }}
.cover {{ background: {NAVY}; color: white; }}
.cover h1 {{ color: white; font-size: 30pt; margin-top: 60mm; }}
.cover .sub {{ font-size: 14pt; color: #bcd3ec; margin-bottom: 30mm; }}
.cover .meta {{ font-size: 10pt; color: #dce6f2; line-height: 1.8; }}
.cover .note {{ position: absolute; bottom: 22mm; left: 20mm; right: 20mm; font-size: 8.3pt; color: #bcd3ec; border-top: 1px solid #3a5a7c; padding-top: 10px; }}
.bar {{ height: 6px; width: 60mm; background: {AQUA}; margin: 0 0 10mm 0; }}
"""


def pg(n, body, kicker=""):
    k = f'<div class="kicker">{kicker}</div>' if kicker else ""
    return f'<div class="pg">{k}{body}<div class="foot"><span>Team Caplet · Strategy proposal for Laura Gao · Internal briefing, not for submission</span><span>{n}</span></div></div>'


pages = []
pages.append("""<div class="pg cover"><h1>A plan that keeps<br>every promise</h1><div class="bar"></div>
<div class="sub">Strategy proposal for Laura Gao<br>Wharton Global High School Investment Competition 2026-27</div>
<div class="meta">Prepared by Team Caplet · September 2026<br>For the team's review before the Trading Notes (23 Oct) and the Investment Policy Statement (6 Nov)</div>
<div class="note">Internal briefing written in the style of a client proposal. AI-generated research (Claude Code) summarising the team's
insight_v1 research run; not text to submit. The team decides and writes every deliverable in its own words and records AI use in its Works Cited.
Figures marked "model" are simulation estimates, not forecasts. Full evidence: Team_Caplet_insight_v1_research_record.pdf.</div></div>""")

pages.append(pg(2, f"""<h1>Our recommendation in one page</h1>
<p class="lead">Laura has made a promise: <b>$50,000 a year for ten years</b> to her creative residency in Taiwan, starting in 2033.
She also wants to put <b>as much as responsibly possible</b> toward the building, and to tell future partners a figure she can stand behind.</p>
<p class="lead">Our plan gives each dollar one job. <b>Money that other people will rely on is bought when it arrives and held.</b>
Money nobody relies on is invested for growth.</p>
<div class="cards"><div class="card"><div class="num">10 of 10</div><div class="lab">operating payments bought in Jan 2027, before any money takes stock-market risk</div></div>
<div class="card"><div class="num">$150k</div><div class="lab">building floor already owned before Laura speaks to partners in 2031</div></div>
<div class="card"><div class="num">$207k</div><div class="lab">typical money for the building and flexibility in 2033 (model median)</div></div></div>
<h2>Why this plan</h2>
<ul><li><b>The payments cannot be taken away by markets.</b> Other plans miss a payment 41-46% of the time if the 2028 deposit falls through (model). Ours: never, once bought.</li>
<li><b>Laura never has to walk back a number.</b> The bottom of her 2031 range is a bond she already owns.</li>
<li><b>Bad years hurt less.</b> In the worst six-year stretch of U.S. market history since 1928, our plan still leaves $169k for the building, against $120k for the earlier plan.</li>
<li><b>It is simple.</b> Three decisions on three dates; nothing to trade in 2031.</li></ul>
<div class="callout"><b>What it costs:</b> less stock-market exposure (about 9% of her money from 2028 to 2032) and a smaller share of any stock-market boom.
We think that is the right trade for a founder whose name rides on these promises, and we say so plainly.</div>""", "Summary"))

pages.append(pg(3, f"""<h1>What Laura asked for</h1>
<table><tr><th style="width:32%">Her goal (from the case)</th><th>What it means for the plan</th></tr>
<tr><td><b>Fund ten $50,000 payments</b>, 2033-2042, "with a high degree of certainty", from the portfolio alone</td><td>These payments come first. We lock them in with U.S. Treasury bonds rather than hope markets cover them.</td></tr>
<tr><td><b>Contribute responsibly to the building</b> after setting aside the operating reserve</td><td>A floor she owns plus a share of growth, so the gift is real and sized to what the markets actually delivered.</td></tr>
<tr><td><b>Tell co-sponsors a credible range</b> in 2031, without overpromising</td><td>The range's bottom is already bought; the top is capped so the gift always lands inside it.</td></tr>
<tr><td><b>Keep financial flexibility</b> as the project develops</td><td>Half of the stock fund stays with her after 2033 (about $32k typical, model).</td></tr>
<tr><td><b>Balance growth with protecting capital</b>; she takes "thoughtful risks"</td><td>Her career already carries the big risk; the portfolio takes market risk only with money nobody depends on.</td></tr></table>
<h2>Her money, in and out</h2>
<ul><li><b>In:</b> $300,000 at the start of 2027; $150,000 at the start of 2028 (from books, speaking and licensing).</li>
<li><b>Out:</b> $50,000 each January 2033-2042 to the residency, plus the building contribution in 2033.</li>
<li>Living costs are covered elsewhere; taxes and Taiwan legal issues are outside this plan.</li></ul>""", "Understanding the client"))

pages.append(pg(4, f"""<h1>The plan, year by year</h1>
{timeline()}
<div class="caption">Five dates. Only the first three involve a decision; after 2033 the plan runs itself.</div>
<h2>Where her $450,000 goes</h2>
{money_split()}
<div class="caption">The building-floor bond costs about $118k in 2028 and repays $150k just before 2033. Approximate amounts at September 2026 prices (they include the small 2027 leftover); they move with interest rates.</div>
<div class="callout"><b>If bond prices rise before January 2027</b> (so the ten bonds cost more than $300,000), we buy the latest payments first and the 2028 deposit completes the rest before anything else happens.
In about 1 in 3 rate scenarios this is needed; the payments are still fully bought once the 2028 money arrives.</div>""", "How it works"))

pages.append(pg(5, f"""<h1>How certain are the payments?</h1>
<p class="lead">Once the ten bonds are bought, each one pays out just before its payment date. Stock-market falls, a bad year for book sales,
or a change in interest rates do not change what those bonds pay.</p>
<h2>Chance of missing a payment if the 2028 deposit never arrives</h2>
{miss_risk()}
<div class="caption">Model estimates. The 2028 deposit comes from book, speaking and licensing income, which Laura has herself described as unstable (verified public interview, 2021).</div>
<h2>What we are honest about</h2>
<table><tr><th style="width:34%">Remaining risk</th><th>How the plan handles it</th></tr>
<tr><td>Bond prices rise before Jan 2027</td><td>Buy latest payments first; the 2028 deposit completes the ladder first.</td></tr>
<tr><td>Prices rise <i>and</i> the 2028 deposit never comes</td><td>Up to about $31k of the first (2033) payment would be unfunded. We state this openly.</td></tr>
<tr><td>Costs in Taiwan rise; a fixed $50k buys less each year</td><td>Payments are certain in U.S. dollars; we name the currency and inflation gap rather than hide it.</td></tr>
<tr><td>The U.S. government fails to pay its bonds</td><td>The only risk to bought payments; we treat it as remote but name it.</td></tr></table>""", "Certainty"))

pages.append(pg(6, f"""<h1>What Laura can tell co-sponsors in 2031</h1>
<p class="lead">Partners fund buildings; they want to know the founder is committed and that her number is real.
Our plan lets Laura tell them, truthfully, that the first $150,000 for the building is already owned, and that more is likely if markets hold.</p>
{cosponsor_range()}
<div class="caption">Illustration at the typical (median) outcome; the top of the range is set on the day she speaks, from the stock fund's actual value.</div>
<div class="cards"><div class="card"><div class="num">$150k</div><div class="lab">floor, already owned</div></div>
<div class="card"><div class="num">~$174k</div><div class="lab">typical 2033 gift (model median)</div></div>
<div class="card"><div class="num">~$32k</div><div class="lab">typical money she keeps for flexibility</div></div></div>
<p>Because the gift can never exceed the announced top, Laura <b>cannot overpromise</b>. In a strong market the extra stays with her
rather than raising expectations she might not meet next time.</p>""", "Co-sponsors"))

pages.append(pg(7, f"""<h1>Outcomes, good years and bad</h1>
<h2>Money for the building and flexibility in 2033: bad case, typical, good case</h2>
{outcome_ranges()}
<div class="caption">Model estimates (5th percentile, median, 95th percentile) on JPMorgan's 2026 long-term assumptions. Open circle = typical outcome.</div>
<h2>Worst six-year stretch in U.S. market history since 1928</h2>
{history_worst()}
<div class="caption">Every six-year window from 1928 to 2025 replayed as 2027-2032 and rescaled to today's assumptions. Our plan's worst case is $49k better.</div>
<p>The typical outcome is almost the same either way. Our plan gives up some of the best case in exchange for a much better worst case,
and for a building floor that is fixed three years before Laura speaks to partners.</p>""", "Results"))

pages.append(pg(8, f"""<h1>Why Laura would choose this plan</h1>
<p>We tested the plan in a blind comparison. Six anonymised one-page strategies (ours and five common approaches) were ranked independently
by three reviewers simulating Laura's point of view, using only the case and her own public words. Each read them in a different order.</p>
{contest()}
<div class="caption">Ranking points (6 for first place, down to 1 for last), summed over three reviewers. A simulation, not Laura's actual view.</div>
<h2>What the reviewers said</h2>
<ul><li>"The bottom of the range is already owned, so she cannot overpromise."</li>
<li>The other plans leave the payments exposed to markets until 2033.</li>
<li>The plan names its own costs and gaps instead of hiding them.</li></ul>
<div class="callout"><b>Their one request:</b> show the balance more clearly. Say where the leap is (the residency itself is the bold move),
and state the price of certainty in one line. We will make this visible in the IPS.</div>""", "Evidence"))

pages.append(pg(9, f"""<h1>This autumn: the competition portfolio</h1>
<p>In the competition's simulator (WInS, $300,000, trading 28 Sep - 6 Nov), we hold Laura's plan as it looks on 2 January 2028,
scaled to $300,000, so every trade shows a real part of the strategy.</p>
{wins_bar()}
<div class="caption">Recommended mix at 25 September prices. Every fund is subject to checking it is listed in WInS and within the position limit; alternates are ready.</div>
<table><tr><th style="width:26%">Trade</th><th>Its job in Laura's plan</th><th style="width:22%">Trading note</th></tr>
<tr><td>Treasury bond funds (IEF, TLH)</td><td>Stand in for the ten payment bonds; they rise and fall with the cost of the promise</td><td>Note A: the promise</td></tr>
<tr><td>2032 Treasury note or IBTM</td><td>Stands in for the $150k building floor</td><td>Note B: the floor</td></tr>
<tr><td>World stock fund (VT)</td><td>The growth money nobody relies on</td><td>Note C: growth</td></tr></table>
<div class="callout"><b>Timing:</b> no rush. Target fills by Fri 2 Oct (U.S. time), hard stop 9 Oct. Notes cannot be edited, so each is written by a student and checked before the order.</div>""", "In the competition"))

pages.append(pg(10, f"""<h1>Next steps for the team</h1>
<table><tr><th style="width:18%">When</th><th>Action</th></tr>
<tr><td>Before trading</td><td>Vote and log three decisions: adopt this plan; the design (this one or the 2031-lock alternative); what WInS represents.</td></tr>
<tr><td>Before trading</td><td>Screenshot WInS Session Rules (position limit); check every fund is listed; test the note length safely.</td></tr>
<tr><td>By 2 Oct (U.S.)</td><td>Place the three trades; each student-written note checked by a second student.</td></tr>
<tr><td>Oct 2 - Oct 20</td><td>Record prices on the fill date and at the Oct 20 close for the "tested" reflection.</td></tr>
<tr><td>23 Oct</td><td>Submit the Trading Notes Analysis (three notes, reflections of 100 words or fewer).</td></tr>
<tr><td>By 26 Oct</td><td>Fix the plan's decision rules and show the balance clearly (reviewers' request).</td></tr>
<tr><td>6 Nov</td><td>Submit the IPS (50-word pitch + 500-word IPS, strict format). Trading ends; the strategy is final.</td></tr></table>
<h2>Where the detail is</h2>
<ul><li><b>Trading Notes pack</b> and <b>IPS specification</b>: the two working checklists.</li>
<li><b>Research record</b> (831 pages): every question, source, model and audit behind this briefing.</li></ul>
<p style="margin-top:16px;color:{MUTED};font-size:8.5pt">Model figures come from scripts/E6_final_checks.py (JPMorgan 2026 long-term assumptions, 200,000 simulated paths) and
history from U.S. market returns 1928-2025. Quotes of Laura are verified word for word against their original sources.</p>""", "What happens next"))

html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(pages)}</body></html>"
tmp = tempfile.mkdtemp()
h = os.path.join(tmp, "brief.html")
open(h, "w", encoding="utf-8").write(html)
subprocess.run([CHROME, "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + h], check=True, capture_output=True)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "KB")
