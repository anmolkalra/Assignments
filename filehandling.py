

#1
f=open('test.txt')
lines=f.readlines()
print(lines)
c=int(input("enter n"))
for i in range(c):
    print(lines[i])
f.close()
#2
a=[]
dict1={}

f=open('test.txt')
data=f.read()
print(data)


a=(data.split())
for i in a:
    dict1[i]=a.count(i)
print(dict1)
f.close()
#3
f=open('test.txt')
g=open('test1.txt','w')

data=f.read()
g.write(data)
g.close()

g=open('test1.txt')
d=g.read()
print(d)
g.close()
f.close()
#4
f=open('test.txt')
g=open('test1.txt')
data=f.read()
ty=g.read()
print(ty)
a=data.split()
b=ty.split()

for i in range(len(a)):
    print(a[i]+b[i])
g.close()
f.close()
#5
b=[]
f=open('test.txt','w')
for i in range(10):
    a=input('enter element')
    f.write(a)
    f.write('\n')
f.close()
f=open('test.txt')
data=f.read()
t=data.split()

for i in t:
    b.append(int(i))
b.sort()
f.close()
f=open('test.txt','w')
for i in b:
    u=str(i)
    f.write(u)
f.close()
f=open('test.txt')
rt=f.read()


g=open('test1.txt','w')
g.write(rt)
g.close()
g=open('test1.txt')
ty=g.read()
print(ty)
g.close()
f.close()

