"""Build the blind reading packs for voice round 12 (Sun 22 Nov 2026).

Usage: python3 -I build_packs_r12.py OUTDIR
Each of four readers scores version 61 (calibration, Caplet's ground truth) sentence by sentence, then ten passages
in its own shuffled order: W1 W3 W4 X1 X3 X4 (fresh writers, this round), K2 and V4 (round 11's best two, kept for
comparison) and Caplet's IPS paragraphs 3 and 4 (C3, C4). New this round: a Why column for every sentence.
"""
import re, random, json, pathlib, sys
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(__file__).resolve().parent
r11 = d.parent / 'round11'
repo = pathlib.Path('/home/user/caplet-investment')

def parts(fn, keys):
    t = (d / fn).read_text() + '\n=== END ===\n'
    o = {}
    for k in keys:
        m = re.search(r'^=== %s ===\s*\n(.*?)(?=^=== )' % k, t, re.S | re.M)
        assert m, (fn, k)
        o[k] = re.sub(r'[ \t]*(?<!\n)\n(?!\n)[ \t]*', ' ', m.group(1).strip())
    return o

P = {}
for w in 'WX':
    for k, v in parts('writer_%s.md' % w, ['P1', 'P3', 'P4']).items():
        P[w + k[1]] = v
old = json.load(open(r11 / 'passages.json'))
P['K2'] = old['K2']; P['V4'] = old['V4']; P['C3'] = old['C3']; P['C4'] = old['C4']
QUESTION = {
    '1': 'From this passage alone: what pays each $50,000 payment, when is it bought, and why will the money be there on the day it is due?',
    '2': 'From this passage alone: what does the $150,000 that arrives in January 2028 buy, and why is each part bought then?',
    '3': 'From this passage alone: what does Laura tell co-sponsors in 2031, how is it set, and why does she give a range at all?',
    '4': 'From this passage alone: what does Laura keep promised to no one, about how much is it, and what might it have to pay for?',
}
TOPIC = {'C3': '1', 'C4': '2'}
def tkey(k): return TOPIC.get(k, k[1])

SPLIT = re.compile(r'(?<=[.!?])["”’]?\s+(?=[A-Z"“(‘$])')
ABBREV = re.compile(r'(?:\b[A-Z]\.[A-Z]\.|\b(?:Mr|Mrs|Ms|Dr|St|No|vs|e\.g|i\.e)\.)$')
def sentences(text):
    # Round 12 split "J.P. Morgan" into two rows (W4.2, X3.7, X4.3); a piece ending in an
    # abbreviation is now joined to the next (fixed Sun 22 Nov 2026, for round 14 on).
    o = []
    for para in re.split(r'\n\s*\n', text):
        for s in (s.strip() for s in SPLIT.split(para.strip()) if s.strip()):
            if o and ABBREV.search(o[-1]) and not o[-1].endswith('\n'):
                o[-1] = o[-1] + ' ' + s
            else:
                o.append(s)
    return o

v61 = pathlib.Path('/mnt/project-files/ips/FINAL/ips_V61.txt').read_text().strip()
v61_sents = sentences(v61)
assert len(v61_sents) == 21, len(v61_sents)
CAPLET_FOLLOWED = {1, 5, 6, 8}
UNFLAGGED_R11 = {12, 13, 16, 20, 21}
ROLES = {
    1: 'You read as a finance professor judging this competition, who has forty entries to get through today and reads each once. You know bonds and shares well, so jargon does not stop you; what stops you is a sentence that does not say what it means, a step taken without a reason, or a claim that does not follow.',
    2: "You read as a strictly literal reader. You take every word at its ordinary everyday meaning and refuse to repair what the writer left out. If a sentence says a range 'is owned', or that something is done 'so' something else follows, you report what it literally says, and then whether that literal claim makes sense and whether its reason is really there.",
    3: 'You read as a logician checking an argument. For every sentence, find its claim and its stated reason (because, so, therefore, which means, that is why, a colon). Ask whether the reason really produces the claim, whether events happen in a possible order in time, whether a name or an image is offered in place of a reason, and whether the sentence is true of anything at all (empty).',
    4: 'You read as the client in the case: a writer and illustrator with a business degree, reading advice about your own money and your residency. You are intelligent and attentive but not a finance professional, and for every step you want to know why it is being done.',
}
CASE = (r11 / 'brief_r11.md').read_text().split('> Laura Gao', 1)[1].split('\n\nNothing else.', 1)[0]
CASE = 'Laura Gao' + re.sub(r'\n> ?', ' ', CASE).strip()
ORDER = ['W1', 'W3', 'W4', 'X1', 'X3', 'X4', 'K2', 'V4', 'C3', 'C4']
random.seed(20261122)
key = {'v61_followed_by_caplet': sorted(CAPLET_FOLLOWED), 'v61_unflagged_r11': sorted(UNFLAGGED_R11), 'readers': {}}
sent_list = {}
for i, s in enumerate(v61_sents, 1):
    sent_list['V%02d' % i] = {'source': 'V61', 'text': s, 'caplet_followed': i in CAPLET_FOLLOWED}
