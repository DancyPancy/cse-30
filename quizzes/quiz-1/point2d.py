
from math import sqrt


class Point2D:

    #constructor
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    #returns string representation of point
    def __str__(self):
        return str((self.x, self.y))

    # distance(self, point) returns a distance between two points 
    # self and point: if one point is (x1, y1) and another is (x2, y2), 
    # then the distance is the square root of (x1-x2)^2 + (y1-y2)^2
    def distance(self, point):
        if type(point) == type(self):
            return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    # __add__(self, point) returns a new Point2D with x = x1 + x2 and 
    # y = y1 + y2, where x1 and x2 and y1 and y2 are x and y coordinates 
    # respectively of two given points (self and point)
    def __add__(self, point):
        return Point2D(self.x + point.x, self.y + point.y)

    # __sub__(self, point) returns a new Point2D with x = x1 - x2 and 
    # y = y1 - y2, where x1 and x2 and y1 and y2 are x and y coordinates 
    # respectively of two given points (self and point)
    def __sub__(self, point):
        return Point2D(self.x - point.x, self.y - point.y)

    # __mul__(self, scalar) returns a new Point2D with x = x1 * scalar and 
    # y = y1 * scalar, where x1 and y1 are x and y coordinates of a given point (self)
    def __mul__(self, scalar):
        return Point2D(self.x * scalar, self.y * scalar)

    def __eq__(self, point):
        return True if abs(self.x-point.x) < 0.000001 and abs(self.y-point.y) < 0.000001 else False

if __name__ == '__main__':
    A = Point2D(1, 1)
    B = Point2D(0, 0)
    C = Point2D(0, 3)
    D = Point2D(0, 1)
    print(A)             # should print (1.0, 1.0)
    assert A == Point2D(1,1)
    print(A + B)         # should print (1.0, 1.0)
    assert A + B == Point2D(1,1)
    print(A - C)         # should print (1.0, -2.0)
    assert A - C == Point2D(1, -2)
    print(A * 3)         # should print (3.0, 3.0)
    assert A * 3 == Point2D(3, 3)
    print(D.distance(C)) # should print 2.0
    assert D.distance(C) == 2.0
    print(B == A)        # should print False
    assert B != A
    print(B == A * 0)    # should print True
    assert B == A * 0
    print('Everything works correctly!')