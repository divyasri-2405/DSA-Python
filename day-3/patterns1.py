'''#left triangle
n=int(input("Enter n value: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#right traingle
n=int(input("enter n value: "))
for i in range(n):
    for j in range(n):
        if j==n-1 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#reverse left traingle
n=int(input("enter n value: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#reverse right triangle
n=int(input('enter n value: '))
for i in range(n):
    for j in range(n):
        if j==n-1 or i==0 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#print a pyramid
n=int(input("enter n: "))
for i in range(1,n-1):
    print(' '*(n-i),end=' ')
    print('* '*i)
print()

#print equilateral pyramid
n=int(input("enter n: "))
for i in range(1,n-1):
    print(' '*(n-i),end=' ')
    print('*'*(2*i-1))
print()'''

#print normal pyramid
n=int(input("enter n: "))#normal pyramid
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    print('*'*(2*i-1))
print()

#print hallow pyramid
n=int(input("enter n: "))
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    if i==1:
        print('*')
    elif i==n:
        print('*'*(2*i-1))
    else:
        print('*'+' '*(2*i-3)+'*')