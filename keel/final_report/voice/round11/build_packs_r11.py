"""Build the blind reading packs for voice round 11 (Fri 20 Nov 2026, morning).

Usage: python3 -I build_packs_r11.py OUTDIR
Reads writer_U.md, writer_V.md (fresh writers) and writer_K.md (Keel's main session, the control), version 61 of
Keel's IPS (the calibration text, Caplet's ground truth) and Caplet's IPS (paragraphs 3 and 4 as unmarked controls).
Each reader first scores version 61 sentence by sentence, then eight passages: six writer passages and the two
controls. Pack A (readers 1-3): U1 U3 V2 V4 K1 K4 C3 C4. Pack B (readers 4-6): U2 U4 V1 V3 K2 K3 C3 C4. Each reader has
its own role and its own order. Packs go to OUTDIR (outside the repo while reading); the key, passages and sentence
list go to this folder.
"""
import re, random, json, pathlib, sys
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
d = pathlib.Path(__file__).resolve().parent
repo = pathlib.Path('/home/user/caplet-investment')

def parts(fn):
    t = (d / fn).read_text() + '\n=== END ===\n'
    o = {}
    for k in ['P1', 'P2', 'P3', 'P4']:
        m = re.search(r'^=== %s ===\s*\n(.*?)(?=^=== )' % k, t, re.S | re.M)
        assert m, (fn, k)
        o[k] = re.sub(r'[ \t]*(?<!\n)\n(?!\n)[ \t]*', ' ', m.group(1).strip())
    return o

P = {}
for w in 'UVK':
    for k, v in parts('writer_%s.md' % w).items():
        P[w + k[1]] = v
ips = (repo / 'keel/final_report/FINAL_IPS_as_submitted.txt').read_text().split('\n')
paras = [l.strip() for l in ips if l.strip()]
i3 = [i for i, l in enumerate(paras) if l.startswith('In January 2027 we')][0]
i4 = [i for i, l in enumerate(paras) if l.startswith('The building is a different matter')][0]
P['C3'] = paras[i3]
P['C4'] = paras[i4]
topic = {'1': 'T1', '2': 'T2', '3': 'T3', '4': 'T4', 'C3': 'T1', 'C4': 'T2'}
QUESTION = {
    'T1': 'From this passage alone: what pays each $50,000 payment, when is it bought, and why will the money be there on the day it is due?',
    'T2': 'From this passage alone: what does the $150,000 that arrives in January 2028 buy, and why is each part bought then?',
    'T3': 'From this passage alone: what are the two figures Laura gives co-sponsors, how is each one set, and why does she give a range at all?',
    'T4': 'From this passage alone: what does Laura keep promised to no one, about how much is it, and what might it have to pay for?',
}
def tkey(k):
    return topic[k] if k.startswith('C') else topic[k[1]]

SPLIT = re.compile(r'(?<=[.!?])["”’]?\s+(?=[A-Z"“(‘$])')
def sentences(text):
    out = []
    for para in re.split(r'\n\s*\n', text):
        out += [s.strip() for s in SPLIT.split(para.strip()) if s.strip()]
    return out

v61 = (pathlib.Path('/mnt/project-files/ips/FINAL/ips_V61.txt')).read_text().strip()
v61_sents = sentences(v61)
assert len(v61_sents) == 21, len(v61_sents)
CAPLET_FOLLOWED = {1, 5, 6, 8}   # Caplet followed the first line, the ladder's purchase, the name's letters, inflation

ROLES = {
    1: 'You read as a sharp final-year school student who writes top-grade analytical English essays and argues for a living in class. You know the case below well but no finance beyond it. You are impatient with sentences that make you work for nothing, and you are not intimidated by a formal or elevated register.',
    2: 'You read as a finance professor judging this competition, who has forty entries to get through today and reads each once. You know bonds and shares well, so jargon does not stop you; what stops you is a sentence that does not say what it means, or says something that does not follow.',
    3: "You read as a strictly literal reader. You take every word at its ordinary everyday meaning and refuse to repair what the writer left out. If a sentence says a payment 'costs' something, a range 'is owned', or money 'goes into' a fund at a time when it does not yet exist, you report what it literally says, and then say whether that literal claim makes sense.",
    4: 'You read as a newspaper sub-editor whose whole job is making sure every sentence says what it means to an ordinary intelligent reader. You know nothing about finance beyond what the case below says.',
    5: 'You read as a logician checking an argument. For every sentence, find its claim and its stated reason (because, so, therefore, which means, that is why, in effect, a colon). Ask whether the reason really produces the claim, whether events happen in a possible order in time, whether an image or a name is being offered in place of a reason, and whether the sentence is true of anything at all (empty).',
    6: 'You read as the client in the case: a writer and illustrator with a business degree, reading advice addressed to you about your own money and your residency. You are intelligent and attentive, but you are not a finance professional, and you want to know what will be done with your money and why.',
}
CASE = (d / 'brief_r11.md').read_text().split('> Laura Gao', 1)[1].split('\n\nNothing else.', 1)[0]
CASE = 'Laura Gao' + re.sub(r'\n> ?', ' ', CASE).strip()
PACKS = {'A': ['U1', 'U3', 'V2', 'V4', 'K1', 'K4', 'C3', 'C4'], 'B': ['U2', 'U4', 'V1', 'V3', 'K2', 'K3', 'C3', 'C4']}
random.seed(20261120)
key = {'v61_followed_by_caplet': sorted(CAPLET_FOLLOWED), 'readers': {}}
sent_list = {}
for i, s in enumerate(v61_sents, 1):
    sent_list['V%02d' % i] = {'source': 'V61', 'text': s, 'caplet_followed': i in CAPLET_FOLLOWED}
