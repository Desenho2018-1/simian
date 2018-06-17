from simian.engine import GameEngine
from examples.template_scene1 import TemplateScene1
from examples.template_scene2 import TemplateScene2

engine = GameEngine()

engine.load("Template Game", (800, 600))

scene1 = TemplateScene1("Fase1", 0)
scene2 = TemplateScene2("Fase2", 1)

engine.add_scene(scene1, scene2)
engine.set_initial_scene("Fase1")

engine.run()
