#1 it is zero division error
try:
     a=3
     if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Zero divison error")
#2
try:
    l=[1,2,3] 
    print(l[3]) 
except IndexError:
    print("out of range")
#3
'''output:
    there is no defualt name error and we have also not make name error user defined
so it will show error'''
#4
'''-5.0
a/b result in 0'''

#5 import error
try:
    
    
    import fibo

    print(math.factorial(4))
    
    
except ImportError:
    print("module is not imported" )
#5.2 value error
try:
    a='abc'
    
    print(int(a))
except ValueError:
    print("wrong value")
#5.3 index error
    try:
    lst=[1,2,3,4]
    print(lst[5])
except IndexError:
    print("out of index")
