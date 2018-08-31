#1
import datetime as dt

date=dt.datetime.now()
print(date.day)
#2
import webbrowser as wb
wb.open("https://www.youtube.com/watch?v=0xhK7yBYWCY")
#3
import os
os.chdir("E:\newdirectory")
path =  os.getcwd()
filenames = os.listdir(path)
z=5
print(filenames)

for filename in filenames:
    os.rename(filename,str(z)+'.jpg')
    i=i+1
