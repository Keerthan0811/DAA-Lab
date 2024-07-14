# A university is looking for engineering graduates, they need to sort the candidate‘s resume
# based on their ranking. Write a C program to sort the resumes by using heap sort. Determine
# the time required to sort the elements. Plot a graph of the number of elements versus time
# taken. Specify the time efficiency class of this algorithm.

# Heap Sort:


def heapify(arr, n, i):
    largest_index = i
    left_index = 2*i + 1
    right_index = 2*i + 2
    if left_index < n and arr[left_index] > arr[largest_index]:
        largest_index = left_index
    if right_index < n and arr[right_index] > arr[largest_index]:
        largest_index = right_index
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index)


def max_heap(arr):
    for i in range(int(len(arr)/2) - 1, -1, -1):
        heapify(arr, len(arr), i)
    print("Max Heap Tree")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def heap_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def main():
    arr = [1, 12, 9, 5, 6, 10]
    print("Unsorted list")
    print(arr)
    max_heap(arr)
    heap_sort(arr)
    print("Sorted list")
    print(arr)   
main()
#  Output:
# Unsorted list
# [1, 12, 9, 5, 6, 10]
# Max Heap Tree
# 12 6 10 5 1 9 
# Sorted list
# [1, 5, 6, 9, 10, 12]

