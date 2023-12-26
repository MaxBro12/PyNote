from requests import get, post, delete

from core import create_log
from .services import url, server_get_status

from settings import (
    SERVER_NOTES,
)
from spec_types import (
    Note,
    User
)


def server_get_notes(host: str, user: User) -> list[Note]:
    if server_get_status(host):
        return list(map(lambda x: Note(x['name'], x['inner']), get(url(host, SERVER_NOTES), params={
            'token': user.token,
            'username': user.username,
            'password': user.password
        }).json()))
    return []


def server_add_note(host: str, user: User, note: Note) -> bool:
    if server_get_status(host):
        return True if post(url(host, SERVER_NOTES), params={
            'token': user.token,
            'username': user.username,
            'password': user.password,
            'note': note.name,
            'inner': note.inner
        }).json()['msg']  == f'Note {note.name} CREATED' else False
    return False


def server_delete_note(host: str, user: User, note: Note) -> bool:
    if server_get_status(host):
        return True if delete(url(host, SERVER_NOTES), params={
            'token': user.token,
            'username': user.username,
            'password': user.password,
            'note': note.name,
        }).json()['msg'] == f'Note {note.name} DELETED' else False 
    return False
