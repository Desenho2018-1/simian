"""
GameObject classes.
All objects in a game should be represented by this classes.
"""


class Position:
    """
    A position represents a point in a 2D space.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Size:
    """
    Size represents how big something is by measuring height and width.
    """

    def __init__(self, height=None, width=None):
        self.h = height
        self.w = width


class GameObject:
    """
    The base GameObject of Simian Engine. A game object has
    a position that defines his cordinates (x, y) in a 2D space,
    also has a size (height, width) that defines how big the object is.
    """

    def __init__(self, x=None, y=None, height=None, width=None):
        self.pos = Position(x, y)
        self.size = Size(height, width)

    def clone(self):
        """
        Clone the current object for better creation management.
        """
        return self
