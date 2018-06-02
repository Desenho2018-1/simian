"""
RigidBody classes.
All objects that react with game physics
should be represented by this classes.
"""

from simian.gameobject.game_object import GameObject
from simian.physics.space import Size, Position


class RigidBody(GameObject):
    """
    A game object that reacts with game physics,
    his body is indeformable and has mass and velocity.
    """

    def __init__(self, position, size, mass, collider=None, velocity=0):
        super.__init__(position.x, position.y, size.h, size.w)
        self.mass = mass
        self.collider = collider if collider else BoxCollider(position, size)
        self.velocity = velocity


class BoxCollider(GameObject):
    """
    A box that represents the bounds
    of a rigid body, is used to perfofm
    collision detection.
    """

    def __init__(self, position, size):
        super.__init__(position.x, position.y, size.h, size.w)
        half_height = size.h/2
        half_width = size.w/2
        self.top_left_corner = Position(position.x - half_width,
                                        position.y + half_height)
        self.bottom_right_corner = Position(position.x + half_width
                                            position.y - half_height)
