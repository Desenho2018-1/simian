from simian.scene.base_scene import BaseScene
from simian.input.keyboard_manager import Keyboard
from simian.physics.collision import CollisionManager
from simian.utils.lists import GameObjectList
from simian.math.vector import Vec2

from objects.ground import Ground
from objects.pong_bar import PongBar
from objects.ball import Ball


class MainScene(BaseScene):

    def draw(self, graphics):
        for game_object in self.game_objects:
            game_object.draw(graphics)

    def update(self, time_elapsed):
        self.collision_manager.manage_collision()
        for g in self.game_objects:
            g.update(time_elapsed)

    def load(self):
        self.keyboard = Keyboard()
        self.game_objects = GameObjectList(
            Ball((350, 100)),
            Ground((148, 634.5)),
            Ground((444, 634.5)),
            Ground((740, 634.5)),
            Ground((148, -33.5)),
            Ground((444, -33.5)),
            Ground((740, -33.5)),
            PongBar((50, 300), control_p2),
            PongBar((750, 300), control_p1),
        )
        self.collision_manager = CollisionManager()
        self.collision_manager.attach(self.game_objects)

    def unload(self):
        pass


def control_p1():
    keyboard = Keyboard()
    position = Vec2(0, 0)
    if keyboard.is_key_pressed(Keyboard.DOWN):
        position = Vec2(0, 200)
    if keyboard.is_key_pressed(Keyboard.UP):
        position = Vec2(0, -200)
    return position


def control_p2():
    keyboard = Keyboard()
    position = Vec2(0, 0)
    if keyboard.is_key_pressed(Keyboard.K_s):
        position = Vec2(0, 200)
    if keyboard.is_key_pressed(Keyboard.K_w):
        position = Vec2(0, -200)
    return position
