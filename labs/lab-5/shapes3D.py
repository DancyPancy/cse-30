import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d




ax = plt.axes(projection='3d')    # create a 3D Cartesian coordinate system

x = [1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1]
y = [1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1]
z = [1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1]

ax.plot3D(x, y, z, 'lightblue')
ax.set_title('Cube')
plt.show()                 