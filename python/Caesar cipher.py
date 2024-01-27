print(" CAESAR CIPHER ")
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nex = 'yes'
while nex == 'yes':
    n = input("enter whether to encode or decode")
    if n == 'encode':
        a = input("enter a word ")
        b = int(input("enter a shift number"))
        for i in range(0,len(a)):
            c =(a[i])
            if c ==' ':
                print(c,end = '')
            else:
                d = (alpha.index(c))
                e = d+b 
                print(alpha[e], end = '')
        print()
    if n == 'decode':
        a = input("enter a name")
        b = int(input("enter a shift number"))
        for i in range(0,len(a)):
            c =(a[i])
            if c == ' ':
                print(c,end = '')
            else:
                d = (alpha.index(c))
                e = d-b 
                print(alpha[e],end = '')
        print()
    nex = input("do you want to continue? type yes or no ")
print("Thank You")
