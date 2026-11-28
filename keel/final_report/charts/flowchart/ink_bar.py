"""Figure 1: what Laura's Treasuries will pay against what stays in shares. Numbers: draft Table 2 ($500,000), the range
$95,000-$115,000 (NUMBERS 4, central case), about $28,700 kept (draft, audit-checked)."""
from common import *
LS = "#B9C6BB"
b = [t(0, 12, "Figure 1", 11, "bold")]
# key
b.append(f'<rect x="0" y="30" width="16" height="9" fill="{NAVY}"/><rect x="16" y="30" width="16" height="9" fill="{SAGE}"/>')
b.append(t(38, 38, "Paid by Treasuries Laura holds, even if every share is worth nothing", 10))
b.append(f'<rect x="0.5" y="46.5" width="31" height="8" fill="none" stroke="{GRAPH}" stroke-dasharray="3 2"/>')
b.append(t(38, 54, "Shares, promised to no one", 10))
# full bar, to scale
k = 468 / 643.7
ya, h = 72, 30
wp, wf, wt, wk = 500 * k, 95 * k, 20 * k, 28.7 * k
x = 0
b.append(f'<rect x="0" y="{ya}" width="{wp-1:.1f}" height="{h}" fill="{NAVY}"/>')
b.append(t(10, ya + 19.5, "$500,000", 12, "bold", fill="#fff")); b.append(t(80, ya + 19.5, "Ten payments of $50,000, 2033 to 2042", 10, fill="#fff"))
x1 = wp
b.append(f'<rect x="{x1:.1f}" y="{ya}" width="{wf-1:.1f}" height="{h}" fill="{SAGE}"/>')
b.append(f'<rect x="{x1+wf:.1f}" y="{ya}" width="{wt-1:.1f}" height="{h}" fill="{LS}"/>')
b.append(f'<rect x="{x1+wf+wt+0.5:.1f}" y="{ya+0.5}" width="{wk-1.5:.1f}" height="{h-1}" fill="none" stroke="{GRAPH}" stroke-dasharray="3 2"/>')
# zoom
yb = 138
b.append(ln(x1, ya + h, 0, yb, "#BBBBBB", 0.6)); b.append(ln(468, ya + h, 468, yb, "#BBBBBB", 0.6))
kk = 468 / 143.7
wf2, wt2, wk2 = 95 * kk, 20 * kk, 28.7 * kk
b.append(f'<rect x="0" y="{yb}" width="{wf2-2:.1f}" height="{h}" fill="{SAGE}"/>')
b.append(f'<rect x="{wf2:.1f}" y="{yb}" width="{wt2-2:.1f}" height="{h}" fill="{LS}"/>')
b.append(f'<rect x="{wf2+wt2+0.5:.1f}" y="{yb+0.5}" width="{wk2-1:.1f}" height="{h-1}" fill="none" stroke="{GRAPH}" stroke-dasharray="3 2"/>')
b.append(t(10, yb + 19.5, "$95,000", 12, "bold", fill="#fff"))
b.append(t(wf2 + 8, yb + 19.5, "+$20,000", 12, "bold"))
b.append(t(wf2 + wt2 + 7, yb + 19.5, "About $28,700", 12, "bold"))
yl = yb + h + 15
b.append(lines(0, yl, ["Building floor, held from 2028"], 9.5))
b.append(lines(wf2, yl, ["Moved from", "shares in 2031"], 9.5))
b.append(lines(wf2 + wt2 + 1, yl, ["Kept by Laura,", "central case"], 9.5))
H = yl + 16
open("ink_bar.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>' + "".join(b) + "</svg>")
