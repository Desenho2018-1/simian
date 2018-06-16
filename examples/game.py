from simian.engine import GameEngine
from examples.template_scene import TemplateScene

engine = GameEngine()

engine.load("Template Game", (800, 600))

scene1 = TemplateScene("Fase1", 0)
scene2 = TemplateScene("Fase2", 1)
scene3 = TemplateScene("Fase3", 2)

engine.add_scene(scene1, scene2, scene3)
engine.set_initial_scene("Fase1")

engine.run()
