from simian.physics.bodies import RigidBody
from simian.physics.colliders import BoxCollider
from simian.math.vector import Vec2
from simian.sprite import Sprite
from simian.input.keyboard_manager import Keyboard

import conf


class Ball(RigidBody):

    def __init__(self, position):
        super().__init__(position, 1, BoxCollider(position, (27, 26)), 1.2)
        self.keyboard = Keyboard()
        self.sprite = Sprite(conf.ASSETS + 'ball.png')
        self.moving = False

    def update(self, time_elapsed):
        if(self.keyboard.is_key_pressed(Keyboard.RETURN)):
            self.velocity = Vec2(-70, 70)
            self.moving = True

        self.position += self.velocity*time_elapsed

    def draw(self, graphics):
        self.sprite.x = self.position.x
        self.sprite.y = self.position.y
        graphics.add(self.sprite)
