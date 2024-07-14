# // Given an array of elements ‘n’, search for an element in this array. Indicate the number of
# // comparisons for varying values of n. The element to be searched can be the first element, last
# // element, element other than first and last. Assume the number of elements ‘n’, derive a formula
# // to indicate the number of comparisons done.
# // Use the following search techniques
# // 1. Linear Search
# // 2. Binary search

# Linear search
import time
import matplotlib.pyplot as plt
def linear(a,k):
    n=len(a)
    for i in range(0,n):
        if a[i]==k:
            return k
    return -9999
        
        
def main():
    x = []
    y = []
    for n in range(10, 101, 10):
        x.append(n)
        a = []
        for i in range(n):
            a.append(randint(1, n))

        start = time.time()
        res=linear(a,randint(1,10))
        end = time.time()
        elapsed = end - start
        y.append(elapsed)
        print(res)
        print(a)
    plt.plot(x, y, label='Linear search')
    plt.xlabel("Input Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc='upper right')
    plt.show()
main()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# binary search
import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1



def main():
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    times = []

    for i in sizes:
        arr = sorted([random.randint(1, 10000) for _ in range(i)])
        k = random.choice(arr)  # Choose a random element to search for
        start_time = time.time()
        binary_search(arr, k)
        end_time = time.time()
        elapsed=start_time-end_time
        times.append(elapsed)
        print(f"Searched {i} labels in {elapsed:.6f} seconds")

    plt.plot(sizes, times, marker='o')
    plt.xlabel('Number of Label Identifiers')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Binary Search Time Complexity')
    plt.grid(True)
    plt.show()
main()
