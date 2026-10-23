"""Build the private review page (caplet_review.html) from REPORT.md and the September ladder-cost series."""
import html
import json
import re
from datetime import date

import markdown

SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__))  # inputs, fonts/ and outputs sit next to this script
md = open(f'{SP}/REPORT.md').read()
series = json.load(open(f'{SP}/sept_series.json'))  # [iso date, cost on 1 Jan 2027, 10y par]

# ---- body markdown: drop the H1 + byline (the page header replaces them) and the horizontal rules
md = md.split('\n## 1. The short version', 1)[1]
md = '## 1. The short version' + md
md = re.sub(r'\n---\n', '\n', md)

body = markdown.markdown(md, extensions=['tables', 'sane_lists', 'toc'], output_format='html5')

# numbered h2s -> number + title spans; collect a contents list
toc = []
def h2(m):
    hid, num, title = m.group(1), m.group(2), m.group(3)
    short = {
        'The short version': 'Short version', 'What is in the repo now': 'What is in the repo',
        'The plan in plain English': 'The plan', 'Numbers I checked independently': 'Numbers checked',
        "Thursday's vote and Friday's trades": 'Thursday and Friday', 'Authorship and the Wharton AI policy': 'Authorship',
        'Public repo and privacy': 'Privacy', "Devil's advocate: what a tough judge will ask": "Judge's questions",
        'The three deliverables': 'The deliverables', 'Housekeeping and code': 'Housekeeping and code',
        'What this teaches (for the team\'s own understanding)': 'What this teaches',
        'Calendar (Sydney time; Sydney moves to daylight time on Sun 4 Oct, the U.S. on Sun 1 Nov)': 'Calendar',
        'Fixes I recommend but did not make': 'Fixes not made',
    }.get(html.unescape(title), title)
    toc.append((hid, num, short))
    return f'<h2 id="{hid}"><span class="num">{num}</span><span>{title}</span></h2>'
body = re.sub(r'<h2 id="([^"]+)">(\d+)\. (.*?)</h2>', h2, body)
body = re.sub(r'<h2 id="([^"]+)">Appendix: (.*?)</h2>',
              lambda m: (toc.append((m.group(1), 'A', 'Sources')) or f'<h2 id="{m.group(1)}"><span class="num">A</span><span>{m.group(2)[0].upper() + m.group(2)[1:]}</span></h2>'), body)

# tables scroll inside their own box
body = body.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
# severity words become chips (text stays, colour is a second channel)
for word, cls in (('High', 'high'), ('Medium', 'med'), ('Low', 'low'), ('Competitive', 'med')):
    body = body.replace(f'<li><strong>{word}.</strong>', f'<li><span class="chip {cls}">{word}</span>')
# the ranked risk list in section 1 gets its own class
body = body.replace('<ol>\n<li><strong>Authorship.</strong>', '<ol class="risks">\n<li><strong>Authorship.</strong>', 1)

