"""
Classes that represents a entity
to manage all game objects on the
scene.
"""

from simian.exceptions.unimplemented_method import NotOverriddenMethod
from enum import Enum


class State(Enum):
    CREATED = 0
    STARTED = 1
    FINISHED = 2


class BaseScene:
    """
    The base representation of a simian
    scene. A scene manage the load, update,
    draw and unload of all game objects.
    """
    def __init__(self, name='Default Scene', id=0):
        self.name = name
        self.id = id
        self.state = State['CREATED']

    def draw(self, graphics):
        raise NotOverriddenMethod('draw')

    def update(self, time_elapsed):
        raise NotOverriddenMethod('update')

    def load(self):
        raise NotOverriddenMethod('load')

    def unload(self):
        raise NotOverriddenMethod('unload')
