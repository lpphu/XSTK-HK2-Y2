from itertools import *

# BT_102
E = {'W1', 'W2', 'W3', 'W4', 'B1', 'B2', 'B3'}

# 1.
print("1.")
E1 = combinations(E,2)
s=0
for i in E1:
    s+=1
    print(i,end=' ')
print()
print("Have",s,"ways")

# 2.
print("2.")
s=0
E1 = product(('W1', 'W2', 'W3', 'W4'),('B1', 'B2', 'B3'))
for i in E1:
    s+=1
    print(i,end=' ')
print()
print("Have",s,"ways")

# 3.
print("3.")
s=0
E1 = product(('W1', 'W2', 'W3', 'W4'),('B1', 'B2', 'B3'))
for i in E1:
    s+=1
    print(i,end=' ')
E1 = combinations(('W1', 'W2', 'W3', 'W4'),2)
for i in E1:
    s+=1
    print(i,end=' ')
print()
print("Have",s,"ways")