"""E5 (pre-mortem analyst) - deadline clock in Australian time and the risk ranking behind phase_E/E5_premortem.md.

How to run (repo root, under a second, no network needed):
    .venv/bin/python research/insight_v1/scripts/E5_premortem_checks.py

It prints:
 [1] Every 2026-27 deliverable deadline (5:00 p.m. U.S. Eastern) converted to UTC and to the Australian capital-city
     time zones, so the team sees which Saturday-morning hour each deadline really is, and where daylight saving shifts
     it (Australia starts daylight saving on Sun 4 Oct 2026; the U.S. ends it on Sun 1 Nov 2026).
 [2] U.S. regular-session open and close in Australian time on the dates that matter for the Trading Notes and the
     portfolio lock (target fill date, the "tested" window end, the last trading day).
 [3] The pre-mortem risk register ranked by a rough expected harm = likelihood x impact weight, with the top 10 first.
 [4] A robustness check: the rank of every cause under two other impact weightings (one that punishes exclusion
     harder, one that punishes quality losses harder), and which causes stay in the top 10 under all three.

INPUTS and status labels
 - Deadlines, all "no later than 5:00 p.m. ET": roster Oct 9, Trading Notes Oct 23, IPS Nov 6 ("Trading ends and your
   portfolio is locked"), Final Report Dec 4 (VERIFIED-REPO-FILE:
   competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md, Deliverables list).
 - Official trading dates Sep 28 - Nov 6 2026 (VERIFIED-PRIMARY via research/insight_v1/phase_A/wins_week1_guardrails.md,
   SMApply Trading Details). U.S. regular session 9:30 a.m. - 4:00 p.m. ET (ASSUMPTION: standard exchange hours, not
   re-checked for 2026; Columbus Day Oct 12 affects the bond market only, also an ASSUMPTION).
 - Time-zone rules: the IANA database shipped with Python's zoneinfo (ASSUMPTION that the installed rules are current
   for 2026; they give AEDT from 4 Oct 2026 and EST from 1 Nov 2026, matching phase_A A4's table).
 - Likelihood bands and impact weights in RISKS: ASSUMPTION (E5's judgement, explained in the .md file). They are rough
   rankings for deciding where to spend the team's hours, not probabilities anyone measured.
"""

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")
AU_ZONES = [
    ("Sydney/Melbourne/Canberra/Hobart", ZoneInfo("Australia/Sydney")),
    ("Brisbane", ZoneInfo("Australia/Brisbane")),
    ("Adelaide", ZoneInfo("Australia/Adelaide")),
    ("Darwin", ZoneInfo("Australia/Darwin")),
    ("Perth", ZoneInfo("Australia/Perth")),
]

DEADLINES = [
    ("Team roster", datetime(2026, 10, 9, 17, 0, tzinfo=ET)),
    ("Trading Notes Analysis", datetime(2026, 10, 23, 17, 0, tzinfo=ET)),
    ("IPS (portfolio locks the same day)", datetime(2026, 11, 6, 17, 0, tzinfo=ET)),
    ("Final Report + school documentation (later)", datetime(2026, 12, 4, 17, 0, tzinfo=ET)),
]

SESSION_DATES = [
    ("First official trading day", datetime(2026, 9, 28)),
    ("Target fill date (ticket)", datetime(2026, 10, 2)),
    ("Hard stop for first fills (ticket)", datetime(2026, 10, 9)),
    ("End of the 'tested' window (close)", datetime(2026, 10, 20)),
    ("First session after U.S. clocks change", datetime(2026, 11, 2)),
    ("Last trading day (portfolio locks)", datetime(2026, 11, 6)),
]

