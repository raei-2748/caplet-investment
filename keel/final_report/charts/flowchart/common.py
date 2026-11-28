F = "'Times New Roman', Tinos, 'Liberation Serif', Times, serif"
NAVY, SAGE, GOLD, GRAPH, INK, MUTE, RULE = "#26394D", "#829887", "#B99A60", "#A3A29F", "#222222", "#5A5A5A", "#D9D9D9"
W = 468
def t(x, y, s, size=9, w="normal", st="normal", fill=INK, anc="start", extra=""):
    s = s.replace("&", "&amp;")
    return f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{w}" font-style="{st}" fill="{fill}" text-anchor="{anc}" {extra}>{s}</text>'
def lines(x, y, rows, size=9, lead=None, **k):
    lead = lead or size * 1.22
    return "".join(t(x, y + i * lead, r, size, **k) for i, r in enumerate(rows))
def ln(x1, y1, x2, y2, c=RULE, w=0.75, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"{d}/>'
def diamond(x, y, r=4.2, c=GOLD):
    return f'<path d="M{x} {y-r} L{x+r} {y} L{x} {y+r} L{x-r} {y} Z" fill="#fff" stroke="{c}" stroke-width="1.4"/>'
def dot(x, y, c, r=3.2, hollow=False):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{"#fff" if hollow else c}" stroke="{c}" stroke-width="1.2"/>'
def svg(h, body, title, sub):
    head = t(0, 12, title, 11, "bold") + t(0, 27, sub, 11, st="italic")
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{h}pt" viewBox="0 0 {W} {h}"><rect width="{W}" height="{h}" fill="#fff"/>{head}{body}</svg>'
NOTE = ["Note. Treasury curve of 6 November 2026. Cash waiting for a payment is assumed to earn nothing, fund payouts are cut by 0.5%",
        "and the range is rounded down to $5,000. The ceiling and the amount kept are the central case. Source: Team calculations."]
