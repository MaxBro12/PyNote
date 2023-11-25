"""from core import (
    create_log,
    get_files,
    load_file,
    create_file,
    save_file,
    rename_file,
    delete_file,

    pjoin,
)


from settings import (
    DIR_NOTES,
    NOTE_EXT,
)
from spec_types import (
    Note,
)


def get_local_notes() -> list:
    return list(map(lambda x: {
        'name': x.removesuffix(NOTE_EXT)
    }, get_files(DIR_NOTES)))


def add_local_note(name: str, inner: str) -> bool:
    return create_file(pjoin(DIR_NOTES, name + NOTE_EXT), inner)


def save_local_note(name: str, inner: str = '') -> bool:
    if inner != '':
        return save_file(pjoin(DIR_NOTES, name + NOTE_EXT), inner)
    return False


def rename_local_note(last_name: str, new_name: str) -> bool:
    return rename_file(
        pjoin(DIR_NOTES, last_name + NOTE_EXT),
        pjoin(DIR_NOTES, new_name + NOTE_EXT)
    )


def load_local_note(name: str) -> str:
    return load_file(pjoin(DIR_NOTES, name + NOTE_EXT))


def remove_local_note(name: str) -> bool:
    return delete_file(pjoin(DIR_NOTES, name + NOTE_EXT))
"""