from decimal import *
from decimal import Decimal as D
getcontext().prec = 1000
class diff:
    def _init_(self):
        pass
    def d(self,x):
        epsilon = D(1e-20)
        return round((self(x+epsilon)-self(x-epsilon))/(2*epsilon),10)
    def dd(self,x):
        epsilon = D(1e-20)
        return round((self(x+epsilon)-2*self(x)+self(x-epsilon))/(epsilon**2),10)
def f(y):
    return D(y**8)
print(diff.d(f,10))
print(diff.dd(f,1))
