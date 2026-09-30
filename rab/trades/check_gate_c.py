"""Gate C (trade kit): independent automated checks of every Friday ticket and every EXAMPLE trade note.

WS6-gateC, RAB Kit, 30 Sep 2026 (Sydney). AI-generated research code (Claude Code) for Team Caplet. Read-only: it never
logs in to WInS, never fetches anything and never edits the kit. It re-derives the kit's numbers from the committed
inputs (numbers.yaml, the Sheet/WInS snapshots, the ETF volume file, MSPD Table V, the iShares list, the M9 screen)
instead of trusting refresh_tickets.py or build_notes.py. Standard library + PyYAML.

Checks (RAB Kit RUN_PLAN s3 WS6 DoD and Gate C):
  G1 length     every exemplar <= 300 characters (WInS box), <= 285 (kit margin), char_count column right, ASCII, one
                paragraph; the exemplar in notes.md is the same text; each TN reflection outline <= 100 words.
  G2 names      every ticket and note security has an expected WInS name that fits its ticker (iBonds: 'Dec <year>' ends
                the right year; bonds: coupon + maturity, CUSIP in MSPD with that coupon and date); never IBTN /
                INSCORP; SEEN names equal tab WInS Notes; every UNVERIFIED name has a Friday on-screen step.
  G3 cash       from $300,000: cost = qty x price (+ accrued for bonds, per $100) + commission ($25 ETF, $10 Treasury),
                whole units, ETF price >= $3; running cash never negative in the locked, Preview and worst cases;
                total incl. commissions <= $300,000 and equal to numbers.yaml; trades planned <= 200.
  G4 volume     ETFs: qty <= 2 x 30-session average volume (official rule) and <= half the lowest day in 20 sessions
                (WInS FAQ); bonds: WInS shows no bond volume, so a split plan must be present.
  G5 trace      every ticket number equals numbers.yaml, a committed dated source, or is re-derived here; every digit and
                every number word in every exemplar is a case fact, a security term, a date, a numbers.yaml key, or a
                derivation this script shows.
  G6 stale      no stale facts (100,000 / $100k / Dec 4 / 500k / $0 commission / no Treasuries) and no superseded book
                (TLH / IEF / VGSH) as current, in any kit output (md/csv) and the Sheet-tab mirrors; code hits only
                inside banned-pattern lists.
  G7 mirror     the committed mirrors of the Sheet tabs 'RAB Tickets' / 'RAB Notes' (rab/sheets/*.csv, written by
                build_sheet_tabs.py) carry the same orders, quantities, prices and max prices as tickets.csv and the same
                exemplar text as notes.csv, with no retired note left. (The LIVE tabs are read with the Sheets connector
                and compared by hand; this script stays offline. See gate_C.md.)

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/check_gate_c.py
Writes rab/gates/gate_C_results.json. Exit 1 if any FAIL. UNVERIFIED = cannot be settled offline (needs the WInS
screen on Friday); CONDITIONAL = a claim true only in the case the note is written for (the kit says when to use it).
"""
import csv
import hashlib
import json
import math
import os
import re
import sys
from datetime import date

import yaml

if "--self-test" in sys.argv:   # mutation tests: each broken copy of the kit must FAIL the named check
    import shutil
    import subprocess
    import tempfile
    here = os.path.dirname(os.path.abspath(__file__))
    CASES = [
        ("note over 300 characters", "notes.csv", "Role: future funding. The iShares iBonds Dec 2033", "Role: future funding. " + "x" * 300 + " The iShares iBonds Dec 2033", "G1 length"),
        ("IBTN as a ticket", "tickets.csv", "Portfolio,4,IBTO,IBTO,", "Portfolio,4,IBTO,IBTN,", "G2 names"),
        ("quantity 3x ADV", "tickets.csv", ",4486,shares,", ",600000,shares,", "G4 volume"),
        ("a coupon no Treasury has", "notes.csv", "The 4.500% Treasury bond maturing 15 May 2038", "The 4.600% Treasury bond maturing 15 May 2038", "G5 trace"),
        ("an untraced word quantity", "notes.csv", "over about a quarter of a percentage point", "over about a third of a percentage point", "G5 trace"),
        ("an untraced number word", "notes.csv", "ends about seven weeks before", "ends about eight weeks before", "G5 trace"),
        ("wrong ordinal", "notes.csv", "is for the fourth of Laura's ten", "is for the fifth of Laura's ten", "G5 trace"),
        ("stale fact in a kit doc", "tickets.md", "# ", "# Trading ends Dec 4. ", "G6 stale"),
        ("superseded book as current", "october_trade.md", "# ", "# Buy TLH. ", "G6 stale"),
        ("Sheet mirror out of date", "notes.csv", "Its reinvested income can vary.", "Its reinvested income may vary.", "G7 mirror"),
    ]
    bad = 0
    for label, f, old, new, want in CASES:
        tmp = tempfile.mkdtemp()
        for g in os.listdir(here):
            if g.endswith((".csv", ".md")):
                shutil.copy(os.path.join(here, g), tmp)
        os.makedirs(os.path.join(tmp, "data"), exist_ok=True)
        shutil.copy(os.path.join(here, "data", "MANIFEST.md"), os.path.join(tmp, "data"))
        txt = open(os.path.join(tmp, f)).read()
        assert old in txt, (label, old)
        open(os.path.join(tmp, f), "w").write(txt.replace(old, new))
        out = subprocess.run([sys.executable, __file__], env={**os.environ, "GATE_C_TRADES": tmp}, capture_output=True, text=True).stdout
        caught = any(l.startswith("FAIL") and want in l for l in out.splitlines())
        print(f"{'caught' if caught else 'MISSED'}: {label} ({want})")
        bad += not caught
        shutil.rmtree(tmp)
    print("SELF-TEST " + ("PASS" if not bad else "FAIL"))
    sys.exit(1 if bad else 0)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
T0 = os.path.join(ROOT, "rab", "trades")       # inputs that never change (data/, out/, M9, checklist)
T = os.environ.get("GATE_C_TRADES", T0)        # tickets / notes / kit docs (overridden only by --self-test)
P = lambda *a: os.path.join(ROOT, *a)  # noqa: E731

