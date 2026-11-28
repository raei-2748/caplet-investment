"""Figure 2, tidied (Sat 28 Nov 2026): the plain column chart with an APA title, Times New Roman, a muted pair.
Numbers: results_range_rule_2026-11-17.json exhibit3_rows and NUMBERS 8p. Run: python3 -I tidy_figure.py <out_dir>"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
r = json.load(open(HERE.parent.parent / "numbers" / "results_range_rule_2026-11-17.json"))["exhibit3_rows"]
D = [("VT worthless", r["vt_to_zero"]["bottom"], r["vt_to_zero"]["top"]),
     ("VT down 40%", 95_000, 105_000),
     ("VT up 7.5% a year", r["shares_median"]["bottom"], r["shares_median"]["top"]),
     ("VT 1-in-20 high", r["shares_1in20_high_2028_31"]["bottom"], r["shares_1in20_high_2028_31"]["top"])]
F = "'Times New Roman', Tinos, 'Liberation Serif', Times, serif"
DARK, LIGHT, GRID, TXT = "#26394D", "#829887", "#EBEBEB", "#333333"
W, H = 468, 228
x0, x1, y0, y1, vmax = 60, 464, 196, 66, 140_000
y = lambda v: y0 - (y0 - y1) * v / vmax
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}" font-family="{F}" fill="{TXT}">',
     f'<rect width="{W}" height="{H}" fill="#fff"/>',
     '<text x="0" y="13" font-weight="bold" font-size="12">Figure 2</text>',
     '<text x="0" y="32" font-style="italic" font-size="12">Range Laura Could State to Co-Sponsors in 2031, by VT Outcome</text>']
for t in range(0, vmax + 1, 20_000):
    s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="{GRID if t else "#8C8C8C"}" stroke-width="{0.6 if t else 0.8}"/>')
    s.append(f'<text x="{x0-6}" y="{y(t)+3.5:.1f}" text-anchor="end" font-size="9.5">${t:,}</text>')
step = (x1 - x0) / len(D); bw = 30
for i, (lab, b, t) in enumerate(D):
    c = x0 + step * (i + 0.5)
    s.append(f'<rect x="{c-bw-1:.1f}" y="{y(b):.1f}" width="{bw}" height="{y0-y(b):.1f}" fill="{DARK}"/>')
    s.append(f'<rect x="{c+1:.1f}" y="{y(t):.1f}" width="{bw}" height="{y0-y(t):.1f}" fill="{LIGHT}"/>')
    s.append(f'<text x="{c-bw/2-1:.1f}" y="{y(b)-4:.1f}" text-anchor="middle" font-size="8.5">${b:,.0f}</text>')
    s.append(f'<text x="{c+bw/2+1:.1f}" y="{y(t)-4:.1f}" text-anchor="middle" font-size="8.5">${t:,.0f}</text>')
    s.append(f'<text x="{c:.1f}" y="{y0+14}" text-anchor="middle" font-size="10">{lab}</text>')
lx = x1 - 100
s.append(f'<rect x="{lx}" y="48" width="8" height="8" fill="{DARK}"/><text x="{lx+12}" y="55.5" font-size="9.5">Floor</text>')
s.append(f'<rect x="{lx+50}" y="48" width="8" height="8" fill="{LIGHT}"/><text x="{lx+62}" y="55.5" font-size="9.5">Ceiling</text>')
s.append('</svg>')
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE)
(out / "figure2_final.svg").write_text("".join(s)); print(D)
