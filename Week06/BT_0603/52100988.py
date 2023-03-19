#  52100999 Lữ Phúc Phú

import math

from matplotlib import pyplot as plt

''' Exercise 01 '''
print('1.')
def binomial(n,x,p):
    return p*(1-p)**(x-1)
print(binomial(10,3,0.4))

''' Exercise 02 '''
print('2.')
X = [1,2,3,4,5,6,7,8,9,10]
Y = [binomial(10,i,0.4) for i in X]
plt.bar(X,Y,width=0.4)
plt.show()