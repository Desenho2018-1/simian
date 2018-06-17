from simian.physics.bodies import RigidBody
from simian.physics.colliders import BoxCollider
from simian.math.vector import Vec2
from simian.input.keyboard_manager import Keyboard
from simian.sprite import Sprite

import conf


class PongBar(RigidBody):

    def __init__(self, position, control):
        super().__init__(position, 0, BoxCollider(position, (71, 296)), 5)
        self.sprite = Sprite(conf.ASSETS + 'bar.jpg')
        self.keyboard = Keyboard()
        self.control = control

    def update(self, time_elapsed):
        self.position += self.control()*time_elapsed

    def draw(self, graphics):
        self.sprite.set_x(self.position.x)
        self.sprite.set_y(self.position.y)
        graphics.add(self.sprite)
