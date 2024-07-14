# // A library maintains details of N books where every book is assigned a unique ISBN. Develop a
# // program in C to sort the books based on ISBN using merge sort technique. Determine the time
# // required to sort. Repeat the experiment for different values of N and plot a graph of the time taken
# // versus N
# MergeSort-python.txt


import time
from random import randint
import matplotlib.pyplot as plt


def divide(a, low, high):
    if low < high:
        mid = (low + high)//2
        divide(a, low, mid)
        divide(a, mid + 1, high)
        merge(a, low, mid, high)


def merge(a, low, mid, high):
    temp = []
    # Initialize temp array with all zeros and length equal to length of a.
    for i in range(len(a)):
        temp.append(0)

    i = low
    j = mid + 1
    k = low
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = a[j]
        j += 1
        k += 1

    for k in range(low, high + 1):
        a[k] = temp[k]


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
    plt.plot(x, y, label='Merge Sort')
    plt.xlabel("Input Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc='upper right')
    plt.show()
main()
