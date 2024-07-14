# Given ‘N’ items with their weight and value. Also, a bag is given whose capacity is ‘W’. Write a
# C program based on dynamic programming design technique to find the subset of items that fit
# into the bag and earn maximum profit. Give the trace of this algorithm.
# Knapsack python.txt


def show (w,p,n,m,v):
    print(v)
    profit=v[n][m]
    i=n
    j=m
    while(i>0 and profit>0):
        if v[i][j]!=v[i-1][j]:
            print("item weight=",w[i]," item pofit=",p[i])
            j=j-w[i]
        i-=1
def knapsack(w,p,n,m):
    v = [[0 for x in range(m + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                v[i][j]=0
            elif w[i]>j:
                v[i][j]=v[i-1][j]
            else:
                v[i][j]=max(v[i-1][j],p[i]+v[i-1][j-w[i]])
    show(w,p,n,m,v)
    return v[n][m]
w=[0,2,1,3,2]   
p=[0,12,10,20,15]
n=4
m=5
res=knapsack(w,p,n,m)
print("optimal solution=", res)




# OUTPUT:
# [[0, 0, 0, 0, 0, 0], [0, 0, 12, 12, 12, 12], [0, 10, 12, 22, 22, 22], [0, 10, 12, 22, 30, 32], [0, 10, 15, 25, 30, 37]]
# item weight= 2  item pofit= 15
# item weight= 1  item pofit= 10
# item weight= 2  item pofit= 12
# optimal solution= 37
