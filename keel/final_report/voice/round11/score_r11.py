#!/usr/bin/env python3
"""Score voice round 11 (Fri 20 Nov 2026): six blind readers, version 61 calibration plus fourteen passages.

Reads readings/R1.md-R6.md (one table row per labelled sentence: | label | Follow | Sense | Fault | Paraphrase | Why |),
key.json (each reader's pack labels -> passage keys) and sentences.json, and writes SCORES_R11.md and
per_sentence_r11.json. Labels: L01-L21 are version 61's sentences (V01-V21); P<reader><nn>.<j> is sentence j of the
nn-th passage in that reader's pack. A reread (Follow 2 or 3) counts as a failure (Book 21). Run: python3 score_r11.py
"""
import json, re, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = json.load(open(os.path.join(HERE, 'key.json'), encoding='utf-8'))
S = json.load(open(os.path.join(HERE, 'sentences.json'), encoding='utf-8'))
FOLLOWED = set(KEY['v61_followed_by_caplet'])
ROW = re.compile(r'^\|\s*\**(L\d{2}|P\d{3}\.\d+)\**\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|?\s*(.*)$')
WRITER = {'U': 'Fresh writer U', 'V': 'Fresh writer V', 'K': "Keel's main session (K)", 'C': "Caplet's IPS (control)"}
TOPIC = {'1': 'P1 the ten payments', '2': 'P2 the 2028 deposit', '3': 'P3 the 2031 range', '4': 'P4 her flexibility'}


def follow(x):
    m = re.search(r'[123]', x)
    return int(m.group()) if m else None


def sense(x):
    x = x.strip().upper()
    return 'Y' if x.startswith('Y') else 'N' if x.startswith('N') else '?' if '?' in x else None


per = collections.defaultdict(lambda: {'readers': 0, 'reread': 0, 'nonsense': 0, 'unsure': 0, 'faults': [], 'text': '', 'src': ''})
calib = {}
parsed = {}
for r in sorted(KEY['readers']):
    labels = KEY['readers'][r]['labels']
    path = os.path.join(HERE, 'readings', f'R{r}.md')
    n = 0
    c = {'hit17': 0, 'hit4': 0, 'nonsense17': 0}
    for line in open(path, encoding='utf-8'):
        m = ROW.match(line.strip())
        if not m:
            continue
        lab = m.group(1)
        f, s = follow(m.group(2)), sense(m.group(3))
        if lab.startswith('L'):
            i = int(lab[1:])
            sid = f'V{i:02d}'
            src = 'V61'
            flagged = (f or 1) >= 2 or s in ('N', '?')
            if i in FOLLOWED:
                c['hit4'] += flagged
            else:
                c['hit17'] += flagged
                c['nonsense17'] += s == 'N'
        else:
            pk, j = lab.split('.')
            src = labels[pk]
            sid = f'{src}.{j}'
        n += 1
        p = per[sid]
        p['src'] = src
        p['text'] = S.get(lab, S.get(sid, {})).get('text', '') if lab.startswith('P') else S[f'V{int(lab[1:]):02d}']['text']
        p['readers'] += 1
        p['reread'] += (f or 1) >= 2
        p['nonsense'] += s == 'N'
        p['unsure'] += s == '?'
        if s in ('N', '?'):
            p['faults'].append(f'R{r}: {m.group(4).strip()}')
    calib[r] = c
    parsed[r] = n


def group(src):
    return 'V61' if src == 'V61' else src[0]


agg = collections.defaultdict(lambda: collections.Counter())
for sid, p in per.items():
    keys = [group(p['src'])]
    if p['src'] != 'V61' and p['src'][0] != 'C':
        keys.append(p['src'][0] + p['src'][1])
        keys.append('topic' + p['src'][1])
    elif p['src'][0] == 'C':
        keys.append(p['src'])
    for k in keys:
        a = agg[k]
        a['sent'] += 1
        a['j'] += p['readers']
        a['reread'] += p['reread']
        a['nonsense'] += p['nonsense']
        a['fail'] += 0
        a['half'] += p['readers'] > 0 and (p['reread'] + 0) * 2 > p['readers'] or p['nonsense'] * 2 >= p['readers']
        a['clean'] += p['reread'] == 0 and p['nonsense'] == 0 and p['unsure'] == 0


