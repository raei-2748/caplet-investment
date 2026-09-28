"""D9_draft_checker.py - a mechanical check for the team's OWN drafts of WInS notes, TN reflections, the pitch and the IPS.

It never writes or rewrites text. It counts words and characters and flags words that the D9 communication spec
(`research/insight_v1/phase_D/D9_communication.md`) says to avoid or to define. A human decides every change.

Inputs (with status labels):
- Word limits: pitch <= 50 words, IPS <= 500 words (IPS guide lines 31-39, VERIFIED-REPO-FILE); TN reflection <= 100
  words (Trading Notes guide line 46, VERIFIED-REPO-FILE). WInS note limit: none published (UNKNOWN; check the WInS
  note field). Wharton's example note is 59 words / 413 characters (counted by this script, `--demo`).
- IPS bans "Graphics, charts, images, attachments, external links, footnotes, and formal citations" (IPS guide line
  123, VERIFIED-REPO-FILE). No Laura quotes in TN or IPS (D13 rule, brief section 16).
- Official role words for notes: "growth, liquidity, risk management, or future funding" (Investment Competition Guide
  p.3 lines 84-86, VERIFIED-REPO-FILE).
- Overclaim and jargon word lists: ASSUMPTION (D9 judgement, built from the chair memo section 7, the wins_now ticket
  "never say" list, and D13c section 6). They flag words for a second look; a flag is not an error.
- Word counting: whitespace-separated tokens, which is how Microsoft Word counts ("$50,000" = 1 word, "2033-2042" = 1
  word, "U.S." = 1 word). ASSUMPTION: the judges count the same way; leave a margin of 5-10 words.

How to run (from the repo root; keep drafts OUT of the repo, e.g. in a local folder):
    .venv/bin/python research/insight_v1/scripts/D9_draft_checker.py --kind note       path/to/note.txt
    .venv/bin/python research/insight_v1/scripts/D9_draft_checker.py --kind reflection path/to/reflection.txt
    .venv/bin/python research/insight_v1/scripts/D9_draft_checker.py --kind pitch      path/to/pitch.txt
    .venv/bin/python research/insight_v1/scripts/D9_draft_checker.py --kind ips        path/to/ips.txt
    .venv/bin/python research/insight_v1/scripts/D9_draft_checker.py --demo     (runs on Wharton's own example note)
"""
import argparse
import re
import sys

LIMITS = {"pitch": 50, "ips": 500, "reflection": 100, "note": None}

WHARTON_EXAMPLE = (
    "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin "
    "preparing for Laura’s future operating commitment. The position provides income and greater stability than "
    "equities, although interest-rate changes may affect its value. This trade supports our plan to balance continued "
    "growth with reliable future cash flows as the residency funding date approaches."
)

# Words that overclaim for this plan (see D9 M062). Pattern -> why it is flagged.
OVERCLAIM = {
    r"\bguarantee(d|s)?\b": "too strong: say bought/locked at market prices; residual risk is a U.S. government default",
    r"\brisk[- ]free\b|\briskless\b|\bno risk\b": "too strong: the plan's own definition names a residual risk",
    r"\bsafe(ly|st|r)?\b": "vague: safe from what? name the risk that is removed",
    r"\bstable\b|\bstability\b": "false for long Treasury funds (TLT 3y sd 13.74% vs IEF 6.54%, F-201/F-202)",
    r"reduc\w* (portfolio )?volatility": "Wharton-example wording; our hedge reduces risk to the payments, not price swings",
    r"\bmatch(es|ed|ing)?\b": "true for Laura's real bond ladder; NOT for WInS funds (say 'moves like' / 'stands in for')",
    r"\b100 ?%|\bcertain(ly)?\b|\bcertainty\b": "check the object: certainty belongs to the ten payments only (M062)",
    r"\bconfiden(t|ce)\b": "check the object: confidence belongs to the 2031/2033 facility range only (M062)",
    r"\bwill (grow|return|earn|outperform)\b": "a forecast stated as fact: say 'is expected to' and name the source",
    r"\bbeat(s|ing)? the market\b|\boutperform\w*\b": "not a goal in this competition (Guide p.3)",
    r"\bgain(ed|s)?\b|\bprofit\w*\b|\bup \d+(\.\d+)? ?%": "judged on reasoning, not results (TN guide lines 15-16)",
    r"\badvis[eo]r (decided|chose|approved)\b|\bportfolio manager (decided|chose)\b": "advisors may not make decisions",
}

# Terms a high-school reader or Laura may need defined the first time (define once, or replace).
JARGON = [
    "duration", "DV01", "basis point", "bp", "convexity", "liability", "liabilities", "immuniz", "glide path",
    "surplus", "sleeve", "tranche", "alpha", "beta", "Sharpe", "Monte Carlo", "percentile", "p5", "p50", "p95",
    "STRIPS", "zero-coupon", "LDI", "ALM", "drawdown", "yield curve", "forward", "par yield", "funded ratio",
    "nominal", "rebalanc", "band", "tail", "hedge",
]

