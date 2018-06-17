"""
Usefull custom lists implementations
used by simian.
"""

from simian.utils.observer import Observer


class GameObjectList(Observer, list):
    """
    A list of game objects that receives
    notifications of changes in a subject.
    """
    def __init__(self, *args):
        list.__init__(self, args)
        self._subject = None
        self._observer_state = None

    def __hash__(self):
        return hash(list)

    def update(self, new_elements):
        self = GameObjectList(new_elements)
