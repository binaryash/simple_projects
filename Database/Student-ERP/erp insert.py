import sqlite3

erpdtb = sqlite3.connect('erp.db')

data = erpdtb.cursor()

n = int(input("Enter the number of days to enter: "))
for i in range (n):
    sub =(input("enter the subject name: "))
    dt = int(input("Enter the date: "))
    dy = int(input("Enter the day: "))
    yr = int(input("Enter the year: "))
    prab =(input("Were you present or absent p/a"))
    data.execute(f'''INSERT INTO attd VALUES ('{sub}',{dt},{dy},{yr},'{prab}')''')


erpdtb.commit()
erpdtb.close()



