from simian.physics.bodies import RigidBody
from simian.physics.colliders import BoxCollider
from simian.math.vector import Vec2
from simian.sprite.sprite import Sprite
import conf


class Ball(RigidBody):

    def __init__(self, position):
        super().__init__(position, 1, BoxCollider(position, (50, 50)), 5)
        self.sprite = Sprite(conf.ASSETS + 'ball.png')

    def update(self, time_elapsed):
        if(self.keyboard.is_key_pressed(Keyboard.RETURN)):
            self.velocity = Vec2(80, 70)
        
        self.position += self.velocity*time_elapsed

    def draw(self, graphics):
        self.sprite.set_x(self.position.x)
        self.sprite.set_y(self.position.y)
        graphics.add(self.sprite)