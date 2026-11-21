#!/usr/bin/env python3
"""Score voice round 13 (Sun 22 Nov 2026): six blind readers, one long piece each (L studied long-form; M did not).
Reads readings/R*.md paragraph tables (| para | Mark | Follow | Why | Note |) and key.json; writes SCORES_R13.md.
Readers are simulated (never people). Run: python3 score_r13.py"""
import json, re, os, collections
H = os.path.dirname(os.path.abspath(__file__))
K = json.load(open(os.path.join(H, 'key.json')))
ROW = re.compile(r'^\|\s*¶?(\d+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*(.*?)\|?\s*$')
agg = {w: collections.Counter() for w in 'LM'}
perpara = {w: collections.defaultdict(list) for w in 'LM'}
readers = {}
for r, w in sorted(K['assign'].items()):
    p = os.path.join(H, 'readings', f'R{r}.md')
    if not os.path.exists(p): continue
    t = open(p).read(); tab = t.split('## Paragraph', 1)[1].split('## Last', 1)[0] if '## Paragraph' in t else ''
    c = collections.Counter()
    for line in tab.splitlines():
        m = ROW.match(line.strip())
        if not m: continue
        mark = m.group(2).strip().lower(); f = re.search(r'[123]', m.group(3)); wy = m.group(4).strip().upper()[:1]
        c['paras'] += 1; c['lost'] += 'lost' in mark; c['drift'] += 'drift' in mark
        c['reread'] += bool(f and int(f.group()) >= 2); c['whyN'] += wy == 'N'
        if 'lost' in mark or 'drift' in mark or (f and int(f.group()) >= 2) or wy == 'N':
            perpara[w][int(m.group(1))].append(f'R{r}: {mark}, F{f.group() if f else "?"}, Why {wy}: {m.group(5).strip()[:160]}')
    readers[r] = (w, c); agg[w].update(c); agg[w]['readers'] += 1
out = ['# Voice round 13: scores (Sun 22 Nov 2026)', '', 'Built by `score_r13.py` from `readings/`. One long piece per reader; L studied long-form explainers before writing, M did not. Readers are simulated (never people).', '',
       '| Reader | Piece | Paragraphs | Lost | Drifting | Reread (Follow 2-3) | Why N |', '|---|---|---|---|---|---|---|']
for r, (w, c) in readers.items():
    out.append(f"| R{r} | {w} | {c['paras']} | {c['lost']} | {c['drift']} | {c['reread']} | {c['whyN']} |")
for w in 'LM':
    a = agg[w]; n = max(1, a['paras'])
    out.append(f"| All ({a['readers']} readers) | {w} | {a['paras']} | {a['lost']} | {a['drift']} ({100*a['drift']/n:.0f}%) | {a['reread']} ({100*a['reread']/n:.0f}%) | {a['whyN']} ({100*a['whyN']/n:.0f}%) |")
for w in 'LM':
    out += ['', f'## Piece {w}: paragraphs any reader flagged', '']
    for k in sorted(perpara[w]):
        out.append(f'- **¶{k}** ({len(perpara[w][k])} of {agg[w]["readers"]})')
        for x in perpara[w][k]: out.append('  - ' + x)
open(os.path.join(H, 'SCORES_R13.md'), 'w').write('\n'.join(out) + '\n')
print('\n'.join(out[:14]))
