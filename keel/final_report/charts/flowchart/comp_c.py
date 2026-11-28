from common import *
b = []
rows = [
 ("January 2027", NAVY, "What must never depend on markets?",
  "The ten $50,000 payments. $300,000 buys the original ladder, one Treasury for each January, $2,388 short.", "$300,000"),
 ("January 2028", NAVY, "Does the ladder hold if early cash earns nothing?",
  "Not alone. The first $39,162 of the second deposit completes it and adds Treasuries.", "$57,070 gap closed"),
 ("January 2028", SAGE, "What can co-sponsors count on?",
  "A floor bought now, not later: $81,244 in IBTM, paid out December 2032. $29,594 goes to VT.", "$95,000 floor"),
 ("January 2031", SAGE, "When does Laura name a figure?",
  "Only once it is held. Half of VT moves into IBTM, whatever the market has done.", "$95,000–$115,000"),
 ("2033 to 2042", GRAPH, "What is left for Laura?",
  "The other half of VT, promised to no one, after a $115,000 contribution.", "About $28,700"),
]
y0, step, xs = 58, 44, 84
b.append(ln(xs, y0 - 4, xs, y0 + step * (len(rows) - 1), "#C8C8C8", 1))
for i, (d, c, q, a, big) in enumerate(rows):
    y = y0 + i * step
    b.append(t(0, y + 3, d, 9, "bold", fill=MUTE))
    b.append(diamond(xs, y, 4.2) if i in (1, 3) else dot(xs, y, c, 3.4))
    b.append(t(xs + 12, y + 3, q, 10, "bold", st="italic"))
    b.append(t(xs + 12, y + 16, a, 8.5))
    b.append(t(W, y + 3, big, 10.5, "bold", fill=INK, anc="end"))
yl = y0 + step * (len(rows) - 1) + 40
b.append(ln(0, yl - 12, W, yl - 12, RULE, .6))
b.append(t(0, yl + 2, "From January 2033 the Treasuries are a $445,655 operating reserve that pays each January to 2042.", 9))
b.append(t(0, yl + 16, "Only a missed deposit or a Treasury default changes the plan. A fall in share prices changes none of these steps.", 9, st="italic"))
b.append(lines(0, yl + 34, NOTE, 7.5, fill=MUTE))
open("comp_c.svg", "w").write(svg(yl + 48, "".join(b), "Figure 1", "Five Questions That Set Laura’s Plan"))
