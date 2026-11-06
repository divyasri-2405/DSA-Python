'''#circular queue 
arr=list(map(int,input("Enter elements: ").split()))
start=int(input("Enter starting point: "))
n=len(arr)
print("Traversal: ")
for i in range(n):
    index=(start+i)%n
    print(arr[index],end=' ')

#circular queue-delete operation
arr=list(map(int,input("Enter elements: ").split()))
value=int(input("Enter value: "))
if value in arr:
    arr.remove(value)
    print(arr,end=' ')
else:
    print("Value not found...")

#circular queue-delete operation
queue=list(map(int,input("Enter elements: ").split()))
value=int(input("Enter value: "))
n=len(queue)
found=False
for i in range(n):
    index=i%n
    if queue[index]==value:
        found=True
        for j in range(index,n-1):
            queue[j]=queue[j+1]
        queue.pop()
        break
if found:
    print("After deletion: ",queue)
else:
    print("Value not found...")

insert
peak
rotate
search
is empty
is full'''

