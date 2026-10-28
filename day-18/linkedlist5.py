'''#insert at end delete at begin delete at end
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter the no of values:"))
for i in range(n):
    data=int(input("Enter value: "))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Doubly Linked List: ")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print('tail')
#delete at begin
if head is None:
    print('DLL is empty...')
else:
    head=head.next
    if head is not None:
        head.prev=None
print('Doubly Linked List:')
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print('tail')
#delete at end
if head is None:
    print('DLL is empty...')
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.prev.next=None
print('Doubly Linked List:')
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print('tail')

#insert at end delete at end
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter the no of values:"))
for i in range(n):
    data=int(input("Enter value: "))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Doubly Linked List: ")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print('tail')
#delete at end
if head is None:
    print('DLL is empty...')
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.prev.next=None
print('Doubly Linked List:')
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print('tail')'''


#insert at position
class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None
n = int(input("Enter number of nodes: "))

# Create DLL
for i in range(n):
    data = int(input("Enter value: "))
    newnode = node(data)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp

# Insert at position
data = int(input("Enter value to insert: "))
pos = int(input("Enter position: "))
newnode = node(data)

if pos == 1:
    newnode.next = head
    if head is not None:
        head.prev = newnode
    head = newnode
else:
    temp = head
    for i in range(pos - 2):
        temp = temp.next

    newnode.next = temp.next
    newnode.prev = temp

    if temp.next is not None:
        temp.next.prev = newnode

    temp.next = newnode

# Display DLL
temp = head
while temp is not None:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("Tail")