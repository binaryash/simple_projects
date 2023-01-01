import random
passwords = []
password1 = ""
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','&','(',')']
a = int(input("Enter the number of alphabets"))
b = int(input("Enter the number of numbers"))
c = int(input("Enter the number of symbols"))
d = random.choices(alphabets,k = a) + random.choices(numbers,k = b) + random.choices(symbols,k = c)
random.shuffle(d)
for i in d:
    password1+=i
print(f"your password is {password1}")
