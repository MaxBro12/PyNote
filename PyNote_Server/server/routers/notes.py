from fastapi import APIRouter

from sql import DataBase, UserData, NoteData
from core import read_toml, create_log

from settings import FILE_DB, FILE_SETTINGS

router = APIRouter()
db = DataBase(FILE_DB)
config = read_toml(FILE_SETTINGS)


@router.get('/notes')
def all_notes(token: str, username: str, password: str):
    if config['token'] == token:
        user = db.get_user(username)
        if user is not None:
            if user.password == password:
                return db.get_notes(user.id)
            return {'msg': 'Wrong password!'}
        return {'msg': 'User not found'}
    create_log('Try to connect with WRONG TOKEN', 'info')
    return {'msg': 'Wrong token'}


@router.delete('/notes')
def delete_user(token: str, username: str, password: str, note: str):
    if config['token'] == token:
        user = db.get_user(username)
        if user is not None:
            if user.password == password:
                db.remove_note(NoteData(user.id, note))
                return {'msg': f'Note {note} DELETED'}
            return {'msg': 'Wrong password!'}
        return {'msg': 'User not found'}
    create_log('Try to connect with WRONG TOKEN', 'info')
    return {'msg': 'Wrong token'}