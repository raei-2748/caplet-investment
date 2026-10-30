"""Writing Room, Fri 30 Oct (round 3, beat 7): the texts the Long Room may pick between tonight.
B2 and B3 are the Courtroom's (C-03). Every arm below carries the Window's fact fix (the wipe-out line read A19
backwards), so the blind read compares only what is still a choice. Counts and blind reads: cold_reads.md.
Rerun after any change to the Courtroom texts: python3 build.py"""
B2 = open('../../rooms/courtroom/C-03_B2.txt').read()
B3 = open('../../rooms/courtroom/C-03_B3_candidate.txt').read()

def rep(t, a, b):
    assert t.count(a) == 1, a
    return t.replace(a, b)

# W1, the Window's first choice: 0 of 600,000 paths where the shares leave a cheque worse off (A19), 10 words, saves 5
WIPE = ("Wipe out every share she owns and no cheque is worse off – only the gift.",
        "The shares can help a cheque, never hurt one.")

# B2f: B2 with the fact fix only
b2f = rep(B2, *WIPE)
open('ips_B2f.txt', 'w').write(b2f)

# B3S: the Lab variant (L-13 slide: the cheques' 2033 claim comes off both ends before quoting, so para 11's
# "lands on what isn't yet promised" is true at the top) + Laura's Room's "co-sponsors'" (B3 never names them) + W1
b3s = rep(B3, *WIPE)
b3s = rep(b3s, "comes off the bottom before it is quoted", "comes off the range before it is quoted")
b3s = rep(b3s, "too low costs gifts;", "too low costs co-sponsors' gifts;")
open('ips_B3S.txt', 'w').write(b3s)

# B3O: B3S with the Library's per-end odds as the range's why (#84), stated as a principle: Book 7 keeps the
# final range and its numbers for the Final Report ("not expected to include ... a final facility-contribution range")
b3o = rep(b3s, "In 2031 she names a range: too low costs co-sponsors' gifts; too high, her word. Its bottom is the floor "
               "she owns, rounded down; the top adds half the stocks, and the other half stays hers.",
          "In 2031 she names a range, each end as sure as its miss is costly. Its bottom is the floor she owns, "
          "rounded down: missing it breaks her word. The top adds half the stocks: missing it only trims "
          "co-sponsors' plans. The other half stays hers.")
# Over 500 by 2, so B3O pays with one whole idea: the fund's size, "about one dollar in fifteen" (three cold
# readers in two rounds called it opaque; the FR keeps the number). A confound in B3O's favour, noted in cold_reads.md
b3o = rep(b3o, "The floor's expected interest, about one dollar in fifteen, buys", "The floor's expected interest buys")
open('ips_B3O.txt', 'w').write(b3o)

for n, t in [('B2', B2), ('B3', B3), ('B2f', b2f), ('B3S', b3s), ('B3O', b3o)]:
    print(n, len(t.split()), 'words by spaces')

# B3W, the Writing Room's pick for the Long Room: B3O (advanced by 3 of 3 blind readers) with the Window's second
# line, which 3 of 3 readers found more believable than W1 ("a stress test I can check"). "barely" stays: two readers
# asked to drop it, but the A19 count says the cheques do notice, in ~1 path in 550 by up to $2,953 (MODEL)
# The Window's wording began "Wipe them all out": in B3 "them" would follow "a world index fund" (singular) and miss
# Laura's half, which is shares too; "every share" keeps the antecedent and the scope, one word shorter
W2 = "Wipe out every share and the cheques barely notice; the gift does."
b3w = rep(b3o, WIPE[1], W2)
open('ips_B3W.txt', 'w').write(b3w)
print('B3W', len(b3w.split()), 'words by spaces')
