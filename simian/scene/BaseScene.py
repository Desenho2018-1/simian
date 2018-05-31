import pygame

# This class creates the scene basic structure


class BaseScene(object):

    def __init__(self, name="DEFAULT", id=0):
        self.name = name
        self.id = id

    def draw(self, grafics):
        pass

    def update(self, time_elapsed):
        pass

    def load(self):
        pass

    def unload(self):
        pass
