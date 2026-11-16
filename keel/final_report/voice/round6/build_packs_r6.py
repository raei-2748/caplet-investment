"""Build blind reading packs for voice rounds 5 and 6 (Mon 16 Nov 2026, evening; round 6 writers K and L, Tue 17 Nov).

Usage: python3 -I build_packs_r56.py ROUND OUTDIR
ROUND 5 reads round5/writer_H.md and round5/writer_J.md (two fresh writers on different reading diets).
Each pack also holds Caplet's three Trading Note reflections (C1-C3) and two paragraphs of Keel's last IPS draft (X1-X2),
as in round 2. Keys: <writer letter><passage number>; odd passage numbers are plain, even ones carry one conceit turn.
Packs go to OUTDIR (outside the repo, so readers never see the key); passages.json and order_reader*.txt to the round dir.
"""
import re, random, json, pathlib, sys
rnd = int(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
voice = pathlib.Path(__file__).resolve().parent.parent
repo = pathlib.Path('/home/user/caplet-investment')
d = voice / ('round%d' % rnd)
writers = {5: [('H', 'writer_H.md'), ('J', 'writer_J.md')], 6: [('K', 'writer_K.md'), ('L', 'writer_L.md')]}[rnd]
def parts(fn):
    t = (d / fn).read_text() + '\n=== END ===\n'
    o = {}
    for k in ['P1', 'P2', 'P3', 'P4']:
        m = re.search(r'^=== %s ===\s*\n(.*?)(?=^=== )' % k, t, re.S | re.M)
        o[k] = m.group(1).strip() if m else None
    return o
P = {}
for w, fn in writers:
    for k, v in parts(fn).items():
        assert v, (w, k)
        P[w + k[1]] = re.sub(r'[ \t]*(?<!\n)\n(?!\n)[ \t]*', ' ', v)   # unwrap hard line breaks inside paragraphs
corpus = (voice / 'CORPUS.md').read_text()
refl = re.findall(r'^> \*\*(The Treasury maturing 15 Feb 2037|IBTM|VT)\.\*\*(.*?)(?=^\s*$)', corpus, re.S | re.M)
for i, (h, body) in enumerate(refl[:3], 1):
    P['C%d' % i] = re.sub(r'\n>\s?', ' ', body).strip()
v56 = (repo / 'keel/ips_rewrite/drafts/D36_I81/ips_V56.txt').read_text().split('\n')
P['X1'] = v56[4].strip()
P['X2'] = v56[10].strip() + '\n\n' + v56[12].strip()
keys = sorted(P)
json.dump(P, open(d / 'passages.json', 'w'), indent=1)
random.seed(20261116 + rnd)
for r in (1, 2, 3):
    order = keys[:]; random.shuffle(order)
    lines = ['# Passages for reader %d (%d passages)\n' % (r, len(order))]
    for i, k in enumerate(order, 1):
        lines.append('## Passage %d\n\n%s\n' % (i, P[k]))
    (out / ('pack_r%d_reader%d.md' % (rnd, r))).write_text('\n'.join(lines))
    (d / ('order_reader%d.txt' % r)).write_text(','.join(order))
print(len(keys), keys)
for k in keys: print(k, len(P[k].split()))
