# A university is looking for engineering graduates, they need to sort the candidate‘s resume
# based on their ranking. Write a C program to sort the resumes by using heap sort. Determine
# the time required to sort the elements. Plot a graph of the number of elements versus time
# taken. Specify the time efficiency class of this algorithm.

# Heap Sort:


import random
import matplotlib.pyplot as plt
import time
import numpy as np

def heapify(a,n,i):
    large_i=i
    left_i=2*i+1
    right_i=2*i+2
    
    if left_i<n and a[left_i]>a[large_i]:
        large_i=left_i
    if right_i<n and a[right_i]>a[large_i]:
        large_i=right_i
    if large_i != i:
        a[i],a[large_i]=a[large_i],a[i]
        heapify(a,n,large_i)
        
def max_haep(a):
    for i in range((len(a)//2) -1,-1,-1):
        heapify(a,len(a),i)
    print("max heap")
    print(a)

def heapsort(a):
    for i in range(len(a)-1,-1,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,i,0)
        
def graph(x,y,name):
    plt.plot(x,y,label=name)
    plt.xlabel("Array Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc="upper right")
    plt.show

def main():
    x=[]
    y=[]
    for n in range(10,101,10):
        x.append(n)
        a=[]
        for i in range(n):
            a.append(random.randint(0,n))
        
        start=time.time()
        max_haep(a)
        heapsort(a)
        end=time.time()
        t=end-start
        
        print("Sorted")
        print(a)
        y.append(t)
    graph(x,y,"Heap Sort")
    
main()
#  Output:
# Unsorted list
# [1, 12, 9, 5, 6, 10]
# Max Heap Tree
# 12 6 10 5 1 9 
# Sorted list
# [1, 5, 6, 9, 10, 12]

