import pygame
from simian.utils.singleton import Singleton


class Mouse(metaclass=Singleton):
    # Check if left button of mouse is pressed
    def left_pressed(self):
        if pygame.mouse.get_pressed()[0] is 1:
            return True

        return False

    # Check if scroll button of mouse is pressed
    def scroll_pressed(self):
        if pygame.mouse.get_pressed()[1] is 1:
            return True

        return False

    # Check if right button of mouse is pressed
    def right_pressed(self):
        if pygame.mouse.get_pressed()[2] is 1:
            return True

        return False

    # Get current position of mouse
    def get_position(self):
        return pygame.mouse.get_pos()

    # Set a position to mouse
    def set_position(self, x, y):
        pygame.mouse.set_pos([x,y])

    # Get the position based on the last call of function
    def get_relative_position(self):
        return pygame.mouse.get_rel()

    # Set visibility of mouse cursor
    def set_visible(self, is_visible):
        pygame.mouse.set_visible(is_visible)

    # Check if the mouse is over the game window
    def is_focused(self):
        if pygame.mouse.get_focused() is 1:
            return True

        return False

    # Get data that compose mouse cursor
    def get_cursor(self):
        return pygame.mouse.get_cursor()

    #
    def set_cursor(size, hotspot, xormasks, andmasks):
        pygame.mouse.set_cursor(size, hotspot, xormasks, andmasks)

    # Set an gameObject to be your new icon
    def set_custom_cursor(self, gameObject):
        self.set_visible(False)
        position = self.get_position()


    # Check if mouse is over a gameObject
    def is_over(self, gameObject):
        pass

    # Check if mouse clicked over gameObject
    def is_clicked(self, gameObject):
        pass
