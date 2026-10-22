"""Format gate for an exported deliverable PDF (no AI; needs pypdf).

    python3 pdfgate.py IPS.pdf --max-pages 3 --locked locked_text.txt
    python3 pdfgate.py TNA.pdf

Checks what a machine can check against the IPS rules (IPS:110-123, `2026_WGY_Investment_Policy-FINAL.txt`):
file size <= 5 MB, not encrypted, page count, page size, fonts (expects Times), font size 12, line spacing near
double, left/right/top/bottom text margins >= 1 inch, no images, no link annotations, no "http"/"www" text, no "[AI]"
tag, and (with --locked) whether the PDF's words equal the locked text's words, which catches printed suggestions
(both wordings print) and a wrong tab. It cannot see colour or comments: a person still reads every page.
Exit 0 = every check passed; 1 = at least one FAIL.
"""

from __future__ import annotations

import argparse
import re
import statistics
import sys
from pathlib import Path

from pypdf import PdfReader

INCH = 72.0


def words(text: str) -> list[str]:
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return [w.strip(".,;:!?()[]\"'").lower() for w in re.split(r"\s+", text) if re.search(r"\w", w)]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--max-pages", type=int, help="IPS: 3 (title page + 2 strategy pages)")
    ap.add_argument("--max-mb", type=float, default=5.0)
    ap.add_argument("--locked", help="the locked text (.txt) the PDF must contain, title page lines included")
    a = ap.parse_args(argv)

    results: list[tuple[str, bool, str]] = []
    path = Path(a.pdf)
    mb = path.stat().st_size / 1_000_000
    mib = path.stat().st_size / 1_048_576
    results.append(("file size", mib <= a.max_mb and mb <= a.max_mb, f"{mb:.3f} MB ({mib:.3f} MiB), limit {a.max_mb} MB"))

    r = PdfReader(str(path))
    results.append(("not encrypted", not r.is_encrypted, "SMApply 'won't accept encrypted files'"))
    if r.is_encrypted:
        for name, passed, detail in results:
            print(f"{'PASS' if passed else 'FAIL'}  {name}: {detail}")
        print("Stop: export again from Google Docs without a password, then re-run.")
        return 1
    n = len(r.pages)
    results.append(("page count", a.max_pages is None or n <= a.max_pages, f"{n} pages" + (f", max {a.max_pages}" if a.max_pages else "")))

    fonts, sizes, images, links, xs, ys_top, ys_bot, gaps = set(), [], 0, 0, [], [], [], []
    page_w = page_h = None
    text_all = []
    for p in r.pages:
        page_w, page_h = float(p.mediabox.width), float(p.mediabox.height)
        res = p.get("/Resources") or {}
        res = res.get_object() if hasattr(res, "get_object") else res
        for _, x in (res.get("/XObject") or {}).items():
            if x.get_object().get("/Subtype") == "/Image":
                images += 1
        for an in p.get("/Annots") or []:
            o = an.get_object()
            if o.get("/Subtype") == "/Link":
                links += 1
        lines: dict[float, list[float]] = {}

        def visit(text, cm, tm, font_dict, font_size):
            if not text.strip():
                return
            scale = (tm[0] ** 2 + tm[1] ** 2) ** 0.5 * (cm[0] ** 2 + cm[1] ** 2) ** 0.5
            sizes.append(round(font_size * scale, 1))
            if font_dict is not None:
                fonts.add(str(font_dict.get("/BaseFont")))
            x = tm[4] * cm[0] + cm[4]
            y = tm[5] * cm[3] + cm[5]
            lines.setdefault(round(y, 1), []).append(x)

        t = p.extract_text(visitor_text=visit) or ""
        text_all.append(t)
        if lines:
            ys = sorted(lines, reverse=True)
            xs += [min(v) for v in lines.values()]
            ys_top.append(page_h - ys[0])
            ys_bot.append(ys[-1])
            gaps += [round(ys[i] - ys[i + 1], 1) for i in range(len(ys) - 1)]

    results.append(("page size", True, f"{page_w:.0f} x {page_h:.0f} pt ({page_w / INCH:.2f} x {page_h / INCH:.2f} in)"))
    times = [f for f in fonts if "times" in f.lower()]
    results.append(("fonts used are Times", bool(fonts) and len(times) == len(fonts), ", ".join(sorted(fonts)) or "none found"))
    body = statistics.mode(sizes) if sizes else 0
    results.append(("font size 12", abs(body - 12) < 0.3 and all(abs(s - 12) < 0.3 for s in sizes),
                    f"most common {body}; all sizes seen {sorted(set(sizes))}"))
    g = statistics.median(gaps) if gaps else 0
    results.append(("line spacing about double", g >= 22, f"median line gap {g} pt (single TNR 12 is about 13.8 pt; double about 27.6 pt)"))
    left = min(xs) if xs else 0
    results.append(("left margin >= 1 in", left >= INCH - 1, f"leftmost text at {left / INCH:.2f} in"))
    results.append(("top margin >= 1 in (baseline-based, approx.)", (min(ys_top) if ys_top else 99) >= INCH - 1,
                    f"highest baseline {min(ys_top) / INCH:.2f} in from top" if ys_top else "no text"))
    results.append(("bottom margin >= 1 in (approx.)", (min(ys_bot) if ys_bot else 99) >= INCH - 1,
                    f"lowest baseline {min(ys_bot) / INCH:.2f} in from bottom" if ys_bot else "no text"))
    results.append(("no images", images == 0, f"{images} image objects"))
    results.append(("no link annotations", links == 0, f"{links} links"))
    full = "\n".join(text_all)
    url_hits = re.findall(r"https?://\S+|www\.\S+", full)
    results.append(("no URLs in text", not url_hits, ", ".join(url_hits[:3]) or "none"))
    results.append(("no [AI] tag", "[AI]" not in full, "found" if "[AI]" in full else "none"))
    if a.locked:
        want = words(Path(a.locked).read_text(encoding="utf-8"))
        got = words(full)
        same = want == got
        detail = f"PDF {len(got)} words, locked text {len(want)} words"
        if not same:
            i = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
            detail += f"; first difference at word {i + 1}: PDF {' '.join(got[i:i + 6])!r} vs locked {' '.join(want[i:i + 6])!r}"
        results.append(("PDF words = locked text", same, detail))

    ok = True
    for name, passed, detail in results:
        ok &= passed
        print(f"{'PASS' if passed else 'FAIL'}  {name}: {detail}")
    print("Not checkable here: colour (green suggestion text), comments, right margin, the exact font name in Docs."
          " Open the PDF on a second device and read every page.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
