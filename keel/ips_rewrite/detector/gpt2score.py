"""GPT-2 (small, ONNX Model Zoo) scoring: log-probs, Fast-DetectGPT analytic criterion, sentence burstiness."""
import json, regex as re, numpy as np, onnxruntime as ort, os, lzma
D = os.path.dirname(os.path.abspath(__file__))
enc = json.load(open(f'{D}/gpt2tok/encoder.json'))
merges = [tuple(l.split()) for l in open(f'{D}/gpt2tok/vocab.bpe', encoding='utf-8').read().split('\n')[1:-1]]
ranks = {m: i for i, m in enumerate(merges)}
def bytes_to_unicode():
    bs = list(range(ord("!"), ord("~")+1))+list(range(ord("¡"), ord("¬")+1))+list(range(ord("®"), ord("ÿ")+1))
    cs = bs[:]; n = 0
    for b in range(256):
        if b not in bs: bs.append(b); cs.append(256+n); n += 1
    return dict(zip(bs, map(chr, cs)))
B2U = bytes_to_unicode()
PAT = re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")
cache = {}
def bpe(tok):
    if tok in cache: return cache[tok]
    word = tuple(tok)
    while len(word) > 1:
        pairs = {(word[i], word[i+1]) for i in range(len(word)-1)}
        best = min(pairs, key=lambda p: ranks.get(p, 1e18))
        if best not in ranks: break
        a, b = best; out = []; i = 0
        while i < len(word):
            if i < len(word)-1 and word[i] == a and word[i+1] == b: out.append(a+b); i += 2
            else: out.append(word[i]); i += 1
        word = tuple(out)
    cache[tok] = word; return word
def encode(text):
    ids = []
    for t in re.findall(PAT, text):
        t = ''.join(B2U[b] for b in t.encode('utf-8'))
        ids += [enc[w] for w in bpe(t)]
    return ids
def normalise(t):
    return (t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
             .replace('–', '-').replace('—', '-'))
_sess = None
def logits(ids):
    global _sess
    if _sess is None:
        so = ort.SessionOptions(); so.intra_op_num_threads = 4
        _sess = ort.InferenceSession(f'{D}/gpt2-lm-head-10.onnx', so)
    return _sess.run(['output1'], {'input1': np.array([[ids]], dtype=np.int64)})[0][0, 0]
def features(text):
    text = normalise(text.strip())
    ids = [50256] + encode(text)[:1000]
    lg = logits(ids).astype(np.float64)[:-1]
    lg -= lg.max(-1, keepdims=True)
    lp = lg - np.log(np.exp(lg).sum(-1, keepdims=True))
    p = np.exp(lp)
    tgt = np.array(ids[1:])
    ll = lp[np.arange(len(tgt)), tgt]
    mu = (p * lp).sum(-1); var = (p * lp**2).sum(-1) - mu**2
    fdg = (ll.sum() - mu.sum()) / np.sqrt(var.sum())          # Fast-DetectGPT (analytic, same model)
    rank = (lp > ll[:, None]).sum(-1)
    # sentence-level perplexity spread (burstiness, GPTZero's original second signal)
    sents = [s for s in re.split(r'(?<=[.!?])\s+', text) if len(s.split()) >= 4]
    sp = []
    pos = 0
    toks = [encode(' ' + s if i else s) for i, s in enumerate(sents)]
    # approximate: map sentences onto token stream by length
    for t in toks:
        n = len(t); seg = ll[pos:pos+n]; pos += n
        if len(seg) > 2: sp.append(np.exp(-seg.mean()))
    return dict(mean_ll=float(ll.mean()), ppl=float(np.exp(-ll.mean())), fdg=float(fdg / np.sqrt(len(tgt)) * 10),
                fdg_raw=float(fdg), top1=float((rank == 0).mean()), top10=float((rank < 10).mean()),
                burst=float(np.std(sp) / (np.mean(sp) + 1e-9)) if len(sp) > 2 else 0.0, ntok=len(tgt))
if __name__ == '__main__':
    import sys
    print(features(open(sys.argv[1]).read()))
