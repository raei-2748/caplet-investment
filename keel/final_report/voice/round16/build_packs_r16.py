"""Build the blind reading packs for voice round 16 (Mon 23 Nov 2026, evening).

Usage: python3 -I build_packs_r16.py OUTDIR
Six readers in two arms. Every reader reads version 61 (calibration: Caplet followed sentences 1, 5, 6 and 8 only),
then Caplet's IPS paragraph C3 (control), then D (the report's first use of pencil and ink), then, "some pages later",
the team's lead-in and Laura's words to co-sponsors: plain (P) for readers 4-6, or with one added sentence carrying
"a signature is the other kind of ink" (T) for readers 1-3. Roles are matched across arms. Then four questions from
memory. Writer: writer_X.md (brief_r16_X.md).
"""
import re, json, pathlib, sys
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(__file__).resolve().parent
r11 = d.parent / 'round11'

t = (d / 'writer_X.md').read_text() + '\n=== END ===\n'
P = {}
for k in ['C', 'D', 'P', 'T', 'NOTES']:
    m = re.search(r'^=== %s ===\s*\n(.*?)(?=^=== )' % k, t, re.S | re.M)
    assert m, k
    P[k] = m.group(1).strip()
P['C3'] = json.load(open(r11 / 'passages.json'))['C3']

SPLIT = re.compile(r'(?<=[.!?])["”’]?\s+(?=[A-Z"“(‘$])')
ABBREV = re.compile(r'(?:\b[A-Z]\.[A-Z]\.|\b(?:Mr|Mrs|Ms|Dr|St|No|vs|e\.g|i\.e)\.)$')
def sentences(text):
    o = []
    for para in re.split(r'\n\s*\n', text):
        para = re.sub(r'\s*\n\s*', ' ', para.strip())
        for s in (s.strip() for s in SPLIT.split(para) if s.strip()):
            if o and ABBREV.search(o[-1]):
                o[-1] = o[-1] + ' ' + s
            else:
                o.append(s)
    return o

# The one added sentence: the sentence in T that is not in P.
pS, tS = sentences(P['P']), sentences(P['T'])
added = [s for s in tS if s not in pS]
assert len(added) == 1 and 'other kind of ink' in added[0], added
assert [s for s in tS if s != added[0]] == pS, 'T differs from P beyond the added sentence'

v61 = pathlib.Path('/mnt/project-files/ips/FINAL/ips_V61.txt').read_text().strip()
v61_sents = sentences(v61)
assert len(v61_sents) == 21, len(v61_sents)
CASE = (r11 / 'brief_r11.md').read_text().split('> Laura Gao', 1)[1].split('\n\nNothing else.', 1)[0]
CASE = 'Laura Gao' + re.sub(r'\n> ?', ' ', CASE).strip()
ROLES = {
    'prof': 'You read as a finance professor judging this competition, who has forty entries to get through today and reads each once. You know bonds and shares well, so jargon does not stop you; what stops you is a sentence that does not say what it means, a step taken without a reason, or a claim that does not follow.',
    'literal': 'You read as a strictly literal reader. You take every word at its ordinary everyday meaning and refuse to repair what the writer left out.',
    'client': 'You read as the client in the case: a writer and illustrator with a business degree, reading advice about your own money and your residency. You are intelligent and attentive but not a finance professional, and for every step you want to know why it is being done.',
}
READERS = {1: ('T', 'prof'), 2: ('T', 'literal'), 3: ('T', 'client'),
           4: ('P', 'prof'), 5: ('P', 'literal'), 6: ('P', 'client')}
HOW = '''## How to read each text

You are one of several independent readers, not on the writer's side. Do not open any other file, do not look
anything up, and do not try to find out who wrote what. Use only the page and the case above. Read each text straight
through once at a normal pace, from the plain version, then go to its numbered sentences and fill one table row per
sentence:

- **Follow**: 1 = understood the first time; 2 = had to read it again or hold something in mind to get it; 3 = had to
  rebuild the reasoning, or still unsure what it says.
- **Sense**: once understood, does what it says make sense? Y, N with the fault in a few words, or ? cannot judge.
- **Note**: only when Follow is 2-3 or Sense is N or ?: one short line on what is missing or wrong.

For the **last passage only**, add a **Paraphrase** column: what the sentence says, in your own everyday words.

Do not be charitable, and do not invent faults: a clear sentence that holds together gets 1 and Y however plain or
elaborate. Long words and long sentences are not faults in themselves.

When you have finished the last table, **do not look back at any text** and answer the four questions at the end of the
pack from memory.

Write your answers as Markdown to the file named in your instructions: one section per text (`## Letter`,
`## Passage 1`, `## Passage 2`, `## Passage 3`), each with its table (columns: # | Follow | Sense | Note, and for
Passage 3: # | Follow | Sense | Paraphrase | Note), then `## From memory` with the four answers.
'''
QUESTIONS = '''## The four questions (answer from memory, without looking back)

1. In this report, what does it mean for a figure to be "in ink"? Say it in your own words, as you would to a friend.
2. What does Laura tell co-sponsors about her contribution to the building, and what stands behind each figure she
   gives?
3. Is there a difference between Laura owning the money and Laura signing for it? If so, what is it, and why would a
   funder care?
4. In the last passage, did any word seem to change its meaning from how it was used earlier? If so, which word, what
   did you take it to mean there, and did that help or get in the way?
'''
key = {'added_sentence': added[0], 'readers': {}}
for r, (arm, role) in READERS.items():
    last = P[arm]
    L = ['# Reader pack %d (voice round 16, Mon 23 Nov 2026)\n' % r,
         'A short letter from an earlier round of the competition, then three short passages about the same client. '
         'Each is read on its own, as if it were a page you had just turned to.\n',
         '**Your role.** ' + ROLES[role] + '\n',
         '**The case, in brief (what you know before you read).** ' + CASE + '\n', HOW,
         '## The letter\n', v61 + '\n', '### The letter, sentence by sentence\n']
    L += ['- **L%02d** %s' % (i, s) for i, s in enumerate(v61_sents, 1)] + ['']
    for n, (k, intro) in enumerate([('C3', 'A paragraph from a team\'s letter to Laura.'),
                                    ('D', 'The first page of a team\'s Final Report on Laura\'s plan.'),
                                    (arm, 'Some pages later in the same Final Report: the part that gives the words '
                                          'Laura could use with co-sponsors.')], 1):
        L += ['## Passage %d\n' % n, '*' + intro + '*\n', P[k] + '\n', '### Passage %d, sentence by sentence\n' % n]
        L += ['- **P%d.%d** %s' % (n, j, s) for j, s in enumerate(sentences(P[k]), 1)] + ['']
    L.append(QUESTIONS)
    (out / ('pack_r16_reader%d.md' % r)).write_text('\n'.join(L))
    key['readers'][r] = {'arm': arm, 'role': role,
                         'added_index': (sentences(last).index(added[0]) + 1) if arm == 'T' else None}

def we_rate(t):
    w = re.findall(r"[A-Za-z’']+", t)
    n = sum(1 for x in w if x.lower().replace('’', "'") in {'we', 'our', 'us', "we'll", "we've", "we're", "we'd", 'ours'})
    return round(100 * n / len(w), 2), len(w)
key['we_per_100_words'] = {k: we_rate(P[k]) for k in ['C', 'D', 'P', 'T']}
json.dump(P, open(d / 'passages.json', 'w'), indent=1)
json.dump(key, open(d / 'key.json', 'w'), indent=1)
print(json.dumps(key, indent=1))
