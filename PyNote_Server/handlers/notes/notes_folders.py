from core import create_file, create_folder, pjoin


from settings import fold_notes


def create_userfolder(user: str) -> bool:
    return create_folder(pjoin(fold_notes, user))


def create_notes(user: str, data: dict[dict, str]) -> bool:
    # for note in data.keys():
    #     create_file(pjoin(fold_notes, user, note['name']), note['data'])

    return True if all(
        map(lambda x: create_file(
            pjoin(fold_notes, user, x['name']), x['data']
        ), data.keys())
    ) else False


def delete_userfolder(user: str) -> bool:
    pass


def delete_note(user: str) -> bool:
    pass
