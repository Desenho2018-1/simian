

"""
This class create base structure for
creation scenes in games
"""

from simian.utils.exception.unimplemented_method import NotOverriddenMethod
import pygame
class BaseScene():

    def __init__(self, name="DEFAULT", id=0):
        self.name = name
        self.id = id

    def draw(self, grafics):
        raise NotOverriddenMethod("draw")

    def update(self, time_elapsed):
        raise NotOverriddenMethod("update")

    def load(self):
        raise NotOverriddenMethod("load")

    def unload(self):
        raise NotOverriddenMethod("unload")
