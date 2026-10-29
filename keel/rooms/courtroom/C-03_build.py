"""Courtroom C-03, Thu 29 Oct 2026 (round 2 beat 8). AI-generated (Claude Code). (Keel is a simulated team, AI-written.)
Jun's one repair to the Writing Room's B (four doors as one line). Kai's charge K1: B's order line ("the gift takes it
before it is named, her half after, a cheque last") reads as a priority list, but para 17 two paragraphs up makes her
half pay the coupon gap BEFORE the quoted bottom moves, and so does the model (LR8 run.py line 29: x is sold from
Laura's half in Jan 2031; q_mc takes off only what spare cash and her half can't cover; door 4 in 2033 the same).
Repair: the order line states the principle the model obeys - a change lands on what isn't yet promised.
Run from repo root: python3 keel/rooms/courtroom/C-03_build.py"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE.parents[1] / "drafts" / "writing_room_2026-10-29" / "ips_B_doors.txt").read_text()

def rep(t, a, b):
    assert t.count(a) == 1, a
    return t.replace(a, b)

b2 = rep(src, "if needs change, the gift takes it before it is named, her half after, a cheque last.",
         "if needs change, the change lands on what isn't yet promised, never a cheque.")
(HERE / "C-03_B2.txt").write_text(b2)

# Nora's amendment after the cold judges (2 of 2 advanced B2 over V29; both docked Client Knowledge for losing the
# range's why, and both tripped on "comes off the quoted bottom" and the floor-sizing clause). Candidate only, untested:
# the Writing Room reads it blind on Fri 30 Oct.
b3 = rep(b2, "In 2031 she names a range.", "In 2031 she names a range: too low costs gifts; too high, her word.")
b3 = rep(b3, "comes off the quoted bottom", "comes off the bottom before it is quoted")
b3 = rep(b3, " sized to regrow what's left by 2033 and", "")
(HERE / "C-03_B3_candidate.txt").write_text(b3)
