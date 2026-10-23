"""Estimate IPS page fit with Times-metric font (Liberation Serif), Word-style double spacing.
Measures the 30 Sep draft (repo snapshot) and a version padded to the 50+500 word maxima."""
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
pdfmetrics.registerFont(TTFont('LS', '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'))
src = open('../../../../archive/rab/trades/data/ips_doc_text_2026-09-30.txt').read()
pitch = src.split('Investment Strategy Elevator Pitch')[1].split('Investment Policy Statement')[0].strip()
paras = [p.strip() for p in src.split('Investment Policy Statement\n', 1)[1].split('\n') if p.strip()]
LEAD = 27.6   # Word "Double" for TNR 12pt ~ 2 x 13.8pt
def lines(text, width_in, indent_in=0.5):
    first = simpleSplit(text, 'LS', 12, (width_in - indent_in) * 72)
    if len(first) <= 1:
        return 1
    rest = ' '.join(text.split()[len(first[0].split()):])
    return 1 + len(simpleSplit(rest, 'LS', 12, width_in * 72))
def pages(pitch_t, paras_t, paper):
    w, h = (6.5, 9.0) if paper == 'Letter' else (6.27, 9.69)
    per_page = int(h * 72 // LEAD)
    n = 1 + lines(pitch_t, w, 0) + 1 + sum(lines(p, w) for p in paras_t)   # 2 headings + text
    return n, per_page
filler = ' strategy'
for label, pt, ps in [('draft as is', pitch, paras),
                      ('padded to 50 + 500 words', pitch + filler * (50 - len(pitch.split())),
                       paras[:-1] + [paras[-1] + filler * (500 - sum(len(p.split()) for p in paras))])]:
    for paper in ('Letter', 'A4'):
        n, pp = pages(pt, ps, paper)
        print(f"{label:26s} {paper:6s}: {n} lines needed vs {2*pp} lines on two pages ({pp}/page) -> {'FITS' if n <= 2*pp else 'OVERFLOWS by %d lines' % (n - 2*pp)}")
