from server import (
    api_save_note,
    api_get_notes,
    api_delete_note,
)
from core import (
    create_log_file,
    create_file,
    load_file,

    get_files,
    pjoin,
)


from settings import (
    fold_notes,
)
from spec_types import (
    User_Data,
    Delete_Note,
)


def sent_notes(host: str, user: User_Data):
    for i in get_files(pjoin(fold_notes)):
        if not api_save_note(host, {
            'id': user['id'],
            'username': user['username'],
            'password': user['password'],
            'token': user['token'],
            'name': i,
            'inner': load_file(pjoin(fold_notes, i))
        }):
            create_log_file("Can't sent data to server", 'error')


def upload_notes(host: str, user: User_Data):
    files = api_get_notes(host, user)
    if files is not None:
        for f in files:
            if not create_file(pjoin(fold_notes, f['name']), f['inner']):
                create_log_file(f"Can't create note {f['name']}", 'error')


def serv_delete_note(host: str, note: Delete_Note):
    if not api_delete_note(host, note):
        create_log_file(f"Can't delete note {note['name']}", 'error')
