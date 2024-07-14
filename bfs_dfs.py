# Design and develop a program in C to print all the nodes reachable from a given starting
# node in a digraph by using BFS method. Give the trace of this algorithm



visited=[]
def dfs(graph,n,u):
    visited[u]=1
    for v in range(n):
        if visited[v]==0 and graph[u][v]==1:
            dfs(graph,n,v)
    print(u)
   
    
def main():  
    graph=[ [0,1,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0]]
    n=len(graph[0])
    source=0
    for i in range(n):
        visited.append(0)
    print(".....adjacency matrix........")
    for row in graph:
        print(row)
    print(".........DFS Order............")
    dfs(graph,n,source)
main()


# Output:
# .....adjacency matrix........
# [0, 1, 1, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 1, 1, 0, 0]
# [0, 0, 0, 0, 0, 1, 0, 0]
# [0, 0, 0, 0, 0, 0, 1, 0]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 0]
# .........DFS Order............
# 7
# 4
# 5
# 1
# 2
# 6
# 3
# 0







# Branch-First Search (BFS).	

def bfs(graph, n, u):
    visited = [0] * n  # Initialize the visited list inside the function
    queue = []  # Initialize the queue inside the function
    count = 0
    queue.append(u)
    visited[u] = 1
    while queue:
        u = queue.pop(0)
        count += 1
        print(u)
        for v in range(n):
            if not visited[v] and graph[u][v]:
                queue.append(v)
                visited[v] = 1

def main():
    graph = [
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    n = len(graph)
    source = 0

    print("Adjacency Matrix")
    for row in graph:
        print(row)

    print("BFS Order")
    bfs(graph, n, source)

main()


# Adjacency Matrix
# [0, 1, 1, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 1, 1, 0, 0]
# [0, 0, 0, 0, 0, 1, 0, 0]
# [0, 0, 0, 0, 0, 0, 1, 0]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 0]
# BFS Order
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
