from simian.physics.bodies import RigidBody
from simian.physics.colliders import BoxCollider
from simian.math.vector import Vec2
from simian.input.keyboard_manager import Keyboard
from simian.sprite.sprite import Sprite

import conf


class Ground(RigidBody):

    def __init__(self, position):
        super().__init__(position, 0, BoxCollider(position, (296, 71)), 5)
        self.sprite = Sprite(conf.ASSETS + 'bar2.jpg')
        self.keyboard = Keyboard()

    def update(self, time_elapsed):
        self.position += self.velocity*time_elapsed

    def draw(self, graphics):
        self.sprite.set_x(self.position.x)
        self.sprite.set_y(self.position.y)

        graphics.add(self.sprite)
