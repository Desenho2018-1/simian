
from base_scene import BaseScene

class TestScene(BaseScene):

    def __init__(self, name, id):
        super().__init__(name,id)

    def draw(self):
        print("test")

teste = TestScene("test", 1)
teste.draw()
