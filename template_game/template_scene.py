from simian.scene.base_scene import BaseScene
from simian.input.keyboard_manager import Keyboard

class TemplateScene(BaseScene):
    def draw(self, graphics):
        pass

    def update(self, time_elapsed):
        print(time_elapsed)

    def load(self):
        self.keyboard = Keyboard()

    def unload(self):
        pass
