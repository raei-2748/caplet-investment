"""D10_ips_page_fit.py - does a 50-word pitch + 500-word IPS fit on the two allowed pages? (question M013, word budget)

Agent D10 (Compliance Officer), insight_v1 run, 2026-09-28.

What it does (plain English):
The IPS rules allow pages 2-3 only ("2-page maximum") for a 50-word elevator pitch plus a 500-word IPS in Times New
Roman 12, double-spaced, 1-inch margins; a submission that breaks these "will not be considered for semifinal
selection". This script estimates how many lines 550 words of Wharton-register English take at those settings, on
U.S. Letter and on A4 paper (an Australian Word default), with and without Word's default 8pt space after each
paragraph, and how many words of slack remain. It also turns the slack into a governance word budget.

Method: word widths are measured with Liberation Serif Regular (metrically compatible with Times New Roman: same
character widths). Text is built by sampling real word sequences from Wharton's own official guides (never drafted
prose), wrapped greedily into the text width, split into paragraphs, with the two headings on their own lines.
Line height for "double" spacing = 2 x the font's single line height (usWinAscent + usWinDescent), which is how Word
sets it.

Inputs and status labels:
- Format rules: `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` L103-123, VERIFIED-REPO-FILE.
- Liberation Serif metric compatibility with Times New Roman: Wikipedia "Liberation fonts" infobox, read 2026-09-28
  (secondary source; used as an ASSUMPTION).
- Font file: /usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf (system file).
- Word-length sample: official guides in `competition/official/2026_27/` (VERIFIED-REPO-FILE), lorem ipsum removed.
- Paragraph counts (pitch 1; IPS 5, 7 or 9 paragraphs), headings, 8pt space-after and 0.5in first-line indent
  variants: ASSUMPTION (team layout choices).
- Page sizes: Letter 8.5x11 in; A4 8.27x11.69 in.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D10_ips_page_fit.py
Results are recorded in research/insight_v1/phase_D/D10_compliance.md (M013).
"""
import random
import re

from fontTools.ttLib import TTFont

FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SIZE = 12.0
SRC = [
    "competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt",
    "competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt",
    "competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt",
    "competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt",
]

f = TTFont(FONT)
upm = f["head"].unitsPerEm
cmap = f.getBestCmap()
hmtx = f["hmtx"]
os2 = f["OS/2"]
single = (os2.usWinAscent + os2.usWinDescent) / upm * SIZE
LINE = 2 * single  # "double"


def width(s):
    return sum(hmtx[cmap.get(ord(ch), cmap[ord("?")])][0] for ch in s) / upm * SIZE


SPACE = width(" ")

words = []
for p in SRC:
    t = open(p, encoding="utf-8").read()
    t = re.sub(r"=====.*?=====", " ", t)
    t = t[: t.find("Lorem")] + " " if "Lorem" in t else t
    words += [w for w in t.split() if re.search(r"[A-Za-z]", w) and "ipsum" not in w]


def wrap(par_words, text_w, indent):
    lines, cur, first = 1, 0.0, True
    avail = text_w - indent
    for w in par_words:
        ww = width(w)
        add = ww if cur == 0 else SPACE + ww
        if cur + add <= avail:
            cur += add
        else:
            lines += 1
            cur = ww
            avail = text_w
    return lines


def layout(page, n_par, space_after_pt, indent_in, rng):
    pw, ph = page
    text_w, text_h = (pw - 2) * 72, (ph - 2) * 72
    start = rng.randrange(0, len(words) - 600)
    seq = words[start:start + 550]
    pitch, ips = seq[:50], seq[50:]
    cuts = sorted(rng.sample(range(40, 460), n_par - 1))
    pars = [ips[a:b] for a, b in zip([0] + cuts, cuts + [500])]
    height = 0.0
    height += LINE  # heading "Investment Strategy Elevator Pitch"
    height += wrap(pitch, text_w, indent_in * 72) * LINE + space_after_pt
    height += LINE  # heading "Investment Policy Statement"
    for par in pars:
        height += wrap(par, text_w, indent_in * 72) * LINE + space_after_pt
    lines_per_page = int(text_h // LINE)
    return height, 2 * text_h, lines_per_page


if __name__ == "__main__":
    rng = random.Random(20260928)
    print(f"Single line {single:.2f}pt; double {LINE:.2f}pt; average word width "
          f"{sum(width(w) for w in words) / len(words):.1f}pt + space {SPACE:.1f}pt; sample {len(words)} words")
    pages = {"Letter": (8.5, 11.0), "A4": (8.27, 11.69)}
    for name, page in pages.items():
        for n_par in (5, 7, 9):
            for sa, ind in ((0.0, 0.0), (8.0, 0.0), (0.0, 0.5), (8.0, 0.5)):
                used, cap, lpp = [], None, None
                for _ in range(400):
                    h, cap, lpp = layout(page, n_par, sa, ind, rng)
                    used.append(h)
                used.sort()
                p50, p95 = used[len(used) // 2], used[int(0.95 * len(used))]
                # words of slack at the median: remaining height -> lines -> words (~words per full line)
                text_w = (page[0] - 2) * 72
                wpl = text_w / (sum(width(w) for w in words) / len(words) + SPACE)
                slack_words = (cap - p50) / LINE * wpl
                print(f"{name:6s} IPS paras {n_par} space-after {sa:3.0f}pt indent {ind:.1f}in: "
                      f"{lpp} lines/page; uses {p50 / cap * 100:5.1f}% (p95 {p95 / cap * 100:5.1f}%) of 2 pages; "
                      f"slack ~{slack_words:4.0f} words; fits at p95: {'YES' if p95 <= cap else 'NO'}")
