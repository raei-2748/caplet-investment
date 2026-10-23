import csv, re, sys
from rapidfuzz import fuzz
notes = []
for line in open('caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md'):
    m = re.match(r'\| (\d\d/\d\d/2026 [\d:]+ [AP]M) \| (\S+) \| (.+) \|$', line.strip())
    if m: notes.append(m.groups())
ex = []
for f in ['archive/rab/trades/notes.csv']:
    for r in csv.DictReader(open(f)):
        ex.append((r['ticker'], r['exemplar']))
for d,t,n in notes:
    best = max(ex, key=lambda e: fuzz.ratio(n, e[1]))
    print(d, t, round(fuzz.ratio(n,best[1])), best[0][:25])
