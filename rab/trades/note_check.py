"""Check a team-written WInS trade note before it is pasted into WInS. It never writes or rewrites text.

WS6-notes, RAB Kit, 30 Sep 2026 (Sydney). AI-generated tool (Claude Code) for Team Caplet. Standard library only.

What it checks (rules in note_rules.py; sources there):
  FAIL  over 300 characters (the WInS box cuts silently), non-ASCII characters, more than one paragraph,
        a banned word, or phrase overlap of 50% or more with an EXAMPLE note (PM-13: rewrite, or disclose the
        exemplar in the Final Report's Works Cited).
  WARN  286-300 characters, no official role word, nothing tied to Laura (a year alone does not count), more than one
        analytic number, a number not traced to rab/numbers.yaml, a dollar figure without "in Laura's plan",
        overlap of 25-49% (not a pass: rewrite, or disclose the exemplar in Works Cited), or a shared run of 6 or
        more words with an exemplar. With --pick (a note that may be featured in the Trading Notes Analysis): no
        mention of the residency, co-sponsors or which of her ten payments.
Overlap = share of the draft's three-word phrases that also appear in the exemplar. Plain word overlap is not
used, because an honest rewrite shares the facts (Laura, 2037, Treasury) with the exemplar.

Run from the worktree root:
  /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --ticker IBTM --text "Role: future ..."
  /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --ticker IBTR --pick --text "..."
  /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --file my_note.txt        (whole file = 1 note)
  /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --csv team_notes.csv      (columns ticker,note)
  /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/note_check.py --self-test
Without --ticker, the draft is compared with every exemplar. Exit code 1 if anything FAILs.
"""
import argparse
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from note_rules import check_text, phrase_overlap, pick_anchor  # noqa: E402

WHARTON_EXAMPLE = (   # Trading Note Instruction.pdf p.2 (official 2026-27), typed with straight quotes
    "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin "
    "preparing for Laura's future operating commitment. The position provides income and greater stability than "
    "equities, although interest-rate changes may affect its value. This trade supports our plan to balance continued "
    "growth with reliable future cash flows as the residency funding date approaches.")


def exemplars(path=os.path.join(HERE, "notes.csv")):
    rows = list(csv.DictReader(open(path)))
    seen, out = set(), []
    for r in rows:
        if r["note_id"] not in seen:
            seen.add(r["note_id"])
            out.append(r)
    return out


def report(text, ticker=None, ex=None, quiet=False, declared=(), pick=False):
    """Print the checks for one draft; return (fails, warns). `declared`: numbers already traced (e.g. '9%').
    `pick`: the note may be featured in the Trading Notes Analysis (adds the pick-anchor check)."""
    ex = ex if ex is not None else exemplars()
    fails, warns = [], []
    pool = [r for r in ex if ticker is None or r["ticker"] == ticker or r["note_id"] == ticker] or ex
    if not declared:   # numbers the exemplars for this holding already trace to numbers.yaml (notes.csv 'numbers')
        declared = [d.split(" = ")[0] for r in pool for d in r.get("numbers", "").split("; ") if d]
    for name, ok, detail, sev in check_text(text, declared):
        if not ok:
            (fails if sev == "FAIL" else warns).append(f"{name}: {detail}")
    if pick:
        ok, detail = pick_anchor(text)
        if not ok:
            warns.append(f"pick anchor: {detail}")
    over = []
    for r in pool:
        share, run = phrase_overlap(text, r["exemplar"])
        over.append((share, run, r["note_id"]))
        if share >= 0.5:
            fails.append(f"overlap with EXAMPLE {r['note_id']}: {share:.0%} of three-word phrases (rewrite, or "
                         f"disclose in Works Cited)")
        elif share >= 0.25 or run >= 6:
            warns.append(f"overlap with EXAMPLE {r['note_id']}: {share:.0%} of phrases, longest shared run {run} words "
                         f"(not a pass: rewrite, or disclose the exemplar in Works Cited)")
    wshare, wrun = phrase_overlap(text, WHARTON_EXAMPLE)
    if wshare >= 0.25 or wrun >= 6:
        warns.append(f"reads like Wharton's own example note ({wshare:.0%} of phrases): hundreds of teams will")
    if not quiet:
        print(f"Draft ({len(text)} characters): {text}")
        top = sorted(over, reverse=True)[:3]
        print("Closest exemplars: " + ", ".join(f"{i} {s:.0%} (run {r})" for s, r, i in top))
        for f in fails:
            print(f"  FAIL  {f}")
        for w in warns:
            print(f"  WARN  {w}")
        print("  RESULT: " + ("FAIL - fix before pasting" if fails else ("check the warnings" if warns else "pass")))
    return fails, warns


