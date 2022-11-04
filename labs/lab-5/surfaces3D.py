import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


def hyperbolic_paraboloid():
    ax = plt.axes(projection='3d')
    x = np.linspace(-1, 1, 30)
    y = np.linspace(-1, 1, 30) 
    X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Yprn
    a, b = 1, 1
    Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z

    # plot and show
    ax.contour3D(X, Y, Z, 50)
    ax.set_title('Hyperbolic Paraboloid')
    plt.show()  


def elliptic_paraboloid():
    ax = plt.axes(projection='3d')

    # create 2d meshgrid (plane)
    x = np.linspace(-1, 1, 30)
    y = np.linspace(-1, 1, 30)
    X, Y = np.meshgrid(x, y)

    # equation of z-height
    a, b = 1, 1
    Z = (a * X**2) + (b * Y**2)

    # plot and show
    ax.contour3D(X, Y, Z, 50)
    ax.set_title('Elliptic Paraboloid')
    plt.show()


def hyperbolic_hyperboloid():
    ax = plt.axes(projection='3d')

    # create parametric meshgrid
    t = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(-1, 1, 30)
    T, V = np.meshgrid(t, v)

    # parametric equations for hyperboloid
    a, b, c = 1, 1, 1
    X = a*np.cosh(V)*np.cos(T)
    Y = b*np.cosh(V)*np.sin(T)
    Z = c*np.sinh(V)

    # plot and show
    ax.contour3D(X, Y, Z, 50)
    ax.set_title('Hyperbolic Hyperboloid')
    plt.show()


def elliptic_hyperboloid():
    ax = plt.axes(projection='3d')

    # create parametric meshgrid
    t = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(-2, 2, 30)
    T, V = np.meshgrid(t, v)
    a, b = 1, 1

    # Top sheet coordinates
    X = a*np.sinh(V)*np.cos(T)
    Y = a*np.sinh(V)*np.sin(T)
    Z = b*np.cosh(V)

    # Bottom sheet coordinates
    X2 = -a*np.sinh(V)*np.cos(T)
    Y2 = -a*np.sinh(V)*np.sin(T)
    Z2 = -b*np.cosh(V)

    # plot and show
    ax.contour3D(X, Y, Z, 50)
    ax.contour3D(X2, Y2, Z2, 50)
    ax.set_title('Elliptic Hyperboloid')
    plt.show()


def sphere():
    ax = plt.axes(projection='3d')

    # create parametric meshgrid
    t = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    T, V = np.meshgrid(t, v)
    a, b, c = 1, 1, 1

    # parametric equations for sphere
    X = a*np.cos(T)*np.sin(V)
    Y = b*np.sin(T)*np.sin(V)
    Z = c*np.cos(V)

    # plot and show
    ax.contour3D(X, Y, Z, 50)
    ax.set_title('Sphere')
    plt.show()


def cone():
    ax = plt.axes(projection='3d')

    # create meshgrid
    h = 1
    r = 1
    v = np.linspace(0, h, 30)
    t = np.linspace(0, 2*np.pi, 30)
    V, T = np.meshgrid(v, t)

    # parametric equations for cone
    X = (h - V)/h * r*np.cos(T)
    Y = (h - V)/h * r*np.sin(T)
    Z = V

    # plot and show
    ax.contour3D(X, Y, Z, 50)
    ax.set_title('Cone')
    plt.show()

def square_pyramid():
    ax = plt.axes(projection='3d')

    h = 1
    b = 1
    
    x = [b, b, -b, -b, 0]
    y = [b, -b, b, -b, 0]
    z = [0, 0, 0, 0, h]


    ax.plot_trisurf(x, y, z)
    ax.set_title('Square Pyramid')
    plt.show()


def parallelepiped():
    points = np.array([[-1, -1, -1], [1, -1, -1 ], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1 ], [1, 1, 1], [-1, 1, 1]])

    P = [[2.06498904e-01 , -6.30755443e-07 ,  1.07477548e-03],
    [1.61535574e-06 ,  1.18897198e-01 ,  7.85307721e-06],
    [7.08353661e-02 ,  4.48415767e-06 ,  2.05395893e-01]]

    Z = np.zeros((8,3))
    for i in range(8): Z[i,:] = np.dot(points[i,:],P)
    Z = 10.0*Z

    ax = plt.axes(projection='3d')

    # plot vertices
    ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides' polygons of figure
    verts = [[Z[0],Z[1],Z[2],Z[3]],
    [Z[4],Z[5],Z[6],Z[7]], 
    [Z[0],Z[1],Z[5],Z[4]], 
    [Z[2],Z[3],Z[7],Z[6]], 
    [Z[1],Z[2],Z[6],Z[5]],
    [Z[4],Z[7],Z[3],Z[0]]]

    # plot sides
    ax.add_collection3d(Poly3DCollection(verts, linewidths=1, edgecolors='black'))


    plt.show()
    


if __name__ == '__main__':
    hyperbolic_paraboloid()
    elliptic_paraboloid()
    hyperbolic_hyperboloid()
    elliptic_hyperboloid()
    sphere()
    cone()
    square_pyramid()
    parallelepiped()