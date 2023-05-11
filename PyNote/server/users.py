from requests import get, post, exceptions


from core import create_log_file


from .urls import url


from settings import (
    api_new,
    api_usr,
)
from spec_types import (
    Load_User,
    User_Data,
    Server_Log,
)


def api_check_user(host: str, key: str, name: str) -> bool:
    try:
        return True if get(url(host, key, api_new, name)).json()['log'] \
            else False
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return False
    except KeyError:
        create_log_file('Server dont undestend request', 'error')
        return False


def api_create_user(host: str, key: str, user: Load_User) \
        -> User_Data | Server_Log:
    try:
        return post(
            url(host, key, api_new, user['username']), data=user
        ).json()
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return {'log': 'timeout'}


def api_login_user(host: str, key: str, user: Load_User) \
        -> User_Data | Server_Log:
    try:
        return get(
            url(host, key, api_usr, user['username']), data=user
        ).json()
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return {'log': 'timeout'}
