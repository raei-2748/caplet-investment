# Source access check

Checked 2026-09-27 11:35 UTC from the run's cloud container (curl through the egress proxy; WebFetch uses the same policy).
Earlier the same day almost every primary site was blocked; the team widened network access before the run.

| Host | Result |
|---|---|
| home.treasury.gov | 200 reachable |
| fred.stlouisfed.org | 200 reachable |
| www.ishares.com | 200 reachable |
| am.jpmorgan.com | 200 reachable |
| globalyouth.wharton.upenn.edu | 200 reachable |
| magazine.wharton.upenn.edu | 200 reachable |
| lauragao.com | 200 reachable |
| en.wikipedia.org | 200 reachable |
| poetsandquantsforundergrads.com | 200 reachable |
| wghsinvcomp.smapply.us | 200 reachable (public pages only; logged-in pages not accessible) |
| www.federalreserve.gov | 200 reachable |
| nuvoices.com, legacy.diversebooks.org, www.bookweb.org, thenerddaily.com | reachable |
| www.apra.gov.au | 200 reachable |
| www.futurefund.gov.au | **403 refused by the site** (also with a browser user agent) |

Official competition files in the repo: both PDFs (client case, IPS guide) match the SHA-256 values in
`competition/official/2026_27/manifest.yaml`; text extractions are complete.

Python: `.venv` (Python 3.12) with numpy, scipy, pandas, matplotlib, pypdf. Both verified scripts re-run and reproduce
their recorded outputs ($292,264; lock-early surplus p5/p50/p95 $159k/$207k/$273k; growth-first 3.2% miss).

## What this teaches
Always record where a fact came from and whether you could open the original. "I couldn't reach the source" is a
finding, not a failure; guessing is the failure.
