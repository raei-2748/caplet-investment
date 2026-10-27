"""Voice fingerprint: measures how a piece of prose moves, not what it says.

AI-generated (Claude Code), 27 Oct 2026, for the voice study in keel/voice/. Ahaan's 24 Oct note says Keel's prose
"STILL sounded AI ... aspects of AI writing transcend the kinds of things which you can ban with a neat list". Word
lists can't see rhythm. This script counts the things a reader feels but a banned-word list misses: how much sentence
length swings, how often a long build drops into a short punch, how many asides, numerals and dashes, how often the
"X, not Y" antithesis repeats, and how much of the text is abstract nouns.

Usage:
    python3 keel/voice/fingerprint.py LABEL=PATH [LABEL=PATH ...]
    PATH may be a .txt or .md file. For keel/BIBLE.md only the quoted books are read (lines starting "> ").
    Markdown headings, tables, code, blockquotes and list bullets are dropped; the rest is read as prose. In an
    exercise file everything from a "## Critique" heading down is ignored.

Ahaan's essays are a PRIVATE project file (/mnt/project-files/voice/ahaan_essays_2026-10-24.txt). Never copy their
text into the repo: this script only prints numbers.
"""
import re
import statistics as st
import sys
from pathlib import Path

ABBREV = re.compile(r"\b(e\.g|i\.e|U\.S|vs|etc|Mr|Dr|St|approx|no)\.", re.I)
NOMINAL = re.compile(r"\b\w{4,}(tion|tions|ity|ities|ness|ment|ments|ance|ence)\b", re.I)
ANTITHESIS = re.compile(r",\s+not\s+\w|\bnot\s+(?:just\s+|only\s+|merely\s+)?[\w' ]{1,40},\s+but\b|\brather than\b", re.I)
WE = re.compile(r"\b(we|our|us)\b", re.I)
NUMERAL = re.compile(r"(?<![\w.])[$]?\d[\d,.]*%?")
ACRONYM = re.compile(r"\b[A-Z]{2,}[A-Z0-9-]*\b")


def prose(path):
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    if path.endswith("BIBLE.md"):
        lines = [l[2:] for l in lines if l.startswith("> ")]
    keep, code = [], False
    for l in lines:
        s = l.strip()
        if s.startswith("## Critique"):
            break
        if s.startswith(">"):
            keep.append("")
            continue
        if s.startswith("```"):
            code = not code
            continue
        if code or not s or s.startswith(("#", "|", "===", "---", "STAMP")):
            keep.append("")
            continue
        s = re.sub(r"^([-*]|\d+\.)\s+", "", s)
        s = re.sub(r"[*_`]", "", s)
        keep.append(s)
    paras = [p.strip() for p in "\n".join(keep).split("\n\n")]
    return [re.sub(r"\s*\n\s*", " ", p) for p in paras if p.strip()]


def sentences(paras):
    out = []
    for p in paras:
        p2 = ABBREV.sub(lambda m: m.group(0).replace(".", "§"), p)
        for s in re.split(r"(?<=[.!?])[\"')\]]*\s+(?=[\"'(\[]?[A-Z0-9$])", p2):
            s = s.replace("§", ".").strip()
            if len(s.split()) >= 1:
                out.append(s)
    return out


def words(s):
    return re.findall(r"[A-Za-z0-9$%'’.,-]*[A-Za-z0-9]", s)


def fingerprint(path):
    paras = prose(path)
    sents = sentences(paras)
    lens = [len(words(s)) for s in sents]
    text = " ".join(paras)
    n = sum(lens) or 1
    per100 = lambda c: round(100 * c / n, 2)
    per1k = lambda c: round(1000 * c / n, 1)
    drops = sum(1 for a, b in zip(lens, lens[1:]) if a >= 20 and b <= 6)
    plen = [len(words(p)) for p in paras]
    return {
        "words": n,
        "sentences": len(sents),
        "mean_len": round(st.mean(lens), 1) if lens else 0,
        "sd_len": round(st.pstdev(lens), 1) if lens else 0,
        "swing (cv)": round(st.pstdev(lens) / st.mean(lens), 2) if lens else 0,
        "short<=6 %": round(100 * sum(l <= 6 for l in lens) / len(lens)) if lens else 0,
        "long>=30 %": round(100 * sum(l >= 30 for l in lens) / len(lens)) if lens else 0,
        "punch drops /1k": per1k(drops),
        "one-line paras %": round(100 * sum(l <= 12 for l in plen) / len(plen)) if plen else 0,
        "dashes /100": per100(text.count(" – ") + text.count("—") + text.count(" - ")),
        "brackets /100": per100(text.count("(")),
        "numerals /100": per100(len(NUMERAL.findall(text))),
        "we-our /100": per100(len(WE.findall(text))),
        "questions /1k": per1k(text.count("?")),
        "commas /sentence": round(text.count(",") / len(sents), 2) if sents else 0,
        "But/And/Yet starts %": round(100 * sum(bool(re.match(r"(But|And|Yet|So|Alas|Still)\b", s)) for s in sents) / len(sents)) if sents else 0,
        "X-not-Y /1k": per1k(len(ANTITHESIS.findall(text))),
        "abstract nouns /100": per100(len(NOMINAL.findall(text))),
        "ACRONYMS /100": per100(len(ACRONYM.findall(text))),
    }


def main(args):
    rows = []
    for a in args:
        label, _, path = a.partition("=")
        rows.append((label, fingerprint(path)))
    keys = list(rows[0][1].keys())
    w = max(len(k) for k in keys) + 2
    print("metric".ljust(w) + "".join(l[:14].rjust(15) for l, _ in rows))
    for k in keys:
        print(k.ljust(w) + "".join(str(r[k]).rjust(15) for _, r in rows))


if __name__ == "__main__":
    main(sys.argv[1:])
