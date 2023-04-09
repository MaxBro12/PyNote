from requests import get, post, delete, exceptions


from core import create_log_file


from .urls import url


from settings import (
    api_notes,
    Note,
    Get_User_Note,
    Post_Note,
    Delete_Note,

    User_Data,
    UserNote
)


def api_get_notes(host: str, key: str, data: User_Data) -> list[Note] | None:
    try:
        return get(url(host, key, api_notes), data=data).json()['log']
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return None


def api_save_note(host: str, key: str, data: UserNote) -> bool:
    try:
        return True if post(
            url(host, key, api_notes), data=data
        ).json()['log'] else False
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return False
    except KeyError:
        create_log_file('Server dont undestend request', 'error')
        return False


def api_delete_note(host: str, key: str, data: Delete_Note) -> bool:
    try:
        return True if delete(
            url(host, key, api_notes), data=data
        ).json()['log'] else False
    except exceptions.Timeout:
        create_log_file('Server timeout!', 'error')
        return False
    except KeyError:
        create_log_file('Server dont undestend request', 'error')
        return False
