"""
Colliders classes.
All representations of colliders shapes
used to detect collision between game objects.
"""

from simian.math.vector import Vec2


class BoxCollider:
    """
    A box that represents the shape
    of a rigid body, is used to perform
    AABB collision detection.
    """
    __slots__ = ['_position', '_size', 'max', 'min']

    def __init__(self, position, size):
        self._position = Vec2(position[0], position[1])
        self._size = size
        self.max, self.min = self._get_max_min()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_pos):
        self._position = new_pos
        self.max, self.min = self._get_max_min()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size
        self.max, self.min = self._get_max_min()

    def _get_max_min(self):
        return (Vec2(self.position.x + self.size[0]/2,
                     self.position.y + self.size[1]/2),
                Vec2(self.position.x - self.size[0]/2,
                     self.position.y - self.size[1]/2))
