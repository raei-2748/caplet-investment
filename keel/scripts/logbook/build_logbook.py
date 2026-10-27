"""FICTION (Team Keel). Builds the Keel Logbook page from episodes/, IDEAS.md and ARCS.md.
Run: python3 keel/scripts/logbook/build_logbook.py keel/scripts/logbook/head.html > /tmp/keel_logbook.html
Then republish it to https://claude.ai/artifact/VNXgEcdGmGEPkwcFVTLP26 (cast and values are hard-coded below)."""
import re, html, glob, sys
import os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')+'/'
esc=html.escape
def md(s):
    s=esc(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*(.+?)\*',r'<em>\1</em>',s)
    return s
# episodes
eps=[]
for f in sorted(glob.glob(R+'episodes/2026-*.md')):
    t=open(f).read()
    title=re.search(r'^# FICTION\. Episode (\d+): (.+)$',t,re.M)
    head=re.search(r'^\*\*(.+?)\*\*\s*$',t,re.M).group(1)
    sm=re.search(r'> \*\*Summary\.\*\*(.+?)\n> \*\*Arcs',t,re.S)
    summ=' '.join(l.lstrip('> ').strip() for l in sm.group(1).split('\n'))
    tags=re.search(r'> \*\*Arcs:\*\*(.+)',t).group(1)
    parts=[p.strip() for p in head.split('·')]
    eps.append(dict(n=int(title.group(1)),title=title.group(2),date=parts[0].replace(', Sydney',''),pov=parts[1].replace('Point of view: ',''),room=parts[2].replace('Long Room: ','') if len(parts)>2 else '',summ=summ,tags=tags.strip()))
eps.sort(key=lambda e:e['n'])
# room column from INDEX
room={}
for line in open(R+'episodes/INDEX.md'):
    m=re.match(r'\| (\d+) \|.*\| ([^|]+) \|\s*$',line)
    if m: room[int(m.group(1))]=m.group(2).strip()
mile={}
for line in open(R+'episodes/INDEX.md'):
    c=[x.strip() for x in line.split('|')]
    if len(c)>8 and c[1].isdigit(): mile[int(c[1])]=c[7]
# ideas
ideas=[]
for line in open(R+'IDEAS.md'):
    c=[x.strip() for x in line.split('|')]
    if len(c)>8 and c[1].startswith('I-'):
        ideas.append(dict(id=c[1],name=c[2],by=c[3],ep=c[4],verdict=c[7],why=c[8]))
def vclass(v):
    v=v.upper()
    for k in ('ADOPTED','ADAPTED','REJECTED','PARKED'):
        if v.startswith(k): return k.lower()
    return 'parked'
# cast
cast=[('Nora Haddad','17','Leader','Turns a 40-minute argument into a two-option vote, then makes the team live with it.','Closes questions before the quiet person has spoken.','Hold a question open on purpose.','"So what?"'),
('Felix Wong','16','Rules and sources','Reads every email twice and never relies on a rule without its line number.','Right, and late: cannot rank his own checks.','Say "this one matters" fast.','"Where does it say that?"'),
('Jun Park','17','Numbers','Turns "a lot" into a dated number, then tells you how it could be wrong.','Works alone in the Long Room after everyone sleeps.','Stop working alone; say what he is afraid of.','"A model is a torch, not a map."'),
('Kai Tran','17','Contrarian, finance reader, the only trader','Finds the weakest point of any plan in five minutes; brings a new idea every week.','Reads "bold" as "more stocks"; hides worry behind jokes.','Learn that the leap is the honesty rule.','"Who says?"'),
('Amara Singh','16','Client lead','Makes a strategy sound like it was written for Laura, not for a textbook.','Lets a good sentence outrun the evidence.','The most persuasive sentence is the exactly true one.','"What does Laura feel in a bad year?"'),
('Tess Bell','16','Editor and team memory','Cuts any draft by a third without losing an idea, and remembers who argued what.','Sits on a problem, especially a friend\'s.','She is a maker, not only a recorder.','"Which job is that sentence doing?"')]
values=[('The promise comes first','Laura\'s ten payments are bought before anything is grown. Deadlines are promises too.','Amara'),
('Where does it say that?','Every rule has a line number, every number a date and a basis.','Felix'),
('Argue hard, decide once','Disagreement is a duty. When the vote is logged, everyone carries it.','Kai and Nora'),
('Say it the day you see it','A problem raised late costs more than one raised clumsily. Added 17 Oct.','Tess'),
('Leave it better, and say what you learned','Every mistake gets a row and a "what we\'d do differently".','Jun')]
arcs=[]
t=open(R+'ARCS.md').read()
for m in re.finditer(r'### \d+\. (.+?)\n(.+?)\n.*?\*\*Where it stands \(23 Oct\):\*\* (.+?)\n',t,re.S):
    arcs.append((m.group(1),m.group(2).strip(),m.group(3).strip()))
def short(d):
    m=re.search(r'(\d{1,2}) ([A-Z][a-z]{2})',d)
    return m.group(1)+' '+m.group(2) if m else d
out=[]
A=out.append
A(open(sys.argv[1]).read())  # head + css
A('<main class="wrap">')
A('''<header class="hero"><p class="eyebrow">Team Keel · fiction · Wharton Global High School Investment Competition 2026-27</p>
<h1>The Keel logbook</h1>
<p class="lede">Six simulated Year 11 students in Sydney, working on the same case as Caplet. In their Long Room, one real minute is about one day of their working time, so they live weeks of argument, research and sleep inside a short session. This page shows what they have done since the night before trading opened.</p>
<dl class="stats">
<div><dt>Episodes</dt><dd>%d</dd></div><div><dt>Days covered</dt><dd>%s to %s</dd></div><div><dt>Ideas debated</dt><dd>%d</dd></div><div><dt>WInS trades</dt><dd>11</dd></div>
</dl>
<p class="mission"><span>Mission</span> Help Laura keep her promise and build what she dreams of, with a plan a stranger could check.</p>
<p class="mission"><span>Vision</span> By December, a judge who reads our three documents can repeat our idea in one sentence, find every number's source, and tell that six people built it together.</p>
</header>'''%(len(eps),short(eps[0]['date']),short(eps[-1]['date']),len(ideas)))
A('<nav class="tabs" aria-label="Sections"><a href="#timeline">Timeline</a><a href="#cast">The six</a><a href="#values">Values</a><a href="#ideas">Ideas ledger</a><a href="#arcs">Arcs</a></nav>')
A('<section id="timeline"><h2>Timeline</h2><p class="note">Room = how far Jun\'s daily price for Laura\'s ten payments sat under $300,000, in basis points (MODEL, Treasury par curve of the previous U.S. close). It fell from 42bp on 6 Oct to 18bp on 16 Oct.</p><ol class="log">')
for e in eps:
    r=room.get(e['n'],'-'); ms=mile.get(e['n'],'-')
    A('<li class="ep"><div class="when"><span class="num">Ep %d</span><span class="date">%s</span></div><div class="body"><h3>%s</h3><p class="meta">%s · Long Room: %s%s</p><p>%s</p><p class="tags">%s</p></div><div class="room"><span class="rv">%s</span><span class="rl">room</span></div></li>'%(e['n'],esc(e['date']),esc(e['title']),esc(e['pov']),esc(e['room'] or 'none'),(' · <strong>'+esc(ms)+'</strong>') if ms not in ('-','') else '',md(e['summ']),md('Arcs: '+e['tags']),esc(r)))
A('</ol></section>')
A('<section id="cast"><h2>The six</h2><div class="cast">')
for n,a,role,s,w,arc,line in cast:
    A('<article class="person"><h3>%s <span>%s</span></h3><p class="role">%s</p><p class="line">%s</p><dl><dt>Strength</dt><dd>%s</dd><dt>Weakness</dt><dd>%s</dd><dt>Arc</dt><dd>%s</dd></dl></article>'%(esc(n),a,esc(role),esc(line),esc(s),esc(w),esc(arc)))
A('</div><p class="note">Full profiles (family, turning points, skills, fears, relationships): <code>keel/members/</code>. One screen: <code>keel/CAST.md</code>.</p></section>')
A('<section id="values"><h2>Values on the Long Room door</h2><ol class="values">')
for i,(v,d,who) in enumerate(values,1):
    A('<li><span class="vn">%d</span><div><h3>%s</h3><p>%s <em>Argued for by %s.</em></p></div></li>'%(i,esc(v),esc(d),esc(who)))
A('</ol></section>')
A('<section id="ideas"><h2>Ideas ledger</h2><p class="note">Every concept someone brought, with the verdict for Laura\'s case. A rejected idea with a reason is still research.</p><div class="tablewrap"><table><thead><tr><th>#</th><th>Concept</th><th>By</th><th>Ep</th><th>Verdict</th><th>Why</th></tr></thead><tbody>')
for i in ideas:
    A('<tr><td class="mono">%s</td><td>%s</td><td>%s</td><td class="mono">%s</td><td><span class="chip %s">%s</span></td><td>%s</td></tr>'%(i['id'],md(i['name']),esc(i['by']),esc(i['ep']),vclass(i['verdict']),esc(i['verdict']),md(i['why'])))
A('</tbody></table></div></section>')
A('<section id="arcs"><h2>Story arcs to December</h2><div class="arcs">')
for n,d,w in arcs:
    A('<article><h3>%s</h3><p>%s</p><p class="stand"><span>Where it stands</span> %s</p></article>'%(esc(n),md(d),md(w)))
A('</div></section>')
A('<footer><p>Fiction, AI-generated (Claude Code) for Team Caplet, 23 Oct 2026. Keel\'s events never go into Caplet\'s deliverables; its research may, once re-checked. Source files: <code>keel/</code> in the team repository.</p></footer></main>')
print('\n'.join(out))
