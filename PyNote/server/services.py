from requests import get, exceptions

from core import create_log

from settings import SERVER_STATUS


def server_get_status(host: str) -> bool:
    try:
        return True if get(url(host, SERVER_STATUS)).json()['msg'] == 'All good' else False
    except exceptions.Timeout:
        create_log(f'Server timeout! {host}', 'error')
        return False
    except exceptions.ConnectionError:
        create_log(f'Connect to server FAILD {host}', 'error')
        return False


def url(*links: str) -> str:
    """Создает url по заданным точкам"""
    return '/'.join(links)
