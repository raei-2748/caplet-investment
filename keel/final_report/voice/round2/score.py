import re,json,collections
P=json.load(open('passages.json'))
V={'surely':3,'probably':2,'probably not':1,'surely not':0}
res=collections.defaultdict(list); ranks=collections.defaultdict(list); yes=collections.defaultdict(int)
for r in (1,2,3):
    order=open(f'order_reader{r}.txt').read().strip().split(',')
    t=open(f'reading_{r}.md').read()
    blocks=re.split(r'^### Passage (\d+)\s*$',t,flags=re.M)
    got={}
    for i in range(1,len(blocks),2):
        n=int(blocks[i]); b=blocks[i+1]
        m=re.search(r'\*\*Verdict:?\*\*:?\s*\**\s*(Surely not|Probably not|Surely|Probably)',b,re.I)
        got[n]=m.group(1).lower() if m else None
    for n,k in enumerate(order,1):
        v=got.get(n); res[k].append(v)
        if v in ('surely','probably'): yes[k]+=1
    # ranking: find lines after "rank" heading with "Passage n" in order
    tail=t[t.rfind('### Passage 21'):]
    mm=re.search(r'(?is)rank(?:ing)?[^\n]*\n(.*)',tail)
    seq=[int(x) for x in re.findall(r'Passage (\d+)',mm.group(1))] if mm else []
    seen=[];
    for x in seq:
        if x not in seen: seen.append(x)
    for pos,x in enumerate(seen[:21],1):
        ranks[order[x-1]].append(pos)
    print('reader',r,'parsed verdicts',sum(1 for v in got.values() if v),'rank list len',len(seen))
grp=collections.defaultdict(lambda:[0,0])
for k in sorted(P):
    g=k[0]; grp[g][0]+=yes[k]; grp[g][1]+=3
    print(k, res[k], 'yes',yes[k], 'ranks',ranks[k], 'mean %.1f'%(sum(ranks[k])/len(ranks[k]) if ranks[k] else 0))
for g,(a,b) in sorted(grp.items()):
    rk=[x for k in P if k[0]==g for x in ranks[k]]
    print(g, f'{a}/{b}', 'mean rank %.1f'%(sum(rk)/len(rk) if rk else 0))
