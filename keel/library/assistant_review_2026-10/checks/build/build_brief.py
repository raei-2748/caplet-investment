"""Build the team brief (A4 PDF) from hand-written content + the Aug-Sep ladder-cost series."""
import asyncio
import json
from datetime import date

from playwright.async_api import async_playwright

SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__))  # inputs, fonts/ and outputs sit next to this script
F = f'file://{SP}/fonts'
series = json.load(open(f'{SP}/sept_series.json'))


def chart(W=680, H=150):
    ml, mr, mt, mb = 46, 92, 16, 22
    d0, d1 = date(2026, 8, 3).toordinal(), date(2026, 9, 29).toordinal()
    y0, y1 = 288_000, 311_000
    X = lambda iso: ml + (date.fromisoformat(iso).toordinal() - d0) / (d1 - d0) * (W - ml - mr)
    Y = lambda v: mt + (y1 - v) / (y1 - y0) * (H - mt - mb)
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Ladder cost against the $300,000 deposit">']
    for v in (290_000, 295_000, 305_000, 310_000):
        s.append(f'<line class="g" x1="{ml}" x2="{W - mr}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>')
        s.append(f'<text class="ax" x="{ml - 6}" y="{Y(v) + 3.5:.1f}" text-anchor="end">${v // 1000}k</text>')
    s.append(f'<line class="ref" x1="{ml}" x2="{W - mr}" y1="{Y(300_000):.1f}" y2="{Y(300_000):.1f}"/>')
    s.append(f'<text class="ax" x="{ml - 6}" y="{Y(300_000) + 3.5:.1f}" text-anchor="end">$300k</text>')
    s.append(f'<text class="reflab" x="{ml + 5}" y="{Y(300_000) - 6:.1f}">Laura\'s first deposit, $300,000</text>')
    for t in ('2026-08-03', '2026-08-17', '2026-08-31', '2026-09-14', '2026-09-29'):
        dt = date.fromisoformat(t)
        a = 'start' if t.endswith('08-03') else 'middle'
        s.append(f'<text class="ax" x="{X(t):.1f}" y="{H - 6}" text-anchor="{a}">{dt.day} {dt.strftime("%b")}</text>')
    s.append('<polyline class="ln" points="' + ' '.join(f'{X(d):.1f},{Y(v):.1f}' for d, v, _ in series) + '"/>')
    d22 = next(x for x in series if x[0] == '2026-09-22')
    s.append(f'<circle class="dt" cx="{X(d22[0]):.1f}" cy="{Y(d22[1]):.1f}" r="3.6"/>')
    s.append(f'<text class="note" x="{X(d22[0]) - 7:.1f}" y="{Y(d22[1]) - 9:.1f}" text-anchor="end">22 Sep: ${d22[1]:,}</text>')
    last = series[-1]
    s.append(f'<circle class="dt" cx="{X(last[0]):.1f}" cy="{Y(last[1]):.1f}" r="3.6"/>')
    s.append(f'<text class="end" x="{X(last[0]) + 8:.1f}" y="{Y(last[1]) + 3.5:.1f}">${last[1]:,}</text>')
    s.append(f'<text class="ax" x="{X(last[0]) + 8:.1f}" y="{Y(last[1]) + 16:.1f}">29 Sep</text>')
    s.append('</svg>')
    return '\n'.join(s)


