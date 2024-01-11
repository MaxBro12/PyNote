from requests import post, delete

from core import create_log
from .services import url, server_get_status

from spec_types import User
from settings import (
    SERVER_USER,
)


def server_new_user(host: str, user: User) -> bool:
    if server_get_status(host):
        return True if post(url(host, SERVER_USER), json={
            'token': user.token,
            'username': user.username,
            'password': user.password
        }).json()['msg'] == 'All good' else False
    return False


def server_delete_user(host: str, user: User) -> bool:
    if server_get_status(host):
        return True if delete(url(host, SERVER_USER), json={
            'token': user.token,
            'username': user.username,
            'password': user.password
        }).json()['msg'] == f'User {user.username} DELETED' else False
    return False