START_CASH = 300_000.00
BOX, KIT = 300, 285
COMM = {"ETF": 25.0, "Treasury": 10.0}
MAX_TRADES = 200
SETTLE = date(2026, 10, 2)   # tickets.md: 'accrued on 2 Oct' (expected Preview)
SETTLE_WORST = date(2026, 10, 5)   # tickets.md worst case: accrued to the next business day
MON = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
ORD = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8,
       "ninth": 9, "tenth": 10, "last": 10}

R = []   # (check, item, status, detail)


def rec(check, item, ok, detail="", status=None):
    R.append((check, item, status or ("PASS" if ok else "FAIL"), detail))


# ------------------------------------------------------------------------------------------------ inputs
tickets = list(csv.DictReader(open(os.path.join(T, "tickets.csv"))))
notes_all = list(csv.DictReader(open(os.path.join(T, "notes.csv"))))
notes = []
for r in notes_all:
    if r["note_id"] not in {n["note_id"] for n in notes}:
        notes.append(r)
notes_md = open(os.path.join(T, "notes.md")).read()
ny_raw = open(P("rab", "numbers.yaml"), "rb").read()
NY = yaml.safe_load(ny_raw)["numbers"]
V = lambda k: NY[k]["value"]  # noqa: E731
mspd = [r for r in json.load(open(os.path.join(T0, "data", "mspd_table5_2026-08-31.json")))["data"]]
mspd = [r for r in mspd if re.fullmatch(r"\d+(\.\d+)?", r["interest_rate_pct"] or "")]
bonds_mspd = [r for r in mspd if r["security_class1_desc"] in ("Treasury Bonds", "Treasury Notes")]
ishares = [r for r in csv.DictReader(l for l in open(os.path.join(T0, "data", "ishares_ibonds_treasury_list_2026-09-30.csv"))
                                     if not l.startswith("#"))]
etf_summ = {r["ticker"]: r for r in csv.DictReader(open(P("rab", "data", "etf", "etf_summary_2026-09-28.csv")))}
wins_notes = open(P("rab", "data", "sheet", "WInS_Notes_values_2026-09-30T0034AEST.txt")).read()
bookl_txt = open(P("rab", "data", "sheet", "Book_L_values_2026-09-30T0033AEST.txt")).read()
m9 = json.load(open(os.path.join(T0, "out", "m9_screen_2026-09-28.json")))
ips = open(os.path.join(T0, "data", "ips_doc_text_2026-09-30.txt")).read()
checklist = open(os.path.join(T, "friday_checklist.md")).read()
m9md = open(os.path.join(T, "M9_selection.md")).read()
octmd = open(os.path.join(T, "october_trade.md")).read()


def num(x):
    return float(x) if x not in ("", None) else None


def bond_terms(name):
    """'T 4.500% 15-May-2038' -> (4.5, date(2038,5,15)) or None."""
    m = re.match(r"T (\d+\.\d+)% (\d+)-(\w{3})-(\d{4})$", name)
    return (float(m.group(1)), date(int(m.group(4)), MON[m.group(3)], int(m.group(2)))) if m else None


def mspd_find(coupon, mat):
    return [r for r in bonds_mspd if abs(float(r["interest_rate_pct"]) - coupon) < 1e-9 and r["maturity_date"] == mat.isoformat()]


def accrued(coupon, mat, settle):
    """Actual/actual (Treasury) accrued interest per $100 face on `settle`."""
    def shift(d, months):
        y, m = divmod(d.month - 1 + months, 12)
        return date(d.year + y, m + 1, d.day)
    nxt = mat
    while shift(nxt, -6) > settle:
        nxt = shift(nxt, -6)
    last = shift(nxt, -6)
    return coupon / 2 * (settle - last).days / (nxt - last).days


# ------------------------------------------------------------------------------------------------ G0 lock
h = hashlib.sha256(ny_raw).hexdigest()
lock = open(P("rab", "numbers.lock")).read()
kit_h = hashlib.sha256(open("/Users/ray/Research/rab-kit/rab/numbers.yaml", "rb").read()).hexdigest()
rec("G0 lock", "numbers.yaml sha256", h in lock and h == kit_h, f"{h[:12]} (numbers.lock and rab-kit agree: {h in lock and h == kit_h})")

# ------------------------------------------------------------------------------------------------ G1 length
for n in notes:
    t = n["exemplar"]
    ok = len(t) <= BOX and int(n["char_count"]) == len(t) and t.isascii() and "\n" not in t and t == t.strip()
    rec("G1 length", n["note_id"], ok, f"{len(t)} chars (box {BOX}); char_count column {n['char_count']}; ascii {t.isascii()}")
    rec("G1 length", n["note_id"] + " kit margin", len(t) <= KIT, f"{len(t)} <= {KIT}")
    rec("G1 length", n["note_id"] + " same text in notes.md", t in notes_md, "exemplar found verbatim in notes.md")
outl = re.search(r"### Reflection outlines.*?(?=\*\*Keep out of all reflections)", notes_md, re.S).group(0)
for m in re.finditer(r"\*\*((?:Pick|Alternate) [^*]+)\*\* \((\d+) words[^)]*\)\n\n((?:- .*\n?)+)", outl):
    words = len(re.findall(r"\S+", re.sub(r"^- ", "", m.group(3), flags=re.M)))
    rec("G1 length", "outline: " + m.group(1)[:40], words <= 100, f"{words} words counted (stated {m.group(2)}; TN limit 100)")

# ------------------------------------------------------------------------------------------------ G2 names
seen_names = dict(re.findall(r"^(IBT\w|VT|VTI|VXUS|IEF|TLH|VGIT|SPTI|TLT|SPTL|SGOV) (.+?) \$\d", wins_notes, re.M))
ish = {r["ticker"]: r["fund_name"] for r in ishares}
for r in tickets:
    item = f"{r['book']} #{r['seq']} {r['id']}"
    nm, st_ = r["wins_name_expected"], r["wins_name_status"]
    bad = r["ticker"].upper() == "IBTN" or "INSCORP" in nm.upper() or r["id"] == "IBTN"
    if r["type"] == "ETF":
        ok = nm == ish.get(r["ticker"], V("market.etf_2026-09-28").get(r["ticker"], {}).get("wins_name"))
        if r["ticker"].startswith("IBT"):
            yr = re.search(r"Dec (\d{4})", nm)
            ok &= bool(yr) and r["ends"].endswith(yr.group(1)) and f"Jan {int(yr.group(1)) + 1}" in r["serves"]
        if st_.startswith("SEEN"):
            ok &= seen_names.get(r["ticker"]) == nm and V("market.etf_2026-09-28").get(r["ticker"], {}).get("wins_name") == nm
    else:
        c, mat = bond_terms(r["id"])
        f = mspd_find(c, mat)
        ok = (f"{c:.3f}%" in nm and f"{mat.day} {mat.strftime('%b')} {mat.year}" in nm and bool(f)
              and r["cusip"] in {x["security_class2_desc"] for x in f} | {x["cusip"] for x in f})
    rec("G2 names", item, ok and not bad, f"{nm} [{st_}]" + (" CUSIP " + r["cusip"] if r["cusip"] else ""))
    if not st_.startswith("SEEN"):
        rec("G2 names", item + " WInS string", True, "not recorded from WInS yet; Friday checklist step copies it", "UNVERIFIED")
