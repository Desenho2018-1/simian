"""
Classes that represents a manifold.
An object that contains information about
a collision between two objects.
"""


class Manifold:
    """
    A manifold representation that gives
    information about collision of two objects.
    """
    def __init__(self, obj_a, obj_b, penetration, normal):
        self.obj_a = obj_a
        self.obj_b = obj_b
        self.penetration = penetration
        self.normal = normal
