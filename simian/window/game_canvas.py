"""
GameCanvas classes.
All renderable objects must use this class
to render.
"""

from simian.physics import space
from simian.utils.singleton import Singleton
import pygame


WIDTH = 800
HEIGHT = 600

class GameCanvas(metaclass=Singleton):
    """
    This class manages game canvas
    (windows where every renderable object must be rendered)
    """

    def __init__(self, size=None, name='Simian Engine'):
        self.size = size if size else space.Size(WIDTH, HEIGHT)
        self.name = name

    def open(self):
        """
        Open the screen
        """
        screen = pygame.display.set_mode(self.size())
        pygame.display.set_caption(self.name)

    def close(self):
        """
        Close the screen
        """
        pygame.display.quit()
