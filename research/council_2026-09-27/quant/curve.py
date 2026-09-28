import numpy as np
# Par CMT yields (%, bond-equivalent) from WebSearch snippets, as of 2026-09-23/25:
# 2y 4.81 (9/25), 5y 4.99 (9/23), 7y 5.05 (9/23), 10y 5.17 (9/25), 20y 5.45 (9/23), 30y 5.49 (9/25)
T=np.array([2,5,7,10,20,30.]); Y=np.array([4.81,4.99,5.05,5.17,5.45,5.49])/100
grid=np.arange(0.5,30.01,0.5); par=np.interp(grid,T,Y)  # ASSUMPTION: flat below 2y
D=[]
for i,t in enumerate(grid):
    c=par[i]/2; D.append((1-c*sum(D))/(1+c))
D=np.array(D); Z=2*(D**(-1/(2*grid))-1)  # semiannual zero rates
def zero(t):
    t=np.maximum(np.asarray(t,float),0.5); return np.interp(t,grid,Z)
def df(t,shift=0.0):
    t=np.asarray(t,float); return np.where(t<=0,1.0,(1+(zero(t)+shift)/2)**(-2*t))