def self_test():
    ex = exemplars()
    ok = True
    print(f"1. Every exemplar in notes.csv passes the text checks ({len(ex)} notes):")
    for r in ex:
        declared = [d.split(" = ")[0] for d in r.get("numbers", "").split("; ") if d]
        f, w = report(r["exemplar"], ex=[], quiet=True, declared=declared)
        bad = f + w
        print(f"   {r['note_id']:7s} {len(r['exemplar']):3d} chars  {'pass' if not bad else bad}")
        ok &= not bad
    base = next(r for r in ex if r["note_id"] == "IBTM_P")["exemplar"]
    copied = base.replace("it covers", "it funds").replace("What its income earns", "What its income makes")
    assert copied != base
    f, _ = report(copied, ticker="IBTM", ex=ex, quiet=True)
    print(f"2. A lightly edited copy of the IBTM exemplar is caught: {'yes' if any('overlap' in x for x in f) else 'NO'}")
    ok &= any("overlap" in x for x in f)
    rewrite = ("Role: future funding and risk management. We bought the iBonds fund that closes in December 2032. "
               "It sets aside Laura's first payment in January 2033 and also the minimum she will give toward the "
               "facility. WInS had no bond ending late in 2032. The fund's final value can still move.")
    f, w = report(rewrite, ticker="IBTM", ex=ex, quiet=True)
    print(f"3. An own-words rewrite of the same facts passes: {'yes' if not f else 'NO ' + str(f)}")
    ok &= not f
    bad = "Role: growth. We’re buying VT, guaranteed to grow Laura’s facility money, about $26,000 or 9%."
    f, _ = report(bad, ex=ex, quiet=True)
    caught = {"ascii", "banned words"} <= {x.split(":")[0] for x in f}
    print(f"4. Curly quotes and 'guaranteed' are caught: {'yes' if caught else 'NO ' + str(f)}")
    ok &= caught
    pick = next(r for r in ex if r["note_id"] == "IBTR")["exemplar"]
    generic = ("Role: future funding. We bought a Treasury fund that ends in Dec 2036, before the 2037 payment. Our "
               "check said the payments cost less than $300,000. Its income must be reinvested.")
    _, w_pick = report(pick, ticker="IBTR", ex=ex, quiet=True, pick=True)
    _, w_gen = report(generic, ticker="IBTR", ex=ex, quiet=True, pick=True)
    caught = not any("pick anchor" in x for x in w_pick) and any("pick anchor" in x for x in w_gen)
    print(f"5. --pick passes the IBTR exemplar and warns on a draft with no residency, co-sponsor or 'her ten': "
          f"{'yes' if caught else 'NO'}")
    ok &= caught
    print("SELF-TEST " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--text")
    ap.add_argument("--file")
    ap.add_argument("--csv", help="team drafts, columns ticker,note")
    ap.add_argument("--ticker", help="compare only with this holding's exemplars (e.g. IBTM, VT, 'T 4.500%% 15-May-2038')")
    ap.add_argument("--pick", action="store_true", help="the note may be featured in the Trading Notes Analysis")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    drafts = []
    if a.text:
        drafts.append((a.ticker, a.text))
    if a.file:
        drafts.append((a.ticker, open(a.file, encoding="utf-8").read().strip()))
    if a.csv:
        drafts += [(r.get("ticker") or None, r["note"].strip()) for r in csv.DictReader(open(a.csv, encoding="utf-8"))]
    if not drafts:
        ap.error("give --text, --file, --csv or --self-test")
    nfail = 0
    for t, text in drafts:
        f, _ = report(text, ticker=t, pick=a.pick)
        nfail += bool(f)
        print()
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
