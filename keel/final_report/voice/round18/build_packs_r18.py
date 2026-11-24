"""Build the blind reading packs for voice round 18 (Tue 24 Nov 2026, evening).

Usage: python3 -I build_packs_r18.py OUTDIR
Three readers, one per role (a co-sponsor, a foundation programme officer, a Taiwan arts official), as in round 17.
Every reader reads version 61 (calibration: Caplet followed sentences 1, 5, 6 and 8 only), then Caplet's IPS
paragraph C3 (control), then the team's lead-in (L) and Laura's repaired words (N). Then round 17's five questions
from memory, unchanged. The comparison is round 17's range-first arm (readers 1-3). Writer: writer_Y.md
(brief_r18_Y.md).
"""
import re, json, pathlib, sys
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(__file__).resolve().parent
r11 = d.parent / 'round11'

t = (d / 'writer_Y.md').read_text() + '\n=== END ===\n'
P = {}
for k in ['C', 'L', 'N', 'NOTES']:
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
    'cosponsor': 'You read as a co-sponsor Laura is approaching in 2031: the head of giving at a family-owned company in Taiwan that has sponsored arts venues before. You read English well. You report to the family board, which decides each sponsorship once a year and hates surprises. You read each page once.',
    'officer': 'You read as a programme officer at a US private foundation that funds artists\' residencies. You write the memo your board reads, you check every pledge with your gift and finance office, and you have seen founders over-promise. You read each page once.',
    'official': 'You read as a grants officer at Taiwan\'s Ministry of Culture who handles applications for arts venues and residencies. You read English well but it is your second language. You apply the ministry\'s rules: an applicant shows its own funding share and proof of other bodies\' resources. You read each page once.',
}
READERS = {1: ('N', 'cosponsor'), 2: ('N', 'officer'), 3: ('N', 'official')}
HOW = '''## How to read each text

You are one of several independent readers, not on the writer's side. Do not open any other file, do not look
anything up, and do not try to find out who wrote what. Use only the page and the case above. Read each text straight
through once at a normal pace, from the plain version, then go to its numbered sentences and fill one table row per
sentence:

- **Follow**: 1 = understood the first time; 2 = had to read it again or hold something in mind to get it; 3 = had to
  rebuild the reasoning, or still unsure what it says.
- **Sense**: once understood, does what it says make sense? Y, N with the fault in a few words, or ? cannot judge.
- **Note**: only when Follow is 2-3 or Sense is N or ?: one short line on what is missing or wrong.

For **Passage 2 only**, add a **Paraphrase** column: what the sentence says, in your own everyday words.

Do not be charitable, and do not invent faults: a clear sentence that holds together gets 1 and Y however plain or
elaborate. Long words and long sentences are not faults in themselves.

When you have finished the last table, **do not look back at any text** and answer the five questions at the end of the
pack from memory.

Write your answers as Markdown to the file named in your instructions: one section per text (`## Letter`,
`## Passage 1`, `## Passage 2`), each with its table (columns: # | Follow | Sense | Note, and for Passage 2:
# | Follow | Sense | Paraphrase | Note), then `## From memory` with the five answers.
'''
QUESTIONS = '''## The five questions (answer from memory, without looking back)

1. How much will Laura give towards the building, and when will the money arrive?
2. Could her building contribution end up lower than the figure you just gave? If yes, how low, and what could lower
   it? If no, why not?
3. What is the $95,000 in her words?
4. How sure is she of her figure, and why should a funder believe her?
5. In your role, what figure would you write down as her commitment (to book, to plan around, or to put in a file),
   and what one thing would you still ask her for before committing your own money?
'''
key = {'readers': {}}
for r, (arm, role) in READERS.items():
    L = ['# Reader pack %d (voice round 18, Tue 24 Nov 2026)\n' % r,
         'A short letter from an earlier round of the competition, then two short passages about the same client. '
         'Each is read on its own, as if it were a page you had just turned to.\n',
         '**Your role.** ' + ROLES[role] + '\n',
         '**The case, in brief (what you know before you read).** ' + CASE + '\n', HOW,
         '## The letter\n', v61 + '\n', '### The letter, sentence by sentence\n']
    L += ['- **L%02d** %s' % (i, s) for i, s in enumerate(v61_sents, 1)] + ['']
    passage2 = P['L'] + '\n\n' + P[arm]
    for n, (text, intro) in enumerate([(P['C3'], 'A paragraph from a team\'s letter to Laura.'),
                                       (passage2, 'From a team\'s Final Report on Laura\'s plan: the team\'s lead-in, '
                                                  'then the words Laura could use with co-sponsors in 2031.')], 1):
        L += ['## Passage %d\n' % n, '*' + intro + '*\n', text + '\n', '### Passage %d, sentence by sentence\n' % n]
        L += ['- **P%d.%d** %s' % (n, j, s) for j, s in enumerate(sentences(text), 1)] + ['']
    L.append(QUESTIONS)
    (out / ('pack_r18_reader%d.md' % r)).write_text('\n'.join(L))
    key['readers'][r] = {'arm': arm, 'role': role, 'n_sentences_p2': len(sentences(passage2)),
                         'lead_in_sentences': len(sentences(P['L']))}

def we_rate(t):
    w = re.findall(r"[A-Za-z’']+", t)
    n = sum(1 for x in w if x.lower().replace('’', "'") in {'we', 'our', 'us', "we'll", "we've", "we're", "we'd", 'ours'})
    return round(100 * n / len(w), 2), len(w)
key['we_per_100_words'] = {k: we_rate(P[k]) for k in ['C', 'L', 'N']}
json.dump(P, open(d / 'passages.json', 'w'), indent=1)
json.dump(key, open(d / 'key.json', 'w'), indent=1)
print(json.dumps(key, indent=1))
