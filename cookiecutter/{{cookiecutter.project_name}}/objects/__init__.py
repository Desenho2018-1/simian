import os

__all__ = []

cur_path = os.path.dirname(__file__)

files = [f for f in os.listdir(cur_path) if os.path.isfile(cur_path + '/' + f)]

for f in files:
    if f != '__init__.py':
        __all__.append(f.split('.')[0])
