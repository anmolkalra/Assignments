#1
def area():
    radius=float(input("enter the radius of sphere"))
    areaa=(4*3.14*(radius**2))
    return areaa
print("area of sphere is:",area())
#2

def perfect(num):
    c=0
    for i in range(1,num):
        if(num%i==0):
            c=c+i
    if(c==num):
        print(num)
for i in range(1,1001):
    perfect(i)
#3
n=int(input("enter number"))
def table(n):
    for i in range(1,11):
        print("{}*{}=".format(n,i),(n*i))
table(n)
#4
a=int(input("enter a"))
b=int(input("enter b"))

def fun(b):
    
    if(b==0):
        return 1
    else:
        return a*fun(b-1)
    
print(fun(b))
    

