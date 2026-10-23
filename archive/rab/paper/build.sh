#!/bin/sh
# Build the Root-and-Branch working paper (RAB Kit, WS8). AI-generated for Team Caplet - not a competition submission.
# 1) number trace (fails on any untraceable key/file)  2) pdflatex + bibtex  3) report page counts.
# Figures come from rab/results/ (regenerate them first with `make -C rab models`).
set -e
cd "$(dirname "$0")"
PY=${PY:-/Users/ray/Research/rab-ws/.venv/bin/python}
TEXBIN=${TEXBIN:-/Library/TeX/texbin}
"$PY" make_trace.py
"$TEXBIN/pdflatex" -interaction=nonstopmode -halt-on-error RAB_working_paper.tex >/dev/null
"$TEXBIN/bibtex" RAB_working_paper >/dev/null
"$TEXBIN/pdflatex" -interaction=nonstopmode -halt-on-error RAB_working_paper.tex >/dev/null
"$TEXBIN/pdflatex" -interaction=nonstopmode -halt-on-error RAB_working_paper.tex >/dev/null
if grep -q "Citation.*undefined\|Reference.*undefined" RAB_working_paper.log; then
  echo "WARNING: undefined citations or references"; grep "undefined" RAB_working_paper.log | head
fi
PAGES=$(sed -n 's/^Output written on .*(\([0-9]*\) pages.*/\1/p' RAB_working_paper.log)
MAIN=$(sed -n 's/.*newlabel{lastmainpage}{{[^}]*}{\([0-9]*\)}.*/\1/p' RAB_working_paper.aux)
echo "PDF: $(pwd)/RAB_working_paper.pdf  pages total: ${PAGES:-?}  main text ends on page: ${MAIN:-?}"
