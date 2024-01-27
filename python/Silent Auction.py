import os
bidder = {} 
highest_amt = 0
name = ""
def highest_bid():
    global highest_amt 
    global name
    ab = bidder.keys()
    for i in ab:
        if highest_amt < bidder[i]:
            highest_amt = bidder[i]
            name = i


hf = True
while hf == True:
    a = input("Enter the name of the bidder: ")
    b = int(input("enter the amount: "))
    bidder[a] = b
    c = input("do you want to continue, Type yes or no: ")
    if (c == 'yes'):
        hf = True
    else:
        hf = False
    os.system('cls')

highest_bid()
print(f" {name} is the winner and the amount paid is {highest_amt}")
