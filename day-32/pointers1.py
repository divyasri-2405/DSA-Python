'''#two pointer approach from either sides
arr=list(map(int,input("Enter elements: ").split()))
target=int(input("Enter target: "))
arr.sort()
left=0
right=len(arr)-1
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        print(arr[left],arr[right])
        break
    elif total<target:
        left+=1
    else:
        right-=1
else:
    print("target not found")

#two pointer approach from either sides reverse an array
arr=list(map(int,input("Enter elements: ").split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print("Reversed array: ", *arr)'''

