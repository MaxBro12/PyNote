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
    Note,
)


def get_local_notes() -> list[Note]:
    return list(map(lambda x: {
        'name': x, 'inner': load_file(pjoin(fold_notes, x))
    }, get_files(fold_notes)))


def add_local_note(name: str) -> bool:
    return create_file(pjoin(fold_notes, name + '.txt'))
    # https://ru.stackoverflow.com/questions/1295971/%D0%94%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82%D0%BE%D0%B2


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
