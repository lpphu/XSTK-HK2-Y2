# 52100988 Lữ Phúc Phú

import random
import matplotlib.pyplot as plt
import numpy as np

X = {1,2,3,4,5,6}
def random_cube(n):
    tempList = []
    for i in range(n):
        tempList.append(random.randint(1,6))
    ans = []
    for i in range(1,6+1):
        ans.append(tempList.count(i))
    return ans

x = list(X)
y = random_cube(1000)

plt.bar(x,y,width=0.5)

plt.show()
