
import pygame
class TextObject():

    def __init__(self):
        pass
    def set_text_font(self,font_text,size_font_text):
         pygame.font.SysFont(font_text, size_font_text)

    def draw_text(text_message,soft_edges,color):
        font.render(text_message, soft_edges, color)

    def available_fonts_on_machine(self):
        all_fonts = pygame.font.get_fonts()
        for font in all_fonts:
            print(font)
