"""
Classes that provide methods for display
and manage texts on screens.
"""

import pygame
from simian.engine import GameEngine

class Text:
    """
    This class represents a simian
    text. A text with custom size and font
    that can be drawn to the screen.
    """
    def __init__(self, content, size, font='default'):
        pygame.font.init()
        self.content = str(content)
        self.size = size
        self._font = pygame.font.SysFont(font, size)
        self._styles = {'underline': False, 'bold': False, 'italic': False}

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font):
        self._font = SysFont(font, size)
        self._font.set_underline(_styles['underline'])
        self._font.set_underline(_styles['bold'])
        self._font.set_underline(_styles['italic'])

    @property
    def styles(self):
        return self._styles

    def draw(self, position, soft_edges=True, color=(255, 255, 255)):
        """
        Render the text content with the given
        color, on the given surface and in the given position.
        """
        render = self._font.render(self.content, soft_edges, color)
        self.canvas = GameEngine().game_canvas.get_screen().blit(render, position)

    def available_fonts(self):
        """
        Return all available fonts on the user machine.
        """
        return pygame.font.get_fonts()

    def underline(self, boolean):
        self._styles['underline'] = boolean
        self._font.set_underline(boolean)

    def bold(self, boolean):
        self._styles['bold'] = boolean
        self._font.set_bold(boolean)

    def italic(self, boolean):
        self._styles['italic'] = boolean
        self._font.set_italic(boolean)


    """
        Methods for check if style is applied to text
    """
    def is_underline(self):
        return self.styles['underline']

    def is_bold(self):
        return self.styles['bold']

    def is_italic(self):
        return self.styles['italic']
