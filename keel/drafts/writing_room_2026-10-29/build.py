"""Writing Room, 29 Oct (beat 7): V29 with the hard fixes (A); A plus the four-doors rule (B, the readers' pick);
B with the range's reasoning restored (C). Counts and blind reads: cold_reads.md.
Rerun after any V29 change: python3 build.py  (reads ../../ips_rewrite/drafts/D9/ips.txt)."""
src = open('../../ips_rewrite/drafts/D9/ips.txt').read()

def rep(t, a, b):
    assert t.count(a) == 1, a
    return t.replace(a, b)

# A: hard fixes only, at the smallest word cost (+3)
a = rep(src, "So money she has buys certainty; money she expects carries risk.",
        "So money she has buys certainty; money she expects insures it, then carries risk.")
a = rep(a, "In 2033 the reserve tops up once, then never changes.",
        "In 2033 the operating reserve tops up once, then only shrinks.")
# H4: 'three times worse' is stale once the 2031 lock is in (IDEA_BANK note under row 77): top reached 86.6% (L-12, S0)
# puts the top at the 13.4th percentile, so over-promising is weighted 0.866/0.134 = ~6.5 times under-promising.
a = rep(a, "which we judge three times worse", "which we judge six times worse")
open('ips_A_hard.txt', 'w').write(a)

# B: A + the dated rule (four doors) + the ten holdings named as the reserve,
# paid by dropping one whole idea: the range's two embarrassments (its 'why' is the one rule; FR keeps it)
b = rep(a, "If needs change, cheques first; floor and stocks are bought smaller together.",
        "Every rule here fires in a year the case already set, never on a hunch; "
        "if needs change, the gift takes it before it is named, her half after, a cheque last.")
b = rep(b, "In 2033 the operating reserve tops up once, then only shrinks.",
        "In 2033 the ten holdings become the operating reserve, topped up once; after that it only shrinks.")
# Round-2 reader: "topped up once from her half" collided with "Wipe out every share ... no cheque is worse off"
# (her half is shares); the order line says who pays. Third reader in a row tripped on "$300,000 buys them": H3.
b = rep(b, "So her first $300,000 buys them in January 2027:", "So her first $300,000 buys them, or nearly, in January 2027:")
b = rep(b, "Her 2031 range can embarrass her twice over. Too low, and co-sponsors give less – bigger lead gifts draw "
           "bigger gifts. Too high, and she breaks her word, which we judge six times worse. So the bottom is the "
           "floor she owns, rounded down;",
        "In 2031 she names a range. Its bottom is the floor she owns, rounded down;")
open('ips_B_doors.txt', 'w').write(b)

# B as first read blind is kept in the memo; the line above is B after both readers tripped on
# "never below its named bottom" next to "comes off the quoted bottom" and asked who pays after naming.

# C: B, but the range's reasoning comes back (both readers named it the loser's one strength), without the
# "three times" both called made up, nor the donor clause (FR, cited: bank #6); paid by the deletion-test kicker, which B's order line now repeats, and "never on a hunch".
c = rep(b, "In 2031 she names a range. Its bottom is the floor she owns, rounded down;",
        "Her 2031 range can embarrass her twice over. Too low, and co-sponsors give less. "
        "Too high, and she breaks her word, which is worse. So the bottom is the floor she owns, rounded down;")
c = rep(c, " Wipe out every share she owns and no cheque is worse off – only the gift.", "")
c = rep(c, ", never on a hunch;", ";")
open('ips_C_doors_keep_range.txt', 'w').write(c)
