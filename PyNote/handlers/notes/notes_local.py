from core import (
    create_log_file,
    get_files,
    load_file,

    pjoin
)


from settings import (
    fold_notes,
    Note,
)


def get_local_notes() -> list[Note]:
    return list(map(lambda x: {
        'name': x, 'inner': load_file(pjoin(fold_notes, x))
    }, get_files(fold_notes)))
