"""C-05: build the blind sheet for the cold readers (Courtroom, Sun 1 Nov 2026).

Writes cold/sheet.md (Wharton's word, sections 1-2 only, plus two unlabelled versions in a seeded order) and
cold/KEY.md (which letter is which; never shown to a reader). Standard library only.

    python3 keel/rooms/courtroom/C-05_build_sheet.py
"""
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parents[3]
HUD = ROOT / "keel/huddles/2026-11-01_do-not-crush-on-trial"
WW = (ROOT / "keel/WHARTON_WORD.md").read_text()

# Wharton's word, sections 1 and 2 only (the criteria and what the IPS is for)
start = WW.index("## 1. The five things judges score")
end = WW.index("## 3. What Wharton says judges look for")
wharton = WW[start:end].strip()

versions = {
    "V50": (HUD / "exhibits/V50_ips.txt").read_text().strip(),
    "V50R": (HUD / "exhibits/V50R_ips.txt").read_text().strip(),
}
order = list(versions)
random.Random(20261101).shuffle(order)
letters = dict(zip("AB", order))

out = ["# Two versions of one Investment Policy Statement (IPS)", "",
       "Both answer the same client case (Laura Gao, Wharton Global High School Investment Competition 2026-27).",
       "The IPS is a 500-word form field: no charts, links or citations. Read both, then judge.", "",
       "## What Wharton asks for (its own words)", "", wharton, ""]
for letter, name in letters.items():
    out += [f"## Version {letter}", "", versions[name], ""]
(HUD / "cold").mkdir(exist_ok=True)
(HUD / "cold/sheet.md").write_text("\n".join(out))
(HUD / "cold/KEY.md").write_text(
    "# Key (never shown to a cold reader)\n\n"
    + "\n".join(f"- Version {k} = {v}" for k, v in letters.items())
    + "\n\nSeed 20261101 (random.Random.shuffle).\n")
print(letters)
