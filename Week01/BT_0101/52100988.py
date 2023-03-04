from itertools import *

# BT_101
E = {3, 2, 1}

# 1.
E1 = combinations(E,2)
print("1.",end=' ')
for i in E1:
    print(i,end=' ')
print()

# 2.
E2 = permutations(E,2)
print("2.",end=' ')
for i in E2:
    print(i,end=' ')
print()

# 3.
E3 = product(E, repeat=2)
print("3.",end=' ')
for i in E3:
    print(i,end=' ')
print()