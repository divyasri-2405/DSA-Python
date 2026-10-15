'''#reverse a SLL
#insert at end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
values=list(map(int,input("Enter values: ").split()))
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
    else:
        current=head
        while current.next is not None:
            current=current.next
        current.next=newnode
#reversal
previous=None
current=head
while current is not None:
    nextnode=current.next
    current.next=previous
    previous=current 
    current=nextnode
head=previous
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print("Tail")'''

#cycle detection
#detect a cycle in the sll
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("Enter values: ").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
for i in range(len(nodes)-1):
    nodes[i].next=nodes[i+1]
#create a cycle with position
cycleposition=int(input("Enter position to connect the last node with: "))
nodes[-1].next=nodes[cycleposition]
#detect the cycle
x=head=nodes[0]
y=head
while y is not None and y.next is not None:
    x=x.next
    y=y.next.next
    if x==y:
        print('Cycle detected...')
        #find the starting node of the cycle
        x=head
        while x!=y:
            x=x.next
            y=y.next
        cyclestart=x
        current=cyclestart
        while True:
            print(current.data,end='->')
            current=current.next
            if current==cyclestart:
                print(current.data)
                break
        break
else:
    print('no cycle detected')