import pygame
from simian.utils.singleton import Singleton


class Mouse(metaclass=Singleton):
    def left_pressed(self):
        """
        Returns True if the LEFT button of
        mouse is being pressed and False otherwise.
        """
        if pygame.mouse.get_pressed()[0] is 1:
            return True

        return False

    def scroll_pressed(self):
        """
        Returns True if the SCROLL button of
        mouse is being pressed and False otherwise.
        """
        if pygame.mouse.get_pressed()[1] is 1:
            return True

        return False

    def right_pressed(self):
        """
        Returns True if the RIGHT button of
        mouse is being pressed and False otherwise.
        """
        if pygame.mouse.get_pressed()[2] is 1:
            return True

        return False

    def get_position(self):
        """
        Returns a tuple with the current position
        of mouse.
        """
        return pygame.mouse.get_pos()

    def set_position(self, x, y):
        """
        Sets the current position of mouse.
        """
        pygame.mouse.set_pos([x, y])

    # Get the position based on the last call of function
    def get_relative_position(self):
        """
        Returns a tuple with the current position
        of mouse based on the last call of the function.
        """
        return pygame.mouse.get_rel()

    # Set visibility of mouse cursor
    def set_visible(self, is_visible):
        """
        Sets the mouse cursor visibility.
        Set it True to be visible, and False to not to be.
        """
        pygame.mouse.set_visible(is_visible)

    def is_focused(self):
        """
        Returns True if mouse is over the game window and False otherwise.
        """
        if pygame.mouse.get_focused() is 1:
            return True

        return False

    def get_cursor(self):
        """
        Returns data that constructs the cursor.
        """
        return pygame.mouse.get_cursor()

    def set_cursor(self, size, hotspot, xormasks, andmasks):
        """
        Get data that construct the cursor layout based on (xor/and)masks
        """
        pygame.mouse.set_cursor(size, hotspot, xormasks, andmasks)

    def set_custom_cursor(self, game_object):
        """
        Sets an game_object to be your new cursor icon.
        """
        self.set_visible(False)
        mouse_position = self.get_position()
        game_object.set_x(mouse_position[0])
        game_object.set_y(mouse_position[1])

    def is_over(self, game_object):
        """
        Returns True if mouse is over some game_object,
        otherwise returns False.
        """
        collider = game_object.collider
        mouse_position_x, mouse_position_y = self.get_position()

        first_point = (collider.position[0] - collider.size[0] / 2,
                       collider.position[1] - collider.size[1] / 2)
        second_point = (collider.position[0] + collider.size[0] / 2,
                        collider.position[1] + collider.size[1] / 2)

        if ((mouse_position_x >= first_point[0] and
             mouse_position_x <= second_point[0]) and
            (mouse_position_y >= first_point[1] and
             mouse_position_y <= second_point[1])):
            return True

        return False

    def is_clicked_over(self, game_object):
        """
        Returns a dictionary where the keys are the
        button names and the values are:
        True if the button was pressed over a
        game_object or false if not.
        """
        is_over = self.is_over(game_object)
        button_pressed = {'left': False,
                          'scroll': False,
                          'right': False}

        if is_over:
            button_pressed['left'] = self.left_pressed()
            button_pressed['scroll'] = self.scroll_pressed()
            button_pressed['right'] = self.right_pressed()

        return button_pressed

    def drag(self, button_choice, game_object):
        """
        Returns a tuple with mouse x, y coordinates
        based on button name pressed.
        """
        buttons = {'left': self.left_pressed(),
                   'scroll': self.scroll_pressed(),
                   'right': self.right_pressed()}

        button_clicked = buttons[button_choice]

        if button_clicked:
            mouse_position = self.get_position()
            return mouse_position

        return (game_object.position.x, game_object.position.y)
