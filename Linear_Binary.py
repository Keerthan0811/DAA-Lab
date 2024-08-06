# // Given an array of elements ‘n’, search for an element in this array. Indicate the number of
# // comparisons for varying values of n. The element to be searched can be the first element, last
# // element, element other than first and last. Assume the number of elements ‘n’, derive a formula
# // to indicate the number of comparisons done.
# // Use the following search techniques
# // 1. Linear Search
# // 2. Binary search

import time
import matplotlib.pyplot as plt
import random

def linear(a,k):
    for i in range(len(a)):
        if a[i]==k:
            return i
    return -1
    
def binary(a,k):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if k==a[mid]:
            return mid
        elif k>a[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
    
def graph(x,y,str):
    
    plt.plot(x,y,label=str)
    plt.xlabel("Input size")
    plt.ylabel("Time(ms)")
    plt.legend(loc="upper right")
    plt.show()
    
def main():
    x1=[]
    y1=[]
    y2=[]
    lin=[]
    bina=[]
    for n in range(10,101,1):
        x1.append(n)
        a=[]
        for i in range(n):
            a.append(random.randint(0,n))
            
        start=time.time()
        res1=linear(a,random.choice(a))
        end=time.time()
        t=end-start
        y1.append(t)
        lin.append(res1)
        
        a.sort()
        start=time.time()
        res2=binary(a,random.choice(a))
        end=time.time()
        t=end-start
        y2.append(t)
        bina.append(res2)
    
    print(lin)
    print(bina)
    graph(x1,y1,"Linear search")
    graph(x1,y2,"Binary search")
main()
