from common import *
X = [104, 196, 288, 366]
b = [t(0, 12, "Figure 1", 11, "bold")]
for x, s in zip(X[:3] + [X[3] - 6], ["2027", "2028", "2031", "2033–2042"]):
    b.append(t(x, 40, s, 10, "bold", fill=MUTE, anc="middle" if x != X[3] - 6 else "start"))
b.append(ln(0, 47, W, 47, "#BBBBBB", 0.6))
def row(y, name, c, x0, cells, end, dash=None, w=2):
    b.append(t(0, y + 3.5, name, 10.5, "bold"))
    b.append(ln(x0, y, X[3] - 12, y, c, w, dash))
    for x, s in cells:
        b.append(dot(x, y, c, 3.2))
        b.append(t(x + 7, y + 17, s, 9.5, anc="start") if x == X[2] else t(x, y + 17, s, 9.5, anc="middle"))
    b.append(t(X[3] - 6, y + 3.5, end, 10.5, "bold"))
row(70, "Ten payments", NAVY, X[0], [(X[0], "$300,000"), (X[1], "+ $39,162")], "$50,000 a year")
row(112, "Building", SAGE, X[1], [(X[1], "$81,244 IBTM"), (X[2], "+ half of VT")], "$95,000–$115,000")
row(154, "VT", GRAPH, X[1], [(X[1], "$29,594"), (X[2], "half kept")], "about $28,700", dash="4 3", w=1.5)
b.append(ln(X[2], 150, X[2], 117, SAGE, 1.1))
b.append(f'<path d="M{X[2]-2.8} {120} L{X[2]} {115} L{X[2]+2.8} {120} Z" fill="{SAGE}"/>')
h = 180
open("comp_a.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{h}pt" viewBox="0 0 {W} {h}"><rect width="{W}" height="{h}" fill="#fff"/>' + "".join(b) + "</svg>")
