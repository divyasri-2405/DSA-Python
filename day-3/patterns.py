'''#print a square
n=int(input("enter n: "))
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()

#print a hollow square
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#print a hallow square with diagonal and anti-diagonal
n=int(input("enter the n value"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#print a hour sand glass
n=int(input("enter n value: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#print butterfly
n=int(input("enter n value: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#print + symbol
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()