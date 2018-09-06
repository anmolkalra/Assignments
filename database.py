#1

import sqlite3

con = sqlite3.connect('Students.db')
print(" database successfully opened")
con.close()
#2

try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'create table students(Name varchar(10) primary key, \
    Marks int(3))'
    
    cursor.execute(query)
    
    print('Table created !')
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('error occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!')

l = []
i=0
while(i<10):
    try:
        name = input("Enter the name: ")
        marks = int(input('Enter your Marks: '))
        if(marks<0 or marks >100):
            raise ValueError('Invalid entry of marks')
            i=i-1
        else:
            t = name,marks
            l.append(t)
            i=i+1
    except  ValueError as msg:
        print(msg)

#3
try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = "insert into students(Name, Marks) \
    values(?,?)"
    
    records = l
    
    cursor.executemany(query, records)
    
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')

#4

try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'select * from students where Marks > 80'
    
    cursor.execute(query)
    
    data = cursor.fetchall()

    print("Name of Student who scored greater then 80 are :")
    for row in data:
        print('Name: {}'\
             .format(row[0]))
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')
