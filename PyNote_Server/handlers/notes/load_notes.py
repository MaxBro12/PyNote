from core import get_files, create_file, load_file, pjoin


from settings import fold_notes


def get_notes(username: str) -> dict:
    files = get_files(pjoin(fold_notes, username))
    data = {}
    for i in files:
        data[i] = load_file(pjoin(fold_notes, username, i))
    return data
