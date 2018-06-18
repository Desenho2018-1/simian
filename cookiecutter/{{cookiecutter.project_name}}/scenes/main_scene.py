from simian.scene.base_scene import BaseScene, State
from simian.input.keyboard_manager import Keyboard
from simian.physics.collision import CollisionManager
from simian.utils.lists import GameObjectList
from simian.math.vector import Vec2
from simian.text import Text
from objects.ground import Ground
from objects.pong_bar import PongBar
from objects.ball import Ball
from simian.engine import GameEngine


class MainScene(BaseScene):

    def draw(self, graphics):
        for game_object in self.game_objects:
            game_object.draw(graphics)
        if(self.game_end):
            self.game_text.draw((400, 300))
            self.game_text2.draw((400, 350))

        if(self.game_start):
            self.game_text2.draw((400, 350))
            if(self.ball.moving):
                self.game_start = False

    def update(self, time_elapsed):
        self.collision_manager.manage_collision()
        for g in self.game_objects:
            g.update(time_elapsed)

        if self.ball.position.x > 800:
            self.game_end = True
            self.game_text = Text("Player 1 Wins", 24)
        elif self.ball.position.x < 0:
            self.game_end = True
            self.game_text = Text("Player 2 Wins", 24)

        if(self.game_end):
            if(Keyboard().is_key_pressed(Keyboard.RETURN)):
                GameEngine().set_next_scene("Stage 1")
                self.state = State.FINISHED

    def load(self):
        self.keyboard = Keyboard()
        self.ball = Ball((350, 100))
        self.game_end = False
        self.game_start = True
        self.game_text2 = Text("Pressione enter para começar", 24)
        self.game_objects = GameObjectList(
            self.ball,
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
