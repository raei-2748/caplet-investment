"""Build the blind reading packs for voice round 14 (Sun 22 Nov 2026, evening).

Usage: python3 -I build_packs_r14.py OUTDIR
Each of four readers reads version 61 (calibration, Caplet's ground truth), then seven passages in its own shuffled
order: Y3 Y5 Z3 Z5 (fresh writers who first carried the IPS on from its last line), X3 (round 12's range passage, the
same topic) and Caplet's IPS paragraphs 3 and 4 (C3, C4). New this round: a cold retelling of each text's steps and
reasons, written before the reader goes back to the sentences; a separate blind scorer marks each retold reason.
"""
import re, random, json, pathlib, sys
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(__file__).resolve().parent
r11 = d.parent / 'round11'; r12 = d.parent / 'round12'

def parts(fn, keys):
    t = (d / fn).read_text() + '\n=== END ===\n'
    o = {}
    for k in keys:
        m = re.search(r'^=== %s ===\s*\n(.*?)(?=^=== )' % k, t, re.S | re.M)
        assert m, (fn, k)
        o[k] = re.sub(r'[ \t]*(?<!\n)\n(?!\n)[ \t]*', ' ', m.group(1).strip())
    return o

P, CONT = {}, {}
for w in 'YZ':
    p = parts('writer_%s.md' % w, ['C', 'P3', 'P5'])
    P[w + '3'] = p['P3']; P[w + '5'] = p['P5']; CONT[w] = p['C']
old12 = json.load(open(r12 / 'passages.json'))
old11 = json.load(open(r11 / 'passages.json'))
P['X3'] = old12['X3']; P['C3'] = old11['C3']; P['C4'] = old11['C4']

SPLIT = re.compile(r'(?<=[.!?])["”’]?\s+(?=[A-Z"“(‘$])')
ABBREV = re.compile(r'(?:\b[A-Z]\.[A-Z]\.|\b(?:Mr|Mrs|Ms|Dr|St|No|vs|e\.g|i\.e)\.)$')
def sentences(text):
    o = []
    for para in re.split(r'\n\s*\n', text):
        for s in (s.strip() for s in SPLIT.split(para.strip()) if s.strip()):
            if o and ABBREV.search(o[-1]):
                o[-1] = o[-1] + ' ' + s
            else:
                o.append(s)
    return o

v61 = pathlib.Path('/mnt/project-files/ips/FINAL/ips_V61.txt').read_text().strip()
v61_sents = sentences(v61)
assert len(v61_sents) == 21, len(v61_sents)
CAPLET_FOLLOWED = {1, 5, 6, 8}
UNFLAGGED = {12, 13, 16, 20, 21}
ROLES = {
    1: 'You read as a finance professor judging this competition, who has forty entries to get through today and reads each once. You know bonds and shares well, so jargon does not stop you; what stops you is a sentence that does not say what it means, a step taken without a reason, or a claim that does not follow.',
    2: "You read as a strictly literal reader. You take every word at its ordinary everyday meaning and refuse to repair what the writer left out.",
    3: 'You read as a logician checking an argument: for every step, what is its reason, and does the reason really produce it?',
    4: 'You read as the client in the case: a writer and illustrator with a business degree, reading advice about your own money and your residency. You are intelligent and attentive but not a finance professional, and for every step you want to know why it is being done.',
}
CASE = (r11 / 'brief_r11.md').read_text().split('> Laura Gao', 1)[1].split('\n\nNothing else.', 1)[0]
CASE = 'Laura Gao' + re.sub(r'\n> ?', ' ', CASE).strip()
ORDER = ['Y3', 'Y5', 'Z3', 'Z5', 'X3', 'C3', 'C4']
random.seed(202611221)
key = {'v61_followed_by_caplet': sorted(CAPLET_FOLLOWED), 'v61_unflagged': sorted(UNFLAGGED), 'readers': {}}
sent_list = {}
for i, s in enumerate(v61_sents, 1):
    sent_list['L%02d' % i] = {'source': 'V61', 'text': s, 'caplet_followed': i in CAPLET_FOLLOWED}
