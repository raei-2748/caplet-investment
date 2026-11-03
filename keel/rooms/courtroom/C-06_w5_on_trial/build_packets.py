"""AI-generated (Claude Code), Tue 3 Nov 2026, the Courtroom (C-06, huddle H-026). Builds the two blind reader packets.
(Keel is a simulated team, AI-written.) Each reader gets Nora's sheet (cold/SHEET.md, written before any reader ran)
and the two texts as X and Y, order drawn per reader from a fixed seed. The mapping goes to cold/MAPPING_sealed.md,
which no reader sees. Run from repo root after the defence's repair exists:
    python3 keel/rooms/courtroom/C-06_w5_on_trial/build_packets.py"""
import hashlib, pathlib, random

ROOT = pathlib.Path(__file__).resolve().parents[4]
H = ROOT / "keel" / "huddles" / "2026-11-03_w5-on-trial"
TEXTS = {"V54": H / "exhibits" / "V54_ips.txt", "W5R": H / "exhibits" / "W5R_ips.txt"}
SEED = 20261103
rng = random.Random(SEED)
sheet = (H / "cold" / "SHEET.md").read_text()
lines = [f"# Sealed mapping (C-06, seed {SEED}); never shown to a reader", ""]
first = ["V54", "W5R"]; rng.shuffle(first)                         # J's order from the seed; S gets the reverse
for reader in ("J", "S"):                                            # (counterbalanced: the first build drew the same
    order = first if reader == "J" else first[::-1]                  # order for both; changed before any reader ran)
    body = [sheet.rstrip(), "", "---", ""]
    for lab, key in zip(("X", "Y"), order):
        body += [f"## Text {lab}", "", TEXTS[key].read_text().strip(), ""]
    (H / "cold" / f"packet_{reader}.md").write_text("\n".join(body))
    lines.append(f"- Reader {reader}: X = {order[0]}, Y = {order[1]}")
for key, p in TEXTS.items():
    lines.append(f"- sha256 {key}: {hashlib.sha256(p.read_bytes()).hexdigest()[:16]}")
(H / "cold" / "MAPPING_sealed.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
