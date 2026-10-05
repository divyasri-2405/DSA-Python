'''#Constant time complexity
n=int(input("Enter a number: "))
print("Number: ",n) #T.C=O(1),S.C=O(1)

#Linear time complexity
#O(n)
n=int(input("Enter a number: "))
for i in range(n):
    print(i,end=' ') #T.C=O(n),S.C=O(1)

#convert O(n) to O(1)
n=int(input("Enter a number: "))
s=0
for i in range(n):
    s+=i
print(s) #T.C=O(1),SC=O(1)

#TC=O(n),SC=O(2)
n=int(input("Enter a number: "))
for i in range(n):
    print(i,'vijay',end=' ')

#quadratic time complexity
#TC-O(n^2) SC=O(2)
n=int(input("Enter n: "))
for i in range(n): 
    for j in range(n):
        print(i,j,end=' ')
    print()

#TC-O(n^3) SC=O(3)
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        for k in range(n): 
          print(i,j,k,end=' ')
        print()
    print()

n=int(input("enter n: ")) #TC-O(n(2n))=O(2(n^2)),SC-O(1)
for i in range(n):
    for j in range(n):
        print('😊',end=' ')
    for k in range(n):
        print('👍',end=' ')
    print()
print()

n=int(input("enter n: ")) #TC-O(2n),SC-O(1)
for j in range(n):
    print('😊',end=' ')
for k in range(n):
    print('👍',end=' ')
print()

n=int(input("enter n: ")) #TC-O(n(2n))=O(2(n^2)),SC-O(1)
for i in range(n):
    for j in range(n):
        print('hello',end=' ')
    for k in range(n):
        print('hi',end=' ')
    print()
print()

n=int(input("enter n: ")) #TC-O(n(3n))=O(3(n^2)),SC-O(1)
for i in range(n):
    for j in range(n):
        print('hello',end=' ')
    for k in range(n):
        print('hi',end=' ')
    for l in range(n):
        print('bye',end=' ')
    print()
print()'''

#logarithmic time complexity
#TC-O(log(n)) SC-O(1)
n=int(input("Enter n:"))
while n>1:
    print(n)
    n//=2

import math #TC-O(log(log(n))),SC-O(1)
n=int(input("Enter n:"))
while n>2:
    print(n)
    n=math.sqrt(n)