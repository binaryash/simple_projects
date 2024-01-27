# Blackjack without Object oriented programming concepts

import random
import os
cards = [2,3,4,5,6,7,8,9,"j","k","q","a",2,3,4,5,6,7,8,9,"j","k","q","a",2,3,4,5,6,7,8,9,
         "j","k","q","a",2,3,4,5,6,7,8,9,"j","k","q","a"]
cust = []
cust2 = 0 
deal = []
deal2 = 0
def draw():
    global cust2
    a = random.choice(cards)
    cust.append(a)
    if a == 'j' or a == 'q' or a =='k':
        cust2+=10
    elif a == 'a':
        if cust2<=12:
            cust2+=11
        else:
            cust2+=1
    else:
        cust2 += a
    cards.remove(a)
        
def draw1():
    global deal2
    a = random.choice(cards)
    deal.append(a)
    if a == 'j' or a == 'q' or a =='k':
        deal2+=10
    elif a == 'a':
        if deal2<=12:
            deal2+=11
        else:
            deal2+=1
    else:
        deal2 += a
    cards.remove(a)


while cust2<=21:
    b = input("hit or stand \n")
    if b == "hit":
        draw()
        print(cust)
        print(cust2)
    elif b == "stand":
        print(cust2)
        break

while deal2 <=17:
    draw1()

if cust2 <= 21:
    if cust2 > deal2:
        print("You won")
    else:
        print("you lost")
print("You Lost\n")
print("Your cards:", cust)
print("Your Total:", cust2)
print("dealer's cards", deal)
print("dealer's Total", deal2)
