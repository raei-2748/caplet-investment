"""Format checks for Caplet deliverable text. No AI, standard library only.

    python3 keel/office/tools/textcheck.py draft.txt --limit 100
    python3 keel/office/tools/textcheck.py my_paste.txt --compare wins_note.txt
    python3 keel/office/tools/textcheck.py - < draft.txt
    python3 keel/office/tools/textcheck.py draft.txt --limit 500 --voice

Reports two word counts (the stricter one is what to keep under the limit), the character count, every non-ASCII
character (Google Docs turns straight quotes into curly ones; WInS notes are plain ASCII), words the team agreed
not to use for our plan, and an exact-match check against a second file. --voice adds a rhythm-and-habit meter built
from the rewrite's voice study (`keel/ips_rewrite/research/R03_voice_study.md`): a smoke alarm for prose that reads as
machine-made, never a score to write towards.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# From competition/COMPETITION.md section 7 and the 16 Oct review (items 8, 12): overclaims for a plan that is not riskless.
BANNED = [
    "guaranteed", "guarantee", "guarantees", "risk-free", "riskless", "locked", "secured", "secures", "promised",
    "cannot miss",
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


# R03 voice study (26 Oct): habits that made the TNA read as AI. Lists are short on purpose; a hit is a question, not a fault.
CONNECTIVES = [
    "furthermore", "moreover", "additionally", "notably", "ultimately", "crucially", "importantly", "in other words",
    "in essence", "in summary", "in conclusion", "that said", "it is worth", "which means", "meaning",
]
ABSTRACT = [
    "certainty", "uncertainty", "flexibility", "reliability", "stability", "resilience", "transparency", "liquidity",
    "alignment", "framework", "robust", "robustness", "discipline", "exposure", "objective", "objectives",
]
CONTRAST = r",\s+not\s+\w+|\brather than\b|\bas opposed to\b|\bnot merely\b|\bnot just\b"
TRICOLON = r"\b[\w$%.-]+,\s+[\w$%.-]+(?:\s+[\w$%.-]+)?,?\s+and\s+[\w$%.-]+"


def sentences(text: str) -> list[str]:
    """Split on . ! ? followed by a space and a capital, a digit, a quote or a bracket ("$10.5k" stays whole)."""
    flat = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])[\"')\u2019\u201d]?\s+(?=[A-Z0-9$\"'(\u2018\u201c\[])", flat)
    return [p for p in parts if re.search(r"\w", p)]


def voice(text: str) -> dict:
    """Rhythm and habit counts; see R03. Lengths use words_strict so numbers match the limit check."""
    sents = sentences(text)
    lens = [words_strict(s) for s in sents] or [0]
    n = len(lens)
    mean = sum(lens) / n
    sd = (sum((x - mean) ** 2 for x in lens) / n) ** 0.5
    paras = [p for p in re.split(r"\n\s*\n|\n", text) if p.strip()]
    one_line = sum(1 for p in paras if len(sentences(p)) == 1)
    low = text.lower()

    def hits(words):
        return [w for w in words for _ in re.finditer(rf"(?<!\w){re.escape(w)}(?!\w)", low)]

    return {
        "sentences": n, "mean": mean, "sd": sd, "cv": sd / mean if mean else 0.0,
        "middle_band": sum(1 for x in lens if 15 <= x <= 28) / n, "blunt": sum(1 for x in lens if x <= 6),
        "longest": max(lens), "paragraphs": len(paras), "one_line_paragraphs": one_line,
        "contrasts": re.findall(CONTRAST, text, flags=re.IGNORECASE), "tricolons": re.findall(TRICOLON, text),
        "connectives": hits(CONNECTIVES), "abstract": hits(ABSTRACT),
        "thesis_first": bool(re.match(r"(this|our|the) (policy|ips|strategy|plan|goal|objective)\b", sents[0].lower()))
        if sents else False,
        "turns": [s for s in sents if re.match(r"(but|yet|and yet|still|alas)\b", s.lower())],
        "openers": sorted({w: sum(1 for s in sents if s.split()[0].strip("\"'(").lower() == w)
                           for w in {s.split()[0].strip("\"'(").lower() for s in sents}}.items(), key=lambda kv: -kv[1])[:3],
    }


def voice_flags(v: dict, words: int) -> list[str]:
    """Only habits that separated the locked TNA reflections (detectors: 100% AI) from a human control (Orwell, 1946).
    Rhythm (spread, blunt lines, the 15-28 band) did NOT separate them, so it is printed as information, never flagged.
    Calibration: keel/office/outbox/2026-10-26_writing-room_voice-meter.md."""
    per100 = 100 / max(words, 1)
    flags = []
    if len(v["contrasts"]) * per100 > 0.5:
        flags.append(f"'X, not Y' / 'rather than' {len(v['contrasts'])} times: use it once, then concede and turn")
    if len(v["tricolons"]) * per100 > 0.6:
        flags.append(f"lists of three {len(v['tricolons'])} times")
    if len(v["connectives"]) * per100 > 0.6:
        flags.append(f"stock connectives: {', '.join(v['connectives'])}")
    if len(v["abstract"]) * per100 > 1.5:
        flags.append(f"abstract nouns {len(v['abstract'])} ({len(v['abstract']) * per100:.1f} per 100 words): "
                     f"{', '.join(sorted(set(v['abstract'])))}; name the bond, the cheque or the meeting instead")
    if v["thesis_first"]:
        flags.append("opens on a thesis ('This policy...'): open on a fact, a number or the other side")
    if v["sentences"] >= 6 and not v["turns"]:
        flags.append("no turn: no sentence opens with But, Yet or Still (no sceptic is voiced and answered)")
    top = v["openers"][0] if v["openers"] else ("", 0)
    if v["sentences"] >= 6 and top[1] / v["sentences"] > 0.3:
        flags.append(f"{top[1]} of {v['sentences']} sentences open with '{top[0]}'")
    return flags


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
    ap.add_argument("--voice", action="store_true", help="add the rhythm-and-habit meter (R03 voice study)")
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
    if args.voice:
        v = voice(text)
        print(f"voice: {v['sentences']} sentences, mean {v['mean']:.1f} words, spread {v['cv']:.0%}, "
              f"{v['blunt']} blunt (<=6), longest {v['longest']}; {v['paragraphs']} paragraphs, "
              f"{v['one_line_paragraphs']} of one sentence")
        flags = voice_flags(v, strict)
        print(f"voice flags: {len(flags)} (a smoke alarm, not a score; never a reason to soften)")
        for f in flags:
            print(f"  - {f}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
