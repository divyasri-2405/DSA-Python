#circular queue-insert
from queue import Queue
q=Queue()
arr=list(map(int,input("Enter elements: ").split()))
for x in arr:
    q.put(x)
value=input("Enter value to insert: ")
q.put(value)
n=q.qsize()
print("Circular queue: ",end=' ')
for x in range(n+1):
    x=q.get()
    print(x,end=' ')
    q.put(x)

'''#circular queue-peek
from queue import Queue
q=Queue()
arr=list(map(int,input("Enter elements: ").split()))
for x in arr:
    q.put(x)
if q.empty():
    print("Queue is empty")
else:
    print("Front Element: ",q.queue[0]) #peek

#circular queue-rotate
from queue import Queue
q=Queue()
arr=list(map(int,input("Enter elements: ").split()))
for x in arr:
    q.put(x)
if not q.empty():
    x=q.get()
    q.put(x)
print("Queue after rotate: ",q.queue)
print("Queue after rotate: ",list(q.queue))

#circular queue-search
from queue import Queue
q=Queue()
arr=list(map(int,input("Enter elements: ").split()))
for x in arr:
    q.put(x)
value=int(input("Enter the value to be searched: "))
if value in q.queue:
    print("Value found")
else:
    print("Value not found")

#circular queue-isEmpty
from queue import Queue
q=Queue()
arr=list(map(int,input("Enter elements: ").split()))
for x in arr:
    q.put(x)
if q.empty():
    print("Queue is empty")
else:
    print("Queue is not empty",list(q.queue))'''

#circular queue-isFull
from queue import Queue
q=Queue(maxsize=3)
arr=list(map(int,input("Enter elements: ").split()))
for x in arr:
    if not q.full():
        q.put(x)
    else:
        print("Queue is full cannot be inserted",x)
if q.full():
    print("Queue is full")
else:
    print("Queue is not full")
print("Queue Elements: ",list(q.queue))