import argparse
import os
from simian.cli.regex import validate_project_name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('option', help='siamian options')
    parser.add_argument('arg_option', help='option arguments [game_name, run.py]')

    args = parser.parse_args()
    if args.option == 'startgame':
        project_name = args.arg_option
        print(validate_project_name(project_name))
        if validate_project_name(project_name):
            print('wow')
            create_project(project_name)
        else:
            raise NameError(f'Invalid project name {project_name}')

    elif args.option == 'rungame':
        print(f'running {args.arg_option}')
        os.system(f'python {args.arg_option}')


def create_project(project_name):
    os.mkdir(project_name)
    os.chdir(project_name)
    os.mkdir('scenes')
    os.mkdir('game_objects')
    