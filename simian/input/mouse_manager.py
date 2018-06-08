import pygame
from simian.utils.singleton import Singleton


class Mouse(metaclass=Singleton):

    def get_mouse_position(self):
        return pygame.mouse.get_pos()
