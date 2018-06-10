import argparse
import os
from simian.cli.regex import validate_project_name
from simian.utils.project import create_project


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('option', help='siamian options')
    parser.add_argument('arg_option',
                        help='option arguments [game_name, run.py]')

    args = parser.parse_args()

    if args.option == 'startproject':
        project_name = args.arg_option
        if validate_project_name(project_name):
            create_project(project_name)
        else:
            raise NameError(f'Invalid project name "{project_name}"')
    elif args.option == 'runproject':
        os.system(f'python {args.arg_option}')
    else:
        raise ValueError(f'Invalid command "{args.option}"')
