#!/usr/bin/env python3
"""Count the Final Report's research and analysis volume by day (Sydney), for VOLUME.md and the portal.

Caplet, Mon 16 Nov 2026: "I don't see you doing anywhere near the volume of research and analysis I want to see from
you." This makes the volume visible. Counted from the files themselves, so nobody types a number in:

  cards        research cards in research/cards/ (dated by the commit that added them; uncommitted = today)
  rows         store rows in those cards (lines starting "| <number> |")
  sources      entries in each card's Sources section (one per non-empty line)
  passages     voice passages written (voice/round*/passages.json, by round folder date)
  readings     blind readings (reader files in voice/round*/ and goldmine/aha_test_*/; judge files in experience/)
  workers      research, analysis and reader workers sent out, from volume_runs.csv (kept by each run)

Outputs: VOLUME.md (the table) and volume.json (read by keel/office/portal/build_portal.py).
"""
import csv, datetime as dt, json, re, subprocess, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent            # keel/final_report/research
FR = HERE.parent
ROOT = FR.parent.parent
SYD = dt.timezone(dt.timedelta(hours=11))          # AEDT until April 2027
TODAY = dt.datetime.now(SYD).date().isoformat()
ROW = re.compile(r"^\|\s*\d+\s*\|")


def added_day(path):
    """Sydney date of the commit that first added the file; today if it is not committed yet."""
    try:
        out = subprocess.run(["git", "log", "--diff-filter=A", "--follow", "--format=%at", "--", str(path)],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    except Exception:
        out = []
    if not out:
        return TODAY
    return dt.datetime.fromtimestamp(int(out[-1]), SYD).date().isoformat()


def sources_in(text):
    n, on = 0, False
    for line in text.splitlines():
        if line.startswith("## "):
            on = "source" in line.lower()
            continue
        if on and line.strip() and not line.startswith("#") and len(line.strip()) > 25:
            n += 1
    return n


def main():
    day = defaultdict(lambda: defaultdict(int))
    cards = []
    for f in sorted((HERE / "cards").glob("*.md")):
        t = f.read_text(encoding="utf-8")
        d = added_day(f)
        rows = sum(1 for l in t.splitlines() if ROW.match(l))
        src = sources_in(t)
        day[d]["cards"] += 1
        day[d]["rows"] += rows
        day[d]["sources"] += src
        cards.append({"card": f.stem, "day": d, "rows": rows, "sources": src})
    for pj in sorted((FR / "voice").glob("round*/passages.json")):
        try:
            n = len(json.loads(pj.read_text(encoding="utf-8")))
        except Exception:
            n = 0
        day[added_day(pj)]["passages"] += n
    readers = list((FR / "voice").glob("round*/read*")) + list((FR / "voice").glob("round*/readings/*")) \
        + list((HERE / "goldmine").glob("aha_test_*/reader_*.md")) + list((HERE / "experience").glob("judge*.md"))
    for r in readers:
        if r.is_file():
            day[added_day(r)]["readings"] += 1
    runs = HERE / "volume_runs.csv"
    run_rows = []
    if runs.exists():
        for r in csv.DictReader(runs.open(encoding="utf-8")):
            run_rows.append(r)
            for k in ("research_workers", "analysis_workers", "readers"):
                day[r["date"]]["workers"] += int(r.get(k) or 0)
    store = HERE / "store" / "insights.jsonl"
    ideas = judged = 0
    if store.exists():
        for line in store.read_text(encoding="utf-8").splitlines():
            if line.strip():
                ideas += 1
                judged += 1 if json.loads(line).get("rated_by") == "judgement" else 0
    keys = ["workers", "cards", "rows", "sources", "passages", "readings"]
    days = sorted(day, reverse=True)
    totals = {k: sum(day[d][k] for d in days) for k in keys}
    since9 = [d for d in days if d >= "2026-11-08"]
    data = {"built": dt.datetime.now(SYD).isoformat(timespec="minutes"), "today": TODAY,
            "store_ideas": ideas, "store_judged": judged, "totals": totals,
            "days": [{"day": d, **{k: day[d][k] for k in keys}} for d in since9],
            "runs": run_rows[-12:], "cards": cards[-30:]}
    (HERE / "volume.json").write_text(json.dumps(data, indent=1), encoding="utf-8")

    lines = ["# Research and analysis volume, by day (Sydney)", "",
             "Caplet, Mon 16 Nov 2026: \"I don't see you doing anywhere near the volume of research and analysis I want to see",
             "from you ... GO INTO OVERDRIVE\". This page counts the Final Report's research and analysis by day, straight from",
             "the files (`volume.py`; the workers column from `volume_runs.csv`, kept by each run). Rebuilt by every run.", "",
             f"Store: {ideas:,} ideas, every one kept, {judged:,} judged one by one (`store/insights.jsonl`). Cards in `cards/`: {totals['cards']}; store rows in them: "
             f"{totals['rows']:,}; sources listed: {totals['sources']:,}.", "",
             "| Day | Workers sent | New cards | Store rows | Sources read | Voice passages | Blind readings |",
             "|---|---|---|---|---|---|---|"]
    for d in since9:
        x = day[d]
        lines.append(f"| {dt.date.fromisoformat(d).strftime('%a %d %b')} | {x['workers'] or ''} | {x['cards']} | {x['rows']} | "
                     f"{x['sources']} | {x['passages'] or ''} | {x['readings'] or ''} |")
    lines += ["", "Workers are counted from Mon 16 Nov, when the count began; before that each run sent at least four research workers (`../DAILY_RUN.md`).",
              "A card dated by its commit can land a day after its research when a run ends after midnight.", "",
              "## Runs", "", "| Day | Run | Research workers | Analysis workers | Blind readers | What they did |",
              "|---|---|---|---|---|---|"]
    for r in reversed(run_rows):
        lines.append(f"| {r['date']} | {r['run']} | {r['research_workers']} | {r['analysis_workers']} | {r['readers']} | {r['notes']} |")
    (HERE / "VOLUME.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"VOLUME.md: {len(since9)} days; totals {totals}; store {ideas} ideas")


if __name__ == "__main__":
    sys.exit(main())
