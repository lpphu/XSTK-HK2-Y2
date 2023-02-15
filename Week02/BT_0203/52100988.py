# 52100988 Lữ Phúc Phú
import random
import numpy as np


white = ['w1', 'w2', 'w3', 'w4'] 
black = ['b1', 'b2', 'b3', 'b4', 'b5'] 
red = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6'] 

box = white
box  = np.append(black,box)
box  = np.append(red,box)

# print(box)

' ' ' Exercise01 ' ' '
def def_function_01(n):
    count = 0
    for i in range(n):
        tempList = random.choices(box,k=3)
        if tempList[0][0] != tempList[1][0] and tempList[0][0] != tempList[2][0] and tempList[1][0] != tempList[2][0]:
            count+=1
    return count/n
print("1.", def_function_01(10))

' ' ' Exercise02 ' ' '
def def_function_02(n):
    count = 0
    for i in range(n):
        tempList = random.choices(box,k=3)
        c = 0
        for i in tempList:
            if i[0] == 'w':
                c+=1
        if c>0:
            count+=1
    return count/n
print("2.", def_function_02(10))

' ' ' Exercise03 ' ' '
def def_function_03(n):
    count = 0
    for i in range(n):
        tempList = random.choices(box,k=3)
        if tempList[0][0] == 'w':
            count+=1
    return count/n
print("3.", def_function_03(10))

' ' ' Exercise04 ' ' '
def def_function_04(n):
    count = 0
    for i in range(n):
        tempList = random.choices(box,k=3)
        if tempList[0][0] == 'w' and tempList[2][0] == 'r':
            count+=1
    return count/n
print("4.", def_function_04(10))

' ' ' Exercise05 ' ' '
def def_function_05(n):
    count = 0
    for i in range(n):
        tempList = random.choices(box,k=3)
        if tempList[0][0] == tempList[1][0] == tempList[2][0]:
            count+=1
    return count/n
print("5.", def_function_05(10))