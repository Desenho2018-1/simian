"""
GameCanvas classes.
All renderable objects must use this class
to render.
"""
import pygame

from simian.physics.space import Size
from simian.utils.singleton import Singleton


class GameCanvas(metaclass=Singleton):
    """
    This class manages game canvas
    (windows where every renderable object must be rendered)
    """

    def __init__(self, size=None, name='Game made with Simian',
                 width=800, height=600):
        self.size = size if size else Size(width, height)
        self.name = name

    def open(self):
        """
        Open the screen
        """
        screen = pygame.display.set_mode(self.size())
        pygame.display.set_caption(self.name)
        """
        Keep the screen open, when on while True
        """
        self.refresh_screen()

    def refresh_screen(self):
        pygame.display.flip()

    def close(self):
        """
        Close the screen
        """
        pygame.display.quit()
