import sqlite3
count = 0
count1 = 0
count2 = 0
b = 0

erpdtb = sqlite3.connect('erp.db')

data = erpdtb.cursor()
data.execute('''SELECT * FROM attd''')
ab = data.fetchall()
for i in ab:
    if (i[4]=='a'):
        count+=1
    else:
        count1+=1

avg = (count1/(count1+count))

print(f" present = {count1},\n absent = {count},\n attendance percentage = {round(avg,2)}\n")
while b == 0:
    c = input("enter the subject ")
    for i in ab:
        if i[0] == c and i[4] == 'a':
            count2+=1
    print(f"you have been absent in {c} for {count2} days\n\n")
    count2 = 0
    b = int(input("Do you want to continue, 0 for yes 1 for no "))



erpdtb.commit()
erpdtb.close()


