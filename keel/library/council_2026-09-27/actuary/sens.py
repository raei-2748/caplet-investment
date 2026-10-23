import mc, numpy as np
for mu in [0.05,0.08]:
    mc.MU_EQ=mu; print("MU_EQ",mu)
    for s in ["lock","rule","wait"]:
        o=mc.run(s,0.0); print(" ",s,"p_short %.4f p5 %d med %d"%(o['p_short'],o['p5'],o['med']))
mc.MU_EQ=0.065
# no 2028 contribution: patch by monkeypatching run - simple copy
src=open('mc.py').read().replace("if year==2028: A+=150000","if year==2028: A+=0").split("for rho in")[0]
ns={}; exec(src,ns)
print("No 2028 contribution:")
for s in ["lock","rule","wait"]:
    o=ns['run'](s,0.0); print(" ",s,"p_short %.4f p5 %d med %d"%(o['p_short'],o['p5'],o['med']))
