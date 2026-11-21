#prefix sum
arr=list(map(int,input("Enter elements: ").split()))
prefix=[]
total=0
for num in arr:
    total+=num
    prefix.append(total)
print("Prefix sum: ",prefix)

#prefix sum range
arr=list(map(int,input("Enter elements: ").split()))
prefix=[arr[0]]
for i in range(len(arr)):
    prefix.append(prefix[i-1]+arr[i])
print(prefix)
start=int(input("Enter starting index: "))
end=int(input("Enter ending node: "))
if start==0:
    print(prefix[end])
else:
    print(prefix[end]-prefix[start-1])