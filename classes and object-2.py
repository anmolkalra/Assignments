class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def getcircumference(self):
        print(2*3.14*self.radius)
    def getarea(self):
        print(3.14*self.radius*self.radius)
c1=circle(3)
c1.getcircumference()
c1.getarea()
#2
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def setage(self,age):
        self.age=age
    def setmarks(self,marks):
        self.marks=marks
    def display(self):
        print(self.name,self.rollno,self.age,self.marks)
s1=student('anmol',11)
s1.setage(19)
s1.setmarks(99)
s1.display()
#3
class temprature:
    def convertfahrenheit(self,celsiu):
        self.fahre=celsiu*1.8+32
        print(self.fahre)
    def convertcelsius(self,fahren):
        self.celsius=((fahren-32)/1.8)
        print(self.celsius)
t1=temprature()
t1.convertfahrenheit(20)
t1.convertcelsius(92)
#4
class moviedetails:
    def __init__(self,aname,yor,r):
        pass
       
    def add(self,aname,yor,r):
        self.aname=aname
        self.yor=yor
        self.r=r
    def display(self):
        print(self.aname,self.yor,self.r)
m1=moviedetails('anmol',1999,10)
m1.add('anmol',1999,10)
m1.display()
#5
class animal:
    def animal_attribute(self):
        print("this is animal class")
class Tiger(animal):
    pass
a1=animal()
t1=Tiger()
t1.animal_attribute()
#6
A B
A B
#7
class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        pass
class rectangle(shape):
    def area(self):
        print(self.length*self.breadth)
class square(shape):
    def area(self):
        print(self.length*self.length)
s1=shape(2,3)
r1=rectangle(10,20)
s2=square(10,10)
r1.area()
s2.area()


