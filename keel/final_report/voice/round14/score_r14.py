"""Voice round 14: build the blind scorer packs (mode 'packs') and score the round (mode 'score').

python3 -I score_r14.py packs   -> scorer/pack_scorer_A.md (readers 1-2), pack_scorer_B.md (readers 3-4)
python3 -I score_r14.py score   -> SCORES_R14.md and per_sentence_r14.json, from readings/R1-R4.md and scorer/MARKS_*.md
A retold reason is marked E (explains: more than the step said again, and a sceptic would accept it produces the
step), R (restates the step, circular or empty), M (missing: no reason recalled), W (wrong: not what the text said).
A sentence counts as caught for a reader when no retelling line maps to it, or every line that maps to it is R, M or W.
"""
import re, json, sys, pathlib, collections
d = pathlib.Path(__file__).resolve().parent
S = json.load(open(d / 'sentences.json')); K = json.load(open(d / 'key.json'))

def parse(r):
    t = (d / 'readings' / ('R%d.md' % r)).read_text()
    secs = re.split(r'^## ', t, flags=re.M)
    out = {}
    for s in secs[1:]:
        head = s.split('\n', 1)[0].strip()
        if head.startswith('Letter'):
            text = 'LETTER'
        else:
            m = re.match(r'Passage (\d+)', head)
            if not m:
                continue
            text = 'P%d%02d' % (r, int(m.group(1)))
        ret = {}
        for m in re.finditer(r'^\s*[-*]?\s*\**(R\d+)\.?\**\s*(.*)$', s, re.M):
            if '|' in m.group(2) or 'Because' in m.group(2):
                ret[m.group(1)] = m.group(2).strip()
        rows = {}
        for m in re.finditer(r'^\|\s*\**((?:L\d{2})|(?:P\d{3}\.\d+))\**\s*\|\s*([123])[^|]*\|\s*([YN?])[^|]*\|\s*([^|]*)\|\s*(.*?)\|?\s*$', s, re.M):
            sid, fol, sen, frm, note = m.groups()
            rows[sid] = {'follow': int(fol), 'sense': sen, 'from': re.findall(r'R\d+', frm), 'note': note.strip()}
        out[text] = {'ret': ret, 'rows': rows}
    return out

if sys.argv[1] == 'packs':
    (d / 'scorer').mkdir(exist_ok=True)
    for tag, readers in (('A', (1, 2)), ('B', (3, 4))):
        L = ['# Scorer pack %s (voice round 14, Sun 22 Nov 2026)\n' % tag,
             'Readers read short texts about one client (Laura Gao, planning an artists\' residency in Taiwan, with $300,000 in 2027 and $150,000 in 2028, ten $50,000 payments 2033-2042 that must be met with a high degree of certainty, and a contribution to the building that she states to co-sponsors as a range in 2031). After reading each text once, each reader retold from memory every step the text takes and the reason it gave, for a friend who keeps asking "but why?".\n',
             'Your job: mark every retelling line with one letter, judging the **reason** ("Because") against the **step**, with the text beside you:',
             '- **E**, explains: the reason does more than say the step again, it is what the text gave (or a fair reading of it), and a sceptical friend would accept that it produces the step.',
             '- **R**, restates: the reason is the step in other words, circular, empty, or a name or label offered as a reason ("because that is the rule", "to set the bottom" for buying what sets the bottom).',
             '- **M**, missing: the reader recalled no reason ("none that I recall"), or only a guess the reader marks as their own.',
             '- **W**, wrong: the reason is not what the text said, or contradicts it.',
             'Judge each line on its own; you are not told who wrote the texts, and it does not matter. Do not be charitable to a reason the reader supplied from outside the text: mark it M (if the reader says it is a guess) or W.\n',
             'Write a Markdown file named in your instructions with one table per reader and text: columns `reader | text | line | mark | why (a few words)`, one row per retelling line, every line marked. Nothing else is needed.\n']
        for r in readers:
            P = parse(r)
            for text, v in P.items():
                L.append('## Reader %d, %s\n' % (r, 'the letter' if text == 'LETTER' else 'passage ' + text))
                L.append('**The text, sentence by sentence:**\n')
                pref = 'L' if text == 'LETTER' else text + '.'
                for sid in sorted([k for k in S if (k.startswith('L') and text == 'LETTER') or k.startswith(text + '.')], key=lambda k: (len(k), k)):
                    L.append('- %s %s' % (sid, S[sid]['text']))
                L.append('\n**The reader\'s retelling:**\n')
                for k, line in sorted(v['ret'].items(), key=lambda kv: int(kv[0][1:])):
                    L.append('- %s. %s' % (k, line))
                L.append('')
        (d / 'scorer' / ('pack_scorer_%s.md' % tag)).write_text('\n'.join(L))
    print('packs built')
    sys.exit()

