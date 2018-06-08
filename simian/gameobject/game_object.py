"""
GameObject classes.
All objects in a game should be represented by this classes.
"""

from simian.math.vector import Vec2


class GameObject(object):
    """
    The base GameObject of Simian Engine. A game object has
    a position that defines his cordinates (x, y) in a 2D space
    and also has a draw and a update method.
    """
    __slots__ = ['position']

    def __init__(self, x=None, y=None):
        self.position = Vec2(x, y)

    def update(self):
        """
        This method is called every frame of the game loop.
        All the logic that changes something in a game object goes here.
        E.g. a square that change his color every 5 seconds, your code
        could be something like
            >>> def update(self):
                    if its_time:
                        self.color = next_color(self.color)
        """
        pass

    def draw(self, renderable_object):
        """
        This method is called every frame of the game loop.
        Draw the renderable object in the position of this game object.
        """
        pass

    def clone(self):
        """
        Clone the current object for better creation management.
        """
        return self
