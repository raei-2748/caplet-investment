# Kai's sources, H-017 round 1 (Mon 2 Nov 2026)

(Keel is a simulated team, AI-written.) This is AI-generated research (Claude Code) and is not for submission. The
practitioner I read is a clearing house's default waterfall, in the clearing house's own published words.

## How it was fetched (read this before trusting a quote)
- I couldn't use the house script as written: `.venv/bin/python` doesn't exist in this container. With the system
  `python3`, `fetch_text.py` got a proxy **403 (policy denial)** for www.cmegroup.com, www.eurex.com and www.lch.com.
  One-shot checks of eur-lex.europa.eu, www.bis.org, www.sec.gov, www.dtcc.com, www.theocc.com, www.ice.com,
  www.federalreserve.gov, www.bankofengland.co.uk, www.gov.uk, ppp.worldbank.org, www.esma.europa.eu, www.cftc.gov,
  www.isda.org, www.fsb.org, home.treasury.gov and en.wikipedia.org were all 403 as well. I didn't retry any of them.
- So I read the pages through the **WebFetch tool**, the same way the Lab read ICH Q8 today. Its answers go through a
  small summarising model, and it only gives quotes under 125 characters. The words below are exactly what WebFetch
  returned, but nobody has byte-checked them. Re-check with `fetch_text.py URL --grep "phrase"` once the host is allowed.

## Source 1 (primary; the practitioner's own words)
CME Group, **"101 Overview: CME Clearing Financial Safeguards Waterfalls"**,
https://www.cmegroup.com/articles/brochures-and-handbooks/101-overview-cme-clearing-financial-safeguards-waterfalls.html
(page metadata dated 16 Jul 2020; read Mon 2 Nov 2026 through WebFetch).

