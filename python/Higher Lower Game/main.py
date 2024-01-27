import random
from Data import data
from Art import head
from Art import vs 
hf = True
hs = 0
def assign():
    a = random.choice (data)
    return a

def people():
    global pera
    global perb
    pera = assign()
    perb = assign()
    if perb== pera:
        perb = assign()
        
while hf:
    b = input("Do you want to continue? yes or no")
    if b == "yes":
        people()
    elif b == "no":
        break
    print(f"name is {pera['name']}, follower count is {pera['follower_count']} is a {pera['description']} from {pera['country']} ")
    print(vs)
    print(f"name is {perb['name']} is a {perb['description']} from {perb['country']} ")
    
    c = input("higher or lower")
    if (pera['follower_count'] < perb['follower_count'] and c == "higher") or (pera['follower_count']>perb['follower_count'] and c == "lower") :
        print("You Won")
        hs+=1 
    else:
        print("you lost")
        hs = 0
    print(f"your score is {hs}")
    
    
    
    