"""
Classes that provide methods for display
and manage texts on screens.
"""

import pygame


class Text:
    """
    This class represents a simian
    text. A text with custom size and font
    that can be drawn to the screen.
    """
    def __init__(self, content, size, font='default'):
        self.content = content
        self.size = size
        self._font = pygame.SysFont(font, size)
        self._styles = {'underline': False, 'bold': False, 'italic': False}

    @property
    def font(self):
        return self.font

    @font.setter
    def font(self, font):
        self._font = SysFont(font, size)
        self._font.set_underline(_styles['underline'])
        self._font.set_underline(_styles['bold'])
        self._font.set_underline(_styles['italic'])

    @property
    def styles(self):
        return self._styles

    def draw(self, surface, position, soft_edges=True, color=(255, 255, 255)):
        """
        Render the text content with the given
        color, on the given surface and in the given position.
        """
        render = self._font.render(self.content, soft_edges, color)
        surface.blit(render, position)

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
