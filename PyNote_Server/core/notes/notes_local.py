from core.filemanage import (
    get_files,
    load_file,
    create_file,
    save_file,
    rename_file,
    delete_file,

    wayfinder,
    pjoin,
)
from .notes_users import create_userdir


from settings import (
    DIR_NOTES,
)


def get_user_notes(username: str) -> list:
    if not wayfinder(pjoin(DIR_NOTES, username)):
        create_userdir(username)
    return list(map(lambda x: {
        'name': x,
        'inner': load_file(pjoin(DIR_NOTES, username, x))
    }, get_files(pjoin(DIR_NOTES, username))))


def add_note(username: str, name: str, inner: str) -> bool:
    if not wayfinder(pjoin(DIR_NOTES, username)):
        create_userdir(username)
    return create_file(pjoin(DIR_NOTES, username, name), inner)


def delete_note(username: str, name: str) -> bool:
    return delete_file(pjoin(DIR_NOTES, username, name))


# def save_local_note(name: str, inner: str = '') -> bool:
#     if inner != '':
#         return save_file(pjoin(DIR_NOTES, name + NOTE_EXT), inner)
#     return False


def rename_note(username: str, last_name: str, new_name: str) -> bool:
    return rename_file(
        pjoin(DIR_NOTES, username, last_name),
        pjoin(DIR_NOTES, username, new_name)
    )


# def load_local_note(name: str) -> str:
#     return load_file(pjoin(DIR_NOTES, name + NOTE_EXT))