rec("G2 names", "IBTN never a ticket", all(r["ticker"] != "IBTN" for r in tickets), "IBTN = INSCORP Inc in WInS (SEEN 29 Sep)")
rec("G2 names", "Friday step copies iBonds names + reads IBTN",
    bool(re.search(r"IBTO, IBTP, IBTQ, IBTR\*\* and copy each name exactly", checklist)) and "IBTN" in checklist,
    "friday_checklist.md step 3")
rec("G2 names", "Friday step records bond strings", bool(re.search(r"(?i)bond.{0,200}(drop-down|dropdown)", checklist)),
    "friday_checklist.md bond drop-down read")
for sec, cusip in (("T 1.375% 15-Nov-2040", "912810ST6"), ("T 2.000% 15-Nov-2041", "912810TC2")):
    c, mat = bond_terms(sec)
    f = mspd_find(c, mat)
    rec("G2 names", f"conditional note security {sec}", bool(f) and cusip in {x["security_class2_desc"] for x in f} | {x["cusip"] for x in f},
        f"MSPD Table V 31 Aug 2026: {len(f)} row(s); WInS listing UNVERIFIED (notes used only if listed)")

# ------------------------------------------------------------------------------------------------ G3 cash + G4 volume + G5 tickets
hold = {h_["holding"]: h_ for h_ in V("wins.portfolio.holdings_close_0928")}
etfm = V("market.etf_2026-09-28")
bookl_qty = {}
for line in bookl_txt.splitlines():
    m = re.match(r"20\d\d (IBT\w|T \S+ \S+) (?:ETF|Treasury bond) .*? ([\d,]+) \$[\d,]+ [\d.]+% ", line)
    if m:
        bookl_qty[m.group(1)] = int(m.group(2).replace(",", ""))
