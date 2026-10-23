// Runs the page's own compute core (lab_core.js) on the exported data and compares it with the numpy twin in
// build_page.py (data.check.cases). Exit 1 on any mismatch. WS8, AI-generated (Claude Code).
const fs = require("fs"), path = require("path");
const LabCore = require(path.join(__dirname, "lab_core.js"));
const data = JSON.parse(fs.readFileSync(path.join(__dirname, "lab_data.json"), "utf8"));
const P = LabCore.prepare(data);
const scen = Object.fromEntries(data.scenarios.map((s) => [s.key, s]));
let worstD = 0, worstP = 0, n = 0;
for (const c of data.check.cases) {
  const m = data.models[c.model], sc = scen[c.scenario];
  const r = LabCore.compute(P, { model: c.model, s: c.s, mu: m.mean, vol: m.sd, g31: sc.g31, rate: sc.rate });
  for (const k of Object.keys(c.expect)) {
    const d = Math.abs(r[k] - c.expect[k]);
    if (k.startsWith("p_")) worstP = Math.max(worstP, d); else worstD = Math.max(worstD, d);
  }
  n++;
}
const ok = worstD < 0.01 && worstP <= 2 / P.n;
console.log(`page JS (node) vs numpy twin on the stored data, ${n} cases: largest dollar gap $${worstD.toFixed(6)}, ` +
  `largest probability gap ${(worstP * 100).toFixed(4)} points -> ${ok ? "PASS" : "FAIL"}`);
process.exit(ok ? 0 : 1);
