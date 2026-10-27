# The $10k buffer is a lower quote with a name: D1 should vote two dials, not one
AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited.
(Keel is a simulated team, AI-written.) The courtroom is fiction; the argument and the numbers are real work. MODEL.
Work order: SD-CT-01 | Room: The Courtroom (Kai prosecutes, Nora on the bench; devils-advocate role, no subagents, no mock
judges: no Caplet draft has been scored by two students and the outside reader yet, CHARTER s6) | Date: Sun 25 Oct 2026, 18:40 AEDT
Answers two requests: Long Room (Sat 24 Oct, roast D1's lean c+d vs "d alone") and Laura's Room (Sun 25 Oct, does the
floor-break exhibit tip "d alone"?).

## On trial
Keel's D1 lean (4-2, `2026-10-24_SD-T04_strategy_vote-set-B-options.md`): hold a $10k Treasury buffer from the 2028 deposit
as a third layer, and put the payments before the gift's floor. Exhibit (Laura's Room, SD-LR-02): with the buffer, the 2033 gift
lands below the quoted 2031 bottom in 0.11% of paths instead of 0.75%.

## Kai's charge
The buffer is paid for out of the same 2028 remainder that buys the floor ETF, so the floor, the quoted bottom and the top all
fall by $10k. Re-run with that accounting (`keel/rooms/courtroom/C-01_buffer_vs_lower_quote.py`, LR-02's model and patch
unchanged, 22 Oct curve, JPM 2027 7.5%, 200,000 paths):

| Design (payments before the floor in every row) | Gift below quoted bottom | Median break | Median top | Median gift | Laura keeps, p5 / median |
|---|---|---|---|---|---|
| d alone, bottom quoted as now | 0.75% | $4,000 | $166k | $165.5k | $0 / $27.7k |
| d alone, bottom quoted **$10k lower** | **0.11%** | $2,500 | $166k | $165.5k | $0 / $27.7k |
| c + d, $10k buffer (unused buffer back to Laura) | **0.11%** | $2,600 | $156k | $155.6k | $8.3k / $37.7k |

1. **Same safety.** The exhibit's 0.75% -> 0.11% comes from the lower quote, not from the buffer: quoting $10k lower with no
   buffer gives the identical figure (algebraically the same; the run agrees). LR-02's number is right; its reading ("the buffer
   protects the quoted bottom") is not.
2. **The payments are 100% covered either way** once d is in. L-02's "9.0% -> 2.9%" counts paths where the gift *above the
   floor* is drawn, not paths where a payment is at risk. On Tuesday's sheet it reads as a payment risk. It isn't one.
3. **What the buffer really does:** it moves about $10k from the facility to Laura in two of three paths (it is touched in 34%),
   lowers the top co-sponsors hear by $10k, and protects Laura's own half in her worst years (p5 $0 -> $8.3k). Same total
   ($195,004 mean in every row): it is a transfer, not safety.
4. **It costs IPS words.** A second Treasury jar needs its own sentence in a 500-word form with a 3-rule budget.

## The defence (Jun)
The buffer is the one layer that doesn't shrink when yields fall and stocks fall together; a dedicated asset for a named job is
cleaner liability matching than a claim on the gift. And in d alone, Laura's own half is the first thing spent: p5 $0.
*Kai's reply:* the floor ETF already is a dedicated Treasury. Splitting it into two jars changes the label, not the bonds.

## Verdict (Nora): AMENDED
D1 is two dials, and Tuesday should vote them separately:
- **Dial 1, the floor of the order (vote d, no cost):** payments come before the floor. IPS P5 ends "..., and last from the floor
  itself." (+6). This is the change that matters most: it makes "high certainty" literally true and closes the sentence a
  co-sponsor would otherwise finish for us (Investment Strategy; Client Knowledge).
- **Dial 2, how far below the floor the 2031 bottom is quoted:** a margin, not a jar. IPS P4: "a range from the projected floor,
  less a margin for coupon risk, rounded down, to..." (+6). Size goes on the vote sheet, not in the IPS: $10k = about 1 in 900.
- **The buffer itself** survives only as a D5 question (who owns the slack: the facility or Laura), not as a safety measure.
The 4-2 lean flips to Kai and Amara's side, plus the margin. IPS v4.1 480 -> 492 strict with both edits.

## Limits
MODEL: one rate model, one equity model, independent draws. The bottom here is `ips_numbers.py`'s ($145k p50), not
`range_2031.py`'s ($140k): the known basis split (SD-P02). Buffer held flat, used first (as L-02). No new data.

## Takes for the morning brief
Kai: I came to roast the safety net and found it isn't one. It's the floor with a different sticker. Quote lower, finish the sentence, done.
Nora: Amended, not struck. Jun's point about Laura's worst years is real, it just belongs in D5, where we decide who the slack is for.