# Likelihood bands (chance the failure happens by its deadline if the team does nothing beyond what exists on
# 2026-09-28). ASSUMPTION.
L_BANDS = {"VL": 0.02, "L": 0.06, "LM": 0.11, "M": 0.20, "MH": 0.30, "H": 0.40, "VH": 0.60}
# Impact weights (effect on the chance of a Top-50 place if the failure happens). ASSUMPTION.
IMPACT_SETS = {
    "base": {"Fatal": 1.00, "Severe": 0.60, "Major": 0.30, "Moderate": 0.15, "Minor": 0.05},
    "exclusion-heavy": {"Fatal": 1.00, "Severe": 0.40, "Major": 0.15, "Moderate": 0.08, "Minor": 0.02},
    "quality-heavy": {"Fatal": 1.00, "Severe": 0.70, "Major": 0.45, "Moderate": 0.25, "Minor": 0.10},
}

# (id, short name, deliverable, likelihood band, impact level)
RISKS = [
    ("PM-01", "Strategy not owned by the students; voice reads AI-made", "TN+IPS", "H", "Severe"),
    ("PM-02", "IPS format breach (pages, word caps, font, spacing, banned items)", "IPS", "M", "Fatal"),
    ("PM-03", "Over-complex, jargon-dense pitch and IPS", "IPS", "H", "Major"),
    ("PM-04", "AI wording in permanent WInS notes or in reflections", "TN", "M", "Severe"),
    ("PM-05", "Team process breakdown (roles, one login, holidays/exams, late drafts)", "TN+IPS", "H", "Major"),
    ("PM-06", "Notes contradict the pitch/IPS (book date, scaling, split, labels)", "TN+IPS", "MH", "Major"),
    ("PM-07", "Plan reads timid, or reads as analysing her; residency missing", "TN+IPS", "MH", "Major"),
    ("PM-08", "AI use not logged, or logged inaccurately", "TN+IPS", "M", "Severe"),
    ("PM-09", "Generic thesis (fails the swap test; copies Wharton's example)", "TN+IPS", "MH", "Major"),
    ("PM-10", "Overclaiming words (guaranteed, matched, bought in Jan 2027, promised...)", "TN+IPS", "H", "Moderate"),
    ("PM-11", "A required IPS element missing (certainty test, diversification, liquidity...)", "IPS", "M", "Major"),
    ("PM-12", "Decision rules left open in the IPS (split, floor timing, a/s/q...)", "IPS", "M", "Major"),
    ("PM-13", "Missed deadline (Australian time, upload, one account holder)", "TN+IPS", "L", "Fatal"),
    ("PM-14", "WInS rule breach (instrument, day trade, cap, cash)", "TN (WInS)", "LM", "Severe"),
    ("PM-15", "Undefined 'required trading activity' minimum missed", "TN (WInS)", "LM", "Severe"),
    ("PM-16", "Fewer than three usable executed trades by Oct 23", "TN", "LM", "Severe"),
    ("PM-17", "A wrong, stale or mislabelled number", "TN+IPS", "MH", "Moderate"),
    ("PM-18", "IPS title page mismatch (team name, member names, WInS username)", "IPS", "L", "Fatal"),
    ("PM-19", "Roster missed or wrong (members lock; names must match later)", "IPS", "VL", "Fatal"),
    ("PM-20", "Trading-note mechanics (cut-off, typo, wrong trade, added note)", "TN", "M", "Moderate"),
    ("PM-21", "Reflections weak or non-compliant (>100 words, cherry-picked, staged)", "TN", "M", "Moderate"),
    ("PM-22", "Frozen Nov 6 book does not reflect the IPS", "IPS", "LM", "Major"),
    ("PM-23", "SMApply submission forms not read in advance", "TN+IPS", "LM", "Major"),
    ("PM-24", "Visible case misread (2027 purchase vs 'set aside' 2033, WInS P&L...)", "IPS", "L", "Major"),
    ("PM-25", "Laura misused (quotes, pull quote, identity tilt, flattery, private detail)", "TN+IPS", "LM", "Moderate"),
    ("PM-26", "Anyone on the team contacts Laura (including social media)", "all", "VL", "Fatal"),
    ("PM-27", "Paid help or a non-Wharton competition course", "all", "VL", "Fatal"),
    ("PM-28", "Membership or team-leader rule breach", "all", "VL", "Fatal"),
    ("PM-29", "Advisor decides or trades; 'our portfolio manager approved'", "TN+IPS", "L", "Moderate"),
    ("PM-30", "Public repo exposure (copying, findable AI text, student data)", "TN+IPS", "L", "Major"),
]


