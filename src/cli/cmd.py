import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('option', help='siamian options')
    parser.add_argument('arg_option', help='name of your game')

    args = parser.parse_args()
    if args.option == 'startgame':
        print(f'creating new game project {args.game_name}')
    elif args.option == 'rungame':
        print(f'running {args.arg_option}')
        os.system(f'python {args.arg_option}')