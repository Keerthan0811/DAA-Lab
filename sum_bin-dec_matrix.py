# // Write programs for each of the following and plot the time complexity for varying values of n.
# // Indicate the parameter ‘n’ and the basic operations.
# // a. To find the sum of all the elements of the array.
# // b. To find the binary equivalent of a given decimal number.
# // c. Read a matrix and print those elements of the matrix that are even

import random
import matplotlib.pyplot as plt
import time
import numpy as np


def total(a):
    s=0
    for i in range(len(a)):
        s+=a[i]
    return s

def dec_bin(n):
    b=""
    while n>0:
        b=str(n % 2) + b
        n=n//2
    return b

def matrix(a):
    even=[]
    for i in a:
        for j in i:
            if j%2 == 0:
                even.append(j)
    return even

def graph(x,y,name):
    
    plt.plot(x,y,label=name)
    plt.xlabel("Array size")
    plt.ylabel("Timee(ms)")
    plt.legend(loc="upper right")
    plt.show()
    
def main1():
    x1=[]
    y1=[]
    sarr=[]
    for n in range(10,101,10):
        x1.append(n)
        a=[]
        for i in range(n):
            a.append(random.randint(0,10000))
        
        start=time.time()
        res=total(a)
        end=time.time()
        t=end-start
        
        sarr.append(res)
        y1.append(t)
    print(sarr)
    graph(x1,y1,"Sum of Array")
    
def main2():
    for n in range(1,100,10):
        print(str(n)+"-->"+str(dec_bin(n)))
        
def main3():
    rows = 10
    cols = 10
    m = np.random.randint(1,100,(rows,cols))
    even=matrix(m)
    print(m)
    print(even)
main1()
main2()
main3()
