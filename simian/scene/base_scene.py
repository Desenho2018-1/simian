"""
Classes that represents a entity
to manage all game objects on the
scene.
"""

from simian.exceptions.unimplemented_method import NotOverriddenMethod


class BaseScene:
    """
    The base representation of a simian
    scene. A scene manage the load, update,
    draw and unload of all game objects.
    """
    def __init__(self, name='Default Scene', id=0):
        self.name = name
        self.id = id

    def draw(self, graphics):
        raise NotOverriddenMethod('draw')

    def update(self, time_elapsed):
        raise NotOverriddenMethod('update')

    def load(self):
        raise NotOverriddenMethod('load')

    def unload(self):
        raise NotOverriddenMethod('unload')
