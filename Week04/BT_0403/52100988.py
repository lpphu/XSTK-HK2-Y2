# 52100988 Lữ Phúc Phú

' ' ' BT_0403 ' ' '

' ' ' a. ' ' '
from itertools import *

print('a.')
URN = ['W1','W2','B1','B2','B3','R1','R2','R3','R4']

' ' ' b. ' ' '
print('b.')
U3 = list(combinations(URN,3))
print(U3)

' ' ' c. ' ' '
count = 0
print('c.')
white1blue1red1 = []
for i in U3:
    temp = ''.join(i)
    check = True
    for k in ['W','B','R']:
        if temp.count(k) > 1:
            check = False
            break
    if check:
        count += 1
        white1blue1red1.append(temp)
print(white1blue1red1)

' ' ' d. ' ' '
print('d. =',100*count/len(U3),'%')



