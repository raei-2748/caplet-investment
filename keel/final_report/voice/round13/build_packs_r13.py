"""Build the blind reading packs for voice round 13 (Sun 22 Nov 2026): one long piece per reader.

Usage: python3 -I build_packs_r13.py OUTDIR
Writer L studied long-form explainers before writing; writer M did not. Six readers, three per piece, each reading one
piece once (so recall is not contaminated by the other). Readers 1-3 get one piece and 4-6 the other, assigned by a
seeded coin; the same three roles in each group.
"""
import re, random, json, pathlib, sys
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(__file__).resolve().parent
r11 = d.parent / 'round11'

def piece(fn):
    t = (d / fn).read_text() + '\n=== END ===\n'
    m = re.search(r'^=== PIECE ===\s*\n(.*?)(?=^=== )', t, re.S | re.M)
    assert m, fn
    return m.group(1).strip()

def paragraphs(text):
    ps, held = [], ''
    for block in re.split(r'\n\s*\n', text):
        b = re.sub(r'[ \t]*\n[ \t]*', ' ', block.strip())
        if not b:
            continue
        if b.startswith('#') or (len(b) < 80 and not b.endswith('.')):
            held = (held + ' ' if held else '') + b.lstrip('#').strip()
            continue
        ps.append(('[' + held + '] ' if held else '') + b)
        held = ''
    return ps

P = {'L': paragraphs(piece('writer_L.md')), 'M': paragraphs(piece('writer_M.md'))}
CASE = (r11 / 'brief_r11.md').read_text().split('> Laura Gao', 1)[1].split('\n\nNothing else.', 1)[0]
CASE = 'Laura Gao' + re.sub(r'\n> ?', ' ', CASE).strip()
ROLES = {
    'a': 'You read as an intelligent general reader: a well-read adult who knows the case below and no finance beyond it, reading at a normal pace with other things to do.',
    'b': 'You read as a finance professor judging this competition, with forty entries to get through today; you know bonds and shares well and read each entry once.',
    'c': 'You read as the client in the case: a writer and illustrator with a business degree, reading about your own money and your residency, attentive but not a finance professional.',
}
random.seed(20261122)
first = random.choice(['L', 'M'])
assign = {1: (first, 'a'), 2: (first, 'b'), 3: (first, 'c')}
second = 'M' if first == 'L' else 'L'
assign.update({4: (second, 'a'), 5: (second, 'b'), 6: (second, 'c')})
key = {'assign': {r: v[0] for r, v in assign.items()}, 'paragraphs': {k: len(v) for k, v in P.items()}}
for r, (w, role) in assign.items():
    L = ['# Reader pack %d (voice round 13, Sun 22 Nov 2026)\n' % r,
         'One long piece drafted for a competition team\'s Final Report about a client\'s money. Read it as a section of a report you had been handed.\n',
         '**Your role.** ' + ROLES[role] + '\n',
         '**The case, in brief (what you know before you read).** ' + CASE + '\n',
         '## How to read\n',
         'You are an independent reader, not the writer\'s colleague. Do not open any other file, look anything up, or try to find out who wrote it. Use only the page and the case above.\n',
         '1. **Read the piece once, straight through, at a normal pace, in order.** As you go, keep a one-word mark for each numbered paragraph: **with it** (following and wanting to go on), **drifting** (following but no longer sure why you are being told this), or **lost** (lost the thread of the argument). Do not go back while reading.',
         '2. **Then, before you look back at the piece**, answer from memory, in your own words, without quoting:',
         '   - **A.** The plan\'s argument in three sentences.',
         '   - **B.** The three things you remember most, in order of how strongly.',
         '   - **C.** Any moment where something said earlier paid off later ("so that is why ..."): give the two paragraph numbers if you can, and what clicked.',
         '   - **D.** Any question the piece made you ask that it never answered.',
         '   - **E.** Any sentence that announced or promised a point instead of making it.',
         '3. **Now look back** and fill one table row per paragraph: ¶ | Mark (from step 1) | Follow (1 = understood first time; 2 = needed a second read or had to hold something in mind; 3 = had to rebuild the reasoning or still unsure) | Why (Y = for every step or claim in it you could tell a friend why, from the page alone; N = at least one step or claim has no reason on the page) | Note (one line: for drifting, lost, 2-3 or N, what happened).',
         '4. **Last, two lines:** where in the piece you would most likely have stopped reading if you were busy, and why; and the one change that would most help a reader like you.\n',
         'Write your answers as Markdown to the file named in your instructions, in this order: `## Marks while reading` (¶1: mark, ...), `## From memory` (A-E), `## Paragraph by paragraph` (the table), `## Last`.\n',
         '## The piece\n']
    for i, p in enumerate(P[w], 1):
        L.append('**¶%d** %s\n' % (i, p))
    (out / ('pack_r13_reader%d.md' % r)).write_text('\n'.join(L))
json.dump(P, open(d / 'paragraphs.json', 'w'), indent=1)
json.dump(key, open(d / 'key.json', 'w'), indent=1)
print(key)
