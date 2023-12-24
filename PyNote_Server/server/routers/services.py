from sql import DataBase, UserData
from core import read_toml, create_log

from settings import FILE_DB, FILE_SETTINGS


db = DataBase(FILE_DB)
config = read_toml(FILE_SETTINGS)


def correct_token(token: str) -> bool:
    """Проверяем наличие правильного токена """
    if config['SERVER']['TOKEN'] == token:
        return True
    create_log('Try to connect with WRONG TOKEN', 'info')
    return False


def check_access(token: str, username: str, password: str) -> UserData | dict:
    if correct_token(token):
        user = db.get_user(username)
        if user is not None:
            if user.password == password:
                return user
            return {'msg': 'Wrong password!'}
        return {'msg': 'User not found'}
    return {'msg': 'Wrong token'}
