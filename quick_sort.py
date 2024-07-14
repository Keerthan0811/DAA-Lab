# Consider a list of ‘n’ files numbered using ID’s. Write a C program to sort files based on its ID
# using Quick sort. Determine the time required to sort the files. Plot a graph of number of IDs
# versus time taken
# QuickSort-Python.txt


import time
from random import randint
def divide(a, low, high):
    if low < high:
        j=part(a,low,high)
        divide(a, low, j-1)
        divide(a, j+ 1, high)
      
def part(a, low, high):
    pivot=low
    i=low+1;
    j=high
    while(i<=j):
        while(a[i]<=a[pivot] and i<high):
            i+=1
        while(a[j]>a[pivot]):
            j-=1
        if(i<j):
            a[i],a[j]=a[j],a[i]
    a[pivot],a[j]=a[j],a[pivot]
    return j
  
def main():
    x = []
    y = []
    for n in range(10, 101, 10):
        x.append(n)
        a = []
        for i in range(n):
            a.append(randint(1, n))

        start = time.time()
        divide(a, 0, len(a) - 1)
        end = time.time()
        elapsed = end - start
        y.append(elapsed)
        print("\n-----Sorted list----\n")
        print(a)
main()


