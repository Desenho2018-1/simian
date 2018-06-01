

"""
This class create base structure for
creation scenes in games
"""

import sys
sys.path.append("../utils/exception")
import pygame
from unimplemented_method import NotOverriddenMethod
class BaseScene(object):


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
