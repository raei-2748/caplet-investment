"""Writing Room, Sun 1 Nov 2026 (round 5, beat 7): every challenger beside the champion (V49), like for like.

AI DRAFT (Claude, 1 Nov 2026); GPTZero not yet checked. (Keel is a simulated team, AI-written.)
Base: V49 = keel/ips_rewrite/drafts/D29/ips_V49.txt on branch claude/project-thread-3ahu9r (commit 84f1c4f),
copied here as base_V49.txt. Each arm swaps ONE paragraph (or one sentence) and the script counts the whole IPS
with keel/office/tools/textcheck.py's strict count. Arms come from today's rooms (sources in ARMS below);
the chair only applies the repairs those rooms specified. Run: python3 keel/drafts/writing_room_2026-11-01/build.py
"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "office" / "tools"))
from textcheck import words_limit  # noqa: E402

BASE = (HERE / "base_V49.txt").read_text()
P = BASE.split("\n\n")  # 0 opener, 1 ladder, 2 heading, 3 bounce, 4 floor, 5 range, 6 catch, 7 heading, 8 rival, 9 reserve, 10 kicker
assert P[6].startswith("Every fall") and P[8].startswith("We know this rival"), "V49 layout changed"

S1 = ("it names about $90,000, against our $140,000", "it names about $85,000, against our $135,000")  # near-breach 2: P4's linked world (A26 S1)

def sent_swap(par, old, new):
    assert old in par, old
    return par.replace(old, new)

REC = "shrink, and with them the 2028 deposit that was meant to top it up."
ARMS = {
  "opener": {  # V49 P1's last line: Laura's Room cut it (2-1) to pay for the bounce number
    "A": ("V49 own", P[0]),
    "B": ("Laura's Room: cut 'shopping problem' (2-1, pays for the bounce)", P[0].replace(" The cheques are a shopping problem, not an investing one.", "")),
  },
  "bounce": {  # V49 P4
    "A": ("V49 own", P[3]),
    "B": ("Laura's Room 2-1 (LR-09, S9)", sent_swap(P[3], REC, REC + " If it halves that deposit, our model bounces a cheque once in 66.")),
    "C": ("Kai's minority (LR-09)", sent_swap(P[3], REC, REC + " Barring default, our model pays every cheque in full over 99 times in 100; in that recession, 98.")),
  },
  "range": {  # V49 P6; near-breach 1 ($150,000 floor v $145,000 bottom)
    "A": ("V49 own", P[5]),
    "B": ("Window's bridge on V49 (+11)", sent_swap(P[5], "The bottom is her floor, owned since 2028.", "The bottom is her floor, owned since 2028, named a little under it, since a fund's payout isn't fixed to the dollar.")),
    "C": ("Jun's (Library) with the Window's bridge in place of 'held in Treasuries'",
          "In 2031 she gives co-sponsors a range – and says which money pays each end. The bottom is the floor she's owned since 2028, named a little under it, since a fund's payout isn't fixed to the dollar. The top adds half her stocks. The other half stays hers, to sell any day if a building priced in Taiwan dollars comes in dearer."),
  },
  "catch": {  # V49 P7
    "A": ("V49 own (Laura's Room: mis-timed)", P[6]),
    "B": ("Laura's Room repair 3-0 + V49's 97 sentence",
          "A range named on stocks has a catch: every fall comes off the gift, every rise past the top goes to Laura. So in January 2031, before any co-sponsor hears a number, Laura moves the promised half into Treasuries. Our model puts the gift at its top about 97 times in 100."),
    "C": ("Nora's (i), Genius Lab ADOPT 2-0",
          "A capped range has a catch: once named, every fall in stocks comes off the gift while every rise past the top goes to Laura. Before she names it, the half she'll promise moves into Treasuries, and in our model the gift reaches its top about 97 times in 100."),
    "D": ("V47 own",
          "A capped range has a catch: once named, every fall in stocks comes off the gift while every rise past the top goes to Laura. On the day she names it, the half she promised moves into Treasuries, and in our model the gift reaches its top about 97 times in 100."),
  },
  "rival": {  # V49 P9 (after 'Know thy rival'); every arm carries the S1 pair (near-breach 2, zero words)
    "A": ("V49 own + S1 pair", sent_swap(P[8], *S1)),
    "B": ("Kai's (Library), repaired to Felix's spec: S1 pair, 'in our model' on the $145,000, cost against the rival first",
          "In our model, our plan costs Laura about $15,000 on average by 2042 against the strongest rival, counting the gift and what she keeps. That rival, matched in our model to name our $145,000 median bottom, usually wins. It keeps our ladder but puts the 2028 deposit mostly in stocks, and in January 2031 buys its bottom with whatever they fetch that morning. Laura has been willing to take thoughtful risks, the case says, and our first plan was three-quarters stocks until our own model sank it. But the rival has a flaw – and we can say where. In the twentieth of modelled paths where 2028-30 is worst for stocks, it names about $85,000 to co-sponsors against our $135,000 after the 2031 set-aside. We'd pay the $15,000."),
    "C": ("Courtroom's callback ('that morning comes mid-slump') on V49 + S1 pair",
          sent_swap(sent_swap(P[8], *S1), "2028–30, it names", "2028–30, that morning comes mid-slump, and it names").replace("mid-slump, and it names about $85,000, against", "mid-slump, and it names about $85,000 against")),
    "D": ("Window's flat yes (W-06) on V49 + S1 pair",
          sent_swap(sent_swap(sent_swap(P[8], *S1), "Asked in our model to name our typical bottom, $145,000, it leaves Laura", "Does our floor cost her anything, then? Yes. Asked in our model to name our typical bottom, $145,000, the rival leaves Laura"), " Sounds good, on average.", "")),
    "E": ("Kitchen's agreed value v market value (MoneySmart, verified 1 Nov) on V49 + S1 pair",
          sent_swap(sent_swap(P[8], *S1), "Sounds good, on average.", "Sounds good, on average: market-value cover is always cheaper than agreed value.")),
  },
}
IDX = {"opener": 0, "bounce": 3, "range": 5, "catch": 6, "rival": 8}

def assemble(choice):
    parts = list(P)
    for slot, arm in choice.items():
        parts[IDX[slot]] = ARMS[slot][arm][1]
    return "\n\n".join(parts)

if __name__ == "__main__":
    base = words_limit(BASE)
    out = {"base_V49": base, "arms": {}}
    print(f"V49 base: {base} strict")
    for slot, arms in ARMS.items():
        for k, (src, text) in arms.items():
            whole = words_limit(assemble({slot: k}))
            out["arms"][f"{slot}_{k}"] = {"source": src, "paragraph_words": words_limit(text), "ips_words": whole, "delta": whole - base, "text": text}
            print(f"{slot:7s} {k}  para {words_limit(text):4d}  IPS {whole:4d} ({whole-base:+d})  {src}")
    (HERE / "arms.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
