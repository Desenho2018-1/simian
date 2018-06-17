from simian.scene.base_scene import BaseScene
from simian.input.keyboard_manager import Keyboard
from examples.template_player_object import Player
from simian.math.vector import Vec2


class TemplateScene(BaseScene):

    def draw(self, graphics):
        for game_object in self.game_objects:
            game_object.draw(graphics)

    def update(self, time_elapsed):
        for game_object in self.game_objects:
            game_object.update(time_elapsed)

        # print(self.game_objects[0].collider.position)
        # print(self.game_objects[1].collider.position)
        print('\nCOLIDIU\n')
        self.game_objects[0].position += self.game_objects[0].velocity*time_elapsed
        self.game_objects[1].position += self.game_objects[1].velocity*time_elapsed

    def load(self):
        self.keyboard = Keyboard()
        self.game_objects = [Player(50, 50)]

    def unload(self):
        pass
