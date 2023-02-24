# 52100988 Lữ Phúc Phú
' ' ' BT_0401 ' ' '

import random


blue = ['b1', 'b2']
red = ['r1','r2','r3']
white = ['w1','w2','w3','w4','w5']

box = blue
for i in red:
    box.append(i)
for i in white:
    box.append(i)

' ' ' Exercise01 cả 3 viên khác màu ' ' '
def function_01(n):
    count = 0
    for i in range(n):
        temp = random.choices(box,k=3)
        if temp[0][0] != temp[1][0] and temp[0][0] != temp[2][0] and temp[1][0] != temp[2][0]:
            count += 1
    return count/n

print(function_01(100000))

' ' ' Exercise02 cả 3 viên cùng màu ' ' '
def function_02(n):
    count = 0
    for i in range(n):
        temp = random.choices(box,k=3)
        if temp[0][0] == temp[1][0] == temp[2][0]:
            count += 1
    return count/n

print(function_02(100000))

' ' ' Exercise03 có 2 viên cùng màu ' ' '
def function_03(n):
    count = 0
    for i in range(n):
        temp = random.choices(box,k=3)
        tempColor = temp[0][0] + temp[1][0] + temp[2][0]
        for i in ['r','w','b']:
            if tempColor.count(i) == 2:
                count += 1
    return count/n

print(function_03(100000))

' ' ' Exercise04 có 2 trắng 1 xanh ' ' '
def function_04(n):
    count = 0
    for i in range(n):
        temp = random.choices(box,k=3)
        tempColor = temp[0][0] + temp[1][0] + temp[2][0]
        if tempColor.count('w') == 2 and tempColor.count('b') == 1:
            count += 1
    return count/n

print(function_04(100000))

' ' ' Exercise05 cả 3 viên đỏ ' ' '
def function_05(n):
    count = 0
    for i in range(n):
        temp = random.choices(box,k=3)
        tempColor = temp[0][0] + temp[1][0] + temp[2][0]
        if tempColor.count('r') == 3:
            count += 1
    return count/n

print(function_05(100000))