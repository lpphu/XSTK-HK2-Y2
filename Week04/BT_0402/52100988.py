# 52100988 Lữ Phúc Phú
' ' ' BT_0402 ' ' '

from itertools import product

import numpy as np
import random


card = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K'}
suit = {'♠' , '♣', '♦', '♥'}
red = {'♦', '♥'}
black = {'♠' , '♣'}
deck = list(product(card,suit))
ans = []
for i in np.asarray(deck):
    str = ''
    ans.append(str.join(i))
deck = ans

' ' ' Exercise a Bốn lá cùng chất ' ' '
def function_01(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=4)
        if temp[0][1] == temp[1][1] == temp[2][1] == temp[3][1]:
            count += 1
    return count/n

' ' ' Exercise b Bốn lá đôi một khác chất ' ' '
def function_02(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=4)
        tempSuit = temp[0][1] + temp[1][1] + temp[2][1] + temp[3][1]
        for i in suit:
            if tempSuit.count(i) == 4:
                count += 1
    return count/n

print(function_02(100000))

' ' ' Exercise c Bốn lá cùng màu ' ' '
def function_03(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=4)
        tempSuit = temp[0][1] + temp[1][1] + temp[2][1] + temp[3][1]
        for i in red:
            if tempSuit.count(i) == 2:
                count += 1
    return count/n

' ' ' Exercise d Bốn lá cùng chỉ số (tứ quý) ' ' '
def function_04(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=4)
        if temp[0][0] == temp[1][0] == temp[2][0] == temp[3][0]:
            count += 1
    return count/n

' ' ' Exercise e Bốn lá cùng là loại số ' ' '
def function_05(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=4)
        if temp[0][1] == temp[1][1] == temp[2][1] == temp[3][1]:
            count += 1
    return count/n

' ' ' Exercise f Bốn lá cùng là loại hình ' ' '
def function_01(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=4)
        if temp[0][0] == temp[1][0] == temp[2][0] == temp[3][0]:
            count += 1
    return count/n