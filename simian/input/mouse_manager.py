import pygame
from simian.utils.singleton import Singleton


class Mouse(metaclass=Singleton):

    def get_position(self):
        return pygame.mouse.get_pos()

    def set_position(self, x, y):
        pygame.mouse.set_pos([x,y])

    def set_visible(self, is_visible):
        pygame.mouse.set_visible(is_visible)

    def is_focused(self):
        if pygame.mouse.get_focused() is 1:
            return True

        return False

    def get_cursor(self):
        return pygame.mouse.get_cursor()

    def set_cursor(self):
        pass
           
    def set_custom_cursor(self):
        pass

    def left_pressed(self):
        if pygame.mouse.get_pressed()[0] is 1:
            return True

        return False

    def scroll_pressed(self):
        if pygame.mouse.get_pressed()[1] is 1:
            return True

        return False

    def right_pressed(self):
        if pygame.mouse.get_pressed()[2] is 1:
            return True

        return False

    def amount_mov(self):
        return pygame.mouse.get_rel()
