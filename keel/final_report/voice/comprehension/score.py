#!/usr/bin/env python3
"""Score the comprehension study's readings (Book 21, Thu 19 Nov 2026).

Reads readings/*.md (one table row per numbered sentence), the sentence list sentences.json and KEY.md, and writes
SCORES.md: per text, how many sentences the readers had to reread (Follow 2-3) and how many did not make sense once
understood (Sense N); per sentence, how many readers flagged it. Run: python3 score.py
"""
import json, re, glob, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, 'sentences.json'), encoding='utf-8'))

ROW = re.compile(r'^\|\s*\**([A-Z]\d+|P\d{3}\.\d+|F\d+)\**\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|?\s*(.*)$')

def norm_follow(x):
    m = re.search(r'[123]', x)
    return int(m.group()) if m else None

def norm_sense(x):
    x = x.strip().upper()
    if x.startswith('Y'):
        return 'Y'
    if x.startswith('N'):
        return 'N'
    if '?' in x:
        return '?'
    return None

readings = {}
for f in sorted(glob.glob(os.path.join(HERE, 'readings', '*.md'))):
    r = os.path.basename(f)[:-3]
    rows = {}
    for line in open(f, encoding='utf-8'):
        m = ROW.match(line.strip())
        if not m:
            continue
        sid = m.group(1)
        if sid not in S:
            continue
        rows[sid] = {'follow': norm_follow(m.group(2)), 'sense': norm_sense(m.group(3)),
                     'fault': m.group(4).strip(), 'para': m.group(5).strip(), 'why': m.group(6).strip(' |')}
    readings[r] = rows

def group_of(sid):
    return S[sid]['source'].split(':')[0] if ':' in S[sid]['source'] else S[sid]['source']

per_sentence = collections.defaultdict(lambda: {'readers': 0, 'reread': 0, 'nonsense': 0, 'faults': []})
for r, rows in readings.items():
    for sid, v in rows.items():
        p = per_sentence[sid]
        p['readers'] += 1
        if v['follow'] and v['follow'] >= 2:
            p['reread'] += 1
        if v['sense'] == 'N':
            p['nonsense'] += 1
            p['faults'].append(f"{r}: {v['fault']}")

def source_label(sid):
    src = S[sid]['source']
    if src.startswith('control:'):
        return 'Caplet TNA reflections (control)'
    if src.startswith('round'):
        return 'Fresh writers, voice ' + src.split(':')[0].replace('round', 'round ')
    if src.startswith('aha8'):
        return 'Aha test 8 items (Keel)'
    return {'V63': 'Keel version 63', 'V62': 'Keel version 62', 'V57': 'Keel version 57',
            'CAPLET': "Caplet's IPS (control)", 'FACTS_PLAIN': 'Fact sheet for writers (Keel)'}.get(src, src)

agg = collections.defaultdict(lambda: {'sent': set(), 'judgements': 0, 'reread': 0, 'nonsense': 0, 'flag_any_half': 0})
for sid, p in per_sentence.items():
    lab = source_label(sid)
    a = agg[lab]
    a['sent'].add(sid)
    a['judgements'] += p['readers']
    a['reread'] += p['reread']
    a['nonsense'] += p['nonsense']
    if p['readers'] and p['nonsense'] * 2 >= p['readers']:
        a['flag_any_half'] += 1

out = ['# Comprehension study: scores (Thu 19 Nov 2026)', '',
       'Built by `score.py` from `readings/`. A judgement is one reader on one sentence. "Reread" = Follow 2 or 3; '
       '"no sense" = Sense N. "Half or more say no sense" counts sentences where at least half the readers who saw '
       'them scored N. Readers are simulated (never people); the scores say how the words read to them.', '',
       f"Readings parsed: {', '.join(f'{r} ({len(v)})' for r, v in readings.items())}", '',
       '| Text | Sentences | Judgements | Reread | No sense | Half or more say no sense |', '|---|---|---|---|---|---|']
for lab in sorted(agg, key=lambda l: -agg[l]['nonsense'] / max(1, agg[l]['judgements'])):
    a = agg[lab]
    j = max(1, a['judgements'])
    out.append(f"| {lab} | {len(a['sent'])} | {a['judgements']} | {a['reread']} ({100*a['reread']/j:.0f}%) | "
               f"{a['nonsense']} ({100*a['nonsense']/j:.0f}%) | {a['flag_any_half']} |")
out += ['', '## Every sentence that half or more of its readers found made no sense', '',
        '| # | Text | Readers | No sense | Reread | Sentence | Faults named |', '|---|---|---|---|---|---|---|']
def sort_key(sid):
    p = per_sentence[sid]
    return (-p['nonsense'] / max(1, p['readers']), sid)
for sid in sorted(per_sentence, key=sort_key):
    p = per_sentence[sid]
    if p['readers'] and p['nonsense'] * 2 >= p['readers']:
        txt = S[sid]['text'].replace('|', '/')
        faults = '; '.join(p['faults']).replace('|', '/')
        out.append(f"| {sid} | {source_label(sid)} | {p['readers']} | {p['nonsense']} | {p['reread']} | {txt} | {faults} |")
open(os.path.join(HERE, 'SCORES.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
json.dump({k: dict(v) for k, v in per_sentence.items()}, open(os.path.join(HERE, 'per_sentence.json'), 'w'), indent=1)
print('\n'.join(out[:20]))
