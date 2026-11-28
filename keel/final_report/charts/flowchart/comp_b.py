from common import *
# One bar of $450,000, in the order each dollar is committed
L, R = 0, W
k = (R - L) / 450000
segs = [(300000, NAVY, None), (39162, NAVY, None), (81244, SAGE, None), (29594 / 2, SAGE, "half"), (29594 / 2, GRAPH, None)]
b = []
yb, hb = 92, 22
x = L
xs = []
for v, c, tag in segs:
    w = v * k
    op = ' fill-opacity="0.55"' if tag == "half" else ""
    b.append(f'<rect x="{x:.2f}" y="{yb}" width="{w:.2f}" height="{hb}" fill="{c}"{op}/>')
    xs.append((x, x + w)); x += w
# white separators
for a, _ in xs[1:]:
    b.append(ln(a, yb, a, yb + hb, "#fff", 1.2))
# deposits above
x300 = L + 300000 * k
b.append(ln(L, 70, L, 78, MUTE, .6)); b.append(ln(L, 78, x300 - 2, 78, MUTE, .6)); b.append(ln(x300 - 2, 70, x300 - 2, 78, MUTE, .6))
b.append(ln(x300 + 2, 70, x300 + 2, 78, MUTE, .6)); b.append(ln(x300 + 2, 78, R, 78, MUTE, .6)); b.append(ln(R, 70, R, 78, MUTE, .6))
b.append(t(L, 64, "January 2027 deposit, $300,000", 9, "bold", fill=MUTE))
b.append(t(R, 64, "January 2028 deposit, $150,000", 9, "bold", fill=MUTE, anc="end"))
# claim labels below
def claim(x, num, head, rows, c, anc="start"):
    b.append(t(x, yb + hb + 16, f"{num}  {head}", 10, "bold", fill=INK, anc=anc))
    b.append(lines(x, yb + hb + 29, rows, 8.5, anc=anc))
claim(L, "1", "Ten payments, $339,162",
      ["The whole first deposit and the first $39,162 of the second buy Treasuries maturing",
       "before each January. $36,774 of it covers the $57,070 that early cash might not earn."], NAVY)
x2 = xs[2][0]
b.append(ln(x2, yb + hb, x2, yb + hb + 6, SAGE, 1))
claim(R, "2", "Facility floor, $81,244", ["IBTM, paid out", "December 2032"], SAGE, "end")
# VT callout
xv = xs[3][0]
b.append(t(xv - 4, yb - 4, "VT $29,594", 8.5, "bold", fill=INK, anc="end"))
# section: 2031 and 2033
y2 = 196
b.append(ln(0, y2 - 14, W, y2 - 14, RULE, .6))
b.append(t(0, y2, "January 2031", 10, "bold"))
b.append(diamond(72, y2 - 3.5, 3.8))
b.append(lines(82, y2, ["Half of VT moves into IBTM, whatever the market has done. Laura states her range",
                         "to co-sponsors only once the Treasuries for it are held. The other half is promised to no one."], 9))
y3 = y2 + 40
b.append(t(0, y3, "2033 to 2042", 10, "bold"))
cols = [(0, NAVY, "$445,655", ["operating reserve in January 2033;", "$50,000 each January to 2042"]),
        (168, SAGE, "$95,000–$115,000", ["to the building; $95,000 even", "if shares were worth nothing"]),
        (330, GRAPH, "About $28,700", ["left to Laura after", "a $115,000 contribution"])]
for x, c, big, rows in cols:
    b.append(f'<rect x="{x}" y="{y3+10}" width="3" height="40" fill="{c}"/>')
    b.append(t(x + 9, y3 + 22, big, 12, "bold"))
    b.append(lines(x + 9, y3 + 35, rows, 8.5))
b.append(lines(0, y3 + 74, NOTE, 7.5, fill=MUTE))
open("comp_b.svg", "w").write(svg(y3 + 88, "".join(b), "Figure 1", "Where Each Dollar Goes, in the Order It Is Committed"))
