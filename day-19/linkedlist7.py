'''#circular linked list traversal delete by value
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("Enter elements: ").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head
x=int(input("Enter value to be deleted: "))
current=head
previous=tail
while True:
    if current.data==x:
        if current==current.next:
            head=None
        elif current==head:
            head=head.next
            tail.next=head
        else:
            previous.next=current.next
        break
    previous=current
    current=current.next
    if current==head:
        print("Value not found")
        break
print("Traversal: ")
if head is None:
    print("CLL empty")
else:
    print("After deletion")
    current=head
    while True:
        print(current.data,end=' ')
        current=current.next
        if current==head:
            break'''

#circular linked list traversal delete by position
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

values = list(map(int, input("Enter elements: ").split()))
head = None
tail = None

for value in values:
    newnode = node(value)
    if head is None:
        head = newnode
        tail = newnode
    else:
        tail.next = newnode
        tail = newnode

tail.next = head

pos = int(input("Enter position to be deleted: "))
current = head
previous = tail

if pos == 1:
    if head == tail:
        head = None
    else:
        head = head.next
        tail.next = head
else:
    for i in range(pos - 1):
        previous = current
        current = current.next

    previous.next = current.next

    if current == tail:
        tail = previous

    tail.next = head

print("Traversal: ")

if head is None:
    print("CLL empty")
else:
    print("After deletion")
    current = head
    while True:
        print(current.data, end=' ')
        current = current.next
        if current == head:
            break
