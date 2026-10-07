#iteration-step by step process
#recursion -to call a function itself
#arg pass return value
#no arg return value
#arg pass no return value
#no arg no return

#types of recursions
#direct
#indirect
#head
#tail
#tree 
#nested

#direct recursion
'''def numbers(n):
    if n==0:
        print("Done")
        return
    print(n,end=' ')
    numbers(n-1)
n=int(input("Enter a value: "))
numbers(n)

#indirect recursion
def even(n):
    if n==0:
        print(copy, "is even")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print(copy, 'is odd')
        return
    even(n-1)
n=int(input("enter a value: "))
copy=n
even(n)

#tree recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("Enter a number: "))
for i in range(n):
    print(fib(i),end=' ')

def tree(n):
    if n<=0:
        return
    print(n,end=' ')
    tree(n-1)
    tree(n-1)
n=int(input("enter a number: "))
tree(n)

def tree(n):
    if n<=-1:
        return
    print(n,end=' ')
    tree(n-1)
    tree(n-1)
n=int(input("enter a number: "))
tree(n)'''

#head recursion
def head(n):
    if n==0:
        return
    head(n-1)
    print(n)
n=int(input("Enter a value: "))
head(n)