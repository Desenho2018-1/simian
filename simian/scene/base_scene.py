
from simian.utils.exception.unimplemented_method import NotOverriddenMethod
"""
This class create base structure for
creation scenes in games
"""


class BaseScene(object):

    def __init__(self, name="DEFAULT", id=0):
        self.name = name
        self.id = id

    def draw(self, graphics):
        raise NotOverriddenMethod("draw")

    def update(self, time_elapsed):
        raise NotOverriddenMethod("update")

    def load(self):
        raise NotOverriddenMethod("load")

    def unload(self):
        raise NotOverriddenMethod("unload")
