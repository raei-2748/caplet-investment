#!/usr/bin/env python3
"""Score voice round 12 (Sun 22 Nov 2026): four blind readers, version 61 calibration plus ten passages, with Why.

Reads readings/R1.md-R4.md (rows | label | Follow | Sense | Why | Fault | Paraphrase | Note |), key.json and
sentences.json; writes SCORES_R12.md and per_sentence_r12.json. A reread (Follow 2-3), Sense N, or Why N each count as a
failure (Books 21 and 22). Readers are simulated (never people). Run: python3 score_r12.py
"""
import json, re, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = json.load(open(os.path.join(HERE, 'key.json')))
S = json.load(open(os.path.join(HERE, 'sentences.json')))
FOLLOWED = set(KEY['v61_followed_by_caplet']); UNFL = set(KEY['v61_unflagged_r11'])
ROW = re.compile(r'^\|\s*\**(L\d{2}|P\d{3}\.\d+)\**\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|?\s*(.*)$')
WRITER = {'W': 'Fresh writer W (round 12)', 'X': 'Fresh writer X (round 12)', 'K': "Round 11's K, P2 (kept)", 'V': "Round 11's V, P4 (kept)", 'C': "Caplet's IPS paragraphs 3-4 (control)"}

def fol(x):
    m = re.search(r'[123]', x); return int(m.group()) if m else None
def yn(x):
    x = x.strip().upper().lstrip('*')
    return 'Y' if x.startswith('Y') else 'N' if x.startswith('N') else '?' if '?' in x else '-'

per = collections.defaultdict(lambda: collections.Counter())
txt, src_of, notes = {}, {}, collections.defaultdict(list)
calib = {}
for r in sorted(KEY['readers']):
    labels = KEY['readers'][r]['labels']
    c = collections.Counter()
    for line in open(os.path.join(HERE, 'readings', f'R{r}.md')):
        m = ROW.match(line.strip())
        if not m: continue
        lab = m.group(1); f, s, w = fol(m.group(2)), yn(m.group(3)), yn(m.group(4))
        if lab.startswith('L'):
            i = int(lab[1:]); sid = f'V{i:02d}'; src = 'V61'
            flag_old = (f or 1) >= 2 or s in ('N', '?')
            flag_new = flag_old or w == 'N'
            grp = 'f4' if i in FOLLOWED else 'm17'
            c[grp + '_old'] += flag_old; c[grp + '_new'] += flag_new
            if i in UNFL: c['unfl_whyN'] += w == 'N'; c['unfl_new'] += flag_new
        else:
            pk, j = lab.split('.'); src = labels[pk]; sid = f'{src}.{j}'
        p = per[sid]; src_of[sid] = src
        txt[sid] = S[sid]['text'] if sid in S else S.get(lab, {}).get('text', '')
        p['n'] += 1; p['reread'] += (f or 1) >= 2; p['nonsense'] += s == 'N'; p['unsure'] += s == '?'
        p['step'] += w in ('Y', 'N'); p['whyN'] += w == 'N'
        p['fail'] += ((f or 1) >= 2) or s == 'N' or w == 'N'
        if (f or 1) >= 2 or s in ('N', '?') or w == 'N':
            notes[sid].append(f'R{r}: ' + (m.group(5).strip() + ' ' + m.group(6).split('|')[-2].strip() if '|' in m.group(6) else m.group(5).strip()))
    calib[r] = c

def grp(src): return 'V61' if src == 'V61' else src[0]
agg = collections.defaultdict(collections.Counter)
for sid, p in per.items():
    s = src_of[sid]; keys = [grp(s)]
    if s[0] in 'WX': keys += [s, 'topic' + s[1]]
    for k in keys:
        a = agg[k]; a['sent'] += 1
        for f in ('n', 'reread', 'nonsense', 'step', 'whyN', 'fail'): a[f] += p[f]
        a['clean'] += p['fail'] == 0 and p['unsure'] == 0
def row(label, a):
    n = max(1, a['n']); st = max(1, a['step'])
    return (f"| {label} | {a['sent']} | {a['reread']} ({100*a['reread']/n:.0f}%) | {a['nonsense']} ({100*a['nonsense']/n:.0f}%) | "
            f"{a['whyN']} of {a['step']} ({100*a['whyN']/st:.0f}%) | {100*a['fail']/n:.0f}% | {a['clean']} ({100*a['clean']/max(1,a['sent']):.0f}%) |")
H = '| Text | Sentences | Reread | No sense | Why N (of judgements on steps or claims) | Any failure | Clean for every reader |\n|---|---|---|---|---|---|---|'
out = ['# Voice round 12: scores (Sun 22 Nov 2026)', '', 'Built by `score_r12.py` from `readings/`. A judgement is one reader on one sentence. A reread (Follow 2-3), Sense N or Why N is a failure. Readers are simulated (never people).', '',
       '## Calibration on version 61: does the Why column catch what Caplet failed?', '',
       '| Reader | Of the 17 Caplet failed: flagged by Follow/Sense | ... adding Why | Of round 11\'s 5 unflagged: Why N | Of the 4 Caplet followed: flagged (with Why) |', '|---|---|---|---|---|']
for r, c in calib.items():
    out.append(f"| R{r} ({KEY['readers'][r]['role'][9:55].strip()}...) | {c['m17_old']} | {c['m17_new']} | {c['unfl_whyN']} | {c['f4_new']} |")
T = collections.Counter()
for c in calib.values(): T.update(c)
nr = len(calib)
out.append(f"| All {nr} | {T['m17_old']} of {17*nr} | {T['m17_new']} of {17*nr} | {T['unfl_whyN']} of {5*nr} | {T['f4_new']} of {4*nr} |")
caught = [f'V{i:02d}' for i in sorted(UNFL) if per[f'V{i:02d}']['whyN'] * 2 >= per[f'V{i:02d}']['n']]
out += ['', f"Round 11's five unflagged sentences given Why N by at least half the readers: {len(caught)} ({', '.join(caught) or 'none'}).", '', '## By writer', '', H]
for k in ['V61', 'C', 'W', 'X', 'K', 'V']:
    if agg[k]['sent']: out.append(row('Version 61 (calibration)' if k == 'V61' else WRITER[k], agg[k]))
out += ['', '## By passage (this round\'s writers)', '', H]
for k in ['W1', 'W3', 'W4', 'X1', 'X3', 'X4']:
    out.append(row(k, agg[k]))
out += ['', '## By topic (W and X together)', '', H]
for t, nm in (('1', 'P1 the ten payments'), ('3', 'P3 the 2031 range'), ('4', 'P4 her flexibility')):
    out.append(row(nm, agg['topic' + t]))
out += ['', '## Sentences that half or more of their readers failed (any failure)', '']
for sid in sorted(per, key=lambda s: (src_of[s], s)):
    p = per[sid]
    if src_of[sid] != 'V61' and p['fail'] * 2 >= p['n'] and p['n']:
        out.append(f"- **{sid}** ({p['fail']}/{p['n']}; reread {p['reread']}, no sense {p['nonsense']}, why N {p['whyN']}): {txt[sid]}")
        for nt in notes[sid][:4]: out.append(f'  - {nt[:220]}')
open(os.path.join(HERE, 'SCORES_R12.md'), 'w').write('\n'.join(out) + '\n')
json.dump({sid: dict(per[sid], src=src_of[sid], text=txt[sid]) for sid in per}, open(os.path.join(HERE, 'per_sentence_r12.json'), 'w'), indent=1)
print('\n'.join(out[:40]))
