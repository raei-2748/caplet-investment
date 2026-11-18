"""Score voice round 10 (Thu 19 Nov 2026, morning; adapted from round 9). Usage: python3 -I score_r10.py 10.

Reads roundN/passages.json, order_reader{1,2,3}.txt and reading_{1,2,3}.md. Prints each passage's verdicts and ranks,
then per writer and per condition: P1 is 3e plain, P2 3e with one turn, P3 3b plain, P4 3b with one turn.
"""
import collections, json, pathlib, re, sys
rnd = int(sys.argv[1]); d = pathlib.Path(__file__).resolve().parent.parent / ('round%d' % rnd)
P = json.load(open(d / 'passages.json')); N = len(P)
res = collections.defaultdict(list); ranks = collections.defaultdict(list); yes = collections.defaultdict(int)
for r in (1, 2, 3):
    order = (d / f'order_reader{r}.txt').read_text().strip().split(',')
    t = (d / f'reading_{r}.md').read_text()
    blocks = re.split(r'^### Passage (\d+)\s*$', t, flags=re.M)
    got = {}
    for i in range(1, len(blocks), 2):
        m = re.search(r'\*\*Verdict:?\*\*:?\s*\**\s*(Surely not|Probably not|Surely|Probably)', blocks[i + 1], re.I)
        got[int(blocks[i])] = m.group(1).lower() if m else None
    for n, k in enumerate(order, 1):
        v = got.get(n); res[k].append(v)
        if v in ('surely', 'probably'): yes[k] += 1
    mm = re.search(r'(?is)^###\s*Ranking[^\n]*\n(.*?)(?=^###|\Z)', t, re.M)
    seq = [int(x) for x in re.findall(r'(?m)^\s*\d+\.\s*(?:Passage\s*)?(\d+)', mm.group(1))] if mm else []
    seen = []
    for x in seq:
        if x not in seen and 1 <= x <= N: seen.append(x)
    for pos, x in enumerate(seen[:N], 1):
        ranks[order[x - 1]].append(pos)
    print('reader', r, 'verdicts parsed', sum(1 for v in got.values() if v), 'ranking length', len(seen))
def mean(xs): return sum(xs) / len(xs) if xs else float('nan')
for k in sorted(P):
    print(k, res[k], 'yes', yes[k], 'ranks', ranks[k], 'mean %.1f' % mean(ranks[k]))
print('\nBy writer:')
for g in sorted({k[0] for k in P}):
    ks = [k for k in P if k[0] == g]
    print(g, f'{sum(yes[k] for k in ks)}/{3 * len(ks)}', 'mean rank %.1f' % mean([x for k in ks for x in ranks[k]]))
print('\nBy condition (practice writers only):')
for g in sorted({k[0] for k in P} - {'C', 'X'}):
    for cond, nums in (('3e plain', '1'), ('3e one turn', '2'), ('Laura to co-sponsors (plain)', '34')):
        ks = [k for k in P if k[0] == g and k[1] in nums]
        print(g, cond, f'{sum(yes[k] for k in ks)}/{3 * len(ks)}', 'mean rank %.1f' % mean([x for k in ks for x in ranks[k]]))
