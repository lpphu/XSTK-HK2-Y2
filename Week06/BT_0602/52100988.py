# 52100988 Lữ Phúc Phú

import math

from matplotlib import pyplot as plt

''' Exercise 01 '''
print("1.")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1)*n
def posion(u,n):
    return (pow(u,n)*pow(math.e,-u))/factorial(n)
print(posion(3,2))

''' Exercise 02 '''
print("2.")
X = [1,2,3,4,5]
Y = [posion(i) for i in X]
plt.bar(X,Y,width=0.1)
plt.show()