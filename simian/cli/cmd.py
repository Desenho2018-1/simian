import argparse
import os

from cookiecutter.main import cookiecutter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('option', help='siamian options [startproject, run]')

    args = parser.parse_args()

    if args.option == 'startproject':
        template_path = os.path.dirname(os.path.dirname(os.path.dirname(
                                        os.path.abspath(__file__))))
        cookiecutter(template_path + '/cookiecutter')
    elif args.option == 'run':
        os.system(f'python run.py')
    else:
        raise ValueError(f'Invalid command "{args.option}"')
