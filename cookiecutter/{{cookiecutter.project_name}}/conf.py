import os
from scenes.main_scene import MainScene


GAME_NAME = '{{cookiecutter.project_name}}'

WINDOW_SIZE = ({{cookiecutter.window_width}}, {{cookiecutter.window_height}})

SCENE_LIST = [MainScene('Stage 1', 0)]

INITIAL_SCENE = {{cookiecutter.initial_scene}}

ASSETS = os.getcwd() + '/assets/'
