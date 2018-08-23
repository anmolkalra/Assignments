#1
d=eval(input('enter dic'))
e=int(input("enter the value"))
flag=False
for i in d.items():
    
    if(e==i[1]):
        
        print(i[0])
#2
dic1={}
for i in range(2):
    stu=input("enter student name")
    for j in range(2):
        sub=input("enter subject ")
        marks=input("enter marks")
        
        dic1[stu,sub]=[sub,marks]
name=input("enter name")
for j in dic1.items():
    for r in range(2):
        if(j[r][0]==name):
            print(j[1])
