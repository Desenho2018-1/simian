"""
Module that contain functions to
manage rigid body collisions.
"""

from math import sqrt
from simian.math.vector import Vec2


def detect_collision(body_a, body_b):
    """
    Verify if two rigid bodies
    are colliding.
    """
    # is a box vs box collision
    if hasattr(body_a, 'size') and hasattr(body_b, 'size'):
        return box_vs_box(body_a.collider, body_b.collider)
    else:
        raise NotImplementedError


def resolve_collision(body_a, body_b):
    """
    Resolve the collision between
    two rigid bodies.
    """
    relative_velocity = body_b.velocity - body_a.velocity
    relative_velocity_normal = relative_velocity.dot(normal)

    if relative_velocity_normal > 0:
        e = sqrt(body_a.restitution + body_b.restitution)

        scalar_impulse = -(1 * e) * relative_velocity_normal
        scalar_impulse /= 1/body_a + 1/body_b

        impulse = scalar_impulse * normal
        body_a.velocity -= 1/body_a.mass * impulse
        body_b.velocity += 1/body_b.mass * impulse


def box_vs_box(box_a, box_b):
    """
    Verify colision between two
    box colliders (AABB).
    """
    if box_a.bottom_right.x < box_b.top_left.x or
    box_a.top_left.x > box_b.bottom_right.x:
        return True
    if box_a.bottom_right.y < box_b.top_left.y or
    box_a.top_left.y > box_b.bottom_right.y:
        return True

    return True
