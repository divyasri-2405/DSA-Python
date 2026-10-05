'''#generating numbers n times
n=int(input("enter the number"))
for i in range(n):
    print("India")

n=int(input("enter the number"))
for i in range(n):
    print(i,end=" ")'''

#generating numbers n times and finding its sum/2
n=int(input("Enter a number: "))
sum=0
for i in range(n):
    sum+=i
    print(i,end=" ")
print()
print("sum: ",sum)

n=int(input("Enter a number: "))
sum=0
for i in range(n):
    sum+=i/2
    print(i,end=" ")
print()
print("sum: ",sum)



