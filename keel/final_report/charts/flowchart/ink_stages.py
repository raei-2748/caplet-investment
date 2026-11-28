"""Figure 1: the plan as a pencil sketch inked in three stages. Payments' 2027 ink = Table 2 net receipts (original
ladder, early cash earning nothing); floor $95,000 from 2028; top $115,000 from 2031 (central case); about $28,700 kept."""
from common import *
NET = [47101, 46497, 45911, 45204, 44268, 43195, 43061, 43043, 42180, 42469]
PEN = "#8A8A8A"
U = 44 / 50000          # pt per dollar
BASE = 176
def pencil(x, y, w, h):
    e = 2.2  # construction-line overshoot at each corner
    return "".join(ln(a, b, c, d, PEN, 0.7) for a, b, c, d in [
        (x - e, y, x + w + e, y), (x - e, y + h, x + w + e, y + h), (x, y - e, x, y + h + e), (x + w, y - e, x + w, y + h + e)])
def ink(x, v, w, c, v0=0):
    return f'<rect x="{x:.1f}" y="{BASE - v*U:.1f}" width="{w}" height="{(v-v0)*U:.1f}" fill="{c}"/>'
def panel(x0, year, stage, cap):
    o = [t(x0, 56, year, 11, "bold")]
    bw, gap = 7, 1.6
    for i in range(10):
        x = x0 + i * (bw + gap)
        o.append(pencil(x, BASE - 50000 * U, bw, 50000 * U))
        o.append(ink(x, NET[i] if stage == 0 else 50000, bw, NAVY))
    xb = x0 + 10 * (bw + gap) + 8
    o.append(pencil(xb, BASE - 115000 * U, 20, 115000 * U))
    if stage >= 1: o.append(ink(xb, 95000 if stage == 1 else 115000, 20, SAGE))
    xk = xb + 28
    o.append(pencil(xk, BASE - 28700 * U, 20, 28700 * U))
    o.append(t(x0 + 42, BASE + 12, "Ten payments", 8.5, anc="middle", fill=MUTE))
    o.append(t(xb + 10, BASE + 12, "Building", 8.5, anc="middle", fill=MUTE))
    o.append(t(xk + 10, BASE + 12, "Kept", 8.5, anc="middle", fill=MUTE))
    o.append(lines(x0, BASE + 30, cap, 9.5))
    return "".join(o), xb, xk
b = [t(0, 12, "Figure 1", 11, "bold")]
b.append(f'<rect x="0" y="27" width="14" height="9" fill="{NAVY}"/><rect x="14" y="27" width="14" height="9" fill="{SAGE}"/>')
b.append(t(34, 35, "Ink: paid by Treasuries Laura holds", 10))
b.append(pencil(212, 27, 28, 9))
b.append(t(246, 35, "Pencil: not yet paid for", 10))
P = [(0, "2027", 0, ["$300,000 buys the ten Treasuries.", "If early cash earns nothing,", "they fall $57,070 short."]),
     (160, "2028", 1, ["$39,162 of the second deposit", "fills the gap. $81,244 inks", "a $95,000 floor for the building."]),
     (320, "2031", 2, ["Half the shares move to Treasuries,", "whatever the market has done:", "$115,000 in the central case."])]
for x0, yr, st, cap in P:
    s, xb, xk = panel(x0, yr, st, cap); b.append(s)
    if st == 1:
        b.append(t(xb + 24, BASE - 95000 * U + 3, "$95,000", 8.5, "bold"))
    if st == 2:
        b.append(t(xb + 10, BASE - 115000 * U - 5, "$115,000", 8.5, "bold", anc="middle"))
        b.append(t(xk + 10, BASE - 28700 * U - 5, "$28,700", 8.5, "bold", anc="middle"))
H = BASE + 66
open("ink_stages.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>' + "".join(b) + "</svg>")
