# Consider an electrical layout where ‘n’ houses are connected by electrical wires. Design a ‘C’
# program using Kruskal’s Algorithm to output a connection with minimum cost. Find its time and
# space complexity.


# Kruskal Algorithm:


p=[]
def kruskal(graph,n):
    for i in range(n):
        p.append(i)
    sum=0
    ecount=0
    while ecount<n-1:
        min=999;
        for i in range(n):
            for j in range(n):
                if(i!=j and graph[i][j]<min):
                    min=graph[i][j]
                    u=i
                    v=j
        if parent(u)!=parent(v):
            print("connect",u,"--->",v,"=",graph[u][v])
            ecount+=1
            p[v]=u
            sum+=graph[u][v]
        graph[u][v]=graph[v][u]=999
    print("MST Total Cost=",sum)    
def parent(x):
    while(x!=p[x]):
        x=p[x]
    return x                
def main():  
    graph=[ [0,30,40,999,999,999],
        [30,0,50,10,999,999],
        [40,50,0,999,20,999],
        [999,10,999,0,60,80],
        [999,999,20,60,0,70],
        [999,999,999,80,70,0]]
    n=len(graph[0])
    print(".....weight matrix........")
    for row in graph:
        print(row)
    print("..........MST Edge.........")
    kruskal(graph,n)
main() 



# OUTPUT:
# .....weight matrix........
# [0, 30, 40, 999, 999, 999]
# [30, 0, 50, 10, 999, 999]
# [40, 50, 0, 999, 20, 999]
# [999, 10, 999, 0, 60, 80]
# [999, 999, 20, 60, 0, 70]
# [999, 999, 999, 80, 70, 0]
# ..........MST Edge.........
# connect 1 ---> 3 = 10
# connect 2 ---> 4 = 20
# connect 0 ---> 1 = 30
# connect 0 ---> 2 = 40
# connect 4 ---> 5 = 70
# MST Total Cost= 170
