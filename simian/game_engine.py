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

    def load(self):
        game_window_size = Size(GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT)
        self.game_canvas = GameCanvas(game_window_size, GAME_NAME)
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
        pygame.key.set_repeat(True)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                else:
                    # Update Actual Game Scene
                    self.scene_manager.current_scene.update(1)

            # Refresh screen
            self.game_canvas.refresh_screen()

            # Set the number of frames per second
            clock.tick(NUMBER_OF_FRAMES)
