import sys
sys.path.append("../utils/exception")
#from simian.utils.expection.unimplemented_method import NotOverridenMethod
import pygame
from unimplemented_method import NotOverridenMethod
class BaseScene(object):

    # This class creates the scene basic structure

    def __init__(self, name="DEFAULT", id=0):
        self.name = name
        self.id = id

    def draw(self, grafics):
        raise NotOverridenMethod("draw")

    def update(self, time_elapsed):
        raise NotOverridenMethod("update")

    def load(self):
        raise NotOverridenMethod("load")

    def unload(self):
        raise NotOverridenMethod("unload")
