from requests import get, post, exceptions


from core import create_log_file


from .urls import url


from settings import (
    api_new,
    api_usr,

    Load_User,
    User_Data
)


def api_check_user(host: str, name: str) -> bool:
    try:
        return True if get(url(host, api_new, name)).json()['log'] \
            else False
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return False
    except KeyError:
        create_log_file('Server dont undestend request', 'error')
        return False


def api_create_user(host: str, user: Load_User) -> User_Data | None:
    try:
        return post(
            url(host, api_new, user['username']), data=user
        ).json()
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return None


def api_login_user(host: str, user: Load_User) -> User_Data | None:
    try:
        return get(
            url(host, api_usr, user['username']), data=user
        ).json()
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return None
