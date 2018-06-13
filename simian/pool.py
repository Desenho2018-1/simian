"""
Implements an object pool for
all classes in objects folder of
a simian project.
"""

from simian.utils.singleton import Singleton
import importlib


class ObjectPool(metaclass=Singleton):
    """
    Represents a pool of objects
    that are in objects folder of a simian project.
    """
    def __init__(self):
        self._objects = []

    def get(self, class_name, *args):
        """
        Return a unused object in the pool
        or create a new one otherwise.
        """
        for obj in self._objects:
            if isinstance(obj, class_name) and obj[1] == 'released':
                obj[1] = 'in_use'
                return obj[0]

        module = importlib.import_module('objects')

        # we need this to verify in each file of 'objects'
        # folder if the given 'class_name' exists
        for sub_module in module.__all__:
            try:
                module = importlib.import_module(f'objects.{sub_module}')
                loc = {'module': module}

                exec(f'obj = module.{class_name}({args})', globals(), loc)

                obj = loc['obj']
                self._objects.append((obj, 'in_use'))
                return obj
            except AttributeError:
                pass
        raise AttributeError(f'Class {class_name} does not exists!!')

    def release(self, obj):
        """
        Change the state 'in_use' of an object
        to 'released'.
        """
        for i in range(len(self._objects)):
            if self._objects[i][0] is obj:
                self._objects[i] = (obj, 'released')
