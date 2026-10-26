# The TNA's "about 7.5% a year (as per JPMorgan)" is J.P. Morgan's 2027 global-equity figure, not EAFE. The rewrite's correction is wrong
AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited. (Keel is a simulated team, AI-written.)
Work order: SD-N01 | Asked by: self-directed (rewrite inbox `2026-10-26_thread_check-7-5.md`: "confirm which edition and asset class") | Room: the Noticeboard (Nora), Felix checking | Date: Tue 27 Oct 2026, 07:30 AEDT

## Answer
- **J.P. Morgan's own release says it plainly.** "Global equities are projected to return 7.5% (USD), increasing from
  7.0%." Same release: "U.S. large cap equities are expected to return 7.5%, increasing from 6.7%"; the 60/40 "rises
  to 7.0%". Dated **19 Oct 2026**, four days before the TNA went in (J.P. Morgan press release, "J.P. Morgan releases
  2027 Long-Term Capital Market Assumptions", https://am.jpmorgan.com/us/en/asset-management/institutional/about-us/media/press-releases/jp-morgan-releases-2027-long-term-capital-market-assumptions/, read 27 Oct 2026).
- **The 7.0% it rose from is the 2026 AC World row** (2026 USD matrix: "AC World Equity 7.00"; Library LC-02). So the
  2027 global-equity 7.5% is the world-stocks number, the right one for VT.
- **R04's "7.5% is EAFE" read the 2026 edition.** EAFE was 7.50 *in 2026*; the match was a coincidence of editions.
  The rewrite's line "the IPS must not repeat 7.5%" (`../../ips_rewrite/THINKING_LOG.md`, day 1) and the CHANGES row
  "Corrected: the TNA's 7.5% is JPM's EAFE figure" are withdrawn by this memo.

## What it changes for the judges
1. **The locked VT reflection is right.** Nothing in the IPS or the Final Report should "correct" it; that would
   tell a judge our own TNA was wrong when it wasn't.
2. **If the IPS states a stock return, 7.5% is the one that coheres** with the TNA (Keel's call of 24 Oct stands).
   The rewrite thread's lean to quote no return at all (form: no "detailed financial calculations") is still fine.
3. **Final Report citation:** "J.P. Morgan Asset Management, *2027 Long-Term Capital Market Assumptions*, press
   release 19 Oct 2026: global equities 7.5% (USD), 10-15 years." Not "ACWI compound": the release names neither.
4. **Models.** Any run since 26 Oct at 7.0% (e.g. R05's quick 70-73% "reach the top") is one edition behind. P06
   showed the half point barely moves the tails (29% -> 28%); WO-R5's newsvendor run should use 7.5%.

## Limits
The matrix itself (compound vs arithmetic, the ACWI row by name) is behind a J.P. Morgan login: UNVERIFIED. The
release's "global equities" is the strongest public wording; Keel never writes "compound" beside it.

AI use: Keel Office (Claude Code) read J.P. Morgan's 19 Oct 2026 release to settle which index the TNA's 7.5% is, 27 Oct 2026.

- **Felix:** Two of our rooms read the same number off different years and both were sure. That's the bit I'd underline.
- **Jun:** I'll re-run the newsvendor at 7.5%. I'd rather know than assume it's half a point of nothing.
- **Kai:** Good. The one line in the TNA I actually liked writing nearly got "fixed" into a mistake.
