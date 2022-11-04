import numpy as np

A = np.linspace(0, 2, 3)
B = np.gradient(2**A, 0.5)
print(B)

C = np.meshgrid(A,B)
print(type(C))

C1, C2 = C
print(C1)

print(C2)

D = np.mgrid[0:3, 1:6:2]
D1, D2 = D
print(D1)

print(D2)

E = np.ogrid[0:3, 1:6:2]
E1, E2 = E
print(E1)
print(E2)