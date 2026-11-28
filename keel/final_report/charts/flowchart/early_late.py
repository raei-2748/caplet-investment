"""Early versus delayed facility protection (replaces Table 3's simulated rows). Numbers: the draft's Table 3,
checked by the 28 Nov audit (keel/final_report/AUDIT_2026-11-28.md)."""
from common import F, NAVY, SAGE, MUTE, lines
G = [("5th percentile", 100_477, 76_556), ("Median", 123_036, 130_471), ("95th percentile", 151_053, 222_342)]
W, H = 468, 284
x0, x1, y0, y1, vmax = 46, 464, 214, 84, 250_000
y = lambda v: y0 - (y0 - y1) * v / vmax
k = lambda v: f"${v/1000:,.0f}k"
TXT = "#333333"
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}" font-family="{F}" fill="{TXT}">',
     f'<rect width="{W}" height="{H}" fill="#fff"/>',
     '<text x="0" y="13" font-weight="bold" font-size="12">Figure 3</text>',
     '<text x="0" y="32" font-style="italic" font-size="12">Projected Facility Proceeds by December 2032, Floor Bought in 2028 or 2031</text>']
for v in range(0, vmax + 1, 50_000):
    s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="{"#EBEBEB" if v else "#8C8C8C"}" stroke-width="{0.6 if v else 0.8}"/>')
    s.append(f'<text x="{x0-6}" y="{y(v)+3.5:.1f}" text-anchor="end" font-size="10">{k(v)}</text>')
s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(95_000):.1f}" y2="{y(95_000):.1f}" stroke="#8C8C8C" stroke-width="0.9" stroke-dasharray="4 3"/>')
s.append(f'<line x1="{x0+330}" x2="{x0+352}" y1="52" y2="52" stroke="#8C8C8C" stroke-width="0.9" stroke-dasharray="4 3"/><text x="{x0+357}" y="55.5" font-size="9.5">$95,000 target</text>')
step = (x1 - x0) / 3; bw = 44
for i, (lab, a, b) in enumerate(G):
    c = x0 + step * (i + 0.5)
    for dx, v, col in ((-bw / 2 - 2, a, NAVY), (bw / 2 + 2, b, SAGE)):
        s.append(f'<rect x="{c+dx-bw/2:.1f}" y="{y(v):.1f}" width="{bw}" height="{y0-y(v):.1f}" fill="{col}"/>')
        inside = abs(y(v) - y(95_000)) < 16 and v < 95_000
        ty, fc = (y(v) + 14, "#fff") if inside else (y(v) - 5, TXT)
        s.append(f'<text x="{c+dx:.1f}" y="{ty:.1f}" text-anchor="middle" font-size="11" font-weight="bold" fill="{fc}">{k(v)}</text>')
    s.append(f'<text x="{c:.1f}" y="{y0+15}" text-anchor="middle" font-size="10.5">{lab}</text>')
# legend with the shortfall share beside each strategy
ly = 48
s.append(f'<rect x="{x0+8}" y="{ly}" width="8" height="8" fill="{NAVY}"/><text x="{x0+20}" y="{ly+7.5}" font-size="9.5">Floor bought in 2028 (our plan): 1.5% of simulations below $95,000</text>')
s.append(f'<rect x="{x0+8}" y="{ly+13}" width="8" height="8" fill="{SAGE}"/><text x="{x0+20}" y="{ly+20.5}" font-size="9.5">Floor bought in 2031 (alternative): 16.4% below $95,000</text>')
note = ["Note. Projected Treasury payouts to the facility by December 2032, including projected reinvestment income, from 200,000",
        "simulations with 7.5% median annual equity growth. Both strategies are measured against today’s $95,000 target, not against",
        "a range stated in 2031: our plan’s 1.5% are futures in which yields fall before 2028. Source: Team calculations."]
s.append(lines(0, y0 + 40, note, 8, fill=MUTE))
s.append('</svg>')
open("early_late.svg", "w").write("".join(s))
