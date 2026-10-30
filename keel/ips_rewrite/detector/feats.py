import json, lzma, hashlib, os, sys
from gpt2score import features, normalise
PRE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../zippy/zippy/ai-generated.txt')).read()
_c = lambda b: len(lzma.compress(b, preset=2))
PRE_B = normalise(PRE).encode(); PRE_C = _c(PRE_B)
def zip_score(text):
    # ZipPy idea (Thinkst 2023): how well the sample compresses after a prelude of AI text; reimplemented here
    t = normalise(text).encode()
    return (_c(PRE_B + t) - PRE_C) / len(t)
CACHE = 'featcache.json'
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def feat(text):
    k = hashlib.md5(text.encode()).hexdigest()
    if k not in cache:
        f = features(text); f['zip'] = zip_score(text); cache[k] = f
        json.dump(cache, open(CACHE, 'w'))
    return cache[k]
if __name__ == '__main__':
    c = json.load(open('corpus.json'))
    for part in ('train', 'held'):
        for i, (s, y, t) in enumerate(c[part]): feat(t)
    print('done', len(cache))
