#linear search
#binary search
#jump search

#binary search
n=int(input("Enter number of elements: "))
arr=[]
print("Elements in sorted order: ")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter element to search: "))
left=0
right=n-1
found=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        found=mid
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
if found!=-1:
    print("Value found at index",found)
else:
    print('Value not found')