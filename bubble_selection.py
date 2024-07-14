# // The goods packages in a supermarket are assigned an integer label. Write a C program to sort the
# // set of goods packages based on label identifier using Bubble Sort/Selection Sort and determine
# // the time required to sort. Plot a graph of number of label identifiers versus time taken.

# SelectionSort python.txt
import sys
import matplotlib.pyplot as plt
import time
from random import randint

def Selectionsort(a,n):
    for i in range (n-1):
        min=i
        for j in range (i+1,n):
            if(a[j]<a[min]):
                min=j

        a[i],a[min]=a[min],a[i]

def main():
    x=[]
    y=[]
    for n in range(10,101,10):
        a = []
        x.append(n)
        for i in range(n):
            a.append(randint(1,n))
        print('------------------------------\n')
        print (a)
        start=time.time()
        Selectionsort(a,n)
        end=time.time()
        print(a)
        gaptime=end-start
        y.append(gaptime)
    plt.plot(x,y,c='red')
    plt.scatter(x,y,c='green')
    plt.bar(x,y)
    plt.xlabel("N-size")
    plt.ylabel("Time(ms)")
    plt.show()
main()
