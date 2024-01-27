import random
c = input("Enter \"hard\" or \"easy\" ")
d = random.randint(1,100)
if c == "hard":
    global a
    a = 5
elif c == "easy":
    a = 10
for i in range (a,0,-1):
    e = int(input("Enter the number: "))
    if e < d:
        print("Too low")
    elif e > d :
        print("Too High")
    elif e == d:
        print('Youre Correct! ')
        break
    
