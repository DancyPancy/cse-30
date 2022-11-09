import numpy as np
import matplotlib.pyplot as plt

def cylinder(r, h):
    ax = plt.axes(projection='3d')

    t = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, h, 100)

    T, Z = np.meshgrid(t, z)

    X = r * np.cos(T)
    Y = r * np.sin(T) 

    ax.contour3D(X, Y, Z, 50)
    ax.set_title('Cylinder')
    plt.show()

if __name__ == '__main__':
    cylinder(1, 2)
    cylinder(2, 10)