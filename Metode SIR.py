import numpy as np
import matplotlib. pyplot as plt

t0 = 0
tn = 300
ndata = 1000

t = np. linspace(t0, tn, ndata) 
h = t[2]-t[1]


N = 1000 #rakyat
I0 = 1
R0 = 0
S0 = N - I0 - R0

I = np.zeros(ndata) 
S = np.zeros(ndata) 
R = np.zeros(ndata) 

I[0] = I0
R[0] = R0
S[0] = S0

beta = 0.2
gamma = 0.1

for v in range (0,ndata-1):
    S[v+1] = S[v] - h*beta/N*S[v]*I[v]
    I[v+1] = I[v] + h*beta/N*S[v]*I[v]-h*gamma*I[v]
    R[v+1] = R[v] + h*gamma*I[v]

plt.plot(t,S,label = 'S') 
plt.plot(t,I,label = 'I') 
plt.plot(t,R,label = 'R') 

plt.legend() 
plt.show()
