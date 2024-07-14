# Given a weighted connected graph of N cities, write a C program to find shortest paths from a
# given city to all other cities using Dijkstra's algorithm. Give the trace of this algorithm.
# Dijkstra Algorithm:


visited=[]
dist=[]
def dijkstra(graph,n,source):
    
    for i in range(n):
        visited.append(0)
        dist.append(graph[source][i])
    visited[source]=1
    dist[source]=0
    for ecount in range(n): 
        min=999;
        for i in range(n):
            if(visited[i]==0 and dist[i]<min):
                min=dist[i]
                u=i
        visited[u]=1
        for v in range(n):
            if(visited[v]==0 and dist[u]+graph[u][v]<dist[v]):
                dist[v]=dist[u]+graph[u][v]
                
def main():  
    graph=[ [0,3,999,7,999],
            [3,0,4,2,999],
            [999,4,0,5,6],
            [7,2,5,0,4],
            [999,999,6,4,0]]
    n=len(graph[0])
    source=int(input("enter source node="))
    print(".....weight matrix........")
    for row in graph:
        print(row)
    dijkstra(graph,n,source)
    print("shortest path from source=",source)
    for i in range(n):
        print(source,"------>",i,"====",dist[i])
main() 




# OUTPUT:

# enter source node=0
# .....weight matrix........
# [0, 3, 999, 7, 999]
# [3, 0, 4, 2, 999]
# [999, 4, 0, 5, 6]
# [7, 2, 5, 0, 4]
# [999, 999, 6, 4, 0]
# shortest path from source= 0
# 0 ------> 0 ==== 0
# 0 ------> 1 ==== 3
# 0 ------> 2 ==== 7
# 0 ------> 3 ==== 5
# 0 ------> 4 ==== 9
