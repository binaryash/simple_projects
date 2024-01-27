# Inventory management using text files

import os

def readitems():
    f = open("items.txt",'r')
    itemslist = f.readlines()
    f.close()
    return itemslist


def additems(items):
    f1 = open("inventory.txt", 'a')
    f1.write(items)
    f1.close()

def sales(itemcode1, salesno):
    with open("inventory.txt", 'r') as f2:
        inventorylist = f2.readlines()

    for i in range(len(inventorylist)):
        items1 = inventorylist[i].split(',')
        if items1[0] == itemcode1:
            item_no_new = int(items1[1].replace('\n', '')) - salesno
            inventorylist[i] = f"{itemcode1},{item_no_new}\n"

    # Write the updated content back to the file
    with open("inventory.txt", 'w') as f2:
        f2.writelines(inventorylist)

    with open("sales.txt","r") as f3:
        saleslist = f3.readlines()

        for j in (len(saleslist)):
            items2 = saleslist[j].split(',')
            if items2[0] == itemcode1:
                item_new_no = int(items2[1].replace('\n','')) + salesno
                saleslist[i] = f"{itemcode1},{item_new_no}\n"

    with open("sales.txt",'w') as f3:
        f3.writelines(saleslist)


print(" Do you want to see or add items ? 1 to view or 2 to add or 3 for sales")
a = int(input("Enter the number"))
if (a == 1):
    b = int(input("Enter 1 to view by product number or 2 for whole list"))
    if (b == 1):
        for k in readitems():
            print(k,end='')
    elif (b == 2):
        itemcode = input("Enter the item code")
        itemlist = readitems()
        for i in itemlist:
            if itemcode in i:
                print(i)
elif (a==2):
    itemcode1 = input("Enter the item code")
    itemno = int(input("Enter the number of items to be added"))
    addeditem = (f"{itemcode1},{itemno}\n")
    additems(addeditem)

elif (a==3):
        itemcode1 = input("Enter the item code")
        salesno = int(input("number of items sold"))
        sales(itemcode1,salesno)
        
else :
    print("Invalid Input")



