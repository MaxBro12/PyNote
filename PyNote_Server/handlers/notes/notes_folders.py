from core import (
    create_folder,
    delete_folder,

    create_file,
    delete_file,

    pjoin,
)


from settings import fold_notes, Notes_dict


def create_userfolder(user: str) -> bool:
    return create_folder(pjoin(fold_notes, user))


def create_note(user: str, data: Notes_dict) -> bool:
    return create_file(
        pjoin(fold_notes, user, data['name']), data['inner']
    )


def delete_userfolder(user: str) -> bool:
    return delete_folder(
        pjoin(fold_notes, user)
    )


def delete_note(user: str, note_name: str) -> bool:
    return delete_file(
        pjoin(fold_notes, user, note_name)
    )
