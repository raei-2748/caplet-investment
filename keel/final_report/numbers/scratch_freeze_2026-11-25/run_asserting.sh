#!/bin/bash
# Scratch for the 25 Nov freeze: run every numbers/ script that asserts its own figures, from the numbers folder,
# with python3 -I, a 200-second limit each; log pass/fail and seconds. Results files are hashed before and after
# by the caller (hash_numbers.sh), so any rewrite can be restored from git.
cd /home/user/caplet-investment/keel/final_report/numbers || exit 1
OUT=scratch_freeze_2026-11-25/run_log
mkdir -p "$OUT"
: > "$OUT/summary.tsv.tmp"
for s in "$@"; do
  t0=$(date +%s.%N)
  timeout 200 python3 -I "$s" > "$OUT/${s%.py}.out" 2>&1
  rc=$?
  t1=$(date +%s.%N)
  secs=$(python3 -c "print(round($t1-$t0,1))")
  printf "%s\t%s\t%s\n" "$s" "$rc" "$secs" >> "$OUT/summary.tsv.tmp"
done
cat "$OUT/summary.tsv.tmp"