# ---- chart: static SVG (complete at rest), re-rendered to the container width by the script below
def render_svg(W):
    narrow = W < 600
    H = 250 if narrow else 300
    ml, mr, mt, mb = 52, (16 if narrow else 132), 30, 32
    d0, d1 = date(2026, 8, 3).toordinal(), date(2026, 9, 29).toordinal()
    y0, y1 = 287_500, 311_000
    X = lambda iso: ml + (date.fromisoformat(iso).toordinal() - d0) / (d1 - d0) * (W - ml - mr)
    Y = lambda v: mt + (y1 - v) / (y1 - y0) * (H - mt - mb)
    out = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="viz-title viz-desc" tabindex="0">']
    for v in (290_000, 295_000, 305_000, 310_000):
        out.append(f'<line class="grid" x1="{ml}" x2="{W - mr}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>')
        out.append(f'<text class="axis-label" x="{ml - 8}" y="{Y(v) + 4:.1f}" text-anchor="end">${v // 1000}k</text>')
    out.append(f'<line class="ref" x1="{ml}" x2="{W - mr}" y1="{Y(300_000):.1f}" y2="{Y(300_000):.1f}"/>')
    out.append(f'<text class="axis-label" x="{ml - 8}" y="{Y(300_000) + 4:.1f}" text-anchor="end">$300k</text>')
    out.append(f'<text class="ref-label" x="{ml + 6}" y="{Y(300_000) - 7:.1f}">' + ('First deposit, $300,000' if narrow else "Laura's first deposit, $300,000") + '</text>')
    ticks = ['2026-08-03', '2026-08-31', '2026-09-29'] if narrow else ['2026-08-03', '2026-08-17', '2026-08-31', '2026-09-14', '2026-09-29']
    for t in ticks:
        dt = date.fromisoformat(t)
        anchor = 'start' if t == ticks[0] else ('end' if t == ticks[-1] and narrow else 'middle')
        out.append(f'<text class="axis-label" x="{X(t):.1f}" y="{H - 10}" text-anchor="{anchor}">{dt.day} {dt.strftime("%b")}</text>')
    pts = ' '.join(f'{X(d):.1f},{Y(v):.1f}' for d, v, _ in series)
    out.append(f'<polyline class="line" points="{pts}"/>')
    # 22 Sep: last day the ladder did not fit
    d22 = next(s for s in series if s[0] == '2026-09-22')
    out.append(f'<circle class="dot" cx="{X(d22[0]):.1f}" cy="{Y(d22[1]):.1f}" r="4.5"/>')
    if not narrow:
        out.append(f'<text class="note-label" x="{X(d22[0]) - 8:.1f}" y="{Y(d22[1]) - 12:.1f}" text-anchor="end">22 Sep: ${d22[1]:,}</text>')
    last = series[-1]
    out.append(f'<circle class="dot" cx="{X(last[0]):.1f}" cy="{Y(last[1]):.1f}" r="4.5"/>')
    if narrow:
        out.append(f'<text class="end-label" x="{X(last[0]) - 8:.1f}" y="{Y(last[1]) + 20:.1f}" text-anchor="end">29 Sep: ${last[1]:,}</text>')
    else:
        out.append(f'<text class="end-label" x="{X(last[0]) + 10:.1f}" y="{Y(last[1]) + 4:.1f}">${last[1]:,}</text>')
        out.append(f'<text class="axis-label" x="{X(last[0]) + 10:.1f}" y="{Y(last[1]) + 20:.1f}">29 Sep</text>')
    out.append(f'<line class="cross" x1="0" x2="0" y1="{mt}" y2="{H - mb}" visibility="hidden"/>')
    out.append(f'<circle class="dot hover-dot" r="4.5" cx="0" cy="0" visibility="hidden"/>')
    out.append('</svg>')
    return '\n'.join(out)

rows = '\n'.join(
    f'<tr><td>{date.fromisoformat(d).strftime("%a %d %b").replace(" 0", " ")}</td><td class="n">${v:,}</td><td class="n">{y:.2f}%</td></tr>'
    for d, v, y in reversed(series))
chart = f'''<figure class="viz" id="ladder-viz">
<figcaption>
<p class="viz-title" id="viz-title">What the ten payments would cost on 1 January 2027</p>
<p class="viz-sub" id="viz-desc">Priced on each day's official Treasury curve, August to September 2026, against Laura's
$300,000 first deposit. Zero-coupon (15-Nov) basis, forward to 1 Jan 2027. It first fitted under $300,000 on 11 Sep and
was above it again on 17, 21 and 22 Sep.</p>
</figcaption>
<div class="viz-plot">{render_svg(720)}<div class="viz-tip" hidden></div></div>
<details class="viz-table"><summary>Show the numbers</summary>
<div class="table-wrap"><table><thead><tr><th>Curve date</th><th class="n">Cost on 1 Jan 2027</th><th class="n">10-year yield</th></tr></thead>
<tbody>{rows}</tbody></table></div></details>
<p class="viz-source">Source: home.treasury.gov daily par yield curves, fetched 30 Sep 2026; my own pricer (bootstrapped
discount factors), independent of the repo's code.</p>
</figure>'''

anchor = '<p><strong>What this means.</strong>'
assert anchor in body
body = body.replace(anchor, chart + '\n' + anchor, 1)

toc_html = '\n'.join(f'<li><a href="#{hid}"><span class="num">{num}</span>{html.escape(html.unescape(short))}</a></li>' for hid, num, short in toc)

page = open(f'{SP}/page_template.html').read()
page = page.replace('{{TOC}}', toc_html).replace('{{BODY}}', body).replace('{{DATA}}', json.dumps(series))
open(f'{SP}/caplet_review.html', 'w').write(page)
print('written', len(page), 'bytes;', len(toc), 'sections')