HTML = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Caplet Team Brief</title>
<style>
@font-face {{ font-family: "Public Sans"; src: url("{F}/PublicSans-normal-400.woff2") format("woff2"); font-weight: 100 900; font-style: normal; }}
@font-face {{ font-family: "Public Sans"; src: url("{F}/PublicSans-italic-400.woff2") format("woff2"); font-weight: 100 900; font-style: italic; }}
@font-face {{ font-family: "Source Serif 4"; src: url("{F}/SourceSerif4-normal-700.woff2") format("woff2"); font-weight: 200 900; font-style: normal; }}
@font-face {{ font-family: "IBM Plex Mono"; src: url("{F}/IBMPlexMono-normal-400.woff2") format("woff2"); font-weight: 400; font-style: normal; }}
:root {{
  --ink: #16201b; --ink2: #44514a; --ink3: #66726b; --rule: #d3d9d4; --wash: #eef2ef; --accent: #1d5c47;
  --series: #0f7a55; --high: #a8261b; --highwash: #fbe9e7; --med: #7d5200; --medwash: #fbf1dc;
}}
@page {{ size: A4; margin: 12mm 15mm 14mm; }}
* {{ box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; font-family: "Public Sans", Arial, sans-serif; font-size: 9pt; line-height: 1.38; color: var(--ink); }}
h1 {{ font-family: "Source Serif 4", Georgia, serif; font-weight: 700; font-size: 21pt; line-height: 1.1; margin: 3pt 0 5pt; letter-spacing: -0.01em; }}
h2 {{ font-family: "Source Serif 4", Georgia, serif; font-weight: 700; font-size: 12.5pt; margin: 10pt 0 4pt; break-after: avoid; }}
h3 {{ font-size: 9.4pt; font-weight: 700; margin: 7pt 0 2pt; break-after: avoid; }}
p {{ margin: 0 0 5pt; }}
ul, ol {{ margin: 0 0 5pt; padding-left: 14pt; }}
li {{ margin: 0 0 2pt; }}
code {{ font-family: "IBM Plex Mono", monospace; font-size: 8.3pt; background: var(--wash); padding: 0 2pt; border-radius: 2pt; }}
.eyebrow {{ font-size: 8pt; font-weight: 700; letter-spacing: 0.09em; text-transform: uppercase; color: var(--ink3); }}
.byline {{ font-size: 8.3pt; color: var(--ink3); margin-bottom: 8pt; padding-bottom: 6pt; border-bottom: 1.5pt solid var(--accent); }}
.box {{ border: 1pt solid var(--rule); background: #f6f8f6; border-radius: 4pt; padding: 6pt 10pt 2pt; margin: 0 0 6pt; break-inside: avoid; }}
.box h2 {{ margin-top: 0; font-size: 11.5pt; }}
.box li {{ margin-bottom: 2.5pt; }}
.steps {{ padding-left: 15pt; }}
.steps li {{ margin-bottom: 2pt; }}
table {{ width: 100%; border-collapse: collapse; margin: 1pt 0 6pt; font-size: 8.6pt; break-inside: auto; }}
tr {{ break-inside: avoid; }}
th {{ text-align: left; font-size: 7.9pt; color: var(--ink2); font-weight: 700; padding: 2.5pt 5pt; border-bottom: 1pt solid var(--ink3); }}
td {{ padding: 2.6pt 5pt; border-bottom: 0.6pt solid var(--rule); vertical-align: top; }}
td.n {{ white-space: nowrap; font-variant-numeric: tabular-nums; }}
.q td:first-child {{ width: 31%; font-weight: 600; }}
.two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0 16pt; }}
.risk {{ border-left: 3pt solid var(--high); padding: 0 0 0 8pt; margin: 0 0 5pt; break-inside: avoid; }}
.risk.m {{ border-left-color: var(--med); }}
.risk b.t {{ display: block; margin-bottom: 1pt; }}
.fix {{ color: var(--ink2); }}
.fix::before {{ content: "What we do: "; font-weight: 700; color: var(--accent); }}
.chartbox {{ break-inside: avoid; margin: 2pt 0 0; }}
.chartcap {{ font-size: 8.3pt; color: var(--ink2); margin: 0 0 2pt; }}
.chartcap b {{ color: var(--ink); }}
svg .g {{ stroke: var(--rule); stroke-width: 0.8; }}
svg .ref {{ stroke: var(--ink2); stroke-width: 1.1; }}
svg .ax {{ fill: var(--ink3); font-size: 9.5px; font-family: "Public Sans", Arial, sans-serif; }}
svg .reflab {{ fill: var(--ink2); font-size: 9.5px; font-weight: 600; font-family: "Public Sans", Arial, sans-serif; }}
svg .note {{ fill: var(--ink2); font-size: 9.5px; font-family: "Public Sans", Arial, sans-serif; }}
svg .end {{ fill: var(--ink); font-size: 10.5px; font-weight: 700; font-family: "Public Sans", Arial, sans-serif; }}
svg .ln {{ fill: none; stroke: var(--series); stroke-width: 1.8; stroke-linejoin: round; stroke-linecap: round; }}
svg .dt {{ fill: var(--series); stroke: #fff; stroke-width: 1.6; }}
.dates td:first-child {{ width: 30%; white-space: nowrap; font-variant-numeric: tabular-nums; }}
.small {{ font-size: 8.2pt; color: var(--ink2); }}
.pb {{ break-before: page; }}
.tick li {{ list-style: none; position: relative; padding-left: 2pt; }}
.tick {{ padding-left: 12pt; }}
.tick li::before {{ content: ""; position: absolute; left: -11pt; top: 2.6pt; width: 6.5pt; height: 6.5pt; border: 1pt solid var(--ink2); border-radius: 1.5pt; }}
</style></head><body>

<div class="eyebrow">Team Caplet &middot; Team brief &middot; Thursday 1 October 2026</div>
<h1>Where we are, and what we do this week</h1>
<div class="byline">From a full review of our repo on 30 Sep. Prepared with Claude Code (AI) for our planning only: not text for any submission,
and it goes in our AI-use log.</div>

<div class="box">
<h2>The bottom line</h2>
<ul>
<li><b>Our strategy is strong, and the numbers check out.</b> Root-and-Branch was re-checked from scratch against official
U.S. Treasury data, and every key number matched.</li>
<li><b>The biggest risks are no longer the maths.</b> They are authorship (Wharton's AI rules), our public GitHub repo, too
much complexity, and Friday-night logistics.</li>
<li><b>This week:</b> read the Week-One email, settle three votes on Thursday, and place our first trades on Friday night.</li>
<li><b>All six of us must be able to explain the plan in our own words.</b> The semifinal is a live presentation, and every
member has to take part.</li>
</ul>
</div>

<h2>Our plan in six steps (Root-and-Branch)</h2>
<ol class="steps">
<li><b>January 2027, the roots.</b> Laura's $300,000 buys ten dated U.S. Treasury holdings, one ending just before each
$50,000 payment (2033&ndash;2042). In WInS: iShares iBonds funds IBTM&ndash;IBTR for 2033&ndash;2037, and five Treasury
bonds for 2038&ndash;2042.</li>
<li><b>If yields fall first</b> and the ten cost more than $300,000 in January, her 2028 deposit completes them first.</li>
<li><b>January 2028, the floor.</b> Most of the $150,000 buys Treasuries that repay about $150,000 in late 2032: the least
she will give the facility.</li>
<li><b>The branch.</b> The rest (about $41,000) goes into one world stock fund (VT), held to 2033.</li>
<li><b>2031, co-sponsors.</b> She announces a range: the floor (quoted rounded down, about $145,000) up to the floor plus
half the fund's value then (about $175,000 on today's projection).</li>
<li><b>2033.</b> She gives the floor plus half the fund, capped at the announced top, so the gift cannot land outside the
range. The other half stays with her as a cushion. The ten holdings become the operating reserve and pay out one a year.</li>
</ol>
<p class="small">Our WInS &ldquo;Portfolio tab&rdquo; book is this plan on 2 January 2028, scaled to $300,000: about 66% dated
Treasuries, 24% floor (inside IBTM), 9% VT and 1% cash.</p>

<h2>Numbers we checked independently</h2>
<table>
<tr><th>What</th><th>Result</th></tr>
<tr><td>Cost of the ten payments, 28 Sep Treasury curve</td><td class="n">$289,119 (matches our kit to the dollar)</td></tr>
<tr><td>Cost on 1 Jan 2027 at today's yields</td><td class="n">about $292,000, leaving about $8,000 spare</td></tr>
<tr><td>Chance yields fall enough by January that the 2028 deposit must help</td><td class="n">about 1 in 3</td></tr>
<tr><td>The same ladder priced at 2020 yields</td><td class="n">about $460,000</td></tr>
<tr><td>Typical top of the 2031 range</td><td class="n">about $175,000</td></tr>
<tr><td>Moving $25,000 of the floor into stocks</td><td class="n">+$2,400 typically; &minus;$9,500 in a 1-in-20 bad market</td></tr>
</table>

<div class="chartbox">
<p class="chartcap"><b>Why January yields matter.</b> What the ten payments would cost on 1 Jan 2027, priced on each day's
official Treasury curve. Above the line, $300,000 is not enough and the 2028 deposit has to help. They have fitted only since
mid-September.</p>
{chart()}
<p class="small" style="margin:2pt 0 0">Source: home.treasury.gov daily par yield curves (fetched 30 Sep 2026), independent pricer.</p>
</div>

<h2 class="pb" style="margin-top:0">This week</h2>
<h3>Before Thursday's meeting: one person, read-only login, place nothing</h3>
<ul class="tick">
<li>Read the Week-One email and the logged-in Trading Details page: any minimum trading-activity rule or first-trade deadline?
(The official FAQ says a rule exists but does not define it.)</li>
<li>Open an order screen without submitting: which order types exist (limit? day orders?), and how is bond quantity entered?</li>
<li>Copy the full bond drop-down (43 Treasuries, with coupon and maturity).</li>
</ul>
<h3>Thursday meeting: decide, and write it down</h3>
<ol>
<li>We adopt Root-and-Branch <b>as a team</b>. Record who agreed and why, in our own words. It is our decision, not the AI's.</li>
<li><b>Book:</b> the Portfolio tab (recommended, because it shows all three parts of the plan) or Book L (ladder only).</li>
<li><b>Swap rule:</b> buy a listed low-coupon alternate only if it passes its price check on Friday; otherwise buy the planned bond.</li>
<li><b>Note writers:</b> who writes each WInS note (our own words, 300 characters at most, cannot be edited later).</li>
<li><b>Friday roles, each with a backup:</b> trader, checker, note keeper, recorder, timekeeper. If the refresh script cannot
run, trade from <code>archive/rab/trades/tickets.md</code> using its stop rules.</li>
<li><b>Timing:</b> limit orders placed before bed (if WInS allows them) or trading from 12:30 to 1:30 am; VT on Friday or on
Tue 6 Oct at 1:30 am.</li>
</ol>
<h3>Friday-night rules</h3>
<ul>
<li>Read the name WInS shows before every order. <b>IBTN is INSCORP Inc, not an iBond.</b></li>
<li>Never pay above the ticket's max price. Stop if the Preview total is outside the ticket's band (a 10x gap means the
bond unit is wrong).</li>
<li>Never re-enter a pending order. Never sell anything on the day it was bought.</li>
<li>After each order, copy the saved note back from Order History and check that nothing was cut off.</li>
</ul>
<h3>Admin</h3>
<ul>
<li><b>Roster by Fri 9 Oct (Sat 10 Oct, 8 am Sydney):</b> full names, emails, birthdays, graduation years, team name and school
details. Members are locked once it is submitted.</li>
<li><b>School documentation:</b> ask the school for its letter now. It is due with the Final Report.</li>
</ul>

<h2>Four risks, and what we do about each</h2>
<div class="risk"><b class="t">1. Authorship: this one could get us dismissed.</b>
The IPS draft in our Google Doc is an AI-written exemplar. Wharton's rules say AI-generated work may not be submitted as your
own, and plagiarism is grounds for dismissal.
<div class="fix">We write the IPS ourselves, from a blank page, using the list of what it must cover rather than the
exemplar's sentences. The same goes for WInS notes and reflections. We don't use the ready-made AI disclosure in
<code>caplet/docs/AI_USE.md</code> (it is inaccurate), and our Final Report says plainly how we used AI.</div></div>
<div class="risk"><b class="t">2. Our repo is public.</b>
Anyone can read our full plan and the example notes. One file contains a teammate's school email, and the repo's history
still holds our WInS username. Another team could copy us, and lookalike submissions hurt both teams.
<div class="fix">Ray makes the repo private (Settings, General, Change visibility). A strong WInS password that is never
sent by message. The IPS Doc and the team Sheet set to Restricted sharing.</div></div>
<div class="risk m"><b class="t">3. Complexity.</b>
About 45,000 lines of code and 700,000 words of research sit behind roughly 1,000 words of submissions. Last year's lesson was
that our packaging was too complex for the idea.
<div class="fix">No new research unless a decision needs it. Each of us owns one part of the plan and can explain it in three
sentences.</div></div>
<div class="risk m"><b class="t">4. Friday logistics.</b>
Unread Week-One email, unseen order screen, a refresh script that runs on one laptop, and trading at 12:30 am.
<div class="fix">The Thursday read-only login, a backup for every role, and limit orders if WInS offers them.</div></div>

<h2 class="pb" style="margin-top:0">Questions a judge will ask, and our answers</h2>
<table class="q">
<tr><th>Question</th><th>Our answer</th></tr>
<tr><td>&ldquo;91% Treasuries? Laura says she takes thoughtful risks.&rdquo;</td><td>Her payments are fixed dollar amounts, so
dollar bonds match them, and they use about $290,000 of her first $300,000. Only the 2028 money is free. Moving $25,000 of the
floor into stocks adds about $2,400 typically and loses about $9,500 in a bad market.</td></tr>
<tr><td>&ldquo;Your own model says all-Treasuries gives the facility more. Why hold stocks?&rdquo;</td><td>That comparison
gives the whole pot to the facility, while we keep half the fund for Laura. The fund is her flexibility money: it has the
longest horizon, it is the only part that can keep up with rising costs, and it is the balance she asked for.</td></tr>
<tr><td>&ldquo;Do the payments really depend only on the U.S. government?&rdquo;</td><td>Mostly. About 85% of each payment is
owed outright by the government; the rest depends on reinvesting interest. If rates sat at 2% for years, the ten would
deliver about $466,000 of $500,000, so we name who covers a shortfall (our decision by 26 Oct).</td></tr>
<tr><td>&ldquo;100% confidence in the range sounds like a trick.&rdquo;</td><td>It is by design: the bottom is bonds she
already owns, and the top is a cap she sets. The gift lands at or near the top about 3 times in 4.</td></tr>
<tr><td>&ldquo;What if her 2028 deposit never arrives?&rdquo;</td><td>The payments still happen: at today's yields the 2027
deposit covers all ten. A stock-heavy plan missed payments in about 4 cases in 10 without it.</td></tr>
<tr><td>&ldquo;The residency is in Taiwan.&rdquo;</td><td>The gift is in U.S. dollars and the costs are in Taiwan dollars.
We say so, and we name who carries that risk.</td></tr>
</table>

<h2>The three deliverables</h2>
<p><b>Trading Notes Analysis</b> (due Fri 23 Oct; aim for Thu 22). Three notes copied exactly from WInS, each with a reflection
of 100 words or fewer. Candidates: <i>tested</i> (the ladder against $300,000: it did not fit on 22 Sep, and did a week later),
<i>refined</i> (we switched from bond ETFs to one dated holding per payment, because most of TLH's bonds mature after Laura's
last payment in 2042), and <i>supported</i> (VT, the growth part).</p>
<p><b>IPS</b> (due Fri 6 Nov, which is Sat 7 Nov 9 am Sydney; trading freezes an hour earlier). A 50-word pitch and 500 words,
Times New Roman 12, double-spaced, no charts or citations. Settle first: our definition of &ldquo;high certainty&rdquo;, who
covers a shortfall, how the floor is defined, and who pays costs.</p>
<p><b>Final Report</b> (instructions 9 Nov; due 4 Dec). Also needs: our co-sponsor text (we write it), why a credible lead gift
matters (seed-money research such as List &amp; Lucking-Reiley, 2002), currency, inflation, our team story (start a short
journal now) and an honest AI disclosure.</p>

<div class="two">
<div>
<h2>Own the numbers</h2>
<p>Rebuild these five in our own Sheet, so the numbers in the Final Report are ours:</p>
<ol>
<li>the ladder cost from treasury.gov yields</li>
<li>the floor's cost in January 2028</li>
<li>the top of the 2031 range</li>
<li>a bad-case gift (the fund falls 40%)</li>
<li>the floor trade-off ($25,000 of floor into stocks)</li>
</ol>
<h2>Read next</h2>
<p class="small"><code>archive/rab/trades/friday_checklist.md</code>, <code>archive/rab/trades/tickets.md</code>,
<code>archive/rab/decisions/D7_wins_book.md</code>, <code>archive/rab/trades/notes.md</code> (the briefs, not the example wording),
<code>archive/rab/decisions/D_certainty_definition.md</code>. Ignore <code>caplet/decisions/</code>, <code>caplet/deliverables/</code>,
<code>MISSION.md</code> and the old Strategy Brief PDFs: they describe earlier plans.</p>
</div>
<div>
<h2>Key dates (Sydney time)</h2>
<table class="dates">
<tr><td>Fri 2 Oct, 9 pm</td><td>Refresh the tickets from live prices</td></tr>
<tr><td>Fri 2 Oct, 10:30 pm</td><td>U.S. jobs report: prices can jump</td></tr>
<tr><td>Sat 3 Oct, 12:30 am</td><td>Trades (or limit orders placed earlier)</td></tr>
<tr><td>Tue 6 Oct, 1:30 am</td><td>VT, unless it went in on Friday</td></tr>
<tr><td>Sat 10 Oct, 8 am</td><td><b>Roster due</b></td></tr>
<tr><td>Thu 15 Oct, 7 am</td><td>October check (no trade is a valid result)</td></tr>
<tr><td>Sat 24 Oct, 8 am</td><td><b>Trading Notes Analysis due</b></td></tr>
<tr><td>Sat 7 Nov, 8 am</td><td>Trading ends; portfolio frozen</td></tr>
<tr><td>Sat 7 Nov, 9 am</td><td><b>IPS due</b></td></tr>
<tr><td>Sat 5 Dec, 9 am</td><td><b>Final Report and school letter due</b></td></tr>
</table>
<p class="small">Sydney moves to daylight time on Sun 4 Oct, and the U.S. on Sun 1 Nov.</p>
</div>
</div>

</body></html>'''

open(f'{SP}/brief.html', 'w').write(HTML)

FOOT = ('<div style="width:100%;font-family:Arial,sans-serif;font-size:7.5px;color:#66726b;padding:0 15mm;display:flex;'
        'justify-content:space-between"><span>Team Caplet brief, 1 Oct 2026. Prepared with Claude Code (AI); planning only, '
        'not for submission.</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>')


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = await b.new_page()
        await pg.goto(f'file://{SP}/brief.html', wait_until='load')
        await pg.evaluate('document.fonts.ready')
        fams = await pg.evaluate('[...document.fonts].filter(f => f.status === "loaded").map(f => f.family + " " + f.style)')
        print('fonts loaded:', sorted(set(fams)))
        await pg.pdf(path=f'{SP}/Caplet_Team_Brief_1Oct2026.pdf', format='A4', print_background=True,
                     display_header_footer=True, header_template='<div></div>', footer_template=FOOT,
                     margin={'top': '12mm', 'bottom': '14mm', 'left': '15mm', 'right': '15mm'})
        await b.close()

asyncio.run(main())
print('pdf written')
