# 52100988 Lữ Phúc Phú

' ' ' Check-in ' ' '
from itertools import product
import random


number = ['1','2','3','4','5','6']
dice = list(product('D',number))
temp = []
for i in dice:
    str = ''
    temp.append(str.join(i))
dice = temp
print(dice)

' ' ' Exercise01 2 viên cùng chẵn ' ' '
def function_01(n):
    count = 0
    for i in range(n):
        temp1 = random.choice(dice)
        temp2 = random.choice(dice)
        if int(temp1[1])%2==0 and int(temp2[1])%2==0:
            count +=1
    return count/n

' ' ' Exercise02 một chẵn một lẻ ' ' '
def function_02(n):
    count = 0
    for i in range(n):
        temp1 = random.choice(dice)
        temp2 = random.choice(dice)
        if int(temp1[1])%2==1 and int(temp2[1])%2==0:
            count +=1
        if int(temp1[1])%2==0 and int(temp2[1])%2==1:
            count +=1
    return count/n

' ' ' Exercise03 cả 2 đều ra 7 ' ' '
def function_03(n):
    count = 0
    for i in range(n):
        temp1 = random.choice(dice)
        temp2 = random.choice(dice)
        if int(temp1[1])==7 and int(temp2[1])==7:
            count +=1
    return count/n

' ' ' Exercise04 tổng số nút 2 viên lớn hơn 10 ' ' '
def function_04(n):
    count = 0
    for i in range(n):
        temp1 = random.choice(dice)
        temp2 = random.choice(dice)
        if int(temp1[1]) + int(temp2[1]) > 10:
            count +=1
    return count/n

print(function_01(10))