HOW = [
 '## How to read each text (the letter and every passage, the same three steps)\n',
 'You are one of several independent readers, not on the writer\'s side. Do not open any other file, do not look anything up, and do not try to find out who wrote what. Use only the page and the case above.\n',
 '1. **Read the text straight through once**, at a normal pace, from the plain version (not the numbered list).',
 '2. **Retell it cold.** Now, without looking back at the text, write a short retelling for a friend who keeps asking "but why?". One numbered line per thing the text says is done, chosen, set, moved, kept or claimed to be true: `R1. Step: ... | Because: ...`, in your own everyday words. The "Because" is the reason the text gave you, as you remember it, said so that your friend would be satisfied. If you remember the step but no reason, write `Because: none that I recall`. If the only reason you can give is the step said again in other words, write it anyway, as it comes. Do not go back to the text while you write this, and never change a retelling line afterwards.',
 '3. **Then go back to the numbered sentences** and fill one table row per sentence: **Follow** (1 = understood the first time; 2 = had to read it again or hold something in mind to get it; 3 = had to rebuild the reasoning, or still unsure what it says); **Sense** (once understood, does what it says make sense? Y, N with the fault in a few words, or ? cannot judge); **From** (which of your retelling lines, if any, came from this sentence, for example "R2" or "R2, R3", or "-" if none); **Note** (only when Follow is 2-3 or Sense is N or ?: one short line on what is missing or wrong).',
 '\nDo not be charitable, and do not invent faults: a clear sentence that holds together gets 1 and Y however plain or elaborate. Long words and long sentences are not faults in themselves.\n',
 'Write your answers as Markdown to the file named in your instructions: one section per text (`## Letter`, `## Passage n`), each with **Retelling** (the numbered lines, written before the table) and then the table (columns: # | Follow | Sense | From | Note). At the end, three short sections: **Steps I could not give a reason for** (up to eight, by text and retelling line, each with what was missing); **The clearest passage** (by number, and what it does that the others do not); **Any pattern** in what failed.\n']
for r in range(1, 5):
    order = ORDER[:]; random.shuffle(order)
    labels = {}
    L = ['# Reader pack %d (voice round 14, Sun 22 Nov 2026)\n' % r,
         'Two kinds of text about the same client: first a short letter, then seven short passages drafted for a competition team\'s Final Report. They come from different writers. Each is read on its own, as if it were a page you had just turned to.\n',
         '**Your role.** ' + ROLES[r] + '\n',
         '**The case, in brief (what you know before you read).** ' + CASE + '\n'] + HOW + [
         '## The letter\n', 'A team wrote this short letter to Laura in an earlier round of the competition. Read it straight through once, then retell it cold, then go to its numbered sentences.\n',
         v61 + '\n', '### The letter, sentence by sentence (only after your retelling)\n']
    for i, s in enumerate(v61_sents, 1):
        L.append('- **L%02d** %s' % (i, s))
    L.append('')
    for n, k in enumerate(order, 1):
        lab = 'P%d%02d' % (r, n)
        labels[lab] = k
        L.append('## Passage %d\n' % n)
        L.append(P[k] + '\n')
        L.append('### Passage %d, sentence by sentence (only after your retelling)\n' % n)
        for j, s in enumerate(sentences(P[k]), 1):
            sid = '%s.%d' % (lab, j)
            L.append('- **%s** %s' % (sid, s))
            sent_list[sid] = {'source': k, 'text': s}
        L.append('')
    (out / ('pack_r14_reader%d.md' % r)).write_text('\n'.join(L))
    key['readers'][r] = {'role': ROLES[r][:60], 'order': order, 'labels': labels}
def we_rate(t):
    w = re.findall(r"[A-Za-z’']+", t)
    n = sum(1 for x in w if x.lower().replace('’', "'") in {'we', 'our', 'us', "we'll", "we've", "we're", "we'd", 'ours'})
    return round(100 * n / len(w), 2), len(w)
key['we_per_100_words'] = {k: we_rate(v) for k, v in list(P.items()) + [('cont_' + w, c) for w, c in CONT.items()]}
json.dump(P, open(d / 'passages.json', 'w'), indent=1)
json.dump(CONT, open(d / 'continuations.json', 'w'), indent=1)
json.dump(key, open(d / 'key.json', 'w'), indent=1)
json.dump(sent_list, open(d / 'sentences.json', 'w'), indent=1)
print({k: len(sentences(v)) for k, v in P.items()})
print(key['we_per_100_words'])
