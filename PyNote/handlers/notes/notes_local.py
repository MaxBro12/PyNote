from core import (
    create_log_file,
    get_files,
    load_file,
    create_file,
    save_file,
    rename_file,
    delete_file,

    pjoin,
)


from settings import (
    fold_notes,
)
from spec_types import (
    Note,
)


def get_local_notes() -> list[Note]:
    return list(map(lambda x: {
        'name': x, 'inner': load_file(pjoin(fold_notes, x))
    }, get_files(fold_notes)))


def add_local_note(name: str) -> bool:
    return create_file(pjoin(fold_notes, name + '.txt'))


def save_local_note(name: str, inner: str = '') -> bool:
    if inner != '':
        return save_file(pjoin(fold_notes, name + '.txt'), inner)
    return False


def rename_local_note(last_name: str, new_name: str) -> bool:
    return rename_file(
        pjoin(fold_notes, last_name + '.txt'),
        pjoin(fold_notes, new_name + '.txt')
    )


def remove_local_note(name: str) -> bool:
    return delete_file(pjoin(fold_notes, name + '.txt'))
