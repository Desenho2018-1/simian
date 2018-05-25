##### SIMIAN COMMAND LINE INTERFACE #####
import sys


def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("usage: ...")
