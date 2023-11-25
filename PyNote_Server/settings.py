from typing import Final


# ! Основное
DIR_DATA: Final = 'server_data'

FILE_SETTINGS: Final = f'{DIR_DATA}/settings.toml'
FILE_SETTINGS_IN: Final = {
    'SERVER': {
        'HOST': "",
        'PORT': "",
        'TOKEN': "",
        'DEBUG': "",
    },
}

FILE_LOGGER = f'{DIR_DATA}/logger.log'
FILE_ERROR = f'{DIR_DATA}/error.log'

FILE_DB = f'{DIR_DATA}/base.db'

DIR_NOTES = f'{DIR_DATA}/notes'


# ! SQL
CREATE_TABLE: Final = """CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT NOT NULL);"""

# table_get_users = """SELECT username from users"""
# table_get_id = """SELECT id from users"""

"""
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
"""