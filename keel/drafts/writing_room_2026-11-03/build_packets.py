"""Build the four stranger packets for huddle H-025 (Writing Room, Tue 3 Nov 2026).

Each packet = persona line + (optional) the submitted Trading Notes + pitch + FIRST TEXT + Part 1 questions +
SECOND TEXT + the changed sentences as shuffled pairs + the sentence block. Seeded, so a re-run gives the same packets.
Usage: python3 build_packets.py <W3 file> <lock variants file>
(Keel is a simulated team, AI-written.)
"""
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HUD = ROOT / "keel/huddles/2026-11-03_words-a-stranger-can-say-back"
OUT = HUD / "research/packets"

A = (HUD / "arms/A_V54.txt").read_text().strip()
W = Path(sys.argv[1]).read_text().strip()
LOCKS = [l.strip() for l in Path(sys.argv[2]).read_text().splitlines() if l.strip()]
PITCH = (HUD / "arms/pitch_V54.txt").read_text().strip()
TNA = (HERE / "tna_as_submitted.txt").read_text().strip()
SHEET = (HERE / "stranger_sheet.md").read_text()


def sentences(text):
    out = []
    for para in text.split("\n\n"):
        out += [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", para.strip()) if s.strip()]
    return out


def changed_pairs(a, w):
    sa, sw = sentences(a), sentences(w)
    only_a = [s for s in sa if s not in sw]
    only_w = [s for s in sw if s not in sa]
    # pair by paragraph position: each changed V54 sentence with the W3 sentences of the same paragraph
    pa, pw = a.split("\n\n"), w.split("\n\n")
    pairs = []
    for i, (x, y) in enumerate(zip(pa, pw)):
        xa = [s for s in sentences(x) if s in only_a]
        yw = [s for s in sentences(y) if s in only_w]
        if xa or yw:
            pairs.append((" ".join(xa) or "(nothing)", " ".join(yw) or "(nothing)"))
    return pairs


PERSONAS = {
    "S1": ("a 15-year-old Year 10 student in Brisbane who has never invested or owned a share or a bond", "A", False),
    "S2": ("a 38-year-old nurse in Perth whose only investment is a work super fund she has never looked into", "W", True),
    "S3": ("a 67-year-old retired carpenter in Hobart who keeps his savings in a bank term deposit and has never bought a share or a bond", "W", False),
    "S4": ("a 24-year-old cafe manager in Adelaide who has a share-trading app with $300 in it and has never bought a bond", "A", True),
}

PART1 = SHEET.split("## Part 1")[1].split("## Part 2")[0]
PART1 = "## Part 1" + PART1
P2HEAD = "## Part 2, the SECOND TEXT\n10. Read it once. List every sentence you didn't understand the first time.\n11. For each pair below (the places the two texts differ; which is \"1\" and which is \"2\" is shuffled), which one did you understand on first read, \"1\", \"2\" or \"same\", and why in a few words?\n"
P3HEAD = "## Part 3, the sentence block\n12. Each version of the same sentence below: say it back in one line. Do the bonds still pay their interest? Does money already reinvested stop earning? Which version would you act on with the least guessing?\n"
P3B = "13. Two endings for the last paragraph: (x) \"...paying out one rung per cheque and returning to Laura what the cheques don't need.\" (y) \"...paying out one rung per cheque and returning to Laura what no remaining cheque needs.\" In 2036, what money goes back to Laura under each? Which is clearer?\n"
RULES = "Rules: answer only from the texts; don't use finance knowledge the person you play wouldn't have; never look anything up or open any file; keep each answer short; number your answers 1-13."


def build(name, seed):
    who, first, tna = PERSONAS[name]
    rng = random.Random(seed)
    t1, t2 = (A, W) if first == "A" else (W, A)
    pairs = changed_pairs(A, W)
    lines = []
    for k, (va, vw) in enumerate(pairs, 1):
        one, two = (va, vw) if rng.random() < 0.5 else (vw, va)
        lines.append(f"Pair {k}:\n  1: {one}\n  2: {two}")
    locks = LOCKS[:]
    rng.shuffle(locks)
    lock_txt = "\n".join(f"  Version {chr(65 + i)}: {l}" for i, l in enumerate(locks))
    parts = [f"You are {who}. Someone hands you a short investment plan written by a team of high-school students for a client called Laura Gao, and asks what you understood. Read as that person would, honestly. If a word means nothing to you, say so; don't be cleverer than the person you are playing.\n", RULES + "\n"]
    if tna:
        parts.append("First, the team's earlier submission, three Trading Notes with a reflection each (read them once; you may look back at them):\n\n" + TNA + "\n")
    parts.append("THE PITCH (sits above the plan):\n" + PITCH + "\n")
    parts.append("FIRST TEXT:\n" + t1 + "\n")
    parts.append(PART1)
    parts.append("SECOND TEXT (another version of the same plan; the pitch above is the same):\n" + t2 + "\n")
    parts.append(P2HEAD + "\n".join(lines) + "\n")
    parts.append(P3HEAD + lock_txt + "\n" + P3B)
    key = {"first": first, "pairs": [(va, vw) for va, vw in pairs], "lock_order": locks}
    return "\n".join(parts), key


if __name__ == "__main__":
    import json
    OUT.mkdir(parents=True, exist_ok=True)
    keys = {}
    for i, n in enumerate(["S1", "S2", "S3", "S4"]):
        txt, key = build(n, 20261103 + i)
        (OUT / f"{n}.txt").write_text(txt)
        keys[n] = key
    (OUT / "keys.json").write_text(json.dumps(keys, indent=1))
    print("pairs:", len(keys["S1"]["pairs"]))
    for k, (a, w) in enumerate(keys["S1"]["pairs"], 1):
        print(k, "A:", a[:90], "| W:", w[:90])
