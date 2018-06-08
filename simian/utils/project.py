import os


def create_project(project_name):
    """
    Create a simian project structure
    """
    os.mkdir(project_name)
    os.chdir(project_name)
    os.mkdir('scenes')
    os.mkdir('game_objects')
    os.mkdir('assets')
    with open('conf.py', 'a') as conffile:
        create_confpy(conffile)
    with open('run.py', 'a') as runfile:
        create_runpy(runfile)


def create_confpy(conffile):
    conffile.write('GAME_NAME = "Pong"')
    conffile.write('WINDOW_SIZE = (800, 600)')
    conffile.write('SCENE_LIST = []')
    conffile.write('INITIAL_SCENE = "Menu"')


def create_runpy(runfile):
    runfile.write('from conf.py import *\n')
    runfile.write('from simian.game_engine import GameEngine\n\n')
    runfile.write('engine = GameEngine()')
    runfile.write('engine.load(GAME_NAME, WINDOW_SIZE)')
    runfile.write('[engine.add(scene) for scene in SCENE_LIST]')
    runfile.write('engine.set(INITIAL_SCENE)')
    runfile.write('engine.run()')
