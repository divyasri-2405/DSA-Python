#approaches
#naive approach
#math approach
#brute force
#greddy approach
#backtracking

'''#math approach
r=int(input("enter the value of r: "))
area=3.14159*r*r
cir=2*3.14159*r
print("Area: ",area)
print("Circumference: ",cir)

#math approach series expression
#till n numbers
import math
n=int(input("enter n value: "))
s=0
for i in range(1,n+1):
    s+=math.factorial(i)/(i+1)
print(s)

n=int(input("Enter the value of n: "))
s=0
f=1
for i in range(1,n+1):
    f*=i
    s+=f/(i+1)
print(s)

#naive approach max of a list
arr=list(map(int,input().split()))
max=arr[0]
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]>max:
            max=arr[j]
print(max)

arr=list(map(int,input().split()))
max=arr[0]
for i in range(1,len(arr)):
      if arr[i]>max:
          max=arr[i]
print(max)'''

#brute approach for anagram
s1=input().lower().replace(' ','')
s2=input().lower().replace(' ','')
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print(s1, "is anagram with", s2)
    else:
        print(s1, "is not anagram with", s2)