from simian.game_engine import GameEngine
from template_game.template_scene import TemplateScene

engine = GameEngine()

engine.load()

scene1 = TemplateScene("Fase1", 0)
scene2 = TemplateScene("Fase2", 1)
scene3 = TemplateScene("Fase3", 2)

engine.add_scene(scene1,scene2,scene3)


engine.run()