Exact words, as returned:
1. "CME Clearing would utilize its own contribution to the relevant financial safeguards waterfall"
2. "pre-funded at $100 million for base products and $150 million for IRS products."
3. "non-defaulting clearing members’ pre-funded contributions to the guaranty fund"
4. "clearing members must provide CME Clearing with additional financial resources up to a capped amount"
5. "CME Clearing has never utilized layers of the waterfall beyond the financial resources" (WebFetch cut the quote
   here; according to its summary, the sentence goes on to the defaulted clearing member's resources)
6. "CME Clearing has established a separate financial safeguards waterfall for base products"

The order, in WebFetch's summary (this is not a quote): the defaulted member's own resources come first, then CME's
own contribution, then the non-defaulting members' guaranty fund, then assessments, which are capped.

**What it means for us**
- **Order.** The owner's own money stands in front of money other people put up. That is V53 P8's "so her
  flexibility shrinks before her promise does". PASS.
- **Size and timing.** CME's own layer is a fixed sum, pre-funded before anyone is exposed, and it is still there
  while members are exposed. V53 puts no limit on Laura's layer before naming day, so in some futures the whole pocket
  is spent before any promise exists, and after she speaks only the cushion stands in front of the gift. The question
  the practitioner would put to P8: *how much of her own money is still standing in front of the co-sponsors after
  she has spoken?* That supports H25.
- **Separate waterfalls.** CME keeps one waterfall for base products and another for IRS. This page doesn't say why.
  My reading is that losses on one book can't drain the resources behind the other. Laura's kept half has two jobs in
  one pocket (L-16: the reinvestment gap and the building), and keeping back a quarter is a crude ring-fence for the
  building's job.
- **"Up to a capped amount".** CME tells members in advance the most it can ask of them. V53's bottom, "money she
  already owns", does that job for Laura's co-sponsors, and P6 already says it.
- **"Never utilized layers ... beyond".** The first layer has always been enough. Ours mostly is too: in the base
  world V53's pocket is all gone in 19 futures in 100, which leaves 81 where it isn't.
- Where it can go: not in the IPS (no citations; Book 11). At most it's the Final Report's picture of who stands in
  front of whom.

## Context (secondary; an academic, not the practitioner)
Ron Berndsen (Tilburg University), **"A CCP's skin-in-the-game: Is there a trade-off?"**, WFE Focus, October 2020,
https://focus.world-exchanges.org/articles/ccp-skin-game (read 2 Nov 2026 through WebFetch). Exact words, as returned:
"the CCP suffers a loss of its own resources prior to any surviving clearing member"; "There are however limits to
increasing SITG"; "As such there is a trade-off between higher SITG and clearing costs." What it means: inside the
field the argument is over how big the owner's layer should be, which is exactly H25 against H50. It isn't
Laura's case, so it's background only.

## Tried, not used
CME Group, "Balancing CCP and Member Contributions with Exposures",
https://www.cmegroup.com/education/articles-and-reports/balancing-ccp-and-member-contributions-with-exposures (the
page says 18 Aug 2017). WebFetch got back only the summary page, with one phrase: "incentivize market participants to
manage the risks they create". The 20 Jan 2015 press release
(https://www.cmegroup.com/media-room/press-releases/2015/1/20/cme_group_releaseswhitepaperclearing-balancingccpandmembercontri.html)
doesn't set out the paper's position. I didn't use either.

## The numbers in my post (MODEL, never in the IPS)
`../../../rooms/lauras_room/LR-10_results.json`; curve 22 Oct 2026, J.P. Morgan 7.5% world stocks, 200,000 paths,
seed 20261016. A0 = V53 as written and modelled.

| per 100 futures | S0 A0 / H25 / H50 | S2 A0 / H25 / H50 | S6 A0 / H25 / H50 | S9 A0 / H25 / H50 |
|---|---|---|---|---|
| All ten cheques paid | 99.82 / 99.86 / 99.85 | 99.74 / 99.80 / 99.78 | 99.68 / 99.77 / 99.74 | 98.49 / 98.51 / 98.51 |
| Kept half all gone by Jan 2033 | 19.0 / 6.6 / 4.9 | 41.6 / 23.2 / 20.9 | 65.4 / 44.5 / 41.6 | 86.1 / 54.8 / 53.1 |
| Range lowered on naming day | 16.9 / 23.5 / 36.3 | 37.9 / 48.2 / 59.5 | 62.8 / 68.8 / 75.4 | 83.5 / 92.5 / 97.9 |
| Gift reaches the quoted top | 97.9 / 99.3 / 99.6 | 96.7 / 98.4 / 99.3 | 96.0 / 98.9 / 99.6 | 95.9 / 97.7 / 98.7 |
| Gift pays a cheque top-up after naming | 16.1 / 5.9 / 4.6 | 35.7 / 21.9 / 19.9 | 61.2 / 43.2 / 40.7 | 79.4 / 51.9 / 50.4 |
| Median top quoted | $165k / $165k / $160k | $80k / $75k / $75k | $145k / $140k / $140k | $40k / $35k / $35k |
| Gift, mean | $159,957 / $159,127 / $157,721 | $71,946 / $70,986 / $69,821 | $141,771 / $140,096 / $138,128 | $37,464 / $36,359 / $35,070 |
| Median left of the kept half, Jan 2033 | $13,910 / $13,911 / $14,505 | $2,888 / $3,508 / $5,887 | $0 / $2,179 / $4,218 | $0 / $0 / $0 |
| Laura's money in 2042, mean | $49,270 / $50,832 / $53,569 | $27,995 / $29,581 / $31,793 | $23,725 / $26,549 / $30,023 | $13,409 / $15,339 / $17,683 |
The gift never falls below the quoted bottom under H25 or H50 in any world (A0: 0.01% in S9).

## The offer's count (`keel/office/tools/textcheck.py`, piped from V53 with the two swaps, no file written)
V53 497 strict. Swapping P8's last sentence for "Once the gap takes three quarters of those stocks, the rest lowers
the whole range." takes it to 503. Cutting P5's ", but the cheques never depend on it" brings it to **496** strict (495
by spaces).
