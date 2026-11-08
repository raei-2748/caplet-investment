# Tools for the Final Report: skills, connectors and plugins, ranked

Ray, Sun 8 Nov 2026 (INSTRUCTIONS I94-I95): "Find useful skills online that would greatly increase our capabilities
for the final report", and "Use skills or find skills whever you meet a bottleneck or you feel like you are falling
short." Searched on 8 Nov: the in-product plugin, skill and connector directories, Anthropic's public skills and
financial-services repositories, and the open skills directory (skills.sh and `npx skills find` are blocked from this
container by the network proxy, so it was searched through the web instead).

## 1. Already connected; use from Mon 9 Nov

| Tool | What it adds to the Final Report | Use it for |
|---|---|---|
| Firecrawl data providers: FRED and the US Treasury's FiscalData | Official series straight from the source, with dates: historical Treasury yields, CPI, USD/TWD, recession dates | Q2, Q3, Q6, Q10; NUMBERS.md sources for the Works Cited |
| Consensus (400M+ peer-reviewed papers) | Real papers with authors, years and links, so no citation is invented | Q1 (human capital), Q8 (reliability), Q13 (decision-making), Q14 (charts and risk communication) |
| Firecrawl research and web search; Parallel search and fetch | Papers, essays, reports and primary pages read at the source | Every question; checking a source before it enters the Works Cited |
| Google Docs and Drive (read; write only the Research tabs) | Caplet's Final Report document, read only outside the Research tabs | Reading Caplet's text and their sentences; nothing else is edited |

## 2. Built-in skills; use at the step named

| Skill | What it adds | When |
|---|---|---|
| dataviz | One consistent, accessible chart system: chart choice, colour formula with a validator, mark specs | Exhibit designs (Mon 16), finished exhibits (Mon 23) |
| stop-slop | A checklist of machine-made writing patterns to remove | Every round of the writing session; Keel's diary entries |
| deep-research | Coordinated research across many sources, synthesised | The broad questions (Q4, Q9, Q11) and the "why Wharton" angle |
| pdf, docx | Reading Wharton's Final Report instructions if they arrive as files; producing a file if Caplet asks for one | Tue 10 Nov; Sat 28 Nov if a file is wanted |
| caplet-submission-standards | Caplet's own standards for submission text | Every review round |

## 3. A method adopted from Anthropic's doc-coauthoring skill: Reader Testing

Anthropic's public doc-coauthoring skill ends with a "Reader Testing" stage: predict the questions a real reader will
bring; give the document, and nothing else, to fresh readers with no context; ask them those questions; look for
ambiguity, assumed knowledge and contradictions; fix and repeat until their answers are right. It solves the problem
Caplet named after the IPS (Book 16: "COMPREHENSIBLE to humans, not just to fellow robots"), so it is built into the
plan: a fresh-reader test of every exhibit (Mon 23), a rehearsal on Caplet's submitted IPS (Wed 25), and a reader test
in every writing-session round (Fri 27). The readers are given the judge's questions: what does Laura get, how sure
is it, what can co-sponsors be told, what did the team learn.

## 4. Plugins worth adding to the account (the users' call; offered on a card in the thread)

| Plugin | What it adds | Note |
|---|---|---|
| Research Desk (community) | Checks that every reference in a list is real and says what it is cited for; critiques a paper; a "council" of differing reviewers | The Works Cited is judged; a check that each source exists is the cheapest insurance there is. Runs remote tools. |
| Copyedit and Proofreading (community) | Checks dates against weekdays, counts, percentages and consistency; compares the final text with an approved version | Useful in the last rounds and in review week. Self-contained. |
| Writing Desk (community) | Reference-writing helpers | Optional; overlaps with the two above. |

Installing a plugin changes the account, so it waits for Ray or Ahaan. Whether a plugin installed now loads in this
thread's scheduled runs is not certain; if it does not, its checks are done by hand with the tools in section 1.

## 5. Looked at and not taken

- Data Visualization plugin (Anthropic): the built-in dataviz skill already covers it.
- Citation Needed: installs a start-of-session hook with broad permissions; not worth the risk.
- Equity research, investment banking and private equity skill packs (Anthropic financial-services repository): built
  for pitch books and company valuation, not a fixed-payment liability plan. Its investment-proposal and client-report
  templates were read for structure only.
- Paid data connectors (FactSet, LSEG, Oxford Economics): paid accounts; the free official series in section 1 are
  the better sources for a Works Cited anyway. LSEG's fixed-income portfolio skill needs its connector.
- Alpha Vantage: needs an API key; adds nothing over FRED and Treasury data.
- alphaXiv: finance preprints; Consensus and Firecrawl's paper search cover the published work.

## 6. When a run hits a bottleneck

Name the bottleneck, classify the problem at its core (writing, persuasion, forecasting communication, project
management, computing, research), then look in this order: a skill above; the in-product skill and plugin search; how
people in that field solved it (`research/meta/HOW_STRATEGISTS_PLAN.md`, "Classify, then borrow"). Log what was tried in
`../pm/RUNLOG.md`.
