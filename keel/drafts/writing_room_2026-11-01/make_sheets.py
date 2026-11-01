"""Blind sheets for the two outside readers (shuffled per reader) and the labelled sheet for the room.
Keys are written to keys.json, never shown to a reader. Run after build.py."""
import json, random
from pathlib import Path
HERE = Path(__file__).resolve().parent
import importlib.util
spec = importlib.util.spec_from_file_location("build", HERE / "build.py"); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)

PLACES = ["opener", "bounce", "range", "catch", "rival"]
WHAT = {"opener": "the first paragraph", "bounce": "the paragraph under 'How to bounce a cheque'",
        "range": "the paragraph that begins 'In 2031'", "catch": "the paragraph after it",
        "rival": "the paragraph under 'Know thy rival'"}

def context():
    parts = list(b.P)
    for n, slot in enumerate(PLACES, 1):
        parts[b.IDX[slot]] = f"[PLACE {n}: one of the versions below]"
    return "\n\n".join(parts)

def sheet(seed, blind=True):
    rng = random.Random(seed); key = {}
    out = ["PITCH (50 words, fixed):", (HERE / "base_V49_pitch.txt").read_text().strip(), "",
           "IPS (500-word limit), with five places where versions differ:", "", context(), ""]
    for n, slot in enumerate(PLACES, 1):
        arms = list(b.ARMS[slot].items())
        if blind: rng.shuffle(arms)
        out.append(f"=== PLACE {n} ({WHAT[slot]}) ===")
        for i, (k, (src, text)) in enumerate(arms):
            label = f"{n}{'pqrstu'[i]}" if blind else f"{slot} {k}"
            key[label] = f"{slot} {k}"
            head = f"--- Version {label}" + ("" if blind else f" ({src}; IPS {b.words_limit(b.assemble({slot: k}))} strict)") + " ---"
            out += [head, text, ""]
    return "\n".join(out), key

keys = {}
for name, seed in [("reader_1", 11), ("reader_2", 22)]:
    text, key = sheet(seed); (HERE / f"blind_{name}.txt").write_text(text); keys[name] = key
text, _ = sheet(0, blind=False); (HERE / "room_sheet.txt").write_text(text)
(HERE / "keys.json").write_text(json.dumps(keys, indent=1))
print("ok", {k: len(v) for k, v in keys.items()})
