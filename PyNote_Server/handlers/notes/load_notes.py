from core import get_files, load_file, pjoin


from settings import fold_notes, Notes_dict


def get_notes(username: str) -> list[Notes_dict]:
    files = get_files(pjoin(fold_notes, username))
    data = list()
    for i in files:
        data.append(
            {
                'name': i,
                'inner': load_file(pjoin(fold_notes, username, i))
            }
        )
    return data
