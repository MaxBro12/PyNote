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
from .debug import create_log

from settings import DIR_NOTES


def create_userfolder(uid: int):
    way = pjoin(DIR_NOTES, str(uid))
    if not wayfinder(way):
        create_folder(way)
        create_log(f'Create userdir {uid}')


def create_note(uid: int, notename: str, inner: str):
    create_userfolder(uid)
    create_file(pjoin(DIR_NOTES, str(uid), notename), inner)
    create_log(f'Create note {notename} user {uid}', 'debug')


def delete_userfolder(uid):
    way = pjoin(DIR_NOTES, str(uid))
    if wayfinder(way):
        remove_dir_tree(way)
        create_log(f'Remove userdir {uid}', 'debug')


def delete_note(uid, note: str):
    way = pjoin(DIR_NOTES, str(uid), note)
    if wayfinder(way):
        delete_file(way)
        create_log(f'Remove note {note} from {uid}', 'debug')
