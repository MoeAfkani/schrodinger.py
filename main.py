psi=[0,0.001]
v=2
E=5
m=0.01
h=1e-34
epsl=0.001
def Next_psi():
    return ( 2*m/h**2 * epsl**2 * (v-E) + 2 ) * psi[-1] - psi[-2]
for i in range (0,100):
    #print(Next_psi())
    psi.append(Next_psi())


import matplotlib.pyplot as plt
#plt.plot(psi,len(psi))
print(psi)
