"""
Vectors representations in cartesian
coordinate system.
"""

from math import sqrt, pow


class Vec2:
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

    # Generic operator handlers
    def _o2(self, other, f):
        "Any two-operator operation where the left operand is a Vec2"
        if isinstance(other, Vec2):
            return Vec2(f(self.x, other.x),
                        f(self.y, other.y))
        elif (hasattr(other, "__getitem__")):
            return Vec2(f(self.x, other[0]),
                        f(self.y, other[1]))
        else:
            return Vec2(f(self.x, other),
                        f(self.y, other))

    def _r_o2(self, other, f):
        "Any two-operator operation where the right operand is a Vec2"
        if (hasattr(other, "__getitem__")):
            return Vec2(f(other[0], self.x),
                        f(other[1], self.y))
        else:
            return Vec2(f(other, self.x),
                        f(other, self.y))

    def _io(self, other, f):
        "inplace operator"
        if (hasattr(other, "__getitem__")):
            self.x = f(self.x, other[0])
            self.y = f(self.y, other[1])
        else:
            self.x = f(self.x, other)
            self.y = f(self.y, other)
        return self

    # Addition
    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif hasattr(other, "__getitem__"):
            return Vec2(self.x + other[0], self.y + other[1])
        else:
            return Vec2(self.x + other, self.y + other)
    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, Vec2):
            self.x += other.x
            self.y += other.y
        elif hasattr(other, "__getitem__"):
            self.x += other[0]
            self.y += other[1]
        else:
            self.x += other
            self.y += other
        return self

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        elif (hasattr(other, "__getitem__")):
            return Vec2(self.x - other[0], self.y - other[1])
        else:
            return Vec2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(other.x - self.x, other.y - self.y)
        if (hasattr(other, "__getitem__")):
            return Vec2(other[0] - self.x, other[1] - self.y)
        else:
            return Vec2(other - self.x, other - self.y)

    def __isub__(self, other):
        if isinstance(other, Vec2):
            self.x -= other.x
            self.y -= other.y
        elif (hasattr(other, "__getitem__")):
            self.x -= other[0]
            self.y -= other[1]
        else:
            self.x -= other
            self.y -= other
        return self

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        if (hasattr(other, "__getitem__")):
            return Vec2(self.x * other[0], self.y * other[1])
        else:
            return Vec2(self.x * other, self.y * other)
    
    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x*other.x, self.y*other.y)
        if (hasattr(other, "__getitem__")):
            return Vec2(self.x*other[0], self.y*other[1])
        else:
            return Vec2(self.x*other, self.y*other)
    __rmul__ = __mul__

    def __imul__(self, other):
        if isinstance(other, Vec2):
            self.x *= other.x
            self.y *= other.y
        elif (hasattr(other, "__getitem__")):
            self.x *= other[0]
            self.y *= other[1]
        else:
            self.x *= other
            self.y *= other
        return self

    # Division
    def __div__(self, other):
        return self._o2(other, operator.div)

    def __rdiv__(self, other):
        return self._r_o2(other, operator.div)

    def __idiv__(self, other):
        return self._io(other, operator.div)

    def __floordiv__(self, other):
        return self._o2(other, operator.floordiv)

    def __rfloordiv__(self, other):
        return self._r_o2(other, operator.floordiv)

    def __ifloordiv__(self, other):
        return self._io(other, operator.floordiv)

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def __rtruediv__(self, other):
        return self._r_o2(other, other.__truediv__)

    def __itruediv__(self, other):
        return self._io(other, operator.floordiv)

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __str__(self):
        return f'Vec2({self.x, self.y})'

    def dot(self, other):
        return float(self.x * other[0] + self.y * other[1])