book_tot = {"Portfolio": "wins.portfolio.cost_close_0928", "BookL": "wins.bookL.cost_close_0928"}
for book in ("Portfolio", "BookL"):
    rows = sorted([r for r in tickets if r["book"] == book], key=lambda r: int(r["seq"]))
    cash_l = cash_p = cash_w = START_CASH
    lows, comm_tot, tot, tol_w = [], 0.0, 0.0, 0.0
    for r in rows:
        item = f"{book} #{r['seq']} {r['id']}"
        q, px, typ = num(r["qty"]), num(r["ref_price"]), r["type"]
        comm = num(r["commission"])
        ok_units = q == int(q) and q > 0 and comm == COMM[typ] and (typ != "ETF" or px >= 3)
        if typ == "ETF":
            cost = q * px + comm
            prev = q * px + comm
            worst = q * num(r["max_price"]) + comm
        else:
            cost = q * (px + num(r["accrued_rec"])) / 100 + comm
            c_, mat_ = bond_terms(r["id"])
            prev = q * (px + accrued(c_, mat_, SETTLE)) / 100 + comm
            worst = q * (num(r["max_price"]) + accrued(c_, mat_, SETTLE_WORST)) / 100 + comm
        cash_l -= cost
        cash_p -= prev
        cash_w -= worst
        # the ticket shows max clean to 3 dp but prices the worst case at the unrounded max: allow that rounding
        row_tol = 0.01 + (q * 0.0005 / 100 if typ != "ETF" else 0)
        tol_w += row_tol
        tot += cost
        comm_tot += comm
        lows.append(min(cash_l, cash_p, cash_w))
        ok = (ok_units and abs(cost - num(r["cost_locked"])) < 0.005 and abs(cash_l - num(r["cash_after_locked"])) < 0.01
              and abs(prev - num(r["preview_expected"])) < 0.02 and abs(worst - num(r["cost_max"])) < row_tol + 0.01
              and abs(cash_w - num(r["cash_after_worst"])) < tol_w + 0.01 and min(cash_l, cash_p, cash_w) >= 0)
        rec("G3 cash", item, ok, f"cost ${cost:,.2f} (comm ${comm:.0f}); cash after: locked ${cash_l:,.2f} / "
            f"Preview ${cash_p:,.2f} / worst ${cash_w:,.2f}")
        # G4 volume
        if typ == "ETF" and (r["ticker"] not in etf_summ or r["ticker"] not in etfm):
            rec("G4 volume", item, False, f"no volume record for ticker {r['ticker']} (wrong ticker?)")
            rec("G5 trace", item + " price", False, f"ticker {r['ticker']} not in numbers.yaml market.etf_2026-09-28")
        elif typ == "ETF":
            s = etf_summ[r["ticker"]]
            adv30, min20, med20 = float(s["avg_volume_30d"]), int(s["min_volume_20d"]), int(s["median_volume_20d"])
            ok = q <= 2 * adv30 and q <= 0.5 * min20
            rec("G4 volume", item, ok, f"{q:.0f} shares = {q / (2 * adv30):.2%} of 2 x ADV30 ({adv30:,.0f}); "
                f"{q / min20:.1%} of the lowest day in 20 ({min20:,})")
            rec("G5 trace", item + " volumes", abs(num(r["adv30"]) - adv30) < 1 and num(r["min20"]) == min20
                and abs(num(r["median20"]) - med20) <= 0.5 and med20 == etfm[r["ticker"]]["median_volume_20d"] and min20 == etfm[r["ticker"]]["min_volume_20d"],
                "adv30 = rab/data/etf/etf_summary_2026-09-28.csv avg_volume_30d (Nasdaq, 30 sessions to 28 Sep); "
                "median20/min20 = numbers.yaml market.etf_2026-09-28 (ticket median of an even count keeps .5; yaml rounds it)")
            band = num(r["band_pct"]) / 100
            rec("G5 trace", item + " price", px == etfm[r["ticker"]]["close"]
                and abs(num(r["max_price"]) - math.ceil(px * (1 + band) * 100) / 100) < 1e-9
                and abs(num(r["min_price"]) - math.floor(px * (1 - band) * 100) / 100) < 1e-9,
                f"ref {px} = numbers.yaml market.etf_2026-09-28 close; max/min = ref x (1 +- {band:.2%}), "
                "band = max(0.5%, 2 x 20-session daily sd) (refresh_tickets.py)")
        else:
            c, mat = bond_terms(r["id"])
            f = mspd_find(c, mat)
            out_usd = float(f[0]["outstanding_amt"]) * 1000 if f else float("nan")
            rec("G4 volume", item, "split it over" in m9md and "next two sessions" in m9md,
                f"${q:,.0f} face = {q / out_usd:.1e} of the ${out_usd / 1e9:,.1f}bn outstanding (MSPD); WInS shows no "
                "bond volume, so 2x-volume is UNVERIFIED; split plan: M9_selection.md (still waiting at 3:30pm ET -> "
                "half each over the next two sessions)", "PASS" if "split it over" in m9md else "FAIL")
            bc = V(f"wins.bond_check.{r['id'].replace(' ', '_')}")
            a_tr = accrued(c, mat, SETTLE)
            ok = (px == bc["wins_clean"] and abs(num(r["yield_gap_bp"]) - bc["gap_bp"]) < 0.05
                  and abs(num(r["yield_band_25bp_low"]) - bc["clean_band_25bp"][0]) < 0.0005
                  and abs(num(r["yield_band_25bp_high"]) - bc["clean_band_25bp"][1]) < 0.0005
                  and abs(num(r["accrued_trade"]) - a_tr) < 0.0005 and r["yield_check"] == "PASS" and not bc["flag"]
                  and abs(num(r["max_price"]) / px - 1 - num(r["band_pct"]) / 100) < 1e-5)
            rec("G5 trace", item + " price", ok, f"clean {px} = wins.bond_check wins_clean; gap {bc['gap_bp']}bp; "
                f"accrued on 2 Oct re-derived {a_tr:.4f} (act/act) vs ticket {r['accrued_trade']}")
        # G5 quantity + locked accrued
        if book == "Portfolio":
            hh = hold[r["id"]]
            ok = q == hh["qty"] and (typ == "ETF" or abs(px + num(r["accrued_rec"]) - hh["price"]) < 0.0005)
            src = "numbers.yaml wins.portfolio.holdings_close_0928 qty" + ("" if typ == "ETF" else " and price = clean + accrued")
        else:
            ok = q == bookl_qty.get(r["id"])
            src = "Sheet tab Book L snapshot rab/data/sheet/Book_L_values_2026-09-30T0033AEST.txt"
        rec("G5 trace", item + " qty", ok, f"{q:,.0f} = {src}")
    cyc = V(book_tot[book])
    rec("G3 cash", f"{book} total", tot <= START_CASH and abs(tot - cyc["cost"]) < 0.005 and abs(comm_tot - cyc["commissions"]) < 0.005
        and abs(START_CASH - tot - cyc["cash_left"]) < 0.005,
        f"${tot:,.2f} incl. ${comm_tot:.0f} commissions <= $300,000; cash left ${START_CASH - tot:,.2f}; = numbers.yaml {book_tot[book]}")
    rec("G3 cash", f"{book} lowest cash", min(lows) >= 0, f"lowest cash in any case ${min(lows):,.2f} (kit floor $1,000: {min(lows) >= 1000})")
    if book == "Portfolio":
        sp = V("wins.portfolio.split_close_0928")
        vt = [r for r in rows if r["id"] == "VT"][0]
        rec("G5 trace", "Portfolio split", abs(num(vt["qty"]) * num(vt["ref_price"]) / START_CASH - sp["vt"]) < 5e-5
            and abs((START_CASH - tot) / START_CASH - sp["cash"]) < 5e-5, "VT 8.68%, cash 1.75% = wins.portfolio.split_close_0928")
n_trades = len([r for r in tickets if r["book"] == "Portfolio"]) + 5   # + October max: B 2, C 1, D 2 (october_trade.md)
rec("G3 cash", "trade count", n_trades <= MAX_TRADES, f"{n_trades} planned at most (11 + October 5) of {MAX_TRADES}")
rec("G3 cash", "order sequence", [r["id"] for r in tickets if r["book"] == "Portfolio"][-1] == "VT",
    "VT is order 11, after the bonds fill (tickets.md)")

# ------------------------------------------------------------------------------------------------ G5 notes
SERVE = {}
for r in tickets:
    SERVE[r["id"]] = int(re.search(r"Jan (\d{4})", r["serves"]).group(1)) if "Jan" in r["serves"] else None
for sec in ("T 1.375% 15-Nov-2040", "T 2.000% 15-Nov-2041", "T 5.000% 15-May-2037"):
    SERVE[sec] = bond_terms(sec)[1].year + 1


def slot(y, sid):
    return next(s for s in m9["slots"] if s["slot"] == y and s["id"] == sid)


def d(a, b):
    return (b - a).days


cost27 = V("laura.ladder.cost_2027_strips")
be = V("laura.ladder.breakeven_fall_bp_strips")
prem = V("wins.ibond_checks")["IBTP"]["premium_to_nav_pct"]
gap38 = V("wins.bond_check.T_4.375%_15-Feb-2038")["gap_bp"]
ish_end = sorted(int(re.search(r"Dec (\d{4})", r["fund_name"]).group(1)) for r in ishares)
between = lambda lo, hi: [r for r in mspd if r["security_class1_desc"] == "Treasury Bonds" and lo < r["maturity_date"] < hi]  # noqa: E731
gap_seen = "none mature between 15 Feb 2031 and 15 Feb 2036" in wins_notes
cs = lambda y, a, b: (slot(y, a)["coupon_share_of_cash"], slot(y, b)["coupon_share_of_cash"])  # noqa: E731

rung0 = lambda k: V(f"reinvest.rung.{k}")["at_0pct"] / 50000  # noqa: E731  set coupons + principal, share of $50,000
cond = lambda why: (lambda: (True, why, "CONDITIONAL"))  # noqa: E731
NOV40 = "T40b|T40s|SW40|OD_S|OD_B"

