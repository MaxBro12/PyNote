from os import path


from core import get_files, load_file


from settings import fold_notes


def add_note(name: str):
    pass


def remove_note(name: str):
    pass


def save_note(name: str):
    pass


def get_notes() -> list:
    # lst = get_files(fold_notes)
    # lst = list(map(lambda x: path.splitext(x)[0], lst))
    return list(map(lambda x: path.splitext(x)[0], get_files(fold_notes)))
