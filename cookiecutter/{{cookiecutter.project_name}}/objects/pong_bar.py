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
        
        print("Y: " + str(self.position.y))
        if new_position.y < 0 and self.position.y < 3 + self.sprite.get_height()/2:
            self.position -= new_position
            print("Maior que o topo, desfiz move")
        elif new_position.y > 0 and self.position.y + self.sprite.get_height() > 597 + self.sprite.get_height()/2:
            self.position -= new_position
            print("Maior que o bottom, desfiz move")
        else:
            print("tá susse")
             

    def draw(self, graphics):
        self.sprite.set_x(self.position.x)
        self.sprite.set_y(self.position.y)
        graphics.add(self.sprite)