for r in range(1, 5):
    order = ORDER[:]; random.shuffle(order)
    labels = {}
    L = ['# Reader pack %d (voice round 12, Sun 22 Nov 2026)\n' % r,
         'Two kinds of text about the same client: first a short letter, then ten short passages drafted for a competition team\'s Final Report. They come from different writers. Each is read on its own, as if it were a page you had just turned to.\n',
         '**Your role.** ' + ROLES[r] + '\n',
         '**The case, in brief (what you know before you read).** ' + CASE + '\n',
         '## How to read\n',
         'You are one of several independent readers. You are not on the writer\'s side and you are not their colleague. Read the way an intelligent person reads a document they were handed: once, at a normal pace, in order. Do not open any other file, do not look anything up, and do not try to find out who wrote what. Use only what the page and the case above tell you.\n',
         '1. **Read each text straight through once**, without the numbers. Note where you stalled, went back, or gave up.',
         '2. **Then go sentence by sentence** through its numbered list and fill one table row per sentence:',
         '   - **Follow**: 1 = understood the first time; 2 = had to read it again or hold something in mind to get it; 3 = had to rebuild the chain of reasoning, or still unsure what it says.',
         '   - **Sense**: once understood (or your best attempt), does what it says make sense? Y = yes. N = no: give the fault in a few words of your own (for example "doesn\'t follow", "impossible as stated", "circular or empty", "points at nothing", "unexplained term", "names something never introduced"). ? = cannot judge.',
         '   - **Why**: if the sentence takes a step (something is bought, set, moved, chosen, kept back) or makes a claim (something is said to be true, safe, enough, likely), could you tell a friend, from this page alone, *why* the step is taken or *why* the claim is true? The reason may be in the same sentence or anywhere earlier or later in the same text. Y = yes, and say the reason in a few words in the Paraphrase column; N = no, the page gives no reason, or the reason it gives does not produce the step or claim; - = the sentence takes no step and makes no claim (a fact of the case, a date, a definition).',
         '   - **Plain paraphrase**: what the sentence says, in your own everyday words, in one line; if you had to guess, write "guess:" first; put words the sentence did not give you in [brackets].',
         '   - **Note** (only when Follow is 2-3, Sense is N or ?, or Why is N): one short line on what is missing or wrong.',
         '3. **Do not be charitable.** If you find yourself supplying a reason the page did not give, the page did not give it: Why is N. Equally, do not invent faults: a sentence that is clear, holds together and has its reason gets 1, Y and Y, however plain or elaborate. Long words, formal register and long sentences are not faults in themselves.',
         '4. **After each passage** (not the letter), answer its question in two or three sentences from the passage alone. If the passage does not say, write "not said".',
         '5. **At the end**, three short sections: **The sentences that made least sense or gave no reason** (up to eight, by number, each with what exactly is wrong); **The clearest passage** (by number, and what it does that the others do not); **Any pattern** in the sentences that failed.\n',
         'Write your answers as Markdown to the file named in your instructions: one section per text (`## Letter` and `## Passage n`), each with a table (columns: # | Follow | Sense | Why | Fault | Plain paraphrase | Note), and for each passage an **Answer:** line after its table; then the three closing sections.\n',
         '## The letter (read it straight through once)\n',
         'A team wrote this short letter to Laura in an earlier round of the competition.\n',
         v61 + '\n',
         '### The letter, sentence by sentence\n']
    for i, s in enumerate(v61_sents, 1):
        L.append('- **L%02d** %s' % (i, s))
    L.append('')
    for n, k in enumerate(order, 1):
        lab = 'P%d%02d' % (r, n)
        labels[lab] = k
        L.append('## Passage %d\n' % n)
        L.append(P[k] + '\n')
        L.append('### Passage %d, sentence by sentence\n' % n)
        for j, s in enumerate(sentences(P[k]), 1):
            sid = '%s.%d' % (lab, j)
            L.append('- **%s** %s' % (sid, s))
            sent_list[sid] = {'source': k, 'text': s}
        L.append('\n**Question for passage %d.** %s\n' % (n, QUESTION[tkey(k)]))
    (out / ('pack_r12_reader%d.md' % r)).write_text('\n'.join(L))
    key['readers'][r] = {'role': ROLES[r][:60], 'order': order, 'labels': labels}
json.dump(P, open(d / 'passages.json', 'w'), indent=1)
json.dump(key, open(d / 'key.json', 'w'), indent=1)
json.dump(sent_list, open(d / 'sentences.json', 'w'), indent=1)
print({k: len(sentences(v)) for k, v in P.items()})
