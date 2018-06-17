"""
Module that contain functions to
manage rigid body collisions.
"""

from math import sqrt
from simian.math.manifold import Manifold
from simian.math.vector import Vec2

MAX_VELOCITY = 3000
MIN_VELOCITY = -3000


class CollisionManager:

    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)
        self._game_objects = observer

    def detach(self, observer):
        observer._subjet = None
        self._observers.discard(observer)
        self._game_objects = []

    def _notify(self):
        for observer in self._observers:
            observer.update(self._game_objects)

    def manage_collision(self):
        index = 1
        for i in range(len(self._game_objects)):
            for j in range(index, len(self._game_objects)):
                manifold = self._detect_collision(
                    self._game_objects[i], self._game_objects[j])
                if manifold:
                    self._game_objects[i] = self._resolve_collision(manifold)[0]
                    self._game_objects[j] = self._resolve_collision(manifold)[1]
                    self._notify()
            index += 1

    def _detect_collision(self, body_a, body_b):
        """
        Verify if two rigid bodies
        are colliding.
        """
        A = body_a.collider
        B = body_b.collider

        # vector from a to b
        n = A.position - B.position

        A_extent = (A.max.x - A.min.x) / 2
        B_extent = (B.max.x - B.min.x) / 2

        x_overlap = A_extent + B_extent - abs(n.x)

        if x_overlap > 0:
            A_extent = (A.max.y - A.min.y) / 2
            B_extent = (B.max.y - B.min.y) / 2

            y_overlap = A_extent + B_extent - abs(n.y)

            # SAT test on y axis
            if y_overlap > 0:
                if x_overlap < y_overlap:
                    if n.x < 0:
                        normal = Vec2(1, 0)
                    else:
                        normal = Vec2(-1, 0)
                    penetration = x_overlap
                    return Manifold(body_a, body_b, penetration, normal)
                else:
                    if n.y < 0:
                        normal = Vec2(0, 1)
                    else:
                        normal = Vec2(0, -1)
                    penetration = y_overlap
                    return Manifold(body_a, body_b, penetration, normal)

    def _resolve_collision(self, manifold):
        """
        Resolve the collision between
        two rigid bodies.
        """
        A = manifold.obj_a
        B = manifold.obj_b

        # relative velocity
        rv = B.velocity - A.velocity

        # relative velocity in terms of normal direction
        rv_n = rv.dot(manifold.normal)

        # resolve only if velocities are not separating
        if rv_n <= 0:
            A_inv_mass = 0 if A.mass == 0 else 1/A.mass
            B_inv_mass = 0 if B.mass == 0 else 1/B.mass

            # calculate restitution
            e = min(A.restitution, B.restitution)

            # calculate impulse scalar
            j = -(1 + e) * rv_n

            j /= A_inv_mass + B_inv_mass

            # apply impulse
            impulse = j * manifold.normal

            A.velocity -= A_inv_mass * impulse
            B.velocity += B_inv_mass * impulse

            A.velocity.x = MAX_VELOCITY if A.velocity.x > MAX_VELOCITY else A.velocity.x
            A.velocity.x = MIN_VELOCITY if A.velocity.x < MIN_VELOCITY else A.velocity.x
            A.velocity.y = MAX_VELOCITY if A.velocity.y > MAX_VELOCITY else A.velocity.y
            A.velocity.y = MIN_VELOCITY if A.velocity.y < MIN_VELOCITY else A.velocity.y

            B.velocity.x = MAX_VELOCITY if B.velocity.x > MAX_VELOCITY else B.velocity.x
            B.velocity.x = MIN_VELOCITY if B.velocity.x < MIN_VELOCITY else B.velocity.x

            B.velocity.y = MAX_VELOCITY if B.velocity.y > MAX_VELOCITY else B.velocity.y
            B.velocity.y = MIN_VELOCITY if B.velocity.y < MIN_VELOCITY else B.velocity.y

        return A, B
