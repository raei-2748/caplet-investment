"""Build voice round 15's reader packs and the scorer's pack (Mon 23 Nov 2026).

Each reader reads three texts once each (writer W's piece, writer V's piece, the IPS's l.15 and l.17 as a control),
in a rotated order under neutral labels, and answers the nine depth questions after each text from that text alone.
"""
import json, re, pathlib

HERE = pathlib.Path(__file__).parent
IPS = HERE.parent.parent / "FINAL_IPS_as_submitted.txt"

def piece(path):
    s = (HERE / path).read_text()
    m = re.search(r"=== P ===\s*(.*?)\s*=== NOTES ===", s, re.S)
    return m.group(1).strip()

lines = IPS.read_text().splitlines()
control = lines[14].strip() + "\n\n" + lines[16].strip()
texts = {"W": piece("writer_W.md"), "V": piece("writer_V.md"), "C": control}

CASE = (HERE / "brief_r15_W.md").read_text()
case = re.search(r"> (Laura Gao, a writer.*?)\n\nSo a step", CASE, re.S).group(1)
case = re.sub(r"\n> ", "\n", case)

QUESTIONS = [
    "Suppose world share prices halve during 2029. What happens to the range Laura can state in 2031, and to the ten $50,000 payments?",
    "Suppose instead share prices halve during 2032, after the shares have been moved. What changes?",
    "Why not move all of her shares into Treasuries before 2031 and promise more?",
    "Why can Laura be sure of the bottom of the range from January 2028, three years before she states it?",
    "Why does she give co-sponsors a range rather than one figure, and why can't the top be known today?",
    "What, if anything, could stop the top she states being paid in December 2032?",
    "If the building ends up costing 25% more than planned, who pays the extra?",
    "Why are the shares moved in January 2031, and not on the day she meets co-sponsors or a year earlier?",
    "If interest rates fell to 1% from 2028 and stayed there, what would happen to the ten payments and to the range?",
]

ORDERS = {"R1": ["W", "V", "C"], "R2": ["V", "C", "W"], "R3": ["C", "W", "V"]}
LABELS = ["Text K", "Text M", "Text Q"]
key = {}
(HERE / "packs").mkdir(exist_ok=True)
for r, order in ORDERS.items():
    out = [f"# Reading pack {r}\n", "## What you know before you start\n", case, "\n"]
    for lab, t in zip(LABELS, order):
        key[f"{r}:{lab}"] = t
        out.append(f"\n## {lab}\n\n{texts[t]}\n")
    (HERE / "packs" / f"pack_{r}.md").write_text("\n".join(out))
(HERE / "packs" / "questions.md").write_text(
    "# The nine questions\n\n" + "\n".join(f"{i+1}. {q}" for i, q in enumerate(QUESTIONS)) + "\n")
# Scorer's texts under one neutral label per text, independent of reader labels.
SCORER = {"W": "Text 1", "V": "Text 2", "C": "Text 3"}
sc = ["# The three texts the readers read\n"]
for t in ["W", "V", "C"]:
    sc.append(f"\n## {SCORER[t]}\n\n{texts[t]}\n")
(HERE / "packs" / "scorer_texts.md").write_text("\n".join(sc))
key["scorer"] = SCORER
(HERE / "key.json").write_text(json.dumps(key, indent=1))
for t, s in texts.items():
    w = len(re.findall(r"[A-Za-z0-9$%.,'’-]+", s))
    we = len(re.findall(r"\b(we|We|our|Our|us)\b", s))
    print(t, "words", w, "we/our/us per 100", round(100 * we / w, 1))
