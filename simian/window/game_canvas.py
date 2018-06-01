"""
GameCanvas classes.
All renderable objects must use this class
to render.
"""
import pygame
import sys
sys.path.append("../physics")
sys.path.append("../utils/")

from space import Size
from singleton import Singleton


class GameCanvas(metaclass=Singleton):
    """
    This class manages game canvas
    (windows where every renderable object must be rendered)
    """

    def __init__(self, size=None, name='Simian Engine',width=800, height=600):
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
        pygame.display.flip()

    def close(self):
        """
        Close the screen
        """
        pygame.display.quit()

while True:
    a = GameCanvas()
    a.open()
