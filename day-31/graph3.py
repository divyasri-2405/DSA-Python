'''#DFS-Depth first search
n=int(input("Enter number of nodes: "))
nodes=input("Enter nodes: ").split()
graph={}
for node in nodes:
    graph[node]=input(f"Enter neighbors of {node}: ").split()
start=input("Enter starting node: ")
visited=set()
def dfs(node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for adj in graph[node]:
            dfs(adj)
dfs(start)'''

#DFS-Depth first search with backtracking
n=int(input("Enter number of nodes: "))
nodes=input("Enter nodes: ").split()
graph={}
for node in nodes:
    graph[node]=input(f"Enter neighbors of {node}: ").split()
visited=set()
def dfs(node):
    print(node,end=' ')
    visited.add(node)
    for adj in graph[node]:
            if adj not in visited:
                 dfs(adj)
    print("backtracking from",node) #backtracking step
start=input("Enter starting node: ")
dfs(start)