import pygame

IMAGE_ASSETS = "/home/shammyz/Documents/repos/simian/tests/assets/images/"


class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        super(Sprite, self).__init__()

        # Returns a Surface object
        self.image = pygame.image.load(IMAGE_ASSETS + filename)

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
