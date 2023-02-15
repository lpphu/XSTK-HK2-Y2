# 52100988 Lữ Phúc Phú
' ' ' BT_0202 ' ' '
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
print("1.",def_function_01(100000))

' ' ' Exercise02 ' ' '
def def_function_02(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=5)
        c = 0
        for j in temp:
            if j[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                c += 1
        if c == 5:
            count +=1
    return count/n
print("2.",def_function_02(100000))

' ' ' Exercise03 ' ' '
def def_function_03(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=5)
        c = 0
        tempList = []
        for j in temp:
            match j[0]:
                case 'A':
                    tempList.append(1)
                case 'J':
                    tempList.append(11)
                case 'Q':
                    tempList.append(12)
                case 'K':
                    tempList.append(13)
                case _:
                    tempList.append(int(j[0]))
        tempList.sort()
        if tempList[4] > 10:
            tempList = [14 if card == 1 else card for card in tempList]
        tempList.sort()
        
        for i in range(4):
            if tempList[i+1]-tempList[i]==1:
                c+=1
        if c == 4:
            count +=1
    return count/n

print("3.",def_function_03(100000))

' ' ' Exercise04 ' ' '
def def_function_04(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=5)
        c = 0
        tempCard = temp[0]
        for j in temp:
            if j[1] == tempCard[1]:
                c += 1
        if c == 5:
            count +=1
    return count/n
print("4.",def_function_04(100000))

' ' ' Exercise05 ' ' '
def def_function_05(n):
    count = 0
    for i in range(n):
        temp = random.choices(deck,k=5)
        black = red = 0
        for j in temp:
            if j[1] in ['♠' , '♣']:
                black += 1
            else:
                red += 1
        if black == 5 or red == 5:
            count +=1
    return count/n
print("5.",def_function_05(100000))

