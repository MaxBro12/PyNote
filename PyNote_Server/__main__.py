from sys import argv
from core import error_found


def main(args: list = []):
    pass


if __name__ == '__main__':
    try:
        argv.pop()
        main(argv)
    except Exception as err:
        error_found(err)
