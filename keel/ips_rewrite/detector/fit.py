import json, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from feats import feat
c = json.load(open('corpus.json'))
F = ['mean_ll','fdg','top1','top10','burst','zip']
def X(t): f = feat(t); return [f[k] for k in F]
tr = c['train']; Xs = np.array([X(t) for _,_,t in tr]); y = np.array([l for _,l,_ in tr]); src = [s.split('_')[0] if s.startswith(('draft','rival')) else s for s,_,_ in tr]
# per-feature group means
import collections
g = collections.defaultdict(list)
for s,(_,l,t) in zip(src,tr): g[s].append(X(t))
for s,v in sorted(g.items()): print(f'{s:22s} n={len(v):2d} ' + ' '.join(f'{k}={m:7.3f}' for k,m in zip(F,np.mean(v,0))))
# leave-one-source-out
groups = sorted(set(src)); correct=0; tot=0
for gname in groups:
    m = np.array([s==gname for s in src])
    clf = make_pipeline(StandardScaler(), LogisticRegression(C=0.5, max_iter=1000)).fit(Xs[~m], y[~m])
    p = clf.predict_proba(Xs[m])[:,1]
    acc = ((p>0.5)==y[m]).mean(); correct += ((p>0.5)==y[m]).sum(); tot += m.sum()
    print(f'held-out {gname:22s} true={"human" if y[m][0] else "AI   "} mean P(human)={p.mean():.2f} acc={acc:.2f}')
print('LOSO accuracy', round(correct/tot,3))
clf = make_pipeline(StandardScaler(), LogisticRegression(C=0.5, max_iter=1000)).fit(Xs, y)
print('coefs', dict(zip(F, np.round(clf[-1].coef_[0],2))))
for s,l,t in c['held'][:0]: pass
H = collections.defaultdict(list)
for s,l,t in c['held']: H[s].append(clf.predict_proba([X(t)])[0,1])
for s,v in H.items(): print('external human', s, 'mean P(human)', round(np.mean(v),2), 'share >0.5', round(np.mean(np.array(v)>0.5),2))
import pickle; pickle.dump(clf, open('clf.pkl','wb'))
