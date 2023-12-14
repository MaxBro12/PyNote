from fastapi import APIRouter
from sql import DataBase, UserData
from core import read_toml, create_log

from settings import FILE_DB, FILE_SETTINGS

router = APIRouter()
db = DataBase(FILE_DB)
config = read_toml(FILE_SETTINGS)


@router.post('/user')
def new_user(token: str, username: str, password: str):
    if config['token'] == token:
        if username in db.users:
            return {'msg': 'exist'}
        else:
            uid = db.create_id()
            db.add_user(UserData(uid, username, password))
            return {'msg': 'All good'}
    create_log('Try to connect with WRONG TOKEN', 'info')
    return {'msg': 'Wrong token'}


@router.delete('/user')
def delete_user(token: str, username: str, password: str):
    if config['token'] == token:
        user = db.get_user(username)
        if user is not None:
            if user.password == password:
                db.remove_user(user.id)
                return {'msg': f'User {username} DELETED'}
            return {'msg': 'Wrong password!'}
        return {'msg': 'User not found'}
    create_log('Try to connect with WRONG TOKEN', 'info')
    return {'msg': 'Wrong token'}