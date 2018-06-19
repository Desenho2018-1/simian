"""
Implements an object pool for
all classes in objects folder of
a simian project.
"""

from simian.utils.singleton import Singleton
import importlib
import sys


class ObjectPool(metaclass=Singleton):
    """
    Represents a pool of objects
    that are in objects folder of a simian project.
    """
    def __init__(self):
        self._objects = []

    def get(self, p_class, *args):
        """
        Return a unused object in the pool
        or create a new one otherwise.
        """
        for obj in self._objects:
            if isinstance(obj, p_class) and not obj.is_active:
                obj.is_active = True
                obj.position.x = args[0]
                obj.position.y = args[1]
                return obj

        module = importlib.import_module('objects')
        class_name = p_class.__name__
        # we need this to verify in each file of 'objects'
        # folder if the given 'class_name' exists
        for sub_module in module.__all__:
            try:
                module = importlib.import_module(f'objects.{sub_module}')
                loc = {'module': module}

                exec(f'obj = module.{class_name}({args})', globals(), loc)

                obj = loc['obj']
                self._objects.append(obj)
                return obj
            except AttributeError:
                pass
        raise AttributeError(f'Class {class_name} does not exists!!')

    def release(self, obj):
        """
        Change the state 'in_use' of an object
        to 'released'.
        """
        obj.is_active = False
