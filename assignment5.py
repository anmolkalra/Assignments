#1
x=int(input("enter the year"))
if(x%4==0):
    if(x%100==0):
        if(x%400==0):
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
    
#2
l=int(input("enter the length"))
b=int(input("enter the breadth"))
if(l==b):
    print("dimensions are of square")
else:
    print("dimensions are of rectangle")
    
#3
p1=int(input("enter the age of 1st person"))
p2=int(input("enter the age of 2nd person"))
p3=int(input("enter the age of 3rd person"))
if(p1>=p2 and p1>=p3):
    print("p1 is oldest")
elif(p2>=p1 and p2>=p3):
    print("p2 is oldest")
else:
    print("p3 is oldest")
if(p1<=p2 and p1<=p3):
    print("p1 is youngest")
elif(p2<=p1 and p2<=p3):
    print("p2 is youngest")
else:
    print("p3 is youngest")
#4
age=int(input("enter age"))
sex=input("enter sex")
ms=input("enter marital status")
if(sex=='F'):
    print("work only in urban areas")
else:
    if(age>=20 and age<40):
        print("work anywhere")
    elif(age>=40 and age<60):
        print("work anywhere")
    else:
        print("ERROR")
#5
q=int(input("enter quantity"))
cost=(100*q)
if(cost>1000):
    cost=cost-(0.1*cost)
    print("total cost is",cost)
else:
    print("total cost is",cost)
#6
a=[]
for i in range(10):
    c=int(input("enter number"))
    a.append(c)
for i in a:
    print(i)
#7
while True:
    print('*')
#8
a=[]
b=[]
num=int(input("enter no of numbers"))
for i in range(num):
    w=int(input("enter numbers"))
    a.append(w)
for i in a:
    f=i*i
    b.append(f)
print(b)
#9
li=[]
li1=[]
li2=[]
li3=[]
bn=int(input("enter number"))
for i in range(bn):
    r=input("enter elements")
    li.append(r)
for i in li:
    if(i.isdigit()):
        li1.append(i)
    elif(i.isalpha()):
        li2.append(i)
    else:
        li3.append(i)
print(li1)
print(li2)
print(li3)
#10
a=[]

for i in range(1,101):
    
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                a.append(i)
for i in range(1,101):
    if i not in a:
        print(i)
     
                
#11
for i in range(1,5):
    for j in range(i):
        print('*',end=' ')
    print()
#12
e=[]
f=[]
flag=True
vn=int(input("enter no of elements"))
for i in range(vn):
    d=int(input("enter number"))
    e.append(d)
ele=int(input("enter the element u want 2 search"))
for i in e:
    if(ele==i):
        flag=False
        
    else:
        f.append(i)
if(flag==True):
    print("number not found")

        
    
print(f)
    


    
