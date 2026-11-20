'''import heapq
arr=list(map(int,input("Enter elements: ").split()))
n=int(input("Enter the value of n: "))
print(heapq.nlargest(n,arr))
print(heapq.nsmallest(n,arr))'''

import heapq
arr=list(map(int,input("Enter elements: ").split()))
heapq.heapify(arr)
result=[]
while arr:
    result.append(heapq.heappop(arr))
print("The sorted elements are: ",result)