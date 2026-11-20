'''#create a graph and connecting the vertices
#unweighted graph
n=int(input("Enter number of vertices: "))
e=int(input("Enter number of edges: "))
vertices=input("Enter vertices: ").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(e):
    u,v=input("Enter edges: ").split()
    graph[u].append(v)
    graph[v].append(u)
for v in graph:
    print(v,'->',graph[v])'''

#create a graph and connecting the vertices and add weights
#weighted graph
n=int(input("Enter number of vertices: "))
e=int(input("Enter number of edges: "))
vertices=input("Enter vertices: ").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(e):
    u,v,w=input("Enter edges: ").split()
    w=int(w)
    graph[u].append((v,w))
    graph[v].append((u,w))
for v in graph:
    print(v,'->',graph[v])

