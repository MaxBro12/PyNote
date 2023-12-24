from .filemanage import (
    create_file,
    create_folder,

    delete_file,
    delete_folder,

    load_file,

    remove_dir_tree,

    wayfinder,
    pjoin,
)

from settings import DIR_NOTES


def create_userfolder(uid: int):
    way = pjoin(DIR_NOTES, str(uid))
    if not wayfinder(way):
        create_folder(way)


def create_note(uid: int, notename: str, inner: str):
    create_userfolder(uid)
    create_file(pjoin(DIR_NOTES, str(uid), notename), inner)


def delete_userfolder(uid):
    way = pjoin(DIR_NOTES, str(uid))
    if wayfinder(way):
        remove_dir_tree(way)


def delete_note(uid, note: str):
    way = pjoin(DIR_NOTES, str(uid), note)
    if wayfinder(way):
        delete_file(way)
