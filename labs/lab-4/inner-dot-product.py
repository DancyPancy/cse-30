import numpy as np

# vector dot product
a = np.array([1,2,3])
b = np.arange(0,3)
print('a:\n', a, '\nb:\n', b)
c = np.dot(a, b)
print('c:\n', c)

# matrix dot product
x, y = np.meshgrid(a, b)
print('x:\n',x,'\ny:\n',y)
z = np.dot(x,y)
print('z:\n', z)

# vector cross product
i = np.array([1,0,0])
j = np.array([0,1,0])
k = np.cross(i,j)
print(k)

x = [1,2,0]
y = [3,6,0]
z = np.cross(x,y)
print(z)

a = [1,2,1]
b = [2,0,3]
c = np.cross(a,b)
print(c)