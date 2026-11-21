#boundary view of a tree
#Boundary view of a tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def is_leaf(node):
    return node.left is None and node.right is None
def left_boundary(root, result):
    node=root.left
    while node:
        if not is_leaf(node):
            result.append(node.data)
        if node.left:
            node=node.left
        else:
            node=node.right
def leaf_nodes(root,result):
    if root is None:
        return
    if is_leaf(root):
        result.append(root.data)
        return
    leaf_nodes(root.left, result)
    leaf_nodes(root.right, result)
def right_boundary(root, result):
    node=root.right
    temp=[]
    while node:
        if not is_leaf(node):
            temp.append(node.data)
        if node.right:
            node=node.right
        else:
            node=node.left
    result.extend(temp[::-1])
def boundary_view(root):
    if root is None:
        return
    result=[]
    if not is_leaf(root):
        result.append(root.data)
    left_boundary(root, result)
    leaf_nodes(root, result)
    right_boundary(root, result)
    print(*result)
values=list(map(int,input("Enter values:").split())) 
root=Node(values[0])
queue=[root]
i=1
while queue and i<len(values):
    node=queue.pop(0)
    if values[i]!=-1:
        node.left=Node(values[i])
        queue.append(node.left)
    i+=1
    if i<len(values) and values[i]!=-1:
        node.right=Node(values[i])
        queue.append(node.right)
    i+=1
boundary_view(root)