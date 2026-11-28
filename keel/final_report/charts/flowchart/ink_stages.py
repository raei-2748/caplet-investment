"""Figure 1: the plan as a pencil sketch inked in three stages. Payments' 2027 ink = Table 2 net receipts (original
ladder, early cash earning nothing); floor $95,000 from 2028; top $115,000 from 2031 (central case); about $28,700 kept."""
from common import *
NET = [47101, 46497, 45911, 45204, 44268, 43195, 43061, 43043, 42180, 42469]
PEN = "#8A8A8A"
U = 44 / 50000          # pt per dollar
BASE = 176
import random
random.seed(7)
DEFS = ('<defs><filter id="graphite" x="-5%" y="-5%" width="110%" height="110%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="n"/>'
        '<feDisplacementMap in="SourceGraphic" in2="n" scale="1.3" xChannelSelector="R" yChannelSelector="G" result="d"/>'
        '<feTurbulence type="fractalNoise" baseFrequency="2.2" numOctaves="1" seed="9" result="g"/>'
        '<feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25" result="ga"/>'
        '<feComposite in="d" in2="ga" operator="in"/></filter></defs>')
def _j(v, a=0.5): return v + random.uniform(-a, a)
def pencil(x, y, w, h, hatch=True):
    e = 2.4
    o = []
    for k in range(2):  # two light passes, as a hand draws over a line
        for a, b, c, d in [(x - e, y, x + w + e, y), (x - e, y + h, x + w + e, y + h), (x, y - e, x, y + h + e), (x + w, y - e, x + w, y + h + e)]:
            o.append(f'<line x1="{_j(a):.2f}" y1="{_j(b):.2f}" x2="{_j(c):.2f}" y2="{_j(d):.2f}" stroke="#5A5A5A" stroke-width="{0.55 if k else 0.75}" stroke-linecap="round" opacity="{0.55 if k else 0.85}"/>')
    if hatch:  # loose diagonal shading inside the box
        cid = f"c{random.randint(0, 10**9)}"
        o.append(f'<clipPath id="{cid}"><rect x="{x+1}" y="{y+1}" width="{w-2}" height="{h-2}"/></clipPath><g clip-path="url(#{cid})">')
        sp = 3.2
        i = -h
        while i < w:
            o.append(f'<line x1="{x+i+_j(0,0.6):.2f}" y1="{y+h:.2f}" x2="{x+i+h+_j(0,0.6):.2f}" y2="{y:.2f}" stroke="#8C8C8C" stroke-width="0.4" opacity="{random.uniform(0.45,0.75):.2f}"/>')
            i += sp
        o.append("</g>")
    return '<g filter="url(#graphite)">' + "".join(o) + "</g>"
def ink(x, v, w, c, v0=0):
    return f'<rect x="{x:.1f}" y="{BASE - v*U:.1f}" width="{w}" height="{(v-v0)*U:.1f}" fill="{c}"/>'
def panel(x0, year, stage, cap):
    o = [t(x0, 56, year, 11, "bold")]
    bw, gap = 4.8, 1.2
    for k in range(10):
        x = x0 + k * (bw + gap)
        o.append(pencil(x, BASE - 50000 * U, bw, 50000 * U, hatch=False))
        o.append(ink(x, NET[k] if stage == 0 else 50000, bw, NAVY))
    xb = x0 + 10 * (bw + gap) + 6
    o.append(pencil(xb, BASE - 115000 * U, 15, 115000 * U))
    if stage >= 1: o.append(ink(xb, 95000 if stage == 1 else 115000, 15, SAGE))
    xk = xb + 28
    o.append(pencil(xk, BASE - 29594 * U, 15, 29594 * U))
    if stage == 2:  # half the shares move into the building
        sx, sy = xk + 7.5, BASE - 29594 * U - 4
        ex, ey = xb + 17, BASE - 105000 * U
        o.append(f'<path d="M{sx} {sy} C{sx} {ey+10}, {sx-2} {ey}, {ex+4} {ey}" fill="none" stroke="{SAGE}" stroke-width="1.1"/>')
        o.append(f'<path d="M{ex} {ey} L{ex+5} {ey-2.8} L{ex+5} {ey+2.8} Z" fill="{SAGE}"/>')
    o.append(t(x0 + 29, BASE + 11, "Payments", 7.5, anc="middle", fill=MUTE))
    o.append(t(xb + 7.5, BASE + 11, "Building", 7.5, anc="middle", fill=MUTE))
    o.append(t(xk + 7.5, BASE + 11, "Shares", 7.5, anc="middle", fill=MUTE))
    o.append(lines(x0, BASE + 27, cap, 8.5))
    return "".join(o), xb, xk
b = [t(0, 12, "Figure 1", 11, "bold")]
b.append(f'<rect x="0" y="27" width="14" height="9" fill="{NAVY}"/><rect x="14" y="27" width="14" height="9" fill="{SAGE}"/>')
b.append(t(34, 35, "Ink: paid by Treasuries Laura holds", 10))
b.append(pencil(212, 27, 28, 9))
b.append(t(246, 35, "Pencil: not yet paid for", 10))
P = [(0, "2027", 0, ["$300,000 buys ten", "Treasuries, one per", "payment. If early cash", "earns nothing, they", "fall $57,070 short."]),
     (118, "2028", 1, ["$39,162 closes the gap.", "$81,244 inks a $95,000", "floor for the building.", "$29,594 buys shares."]),
     (236, "2031", 2, ["Half the shares move to", "Treasuries, whatever the", "market has done. Laura", "tells co-sponsors", "$95,000 to $115,000."]),
     (354, "2033\u20132042", 3, ["A $445,655 reserve pays", "$50,000 each January.", "$115,000 to the building", "and about $28,700 kept,", "in the central case."])]
for x0, yr, st, cap in P:
    s_, xb, xk = panel(x0, yr, st, cap); b.append(s_)
    if st == 1:
        b.append(t(xb + 18, BASE - 95000 * U + 3, "$95,000", 8, "bold"))
    if st == 3:
        b.append(t(xb + 7.5, BASE - 115000 * U - 5, "$115,000", 8, "bold", anc="middle"))
H = BASE + 78
open("ink_stages.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>' + DEFS + "".join(b) + "</svg>")
