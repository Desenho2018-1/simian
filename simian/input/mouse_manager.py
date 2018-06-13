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

    # Set an game_object to be your new icon
    def set_custom_cursor(self, game_object):
        self.set_visible(False)
        position = self.get_position()


    # Check if mouse is over a game_object
    def is_over(self, game_object):
        collider = game_object.collider
        mouse_position_x, mouse_position_y = self.get_position()

        first_point = (collider.position[0] - collider.size[0] / 2 , collider.position[1] - collider.size[1] / 2)
        second_point = (collider.position[0] + collider.size[0] / 2 , collider.position[1] + collider.size[1] / 2)

        if ((mouse_position_x >= first_point[0] and mouse_position_x <= second_point[0]) and
           (mouse_position_y >= first_point[1] and mouse_position_y <= second_point[1])):
           return True

        return False

    # Check if mouse clicked over game_object
    def is_clicked_over(self, game_object):
        is_over = self.is_over(game_object)
        button_pressed = {'left': False,
                          'scroll': False,
                          'right':False}

        if is_over:
            button_pressed['left'] = self.left_pressed()
            button_pressed['scroll'] = self.scroll_pressed()
            button_pressed['right'] = self.right_pressed()


        return button_pressed

    # Drag a game_object changing the position
    def drag(self, button_choice, game_object):
        buttons = {'left': self.left_pressed(),
                   'scroll': self.scroll_pressed(),
                   'right': self.right_pressed()}

        button_clicked = buttons[button_choice]

        if button_clicked:
            mouse_position = self.get_position()
            return mouse_position

        return (game_object.position.x, game_object.position.y)
