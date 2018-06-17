from simian.scene.base_scene import BaseScene, State
from simian.input.keyboard_manager import Keyboard
from examples.template_player_object import Player
from simian.engine import GameEngine


class TemplateScene2(BaseScene):
    def draw(self, graphics):
        for game_object in self.game_objects:
            game_object.draw(graphics)

    def update(self, time_elapsed):
        for game_object in self.game_objects:
            game_object.update(time_elapsed)

        if(self.player.position.x < 30):
            GameEngine().set_next_scene("Fase1")
            self.state = State.FINISHED

    def load(self):
        self.keyboard = Keyboard()
        self.player = Player(400, 400)
        self.game_objects = [self.player]

    def unload(self):
        pass
