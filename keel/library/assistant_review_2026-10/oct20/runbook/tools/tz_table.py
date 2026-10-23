"""Time-zone table for the TNA and IPS submission runbooks (Python zoneinfo; no network).

    python3 tz_table.py

Each row is defined once in the zone it is anchored to (Sydney for internal steps, New York for Wharton deadlines
and US market events) and printed in Sydney, US Eastern and UTC, with the hours left to the deadline.
"""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

SYD, NY, UTC = ZoneInfo("Australia/Sydney"), ZoneInfo("America/New_York"), ZoneInfo("UTC")

ROWS = [
    # (deliverable, label, local datetime, zone)
    ("TNA", "Wharton Thu working day starts (UNVERIFIED hours, 9 am ET)", datetime(2026, 10, 22, 9, 0), NY),
    ("TNA", "Text lock", datetime(2026, 10, 22, 16, 0), SYD),
    ("TNA", "Paste and word-count gate ends", datetime(2026, 10, 22, 18, 30), SYD),
    ("TNA", "M3 starts (submit on screen-share)", datetime(2026, 10, 22, 19, 0), SYD),
    ("TNA", "Team submit target", datetime(2026, 10, 22, 20, 0), SYD),
    ("TNA", "Wharton Thu working day ends (UNVERIFIED, 5 pm ET)", datetime(2026, 10, 22, 17, 0), NY),
    ("TNA", "Wharton Fri working day starts (UNVERIFIED, 9 am ET)", datetime(2026, 10, 23, 9, 0), NY),
    ("TNA", "Fallback: absolute latest team submit", datetime(2026, 10, 23, 18, 0), SYD),
    ("TNA", "Wharton deadline 5:00 pm ET", datetime(2026, 10, 23, 17, 0), NY),
    ("TNA", "Status re-check", datetime(2026, 10, 24, 9, 0), SYD),
    ("IPS", "US clocks go back (02:00 EDT becomes 01:00 EST = 06:00 UTC)", datetime(2026, 11, 1, 6, 0), UTC),
    ("IPS", "Format gate on exported PDF", datetime(2026, 11, 3, 18, 0), SYD),
    ("IPS", "Last fallback WInS order: Wed 4 Nov ET close", datetime(2026, 11, 4, 16, 0), NY),
    ("IPS", "Text lock", datetime(2026, 11, 5, 9, 0), SYD),
    ("IPS", "Wharton Thu working day starts (UNVERIFIED, 9 am ET)", datetime(2026, 11, 5, 9, 0), NY),
    ("IPS", "M9 starts (submit on screen-share)", datetime(2026, 11, 5, 19, 0), SYD),
    ("IPS", "Team submit target", datetime(2026, 11, 5, 20, 0), SYD),
    ("IPS", "Wharton Thu working day ends (UNVERIFIED, 5 pm ET)", datetime(2026, 11, 5, 17, 0), NY),
    ("IPS", "Wharton Fri working day starts (UNVERIFIED, 9 am ET)", datetime(2026, 11, 6, 9, 0), NY),
    ("IPS", "Fallback: absolute latest team submit", datetime(2026, 11, 6, 18, 0), SYD),
    ("IPS", "WInS market close, trading ends (4:00 pm ET)", datetime(2026, 11, 6, 16, 0), NY),
    ("IPS", "Wharton deadline 5:00 pm ET", datetime(2026, 11, 6, 17, 0), NY),
    ("IPS", "Status re-check", datetime(2026, 11, 7, 9, 30), SYD),
]

DEADLINE = {"TNA": datetime(2026, 10, 23, 17, 0, tzinfo=NY), "IPS": datetime(2026, 11, 6, 17, 0, tzinfo=NY)}


def fmt(dt: datetime) -> str:
    return dt.strftime("%a %d %b %H:%M %Z")


def main() -> None:
    print("| Deliverable | Event | Sydney | US Eastern | UTC | Hours to deadline |")
    print("|---|---|---|---|---|---|")
    for d, label, local, zone in sorted(ROWS, key=lambda r: (r[0] != "TNA", r[2].replace(tzinfo=r[3]).astimezone(UTC))):
        t = local.replace(tzinfo=zone)
        left = (DEADLINE[d] - t) / timedelta(hours=1)
        print(f"| {d} | {label} | {fmt(t.astimezone(SYD))} | {fmt(t.astimezone(NY))} | {fmt(t.astimezone(UTC))} | {left:+.1f} |")
    # offsets around the US change
    for probe in (datetime(2026, 11, 1, 16, 59), datetime(2026, 11, 1, 17, 0)):
        p = probe.replace(tzinfo=SYD)
        gap = (p.utcoffset() - p.astimezone(NY).utcoffset()) / timedelta(hours=1)
        print(f"Sydney {fmt(p)}: Sydney is {gap:.0f} h ahead of New York")


if __name__ == "__main__":
    main()
