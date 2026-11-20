#two pointer approach from either sides palindromic array
arr=list(map(int,input("Enter elements: ").split()))
left=0
right=len(arr)-1
while left<right:
    if arr[left]!=arr[right]:
        found=False
        break
    left+=1
    right-=1
if found:
    print("Palindromic array")
else:
    print("Not a Palindromic array")

#two pointer approach from either sides find the middle element of an array
arr=list(map(int,input("Enter elements: ").split()))
slow=0
fast=0
while fast<len(arr)-1 and fast+1<len(arr):
    slow+=1
    fast+=2
print("Middle element: ",arr[slow])
