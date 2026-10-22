# Public SMApply pages, snapshot of 2026-10-20 (Sydney)

Text copies of two public pages of the competition site, fetched on 2026-10-19 at 23:32 UTC (Tue 20 Oct 10:32
Sydney) with plain `curl`, no login, and a cache-busting query string so no old copy was served:

| File | Live page | HTML sha256 |
|---|---|---|
| `faqs.txt` | https://wghsinvcomp.smapply.us/res/p/faqs/ | `73a9532ea7720c054265fcd12e82ecb1fd9d8deaa0a44f1407e18395329f7302` |
| `trading.txt` | https://wghsinvcomp.smapply.us/res/p/trading/ | `112709a77563f09fdf87fb0a31a610420ea26128ab6daecac803d652f2bff2a7` |

The HTML was turned into text in the same layout as the 14 Oct snapshot (`../smapply_public_2026-10-14/`): scripts
and styles dropped, one line per block, page `<title>` line dropped. The text is unedited. These pages contain no staff
email address. AI-prepared copy (Claude Code); the live pages are the authority.

## What changed since the 14 Oct snapshot

Line numbers are in this folder's files. Differences in spaces only (non-breaking or double spaces) are not listed.

| Page | Line | 14 Oct snapshot | Live 20 Oct |
|---|---|---|---|
| FAQ | 39 | "...how your portfolio performs over 10 weeks of trading." | "...how your portfolio performs over six weeks of trading." |
| FAQ | 42 | "Investments permitted (for BOTH contributions):" | "Investments permitted (for BOTH contributions, the IPS and Final Report):" |
| FAQ | 43 | "Any stock from any exchange available on WInS priced at $5 (or the equivalent of $5 in the local currency) or higher." | "Any stock from any exchange available on WInS." |
| FAQ | 52-53 | (absent) | Under "The following are NOT permitted:": "TIPS (Treasury Inflation-Protected Securities)" and "STRIPS (Separate Trading of Registered Interest and Principal of Securities)" |
| Trading | 43 | "Your team may invest in:" | "Your team may invest in (for BOTH contributions):" |
| Trading | 44 | "Stocks: Any stock available on WInS priced at $5 or more, or the equivalent of $5 in its local currency." | "Stocks: Any stock available on WInS." |

Notes:
- The TIPS/STRIPS lines appear on the FAQ page only. The Trading page's "Approved Securities" list does not name
  them, and its bond line still lists Treasury bonds from the US, UK, Germany, France, Italy and the Netherlands.
- The logged-in WInS Session Rules recorded a $3.00 minimum buy price on 29 Sep
  (`team/google_drive/sheets/portfolio_and_trading_notes/wins_notes.csv`). Whether that changed too is UNVERIFIED.
- The other five public pages (home, guide, client, deliverables, wins) were fetched at 23:35 UTC the same day and
  matched the 14 Oct snapshot apart from spaces, so they are not copied here.
- When exactly each change was made is not known from these two snapshots alone. The 14 Oct fetch time is not
  recorded.
