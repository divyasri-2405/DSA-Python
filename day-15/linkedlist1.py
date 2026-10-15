'''#sll linked list insert at begin and delete at end 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
values=list(map(int,input("Enter values: ").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
current=head
print("SLL before deletion")
while current is not None:
    print(current.data,end='->')
    current=current.next
print("Tail")
if head is None:
    print("SLL empty.....")
elif head.next is None:
    head=None
else:
    current=head
    while current.next.next is not None:
        current=current.next
    current.next=None
print("SLL After deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')'''

#sll linked list insert at begin and delete at begin 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
values=list(map(int,input("Enter values: ").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
current=head
print("SLL before deletion")
while current is not None:
    print(current.data,end='->')
    current=current.next
print("Tail")
if head is None:
    print("SLL empty.....")
else:
    head=head.next
print("SLL After deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')