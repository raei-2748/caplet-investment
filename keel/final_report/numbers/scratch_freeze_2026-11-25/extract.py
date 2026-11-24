"""Scratch for the 25 Nov freeze table: list every numeric token in ARGUMENT_TREE.md and
voice/FACTS_PLAIN.md with line numbers, and where the same token appears in NUMBERS.md.
Read-only; prints to stdout."""
import re, sys, collections, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
files = {"AT": ROOT / "ARGUMENT_TREE.md", "FP": ROOT / "voice" / "FACTS_PLAIN.md"}
num = (ROOT / "NUMBERS.md").read_text().split("\n")

TOK = re.compile(r"(?:NT)?\$[0-9][0-9,]*(?:\.[0-9]+)?(?:\s?(?:million|m|bn))?|-?[0-9][0-9,]*(?:\.[0-9]+)?%|[0-9]+(?:\.[0-9]+)? (?:in|of) [0-9,]+|[0-9]+(?:\.[0-9]+)? points?|[0-9.]+ times")
occ = collections.OrderedDict()
for tag, p in files.items():
    for i, line in enumerate(p.read_text().split("\n"), 1):
        for m in TOK.finditer(line):
            t = m.group(0).strip()
            occ.setdefault(t, []).append(f"{tag}{i}")

def where(t):
    key = t.replace("NT$", "")
    hits = [str(i) for i, l in enumerate(num, 1) if key in l]
    return hits

for t, locs in occ.items():
    h = where(t)
    print(f"{t}\t{','.join(locs)}\tNUMBERS:{len(h)}\t{','.join(h[:12])}")
