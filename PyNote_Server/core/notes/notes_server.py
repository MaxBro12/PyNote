from server import (
    api_save_note,
    api_get_notes,
    api_delete_note,
)
from core import (
    create_log,
    create_file,
    load_file,

    get_files,
    pjoin,
)


from settings import (
    DIR_NOTES,
)
from spec_types import (
    User_Data,
    Delete_Note,
)


def sent_notes(host: str, user: User_Data):
    for i in get_files(pjoin(DIR_NOTES)):
        if not api_save_note(host, {
            'id': user['id'],
            'username': user['username'],
            'password': user['password'],
            'token': user['token'],
            'name': i,
            'inner': load_file(pjoin(DIR_NOTES, i))
        }):
            create_log("Can't sent data to server", 'error')


def upload_notes(host: str, user: User_Data):
    files = api_get_notes(host, user)
    if files is not None:
        for f in files:
            if not create_file(pjoin(DIR_NOTES, f['name']), f['inner']):
                create_log(f"Can't create note {f['name']}", 'error')


def serv_delete_note(host: str, note: Delete_Note):
    if not api_delete_note(host, note):
        create_log(f"Can't delete note {note['name']}", 'error')
