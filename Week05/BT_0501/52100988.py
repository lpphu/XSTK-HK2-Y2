# 52100988 Lữ Phúc Phú

import random
import matplotlib.pyplot as plt
import numpy as np

''' 1. '''
X = [0, 2, 1]

''' 2. '''
def random_cube(n):
    tempList = []
    temp_0 = 0
    temp_1 = 0
    temp_2 = 0
    for i in range(n):
        temp1 = random.randint(0,1)
        temp2 = random.randint(0,1)
        if temp1 == temp2:
            if temp1 == 0:
                temp_0 += 1
            else:
                temp_1 += 1
        else:
            temp_2 += 1
    tempList.append(temp_0/n)
    tempList.append(temp_2/n)
    tempList.append(temp_1/n)
    return tempList

''' 3. '''
s = 0
for i,j in zip(X,list(random_cube(10))):
    s += i*j
print("3.",s)

''' 4. '''
print("4.")
x = list(X)
y = random_cube(10)

plt.bar(x,y,width=0.5)

plt.show()
