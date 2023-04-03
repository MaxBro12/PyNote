
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
api_user_data = "/usr/<int:id>"
