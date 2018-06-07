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
    edges = body_a.collider.edges
    edges += body_b.collider.edges

    orthogonals = [_orthogonal(e) for e in edges]

    push_vectors = []
    for orthogonal in orthogonals:
        separates, push_vec = _is_separating_axis(orthogonal,
                                                  body_a.collider.vertices,
                                                  body_b.collider.vertices)

        if separates:
            # Collision not detected
            return None
        else:
            push_vectors.append(push_vec)

    # smallest push vector
    minimal_push_vec = min(push_vectors, key=(lambda v: v.dot(v)))

    # assert minimal push vector push body_a away from body_b
    d = _centers_displacement(body_a.collider.vertices,
                              body_b.collider.vertices)

    # if it's the same direction, invert
    if d.dot(minimal_push_vec) > 0:
        minimal_push_vec = -minimal_push_vec

    return minimal_push_vec


def resolve_collision(body_a, body_b, normal):
    """
    Resolve the collision between
    two rigid bodies.
    """
    relative_velocity = body_b.velocity - body_a.velocity
    relative_velocity_normal = relative_velocity.dot(normal)

    if relative_velocity_normal > 0:
        e = sqrt(body_a.restitution + body_b.restitution)

        scalar_impulse = -(1 * e) * relative_velocity_normal
        scalar_impulse /= 1/body_a.mass + 1/body_b.mass

        impulse = normal * scalar_impulse

        body_a.velocity -= impulse * (1/body_a.mass)
        body_b.velocity += impulse * (1/body_b.mass)

    return body_a, body_b


def _centers_displacement(vertices1, vertices2):
    """
    Return the displacement between the geometric center
    of vertices of a polygon and another.
    """
    sum1_x = 0
    sum1_y = 0

    sum2_x = 0
    sum2_y = 0

    for v in vertices1:
        sum1_x += v.x
        sum1_y += v.y

    for v in vertices2:
        sum2_x += v.x
        sum2_y += v.y

    center_1 = Vec2(sum1_x/len(vertices1), sum1_y/len(vertices1))
    center_2 = Vec2(sum2_x/len(vertices2), sum2_y/len(vertices2))

    return center_2 - center_1


def _orthogonal(vector):
    """
    Return a 90 degree clockwise rotation
    of the given vector.
    """
    return Vec2(-vector.y, vector.x)


def _is_separating_axis(orthogonal, vertices1, vertices2):
    """
    Return True and the push vector if orthogonal
    is a separating axis of vertices1 and vertices2.
    Otherwise, return False and None.
    """
    min1, max1 = float('+inf'), float('-inf')
    min2, max2 = float('+inf'), float('-inf')

    for v in vertices1:
        projection = v.dot(orthogonal)

        min1 = min(min1, projection)
        max1 = max(max1, projection)

    for v in vertices2:
        projection = v.dot(orthogonal)

        min2 = min(min2, projection)
        max2 = max(max2, projection)

    if max1 >= min2 and max2 >= min1:
        d = min(max2 - min1, max1 - min2)

        d_over_orthogonal_squared = d / orthogonal.dot(orthogonal) + 1e-10
        push_vec = orthogonal * d_over_orthogonal_squared
        return False, push_vec
    else:
        return True, None
