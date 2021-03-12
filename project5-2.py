# CI SHI
# 2020/03/11

import numpy as np

suits = ["Heart","Diamonds","Clubs","Pikes"]
cards = ['Ace',"2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

deck = []
for (v,s) in zip(cards,values):
    for s in suits:
        deck.append((v,s))

print(np.array(deck))
