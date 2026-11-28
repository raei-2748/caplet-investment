from common import *
X = [110, 198, 290, 366]   # Jan 2027, Jan 2028, Jan 2031, outcome
b = []
for x, s in zip(X, ["January 2027", "January 2028", "January 2031", "2033 to 2042"]):
    b.append(t(x - 4, 48, s, 9, "bold", fill=MUTE))
b.append(ln(0, 54, W, 54, "#BBBBBB", 0.6))
def lane(y, num, name, why, c, x0, dash=None, w=2.2):
    b.append(t(0, y + 3, f"{num}", 10, "bold", fill=c))
    b.append(t(12, y + 3, name, 10, "bold"))
    b.append(lines(12, y + 15, why, 8.5, st="italic", fill=MUTE))
    b.append(ln(x0, y, X[3] - 8, y, c, w, dash))
    b.append(f'<path d="M{X[3]-8} {y-3.5} L{X[3]-2} {y} L{X[3]-8} {y+3.5} Z" fill="{c}"/>')
# lane 1
y1 = 70
lane(y1, "1", "The ten payments", ["Bought first, in Treasuries,", "with no reliance on shares", "or on interest not yet earned"], NAVY, X[0])
b += [dot(X[0], y1, NAVY), dot(X[1], y1, NAVY)]
b.append(lines(X[0] + 7, y1 + 15, ["$300,000 buys the", "original ladder,", "$2,388 short"], 8.5))
b.append(lines(X[1] + 7, y1 + 15, ["$39,162 first: $2,388", "completes the ladder;", "$36,774 buys Treasuries", "for a $57,070 gap if", "early cash earns nothing"], 8.5))
b.append(t(X[3], y1 + 3, "$445,655 reserve", 10.5, "bold", fill=NAVY))
b.append(lines(X[3], y1 + 15, ["in January 2033, paying", "$50,000 each January"], 8.5))
# lane 2
y2 = 140
lane(y2, "2", "The facility floor", ["What co-sponsors can", "count on, bought in 2028"], SAGE, X[1])
b += [dot(X[1], y2, SAGE), dot(X[2], y2, SAGE)]
b.append(lines(X[1] + 7, y2 + 15, ["$81,244 in IBTM,", "paid out December 2032"], 8.5))
b.append(lines(X[2] + 7, y2 + 15, ["Half of VT", "moves in; the", "range is stated"], 8.5))
b.append(t(X[3], y2 + 3, "$95,000–$115,000", 10.5, "bold", fill=INK))
b.append(lines(X[3], y2 + 15, ["to the building; $95,000", "even if shares were", "worth nothing"], 8.5))
# lane 3
y3 = 196
lane(y3, "3", "Growth", ["Half of it promised", "to no one"], GRAPH, X[1], dash="4 3", w=1.6)
b += [dot(X[1], y3, GRAPH), dot(X[2], y3, GRAPH, hollow=True)]
b.append(lines(X[1] + 7, y3 + 15, ["$29,594 in VT"], 8.5))
b.append(lines(X[2] + 7, y3 + 15, ["Half stays in VT"], 8.5))
b.append(t(X[3], y3 + 3, "About $28,700", 10.5, "bold", fill=INK))
b.append(lines(X[3], y3 + 15, ["left to Laura after", "a $115,000 contribution"], 8.5))
# the 2031 move: VT half up into the floor
b.append(ln(X[2], y3 - 4, X[2], y2 + 6, SAGE, 1.2))
b.append(f'<path d="M{X[2]-3} {y2+9} L{X[2]} {y2+4} L{X[2]+3} {y2+9} Z" fill="{SAGE}"/>')
# decision points
yd = 240
b.append(ln(0, yd - 12, W, yd - 12, RULE, 0.6))
b.append(t(0, yd + 3, "Decision points", 10, "bold"))
for x, rows in [(X[0], ["Reprice the ladder"]),
                (X[1], ["Reconsider if the", "deposit is not in", "by 31 March"]),
                (X[2], ["Move half of VT", "whatever the", "market has done"]),
                (X[3], ["Each December,", "confirm the", "next $50,000"])]:
    b.append(diamond(x, yd, 3.8))
    b.append(lines(x + 7, yd + 3, rows, 8.5))
b.append(t(0, yd + 48, "Only a missed deposit or a Treasury default changes the plan. A fall in share prices changes none of these steps.", 9, st="italic"))
b.append(lines(0, yd + 66, NOTE, 7.5, fill=MUTE))
open("comp_a.svg", "w").write(svg(yd + 80, "".join(b), "Figure 1", "How Laura’s Two Deposits Are Committed, in Order of Priority"))
