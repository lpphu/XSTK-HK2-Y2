# 52100988 Lữ Phúc Phú

' ' ' BT_0404 ' ' '
from itertools import *

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

' ' ' a. Xác suất lý thuyết bốc sảnh 5 lá ' ' '
C5 =list(combinations(deck,5))
count = 0
for i in C5:
    tempList = []
    c = 0
    for j in i:
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
print('a. = ',100*count/len(C5),'%')





' ' ' b. Xác suất thực nghiệm bốc sảnh 5 lá ' ' '
def def_function_02(n):
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







