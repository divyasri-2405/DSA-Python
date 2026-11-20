'''import heapq
arr=list(map(int,input("Enter elements: ").split()))
heapq.heapify(arr)
print("Heapified array: ",arr)
value=int(input("Enter value to be inserted: "))
heapq.heappush(arr,value)
print("Array after insertion: ",arr)
heapq.heappop(arr)
print("Array after deletion: ",arr)

import heapq
arr=list(map(int,input("Enter elements: ").split()))
heapq.heapify(arr)
print("Heapified array: ",arr)
value=int(input("Enter value to be inserted: "))
heapq.heappushpop(arr,value)
print("Array after insertion & deletion: ",arr)'''

import heapq
arr=list(map(int,input("Enter elements: ").split()))
heapq.heapify(arr)
print("Heapified array: ",arr)
value=int(input("Enter value to be replaced: "))
heapq.heapreplace(arr,value)
print("Array after replacement: ",arr)