ROLE_WORDS = ["growth", "liquidity", "risk management", "future funding"]
LAURA_ANCHORS = [r"\$?50,000|\$50k", r"\b2033\b", r"\b2042\b", r"\bpayments?\b", r"\bfacility\b", r"\b2031\b",
                 r"co-?sponsor", r"\boperating\b", r"\b2028\b", r"\$?150,000|\$150k"]
IPS_BANNED = {
    r"https?://|www\.": "external link (banned in the IPS)",
    r"\[\d+\]|\(\d{4}\)|et al\.|\bSource:": "looks like a formal citation or footnote (banned in the IPS)",
    r"[“”\"]": "quotation marks: no Laura quotes in the IPS or TN (D13 rule); check any quote",
}
TN_NOT_EXPECTED = {
    r"operating reserve of \$|reserve (size|of) \$": "reserve size is not expected in the TN (TN guide lines 20-22)",
    r"contribut\w* (of )?\$\d|facility (contribution|gift) of \$": "facility amount is not expected in the TN",
    r"range of \$": "a co-sponsor range is not expected before the Final Report",
}


def words(text):
    return [w for w in re.split(r"\s+", text.strip()) if w]


def ngram_overlap(a, b, n=3):
    def grams(t):
        ws = [re.sub(r"[^a-z0-9']", "", w.lower()) for w in words(t)]
        return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}
    ga, gb = grams(a), grams(b)
    return sorted(" ".join(g) for g in ga & gb)


def check(text, kind):
    ws = words(text)
    print(f"KIND: {kind}")
    lim = LIMITS[kind]
    print(f"Words: {len(ws)}" + (f" / limit {lim} ({'OK' if len(ws) <= lim else 'OVER LIMIT'})" if lim else
                                 " (no published limit; Wharton's example is 59)"))
    print(f"Characters incl. spaces: {len(text.strip())}")
    nums = [w for w in ws if re.search(r"\d", w)]
    print(f"Tokens containing digits: {len(nums)} -> {nums}")
    if kind in ("pitch", "ips") and len(nums) > (2 if kind == "pitch" else 8):
        print("  FLAG: many numbers for a document that should carry rules, not calculations (IPS guide line 51-52)")
    print("\nOverclaim / wording flags (a second look, not automatic errors):")
    hit = False
    for pat, why in OVERCLAIM.items():
        for m in re.finditer(pat, text, flags=re.I):
            hit = True
            s = max(0, m.start() - 30)
            print(f"  - '{m.group(0)}' ...{text[s:m.end() + 30].strip()}...  -> {why}")
    if not hit:
        print("  none")
    print("\nJargon to define on first use (or replace):")
    jj = [j for j in JARGON if re.search(r"\b" + re.escape(j), text, flags=re.I)]
    print("  " + (", ".join(jj) if jj else "none"))
    if kind in ("note", "reflection"):
        roles = [r for r in ROLE_WORDS if re.search(r"\b" + r, text, flags=re.I)]
        print(f"\nGuide role words present (growth / liquidity / risk management / future funding): {roles or 'NONE'}")
        for pat, why in TN_NOT_EXPECTED.items():
            if re.search(pat, text, flags=re.I):
                print(f"  FLAG: {why}")
        ov = ngram_overlap(text, WHARTON_EXAMPLE)
        if ov:
            print(f"Three-word phrases shared with Wharton's example note ({len(ov)}): {ov}")
            if len(ov) >= 4:
                print("  FLAG: reads like a copy of the example; hundreds of teams will write this.")
    anchors = [p for p in LAURA_ANCHORS if re.search(p, text, flags=re.I)]
    print(f"\nLaura-specific anchors found: {len(anchors)} {anchors}")
    if not anchors:
        print("  FLAG: nothing ties this text to Laura's dated needs (payments 2033-2042, 2031 range, facility)")
    if kind in ("ips", "pitch", "note", "reflection"):
        for pat, why in IPS_BANNED.items():
            if re.search(pat, text):
                print(f"FLAG: {why}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--kind", choices=sorted(LIMITS), default="note")
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()
    if a.demo:
        print("DEMO on Wharton's own example note (TN guide p.2 lines 36-39, VERIFIED-REPO-FILE)\n")
        check(WHARTON_EXAMPLE, "note")
        return 0
    if not a.path:
        ap.error("give a draft file path or --demo")
    check(open(a.path, encoding="utf-8").read(), a.kind)
    return 0


if __name__ == "__main__":
    sys.exit(main())
