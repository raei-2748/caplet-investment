"""D9_ips_page_fit.py - Will a 50-word pitch plus a 500-word IPS fit on the two allowed pages?

Question (D9, IPS format compliance; serves M036): the IPS guide allows "Pages 2 and 3: Investment Strategy, 2-page
maximum" holding the 50-word pitch and the 500-word IPS, in Times New Roman 12, double-spaced, 1-inch margins
(`competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` lines 103-123, VERIFIED-REPO-FILE). Breaking a
format rule means the IPS "will not be considered for semifinal selection" (same file, lines 82-83). This script
estimates how many lines the text needs and how many the two pages hold, for the page sizes and "double" line
heights a team is likely to get.

Inputs (with status labels):
- Page rules: TNR 12 pt, double-spaced, 1-inch margins, 2 pages for pitch + IPS: VERIFIED-REPO-FILE (IPS guide).
- The guide PDFs are US Letter (612 x 792 pt): VERIFIED-REPO-FILE (pypdf mediabox of the official PDFs).
- Wharton's own illustrative sample (IPS guide p.5-6) uses a 24 pt line pitch, a blank line between the pitch and the
  "Investment Policy Statement" heading, bold headings and a tab indent at each new paragraph: VERIFIED-REPO-FILE
  (pypdf text positions, measured by this script's helper in the D9 run on 2026-09-28).
- Paper size the team will use: UNKNOWN. The guide does not name one. Australian Word/Docs installs usually default to
  A4 (ASSUMPTION), so both Letter and A4 are computed.
- "Double" line height: 24 pt (exactly 2 x 12 pt, as in Wharton's sample) and 27.6 pt (Microsoft Word "Double" for
  Times New Roman 12, which uses the font's 1.15 line-height ratio): ASSUMPTION (commonly measured Word behaviour; the
  team should check its own file, see "How to check" below).
- Font widths: Liberation Serif Regular/Bold, which is designed to be metric-compatible with Times New Roman (same
  character widths): ASSUMPTION (documented design goal of the Liberation fonts; not re-verified here).
- Proxy text for word lengths: the case's own prose (Laura_Gao_2026_Client_Profile.txt lines 36-169) and the IPS
  guide's prose: VERIFIED-REPO-FILE text used only as a sample of plain-English financial vocabulary. Real drafts with
  more long words ("contribution", "Treasury", "$50,000") will need slightly more lines; the script also reports a
  long-word stress case.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D9_ips_page_fit.py
    .venv/bin/python research/insight_v1/scripts/D9_ips_page_fit.py --draft path/to/team_ips_draft.txt
With --draft, the file's first paragraph is treated as the pitch and the rest (paragraphs separated by blank lines) as
the IPS; the script then lays out the team's own words instead of the proxy text. The draft stays on the team's machine;
do not commit it.

How to check for real (the only test that counts): export the final PDF from the same program the team submits from
and confirm the text ends on page 3 (title page = page 1). Do not trust this estimate over the actual PDF.
"""
import argparse
import re
import sys

import warnings

from matplotlib import ft2font

warnings.filterwarnings("ignore")
NO_SCALE = getattr(getattr(ft2font, "LoadFlags", None), "NO_SCALE", None) or ft2font.LOAD_NO_SCALE

REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
PT = 12.0
MARGIN = 72.0
PAGES = {"US Letter": (612.0, 792.0), "A4": (595.28, 841.89)}
LEADS = {"24.0 pt (Wharton sample)": 24.0, "27.6 pt (Word 'Double', TNR 12)": 27.6}
INDENT = 36.0  # 0.5 inch first-line indent (the sample uses a tab at each new paragraph)


def make_width(path):
    f = ft2font.FT2Font(path)
    upem = f.units_per_EM
    adv = {}

    def char_adv(ch):
        if ch not in adv:
            try:
                adv[ch] = f.load_char(ord(ch), flags=NO_SCALE).horiAdvance
            except RuntimeError:
                adv[ch] = f.load_char(ord("n"), flags=NO_SCALE).horiAdvance  # fallback width for a missing glyph
        return adv[ch]

    def width(s, size=PT):
        return sum(char_adv(c) for c in s) * size / upem

    return width


wreg = make_width(REG)
wbold = make_width(BOLD)


def lines_for(words, avail, first_indent=0.0, width=wreg):
    """Greedy line fill, like a word processor with left alignment (no hyphenation)."""
    if not words:
        return 0
    space = width(" ")
    n, cur, first = 1, 0.0, True
    for w in words:
        ww = width(w)
        limit = avail - (first_indent if first else 0.0)
        if cur == 0.0:
            cur = ww
        elif cur + space + ww <= limit:
            cur += space + ww
        else:
            n += 1
            first = False
            cur = ww
    return n


