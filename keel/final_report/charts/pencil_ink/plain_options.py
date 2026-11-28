"""Three plain alternatives (Sat 28 Nov 2026, after Caplet found the first figure too contrived).
Same checked numbers: the stated 2031 range in four share markets (model; results_range_rule_2026-11-17.json
exhibit3_rows and NUMBERS 8p). Run: python3 -I plain_options.py <out_dir>"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
r = json.load(open(HERE.parent.parent / "numbers" / "results_range_rule_2026-11-17.json"))["exhibit3_rows"]
W = [  # (label, bottom, top)
    ("Shares become worthless", r["vt_to_zero"]["bottom"], r["vt_to_zero"]["top"]),
    ("Shares fall 40% before 2031", 95_000, 105_000),   # NUMBERS 8p
    ("Shares earn 7.5% a year", r["shares_median"]["bottom"], r["shares_median"]["top"]),
    ("Shares do very well (1 in 20)", r["shares_1in20_high_2028_31"]["bottom"], r["shares_1in20_high_2028_31"]["top"]),
]
for w in W: print(w)
FONT = "'Times New Roman', Tinos, 'Liberation Serif', Times, serif"
NAVY, LIGHT, GRID, TXT, MUT = "#26394D", "#B9C3CE", "#D9D9D6", "#1A1A1A", "#5E5E5B"
def money(v): return f"${v:,.0f}"
def head(s, w, title, sub):
    s.append(f'<text x="0" y="15" font-size="13" font-weight="bold" fill="{TXT}">{title}</text>')
    s.append(f'<text x="0" y="31" font-size="11" fill="{MUT}">{sub}</text>')
def foot(s, h, text):
    s.append(f'<text x="0" y="{h-4}" font-size="9" fill="{MUT}">{text}</text>')
def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}pt" height="{h}pt" viewBox="0 0 {w} {h}" '
            f'font-family="{FONT}"><rect width="{w}" height="{h}" fill="#fff"/>' + "".join(body) + "</svg>")
SRC = "Source: team model; Treasury curve of 6 November 2026; both deposits assumed to arrive."

def option_a():  # columns: what the building gets
    w, h = 468, 214; s = []
    head(s, w, "Whatever shares do, the building gets at least $95,000",
         "Laura's facility contribution in 2033, by how world shares perform from 2028")
    x0, y0, y1, vmax = 52, 168, 48, 140_000
    y = lambda v: y0 - (y0 - y1) * v / vmax
    for t in range(0, 140_001, 20_000):
        s.append(f'<line x1="{x0}" x2="{w}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="{GRID if t else TXT}" stroke-width="{0.5 if t else 0.8}"/>')
        s.append(f'<text x="{x0-6}" y="{y(t)+3.5:.1f}" font-size="9.5" fill="{MUT}" text-anchor="end">{money(t)}</text>')
    cw, step = 58, (w - x0) / 4
    for i, (lab, b, t) in enumerate(W):
        cx = x0 + step * i + (step - cw) / 2
        s.append(f'<rect x="{cx:.1f}" y="{y(b):.1f}" width="{cw}" height="{y0-y(b):.1f}" fill="{NAVY}"/>')
        if t > b:
            s.append(f'<rect x="{cx:.1f}" y="{y(t):.1f}" width="{cw}" height="{y(b)-y(t):.1f}" fill="{LIGHT}"/>')
        s.append(f'<text x="{cx+cw/2:.1f}" y="{y(t)-4:.1f}" font-size="10" text-anchor="middle" fill="{TXT}">{money(t)}</text>')
        words = lab.split(" ")
        l1, l2 = " ".join(words[:2]), " ".join(words[2:])
        s.append(f'<text x="{cx+cw/2:.1f}" y="{y0+12}" font-size="9.5" text-anchor="middle" fill="{TXT}">{l1}</text>')
        s.append(f'<text x="{cx+cw/2:.1f}" y="{y0+23}" font-size="9.5" text-anchor="middle" fill="{TXT}">{l2}</text>')
    lx = x0 + step * 3 + (step - cw) / 2 + cw + 4
    c0 = x0 + (step - cw) / 2 + cw / 2
    for j, tline in enumerate(("Held in", "Treasuries", "since", "January", "2028")):
        s.append(f'<text x="{c0:.1f}" y="{y(78_000)+11*j:.1f}" font-size="9.5" fill="#fff" text-anchor="middle">{tline}</text>')
    c3 = x0 + step * 3 + (step - cw) / 2 + cw / 2
    s.append(f'<text x="{c3:.1f}" y="{y(110_000)+3:.1f}" font-size="9.5" fill="{TXT}" text-anchor="middle">From shares</text>')
    foot(s, h, SRC)
    return svg(w, h, s)

def option_b():  # dumbbell: the stated range
    w, h = 468, 168; s = []
    head(s, w, "Shares move the top of Laura's range, never the bottom",
         "The range Laura could state to co-sponsors in 2031, by how world shares perform from 2028")
    x0, x1, vmin, vmax = 150, 452, 90_000, 135_000
    x = lambda v: x0 + (x1 - x0) * (v - vmin) / (vmax - vmin)
    top, pitch = 58, 22
    base = top + pitch * (len(W) - 1) + 12
    for t in range(90_000, 135_001, 10_000):
        s.append(f'<line x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top-10}" y2="{base}" stroke="{GRID}" stroke-width="0.5"/>')
        s.append(f'<text x="{x(t):.1f}" y="{base+12}" font-size="9.5" text-anchor="middle" fill="{MUT}">{money(t)}</text>')
    for i, (lab, b, t) in enumerate(W):
        yy = top + pitch * i
        s.append(f'<text x="0" y="{yy+3.5}" font-size="10.5" fill="{TXT}">{lab}</text>')
        s.append(f'<line x1="{x(b):.1f}" x2="{x(t):.1f}" y1="{yy}" y2="{yy}" stroke="{MUT}" stroke-width="1.6"/>')
        s.append(f'<circle cx="{x(b):.1f}" cy="{yy}" r="4.2" fill="{NAVY}"/>')
        if t > b:
            s.append(f'<circle cx="{x(t):.1f}" cy="{yy}" r="4.2" fill="#fff" stroke="{NAVY}" stroke-width="1.4"/>')
        s.append(f'<text x="{x(t)+8:.1f}" y="{yy+3.5}" font-size="10" fill="{TXT}">{money(t)}</text>')
    s.append(f'<text x="{x(95_000)-7:.1f}" y="{top-14}" font-size="9.5" fill="{NAVY}" text-anchor="start">Bottom: $95,000 in every case</text>')
    foot(s, h, SRC)
    return svg(w, h, s)

def option_c():  # horizontal stacked bars on a real $ axis: promises against the extra
    w, h = 468, 168; s = []
    head(s, w, "Shares can only add to what Laura has already promised",
         "What Laura will pay out from 2033, by how world shares perform from 2028")
    x0, x1, vmax = 150, 440, 700_000
    x = lambda v: x0 + (x1 - x0) * v / vmax
    top, pitch, bh = 50, 22, 12
    base = top + pitch * len(W) - 4
    for t in range(0, 700_001, 200_000):
        s.append(f'<line x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top-6}" y2="{base}" stroke="{GRID if t else TXT}" stroke-width="{0.5 if t else 0.8}"/>')
        s.append(f'<text x="{x(t):.1f}" y="{base+12}" font-size="9.5" text-anchor="middle" fill="{MUT}">{money(t)}</text>')
    for i, (lab, b, t) in enumerate(W):
        yy = top + pitch * i
        s.append(f'<text x="0" y="{yy+bh-2.5}" font-size="10.5" fill="{TXT}">{lab}</text>')
        s.append(f'<rect x="{x0}" y="{yy}" width="{x(595_000)-x0:.1f}" height="{bh}" fill="{NAVY}"/>')
        if t > b:
            s.append(f'<rect x="{x(595_000):.1f}" y="{yy}" width="{x(500_000+t)-x(595_000):.1f}" height="{bh}" fill="{LIGHT}"/>')
        s.append(f'<text x="{x(500_000+t)+5:.1f}" y="{yy+bh-2.5}" font-size="10" fill="{TXT}">{money(500_000+t)}</text>')
    s.append(f'<text x="{x0+4}" y="{top-9}" font-size="9.5" fill="{NAVY}">Ten payments of $50,000 and the building\'s first $95,000</text>')
    foot(s, h, SRC)
    return svg(w, h, s)

out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE); out.mkdir(parents=True, exist_ok=True)
for name, f in (("option_a_columns", option_a), ("option_b_range", option_b), ("option_c_bars", option_c)):
    (out / f"{name}.svg").write_text(f()); print("wrote", name)
