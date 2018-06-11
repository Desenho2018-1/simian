"""
GameCanvas classes.
All renderable objects must use this class
to render.
"""
import pygame

from simian.utils.singleton import Singleton


class GameCanvas(metaclass=Singleton):
    """
    This class manages game canvas
    (windows where every renderable object must be rendered)
    """
    def __init__(self, name='Game made with Simian', size=(800, 600)):
        self.size = size
        self.name = name
        self.screen = None

    def open(self):
        """
        Open a window to draw all elements
        of the game.
        """
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)

    def refresh(self):
        pygame.display.flip()
        self.screen.fill((0,0,0))

    def get_screen(self):
        """
        Return the canvas surface.
        """
        return self.screen

    def close(self):
        """
        Close the window and consequently the game.
        """
        pygame.display.quit()
