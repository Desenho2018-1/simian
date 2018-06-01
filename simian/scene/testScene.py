import pygame

from base_scene import BaseScene

class TestScene(BaseScene):
    def __init__(self, name, id):
        super().__init__(name,id)

    def load(self):
        print("hue")

a = TestScene(name="teste",id=2)
a.load()

a.unload()
