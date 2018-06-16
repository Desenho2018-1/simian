"""
Bodies classes.
All objects that react with game physics
should be represented by this classes.
"""

from simian.object import GameObject
from simian.math.vector import Vec2


class RigidBody(GameObject):
    """
    A game object that reacts with game physics,
    his body is not deformable and has mass, velocity,
    a force applied at a point of his body and
    a restitution coefficient.
    """
    __slots__ = ['mass', 'velocity', 'restitution', 'collider']

    def __init__(self, position, mass, collider, restitution=0,
                 velocity=None, force=None):
        super().__init__(position[0], position[1])
        self.mass = mass
        self.collider = collider
        self.restitution = restitution
        self.velocity = velocity if velocity is not None else Vec2(0, 0)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_pos):
        self._position = new_pos
        self.collider.position = new_pos

    def apply_impulse(self, impulse):
        """
        Apply a given impulse to his body.
        """
        self.velocity += impulse / self.mass
