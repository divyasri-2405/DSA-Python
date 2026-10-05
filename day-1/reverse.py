#reverse a given number
n=int(input("Enter the number "))
rev=0
while n!=0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print("reverse of digits", rev)