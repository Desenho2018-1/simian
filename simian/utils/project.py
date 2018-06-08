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

    with open('__init__.py', 'a'):
        pass

    with open('conf.py', 'a') as conffile:
        create_confpy(conffile)

    with open('run.py', 'a') as runfile:
        create_runpy(runfile)


def create_confpy(conffile):
    conffile.write('GAME_NAME = "Pong"\n\n')
    conffile.write('WINDOW_SIZE = (800, 600)\n\n')
    conffile.write('SCENE_LIST = []\n\n')
    conffile.write('INITIAL_SCENE = "Menu"\n\n')


def create_runpy(runfile):
    runfile.write('from conf import *\n')
    runfile.write('from simian.engine import GameEngine\n\n')
    runfile.write('engine = GameEngine()\n')
    runfile.write('engine.load(GAME_NAME, WINDOW_SIZE)\n')
    runfile.write('[engine.add(scene) for scene in SCENE_LIST]\n')
    runfile.write('engine.set(INITIAL_SCENE)\n')
    runfile.write('engine.run()\n')
