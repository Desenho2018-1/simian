"""
Colliders classes.
All representations of colliders shapes
used to detect collision between game objects.
"""

from simian.math.vector import Vec2


class BoxCollider(object):
    """
    A box that represents the shape
    of a rigid body, is used to perfofm
    AABB collision detection.
    """
    __slots__ = ['position', 'size', 'top_left', 'bottom_right']

    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.top_left = Vec2(position.x - (size.x/2), position.y + (size.y/2))
        self.bottom_right = Vec2(position.x + (size.x/2), position.y - (size.y/2))
