
import pygame
class TextObject():

    def __init__(self):
        pass


    def set_text_font(self,font_text,size_font_text):
         font = pygame.font.SysFont(font_text, size_font_text)
         return font

    def draw_text(self,font_object,text_message,soft_edges,color):
         display_message = font_object.render(text_message, soft_edges, color)
         return display_message

    def available_fonts_on_machine(self):
        all_fonts = pygame.font.get_fonts()
        for font in all_fonts:
            print(font)

    def bold_text(self,is_bold):
        pygame.font.Font.set_bold(is_bold)