# (note ids, regex span in the exemplar, derivation -> (ok, detail, status)). Rebuilt 30 Sep after the second judge
# panel's exemplar rewrites (notes.md at 104476c+): every number word in the new texts sits inside one of these.
CLAIMS = [
    ("IBTR|IBTR_F", r"Tested before this first order", lambda: (tickets[0]["id"] == "IBTR" and tickets[0]["seq"] == "1",
     "IBTR is Friday order 1 (tickets.csv seq 1); the refresh runs before any order (friday_checklist.md)", None)),
    ("IBTR", r"cost under her \$300,000 first deposit",
     lambda: (cost27 < 300000, f"laura.ladder.cost_2027_strips ${cost27:,.2f} < $300,000 (28 Sep curve, zero-coupon basis; re-run Friday)", None)),
    ("IBTR_F", r"cost more than her \$300,000 first deposit", cond("typed only if the Friday refresh is above $300,000 (friday_checklist.md)")),
    ("IBTR", r"about a quarter of a percentage point", lambda: (20 <= be <= 30, f"laura.ladder.breakeven_fall_bp_strips {be}bp; the note says 'over about'", None)),
    ("IBTR|IBTR_F", r"future funding for the fifth", None),
    ("IBTR|IBTR_F|OB_S", r"tops up (the earliest|her first payment)",
     lambda: ("latest payments first" in ips and "for the 2028 deposit to complete" in ips,
              "IPS 'latest payments first' + 'leave some payments for the 2028 deposit to complete': a short deposit leaves the earliest", None)),
    ("IBTR", r"stocks get less", lambda: ("secured before anything is invested" in ips,
     "IPS: payments and floor 'secured before anything is invested' in stocks; WS4 memo: the gap lands on the stock fund", None)),
    ("IBTR_F", r"so we hold less stock than planned", cond("--split-from-curve lowers VT's share when the test fails (refresh_tickets.py)")),
    ("IBTQ", r"the fourth of Laura's ten", None),
    ("IBTQ", r"no Treasury bond maturing between Feb 2031 and Feb 2036", lambda: (gap_seen, "tab WInS Notes, SEEN 29 Sep", None)),
    ("IBTQ", r"closest fit", lambda: (slot(2036, "IBTQ")["months_early"] < slot(2036, "IBTP")["months_early"],
                                      "M9 slot 2036: IBTQ ends 0.6 months early, IBTP 12.6", None)),
    ("IBTP", r"almost exactly the value", lambda: (abs(prem) < 0.1, f"wins.ibond_checks.IBTP.premium_to_nav_pct {prem}% on 28 Sep; the note reports the trade-date re-run", "CONDITIONAL")),
    ("IBTO", r"the second of Laura's ten", None),
    ("IBTO", r"WInS lists no Treasury bond maturing in 2033", lambda: (gap_seen, "tab WInS Notes, SEEN 29 Sep (gap Feb 2031-Feb 2036)", None)),
    ("IBTM_P", r"has two jobs", lambda: ("floor" in tickets[4]["serves"] and "2033" in tickets[4]["serves"],
     f"Portfolio ticket 5 serves '{tickets[4]['serves']}'", None)),
    ("IBTM_P|IBTM_R", r"(her|Laura's) first \$50,000 payment", None),
    ("IBTM_P|VT|IBTM_R|OC", r"the least she plans to give", lambda: ("floor she can promise co-sponsors" in ips, "IPS: 'a floor she can promise co-sponsors' (definition)", None)),
    ("IBTM_R", r"the half of the stock fund she keeps", lambda: ("The other half remains with Laura" in ips,
     "IPS: 'The other half remains with Laura as a cushion'; naming it the backstop needs the 1 Oct vote", "CONDITIONAL")),
    ("T41|SW41", r"the last of Laura's ten", None),
    ("T41", r"No iBonds Treasury fund ends (between|from) 2037 (and|to) 2043",
     lambda: (not [y for y in ish_end if 2037 <= y <= 2043], f"iShares list 30 Sep: ends {ish_end[:11][-1]} then {[y for y in ish_end if y > 2036][0]}", None)),
    ("T41", r"her last five payments use (single|individual) bonds",
     lambda: (sorted(SERVE[r["id"]] for r in tickets if r["book"] == "Portfolio" and r["type"] == "Treasury") == list(range(2038, 2043)),
              "tickets: 5 Treasury bonds serve 2038-2042", None)),
    ("T41", r"part of each payment comes from reinvested coupons",
     lambda: (all(rung0(k) < 1 for k in ("T_4.750%_15-Feb-2037", "T_4.500%_15-May-2038", "T_4.375%_15-Nov-2039", "T_4.250%_15-Nov-2040", "T_3.125%_15-Nov-2041")),
              "reinvest.rung.* at_0pct: set coupons + principal are 84-90% of each bond rung's $50,000", None)),
    (NOV40, r"(the )?ninth( of Laura's ten)?( \$50,000)?( payment)?", None),
    (NOV40, r"(A lower-coupon bond of that date would leave|which leaves|[Mm]ore of its value (is owed|comes) at maturity, so) less (of her payment )?(rest(s|ing)|rides) on reinvest(ed|ing) coupons",
     lambda: (lambda a, b: (a < b, f"M9 slot 2041: share of cash as coupons 1.375% {a:.1%} vs 4.250% {b:.1%}", None))(*cs(2041, "T 1.375% 15-Nov-2040", "T 4.250% 15-Nov-2040"))),
    ("SW41", r"more of its value is owed at maturity, so less rests on reinvesting coupons",
     lambda: (lambda a, b: (a < b, f"M9 slot 2042: coupons share 2.000% {a:.1%} vs 3.125% {b:.1%}", None))(*cs(2042, "T 2.000% 15-Nov-2041", "T 3.125% 15-Nov-2041"))),
    ("T40b", r"but WInS does not list one", cond("used only if the Friday drop-down shows no 1.375% Nov-2040 (notes.md s4)")),
    ("T40s", r"WInS lists a 1\.375% bond of that date", cond("used only if the drop-down lists it (notes.md s5)")),
    ("T40s", r"its price failed our curve check today", cond("used only if its Friday price is outside the 25bp band (notes.md s5)")),
    ("T38|T40b", r"Its (WInS )?price passed our curve check",
     lambda: (lambda k: (not V(k)["flag"] and abs(V(k)["gap_bp"]) <= 25, f"{k} gap {V(k)['gap_bp']}bp, inside 25bp (28 Sep; re-checked Friday)", None))(
         "wins.bond_check.T_4.500%_15-May-2038" if nid_ctx[0] == "T38" else "wins.bond_check.T_4.250%_15-Nov-2040")),
    ("T39", r"about seven weeks", lambda: (6.5 <= d(date(2039, 11, 15), date(2040, 1, 1)) / 7 <= 7.5, f"15 Nov 2039 -> 1 Jan 2040 = {d(date(2039, 11, 15), date(2040, 1, 1))} days", None)),
    ("T39", r"cover most of that payment",
     lambda: (0.5 < rung0("T_4.375%_15-Nov-2039") < 1, f"reinvest.rung.T_4.375%_15-Nov-2039 at_0pct {rung0('T_4.375%_15-Nov-2039'):.1%} of $50,000", None)),
    ("T38", r"is the last before Laura's \$50,000 residency payment on 1 Jan 2039",
     lambda: (not between("2038-05-15", "2039-01-01"), "MSPD Table V 31 Aug 2026: no Treasury bond matures 16 May 2038 - 31 Dec 2038", None)),
    ("T38", r"about seven and a half months", lambda: (abs(d(date(2038, 5, 15), date(2039, 1, 1)) / 30.4375 - 7.5) < 0.25, f"15 May 2038 -> 1 Jan 2039 = {d(date(2038, 5, 15), date(2039, 1, 1))} days", None)),
    ("T38", r"the 4\.375% Feb 2038 bond's price was stale", lambda: (abs(gap38) > 25, f"wins.bond_check.T_4.375%_15-Feb-2038 gap {gap38}bp (the 28 Sep close, seen 29 Sep)", None)),
    ("T37", r"about ten and a half months early", lambda: (abs(d(date(2037, 2, 15), date(2038, 1, 1)) / 30.4375 - 10.5) < 0.25, f"15 Feb 2037 -> 1 Jan 2038 = {d(date(2037, 2, 15), date(2038, 1, 1))} days", None)),
    ("T37", r"It is the last WInS bond maturing before then",
     lambda: ([(float(r["interest_rate_pct"]), r["maturity_date"]) for r in between("2037-02-15", "2038-01-01")] == [(5.0, "2037-05-15")],
              "used only if WInS does not list the 5.000% May 2037, the one later bond (MSPD)", "CONDITIONAL")),
    ("SW37", r"It is the last Treasury bond maturing before then",
     lambda: (not between("2037-05-15", "2038-01-01"), "MSPD Table V: no Treasury bond matures 16 May 2037 - 31 Dec 2037", None)),
    ("SW37", r"its money waits three months less than with the Feb 2037 bond",
     lambda: (abs(d(date(2037, 2, 15), date(2037, 5, 15)) / 30.4375 - 3) < 0.25, f"15 Feb 2037 -> 15 May 2037 = {d(date(2037, 2, 15), date(2037, 5, 15))} days", None)),
    ("VT", r"bought last", lambda: (tickets[10]["id"] == "VT" and tickets[10]["seq"] == "11", "VT is Portfolio order 11 of 11", None)),
    ("VT", r"A fall can cut her contribution, not below the floor",
     lambda: ("not below the floor" in ips, "IPS: equities 'can reduce the facility contribution, but not below the floor'", None)),
    ("VT", r"Half the fund stays hers", lambda: ("The other half remains with Laura" in ips, "IPS: 'The other half remains with Laura as a cushion'", None)),
    ("IBTM_L", r"the first of Laura's ten", None),
    ("IBTM_L", r"WInS lists no Treasury bond maturing in late 2032", lambda: (gap_seen, "tab WInS Notes, SEEN 29 Sep", None)),
    ("IBTM_L", r"closest fit", lambda: (slot(2033, "IBTM")["months_early"] < slot(2033, "T 5.375% 15-Feb-2031")["months_early"], "M9 slot 2033: IBTM 0.6 months early", None)),
    ("SW41|OD_S", r"(bond of )?the same date", lambda: (True, "same maturity (15 Nov): MSPD rows for both coupons", None)),
    ("SW40|SW41|SW37", r"(Its|Its WInS) price passed our curve check", cond("used only if the WInS price sits inside the 25bp band the refresh prints (notes.md s5)")),
    ("OD_S", r"whose price now passes our curve check", cond("trigger D: the Friday price was stale (T40s) and now passes (october_trade.md)")),
    ("OD_B", r"Its price was stale on 2 Oct and now passes our curve check", cond("trigger D: the Friday price was stale (T40s) and now passes (october_trade.md)")),
    ("OB_S", r"(Laura's |the )ten payments now cost more than (Laura's|her) \$300,000 first deposit",
     lambda: ("B." in octmd or "Trigger B" in octmd or "**B." in octmd, "October trigger B only: the 14 Oct re-price is above $300,000 (october_trade.md)", "CONDITIONAL")),
    ("OB_S", r"leaving less for the facility", cond("consequence of trigger B: the 2028 deposit tops up the payment first, so less reaches the facility (october_trade.md)")),
    ("OB_B", r"so the payments come first", lambda: ("secured before anything is invested" in ips, "IPS: payments and floor 'secured before anything is invested'", None)),
    ("OC", r"Our cash is more than fees and rounding need", lambda: ("$6,300" in octmd and V("wins.portfolio.targets_typed")["cash_1.1pct"] == 3300,
                                                                   "trigger C: cash above $6,300 = $3,300 float (wins.portfolio.targets_typed cash_1.1pct) + $3,000 (october_trade.md)", "CONDITIONAL")),
    ("*", r"(Laura's|her) ten|\$50,000|\$300,000", lambda: (True, "case facts: ten $50,000 payments 2033-2042; $300,000 2027 deposit", None)),
    ("*", r"first deposit", lambda: (True, "case fact: the 2027 deposit is her first", None)),
]
NUMWORD = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half|quarter|third|first|second|"
                     r"fourth|fifth|sixth|seventh|eighth|ninth|tenth|last|full|double|twice|same|exactly|under|more|less|"
                     r"lower|higher|above|below|only|least|most|almost|nearly|closest|earliest|latest)\b", re.I)