def fmt(dt):
    return dt.strftime("%a %d %b %H:%M %Z")


def section_1():
    print("[1] Deadlines (5:00 p.m. U.S. Eastern) in UTC and Australian time")
    for name, dt in DEADLINES:
        print(f"  {name}: {fmt(dt)} = {fmt(dt.astimezone(UTC))}")
        for label, tz in AU_ZONES:
            print(f"      {label:34s} {fmt(dt.astimezone(tz))}")
    print()


def section_2():
    print("[2] U.S. regular session (9:30-16:00 ET, ASSUMPTION) in Sydney and Perth time")
    syd = ZoneInfo("Australia/Sydney")
    per = ZoneInfo("Australia/Perth")
    for name, d in SESSION_DATES:
        op = datetime.combine(d.date(), time(9, 30), tzinfo=ET)
        cl = datetime.combine(d.date(), time(16, 0), tzinfo=ET)
        print(f"  {name} ({d:%a %d %b} ET): open {fmt(op.astimezone(syd))} / close {fmt(cl.astimezone(syd))};"
              f" Perth open {fmt(op.astimezone(per))}")
    print()


def ranked(weights):
    rows = []
    for rid, name, deliv, band, imp in RISKS:
        lik = L_BANDS[band]
        rows.append((lik * weights[imp], rid, name, deliv, band, lik, imp))
    rows.sort(key=lambda r: (-r[0], r[1]))
    return rows


def section_3():
    print("[3] Risk register ranked by expected harm = likelihood x impact weight (base weights; ASSUMPTION)")
    print(f"  {'rank':>4} {'id':6} {'L':>3} {'L~':>5} {'impact':8} {'harm':>6}  deliverable  cause")
    for i, (harm, rid, name, deliv, band, lik, imp) in enumerate(ranked(IMPACT_SETS["base"]), 1):
        mark = " <- top 10" if i <= 10 else ""
        print(f"  {i:4d} {rid:6} {band:>3} {lik:5.2f} {imp:8} {harm:6.3f}  {deliv:11s}  {name}{mark}")
    rows = ranked(IMPACT_SETS["base"])
    cut = rows[9][0]
    tied = [r[1] for r in rows if abs(r[0] - cut) < 1e-12]
    if len(tied) > 1:
        print(f"  Note: rank 10 is a tie at harm {cut:.3f} between {', '.join(tied)}; the order among them is by id only.")
    print()


def section_4():
    print("[4] Robustness: rank under each impact weighting (lower = worse)")
    ranks = {}
    for key, w in IMPACT_SETS.items():
        for i, row in enumerate(ranked(w), 1):
            ranks.setdefault(row[1], {})[key] = i
    keys = list(IMPACT_SETS)
    print("  id     " + " ".join(f"{k:>16s}" for k in keys) + "  in top 10 under all three?")
    for rid, *_ in RISKS:
        r = ranks[rid]
        allin = all(r[k] <= 10 for k in keys)
        print(f"  {rid:6} " + " ".join(f"{r[k]:16d}" for k in keys) + f"  {'YES' if allin else ''}")
    stable = [rid for rid, *_ in RISKS if all(ranks[rid][k] <= 10 for k in keys)]
    print(f"  In the top 10 under all three weightings: {', '.join(stable)} ({len(stable)} causes)")
    entering = sorted({rid for rid, *_ in RISKS if any(ranks[rid][k] <= 10 for k in keys)} - set(stable))
    print(f"  In the top 10 under at least one weighting but not all: {', '.join(entering)}")
    print()


if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
