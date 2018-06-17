"""
Define a interface to observe
a subject and receive notifications
when it changes.
"""

import abc


class Observer(metaclass=abc.ABCMeta):
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass
