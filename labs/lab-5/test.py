import matplotlib.pyplot as plt
import numpy as np


ax = plt.axes(projection='3d')

# create meshgrid

# parametric equations for cone
X = [[1, 1], [-1, -1]]
Y = [[1, -1], [1, -1]]
Z = [[1, 1], [1, 1]]

# plot and show
ax.contour3D(X, Y, Z, 50)
ax.set_title('Cone')
plt.show()