def proxy_words():
    txt = open("competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt").read().splitlines()[35:169]
    txt += open("competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt").read().splitlines()[2:78]
    words = []
    for line in txt:
        if line.startswith("=====") or "Investment Competition Guide" in line or "Investment Policy Statement (IPS)" in line:
            continue
        words += [w for w in re.split(r"\s+", line.replace("­", "")) if w and w != "•" and w != "–"]
    return words


def take(words, n, start=0):
    out = []
    i = start
    while len(out) < n:
        out.append(words[i % len(words)])
        i += 1
    return out, i


def layout(pitch_paras, ips_paras, page, lead):
    w, h = PAGES[page]
    avail_w = w - 2 * MARGIN
    lines_per_page = int((h - 2 * MARGIN) // lead)
    need = 1  # heading "Investment Strategy Elevator Pitch"
    need += sum(lines_for(p, avail_w, 0.0) for p in pitch_paras)
    need += 1  # blank line, as in Wharton's sample
    need += 1  # heading "Investment Policy Statement"
    need += sum(lines_for(p, avail_w, INDENT) for p in ips_paras)
    return need, 2 * lines_per_page, lines_per_page


def words_per_line(words, page):
    w, _ = PAGES[page]
    avail = w - 2 * MARGIN
    n = lines_for(words, avail)
    return len(words) / n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", help="team draft: first paragraph = pitch, remaining paragraphs = IPS")
    a = ap.parse_args()
    words = proxy_words()
    print(f"Proxy text: {len(words)} words from the case and IPS guide (VERIFIED-REPO-FILE, used only for word lengths).")
    for page in PAGES:
        print(f"  average words per full line on {page}: {words_per_line(words, page):.1f}")
    longw = [x for x in words if len(x) >= 7]
    print(f"  stress case (only words of 7+ characters) on US Letter: {words_per_line(longw, 'US Letter'):.1f} words/line")
    print()

    if a.draft:
        paras = [re.split(r"\s+", p.strip()) for p in re.split(r"\n\s*\n", open(a.draft).read()) if p.strip()]
        pitch, ips = paras[:1], paras[1:]
        print(f"DRAFT: pitch {sum(map(len, pitch))} words; IPS {sum(map(len, ips))} words in {len(ips)} paragraphs")
        for page in PAGES:
            for lname, lead in LEADS.items():
                need, have, lpp = layout(pitch, ips, page, lead)
                flag = "FITS" if need <= have else "OVERFLOWS TO PAGE 4: NON-COMPLIANT"
                print(f"  {page:9s} {lname:32s} needs {need:2d} of {have:2d} lines ({lpp}/page): {flag}")
        return

    print("Full budget: 50-word pitch + 500-word IPS, heading lines and one blank line as in Wharton's sample.")
    print("Lines needed vs lines available on pages 2-3 (1-inch margins, TNR-metric font, 12 pt):")
    print(f"{'page':10s}{'line height':34s}{'IPS paras':>10s}{'needed':>8s}{'avail':>7s}  result")
    for page in PAGES:
        for lname, lead in LEADS.items():
            for k in (4, 6, 8):
                pitch, pos = take(words, 50)
                per = [500 // k + (1 if i < 500 % k else 0) for i in range(k)]
                ips = []
                for n in per:
                    para, pos = take(words, n, pos)
                    ips.append(para)
                need, have, lpp = layout([pitch], ips, page, lead)
                res = "fits, spare %d" % (have - need) if need <= have else "OVERFLOW by %d line(s)" % (need - have)
                print(f"{page:10s}{lname:34s}{k:>10d}{need:>8d}{have:>7d}  {res}")
    print()
    print("Largest IPS word count that still fits (50-word pitch, 6 IPS paragraphs), proxy vocabulary:")
    for page in PAGES:
        for lname, lead in LEADS.items():
            best = 0
            for total in range(300, 701, 5):
                pitch, pos = take(words, 50)
                k = 6
                per = [total // k + (1 if i < total % k else 0) for i in range(k)]
                ips = []
                for n in per:
                    para, pos = take(words, n, pos)
                    ips.append(para)
                need, have, _ = layout([pitch], ips, page, lead)
                if need <= have:
                    best = total
            print(f"  {page:9s} {lname:32s} about {best} IPS words")
    print()
    print("Reading: numbers are estimates (ASSUMPTION-based). The binding test is the exported PDF.")


if __name__ == "__main__":
    sys.exit(main())
