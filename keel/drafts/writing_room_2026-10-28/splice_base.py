import sys
sys.path.insert(0, '/home/user/caplet-investment/keel/office/tools')
from textcheck import words_by_spaces, words_strict, words_limit
base = open('/home/user/caplet-investment/keel/ips_rewrite/drafts/D8/ips.txt').read()
FIX = [  # hard-issue fixes, every arm
 ("So her first $300,000 buys them in January 2027:", "So her first $300,000 buys them in January 2027, and her second fills any gap:"),
 ("That deposit fills any gap in the ladder, then buys the floor", "That deposit then buys the floor"),
 ("the promised half moves into Treasuries maturing before 2033.", "the promised half moves into the first cheque's fund."),
 ("that is what Laura's half, sellable any day, is for.", "that is what the rest of Laura's half, sellable any day, is for."),
]
CUT = [(" Keep the seed; risk only the harvest.", "")]
C6 = []
C6MC = [
 ("So the bottom is the floor she owns, rounded down;", "So the bottom is the floor she owns, rounded down, less any gap the bond market has already shown her that her own money can't cover;"),
 ("The fourth is our soft spot, the one thing that can still trim the gift.", "The fourth is our soft spot, so it gets one bite: the bottom, in 2031, before anyone hears it."),
]
A = [
 ("That deposit then buys the floor", "That deposit then buys a small Treasury holding for the coupons, then the floor"),
 ("The fourth is our soft spot, the one thing that can still trim the gift. So in January 2033 the reserve changes once: any projected shortfall, plus a cushion, moves into the next fund to mature, from leftover cash and Laura's half first.",
  "The fourth is our soft spot, so it was paid for in 2028: that small holding, Laura's again after the tenth cheque. In January 2033 any gap already showing moves into the next fund to mature, from leftover cash and Laura's half first."),
]
def apply(t, edits):
    for o, n in edits:
        assert t.count(o) == 1, o
        t = t.replace(o, n)
    return t
arms = {'V28': [], 'V28+fix': FIX, 'V28+fix+cut': FIX+CUT, 'C6': FIX+CUT+C6, 'C6+MC': FIX+CUT+C6MC, 'A': FIX+CUT+A}
for k, e in arms.items():
    t = apply(base, e)
    open(f'{k}.txt','w').write(t)
    print(f'{k:12} spaces {words_by_spaces(t)} strict {words_strict(t)} limit {words_limit(t)}')
