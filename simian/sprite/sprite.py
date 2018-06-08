import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        super(Sprite, self).__init__()

        self.image = pygame.image.load(filename)  # Returns a Surface object

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
