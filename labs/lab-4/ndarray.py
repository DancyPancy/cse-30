import numpy as np


arr = np.array([1, 2, 3, 4, 5])
print(arr)

print(type(arr))     # the data type of the object arr

print(arr.dtype)     # the data type of items in arr

for i in dir(arr):
    print(i)

print(arr.size)

print(arr.sum())

print(arr.shape)