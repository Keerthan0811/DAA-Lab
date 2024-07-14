# Consider a network of ‘n’ cities which is represented as a Graph.
# a. Write a ‘C’ program to find the transitive closure of such a network using Warshall’s algorithm.
# b. Write a ‘C’ program to find the shortest paths between all cities using Floyd’s algorithm.
# Note : Give the trace of both algorithms.

# Warshall's python.txt
def trans(a,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                 a[i][j]=a[i][j]or(a[i][k] and a[k][j])
def main():  
    a=[ [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1],
        [1,0,0,0]]
    n=len(a[0])    
    print(".....adjacency matrix........")    
    print(a)
    trans(a,n)
    print("....Transitive clouser matrix....")
    print(a)   
main() 


# OUTPUT:
# .....adjacency matrix........
# [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
# ....Transitive clouser matrix....
# [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]] 
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Floyd's python.txt



def floyd(dist,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                 dist[i][j]=min(dist[i][j],(dist[i][k]+dist[k][j]))
def main():  
    dist=[ [0,999,3,999],
        [2,0,999,999],
        [999,7,0,1],
        [6,999,999,0]]
    n=len(dist[0])    
    print(".....weight matrix........")    
    print(dist)
    floyd(dist,n)
    print("....All pair shortest path....")
    print(dist)   
main() 


# OUTPUT:
# .....weight matrix........
# [[0, 999, 3, 999], [2, 0, 999, 999], [999, 7, 0, 1], [6, 999, 999, 0]]
# ....All pair shortest path....
# [[0, 10, 3, 4], [2, 0, 5, 6], [7, 7, 0, 1], [6, 16, 9, 0]]
