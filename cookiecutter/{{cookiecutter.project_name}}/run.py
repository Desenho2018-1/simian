from conf import *
from simian.engine import GameEngine

# Main game loop
engine = GameEngine()

# Initialize
engine.load(GAME_NAME, WINDOW_SIZE)

# Add all game scenes
[engine.add_scene(scene) for scene in SCENE_LIST]

# Set an initial scene
engine.set_initial_scene(SCENE_LIST[INITIAL_SCENE].name)

# Run game
engine.run()
