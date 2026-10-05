#find out it is niven's number or not
n=int(input("Enter a number: "))
s=0
c=n
while n!=0:
    d=n%10
    s+=d
    n//=10
if c%s==0:
    print("niven number")
else:
    print("Not niven number")