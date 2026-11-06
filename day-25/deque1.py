#deque-double ended queue

'''#append/append left/pop/pop left
from collections import deque
dq=deque(map(int,input("Enter values: ").split()))
print(dq)
val=int(input("Enter a value: "))
dq.append(val)
print(dq)
value=int(input("Enter a value: "))
dq.appendleft(value)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)

#count/remove/reverse
from collections import deque
dq=deque(map(int,input("Enter values: ").split()))
print(dq)
x=int(input("Enter value: "))
print("count: ",dq.count(x))
y=int(input("Enter value to remove: "))
y=dq.remove(y)
print("Remove: ",dq)
dq.reverse()
print(dq)'''

#insert/rotate-clock and anti-clockwise/clear
from collections import deque
dq=deque(map(int,input("Enter values: ").split()))
print(dq)
x=int(input("Enter value: "))
dq.rotate(x)
print(dq)
y=int(input("Enter value: "))
dq.rotate(-y)
print(dq)
pos=int(input("Enter pos: "))
z=int(input("Enter value: "))
dq.insert(pos,z)
print(dq)
dq.clear()
print(dq)