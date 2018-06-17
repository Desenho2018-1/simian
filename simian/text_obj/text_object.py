import pygame

from simian.utils.exception.text_exception import TextException


class TextObject(object):

    """
        This class provide, methods
        for display and to menage texts
        on screen and scene
    """

    def __init__(self, text_message, size, font_text):
        self.text_message = text_message
    #    self.text_is_str(self.text_message)
        self.size = size
        self.font_text = font_text
        self.font_object = pygame.font.SysFont(self.font_text, self.size)

    def text_is_str(self, message):
        if(isinstance(message, str)):
            raise TextException()
        else:
            # nothing todo
            pass

    def draw_text(self, soft_edges, color):
        return self.font_object.render(self.text_message, soft_edges, color)

    """
        Return all font available on the user machine
    """
    def available_fonts_on_machine(self):
        all_fonts = pygame.font.get_fonts()
        for font in all_fonts:
            print(font)

    """
        Methods for custom display text
    """
    def is_bold(self, boolean):
        """ default is false """
        self.font_object.set_bold(boolean)

    def is_italic(self, boolean):
        """ default is false """
        self.font_object.set_italic(boolean)

    def is_underline(self, boolen):
        """ default is false """
        self.font_object.set_underline(boolen)

    """
        Methods for check if custom text is display
    """

    def check_bold(self):
        self.font_object.get_bold()

    def check_italic(self):
        self.font_object.get_italic()

    def check_underline(self):
        self.font_object.get_underline()