for r in range(1, 7):
    pack = 'A' if r <= 3 else 'B'
    order = PACKS[pack][:]; random.shuffle(order)
    labels = {}
    L = ['# Reader pack %d (voice round 11, Fri 20 Nov 2026)\n' % r,
         'Two kinds of text about the same client: first a short letter, then eight short passages drafted for a competition team\'s Final Report. They come from different writers. Each is read on its own, as if it were a page you had just turned to.\n',
         '**Your role.** ' + ROLES[r] + '\n',
         '**The case, in brief (what you know before you read).** ' + CASE + '\n',
         '## How to read\n',
         'You are one of several independent readers. You are not on the writer\'s side and you are not their colleague. Read the way an intelligent person reads a document they were handed: once, at a normal pace, in order. Do not open any other file, do not look anything up, and do not try to find out who wrote what. Use only what the page and the case above tell you.\n',
         '1. **Read each text straight through once**, without the numbers. Note where you stalled, went back, or gave up.',
         '2. **Then go sentence by sentence** through its numbered list and fill one table row per sentence:',
         '   - **Follow**: 1 = understood the first time; 2 = had to read it again or hold something in mind to get it; 3 = had to rebuild the chain of reasoning, or still unsure what it says.',
         '   - **Sense**: once you have understood it (or done your best), does what it says make sense? Y = yes, it is clear what it claims and the claim holds together. N = no: give the fault in a few words of your own (for example "doesn\'t follow", "impossible as stated", "circular or empty", "points at nothing", "unexplained term", "answers a question nobody asked", "names something never introduced"). ? = cannot judge.',
         '   - **Plain paraphrase**: what the sentence says, in your own everyday words, in one line. If you had to guess, write "guess:" first; put any words the sentence did not give you in [brackets].',
         '   - **Why** (only when Follow is 2-3 or Sense is N or ?): one short line.',
         '3. **Do not be charitable.** If you find yourself working out what the writer must have meant, the sentence did not say it: score Follow 2 or 3, write what you worked out, then judge whether that meaning makes sense. Equally, do not invent faults: a sentence that is clear and holds together gets 1 and Y, however plain or elaborate. Long words, formal register and long sentences are not faults in themselves.',
         '4. **After each passage** (not the letter), answer its question in two or three sentences from the passage alone. If the passage does not say, write "not said".',
         '5. **At the end**, three short sections: **The sentences that made least sense** (up to eight, by number, each with what exactly is wrong); **The clearest passage** (by number, and what it does that the others do not); **Any pattern** in the sentences that failed.\n',
         'Write your answers as Markdown to the file named in your instructions: one section per text (`## Letter` and `## Passage n`), each with a table (columns: # | Follow | Sense | Fault | Plain paraphrase | Why), and for each passage an **Answer:** line after its table; then the three closing sections.\n',
         '## The letter (read it straight through once)\n',
         'A team wrote this short letter to Laura in an earlier round of the competition.\n',
         v61.replace('\n\n', '\n\n') + '\n',
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
    (out / ('pack_r11_reader%d.md' % r)).write_text('\n'.join(L))
    key['readers'][r] = {'pack': pack, 'role': ROLES[r][:60], 'order': order, 'labels': labels}
json.dump(P, open(d / 'passages.json', 'w'), indent=1)
json.dump(key, open(d / 'key.json', 'w'), indent=1)
json.dump(sent_list, open(d / 'sentences.json', 'w'), indent=1)
print({k: len(sentences(v)) for k, v in P.items()})
