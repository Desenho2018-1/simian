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
    with open('run.py', 'a') as runfile:
        runfile.write('print("Simian 2D Engine")')