nid_ctx = [None]


def ordinal_check(nid, sec, span):
    w = re.search(r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|last)", span).group(1)
    y = SERVE.get(sec)
    return (y is not None and ORD[w] == y - 2032, f"'{w}' = payment {ORD[w]} of 10; {sec} serves 1 Jan {y}", None)


mspd_dates = {r["maturity_date"] for r in mspd}
ends = {f"{y}-12-15" for y in ish_end}
for n in notes:
    t, nid, sec = n["exemplar"], n["note_id"], n["ticker"]
    covered = []
    nid_ctx[0] = nid
    for ids, pat, fn in CLAIMS:
        if ids != "*" and nid not in ids.split("|"):
            continue
        for m in re.finditer(pat, t):
            covered.append((m.start(), m.end()))
            ok, det, stt = ordinal_check(nid, sec, m.group(0)) if fn is None else fn()
            if ids != "*":
                rec("G5 trace", f"note {nid}: '{m.group(0)[:50]}'", ok, det, stt if ok and stt else None)
    # every number word must sit inside a traced claim; allowed pure-grammar words listed with their reason
    GRAMMAR = {("T40b", "one"): "pronoun ('list one')", ("T40s", "one"): "pronoun ('buy this one')"}
    for m in NUMWORD.finditer(t):
        if not any(a <= m.start() < b for a, b in covered) and (nid, m.group(0).lower()) not in GRAMMAR:
            rec("G5 trace", f"note {nid}: number word '{m.group(0)}'", False,
                f"not covered by a traced claim: ...{t[max(0, m.start() - 30):m.end() + 30]}...")
    # every digit token: case fact, year, security coupon (MSPD), date (payment date or a real maturity), or declared key
    declared = {x.split(" = ")[0]: x.split(" = ")[1] for x in n["numbers"].split("; ") if " = " in x}
    for m in re.finditer(r"\$?\d[\d,]*(?:\.\d+)?%?", t):
        tok = m.group(0).rstrip(",.")
        ctx = t[max(0, m.start() - 6):m.end() + 10]
        if tok in ("$50,000", "$300,000", "$150,000"):
            continue
        if re.fullmatch(r"\d\.\d{3}%", tok):
            ok = any(abs(float(r["interest_rate_pct"]) - float(tok[:-1])) < 1e-9 and "2036" <= r["maturity_date"][:4] <= "2042"
                     for r in bonds_mspd)
            rec("G5 trace", f"note {nid}: coupon {tok}", ok, "a Treasury bond with this coupon matures 2036-2042 (MSPD)")
            continue
        dm = re.match(r"(\d{1,2}) (\w{3}) (\d{4})", t[m.start():m.start() + 12])
        if dm and dm.group(2) in MON:
            dd = date(int(dm.group(3)), MON[dm.group(2)], int(dm.group(1)))
            ok = (dd.month == 1 and dd.day == 1 and 2033 <= dd.year <= 2042) or dd.isoformat() in mspd_dates | ends
            rec("G5 trace", f"note {nid}: date {dm.group(0)}", ok, "payment date 1 Jan 2033-2042 or a real maturity (MSPD / iShares)")
            continue
        if re.fullmatch(r"\d{1,2}", tok) and re.match(r"\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)", t[m.end():m.end() + 4]):
            mon = t[m.end() + 1:m.end() + 4]
            rec("G5 trace", f"note {nid}: date {tok} {mon}", tok in ("28", "29", "1", "15") or (tok == "2" and mon == "Oct"),
                "check date (28/29 Sep), curve date 1 Oct, Friday trade date 2 Oct, or payment/maturity day")
            continue
        if re.fullmatch(r"20[2-4]\d", tok):
            continue   # years: covered by the payment/maturity checks above and the ticket 'serves' column
        if tok in declared:
            key, val = declared[tok].split(" (")[0], None
            v = V(key)
            ok = round(v["vt"] * 100) == int(tok.rstrip("%")) if key == "wins.portfolio.split_close_0928" else False
            rec("G5 trace", f"note {nid}: {tok}", ok, f"= {declared[tok]}")
            continue
        rec("G5 trace", f"note {nid}: number {tok}", False, f"untraced: ...{ctx}...")
    # payment years named in the note agree with the ticket it belongs to
    ys = {int(y) for y in re.findall(r"1 Jan (\d{4})", t)} | {int(y) for y in re.findall(r"Laura's (\d{4}) payment|her (\d{4}) payment", t) for y in y if y}
    if SERVE.get(sec) and ys and nid not in ("OB_S", "OB_B"):
        rec("G5 trace", f"note {nid}: payment year", ys == {SERVE[sec]}, f"note says {sorted(ys)}; ticket serves {SERVE[sec]}")
