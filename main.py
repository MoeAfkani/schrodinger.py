from decimal import *
from decimal import Decimal as D
getcontext().prec = 1000
psi=[D(0),D(1e-40)]
v=D(2.0)
E=D(5.0)
m=D(1e-15)
h=D(1e-34)
epsl=D(1e-20)
def Next_psi():
    return ( 2*m/h**2 * epsl**2 * (v-E) - D(2) ) * psi[-1] - psi[-2]
for i in range (0,100):
    print(Next_psi())
    psi.append(Next_psi())


import matplotlib.pyplot as plt
plt.plot(psi,len(psi))
print(psi)
