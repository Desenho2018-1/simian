from simian.physics.bodies import RigidBody
from simian.physics.colliders import BoxCollider
from simian.sprite import Sprite
from simian.input.keyboard_manager import Keyboard
from simian.math.vector import Vec2
from simian.object import GameObject


class Player(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = Sprite("engineer.jpg")
        self.keyboard = Keyboard()

    def update(self, time_elapsed):
        if(self.keyboard.is_key_pressed(Keyboard.RIGHT)):
            self.velocity = Vec2(100, 0)

        if(self.keyboard.is_key_pressed(Keyboard.LEFT)):
            self.velocity = Vec2(-100, 0)

        if(self.keyboard.is_key_pressed(Keyboard.DOWN)):
            self.velocity = Vec2(0, 100)

        if(self.keyboard.is_key_pressed(Keyboard.UP)):
            self.velocity = Vec2(0, -100)

    def draw(self, graphics):
        self.sprite.set_x(self.position.x)
        self.sprite.set_y(self.position.y)
        graphics.add(self.sprite)
