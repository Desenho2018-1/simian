"""
Vectors representations in cartesian
coordinate system.
"""

from math import sqrt, pow


class Vec2(object):
    """
    A vector with 2 dimensions.
    """

    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        """
        Length or magnitude of a 2D vector
        computed using pythagorean theorem.
        """
        return sqrt(pow(self.x, 2)+pow(self.y, 2))

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError(f'Invalid subscript {str(key)} to Vec2')

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif hasattr(other, "__getitem__"):
            return Vec2(self.x + other[0], self.y + other[1])
        else:
            return Vec2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        elif hasattr(other, "__getitem__"):
            return Vec2(self.x - other[0], self.y - other[1])
        else:
            return Vec2(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        if (hasattr(other, "__getitem__")):
            return Vec2(self.x * other[0], self.y * other[1])
        else:
            return Vec2(self.x * other, self.y * other)

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __str__(self):
        return f'Vec2({self.x, self.y})'

    def dot(self, other):
        return float(self.x * other[0] + self.y * other[1])
