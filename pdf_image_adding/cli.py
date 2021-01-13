import argparse
import sys


def main(args):
    print(args.file_name)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    sys.exit(main(args))
