"""Format checks for Caplet deliverable text. No AI, standard library only.

    python3 keel/office/tools/textcheck.py draft.txt --limit 100
    python3 keel/office/tools/textcheck.py my_paste.txt --compare wins_note.txt
    python3 keel/office/tools/textcheck.py - < draft.txt

Reports two word counts (the stricter one is what to keep under the limit), the character count, every non-ASCII
character (Google Docs turns straight quotes into curly ones; WInS notes are plain ASCII), words the team agreed
not to use for our plan, and an exact-match check against a second file.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# From competition/COMPETITION.md section 7 and the 16 Oct review (items 8, 12): overclaims for a plan that is not riskless.
BANNED = [
    "guaranteed", "guarantee", "risk-free", "riskless", "locked", "secured", "promised", "cannot miss",
    "never below", "certain to", "immunisation", "immunization", "cppi",
]


def words_by_spaces(text: str) -> int:
    """Count like a simple word counter: runs of non-whitespace."""
    return len(text.split())


def words_strict(text: str) -> int:
    """A stricter count: also splits on hyphens, slashes and dashes ("2033-2042" is two words)."""
    return len([t for t in re.split(r"[\s\-/–—]+", text) if re.search(r"\w", t)])


def non_ascii(text: str) -> list[tuple[int, str, str]]:
    """(position, character, Unicode name) for every non-ASCII character."""
    return [(i, ch, unicodedata.name(ch, "UNKNOWN")) for i, ch in enumerate(text) if ord(ch) > 127]


def banned_hits(text: str) -> list[tuple[str, int]]:
    """(banned phrase, position) for each match, case-insensitive, whole words."""
    hits = []
    for phrase in BANNED:
        for m in re.finditer(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, flags=re.IGNORECASE):
            hits.append((phrase, m.start()))
    return sorted(hits, key=lambda h: h[1])


def first_difference(a: str, b: str) -> int | None:
    """Index of the first differing character, or None if the strings are identical."""
    if a == b:
        return None
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    return min(len(a), len(b))


def read(path: str) -> str:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return text.rstrip("\n")  # a trailing newline from the editor is not part of the text


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="text file to check, or - for stdin")
    ap.add_argument("--limit", type=int, help="word limit (e.g. 100 for a TNA reflection, 500 for the IPS)")
    ap.add_argument("--chars", type=int, help="character limit (e.g. 300 for a WInS trade note)")
    ap.add_argument("--compare", help="file that must match exactly (e.g. the note copied from WInS)")
    args = ap.parse_args(argv)

    text = read(args.file)
    ok = True
    by_spaces, strict = words_by_spaces(text), words_strict(text)
    print(f"words: {by_spaces} by spaces, {strict} strict")
    print(f"characters: {len(text)}")
    if args.limit is not None:
        worst = max(by_spaces, strict)
        status = "PASS" if worst <= args.limit else "FAIL"
        ok &= status == "PASS"
        print(f"word limit {args.limit}: {status} (stricter count {worst}, margin {args.limit - worst})")
    if args.chars is not None:
        status = "PASS" if len(text) <= args.chars else "FAIL"
        ok &= status == "PASS"
        print(f"character limit {args.chars}: {status}")

    odd = non_ascii(text)
    print(f"non-ASCII characters: {len(odd)}")
    for pos, ch, name in odd[:20]:
        print(f"  at {pos}: {ch!r} {name}")

    hits = banned_hits(text)
    print(f"overclaim words: {len(hits)}")
    for phrase, pos in hits:
        print(f"  at {pos}: {text[max(0, pos - 20):pos + len(phrase) + 20]!r}")

    if args.compare:
        other = read(args.compare)
        diff = first_difference(text, other)
        if diff is None:
            print("exact match: YES")
        else:
            ok = False
            print(f"exact match: NO, first difference at character {diff}")
            print(f"  this file : {text[max(0, diff - 15):diff + 15]!r}")
            print(f"  compare to: {other[max(0, diff - 15):diff + 15]!r}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
