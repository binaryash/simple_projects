hh = True
a = int(input("enter the first number"))

def calculate():
    if b == "+":
        return a+c
    if b == "-":
        return a-c
    if b == "*":
        return a*c
    if b == "/":
        return a/c

while hh:
    b = input("+ , - , * , / ")
    c = int(input("Enter the second number : "))
    e = calculate()
    d = input("do you want to continue? Type y or n")
    a = e
    if d == "n":
        print(f"the answer is {e}")
        break
