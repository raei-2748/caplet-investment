"""Build the blind reading packs for voice round 19 (Wed 25 Nov 2026, morning).

Usage: python3 -I build_packs_r19.py OUTDIR
Three readers, one in each of panel 5's roles (an LDI professor, an arts capital-campaign consultant, a teacher who
reads first-round entries). Every reader reads version 61 (calibration: Caplet followed sentences 1, 5, 6 and 8 only),
then Caplet's IPS paragraph C3 (control), then A (the commitment and the reserve) and E (assumptions, limits and what
to watch). Then five questions from memory. Writer: writer_Z.md (brief_r19_Z.md).
"""
import re, json, pathlib, sys
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(__file__).resolve().parent
r11 = d.parent / 'round11'

t = (d / 'writer_Z.md').read_text() + '\n=== END ===\n'
P = {}
for k in ['C', 'A', 'E', 'NOTES']:
    m = re.search(r'^=== %s ===\s*\n(.*?)(?=^=== )' % k, t, re.S | re.M)
    assert m, k
    P[k] = m.group(1).strip()
P['C3'] = json.load(open(r11 / 'passages.json'))['C3']

SPLIT = re.compile(r'(?<=[.!?])["”’]?\s+(?=[A-Z"“(‘$>])')
ABBREV = re.compile(r'(?:\b[A-Z]\.[A-Z]\.|\b(?:Mr|Mrs|Ms|Dr|St|No|vs|e\.g|i\.e)\.)$')
def sentences(text):
    o = []
    for para in re.split(r'\n\s*\n', text):
        para = re.sub(r'\s*\n\s*', ' ', para.strip())
        para = re.sub(r'^>\s*', '', para)
        para = re.sub(r'\s>\s', ' ', para)
        for s in (s.strip() for s in SPLIT.split(para) if s.strip()):
            if o and ABBREV.search(o[-1]):
                o[-1] = o[-1] + ' ' + s
            else:
                o.append(s)
    return o


v61 = pathlib.Path('/mnt/project-files/ips/FINAL/ips_V61.txt').read_text().strip()
v61_sents = sentences(v61)
assert len(v61_sents) == 21, len(v61_sents)
CASE = (r11 / 'brief_r11.md').read_text().split('> Laura Gao', 1)[1].split('\n\nNothing else.', 1)[0]
CASE = 'Laura Gao' + re.sub(r'\n> ?', ' ', CASE).strip()
ROLES = {
    'professor': 'You read as a professor who teaches liability-driven investing and fixed income to graduate students, and has judged student investment competitions. You know exactly how bonds, bond funds and pension hedges work, and you mark down any loose claim. You read each page once.',
    'consultant': 'You read as a consultant who runs capital campaigns for arts buildings: you raise money from foundations, companies and government, and you know how donors judge a founder\'s promises. You are not an investment specialist. You read each page once.',
    'teacher': 'You read as a high-school economics teacher who coaches students for investment competitions and reads first-round entries. You are a careful general reader with some finance, not a specialist. You read each page once.',
}
READERS = {1: ('AE', 'professor'), 2: ('AE', 'consultant'), 3: ('AE', 'teacher')}
HOW = '''## How to read each text

You are one of several independent readers, not on the writer's side. Do not open any other file, do not look
anything up, and do not try to find out who wrote what. Use only the page and the case above. Read each text straight
through once at a normal pace, from the plain version, then go to its numbered sentences and fill one table row per
sentence:

- **Follow**: 1 = understood the first time; 2 = had to read it again or hold something in mind to get it; 3 = had to
  rebuild the reasoning, or still unsure what it says.
- **Sense**: once understood, does what it says make sense? Y, N with the fault in a few words, or ? cannot judge.
- **Note**: only when Follow is 2-3 or Sense is N or ?: one short line on what is missing or wrong.

For **Passage 3 only**, add a **Paraphrase** column: what the sentence says, in your own everyday words.

Do not be charitable, and do not invent faults: a clear sentence that holds together gets 1 and Y however plain or
elaborate. Long words and long sentences are not faults in themselves.

When you have finished the last table, **do not look back at any text** and answer the five questions at the end of the
pack from memory.

Write your answers as Markdown to the file named in your instructions: one section per text (`## Letter`,
`## Passage 1`, `## Passage 2`, `## Passage 3`), each with its table (columns: # | Follow | Sense | Note, and for
Passage 3: # | Follow | Sense | Paraphrase | Note), then `## From memory` with the five answers.
'''
QUESTIONS = '''## The five questions (answer from memory, without looking back)

1. What do Laura's ten payments rest on from January 2028, and what did that cost her?
2. Why does the team hold the payments to that standard, rather than counting on the interest the bonds pay?
3. What would make the team change the plan?
4. For each of these, what could make it fall short, roughly how large a change that would take, and who would bear
   the loss: (a) the ten payments; (b) the top figure she states to co-sponsors; (c) her flexibility.
5. What could a fall in share prices change, and what could it not? In your role, what one sentence or point would you
   ask the team to make clearer?
'''
key = {'readers': {}}
for r, (arm, role) in READERS.items():
    L = ['# Reader pack %d (voice round 19, Wed 25 Nov 2026)\n' % r,
         'A short letter from an earlier round of the competition, then three short passages about the same client. '
         'Each is read on its own, as if it were a page you had just turned to.\n',
         '**Your role.** ' + ROLES[role] + '\n',
         '**The case, in brief (what you know before you read).** ' + CASE + '\n', HOW,
         '## The letter\n', v61 + '\n', '### The letter, sentence by sentence\n']
    L += ['- **L%02d** %s' % (i, s) for i, s in enumerate(v61_sents, 1)] + ['']
    texts = [(P['C3'], 'A paragraph from a team\'s letter to Laura.'),
             (P['A'], 'From a team\'s Final Report on Laura\'s plan: the ten-year commitment and the operating reserve.'),
             (P['E'], 'From the same report: assumptions, limits and what to watch.')]
    for n, (text, intro) in enumerate(texts, 1):
        L += ['## Passage %d\n' % n, '*' + intro + '*\n', text + '\n', '### Passage %d, sentence by sentence\n' % n]
        L += ['- **P%d.%d** %s' % (n, j, s) for j, s in enumerate(sentences(text), 1)] + ['']
    L.append(QUESTIONS)
    (out / ('pack_r19_reader%d.md' % r)).write_text('\n'.join(L))
    key['readers'][r] = {'arm': arm, 'role': role, 'n_sentences_A': len(sentences(P['A'])),
                         'n_sentences_E': len(sentences(P['E']))}

def we_rate(t):
    w = re.findall(r"[A-Za-z’']+", t)
    n = sum(1 for x in w if x.lower().replace('’', "'") in {'we', 'our', 'us', "we'll", "we've", "we're", "we'd", 'ours'})
    return round(100 * n / len(w), 2), len(w)
key['we_per_100_words'] = {k: we_rate(P[k]) for k in ['C', 'A', 'E']}
json.dump(P, open(d / 'passages.json', 'w'), indent=1)
json.dump(key, open(d / 'key.json', 'w'), indent=1)
print(json.dumps(key, indent=1))
