n = int(input("Enter the number"))
b = True
for i in range (2,n):
    if n%i == 0 :
        b = False
        break
    
if b :
    print("Prime")
else:
    print("Not Prime")
