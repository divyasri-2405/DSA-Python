'''#doubly linked list
#insert at begin
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes: "))
for i in range(n):
    data=int(input("Enter value: "))
    newnode=node(data)
    newnode.next=head
    if head is not None:
        head.prev=newnode
    head=newnode
print('Doubly linked list: ')
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print('tail')

#insert at end
class node:
    def __init__(self,data):
        self.data=data
        self.previous=None
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
print('tail')'''

#insert at end delete at begin
class node:
    def __init__(self,data):
        self.data=data
        self.previous=None
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
