from server import (
    api_create_user,
    api_check_user,
    api_login_user,
)
from core import create_log_file


from settings import (
    User_Data,
    Load_User,

    Config_server,
)


def create_user(server: Config_server, user: Load_User) -> User_Data | None:
    data = api_create_user(server['host'], server['token'], user)
    if type(data) == User_Data:
        return data
    else:
        return None


def login_user(server: Config_server, user: Load_User) -> User_Data | None:
    data = api_login_user(server['host'], server['token'], user)
    if type(data) == User_Data:
        return data
    else:
        return None
