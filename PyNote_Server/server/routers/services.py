from sql import UserData, db_get_user
from core import read_toml, create_log

from settings import FILE_SETTINGS


config = read_toml(FILE_SETTINGS)


def correct_token(token: str) -> bool:
    """Проверяем наличие правильного токена """
    if config['SERVER']['TOKEN'] == token:
        return True
    create_log('Try to connect with WRONG TOKEN', 'info')
    return False


async def check_access(token: str, username: str, password: str) -> UserData | dict:
    if correct_token(token):
        user = await db_get_user(username)
        if user is not None:
            if user.password == password:
                return user
            create_log(f'Try to get {username} with WRONG PASSWORD', 'info')
            return {'msg': 'Wrong password!'}
        create_log(f'No such user with name {username}', 'info')
        return {'msg': 'User not found'}
    return {'msg': 'Wrong token'}
