import pygame
from simian.window.game_canvas import GameCanvas
from simian.physics.space import Size
from simian.utils.singleton import Singleton
from simian.scene.scene_manager import SceneManager
from simian.input.keyboard_manager import Keyboard

# Game Configuration Constants
GAME_WINDOW_HEIGHT = 800
GAME_WINDOW_WIDTH = 600
GAME_NAME = "PlaceHolder Name"
NUMBER_OF_FRAMES = 60

class GameEngine(metaclass=Singleton):

    def load(self, game_name, width, height):
        self.game_canvas = GameCanvas(Size(width, height), game_name)
        self.scene_manager = SceneManager()
        self.keyboard = Keyboard()

    def add_scene(self, *args):
        self.scene_manager.add_scene(args)

    def set_initial_scene(self, scene_name):
        self.scene_manager.load_scene(scene_name)

    def run(self):
        pygame.init()

        clock = pygame.time.Clock()
        self.game_canvas.open()
        self.screen = self.game_canvas.get_screen()

        pygame.key.set_repeat(True)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.scene_manager.current_scene.update(clock.get_time()/1000)
            
            groups = pygame.sprite.OrderedUpdates()
            self.scene_manager.current_scene.draw(groups)
            groups.draw(self.screen)
            
            # Refresh screen
            self.game_canvas.refresh_screen()

            # Set the number of frames per second
            clock.tick(NUMBER_OF_FRAMES)
