#Basic Calculator Program which can store past 3 calculation history


hist1 = 0
hist2 = 0
hist3 = 0

print("      BASIC CALCULATOR")
print("      ----------------\n\n\n")
h = input(" Enter a to add, b to subtract, c to multiply , d to divide \n\n\n ")

f = int(input("enter the first number"))
g = int(input("enter the second number"))

if h =='a':
    print("the sum is", f+g)
elif h =='b':
    print("the sum is", f-g)
elif h =='c':
    print("the product is:", f*g)
elif h =='d':
    print("the quotient is ",f/g)
