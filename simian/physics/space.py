"""
Classes that represents position, size
of objects.
"""


class Position:
    """
    A position represents a point in a 2D space.
    Measure unite: pixels
    """

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __call__(self):
        """
        Return a tuple representation of the
        measures to facilitate usage in some contexts.
        """
        return (self.x, self.y)


class Size:
    """
    Size represents how big something is by
    measuring height and width.
    Measure unit: pixels
    """

    def __init__(self, width=None, height=None):
        self.h = height
        self.w = width

    def __call__(self):
        """
        Return a tuple representation of the
        measures to facilitate usage in some contexts.
        """
        return (self.h, self.w)
