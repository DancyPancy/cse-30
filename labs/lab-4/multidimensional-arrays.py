import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr2D = np.array([[1,2,3], [4,5,6]])
print(arr2D)

arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3D)

print(arr.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

arr5D = np.array([1, 2, 3, 4], ndmin=5)
print(arr5D)

print(arr5D.ndim)

nested_list = [[1,2,3],[4,5,6]]
print(nested_list[ 1][ 2])

print(arr2D[1,2])

arr_to2D = arr.reshape(5,1)
print(arr_to2D)

print(arr_to2D.reshape(-1))

for k in np.nditer(arr3D):
    print(k)

filter_ = [True, False, True, False, True]
print(arr[filter_ ])

print( arr [ arr > 2 ])

print( arr [ arr % 2 == 0 ])