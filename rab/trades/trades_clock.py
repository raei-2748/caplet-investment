"""Clock for the trade kit: every time printed in both U.S. Eastern and Sydney time, from the IANA zone database.

WS6, RAB Kit, 2026-09-30 (Sydney). AI-generated (Claude Code) for Team Caplet. No hand arithmetic (PM-07):
Sydney moves to AEDT on Sun 4 Oct 2026; the U.S. moves to EST on Sun 1 Nov 2026 (zoneinfo rules shipped with Python).

Run:  /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/trades_clock.py      (prints a markdown table)
"""
from datetime import datetime
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
SYD = ZoneInfo("Australia/Sydney")

# (label, ET date-time). Deadlines are "no later than 5:00 p.m. ET" (official Guide / SMApply deliverables page);
# trading ends and the portfolio freezes 6 Nov 2026 4:00 p.m. ET (Session Rules, tab WInS Notes, seen 29 Sep).
EVENTS = [
    ("Fri 2 Oct: read WInS bond prices, run refresh_tickets.py (Thursday close and curve are out)",
     datetime(2026, 10, 2, 7, 0, tzinfo=ET)),
    # Longbridge finance_calendar (read-only, 30 Sep 2026): U.S. September employment data 2026-10-02T12:30:00Z.
    # BLS schedule page returned HTTP 403, so the BLS date is UNVERIFIED (WS7 fact audit r2, fixed at Gate D).
    ("Fri 2 Oct: U.S. jobs report (UNVERIFIED with BLS): yields and ETF prices can jump; re-check every ETF price "
     "against its max before ordering", datetime(2026, 10, 2, 8, 30, tzinfo=ET)),
    ("Fri 2 Oct: U.S. market opens (do not trade in the first 15 minutes)", datetime(2026, 10, 2, 9, 30, tzinfo=ET)),
    ("Fri 2 Oct: earliest any order may go in, only if Plan A cannot wait (iBonds normally wait for 10:30)",
     datetime(2026, 10, 2, 9, 45, tzinfo=ET)),
    ("Fri 2 Oct: Plan A starts: iBonds orders after the first hour", datetime(2026, 10, 2, 10, 30, tzinfo=ET)),
    ("Fri 2 Oct: Plan A ends (orders 1-10 in; VT waits for the bond fills)", datetime(2026, 10, 2, 11, 30, tzinfo=ET)),
    ("Fri 2 Oct: Plan B starts (if Plan A was missed): last full trading hours", datetime(2026, 10, 2, 14, 0, tzinfo=ET)),
    ("Fri 2 Oct: Plan B last order (bonds need time before the close)", datetime(2026, 10, 2, 15, 30, tzinfo=ET)),
    ("Fri 2 Oct: U.S. market closes; bond orders fill at end-of-day prices", datetime(2026, 10, 2, 16, 0, tzinfo=ET)),
    ("Mon 5 Oct: first open after Sydney daylight saving starts", datetime(2026, 10, 5, 9, 30, tzinfo=ET)),
    ("Mon 5 Oct: order 11 (VT, Portfolio book) once all five bonds show Filled; after the first hour",
     datetime(2026, 10, 5, 10, 30, tzinfo=ET)),
    ("Mon 5 Oct: VT fallback, last full trading hours (if the first window was missed)",
     datetime(2026, 10, 5, 14, 0, tzinfo=ET)),
    ("Fri 9 Oct: team roster due", datetime(2026, 10, 9, 17, 0, tzinfo=ET)),
    ("Wed 14 Oct: October price check uses this close", datetime(2026, 10, 14, 16, 0, tzinfo=ET)),
    ("Thu 15 Oct: October trade window opens (if a trigger fires)", datetime(2026, 10, 15, 10, 30, tzinfo=ET)),
    ("Tue 20 Oct: October trade window closes (fills before the TN picks)", datetime(2026, 10, 20, 15, 30, tzinfo=ET)),
    ("Fri 23 Oct: Trading Notes Analysis due", datetime(2026, 10, 23, 17, 0, tzinfo=ET)),
    ("Mon 2 Nov: first open after U.S. clocks go back", datetime(2026, 11, 2, 9, 30, tzinfo=ET)),
    ("Fri 6 Nov: trading ends, portfolio freezes", datetime(2026, 11, 6, 16, 0, tzinfo=ET)),
    ("Fri 6 Nov: IPS due", datetime(2026, 11, 6, 17, 0, tzinfo=ET)),
]


def fmt(t):
    return t.strftime("%a %-d %b %Y %-I:%M %p %Z")


def both(t):
    """(ET string, Sydney string) for an aware datetime."""
    return fmt(t.astimezone(ET)), fmt(t.astimezone(SYD))


def table():
    lines = ["| Event | U.S. Eastern | Sydney |", "|---|---|---|"]
    for lab, t in EVENTS:
        e, s = both(t)
        lines.append(f"| {lab} | {e} | {s} |")
    return "\n".join(lines)


if __name__ == "__main__":
    print(table())
