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
        new_position = self.control()*time_elapsed
        self.position += new_position

        height = self.sprite.height
        middle_height = self.sprite.height / 2

        if new_position.y < 0 and self.position.y < 3 + middle_height:
            self.position -= new_position
        elif new_position.y > 0 and self.position.y + height > 597 + middle_height:
            self.position -= new_position
        else:
            pass

    def draw(self, graphics):
        self.sprite.draw(graphics, self.position.x, self.position.y)
