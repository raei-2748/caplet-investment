# Amara's research (round 1, H-022, Tue 3 Nov 2026)

(Keel is a simulated team, AI-written.) Written by the Keel scout Amara (Claude Haiku 5.5). The team is fiction; the pages below are real, read on 3 Nov 2026 with WebFetch and WebSearch.

**Caution on quotes.** WebFetch summarises each page through a small model. Every quote here is near-verbatim via fetch tool, not checked word for word against the page. Re-check any quote against the live page before it goes into a deliverable.

**Test sentence (V54, P5):** "Banks sell the same idea as a capital-protected note, but they spend that interest on an option, which expires worthless if the market stands still. Shares don't expire."

**Short answer.** All three sources put a bond first and the option second. None of them says the option "expires worthless". The one example that covers a flat market (SEC) shows a 0% market-linked return with principal returned. The word a cold reader has to guess is "option".

---

## Find 1: ASIC Moneysmart, "Get the facts: 'Capital guaranteed' or 'protected' investments"

- **Source:** ASIC MoneySmart consumer guide (PDF). URL: https://static.moneysmart.gov.au/files/publications/get-the-facts-capital-guaranteed-or-protected-investments.pdf. Date read: 3 Nov 2026. Date on the document: "© ASIC, January 2013". This is the most recent ASIC guide on the topic I could open; see "Pages tried and not opened".
- **Source's own words (near-verbatim via fetch tool):** "Others use a portion of the money you invest to buy a bond to provide capital protection." The same section says the rest goes into "options and other derivatives". Other lines: "if the cumulative growth turns out to be negative you will still get back the original amount"; "Several of these products do not pay any returns until maturity"; "your overall cumulative investment return over the life of the investment may be capped at 70%".
- **Mechanism, plain:** Part of the money you put in buys a bond, and that bond is what protects your capital. The rest buys options and other derivatives, which are what can add a return.
- **V54 sentence it tests:** P5, sentence 1 ("Banks sell the same idea ... stands still.").
- **What the source explains first that our sentence skips:** Where the money goes. A portion buys the protecting bond first; the option is paid for with what is left. V54 names no bond in P5, so "that interest" has nothing in that sentence to attach to.
- **If the market stands still or falls:** On a fall, the guide says you still get back the original amount (its example is negative growth). On a flat market the guide says nothing; its example only covers negative growth. It also says several products pay no return until maturity.
- **Verdict: GUESS.** Word: **"option"** (the guide says "options and other derivatives" and does not explain them).

---

## Find 2: SEC and Investor.gov, "Structured Notes with Principal Protection: Note the Terms of Your Investment"

- **Source:** SEC investor alert, issued with FINRA, on investor.gov. URL: https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/structured-notes-principal-protection-note-terms. Date read: 3 Nov 2026. Date on the page (per fetch tool): "June 2, 2011".
- **Source's own words (near-verbatim via fetch tool):** A note "typically combines 'a zero-coupon bond' with 'an option or other derivative product whose payoff is linked to an underlying asset, index or benchmark.'" In the page's hypothetical, "Has no gain or loss at maturity" gives "a 0% return" and "100% of principal returned". The page also says a note "could earn no return for the entire term of the note, even if you hold the note to maturity." And: "Products offering principal protection can be expensive."
- **Mechanism, plain:** The note has two parts: a zero-coupon bond, which pays no interest until it matures, and an option whose payoff is tied to an index. If the index ends where it started, the option pays nothing, and the page's example still returns all principal.
- **V54 sentence it tests:** P5, sentences 1 and 2.
- **What the source explains first that our sentence skips:** The zero-coupon bond. It comes first in the source's sentence. The source also explains "option" in one line: a payoff linked to an index. V54 gives neither the bond nor the index link.
- **If the market stands still or falls:** Flat (no gain or loss at maturity): 0% return, 100% of principal back, in the hypothetical. Falls: in that example, a fall of up to 10% returns all principal; a bigger fall returns less (their example: index down 15%, note returns 95% of principal).
- **Verdict: GUESS.** Word: **"option"**. The page explains it only as a payoff tied to an index, which V54 never says.
- **Claim check on "expires worthless if the market stands still":** see the section below. Supported for this hypothetical; not stated as a general rule.

---

## Find 3: SEC and FINRA joint release, "SEC, FINRA Warn Retail Investors About Investing in Structured Notes With Principal Protection"

