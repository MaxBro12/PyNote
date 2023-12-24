from fastapi import APIRouter

from sql import DataBase, UserData, NoteData
from core import (
    create_userfolder,
    create_note,
    delete_userfolder,
    delete_note,
)

from .services import check_access, correct_token

from settings import FILE_DB, FILE_SETTINGS

router = APIRouter()
db = DataBase(FILE_DB)


@router.get('/notes')
def all_notes(token: str, username: str, password: str):
    user = check_access(token, username, password)
    if type(user) == UserData:
        return db.get_notes(user.id)
    else:
        return user


@router.post('/notes')
def add_note(token: str, username: str, password: str, note: str, inner: str):
    user = check_access(token, username, password)
    if type(user) == UserData:
        db.add_note(NoteData(user.id, note))
        create_userfolder(user.id)
        create_note(user.id, note, inner)
        return {'msg': f'Note {note} DELETED'}
    else:
        return user


@router.delete('/notes')
def delete_user(token: str, username: str, password: str, note: str):
    user = check_access(token, username, password)
    if type(user) == UserData:
        db.remove_note(NoteData(user.id, note))
        delete_note()
        return {'msg': f'Note {note} DELETED'}
    else:
        return user