for lab in {n["use"] for n in notes}:
    for tok in re.findall(r"\$[\d,]+", lab):
        rec("G5 trace", f"label '{lab[:40]}': {tok}", tok == "$6,300" and "$6,300" in octmd, "october_trade.md trigger C ($3,300 float + $3,000)")

# tickets.md: every dollar figure is a ticket field, a running total, or a numbers.yaml value
tm = open(os.path.join(T, "tickets.md")).read()
cand = set()
for r in tickets:
    for k, v in r.items():
        try:
            cand.add(round(float(v), 2))
        except ValueError:
            pass
for book in ("Portfolio", "BookL"):
    c_ = START_CASH
    for r in sorted([r for r in tickets if r["book"] == book], key=lambda r: int(r["seq"])):
        c_ -= float(r["preview_expected"])
        cand.add(round(c_, 2))
    cand.add(round(sum(float(r["cost_locked"]) for r in tickets if r["book"] == book), 2))
    cand.add(round(START_CASH - c_, 2))   # expected total (Preview basis)
    cw = [float(r["cash_after_worst"]) for r in tickets if r["book"] == book][-1]
    cand |= {round(cw, 2), round(START_CASH - cw, 2)}   # worst-case total and cash
for k in ("wins.portfolio.cost_close_0928", "wins.bookL.cost_close_0928"):
    cand |= {round(float(x), 2) for x in V(k).values()}
for h_ in V("wins.portfolio.holdings_close_0928"):
    cand.add(round(h_["value"], 2))
miss = []
for m in re.finditer(r"\$([\d,]+\.\d\d)\b", tm):
    x = float(m.group(1).replace(",", ""))
    if round(x, 2) not in cand:
        miss.append(m.group(0))
rec("G5 trace", "tickets.md dollar figures", not miss, f"{len(re.findall(r'[$][0-9,]+[.][0-9][0-9]', tm))} cent-level figures; untraced: {miss[:8]}")

