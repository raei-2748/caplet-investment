"""Plain APA figure (Sat 28 Nov 2026): the 2031 range in four share outcomes, as a student's grouped column chart.
Numbers: results_range_rule_2026-11-17.json exhibit3_rows and NUMBERS 8p. Run: python3 -I plain_figure.py <out_dir>"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
r = json.load(open(HERE.parent.parent / "numbers" / "results_range_rule_2026-11-17.json"))["exhibit3_rows"]
D = [("VT worthless", r["vt_to_zero"]["bottom"], r["vt_to_zero"]["top"]),
     ("VT down 40%", 95_000, 105_000),
     ("VT up 7.5% a year", r["shares_median"]["bottom"], r["shares_median"]["top"]),
     ("VT 1-in-20 high", r["shares_1in20_high_2028_31"]["bottom"], r["shares_1in20_high_2028_31"]["top"])]
F = "Calibri, Carlito, 'Liberation Sans', Arial, sans-serif"
W, H = 432, 216
x0, x1, y0, y1, vmax = 52, 420, 172, 34, 140_000
y = lambda v: y0 - (y0 - y1) * v / vmax
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}" font-family="{F}" font-size="11">',
     f'<rect width="{W}" height="{H}" fill="#fff"/>',
     f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="none" stroke="#d9d9d9"/>',
     f'<text x="{W/2}" y="20" text-anchor="middle" font-size="13" fill="#595959">2031 range by VT outcome</text>']
for t in range(0, vmax + 1, 20_000):
    s.append(f'<line x1="{x0}" x2="{x1}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="#d9d9d9" stroke-width="0.75"/>')
    s.append(f'<text x="{x0-5}" y="{y(t)+3.5:.1f}" text-anchor="end" font-size="9" fill="#595959">${t:,}</text>')
step = (x1 - x0) / len(D); bw = 24
for i, (lab, b, t) in enumerate(D):
    c = x0 + step * (i + 0.5)
    s.append(f'<rect x="{c-bw-1:.1f}" y="{y(b):.1f}" width="{bw}" height="{y0-y(b):.1f}" fill="#4472C4"/>')
    s.append(f'<rect x="{c+1:.1f}" y="{y(t):.1f}" width="{bw}" height="{y0-y(t):.1f}" fill="#ED7D31"/>')
    s.append(f'<text x="{c:.1f}" y="{y0+14}" text-anchor="middle" font-size="9" fill="#595959">{lab}</text>')
s.append(f'<line x1="{x0}" x2="{x1}" y1="{y0}" y2="{y0}" stroke="#d9d9d9" stroke-width="0.75"/>')
lx = (x0 + x1) / 2 - 70
s.append(f'<rect x="{lx}" y="{y0+26}" width="7" height="7" fill="#4472C4"/><text x="{lx+12}" y="{y0+33}" font-size="9" fill="#595959">Bottom</text>')
s.append(f'<rect x="{lx+60}" y="{y0+26}" width="7" height="7" fill="#ED7D31"/><text x="{lx+72}" y="{y0+33}" font-size="9" fill="#595959">Top</text>')
s.append('</svg>')
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE)
(out / "figure2_plain.svg").write_text("".join(s)); print(D)
