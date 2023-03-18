from sys import argv
from core import error_found


def main(args: list = []):
    pass


if __name__ == '__main__':
    try:
        if len(argv) > 1:
            main(argv[1:])
        main()
    except Exception as err:
        error_found(err)
