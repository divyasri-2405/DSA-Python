#queue data structure
#fifo-first in first out
#enqueue-insert dequeue-delete
#input-rear output-front

'''#insert operation in queue
from queue import Queue
q=Queue()
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    q.put(value)
print(list(q.queue))

#insert operation in queue and delete operation
from queue import Queue
q=Queue()
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    q.put(value)
print(list(q.queue))
removed=q.get()
print(list(q.queue))

#insert operation in queue check whether it is empty or not
from queue import Queue
q=Queue()
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    q.put(value)
if q.empty():
    print("Queue is Empty")
else:
    print(list(q.queue))

#insert operation in queue check whether it is empty or not and element ready to be deleted
from queue import Queue
q=Queue()
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    q.put(value)
if q.empty():
    print("Queue is Empty")
else:
    print(list(q.queue))
print(q.queue[0]) #peek-ready to be deleted

#insert operation in queue check whether it is full or not
from queue import Queue,Full
size=int(input("Enter queue size: "))
q=Queue(maxsize=size)
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    try:
        q.put_nowait(value)
        print(value,"inserted")
    except Full:
        print("Queue is Full")
        break
    print(list(q.queue))'''

#insert operation in queue check whether it is empty or not

from queue import Queue
q=Queue()
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    q.put(value)
print(list(q.queue))
while not q.empty():
    removed=q.get()
    print(removed,"deleted")
if q.empty():
    print("Queue empty")
else:
    print(list(q.queue))

