from typing import TypedDict
# ! Основное
fold_data = 'server_data'

file_conf = f'{fold_data}/settings.toml'

file_conf_inner = {
    'app': {
        'width': 500,
        'height': 500,
    },
    'user': {
        'id': 0,
        'token': 0,
    }
}

file_log = f'{fold_data}/logger.log'
file_error = f'{fold_data}/error.log'

file_db = f'{fold_data}/base.db'

fold_notes = f'{fold_data}/notes'


# ! SQL
file_db = f'{fold_data}/data.db'
table = """CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT NOT NULL);"""

table_get_users = """SELECT username from users"""
table_get_id = """SELECT id from users"""

token_len = 20


# ! Flask
debug = False
port = 3334
host = "127.0.0.1"

api_new_user_1 = "/new/<string:user>"
api_new_user_2 = "/new/"
api_new_user_3 = "/new"

api_user_data_1 = "/usr/<string:user>"
api_user_data_2 = "/usr/"
api_user_data_3 = "/usr"

api_notes_1 = "/note/<string:user>"
api_notes_2 = "/note/"
api_notes_3 = "/note"


# ! Доп классы
class User_Dict(TypedDict):
    id: int
    username: str
    password: str
    token: str


class Notes_dict(TypedDict):
    name: str
    inner: str
