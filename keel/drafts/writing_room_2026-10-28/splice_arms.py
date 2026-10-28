# Applies the Writing Room's 28 Oct splices to V28 and counts words (run from this folder after setting base path).
exec(open(__file__.replace('splice_arms.py','splice_base.py')).read().split("arms = {")[0])
OLD9 = "The fourth is our soft spot, the one thing that can still trim the gift. So in January 2033 the reserve changes once: any projected shortfall, plus a cushion, moves into the next fund to mature, from leftover cash and Laura's half first."
C6MC = [(OLD9, "The fourth is our soft spot, so it is priced in 2031: any gap the bond market has already shown her, plus a cushion, falls on spare cash and her half before the bottom. In January 2033 that money moves into the next fund to mature.")]
A = [("That deposit then buys the floor", "That deposit buys a Treasury holding for the coupons, then the floor"),
     (OLD9, "The fourth is our soft spot, so it is paid for in 2028: that holding, hers after the tenth cheque. In January 2033 money for any gap already showing goes into the next fund to mature, from leftover cash and her half.")]
arms = {'C6':FIX+CUT,'C6+MC':FIX+CUT+C6MC,'A':FIX+CUT+A}
if __name__ == '__main__':
    for k,e in arms.items():
        t=apply(base,e); open(f'{k}.txt','w').write(t); print(k, words_limit(t), words_strict(t))
