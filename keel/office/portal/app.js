/* Keel Office portal: a one-page app over window.KEEL (data.js, built by build_portal.py). */
(function () {
  "use strict";
  const K = window.KEEL;
  const app = document.getElementById("app");
  const tip = document.getElementById("tip");
  const LINE_COLOR = { "Caplet doc": "var(--s1)", "Keel": "var(--s2)", "Rewrite": "var(--s3)", "AI exemplar": "var(--s4)" };
  const LINES = ["Caplet doc", "Keel", "Rewrite", "AI exemplar"];
  const roomById = Object.fromEntries(K.rooms.map(r => [r.id, r]));
  const memberById = Object.fromEntries(K.members.map(m => [m.id, m]));

  // ---------- helpers ----------
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const syd = (iso, opts) => new Intl.DateTimeFormat("en-AU", Object.assign({ timeZone: "Australia/Sydney" }, opts)).format(new Date(iso));
  const sydDay = iso => syd(iso, { year: "numeric", month: "2-digit", day: "2-digit" }).split("/").reverse().join("-");
  const shortWhen = iso => syd(iso, { weekday: "short", day: "numeric", month: "short" }) + " " + syd(iso, { hour: "2-digit", minute: "2-digit", hour12: false });
  const plural = (n, w) => `${n} ${w}${n === 1 ? "" : "s"}`;
  const docLink = (path, label) => path ? `<a href="#/doc/${esc(path)}">${esc(label || path.split("/").pop())}</a>` : "";
  const gh = path => `${K.meta.repo}/blob/main/${path}`;
  function tone(s) {
    s = (s || "").toLowerCase();
    if (/^(on time|applied|done|answered|fixed|doing)/.test(s)) return "good";
    if (/^(late|partly|open)/.test(s)) return "warn";
    if (/^(ignored|no update|killed)/.test(s)) return "crit";
    return "";
  }
  const pill = s => `<span class="pill ${tone(s)}"><span class="dot"></span>${esc(s)}</span>`;
  function showTip(html, ev) {
    tip.innerHTML = html; tip.style.display = "block";
    const r = tip.getBoundingClientRect();
    let x = ev.clientX + 14, y = ev.clientY + 14;
    if (x + r.width > innerWidth - 8) x = ev.clientX - r.width - 14;
    if (y + r.height > innerHeight - 8) y = ev.clientY - r.height - 14;
    tip.style.left = Math.max(8, x) + "px"; tip.style.top = Math.max(8, y) + "px";
  }
  const hideTip = () => { tip.style.display = "none"; };

  // ---------- pixel avatars (16 x 16) ----------
  const FACE = [
    "................", "................", "................",
    "....kkkkkkkk....", "...kssssssssk...", "...kssssssssk...", "...kssessessk...", "...kssessessk...",
    "...kspsssspsk...", "...ksssmmsssk...", "....kssssssk....", "......kssk......",
    "..kkcccwwccckk..", ".kccccwttwcccck.", ".kcccccttccccck.", ".kcccccttccccck."];
  const TOP = ["................", "................", "....kkkkkkkk....", "...khhhhhhhhk...", "...khhhhhhhhk...", "...kh......hk..."];
  const HAIR = {
    nora: { rows: { 0: "..........kk....", 1: ".........khhk...", 2: "....kkkkkkhhk...", 3: "...khhhhhhhhkk..", 4: "...khhhhhhhhkhk.",
      5: "...kh......hkhk.", 6: "............khk.", 7: "............khk.", 8: ".............k.." },
      extra: { 4: "....aaaaaaaa...." } },
    felix: { rows: { 2: "....kkkkkkkk....", 3: "...khhhHHhhhk...", 4: "...kHhhhhhhhk...", 5: "...kh......hk..." },
      extra: { 5: ".....gggggg.....", 6: ".....g.gg.g.....", 7: ".....g.gg.g.....", 8: ".....gggggg....." } },
    jun: { rows: { 1: "......k.k.k.....", 2: "...aaaaaaaaaa...", 3: "...ahhhhhhhha...", 4: "...ahhHhhhhha...", 5: "..aah......haa..",
      6: "..aa........aa..", 7: "..aa........aa..", 8: "..aa........aa.." } },
    kai: { rows: { 1: ".....kkkkkk.....", 2: "....kaaaaaak....", 3: "...kaaaWaaaak...", 4: "..kbbbbbbbbbbk..", 5: "...kh......hk..." } },
    amara: { rows: { 2: "....kkkkkkkk....", 3: "...khhhHHhhhk...", 4: "..khhhhhhhhhhk..", 5: "..khh......hhk..",
      6: "..kh........hk..", 7: "..kh........hk..", 8: "..kh........hk..", 9: "..kh........hk..",
      10: "..khh......hhk..", 11: "..khhh....hhhk..", 12: "..khh......hhk.." } },
    tess: { rows: { 2: "....kkkkkkkk....", 3: "...khhhhhhhhk...", 4: "..khhhhhhhHhhk..", 5: "..khhhhhhhhhhk..",
      6: "..kh........hk..", 7: "..kh........hk..", 8: "..kh........hk..", 9: "..khh......hhk..", 10: "...kh......hk..." },
      extra: { 4: "..........aa...." } },
  };
  const BASE = { k: "#1d1b26", e: "#1d1b26", g: "#1d1b26", p: "#e88f8f", m: "#a5523f", w: "#f6f6f2", c: "#26355a", W: "#f6f6f2" };
  const PAL = {
    nora: { s: "#d6a47c", h: "#4a2c1d", H: "#6b432c", t: "#c0392b", a: "#e6b422", bg: "#f3e3c3" },
    felix: { s: "#f0c8a2", h: "#16161c", H: "#4a4a5a", t: "#2a78d6", bg: "#dce9f8" },
    jun: { s: "#edc29a", h: "#1b1a1f", H: "#45434c", t: "#1baf7a", a: "#9aa3ad", bg: "#daf1e8" },
    kai: { s: "#dcae86", h: "#121216", H: "#2e2e36", t: "#eb6834", a: "#d63c3c", b: "#9e2626", bg: "#fbe1d5" },
    amara: { s: "#a8714f", h: "#121014", H: "#3a3340", t: "#8e44ad", bg: "#ecdff3" },
    tess: { s: "#f6d2b5", h: "#c4612b", H: "#e8893f", t: "#eda100", a: "#f5d142", bg: "#fdf0cf" },
  };
  const sprites = {};
  function sprite(id) {
    if (sprites[id]) return sprites[id];
    const grid = FACE.map(r => r.padEnd(16, ".").slice(0, 16).split(""));
    const paint = rows => Object.entries(rows || {}).forEach(([y, row]) => row.split("").forEach((ch, x) => { if (ch !== "." && grid[y]) grid[y][x] = ch; }));
    const h = HAIR[id] || { rows: {} };
    paint(Object.fromEntries(TOP.map((r, i) => [i, h.rows[i] || r]).filter(([i]) => i >= 2)));
    paint(h.rows); paint(h.extra);
    const pal = Object.assign({}, BASE, PAL[id] || {});
    let rects = "";
    grid.forEach((row, y) => row.forEach((ch, x) => { if (ch !== "." && pal[ch]) rects += `<rect x="${x}" y="${y}" width="1.02" height="1.02" fill="${pal[ch]}"/>`; }));
    return (sprites[id] = { rects, bg: pal.bg });
  }
  function avatar(id, size, title) {
    const sp = sprite(id);
    return `<svg class="ava" width="${size}" height="${size}" viewBox="-1 -1 18 18" shape-rendering="crispEdges" role="img" aria-label="${esc(title || id)}"><rect x="-1" y="-1" width="18" height="18" fill="${sp.bg}"/>${sp.rects}</svg>`;
  }
  function whoAvatars(who, size) {
    const ids = /all six|everyone/i.test(who) ? K.members.map(m => m.id) : K.members.filter(m => who.includes(m.name)).map(m => m.id);
    return ids.map(id => avatar(id, size, memberById[id].name)).join("");
  }

  // ---------- charts ----------
  /* Charts are drawn at the width of their card (1 SVG unit = 1 CSS pixel), after the page is in the DOM. */
  let slots = [];
  function slot(render, wire) { const id = "chart" + slots.length; slots.push({ id, render, wire }); return `<div class="chart" id="${id}"></div>`; }
  function mount() {
    slots.forEach(sl => { const el = document.getElementById(sl.id); if (!el) return; el.innerHTML = sl.render(Math.max(260, Math.floor(el.clientWidth))); if (sl.wire) sl.wire(el); });
  }
  function chartFrame(w, h, pad) { return { w, h, pad, iw: w - pad.l - pad.r, ih: h - pad.t - pad.b }; }
  function ticks(lo, hi, n) {
    const step = Math.pow(10, Math.floor(Math.log10((hi - lo) / n || 1)));
    const s = [1, 2, 5, 10].map(m => m * step).find(m => (hi - lo) / m <= n) || step * 10;
    const out = []; for (let v = Math.ceil(lo / s) * s; v <= hi + 1e-9; v += s) out.push(v); return out;
  }
  /* Versions as dots on one value axis, coloured by line, with a limit rule. Click opens the version. */
  function versionChart(vs, field, limit, label, H) {
    return slot(W => versionSvg(vs, field, limit, label, W, H || 250), el => wireVersionChart(el, vs, field, "words"));
  }
  function versionSvg(vs, field, limit, label, W, H) {
    const f = chartFrame(W, H, { l: 40, r: 16, t: 14, b: 30 });
    const vals = vs.map(v => v[field]).filter(x => x > 0);
    if (!vals.length) return `<p class="empty">No ${esc(label)} yet.</p>`;
    let lo = Math.min(...vals, limit) , hi = Math.max(...vals, limit);
    const span = Math.max(hi - lo, limit * 0.1); lo = Math.max(0, Math.floor((lo - span * 0.15) / 5) * 5); hi = Math.ceil((hi + span * 0.12) / 5) * 5;
    const x = i => f.pad.l + (vs.length === 1 ? f.iw / 2 : i * f.iw / (vs.length - 1));
    const y = v => f.pad.t + f.ih - (v - lo) / (hi - lo) * f.ih;
    let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(label)} by version">`;
    ticks(lo, hi, 5).forEach(t => { s += `<line class="grid-l" x1="${f.pad.l}" x2="${W - f.pad.r}" y1="${y(t)}" y2="${y(t)}"/><text x="${f.pad.l - 6}" y="${y(t) + 4}" text-anchor="end">${t}</text>`; });
    s += `<line class="limit" x1="${f.pad.l}" x2="${W - f.pad.r}" y1="${y(limit)}" y2="${y(limit)}"/><text class="limit-t" x="${W - f.pad.r}" y="${y(limit) - 5}" text-anchor="end">limit ${limit}</text>`;
    const pts = vs.map((v, i) => v[field] > 0 ? `${x(i)},${y(v[field])}` : null).filter(Boolean);
    s += `<polyline class="trend" points="${pts.join(" ")}"/>`;
    const every = Math.ceil(vs.length / Math.max(2, Math.floor(f.iw / 46)));
    vs.forEach((v, i) => {
      if (i % every === 0 || i === vs.length - 1) s += `<text x="${x(i)}" y="${H - 10}" text-anchor="middle">V${v.n}</text>`;
      if (!(v[field] > 0)) return;
      s += `<circle class="mark" cx="${x(i)}" cy="${y(v[field])}" r="5.5" fill="${LINE_COLOR[v.line] || "var(--muted)"}" data-i="${i}"/>`;
    });
    const bw = f.iw / Math.max(vs.length - 1, 1);
    vs.forEach((v, i) => { s += `<rect class="hit" x="${x(i) - bw / 2}" y="${f.pad.t}" width="${bw}" height="${f.ih}" data-n="${v.n}" data-i="${i}" tabindex="0"><title>V${v.n}</title></rect>`; });
    return s + `</svg>`;
  }
  function wireVersionChart(root, vs, field, unit) {
    root.querySelectorAll(".hit").forEach(r => {
      const v = vs[+r.dataset.i];
      const show = ev => showTip(`<b>${v[field]} ${unit}</b><span class="k" style="background:${LINE_COLOR[v.line]}"></span>V${v.n} · ${esc(v.label)}<br><span class="muted">${esc(v.line)} · ${esc(v.date)}</span>`, ev);
      r.addEventListener("pointermove", show); r.addEventListener("pointerleave", hideTip);
      r.addEventListener("focus", () => { const b = r.getBoundingClientRect(); show({ clientX: b.left + b.width / 2, clientY: b.top + 40 }); });
      r.addEventListener("blur", hideTip);
      r.addEventListener("click", () => { hideTip(); location.hash = `#/ips/${v.n}`; });
      r.addEventListener("keydown", e => { if (e.key === "Enter") location.hash = `#/ips/${v.n}`; });
    });
  }
  function legendLines(lines) {
    return `<div class="legend">${lines.map(l => `<span><span class="key" style="background:${LINE_COLOR[l]};border-radius:50%"></span>${esc(l)}</span>`).join("")}</div>`;
  }
  function changeBars(vs) {
    const rows = vs.slice(1).map((v, i) => ({ v, share: changedShare(vs[i], v), pct: Math.round(changedShare(vs[i], v) * 100) }));
    return slot(W => changeSvg(rows, W), el => wireChangeBars(el, rows));
  }
  function changeSvg(rows, W) {
    const H = 190, f = chartFrame(W, H, { l: 40, r: 12, t: 10, b: 28 });
    const hi = Math.max(50, ...rows.map(r => r.pct));
    const bw = f.iw / Math.max(rows.length, 1);
    const y = p => f.pad.t + f.ih - p / hi * f.ih;
    let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Share of words changed from the previous version">`;
    ticks(0, hi, 4).forEach(t => { s += `<line class="grid-l" x1="${f.pad.l}" x2="${W - f.pad.r}" y1="${y(t)}" y2="${y(t)}"/><text x="${f.pad.l - 6}" y="${y(t) + 4}" text-anchor="end">${t}%</text>`; });
    rows.forEach((r, i) => {
      const x0 = f.pad.l + i * bw + 2, w = Math.max(bw - 4, 2), y0 = y(r.pct);
      const hgt = Math.max(f.pad.t + f.ih - y0, 1.5);
      s += `<path d="M${x0},${f.pad.t + f.ih} v${-(hgt - Math.min(4, hgt))} q0,-${Math.min(4, hgt)} ${Math.min(4, w / 2)},-${Math.min(4, hgt)} h${w - 2 * Math.min(4, w / 2)} q${Math.min(4, w / 2)},0 ${Math.min(4, w / 2)},${Math.min(4, hgt)} v${hgt - Math.min(4, hgt)} z" fill="${LINE_COLOR[r.v.line]}"/>`;
      if (i % Math.ceil(rows.length / Math.max(2, Math.floor(f.iw / 46))) === 0 || i === rows.length - 1) s += `<text x="${x0 + w / 2}" y="${H - 9}" text-anchor="middle">V${r.v.n}</text>`;
      s += `<rect class="hit" x="${f.pad.l + i * bw}" y="${f.pad.t}" width="${bw}" height="${f.ih}" data-i="${i}" tabindex="0"/>`;
    });
    return s + `<line class="axis-l" x1="${f.pad.l}" x2="${W - f.pad.r}" y1="${f.pad.t + f.ih}" y2="${f.pad.t + f.ih}"/></svg>`;
  }
  function wireChangeBars(root, rows) {
    root.querySelectorAll(".hit").forEach(h => {
      const r = rows[+h.dataset.i];
      const show = ev => showTip(`<b>${pctText(r.share)} of words changed</b>V${r.v.n - 1} → V${r.v.n} · ${esc(r.v.label)}`, ev);
      h.addEventListener("pointermove", show); h.addEventListener("pointerleave", hideTip);
      h.addEventListener("click", () => { hideTip(); location.hash = `#/compare/${r.v.n - 1}/${r.v.n}`; });
    });
  }
  const HEAT = ["var(--surface-2)", "#b7d3f6", "#6da7ec", "#2a78d6", "#184f95"];
  const heatStep = n => n === 0 ? 0 : n <= 2 ? 1 : n <= 5 ? 2 : n <= 10 ? 3 : 4;
  function heatmap(commits) {
    const byDay = {}; commits.forEach(c => { const d = sydDay(c.at); byDay[d] = (byDay[d] || 0) + 1; });
    const start = new Date("2026-09-27T00:00:00+10:00"); // a Sunday, the night before trading opened
    const today = sydDay(new Date().toISOString());
    let cells = "", d = new Date(start);
    for (let i = 0; i < 140; i++) {
      const key = sydDay(d.toISOString());
      if (key > today && d.getUTCDay() === 0) break;
      const n = byDay[key] || 0, future = key > today;
      cells += `<i data-d="${key}" data-n="${n}" style="background:${future ? "transparent" : HEAT[heatStep(n)]}${key === today ? ";outline:2px solid var(--ink);outline-offset:-1px" : ""}"></i>`;
      d = new Date(d.getTime() + 864e5);
    }
    return `<div class="heat" data-heat>${cells}</div><div class="heat-legend">less ${HEAT.map(c => `<i style="background:${c}"></i>`).join("")} more · one square per Sydney day, from Sun 27 Sep</div>`;
  }
  function wireHeat(root) {
    root.querySelectorAll("[data-heat] i").forEach(i => {
      i.addEventListener("pointermove", ev => showTip(`<b>${plural(+i.dataset.n, "commit")}</b>${new Date(i.dataset.d + "T12:00:00+11:00").toLocaleDateString("en-AU", { weekday: "short", day: "numeric", month: "short" })}`, ev));
      i.addEventListener("pointerleave", hideTip);
      i.addEventListener("click", () => { location.hash = `#/activity/${i.dataset.d}`; });
      i.style.cursor = "pointer";
    });
  }
  function hbars(items) {
    const hi = Math.max(1, ...items.map(i => i.n));
    return `<div class="bars">${items.map(i => `<div class="row"><a href="${i.href}" class="small">${esc(i.label)}</a><div class="track"><div class="fill" style="width:${i.n / hi * 100}%"></div></div><span class="num small">${i.n}</span></div>`).join("")}</div>`;
  }
  function headroomChart(eps) {
    const pts = eps.filter(e => e.headroom_bp != null);
    if (pts.length < 2) return "";
    return slot(W => headroomSvg(pts, W), el => wireHeadroom(el, pts, W0(el)));
  }
  const W0 = el => Math.max(260, Math.floor(el.clientWidth));
  function headroomSvg(pts, W) {
    const H = 220, f = chartFrame(W, H, { l: 40, r: 16, t: 12, b: 28 });
    const lo = Math.min(0, ...pts.map(p => p.headroom_bp)), hi = Math.max(...pts.map(p => p.headroom_bp)) + 5;
    const x = i => f.pad.l + i * f.iw / (pts.length - 1), y = v => f.pad.t + f.ih - (v - lo) / (hi - lo) * f.ih;
    let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Ladder headroom by episode">`;
    ticks(lo, hi, 4).forEach(t => { s += `<line class="grid-l" x1="${f.pad.l}" x2="${W - f.pad.r}" y1="${y(t)}" y2="${y(t)}"/><text x="${f.pad.l - 6}" y="${y(t) + 4}" text-anchor="end">${t}</text>`; });
    s += `<polyline fill="none" stroke="var(--s1)" stroke-width="2" points="${pts.map((p, i) => `${x(i)},${y(p.headroom_bp)}`).join(" ")}"/>`;
    const ev = Math.ceil(pts.length / Math.max(2, Math.floor(f.iw / 64)));
    pts.forEach((p, i) => { if (i % ev === 0 || i === pts.length - 1) s += `<text x="${x(i)}" y="${H - 9}" text-anchor="middle">${esc(p.date.replace(/^\w+ /, ""))}</text>`; });
    s += `<line class="xhair" x1="0" x2="0" y1="${f.pad.t}" y2="${f.pad.t + f.ih}" stroke="var(--ink-2)" stroke-width="1" visibility="hidden"/>`;
    return s + `<rect class="hit" x="${f.pad.l}" y="${f.pad.t}" width="${f.iw}" height="${f.ih}" data-head/></svg>`;
  }
  function wireHeadroom(root, pts, W) {
    const hit = root.querySelector("[data-head]"), xh = root.querySelector(".xhair");
    const meta = { l: 40, iw: W - 56, W };
    hit.addEventListener("pointermove", ev => {
      const b = hit.ownerSVGElement.getBoundingClientRect(), sx = (ev.clientX - b.left) / b.width * meta.W;
      const i = Math.max(0, Math.min(pts.length - 1, Math.round((sx - meta.l) / meta.iw * (pts.length - 1))));
      const px = meta.l + i * meta.iw / (pts.length - 1);
      xh.setAttribute("x1", px); xh.setAttribute("x2", px); xh.setAttribute("visibility", "visible");
      const p = pts[i];
      showTip(`<b>${p.headroom_bp} bp</b>Ep ${p.ep} · ${esc(p.date)} · ${esc(p.title)}`, ev);
    });
    hit.addEventListener("pointerleave", () => { hideTip(); xh.setAttribute("visibility", "hidden"); });
  }

  // ---------- word diff ----------
  const toks = s => (s || "").match(/\n\n|\S+|\s+/g) || [];
  function diffWords(a, b) {
    const A = toks(a).filter(t => !/^\s+$/.test(t) || t === "\n\n"), B = toks(b).filter(t => !/^\s+$/.test(t) || t === "\n\n");
    const n = A.length, m = B.length, L = new Uint16Array((n + 1) * (m + 1));
    for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--)
      L[i * (m + 1) + j] = A[i] === B[j] ? L[(i + 1) * (m + 1) + j + 1] + 1 : Math.max(L[(i + 1) * (m + 1) + j], L[i * (m + 1) + j + 1]);
    const ops = []; let i = 0, j = 0;
    while (i < n && j < m) {
      if (A[i] === B[j]) { ops.push(["=", A[i]]); i++; j++; }
      else if (L[(i + 1) * (m + 1) + j] >= L[i * (m + 1) + j + 1]) ops.push(["-", A[i++]]);
      else ops.push(["+", B[j++]]);
    }
    while (i < n) ops.push(["-", A[i++]]); while (j < m) ops.push(["+", B[j++]]);
    return { ops, common: L[0], n: A.filter(t => t !== "\n\n").length, m: B.filter(t => t !== "\n\n").length };
  }
  const diffCache = {};
  function changedShare(va, vb) {
    const key = va.n + ":" + vb.n;
    if (!(key in diffCache)) {
      const d = diffWords(va.pitch + "\n\n" + va.ips, vb.pitch + "\n\n" + vb.ips);
      diffCache[key] = d.n + d.m ? 1 - 2 * d.common / (d.n + d.m) : 0;
    }
    return diffCache[key];
  }
  function diffHtml(a, b) {
    const { ops } = diffWords(a, b);
    let out = "<p>", cur = null, buf = [];
    const flush = () => { if (!buf.length) return; const t = buf.join(" "); out += cur === "+" ? `<ins>${esc(t)}</ins> ` : cur === "-" ? `<del>${esc(t)}</del> ` : esc(t) + " "; buf = []; };
    ops.forEach(([op, t]) => {
      if (t === "\n\n") { flush(); cur = null; if (op !== "-") out += "</p><p>"; return; }
      if (op !== cur) { flush(); cur = op; }
      buf.push(t);
    });
    flush();
    return out + "</p>";
  }
  const pctText = x => x > 0 && x < 0.005 ? "<1%" : Math.round(x * 100) + "%";
  const paras = t => (t || "").split(/\n\s*\n/).filter(p => p.trim()).map(p => `<p>${esc(p.trim())}</p>`).join("");

  // ---------- pages ----------
  const latest = () => K.ips[K.ips.length - 1];
  function countdowns() {
    const now = Date.now();
    return K.meta.deadlines.map(d => {
      const ms = new Date(d.at) - now, days = Math.floor(ms / 864e5), hrs = Math.floor(ms % 864e5 / 36e5);
      const when = syd(d.at, { weekday: "short", day: "numeric", month: "short" }) + " " + syd(d.at, { hour: "2-digit", minute: "2-digit", hour12: false });
      return `<div class="tile"><span class="px">${esc(d.name)}</span><b class="num">${ms > 0 ? `${days}d ${hrs}h` : "passed"}</b><span>${esc(when)} Sydney (${esc(d.et)})</span></div>`;
    }).join("");
  }
  function roomCard(r) {
    return `<a class="card room-card" href="#/room/${r.id}">
      <div class="top-row"><h3>${esc(r.name)}</h3>${pill(r.health)}</div>
      <div class="who">${whoAvatars(r.who, 26)}</div>
      <p class="doing" style="margin:0">${esc(r.doing !== "—" ? r.doing : "No Now block yet.")}</p>
      <div class="foot"><span>${esc(r.schedule)}</span><span>${plural(r.commits, "commit")} · ${plural(r.memos, "memo")}</span></div></a>`;
  }
  function commitFeed(cs, n) {
    if (!cs.length) return `<p class="empty">No commits.</p>`;
    return `<ul class="feed">${cs.slice(0, n).map(c => `<li><time datetime="${esc(c.at)}">${esc(shortWhen(c.at))}</time><div>${esc(c.subject)}<div class="room">${c.room ? `<a href="#/room/${c.room}">${esc(roomById[c.room].name)}</a> · ` : ""}${plural(c.files, "file")} · <a href="${K.meta.repo}/commit/${c.sha}" target="_blank" rel="noopener">${esc(c.sha)}</a></div></div></li>`).join("")}</ul>`;
  }
  function memoList(ms, n) {
    if (!ms.length) return `<p class="empty">No memos yet.</p>`;
    return `<ul class="feed">${ms.slice(0, n).map(m => `<li><time>${esc(m.date)}</time><div><a href="#/doc/${esc(m.path)}">${esc(m.title)}</a>${m.takes.length ? `<div class="room">takes: ${m.takes.map(t => esc(t.name)).join(", ")}</div>` : ""}</div></li>`).join("")}</ul>`;
  }

  function bibleCard() {
    const B = K.bible;
    if (!B || !B.rules) return "";
    const byName = Object.fromEntries(K.members.map(m => [m.name.split(" ")[0], m]));
    return `<section class="card bible"><div class="sec-head"><span class="tag px">The bible · nine books (Wharton's three rank first) · read first, every run</span><a href="#/doc/${esc(B.doc)}">Read all nine books →</a></div>
      <blockquote>${esc(B.quote)}<cite>${esc(B.said)}</cite></blockquote>
      ${B.books && B.books.length ? `<ul class="books">${B.books.map(b => `<li><a href="#/doc/${esc(B.doc)}"><span class="px">${esc(b.title.split(":")[0])}</span>${esc(b.title.split(": ").slice(1).join(": "))}<span class="tiny muted">${esc(b.date)}</span></a></li>`).join("")}</ul>` : ""}
      <h3 style="margin:1rem 0 0">Keel's reading: the rules every run applies</h3>
      <ol class="rules">${B.rules.map(r => `<li><b>${esc(r.lead)}</b> ${esc(r.text)}</li>`).join("")}</ol>
      ${B.takes.length ? `<div class="sec-head" style="margin-top:1rem"><h2>What Book 5 changes for each of us</h2><a href="#/doc/${esc(B.takes_doc)}">All six takes →</a></div>
      <div class="takes">${B.takes.map(t => { const m = byName[t.name]; return `<div class="take-card">${m ? `<a href="#/member/${m.id}">${avatar(m.id, 40, m.name)}</a>` : ""}<div><span class="px">${esc(t.name)}</span> <span class="tiny muted">${esc(t.room)}</span><p>${esc(t.text)}</p></div></div>`; }).join("")}</div>` : ""}
    </section>`;
  }

  function pageHome() {
    const v = latest(), prev = K.ips[K.ips.length - 2];
    const danger = K.asks.filter(a => a.status.startsWith("Danger")).length, calls = K.asks.filter(a => a.status === "Keel's call").length;
    const day = Date.now() - 864e5, week = Date.now() - 7 * 864e5;
    const c24 = K.commits.filter(c => new Date(c.at) > day).length;
    const onTime = K.rooms.filter(r => r.health === "on time").length;
    const week7 = K.rooms.map(r => ({ label: r.name.replace(/^The /, ""), href: `#/room/${r.id}`, n: K.commits.filter(c => c.room === r.id && new Date(c.at) > week).length })).sort((a, b) => b.n - a.n);
    const chg = prev ? pctText(changedShare(prev, v)) : "0%";
    app.innerHTML = `
      <section class="hero"><div>${avatarsRow(44)}</div><div><h1>The office, live</h1>
        <p class="lede">Six simulated students working for Team Caplet in the Wharton Global High School Investment Competition. Every room's run, every IPS draft and every commit, straight from the repo. Updated ${esc(K.meta.built)}.</p></div></section>
      ${bibleCard()}
      <section class="tiles">${countdowns()}</section>
      <section class="tiles">
        <a class="tile" href="#/ips/${v.n}"><span class="px">Latest IPS</span><b class="num">V${v.n}</b><span>${esc(v.label)} · ${v.ips_words}/500 words</span></a>
        <a class="tile" href="#/rooms"><span class="px">Rooms on time</span><b class="num">${onTime}/${K.rooms.length}</b><span>${esc(K.meta.health)}</span></a>
        <a class="tile" href="#/activity"><span class="px">Commits, 24 h</span><b class="num">${c24}</b><span>${K.commits.length} since 27 Sep</span></a>
        <a class="tile" href="#/plan"><span class="px">Danger zone: yours</span><b class="num">${danger}</b><span>Keel made the other ${calls} calls itself</span></a>
      </section>
      <section class="two">
        <div class="card"><div class="sec-head"><h2>IPS: ${K.ips.length} versions so far</h2><a href="#/ips">All versions and diffs →</a></div>
          <p class="small muted" style="margin:.3rem 0 .4rem">IPS words by version (strict count). Click a dot to read that version.</p>
          ${legendLines(LINES.filter(l => K.ips.some(x => x.line === l)))}${versionChart(K.ips, "ips_words", 500, "IPS words", 230)}</div>
        <div class="card"><span class="tag">Latest · V${v.n} · ${esc(v.date)}</span><h2 style="margin:.5rem 0 .3rem">${esc(v.label)}</h2>
          <p class="small ink2" style="margin:0 0 .6rem">${esc(v.note)}</p>
          <div class="vstats"><div><b class="num">${v.pitch_words}</b><span>pitch words (limit 50)</span></div><div><b class="num">${v.ips_words}</b><span>IPS words (limit 500)</span></div>
          <div><b class="num">${chg}</b><span>changed from V${prev ? prev.n : "-"}</span></div><div><b class="num">${v.sentences}</b><span>sentences</span></div></div>
          <p class="small" style="margin:.9rem 0 0"><a href="#/ips/${v.n}">Read V${v.n}</a>${prev ? ` · <a href="#/compare/${prev.n}/${v.n}">What changed from V${prev.n}</a>` : ""}</p></div>
      </section>
      <section><div class="sec-head"><h2>The six</h2><a href="#/team">Profiles →</a></div>
        <div class="team-strip">${K.members.map(m => `<a href="#/member/${m.id}">${avatar(m.id, 64, m.name)}<span class="px">${esc(m.name)}</span><span class="tiny muted">${esc(m.home)}</span></a>`).join("")}</div></section>
      <section><div class="sec-head"><h2>Rooms</h2><span class="small muted">Click a room for its decisions, runs, memos and work</span></div>
        <div class="grid">${K.rooms.map(roomCard).join("")}</div></section>
      <section class="two">
        <div class="card"><div class="sec-head"><h2>What changed for the judges</h2><a href="#/plan">Plan →</a></div>
          ${K.changes.length ? `<ul class="feed">${K.changes.slice(0, 8).map(c => `<li><time>${esc(c.date)}</time><div>${esc(c.name)}<div class="room">${esc(c.deliverable)} · ${esc(c.owner)}</div></div></li>`).join("")}</ul>` : `<p class="empty">No draft changes logged.</p>`}</div>
        <div class="card"><div class="sec-head"><h2>Latest commits</h2><a href="#/activity">All activity →</a></div>${commitFeed(K.commits, 8)}</div>
      </section>
      <section class="two">
        <div class="card"><h2>Work by day</h2><p class="small muted" style="margin:.2rem 0 .7rem">Commits to Keel's files. Click a day.</p>${heatmap(K.commits)}</div>
        <div class="card"><h2>Commits by room, last 7 days</h2><p class="small muted" style="margin:.2rem 0 .7rem">Rooms named in the commit or owning every file in it.</p>${hbars(week7)}</div>
      </section>`;
    wireHeat(app);
  }
  const avatarsRow = size => `<div style="display:flex;gap:4px;flex-wrap:wrap">${K.members.map(m => `<a href="#/member/${m.id}" title="${esc(m.name)}">${avatar(m.id, size, m.name)}</a>`).join("")}</div>`;

  function pageIps() {
    const vs = K.ips;
    const present = LINES.filter(l => vs.some(x => x.line === l));
    app.innerHTML = `
      <div><div class="crumbs"><a href="#/more">More</a>›<span>IPS</span></div><h1>The IPS, version by version</h1>
        <p class="lede">Every full draft of the pitch and the IPS, numbered for good (register: ${docLink("keel/ips_rewrite/VERSIONS.md", "VERSIONS.md")}). Caplet doc versions are the team's own Google Doc tabs; everything else is an AI DRAFT for Caplet to rewrite. Word counts are the strict count (a hyphen splits a word), the one to keep under the limit.</p></div>
      ${judgedCard()}
      <section class="card"><div class="sec-head"><h2>IPS words</h2>${legendLines(present)}</div>${versionChart(vs, "ips_words", 500, "IPS words")}</section>
      <section class="two">
        <div class="card"><h2>Pitch words</h2>${versionChart(vs, "pitch_words", 50, "pitch words")}</div>
        <div class="card"><h2>How much each version changed</h2><p class="small muted" style="margin:.2rem 0 .3rem">Share of words added or removed against the version before. Click to see the diff.</p>${changeBars(vs)}</div>
      </section>
      <section class="card"><div class="sec-head"><h2>Compare any two</h2></div>
        <div class="diff-bar"><select id="ca">${vs.map(v => `<option value="${v.n}">V${v.n} · ${esc(v.label)}</option>`).join("")}</select><span>→</span>
        <select id="cb">${vs.map(v => `<option value="${v.n}">V${v.n} · ${esc(v.label)}</option>`).join("")}</select>
        <button class="chip" id="go" type="button">Show changes</button></div></section>
      <section><div class="tbl"><table><thead><tr><th>V</th><th>Version</th><th>Date</th><th>Line</th><th class="n">Pitch</th><th class="n">IPS</th><th class="n">Changed</th><th>What changed</th></tr></thead><tbody>
        ${vs.slice().reverse().map(v => { const i = vs.indexOf(v); return `<tr class="click" data-n="${v.n}"><td class="num"><b>V${v.n}</b></td><td>${esc(v.label)}</td><td>${esc(v.date)}</td><td><span class="key" style="background:${LINE_COLOR[v.line]};border-radius:50%"></span>${esc(v.line)}</td><td class="n">${v.pitch_words || "–"}</td><td class="n" style="${v.ips_words > 500 ? "color:var(--crit)" : ""}">${v.ips_words}</td><td class="n">${i ? pctText(changedShare(vs[i - 1], v)) : "–"}</td><td class="w small">${esc(v.note)}</td></tr>`; }).join("")}
      </tbody></table></div></section>`;
    const ca = app.querySelector("#ca"), cbx = app.querySelector("#cb");
    ca.value = vs[Math.max(0, vs.length - 2)].n; cbx.value = vs[vs.length - 1].n;
    app.querySelector("#go").addEventListener("click", () => { location.hash = `#/compare/${ca.value}/${cbx.value}`; });
    app.querySelectorAll("tr[data-n]").forEach(tr => tr.addEventListener("click", () => { location.hash = `#/ips/${tr.dataset.n}`; }));
  }

  function versionStats(v) {
    const meter = (n, lim) => `<div class="meter ${n > lim ? "over" : ""}"><i style="width:${Math.min(100, n / lim * 100)}%"></i></div>`;
    return `<div class="card side"><div><span class="tag">V${v.n}</span> <span class="tag" style="color:${LINE_COLOR[v.line]}">${esc(v.line)}</span></div>
      <div><div class="sec-head"><span class="small">Pitch</span><b class="num">${v.pitch_words} / 50</b></div>${meter(v.pitch_words, 50)}</div>
      <div><div class="sec-head"><span class="small">IPS</span><b class="num">${v.ips_words} / 500</b></div>${meter(v.ips_words, 500)}</div>
      <div class="vstats"><div><b class="num">${v.sentences}</b><span>sentences</span></div><div><b class="num">${v.mean_sentence}</b><span>words a sentence</span></div>
      <div><b class="num">${v.longest_sentence}</b><span>longest sentence</span></div><div><b class="num">${v.short_lines}</b><span>sentences of 6 words or fewer</span></div></div>
      <p class="small ink2" style="margin:0">${esc(v.note)}</p>
      <p class="small" style="margin:0">Source: ${[v.pitch_src, v.ips_src].filter((s, i, a) => s && a.indexOf(s) === i).map(s => docLink(s, s.replace(/^keel\//, "")) || `<a href="${gh(s)}" target="_blank" rel="noopener">${esc(s)}</a>`).join(", ")}</p></div>`;
  }
  function pageVersion(n) {
    const vs = K.ips, i = vs.findIndex(v => v.n === +n);
    if (i < 0) return notFound();
    const v = vs[i], prev = vs[i - 1], next = vs[i + 1];
    app.innerHTML = `
      <div><div class="crumbs"><a href="#/more">More</a>›<a href="#/ips">IPS</a>›<span>V${v.n}</span></div>
        <h1>V${v.n} · ${esc(v.label)}</h1><p class="lede">${esc(v.date)} · ${esc(v.line)}${v.line === "Caplet doc" ? " (the team's own draft)" : " (AI DRAFT for Caplet to rewrite)"}</p></div>
      <div class="diff-bar">${prev ? `<a class="chip" href="#/ips/${prev.n}">← V${prev.n}</a>` : ""}${next ? `<a class="chip" href="#/ips/${next.n}">V${next.n} →</a>` : ""}
        ${prev ? `<span class="seg" role="group"><button type="button" data-m="text" aria-pressed="true">Text</button><button type="button" data-m="diff" aria-pressed="false">Changes from V${prev.n}</button></span>` : ""}</div>
      <section class="two"><div class="card"><div class="prose ips-text" id="vt"></div></div>${versionStats(v)}</section>`;
    const vt = app.querySelector("#vt");
    const show = mode => {
      app.querySelectorAll(".seg button").forEach(b => b.setAttribute("aria-pressed", b.dataset.m === mode));
      vt.innerHTML = mode === "diff" && prev
        ? `<h3>Pitch</h3>${diffHtml(prev.pitch, v.pitch)}<h3>IPS</h3>${diffHtml(prev.ips, v.ips)}`
        : `${v.pitch ? `<h3>Elevator pitch</h3>${paras(v.pitch)}` : ""}<h3>Investment Policy Statement</h3>${paras(v.ips)}`;
    };
    app.querySelectorAll(".seg button").forEach(b => b.addEventListener("click", () => show(b.dataset.m)));
    show("text");
  }
  function pageCompare(a, b) {
    const va = K.ips.find(v => v.n === +a), vb = K.ips.find(v => v.n === +b);
    if (!va || !vb) return notFound();
    const pct = pctText(changedShare(va, vb));
    app.innerHTML = `
      <div><div class="crumbs"><a href="#/more">More</a>›<a href="#/ips">IPS</a>›<span>Compare</span></div>
        <h1>V${va.n} → V${vb.n}</h1><p class="lede"><del>Removed</del> and <ins>added</ins> words, from ${esc(va.label)} to ${esc(vb.label)}. ${pct} of words changed; IPS ${va.ips_words} → ${vb.ips_words}, pitch ${va.pitch_words} → ${vb.pitch_words}.</p></div>
      <div class="diff-bar"><a class="chip" href="#/ips/${va.n}">Read V${va.n}</a><a class="chip" href="#/ips/${vb.n}">Read V${vb.n}</a></div>
      <section class="card"><div class="prose ips-text"><h3>Pitch</h3>${diffHtml(va.pitch, vb.pitch)}<h3>IPS</h3>${diffHtml(va.ips, vb.ips)}</div></section>`;
  }

  function pageRooms() {
    app.innerHTML = `<div><div class="crumbs"><a href="#/more">More</a>›<span>Rooms</span></div><h1>Twelve rooms</h1>
      <p class="lede">Each room is a scheduled run. At the end of every run it updates its "Now" block, logs what it made and pushes; this page reads those files. "Late" means it missed its schedule.</p></div>
      <div class="grid">${K.rooms.map(roomCard).join("")}</div>`;
  }
  function pageRoom(id) {
    const r = roomById[id];
    if (!r) return notFound();
    const cs = K.commits.filter(c => c.room === id), ms = K.memos.filter(m => m.room === id), rl = K.runlog.filter(x => x.rid === id);
    const people = K.members.filter(m => /all six|everyone/i.test(r.who) || r.who.includes(m.name));
    const week = Date.now() - 7 * 864e5, c7 = cs.filter(c => new Date(c.at) > week).length;
    const last = cs.length ? shortWhen(cs[0].at) : "–";
    // Decisions: the current one first, then what the room decided before (git history of its Now block)
    const decs = (r.decisions || []).slice();
    if (r.decided && !decs.some(d => d.text === r.decided)) decs.unshift({ date: "Now · " + (r.updated || ""), text: r.decided });
    // Work, grouped by folder; long groups fold away
    const groups = {};
    r.work.forEach(w => { const f = w.path.replace(/^keel\//, "").split("/").slice(0, -1).join("/") || "keel"; (groups[f] = groups[f] || []).push(w); });
    const tidy = t => t.replace(/^FICTION(\s*\([^)]*\))?(\s*\+\s*real [^.]*)?\.\s*/i, "");
    const workItem = w => `<li><a href="#/doc/${esc(w.path)}"><span>${esc(tidy(w.title))}</span><span class="tiny muted">${esc(w.path.split("/").pop())}</span></a></li>`;
    const workHtml = Object.entries(groups).map(([f, ws]) => `<div class="wgroup"><h3 class="px">${esc(f)} <span class="muted">${ws.length}</span></h3>
      <ul class="folder">${ws.slice(0, 6).map(workItem).join("")}</ul>${ws.length > 6 ? `<details><summary>${ws.length - 6} more</summary><ul class="folder">${ws.slice(6).map(workItem).join("")}</ul></details>` : ""}</div>`).join("");
    // Latest outputs: run-log rows and memos, newest first
    const outs = [...rl.map(x => ({ when: x.date, kind: "Run", text: x.output, sub: x.aim ? `aimed at ${x.aim}` : "", href: "" })),
      ...ms.map(m => ({ when: m.date, kind: "Memo", text: m.title, sub: m.takes.length ? `takes: ${m.takes.map(t => t.name).join(", ")}` : "", href: `#/doc/${m.path}` }))].slice(0, 6);
    app.innerHTML = `
      <div><div class="crumbs"><a href="#/more">More</a>›<a href="#/rooms">Rooms</a>›<span>${esc(r.name)}</span></div>
        <div class="hero"><div class="who" style="display:flex;gap:4px">${people.map(m => `<a href="#/member/${m.id}">${avatar(m.id, 48, m.name)}</a>`).join("")}</div>
        <div><h1>${esc(r.name)}</h1><p class="lede">${esc(r.who)} · ${esc(r.schedule)} · ${pill(r.health)}</p></div></div></div>
      <section class="card room-now"><div class="sec-head"><span class="tag px">Right now</span><span class="small muted">updated ${esc(r.updated)}</span></div>
        <p class="doing">${esc(r.doing || "Nothing logged yet.")}</p>
        <div class="now-grid"><div><span class="px">Decided</span><p>${esc(r.decided || "–")}</p></div><div><span class="px">Next</span><p>${esc(r.next || "–")}</p></div><div><span class="px">Why it matters to the judges</span><p>${esc(r.for_judges || "–")}</p></div></div>
        <p class="small" style="margin:.8rem 0 0">${[docLink(r.runbook, "How this room works"), docLink(r.log, "Room log")].filter(Boolean).join(" · ")}</p></section>
      <section class="tiles">
        <div class="tile"><span class="px">Runs logged</span><b class="num">${rl.length}</b></div>
        <div class="tile"><span class="px">Memos</span><b class="num">${ms.length}</b></div>
        <div class="tile"><span class="px">Commits, 7 days</span><b class="num">${c7}</b><span>${cs.length} in all</span></div>
        <div class="tile"><span class="px">Last activity</span><b class="num" style="font-size:1.1rem">${esc(last)}</b></div>
      </section>
      <section class="two">
        <div class="card"><h2>Decisions</h2>${decs.length ? `<ol class="timeline">${decs.map((d, i) => `<li${i ? "" : ' class="current"'}><time>${esc(d.date)}</time><p>${esc(d.text)}</p></li>`).join("")}</ol>` : `<p class="empty">No decisions logged yet.</p>`}</div>
        <div class="card"><h2>Latest output</h2>${outs.length ? `<ul class="outs">${outs.map(o => `<li><span class="kind">${o.kind}</span><div>${o.href ? `<a href="${esc(o.href)}">${esc(o.text)}</a>` : esc(o.text)}<div class="tiny muted">${esc(o.when)}${o.sub ? " · " + esc(o.sub) : ""}</div></div></li>`).join("")}</ul>` : `<p class="empty">Nothing yet.</p>`}</div>
      </section>
      ${r.work.length ? `<section class="card"><div class="sec-head"><h2>Work this room made</h2><span class="small muted">${plural(r.work.length, "file")}</span></div><div class="wgroups">${workHtml}</div></section>` : ""}
      <section class="history"><h2>History</h2>
        ${rl.length ? `<details><summary>Run log <span class="muted">${rl.length}</span></summary><div class="tbl"><table><thead><tr><th>When</th><th>Output</th><th>Aimed at</th><th>Used by</th></tr></thead><tbody>${rl.map(x => `<tr><td>${esc(x.date)}</td><td class="w">${esc(x.output)}</td><td>${esc(x.aim)}</td><td>${esc(x.used_by)}</td></tr>`).join("")}</tbody></table></div></details>` : ""}
        ${ms.length ? `<details><summary>All memos <span class="muted">${ms.length}</span></summary>${memoList(ms, 100)}</details>` : ""}
        ${cs.length ? `<details><summary>All commits <span class="muted">${cs.length}</span></summary>${commitFeed(cs, 200)}</details>` : ""}
        ${r.log ? `<details id="logbox"><summary>Full room log</summary><div class="doc" id="roomlog"><p class="muted">Loading…</p></div></details>` : ""}
      </section>`;
    const lb = app.querySelector("#logbox");
    if (lb) lb.addEventListener("toggle", () => { if (lb.open && !lb.dataset.done) { lb.dataset.done = 1; loadDoc(r.log, app.querySelector("#roomlog")); } });
  }

  function pageTeam() {
    app.innerHTML = `<div><div class="crumbs"><a href="#/more">More</a>›<span>Team</span></div><h1>The six</h1>
      <p class="lede">Year 11 at a Sydney selective school, all fictional. Each heads a room and speaks in the memos; the latest take is from the newest memo or stand-up.</p></div>
      <div class="grid wide">${K.members.map(m => `<a class="card member-card" href="#/member/${m.id}">${avatar(m.id, 88, m.name)}<div><h2 class="px">${esc(m.name)}</h2><div class="small muted">${esc(m.role)}</div><p class="take">${esc(m.take)}</p><span class="tag">${esc(m.home)}</span></div></a>`).join("")}</div>`;
  }
  function pageMember(id) {
    const m = memberById[id];
    if (!m) return notFound();
    const takes = K.memos.flatMap(x => x.takes.filter(t => t.name === m.name).map(t => ({ ...t, memo: x }))).slice(0, 12);
    const prof = Object.entries(m.profile).filter(([, v]) => v);
    app.innerHTML = `
      <div><div class="crumbs"><a href="#/more">More</a>›<a href="#/team">Team</a>›<span>${esc(m.name)}</span></div>
      <div class="hero">${avatar(m.id, 128, m.name)}<div><h1 class="px">${esc(m.full)}</h1><p class="lede">${esc(m.role)} · home room <a href="#/room/${m.home_id}">${esc(m.home)}</a>${m.doc ? ` · ${docLink(m.doc, "full profile")}` : ""}</p>
      <p class="notice fiction" style="margin:.7rem 0 0">Keel is a simulated team, AI-written. None of the six is based on a real person.</p></div></div></div>
      <section class="two"><div class="card"><h2>Latest take</h2><p class="prose" style="margin:.4rem 0 0">${esc(m.take)}</p><p class="small muted">${esc(m.take_date)}</p></div>
        <div class="card"><dl class="now">${prof.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("")}</dl></div></section>
      ${(K.bible && K.bible.takes || []).filter(t => t.name === m.name.split(" ")[0]).map(t => `<section class="card bible"><span class="tag px">On the bible</span><p style="margin:.5rem 0 0">${esc(t.text)}</p><p class="small" style="margin:.4rem 0 0"><a href="#/doc/${esc(K.bible.doc)}">Read the bible →</a></p></section>`).join("")}
      <section class="card"><h2>In the memos</h2>${takes.length ? `<ul class="feed">${takes.map(t => `<li><time>${esc(t.memo.date)}</time><div>${esc(t.text)}<div class="room"><a href="#/doc/${esc(t.memo.path)}">${esc(t.memo.title)}</a></div></div></li>`).join("")}</ul>` : `<p class="empty">No labelled takes yet.</p>`}</section>`;
  }

  function pageActivity(day) {
    let cs = K.commits, rf = "";
    if (day) cs = cs.filter(c => sydDay(c.at) === day);
    const render = () => {
      const list = rf ? cs.filter(c => c.room === rf) : cs;
      app.querySelector("#feed").innerHTML = commitFeed(list, 400);
      app.querySelectorAll(".chip[data-r]").forEach(b => b.setAttribute("aria-pressed", b.dataset.r === rf));
    };
    const total = {}; K.commits.forEach(c => { total[c.room || ""] = (total[c.room || ""] || 0) + 1; });
    app.innerHTML = `
      <div><div class="crumbs"><a href="#/more">More</a>›<span>Activity</span></div><h1>Activity${day ? ` on ${esc(day)}` : ""}</h1>
        <p class="lede">Every commit to Keel's files${day ? ` that day (<a href="#/activity">all days</a>)` : ""}, newest first, including today's day branch before it is merged.</p></div>
      <section class="card">${heatmap(K.commits)}</section>
      <section class="card"><h2>All-time commits by room</h2><div style="margin-top:.6rem">${hbars(K.rooms.map(r => ({ label: r.name.replace(/^The /, ""), href: `#/room/${r.id}`, n: total[r.id] || 0 })).sort((a, b) => b.n - a.n))}</div></section>
      <section class="card"><div class="filters"><button class="chip" data-r="" type="button">All rooms</button>${K.rooms.map(r => `<button class="chip" data-r="${r.id}" type="button">${esc(r.name.replace(/^The /, ""))}</button>`).join("")}</div><div id="feed" style="margin-top:.6rem"></div></section>
      <section><h2>Run log</h2><div class="tbl"><table><thead><tr><th>When</th><th>Room</th><th>Output</th><th>Aimed at</th></tr></thead><tbody>${K.runlog.map(x => `<tr><td>${esc(x.date)}</td><td>${x.rid ? `<a href="#/room/${x.rid}">${esc(x.room)}</a>` : esc(x.room)}</td><td class="w">${esc(x.output)}</td><td>${esc(x.aim)}</td></tr>`).join("")}</tbody></table></div></section>`;
    app.querySelectorAll(".chip[data-r]").forEach(b => b.addEventListener("click", () => { rf = b.dataset.r; render(); }));
    wireHeat(app); render();
  }

  function pageEpisodes() {
    const eps = K.episodes;
    app.innerHTML = `<div><div class="crumbs"><a href="#/more">More</a>›<span>Episodes</span></div><h1>The season so far</h1>
      <p class="lede">A daily episode since the night before trading opened. Fiction: the events are made up, the research inside them is real and dated.</p></div>
      ${eps.some(e => e.headroom_bp != null) ? `<section class="card"><h2>Ladder headroom under $300,000, by episode (bp)</h2><p class="small muted" style="margin:.2rem 0 .3rem">Jun's daily price of the payment ladder (MODEL, previous U.S. close). Lower means less room before the ladder costs more than the 2027 deposit.</p>${headroomChart(eps)}</section>` : ""}
      <section class="grid wide">${eps.slice().reverse().map(e => `<a class="card" href="#/doc/${esc(e.path)}"><div class="sec-head"><span class="tag">Ep ${e.ep} · ${esc(e.date)}</span>${memberById[e.pov.toLowerCase()] ? avatar(e.pov.toLowerCase(), 28, e.pov) : ""}</div><h3 style="margin:.5rem 0 .3rem">${esc(e.title)}</h3><p class="small ink2" style="margin:0">${esc(e.what)}</p>${e.milestone && e.milestone !== "-" ? `<p class="tiny muted" style="margin:.4rem 0 0">Milestone: ${esc(e.milestone)}</p>` : ""}</a>`).join("")}</section>`;
  }

  function askTable(title, lede, rows, col, open) {
    if (!rows.length && title) return `<section><h2>${esc(title)}</h2><p class="empty">None.</p></section>`;
    return `<section>${title ? `<h2>${esc(title)} <span class="muted">${rows.length}</span></h2><p class="small muted" style="margin:.2rem 0 .6rem">${esc(lede)}</p>` : ""}<div class="tbl"><table><thead><tr><th>Asked</th><th>Room</th><th>Question</th><th>${esc(col)}</th>${open ? "<th>By</th>" : "<th>Answer</th>"}</tr></thead><tbody>${rows.map(a => `<tr><td>${esc(a.date)}</td><td>${esc(a.owner)}</td><td class="w">${esc(a.name)}</td><td class="w">${esc(a.default)}</td><td${open ? "" : ' class="w"'}>${esc(open ? a.due : a.answer)}</td></tr>`).join("")}</tbody></table></div></section>`;
  }

  function pagePlan() {
    const st = {}; K.instructions.forEach(i => { st[i.status] = (st[i.status] || 0) + 1; });
    const order = Object.keys(st).sort((a, b) => ({ good: 0, warn: 1, crit: 2, "": 3 }[tone(a)] - { good: 0, warn: 1, crit: 2, "": 3 }[tone(b)]));
    const colour = s => ({ good: "var(--good)", warn: "var(--warn)", crit: "var(--crit)" }[tone(s)] || "var(--axis)");
    app.innerHTML = `<div><div class="crumbs"><a href="#/more">More</a>›<span>Plan</span></div><h1>Projects, questions and your instructions</h1>
      <p class="lede">Keel plans its own projects, makes its own calls (only danger-zone decisions wait for you), and tracks every instruction Caplet has given it.</p></div>
      <section><h2>Keel's projects</h2><div class="grid wide">${K.projects.map(p => `<div class="card"><div class="sec-head"><span class="tag">${esc(p.id)}</span>${pill(p.status)}</div><h3 style="margin:.5rem 0 .4rem">${esc(p.name)}</h3><dl class="now"><dt>For the judges</dt><dd class="small">${esc(p.for_judges)}</dd><dt>Next step</dt><dd class="small">${esc(p.next)}</dd></dl><p class="tiny muted" style="margin:.6rem 0 0">${esc(p.owner)} · due ${esc(p.due)}</p></div>`).join("")}</div></section>
      ${askTable("Danger zone: waiting for you", "Irreversible or outward-facing (WInS orders, submitting, your docs, money, accounts). Keel recommends and does nothing until a student answers.", K.asks.filter(a => a.status.startsWith("Danger")), "Keel recommends", true)}
      ${askTable("Keel's calls", "Ray, 26 Oct: \u201cjust make your own call whichever you think work the best\u201d. Each call with its one-line reason; overrule any of them in chat.", K.asks.filter(a => a.status === "Keel's call"), "Keel's call and why", true)}
      ${askTable("Facts only you have", "Not decisions: Keel writes \u201cstudents to confirm\u201d and never invents them. Needed by the Final Report.", K.asks.filter(a => a.status.startsWith("Fact")), "Meanwhile", true)}
      <section class="history"><details><summary>Answered by a student <span class="muted">${K.asks.filter(a => a.status === "Answered").length}</span></summary>${askTable("", "", K.asks.filter(a => a.status === "Answered"), "Keel's default", false)}</details></section>
      <section><div class="sec-head"><h2>Your instructions (${K.instructions.length})</h2>${docLink("keel/INSTRUCTIONS.md", "the register")}</div>
        <div class="stack" role="img" aria-label="Instructions by status">${order.map(s => `<span title="${esc(s)}: ${st[s]}" style="flex:${st[s]};background:${colour(s)}"></span>`).join("")}</div>
        <div class="legend">${order.map(s => `<span><span class="key" style="background:${colour(s)}"></span>${esc(s)} ${st[s]}</span>`).join("")}</div>
        <input type="search" id="q" placeholder="Search your instructions" aria-label="Search instructions">
        <div class="tbl"><table><thead><tr><th>#</th><th>Date</th><th>Instruction</th><th>Status</th><th>What we found</th><th>Enforced in</th></tr></thead><tbody id="ib"></tbody></table></div></section>`;
    const ib = app.querySelector("#ib"), q = app.querySelector("#q");
    const fill = () => { const t = q.value.toLowerCase(); ib.innerHTML = K.instructions.filter(i => !t || JSON.stringify(i).toLowerCase().includes(t)).map(i => `<tr><td>${esc(i.id.replace("instr-", ""))}</td><td>${esc(i.date)}</td><td class="w">${esc(i.name)}</td><td>${pill(i.status)}</td><td class="w small">${esc(i.evidence)}</td><td class="small">${esc(i.file)}</td></tr>`).join(""); };
    q.addEventListener("input", fill); fill();
  }

  function pageLibrary() {
    const groups = {};
    K.docs.forEach(d => { const g = d.path.split("/").slice(1, -1).join("/") || "keel"; (groups[g] = groups[g] || []).push(d); });
    app.innerHTML = `<div><div class="crumbs"><a href="#/more">More</a>›<span>Library</span></div><h1>Every page Keel has written</h1>
      <p class="lede">${K.docs.length} pages, rendered from the repo. Links inside a page open here.</p></div>
      <input type="search" id="q" placeholder="Search titles and paths" aria-label="Search pages"><section id="lib"></section>`;
    const lib = app.querySelector("#lib"), q = app.querySelector("#q");
    const fill = () => {
      const t = q.value.toLowerCase();
      lib.innerHTML = Object.keys(groups).sort().map(g => {
        const ds = groups[g].filter(d => !t || (d.title + " " + d.path).toLowerCase().includes(t));
        return ds.length ? `<details class="fold card" ${t || ds.length < 12 ? "open" : ""}><summary>${esc(g)} <span class="muted small">(${ds.length})</span></summary><ul class="folder">${ds.map(d => `<li><a href="#/doc/${esc(d.path)}"><span>${esc(d.title)}</span><span class="tiny muted">${esc(d.path.split("/").pop())} · ${d.kb} KB</span></a></li>`).join("")}</ul></details>` : "";
      }).join("") || `<p class="empty">Nothing matches.</p>`;
    };
    q.addEventListener("input", fill); fill();
  }

  function loadDoc(path, target) {
    fetch("d/" + path.split("/").map(encodeURIComponent).join("/") + ".html").then(r => { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then(h => { target.innerHTML = h; target.querySelectorAll("table").forEach(t => { const w = document.createElement("div"); w.className = "tblwrap"; t.replaceWith(w); w.appendChild(t); }); })
      .catch(() => { target.innerHTML = `<p class="empty">This page isn't in the portal yet. <a href="${gh(path)}" target="_blank" rel="noopener">Open it on GitHub</a>.</p>`; });
  }
  function pageDoc(path) {
    const d = K.docs.find(x => x.path === path);
    const parts = path.split("/");
    app.innerHTML = `<div><div class="crumbs"><a href="#/more">More</a>›<a href="#/library">Library</a>›${parts.slice(1, -1).map(p => `<span>${esc(p)}</span>›`).join("")}<span>${esc(parts[parts.length - 1])}</span></div>
      <p class="small" style="margin:.4rem 0 0"><a href="${gh(path)}" target="_blank" rel="noopener">Open on GitHub</a>${d ? ` · ${d.kb} KB` : ""}</p></div>
      ${/episodes\/|members\/|CAST|STORY|ARCS|WORLD|tea_room/.test(path) ? `<p class="notice fiction">Fiction: Keel is a simulated team, AI-written. Events and people are made up; research findings are real and dated.</p>` : ""}
      <article class="card"><div class="doc" id="doc"><p class="muted">Loading…</p></div></article>`;
    loadDoc(path, app.querySelector("#doc"));
  }
  function notFound() { app.innerHTML = `<h1>Not found</h1><p><a href="#/">Back to the office</a></p>`; }

  // ---------- Today: the front page ----------
  const DAYS = K.days || [];
  const longDay = d => new Intl.DateTimeFormat("en-AU", { weekday: "long", day: "numeric", month: "long", timeZone: "UTC" }).format(new Date(d + "T00:00:00Z"));
  const shortDay = d => new Intl.DateTimeFormat("en-AU", { weekday: "short", day: "numeric", month: "short", timeZone: "UTC" }).format(new Date(d + "T00:00:00Z"));
  const cleanTitle = t => { const x = String(t || "").replace(/^FICTION[^.]*\.\s*/, "").replace(/^[^:]{0,70}\b20\d\d\b[^:]{0,40}: /, ""); return x.charAt(0).toUpperCase() + x.slice(1); };
  const roomName = id => id && roomById[id] ? roomById[id].name : "";
  const nameId = n => (K.members.find(m => m.name === n) || {}).id;
  function nextDeadline() {
    const d = K.meta.deadlines.find(x => new Date(x.at) > Date.now());
    if (!d) return "";
    const days = Math.ceil((new Date(d.at) - Date.now()) / 864e5);
    return `${esc(d.name)} in ${plural(days, "day")} (${esc(syd(d.at, { weekday: "short", day: "numeric", month: "short" }))}, ${esc(syd(d.at, { hour: "2-digit", minute: "2-digit", hour12: false }))} Sydney)`;
  }
  function talkCard(t, open) {
    const head = t.kind === "Memo" ? esc(roomName(t.room) || "Memo") : t.kind === "Huddle" ? `Huddle · ${plural(new Set(t.lines.map(l => l.name)).size, "voice")} · ${plural(t.lines.length, "post")}` : esc(t.kind);
    const shown = t.lines.slice(0, 4), rest = t.lines.slice(4);
    const msg = l => { const id = nameId(l.name); return `<div class="msg">${id ? `<a href="#/member/${id}" class="msg-ava">${avatar(id, 30, l.name)}</a>` : ""}<div><b>${esc(l.name)}</b><p>${esc(l.text)}</p></div></div>`; };
    return `<details class="talk"${open ? " open" : ""}><summary><span class="kicker">${head}</span><span class="t">${esc(cleanTitle(t.title))}</span>${t.kind === "Huddle" && t.essence ? `<span class="ess">${esc(t.essence)}</span>` : ""}<span class="who-row">${[...new Set(t.lines.map(l => l.name))].map(n => nameId(n) ? avatar(nameId(n), 18, n) : "").join("")}</span></summary>
      ${t.decided && t.decided.length ? `<div class="decided"><b>Decided</b><ul>${t.decided.map(x => `<li>${esc(x)}</li>`).join("")}</ul></div>` : ""}
      <div class="chat">${shown.map(msg).join("")}${rest.length ? `<details class="more-lines"><summary>${plural(rest.length, "more line")}</summary>${rest.map(msg).join("")}</details>` : ""}</div>
      ${t.path ? `<p class="go">${docLink(t.path, "Read it all →")}</p>` : ""}</details>`;
  }
  function pageToday(day) {
    if (!DAYS.length) { app.innerHTML = `<div class="today"><h1>Nothing yet</h1></div>`; return; }
    const i = Math.max(0, day ? DAYS.findIndex(d => d.day === day) : 0), D = DAYS[i];
    if (!D) return notFound();
    const prev = DAYS[i + 1], next = DAYS[i - 1];
    const plainItems = D.plain.map(p => `<li><span class="who">${esc(p.who.replace(/^The /, ""))}</span><p>${esc(p.text)}${p.href ? ` <a href="#/doc/${esc(p.href)}" class="nowrap">read →</a>` : ""}</p></li>`).join("");
    const done = [...D.done.map(d => ({ text: d.text, who: d.who })), ...D.calls.map(c => ({ text: "Decided: " + c.text.replace(/^\w{3} \d+ \w{3}: /, ""), who: roomName(c.room) }))];
    app.innerHTML = `<div class="today">
      <div class="day-nav">
        ${prev ? `<a class="arrow" href="#/day/${prev.day}" aria-label="Earlier day: ${esc(shortDay(prev.day))}">‹</a>` : `<span class="arrow off">‹</span>`}
        <div class="day-title"><span class="eyebrow">${i === 0 ? "Today at Keel" : "What Keel did"}</span><h1>${esc(longDay(D.day))}</h1>
          <p class="meta">${plural(D.memos, "memo")} · ${plural(D.talks.length, "conversation")} · ${plural(D.commits, "commit")}${i === 0 && nextDeadline() ? ` · ${nextDeadline()}` : ""}</p></div>
        ${next ? `<a class="arrow" href="#/day/${next.day}" aria-label="Later day: ${esc(shortDay(next.day))}">›</a>` : `<span class="arrow off">›</span>`}
      </div>
      ${D.for_caplet.length ? `<section class="essence"><h2>For Caplet</h2><ol>${D.for_caplet.map(p => `<li>${p.who ? `<b>${esc(p.who)}</b> ` : ""}${esc(p.text)}</li>`).join("")}</ol></section>` : ""}
      <section class="block"><h2>In plain words</h2><ul class="plainlist">${plainItems || `<li class="muted">Nothing written yet today.</li>`}</ul>
        ${D.plain_auto && D.plain.length ? `<p class="note">No one wrote a plain summary this day, so these are the rooms' own result lines.</p>` : ""}${D.today_doc ? `<p class="note">${docLink(D.today_doc, "The day's page")}</p>` : ""}</section>
      ${D.round && D.round.path ? `<section class="block"><h2>The research round</h2>${D.round.question ? `<p class="q">${esc(D.round.question)}</p>` : ""}<p class="note">${D.round.lens ? `Lens: ${esc(D.round.lens)} · ` : ""}${D.round.beats.length} of 9 beats in · ${docLink(D.round.path, "Read the round →")} · ${docLink("keel/loop/CHAMPIONS.md", "champion board")}</p></section>` : ""}
      ${D.talks.length ? `<section class="block"><h2>Conversations <span class="count">${D.talks.length}</span></h2><div class="talks">${D.talks.map((t, k) => talkCard(t, k < 2 && t.kind !== "Huddle")).join("")}</div></section>` : ""}
      ${D.research.length || D.files.length ? `<section class="block"><h2>Research <span class="count">${D.research.length}</span></h2><ul class="rlist">${D.research.map(r => `<li><div class="r-head"><span class="kicker">${esc(roomName(r.room).replace(/^The /, "") || "Huddle")}</span><a href="#/doc/${esc(r.path)}">${esc(cleanTitle(r.title))}</a></div>${r.text ? `<p>${esc(r.text)}</p>` : ""}${r.sources && r.sources.length ? `<details><summary>${plural(r.sources.length, "source")} read</summary><ul>${r.sources.map(x => `<li>${esc(x)}</li>`).join("")}</ul></details>` : ""}</li>`).join("")}</ul>
        ${D.files.length ? `<details class="files"><summary>${plural(D.files.length, "new research page")}</summary><ul>${D.files.map(f => `<li>${docLink(f.path, f.title)}</li>`).join("")}</ul></details>` : ""}</section>` : ""}
      ${done.length || D.open.length ? `<section class="block"><h2>Done <span class="count">${done.length}</span></h2><ul class="done">${done.map(d => `<li><span class="tick" aria-hidden="true">✓</span><span>${esc(d.text)}${d.who ? ` <span class="muted small">${esc(d.who)}</span>` : ""}</span></li>`).join("")}${D.open.map(d => `<li class="todo"><span class="tick" aria-hidden="true">○</span><span>${esc(d.text)} <span class="muted small">${esc(d.who)}</span></span></li>`).join("")}</ul></section>` : ""}
      ${D.ips.length ? `<section class="block"><h2>The IPS rewrite's thinking</h2><ul class="rlist">${D.ips.map(t => `<li><div class="r-head"><a href="#/doc/keel/ips_rewrite/THINKING_LOG.md">${esc(cleanTitle(t.title))}</a></div><p>${esc(t.text)}</p></li>`).join("")}</ul><p class="note">The rewrite is slow on purpose (the bible, rule 2). ${docLink("keel/ips_rewrite/THINKING_LOG.md", "Whole thinking log →")} · <a href="#/ips">Every IPS version →</a></p></section>` : ""}
      <p class="note center"><a href="#/days">All days</a> · <a href="#/more">Everything else</a></p>
    </div>`;
  }
  function pageDays() {
    app.innerHTML = `<div class="today"><div class="day-title"><span class="eyebrow">The log</span><h1>Every day so far</h1></div>
      <ul class="daylist">${DAYS.map(D => { const f = D.for_caplet[0] || D.plain[0] || {}; const lead = f.text ? (f.who ? f.who.replace(/^The /, "") + (/[.!?]$/.test(f.who) ? " " : ": ") : "") + f.text : ""; return `<li><a href="#/day/${D.day}"><span class="d">${esc(shortDay(D.day))}</span><span class="l">${esc(lead.length > 170 ? lead.slice(0, 170).replace(/\s\S*$/, "") + "…" : lead)}</span><span class="c">${plural(D.talks.length, "conversation")} · ${D.research.length} research · ${D.done.length + D.calls.length} done</span></a></li>`; }).join("")}</ul></div>`;
  }
  // The five criteria in short (Wharton's full words: the bible, Book 8)
  const CRITERIA = [
    ["Investment Strategy", "A clear, creative thesis; disciplined planning across Laura's changing horizons and cash flows; sensible diversification; everything consistent with the IPS."],
    ["Client Knowledge and Objectives", "Tailored to Laura's circumstances, priorities, risk and residency goals; recommendations that can earn her confidence."],
    ["Portfolio Analysis", "Investing concepts and tools used well; numbers and judgement together; reasonable projections of funding reliability, the facility gift and her flexibility in good and bad markets."],
    ["Articulation of Competition Experience", "Teamwork, communication and learning; how we researched and decided; how we grew and handled setbacks."],
    ["Creativity and Presentation", "A compelling story in our own voice; data that backs the conclusions; original thinking and real reflection; the gift and its uncertainty told credibly to co-sponsors."]];
  function judgedCard() {
    return `<section class="card judged"><div class="sec-head"><h2>How the judges score us</h2><a href="#/doc/keel/BIBLE.md">Wharton's words (Book 8) →</a></div>
      <ol class="crit">${CRITERIA.map(([t, d]) => `<li><b>${esc(t)}</b><span>${esc(d)}</span></li>`).join("")}</ol>
      <p class="small muted" style="margin:.5rem 0 0">Five criteria across the Trading Notes, the IPS and the Final Report, judged together. WInS gains and losses are not scored. The bible, Book 8; part by part in ${docLink("keel/library/ips_road_2026-10/03_CRITERION_MAP.md", "the criterion map")}.</p></section>`;
  }
  function pageMore() {
    const L = [["#/office", "Office dashboard", "Rooms on time, charts, deadlines and the latest commits"], ["#/ideas", "The idea bank", "Every good idea and the deliverable it lands in"], ["#/ips", "The IPS", "Every version and what changed"], ["#/doc/keel/BIBLE.md", "The bible", "Nine books, read first by every run"],
      ["#/plan", "Questions for you", "The danger-zone question, Keel's own calls with reasons, and your instructions"], ["#/rooms", "Rooms", "Twelve rooms, each with its decisions and work"], ["#/team", "The six", "Profiles and every take"],
      ["#/activity", "Activity", "Every commit and the run log"], ["#/episodes", "Episodes", "The story so far (fiction)"], ["#/library", "Library", "Every page Keel has written"]];
    app.innerHTML = `<div class="today"><div class="day-title"><span class="eyebrow">One click deeper</span><h1>Everything else</h1></div>
      <ul class="morelist">${L.map(([h, t, d]) => `<li><a href="${h}"><b>${esc(t)}</b><span>${esc(d)}</span></a></li>`).join("")}</ul>${judgedCard()}</div>`;
  }

  // ---------- the idea bank (BIBLE Book 9: every good idea lands in a deliverable) ----------
  function landsKey(l) { return /^both/i.test(l) ? "both" : /^ips/i.test(l) ? "ips" : "fr"; }
  function pageIdeas(filter) {
    const B = K.idea_bank || { ideas: [], dropped: [] }, f = ["ips", "fr", "both"].includes(filter) ? filter : "all";
    const n = k => B.ideas.filter(i => landsKey(i.lands) === k).length;
    const shown = B.ideas.filter(i => f === "all" || landsKey(i.lands) === f);
    const chip = (k, label, c) => `<a class="chip" href="#/ideas${k === "all" ? "" : "/" + k}" aria-pressed="${f === k}">${esc(label)} · ${c}</a>`;
    const groups = [...new Set(shown.map(i => i.area))];
    app.innerHTML = `<div class="today"><div class="day-title"><span class="eyebrow">The idea bank</span><h1>Every good idea, and where it lands</h1></div>
      <p class="lede">Ahaan, 27 Oct: "Every single good idea you have ... must end up in either the IPS or the Final Report or both." Each one is banked the day it's found, with its honest weakness. ${docLink("keel/ips_rewrite/IDEA_BANK.md", "The bank →")}</p>
      <div class="filters" style="margin:.8rem 0 1rem">${chip("all", "All", B.ideas.length)}${chip("ips", "IPS", n("ips"))}${chip("both", "Both", n("both"))}${chip("fr", "Final Report", n("fr"))}</div>
      ${groups.map(g => `<section class="block"><h2>${esc(g)}</h2><ul class="ideas">${shown.filter(i => i.area === g).map(i => `<li><details><summary><span class="i-head"><b>${esc(i.title)}</b></span><span class="i-meta"><span class="pill">${{ ips: "IPS", fr: "Final Report", both: "Both" }[landsKey(i.lands)]}</span></span></summary>
        ${i.more ? `<p>${esc(i.more)}</p>` : ""}${/[(:]/.test(i.lands) ? `<p class="small"><b>Where:</b> ${esc(i.lands)}</p>` : ""}${i.notes.map((t, k) => `<p class="small${k ? " muted" : ""}">${esc(t)}</p>`).join("")}</details></li>`).join("")}</ul></section>`).join("")}
      ${B.dropped.length ? `<details class="dropped"><summary>Dropped, with the reason · ${B.dropped.length}</summary><ul class="rlist">${B.dropped.map(d => `<li><b>${esc(d.idea)}</b><p class="small muted">${esc(d.why)}</p></li>`).join("")}</ul></details>` : ""}</div>`;
  }

  // ---------- router ----------
  const TABS = [["#/", "Today"], ["#/days", "Days"], ["#/ideas", "Ideas"], ["#/ips", "IPS"], ["#/more", "More"]];
  function route() {
    hideTip();
    const h = location.hash || "#/", seg = h.replace(/^#\/?/, "").split("/");
    const tab = seg[0] === "" ? "#/" : seg[0] === "day" ? "#/days" : ["ips", "compare"].includes(seg[0]) ? "#/ips" : seg[0] === "days" ? "#/days" : seg[0] === "ideas" ? "#/ideas" : "#/more";
    document.getElementById("tabs").innerHTML = TABS.map(([href, label]) => `<a href="${href}" ${href === tab || (href === "#/" && tab === "#/") ? 'aria-current="page"' : ""}>${label}</a>`).join("");
    const pages = {
      "": () => pageToday(), day: () => pageToday(seg[1]), days: pageDays, ideas: () => pageIdeas(seg[1]), more: pageMore, office: pageHome, ips: () => seg[1] ? pageVersion(seg[1]) : pageIps(), compare: () => pageCompare(seg[1], seg[2]),
      rooms: pageRooms, room: () => pageRoom(seg[1]), team: pageTeam, member: () => pageMember(seg[1]),
      activity: () => pageActivity(seg[1]), episodes: pageEpisodes, plan: pagePlan, library: pageLibrary,
      doc: () => pageDoc(decodeURIComponent(seg.slice(1).join("/"))),
    };
    slots = [];
    (pages[seg[0]] || notFound)();
    mount();
    if (!h.startsWith("#/doc/") || !app.dataset.keepScroll) window.scrollTo(0, 0);
  }
  window.addEventListener("hashchange", route);
  let lastW = innerWidth, rt;
  window.addEventListener("resize", () => { if (innerWidth === lastW) return; lastW = innerWidth; clearTimeout(rt); rt = setTimeout(mount, 120); });
  const themeBtn = document.getElementById("theme");
  try { const t = localStorage.getItem("keel-theme"); if (t) document.documentElement.dataset.theme = t; } catch (e) { /* storage blocked */ }
  themeBtn.addEventListener("click", () => {
    const dark = document.documentElement.dataset.theme ? document.documentElement.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    document.documentElement.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("keel-theme", document.documentElement.dataset.theme); } catch (e) { /* storage blocked */ }
  });
  document.getElementById("foot").innerHTML = `Built ${esc(K.meta.built)} from <a href="${K.meta.repo}" target="_blank" rel="noopener">the repo</a> (${esc(K.meta.head)}${K.meta.branches.length ? ", with " + K.meta.branches.map(esc).join(", ") : ""}). Rebuilds within minutes of every Keel push. Keel is a simulated team, AI-written; Team Caplet decides and submits.`;
  route();
})();
