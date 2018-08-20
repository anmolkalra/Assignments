#1
a = []
x = int(input("enter the no of elements "))
for i in range(x):
    c=input("enter element")
    a.append(c)
print(a)


#2
b = ['google','apple','facebook','microsoft','tesla']
a.extend(b)
print(a)

#3
w = [2,3,4,1,2,3,4,3,3,5,3,3,3,4,5]
print(w.count(3))

#4
q = [3,2,6,7,9,5,34,56,78,98,76,102,67,152]
q.sort()
print(q)

#5
r =[1,2,3,4,5]
e=[6,7,8,9]
f=[]
r.extend(e)
f=r
r.sort()
print(r)

#6
rt=[1,2,3,4,5,6]
e=0
o=0
for i in rt:
    if(i%2==0):
        
        
        e=e+1
    else:
      
        o=o+1
    
print(" even numbers =",e)
print("odd numbers =",o)







#7
t=(5,3,6,7)
print(t[::-1])


#8
t2=(7,8,3,2)
print("Largest element=",max(t2))
print("Smallest element=",min(t2))






#9
s='anmol'
s1=s.upper()
print(s1)


#10
s2='6789'
s4='1267abc'
s3=s2.isdigit()
s5=s4.isdigit()
print(s3)
print(s5)


#11
s6='hello world'
s7=s6.replace('world','Anmol')
print(s7)

