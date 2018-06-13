import pygame
import os
from simian.config import Configuration

# TODO Correct this so we use the singleton instance of the engine
# not a new instance of config

IMAGE_ASSETS = Configuration().IMAGE_ASSETS_PATH


class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        super(Sprite, self).__init__()

        file_absolute_path = os.path.join(IMAGE_ASSETS, filename)

        # Returns a Surface object
        self.image = pygame.image.load(file_absolute_path)

        # Returns the rectangular area of the Surface
        self.rect = self.image.get_rect()

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

        # Since we resized the image, the rect just got bigger!
        self.rect = self.image.get_rect()

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def draw(self, graphics, x, y):
        self.set_x(x)
        self.set_y(y)
        graphics.add(self)