- **Source:** Joint SEC and FINRA investor release. URL: https://finra.org/media-center/news-releases/2011/sec-finra-warn-retail-investors-about-investing-structured-notes. Date read: 3 Nov 2026. Date: the fetched text carried no date; "2011" comes from the URL and the search result. Treat the date as unconfirmed on the page.
- **Source's own words (near-verbatim via fetch tool):** These notes "typically combine a zero-coupon bond" with a derivative, such as an option. The bond "pays no interest until the bond matures." The notes "are not risk-free". "Any guarantee is only as good as the financial strength of the company that makes that promise." Investors who "hold these notes until maturity" typically get some money back. Protection levels vary, with some "guaranteeing as little as 10 percent".
- **Mechanism, plain:** The bond provides the protection, and because it pays no interest until it matures, the protection only pays out at the end. The option provides the return, and the return can be limited or capped.
- **V54 sentence it tests:** P5, sentence 1.
- **What the source explains first that our sentence skips:** The bond, and that it protects only at maturity and only as far as the issuer can pay. V54 says "capital-protected" and never says what does the protecting, when, or on whose promise.
- **If the market stands still or falls:** The release does not address a flat market directly. On a fall, holders "typically still recover at least some principal, 'even if the underlying asset, index or benchmark declines'", provided they hold to maturity.
- **Verdict: GUESS.** Word: **"option"**. The bond is the step that comes before it.

---

## Is it true the option "expires worthless if the market stands still"?

- **Supported for the SEC's hypothetical.** The note-terms page says "Has no gain or loss at maturity" gives a 0% return. An option whose payoff is zero on a flat index is the ordinary meaning of "worth nothing at the end". The pages do not use the words "expires" or "worthless".
- **Not stated as a general rule.** The same SEC page lists five ways of measuring an index: point-to-point, high water mark, accrual, range, and shark fin. For point-to-point, the page does not say how a flat index is treated. For accrual and range, it does not say what the note pays on a flat or in-range market. So "expires worthless" is not something these sources say of every note.
- **My own check, not from a source.** For a plain point-to-point call, a flat index means zero payoff, by the arithmetic. The SEC page does not say this, so I count it as a reasoned check only.
- **Verdict on the claim:** UNVERIFIED as a general rule. True for the hypothetical the SEC gives; the sources do not settle the other measuring methods.

## A precision point (not a stranger trip)

- The SEC note-terms page says "The issuer generally raises this value by a spread to arrive at the offering price". The fetch tool reports that the spread "covers hedging costs and the issuer's profit". That last part is the tool's wording, not a quote, and needs a re-check.
- If so, "they spend that interest on an option" leaves out the bank's spread. I would not call the sentence false, because it says what the interest is spent on, but the sentence reads as if all of it goes to the option.

## What the sources do not settle

- **"Capital-protected".** The Moneysmart glossary (opened; no date on the page) defines it as "A product where investors are protected against significant loss of the amount invested. Also called capital protection." It adds: "Can contain clauses and performance hurdles that limit the protection." This is not a P5 trip, because P5 does not promise full protection. But a stranger reads "protected" as "safe", and the regulator's word is "significant loss".

---

## Pages tried and not opened

- **Investor.gov, "Structured Notes with Principal Protection"** (https://www.investor.gov/introduction-investing/investing-basics/investment-products/structured-notes-principal-protection). Reached by a 302 redirect from https://www.sec.gov/investor/alerts/structurednotes.htm. Opened: no mechanism on the page; it points to the note-terms alert in Find 2.
- **ASIC media release 13-093MR, "ASIC health check on capital protected products"** (1 May 2013; https://asic.gov.au/about-asic/news-centre/find-a-media-release/2013-releases/13-093mr-asic-health-check-on-capital-protected-products/). Opened: it covers reverse convertibles and internally geared products, not the bond-plus-option mechanism. No flat-market or fee text.
- **ASIC REP 340 and REP 341** (linked from 13-093MR). Not opened. They may hold more detail. UNVERIFIED.
- **Moneysmart, a current structured-products page.** My search returned no Moneysmart page on structured products. Nothing newer than the January 2013 guide was opened for the mechanism. Current ASIC wording is UNVERIFIED.
- **SEC press release 2011-118** (https://sec.gov/news/press/2011/2011-118.htm). In search results, not opened. Probably the same joint release as Find 3.
