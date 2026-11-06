#queue operations using 2 stacks
stack1=[]
stack2=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    val=int(input("Enter value: "))
    stack1.append(val)
print("queue: ",stack1)
while stack1:
    stack2.append(stack1.pop())
print("Deleted: ",stack2.pop())
while stack2:
    stack1.append(stack2.pop())
print("Queue after deletion: ",stack1)