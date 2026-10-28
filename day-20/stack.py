'''#stack operations-push
stack=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    stack.append(value)
print("Stack", stack)
#peek
print("Stack peek element: ",stack[-1])
#pop
print("Removed: ",stack.pop())
print("Stack", stack)
print("Stack peek element: ",stack[-1])

#stack operations-isEmpty condition
stack=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    stack.append(value)
print("Stack", stack)
while len(stack)>0:
    print("Popped:",stack.pop())
if len(stack)==0:
    print("Stack Empty")

#stack operations-overflow operations
stack=[]
size=int(input("Enter the size of the stack: "))
n=int(input("Enter number of elements: "))
for i in range(n):
    value=int(input("Enter value: "))
    if (len(stack)<size):
        stack.append(value)
        print("Pushed: ",value)
    else:
        print("Stack overflow....")
print("Stack", stack)'''

#stack operations-merge two stacks
#s1=[1,3,5],s2=[2,4,6] merged=[1,2,3,4,5,6]
stack1=[]
stack2=[]
merged=[]
n1=int(input("Enter number of elements: "))
for i in range(n1):
    value=int(input("Enter value: "))
    stack1.append(value)
n2=int(input("Enter number of elements: "))
for j in range(n2):
    value=int(input("Enter value: "))
    stack2.append(value)
i,j=0,0
while i<len(stack1) and j<len(stack2):
    if stack1[i]<stack2[j]:
        merged.append(stack1[i])
        i+=1
    else:
        merged.append(stack2[j])
        j+=1
while i<len(stack1):
    merged.append(stack1[i])
    i+=1
while j<len(stack2):
    merged.append(stack2[j])
    j+=1
print(merged)