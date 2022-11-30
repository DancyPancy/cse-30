# Code by: Jack Wong
# Date: Tue Nov 22 2022
# About: Plot size of input vs time for various sorting algorithms

from timeit import Timer, timeit
from random import choice
from matplotlib import pyplot as plt
import numpy as np


def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items 

def quickSort(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[ first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[ leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[ rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           alist[ leftmark], alist[ rightmark] = alist[ rightmark],alist[ leftmark]       
   alist[ first], alist[ rightmark] = alist[ rightmark], alist[ first]
   return rightmark          

def mergeSort(items):
    print("Splitting ",items)
    if len(items)>1:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        print("Merging ",items)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[ i] <= r[ j]:
                items[ k] = l[ i]
                i += 1
            else:
                items[ k] = r[ j]
                j += 1
            k += 1
        while i < len(l):
            items[ k] = l[ i]
            i, k = i+1, k+1
        while j < len(r):
            items[ k] = r[ j]
            j, k = j+1, k+1


list_ = list(range(0,500))      # list of numbers
d1 = [choice(list_) for i in range(10)]  # random list of size 10
d2 = [choice(list_) for i in range(20)]  # random list of size 20
d3 = [choice(list_) for i in range(50)]  # random list of size 50
d4 = [choice(list_) for i in range(100)]  # random list of size 100
d5 = [choice(list_) for i in range(200)]  # random list of size 200
d6 = [choice(list_) for i in range(500)]  # random list of size 500

# you need to add more lists of different sizes: d3, d4, d5, and d6
data = [d1, d2, d3, d4, d5, d6]  # your input
bub_times = []       # times required to bubble sort input
qui_times = []       # times required to quick sort input
mer_times = []       # times required to merge sort input

for i in data:
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    t = t1.timeit(number=3)
    print("bubblesort ",t, "milliseconds") # for debugging
    bub_times.append(t) # record the time required to sort the input

    t1 = Timer(f"quickSort({i}, {0}, {len(i)-1})", "from __main__ import quickSort")
    t = t1.timeit(number=3)
    print("quicksort ",t, "milliseconds") # for debugging
    qui_times.append(t) # record the time required to sort the input

    t1 = Timer(f"mergeSort({i})", "from __main__ import mergeSort")
    t = t1.timeit(number=3)
    print("mergesort ",t, "milliseconds") # for debugging
    mer_times.append(t) # record the time required to sort the input

# do not forget to plot your data!!!

bub_points = np.array(bub_times)
qui_points = np.array(qui_times)
mer_points = np.array(mer_times)
data_size = [len(i) for i in data]

plt.plot(data_size, bub_points, 'b-')
plt.plot(data_size, qui_points, 'r-')
plt.plot(data_size, mer_points, 'g-')
plt.title('Sorting Algorithms Analysis', fontsize=10)
plt.xlabel('Size of Input', fontsize=8)
plt.ylabel('Time', fontsize=8)
plt.tick_params(axis='both', labelsize=8)
plt.legend(labels = ('Bubble Sort', 'Quick Sort', 'Merge Sort'), loc = 'upper right')
plt.show()
