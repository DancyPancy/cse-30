# Vector2D class for operating with vector objects
from ast import Div
from locale import normalize
import math

class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001
        
    def __add__(self, other):
        if type(other) == type(self):
            return Vector2D(self.x + other.x, self.y - other.y)
        else:
            raise TypeError('TypeError: unsupported operand type')

    def __sub__(self, other):
        if type(other) == type(self):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            raise TypeError('TypeError: unsupported operand type')

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):
        if type(scalar) == int or type(scalar) == float:
            return Vector2D(self.x * scalar, self.y * scalar)
        else:
            raise TypeError('TypeError: unsupported scalar type')

    def __div__(self, scalar):
        if type(scalar) == int or type(scalar) == float:
            if scalar != 0:
                return Vector2D(self.x / scalar, self.y / scalar)
            else:
                return None
        else:
            raise TypeError('TypeError: unsupported scalar type')

    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    def __ge__(self, other):
        if type(self) == type(other):
            return self.magnitude() >= other.magnitude()
        else:
            raise TypeError('TypeError: unsupported operand type')

    def __lt__(self, other):
        if type(self) == type(other):
            return self.magnitude() <= other.magnitude()
        else:
            raise TypeError('TypeError: unsupported operand type')

    def __hash__(self):
        return id(self)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def magnitudeSquared(self):
        return self.x ** 2 + self.y ** 2

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return self.__div__(mag)
        return None
    
    def dot(self, other):
        if type(self) == type(other):
            return (self.x * other.x) + (self.y * other.y)
        else:
            raise TypeError('TypeError: unsupported operand type')

    def copy(self):
        return Vector2D(self.x, self.y)
            
if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(0.5, -1.5)
    print(f'The sum of {v1} and {v2} is {v1+v2}')
    print(f'The dot product of {v1} and {v2} is {v1.dot(v2)}')