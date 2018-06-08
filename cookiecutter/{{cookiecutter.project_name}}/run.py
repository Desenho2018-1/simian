from conf import *
from simian.engine import GameEngine

# Main game loop
engine = GameEngine()

# Initialize
engine.load(GAME_NAME, WINDOW_SIZE)

# Add all game scenes
[engine.add(scene) for scene in SCENE_LIST]

# Set an initial scene
engine.set(INITIAL_SCENE)

# Run game
engine.run()
