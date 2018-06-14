from simian.scene.base_scene import BaseScene
from simian.input.keyboard_manager import Keyboard
from simian.physics.collision import detect_collision

from objects.pong_bar import PongBar
from objects.ball import Ball


class MainScene(BaseScene):

    def draw(self, graphics):
        for game_object in self.game_objects:
            game_object.draw(graphics)

    def update(self, time_elapsed):
        for game_object in self.game_objects:
            game_object.update(time_elapsed)
        

    def load(self):
        self.keyboard = Keyboard()
        self.game_objects = [PongBar((50, 300)), PongBar((700, 300)), Ball((200, 100))]

    def unload(self):
        pass