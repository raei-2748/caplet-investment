"""FICTION (Team Keel). Draws the Office floor plan with people: keel/office/office_map.svg.
Edit ROOMS and re-run (python3 keel/scripts/office_map.py) instead of editing the SVG by hand. Map text: keel/OFFICE.md."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parents[1] / "office/office_map.svg"
W, H = 1400, 980
PEOPLE = {"Nora": "#7C3AED", "Felix": "#2563EB", "Jun": "#059669",
          "Kai": "#DC2626", "Amara": "#B45309", "Tess": "#DB2777"}
SIM = "#6B7280"
HOME = {"Nora": "THE NOTICEBOARD", "Felix": "THE WINDOW", "Jun": "THE LAB",
        "Kai": "THE TRADING DESK", "Amara": "LAURA'S ROOM", "Tess": "THE WRITING ROOM"}

# (name, x, y, w, h, job lines, people [(name, role)], simulated visitors, agents, files, fill)
ROOMS = [
    ("LAURA'S ROOM", 30, 100, 330, 250, ["A simulated Laura and co-sponsors", "react to the plan (case only)"],
     [("Amara", "host")], ["Laura (sim)", "co-sponsors (sim)"],
     ["case-analyst", "cosponsor-reader", "taiwan-researcher"], "rooms/lauras_room.md", "#FEF3C7"),
    ("THE LONG ROOM", 380, 100, 640, 250, ["Debates, votes, decisions. The clocks stretch here.",
                                           "Six bunks behind a bookcase; a skylight; two clocks"],
     [("Nora", "chair"), ("Felix", "votes"), ("Jun", "votes"), ("Kai", "votes"), ("Amara", "votes"), ("Tess", "votes")],
     [], [], "tea_room.md (the wall), meetings/", "#EDE9FE"),
    ("THE COURTROOM", 1040, 100, 330, 250, ["Drafts on trial: rival team,", "devil's advocate, mock judges"],
     [("Kai", "prosecutor"), ("Nora", "bench")], ["Team Spinnaker (Kai plays them)", "5 mock judges (sim)"],
     ["devils-advocate", "mock-judge"], "rooms/courtroom.md", "#FEE2E2"),
    ("THE LIBRARY", 30, 370, 250, 270, ["Wide reading, often not finance.", "\"This reminds me of Laura's", "plan because...\" (must hold up)"],
     [("Felix", "librarian"), ("Kai", "reading pile")], [],
     ["ideation ladder:", "Haiku > Sonnet > Opus"], "rooms/library.md, library/", "#DBEAFE"),
    ("THE LAB", 300, 370, 250, 270, ["Experiments: hypothesis, roast,", "test, result, verdict.", "Failures are kept."],
     [("Jun", "head"), ("Kai", "roasts")], [],
     ["scenario-modeller", "numbers-auditor"], "rooms/lab.md, scripts/", "#D1FAE5"),
    ("THE TRADING DESK", 570, 370, 250, 270, ["Market check, rules check,", "every order checked first"],
     [("Kai", "trades (story)"), ("Jun", "markets"), ("Felix", "rules")], [],
     ["trade-checker", "ladder-pricer"], "pm/MARKETS.md, office/checks/", "#FFE4E6"),
    ("THE WRITING ROOM", 840, 370, 260, 270, ["Drafts get the house voice;", "fat cut, words counted"],
     [("Tess", "editor"), ("Amara", "first drafts")], [],
     ["format-gatekeeper", "final-report-planner"], "VOICE.md, drafts/", "#FCE7F3"),
    ("THE ARCHIVE", 1120, 370, 250, 270, ["Locked submissions, the spine,", "the AI-use record.", "Nothing may contradict it."],
     [("Tess", "keeper")], [],
     ["evidence-archivist", "ai-use-recorder", "coherence-checker (Nora)"], "rooms/archive.md", "#F3F4F6"),
    ("THE WINDOW", 30, 660, 250, 200, ["The only way in or out.", "Facts come in dated;", "nothing goes out unread"],
     [("Felix", "watch")], [],
     ["rules-verifier", "integrity-officer", "fact-checker"], "competition/", "#E0F2FE"),
    ("THE NOTICEBOARD", 300, 660, 520, 200, ["Nora's plain update, loose ends, proposed work,",
                                             "road map and countdown to each lock"],
     [("Nora", "update and board")], [], ["chief-of-staff"], "pm/, office/outbox/, office/LEDGER.md", "#EDE9FE"),
    ("THE KITCHEN", 840, 660, 260, 200, ["Off duty: snacks, jokes,", "friendships, tensions"],
     [("Amara", "the thermos"), ("Jun", "coffee")], [], [], "the episodes", "#FEF9C3"),
    ("THE ROOFTOP", 1120, 660, 250, 200, ["Sundays: why are we doing this,", "what did we learn, who are", "we becoming?"],
     [("Tess", "host")], [], [], "rooms/rooftop.md", "#ECFCCB"),
]


def text(x, y, s, size=12, weight="normal", fill="#111827", family="Helvetica, Arial, sans-serif", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')


def chip(x, y, name, role, room_name=""):
    c = PEOPLE[name]
    return (f'<circle cx="{x + 9}" cy="{y - 4}" r="9" fill="{c}"/>' + text(x + 9, y, name[0], 11, "bold", "#fff", anchor="middle")
            + f'<text x="{x + 23}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="12">'
            f'<tspan font-weight="bold" fill="{c}">{name}</tspan><tspan fill="#374151" font-size="11">  {escape(role)}</tspan>'
            + ('<tspan fill="#111827" font-size="11" font-weight="bold">  \u2605 home room</tspan>' if HOME[name] == room_name else "")
            + '</text>')


def room(r):
    name, x, y, w, h, job, people, sims, agents, files, fill = r
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#374151" stroke-width="1.5"/>',
           text(x + 12, y + 24, name, 15, "bold")]
    cy = y + 42
    for line in job:
        out.append(text(x + 12, cy, line, 11, fill="#374151")); cy += 15
    cy += 8
    if name == "THE LONG ROOM":  # six seats round the table
        out.append(f'<rect x="{x + 150}" y="{cy}" width="340" height="44" rx="22" fill="#fff" stroke="#9CA3AF"/>')
        for i, (p, _) in enumerate(people):
            px = x + 175 + i * 58
            out.append(f'<circle cx="{px}" cy="{cy + 22}" r="13" fill="{PEOPLE[p]}"/>' + text(px, cy + 27, p[0], 13, "bold", "#fff", anchor="middle"))
            out.append(text(px, cy + 60, p, 11, "bold", PEOPLE[p], anchor="middle"))
        out.append(text(x + 320, cy + 80, "Nora chairs; all six vote", 11, fill="#374151", anchor="middle"))
        cy += 96
    else:
        for p, role in people:
            out.append(chip(x + 12, cy + 4, p, role, name)); cy += 21
        for s in sims:
            out.append(f'<circle cx="{x + 21}" cy="{cy}" r="8" fill="none" stroke="{SIM}" stroke-dasharray="3 2"/>'
                       + text(x + 35, cy + 4, s, 11, fill=SIM)); cy += 19
    cy += 4
    for a in agents:
        out.append(text(x + 12, cy + 4, a, 10.5, fill="#4B5563", family="Menlo, Consolas, monospace")); cy += 14
    out.append(text(x + 12, y + h - 10, files, 10, fill="#6B7280", family="Menlo, Consolas, monospace"))
    return "\n".join(out)


def main():
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
             f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
             text(30, 42, "The Keel Office: top floor, Fernleigh library (FICTION)", 22, "bold"),
             text(30, 70, "Twelve rooms, six people, 18 AI agents (names in grey monospace). \u2605 marks each person's home room. "
                  "Map and rules: keel/OFFICE.md", 12, fill="#374151")]
    parts += [room(r) for r in ROOMS]
    ly = 892
    parts.append(text(30, ly, "People", 12, "bold"))
    lx = 90
    for p, c in PEOPLE.items():
        parts.append(f'<circle cx="{lx}" cy="{ly - 4}" r="7" fill="{c}"/>' + text(lx + 12, ly, p, 12, "bold", c)); lx += 90
    parts.append(f'<circle cx="{lx + 10}" cy="{ly - 4}" r="7" fill="none" stroke="{SIM}" stroke-dasharray="3 2"/>'
                 + text(lx + 22, ly, "simulated visitor (a test, never a quote)", 12, fill=SIM))
    parts.append(text(30, ly + 26, "Outside the Window: Caplet's six students (real). They ask (/keel, /office), vote, rewrite in their own words "
                      "and submit; only Ray trades. Keel proposes, Caplet decides.", 12, fill="#111827"))
    parts.append(text(30, ly + 48, "Quiet period until Sat 7 Nov 09:00 Sydney: the Lab and the Library work only on the IPS. Nothing leaves "
                      "the Office for a deliverable without Felix's rules check, a judging criterion and a student's own words.", 12, fill="#111827"))
    parts.append("</svg>")
    OUT.write_text("\n".join(parts) + "\n")
    print(OUT)


if __name__ == "__main__":
    main()
