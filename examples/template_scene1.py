from simian.scene.base_scene import BaseScene, State
from simian.input.keyboard_manager import Keyboard
from examples.template_player_object import Player
from simian.engine import GameEngine


class TemplateScene1(BaseScene):
    def draw(self, graphics):
        for game_object in self.game_objects:
            game_object.draw(graphics)

    def update(self, time_elapsed):
        for game_object in self.game_objects:
            game_object.update(time_elapsed)

        print(self.player.position.x)
        if(self.player.position.x > 400):
            GameEngine().set_next_scene("Fase2")
            self.state = State.FINISHED

    def load(self):
        self.keyboard = Keyboard()
        self.player = Player(50, 50)
        self.game_objects = [self.player]

    def unload(self):
        pass
