# // Write programs for each of the following and plot the time complexity for varying values of n.
# // Indicate the parameter ‘n’ and the basic operations.
# // a. To find the sum of all the elements of the array.
# // b. To find the binary equivalent of a given decimal number.
# // c. Read a matrix and print those elements of the matrix that are even

# sum 
import matplotlib.pyplot as plt
import time

x=[]
y = []
for n in range(10, 101, 10):
    x.append(n)
    xn=len(x)
    sum=0
    
    start = time.time()
    for i in range(xn):
        sum=sum+x[i]
    end = time.time()
    
    elapsed = end - start
    y.append(elapsed)
    print("\nsum:",sum)
plt.plot(x, y, label='Quick sort')
plt.xlabel("Input Size")
plt.ylabel("Time(ms)")
plt.legend(loc='upper right')
plt.show()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# binary
import matplotlib.pyplot as plt
import time
def binary(n):
    binary_num = ""
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num

def main():
    x=[]
    y = []
    for n in range(10, 101, 10):
        x.append(n)
        xn=len(x)
        bin=""
    
        start = time.time()
        for i in range(n):
            bin=binary(n)
        end = time.time()
    
        elapsed = end - start
        y.append(elapsed)
        print("\nbinary:",bin)
    plt.plot(x, y, label='Dec-Bin')
    plt.xlabel("Input Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc='upper right')
    plt.show()
main()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# matrix
import time
import random
import matplotlib.pyplot as plt

def print_even_elements(matrix):
    even_elements = []
    for row in matrix:
        for elem in row:
            if elem % 2 == 0:
                even_elements.append(elem)
    return even_elements

def plot_time_complexity():
    n= list(range(1, 1001, 100))
    times = []
    for i in n:
        matrix = [[random.randint(1, 100) for _ in range(i)] for _ in range(i)]
        start_time = time.time()
        print_even_elements(matrix)
        end_time = time.time()
        times.append(end_time - start_time)
    plt.plot(n, times)
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Printing Even Elements in a Matrix')
    plt.show()

plot_time_complexity()