def row(label, a):
    j = max(1, a['j'])
    return (f"| {label} | {a['sent']} | {a['j']} | {a['reread']} ({100 * a['reread'] / j:.0f}%) | "
            f"{a['nonsense']} ({100 * a['nonsense'] / j:.0f}%) | {a['clean']} ({100 * a['clean'] / max(1, a['sent']):.0f}%) | {a['half']} |")


H = '| Text | Sentences | Judgements | Reread | No sense | Clean for every reader | Half or more failed it |\n|---|---|---|---|---|---|---|'
out = ['# Voice round 11: scores (Fri 20 Nov 2026)', '',
       'Built by `score_r11.py` from `readings/`. A judgement is one reader on one sentence. "Reread" = Follow 2 or 3, '
       'which counts as a failure (Book 21); "no sense" = Sense N. "Clean" = no reader reread it or doubted its sense. '
       '"Half or more failed it" = more than half its readers reread it, or half or more said no sense. Readers are '
       'simulated (never people).', '',
       'Judgements parsed: ' + ', '.join(f'R{r} {n}' for r, n in parsed.items()), '',
       '## Calibration on version 61 (Caplet followed sentences 1, 5, 6 and 8 only)', '',
       '| Reader | Flagged of the 17 Caplet could not follow | Of those, no sense | Flagged of the 4 it followed |',
       '|---|---|---|---|']
for r, c in calib.items():
    out.append(f"| R{r} ({KEY['readers'][r]['role'][9:60].strip()}...) | {c['hit17']} | {c['nonsense17']} | {c['hit4']} |")
t17 = sum(c['hit17'] for c in calib.values())
t4 = sum(c['hit4'] for c in calib.values())
out += [f'| All six | {t17} of 102 ({100 * t17 / 102:.0f}%) | {sum(c["nonsense17"] for c in calib.values())} | {t4} of 24 ({100 * t4 / 24:.0f}%) |', '',
        '## By writer', '', H]
for k in ['V61', 'C', 'U', 'V', 'K']:
    out.append(row('Version 61 (calibration)' if k == 'V61' else WRITER[k], agg[k]))
out += ['', '## By topic (writers U, V and K together)', '', H]
for t in '1234':
    out.append(row(TOPIC[t], agg['topic' + t]))
out += ['', '## Every passage', '', H]
for k in ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'K1', 'K2', 'K3', 'K4', 'C3', 'C4']:
    out.append(row(f"{WRITER[k[0]].split(' (')[0]}, {TOPIC[k[1]] if k[0] != 'C' else ('IPS paragraph ' + k[1])}", agg[k]))
out += ['', '## Sentences more than half their readers reread, or half or more found made no sense', '',
        '| Sentence | Readers | Reread | No sense | Text | Faults named |', '|---|---|---|---|---|---|']
for sid in sorted(per, key=lambda s: (-(per[s]['nonsense'] * 2 + per[s]['reread']) / max(1, per[s]['readers']), s)):
    p = per[sid]
    if p['reread'] * 2 > p['readers'] or p['nonsense'] * 2 >= p['readers']:
        out.append(f"| {sid} | {p['readers']} | {p['reread']} | {p['nonsense']} | {p['text'].replace('|', '/')} | "
                   f"{'; '.join(p['faults']).replace('|', '/')} |")
open(os.path.join(HERE, 'SCORES_R11.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
json.dump({k: dict(v) for k, v in per.items()}, open(os.path.join(HERE, 'per_sentence_r11.json'), 'w'), indent=1)
print('\n'.join(out[:60]))
