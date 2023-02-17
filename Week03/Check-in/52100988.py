# 52100988 Lữ Phúc Phú
' ' ' BT_0202 ' ' '
from itertools import product

import numpy as np
import random


' ' ' Exercise01 ' ' '
card = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K'}
suit = {'♠' , '♣', '♦', '♥'}
deck = list(product(card,suit))
ans = []
for i in np.asarray(deck):
    str = ''
    ans.append(str.join(i))
deck = ans

' ' ' Exercise02 ' ' '
print(deck)

' ' ' Exercise03 ' ' '
def def_function_03(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=3)
        c = 0
        for j in temp:
            if j[0] == 'K':
                c += 1
        if c >= 1:
            count +=1
    return count/n
print("3.",def_function_03(100000))