# score
marks = {}
for f in sorted((d / 'scorer').glob('MARKS_*.md')):
    for m in re.finditer(r'^\|\s*(\d)\s*\|\s*([^|]+?)\s*\|\s*\**(R\d+)\**\s*\|\s*\**([ERMW])\**\s*\|', f.read_text(), re.M):
        r, text, line, mk = m.groups()
        text = 'LETTER' if 'letter' in text.lower() else re.search(r'P\d{3}', text).group(0)
        marks[(int(r), text, line)] = mk
res = collections.defaultdict(lambda: collections.defaultdict(list))
per = {}
for r in range(1, 5):
    P = parse(r)
    labels = K['readers'][str(r)]['labels']
    for text, v in P.items():
        src = 'V61' if text == 'LETTER' else labels[text]
        for sid, row in v['rows'].items():
            ms = [marks.get((r, text, x), '?') for x in row['from']]
            caught = (not ms) or all(m in 'RMW' for m in ms)
            key = sid if text == 'LETTER' else '%s.%s' % (src, sid.split('.')[1])
            per.setdefault(key, []).append({'reader': r, 'follow': row['follow'], 'sense': row['sense'], 'marks': ms, 'caught': caught})
        for k, mk in ((k, marks.get((r, text, k), '?')) for k in v['ret']):
            res[src]['marks'].append(mk)
json.dump(per, open(d / 'per_sentence_r14.json', 'w'), indent=1)
out = ['# Voice round 14 scores (built by score_r14.py)\n']
out.append('## Version 61 calibration (caught = for at least half the readers, no retold reason maps to the sentence or all are R/M/W)\n')
out.append('| Sentence | Caplet followed | Caught by (readers of 4) | Caught | Marks | Rereads |')
out.append('|---|---|---|---|---|---|')
caught_unflag = 0; caught_failed = 0; false_al = 0
for i in range(1, 22):
    sid = 'L%02d' % i; rows = per.get(sid, [])
    n = sum(x['caught'] for x in rows); c = n * 2 >= len(rows) and len(rows) > 0
    fol = i in K['v61_followed_by_caplet']
    if c and i in K['v61_unflagged']: caught_unflag += 1
    if c and not fol: caught_failed += 1
    if c and fol: false_al += 1
    out.append('| V%02d%s | %s | %d of %d | %s | %s | %d |' % (i, ' *' if i in K['v61_unflagged'] else '', 'yes' if fol else 'no', n, len(rows), 'yes' if c else 'no', ' '.join(''.join(x['marks']) or '-' for x in rows), sum(x['follow'] > 1 for x in rows)))
out.append('\n* = one of the five every earlier reader passed. Caught among those five: **%d of 5**; among the seventeen Caplet failed: **%d of 17**; false alarms among the four Caplet followed: **%d of 4**.\n' % (caught_unflag, caught_failed, false_al))
out.append('## By text\n')
out.append('| Text | Sentences read | Reread | No sense | Caught (no reason retold that explains) | Retold reasons E / R / M / W |')
out.append('|---|---|---|---|---|---|')
for src in ['V61', 'Y3', 'Y5', 'Z3', 'Z5', 'X3', 'C3', 'C4']:
    rows = [x for k, v in per.items() for x in v if (src == 'V61' and k.startswith('L')) or k.startswith(src + '.')]
    if not rows: continue
    mk = collections.Counter(res[src]['marks'])
    tot = sum(mk.values()) or 1
    out.append('| %s | %d | %d%% | %d%% | %d%% | %d%% / %d%% / %d%% / %d%% |' % (src, len(rows), round(100 * sum(x['follow'] > 1 for x in rows) / len(rows)), round(100 * sum(x['sense'] == 'N' for x in rows) / len(rows)), round(100 * sum(x['caught'] for x in rows) / len(rows)), round(100 * mk['E'] / tot), round(100 * mk['R'] / tot), round(100 * mk['M'] / tot), round(100 * mk['W'] / tot)))
out.append('\n"We" per 100 words: ' + ', '.join('%s %.2f' % (k, v[0]) for k, v in K['we_per_100_words'].items()))
(d / 'SCORES_R14.md').write_text('\n'.join(out) + '\n')
print('\n'.join(out))
