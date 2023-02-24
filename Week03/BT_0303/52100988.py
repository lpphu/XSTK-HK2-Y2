# 52100988 Lữ Phúc Phú
' ' ' BT_0303 ' ' '
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

import numpy as np
import random



card = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K'}
suit = {'♠' , '♣', '♦', '♥'}
deck = list(product(card,suit))
ans = []
for i in np.asarray(deck):
    str = ''
    ans.append(str.join(i))
deck = ans
# print(deck)

' ' ' Exercise01 ' ' '
def def_function_01(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=5)
        c = 0
        for j in temp:
            if j[0] in ['J', 'Q', 'K']:
                c += 1
        if c == 5:
            count +=1
    return count/n
x = []
y = []
for i in range(1,1000):
    x.append(i)
    y.append(def_function_01(i))

x_points = np.array(x)
y_points = np.array(y)
plt.plot(x_points, y_points, linestyle='-')
plt.show()