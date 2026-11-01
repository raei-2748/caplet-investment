"""Round-2 menu: whole packages on V49, counted strict. AI DRAFT (Claude, 1 Nov 2026). Run after build.py."""
import importlib.util, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "office" / "tools"))
from textcheck import words_limit as w
spec = importlib.util.spec_from_file_location("b", HERE / "build.py"); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)

CUTS = {
  "no145_tess": ("Asked in our model to name our typical bottom, $145,000, it leaves", "Asked in our model to name our typical bottom, it leaves"),
  "no145_kai": ("Asked in our model to name our typical bottom, $145,000, it leaves", "Matched in our model to our typical bottom, it leaves"),
  "sounds": (" Sounds good, on average.", ""),
  "sounds_colon": ("Sounds good, on average. But", "But"),
  "head_bounce": ("How to bounce a cheque\n\n", ""),
  "head_rival": ("Know thy rival\n\n", ""),
  "crush": ("\n\nDo not crush.", ""),
  "bounce_tess": ("our model bounces a cheque once in 66.", "a cheque bounces in one modelled future in 66."),
  "bounce_kai": ("our model bounces a cheque once in 66.", "one modelled future in 66 bounces a cheque."),
  "setaside_kai": ("take it from what she keeps, before she names a gift, not after.", "take it from what she keeps, then the gift, before she names one, not after."),
  "setaside_kai_p9": ("after the set-aside.", "after the shortfall."),
  "our_rival": ("We know this rival because", "We know our rival because"),
}
def pkg(picks, cuts):
    t = b.assemble(picks)
    for c in cuts:
        old, new = CUTS[c]
        if old not in t: return None, f"missing: {c}"
        t = t.replace(old, new, 1)
    return t, w(t)

MENU = {
  "readers' firsts (1A 2B 3C 4B 5C)": ({"opener":"A","bounce":"B","range":"C","catch":"B","rival":"C"}, []),
  "Tess r1 (1B 2B+repair 3A 4C 5A, no $145k)": ({"opener":"B","bounce":"B","range":"A","catch":"C","rival":"A"}, ["bounce_tess","no145_tess"]),
  "Kai r1 (1A 2B 3A 4C 5A; no $145k, no 'Sounds good', no rival heading)": ({"opener":"A","bounce":"B","range":"A","catch":"C","rival":"A"}, ["no145_kai","sounds","head_rival"]),
  "Amara r1 by ear (1B 2B 3 own 4B 5C)": ({"opener":"B","bounce":"B","range":"A","catch":"B","rival":"C"}, []),
  "readers' firsts where affordable (1A 2B 3A 4B 5C; no $145k)": ({"opener":"A","bounce":"B","range":"A","catch":"B","rival":"C"}, ["no145_tess"]),
}
R3 = {  # round 3: the two packages the cold readers paraphrase (AI DRAFT, Claude, 1 Nov 2026)
  "K": ({"opener":"A","bounce":"B","range":"A","catch":"B","rival":"C"},
        ["no145_kai","sounds","head_bounce","head_rival","our_rival","crush","bounce_kai","setaside_kai","setaside_kai_p9"]),
  "T": ({"opener":"A","bounce":"B","range":"A","catch":"C","rival":"C"},
        ["no145_kai","sounds","head_bounce","crush","setaside_kai","setaside_kai_p9"]),
}

W1_EDITS = [  # Tess lands it, round 3 (H-012): package K + these. AI DRAFT (Claude, 1 Nov 2026)
  ("If it halves that deposit, one modelled future in 66 bounces a cheque.",
   "If the recession halves that deposit, our model bounces a cheque once in 66."),   # Kai (b) + round-2 unit vote
  ("then the gift, before she names one, not after.", "then the gift's floor, before she names a range."),  # Kai (a) amended; ', not after' pays
  ("enough to grow back into all of it: her floor.", "enough to grow back into whatever the ladder didn't take: her floor."),  # Kai (c) amended (truth)
  ("The rest, the interest they should earn,", "The rest, worth the interest they should earn,"),  # read twice by 4 of 4 readers
  (" The US government defaults.", ""),  # pays (Tess)
]

def w1():
    t, _ = pkg(*R3["K"])
    for old, new in W1_EDITS:
        assert old in t, old
        t = t.replace(old, new, 1)
    return t

if __name__ == "__main__":
    t = w1(); (HERE / "final_package_W1.txt").write_text(t + "\n"); print(f"{w(t):>4}  final package W1 (Tess lands it)")
    for k, (picks, cuts) in R3.items():
        t, n = pkg(picks, cuts)
        (HERE / f"r3_package_{k}.txt").write_text(t + "\n")
        print(f"{n!s:>4}  round-3 package {k}")
    for name, (picks, cuts) in MENU.items():
        t, n = pkg(picks, cuts)
        print(f"{n!s:>4}  {name}")
    print("cuts available (strict words saved): headings 5 + 3, 'Sounds good, on average.' 4, 'Do not crush.' 3, '$145,000,' 1-2")
