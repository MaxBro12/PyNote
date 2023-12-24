from fastapi import APIRouter
from sql import DataBase, UserData
from core import read_toml, create_log

from .services import check_access, correct_token

from settings import FILE_DB, FILE_SETTINGS

router = APIRouter()
db = DataBase(FILE_DB)


@router.post('/user')
def new_user(token: str, username: str, password: str):
    if correct_token(token):
        if username in db.users:
            return {'msg': 'exist'}
        else:
            uid = db.create_id()
            db.add_user(UserData(uid, username, password))
            return {'msg': 'All good'}
    return {'msg': 'Wrong token'}


@router.delete('/user')
def delete_user(token: str, username: str, password: str):
    user = check_access(token, username, password)
    if type(user) == UserData:
        db.remove_user(user.id)
        return {'msg': f'User {username} DELETED'}
    else:
        return user