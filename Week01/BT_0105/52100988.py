from itertools import *

# BT_105
card = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K'}
suit = {'♠' , '♣', '♦', '♥'}
deck = list(product(card,suit))

' ' ' Câu 1 ' ' '
C5 = combinations(deck, 5)
for i in C5:
    print(i)

' ' ' Câu 2 ' ' '
red = list(product(card,('♦', '♥')))
black = list(product(card,('♠' , '♣')))

C5 = product(red,combinations(black,4))
for i in C5:
    print(i)

' ' ' Câu 3 ' ' '
C5 = combinations(deck, 5)
for i in C5:
    print(i[0])


S5 = product(combinations(suit,3),suit,suit)
