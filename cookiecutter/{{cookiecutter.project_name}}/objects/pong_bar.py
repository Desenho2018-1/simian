from simian.physics.bodies import RigidBody
from simian.physics.colliders import BoxCollider
from simian.math.vector import Vec2
from simian.input.keyboard_manager import Keyboard
from simian.sprite.sprite import Sprite

import conf


class PongBar(RigidBody):

    def __init__(self, position):
        super().__init__(position, 100, BoxCollider(position, (50, 300)))
        self.sprite = Sprite(conf.ASSETS + 'bar.jpg')
        self.keyboard = Keyboard()

    def update(self, time_elapsed):
        if(self.keyboard.is_key_pressed(Keyboard.DOWN)):
            self.position += Vec2(0, 20)
        if(self.keyboard.is_key_pressed(Keyboard.UP)):
            self.position += Vec2(0, -20)

    def draw(self, graphics):
        self.sprite.set_x(self.position.x)
        self.sprite.set_y(self.position.y)
        graphics.add(self.sprite)
