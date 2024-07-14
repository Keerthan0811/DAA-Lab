# Consider a list of ‘n’ files numbered using ID’s. Write a C program to sort files based on its ID
# using Quick sort. Determine the time required to sort the files. Plot a graph of number of IDs
# versus time taken
# QuickSort-Python.txt


import time
from random import randint
import matplotlib.pyplot as plt

def divide(a, low, high):
    if low < high:
        j = part(a, low, high)
        divide(a, low, j - 1)
        divide(a, j + 1, high)

def part(a, low, high):
    pivot = a[low]
    i = low + 1
    j = high
    while True:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            break
    a[low], a[j] = a[j], a[low]
    return j

def main():
    x = []
    y = []
    for n in range(100, 1100, 100): 
        x.append(n)
        a = [randint(1, 10000) for _ in range(n)]

        start = time.time()
        divide(a, 0, len(a) - 1)
        end = time.time()
        elapsed = end - start
        y.append(elapsed)
        print(f"\n-----Sorted list of size {n}----\n")
        print(a) 

    plt.plot(x, y, label='Quick sort')
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.legend(loc='upper left')
    plt.show()

main()



