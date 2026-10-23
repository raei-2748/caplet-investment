// RAB Lab compute core (pure functions; inlined into index.html by build_page.py and run under node by
// check_core.js). Mirrors ws2_common.rule, m4_cap.measures and m4_gap_owner.outcome mechanism C.
// AI-generated research (Claude Code) for Team Caplet, WS8, 30 Sep 2026.
var LabCore = (function () {
  function b64bytes(s) {
    if (typeof atob === "function") {
      var bin = atob(s), n = bin.length, u = new Uint8Array(n);
      for (var i = 0; i < n; i++) u[i] = bin.charCodeAt(i);
      return u;
    }
    return new Uint8Array(Buffer.from(s, "base64"));
  }
  function readInt16(s) {
    var b = b64bytes(s), dv = new DataView(b.buffer, b.byteOffset, b.byteLength), n = b.byteLength / 2;
    var out = new Float64Array(n);
    for (var i = 0; i < n; i++) out[i] = dv.getInt16(2 * i, true);
    return out;
  }
  function readUint16(s) {
    var b = b64bytes(s), dv = new DataView(b.buffer, b.byteOffset, b.byteLength), n = b.byteLength / 2;
    var out = new Float64Array(n);
    for (var i = 0; i < n; i++) out[i] = dv.getUint16(2 * i, true);
    return out;
  }
  // Decode once: z (paths x 5, standardised annual log returns) per model, phi per path.
  function prepare(data) {
    var m = data.meta, models = {};
    Object.keys(data.models).forEach(function (k) {
      var q = readInt16(data.models[k].z);
      for (var i = 0; i < q.length; i++) q[i] = q[i] / m.z_scale;
      models[k] = { z: q, mean: data.models[k].mean, sd: data.models[k].sd };
    });
    var phi = readUint16(data.phi);
    for (var i = 0; i < phi.length; i++) phi[i] = phi[i] / m.phi_scale + m.phi_off;
    return { meta: m, models: models, phi: phi, n: phi.length };
  }
  function pct(sorted, p) {             // numpy's default (linear) percentile
    var n = sorted.length, pos = (n - 1) * p / 100, lo = Math.floor(pos), hi = Math.min(lo + 1, n - 1);
    return sorted[lo] + (sorted[hi] - sorted[lo]) * (pos - lo);
  }
  // opts: model, s (share promised), mu (annual log mean) and vol (annual log sd), g31 and rate (coupon gap)
  function compute(P, opts) {
    var M = P.models[opts.model], z = M.z, phi = P.phi, n = P.n, meta = P.meta;
    var B0 = meta.B0, F = meta.F, A = meta.A, s = opts.s, mu = opts.mu, vol = opts.vol;
    var g31 = opts.g31 || 0, r = opts.rate || 0, grow = (1 + r) * (1 + r);
    var U = new Float64Array(n), G = new Float64Array(n), K = new Float64Array(n);
    var below = 0, top = 0, keep = 0, down = 0, lowered = 0, gsum = 0;
    for (var i = 0; i < n; i++) {
      var o = 5 * i;
      var a3 = 0, a5 = 0;
      for (var t = 0; t < 3; t++) a3 += mu + vol * z[o + t];
      for (t = 3; t < 5; t++) a5 += mu + vol * z[o + t];
      var B3 = B0 * Math.exp(a3), B5 = B3 * Math.exp(a5), ph = phi[i], u, g, k;
      if (g31 === 0) {
        u = F + s * B3;
        g = Math.min(ph * F + s * Math.min(B5, B3), u);
        k = ph * F + B5 - g;
      } else {                           // WS3 rule 3: Laura's half first, then the gift above the floor, then the floor
        var ex = Math.max(0, g31 - (1 - s) * B3), B3n = B3 - ex, short = B3n < 0;
        var f = short ? 0 : B3n / (B3 > 0 ? B3 : 1), B3p = Math.max(B3n, 0), B5p = B5 * f;
        u = F + s * B3 - ex;
        g = Math.min(ph * F + s * Math.min(B5p, B3p), u);
        k = ph * F + B5p - g - (g31 - ex) * grow;
        var cut = Math.max(0, -k);
        g -= cut; k += cut;
        if (short) { var take = -B3n * grow; g = ph * F - take; u = F - take; k = 0; }
        if (ex > 0) lowered++;
      }
      U[i] = u; G[i] = g; K[i] = k; gsum += g;
      if (g < A) below++;
      if (B5 >= B3) top++;
      if (k >= meta.kappa * g) keep++;
      if (B3 < B0) down++;
    }
    var Us = Float64Array.from(U).sort(), Gs = Float64Array.from(G).sort(), Ks = Float64Array.from(K).sort();
    return {
      top_p5: pct(Us, 5), top_p50: pct(Us, 50), top_p95: pct(Us, 95),
      gift_p5: pct(Gs, 5), gift_p50: pct(Gs, 50), gift_p95: pct(Gs, 95), gift_mean: gsum / n,
      p_below_low: below / n, p_top: top / n, p_keep10: keep / n, kept_p5: pct(Ks, 5),
      p_fund_down: down / n, p_lowered: lowered / n, giftSorted: Gs, n: n
    };
  }
  return { prepare: prepare, compute: compute, pct: pct };
})();
if (typeof module !== "undefined") module.exports = LabCore;
