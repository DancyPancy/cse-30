import numpy as np

# linear system: Ax = b
# x + 2y = 1
# 3x + 5y = 2
A = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print(x)

print(np.dot(A,x))

print(np.allclose(np.dot(A, x), b))