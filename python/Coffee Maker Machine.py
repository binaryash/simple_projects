print('''
_________         _____  _____                  _____                .__    .__               
\_   ___ \  _____/ ____\/ ____\____   ____     /     \ _____    ____ |  |__ |__| ____   ____  
/    \  \/ /  _ \   __\\   __\/ __ \_/ __ \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\     \___(  <_> )  |   |  | \  ___/\  ___/  /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \______  /\____/|__|   |__|  \___  >\___  > \____|__  (____  /\___  >___|  /__|___|  /\___  >
        \/                        \/     \/          \/     \/     \/     \/        \/     \/ 
        ''')

hf = 0
hs = True
ingredient = {
    "capucchino" : [500, 50, 150, 100],
    "expresso": [250, 25, 100, 50],
    "latte": [100, 10, 50, 25]
}

money = {
    1:0,
    2:0,
    5:0,
    10:0,
}
money2 = 0
powder2 = 2000
milk = 3000
water = 3000

class CoffeeMaker:
    def __init__ (self,mone):
        self.mone = c

    def money1(self):
        global money2
        global hf
        change = 0
        if c< ingredient[b][0]:
            print("insufficient balance")
            pass
        else:
            cd = 0
            change = c-ingredient[b][0]
            print(f"the change is {change}")
            money2+=(c-change)
            cd = c
            money[10] = cd//10
            cd = cd%10
            money[5] = cd//5
            cd = cd%5
            money[2] = cd//2
            cd = cd%2
            money[1] = cd//1

            hf+=1


    def water1(self):
        global water,hf
        if water < ingredient[b][3]:
            print("Insufficient water")
        else:
            water-=ingredient[b][3]
            hf+=1

    def powder(self):
        global powder2,hf
        if powder2 < ingredient[b][1]:
            print("Insufficient powder")
        else:
            powder2-=ingredient[b][1]
            hf+=1


    def milk(self):
        global milk,hf
        if milk < ingredient[b][2]:
            print("Insufficient milk")
        else:
            milk-=ingredient[b][2]
            hf+=1



while hs:
    hf = 0
    a = ingredient.keys()
    print("We have :- ")
    for i in a:
        print(i, end = " - price = ")
        print(ingredient[i][0], end = " , ")
    print()
    b = input("Choose what you want to try : ")
    c = int(input("Enter the money "))
    d = CoffeeMaker(c)
    d.money1()
    d.water1()
    d.powder()
    d.milk()
    print("Denominations are ", end = " = ")
    print(money)
    print(f"Amount in machine is : {money2}")
    print(f"remaining powder is : {powder2}")
    print(f"remaining milk is : {milk}")
    print(f"remaining water is : {water}")
    if hf == 4:
        print("Here's your drink !")
    else:
        print("Failure")
    afg = input("Do you want to continue? \"yes\" or \"no\" ")
    if afg == "no":
        print("Thank You")
        hs = False