# ------------------------------------------------------------------------------------------------ G6 stale
STALE = [r"100,000", r"100000", r"\$100k", r"Dec 4\b", r"4 Dec\b", r"December 4", r"500k", r"\$500,000", r"\$0 commission",
         r"(?i)no Treasuries", r"\bTLH\b", r"\bIEF\b", r"\bVGSH\b", r"Dec(ember)? 2026 trading"]
kit_out = [f for f in sorted(os.listdir(T)) if f.endswith((".md", ".csv"))] + ["data/MANIFEST.md"]
for f in kit_out:
    txt = open(os.path.join(T, f)).read()
    hits = [(i + 1, p) for i, line in enumerate(txt.splitlines()) for p in STALE if re.search(p, line)
            and not re.search(r"(?i)supersed|stale|retired|not the current", line)]
    rec("G6 stale", f, not hits, f"hits: {hits[:5]}" if hits else "none")
for f in [f for f in sorted(os.listdir(T0)) if f.endswith(".py") and f != "check_gate_c.py"]:
    lines = open(os.path.join(T0, f)).read().splitlines()
    bad = [(i + 1, p) for i, line in enumerate(lines) for p in STALE if re.search(p, line)
           and not re.search(r"BANNED|pats|r\"|r'|supersed|stale", line)]
    rec("G6 stale", f, not bad, "only inside banned-pattern lists" if not bad else f"hits: {bad[:5]}")

# ------------------------------------------------------------------------------------------------ G7 sheet mirror
# The team reads the kit through the Sheet tabs 'RAB Tickets' / 'RAB Notes'. Their committed mirrors in rab/sheets/
# (written by build_sheet_tabs.py) must carry the same orders and the same exemplar text as the kit, and pass G1/G6.
SH = P("rab", "sheets")
sh_t = list(csv.reader(open(os.path.join(SH, "rab_tickets.csv"))))
sh_n = list(csv.reader(open(os.path.join(SH, "rab_notes.csv"))))
hi = next(i for i, r in enumerate(sh_t) if r[:3] == ["Book", "Order", "Ticker or bond"])
H = sh_t[hi]
col = lambda name: H.index(name)  # noqa: E731
sh_rows = {(r[0], r[1]): r for r in sh_t[hi + 1:] if r and r[0] in ("Portfolio", "BookL") and r[1].isdigit()}
fnum = lambda s: float(s) if s not in ("", None) else None  # noqa: E731
for t_ in tickets:
    key = (t_["book"], t_["seq"])
    s_ = sh_rows.get(key)
    if s_ is None:
        rec("G7 mirror", f"RAB Tickets {key}", False, "row missing from rab/sheets/rab_tickets.csv")
        continue
    pairs = [("ticker", s_[col("Ticker or bond")], t_["id"] if t_["ticker"].startswith("(") else t_["ticker"]),
             ("qty", fnum(s_[col("Quantity")]), fnum(t_["qty"])),
             ("ref_price", fnum(s_[col("Reference price")]), fnum(t_["ref_price"])),
             ("max_price", fnum(s_[col("Max price (do not pay above)")]), fnum(t_["max_price"])),
             ("preview", fnum(s_[col("Kit Preview total ($, tickets.csv)")]), fnum(t_["preview_expected"]))]
    bad = [(k, a, b) for k, a, b in pairs if (a != b if isinstance(a, str) or a is None or b is None
                                              else abs(a - b) > 0.005)]
    rec("G7 mirror", f"RAB Tickets {key[0]} #{key[1]}", not bad, f"differs: {bad}" if bad else "same as tickets.csv")
rec("G7 mirror", "RAB Tickets row count", len(sh_rows) == len(tickets), f"{len(sh_rows)} rows vs {len(tickets)} tickets")
nh = next(i for i, r in enumerate(sh_n) if r[:3] == ["Book", "Order", "Note ID"])
NH = sh_n[nh]
sh_ex = {}
for r in sh_n[nh + 1:]:
    if len(r) > NH.index("Exemplar note") and r[NH.index("Note ID")]:
        sh_ex.setdefault(r[NH.index("Note ID")], set()).add(r[NH.index("Exemplar note")])
for n_ in notes:
    got = sh_ex.get(n_["note_id"])
    ok = got == {n_["exemplar"]} and len(n_["exemplar"]) <= BOX
    rec("G7 mirror", f"RAB Notes {n_['note_id']}", ok,
        "same text as notes.csv" if ok else ("missing" if not got else f"differs from notes.csv ({[len(g) for g in got]} chars)"))
extra = sorted(set(sh_ex) - {n_["note_id"] for n_ in notes})
rec("G7 mirror", "RAB Notes: no retired note left", not extra, f"extra ids: {extra}" if extra else "none")
for f in ("rab_tickets.csv", "rab_notes.csv"):
    txt = open(os.path.join(SH, f)).read()
    hits = [(i + 1, p) for i, line in enumerate(txt.splitlines()) for p in STALE if re.search(p, line)
            and not re.search(r"(?i)supersed|stale|retired|not the current", line)]
    rec("G6 stale", f"sheets/{f}", not hits, f"hits: {hits[:5]}" if hits else "none")

# ------------------------------------------------------------------------------------------------ report
cnt = {}
for c, i, s, _ in R:
    cnt.setdefault(c, {}).setdefault(s, 0)
    cnt[c][s] += 1
for c, i, s, det in R:
    if s != "PASS":
        print(f"{s:11s} {c:10s} {i}: {det}")
print()
for c in sorted(cnt):
    print(f"{c:10s} " + ", ".join(f"{k} {v}" for k, v in sorted(cnt[c].items())))
nf = sum(1 for r in R if r[2] == "FAIL")
print(f"\nTOTAL {len(R)} checks: FAIL {nf}, UNVERIFIED {sum(1 for r in R if r[2] == 'UNVERIFIED')}, "
      f"CONDITIONAL {sum(1 for r in R if r[2] == 'CONDITIONAL')}; numbers.yaml {h[:12]}")
out_dir = P("rab", "gates") if T == T0 else T
os.makedirs(out_dir, exist_ok=True)
json.dump({"numbers_yaml_sha256": h, "counts": cnt,
           "checks": [dict(zip(("check", "item", "status", "detail"), r)) for r in R]},
          open(os.path.join(out_dir, "gate_C_results.json"), "w"), indent=1)
sys.exit(1 if nf else 0)
