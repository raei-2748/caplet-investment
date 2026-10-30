import re, glob, os, json
R='/home/user/caplet-investment/'
def windows(text, n=220, minw=120):
    w = text.split(); out=[]
    for i in range(0, len(w), n):
        c = w[i:i+n]
        if len(c) >= minw: out.append(' '.join(c))
    return out
def clean_md(t):
    t = re.sub(r'`[^`]*`', '', t); t = re.sub(r'\*\*|__|#+ ', '', t); t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    return t
docs = []  # (source_id, label, text)  label 1 = human
# human: Ahaan's essays (split by essay title lines)
ess = open('/mnt/project-files/voice/ahaan_essays_2026-10-24.txt').read()
for i, w in enumerate(windows(ess)): docs.append((f'essay', 1, w))
# human: Caplet's own messages quoted in the Bible (lines starting "> ")
bib = open(R+'keel/BIBLE.md').read()
book = None; buf = {}
for line in bib.split('\n'):
    m = re.match(r'#+ .*Book (\d+)', line)
    if m: book = m.group(1)
    if line.startswith('> ') and book: buf.setdefault(book, []).append(line[2:])
for b, lines in buf.items():
    for w in windows(clean_md(' '.join(lines))): docs.append((f'bible{b}', 1, w))
# AI: our drafts
for d in sorted(glob.glob(R+'keel/ips_rewrite/drafts/*/ips.txt')):
    t = open(d).read()
    if len(t.split()) > 150: docs.append(('draft_'+d.split('/')[-2], 0, ' '.join(t.split()[:520])))
for f in sorted(glob.glob(R+'keel/ips_rewrite/rivals/*.md')):
    s = open(f).read()
    if '## IPS' in s:
        ips = s.split('## IPS',1)[1].split('## SIMULATOR NOTES')[0]
        docs.append(('rival_'+os.path.basename(f)[:3], 0, ' '.join(clean_md(ips).split()[:520])))
for f in sorted(glob.glob('ai_controls/*.txt')):
    for w in windows(open(f).read()): docs.append(('ctl_'+os.path.basename(f)[:-4], 0, w))
# held-out (not trained on): last year's human report, Wharton's case
knox = clean_md(open(R+'caplet/google_drive/2025_knox_wharton.md').read())
held = [('knox2025', 1, w) for w in windows(knox)[40:70]]
case = open(R+'competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt').read()
held += [('wharton_case', 1, w) for w in windows(case)]
json.dump({'train': docs, 'held': held}, open('corpus.json','w'))
from collections import Counter
print(Counter((d[0].split('_')[0], d[1]) for d in docs)); print(len(held))
