'''#counter-(case sensitive-Counter)
from collections import Counter
nums=input("Enter numbers: ").split()
c=Counter(nums)
print("Counter:",c)
#most common number
print(c.most_common(1)) #most repeated number

#default dict-(no case sensitive-defaultdict)
from collections import defaultdict
d=defaultdict(int)
n=int(input("Enter number of elements: "))
for i in range(n):
    key=input("Enter key: ")
    d[key]+=1
print("Dictionary: ",dict(d))

#named tuple-(no case sensitive-namedtuple)
from collections import namedtuple
Student=namedtuple("Student",["name","age","marks"])
name=input("Enter name: ")
age=int(input("Enter age: "))
marks=int(input("Enter marks: "))
s=Student(name,age,marks)
print("Student",s)
print(s)
print("Name",s.name)
print("Marks",s.marks)'''

#ordered dictionary
from collections import OrderedDict
d=OrderedDict()
n=int(input("Enter number of elements: "))
for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    d[key]=value
print("Ordered dictionary: ",d)
print(d)

#chainmap
from collections import ChainMap
d1={}
d2={}
n=int(input("Enter numbers of elements in d1: "))
for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    d1[key]=value
n=int(input("Enter numbers of elements in d2: "))
for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    d2[key]=value 
c=ChainMap(d1,d2)
print("First data: ",d1)
print("Second data: ",d2)
print("ChainMap",c)
print(d1)
print(d2)
print(c)