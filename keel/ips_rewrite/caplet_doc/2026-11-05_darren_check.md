# Check of two Version 5 / "IPS Body" paragraphs Darren queried (Claude, Thu 5 Nov 2026)

Both paragraphs come word for word from Claude's AI exemplar of 17 Oct (`keel/library/blueprints/04_exemplar_ips_tna_17Oct.md`, lines 42 and 44).

## 1. The 2031 range paragraph: needed, but written for the old design
- Needed: the case says teams "must recommend the dollar range Laura should communicate and state how confident they are" (case p.3). This is the only paragraph in the IPS Body that gives a confidence figure.
- Old design: it assumes nothing is traded in 2031 and half the fund is given in 2033. V57 and the new pitch move half the shares into Treasuries before Laura names the range. Under that design:
  - "about three of four paths" (76%, `keel/library/range_2031/README.md`) becomes about 9 in 10 to reach the top (88% model, 81% history bootstrap; `keel/library/assistant_review_2026-10/oct20/lockin/lockin_2031.md` s.3, s.5);
  - "a 40% fall during 2032 would lower a typical contribution from about $169,000 to $162,000" stops being true: the fall no longer moves it (same file, s.5).
  - Within the range: 98.1% either way (same file, s.2).
- Uses "floor" (banned, INSTRUCTIONS I83).

## 2. The inflation sentence: Darren's premise is wrong, the sentence needs fixing
- The case does not say "don't account for inflation". It says only that each payment "is a fixed $50,000 and is not adjusted for inflation" (case line 90), and it asks teams to explain "the effect of inflation on portfolio projections and facility costs" (case line 147).
- "About 12% by 2033" holds only from January 2028 (2.5% for 5 years = 11.6%); from 2027 it is 13.8%. Name the start year.
- 2.5% is JPM's US inflation assumption (2026 LTCMA). The facility is built in Taiwan: Taiwan's construction cost index has risen about 3.5% a year since 2021, which gives a larger cut (13-16%, `keel/library/assistant_review_2026-10/oct20/inflation/inflation.md` line 196).
- "the floor" -> "her minimum facility contribution" (I83).
- Checked and sourced: "$136,000" after a half-point fall (`range_2031/README.md` line 84) and "$21,000" shortfall (`ips_numbers_2026-10/IPS_number_sheet.md`).
