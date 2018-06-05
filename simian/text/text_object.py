import pygame

    """
        This class provide, methods
        for display and to menage texts
        on screen and scene
    """

class TextObject(Object):

    def __init__(self,text_message,size,font_text):
        self.text_message = text_message
        self.size = size
        self.font_text = font_text
        self.font_object = None

    def set_text_font(self):
        self.font_object =  pygame.font.SysFont(self.font_text, self.size)


    def draw_text(self,soft_edges,color):
        return self.font_object.render(self.text_message, soft_edges, color)

        """
            Return all font available on the user machine
        """
    def available_fonts_on_machine(self):
        all_fonts = pygame.font.get_fonts()
        for font in all_fonts:
            print(font)

    def is_bold(self,boolean):
            self.font_object.set_bold(boolean)

    def is_italic(self,boolean):
            self.font_object.set_italic(boolean)
