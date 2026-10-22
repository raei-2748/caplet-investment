"""Provenance check: shared 5-word runs between a student's final text and AI files. No AI, standard library only.

    python3 provenance.py final_text.txt --ai AI_FOLDER_OR_FILE [--ai ...] [--allow official_quotes.txt ...] [-n 5]

What it does
- Splits every file into words (lower case; curly quotes made straight; dashes treated as spaces; punctuation at
  the ends of a word removed; "co-sponsors" stays one word).
- Finds every run of n words (default 5) in the final text that also appears in any AI file, merges overlapping
  runs into spans, and prints each span with the AI file and line where it first appears.
- Runs that also appear in an --allow file are reported as ALLOWED (use it for text a rule makes you quote exactly:
  the WInS trade note, TNA:44, or an official heading). They do not fail the check.
- Exit code 0 = no disallowed shared run; 1 = at least one (the author rewrites it from their own notes, or cuts it).

AI files can be .txt, .md, .csv, .tsv, .html or .docx (Word text is read from word/document.xml). Folders are
searched recursively. Convert PDFs or Google Docs to .txt first (Docs: File > Download > Plain text).

It is a tripwire, not a verdict: a shared run can be a proper name ("iShares iBonds Dec 2032 Term Treasury ETF") or a
fact phrase. A person decides each one and logs the decision. A clean result does not prove authorship either.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

TEXT_EXT = {".txt", ".md", ".csv", ".tsv", ".html", ".htm"}


def read_any(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", "replace")
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    return path.read_text(encoding="utf-8", errors="replace")


def tokens_with_lines(text: str) -> list[tuple[str, int]]:
    text = (text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
            .replace("–", " ").replace("—", " ").replace(" ", " "))
    out = []
    for ln, line in enumerate(text.split("\n"), start=1):
        for raw in line.split():
            w = raw.strip(".,;:!?()[]{}\"'*_`|>#").lower()
            if re.search(r"\w", w):
                out.append((w, ln))
    return out


def ngrams(toks: list[tuple[str, int]], n: int) -> dict[tuple[str, ...], int]:
    """n-gram -> line number of its first occurrence."""
    g: dict[tuple[str, ...], int] = {}
    words = [t for t, _ in toks]
    for i in range(len(words) - n + 1):
        g.setdefault(tuple(words[i:i + n]), toks[i][1])
    return g


def collect(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        q = Path(p)
        if q.is_dir():
            files += sorted(f for f in q.rglob("*") if f.is_file() and (f.suffix.lower() in TEXT_EXT or f.suffix.lower() == ".docx"))
        elif q.is_file():
            files.append(q)
        else:
            print(f"warning: not found: {p}", file=sys.stderr)
    return files


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text", help="the final text to check (.txt)")
    ap.add_argument("--ai", action="append", required=True, help="AI file or folder (repeat)")
    ap.add_argument("--allow", action="append", default=[], help="file of text that must be quoted exactly (repeat)")
    ap.add_argument("-n", type=int, default=5, help="run length in words (default 5)")
    args = ap.parse_args(argv)

    final = tokens_with_lines(read_any(Path(args.text)))
    words = [t for t, _ in final]
    n = args.n
    ai_index: dict[tuple[str, ...], tuple[str, int]] = {}
    ai_files = collect(args.ai)
    for f in ai_files:
        for g, ln in ngrams(tokens_with_lines(read_any(f)), n).items():
            ai_index.setdefault(g, (str(f), ln))
    allowed: set[tuple[str, ...]] = set()
    for f in collect(args.allow):
        allowed |= set(ngrams(tokens_with_lines(read_any(f)), n))

    hit = [False] * len(words)       # covered by any AI run
    bad = [False] * len(words)       # covered by an AI run that is not allowed
    first_src: dict[int, tuple[str, int]] = {}
    for i in range(len(words) - n + 1):
        g = tuple(words[i:i + n])
        if g in ai_index:
            first_src.setdefault(i, ai_index[g])
            for j in range(i, i + n):
                hit[j] = True
                if g not in allowed:
                    bad[j] = True

    # merge covered positions into spans
    spans = []
    i = 0
    while i < len(words):
        if hit[i]:
            j = i
            while j + 1 < len(words) and hit[j + 1]:
                j += 1
            src = next((first_src[k] for k in range(i, j + 1) if k in first_src), ("?", 0))
            spans.append((i, j, any(bad[i:j + 1]), src))
            i = j + 1
        else:
            i += 1

    total = max(1, len(words))
    print(f"final text: {args.text} ({len(words)} words); AI files read: {len(ai_files)}; run length n={n}")
    print(f"coverage by AI runs: {sum(hit) / total:.0%} of words; not allowed: {sum(bad) / total:.0%}")
    for i, j, is_bad, (src, ln) in spans:
        tag = "FLAG   " if is_bad else "ALLOWED"
        print(f"  {tag} words {i + 1}-{j + 1} (line {final[i][1]}): \"{' '.join(words[i:j + 1])}\"  <- {src}:{ln}")
    nbad = sum(1 for s in spans if s[2])
    print(f"result: {'CLEAN' if nbad == 0 else f'{nbad} flagged span(s): the author rewrites each from their own notes, or cuts it'}")
    return 0 if nbad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
