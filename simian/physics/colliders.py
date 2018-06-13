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
    __slots__ = ['_position', '_size', 'vertices', 'edges']

    def __init__(self, position, size):
        self._position = position
        self._size = size
        self.vertices = self._get_vertices()
        self.edges = self._get_edges()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_pos):
        self._position = new_pos
        self.vertices = self._get_vertices()
        self.edges = self._get_edges()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size
        self.vertices = self._get_vertices()
        self.edges = self._get_edges()

    def _get_vertices(self):
        """
        Return a list with all vertices
        ordered in counterclockwise direction.
        """
        half_width = self.size[0] / 2
        half_height = self.size[1] / 2

        v1 = Vec2(self.position[0] - half_width, self.position[1] + half_height)
        v2 = Vec2(self.position[0] - half_width, self.position[1] - half_height)
        v3 = Vec2(self.position[0] + half_width, self.position[1] - half_height)
        v4 = Vec2(self.position[0] + half_width, self.position[1] + half_height)

        return [v1, v2, v3, v4]

    def _get_edges(self):
        """
        Return the vectors that represent
        all edges of the box collider with
        the given vertices.
        """
        edges = []
        N = len(self.vertices)

        for i in range(N):
            edge = self.vertices[(i + 1) % N] - self.vertices[i]
            edges.append(edge)

        return edges
